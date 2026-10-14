# Master of Foundry VTT 🎲⚡

> **Comprehensive Foundry Virtual Tabletop Mastery, Development & Architecture Suite**  
> *Suíte Completa de Desenvolvimento, Arquitetura e Mestria em Foundry Virtual Tabletop por GM Charles Corrêa*  
> **Current up to Foundry VTT v14.369 Stable**

---

## 🇺🇸 English

### 📌 Overview & Practical Authority
**Master of Foundry VTT** is an end-to-end development, scripting, and rule ingestion suite designed for developers, module creators, and Game Masters running **Foundry Virtual Tabletop**.

> [!IMPORTANT]
> **Source Material & Real-World Experience:**  
> All information, architectural patterns, and troubleshooting guides in this repository are rigorously based on **official Foundry VTT documentation, official release notes, policies, and API references**, combined directly with **first-hand, battle-tested practical experience in developing custom modules and systems for Foundry VTT (including the latest v14 architecture, ApplicationV2, and TypeDataModels)**.

This suite encapsulates official documentation, knowledge base articles, policies, API references from **Version 8 through Version 14**, Model Context Protocol (MCP) integrations, modern web exploration tools for module repositories, and architecture guides for over 60 famous RPG systems.

---

### 🌐 Knowledge Sources & Documentation

| Category | Reference / Guides |
|---|---|
| **Model Context Protocol (MCP)** | [`mcp/README.md`](mcp/README.md) (ninjos-foundry-mcp, foundryvtt-mcp, foundry-vtt-mcp) |
| **CLI Tools & Automation** | [`guides/cli-tools.md`](guides/cli-tools.md) (`@foundryvtt/foundryvtt-cli` & `fvtt-world-cli`) |
| **Sockets & Client-Server RPC** | [`guides/sockets.md`](guides/sockets.md) (Native `game.socket` & `socketlib`) |
| **Combat Tracker & Automation** | [`guides/combat.md`](guides/combat.md) (`Combat`, `Combatant`, `CombatTracker`) |
| **Famous Systems Knowledge Base** | [`systems/README.md`](systems/README.md) (D&D, PF2e, WoD, SWADE, Tormenta20, YZE, GURPS, CoC7, etc.) |
| **Official Systems Directory** | [https://foundryvtt.com/packages/systems](https://foundryvtt.com/packages/systems) |
| **Knowledge Base (Official & Guides)** | [`kb/`](kb/) & [https://foundryvtt.com/kb/](https://foundryvtt.com/kb/) |
| **SSL, HTTPS & Let's Encrypt (v14+)** | [`kb/07-ssl-and-https.md`](kb/07-ssl-and-https.md) (Native SSL in v14.369 vs Reverse Proxy) |
| **Releases & Changelogs** | [https://foundryvtt.com/releases/](https://foundryvtt.com/releases/) |
| **Limited License Agreement** | [`policies/license.md`](policies/license.md) |
| **AI Policy** | [`policies/ai-policy.md`](policies/ai-policy.md) |
| **Branding Guidelines** | [`policies/branding.md`](policies/branding.md) |
| **Privacy Policy** | [`policies/privacy-policy.md`](policies/privacy-policy.md) |
| **API Version 14 (Latest)** | [`versions/v14-api-guide.md`](versions/v14-api-guide.md) |
| **API Version 13** | [`versions/v13-api-guide.md`](versions/v13-api-guide.md) |
| **API Version 12** | [`versions/v12-api-guide.md`](versions/v12-api-guide.md) |
| **API Version 11** | [`versions/v11-api-guide.md`](versions/v11-api-guide.md) |
| **API Version 10** | [`versions/v10-api-guide.md`](versions/v10-api-guide.md) |
| **API Version 9** | [`versions/v09-api-guide.md`](versions/v09-api-guide.md) |
| **API Version 8** | [`versions/v08-api-guide.md`](versions/v08-api-guide.md) |

---

### 🔍 Repository Inspection & Analysis Web Tools
For studying third-party systems and modules directly in the browser or via automated ingestion:

| Tool | URL Template | Example (Foundry D&D 5e / SWADE Tools) |
|---|---|---|
| **Gitingest** | `https://gitingest.com/{{owner}}/{{repo}}` | `https://gitingest.com/foundryvtt/dnd5e` |
| **GitDiagram** | `https://gitdiagram.com/{{owner}}/{{repo}}` | `https://gitdiagram.com/foundryvtt/dnd5e` |
| **Repomix** | `https://repomix.com/?repo={{owner}}/{{repo}}` | `https://repomix.com/?repo=lipefl/swade-tools` |
| **Uithub** | `https://uithub.com/{{owner}}/{{repo}}?maxTokens=500000` | `https://uithub.com/lipefl/swade-tools?maxTokens=500000` |
| **DeepWiki** | `https://deepwiki.com/{{owner}}/{{repo}}` | `https://deepwiki.com/lipefl/swade-tools` |
| **Star History** | `https://www.star-history.com/?type=date&repos={{owner}}/{{repo}}` | `https://www.star-history.com/?type=date&repos=foundryvtt/dnd5e` |

---

### 🚀 How to Install & Use this Skill in Your Favorite AI Agent

#### ⚡ Fast Installation via `npx skills` (Skills.sh & Agent Skills Directory)
The fastest way to install this skill directly into your AI coding assistant (Antigravity, Claude Code, Cursor, Windsurf, etc.) is via the official **`skills`** CLI:

```bash
# Install directly from GitHub into your current project:
npx skills add CharlesCorreaDev/skills-ai --skill master-of-foundryvtt

# Or install it globally for your user across all projects:
npx skills add CharlesCorreaDev/skills-ai --skill master-of-foundryvtt -g
```

#### Option 1: Install from GitHub via Agent Customizations / Skills Root
Clone or copy the `master-of-foundryvtt` folder into your agent's global or workspace skills directory:

```bash
# 1. Clone this repository (or copy the master-of-foundryvtt directory)
git clone https://github.com/CharlesCorreaDev/skills-ai.git

# 2. Link or copy to your agent's skill folder:
# For Antigravity / Gemini CLI:
# Global: ~/.gemini/config/skills/master-of-foundryvtt (or %USERPROFILE%\.gemini\config\skills\master-of-foundryvtt on Windows)
# Workspace: .agents/skills/master-of-foundryvtt

# For Claude Code:
# Global: ~/.claude/skills/master-of-foundryvtt
# Workspace: .claude/skills/master-of-foundryvtt

# For Cursor / Windsurf:
# Place inside .cursor/rules/ or reference SKILL.md in project rules (.cursorrules / .windsurfrules)
```

#### Option 2: Direct Workspace Integration
Simply drop the `master-of-foundryvtt/` folder inside your Foundry VTT module or system project root:
```text
my-foundry-system/
├── src/
├── system.json
└── .agents/
    └── skills/
        └── master-of-foundryvtt/   <-- Entire skill folder here
```

#### 💬 How to Prompt Your AI Agent
Once loaded, the AI Agent automatically detects `SKILL.md`. You can invoke it naturally or explicitly:

- **Developing a New System (v14):**
  > *"Create a new Foundry VTT v14 system using ApplicationV2 and TypeDataModel for a d20-based modern horror game."*
- **Migrating Modules from v11/v12 to v14:**
  > *"Analyze this module's sheet code and migrate it from legacy Application to ApplicationV2 following the Master of Foundry VTT v14 standards."*
- **Connecting via MCP:**
  > *"Connect to my local Foundry VTT server using the ninjos-foundry-mcp server and inspect the active actors in the world."*
- **Investigating System Rules & Compendiums:**
  > *"Using the master-of-foundryvtt knowledge base, show me how to register custom roll formulas and active effects for Savage Worlds Adventure Edition (SWADE)."*

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (`pandoc`, `libreoffice`, `tesseract`), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---
---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral e Experiência Prática
O **Master of Foundry VTT** é uma suíte completa de desenvolvimento, automação, ingestão de regras e arquitetura desenvolvida para desenvolvedores de sistemas, criadores de módulos e Mestres de RPG que utilizam o **Foundry Virtual Tabletop**.

> [!IMPORTANT]
> **Base Oficial e Experiência Prática Real:**  
> Todas as informações, arquiteturas, padrões de código e diretrizes contidas neste repositório são rigorosamente fundamentadas na **documentação oficial do Foundry VTT, notas oficiais de lançamento, diretrizes/políticas e referências de API**, somadas diretamente à **experiência prática acumulada no desenvolvimento ativo de módulos e sistemas para o Foundry VTT v14** (incluindo o novo paradigma `ApplicationV2`, `TypeDataModel`, arquitetura de canvas e ESM nativo).

Ela consolida a base de conhecimento oficial, artigos, termos de licença, integrações MCP e referências de API da **Versão 8 até a Versão 14 (v14.369 Stable)**, oferecendo suporte para:
- Integração com **Servidores MCP** ([`mcp/README.md`](mcp/README.md)) para inspeção em tempo real e teste de macros.
- **Ferramentas de Linha de Comando (CLI)** ([`guides/cli-tools.md`](guides/cli-tools.md)) com `@foundryvtt/foundryvtt-cli` e `fvtt-world-cli` para compilação e automação de compêndios e mundos.
- Base de conhecimento arquitetural para **mais de 60 sistemas de RPG** ([`systems/README.md`](systems/README.md)).
- Criação e migração de **Sistemas de RPG** (`system.json`, `TypeDataModel`, Fichas Customizadas em `ApplicationV2`).
- Criação de **Módulos Adicionais** (`module.json`, Configurações, Sockets, libWrapper, Hooks).
- Guia nativo de **SSL, HTTPS e Let's Encrypt** ([`kb/07-ssl-and-https.md`](kb/07-ssl-and-https.md)) introduzido na v14.369.
- Ferramentas web para inspeção e estudo reverso de código de repositórios do ecossistema.

---

### 🚀 Como Instalar e Usar no seu Agente de IA Favorito

#### ⚡ Instalação Rápida via `npx skills` (Skills.sh & Diretório Agent Skills)
A maneira mais rápida de instalar esta skill diretamente no seu agente de IA (Antigravity, Claude Code, Cursor, Windsurf, etc.) é utilizando a CLI oficial do **`skills`**:

```bash
# Instalar diretamente no projeto atual:
npx skills add CharlesCorreaDev/skills-ai --skill master-of-foundryvtt

# Ou instalar globalmente para seu usuário (todos os projetos):
npx skills add CharlesCorreaDev/skills-ai --skill master-of-foundryvtt -g
```

#### Opção 1: Instalação via Diretório de Skills / Customizações
Clone o repositório ou copie a pasta `master-of-foundryvtt` para a pasta de skills do seu assistente:

```bash
# 1. Clone o repositório
git clone https://github.com/CharlesCorreaDev/skills-ai.git

# 2. Vincule ou copie a pasta master-of-foundryvtt para o diretório de skills:
# No Antigravity / Gemini CLI:
# Global: ~/.gemini/config/skills/master-of-foundryvtt (ou %USERPROFILE%\.gemini\config\skills\master-of-foundryvtt no Windows)
# Workspace local: .agents/skills/master-of-foundryvtt

# No Claude Code:
# Global: ~/.claude/skills/master-of-foundryvtt
# Workspace local: .claude/skills/master-of-foundryvtt

# No Cursor / Windsurf:
# Copie para .cursor/rules/ ou referencie o SKILL.md no seu .cursorrules ou .windsurfrules
```

#### Opção 2: Integração Direta no Repositório do seu Módulo ou Sistema
Você pode colocar a pasta `master-of-foundryvtt/` dentro da raiz do seu projeto de módulo ou sistema:
```text
meu-modulo-foundry/
├── src/
├── module.json
└── .agents/
    └── skills/
        └── master-of-foundryvtt/   <-- Pasta completa da skill aqui
```

#### 💬 Exemplos de Comandos e Prompts para o Agente
Com a skill ativa, seu agente reconhece automaticamente as diretrizes do `SKILL.md`. Experimente prompts como:

- **Desenvolvimento de Novo Sistema (v14):**
  > *"Crie a base de um novo sistema para Foundry VTT v14 utilizando ApplicationV2 e TypeDataModel para um RPG de investigação cósmica."*
- **Migração de Fichas Legadas:**
  > *"Migre esta ficha de ator feita no Application antigo do v11 para ApplicationV2 com template Handlebars limpo no padrão v14."*
- **Inspeção de Mundo em Tempo Real via MCP:**
  > *"Conecte ao meu servidor Foundry local usando o ninjos-foundry-mcp e liste todos os atores e itens do compêndio."*
- **Desenvolvimento de Módulos e Hooks:**
  > *"Crie um módulo com um hook de 'renderActorSheet' que injete um botão de rolagem rápida e envie notificações sonoras."*

---

### 🔍 Ferramentas Web para Análise de Repositórios e Módulos
Ferramentas úteis para estudar a arquitetura de sistemas e módulos existentes diretamente no navegador:

| Ferramenta | Template de URL | Exemplo de Uso (D&D 5e / SWADE Tools) |
|---|---|---|
| **Gitingest** | `https://gitingest.com/{{owner}}/{{repo}}` | `https://gitingest.com/foundryvtt/dnd5e` |
| **GitDiagram** | `https://gitdiagram.com/{{owner}}/{{repo}}` | `https://gitdiagram.com/foundryvtt/dnd5e` |
| **Repomix** | `https://repomix.com/?repo={{owner}}/{{repo}}` | `https://repomix.com/?repo=lipefl/swade-tools` |
| **Uithub** | `https://uithub.com/{{owner}}/{{repo}}?maxTokens=500000` | `https://uithub.com/lipefl/swade-tools?maxTokens=500000` |
| **DeepWiki** | `https://deepwiki.com/{{owner}}/{{repo}}` | `https://deepwiki.com/lipefl/swade-tools` |
| **Star History** | `https://www.star-history.com/?type=date&repos={{owner}}/{{repo}}` | `https://www.star-history.com/?type=date&repos=foundryvtt/dnd5e` |

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir pacotes extras (`pandoc`, `libreoffice`, `tesseract`, pacotes globais ou chaves de API), o agente DEVE solicitar permissão explícita ao desenvolvedor antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar o que foi instalado e configurado e executar um teste de validação.

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)
