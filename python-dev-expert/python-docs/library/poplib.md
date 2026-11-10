"poplib" --- Cliente de protocolo POP3
**************************************

**Source code:** Lib/poplib.py

======================================================================

Este módulo define uma classe, "POP3", que encapsula uma conexão com
um servidor POP3 e implementa o protocolo conforme definido em **RFC
1939**. A classe "POP3" oferece suporte aos conjuntos de comandos
mínimos e opcionais de **RFC 1939**. A classe "POP3" também oferece
suporte ao comando "STLS" introduzido em **RFC 2595** para permitir a
comunicação criptografada em uma conexão já estabelecida.

Além disso, este módulo fornece uma classe "POP3_SSL", que fornece
suporte para conexão a servidores POP3 que usam SSL como uma camada de
protocolo subjacente.

Observe que o POP3, embora amplamente suportado, está obsoleto. A
qualidade de implementação dos servidores POP3 varia muito, e muitos
são bastante ruins. Se o seu servidor de e-mail oferece suporte a
IMAP, seria melhor usar a classe "imaplib.IMAP4", pois os servidores
IMAP tendem a ter uma implementação melhor.

Disponibilidade: not WASI.

Este módulo não funciona ou não está disponível em WebAssembly. Veja
Plataformas WebAssembly para mais informações.

The "poplib" module provides two classes:

class poplib.POP3(host, port=POP3_PORT[, timeout])

   Esta classe implementa o protocolo POP3 real. A conexão é criada
   quando a instância é inicializada. Se *port* for omitido, a porta
   POP3 padrão (110) será usada. O parâmetro opcional *timeout*
   especifica um tempo limite em segundos para a tentativa de conexão
   (se não for especificado, a configuração de tempo limite padrão
   global será usada).

   Levanta um evento de auditoria "ftplib.connect" com os argumentos
   "self", "host", "port".

   Todos os comandos levantarão um evento de auditoria
   "poplib.putline" com os argumentos "self" e "line", onde "line" são
   os bytes prestes a serem enviados ao host remoto.

   Alterado na versão 3.9: Se o parâmetro *timeout* for definido como
   zero, será levantada "ValueError" para impedir a criação de um
   soquete não bloqueante.

class poplib.POP3_SSL(host, port=POP3_SSL_PORT, *, timeout=None, context=None)

   Esta é uma subclasse de "POP3" que se conecta ao servidor por meio
   de um soquete criptografado SSL. Se *port* não for especificado,
   995, a porta padrão POP3 sobre SSL será usada. *timeout* funciona
   como no construtor "POP3". *context* é um objeto opcional
   "ssl.SSLContext" que permite agrupar opções de configuração SSL,
   certificados e chaves privadas em uma única estrutura
   (potencialmente duradoura). Consulte Considerações de segurança
   para obter as melhores práticas.

   Levanta um evento de auditoria "ftplib.connect" com os argumentos
   "self", "host", "port".

   Todos os comandos levantarão um evento de auditoria
   "poplib.putline" com os argumentos "self" e "line", onde "line" são
   os bytes prestes a serem enviados ao host remoto.

   Alterado na versão 3.2: Parâmetro *context* adicionado.

   Alterado na versão 3.4: A classe agora oferece suporte a
   verificação de nome de host com "ssl.SSLContext.check_hostname" e
   *Indicação de nome de servidor* (veja "ssl.HAS_SNI").

   Alterado na versão 3.9: Se o parâmetro *timeout* for definido como
   zero, será levantada "ValueError" para impedir a criação de um
   soquete não bloqueante.

   Alterado na versão 3.12: Os parâmetros depreciados *keyfile* e
   *certfile*  foram removidos.

One exception is defined as an attribute of the "poplib" module:

exception poplib.error_proto

   Exceção levantada em caso de erros deste módulo (erros do módulo
   "socket" não são detectados). O motivo da exceção é passado ao
   construtor como uma string.

Ver também:

  Módulo "imaplib"
     The standard Python IMAP module.

  Frequently Asked Questions About Fetchmail
     The FAQ for the **fetchmail** POP/IMAP client collects
     information on POP3 server variations and RFC noncompliance that
     may be useful if you need to write an application based on the
     POP protocol.


Objetos POP3
============

All POP3 commands are represented by methods of the same name, in
lowercase; most return the response text sent by the server.

A "POP3" instance has the following methods:

POP3.set_debuglevel(level)

   Set the instance's debugging level.  This controls the amount of
   debugging output printed.  The default, "0", produces no debugging
   output.  A value of "1" produces a moderate amount of debugging
   output, generally a single line per request.  A value of "2" or
   higher produces the maximum amount of debugging output, logging
   each line sent and received on the control connection.

POP3.getwelcome()

   Returns the greeting string sent by the POP3 server.

POP3.capa()

   Query the server's capabilities as specified in **RFC 2449**.
   Returns a dictionary in the form "{'name': ['param'...]}".

   Adicionado na versão 3.4.

POP3.user(username)

   Send user command, response should indicate that a password is
   required.

POP3.pass_(password)

   Send password, response includes message count and mailbox size.
   Note: the mailbox on the server is locked until "quit()" is called.

POP3.apop(user, secret)

   Use the more secure APOP authentication to log into the POP3
   server.

POP3.rpop(user)

   Use RPOP authentication (similar to UNIX r-commands) to log into
   POP3 server.

POP3.stat()

   Get mailbox status.  The result is a tuple of 2 integers: "(message
   count, mailbox size)".

POP3.list([which])

   Request message list, result is in the form "(response, ['mesg_num
   octets', ...], octets)". If *which* is set, it is the message to
   list.

POP3.retr(which)

   Retrieve whole message number *which*, and set its seen flag.
   Result is in form "(response, ['line', ...], octets)".

POP3.dele(which)

   Flag message number *which* for deletion.  On most servers
   deletions are not actually performed until QUIT (the major
   exception is Eudora QPOP, which deliberately violates the RFCs by
   doing pending deletes on any disconnect).

POP3.rset()

   Remove any deletion marks for the mailbox.

POP3.noop()

   Do nothing.  Might be used as a keep-alive.

POP3.quit()

   Signoff:  commit changes, unlock mailbox, drop connection.

POP3.top(which, howmuch)

   Retrieves the message header plus *howmuch* lines of the message
   after the header of message number *which*. Result is in form
   "(response, ['line', ...], octets)".

   The POP3 TOP command this method uses, unlike the RETR command,
   doesn't set the message's seen flag; unfortunately, TOP is poorly
   specified in the RFCs and is frequently broken in off-brand
   servers. Test this method by hand against the POP3 servers you will
   use before trusting it.

POP3.uidl(which=None)

   Return message digest (unique id) list. If *which* is specified,
   result contains the unique id for that message in the form
   "'response mesgnum uid", otherwise result is list "(response,
   ['mesgnum uid', ...], octets)".

POP3.utf8()

   Try to switch to UTF-8 mode. Returns the server response if
   successful, raises "error_proto" if not. Specified in **RFC 6856**.

   Adicionado na versão 3.5.

POP3.stls(context=None)

   Start a TLS session on the active connection as specified in **RFC
   2595**. This is only allowed before user authentication

   *context* parameter is a "ssl.SSLContext" object which allows
   bundling SSL configuration options, certificates and private keys
   into a single (potentially long-lived) structure.  Please read
   Considerações de segurança for best practices.

   This method supports hostname checking via
   "ssl.SSLContext.check_hostname" and *Server Name Indication* (see
   "ssl.HAS_SNI").

   Adicionado na versão 3.4.

Instances of "POP3_SSL" have no additional methods. The interface of
this subclass is identical to its parent.


Exemplo POP3
============

Here is a minimal example (without error checking) that opens a
mailbox and retrieves and prints all messages:

   import getpass, poplib

   M = poplib.POP3('localhost')
   M.user(getpass.getuser())
   M.pass_(getpass.getpass())
   numMessages = len(M.list()[1])
   for i in range(numMessages):
       for j in M.retr(i+1)[1]:
           print(j)

At the end of the module, there is a test section that contains a more
extensive example of usage.
