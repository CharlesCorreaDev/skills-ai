Estruturas comuns de objetos
****************************

Existe um grande número de estruturas usadas para a definição de tipos
objeto para o Python. Esta seção descreve essas estruturas e como são
usadas.


Macros e tipos de objetos base
==============================

Todos os objetos Python por fim compartilham um pequeno número de
campos no começo da representação o objeto na memória. Esses são
representados pelos tipos "PyObject" e "PyVarObject", que são
definidos, por sua vez, pelas expansões de alguns macros também,
utilizados, direta ou indiretamente, na definição de todos outros
objetos Python. Macros adicionais podem ser encontrados em contagem de
referências.

type PyObject
    * Parte da ABI Estável (see below).*

   Todos os tipos de objeto são extensões deste tipo. Este é um tipo
   que contém as informações necessárias para que o Python trate um
   ponteiro para um objeto como tal. Em uma versão de "lançamento"
   normal, ele contém apenas a contagem de referências do objeto e um
   ponteiro para o objeto do tipo correspondente. Nada é declarado
   como um "PyObject", mas todo ponteiro para um objeto Python pode
   ser convertido para um PyObject*.

   Os membros não devem ser acessados diretamente; em vez disso, use
   macros como "Py_REFCNT" e "Py_TYPE".

   In the Stable ABI for Free-Threaded Builds ("abi3t"), this struct
   is opaque; its size and layout may change between Python versions.
   In Stable ABI for non-free-threaded builds ("abi3"), the
   "ob_refcnt" and "ob_type" fields are available, but using them
   directly is discouraged.

   Py_ssize_t ob_refcnt
       * Parte da ABI Estável.*

      A contagem de referências do objeto, conforme retornada por
      "Py_REFCNT". Não use este campo diretamente; em vez disso, use
      funções e macros como "Py_REFCNT", "Py_INCREF()" e
      "Py_DecRef()".

      O tipo de campo pode ser diferente de "Py_ssize_t", dependendo
      da configuração e da plataforma de construção.

   PyTypeObject *ob_type
       * Parte da ABI Estável.*

      O tipo do objeto. Não use este campo diretamente; use "Py_TYPE"
      e "Py_SET_TYPE()" em vez disso.

   PyMutex ob_mutex

      A per-object lock, present only in the *free-threaded* build
      (when "Py_GIL_DISABLED" is defined).

      This field is **reserved for use by the critical section API**
      ("Py_BEGIN_CRITICAL_SECTION" / "Py_END_CRITICAL_SECTION"). Do
      **not** lock it directly with "PyMutex_Lock"; doing so can cause
      deadlocks.  If you need your own lock, add a separate "PyMutex"
      field to your object struct.

      Adicionado na versão 3.13.

type PyVarObject
    * Parte da ABI Estável (see below).*

   Uma extensão de "PyObject" que adiciona o campo "ob_size". Isso se
   destina a objetos que possuem alguma noção de *comprimento*.

   Assim como com "PyObject", os membros não devem ser acessados
   diretamente; em vez disso, use macros como "Py_SIZE", "Py_REFCNT" e
   "Py_TYPE".

   In the Stable ABI for Free-Threaded Builds ("abi3t"), this struct
   is opaque; its size and layout may change between Python versions.
   In Stable ABI for non-free-threaded builds ("abi3"), the "ob_base"
   and "ob_size" fields are available, but using them directly is
   discouraged.

   PyObject ob_base
       * Parte da ABI Estável.*

      Common object header. Typically, this field is not accessed
      directly; instead "PyVarObject" can be cast to "PyObject".

   Py_ssize_t ob_size
       * Parte da ABI Estável.*

      Um campo de tamanho, cujo conteúdo deve ser considerado um
      detalhe de implementação interna do objeto.

      Não utilize este campo diretamente; utilize "Py_SIZE" em vez
      disso.

      Funções de criação de objetos, como "PyObject_NewVar()",
      geralmente definem este campo com o tamanho solicitado (número
      de itens). Após a criação, valores arbitrários podem ser
      armazenados em "ob_size" usando "Py_SET_SIZE".

      Para obter o comprimento publicamente exposto de um objeto,
      conforme retornado pela função Python "len()", use
      "PyObject_Length()" em vez disso.

PyObject_HEAD

   Este é um macro usado ao declarar novos tipos que representam
   objetos sem comprimento variável. O macro PyObject_HEAD se expande
   para:

      PyObject ob_base;

   Veja documentação de "PyObject" acima.

PyObject_VAR_HEAD

   Esta é uma macro usada ao declarar novos tipos que representam
   objetos com um comprimento que varia de instância para instância. A
   macro PyObject_VAR_HEAD se expande para:

      PyVarObject ob_base;

   Veja documentação de "PyVarObject" acima.

PyTypeObject PyBaseObject_Type
    * Parte da ABI Estável.*

   A classe base de todos os outros objetos, equivalente a "object" em
   Python.

int Py_Is(PyObject *x, PyObject *y)
    * Parte da ABI Estável desde a versão 3.10.*

   Testa se o objeto *x* é o objeto *y*, o mesmo que "x is y" em
   Python.

   Adicionado na versão 3.10.

int Py_IsNone(PyObject *x)
    * Parte da ABI Estável desde a versão 3.10.*

   Test if an object is the "None" singleton, the same as "x is None"
   in Python.

   Adicionado na versão 3.10.

int Py_IsTrue(PyObject *x)
    * Parte da ABI Estável desde a versão 3.10.*

   Test if an object is the "True" singleton, the same as "x is True"
   in Python.

   Adicionado na versão 3.10.

int Py_IsFalse(PyObject *x)
    * Parte da ABI Estável desde a versão 3.10.*

   Test if an object is the "False" singleton, the same as "x is
   False" in Python.

   Adicionado na versão 3.10.

PyTypeObject *Py_TYPE(PyObject *o)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável
   desde a versão 3.14.*

   Get the type of the Python object *o*.

   The returned reference is *borrowed* from *o*. Do not release it
   with "Py_DECREF()" or similar.

   Alterado na versão 3.11: "Py_TYPE()" is changed to an inline static
   function. The parameter type is no longer const PyObject*.

int Py_IS_TYPE(PyObject *o, PyTypeObject *type)
    * Parte da ABI Estável desde a versão 3.15.*

   Return non-zero if the object *o* type is *type*. Return zero
   otherwise. Equivalent to: "Py_TYPE(o) == type".

   Adicionado na versão 3.9.

void Py_SET_TYPE(PyObject *o, PyTypeObject *type)
    * This macro is available when compiling for the ABI Estável desde
   a versão 3.9.*

   Set the type of object *o* to *type*, without any checking or
   reference counting.

   This is a very low-level operation. Consider instead setting the
   Python attribute "__class__" using "PyObject_SetAttrString()" or
   similar.

   Note that assigning an incompatible type can lead to undefined
   behavior.

   If *type* is a heap type, the caller must create a new reference to
   it. Similarly, if the old type of *o* is a heap type, the caller
   must release a reference to that type.

   Adicionado na versão 3.9.

Py_ssize_t Py_SIZE(PyVarObject *o)
    * Parte da ABI Estável desde a versão 3.15.*

   Get the "ob_size" field of *o*.

   Alterado na versão 3.11: "Py_SIZE()" is changed to an inline static
   function. The parameter type is no longer const PyVarObject*.

void Py_SET_SIZE(PyVarObject *o, Py_ssize_t size)
    * Parte da ABI Estável desde a versão 3.15.*

   Set the "ob_size" field of *o* to *size*.

   Adicionado na versão 3.9.

PyObject_HEAD_INIT(type)

   This is a macro which expands to initialization values for a new
   "PyObject" type.  This macro expands to:

      _PyObject_EXTRA_INIT
      1, type,

PyVarObject_HEAD_INIT(type, size)

   This is a macro which expands to initialization values for a new
   "PyVarObject" type, including the "ob_size" field. This macro
   expands to:

      _PyObject_EXTRA_INIT
      1, type, size,


Implementing functions and methods
==================================

type PyCFunction
    * Parte da ABI Estável.*

   Type of the functions used to implement most Python callables in C.
   Functions of this type take two PyObject* parameters and return one
   such value.  If the return value is "NULL", an exception shall have
   been set.  If not "NULL", the return value is interpreted as the
   return value of the function as exposed in Python.  The function
   must return a new reference.

   A assinatura da função é:

      PyObject *PyCFunction(PyObject *self,
                            PyObject *args);

type PyCFunctionWithKeywords
    * Parte da ABI Estável.*

   Type of the functions used to implement Python callables in C with
   signature METH_VARARGS | METH_KEYWORDS. The function signature is:

      PyObject *PyCFunctionWithKeywords(PyObject *self,
                                        PyObject *args,
                                        PyObject *kwargs);

type PyCFunctionFast
    * Parte da ABI Estável desde a versão 3.13.*

   Type of the functions used to implement Python callables in C with
   signature "METH_FASTCALL". The function signature is:

      PyObject *PyCFunctionFast(PyObject *self,
                                PyObject *const *args,
                                Py_ssize_t nargs);

type PyCFunctionFastWithKeywords
    * Parte da ABI Estável desde a versão 3.13.*

   Type of the functions used to implement Python callables in C with
   signature METH_FASTCALL | METH_KEYWORDS. The function signature is:

      PyObject *PyCFunctionFastWithKeywords(PyObject *self,
                                            PyObject *const *args,
                                            Py_ssize_t nargs,
                                            PyObject *kwnames);

type PyCMethod

   Type of the functions used to implement Python callables in C with
   signature METH_METHOD | METH_FASTCALL | METH_KEYWORDS. The function
   signature is:

      PyObject *PyCMethod(PyObject *self,
                          PyTypeObject *defining_class,
                          PyObject *const *args,
                          Py_ssize_t nargs,
                          PyObject *kwnames)

   Adicionado na versão 3.9.

type PyMethodDef
    * Parte da ABI Estável (incluindo todos os membros).*

   Structure used to describe a method of an extension type.  This
   structure has four fields:

   const char *ml_name

      Nome do método.

      A "NULL" *ml_name* marks the end of a "PyMethodDef" array.

   PyCFunction ml_meth

      Pointer to the C implementation.

   int ml_flags

      Flags bits indicating how the call should be constructed.

   const char *ml_doc

      Points to the contents of the docstring.

The "ml_meth" is a C function pointer. The functions may be of
different types, but they always return PyObject*.  If the function is
not of the "PyCFunction", the compiler will require a cast in the
method table. Even though "PyCFunction" defines the first parameter as
PyObject*, it is common that the method implementation uses the
specific C type of the *self* object.

The "ml_flags" field is a bitfield which can include the following
flags. The individual flags indicate either a calling convention or a
binding convention.

There are these calling conventions:

METH_VARARGS
    * Parte da ABI Estável.*

   This is the typical calling convention, where the methods have the
   type "PyCFunction". The function expects two PyObject* values. The
   first one is the *self* object for methods; for module functions,
   it is the module object.  The second parameter (often called
   *args*) is a tuple object representing all arguments. This
   parameter is typically processed using "PyArg_ParseTuple()" or
   "PyArg_UnpackTuple()".

METH_KEYWORDS

   Can only be used in certain combinations with other flags:
   METH_VARARGS | METH_KEYWORDS, METH_FASTCALL | METH_KEYWORDS and
   METH_METHOD | METH_FASTCALL | METH_KEYWORDS.

METH_VARARGS | METH_KEYWORDS
   Methods with these flags must be of type "PyCFunctionWithKeywords".
   The function expects three parameters: *self*, *args*, *kwargs*
   where *kwargs* is a dictionary of all the keyword arguments or
   possibly "NULL" if there are no keyword arguments.  The parameters
   are typically processed using "PyArg_ParseTupleAndKeywords()".

METH_FASTCALL
    * Parte da ABI Estável desde a versão 3.10.*

   Fast calling convention supporting only positional arguments. The
   methods have the type "PyCFunctionFast". The first parameter is
   *self*, the second parameter is a C array of PyObject* values
   indicating the arguments and the third parameter is the number of
   arguments (the length of the array).

   Adicionado na versão 3.7.

   Alterado na versão 3.10: "METH_FASTCALL" is now part of the stable
   ABI.

METH_FASTCALL | METH_KEYWORDS
   Extension of "METH_FASTCALL" supporting also keyword arguments,
   with methods of type "PyCFunctionFastWithKeywords". Keyword
   arguments are passed the same way as in the vectorcall protocol:
   there is an additional fourth PyObject* parameter which is a tuple
   representing the names of the keyword arguments (which are
   guaranteed to be strings) or possibly "NULL" if there are no
   keywords.  The values of the keyword arguments are stored in the
   *args* array, after the positional arguments.

   Adicionado na versão 3.7.

METH_METHOD
    * Parte da ABI Estável desde a versão 3.7.*

   Can only be used in the combination with other flags: METH_METHOD |
   METH_FASTCALL | METH_KEYWORDS.

METH_METHOD | METH_FASTCALL | METH_KEYWORDS
   Extension of METH_FASTCALL | METH_KEYWORDS supporting the *defining
   class*, that is, the class that contains the method in question.
   The defining class might be a superclass of "Py_TYPE(self)".

   The method needs to be of type "PyCMethod", the same as for
   "METH_FASTCALL | METH_KEYWORDS" with "defining_class" argument
   added after "self".

   Adicionado na versão 3.9.

METH_NOARGS
    * Parte da ABI Estável.*

   Methods without parameters don't need to check whether arguments
   are given if they are listed with the "METH_NOARGS" flag.  They
   need to be of type "PyCFunction".  The first parameter is typically
   named *self* and will hold a reference to the module or object
   instance.  In all cases the second parameter will be "NULL".

   The function must have 2 parameters. Since the second parameter is
   unused, "Py_UNUSED" can be used to prevent a compiler warning.

METH_O
    * Parte da ABI Estável.*

   Methods with a single object argument can be listed with the
   "METH_O" flag, instead of invoking "PyArg_ParseTuple()" with a
   ""O"" argument. They have the type "PyCFunction", with the *self*
   parameter, and a PyObject* parameter representing the single
   argument.

These two constants are not used to indicate the calling convention
but the binding when used with methods of classes.  These may not be
used for functions defined for modules.  At most one of these flags
may be set for any given method.

METH_CLASS
    * Parte da ABI Estável.*

   The method will be passed the type object as the first parameter
   rather than an instance of the type.  This is used to create *class
   methods*, similar to what is created when using the "@classmethod"
   built-in decorator.

METH_STATIC
    * Parte da ABI Estável.*

   The method will be passed "NULL" as the first parameter rather than
   an instance of the type.  This is used to create *static methods*,
   similar to what is created when using the "@staticmethod" built-in
   decorator.

One other constant controls whether a method is loaded in place of
another definition with the same method name.

METH_COEXIST
    * Parte da ABI Estável.*

   The method will be loaded in place of existing definitions.
   Without *METH_COEXIST*, the default is to skip repeated
   definitions.  Since slot wrappers are loaded before the method
   table, the existence of a *sq_contains* slot, for example, would
   generate a wrapped method named "__contains__()" and preclude the
   loading of a corresponding PyCFunction with the same name.  With
   the flag defined, the PyCFunction will be loaded in place of the
   wrapper object and will co-exist with the slot.  This is helpful
   because calls to PyCFunctions are optimized more than wrapper
   object calls.

PyTypeObject PyCMethod_Type

   The type object corresponding to Python C method objects. This is
   available as "types.BuiltinMethodType" in the Python layer.

int PyCMethod_Check(PyObject *op)

   Return true if *op* is an instance of the "PyCMethod_Type" type or
   a subtype of it. This function always succeeds.

int PyCMethod_CheckExact(PyObject *op)

   This is the same as "PyCMethod_Check()", but does not account for
   subtypes.

PyObject *PyCMethod_New(PyMethodDef *ml, PyObject *self, PyObject *module, PyTypeObject *cls)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.9.*

   Turn *ml* into a Python *callable* object. The caller must ensure
   that *ml* outlives the *callable*. Typically, *ml* is defined as a
   static variable.

   The *self* parameter will be passed as the *self* argument to the C
   function in "ml->ml_meth" when invoked. *self* can be "NULL".

   The *callable* object's "__module__" attribute can be set from the
   given *module* argument. *module* should be a Python string, which
   will be used as name of the module the function is defined in. If
   unavailable, it can be set to "None" or "NULL".

   Ver também: "function.__module__"

   The *cls* parameter will be passed as the *defining_class* argument
   to the C function. Must be set if "METH_METHOD" is set on
   "ml->ml_flags".

   Adicionado na versão 3.9.

PyTypeObject PyCFunction_Type
    * Parte da ABI Estável.*

   The type object corresponding to Python C function objects. This is
   available as "types.BuiltinFunctionType" in the Python layer.

int PyCFunction_Check(PyObject *op)

   Return true if *op* is an instance of the "PyCFunction_Type" type
   or a subtype of it. This function always succeeds.

int PyCFunction_CheckExact(PyObject *op)

   This is the same as "PyCFunction_Check()", but does not account for
   subtypes.

PyObject *PyCFunction_NewEx(PyMethodDef *ml, PyObject *self, PyObject *module)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Equivalente a "PyCMethod_New(ml, self, module, NULL)".

PyObject *PyCFunction_New(PyMethodDef *ml, PyObject *self)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.4.*

   Equivalente a "PyCMethod_New(ml, self, NULL, NULL)".

int PyCFunction_GetFlags(PyObject *func)
    * Parte da ABI Estável.*

   Get the function's flags on *func* as they were passed to
   "ml_flags".

   If *func* is not a C function object, this fails with an exception.
   *func* must not be "NULL".

   This function returns the function's flags on success, and "-1"
   with an exception set on failure.

int PyCFunction_GET_FLAGS(PyObject *func)

   This is the same as "PyCFunction_GetFlags()", but without error or
   type checking.

PyCFunction PyCFunction_GetFunction(PyObject *func)
    * Parte da ABI Estável.*

   Get the function pointer on *func* as it was passed to "ml_meth".

   If *func* is not a C function object, this fails with an exception.
   *func* must not be "NULL".

   This function returns the function pointer on success, and "NULL"
   with an exception set on failure.

int PyCFunction_GET_FUNCTION(PyObject *func)

   This is the same as "PyCFunction_GetFunction()", but without error
   or type checking.

PyObject *PyCFunction_GetSelf(PyObject *func)
    * Parte da ABI Estável.*

   Get the "self" object on *func*. This is the object that would be
   passed to the first argument of a "PyCFunction". For C function
   objects created through a "PyMethodDef" on a "PyModuleDef", this is
   the resulting module object.

   If *func* is not a C function object, this fails with an exception.
   *func* must not be "NULL".

   This function returns a *borrowed reference* to the "self" object
   on success, and "NULL" with an exception set on failure.

PyObject *PyCFunction_GET_SELF(PyObject *func)

   This is the same as "PyCFunction_GetSelf()", but without error or
   type checking.

PyTypeObject *PyCFunction_GET_CLASS(PyObject *func)

   Return a *borrowed reference* to the defining class of *func* if
   its "ml_flags" includes "METH_METHOD". Otherwise, return "NULL"
   without setting an exception.

   *func* must be a C function object and must not be "NULL". This
   function does not perform error or type checking.

   Adicionado na versão 3.9.


Accessing attributes of extension types
=======================================

type PyMemberDef
    * Parte da ABI Estável (incluindo todos os membros).*

   Structure which describes an attribute of a type which corresponds
   to a C struct member. When defining a class, put a NULL-terminated
   array of these structures in the "tp_members" slot.

   Its fields are, in order:

   const char *name

      Name of the member. A NULL value marks the end of a
      "PyMemberDef[]" array.

      The string should be static, no copy is made of it.

   int type

      The type of the member in the C struct. See Member types for the
      possible values.

   Py_ssize_t offset

      The offset in bytes that the member is located on the type’s
      object struct.

   int flags

      Zero or more of the Member flags, combined using bitwise OR.

   const char *doc

      The docstring, or NULL. The string should be static, no copy is
      made of it. Typically, it is defined using "PyDoc_STR".

   By default (when "flags" is "0"), members allow both read and write
   access. Use the "Py_READONLY" flag for read-only access. Certain
   types, like "Py_T_STRING", imply "Py_READONLY". Only
   "Py_T_OBJECT_EX" (and legacy "T_OBJECT") members can be deleted.

   For heap-allocated types (created using "PyType_FromSpec()" or
   similar), "PyMemberDef" may contain a definition for the special
   member ""__vectorcalloffset__"", corresponding to
   "tp_vectorcall_offset" in type objects. This member must be defined
   with "Py_T_PYSSIZET", and either "Py_READONLY" or "Py_READONLY |
   Py_RELATIVE_OFFSET". For example:

      static PyMemberDef spam_type_members[] = {
          {"__vectorcalloffset__", Py_T_PYSSIZET,
           offsetof(Spam_object, vectorcall), Py_READONLY},
          {NULL}  /* Sentinel */
      };

   (You may need to "#include <stddef.h>" for "offsetof()".)

   The legacy offsets "tp_dictoffset" and "tp_weaklistoffset" can be
   defined similarly using ""__dictoffset__"" and
   ""__weaklistoffset__"" members, but extensions are strongly
   encouraged to use "Py_TPFLAGS_MANAGED_DICT" and
   "Py_TPFLAGS_MANAGED_WEAKREF" instead.

   Alterado na versão 3.12: "PyMemberDef" is always available.
   Previously, it required including ""structmember.h"".

   Alterado na versão 3.14: "Py_RELATIVE_OFFSET" is now allowed for
   ""__vectorcalloffset__"", ""__dictoffset__"" and
   ""__weaklistoffset__"".

PyObject *PyMember_GetOne(const char *obj_addr, struct PyMemberDef *m)
    * Parte da ABI Estável.*

   Get an attribute belonging to the object at address *obj_addr*.
   The attribute is described by "PyMemberDef" *m*.  Returns "NULL" on
   error.

   Alterado na versão 3.12: "PyMember_GetOne" is always available.
   Previously, it required including ""structmember.h"".

int PyMember_SetOne(char *obj_addr, struct PyMemberDef *m, PyObject *o)
    * Parte da ABI Estável.*

   Set an attribute belonging to the object at address *obj_addr* to
   object *o*. The attribute to set is described by "PyMemberDef" *m*.
   Returns "0" if successful and a negative value on failure.

   Alterado na versão 3.12: "PyMember_SetOne" is always available.
   Previously, it required including ""structmember.h"".


Member flags
------------

The following flags can be used with "PyMemberDef.flags":

Py_READONLY
    * Parte da ABI Estável desde a versão 3.12.*

   Not writable.

Py_AUDIT_READ
    * Parte da ABI Estável desde a versão 3.12.*

   Emit an "object.__getattr__" audit event before reading.

Py_RELATIVE_OFFSET
    * Parte da ABI Estável desde a versão 3.12.*

   Indicates that the "offset" of this "PyMemberDef" entry indicates
   an offset from the subclass-specific data, rather than from
   "PyObject".

   Can only be used as part of the "Py_tp_members" "slot" when
   creating a class using negative "basicsize". It is mandatory in
   that case. When setting "tp_members" from the slot during class
   creation, Python clears the flag and sets "PyMemberDef.offset" to
   the offset from the "PyObject" struct.

Alterado na versão 3.10: The "RESTRICTED", "READ_RESTRICTED" and
"WRITE_RESTRICTED" macros available with "#include "structmember.h""
are deprecated. "READ_RESTRICTED" and "RESTRICTED" are equivalent to
"Py_AUDIT_READ"; "WRITE_RESTRICTED" does nothing.

Alterado na versão 3.12: The "READONLY" macro was renamed to
"Py_READONLY". The "PY_AUDIT_READ" macro was renamed with the "Py_"
prefix. The new names are now always available. Previously, these
required "#include "structmember.h"". The header is still available
and it provides the old names.

PY_AUDIT_READ

   Soft-deprecated alias of "Py_AUDIT_READ" (note capitalization of
   the "y"). Only available with  "#include "structmember.h"".

   Suavemente descontinuado desde a versão 3.12: Use "Py_AUDIT_READ"
   instead.

PY_WRITE_RESTRICTED

   A member flag that has no effect, retained solely for backwards
   compatibility. This is only available with "#include
   "structmember.h"".

   Suavemente descontinuado desde a versão 3.15.2: Omit this flag
   instead.


Member types
------------

"PyMemberDef.type" can be one of the following macros corresponding to
various C types. When the member is accessed in Python, it will be
converted to the equivalent Python type. When it is set from Python,
it will be converted back to the C type. If that is not possible, an
exception such as "TypeError" or "ValueError" is raised.

Unless marked (D), attributes defined this way cannot be deleted using
e.g. "del" or "delattr()".

These values are available when compiling for the Stable ABI since
version 3.12.

+-----------------------------------+-----------------------------------+-----------------------------------+
| Macro name                        | Tipo em C                         | Tipo em Python                    |
|===================================|===================================|===================================|
| Py_T_BYTE                         | char                              | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_SHORT                        | short                             | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_INT                          | int                               | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_LONG                         | long                              | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_LONGLONG                     | long long                         | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_UBYTE                        | unsigned char                     | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_UINT                         | unsigned int                      | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_USHORT                       | unsigned short                    | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_ULONG                        | unsigned long                     | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_ULONGLONG                    | unsigned long long                | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_PYSSIZET                     | Py_ssize_t                        | "int"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_FLOAT                        | float                             | "float"                           |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_DOUBLE                       | double                            | "float"                           |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_BOOL                         | char (escrito como 0 ou 1)        | "bool"                            |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_STRING                       | const char* (*)                   | "str" (RO)                        |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_STRING_INPLACE               | const char[] (*)                  | "str" (RO)                        |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_CHAR                         | char (0-127)                      | "str" (**)                        |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Py_T_OBJECT_EX                    | PyObject*                         | "object" (D)                      |
+-----------------------------------+-----------------------------------+-----------------------------------+

   (*): Zero-terminated, UTF8-encoded C string. With "Py_T_STRING" the
   C representation is a pointer; with "Py_T_STRING_INPLACE" the
   string is stored directly in the structure.

   (**): String of length 1. Only ASCII is accepted.

   (RO): implica "Py_READONLY".

   (D): pode ser deletado, neste caso o ponteiro é definido para
   "NULL". Ler um ponteiro "NULL" levanta uma exceção
   "AttributeError".

Adicionado na versão 3.12: In previous versions, the macros were only
available with "#include "structmember.h"" and were named without the
"Py_" prefix (e.g. as "T_INT"). The header is still available and
contains the old names, along with the following deprecated types:

T_OBJECT

   Like "Py_T_OBJECT_EX", but "NULL" is converted to "None". This
   results in surprising behavior in Python: deleting the attribute
   effectively sets it to "None".

T_NONE

   Sempre "None". Deve ser usado com  "Py_READONLY".


Defining Getters and Setters
----------------------------

type PyGetSetDef
    * Parte da ABI Estável (incluindo todos os membros).*

   Structure to define property-like access for a type. See also
   description of the "PyTypeObject.tp_getset" slot.

   const char *name

      attribute name

   getter get

      C function to get the attribute.

   setter set

      Optional C function to set or delete the attribute. If "NULL",
      the attribute is read-only.

   const char *doc

      optional docstring

   void *closure

      Optional user data pointer, providing additional data for getter
      and setter.

typedef PyObject *(*getter)(PyObject*, void*)
    * Parte da ABI Estável.*

   The "get" function takes one PyObject* parameter (the instance) and
   a user data pointer (the associated "closure"):

   It should return a new reference on success or "NULL" with a set
   exception on failure.

typedef int (*setter)(PyObject*, PyObject*, void*)
    * Parte da ABI Estável.*

   "set" functions take two PyObject* parameters (the instance and the
   value to be set) and a user data pointer (the associated
   "closure"):

   In case the attribute should be deleted the second parameter is
   "NULL". Should return "0" on success or "-1" with a set exception
   on failure.
