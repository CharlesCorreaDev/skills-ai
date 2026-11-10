Importando módulos
******************

PyObject *PyImport_ImportModule(const char *name)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Esta é uma função auxiliar em torno de "PyImport_Import()", que
   recebe um const char* como argumento em vez de um PyObject*.

PyObject *PyImport_ImportModuleEx(const char *name, PyObject *globals, PyObject *locals, PyObject *fromlist)
    *Retorna valor: Nova referência.*

   Importa um módulo. Isso é melhor descrito referindo-se à função
   embutida do Python "__import__()".

   O valor de retorno é uma nova referência ao módulo importado ou
   pacote de nível superior, ou "NULL" com uma exceção definida em
   caso de falha. Como para "__import__()", o valor de retorno quando
   um submódulo de um pacote é solicitado é normalmente o pacote de
   nível superior, a menos que um *fromlist* não vazio seja fornecido.

   As importações com falhas removem objetos incompletos do módulo,
   como em "PyImport_ImportModule()".

PyObject *PyImport_ImportModuleLevelObject(PyObject *name, PyObject *globals, PyObject *locals, PyObject *fromlist, int level)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Importa um módulo. Isso é melhor descrito referindo-se à função
   embutida do Python "__import__()", já que a função padrão
   "__import__()" chama essa função diretamente.

   O valor de retorno é uma nova referência ao módulo importado ou
   pacote de nível superior, ou "NULL" com uma exceção definida em
   caso de falha. Como para "__import__()", o valor de retorno quando
   um submódulo de um pacote é solicitado é normalmente o pacote de
   nível superior, a menos que um *fromlist* não vazio seja fornecido.

   Adicionado na versão 3.3.

PyObject *PyImport_ImportModuleLevel(const char *name, PyObject *globals, PyObject *locals, PyObject *fromlist, int level)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Semelhante para "PyImport_ImportModuleLevelObject()", mas o nome é
   uma string codificada em UTF-8 de um objeto Unicode.

   Alterado na versão 3.3: Valores negativos para *level* não são mais
   aceitos.

PyObject *PyImport_Import(PyObject *name)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Essa é uma interface de alto nível que chama a atual "função
   auxiliar de importação" (com um *level* explícito de 0,
   significando importação absoluta). Invoca a função "__import__()" a
   partir de "__builtins__" da global atual. Isso significa que a
   importação é feita usando quaisquer extras de importação instalados
   no ambiente atual.

   Esta função sempre usa importações absolutas.

PyObject *PyImport_ReloadModule(PyObject *m)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Recarrega um módulo. Retorna uma nova referência para o módulo
   recarregado, ou "NULL" com uma exceção definida em caso de falha (o
   módulo ainda existe neste caso).

PyObject *PyImport_AddModuleRef(const char *name)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.13.*

   Retorna o objeto do módulo correspondente ao nome do módulo.

   O argumento *name* pode ter o formato "pacote.módulo". Primeiro,
   verifica se existe um módulo no dicionário de módulos e, caso
   contrário, cria um novo e insere-o no dicionário de módulos.

   Retorna uma *referência forte* ao módulo em caso de sucesso.
   Retorna "NULL" com uma exceção definida em caso de falha.

   O nome do módulo *name* é decodificado de UTF-8.

   Esta função não carrega nem importa o módulo; se o módulo ainda não
   estiver carregado, você receberá um objeto de módulo vazio. Use
   "PyImport_ImportModule()" ou uma de suas variantes para importar um
   módulo. Estruturas de pacotes implícitas por um nome com pontos
   para *name* não são criadas se ainda não existirem.

   Adicionado na versão 3.13.

PyObject *PyImport_AddModuleObject(PyObject *name)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável
   desde a versão 3.7.*

   Semelhante a "PyImport_AddModuleRef()", mas retorna uma *referência
   emprestada* e *name* é um objeto Python "str".

   Adicionado na versão 3.3.

PyObject *PyImport_AddModule(const char *name)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Semelhante a "PyImport_AddModuleRef()", mas retorna uma *referência
   emprestada*.

PyObject *PyImport_ExecCodeModule(const char *name, PyObject *co)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Dado um nome de módulo (possivelmente no formato "pacote.módulo") e
   um objeto código lido de um arquivo bytecode Python ou obtido da
   função embutida "compile()", carrea o módulo. Retorna uma nova
   referência ao objeto do módulo ou "NULL" com uma exceção definida
   se ocorrer um erro. *name* é removido de "sys.modules" em casos de
   erro, mesmo que *name* já estivesse em "sys.modules" na entrada de
   "PyImport_ExecCodeModule()". Deixar módulos incompletamente
   inicializados em "sys.modules" é perigoso, pois as importações
   desses módulos não têm como saber que o objeto do módulo está em um
   estado desconhecido (e provavelmente corrompido em relação às
   intenções do autor do módulo).

   Os atributos "__spec__" e "__loader__" do módulo serão definidos,
   caso ainda não estejam, com os valores apropriados. O carregador do
   spec será definido como o atributo "__loader__" do módulo (se
   definido) e, caso contrário, como uma instância de
   "SourceFileLoader".

   The module's "__file__" attribute will be set to the code object's
   "co_filename".

   Esta função recarregará o módulo se este já tiver sido importado.
   Veja "PyImport_ReloadModule()" para forma desejada de recarregar um
   módulo.

   Se *name* apontar para um nome pontilhado no formato de
   "package.module", quaisquer estruturas de pacote ainda não criadas
   ainda não serão criadas.

   Veja também "PyImport_ExecCodeModuleEx()" e
   "PyImport_ExecCodeModuleWithPathnames()".

   Alterado na versão 3.12: The setting of "__cached__" and
   "__loader__" is deprecated. See "ModuleSpec" for alternatives.

   Alterado na versão 3.15: The "__cached__" attribute is no longer
   set.

PyObject *PyImport_ExecCodeModuleEx(const char *name, PyObject *co, const char *pathname)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Como "PyImport_ExecCodeModule()", mas o atributo "__file__" do
   objeto módulo é definido como *pathname*  se não for "NULL".

   Veja também "PyImport_ExecCodeModuleWithPathnames()".

PyObject *PyImport_ExecCodeModuleObject(PyObject *name, PyObject *co, PyObject *pathname, PyObject *cpathname)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Like "PyImport_ExecCodeModuleEx()", but the path to any compiled
   file via *cpathname* is used appropriately when non-"NULL".  Of the
   three functions, this is the preferred one to use.

   Adicionado na versão 3.3.

   Alterado na versão 3.12: Setting "__cached__" is deprecated. See
   "ModuleSpec" for alternatives.

   Alterado na versão 3.15: The "__cached__" attribute no longer set.

PyObject *PyImport_ExecCodeModuleWithPathnames(const char *name, PyObject *co, const char *pathname, const char *cpathname)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Como "PyImport_ExecCodeModuleObject()", mas *name*, *pathname* e
   *cpathname* são strings codificadas em UTF-8. Também são feitas
   tentativas para descobrir qual valor para *pathname* deve ser de
   *cpathname* se o primeiro estiver definido como "NULL".

   Adicionado na versão 3.2.

   Alterado na versão 3.3: Usa "imp.source_from_cache()" no cálculo do
   caminho de origem se apenas o caminho do bytecode for fornecido.

   Alterado na versão 3.12: Não usa mais o módulo "imp" removido.

long PyImport_GetMagicNumber()
    * Parte da ABI Estável.*

   Retorna o número mágico para arquivos de bytecode Python (também
   conhecido como arquivo ".pyc"). O número mágico deve estar presente
   nos primeiros quatro bytes do arquivo bytecode, na ordem de bytes
   little-endian. Retorna "-1" em caso de erro.

   Alterado na versão 3.3: Retorna o valor de "-1" no caso de falha.

const char *PyImport_GetMagicTag()
    * Parte da ABI Estável.*

   Retorna a string de tag mágica para nomes de arquivo de bytecode
   Python no formato de **PEP 3147**. Tenha em mente que o valor em
   "sys.implementation.cache_tag" é autoritativo e deve ser usado no
   lugar desta função.

   Adicionado na versão 3.2.

PyObject *PyImport_GetModuleDict()
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Retorna o dicionário usado para a administração do módulo (também
   conhecido como "sys.modules"). Observe que esta é uma variável por
   interpretador.

PyObject *PyImport_GetModule(PyObject *name)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.8.*

   Retorna o módulo já importado com o nome fornecido. Se o módulo
   ainda não foi importado, retorna "NULL", mas não define um erro.
   Retorna "NULL" e define um erro se a pesquisa falhar.

   Adicionado na versão 3.7.

PyObject *PyImport_GetImporter(PyObject *path)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return a finder object for a "sys.path"/"pkg.__path__" item *path*,
   possibly by fetching it from the "sys.path_importer_cache" dict.
   If it wasn't yet cached, traverse "sys.path_hooks" until a hook is
   found that can handle the path item.  Return "None" if no hook
   could; this tells our caller that the *path based finder* could not
   find a finder for this path item. Cache the result in
   "sys.path_importer_cache". Return a new reference to the finder
   object.

int PyImport_ImportFrozenModuleObject(PyObject *name)
    * Parte da ABI Estável desde a versão 3.7.*

   Carrega um módulo congelado chamado *name*. Retorna "1" para
   sucesso, "0" se o módulo não for encontrado e "-1" com uma exceção
   definida se a inicialização falhar. Para acessar o módulo importado
   em um carregamento bem-sucedido, use "PyImport_ImportModule()".
   (Observe o nome incorreto --- esta função recarregaria o módulo se
   ele já tivesse sido importado.)

   Adicionado na versão 3.3.

   Alterado na versão 3.4: O atributo "__file__" não está mais
   definido no módulo.

int PyImport_ImportFrozenModule(const char *name)
    * Parte da ABI Estável.*

   Semelhante a "PyImport_ImportFrozenModuleObject()", mas o nome é
   uma string codificada em UTF-8 em vez de um objeto Unicode.

struct _frozen

   This is the structure type definition for frozen module
   descriptors, as generated by the **freeze** utility (see
   "Tools/freeze/" in the Python source distribution).  Its
   definition, found in "Include/import.h", is:

      struct _frozen {
          const char *name;                 /* ASCII encoded string */
          const unsigned char *code;
          int size;
          int is_package;
      };

   Alterado na versão 3.11: O novo campo "is_package" indica se o
   módulo é um pacote ou não. Isso substitui a configuração do campo
   "size" para um valor negativo.

const struct _frozen *PyImport_FrozenModules

   Este ponteiro é inicializado para apontar para um vetor de
   registros de "_frozen", terminado por um cujos membros são todos
   "NULL" ou zero. Quando um módulo congelado é importado, ele é
   pesquisado nesta tabela. O código de terceiros pode fazer truques
   com isso para fornecer uma coleção criada dinamicamente de módulos
   congelados.

int PyImport_AppendInittab(const char *name, PyObject *(*initfunc)(void))
    * Parte da ABI Estável.*

   Adiciona um único módulo à tabela existente de módulos embutidos.
   Este é um invólucro prático em torno de "PyImport_ExtendInittab()",
   retornando "-1" se a tabela não puder ser estendida. O novo módulo
   pode ser importado pelo nome *name* e usa a função *initfunc* como
   a função de inicialização chamada na primeira tentativa de
   importação. Deve ser chamado antes de "Py_Initialize()".

struct _inittab

   Structure describing a single entry in the list of built-in
   modules. Programs which embed Python may use an array of these
   structures in conjunction with "PyImport_ExtendInittab()" to
   provide additional built-in modules. The structure consists of two
   members:

   const char *name

      The module name, as an ASCII encoded string.

   PyObject *(*initfunc)(void)

      Initialization function for a module built into the interpreter.

      Note that the inittab uses ""PyInit"" initialization functions;
      there is currently no way to include ""PyModExport_"" export
      hooks.

int PyImport_ExtendInittab(struct _inittab *newtab)

   Add a collection of modules to the table of built-in modules.  The
   *newtab* array must end with a sentinel entry which contains "NULL"
   for the "name" field; failure to provide the sentinel value can
   result in a memory fault. Returns "0" on success or "-1" if
   insufficient memory could be allocated to extend the internal
   table.  In the event of failure, no modules are added to the
   internal table.  This must be called before "Py_Initialize()".

   Se Python é inicializado várias vezes, "PyImport_AppendInittab()"
   ou "PyImport_ExtendInittab()" devem ser chamados antes de cada
   inicialização do Python.

struct _inittab *PyImport_Inittab

   The table of built-in modules used by Python initialization. Do not
   use this directly; use "PyImport_AppendInittab()" and
   "PyImport_ExtendInittab()" instead.

PyObject *PyImport_ImportModuleAttr(PyObject *mod_name, PyObject *attr_name)
    *Retorna valor: Nova referência.*

   Import the module *mod_name* and get its attribute *attr_name*.

   Names must be Python "str" objects.

   Helper function combining "PyImport_Import()" and
   "PyObject_GetAttr()". For example, it can raise "ImportError" if
   the module is not found, and "AttributeError" if the attribute
   doesn't exist.

   Adicionado na versão 3.14.

PyObject *PyImport_ImportModuleAttrString(const char *mod_name, const char *attr_name)
    *Retorna valor: Nova referência.*

   Similar to "PyImport_ImportModuleAttr()", but names are UTF-8
   encoded strings instead of Python "str" objects.

   Adicionado na versão 3.14.

PyImport_LazyImportsMode PyImport_GetLazyImportsMode()

   Gets the current lazy imports mode.

   Adicionado na versão 3.15.

PyObject *PyImport_GetLazyImportsFilter()

   Return a *strong reference* to the current lazy imports filter, or
   "NULL" if none exists. This function always succeeds.

   Adicionado na versão 3.15.

int PyImport_SetLazyImportsMode(PyImport_LazyImportsMode mode)

   Sets the current lazy imports mode.

   This function always returns "0".

   Adicionado na versão 3.15.

int PyImport_SetLazyImportsFilter(PyObject *filter)

   Sets the current lazy imports filter. The *filter* should be a
   callable that will receive "(importing_module_name,
   imported_module_name, [fromlist])" when an import can potentially
   be lazy. The "imported_module_name" value is the resolved module
   name, so "lazy from .spam import eggs" passes "package.spam". The
   callable must return "True" if the import should be lazy and
   "False" otherwise.

   Return "0" on success and "-1" with an exception set otherwise.

   Adicionado na versão 3.15.

type PyImport_LazyImportsMode

   Enumeration of possible lazy import modes.

   enumerator PyImport_LAZY_NORMAL

      Respect the "lazy" keyword in source code. This is the default
      mode.

   enumerator PyImport_LAZY_ALL

      Make all imports lazy by default.

   Adicionado na versão 3.15.

PyObject *PyImport_CreateModuleFromInitfunc(PyObject *spec, PyObject *(*initfunc)(void))

   This function is a building block that enables embedders to
   implement the "create_module()" step of custom static extension
   importers (e.g. of statically-linked extensions).

   *spec* must be a "ModuleSpec" object.

   *initfunc* must be an initialization function, the same as for
   "PyImport_AppendInittab()".

   On success, create and return a module object. This module will not
   be initialized; call "PyModule_Exec()" to initialize it. (Custom
   importers should do this in their "exec_module()" method.)

   On error, return NULL with an exception set.

   For modules using legacy single-phase initialization, most of the
   import process is done in this function, rather than in extra steps
   that importers typically take after "create_module()".
   Specifically:

   * The module is added to "sys.modules" under the *spec*'s "name" as
     part of initialization.

   * If a single-phase module was previously imported under the same
     "name" by this function or as a built-in module (for example, one
     registered with "PyImport_AppendInittab()"), Python may reuse the
     previous module's contents instead of calling *initfunc* again.

   * The module will be fully initialized by *initfunc*. Calling
     "PyModule_Exec()" on it will have no effect, though it is still
     recommended, in case the module later switches to multi-phase
     initialization.

   * Also, if the *spec*'s "name" contains dots, this name is used for
     prepending a parent package to the new module's "__name__".

   Adicionado na versão 3.15.
