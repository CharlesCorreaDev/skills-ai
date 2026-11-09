---
name: sms-legal
description: Suite completa e assistente de integração da API SMS Legal / SMS Gateway com MCP Server nativo unificado (Node.js/Python), SDKs em PHP, Python e JavaScript, documentação de endpoints, envio em lote, agendamento, voz, áudio, consulta de créditos e captura de respostas. Use quando o usuário quiser enviar SMS, integrar SMS Legal em qualquer sistema ou linguagem, consultar saldo/status de envio ou configurar o servidor MCP no Antigravity, Claude Code, Cursor, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA ou Ollama.
---

# SMS Legal - Suite de Integração & MCP Nativo 📱⚡
> *Criado para Antigravity IDE, Claude Desktop, Cursor e Agentes de IA Autônomos*  
> *Base Oficial: SMS Legal / SMS Gateway API (v1)*

---

## 📌 Missão & Atuação do Agente

A skill **SMS Legal** capacita agentes de IA a atuar como **Engenheiro Especialista de Integração** e **Operador Automatizado de Mensageria SMS**. Ela fornece:
1. **Servidor MCP Nativo Unificado (`sms-legal-mcp`)** em Node.js e Python para disparo, agendamento e consulta de SMS diretamente pelo chat de IA.
2. **SDKs e Clientes Nativos** prontos para produção em **PHP**, **Python** e **Node.js/JavaScript**.
3. **Assistente de Integração Multilinguagem:** Suporte a PHP (Laravel, Symfony, WordPress, nativo), Python (FastAPI, Django, Flask), Node.js/TypeScript (NestJS, Express), C#/.NET, Java e Go.
4. **Resolução Rápida de Erros:** Diagnóstico instantâneo de códigos da API (`000` a `011`) e boas práticas de codificação URL e proteção contra bloqueio por links.

---

## 🚨 Diretrizes Obrigatórias para o Agente de IA

Sempre que o usuário solicitar qualquer tarefa envolvendo envio de SMS ou integração com a API SMS Legal, siga estas diretrizes:

### 1. Higienização e Validação do Número Destino
- Telefone sempre no formato numérico puro: **DDI (55) + DDD + Número** (ex: `5551999999999` ou `5511988887777`).
- Remova automaticamente espaços, parênteses, pontos e traços (`\D+`).
- Alerte o usuário caso o DDD ou o DDI estejam ausentes.

### 2. URL Encoding Obrigatório
- Todos os textos de mensagens (`msg`) devem ser codificados com `urlencode` (PHP), `urllib.parse.quote` (Python), `encodeURIComponent` (Node.js) ou equivalente, para evitar perda de acentos, quebra de linha ou quebra por espaços.

### 3. Gerenciamento Seguro do Token
- Oriente o usuário a **nunca colocar o token no código front-end** (browser).
- Configure a variável de ambiente `SMS_LEGAL_TOKEN` para o servidor MCP ou no arquivo `.env` da aplicação.

### 4. Suporte Ativo a Integrações em Qualquer Stack
Quando o usuário pedir ajuda para integrar a SMS Legal em sua aplicação:
- Pergunte qual é a stack do projeto (PHP, Python, Node, C#, Java, etc.) ou detecte-a nos arquivos do workspace.
- Forneça a classe client pronta, controllers de exemplo e instruções de tratamento de erro.
- Se for envio em lote, lembre do limite de **1.000 números por requisição**.
- Se a mensagem tiver links ou URLs, alerte que a conta precisa ter essa permissão liberada pelo suporte técnico da SMS Legal (código `006`).

---

## 🛠️ Servidor MCP Nativo (`sms-legal`)

O servidor MCP nativo está disponível em dois runtimes sem dependências externas:
- **Node.js**: [`mcp/sms_legal_mcp_server.js`](mcp/sms_legal_mcp_server.js)
- **Python 3**: [`mcp/sms_legal_mcp_server.py`](mcp/sms_legal_mcp_server.py)

### Ferramentas Expostas pelo MCP:
- `sms_enviar_texto`: Envio de SMS texto para 1 número (`to`, `msg`, `token?`).
- `sms_enviar_lote`: Envio em lote com múltiplos números separados por vírgula (`to`, `msg`, `token?`).
- `sms_agendar`: Agendamento de envio (`to`, `msg`, `dtenvio`, `token?`).
- `sms_consultar_status`: Consulta de status de entrega (`idsms`, `token?`).
- `sms_consultar_creditos`: Consulta de saldo de créditos disponíveis (`token?`).
- `sms_consultar_respostas`: Captura respostas de clientes / replies (`qt?`, `token?`).
- `sms_consultar_numero`: Consulta operadora, portabilidade e status ativo (`nr`, `token?`).
- `sms_enviar_voz`: Envio de mensagem de voz sintetizada TTS (`to`, `msg`, `from`, `token?`).
- `sms_enviar_audio`: Ligação telefônica com áudio pré-gravado (`to`, `idaudio`, `from`, `token?`).

### Como Ativar no `mcp_config.json`:
```json
{
  "mcpServers": {
    "sms-legal": {
      "command": "node",
      "args": ["<CAMINHO_PARA_SKILL>/sms-legal/mcp/sms_legal_mcp_server.js"],
      "env": {
        "SMS_LEGAL_TOKEN": "SEU_TOKEN_AQUI"
      }
    }
  }
}
```

---

## 📚 Documentos e Recursos de Referência

- [Manual do MCP Nativo](mcp/README.md)
- [Cheatsheet de Endpoints e Erros](cheatsheet.md)
- [Padrões Arquiteturais e Boas Práticas](patterns.md)
- [Glossário de Termos](glossary.md)
- [SDK PHP Nativo](integrations/SmsLegalClient.php)
- [SDK Python Nativo](integrations/sms_legal_client.py)
- [SDK Node.js / JavaScript Nativo](integrations/sms_legal_client.js)

