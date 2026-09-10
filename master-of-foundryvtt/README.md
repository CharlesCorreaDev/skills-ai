# Master of Foundry VTT 🎲⚡

> **Comprehensive Foundry Virtual Tabletop Mastery, Development & Architecture Suite**  
> *Suíte Completa de Desenvolvimento, Arquitetura e Mestria em Foundry Virtual Tabletop por GM Charles Corrêa*

---

## 🇺🇸 English

### 📌 Overview
**Master of Foundry VTT** is an end-to-end development, scripting, and rule ingestion suite designed for developers, module creators, and Game Masters running **Foundry Virtual Tabletop**.

It encapsulates official documentation, knowledge base articles, policies, API references from **Version 8 through Version 14**, Model Context Protocol (MCP) integrations, and architecture guides for over 60 famous RPG systems.

---

### 🌐 Knowledge Sources & Documentation

| Category | Reference / Guides |
|---|---|
| **Model Context Protocol (MCP)** | [`mcp/README.md`](mcp/README.md) (ninjos-foundry-mcp, foundryvtt-mcp, foundry-vtt-mcp) |
| **CLI Tools & Automation** | [`guides/cli-tools.md`](guides/cli-tools.md) (`@foundryvtt/foundryvtt-cli` & `fvtt-world-cli`) |
| **Famous Systems Knowledge Base** | [`systems/README.md`](systems/README.md) (D&D, PF2e, WoD, SWADE, Tormenta20, YZE, GURPS, CoC7, etc.) |
| **Official Systems Directory** | [https://foundryvtt.com/packages/systems](https://foundryvtt.com/packages/systems) |
| **Knowledge Base (Official)** | [`kb/`](kb/) & [https://foundryvtt.com/kb/](https://foundryvtt.com/kb/) |
| **Releases & Changelogs** | [https://foundryvtt.com/releases/](https://foundryvtt.com/releases/) |
| **Limited License Agreement** | [`policies/license.md`](policies/license.md) |
| **AI Policy** | [`policies/ai-policy.md`](policies/ai-policy.md) |
| **Branding Guidelines** | [`policies/branding.md`](policies/branding.md) |
| **Privacy Policy** | [`policies/privacy-policy.md`](policies/privacy-policy.md) |
| **API Version 14** | [`versions/v14-api-guide.md`](versions/v14-api-guide.md) |
| **API Version 13** | [`versions/v13-api-guide.md`](versions/v13-api-guide.md) |
| **API Version 12** | [`versions/v12-api-guide.md`](versions/v12-api-guide.md) |
| **API Version 11** | [`versions/v11-api-guide.md`](versions/v11-api-guide.md) |
| **API Version 10** | [`versions/v10-api-guide.md`](versions/v10-api-guide.md) |
| **API Version 9** | [`versions/v09-api-guide.md`](versions/v09-api-guide.md) |
| **API Version 8** | [`versions/v08-api-guide.md`](versions/v08-api-guide.md) |

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (`pandoc`, `libreoffice`, `tesseract`), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---
---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
O **Master of Foundry VTT** é uma suíte de desenvolvimento, automação e ingestão de regras desenvolvida para desenvolvedores de sistemas, criadores de módulos e Mestres de RPG que utilizam o **Foundry Virtual Tabletop**.

Ela consolida a base de conhecimento oficial, artigos, termos de licença, integrações MCP e referências de API da **Versão 8 até a Versão 14**, oferecendo suporte para:
- Integração com **Servidores MCP** ([`mcp/README.md`](mcp/README.md)) para inspeção em tempo real e teste de macros.
- **Ferramentas de Linha de Comando (CLI)** ([`guides/cli-tools.md`](guides/cli-tools.md)) com `@foundryvtt/foundryvtt-cli` e `fvtt-world-cli` para automação de compêndios e mundos.
- Base de conhecimento arquitetural para **mais de 60 sistemas de RPG** ([`systems/README.md`](systems/README.md)).
- Criação de **Sistemas de RPG** (`system.json`, TypeDataModels, Fichas Customizadas).
- Criação de **Módulos Adicionais** (`module.json`, Configurações, Sockets, libWrapper, Hooks).
- Criação de **Macros Avançadas, Tabelas Roláveis, Compêndios e Efeitos Ativos**.

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir pacotes extras, o agente DEVE solicitar permissão explícita ao desenvolvedor antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar o que foi instalado e configurado e executar um teste de validação.

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)
