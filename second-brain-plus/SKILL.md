---
name: second-brain-plus
description: Persistent memory, context management, and second brain orchestration suite for AI agents via Notion API and local structured files. Synchronizes project knowledge, episodic session logs, and architectural decisions automatically with claude-mem, graphify, caveman, headroom, and context7 to eliminate agent amnesia and prevent hallucinations. Enforces automatic background synchronization and provides slash commands (/second-brain install, /second-brain save memory, /second-brain adr, /second-brain sync, /second-brain status, /second-brain focus). Integrates with grill-me for pre-decision alignment, karpathy-guidelines for engineering rigor, impeccable for craft design, and activates not-today-adhd for neurodivergent cognitive accessibility. Use when building or managing persistent AI memory, setting up Notion as a Single Source of Truth, synchronizing local markdown vaults with remote knowledge bases, or designing anti-hallucination context architectures for autonomous agents.
---

# Second Brain Plus 🧠⚡💾
> *by GM Charles Corrêa — Ecossistema Skills AI*  
> **Status:** Beta (`v0.1.0-beta`)  
> **Conceito Central:** Single Source of Truth (SSOT), 5-Layer Persistent Memory, Slash Commands & Automatic Synchronization

---

## 🇺🇸 English

### 📌 Overview & Philosophy

**Second Brain Plus** solves the fundamental flaw of modern Large Language Models and autonomous coding agents: **context amnesia and hallucination**.

When AI agents switch sessions or reach context window boundaries, they forget past decisions, project status, active blockers, and lessons learned.

**Second Brain Plus** establishes a synchronized dual-layer infrastructure:
- **Notion API Hub:** Collaborative, visual, and relational cloud dashboard.
- **Local Markdown Vault (`.second-brain/`):** Git-versioned, zero-latency, and offline-ready.

---

### ⌨️ Dedicated Slash Commands (`/second-brain`)

The skill responds to human-friendly slash commands:

| Slash Command | Execution & Value |
|---|---|
| **`/second-brain install`** | Runs interactive setup, scaffolds PARA vault, and creates Notion databases |
| **`/second-brain save memory <fact>`** | Instantly saves rules, learnings, or facts into persistent memory & auto-syncs |
| **`/second-brain adr <title>`** | Formally registers an immutable Architecture Decision Record (anti-hallucination) |
| **`/second-brain sync`** | Triggers immediate two-way synchronization with Notion, claude-mem & graphify |
| **`/second-brain status`** | Displays vault health, note count, graph nodes, and cloud connection status |
| **`/second-brain focus`** | Switches to ADHD / Neurodivergent Orbit OS single-task view |
| **`/second-brain tdah`** | Ativa o modo TDAH com formatação biônica, 1 micro-ação por vez e Body Doubling |

---

### 🔄 Automatic File-Change Synchronization Rule

> 🚨 **NON-NEGOTIABLE AUTO-SYNC RULE:**  
> Whenever the AI agent modifies, creates, or detects changes in any project file, note, ADR, or task:
> 1. The agent **MUST IMMEDIATELY TRIGGER AUTOMATIC SYNCHRONIZATION**:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --now
>    ```
> 2. This coordinates:
>    - **Notion API:** Pushes updated note properties, hashes, and ADR content to cloud databases.
>    - **`claude-mem`:** Refreshes episodic timelines and observation logs.
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

## 🇧🇷 Português

### 🎯 Princípio da Única Fonte da Verdade (SSOT)

> *"Se as anotações e decisões estiverem dispersas entre chats temporários, arquivos de notas soltas e cabeças de desenvolvedores, o agente de IA alucinará com 100% de certeza."*

O **Second Brain Plus** estabelece dois pilares sincronizados:
1. **Local Vault (`.second-brain/` ou `memory/`):** Repositório local versionado via Git, composto de notas Markdown puras com Frontmatter YAML padronizado.
2. **Notion Central Hub:** Dashboard interativo com bancos de dados relacionais para visualização humana e consultas estruturadas via Notion API.

---

### ⌨️ Comandos de Barra Dedicados (`/second-brain`)

O usuário e o agente operam através de comandos diretos:

| Comando de Barra | Ação & Papel no Sistema |
|---|---|
| **`/second-brain install`** | Inicia a instalação guiada, cria pastas PARA e bancos relacionais no Notion |
| **`/second-brain save memory <fato>`** | Salva instantaneamente qualquer fato, regra ou aprendizado na memória e auto-sincroniza |
| **`/second-brain adr <título>`** | Registra formalmente um novo ADR inviolável contra alucinações |
| **`/second-brain sync`** | Dispara a sincronização manual imediata entre local, Notion, claude-mem e graphify |
| **`/second-brain status`** | Exibe painel de saúde: notas ativas, nós do grafo e status da conexão com a API |
| **`/second-brain focus`** | Ativa o painel de foco único do modo neurodivergente (Orbit OS / TDAH) |
| **`/second-brain tdah`** | Ativa o modo TDAH com formatação biônica, 1 micro-ação por vez e Body Doubling |

---

### 🔄 Regra Obrigatória de Sincronização Automática Contínua

> 🚨 **REGRA DE OURO DA AUTO-SINCRONIZAÇÃO:**  
> Sempre que o agente de IA realizar uma alteração, criar uma nova nota ou detectar que qualquer arquivo foi modificado:
> 1. O agente **DEVE DISPARAR A SINCRONIZAÇÃO AUTOMÁTICA IMEDIATA**:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --now
>    ```
> 2. O usuário também pode deixar o monitor contínuo rodando em segundo plano:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --watch
>    ```

---

### 🎙️ Sinergia "Grill-then-Persist" (`grill-me` + `second-brain-plus`)

A skill `grill-me` conduz uma entrevista dialética profunda para eliminar ambiguidades antes de começar a codificar. O resultado é destilado automaticamente em um ADR formal no Notion e no repositório local.

---

### 🔬 Disciplina de Engenharia Karpathy (`karpathy-guidelines`)

O agente aplica rigorosamente as 4 Leis de Andrej Karpathy: Pense Antes de Codificar, Simplicidade Primeiro, Mudanças Cirúrgicas e Execução Orientada a Metas.

---

### ⚡ Adaptação Neurodivergente (`not-today-adhd` & Orbit OS)

Quando ativado, oculta listas longas, exibe **somente 1 micro-tarefa ativa de 5 a 10 minutos**, adota matriz de Eisenhower enxuta e formatação biônica sem muralhas de texto.

---

### ⚙️ Execução via CLI

```bash
# Salvar memória
python second-brain-plus/scripts/cli.py save memory "PostgreSQL porta 5433 banco skills_db"

# Registrar ADR
python second-brain-plus/scripts/cli.py adr "Adoção do Redis para Cache" --rationale "Garantir respostas < 5ms"

# Ver status
python second-brain-plus/scripts/cli.py status

# Sincronizar
python second-brain-plus/scripts/cli.py sync
```
