# SMS Legal - Integration Suite & Native MCP Server 📱⚡

> **Suite Completa de Integração da API SMS Legal / SMS Gateway & Servidor MCP Nativo**  
> *Desenvolvido para Antigravity IDE, Claude Desktop, Cursor e Agentes de IA Autônomos por Charles Corrêa*  
> **Versão Atual: v1.0.0**

---

## 🇧🇷 Português

### 📌 Visão Geral
A suite **SMS Legal** é uma solução completa para desenvolvedores e agentes de Inteligência Artificial que precisam integrar, disparar e gerenciar mensagens de SMS, agendamentos, chamadas de voz e consultas de operadora utilizando a API oficial do **SMS Legal / SMS Gateway**.

Ela combina:
1. **Servidor MCP Nativo Unificado (`mcp/`)**: Execute envios e consultas diretamente a partir do chat do seu agente no Antigravity, Claude Desktop ou Cursor sem precisar abrir navegador ou terminal.
2. **SDKs Oficiais Multilinguagem (`integrations/`)**: Bibliotecas prontas para produção em **PHP**, **Python** e **Node.js/JavaScript**, todas desenvolvidas com código nativo e **zero dependências externas**.
3. **Assistente de Integração Especialista**: Padrões de arquitetura para Laravel, Flight PHP, WordPress, FastAPI, Django, Express e NestJS com suporte a filas e workers assíncronos.

---

### 🌐 Estrutura de Documentos e Módulos

| Categoria | Arquivo / Diretório | Descrição |
|---|---|---|
| **Skill Principal** | [`SKILL.md`](SKILL.md) | Diretrizes para agentes autônomos, sanitização e boas práticas |
| **Servidor MCP Nativo** | [`mcp/README.md`](mcp/README.md) | Guia de instalação e configuração do servidor MCP JSON-RPC |
| **Implementação MCP Node.js** | [`mcp/sms_legal_mcp_server.js`](mcp/sms_legal_mcp_server.js) | Servidor MCP nativo em Node.js via `stdio` |
| **Implementação MCP Python** | [`mcp/sms_legal_mcp_server.py`](mcp/sms_legal_mcp_server.py) | Servidor MCP nativo em Python 3 via `stdio` |
| **SDK PHP** | [`integrations/SmsLegalClient.php`](integrations/SmsLegalClient.php) | Classe pronta para PHP 7.4 a 8.5+ |
| **SDK Python** | [`integrations/sms_legal_client.py`](integrations/sms_legal_client.py) | Cliente assíncrono/síncrono Python 3.8+ |
| **SDK Node.js** | [`integrations/sms_legal_client.js`](integrations/sms_legal_client.js) | Cliente nativo em JavaScript/TypeScript |
| **Cheatsheet Rápido** | [`cheatsheet.md`](cheatsheet.md) | Tabela de endpoints, parâmetros e códigos de erro |
| **Padrões & Boas Práticas** | [`patterns.md`](patterns.md) | Arquitetura de filas, rate limits e segurança de tokens |
| **Glossário Técnico** | [`glossary.md`](glossary.md) | Termos e definições da API SMS Legal |
| **Histórico de Mudanças** | [`CHANGELOG.md`](CHANGELOG.md) | Registro de versões e adições |
| **Versão** | [`VERSION`](VERSION) | Versão semântica atual |

---

### ⚡ Início Rápido: MCP Server no Antigravity / Claude Desktop

Adicione ao seu `mcp_config.json` ou `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sms-legal": {
      "command": "node",
      "args": [
        "<CAMINHO_PARA_SKILL>/sms-legal/mcp/sms_legal_mcp_server.js"
      ],
      "env": {
        "SMS_LEGAL_TOKEN": "SEU_TOKEN_AQUI"
      }
    }
  }
}
```

---

## 🇺🇸 English

### 📌 Overview
The **SMS Legal Suite** is an all-in-one developer and AI agent toolkit for integrating with the SMS Legal / SMS Gateway API. It features native Model Context Protocol (MCP) servers (Node.js & Python), lightweight native SDKs (PHP, Python, JS), and battle-tested architectural patterns.

### 🚀 Key Features
- **Zero External Dependencies:** Built using native standard libraries across all runtimes.
- **Model Context Protocol (MCP):** Send SMS, schedule messages, check balance and inspect replies directly through AI chat.
- **Strict Data Sanitization:** Automatic phone formatting (`55 + DDD + 9 digits`) and mandatory URL encoding.

