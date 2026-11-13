# Second Brain Plus 🧠⚡💾

> **Comprehensive Persistent Memory, Context Optimization & AI Second Brain Suite**  
> *Suíte Completa de Memória Persistente, Otimização de Contexto e Segundo Cérebro para Agentes de IA por GM Charles Corrêa*  
> **Status:** Beta (`v0.1.0-beta`) | **Layout Padrão:** [Second Brain All-in-One Productivity System 2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026) (P.A.R.A. 2.0)

---

## 🇺🇸 English

### 📌 What is Second Brain Plus? (The Problem vs. The Solution)

Modern Large Language Models (LLMs) and autonomous coding agents (Antigravity, Claude Code, Cursor, Codex, Copilot CLI) are formidable at generating code, but suffer from three structural handicaps:

1. **Context Window Amnesia:** When conversation turns expire, sessions restart, or context boundaries compress, the agent forgets previous architectural decisions, port numbers, bug workarounds, and project status.
2. **Hallucination of Stale APIs:** Agents guess parameters based on stale pre-training data instead of consulting live, versioned documentation.
3. **Cognitive Overload & Context Bloat:** Dumping massive monolithic files into prompts drains context tokens, increases cost, and degrades reasoning precision.

**Second Brain Plus** solves these systemic problems. It acts as an **autonomous operating system for AI memory and knowledge**, creating a synchronized tri-layer bridge between:
- **Cloud Workspace (Notion API & Notion CLI):** Collaborative, visual, relational databases with Kanban boards and mobile accessibility.
- **Remote Git Repositories (GitHub `gh` & GitLab `glab`):** Cryptographic, immutable, version-controlled backup with private or public visibility controls.
- **Local Git Repository (`.second-brain/`):** Zero-latency, Git-versioned, offline-ready Markdown files following Tiago Forte's **P.A.R.A. 2.0** methodology (Projects, Areas, Resources, Archives).

---

### 🏛️ The 5-Layer AI Memory Architecture

Second Brain Plus organizes memory into 5 distinct, hierarchical tiers so agents retrieve exactly what they need without saturating the prompt context:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       5-LAYER AI MEMORY ARCHITECTURE                        │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ Layer                        │ Purpose                      │ Persistence   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 1. Working Memory (Short)    │ Active prompt turn state,    │ Session RAM   │
│                              │ compressed via Caveman       │ (Headroom)    │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 2. Episodic Memory (Events)  │ Session logs, timeline, and  │ claude-mem /  │
│                              │ observation histories        │ Notion Logs   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 3. Semantic Memory (Facts)   │ ADRs, permanent project rules│ Notion ADRs / │
│                              │ and learned technical truths │ PARA Markdown │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 4. Procedural Memory (Skills)│ Step-by-step playbooks, run- │ SKILL.md /    │
│                              │ books and reusable workflows │ CI/CD scripts │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 5. Knowledge Graph (Edges)   │ Relational dependencies,     │ graphify /    │
│                              │ AST links, cross-references  │ Notion Rel.   │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

### 🔄 The Automatic Synchronization Lifecycle

Second Brain Plus enforces an **event-driven, zero-friction sync rule**:

```
[Agent or Developer Modifies Code / ADR / Notes]
                       │
                       ▼
             [auto_sync.py --now]
                       │
       ┌───────────────┼───────────────┬────────────────┐
       ▼               ▼               ▼                ▼
 [Notion Cloud]  [claude-mem]     [graphify]      [Git Remote]
 (API / ntn)    (Episodic Log)  (AST Graph)     (GitHub/GitLab)
```

1. **Non-Negotiable Auto-Sync:** Whenever a file, note, ADR, or session log changes, the agent triggers:
   ```bash
   python second-brain-plus/scripts/auto_sync.py --now
   ```
2. **Background Watcher:** For continuous real-time synchronization during development:
   ```bash
   python second-brain-plus/scripts/auto_sync.py --watch
   ```

---

### ⌨️ Dedicated Slash Commands (`/second-brain`)

Second Brain Plus introduces dedicated slash commands natively recognized across Antigravity IDE, Claude Code, Cursor, and terminal CLI:

| Slash Command | What It Does | Example Use Case |
| :--- | :--- | :--- |
| **`/second-brain install`** | Interactive setup wizard; scaffolds `.second-brain/` PARA vault, applies the 2026 Dev & AI blueprint, and builds all 7 Notion relational master databases via official API. | Initializing memory for a new repo. |
| **`/second-brain save memory <fact>`** | Instantly saves an atomic technical rule, port, or learning into persistent memory and auto-syncs. | `/second-brain save memory "Redis runs on port 6380 in docker-compose.prod"` |
| **`/second-brain adr <title>`** | Interactively registers an immutable Architecture Decision Record (ADR) with rationale and consequences. | `/second-brain adr "Migrate Auth to Passkeys"` |
| **`/second-brain sync`** | Forces an immediate bidirectional synchronization between local vault, Notion API, claude-mem, and graphify. | Running manual catch-up after offline git pull. |
| **`/second-brain status`** | Prints a visual telemetry dashboard showing note counts, API latency, hash integrity, and graph nodes. | Diagnostic check before starting work. |
| **`/second-brain git-status`** | Audits GitHub (`gh`) & GitLab (`glab`) remote synchronization, privacy (public/private), and proactive checks ("Needs anything else?"). | Inspecting backup security & remote divergence. |
| **`/second-brain git-sync`** | Commits and pushes all second-brain changes to the configured Git remote repository. | Offsite backup to GitHub or GitLab. |
| **`/second-brain task <title>`** | Schedules a task with target date/time, priority, and 4 atomic micro-steps (5-10 min each). | `/second-brain task "Refactor Auth" --when "2026-11-16 14:00" --p1` |
| **`/second-brain tasks`** | Displays a dashboard of all active, overdue, and scheduled tasks. | Reviewing today's schedule and sprint deliverables. |
| **`/second-brain do <id>`** | Autonomously executes a task: runs micro-steps, validates DoD, marks completed, and logs session. | `/second-brain do "Refactor Auth"` |
| **`/second-brain focus`** | Switches to ADHD / Neurodivergent Orbit OS single-task dashboard (1 micro-task at a time). | Countering cognitive overload and decision paralysis. |
| **`/second-brain tdah`** | Activates Portuguese TDAH accessibility mode with bionic bolding, short 45-65 character lines, and Body Doubling. | Maximum cognitive comfort during complex sessions. |

---

### 🐙🦊 Multi-Platform Remote Git Sync (GitHub `gh` & GitLab `glab`)

Second Brain Plus enables cryptographic, immutable Git backup across **GitHub** and **GitLab**:
1. **GitHub CLI (`gh` / https://cli.github.com/):**
   - Direct integration via `gh auth status`, `gh repo view`, and `gh repo create`.
2. **GitLab CLI (`glab` / https://docs.gitlab.com/cli/):**
   - Native integration via `glab auth status`, `glab repo view`, and `glab repo create`.
3. **Visibility Management (Private vs. Public):**
   - Defaults to **Private** repositories to safeguard sensitive decisions, internal notes, and proprietary architectures.
   - Supports **Public Digital Gardens** for open-source knowledge bases and community ADRs.
4. **Proactive Diagnostics ("Does It Need Anything Else?"):**
   - The engine audits `.gitignore` for secret leakage prevention, alerts on accidental public repo exposure, verifies commit sync (ahead/behind), and recommends automated CI/CD backup workflows.
   - See full technical guide in [docs/git_remote_sync_guide.md](docs/git_remote_sync_guide.md).

---

### 🌐 Official Notion 2026 Developer Stack Integration

Second Brain Plus incorporates the complete official Notion Developer platform:

| Component | Official Reference | Capabilities in Second Brain Plus |
| :--- | :--- | :--- |
| **Notion CLI (`ntn`)** | [ntn.dev](https://ntn.dev) & [CLI Docs](https://developers.notion.com/cli/get-started/overview) | Blazing-fast terminal access (`ntn whoami`, `ntn pages get`, `ntn databases query`, `ntn api`). |
| **Notion Workers** | [Notion Workers](https://developers.notion.com/workers/get-started/overview) | Serverless edge functions (`@notionhq/workers`) that run `onPageCreated` and `onPropertyChanged` triggers. |
| **Notion MCP Server** | [Notion MCP Guide](https://developers.notion.com/guides/mcp/get-started-with-mcp) | Native Model Context Protocol tools (`notion_search`, `notion_read_page`, `notion_append_block_children`). |
| **Agent & Data APIs** | [Working with Page Content](https://developers.notion.com/guides/data-apis/working-with-page-content) | Manipulates atomic Block trees (paragraphs, callouts, toggles, headings, code, tables). |
| **Admin API** | [Notion Admin API](https://developers.notion.com/reference/admin/intro) | Enterprise workspace audit logging (`/v1/admin/audit_logs`) and user provisioning (SCIM). |

*(See full technical guide in [docs/notion_developer_suite.md](docs/notion_developer_suite.md))*

---

### 🧩 Synergistic Ecosystem Integrations

Second Brain Plus does not reinvent existing best-of-breed tools — it orchestrates them into a unified cognitive stack:

- **`claude-mem`:** Manages episodic event timelines and temporal observation streams.
- **`graphify`:** Builds AST knowledge graph connections between notes, files, and architectural decisions (`.graphify/graph.json`).
- **`caveman`:** Enforces ASD-STE100 Simplified English to eliminate conversational fluff and token wastage.
- **`headroom`:** Intelligently compresses bulky tool outputs and JSON payloads before injection into context.
- **`context7`:** Connects to Upstash Context7 to fetch real-time, versioned API documentation for evolving packages.
- **`grill-me`:** Enforces the "Grill-then-Persist" cycle: conducts dialectical interviews to resolve ambiguities *before* coding, persisting conclusions as formal ADRs.
- **`karpathy-guidelines`:** Ingests Andrej Karpathy's 4 Laws of Engineering: Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution.
- **`impeccable`:** Enforces Paul Bakaus' craft standards to eliminate generic AI design artifacts.
- **`not-today-adhd`:** Cognitive accessibility engine ensuring neurodivergent individuals stay in flow state without paralysis.

---

### 📂 Directory Structure

```
second-brain-plus/
├── SKILL.md                              # Main bilingual agent runbook & instructions
├── README.md                             # Comprehensive documentation (this file)
├── CHANGELOG.md                          # SemVer changelog
├── VERSION                               # Current release (0.1.0-beta)
├── docs/                                 # In-depth architectural references
│   ├── architecture.md                   # 5-Layer memory specification & comparison
│   ├── notion_schemas.md                 # 7 Relational Notion master databases schema
│   ├── notion_developer_suite.md         # Notion CLI, Workers, MCP & Block tree guide
│   ├── git_remote_sync_guide.md          # GitHub (gh) & GitLab (glab) remote sync guide
│   ├── task_scheduling_and_execution.md  # Autonomous task scheduler & Orbit OS micro-steps
│   ├── recommended_notion_templates.md   # Canonical template gallery (Tiago Forte 2026)
│   ├── adhd_neurodivergent_guide.md      # Orbit OS & Brain Reset OS principles
│   ├── grill_me_integration.md           # "Grill-then-Persist" ADR workflow
│   ├── karpathy_guidelines_integration.md# 4 Laws of Engineering
│   ├── headroom_caveman_impeccable.md    # Context optimization & craft rules
│   └── context7_live_docs.md             # Real-time versioned documentation fetching
├── scripts/                              # Executable Python & CLI automation
│   ├── cli.py                            # Unified CLI for slash commands (/second-brain)
│   ├── auto_sync.py                      # Continuous watcher & one-shot sync engine
│   ├── task_scheduler.py                 # Autonomous task scheduling & execution engine
│   ├── git_remote_sync.py                # GitHub CLI & GitLab CLI multi-platform engine
│   ├── notion_sync.py                    # Zero-dependency Notion REST v2022-06-28 dynamic client
│   ├── build_notion_dashboard.py         # Canonical 2026 Dev & AI layout builder
│   ├── export_notion_blueprint.py        # Serializes live Notion dashboard into blueprint JSON
│   ├── memory_bridge.py                  # claude-mem + graphify + caveman bridge
│   ├── setup_and_sync.py                 # Interactive wizard, blueprint deployer & sync
│   ├── verify_brain.py                   # Integrity auditor for vaults and frontmatter
│   └── distribute_to_all_agents.py       # Universal deployer for all 9 AI agent runtimes
├── templates/                            # Ready-to-use schemas, blueprints and templates
│   ├── github/second-brain-sync.yml      # Automated GitHub Actions workflow template
│   ├── gitlab/.gitlab-ci.yml             # GitLab CI pipeline template
│   ├── notion/second_brain_blueprint.json# Canonical 2026 Dev & AI Layout Blueprint (7 Master DBs)
│   ├── notion-workers/sync-worker/       # TypeScript template for serverless Notion Workers
│   └── markdown/                         # Structured markdown notes (Project, ADR, Session, Orbit OS)
└── workflows/                            # Workflow definitions for Antigravity & AI agents
    ├── second-brain.md
    ├── second-brain-plus.md
    └── tdah.md
```

---

### 🏗️ Canonical 2026 Dev & AI Layout Blueprint (Cross-Project Ready)

Second Brain Plus ships with a **locked, official 2026 Software Engineering & AI Agent Layout Blueprint** (`templates/notion/second_brain_blueprint.json`):

1. **7 Master Databases (Encapsulated in `Backend`):**
   - 📁 **`Project`:** Active sprints, deliverables, and progress rollups.
   - ⚡ **`Tasks Manager`:** Scheduled tasks decomposed into 4 atomic micro-steps (5-10 min each).
   - 📝 **`Notes`:** Persistent Architecture Decision Records (ADRs) and episodic AI memories.
   - 📚 **`Resources`:** Technical references, API documentation, whitepapers, and runbooks.
   - 🌐 **`Areas`:** 5 core software engineering domains (`Engenharia de Software & Skills IA`, `Foundry VTT & Gravewright`, `DevOps & Docker`, `Arquitetura & Clean Code`, `Gestão Cognitiva & Foco TDAH`).
   - 🔄 **`Rotina Operacional Dev & IA`:** Daily operational checklist (`Git Sync`, `Auditoria 19/19`, `Micro-passos Orbit OS`, `Revisão de ADRs`, `Backup Remoto`).
   - 📖 **`Sessões & Diário de Bordo de IA`:** Persistent session logs tracking AI agent runs (`Antigravity`, `Claude Code`, `Hermes`, `Dev Charles`).

2. **Zero-Friction Cross-Project Deployment:**
   - **Deploy in New Project:** When installing in any new repository, simply set `NOTION_PARENT_PAGE_ID` in `.env` and run:
     ```bash
     python second-brain-plus/scripts/setup_and_sync.py
     ```
   - **Auto-Population:** The engine instantiates the exact visual layout from the blueprint and immediately scans the new repository's `.second-brain/`, populating all databases with that project's specific memories, tasks, and ADRs.

---

### 🚀 Quickstart: 3 Steps to Master Second Brain Plus

#### Step 1: Environment Setup
Add your Notion API Token and Parent Page ID to your environment or `.env` file:
```env
NOTION_API_KEY=ntn_your_notion_api_token_here
NOTION_PARENT_PAGE_ID=your_parent_page_id_here
SECOND_BRAIN_DIR=./.second-brain
```

#### Step 2: Run Setup & Verification
```bash
# Via slash command inside your AI chat:
/second-brain install

# Or directly in terminal:
python second-brain-plus/scripts/setup_and_sync.py
```

#### Step 3: Work with Persistent Memory & Git Sync
Save facts, create ADRs, query vault status, and sync to GitHub/GitLab:
```bash
python second-brain-plus/scripts/cli.py save memory "Production DB uses PostgreSQL 16"
python second-brain-plus/scripts/cli.py adr "Adopt DuckDB for Fast Analytics"
python second-brain-plus/scripts/cli.py status
python second-brain-plus/scripts/cli.py git-status
python second-brain-plus/scripts/cli.py git-sync
```

---

## 🇧🇷 Português (PT-BR)

### 📌 O Que É o Second Brain Plus?

O **Second Brain Plus** é uma suíte completa de **memória persistente, otimização de contexto e segundo cérebro** desenvolvida especificamente para agentes de inteligência artificial (Google Antigravity, Claude Code, Cursor, Codex, Copilot CLI, Hermes, Ollama).

#### ❌ O Problema dos Agentes Tradicionais:
1. **Amnésia de Contexto:** Cada reinício de sessão ou corte de janela de contexto apaga da memória do agente decisões anteriores, portas de serviços, bibliotecas adotadas e erros já superados.
2. **Alucinação por Dados Obsoletos:** Agentes inventam parâmetros e métodos de APIs que mudaram.
3. **Sobrecarga Cognitiva:** Prompts sobrecarregados de informações desnecessárias gastam tokens, encarecem a operação e diminuem a acurácia do raciocínio lógico.

#### ✅ A Solução do Second Brain Plus:
O Second Brain Plus estabelece uma **Única Fonte da Verdade (SSOT)** sincronizada em tempo real entre:
- **Nuvem no Notion:** Bancos de dados relacionais com visualização em Kanban, tabelas e acesso móvel (adotando oficialmente o modelo canônico [Second Brain All-in-One Productivity System 2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026)).
- **Repositórios Remotos Git (GitHub / GitLab):** Backup criptográfico, versionado e auditado via GitHub CLI (`gh`) e GitLab CLI (`glab`) com opção de visibilidade pública ou privada.
- **Cofre Local em Markdown (`.second-brain/`):** Arquivos versionados no Git local, com latência zero e leitura imediata offline.

---

### 🏛️ As 5 Camadas de Memória

1. **Memória de Trabalho (Working):** Estado do turno ativo, compactado via dialeto enxuto `caveman`.
2. **Memória Episódica (Eventos):** Linha do tempo de sessões e observações registradas no `claude-mem` e no Notion.
3. **Memória Semântica (Fatos e Regras):** Decisões Arquiteturais (ADRs), regras de negócio e verdades técnicas imutáveis.
4. **Memória Procedural (Habilidades):** Runbooks, checklists passo a passo e scripts operacionais reutilizáveis.
5. **Grafo de Conhecimento (Relações):** Conexões sintáticas e conceituais mapeadas pelo `graphify` em `.graphify/graph.json`.

---

### ⌨️ Comandos de Barra Dedicados (`/second-brain`)

| Comando | O Que Faz na Prática |
| :--- | :--- |
| **`/second-brain install`** | Executa o assistente de instalação, cria o cofre local P.A.R.A., aplica o blueprint Dev & IA 2026 e constrói os 7 bancos relacionais mestres no Notion via API. |
| **`/second-brain save memory <texto>`** | Grava instantaneamente uma verdade técnica ou regra no cofre persistente e sincroniza com a nuvem. |
| **`/second-brain adr <título>`** | Registra formalmente uma Decisão de Arquitetura (ADR) com justificativa e consequências, combatendo alucinações. |
| **`/second-brain sync`** | Dispara sincronização bidirecional forçada entre Notion, cofre local, claude-mem e grafo de conhecimento. |
| **`/second-brain status`** | Exibe painel com contagem de notas, saúde da conexão, hashes de integridade e nós do grafo. |
| **`/second-brain git-status`** | Audita a sincronização com GitHub (`gh`) e GitLab (`glab`), privacidade e verificações proativas ("Precisa de algo a mais?"). |
| **`/second-brain git-sync`** | Commita e envia (push) todas as alterações do segundo cérebro para o remote Git configurado. |
| **`/second-brain task <título>`** | Agenda uma tarefa com data/horário, prioridade e 4 micro-passos atômicos (5-10 min cada). |
| **`/second-brain tasks`** | Exibe painel com todas as tarefas ativas, agendadas e pendentes no cofre e Notion. |
| **`/second-brain do <id>`** | Executa autonomamente uma tarefa: cumpre micro-passos, valida DoD, marca como concluída e arquiva log. |
| **`/second-brain focus`** | Ativa a visualização Orbit OS com apenas 1 micro-tarefa ativa de 5 a 10 minutos. |
| **`/second-brain tdah`** | Ativa o modo neurodivergente com formatação biônica, linhas curtas e Body Doubling contra paralisia de tarefa. |

---

### 🐙🦊 Sincronização Remota Git (GitHub `gh` & GitLab `glab`)

- **Suporte Multi-Provedor:** Suporta nativamente repositórios no GitHub e no GitLab através de seus respectivos utilitários oficiais (`gh` e `glab`).
- **Controle de Privacidade:**
  - **Repositórios Privados (Padrão Recomendado):** Mantém decisões, anotações de equipe e planos proprietários sob sigilo absoluto.
  - **Jardins Digitais Públicos:** Permite publicar wikis abertas, ADRs comunitários e guias públicos.
- **Diagnóstico Proativo ("Precisa de Algo a Mais?"):**
  - O comando `git-status` verifica vazamento de chaves no `.gitignore`, divergência de branches (*ahead/behind*), visibilidade do repositório e sugere templates de automação de CI/CD. *(Consulte [docs/git_remote_sync_guide.md](docs/git_remote_sync_guide.md))*.

---

### 🌐 Ecossistema Oficial Notion Developer

- **Notion CLI (`ntn`):** Utilitário de linha de comando oficial de alta velocidade para consulta e exportação de páginas em Markdown puro.
- **Notion Workers (`@notionhq/workers`):** Automações serverless edge disparadas quando notas são criadas ou quando status são alterados.
- **Notion MCP (Model Context Protocol):** Conexão universal de ferramentas para os agentes consultarem o Notion em tempo de execução.
- **Manipulação de Blocos:** Edição e leitura direta da árvore de blocos (paragraphs, callouts, toggles, headings, code, tables).
- **Notion Admin API:** Logs corporativos de auditoria e sincronização de identidade (SCIM).

---

### 🏗️ Blueprint Canônico Padrão 2026 para Dev & IA (Pronto para Novos Projetos)

O Second Brain Plus inclui o **Blueprint Oficial de Engenharia de Software & Agentes de IA 2026** (`templates/notion/second_brain_blueprint.json`):

1. **7 Bancos de Dados Mestres (Alojados em `Backend`):**
   - 📁 **`Project`:** Projetos ativos, sprints, entregáveis e rollups de progresso.
   - ⚡ **`Tasks Manager`:** Tarefas agendadas e decompostas em 4 micro-passos atômicos (5-10 min cada).
   - 📝 **`Notes`:** Decisões Arquiteturais imutáveis (ADRs) e memórias episódicas de agentes de IA.
   - 📚 **`Resources`:** Referências técnicas, documentações de APIs e manuais de runbook.
   - 🌐 **`Areas`:** 5 áreas centrais de engenharia (`Engenharia de Software & Skills IA`, `Foundry VTT & Gravewright`, `DevOps & Docker`, `Arquitetura & Clean Code`, `Gestão Cognitiva & Foco TDAH`).
   - 🔄 **`Rotina Operacional Dev & IA`:** Checklist operacional diário (`Git Sync`, `Auditoria 19/19`, `Micro-passos Orbit OS`, `Revisão de ADRs`, `Backup Remoto`).
   - 📖 **`Sessões & Diário de Bordo de IA`:** Histórico persistente de execuções dos agentes (`Antigravity`, `Claude Code`, `Hermes`, `Dev Charles`).

2. **Provisionamento e Preenchimento em Novos Projetos:**
   - Ao iniciar qualquer novo repositório, basta definir `NOTION_PARENT_PAGE_ID` no `.env` e rodar:
     ```bash
     python second-brain-plus/scripts/setup_and_sync.py
     ```
   - O motor aplica automaticamente o layout padrão oficial idêntico e faz o auto-scout das notas, tarefas e memórias locais daquele novo projeto, preenchendo todos os cartões e tabelas na hora.

---

### ⚡ Regra Inegociável de Auto-Sincronização

> 🚨 **REGRA DE OURO:**  
> Sempre que qualquer arquivo de projeto, nota ou ADR for modificado pelo agente ou pelo desenvolvedor, a sincronização automática em segundo plano é disparada:
> ```bash
> python second-brain-plus/scripts/auto_sync.py --now
> ```
> Opcionalmente, mantenha o observador contínuo aberto em um terminal:
> ```bash
> python second-brain-plus/scripts/auto_sync.py --watch
> ```

---

## 📄 Licença / License
Desenvolvido por **GM Charles Corrêa** no âmbito do **Ecossistema Skills AI**. Distribuído sob a licença MIT.
