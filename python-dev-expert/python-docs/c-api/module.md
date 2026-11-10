Objetos do Módulo
*****************

PyTypeObject PyModule_Type
    * Parte da ABI Estável.*

   This instance of "PyTypeObject" represents the Python module type.
   This is exposed to Python programs as "types.ModuleType".

int PyModule_Check(PyObject *p)

   Retorna true se *p* for um objeto de módulo ou um subtipo de um
   objeto de módulo. Esta função sempre é bem-sucedida.

int PyModule_CheckExact(PyObject *p)

   Retorna true se *p* for um objeto de módulo, mas não um subtipo de
   "PyModule_Type". Essa função é sempre bem-sucedida.

PyObject *PyModule_NewObject(PyObject *name)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Retorna um novo objeto de módulo com "module.__name__" definido
   como *name*. Os atributos "__name__", "__doc__", "__package__" e
   "__loader__" do módulo são preenchidos (todos, exceto "__name__",
   são definidos como "None"). O chamador é responsável por definir um
   atributo "__file__".

   Retorna "NULL" com uma exceção definida em caso de erro.

   Adicionado na versão 3.3.

   Alterado na versão 3.4: "__package__" e "__loader__" agora estão
   definidos como "None".

PyObject *PyModule_New(const char *name)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Semelhante a "PyModule_NewObject()", mas o nome é uma string
   codificada em UTF-8 em vez de um objeto Unicode.

PyObject *PyModule_GetDict(PyObject *module)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Retorna o objeto dicionário que implementa o espaço de nomes de
   *module*; este objeto é o mesmo que o atributo "__dict__" do objeto
   de módulo. Se *module* não for um objeto de módulo (ou um subtipo
   de um objeto de módulo), "SystemError" é levantada e "NULL" é
   retornado.

   É recomendado que as extensões usem outras funções "PyModule_*" e
   "PyObject_*" em vez de manipular diretamente o "__dict__" de um
   módulo.

   The returned reference is borrowed from the module; it is valid
   until the module is destroyed.

PyObject *PyModule_GetNameObject(PyObject *module)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Retorna o valor "__name__" do *module*. Se o módulo não fornecer
   um, ou se não for uma string, "SystemError" é levantada e "NULL" é
   retornado.

   Adicionado na versão 3.3.

const char *PyModule_GetName(PyObject *module)
    * Parte da ABI Estável.*

   Semelhante a "PyModule_GetNameObject()" mas retorna o nome
   codificado em "'utf-8'"

   The returned buffer is only valid until the module is renamed or
   destroyed. Note that Python code may rename a module by setting its
   "__name__" attribute.

PyModuleDef *PyModule_GetDef(PyObject *module)
    * Parte da ABI Estável.*

   Retorna um ponteiro para a estrutura "PyModuleDef" da qual o módulo
   foi criado, ou "NULL" se o módulo não foi criado de uma definição.

   On error, return "NULL" with an exception set. Use
   "PyErr_Occurred()" to tell this case apart from a missing
   "PyModuleDef".

PyObject *PyModule_GetFilenameObject(PyObject *module)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o nome do arquivo do qual o *module* foi carregado usando o
   atributo "__file__" do *module*. Se não estiver definido, ou se não
   for uma string unicode, levanta "SystemError" e retorna "NULL";
   Caso contrário, retorna uma referência a um objeto Unicode.

   Adicionado na versão 3.2.

const char *PyModule_GetFilename(PyObject *module)
    * Parte da ABI Estável.*

   Semelhante a "PyModule_GetFilenameObject()" mas retorna o nome do
   arquivo codificado em 'utf-8'.

   The returned buffer is only valid until the module's "__file__"
   attribute is reassigned or the module is destroyed.

   Descontinuado desde a versão 3.2: "PyModule_GetFilename()": levanta
   "UnicodeEncodeError" quando há nomes de arquivos não codificáveis,
   use "PyModule_GetFilenameObject()".


Module definition
=================

Modules created using the C API are typically defined using an array
of "PySlot" structs, which provides a "description" of how a module
should be created. See Slots de definição for more information on
slots in general.

Alterado na versão 3.15: Previously, a "PyModuleDef" struct was
necessary to define modules. The older way of defining modules is
still available: consult either the Module definition struct section
or earlier versions of this documentation if you plan to support
earlier Python versions.

The slots array is usually used to define an extension module's “main”
module object (see Definindo módulos de extensão for details). It can
also be used to create extension modules dynamically.

Unless specified otherwise, the same slot ID may not be repeated in an
array of slots.


Metadata slots
--------------

Py_mod_name
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for the name of the new module, as a NUL-terminated
   UTF8-encoded "const char *".

   Note that modules are typically created using a "ModuleSpec", and
   when they are, the name from the spec will be used instead of
   "Py_mod_name". However, it is still recommended to include this
   slot for introspection and debugging purposes.

   Adicionado na versão 3.15: Use "PyModuleDef.m_name" instead to
   support previous versions.

Py_mod_doc
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for the docstring of the new module, as a NUL-terminated
   UTF8-encoded "const char *".

   Usually it is set to a variable created with "PyDoc_STRVAR".

   Adicionado na versão 3.15: Use "PyModuleDef.m_doc" instead to
   support previous versions.


Feature slots
-------------

Py_mod_abi
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" whose value points to a "PyABIInfo" structure describing
   the ABI that the extension is using.

   A suitable "PyABIInfo" variable can be defined using the
   "PyABIInfo_VAR" macro, as in:

      PyABIInfo_VAR(abi_info);

      static PySlot mymodule_slots[] = {
         PySlot_DATA(Py_mod_abi, &abi_info),
         ...
      };

   When creating a module, Python checks the value of this slot using
   "PyABIInfo_Check()".

   This slot is required, except for modules created from
   "PyModuleDef".

   Adicionado na versão 3.15.

Py_mod_multiple_interpreters
    * Parte da ABI Estável desde a versão 3.12.*

   "Slot ID" whose value is one of:

   Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED

      The module does not support being imported in subinterpreters.

   Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED

      The module supports being imported in subinterpreters, but only
      when they share the main interpreter's GIL. (See Isolando
      módulos de extensão.)

   Py_MOD_PER_INTERPRETER_GIL_SUPPORTED

      The module supports being imported in subinterpreters, even when
      they have their own GIL. (See Isolando módulos de extensão.)

   This slot determines whether or not importing this module in a
   subinterpreter will fail.

   If "Py_mod_multiple_interpreters" is not specified, the import
   machinery defaults to "Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED".

   For historical reasons, the values are declared as pointers ("void
   *"). When using "PySlot" arrays, use "PySlot_DATA" for
   "Py_mod_multiple_interpreters":

      PySlot_DATA(Py_mod_multiple_interpreters,
                  Py_MOD_PER_INTERPRETER_GIL_SUPPORTED)

   Adicionado na versão 3.12.

Py_mod_gil
    * Parte da ABI Estável desde a versão 3.13.*

   "Slot ID" whose value is one of:

   Py_MOD_GIL_USED

      The module depends on the presence of the global interpreter
      lock (GIL), and may access global state without synchronization.

   Py_MOD_GIL_NOT_USED

      The module is safe to run without an active GIL.

   This slot is ignored by Python builds not configured with "--
   disable-gil".  Otherwise, it determines whether or not importing
   this module will cause the GIL to be automatically enabled. See
   CPython com threads livres for more detail.

   If "Py_mod_gil" is not specified, the import machinery defaults to
   "Py_MOD_GIL_USED".

   For historical reasons, the values are declared as pointers ("void
   *"). When using "PySlot" arrays, use "PySlot_DATA" for
   "Py_mod_gil":

      PySlot_DATA(Py_mod_gil, Py_MOD_GIL_NOT_USED)

   Adicionado na versão 3.13.


Creation and initialization slots
---------------------------------

Py_mod_create
    * Parte da ABI Estável desde a versão 3.5.*

   "Slot ID" for a function that creates the module object itself. The
   function must have the signature:

   PyObject *create_module(PyObject *spec, PyModuleDef *def)

   The function will be called with:

   * *spec*: a "ModuleSpec"-like object, meaning that any attributes
     defined for "importlib.machinery.ModuleSpec" have matching
     semantics. However, any of the attributes may be missing.

   * *def*: "NULL", or the module definition if the module is created
     from one.

   The function should return a new module object, or set an error and
   return "NULL".

   This function should be kept minimal. In particular, it should not
   call arbitrary Python code, as trying to import the same module
   again may result in an infinite loop.

   If "Py_mod_create" is not specified, the import machinery will
   create a normal module object using "PyModule_New()". The name is
   taken from *spec*, not the definition, to allow extension modules
   to dynamically adjust to their place in the module hierarchy and be
   imported under different names through symlinks, all while sharing
   a single module definition.

   There is no requirement for the returned object to be an instance
   of "PyModule_Type". However, some slots may only be used with
   "PyModule_Type" instances; in particular:

   * "Py_mod_exec",

   * module state slots ("Py_mod_state_*"),

   * "Py_mod_token".

   Adicionado na versão 3.5.

   Alterado na versão 3.15: The *slots* argument may be a
   "ModuleSpec"-like object, rather than a true "ModuleSpec" instance.
   Note that previous versions of CPython did not enforce this.The
   *def* argument may now be "NULL", since modules are not necessarily
   made from definitions.

Py_mod_exec
    * Parte da ABI Estável desde a versão 3.5.*

   "Slot ID" for a function that will *execute*, or initialize, the
   module. This function does the equivalent to executing the code of
   a Python module: typically, it adds classes and constants to the
   module. The signature of the function is:

   int exec_module(PyObject *module)

   See the Support functions section for some useful functions to
   call.

   For backwards compatibility, the "PyModuleDef.m_slots" array may
   contain multiple "Py_mod_exec" slots; these are processed in the
   order they appear in the array. Elsewhere (that is, in arguments to
   "PyModule_FromSlotsAndSpec()" and in return values of
   "PyModExport_*<name>*"), repeating the slot is not allowed.

   Adicionado na versão 3.5.

   Alterado na versão 3.15: Repeated "Py_mod_exec" slots are
   disallowed, except in "PyModuleDef.m_slots".

Py_mod_methods
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for a table of module-level functions, as an array of
   "PyMethodDef" values suitable as the *functions* argument to
   "PyModule_AddFunctions()".

   Like other slot IDs, a slots array may only contain one
   "Py_mod_methods" entry. To add functions from multiple
   "PyMethodDef" arrays, call "PyModule_AddFunctions()" in the
   "Py_mod_exec" function.

   The table must be statically allocated (or otherwise guaranteed to
   outlive the module object).

   Adicionado na versão 3.15: Use "PyModuleDef.m_methods" instead to
   support previous versions.


Module state
============

Extension modules can have *module state* -- a piece of memory that is
allocated on module creation, and freed when the module object is
deallocated. The module state is specified using dedicated slots.

A typical use of module state is storing an exception type -- or
indeed *any* type object defined by the module --

Unlike the module's Python attributes, Python code cannot replace or
delete data stored in module state.

Keeping per-module information in attributes and module state, rather
than in static globals, makes module objects *isolated* and safer for
use in multiple sub-interpreters. It also helps Python do an orderly
clean-up when it shuts down.

Extensions that keep references to Python objects as part of module
state must implement "Py_mod_state_traverse" and "Py_mod_state_clear"
functions to avoid reference leaks.

To retrieve the state from a given module, use the following
functions:

void *PyModule_GetState(PyObject *module)
    * Parte da ABI Estável.*

   Return the "state" of the module, that is, a pointer to the block
   of memory allocated at module creation time, or "NULL".  See
   "Py_mod_state_size".

   On error, return "NULL" with an exception set. Use
   "PyErr_Occurred()" to tell this case apart from missing module
   state.

int PyModule_GetStateSize(PyObject *module, Py_ssize_t *result)
    * Parte da ABI Estável desde a versão 3.15.*

   Set **result* to the size of *module*'s state, as specified using
   "Py_mod_state_size" (or "PyModuleDef.m_size"), and return 0.

   On error, set **result* to -1, and return -1 with an exception set.

   Adicionado na versão 3.15.


Slots for defining module state
-------------------------------

The following "slot IDs"  are available for defining the module state.

Py_mod_state_size
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for the size of the module state, in bytes.

   Setting the value to a non-negative value means that the module can
   be re-initialized and specifies the additional amount of memory it
   requires for its state.

   Ver **PEP 3121** para mais detalhes.

   Use "PyModule_GetStateSize()" to retrieve the size of a given
   module.

   Adicionado na versão 3.15: Use "PyModuleDef.m_size" instead to
   support previous versions.

Py_mod_state_traverse
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for a traversal function to call during GC traversal of
   the module object.

   The signature of the function, and meanings of the arguments, is
   similar as for "PyTypeObject.tp_traverse":

   int traverse_module_state(PyObject *module, visitproc visit, void *arg)

   This function is not called if the module state was requested but
   is not allocated yet. This is the case immediately after the module
   is created and before the module is executed ("Py_mod_exec"
   function). More precisely, this function is not called if the state
   size ("Py_mod_state_size") is greater than 0 and the module state
   (as returned by "PyModule_GetState()") is "NULL".

   Adicionado na versão 3.15: Use "PyModuleDef.m_traverse" instead to
   support previous versions.

Py_mod_state_clear
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for a clear function to call during GC clearing of the
   module object.

   The signature of the function is:

   int clear_module_state(PyObject *module)

   This function is not called if the module state was requested but
   is not allocated yet. This is the case immediately after the module
   is created and before the module is executed ("Py_mod_exec"
   function). More precisely, this function is not called if the state
   size ("Py_mod_state_size") is greater than 0 and the module state
   (as returned by "PyModule_GetState()") is "NULL".

   Like "PyTypeObject.tp_clear", this function is not *always* called
   before a module is deallocated. For example, when reference
   counting is enough to determine that an object is no longer used,
   the cyclic garbage collector is not involved and the
   "Py_mod_state_free" function is called directly.

   Adicionado na versão 3.15: Use "PyModuleDef.m_clear" instead to
   support previous versions.

Py_mod_state_free
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for a function to call during deallocation of the module
   object.

   The signature of the function is:

   int free_module_state(PyObject *module)

   This function is not called if the module state was requested but
   is not allocated yet. This is the case immediately after the module
   is created and before the module is executed ("Py_mod_exec"
   function). More precisely, this function is not called if the state
   size ("Py_mod_state_size") is greater than 0 and the module state
   (as returned by "PyModule_GetState()") is "NULL".

   Adicionado na versão 3.15: Use "PyModuleDef.m_free" instead to
   support previous versions.


Module token
------------

Each module may have an associated *token*: a pointer-sized value
intended to identify of the module state's memory layout. This means
that if you have a module object, but you are not sure if it “belongs”
to your extension, you can check using code like this:

   PyObject *module = <the module in question>

   void *module_token;
   if (PyModule_GetToken(module, &module_token) < 0) {
       return NULL;
   }
   if (module_token != your_token) {
       PyErr_SetString(PyExc_ValueError, "unexpected module")
       return NULL;
   }

   // This module's state has the expected memory layout; it's safe to cast
   struct my_state state = (struct my_state*)PyModule_GetState(module)

A module's token -- and the *your_token* value to use in the above
code -- is:

* For modules created with "PyModuleDef": the address of that
  "PyModuleDef";

* For modules defined with the "Py_mod_token" slot: the value of that
  slot;

* For modules created from an "PyModExport_*" export hook: the slots
  array that the export hook returned (unless overridden with
  "Py_mod_token").

Py_mod_token
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for the module token.

   If you use this slot to set the module token (rather than rely on
   the default), you must ensure that:

   * The pointer outlives the class, so it's not reused for something
     else while the class exists.

   * It "belongs" to the extension module where the class lives, so it
     will not clash with other extensions.

   * If the token points to a "PyModuleDef" struct, the module should
     behave as if it was created from that "PyModuleDef". In
     particular, the module state must have matching layout and
     semantics.

   Modules created from "PyModuleDef" always use the address of the
   "PyModuleDef" as the token. This means that "Py_mod_token" cannot
   be used in "PyModuleDef.m_slots".

   Adicionado na versão 3.15.

int PyModule_GetToken(PyObject *module, void **result)
    * Parte da ABI Estável desde a versão 3.15.*

   Set **result* to the module token for *module* and return 0.

   On error, set **result* to NULL, and return -1 with an exception
   set.

   Adicionado na versão 3.15.

See also "PyType_GetModuleByToken()".


Creating extension modules dynamically
======================================

The following functions may be used to create an extension module
dynamically, rather than from an extension's export hook.

PyObject *PyModule_FromSlotsAndSpec(const PySlot *slots, PyObject *spec)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.15.*

   Create a new module object, given an array of slots and the
   "ModuleSpec" *spec*.

   The *slots* argument must point to an array of "PySlot" structures,
   terminated by an entry with slot ID of 0 (typically written as
   "PySlot_END"). The array must include a "Py_mod_abi" entry.

   The *spec* argument may be any "ModuleSpec"-like object, as
   described in "Py_mod_create" documentation. Currently, the *spec*
   must have a "name" attribute.

   On success, return the new module. On error, return "NULL" with an
   exception set.

   Note that this does not process the module's execution slot
   ("Py_mod_exec"). Both "PyModule_FromSlotsAndSpec()" and
   "PyModule_Exec()" must be called to fully initialize a module. (See
   also Inicialização multifásica.)

   Adicionado na versão 3.15.

int PyModule_Exec(PyObject *module)
    * Parte da ABI Estável desde a versão 3.15.*

   Execute the "Py_mod_exec" slot(s) of *module*.

   On success, return 0. On error, return -1 with an exception set.

   For clarity: If *module* has no slots, for example if it uses
   legacy single-phase initialization, this function does nothing and
   returns 0.

   Adicionado na versão 3.15.


Module definition struct
========================

Traditionally, extension modules were defined using a *module
definition* as the “description" of how a module should be created.
Rather than using an array of slots directly, the definition has
dedicated members for most common functionality, and allows additional
slots as an extension mechanism.

This way of defining modules is still available and there are no plans
to remove it.

type PyModuleDef
    * Parte da ABI Estável (see below).*

   The module definition struct, which holds information needed to
   create a module object.

   This structure must be statically allocated (or be otherwise
   guaranteed to be valid while any modules created from it exist).
   Usually, there is only one variable of this type for each extension
   module defined this way.

   The struct, including all members, is part of the Stable ABI for
   non-free-threaded builds ("abi3"). In the Stable ABI for free-
   threaded builds ("abi3t"), this struct is opaque, and unusable in
   practice; see Module definition for a replacement.

   PyModuleDef_Base m_base

      Always initialize this member to "PyModuleDef_HEAD_INIT":

      type PyModuleDef_Base
          * Parte da ABI Estável (see below).*

         The type of "PyModuleDef.m_base".

         The struct is part of the Stable ABI for non-free-threaded
         builds ("abi3"). In the Stable ABI for Free-Threaded Builds
         ("abi3t"), this struct is opaque, and unusable in practice.

      PyModuleDef_HEAD_INIT

         The required initial value for "PyModuleDef.m_base".

   const char *m_name

      Corresponds to the "Py_mod_name" slot.

   const char *m_doc

      These members correspond to the "Py_mod_doc" slot. Setting this
      to NULL is equivalent to omitting the slot.

   Py_ssize_t m_size

      Corresponds to the "Py_mod_state_size" slot. Setting this to
      zero is equivalent to omitting the slot.

      When using legacy single-phase initialization or when creating
      modules dynamically using "PyModule_Create()" or
      "PyModule_Create2()", "m_size" may be set to -1. This indicates
      that the module does not support sub-interpreters, because it
      has global state.

   PyMethodDef *m_methods

      Corresponds to the "Py_mod_methods" slot. Setting this to NULL
      is equivalent to omitting the slot.

   PyModuleDef_Slot *m_slots

      An array of additional slots, terminated by a "{0, NULL}" entry.
      Note that the entries use the older "PyModuleDef_Slot"
      structure, rather than "PySlot".

      If the array contains slots corresponding to "PyModuleDef"
      members, the values must match. For example, if you use
      "Py_mod_name" in "m_slots", "PyModuleDef.m_name" must be set to
      the same pointer (not just an equal string).

      Alterado na versão 3.5: Antes da versão 3.5, esse membro era
      sempre definido como "NULL" e era definido como:

         inquiry m_reload

      type PyModuleDef_Slot
          * Parte da ABI Estável (incluindo todos os membros) desde a
         versão 3.5.*

         Older structure defining additional slots of a module.

         Note that a "PyModuleDef_Slot" array may be included in a
         "PySlot" array using "Py_mod_slots", and vice versa using
         "Py_slot_subslots".

         Each "PyModuleDef_Slot" structure "modslot" is interpreted as
         the following "PySlot" structure:

            (PySlot){
               .sl_id=modslot.slot,
               .sl_flags=PySlot_INTPTR | sub_static,
               .sl_ptr=modslot.value
            }

         where "sub_static" is "PySlot_STATIC" if the slot requires
         the flag (such as for "Py_mod_methods"), or if this flag is
         present on the "parent" "Py_mod_slots" slot (if any).

         int slot

            Corresponds to "PySlot.sl_id".

         void *value

            Corresponds to "PySlot.sl_ptr".

         Adicionado na versão 3.5.

   traverseproc m_traverse
   inquiry m_clear
   freefunc m_free

      These members correspond to the "Py_mod_state_traverse",
      "Py_mod_state_clear", and "Py_mod_state_free" slots,
      respectively.

      Setting these members to NULL is equivalent to omitting the
      corresponding slots.

      Alterado na versão 3.9: "m_traverse", "m_clear" and "m_free"
      functions are no longer called before the module state is
      allocated.

PyTypeObject PyModuleDef_Type
    * Parte da ABI Estável desde a versão 3.5.*

   The type of "PyModuleDef" objects.

Py_mod_slots
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" that works like "Py_slot_subslots", except it specifies
   an array of "PyModuleDef_Slot" structures.

   Adicionado na versão 3.15.

The following API can be used to create modules from a "PyModuleDef"
struct:

PyObject *PyModule_Create(PyModuleDef *def)
    *Retorna valor: Nova referência.*

   Create a new module object, given the definition in *def*. This is
   a macro that calls "PyModule_Create2()" with *module_api_version*
   set to "PYTHON_API_VERSION", or to "PYTHON_ABI_VERSION" if using
   the limited API.

PyObject *PyModule_Create2(PyModuleDef *def, int module_api_version)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a new module object, given the definition in *def*, assuming
   the API version *module_api_version*.  If that version does not
   match the version of the running interpreter, a "RuntimeWarning" is
   emitted.

   Retorna "NULL" com uma exceção definida em caso de erro.

   This function does not support slots. The "m_slots" member of *def*
   must be "NULL".

   Nota:

     A maioria dos usos dessa função deve ser feita com
     "PyModule_Create()"; use-o apenas se tiver certeza de que
     precisa.

PyObject *PyModule_FromDefAndSpec(PyModuleDef *def, PyObject *spec)
    *Retorna valor: Nova referência.*

   This macro calls "PyModule_FromDefAndSpec2()" with
   *module_api_version* set to "PYTHON_API_VERSION", or to
   "PYTHON_ABI_VERSION" if using the limited API.

   Adicionado na versão 3.5.

   Suavemente descontinuado desde a versão 3.15: Prefer
   "PyModule_FromSlotsAndSpec()" in new code.

PyObject *PyModule_FromDefAndSpec2(PyModuleDef *def, PyObject *spec, int module_api_version)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Create a new module object, given the definition in *def* and the
   ModuleSpec *spec*, assuming the API version *module_api_version*.
   If that version does not match the version of the running
   interpreter, a "RuntimeWarning" is emitted.

   Retorna "NULL" com uma exceção definida em caso de erro.

   Note that this does not process execution slots ("Py_mod_exec").
   Both "PyModule_FromDefAndSpec" and "PyModule_ExecDef" must be
   called to fully initialize a module.

   Nota:

     Most uses of this function should be using
     "PyModule_FromDefAndSpec()" instead; only use this if you are
     sure you need it.

   Adicionado na versão 3.5.

   Suavemente descontinuado desde a versão 3.15: Prefer
   "PyModule_FromSlotsAndSpec()" in new code.

int PyModule_ExecDef(PyObject *module, PyModuleDef *def)
    * Parte da ABI Estável desde a versão 3.7.*

   Process any execution slots ("Py_mod_exec") given in *def*.

   Adicionado na versão 3.5.

   Suavemente descontinuado desde a versão 3.15: To run a module's own
   execution slots, prefer "PyModule_Exec()", which works on modules
   that were not created from a "PyModuleDef" structure.

PYTHON_API_VERSION
PYTHON_API_STRING

   The C API version, as an integer ("1013") and string (""1013""),
   respectively. Defined for backwards compatibility.

   Atualmente, essa constante não é atualizada nas novas versões de
   Python e não é útil para controle de versão. Isso pode mudar no
   futuro.

PYTHON_ABI_VERSION
PYTHON_ABI_STRING

   Defined as "3" and ""3"", respectively, for backwards
   compatibility.

   Atualmente, essa constante não é atualizada nas novas versões de
   Python e não é útil para controle de versão. Isso pode mudar no
   futuro.


Support functions
=================

The following functions are provided to help initialize a module
object. They are intended for a module's execution slot
("Py_mod_exec"), the initialization function for legacy single-phase
initialization, or code that creates modules dynamically.

int PyModule_AddObjectRef(PyObject *module, const char *name, PyObject *value)
    * Parte da ABI Estável desde a versão 3.10.*

   Add an object to *module* as *name*.  This is a convenience
   function which can be used from the module's initialization
   function.

   On success, return "0". On error, raise an exception and return
   "-1".

   Exemplo de uso:

      static int
      add_spam(PyObject *module, int value)
      {
          PyObject *obj = PyLong_FromLong(value);
          if (obj == NULL) {
              return -1;
          }
          int res = PyModule_AddObjectRef(module, "spam", obj);
          Py_DECREF(obj);
          return res;
       }

   To be convenient, the function accepts "NULL" *value* with an
   exception set. In this case, return "-1" and just leave the raised
   exception unchanged.

   O exemplo também pode ser escrito sem verificar explicitamente se
   *obj* é "NULL":

      static int
      add_spam(PyObject *module, int value)
      {
          PyObject *obj = PyLong_FromLong(value);
          int res = PyModule_AddObjectRef(module, "spam", obj);
          Py_XDECREF(obj);
          return res;
       }

   Note that "Py_XDECREF()" should be used instead of "Py_DECREF()" in
   this case, since *obj* can be "NULL".

   The number of different *name* strings passed to this function
   should be kept small, usually by only using statically allocated
   strings as *name*. For names that aren't known at compile time,
   prefer calling "PyUnicode_FromString()" and "PyObject_SetAttr()"
   directly. For more details, see "PyUnicode_InternFromString()",
   which may be used internally to create a key object.

   Adicionado na versão 3.10.

int PyModule_Add(PyObject *module, const char *name, PyObject *value)
    * Parte da ABI Estável desde a versão 3.13.*

   Similar to "PyModule_AddObjectRef()", but "*steals*" a reference to
   *value* (even on error). It can be called with a result of function
   that returns a new reference without bothering to check its result
   or even saving it to a variable.

   Exemplo de uso:

      if (PyModule_Add(module, "spam", PyBytes_FromString(value)) < 0) {
          goto error;
      }

   Adicionado na versão 3.13.

int PyModule_AddObject(PyObject *module, const char *name, PyObject *value)
    * Parte da ABI Estável.*

   Similar to "PyModule_AddObjectRef()", but *steals* a reference to
   *value* on success (if it returns "0").

   The new "PyModule_Add()" or "PyModule_AddObjectRef()" functions are
   recommended, since it is easy to introduce reference leaks by
   misusing the "PyModule_AddObject()" function.

   Nota:

     Unlike other functions that steal references,
     "PyModule_AddObject()" only releases the reference to *value*
     **on success**.This means that its return value must be checked,
     and calling code must "Py_XDECREF()" *value* manually on error.

   Exemplo de uso:

      PyObject *obj = PyBytes_FromString(value);
      if (PyModule_AddObject(module, "spam", obj) < 0) {
          // If 'obj' is not NULL and PyModule_AddObject() failed,
          // 'obj' strong reference must be deleted with Py_XDECREF().
          // If 'obj' is NULL, Py_XDECREF() does nothing.
          Py_XDECREF(obj);
          goto error;
      }
      // PyModule_AddObject() stole a reference to obj:
      // Py_XDECREF(obj) is not needed here.

   Suavemente descontinuado desde a versão 3.13.

int PyModule_AddIntConstant(PyObject *module, const char *name, long value)
    * Parte da ABI Estável.*

   Add an integer constant to *module* as *name*.  This convenience
   function can be used from the module's initialization function.
   Return "-1" with an exception set on error, "0" on success.

   This is a convenience function that calls "PyLong_FromLong()" and
   "PyModule_AddObjectRef()"; see their documentation for details.

int PyModule_AddStringConstant(PyObject *module, const char *name, const char *value)
    * Parte da ABI Estável.*

   Add a string constant to *module* as *name*.  This convenience
   function can be used from the module's initialization function.
   The string *value* must be "NULL"-terminated. Return "-1" with an
   exception set on error, "0" on success.

   This is a convenience function that calls
   "PyUnicode_InternFromString()" and "PyModule_AddObjectRef()"; see
   their documentation for details.

PyModule_AddIntMacro(module, macro)

   Add an int constant to *module*. The name and the value are taken
   from *macro*. For example "PyModule_AddIntMacro(module, AF_INET)"
   adds the int constant *AF_INET* with the value of *AF_INET* to
   *module*. Return "-1" with an exception set on error, "0" on
   success.

PyModule_AddStringMacro(module, macro)

   Add a string constant to *module*.

int PyModule_AddType(PyObject *module, PyTypeObject *type)
    * Parte da ABI Estável desde a versão 3.10.*

   Add a type object to *module*. The type object is finalized by
   calling internally "PyType_Ready()". The name of the type object is
   taken from the last component of "tp_name" after dot. Return "-1"
   with an exception set on error, "0" on success.

   Adicionado na versão 3.9.

int PyModule_AddFunctions(PyObject *module, PyMethodDef *functions)
    * Parte da ABI Estável desde a versão 3.7.*

   Add the functions from the "NULL" terminated *functions* array to
   *module*. Refer to the "PyMethodDef" documentation for details on
   individual entries (due to the lack of a shared module namespace,
   module level "functions" implemented in C typically receive the
   module as their first parameter, making them similar to instance
   methods on Python classes).

   This function is called automatically when creating a module from
   "PyModuleDef" (such as when using Inicialização multifásica,
   "PyModule_Create", or "PyModule_FromDefAndSpec"). Some module
   authors may prefer defining functions in multiple "PyMethodDef"
   arrays; in that case they should call this function directly.

   The *functions* array must be statically allocated (or otherwise
   guaranteed to outlive the module object).

   Adicionado na versão 3.5.

int PyModule_SetDocString(PyObject *module, const char *docstring)
    * Parte da ABI Estável desde a versão 3.7.*

   Set the docstring for *module* to *docstring*. This function is
   called automatically when creating a module from "PyModuleDef"
   (such as when using Inicialização multifásica, "PyModule_Create",
   or "PyModule_FromDefAndSpec").

   Return "0" on success. Return "-1" with an exception set on error.

   Adicionado na versão 3.5.

int PyUnstable_Module_SetGIL(PyObject *module, void *gil)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Indicate that *module* does or does not support running without the
   global interpreter lock (GIL), using one of the values from
   "Py_mod_gil". It must be called during *module*'s initialization
   function when using Inicialização monofásica legada. If this
   function is not called during module initialization, the import
   machinery assumes the module does not support running without the
   GIL. This function is only available in Python builds configured
   with "--disable-gil". Return "-1" with an exception set on error,
   "0" on success.

   Adicionado na versão 3.13.


Module lookup (single-phase initialization)
-------------------------------------------

The legacy single-phase initialization initialization scheme creates
singleton modules that can be looked up in the context of the current
interpreter. This allows the module object to be retrieved later with
only a reference to the module definition.

These functions will not work on modules created using multi-phase
initialization, since multiple such modules can be created from a
single definition.

PyObject *PyState_FindModule(PyModuleDef *def)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Returns the module object that was created from *def* for the
   current interpreter. This method requires that the module object
   has been attached to the interpreter state with
   "PyState_AddModule()" beforehand. In case the corresponding module
   object is not found or has not been attached to the interpreter
   state yet, it returns "NULL".

int PyState_AddModule(PyObject *module, PyModuleDef *def)
    * Parte da ABI Estável desde a versão 3.3.*

   Attaches the module object passed to the function to the
   interpreter state. This allows the module object to be accessible
   via "PyState_FindModule()".

   Only effective on modules created using single-phase
   initialization.

   Python calls "PyState_AddModule" automatically after importing a
   module that uses single-phase initialization, so it is unnecessary
   (but harmless) to call it from module initialization code. An
   explicit call is needed only if the module's own init code
   subsequently calls "PyState_FindModule". The function is mainly
   intended for implementing alternative import mechanisms (either by
   calling it directly, or by referring to its implementation for
   details of the required state updates).

   If a module was attached previously using the same *def*, it is
   replaced by the new *module*.

   O chamador deve ter um *estado de thread anexado*.

   Retorna "-1" com uma exceção definida em caso de erro, "0" em caso
   de sucesso.

   Adicionado na versão 3.3.

int PyState_RemoveModule(PyModuleDef *def)
    * Parte da ABI Estável desde a versão 3.3.*

   Removes the module object created from *def* from the interpreter
   state. Return "-1" with an exception set on error, "0" on success.

   O chamador deve ter um *estado de thread anexado*.

   Adicionado na versão 3.3.
