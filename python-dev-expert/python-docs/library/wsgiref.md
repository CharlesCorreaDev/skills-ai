"wsgiref" --- Implementação de referência e utilitários WSGI
************************************************************

**Código-fonte:** Lib/wsgiref

======================================================================

Aviso:

  "wsgiref" is a reference implementation and is not recommended for
  production. The module only implements basic security checks.

A Interface de Gateway para Servidor Web (em inglês, Web Server
Gateway Interface - WSGI) é uma interface padrão localizada entre
software de servidores web e aplicações web escritas em Python. Ter um
interface padrão torna mais fácil a utilização de uma aplicação que
suporta WSGI com inúmeros diferentes servidores web.

Apenas autores de servidores web e frameworks de programação
necessitam saber todos os detalhes e especificidades do design WSGI.
Você não precisa entender todos os detalhes do WSGI para apenas
instalar uma aplicação WSGI ou para escrever uma aplicação web usando
um framework existente.

"wsgiref" is a reference implementation of the WSGI specification that
can be used to add WSGI support to a web server or framework.  It
provides utilities for manipulating WSGI environment variables and
response headers, base classes for implementing WSGI servers, a demo
HTTP server that serves WSGI applications, types for static type
checking, and a validation tool that checks WSGI servers and
applications for conformance to the WSGI specification (**PEP 3333**).

Veja wsgi.readthedocs.io para mais informações sobre WSGI, além de
links para tutoriais e outros recursos.


"wsgiref.util" -- WSGI environment utilities
============================================

Este módulo fornece uma variedade de funções de utilidade para
trabalhar com ambientes WSGI. Um ambiente WSGI é um dicionário
contendo variáveis de solicitação HTTP, conforme descrito na **PEP
3333**. Todas as funções que recebem um parâmetro *environ* esperam
que um dicionário compatível com WSGI seja fornecido; consulte a **PEP
3333** para uma especificação detalhada e "WSGIEnvironment" para um
apelido de tipo que pode ser usado em anotações de tipos.

wsgiref.util.guess_scheme(environ)

   Retorna uma sugestão sobre "wsgi.url_scheme" ser "http" ou "https"
   buscando por uma variável de ambiente "HTTPS" dentro do dicionário
   *environ*. O valor de retorno é uma string.

   Esta função é útil ao criar um gateway que encapsula CGI ou um
   protocolo semelhante a CGI, como FastCGI. Normalmente, servidores
   que fornecem tais protocolos incluirão uma variável "HTTPS" com um
   valor de "1", "yes" ou "on" quando uma solicitação é recebida via
   SSL. Então, esta função retorna "https" se tal valor for
   encontrado, e "http" caso contrário.

wsgiref.util.request_uri(environ, include_query=True)

   Retorna o URI de solicitação completo, opcionalmente incluindo a
   string de consulta, usando o algoritmo encontrado na seção "URL
   Reconstruction" da **PEP 3333**. Se *include_query* for falso, a
   string de consulta não será incluída no URI resultante.

wsgiref.util.application_uri(environ)

   Semelhante a "request_uri()", exceto que as variáveis "PATH_INFO" e
   "QUERY_STRING" são ignoradas. O resultado é o URI base do objeto da
   aplicação endereçado pela solicitação.

wsgiref.util.shift_path_info(environ)

   Desloca um único nome de "PATH_INFO" para "SCRIPT_NAME" e retorna o
   nome. O dicionário *environ* é *modificado* no local; use uma cópia
   se precisar manter o "PATH_INFO" ou "SCRIPT_NAME" original intacto.

   Se não houver segmentos de caminho restantes em "PATH_INFO", "None"
   será retornado.

   Normalmente, essa rotina é usada para processar cada porção de um
   caminho de URI de solicitação, por exemplo, para tratar o caminho
   como uma série de chaves de dicionário. Essa rotina modifica o
   ambiente passado para torná-lo adequado para invocar outra
   aplicação WSGI localizada no URI de destino. Por exemplo, se houver
   uma aplicação WSGI em "/foo", e o caminho de URI de solicitação for
   "/foo/bar/baz", e a aplicação WSGI em "/foo" chamar
   "shift_path_info()", ele receberá a string "bar", e o ambiente será
   atualizado para ser adequado para passar para uma aplicação WSGI em
   "/foo/bar". Ou seja, "SCRIPT_NAME" mudará de "/foo" para
   "/foo/bar", e "PATH_INFO" mudará de "/bar/baz" para "/baz".

   Quando "PATH_INFO" é apenas um "/", esta rotina retorna uma string
   vazia e acrescenta uma barra final a "SCRIPT_NAME", embora
   segmentos de caminho vazios sejam normalmente ignorados, e
   "SCRIPT_NAME" normalmente não termine em uma barra. Este é um
   comportamento intencional, para garantir que uma aplicação possa
   diferenciar URIs terminando em "/x" daqueles terminando em "/x/" ao
   usar esta rotina para fazer travessia de objetos.

wsgiref.util.setup_testing_defaults(environ)

   Atualiza *environ* com padrões triviais para fins de teste.

   Esta rotina adiciona vários parâmetros necessários para WSGI,
   incluindo "HTTP_HOST", "SERVER_NAME", "SERVER_PORT",
   "REQUEST_METHOD", "SCRIPT_NAME", "PATH_INFO" e todas as variáveis
   "wsgi.*" definidas pela **PEP 3333**. Ela fornece apenas valores
   padrão e não substitui nenhuma configuração existente para essas
   variáveis.

   Esta rotina tem como objetivo facilitar que testes unitários de
   servidores e aplicações WSGI configurem ambientes fictícios. Ela
   NÃO deve ser usada por servidores ou aplicações WSGI reais, pois os
   dados são falsos!

   Exemplo de uso (veja também "demo_app()" para outro exemplo):

      from wsgiref.util import setup_testing_defaults
      from wsgiref.simple_server import make_server

      # Uma aplicação WSGI relativamente simples. Vai exibir o dicionário
      # do ambiente após ser atualizada por setup_testing_defaults
      def simple_app(environ, start_response):
          setup_testing_defaults(environ)

          status = '200 OK'
          headers = [('Content-type', 'text/plain; charset=utf-8')]

          start_response(status, headers)

          ret = [("%s: %s\n" % (key, value)).encode("utf-8")
                 for key, value in environ.items()]
          return ret

      with make_server('', 8000, simple_app) as httpd:
          print("Serving on port 8000...")
          httpd.serve_forever()

In addition to the environment functions above, the "wsgiref.util"
module also provides these miscellaneous utilities:

wsgiref.util.is_hop_by_hop(header_name)

   Retorna "True" se 'header_name' for um cabeçalho HTTP/1.1 "Hop-by-
   Hop", conforme definido por **RFC 2616**.

class wsgiref.util.FileWrapper(filelike, blksize=8192)

   Uma implementação concreta do protocolo "wsgiref.types.FileWrapper"
   usado para converter um objeto arquivo ou similar em um *iterador*.
   Os objetos resultantes são *iteráveis*. Conforme o objeto é
   iterado, o parâmetro opcional *blksize* será repetidamente passado
   para o método "read()" do objeto *filelike* para obter bytestrings
   para produzir. Quando "read()" retorna uma string de bytes vazia, a
   iteração é encerrada e não pode ser retomada.

   Se *filelike* tiver um método "close()", o objeto retornado também
   terá um método "close()" e invocará o método "close()" do objeto
   *filelike* quando chamado.

   Exemplo de uso:

      from io import StringIO
      from wsgiref.util import FileWrapper

      # Estamos usando um StringIO-buffer como objeto arquivo ou similar
      filelike = StringIO("This is an example file-like object"*10)
      wrapper = FileWrapper(filelike, blksize=5)

      for chunk in wrapper:
          print(chunk)

   Alterado na versão 3.11: O suporte para o método "__getitem__()"
   foi removido


"wsgiref.headers" -- WSGI response header tools
===============================================

Este módulo fornece uma única classe, "Headers", para manipulação
conveniente de cabeçalhos de resposta WSGI usando uma interface
semelhante a mapeamento.

class wsgiref.headers.Headers([headers])

   Cria um objeto mapeamento envolvendo *headers*, que deve ser uma
   lista de tuplas de nome/valor de cabeçalho, conforme descrito na
   **PEP 3333**. O valor padrão de *headers* é uma lista vazia.

   Os objetos "Headers" oferecem suporte a operações de mapeamento
   típicas, incluindo "__getitem__()", "get()", "__setitem__()",
   "setdefault()", "__delitem__()" e "__contains__()". Para cada um
   desses métodos, a chave é o nome do cabeçalho (tratado sem
   distinção entre maiúsculas e minúsculas) e o valor é o primeiro
   valor associado a esse nome de cabeçalho. Definir um cabeçalho
   exclui quaisquer valores existentes para esse cabeçalho e, em
   seguida, adiciona um novo valor ao final da lista de cabeçalhos
   encapsulados. A ordem existente dos cabeçalhos geralmente é
   mantida, com novos cabeçalhos adicionados ao final da lista
   encapsulada.

   Diferentemente de um dicionário, objetos "Headers" não levantam um
   erro quando você tenta obter ou excluir uma chave que não está na
   lista de cabeçalhos encapsulados. Obter um cabeçalho inexistente
   retorna apenas "None", e excluir um cabeçalho inexistente não faz
   nada.

   Os objetos "Headers" também oferecem suporte aos métodos "keys()",
   "values()" e "items()". As listas retornadas por "keys()" e
   "items()" podem incluir a mesma chave mais de uma vez se houver um
   cabeçalho multivalorado. O "len()" de um objeto "Headers" é o mesmo
   que o comprimento de seus "items()", que é o mesmo que o
   comprimento da lista de cabeçalhos encapsulados. Na verdade, o
   método "items()" apenas retorna uma cópia da lista de cabeçalhos
   encapsulados.

   Chamar "bytes()" em um objeto "Headers" retorna uma bytestring
   formatada adequada para transmissão como cabeçalhos de resposta
   HTTP. Cada cabeçalho é colocado em uma linha com seu valor,
   separado por dois pontos e um espaço. Cada linha é terminada por um
   retorno de carro e uma quebra de linha, e a bytestring é terminada
   com uma linha em branco.

   Além de sua interface de mapeamento e recursos de formatação, os
   objetos "Headers" também têm os seguintes métodos para consultar e
   adicionar cabeçalhos multivalorados e para adicionar cabeçalhos com
   parâmetros MIME:

   get_all(name)

      Retorna uma lista de todos os valores para o cabeçalho nomeado.

      A lista retornada será classificada na ordem em que apareceu na
      lista de cabeçalho original ou foi adicionada a esta instância,
      e pode conter duplicatas. Quaisquer campos excluídos e
      reinseridos são sempre anexados à lista de cabeçalho. Se não
      houver campos com o nome fornecido, retorna uma lista vazia.

   add_header(name, value, **_params)

      Adiciona um cabeçalho (possivelmente multivalorado), com
      parâmetros MIME opcionais especificados por meio de argumentos
      nomeados.

      *name* é o campo de cabeçalho a ser adicionado. Argumentos
      nomeados podem ser usados para definir parâmetros MIME para o
      campo de cabeçalho. Cada parâmetro deve ser uma string ou
      "None". Sublinhados em nomes de parâmetros são convertidos em
      traços, já que traços são ilegais em identificadores Python, mas
      muitos nomes de parâmetros MIME incluem traços. Se o valor do
      parâmetro for uma string, ele será adicionado aos parâmetros de
      valor do cabeçalho no formato "name="value"". Se for "None",
      somente o nome do parâmetro será adicionado. (Isso é usado para
      parâmetros MIME sem um valor.) Exemplo de uso:

         h.add_header('content-disposition', 'attachment', filename='bud.gif')

      O exemplo acima adicionará um cabeçalho parecido com este:

         Content-Disposition: attachment; filename="bud.gif"

   Alterado na versão 3.5: o parâmetro *headers* é opcional.


"wsgiref.simple_server" -- a simple WSGI HTTP server
====================================================

Este módulo implementa um servidor HTTP simples (com base em
"http.server") que serve aplicações WSGI. Cada instância de servidor
serve uma única aplicação WSGI em um host e porta fornecidos. Se você
quiser servir várias aplicações em um único host e porta, você deve
criar uma aplicação WSGI que analise "PATH_INFO" para selecionar qual
aplicação invocar para cada solicitação. (Por exemplo, usando a função
"shift_path_info()" de "wsgiref.util".)

wsgiref.simple_server.make_server(host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler)

   Cria um novo servidor WSGI escutando em *host* e *port*, aceitando
   conexões para *app*. O valor de retorno é uma instância da
   *server_class* fornecida e processará solicitações usando a
   *handler_class* especificada. *app* deve ser um objeto de aplicação
   WSGI, conforme definido pela **PEP 3333**.

   Exemplo de uso:

      from wsgiref.simple_server import make_server, demo_app

      with make_server('', 8000, demo_app) as httpd:
          print("Serving HTTP on port 8000...")

          # Responde a solicitações até o processo ser encerrado
          httpd.serve_forever()

          # Alternativa: serve uma solicitação e então sai
          httpd.handle_request()

wsgiref.simple_server.demo_app(environ, start_response)

   This function is a small but complete WSGI application that returns
   a text page containing the message "Hello world!" and a list of the
   key/value pairs provided in the *environ* parameter.  It's useful
   for verifying that a WSGI server (such as "wsgiref.simple_server")
   is able to run a simple WSGI application correctly.

   O chamável *start_response* deve seguir o protocolo
   "StartResponse".

class wsgiref.simple_server.WSGIServer(server_address, RequestHandlerClass)

   Cria uma instância "WSGIServer". *server_address* deve ser uma
   tupla "(host,port)" e *RequestHandlerClass* deve ser a subclasse de
   "http.server.BaseHTTPRequestHandler" que será usada para processar
   solicitações.

   Normalmente você não precisa chamar esse construtor, pois a função
   "make_server()" pode cuidar de todos os detalhes para você.

   "WSGIServer" é uma subclasse de "http.server.HTTPServer", então
   todos os seus métodos (como "serve_forever()" e "handle_request()")
   estão disponíveis. "WSGIServer" também fornece estes métodos
   específicos do WSGI:

   set_app(application)

      Define o chamável *application* como a aplicação WSGI que
      receberá solicitações.

   get_app()

      Retorna o chamável da aplicação definido atualmente.

   Normalmente, no entanto, você não precisa usar esses métodos
   adicionais, pois "set_app()" é normalmente chamado por
   "make_server()", e "get_app()" existe principalmente para o
   benefício de instâncias do manipulador de solicitações.

class wsgiref.simple_server.WSGIRequestHandler(request, client_address, server)

   Cria um manipulador HTTP para *request* fornecido (isto é, um
   soquete), *client_address* (uma tupla "(host,port)") e *server*
   (instância "WSGIServer").

   Você não precisa criar instâncias desta classe diretamente; elas
   são criadas automaticamente conforme necessário pelos objetos
   "WSGIServer". Você pode, no entanto, estender esta classe e
   fornecê-la como uma *handler_class* para a função "make_server()".
   Alguns métodos possivelmente relevantes para substituir em
   subclasses:

   get_environ()

      Retorna um dicionário "WSGIEnvironment" para uma solicitação. A
      implementação padrão copia o conteúdo do atributo de dicionário
      "base_environ" do objeto "WSGIServer" e então adiciona vários
      cabeçalhos derivados da solicitação HTTP. Cada chamada para esse
      método deve retornar um novo dicionário contendo todas as
      variáveis de ambiente CGI relevantes conforme especificado na
      **PEP 3333**.

   get_stderr()

      Retorna o objeto que deve ser usado como o fluxo "wsgi.errors".
      A implementação padrão retorna apenas "sys.stderr".

   handle()

      Processa a solicitação HTTP. A implementação padrão cria uma
      instância manipuladora usando uma classe "wsgiref.handlers" para
      implementar a interface da aplicação WSGI.


"wsgiref.validate" --- WSGI conformance checker
===============================================

When creating new WSGI application objects, frameworks, servers, or
middleware, it can be useful to validate the new code's conformance
using "wsgiref.validate".  This module provides a function that
creates WSGI application objects that validate communications between
a WSGI server or gateway and a WSGI application object, to check both
sides for protocol conformance.

Note que este utilitário não garante a conformidade completa com **PEP
3333**; uma ausência de erros deste módulo não significa
necessariamente que os erros não existam. No entanto, se este módulo
produzir um erro, então é virtualmente certo que o servidor ou a
aplicação não está 100% em conformidade.

Este módulo é baseado no módulo "paste.lint" da biblioteca "Python
Paste" de Ian Bicking.

wsgiref.validate.validator(application)

   Encapsula *application* e retorna um novo objeto de aplicação WSGI.
   A aplicação retornada encaminhará todas as solicitações para a
   *application* original e verificará se tanto a *application* quanto
   o servidor que o invoca estão em conformidade com a especificação
   WSGI e com **RFC 2616**.

   Qualquer falta de conformidade detectada resulta em uma
   "AssertionError" sendo levantado; note, entretanto, que a forma
   como esses erros são manipulados depende do servidor. Por exemplo,
   "wsgiref.simple_server" e outros servidores baseados em
   "wsgiref.handlers" (que não substituem os métodos de manipulação de
   erros para fazer outra coisa) simplesmente emitirão uma mensagem de
   que ocorreu um erro e despejarão o traceback para "sys.stderr" ou
   algum outro fluxo de erro.

   Este invólucro também pode gerar saída usando o módulo "warnings"
   para indicar comportamentos que são questionáveis, mas que podem
   não ser realmente proibidos por **PEP 3333**. A menos que sejam
   suprimidos usando opções de linha de comando do Python ou a API
   "warnings", quaisquer avisos serão gravados em "sys.stderr" (*não*
   "wsgi.errors", a menos que sejam o mesmo objeto).

   Exemplo de uso:

      from wsgiref.validate import validator
      from wsgiref.simple_server import make_server

      # Nosso objeto chamável que intencionalmente não está em
      # conformidade com o padrão, então o validador irá quebrar
      def simple_app(environ, start_response):
          status = '200 OK'  # HTTP Status
          headers = [('Content-type', 'text/plain')]  # HTTP Headers
          start_response(status, headers)

          # Isso vai quebrar porque precisamos retornar uma lista,
          # e o validador vai nos informar
          return b"Hello World"

      # Este é a aplicação encapsulada em um validador
      validator_app = validator(simple_app)

      with make_server('', 8000, validator_app) as httpd:
          print("Listening on port 8000....")
          httpd.serve_forever()


"wsgiref.handlers" -- server/gateway base classes
=================================================

Este módulo fornece classes de manipulador base para implementar
servidores e gateways WSGI. Essas classes base lidam com a maior parte
do trabalho de comunicação com uma aplicação WSGI, desde que recebam
um ambiente semelhante ao CGI, junto com fluxos de entrada, saída e
erro.

class wsgiref.handlers.CGIHandler

   Invocação baseada em CGI via "sys.stdin", "sys.stdout",
   "sys.stderr" e "os.environ". Isso é útil quando você tem uma
   aplicação WSGI e quer executá-lo como um script CGI. Basta invocar
   "CGIHandler().run(app)", onde "app" é o objeto da aplicação WSGI
   que você deseja invocar.

   Esta classe é uma subclasse de "BaseCGIHandler" que define
   "wsgi.run_once" como true, "wsgi.multithread" como false e
   "wsgi.multiprocess" como true, e sempre usa "sys" e "os" para obter
   os fluxos CGI e o ambiente necessários.

class wsgiref.handlers.IISCGIHandler

   Uma alternativa especializada para "CGIHandler", para uso ao
   implantar no servidor web IIS da Microsoft, sem ter definido a
   opção de configuração allowPathInfo (IIS>=7) ou metabase
   allowPathInfoForScriptMappings (IIS<7).

   Por padrão, o IIS fornece um "PATH_INFO" que duplica o
   "SCRIPT_NAME" na frente, causando problemas para aplicações WSGI
   que desejam implementar roteamento. Este manipulador remove
   qualquer caminho duplicado.

   O IIS pode ser configurado para passar o "PATH_INFO" correto, mas
   isso causa outro bug onde "PATH_TRANSLATED" está errado.
   Felizmente, essa variável raramente é usada e não é garantida pelo
   WSGI. No IIS<7, no entanto, a configuração só pode ser feita em um
   nível de vhost, afetando todos os outros mapeamentos de script,
   muitos dos quais quebram quando expostos ao bug "PATH_TRANSLATED".
   Por esse motivo, o IIS<7 quase nunca é implantado com a correção
   (mesmo o IIS7 raramente a usa porque ainda não há uma UI para ela).

   Não há como o código CGI dizer se a opção foi definida, então uma
   classe de manipulador separada é fornecida. Ela é usada da mesma
   forma que "CGIHandler", ou seja, chamando
   "IISCGIHandler().run(app)", onde "app" é o objeto de aplicação WSGI
   que você deseja invocar.

   Adicionado na versão 3.2.

class wsgiref.handlers.BaseCGIHandler(stdin, stdout, stderr, environ, multithread=True, multiprocess=False)

   Similar to "CGIHandler", but instead of using the "sys" and "os"
   modules, the CGI environment and I/O streams are specified
   explicitly. The *multithread* and *multiprocess* values are used to
   set the "wsgi.multithread" and "wsgi.multiprocess" flags for any
   applications run by the handler instance.

   This class is a subclass of "SimpleHandler" intended for use with
   software other than HTTP "origin servers".  If you are writing a
   gateway protocol implementation (such as CGI, FastCGI, SCGI, etc.)
   that uses a "Status:" header to send an HTTP status, you probably
   want to subclass this instead of "SimpleHandler".

class wsgiref.handlers.SimpleHandler(stdin, stdout, stderr, environ, multithread=True, multiprocess=False)

   Similar to "BaseCGIHandler", but designed for use with HTTP origin
   servers.  If you are writing an HTTP server implementation, you
   will probably want to subclass this instead of "BaseCGIHandler".

   This class is a subclass of "BaseHandler".  It overrides the
   "__init__()", "get_stdin()", "get_stderr()", "add_cgi_vars()",
   "_write()", and "_flush()" methods to support explicitly setting
   the environment and streams via the constructor.  The supplied
   environment and streams are stored in the "stdin", "stdout",
   "stderr", and "environ" attributes.

   The "write()" method of *stdout* should write each chunk in full,
   like "io.BufferedIOBase".

class wsgiref.handlers.BaseHandler

   This is an abstract base class for running WSGI applications.  Each
   instance will handle a single HTTP request, although in principle
   you could create a subclass that was reusable for multiple
   requests.

   "BaseHandler" instances have only one method intended for external
   use:

   run(app)

      Run the specified WSGI application, *app*.

   All of the other "BaseHandler" methods are invoked by this method
   in the process of running the application, and thus exist primarily
   to allow customizing the process.

   The following methods MUST be overridden in a subclass:

   _write(data)

      Buffer the bytes *data* for transmission to the client.  It's
      okay if this method actually transmits the data; "BaseHandler"
      just separates write and flush operations for greater efficiency
      when the underlying system actually has such a distinction.

   _flush()

      Force buffered data to be transmitted to the client.  It's okay
      if this method is a no-op (i.e., if "_write()" actually sends
      the data).

   get_stdin()

      Return an object compatible with "InputStream" suitable for use
      as the "wsgi.input" of the request currently being processed.

   get_stderr()

      Return an object compatible with "ErrorStream" suitable for use
      as the "wsgi.errors" of the request currently being processed.

   add_cgi_vars()

      Insert CGI variables for the current request into the "environ"
      attribute.

   Here are some other methods and attributes you may wish to
   override. This list is only a summary, however, and does not
   include every method that can be overridden.  You should consult
   the docstrings and source code for additional information before
   attempting to create a customized "BaseHandler" subclass.

   Attributes and methods for customizing the WSGI environment:

   wsgi_multithread

      The value to be used for the "wsgi.multithread" environment
      variable.  It defaults to true in "BaseHandler", but may have a
      different default (or be set by the constructor) in the other
      subclasses.

   wsgi_multiprocess

      The value to be used for the "wsgi.multiprocess" environment
      variable.  It defaults to true in "BaseHandler", but may have a
      different default (or be set by the constructor) in the other
      subclasses.

   wsgi_run_once

      The value to be used for the "wsgi.run_once" environment
      variable.  It defaults to false in "BaseHandler", but
      "CGIHandler" sets it to true by default.

   os_environ

      The default environment variables to be included in every
      request's WSGI environment.  By default, this is a copy of
      "os.environ" at the time that "wsgiref.handlers" was imported,
      but subclasses can either create their own at the class or
      instance level.  Note that the dictionary should be considered
      read-only, since the default value is shared between multiple
      classes and instances.

   server_software

      If the "origin_server" attribute is set, this attribute's value
      is used to set the default "SERVER_SOFTWARE" WSGI environment
      variable, and also to set a default "Server:" header in HTTP
      responses.  It is ignored for handlers (such as "BaseCGIHandler"
      and "CGIHandler") that are not HTTP origin servers.

      Alterado na versão 3.3: O termo "Python" é substituído por
      termos específicos de implementação, como "CPython", "Jython"
      etc.

   get_scheme()

      Return the URL scheme being used for the current request.  The
      default implementation uses the "guess_scheme()" function from
      "wsgiref.util" to guess whether the scheme should be "http" or
      "https", based on the current request's "environ" variables.

   setup_environ()

      Set the "environ" attribute to a fully populated WSGI
      environment.  The default implementation uses all of the above
      methods and attributes, plus the "get_stdin()", "get_stderr()",
      and "add_cgi_vars()" methods and the "wsgi_file_wrapper"
      attribute.  It also inserts a "SERVER_SOFTWARE" key if not
      present, as long as the "origin_server" attribute is a true
      value and the "server_software" attribute is set.

   Methods and attributes for customizing exception handling:

   log_exception(exc_info)

      Log the *exc_info* tuple in the server log.  *exc_info* is a
      "(type, value, traceback)" tuple.  The default implementation
      simply writes the traceback to the request's "wsgi.errors"
      stream and flushes it.  Subclasses can override this method to
      change the format or retarget the output, mail the traceback to
      an administrator, or whatever other action may be deemed
      suitable.

   traceback_limit

      The maximum number of frames to include in tracebacks output by
      the default "log_exception()" method.  If "None", all frames are
      included.

   error_output(environ, start_response)

      This method is a WSGI application to generate an error page for
      the user.  It is only invoked if an error occurs before headers
      are sent to the client.

      This method can access the current error using
      "sys.exception()", and should pass that information to
      *start_response* when calling it (as described in the "Error
      Handling" section of **PEP 3333**). In particular, the
      *start_response* callable should follow the "StartResponse"
      protocol.

      The default implementation just uses the "error_status",
      "error_headers", and "error_body" attributes to generate an
      output page.  Subclasses can override this to produce more
      dynamic error output.

      Note, however, that it's not recommended from a security
      perspective to spit out diagnostics to any old user; ideally,
      you should have to do something special to enable diagnostic
      output, which is why the default implementation doesn't include
      any.

   error_status

      The HTTP status used for error responses.  This should be a
      status string as defined in **PEP 3333**; it defaults to a 500
      code and message.

   error_headers

      The HTTP headers used for error responses.  This should be a
      list of WSGI response headers ("(name, value)" tuples), as
      described in **PEP 3333**.  The default list just sets the
      content type to "text/plain".

   error_body

      The error response body.  This should be an HTTP response body
      bytestring. It defaults to the plain text, "A server error
      occurred.  Please contact the administrator."

   Methods and attributes for **PEP 3333**'s "Optional Platform-
   Specific File Handling" feature:

   wsgi_file_wrapper

      A "wsgi.file_wrapper" factory, compatible with
      "wsgiref.types.FileWrapper", or "None".  The default value of
      this attribute is the "wsgiref.util.FileWrapper" class.

   sendfile()

      Override to implement platform-specific file transmission.  This
      method is called only if the application's return value is an
      instance of the class specified by the "wsgi_file_wrapper"
      attribute.  It should return a true value if it was able to
      successfully transmit the file, so that the default transmission
      code will not be executed. The default implementation of this
      method just returns a false value.

   Miscellaneous methods and attributes:

   origin_server

      This attribute should be set to a true value if the handler's
      "_write()" and "_flush()" are being used to communicate directly
      to the client, rather than via a CGI-like gateway protocol that
      wants the HTTP status in a special "Status:" header.

      This attribute's default value is true in "BaseHandler", but
      false in "BaseCGIHandler" and "CGIHandler".

   http_version

      If "origin_server" is true, this string attribute is used to set
      the HTTP version of the response set to the client.  It defaults
      to ""1.0"".

wsgiref.handlers.read_environ()

   Transcode CGI variables from "os.environ" to **PEP 3333** "bytes in
   unicode" strings, returning a new dictionary.  This function is
   used by "CGIHandler" and "IISCGIHandler" in place of directly using
   "os.environ", which is not necessarily WSGI-compliant on all
   platforms and web servers using Python 3 -- specifically, ones
   where the OS's actual environment is Unicode (i.e. Windows), or
   ones where the environment is bytes, but the system encoding used
   by Python to decode it is anything other than ISO-8859-1 (e.g. Unix
   systems using UTF-8).

   If you are implementing a CGI-based handler of your own, you
   probably want to use this routine instead of just copying values
   out of "os.environ" directly.

   Adicionado na versão 3.2.


"wsgiref.types" -- WSGI types for static type checking
======================================================

This module provides various types for static type checking as
described in **PEP 3333**.

Adicionado na versão 3.11.

class wsgiref.types.StartResponse

   A "typing.Protocol" describing **start_response()** callables
   (**PEP 3333**).

wsgiref.types.WSGIEnvironment

   A type alias describing a WSGI environment dictionary.

wsgiref.types.WSGIApplication

   A type alias describing a WSGI application callable.

class wsgiref.types.InputStream

   A "typing.Protocol" describing a **WSGI Input Stream**.

class wsgiref.types.ErrorStream

   A "typing.Protocol" describing a **WSGI Error Stream**.

class wsgiref.types.FileWrapper

   A "typing.Protocol" describing a **file wrapper**. See
   "wsgiref.util.FileWrapper" for a concrete implementation of this
   protocol.


Exemplos
========

This is a working "Hello World" WSGI application, where the
*start_response* callable should follow the "StartResponse" protocol:

   """
   Every WSGI application must have an application object - a callable
   object that accepts two arguments. For that purpose, we're going to
   use a function (note that you're not limited to a function, you can
   use a class for example). The first argument passed to the function
   is a dictionary containing CGI-style environment variables and the
   second variable is the callable object.
   """
   from wsgiref.simple_server import make_server


   def hello_world_app(environ, start_response):
       status = "200 OK"  # HTTP Status
       headers = [("Content-type", "text/plain; charset=utf-8")]  # HTTP Headers
       start_response(status, headers)

       # The returned object is going to be printed
       return [b"Hello World"]

   with make_server("", 8000, hello_world_app) as httpd:
       print("Serving on port 8000...")

       # Serve until process is killed
       httpd.serve_forever()

Example of a WSGI application serving the current directory, accept
optional directory and port number (default: 8000) on the command
line:

   """
   Small wsgiref based web server. Takes a path to serve from and an
   optional port number (defaults to 8000), then tries to serve files.
   MIME types are guessed from the file names, 404 errors are raised
   if the file is not found.
   """
   import mimetypes
   import os
   import sys
   from wsgiref import simple_server, util


   def app(environ, respond):
       # Get the file name and MIME type
       fn = os.path.join(path, environ["PATH_INFO"][1:])
       if "." not in fn.split(os.path.sep)[-1]:
           fn = os.path.join(fn, "index.html")
       mime_type = mimetypes.guess_file_type(fn)[0]

       # Return 200 OK if file exists, otherwise 404 Not Found
       if os.path.exists(fn):
           respond("200 OK", [("Content-Type", mime_type)])
           return util.FileWrapper(open(fn, "rb"))
       else:
           respond("404 Not Found", [("Content-Type", "text/plain")])
           return [b"not found"]


   if __name__ == "__main__":
       # Get the path and port from command-line arguments
       path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
       port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000

       # Make and start the server until control-c
       httpd = simple_server.make_server("", port, app)
       print(f"Serving {path} on port {port}, control-C to stop")
       try:
           httpd.serve_forever()
       except KeyboardInterrupt:
           print("Shutting down.")
           httpd.server_close()
