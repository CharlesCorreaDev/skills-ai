# Changelog 📜⚡

All notable changes to the **Skills AI** repository will be documented in this file.  
*Todas as alterações notáveis no repositório **Skills AI** serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
