Objetos tipo
************

type PyTypeObject
    * Parte da ABI Estável (como uma estrutura opaca).*

   A estrutura C dos objetos usados para descrever tipos embutidos.

PyTypeObject PyType_Type
    * Parte da ABI Estável.*

   Este é o objeto de tipo para objetos tipo; é o mesmo objeto que
   "type" na camada Python.

int PyType_Check(PyObject *o)

   Retorna valor diferente de zero se o objeto *o* for um objeto tipo,
   incluindo instâncias de tipos derivados do objeto tipo padrão.
   Retorna 0 em todos os outros casos. Esta função sempre tem sucesso.

int PyType_CheckExact(PyObject *o)

   Retorna valor diferente de zero se o objeto *o* for um objeto tipo,
   mas não um subtipo do objeto tipo padrão. Retorna 0 em todos os
   outros casos. Esta função sempre tem sucesso.

unsigned int PyType_ClearCache()
    * Parte da ABI Estável.*

   Limpa o cache de pesquisa interno. Retorna a marcação de versão
   atual.

unsigned long PyType_GetFlags(PyTypeObject *type)
    * Parte da ABI Estável.*

   Return the "tp_flags" member of *type*. This function is primarily
   meant for use with "Py_LIMITED_API"; the individual flag bits are
   guaranteed to be stable across Python releases, but access to
   "tp_flags" itself is not part of the limited API.

   Adicionado na versão 3.2.

   Alterado na versão 3.4: O tipo de retorno é agora um "unsigned
   long" em vez de um "long".

PyObject *PyType_GetDict(PyTypeObject *type)

   Return the type object's internal namespace, which is otherwise
   only exposed via a read-only proxy ("cls.__dict__"). This is a
   replacement for accessing "tp_dict" directly. The returned
   dictionary must be treated as read-only.

   This function is meant for specific embedding and language-binding
   cases, where direct access to the dict is necessary and indirect
   access (e.g. via the proxy or "PyObject_GetAttr()") isn't adequate.

   Extension modules should continue to use "tp_dict", directly or
   indirectly, when setting up their own types.

   Adicionado na versão 3.12.

void PyType_Modified(PyTypeObject *type)
    * Parte da ABI Estável.*

   Invalida o cache de pesquisa interna para o tipo e todos os seus
   subtipos. Esta função deve ser chamada após qualquer modificação
   manual dos atributos ou classes bases do tipo.

int PyType_AddWatcher(PyType_WatchCallback callback)

   Register *callback* as a type watcher. Return a non-negative
   integer ID which must be passed to future calls to
   "PyType_Watch()". In case of error (e.g. no more watcher IDs
   available), return "-1" and set an exception.

   In free-threaded builds, "PyType_AddWatcher()" is not thread-safe,
   so it must be called at start up (before spawning the first
   thread).

   Adicionado na versão 3.12.

int PyType_ClearWatcher(int watcher_id)

   Clear watcher identified by *watcher_id* (previously returned from
   "PyType_AddWatcher()"). Return "0" on success, "-1" on error (e.g.
   if *watcher_id* was never registered.)

   An extension should never call "PyType_ClearWatcher" with a
   *watcher_id* that was not returned to it by a previous call to
   "PyType_AddWatcher()".

   Adicionado na versão 3.12.

int PyType_Watch(int watcher_id, PyObject *type)

   Mark *type* as watched. The callback granted *watcher_id* by
   "PyType_AddWatcher()" will be called whenever "PyType_Modified()"
   reports a change to *type*. (The callback may be called only once
   for a series of consecutive modifications to *type*, if
   "_PyType_Lookup()" is not called on *type* between the
   modifications; this is an implementation detail and subject to
   change.)

   The callback is also invoked when a watched heap type is
   deallocated.

   An extension should never call "PyType_Watch" with a *watcher_id*
   that was not returned to it by a previous call to
   "PyType_AddWatcher()".

   Adicionado na versão 3.12.

   Alterado na versão 3.15: The callback is now also invoked when a
   watched heap type is deallocated.

int PyType_Unwatch(int watcher_id, PyObject *type)

   Mark *type* as not watched. This undoes a previous call to
   "PyType_Watch()". *type* must not be "NULL".

   An extension should never call this function with a *watcher_id*
   that was not returned to it by a previous call to
   "PyType_AddWatcher()".

   On success, this function returns "0". On failure, this function
   returns "-1" with an exception set.

   Adicionado na versão 3.12.

typedef int (*PyType_WatchCallback)(PyObject *type)

   Type of a type-watcher callback function.

   The callback must not modify *type* or cause "PyType_Modified()" to
   be called on *type* or any type in its MRO; violating this rule
   could cause infinite recursion.

   The callback may be called during type deallocation. In this case,
   the type object is temporarily resurrected (its reference count is
   at least 1) and all its attributes are still valid. However, the
   callback should not store new strong references to the type, as
   this would resurrect the object and prevent its deallocation.

   Adicionado na versão 3.12.

   Alterado na versão 3.15: The callback may now be called during
   deallocation of a watched heap type.

int PyType_HasFeature(PyTypeObject *o, int feature)

   Retorna valor diferente de zero se o objeto tipo *o* define o
   recurso *feature*. Os recursos de tipo são denotados por
   sinalizadores de bit único.

int PyType_FastSubclass(PyTypeObject *type, int flag)

   Return non-zero if the type object *type* sets the subclass flag
   *flag*. Subclass flags are denoted by "Py_TPFLAGS_*_SUBCLASS". This
   function is used by many "_Check" functions for common types.

   Ver também:

     "PyObject_TypeCheck()", which is used as a slower alternative in
     "_Check" functions for types that don't come with subclass flags.

int PyType_IS_GC(PyTypeObject *o)

   Return true if the type object includes support for the cycle
   detector; this tests the type flag "Py_TPFLAGS_HAVE_GC".

int PyType_IsSubtype(PyTypeObject *a, PyTypeObject *b)
    * Parte da ABI Estável.*

   Retorna verdadeiro se *a* for um subtipo de *b*.

   This function only checks for actual subtypes, which means that
   "__subclasscheck__()" is not called on *b*.  Call
   "PyObject_IsSubclass()" to do the same check that "issubclass()"
   would do.

PyObject *PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Generic handler for the "tp_alloc" slot of a type object.  Uses
   Python's default memory allocation mechanism to allocate memory for
   a new instance, zeros the memory, then initializes the memory as if
   by calling "PyObject_Init()" or "PyObject_InitVar()".

   Do not call this directly to allocate memory for an object; call
   the type's "tp_alloc" slot instead.

   For types that support garbage collection (i.e., the
   "Py_TPFLAGS_HAVE_GC" flag is set), this function behaves like
   "PyObject_GC_New" or "PyObject_GC_NewVar" (except the memory is
   guaranteed to be zeroed before initialization), and should be
   paired with "PyObject_GC_Del()" in "tp_free". Otherwise, it behaves
   like "PyObject_New" or "PyObject_NewVar" (except the memory is
   guaranteed to be zeroed before initialization) and should be paired
   with "PyObject_Free()" in "tp_free".

PyObject *PyType_GenericNew(PyTypeObject *type, PyObject *args, PyObject *kwds)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Generic handler for the "tp_new" slot of a type object.  Creates a
   new instance using the type's "tp_alloc" slot and returns the
   resulting object.

int PyType_Ready(PyTypeObject *type)
    * Parte da ABI Estável.*

   Finaliza um objeto tipo. Isso deve ser chamado em todos os objetos
   tipo para finalizar sua inicialização. Esta função é responsável
   por adicionar slots herdados da classe base de um tipo. Retorna "0"
   em caso de sucesso, ou retorna "-1" e define uma exceção em caso de
   erro.

   Nota:

     If some of the base classes implements the GC protocol and the
     provided type does not include the "Py_TPFLAGS_HAVE_GC" in its
     flags, then the GC protocol will be automatically implemented
     from its parents. On the contrary, if the type being created does
     include "Py_TPFLAGS_HAVE_GC" in its flags then it **must**
     implement the GC protocol itself by at least implementing the
     "tp_traverse" handle.

PyObject *PyType_GetName(PyTypeObject *type)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.11.*

   Retorna o nome do tipo. Equivalente a pegar o atributo "__name__"
   do tipo.

   Adicionado na versão 3.11.

PyObject *PyType_GetQualName(PyTypeObject *type)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.11.*

   Retorna o nome qualificado do tipo. Equivalente a pegar o atributo
   "__qualname__" do tipo.

   Adicionado na versão 3.11.

PyObject *PyType_GetFullyQualifiedName(PyTypeObject *type)
    * Parte da ABI Estável desde a versão 3.13.*

   Retorna o nome qualificado do tipo. Equivalente à
   "f"{type.__module__}.{type.__qualname__}"", ou "type.__qualname__"
   se "type.__module__" não é uma string ou é igual a ""builtins"".

   Adicionado na versão 3.13.

PyObject *PyType_GetModuleName(PyTypeObject *type)
    * Parte da ABI Estável desde a versão 3.13.*

   Retorna o nome do tipo do módulo. Equivalente a pegar o atributo
   "type.__module__".

   Adicionado na versão 3.13.

void *PyType_GetSlot(PyTypeObject *type, int slot)
    * Parte da ABI Estável desde a versão 3.4.*

   Retorna o ponteiro de função armazenado no slot fornecido. Se o
   resultado for "NULL", isso indica que o slot é "NULL" ou que a
   função foi chamada com parâmetros inválidos. Os chamadores
   normalmente lançarão o ponteiro do resultado no tipo de função
   apropriado.

   Veja "PyType_Slot.slot" por possíveis valores do argumento *slot*.

   Adicionado na versão 3.4.

   Alterado na versão 3.10: "PyType_GetSlot()" agora aceita todos os
   tipos. Antes, estava limitada a tipos heap.

PyObject *PyType_GetModule(PyTypeObject *type)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável
   desde a versão 3.10.*

   Retorna o objeto de módulo associado ao tipo fornecido quando o
   tipo foi criado usando "PyType_FromModuleAndSpec()".

   The returned reference is *borrowed* from *type*, and will be valid
   as long as you hold a reference to *type*. Do not release it with
   "Py_DECREF()" or similar.

   Se nenhum módulo estiver associado com o tipo fornecido, define
   "TypeError" e retorna "NULL".

   This function is usually used to get the module in which a method
   is defined. Note that in such a method,
   "PyType_GetModule(Py_TYPE(self))" may not return the intended
   result. "Py_TYPE(self)" may be a *subclass* of the intended class,
   and subclasses are not necessarily defined in the same module as
   their superclass. See "PyCMethod" to get the class that defines the
   method. See "PyType_GetModuleByToken()" for cases when "PyCMethod"
   cannot be used.

   Adicionado na versão 3.9.

void *PyType_GetModuleState(PyTypeObject *type)
    * Parte da ABI Estável desde a versão 3.10.*

   Return the state of the module object associated with the given
   type. This is a shortcut for calling "PyModule_GetState()" on the
   result of "PyType_GetModule()".

   Se nenhum módulo estiver associado com o tipo fornecido, define
   "TypeError" e retorna "NULL".

   Se o *tipo* tem um módulo associado mas o seu estado é "NULL",
   retorna "NULL" sem definir uma exceção.

   Adicionado na versão 3.9.

PyObject *PyType_GetModuleByToken(PyTypeObject *type, const void *mod_token)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.15.*

   Find the first superclass whose module has the given module token,
   and return that module.

   Se nenhum módulo é encontrado, levanta um "TypeError" e retorna
   "NULL".

   This function is intended to be used together with
   "PyModule_GetState()" to get module state from slot methods (such
   as "tp_init" or "nb_add") and other places where a method's
   defining class cannot be passed using the "PyCMethod" calling
   convention.

   Adicionado na versão 3.15.

PyObject *PyType_GetModuleByDef(PyTypeObject *type, struct PyModuleDef *def)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável
   desde a versão 3.13.*

   Find the first superclass whose module was created from the given
   "PyModuleDef" *def*, or whose module token is equal to *def*, and
   return that module.

   Note that modules created from a "PyModuleDef" always have their
   token set to the "PyModuleDef"'s address. In other words, this
   function is equivalent to "PyType_GetModuleByToken()", except that
   it:

   * returns a borrowed reference, and

   * has a non-"void*" argument type (which is a cosmetic difference
     in C).

   The returned reference is *borrowed* from *type*, and will be valid
   as long as you hold a reference to *type*. Do not release it with
   "Py_DECREF()" or similar.

   Adicionado na versão 3.11.

int PyType_GetBaseByToken(PyTypeObject *type, void *tp_token, PyTypeObject **result)
    * Parte da ABI Estável desde a versão 3.14.*

   Find the first superclass in *type*'s *method resolution order*
   whose "Py_tp_token" token is equal to *tp_token*.

   * If found, set **result* to a new *strong reference* to it and
     return "1".

   * If not found, set **result* to "NULL" and return "0".

   * On error, set **result* to "NULL" and return "-1" with an
     exception set.

   The *result* argument may be "NULL", in which case **result* is not
   set. Use this if you need only the return value.

   The *tp_token* argument may not be "NULL".

   Adicionado na versão 3.14.

int PyUnstable_Type_AssignVersionTag(PyTypeObject *type)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Attempt to assign a version tag to the given type.

   Returns 1 if the type already had a valid version tag or a new one
   was assigned, or 0 if a new tag could not be assigned.

   Adicionado na versão 3.12.

int PyType_SUPPORTS_WEAKREFS(PyTypeObject *type)

   Return true if instances of *type* support creating weak
   references, false otherwise. This function always succeeds. *type*
   must not be "NULL".

   Ver também:

     * Objetos referência fraca

     * "weakref"


Creating Heap-Allocated Types
=============================

The following function is used to create heap types:

PyObject *PyType_FromSlots(const PySlot *slots)
    * Parte da ABI Estável desde a versão 3.15.*

   Create and return a heap type from a "PySlot" array. See Slots de
   definição for general information on slots, and Type slot IDs for
   slots specific to type creation.

   This function calls "PyType_Ready()" on the new type.

   Note that this function does *not* fully match the behavior of
   calling "type()" or using the "class" statement. With user-provided
   base types or metaclasses, prefer calling "type" (or the metaclass)
   over "PyType_From*" functions. Specifically:

   * "__new__()" is not called on the new class (and it must be set to
     "type.__new__").

   * "__init__()" is not called on the new class.

   * "__init_subclass__()" is not called on any bases.

   * "__set_name__()" is not called on new descriptors.

   Slots are typically defined as a global static constant arrays.
   However, sometimes slot values are not statically known at compile
   time. For example, slots like "Py_tp_bases", "Py_tp_metaclass" and
   "Py_tp_module" require live Python objects. In this case, it is
   recommended to put such slots on the stack, and use
   "Py_slot_subslots" to refer to an array of static slots. For
   example:

      static const PySlot my_slots[] = {
         PySlot_STATIC_DATA(Py_tp_name, "MyClass"),
         PySlot_FUNC(Py_tp_repr, my_repr_func),
         ...
         PySlot_END
      };

      PyObject *make_my_class(PyObject *module) {
         PySlot all_slots[] = {
            PySlot_STATIC_DATA(Py_slot_subslots, my_slots),
            PySlot_DATA(Py_tp_module, module),
            PySlot_END
         };
         return PyType_FromSlots(all_slots);
      }

Heap types created without the "Py_TPFLAGS_IMMUTABLETYPE" flag may be
modified, for example by setting attributes on them, as with classes
defined in Python code. Sometimes, such modifications are necessary to
fully initialize a type, but you may wish to prevent users from
changing the type after the initialization is done:

int PyType_Freeze(PyTypeObject *type)
    * Parte da ABI Estável desde a versão 3.14.*

   Make a type immutable: set the "Py_TPFLAGS_IMMUTABLETYPE" flag.

   All base classes of *type* must be immutable.

   On success, return "0". On error, set an exception and return "-1".

   The type must not be used before it's made immutable. For example,
   type instances must not be created before the type is made
   immutable.

   Adicionado na versão 3.14.


Type slot IDs
-------------

Most type slot IDs are named like the field names of the structures
"PyTypeObject", "PyNumberMethods", "PySequenceMethods",
"PyMappingMethods" and "PyAsyncMethods" with an added "Py_" prefix.
For example, use:

* "Py_tp_dealloc" to set "PyTypeObject.tp_dealloc"

* "Py_nb_add" to set "PyNumberMethods.nb_add"

* "Py_sq_length" to set "PySequenceMethods.sq_length"

The following slots need additional considerations when specified as
slots:

* "Py_tp_name"

* "Py_tp_basicsize" and "Py_tp_extra_basicsize"

* "Py_tp_itemsize"

* "Py_tp_flags"

Additional slots do not directly correspond to a "PyTypeObject" struct
field:

* "Py_tp_token"

* "Py_tp_metaclass"

* "Py_tp_module"

The following “offset” fields cannot be set using "PyType_Slot":

* "tp_weaklistoffset" (use "Py_TPFLAGS_MANAGED_WEAKREF" instead if
  possible)

* "tp_dictoffset" (use "Py_TPFLAGS_MANAGED_DICT" instead if possible)

* "tp_vectorcall_offset" (use ""__vectorcalloffset__"" in PyMemberDef)

If it is not possible to switch to a "MANAGED" flag (for example, for
vectorcall or to support Python older than 3.12), specify the offset
in "Py_tp_members". See PyMemberDef documentation for details.

The following internal fields cannot be set at all when creating a
heap type:

* "tp_dict", "tp_mro", "tp_cache", "tp_subclasses", and "tp_weaklist".

The "Py_tp_base" slot is equivalent to "Py_tp_bases"; both may be set
either to a type or a tuple of types. If both are specified, the value
of "Py_tp_bases" is used.

Slot values may not be "NULL", except for the following:

* "Py_tp_doc"

* "Py_tp_token" (for clarity, prefer "Py_TP_USE_SPEC" rather than
  "NULL")

Alterado na versão 3.9: Slots in "PyBufferProcs" may be set in the
unlimited API.

Alterado na versão 3.11: "bf_getbuffer" and "bf_releasebuffer" are now
available under the limited API.

Alterado na versão 3.14: The field "tp_vectorcall" can now be set
using "Py_tp_vectorcall".  See the field's documentation for details.

Alterado na versão 3.15: The "Py_tp_bases" slot may be set to a single
type object, making it equivalent to the "Py_tp_base" slot.
Previously, a tuple of types was required.

The following slots correspond to fields in the underlying type
structure, but need extra remarks for use as slots:

Py_tp_name
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for the name of the type, used to set
   "PyTypeObject.tp_name".

   This slot (or "PyType_Spec.name") is required to create a type.

   This may not be used in "PyType_Spec.slots". Use "PyType_Spec.name"
   instead.

   **Detalhes da implementação do CPython:** CPython processes slots
   in order. It is recommended to put "Py_tp_name" at the beginning of
   the slots array, so that if processing of a later slots fails,
   error messages can include the name.

   Adicionado na versão 3.15.

Py_tp_basicsize
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for the size of the instance in bytes. It is used to set
   "PyTypeObject.tp_basicsize".

   The value must be positive.

   This may not be used in "PyType_Spec.slots". Use
   "PyType_Spec.basicsize" instead.

   This slot may not be used with "PyType_GetSlot()". Use
   "PyTypeObject.tp_basicsize" instead if needed, but be aware that a
   type's size is often considered an implementation detail.

   Adicionado na versão 3.15.

Py_tp_extra_basicsize
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for type data size in bytes, that is, how much space
   instances of the class need *in addition* to space needed for
   superclasses.

   The value is used, together with the size of superclasses, to set
   "PyTypeObject.tp_basicsize". Python will insert padding as needed
   to meet "tp_basicsize"'s alignment requirements.

   Use "PyObject_GetTypeData()" to get a pointer to subclass-specific
   memory reserved this way.

   The value must be positive. To specify that instances need no
   additional size (that is, size should be inherited), omit the
   "Py_tp_extra_basicsize" slot rather than set it to zero.

   Specifying both "Py_tp_basicsize" and "Py_tp_extra_basicsize" is an
   error.

   This may not be used in "PyType_Spec.slots". Use negative
   "PyType_Spec.basicsize" instead.

   This slot may not be used with "PyType_GetSlot()".

   Adicionado na versão 3.15.

Py_tp_itemsize
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for the size of one element of a variable-size type, in
   bytes. Used to set "PyTypeObject.tp_itemsize". See "tp_itemsize"
   documentation for caveats.

   The value must be positive.

   If this slot is missing, "tp_itemsize" is inherited. Extending
   arbitrary variable-sized classes is dangerous, since some types use
   a fixed offset for variable-sized memory, which can then overlap
   fixed-sized memory used by a subclass. To help prevent mistakes,
   inheriting "itemsize" is only possible in the following situations:

   * The base is not variable-sized (its "tp_itemsize" is zero).

   * The requested "PyType_Spec.basicsize" is positive, suggesting
     that the memory layout of the base class is known.

   * The requested "PyType_Spec.basicsize" is zero, suggesting that
     the subclass does not access the instance's memory directly.

   * With the "Py_TPFLAGS_ITEMS_AT_END" flag.

   This may not be used in "PyType_Spec.slots". Use
   "PyType_Spec.itemsize" instead.

   This slot may not be used with "PyType_GetSlot()".

   Adicionado na versão 3.15.

Py_tp_flags
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for type flags, used to set "PyTypeObject.tp_flags".

   The "Py_TPFLAGS_HEAPTYPE" flag is not set,
   "PyType_FromSpecWithBases()" sets it automatically.

   This may not be used in "PyType_Spec.slots". Use negative
   "PyType_Spec.basicsize" instead.

   This slot may not be used with "PyType_GetSlot()". Use
   "PyType_GetFlags()" instead.

   Adicionado na versão 3.15.

Py_tp_bases
    * Parte da ABI Estável.*

   "Slot ID" for type flags, used to set "PyTypeObject.tp_bases".

   The slot can be set to a tuple of type objects which the newly
   created type should inherit from, like the "positional arguments"
   of a Python class definition.

   Alternately, the slot can be set to a single type object to specify
   a single base. The effect is the same as specifying a one-element
   tuple.

   Alterado na versão 3.15: Previously, "Py_tp_bases" required a tuple
   of types.

Py_tp_base
    * Parte da ABI Estável.*

   Equivalent to "Py_tp_bases" (with "s" at the end). If both are
   specified, "Py_tp_bases" takes priority and this slot is ignored.

   Alterado na versão 3.15: Previously, "Py_tp_base" required a single
   type, not a tuple.

   Suavemente descontinuado desde a versão 3.15: When not targeting
   older Python versions, prefer "Py_tp_bases".

The following slots do not correspond to public fields in the
underlying structures:

Py_tp_metaclass
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for the metaclass used to construct the resulting type
   object. When omitted the metaclass is derived from bases
   ("Py_tp_bases" or the *bases* argument of
   "PyType_FromMetaclass()").

   Metaclasses that override "tp_new" are not supported, except if
   "tp_new" is "NULL".

   This may not be used in "PyType_Spec.slots". Use
   "PyType_FromMetaclass()" to specify a metaclass with "PyType_Spec".

   This slot may not be used with "PyType_GetSlot()". Use "Py_TYPE()"
   on the type object instead.

   Adicionado na versão 3.15.

Py_tp_module
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" for recording the module in which the new class is
   defined.

   The value must be a module object. The module is associated with
   the new type and can later be retrieved with "PyType_GetModule()".
   The associated module is not inherited by subclasses; it must be
   specified for each class individually.

   This may not be used in "PyType_Spec.slots". Use
   "PyType_FromMetaclass()" to specify a module with "PyType_Spec".

   This slot may not be used with "PyType_GetSlot()". Use
   "PyType_GetModule()" instead.

   Adicionado na versão 3.15.

Py_tp_token
    * Parte da ABI Estável desde a versão 3.14.*

   "Slot ID" for recording a static memory layout ID for a class.

   If the class is defined using a "PyType_Spec", and that spec is
   statically allocated, the token can be set to the spec using the
   special value "Py_TP_USE_SPEC":

      static PyType_Slot foo_slots[] = {
         {Py_tp_token, Py_TP_USE_SPEC},

   It can also be set to an arbitrary pointer, but you must ensure
   that:

   * The pointer outlives the class, so it's not reused for something
     else while the class exists.

   * It "belongs" to the extension module where the class lives, so it
     will not clash with other extensions.

   Use "PyType_GetBaseByToken()" to check if a class's superclass has
   a given token -- that is, check whether the memory layout is
   compatible.

   To get the token for a given class (without considering
   superclasses), use "PyType_GetSlot()" with "Py_tp_token".

   Adicionado na versão 3.14.

   Py_TP_USE_SPEC
       * Parte da ABI Estável desde a versão 3.14.*

      Used as a value with "Py_tp_token" to set the token to the
      class's "PyType_Spec". May only be used for classes defined
      using "PyType_Spec".

      Expands to "NULL".

      Adicionado na versão 3.14.

Py_tp_slots
    * Parte da ABI Estável desde a versão 3.15.*

   "Slot ID" that works like "Py_slot_subslots", except it specifies
   an array of "PyType_Slot" structures.

   Adicionado na versão 3.15.


Soft-deprecated API
===================

The following functions are *soft deprecated*. They will continue to
work, but new features will be added as slots for
"PyType_FromSlots()", not as arguments to new "PyType_From*"
functions.

PyObject *PyType_FromMetaclass(PyTypeObject *metaclass, PyObject *module, PyType_Spec *spec, PyObject *bases)
    * Parte da ABI Estável desde a versão 3.12.*

   Create and return a heap type from the *spec* (see
   "Py_TPFLAGS_HEAPTYPE").

   A non-"NULL" *metaclass* argument corresponds to the
   "Py_tp_metaclass" slot.

   A non-"NULL" *bases* argument corresponds to the "Py_tp_bases"
   slot, and takes precedence over "Py_tp_bases" and "Py_tp_bases"
   slots.

   A non-"NULL" *module* argument corresponds to the "Py_tp_module"
   slot.

   This function calls "PyType_Ready()" on the new type.

   Note that this function does *not* fully match the behavior of
   calling "type()" or using the "class" statement. See the note in
   "PyType_FromSlots()" documentation for details.

   Adicionado na versão 3.12.

   Suavemente descontinuado desde a versão 3.15: Prefer
   "PyType_FromSlots()" in new code.

PyObject *PyType_FromModuleAndSpec(PyObject *module, PyType_Spec *spec, PyObject *bases)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.10.*

   Equivalent to "PyType_FromMetaclass(NULL, module, spec, bases)".

   Adicionado na versão 3.9.

   Alterado na versão 3.10: The function now accepts a single class as
   the *bases* argument and "NULL" as the "tp_doc" slot.

   Alterado na versão 3.12: The function now finds and uses a
   metaclass corresponding to the provided base classes.  Previously,
   only "type" instances were returned.The "tp_new" of the metaclass
   is *ignored*. which may result in incomplete initialization.
   Creating classes whose metaclass overrides "tp_new" is deprecated.

   Alterado na versão 3.14: Creating classes whose metaclass overrides
   "tp_new" is no longer allowed.

   Suavemente descontinuado desde a versão 3.15: Prefer
   "PyType_FromSlots()" in new code.

PyObject *PyType_FromSpecWithBases(PyType_Spec *spec, PyObject *bases)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.3.*

   Equivalent to "PyType_FromMetaclass(NULL, NULL, spec, bases)".

   Adicionado na versão 3.3.

   Alterado na versão 3.12: The function now finds and uses a
   metaclass corresponding to the provided base classes.  Previously,
   only "type" instances were returned.The "tp_new" of the metaclass
   is *ignored*. which may result in incomplete initialization.
   Creating classes whose metaclass overrides "tp_new" is deprecated.

   Alterado na versão 3.14: Creating classes whose metaclass overrides
   "tp_new" is no longer allowed.

   Suavemente descontinuado desde a versão 3.15: Prefer
   "PyType_FromSlots()" in new code.

PyObject *PyType_FromSpec(PyType_Spec *spec)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Equivalent to "PyType_FromMetaclass(NULL, NULL, spec, NULL)".

   Alterado na versão 3.12: The function now finds and uses a
   metaclass corresponding to the base classes provided in
   *Py_tp_base[s]* slots. Previously, only "type" instances were
   returned.The "tp_new" of the metaclass is *ignored*. which may
   result in incomplete initialization. Creating classes whose
   metaclass overrides "tp_new" is deprecated.

   Alterado na versão 3.14: Creating classes whose metaclass overrides
   "tp_new" is no longer allowed.

   Suavemente descontinuado desde a versão 3.15: Prefer
   "PyType_FromSlots()" in new code.

type PyType_Spec
    * Parte da ABI Estável (incluindo todos os membros).*

   Structure defining a type's behavior, used for soft-deprecated
   functions like "PyType_FromMetaclass()".

   This structure contains several members that can instead be
   specified as slots for "PyType_FromSlots()", and an array of slot
   entries with a simpler structure.

   const char *name

      Corresponds to "Py_tp_name".

   int basicsize

      If positive, corresponds to "Py_tp_basicsize".

      If negative, corresponds to "Py_tp_extra_basicsize" set to the
      absolute value.

      Alterado na versão 3.12: Previously, this field could not be
      negative.

   int itemsize

      Corresponds to "Py_tp_itemsize".

   unsigned int flags

      Corresponds to "Py_tp_flags".

   PyType_Slot *slots

      Array of "PyType_Slot" (not "PySlot") structures.

      Terminated by the special slot value "{0, NULL}". Each slot ID
      should be specified at most once.

      type PyType_Slot
          * Parte da ABI Estável (incluindo todos os membros).*

         Structure defining optional functionality of a type, used for
         soft-deprecated functions like "PyType_FromMetaclass()".

         Note that a "PyType_Slot" array may be included in a "PySlot"
         array using "Py_tp_slots", and vice versa using
         "Py_slot_subslots".

         Each "PyType_Slot" structure "tpslot" is interpreted as the
         following "PySlot" structure:

            (PySlot){
               .sl_id=tpslot.slot,
               .sl_flags=PySlot_INTPTR | sub_static,
               .sl_ptr=tpslot.func
            }

         where "sub_static" is "PySlot_STATIC" if the slot requires
         the flag (such as for "Py_tp_methods"), or if this flag is
         present on the "parent" "Py_tp_slots" slot (if any).

         int slot

            Corresponds to "PySlot.sl_id".

         void *pfunc

            Corresponds to "PySlot.sl_ptr".
