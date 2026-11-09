#!/usr/bin/env node
/**
 * SMS Legal MCP Server (Model Context Protocol)
 * Protocol Standard: JSON-RPC 2.0 over stdio
 * Native implementation using Node.js without external dependencies.
 */

const https = require('https');
const http = require('http');
const readline = require('readline');

const BASE_URL = 'https://v1.smsgateway.com.br/api/';
const DEFAULT_TOKEN = process.env.SMS_LEGAL_TOKEN || '';

/**
 * Utility to make HTTP GET/POST requests to SMS Legal API
 */
function apiRequest(endpoint, params = {}, method = 'GET') {
  return new Promise((resolve, reject) => {
    const token = params.token || DEFAULT_TOKEN;
    if (!token) {
      resolve({
        error: true,
        code: '001',
        message: 'Token não fornecido. Configure a variável de ambiente SMS_LEGAL_TOKEN ou passe o parâmetro "token".'
      });
      return;
    }

    const mergedParams = { ...params, token };
    const searchParams = new URLSearchParams();

    for (const [key, value] of Object.entries(mergedParams)) {
      if (value !== undefined && value !== null) {
        searchParams.append(key, String(value));
      }
    }

    let urlStr = `${BASE_URL}${endpoint}`;
    let requestOptions = {
      method: method.toUpperCase(),
      headers: {
        'User-Agent': 'SMS-Legal-MCP-Server/1.0.0',
        'Accept': 'application/json, text/plain, */*'
      },
      timeout: 30000
    };

    if (method.toUpperCase() === 'GET') {
      urlStr += `?${searchParams.toString()}`;
    } else {
      const postBody = searchParams.toString();
      requestOptions.headers['Content-Type'] = 'application/x-www-form-urlencoded';
      requestOptions.headers['Content-Length'] = Buffer.byteLength(postBody);
    }

    const urlObj = new URL(urlStr);
    const transport = urlObj.protocol === 'https:' ? https : http;

    const req = transport.request(urlObj, requestOptions, (res) => {
      let rawData = '';
      res.setEncoding('utf8');

      res.on('data', (chunk) => {
        rawData += chunk;
      });

      res.on('end', () => {
        try {
          const parsed = JSON.parse(rawData);
          resolve(parsed);
        } catch (e) {
          // If response is not JSON or is plain string
          resolve({
            raw: rawData.trim(),
            statusCode: res.statusCode
          });
        }
      });
    });

    req.on('error', (err) => {
      resolve({
        error: true,
        message: `Falha na requisição de rede: ${err.message}`
      });
    });

    req.on('timeout', () => {
      req.destroy();
      resolve({
        error: true,
        message: 'Timeout ao conectar com a API SMS Legal (30s)'
      });
    });

    if (method.toUpperCase() === 'POST') {
      req.write(searchParams.toString());
    }

    req.end();
  });
}

// Tool definitions for MCP
const TOOLS = [
  {
    name: 'sms_enviar_texto',
    description: 'Envia uma mensagem de SMS texto simples para um único número celular através da API SMS Legal.',
    inputSchema: {
      type: 'object',
      properties: {
        to: {
          type: 'string',
          description: 'Número de telefone no padrão DDI + DDD + Número (ex: 5551999999999 ou 5511988887777).'
        },
        msg: {
          type: 'string',
          description: 'Texto da mensagem SMS (até 160 caracteres por crédito).'
        },
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal (se omitido, usará o SMS_LEGAL_TOKEN do ambiente).'
        }
      },
      required: ['to', 'msg']
    }
  },
  {
    name: 'sms_enviar_lote',
    description: 'Envia a mesma mensagem de SMS para múltiplos números simultâneos (separados por vírgula, máx 1.000).',
    inputSchema: {
      type: 'object',
      properties: {
        to: {
          type: 'string',
          description: 'Números separados por vírgula (ex: 5551999887766,5551999887767).'
        },
        msg: {
          type: 'string',
          description: 'Texto da mensagem que será entregue a todos os destinatários.'
        },
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal.'
        }
      },
      required: ['to', 'msg']
    }
  },
  {
    name: 'sms_agendar',
    description: 'Agenda o envio de uma mensagem SMS para uma data e hora específicas no futuro.',
    inputSchema: {
      type: 'object',
      properties: {
        to: {
          type: 'string',
          description: 'Número ou números separados por vírgula (máximo 1.000).'
        },
        msg: {
          type: 'string',
          description: 'Texto da mensagem a ser agendada.'
        },
        dtenvio: {
          type: 'string',
          description: 'Data e hora do envio no formato estrito "DD-MM-AAAA HH:MM:SS" (ex: 25-10-2026 08:45:00).'
        },
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal.'
        }
      },
      required: ['to', 'msg', 'dtenvio']
    }
  },
  {
    name: 'sms_consultar_status',
    description: 'Consulta o status de entrega detalhado de um SMS enviado utilizando o IdSMS.',
    inputSchema: {
      type: 'object',
      properties: {
        idsms: {
          type: 'string',
          description: 'ID retornado pela API no momento do envio (ex: R010000A789AFD2E5CCFBEC6137AB525105P5G).'
        },
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal.'
        }
      },
      required: ['idsms']
    }
  },
  {
    name: 'sms_consultar_creditos',
    description: 'Verifica o saldo atual de créditos SMS disponíveis na conta SMS Legal.',
    inputSchema: {
      type: 'object',
      properties: {
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal.'
        }
      }
    }
  },
  {
    name: 'sms_consultar_respostas',
    description: 'Captura as respostas (replies bidirecionais) enviadas pelos destinatários para suas mensagens SMS.',
    inputSchema: {
      type: 'object',
      properties: {
        qt: {
          type: 'number',
          description: 'Quantidade de respostas a retornar (de 1 até no máximo 500). Padrão: 50.',
          default: 50
        },
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal.'
        }
      }
    }
  },
  {
    name: 'sms_consultar_numero',
    description: 'Consulta operadora atual, portabilidade e status de ativação de um número de celular.',
    inputSchema: {
      type: 'object',
      properties: {
        nr: {
          type: 'string',
          description: 'Número de celular no formato DDI+DDD+Número (ex: 5511998776655).'
        },
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal.'
        }
      },
      required: ['nr']
    }
  },
  {
    name: 'sms_enviar_voz',
    description: 'Envia mensagem de voz sintetizada (TTS - Text to Speech) para ligação telefônica.',
    inputSchema: {
      type: 'object',
      properties: {
        to: {
          type: 'string',
          description: 'Número de telefone de destino (ex: 5551999999999).'
        },
        msg: {
          type: 'string',
          description: 'Texto que será lido pela voz sintética durante a ligação.'
        },
        from: {
          type: 'string',
          description: 'ID do Remetente cadastrado no painel ("Todos Números" > coluna "ID API").'
        },
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal.'
        }
      },
      required: ['to', 'msg', 'from']
    }
  },
  {
    name: 'sms_enviar_audio',
    description: 'Dispara uma chamada telefônica executando um áudio pré-gravado na plataforma.',
    inputSchema: {
      type: 'object',
      properties: {
        to: {
          type: 'string',
          description: 'Número de destino (ex: 5551999999999).'
        },
        idaudio: {
          type: 'string',
          description: 'ID do arquivo de áudio pré-gravado (consultar no painel SMS Legal).'
        },
        from: {
          type: 'string',
          description: 'ID do Remetente cadastrado no painel.'
        },
        token: {
          type: 'string',
          description: 'Opcional. Token da API do SMS Legal.'
        }
      },
      required: ['to', 'idaudio', 'from']
    }
  }
];

/**
 * Handle incoming MCP tool call
 */
async function callTool(name, args = {}) {
  switch (name) {
    case 'sms_enviar_texto': {
      const { to, msg, token } = args;
      return await apiRequest('send-sms-texto.php', { to, msg, token }, 'POST');
    }
    case 'sms_enviar_lote': {
      const { to, msg, token } = args;
      return await apiRequest('send-sms-texto-lote.php', { to, msg, token }, 'POST');
    }
    case 'sms_agendar': {
      const { to, msg, dtenvio, token } = args;
      return await apiRequest('agendar-sms.php', { to, msg, dtenvio, token }, 'POST');
    }
    case 'sms_consultar_status': {
      const { idsms, token } = args;
      return await apiRequest('status.php', { idsms, token }, 'GET');
    }
    case 'sms_consultar_creditos': {
      const { token } = args;
      return await apiRequest('creditos.php', { token }, 'GET');
    }
    case 'sms_consultar_respostas': {
      const { qt = 50, token } = args;
      return await apiRequest('respostas.php', { qt, token }, 'GET');
    }
    case 'sms_consultar_numero': {
      const { nr, token } = args;
      return await apiRequest('consultar-numero.php', { nr, token }, 'GET');
    }
    case 'sms_enviar_voz': {
      const { to, msg, from, token } = args;
      return await apiRequest('send-sms-voz.php', { to, msg, from, token }, 'POST');
    }
    case 'sms_enviar_audio': {
      const { to, idaudio, from, token } = args;
      return await apiRequest('send-sms-audio.php', { to, idaudio, from, token }, 'POST');
    }
    default:
      throw new Error(`Ferramenta desconhecida: ${name}`);
  }
}

/**
 * JSON-RPC stdio handler
 */
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', async (line) => {
  if (!line.trim()) return;

  let request;
  try {
    request = JSON.parse(line);
  } catch (err) {
    const errorResponse = {
      jsonrpc: '2.0',
      id: null,
      error: {
        code: -32700,
        message: 'Parse error: invalid JSON'
      }
    };
    process.stdout.write(JSON.stringify(errorResponse) + '\n');
    return;
  }

  const { id, method, params } = request;

  try {
    if (method === 'initialize') {
      const response = {
        jsonrpc: '2.0',
        id,
        result: {
          protocolVersion: '2024-11-05',
          capabilities: {
            tools: {}
          },
          serverInfo: {
            name: 'sms-legal-mcp-server',
            version: '1.0.0'
          }
        }
      };
      process.stdout.write(JSON.stringify(response) + '\n');
    } else if (method === 'notifications/initialized') {
      // Client confirmed init, no response required
    } else if (method === 'tools/list') {
      const response = {
        jsonrpc: '2.0',
        id,
        result: {
          tools: TOOLS
        }
      };
      process.stdout.write(JSON.stringify(response) + '\n');
    } else if (method === 'tools/call') {
      const toolName = params?.name;
      const toolArgs = params?.arguments || {};
      const resultData = await callTool(toolName, toolArgs);

      const response = {
        jsonrpc: '2.0',
        id,
        result: {
          content: [
            {
              type: 'text',
              text: typeof resultData === 'string' ? resultData : JSON.stringify(resultData, null, 2)
            }
          ]
        }
      };
      process.stdout.write(JSON.stringify(response) + '\n');
    } else if (method === 'ping') {
      process.stdout.write(JSON.stringify({ jsonrpc: '2.0', id, result: {} }) + '\n');
    } else {
      const response = {
        jsonrpc: '2.0',
        id,
        error: {
          code: -32601,
          message: `Método não suportado: ${method}`
        }
      };
      process.stdout.write(JSON.stringify(response) + '\n');
    }
  } catch (err) {
    const response = {
      jsonrpc: '2.0',
      id,
      error: {
        code: -32000,
        message: err.message || 'Erro interno no servidor MCP'
      }
    };
    process.stdout.write(JSON.stringify(response) + '\n');
  }
});

