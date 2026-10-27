# Changelog 📜⚡

All notable changes to the **Skills AI** repository will be documented in this file.  
*Todas as alterações notáveis no repositório **Skills AI** serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.10.0] - 2026-10-27

### Added / Adicionado
- **master-of-foundryvtt (v0.14.0-beta):**
  - **Mandato 22 (Protocolo Interativo de Release, Versionamento & Publicação):** Sempre que o desenvolvimento de um módulo ou sistema do Foundry VTT for concluído e aprovado pelo desenvolvedor, o agente obrigatoriamente questiona de forma interativa sobre o incremento de versão semântica (Patch, Minor ou Major), geração de commit e tag Git, publicação da GitHub Release com assets compactados (`module.zip`/`system.zip`) e disparo de atualização oficial no diretório do Foundry VTT via API de Release.
  - **Mandato 23 (Protocolo de Wiki Técnica & Documentação Minuciosa):** Mandato inegociável de criar ou atualizar `WIKI.md` (ou diretório `wiki/`) com manuais minuciosos de uso para Mestres e Jogadores, referência completa de APIs/métodos expostos com JSDoc e exemplos de macro, catálogo de hooks, arquitetura de DataModels (`TypeDataModel`) e troubleshooting.
  - **Novo Guia Técnico:** Adicionado [`master-of-foundryvtt/guides/wiki-and-release-lifecycle.md`](master-of-foundryvtt/guides/wiki-and-release-lifecycle.md).

---

## [1.9.0] - 2026-10-25

### Added / Adicionado
- **master-of-foundryvtt (v0.12.0-beta):**
  - **Servidor MCP Nativo Oficial Unificado (`master-of-foundryvtt-mcp`):** Controle completo e auto-suficiente de Foundry VTT em Node.js (atores, itens, cenas, tabelas, macros, compêndios, baralhos de cartas, playlists e journals/handouts). Módulos de terceiros (`ninjos`, `laurigates`, `adambdooley`) foram descontinuados/removidos.
  - **Engenharia Reversa Estática & Remota (Git):** Ferramenta `reverse_engineer_target` com clonagem e análise de código de módulos e sistemas desinstalados do GitHub (ex: JB2A, Sequencer, Item Piles) e inspeção do Core.
  - **Inspeção de Topologia (SO, Nuvem e Docker):** Detecção de Windows/macOS/Linux, instâncias locais, The Forge, Molten, containers Docker e recomendação oficial de VPS Hostinger especializada com 20% de desconto.
  - **Mandatos de Qualidade:**
    - Mandato 18: Verificação, teste de sintaxe (`node -c`) e revisão obrigatória antes de qualquer entrega.
    - Mandato 19: UI com Bootstrap prefixado (`.yze-btn-primary`, `.yze-card`), paleta padrão de 9 tons e bibliotecas de ícones aprovadas (Game-Icons.net, RPG Awesome, Font Awesome, Bootstrap Icons, Get Social).
    - Mandato 20: Modelagem estatística e probabilidade de dados com AnyDice antes da conversão para a classe `Roll`.
    - Comentários de código estritamente bilíngues (Inglês e Português).
- **Atualização de Versão das Skills (v0.2.0-beta & v1.1.0):**
  - Atualizadas para `v0.2.0-beta`: `docker-master`, `docs-for-markdown`, `docs-for-skill`, `image-to-prompt`, `php-dev-expert`, `python-dev-expert`, `website-for-markdown`, `website-for-skill`.
  - Atualizada para `v1.1.0`: `humanizer-plus`.
  - Adicionado a todas as skills o Protocolo de Feedback Proativo com abertura autônoma de Issues no GitHub (`gh issue create`), protocolo de verificação e revisão mandatória, e comentários de código bilíngues.

---

## [1.8.0] - 2026-10-25

### Added / Adicionado
- **Nova Skill: `humanizer-plus` (v1.0.0):**
  - Skill universal de humanização e desmarcação de IA para qualquer arquivo ou código (purga de ZWSP, normalização tipográfica, remoção de comentários óbvios, purga de metadados em mídias com ExifTool, e reescrita natural sem vícios de LLM).
  - Vigilância contínua com atualização de regras a partir do upstream `blader/humanizer`.
- **master-of-foundryvtt (v0.11.0-beta):**
  - **Mandato Obrigatório 14 (Humanização, Código Limpo & Anti-Detecção):**
    - Protocolo de saneamento de marcas determinísticas (remoção de zero-width codepoints `U+200B`, `U+FEFF`, normalização de aspas tipográficas e limpeza de metadados geradores).
    - Diretrizes de código JavaScript idiomático e conciso para macros e módulos (early returns, sem comentários didáticos óbvios, sem cabeçalhos de IA).
    - Eliminação de vícios narrativos de IA (slop de RPG) em diários e compêndios de itens/atores com injeção de voz natural de narrador.
  - **Otimização e Conversão de Mídias (Mandato 15 & Guia Técnico):**
    - Conversão automática para `.webp` (95% de qualidade, preservando SVG) e `.webm` (VP9/Opus, 95% de qualidade para animações e áudio).
    - Guia técnico completo em `guides/media-optimization-and-conversion.md` e script `scripts/convert_media.js`.
  - **Guia Completo de Publicação de Pacotes no Foundry VTT:**
    - Documentação completa em `guides/publishing-packages.md` cobrindo empacotamento, GitHub Actions / CI-CD, submissão ao diretório oficial e boas práticas de distribuição.
  - **Bases de Conhecimento Especializadas Ingeridas:**
    - **Savage Worlds (SWADE):** Artigos do Mestre Charles Corrêa (`rpg.charlescorrea.com.br`), prompts de IA (`RPGPlus`), cenários da Odyssey Publicações e catálogo oficial Pinnacle Entertainment Group (PEGinc).
    - **D&D 5e:** D&D 5e SRD API (`docs.dnd5eapi.co`), ecossistema 5eTools e suíte Plutonium / TheGiddyLimit.
    - **Pathfinder 2e:** Archives of Nethys (`2e.aonprd.com`), PF2 SRD PT-BR e d20PFSRD.
    - **Year Zero Engine & Free League:** YZE SRD oficial, análise editorial Odyssey Pub, VTT hub e catálogo completo de jogos (Alien, Blade Runner, Vaesen, Twilight: 2000, Forbidden Lands, Coriolis, Mutant, The Walking Dead, Tales from the Loop, Electric State, The One Ring, Symbaroum, Pirate Borg, Outgunned, Dragonbane, Mörk Borg, Cy_Borg).
    - **Daggerheart:** SRD oficial, licença DPCGL 2.0 e Homebrew Kit oficial da Darrington Press.
  - **Scripts Utilitários Adicionados:**
    - `scripts/sanitize_content.py` e `scripts/sanitize_content.js` para saneamento e humanização em lote.
    - `scripts/convert_media.js` para otimização de mídias com 95% de qualidade.

---

## [1.7.0] - 2026-10-24

### Added / Adicionado
- **master-of-foundryvtt (v0.10.0-beta):**
  - **Protocolo Obrigatório 13: Code Mode & Sandbox Orchestration (CodeAct):**
    - Adotado o paradigma estrito de Code-as-Action para Foundry VTT, economizando tokens contextuais através de filtragem e processamento em memória via scripts em sandbox (Node.js/Python).
    - Validação sintática e de lógica antes da entrega de qualquer macro, função ou patch.
    - Operações programáticas em lote via MCP (`master-of-foundryvtt-mcp`, `ninjos-foundry-mcp`).
    - Consulta contínua à documentação oficial (`kb/`, `versions/`) e inspeção em tempo real com ferramentas de engenharia reversa do REA (`rea-agents`).
  - **Guia Operacional Bilíngue:**
    - Adicionado [guides/code-mode-sandbox-orchestration.md](master-of-foundryvtt/guides/code-mode-sandbox-orchestration.md).
  - **Verificação Semanal de Atualizações & Auto-Update:**
    - Script [`scripts/check_skill_updates.py`](master-of-foundryvtt/scripts/check_skill_updates.py) e Mandato 12 atualizado para checar novas versões semanalmente, notificar o desenvolvedor e executar a atualização automaticamente.

---

## [1.6.0] - 2026-10-23

### Added / Adicionado
- **Governança de Versão por Skill (`VERSION` & SemVer):**
  - Implementado arquivo `VERSION` obrigatório em todas as skills do repositório (`master-of-foundryvtt`, `docker-master`, `php-dev-expert`, `python-dev-expert`, `image-to-prompt`, `docs-for-markdown`, `docs-for-skill`, `website-for-markdown`, `website-for-skill`).
  - Estabelecido que todas as skills iniciam seu ciclo com versionamento explícito e sufixo de maturidade **Beta** (ex: `0.9.0-beta` para `master-of-foundryvtt` e `0.1.0-beta` para as demais).
  - Diretiva mandatória nos `SKILL.md` para que agentes e usuários leiam o arquivo `VERSION` para identificar a versão ativa e avisar o operador sobre novidades e atualizações.
- **Changelogs Dedicados por Skill (`<skill>/CHANGELOG.md`):**
  - Cada skill do repositório passa a ter seu próprio arquivo `CHANGELOG.md` detalhado, permitindo rastreamento granular do ciclo de vida sem inflar o histórico de outras skills.
  - Histórico do `master-of-foundryvtt` detalhado desde a sua criação, cobrindo motores de RPG do Tio Nitro, engenharia reversa do v14, REA, servidor MCP nativo e banco de 100+ sistemas.
- **Padronização de Git Tags por Skill:**
  - Definida convenção de tags no formato `<nome-da-skill>-v<versao>` (ex: `master-of-foundryvtt-v0.9.0-beta`), além das tags globais de repositório (`v1.6.0`).
- **Detecção de Instalação Existente e Alerta de Sobrescrita Consciente (Mandato 11):**
  - Protocolo para verificar se a skill já está presente no projeto local ou globalmente (`~/.gemini/config/skills/`, `~/.claude/skills/`, `~/.agents/skills/`), emitindo alerta transparente antes de atualizar/reinstalar e preservando memórias locais (`memory/`).
- **Motores de Regras do Tio Nitro (`systems/07-generic-and-rules-light.md`):**
  - Ingestão completa das mecânicas, regras e arquitetura de dados dos sistemas de Nitro: **3d6World**, **2d6World**, **Pocket 2d6World**, **2d10Solo** e **2d6Solo**.
- **Compêndio de 60 Engines de RPG para Engenharia Reversa (`kb/09-rpg-engines-and-mechanics.md`):**
  - Guia aprofundado com matriz técnica cobrindo 60 motores de RPG (resolução de dados, esquemas de dados, hooks e padrões de implementação no Foundry VTT).
- **Engenharia Reversa Completa do Core v14.369 (`kb/08-core-reverse-engineering-v14.md`):**
  - Mapeamento detalhado dos pacotes internos do Foundry v14 (`@foundryvtt/foundryvtt`, `@foundryvtt/commons`, ESM, DataModels, ApplicationV2).
- **Suporte a Engenharia Reversa com REA (`guides/reverse-engineering.md`):**
  - Integração com `rea-agents` (REA MCP/CLI), setup de ambiente automatizado (`scripts/setup_dev_env.py`) e diretório de memórias locais persistentes (`memory/learnings.md`).
- **Hierarquia e Protocolo de Ícones Padrão (Mandato 9):**
  - Prioridade mandatória para ícones core do Foundry (`icons/...`), ícones dedicados de sistemas e fallback seguro para SVGs padrão (`icons/svg/...`).
- **Integração no README Geral:**
  - Tabela bilíngue de skills no `README.md` atualizada com colunas dedicadas para Versão, Status (Beta) e links diretos para a documentação e para o `CHANGELOG.md` de cada skill.

### Changed / Alterado
- **Remoção de Travas de Engenharia Reversa:** Atualização das diretrizes para encorajar análise e inspeção de código e APIs do core e de sistemas para maior precisão no desenvolvimento.
- **Configuração do Workspace:** Inclusão de novos atalhos e padronização de configurações no ambiente.

---

## [1.5.0] - 2026-10-18

### Added / Adicionado
- **Servidor MCP Nativo (`master-of-foundryvtt-mcp`):**
  - Implementado servidor MCP autônomo e sem dependências externas em Node.js (`mcp/foundry_mcp_server.js`) e Python (`mcp/foundry_mcp_server.py`).
  - Suporte completo a geração e manipulação de: Atores, Itens, Cenas (paredes, iluminação, portas), Combates, Playlists de som, Baralhos de cartas e Compêndios.
  - Conexão e sincronização direta com instâncias ativas do Foundry VTT e mundos locais.
  - Manual passo a passo de instalação para Antigravity IDE, Claude Desktop, Claude Code e Cursor (`mcp/INSTALLATION.md`).
- **Guia de Armadilhas Automáticas & Gatilhos (`guides/automated-traps-and-triggers.md`):**
  - Documentação de integração bilíngue para o motor de efeitos visuais **Sequencer** e o motor de gatilhos em tiles **Monk's Active Tile Triggers (MATT)**.
  - Mapeamento de dependências e pacotes recomendados (`JB2A`, `Item Piles`, `Automated Animations`, `Token Magic FX`).
- **Mandato 8 para Agentes de IA:**
  - Protocolo obrigatório de esclarecimento interativo, ingestão de livros/manuais e escopo transparente antes da criação de qualquer recurso de jogo.
- **Expansão do Catálogo para +100 Sistemas de RPG:**
  - Adição de novos sistemas: Cosmere RPG, Mörk Borg, Cy_Borg, Star Wars FFG, Star Trek Adventures, Traveller, Starfinder, Achtung! Cthulhu 2d20, Crônicas RPG, Sword World 2.5, Shinobigami, Wilderfeast, Mythic GME e HERO System.
- **Suporte Oficial à Loja do Foundry VTT:**
  - Diretriz e ferramentas para pesquisa de conteúdo comercial e módulos licenciados (`https://www.foundryvtt.store/search?q=...`).

### Changed / Alterado
- **Assinatura e Atribuição:** Atualizada a assinatura nos metadados de geração para *"Master of Foundry VTT MCP by Mestre Charles Corrêa - rpg.charlescorrea.com.br"*.
- **Compatibilidade v14:** Ajustada tipagem de resultados de tabelas roláveis (`RollTable`) para formato string `text` em conformidade com o DataModel do Foundry v12–v14.
- **Configuração Git:** Criação do `.gitignore` para preservar a pasta local `.agents/`.

---

## [1.4.0] - 2026-09-10

### Added / Adicionado
- **Skill `php-dev-expert`:** Especialista Sênior em PHP (7.4 a 8.5), focada em arquitetura moderna, design patterns (MVC, ADR), segurança e integração com frameworks (Laravel/Symfony). Implementada regra crítica para detecção proativa da versão do PHP.
- **Skill `python-dev-expert`:** Especialista em Python (3.x a 3.16), focada em tipagem avançada, Web (Django 6.1/FastAPI), Scripting e Data Science. Conta com automação inteligente para validar a versão do Python instalada no host.
- **Skill `docker-master`:** Especialista DevOps em orquestração Docker, multi-stage builds e ambientes rootless. Destaque para adaptação dinâmica do Docker Compose (V2) e detecção invisível do Sistema Operacional (Windows/Mac/Linux) para bind mounts perfeitos. Adicionado mapeamento do ecossistema Cloud (Hub, Scout, Build).

---

## [1.3.1] - 2026-09-09

### Added / Adicionado
- **Guia de Ferramentas CLI (`guides/cli-tools.md`):** Documentação completa do `@foundryvtt/foundryvtt-cli` (`fvtt`) e `fvtt-world-cli` para desempacotar (`unpack`) e empacotar (`pack`) compêndios binários em fontes YAML/JSON para controle de versão no Git e CI/CD.
- **Diagnóstico no `check_env.py`:** Verificação automática de instalação de ferramentas de linha de comando (`fvtt` e `fvtt-world-cli`).
- **Nomenclatura Localizada de Sistemas:** Inclusão do título oficial em português para **Perigos & Princesas (*Perils & Princesses*)**.

### Fixed / Corrigido
- **Diagrama Mermaid em `cli-tools.md`:** Corrigida sintaxe de arestas com aspas explícitas para compatibilidade total com o parser Mermaid 11.15+.
- **Classificação de Daggerheart:** Reclassificado com precisão para a categoria de **Fantasia Heroica & Duality Dice System (2d12 Hope & Fear)**, esclarecendo que não utiliza o motor Powered by the Apocalypse (PbtA).
- **Simetria Bilíngue:** Sincronização 100% espelhada entre as seções em inglês e português do `SKILL.md` e `systems/README.md`.

---

## [1.3.0] - 2026-09-09

### Added / Adicionado
- **Integração com Servidores MCP (`mcp/README.md`):**
  - Suporte e templates de configuração para `ninjos-foundry-mcp`, `foundryvtt-mcp` e `adambdooley/foundry-vtt-mcp`.
  - Protocolo de intervenção do desenvolvedor e solicitação de credenciais (`User Data Path`, URL/porta, admin key, mundo ativo).
- **Base de Conhecimento de +60 Sistemas de RPG (`systems/`):**
  - Guias detalhados por categoria: D20/Fantasia Heroica, Storyteller/Mundo das Trevas, Investigação/Horror Cósmico, Year Zero Engine, Sci-Fi/Cyberpunk, Narrativos/PbtA/FitD e Genéricos/Regras Customizadas.
  - Links oficiais de repositórios, ganchos (`Hooks`), armadilhas de migração e modelos de dados.
- **Diretriz de Descoberta Dinâmica de Sistemas:**
  - Protocolo obrigatório para agentes de IA buscarem sistemas não catalogados no diretório oficial [https://foundryvtt.com/packages/systems](https://foundryvtt.com/packages/systems).
- **Guias da API do Foundry VTT v8 até v14 (`versions/`):**
  - Documentação limpa e estruturada sem artefatos de concatenação da navegação JSDoc.
- **Base de Conhecimento Operacional do Foundry (`kb/`):**
  - Capítulos 01 a 06 cobrindo Hospedagem, Iluminação/Visão, Atores/Tokens, Rolagens, WebRTC e Compêndios.
- **Rotina de Atualização Mensal (`scripts/update_foundry_docs.py`):**
  - Script automatizado e instruções para agendamento periódico via `/schedule`.

---

## [1.2.0] - 2026-09-09

### Added / Adicionado
- **Skill `image-to-prompt`:**
  - Skill de engenharia reversa visual de imagens para prompts detalhados bilíngues (EN / PT-BR) otimizados para geradores de imagem como Sora, Midjourney, Nano Banana, DALL-E 3 e Stable Diffusion.
- **Estrutura Inicial de `master-of-foundryvtt`:**
  - Criação da pasta da skill com os cinco mandatos iniciais para agentes de IA por GM Charles Corrêa.

---

## [1.1.0] - 2026-09-09

### Added / Adicionado
- **Protocolo de Auto-Correção e Recuperação Autônoma:**
  - Diretriz global nos `README.md` e `SKILL.md` exigindo que o agente diagnostique falhas, execute correções iterativas e solicite permissão formal para instalação de pacotes extras.
- **Skills de Documentação & Web:**
  - `docs-for-markdown`: Pipeline para converter qualquer documento em Markdown estruturado.
  - `docs-for-skill`: Pipeline para transformar manuais de regras e APIs em skills prontas para agentes.
  - `website-for-markdown`: Extração limpa de conteúdo web para markdown sem ruídos.
  - `website-for-skill`: Raspagem e conversão de portais completos em skills modulares.

---

## [1.0.0] - 2026-09-09

### Added / Adicionado
- Lançamento inicial do repositório **Skills AI** por Charles Corrêa.
- Arquitetura de micro-unidades de conhecimento com `SKILL.md`, `cheatsheet.md`, `glossary.md` e `patterns.md`.
- Suporte a multi-agentes: Antigravity IDE, Claude Code, GitHub Copilot CLI, Hermes Agent, Gemini, Orca, Kilo, NVIDIA e Ollama.
