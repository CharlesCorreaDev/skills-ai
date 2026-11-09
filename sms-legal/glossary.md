# Glossário de Termos - SMS Legal API 📖

| Termo | Significado no Contexto do Gateway |
| :--- | :--- |
| **Token** | Chave alfanumérica única (com aproximadamente 40 caracteres) fornecida no painel do SMS Legal para autenticar requisições. |
| **IdSMS** | Identificador único alfanumérico gerado pelo gateway para cada mensagem enviada (ex: `R010000A789AFD2E5CCFBEC6137AB525105P5G`). Utilizado para rastreamento de status e cruzamento de respostas. |
| **DDI + DDD** | Código do país (55 para Brasil) somado ao código de área da localidade (ex: 11 para SP, 51 para Porto Alegre/RS) antecedendo o número de 9 dígitos. |
| **SMS Curto (1 Crédito)** | Mensagem contendo até 160 caracteres padrão GSM 7-bit ou 70 caracteres caso contenha acentuação e caracteres especiais UTF-16. |
| **SMS Lote** | Envio de uma mensagem idêntica para até 1.000 números diferentes na mesma requisição HTTP. |
| **SMS Voz (TTS)** | Text-to-Speech: serviço onde o texto enviado é sintetizado por robô de voz e transmitido através de uma ligação telefônica atendida pelo destinatário. |
| **SMS Áudio** | Ligação telefônica que reproduz um arquivo `.wav` ou áudio gravado e aprovado previamente no painel. |
| **ID Remetente (`from`)** | Identificador cadastrado e validado no painel do SMS Legal em "Todos Números" > "ID API", obrigatório para chamadas de voz e áudio. |
| **Portabilidade** | Verificação se um número de celular mudou de operadora (ex: da Claro para a Vivo), permitida via `consultar-numero.php`. |
| **Reply / Resposta** | Mensagem de SMS que o usuário destinatário responde no próprio celular, capturada através do endpoint `respostas.php`. |

