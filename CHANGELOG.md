# Changelog 📜⚡

All notable changes to the **Skills AI** repository will be documented in this file.  
*Todas as alterações notáveis no repositório **Skills AI** serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.27.0] - 2026-11-12

### Added / Adicionado
- **Lançamento do `bootstrap-ux-ui-plus` v0.5.0-beta:**
  - **Clone do Mazer com Documentação Viva (`templates/admin-dashboard-template.html`):** Arquitetura `#app > #sidebar + #main` com exemplos práticos e documentação em HTML de grids, breakpoints, formulários acessíveis, floating labels, validação WCAG, botões semânticos, badges, modais com focus trapping, toasts e painel de inclusão TEA/TDAH.
  - **Template Canônico do AdminKit (`templates/adminkit-dashboard-template.html`):** Estrutura `.wrapper > nav.sidebar + div.main` com design minimalista, topbar flexível e cards com elevação sutil.
  - **Fundamentos Canônicos de UI Design (`fundamentals/ui-design-core-principles.md`):** Os 6 princípios canônicos do UI Design (Clareza, Consistência, Hierarquia Visual, Eficiência, Tolerância a Erros e Ritmo Base 4/8px) e regras contra AI slop visual.
  - **Human Interface Guidelines (HIG) Comparadas (`standards/human-interface-guidelines-and-design-systems.md`):** Apple HIG (Deferência, Clareza, Profundidade, cantos orgânicos, vidro fosco), Microsoft Fluent UI, GNOME e KDE.
  - **Repositórios de Inspiração e Ferramentas (`references/ui-inspiration-and-pattern-libraries.md`):** Mapeamento de UI Patterns, UI Design Daily, UI Skills, Figma UI Kits, Awwwards, Dribbble, Uizard, Pixso, Canva e Maze.
  - **Bilinguismo Completo (PT-BR / EN):** Tradução e estruturação bilíngue em todos os guias mestres e templates.

---

## [1.26.0] - 2026-11-12

### Added / Adicionado
- **Expansão de UX/UI, Psicologia das Cores & Ergonomia Sensorial em Todo o Ecossistema:**
  - **ootstrap-ux-ui-plus (0.4.0-beta):**
    - Integração dos Fundamentos Canônicos de UX Design & Negócios com a Colmeia de 7 Facetas de Peter Morville, Duplo Diamante e métricas de CRO com redução de atrito (Mandaê, Figma, EBAC, Alura, Adobe Express, Catarinas, Tuia).
    - Módulo de Acessibilidade no Espectro Autista (TEA) com a Matriz dos 7 Vetores da Dissertação de Mestrado UFPE (2025) por Lucas Silva e mitigação de sobrecarga sensorial (*Interference Journal*, *Brasil UX Design*, *Ladies That UX BR*).
    - Módulo de Ergonomia Cognitiva para TDAH (*Fast Company*, *Revista Projética / UEL*, *Homem Máquina*, *DIO.me*).
    - Compêndio de Psicologia das Cores (Eva Heller, Goethe, Lüscher), Neuromarketing, Regra 60-30-10, Design Informado Culturalmente e modelos técnicos Hex, RGB, HSL, CMYK, XYZ, Yxy e LAB (*Muzli*, *Buzzvel*, *Toptal*, *ESPM*, *Supercharge*, *TerraLab*).
    - Catálogo de componentes acessíveis, padrões de animação GPU em CSS3, e guia mestre de JavaScript Moderno, jQuery 3.7+ e jQuery UI 1.14+.
  - **master-of-foundryvtt (0.20.0-beta):**
    - Criação do Guia de Ergonomia Sensorial e Acessibilidade Cognitiva em Foundry VTT (guides/sensory-and-cognitive-accessibility.md) aplicando os 7 Vetores da UFPE para fichas e janelas ApplicationV2.
    - Padrões de conforto sonoro (eliminação de autoplay, sons suaves de dados), modo de conforto sensorial em SCSS com fontes clinicamente testadas (Atkinson Hyperlegible, Lexend) e diálogo de confirmação em ações destrutivas.
  - **
ot-today-adhd (1.2.0-beta):**
    - Ingestão das diretrizes de TEA e redução de sobrecarga sensorial, linguagem puramente literal (sem metáforas abstratas), pareamento obrigatório de ícone + texto e largura ergonômica de leitura de 45 a 65 caracteres por linha (
eferences/cognitive-formatting.md).
  - **ook-formatter (0.17.0-beta):**
    - Diretrizes de diagramação editorial inclusiva para TDAH com leitura biônica e caixas de destaque (
eurodiversity/adhd-editorial-layout-guide.md).
    - Teoria das cores aplicada a livros de RPG por gênero e prevenção de halação visual (design-systems/color-theory-and-rpg-layouts.md).
  - **docker-master (0.4.0-beta):**
    - Suporte a múltiplos runtimes de contêineres: Docker Engine, Kiri (gerenciador Rust leve) e Podman rootless nativo.
    - Otimização de performance com .wslconfig e tuning de I/O em Windows/Linux.
    - Guia mestre de orquestração Kubernetes Multi-Cloud (AWS EKS, GCP GKE, Azure AKS, Oracle OKE e DigitalOcean DOKS).
    - Ferramental companheiro expandido: Lazydocker, Trivy, Hadolint, SlimToolkit e Testcontainers.

---

## [1.25.0] - 2026-11-10

### Added / Adicionado
- **Engenharia Reversa Cross-VTT & Adaptação de Módulos no `master-of-gravewright` (`v0.3.0-beta`):**
  - Integração do protocolo de engenharia reversa via `rea-agents` para desconstruir sistemas, módulos e mecânicas do Foundry VTT, Roll20 e Fantasy Grounds e adaptá-los com precisão para os domínios nativos do Gravewright VTT (`actors`, `items`, `tokens`, `combat`, `services.py` e WebSockets).
  - Criação do [Guia de Engenharia Reversa e Adaptação Cross-VTT](master-of-gravewright/docs/reverse-engineering-cross-vtt.md) com matriz de equivalência Foundry ➔ Gravewright e 4 fases de desconstrução ancoradas nas regras oficiais de Porte Ético.

---

## [1.24.0] - 2026-11-10

### Added / Adicionado
- **Servidor MCP Nativo & Skills para Git, SQLite e PostgreSQL no `master-of-gravewright` (`v0.2.0-beta`):**
  - **Servidor MCP Nativo (`master-of-gravewright-mcp`):** Implementado servidor stdio JSON-RPC 2.0 em Python zero-dependency (`master-of-gravewright/mcp/gravewright_mcp_server.py`) expondo 6 ferramentas para o agente de IA interagir com projetos Gravewright em tempo real.
  - **Skills de Banco de Dados (`microsoft/postgres-skills`):** Integração com SQLite local e PostgreSQL para ambientes de produção com Django ORM e WebSockets (`docs/database-guide.md`).
  - **Skills de Controle de Versão (Git & GitHub):** Padronização de repositórios, `.gitignore`, tags SemVer e empacotamento de extensões para o Marketplace (`docs/git-guide.md`).

---

## [1.23.0] - 2026-11-10

### Added / Adicionado
- **Nova Skill Oficial: `master-of-gravewright` (`v0.1.0-beta`):**
  - Engenharia reversa completa do **[Gravewright VTT](https://gravewright.com/)** (`Gravewright/gravewright`), o Virtual Tabletop open-source brasileiro desenvolvido em Python 3.12+, Astral `uv`, Django 5.x/6.x, Jinja2 e Django Channels (WebSockets).
  - **Diagnóstico de Ambiente & Scaffolder (`scripts/setup_dev_env.py`):** Script em Python com comentários e saídas bilíngues (EN e pt-BR) que avalia os requisitos do sistema (Python, uv, Git) e cria módulos de navegador (`browser-module`) ou extensões de servidor (`django-app-module`) com `manifest.json` canônico.
  - **Acervo Offline Bilíngue Completo (`docs/en/` e `docs/pt-BR/`):** 50 guias técnicos cobrindo arquitetura, code map, APIs, módulos, frontend, campaign management, clocks, clues, mindmaps, map builder, PDF system, universal VTT (UVTT), runners e ethical porting.
  - **Integração Mandatória com Skills Parceiras:** Pareamento obrigatório com `python-dev-expert` para o backend Django, `bootstrap-ux-ui-plus` para ergonomia e acessibilidade de UI, e a dupla `cloudflare/security-audit-skill` & `NVIDIA/auto-ontology`.

---

## [1.22.0] - 2026-11-09

### Added / Adicionado
- **Integração Mandatória do Foundry Next Factory (FNF) no `master-of-foundryvtt` (`v0.19.0-beta`):**
  - Adoção oficial do [Foundry Next Factory](https://github.com/CharlesCorreaDev/fvtt-modules-plus/tree/main/foundry-next-factory) (`CharlesCorreaDev/fvtt-modules-plus/foundry-next-factory`) como motor de scaffolding e CLI para criação de novos módulos e sistemas de RPG do zero para Foundry VTT v13, v14.369 Stable e v15+.
  - Suporte nativo aos presets `vite-ts-appv2` (Vite 6+, TypeScript estrito, `ApplicationV2`, `HandlebarsApplicationMixin` e `TypeDataModel`) e `vanilla-esm` (Zero-build, JavaScript ESModules direto com isolamento de CSS).

---

## [1.21.0] - 2026-11-09

### Added / Adicionado
- **Blindagem Universal de Segurança (Cloudflare Security Audit) & Anti-Alucinação Numérica (NVIDIA Auto-Ontology):**
  - **Todas as 16 Skills:** Incorporadas diretrizes obrigatórias de auditoria em 6 fases com `cloudflare/security-audit-skill` e proibição absoluta de invenção de números inexistentes com `NVIDIA/auto-ontology` (`docs-for-skill/security-audit-and-auto-ontology.md`). Em skills de desenvolvimento, sempre que algo for criado ou alterado, a IA deve rodar análise e auto-reparar qualquer falha ou vazamento de dados.
- **Python Developer Expert (`v0.4.0-beta`):**
  - Adoção oficial do **Ruff (Astral)** como linter e formatador de código ultrarrápido em Rust (`docs.astral.sh/ruff`), substituindo Flake8, Black, isort e pyupgrade (`python-dev-expert/ruff-guide.md`).
- **Master of Foundry VTT (`v0.18.0-beta`):**
  - Guia mestre completo de Deploy e Instalação do Foundry VTT 24/7 em Nuvens e VPS (`master-of-foundryvtt/cloud-deployment-guide.md`): Oracle Cloud (Always Free ARM Ampere 24GB), AWS (EC2), Google Cloud (GCP via `github.com/google/skills`), Microsoft Azure e Hostinger VPS (KVM Linux), com reverse proxy Caddy (SSL automático HTTPS) e PM2.
- **Atualização SemVer em Lote de Todas as Skills:**
  - `book-formatter`: `0.16.0-beta`
  - `bootstrap-ux-ui-plus`: `0.3.0-beta`
  - `docker-master`: `0.3.0-beta`
  - `docs-for-markdown`: `0.3.0-beta`
  - `docs-for-skill`: `0.3.0-beta`
  - `humanizer-plus`: `1.3.0`
  - `image-to-prompt`: `0.3.0-beta`
  - `master-of-foundryvtt`: `0.18.0-beta`
  - `mcp-builder`: `0.2.0-beta`
  - `not-today-adhd`: `0.2.0-beta`
  - `php-dev-expert`: `0.9.0-beta`
  - `python-dev-expert`: `0.4.0-beta`
  - `sms-legal`: `1.1.0`
  - `video-to-md`: `0.3.0-beta`
  - `website-for-markdown`: `0.4.0-beta`
  - `website-for-skill`: `0.4.0-beta`

---

## [1.20.0] - 2026-11-09

### Added / Adicionado
- **Integração de IA Generativa, RAG & Agentes com LLPhant no `php-dev-expert` (`v0.8.0-beta`):**
  - Incorporação do framework SOTA [LLPhant](https://github.com/theodo-group/LLPhant) (`theodo-group/llphant`) — o "LangChain do ecossistema PHP".
  - **Pipelines RAG:** Leitura de arquivos (`FileDataReader`), chunking inteligente (`DocumentSplitter`), geração de embeddings vetoriais (OpenAI, Mistral, Ollama) e armazenamento vetorial com PostgreSQL (`pgvector` via Doctrine), Redis, Qdrant, Chroma, ElasticSearch e Memory.
  - **Agentes com Function Calling (Tools):** Execução orientada a reflexão de métodos PHP nativos (`FunctionBuilder`) para acionar APIs e tarefas de negócio a partir do modelo de linguagem.
  - **Guardrails & Segurança de Prompt:** Detecção e bloqueio de Prompt Injections com `ClassifierPromptInjectionQueryTransformer` e suporte a fluxos Human-in-the-Loop.
  - **Guia Mestre & Documentação Offline:** Adicionados [`php-dev-expert/php-docs/llphant-framework-guide.md`](php-dev-expert/php-docs/llphant-framework-guide.md) e acervo de documentação offline oficial do LLPhant em Markdown em [`php-dev-expert/php-docs/llphant/`](php-dev-expert/php-docs/llphant/).

---

## [1.19.0] - 2026-11-09

### Added / Adicionado
- **Atualização SemVer em Lote das Skills do Ecossistema:**
  - **`python-dev-expert` (`v0.3.0-beta`):** Documentação offline completa em Markdown do Python (pt-br 3.15, 550+ arquivos) e Django (6.1, 680+ arquivos) com índices mestres para economia extrema de tokens; blindagem contra CVEs recentes (2024–2026); mandato de `PDF Oxide` em 1º Lugar; integração oficial Django + `bootstrap-ux-ui-plus`; e padrões de engenharia SOTA (TDD, Systematic Debugging, `structlog`, `pydantic-settings`, Trail of Bits e novo `README.md`).
  - **`php-dev-expert` (`v0.7.0-beta`):** Mandato de prioridade absoluta para `PDF Oxide` (`oxide/pdf-oxide` via FFI); mandato de instalação e uso da skill companheira `bootstrap-ux-ui-plus`; tríade Impeccable Design, Systematic Debugging e Trail of Bits Security; e novo `README.md` bilíngue oficial.
  - **`bootstrap-ux-ui-plus` (`v0.2.0-beta`):** Integração com `whaleyxbt/claude-motion` para animações fluidas aceleradas por GPU; tríade Impeccable Design (anti-slop visual de Paul Bakaus), Systematic Debugging e segurança Trail of Bits; e compatibilidade multiplataforma.
  - **`master-of-foundryvtt` (`v0.17.0-beta`):** Integração do `pdf-oxide` em 1º Lugar para ingestão de PDFs de RPG sem travar o event loop do Node.js; motion design para sheets com `Claude-Motion`; e tríade canônica Impeccable, Debugging e Trail of Bits.
  - **`book-formatter` (`v0.15.0-beta`):** Elevação do `PDF Oxide` (`pdf_oxide`) ao topo da matriz como motor primário mandatório em 1º Lugar para diagramação e extração de layouts de PDFs (~0.8ms); diretrizes Impeccable contra quebras artificiais de layout; e protocolo de depuração sistemática.
- **Tríade Canônica de Engenharia & Design (`docs-for-skill/impeccable-debugging-security-trinity.md`):**
  - Módulo compartilhado para o ecossistema cobrindo Impeccable Design (anti-slop visual), Depuração Sistemática em 4 etapas e Padrões de Segurança Trail of Bits (SAST e OWASP Top 10).

---

## [1.18.0] - 2026-11-08

### Added / Adicionado
- **Nova Skill Oficial: `bootstrap-ux-ui-plus` (v0.1.0-beta):**
  - **Engenharia Cognitiva de Usabilidade & 18 Leis do UX:**
    - Mapeamento direto de todas as 18 Leis Canônicas do UX (Hick, Fitts, Jakob, Proximidade, Semelhança, Região Comum, Conectividade Uniforme, Miller, Doherty <400ms, Von Restorff, Posição Serial, Pico-Fim, Zeigarnik, Prägnanz, Tesler, Postel, Parkinson, Navalha de Occam & Pareto 80/20) em classes e componentes do Bootstrap (v5.3 & v6.0).
  - **10 Heurísticas de Jakob Nielsen:**
    - Diretrizes de visibilidade de status, saídas de emergência (Undo), consistência semântica e prevenção ativa de erros.
  - **Acessibilidade WCAG 2.2 AA, AccessLint e Inclusão para Daltonismo:**
    - Manual técnico completo (`accessibility/visual-accessibility-colorblindness.md`) com suporte a Protanopia, Deuteranopia, Tritanopia e Acromatopsia. Proibição da cor como único comunicador de status, contraste legal conforme a LBI (Lei 13.146/2015 Art. 63), eMAG e ABNT NBR 17225.
  - **Paleta Padrão Calibrada (#90271) & Tipografia Oficial Google Sans:**
    - Paleta padrão de azuis corporativos de alto contraste (`#869dcc`, `#5772ac`, `#3b5998`, `#224389`, `#14306b`) com consulta proativa ao usuário caso deseje customizar. Tipografia oficial com `Google Sans Flex` (títulos), `Google Sans` (texto) e `Google Sans Code` (monospace).
  - **Mandato de Temas: TEMA CLARO PADRÃO (Light Theme Default):**
    - Padrão estrito de Tema Claro (`data-bs-theme="light"`) para arquiteturas Mazer, AdminKit e interfaces geradas; tema escuro / noturno estritamente opt-in sob pedido explícito do usuário com calibração refinada de luminância.
  - **Verificador de Atualizações & Sincronização com Portão de Permissão (`scripts/check_updates.mjs`):**
    - Monitoramento contínuo de versões upstream do Bootstrap (NPM registry) e comparação de versão do repositório remoto GitHub com a instalação local do computador do usuário, exigindo autorização expressa antes de sobrescrever arquivos.
  - **Template Responsivo de Dashboard Administrativo (`templates/admin-dashboard-template.html`):**
    - Painel corporativo completo em HTML5 com Sidebar sanfonada, Topbar com busca e ações táteis (44px+), cards de métricas (Chunking), tabela com status inclusivo para daltônicos (cor + ícone + texto) e alternador de tema claro/noturno e filtros de acessibilidade visual.
  - **Motor CLI de Auditoria (`scripts/audit_ux_bootstrap.mjs`):**
    - Linter automatizado para validar acessibilidade e UX em arquivos HTML, PHP, JSX e templates.
  - **Padrões Canônicos de Dashboards Mazer & AdminKit:**
    - Arquitetura de referência espelhada em [zuramai/mazer](https://github.com/zuramai/mazer) e [adminkit/adminkit](https://github.com/adminkit/adminkit) com Vanilla ES6 e zero dependência de jQuery.
  - **Padrões Multi-Framework:**
    - Arquitetura de componentes para HTML, PHP (Blade/Twig), Node.js, React (Next.js/TSX), Python (Django/Jinja2) e Java.
  - **Documentação Bilíngue Completa:**
    - `SKILL.md`, `README.md`, `VERSION` (0.1.0-beta), `CHANGELOG.md`, `cheatsheet.md`, `patterns.md` e `glossary.md`.

---

## [1.17.0] - 2026-11-08

### Added / Adicionado
- **master-of-foundryvtt (v0.16.0-beta):**
  - **Engenharia Reversa SDD com Reversa (Sandeco):** Integração do framework Reversa ([sandeco.github.io/reversa/pt/](https://sandeco.github.io/reversa/pt/)) para dissecação e especificação formal de sistemas legados de Foundry VTT para migrações v14.
  - **GitLab & Git Repository Diagrammer (`scripts/generate_repo_diagram.mjs`):** Ferramenta CLI híbrida com suporte a GitLab REST API e shallow clone fallback para mapear e gerar diagramas Mermaid.js e relatórios de camadas arquiteturais de repositórios remotos (testado com `peginc/swade`).
  - **GitLab MCP Server Integration:** Documentação de integração com o servidor MCP oficial do GitLab ([docs.gitlab.com/user/model_context_protocol/mcp_server/](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)).
  - **README Bilíngue Completo:** Guia estruturado em Inglês e Português da skill.

---

## [1.16.0] - 2026-11-04

### Added / Adicionado
- **Nova Skill Oficial: `mcp-builder` (v0.1.0-beta):**
  - **Arquiteto & Gerador Universal de Servidores MCP:**
    - Suporte nativo a **PHP 8.4+** (`adapters/Php84Adapter.php`), **Python 3.12+** (`adapters/python_adapter.py`) e **Node.js 22+ ESM** (`adapters/node_adapter.mjs`) operando via JSON-RPC 2.0 stdio com zero dependências externas.
  - **Security Shield (Blindagem Contra Ataques & Anti-Prompt Injection):**
    - Módulo `security/prompt_shield.py` com detecção heurística de jailbreaks, quarentena de credenciais/segredos e análise estática SAST (proteção contra SQLi, XSS, Path Traversal, SSRF e Command Injection).
  - **Resiliência Fail-Safe & Auto Issue Reporter:**
    - Módulo `scripts/issue_reporter.py` para reporte amigável de falhas ao usuário e abertura automática de Issues estruturadas com diagnóstico higienizado no repositório GitHub (`CharlesCorreaDev/skills-ai`).
  - **Self-Updater & Monitor de Atualizações:**
    - Módulo `scripts/check_updates.py` para consulta de novas versões no GitHub Releases.
  - **Configurador de MCPs Externos:**
    - Módulo `scripts/configure_external_mcp.py` para injeção automática de configurações no Antigravity IDE, Claude Desktop e Cursor.
  - **Documentação e Guias Técnicos:**
    - `SKILL.md`, `README.md`, `VERSION` (0.1.0-beta), `CHANGELOG.md`, `cheatsheet.md`, `patterns.md` e `glossary.md`.
- **Nova Skill Oficial: `sms-legal` (v1.0.0):**
  - **Servidor MCP Nativo Unificado (`sms-legal/mcp/`):**
    - Implementação nativa em Node.js (`sms_legal_mcp_server.js`) via JSON-RPC 2.0 stdio (sem dependências externas).
    - Implementação nativa alternativa em Python 3 (`sms_legal_mcp_server.py`) com módulo nativo `urllib`.
    - 9 ferramentas MCP nativas: `sms_enviar_texto`, `sms_enviar_lote`, `sms_agendar`, `sms_consultar_status`, `sms_consultar_creditos`, `sms_consultar_respostas`, `sms_consultar_numero`, `sms_enviar_voz` e `sms_enviar_audio`.
    - Manual completo de integração (`mcp/README.md`) para Antigravity IDE, Claude Desktop, Cursor e outros clientes MCP.
  - **SDKs Multilinguagem Nativos (`sms-legal/integrations/`):**
    - SDK em **PHP** (`SmsLegalClient.php`): compatível com PHP 7.4 a 8.5+, cURL nativo e tipagem estrita.
    - SDK em **Python** (`sms_legal_client.py`): compatível com Python 3.8+, sem bibliotecas externas.
    - SDK em **Node.js** (`sms_legal_client.js`): cliente assíncrono modular com Promises.
  - **Documentação Arquitetural e de Integração:**
    - `cheatsheet.md`: Tabela rápida de endpoints, parâmetros e códigos de erro de `000` a `011`.
    - `patterns.md`: Padrões de arquitetura (BFF, filas de mensageria assíncronas, proteção contra bloqueio por links e particionamento de lotes).
    - `glossary.md`: Glossário técnico com termos e definições do SMS Gateway.
    - `README.md`, `VERSION` (1.0.0) e `CHANGELOG.md` dedicados.

---

## [1.15.0] - 2026-11-03

### Added / Adicionado
- **Motor Universal de Layout e Tradução de PDFs (`book-formatter`):**
  - Adicionado script multiplataforma `universal_pdf_layout_translator.py` para processar e traduzir qualquer PDF em alta fidelidade.
  - Adicionado utilitário multiplataforma `patch_save.py` para salvamento seguro e resiliente de PDFs contra bloqueios de arquivos.
- **Documentação Offline PHP Completa (`php-dev-expert`):**
  - Adicionada documentação oficial completa em arquivo único `php-bigxhtml.html` (~68 MB) para consulta local de alta velocidade offline.

### Fixed / Corrigido
- **Fidelidade Tipográfica e Grid de Colunas (`book-formatter`):**
  - Correção de sobreposição de textos e invasão de colunas no lote de teste de Savage Worlds: Necessary Evil Invasão.
  - Migração de todas as rotinas para o padrão moderno `import pymupdf as fitz`.
  - Remoção de fluxos de texto `BT...ET` diretamente do content stream vetorial para 100% de preservação de texturas e relâmpagos.

---

## [1.14.0] - 2026-11-03

### Added / Adicionado
- **Requisitos Mandatórios Globais e Locais do Ecossistema: GitHub CLI (`gh`) & Tríade de Skills:**
  - **GitHub CLI (`gh`) & Autenticação Obrigatória:** Padronização em todas as skills para exigir e forçar a verificação do `gh` instalado e conectado (`gh auth login`), facilitando clonagem fluida, atualização de forks e submissão formal de issues e novos glossários via CLI.
  - **Tríade Obrigatória de Skills Companheiras (Disponíveis Globalmente e no Projeto do Usuário):**
    - Todas as skills criadas no repositório operam em conjunto com:
      1. **`andrej-karpathy-skills`** (`https://github.com/multica-ai/andrej-karpathy-skills`): Engenharia de software enxuta, código cirúrgico e ausência de suposições cegas.
      2. **`grill-me`** (`https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me`): Entrevista profunda com o usuário/autor para travar requisitos e eliminar ambiguidades antes da execução.
      3. **`skills-code-review`** (`https://www.aihero.dev/skills-code-review`): Revisão automatizada de código e auditoria rigorosa de qualidade antes de qualquer entrega.
    - Disponibilidade obrigatória em escopo global (`~/.gemini/config/skills/`, `~/.claude/skills/`) e no projeto local (`.agents/skills/`, `.claude/skills/`).
- **video-to-md (v0.2.0-beta):**
  - Expansão multiplataforma: YouTube, Vimeo (oEmbed + v2 API) e Twitch (VODs e Clipes via `yt-dlp`).
  - Fallback por Áudio via IA (`--fallback-audio`) com suporte a Whisper e WhisperX (`--whisper-model`).
  - Ajuste de `--delay-ms` para 15.000 ms (15s) padrão para mitigar bloqueios de rate limit do YouTube.
- **book-formatter (v0.14.0-beta):**
  - **Protocolo de Testes e Amostragem em Lotes de 5 Páginas:** Fixado o padrão de **5 páginas** (`--max-pages 5`) para todas as rodadas de teste e validação de diagramação e tradução antes da execução de lotes maiores.
  - **Comparativos Visuais Lado a Lado Obrigatórios:** Geração obrigatória de imagens lado a lado comparando original em inglês vs traduzido em português para checagem de entrelinhas (*leading* de 12.0 pt) e fontes originais (`PopulationZeroBB`, `Palatino Linotype`).
  - **Deduplicação de Camadas e Des-hifenização:** Remoção automática de textos duplicados por *drop-shadow* de PDF e reunião de palavras translineadas em margens de coluna.
  - **Motor Universal de Conversão (`batch_convert_to_md_jsonl.py`):** Suporte genérico para qualquer pasta ou arquivo PDF com saída em `.md`, `.txt` e `.jsonl` para IA.
- **book-formatter (v0.13.0-beta):**
  - **Segmentação de Regras para IA, RAG e MCP:** Script `scripts/export_rules_for_ai.py` que fragmenta livros em datasets JSONL para RAG, datasets para fine-tuning e arquivos por categorias (`combat.md`, `spells.md`, etc.) para uso em ferramentas de MCP servers.
  - **Comunicação de Novos Glossários Formalizada via GitHub Issue:** Notificação ao usuário e proposta de inclusão no repositório oficial obrigatoriamente submetidas via issue.
  - **Manutenção e Atualização Contínua de Dependências:** `scripts/check_env.py --upgrade` para atualização automática de pacotes Python da skill.
  - **Aprendizado Contínuo & Criação Automática de Glossários:** Ao ler qualquer livro de sistema de RPG, o vocabulário mecânico é extraído e gravado na pasta `glossarys/` e na memória.
  - **Monitor de Versão e Atualização Automática:** Script `scripts/check_update.py` para detecção de novas versões publicadas no repositório remoto e atualização automática (`--upgrade`).
  - **Integração de Motores SOTA de IA e Utilitários de PDF:** Inclusão de Docling (IBM/DS4SD), Marker (Datalab), Unstructured, Nougat (Meta AI), Stirling-PDF, Nano-PDF e auditoria RAG inspirada em PDFtoGPT e AI-powered-PDF-agent.
  - **Diretrizes Rigorosas do Tradutor Profissional de Livros de RPG:** 5 mandamentos obrigatórios de fidelidade de tradução, preservação estrita da página original (sem recriar do zero), inviolabilidade numérica (`1d8` e `+2`), checklist de controle de qualidade e formato de entrega.
  - **Protocolo Code Mode, Grill-Me & Andrej Karpathy Skills:** Obrigatório executar tarefas de diagramação em etapas via Code Mode; instalação e uso compulsório das skills `mattpocock/grill-me` (entrevista profunda com o autor antes de executar) e `multica-ai/andrej-karpathy-skills` (engenharia mínima, sem suposições e com validação contínua).

---

## [1.13.0] - 2026-10-29

### Added / Adicionado
- **book-formatter (v0.8.0-beta):** nova skill de formatação e diagramação de livros de RPG.
  - **Instalação de ferramentas de leitura:** PDF com/sem OCR, TXT, DOCX, DOC, CSV/TSV, XLSX/XLS, HTML, EPUB e imagens com OCR, com matriz de formatos e engines de extração.
  - **Artefatos de entrega:** arquivo `.txt` com os textos, `.md` (Markdown) e `.pdf` devidamente diagramado/formatado (fiel ao original: imagens, colunas, fontes, títulos, recuos, parágrafos e número de páginas).
  - **Fluxo de diagramação:** 8 fases (Analisar PDF → Descobrir/Usar Fontes → Extrair Texto → Ensinar Vocabulário RPG → Traduzir em Lotes → Verificar Tradução → Diagramar → Auditar Final) baseado na metodologia de tradução/diagramação com IA paga (ChatGPT + plugin Adobe WORK).
  - **Scripts:** `scripts/check_env.py` (verificação de ambiente multiplataforma) e `scripts/convert_to_txt_md.py` (conversão para TXT/Markdown).
  - **Glossário:** `glossarys/glossary.md` com dicionário inicial de termos de RPG e gamers (futuros dicionários em breve).
  - **Glossário Sci-Fi (v0.2.0-beta):** Adicionado `glossarys/glossary-scifi.md` com termos de ficção científica, ciberpunk, space opera, militar, science fantasy e psionics, ampliando o dicionário de RPG e gamers da skill.
  - **Glossário de Terror (v0.3.0-beta):** Adicionado `glossarys/glossary-horror.md` com termos de terror cósmico, Lovecraft, survival horror, gothic horror e psionics, ampliando a coleção de dicionários da skill.
  - **Glossário Savage Worlds (v0.4.0-beta):** Adicionado `glossarys/glossary-savage-worlds.md` com termos do **Savage Worlds Adventure Edition (SWADE)** (conceitos, traits, perícias, combate, edges e cenários).
  - **Glossário Year Zero (v0.5.0-beta):** Adicionado `glossarys/glossary-year-zero.md` com termos do **Year Zero Engine (YZE)** (Forbidden Lands, Vaesen, Alien, Blade Runner, Twilight 2000, Mutant, The Walking Dead, Tales from the Loop, Electric State, etc.).
  - **Glossário do Mundo das Trevas (v0.6.0-beta):** Adicionado `glossarys/glossary-world-of-darkness.md` com glossário exclusivo do **Mundo das Trevas (World of Darkness)**, cobrindo **todas as suas franquias**.
  - **Nova Capacidade (v0.7.0-beta):** Criação de **Formulários e Fichas de RPG em PDF preenchíveis** (toolchain `fpdf2`/`reportlab`/`pdfcpu` e inspeção `pypdf`/`pdfplumber`).
  - **Glossário Pathfinder 2e (v0.8.0-beta):** Adicionado `glossarys/glossary-pathfinder-2e.md` com glossário de **Pathfinder 2ª Edição (PF2e)** (Classes, Feats/Dotações, Salvamentos, Ações, Condições, Mecânicas).

---

## [1.12.0] - 2026-10-28

### Added / Adicionado
- **youtube-to-md (v0.1.0-beta):** nova skill que converte vídeos soltos e playlists do YouTube em Markdown (metadados, descrição, capítulos e transcrição com timestamps clicáveis), com `_INDEX.md`, `manifest.json` e `_ALL.md` opcional. Ver [`youtube-to-md/SKILL.md`](youtube-to-md/SKILL.md).
- **master-of-foundryvtt (v0.16.0-beta):**

  - **Perfilador de Hardware (CPU, RAM e GPU/VRAM) & Governador Adaptativo Anti-Travamento (`scripts/hardware_governor.py`, `scripts/hardware_governor.mjs`, `scripts/check_env.py`, `scripts/convert_media.js`, `mcp/foundry_mcp_server.js`, `mcp/foundry_mcp_server.py` e Mandato 24 no `SKILL.md`):**
    - Verifica automaticamente o processador (`modelo da CPU` e `núcleos lógicos`), memória RAM (`Total`, `Livre`, `% em uso`) e GPU/VRAM (`VRAM Total`, `VRAM Livre` e se a GPU é integrada compartilhando RAM do sistema ou dedicada via `nvidia-smi`, Registro do Windows `HardwareInformation.qwMemorySize` e `lspci`).
    - Calcula o orçamento seguro (`max_workers`, `ffmpeg_threads`, `sharp_concurrency`, `batch_size`, `batch_delay_ms`) e aplica prioridade baixa no SO (`BELOW_NORMAL_PRIORITY_CLASS` / `nice(10)`) + guardião de RAM em tempo real para jamais travar a máquina operante.
    - Calcula o orçamento de VRAM do Canvas WebGL/PixiJS do Foundry VTT (`foundry_vram_canvas_budget`: resolução máxima de mapa `4096x4096` / `8192x8192` / `16384x16384`, limite de tiles WebM animados e qualidade WebP).
- **website-for-markdown (v0.3.0-beta):**
  - **Motor Nativo de Crawling Recursivo Local (`scripts/scrape_to_md.py`):** Varredura recursiva em largura (BFS) sem depender de API externa, trava automática de escopo por prefixo de URL (`get_scope_prefix`), modo HTTP multi-thread rápido (`--fast` / `--workers`) com fallback Playwright, limpeza cirúrgica de DOM (`#layout-content`, `article`, `main`), reescrita de links internos (`.php`/`.html` para `.md`), filtros regex (`--include`/`--exclude`), *resume cache* e geração de `_INDEX.md` + `crawl_manifest.json`.
  - **Perfilador Automático de Hardware & Controle Eco de CPU/RAM (`detect_hardware_budget`):** Detecta modelo do processador, núcleos lógicos, RAM total e RAM livre da máquina operante antes de iniciar, define prioridade baixa no SO (`BELOW_NORMAL_PRIORITY_CLASS` / `nice(10)`), limita threads de forma conservadora (~15-20% da CPU), faz streaming em micro-lotes a partir do disco e pausa com `gc.collect()` caso a RAM ultrapasse 78%.
- **website-for-skill (v0.3.0-beta):**
  - **Orquestração de Portais Multipágina e Preservação de Links (`Scripts/build_skill.py`):** Repasse completo de parâmetros de crawling (`--crawl`, `--fast`, `--max-pages`, `--max-depth`, `--include`, `--exclude`, `--from-dir`, `--delay-ms`, `--max-ram-percent`), preservação dos nomes semânticos em `chapters/` para manter links internos funcionais, geração de `chapters/_INDEX.md` em streaming de baixo uso de memória (evitando colisão com `index.md` no Windows) e agrupamento inteligente por categoria no `SKILL.md`.
- **php-dev-expert (v0.6.0-beta):**
  - **Documentação de POO em PHP em [`php-dev-expert/OOP/`](php-dev-expert/OOP/README.md)** (4 módulos + índice, cobrindo as aulas `#01` a `#15` da playlist, com extensão para PHP 8.x).
  - **Acervo Completo de 31 Plataformas de CMS, LMS, E-Commerce, Helpdesk, Faturamento, Redes Sociais, Analytics e Ferramentas em PHP em [`php-dev-expert/cms/`](php-dev-expert/cms/README.md) (`2.501 páginas`):** [`wordpress`](php-dev-expert/cms/wordpress/_INDEX.md) (452 págs), [`joomla`](php-dev-expert/cms/joomla/_INDEX.md) (322 págs), [`craftcms`](php-dev-expert/cms/craftcms/_INDEX.md) (249 págs), [`octobercms`](php-dev-expert/cms/octobercms/_INDEX.md) (155 págs), [`blesta`](php-dev-expert/cms/blesta/_INDEX.md) (100 págs), [`matomo`](php-dev-expert/cms/matomo/_INDEX.md) (96 págs), [`opencart`](php-dev-expert/cms/opencart/_INDEX.md) (90 págs), [`ossn`](php-dev-expert/cms/ossn/_INDEX.md) (66 págs), [`invoiceninja`](php-dev-expert/cms/invoiceninja/_INDEX.md) (62 págs), [`invoiceplane`](php-dev-expert/cms/invoiceplane/_INDEX.md) (61 págs), [`livehelperchat`](php-dev-expert/cms/livehelperchat/_INDEX.md) (61 págs), [`zenbership`](php-dev-expert/cms/zenbership/_INDEX.md) (61 págs), [`elgg`](php-dev-expert/cms/elgg/_INDEX.md) (60 págs), [`formalms`](php-dev-expert/cms/formalms/_INDEX.md) (60 págs), [`moodle`](php-dev-expert/cms/moodle/_INDEX.md) (60 págs), [`humhub`](php-dev-expert/cms/humhub/_INDEX.md) (54 págs), [`mywebsql`](php-dev-expert/cms/mywebsql/_INDEX.md) (51 págs), [`htmlpurifier`](php-dev-expert/cms/htmlpurifier/_INDEX.md) (50 págs), [`openwebanalytics`](php-dev-expert/cms/openwebanalytics/_INDEX.md) (50 págs), [`oscommerce`](php-dev-expert/cms/oscommerce/_INDEX.md) (50 págs), [`freescout`](php-dev-expert/cms/freescout/_INDEX.md) (49 págs), [`phpmyadmin`](php-dev-expert/cms/phpmyadmin/_INDEX.md) (48 págs), [`eventschedule`](php-dev-expert/cms/eventschedule/_INDEX.md) (41 págs), [`maianmedia`](php-dev-expert/cms/maianmedia/_INDEX.md) (40 págs), [`roundcube`](php-dev-expert/cms/roundcube/_INDEX.md) (39 págs), [`subrion`](php-dev-expert/cms/subrion/_INDEX.md) (24 págs), [`jcow`](php-dev-expert/cms/jcow/_INDEX.md) (15 págs), [`afterlogic`](php-dev-expert/cms/afterlogic/_INDEX.md) (13 págs), [`mibew`](php-dev-expert/cms/mibew/_INDEX.md) (10 págs), [`kohana`](php-dev-expert/cms/kohana/_INDEX.md) (8 págs) e [`x2crm`](php-dev-expert/cms/x2crm/_INDEX.md) (4 págs).
  - **Documentação Conceitual, Histórica e Comparativa de Frameworks PHP em [`php-dev-expert/frameworks/doc/`](php-dev-expert/frameworks/doc/README.md)** + **10 Frameworks PHP Documentados Localmente em Markdown** ([`laravel`](php-dev-expert/frameworks/laravel/_INDEX.md), [`symfony`](php-dev-expert/frameworks/symfony/_INDEX.md), [`yii`](php-dev-expert/frameworks/yii/_INDEX.md), [`spiral`](php-dev-expert/frameworks/spiral/SKILL.md), [`codeigniter`](php-dev-expert/frameworks/codeigniter/_INDEX.md), [`fuelphp`](php-dev-expert/frameworks/fuelphp/_INDEX.md), [`slim`](php-dev-expert/frameworks/slim/_INDEX.md), [`flightphp`](php-dev-expert/frameworks/flightphp/_INDEX.md), [`fatfree`](php-dev-expert/frameworks/fatfree/_INDEX.md) e [`web-framework`](php-dev-expert/frameworks/web-framework/_INDEX.md)).
  - **Documentação Oficial Completa de 6 Servidores Web em [`php-dev-expert/servers/`](php-dev-expert/servers/):** [`caddy-web-server`](php-dev-expert/servers/caddy-web-server/_INDEX.md), [`apache-server/2.4`](php-dev-expert/servers/apache-server/2.4/_INDEX.md), [`apache-server/2.2`](php-dev-expert/servers/apache-server/2.2/_INDEX.md), [`lightspeed-server`](php-dev-expert/servers/lightspeed-server/_INDEX.md), [`nginx-server`](php-dev-expert/servers/nginx-server/_INDEX.md) e [`iis-server`](php-dev-expert/servers/iis-server/_INDEX.md).
  - **Documentação Oficial do Bootstrap por Versão em [`php-dev-expert/bootstrap/`](php-dev-expert/bootstrap/README.md):** [`3.4`](php-dev-expert/bootstrap/3.4/_INDEX.md) (27 págs), [`4.6`](php-dev-expert/bootstrap/4.6/_INDEX.md) (106 págs), [`5.3`](php-dev-expert/bootstrap/5.3/_INDEX.md) (162 págs) e [`6.0`](php-dev-expert/bootstrap/6.0/_INDEX.md) (182 págs).
  - **Documentação Modular Completa de Arquitetura PHP MVC em [`php-dev-expert/MVC/`](php-dev-expert/MVC/README.md):**
    - 6 guias interligados cobrindo Front Controller (`public/index.php`), Nginx/Apache rewrite, Composer PSR-4, Container DI com Auto-Wiring, Router + Middlewares, Controllers enxutos, objetos `Request`/`Response`, DTOs, Single-Action Controllers (`__invoke` / ADR), camada Model dividida em Entidades/Enums + Services + Repositories com PDO seguro (anti-SQLi e transações), camada View com Layouts + anti-XSS + `CsrfMiddleware` + APIs JSON, evolução sintática do PHP 7.4 ao PHP 8.5 (`readonly class`, Property Hooks, Asymmetric Visibility, Pipe Operator `|>`), comparativo Laravel/Symfony/FlightPHP/Slim, Anti-Patterns e testes unitários com PHPUnit.
  - **Segurança Crítica & Mitigação PHP2Shell (`CVE-2026-109618` e `CVE-2026-109619`) em [`php-dev-expert/security-cves.md`](php-dev-expert/security-cves.md):**
    - Análise de causa raiz no Zend Engine: corrupção de memória por `longjmp()` (`zend_bailout`) em erros Out-Of-Memory com estruturas parcialmente inicializadas (`CVE-2026-109618`) e *Use-After-Free* (UAF) por estado global obsoleto (`session.upload_progress`) em workers persistentes (`CVE-2026-109619`).
    - Contexto de descoberta (agosto de 2026) pelas equipes da Calif e Wiz em parceria com a OpenAI (*Patch the Planet*), utilizando auditoria assistida por IA.
    - Diretrizes de prevenção para **PHP 8.2+** (`>= 8.2.35`, `>= 8.3.36`, `>= 8.4.27`, `>= 8.5.12` e contenção sem atualização imediata), blindagem em camadas para **PHP 8.1 ou menor** sem possibilidade de atualização de versão (backports LTS, `session.upload_progress.enabled = 0` no `php.ini` global, `php_admin_flag` no PHP-FPM, controle de limites multipart/memória e bloqueio no Nginx/WAF) e **protocolos específicos para servidores Docker com PHP** (`docker-compose.yml` sem rebuild, `Dockerfile`, cgroups e hotfix zero-downtime via `USR2`/`USR1`).
  - **Base Completa do Manual Oficial do PHP (`pt_BR`) em [`php-dev-expert/php-docs/`](php-dev-expert/php-docs/_INDEX.md):** 11.838 páginas oficiais convertidas para Markdown com links internos preservados (`.md`), `_INDEX.md` categorizado e `crawl_manifest.json`.

---

## [1.11.0] - 2026-10-27

### Added / Adicionado
- **master-of-foundryvtt (v0.15.0-beta):**
  - **Diagnóstico & Resiliência na Foundry Package Release API (`guides/publishing-packages.md`):**
    - Protocolo de captura explícita de status HTTP e resposta do servidor para a API oficial do Foundry VTT (`https://foundryvtt.com/_api/packages/release_version/`).
    - Proibição do uso de `curl -s` isolado para eliminar falsos positivos (exit code 0 em HTTP 400, 401 e 429).
    - Exemplos com `curl -w "\nHTTP_STATUS:%{http_code}" -s -S` e verificação estrita de HTTP 200.
    - Notificação com `::warning::` em vez de skip silencioso caso `FOUNDRY_RELEASE_TOKEN_*` ou `FOUNDRY_API_TOKEN` estejam ausentes nos Secrets.
  - **Atualização do Workflow Template (`templates/github/workflows/release.yml`):**
    - Suporte padronizado para secrets de release com tratamento de erro e status HTTP transparente.

---

## [1.10.0] - 2026-10-27

### Added / Adicionado
- **master-of-foundryvtt (v0.14.0-beta):**
  - **Mandato 22 (Protocolo Interativo de Release, Versionamento & Publicação):** Sempre que o desenvolvimento de um módulo ou sistema do Foundry VTT for concluído e aprovado pelo desenvolvedor, o agente obrigatoriamente questiona de forma interativa sobre o incremento de versão semântica (Patch, Minor ou Major), geração de commit e tag Git, publicação da GitHub Release com assets compactados (`module.zip`/`system.zip`) e disparo de atualização oficial no diretório do Foundry VTT via API de Release.
  - **Mandato 23 (Protocolo de Wiki Técnica & Documentação Minuciosa):** Mandato inegociável de criar ou atualizar `WIKI.md` (ou diretório `wiki/`) com manuais minuciosos de uso para Mestres e Jogadores, referência completa de APIs/métodos expostos com JSDoc e exemplos de macro, catálogo de hooks, arquitetura de DataModels (`TypeDataModel`) e troubleshooting.
  - **Novo Guia Técnico:** Adicionado [`master-of-foundryvtt/guides/wiki-and-release-lifecycle.md`](master-of-foundryvtt/guides/wiki-and-release-lifecycle.md).

---

## [1.9.0] - 2026-10-25

### Added / Adicionado
- **master-of-foundryvtt (v0.12.0-beta):**
  - **Servidor MCP Nativo Oficial Unificado (`master-of-foundryvtt-mcp`):** Controle completo e auto-suficiente de Foundry VTT em Node.js (atores, itens, cenas, tabelas, macros, compêndios, baralhos de cartas, playlists e journals/handouts). Módulos de terceiros (`ninjos`, `laurigates`, `adambdooley`) foram descontinuados/removidos.
  - **Engenharia Reversa Estática & Remota (Git):** Ferramenta `reverse_engineer_target` com clonagem e análise de código de módulos e sistemas desinstalados do GitHub (ex: JB2A, Sequencer, Item Piles) e inspeção do Core.
  - **Inspeção de Topologia (SO, Nuvem e Docker):** Detecção de Windows/macOS/Linux, instâncias locais, The Forge, Molten, containers Docker e recomendação oficial de VPS Hostinger especializada com 20% de desconto.
  - **Mandatos de Qualidade:**
    - Mandato 18: Verificação, teste de sintaxe (`node -c`) e revisão obrigatória antes de qualquer entrega.
    - Mandato 19: UI com Bootstrap prefixado (`.yze-btn-primary`, `.yze-card`), paleta padrão de 9 tons e bibliotecas de ícones aprovadas (Game-Icons.net, RPG Awesome, Font Awesome, Bootstrap Icons, Get Social).
    - Mandato 20: Modelagem estatística e probabilidade de dados com AnyDice antes da conversão para a classe `Roll`.
    - Comentários de código estritamente bilíngues (Inglês e Português).
- **Atualização de Versão das Skills (v0.2.0-beta & v1.1.0):**
  - Atualizadas para `v0.2.0-beta`: `docker-master`, `docs-for-markdown`, `docs-for-skill`, `image-to-prompt`, `php-dev-expert`, `python-dev-expert`, `website-for-markdown`, `website-for-skill`.
  - Atualizada para `v1.1.0`: `humanizer-plus`.
  - Adicionado a todas as skills o Protocolo de Feedback Proativo com abertura autônoma de Issues no GitHub (`gh issue create`), protocolo de verificação e revisão mandatória, e comentários de código bilíngues.

---

## [1.8.0] - 2026-10-25

### Added / Adicionado
- **Nova Skill: `humanizer-plus` (v1.0.0):**
  - Skill universal de humanização e desmarcação de IA para qualquer arquivo ou código (purga de ZWSP, normalização tipográfica, remoção de comentários óbvios, purga de metadados em mídias com ExifTool, e reescrita natural sem vícios de LLM).
  - Vigilância contínua com atualização de regras a partir do upstream `blader/humanizer`.
- **master-of-foundryvtt (v0.11.0-beta):**
  - **Mandato Obrigatório 14 (Humanização, Código Limpo & Anti-Detecção):**
    - Protocolo de saneamento de marcas determinísticas (remoção de zero-width codepoints `U+200B`, `U+FEFF`, normalização de aspas tipográficas e limpeza de metadados geradores).
    - Diretrizes de código JavaScript idiomático e conciso para macros e módulos (early returns, sem comentários didáticos óbvios, sem cabeçalhos de IA).
    - Eliminação de vícios narrativos de IA (slop de RPG) em diários e compêndios de itens/atores com injeção de voz natural de narrador.
  - **Otimização e Conversão de Mídias (Mandato 15 & Guia Técnico):**
    - Conversão automática para `.webp` (95% de qualidade, preservando SVG) e `.webm` (VP9/Opus, 95% de qualidade para animações e áudio).
    - Guia técnico completo em `guides/media-optimization-and-conversion.md` e script `scripts/convert_media.js`.
  - **Guia Completo de Publicação de Pacotes no Foundry VTT:**
    - Documentação completa em `guides/publishing-packages.md` cobrindo empacotamento, GitHub Actions / CI-CD, submissão ao diretório oficial e boas práticas de distribuição.
  - **Bases de Conhecimento Especializadas Ingeridas:**
    - **Savage Worlds (SWADE):** Artigos do Mestre Charles Corrêa (`rpg.charlescorrea.com.br`), prompts de IA (`RPGPlus`), cenários da Odyssey Publicações e catálogo oficial Pinnacle Entertainment Group (PEGinc).
    - **D&D 5e:** D&D 5e SRD API (`docs.dnd5eapi.co`), ecossistema 5eTools e suíte Plutonium / TheGiddyLimit.
    - **Pathfinder 2e:** Archives of Nethys (`2e.aonprd.com`), PF2 SRD PT-BR e d20PFSRD.
    - **Year Zero Engine & Free League:** YZE SRD oficial, análise editorial Odyssey Pub, VTT hub e catálogo completo de jogos (Alien, Blade Runner, Vaesen, Twilight: 2000, Forbidden Lands, Coriolis, Mutant, The Walking Dead, Tales from the Loop, Electric State, The One Ring, Symbaroum, Pirate Borg, Outgunned, Dragonbane, Mörk Borg, Cy_Borg).
    - **Daggerheart:** SRD oficial, licença DPCGL 2.0 e Homebrew Kit oficial da Darrington Press.
  - **Scripts Utilitários Adicionados:**
    - `scripts/sanitize_content.py` e `scripts/sanitize_content.js` para saneamento e humanização em lote.
    - `scripts/convert_media.js` para otimização de mídias com 95% de qualidade.

---

## [1.7.0] - 2026-10-24

### Added / Adicionado
- **master-of-foundryvtt (v0.10.0-beta):**
  - **Protocolo Obrigatório 13: Code Mode & Sandbox Orchestration (CodeAct):**
    - Adotado o paradigma estrito de Code-as-Action para Foundry VTT, economizando tokens contextuais através de filtragem e processamento em memória via scripts em sandbox (Node.js/Python).
    - Validação sintática e de lógica antes da entrega de qualquer macro, função ou patch.
    - Operações programáticas em lote via MCP (`master-of-foundryvtt-mcp`, `ninjos-foundry-mcp`).
    - Consulta contínua à documentação oficial (`kb/`, `versions/`) e inspeção em tempo real com ferramentas de engenharia reversa do REA (`rea-agents`).
  - **Guia Operacional Bilíngue:**
    - Adicionado [guides/code-mode-sandbox-orchestration.md](master-of-foundryvtt/guides/code-mode-sandbox-orchestration.md).
  - **Verificação Semanal de Atualizações & Auto-Update:**
    - Script [`scripts/check_skill_updates.py`](master-of-foundryvtt/scripts/check_skill_updates.py) e Mandato 12 atualizado para checar novas versões semanalmente, notificar o desenvolvedor e executar a atualização automaticamente.

---

## [1.6.0] - 2026-10-23

### Added / Adicionado
- **Governança de Versão por Skill (`VERSION` & SemVer):**
  - Implementado arquivo `VERSION` obrigatório em todas as skills do repositório (`master-of-foundryvtt`, `docker-master`, `php-dev-expert`, `python-dev-expert`, `image-to-prompt`, `docs-for-markdown`, `docs-for-skill`, `website-for-markdown`, `website-for-skill`).
  - Estabelecido que todas as skills iniciam seu ciclo com versionamento explícito e sufixo de maturidade **Beta** (ex: `0.9.0-beta` para `master-of-foundryvtt` e `0.1.0-beta` para as demais).
  - Diretiva mandatória nos `SKILL.md` para que agentes e usuários leiam o arquivo `VERSION` para identificar a versão ativa e avisar o operador sobre novidades e atualizações.
- **Changelogs Dedicados por Skill (`<skill>/CHANGELOG.md`):**
  - Cada skill do repositório passa a ter seu próprio arquivo `CHANGELOG.md` detalhado, permitindo rastreamento granular do ciclo de vida sem inflar o histórico de outras skills.
  - Histórico do `master-of-foundryvtt` detalhado desde a sua criação, cobrindo motores de RPG do Tio Nitro, engenharia reversa do v14, REA, servidor MCP nativo e banco de 100+ sistemas.
- **Padronização de Git Tags por Skill:**
  - Definida convenção de tags no formato `<nome-da-skill>-v<versao>` (ex: `master-of-foundryvtt-v0.9.0-beta`), além das tags globais de repositório (`v1.6.0`).
- **Detecção de Instalação Existente e Alerta de Sobrescrita Consciente (Mandato 11):**
  - Protocolo para verificar se a skill já está presente no projeto local ou globalmente (`~/.gemini/config/skills/`, `~/.claude/skills/`, `~/.agents/skills/`), emitindo alerta transparente antes de atualizar/reinstalar e preservando memórias locais (`memory/`).
- **Motores de Regras do Tio Nitro (`systems/07-generic-and-rules-light.md`):**
  - Ingestão completa das mecânicas, regras e arquitetura de dados dos sistemas de Nitro: **3d6World**, **2d6World**, **Pocket 2d6World**, **2d10Solo** e **2d6Solo**.
- **Compêndio de 60 Engines de RPG para Engenharia Reversa (`kb/09-rpg-engines-and-mechanics.md`):**
  - Guia aprofundado com matriz técnica cobrindo 60 motores de RPG (resolução de dados, esquemas de dados, hooks e padrões de implementação no Foundry VTT).
- **Engenharia Reversa Completa do Core v14.369 (`kb/08-core-reverse-engineering-v14.md`):**
  - Mapeamento detalhado dos pacotes internos do Foundry v14 (`@foundryvtt/foundryvtt`, `@foundryvtt/commons`, ESM, DataModels, ApplicationV2).
- **Suporte a Engenharia Reversa com REA (`guides/reverse-engineering.md`):**
  - Integração com `rea-agents` (REA MCP/CLI), setup de ambiente automatizado (`scripts/setup_dev_env.py`) e diretório de memórias locais persistentes (`memory/learnings.md`).
- **Hierarquia e Protocolo de Ícones Padrão (Mandato 9):**
  - Prioridade mandatória para ícones core do Foundry (`icons/...`), ícones dedicados de sistemas e fallback seguro para SVGs padrão (`icons/svg/...`).
- **Integração no README Geral:**
  - Tabela bilíngue de skills no `README.md` atualizada com colunas dedicadas para Versão, Status (Beta) e links diretos para a documentação e para o `CHANGELOG.md` de cada skill.

### Changed / Alterado
- **Remoção de Travas de Engenharia Reversa:** Atualização das diretrizes para encorajar análise e inspeção de código e APIs do core e de sistemas para maior precisão no desenvolvimento.
- **Configuração do Workspace:** Inclusão de novos atalhos e padronização de configurações no ambiente.

---

## [1.5.0] - 2026-10-18

### Added / Adicionado
- **Servidor MCP Nativo (`master-of-foundryvtt-mcp`):**
  - Implementado servidor MCP autônomo e sem dependências externas em Node.js (`mcp/foundry_mcp_server.js`) e Python (`mcp/foundry_mcp_server.py`).
  - Suporte completo a geração e manipulação de: Atores, Itens, Cenas (paredes, iluminação, portas), Combates, Playlists de som, Baralhos de cartas e Compêndios.
  - Conexão e sincronização direta com instâncias ativas do Foundry VTT e mundos locais.
  - Manual passo a passo de instalação para Antigravity IDE, Claude Desktop, Claude Code e Cursor (`mcp/INSTALLATION.md`).
- **Guia de Armadilhas Automáticas & Gatilhos (`guides/automated-traps-and-triggers.md`):**
  - Documentação de integração bilíngue para o motor de efeitos visuais **Sequencer** e o motor de gatilhos em tiles **Monk's Active Tile Triggers (MATT)**.
  - Mapeamento de dependências e pacotes recomendados (`JB2A`, `Item Piles`, `Automated Animations`, `Token Magic FX`).
- **Mandato 8 para Agentes de IA:**
  - Protocolo obrigatório de esclarecimento interativo, ingestão de livros/manuais e escopo transparente antes da criação de qualquer recurso de jogo.
- **Expansão do Catálogo para +100 Sistemas de RPG:**
  - Adição de novos sistemas: Cosmere RPG, Mörk Borg, Cy_Borg, Star Wars FFG, Star Trek Adventures, Traveller, Starfinder, Achtung! Cthulhu 2d20, Crônicas RPG, Sword World 2.5, Shinobigami, Wilderfeast, Mythic GME e HERO System.
- **Suporte Oficial à Loja do Foundry VTT:**
  - Diretriz e ferramentas para pesquisa de conteúdo comercial e módulos licenciados (`https://www.foundryvtt.store/search?q=...`).

### Changed / Alterado
- **Assinatura e Atribuição:** Atualizada a assinatura nos metadados de geração para *"Master of Foundry VTT MCP by Mestre Charles Corrêa - rpg.charlescorrea.com.br"*.
- **Compatibilidade v14:** Ajustada tipagem de resultados de tabelas roláveis (`RollTable`) para formato string `text` em conformidade com o DataModel do Foundry v12–v14.
- **Configuração Git:** Criação do `.gitignore` para preservar a pasta local `.agents/`.

---

## [1.4.0] - 2026-09-10

### Added / Adicionado
- **Skill `php-dev-expert`:** Especialista Sênior em PHP (7.4 a 8.5), focada em arquitetura moderna, design patterns (MVC, ADR), segurança e integração com frameworks (Laravel/Symfony). Implementada regra crítica para detecção proativa da versão do PHP.
- **Skill `python-dev-expert`:** Especialista em Python (3.x a 3.16), focada em tipagem avançada, Web (Django 6.1/FastAPI), Scripting e Data Science. Conta com automação inteligente para validar a versão do Python instalada no host.
- **Skill `docker-master`:** Especialista DevOps em orquestração Docker, multi-stage builds e ambientes rootless. Destaque para adaptação dinâmica do Docker Compose (V2) e detecção invisível do Sistema Operacional (Windows/Mac/Linux) para bind mounts perfeitos. Adicionado mapeamento do ecossistema Cloud (Hub, Scout, Build).

---

## [1.3.1] - 2026-09-09

### Added / Adicionado
- **Guia de Ferramentas CLI (`guides/cli-tools.md`):** Documentação completa do `@foundryvtt/foundryvtt-cli` (`fvtt`) e `fvtt-world-cli` para desempacotar (`unpack`) e empacotar (`pack`) compêndios binários em fontes YAML/JSON para controle de versão no Git e CI/CD.
- **Diagnóstico no `check_env.py`:** Verificação automática de instalação de ferramentas de linha de comando (`fvtt` e `fvtt-world-cli`).
- **Nomenclatura Localizada de Sistemas:** Inclusão do título oficial em português para **Perigos & Princesas (*Perils & Princesses*)**.

### Fixed / Corrigido
- **Diagrama Mermaid em `cli-tools.md`:** Corrigida sintaxe de arestas com aspas explícitas para compatibilidade total com o parser Mermaid 11.15+.
- **Classificação de Daggerheart:** Reclassificado com precisão para a categoria de **Fantasia Heroica & Duality Dice System (2d12 Hope & Fear)**, esclarecendo que não utiliza o motor Powered by the Apocalypse (PbtA).
- **Simetria Bilíngue:** Sincronização 100% espelhada entre as seções em inglês e português do `SKILL.md` e `systems/README.md`.

---

## [1.3.0] - 2026-09-09

### Added / Adicionado
- **Integração com Servidores MCP (`mcp/README.md`):**
  - Suporte e templates de configuração para `ninjos-foundry-mcp`, `foundryvtt-mcp` e `adambdooley/foundry-vtt-mcp`.
  - Protocolo de intervenção do desenvolvedor e solicitação de credenciais (`User Data Path`, URL/porta, admin key, mundo ativo).
- **Base de Conhecimento de +60 Sistemas de RPG (`systems/`):**
  - Guias detalhados por categoria: D20/Fantasia Heroica, Storyteller/Mundo das Trevas, Investigação/Horror Cósmico, Year Zero Engine, Sci-Fi/Cyberpunk, Narrativos/PbtA/FitD e Genéricos/Regras Customizadas.
  - Links oficiais de repositórios, ganchos (`Hooks`), armadilhas de migração e modelos de dados.
- **Diretriz de Descoberta Dinâmica de Sistemas:**
  - Protocolo obrigatório para agentes de IA buscarem sistemas não catalogados no diretório oficial [https://foundryvtt.com/packages/systems](https://foundryvtt.com/packages/systems).
- **Guias da API do Foundry VTT v8 até v14 (`versions/`):**
  - Documentação limpa e estruturada sem artefatos de concatenação da navegação JSDoc.
- **Base de Conhecimento Operacional do Foundry (`kb/`):**
  - Capítulos 01 a 06 cobrindo Hospedagem, Iluminação/Visão, Atores/Tokens, Rolagens, WebRTC e Compêndios.
- **Rotina de Atualização Mensal (`scripts/update_foundry_docs.py`):**
  - Script automatizado e instruções para agendamento periódico via `/schedule`.

---

## [1.2.0] - 2026-09-09

### Added / Adicionado
- **Skill `image-to-prompt`:**
  - Skill de engenharia reversa visual de imagens para prompts detalhados bilíngues (EN / PT-BR) otimizados para geradores de imagem como Sora, Midjourney, Nano Banana, DALL-E 3 e Stable Diffusion.
- **Estrutura Inicial de `master-of-foundryvtt`:**
  - Criação da pasta da skill com os cinco mandatos iniciais para agentes de IA por GM Charles Corrêa.

---

## [1.1.0] - 2026-09-09

### Added / Adicionado
- **Protocolo de Auto-Correção e Recuperação Autônoma:**
  - Diretriz global nos `README.md` e `SKILL.md` exigindo que o agente diagnostique falhas, execute correções iterativas e solicite permissão formal para instalação de pacotes extras.
- **Skills de Documentação & Web:**
  - `docs-for-markdown`: Pipeline para converter qualquer documento em Markdown estruturado.
  - `docs-for-skill`: Pipeline para transformar manuais de regras e APIs em skills prontas para agentes.
  - `website-for-markdown`: Extração limpa de conteúdo web para markdown sem ruídos.
  - `website-for-skill`: Raspagem e conversão de portais completos em skills modulares.

---

## [1.0.0] - 2026-09-09

### Added / Adicionado
- Lançamento inicial do repositório **Skills AI** por Charles Corrêa.
- Arquitetura de micro-unidades de conhecimento com `SKILL.md`, `cheatsheet.md`, `glossary.md` e `patterns.md`.
- Suporte a multi-agentes: Antigravity IDE, Claude Code, GitHub Copilot CLI, Hermes Agent, Gemini, Orca, Kilo, NVIDIA e Ollama.
