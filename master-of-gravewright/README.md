# Master of Gravewright VTT ⚔️🎲

> **Reverse Engineering, Systems, Modules, Compendiums, Architecture & Toolchain for Gravewright Virtual Tabletop**  
> *Engenharia Reversa, Sistemas, Módulos, Compêndios, Arquitetura e Ferramental para o Gravewright VTT por GM Charles Corrêa*  
> **Status: Beta (v0.3.0-beta)**

---

## 🇺🇸 English

### 📌 Overview
**Master of Gravewright** is a specialized AI agent skill designed for reverse engineering, configuring development environments, and creating modules, game systems, and compendiums for the **[Gravewright VTT](https://gravewright.com/)** ([GitHub Repository](https://github.com/Gravewright/gravewright)).

Created by Brazilian developer **Rodrigo Tristão Porfírio**, Gravewright is an open-source virtual tabletop built on top of **Python 3.12+**, **Django**, **Jinja2**, **Django Channels (WebSockets)**, and native browser JavaScript.

### 🌟 Core Capabilities
1. **Cross-VTT Reverse Engineering & Adaptation:** Deconstructs third-party systems and modules (Foundry VTT, Roll20, Fantasy Grounds) via REA (`rea-agents`) and maps mechanics into Gravewright's Django services and WebSockets while strictly obeying ethical porting rules.
2. **Automated Environment Diagnosis:** Checks Python 3.12+, Astral `uv`, Git, SQLite and PostgreSQL via `scripts/setup_dev_env.py --check`.
3. **Native Model Context Protocol (MCP) Server:** Features `master-of-gravewright-mcp` (`mcp/gravewright_mcp_server.py`) with 6 tools for environment inspection, module listing, manifest validation, marketplace query, scaffolding, and offline search.
4. **Companion Skills Integration:** Recommends and pairs with `python-dev-expert` for Django backend, `microsoft/postgres-skills` for PostgreSQL/SQLite database engineering, Git workflow skills for release management, `bootstrap-ux-ui-plus` for UI ergonomics, and Cloudflare/NVIDIA for security and truth grounding.
5. **Module Scaffolding:** Generates clean **Browser Modules** (JS/CSS) and **Django App Modules** (Python services/models) adhering to Gravewright's packaging specifications.
6. **Offline Documentation (EN & pt-BR):** 50 offline Markdown guides covering architecture, API endpoints, map builder, clocks, clues, and ethical module porting.

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
A skill **Master of Gravewright** é a suíte de engenharia reversa e desenvolvimento para o **Gravewright VTT** — o Virtual Tabletop open-source brasileiro desenvolvido em Python e Django.

A skill fornece diagnóstico automatizado do ambiente de desenvolvimento, engenharia reversa Cross-VTT para adaptação de módulos do Foundry/Roll20 para o Gravewright, servidor MCP nativo, scaffolding de módulos do zero e todo o conhecimento técnico para criar fichas, regras, automações, compêndios e integrações com bancos de dados (SQLite/PostgreSQL) e versionamento Git.

### 🌟 Principais Recursos
- **Engenharia Reversa Cross-VTT:** Capacidade de analisar sistemas e módulos de outros VTTs (Foundry VTT, Roll20) usando REA (`rea-agents`), desconstruir seus esquemas de dados e regras e adaptá-los com precisão para os domínios nativos do Gravewright (`actors`, `items`, `tokens`, `services.py`), com respeito absoluto às diretrizes de Porte Ético.
- **Verificação Automática do Ambiente:** Diagnóstico de Python 3.12+, Astral `uv`, Git, SQLite e PostgreSQL.
- **Servidor MCP Nativo (`master-of-gravewright-mcp`):** Conecta agentes de IA diretamente ao projeto para inspecionar campanhas, validar manifests e scaffoldar extensões via stdio JSON-RPC 2.0.
- **Skills Companheiras Obrigatórias:** Integração nativa com `python-dev-expert`, `microsoft/postgres-skills` (SQLite/PostgreSQL), workflows Git/GitHub, `bootstrap-ux-ui-plus`, Cloudflare Security Audit e NVIDIA Auto-Ontology.
- **Gerador de Módulos (Scaffolder):** Criação rápida de módulos de navegador ou aplicativos Django com `manifest.json` canônico.
- **Acervo Offline Bilíngue:** Mais de 50 manuais técnicos originais em inglês e português do Brasil para consulta imediata sem consumo de tokens de internet.

---

## 📁 Estrutura de Arquivos / Folder Structure

```
master-of-gravewright/
├── SKILL.md                          # Diretrizes e mandatos mestres para a IA
├── README.md                         # Visão geral completa bilíngue (EN / PT-BR)
├── VERSION                           # Versão semântica atual (0.1.0-beta)
├── CHANGELOG.md                      # Histórico detalhado de versões
├── scripts/
│   └── setup_dev_env.py              # Diagnóstico de ferramentas e scaffolder de módulos
└── docs/                             # Documentação técnica oficial offline
    ├── en/                           # Manuais oficiais em Inglês
    └── pt-BR/                        # Manuais oficiais em Português do Brasil
```

---

## 👨‍💻 Autor / Author
**GM Charles Corrêa**  
- 🌐 Website: [charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 GitHub: [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ Skills AI: [github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)

