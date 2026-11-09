# Cheatsheet Rápido - SMS Legal API 📱⚡

## Base URL & Autenticação
- **Base URL**: `https://v1.smsgateway.com.br/api/`
- **Autenticação**: Parâmetro `token=SEU_TOKEN`
- **Formato Telefone**: `DDI + DDD + Número` (sem pontuação, traços ou parênteses). Ex: `5551999999999`.
- **Codificação de Mensagem**: Sempre `URL Encoded` (`urlencode` em PHP, `urllib.parse.quote` em Python, `encodeURIComponent` em JS).

---

## Tabela de Endpoints

| Ação | Endpoint | Método | Parâmetros Principais | Resposta Chave |
| :--- | :--- | :--- | :--- | :--- |
| **SMS Texto Simples** | `send-sms-texto.php` | `POST`/`GET` | `token`, `to`, `msg` | `IdSMS`, `Sucesso: 200`, `Creditos` |
| **SMS em Lote** | `send-sms-texto-lote.php` | `POST`/`GET` | `token`, `to` (vírgula), `msg` | Array com `IdSMS`, `NrDestino` |
| **Agendar SMS** | `agendar-sms.php` | `POST`/`GET` | `token`, `to`, `msg`, `dtenvio` | `CodigoEnvio`, `DataAgendamento` |
| **Consultar Status** | `status.php` | `GET` | `token`, `idsms` | `CodStatus`, `DescStatus` |
| **Consultar Créditos** | `creditos.php` | `GET` | `token` | `SaldoCreditos`, `DataSaldo` |
| **Ver Respostas** | `respostas.php` | `GET` | `token`, `qt` (máx 500) | `TextoResposta`, `DataResposta` |
| **Consultar Operadora** | `consultar-numero.php` | `GET` | `token`, `nr` | `OperadoraAtual`, `Portado`, `Status` |
| **SMS Voz (TTS)** | `send-sms-voz.php` | `POST`/`GET` | `token`, `to`, `msg`, `from` | `IdSMS`, `Remetente` |
| **SMS Áudio Gravado** | `send-sms-audio.php` | `POST`/`GET` | `token`, `to`, `idaudio`, `from` | `IdSMS`, `IdAudio` |

---

## Formato de Agendamento (`dtenvio`)
- Padrão obrigatório: `DD-MM-AAAA HH:MM:SS`
- Exemplo: `25-10-2026 14:30:00`

---

## Tabela de Códigos de Erro da API

| Código | Descrição / Causa | Ação Recomendada |
| :---: | :--- | :--- |
| **000** | Conta bloqueada ou nenhum registro encontrado | Verificar regularidade da conta no suporte SMS Legal. |
| **001** | Token Inválido ou não informado | Verificar variável `SMS_LEGAL_TOKEN` ou token fornecido. |
| **002** | Número de celular não informado ou token < 40 chars | Confirmar telefone no formato `5551999999999`. |
| **003** | Texto da mensagem não informado ou token > 40 chars | Confirmar preenchimento do campo `msg`. |
| **004** | Número de celular inválido, ID remetente não informado ou data inválida | Validar máscara e ID remetente de voz. |
| **005** | Usuário não cadastrado ou data de agendamento inválida | Verificar formato `DD-MM-AAAA HH:MM:SS`. |
| **006** | Contém URL/Link não autorizado ou mais de 1.000 números | Solicitar liberação de envio de links ou particionar lote. |
| **007** | Palavra proibida na mensagem ou sem áudio liberado | Remover termos proibidos pelo gateway. |
| **008** | Saldo insuficiente de créditos | Realizar recarga de créditos no painel. |
| **009** | SMS não enviada (falha no gateway) ou parâmetros ausentes | Tentar novamente após alguns segundos. |
| **010** | Saldo insuficiente ou parâmetros de voz ausentes | Verificar saldo e remetente de voz. |
| **011** | Parâmetros de agendamento obrigatórios não informados | Validar envio conjunto de `to`, `msg`, `dtenvio`. |

