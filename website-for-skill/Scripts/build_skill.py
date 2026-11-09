#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-platform orchestrator that crawls a live website/documentation portal and compiles it
into a token-efficient, modular AI Skill with Hardware-Aware Eco Throttling (Low CPU & RAM).
Orquestrador multiplataforma que rastreia um site/portal de documentação ao vivo e o compila
em uma Skill modular com Controle Adaptativo de Hardware (Baixo consumo de CPU e RAM).

Depends on / Depende das skills: 'website-for-markdown' & 'docs-for-markdown'.
"""
import argparse
import ctypes
import gc
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

# Force UTF-8 on Windows console outputs / Força UTF-8 nas saídas de console no Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def apply_low_cpu_priority():
    """
    Lowers OS scheduling priority so skill building never freezes the user's machine.
    Reduz a prioridade do processo no SO para nunca travar a máquina durante a compilação da skill.
    """
    try:
        if sys.platform == "win32":
            handle = ctypes.windll.kernel32.GetCurrentProcess()
            ctypes.windll.kernel32.SetPriorityClass(handle, 0x00004000)  # BELOW_NORMAL_PRIORITY_CLASS
        elif hasattr(os, "nice"):
            os.nice(10)
    except Exception:
        pass


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
                return {
                    "total_gb": round(stat.ullTotalPhys / (1024 ** 3), 2),
                    "avail_gb": round(stat.ullAvailPhys / (1024 ** 3), 2),
                    "used_percent": int(stat.dwMemoryLoad),
                }
        elif sys.platform.startswith("linux"):
            mem = {}
            with open("/proc/meminfo", "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    parts = line.split(":")
                    if len(parts) == 2:
                        mem[parts[0].strip()] = int(parts[1].strip().split()[0]) * 1024
            total = mem.get("MemTotal", 4 * 1024 ** 3)
            avail = mem.get("MemAvailable", mem.get("MemFree", 2 * 1024 ** 3))
            return {
                "total_gb": round(total / (1024 ** 3), 2),
                "avail_gb": round(avail / (1024 ** 3), 2),
                "used_percent": int(round((1.0 - (avail / total)) * 100)) if total else 50,
            }
    except Exception:
        pass
    return {"total_gb": 8.0, "avail_gb": 4.0, "used_percent": 50}


def find_skill_script(skill_name: str, script_name: str):
    """
    Locates the script path of a dependent skill across standard installation roots.
    Encontra o caminho do script de uma skill dependente em múltiplos locais padrão.
    """
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parents[1]

    possible_paths = [
        repo_root / skill_name / "scripts" / script_name,
        repo_root / skill_name / "Scripts" / script_name,
        script_dir.parent.parent / skill_name / "scripts" / script_name,
        Path.cwd() / skill_name / "scripts" / script_name,
        Path.cwd().parent / skill_name / "scripts" / script_name,
        Path.home() / ".agents" / "skills" / skill_name / "scripts" / script_name,
        Path.home() / ".gemini" / "config" / "skills" / skill_name / "scripts" / script_name,
        Path.home() / ".copilot" / "skills" / skill_name / "scripts" / script_name,
        Path.home() / ".claude" / "skills" / skill_name / "scripts" / script_name,
    ]
    for p in possible_paths:
        if p.exists():
            return p.resolve()
    return None


def extract_page_title(md_file: Path) -> str:
    """
    Reads only the first 512 bytes of a Markdown file to extract the H1 title with near-zero RAM.
    Lê apenas os primeiros 512 bytes de um arquivo Markdown para extrair o título H1 com uso quase zero de RAM.
    """
    try:
        with md_file.open("r", encoding="utf-8", errors="replace") as f:
            for _ in range(8):
                line = f.readline(512)
                if not line:
                    break
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception:
        pass
    return md_file.stem.replace("_", " ").replace("-", " ").title()


def categorize_chapter(filename: str) -> str:
    """
    Determines the logical category group of a chapter from its filename prefix.
    Determina o grupo lógico de categoria de um capítulo a partir do prefixo do nome do arquivo.
    """
    stem = filename[:-3] if filename.endswith(".md") else filename
    if "." in stem:
        return stem.split(".")[0].lower()
    if "__" in stem:
        return stem.split("__")[0].lower()
    if "-" in stem and not stem.startswith("ch"):
        return stem.split("-")[0].lower()
    return "general"


def generate_skill_structure(
    skill_name: str,
    md_files_dir: Path,
    output_skill_dir: Path,
    source_url: str,
    max_ram_percent: int = 78,
) -> bool:
    """
    Structures captured Markdown files into a modular, token-efficient AI Skill using low-memory streaming.
    Estrutura os arquivos Markdown capturados em uma Skill modular usando streaming de baixo consumo de RAM.
    """
    apply_low_cpu_priority()
    skill_dir = Path(output_skill_dir).resolve()
    skill_dir.mkdir(parents=True, exist_ok=True)

    chapters_dir = skill_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(
        [
            p for p in Path(md_files_dir).glob("*.md")
            if p.name.lower() not in ("_index.md",)
        ]
    )
    if not md_files:
        print("❌ Nenhum arquivo Markdown encontrado para estruturar.")
        return False

    mem_info = get_system_memory_info()
    print(
        f"📚 Estruturando {len(md_files)} arquivo(s) em Skill modular (Modo Eco | "
        f"RAM Livre: {mem_info['avail_gb']} GB)..."
    )

    chapters_info = []

    if len(md_files) == 1:
        content = md_files[0].read_text(encoding="utf-8", errors="replace").strip()
        h2_matches = list(re.finditer(r"^##\s+(.+)$", content, re.MULTILINE))
        if len(h2_matches) >= 3:
            print("ℹ️ Subdividindo documento único em capítulos por tópicos principais (H2)...")
            (chapters_dir / "index.md").write_text(content + "\n", encoding="utf-8", newline="\n")
            for j, m in enumerate(h2_matches):
                t = m.group(1).strip()
                s = m.start()
                e = h2_matches[j + 1].start() if j + 1 < len(h2_matches) else len(content)
                sub_c = content[s:e].strip()
                slug = re.sub(r"[^\w\s-]", "", t).strip().lower().replace(" ", "-")[:35] or f"secao-{j+1}"
                fname = f"ch{j+1:02d}-{slug}.md"
                (chapters_dir / fname).write_text(f"# {t}\n\n" + sub_c + "\n", encoding="utf-8", newline="\n")
                chapters_info.append({"file": fname, "title": t, "category": "sections"})
        else:
            fname = md_files[0].name
            if md_files[0].resolve() != (chapters_dir / fname).resolve():
                shutil.copyfile(md_files[0], chapters_dir / fname)
            chapters_info.append({
                "file": fname,
                "title": extract_page_title(md_files[0]),
                "category": "general",
            })
        del content
        gc.collect()
    else:
        # Multi-page crawl mode: stream copy and periodically free RAM & yield CPU
        # Modo multipágina: copia em streaming e libera RAM / alivia CPU periodicamente
        for idx, md_file in enumerate(md_files, 1):
            fname = md_file.name
            dest_file = chapters_dir / fname
            if md_file.resolve() != dest_file.resolve():
                shutil.copyfile(md_file, dest_file)
            title = extract_page_title(md_file)
            cat = "index" if fname.lower() == "index.md" else categorize_chapter(fname)
            chapters_info.append({"file": fname, "title": title, "category": cat})

            if idx % 200 == 0:
                gc.collect()
                m_now = get_system_memory_info()
                if m_now["used_percent"] >= max_ram_percent:
                    time.sleep(0.5)
                else:
                    time.sleep(0.02)

    manifest_src = Path(md_files_dir) / "crawl_manifest.json"
    if manifest_src.exists() and manifest_src.resolve() != (chapters_dir / "crawl_manifest.json").resolve():
        shutil.copyfile(manifest_src, chapters_dir / "crawl_manifest.json")

    categories = {}
    for ch in chapters_info:
        categories.setdefault(ch["category"], []).append(ch)

    # Stream write chapters/_INDEX.md directly to file without building giant string in RAM
    # Grava chapters/_INDEX.md em streaming direto no disco sem alocar string gigante na RAM
    with (chapters_dir / "_INDEX.md").open("w", encoding="utf-8", newline="\n") as idx_f:
        idx_f.write(f"# 📚 Índice Completo de Capítulos / Complete Chapter Index ({len(chapters_info)} páginas)\n\n")
        idx_f.write(f"- **Fonte Oficial / Official Source:** {source_url}\n")
        idx_f.write(f"- **Total de Arquivos / Total Files:** {len(chapters_info)}\n\n---\n\n")
        for cat_name in sorted(categories.keys()):
            items = categories[cat_name]
            idx_f.write(f"## 📂 Categoria: `{cat_name}` ({len(items)} páginas)\n\n")
            for ch in items:
                idx_f.write(f"- [{ch['title']}]({ch['file']}) (`chapters/{ch['file']}`)\n")
            idx_f.write("\n")

    is_large_site = len(chapters_info) > 40
    if not is_large_site:
        en_chapters_block = "\n".join(
            f"- [{ch['title']}](chapters/{ch['file']})" for ch in chapters_info
        )
        pt_chapters_block = en_chapters_block
    else:
        cat_summary_en = [
            f"- **[Full Searchable Index ({len(chapters_info)} pages)](chapters/_INDEX.md)**"
        ]
        cat_summary_pt = [
            f"- **[Índice Completo Pesquisável ({len(chapters_info)} páginas)](chapters/_INDEX.md)**"
        ]
        for cat_name in sorted(categories.keys()):
            items = categories[cat_name]
            sample_links = ", ".join(
                f"[{c['title']}](chapters/{c['file']})" for c in items[:3]
            )
            more = f" *(+{len(items) - 3} more in [_INDEX.md](chapters/_INDEX.md))*" if len(items) > 3 else ""
            more_pt = f" *(+{len(items) - 3} mais em [_INDEX.md](chapters/_INDEX.md))*" if len(items) > 3 else ""
            cat_summary_en.append(f"- **Category `{cat_name}` ({len(items)} pages):** {sample_links}{more}")
            cat_summary_pt.append(f"- **Categoria `{cat_name}` ({len(items)} páginas):** {sample_links}{more_pt}")
        en_chapters_block = "\n".join(cat_summary_en)
        pt_chapters_block = "\n".join(cat_summary_pt)

    skill_title = skill_name.replace("-", " ").title()
    skill_md_content = f"""---
name: {skill_name}
description: Base de conhecimento e documentação técnica extraída de {source_url} ({len(chapters_info)} páginas mapeadas).
language: en, pt-BR
---

# {skill_title}

## 🇺🇸 English
### Mental Model & Core Structure
This skill provides structured reference and knowledge extracted from `{source_url}`.
Chapters are modularized inside `chapters/` with preserved internal links and loaded on-demand to optimize token usage and context efficiency.

### Navigation & Chapters ({len(chapters_info)} total files)
{en_chapters_block}

---

## 🇧🇷 Português (Brasil)
### Modelo Mental & Estrutura Central
Esta skill fornece referência estruturada e conhecimento extraído de `{source_url}`.
Os capítulos estão modularizados em `chapters/` com links internos preservados e são carregados sob demanda para otimizar o uso de tokens e a janela de contexto.

### Navegação & Capítulos ({len(chapters_info)} arquivos no total)
{pt_chapters_block}
"""
    (skill_dir / "SKILL.md").write_text(skill_md_content, encoding="utf-8", newline="\n")

    cheatsheet_content = f"""# Cheatsheet / Guia Rápido - {skill_title}

*Resumo operacional, mapa de categorias e referências rápidas extraídas de {source_url}.*

- **Fonte Oficial / Official Source:** {source_url}
- **Total de Páginas / Total Pages:** {len(chapters_info)}
- **Índice Mestre de Links / Master Link Index:** [chapters/_INDEX.md](chapters/_INDEX.md)

## 📂 Categorias Mapeadas / Mapped Categories
| Categoria / Category | Arquivos / Files | Exemplo Principal / Primary Entry |
|---|---|---|
"""
    for cat_name in sorted(categories.keys()):
        items = categories[cat_name]
        first = items[0]
        cheatsheet_content += f"| `{cat_name}` | {len(items)} | [{first['title']}](chapters/{first['file']}) |\n"

    (skill_dir / "cheatsheet.md").write_text(cheatsheet_content, encoding="utf-8", newline="\n")

    glossary_limit = chapters_info[:60]
    glossary_content = f"""# Glossary / Glossário - {skill_title}

*Dicionário de tópicos, módulos e entidades centrais (veja o mapa completo em [chapters/_INDEX.md](chapters/_INDEX.md)).*

"""
    for ch in glossary_limit:
        glossary_content += f"- **{ch['title']}** (`{ch['category']}`): Consulte [chapters/{ch['file']}](chapters/{ch['file']})\n"
    if len(chapters_info) > 60:
        glossary_content += f"\n> ℹ️ *Mais {len(chapters_info) - 60} tópicos listados em [chapters/_INDEX.md](chapters/_INDEX.md).*\n"

    (skill_dir / "glossary.md").write_text(glossary_content, encoding="utf-8", newline="\n")

    patterns_content = f"""# Patterns & Architecture / Padrões e Arquitetura - {skill_title}

*Padrões recomendados, navegação entre módulos e boas práticas extraídas de {source_url}.*

- Para buscar rapidamente qualquer função, classe ou guia sem estourar a janela de contexto, consulte primeiro [`chapters/_INDEX.md`](chapters/_INDEX.md) ou use busca por nome de arquivo em `chapters/`.
"""
    (skill_dir / "patterns.md").write_text(patterns_content, encoding="utf-8", newline="\n")

    if not (skill_dir / "VERSION").exists():
        (skill_dir / "VERSION").write_text("0.1.0-beta\n", encoding="utf-8", newline="\n")

    gc.collect()
    print(f"✅ Skill estruturada com sucesso em: {skill_dir}")
    print(f"📊 Capítulos gerados: {len(chapters_info)} (organizados em {len(categories)} categoria(s))")
    print(f"📑 Índice completo: {chapters_dir / '_INDEX.md'}")
    return True


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Constrói uma Skill modular completa a partir de um website com Controle Adaptativo de Hardware (Baixo uso de CPU/RAM)."
    )
    parser.add_argument("url", help="URL do site ou documentação (ex: https://www.php.net/manual/pt_BR/)")
    parser.add_argument("skill_name", help="Nome da skill a ser criada (ex: php-manual-pt-br)")
    parser.add_argument("output_dir", nargs="?", default=None, help="(Opcional) Diretório onde a skill será salva")
    parser.add_argument("--crawl", action="store_true", help="Varre recursivamente todos os links internos do escopo")
    parser.add_argument("--max-pages", type=int, default=100, help="Limite máximo de páginas no crawl (0 = ilimitado. Padrão: 100)")
    parser.add_argument("--max-depth", type=int, default=5, help="Profundidade máxima de cliques (0 = ilimitada. Padrão: 5)")
    parser.add_argument("--fast", action="store_true", help="Usa motor HTTP leve para documentações SSR/estáticas")
    parser.add_argument("--engine", choices=["auto", "http", "playwright", "firecrawl"], default="auto", help="Motor de captura")
    parser.add_argument("--workers", type=int, default=0, help="Threads simultâneas (Padrão: 0 = auto-calculado conforme CPU e RAM da máquina)")
    parser.add_argument("--delay-ms", type=int, default=-1, help="Pausa em ms entre lotes para reduzir uso de CPU (Padrão: auto)")
    parser.add_argument("--max-ram-percent", type=int, default=78, help="Teto percentual de RAM antes de pausar e rodar Garbage Collector (Padrão: 78)")
    parser.add_argument("--selector", type=str, default=None, help="Seletor CSS do conteúdo principal")
    parser.add_argument("--include", type=str, default=None, help="Regex de URLs para incluir no crawl")
    parser.add_argument("--exclude", type=str, default=None, help="Regex de URLs para excluir do crawl")
    parser.add_argument("--keep-raw", action="store_true", help="Mantém a pasta temporária de captura (.temp_scrape_*)")
    parser.add_argument("--from-dir", type=str, default=None, help="Pula o download e estrutura a skill diretamente de uma pasta com arquivos .md já baixados")
    return parser


def main():
    apply_low_cpu_priority()
    parser = build_arg_parser()
    args = parser.parse_args()

    url = args.url
    skill_name = args.skill_name
    output_skill_dir = Path(args.output_dir).resolve() if args.output_dir else (Path.cwd() / skill_name).resolve()

    if args.from_dir:
        source_md_dir = Path(args.from_dir).resolve()
        if not source_md_dir.exists():
            print(f"❌ Diretório informado em --from-dir não encontrado: {source_md_dir}")
            sys.exit(1)
        success = generate_skill_structure(
            skill_name,
            source_md_dir,
            output_skill_dir,
            url,
            max_ram_percent=args.max_ram_percent,
        )
        sys.exit(0 if success else 1)

    scrape_script = find_skill_script("website-for-markdown", "scrape_to_md.py")
    if not scrape_script:
        print("❌ Script 'scrape_to_md.py' da skill 'website-for-markdown' não encontrado.")
        sys.exit(1)

    temp_dir = Path.cwd() / f".temp_scrape_{skill_name}"
    temp_dir.mkdir(parents=True, exist_ok=True)

    print(f"🌐 Iniciando captura do site (Modo Eco Adaptativo): {url}")
    cmd = [
        sys.executable,
        str(scrape_script),
        url,
        str(temp_dir),
        "--max-pages", str(args.max_pages),
        "--max-depth", str(args.max_depth),
        "--engine", "http" if args.fast else args.engine,
        "--workers", str(args.workers),
        "--delay-ms", str(args.delay_ms),
        "--max-ram-percent", str(args.max_ram_percent),
    ]
    if args.crawl:
        cmd.append("--crawl")
    if args.selector:
        cmd.extend(["--selector", args.selector])
    if args.include:
        cmd.extend(["--include", args.include])
    if args.exclude:
        cmd.extend(["--exclude", args.exclude])

    result = subprocess.run(cmd)

    md_files = list(temp_dir.glob("*.md"))
    if result.returncode != 0 and not md_files:
        existing_skill = Path.cwd() / skill_name
        if existing_skill.exists() and (existing_skill / "chapters").exists():
            print(f"ℹ️ Reestruturando a partir do conteúdo existente em {existing_skill}...")
            for f in (existing_skill / "chapters").glob("*.md"):
                shutil.copyfile(f, temp_dir / f.name)

    print(f"🏗️ Construindo skill em: {output_skill_dir}")
    success = generate_skill_structure(
        skill_name,
        temp_dir,
        output_skill_dir,
        url,
        max_ram_percent=args.max_ram_percent,
    )

    if not args.keep_raw:
        shutil.rmtree(temp_dir, ignore_errors=True)
    else:
        print(f"💾 Arquivos brutos preservados em: {temp_dir}")

    if success:
        print(f"\n🎉 Skill '{skill_name}' construída e validada com sucesso!")
        print(f"📂 Localização: {output_skill_dir}")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
