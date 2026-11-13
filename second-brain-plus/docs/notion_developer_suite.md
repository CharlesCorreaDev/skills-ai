# Notion Developer Suite & AI Agent Ecosystem 🧠⚡🌐
> *Comprehensive Reference for Notion CLI, Workers, MCP Servers, Agent APIs & Page Content*  
> **Status:** Official 2026 Reference | **Compatible with:** Antigravity, Claude Code, Cursor, Codex, Copilot CLI

---

## 🇺🇸 English

### 1. Architectural Overview

The **Second Brain Plus** architecture interfaces with Notion across four complementary integration tiers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AI AGENTS & INTERFACES                          │
│  (Antigravity IDE / Claude Code / Cursor / Codex / Copilot CLI / TTY) │
└──────────────────┬─────────────────┬───────────────────┬───────────────┘
                   │                 │                   │
         [Tier 1: MCP Server] [Tier 2: CLI (ntn)] [Tier 3: Native SDK]
                   │                 │                   │
┌──────────────────▼─────────────────▼───────────────────▼───────────────┐
│                    OFFICIAL NOTION CLOUD PLATFORM                      │
│                                                                        │
│  ┌───────────────────────────┐       ┌───────────────────────────────┐ │
│  │   Notion Agent & Data     │       │    Notion Workers Engine      │ │
│  │   REST APIs (2022-06-28)  │       │    (@notionhq/workers edge)   │ │
│  └─────────────┬─────────────┘       └───────────────┬───────────────┘ │
│                │                                     │                 │
│  ┌─────────────▼─────────────────────────────────────▼───────────────┐ │
│  │  P.A.R.A. 2.0 Workspaces (Projects, ADRs, Sessions, Resources)    │ │
│  │  Enterprise Admin APIs (Audit Logs, SCIM, Workspace Controls)     │ │
│  └───────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 2. Notion CLI (`ntn` / https://ntn.dev)

The official **Notion CLI** provides zero-latency terminal commands, instant markdown export, and worker deployment.

#### Installation
- **Windows (Winget):** `winget install Notion.ntn`
- **npm (Universal):** `npm install -g --allow-scripts=ntn ntn`
- **Linux / macOS:** `curl -fsSL https://ntn.dev | bash`

#### Authentication & Setup
```bash
# 1. Login interactively via browser
ntn login

# 2. Or authenticate using bot token
export NOTION_API_TOKEN="ntn_your_notion_api_token_here" # Linux/macOS
$env:NOTION_API_TOKEN="ntn_your_notion_api_token_here"  # Windows PowerShell

# 3. Verify identity
ntn whoami
```

#### Core CLI Commands for Second Brain
| Command | Action | Output / Use Case |
| :--- | :--- | :--- |
| `ntn whoami` | Inspect authenticated bot/user | Validates token scope & bot identity |
| `ntn pages get <page_id>` | Fetch page as clean Markdown | Direct ingest into local `.second-brain/` vault |
| `ntn databases query <db_id>` | Query database entries as JSON | Batch sync for Projects, ADRs, Sessions |
| `ntn api <method> <path> [data]`| Direct curl-like raw API access | Test custom endpoints without writing scripts |
| `ntn workers deploy` | Deploy serverless Notion Worker | Ship automated edge triggers to Notion Cloud |

---

### 3. Notion Workers (`@notionhq/workers`)

**Notion Workers** are serverless JavaScript/TypeScript functions running at the edge natively inside Notion. They enable event-driven automations, automated memory distillation, and proactive agent notifications.

#### Key Triggers & Events
1. **`on_page_created`**: Triggers when a human adds a task or note; distills key insights and updates ADRs.
2. **`on_property_changed`**: Detects status transitions (e.g., Project moving from `In Progress` to `Completed`) and triggers memory compaction.
3. **`scheduled_cron`**: Runs nightly episodic log summarization and pushes alerts to AI agent webhooks.

#### Sample Worker Definition (`sync-worker.ts`)
```typescript
import { defineWorker } from "@notionhq/workers";

export default defineWorker({
  name: "second-brain-sync-worker",
  async onPageCreated({ page, notion }) {
    console.log(`[Worker] New page created: ${page.id}`);
    // Auto-tag neurodivergent priority if flagged
    if (page.properties["Title"]?.title?.[0]?.plain_text.includes("[CRITICAL]")) {
      await notion.pages.update({
        page_id: page.id,
        properties: {
          "Status": { select: { name: "Active" } }
        }
      });
    }
  }
});
```

---

### 4. Notion MCP (Model Context Protocol) & Notion Skills

Notion MCP bridges AI Agent runtimes directly into Notion workspace knowledge without manual copy-pasting.

#### Available MCP Primitives
- `notion_search`: Global hybrid vector and keyword search across pages and databases.
- `notion_read_page`: Read page blocks and extract nested text, tables, and synced blocks.
- `notion_append_block_children`: Append new content blocks to a page or database item.
- `notion_update_properties`: Modify frontmatter properties (Status, Tags, Dates, Relations).
- `notion_query_database`: Query relational databases using complex property filters and sorting.

#### MCP Configuration (`mcp_config.json`)
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-notion"],
      "env": {
        "NOTION_API_TOKEN": "ntn_your_notion_api_token_here"
      }
    }
  }
}
```

---

### 5. Working with Page Content (Block Architecture)

The Notion REST API treats documents as trees of **Blocks**. Every paragraph, heading, list item, and code block is an atomic unit.

#### Block Types Supported by Second Brain Plus
- `heading_1`, `heading_2`, `heading_3`: Structured hierarchies.
- `paragraph`: Standard prose with markdown-equivalent annotations.
- `bulleted_list_item` & `numbered_list_item`: Progressive procedural checklists.
- `to_do`: Action items (`checked: true | false`).
- `toggle`: Expandable disclosures for progressive token disclosure.
- `callout`: Visual emphasis with emoji badges (crucial for ADHD microcopy).
- `code`: Syntactically highlighted snippets with `language` metadata.
- `table` & `table_row`: Structured tabular comparative data.

---

### 6. Admin API (`/v1/admin/`)

For enterprise workspaces, Notion provides workspace-wide governance:
- **Audit Logs API (`/v1/admin/audit_logs`)**: Real-time log export of page views, edits, permissions, and exports.
- **SCIM API (`/v1/admin/scim`)**: Automated user provisioning, group synchronization, and role management.
- **Workspace Analytics**: Usage tracking and bot rate-limit consumption telemetry.

---

## 🇧🇷 Português (PT-BR)

### 1. Visão Geral da Arquitetura

O **Second Brain Plus** integra-se com a plataforma oficial do Notion em quatro camadas complementares:
1. **Notion CLI (`ntn`)**: Utilitário nativo de terminal de alta velocidade para inspeção de páginas e deploy de workers.
2. **Notion Workers**: Funções serverless edge que executam internamente no Notion para automação de eventos e gatilhos de IA.
3. **Notion MCP (Model Context Protocol)**: Ferramentas nativas consumidas por agentes (Antigravity, Claude Code, Cursor) para consultar e gravar blocos em tempo real.
4. **Notion Agent & Data APIs**: API REST v2022-06-28 completa para manipular banco de dados relacionais e árvores de blocos.

### 2. Comandos do Notion CLI (`ntn`)
- `ntn whoami`: Verifica autenticação do bot (`Second-brain-plus`).
- `ntn pages get <page_id>`: Exporta página do Notion diretamente como Markdown limpo para o vault local `.second-brain/`.
- `ntn databases query <db_id>`: Consulta os bancos de dados de Projetos, ADRs e Sessões.
- `ntn workers deploy`: Publica workers serverless para execução automatizada na nuvem.

### 3. Integração com Neurodivergência (ADHD / TDAH)
- Chamadas de API formatadas com blocos `callout` e títulos claros.
- Redução de ruído com `toggle blocks` para ocultar detalhes secundários até que o usuário solicite.
- Sincronização em background zero-atrito para evitar paralisia de decisão.
