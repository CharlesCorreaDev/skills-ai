"email" --- Um e-mail e um pacote MIME manipulável
**************************************************

**Código-fonte:** Lib/email/__init__.py

======================================================================

The "email" package is a library for managing email messages.  It is
specifically *not* designed to do any sending of email messages to
SMTP (**RFC 2821**), NNTP, or other servers; those are functions of
modules such as "smtplib".  The "email" package attempts to be as RFC-
compliant as possible, supporting **RFC 5322** and **RFC 6532**, as
well as such MIME-related RFCs as **RFC 2045**, **RFC 2046**, **RFC
2047**, **RFC 2183**, and **RFC 2231**.

No geral a estrutura do pacote de e-mail pode ser dividida em três
componentes principais, mais um quarto componente que controla o
comportamento dos outros componentes.

O componente central do pacote é um "modelo de objeto" que representa
mensagens de e-mail. Uma aplicação interage com o pacote
principalmente através da interface do modelo de objeto definida no
submódulo "message". A aplicação pode usar essa API para fazer
perguntas sobre um e-mail existente, construir um novo e-mail ou
adicionar ou remover subcomponentes de e-mail que usam a mesma
interface de modelo de objeto. Ou seja, seguindo a natureza das
mensagens de e-mail e seus subcomponentes MIME, o modelo de objeto de
e-mail é uma estrutura em árvore de objetos que fornecem a API
"EmailMessage".

Os outros dois componentes principais do pacote são "parser" e
"generator". O analisador sintático pega a versão serializada de uma
mensagem de e-mail (um fluxo de bytes) e a converte em uma árvore de
objetos "EmailMessage". O gerador pega um "EmailMessage" e o
transforma novamente em um fluxo de bytes serializado. (O analisador
sintático e o gerador também lidam com fluxos de caracteres de texto,
mas esse uso é desencorajado, pois é muito fácil terminar com
mensagens que não são válidas de uma maneira ou de outra.)

O componente de controle é o módulo "policy". Cada "EmailMessage",
cada "generator" e cada "parser" tem um objeto associado "policy" que
controla seu comportamento. Normalmente, uma aplicação precisa
especificar a política apenas quando uma "EmailMessage" é criada,
instanciando diretamente uma "EmailMessage" para criar um novo e-mail
ou analisando um fluxo de entrada usando um "parser". Mas a política
pode ser alterada quando a mensagem é serializada usando um
"generator". Isso permite, por exemplo, analisar uma mensagem de
e-mail genérica do disco, mas serializá-la usando as configurações
SMTP padrão ao enviá-la para um servidor de e-mail.

The email package does its best to hide the details of the various
governing RFCs from the application.  Conceptually the application
should be able to treat the email message as a structured tree of
Unicode text and binary attachments, without having to worry about how
these are represented when serialized.  In practice, however, it is
often necessary to be aware of at least some of the rules governing
MIME messages and their structure, specifically the names and nature
of the MIME "content types" and how they identify multipart documents.
For the most part this knowledge should only be required for more
complex applications, and even then it should only be the high level
structure in question, and not the details of how those structures are
represented.  Since MIME content types are used widely in modern
internet software (not just email), this will be a familiar concept to
many programmers.

The following sections describe the functionality of the "email"
package. We start with the "message" object model, which is the
primary interface an application will use, and follow that with the
"parser" and "generator" components.  Then we cover the "policy"
controls, which completes the treatment of the main components of the
library.

As próximas três seções cobrem as exceções que o pacote pode
apresentar e os defeitos (não conformidade com as RFCs) que o "parser"
pode detectar. A seguir, abordamos os subcomponentes "headerregistry"
e os subcomponentes "contentmanager", que fornecem ferramentas para
manipulação mais detalhada de cabeçalhos e cargas úteis,
respectivamente. Ambos os componentes contêm recursos relevantes para
consumir e produzir mensagens não triviais, mas também documentam suas
APIs de extensibilidade, que serão de interesse para aplicações
avançadas.

A seguir, é apresentado um conjunto de exemplos de uso das partes
fundamentais das APIs abordadas nas seções anteriores.

The foregoing represent the modern (Unicode friendly) API of the email
package. The remaining sections, starting with the "Message" class,
cover the legacy "compat32" API that deals much more directly with the
details of how email messages are represented.  The "compat32" API
does *not* hide the details of the RFCs from the application, but for
applications that need to operate at that level, they can be useful
tools.  This documentation is also relevant for applications that are
still using the "compat32" API for backward compatibility reasons.

Alterado na versão 3.6: Documentos reorganizados e reescritos para
promover a nova API "EmailMessage"/"EmailPolicy".

Contents of the "email" package documentation:

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

API legada

* "email.message.Message": Representing an email message using the
  "compat32" API

* "email.mime""email.mime": Criando e-mail e objetos MIME do zero

* "email.header": Internationalized headers

* "email.charset": Representando conjuntos de caracteres

* "email.encoders": Codificadores

* "email.utils": Utilitários diversos

* "email.iterators": Iteradores

Ver também:

  Módulo "smtplib"
     Cliente SMTP (Protocolo Simples de Envio de E-mail)

  Módulo "poplib"
     Cliente POP (Post Office Protocol)

  Módulo "imaplib"
     Cliente IMAP (Internet Message Access Protocol)

  Módulo "mailbox"
     Ferramentas para criar, ler, e gerenciar coleções de mensagem em
     disco usando vários formatos padrão.
