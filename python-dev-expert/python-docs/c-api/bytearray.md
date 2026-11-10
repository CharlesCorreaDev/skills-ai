Objetos byte array
******************

type PyByteArrayObject

   Esse subtipo de "PyObject" representa um objeto Python bytearray.

   O buffer interno de "PyByteArrayObject" sempre inclui um byte nulo
   adicional ao final para compatibilidade com strings C terminadas em
   nulo. Esse byte extra não é contabilizado em "PyByteArray_Size()"
   nem nos argumentos *len* das funções abaixo.

PyTypeObject PyByteArray_Type
    * Parte da ABI Estável.*

   Essa instância de "PyTypeObject" representa um tipo Python
   bytearray; é o mesmo objeto que o "bytearray" na camada Python.


Macros para verificação de tipo
===============================

int PyByteArray_Check(PyObject *o)

   Retorna verdadeiro se o objeto *o* for um objeto bytearray ou se
   for uma instância de um subtipo do tipo bytearray. Esta função
   sempre tem sucesso.

int PyByteArray_CheckExact(PyObject *o)

   Retorna verdadeiro se o objeto *o* for um objeto bytearray, mas não
   uma instância de um subtipo do tipo bytearray. Esta função sempre
   tem sucesso.


Funções diretas da API
======================

PyObject *PyByteArray_FromObject(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Safe for concurrent use on the same object.*

   Retorna um novo objeto bytearray, *o*, que implementa o protocolo
   de buffer.

   Em caso de falha, retorna "NULL" com uma exceção definida.

   Nota:

     Se o objeto implementar o protocolo de buffer, o buffer não deve
     ser modificado enquanto o objeto bytearray estiver a ser criado.

PyObject *PyByteArray_FromStringAndSize(const char *string, Py_ssize_t len)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Cria um novo objeto bytearray a partir de *string* e seu
   comprimento, *len*.

   Em caso de falha, retorna "NULL" com uma exceção definida.

PyObject *PyByteArray_Concat(PyObject *a, PyObject *b)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Safe for concurrent use on the same object.*

   Concatena os bytearrays *a* e *b* e retorna um novo bytearray com o
   resultado.

   Em caso de falha, retorna "NULL" com uma exceção definida.

   Nota:

     Se o objeto implementar o protocolo de buffer, o buffer não deve
     ser modificado enquanto o objeto bytearray estiver a ser criado.

Py_ssize_t PyByteArray_Size(PyObject *bytearray)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Retorna o tamanho de *bytearray* após verificar se há um ponteiro
   "NULL".

char *PyByteArray_AsString(PyObject *bytearray)
    * Parte da ABI Estável.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Retorna o conteúdo de *bytearray* como uma matriz de caracteres
   após verificar um ponteiro "NULL". O array retornado sempre tem um
   byte nulo extra acrescentado.

   Nota:

     Não é seguro para thread modificar o objeto bytearray enquanto se
     utiliza o vetor de caracteres retornado.

int PyByteArray_Resize(PyObject *bytearray, Py_ssize_t len)
    * Parte da ABI Estável.*

   Redimensiona o buffer interno de *bytearray* para o tamanho *len*.
   Falha é um retorno "-1" com um conjunto de exceções.

   Alterado na versão 3.14: Um *len* negativo agora resultará na
   definição de uma exceção e no retorno de -1.


Macros
======

Estas macros trocam segurança por velocidade e não verificam os
ponteiros.

char *PyByteArray_AS_STRING(PyObject *bytearray)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Similar a "PyByteArray_AsString()", mas sem verificação de erro.

   Nota:

     Não é seguro para thread modificar o objeto bytearray enquanto se
     utiliza o vetor de caracteres retornado.

Py_ssize_t PyByteArray_GET_SIZE(PyObject *bytearray)
    * Thread safety: Atomic.*

   Similar a "PyByteArray_Size()", mas sem verificação de erro.
