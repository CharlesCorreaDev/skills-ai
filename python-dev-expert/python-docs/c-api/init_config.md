Configuração de inicialização do Python
***************************************


API C PyInitConfig
==================

Adicionado na versão 3.14.

O Python pode ser inicializado com "Py_InitializeFromInitConfig()".

A função "Py_RunMain()" pode ser usada para escrever um programa
Python personalizado.

Veja também Inicialização, Finalização e Threads.

Ver também: **PEP 741** "API C de configuração do Python".


Exemplo
-------

Exemplo de Python personalizado sempre em execução com o Modo de
Desenvolvimento Python ativado; retorna "-1" em caso de erro:

   int init_python(void)
   {
       PyInitConfig *config = PyInitConfig_Create();
       if (config == NULL) {
           printf("PYTHON INIT ERROR: memory allocation failed\n");
           return -1;
       }

       // Habilita o Modo de Desenvolvimento do Python
       if (PyInitConfig_SetInt(config, "dev_mode", 1) < 0) {
           goto error;
       }

       // Inicializa o Python com a configuração
       if (Py_InitializeFromInitConfig(config) < 0) {
           goto error;
       }
       PyInitConfig_Free(config);
       return 0;

   error:
       {
           // Exibe a mensagem de erro.
           //
           // Esse estilo incomum de chaves é usado porque você não
           // fazer alvos goto apontarem para declarações de variáveis.
           const char *err_msg;
           (void)PyInitConfig_GetError(config, &err_msg);
           printf("PYTHON INIT ERROR: %s\n", err_msg);
           PyInitConfig_Free(config);
           return -1;
       }
   }


Criar configuração
------------------

struct PyInitConfig

   Estrutura opaca para configurar a inicialização do Python.

PyInitConfig *PyInitConfig_Create(void)

   Cria uma nova configuração de inicialização usando os valores
   padrão de configuração isolada.

   Deve ser liberada por "PyInitConfig_Free()".

   Retorna "NULL" em caso de falha na alocação de memória.

void PyInitConfig_Free(PyInitConfig *config)

   Libera a memória da configuração de inicialização *config*.

   Se *config* for "NULL", nenhuma operação será realizada.


Tratamento de erros
-------------------

int PyInitConfig_GetError(PyInitConfig *config, const char **err_msg)

   Obtém a mensagem de erro *config*.

   * Define **err_msg* e retorna "1" se um erro for definido.

   * Define **err_msg* como "NULL" e retorna "0" caso contrário.

   Uma mensagem de erro é uma string codificada em UTF-8.

   Se *config* tiver um código de saída, formata o código de saída
   como uma mensagem de erro.

   A mensagem de erro permanece válida até que outra função
   "PyInitConfig" seja chamada com *config*. O chamador não precisa
   liberar a mensagem de erro.

int PyInitConfig_GetExitCode(PyInitConfig *config, int *exitcode)

   Obtém o código de saída *config*.

   * Define **exitcode* e retorna "1" se *config* tiver um código de
     saída definido.

   * Retorna "0" se *config* não tiver nenhum código de saída
     definido.

   Somente a função "Py_InitializeFromInitConfig()" pode definir um
   código de saída se a opção "parse_argv" for diferente de zero.

   Um código de saída pode ser definido quando a análise da linha de
   comando falhar (código de saída "2") ou quando uma opção da linha
   de comando solicitar a exibição da ajuda da linha de comando
   (código de saída "0").


Opções de get
-------------

O parâmetro *name* da opção de configuração deve ser uma string
codificada em UTF-8 terminada em nulo e não nula. Consulte as opções
de configuração.

int PyInitConfig_HasOption(PyInitConfig *config, const char *name)

   Verifica se a configuração possui uma opção chamada *name*.

   Retorna "1" se a opção existir, ou retorna "0" caso contrário.

int PyInitConfig_GetInt(PyInitConfig *config, const char *name, int64_t *value)

   Obtém uma opção de configuração de número inteiro.

   * Define **value* e retorna "0" em caso de sucesso.

   * Define um erro em *config* e retorna "-1" em caso de erro.

int PyInitConfig_GetStr(PyInitConfig *config, const char *name, char **value)

   Obtém uma opção de configuração de string como uma string
   codificada em UTF-8 terminada em nulo.

   * Define **value* e retorna "0" em caso de sucesso.

   * Define um erro em *config* e retorna "-1" em caso de erro.

   **value* pode ser definido como "NULL" se a opção for uma string
   opcional e não estiver definida.

   Em caso de sucesso, a string deve ser liberada com "free(value)" se
   não for "NULL".

int PyInitConfig_GetStrList(PyInitConfig *config, const char *name, size_t *length, char ***items)

   Obtém uma opção de configuração de lista de strgins como um vetor
   de strings codificadas em UTF-8 terminadas em null.

   * Define **length* e **value* retorna "0" em caso de sucesso.

   * Define um erro em *config* e retorna "-1" em caso de erro.

   Em caso de sucesso, a lista de strings deve ser liberada com
   "PyInitConfig_FreeStrList(length, items)".

void PyInitConfig_FreeStrList(size_t length, char **items)

   Libera memória de uma lista de strings criada por
   "PyInitConfig_GetStrList()".


Opções de set
-------------

O parâmetro *name* da opção de configuração deve ser uma string
codificada em UTF-8 terminada em nulo e não nula. Consulte as opções
de configuração.

Algumas opções de configuração têm efeitos colaterais em outras
opções. Essa lógica só é implementada quando
"Py_InitializeFromInitConfig()" é chamada, e não pelas funções "Set"
abaixo. Por exemplo, definir "dev_mode" como "1" não define
"faulthandler" como "1".

int PyInitConfig_SetInt(PyInitConfig *config, const char *name, int64_t value)

   Define uma opção de configuração de inteiro.

   * Retorna "0" em caso de sucesso.

   * Define um erro em *config* e retorna "-1" em caso de erro.

int PyInitConfig_SetStr(PyInitConfig *config, const char *name, const char *value)

   Define uma opção de configuração de string a partir de uma string
   codificada em UTF-8 terminada em nulo. A string será copiada.

   * Retorna "0" em caso de sucesso.

   * Define um erro em *config* e retorna "-1" em caso de erro.

int PyInitConfig_SetStrList(PyInitConfig *config, const char *name, size_t length, char *const *items)

   Define uma opção de configuração de lista de strings a partir de um
   vetor de strings codificadas em UTF-8 terminadas em nulo. A lista
   de strings será copiada.

   * Retorna "0" em caso de sucesso.

   * Define um erro em *config* e retorna "-1" em caso de erro.


Módulo
------

int PyInitConfig_AddModule(PyInitConfig *config, const char *name, PyObject *(*initfunc)(void))

   Adiciona um módulo de extensão embutido à tabela de módulos
   embutidos.

   O novo módulo pode ser importado pelo nome *name* e utiliza a
   função *initfunc* como função de inicialização, sendo chamada na
   primeira tentativa de importação.

   * Retorna "0" em caso de sucesso.

   * Define um erro em *config* e retorna "-1" em caso de erro.

   Se o Python for inicializado várias vezes,
   "PyInitConfig_AddModule()" deve ser chamada em cada inicialização
   do Python.

   Similar à função "PyImport_AppendInittab()".


Inicializar o Python
--------------------

int Py_InitializeFromInitConfig(PyInitConfig *config)

   Inicializa o Python por meio da configuração de inicialização.

   * Retorna "0" em caso de sucesso.

   * Define um erro em *config* e retorna "-1" em caso de erro.

   * Define um código de saída em *config* e retorna "-1" se o Python
     desejar sair.

   Consulte "PyInitConfig_GetExitcode()" para o caso de código de
   saída.


Opções de configuração
======================

+---------------------------+---------------------------+---------------------------+---------------------------+
| Opção                     | Membro de                 | Tipo                      | Visibilidade              |
|                           | PyConfig/PyPreConfig      |                           |                           |
|===========================|===========================|===========================|===========================|
| ""allocator""             | "allocator"               | "int"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""argv""                  | "argv"                    | "list[str]"               | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""base_exec_prefix""      | "base_exec_prefix"        | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""base_executable""       | "base_executable"         | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""base_prefix""           | "base_prefix"             | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""buffered_stdio""        | "buffered_stdio"          | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""bytes_warning""         | "bytes_warning"           | "int"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""check_hash_pycs_mode""  | "check_hash_pycs_mode"    | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""code_debug_ranges""     | "code_debug_ranges"       | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""coerce_c_locale""       | "coerce_c_locale"         | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""coerce_c_locale_warn""  | "coerce_c_locale_warn"    | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""configure_c_stdio""     | "configure_c_stdio"       | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""configure_locale""      | "configure_locale"        | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""cpu_count""             | "cpu_count"               | "int"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""dev_mode""              | "dev_mode"                | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""dump_refs""             | "dump_refs"               | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""dump_refs_file""        | "dump_refs_file"          | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""exec_prefix""           | "exec_prefix"             | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""executable""            | "executable"              | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""faulthandler""          | "faulthandler"            | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""filesystem_encoding""   | "filesystem_encoding"     | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""filesystem_errors""     | "filesystem_errors"       | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""hash_seed""             | "hash_seed"               | "int"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""home""                  | "home"                    | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""import_time""           | "import_time"             | "int"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""inspect""               | "inspect"                 | "bool"                    | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""install_signal_handler  | "install_signal_handlers" | "bool"                    | Somente leitura           |
| s""                       |                           |                           |                           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""int_max_str_digits""    | "int_max_str_digits"      | "int"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""interactive""           | "interactive"             | "bool"                    | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""isolated""              | "isolated"                | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""legacy_windows_fs_enco  | "legacy_windows_fs_encod  | "bool"                    | Somente leitura           |
| ding""                    | ing"                      |                           |                           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""legacy_windows_stdio""  | "legacy_windows_stdio"    | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""malloc_stats""          | "malloc_stats"            | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""module_search_paths""   | "module_search_paths"     | "list[str]"               | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""optimization_level""    | "optimization_level"      | "int"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""orig_argv""             | "orig_argv"               | "list[str]"               | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""parse_argv""            | "parse_argv"              | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""parser_debug""          | "parser_debug"            | "bool"                    | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""pathconfig_warnings""   | "pathconfig_warnings"     | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""perf_profiling""        | "perf_profiling"          | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""platlibdir""            | "platlibdir"              | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""prefix""                | "prefix"                  | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""program_name""          | "program_name"            | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""pycache_prefix""        | "pycache_prefix"          | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""quiet""                 | "quiet"                   | "bool"                    | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""run_command""           | "run_command"             | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""run_filename""          | "run_filename"            | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""run_module""            | "run_module"              | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""run_presite""           | "run_presite"             | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""safe_path""             | "safe_path"               | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""show_ref_count""        | "show_ref_count"          | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""site_import""           | "site_import"             | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""skip_source_first_line  | "skip_source_first_line"  | "bool"                    | Somente leitura           |
| ""                        |                           |                           |                           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""stdio_encoding""        | "stdio_encoding"          | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""stdio_errors""          | "stdio_errors"            | "str"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""stdlib_dir""            | "stdlib_dir"              | "str"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""tracemalloc""           | "tracemalloc"             | "int"                     | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""use_environment""       | "use_environment"         | "bool"                    | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""use_frozen_modules""    | "use_frozen_modules"      | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""use_hash_seed""         | "use_hash_seed"           | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""use_system_logger""     | "use_system_logger"       | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""user_site_directory""   | "user_site_directory"     | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""utf8_mode""             | "utf8_mode"               | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""verbose""               | "verbose"                 | "int"                     | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""warn_default_encoding"" | "warn_default_encoding"   | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""warnoptions""           | "warnoptions"             | "list[str]"               | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""write_bytecode""        | "write_bytecode"          | "bool"                    | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""xoptions""              | "xoptions"                | "dict[str, str]"          | Pública                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| ""_pystats""              | "_pystats"                | "bool"                    | Somente leitura           |
+---------------------------+---------------------------+---------------------------+---------------------------+

Visibilidade:

* Public: Can be retrieved by "PyConfig_Get()" and set by
  "PyConfig_Set()".

* Read-only: Can be retrieved by "PyConfig_Get()", but cannot be set
  by "PyConfig_Set()".


API de configuração Python em tempo de execução
===============================================

Em tempo de execução, é possível obter e definir opções de
configuração usando as funções "PyConfig_Get()" e "PyConfig_Set()".

O parâmetro *name* da opção de configuração deve ser uma string
codificada em UTF-8 terminada em nulo e não nula. Consulte as opções
de configuração.

Algumas opções são lidas a partir dos atributos "sys". Por exemplo, a
opção ""argv"" é lida a partir de "sys.argv".

PyObject *PyConfig_Get(const char *name)

   Obtém o valor de tempo de execução atual de uma opção de
   configuração como um objeto Python.

   * Retorna uma nova referência em caso de sucesso.

   * Define uma exceção e retorna "NULL" em caso de erro.

   O tipo de objeto depende da opção de configuração. Pode ser:

   * "bool"

   * "int"

   * "str"

   * "list[str]"

   * "dict[str, str]"

   O chamador deve ter um *estado de thread anexado*. A função não
   pode ser chamada antes da inicialização do Python nem depois da
   finalização do Python.

   Adicionado na versão 3.14.

int PyConfig_GetInt(const char *name, int *value)

   Similar a "PyConfig_Get()", mas obtém o valor como um int C.

   * Retorna "0" em caso de sucesso.

   * Define uma exceção e retorna "-1" em caso de erro.

   Adicionado na versão 3.14.

PyObject *PyConfig_Names(void)

   Obtém todos os nomes das opções de configuração como um
   "frozenset".

   * Retorna uma nova referência em caso de sucesso.

   * Define uma exceção e retorna "NULL" em caso de erro.

   O chamador deve ter um *estado de thread anexado*. A função não
   pode ser chamada antes da inicialização do Python nem depois da
   finalização do Python.

   Adicionado na versão 3.14.

int PyConfig_Set(const char *name, PyObject *value)

   Define o valor de tempo de execução atual de uma opção de
   configuração.

   * Levanta uma "ValueError" se não houver uma opção *name*.

   * Levanta uma "ValueError" se *value* foi um valor inválido.

   * Levanta uma "ValueError" se a opção for somente leitura (não
     puder ser definida).

   * Levanta um "TypeError" se *value* não tiver um tipo adequado.

   O chamador deve ter um *estado de thread anexado*. A função não
   pode ser chamada antes da inicialização do Python nem depois da
   finalização do Python.

   Levanta um evento de auditoria "cpython.PyConfig_Set" com os
   argumentos "name", "value".

   Adicionado na versão 3.14.

   Alterado na versão 3.15: The function now replaces "sys.flags"
   (create a new object), instead of modifying "sys.flags" in-place.


API C PyConfig
==============

Adicionado na versão 3.8.

Python pode ser inicializado com "Py_InitializeFromConfig()" e a
estrutura "PyConfig". Pode ser pré-inicializado com
"Py_PreInitialize()" e a estrutura "PyPreConfig".

Existem dois tipos de configuração:

* A Python Configuration pode ser usada para construir um Python
  personalizado que se comporta como um Python comum. Por exemplo,
  variáveis de ambiente e argumento de linha de comando são usados
  para configurar Python.

* A Configuração isolada pode ser usada para incorporar Python em uma
  aplicação. Isso isola Python de um sistema. Por exemplo, variáveis
  de ambiente são ignoradas, a variável local LC_CTYPE fica inalterada
  e nenhum manipulador de sinal é registrado.

A função "Py_RunMain()" pode ser usada para escrever um programa
Python personalizado.

Veja também Inicialização, Finalização e Threads.

Ver também: **PEP 587** "Configuração da inicialização do Python".


Exemplo
-------

Exemplo de Python personalizado sendo executado sempre em um modo
isolado:

   int main(int argc, char **argv)
   {
       PyStatus status;

       PyConfig config;
       PyConfig_InitPythonConfig(&config);
       config.isolated = 1;

       /* Decode command line arguments.
          Implicitly preinitialize Python (in isolated mode). */
       status = PyConfig_SetBytesArgv(&config, argc, argv);
       if (PyStatus_Exception(status)) {
           goto exception;
       }

       status = Py_InitializeFromConfig(&config);
       if (PyStatus_Exception(status)) {
           goto exception;
       }
       PyConfig_Clear(&config);

       return Py_RunMain();

   exception:
       PyConfig_Clear(&config);
       if (PyStatus_IsExit(status)) {
           return status.exitcode;
       }
       /* Display the error message and exit the process with
          non-zero exit code */
       Py_ExitStatusException(status);
   }


PyWideStringList
----------------

type PyWideStringList

   Lista de strings "wchar_t*".

   Se *length* é diferente de zero, *items* deve ser diferente de
   "NULL" e todas as strings devem ser diferentes de "NULL".

   Métodos:

   PyStatus PyWideStringList_Append(PyWideStringList *list, const wchar_t *item)

      Anexa *item* a *list*.

      Python deve ser inicializado previamente antes de chamar essa
      função.

   PyStatus PyWideStringList_Insert(PyWideStringList *list, Py_ssize_t index, const wchar_t *item)

      Insere *item* na *list* na posição *index*.

      Se *index* for maior ou igual ao comprimento da *list*, anexa o
      *item* a *list*.

      *index* deve ser maior que ou igual a "0".

      Python deve ser inicializado previamente antes de chamar essa
      função.

   Campos de estrutura:

   Py_ssize_t length

      Comprimento da lista.

   wchar_t **items

      Itens da lista.


PyStatus
--------

type PyStatus

   Estrutura para armazenar o status de uma função de inicialização:
   sucesso, erro ou saída.

   Para um erro, ela pode armazenar o nome da função C que criou o
   erro.

   Campos de estrutura:

   int exitcode

      Código de saída. Argumento passado para "exit()".

   const char *err_msg

      Mensagem de erro.

   const char *func

      Nome da função que criou um erro. Pode ser "NULL".

   Funções para criar um status:

   PyStatus PyStatus_Ok(void)

      Sucesso.

   PyStatus PyStatus_Error(const char *err_msg)

      Erro de inicialização com uma mensagem.

      *err_msg* não deve ser "NULL".

   PyStatus PyStatus_NoMemory(void)

      Falha de alocação de memória (sem memória).

   PyStatus PyStatus_Exit(int exitcode)

      Sai do Python com o código de saída especificado.

   Funções para manipular um status:

   int PyStatus_Exception(PyStatus status)

      O status é um erro ou uma saída? Se verdadeiro, a exceção deve
      ser tratada; chamando "Py_ExitStatusException()", por exemplo.

   int PyStatus_IsError(PyStatus status)

      O resultado é um erro?

   int PyStatus_IsExit(PyStatus status)

      O resultado é uma saída?

   void Py_ExitStatusException(PyStatus status)

      Chama "exit(exitcode)" se *status* for uma saída. Exibe a
      mensagem de erro e sai com um código de saída diferente de zero
      se *status* for um erro. Deve ser chamado apenas se
      "PyStatus_Exception(status)" for diferente de zero.

Nota:

  Internamente, Python usa macros que definem "PyStatus.func",
  enquanto funções para criar um status definem "func" para "NULL".

Exemplo:

   PyStatus alloc(void **ptr, size_t size)
   {
       *ptr = PyMem_RawMalloc(size);
       if (*ptr == NULL) {
           return PyStatus_NoMemory();
       }
       return PyStatus_Ok();
   }

   int main(int argc, char **argv)
   {
       void *ptr;
       PyStatus status = alloc(&ptr, 16);
       if (PyStatus_Exception(status)) {
           Py_ExitStatusException(status);
       }
       PyMem_RawFree(ptr);
       return 0;
   }


PyPreConfig
-----------

type PyPreConfig

   Estrutura usada para pré-inicializar o Python.

   A função para inicializar uma pré-configuração:

   void PyPreConfig_InitPythonConfig(PyPreConfig *preconfig)

      Inicializa a pré-configuração com Configuração do Python.

   void PyPreConfig_InitIsolatedConfig(PyPreConfig *preconfig)

      Inicializa a pré-configuração com Configuração isolada.

   Campos de estrutura:

   int allocator

      Nome de alocadores de memória em Python:

      * "PYMEM_ALLOCATOR_NOT_SET" ("0"): não altera os alocadores de
        memória (usa o padrão).

      * "PYMEM_ALLOCATOR_DEFAULT" ("1"): alocadores de memória padrão.

      * "PYMEM_ALLOCATOR_DEBUG" ("2"): alocadores de memória padrão
        com ganchos de depuração.

      * "PYMEM_ALLOCATOR_MALLOC" ("3"): usa "malloc()" da biblioteca
        C.

      * "PYMEM_ALLOCATOR_MALLOC_DEBUG" ("4"): força uso de "malloc()"
        com ganchos de depuração.

      * "PYMEM_ALLOCATOR_PYMALLOC" ("5"): alocador de memória do
        Python pymalloc.

      * "PYMEM_ALLOCATOR_PYMALLOC_DEBUG" ("6"): alocador de memória
        deo Python pymalloc com ganchos de depuração.

      * "PYMEM_ALLOCATOR_MIMALLOC" ("7"): use "mimalloc", a fast
        malloc replacement.

      * "PYMEM_ALLOCATOR_MIMALLOC_DEBUG" ("8"): use "mimalloc", a fast
        malloc replacement with debug hooks.

      "PYMEM_ALLOCATOR_PYMALLOC" e "PYMEM_ALLOCATOR_PYMALLOC_DEBUG"
      não são suportados se o Python estiver "configurado usando
      --without-pymalloc".

      "PYMEM_ALLOCATOR_MIMALLOC" e "PYMEM_ALLOCATOR_MIMALLOC_DEBUG"
      não são suportados se o Python estiver "configurado usando
      --without-mimalloc" ou se suporte atômico subjacente não estiver
      disponível.

      Veja Gerenciamento de memória.

      Padrão: "PYMEM_ALLOCATOR_NOT_SET".

   int configure_locale

      Define a localidade LC_CTYPE para a localidade preferida do
      usuário.

      Se igual a "0", define os membros "coerce_c_locale" e
      "coerce_c_locale_warn" para "0".

      Veja a *codificação da localidade*.

      Padrão: "1" na configuração do Python, "0" na configuração
      isolada.

   int coerce_c_locale

      Se igual a "2", força a localidade para C.

      Se for igual a "1", lê a localidade LC_CTYPE para decidir se
      deve ser forçado.

      Veja a *codificação da localidade*.

      Padrão: "-1" na configuração do Python, "0" na configuração
      isolada.

   int coerce_c_locale_warn

      Se diferente de zero, emite um aviso se a localidade C for
      forçada.

      Padrão: "-1" na configuração do Python, "0" na configuração
      isolada.

   int dev_mode

      Modo de desenvolvimento do Python: veja "PyConfig.dev_mode".

      Padrão: "-1" no modo do Python, "0" no modo isolado.

   int isolated

      Modo isolado: veja "PyConfig.isolated".

      Padrão: "0" no modo do Python, "1" no modo isolado.

   int legacy_windows_fs_encoding

      Se não zero:

      * Define "PyPreConfig.utf8_mode" para "0",

      * Define "PyConfig.filesystem_encoding" para ""mbcs"",

      * Define "PyConfig.filesystem_errors" para ""replace"".

      Initialized from the "PYTHONLEGACYWINDOWSFSENCODING" environment
      variable value.

      Disponível apenas no Windows. A macro "#ifdef MS_WINDOWS" pode
      ser usada para código específico do Windows.

      Padrão: "0".

   int parse_argv

      Se diferente de zero, "Py_PreInitializeFromArgs()" e
      "Py_PreInitializeFromBytesArgs()" analisam seu argumento "argv"
      da mesma forma que o Python regular analisa argumentos de linha
      de comando: veja Argumentos de linha de comando.

      Padrão: "1" na configuração do Python, "0" na configuração
      isolada.

   int use_environment

      Usar variáveis de ambiente? Veja "PyConfig.use_environment".

      Padrão: "1" na configuração do Python e "0" na configuração
      isolada.

   int utf8_mode

      Se não zero, habilita o modo UTF-8 do Python.

      Define para "0" ou "1" pela opção de linha de comando "-X utf8"
      e a variável de ambiente "PYTHONUTF8".

      Padrão: "1".


Pré-inicializar Python com PyPreConfig
--------------------------------------

A pré-inicialização do Python:

* Define os alocadores de memória Python ("PyPreConfig.allocator")

* Configura a localidade LC_CTYPE (*codificação da localidade*)

* Define o Modo UTF-8 do Python ("PyPreConfig.utf8_mode")

A pré-configuração atual (tipo "PyPreConfig") é armazenada em
"_PyRuntime.preconfig".

Funções para pré-inicializar Python:

PyStatus Py_PreInitialize(const PyPreConfig *preconfig)

   Pré-inicializa o Python a partir da pré-configuração *preconfig*.

   *preconfig* não pode ser "NULL"..

PyStatus Py_PreInitializeFromBytesArgs(const PyPreConfig *preconfig, int argc, char *const *argv)

   Pré-inicializa o Python a partir da pré-configuração *preconfig*.

   Analisa argumentos de linha de comando *argv* (strings de bytes) se
   "parse_argv" de *preconfig* for diferente de zero.

   *preconfig* não pode ser "NULL"..

PyStatus Py_PreInitializeFromArgs(const PyPreConfig *preconfig, int argc, wchar_t *const *argv)

   Pré-inicializa o Python a partir da pré-configuração *preconfig*.

   Analisa argumentos de linha de comando *argv* (strings largas) se
   "parse_argv" de *preconfig* for diferente de zero.

   *preconfig* não pode ser "NULL"..

O chamador é responsável por manipular exceções (erro ou saída) usando
"PyStatus_Exception()" e "Py_ExitStatusException()".

Para configuração do Python ("PyPreConfig_InitPythonConfig()"), se o
Python for inicializado com argumentos de linha de comando, os
argumentos de linha de comando também devem ser passados para
pré-inicializar o Python, pois eles têm um efeito na pré-configuração
como codificações. Por exemplo, a opção de linha de comando "-X utf8"
habilita o Modo UTF-8 do Python.

"PyMem_SetAllocator()" pode ser chamado depois de "Py_PreInitialize()"
e antes de "Py_InitializeFromConfig()" para instalar um alocador de
memória personalizado. Ele pode ser chamado antes de
"Py_PreInitialize()" se "PyPreConfig.allocator" estiver definido como
"PYMEM_ALLOCATOR_NOT_SET".

Funções de alocação de memória do Python como "PyMem_RawMalloc()" não
devem ser usadas antes da pré-inicialização do Python, enquanto chamar
diretamente "malloc()" e "free()" é sempre seguro. "Py_DecodeLocale()"
não deve ser chamado antes da pré-inicialização do Python.

Exemplo usando a pré-inicialização para habilitar o modo UTF-8 do
Python.

   PyStatus status;
   PyPreConfig preconfig;
   PyPreConfig_InitPythonConfig(&preconfig);

   preconfig.utf8_mode = 1;

   status = Py_PreInitialize(&preconfig);
   if (PyStatus_Exception(status)) {
       Py_ExitStatusException(status);
   }

   /* at this point, Python speaks UTF-8 */

   Py_Initialize();
   /* ... use Python API here ... */
   Py_Finalize();


PyConfig
--------

type PyConfig

   Estrutura contendo a maioria dos parâmetros para configurar o
   Python.

   Ao terminar, a função "PyConfig_Clear()" deve ser usada para
   liberar a memória de configuração.

   Structure methods:

   void PyConfig_InitPythonConfig(PyConfig *config)

      Initialize configuration with the Python Configuration.

   void PyConfig_InitIsolatedConfig(PyConfig *config)

      Initialize configuration with the Isolated Configuration.

   PyStatus PyConfig_SetString(PyConfig *config, wchar_t *const *config_str, const wchar_t *str)

      Copy the wide character string *str* into "*config_str".

      Preinitialize Python if needed.

   PyStatus PyConfig_SetBytesString(PyConfig *config, wchar_t *const *config_str, const char *str)

      Decode *str* using "Py_DecodeLocale()" and set the result into
      "*config_str".

      Preinitialize Python if needed.

   PyStatus PyConfig_SetArgv(PyConfig *config, int argc, wchar_t *const *argv)

      Set command line arguments ("argv" member of *config*) from the
      *argv* list of wide character strings.

      Preinitialize Python if needed.

   PyStatus PyConfig_SetBytesArgv(PyConfig *config, int argc, char *const *argv)

      Set command line arguments ("argv" member of *config*) from the
      *argv* list of bytes strings. Decode bytes using
      "Py_DecodeLocale()".

      Preinitialize Python if needed.

   PyStatus PyConfig_SetWideStringList(PyConfig *config, PyWideStringList *list, Py_ssize_t length, wchar_t **items)

      Set the list of wide strings *list* to *length* and *items*.

      Preinitialize Python if needed.

   PyStatus PyConfig_Read(PyConfig *config)

      Lê toda a configuração do Python.

      Campos que já estão inicializados permanecem inalterados.

      Fields for path configuration are no longer calculated or
      modified when calling this function, as of Python 3.11.

      The "PyConfig_Read()" function only parses "PyConfig.argv"
      arguments once: "PyConfig.parse_argv" is set to "2" after
      arguments are parsed. Since Python arguments are stripped from
      "PyConfig.argv", parsing arguments twice would parse the
      application options as Python options.

      Preinitialize Python if needed.

      Alterado na versão 3.10: The "PyConfig.argv" arguments are now
      only parsed once, "PyConfig.parse_argv" is set to "2" after
      arguments are parsed, and arguments are only parsed if
      "PyConfig.parse_argv" equals "1".

      Alterado na versão 3.11: "PyConfig_Read()" no longer calculates
      all paths, and so fields listed under Python Path Configuration
      may no longer be updated until "Py_InitializeFromConfig()" is
      called.

   void PyConfig_Clear(PyConfig *config)

      Libera memória de configuração.

   Most "PyConfig" methods preinitialize Python if needed. In that
   case, the Python preinitialization configuration ("PyPreConfig") is
   based on the "PyConfig". If configuration fields which are in
   common with "PyPreConfig" are tuned, they must be set before
   calling a "PyConfig" method:

   * "PyConfig.dev_mode"

   * "PyConfig.isolated"

   * "PyConfig.parse_argv"

   * "PyConfig.use_environment"

   Moreover, if "PyConfig_SetArgv()" or "PyConfig_SetBytesArgv()" is
   used, this method must be called before other methods, since the
   preinitialization configuration depends on command line arguments
   (if "parse_argv" is non-zero).

   The caller of these methods is responsible to handle exceptions
   (error or exit) using "PyStatus_Exception()" and
   "Py_ExitStatusException()".

   Campos de estrutura:

   PyWideStringList argv

      Set "sys.argv" command line arguments based on "argv".  These
      parameters are similar to those passed to the program's "main()"
      function with the difference that the first entry should refer
      to the script file to be executed rather than the executable
      hosting the Python interpreter.  If there isn't a script that
      will be run, the first entry in "argv" can be an empty string.

      Set "parse_argv" to "1" to parse "argv" the same way the regular
      Python parses Python command line arguments and then to strip
      Python arguments from "argv".

      If "argv" is empty, an empty string is added to ensure that
      "sys.argv" always exists and is never empty.

      Padrão: "NULL".

      See also the "orig_argv" member.

   int safe_path

      If equals to zero, "Py_RunMain()" prepends a potentially unsafe
      path to "sys.path" at startup:

      * If "argv[0]" is equal to "L"-m"" ("python -m module"), prepend
        the current working directory.

      * If running a script ("python script.py"), prepend the script's
        directory.  If it's a symbolic link, resolve symbolic links.

      * Otherwise ("python -c code" and "python"), prepend an empty
        string, which means the current working directory.

      Set to "1" by the "-P" command line option and the
      "PYTHONSAFEPATH" environment variable.

      Default: "0" in Python config, "1" in isolated config.

      Adicionado na versão 3.11.

   wchar_t *base_exec_prefix

      "sys.base_exec_prefix".

      Padrão: "NULL".

      Part of the Python Path Configuration output.

      Veja também "PyConfig.exec_prefix".

   wchar_t *base_executable

      Python base executable: "sys._base_executable".

      Set by the "__PYVENV_LAUNCHER__" environment variable.

      Set from "PyConfig.executable" if "NULL".

      Padrão: "NULL".

      Part of the Python Path Configuration output.

      See also "PyConfig.executable".

   wchar_t *base_prefix

      "sys.base_prefix".

      Padrão: "NULL".

      Part of the Python Path Configuration output.

      See also "PyConfig.prefix".

   int buffered_stdio

      If equals to "0" and "configure_c_stdio" is non-zero, disable
      buffering on the C streams stdout and stderr.

      Set to "0" by the "-u" command line option and the
      "PYTHONUNBUFFERED" environment variable.

      stdin is always opened in buffered mode.

      Padrão: "1".

   int bytes_warning

      If equals to "1", issue a warning when comparing "bytes" or
      "bytearray" with "str", or comparing "bytes" with "int".

      If equal or greater to "2", raise a "BytesWarning" exception in
      these cases.

      Incremented by the "-b" command line option.

      Padrão: "0".

      Descontinuado desde a versão 3.15, será removido na versão 3.17:
      The "-b" and "-bb" options will become no-op in 3.17.
      "bytes_warning" member will be removed in 3.17.

   int warn_default_encoding

      If non-zero, emit a "EncodingWarning" warning when
      "io.TextIOWrapper" uses its default encoding. See Ativar
      EncodingWarning for details.

      Padrão: "0".

      Adicionado na versão 3.10.

   int code_debug_ranges

      If equals to "0", disables the inclusion of the end line and
      column mappings in code objects. Also disables traceback
      printing carets to specific error locations.

      Set to "0" by the "PYTHONNODEBUGRANGES" environment variable and
      by the "-X no_debug_ranges" command line option.

      Padrão: "1".

      Adicionado na versão 3.11.

   wchar_t *check_hash_pycs_mode

      Control the validation behavior of hash-based ".pyc" files:
      value of the "--check-hash-based-pycs" command line option.

      Valores válidos:

      * "L"always"": Hash the source file for invalidation regardless
        of value of the 'check_source' flag.

      * "L"never"": Assume that hash-based pycs always are valid.

      * "L"default"": The 'check_source' flag in hash-based pycs
        determines invalidation.

      Default: "L"default"".

      See also **PEP 552** "Deterministic pycs".

   int configure_c_stdio

      If non-zero, configure C standard streams:

      * On Windows, set the binary mode ("O_BINARY") on stdin, stdout
        and stderr.

      * If "buffered_stdio" equals zero, disable buffering of stdin,
        stdout and stderr streams.

      * If "interactive" is non-zero, enable stream buffering on stdin
        and stdout (only stdout on Windows).

      Padrão: "1" na configuração do Python, "0" na configuração
      isolada.

   int dev_mode

      If non-zero, enable the Python Development Mode.

      Set to "1" by the "-X dev" option and the "PYTHONDEVMODE"
      environment variable.

      Padrão: "-1" no modo do Python, "0" no modo isolado.

   int dump_refs

      Dump Python references?

      If non-zero, dump all objects which are still alive at exit.

      Set to "1" by the "PYTHONDUMPREFS" environment variable.

      Needs a special build of Python with the "Py_TRACE_REFS" macro
      defined: see the "configure --with-trace-refs option".

      Padrão: "0".

   wchar_t *dump_refs_file

      Filename where to dump Python references.

      Set by the "PYTHONDUMPREFSFILE" environment variable.

      Padrão: "NULL".

      Adicionado na versão 3.11.

   wchar_t *exec_prefix

      The site-specific directory prefix where the platform-dependent
      Python files are installed: "sys.exec_prefix".

      Padrão: "NULL".

      Part of the Python Path Configuration output.

      See also "PyConfig.base_exec_prefix".

   wchar_t *executable

      The absolute path of the executable binary for the Python
      interpreter: "sys.executable".

      Padrão: "NULL".

      Part of the Python Path Configuration output.

      See also "PyConfig.base_executable".

   int faulthandler

      Enable faulthandler?

      If non-zero, call "faulthandler.enable()" at startup.

      Set to "1" by "-X faulthandler" and the "PYTHONFAULTHANDLER"
      environment variable.

      Padrão: "-1" no modo do Python, "0" no modo isolado.

   wchar_t *filesystem_encoding

      *Filesystem encoding*: "sys.getfilesystemencoding()".

      On macOS, Android and VxWorks: use ""utf-8"" by default.

      On Windows: use ""utf-8"" by default, or ""mbcs"" if
      "legacy_windows_fs_encoding" of "PyPreConfig" is non-zero.

      Default encoding on other platforms:

      * ""utf-8"" if "PyPreConfig.utf8_mode" is non-zero.

      * ""ascii"" if Python detects that "nl_langinfo(CODESET)"
        announces the ASCII encoding, whereas the "mbstowcs()"
        function decodes from a different encoding (usually Latin1).

      * ""utf-8"" if "nl_langinfo(CODESET)" returns an empty string.

      * Otherwise, use the *locale encoding*: "nl_langinfo(CODESET)"
        result.

      At Python startup, the encoding name is normalized to the Python
      codec name. For example, ""ANSI_X3.4-1968"" is replaced with
      ""ascii"".

      See also the "filesystem_errors" member.

      See also "PyUnicode_EncodeFSDefault()" and related functions for
      encoding paths at runtime.

   wchar_t *filesystem_errors

      *Filesystem error handler*: "sys.getfilesystemencodeerrors()".

      On Windows: use ""surrogatepass"" by default, or ""replace""  if
      "legacy_windows_fs_encoding" of "PyPreConfig" is non-zero.

      On other platforms: use ""surrogateescape"" by default.

      Supported error handlers:

      * ""strict""

      * ""surrogateescape""

      * ""surrogatepass"" (only supported with the UTF-8 encoding)

      See also the "filesystem_encoding" member.

   int use_frozen_modules

      If non-zero, use frozen modules.

      Set by the "PYTHON_FROZEN_MODULES" environment variable.

      Default: "1" in a release build, or "0" in a debug build.

   unsigned long hash_seed

   int use_hash_seed

      Randomized hash function seed.

      If "use_hash_seed" is zero, a seed is chosen randomly at Python
      startup, and "hash_seed" is ignored.

      Set by the "PYTHONHASHSEED" environment variable.

      Default *use_hash_seed* value: "-1" in Python mode, "0" in
      isolated mode.

   wchar_t *home

      Set the default Python "home" directory, that is, the location
      of the standard Python libraries (see "PYTHONHOME").

      Set by the "PYTHONHOME" environment variable.

      Padrão: "NULL".

      Part of the Python Path Configuration input.

   int import_time

         If "1", profile import time. If "2", include additional
         output that indicates when an imported module has already
         been loaded.

         Set by the "-X importtime" option and the
         "PYTHONPROFILEIMPORTTIME" environment variable.

         Padrão: "0".

      Alterado na versão 3.14: Added support for "import_time = 2"

   int inspect

      Enter interactive mode after executing a script or a command.

      If greater than "0", enable inspect: when a script is passed as
      first argument or the -c option is used, enter interactive mode
      after executing the script or the command, even when "sys.stdin"
      does not appear to be a terminal.

      Incremented by the "-i" command line option. Set to "1" if the
      "PYTHONINSPECT" environment variable is non-empty.

      Padrão: "0".

   int install_signal_handlers

      Install Python signal handlers?

      Default: "1" in Python mode, "0" in isolated mode.

   int interactive

      If greater than "0", enable the interactive mode (REPL).

      Incremented by the "-i" command line option.

      Padrão: "0".

   int int_max_str_digits

      Configures the integer string conversion length limitation.  An
      initial value of "-1" means the value will be taken from the
      command line or environment or otherwise default to 4300
      ("sys.int_info.default_max_str_digits").  A value of "0"
      disables the limitation.  Values greater than zero but less than
      640 ("sys.int_info.str_digits_check_threshold") are unsupported
      and will produce an error.

      Configured by the "-X int_max_str_digits" command line flag or
      the "PYTHONINTMAXSTRDIGITS" environment variable.

      Default: "-1" in Python mode.  4300
      ("sys.int_info.default_max_str_digits") in isolated mode.

      Adicionado na versão 3.12.

   int cpu_count

      If the value of "cpu_count" is not "-1" then it will override
      the return values of "os.cpu_count()", "os.process_cpu_count()",
      and "multiprocessing.cpu_count()".

      Configured by the "-X cpu_count=*n|default*" command line flag
      or the "PYTHON_CPU_COUNT" environment variable.

      Default: "-1".

      Adicionado na versão 3.13.

   int isolated

      If greater than "0", enable isolated mode:

      * Set "safe_path" to "1": don't prepend a potentially unsafe
        path to "sys.path" at Python startup, such as the current
        directory, the script's directory or an empty string.

      * Set "use_environment" to "0": ignore "PYTHON" environment
        variables.

      * Set "user_site_directory" to "0": don't add the user site
        directory to "sys.path".

      * Python REPL doesn't import "readline" nor enable default
        readline configuration on interactive prompts.

      Set to "1" by the "-I" command line option.

      Padrão: "0" no modo do Python, "1" no modo isolado.

      See also the Isolated Configuration and "PyPreConfig.isolated".

   int legacy_windows_stdio

      If non-zero, use "io.FileIO" instead of "io._WindowsConsoleIO"
      for "sys.stdin", "sys.stdout" and "sys.stderr".

      Definida como "1" se a variável de ambiente
      "PYTHONLEGACYWINDOWSSTDIO" estiver definida como uma string não
      vazia.

      Disponível apenas no Windows. A macro "#ifdef MS_WINDOWS" pode
      ser usada para código específico do Windows.

      Padrão: "0".

      See also the **PEP 528** (Change Windows console encoding to
      UTF-8).

   int malloc_stats

      If non-zero, dump statistics on Python pymalloc memory allocator
      at exit.

      Set to "1" by the "PYTHONMALLOCSTATS" environment variable.

      The option is ignored if Python is "configured using the
      --without-pymalloc option".

      Padrão: "0".

   wchar_t *platlibdir

      Platform library directory name: "sys.platlibdir".

      Set by the "PYTHONPLATLIBDIR" environment variable.

      Default: value of the "PLATLIBDIR" macro which is set by the
      "configure --with-platlibdir option" (default: ""lib"", or
      ""DLLs"" on Windows).

      Part of the Python Path Configuration input.

      Adicionado na versão 3.9.

      Alterado na versão 3.11: This macro is now used on Windows to
      locate the standard library extension modules, typically under
      "DLLs". However, for compatibility, note that this value is
      ignored for any non-standard layouts, including in-tree builds
      and virtual environments.

   wchar_t *pythonpath_env

      Module search paths ("sys.path") as a string separated by
      "DELIM" ("os.pathsep").

      Set by the "PYTHONPATH" environment variable.

      Padrão: "NULL".

      Part of the Python Path Configuration input.

   PyWideStringList module_search_paths

   int module_search_paths_set

      Module search paths: "sys.path".

      If "module_search_paths_set" is equal to "0",
      "Py_InitializeFromConfig()" will replace "module_search_paths"
      and sets "module_search_paths_set" to "1".

      Default: empty list ("module_search_paths") and "0"
      ("module_search_paths_set").

      Part of the Python Path Configuration output.

   int optimization_level

      Compilation optimization level:

      * "0": Peephole optimizer, set "__debug__" to "True".

      * "1": Level 0, remove assertions, set "__debug__" to "False".

      * "2": Level 1, strip docstrings.

      Incremented by the "-O" command line option. Set to the
      "PYTHONOPTIMIZE" environment variable value.

      Padrão: "0".

   PyWideStringList orig_argv

      The list of the original command line arguments passed to the
      Python executable: "sys.orig_argv".

      If "orig_argv" list is empty and "argv" is not a list only
      containing an empty string, "PyConfig_Read()" copies "argv" into
      "orig_argv" before modifying "argv" (if "parse_argv" is non-
      zero).

      See also the "argv" member and the "Py_GetArgcArgv()" function.

      Padrão: lista vazia.

      Adicionado na versão 3.10.

   int parse_argv

      Parse command line arguments?

      If equals to "1", parse "argv" the same way the regular Python
      parses command line arguments, and strip Python arguments from
      "argv".

      The "PyConfig_Read()" function only parses "PyConfig.argv"
      arguments once: "PyConfig.parse_argv" is set to "2" after
      arguments are parsed. Since Python arguments are stripped from
      "PyConfig.argv", parsing arguments twice would parse the
      application options as Python options.

      Default: "1" in Python mode, "0" in isolated mode.

      Alterado na versão 3.10: The "PyConfig.argv" arguments are now
      only parsed if "PyConfig.parse_argv" equals to "1".

   int parser_debug

      Parser debug mode. If greater than "0", turn on parser debugging
      output (for expert only, depending on compilation options).

      Incremented by the "-d" command line option. Set to the
      "PYTHONDEBUG" environment variable value.

      Needs a debug build of Python (the "Py_DEBUG" macro must be
      defined).

      Padrão: "0".

   int pathconfig_warnings

      If non-zero, calculation of path configuration is allowed to log
      warnings into "stderr". If equals to "0", suppress these
      warnings.

      Default: "1" in Python mode, "0" in isolated mode.

      Part of the Python Path Configuration input.

      Alterado na versão 3.11: Now also applies on Windows.

   wchar_t *prefix

      The site-specific directory prefix where the platform
      independent Python files are installed: "sys.prefix".

      Padrão: "NULL".

      Part of the Python Path Configuration output.

      See also "PyConfig.base_prefix".

   wchar_t *program_name

      Program name used to initialize "executable" and in early error
      messages during Python initialization.

      * On macOS, use "PYTHONEXECUTABLE" environment variable if set.

      * If the "WITH_NEXT_FRAMEWORK" macro is defined, use
        "__PYVENV_LAUNCHER__" environment variable if set.

      * Use "argv[0]" of "argv" if available and non-empty.

      * Otherwise, use "L"python"" on Windows, or "L"python3"" on
        other platforms.

      Padrão: "NULL".

      Part of the Python Path Configuration input.

   wchar_t *pycache_prefix

      Directory where cached ".pyc" files are written:
      "sys.pycache_prefix".

      Set by the "-X pycache_prefix=PATH" command line option and the
      "PYTHONPYCACHEPREFIX" environment variable. The command-line
      option takes precedence.

      If "NULL", "sys.pycache_prefix" is set to "None".

      Padrão: "NULL".

   int quiet

      Quiet mode. If greater than "0", don't display the copyright and
      version at Python startup in interactive mode.

      Incremented by the "-q" command line option.

      Padrão: "0".

   wchar_t *run_command

      Value of the "-c" command line option.

      Used by "Py_RunMain()".

      Padrão: "NULL".

   wchar_t *run_filename

      Filename passed on the command line: trailing command line
      argument without "-c" or "-m". It is used by the "Py_RunMain()"
      function.

      For example, it is set to "script.py" by the "python3 script.py
      arg" command line.

      See also the "PyConfig.skip_source_first_line" option.

      Padrão: "NULL".

   wchar_t *run_module

      Value of the "-m" command line option.

      Used by "Py_RunMain()".

      Padrão: "NULL".

   wchar_t *run_presite

      "module" or "module:func" entry point that should be executed
      before the "site" module is imported.

      Set by the "-X presite=module:func" command-line option and the
      "PYTHON_PRESITE" environment variable. The command-line option
      takes precedence.

      Needs a debug build of Python (the "Py_DEBUG" macro must be
      defined).

      Padrão: "NULL".

   int show_ref_count

      Show total reference count at exit (excluding *immortal*
      objects)?

      Set to "1" by "-X showrefcount" command line option.

      Needs a debug build of Python (the "Py_REF_DEBUG" macro must be
      defined).

      Padrão: "0".

   int site_import

      Import the "site" module at startup?

      If equal to zero, disable the import of the module site and the
      site-dependent manipulations of "sys.path" that it entails.

      Also disable these manipulations if the "site" module is
      explicitly imported later (call "site.main()" if you want them
      to be triggered).

      Set to "0" by the "-S" command line option.

      "sys.flags.no_site" is set to the inverted value of
      "site_import".

      Padrão: "1".

   int skip_source_first_line

      If non-zero, skip the first line of the "PyConfig.run_filename"
      source.

      It allows the usage of non-Unix forms of "#!cmd". This is
      intended for a DOS specific hack only.

      Set to "1" by the "-x" command line option.

      Padrão: "0".

   wchar_t *stdio_encoding

   wchar_t *stdio_errors

      Encoding and encoding errors of "sys.stdin", "sys.stdout" and
      "sys.stderr" (but "sys.stderr" always uses ""backslashreplace""
      error handler).

      Use the "PYTHONIOENCODING" environment variable if it is non-
      empty.

      Codificação padrão:

      * ""UTF-8"" if "PyPreConfig.utf8_mode" is non-zero.

      * Otherwise, use the *locale encoding*.

      Tratador de erros padrão:

      * On Windows: use ""surrogateescape"".

      * ""surrogateescape"" if "PyPreConfig.utf8_mode" is non-zero, or
        if the LC_CTYPE locale is "C" or "POSIX".

      * ""strict"" otherwise.

      See also "PyConfig.legacy_windows_stdio".

   int tracemalloc

      Enable tracemalloc?

      If non-zero, call "tracemalloc.start()" at startup.

      Set by "-X tracemalloc=N" command line option and by the
      "PYTHONTRACEMALLOC" environment variable.

      Padrão: "-1" no modo do Python, "0" no modo isolado.

   int perf_profiling

      Enable the Linux "perf" profiler support?

      If equals to "1", enable support for the Linux "perf" profiler.

      If equals to "2", enable support for the Linux "perf" profiler
      with DWARF JIT support.

      Set to "1" by "-X perf" command-line option and the
      "PYTHONPERFSUPPORT" environment variable.

      Set to "2" by the "-X perf_jit" command-line option and the
      "PYTHON_PERF_JIT_SUPPORT" environment variable.

      Default: "-1".

      Ver também:

        See Python support for the perf map compatible profilers for
        more information.

      Adicionado na versão 3.12.

   wchar_t *stdlib_dir

      Directory of the Python standard library.

      Padrão: "NULL".

      Adicionado na versão 3.11.

   int use_environment

      Use environment variables?

      If equals to zero, ignore the environment variables.

      Set to "0" by the "-E" environment variable.

      Padrão: "1" na configuração do Python e "0" na configuração
      isolada.

   int use_system_logger

      If non-zero, "stdout" and "stderr" will be redirected to the
      system log.

      Only available on macOS 10.12 and later, and on iOS.

      Default: "0" (don't use the system log) on macOS; "1" on iOS
      (use the system log).

      Adicionado na versão 3.14.

   int user_site_directory

      If non-zero, add the user site directory to "sys.path".

      Set to "0" by the "-s" and "-I" command line options.

      Set to "0" by the "PYTHONNOUSERSITE" environment variable.

      Default: "1" in Python mode, "0" in isolated mode.

   int verbose

      Verbose mode. If greater than "0", print a message each time a
      module is imported, showing the place (filename or built-in
      module) from which it is loaded.

      If greater than or equal to "2", print a message for each file
      that is checked for when searching for a module. Also provides
      information on module cleanup at exit.

      Incremented by the "-v" command line option.

      Set by the "PYTHONVERBOSE" environment variable value.

      Padrão: "0".

   PyWideStringList warnoptions

      Options of the "warnings" module to build warnings filters,
      lowest to highest priority: "sys.warnoptions".

      The "warnings" module adds "sys.warnoptions" in the reverse
      order: the last "PyConfig.warnoptions" item becomes the first
      item of "warnings.filters" which is checked first (highest
      priority).

      The "-W" command line options adds its value to "warnoptions",
      it can be used multiple times.

      The "PYTHONWARNINGS" environment variable can also be used to
      add warning options. Multiple options can be specified,
      separated by commas (",").

      Padrão: lista vazia.

   int write_bytecode

      If equal to "0", Python won't try to write ".pyc" files on the
      import of source modules.

      Set to "0" by the "-B" command line option and the
      "PYTHONDONTWRITEBYTECODE" environment variable.

      "sys.dont_write_bytecode" is initialized to the inverted value
      of "write_bytecode".

      Padrão: "1".

   PyWideStringList xoptions

      Values of the "-X" command line options: "sys._xoptions".

      Padrão: lista vazia.

   int _pystats

      If non-zero, write performance statistics at Python exit.

      Need a special build with the "Py_STATS" macro: see "--enable-
      pystats".

      Padrão: "0".

If "parse_argv" is non-zero, "argv" arguments are parsed the same way
the regular Python parses command line arguments, and Python arguments
are stripped from "argv".

The "xoptions" options are parsed to set other options: see the "-X"
command line option.

Alterado na versão 3.9: The "show_alloc_count" field has been removed.


Initialization with PyConfig
----------------------------

Initializing the interpreter from a populated configuration struct is
handled by calling "Py_InitializeFromConfig()".

O chamador é responsável por manipular exceções (erro ou saída) usando
"PyStatus_Exception()" e "Py_ExitStatusException()".

If "PyImport_FrozenModules()", "PyImport_AppendInittab()" or
"PyImport_ExtendInittab()" are used, they must be set or called after
Python preinitialization and before the Python initialization. If
Python is initialized multiple times, "PyImport_AppendInittab()" or
"PyImport_ExtendInittab()" must be called before each Python
initialization.

The current configuration ("PyConfig" type) is stored in
"PyInterpreterState.config".

Example setting the program name:

   void init_python(void)
   {
       PyStatus status;

       PyConfig config;
       PyConfig_InitPythonConfig(&config);

       /* Set the program name. Implicitly preinitialize Python. */
       status = PyConfig_SetString(&config, &config.program_name,
                                   L"/path/to/my_program");
       if (PyStatus_Exception(status)) {
           goto exception;
       }

       status = Py_InitializeFromConfig(&config);
       if (PyStatus_Exception(status)) {
           goto exception;
       }
       PyConfig_Clear(&config);
       return;

   exception:
       PyConfig_Clear(&config);
       Py_ExitStatusException(status);
   }

More complete example modifying the default configuration, read the
configuration, and then override some parameters. Note that since
3.11, many parameters are not calculated until initialization, and so
values cannot be read from the configuration structure. Any values set
before initialize is called will be left unchanged by initialization:

   PyStatus init_python(const char *program_name)
   {
       PyStatus status;

       PyConfig config;
       PyConfig_InitPythonConfig(&config);

       /* Set the program name before reading the configuration
          (decode byte string from the locale encoding).

          Implicitly preinitialize Python. */
       status = PyConfig_SetBytesString(&config, &config.program_name,
                                        program_name);
       if (PyStatus_Exception(status)) {
           goto done;
       }

       /* Read all configuration at once */
       status = PyConfig_Read(&config);
       if (PyStatus_Exception(status)) {
           goto done;
       }

       /* Specify sys.path explicitly */
       /* If you want to modify the default set of paths, finish
          initialization first and then use PySys_GetAttrString("path") */
       config.module_search_paths_set = 1;
       status = PyWideStringList_Append(&config.module_search_paths,
                                        L"/path/to/stdlib");
       if (PyStatus_Exception(status)) {
           goto done;
       }
       status = PyWideStringList_Append(&config.module_search_paths,
                                        L"/path/to/more/modules");
       if (PyStatus_Exception(status)) {
           goto done;
       }

       /* Override executable computed by PyConfig_Read() */
       status = PyConfig_SetString(&config, &config.executable,
                                   L"/path/to/my_executable");
       if (PyStatus_Exception(status)) {
           goto done;
       }

       status = Py_InitializeFromConfig(&config);

   done:
       PyConfig_Clear(&config);
       return status;
   }


Isolated Configuration
----------------------

"PyPreConfig_InitIsolatedConfig()" and "PyConfig_InitIsolatedConfig()"
functions create a configuration to isolate Python from the system.
For example, to embed Python into an application.

This configuration ignores global configuration variables, environment
variables, command line arguments ("PyConfig.argv" is not parsed) and
user site directory. The C standard streams (ex: "stdout") and the
LC_CTYPE locale are left unchanged. Signal handlers are not installed.

Configuration files are still used with this configuration to
determine paths that are unspecified. Ensure "PyConfig.home" is
specified to avoid computing the default path configuration.


Configuração do Python
----------------------

"PyPreConfig_InitPythonConfig()" and "PyConfig_InitPythonConfig()"
functions create a configuration to build a customized Python which
behaves as the regular Python.

Environments variables and command line arguments are used to
configure Python, whereas global configuration variables are ignored.

This function enables C locale coercion (**PEP 538**) and Python UTF-8
Mode (**PEP 540**) depending on the LC_CTYPE locale, "PYTHONUTF8" and
"PYTHONCOERCECLOCALE" environment variables.


Python Path Configuration
-------------------------

"PyConfig" contains multiple fields for the path configuration:

* Path configuration inputs:

  * "PyConfig.home"

  * "PyConfig.platlibdir"

  * "PyConfig.pathconfig_warnings"

  * "PyConfig.program_name"

  * "PyConfig.pythonpath_env"

  * current working directory: to get absolute paths

  * "PATH" environment variable to get the program full path (from
    "PyConfig.program_name")

  * "__PYVENV_LAUNCHER__" environment variable

  * (Windows only) Application paths in the registry under
    "SoftwarePythonPythonCoreX.YPythonPath" of HKEY_CURRENT_USER and
    HKEY_LOCAL_MACHINE (where X.Y is the Python version).

* Path configuration output fields:

  * "PyConfig.base_exec_prefix"

  * "PyConfig.base_executable"

  * "PyConfig.base_prefix"

  * "PyConfig.exec_prefix"

  * "PyConfig.executable"

  * "PyConfig.module_search_paths_set", "PyConfig.module_search_paths"

  * "PyConfig.prefix"

If at least one "output field" is not set, Python calculates the path
configuration to fill unset fields. If "module_search_paths_set" is
equal to "0", "module_search_paths" is overridden and
"module_search_paths_set" is set to "1".

It is possible to completely ignore the function calculating the
default path configuration by setting explicitly all path
configuration output fields listed above. A string is considered as
set even if it is non-empty. "module_search_paths" is considered as
set if "module_search_paths_set" is set to "1". In this case,
"module_search_paths" will be used without modification.

Set "pathconfig_warnings" to "0" to suppress warnings when calculating
the path configuration (Unix only, Windows does not log any warning).

If "base_prefix" or "base_exec_prefix" fields are not set, they
inherit their value from "prefix" and "exec_prefix" respectively.

"Py_RunMain()" and "Py_Main()" modify "sys.path":

* If "run_filename" is set and is a directory which contains a
  "__main__.py" script, prepend "run_filename" to "sys.path".

* If "isolated" is zero:

  * If "run_module" is set, prepend the current directory to
    "sys.path". Do nothing if the current directory cannot be read.

  * If "run_filename" is set, prepend the directory of the filename to
    "sys.path".

  * Otherwise, prepend an empty string to "sys.path".

If "site_import" is non-zero, "sys.path" can be modified by the "site"
module. If "user_site_directory" is non-zero and the user's site-
package directory exists, the "site" module appends the user's site-
package directory to "sys.path".

The following configuration files are used by the path configuration:

* "pyvenv.cfg"

* "._pth" file (ex: "python._pth")

* "pybuilddir.txt" (Unix only)

If a "._pth" file is present:

* Set "isolated" to "1".

* Set "use_environment" to "0".

* Set "site_import" to "0".

* Set "user_site_directory" to "0" (since 3.15).

* Set "safe_path" to "1".

If "home" is not set and a "pyvenv.cfg" file is present in the same
directory as "executable", or its parent, "prefix" and "exec_prefix"
are set that location. When this happens, "base_prefix" and
"base_exec_prefix" still keep their value, pointing to the base
installation. See Ambientes virtuais for more information.

The "__PYVENV_LAUNCHER__" environment variable is used to set
"PyConfig.base_executable".

Alterado na versão 3.14: "prefix", and "exec_prefix", are now set to
the "pyvenv.cfg" directory. This was previously done by "site",
therefore affected by "-S".

Alterado na versão 3.15: "user_site_directory" is now set to "0" when
a "._pth" file is present.


Py_GetArgcArgv()
================

void Py_GetArgcArgv(int *argc, wchar_t ***argv)

   Get the original command line arguments, before Python modified
   them.

   See also "PyConfig.orig_argv" member.


Multi-Phase Initialization Private Provisional API
==================================================

This section is a private provisional API introducing multi-phase
initialization, the core feature of **PEP 432**:

* "Core" initialization phase, "bare minimum Python":

  * Builtin types;

  * Builtin exceptions;

  * Builtin and frozen modules;

  * The "sys" module is only partially initialized (ex: "sys.path"
    doesn't exist yet).

* "Main" initialization phase, Python is fully initialized:

  * Install and configure "importlib";

  * Apply the Path Configuration;

  * Install signal handlers;

  * Finish "sys" module initialization (ex: create "sys.stdout" and
    "sys.path");

  * Enable optional features like "faulthandler" and "tracemalloc";

  * Import the "site" module;

  * etc.

Private provisional API:

int PyConfig._init_main

   If set to "0", "Py_InitializeFromConfig()" stops at the "Core"
   initialization phase.

PyStatus _Py_InitializeMain(void)

   Move to the "Main" initialization phase, finish the Python
   initialization.

No module is imported during the "Core" phase and the "importlib"
module is not configured: the Path Configuration is only applied
during the "Main" phase. It may allow to customize Python in Python to
override or tune the Path Configuration, maybe install a custom
"sys.meta_path" importer or an import hook, etc.

It may become possible to calculate the Path Configuration in Python,
after the Core phase and before the Main phase, which is one of the
**PEP 432** motivation.

The "Core" phase is not properly defined: what should be and what
should not be available at this phase is not specified yet. The API is
marked as private and provisional: the API can be modified or even be
removed anytime until a proper public API is designed.

Example running Python code between "Core" and "Main" initialization
phases:

   void init_python(void)
   {
       PyStatus status;

       PyConfig config;
       PyConfig_InitPythonConfig(&config);
       config._init_main = 0;

       /* ... customize 'config' configuration ... */

       status = Py_InitializeFromConfig(&config);
       PyConfig_Clear(&config);
       if (PyStatus_Exception(status)) {
           Py_ExitStatusException(status);
       }

       /* Use sys.stderr because sys.stdout is only created
          by _Py_InitializeMain() */
       int res = PyRun_SimpleString(
           "import sys; "
           "print('Run Python code before _Py_InitializeMain', "
                  "file=sys.stderr)");
       if (res < 0) {
           exit(1);
       }

       /* ... put more configuration code here ... */

       status = _Py_InitializeMain();
       if (PyStatus_Exception(status)) {
           Py_ExitStatusException(status);
       }
   }
