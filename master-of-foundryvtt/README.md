# Master of Foundry VTT 🎲⚡

> **Comprehensive Foundry Virtual Tabletop Mastery, Development & Architecture Suite**  
> *Suíte Completa de Desenvolvimento, Arquitetura e Mestria em Foundry Virtual Tabletop por GM Charles Corrêa*

---

## 🇺🇸 English

### 📌 Overview
**Master of Foundry VTT** is an end-to-end development, scripting, and rule ingestion suite designed for developers, module creators, and Game Masters running **Foundry Virtual Tabletop**.

It encapsulates official documentation, knowledge base articles, policies, and API references from **Version 8 through Version 14**, providing intelligent assistance for:
- Developing **Game Systems** (`system.json`, TypeDataModels, Custom Sheets).
- Developing **Add-on Modules** (`module.json`, Settings, Sockets, libWrapper, Hooks).
- Scripting advanced **Macros, Rollable Tables, Compendiums, and Active Effects**.
- Ingesting and cross-referencing external RPG rulebooks (Pathfinder 2e, D&D 5e, GURPS, Savage Worlds, Fate, Tormenta20).

---

### 🌐 Official Knowledge Sources & Documentation

| Category | URL |
|---|---|
| **Knowledge Base** | [https://foundryvtt.com/kb/](https://foundryvtt.com/kb/) |
| **Releases & Changelogs** | [https://foundryvtt.com/releases/](https://foundryvtt.com/releases/) |
| **Limited License Agreement** | [https://foundryvtt.com/article/license/](https://foundryvtt.com/article/license/) |
| **AI Policy** | [https://foundryvtt.com/article/ai-policy/](https://foundryvtt.com/article/ai-policy/) |
| **Branding Guidelines** | [https://foundryvtt.com/article/branding/](https://foundryvtt.com/article/branding/) |
| **Privacy Policy** | [https://foundryvtt.com/article/privacy-policy/](https://foundryvtt.com/article/privacy-policy/) |
| **API Version 14** | [https://foundryvtt.com/api/v14/](https://foundryvtt.com/api/v14/) |
| **API Version 13** | [https://foundryvtt.com/api/v13/](https://foundryvtt.com/api/v13/) |
| **API Version 12** | [https://foundryvtt.com/api/v12/](https://foundryvtt.com/api/v12/) |
| **API Version 11** | [https://foundryvtt.com/api/v11/](https://foundryvtt.com/api/v11/) |
| **API Version 10** | [https://foundryvtt.com/api/v10/](https://foundryvtt.com/api/v10/) |
| **API Version 9** | [https://foundryvtt.com/api/v9/](https://foundryvtt.com/api/v9/) |
| **API Version 8** | [https://foundryvtt.com/api/v8/](https://foundryvtt.com/api/v8/) |

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

Ela consolida a base de conhecimento oficial, artigos, termos de licença e referências de API da **Versão 8 até a Versão 14**, oferecendo suporte para:
- Criação de **Sistemas de RPG** (`system.json`, TypeDataModels, Fichas Customizadas).
- Criação de **Módulos Adicionais** (`module.json`, Configurações, Sockets, libWrapper, Hooks).
- Criação de **Macros Avançadas, Tabelas Roláveis, Compêndios e Efeitos Ativos**.
- Ingestão e cruzamento de dados de manuais de RPG (Pathfinder 2e, D&D 5e, GURPS, Savage Worlds, Fate, Tormenta20).

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (`pandoc`, `libreoffice`, `tesseract`), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)
