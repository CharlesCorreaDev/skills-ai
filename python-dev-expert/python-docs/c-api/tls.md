Thread-local storage support
****************************

The Python interpreter provides low-level support for thread-local
storage (TLS) which wraps the underlying native TLS implementation to
support the Python-level thread-local storage API ("threading.local").
The CPython C level APIs are similar to those offered by pthreads and
Windows: use a thread key and functions to associate a void* value per
thread.

A *thread state* does *not* need to be *attached* when calling these
functions; they supply their own locking.

Note that "Python.h" does not include the declaration of the TLS APIs,
you need to include "pythread.h" to use thread-local storage.

Nota:

  None of these API functions handle memory management on behalf of
  the void* values.  You need to allocate and deallocate them
  yourself. If the void* values happen to be PyObject*, these
  functions don't do refcount operations on them either.


Thread-specific storage API
===========================

The thread-specific storage (TSS) API was introduced to supersede the
use of the existing TLS API within the CPython interpreter.  This API
uses a new type "Py_tss_t" instead of int to represent thread keys.

Adicionado na versão 3.7.

Ver também:

  "A New C-API for Thread-Local Storage in CPython" (**PEP 539**)

type Py_tss_t

   This data structure represents the state of a thread key, the
   definition of which may depend on the underlying TLS
   implementation, and it has an internal field representing the key's
   initialization state.  There are no public members in this
   structure.

   Quando Py_LIMITED_API não é definido, a alocação estática deste
   tipo por "Py_tss_NEEDS_INIT" é permitida.

Py_tss_NEEDS_INIT

   This macro expands to the initializer for "Py_tss_t" variables.
   Note that this macro won't be defined with Py_LIMITED_API.


Dynamic allocation
==================

Dynamic allocation of the "Py_tss_t", required in extension modules
built with Py_LIMITED_API, where static allocation of this type is not
possible due to its implementation being opaque at build time.

Py_tss_t *PyThread_tss_alloc()
    * Parte da ABI Estável desde a versão 3.7.*

   Retorna um valor que é o mesmo estado de um valor inicializado com
   "Py_tss_NEEDS_INIT", ou "NULL" no caso de falha de alocação
   dinâmica.

void PyThread_tss_free(Py_tss_t *key)
    * Parte da ABI Estável desde a versão 3.7.*

   Free the given *key* allocated by "PyThread_tss_alloc()", after
   first calling "PyThread_tss_delete()" to ensure any associated
   thread locals have been unassigned. This is a no-op if the *key*
   argument is "NULL".

   Nota:

     A freed key becomes a dangling pointer. You should reset the key
     to "NULL".


Métodos
=======

The parameter *key* of these functions must not be "NULL".  Moreover,
the behaviors of "PyThread_tss_set()" and "PyThread_tss_get()" are
undefined if the given "Py_tss_t" has not been initialized by
"PyThread_tss_create()".

int PyThread_tss_is_created(Py_tss_t *key)
    * Parte da ABI Estável desde a versão 3.7.*

   Return a non-zero value if the given "Py_tss_t" has been
   initialized by "PyThread_tss_create()".

int PyThread_tss_create(Py_tss_t *key)
    * Parte da ABI Estável desde a versão 3.7.*

   Retorna um valor zero na inicialização bem-sucedida de uma chave
   TSS. O comportamento é indefinido se o valor apontado pelo
   argumento *key* não for inicializado por "Py_tss_NEEDS_INIT". Essa
   função pode ser chamada repetidamente na mesma tecla -- chamá-la em
   uma tecla já inicializada não funciona e retorna imediatamente com
   sucesso.

void PyThread_tss_delete(Py_tss_t *key)
    * Parte da ABI Estável desde a versão 3.7.*

   Destroy a TSS key to forget the values associated with the key
   across all threads, and change the key's initialization state to
   uninitialized.  A destroyed key is able to be initialized again by
   "PyThread_tss_create()". This function can be called repeatedly on
   the same key -- calling it on an already destroyed key is a no-op.

int PyThread_tss_set(Py_tss_t *key, void *value)
    * Parte da ABI Estável desde a versão 3.7.*

   Return a zero value to indicate successfully associating a void*
   value with a TSS key in the current thread.  Each thread has a
   distinct mapping of the key to a void* value.

void *PyThread_tss_get(Py_tss_t *key)
    * Parte da ABI Estável desde a versão 3.7.*

   Return the void* value associated with a TSS key in the current
   thread.  This returns "NULL" if no value is associated with the key
   in the current thread.


Legacy APIs
===========

Descontinuado desde a versão 3.7: This API is superseded by the
thread-specific storage (TSS) API.

Nota:

  This version of the API does not support platforms where the native
  TLS key is defined in a way that cannot be safely cast to "int".  On
  such platforms, "PyThread_create_key()" will return immediately with
  a failure status, and the other TLS functions will all be no-ops on
  such platforms.

Due to the compatibility problem noted above, this version of the API
should not be used in new code.

int PyThread_create_key()
    * Parte da ABI Estável.*

void PyThread_delete_key(int key)
    * Parte da ABI Estável.*

int PyThread_set_key_value(int key, void *value)
    * Parte da ABI Estável.*

void *PyThread_get_key_value(int key)
    * Parte da ABI Estável.*

void PyThread_delete_key_value(int key)
    * Parte da ABI Estável.*

void PyThread_ReInitTLS()
    * Parte da ABI Estável.*
