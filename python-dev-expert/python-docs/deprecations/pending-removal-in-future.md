Remoção pendente em versões futuras
***********************************

As APIs a seguir serão removidas no futuro, embora atualmente não haja
uma data agendada para sua remoção.

* "argparse":

  * O aninhamento de grupos de argumentos e o aninhamento de grupos
    mutuamente exclusivos estão descontinuado.

  * A passagem do argumento nomeado não documentado *prefix_chars*
    para "add_argument_group()" agora está descontinuado.

  * O conversor de tipo "argparse.FileType" está descontinuado.

* "builtins":

  * Geradores: A assinatura "throw(type, exc, tb)" e "athrow(type,
    exc, tb)" está descontinuada: use "throw(exc)" e "athrow(exc)", a
    assinatura do argumento único.

  * Atualmente Python aceita literais numéricos imediatamente seguidos
    por palavras reservadas como, por exemplo, "0in x", "1or x", "0if
    1else 2". Ele permite expressões confusas e ambíguas como "[0x1for
    x in y]" (que pode ser interpretada como "[0x1 for x in y]" ou
    "[0x1f or x in y]"). Um aviso de sintaxe é levantado se o literal
    numérico for imediatamente seguido por uma das palavras reservadas
    "and", "else", "for", "if", "in" , "is" e "or". Em uma versão
    futura, será alterado para um erro de sintaxe. (gh-87999)

  * Suporte para métodos "__index__()" e "__int__()" retornando tipo
    não-int: esses métodos serão necessários para retornar uma
    instância de uma subclasse estrita de "int".

  * Suporte para o método "__float__()" retornando uma subclasse
    estrita de "float": esses métodos serão necessários para retornar
    uma instância de "float".

  * Suporte para o método "__complex__()" retornando uma subclasse
    estrita de "complex": esses métodos serão necessários para
    retornar uma instância de "complex".

  * Passar um número complexo como argumento *real* ou *imag* no
    construtor "complex()" agora está descontinuado; deve ser passado
    apenas como um único argumento posicional. (Contribuição de Serhiy
    Storchaka em gh-109218.)

* "calendar": As constantes "calendar.January" e "calendar.February"
  foram descontinuadas e substituídas por "calendar.JANUARY" e
  "calendar.FEBRUARY". (Contribuição de Prince Roshan em gh-103636.)

* "codecs": use "open()" em vez de "codecs.open()". (gh-133038)

* "codeobject.co_lnotab": use o método "codeobject.co_lines()".

* "datetime":

  * "utcnow()": use "datetime.datetime.now(tz=datetime.UTC)".

  * "utcfromtimestamp()": use
    "datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)".

* "gettext": O valor de plural deve ser um número inteiro.

* "importlib":

  * O parâmetro *debug_override* de "cache_from_source()" foi
    descontinuado: em vez disso, use o parâmetro *optimization*.

* "importlib.metadata":

  * Interface de tupla "EntryPoints".

  * "None" implícito nos valores de retorno.

* "logging": o método "warn()" foi descontinuado desde o Python 3.3,
  use "warning()".

* "mailbox": O uso da entrada StringIO e do modo de texto foi
  descontinuado; em vez disso, use BytesIO e o modo binário.

* "os": chame "os.register_at_fork()" em um processo multithread.

* "os.path": "os.path.commonprefix()" está descontinuada; use
  "os.path.commonpath()" para prefixos de caminho. A função
  "os.path.commonprefix()" está sendo descontinuada por possuir nome e
  módulo enganosos. O uso dessa função não é seguro para prefixos de
  caminho, apesar de ela estar incluída em um módulo voltado à
  manipulação de caminhos; isso significa que é fácil introduzir
  acidentalmente vulnerabilidades de *path traversal* (travessia de
  diretórios) em programas Python ao utilizá-la.

* "pydoc.ErrorDuringImport": Um valor de tupla para o parâmetro
  *exc_info* foi descontinuado, use uma instância de exceção.

* "re": Regras mais rigorosas agora são aplicadas para referências
  numéricas de grupos e nomes de grupos em expressões regulares.
  Apenas a sequência de dígitos ASCII agora é aceita como referência
  numérica. O nome do grupo em padrões de bytes e strings de
  substituição agora pode conter apenas letras e dígitos ASCII e
  sublinhado. (Contribuição de Serhiy Storchaka em gh-91760.)

* "shutil": O parâmetro *onerror* de "rmtree()" foi descontinuado no
  Python 3.12; use o parâmetro *onexc*.

* Protocolos e opções de "ssl"

  * "ssl.SSLContext" sem argumento de protocolo foi descontinuado.

  * "ssl.SSLContext": "set_npn_protocols()" e
    "selected_npn_protocol()" foram descontinuados: use ALPN.

  * Opções de "ssl.OP_NO_SSL*"

  * Opções de "ssl.OP_NO_TLS*"

  * "ssl.PROTOCOL_SSLv3"

  * "ssl.PROTOCOL_TLS"

  * "ssl.PROTOCOL_TLSv1"

  * "ssl.PROTOCOL_TLSv1_1"

  * "ssl.PROTOCOL_TLSv1_2"

  * "ssl.TLSVersion.SSLv3"

  * "ssl.TLSVersion.TLSv1"

  * "ssl.TLSVersion.TLSv1_1"

* Métodos de "threading":

  * "threading.Condition.notifyAll()": use "notify_all()".

  * "threading.Event.isSet()": use "is_set()".

  * "threading.Thread.isDaemon()", "threading.Thread.setDaemon()": use
    o atributo "threading.Thread.daemon".

  * "threading.Thread.getName()", "threading.Thread.setName()": use o
    atributo "threading.Thread.name".

  * "threading.currentThread()": use "threading.current_thread()".

  * "threading.activeCount()": use "threading.active_count()".

* "typing.Text" (gh-92332).

* A classe interna "typing._UnionGenericAlias" não é mais usada para
  implementar "typing.Union". Para preservar a compatibilidade com
  usuários que utilizam esta classe privada, uma correção de
  compatibilidade será fornecida pelo menos até a versão 3.17 do
  Python. (Contribuição de Jelle Zijlstra em gh-105499.)

* "unittest.IsolatedAsyncioTestCase": foi descontinuado retornar um
  valor que não seja "None" de um caso de teste.

* Funções descontinuadas de "urllib.parse": use "urlparse()"

  * "splitattr()"

  * "splithost()"

  * "splitnport()"

  * "splitpasswd()"

  * "splitport()"

  * "splitquery()"

  * "splittag()"

  * "splittype()"

  * "splituser()"

  * "splitvalue()"

  * "to_bytes()"

* "wsgiref": "SimpleHandler.stdout.write()" não deve fazer gravações
  parciais.

* "xml.etree.ElementTree": testar o valor verdade de um "Element" está
  descontinuado. Em um lançamento futuro isso sempre retornará "True".
  Em vez disso, prefira os testes explícitos "len(elem)" ou "elem is
  not None".

* "sys._clear_type_cache()" está descontinuada: use
  "sys._clear_internal_caches()".
