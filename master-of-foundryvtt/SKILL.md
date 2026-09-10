---
name: master-of-foundryvtt
description: Master development, administration, and automation suite for Foundry Virtual Tabletop (v8, v9, v10, v11, v12, v13, v14) by GM Charles Corrêa. Ingests Knowledge Base, Release Notes, Policies (Branding, AI, License, Privacy), API documentation across all versions, MCP integration (ninjos-foundry-mcp, foundryvtt-mcp, foundry-vtt-mcp), and 60+ famous RPG system architectures (PF2e, D&D 5e/3.5e, WoD20/5E, SWADE, Tormenta20, YZE, GURPS, Cyberpunk RED, CoC7, CSB). Use when developing systems/modules, troubleshooting errors, configuring MCP bridges, or scripting Foundry VTT via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama.
---

# Master of Foundry VTT 🎲⚡
> *by GM Charles Corrêa*

---

## 🇺🇸 English

### 📌 Core Mission & Agent Mandates

**Master of Foundry VTT** is the definitive, multi-version knowledge base, MCP bridge, and development companion for **Foundry Virtual Tabletop**. It covers client/server architecture, API evolutions from v8 through v14, policies, system and module creation, macro scripting, Model Context Protocol (MCP) integrations, and 60+ RPG system architectures.

---

### 🚨 Mandatory Directives for AI Agents

Whenever an AI Agent is tasked with any Foundry VTT assignment, it **MUST ALWAYS** follow these core protocols:

#### 1. Version Inquiry Mandate (Gatekeeper)
Before writing any code, script macro, DataModel, or advising on APIs:
- **The Agent MUST ASK the developer/operator which Foundry VTT version they are targeting** (e.g., v12, v11, v13, v10, v9, or v8), unless explicitly stated in the prompt.
- **Rationale:** API contracts change dramatically between versions (e.g., `0.8.x` document migration, `v10` DataModel schema system, `v12` ApplicationV2 migration). Mixing versions causes silent failures.

#### 2. License & Policy Compliance Verification
- The Agent must audit every planned feature against Foundry VTT's **Limited License Agreement**, **AI Policy**, and **Branding Guidelines**.
- **Crucial Rule:** Never redistribute core Foundry software, proprietary premium compendium content, or trademarked logos without authorization. If a requested feature risks violating policies, the Agent **MUST WARN the developer immediately**.

#### 3. MCP Installation, Configuration & Credential Request Protocol
When installing or configuring Model Context Protocol (MCP) servers ([`ninjos-foundry-mcp`](https://github.com/Niclasp1501/ninjos-foundry-mcp), [`foundryvtt-mcp`](https://github.com/laurigates/foundryvtt-mcp), [`foundry-vtt-mcp`](https://github.com/adambdooley/foundry-vtt-mcp)):
1. **Explain the benefits clearly:** Explain how the MCP server empowers the AI to read live world data, inspect DataModels, run safe macro tests, and diagnose errors in real time.
2. **Interactive Credential & Path Checklist:** Ask the developer for required connection details if not autodetected:
   - Local Foundry User Data Path (e.g., `AppData/Local/FoundryVTT/Data` or custom directory).
   - Foundry VTT instance URL and Port (e.g., `http://localhost:30000`).
   - Admin Access Key or World Password / API key.
   - Active World ID and target user role.
3. **Permission Gate:** Always explain what packages (`npm`, `npx`, Node.js) or companion modules will be installed and obtain user approval before executing modifying setup commands.

#### 4. RPG System Ingestion & Multi-System Knowledge Base
When developing or troubleshooting for specific RPG systems (e.g., **Pathfinder 2e, D&D 5e, Savage Worlds, WoD20, Tormenta20, YZE, GURPS, CoC7, Cyberpunk RED**):
1. Consult the pre-indexed knowledge base under [`systems/`](systems/).
2. **Dynamic System Discovery:** If the requested RPG system is **not** yet cataloged in the local knowledge base, the Agent **MUST automatically search [https://foundryvtt.com/packages/systems](https://foundryvtt.com/packages/systems)** to locate the official package entry, manifest URL, compatibility tags, and the source code repository (GitHub, GitLab, etc.).
3. Ingest the system's data model, template schema, and sheet architecture into context, and ask the developer for custom rulebook PDFs and the exact installed version.

#### 5. Active Module Audit & Troubleshooting Protocol
When diagnosing errors, console exceptions, or unexpected UI behavior:
- The Agent **MUST ask the developer for the list of currently active modules and their versions**.
- Isolate conflicts by advising binary search testing (`Find the Culprit` / safe mode) and checking `libWrapper` hooks.

#### 6. Autonomous Error Recovery & Permission Protocol
- If installation or execution fails, diagnose root causes and self-correct iteratively.
- For extra system packages or external tools, request explicit user permission before proceeding.

#### 7. Monthly Knowledge Base Refresh Protocol
- The Knowledge Base, release notes, and policies should be refreshed periodically (e.g., once a month) using the built-in update script `scripts/update_foundry_docs.py` or scheduled via `/schedule` to ensure API methods, deprecations, and system links stay 100% current.

---

### 📚 Structure & Fast-Path Navigation

- [Model Context Protocol (MCP) Guide](mcp/README.md)
  - [MCP Integration & Configuration](mcp/README.md)
- [Famous RPG Systems Knowledge Base](systems/README.md)
  - [Fantasy, D20 & Duality Dice (D&D 5e, PF2e, Daggerheart, T20, OD2e, Draw Steel)](systems/01-d20-and-fantasy.md)
  - [Storyteller & World of Darkness (WoD20, V5, WoD5E, KULT)](systems/02-storyteller-and-world-of-darkness.md)
  - [Investigative & Cosmic Horror (CoC 7e, Delta Green, GUMSHOE)](systems/03-investigative-and-horror.md)
  - [Year Zero Engine (Alien, Blade Runner, Vaesen, Twilight 2000, Dragonbane)](systems/04-year-zero-engine.md)
  - [Sci-Fi, Cyberpunk & Pulp (Cyberpunk RED/2020, Shadowrun, Cosmere)](systems/05-pulp-scifi-and-cyberpunk.md)
  - [Narrative, PbtA & FitD (Blades in the Dark, City of Mist, Fate, Perigos & Princesas)](systems/06-narrative-and-pbta-fitd.md)
  - [Generic & Rules-Light (GURPS 4e, SWADE, CSB, Worldbuilding, 3D&T, ABEA)](systems/07-generic-and-rules-light.md)
- [API Versions Guide](versions/)
  - [Version 14 API Guide](versions/v14-api-guide.md)
  - [Version 13 API Guide](versions/v13-api-guide.md)
  - [Version 12 API Guide & ApplicationV2](versions/v12-api-guide.md)
  - [Version 11 API Guide & DataModels](versions/v11-api-guide.md)
  - [Version 10 API Guide & Schemas](versions/v10-api-guide.md)
  - [Version 9 API Guide & Canvas](versions/v09-api-guide.md)
  - [Version 8 API Guide & Document Refactor](versions/v08-api-guide.md)
- [Knowledge Base & Operations](kb/)
  - [Getting Started & Hosting](kb/01-getting-started-and-hosting.md)
  - [Scenes, Lighting & Vision](kb/02-scenes-lighting-and-vision.md)
  - [Actors, Items & Tokens](kb/03-actors-items-and-tokens.md)
  - [Dice Rolling & Chat](kb/04-dice-rolling-and-chat.md)
  - [Audio, Video & WebRTC](kb/05-audio-video-and-webrtc.md)
  - [Compendiums & World Data](kb/06-compendiums-and-world-data.md)
- [Development Guides](guides/)
  - [CLI Tools & Compendium Automation (`@foundryvtt/foundryvtt-cli` & `fvtt-world-cli`)](guides/cli-tools.md)
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

---
---

## 🇧🇷 Português (Brasil)

### 📌 Missão Central e Mandatos do Agente de IA

O **Master of Foundry VTT** é a base de conhecimento, ponte MCP e guia de desenvolvimento definitivo para o **Foundry Virtual Tabletop**, cobrindo a arquitetura do cliente/servidor, evolução das APIs da v8 até a v14, integração de servidores MCP, políticas de uso e arquitetura de mais de 60 sistemas de RPG.

---

### 🚨 Diretrizes Obrigatórias para o Agente de IA

Sempre que o Agente for solicitado a realizar qualquer tarefa relacionada ao Foundry VTT, ele **DEVE OBRIGATORIAMENTE** seguir estes protocolos:

#### 1. Consulta Obrigatória de Versão (Portão de Entrada)
Antes de escrever código, macros, esquemas de dados (DataModel) ou orientar sobre métodos da API:
- **O Agente DEVE PERGUNTAR ao desenvolvedor/operador qual versão do Foundry VTT está sendo utilizada** (ex: v12, v11, v13, v10, v9 ou v8), a menos que já tenha sido explicitado no prompt.
- **Motivo:** As APIs mudam profundamente entre versões (ex: migração de documentos na `0.8.x`, introdução de `DataModel` na `v10`, `ApplicationV2` na `v12`). Misturar sintaxes gera falhas silenciosas.

#### 2. Auditoria de Licenças e Políticas do Foundry
- O Agente deve auditar se a funcionalidade solicitada cumpre o **Contrato de Licença Limitada**, a **Política de IA** e as **Diretrizes de Marca (Branding)** do Foundry VTT.
- **Regra Crucial:** Nunca redistribuir código-fonte do core, conteúdos proprietários de pacotes pagos ou usar marcas registradas indevidamente. Caso haja risco, o Agente **DEVE ALERTAR o desenvolvedor imediatamente**.

#### 3. Protocolo de Instalação de MCPs e Solicitação de Credenciais
Ao configurar servidores MCP ([`ninjos-foundry-mcp`](https://github.com/Niclasp1501/ninjos-foundry-mcp), [`foundryvtt-mcp`](https://github.com/laurigates/foundryvtt-mcp), [`foundry-vtt-mcp`](https://github.com/adambdooley/foundry-vtt-mcp)):
1. **Explicar os motivos e vantagens:** Explicar detalhadamente como o MCP permite ao agente ler dados reais do mundo, testar macros, inspecionar esquemas e resolver bugs em tempo real.
2. **Solicitar dados necessários ao desenvolvedor:**
   - Caminho local da pasta de dados (`Data/` / `User Data Path`).
   - URL e porta da instância do Foundry (ex: `http://localhost:30000`).
   - Chave de administração (`adminPassword`) ou senha de usuário/mundo.
   - Nome do mundo ativo e papel de usuário (GM / Assistente).
3. **Solicitar autorização prévia:** Explicar os comandos e pacotes que serão instalados e pedir confirmação antes de executar comandos de instalação.

#### 4. Protocolo de Ingestão e Conhecimento de Sistemas de RPG
Ao desenvolver ou prestar suporte para sistemas de RPG:
1. Consultar a base de conhecimento de mais de 60 sistemas catalogados em [`systems/`](systems/).
2. **Descoberta Dinâmica de Sistemas Não Catalogados:** Se o sistema solicitado **não** constar na base local da skill, o Agente **DEVE OBRIGATORIAMENTE buscar em [https://foundryvtt.com/packages/systems](https://foundryvtt.com/packages/systems)** a página do pacote, a URL do manifesto (`system.json`), as versões compatíveis do Foundry e o repositório oficial do código-fonte (GitHub, GitLab, etc.).
3. Ingerir a arquitetura de esquemas, fichas e templates do repositório localizado e solicitar ao desenvolvedor os manuais/PDFs de regras específicas e a versão instalada.

#### 5. Auditoria de Módulos Ativos e Resolução de Erros
Ao investigar erros no console, exceções ou conflitos visuais:
- O Agente **DEVE solicitar a lista completa de módulos ativos e suas respectivas versões**.
- Isolar incompatibilidades orientando testes em modo seguro e inspecionando ganchos (`libWrapper`).

#### 6. Protocolo de Auto-Correção e Permissão
- Se houver falhas de execução, diagnosticar e auto-corrigir iterativamente.
- Solicitar permissão explícita ao desenvolvedor caso haja necessidade de instalar pacotes extras de sistema.

#### 7. Protocolo de Atualização Mensal da Base de Conhecimento
- A base de conhecimento, notas de lançamento e políticas do Foundry VTT devem ser atualizadas periodicamente (aproximadamente 1 vez ao mês) executando o script `scripts/update_foundry_docs.py` ou via agendamento com `/schedule` para garantir que novos métodos da API, migrações e sistemas permaneçam sempre em dia.

---

### 📚 Estrutura e Navegação Rápida

- [Guia de Servidores MCP (Model Context Protocol)](mcp/README.md)
  - [Integração e Configuração dos MCPs](mcp/README.md)
- [Base de Conhecimento dos Sistemas de RPG Famosos](systems/README.md)
  - [Fantasia Heroica, D20 & Duality Dice (D&D 5e, PF2e, Daggerheart, T20, OD2e, Draw Steel)](systems/01-d20-and-fantasy.md)
  - [Storyteller & Mundo das Trevas (WoD20, V5, WoD5E, KULT)](systems/02-storyteller-and-world-of-darkness.md)
  - [Investigação & Horror Cósmico (CoC 7e, Delta Green, GUMSHOE)](systems/03-investigative-and-horror.md)
  - [Year Zero Engine (Alien, Blade Runner, Vaesen, Twilight 2000, Dragonbane)](systems/04-year-zero-engine.md)
  - [Sci-Fi, Cyberpunk & Pulp (Cyberpunk RED/2020, Shadowrun, Cosmere)](systems/05-pulp-scifi-and-cyberpunk.md)
  - [Narrativos, PbtA & FitD (Blades in the Dark, City of Mist, Fate, Perigos & Princesas)](systems/06-narrative-and-pbta-fitd.md)
  - [Genéricos & Regras Customizadas (GURPS 4e, SWADE, CSB, Worldbuilding, 3D&T, ABEA)](systems/07-generic-and-rules-light.md)
- [Guias das Versões da API](versions/)
  - [Guia da API Versão 14](versions/v14-api-guide.md)
  - [Guia da API Versão 13](versions/v13-api-guide.md)
  - [Guia da API Versão 12 & ApplicationV2](versions/v12-api-guide.md)
  - [Guia da API Versão 11 & DataModels](versions/v11-api-guide.md)
  - [Guia da API Versão 10 & Schemas](versions/v10-api-guide.md)
  - [Guia da API Versão 9 & Canvas](versions/v09-api-guide.md)
  - [Guia da API Versão 8 & Refatoração de Documentos](versions/v08-api-guide.md)
- [Base de Conhecimento e Operações (KB)](kb/)
  - [Primeiros Passos e Hospedagem](kb/01-getting-started-and-hosting.md)
  - [Cenas, Iluminação e Visão](kb/02-scenes-lighting-and-vision.md)
  - [Atores, Itens e Tokens](kb/03-actors-items-and-tokens.md)
  - [Rolagens de Dados e Chat](kb/04-dice-rolling-and-chat.md)
  - [Áudio, Vídeo e WebRTC](kb/05-audio-video-and-webrtc.md)
  - [Compêndios e Dados do Mundo](kb/06-compendiums-and-world-data.md)
- [Guias de Desenvolvimento](guides/)
  - [Ferramentas CLI & Automação de Compêndios (`@foundryvtt/foundryvtt-cli` e `fvtt-world-cli`)](guides/cli-tools.md)
  - [Criando Sistemas de Jogo](guides/creating-systems.md)
  - [Criando Módulos](guides/creating-modules.md)
  - [Macros, Tabelas e Compêndios](guides/macros-and-tables.md)
  - [Efeitos Ativos e Condições](guides/active-effects.md)
  - [Resolução de Erros e Isolamento de Conflitos](guides/troubleshooting.md)
- [Políticas e Governança](policies/)
  - [Contrato de Licença Limitada](policies/license.md)
  - [Política de Inteligência Artificial](policies/ai-policy.md)
  - [Diretrizes de Marca (Branding)](policies/branding.md)
  - [Política de Privacidade](policies/privacy-policy.md)

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)
