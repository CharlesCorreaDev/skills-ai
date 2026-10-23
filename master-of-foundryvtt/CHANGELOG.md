# Changelog - Master of Foundry VTT 🎲⚡

All notable changes to the `master-of-foundryvtt` skill will be documented in this file.  
*Todas as alterações notáveis na skill `master-of-foundryvtt` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.9.0-beta] - 2026-10-23

### Added / Adicionado
- **Arquivo `VERSION` e Mandato 12 de Versionamento Semântico:**
  - Adicionado arquivo `VERSION` dedicado (`0.9.0-beta`) e mandato obrigatório para o Agente ler o arquivo, alertar o desenvolvedor sobre a versão ativa e seguir rigorosamente o SemVer nas atualizações.
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
- **Guia de Armadilhas Automáticas e Gatilhos (`guides/automated-traps-and-triggers.md`):**
  - Documentação bilíngue de automação com Sequencer, Monk's Active Tile Triggers (MATT), JB2A e Item Piles.
- **Mandato 8 de Esclarecimento Interativo e Escopo Transparente:**
  - Portão obrigatório de perguntas antes de criar qualquer documento ou cena, prevenindo alucinações de dados incompletos.
- **Expansão do Servidor MCP Nativo (`master-of-foundryvtt-mcp`):**
  - Ferramentas nativas para `create_scene` (com geração de paredes e iluminação), `create_combat`, `create_playlist`, `create_deck` e `create_compendium_pack`.
  - Persistência direta em mundos ativos via sessão GM autenticada.
  - Script auxiliar `generate_macro.py` para injeção pública em lote via macros.
- **Expansão do Catálogo de RPG para +100 Sistemas:**
  - Mapeamento detalhado de sistemas famosos e de nicho em `systems/` com protocolo de descoberta dinâmica paginada no diretório oficial e busca na Loja Oficial do Foundry VTT.
- **Guias Técnicos Especializados:**
  - Documentação de WebSockets, Combat Tracker, Active Effects v14 e linhagem D&D 3.5e/dnd35e.
  - Suporte à CLI oficial `@foundryvtt/foundryvtt-cli` e `fvtt-world-cli` (`guides/cli-tools.md`).

### Changed / Alterado
- **Remoção de Travas de Engenharia Reversa:** Atualização das diretrizes para encorajar análise e inspeção de código e APIs do core e de sistemas para maior precisão no desenvolvimento.
- **Atribuição Oficial nos MCPs:** Flags e metadados padronizados para *"Master of Foundry VTT MCP by Mestre Charles Corrêa - rpg.charlescorrea.com.br"*.
- **Compatibilidade v12–v14 em Tabelas:** Atualizado o tipo de resultado de `RollTable` no MCP para formato string `text` em conformidade com o DataModel moderno.
- **Simetria Bilíngue:** Seções em inglês e português do `SKILL.md` e `systems/README.md` equalizadas de forma 100% espelhada.

---

## [0.8.0-beta] - 2026-09-09

### Added / Adicionado
- **Servidor MCP Nativo e Pontes Externas:**
  - Suporte e templates para `ninjos-foundry-mcp`, `foundryvtt-mcp` e `adambdooley/foundry-vtt-mcp`.
  - Manual de instalação do servidor MCP nativo (`mcp/INSTALLATION.md`).
- **Base de Conhecimento Operacional (`kb/`):**
  - Capítulos 01 a 06 cobrindo Hospedagem, Iluminação/Visão, Atores/Tokens, Rolagens, WebRTC e Compêndios.
- **Guias da API do Foundry v8 a v14:**
  - Documentação estruturada por versão e rotina mensal de atualização (`scripts/update_foundry_docs.py`).
- **Suporte Inicial para mais de 60 Sistemas de RPG:**
  - Organização por categorias em `systems/` cobrindo D20, Storyteller, Horror, YZE, Sci-Fi e Narrativos.

---

## [0.1.0-beta] - 2026-09-09

### Added / Adicionado
- Criação inicial da skill `master-of-foundryvtt` por GM Charles Corrêa.
- Mandatos 1 a 6 estabelecendo version gate, conformidade de licenças, protocolo MCP e recuperação autônoma de erros.
