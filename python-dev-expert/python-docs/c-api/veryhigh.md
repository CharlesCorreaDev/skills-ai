A camada de nível muito alto
****************************

As funções neste capítulo permitirão que você execute um código-fonte
Python fornecido em um arquivo ou buffer, mas não permitirão que você
interaja de forma mais detalhada com o interpretador.

Várias dessas funções aceitam um símbolo de início da gramática como
parâmetro. Os símbolos de início disponíveis são "Py_eval_input",
"Py_file_input" e "Py_single_input" e "Py_func_type_input". Eles são
descritos seguindo as funções que os aceitam como parâmetros.

Note também que várias dessas funções aceitam parâmetros FILE*. Um
problema específico que precisa ser tratado com cuidado é que a
estrutura "FILE" para diferentes bibliotecas C pode ser diferente e
incompatível. No Windows (pelo menos), é possível que extensões
vinculadas dinamicamente usem bibliotecas diferentes, então deve-se
tomar cuidado para que os parâmetros FILE* sejam passados para essas
funções somente se for certo que elas foram criadas pela mesma
biblioteca que o tempo de execução do Python está usando.

int PyRun_AnyFile(FILE *fp, const char *filename)

   Esta é uma interface simplificada para "PyRun_AnyFileExFlags()"
   abaixo, deixando *closeit* definido como "0" e *flags* definido
   como "NULL".

int PyRun_AnyFileFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

   Esta é uma interface simplificada para "PyRun_AnyFileExFlags()"
   abaixo, deixando o argumento *closeit* definido como "0".

int PyRun_AnyFileEx(FILE *fp, const char *filename, int closeit)

   Esta é uma interface simplificada para "PyRun_AnyFileExFlags()"
   abaixo, deixando o argumento *flags* definido como "NULL".

int PyRun_AnyFileExFlags(FILE *fp, const char *filename, int closeit, PyCompilerFlags *flags)

   Se *fp* se referir a um arquivo associado a um dispositivo
   interativo (entrada de console ou terminal ou pseudo-terminal
   Unix), retorna o valor de "PyRun_InteractiveLoop()", caso
   contrário, retorna o resultado de "PyRun_SimpleFile()". *filename*
   é decodificado da codificação do sistema de arquivos
   ("sys.getfilesystemencoding()"). Se *filename* for "NULL", esta
   função usa ""???"" como o nome do arquivo. Se *closeit* for
   verdadeiro, o arquivo será fechado antes de
   "PyRun_SimpleFileExFlags()" retornar.

int PyRun_SimpleString(const char *command)

   Esta é uma interface simplificada para "PyRun_SimpleStringFlags()"
   abaixo, deixando o argumento "PyCompilerFlags"* definido como
   "NULL".

int PyRun_SimpleStringFlags(const char *command, PyCompilerFlags *flags)

   Executa o código-fonte Python de *command* no módulo "__main__" de
   acordo com o argumento *flags*. Se "__main__" ainda não existir,
   ele será criado. Retorna "0" em caso de sucesso ou "-1" se uma
   exceção foi gerada. Se houve um erro, não há como obter as
   informações da exceção. Para o significado de *flags*, veja abaixo.

   Observe que se uma exceção "SystemExit" não tratada for levantada,
   esta função não retornará "-1", mas sairá do processo, desde que
   "PyConfig.inspect" seja zero.

int PyRun_SimpleFile(FILE *fp, const char *filename)

   Esta é uma interface simplificada para "PyRun_SimpleFileExFlags()"
   abaixo, deixando *closeit* definido como "0" e *flags* definido
   como "NULL".

int PyRun_SimpleFileEx(FILE *fp, const char *filename, int closeit)

   Esta é uma interface simplificada para "PyRun_SimpleFileExFlags()"
   abaixo, deixando o *flags* definido como "NULL".

int PyRun_SimpleFileExFlags(FILE *fp, const char *filename, int closeit, PyCompilerFlags *flags)

   Semelhante a "PyRun_SimpleStringFlags()", mas o código-fonte Python
   é lido de *fp* em vez de uma string na memória. *filename* deve ser
   o nome do arquivo, ele é decodificado a partir do *tratador de
   erros e codificação do sistema de arquivos*. Se *closeit* for true,
   o arquivo será fechado antes que "PyRun_SimpleFileExFlags()"
   retorne.

   Nota:

     No Windows, *fp* deve ser aberto como modo binário (por exemplo,
     "fopen(filename, "rb")"). Caso contrário, o Python pode não
     manipular corretamente o arquivo de script com final de linha LF.

int PyRun_InteractiveOneObject(FILE *fp, PyObject *filename, PyCompilerFlags *flags)

   Lê e executa uma única instrução de um arquivo associado a um
   dispositivo interativo de acordo com o argumento *flags*. O usuário
   será solicitado usando "sys.ps1" e "sys.ps2". *filename* deve ser
   um objeto "str" Python.

   Retorna "0" quando a entrada foi executada com sucesso, "-1" se
   houve uma exceção ou um código de erro do arquivo de inclusão
   "errcode.h" distribuído como parte do Python se houve um erro de
   análise. (Observe que "errcode.h" não é incluído por "Python.h",
   então deve ser incluído especificamente se necessário.)

int PyRun_InteractiveOne(FILE *fp, const char *filename)

   Esta é uma interface simplificada para
   "PyRun_InteractiveOneFlags()" abaixo, deixando *flags* definido
   como "NULL".

int PyRun_InteractiveOneFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

   Semelhante a "PyRun_InteractiveOneObject()", mas *filename* é um
   const char*, que é decodificado a partir do *tratador de erros e
   codificação do sistema de arquivos*.

int PyRun_InteractiveLoop(FILE *fp, const char *filename)

   Esta é uma interface simplificada para
   "PyRun_InteractiveLoopFlags()" abaixo, deixando *flags* definido
   como "NULL".

int PyRun_InteractiveLoopFlags(FILE *fp, const char *filename, PyCompilerFlags *flags)

   Lê e executa instruções de um arquivo associado a um dispositivo
   interativo até que o EOF seja atingido. O usuário será consultado
   usando "sys.ps1" e "sys.ps2". *filename* é decodificado a partir do
   *tratador de erros e codificação do sistema de arquivos*. Retorna
   "0" no EOF ou um número negativo em caso de falha.

int (*PyOS_InputHook)(void)
    * Parte da ABI Estável.*

   Pode ser definido para apontar para uma função com o protótipo "int
   func(void)". A função será chamada quando o prompt do interpretador
   do Python estiver prestes a ficar ocioso e aguardar a entrada do
   usuário no terminal. O valor de retorno é ignorado. A substituição
   deste hook pode ser usada para integrar o prompt do interpretador
   com outros laços de eventos, como feito em "Modules/_tkinter.c" no
   código-fonte do Python.

   The function is called without an *attached thread state*.

   Alterado na versão 3.12: Esta função só é chamada pelo
   interpretador principal.

char *(*PyOS_ReadlineFunctionPointer)(FILE*, FILE*, const char*)

   Can be set to point to a function with the prototype "char
   *func(FILE *stdin, FILE *stdout, const char *prompt)", overriding
   the default function used to read a single line of input at the
   interpreter's prompt.  The function is expected to output the
   string *prompt* if it's not "NULL", and then read a line of input
   from the provided standard input file, returning the resulting
   string.  For example, the "readline" module sets this hook to
   provide line-editing and tab-completion features.

   The function is called without an *attached thread state*.

   If this pointer is "NULL", "PyOS_Readline()" sets it to the default
   implementation, "PyOS_Readline()", before reading input.

   The returned string must be null-terminated and include the
   trailing newline, if one was read. Return an empty string if the
   end of the file is reached before any characters are read. Return
   "NULL" on failure or interruption; a Python exception may be set.

   A non-"NULL" result must be a string allocated by
   "PyMem_RawMalloc()" or "PyMem_RawRealloc()".

   Alterado na versão 3.4: O resultado deve ser alocado por
   "PyMem_RawMalloc()" ou "PyMem_RawRealloc()", em vez de ser alocado
   por "PyMem_Malloc()" ou "PyMem_Realloc()".

   Alterado na versão 3.12: Esta função só é chamada pelo
   interpretador principal.

char *PyOS_Readline(FILE *sys_stdin, FILE *sys_stdout, const char *prompt)

   Display *prompt*, if it is not "NULL", and read a line from
   *sys_stdin*. If both streams are terminals and the call is made
   from the main interpreter, use "PyOS_ReadlineFunctionPointer".
   Otherwise, use the default implementation, which flushes
   *sys_stdout* and writes *prompt* to the C standard error stream.

   The returned string follows the contract of
   "PyOS_ReadlineFunctionPointer", but the caller must free it with
   "PyMem_Free()". Return "NULL" on failure or interruption; a Python
   exception may be set.

PyObject *PyRun_String(const char *str, int start, PyObject *globals, PyObject *locals)
    *Retorna valor: Nova referência.*

   Esta é uma interface simplificada para "PyRun_StringFlags()"
   abaixo, deixando *flags* definido como "NULL".

PyObject *PyRun_StringFlags(const char *str, int start, PyObject *globals, PyObject *locals, PyCompilerFlags *flags)
    *Retorna valor: Nova referência.*

   Execute Python source code from *str* in the context specified by
   the objects *globals* and *locals* with the compiler flags
   specified by *flags*.  *globals* must be a dictionary; *locals* can
   be any object that implements the mapping protocol.  The parameter
   *start* specifies the start symbol and must be one of the available
   start symbols.

   Retorna o resultado da execução do código como um objeto Python, ou
   "NULL" se uma exceção foi levantada.

PyObject *PyRun_File(FILE *fp, const char *filename, int start, PyObject *globals, PyObject *locals)
    *Retorna valor: Nova referência.*

   Esta é uma interface simplificada para "PyRun_FileExFlags()"
   abaixo, deixando *closeit* definido como "0" e *flags* definido
   como "NULL".

PyObject *PyRun_FileEx(FILE *fp, const char *filename, int start, PyObject *globals, PyObject *locals, int closeit)
    *Retorna valor: Nova referência.*

   Esta é uma interface simplificada para "PyRun_FileExFlags()"
   abaixo, deixando *flags* definido como "NULL".

PyObject *PyRun_FileFlags(FILE *fp, const char *filename, int start, PyObject *globals, PyObject *locals, PyCompilerFlags *flags)
    *Retorna valor: Nova referência.*

   Esta é uma interface simplificada para "PyRun_FileExFlags()"
   abaixo, deixando *closeit* definido como "0".

PyObject *PyRun_FileExFlags(FILE *fp, const char *filename, int start, PyObject *globals, PyObject *locals, int closeit, PyCompilerFlags *flags)
    *Retorna valor: Nova referência.*

   Semelhante a "PyRun_StringFlags()", mas o código-fonte Python é
   lido de *fp* em vez de uma string na memória. *filename* deve ser o
   nome do arquivo, ele é decodificado a partir do *tratador de erros
   e codificação do sistema de arquivos*. Se *closeit* for true, o
   arquivo será fechado antes que "PyRun_FileExFlags()" retorne.

PyObject *Py_CompileString(const char *str, const char *filename, int start)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Esta é uma interface simplificada para "Py_CompileStringFlags()"
   abaixo, deixando *flags* definido como "NULL".

PyObject *Py_CompileStringFlags(const char *str, const char *filename, int start, PyCompilerFlags *flags)
    *Retorna valor: Nova referência.*

   Esta é uma interface simplificada para "Py_CompileStringExFlags()"
   abaixo, com *optimize* definido como "-1".

PyObject *Py_CompileStringObject(const char *str, PyObject *filename, int start, PyCompilerFlags *flags, int optimize)
    *Retorna valor: Nova referência.*

   Analisa e compila o código-fonte Python em *str*, retornando o
   objeto de código resultante. O símbolo inicial é fornecido por
   *start*; isso pode ser usado para restringir o código que pode ser
   compilado e deve ser símbolos iniciais disponíveis. O nome do
   arquivo especificado por *filename* é usado para construir o objeto
   de código e pode aparecer em tracebacks ou mensagens de exceção
   "SyntaxError". Isso retorna "NULL" se o código não puder ser
   analisado ou compilado.

   O inteiro *optimize* especifica o nível de otimização do
   compilador; um valor de "-1" seleciona o nível de otimização do
   interpretador dado pela opção "-O". Níveis explícitos são "0"
   (nenhuma otimização; "__debug__" é verdadeiro), "1" (instruções
   "assert" são removidas, "__debug__" é falso) ou "2" (strings de
   documentação também são removidas).

   Adicionado na versão 3.4.

PyObject *Py_CompileStringExFlags(const char *str, const char *filename, int start, PyCompilerFlags *flags, int optimize)
    *Retorna valor: Nova referência.*

   Como "Py_CompileStringObject()", mas *filename* é uma string de
   bytes decodificada a partir do *tratador de erros e codificação do
   sistema de arquivos*.

   Adicionado na versão 3.2.

PyObject *PyEval_EvalCode(PyObject *co, PyObject *globals, PyObject *locals)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Esta é uma interface simplificada para "PyEval_EvalCodeEx()", com
   apenas o objeto código e variáveis locais e globais. Os outros
   argumentos são definidos como "NULL".

PyObject *PyEval_EvalCodeEx(PyObject *co, PyObject *globals, PyObject *locals, PyObject *const *args, int argcount, PyObject *const *kws, int kwcount, PyObject *const *defs, int defcount, PyObject *kwdefs, PyObject *closure)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Avalia um objeto código pré-compilado, dado um ambiente particular
   para sua avaliação. Este ambiente consiste em um dicionário de
   variáveis globais, um objeto mapeamento de variáveis locais,
   vetores de argumentos, nomeados e padrões, um dicionário de valores
   padrões para argumentos somente-nomeados e uma tupla de clausura de
   células.

PyObject *PyEval_EvalFrame(PyFrameObject *f)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Avalia um quadro de execução. Esta é uma interface simplificada
   para "PyEval_EvalFrameEx()", para retrocompatibilidade.

PyObject *PyEval_EvalFrameEx(PyFrameObject *f, int throwflag)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Esta é a função principal e sem retoques da interpretação Python. O
   objeto código associado ao quadro de execução *f* é executado,
   interpretando bytecode e executando chamadas conforme necessário. O
   parâmetro adicional *throwflag* pode ser ignorado na maioria das
   vezes - se verdadeiro, ele faz com que uma exceção seja levantada
   imediatamente; isso é usado para os métodos "throw()" de objetos
   geradores.

   Alterado na versão 3.4: Essa função agora inclui uma asserção de
   depuração para ajudar a garantir que ela não descarte
   silenciosamente uma exceção ativa.

int PyEval_MergeCompilerFlags(PyCompilerFlags *cf)

   Esta função altera os sinalizadores do quadro de avaliação atual e
   retorna verdadeiro em caso de sucesso e falso em caso de falha.

struct PyCompilerFlags

   Esta é a estrutura usada para manter os sinalizadores do
   compilador. Em casos onde o código está apenas sendo compilado, ele
   é passado como "int flags", e em casos onde o código está sendo
   executado, ele é passado como "PyCompilerFlags *flags". Neste caso,
   "from __future__ import" pode modificar *flags*.

   Sempre que "PyCompilerFlags *flags" for "NULL", "cf_flags" é
   tratado como igual a "0", e qualquer modificação devido a "from
   __future__ import" é descartada.

   int cf_flags

      Sinalizadores do compilador.

   int cf_feature_version

      *cf_feature_version* é a versão secundária do Python. Deve ser
      inicializada como "PY_MINOR_VERSION".

      O campo é ignorado por padrão, ele é usado se e somente se o
      sinalizador "PyCF_ONLY_AST" estiver definido em "cf_flags".

   Alterado na versão 3.8: Adicionado campo *cf_feature_version*.

   Os sinalizadores do compilador disponíveis são acessíveis como
   macros:

   PyCF_ALLOW_TOP_LEVEL_AWAIT
   PyCF_ONLY_AST
   PyCF_OPTIMIZED_AST
   PyCF_TYPE_COMMENTS

      Veja sinalizadores do compilador na documentação do módulo
      Python "ast", que exporta essas constantes com os mesmos nomes.

   -[ Low-level flags ]-

   The following flags and masks serve narrow needs of the standard
   library and interactive interpreters.  Code outside the standard
   library rarely has a reason to use them.  They are considered
   implementation details and may change at any time.

   PyCF_ALLOW_INCOMPLETE_INPUT

      This flag is a private interface between the compiler and the
      "codeop" module.  Do not use it; its behavior is unsupported and
      may change without warning.

      With this flag set, when compilation fails because the source
      text ends where more input is expected, for example in the
      middle of an indented block or an unterminated string literal,
      the error raised is the undocumented "_IncompleteInputError", a
      subclass of "SyntaxError".  The "codeop" module sets this flag,
      together with "PyCF_DONT_IMPLY_DEDENT", to tell input that is
      incomplete apart from input with a real syntax error, so that
      interactive interpreters know when to prompt for another line
      instead of reporting an error.

      Adicionado na versão 3.11.

   PyCF_DONT_IMPLY_DEDENT

      By default, when compiling with the "Py_single_input" start
      symbol, reaching the end of the source text implicitly closes
      any open indented blocks.  With this flag set, open blocks are
      only closed if the last line of the source ends with a newline;
      otherwise, compilation fails with a "SyntaxError":

         PyCompilerFlags flags = {
             .cf_flags = 0,
             .cf_feature_version = PY_MINOR_VERSION,
         };
         const char *source = "if a:\n    pass";

         /* The "if" block is closed implicitly;
            this returns a code object: */
         Py_CompileStringFlags(source, "<input>", Py_single_input, &flags);

         /* With the flag, this fails with a SyntaxError,
            because the last line does not end with a newline: */
         flags.cf_flags = PyCF_DONT_IMPLY_DEDENT;
         Py_CompileStringFlags(source, "<input>", Py_single_input, &flags);

      The "codeop" module uses this flag to detect incomplete
      interactive input.  While the user is still typing inside an
      indented block, the source does not yet end with a newline, so
      it fails to compile and the user is prompted for another line.

   PyCF_IGNORE_COOKIE

      Read the source text as UTF-8, ignoring its **PEP 263** encoding
      declaration ("coding cookie"), if any:

         PyCompilerFlags flags = {
             .cf_flags = 0,
             .cf_feature_version = PY_MINOR_VERSION,
         };
         const char *source = "# coding: latin-1\ns = '\xe9'\n";

         /* The coding cookie is honored: byte 0xE9 is decoded as
            Latin-1, and this returns a code object that sets s to "é": */
         Py_CompileStringFlags(source, "<input>", Py_file_input, &flags);

         /* With the flag, the cookie is ignored and compilation fails
            with a SyntaxError, because 0xE9 is not valid UTF-8: */
         flags.cf_flags = PyCF_IGNORE_COOKIE;
         Py_CompileStringFlags(source, "<input>", Py_file_input, &flags);

      The "compile()", "eval()" and "exec()" built-in functions set
      this flag when the source is a "str" object, because they pass
      the text to the parser encoded as UTF-8.

   PyCF_SOURCE_IS_UTF8

      Mark the source text as known to be UTF-8 encoded. The
      "compile()", "eval()" and "exec()" built-in functions set this
      flag, but it currently has no effect.

   Os sinalizadores ""PyCF"" acima podem ser combinados com
   sinalizadores ""CO_FUTURE"", como "CO_FUTURE_ANNOTATIONS", para
   habilitar recursos normalmente selecionáveis usando instruções
   future. Consulte Sinalizadores de objetos código para obter uma
   lista completa.

   The following masks combine several flags:

   PyCF_MASK

      Bitmask of all "CO_FUTURE" flags (see Sinalizadores de objetos
      código), which select features normally enabled by future
      statements. When code compiled with a "PyCompilerFlags *flags"
      argument contains a "from __future__ import" statement, the flag
      for the imported feature is added to *flags*, so that code
      executed later in the same context inherits it.

   PyCF_MASK_OBSOLETE

      Do not use this mask in new code.  It is kept only so that old
      code passing its flags to "compile()" keeps working.

      Bitmask of flags for obsolete future features that no longer
      have any effect.

   PyCF_COMPILE_MASK

      Bitmask of all "PyCF" flags that change how the source is
      compiled, such as "PyCF_ONLY_AST". The "compile()" built-in
      function uses this mask to validate its *flags* argument.


Símbolos iniciais disponíveis
=============================

int Py_eval_input

   O símbolo inicial da gramática Python para expressões isoladas;
   para uso com "Py_CompileString()".

int Py_file_input

   O símbolo de início da gramática Python para sequências de
   instruções conforme lidas de um arquivo ou outra fonte; para uso
   com "Py_CompileString()". Este é o símbolo a ser usado ao compilar
   código-fonte Python arbitrariamente longo.

int Py_single_input

   O símbolo de início da gramática Python para uma única declaração;
   para uso com "Py_CompileString()". Este é o símbolo usado para o
   laço do interpretador interativo.

int Py_func_type_input

   O símbolo inicial da gramática Python para um tipo de função; para
   uso com "Py_CompileString()". É usado para analisar "comentários de
   tipo de assinatura" de **PEP 484**.

   Isso requer que o sinalizador "PyCF_ONLY_AST" seja definido.

   Ver também:

     * "ast.FunctionType"

     * **PEP 484**

   Adicionado na versão 3.8.


Stack Effects
=============

Ver também: "dis.stack_effect()"

PY_INVALID_STACK_EFFECT

   Sentinel value representing an invalid stack effect.

   This is currently equivalent to "INT_MAX".

   Adicionado na versão 3.8.

int PyCompile_OpcodeStackEffect(int opcode, int oparg)

   Calcula o efeito que o *opcode* com argumento *oparg* tem na pilha.

   On success, this function returns the stack effect; on failure,
   this returns "PY_INVALID_STACK_EFFECT".

   Adicionado na versão 3.4.

int PyCompile_OpcodeStackEffectWithJump(int opcode, int oparg, int jump)

   Similar to "PyCompile_OpcodeStackEffect()", but don't include the
   stack effect of jumping if *jump* is zero.

   If *jump* is "0", this will not include the stack effect of
   jumping, but if *jump* is "1" or "-1", this will include it.

   On success, this function returns the stack effect; on failure,
   this returns "PY_INVALID_STACK_EFFECT".

   Adicionado na versão 3.8.
