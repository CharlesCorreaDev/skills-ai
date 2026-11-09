/**
 * SMS Legal Node.js / TypeScript Client
 * Universal SDK for SMS Legal / SMS Gateway API.
 */

const https = require('https');

class SmsLegalClient {
  constructor(token, options = {}) {
    if (!token) {
      throw new Error('Token da API SMS Legal é obrigatório.');
    }
    this.token = token.trim();
    this.baseUrl = options.baseUrl || 'https://v1.smsgateway.com.br/api/';
    this.timeout = options.timeout || 30000;
  }

  _sanitizePhone(phone) {
    return String(phone).replace(/\D+/g, '');
  }

  _request(endpoint, params = {}, method = 'GET') {
    return new Promise((resolve, reject) => {
      const merged = { ...params, token: this.token };
      const searchParams = new URLSearchParams();

      for (const [key, val] of Object.entries(merged)) {
        if (val !== undefined && val !== null) {
          searchParams.append(key, String(val));
        }
      }

      let urlStr = `${this.baseUrl}${endpoint}`;
      const headers = {
        'User-Agent': 'SmsLegal-NodeClient/1.0.0',
        'Accept': 'application/json, text/plain, */*'
      };

      const options = {
        method: method.toUpperCase(),
        headers,
        timeout: this.timeout
      };

      if (options.method === 'GET') {
        urlStr += `?${searchParams.toString()}`;
      } else {
        const bodyStr = searchParams.toString();
        options.headers['Content-Type'] = 'application/x-www-form-urlencoded';
        options.headers['Content-Length'] = Buffer.byteLength(bodyStr);
      }

      const req = https.request(urlStr, options, (res) => {
        let raw = '';
        res.setEncoding('utf8');
        res.on('data', (c) => { raw += c; });
        res.on('end', () => {
          try {
            resolve(JSON.parse(raw));
          } catch (e) {
            resolve({ raw: raw.trim(), statusCode: res.statusCode });
          }
        });
      });

      req.on('error', (err) => resolve({ error: true, message: err.message }));
      req.on('timeout', () => {
        req.destroy();
        resolve({ error: true, message: 'Timeout ao conectar com a API SMS Legal' });
      });

      if (options.method === 'POST') {
        req.write(searchParams.toString());
      }
      req.end();
    });
  }

  enviarTexto(to, msg) {
    return this._request('send-sms-texto.php', {
      to: this._sanitizePhone(to),
      msg
    }, 'POST');
  }

  enviarLote(recipients, msg) {
    const toStr = Array.isArray(recipients)
      ? recipients.map(this._sanitizePhone).join(',')
      : recipients;
    return this._request('send-sms-texto-lote.php', {
      to: toStr,
      msg
    }, 'POST');
  }

  agendar(recipients, msg, dtenvio) {
    const toStr = Array.isArray(recipients)
      ? recipients.map(this._sanitizePhone).join(',')
      : recipients;
    return this._request('agendar-sms.php', {
      to: toStr,
      msg,
      dtenvio
    }, 'POST');
  }

  consultarStatus(idsms) {
    return this._request('status.php', { idsms }, 'GET');
  }

  consultarCreditos() {
    return this._request('creditos.php', {}, 'GET');
  }

  consultarRespostas(qt = 50) {
    return this._request('respostas.php', { qt }, 'GET');
  }

  consultarNumero(phone) {
    return this._request('consultar-numero.php', {
      nr: this._sanitizePhone(phone)
    }, 'GET');
  }

  enviarVoz(to, msg, from) {
    return this._request('send-sms-voz.php', {
      to: this._sanitizePhone(to),
      msg,
      from
    }, 'POST');
  }

  enviarAudio(to, idaudio, from) {
    return this._request('send-sms-audio.php', {
      to: this._sanitizePhone(to),
      idaudio,
      from
    }, 'POST');
  }
}

module.exports = { SmsLegalClient };

