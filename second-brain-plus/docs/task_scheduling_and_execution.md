# Autonomous Task Scheduling & Execution Engine 📅⚡🤖
> *Scheduling, Calendar Synchronization, Micro-Step Decomposition & Autonomous Task Runner*  
> **Status:** Official 2026 Reference | **Compatible with:** Antigravity, Claude Code, Cursor, Codex, Copilot CLI

---

## 🇺🇸 English

### 1. Architectural Overview: From Passive Memory to Active Execution

Second Brain Plus transitions from a passive cognitive store into an **active autonomous executive assistant**. It manages the complete lifecycle of tasks:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        USER / AGENT INTERFACE                          │
│          /second-brain task  •  /second-brain do  •  /second-brain tasks│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      TASK SCHEDULER & RUNNER                           │
│  ┌─────────────────────────┐           ┌────────────────────────────┐  │
│  │  1. Scheduling & Dates  │           │  2. Action Loop Pipeline   │  │
│  │  - ISO Date/Time        │           │  - Micro-Decomposition     │  │
│  │  - Notion Calendar View │           │  - Autonomous Execution    │  │
│  │  - Google Cal Two-Way   │           │  - Definition of Done (DoD)│  │
│  └────────────┬────────────┘           └────────────┬───────────────┘  │
└───────────────┼─────────────────────────────────────┼──────────────────┘
                │                                     │
                ▼                                     ▼
┌───────────────────────────────┐     ┌──────────────────────────────────┐
│      NOTION CLOUD HUB         │     │     LOCAL VAULT & GIT BACKUP     │
│ - Projects & Sprints DB       │     │ - .second-brain/1-Projects/tasks/│
│ - Calendar & Kanban Views     │     │ - 4-Archives/sessions/ (Logs)    │
│ - Auto-Checked Micro-Steps    │     │ - Git Commit & Push Safeguard    │
└───────────────────────────────┘     └──────────────────────────────────┘
```

---

### 2. Dedicated Slash Commands for Tasks & Scheduling

| Slash Command | Execution & Purpose |
| :--- | :--- |
| **`/second-brain task <title> [--when <datetime>] [--p1\|--p0]`** | Creates and schedules a new task with target date/time, priority, and 4 atomic micro-steps (5-10 min each). Slices work immediately to defeat procrastination. |
| **`/second-brain tasks`** | Displays a clean, bionic-formatted dashboard of all active, overdue, and scheduled tasks. |
| **`/second-brain do <task_id_or_title>`** | Launches autonomous execution: updates status to `In Progress`, verifies each micro-step, marks `Completed`, logs session in `4-Archives/sessions/`, and auto-syncs Notion & Git. |

---

### 3. Notion Calendar & Google Calendar Integration

- Any item created via `/second-brain task` with a `--when` flag (e.g. `2026-11-16 10:00`) populates the **`Deadline`** and **`ScheduledDate`** property.
- When opening **Notion Calendar** (desktop or mobile), the `Projects & Sprints` database automatically renders as an interactive calendar timeline.
- Because Notion Calendar links directly with **Google Calendar**, tasks scheduled through Second Brain Plus appear immediately on your smartphone and laptop calendar with reminders.

---

### 4. The 4-Step Autonomous Action Loop

When `/second-brain do` is triggered:
1. **Decompose (Anti-Procrastination):** Enforces Orbit OS / TDAH ergonomics: decomposes the objective into 4 atomic micro-actions of 5-10 minutes.
2. **Execute (Karpathy Rigor):** The agent applies Karpathy's 4 Laws of Engineering: think before coding, minimal surgical modifications, and goal-driven verification.
3. **Verify (Definition of Done):** Tests and validates that the solution functions cleanly without regressions.
4. **Persist & Complete:**
   - Marks the task as `Completed` in Notion and local Markdown.
   - Archives the session execution log into `.second-brain/4-Archives/sessions/sess-task-<id>.md`.
   - Triggers `auto_sync.py --now` and Git remote sync.

---

## 🇧🇷 Português (PT-BR)

### 1. Visão Geral: De Memória Passiva para Assistente Executivo Ativo

O Second Brain Plus evolui de um simples repositório cognitivo para um **assistente executivo autônomo**. Ele cuida do ciclo completo de agendamento e realização de tarefas:
- **Agendamento com Data/Hora:** Integração direta com o Notion Calendar e Google Agenda.
- **Decomposição em Micro-Passos (Orbit OS / TDAH):** Fatiamento em blocos atômicos de 5 a 10 minutos para vencer a paralisia de tarefa.
- **Execução Autônoma (`/second-brain do`):** O agente assume a tarefa, implementa, testa, conclui e gera o relatório na memória episódica.

### 2. Comandos de Barra Práticos

```bash
# 1. Agendar uma nova tarefa com data e alta prioridade
/second-brain task "Refatorar Módulo de Autenticação" --when "2026-11-16 14:00" --p1

# 2. Listar tarefas ativas e agendadas
/second-brain tasks

# 3. Executar autonomamente uma tarefa pendente
/second-brain do "Refatorar Módulo"
```

### 3. Sincronização com o Calendário

- Tarefas agendadas aparecem instantaneamente no **Notion Calendar** e no **Google Calendar**.
- Ao concluir a tarefa via `/second-brain do`, o status no Notion é atualizado automaticamente para `Completed`, a sessão é arquivada em `.second-brain/4-Archives/sessions/` e o backup no Git é sincronizado.
