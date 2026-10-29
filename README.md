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
| **`docs-for-markdown`** | Universal converter for multi-format documents (PDF, DOCX, XLSX, PPTX, ODT, HTML, RTF) into clean Markdown. | [`0.2.0-beta`](docs-for-markdown/VERSION) | Beta | [README](docs-for-markdown/README.md) • [Changelog](docs-for-markdown/CHANGELOG.md) |
| **`docs-for-skill`** | Transforms document Markdown into high-performance, modular AI Skills. | [`0.2.0-beta`](docs-for-skill/VERSION) | Beta | [README](docs-for-skill/README.md) • [Changelog](docs-for-skill/CHANGELOG.md) |
| **`website-for-markdown`** | Hybrid web scraping engine (Firecrawl + Playwright/Chromium) for clean Markdown extraction from web pages and SPAs. | [`0.3.0-beta`](website-for-markdown/VERSION) | Beta | [README](website-for-markdown/README.md) • [Changelog](website-for-markdown/CHANGELOG.md) |
| **`website-for-skill`** | End-to-end pipeline that crawls websites/APIs and builds structured AI Skills automatically. | [`0.3.0-beta`](website-for-skill/VERSION) | Beta | [README](website-for-skill/README.md) • [Changelog](website-for-skill/CHANGELOG.md) |
| **`youtube-to-md`** | Converts YouTube videos and playlists into structured Markdown (metadata, chapters and timestamped transcript) with index and manifest. | [`0.1.0-beta`](youtube-to-md/VERSION) | Beta | [README](youtube-to-md/README.md) • [Changelog](youtube-to-md/CHANGELOG.md) |
| **`image-to-prompt`** | High-fidelity visual reverse engineering: extracts art styles, eras, clothing, lighting, camera angles, and facial physiognomy to create generative prompts (Sora, Nano Banana, Midjourney, DALL-E 3, SDXL, Flux). | [`0.2.0-beta`](image-to-prompt/VERSION) | Beta | [README](image-to-prompt/README.md) • [Changelog](image-to-prompt/CHANGELOG.md) |
| **`master-of-foundryvtt`** | Master development, architecture, scripting, rule ingestion suite (100+ RPG systems) and native MCP Server for Foundry VTT (v8–v14) by GM Charles Corrêa. | [`0.16.0-beta`](master-of-foundryvtt/VERSION) | Beta | [README](master-of-foundryvtt/README.md) • [Changelog](master-of-foundryvtt/CHANGELOG.md) |
| **`humanizer-plus`** | Multi-layer AI de-watermarking, Unicode sanitization (ZWSP, BOM), and natural human text rewrite engine (PT-BR & EN). | [`1.2.0`](humanizer-plus/VERSION) | Stable | [README](humanizer-plus/README.md) • [Changelog](humanizer-plus/CHANGELOG.md) |
| **`php-dev-expert`** | Senior Software Engineer skill focused on PHP (7.4 to 8.5), modern patterns, debugging, and frameworks. | [`0.5.0-beta`](php-dev-expert/VERSION) | Beta | [Skill](php-dev-expert/SKILL.md) • [Changelog](php-dev-expert/CHANGELOG.md) |
| **`python-dev-expert`** | Python expert skill covering Web (Django/FastAPI), CLI, Data Science, and modern type hinting. | [`0.2.0-beta`](python-dev-expert/VERSION) | Beta | [Skill](python-dev-expert/SKILL.md) • [Changelog](python-dev-expert/CHANGELOG.md) |
| **`docker-master`** | DevOps specialist for Docker optimization, security, local environments, and smart OS detection. | [`0.2.0-beta`](docker-master/VERSION) | Beta | [Skill](docker-master/SKILL.md) • [Changelog](docker-master/CHANGELOG.md) |

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
| **`docs-for-markdown`** | Conversor universal de documentos multiformato (PDF, DOCX, XLSX, PPTX, ODT, HTML, RTF) para Markdown limpo. | [`0.2.0-beta`](docs-for-markdown/VERSION) | Beta | [README](docs-for-markdown/README.md) • [Changelog](docs-for-markdown/CHANGELOG.md) |
| **`docs-for-skill`** | Transforma Markdowns extraídos de documentos em Skills modulares de alto desempenho para IA. | [`0.2.0-beta`](docs-for-skill/VERSION) | Beta | [README](docs-for-skill/README.md) • [Changelog](docs-for-skill/CHANGELOG.md) |
| **`website-for-markdown`** | Motor híbrido de raspagem web (Firecrawl + Playwright/Chromium) para extração de Markdown limpo a partir de sites e SPAs. | [`0.3.0-beta`](website-for-markdown/VERSION) | Beta | [README](website-for-markdown/README.md) • [Changelog](website-for-markdown/CHANGELOG.md) |
| **`website-for-skill`** | Pipeline completo que rastreia websites/APIs e compila Skills de IA estruturadas automaticamente. | [`0.3.0-beta`](website-for-skill/VERSION) | Beta | [README](website-for-skill/README.md) • [Changelog](website-for-skill/CHANGELOG.md) |
| **`youtube-to-md`** | Converte vídeos e playlists do YouTube em Markdown estruturado (metadados, capítulos e transcrição com timestamps), com índice e manifesto. | [`0.1.0-beta`](youtube-to-md/VERSION) | Beta | [README](youtube-to-md/README.md) • [Changelog](youtube-to-md/CHANGELOG.md) |
| **`image-to-prompt`** | Engenharia reversa visual de alta fidelidade: extrai traços artísticos, época, vestimentas, iluminação, fisionomia e câmeras para gerar prompts de imagem/vídeo (Sora, Nano Banana, Midjourney, DALL-E 3, SDXL, Flux). | [`0.2.0-beta`](image-to-prompt/VERSION) | Beta | [README](image-to-prompt/README.md) • [Changelog](image-to-prompt/CHANGELOG.md) |
| **`master-of-foundryvtt`** | Suíte mestra de desenvolvimento, arquitetura, scripting, ingestão de regras (+100 sistemas de RPG) e Servidor MCP Nativo para Foundry VTT (v8–v14) por GM Charles Corrêa. | [`0.16.0-beta`](master-of-foundryvtt/VERSION) | Beta | [README](master-of-foundryvtt/README.md) • [Changelog](master-of-foundryvtt/CHANGELOG.md) |
| **`humanizer-plus`** | Desmarcação de IA multicamada, purga de Unicode invisível (ZWSP, BOM), normalização de código e reescrita natural com voz humana real (PT-BR e EN). | [`1.2.0`](humanizer-plus/VERSION) | Estável | [README](humanizer-plus/README.md) • [Changelog](humanizer-plus/CHANGELOG.md) |
| **`php-dev-expert`** | Skill de Engenheiro de Software Sênior focada em PHP (7.4 a 8.5), arquitetura moderna, debugging e frameworks. | [`0.5.0-beta`](php-dev-expert/VERSION) | Beta | [Skill](php-dev-expert/SKILL.md) • [Changelog](php-dev-expert/CHANGELOG.md) |
| **`python-dev-expert`** | Especialista Python abordando Web (Django/FastAPI), Automações, Data Science e tipagem avançada. | [`0.2.0-beta`](python-dev-expert/VERSION) | Beta | [Skill](python-dev-expert/SKILL.md) • [Changelog](python-dev-expert/CHANGELOG.md) |
| **`docker-master`** | Especialista DevOps para otimização de imagens Docker, segurança, Compose e detecção inteligente de SO. | [`0.2.0-beta`](docker-master/VERSION) | Beta | [Skill](docker-master/SKILL.md) • [Changelog](docker-master/CHANGELOG.md) |

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