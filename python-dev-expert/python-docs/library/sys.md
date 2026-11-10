"sys" --- Parâmetros e funções específicas do sistema
*****************************************************

======================================================================

Este módulo fornece acesso a algumas variáveis usadas ou mantidas pelo
interpretador e a funções que interagem fortemente com o
interpretador. Sempre disponível. A menos que explicitamente indicado
o contrário, todas as variáveis são somente leitura.

sys.abi_info

   Adicionado na versão 3.15.

   An object containing information about the ABI of the currently
   running Python interpreter. It should include information that
   affect the CPython ABI in ways that require a specific build of the
   interpreter chosen from variants that can co-exist on a single
   machine. For example, it does not encode the base OS (Linux or
   Windows), but does include pointer size since some systems support
   both 32- and 64-bit builds. The available entries are the same on
   all platforms; e.g. *pointer_size* is available even on 64-bit-only
   architectures.

   The following attributes are available:

   abi_info.pointer_bits

      The width of pointers in bits, as an integer, equivalent to "8 *
      sizeof(void *)". Usually, this is  "32" or "64".

   abi_info.free_threaded

      A Boolean indicating whether the interpreter was built with
      *free threading* support. This reflects either the presence of
      the "--disable-gil" "configure" option (on Unix) or setting the
      "DisableGil" property (on Windows).

   abi_info.debug

      A Boolean indicating whether the interpreter was built in debug
      mode. This reflects either the presence of the "--with-pydebug"
      "configure" option (on Unix) or the "Debug" configuration (on
      Windows).

   abi_info.byteorder

      A string indicating the native byte order, either "'big'" or
      "'little'". This is the same as the "byteorder" attribute.

sys.abiflags

   Em sistemas POSIX onde Python foi construído com o script
   "configure" padrão, ele contém os sinalizadores ABI conforme
   especificado por **PEP 3149**.

   Adicionado na versão 3.2.

   Alterado na versão 3.8: Os sinalizadores padrões se tornaram uma
   string vazia (o sinalizador "m" para pymalloc foi removido).

   Disponibilidade: Unix.

sys.addaudithook(hook)

   Anexa o *hook* chamável à lista de ganchos de auditoria ativos para
   o (sub)interpretador atual.

   Quando um evento de auditoria é levantado através da função
   "sys.audit()", cada gancho será chamado na ordem em que foi
   adicionado com o nome do evento e a tupla de argumentos. Ganchos
   nativos adicionados por "PySys_AddAuditHook()" são chamados
   primeiro, seguidos por ganchos adicionados no (sub)interpretador
   atual. Os ganchos podem registrar o evento, levantar uma exceção
   para cancelar a operação ou encerrar o processo completamente.

   Observe que os ganchos de auditoria são principalmente para coletar
   informações sobre ações internas ou não observáveis, seja por
   Python ou bibliotecas escritas em Python. Eles não são adequados
   para implementar um ambiente isolado estilo "sandbox". Em
   particular, o código malicioso pode desabilitar ou ignorar os
   ganchos adicionados usando esta função. No mínimo, quaisquer
   ganchos sensíveis à segurança devem ser adicionados usando a API C
   "PySys_AddAuditHook()" antes de inicializar o tempo de execução, e
   quaisquer módulos que permitam modificação arbitrária da memória
   (como "ctypes") devem ser completamente removidos ou monitorados de
   perto.

   Chamar "sys.addaudithook()" levantará um evento de auditoria
   denominado "sys.addaudithook" sem argumentos. Se qualquer gancho
   existente levantar uma exceção derivada de "RuntimeError", o novo
   gancho não será adicionado e a exceção será suprimida. Como
   resultado, os chamadores não podem presumir que seu gancho foi
   adicionado, a menos que controlem todos os ganchos existentes.

   Veja tabela de eventos de auditoria para todos os eventos
   levantados pelo CPython, e **PEP 578** para a discussão do projeto
   original.

   Adicionado na versão 3.8.

   Alterado na versão 3.8.1: Exceções derivadas de "Exception", mas
   não de "RuntimeError", não são mais suprimidas.

   Quando o rastreamento está ativado (consulte "settrace()"), os
   ganchos do Python são rastreados apenas se o chamável tiver um
   membro "__cantrace__" definido como um valor verdadeiro. Caso
   contrário, as funções de rastreamento ignorarão o gancho.

sys.argv

   A lista de argumentos de linha de comando passados para um script
   Python. "argv[0]" é o nome do script (depende do sistema
   operacional se este é um nome de caminho completo ou não). Se o
   comando foi executado usando a opção de linha de comando "-c" para
   o interpretador, "argv[0]" é definido como a string "'-c'". Se
   nenhum nome de script foi passado para o interpretador Python,
   "argv[0]" é a string vazia.

   Para percorrer a entrada padrão ou a lista de arquivos fornecida na
   linha de comando, consulte o módulo "fileinput".

   Veja também "sys.orig_argv".

   Nota:

     No Unix, os argumentos da linha de comando são passados por bytes
     do sistema operacional. O Python os decodifica com a codificação
     do sistema de arquivos e o tratador de erros "surrogateescape".
     Quando você precisar de bytes originais, você pode obtê-los por
     "[os.fsencode(arg) for arg in sys.argv]".

sys.audit(event, *args)

   Levanta um evento de auditoria e aciona quaisquer ganchos de
   auditoria ativos. *event* é uma string que identifica o evento e
   *args* pode conter argumentos opcionais com mais informações sobre
   o evento. O número e os tipos de argumentos para um determinado
   evento são considerados uma API pública e estável e não devem ser
   modificados entre as versões.

   Por exemplo, um evento de auditoria é denominado "os.chdir". Este
   evento tem um argumento chamado *path* que conterá o novo diretório
   de trabalho solicitado.

   "sys.audit()" chamará os ganchos de auditoria existentes, passando
   o nome do evento e os argumentos, e levantará novamente a primeira
   exceção de qualquer gancho. Em geral, se uma exceção for levantada,
   ela não deve ser tratada e o processo deve ser encerrado o mais
   rápido possível. Isso permite que as implementações de gancho
   decidam como responder a eventos específicos: elas podem
   simplesmente registrar o evento ou abortar a operação levantando
   uma exceção.

   Ganchos são adicionados usando as funções "sys.addaudithook()" ou
   "PySys_AddAuditHook()".

   O equivalente nativo desta função é "PySys_Audit()". Usar a função
   nativa é preferível quando possível.

   Veja tabela de eventos de auditoria para todos os eventos
   levantados pelo CPython.

   Adicionado na versão 3.8.

sys.base_exec_prefix

   Equivalente a "exec_prefix", mas referindo-se à instalação base do
   Python.

   Ao executar em Ambientes virtuais, "exec_prefix" é substituído pelo
   prefixo do ambiente virtual. "base_exec_prefix", por outro lado,
   não muda e sempre aponta para a instalação base do Python. Consulte
   Ambientes virtuais para obter mais informações.

   Adicionado na versão 3.3.

sys.base_prefix

   Equivalente a "prefix", mas referindo-se à instalação base do
   Python.

   Ao executar em ambiente virtual, "prefix" é substituído pelo
   prefixo do ambiente virtual. "base_prefix", por outro lado, não
   muda e sempre aponta para a instalação base do Python. Consulte
   Ambientes virtuais para obter mais informações.

   Adicionado na versão 3.3.

sys.byteorder

   Um indicador da ordem nativa de bytes. Isso terá o valor "'big'" em
   plataformas big endian (byte mais significativo primeiro) e
   "'little'" em plataformas little endian (byte menos significativo
   primeiro).

sys.builtin_module_names

   Uma tupla de strings contendo os nomes de todos os módulos
   compilados neste interpretador Python. (Esta informação não está
   disponível de nenhuma outra forma --- "modules.keys()" apenas lista
   os módulos importados.)

   Veja também a lista de "sys.stdlib_module_names".

sys.call_tracing(func, args)

   Chama "func(*args)", enquanto o rastreamento está habilitado. O
   estado de rastreamento é salvo e restaurado posteriormente. Isso
   deve ser chamado de um depurador de um ponto de verificação, para
   depurar ou analisar o desempenho recursivamente algum outro código.

   O rastreamento é suspenso ao chamar uma função de rastreamento
   definida por "settrace()" ou "setprofile()" para evitar recursão
   infinita. "call_tracing()" habilita a recursão explícita da função
   de rastreamento.

sys.copyright

   Uma string contendo os direitos autorais pertencentes ao
   interpretador Python.

sys._clear_type_cache()

   Limpa o cache de tipo interno. O cache de tipo é usado para
   acelerar pesquisas de atributos e métodos. Use a função *apenas*
   para descartar referências desnecessárias durante a depuração de
   vazamento de referência.

   Esta função deve ser usada apenas para fins internos e
   especializados.

   Descontinuado desde a versão 3.13: Em vez disso, use a função mais
   geral "_clear_internal_caches()".

sys._clear_internal_caches()

   Limpa todos os caches internos relacionados ao desempenho. Use esta
   função *somente* para liberar referências e blocos de memória
   desnecessários ao procurar por vazamentos.

   Adicionado na versão 3.13.

sys._current_frames()

   Retorna um dicionário mapeando o identificador de cada encadeamento
   (*thread*) para o quadro de pilha mais alto atualmente ativo nesse
   encadeamento no momento em que a função é chamada. Observe que as
   funções no módulo "traceback" podem construir a pilha de chamadas
   dado tal quadro.

   Isso é mais útil para fazer a depuração de impasses: esta função
   não requer a cooperação das threads em impasse e as pilhas de
   chamadas de tais threads são congeladas enquanto permanecerem em
   impasse (*deadlock*). O quadro retornado para uma thread sem
   impasse pode não ter nenhuma relação com a atividade atual da
   thread no momento em que o código de chamada examina o quadro.

   Esta função deve ser usada apenas para fins internos e
   especializados.

   Levanta um evento de auditoria "sys._current_frames" sem
   argumentos.

sys._current_exceptions()

   Retorna um dicionário mapeando o identificador de cada encadeamento
   (*thread*) para a exceção mais alta atualmente ativo nesse
   encadeamento no momento em que a função é chamada. Se um
   encadeamento não estiver manipulando uma exceção no momento, ele
   não será incluído no dicionário de resultados.

   Isso é mais útil para criação de perfil estatístico.

   Esta função deve ser usada apenas para fins internos e
   especializados.

   Levanta um evento de auditoria "sys._current_exceptions" sem
   argumentos.

   Alterado na versão 3.12: Cada valor no dicionário agora é uma única
   instância de exceção, em vez de uma tupla de 3 elementos, como
   retornado de "sys.exc_info()".

sys.breakpointhook()

   Esta função de gancho é chamada pela função embutida
   "breakpoint()". Por padrão, ela leva você ao depurador "pdb", mas
   pode ser configurado para qualquer outra função para que você possa
   escolher qual depurador será usado.

   A assinatura dessa função depende do que ela chama. Por exemplo, a
   ligação padrão (por exemplo, "pdb.set_trace()") não espera nenhum
   argumento, mas você pode vinculá-la a uma função que espera
   argumentos adicionais (posicionais e/ou nomeados). A função
   embutida "breakpoint()" passa seus "*args" e "**kws" diretamente. O
   que quer que "breakpointhooks()" retorne é retornado de
   "breakpoint()".

   A implementação padrão primeiro consulta a variável de ambiente
   "PYTHONBREAKPOINT". Se for definido como ""0"", então esta função
   retorna imediatamente; ou seja, é um no-op. Se a variável de
   ambiente não for definida, ou for definida como uma string vazia,
   "pdb.set_trace()" será chamado. Caso contrário, essa variável deve
   nomear uma função a ser executada, usando a nomenclatura de
   importação pontilhada do Python, por exemplo
   "package.subpackage.module.function". Neste caso,
   "package.subpackage.module" seria importado e o módulo resultante
   deve ter um chamável chamado "function()". Isso é executado,
   passando "*args" e "**kws", e qualquer que seja o retorno de
   "function()", "sys.breakpointhook()" retorna para a função embutida
   "breakpoint()".

   Observe que se algo der errado ao importar o chamável nomeado por
   "PYTHONBREAKPOINT", uma "RuntimeWarning" é relatado e o ponto de
   interrupção é ignorado.

   Observe também que se "sys.breakpointhook()" for sobrescrito
   programaticamente, "PYTHONBREAKPOINT" *não* será consultado.

   Adicionado na versão 3.7.

sys._debugmallocstats()

   Imprima informações de baixo nível para stderr sobre o estado do
   alocador de memória do CPython.

   Se o Python for compilado no modo de depuração ("opção --with-
   pydebug do configure"), ele também executa algumas verificações de
   consistência interna custosas.

   Adicionado na versão 3.3.

   Esta função é específica para CPython. O formato de saída exato não
   é definido aqui e pode mudar.

sys.dllhandle

   Número inteiro que especifica o identificador da DLL do Python.

   Disponibilidade: Windows.

sys.displayhook(value)

   Se *value* não for "None", esta função imprime "repr(value)" em
   "sys.stdout", e salva *value* em "builtins._". Se "repr(value)" não
   for codificável para "sys.stdout.encoding" com o tratador de erros
   "sys.stdout.errors" (que provavelmente é "'strict'"), codifica-o
   para "sys.stdout.encoding" com tratador de erros
   "'backslashreplace'".

   "sys.displayhook" é chamado no resultado da avaliação de uma
   *expressão* inserida em uma sessão interativa do Python. A exibição
   desses valores pode ser personalizada atribuindo outra função de um
   argumento a "sys.displayhook".

   Pseudocódigo:

      def displayhook(value):
          if value is None:
              return
          # Define '_' como None para evitar recursão
          builtins._ = None
          text = repr(value)
          try:
              sys.stdout.write(text)
          except UnicodeEncodeError:
              bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
              if hasattr(sys.stdout, 'buffer'):
                  sys.stdout.buffer.write(bytes)
              else:
                  text = bytes.decode(sys.stdout.encoding, 'strict')
                  sys.stdout.write(text)
          sys.stdout.write("\n")
          builtins._ = value

   Alterado na versão 3.2: Usa o tratador de erros
   "'backslashreplace'" ao ser levantada "UnicodeEncodeError".

sys.dont_write_bytecode

   Se isso for true, o Python não tentará escrever arquivos ".pyc" na
   importação de módulos fonte. Este valor é inicialmente definido
   como "True" ou "False" dependendo da opção de linha de comando "-B"
   e da variável de ambiente "PYTHONDONTWRITEBYTECODE", mas você mesmo
   pode configurá-lo para controlar geração de arquivo bytecode.

sys._emscripten_info

   Um *tupla nomeada* contendo informações sobre o ambiente na
   plataforma *wasm32-emscripten*. A tupla nomeada é provisória e pode
   mudar no futuro.

   _emscripten_info.emscripten_version

      Versão emscripten como tupla de ints (maior, menor, micro), por
      exemplo "(3, 1, 8)".

   _emscripten_info.runtime

      String em tempo de execução; por exemplo, user-agent do
      navegador, "'Node.js v14.18.2'", ou "'UNKNOWN'".

   _emscripten_info.pthreads

      "True" se o Python for compilado com suporte a pthreads do
      Emscripten.

   _emscripten_info.shared_memory

      "True" se o Python for compilado com suporte a memória
      compartilhada.

   Disponibilidade: Emscripten.

   Adicionado na versão 3.11.

sys.pycache_prefix

   Se for definido (não "None"), o Python escreverá arquivos de cache
   de bytecode ".pyc" para (e os lerá de) uma árvore de diretórios
   paralela com raiz neste diretório, em vez de diretórios
   "__pycache__" na árvore de código-fonte. Quaisquer diretórios
   "__pycache__" na árvore de código-fonte serão ignorados e novos
   arquivos ".pyc" gravados dentro do prefixo pycache. Portanto, se
   você usar "compileall" como uma etapa de pré-compilação,
   certifique-se de executá-lo com o mesmo prefixo pycache (se houver)
   que usará em tempo de execução.

   Um caminho relativo é interpretado em relação ao diretório de
   trabalho atual.

   Este valor é definido inicialmente com base no valor da opção de
   linha de comando "-X" "pycache_prefix=PATH" ou na variável de
   ambiente "PYTHONPYCACHEPREFIX" (a linha de comando tem
   precedência). Se nenhum estiver definido, é "None".

   Adicionado na versão 3.8.

sys.excepthook(type, value, traceback)

   Esta função imprime um determinado traceback (situação da pilha de
   execução) e exceção para "sys.stderr".

   Quando uma exceção além da "SystemExit" é levantada e não
   capturada, o interpretador chama "sys.excepthook" com três
   argumentos, a classe de exceção, a instância de exceção e um objeto
   traceback. Em uma sessão interativa, isso acontece logo antes de o
   controle retornar ao prompt; em um programa Python, isso acontece
   pouco antes de o programa ser encerrado. A manipulação de tais
   exceções de nível superior pode ser personalizada atribuindo outra
   função de três argumentos a "sys.excepthook".

   Levanta um evento de auditoria "sys.excepthook" com os argumentos
   "hook", "type", "value", "traceback" quando ocorre uma exceção não
   capturada. Se nenhum gancho foi definido, "hook" pode ser "None".
   Se algum gancho gerar uma exceção derivada de "RuntimeError", a
   chamada para o gancho será suprimida. Caso contrário, a exceção de
   gancho de auditoria será relatada como não aumentável e
   "sys.excepthook" será chamado.

   Ver também:

     A função "sys.unraisablehook()" lida com exceções que não podem
     ser levantadas e a função "threading.excepthook()" trata exceções
     levantadas por "threading.Thread.run()".

sys.__breakpointhook__
sys.__displayhook__
sys.__excepthook__
sys.__unraisablehook__

   Esses objetos contêm os valores originais de "breakpointhook",
   "displayhook", "excepthook" e "unraisablehook" no início do
   programa. Eles são salvos para que "breakpointhook", "displayhook"
   e "excepthook", "unraisablehook" possam ser restaurados caso sejam
   substituídos por objetos quebrados ou alternativos.

   Adicionado na versão 3.7: __breakpointhook__

   Adicionado na versão 3.8: __unraisablehook__

sys.exception()

   Esta função, quando chamada enquanto um tratador de exceção está em
   execução (como uma cláusula "except" ou "except*"), retorna a
   instância da exceção que foi capturada por este tratador. Quando os
   manipuladores de exceção estão aninhados um dentro do outro, apenas
   a exceção tratada pelo tratador mais interno é acessível.

   Se nenhum tratador de exceções estiver em execução, esta função
   retornará "None".

   Adicionado na versão 3.11.

sys.exc_info()

   Essa função retorna a representação de estilo antigo da exceção
   tratada. Se uma exceção "e" é tratada atualmente (de forma que
   "exception()" retornaria "e"), "exc_info()" retorna a tupla
   "(type(e), e, e.__traceback__)". Ou seja, uma tupla contendo o tipo
   da exceção (uma subclasse de "BaseException"), a própria exceção e
   um objeto de traceback que normalmente encapsula a pilha de
   chamadas no ponto em que a última exceção ocorreu.

   Se nenhuma exceção estiver sendo tratada em qualquer lugar da
   pilha, esta função retornará uma tupla contendo três valores
   "None".

   Alterado na versão 3.11: Os campos "type" e "traceback" agora são
   derivados do "value" (a instância da exceção), portanto, quando uma
   exceção é modificada enquanto está sendo tratada, as alterações são
   refletidas nos resultados das subsequentes chamadas para
   "exc_info()".

sys.exec_prefix

   Uma string que fornece o prefixo do diretório específico do site
   onde os arquivos Python dependentes da plataforma são instalados;
   por padrão, também é "'/usr/local'". Isso pode ser definido em
   tempo de compilação com o argumento "--exec-prefix" para o script
   **configure**. Especificamente, todos os arquivos de configuração
   (por exemplo, o arquivo de cabeçalho "pyconfig.h") são instalados
   no diretório "*exec_prefix*/lib/python*X.Y*/config", e os módulos
   da biblioteca compartilhada são instalados em
   "*exec_prefix*/lib/python*X.Y*/lib-dynload", onde *X.Y* é o número
   da versão do Python, por exemplo "3.2".

   Nota:

     Se um ambiente virtual estiver em vigor, este "exec_prefix" vai
     apontar para o ambiente virtual. O valor para a instalação do
     Python ainda estará disponível, via "base_exec_prefix". Confira
     Ambientes virtuais para mais informações.

   Alterado na versão 3.14: Ao executar em um ambiente virtual,
   "prefix" e "exec_prefix" agora são definidos como o prefixo do
   ambiente virtual pela inicialização do caminho, em vez de "site".
   Isso significa que "prefix" e "exec_prefix" sempre apontam para o
   ambiente virtual, mesmo quando "site" está desabilitado ("-S").

sys.executable

   Uma string que fornece o caminho absoluto do binário executável
   para o interpretador Python, em sistemas onde isso faz sentido. Se
   o Python não conseguir recuperar o caminho real para seu
   executável, "sys.executable" será uma string vazia ou "None".

sys.exit([arg])

   Levanta uma exceção "SystemExit", sinalizando a intenção de sair do
   interpretador.

   The optional argument *arg* can be an integer giving the exit
   status (defaulting to zero), or another type of object.  If it is
   an integer, zero is considered "successful termination" and any
   nonzero value is considered "abnormal termination" by shells and
   the like.  Most systems require it to be in the range 0--127, and
   produce undefined results otherwise.  Some systems have a
   convention for assigning specific meanings to specific exit codes,
   but these are generally underdeveloped; Unix programs generally use
   2 for command line syntax errors and 1 for all other kinds of
   errors.  If another type of object is passed, "None" is equivalent
   to passing zero, and any other object is printed to "stderr" and
   results in an exit code of 1.  In particular, "sys.exit("some error
   message")" is a quick way to exit a program when an error occurs.

   Since "exit()" ultimately "only" raises an exception, it will only
   exit the process when called from the main thread, and the
   exception is not intercepted. Cleanup actions specified by
   "finally" clauses of "try" statements are honored, and it is
   possible to intercept the exit attempt at an outer level.

   Alterado na versão 3.6: Se ocorrer um erro na limpeza após o
   interpretador Python ter capturado "SystemExit" (como um erro ao
   liberar dados em buffer nos fluxos padrão), o status de saída é
   alterado para 120.

sys.flags

   A *tupla nomeada* *flags* expõe o status dos sinalizadores de linha
   de comando. Os sinalizadores devem ser acessados somente pelo nome
   e não pelo índice. Os atributos são somente leitura.

   +----------------------------------------------------+----------------------------------------------------+
   | flags.debug                                        | "-d"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.inspect                                      | "-i"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.interactive                                  | "-i"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.isolated                                     | "-I"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.optimize                                     | "-O" ou "-OO"                                      |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.dont_write_bytecode                          | "-B"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.no_user_site                                 | "-s"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.no_site                                      | "-S"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.ignore_environment                           | "-E"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.verbose                                      | "-v"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.bytes_warning                                | "-b"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.quiet                                        | "-q"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.hash_randomization                           | "-R"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.dev_mode                                     | "-X dev" (Modo de Desenvolvimento do Python)       |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.utf8_mode                                    | "-X utf8"                                          |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.safe_path                                    | "-P"                                               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.int_max_str_digits                           | "-X int_max_str_digits" (limitação de comprimento  |
   |                                                    | de string na conversão para inteiro)               |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.warn_default_encoding                        | "-X warn_default_encoding"                         |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.gil                                          | "-X gil" e "PYTHON_GIL"                            |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.thread_inherit_context                       | "-X thread_inherit_context" e                      |
   |                                                    | "PYTHON_THREAD_INHERIT_CONTEXT"                    |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.context_aware_warnings                       | "-X context_aware_warnings" e                      |
   |                                                    | "PYTHON_CONTEXT_AWARE_WARNINGS"                    |
   +----------------------------------------------------+----------------------------------------------------+
   | flags.lazy_imports                                 | "-X lazy_imports" and "PYTHON_LAZY_IMPORTS" ("1"   |
   |                                                    | for "all", "-1" otherwise; not changed by          |
   |                                                    | "set_lazy_imports()")                              |
   +----------------------------------------------------+----------------------------------------------------+

   Alterado na versão 3.2: Adicionado o atributo "quiet" para o novo
   sinalizador "-q".

   Adicionado na versão 3.2.3: O atributo "hash_randomization".

   Alterado na versão 3.3: Removido o atributo obsoleto
   "division_warning".

   Alterado na versão 3.4: Adicionado o atributo "isolated" para o
   sinalizador "-I" "isolated".

   Alterado na versão 3.7: Adicionado o atributo "dev_mode" para o
   novo Modo de Desenvolvimento do Python e o atributo "utf8_mode"
   para o novo sinalizador "-X" "utf8".

   Alterado na versão 3.10: Adicionado o atributo
   "warn_default_encoding" para o sinalizador "-X"
   "warn_default_encoding".

   Alterado na versão 3.11: Adicionado o atributo "safe_path" para a
   opção "-P".

   Alterado na versão 3.11: Adicionado o atributo
   "int_max_str_digits".

   Alterado na versão 3.13: Adicionado o atributo "gil".

   Alterado na versão 3.14: Adicionado o atributo
   "thread_inherit_context".

   Alterado na versão 3.14: Adicionado o atributo
   "context_aware_warnings".

   Alterado na versão 3.15: Added the "lazy_imports" attribute.

sys.float_info

   Uma *tupla nomeada* contendo informações sobre o tipo float, ponto
   flutuante. Ele contém informações de baixo nível sobre a precisão e
   a representação interna. Os valores correspondem às várias
   constantes de ponto flutuante definidas no arquivo de cabeçalho
   padrão "float.h" para a linguagem de programação 'C'; consulte a
   seção 5.2.4.2.2 do padrão ISO/IEC C de 1999 [C99], 'Características
   dos tipos flutuantes', para obter detalhes.


   Atributos da *tupla nomeada* "float_info"
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   +-----------------------------------+-----------------------------------+-----------------------------------+
   | atributo                          | macro em float.h                  | explicação                        |
   |===================================|===================================|===================================|
   | float_info.epsilon                | "DBL_EPSILON"                     | diferença entre 1,0 e o menor     |
   |                                   |                                   | valor maior que 1,0 que pode ser  |
   |                                   |                                   | representado como ponto           |
   |                                   |                                   | flutuante.  Veja também           |
   |                                   |                                   | "math.ulp()".                     |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.dig                    | "DBL_DIG"                         | O número máximo de dígitos        |
   |                                   |                                   | decimais que podem ser fielmente  |
   |                                   |                                   | representados em um ponto         |
   |                                   |                                   | flutuante; veja abaixo.           |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.mant_dig               | "DBL_MANT_DIG"                    | Precisão do ponto flutuante: o    |
   |                                   |                                   | número de dígitos de base "radix" |
   |                                   |                                   | no significando de um ponto       |
   |                                   |                                   | flutuante.                        |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.max                    | "DBL_MAX"                         | O ponto flutuante finito positivo |
   |                                   |                                   | máximo representável.             |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.max_exp                | "DBL_MAX_EXP"                     | O inteiro máximo *e* de tal modo  |
   |                                   |                                   | que "radix**(e-1)" é um ponto     |
   |                                   |                                   | flutuante finito representável.   |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.max_10_exp             | "DBL_MAX_10_EXP"                  | O inteiro máximo *e* de tal modo  |
   |                                   |                                   | que "10**e" é um intervalo de     |
   |                                   |                                   | pontos flutuantes finitos         |
   |                                   |                                   | representáveis.                   |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.min                    | "DBL_MIN"                         | O ponto flutuante *normalizado*   |
   |                                   |                                   | positivo mínimo representável.    |
   |                                   |                                   | Use "math.ulp(0.0)" para obter o  |
   |                                   |                                   | menor ponto flutuante             |
   |                                   |                                   | representável positivo            |
   |                                   |                                   | *desnormalizado*.                 |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.min_exp                | "DBL_MIN_EXP"                     | O inteiro mínimo *e* de tal modo  |
   |                                   |                                   | que "radix**(e-1)" é um ponto     |
   |                                   |                                   | flutuante normalizado.            |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.min_10_exp             | "DBL_MIN_10_EXP"                  | O inteiro mínimo *e* de tal modo  |
   |                                   |                                   | que "10**e" é um ponto flutuante  |
   |                                   |                                   | normalizado.                      |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.radix                  | "FLT_RADIX"                       | A raiz da representação do        |
   |                                   |                                   | expoente.                         |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | float_info.rounds                 | "FLT_ROUNDS"                      | Um inteiro representando o modo   |
   |                                   |                                   | de arredondamento para aritmética |
   |                                   |                                   | de ponto flutuante. Isso reflete  |
   |                                   |                                   | o valor da macro do sistema       |
   |                                   |                                   | "FLT_ROUNDS" no momento da        |
   |                                   |                                   | inicialização do interpretador:   |
   |                                   |                                   | * "-1": indeterminável  * "0": em |
   |                                   |                                   | direção a zero  * "1": para o     |
   |                                   |                                   | mais próximo  * "2": em direção   |
   |                                   |                                   | ao infinito positivo  * "3": em   |
   |                                   |                                   | direção ao infinito negativo      |
   |                                   |                                   | Todos os outros valores para      |
   |                                   |                                   | "FLT_ROUNDS" caracterizam o       |
   |                                   |                                   | comportamento de arredondamento   |
   |                                   |                                   | definido pela implementação.      |
   +-----------------------------------+-----------------------------------+-----------------------------------+

   O atributo "sys.float_info.dig" precisa de mais explicações. Se "s"
   for qualquer string representando um número decimal com no máximo
   "sys.float_info.dig" dígitos significativos, então converter "s"
   para ponto flutuante e vice-versa recuperará uma string
   representando o mesmo decimal valor:

      >>> import sys
      >>> sys.float_info.dig
      15
      >>> s = '3.14159265358979'    # string decimal com 15 dígitos significativos
      >>> format(float(s), '.15g')  # converter para float e desconverter retorna mesmo valor
      '3.14159265358979'

   Mas para strings com mais de "sys.float_info.dig" dígitos
   significativos, isso nem sempre é verdade:

      >>> s = '9876543211234567'    # 16 dígitos significativos é muito!
      >>> format(float(s), '.16g')  # a conversão muda o valor
      '9876543211234568'

sys.float_repr_style

   Uma string indicando como a função "repr()" se comporta para
   floats. Se a string tem valor "'short'" então para um ponto
   flutuante finito "x", "repr(x)" visa produzir uma string curta com
   a propriedade que "float(repr(x)) == x". Este é o comportamento
   usual no Python 3.1 e posterior. Caso contrário, "float_repr_style"
   tem valor "'legacy'" e "repr(x)" se comporta da mesma forma que nas
   versões do Python anteriores a 3.1.

   Adicionado na versão 3.1.

sys.getallocatedblocks()

   Retorna a quantidade de blocos de memória alocados atualmente pelo
   interpretador, independentemente do tamanho. Esta função é útil
   principalmente ao acompanhar e depurar vazamentos de memória.
   Devido aos caches internos do interpretador, o resultado pode
   variar de chamada a chamada; você pode ter que chamar
   "_clear_internal_caches()" e "gc.collect()" para obter resultados
   mais previsíveis.

   Se uma construção ou implementação do Python não puder computar
   razoavelmente essas informações, "getallocatedblocks()" poderá
   retornar 0 em seu lugar.

   Adicionado na versão 3.4.

sys.getunicodeinternedsize()

   Retorna o número de objetos unicode que foram internalizados.

   Adicionado na versão 3.12.

sys.getandroidapilevel()

   Retorna o nível de API de tempo de construção do Android como um
   inteiro. Isso representa a versão mínima do Android em que esta
   construção do Python pode ser executada. Para obter informações
   sobre a versão de tempo de execução, consulte
   "platform.android_ver()".

   Disponibilidade: Android.

   Adicionado na versão 3.7.

sys.getdefaultencoding()

   Retorna "'utf-8'". Este é o nome da codificação de string padrão,
   usada em métodos como "str.encode()".

sys.getdlopenflags()

   Retorna o valor atual dos sinalizadores que são usados para
   chamadas "dlopen()". Nomes simbólicos para os valores dos
   sinalizadores podem ser encontrados no módulo "os" (constantes
   "RTLD_*xxx*", por exemplo "os.RTLD_LAZY").

   Disponibilidade: Unix.

sys.getfilesystemencoding()

   Obtém o *codificação do sistema de arquivos*: a codificação usada
   com o *manipulador de erros do sistema de arquivos* para converter
   entre nomes de arquivos Unicode e nomes de arquivos de bytes. O
   manipulador de erros do sistema de arquivos é retornado de
   "getfilesystemencodeerrors()".

   Para melhor compatibilidade, str deve ser usado para nomes de
   arquivos em todos os casos, embora a representação de nomes de
   arquivos como bytes também seja suportada. As funções que aceitam
   ou retornam nomes de arquivo devem suportar str ou bytes e
   converter internamente para a representação preferencial do
   sistema.

   "os.fsencode()" e "os.fsdecode()" devem ser usados para garantir
   que a codificação correta e o modo de erros sejam usados.

   O *tratador de erros e codificação do sistema de arquivos* são
   configurados na inicialização do Python pela função
   "PyConfig_Read()": veja os membros "filesystem_encoding" e
   "filesystem_errors" do "PyConfig".

   Alterado na versão 3.2: O resultado de "getfilesystemencoding()"
   não pode mais ser "None".

   Alterado na versão 3.6: O Windows não tem mais garantia de retornar
   "'mbcs'". Veja **PEP 529** e "_enablelegacywindowsfsencoding()"
   para mais informações.

   Alterado na versão 3.7: Retorna "'utf-8'" se o Modo UTF-8 do Python
   estiver ativado.

sys.getfilesystemencodeerrors()

   Obtém o *manipulador de erros do sistema de arquivos*: o
   manipulador de erros usado com a *codificação do sistema de
   arquivos* para converter entre nomes de arquivos Unicode e nomes de
   arquivos de bytes. A codificação do sistema de arquivos é retornado
   de "getfilesystemencoding()".

   "os.fsencode()" e "os.fsdecode()" devem ser usados para garantir
   que a codificação correta e o modo de erros sejam usados.

   O *tratador de erros e codificação do sistema de arquivos* são
   configurados na inicialização do Python pela função
   "PyConfig_Read()": veja os membros "filesystem_encoding" e
   "filesystem_errors" do "PyConfig".

   Adicionado na versão 3.6.

sys.get_int_max_str_digits()

   Retorna o valor atual para a limitação de comprimento de string na
   conversão para inteiro. Veja também "set_int_max_str_digits()".

   Adicionado na versão 3.11.

sys.get_lazy_imports()

   Returns the current lazy imports mode as a string.

   * ""normal"": Only imports explicitly marked with the "lazy"
     keyword are lazy

   * ""all"": All top-level imports are potentially lazy

   See also "set_lazy_imports()" and **PEP 810**.

   Adicionado na versão 3.15.

sys.get_lazy_imports_filter()

   Returns the current lazy imports filter function, or "None" if no
   filter is set.

   The filter function is called for every potentially lazy import to
   determine whether it should actually be lazy. See
   "set_lazy_imports_filter()" for details on the filter function
   signature.

   Adicionado na versão 3.15.

sys.getrefcount(object)

   Retorna a contagem de referências do *object*. A contagem retornada
   é geralmente um valor maior do que o esperado, porque inclui a
   referência (temporária) passada como argumento para
   "getrefcount()".

   Observe que o valor retornado pode não refletir realmente quantas
   referências ao objeto são realmente mantidas. Por exemplo, alguns
   objetos são *imortais* e têm uma contagem de referências muito
   alta, que não reflete o número real de referências.
   Consequentemente, não confie no valor retornado para ser preciso,
   exceto um valor de 0 ou 1.

   Objetos *imortais* com uma grande contagem de referências podem ser
   identificados via "_is_immortal()".

   Alterado na versão 3.12: Objetos imortais têm contagens de
   referência muito grandes que não correspondem ao número real de
   referências ao objeto.

sys.getrecursionlimit()

   Retorna o valor atual do limite de recursão, a profundidade máxima
   da pilha do interpretador Python. Esse limite evita que a recursão
   infinita cause um estouro da pilha C e falhe o Python. Pode ser
   definido por "setrecursionlimit()".

sys.getsizeof(object[, default])

   Retorna o tamanho de um objeto em bytes. O objeto pode ser qualquer
   tipo de objeto. Todos os objetos embutidos retornarão resultados
   corretos, mas isso não precisa ser verdadeiro para extensões de
   terceiros, pois é específico da implementação.

   Apenas o consumo de memória diretamente atribuído ao objeto é
   contabilizado, não o consumo de memória dos objetos a que ele se
   refere.

   Se fornecido, *default* será retornado se o objeto não fornecer
   meios para recuperar o tamanho. Caso contrário, uma exceção
   "TypeError" será levantada.

   "getsizeof()" chama o método "__sizeof__" do objeto e adiciona uma
   sobrecarga adicional do coletor de lixo se o objeto for gerenciado
   pelo coletor de lixo.

   Consulte receita de tamanho recursivo para obter um exemplo de uso
   de "getsizeof()" recursivamente para encontrar o tamanho dos
   contêineres e todo o seu conteúdo.

sys.getswitchinterval()

   Retorna o "intervalo de troca de thread" do interpretador em
   segundos; veja "setswitchinterval()".

   Adicionado na versão 3.2.

sys._getframe([depth])

   Retorna um objeto quadro da pilha de chamadas. Se o inteiro
   opcional *depth* for fornecido, retorna o objeto de quadro que
   muitos chamam abaixo do topo da pilha. Se for mais profundo do que
   a pilha de chamadas, "ValueError" é levantada. O padrão para
   *depth* é zero, retornando o quadro no topo da pilha de chamadas.

   Levanta um evento de auditoria "sys._getframe" com o argumento
   "frame".

   Esta função deve ser usada apenas para fins internos e
   especializados. Não é garantido que exista em todas as
   implementações do Python.

sys._getframemodulename([depth])

   Retorna o nome de um módulo da pilha de chamadas. Se o inteiro
   opcional *depth* for fornecido, retorna o módulo que muitas
   chamadas abaixo do topo da pilha. Se for mais profundo do que a
   pilha de chamadas, ou se o módulo não for identificável, "None" é
   retornado. O padrão para *depth* é zero, retornando o módulo no
   topo da pilha de chamadas.

   Levanta um evento de auditoria "sys._getframemodulename" com o
   argumento "depth".

   Esta função deve ser usada apenas para fins internos e
   especializados. Não é garantido que exista em todas as
   implementações do Python.

   Adicionado na versão 3.12.

sys.getobjects(limit[, type])

   Esta função só existe se o CPython foi construído usando a opção de
   configuração especializada "--with-trace-refs". Ela é destinada
   apenas para depurar problemas de coleta de lixo.

   Retorna uma lista de até *limit* objetos Python alocados
   dinamicamente. Se *type* for fornecido, somente objetos daquele
   tipo exato (não subtipos) serão incluídos.

   Objetos da lista não são seguros para uso. Especificamente, o
   resultado incluirá objetos de todos os interpretadores que
   compartilham seu estado de alocador de objetos (ou seja, aqueles
   criados com "PyInterpreterConfig.use_main_obmalloc" definido como 1
   ou usando "Py_NewInterpreter()" e o interpretador principal).
   Misturar objetos de diferentes iinterpretadores pode levar a
   travamentos ou outros comportamentos inesperados.

   Esta função deve ser usada apenas para fins especializados. Não é
   garantido que exista em todas as implementações do Python.

   Alterado na versão 3.14: O resultado pode incluir objetos de outros
   interpretadores.

sys.getprofile()

   Obtém a função do criador de perfil conforme definido por
   "setprofile()".

sys.gettrace()

   Obtém a função trace conforme definido por "settrace()".

   A função "gettrace()" destina-se apenas à implementação de
   depuradores, perfiladores, ferramentas de cobertura e similares.
   Seu comportamento faz parte da plataforma de implementação, e não
   da definição da linguagem e, portanto, pode não estar disponível em
   todas as implementações do Python.

sys.getwindowsversion()

   Retorna uma tupla nomeada que descreve a versão do Windows em
   execução no momento. Os elementos nomeados são *major*, *minor*,
   *build*, *platform*, *service_pack*, *service_pack_minor*,
   *service_pack_major*, *suite_mask*, *product_type* e
   *platform_version*. *service_pack* contém uma string,
   *platform_version* uma tupla de 3 elementos e todos os outros
   valores são inteiros. Os componentes também podem ser acessados
   pelo nome, então "sys.getwindowsversion()[0]" é equivalente a
   "sys.getwindowsversion().major". Para compatibilidade com versões
   anteriores, apenas os primeiros 5 elementos são recuperáveis por
   indexação.

   *platform* será "2" (VER_PLATFORM_WIN32_NT).

   *product_type* pode ser um dos seguintes valores:

   +-----------------------------------------+-----------------------------------+
   | Constante                               | Significado                       |
   |=========================================|===================================|
   | "1" (VER_NT_WORKSTATION)                | O sistema é uma estação de        |
   |                                         | trabalho                          |
   +-----------------------------------------+-----------------------------------+
   | "2" (VER_NT_DOMAIN_CONTROLLER)          | O sistema é um controlador de     |
   |                                         | domínio.                          |
   +-----------------------------------------+-----------------------------------+
   | "3" (VER_NT_SERVER)                     | O sistema é um servidor, mas não  |
   |                                         | um controlador de domínio.        |
   +-----------------------------------------+-----------------------------------+

   Esta função atua como um envólucro em volta da função Win32
   "GetVersionEx()"; consulte a documentação da Microsoft em
   "OSVERSIONINFOEX()" para obter mais informações sobre esses campos.

   *platform_version* retorna a versão principal, a versão secundária
   e o número de compilação do sistema operacional atual, em vez da
   versão que está sendo emulada para o processo. Destina-se a ser
   usado no registro, e não na detecção de recursos.

   Nota:

     *platform_version* deriva a versão de kernel32.dll que pode ser
     de uma versão diferente da versão do sistema operacional. Use o
     módulo "platform" para obter a versão precisa do sistema
     operacional.

   Disponibilidade: Windows.

   Alterado na versão 3.2: Alterado para uma tupla nomeada e
   adicionado *service_pack_minor*, *service_pack_major*, *suite_mask*
   e *product_type*.

   Alterado na versão 3.6: Adicionado *platform_version*

sys.get_asyncgen_hooks()

   Retorna um objeto *asyncgen_hooks*, que é semelhante a um
   "namedtuple" no formato "(firstiter, finalizer)", onde *firstiter*
   e *finalizer* devem ser "None" ou funções que recebem um *iterador
   gerador assíncrono* como argumento e são usadas para agendar a
   finalização de um gerador assíncrono por um laço de eventos.

   Adicionado na versão 3.6: Veja **PEP 525** para mais detalhes.

   Nota:

     Esta função foi adicionada provisoriamente (veja **PEP 411** para
     detalhes.)

sys.get_coroutine_origin_tracking_depth()

   Obtém a profundidade de rastreamento da origem da corrotina atual,
   conforme definido por "set_coroutine_origin_tracking_depth()".

   Adicionado na versão 3.7.

   Nota:

     Esta função foi adicionada provisoriamente (veja **PEP 411** para
     detalhes.) Use-a apenas para propósitos de depuração.

sys.hash_info

   Uma *tupla nomeada* fornecendo parâmetros da implementação de hash
   numérico. Para mais detalhes sobre hashing de tipos numéricos, veja
   Hashing de tipos numéricos.

   hash_info.width

      A largura em bits usada para fazer hash de valores

   hash_info.modulus

      O módulo primo P usado para esquema de hash numérico

   hash_info.inf

      O valor de hash retornado para um infinito positivo

   hash_info.nan

      (Este atributo não é mais usado)

   hash_info.imag

      O multiplicador usado para a parte imaginária de um número
      complexo

   hash_info.algorithm

      O nome do algoritmo para hash de str, bytes e memoryview

   hash_info.hash_bits

      O tamanho da saída interna do algoritmo de hash

   hash_info.seed_bits

      O tamanho da chave semente do algoritmo hash

   hash_info.cutoff

      Limite para otimização de strings pequenas DJBX33A no intervalo
      "[1, cutoff)".

   Adicionado na versão 3.2.

   Alterado na versão 3.4: Adicionados *algorithm*, *hash_bits*,
   *seed_bits* e *cutoff*.

sys.hexversion

   O número da versão codificado como um único inteiro. Isso é
   garantido para aumentar com cada versão, incluindo suporte adequado
   para lançamentos de não produção. Por exemplo, para testar se o
   interpretador Python é pelo menos a versão 1.5.2, use:

      if sys.hexversion >= 0x010502F0:
          # usa algum recurso avançado
          ...
      else:
          # usa uma implementação alternativa ou adverte o usuário
          ...

   Isso é chamado "hexversion" já que só parece realmente
   significativo quando visto como o resultado de passá-lo para a
   função embutida "hex()". A *tupla nomeada* "sys.version_info" pode
   ser usada para uma codificação mais amigável das mesmas
   informações.

   Mais detalhes sobre "hexversion" podem ser encontrados em API e
   Versionamento de ABI.

sys.implementation

   Um objeto que contém informações sobre a implementação do
   interpretador Python em execução no momento. Os atributos a seguir
   devem existir em todas as implementações do Python.

   *name* é o identificador da implementação, por exemplo "'cpython'".
   A string real é definida pela implementação do Python, mas é
   garantido que seja minúscula.

   *version* é uma tupla nomeada, no mesmo formato que
   "sys.version_info". Ela representa a versão da implementação Python
   em *implementation*. Isso tem um significado distinto da versão
   específica da *linguagem* Python à qual o interpretador em execução
   no momento está em conformidade, que "sys.version_info" representa.
   Por exemplo, para PyPy 1.8 "sys.implementation.version" pode ser
   "sys.version_info(1, 8, 0, 'final', 0)", enquanto
   "sys.version_info" seria "sys.version_info(2, 7, 2, 'final', 0)".
   Para CPython, eles são o mesmo valor, pois é a implementação de
   referência.

   *hexversion* é a versão de implementação em formato hexadecimal,
   como "sys.hexversion".

   *cache_tag* é a tag usada pelo mecanismo de importação nos nomes de
   arquivo dos módulos em cache. Por convenção, seria um composto do
   nome e da versão da implementação, como "'cpython-33'". No entanto,
   uma implementação Python pode usar algum outro valor, se
   apropriado. Se "cache_tag" for definido como "None", isso indica
   que o cache do módulo deve ser desabilitado.

   *supports_isolated_interpreters* é um valor booleano que indica se
   esta implementação oferece suporte a múltiplos interpretadores
   isolados. É "True" para CPython na maioria das plataformas.
   Plataformas com este suporte implementam o módulo de baixo nível
   "_interpreters".

   Ver também: **PEP 684**, **PEP 734** e "concurrent.interpreters".

   "sys.implementation" pode conter atributos adicionais específicos
   para a implementação do Python. Esses atributos não padrão devem
   começar com um sublinhado e não são descritos aqui.
   Independentemente do seu conteúdo, "sys.implementation" não mudará
   durante uma execução do interpretador, nem entre versões de
   implementação. (No entanto, ele pode mudar entre versões da
   linguagem Python.) Veja a **PEP 421** para mais informações.

   Adicionado na versão 3.3.

   Alterado na versão 3.14: Adicionado o campo
   "supports_isolated_interpreters".

   Nota:

     A adição de novos atributos obrigatórios deve passar pelo
     processo normal de PEPs. Veja a **PEP 421** para mais
     informações.

sys.int_info

   Uma *tupla nomeada* que contém informações sobre a representação
   interna de inteiros do Python. Os atributos são somente leitura.

   int_info.bits_per_digit

      O número de bits mantidos em cada dígito. Os inteiros do Python
      são armazenados internamente na base
      "2**int_info.bits_per_digit".

   int_info.sizeof_digit

      O tamanho em bytes do tipo C usado para representar um dígito.

   int_info.default_max_str_digits

      O valor padrão para "sys.get_int_max_str_digits()" quando não
      estiver explicitamente configurado.

   int_info.str_digits_check_threshold

      O valor mínimo diferente de zero para
      "sys.set_int_max_str_digits()", "PYTHONINTMAXSTRDIGITS" ou "-X
      int_max_str_digits".

   Adicionado na versão 3.1.

   Alterado na versão 3.11: Adicionados "default_max_str_digits" e
   "str_digits_check_threshold".

sys.__interactivehook__

   Quando esse atributo existe, seu valor é chamado automaticamente
   (sem argumentos) quando o interpretador é iniciado em modo
   interativo. Isso é feito após o arquivo "PYTHONSTARTUP" ser lido,
   para que você possa definir esse gancho lá. O módulo "site" define
   isso.

   Levanta um evento de auditoria "cpython.run_interactivehook" com o
   objeto gancho como o argumento quando o gancho é chamado na
   inicialização.

   Adicionado na versão 3.4.

sys.intern(string)

   Insere *string* na tabela de strings "internalizadas" e retorna a
   string internalizada -- que é a própria *string* ou uma cópia.
   Strings internalizadas são úteis para obter um pouco de desempenho
   na pesquisa de dicionário -- se as chaves em um dicionário foram
   internalizadas, e a chave de pesquisa para internalizada, já que
   comparações de chaves (após o hash) podem ser feitas por uma
   comparação de ponteiros em vez de uma comparação de strings.
   Normalmente, os nomes usados em programas Python são internalizados
   automaticamente, e os dicionários usados para armazenar atributos
   de módulo, classe ou instância têm chaves internalizadas.

   Strings internalizadas não são *imortais*; você deve manter uma
   referência ao valor de retorno de "intern()" para se beneficiar
   dela.

sys._is_gil_enabled()

   Retorna "True" se a *GIL* estiver habiltada e "False" caso
   contrário.

   Adicionado na versão 3.13.

   Não há garantia de que exista em todas as implementações do Python.

sys.is_finalizing()

   Retorna "True" se o interpretador Python principal estiver
   *desligando*. Retorna "False" caso contrário.

   Veja também a exceção "PythonFinalizationError".

   Adicionado na versão 3.5.

sys._jit

   Utilitários para observar compilação just-in-time.

   A compilação JIT é um *detalhe de implementação experimental* do
   CPython. Não há garantia de que "sys._jit" exista ou se comporte da
   mesma maneira em todas as implementações, versões ou configurações
   de construção do Python.

   Adicionado na versão 3.14.

   _jit.is_available()

      Retorna "True" se o executável Python atual oferecer suporte à
      compilação JIT e "False" caso contrário. Isso pode ser
      controlado compilando o CPython com a opção "--experimental-jit"
      no Windows e a opção "--enable-experimental-jit" em todas as
      outras plataformas.

   _jit.is_enabled()

      Retorna "True" se a compilação JIT estiver habilitada para o
      processo Python atual (implica "sys._jit.is_available()"), e
      "False" caso contrário. Se a compilação JIT estiver disponível,
      isso pode ser controlado definindo a variável de ambiente
      "PYTHON_JIT" como "0" (desabilitada) ou "1" (habilitada) na
      inicialização do interpretador.

   _jit.is_active()

      Retorna "True" se o quadro Python mais alto estiver executando
      código JIT (implica "sys._jit.is_enabled()"), e "False" caso
      contrário.

      Nota:

        Esta função destina-se a testar e depurar o próprio JIT. Deve
        ser evitada para qualquer outro propósito.

      Nota:

        Devido à natureza do rastreamento de compiladores JIT,
        chamadas repetidas a esta função podem gerar resultados
        surpreendentes. Por exemplo, ramificar seu valor de retorno
        provavelmente levará a um comportamento inesperado (se isso
        fizer com que o código JIT seja inserido ou encerrado):

           >>> for warmup in range(BIG_NUMBER):
           ...     # Esta linha está "quente" e, eventualmente, é compilada JIT:
           ...     if sys._jit.is_active():
           ...         # Esta linha está "fria" e é executada no interpretador:
           ...         assert sys._jit.is_active()
           ...
           Traceback (most recent call last):
             File "<stdin>", line 5, in <module>
               assert sys._jit.is_active()
                      ~~~~~~~~~~~~~~~~~~^^
           AssertionError

sys.last_exc

   Esta variável nem sempre está definida; ela é definida para a
   instância de exceção quando uma exceção não é tratada e o
   interpretador imprime uma mensagem de erro e um stack traceback.
   Seu uso pretendido é permitir que um usuário interativo importe um
   módulo depurador e se envolva na depuração post-mortem sem ter que
   reexecutar o comando que causou o erro. (O uso típico é "import
   pdb; pdb.pm()" para entrar no depurador post-mortem; veja o módulo
   "pdb" para mais informações.)

   Adicionado na versão 3.12.

sys._is_immortal(op)

   Retorna "True" se o objeto fornecido for *imortal*, "False" caso
   contrário.

   Nota:

     Objetos que são imortais (e, portanto, retornam "True" ao serem
     passados para esta função) não têm garantia de serem imortais em
     versões futuras, e vice-versa para objetos mortais.

   Adicionado na versão 3.14.

   Esta função deve ser usada apenas para fins especializados. Não é
   garantido que exista em todas as implementações do Python.

sys._is_interned(string)

   Retorna "True" se a string fornecida for "internalizada", "False"
   caso contrário.

   Adicionado na versão 3.13.

   Não há garantia de que exista em todas as implementações do Python.

sys.last_type
sys.last_value
sys.last_traceback

   Essas três variáveis estão descontinuadas; use "sys.last_exc" em
   vez disso. Elas mantêm a representação legada de "sys.last_exc",
   conforme retornada de "exc_info()" acima.

sys.lazy_modules

   A "set" of fully qualified module name strings that have been
   lazily imported in the current interpreter but not yet loaded. When
   a lazily imported module is accessed for the first time, its name
   is typically removed from this set.

   The set may contain some additional strings. It is intended for
   debugging and introspection, and consumers are expected to verify
   each entry's status.

   **Detalhes da implementação do CPython:** Currently, "lazy_modules"
   may also contain:

   * names of *attributes* (non-modules), such as ""pathlib.Path""
     after running "lazy from pathlib import Path", and

   * names of items than have already been accessed.

   In future versions of Python, these may be removed, and/or
   additional extras may be added.

   See also "set_lazy_imports()" and **PEP 810**.

   Adicionado na versão 3.15.

sys.maxsize

   Um inteiro que fornece o valor máximo que uma variável do tipo
   "Py_ssize_t" pode assumir. Geralmente é "2**31 - 1" em uma
   plataforma de 32 bits e "2**63 - 1" em uma plataforma de 64 bits.

sys.maxunicode

   Um inteiro que fornece o valor do maior ponto de código Unicode, ou
   seja, "1114111" ("0x10FFFF" em hexadecimal).

   Alterado na versão 3.3: Antes da **PEP 393**, "sys.maxunicode"
   costumava ser "0xFFFF" ou "0x10FFFF", dependendo da opção de
   configuração que especificava se os caracteres Unicode eram
   armazenados como UCS-2 ou UCS-4.

sys.meta_path

   Uma lista de objetos *localizadores de metacaminho* que têm seus
   métodos "find_spec()" chamados para que algum deles localize o
   módulo a ser importado. Por padrão, armazena entradas que
   implementam a semântica de importação padrão de Python. O método
   "find_spec()" é chamado com pelo menos o nome absoluto do módulo a
   ser importado. Se o módulo a ser importado estiver contido num
   pacote, o atributo "__path__" do pacote pai é passado como segundo
   argumento. O método retorna um *spec de módulo*, ou "None" se o
   módulo não for encontrado.

   Ver também:

     "importlib.abc.MetaPathFinder"
        A classe base abstrata que define a interface dos objetos
        localizadores em "meta_path".

     "importlib.machinery.ModuleSpec"
        A classe concreta da qual "find_spec()" deve retornar
        instâncias.

   Alterado na versão 3.4: *Especificações de módulo* foram
   introduzidas no Python 3.4, pela **PEP 451**.

   Alterado na versão 3.12: Foi removido o alternativa que procurava
   um método "find_module()" se uma entrada "meta_path" não tivesse um
   método "find_spec()".

sys.modules

   Este é um dicionário que mapeia nomes de módulos para módulos que
   já foram carregados. Isso pode ser manipulado para forçar o
   recarregamento de módulos e outros truques. No entanto, substituir
   o dicionário não vai funcionar necessariamente como esperado e
   excluir itens essenciais do dicionário pode fazer com que o Python
   falhe. Se você quiser iterar sobre este dicionário global, sempre
   use "sys.modules.copy()" ou "tuple(sys.modules)" para evitar
   exceções, pois seu tamanho pode mudar durante a iteração como um
   efeito colateral do código ou atividade em outros threads.

sys.orig_argv

   A lista dos argumentos originais da linha de comando passados para
   o executável Python.

   Os elementos de "sys.orig_argv" são os argumentos para o
   interpretador Python, enquanto os elementos de "sys.argv" são os
   argumentos para o programa do usuário. Os argumentos consumidos
   pelo próprio interpretador estarão presentes em "sys.orig_argv" e
   ausentes em "sys.argv".

   Adicionado na versão 3.10.

sys.path

   Uma lista de strings que especifica o caminho de pesquisa para
   módulos. Inicializado a partir da variável de ambiente
   "PYTHONPATH", mais um padrão dependente da instalação.

   Por padrão, conforme inicializado na inicialização do programa, um
   caminho potencialmente inseguro é adicionado ao "sys.path" (*antes*
   das entradas inseridas como resultado de "PYTHONPATH"):

   * A linha de comando "python -m módulo": adiciona o diretório de
     trabalho atual

   * A linha de comando "python script.py": prefixa o diretório do
     script. Se for um link simbólico, resolve links simbólicos.

   * As linhas de comando "python -c código" e "python" (REPL):
     adiciona uma string vazia, que indica o diretório de trabalho
     atual.

   Para não acrescentar esse caminho potencialmente inseguro, use a
   opção de linha de comando "-P" ou a variável de ambiente
   "PYTHONSAFEPATH".

   Um programa é livre para modificar esta lista para seus próprios
   propósitos. Somente strings devem ser adicionadas a "sys.path";
   todos os outros tipos de dados são ignorados durante a importação.

   Ver também:

     * Módulo "site" Descreve como usar arquivos .pth para estender
       "sys.path".

sys.path_hooks

   Uma lista de chamáveis que recebem um argumento de caminho para
   tentar criar um *localizador* para o caminho. Se um localizador
   puder ser criado, ele deve ser retornado pelo chamável, senão, ele
   levanta "ImportError".

   Originalmente especificado na **PEP 302**.

sys.path_importer_cache

   Um dicionário atuando como um cache para objetos do *localizador*.
   As chaves são caminhos que foram passados para "sys.path_hooks" e
   os valores são os localizadores que são encontrados. Se um caminho
   for um caminho de sistema de arquivo válido, mas nenhum localizador
   for encontrado em "sys.path_hooks", então "None" é armazenado.

   Originalmente especificado na **PEP 302**.

sys.platform

   Uma string contendo um identificador da plataforma. Valores
   conhecidos são:

   +------------------+-----------------------------+
   | Sistema          | Valor de "platform"         |
   |==================|=============================|
   | AIX              | "'aix'"                     |
   +------------------+-----------------------------+
   | Android          | "'android'"                 |
   +------------------+-----------------------------+
   | Emscripten       | "'emscripten'"              |
   +------------------+-----------------------------+
   | FreeBSD          | "'freebsd'"                 |
   +------------------+-----------------------------+
   | iOS              | "'ios'"                     |
   +------------------+-----------------------------+
   | Linux            | "'linux'"                   |
   +------------------+-----------------------------+
   | macOS            | "'darwin'"                  |
   +------------------+-----------------------------+
   | Windows          | "'win32'"                   |
   +------------------+-----------------------------+
   | Windows/Cygwin   | "'cygwin'"                  |
   +------------------+-----------------------------+
   | WASI             | "'wasi'"                    |
   +------------------+-----------------------------+

   Em sistemas Unix não listados na tabela, o valor é o nome do
   sistema operacional em letras minúsculas, conforme retornado por
   "uname -s", com a primeira parte da versão, conforme retornado por
   "uname -r" anexada, por exemplo, "'sunos5'", *no momento em que o
   Python foi construído*. A menos que você queira testar uma versão
   específica do sistema, é recomendável usar o seguinte idioma:

      if sys.platform.startswith('sunos'):
          # código específico do SunOS aqui...

   Alterado na versão 3.3: No Linux, "sys.platform" não contém mais a
   versão principal. É sempre "'linux'", em vez de "'linux2'" ou
   "'linux3'".

   Alterado na versão 3.8: No AIX, "sys.platform" não contém mais a
   versão principal. É sempre "'aix'", em vez de "'aix5'" ou "'aix7'".

   Alterado na versão 3.13: No Android, "sys.platform" agora retorna
   "'android'" em vez de "'linux'".

   Alterado na versão 3.14: No FreeBSD, "sys.platform" não contém mais
   a versão principal. É sempre "'freebsd'", em vez de "'freebsd13'"
   ou "'freebsd14'".

   Ver também:

     "os.name" tem uma granularidade mais substancial. "os.uname()"
     fornece informações de versão dependentes do sistema.

     O módulo "platform" fornece verificações detalhadas sobre a
     identificação do sistema.

sys.platlibdir

   Nome do diretório da biblioteca específica da plataforma. É usado
   para construir o caminho da biblioteca padrão e os caminhos dos
   módulos de extensão instalados.

   É igual a ""lib"" na maioria das plataformas. No Fedora e SuSE, é
   igual a ""lib64"" em plataformas de 64 bits, o que fornece os
   seguintes caminhos "sys.path" (onde "X.Y" é a versão "major.minor"
   do Python):

   * "/usr/lib64/pythonX.Y/": Biblioteca padrão (como "os.py" do
     módulo "os")

   * "/usr/lib64/pythonX.Y/lib-dynload/": Módulos de extensão C da
     biblioteca padrão (como o módulo "errno", o nome exato do arquivo
     é específico da plataforma)

   * "/usr/lib/pythonX.Y/site-packages/" (sempre usa "lib", não
     "sys.platlibdir"): Módulos de terceiros

   * "/usr/lib64/pythonX.Y/site-packages/": Módulos de extensão C de
     pacotes de terceiros

   Adicionado na versão 3.9.

sys.prefix

   Uma string que fornece o prefixo do diretório específico do site
   onde os arquivos Python independentes de plataforma são instalados;
   no Unix, o padrão é "/usr/local". Isso pode ser definido no momento
   da construção com o argumento "--prefix" para o script
   **configure**. Veja Caminhos de instalação para caminhos derivados.

   Nota:

     Se um ambiente virtual estiver em vigor, este "prefix" vai
     apontar para o ambiente virtual. O valor para a instalação do
     Python ainda estará disponível, via "base_prefix". Confira
     Ambientes virtuais para mais informações.

   Alterado na versão 3.14: Ao executar em um ambiente virtual,
   "prefix" e "exec_prefix" agora são definidos como o prefixo do
   ambiente virtual pela inicialização do caminho, em vez de "site".
   Isso significa que "prefix" e "exec_prefix" sempre apontam para o
   ambiente virtual, mesmo quando "site" está desabilitado ("-S").

sys.ps1
sys.ps2

   Strings especificando o prompt primário e secundário do
   interpretador. Elas são definidas somente se o interpretador
   estiver no modo interativo. Seus valores iniciais neste caso são
   "'>>> '" e "'... '". Se um objeto não string for atribuído a
   qualquer variável, seu "str()" é reavaliado cada vez que o
   interpretador se prepara para ler um novo comando interativo; isso
   pode ser usado para implementar um prompt dinâmico.

sys.setdlopenflags(n)

   Define os sinalizadores usados pelo interpretador para chamadas
   "dlopen()", como quando o interpretador carrega módulos de
   extensão. Entre outras coisas, isso habilitará uma resolução
   preguiçosa de símbolos ao importar um módulo, se chamado como
   "sys.setdlopenflags(0)". Para compartilhar símbolos entre módulos
   de extensão, chame como "sys.setdlopenflags(os.RTLD_GLOBAL)". Nomes
   simbólicos para os valores de sinalizadores podem ser encontrados
   no módulo "os" (constantes "RTLD_*xxx*", por exemplo,
   "os.RTLD_LAZY").

   Disponibilidade: Unix.

sys.set_int_max_str_digits(maxdigits)

   Define a limitação de comprimento de string na conversão para
   inteiro usada por este interpretador. Veja também
   "get_int_max_str_digits()".

   Adicionado na versão 3.11.

sys.set_lazy_imports(mode)

   Sets the global lazy imports mode. The *mode* parameter must be one
   of the following strings:

   * ""normal"": Only imports explicitly marked with the "lazy"
     keyword are lazy

   * ""all"": All top-level imports become potentially lazy

   This function is intended for advanced users who need to control
   lazy imports across their entire application. Library developers
   should generally not use this function as it affects the runtime
   execution of applications.

   In addition to the mode, lazy imports can be controlled via the
   filter provided by "set_lazy_imports_filter()".

   See also "get_lazy_imports()" and **PEP 810**.

   Adicionado na versão 3.15.

sys.set_lazy_imports_filter(filter)

   Sets the lazy imports filter callback. The *filter* parameter must
   be a callable or "None" to clear the filter.

   The filter function is called for every potentially lazy import to
   determine whether it should actually be lazy. It should have the
   following signature:

      def filter(importing_module: str, imported_module: str,
                 fromlist: tuple[str, ...] | None) -> bool

   The function is called with three positional arguments:

   * *importing_module* is the name of the module doing the import

   * *imported_module* is the resolved name of the module being
     imported (for example, "lazy from .spam import eggs" passes
     "package.spam")

   * *fromlist* is the tuple of names being imported (for "from ...
     import" statements), or "None" for regular imports

   The filter should return "True" to allow the import to be lazy, or
   "False" to force an eager import.

   This is an advanced feature intended for specialized users who need
   fine-grained control over lazy import behavior.

   See also "get_lazy_imports_filter()" and **PEP 810**.

   Adicionado na versão 3.15.

sys.setprofile(profilefunc)

   Define a função de perfil do sistema, que permite implementar um
   perfilador de código-fonte Python em Python. Veja o capítulo
   profile --- Pure Python profiler para mais informações sobre o
   perfilador Python. A função de perfil do sistema é chamada de forma
   semelhante à função de rastreamento do sistema (veja "settrace()"),
   mas é chamada com eventos diferentes, por exemplo, não é chamada
   para cada linha de código executada (apenas na chamada e retorno,
   mas o evento de retorno é relatado mesmo quando uma exceção foi
   definida). A função é específica do thread, mas não há como o
   perfilador saber sobre trocas de contexto entre threads, então não
   faz sentido usá-la na presença de vários threads. Além disso, seu
   valor de retorno não é usado, então ele pode simplesmente retornar
   "None". Um erro na função de perfil fará com que sua própria
   definição seja removida.

   Nota:

     O mesmo mecanismo de rastreamento é usado para "setprofile()"
     como "settrace()". Para rastrear chamadas com "setprofile()"
     dentro de uma função de rastreamento (por exemplo, em um ponto de
     interrupção do depurador), consulte "call_tracing()".

   As funções de perfil devem ter três argumentos: *frame*, *event* e
   *arg*. *frame* é o quadro de pilha atual. *event* é uma string:
   "'call'", "'return'", "'c_call'", "'c_return'" ou "'c_exception'".
   *arg* depende do tipo de evento.

   Os eventos têm o seguinte significado:

   "'call'"
      Uma função é chamada (ou algum outro bloco de código é
      inserido). A função de perfil é chamada; *arg* é "None".

   "'return'"
      Uma função (ou outro bloco de código) está prestes a retornar. A
      função de perfilação é chamada; *arg* é o valor que será
      retornado, ou "None" se o evento for causado por uma exceção
      sendo levantada.

   "'c_call'"
      Uma função C está prestes a ser chamada. Pode ser uma função de
      extensão ou uma embutida. *arg* é o objeto da função C.

   "'c_return'"
      Uma função C foi retornada. *arg* é o objeto da função C.

   "'c_exception'"
      Uma função C levantou uma exceção. *arg* é o objeto da função C.

   Levanta um evento de auditoria "sys.setprofile" sem argumentos.

sys.setrecursionlimit(limit)

   Define a profundidade máxima da pilha do interpretador Python para
   *limit*. Esse limite impede que a recursão infinita cause um
   estouro da pilha C e trave o Python.

   O limite mais alto possível depende da plataforma. Um usuário pode
   precisar definir o limite mais alto quando tiver um programa que
   exija recursão profunda e uma plataforma que dê suporte a um limite
   mais alto. Isso deve ser feito com cuidado, porque um limite muito
   alto pode levar a uma falha.

   Se o novo limite for muito baixo na profundidade de recursão atual,
   uma exceção "RecursionError" será levantada.

   Alterado na versão 3.5.1: Uma exceção "RecursionError" agora é
   levantada se o novo limite for muito baixo na profundidade de
   recursão atual.

sys.setswitchinterval(interval)

   Define o intervalo de troca de thread do interpretador (em
   segundos). Este valor de ponto flutuante determina a duração ideal
   das "fatias de tempo" alocadas para threads Python em execução
   simultânea. Observe que o valor real pode ser maior, especialmente
   se funções ou métodos internos de execução longa forem usados. Além
   disso, qual thread se torna agendada no final do intervalo é uma
   decisão do sistema operacional. O interpretador não tem seu próprio
   escalonador.

   Adicionado na versão 3.2.

sys.settrace(tracefunc)

   Define a função trace do sistema, que permite que você implemente
   um depurador de código-fonte Python em Python. A função é
   específica de thread; para um depurador suportar múltiplas threads,
   ele deve registrar uma função trace usando "settrace()" para cada
   thread que está sendo depurada ou usar "threading.settrace()".

   As funções de rastreamento devem ter três argumentos: *frame*,
   *event* e *arg*. *frame* é o quadro de pilha atual. *event* é uma
   string: "'call'", "'line'", "'return'", "'exception'" ou
   "'opcode'". *arg* depende do tipo de evento.

   A função de rastreamento é invocada (com *event* definido como
   "'call'") sempre que um novo escopo local é inserido; ela deve
   retornar uma referência a uma função de rastreamento local a ser
   usada para o novo escopo, ou "None" se o escopo não deve ser
   rastreado.

   A função de rastreamento local deve retornar uma referência a si
   mesma ou a outra função que seria então usada como a função de
   rastreamento local para o escopo.

   Se ocorrer algum erro na função de rastreamento, ela será
   desativada, assim como "settrace(None)" é chamado.

   Nota:

     O rastreamento é desabilitado ao chamar a função de rastreamento
     (por exemplo, uma função definida por "settrace()"). Para
     rastreamento recursivo, veja "call_tracing()".

   Os eventos têm o seguinte significado:

   "'call'"
      Uma função é chamada (ou algum outro bloco de código é
      inserido). A função de rastreamento global é chamada; *arg* é
      "None"; o valor de retorno especifica a função de rastreamento
      local.

   "'line'"
      The interpreter is about to execute a new line of code or re-
      execute the condition of a loop.  The local trace function is
      called; *arg* is "None"; the return value specifies the new
      local trace function.  See InternalDocs/code_objects.md for a
      detailed explanation of how this works. Per-line events may be
      disabled for a frame by setting "f_trace_lines" to "False" on
      that frame.

   "'return'"
      Uma função (ou outro bloco de código) está prestes a retornar. A
      função de rastreamento local é chamada; *arg* é o valor que será
      retornado, ou "None" se o evento for causado por uma exceção
      sendo levantada. O valor de retorno da função de rastreamento é
      ignorado.

   "'exception'"
      Ocorreu uma exceção. A função de rastreamento local é chamada;
      *arg* é uma tupla "(exception, value, traceback)"; o valor de
      retorno especifica a nova função de rastreamento local.

   "'opcode'"
      O interpretador está prestes a executar um novo opcode (veja
      "dis" para detalhes do opcode). A função de rastreamento local é
      chamada; *arg* é "None"; o valor de retorno especifica a nova
      função de rastreamento local. Eventos por opcode não são
      emitidos por padrão: eles devem ser explicitamente solicitados
      definindo "f_trace_opcodes" como "True" no quadro.

   Observe que, à medida que uma exceção é propagada pela cadeia de
   chamadores, um evento "'exception'" é gerado em cada nível.

   Para um uso mais refinado, é possível definir uma função de
   rastreamento atribuindo "frame.f_trace = tracefunc" explicitamente,
   em vez de depender de ser definida indiretamente por meio do valor
   de retorno de uma função de rastreamento já instalada. Isso também
   é necessário para ativar a função de rastreamento no quadro atual,
   o que "settrace()" não faz. Observe que, para que isso funcione,
   uma função de rastreamento global deve ter sido instalada com
   "settrace()" para habilitar o maquinário de rastreamento em tempo
   de execução, mas não precisa ser a mesma função de rastreamento
   (por exemplo, pode ser uma função de rastreamento de baixa
   sobrecarga que simplesmente retorna "None" para se desabilitar
   imediatamente em cada quadro).

   Para mais informações sobre objetos de código e quadro, consulte A
   hierarquia de tipos padrão.

   Levanta um evento de auditoria "sys.settrace" sem argumentos.

   A função "settrace()" destina-se apenas à implementação de
   depuradores, perfiladores, ferramentas de cobertura e similares.
   Seu comportamento faz parte da plataforma de implementação, e não
   da definição da linguagem e, portanto, pode não estar disponível em
   todas as implementações do Python.

   Alterado na versão 3.7: Tipo de evento "'opcode'" adicionado;
   atributos "f_trace_lines" e "f_trace_opcodes" adicionados a quadros

sys.set_asyncgen_hooks([firstiter] [, finalizer])

   Aceita dois argumentos nomeados opcionais que são chamáveis que
   aceitam um *iterador gerador assíncrono* como argumento. O chamável
   *firstiter* será chamado quando um gerador assíncrono for iterado
   pela primeira vez. O *finalizer* será chamado quando um gerador
   assíncrono estiver prestes a ser coletado como lixo.

   Levanta um evento de auditoria "sys.set_asyncgen_hooks_firstiter"
   sem argumentos.

   Levanta um evento de auditoria "sys.set_asyncgen_hooks_finalizer"
   sem argumentos.

   Dois eventos de auditoria são gerados porque a API subjacente
   consiste em duas chamadas, cada uma das quais deve levantar seu
   próprio evento.

   Adicionado na versão 3.6: Veja a **PEP 525** para mais detalhes, e
   para um exemplo de referência de um método *finalizer* veja a
   implementação de "asyncio.Loop.shutdown_asyncgens" em
   Lib/asyncio/base_events.py

   Nota:

     Esta função foi adicionada provisoriamente (veja **PEP 411** para
     detalhes.)

sys.set_coroutine_origin_tracking_depth(depth)

   Permite habilitar ou desabilitar o rastreamento de origem de
   corrotina. Quando habilitado, o atributo "cr_origin" em objetos de
   corrotina conterá uma tupla de tuplas (nome do arquivo, número da
   linha, nome da função) descrevendo o traceback onde o objeto
   corrotina foi criado, com a chamada mais recente primeiro. Quando
   desabilitado, "cr_origin" será "None".

   Para habilitar, passe um valor *depth* maior que zero; isso define
   o número de quadros cujas informações serão capturadas. Para
   desabilitar, defina *depth* para zero.

   Esta configuração é específica do thread.

   Adicionado na versão 3.7.

   Nota:

     Esta função foi adicionada provisoriamente (veja **PEP 411** para
     detalhes.) Use-a apenas para propósitos de depuração.

sys.activate_stack_trampoline(backend, /)

   Ativa o trampolim do perfilador de pilha *backend*. O único backend
   suportado é ""perf"".

   Os trampolins empilháveis não podem ser ativados se o JIT estiver
   ativo.

   Disponibilidade: Linux.

   Adicionado na versão 3.12.

   Ver também:

     * Python support for the perf map compatible profilers

     * https://perf.wiki.kernel.org

sys.deactivate_stack_trampoline()

   Desativa o backend trampolim do perfilador de pilha atual.

   Se nenhum perfilador de pilha estiver ativado, esta função não terá
   efeito.

   Disponibilidade: Linux.

   Adicionado na versão 3.12.

sys.is_stack_trampoline_active()

   Retorna "True" se um trampolim de perfilador de pilha estiver
   ativo.

   Disponibilidade: Linux.

   Adicionado na versão 3.12.

sys.remote_exec(pid, script)

   Executa *script*, um arquivo contendo código Python no processo
   remoto com o *pid* fornecido.

   Esta função retorna imediatamente, e o código será executado pela
   thread principal do processo de destino na próxima oportunidade
   disponível, de forma semelhante à manipulação de sinais. Não há
   interface para determinar quando o código foi executado. O chamador
   é responsável por garantir que o arquivo ainda exista sempre que o
   processo remoto tentar lê-lo e que ele não tenha sido sobrescrito.

   O processo remoto deve estar executando um interpretador CPython da
   mesma versão principal e secundária que o processo local. Se o
   interpretador local ou remoto for de pré-lançamento (alfa, beta ou
   candidato a lançamento), os interpretadores local e remoto devem
   ser exatamente da mesma versão.

   See Protocolo de anexação de depuração remota for more information
   about the remote debugging mechanism.

   Quando o código é executado no processo remoto, um evento de
   auditoria "sys.remote_exec" é gerado com o *pid* e o caminho para o
   arquivo de script. Este evento é levantado no processo que chamou
   "sys.remote_exec()".

   Quando o script é executado no processo remoto, um evento de
   auditoria "cpython.remote_debugger_script" é levantado com o
   caminho no processo remoto. Este evento é levantado no processo
   remoto, não naquele que chamou "sys.remote_exec()".

   Disponibilidade: Unix, Windows.

   Adicionado na versão 3.14: See **PEP 768** for more details.

sys._enablelegacywindowsfsencoding()

   Altera *tratador de erros e codificação do sistema de arquivos*
   para 'replace' e 'mbcs' respectivamente, para consistência com
   versões do Python anteriores à 3.6.

   Isso é equivalente a definir a variável de ambiente
   "PYTHONLEGACYWINDOWSFSENCODING" antes de iniciar o Python.

   Veja também "sys.getfilesystemencoding()" e
   "sys.getfilesystemencodeerrors()".

   Disponibilidade: Windows.

   Nota:

     Alterar a codificação do sistema de arquivos após a inicialização
     do Python é arriscado porque o fsencoding antigo ou os caminhos
     codificados pelo fsencoding antigo podem estar armazenados em
     cache em algum lugar. Use "PYTHONLEGACYWINDOWSFSENCODING" em vez
     disso.

   Adicionado na versão 3.6: Veja **PEP 529** para mais detalhes.

   Descontinuado desde a versão 3.13, será removido na versão 3.16:
   Use "PYTHONLEGACYWINDOWSFSENCODING".

sys.stdin
sys.stdout
sys.stderr

   *Objetos arquivo* usados pelo interpretador para entrada padrão,
   saída e erros:

   * "stdin" é usado para todas as entradas interativas (incluindo
     chamadas para "input()");

   * "stdout" é usado para a saída das instruções "print()" e
     *expressões* e para os prompts de "input()";

   * Os prompts do próprio interpretador e suas mensagens de erro vão
     para "stderr".

   Esses fluxos são *arquivos texto* regulares como aqueles retornados
   pela função "open()". Seus parâmetros são escolhidos da seguinte
   forma:

   * The encoding and error handling are initialized from
     "PyConfig.stdio_encoding" and "PyConfig.stdio_errors".

     No Windows, o UTF-8 é usado para o dispositivo de console.
     Dispositivos não-caracteres, como arquivos de disco e pipes, usam
     a codificação da localidade do sistema (ou seja, a página de
     código ANSI). Dispositivos de caracteres não-console, como NUL
     (ou seja, onde "isatty()" retorna "True") usam o valor das
     páginas de código de entrada e saída do console na inicialização,
     respectivamente para stdin e stdout/stderr. Isso assume como
     padrão a *codificação da localidade* do sistema se o processo não
     for inicialmente anexado a um console.

     O comportamento especial do console pode ser substituído
     definindo a variável de ambiente PYTHONLEGACYWINDOWSSTDIO antes
     de iniciar o Python. Nesse caso, as páginas de código do console
     são usadas como para qualquer outro dispositivo de caractere.

     Em todas as plataformas, você pode substituir a codificação de
     caracteres definindo a variável de ambiente "PYTHONIOENCODING"
     antes de iniciar o Python ou usando a nova opção de linha de
     comando "-X" "utf8" e a variável de ambiente "PYTHONUTF8". No
     entanto, para o console do Windows, isso só se aplica quando
     "PYTHONLEGACYWINDOWSSTDIO" também está definido.

   * Quando interativo, o fluxo "stdout" é armazenado em buffer de
     linha. Caso contrário, ele é armazenado em buffer de bloco como
     arquivos texto comuns. O fluxo "stderr" é armazenado em buffer de
     linha em ambos os casos. Você pode tornar ambos os fluxos sem
     buffer passando a opção de linha de comando "-u" ou definindo a
     variável de ambiente "PYTHONUNBUFFERED".

   Alterado na versão 3.9: "stderr" não interativo agora é armazenado
   em buffer de linha em vez de totalmente armazenado em buffer.

   Nota:

     Para escrever ou ler dados binários de/para os fluxos padrão, use
     o objeto binário subjacente "buffer". Por exemplo, para escrever
     bytes em "stdout", use
     "sys.stdout.buffer.write(b'abc')".Entretanto, se você estiver
     escrevendo uma biblioteca (e não controlar em qual contexto seu
     código será executado), esteja ciente de que os fluxos padrão
     podem ser substituídos por objetos arquivo ou similares, como
     "io.StringIO", que não oferecem suporte ao atributo "buffer".

sys.__stdin__
sys.__stdout__
sys.__stderr__

   Esses objetos contêm os valores originais de "stdin", "stderr" e
   "stdout" no início do programa. Eles são usados durante a
   finalização e podem ser úteis para imprimir no fluxo padrão real,
   não importa se o objeto "sys.std*" foi redirecionado.

   Ele também pode ser usado para restaurar os arquivos reais para
   objetos arquivo de trabalho conhecidos, caso tenham sido
   substituídos por um objeto quebrado. No entanto, a maneira
   preferida de fazer isso é salvar explicitamente o fluxo anterior
   antes de substituí-lo e restaurar o objeto salvo.

   Nota:

     Sob algumas condições, "stdin", "stdout" e "stderr", bem como os
     valores originais de "__stdin__", "__stdout__" e "__stderr__"
     podem ser "None". Geralmente é o caso de aplicativos GUI do
     Windows que não estão conectados a um console e aplicativos
     Python iniciados com **pythonw**.

sys.stdlib_module_names

   Um frozenset de strings contendo os nomes dos módulos da biblioteca
   padrão.

   É o mesmo em todas as plataformas. Módulos que não estão
   disponíveis em algumas plataformas e módulos desabilitados na
   construção do Python também são listados. Todos os tipos de módulos
   são listados: Python puro, módulos embutidos, congelados e de
   extensão. Módulos de teste são excluídos.

   Para pacotes, somente o pacote principal é listado: subpacotes e
   submódulos não são listados. Por exemplo, o pacote "email" é
   listado, mas o subpacote "email.mime" e o submódulo "email.message"
   não são listados.

   Veja também a lista de "sys.builtin_module_names".

   Adicionado na versão 3.10.

sys.thread_info

   Uma *tupla nomeada* contendo informações sobre a implementação de
   threads.

   thread_info.name

      O nome da implementação da thread:

      * ""nt"": Threads do Windows

      * ""pthread"": Threads do POSIX

      * ""pthread-stubs"": stubs de threads POSIX (em plataformas
        WebAssembly que não implementam threads).

      * ""solaris"": Threads do Solaris

   thread_info.lock

      O nome da implementação de trava.

      * ""semaphore"": a lock uses a semaphore (Python 3.14 and older)

      * ""mutex+cond"": a lock uses a mutex and a condition variable
        (Python 3.14 and older)

      * ""pymutex"": a lock uses the "PyMutex" implementation (Python
        3.15 and newer)

      * "None" se essa informação for desconhecida

   thread_info.version

      O nome e a versão da biblioteca de threads. É uma string, ou
      "None" se essa informação for desconhecida.

   Adicionado na versão 3.3.

sys.tracebacklimit

   Quando essa variável é definida como um valor inteiro, ela
   determina o número máximo de níveis de informações de traceback
   impressas quando ocorre uma exceção não tratada. O padrão é "1000".
   Quando definida como "0" ou menos, todas as informações de
   traceback são suprimidas e apenas o tipo e o valor da exceção são
   impressos.

sys.unraisablehook(unraisable, /)

   Manipula uma exceção não levantada

   Chamada quando uma exceção ocorreu, mas não há como o Python
   manipulá-la. Por exemplo, quando um destrutor levanta uma exceção
   ou durante a coleta de lixo ("gc.collect()").

   O argumento *unraisable* tem os seguintes atributos:

   * "exc_type": Tipo de exceção.

   * "exc_value": Valor da exceção, pode ser "None".

   * "exc_traceback": Traceback da exceção, pode ser "None".

   * "err_msg": Mensagem de erro, pode ser "None".

   * "object": O objeto que causa a exceção pode ser "None".

   The default hook formats "err_msg" and "object" as: "f'{err_msg}:
   {object!r}'"; use "Exception ignored in" error message if "err_msg"
   is "None". Similar to the "traceback" module, this adds color to
   exceptions by default. This can be disabled using environment
   variables.

   "sys.unraisablehook()" pode ser substituída para controlar como
   exceções não levantáveis são manipuladas.

   Alterado na versão 3.15: Exceptions are now printed with colorful
   text.

   Ver também: "excepthook()", que manipula exceções não capturadas.

   Aviso:

     Armazena "exc_value" usando um gancho personalizado pode criar um
     ciclo de referência. Ele deve ser limpo explicitamente para
     quebrar o ciclo de referência quando a exceção não for mais
     necessária.Armazenar "object" usando um gancho personalizado pode
     ressuscitá-lo se ele for definido como um objeto que está sendo
     finalizado. Evite armazenar "object" após o gancho personalizado
     ser concluído para evitar ressuscitar objetos.

   Levanta um evento de auditoria "sys.unraisablehook" com argumentos
   *hook* e *unraisable* quando ocorrer uma exceção que não puder ser
   manipulada. O objeto *unraisable* é o mesmo que será passado para o
   gancho. Se nenhum gancho tiver sido definido, *hook* pode ser
   "None".

   Adicionado na versão 3.8.

sys.version

   Uma string contendo o número da versão do interpretador Python mais
   informações adicionais sobre o número da construção e o compilador
   usado. Esta string é exibida quando o interpretador interativo é
   iniciado. Não extraia informações de versão dela, em vez disso, use
   "version_info" e as funções fornecidas pelo módulo "platform".

sys.api_version

   A versão da API C, equivalente à macro C  "PYTHON_API_VERSION".
   Definido para retrocompatibilidade.

   Atualmente, essa constante não é atualizada nas novas versões de
   Python e não é útil para controle de versão. Isso pode mudar no
   futuro.

sys.version_info

   Uma tupla contendo os cinco componentes do número da versão:
   *major*, *minor*, *micro*, *releaselevel* e *serial*. Todos os
   valores, exceto *releaselevel*, são inteiros; o nível de versão é
   "'alpha'", "'beta'", "'candidate'" ou "'final'". O valor
   "version_info" correspondente à versão 2.0 do Python é "(2, 0, 0,
   'final', 0)". Os componentes também podem ser acessados por nome,
   então "sys.version_info[0]" é equivalente a
   "sys.version_info.major" e assim por diante.

   Alterado na versão 3.1: Adiciona componentes nomeados como
   atributos.

sys.warnoptions

   Este é um detalhe de implementação do framework de avisos; não
   modifique este valor. Consulte o módulo "warnings" para obter mais
   informações sobre o framework de avisos.

sys.winver

   The version number used to form registry keys on Windows platforms.
   This is stored as string resource 1000 in the Python DLL.  The
   value is normally the major and minor versions of the running
   Python interpreter.  It is provided in the "sys" module for
   informational purposes; modifying this value has no effect on the
   registry keys used by Python.

   Disponibilidade: Windows.

sys.monitoring

   Espaço de nomes contendo funções e constantes para função de
   retorno de registro e controle de eventos de monitoramento. Veja
   "sys.monitoring" para detalhes.

sys._xoptions

   Um dicionário dos vários sinalizadores específicos de implementação
   passados pela opção de linha de comando "-X". Os nomes de opção são
   mapeados para seus valores, se fornecidos explicitamente, ou para
   "True". Exemplo:

      $ ./python -Xa=b -Xc
      Python 3.2a3+ (py3k, Oct 16 2010, 20:14:50)
      [GCC 4.4.3] on linux2
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import sys
      >>> sys._xoptions
      {'a': 'b', 'c': True}

   Esta é uma maneira específica do CPython de acessar opções passadas
   por "-X". Outras implementações podem exportá-las por outros meios,
   ou não exportá-las.

   Adicionado na versão 3.2.

-[ Citações ]-

[C99] ISO/IEC 9899:1999.  "Programming languages -- C." Um rascunho
      público desta norma está disponível em https://www.open-
      std.org/jtc1/sc22/wg14/www/docs/n1256.pdf.
