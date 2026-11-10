Contagem de referências
***********************

As funções e macros nesta sessão são usadas para o gerenciamento de
contagem de referências de objetos Python.

Py_ssize_t Py_REFCNT(PyObject *o)
    * Parte da ABI Estável desde a versão 3.14.*

   Obtêm a contagem de referências do objeto Python *o*.

   Observe que o valor retornado pode não refletir realmente quantas
   referências ao objeto são realmente mantidas. Por exemplo, alguns
   objetos são *imortais* e têm uma refcount muito alta que não
   reflete o número real de referências. Consequentemente, não confie
   no valor retornado para ser preciso, exceto um valor de 0 ou 1.

   Use a função "Py_SET_REFCNT()" para definir uma contagem de
   referências de um objeto.

   Nota:

     On *free-threaded builds* of Python, returning 1 isn't sufficient
     to determine if it's safe to treat *o* as having no access by
     other threads. Use "PyUnstable_Object_IsUniquelyReferenced()" for
     that instead.Veja também a função
     "PyUnstable_Object_IsUniqueReferencedTemporary()".

   Alterado na versão 3.10: "Py_REFCNT()" is changed to the inline
   static function.

   Alterado na versão 3.11: The parameter type is no longer const
   PyObject*.

void Py_SET_REFCNT(PyObject *o, Py_ssize_t refcnt)
    * This macro is available when compiling for the ABI Estável desde
   a versão 3.9.*

   Set the object *o* reference counter to *refcnt*.

   Em uma construção do Python com threads threads livres, se *refcnt*
   for maior que "UINT32_MAX", o objeto será transformado em
   *imortal*.

   Esta função não tem efeito sobre objetos *imortais*.

   Adicionado na versão 3.9.

   Alterado na versão 3.12: Os objetos imortais não são modificados.

void Py_INCREF(PyObject *o)
    * This macro is available when compiling for the ABI Estável.*

   Indicate taking a new *strong reference* to object *o*, indicating
   it is in use and should not be destroyed.

   Esta função não tem efeito sobre objetos *imortais*.

   Esta função é geralmente usada para transformar uma *referência
   emprestada* em uma *referência forte* local. A função "Py_NewRef()"
   pode ser usada para criar uma nova *referência forte*.

   When done using the object, release is by calling "Py_DECREF()".

   The object must not be "NULL"; if you aren't sure that it isn't
   "NULL", use "Py_XINCREF()".

   Do not expect this function to actually modify *o* in any way. For
   at least **some objects**, this function has no effect.

   Alterado na versão 3.12: Os objetos imortais não são modificados.

void Py_XINCREF(PyObject *o)
    * This macro is available when compiling for the ABI Estável.*

   Semelhante a "Py_INCREF()", mas o objeto *o* pode ser "NULL", caso
   em que isso não tem efeito.

   Veja também "Py_XNewRef()".

PyObject *Py_NewRef(PyObject *o)
    * Parte da ABI Estável desde a versão 3.10.*

   Create a new *strong reference* to an object: call "Py_INCREF()" on
   *o* and return the object *o*.

   When the *strong reference* is no longer needed, "Py_DECREF()"
   should be called on it to release the reference.

   The object *o* must not be "NULL"; use "Py_XNewRef()" if *o* can be
   "NULL".

   Por exemplo:

      Py_INCREF(obj);
      self->attr = obj;

   can be written as:

      self->attr = Py_NewRef(obj);

   See also "Py_INCREF()".

   Adicionado na versão 3.10.

PyObject *Py_XNewRef(PyObject *o)
    * Parte da ABI Estável desde a versão 3.10.*

   Semelhante a "Py_NewRef()", mas o objeto *o* pode ser NULL.

   Se o objeto *o* é "NULL", a função apenas retorna "NULL".

   Adicionado na versão 3.10.

void Py_DECREF(PyObject *o)
    * This macro is available when compiling for the ABI Estável.*

   Release a *strong reference* to object *o*, indicating the
   reference is no longer used.

   Esta função não tem efeito sobre objetos *imortais*.

   Once the last *strong reference* is released (i.e. the object's
   reference count reaches 0), the object's type's deallocation
   function (which must not be "NULL") is invoked.

   This function is usually used to delete a *strong reference* before
   exiting its scope.

   The object must not be "NULL"; if you aren't sure that it isn't
   "NULL", use "Py_XDECREF()".

   Do not expect this function to actually modify *o* in any way. For
   at least **some objects**, this function has no effect.

   Aviso:

     The deallocation function can cause arbitrary Python code to be
     invoked (e.g. when a class instance with a "__del__()" method is
     deallocated).  While exceptions in such code are not propagated,
     the executed code has free access to all Python global variables.
     This means that any object that is reachable from a global
     variable should be in a consistent state before "Py_DECREF()" is
     invoked.  For example, code to delete an object from a list
     should copy a reference to the deleted object in a temporary
     variable, update the list data structure, and then call
     "Py_DECREF()" for the temporary variable.

   Alterado na versão 3.12: Os objetos imortais não são modificados.

void Py_XDECREF(PyObject *o)
    * This macro is available when compiling for the ABI Estável.*

   Similar to "Py_DECREF()", but the object *o* can be "NULL", in
   which case this has no effect. The same warning from "Py_DECREF()"
   applies here as well.

void Py_CLEAR(PyObject *o)
    * This macro is available when compiling for the ABI Estável.*

   Release a *strong reference* for object *o*. The object may be
   "NULL", in which case the macro has no effect; otherwise the effect
   is the same as for "Py_DECREF()", except that the argument is also
   set to "NULL".  The warning for "Py_DECREF()" does not apply with
   respect to the object passed because the macro carefully uses a
   temporary variable and sets the argument to "NULL" before releasing
   the reference.

   It is a good idea to use this macro whenever releasing a reference
   to an object that might be traversed during garbage collection.

   Alterado na versão 3.12: The macro argument is now only evaluated
   once. If the argument has side effects, these are no longer
   duplicated.

void Py_IncRef(PyObject *o)
    * Parte da ABI Estável.*

   Indicate taking a new *strong reference* to object *o*. A function
   version of "Py_XINCREF()". It can be used for runtime dynamic
   embedding of Python.

void Py_DecRef(PyObject *o)
    * Parte da ABI Estável.*

   Release a *strong reference* to object *o*. A function version of
   "Py_XDECREF()". It can be used for runtime dynamic embedding of
   Python.

Py_SETREF(dst, src)

   Macro safely releasing a *strong reference* to object *dst* and
   setting *dst* to *src*.

   As in case of "Py_CLEAR()", "the obvious" code can be deadly:

      Py_DECREF(dst);
      dst = src;

   The safe way is:

      Py_SETREF(dst, src);

   That arranges to set *dst* to *src* *before* releasing the
   reference to the old value of *dst*, so that any code triggered as
   a side-effect of *dst* getting torn down no longer believes *dst*
   points to a valid object.

   Adicionado na versão 3.6.

   Alterado na versão 3.12: The macro arguments are now only evaluated
   once. If an argument has side effects, these are no longer
   duplicated.

Py_XSETREF(dst, src)

   Variant of "Py_SETREF" macro that uses "Py_XDECREF()" instead of
   "Py_DECREF()".

   Adicionado na versão 3.6.

   Alterado na versão 3.12: The macro arguments are now only evaluated
   once. If an argument has side effects, these are no longer
   duplicated.
