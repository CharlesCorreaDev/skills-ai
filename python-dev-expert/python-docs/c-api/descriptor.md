Objetos descritores
*******************

"Descritores" são objetos que descrevem algum atributo de um objeto.
Eles são encontrados no dicionário de objetos de tipo.

PyObject *PyDescr_NewGetSet(PyTypeObject *type, struct PyGetSetDef *getset)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a new get-set descriptor for extension type *type* from the
   "PyGetSetDef" structure *getset*.

   Get-set descriptors expose attributes implemented by C getter and
   setter functions rather than stored directly in the instance. This
   is the same kind of descriptor created for entries in "tp_getset",
   and it appears in Python as a "types.GetSetDescriptorType" object.

   On success, return a *strong reference* to the descriptor. Return
   "NULL" with an exception set on failure.

PyObject *PyDescr_NewMember(PyTypeObject *type, struct PyMemberDef *member)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a new member descriptor for extension type *type* from the
   "PyMemberDef" structure *member*.

   Member descriptors expose fields in the type's C struct as Python
   attributes. This is the same kind of descriptor created for entries
   in "tp_members", and it appears in Python as a
   "types.MemberDescriptorType" object.

   On success, return a *strong reference* to the descriptor. Return
   "NULL" with an exception set on failure.

PyTypeObject PyMemberDescr_Type
    * Parte da ABI Estável.*

   O objeto de tipo para descritores de membros criados a partir de
   estruturas "PyMemberDef". Esses descritores expõem campos de uma
   estrutura C como atributos de um tipo e correspondem a objetos
   "types.MemberDescriptorType" em Python.

PyTypeObject PyGetSetDescr_Type
    * Parte da ABI Estável.*

   The type object for get/set descriptor objects created from
   "PyGetSetDef" structures. These descriptors implement attributes
   whose value is computed by C getter and setter functions, and are
   used for many built-in type attributes. They correspond to
   "types.GetSetDescriptorType" objects in Python.

PyObject *PyDescr_NewMethod(PyTypeObject *type, struct PyMethodDef *meth)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a new method descriptor for extension type *type* from the
   "PyMethodDef" structure *meth*.

   Method descriptors expose C functions as methods on a type. This is
   the same kind of descriptor created for entries in "tp_methods",
   and it appears in Python as a "types.MethodDescriptorType" object.

   On success, return a *strong reference* to the descriptor. Return
   "NULL" with an exception set on failure.

PyTypeObject PyMethodDescr_Type
    * Parte da ABI Estável.*

   The type object for method descriptor objects created from
   "PyMethodDef" structures. These descriptors expose C functions as
   methods on a type, and correspond to "types.MethodDescriptorType"
   objects in Python.

PyTypeObject PyWrapperDescr_Type
    * Parte da ABI Estável.*

   The type object for wrapper descriptor objects created by
   "PyDescr_NewWrapper()" and "PyWrapper_New()".

   Wrapper descriptors are used internally to expose special methods
   such as "__repr__" or "__add__", which are implemented by type
   slots. The type is exposed in Python as
   "types.WrapperDescriptorType".

PyObject *PyDescr_NewWrapper(PyTypeObject *type, struct wrapperbase *base, void *wrapped)
    *Retorna valor: Nova referência.*

   Create a new wrapper descriptor of type "PyWrapperDescr_Type".

   This function is meant for internal use only; it and related API
   ("struct wrapperbase" and the "PyWrapperFlag_KEYWORDS" flag) are
   exposed publicly for backwards compatibility reasons.

   See "PyCMethod_New()" for wrapping a C function.

PyObject *PyDescr_NewClassMethod(PyTypeObject *type, PyMethodDef *method)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a new class method descriptor for extension type *type* from
   the "PyMethodDef" structure *method*.

   Class method descriptors expose C methods that receive the class
   rather than an instance when accessed. This is the same kind of
   descriptor created for "METH_CLASS" entries in "tp_methods", and it
   appears in Python as a "types.ClassMethodDescriptorType" object.

   On success, return a *strong reference* to the descriptor. Return
   "NULL" with an exception set on failure.

int PyDescr_IsData(PyObject *descr)

   Retorna não-zero se o objeto descritor *descr* descrevem um
   atributo de dados, ou "0" se os mesmos descrevem um método. *descr*
   deve ser um objeto descritor; não há verificação de erros.

PyObject *PyWrapper_New(PyObject *d, PyObject *self)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a new bound wrapper object from the wrapper descriptor *d*
   and the instance *self*.

   This is the bound form of a wrapper descriptor created by
   "PyDescr_NewWrapper()". CPython creates these objects when a slot
   wrapper is accessed through an instance, and they appear in Python
   as "types.MethodWrapperType" objects.

   On success, return a *strong reference* to the wrapper object.
   Return "NULL" with an exception set on failure.

PyDescr_TYPE(descr)

   Return a *borrowed reference* to the type that the descriptor
   *descr* belongs to. This is accessible as "__objclass__" in Python.

   *descr* must be a descriptor object created by one of the
   "PyDescr_New*" functions (an instance of "PyMethodDescr_Type",
   "PyClassMethodDescr_Type", "PyMemberDescr_Type",
   "PyGetSetDescr_Type", or "PyWrapperDescr_Type"). If the passed
   descriptor is not an instance of one of these types, the behavior
   is undefined.

PyDescr_NAME(descr)

   Return the name of the descriptor *descr* as a *borrowed reference*
   to a "str" object. This is available as "__name__" in Python.

   *descr* must be a descriptor object created by one of the
   "PyDescr_New*" functions. If not, the behavior is undefined.

PyDescr_COMMON

   This is a macro including the common fields for a descriptor
   object.

   This was included in Python's C API by mistake; do not use it in
   extensions. For creating custom descriptor objects, create a class
   implementing the descriptor protocol ("tp_descr_get" and
   "tp_descr_set").

   Suavemente descontinuado desde a versão 3.15.


Descritores embutidos
=====================

PyTypeObject PyProperty_Type
    * Parte da ABI Estável.*

   The type object for property objects. This is the same object as
   "property" in the Python layer.

PyTypeObject PySuper_Type
    * Parte da ABI Estável.*

   O objeto de tipo para superobjetos. Este é o mesmo objeto que
   "super" na camada Python.

PyTypeObject PyClassMethod_Type

   O tipo de objeto de método de classe. Este é o mesmo objeto que
   "classmethod" na camada Python.

PyTypeObject PyClassMethodDescr_Type
    * Parte da ABI Estável.*

   The type object for C-level class method descriptor objects. This
   is the type of the descriptors created for "classmethod()" defined
   in C extension types, and corresponds to
   "types.ClassMethodDescriptorType" objects in Python.

PyObject *PyClassMethod_New(PyObject *callable)

   Cria um novo objeto "classmethod" que envolve *callable*.
   *callable* deve ser um objeto chamável e não deve ser "NULL".

   Em caso de sucesso, esta função retorna uma *referência forte* a um
   novo descritor de método de classe. Em caso de falha, esta função
   retorna "NULL" com uma exceção definida.

PyTypeObject PyStaticMethod_Type

   O tipo de objeto de método estático. Este é o mesmo objeto que
   "staticmethod" na camada Python.

PyObject *PyStaticMethod_New(PyObject *callable)

   Cria um novo objeto "staticmethod" que envolve *callable*.
   *callable* deve ser um objeto chamável e não deve ser "NULL".

   Em caso de sucesso, esta função retorna uma *referência forte* a um
   novo descritor de método estático. Em caso de falha, esta função
   retorna "NULL" com uma exceção definida.
