#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-platform website scraping and recursive crawling engine to clean Markdown.
Includes Automatic Hardware Profiler (CPU & RAM inspection) and Adaptive Eco Throttling
to guarantee low CPU and RAM footprint on the host machine.

Motor multiplataforma de captura e rastreamento recursivo de websites para Markdown limpo.
Inclui Perfilador Automático de Hardware (inspeção de CPU e RAM) e Controle Adaptativo Eco
para garantir baixo consumo de CPU e memória RAM na máquina operante.
"""
import argparse
import ctypes
import gc
import json
import os
import platform
import re
import shutil
import sys
import tarfile
import tempfile
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen

# Force UTF-8 on Windows console outputs / Força UTF-8 nas saídas de console no Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

# Extensions to skip during recursive crawling / Extensões ignoradas durante o crawling recursivo
IGNORED_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".bmp",
    ".pdf", ".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".rar",
    ".mp3", ".mp4", ".webm", ".ogg", ".wav", ".avi", ".mov",
    ".css", ".js", ".mjs", ".map", ".woff", ".woff2", ".ttf", ".eot",
    ".xml", ".rss", ".atom", ".json", ".exe", ".dmg", ".deb", ".rpm",
}

# Default CSS selectors for main documentation content / Seletores CSS padrão para conteúdo principal
MAIN_CONTENT_SELECTORS = [
    "#layout-content",          # php.net manual main content
    "main article",
    "article.markdown-body",
    ".markdown-body",
    "article[role='main']",
    "div[role='main']",
    "main",
    "article",
    ".docs-content",
    ".doc-content",
    "#content",
    ".content",
]

# Noise selectors removed before Markdown conversion / Seletores de ruído removidos antes da conversão
NOISE_SELECTORS = [
    "nav", "header", "footer", "aside", "script", "style", "noscript", "iframe",
    ".navbar", ".sidebar", ".toc", ".breadcrumb", ".breadcrumbs", ".pagination",
    ".cookie-banner", "#cookie-banner", ".ads", ".advertisement",
    "#usernotes",               # php.net user contributed notes (optional noise)
    ".headsup", ".ChangeLanguage", ".page-tools", ".edit-bug", "#trick",
    "#goto", "#breadcrumbs", ".layout-menu", ".contribute",
]


# ==============================================================================
# HARDWARE PROFILER & ADAPTIVE ECO GOVERNOR / PERFILADOR DE HARDWARE & MODO ECO
# ==============================================================================

def get_cpu_model_name() -> str:
    """
    Detects the human-readable CPU model name across Windows, Linux, and macOS.
    Detecta o nome legível do modelo do processador no Windows, Linux e macOS.
    """
    try:
        if sys.platform == "win32":
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"HARDWARE\DESCRIPTION\System\CentralProcessor\0",
            )
            model, _ = winreg.QueryValueEx(key, "ProcessorNameString")
            winreg.CloseKey(key)
            if model:
                return model.strip()
        elif sys.platform.startswith("linux"):
            with open("/proc/cpuinfo", "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":", 1)[1].strip()
        elif sys.platform == "darwin":
            import subprocess
            out = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"], text=True, timeout=3)
            if out:
                return out.strip()
    except Exception:
        pass
    return platform.processor() or "Generic CPU"


def get_system_memory_info() -> dict:
    """
    Returns real-time physical RAM metrics: total_gb, avail_gb, used_percent.
    Retorna métricas reais de memória RAM física: total_gb, avail_gb, used_percent.
    """
    try:
        if sys.platform == "win32":
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ("dwLength", ctypes.c_ulong),
                    ("dwMemoryLoad", ctypes.c_ulong),
                    ("ullTotalPhys", ctypes.c_ulonglong),
                    ("ullAvailPhys", ctypes.c_ulonglong),
                    ("ullTotalPageFile", ctypes.c_ulonglong),
                    ("ullAvailPageFile", ctypes.c_ulonglong),
                    ("ullTotalVirtual", ctypes.c_ulonglong),
                    ("ullAvailVirtual", ctypes.c_ulonglong),
                    ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
                ]
            stat = MEMORYSTATUSEX()
            stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
                total_gb = stat.ullTotalPhys / (1024 ** 3)
                avail_gb = stat.ullAvailPhys / (1024 ** 3)
                return {
                    "total_gb": round(total_gb, 2),
                    "avail_gb": round(avail_gb, 2),
                    "used_percent": int(stat.dwMemoryLoad),
                }
        elif sys.platform.startswith("linux"):
            mem = {}
            with open("/proc/meminfo", "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    parts = line.split(":")
                    if len(parts) == 2:
                        k = parts[0].strip()
                        v = int(parts[1].strip().split()[0]) * 1024
                        mem[k] = v
            total = mem.get("MemTotal", 4 * 1024 ** 3)
            avail = mem.get("MemAvailable", mem.get("MemFree", 2 * 1024 ** 3))
            used_pct = int(round((1.0 - (avail / total)) * 100)) if total else 50
            return {
                "total_gb": round(total / (1024 ** 3), 2),
                "avail_gb": round(avail / (1024 ** 3), 2),
                "used_percent": used_pct,
            }
    except Exception:
        pass

    try:
        import psutil
        vm = psutil.virtual_memory()
        return {
            "total_gb": round(vm.total / (1024 ** 3), 2),
            "avail_gb": round(vm.available / (1024 ** 3), 2),
            "used_percent": int(vm.percent),
        }
    except Exception:
        return {"total_gb": 8.0, "avail_gb": 4.0, "used_percent": 50}


def apply_low_cpu_priority():
    """
    Lowers the OS scheduling priority of the current Python process so the host UI/IDE never lags.
    Reduz a prioridade de escalonamento do processo Python atual no SO para nunca travar a máquina.
    """
    try:
        if sys.platform == "win32":
            # BELOW_NORMAL_PRIORITY_CLASS = 0x00004000
            handle = ctypes.windll.kernel32.GetCurrentProcess()
            ctypes.windll.kernel32.SetPriorityClass(handle, 0x00004000)
        elif hasattr(os, "nice"):
            os.nice(10)
    except Exception:
        pass


def detect_hardware_budget(requested_workers: int = 0, requested_delay_ms: int = -1, max_ram_percent: int = 78) -> dict:
    """
    Inspects CPU and RAM and calculates a conservative execution budget.
    Inspeciona CPU e RAM e calcula um orçamento de execução conservador.
    """
    apply_low_cpu_priority()
    cpu_model = get_cpu_model_name()
    cpu_cores = os.cpu_count() or 2
    mem = get_system_memory_info()
    avail_gb = mem["avail_gb"]
    used_pct = mem["used_percent"]

    # Conservative auto-calculation / Cálculo automático conservador (Eco-First)
    if avail_gb < 2.5 or used_pct >= max_ram_percent or cpu_cores <= 2:
        safe_workers = 1
        batch_size = 15
        default_delay_ms = 80
        tier = "ECO-ESTRITO (Baixa RAM/CPU disponível)"
    elif avail_gb < 5.0 or cpu_cores <= 6:
        safe_workers = 1 if used_pct > 65 else 2
        batch_size = 25
        default_delay_ms = 45
        tier = "ECO-MODERADO (Uso equilibrado)"
    else:
        # Even on 12+ core / 16GB+ machines, cap at max 2-3 threads (~16-25% CPU) to keep system cool
        # Mesmo em máquinas de 12+ núcleos / 16GB+, limita a 2-3 threads (~16-25% da CPU)
        safe_workers = 2 if cpu_cores <= 12 else 3
        batch_size = 35
        default_delay_ms = 25
        tier = "ECO-ADAPTATIVO (Máquina potente, limite de segurança de ~20% CPU)"

    final_workers = requested_workers if requested_workers > 0 else safe_workers
    # Never exceed 50% of logical cores unless explicitly forced / Protege contra sobrecarga
    final_workers = max(1, min(final_workers, max(1, cpu_cores // 2)))
    final_delay_ms = requested_delay_ms if requested_delay_ms >= 0 else default_delay_ms

    return {
        "cpu_model": cpu_model,
        "cpu_cores": cpu_cores,
        "total_ram_gb": mem["total_gb"],
        "avail_ram_gb": avail_gb,
        "ram_used_percent": used_pct,
        "workers": final_workers,
        "batch_size": batch_size,
        "delay_ms": final_delay_ms,
        "max_ram_percent": max_ram_percent,
        "tier": tier,
    }


def guard_memory_pressure(budget: dict):
    """
    Checks live RAM usage between batches; forces garbage collection and sleeps if memory is high.
    Verifica o uso de RAM em tempo real entre lotes; força coleta de lixo e pausa se a memória subir.
    """
    gc.collect()
    mem = get_system_memory_info()
    if mem["used_percent"] >= budget["max_ram_percent"] or mem["avail_gb"] < 1.2:
        print(
            f"   🛡️ [PROTEÇÃO DE RAM] Uso atual em {mem['used_percent']}% "
            f"({mem['avail_gb']} GB livres). Pausando 1.5s e liberando memória..."
        )
        gc.collect()
        time.sleep(1.5)
    elif budget["delay_ms"] > 0:
        time.sleep(budget["delay_ms"] / 1000.0)


# ==============================================================================
# URL & HTML PROCESSING FUNCTIONS / FUNÇÕES DE PROCESSAMENTO DE URL E HTML
# ==============================================================================

def get_scope_prefix(root_url: str) -> str:
    """
    Determines the URL prefix scope so recursive crawls stay inside the target directory.
    Determina o prefixo de escopo da URL para que o crawl recursivo permaneça no diretório alvo.
    """
    parsed = urlparse(root_url)
    path = parsed.path
    if not path or path == "/":
        base_path = "/"
    elif path.endswith("/"):
        base_path = path
    else:
        last_segment = path.rsplit("/", 1)[-1]
        if "." in last_segment:
            base_path = path.rsplit("/", 1)[0] + "/"
        else:
            base_path = path + "/"
    return urlunparse((parsed.scheme, parsed.netloc, base_path, "", "", ""))


def normalize_url(url: str) -> str:
    """
    Strips URL fragments and normalizes trailing structure.
    Remove fragmentos (#) da URL e normaliza a estrutura.
    """
    clean, _ = urldefrag(url.strip())
    parsed = urlparse(clean)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))


def url_to_md_filename(url: str, scope_prefix: str, single_mode: bool = False, file_prefix: str = "") -> str:
    """
    Converts a page URL into a deterministic, safe .md filename.
    Converte a URL de uma página em um nome de arquivo .md determinístico e seguro.
    """
    pfx = f"{file_prefix.strip('_')}__" if file_prefix else ""
    if single_mode:
        parsed = urlparse(url)
        name_part = parsed.netloc.replace(".", "_")
        path_part = parsed.path.strip("/").replace("/", "_")
        if path_part.endswith((".php", ".html", ".htm", ".asp", ".aspx")):
            path_part = path_part.rsplit(".", 1)[0]
        base = f"{name_part}_{path_part}.md" if path_part else f"{name_part}.md"
        return f"{pfx}{base}" if pfx and not base.startswith(pfx) else base

    norm = normalize_url(url)
    if norm.startswith(scope_prefix):
        rel = norm[len(scope_prefix):].strip("/")
    elif norm == scope_prefix.rstrip("/"):
        rel = ""
    else:
        parsed = urlparse(norm)
        rel = parsed.path.strip("/")

    if not rel:
        return f"{pfx}index.md"

    for ext in (".php", ".html", ".htm", ".md"):
        if rel.lower().endswith(ext):
            rel = rel[:-len(ext)]
            break

    safe = re.sub(r"[^a-zA-Z0-9._-]+", "_", rel.replace("/", "__")).strip("_")
    return f"{pfx}{safe or 'index'}.md"


def is_valid_crawl_target(
    candidate_url: str,
    scope_prefix: str,
    include_re=None,
    exclude_re=None,
) -> bool:
    """
    Checks if a discovered URL belongs to the target crawl scope and passes regex filters.
    Verifica se uma URL descoberta pertence ao escopo do crawl e passa pelos filtros regex.
    """
    if not candidate_url or candidate_url.startswith(("javascript:", "mailto:", "tel:", "data:")):
        return False

    norm = normalize_url(candidate_url)
    parsed = urlparse(norm)
    if parsed.scheme not in ("http", "https"):
        return False

    if not (norm.startswith(scope_prefix) or norm == scope_prefix.rstrip("/")):
        return False

    lower_path = parsed.path.lower()
    for ext in IGNORED_EXTENSIONS:
        if lower_path.endswith(ext):
            return False

    if include_re and not include_re.search(norm):
        return False
    if exclude_re and exclude_re.search(norm):
        return False

    return True


def clean_html_and_extract_links(
    raw_html: str,
    page_url: str,
    scope_prefix: str,
    custom_selector: str = None,
    keep_usernotes: bool = False,
    single_mode: bool = False,
    include_re=None,
    exclude_re=None,
    file_prefix: str = "",
):
    """
    Extracts valid internal links, strips layout noise, rewrites internal hrefs to .md,
    and returns (page_title, cleaned_html, discovered_links).
    Extrai links internos válidos, remove ruído de layout, reescreve hrefs internos para .md
    e retorna (titulo_da_pagina, html_limpo, links_descobertos).
    """
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(raw_html, "html.parser")

    # Strip language switchers before link discovery to avoid virtual language path loops (e.g. Apache .toplang)
    # Remove seletores de troca de idioma antes de extrair links para evitar loops virtuais de idioma
    for lang_node in soup.select(".toplang, #toplang, .language-switcher, .lang-switcher"):
        lang_node.decompose()

    title_tag = soup.find("title")
    page_title = title_tag.get_text(strip=True) if title_tag else urlparse(page_url).path

    base_tag = soup.find("base", href=True)
    effective_base_url = urljoin(page_url, base_tag["href"].strip()) if base_tag and base_tag["href"].strip() else page_url

    content_node = None
    selectors = ([custom_selector] if custom_selector else []) + MAIN_CONTENT_SELECTORS
    for sel in selectors:
        if not sel:
            continue
        found = soup.select_one(sel)
        if found and len(found.get_text(strip=True)) > 40:
            content_node = found
            break

    if content_node is None:
        content_node = soup.body or soup

    discovered_links = []
    seen_in_page = set()
    for a_tag in soup.find_all("a", href=True):
        raw_href = a_tag["href"].strip()
        if not raw_href or raw_href.startswith("#"):
            continue
        abs_url = urljoin(effective_base_url, raw_href)
        norm_url = normalize_url(abs_url)
        if is_valid_crawl_target(norm_url, scope_prefix, include_re, exclude_re):
            if norm_url not in seen_in_page:
                seen_in_page.add(norm_url)
                discovered_links.append(norm_url)

    active_noise = [
        s for s in NOISE_SELECTORS
        if not (keep_usernotes and s == "#usernotes")
    ]
    for sel in active_noise:
        for noisy in content_node.select(sel):
            noisy.decompose()

    if not single_mode:
        for a_tag in content_node.find_all("a", href=True):
            raw_href = a_tag["href"].strip()
            if not raw_href or raw_href.startswith(("javascript:", "mailto:", "tel:")):
                continue
            if raw_href.startswith("#"):
                continue
            abs_full = urljoin(effective_base_url, raw_href)
            clean_target, frag = urldefrag(abs_full)
            norm_target = normalize_url(clean_target)
            if is_valid_crawl_target(norm_target, scope_prefix, include_re, exclude_re):
                md_name = url_to_md_filename(norm_target, scope_prefix, single_mode=False, file_prefix=file_prefix)
                a_tag["href"] = f"{md_name}#{frag}" if frag else md_name
            else:
                a_tag["href"] = abs_full

    cleaned_str = str(content_node)
    soup.decompose()
    return page_title, cleaned_str, discovered_links


def html_to_markdown(cleaned_html: str) -> str:
    """
    Converts cleaned HTML fragment into formatted Markdown.
    Converte o fragmento HTML limpo em Markdown formatado.
    """
    markdown_content = ""
    try:
        import markdownify
        markdown_content = markdownify.markdownify(
            cleaned_html,
            heading_style="ATX",
            bullets="-",
            strip=["script", "style"],
        )
    except ImportError:
        try:
            from markitdown import MarkItDown
            md = MarkItDown()
            with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as tmp:
                tmp.write(cleaned_html)
                tmp_file = tmp.name
            try:
                res = md.convert(tmp_file)
                markdown_content = (
                    res.text_content
                    if hasattr(res, "text_content")
                    else getattr(res, "markdown", str(res))
                )
            finally:
                if os.path.exists(tmp_file):
                    os.remove(tmp_file)
        except Exception as e:
            raise RuntimeError(f"Nenhum conversor Markdown disponível (markdownify/markitdown): {e}")

    markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content).strip()
    return markdown_content


_META_REFRESH_RE = re.compile(
    r'<meta[^>]+http-equiv=["\']?refresh["\']?[^>]+content=["\']?\d+\s*;\s*url=([^"\'>\s]+)',
    re.IGNORECASE,
)


def fetch_html_http_with_url(url: str, timeout: int = 20, _hops: int = 0):
    """
    Fetches raw HTML via fast HTTP request (following HTTP and meta-refresh redirects) and returns (html, effective_url).
    Busca o HTML bruto via requisição HTTP rápida (seguindo redirecionamentos HTTP e meta-refresh) e retorna (html, url_efetiva).
    """
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    for attempt in range(4):
        try:
            try:
                import requests as _req_lib
                r = _req_lib.get(url, headers=headers, timeout=timeout, allow_redirects=True)
                if r.status_code in (429, 503) and attempt < 3:
                    time.sleep(1.5 * (attempt + 1))
                    continue
                if r.status_code >= 400 and not (r.status_code == 500 and len(r.text) > 2000 and "<html" in r.text.lower()):
                    from urllib.error import HTTPError
                    raise HTTPError(r.url or url, r.status_code, r.reason, r.headers, None)
                final_url = r.url or url
                raw_html = r.text
                break
            except ImportError:
                req = Request(url, headers=headers)
                with urlopen(req, timeout=timeout) as resp:
                    charset = resp.headers.get_content_charset() or "utf-8"
                    final_url = resp.geturl() or url
                    raw_html = resp.read().decode(charset, errors="replace")
                break
        except Exception as e:
            if getattr(e, "code", None) in (429, 503) and attempt < 3:
                time.sleep(1.5 * (attempt + 1))
                continue
            raise

    if _hops < 3 and len(raw_html) < 4096:
        m_ref = _META_REFRESH_RE.search(raw_html)
        if m_ref:
            next_url = urljoin(final_url, m_ref.group(1).strip())
            if next_url != final_url:
                return fetch_html_http_with_url(next_url, timeout=timeout, _hops=_hops + 1)

    return raw_html, final_url


def fetch_html_http(url: str, timeout: int = 20) -> str:
    html, _ = fetch_html_http_with_url(url, timeout=timeout)
    return html


def write_index_and_manifest(out_path: Path, root_url: str, scope_prefix: str, saved_pages: list, merge_existing: bool = False):
    """
    Generates _INDEX.md and crawl_manifest.json summarizing all captured documentation pages.
    Gera _INDEX.md e crawl_manifest.json resumindo todas as páginas de documentação capturadas.
    """
    manifest_file = out_path / "crawl_manifest.json"
    merged_pages = list(saved_pages)

    if merge_existing and manifest_file.exists():
        try:
            old_data = json.loads(manifest_file.read_text(encoding="utf-8", errors="replace"))
            existing_by_file = {p["file"]: p for p in old_data.get("pages", []) if "file" in p}
            for p in saved_pages:
                existing_by_file[p["file"]] = p
            merged_pages = sorted(existing_by_file.values(), key=lambda x: x["file"])
        except Exception:
            pass

    manifest_data = {
        "root_url": root_url,
        "scope_prefix": scope_prefix,
        "total_pages": len(merged_pages),
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "pages": merged_pages,
    }
    manifest_file.write_text(json.dumps(manifest_data, indent=2, ensure_ascii=False), encoding="utf-8")

    groups = {}
    for item in merged_pages:
        fname = item["file"]
        stem = fname[:-3] if fname.endswith(".md") else fname
        prefix = stem.split("__")[0] if "__" in stem else (stem.split(".")[0] if "." in stem else (stem.split("-")[0] if "-" in stem else "geral"))
        groups.setdefault(prefix, []).append(item)

    lines = [
        f"# 📚 Índice da Documentação / Documentation Index",
        "",
        f"- **Fonte / Source:** {root_url}",
        f"- **Escopo / Scope:** `{scope_prefix}`",
        f"- **Total de Páginas Capturadas / Total Captured Pages:** {len(merged_pages)}",
        "",
        "---",
        "",
    ]

    for group_name in sorted(groups.keys()):
        items = groups[group_name]
        lines.append(f"## 📂 `{group_name}` ({len(items)})")
        lines.append("")
        for it in items:
            lines.append(f"- [{it['title']}]({it['file']}) — `{it['url']}`")
        lines.append("")

    (out_path / "_INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    del groups, lines
    gc.collect()


# Regex patterns for low-memory streaming PHP chunked HTML conversion
# Padrões regex para conversão em streaming de baixo consumo de RAM
_TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
_LAYOUT_START_RE = re.compile(r'<div\s+id=["\']layout-content["\'][^>]*>', re.IGNORECASE)
_INTERNAL_HREF_RE = re.compile(
    r'href=(["\'])(?!(?:https?:|mailto:|javascript:|#))([^"\']+?)\.html(#[^"\']*)?\1',
    re.IGNORECASE,
)


def _convert_single_php_html(slug: str, raw_html: str, out_path: Path, scope_prefix: str) -> dict:
    """
    Converts a single php.net HTML chunk to Markdown in-place with minimal RAM allocation.
    Converte uma única página HTML do php.net para Markdown com alocação mínima de RAM.
    """
    import html as html_mod
    import markdownify

    t_match = _TITLE_RE.search(raw_html)
    title = html_mod.unescape(t_match.group(1).strip()) if t_match else slug

    m_start = _LAYOUT_START_RE.search(raw_html)
    if m_start:
        body_html = raw_html[m_start.end():]
        end_idx = body_html.rfind("</div></div></body>")
        if end_idx != -1:
            body_html = body_html[:end_idx]
    else:
        body_html = raw_html

    body_html = _INTERNAL_HREF_RE.sub(r'href=\1\2.md\3\1', body_html)

    md_body = markdownify.markdownify(
        body_html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    md_body = re.sub(r"\n{3,}", "\n\n", md_body).strip()

    page_url = f"{scope_prefix}{slug}.php"
    md_filename = f"{slug}.md"
    header = (
        f"# {title}\n\n"
        f"> **Fonte / Source:** {page_url}\n\n"
        f"---\n\n"
    )
    (out_path / md_filename).write_text(header + md_body + "\n", encoding="utf-8")
    return {"url": page_url, "file": md_filename, "title": title, "depth": 1}


def crawl_php_net_via_official_tarball(
    lang: str,
    root_url: str,
    output_dir: str,
    budget: dict,
    max_pages: int = 0,
    include_pattern: str = None,
    exclude_pattern: str = None,
    resume: bool = True,
) -> bool:
    """
    Streams the official php_manual_<lang>.tar.gz from disk in small micro-batches
    using adaptive Eco throttling so RAM stays < 100MB and CPU stays cool.
    Faz streaming do pacote oficial php_manual_<lang>.tar.gz a partir do disco em micro-lotes
    usando controle adaptativo Eco para manter a RAM < 100MB e o uso de CPU baixo.
    """
    tar_url = f"https://www.php.net/distributions/manual/php_manual_{lang}.tar.gz"
    out_path = Path(output_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)
    scope_prefix = f"https://www.php.net/manual/{lang}/"

    print(
        f"🌱 [MODO STREAMING ECO PHP.NET] Baixando pacote oficial em disco temporário (sem sobrecarregar a RAM):\n"
        f"   ├─ Fonte: {tar_url}\n"
        f"   └─ Orçamento Eco: {budget['workers']} worker(s) | Lote: {budget['batch_size']} págs | Pausa: {budget['delay_ms']}ms"
    )

    tmp_tar_fd, tmp_tar_path = tempfile.mkstemp(suffix=f"_php_{lang}.tar.gz")
    os.close(tmp_tar_fd)

    try:
        # Stream download directly to disk in 64KB chunks (0 RAM spike)
        # Faz download em streaming direto para o disco em blocos de 64KB (zero pico de RAM)
        req = Request(tar_url, headers={"User-Agent": USER_AGENT})
        with urlopen(req, timeout=120) as resp, open(tmp_tar_path, "wb") as out_f:
            shutil.copyfileobj(resp, out_f, length=65536)

        include_re = re.compile(include_pattern, re.IGNORECASE) if include_pattern else None
        exclude_re = re.compile(exclude_pattern, re.IGNORECASE) if exclude_pattern else None

        saved_pages = []
        converted_count = 0
        cached_count = 0
        t0 = time.time()

        batch_size = budget["batch_size"]
        workers = budget["workers"]
        current_batch = []

        def flush_batch(batch_list):
            nonlocal converted_count
            if not batch_list:
                return
            if workers <= 1:
                for s, h in batch_list:
                    res = _convert_single_php_html(s, h, out_path, scope_prefix)
                    saved_pages.append(res)
                    converted_count += 1
            else:
                with ThreadPoolExecutor(max_workers=workers) as pool:
                    futs = [
                        pool.submit(_convert_single_php_html, s, h, out_path, scope_prefix)
                        for s, h in batch_list
                    ]
                    for fut in as_completed(futs):
                        saved_pages.append(fut.result())
                        converted_count += 1
            batch_list.clear()
            guard_memory_pressure(budget)

        # Stream tar.gz sequentially so only `batch_size` small strings exist in RAM at any moment!
        # Lê o tar.gz sequencialmente em streaming para que apenas `batch_size` strings existam na RAM por vez!
        with tarfile.open(tmp_tar_path, mode="r|gz") as tf:
            for member in tf:
                if not member.isfile() or not member.name.endswith(".html"):
                    continue
                fname = os.path.basename(member.name)
                slug = fname[:-5]
                page_url = f"{scope_prefix}{slug}.php"

                if include_re and not include_re.search(page_url):
                    continue
                if exclude_re and exclude_re.search(page_url):
                    continue

                md_file = out_path / f"{slug}.md"
                if resume and md_file.exists() and md_file.stat().st_size > 80:
                    # Read only first 256 bytes to get title without loading full file
                    # Lê apenas os primeiros 256 bytes para obter o título sem carregar o arquivo todo
                    try:
                        with md_file.open("r", encoding="utf-8", errors="replace") as mf:
                            first_line = mf.readline(256).strip()
                        title = first_line.lstrip("# ").strip() or slug
                    except Exception:
                        title = slug
                    saved_pages.append({"url": page_url, "file": f"{slug}.md", "title": title, "depth": 1})
                    cached_count += 1
                else:
                    fobj = tf.extractfile(member)
                    if fobj:
                        raw_html = fobj.read().decode("utf-8", errors="replace")
                        current_batch.append((slug, raw_html))
                        if len(current_batch) >= batch_size:
                            flush_batch(current_batch)
                            if converted_count % (batch_size * 5) == 0:
                                mem_now = get_system_memory_info()
                                elapsed = time.time() - t0
                                print(
                                    f"   🌱 [ECO] Convertidas: {converted_count} | Cache: {cached_count} | "
                                    f"RAM Livre: {mem_now['avail_gb']} GB ({mem_now['used_percent']}%) | {elapsed:.1f}s"
                                )

                if max_pages > 0 and len(saved_pages) + len(current_batch) >= max_pages:
                    break

        if current_batch:
            flush_batch(current_batch)

        saved_pages.sort(key=lambda x: x["file"])
        write_index_and_manifest(out_path, root_url, scope_prefix, saved_pages)
        print(
            f"\n🎉 Manual do PHP ({lang}) processado com baixo consumo de recursos!\n"
            f"📂 Total de páginas: {len(saved_pages)} ({converted_count} convertidas agora, {cached_count} em cache)\n"
            f"📑 Índice mestre: {out_path / '_INDEX.md'}"
        )
        return True

    except Exception as e:
        print(f"⚠️ Aviso no streaming do pacote tar.gz ({e}). Alternando para crawler HTTP...")
        return False
    finally:
        if os.path.exists(tmp_tar_path):
            try:
                os.remove(tmp_tar_path)
            except Exception:
                pass
        gc.collect()


def _discover_toc_json_links(scope_prefix: str, include_re=None, exclude_re=None) -> list:
    """
    Discovers documentation links from Microsoft Learn / DocFX toc.json or JS nav manifests if present.
    Descobre links de documentação a partir do toc.json do Microsoft Learn / DocFX ou manifestos JS de navegação.
    """
    discovered = []
    if "learn.microsoft.com" in scope_prefix:
        toc_url = f"{scope_prefix.rstrip('/')}/toc.json"
        try:
            raw_json, _ = fetch_html_http_with_url(toc_url, timeout=15)
            toc_data = json.loads(raw_json)

            def _walk(nodes):
                if not isinstance(nodes, list):
                    return
                for node in nodes:
                    if not isinstance(node, dict):
                        continue
                    href = node.get("href")
                    if isinstance(href, str) and href.strip():
                        abs_u = normalize_url(urljoin(scope_prefix, href.strip()))
                        if is_valid_crawl_target(abs_u, scope_prefix, include_re, exclude_re):
                            discovered.append(abs_u)
                    if "children" in node:
                        _walk(node["children"])
                    if "items" in node:
                        _walk(node["items"])

            _walk(toc_data.get("items", []))
        except Exception:
            pass
    elif "fuelphp.com/docs" in scope_prefix:
        js_url = f"{scope_prefix.rstrip('/')}/assets/js/combined.js"
        try:
            raw_js, _ = fetch_html_http_with_url(js_url, timeout=15)
            for rel_href in sorted(set(re.findall(r'"([a-zA-Z0-9_/-]+\.html)"', raw_js))):
                abs_u = normalize_url(urljoin(scope_prefix, rel_href))
                if is_valid_crawl_target(abs_u, scope_prefix, include_re, exclude_re):
                    discovered.append(abs_u)
        except Exception:
            pass
    return discovered


def crawl_local(
    root_url: str,
    output_dir: str,
    crawl_mode: bool = False,
    max_pages: int = 100,
    max_depth: int = 5,
    engine: str = "auto",
    workers: int = 0,
    delay_ms: int = -1,
    max_ram_percent: int = 78,
    custom_selector: str = None,
    include_pattern: str = None,
    exclude_pattern: str = None,
    resume: bool = True,
    keep_usernotes: bool = False,
    file_prefix: str = "",
    merge_index: bool = False,
    custom_scope: str = None,
) -> bool:
    """
    Executes single-page scrape or full recursive BFS crawl locally with Hardware Eco Throttling.
    Executa captura de página única ou crawling recursivo BFS local com Controle Eco de Hardware.
    """
    budget = detect_hardware_budget(
        requested_workers=workers,
        requested_delay_ms=delay_ms,
        max_ram_percent=max_ram_percent,
    )

    print(
        f"🖥️ [DIAGNÓSTICO DE HARDWARE DA MÁQUINA OPERANTE]\n"
        f"   ├─ Processador: {budget['cpu_model']} ({budget['cpu_cores']} núcleos lógicos)\n"
        f"   ├─ Memória RAM: {budget['avail_ram_gb']} GB livres de {budget['total_ram_gb']} GB ({budget['ram_used_percent']}% em uso)\n"
        f"   ├─ Perfil Aplicado: {budget['tier']}\n"
        f"   └─ Limites Ativos: {budget['workers']} worker(s) | Lote: {budget['batch_size']} | Pausa: {budget['delay_ms']}ms | Teto RAM: {budget['max_ram_percent']}%\n"
    )

    if crawl_mode and (max_pages == 0 or max_pages >= 500) and not keep_usernotes:
        m_php = re.match(r"^https?://(?:www\.)?php\.net/manual/([a-zA-Z_]+)(?:/(?:index\.php)?)?$", root_url.strip())
        if m_php:
            lang = m_php.group(1)
            if crawl_php_net_via_official_tarball(
                lang=lang,
                root_url=root_url,
                output_dir=output_dir,
                budget=budget,
                max_pages=max_pages,
                include_pattern=include_pattern,
                exclude_pattern=exclude_pattern,
                resume=resume,
            ):
                return True

    out_path = Path(output_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)

    scope_prefix = custom_scope if custom_scope else get_scope_prefix(root_url)
    if not scope_prefix.endswith("/"):
        scope_prefix += "/"
    start_url = normalize_url(root_url)
    single_mode = not crawl_mode

    include_re = re.compile(include_pattern, re.IGNORECASE) if include_pattern else None
    exclude_re = re.compile(exclude_pattern, re.IGNORECASE) if exclude_pattern else None

    start_fname = url_to_md_filename(start_url, scope_prefix, single_mode=single_mode, file_prefix=file_prefix)
    queue = deque([(start_url, 0)])
    visited = {start_url}
    visited_files = {start_fname}
    saved_pages = []

    if crawl_mode:
        toc_links = _discover_toc_json_links(scope_prefix, include_re, exclude_re)
        if toc_links:
            for tl in toc_links:
                tfname = url_to_md_filename(tl, scope_prefix, single_mode=False, file_prefix=file_prefix)
                if tl not in visited and tfname not in visited_files:
                    visited.add(tl)
                    visited_files.add(tfname)
                    queue.append((tl, 1))
            print(f"📑 [TOC.JSON] {len(toc_links)} artigos descobertos no sumário estruturado!")

    use_http = engine in ("http", "fast") or (engine == "auto" and crawl_mode)
    active_workers = budget["workers"]

    print(
        f"🌐 [{'CRAWL RECURSIVO ECO' if crawl_mode else 'SCRAPE ÚNICO'}] "
        f"Iniciando em: {start_url}\n"
        f"   ├─ Escopo de links: {scope_prefix}\n"
        f"   ├─ Motor inicial: {'HTTP Eco (+ fallback Playwright)' if use_http else 'Playwright Headless Chromium'}\n"
        f"   └─ Limite de páginas: {'Ilimitado' if max_pages == 0 else max_pages} | Profundidade máx: {'Ilimitada' if max_depth == 0 else max_depth}"
    )

    pw_instance = None
    pw_browser = None
    pw_context = None

    def get_playwright_page():
        nonlocal pw_instance, pw_browser, pw_context
        if pw_context is None:
            from playwright.sync_api import sync_playwright
            pw_instance = sync_playwright().start()
            base_args = [
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--js-flags=--max-old-space-size=256",
                "--window-position=-32000,-32000",
            ]
            used_native_channel = False
            for ch in ("msedge", "chrome", None):
                try:
                    if ch:
                        pw_browser = pw_instance.chromium.launch(channel=ch, headless=False, args=base_args)
                        used_native_channel = True
                    else:
                        pw_browser = pw_instance.chromium.launch(headless=True, args=base_args)
                    break
                except Exception:
                    continue
            if used_native_channel:
                pw_context = pw_browser.new_context(viewport={"width": 1280, "height": 800})
            else:
                pw_context = pw_browser.new_context(
                    user_agent=USER_AGENT,
                    viewport={"width": 1280, "height": 800},
                )
        return pw_context.new_page()

    def process_single_url(target_url: str, depth: int):
        """Fetches, cleans, and converts a single URL, returning (title, md_filename, links, cached)."""
        nonlocal use_http
        md_filename = url_to_md_filename(target_url, scope_prefix, single_mode=single_mode, file_prefix=file_prefix)
        output_file = out_path / md_filename

        if resume and not single_mode and output_file.exists() and output_file.stat().st_size > 100:
            with output_file.open("r", encoding="utf-8", errors="replace") as f:
                first_line = f.readline(256)
            title = first_line.lstrip("# ").strip() or md_filename
            if depth > 0:
                return title, md_filename, [], True

        raw_html = None
        effective_url = target_url
        if use_http:
            try:
                raw_html, effective_url = fetch_html_http_with_url(target_url)
            except Exception as http_err:
                if engine == "http":
                    raise http_err
                if getattr(http_err, "code", None) == 403:
                    use_http = False

        if raw_html is None:
            page = get_playwright_page()
            try:
                page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(800 if crawl_mode else 1500)
                for _ in range(10):
                    try:
                        t_check = (page.title() or "").lower()
                    except Exception:
                        t_check = "moment"
                    if any(w in t_check for w in ("just a moment", "um momento", "moment", "challenge", "attention")):
                        page.wait_for_timeout(1200)
                    else:
                        break
                for _ in range(3):
                    try:
                        page.wait_for_load_state("domcontentloaded", timeout=10000)
                        raw_html = page.content()
                        break
                    except Exception:
                        page.wait_for_timeout(1000)
                if raw_html is None:
                    raw_html = page.content()
                effective_url = page.url or target_url
            finally:
                page.close()

        page_title, cleaned_html, links = clean_html_and_extract_links(
            raw_html=raw_html,
            page_url=effective_url,
            scope_prefix=scope_prefix,
            custom_selector=custom_selector,
            keep_usernotes=keep_usernotes,
            single_mode=single_mode,
            include_re=include_re,
            exclude_re=exclude_re,
            file_prefix=file_prefix,
        )
        del raw_html

        md_body = html_to_markdown(cleaned_html)
        del cleaned_html

        header = (
            f"# {page_title}\n\n"
            f"> **Fonte / Source:** {target_url}\n\n"
            f"---\n\n"
        )
        output_file.write_text(header + md_body + "\n", encoding="utf-8")
        del md_body
        return page_title, md_filename, links, False

    try:
        if single_mode:
            title, fname, links, _ = process_single_url(start_url, 0)
            saved_pages.append({"url": start_url, "file": fname, "title": title, "depth": 0})
            if merge_index:
                write_index_and_manifest(out_path, start_url, scope_prefix, saved_pages, merge_existing=True)
            print(f"✅ Sucesso! Markdown salvo em: {out_path / fname} ({len(links)} links internos detectados)")
            return True

        while queue:
            if max_pages > 0 and len(saved_pages) >= max_pages:
                break

            batch_size = min(
                active_workers if use_http else 1,
                (max_pages - len(saved_pages)) if max_pages > 0 else (active_workers if use_http else 1),
            )
            batch = []
            while queue and len(batch) < batch_size:
                batch.append(queue.popleft())

            if use_http and len(batch) > 1:
                with ThreadPoolExecutor(max_workers=active_workers) as pool:
                    future_map = {
                        pool.submit(process_single_url, u, d): (u, d)
                        for u, d in batch
                    }
                    for fut in as_completed(future_map):
                        u, d = future_map[fut]
                        try:
                            title, fname, links, cached = fut.result()
                            saved_pages.append({"url": u, "file": fname, "title": title, "depth": d})
                            status_tag = "⏭️ [CACHE]" if cached else "✅ [SALVO]"
                            print(f"{status_tag} ({len(saved_pages)}/{max_pages or '∞'}) [d={d}] {fname} <- {u}")
                            if max_depth == 0 or d < max_depth:
                                for lnk in links:
                                    lfname = url_to_md_filename(lnk, scope_prefix, single_mode=False, file_prefix=file_prefix)
                                    if lnk not in visited and lfname not in visited_files:
                                        visited.add(lnk)
                                        visited_files.add(lfname)
                                        queue.append((lnk, d + 1))
                        except Exception as err:
                            print(f"⚠️ Erro ao processar {u}: {err}")
            else:
                for u, d in batch:
                    try:
                        title, fname, links, cached = process_single_url(u, d)
                        saved_pages.append({"url": u, "file": fname, "title": title, "depth": d})
                        status_tag = "⏭️ [CACHE]" if cached else "✅ [SALVO]"
                        print(f"{status_tag} ({len(saved_pages)}/{max_pages or '∞'}) [d={d}] {fname} <- {u}")
                        if max_depth == 0 or d < max_depth:
                            for lnk in links:
                                lfname = url_to_md_filename(lnk, scope_prefix, single_mode=False, file_prefix=file_prefix)
                                if lnk not in visited and lfname not in visited_files:
                                    visited.add(lnk)
                                    visited_files.add(lfname)
                                    queue.append((lnk, d + 1))
                    except Exception as err:
                        print(f"⚠️ Erro ao processar {u}: {err}")

            guard_memory_pressure(budget)

        if saved_pages:
            write_index_and_manifest(out_path, start_url, scope_prefix, saved_pages, merge_existing=merge_index)
            print(
                f"\n🎉 Crawling concluído! {len(saved_pages)} página(s) salva(s) em: {out_path}\n"
                f"📑 Índice mestre gerado em: {out_path / '_INDEX.md'}\n"
                f"🗺️ Manifesto JSON gerado em: {out_path / 'crawl_manifest.json'}"
            )
            return True
        return False

    finally:
        if pw_browser:
            pw_browser.close()
        if pw_instance:
            pw_instance.stop()
        gc.collect()


def scrape_with_firecrawl(url: str, output_dir: str, mode: str = "scrape", max_pages: int = 100) -> bool:
    """
    Optional cloud scraping/crawling using Firecrawl API when FIRECRAWL_API_KEY is configured.
    Captura/crawling opcional em nuvem usando a API Firecrawl quando FIRECRAWL_API_KEY está configurada.
    """
    try:
        from firecrawl import FirecrawlApp
    except ImportError:
        return False

    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        return False

    try:
        app = FirecrawlApp(api_key=api_key)
        out_path = Path(output_dir).resolve()
        out_path.mkdir(parents=True, exist_ok=True)
        scope_prefix = get_scope_prefix(url)

        print(f"🚀 [Firecrawl] Iniciando modo '{mode}' para: {url}")

        if mode == "scrape":
            result = app.scrape_url(url, params={"formats": ["markdown"]})
            if "markdown" in result:
                filename = url_to_md_filename(url, scope_prefix, single_mode=True)
                (out_path / filename).write_text(result["markdown"], encoding="utf-8")
                print(f"✅ Salvo em: {out_path / filename}")
                return True
        elif mode == "crawl":
            limit_val = max_pages if max_pages > 0 else 1000
            crawl_status = app.crawl_url(
                url,
                params={"limit": limit_val, "scrapeOptions": {"formats": ["markdown"]}},
            )
            if isinstance(crawl_status, dict) and "data" in crawl_status:
                saved = []
                for i, page in enumerate(crawl_status["data"]):
                    if "markdown" in page and "metadata" in page:
                        page_url = page["metadata"].get("sourceURL", f"page_{i}")
                        title = page["metadata"].get("title", page_url)
                        filename = url_to_md_filename(page_url, scope_prefix, single_mode=False)
                        (out_path / filename).write_text(page["markdown"], encoding="utf-8")
                        saved.append({"url": page_url, "file": filename, "title": title, "depth": 1})
                write_index_and_manifest(out_path, url, scope_prefix, saved)
                print(f"✅ Crawling Firecrawl concluído. {len(saved)} páginas salvas em {out_path}")
                return True
    except Exception as e:
        print(f"⚠️ Erro ao executar Firecrawl (alternando para motor local): {e}")

    return False


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Captura páginas únicas ou varre sites/documentações inteiras com Perfilador Automático de Hardware (Baixo uso de CPU/RAM)."
    )
    parser.add_argument("url", help="URL alvo ou diretório raiz da documentação (ex: https://www.php.net/manual/pt_BR/)")
    parser.add_argument("output_dir", help="Diretório onde os arquivos .md serão salvos")
    parser.add_argument(
        "--crawl",
        action="store_true",
        help="Ativa o modo crawler recursivo seguindo todos os links internos do mesmo escopo/prefixo",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=100,
        help="Limite máximo de páginas no modo --crawl (Use 0 para ilimitado. Padrão: 100)",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=5,
        help="Profundidade máxima de cliques a partir da URL inicial (Use 0 para ilimitada. Padrão: 5)",
    )
    parser.add_argument(
        "--engine",
        choices=["auto", "http", "playwright", "firecrawl"],
        default="auto",
        help="Motor de captura: 'http' (leve), 'playwright' (SPA/JS), 'firecrawl' (API) ou 'auto'",
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Atalho para --engine http (extração leve sem abrir navegador para documentações SSR/HTML)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help="Número de threads (Padrão: 0 = auto-calculado de forma conservadora conforme CPU e RAM da máquina)",
    )
    parser.add_argument(
        "--delay-ms",
        type=int,
        default=-1,
        help="Pausa em milissegundos entre lotes para aliviar a CPU (Padrão: auto-calculado pelo perfil Eco)",
    )
    parser.add_argument(
        "--max-ram-percent",
        type=int,
        default=78,
        help="Limite percentual máximo de uso de RAM da máquina antes de pausar e forçar Garbage Collection (Padrão: 78)",
    )
    parser.add_argument(
        "--selector",
        type=str,
        default=None,
        help="Seletor CSS customizado para isolar o conteúdo principal (ex: '#layout-content' ou 'article')",
    )
    parser.add_argument(
        "--include",
        type=str,
        default=None,
        help="Expressão regular (Regex) de URLs que DEVEM ser incluídas no crawl (ex: 'security|language')",
    )
    parser.add_argument(
        "--exclude",
        type=str,
        default=None,
        help="Expressão regular (Regex) de URLs que DEVEM ser ignoradas no crawl (ex: 'function\\.')",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Força o re-download de todas as páginas mesmo que o arquivo .md já exista na pasta de destino",
    )
    parser.add_argument(
        "--keep-usernotes",
        action="store_true",
        help="Mantém comentários de usuários em documentações como php.net (#usernotes)",
    )
    parser.add_argument(
        "--prefix",
        type=str,
        default="",
        help="Prefixo opcional nos nomes dos arquivos .md gerados (útil ao mesclar múltiplas fontes na mesma pasta)",
    )
    parser.add_argument(
        "--merge-index",
        action="store_true",
        help="Mescla as páginas capturadas com o crawl_manifest.json e _INDEX.md existentes na pasta de destino",
    )
    parser.add_argument(
        "--scope",
        type=str,
        default=None,
        help="Prefixo de URL customizado para definir o escopo do crawl (ex: https://fatfreeframework.com/3.9/)",
    )
    return parser


def main():
    parser = build_arg_parser()
    args = parser.parse_args()

    url = args.url
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    engine = "http" if args.fast else args.engine
    mode = "crawl" if args.crawl else "scrape"

    if engine == "firecrawl" or (engine == "auto" and os.environ.get("FIRECRAWL_API_KEY") and not args.crawl):
        if scrape_with_firecrawl(url, args.output_dir, mode=mode, max_pages=args.max_pages):
            sys.exit(0)

    ok = crawl_local(
        root_url=url,
        output_dir=args.output_dir,
        crawl_mode=args.crawl,
        max_pages=args.max_pages,
        max_depth=args.max_depth,
        engine=engine,
        workers=args.workers,
        delay_ms=args.delay_ms,
        max_ram_percent=args.max_ram_percent,
        custom_selector=args.selector,
        include_pattern=args.include,
        exclude_pattern=args.exclude,
        resume=not args.no_resume,
        keep_usernotes=args.keep_usernotes,
        file_prefix=args.prefix,
        merge_index=args.merge_index,
        custom_scope=args.scope,
    )

    if ok:
        sys.exit(0)

    print("❌ Falha na captura. Verifique se o endereço está acessível ou bloqueado por firewall.")
    sys.exit(1)


if __name__ == "__main__":
    main()
