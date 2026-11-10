Protocolo de objeto
*******************

PyObject *Py_GetConstant(unsigned int constant_id)
    * Parte da ABI Estável desde a versão 3.13.*

   Obtém uma *referência forte* para uma constante.

   Define uma exceção e retorna "NULL" se *constant_id* for inválido.

   *constant_id* deve ser um destes identificadores constantes:

   +------------------------------------------+-------+---------------------------+
   | Identificador da constante               | Valor | Objeto retornado          |
   |==========================================|=======|===========================|
   | Py_CONSTANT_NONE                         | "0"   | "None"                    |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_FALSE                        | "1"   | "False"                   |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_TRUE                         | "2"   | "True"                    |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_ELLIPSIS                     | "3"   | "Ellipsis"                |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_NOT_IMPLEMENTED              | "4"   | "NotImplemented"          |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_ZERO                         | "5"   | "0"                       |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_ONE                          | "6"   | "1"                       |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_EMPTY_STR                    | "7"   | "''"                      |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_EMPTY_BYTES                  | "8"   | "b''"                     |
   +------------------------------------------+-------+---------------------------+
   | Py_CONSTANT_EMPTY_TUPLE                  | "9"   | "()"                      |
   +------------------------------------------+-------+---------------------------+

   Valores numéricos são fornecidos apenas para projetos que não podem
   usar identificadores constantes.

   Adicionado na versão 3.13.

   No CPython, todas essas constantes são *imortais*.

PyObject *Py_GetConstantBorrowed(unsigned int constant_id)
    * Parte da ABI Estável desde a versão 3.13.*

   Semelhante a "Py_GetConstant()", mas retorna uma *referência
   emprestada*.

   Esta função destina-se principalmente à compatibilidade com versões
   anteriores: usar "Py_GetConstant()" é recomendado para novo código.

   A referência é emprestada do interpretador e é válida até a
   finalização do interpretador.

   Adicionado na versão 3.13.

PyObject *Py_NotImplemented

   O singleton "NotImplemented", usado para sinalizar que uma operação
   não foi implementada para a combinação de tipo fornecida.

Py_RETURN_NOTIMPLEMENTED

   Manipula adequadamente o retorno de "Py_NotImplemented" de dentro
   de uma função C (ou seja, cria uma nova *referência forte* para
   "NotImplemented" e retorna-a).

Py_PRINT_RAW

   Flag to be used with multiple functions that print the object (like
   "PyObject_Print()" and "PyFile_WriteObject()"). If passed, these
   functions use the "str()" of the object instead of the "repr()".

int PyObject_Print(PyObject *o, FILE *fp, int flags)

   Print an object *o*, on file *fp*.  Returns "-1" on error.  The
   flags argument is used to enable certain printing options.  The
   only option currently supported is "Py_PRINT_RAW"; if given, the
   "str()" of the object is written instead of the "repr()".

void PyObject_Dump(PyObject *op)

   Dump an object *op* to "stderr". This should only be used for
   debugging.

   The output is intended to try dumping objects even after memory
   corruption:

   * Information is written starting with fields that are the least
     likely to crash when accessed.

   * This function can be called without an *attached thread state*,
     but it's not recommended to do so: it can cause deadlocks.

   * An object that does not belong to the current interpreter may be
     dumped, but this may also cause crashes or unintended behavior.

   * Implement a heuristic to detect if the object memory has been
     freed. Don't display the object contents in this case, only its
     memory address.

   * The output format may change at any time.

   Example of output:

      object address  : 0x7f80124702c0
      object refcount : 2
      object type     : 0x9902e0
      object type name: str
      object repr     : 'abcdef'

   Adicionado na versão 3.15.

int PyObject_HasAttrWithError(PyObject *o, PyObject *attr_name)
    * Parte da ABI Estável desde a versão 3.13.*

   Returns "1" if *o* has the attribute *attr_name*, and "0"
   otherwise. This is equivalent to the Python expression "hasattr(o,
   attr_name)". On failure, return "-1".

   Adicionado na versão 3.13.

int PyObject_HasAttrStringWithError(PyObject *o, const char *attr_name)
    * Parte da ABI Estável desde a versão 3.13.*

   This is the same as "PyObject_HasAttrWithError()", but *attr_name*
   is specified as a const char* UTF-8 encoded bytes string, rather
   than a PyObject*.

   Adicionado na versão 3.13.

int PyObject_HasAttr(PyObject *o, PyObject *attr_name)
    * Parte da ABI Estável.*

   Returns "1" if *o* has the attribute *attr_name*, and "0"
   otherwise. This function always succeeds.

   Nota:

     Exceptions that occur when this calls "__getattr__()" and
     "__getattribute__()" methods aren't propagated, but instead given
     to "sys.unraisablehook()". For proper error handling, use
     "PyObject_HasAttrWithError()", "PyObject_GetOptionalAttr()" or
     "PyObject_GetAttr()" instead.

int PyObject_HasAttrString(PyObject *o, const char *attr_name)
    * Parte da ABI Estável.*

   This is the same as "PyObject_HasAttr()", but *attr_name* is
   specified as a const char* UTF-8 encoded bytes string, rather than
   a PyObject*.

   Nota:

     Exceptions that occur when this calls "__getattr__()" and
     "__getattribute__()" methods or while creating the temporary
     "str" object are silently ignored. For proper error handling, use
     "PyObject_HasAttrStringWithError()",
     "PyObject_GetOptionalAttrString()" or "PyObject_GetAttrString()"
     instead.

PyObject *PyObject_GetAttr(PyObject *o, PyObject *attr_name)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retrieve an attribute named *attr_name* from object *o*. Returns
   the attribute value on success, or "NULL" on failure.  This is the
   equivalent of the Python expression "o.attr_name".

   If the missing attribute should not be treated as a failure, you
   can use "PyObject_GetOptionalAttr()" instead.

PyObject *PyObject_GetAttrString(PyObject *o, const char *attr_name)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   This is the same as "PyObject_GetAttr()", but *attr_name* is
   specified as a const char* UTF-8 encoded bytes string, rather than
   a PyObject*.

   If the missing attribute should not be treated as a failure, you
   can use "PyObject_GetOptionalAttrString()" instead.

int PyObject_GetOptionalAttr(PyObject *obj, PyObject *attr_name, PyObject **result);
    * Parte da ABI Estável desde a versão 3.13.*

   Variant of "PyObject_GetAttr()" which doesn't raise
   "AttributeError" if the attribute is not found.

   If the attribute is found, return "1" and set **result* to a new
   *strong reference* to the attribute. If the attribute is not found,
   return "0" and set **result* to "NULL"; the "AttributeError" is
   silenced. If an error other than "AttributeError" is raised, return
   "-1" and set **result* to "NULL".

   Adicionado na versão 3.13.

int PyObject_GetOptionalAttrString(PyObject *obj, const char *attr_name, PyObject **result);
    * Parte da ABI Estável desde a versão 3.13.*

   This is the same as "PyObject_GetOptionalAttr()", but *attr_name*
   is specified as a const char* UTF-8 encoded bytes string, rather
   than a PyObject*.

   Adicionado na versão 3.13.

PyObject *PyObject_GenericGetAttr(PyObject *o, PyObject *name)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Generic attribute getter function that is meant to be put into a
   type object's "tp_getattro" slot.  It looks for a descriptor in the
   dictionary of classes in the object's MRO as well as an attribute
   in the object's "__dict__" (if present).  As outlined in
   Implementando descritores, data descriptors take preference over
   instance attributes, while non-data descriptors don't.  Otherwise,
   an "AttributeError" is raised.

int PyObject_SetAttr(PyObject *o, PyObject *attr_name, PyObject *v)
    * Parte da ABI Estável.*

   Set the value of the attribute named *attr_name*, for object *o*,
   to the value *v*. Raise an exception and return "-1" on failure;
   return "0" on success.  This is the equivalent of the Python
   statement "o.attr_name = v".

   If *v* is "NULL", the attribute is deleted. This behaviour is
   deprecated in favour of using "PyObject_DelAttr()", but there are
   currently no plans to remove it.

   The function must not be called with a "NULL" *v* and an exception
   set. This case can arise from forgetting "NULL" checks and would
   delete the attribute.

   Alterado na versão 3.15: Must not be called with NULL value if an
   exception is set.

int PyObject_SetAttrString(PyObject *o, const char *attr_name, PyObject *v)
    * Parte da ABI Estável.*

   This is the same as "PyObject_SetAttr()", but *attr_name* is
   specified as a const char* UTF-8 encoded bytes string, rather than
   a PyObject*.

   If *v* is "NULL", the attribute is deleted, but this feature is
   deprecated in favour of using "PyObject_DelAttrString()".

   The function must not be called with a "NULL" *v* and an exception
   set. This case can arise from forgetting "NULL" checks and would
   delete the attribute.

   The number of different attribute names passed to this function
   should be kept small, usually by using a statically allocated
   string as *attr_name*. For attribute names that aren't known at
   compile time, prefer calling "PyUnicode_FromString()" and
   "PyObject_SetAttr()" directly. For more details, see
   "PyUnicode_InternFromString()", which may be used internally to
   create a key object.

   Alterado na versão 3.15: Must not be called with NULL value if an
   exception is set.

int PyObject_GenericSetAttr(PyObject *o, PyObject *name, PyObject *value)
    * Parte da ABI Estável.*

   Generic attribute setter and deleter function that is meant to be
   put into a type object's "tp_setattro" slot.  It looks for a data
   descriptor in the dictionary of classes in the object's MRO, and if
   found it takes preference over setting or deleting the attribute in
   the instance dictionary. Otherwise, the attribute is set or deleted
   in the object's "__dict__" (if present). On success, "0" is
   returned, otherwise an "AttributeError" is raised and "-1" is
   returned.

int PyObject_DelAttr(PyObject *o, PyObject *attr_name)
    * Parte da ABI Estável desde a versão 3.13.*

   Delete attribute named *attr_name*, for object *o*. Returns "-1" on
   failure. This is the equivalent of the Python statement "del
   o.attr_name".

int PyObject_DelAttrString(PyObject *o, const char *attr_name)
    * Parte da ABI Estável desde a versão 3.13.*

   This is the same as "PyObject_DelAttr()", but *attr_name* is
   specified as a const char* UTF-8 encoded bytes string, rather than
   a PyObject*.

   The number of different attribute names passed to this function
   should be kept small, usually by using a statically allocated
   string as *attr_name*. For attribute names that aren't known at
   compile time, prefer calling "PyUnicode_FromString()" and
   "PyObject_DelAttr()" directly. For more details, see
   "PyUnicode_InternFromString()", which may be used internally to
   create a key object for lookup.

PyObject *PyObject_GenericGetDict(PyObject *o, void *context)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.10.*

   A generic implementation for the getter of a "__dict__" descriptor.
   It creates the dictionary if necessary.

   This function may also be called to get the "__dict__" of the
   object *o*. Pass "NULL" for *context* when calling it. Since this
   function may need to allocate memory for the dictionary, it may be
   more efficient to call "PyObject_GetAttr()" when accessing an
   attribute on the object.

   On failure, returns "NULL" with an exception set.

   Adicionado na versão 3.3.

int PyObject_GenericSetDict(PyObject *o, PyObject *value, void *context)
    * Parte da ABI Estável desde a versão 3.7.*

   A generic implementation for the setter of a "__dict__" descriptor.
   This implementation does not allow the dictionary to be deleted.

   Adicionado na versão 3.3.

PyObject **_PyObject_GetDictPtr(PyObject *obj)

   Return a pointer to "__dict__" of the object *obj*. If there is no
   "__dict__", return "NULL" without setting an exception.

   This function may need to allocate memory for the dictionary, so it
   may be more efficient to call "PyObject_GetAttr()" when accessing
   an attribute on the object.

PyObject *PyObject_RichCompare(PyObject *o1, PyObject *o2, int opid)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Compare the values of *o1* and *o2* using the operation specified
   by *opid*, which must be one of "Py_LT", "Py_LE", "Py_EQ", "Py_NE",
   "Py_GT", or "Py_GE", corresponding to "<", "<=", "==", "!=", ">",
   or ">=" respectively. This is the equivalent of the Python
   expression "o1 op o2", where "op" is the operator corresponding to
   *opid*. Returns the value of the comparison on success, or "NULL"
   on failure.

int PyObject_RichCompareBool(PyObject *o1, PyObject *o2, int opid)
    * Parte da ABI Estável.*

   Compare the values of *o1* and *o2* using the operation specified
   by *opid*, like "PyObject_RichCompare()", but returns "-1" on
   error, "0" if the result is false, "1" otherwise.

Nota:

  If *o1* and *o2* are the same object, "PyObject_RichCompareBool()"
  will always return "1" for "Py_EQ" and "0" for "Py_NE".

PyObject *PyObject_Format(PyObject *obj, PyObject *format_spec)
    * Parte da ABI Estável.*

   Format *obj* using *format_spec*. This is equivalent to the Python
   expression "format(obj, format_spec)".

   *format_spec* may be "NULL". In this case the call is equivalent to
   "format(obj)". Returns the formatted string on success, "NULL" on
   failure.

PyObject *PyObject_Repr(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Compute a string representation of object *o*.  Returns the string
   representation on success, "NULL" on failure.  This is the
   equivalent of the Python expression "repr(o)".  Called by the
   "repr()" built-in function.

   If argument is "NULL", return the string "'<NULL>'".

   Alterado na versão 3.4: Essa função agora inclui uma asserção de
   depuração para ajudar a garantir que ela não descarte
   silenciosamente uma exceção ativa.

PyObject *PyObject_ASCII(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   As "PyObject_Repr()", compute a string representation of object
   *o*, but escape the non-ASCII characters in the string returned by
   "PyObject_Repr()" with "\x", "\u" or "\U" escapes.  This generates
   a string similar to that returned by "PyObject_Repr()" in Python 2.
   Called by the "ascii()" built-in function.

   If argument is "NULL", return the string "'<NULL>'".

PyObject *PyObject_Str(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Compute a string representation of object *o*.  Returns the string
   representation on success, "NULL" on failure.  This is the
   equivalent of the Python expression "str(o)".  Called by the
   "str()" built-in function and, therefore, by the "print()"
   function.

   If argument is "NULL", return the string "'<NULL>'".

   Alterado na versão 3.4: Essa função agora inclui uma asserção de
   depuração para ajudar a garantir que ela não descarte
   silenciosamente uma exceção ativa.

PyObject *PyObject_Bytes(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Compute a bytes representation of object *o*.  "NULL" is returned
   on failure and a bytes object on success.  This is equivalent to
   the Python expression "bytes(o)", when *o* is not an integer.
   Unlike "bytes(o)", a TypeError is raised when *o* is an integer
   instead of a zero-initialized bytes object.

   If argument is "NULL", return the "bytes" object "b'<NULL>'".

int PyObject_IsSubclass(PyObject *derived, PyObject *cls)
    * Parte da ABI Estável.*

   Return "1" if the class *derived* is identical to or derived from
   the class *cls*, otherwise return "0".  In case of an error, return
   "-1".

   If *cls* is a tuple, the check will be done against every entry in
   *cls*. The result will be "1" when at least one of the checks
   returns "1", otherwise it will be "0".

   If *cls* has a "__subclasscheck__()" method, it will be called to
   determine the subclass status as described in **PEP 3119**.
   Otherwise, *derived* is a subclass of *cls* if it is a direct or
   indirect subclass, i.e. contained in "cls.__mro__".

   Normally only class objects, i.e. instances of "type" or a derived
   class, are considered classes.  However, objects can override this
   by having a "__bases__" attribute (which must be a tuple of base
   classes).

int PyObject_IsInstance(PyObject *inst, PyObject *cls)
    * Parte da ABI Estável.*

   Return "1" if *inst* is an instance of the class *cls* or a
   subclass of *cls*, or "0" if not.  On error, returns "-1" and sets
   an exception.

   If *cls* is a tuple, the check will be done against every entry in
   *cls*. The result will be "1" when at least one of the checks
   returns "1", otherwise it will be "0".

   If *cls* has a "__instancecheck__()" method, it will be called to
   determine the subclass status as described in **PEP 3119**.
   Otherwise, *inst* is an instance of *cls* if its class is a
   subclass of *cls*.

   An instance *inst* can override what is considered its class by
   having a "__class__" attribute.

   An object *cls* can override if it is considered a class, and what
   its base classes are, by having a "__bases__" attribute (which must
   be a tuple of base classes).

Py_hash_t PyObject_Hash(PyObject *o)
    * Parte da ABI Estável.*

   Compute and return the hash value of an object *o*.  On failure,
   return "-1". This is the equivalent of the Python expression
   "hash(o)".

   Alterado na versão 3.2: The return type is now Py_hash_t.  This is
   a signed integer the same size as "Py_ssize_t".

Py_hash_t PyObject_HashNotImplemented(PyObject *o)
    * Parte da ABI Estável.*

   Set a "TypeError" indicating that "type(o)" is not *hashable* and
   return "-1". This function receives special treatment when stored
   in a "tp_hash" slot, allowing a type to explicitly indicate to the
   interpreter that it is not hashable.

int PyObject_IsTrue(PyObject *o)
    * Parte da ABI Estável.*

   Returns "1" if the object *o* is considered to be true, and "0"
   otherwise. This is equivalent to the Python expression "not not o".
   On failure, return "-1".

int PyObject_Not(PyObject *o)
    * Parte da ABI Estável.*

   Returns "0" if the object *o* is considered to be true, and "1"
   otherwise. This is equivalent to the Python expression "not o".  On
   failure, return "-1".

PyObject *PyObject_Type(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   When *o* is non-"NULL", returns a type object corresponding to the
   object type of object *o*. On failure, raises "SystemError" and
   returns "NULL".  This is equivalent to the Python expression
   "type(o)". This function creates a new *strong reference* to the
   return value. There's really no reason to use this function instead
   of the "Py_TYPE()" function, which returns a pointer of type
   PyTypeObject*, except when a new *strong reference* is needed.

int PyObject_TypeCheck(PyObject *o, PyTypeObject *type)

   Return non-zero if the object *o* is of type *type* or a subtype of
   *type*, and "0" otherwise.  Both parameters must be non-"NULL".

Py_ssize_t PyObject_Size(PyObject *o)
Py_ssize_t PyObject_Length(PyObject *o)
    * Parte da ABI Estável.*

   Return the length of object *o*.  If the object *o* provides either
   the sequence and mapping protocols, the sequence length is
   returned.  On error, "-1" is returned.  This is the equivalent to
   the Python expression "len(o)".

Py_ssize_t PyObject_LengthHint(PyObject *o, Py_ssize_t defaultvalue)

   Return an estimated length for the object *o*. First try to return
   its actual length, then an estimate using "__length_hint__()", and
   finally return the default value. On error return "-1". This is the
   equivalent to the Python expression "operator.length_hint(o,
   defaultvalue)".

   Adicionado na versão 3.4.

PyObject *PyObject_GetItem(PyObject *o, PyObject *key)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return element of *o* corresponding to the object *key* or "NULL"
   on failure. This is the equivalent of the Python expression
   "o[key]".

int PyObject_SetItem(PyObject *o, PyObject *key, PyObject *v)
    * Parte da ABI Estável.*

   Map the object *key* to the value *v*.  Raise an exception and
   return "-1" on failure; return "0" on success.  This is the
   equivalent of the Python statement "o[key] = v".  This function
   *does not* steal a reference to *v*.

int PyObject_DelItem(PyObject *o, PyObject *key)
    * Parte da ABI Estável.*

   Remove the mapping for the object *key* from the object *o*.
   Return "-1" on failure.  This is equivalent to the Python statement
   "del o[key]".

int PyObject_DelItemString(PyObject *o, const char *key)
    * Parte da ABI Estável.*

   É o mesmo que "PyObject_DelItem()", mas *key* é especificada como
   uma string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

PyObject *PyObject_Dir(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   This is equivalent to the Python expression "dir(o)", returning a
   (possibly empty) list of strings appropriate for the object
   argument, or "NULL" if there was an error.  If the argument is
   "NULL", this is like the Python "dir()", returning the names of the
   current locals; in this case, if no execution frame is active then
   "NULL" is returned but "PyErr_Occurred()" will return false.

PyObject *PyObject_GetIter(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   This is equivalent to the Python expression "iter(o)". It returns a
   new iterator for the object argument, or the object  itself if the
   object is already an iterator.  Raises "TypeError" and returns
   "NULL" if the object cannot be iterated.

PyObject *PyObject_SelfIter(PyObject *obj)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   This is equivalent to the Python "__iter__(self): return self"
   method. It is intended for *iterator* types, to be used in the
   "PyTypeObject.tp_iter" slot.

PyObject *PyObject_GetAIter(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.10.*

   This is the equivalent to the Python expression "aiter(o)". Takes
   an "AsyncIterable" object and returns an "AsyncIterator" for it.
   This is typically a new iterator but if the argument is an
   "AsyncIterator", this returns itself. Raises "TypeError" and
   returns "NULL" if the object cannot be iterated.

   Adicionado na versão 3.10.

void *PyObject_GetTypeData(PyObject *o, PyTypeObject *cls)
    * Parte da ABI Estável desde a versão 3.12.*

   Get a pointer to subclass-specific data reserved for *cls*.

   The object *o* must be an instance of *cls*, and *cls* must have
   been created using negative "PyType_Spec.basicsize". Python does
   not check this.

   On error, set an exception and return "NULL".

   Adicionado na versão 3.12.

Py_ssize_t PyType_GetTypeDataSize(PyTypeObject *cls)
    * Parte da ABI Estável desde a versão 3.12.*

   Return the size of the instance memory space reserved for *cls*,
   i.e. the size of the memory "PyObject_GetTypeData()" returns.

   This may be larger than requested using "-PyType_Spec.basicsize";
   it is safe to use this larger size (e.g. with "memset()").

   The type *cls* **must** have been created using negative
   "PyType_Spec.basicsize". Python does not check this.

   On error, set an exception and return a negative value.

   Adicionado na versão 3.12.

void *PyObject_GetItemData(PyObject *o)

   Get a pointer to per-item data for a class with
   "Py_TPFLAGS_ITEMS_AT_END".

   On error, set an exception and return "NULL". "TypeError" is raised
   if *o* does not have "Py_TPFLAGS_ITEMS_AT_END" set.

   Adicionado na versão 3.12.

int PyObject_VisitManagedDict(PyObject *obj, visitproc visit, void *arg)

   Visit the managed dictionary of *obj*.

   This function must only be called in a traverse function of the
   type which has the "Py_TPFLAGS_MANAGED_DICT" flag set.

   Adicionado na versão 3.13.

void PyObject_ClearManagedDict(PyObject *obj)

   Clear the managed dictionary of *obj*.

   This function must only be called in a clear function of the type
   which has the "Py_TPFLAGS_MANAGED_DICT" flag set.

   Adicionado na versão 3.13.

int PyUnstable_Object_EnableDeferredRefcount(PyObject *obj)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Enable deferred reference counting on *obj*, if supported by the
   runtime.  In the *free-threaded* build, this allows the interpreter
   to avoid reference count adjustments to *obj*, which may improve
   multi-threaded performance.  The tradeoff is that *obj* will only
   be deallocated by the tracing garbage collector, and not when the
   interpreter no longer has any references to it.

   This function returns "1" if deferred reference counting is enabled
   on *obj*, and "0" if deferred reference counting is not supported
   or if the hint was ignored by the interpreter, such as when
   deferred reference counting is already enabled on *obj*. This
   function is thread-safe, and cannot fail.

   This function does nothing on builds with the *GIL* enabled, which
   do not support deferred reference counting. This also does nothing
   if *obj* is not an object tracked by the garbage collector (see
   "gc.is_tracked()" and "PyObject_GC_IsTracked()").

   This function is intended to be used soon after *obj* is created,
   by the code that creates it, such as in the object's "tp_new" slot.

   Adicionado na versão 3.14.

int PyUnstable_Object_IsUniqueReferencedTemporary(PyObject *obj)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Check if *obj* is a unique temporary object. Returns "1" if *obj*
   is known to be a unique temporary object, and "0" otherwise.  This
   function cannot fail, but the check is conservative, and may return
   "0" in some cases even if *obj* is a unique temporary object.

   If an object is a unique temporary, it is guaranteed that the
   current code has the only reference to the object. For arguments to
   C functions, this should be used instead of checking if the
   reference count is "1". Starting with Python 3.14, the interpreter
   internally avoids some reference count modifications when loading
   objects onto the operands stack by *borrowing* references when
   possible, which means that a reference count of "1" by itself does
   not guarantee that a function argument uniquely referenced.

   In the example below, "my_func" is called with a unique temporary
   object as its argument:

      my_func([1, 2, 3])

   In the example below, "my_func" is **not** called with a unique
   temporary object as its argument, even if its refcount is "1":

      my_list = [1, 2, 3]
      my_func(my_list)

   See also the function "Py_REFCNT()".

   Adicionado na versão 3.14.

int PyUnstable_IsImmortal(PyObject *obj)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Essa função retorna um valor diferente de zero se *obj* for
   *immortal*, e zero caso contrário. Essa função nunca falha.

   Nota:

     Objetos que são imortais em um versão do CPython não têm garantia
     de ser imortal em outro.

   Adicionado na versão 3.14.

int PyUnstable_TryIncRef(PyObject *obj)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Increments the reference count of *obj* if it is not zero.  Returns
   "1" if the object's reference count was successfully incremented.
   Otherwise, this function returns "0".

   "PyUnstable_EnableTryIncRef()" must have been called earlier on
   *obj* or this function may spuriously return "0" in the *free-
   threaded build*.

   This function is logically equivalent to the following C code,
   except that it behaves atomically in the *free-threaded build*:

      if (Py_REFCNT(op) > 0) {
         Py_INCREF(op);
         return 1;
      }
      return 0;

   This is intended as a building block for managing weak references
   without the overhead of a Python weak reference object.

   Typically, correct use of this function requires support from
   *obj*'s deallocator ("tp_dealloc"). For example, the following
   sketch could be adapted to implement a "weakmap" that works like a
   "WeakValueDictionary" for a specific type:

      PyMutex mutex;

      PyObject *
      add_entry(weakmap_key_type *key, PyObject *value)
      {
          PyUnstable_EnableTryIncRef(value);
          weakmap_type weakmap = ...;
          PyMutex_Lock(&mutex);
          weakmap_add_entry(weakmap, key, value);
          PyMutex_Unlock(&mutex);
          Py_RETURN_NONE;
      }

      PyObject *
      get_value(weakmap_key_type *key)
      {
          weakmap_type weakmap = ...;
          PyMutex_Lock(&mutex);
          PyObject *result = weakmap_find(weakmap, key);
          if (PyUnstable_TryIncRef(result)) {
              // `result` is safe to use
              PyMutex_Unlock(&mutex);
              return result;
          }
          // if we get here, `result` is starting to be garbage-collected,
          // but has not been removed from the weakmap yet
          PyMutex_Unlock(&mutex);
          return NULL;
      }

      // tp_dealloc function for weakmap values
      void
      value_dealloc(PyObject *value)
      {
          weakmap_type weakmap = ...;
          PyMutex_Lock(&mutex);
          weakmap_remove_value(weakmap, value);

          ...
          PyMutex_Unlock(&mutex);
      }

   Adicionado na versão 3.14.

void PyUnstable_EnableTryIncRef(PyObject *obj)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Enables subsequent uses of "PyUnstable_TryIncRef()" on *obj*.  The
   caller must hold a *strong reference* to *obj* when calling this.

   Adicionado na versão 3.14.

int PyUnstable_Object_IsUniquelyReferenced(PyObject *op)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Determine if *op* only has one reference.

   On GIL-enabled builds, this function is equivalent to Py_REFCNT(op)
   == 1.

   On a *free-threaded build*, this checks if *op*'s *reference count*
   is equal to one and additionally checks if *op* is only used by
   this thread. Py_REFCNT(op) == 1 is **not** thread-safe on free-
   threaded builds; prefer this function.

   The caller must hold an *attached thread state*, despite the fact
   that this function doesn't call into the Python interpreter. This
   function cannot fail.

   Adicionado na versão 3.14.

int PyUnstable_SetImmortal(PyObject *op)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Marks the object *op* *immortal*. The argument should be uniquely
   referenced by the calling thread. This is intended to be used for
   reducing reference counting contention in the *free-threaded build*
   for objects which are shared across threads.

   This is a one-way process: objects can only be made immortal; they
   cannot be made mortal once again. Immortal objects do not
   participate in reference counting and will never be garbage
   collected. If the object is GC-tracked, it is untracked.

   This function is intended to be used soon after *op* is created, by
   the code that creates it, such as in the object's "tp_new" slot.
   Returns 1 if the object was made immortal and returns 0 if it was
   not. This function cannot fail.

   Adicionado na versão 3.15.
