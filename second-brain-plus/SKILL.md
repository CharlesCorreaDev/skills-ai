---
name: second-brain-plus
description: Persistent memory, context management, and second brain orchestration suite for AI agents via Notion API, GitHub CLI (gh), GitLab CLI (glab), and local structured files. Synchronizes project knowledge, episodic session logs, and architectural decisions automatically with claude-mem, graphify, caveman, headroom, and context7 to eliminate agent amnesia and prevent hallucinations. Enforces automatic background synchronization, supports private or public remote repositories with proactive security auditing, and provides slash commands (/second-brain install, /second-brain save memory, /second-brain adr, /second-brain sync, /second-brain status, /second-brain git-status, /second-brain git-sync, /second-brain focus, /second-brain tdah). Integrates with grill-me for pre-decision alignment, karpathy-guidelines for engineering rigor, impeccable for craft design, and activates not-today-adhd for neurodivergent cognitive accessibility. Use when building or managing persistent AI memory, setting up Notion and Git remotes as a Single Source of Truth, synchronizing local markdown vaults with remote knowledge bases, or designing anti-hallucination context architectures for autonomous agents.
---

# Second Brain Plus 🧠⚡💾
> *by GM Charles Corrêa — Ecossistema Skills AI*  
> **Status:** Beta (`v0.1.0-beta`)  
> **Core Concept / Conceito Central:** Single Source of Truth (SSOT), 5-Layer Persistent Memory, Multi-Platform Git Sync (GitHub/GitLab), Slash Commands & Automatic Synchronization

---

## 🇺🇸 English

### 📌 Overview, Philosophy & The SSOT Principle

**Second Brain Plus** solves the fundamental flaw of modern Large Language Models and autonomous coding agents: **context amnesia, token waste, and hallucination**.

When AI agents switch sessions or reach context window boundaries, they forget past architectural decisions, service ports, active blockers, and lessons learned.

> *"If technical decisions and project rules are scattered across transient chat logs, loose notes, and developer memory, the AI agent will hallucinate with 100% certainty."*

**Second Brain Plus** establishes a synchronized tri-layer infrastructure:
1. **Local Markdown Vault (`.second-brain/`):** Git-versioned, zero-latency, and offline-ready structured files following Tiago Forte's P.A.R.A. 2.0 (Projects, Areas, Resources, Archives).
2. **Notion Central Hub:** Collaborative, visual, and relational cloud dashboard for human review, Kanban tracking, and structured queries via Notion API.
3. **Multi-Platform Remote Git Repositories (GitHub / GitLab):** Cryptographic, versioned, immutable code & decision backup with private/public visibility control.
4. **Canonical Default Template & Blueprint:** [Second Brain All-in-One Productivity System 2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026) adopted and tailored for Software Engineering & AI Agents, versioned in `templates/notion/second_brain_blueprint.json` with 7 Master Databases (Projects, Tasks, Notes/ADRs, Resources, Dev Areas, Daily Dev Routine, AI Session Logs).

---

### ⌨️ Dedicated Slash Commands (`/second-brain`)

The skill responds to human-friendly slash commands across IDEs and terminals:

| Slash Command | Execution & Purpose |
| :--- | :--- |
| **`/second-brain install`** | Runs interactive setup wizard, scaffolds PARA vault, deploys the 2026 Dev & AI blueprint, and creates the 7 Notion relational databases via official API. |
| **`/second-brain save memory <fact>`** | Instantly saves rules, learnings, or facts into persistent memory & triggers immediate auto-sync. |
| **`/second-brain adr <title>`** | Formally registers an immutable Architecture Decision Record (anti-hallucination guardrail). |
| **`/second-brain sync`** | Triggers immediate bidirectional synchronization across Notion API, claude-mem, and graphify. |
| **`/second-brain status`** | Displays vault health, note count, hash integrity, graph nodes, and cloud API connectivity. |
| **`/second-brain git-status`** | Audits GitHub (`gh`) & GitLab (`glab`) remote sync, privacy (public/private), and proactive checks ("Needs anything else?"). |
| **`/second-brain git-sync`** | Commits and pushes all second-brain changes to the configured Git remote. |
| **`/second-brain task <title>`** | Schedules a task with target date/time, priority, and 4 atomic micro-steps (5-10 min each). |
| **`/second-brain tasks`** | Displays a dashboard of all active, overdue, and scheduled tasks. |
| **`/second-brain do <id>`** | Autonomously executes a task: runs micro-steps, validates DoD, marks completed, and logs session. |
| **`/second-brain focus`** | Switches to ADHD / Neurodivergent Orbit OS single-task view (1 micro-task at a time). |
| **`/second-brain tdah`** | Activates Portuguese TDAH mode with bionic bolding, short 45-65 character lines, and Body Doubling. |

---

### 🔄 Automatic File-Change Synchronization Rule

> 🚨 **NON-NEGOTIABLE AUTO-SYNC RULE:**  
> Whenever the AI agent modifies, creates, or detects changes in any project file, note, ADR, or task:
> 1. The agent **MUST IMMEDIATELY TRIGGER AUTOMATIC SYNCHRONIZATION**:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --now
>    ```
> 2. This coordinates:
>    - **Notion API / CLI:** Pushes updated note properties, hashes, and ADR content to cloud databases.
>    - **`claude-mem`:** Refreshes episodic timelines and temporal observation histories.
>    - **`graphify`:** Rebuilds AST connections and knowledge graph edges (`.graphify/graph.json`).
> 3. Alternatively, the user can run the continuous watcher:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --watch
>    ```

---

### 🏛️ The 5-Layer AI Memory Architecture

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
│ 3. Semantic Memory (Facts)   │ Business rules, ADRs, and    │ Local Vault / │
│                              │ live docs via Upstash Context7│ Notion Docs  │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 4. Procedural Memory (Skills)│ How to execute: runbooks and │ SKILL.md /    │
│                              │ Karpathy engineering laws    │ CLI Scripts   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 5. Knowledge Graph (Links)   │ Entity relations, causal     │ graphify /    │
│                              │ webs, and AST code links     │ RDF Triples   │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

### 🎙️ "Grill-then-Persist" Synergy (`grill-me` + `second-brain-plus`)

Before writing complex code or jumping into architecture implementations, the agent invokes `grill-me` to conduct an active, dialectical interview that surfaces implicit assumptions and uncovers blind spots. Once consensus is reached, the conclusion is **automatically distilled into a formal ADR** in `.second-brain/adr/` and pushed to Notion.

---

### 🔬 Karpathy Engineering Discipline (`karpathy-guidelines`)

The agent strictly adheres to Andrej Karpathy's 4 Laws of Software Engineering:
1. **Think Before Coding:** Verify APIs, inspect constraints, and design data flow first.
2. **Simplicity First:** Write the minimum viable code that solves the core problem; avoid premature abstractions.
3. **Surgical Precision:** Modify only what is strictly necessary; preserve surrounding idioms.
4. **Goal-Driven Verification:** Test every hypothesis with reproducible checks.

---

### ⚡ Neurodivergent Ergonomics (`not-today-adhd` & Orbit OS)

When ADHD mode is active (`/second-brain tdah` or `/second-brain focus`):
- Long lists and walls of text are hidden.
- Shows **only 1 active micro-task at a time (5 to 10 minutes duration)**.
- Adopts bionic bolding, short 45-65 character lines, and gentle Body Doubling check-ins to prevent task paralysis.

---

### 🌐 Official Notion Developer & AI Agents Ecosystem

Second Brain Plus integrates the entire official Notion Developer Platform:
1. **Notion CLI (`ntn` / https://ntn.dev):**
   - High-speed terminal operations: `ntn whoami`, `ntn pages get <id>`, `ntn databases query <id>`, `ntn workers deploy`.
2. **Notion Workers (`@notionhq/workers`):**
   - Serverless edge functions with `onPageCreated` and `onPropertyChanged` event triggers.
3. **Notion MCP (Model Context Protocol) & Notion Skills:**
   - Standard tool-calling bridge (`notion_search`, `notion_read_page`, `notion_append_block_children`).
4. **Notion Agent & Data APIs:**
   - Atomic Block tree manipulation (paragraphs, headings, toggles, callouts, tables) and enterprise Admin APIs.
   - See full architectural guide in [docs/notion_developer_suite.md](docs/notion_developer_suite.md).
5. **Canonical 2026 Dev & AI Layout Blueprint:**
   - Versioned natively in `templates/notion/second_brain_blueprint.json`.
   - Features 7 Master Databases (Projects, Tasks, Notes/ADRs, Resources, Dev Areas, Daily Dev Routine, AI Session Logs).
   - Instant deployment in any new project via `build_notion_dashboard.py` and auto-populated with that project's memories via `setup_and_sync.py`.

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

### ⚙️ Command-Line Execution Examples

```bash
# Save an atomic memory fact
python second-brain-plus/scripts/cli.py save memory "Production DB runs PostgreSQL 16 on port 5433"

# Register an immutable Architecture Decision Record (ADR)
python second-brain-plus/scripts/cli.py adr "Adopt Redis for Caching" --rationale "Maintain sub-5ms responses"

# Inspect second brain telemetry & health
python second-brain-plus/scripts/cli.py status

# Run proactive Git remote audit (GitHub/GitLab & privacy check)
python second-brain-plus/scripts/cli.py git-status

# Push second brain changes to Git remote
python second-brain-plus/scripts/cli.py git-sync

# Trigger immediate catch-up sync
python second-brain-plus/scripts/cli.py sync
```

---

## 🇧🇷 Português (PT-BR)

### 📌 Visão Geral, Filosofia & Princípio da SSOT

O **Second Brain Plus** resolve as três maiores limitações dos Large Language Models e agentes autônomos de código: **amnésia de contexto, desperdício de tokens e alucinação**.

Quando agentes trocam de sessão ou atingem o limite da janela de contexto, esquecem decisões de arquitetura anteriores, portas de rede, soluções de contorno e aprendizados obtidos.

> *"Se as anotações técnicas e regras de projeto estiverem dispersas entre chats temporários, arquivos de notas soltas e cabeças de desenvolvedores, o agente de IA alucinará com 100% de certeza."*

O **Second Brain Plus** estabelece uma infraestrutura sincronizada de camada tripla:
1. **Cofre Local em Markdown (`.second-brain/`):** Arquivos estruturados versionados no Git, com latência zero e leitura imediata offline, organizados segundo a metodologia P.A.R.A. 2.0 de Tiago Forte (Projetos, Áreas, Recursos, Arquivos).
2. **Hub Central no Notion:** Dashboard interativo com bancos de dados relacionais para acompanhamento humano em Kanban, tabelas e consultas estruturadas via Notion API.
3. **Repositórios Remotos Git Multi-Plataforma (GitHub / GitLab):** Backup criptográfico, versionado e imutável do código e decisões com controle de visibilidade privada ou pública.
4. **Template Padrão Canônico & Blueprint:** [Second Brain All-in-One Productivity System 2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026) adotado e adaptado para Engenharia de Software e Agentes de IA, versionado em `templates/notion/second_brain_blueprint.json` com 7 Bancos Mestres (Projetos, Tarefas, Notas/ADRs, Recursos, Áreas Dev, Rotina Operacional Dev, Diário de Sessões de IA).

---

### ⌨️ Comandos de Barra Dedicados (`/second-brain`)

A skill responde a comandos de barra amigáveis no chat da IDE e no terminal:

| Comando de Barra | Ação & Papel no Sistema |
| :--- | :--- |
| **`/second-brain install`** | Executa o assistente guiado de instalação, cria as pastas PARA, aplica o blueprint Dev & IA 2026 e constrói os 7 bancos relacionais mestres no Notion via API. |
| **`/second-brain save memory <fato>`** | Salva instantaneamente qualquer fato, regra ou aprendizado na memória persistente e auto-sincroniza. |
| **`/second-brain adr <título>`** | Registra formalmente uma Decisão de Arquitetura (ADR) inviolável contra alucinações. |
| **`/second-brain sync`** | Dispara a sincronização bidirecional imediata entre cofre local, Notion API, claude-mem e graphify. |
| **`/second-brain status`** | Exibe painel de saúde: notas ativas, nós do grafo, integridade de hashes e conectividade com a API. |
| **`/second-brain git-status`** | Audita a sincronização com GitHub (`gh`) e GitLab (`glab`), privacidade e verificações ("Precisa de algo a mais?"). |
| **`/second-brain git-sync`** | Commita e envia (push) todas as alterações do segundo cérebro para o remote Git configurado. |
| **`/second-brain task <título>`** | Agenda uma tarefa com data/horário, prioridade e 4 micro-passos atômicos (5-10 min cada). |
| **`/second-brain tasks`** | Exibe painel com todas as tarefas ativas, agendadas e pendentes no cofre e Notion. |
| **`/second-brain do <id>`** | Executa autonomamente uma tarefa: cumpre micro-passos, valida DoD, marca como concluída e arquiva log. |
| **`/second-brain focus`** | Alterna para o painel de foco único do modo neurodivergente (Orbit OS / TDAH - 1 tarefa por vez). |
| **`/second-brain tdah`** | Ativa o modo TDAH com formatação biônica, linhas curtas de 45-65 caracteres e Body Doubling contra paralisia. |

---

### 🔄 Regra Obrigatória de Sincronização Automática Contínua

> 🚨 **REGRA DE OURO DA AUTO-SINCRONIZAÇÃO:**  
> Sempre que o agente de IA realizar uma alteração, criar uma nova nota ou detectar que qualquer arquivo foi modificado:
> 1. O agente **DEVE DISPARAR A SINCRONIZAÇÃO AUTOMÁTICA IMEDIATA**:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --now
>    ```
> 2. Este comando coordena:
>    - **Notion API / CLI:** Envia propriedades atualizadas, hashes e conteúdo de ADRs para os bancos na nuvem.
>    - **`claude-mem`:** Atualiza a linha do tempo episódica e o histórico de observações.
>    - **`graphify`:** Reconstrói as conexões da AST e as arestas do grafo de conhecimento (`.graphify/graph.json`).
> 3. Opcionalmente, o usuário pode manter o observador contínuo aberto em segundo plano:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --watch
>    ```

---

### 🏛️ Arquitetura de Memória em 5 Camadas

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARQUITETURA DE MEMÓRIA EM 5 CAMADAS                      │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ Camada                       │ Finalidade                   │ Persistência  │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 1. Memória de Trabalho (RAM) │ Estado do turno ativo,       │ RAM da Sessão │
│                              │ compactado via Caveman       │ (Headroom)    │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 2. Memória Episódica (Logs)  │ Linha do tempo de sessões e  │ claude-mem /  │
│                              │ histórico de observações     │ Notion Logs   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 3. Memória Semântica (Fatos) │ Regras de negócio, ADRs e    │ Cofre Local / │
│                              │ docs ao vivo via Context7    │ Notion Docs   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 4. Memória Procedural (Como) │ Como executar: runbooks e    │ SKILL.md /    │
│                              │ as 4 Leis de Karpathy        │ Scripts CLI   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 5. Grafo de Conhecimento     │ Relações entre entidades e   │ graphify /    │
│                              │ links sintáticos de código   │ Triplas RDF   │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

### 🎙️ Sinergia "Grill-then-Persist" (`grill-me` + `second-brain-plus`)

Antes de iniciar a implementação de código complexo ou decisões de arquitetura, o agente aciona o `grill-me` para conduzir uma entrevista dialética profunda, eliminando premissas ocultas e pontos cegos. O consenso resultante é **automaticamente destilado em um ADR formal** em `.second-brain/adr/` e enviado ao Notion.

---

### 🔬 Disciplina de Engenharia Karpathy (`karpathy-guidelines`)

O agente segue rigorosamente as 4 Leis de Engenharia de Andrej Karpathy:
1. **Pense Antes de Codificar:** Verifique APIs, inspecione restrições e projete o fluxo de dados primeiro.
2. **Simplicidade Primeiro:** Escreva a menor quantidade viável de código que resolve o problema central; evite abstrações prematuras.
3. **Precisão Cirúrgica:** Altere apenas o estritamente necessário; preserve os padrões do código existente.
4. **Execução Orientada a Metas:** Valide cada hipótese com verificações reproduzíveis e testes.

---

### ⚡ Adaptação Neurodivergente (`not-today-adhd` & Orbit OS)

Quando o modo TDAH está ativo (`/second-brain tdah` ou `/second-brain focus`):
- Oculta listas longas e muralhas de texto.
- Exibe **somente 1 micro-tarefa ativa por vez (com duração de 5 a 10 minutos)**.
- Adota formatação biônica, linhas curtas de 45-65 caracteres e checagens amigáveis de Body Doubling para combater a paralisia de tarefa.

---

### 🌐 Ecossistema Oficial Notion Developer & AI Agents

A skill integra toda a infraestrutura oficial da Notion para agentes de IA:
1. **Notion CLI (`ntn` / https://ntn.dev):**
   - Comandos de alta performance: `ntn whoami`, `ntn pages get <id>`, `ntn databases query <id>`, `ntn workers deploy`.
2. **Notion Workers (`@notionhq/workers`):**
   - Funções serverless edge com gatilhos de criação de página (`onPageCreated`) e alteração de propriedades (`onPropertyChanged`).
3. **Notion MCP (Model Context Protocol) & Notion Skills:**
   - Protocolo universal para agentes de IA realizarem buscas híbridas e gravação atômica em páginas (`notion_search`, `notion_read_page`, `notion_append_block_children`).
4. **Notion Agent & Data APIs:**
   - Manipulação nativa da árvore de blocos (parágrafos, cabeçalhos, toggles, callouts, tabelas) e APIs corporativas de Admin (Audit Logs e SCIM).
   - Consulte o guia completo em [docs/notion_developer_suite.md](docs/notion_developer_suite.md).
5. **Blueprint Padrão Oficial 2026 para Devs & IA:**
   - Versionado nativamente em `templates/notion/second_brain_blueprint.json`.
   - Inclui os 7 Bancos Mestres (Projetos, Tarefas, Notas/ADRs, Recursos, Áreas Dev, Rotina Operacional Dev, Diário de Sessões de IA).
   - Provisionamento instantâneo em qualquer novo projeto via `build_notion_dashboard.py` e preenchimento automático das memórias daquele projeto via `setup_and_sync.py`.

---

### 🐙🦊 Sincronização Remota Multi-Plataforma Git (GitHub `gh` e GitLab `glab`)

O Second Brain Plus oferece backup criptográfico e imutável via Git no **GitHub** e no **GitLab**:
1. **GitHub CLI (`gh` / https://cli.github.com/):**
   - Integração nativa com `gh auth status`, `gh repo view` e `gh repo create`.
2. **GitLab CLI (`glab` / https://docs.gitlab.com/cli/):**
   - Suporte completo com `glab auth status`, `glab repo view` e `glab repo create`.
3. **Gestão de Visibilidade (Privado vs. Público):**
   - Padrão **Privado** para salvaguardar anotações confidenciais, regras de negócio e ADRs internos.
   - Suporte a **Jardins Digitais Públicos** para documentações abertas e bibliotecas comunitárias.
4. **Diagnóstico Proativo ("Precisa de Algo a Mais?"):**
   - O motor audita o `.gitignore` contra vazamento de segredos, alerta sobre repositórios públicos acidentais, valida commits pendentes (*ahead/behind*) e recomenda workflows de CI/CD para backup automatizado.
   - Consulte o guia técnico em [docs/git_remote_sync_guide.md](docs/git_remote_sync_guide.md).

---

### ⚙️ Exemplos de Execução via Linha de Comando

```bash
# Salvar memória técnica atômica
python second-brain-plus/scripts/cli.py save memory "PostgreSQL 16 de produção roda na porta 5433"

# Registrar Decisão de Arquitetura (ADR) imutável
python second-brain-plus/scripts/cli.py adr "Adoção do Redis para Cache" --rationale "Garantir respostas < 5ms"

# Ver telemetria e saúde do segundo cérebro
python second-brain-plus/scripts/cli.py status

# Executar auditoria proativa do Git remoto (GitHub/GitLab e checagem de privacidade)
python second-brain-plus/scripts/cli.py git-status

# Enviar alterações do cofre para o repositório remoto
python second-brain-plus/scripts/cli.py git-sync

# Disparar sincronização manual imediata
python second-brain-plus/scripts/cli.py sync
```
