# Master of Gravewright VTT ⚔️🎲

> **Reverse Engineering, Systems, Modules, Compendiums, Architecture & Toolchain for Gravewright Virtual Tabletop**  
> *Engenharia Reversa, Sistemas, Módulos, Compêndios, Arquitetura e Ferramental para o Gravewright VTT por GM Charles Corrêa*  
> **Status: Beta (v0.1.0-beta)**

---

## 🇺🇸 English

### 📌 Overview
**Master of Gravewright** is a specialized AI agent skill designed for reverse engineering, configuring development environments, and creating modules, game systems, and compendiums for the **[Gravewright VTT](https://gravewright.com/)** ([GitHub Repository](https://github.com/Gravewright/gravewright)).

Created by Brazilian developer **Rodrigo Tristão Porfírio**, Gravewright is an open-source virtual tabletop built on top of **Python 3.12+**, **Django**, **Jinja2**, **Django Channels (WebSockets)**, and native browser JavaScript.

### 🌟 Core Capabilities
1. **Automated Environment Diagnosis:** Checks Python 3.12+, Astral `uv`, Git, and runtime tools via `scripts/setup_dev_env.py --check`.
2. **Companion Skills Integration:** Recommends and pairs with `python-dev-expert` for Django backend work, `bootstrap-ux-ui-plus` for UI ergonomics, and Cloudflare/NVIDIA for security and truth grounding.
3. **Module Scaffolding:** Generates clean **Browser Modules** (JS/CSS) and **Django App Modules** (Python services/models) adhering to Gravewright's packaging specifications.
4. **Offline Documentation (EN & pt-BR):** 50 offline Markdown guides covering architecture, API endpoints, map builder, clocks, clues, and ethical module porting.

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
A skill **Master of Gravewright** é a suíte de engenharia reversa e desenvolvimento para o **Gravewright VTT** — o Virtual Tabletop open-source brasileiro desenvolvido em Python e Django.

A skill fornece diagnóstico automatizado do ambiente de desenvolvimento, scaffolding de módulos do zero e todo o conhecimento técnico para criar fichas, regras, automações, compêndios e integrações.

### 🌟 Principais Recursos
- **Verificação Automática do Ambiente:** Diagnóstico de Python 3.12+, Astral `uv`, Git e bibliotecas locais.
- **Skills Companheiras:** Integração nativa com `python-dev-expert`, `bootstrap-ux-ui-plus`, Cloudflare Security Audit e NVIDIA Auto-Ontology.
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
