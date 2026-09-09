---
name: master-of-foundryvtt
description: Master development, administration, and automation suite for Foundry Virtual Tabletop (v8, v9, v10, v11, v12, v13, v14) by GM Charles Corrêa. Ingests Knowledge Base, Release Notes, Policies (Branding, AI, License, Privacy), and API documentation across all versions. Guides creation of Systems, Modules, Macros, Rollable Tables, Handouts, Items, and Active Effects. Use when developing for Foundry VTT, troubleshooting module conflicts, verifying license compliance, or ingesting RPG system rulebooks (Pathfinder 2e, D&D 5e, GURPS, Savage Worlds, Fate, Tormenta20) via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama.
---

# Master of Foundry VTT 🎲⚡
> *by GM Charles Corrêa*

---

## 🇺🇸 English

### 📌 Core Mission & Agent Mandates

**Master of Foundry VTT** is the definitive, multi-version knowledge base and development companion for **Foundry Virtual Tabletop**. It covers client/server architecture, API evolutions from v8 through v14, policies, system and module creation, macro scripting, and RPG system integration.

---

### 🚨 Mandatory Directives for AI Agents

Whenever an AI Agent is tasked with any Foundry VTT assignment, it **MUST ALWAYS** follow these five core protocols:

#### 1. Version Inquiry Mandate (Gatekeeper)
Before writing any code, script macro, DataModel, or advising on APIs:
- **The Agent MUST ASK the developer/operator which Foundry VTT version they are targeting** (e.g., v12, v11, v13, v10, v9, or v8), unless explicitly stated in the prompt.
- **Rationale:** API contracts change dramatically between versions (e.g., `0.8.x` document migration, `v10` DataModel schema system, `v12` ApplicationV2 migration). Mixing versions causes silent failures.

#### 2. License & Policy Compliance Verification
- The Agent must audit every planned feature against Foundry VTT's **Limited License Agreement**, **AI Policy**, and **Branding Guidelines**.
- **Crucial Rule:** Never redistribute core Foundry software, proprietary premium compendium content, or trademarked logos without authorization. If a requested feature risks violating policies, the Agent **MUST WARN the developer immediately**.

#### 3. RPG System Ingestion & Context Protocol
When developing or troubleshooting for specific RPG systems (e.g., **Pathfinder 2e, D&D 5e, Savage Worlds, GURPS, Fate, Tormenta20**):
1. The Agent **MUST ask the developer for:**
   - The rulebook PDF or reference material.
   - The repository link (GitHub/GitLab) of the Foundry system.
   - The exact system version installed.
2. The Agent will ingest and convert these references into clean Markdown under a dedicated knowledge base for persistent context.

#### 4. Active Module Audit & Troubleshooting Protocol
When diagnosing errors, console exceptions, or unexpected UI behavior:
- The Agent **MUST ask the developer for the list of currently active modules and their versions**.
- Isolate conflicts by advising binary search testing (`Find the Culprit` / safe mode) and checking `libWrapper` hooks.

#### 5. Autonomous Error Recovery & Permission Protocol
- If installation or execution fails, the agent must diagnose root causes and self-correct.
- For extra system packages or external tools, request explicit user permission before proceeding.

---

### 📚 Structure & Fast-Path Navigation

- [API Versions Guide](versions/)
  - [Version 14 API Guide](versions/v14-api-guide.md)
  - [Version 13 API Guide](versions/v13-api-guide.md)
  - [Version 12 API Guide & ApplicationV2](versions/v12-api-guide.md)
  - [Version 11 API Guide & DataModels](versions/v11-api-guide.md)
  - [Version 10 API Guide & Schemas](versions/v10-api-guide.md)
  - [Version 9 API Guide & Canvas](versions/v09-api-guide.md)
  - [Version 8 API Guide & Document Refactor](versions/v08-api-guide.md)
- [Development Guides](guides/)
  - [Creating Game Systems](guides/creating-systems.md)
  - [Creating Modules](guides/creating-modules.md)
  - [Macros, Tables & Compendiums](guides/macros-and-tables.md)
  - [Active Effects & Statuses](guides/active-effects.md)
  - [Troubleshooting & Conflict Isolation](guides/troubleshooting.md)
- [Policies & Governance](policies/)
  - [Limited License Agreement](policies/license.md)
  - [AI Policy](policies/ai-policy.md)
  - [Branding Guidelines](policies/branding.md)
  - [Privacy Policy](policies/privacy-policy.md)
- [Quick Cheatsheet](cheatsheet.md)
- [Canonical Glossary](glossary.md)
- [Architectural Patterns](patterns.md)

---

## 🇧🇷 Português (Brasil)

### 📌 Missão Central e Mandatos do Agente de IA

O **Master of Foundry VTT** é a base de conhecimento e guia de desenvolvimento definitiva para o **Foundry Virtual Tabletop**, cobrindo a arquitetura do cliente/servidor, evolução das APIs da v8 até a v14, políticas de uso, criação de sistemas, módulos, macros e integração de sistemas de RPG.

---

### 🚨 Diretrizes Obrigatórias para o Agente de IA

Sempre que o Agente for solicitado a realizar qualquer tarefa relacionada ao Foundry VTT, ele **DEVE OBRIGATORIAMENTE** seguir estes cinco protocolos:

#### 1. Consulta Obrigatória de Versão
Antes de escrever código, macros, esquemas de dados (DataModel) ou orientar sobre métodos da API:
- **O Agente DEVE PERGUNTAR ao desenvolvedor/operador qual versão do Foundry VTT está sendo utilizada** (ex: v12, v11, v13, v10, v9 ou v8), a menos que já tenha sido explicitado no prompt.
- **Motivo:** As APIs mudam profundamente entre versões (ex: migração de documentos na `0.8.x`, introdução de `DataModel` na `v10`, `ApplicationV2` na `v12`). Misturar sintaxes gera erros silenciosos.

#### 2. Auditoria de Licenças e Políticas do Foundry
- O Agente deve auditar se a funcionalidade solicitada cumpre o **Contrato de Licença Limitada**, a **Política de IA** e as **Diretrizes de Marca (Branding)** do Foundry VTT.
- **Regra Crucial:** Nunca redistribuir código-fonte do core, conteúdos proprietários de pacotes pagos ou usar marcas registradas indevidamente. Caso haja risco de violação, o Agente **DEVE ALERTAR o desenvolvedor imediatamente**.

#### 3. Protocolo de Ingestão de Livros e Repositórios de Sistemas de RPG
Ao desenvolver ou prestar suporte para sistemas de RPG (ex: **Pathfinder 2e, D&D 5e, Savage Worlds, GURPS, Fate, Tormenta20**):
1. O Agente **DEVE solicitar ao desenvolvedor:**
   - Os livros/manuais em PDF de referência.
   - O link do repositório (GitHub/GitLab) do sistema do Foundry.
   - A versão exata do sistema instalada.
2. O Agente converterá/ingerirá esses materiais em Markdown modular estruturado para servir de base perene de consulta.

#### 4. Auditoria de Módulos Ativos e Resolução de Erros
Ao investigar erros no console, exceções ou conflitos visuais:
- O Agente **DEVE solicitar a lista completa de módulos ativos e suas respectivas versões**.
- Isolar incompatibilidades orientando testes em modo seguro e inspecionando ganchos (`libWrapper`).

#### 5. Protocolo de Auto-Correção e Permissão
- Se houver falhas de execução, diagnosticar e auto-corrigir iterativamente.
- Solicitar permissão explícita ao desenvolvedor caso haja necessidade de instalar pacotes extras ou ferramentas de sistema.
