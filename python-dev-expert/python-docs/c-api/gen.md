Objetos Geradores
*****************

Objetos geradores são o que o Python usa para implementar iteradores
geradores. Eles são normalmente criados por iteração sobre uma função
que produz valores, em vez de invocar explicitamente "PyGen_New()" ou
"PyGen_NewWithQualName()".

type PyGenObject

   A estrutura C usada para objetos geradores.

PyTypeObject PyGen_Type

   O objeto de tipo correspondendo a objetos geradores.

int PyGen_Check(PyObject *ob)

   Retorna verdadeiro se *ob* for um objeto gerador; *ob* não deve ser
   "NULL". Esta função sempre tem sucesso.

int PyGen_CheckExact(PyObject *ob)

   Retorna verdadeiro se o tipo do *ob* é "PyGen_Type"; *ob* não deve
   ser "NULL". Esta função sempre tem sucesso.

PyObject *PyGen_New(PyFrameObject *frame)
    *Retorna valor: Nova referência.*

   Create and return a new generator object based on the *frame*
   object. A reference to *frame* is "*stolen*" by this function (even
   on error). The argument must not be "NULL".

PyObject *PyGen_NewWithQualName(PyFrameObject *frame, PyObject *name, PyObject *qualname)
    *Retorna valor: Nova referência.*

   Create and return a new generator object based on the *frame*
   object, with "__name__" and "__qualname__" set to *name* and
   *qualname*. A reference to *frame* is "*stolen*" by this function
   (even on error).  The *frame* argument must not be "NULL".

PyCodeObject *PyGen_GetCode(PyGenObject *gen)

   Retorna uma nova *referência forte* ao objeto de código encapsulado
   por *gen*. Esta função sempre tem sucesso.


Objetos geradores assíncronos
=============================

Ver também: **PEP 525**

PyTypeObject PyAsyncGen_Type

   O objeto de tipo correspondente aos objetos geradores assíncronos.
   Está disponível como "types.AsyncGeneratorType" na camada Python.

   Adicionado na versão 3.6.

PyObject *PyAsyncGen_New(PyFrameObject *frame, PyObject *name, PyObject *qualname)

   Create a new asynchronous generator wrapping *frame*, with
   "__name__" and "__qualname__" set to *name* and *qualname*. *frame*
   is "*stolen*" by this function (even on error) and must not be
   "NULL".

   Em caso de sucesso, esta função retorna uma *referência forte* ao
   novo gerador assíncrono. Em caso de falha, esta função retorna
   "NULL" com uma exceção definida.

   Adicionado na versão 3.6.

int PyAsyncGen_CheckExact(PyObject *op)

   Retorna verdadeiro se *op* for um objeto gerador assíncrono, falso
   caso contrário. Esta função sempre tem sucesso.

   Adicionado na versão 3.6.


Deprecated API
==============

PyAsyncGenASend_CheckExact(op)

   This is an API that was included in Python's C API by mistake.

   It is solely here for completeness; do not use this API.

   Suavemente descontinuado desde a versão 3.14.
