# Changelog - Master of Gravewright ⚔️🎲

All notable changes to the `master-of-gravewright` skill will be documented in this file.  
*Todas as alterações notáveis na skill `master-of-gravewright` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.4.0-beta] - 2026-11-13

### Fixed / Corrigido (Addressing GitHub Issue #6)
- **Manifesto Oficial (`manifest.json`) em Conformidade com JSON Schema 2020-12:**
  - Corrigido schema canônico em `SKILL.md`, `templates/`, `scripts/setup_dev_env.py` e `mcp/gravewright_mcp_server.py`.
  - Removidos campos inválidos (`title`, `compatibility`, `scripts`, `styles`, `django_app`).
  - Adicionados campos obrigatórios: `name`, `sdk` (com `requires` e `tested`), e `entry` (para módulos de navegador/sistema).
  - Sanitização de `id` para respeitar a regex oficial `^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)+$`.
  - Validação estrita de `version` no formato numérico semântico `X.Y.Z`.
- **Ciclo de Vida do Runtime JS (`module-runtime.js`):**
  - O entrypoint JavaScript nos templates e scaffolder agora exporta `default { start, register, stop }` em formato ES Module.
  - Carregamento de CSS isolado via `styles.use("styles.css")` em vez de declaração no manifest.
  - Registro de superfícies reativas (`actor.directory`, `actor.sheet`, etc.) com descarte via `signal`.
- **Scaffolding de Extensões Django (`django.apps`):**
  - Bloco `"django": { "apps": ["pacote_server.apps.PacoteServerConfig"], "requirements": [] }` aderente ao schema oficial.
  - Geração de pacote Python válido com identificador sanitizado (substituindo `-` por `_`), `apps.py` com `AppConfig`, `models.py`, `services.py` e `migrations/__init__.py`.
  - Registro de APIs de sistema públicas via `api.systems.register_api` em `AppConfig.ready()`.
- **Empacotamento e Controle de Versão Git (`docs/git-guide.md`):**
  - Ajustado fluxo de empacotamento: `manifest.json` na raiz do arquivo ZIP sem pastas envoltórias intermediárias.
  - Substituição de `LICENSE` sem extensão por `LICENSE.txt` (extensões aceitas pelo validador do Gravewright).
  - Exclusão de arquivos ocultos (`.gitignore`, `.git/`, `.DS_Store`) do arquivo ZIP.
- **Servidor MCP Nativo (`master-of-gravewright-mcp`):**
  - Validador `validate_module_manifest` atualizado para validar contra o JSON Schema Draft 2020-12 oficial.
  - `list_installed_modules` agora verifica `data/media/modules/packages/` ou `GRAVEWRIGHT_MODULES_ROOT` e identifica corretamente pacotes `browser`, `django`, `system` e `translation`.
  - Atualizados IDs do catálogo marketplace para IDs canônicos (`gravewright-3d-dice` e `gravewright.5e-srd`).
  - Proteção contra path traversal em `scaffold_extension`.
  - Retorno de erros funcionais com `isError: true` no protocolo MCP.
- **Banco de Dados SQLite Exclusivo (`docs/database-guide.md`):**
  - Removidas menções a PostgreSQL, `DATABASE_URL` e `dj_database_url` (não suportados no core do Gravewright).
  - Documentado uso de SQLite em `data/gravewright.sqlite3` com transações `IMMEDIATE`.
  - Documentação de migrações para modelos de extensões Django.
- **Guia de Engenharia Reversa Cross-VTT (`docs/reverse-engineering-cross-vtt.md`):**
  - Ajustada orientação: todo sistema e regra deve ser empacotado como extensão/sistema instalado sem alterar o core do Gravewright.
  - Mapeamento correto de `actor.sheet` (com substituição de interface e controle otimista de revisão `expectedRevision`), `system.combat` e `api.systems.register_api`.
- **Suporte a Code Mode e Gestão de SQLite:**
  - Adicionada a ferramenta `code_mode` no servidor MCP (`gravewright_mcp_server.py`) com execução em sandbox Python expondo o namespace `gw.*`.
  - Criado o utilitário `scripts/manage_sqlite.py` para inspeção segura de esquemas, consultas JSON e backups pré-mutação.
  - Atualizado `docs/database-guide.md` com protocolos de autorização obrigatória pré-mutação e concorrência SQLite em modo WAL.
- **Stack Atualizada e Aviso Legal de Upstream:**
  - Stack atualizada para Python 3.14+, Django 6.1, Datastar e PixiJS em consonância com o Gravewright 0.3.4.
  - Criado [`docs/NOTICE.md`](docs/NOTICE.md) com atribuição explícita de direitos e cópia sob licença GPL-3.0-only do projeto Gravewright de Rodrigo Tristão Porfírio.
  - Removido caminho absoluto hardcoded no `mcp/README.md`.

---

## [0.3.0-beta] - 2026-11-10

### Added / Adicionado
- **Engenharia Reversa Cross-VTT & Adaptação de Módulos (Foundry/Roll20 ➔ Gravewright):**
  - Implementado protocolo de engenharia reversa via `rea-agents` para desconstruir sistemas, DataModels e regras de outros VTTs e adaptá-los para o ecossistema Django/WebSockets do Gravewright.
  - Criado o [Guia de Engenharia Reversa e Adaptação Cross-VTT](docs/reverse-engineering-cross-vtt.md) com tabela comparativa completa de conceitos (Foundry vs Gravewright), desconstrução em 4 fases e integração com o Porte Ético.

---

## [0.2.0-beta] - 2026-11-10

### Added / Adicionado
- **Servidor MCP Nativo Oficial (`master-of-gravewright-mcp`):**
  - Implementação completa em Python zero-dependency (`mcp/gravewright_mcp_server.py`) operando via protocolo JSON-RPC 2.0 (stdio).
  - 6 ferramentas expostas para Agentes de IA: `inspect_gravewright_environment`, `list_installed_modules`, `validate_module_manifest`, `query_marketplace_packages`, `scaffold_extension` e `search_offline_docs`.
  - Documentação e manual de configuração para clientes MCP em [`mcp/README.md`](mcp/README.md).

---

## [0.1.0-beta] - 2026-11-10

### Added / Adicionado
- **Lançamento Oficial da Skill (`v0.1.0-beta`):**
  - Engenharia reversa completa do [Gravewright VTT](https://gravewright.com/) (`Gravewright/gravewright`), o Virtual Tabletop open-source brasileiro construído em Python 3.12+, Astral `uv`, Django 5.x/6.x, Jinja2 e Django Channels (WebSockets).
  - **Script de Diagnóstico & Scaffolder (`scripts/setup_dev_env.py`):** Ferramenta automatizada em Python com comentários bilíngues (EN e pt-BR) para diagnosticar o ambiente de desenvolvimento e criar novos módulos.
  - **Acervo Offline Bilíngue Completo (`docs/en/` e `docs/pt-BR/`):** 50 guias técnicos cobrindo arquitetura, code map, APIs, módulos, frontend, campaign management, clocks, clues, mindmaps, map builder, PDF system, universal VTT (UVTT), runners e ethical porting.
