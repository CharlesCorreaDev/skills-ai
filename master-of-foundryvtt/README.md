# Master of Foundry VTT 🎲⚡

> **Comprehensive Foundry Virtual Tabletop Mastery, Development & Architecture Suite**  
> *Suíte Completa de Desenvolvimento, Arquitetura e Mestria em Foundry Virtual Tabletop por GM Charles Corrêa*  
> **Current up to Foundry VTT v14.369 Stable**

---

## 🇺🇸 English

### 📌 Overview & Practical Authority
**Master of Foundry VTT** is an end-to-end development, scripting, and rule ingestion suite designed for developers, module creators, and Game Masters running **Foundry Virtual Tabletop**.

> [!IMPORTANT]
> **Source Material & Real-World Experience:**  
> All information, architectural patterns, and troubleshooting guides in this repository are rigorously based on **official Foundry VTT documentation, official release notes, policies, and API references**, combined directly with **first-hand, battle-tested practical experience in developing custom modules and systems for Foundry VTT (including the latest v14 architecture, ApplicationV2, and TypeDataModels)**.

This suite encapsulates official documentation, knowledge base articles, policies, API references from **Version 8 through Version 14**, Model Context Protocol (MCP) integrations, modern web exploration tools for module repositories, and architecture guides for over 60 famous RPG systems.

---

### 🌐 Knowledge Sources & Documentation

| Category | Reference / Guides |
|---|---|
| **Model Context Protocol (MCP)** | [`mcp/README.md`](mcp/README.md) (ninjos-foundry-mcp, foundryvtt-mcp, foundry-vtt-mcp) |
| **CLI Tools & Automation** | [`guides/cli-tools.md`](guides/cli-tools.md) (`@foundryvtt/foundryvtt-cli` & `fvtt-world-cli`) |
| **Famous Systems Knowledge Base** | [`systems/README.md`](systems/README.md) (D&D, PF2e, WoD, SWADE, Tormenta20, YZE, GURPS, CoC7, etc.) |
| **Official Systems Directory** | [https://foundryvtt.com/packages/systems](https://foundryvtt.com/packages/systems) |
| **Knowledge Base (Official & Guides)** | [`kb/`](kb/) & [https://foundryvtt.com/kb/](https://foundryvtt.com/kb/) |
| **SSL, HTTPS & Let's Encrypt (v14+)** | [`kb/07-ssl-and-https.md`](kb/07-ssl-and-https.md) (Native SSL in v14.369 vs Reverse Proxy) |
| **Releases & Changelogs** | [https://foundryvtt.com/releases/](https://foundryvtt.com/releases/) |
| **Limited License Agreement** | [`policies/license.md`](policies/license.md) |
| **AI Policy** | [`policies/ai-policy.md`](policies/ai-policy.md) |
| **Branding Guidelines** | [`policies/branding.md`](policies/branding.md) |
| **Privacy Policy** | [`policies/privacy-policy.md`](policies/privacy-policy.md) |
| **API Version 14 (Latest)** | [`versions/v14-api-guide.md`](versions/v14-api-guide.md) |
| **API Version 13** | [`versions/v13-api-guide.md`](versions/v13-api-guide.md) |
| **API Version 12** | [`versions/v12-api-guide.md`](versions/v12-api-guide.md) |
| **API Version 11** | [`versions/v11-api-guide.md`](versions/v11-api-guide.md) |
| **API Version 10** | [`versions/v10-api-guide.md`](versions/v10-api-guide.md) |
| **API Version 9** | [`versions/v09-api-guide.md`](versions/v09-api-guide.md) |
| **API Version 8** | [`versions/v08-api-guide.md`](versions/v08-api-guide.md) |

---

### 🔍 Repository Inspection & Analysis Web Tools
For studying third-party systems and modules directly in the browser or via automated ingestion:

| Tool | URL Template | Example (Foundry D&D 5e / SWADE Tools) |
|---|---|---|
| **Gitingest** | `https://gitingest.com/{{owner}}/{{repo}}` | `https://gitingest.com/foundryvtt/dnd5e` |
| **GitDiagram** | `https://gitdiagram.com/{{owner}}/{{repo}}` | `https://gitdiagram.com/foundryvtt/dnd5e` |
| **Repomix** | `https://repomix.com/?repo={{owner}}/{{repo}}` | `https://repomix.com/?repo=lipefl/swade-tools` |
| **Uithub** | `https://uithub.com/{{owner}}/{{repo}}?maxTokens=500000` | `https://uithub.com/lipefl/swade-tools?maxTokens=500000` |
| **DeepWiki** | `https://deepwiki.com/{{owner}}/{{repo}}` | `https://deepwiki.com/lipefl/swade-tools` |
| **Star History** | `https://www.star-history.com/?type=date&repos={{owner}}/{{repo}}` | `https://www.star-history.com/?type=date&repos=foundryvtt/dnd5e` |

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (`pandoc`, `libreoffice`, `tesseract`), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---
---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral e Experiência Prática
O **Master of Foundry VTT** é uma suíte completa de desenvolvimento, automação, ingestão de regras e arquitetura desenvolvida para desenvolvedores de sistemas, criadores de módulos e Mestres de RPG que utilizam o **Foundry Virtual Tabletop**.

> [!IMPORTANT]
> **Base Oficial e Experiência Prática Real:**  
> Todas as informações, arquiteturas, padrões de código e diretrizes contidas neste repositório são rigorosamente fundamentadas na **documentação oficial do Foundry VTT, notas oficiais de lançamento, diretrizes/políticas e referências de API**, somadas diretamente à **experiência prática acumulada no desenvolvimento ativo de módulos e sistemas para o Foundry VTT v14** (incluindo o novo paradigma `ApplicationV2`, `TypeDataModel`, arquitetura de canvas e ESM nativo).

Ela consolida a base de conhecimento oficial, artigos, termos de licença, integrações MCP e referências de API da **Versão 8 até a Versão 14 (v14.369 Stable)**, oferecendo suporte para:
- Integração com **Servidores MCP** ([`mcp/README.md`](mcp/README.md)) para inspeção em tempo real e teste de macros.
- **Ferramentas de Linha de Comando (CLI)** ([`guides/cli-tools.md`](guides/cli-tools.md)) com `@foundryvtt/foundryvtt-cli` e `fvtt-world-cli` para compilação e automação de compêndios e mundos.
- Base de conhecimento arquitetural para **mais de 60 sistemas de RPG** ([`systems/README.md`](systems/README.md)).
- Criação e migração de **Sistemas de RPG** (`system.json`, `TypeDataModel`, Fichas Customizadas em `ApplicationV2`).
- Criação de **Módulos Adicionais** (`module.json`, Configurações, Sockets, libWrapper, Hooks).
- Guia nativo de **SSL, HTTPS e Let's Encrypt** ([`kb/07-ssl-and-https.md`](kb/07-ssl-and-https.md)) introduzido na v14.369.
- Ferramentas web para inspeção e estudo reverso de código de repositórios do ecossistema.

---

### 🔍 Ferramentas Web para Análise de Repositórios e Módulos
Ferramentas úteis para estudar a arquitetura de sistemas e módulos existentes diretamente no navegador:

| Ferramenta | Template de URL | Exemplo de Uso (D&D 5e / SWADE Tools) |
|---|---|---|
| **Gitingest** | `https://gitingest.com/{{owner}}/{{repo}}` | `https://gitingest.com/foundryvtt/dnd5e` |
| **GitDiagram** | `https://gitdiagram.com/{{owner}}/{{repo}}` | `https://gitdiagram.com/foundryvtt/dnd5e` |
| **Repomix** | `https://repomix.com/?repo={{owner}}/{{repo}}` | `https://repomix.com/?repo=lipefl/swade-tools` |
| **Uithub** | `https://uithub.com/{{owner}}/{{repo}}?maxTokens=500000` | `https://uithub.com/lipefl/swade-tools?maxTokens=500000` |
| **DeepWiki** | `https://deepwiki.com/{{owner}}/{{repo}}` | `https://deepwiki.com/lipefl/swade-tools` |
| **Star History** | `https://www.star-history.com/?type=date&repos={{owner}}/{{repo}}` | `https://www.star-history.com/?type=date&repos=foundryvtt/dnd5e` |

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir pacotes extras (`pandoc`, `libreoffice`, `tesseract`, pacotes globais ou chaves de API), o agente DEVE solicitar permissão explícita ao desenvolvedor antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar o que foi instalado e configurado e executar um teste de validação.

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)
