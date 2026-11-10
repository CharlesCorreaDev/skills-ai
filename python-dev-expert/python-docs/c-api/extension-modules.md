Definindo módulos de extensão
*****************************

A C extension for CPython is a shared library (for example, a ".so"
file on Linux, ".pyd" DLL on Windows), which is loadable into the
Python process (for example, it is compiled with compatible compiler
settings), and which exports an *export hook* function (or an old-
style initialization function).

Para ser importável por padrão (ou seja, por
"importlib.machinery.ExtensionFileLoader"), a biblioteca compartilhada
deve estar disponível em "sys.path" e deve ser nomeada após o nome do
módulo mais uma extensão listada em
"importlib.machinery.EXTENSION_SUFFIXES".

Nota:

  A construção, o empacotamento e a distribuição de módulos de
  extensão são melhor realizados com ferramentas de terceiros e estão
  fora do escopo deste documento. Uma ferramenta adequada é o
  Setuptools, cuja documentação pode ser encontrada em
  https://setuptools.pypa.io/en/latest/setuptools.html.


Extension export hook
=====================

Adicionado na versão 3.15: Support for the "PyModExport_*<name>*"
export hook was added in Python 3.15. The older way of defining
modules is still available: consult either the PyInit function section
or earlier versions of this documentation if you plan to support
earlier Python versions.

The export hook must be an exported function with the following
signature:

PySlot *PyModExport_modulename(void)

For modules with ASCII-only names, the export hook must be named
"PyModExport_*<name>*", with "<name>" replaced by the module's name.

For non-ASCII module names, the export hook must instead be named
"PyModExportU_*<name>*" (note the "U"), with "<name>" encoded using
Python's *punycode* encoding with hyphens replaced by underscores. In
Python:

   def hook_name(name):
       try:
           suffix = b'_' + name.encode('ascii')
       except UnicodeEncodeError:
           suffix = b'U_' + name.encode('punycode').replace(b'-', b'_')
       return b'PyModExport' + suffix

The export hook returns an array of "PySlot" entries, terminated by an
entry with a slot ID of "0". These slots describe how the module
should be created and initialized.

This array must remain valid and constant until interpreter shutdown.
Typically, it should use "static" storage. Prefer using the
"Py_mod_create" and "Py_mod_exec" slots for any dynamic behavior.

The export hook may return "NULL" with an exception set to signal
failure.

It is recommended to define the export hook function using a helper
macro:

PyMODEXPORT_FUNC
    * This macro is available when compiling for the ABI Estável desde
   a versão 3.15.*

   Declare an extension module export hook. This macro:

   * specifies the PySlot* return type,

   * adiciona quaisquer declarações de vinculação especiais exigidas
     pela plataforma e

   * para C++, declara a função como "extern "C"".

Por exemplo, um módulo chamado "spam" seria definido assim:

   PyABIInfo_VAR(abi_info);

   static PySlot spam_slots[] = {
       PySlot_STATIC_DATA(Py_mod_abi, &abi_info),
       PySlot_STATIC_DATA(Py_mod_name, "spam"),
       PySlot_FUNC(Py_mod_exec, spam_init_function),
       ...
       PySlot_END
   };

   PyMODEXPORT_FUNC
   PyModExport_spam(void)
   {
       return spam_slots;
   }

The export hook is typically the only non-"static" item defined in the
module's C source.

The hook should be kept short. If it does more than "return" a static
array, several caveats apply:

* If you need to use any Python C API, it is recommended to call
  "PyABIInfo_Check()" first to raise an exception, rather than crash,
  in common cases of ABI mismatch.

* Code in the export hook must never rely on the *GIL*: *free-threaded
  builds* of Python can only check the "Py_mod_gil" slot (or the lack
  of it) after the hook returns,

* Similarly, the hook may be called in any subinterpreter, since the
  "Py_mod_multiple_interpreters" slot (or lack of it) is only checked
  after the hook returns.

Por exemplo:

   PyMODEXPORT_FUNC
   PyModExport_modulename(void)
   {
      if (PyABIInfo_Check(&abi_info, "modulename") < 0) {
         /* ABI mismatch. It's not safe to examine the raised exception. */
         return NULL;
      }

      /* use Python API (as little as possible); don't rely on GIL */

      return modulename_slots;
   }

Nota:

  It is possible to export multiple modules from a single shared
  library by defining multiple export hooks. However, importing  them
  requires a custom importer or suitably named copies/links of the
  extension file, because Python's import machinery only finds the
  function corresponding to the filename. See the Multiple modules in
  one library section in **PEP 489** for details.


Inicialização multifásica
=========================

The process of creating an extension module follows several phases:

* Python finds and calls the export hook to get information on how to
  create the module.

* Before any substantial code is executed, Python can determine which
  capabilities the module supports, and it can adjust the environment
  or refuse loading an incompatible extension. Slots like
  "Py_mod_abi", "Py_mod_gil" and "Py_mod_multiple_interpreters"
  influence this step.

* By default, Python itself then creates the module object -- that is,
  it does the equivalent of calling "__new__()" when creating an
  object. This step can be overridden using the "Py_mod_create" slot.

* Python sets initial module attributes like "__package__" and
  "__loader__", and inserts the module object into "sys.modules".

* Afterwards, the module object is initialized in an extension-
  specific way -- the equivalent of "__init__()" when creating an
  object, or of executing top-level code in a Python-language module.
  The behavior is specified using the "Py_mod_exec" slot.

This is called *multi-phase initialization* to distinguish it from the
legacy (but still supported) single-phase initialization, where an
initialization function returns a fully constructed module.

Alterado na versão 3.5: Adicionado suporte para inicialização
multifásica (**PEP 489**).


Várias instâncias de módulo
===========================

By default, extension modules are not singletons. For example, if the
"sys.modules" entry is removed and the module is re-imported, a new
module object is created and, typically, populated with fresh method
and type objects. The old module is subject to normal garbage
collection. This mirrors the behavior of pure-Python modules.

Instâncias adicionais do módulo podem ser criadas em
subinterpretadores ou após a reinicialização do tempo de execução do
Python ("Py_Finalize()" e "Py_Initialize()"). Nesses casos,
compartilhar objetos Python entre instâncias do módulo provavelmente
causaria travamentos ou comportamento indefinido.

Para evitar tais problemas, cada instância de um módulo de extensão
deve ser *isolada*: alterações em uma instância não devem afetar
implicitamente as outras, e todos os estados pertencentes ao módulo,
incluindo referências a objetos Python, devem ser específicos de uma
instância específica do módulo. Consulte Isolando módulos de extensão
para obter mais detalhes e um guia prático.

Uma maneira mais simples de evitar esses problemas é levantar um erro
na inicialização repetida.

Espera-se que todos os módulos ofereçam suporte a subinterpretador, ou
então sinalizem explicitamente a falta de suporte. Isso geralmente é
obtido por isolamento ou bloqueio de inicializações repetidas, como
acima. Um módulo também pode ser limitado ao interpretador principal
usando o slot "Py_mod_multiple_interpreters".


"PyInit" function
=================

Suavemente descontinuado desde a versão 3.15: This functionality will
not get new features, but there are no plans to remove it.

Instead of "PyModExport_modulename()", an extension module can define
an older-style *initialization function* with the signature:

PyObject *PyInit_modulename(void)

Its name should be "PyInit_*<name>*", with "<name>" replaced by the
name of the module. For non-ASCII module names, use "PyInitU_*<name>*"
instead, with "<name>" encoded in the same way as for the export hook
(that is, using Punycode with underscores).

If a module exports both "PyInit_*<name>*" and "PyModExport_*<name>*",
the "PyInit_*<name>*" function is ignored.

Like with "PyMODEXPORT_FUNC", it is recommended to define the
initialization function using a helper macro:

PyMODINIT_FUNC

   Declara uma função de inicialização do módulo de extensão. Esta
   macro:

   * especifica o tipo de retorno PyObject*,

   * adiciona quaisquer declarações de vinculação especiais exigidas
     pela plataforma e

   * para C++, declara a função como "extern "C"".

Normally, the initialization function ("PyInit_modulename") returns a
"PyModuleDef" instance with non-"NULL" "m_slots". This allows Python
to use multi-phase initialization.

Before it is returned, the "PyModuleDef" instance must be initialized
using the following function:

PyObject *PyModuleDef_Init(PyModuleDef *def)
    * Parte da ABI Estável desde a versão 3.5.*

   Garante que uma definição de módulo é um objeto Python devidamente
   inicializado que reporta corretamente seu tipo e uma contagem de
   referências.

   Retorna *def* convertido para "PyObject*", ou "NULL" se ocorrer um
   erro.

   Calling this function is required before returning a "PyModuleDef"
   from a module initialization function. It should not be used in
   other contexts.

   Observe que o Python assume que as estruturas "PyModuleDef" são
   alocadas estaticamente. Esta função pode retornar uma nova
   referência ou uma referência emprestada; esta referência não deve
   ser liberada.

   Adicionado na versão 3.5.

Por exemplo, um módulo chamado "spam" seria definido assim:

   static struct PyModuleDef spam_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "spam",
       ...
   };

   PyMODINIT_FUNC
   PyInit_spam(void)
   {
       return PyModuleDef_Init(&spam_module);
   }


Inicialização monofásica legada
-------------------------------

Suavemente descontinuado desde a versão 3.15: A inicialização
monofásica é um mecanismo legado para inicializar módulos de extensão,
com desvantagens e falhas de projeto conhecidas. Os autores de módulos
de extensão são incentivados a utilizar a inicialização
multifásica.However, there are no plans to remove support for it.

In single-phase initialization, the old-style initialization function
("PyInit_modulename") should create, populate and return a module
object. This is typically done using "PyModule_Create()" and functions
like "PyModule_AddObjectRef()".

A inicialização monofásica difere do padrão nas seguintes maneiras:

* Single-phase modules with "PyModuleDef.m_size" set to -1 are, or
  rather *contain*, “singletons”.

  When such a module is first initialized, Python saves the contents
  of the module's "__dict__" (that is, typically, the module's
  functions and types).

  For subsequent imports, Python does not call the initialization
  function again. Instead, it creates a new module object with a new
  "__dict__", and copies the saved contents to it. Modules are matched
  to the saved contents by a (*module_name*, *file_name*) tuple where:

  * *module_name* is the module's full dotted name, taken from
    "ModuleSpec.name" (or the equivalent argument of the importing
    function). Note that names that the initialization function uses
    to create the module (for example, "PyModuleDef.m_name") are not
    taken into account.

  * *file_name* is the extension's file name. It is unset for modules
    not loaded from a file, such as built-ins and modules added with
    "PyImport_CreateModuleFromInitfunc()" or
    "PyImport_AppendInittab()".

  As part of the first initialization, Python also adds the module to
  "sys.modules" under its name. For example, given a single-phase
  module "_testsinglephase" [1] that defines a function "sum" and an
  exception class "error":

     >>> import sys
     >>> import _testsinglephase as one
     >>> del sys.modules['_testsinglephase']
     >>> import _testsinglephase as two
     >>> one is two
     False
     >>> one.__dict__ is two.__dict__
     False
     >>> one.sum is two.sum
     True
     >>> one.error is two.error
     True

  O comportamento exato deve ser considerado um detalhe da
  implementação do CPython.

* For single-phase modules with non-negative "PyModuleDef.m_size",
  Python may cache a pointer to the initialization function under the
  (*module_name*, *file_name*) key as for "m_size == -1".

  Subsequent imports that specify a different initialization function
  (for example, using "PyImport_CreateModuleFromInitfunc()") may call
  either the cached function or the provided "new" one.

  The exact behavior should again be considered a CPython
  implementation detail.

* Para contornar o fato de que "PyInit_modulename" não aceita um
  argumento *spec*, parte do estado do mecanismo de importação é salvo
  e aplicado ao primeiro módulo adequado criado durante a chamada
  "PyInit_modulename". Especificamente, quando um submódulo é
  importado, esse mecanismo adiciona o nome do pacote pai ao nome do
  módulo.

  Uma função monofásica "PyInit_modulename" deve criar “seu” objeto de
  módulo o mais rápido possível, antes que qualquer outro objeto de
  módulo possa ser criado.

* Nomes de módulos não ASCII ("PyInitU_modulename") não são
  suportados.

* Módulos monofásicos oferecem suporte a funções de pesquisa de
  módulos como "PyState_FindModule()".

* The module's "PyModuleDef.m_slots" must be NULL.

[1] "_testsinglephase" é um módulo interno usado no conjunto de
    autotestes do CPython; sua instalação pode ou não incluí-lo.
