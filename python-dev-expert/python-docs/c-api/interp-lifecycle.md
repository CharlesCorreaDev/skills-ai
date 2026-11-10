Interpreter initialization and finalization
*******************************************

Veja Configuração de inicialização do Python para detalhes sobre como
configurar o interpretador antes da inicialização.


Before Python initialization
============================

In an application embedding Python, the "Py_Initialize()" function
must be called before using any other Python/C API functions; with the
exception of a few functions and the global configuration variables.

As seguintes funções podem ser seguramente chamadas antes da
inicialização do Python.

* Funções que inicializam o interpretador:

  * "Py_Initialize()"

  * "Py_InitializeEx()"

  * "Py_InitializeFromConfig()"

  * "Py_BytesMain()"

  * "Py_Main()"

  * as funções de pré-inicialização de tempo de execução cobertas em
    Configuração de inicialização do Python

* Funções de configuração

  * "PyImport_AppendInittab()"

  * "PyImport_ExtendInittab()"

  * "PyInitFrozenExtensions()"

  * "PyMem_SetAllocator()"

  * "PyMem_SetupDebugHooks()"

  * "PyObject_SetArenaAllocator()"

  * "Py_SetProgramName()"

  * "Py_SetPythonHome()"

  * as funções de configuração cobertas em Configuração de
    inicialização do Python

* Funções informativas:

  * "Py_IsInitialized()"

  * "PyMem_GetAllocator()"

  * "PyObject_GetArenaAllocator()"

  * "Py_GetBuildInfo()"

  * "Py_GetCompiler()"

  * "Py_GetCopyright()"

  * "Py_GetPlatform()"

  * "Py_GetVersion()"

* Utilitários:

  * "Py_DecodeLocale()"

  * o relatório de status e funções utilitárias cobertas em
    Configuração de inicialização do Python

* Alocadores de memória:

  * "PyMem_RawMalloc()"

  * "PyMem_RawRealloc()"

  * "PyMem_RawCalloc()"

  * "PyMem_RawFree()"

* Sincronização:

  * "PyMutex_Lock()"

  * "PyMutex_Unlock()"

Nota:

  Despite their apparent similarity to some of the functions listed
  above, the following functions **should not be called** before the
  interpreter has been initialized: "Py_EncodeLocale()",
  "PyEval_InitThreads()", and "Py_RunMain()".


Variáveis de configuração global
================================

Python tem variáveis para a configuração global a fim de controlar
diferentes características e opções. Por padrão, estes sinalizadores
são controlados por opções de linha de comando.

Quando um sinalizador é definido por uma opção, o valor do sinalizador
é o número de vezes que a opção foi definida. Por exemplo, "-b" define
"Py_BytesWarningFlag" para 1 e "-bb" define "Py_BytesWarningFlag" para
2.

int Py_BytesWarningFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.bytes_warning" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Emite um aviso ao comparar "bytes" ou "bytearray" com "str" ou
   "bytes" com "int". Emite um erro se for maior ou igual a "2".

   Definida pela opção "-b".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_DebugFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.parser_debug" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Ativa a saída de depuração do analisador sintático (somente para
   especialistas, dependendo das opções de compilação).

   Definida pela a opção "-d" e a variável de ambiente "PYTHONDEBUG".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_DontWriteBytecodeFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.write_bytecode" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Se definida como diferente de zero, o Python não tentará escrever
   arquivos ".pyc" na importação de módulos fonte.

   Definida pela opção "-B" e pela variável de ambiente
   "PYTHONDONTWRITEBYTECODE".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_FrozenFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.pathconfig_warnings" deve ser usada em seu
   lugar, consulte Configuração de inicialização do Python.

   Sinalizador privado usado pelos programas "_freeze_module" e
   "frozenmain".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_HashRandomizationFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração de "PyConfig.hash_seed" e "PyConfig.use_hash_seed"
   deve ser usada em seu lugar, consulte Configuração de inicialização
   do Python.

   Definida como "1" se a variável de ambiente "PYTHONHASHSEED"
   estiver definida como uma string não vazia.

   Se o sinalizador for diferente de zero, lê a variável de ambiente
   "PYTHONHASHSEED" para inicializar a semente de hash secreta.

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_IgnoreEnvironmentFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.use_environment" deve ser usada em seu
   lugar, consulte Configuração de inicialização do Python.

   Ignora todas as variáveis de ambiente "PYTHON*", por exemplo
   "PYTHONPATH" e "PYTHONHOME", que podem estar definidas.

   Definida pelas opções "-E" e "-I".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_InspectFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.inspect" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Quando um script é passado como primeiro argumento ou a opção "-c"
   é usada, entre no modo interativo após executar o script ou o
   comando, mesmo quando "sys.stdin" não parece ser um terminal.

   Definida pela opção "-i" e pela variável de ambiente
   "PYTHONINSPECT".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_InteractiveFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.interactive" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Definida pela opção "-i".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_IsolatedFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.isolated" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Executa o Python no modo isolado. No modo isolado, "sys.path" não
   contém nem o diretório do script nem o diretório de pacotes de
   sites do usuário.

   Definida pela opção "-I".

   Adicionado na versão 3.4.

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_LegacyWindowsFSEncodingFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyPreConfig.legacy_windows_fs_encoding" deve ser
   usada em seu lugar, consulte Configuração de inicialização do
   Python.

   Se o sinalizador for diferente de zero, use a codificação "mbcs"
   com o tratador de erros "replace", em vez da codificação UTF-8 com
   o tratador de erros "surrogatepass", para a codificação do sistema
   de arquivos e *tratador de erros e codificação do sistema de
   arquivos*.

   Definida como "1" se a variável de ambiente
   "PYTHONLEGACYWINDOWSFSENCODING" estiver definida como uma string
   não vazia.

   Veja **PEP 529** para mais detalhes.

   Disponibilidade: Windows.

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_LegacyWindowsStdioFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.legacy_windows_stdio" deve ser usada em seu
   lugar, consulte Configuração de inicialização do Python.

   Se o sinalizador for diferente de zero, usa "io.FileIO" em vez de
   "io._WindowsConsoleIO" para fluxos padrão "sys".

   Definida como "1" se a variável de ambiente
   "PYTHONLEGACYWINDOWSSTDIO" estiver definida como uma string não
   vazia.

   Veja a **PEP 528** para mais detalhes.

   Disponibilidade: Windows.

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_NoSiteFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.site_import" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Desabilita a importação do módulo "site" e as manipulações
   dependentes do site de "sys.path" que isso acarreta. Também
   desabilita essas manipulações se "site" for explicitamente
   importado mais tarde (chame "site.main()" se você quiser que eles
   sejam acionados).

   Definida pela opção "-S".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_NoUserSiteDirectory

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.user_site_directory" deve ser usada em seu
   lugar, consulte Configuração de inicialização do Python.

   Não adiciona o "diretório site-packages de usuário" a "sys.path".

   Definida pelas opções "-s" e "-I", e pela variável de ambiente
   "PYTHONNOUSERSITE".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_OptimizeFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.optimization_level" deve ser usada em seu
   lugar, consulte Configuração de inicialização do Python.

   Definida pela opção "-O" e pela variável de ambiente
   "PYTHONOPTIMIZE".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_QuietFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.quiet" deve ser usada em seu lugar, consulte
   Configuração de inicialização do Python.

   Não exibe as mensagens de direitos autorais e de versão nem mesmo
   no modo interativo.

   Definida pela opção "-q".

   Adicionado na versão 3.2.

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_UnbufferedStdioFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.buffered_stdio" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Força os fluxos stdout e stderr a não serem armazenados em buffer.

   Definida pela opção "-u" e pela variável de ambiente
   "PYTHONUNBUFFERED".

   Descontinuado desde a versão 3.12, removido na versão 3.15.

int Py_VerboseFlag

   Esta API é mantida para compatibilidade com versões anteriores: a
   configuração "PyConfig.verbose" deve ser usada em seu lugar,
   consulte Configuração de inicialização do Python.

   Exibe uma mensagem cada vez que um módulo é inicializado, mostrando
   o local (nome do arquivo ou módulo embutido) de onde ele é
   carregado. Se maior ou igual a "2", exibe uma mensagem para cada
   arquivo que é verificado durante a busca por um módulo. Também
   fornece informações sobre a limpeza do módulo na saída.

   Definida pela a opção "-v" e a variável de ambiente
   "PYTHONVERBOSE".

   Descontinuado desde a versão 3.12, removido na versão 3.15.


Inicializando e encerrando o interpretador
==========================================

void Py_Initialize()
    * Parte da ABI Estável.*

   Initialize the Python interpreter.  In an application embedding
   Python, this should be called before using any other Python/C API
   functions; see Before Python Initialization for the few exceptions.

   Isso inicializa a tabela de módulos carregados ("sys.modules") e
   cria os módulos fundamentais "builtins", "__main__" e "sys". Também
   inicializa o caminho de pesquisa de módulos ("sys.path"). Isso não
   define "sys.argv"; use a API da Configuração de inicialização do
   Python para isso. Isso é um no-op quando chamado pela segunda vez
   (sem chamar "Py_FinalizeEx()" primeiro). Não há valor de retorno; é
   um erro fatal se a inicialização falhar.

   Usa "Py_InitializeFromConfig()" para personalizar a Configuração de
   inicialização do Python.

   Nota:

     No Windows, altera o modo do console de "O_TEXT" para "O_BINARY",
     o que também afetará usos não Python do console usando o Runtime
     C.

void Py_InitializeEx(int initsigs)
    * Parte da ABI Estável.*

   Esta função funciona como "Py_Initialize()" se *initsigs* for "1".
   Se *initsigs* for "0", ela pula o registro de inicialização de
   manipuladores de sinal, o que pode ser útil quando o CPython é
   incorporado como parte de uma aplicação maior.

   Usa "Py_InitializeFromConfig()" para personalizar a Configuração de
   inicialização do Python.

PyStatus Py_InitializeFromConfig(const PyConfig *config)

   Inicializa o Python a partir da configuração *config*, conforme
   descrito em Initialization with PyConfig.

   Consulte a seção Configuração de inicialização do Python para obter
   detalhes sobre como pré-inicializar o interpretador, preencher a
   estrutura de configuração do tempo de execução e consultar a
   estrutura de status retornada.

int Py_IsInitialized()
    * Parte da ABI Estável.*

   Retorna verdadeiro (diferente de zero) quando o interpretador
   Python foi inicializado, falso (zero) se não. Após
   "Py_FinalizeEx()" ser chamado, isso retorna falso até que
   "Py_Initialize()" seja chamado novamente.

   Alterado na versão 3.15: This function no longer returns true until
   initialization has fully completed, including import of the "site"
   module.  Previously it could return true while "Py_Initialize()"
   was still running.

int Py_IsFinalizing()
    * Parte da ABI Estável desde a versão 3.13.*

   Retorna verdadeiro (diferente de zero) se o interpretador Python
   principal estiver em *desligamento*. Retorna falso (zero) caso
   contrário.

   Adicionado na versão 3.13.

int Py_FinalizeEx()
    * Parte da ABI Estável desde a versão 3.6.*

   Desfaz todas as inicializações feitas por "Py_Initialize()" e o uso
   subsequente de funções da API Python/C, e destrói todos os
   subinterpretadores (veja "Py_NewInterpreter()" abaixo) que foram
   criados e ainda não destruídos desde a última chamada a
   "Py_Initialize()". Esta operação é ineficaz quando chamada pela
   segunda vez (sem chamar "Py_Initialize()" novamente primeiro).

   Como isso é o inverso de "Py_Initialize()", ele deve ser chamado na
   mesma thread com o mesmo interpretador ativo. Isso significa a
   thread principal e o interpretador principal. Isso nunca deve ser
   chamado enquanto "Py_RunMain()" estiver em execução.

   Normalmente, o valor de retorno é "0". Se houver erros durante a
   finalização (limpeza de dados armazenados em buffer), "-1" será
   retornado.

   Note that Python will do a best effort at freeing all memory
   allocated by the Python interpreter.  Therefore, any C-Extension
   should make sure to correctly clean up all of the previously
   allocated PyObjects before using them in subsequent calls to
   "Py_Initialize()".  Otherwise it could introduce vulnerabilities
   and incorrect behavior.

   Esta função é fornecida por vários motivos. Uma aplicação de
   incorporação pode querer reiniciar o Python sem precisar reiniciar
   a própria aplicação. Uma aplicação que carregou o interpretador
   Python de uma biblioteca carregável dinamicamente (ou DLL) pode
   querer liberar toda a memória alocada pelo Python antes de
   descarregar a DLL. Durante uma busca por vazamentos de memória em
   uma aplicação, um desenvolvedor pode querer liberar toda a memória
   alocada pelo Python antes de sair da aplicação.

   **Bugs e advertências:** A destruição de módulos e objetos em
   módulos é feita em ordem aleatória; isso pode fazer com que
   destrutores (métodos "__del__()") falhem quando dependem de outros
   objetos (até mesmo funções) ou módulos. Módulos de extensão
   carregados dinamicamente pelo Python não são descarregados.
   Pequenas quantidades de memória alocadas pelo interpretador Python
   podem não ser liberadas (se você encontrar um vazamento, por favor,
   reporte-o). Memória presa em referências circulares entre objetos
   não é liberada. Strings internadas serão todas desalocadas
   independentemente de sua contagem de referências. Parte da memória
   alocada por módulos de extensão pode não ser liberada. Algumas
   extensões podem não funcionar corretamente se sua rotina de
   inicialização for chamada mais de uma vez; isso pode acontecer se
   uma aplicação chamar "Py_Initialize()" e "Py_FinalizeEx()" mais de
   uma vez. "Py_FinalizeEx()" não deve ser chamado recursivamente de
   dentro de si mesmo. Portanto, ele não deve ser chamado por nenhum
   código que possa ser executado como parte do processo de
   desligamento do interpretador, como manipuladores "atexit",
   finalizadores de objetos ou qualquer código que possa ser executado
   durante a limpeza dos arquivos de stdout e stderr.

   Levanta um evento de auditoria "cpython._PySys_ClearAuditHooks" sem
   argumentos.

   Adicionado na versão 3.6.

void Py_Finalize()
    * Parte da ABI Estável.*

   Esta é uma versão retrocompatível de "Py_FinalizeEx()" que
   desconsidera o valor de retorno.

int Py_BytesMain(int argc, char **argv)
    * Parte da ABI Estável desde a versão 3.8.*

   Semelhante a "Py_Main()", mas *argv* é um vetor de strings de
   bytes, permitindo que a aplicação chamadora delegue a etapa de
   decodificação de texto ao ambiente de execução do CPython.

   Adicionado na versão 3.8.

int Py_Main(int argc, wchar_t **argv)
    * Parte da ABI Estável.*

   O programa principal para o interpretador padrão, encapsulando um
   ciclo completo de inicialização/finalização, bem como comportamento
   adicional para implementar a leitura de configurações do ambiente e
   da linha de comando e, em seguida, executar "__main__" de acordo
   com a Linha de comando.

   Isso é disponibilizado para programas que desejam oferecer suporte
   à interface de linha de comando completa do CPython, em vez de
   apenas incorporar um ambiente de execução do Python em uma
   aplicação maior.

   Os parâmetros *argc* e *argv* são semelhantes aos passados para a
   função "main()" de um programa C, exceto que as entradas *argv* são
   primeiro convertidas para "wchar_t" usando "Py_DecodeLocale()".
   Também é importante observar que as entradas da lista de argumentos
   podem ser modificadas para apontar para strings diferentes daquelas
   passadas (no entanto, o conteúdo das strings apontadas pela lista
   de argumentos não é modificado).

   O valor de retorno é "2" se a lista de argumentos não representar
   uma linha de comando Python válida e, caso contrário, o mesmo que
   "Py_RunMain()".

   Em termos das APIs de configuração de tempo de execução do CPython
   documentadas na seção de configuração do ambiente de execução (e
   sem levar em conta o tratamento de erros), "Py_Main" é
   aproximadamente equivalente a:

      PyConfig config;
      PyConfig_InitPythonConfig(&config);
      PyConfig_SetArgv(&config, argc, argv);
      Py_InitializeFromConfig(&config);
      PyConfig_Clear(&config);

      Py_RunMain();

   Em uso normal, uma aplicação de incorporação chamará esta função
   *em vez* de chamar "Py_Initialize()", "Py_InitializeEx()" ou
   "Py_InitializeFromConfig()" diretamente, e todas as configurações
   serão aplicadas conforme descrito em outra parte desta
   documentação. Se esta função for chamada *após* uma chamada
   anterior à API de inicialização do ambiente de execução, as
   configurações de ambiente e de linha de comando que serão
   atualizadas dependem da versão (pois dependem de quais
   configurações oferecem suporte corretamente à modificação após já
   terem sido definidas uma vez na primeira inicialização do ambiente
   de execução).

int Py_FrozenMain(int argc, char **argv)

   The main program for a "frozen" Python program (an executable that
   embeds the interpreter together with the bytecode of the program's
   modules, as produced by the **freeze** utility; see Tools/freeze).

   This function initializes the interpreter, imports the frozen
   module named "__main__", and finalizes the interpreter. The frozen
   modules must have been registered in "PyImport_FrozenModules"
   before calling this function; it is a fatal error if "__main__" is
   not among them.

   *argc* and *argv* are byte strings like the arguments of a C
   program's "main" function, and are passed to the interpreter with
   "PyConfig_SetBytesArgv()". Unlike "Py_Main()", the arguments are
   not parsed as Python command line options ("PyConfig.parse_argv" is
   "0"), so all of them are made available to the program in
   "sys.argv". Apart from that, the interpreter uses the Python
   Configuration, so environment variables such as "PYTHONPATH" are
   honored. Warnings about the path configuration
   ("PyConfig.pathconfig_warnings") are suppressed. If "PYTHONINSPECT"
   is set and standard input is a terminal, an interactive prompt is
   run after "__main__" has finished, as with the "-i" option.

   Return "0" if "__main__" ran without an unhandled exception, "1"
   otherwise, and "120" if finalizing the interpreter failed (see
   "Py_FinalizeEx()"). An unhandled "SystemExit" terminates the
   process. If the interpreter cannot be initialized, the process
   exits via "Py_ExitStatusException()".

   On Windows, this function is not exported by the Python DLL. The
   **freeze** utility compiles "Python/frozenmain.c" into the frozen
   program instead, together with the Windows-specific hooks that the
   function requires.

int Py_RunMain(void)

   Executa o módulo principal em um ambiente de execução CPython
   totalmente configurado.

   Executa o comando ("PyConfig.run_command"), o script
   ("PyConfig.run_filename") ou o módulo ("PyConfig.run_module")
   especificado na linha de comando ou na configuração. Se nenhum
   desses valores estiver definido, executa o prompt interativo do
   Python (REPL) usando o espaço de nomes global do módulo "__main__".

   Se "PyConfig.inspect" não estiver definido (o padrão), o valor de
   retorno será "0" se o interpretador terminar normalmente (ou seja,
   sem levantar uma exceção), o status de saída de uma exceção
   "SystemExit" não tratada ou "1" para qualquer outra exceção não
   tratada.

   Se "PyConfig.inspect" estiver definido (como quando a opção "-i" é
   usada), em vez de retornar quando o interpretador for encerrado, a
   execução será retomada em um prompt interativo do Python (REPL)
   usando o espaço de nomes global do módulo "__main__". Se o
   interpretador for encerrado com uma exceção, ela será imediatamente
   levantada na sessão do REPL. O valor de retorno da função é então
   determinado pela forma como a *sessão do REPL* termina: "0", "1" ou
   o status de uma exceção "SystemExit", conforme especificado acima.

   Essa função sempre finaliza o interpretador Python antes de
   retornar.

   Consulte a Configuração do Python para obter um exemplo de um
   Python personalizado que sempre é executado em modo isolado usando
   "Py_RunMain()".

int PyUnstable_AtExit(PyInterpreterState *interp, void (*func)(void*), void *data)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Registra uma função de retorno de chamada "atexit" para o
   interpretador de destino *interp*. Isso é semelhante a
   "Py_AtExit()", mas recebe um interpretador explícito e um ponteiro
   de dados para a função de retorno de chamada.

   Deve haver um *estado de thread anexado* para *interp*.

   Adicionado na versão 3.13.


Cautions regarding interpreter finalization
===========================================

In the late stage of *interpreter shutdown*, after attempting to wait
for non-daemon threads to exit (though this can be interrupted by
"KeyboardInterrupt") and running the "atexit" functions, the runtime
is marked as finalizing, meaning that "Py_IsFinalizing()" and
"sys.is_finalizing()" return true.  At this point, only the
finalization thread (the thread that initiated finalization; this is
typically the main thread) is allowed to *attach* a thread state.

Other threads that attempt to attach during finalization, either
explicitly (such as via "PyThreadState_Ensure()" or
"Py_END_ALLOW_THREADS") or implicitly (such as in-between bytecode
instructions), will enter a **permanently blocked state**. Generally,
this is harmless, but this can result in deadlocks. For example, a
thread may be permanently blocked while holding a lock, meaning that
the finalization thread can never acquire that lock.

Prior to CPython 3.13, the thread would exit instead of hanging, which
led to other issues (see the warning note at
"PyThread_exit_thread()").

Gross? Yes. Starting in Python 3.15, there are a number of C APIs that
make it possible to avoid these issues by temporarily preventing
finalization:

Ver também:

  **PEP 788** explains the design, motivation and rationale for these
  APIs.

type PyInterpreterGuard
    * Parte da ABI Estável (como uma estrutura opaca) desde a versão
   3.15.*

   An opaque interpreter guard structure.

   By holding an interpreter guard, the caller can ensure that the
   interpreter will not finalize until the guard is closed (through
   "PyInterpreterGuard_Close()").

   When a guard is held, a thread attempting to finalize the
   interpreter will block until the guard is closed before starting
   finalization. After finalization has started, threads are forever
   unable to acquire guards for that interpreter. This means that if
   you forget to close an interpreter guard, the process will
   **permanently hang** during finalization!

   Holding a guard for an interpreter is similar to holding a *strong
   reference* to a Python object, except finalization does not happen
   automatically after all guards are released: it requires an
   explicit "Py_EndInterpreter()" call.

   Adicionado na versão 3.15.

PyInterpreterGuard *PyInterpreterGuard_FromCurrent(void)
    * Parte da ABI Estável desde a versão 3.15.*

   Create a finalization guard for the current interpreter. This will
   prevent finalization until the guard is closed.

   Por exemplo:

      // Temporarily prevent finalization.
      PyInterpreterGuard *guard = PyInterpreterGuard_FromCurrent();
      if (guard == NULL) {
         // Finalization has already started or we're out of memory.
         return NULL;
      }

      Py_BEGIN_ALLOW_THREADS;
      // Do some critical processing here. For example, we can safely acquire
      // locks that might be acquired by the finalization thread.
      Py_END_ALLOW_THREADS;

      // Now that we're done with our critical processing, the interpreter is
      // allowed to finalize again.
      PyInterpreterGuard_Close(guard);

   On success, this function returns a guard for the current
   interpreter; on failure, it returns "NULL" with an exception set.

   This function will fail only if the current interpreter has already
   started finalizing, or if the process is out of memory.

   The guard pointer returned by this function must be eventually
   closed with "PyInterpreterGuard_Close()"; failing to do so will
   result in the Python process infinitely hanging.

   The caller must hold an *attached thread state*.

   Adicionado na versão 3.15.

PyInterpreterGuard *PyInterpreterGuard_FromView(PyInterpreterView *view)
    * Parte da ABI Estável desde a versão 3.15.*

   Create a finalization guard for an interpreter through a view.

   On success, this function returns a guard to the interpreter
   represented by *view*. The view is still valid after calling this
   function. The guard must eventually be closed with
   "PyInterpreterGuard_Close()".

   If the interpreter no longer exists, is already finalizing, or out
   of memory, then this function returns "NULL" without setting an
   exception.

   The caller does not need to hold an *attached thread state*.

   Adicionado na versão 3.15.

void PyInterpreterGuard_Close(PyInterpreterGuard *guard)
    * Parte da ABI Estável desde a versão 3.15.*

   Close an interpreter guard, allowing the interpreter to start
   finalization if no other guards remain. If an interpreter guard is
   never closed, the interpreter will infinitely wait when trying to
   enter finalization!

   After an interpreter guard is closed, it may not be used in
   "PyThreadState_Ensure()". Doing so will result in undefined
   behavior.

   This function cannot fail, and the caller doesn't need to hold an
   *attached thread state*.

   Adicionado na versão 3.15.


Interpreter views
=================

In some cases, it may be necessary to access an interpreter that may
have been deleted. This can be done using interpreter views.

type PyInterpreterView
    * Parte da ABI Estável (como uma estrutura opaca) desde a versão
   3.15.*

   An opaque view of an interpreter.

   This is a thread-safe way to access an interpreter that may be
   finalizing or already destroyed.

   Adicionado na versão 3.15.

PyInterpreterView *PyInterpreterView_FromCurrent(void)
    * Parte da ABI Estável desde a versão 3.15.*

   Create a view to the current interpreter.

   This function is generally meant to be used alongside
   "PyInterpreterGuard_FromView()" or
   "PyThreadState_EnsureFromView()".

   On success, this function returns a view to the current
   interpreter; on failure, it returns "NULL" with an exception set.

   The caller must hold an *attached thread state*.

   Adicionado na versão 3.15.

void PyInterpreterView_Close(PyInterpreterView *view)
    * Parte da ABI Estável desde a versão 3.15.*

   Close an interpreter view.

   If an interpreter view is never closed, the view's memory will
   never be freed, but there are no other consequences. (In contrast,
   forgetting to close a guard will infinitely hang the main thread
   during finalization.)

   This function cannot fail, and the caller doesn't need to hold an
   *attached thread state*.

   Adicionado na versão 3.15.

PyInterpreterView *PyInterpreterView_FromMain(void)
    * Parte da ABI Estável desde a versão 3.15.*

   Create a view for the main interpreter (the first and default
   interpreter in a Python process; see "PyInterpreterState_Main()").

   On success, this function returns a view to the main interpreter;
   on failure, it returns "NULL" without an exception set. Failure
   indicates that the process is out of memory.

   Use this function when an interpreter pointer or view cannot be
   supplied by the caller, such as when a native threading library
   does not provide a "void *arg" parameter that could carry a
   "PyInterpreterGuard" or "PyInterpreterView". In code that supports
   subinterpreters, prefer "PyInterpreterView_FromCurrent()" so the
   guard tracks the calling interpreter rather than the main one.

   The caller does not need to hold an *attached thread state*.

   Adicionado na versão 3.15.


Parâmetros de todo o processo
=============================

void Py_SetProgramName(const wchar_t *name)
    * Parte da ABI Estável.*

   Esta API é mantida para compatibilidade com versões anteriores: em
   vez disso, deve-se usar a configuração "PyConfig.program_name",
   consulte Configuração de inicialização do Python.

   This function should be called before "Py_Initialize()" is called
   for the first time, if it is called at all.  It tells the
   interpreter the value of the "argv[0]" argument to the "main()"
   function of the program (converted to wide characters). This is
   used by some other functions below to find the Python run-time
   libraries relative to the interpreter executable.  The default
   value is "'python'".  The argument should point to a zero-
   terminated wide character string in static storage whose contents
   will not change for the duration of the program's execution.  No
   code in the Python interpreter will change the contents of this
   storage.

   Use "Py_DecodeLocale()" para decodificar uma string de bytes e
   obter uma string wchar_t*.

   Descontinuado desde a versão 3.11, removido na versão 3.15.

const char *Py_GetVersion()
    * Parte da ABI Estável.*

   Retorna a verão deste interpretador Python. Esta é uma string que
   se parece com

      "3.0a5+ (py3k:63103M, May 12 2008, 00:53:55) \n[GCC 4.2.3]"

   A primeira palavra (até o primeiro espaço em branco) representa a
   versão atual do Python; os primeiros caracteres indicam a versão
   principal e a versão secundária, separados por um ponto. A string
   retornada aponta para um armazenamento estático; o chamador não
   deve modificar seu valor. O valor fica disponível para o código
   Python como "sys.version".

   Veja também a constante "Py_Version".

const char *Py_GetPlatform()
    * Parte da ABI Estável.*

   Retorna o identificador da plataforma atual. No Unix, este
   identificador é formado pelo nome "oficial" do sistema operacional,
   convertido para minúsculas, seguido pelo número da revisão
   principal; por exemplo, para Solaris 2.x, também conhecido como
   SunOS 5.x, o valor é "'sunos5'". No macOS, é "'darwin'". No
   Windows, é "'win'". A string retornada aponta para um armazenamento
   estático; o chamador não deve modificar seu valor. O valor está
   disponível para o código Python como "sys.platform".

const char *Py_GetCopyright()
    * Parte da ABI Estável.*

   Retorna a string oficial de direitos autoriais para a versão atual
   do Python, por exemplo

   "'Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam'"

   A string retornada aponta para o armazenamento estático; o chamador
   não deve modificar o seu valor. O valor está disponível para o
   código Python como "sys.copyright".

const char *Py_GetCompiler()
    * Parte da ABI Estável.*

   Retorna uma indicação do compilador usado para construir a atual
   versão do Python, em colchetes, por exemplo:

      "[GCC 2.7.2.2]"

   A string retornada aponta para o armazenamento estático; o chamador
   não deve modificar o seu valor. O valor está disponível para o
   código Python como "sys.version".

const char *Py_GetBuildInfo()
    * Parte da ABI Estável.*

   Return information about the sequence number and build date and
   time of the current Python interpreter instance, for example

      "#67, Aug  1 1997, 22:34:28"

   A string retornada aponta para o armazenamento estático; o chamador
   não deve modificar o seu valor. O valor está disponível para o
   código Python como "sys.version".

void PySys_SetArgvEx(int argc, wchar_t **argv, int updatepath)
    * Parte da ABI Estável.*

   Esta API é mantida para compatibilidade com versões anteriores: em
   vez disso, deve-se usar a configuração "PyConfig.argv",
   "PyConfig.parse_argv" e "PyConfig.safe_path", consulte Configuração
   de inicialização do Python.

   Define "sys.argv" com base em *argc* e *argv*. Esses parâmetros são
   semelhantes aos passados para a função "main()" do programa, com a
   diferença de que a primeira entrada deve se referir ao arquivo de
   script a ser executado, em vez do executável que hospeda o
   interpretador Python. Se não houver um script a ser executado, a
   primeira entrada em *argv* pode ser uma string vazia. Se esta
   função falhar ao inicializar "sys.argv", uma condição fatal será
   sinalizada usando "Py_FatalError()".

   Se *updatepath* é zero, isto é tudo o que a função faz. Se
   *updatepath* não é zero, a função também modifica "sys.path" de
   acordo com o seguinte algoritmo:

   * Se o nome de um script existente for passado em "argv[0]", o
     caminho absoluto do diretório onde o script está localizado será
     adicionado a "sys.path".

   * Caso contrário (isto é, se *argc* for "0" ou "argv[0]" não
     apontar para um nome de arquivo existente), uma string vazia é
     adicionada ao início de "sys.path", o que é o mesmo que adicionar
     o diretório de trabalho atual (""."").

   Use "Py_DecodeLocale()" para decodificar uma string de bytes e
   obter uma string wchar_t*.

   Veja também os membros "PyConfig.orig_argv" e "PyConfig.argv" da
   Configuração de inicialização do Python.

   Nota:

     Recomenda-se que aplicações que incorporam o interpretador Python
     para fins que não sejam a execução de um único script passem "0"
     como *updatepath*, e atualizem "sys.path" por conta própria, se
     desejarem. Veja **CVE 2008-5983**.Em versões anteriores à 3.1.3,
     você pode obter o mesmo efeito removendo manualmente o primeiro
     elemento de "sys.path" após ter chamado "PySys_SetArgv()", por
     exemplo, usando:

        PyRun_SimpleString("import sys; sys.path.pop(0)\n");

   Adicionado na versão 3.1.3.

   Descontinuado desde a versão 3.11, removido na versão 3.15.

void PySys_SetArgv(int argc, wchar_t **argv)
    * Parte da ABI Estável.*

   Esta API é mantida para retrocompatibilidade: em vez disso, devem
   ser usadas as configurações "PyConfig.argv" e
   "PyConfig.parse_argv", consulte a Configuração de inicialização do
   Python.

   Esta função funciona como "PySys_SetArgvEx()" com *updatepath*
   definido como "1" a menos que o interpretador **python** tenha sido
   iniciado com a "-I".

   Use "Py_DecodeLocale()" para decodificar uma string de bytes e
   obter uma string wchar_t*.

   Veja também os membros "PyConfig.orig_argv" e "PyConfig.argv" da
   Configuração de inicialização do Python.

   Alterado na versão 3.4: O valor *updatepath* depende de "-I".

   Descontinuado desde a versão 3.11, removido na versão 3.15.

void Py_SetPythonHome(const wchar_t *home)
    * Parte da ABI Estável.*

   Esta API é mantida para retrocompatibilidade: em vez disso, deve-se
   usar a configuração "PyConfig.home", consulte a Configuração de
   inicialização do Python.

   Define o diretório pessoal ("home") padrão, ou seja, o local das
   bibliotecas padrão do Python. Consulte "PYTHONHOME" para obter o
   significado da string do argumento.

   O argumento deve apontar para uma string terminada em zero em um
   armazenamento estático, cujo conteúdo não será alterado durante a
   execução do programa. Nenhum código no interpretador Python
   alterará o conteúdo desse armazenamento.

   Use "Py_DecodeLocale()" para decodificar uma string de bytes e
   obter uma string wchar_t*.

   Descontinuado desde a versão 3.11, removido na versão 3.15.
