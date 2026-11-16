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

