# AI Skills Ecosystem 🧠⚡

> **Modular, Token-Efficient Knowledge Base & Skill Ingestion Pipeline for AI Agents**  
> *Ecossistema Modular de Base de Conhecimento e Pipeline de Ingestão de Skills para Agentes de IA*

---

## 🇺🇸 English

### 🎯 Why Skills? (Motivation & Core Purpose)

Modern Large Language Models (LLMs) and Autonomous AI Agents (like Antigravity, Claude Code, GitHub Copilot, OpenAI Codex, etc.) are exceptionally capable at reasoning, coding, and problem-solving. However, when faced with large codebases, extensive API documentation, complex RPG rulebooks, or proprietary company manuals, they suffer from two major problems:

1. **Context Window Exhaustion & High Token Cost:** Dumping entire books or monolithic documentation files into the prompt window wastes thousands of tokens per turn and causes hallucinations or attention degradation ("lost in the middle").
2. **Lack of Domain-Specific Structure:** Raw, unformatted documents contain noisy layout elements (headers, footers, broken tables, column mixing, fragmented code blocks) that confuse the agent.

#### The Solution: The Skills Architecture
**Skills** transform raw data (documents, web portals, APIs) into **structured, on-demand micro-knowledge units**:
- **Master Index (`SKILL.md`):** Serves as the cognitive map and mental model for the agent.
- **On-Demand Chapters (`chapters/*.md`):** Deep technical chapters loaded only when specifically relevant to the current user prompt (~10KB to 40KB each).
- **Fast-Path Reference (`cheatsheet.md`, `glossary.md`, `patterns.md`):** Instant access to syntaxes, canonical terms, and architectural patterns without reading entire manuals.

---

### 📦 Installation & Setup

#### 0. Mandatory Ecosystem Requirements: GitHub CLI (`gh`) & Mandatory Companion Skills
> 🚨 **GOLDEN RULE FOR ALL SKILLS (GLOBAL & LOCAL ENFORCEMENT):**  
> Every skill created and operated within this ecosystem strictly requires:
> 1. **Active GitHub CLI (`gh`) & Authentication:** Enables seamless repository cloning, automatic updates, and instant GitHub issue submission (`gh issue create --repo CharlesCorreaDev/skills-ai`).
>    - **Windows:** `winget install GitHub.cli` or `choco install gh`
>    - **macOS:** `brew install gh`
>    - **Linux:** `sudo apt install gh`
>    - **Authenticate:** `gh auth login`
>
> 2. **Mandatory Companion Skills Trinity (Always Available Globally and in User Projects):**  
>    All skills strictly carry and integrate the following three core skills:
>    - **`andrej-karpathy-skills`** (`https://github.com/multica-ai/andrej-karpathy-skills`): Pragmatic software engineering discipline, minimal code, zero blind assumptions.
>    - **`grill-me`** (`https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me`): Structured alignment interview with the user/author before starting tasks to eliminate design ambiguities.
>    - **`skills-code-review`** (`https://www.aihero.dev/skills-code-review`): Rigorous automated code review and quality gating before delivering any work.
>    ```bash
>    # Install globally and in local project
>    npx skills@latest add multica-ai/andrej-karpathy-skills
>    npx skills@latest add mattpocock/skills --skill=grill-me
>    npx skills@latest add aihero-dev/skills-code-review
>    ```

#### 1. Clone the Repository
```bash
git clone https://github.com/CharlesCorreaDev/skills-ai.git
cd skills-ai
```

#### 2. Create Virtual Environment & Install Python Dependencies
```bash
# Create and activate virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate

# Install core extraction & scraping libraries
pip install markitdown pdfminer.six pdfplumber pypdf python-docx mammoth openpyxl pandas python-pptx markdownify beautifulsoup4 firecrawl-py playwright

# Install browser binaries for Web Scraping (Playwright)
playwright install chromium
```

#### 3. Optional System Binaries (For 100% Format Coverage & OCR)
For advanced format conversions (Legacy `.doc`, `.ppt`, LibreOffice `.odt`, and scanned image OCR):

- **Windows (via Winget or Chocolatey):**
  ```powershell
  winget install JohnMacFarlane.Pandoc TheDocumentFoundation.LibreOffice UB-Mannheim.TesseractOCR
  ```
- **Ubuntu / Debian:**
  ```bash
  sudo apt-get update && sudo apt-get install -y pandoc libreoffice tesseract-ocr poppler-utils
  ```
- **macOS (via Homebrew):**
  ```bash
  brew install pandoc libreoffice tesseract poppler
  ```

#### 4. Installing Skills into your AI Agent
To make these skills available to your agent, copy or symlink the desired skill folders into your agent's configuration directory:

| Agent / Tool | Project-level Root | Global / User-level Root |
|---|---|---|
| **Antigravity** | `.agents/skills/<skill-name>/` | `~/.gemini/config/skills/<skill-name>/` |
| **Claude Code** | `.claude/skills/<skill-name>/` | `~/.claude/skills/<skill-name>/` |
| **Copilot Workspace** | `.github/skills/<skill-name>/` | `~/.copilot/skills/<skill-name>/` |

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (pandoc, libreoffice, tesseract), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---

### 🧩 Available Skills & Ecosystem Map

```text
                                [ Raw Knowledge Sources ]
                                    │               │
                     ┌──────────────┘               └──────────────┐
                     ▼                                             ▼
          [ Local Documents / Files ]                     [ Live Websites / APIs ]
         (PDF, DOCX, XLSX, PPTX, etc.)                   (Websites, SPAs, Portals)
                     │                                             │
                     ▼                                             ▼
          [ docs-for-markdown ]                         [ website-for-markdown ]
         (Extract to Clean .md)                         (Crawl / Render to Clean .md)
                     │                                             │
                     ▼                                             ▼
           [ docs-for-skill ]                            [ website-for-skill ]
         (Modularize Document)                          (Orchestrate Full Web Skill)
                     │                                             │
                     └──────────────┬──────────────────────────────┘
                                    ▼
                         [ Ready Modular Skill ]
                     (SKILL.md, chapters, cheatsheet)
```

| Skill | Purpose | Version | Status | Documentation & Changelog |
|---|---|---|---|---|
| **`docs-for-markdown`** | Universal converter for multi-format documents (PDF, DOCX, XLSX, PPTX, ODT, HTML, RTF) into clean Markdown. | [`0.3.0-beta`](docs-for-markdown/VERSION) | Beta | [README](docs-for-markdown/README.md) • [Changelog](docs-for-markdown/CHANGELOG.md) |
| **`docs-for-skill`** | Transforms document Markdown into high-performance, modular AI Skills. | [`0.4.0-beta`](docs-for-skill/VERSION) | Beta | [README](docs-for-skill/README.md) • [Changelog](docs-for-skill/CHANGELOG.md) |
| **`website-for-markdown`** | Hybrid web scraping engine (Firecrawl + Playwright/Chromium) for clean Markdown extraction from web pages and SPAs. | [`0.4.0-beta`](website-for-markdown/VERSION) | Beta | [README](website-for-markdown/README.md) • [Changelog](website-for-markdown/CHANGELOG.md) |
| **`website-for-skill`** | End-to-end pipeline that crawls websites/APIs and builds structured AI Skills automatically. | [`0.4.0-beta`](website-for-skill/VERSION) | Beta | [README](website-for-skill/README.md) • [Changelog](website-for-skill/CHANGELOG.md) |
| **`video-to-md`** | Multi-platform video and playlist ingestion (YouTube, Vimeo, Twitch) into structured Markdown with timestamps and AI audio fallback (Whisper). | [`0.3.0-beta`](video-to-md/VERSION) | Beta | [README](video-to-md/README.md) • [Changelog](video-to-md/CHANGELOG.md) |
| **`image-to-prompt`** | High-fidelity visual reverse engineering: extracts art styles, eras, clothing, lighting, camera angles, and facial physiognomy to create generative prompts (Sora, Nano Banana, Midjourney, DALL-E 3, SDXL, Flux). | [`0.3.0-beta`](image-to-prompt/VERSION) | Beta | [README](image-to-prompt/README.md) • [Changelog](image-to-prompt/CHANGELOG.md) |
| **`master-of-foundryvtt`** | Master development, architecture, scripting, rule ingestion suite (100+ RPG systems), Foundry Next Factory (FNF), sensory & cognitive accessibility (TEA/ADHD), Code Mode and native MCP Server for Foundry VTT (v8–v14) by GM Charles Corrêa. | [`0.22.0-beta`](master-of-foundryvtt/VERSION) | Beta | [README](master-of-foundryvtt/README.md) • [Changelog](master-of-foundryvtt/CHANGELOG.md) |
| **`master-of-gravewright`** | Cross-VTT reverse engineering (Foundry/Roll20), system/module development, compendiums, rules ingestion, Code Mode, SQLite management, native MCP Server, and Git/PostgreSQL toolchain for the open-source Brazilian Gravewright VTT (Python/Django). | [`0.5.0-beta`](master-of-gravewright/VERSION) | Beta | [README](master-of-gravewright/README.md) • [Changelog](master-of-gravewright/CHANGELOG.md) |
| **`bootstrap-ux-ui-plus`** | Master cognitive UX laws, Nielsen heuristics, WCAG 2.2 AA, Peter Morville Honeycomb, Color Psychology (Eva Heller), neurodiversity (ADHD & Autism TEA), W3Schools HTML5/CSS3 Standards, and fluid microinteractions with Bootstrap (v5.3 & v6.0). | [`0.7.0-beta`](bootstrap-ux-ui-plus/VERSION) | Beta | [README](bootstrap-ux-ui-plus/README.md) • [Changelog](bootstrap-ux-ui-plus/CHANGELOG.md) |
| **`humanizer-plus`** | Multi-layer AI de-watermarking, Unicode sanitization (ZWSP, BOM), and natural human text rewrite engine (PT-BR & EN). | [`1.3.0`](humanizer-plus/VERSION) | Stable | [README](humanizer-plus/README.md) • [Changelog](humanizer-plus/CHANGELOG.md) |
| **`php-dev-expert`** | Senior Software Engineer skill focused on PHP (7.4 to 8.5), modern patterns, debugging, frameworks, and Generative AI with LLPhant. | [`0.10.0-beta`](php-dev-expert/VERSION) | Beta | [README](php-dev-expert/README.md) • [Changelog](php-dev-expert/CHANGELOG.md) |
| **`python-dev-expert`** | Python expert skill covering Web (Django/FastAPI), CLI, Data Science, modern type hinting, and Ruff. | [`0.5.0-beta`](python-dev-expert/VERSION) | Beta | [README](python-dev-expert/README.md) • [Changelog](python-dev-expert/CHANGELOG.md) |
| **`docker-master`** | DevOps specialist for container optimization, security, local environments, Kiri and Podman runtimes, multi-cloud Kubernetes, and smart OS detection. | [`0.4.0-beta`](docker-master/VERSION) | Beta | [Skill](docker-master/SKILL.md) • [Changelog](docker-master/CHANGELOG.md) |
| **`book-formatter`** | Book formatting and RPG book diagramming suite: SOTA layout engines (Docling, Marker, Unstructured, Nougat, Stirling-PDF), rules segmentation for AI/RAG/MCP, color theory for RPG layouts, ADHD/neurodiversity editorial guidelines, and grill-me alignment. | [`0.18.0-beta`](book-formatter/VERSION) | Beta | [Skill](book-formatter/SKILL.md) • [Changelog](book-formatter/CHANGELOG.md) • [Glossary](book-formatter/glossarys/glossary.md) |
| **`not-today-adhd`** | Cognitive accessibility and productivity suite for neurodivergent developers and AI agents (ADHD & Autism TEA): micro-chunking, bionic reading, literal microcopy, and decision-fatigue shielding. | [`1.2.0-beta`](not-today-adhd/VERSION) | Beta | [README](not-today-adhd/README.md) • [Changelog](not-today-adhd/CHANGELOG.md) |
| **`sms-legal`** | Complete integration suite and native MCP Server (Node.js & Python) for SMS Legal / SMS Gateway API. Multi-language SDKs (PHP, Python, JS), batch sending, scheduling, voice, audio, and bi-directional replies. | [`1.1.0`](sms-legal/VERSION) | Stable | [README](sms-legal/README.md) • [Changelog](sms-legal/CHANGELOG.md) |
| **`mcp-builder`** | Universal MCP Server Generator, Security Hardener, and Orchestrator for PHP 8.4+, Python 3.12+, and Node.js 22+. Features Code Mode architecture guidance, prompt injection defense, static code analysis (SAST), fail-safe background GitHub issue reporting, and self-updating. | [`0.4.0-beta`](mcp-builder/VERSION) | Beta | [README](mcp-builder/README.md) • [Changelog](mcp-builder/CHANGELOG.md) |
| **`code-mode-builder`** | Architects, converts, and benchmarks Code Mode (Programmatic Tool Calling & Sandbox Execution) for AI Agents as an alternative or evolution to traditional MCP. | [`0.2.0-beta`](code-mode-builder/VERSION) | Beta | [README](code-mode-builder/README.md) • [Changelog](code-mode-builder/CHANGELOG.md) |
| **`second-brain-plus`** | Persistent memory, context management, and second brain orchestration via Notion API & local Markdown with auto-sync, claude-mem, graphify, caveman, headroom, and context7. | [`0.1.0-beta`](second-brain-plus/VERSION) | Beta | [README](second-brain-plus/README.md) • [Changelog](second-brain-plus/CHANGELOG.md) |

> ℹ️ *Note: All skills in this repository are currently in **Beta** and adhere to [Semantic Versioning (SemVer)](https://semver.org/spec/v2.0.0.html). Each skill contains a dedicated `VERSION` file and `CHANGELOG.md`. See also the global [**CHANGELOG.md**](CHANGELOG.md).*

---

### 🚀 How to Use

#### 1. Converting Local Documents to Markdown
Transform any PDF, Word, Excel, or PowerPoint file into clean Markdown:
```bash
python docs-for-markdown/scripts/convert_to_md.py --input "path/to/manual.pdf" --output "output_dir"
```
👉 *Detailed instructions:* [docs-for-markdown README](docs-for-markdown/README.md)

#### 2. Building a Modular Skill from a Document
Convert a raw manual or rulebook into an AI Skill ready for your agent:
```bash
python docs-for-skill/scripts/structure_skill.py --input "path/to/extracted.md" --name "my-tool-skill" --output "."
```
👉 *Detailed instructions:* [docs-for-skill README](docs-for-skill/README.md)

#### 3. Scraping a Website to Clean Markdown
Extract full web portals or API documentation using local Playwright or Firecrawl:
```bash
python website-for-markdown/scripts/scrape_site.py --url "https://example.com/docs" --engine playwright
```
👉 *Detailed instructions:* [website-for-markdown README](website-for-markdown/README.md)

#### 4. Automated End-to-End Website Skill Generation
Directly build a ready-to-use AI Skill from any live website URL:
```bash
python website-for-skill/Scripts/build_skill.py --url "https://example.com/docs" --name "my-web-skill"
```
👉 *Detailed instructions:* [website-for-skill README](website-for-skill/README.md)

#### 5. Image to Generative Prompt (Visual Reverse-Engineering)
Analyze technical image metadata and reverse-engineer rich prompts for image/video AI generators:
```bash
python image-to-prompt/scripts/analyze_image.py "path/to/image.png"
```
👉 *Detailed instructions:* [image-to-prompt README](image-to-prompt/README.md)

#### 6. Master of Foundry VTT Development, Rule Ingestion & Native MCP Server
Run the native zero-dependency MCP server or query Foundry versions, create packages, scenes, walls, lights, and automated traps:
```bash
# Run the native Node.js MCP Server (JSON-RPC 2.0 stdio):
node master-of-foundryvtt/mcp/foundry_mcp_server.js

# Scaffold a production-ready v12/v14 package (module or system):
python master-of-foundryvtt/scripts/scaffold_package.py --id "my-system" --title "My System" --type system

# Consult version migration guides:
python master-of-foundryvtt/scripts/version_advisor.py 12
```
👉 *Detailed instructions:* [master-of-foundryvtt README](master-of-foundryvtt/README.md) & [MCP Installation Guide](master-of-foundryvtt/mcp/INSTALLATION.md)

#### 7. Universal AI De-Watermarking, Code Cleanup & Humanization (Humanizer Plus)
Sanitize zero-width Unicode characters, curly smart quotes, AI generator watermarks, obvious line-by-line comments, and LLM slop from any file or codebase:
```bash
# Sanitize a specific file:
node humanizer-plus/scripts/sanitize.js "path/to/file.md"

# Dry-run inspect an entire directory:
node humanizer-plus/scripts/sanitize.js "path/to/project" --dry-run

# Check upstream rules synchronization:
node humanizer-plus/scripts/check_upstream_humanizer.js
```
👉 *Detailed instructions:* [humanizer-plus README](humanizer-plus/README.md)

#### 8. Bootstrap UX/UI Plus (Design Cognitivo, Leis de UX, Acessibilidade e Dashboards)
Build production-ready, human-centered web portals, administrative systems, and dashboards with Bootstrap 5.3 & 6.0 following the 18 Laws of UX, Jakob Nielsen's 10 Usability Heuristics, and full visual accessibility (WCAG 2.2 AA, Dyschromatopsia/Colorblindness):
```bash
# Run UX & Accessibility audit on any HTML, PHP or JSX template:
node bootstrap-ux-ui-plus/scripts/audit_ux_bootstrap.mjs path/to/page.html

# Check for Bootstrap upstream updates & repository sync with user permission gate:
node bootstrap-ux-ui-plus/scripts/check_updates.mjs
```
👉 *Detailed instructions:* [bootstrap-ux-ui-plus README](bootstrap-ux-ui-plus/README.md)

#### 9. Code Mode Architecture, Sandboxing & Tool Conversion (Code Mode Builder)
Benchmark, scaffold, and transition high-volume MCP tool schemas into lightweight TypeScript/Python Code Mode gateways:
```bash
# Check runtime environment for Code Mode (Deno, Node, Python, Docker):
python code-mode-builder/scripts/check_codemode_env.py

# Scaffold a production-ready Code Mode Gateway with test suite:
python code-mode-builder/scripts/scaffold_code_mode.py --name "my-codemode-service" --runtime node --sandbox vm2
```
👉 *Detailed instructions:* [code-mode-builder README](code-mode-builder/README.md)

#### 10. Persistent Memory, Context Optimization & AI Second Brain (Second Brain Plus)
Automate project memory persistence across Notion API and local Git vaults with real-time auto-sync:
```bash
# Save memory instantly and auto-sync to Notion, claude-mem, and graphify:
python second-brain-plus/scripts/cli.py save memory "Production environment uses Node 22 on port 8080"

# Register an immutable Architecture Decision Record (ADR):
python second-brain-plus/scripts/cli.py adr "Adopting Redis for Session Caching"

# Run continuous background watcher daemon:
python second-brain-plus/scripts/auto_sync.py --watch
```
👉 *Detailed instructions:* [second-brain-plus README](second-brain-plus/README.md)

---

## 📜 Changelog
To inspect all releases, versions, and notable changes across the repository and individual skills, see [**CHANGELOG.md**](CHANGELOG.md).

---
---

## 🇧🇷 Português

### 🎯 Por que Skills? (Motivação e Propósito)

Modelos de Linguagem de Grande Porte (LLMs) e Agentes de IA Autônomos (como Antigravity, Claude Code, GitHub Copilot, etc.) possuem excelente capacidade de raciocínio lógico e geração de código. No entanto, ao lidar com manuais extensos, documentações gigantescas de API ou regras complexas, enfrentam dois grandes gargalos:

1. **Exaustão de Context Window e Alto Custo de Tokens:** Inserir centenas de páginas em um único prompt gasta tokens excessivos por turno e causa alucinações por sobrecarga ("perda no meio do contexto").
2. **Falta de Estruturação Semântica:** Arquivos brutos contêm ruídos de layout (cabeçalhos, rodapés, tabelas quebradas, colunas misturadas e blocos de código fragmentados).

#### A Solução: Arquitetura de Skills
As **Skills** transformam dados brutos em **unidades modulares de conhecimento sob demanda**:
- **Índice Mestre (`SKILL.md`):** Modelo mental e mapa de navegação rápido para a IA.
- **Capítulos Modulares (`chapters/*.md`):** Conteúdo técnico aprofundado carregado apenas quando a pergunta do usuário requisitar aquele tópico (~10KB a 40KB por capítulo).
- **Acesso Rápido (`cheatsheet.md`, `glossary.md`, `patterns.md`):** Consultas imediatas a tabelas de regras, sintaxes, termos canônicos e padrões de arquitetura.

---

### 📦 Instalação e Configuração

#### 0. Requisitos Mandatórios do Ecossistema: GitHub CLI (`gh`) & Skills Companheiras Obrigatórias
> 🚨 **REGRA DE OURO PARA TODAS AS SKILLS (GLOBAL E NO PROJETO):**  
> Todas as skills criadas e operadas neste ecossistema levam consigo e exigem compulsoriamente:
> 1. **GitHub CLI (`gh`) Conectado e Autenticado:** Viabiliza clonagem fluida, sincronização contínua e submissão formal de issues no repositório (`gh issue create --repo CharlesCorreaDev/skills-ai`).
>    - **Windows:** `winget install GitHub.cli` ou `choco install gh`
>    - **macOS:** `brew install gh`
>    - **Linux:** `sudo apt install gh`
>    - **Autenticar:** `gh auth login`
>
> 2. **Tríade Obrigatória de Skills Companheiras (Disponíveis Globalmente e no Projeto):**  
>    Toda skill sempre operará em conjunto com:
>    - **`andrej-karpathy-skills`** (`https://github.com/multica-ai/andrej-karpathy-skills`): Engenharia de software pragmática, código mínimo, validação contínua e ausência de suposições cegas.
>    - **`grill-me`** (`https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me`): Entrevista profunda e estruturada com o autor/usuário antes de iniciar tarefas para evitar retrabalho.
>    - **`skills-code-review`** (`https://www.aihero.dev/skills-code-review`): Revisão rigorosa de código automatizada e portão de qualidade pré-entrega.
>    ```bash
>    # Instalar globalmente e no projeto local
>    npx skills@latest add multica-ai/andrej-karpathy-skills
>    npx skills@latest add mattpocock/skills --skill=grill-me
>    npx skills@latest add aihero-dev/skills-code-review
>    ```

#### 1. Clonar o Repositório
```bash
git clone https://github.com/CharlesCorreaDev/skills-ai.git
cd skills-ai
```

#### 2. Criar Ambiente Virtual e Instalar Dependências Python
```bash
# Criar e ativar o ambiente virtual
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate

# Instalar bibliotecas de extração e raspagem
pip install markitdown pdfminer.six pdfplumber pypdf python-docx mammoth openpyxl pandas python-pptx markdownify beautifulsoup4 firecrawl-py playwright

# Instalar os navegadores para raspagem web (Playwright)
playwright install chromium
```

#### 3. Binários do Sistema Opcionais (Para Cobertura Total de Formatos e OCR)
Para conversão de formatos legados (`.doc`, `.ppt`, LibreOffice `.odt` e OCR em imagens escaneadas):

- **Windows (via Winget ou Chocolatey):**
  ```powershell
  winget install JohnMacFarlane.Pandoc TheDocumentFoundation.LibreOffice UB-Mannheim.TesseractOCR
  ```
- **Ubuntu / Debian:**
  ```bash
  sudo apt-get update && sudo apt-get install -y pandoc libreoffice tesseract-ocr poppler-utils
  ```
- **macOS (via Homebrew):**
  ```bash
  brew install pandoc libreoffice tesseract poppler
  ```

#### 4. Instalando as Skills no seu Agente de IA
Para que seu agente reconheça as skills, copie ou crie links simbólicos das pastas de skills para a pasta de configuração do seu agente:

| Agente / Ferramenta | Raiz no Projeto (Local) | Raiz Global do Usuário |
|---|---|---|
| **Antigravity** | `.agents/skills/<nome-da-skill>/` | `~/.gemini/config/skills/<nome-da-skill>/` |
| **Claude Code** | `.claude/skills/<nome-da-skill>/` | `~/.claude/skills/<nome-da-skill>/` |
| **Copilot Workspace** | `.github/skills/<nome-da-skill>/` | `~/.copilot/skills/<nome-da-skill>/` |

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (pandoc, libreoffice, tesseract), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).

---

| Skill | Finalidade | Versão | Status | Documentação & Changelog |
|---|---|---|---|---|
| **`docs-for-markdown`** | Conversor universal de documentos multiformato (PDF, DOCX, XLSX, PPTX, ODT, HTML, RTF) para Markdown limpo. | [`0.3.0-beta`](docs-for-markdown/VERSION) | Beta | [README](docs-for-markdown/README.md) • [Changelog](docs-for-markdown/CHANGELOG.md) |
| **`docs-for-skill`** | Transforma Markdowns extraídos de documentos em Skills modulares de alto desempenho para IA. | [`0.4.0-beta`](docs-for-skill/VERSION) | Beta | [README](docs-for-skill/README.md) • [Changelog](docs-for-skill/CHANGELOG.md) |
| **`website-for-markdown`** | Motor híbrido de raspagem web (Firecrawl + Playwright/Chromium) para extração de Markdown limpo a partir de sites e SPAs. | [`0.4.0-beta`](website-for-markdown/VERSION) | Beta | [README](website-for-markdown/README.md) • [Changelog](website-for-markdown/CHANGELOG.md) |
| **`website-for-skill`** | Pipeline completo que rastreia websites/APIs e compila Skills de IA estruturadas automaticamente. | [`0.4.0-beta`](website-for-skill/VERSION) | Beta | [README](website-for-skill/README.md) • [Changelog](website-for-skill/CHANGELOG.md) |
| **`video-to-md`** | Captura multiplataforma de vídeos e playlists (YouTube, Vimeo, Twitch) em Markdown estruturado com timestamps clicáveis e fallback por áudio via IA (Whisper). | [`0.3.0-beta`](video-to-md/VERSION) | Beta | [README](video-to-md/README.md) • [Changelog](video-to-md/CHANGELOG.md) |
| **`image-to-prompt`** | Engenharia reversa visual de alta fidelidade: extrai traços artísticos, época, vestimentas, iluminação, fisionomia e câmeras para gerar prompts de imagem/vídeo (Sora, Nano Banana, Midjourney, DALL-E 3, SDXL, Flux). | [`0.3.0-beta`](image-to-prompt/VERSION) | Beta | [README](image-to-prompt/README.md) • [Changelog](image-to-prompt/CHANGELOG.md) |
| **`master-of-foundryvtt`** | Suíte mestra de desenvolvimento, arquitetura, scripting, ingestão de regras (+100 sistemas de RPG), Foundry Next Factory (FNF), ergonomia sensorial e acessibilidade cognitiva (TEA/TDAH), Code Mode e Servidor MCP Nativo para Foundry VTT (v8–v14) por GM Charles Corrêa. | [`0.22.0-beta`](master-of-foundryvtt/VERSION) | Beta | [README](master-of-foundryvtt/README.md) • [Changelog](master-of-foundryvtt/CHANGELOG.md) |
| **`master-of-gravewright`** | Engenharia reversa Cross-VTT (Foundry/Roll20), desenvolvimento de sistemas e módulos, compêndios, regras, Code Mode, gestão SQLite, Servidor MCP Nativo e suporte a Git/PostgreSQL para o VTT open-source brasileiro Gravewright (Python/Django). | [`0.5.0-beta`](master-of-gravewright/VERSION) | Beta | [README](master-of-gravewright/README.md) • [Changelog](master-of-gravewright/CHANGELOG.md) |
| **`bootstrap-ux-ui-plus`** | Engenharia cognitiva de usabilidade (Leis de UX, Heurísticas de Nielsen), acessibilidade WCAG 2.2 AA, Colmeia de Morville, Psicologia das Cores (Eva Heller), neurodiversidade (TDAH & TEA), padrões canônicos W3Schools HTML5/CSS3 e microinterações fluidas com Bootstrap (v5.3 e v6.0). | [`0.7.0-beta`](bootstrap-ux-ui-plus/VERSION) | Beta | [README](bootstrap-ux-ui-plus/README.md) • [Changelog](bootstrap-ux-ui-plus/CHANGELOG.md) |
| **`humanizer-plus`** | Desmarcação de IA multicamada, purga de Unicode invisível (ZWSP, BOM), normalização de código e reescrita natural com voz humana real (PT-BR e EN). | [`1.3.0`](humanizer-plus/VERSION) | Estável | [README](humanizer-plus/README.md) • [Changelog](humanizer-plus/CHANGELOG.md) |
| **`php-dev-expert`** | Skill de Engenheiro de Software Sênior focada em PHP (7.4 a 8.5), arquitetura moderna, debugging, frameworks e IA Generativa/RAG com LLPhant. | [`0.10.0-beta`](php-dev-expert/VERSION) | Beta | [README](php-dev-expert/README.md) • [Changelog](php-dev-expert/CHANGELOG.md) |
| **`python-dev-expert`** | Especialista Python abordando Web (Django/FastAPI), Automações, Data Science, tipagem avançada e Ruff. | [`0.5.0-beta`](python-dev-expert/VERSION) | Beta | [Skill](python-dev-expert/SKILL.md) • [Changelog](python-dev-expert/CHANGELOG.md) |
| **`docker-master`** | Especialista DevOps para otimização de contêineres, segurança, Compose, runtimes Kiri e Podman, orquestração multi-cloud Kubernetes e detecção inteligente de SO. | [`0.4.0-beta`](docker-master/VERSION) | Beta | [Skill](docker-master/SKILL.md) • [Changelog](docker-master/CHANGELOG.md) |
| **`book-formatter`** | Suíte de formatação de livros e diagramação de livros de RPG: motores SOTA de IA (Docling, Marker, Unstructured, Nougat, Stirling-PDF), segmentação de regras para IA/RAG/MCP, teoria das cores para layouts de RPG, diretrizes editoriais para TDAH/neurodiversidade e alinhamento grill-me. | [`0.18.0-beta`](book-formatter/VERSION) | Beta | [Skill](book-formatter/SKILL.md) • [Changelog](book-formatter/CHANGELOG.md) • [Glossário](book-formatter/glossarys/glossary.md) |
| **`not-today-adhd`** | Suíte de acessibilidade cognitiva e produtividade para desenvolvedores e agentes de IA neurodivergentes (TDAH & Autismo TEA): micro-chunking, leitura biônica, microcópia literal e blindagem contra fadiga de decisão. | [`1.2.0-beta`](not-today-adhd/VERSION) | Beta | [README](not-today-adhd/README.md) • [Changelog](not-today-adhd/CHANGELOG.md) |
| **`sms-legal`** | Suíte completa de integração e Servidor MCP Nativo (Node.js & Python) para a API SMS Legal / SMS Gateway. SDKs multilinguagem (PHP, Python, JS), envio em lote, agendamento, voz, áudio e captura de respostas. | [`1.1.0`](sms-legal/VERSION) | Estável | [README](sms-legal/README.md) • [Changelog](sms-legal/CHANGELOG.md) |
| **`mcp-builder`** | Gerador, blindador de segurança e configurador universal de servidores Model Context Protocol (MCP) para PHP 8.4+, Python 3.12+ e Node.js 22+. Defesa contra prompt injection, arquitetura Code Mode, análise estática de código (SAST), fail-safe com abertura automática de issues no GitHub e auto-update. | [`0.4.0-beta`](mcp-builder/VERSION) | Beta | [README](mcp-builder/README.md) • [Changelog](mcp-builder/CHANGELOG.md) |
| **`code-mode-builder`** | Arquiteta, converte e avalia Code Mode (Chamada Programática de Ferramentas e Execução Sandboxed) para Agentes de IA como alternativa ou evolução do MCP tradicional. | [`0.2.0-beta`](code-mode-builder/VERSION) | Beta | [README](code-mode-builder/README.md) • [Changelog](code-mode-builder/CHANGELOG.md) |
| **`second-brain-plus`** | Suíte de memória persistente, gestão de contexto e Segundo Cérebro para Agentes de IA com Notion API, cofre local Markdown, auto-sync em tempo real, claude-mem, graphify, caveman, headroom, context7 e modo TDAH. | [`0.1.0-beta`](second-brain-plus/VERSION) | Beta | [README](second-brain-plus/README.md) • [Changelog](second-brain-plus/CHANGELOG.md) |

> ℹ️ *Nota: Todas as skills deste repositório encontram-se em estágio **Beta** e aderem ao [Versionamento Semântico (SemVer)](https://semver.org/spec/v2.0.0.html). Cada skill conta com seu arquivo individual `VERSION` e `CHANGELOG.md`. Veja também o histórico global no [**CHANGELOG.md**](CHANGELOG.md).*

---

### 🚀 Modos de Uso

#### 1. Conversão de Documentos Locais para Markdown
Converta qualquer PDF, Word, Excel ou apresentação em Markdown limpo:
```bash
python docs-for-markdown/scripts/convert_to_md.py --input "caminho/do/arquivo.pdf" --output "pasta_saida"
```
👉 *Consulte o guia completo:* [README do docs-for-markdown](docs-for-markdown/README.md)

#### 2. Criando uma Skill Modular a partir de um Documento
Estruture o conteúdo extraído em capítulos e arquivos de referência para Agentes de IA:
```bash
python docs-for-skill/scripts/structure_skill.py --input "caminho/extraido.md" --name "minha-skill" --output "."
```
👉 *Consulte o guia completo:* [README do docs-for-skill](docs-for-skill/README.md)

#### 3. Capturando Websites em Markdown
Extraia portais inteiros ou documentações web usando Playwright local ou Firecrawl:
```bash
python website-for-markdown/scripts/scrape_site.py --url "https://exemplo.com/docs" --engine playwright
```
👉 *Consulte o guia completo:* [README do website-for-markdown](website-for-markdown/README.md)

#### 4. Gerando uma Skill Automática a partir de uma URL Web
Construa uma Skill completa e pronta para uso diretamente da URL de documentação:
```bash
python website-for-skill/Scripts/build_skill.py --url "https://exemplo.com/docs" --name "minha-web-skill"
```
👉 *Consulte o guia completo:* [README do website-for-skill](website-for-skill/README.md)

#### 5. Imagem para Prompt Generativo (Engenharia Reversa Visual)
Analise propriedades técnicas de imagens e faça a engenharia reversa de prompts descritivos para IA:
```bash
python image-to-prompt/scripts/analyze_image.py "caminho/da/imagem.png"
```
👉 *Consulte o guia completo:* [README do image-to-prompt](image-to-prompt/README.md)

#### 6. Mestria em Desenvolvimento, Ingestão de Regras e Servidor MCP Nativo para Foundry VTT
Execute o servidor MCP nativo com zero dependências externas ou consulte versões, crie pacotes, cenas, paredes, luzes e armadilhas automatizadas:
```bash
# Executar o Servidor MCP Nativo em Node.js (JSON-RPC 2.0 via stdio):
node master-of-foundryvtt/mcp/foundry_mcp_server.js

# Gerar scaffold de módulo ou sistema pronto para Foundry v12/v14:
python master-of-foundryvtt/scripts/scaffold_package.py --id "meu-sistema" --title "Meu Sistema" --type system

# Consultar guia de migração e versões:
python master-of-foundryvtt/scripts/version_advisor.py 12
```
👉 *Consulte o guia completo:* [README do master-of-foundryvtt](master-of-foundryvtt/README.md) & [Manual de Instalação do MCP](master-of-foundryvtt/mcp/INSTALLATION.md)

#### 7. Desmarcação de IA Universal, Limpeza de Código e Humanização (Humanizer Plus)
Higienize caracteres Unicode invisíveis, aspas curvas tipográficas, marcas d'água de ferramentas de IA, comentários óbvios linha a linha e vícios narrativos (*slop*) de qualquer arquivo ou código:
```bash
# Higienizar um arquivo específico:
node humanizer-plus/scripts/sanitize.js "caminho/do/arquivo.md"

# Inspeção em lote sem aplicar alterações (--dry-run):
node humanizer-plus/scripts/sanitize.js "pasta/do/projeto" --dry-run

# Verificar sincronização com o repositório upstream:
node humanizer-plus/scripts/check_upstream_humanizer.js
```
👉 *Consulte o guia completo:* [README do humanizer-plus](humanizer-plus/README.md)

#### 8. Bootstrap UX/UI Plus (Design Cognitivo, Leis de UX, Acessibilidade e Dashboards)
Construa portais web, sistemas administrativos e dashboards com Bootstrap 5.3 e 6.0 aplicando as 18 Leis do UX, as 10 Heurísticas de Nielsen e acessibilidade visual completa (WCAG 2.2 AA, daltonismo e baixa visão):
```bash
# Executar auditoria de UX e Acessibilidade em templates HTML, PHP ou JSX:
node bootstrap-ux-ui-plus/scripts/audit_ux_bootstrap.mjs caminho/do/template.html

# Verificar novas versões do Bootstrap e da skill com confirmação do usuário:
node bootstrap-ux-ui-plus/scripts/check_updates.mjs
```
👉 *Consulte o guia completo:* [README do bootstrap-ux-ui-plus](bootstrap-ux-ui-plus/README.md)

#### 9. Arquitetura Code Mode, Sandboxing e Conversão de Ferramentas (Code Mode Builder)
Avalie, gere scaffolds e faça a transição de dezenas de ferramentas MCP para gateways leves de Code Mode em TypeScript ou Python:
```bash
# Verificar ambiente de execução para Code Mode (Deno, Node, Python, Docker):
python code-mode-builder/scripts/check_codemode_env.py

# Gerar scaffold de Gateway Code Mode pronto para produção com suíte de testes:
python code-mode-builder/scripts/scaffold_code_mode.py --name "meu-servico-codemode" --runtime node --sandbox vm2
```
👉 *Consulte o guia completo:* [README do code-mode-builder](code-mode-builder/README.md)

#### 10. Memória Persistente, Otimização de Contexto e Segundo Cérebro (Second Brain Plus)
Automatize a persistência de memória e contexto entre Notion API e cofre Git local com auto-sync em tempo real:
```bash
# Salvar memória instantaneamente e sincronizar com Notion, claude-mem e graphify:
python second-brain-plus/scripts/cli.py save memory "O ambiente de produção usa Node 22 na porta 8080"

# Registrar uma Decisão Arquitetural (ADR) inviolável contra alucinações:
python second-brain-plus/scripts/cli.py adr "Adoção de Redis para Cache de Sessões"

# Monitoramento contínuo em segundo plano:
python second-brain-plus/scripts/auto_sync.py --watch
```
👉 *Consulte o guia completo:* [README do second-brain-plus](second-brain-plus/README.md)

---

## 📜 Changelog
Para conferir o histórico completo de versões e alterações, consulte o arquivo [**CHANGELOG.md**](CHANGELOG.md).

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)