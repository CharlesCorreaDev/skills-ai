Descontinuações
***************


Remoção pendente no Python 3.16
===============================

* O sistema de importação:

  * A definição de "__loader__" em um módulo enquanto falha na
    definição de "__spec__.loader" está descontinuado. No Python 3.16,
    "__loader__" deixará de ser definido ou levado em consideração
    pelo sistema de importação ou pela biblioteca padrão.

* "array":

  * O código de formato "'u'" ("wchar_t") foi descontinuado na
    documentação desde o Python 3.3 e em tempo de execução desde o
    Python 3.13. Use o código de formato "'w'" ("Py_UCS4") para
    caracteres Unicode.

* "asyncio":

  * "asyncio.iscoroutinefunction()" foi descontinuado e será removido
    no Python 3.16, use "inspect.iscoroutinefunction()" em vez disso.
    (Contribuição de Jiahao Li e Kumar Aditya em gh-122875.)

  * O sistema de políticas "asyncio" está descontinuado e será
    removido no Python 3.16. Em particular, as seguintes classes e
    funções estão descontinuadas:

    * "asyncio.AbstractEventLoopPolicy"

    * "asyncio.DefaultEventLoopPolicy"

    * "asyncio.WindowsSelectorEventLoopPolicy"

    * "asyncio.WindowsProactorEventLoopPolicy"

    * "asyncio.get_event_loop_policy()"

    * "asyncio.set_event_loop_policy()"

    Os usuários devem usar "asyncio.run()" ou "asyncio.Runner" com
    *loop_factory* para usar a implementação de loop de eventos
    desejada.

    por exemplo, para usar "asyncio.SelectorEventLoop" no Windows:

       import asyncio

       async def main():
           ...

       asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)

    (Contribuição de Kumar Aditya em gh-127949.)

* "builtins":

  * A inversão bit a bit em tipos booleanos, "~True" ou "~False" foi
    descontinuada desde o Python 3.12, pois produz resultados
    surpreendentes e não intuitivos ("-2" e "-1"). Use "not x" em vez
    disso para a negação lógica de um Booleano. No caso raro de você
    precisar da inversão bit a bit do inteiro subjacente, converta
    para "int" explicitamente ("~int(x)").

* "functools":

  * A chamada da implementação Python de "functools.reduce()" com
    *function* ou *sequence* como argumentos nomeados foi
    descontinuada desde o Python 3.14.

* "logging":

  * O suporte para manipuladores de registro personalizados com o
    argumento *strm* foi descontinuado e está programado para ser
    removido no Python 3.16. Em vez disso, defina manipuladores com o
    argumento *stream*. (Contribuição de Mariusz Felisiak em
    gh-115032.)

* "mimetypes":

  * Extensões válidas começam com um '.' ou estão vazias para
    "mimetypes.MimeTypes.add_type()". Extensões sem ponto estão
    descontinuadas e levantarão uma exceção "ValueError" no Python
    3.16. (Contribuição de Hugo van Kemenade em gh-75223.)

* "shutil":

  * A exceção "ExecError" foi descontinuada desde o Python 3.14. Ela
    não foi usada por nenhuma função em "shutil" desde o Python 3.4, e
    agora é um alias de "RuntimeError".

* "symtable":

  * O método "Class.get_methods" foi descontinuado desde o Python
    3.14.

* "sys":

  * A função "_enablelegacywindowsfsencoding()" foi descontinuada
    desde o Python 3.13. Use a variável de ambiente
    "PYTHONLEGACYWINDOWSFSENCODING".

* "sysconfig":

  * A função "sysconfig.expand_makefile_vars()" está descontinuada
    desde o Python 3.14. Em vez disso, use o argumento "vars" de
    "sysconfig.get_paths()".

* "tarfile":

  * O atributo não documentado e não utilizado "TarFile.tarfile" foi
    descontinuado desde o Python 3.13.


Remoção pendente no Python 3.17
===============================

* "datetime":

  * "strptime()" chama usando uma string de formato contendo "%e" (dia
    do mês) sem um ano. Isso está descontinuado desde Python 3.15.
    (Contribuição de Stan Ulbrych em gh-70647.)

* "collections.abc":

  * "collections.abc.ByteString" está agendado para remoção no Python
    3.17.

    Use "isinstance(obj, collections.abc.Buffer)" para testar se "obj"
    implementa o protocolo de buffer em tempo de execução. Para uso em
    anotações de tipo, use "Buffer" ou uma união que especifique
    explicitamente os tipos suportados pelo seu código (por exemplo,
    "bytes | bytearray | memoryview").

    "ByteString" foi originalmente concebido para ser uma classe
    abstrata que serviria como um supertipo de "bytes" e "bytearray".
    No entanto, como o ABC nunca teve métodos, saber que um objeto era
    uma instância de "ByteString" nunca lhe dizia nada de útil sobre o
    objeto. Outros tipos comuns de buffer, como "memoryview", também
    nunca foram entendidos como subtipos de "ByteString" (seja em
    tempo de execução ou por verificadores de tipo estáticos).

    Veja **PEP 688** para mais detalhes. (Contribuição de Shantanu
    Jain em gh-91896.)

* "encodings":

  * Passar nomes de *codificação* não ASCII para
    "encodings.normalize_encoding()" está descontinuado e sua remoção
    está prevista para o Python 3.17. (Contribuição de Stan Ulbrych em
    gh-136702.)

* "profile":

  * O módulo "profile" está descontinuado e será removido no Python
    3.17. Em vez disso, utilize "profiling.tracing", que oferece uma
    API compatível. Consulte a **PEP 799** para obter detalhes.
    (Contribuição de Pablo Galindo e László Kiss Kollár em gh-138122.)

* "webbrowser":

  * "webbrowser.MacOSXOSAScript" está descontinuado em favor de
    "webbrowser.MacOS". (gh-137586)

* "typing":

  * Antes do Python 3.14, as uniões antigas eram implementadas usando
    a classe privada "typing._UnionGenericAlias". Essa classe não é
    mais necessária para a implementação, mas foi mantida para
    compatibilidade com versões anteriores, com remoção prevista para
    o Python 3.17. Os usuários devem usar auxiliares de introspecção
    documentados, como "typing.get_origin()" e "typing.get_args()", em
    vez de depender de detalhes de implementação privada.

  * "typing.ByteString", obsoleto desde o Python 3.9, está programado
    para ser removido no Python 3.17.

    Use "isinstance(obj, collections.abc.Buffer)" para testar se "obj"
    implementa o protocolo de buffer em tempo de execução. Para uso em
    anotações de tipo, use "Buffer" ou uma união que especifique
    explicitamente os tipos suportados pelo seu código (por exemplo,
    "bytes | bytearray | memoryview").

    "ByteString" foi originalmente concebido para ser uma classe
    abstrata que serviria como um supertipo de "bytes" e "bytearray".
    No entanto, como o ABC nunca teve métodos, saber que um objeto era
    uma instância de "ByteString" nunca lhe dizia nada de útil sobre o
    objeto. Outros tipos comuns de buffer, como "memoryview", também
    nunca foram entendidos como subtipos de "ByteString" (seja em
    tempo de execução ou por verificadores de tipo estáticos).

    Veja **PEP 688** para mais detalhes. (Contribuição de Shantanu
    Jain em gh-91896.)

* "tkinter":

  * Os métodos "trace_variable()", "trace()" (um apelido de
    "trace_variable()"), "trace_vdelete()" e "trace_vinfo()" da classe
    "tkinter.Variable", descontinuados desde o Python 3.14, têm
    remoção prevista para o Python 3.17. Em vez deles, utilize
    "trace_add()", "trace_remove()" e "trace_info()". (Contribuição de
    Serhiy Storchaka em gh-120220.)


Remoção pendente no Python 3.18
===============================

* Não aceita mais um valor booleano quando um descritor de arquivo é
  esperado. (Contribuição de Serhiy Storchaka em gh-82626.)

* "decimal":

  * O especificador de formato de "Decimal" não padrão e não
    documentado "'N'", que só é suportado na implementação C do módulo
    "decimal", foi descontinuada desde o Python 3.13. (Contribuição de
    Serhiy Storchaka em gh-89902.)

* Descontinuações definidas por **PEP 829**:

  * Linhas de "import" em arquivos "*name*.pth" são silenciosamente
    ignoradas.

  (Contribuição de Barry Warsaw em gh-148641.)


Remoção pendente no Python 3.19
===============================

* "ctypes":

  * Troca implícita para o layout de estrutura compatível com MSVC
    definindo "_pack_", mas não "_layout_" em plataformas não Windows.

* "hashlib":

  * Em construtores de funções de hash, como "new()", ou nos
    construtores nomeados diretamente pelo algoritmo de hash, como
    "md5()" e "sha256()", o parâmetro opcional de dados iniciais
    também podia ser passado como um argumento nomeado "data=" ou
    "string=" em várias implementações do "hashlib".

    O suporte ao nome do argumento nomeado "string" está agora
    descontinuado e previsto para ser removido no Python 3.19.

    Antes do Python 3.13, o parâmetro nomeado "string" não era
    suportado corretamente, dependendo da implementação de funções de
    hash do backend. Dê preferência a passar os dados iniciais como um
    argumento posicional para garantir a máxima compatibilidade com
    versões anteriores.

* "http.cookies":

  * "http.cookies.Morsel.js_output()" está descontinuado e será
    removido no Python 3.19.

  * "http.cookies.BaseCookie.js_output()" está descontinuado e será
    removido no Python 3.19.

* "imaplib":

  * A alteração de "IMAP4.file" agora está descontinuado e programado
    para remoção no Python 3.19. Esta propriedade agora não é
    utilizada e alterar seu valor não fecha automaticamente o arquivo
    atual.

    Antes do Python 3.14, essa propriedade era usada para implementar
    os métodos "read()" e "readline()" correspondentes para "IMAP4",
    mas isso não ocorre mais desde então.


Remoção pendente no Python 3.20
===============================

* Chamar o método "__new__()" de "struct.Struct" sem o argumento
  *format* está descontinuado e será removido no Python 3.20. Chamar o
  método "__init__()" em objetos "Struct" já inicializados está
  descontinuado e será removido no Python 3.20.

  (Contribuição de Sergey B Kirpichev e Serhiy Storchaka em
  gh-143715.)

* Os atributos "__version__", "version" e "VERSION" foram
  descontinuados nestes módulos da biblioteca padrão e serão removidos
  no Python 3.20. Utilize "sys.version_info" em seu lugar.

  * "argparse"

  * "csv"

  * "ctypes"

  * "ctypes.macholib"

  * "decimal" (use "decimal.SPEC_VERSION")

  * "http.server"

  * "imaplib"

  * "ipaddress"

  * "json"

  * "logging" ("__date__" também descontinuado)

  * "optparse"

  * "pickle"

  * "platform"

  * "re"

  * "socketserver"

  * "tabnanny"

  * "tarfile"

  * "tkinter.font"

  * "tkinter.ttk"

  * "wsgiref.simple_server"

  * "xml.etree.ElementTree"

  * "xml.sax.expatreader"

  * "xml.sax.handler"

  * "zlib"

  (Contribuição de Hugo van Kemenade e Stan Ulbrych em gh-76007.)

* Descontinuações definidas por **PEP 829**:

  * Avisos são produzidos para linhas "import" encontradas em arquivos
    "*name*.pth".

  * Arquivos "*name*.pth" não são mais decodificados usando a
    codificação da localidade (*locale encoding*) por padrão. Eles
    **DEVEM** estar codificados em "utf-8-sig".

  (Contribuição de Barry Warsaw em gh-148641.)

* "ast":

  * A criação de instâncias de nós abstratos da AST (como "ast.AST" ou
    "ast.expr") está descontinuada e levantará um erro no Python 3.20.

* "typing":

  * A verificação com "isinstance()" e "issubclass()" está
    descontinuado em classes de protocolo que não foram explicitamente
    decoradas com "runtime_checkable()", mas que herdam de uma classe
    de protocolo verificável em tempo de execução. Isso levantará em
    um "TypeError" no Python 3.20.

    (Contribuição de Bartosz Sławecki em gh-132604.)


Remoção pendente em versões futuras
===================================

As APIs a seguir serão removidas no futuro, embora atualmente não haja
uma data agendada para sua remoção.

* "argparse":

  * O aninhamento de grupos de argumentos e o aninhamento de grupos
    mutuamente exclusivos estão descontinuado.

  * A passagem do argumento nomeado não documentado *prefix_chars*
    para "add_argument_group()" agora está descontinuado.

  * O conversor de tipo "argparse.FileType" está descontinuado.

* "builtins":

  * Geradores: a assinatura "throw(type, exc, tb)" e "athrow(type,
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

* "calendar": as constantes "calendar.January" e "calendar.February"
  foram descontinuadas e substituídas por "calendar.JANUARY" e
  "calendar.FEBRUARY". (Contribuição de Prince Roshan em gh-103636.)

* "codecs": use "open()" em vez de "codecs.open()". (gh-133038)

* "codeobject.co_lnotab": use o método "codeobject.co_lines()".

* "datetime":

  * "utcnow()": use "datetime.datetime.now(tz=datetime.UTC)".

  * "utcfromtimestamp()": use
    "datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)".

* "gettext": o valor de plural deve ser um número inteiro.

* "importlib":

  * O parâmetro *debug_override* de "cache_from_source()" foi
    descontinuado: em vez disso, use o parâmetro *optimization*.

* "importlib.metadata":

  * Interface de tupla "EntryPoints".

  * "None" implícito nos valores de retorno.

* "logging": o método "warn()" foi descontinuado desde o Python 3.3,
  use "warning()".

* "mailbox": o uso da entrada StringIO e do modo de texto foi
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

* "pydoc.ErrorDuringImport": um valor de tupla para o parâmetro
  *exc_info* foi descontinuado, use uma instância de exceção.

* "re": regras mais rigorosas agora são aplicadas para referências
  numéricas de grupos e nomes de grupos em expressões regulares.
  Apenas a sequência de dígitos ASCII agora é aceita como referência
  numérica. O nome do grupo em padrões de bytes e strings de
  substituição agora pode conter apenas letras e dígitos ASCII e
  sublinhado. (Contribuição de Serhiy Storchaka em gh-91760.)

* "shutil": o parâmetro *onerror* de "rmtree()" foi descontinuado no
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


descontinuações suave
=====================

Não há planos para remover APIs *suavemente descontinuadas*

* "re.match()" e "re.Pattern.match()" estão agora *suavemente
  descontinuado*s em favor das novas APIs "re.prefixmatch()" e
  "re.Pattern.prefixmatch()", adicionadas como nomes alternativos e
  mais explícitos. Elas visam reduzir a confusão sobre o significado
  de *match*, seguindo o princípio do Zen do Python: *"Explícito é
  melhor que implícito"*. A maioria das bibliotecas de expressões
  regulares de outras linguagens utiliza uma API chamada *match* para
  a funcionalidade que o Python sempre chamou de *search*.

  **Não** planejamos remover o nome mais antigo "match()", pois ele
  tem sido utilizado no código há mais de 30 anos. Códigos que
  oferecem suporte a versões mais antigas do Python devem continuar
  utilizando "match()", enquanto novos códigos devem dar preferência a
  "prefixmatch()". Veja prefixmatch() vs. match().

  (Contribuição de Gregory P. Smith em gh-86519 e Hugo van Kemenade em
  gh-148100.)

* O uso dos códigos de tipo de formato "'F'" e "'D'" do módulo
  "struct" está agora *suavemente descontinuado* em favor das formas
  de duas letras "'Zf'" e "'Zd'". (Contribuição de Sergey B Kirpichev
  em gh-121249.)


Descontinuações na API C
========================


Remoção pendente no Python 3.15
-------------------------------

* A "PyImport_ImportModuleNoBlock()": Use "PyImport_ImportModule()"

* "PyWeakref_GetObject()" e "PyWeakref_GET_OBJECT()": Use
  "PyWeakref_GetRef()". O projeto pythoncapi-compat pod ser usado para
  obter "PyWeakref_GetRef()" no Python 3.12 e versões mais antigas.

* "PyUnicode_AsDecodedObject()": use "PyCodec_Decode()".

* "PyUnicode_AsDecodedUnicode()": Use "PyCodec_Decode()"; Note que
  alguns codecs (por exemplo, "base64") podem retornar um tipo
  diferente de "str", tal como "bytes".

* "PyUnicode_AsEncodedObject()": use "PyCodec_Encode()".

* "PyUnicode_AsEncodedUnicode()": Use "PyCodec_Encode()"; Note que
  alguns codecs (por exemplo, "base64") podem retornar um tipo
  diferente de "bytes", tal com "str".

* Funções de inicialização do Python, descontinuadas no Python 3.13:

  * "Py_GetPath()": Use "PyConfig_Get("module_search_paths")"
    ("sys.path").

  * "Py_GetPrefix()": Use "PyConfig_Get("base_prefix")"
    ("sys.base_prefix"). Use "PyConfig_Get("prefix")" ("sys.prefix")
    se ambientes virtuais precisarem ser tratados.

  * "Py_GetExecPrefix()": Use "PyConfig_Get("base_exec_prefix")"
    ("sys.base_exec_prefix"). Use "PyConfig_Get("exec_prefix")"
    ("sys.exec_prefix") se ambientes virtuais precisarem ser tratados.

  * "Py_GetProgramFullPath()": Use "PyConfig_Get("executable")"
    ("sys.executable").

  * "Py_GetProgramName()": Use "PyConfig_Get("executable")"
    ("sys.executable").

  * "Py_GetPythonHome()": Use "PyConfig_Get("home")" ou a variável de
    ambiente "PYTHONHOME".

  O projeto pythoncapi-compat pode ser usado para obter
  "PyConfig_Get()" no Python 3.13 e versões anteriores.

* Funções para configurar a inicialização do Python, descontinuadas no
  Python 3.11:

  * "PySys_SetArgvEx()": defina "PyConfig.argv".

  * "PySys_SetArgv()": defina "PyConfig.argv".

  * "Py_SetProgramName()": defina "PyConfig.program_name".

  * "Py_SetPythonHome()": defina "PyConfig.home".

  * "PySys_ResetWarnOptions()": Limpe "sys.warnoptions" e
    "warnings.filters".

  A API "Py_InitializeFromConfig()" deve ser usada com "PyConfig".

* Variáveis de configuração globais

  * "Py_DebugFlag": Use "PyConfig.parser_debug" ou
    "PyConfig_Get("parser_debug")".

  * "Py_VerboseFlag": Use "PyConfig.verbose" ou
    "PyConfig_Get("verbose")".

  * "Py_QuietFlag": Use "PyConfig.quiet" ou "PyConfig_Get("quiet")".

  * "Py_InteractiveFlag": Use "PyConfig.interactive" ou
    "PyConfig_Get("interactive")".

  * "Py_InspectFlag": Use "PyConfig.inspect" ou
    "PyConfig_Get("inspect")".

  * "Py_OptimizeFlag": Use "PyConfig.optimization_level" ou
    "PyConfig_Get("optimization_level")".

  * "Py_NoSiteFlag": Use "PyConfig.site_import" ou
    "PyConfig_Get("site_import")".

  * "Py_BytesWarningFlag": Use "PyConfig.bytes_warning" ou
    "PyConfig_Get("bytes_warning")".

  * "Py_FrozenFlag": Use "PyConfig.pathconfig_warnings" ou
    "PyConfig_Get("pathconfig_warnings")".

  * "Py_IgnoreEnvironmentFlag": Use "PyConfig.use_environment" ou
    "PyConfig_Get("use_environment")".

  * "Py_DontWriteBytecodeFlag": Use "PyConfig.write_bytecode" ou
    "PyConfig_Get("write_bytecode")".

  * "Py_NoUserSiteDirectory": Use "PyConfig.user_site_directory" ou
    "PyConfig_Get("user_site_directory")".

  * "Py_UnbufferedStdioFlag": Use "PyConfig.buffered_stdio" ou
    "PyConfig_Get("buffered_stdio")".

  * "Py_HashRandomizationFlag": Use "PyConfig.use_hash_seed" e
    "PyConfig.hash_seed" ou "PyConfig_Get("hash_seed")".

  * "Py_IsolatedFlag": Use "PyConfig.isolated" ou
    "PyConfig_Get("isolated")".

  * "Py_LegacyWindowsFSEncodingFlag": Use
    "PyPreConfig.legacy_windows_fs_encoding" ou
    "PyConfig_Get("legacy_windows_fs_encoding")".

  * "Py_LegacyWindowsStdioFlag": Use "PyConfig.legacy_windows_stdio"
    ou "PyConfig_Get("legacy_windows_stdio")".

  * "Py_FileSystemDefaultEncoding", "Py_HasFileSystemDefaultEncoding":
    Use "PyConfig.filesystem_encoding" ou
    "PyConfig_Get("filesystem_encoding")".

  * "Py_FileSystemDefaultEncodeErrors": Use
    "PyConfig.filesystem_errors" ou
    "PyConfig_Get("filesystem_errors")".

  * "Py_UTF8Mode": Use "PyPreConfig.utf8_mode" ou
    "PyConfig_Get("utf8_mode")". (veja "Py_PreInitialize()")

  A API "Py_InitializeFromConfig()" deve ser usada com "PyConfig" para
  definir essas opções. Ou "PyConfig_Get()" pode ser usado para obter
  essas opções em tempo de execução.


Remoção pendente no Python 3.16
-------------------------------

* A cópia empacotada do "libmpdec".


Remoção pendente no Python 3.18
-------------------------------

* As seguintes funções privadas estão descontinuado e planejadas para
  remoção no Python 3.18:

  * "_PyBytes_Join()": use "PyBytes_Join()".

  * "_PyDict_GetItemStringWithError()": use
    "PyDict_GetItemStringRef()".

  * "_PyDict_Pop()": use "PyDict_Pop()".

  * "_PyLong_Sign()": use "PyLong_GetSign()".

  * "_PyLong_FromDigits()" e "_PyLong_New()": use
    "PyLongWriter_Create()".

  * "_PyThreadState_UncheckedGet()": use
    "PyThreadState_GetUnchecked()".

  * "_PyUnicode_AsString()": use "PyUnicode_AsUTF8()".

  * "_PyUnicodeWriter_Init()": substitua
    "_PyUnicodeWriter_Init(&writer)" com "writer =
    PyUnicodeWriter_Create(0)".

  * "_PyUnicodeWriter_Finish()": substitua
    "_PyUnicodeWriter_Finish(&writer)" por
    "PyUnicodeWriter_Finish(writer)".

  * "_PyUnicodeWriter_Dealloc()": substitua
    "_PyUnicodeWriter_Dealloc(&writer)" por
    "PyUnicodeWriter_Discard(writer)".

  * "_PyUnicodeWriter_WriteChar()": substituta
    "_PyUnicodeWriter_WriteChar(&writer, ch)" com
    "PyUnicodeWriter_WriteChar(writer, ch)".

  * "_PyUnicodeWriter_WriteStr()": substitua
    "_PyUnicodeWriter_WriteStr(&writer, str)" por
    "PyUnicodeWriter_WriteStr(writer, str)".

  * "_PyUnicodeWriter_WriteSubstring()": substitua
    "_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)" por
    "PyUnicodeWriter_WriteSubstring(writer, str, start, end)".

  * "_PyUnicodeWriter_WriteASCIIString()": substitua
    "_PyUnicodeWriter_WriteASCIIString(&writer, str, size)" por
    "PyUnicodeWriter_WriteASCII(writer, str, size)".

  * "_PyUnicodeWriter_WriteLatin1String()": substitua
    "_PyUnicodeWriter_WriteLatin1String(&writer, str, size)"
    decodificando a string com "PyUnicode_DecodeLatin1()", gravando o
    resultado com "PyUnicodeWriter_WriteStr()" e liberando o resultado
    com "Py_DECREF()".

  * "_PyUnicodeWriter_Prepare()": (sem substituto).

  * "_PyUnicodeWriter_PrepareKind()": (sem substituto).

  * "_Py_HashPointer()": use "Py_HashPointer()".

  * "_Py_fopen_obj()": use "Py_fopen()".

  O projeto pythoncapi-compat pode ser usado para obter essas novas
  funções públicas no Python 3.13 e versões anteriores. (Contribuição
  de Victor Stinner em gh-128863.)


Remoção pendente no Python 3.19
-------------------------------

* **PEP 456** suporte para incorporadores à definição do esquema de
  hashing de strings.


Remoção pendente no Python 3.20
-------------------------------

* "_PyObject_CallMethodId()", "_PyObject_GetAttrId()" e
  "_PyUnicode_FromId()" foram descontinuadas desde o 3.15 e serão
  removidas na versão 3.20. Em vez delas, use
  "PyUnicode_InternFromString()" and armazene em cache o resultado no
  estado do módulo e chame "PyObject_CallMethod()" ou
  "PyObject_GetAttr()". (Contribuição de Victor Stinner em gh-141049.)

* O campo "cval" em "PyComplexObject" (gh-128813). Use
  "PyComplex_AsCComplex()" e "PyComplex_FromCComplex()" para converter
  um número complexo Python de/para a representação C de "Py_complex".

* Macros "Py_MATH_PIl" e "Py_MATH_El".


Remoção pendente em versões futuras
-----------------------------------

As APIs a seguir foram descontinuadas e serão removidas, embora
atualmente não haja uma data agendada para sua remoção.

* "Py_TPFLAGS_HAVE_FINALIZE": desnecessária desde o Python 3.8.

* "PyErr_Fetch()": use "PyErr_GetRaisedException()".

* "PyErr_NormalizeException()": use "PyErr_GetRaisedException()".

* "PyErr_Restore()": use "PyErr_SetRaisedException()".

* "PyModule_GetFilename()": use "PyModule_GetFilenameObject()".

* "PyOS_AfterFork()": use "PyOS_AfterFork_Child()".

* "PySlice_GetIndicesEx()": use "PySlice_Unpack()" e
  "PySlice_AdjustIndices()".

* "PyUnicode_READY()": desnecessário desde o Python 3.12

* "PyErr_Display()": use "PyErr_DisplayException()".

* "_PyErr_ChainExceptions()": use "_PyErr_ChainExceptions1()".

* O membro "PyBytesObject.ob_shash": chame "PyObject_Hash()".

* API do Thread Local Storage (TLS):

  * "PyThread_create_key()": use "PyThread_tss_alloc()".

  * "PyThread_delete_key()": use "PyThread_tss_free()".

  * "PyThread_set_key_value()": use "PyThread_tss_set()".

  * "PyThread_get_key_value()": use "PyThread_tss_get()".

  * "PyThread_delete_key_value()": use "PyThread_tss_delete()".

  * "PyThread_ReInitTLS()": desnecessário desde o Python 3.7.
