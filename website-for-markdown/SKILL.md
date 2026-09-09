---
name: website-for-markdown
description: Web scraping and crawling engine that captures single web pages, developer documentation portals, and JavaScript/SPA applications into noise-free, LLM-ready Markdown using Firecrawl or local Playwright + MarkItDown. Use when the user wants to fetch web content, convert online articles, or scrape entire website domains into clean Markdown via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama.
---

# Website for Markdown 🌐➡️📝

---

## 🇺🇸 English

### 📌 Overview & Architecture
**Website for Markdown** is a dual-engine web extraction skill designed to capture websites, SPAs (React, Vue, Angular), and developer documentation portals into clean, noise-free Markdown (`.md`).

It incorporates two complementary engines:
1. **Firecrawl Cloud Engine (Premium / API):** Best for recursive domain-wide crawling (`--crawl`), handling anti-bot protections, parsing sitemaps, and extracting nested documentation trees.
2. **Playwright Local Engine (Free / Built-in):** Headless Chromium instance that renders JavaScript and client-side hydrated SPAs locally without external API dependencies.

### 🚀 Capabilities
- **Noise Elimination:** Filters navigation bars, cookie banners, advertisements, and footer menus.
- **Client-Side Rendering:** Executes client-side scripts to capture fully hydrated content.
- **Semantic Formatting:** Converts tables, code blocks, syntax highlights, and markdown headers accurately.

### 🛠️ CLI Usage
```bash
# Verify environment
python scripts/check_env.py

# Scrape a single URL using local Playwright
python scripts/scrape_to_md.py "https://docs.example.com/api" "output_dir"

# Recursive full-domain crawl using Firecrawl (requires FIRECRAWL_API_KEY)
python scripts/scrape_to_md.py "https://docs.example.com" "output_dir" --crawl
```

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral & Arquitetura
O **Website for Markdown** é uma skill de extração web com motor duplo projetada para capturar páginas da web, SPAs (React, Vue, Angular) e portais de documentação para desenvolvedores em Markdown (`.md`) limpo e livre de ruídos.

Ele integra dois motores complementares:
1. **Motor Firecrawl (Nuvem / API):** Ideal para varredura recursiva de domínios inteiros (`--crawl`), contorno de proteções anti-bot, leitura de sitemaps e extração em árvore de documentações.
2. **Motor Playwright Local (Gratuito / Embutido):** Instância Chromium headless que executa JavaScript e renderiza SPAs hidratadas localmente sem custo de API externa.

### 🚀 Capacidades
- **Eliminação de Ruído:** Filtra menus de navegação, banners de cookies, pop-ups e rodapés redundantes.
- **Renderização Client-Side:** Executa scripts do lado do cliente para capturar o conteúdo dinâmico completo.
- **Formatação Semântica:** Converte tabelas, blocos de código, destaques de sintaxe e títulos com fidelidade.

### 🛠️ Uso via CLI
```bash
# Verificar ambiente
python scripts/check_env.py

# Capturar uma única URL usando Playwright local
python scripts/scrape_to_md.py "https://docs.exemplo.com/api" "pasta_saida"

# Varredura recursiva de domínio inteiro via Firecrawl (requer FIRECRAWL_API_KEY)
python scripts/scrape_to_md.py "https://docs.exemplo.com" "pasta_saida" --crawl
```
