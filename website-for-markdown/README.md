# Website for Markdown 🌐➡️📝

> **Universal Web Scraping & Crawling Engine for AI-Ready Clean Markdown**  
> *Motor Universal de Captura e Rastreamento Web para Markdown Limpo Otimizado para IA*

---

## 🇺🇸 English

### 📌 Overview
**Website for Markdown** is a high-performance, cross-platform toolchain designed to capture and transform web pages, documentation portals, blogs, and Single Page Applications (SPAs) into **clean, noise-free, LLM-optimized Markdown (`.md`)**.

It features a hybrid dual-engine architecture:
1. **Premium / Cloud Engine (Firecrawl):** Ideal for deep crawling entire domains, resolving bot protections, handling sitemaps, and extracting clean markdown recursively.
2. **Local / Free Fallback Engine (Playwright + MarkItDown):** Renders full client-side JavaScript, hydration (React, Vue, Angular, Next.js), and dynamically loaded content locally without API costs.

---

### 🚀 Architecture & Dual-Engine Pipeline

```text
                     [ Target URL / Domain ]
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
     [ FIRECRAWL ENGINE ]            [ LOCAL PLAYWRIGHT ENGINE ]
    (When API Key is present)          (Free / Local Fallback)
                 │                             │
    • Full Domain Recursive Crawl    • Headless Chromium Engine
    • Anti-Bot & Bypass Handling      • JS & SPA DOM Hydration
    • Native Markdown Extraction      • MarkItDown HTML Parsing
                 │                             │
                 └──────────────┬──────────────┘
                                │
                                ▼
               [ Clean, Structured Markdown File(s) ]
```

---

### 🛠️ CLI Usage & Examples

#### 1. Environment Diagnostics
Verify installed Python packages, Playwright Chromium binaries, and API key status:
```bash
# Windows
python scripts/check_env.py

# Linux / macOS
python3 scripts/check_env.py
```

#### 2. Single Page Scraping
Captures a single web page and saves it as Markdown in the specified directory:
```bash
# Windows
python scripts/scrape_to_md.py "https://example.com/docs" "output_folder"

# Linux / macOS
python3 scripts/scrape_to_md.py "https://example.com/docs" "output_folder"
```

#### 3. Full Domain Crawling (Recursive)
Recursively crawls and extracts an entire website (Requires `FIRECRAWL_API_KEY`):
```bash
# Set your API Key
export FIRECRAWL_API_KEY="fc-your-key-here"  # Linux / macOS
$env:FIRECRAWL_API_KEY="fc-your-key-here"     # Windows PowerShell

# Run with --crawl flag
python scripts/scrape_to_md.py "https://docs.example.com" "output_folder" --crawl
```

---

### 📦 Installation

```bash
# 1. Install Python dependencies
pip install markitdown firecrawl-py playwright

# 2. Install Playwright Chromium browser binary
python -m playwright install chromium
```

---
---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
O **Website for Markdown** é uma ferramenta multiplataforma desenvolvida para capturar e converter websites, portais de documentação, artigos, blogs e aplicações de página única (SPAs) em **Markdown (`.md`) limpo, sem anúncios, estruturado e pronto para uso por Agentes de IA**.

A skill opera sob uma arquitetura híbrida de dois motores:
1. **Motor Premium / Nuvem (Firecrawl):** Ideal para varrer sites e documentações inteiras recursivamente (`--crawl`), contornando proteções anti-bot e extraindo markdown semântico direto da nuvem.
2. **Motor Local / Gratuito (Playwright + MarkItDown):** Executa um navegador Chromium headless localmente, renderizando páginas complexas com JavaScript pesado (React, Next.js, Vue, Angular) e convertendo o DOM resultante em Markdown sem custos de API.

---

### 🚀 Fluxo de Execução Híbrido

```text
                   [ URL Alvo / Domínio ]
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
   [ MOTOR FIRECRAWL ]             [ MOTOR PLAYWRIGHT LOCAL ]
 (Quando API Key está ativa)         (Fallback Gratuito / Local)
              │                             │
 • Varredura recursiva de domínio • Navegador Chromium Headless
 • Bypass de proteções anti-bot   • Renderização de SPAs e JS
 • Extração nativa em Markdown    • Conversão HTML via MarkItDown
              │                             │
              └──────────────┬──────────────┘
                             │
                             ▼
             [ Arquivo(s) Markdown Estruturados ]
```

---

### 🛠️ Modo de Uso via Terminal

#### 1. Verificação do Ambiente
Valida os pacotes instalados, binários do Chromium e a presença da chave de API:
```bash
# Windows
python scripts/check_env.py

# Linux / macOS
python3 scripts/check_env.py
```

#### 2. Captura de Página Única (Scrape)
Captura uma página específica e salva no diretório de destino:
```bash
# Windows
python scripts/scrape_to_md.py "https://exemplo.com/artigo" "pasta_saida"

# Linux / macOS
python3 scripts/scrape_to_md.py "https://exemplo.com/artigo" "pasta_saida"
```

#### 3. Rastreamento de Site Inteiro (Crawl Recursivo)
Varre e extrai múltiplas páginas de um domínio (Requer chave do Firecrawl):
```bash
# Configurar Chave de API
$env:FIRECRAWL_API_KEY="fc-sua-chave-aqui"    # Windows PowerShell
export FIRECRAWL_API_KEY="fc-sua-chave-aqui"  # Linux / macOS

# Executar com a flag --crawl
python scripts/scrape_to_md.py "https://docs.exemplo.com" "pasta_saida" --crawl
```

---

### 📦 Instalação de Dependências

```bash
# 1. Instalar bibliotecas Python
pip install markitdown firecrawl-py playwright

# 2. Baixar o navegador Chromium do Playwright
python -m playwright install chromium
```

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (pandoc, libreoffice, tesseract), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (pandoc, libreoffice, tesseract), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)

