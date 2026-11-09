#!/usr/bin/env python3
"""
SMS Legal MCP Server (Model Context Protocol)
Protocol Standard: JSON-RPC 2.0 over stdio
Native implementation using Python 3 standard library (no external dependencies).
"""

import sys
import json
import os
import urllib.request
import urllib.parse
import urllib.error

BASE_URL = "https://v1.smsgateway.com.br/api/"
DEFAULT_TOKEN = os.getenv("SMS_LEGAL_TOKEN", "")

def api_request(endpoint: str, params: dict, method: str = "GET") -> dict:
    token = params.get("token") or DEFAULT_TOKEN
    if not token:
        return {
            "error": True,
            "code": "001",
            "message": "Token não fornecido. Configure a variável SMS_LEGAL_TOKEN ou passe o parâmetro 'token'."
        }

    merged = {k: v for k, v in params.items() if v is not None}
    merged["token"] = token
    query_string = urllib.parse.urlencode(merged)

    headers = {
        "User-Agent": "SMS-Legal-MCP-Python/1.0.0",
        "Accept": "application/json, text/plain, */*"
    }

    try:
        if method.upper() == "GET":
            full_url = f"{BASE_URL}{endpoint}?{query_string}"
            req = urllib.request.Request(full_url, headers=headers, method="GET")
        else:
            full_url = f"{BASE_URL}{endpoint}"
            data_bytes = query_string.encode("utf-8")
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            req = urllib.request.Request(full_url, data=data_bytes, headers=headers, method="POST")

        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8")
            try:
                return json.loads(content)
            except Exception:
                return {"raw": content.strip(), "statusCode": resp.status}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        return {"error": True, "http_status": e.code, "details": err_body}
    except Exception as e:
        return {"error": True, "message": f"Erro de conexão: {str(e)}"}

TOOLS = [
    {
        "name": "sms_enviar_texto",
        "description": "Envia uma mensagem de SMS texto simples para um único número celular através da API SMS Legal.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "Destinatário com DDI + DDD + Número (ex: 5551999999999)."},
                "msg": {"type": "string", "description": "Texto da mensagem (até 160 caracteres por crédito)."},
                "token": {"type": "string", "description": "Opcional. Token de autenticação da API SMS Legal."}
            },
            "required": ["to", "msg"]
        }
    },
    {
        "name": "sms_enviar_lote",
        "description": "Envia a mesma mensagem de SMS para múltiplos números simultâneos (máx 1.000).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "Números separados por vírgula (ex: 5551999887766,5551999887767)."},
                "msg": {"type": "string", "description": "Texto da mensagem em lote."},
                "token": {"type": "string", "description": "Opcional. Token da API."}
            },
            "required": ["to", "msg"]
        }
    },
    {
        "name": "sms_agendar",
        "description": "Agenda o envio de SMS para data/hora futuras no formato DD-MM-AAAA HH:MM:SS.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "Número(s) de destino separados por vírgula."},
                "msg": {"type": "string", "description": "Texto da mensagem."},
                "dtenvio": {"type": "string", "description": "Data e hora no formato: DD-MM-AAAA HH:MM:SS (ex: 25-10-2026 08:45:00)."},
                "token": {"type": "string", "description": "Opcional. Token da API."}
            },
            "required": ["to", "msg", "dtenvio"]
        }
    },
    {
        "name": "sms_consultar_status",
        "description": "Consulta o status de entrega do SMS a partir do IdSMS.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "idsms": {"type": "string", "description": "ID retornado no envio do SMS."},
                "token": {"type": "string", "description": "Opcional. Token da API."}
            },
            "required": ["idsms"]
        }
    },
    {
        "name": "sms_consultar_creditos",
        "description": "Consulta o saldo de créditos SMS disponível na conta.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "token": {"type": "string", "description": "Opcional. Token da API."}
            }
        }
    },
    {
        "name": "sms_consultar_respostas",
        "description": "Captura respostas recebidas dos destinatários das mensagens SMS.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "qt": {"type": "integer", "description": "Quantidade máxima de respostas a capturar (1 a 500). Padrão: 50.", "default": 50},
                "token": {"type": "string", "description": "Opcional. Token da API."}
            }
        }
    },
    {
        "name": "sms_consultar_numero",
        "description": "Verifica a operadora, status de ativação e portabilidade de um número celular.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "nr": {"type": "string", "description": "Número do celular no formato DDI+DDD+Número (ex: 5511998776655)."},
                "token": {"type": "string", "description": "Opcional. Token da API."}
            },
            "required": ["nr"]
        }
    },
    {
        "name": "sms_enviar_voz",
        "description": "Envia mensagem de voz sintetizada (Text-to-Speech) para telefone.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "Número do destinatário."},
                "msg": {"type": "string", "description": "Texto para conversão em voz sintetizada."},
                "from": {"type": "string", "description": "ID do Remetente configurado no painel."},
                "token": {"type": "string", "description": "Opcional. Token da API."}
            },
            "required": ["to", "msg", "from"]
        }
    },
    {
        "name": "sms_enviar_audio",
        "description": "Envia uma chamada telefônica executando áudio pré-gravado.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "Número do destinatário."},
                "idaudio": {"type": "string", "description": "ID do áudio pré-gravado no painel."},
                "from": {"type": "string", "description": "ID do Remetente no painel."},
                "token": {"type": "string", "description": "Opcional. Token da API."}
            },
            "required": ["to", "idaudio", "from"]
        }
    }
]

def call_tool(name: str, args: dict):
    if name == "sms_enviar_texto":
        return api_request("send-sms-texto.php", args, "POST")
    elif name == "sms_enviar_lote":
        return api_request("send-sms-texto-lote.php", args, "POST")
    elif name == "sms_agendar":
        return api_request("agendar-sms.php", args, "POST")
    elif name == "sms_consultar_status":
        return api_request("status.php", args, "GET")
    elif name == "sms_consultar_creditos":
        return api_request("creditos.php", args, "GET")
    elif name == "sms_consultar_respostas":
        return api_request("respostas.php", args, "GET")
    elif name == "sms_consultar_numero":
        return api_request("consultar-numero.php", args, "GET")
    elif name == "sms_enviar_voz":
        return api_request("send-sms-voz.php", args, "POST")
    elif name == "sms_enviar_audio":
        return api_request("send-sms-audio.php", args, "POST")
    else:
        raise ValueError(f"Ferramenta desconhecida: {name}")

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
            continue

        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        try:
            if method == "initialize":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "sms-legal-mcp-python", "version": "1.0.0"}
                    }
                }
            elif method == "notifications/initialized":
                continue
            elif method == "tools/list":
                res = {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}}
            elif method == "tools/call":
                t_name = params.get("name")
                t_args = params.get("arguments", {})
                res_data = call_tool(t_name, t_args)
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [
                            {"type": "text", "text": json.dumps(res_data, indent=2, ensure_ascii=False)}
                        ]
                    }
                }
            elif method == "ping":
                res = {"jsonrpc": "2.0", "id": req_id, "result": {}}
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Método não suportado: {method}"}}
            
            sys.stdout.write(json.dumps(res, ensure_ascii=False) + "\n")
            sys.stdout.flush()
        except Exception as e:
            res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32000, "message": str(e)}}
            sys.stdout.write(json.dumps(res, ensure_ascii=False) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()

