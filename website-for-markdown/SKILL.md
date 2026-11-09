---
name: website-for-markdown
description: Web scraping and recursive crawling engine that captures single web pages, developer documentation portals, and JavaScript/SPA applications into noise-free, LLM-ready Markdown using local HTTP multi-thread crawler, Playwright Headless Chromium, or Firecrawl. Preserves and rewrites internal links (.php/.html to .md) and generates _INDEX.md and crawl_manifest.json.
---

# Website for Markdown 🌐➡️📝

---

## 🇺🇸 English

### 📌 Overview & Architecture
**Website for Markdown** (`v0.3.0-beta`) is a multi-engine web extraction and recursive crawling skill designed to capture websites, SPAs (React, Vue, Angular), and large developer documentation portals (such as `php.net/manual/pt_BR/`) into clean, noise-free Markdown (`.md`) with intact internal navigation links.

It incorporates three complementary engines:
1. **Local Fast HTTP Multi-Thread Crawler (`--crawl --fast` / `--engine http`):** High-speed parallel BFS crawler with automatic path-prefix scope locking, DOM noise removal (`#layout-content`, `article`, `main`), internal link rewriting (`.php`/`.html` $\rightarrow$ `.md`), resume cache, and automatic fallback to Playwright if JS rendering is needed.
2. **Playwright Local Engine (`--engine playwright`):** Headless Chromium instance that reuses a persistent browser context across the crawl queue to render client-side hydrated SPAs locally without external API costs.
3. **Firecrawl Cloud Engine (`--engine firecrawl`):** Optional cloud API integration when `FIRECRAWL_API_KEY` is configured.

### 🚀 Key Capabilities
- **Automatic Hardware Profiler & Adaptive Eco Throttling (`detect_hardware_budget`):** Inspects the host CPU model, logical core count, total physical RAM, and real-time free RAM before starting. Automatically lowers OS process priority (`BELOW_NORMAL_PRIORITY_CLASS` on Windows / `nice(10)` on Linux/macOS), caps workers conservatively (~15–20% of CPU), streams archives from disk in tiny micro-batches (25–35 pages), runs `gc.collect()` between batches, and pauses automatically if system RAM usage exceeds `--max-ram-percent` (default 78%).
- **Path-Prefix Scope Lock:** When crawling `https://www.php.net/manual/pt_BR/`, automatically restricts the crawler to URLs inside `/manual/pt_BR/`, preventing leaks into other languages or external sections.
- **Internal Link Rewriting:** Converts internal `<a href="language.types.php#anchor">` links into local `[...](language.types.md#anchor)` references so agents can navigate across files offline.
- **DOM Noise Elimination:** Isolates main documentation containers (`#layout-content`, `main`, `article`, `.markdown-body`) and strips navigation menus, sidebars, footers, and user comment sections.
- **Resume Cache & Master Index:** Skips already-downloaded `.md` files on interrupted runs and generates `_INDEX.md` + `crawl_manifest.json`.

### 🛠️ CLI Usage
```bash
# Verify environment
python scripts/check_env.py

# Scrape a single URL
python scripts/scrape_to_md.py "https://www.php.net/manual/pt_BR/security.php" "output_dir"

# Recursive local crawl (100 pages default, or --max-pages 0 for unlimited)
python scripts/scrape_to_md.py "https://www.php.net/manual/pt_BR/" "output_dir" --crawl --fast --max-pages 200

# Filter crawl by regex (--include / --exclude) and custom thread workers
python scripts/scrape_to_md.py "https://www.php.net/manual/pt_BR/" "output_dir" --crawl --fast --include "security|language" --max-pages 0 --workers 8
```

---

### 🏷️ Semantic Versioning, VERSION File & Release Protocol
- **`VERSION` File:** Contains the exact skill version string (`0.3.0-beta`).
- **Version Awareness:** The Agent must read `VERSION` to notify the operator/caller of the active skill version.
- **Update Protocol:** Always bump `VERSION` following [SemVer](https://semver.org/spec/v2.0.0.html), register updates in [`CHANGELOG.md`](CHANGELOG.md), and create a git release tag (`website-for-markdown-v<version>`).

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral & Arquitetura
O **Website for Markdown** (`v0.3.0-beta`) é uma skill de extração e rastreamento recursivo (crawler) com múltiplos motores, projetada para capturar páginas da web, SPAs e portais inteiros de documentação técnica (como `https://www.php.net/manual/pt_BR/`) em Markdown (`.md`) limpo, sem ruídos e com todos os links internos reescritos para navegação local.

Integra três motores complementares:
1. **Crawler Local HTTP Multi-Thread (`--crawl --fast` / `--engine http`):** Rastreador recursivo em largura (BFS) de alta velocidade em paralelo, com trava automática de escopo por prefixo de URL, limpeza cirúrgica de DOM (`#layout-content`, `article`, `main`), reescrita de links internos (`.php`/`.html` $\rightarrow$ `.md`), retomada automática (*resume cache*) e fallback transparente para Playwright caso a página exija JS.
2. **Motor Playwright Local (`--engine playwright`):** Instância Chromium headless que reutiliza o mesmo contexto de navegador durante toda a fila de crawling para renderizar SPAs locais sem custo de API externa.
3. **Motor Firecrawl (`--engine firecrawl`):** Integração opcional em nuvem quando `FIRECRAWL_API_KEY` está definida.

### 🛠️ Uso via CLI
```bash
# Verificar ambiente
python scripts/check_env.py

# Capturar uma única URL
python scripts/scrape_to_md.py "https://www.php.net/manual/pt_BR/security.php" "pasta_saida"

# Varredura recursiva local rápida (padrão: 100 páginas, ou --max-pages 0 para ilimitado)
python scripts/scrape_to_md.py "https://www.php.net/manual/pt_BR/" "pasta_saida" --crawl --fast --max-pages 200

# Filtrar seções específicas por Regex (--include / --exclude) sem limite de páginas
python scripts/scrape_to_md.py "https://www.php.net/manual/pt_BR/" "pasta_saida" --crawl --fast --include "security|language" --max-pages 0 --workers 8
```
