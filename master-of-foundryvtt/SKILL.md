---
name: master-of-foundryvtt
description: Master development, administration, and automation suite for Foundry Virtual Tabletop (v8, v9, v10, v11, v12, v13, v14.369 Stable) by GM Charles Corrêa. Ingests Knowledge Base, Release Notes, Policies (Branding, AI, License, Privacy), API documentation across all versions, MCP integration (ninjos-foundry-mcp, foundryvtt-mcp, foundry-vtt-mcp), and 60+ famous RPG system architectures (PF2e, D&D 5e/3.5e, WoD20/5E, SWADE, Tormenta20, YZE, GURPS, Cyberpunk RED, CoC7, CSB). Use when developing systems/modules, troubleshooting errors, configuring MCP bridges, or scripting Foundry VTT via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama.
---

# Master of Foundry VTT 🎲⚡
> *by GM Charles Corrêa*
> **Current up to Foundry VTT v14.369 Stable**

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
- **Crucial v14+ Rule:** When developing for v14 or newer, you **MUST** use `foundry.applications.api.ApplicationV2` (replacing the old `Application`), `foundry.abstract.DataModel` and `TypeDataModel` for strict data structuring in Documents, the new Game Canvas hierarchy (e.g., `CanvasGroupMixin`, `PrimaryCanvasGroup`), and current ESM methods loaded via `client/client.mjs`. Do not use outdated patterns that trigger deprecation notices.
- **Template.json Deprecation (v14+):** The `template.json` file is completely deprecated. For new systems (or migrating existing ones), you **MUST** declare `documentTypes` inside `system.json` and map them to Javascript `TypeDataModel` classes registered in `CONFIG.Actor.dataModels` and `CONFIG.Item.dataModels`. Never use `template.json` for new projects. This also applies to modules injecting new document sub-types.
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
2. **Dynamic System Discovery:** If the requested RPG system is **not** yet cataloged in the local knowledge base, the Agent **MUST automatically search [https://foundryvtt.com/packages/systems?page=1](https://foundryvtt.com/packages/systems?page=1)** (checking paginated listings `?page=2`, `?page=3`, etc., as needed) to locate the official package entry, manifest URL, compatibility tags, and the source code repository (GitHub, GitLab, Gitea, etc.).
3. Ingest the system's data model, template schema, and sheet architecture into context, and ask the developer for custom rulebook PDFs and the exact installed version.

#### 5. Module Recommendation, Premium Content & Troubleshooting Protocol
- **Module Recommendations for Systems:** Whenever the developer or user asks for module recommendations to enhance a specific RPG system (UI, automation, audio, tokens, sheets, compendiums):
  - The Agent **MUST consult the official Foundry VTT Modules Directory with pagination support**: [**https://foundryvtt.com/packages/modules?page=1**](https://foundryvtt.com/packages/modules?page=1) (iterating through `?page=2`, `?page=3`, etc., as needed).
  - Note that while most community modules are cataloged there, some specialized or premium modules (e.g., Patreon-exclusive, developer stores, external GitHub packages) might not appear in this listing. Highlight whether a module is officially listed, open-source, or third-party/paid.
- **Premium / Commercial Content & Official Store Search:** If the developer is willing to invest or asks for official/premium modules, adventures, rules compendiums, or assets:
  - The Agent **MUST search the official Foundry VTT Store**: [**https://www.foundryvtt.store/search?q=<QUERY>**](https://www.foundryvtt.store/search?q=Savage+Worlds) replacing the query string with the system name or keywords (e.g., `?q=Savage+Worlds`, `?q=dnd`, `?q=pathfinder`, `?q=warhammer`, `?q=alien`) to find and recommend official commercial packages and license keys.
- **Active Module Audit & Diagnostics:** When diagnosing errors, console exceptions, or unexpected UI behavior:
  - The Agent **MUST ask the developer for the list of currently active modules and their versions**.
  - Isolate conflicts by advising binary search testing (`Find the Culprit` / safe mode) and checking `libWrapper` hooks.

#### 6. Autonomous Error Recovery & Permission Protocol
- If installation or execution fails, diagnose root causes and self-correct iteratively.
- For extra system packages or external tools, request explicit user permission before proceeding.

#### 7. Monthly Knowledge Base Refresh Protocol
- The Knowledge Base, release notes, and policies should be refreshed periodically (e.g., once a month) using the built-in update script `scripts/update_foundry_docs.py` or scheduled via `/schedule` to ensure API methods, deprecations, and system links stay 100% current.

#### 8. Interactive Clarification, Content Ingestion & Transparent Scoping Protocol (CRITICAL)
Whenever the user or Game Master asks to create or configure ANY game asset or development unit, including:
- **Scenes and Maps:** Dimensions, lighting, walls, doors, darkness levels, weather, and linked soundtracks.
- **Walls and Lighting:** Occlusion types (sight, movement, sound), secret doors, light colors, and animations.
- **Character, NPC, and Creature Sheets:** Attributes, skills, embedded items, edges, hindrances, armor, damage, and lore.
- **Items and Equipment:** Detailed mechanics, cost, weight, damage, range, traits, and active effects.
- **Journals, Handouts, and Notes:** Narrative content, mysteries, player permissions, images, and formatting.
- **Rollable Tables, Decks, and Cards:** Dice formulas, weighted results, suits, faces, and draw/discard rules.
- **Compendiums, Modules, and Systems:** Architectural scope, dependencies, target Foundry version, and rulebook alignment.

**The Agent MUST STRICTLY follow these rules:**
1. **Never Assume or Hallucinate Incomplete Data:** If the request lacks mechanics, specific book references, or aesthetic intent, **do NOT blindly guess or create half-empty placeholder assets**.
2. **Mandatory Clarification Gate:** The Agent **MUST question the user**, actively asking for:
   - Specific rulebook edition, supplement, or setting source (e.g., SWADE Core, Companions, D&D 5e PHB/MM, PF2e Remaster, Tormenta20 JdA).
   - Character tier, level, monster threat rating, or exact tactical role (minion, boss, wild card).
   - Map theme, intended scale (grid square size in meters/feet), lighting atmosphere, and points of interest.
   - Any homebrew tweaks, existing module integrations, or specific lore nuances.
3. **Transparent & Explanatory Plan:** Before generating or writing files, explain clearly what structure is going to be built, why it fits the system's schema, and how it will appear in the world. Ask the user for confirmation or adjustments.

#### 9. Mandatory Icon & Asset Selection Protocol for Items, Abilities & Powers (CRITICAL)
Whenever asked to create or configure any **Item**, **Ability / Talent**, **Power / Spell**, **Weapon**, **Armor**, **Shield**, **Natural Weapon** (claws, bites, horns, tentacles, etc.), **Accessory** (boots, gloves, rings, cloaks), **Consumable** (potions, medicines, remedies, scrolls), or any other game document:
1. **First Priority — Core Foundry VTT Standard Icons:**
   - Search and prioritize using the official default Foundry VTT icons located at:
     `%url-foundry-vtt%/App/resources/app/public/icons/` (serving web paths like `icons/...`, e.g., `icons/weapons/...`, `icons/equipment/...`, `icons/magic/...`, `icons/consumables/...`, `icons/commodities/...`, `icons/tools/...`, `icons/skills/...`).
2. **Second Priority — System Specific Icons Directory:**
   - If a suitable core icon is not found, verify and explore the active game system folder for custom icons (e.g., `systems/<system-id>/icons/` or system assets directory).
3. **Third Priority / Fallback — Generic Core SVG Icons:**
   - If no specific icon exists in core or the system directory, use a generic fallback SVG icon from:
     `%url-foundry-vtt%/App/resources/app/public/icons/svg/` (serving web paths like `icons/svg/item-bag.svg`, `icons/svg/sword.svg`, `icons/svg/shield.svg`, `icons/svg/aura.svg`, `icons/svg/d20-black.svg`, `icons/svg/mystery-man.svg`).

#### 10. Reverse Engineering (REA) & Persistent Memory Protocol (CRITICAL)
Tools: [`rea-agents`](https://github.com/morluto/rea) (REA MCP/CLI) and the guide [`rea-engenharia-reversa`](https://github.com/inematds/rea-engenharia-reversa). Full workflow: [guides/reverse-engineering.md](guides/reverse-engineering.md).
- **Use REA** to study Foundry core, systems and modules (real APIs, hooks, DataModels, sheets) before building, so new code matches the target precisely.
- **Trigger:** ANY request to generate a module for a system/Foundry, reverse engineer something, **create a new system, adjust/fix a system, recreate or rebuild from scratch**.
- **Before work:** read `memory/learnings.md` and `memory/<target>.md`. **After work (even on failure):** save findings, pitfalls, patterns and improvements there using the template in the guide (verified facts only, no secrets/licensed content), then promote generalizable lessons into `guides/`/`systems/`.

#### 11. Auto-Install, Reinstallation & Update Protocol (CRITICAL)
When the user asks to install, update, or reinstall this skill (or when a required tool is missing):
1. **Detect Existing Installation (Local Workspace or Global Roots):**
   - The Agent **MUST check if the skill is already present** either locally in the current project (e.g. `skills/master-of-foundryvtt` or root) or globally in agent configuration directories:
     - Windows/Linux: `~/.gemini/config/skills/master-of-foundryvtt`, `~/.claude/skills/master-of-foundryvtt`, `~/.agents/skills/master-of-foundryvtt`.
2. **Alert Developer & Overwrite with Latest Features:**
   - If an existing installation is found and the user requested an update/reinstall:
     - **The Agent MUST alert the user:** *"Identifiquei que a skill `master-of-foundryvtt` já estava instalada no ambiente (local/global). Estou atualizando e sobrescrevendo os arquivos com a versão mais recente e todos os novos recursos (motores de regras, reverse engineering do v14, MCPs atualizados)."*
     - Overwrite/update the target directory files cleanly (via junction/symlink or files copy) ensuring existing configuration and memories (`memory/`) remain safe while all knowledge bases (`kb/`), guides, systems, and scripts are upgraded to the latest version.
3. **Toolchain & Dependency Check:**
   - Inform the developer of the full toolchain required: Node.js + npm, Git, Python 3.8+, REA (`rea-agents`), `@foundryvtt/foundryvtt-cli`, `fvtt-world-cli`, the Foundry MCPs (`ninjos-foundry-mcp`, `foundryvtt-mcp`, `foundry-vtt-mcp`, native `master-of-foundryvtt`) and optional decompilers.
4. **Single-Permission Execution:**
   - Ask for authorization once. If confirmed, install and configure everything (`python scripts/setup_dev_env.py --yes`, MCP registrations, `npx rea-agents setup`, `fvtt configure`), self-correcting failures.
   - If denied, continue with limited capabilities and explicitly state what is missing.


### 📚 Structure & Fast-Path Navigation

- [Model Context Protocol (MCP) Guide](mcp/README.md)
  - [MCP Integration & Configuration](mcp/README.md)
  - [Native MCP Server Installation Manual (`INSTALLATION.md`)](mcp/INSTALLATION.md)
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
  - [SSL, HTTPS & Let's Encrypt](kb/07-ssl-and-https.md)
  - [Core Reverse Engineering & v14 API Architecture](kb/08-core-reverse-engineering-v14.md)
  - [RPG Engines, Game Design & Mechanics Directory](kb/09-rpg-engines-and-mechanics.md)
- [Development Guides](guides/)
  - [CLI Tools & Compendium Automation (`@foundryvtt/foundryvtt-cli` & `fvtt-world-cli`)](guides/cli-tools.md)
  - [Creating Game Systems](guides/creating-systems.md)
  - [Creating Modules](guides/creating-modules.md)
  - [AI & LLM Integration Guide (Integrate AI, Phil's Assistant, AI Actors)](guides/ai-and-llm-integration.md)
  - [Development Skills Matrix & Engineering Domains](guides/development-skills-matrix.md)
  - [Macros, Tables & Compendiums](guides/macros-and-tables.md)
  - [Automated Traps & Triggers (Sequencer & Monk's Active Tile Triggers)](guides/automated-traps-and-triggers.md)
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
- **Regra Crucial para v14+:** Ao desenvolver para v14 ou superior, você **DEVE OBRIGATORIAMENTE** usar `foundry.applications.api.ApplicationV2` (nova arquitetura de UI que substitui o antigo `Application`), `foundry.abstract.DataModel` e `TypeDataModel` para estruturação forte de dados em Documentos, a nova hierarquia do Game Canvas (ex: `CanvasGroupMixin`, `PrimaryCanvasGroup`) e os métodos ESM atuais carregados via `client/client.mjs`. Não utilize padrões obsoletos que geram alertas de descontinuação (deprecation notices).
- **Descontinuação do Template.json (v14+):** O arquivo `template.json` está totalmente obsoleto e será removido. Em sistemas novos (ou migrações), você **DEVE** declarar a propriedade `documentTypes` diretamente no `system.json` e atrelar os tipos a classes JavaScript `TypeDataModel` registradas em `CONFIG.Actor.dataModels` e `CONFIG.Item.dataModels`. Nunca recrie um `template.json`. Esta regra também vale para Módulos que injetam novos subtipos de fichas ou documentos.
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
2. **Descoberta Dinâmica de Sistemas Não Catalogados:** Se o sistema solicitado **não** constar na base local da skill, o Agente **DEVE OBRIGATORIAMENTE buscar no diretório oficial com suporte a paginação [https://foundryvtt.com/packages/systems?page=1](https://foundryvtt.com/packages/systems?page=1)** (consultando as páginas subsequentes `?page=2`, `?page=3`, etc., conforme necessário) a página do pacote, a URL do manifesto (`system.json`), as versões compatíveis do Foundry e o repositório oficial do código-fonte (GitHub, GitLab, Gitea, etc.).
3. Ingerir a arquitetura de esquemas, fichas e templates do repositório localizado utilizando as ferramentas web de inspeção e engenharia reversa (detalhadas na seção [Extração de Dados de Repositórios](#8-extração-de-dados-de-repositórios-e-engenharia-reversa)), além de solicitar ao desenvolvedor os manuais/PDFs de regras específicas e a versão instalada.

#### 5. Protocolo de Recomendação de Módulos, Conteúdo Premium e Resolução de Erros
- **Recomendação de Módulos para Sistemas:** Sempre que o desenvolvedor ou usuário pedir recomendação de módulos para usar com determinado sistema (automação, combate, fichas, interface, iluminação, áudio, compêndios):
  - O Agente **DEVE OBRIGATORIAMENTE consultar o Diretório Oficial de Módulos do Foundry VTT com suporte a paginação**: [**https://foundryvtt.com/packages/modules?page=1**](https://foundryvtt.com/packages/modules?page=1) (iterando pelas páginas subsequentes `?page=2`, `?page=3`, etc., conforme necessário).
  - É importante lembrar e esclarecer ao desenvolvedor que, embora a maioria dos módulos comunitários conste nesse diretório oficial, existem módulos específicos, premium ou pagos (ex: Patreon, lojas de criadores, repositórios externos do GitHub) que podem não estar listados nessa página. O Agente deve deixar claro a origem (oficial, comunitário ou comercial/externo).
- **Conteúdo Comercial & Loja Oficial (Investimento do Desenvolvedor):** Caso o desenvolvedor queira investir dinheiro ou busque suplementos oficiais, compêndios de regras completos, aventuras e módulos premium licenciados:
  - O Agente **DEVE OBRIGATORIAMENTE pesquisar na Loja Oficial do Foundry VTT**: [**https://www.foundryvtt.store/search?q=<PALAVRA_CHAVE>**](https://www.foundryvtt.store/search?q=Savage+Worlds) substituindo o parâmetro de busca pelo nome do sistema ou produto desejado (ex: `?q=Savage+Worlds`, `?q=dnd`, `?q=pathfinder`, `?q=warhammer`, `?q=alien`, `?q=cthulhu`), recomendando os pacotes e conteúdos oficiais ideais para a demanda.
- **Auditoria de Módulos Ativos e Resolução de Erros:** Ao investigar erros no console, exceções ou conflitos visuais:
  - O Agente **DEVE solicitar a lista completa de módulos ativos e suas respectivas versões**.
  - Isolar incompatibilidades orientando testes em modo seguro e inspecionando ganchos (`libWrapper`).

#### 6. Protocolo de Auto-Correção e Permissão
- Se houver falhas de execução, diagnosticar e auto-corrigir iterativamente.
- Solicitar permissão explícita ao desenvolvedor caso haja necessidade de instalar pacotes extras de sistema.

#### 7. Protocolo de Atualização Mensal da Base de Conhecimento
- A base de conhecimento, notas de lançamento e políticas do Foundry VTT devem ser atualizadas periodicamente (aproximadamente 1 vez ao mês) executando o script `scripts/update_foundry_docs.py` ou via agendamento com `/schedule` para garantir que novos métodos da API, migrações e sistemas permaneçam sempre em dia.

#### 8. Protocolo de Esclarecimento Interativo, Ingestão de Livros e Escopo Transparente (CRÍTICO)
Sempre que o usuário ou Mestre solicitar a criação ou configuração de QUALQUER recurso de jogo, incluindo:
- **Cenas e Mapas:** Dimensões, iluminação, paredes, portas, níveis de escuridão, clima e trilha sonora associada.
- **Paredes e Iluminação:** Tipo de bloqueio (visão, movimento, som), portas secretas, cor e animação de tochas/luzes.
- **Fichas de Personagem, NPCs e Criaturas:** Atributos, perícias, itens embutidos, vantagens, fraquezas, armaduras, dano e biografia.
- **Itens e Equipamentos:** Mecânica detalhada, custo, peso, dano, alcance, propriedades e efeitos ativos.
- **Diários, Handouts e Documentos:** Conteúdo narrativo, mistérios, permissões de jogadores, imagens e formatação.
- **Tabelas Roláveis, Baralhos e Cartas:** Fórmulas de dados, resultados ponderados, naipes, artes e regras de compra/descarte.
- **Compêndios, Módulos e Sistemas:** Escopo da arquitetura, dependências, versão do Foundry e compatibilidade com livros oficiais.

**O Agente DEVE OBRIGATORIAMENTE seguir estas regras:**
1. **Nunca Supor ou Alucinar Dados Incompletos:** Se o pedido não contiver mecânicas completas, referências de livros ou intenção estética, **NÃO tente adivinhar nem crie recursos vazios/placeholders**.
2. **Portão Obrigatório de Questionamento:** O Agente **DEVE questionar ativamente o usuário**, solicitando:
   - Livro de regras oficial, suplemento ou cenário base (ex: SWADE Básico, Compêndios, D&D 5e PHB/MM, PF2e Remaster, Tormenta20 JdA).
   - Estágio do personagem, nível, ND/CR do monstro ou papel tático exato (lacaio, chefe, carta selvagem).
   - Tema do mapa, escala pretendida (tamanho do quadrado em metros/pés), atmosfera de iluminação e pontos de interesse.
   - Modificações caseiras (homebrews), módulos integrados existentes ou detalhes de ambientação.
3. **Plano Transparente e Explicativo:** Antes de gerar arquivos ou salvar no mundo, explique claramente qual estrutura será montada, por que ela atende ao esquema do sistema e como ficará no mundo. Peça confirmação ou ajustes ao usuário.

#### 9. Protocolo Obrigatório de Seleção de Ícones e Assets para Itens, Habilidades e Poderes (CRÍTICO)
Sempre que for solicitado criar ou configurar qualquer **Item**, **Habilidade**, **Poder**, **Magia**, **Arma**, **Armadura**, **Escudo**, **Arma Natural** (garras, presas, mordidas, chifres, caudas, tentáculos), **Acessório** (botas, luvas, anéis, capas), **Consumível** (poções, remédios, elixires, pergaminhos) ou qualquer outro documento de jogo:
1. **Primeira Prioridade — Ícones Padrão do Core do Foundry VTT:**
   - Busque e priorize sempre os ícones padrão oficiais do Foundry VTT localizados em:
     `%url-foundry-vtt%/App/resources/app/public/icons/` (servidos em caminhos web relativos como `icons/...`, ex: `icons/weapons/...`, `icons/equipment/...`, `icons/magic/...`, `icons/consumables/...`, `icons/commodities/...`, `icons/tools/...`, `icons/skills/...`).
2. **Segunda Prioridade — Pasta de Ícones do Sistema de Jogo (System):**
   - Caso não encontre um ícone correspondente no core, verifique e vasculhe a pasta do próprio sistema de jogo ativo por ícones dedicados (ex: `systems/<id-do-sistema>/icons/` ou diretório de assets do sistema).
3. **Terceira Prioridade / Fallback — Ícones Genéricos SVG do Core:**
   - Se ainda assim não houver um ícone específico nem no core nem no sistema, utilize obrigatoriamente um ícone SVG genérico de fallback de:
     `%url-foundry-vtt%/App/resources/app/public/icons/svg/` (servidos em caminhos como `icons/svg/item-bag.svg`, `icons/svg/sword.svg`, `icons/svg/shield.svg`, `icons/svg/aura.svg`, `icons/svg/d20-black.svg`, `icons/svg/mystery-man.svg`).

#### 10. Protocolo de Engenharia Reversa (REA) e Memória Persistente (CRÍTICO)
Ferramentas: [`rea-agents`](https://github.com/morluto/rea) (REA MCP/CLI) e o guia [`rea-engenharia-reversa`](https://github.com/inematds/rea-engenharia-reversa). Fluxo completo: [guides/reverse-engineering.md](guides/reverse-engineering.md).
- **Use o REA** para estudar o core do Foundry, sistemas e módulos (APIs reais, hooks, DataModels, fichas) antes de construir, garantindo precisão e menos erros.
- **Gatilho:** QUALQUER pedido para gerar módulo para um sistema/Foundry, fazer engenharia reversa, **criar sistema novo, ajustar sistema, recriar ou criar do zero**.
- **Antes:** ler `memory/learnings.md` e `memory/<alvo>.md`. **Depois (mesmo se falhar):** salvar descobertas, armadilhas, padrões e melhorias ali com o template do guia (só fatos verificados, sem segredos/conteúdo licenciado) e promover o que for geral para `guides/`/`systems/`.

#### 11. Protocolo de Auto-Instalação, Reinstalação e Atualização com Sobrescrita Consciente (CRÍTICO)
Sempre que o usuário solicitar a instalação, reinstalação ou atualização desta skill (ou quando ferramentas essenciais estiverem ausentes):
1. **Verificar se a Skill Já Existe (No Projeto ou Globalmente):**
   - O Agente **DEVE verificar se a skill já está presente** localmente no projeto (`skills/master-of-foundryvtt` ou diretório atual) ou globalmente no ecossistema do desenvolvedor:
     - Windows/Linux: `~/.gemini/config/skills/master-of-foundryvtt`, `~/.claude/skills/master-of-foundryvtt`, `~/.agents/skills/master-of-foundryvtt`.
2. **Avisar o Usuário e Sobrescrever com os Novos Recursos:**
   - Se a skill já existir e o usuário pediu para reinstalar/atualizar:
     - **O Agente DEVE OBRIGATORIAMENTE emitir o aviso ao usuário:**  
       > 📢 *"Identifiquei que a skill `master-of-foundryvtt` já estava instalada no ambiente (local/global). Estou atualizando e sobrescrevendo os arquivos com a versão mais recente e todos os novos recursos (motores de regras do Tio Nitro, engenharia reversa do Foundry v14, MCPs e bases de conhecimento)."*
     - Prosseguir com a sobrescrita/atualização dos arquivos (via junção/symlink ou cópia direta), preservando memórias persistentes locais (`memory/`) e garantindo que todas as bases de conhecimento (`kb/`), guias, sistemas e scripts fiquem 100% atualizados.
3. **Comunicação de Dependências:**
   - Comunicar ao desenvolvedor os componentes necessários: Node.js + npm, Git, Python 3.8+, REA (`rea-agents`), `@foundryvtt/foundryvtt-cli`, `fvtt-world-cli`, os MCPs do Foundry (`ninjos-foundry-mcp`, `foundryvtt-mcp`, `foundry-vtt-mcp`, nativo `master-of-foundryvtt`) e, opcionalmente, Ghidra/Hopper/IDA para binários nativos.
4. **Autorização Única e Execução Completa:**
   - Pedir autorização uma única vez para instalar/atualizar o ambiente.
   - **Se o dev responder sim**, o agente tem permissão para instalar e configurar tudo da melhor forma para o desenvolvimento Foundry (winget/npm/pip/git, `python scripts/setup_dev_env.py --yes`, registro dos MCPs, `npx rea-agents setup`, `fvtt configure`), auto-corrigindo falhas. Credenciais/caminhos continuam sendo perguntados, nunca chutados. Reiniciar o agente depois.
   - **Se não**, seguir com recursos limitados informando o que ficará indisponível.


---

### 📚 Estrutura e Navegação Rápida

- [Guia de Servidores MCP (Model Context Protocol)](mcp/README.md)
  - [Integração e Configuração dos MCPs](mcp/README.md)
  - [Manual de Instalação do MCP Nativo (`INSTALLATION.md`)](mcp/INSTALLATION.md)
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
  - [Certificados SSL, HTTPS e Let's Encrypt](kb/07-ssl-and-https.md)
  - [Engenharia Reversa do Core & Arquitetura da API v14](kb/08-core-reverse-engineering-v14.md)
  - [Motores de Regras, Game Design & Mecânicas de RPG](kb/09-rpg-engines-and-mechanics.md)
- [Guias de Desenvolvimento](guides/)
  - [Ferramentas CLI & Automação de Compêndios (`@foundryvtt/foundryvtt-cli` e `fvtt-world-cli`)](guides/cli-tools.md)
  - [Criando Sistemas de Jogo](guides/creating-systems.md)
  - [Criando Módulos](guides/creating-modules.md)
  - [Integração de IA & LLMs (Integrate AI, Phil's Assistant, AI Actors)](guides/ai-and-llm-integration.md)
  - [Matriz de Competências & Especializações de Desenvolvimento](guides/development-skills-matrix.md)
  - [Sockets e Comunicação Cliente-Servidor (Nativo e socketlib)](guides/sockets.md)
  - [Gerenciamento de Combate, Tracker e Iniciativa](guides/combat.md)
  - [Macros, Tabelas e Compêndios](guides/macros-and-tables.md)
  - [Armadilhas Automáticas & Gatilhos (Sequencer & Monk's Active Tile Triggers)](guides/automated-traps-and-triggers.md)
  - [Efeitos Ativos e Condições](guides/active-effects.md)
  - [Resolução de Erros e Isolamento de Conflitos](guides/troubleshooting.md)
- [Políticas e Governança](policies/)
  - [Contrato de Licença Limitada](policies/license.md)
  - [Política de Inteligência Artificial](policies/ai-policy.md)
  - [Diretrizes de Marca (Branding)](policies/branding.md)
  - [Política de Privacidade](policies/privacy-policy.md)

---

## 🛠️ Documentação Técnica de Desenvolvimento para Foundry VTT  
**Versão do Documento:** 1.0 (Focado em v12, v13, v14+ e Compatibilidade Futura)  
**Público-Alvo:** Desenvolvedores de Módulos, Sistemas, Tradutores e Agentes de IA/API.  
**Autor:** Charles Corrêa (Padronização de Boas Práticas)

### 1. Introdução e Propósito
Esta documentação estabelece os padrões ouro para o desenvolvimento de pacotes (módulos, sistemas, traduções e mundos) no Foundry Virtual Tabletop. O foco principal é a **compatibilidade futura (*forward compatibility*)**, garantindo que o código funcione nas versões mais recentes (v12, v13, v14+) e evitando o uso de APIs obsoletas (*deprecated*) que foram removidas em migrações recentes (ex: transição de v10 para v12+).

### 2. Ambiente de Desenvolvimento e Setup Inicial (Boas Práticas)
Para evitar erros comuns, corrupção de dados e perda de produtividade, o ambiente deve ser configurado rigorosamente:

#### 2.1. Ferramentas Essenciais
1. **Node.js (LTS)**: Necessário para executar ferramentas de build, linting e o CLI oficial.
2. **Git**: Controle de versão obrigatório. Use branches para funcionalidades (`feat/`, `fix/`, `chore/`).
3. **VS Code** com as seguintes extensões:
   - *ESLint* e *Prettier* (para padronização de código).
   - *Foundry VTT Snippets* (atalhos para Hooks, Documents, etc.).
   - *Handlebars* (para sintaxe de templates).
4. **TypeScript**: Altamente recomendado. Instale `@league-of-foundry-developers/foundry-vtt-types` como dependência de desenvolvimento. Isso permite que sua IDE sinalize APIs obsoletas *antes* da execução.

#### 2.2. Foundry VTT CLI Oficial (`@foundryvtt/foundryvtt-cli`) — Instalação Obrigatória no Desenvolvimento
**Sim, o CLI oficial deve ser instalado em todo ambiente de desenvolvimento profissional de módulos e sistemas.**
Ele é a ferramenta mantida diretamente pela equipe do Foundry Gaming para resolver os principais gargalos de versionamento (Git) e publicação:

* **Por que é indispensável:**
  1. **Compêndios Amigáveis ao Git (`unpack` / `pack`):** O Foundry armazena compêndios em bancos binários `ClassicLevel`/`LevelDB`, que geram conflitos massivos no Git. O CLI desempacota esses bancos em arquivos YAML/JSON legíveis linha a linha, e os recompila para binário antes do teste ou release.
  2. **Validação de Manifestos (`validate`):** Valida os esquemas do `module.json` ou `system.json` contra as regras oficiais do Foundry VTT antes de subir alterações.
  3. **Automação de Build e Releases (`release`):** Cria os pacotes `.zip` e atualiza URLs de download de forma automatizada para GitHub Releases ou CI/CD.

* **Comandos de Instalação e Configuração:**
  ```bash
  # Instalação global via npm (recomendado para desenvolvimento contínuo):
  npm install -g @foundryvtt/foundryvtt-cli

  # Ou execução pontual sem instalar globalmente via npx:
  npx @foundryvtt/foundryvtt-cli --help

  # Configurar o caminho da sua pasta Data do Foundry (executar uma única vez):
  fvtt configure set dataPath "C:/Users/<SeuUsuario>/AppData/Local/FoundryVTT/Data"

  # Para automação complementar de testes/mundos, instale também:
  npm install -g fvtt-world-cli
  ```

* **Fluxo de Trabalho Obrigatório com Compêndios:**
  ```bash
  fvtt package workon "meu-modulo" --type Module   # Define o pacote ativo
  fvtt package unpack "meu-modulo"                 # Extrai compêndios binários para YAML (para commitar no Git)
  fvtt package pack "meu-modulo"                   # Compila YAML para binário ClassicLevel (para rodar no Foundry)
  fvtt package validate "meu-modulo"               # Audita integridade do manifesto
  ```
> 📖 Para guia completo e avançado de comandos, consulte [guides/cli-tools.md](guides/cli-tools.md).

#### 2.3. Configuração Crítica de Antivírus
**Problema:** O Foundry VTT grava arquivos `db.json` com frequência. Antivírus com varredura em tempo real podem bloquear esses arquivos, causando erros `EBUSY`, `EPERM` ou corrupção silenciosa de dados.  
**Solução:** Adicione exclusões permanentes no seu antivírus (Windows Defender, etc.) para:
- A pasta de instalação do Foundry VTT.
- A pasta de `Data` do Foundry (onde ficam os mundos e módulos).
- Sua pasta de workspace de desenvolvimento local.

#### 2.4. Agentes de IA e MCP (Model Context Protocol)
Para que agentes de IA ou ferramentas de codificação assistida gerem código compatível, inclua um arquivo `CLAUDE.md` ou `.cursorrules` na raiz do repositório com as seguintes regras:
> "Este é um projeto Foundry VTT. Use a API mais recente (v12/v13+). NÃO use `document.data.data` (use `document.system`). NÃO use jQuery em `activateListeners` (use DOM puro e o sistema de `actions` do ApplicationV2). Sempre prefixe flags e classes CSS com o ID do pacote."

### 3. Arquitetura de Pacotes e Manifesto

#### 3.1. Estrutura do `module.json` / `system.json`
O manifesto deve declarar explicitamente a compatibilidade para evitar carregamento em versões incompatíveis:
```json
{
  "id": "meu-modulo-incrivel",
  "title": "Meu Módulo Incrível",
  "version": "1.0.0",
  "compatibility": {
    "minimum": "12",
    "verified": "13",
    "maximum": "14"
  },
  "esmodules": ["scripts/main.js"],
  "styles": ["styles/meu-modulo.css"],
  "languages": [
    {
      "lang": "pt-BR",
      "name": "Português (Brasil)",
      "path": "lang/pt-BR.json"
    }
  ]
}
```
⚠️ **Atenção:** O caminho `path` deve ser relativo à raiz do pacote (ex: `lang/pt-BR.json`). O formato antigo `modules/meu-modulo/lang/pt-BR.json` foi **descontinuado e gera erro** em versões recentes.

#### 3.2. Namespacing (Prevenção de Conflitos)
- **Flags:** Sempre use o escopo do seu pacote: `actor.setFlag("meu-modulo-incrivel", "chave", valor)`.
- **CSS:** Prefixe todas as classes e IDs. Ex: `.meu-modulo-incrivel .sheet-body` em vez de `.sheet-body`.

### 4. Guias de Desenvolvimento por Categoria (v12 → v13/v14+)

#### 4.1. Traduções e Internacionalização (i18n)
- Use `game.i18n.localize("MEU_MODULO.Chave")` ou `game.i18n.format("MEU_MODULO.Chave", { data: valor })`.
- Nunca codifique textos fixos em inglês/português no código JavaScript. Centralize tudo em `lang/en.json` e `lang/pt-BR.json`.

#### 4.2. Documents (Actors, Items, NPCs, Inimigos)
A mudança mais crítica das versões antigas (v9/v10) para as atuais:
- **Obsoleto (v10-):** `actor.data.data.forca` ou `item.data.data.dano`.
- **Atual (v11+):** `actor.system.forca` ou `item.system.dano`.
- **Atualização de Dados:** Para modificar dados localmente antes de salvar, use `document.updateSource({ system: { forca: 15 } })` em vez do antigo `document.data.update()`.

#### 4.3. Fichas de Personagem (Sheets) e ApplicationV2
O Foundry está migrando de `Application` (v1) para `ApplicationV2`. Se você está atualizando um módulo, planeje a conversão:
- **Construtor:** Agora aceita um único objeto de opções: `constructor(options) { super(options); }`.
- **Eventos:** O método `activateListeners(html)` (que recebia objetos jQuery) está sendo substituído por um sistema de `actions` no construtor, e o parâmetro `html` agora é um **Elemento DOM puro**, não um objeto jQuery.
  ```javascript
  // Padrão v13+ (ApplicationV2)
  static get defaultOptions() {
    return mergeObject(super.defaultOptions, {
      tag: "form", // OBRIGATÓRIO para formulários
      actions: {
        "click .botao-salvar": this.onSaveClick.bind(this)
      }
    });
  }
  ```
- **Editor de Texto:** O helper `{{editor}}` do Handlebars foi atualizado para suportar o editor ProseMirror. Use `{{editor:context}}` ou as novas diretivas conforme a documentação da API v13+.

#### 4.4. Handouts, Mapas (Scenes) e Tabelas (RollTables)
- Todos são `Document`s. Use `game.scenes`, `game.journal`, `game.tables`.
- Para adicionar dados personalizados a uma Cena ou Tabela, use **Flags**. Não tente injetar campos diretamente no objeto raiz do documento, pois o schema do Foundry os rejeitará.
- **Macros:** Ao criar macros que interagem com esses documentos, sempre verifique se o documento existe: `const cena = game.scenes.get(id); if (!cena) return;`.

#### 4.5. Compêndios (Packs)
- Não edite arquivos `.db` manualmente. Use o Foundry VTT CLI:
  ```bash
  fvtt package pack --input packs/meu-compendio --output packs/meu-compendio.db
  ```
- Para acessar dados de um compêndio via código:
  ```javascript
  const pack = game.packs.get("meu-modulo.itens-especiais");
  const index = await pack.getIndex();
  const itemData = await pack.getDocument(index.find(i => i.name === "Espada Mágica")._id);
  ```

#### 4.6. Sistemas Próprios e Migração de Dados
Se você mantém um Game System, é obrigatório implementar um script de migração no `init` ou `ready`:
```javascript
Hooks.once("ready", async () => {
  if (game.user.isGM) {
    const currentSchemaVersion = game.settings.get("meu-sistema", "schemaVersion");
    if (currentSchemaVersion < 2) {
      await migrateWorld();
      game.settings.set("meu-sistema", "schemaVersion", 2);
    }
  }
});
```
A função `migrateWorld` deve iterar sobre `game.actors` e `game.items`, atualizando estruturas de dados antigas para o novo schema (ex: mover dados de `data.data` para `system`).

#### 4.7. Macros e Hooks
- Use `Hooks.on("createActor", (actor, options, userId) => { ... })` para reagir a eventos.
- Para sobrescrever funcionalidades do núcleo ou de outros módulos, **NÃO** sobrescreva métodos diretamente (monkey-patching). Use a biblioteca **libWrapper** (padrão da comunidade) para garantir compatibilidade entre múltiplos módulos que modificam o mesmo método.

### 5. Estratégias de Compatibilidade e Atualização (v10 → v14)
1. **Auditoria de Depreciação:** Execute o Foundry em modo de desenvolvimento e monitore o Console do Navegador (F12). Qualquer aviso `@deprecated` deve ser tratado imediatamente.
2. **Verificação de Versão:** Use a função nativa `isNewerVersion(game.version, "12.0")` para executar código condicional apenas em versões que suportam novos recursos.
3. **Remoção de jQuery:** Comece a refatorar `$(html).find(".classe")` para `html.querySelector(".classe")`. O jQuery será gradualmente removido do núcleo do Foundry.
4. **Testes Automatizados:** Considere usar o `foundry-vtt-types` para compilar seu projeto TypeScript. Se o compilador passar, há uma chance muito maior de o código estar livre de erros de API obsoleta.

### 6. Checklist de Revisão Pré-Lançamento
- [ ] O `module.json` / `system.json` possui os campos `compatibility.minimum` e `compatibility.verified` atualizados?
- [ ] Todas as referências a `document.data.data` foram substituídas por `document.system`?
- [ ] As classes CSS e IDs possuem prefixo único do pacote?
- [ ] As chaves de tradução estão centralizadas nos arquivos `lang/` e não hardcodadas?
- [ ] O antivírus possui exclusões para a pasta de desenvolvimento e `Data` do Foundry?
- [ ] O código foi testado na versão "Testing" ou "Stable" mais recente do Foundry VTT?
- [ ] O arquivo `CLAUDE.md` / `.cursorrules` está presente para orientar agentes de IA?

### 7. Recursos e Links de Referência Oficiais
Mantenha estes links salvos como referência primária. A documentação da API é a fonte da verdade:

* **Documentação Oficial da API:**
  - [API Documentation (Geral)](https://foundryvtt.com/api/)
  - [API v14 (Futuro/Prototype)](https://foundryvtt.com/api/v14) *(Verificar disponibilidade)*
  - [API v13](https://foundryvtt.com/api/v13)
  - [API v12](https://foundryvtt.com/api/v12)
  - [API v11](https://foundryvtt.com/api/v11)
  - [API v10](https://foundryvtt.com/api/v10)

* **Guias de Migração e Desenvolvimento:**
  - [Introdução ao Desenvolvimento](https://foundryvtt.com/article/intro-development/)
  - [Introdução ao Desenvolvimento de Módulos](https://foundryvtt.com/article/module-development/)
  - [Introdução ao Desenvolvimento de Sistemas](https://foundryvtt.com/article/system-development/)
  - [Guias de Migração da API (v10, v11, v12)](https://foundryvtt.com/article/migration/)
  - [Guia de Conversão para ApplicationV2](https://foundryvtt.wiki/en/development/guides/applicationV2-conversion-guide)

* **Wiki da Comunidade e Ferramentas:**
  - [Foundry VTT Community Wiki (Home)](https://foundryvtt.wiki/en/home)
  - [Guia de Desenvolvimento da API](https://foundryvtt.wiki/en/development/api)
  - [League of Extraordinary Foundry VTT Developers](https://foundryvtt.wiki/en/league) (Mantenedores dos tipos TypeScript)
  - [Guia de Contribuição para Idiomas](https://foundryvtt.wiki/en/languages)
  - [Diretrizes de Contribuição da Wiki](https://foundryvtt.wiki/en/wiki-contribution-guidelines)
  - [Guias de Migração do Core (v8, v9, v10)](https://foundryvtt.wiki/en/migrations)

* **Ferramentas de CLI e Comunidade:**
  - [foundryvtt-cli (Oficial)](https://github.com/foundryvtt/foundryvtt-cli)
  - [fvtt-world-cli (Comunitário)](https://github.com/DroiD16/fvtt-world-cli)
  - [Pacotes com Suporte a Idiomas](https://foundryvtt.wiki/en/community/packages-with-language-support)
  - [Sistemas de Jogo da Comunidade](https://foundryvtt.wiki/en/community/game-systems)

### 8. Extração de Dados de Repositórios e Engenharia Reversa
Esta seção descreve como usar ferramentas web para **extrair informações estruturais** (arquivos, pastas, esquemas e diagramas) de repositórios de sistemas ou módulos do Foundry VTT (sejam do GitHub, GitLab ou outros), facilitando o estudo e o desenvolvimento de novos pacotes.

#### 8.1. Ferramentas Web de Apoio
- **gitingest.com**: Converte o repositório inteiro em contexto de texto limpo para IA e visualiza árvore de pastas, arquivos e estatísticas.
- **gitdiagram.com**: Gera diagramas de arquitetura, fluxos e visualização da árvore de arquivos e diretórios.
- **repomix.com**: Empacota o repositório em arquivo único para ingestão direta por IAs.
- **uithub.com**: Extração de arquivos de repositório em formato token-friendly.
- **github.githistory.xyz**: Navegador visual do histórico de commits e evolução de arquivos específicos (ex: `README.md`, `system.json`).
- **deepwiki.com**: Documentação profunda e insights gerados para repositórios.
- **star-history.com**: Histórico de relevância e adoção de projetos comunitários.
- **download-directory.github.io**: Baixa subdiretórios específicos de repositórios sem clonar o projeto inteiro.
- **codesandbox.io**: Criação de ambiente interativo de sandbox direto de repositórios.
- **markdownviewer.org / markmap-editor**: Visualização e mapas mentais de documentação Markdown.

#### 8.2. Templates de URL Dinâmicos por Repositório Alvo
Ao trabalhar com qualquer repositório, adapte as URLs substituindo `{{owner}}` e `{{repo}}` (ex.: `peginc/swade`, `foundryvtt/dnd5e` ou `lipefl/swade-tools`):

| Ferramenta | Template de URL | Exemplo de Aplicação |
| :--- | :--- | :--- |
| **Gitingest** | `https://gitingest.com/{{owner}}/{{repo}}` | `https://gitingest.com/peginc/swade` |
| **GitDiagram** | `https://gitdiagram.com/{{owner}}/{{repo}}` | `https://gitdiagram.com/foundryvtt/dnd5e` |
| **Repomix** | `https://repomix.com/?repo={{owner}}/{{repo}}&format=markdown&showLineNumbers=true&outputParsable=true` | `https://repomix.com/?repo=lipefl/swade-tools&format=markdown&showLineNumbers=true&outputParsable=true` |
| **Uithub** | `https://uithub.com/{{owner}}/{{repo}}?maxTokens=500000` | `https://uithub.com/lipefl/swade-tools?maxTokens=500000` |
| **GitHistory** | `https://github.githistory.xyz/{{owner}}/{{repo}}/blob/main/README.md` | `https://github.githistory.xyz/lipefl/swade-tools/blob/main/README.md` |
| **DeepWiki** | `https://deepwiki.com/{{owner}}/{{repo}}` | `https://deepwiki.com/lipefl/swade-tools` |
| **Star History** | `https://www.star-history.com/?type=date&repos={{owner}}/{{repo}}` | `https://www.star-history.com/?type=date&repos=foundryvtt/dnd5e` |
| **Download Subdir** | `https://download-directory.github.io/?url=https://github.com/{{owner}}/{{repo}}` | `https://download-directory.github.io/?url=https://github.com/lipefl/swade-tools` |
| **CodeSandbox** | `https://codesandbox.io/p/sandbox/github/{{owner}}/{{repo}}` | `https://codesandbox.io/p/sandbox/github/foundryvtt/dnd5e` |
| **Markmap** | `https://markdownviewer.org/markmap-editor?url=https://raw.githubusercontent.com/{{owner}}/{{repo}}/main/README.md` | `https://markdownviewer.org/markmap-editor?url=https://raw.githubusercontent.com/foundryvtt/dnd5e/main/README.md` |

#### 8.3. Fluxo de Estudo para Novos Módulos ou Sistemas
1. **Identificar o repositório base**: Localize o repositório público do sistema ou módulo no GitHub/GitLab (ex: `peginc/swade` ou `foundryvtt/dnd5e`).
2. **Construir as URLs**: Monte os links usando a tabela acima.
3. **Extrair estrutura e arquivos**: Use o Gitingest / Repomix para absorver a arquitetura (`system.json`/`module.json`, `templates/`, `module/`).
4. **Mapear diagramas de dependências**: Abra o GitDiagram para entender como os arquivos JavaScript/TypeScript se conectam.
5. **Estudar DataModels e Schemas**: Inspecione as classes `TypeDataModel` e `ApplicationV2` usadas no repositório.
6. **Desenvolver com precisão**: Use as descobertas para criar novos módulos com total compatibilidade com o sistema-alvo.

### 9. Arquivo Morto, Migrações Legadas e Ferramentas do Ecossistema
Caso precise dar manutenção em códigos abandonados ou buscar referências e ferramentas da comunidade:

* **Documentação Legada (Pré-v10):**
  - [API v9](https://foundryvtt.com/api/v9) | [API v8](https://foundryvtt.com/api/v8) | [API v7](https://foundryvtt.com/api/v7)
  - [Guia de Migração Core v9](https://foundryvtt.wiki/en/migrations/foundry-core-v9)
  - [Guia de Migração Core 0.8.x](https://foundryvtt.wiki/en/migrations/foundry-core-0_8_x)

* **Diretórios e Recursos Comunitários:**
  - [Community Tools (Ferramentas)](https://foundryvtt.wiki/en/community/Community-Tools)
  - [Defunct Modules (Módulos Abandonados)](https://foundryvtt.wiki/en/community/defunct-modules) - Excelente para checar o que *não* usar ou adotar para refatoração.
  - [Community Adventures](https://foundryvtt.wiki/en/community/Community-Adventures)
  - [Community Media](https://foundryvtt.wiki/en/community/Community-Media)
  - [Community Translations](https://foundryvtt.wiki/en/community/Community-Translations)
  - [Unlisted Game Systems](https://foundryvtt.wiki/en/community/unlisted-game-systems)
  - [Package Changelog](https://foundryvtt.wiki/en/community/package-changelog)

* **Segurança e Proteção para Agentes de IA:**
  - [Hol-Guard](https://github.com/hashgraph-online/hol-guard/) - Antivírus de código aberto para Agentes de IA (bloqueio de ferramentas de risco, acesso a segredos, injeção de prompt, pacotes maliciosos, servidores MCP e plugins em tempo de execução).

**Nota Final para Agentes de IA:** Ao gerar código para este projeto, priorize sempre a sintaxe das versões v12/v13+. Se uma dúvida sobre depreciação surgir, consulte a documentação da API mais recente disponível antes de sugerir uma solução legada. A estabilidade e a longevidade do pacote dependem dessa disciplina.

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)

