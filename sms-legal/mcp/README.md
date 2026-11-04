# Guia de Instalação e Configuração do MCP Nativo SMS Legal 📱⚡
> *Parte da suite SMS-Legal por GM Charles Corrêa*

O **Servidor MCP SMS Legal** permite que agentes de Inteligência Artificial (Antigravity IDE, Claude Desktop, Cursor, Copilot CLI, Hermes Agent, Ollama) executem envio de SMS, agendamentos, verificação de status e consulta de saldo de créditos diretamente no chat.

Disponibilizamos **duas implementações nativas** (zero dependências externas):
1. **Node.js** (`sms_legal_mcp_server.js`) - Rápido, leve e nativo.
2. **Python 3** (`sms_legal_mcp_server.py`) - Nativo com urllib e padrão de biblioteca oficial.

---

## 🛠️ Ferramentas Disponíveis no MCP

| Tool MCP | Endpoint | Descrição |
| :--- | :--- | :--- |
| `sms_enviar_texto` | `send-sms-texto.php` | Envia SMS texto simples para um número. |
| `sms_enviar_lote` | `send-sms-texto-lote.php` | Envia SMS para múltiplos números (separados por vírgula). |
| `sms_agendar` | `agendar-sms.php` | Agenda envio para data/hora futura (`DD-MM-AAAA HH:MM:SS`). |
| `sms_consultar_status` | `status.php` | Consulta status de entrega a partir do `IdSMS`. |
| `sms_consultar_creditos`| `creditos.php` | Consulta saldo de créditos da conta. |
| `sms_consultar_respostas`| `respostas.php`| Consulta respostas recebidas dos clientes (replies). |
| `sms_consultar_numero` | `consultar-numero.php` | Valida portabilidade, operadora e se o número está ativo. |
| `sms_enviar_voz` | `send-sms-voz.php` | Dispara chamada com áudio sintetizado TTS. |
| `sms_enviar_audio` | `send-sms-audio.php` | Dispara chamada reproduzindo áudio pré-gravado. |

---

## ⚙️ Configurações Prontas

### 1. Antigravity IDE / Claude Desktop (`mcp_config.json` ou `claude_desktop_config.json`)

#### Opção A: Executando via Node.js (Recomendado)
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

#### Opção B: Executando via Python 3
```json
{
  "mcpServers": {
    "sms-legal": {
      "command": "python",
      "args": [
        "<CAMINHO_PARA_SKILL>/sms-legal/mcp/sms_legal_mcp_server.py"
      ],
      "env": {
        "SMS_LEGAL_TOKEN": "SEU_TOKEN_AQUI"
      }
    }
  }
}
```

---

## 🔒 Variáveis de Ambiente e Segurança
- `SMS_LEGAL_TOKEN`: Token obtido no painel do cliente SMS Legal (`https://smslegal.com.br` ou `https://smsgateway.com.br`).
- Se preferir não fixar na variável de ambiente, você pode fornecer o `token` diretamente como parâmetro ao chamar qualquer ferramenta do MCP.

