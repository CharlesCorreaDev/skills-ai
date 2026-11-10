Manuseio de Dados na Internet
*****************************

Este capítulo descreve módulos que suportam a manipulação de formatos
de dados comumente usados na Internet.

* "email" --- Um e-mail e um pacote MIME manipulável

  * "email.message": Representing an email message

  * "email.parser": Parsing email messages

    * API do FeedParser

    * Parser API

    * Additional notes

  * "email.generator": Geração de documentos MIME

  * "email.policy": Policy Objects

  * "email.errors": Classes de Exceção e Defeito.

  * "email.headerregistry": Custom Header Objects

  * "email.contentmanager": Gerenciando conteúdo MIME

    * Content Manager Instances

  * "email": Exemplos

  * "email.message.Message": Representing an email message using the
    "compat32" API

  * "email.mime""email.mime": Criando e-mail e objetos MIME do zero

  * "email.header": Internationalized headers

  * "email.charset": Representando conjuntos de caracteres

  * "email.encoders": Codificadores

  * "email.utils": Utilitários diversos

  * "email.iterators": Iteradores

* "json" --- Codificador e decodificador JSON

  * Uso básico

  * Codificadores e decodificadores

  * Exceções

  * Conformidade e interoperabilidade entre padrões

    * Codificações de caracteres

    * Valores numéricos infinitos e NaN

    * Nomes repetidos dentro de um objeto

    * Valores não objeto e não vetor de nível superior

    * Limitações de implementação

  * Interface de linha de comando

    * Opções de linha de comando

* "mailbox" --- Manipule caixas de entradas em vários formatos

  * Objetos "Mailbox"

    * "Maildir" objects

    * "mbox" objects

    * "MH" objects

    * "Babyl" objects

    * "MMDF" objects

  * "Message" objects

    * "MaildirMessage" objects

    * "mboxMessage" objects

    * "MHMessage" objects

    * "BabylMessage" objects

    * "MMDFMessage" objects

  * Exceções

  * Exemplos

* "mimetypes" --- Mapeia nomes de arquivos para tipos MIME

  * Objetos MimeTypes

  * Uso na linha de comando

  * Exemplos na linha de comando

* "base64" --- Base16, Base32, Base64, Base85 Data Encodings

  * RFC 4648 Encodings

  * Base85 Encodings

  * Legacy Interface

  * Considerações de Segurança

* "binascii" --- Converte entre binário e ASCII

* "quopri" --- Codifica e decodifica dados MIME imprimidos entre aspas
