# Padrões Arquiteturais e Boas Práticas - SMS Legal 🏗️🛡️

## 1. Segurança e Gerenciamento do Token
- **Nunca exponha o token no cliente (front-end):** Aplicações Web (React, Vue, Angular, Mobile) nunca devem chamar a API SMS Legal diretamente. Crie sempre um backend intermediário (BFF - Backend For Frontend) em PHP, Node, Python, C#, etc.
- **Variáveis de Ambiente:** Armazene o token em `.env` (`SMS_LEGAL_TOKEN`) ou em segredos gerenciados (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault).

---

## 2. Padrão de Fila Assíncrona (Asynchronous Queue Worker)
Em sistemas de alto volume (notificações de e-commerce, alertas em massa, cobranças):
- Não execute a chamada HTTP síncrona diretamente na requisição do usuário web.
- Enfileire o envio de SMS em filas de mensageria (RabbitMQ, Redis Queue / BullMQ, SQS, Laravel Queues, Celery).
- Um worker consome a fila e dispara o SMS usando `POST` para `send-sms-texto.php` ou `send-sms-texto-lote.php`.
- Em caso de retorno `008` (saldo insuficiente), o worker deve pausar e disparar alerta crítico para os administradores.

---

## 3. Higienização e Validação de Números Telefônicos
- Remova caracteres especiais: `+`, `-`, `(`, `)`, espaços.
- Certifique-se de que o DDI (`55` para Brasil) e o DDD estão presentes.
- O formato final deve conter de 12 a 13 dígitos numéricos:
  - Ex: `55` (DDI) + `11` (DDD) + `999998888` (9 dígitos celular) = `5511999998888` (13 dígitos).
- Números antigos de 8 dígitos de celular devem ser validados antes do envio.

---

## 4. Política de Rate-Limit e Particionamento de Lotes
- O endpoint `send-sms-texto-lote.php` e `agendar-sms.php` aceitam no máximo **1.000 destinatários** por chamada.
- Se você tiver uma base de 5.000 clientes:
  - Divida a lista em blocos (chunks) de até 500 a 1.000 registros.
  - Faça os disparos sequenciais ou concorrentes com intervalo de segurança (ex: 200ms entre lotes) para evitar sobrecarga no gateway.

---

## 5. Captura e Tratamento de Respostas (Webhook Polling)
- Para sistemas que necessitam de confirmação interativa do cliente (ex: "Responda 1 para confirmar sua consulta"):
  - Crie um cronjob ou agendamento executando periodicamente a cada 1 a 5 minutos.
  - Chame `respostas.php?qt=100`.
  - Faça o match da resposta com a mensagem enviada através do `IdSMS` ou pelo número do cliente (`Destino`).
  - Marque como processada no seu banco de dados local.

---

## 6. Tratamento de Links e URLs
- A API SMS Legal bloqueia o envio de links e domínios com erro `006` caso a conta não tenha autorização expressa prévia.
- Antes de disparar links encurtados ou páginas de pagamento, solicite a homologação e liberação de envio de URLs junto ao suporte técnico do SMS Legal.

