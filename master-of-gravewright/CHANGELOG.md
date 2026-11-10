# Changelog - Master of Gravewright ⚔️🎲

All notable changes to the `master-of-gravewright` skill will be documented in this file.  
*Todas as alterações notáveis na skill `master-of-gravewright` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
- **Skills para Git, SQLite e PostgreSQL:**
  - **PostgreSQL & SQLite (`microsoft/postgres-skills`):** Guia detalhado em [`docs/database-guide.md`](docs/database-guide.md) para migrações do Django ORM, banco de dados local SQLite e suporte a PostgreSQL para servidores com alta concorrência.
  - **Git & GitHub Workflows (`git-pr-workflows` / `github`):** Guia completo em [`docs/git-guide.md`](docs/git-guide.md) para controle de versão, tags SemVer e empacotamento ZIP de extensões.

---

## [0.1.0-beta] - 2026-11-10

### Added / Adicionado
- **Lançamento Oficial da Skill (`v0.1.0-beta`):**
  - Engenharia reversa completa do [Gravewright VTT](https://gravewright.com/) (`Gravewright/gravewright`), o Virtual Tabletop open-source brasileiro construído em Python 3.12+, Astral `uv`, Django 5.x/6.x, Jinja2 e Django Channels (WebSockets).
  - **Script de Diagnóstico & Scaffolder (`scripts/setup_dev_env.py`):** Ferramenta automatizada em Python com comentários bilíngues (EN e pt-BR) para diagnosticar o ambiente de desenvolvimento (Python, uv, Git, SQLite/PostgreSQL) e criar novos módulos de navegador (`browser`) ou extensões de servidor (`django`) com `manifest.json` canônico.
  - **Instalação Mandatória de Skills Companheiras:** Requisito de uso conjunto com `python-dev-expert` (para backend Django/services), `bootstrap-ux-ui-plus` (ergonomia de interfaces e acessibilidade WCAG 2.2 AA) e a dupla `cloudflare/security-audit-skill` & `NVIDIA/auto-ontology`.
  - **Acervo Offline Bilíngue Completo (`docs/en/` e `docs/pt-BR/`):** 50 guias técnicos cobrindo arquitetura, code map, APIs, módulos, frontend, campaign management, clocks, clues, mindmaps, map builder, PDF system, universal VTT (UVTT), runners e ethical porting.
  - Documentação mestra bilíngue em [`README.md`](README.md) e [`SKILL.md`](SKILL.md).

