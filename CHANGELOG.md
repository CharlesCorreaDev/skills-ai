# Changelog 📜⚡

All notable changes to the **Skills AI** repository will be documented in this file.  
*Todas as alterações notáveis no repositório **Skills AI** serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
