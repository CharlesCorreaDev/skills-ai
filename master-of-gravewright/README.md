# Master of Gravewright VTT ⚔️🎲

> **Reverse Engineering, Systems, Modules, Compendiums, Architecture & Toolchain for Gravewright Virtual Tabletop**  
> *Engenharia Reversa, Sistemas, Módulos, Compêndios, Arquitetura e Ferramental para o Gravewright VTT por GM Charles Corrêa*  
> **Status: Beta (v0.5.0-beta)**

---

## 🇺🇸 English

### 📌 Overview
**Master of Gravewright** is a specialized AI agent skill designed for reverse engineering, configuring development environments, and creating modules, game systems, and compendiums for the **[Gravewright VTT](https://gravewright.com/)** ([GitHub Repository](https://github.com/Gravewright/gravewright)).

Created by Brazilian developer **Rodrigo Tristão Porfírio**, Gravewright is an open-source virtual tabletop built on top of **Python 3.14+**, **Django 6.1**, **Datastar**, **PixiJS**, **Jinja2**, **Django Channels (WebSockets)**, and native browser JavaScript ES Modules with persistent storage in **SQLite** (`data/gravewright.sqlite3`).

### 🌟 Core Capabilities
1. **Official JSON Schema 2020-12 Compliance:** Generates and validates `manifest.json` files matching official packaging schemas with strict property validation, semver `X.Y.Z`, SDK range constraints, and clean root ZIP packaging.
2. **ESM Runtime Lifecycle Integration:** Implements the official client lifecycle (`export default { start, register, stop }`) and registers surfaces (`actor.directory`, `actor.sheet`, `item.sheet`, `scene.overlay`, etc.) with signal-based cleanup.
3. **Django App Extensions:** Scaffolds decoupled Django apps registered dynamically via `manifest.json` (`django.apps`) and `api.systems.register_api` without touching Gravewright core files.
4. **Cross-VTT Reverse Engineering & Ethical Porting:** Deconstructs third-party systems and modules (Foundry VTT, Roll20, Fantasy Grounds) via REA (`rea-agents`) and maps mechanics into Gravewright's system schemas, sheets, and APIs while strictly obeying ethical porting rules.
5. **Automated Environment Diagnosis:** Checks Python 3.14+, Astral `uv`, Git, SQLite and extensions via `scripts/setup_dev_env.py --check`.
6. **Native Model Context Protocol (MCP) Server:** Features `master-of-gravewright-mcp` (`mcp/gravewright_mcp_server.py`) for environment inspection, module listing, manifest validation against Draft 2020-12, marketplace search with canonical package IDs, scaffolding, and offline search.
7. **Offline Documentation (EN & pt-BR):** 50 offline Markdown guides covering architecture, API endpoints, map builder, clocks, clues, and ethical module porting with GPL-3.0 attribution in [NOTICE.md](docs/NOTICE.md).

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
A skill **Master of Gravewright** é a suíte de engenharia reversa e desenvolvimento para o **Gravewright VTT** — o Virtual Tabletop open-source brasileiro desenvolvido em Python e Django.

A skill fornece diagnóstico automatizado do ambiente de desenvolvimento, engenharia reversa Cross-VTT para adaptação de módulos de outros VTTs, servidor MCP nativo, scaffolding de módulos do zero e todo o conhecimento técnico para criar fichas, regras, compêndios e integrações baseadas em SQLite (`data/gravewright.sqlite3`), respeitando os schemas oficiais de manifesto e empacotamento.

### 🌟 Principais Recursos
- **Manifesto e Validação Oficial (JSON Schema 2020-12):** Gera manifestos válidos com `id` no padrão regex `^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)+$`, versão `X.Y.Z` e bloco `sdk`.
- **Ciclo de Vida ESM Oficial:** Módulos de navegador exportam `default { start, register, stop }`, registrando superfícies reativas e limpando assinaturas via `signal`.
- **Extensões Django Desacopladas:** Criação de pacotes de servidor com `AppConfig` e `services.py` usando `api.systems.register_api`, sem alterar o core do VTT.
- **Engenharia Reversa Cross-VTT:** Protocolo para analisar sistemas e módulos de outros VTTs (Foundry VTT, Roll20) usando REA (`rea-agents`) e adaptá-los para os domínios do Gravewright com respeito rigoroso ao Porte Ético.
- **Verificação Automática do Ambiente:** Diagnóstico de Python 3.14+, Astral `uv`, Git e banco de dados SQLite.
- **Servidor MCP Nativo (`master-of-gravewright-mcp`):** Conecta agentes de IA diretamente ao projeto para inspecionar campanhas, validar manifests e scaffoldar extensões via stdio JSON-RPC 2.0.
- **Acervo Offline Bilíngue:** Mais de 50 manuais técnicos originais em inglês e português do Brasil para consulta imediata sem consumo de tokens de internet.

---

## 📁 Estrutura de Arquivos / Folder Structure

```text
master-of-gravewright/
├── SKILL.md                          # Diretrizes e mandatos mestres para a IA
├── README.md                         # Visão geral completa bilíngue (EN / PT-BR)
├── VERSION                           # Versão semântica atual (0.5.0-beta)
├── CHANGELOG.md                      # Histórico detalhado de versões
├── contracts/
│   └── schemas/
│       └── manifest.json             # Schema oficial de manifest do Gravewright (Draft 2020-12)
├── scripts/
│   └── setup_dev_env.py              # Diagnóstico de ferramentas e scaffolder de módulos
├── mcp/
│   ├── gravewright_mcp_server.py     # Core do Servidor MCP em Python (JSON-RPC 2.0 stdio)
│   └── README.md                     # Guia de configuração e ferramentas MCP
├── templates/                        # Templates canônicos (browser-module e django-app-module)
└── docs/                             # Documentação técnica e manuais offline
    ├── NOTICE.md                     # Atribuição legal upstream (Gravewright GPL-3.0-only)
    ├── database-guide.md             # Guia de Banco de Dados: SQLite & Migrações
    ├── git-guide.md                  # Guia de Versionamento Git e Empacotamento ZIP
    ├── reverse-engineering-cross-vtt.md # Guia de Engenharia Reversa Cross-VTT
    ├── en/                           # 25 manuais oficiais em Inglês
    └── pt-BR/                        # 25 manuais oficiais em Português do Brasil
```

---

## 👨‍💻 Autor / Author
**GM Charles Corrêa**  
- 🌐 Website: [charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 GitHub: [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ Skills AI: [github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)
