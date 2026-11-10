Objetos Bytes
*************

Estas funções levantam "TypeError" quando se espera um parâmetro bytes
e são chamados com um parâmetro que não é bytes.

**Detalhes da implementação do CPython:** The internal buffer of
"PyBytesObject" always includes an extra trailing null byte for
compatibility with null terminated C strings. This extra byte is not
counted in "PyBytes_Size()" nor in the various *length* and *size*
arguments of the functions below.

type PyBytesObject

   Esta é uma instância de "PyObject" representando o objeto bytes do
   Python.

PyTypeObject PyBytes_Type
    * Parte da ABI Estável.*

   Esta instância de "PyTypeObject" representa o tipo de bytes Python;
   é o mesmo objeto que "bytes" na camada de Python.

int PyBytes_Check(PyObject *o)

   Retorna verdadeiro se o objeto *o* for um objeto bytes ou se for
   uma instância de um subtipo do tipo bytes. Esta função sempre tem
   sucesso.

int PyBytes_CheckExact(PyObject *o)

   Retorna verdadeiro se o objeto *o* for um objeto bytes, mas não uma
   instância de um subtipo do tipo bytes. Esta função sempre tem
   sucesso.

PyObject *PyBytes_FromString(const char *v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um novo objeto de bytes com uma cópia da string *v* como
   valor em caso de sucesso e "NULL" em caso de falha. O parâmetro *v*
   não deve ser "NULL" e isso não será verificado.

PyObject *PyBytes_FromStringAndSize(const char *v, Py_ssize_t len)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um novo objeto de bytes com uma cópia da string *v* como
   valor e comprimento *len* em caso de sucesso e "NULL" em caso de
   falha. Se *v* for "NULL", o conteúdo do objeto bytes não será
   inicializado.

   Suavemente descontinuado desde a versão 3.15: Use the
   "PyBytesWriter" API instead of "PyBytes_FromStringAndSize(NULL,
   len)".

PyObject *PyBytes_FromFormat(const char *format, ...)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Leva uma string tipo "printf()" do C *format* e um número variável
   de argumentos, calcula o tamanho do objeto bytes do Python
   resultante e retorna um objeto bytes com os valores formatados
   nela. Os argumentos da variável devem ser tipos C e devem
   corresponder exatamente aos caracteres de formato na string
   *format*. Os seguintes formatos de caracteres são permitidos:

   +---------------------+-----------------+----------------------------------+
   | Caracteres          | Tipo            | Comentário                       |
   | Formatados          |                 |                                  |
   |=====================|=================|==================================|
   | "%%"                | *n/d*           | O caractere literal %.           |
   +---------------------+-----------------+----------------------------------+
   | "%c"                | int             | Um único byte, representado como |
   |                     |                 | um C int.                        |
   +---------------------+-----------------+----------------------------------+
   | "%d"                | int             | Equivalente a "printf("%d")".    |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%u"                | unsigned int    | Equivalente a "printf("%u")".    |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%ld"               | long            | Equivalente a "printf("%ld")".   |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%lu"               | unsigned long   | Equivalente a "printf("%lu")".   |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%zd"               | "Py_ssize_t"    | Equivalente a "printf("%zd")".   |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%zu"               | size_t          | Equivalente a "printf("%zu")".   |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%i"                | int             | Equivalente a "printf("%i")".    |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%x"                | int             | Equivalente a "printf("%x")".    |
   |                     |                 | [1]                              |
   +---------------------+-----------------+----------------------------------+
   | "%s"                | const char*     | Uma matriz de caracteres C com   |
   |                     |                 | terminação nula.                 |
   +---------------------+-----------------+----------------------------------+
   | "%p"                | const void*     | A representação hexadecimal de   |
   |                     |                 | um ponteiro C. Principalmente    |
   |                     |                 | equivalente a "printf("%p")"     |
   |                     |                 | exceto que é garantido que       |
   |                     |                 | comece com o literal "0x"        |
   |                     |                 | independentemente do que o       |
   |                     |                 | "printf" da plataforma ceda.     |
   +---------------------+-----------------+----------------------------------+

   Um caractere de formato não reconhecido faz com que todo o resto da
   string de formato seja copiado como é para o objeto resultante e
   todos os argumentos extras sejam descartados.

   [1] Para especificadores de número inteiro (d, u, ld, lu, zd, zu,
       i, x): o sinalizador de conversão 0 tem efeito mesmo quando uma
       precisão é fornecida.

PyObject *PyBytes_FromFormatV(const char *format, va_list vargs)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Idêntico a "PyBytes_FromFormat()" exceto que é preciso exatamente
   dois argumentos.

PyObject *PyBytes_FromObject(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Safe for concurrent use on the same object.*

   Retorna a representação de bytes do objeto *o* que implementa o
   protocolo de buffer.

   Nota:

     If the object implements the buffer protocol, then the buffer
     must not be mutated while the bytes object is being created.

Py_ssize_t PyBytes_Size(PyObject *o)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Retorna o comprimento dos bytes em objeto bytes *o*.

Py_ssize_t PyBytes_GET_SIZE(PyObject *o)
    * Thread safety: Atomic.*

   Similar a "PyBytes_Size()", mas sem verificação de erro.

char *PyBytes_AsString(PyObject *o)
    * Parte da ABI Estável.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Retorna um ponteiro para o conteúdo de *o*. O ponteiro se refere ao
   buffer interno de *o*, que consiste em "len(o) + 1" bytes. O último
   byte no buffer é sempre nulo, independentemente de haver outros
   bytes nulos. Os dados não devem ser modificados de forma alguma, a
   menos que o objeto tenha sido criado usando
   "PyBytes_FromStringAndSize(NULL, size)". Não deve ser desalocado.
   Se *o* não é um objeto de bytes, "PyBytes_AsString()" retorna
   "NULL" e levanta "TypeError".

char *PyBytes_AS_STRING(PyObject *string)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Similar a "PyBytes_AsString()", mas sem verificação de erro.

int PyBytes_AsStringAndSize(PyObject *obj, char **buffer, Py_ssize_t *length)
    * Parte da ABI Estável.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Retorna os conteúdos terminados nulos do objeto *obj* através das
   variáveis de saída *buffer* e *length*. Retorna "0" em caso de
   sucesso.

   Se *length* for "NULL", o objeto bytes não poderá conter bytes
   nulos incorporados; se isso acontecer, a função retornará "-1" e a
   "ValueError" será levantado.

   O buffer refere-se a um buffer interno de *obj*, que inclui um byte
   nulo adicional no final (não contado em *length*). Os dados não
   devem ser modificados de forma alguma, a menos que o objeto tenha
   sido criado apenas usando "PyBytes_FromStringAndSize(NULL, size)".
   Não deve ser desalinhado. Se *obj* não é um objeto bytes,
   "PyBytes_AsStringAndSize()" retorna "-1" e levanta "TypeError".

   Alterado na versão 3.5: Anteriormente "TypeError" era levantado
   quando os bytes nulos incorporados eram encontrados no objeto
   bytes.

void PyBytes_Concat(PyObject **bytes, PyObject *newpart)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Create a new bytes object in **bytes* containing the contents of
   *newpart* appended to *bytes*; the caller will own the new
   reference. The reference to the old value of *bytes* will be
   "*stolen*". If the new object cannot be created, the old reference
   to *bytes* will still be "stolen", the value of **bytes* will be
   set to "NULL", and the appropriate exception will be set.

   Nota:

     If *newpart* implements the buffer protocol, then the buffer must
     not be mutated while the new bytes object is being created.

void PyBytes_ConcatAndDel(PyObject **bytes, PyObject *newpart)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   "Crie um novo objeto bytes em **bytes* contendo o conteúdo de
   newpart anexado a bytes. Esta versão libera a *strong reference*
   (referência forte) para newpart (ou seja, decrementa a contagem de
   referências a ele)."

   Nota:

     If *newpart* implements the buffer protocol, then the buffer must
     not be mutated while the new bytes object is being created.

PyObject *PyBytes_Join(PyObject *sep, PyObject *iterable)
    * Thread safety: Safe for concurrent use on the same object.*

   Similar a "sep.join(iterable)" no Python.

   *sep* deve ser um objeto Python "bytes". (Observe que
   "PyUnicode_Join()" aceita o separador "NULL" e o trata como um
   espaço, enquanto "PyBytes_Join()" não aceita o separador "NULL".)

   *iterable* deve ser um objeto iterável que produz objetos que
   implementam o protocolo de buffer.

   Em caso de sucesso, retorna um novo objeto "bytes". Em caso de
   erro, define uma exceção e retorna "NULL".

   Adicionado na versão 3.14.

   Nota:

     If *iterable* objects implement the buffer protocol, then the
     buffers must not be mutated while the new bytes object is being
     created.

int _PyBytes_Resize(PyObject **bytes, Py_ssize_t newsize)
    * Thread safety: Safe to call without external synchronization on
   distinct objects.*

   Redimensiona um objeto de bytes. *newsize* será o novo tamanho do
   objeto bytes. Você pode pensar nisso como se estivesse criando um
   novo objeto de bytes e destruindo o antigo, só que de forma mais
   eficiente. Passe o endereço de um objeto de bytes existente como um
   lvalue (pode ser gravado) e o novo tamanho desejado. Em caso de
   sucesso, **bytes* mantém o objeto de bytes redimensionados e "0" é
   retornado; o endereço em **bytes* pode diferir do seu valor de
   entrada. Se a realocação falhar, o objeto de bytes originais em
   **bytes* é desalocado, **bytes* é definido como "NULL",
   "MemoryError" é definido e "-1" é retornado.

   Suavemente descontinuado desde a versão 3.15: Use the
   "PyBytesWriter" API instead.

PyObject *PyBytes_Repr(PyObject *bytes, int smartquotes)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Obtém a representação em string de *bytes*. Esta função é
   atualmente usada para implementar "bytes.__repr__()" em Python.

   Esta função não realiza verificação de tipo; é um comportamento
   indefinido passar *bytes* como um objeto que não seja do tipo bytes
   ou "NULL".

   Se *smartquotes* for verdadeiro, a representação usará uma string
   entre aspas duplas em vez de aspas simples quando aspas simples
   estiverem presentes em *bytes*. Por exemplo, a string de bytes
   "'Python'" seria representada como "b"'Python'"" quando
   *smartquotes* for verdadeiro, ou "b'\'Python\''" quando for falso.

   Em caso de sucesso, esta função retorna uma *referência forte* a um
   objeto "str" contendo a representação. Em caso de falha, ela
   retorna "NULL" com uma exceção definida.

PyObject *PyBytes_DecodeEscape(const char *s, Py_ssize_t len, const char *errors, Py_ssize_t unicode, const char *recode_encoding)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Remove um string *s* que foi escapada com contrabarra. *s* não pode
   ser "NULL". *len* deve ser o tamanho de *s*.

   *errors* deve ser um dos seguintes valores: ""strict"", ""replace""
   ou ""ignore"". Se *errors* for "NULL", o valor padrão será
   ""strict"".

   Em caso de sucesso, esta função retorna uma *referência forte* a um
   objeto Python "bytes" contendo a string sem escape. Em caso de
   falha, esta função retorna "NULL" com uma exceção definida.

   Alterado na versão 3.9: *unicode* e *recode_encoding* não são mais
   usadas.


PyBytesWriter
*************

The "PyBytesWriter" API can be used to create a Python "bytes" object.

Adicionado na versão 3.15.

type PyBytesWriter

   A bytes writer instance.

   The API is **not thread safe**. To share a writer with multiple
   threads, a critical section or a lock is needed.

   The instance must be destroyed by "PyBytesWriter_Finish()" on
   success, or "PyBytesWriter_Discard()" on error.


Create, Finish, Discard
=======================

PyBytesWriter *PyBytesWriter_Create(Py_ssize_t size)

   Create a "PyBytesWriter" to write *size* bytes.

   If *size* is greater than zero, allocate *size* bytes, and set the
   writer size to *size*. The caller is responsible to write *size*
   bytes using "PyBytesWriter_GetData()". This function does not
   overallocate.

   On error, set an exception and return "NULL".

   *size* must be positive or zero.

PyObject *PyBytesWriter_Finish(PyBytesWriter *writer)

   Finish a "PyBytesWriter" created by "PyBytesWriter_Create()".

   On success, return a Python "bytes" object. On error, set an
   exception and return "NULL".

   The writer instance is invalid after the call in any case. No API
   can be called on the writer after "PyBytesWriter_Finish()".

PyObject *PyBytesWriter_FinishWithSize(PyBytesWriter *writer, Py_ssize_t size)

   Similar to "PyBytesWriter_Finish()", but resize the writer to
   *size* bytes before creating the "bytes" object.

PyObject *PyBytesWriter_FinishWithPointer(PyBytesWriter *writer, void *buf)

   Similar to "PyBytesWriter_Finish()", but resize the writer using
   *buf* pointer before creating the "bytes" object.

   Set an exception and return "NULL" if *buf* pointer is outside the
   internal buffer bounds.

   Function pseudo-code:

      Py_ssize_t size = (char*)buf - (char*)PyBytesWriter_GetData(writer);
      return PyBytesWriter_FinishWithSize(writer, size);

void PyBytesWriter_Discard(PyBytesWriter *writer)

   Discard a "PyBytesWriter" created by "PyBytesWriter_Create()".

   Do nothing if *writer* is "NULL".

   The writer instance is invalid after the call. No API can be called
   on the writer after "PyBytesWriter_Discard()".


High-level API
==============

int PyBytesWriter_WriteBytes(PyBytesWriter *writer, const void *bytes, Py_ssize_t size)

   Grow the *writer* internal buffer by *size* bytes, write *size*
   bytes of *bytes* at the *writer* end, and add *size* to the
   *writer* size.

   If *size* is equal to "-1", call "strlen(bytes)" to get the string
   length.

   On success, return "0". On error, set an exception and return "-1".

int PyBytesWriter_Format(PyBytesWriter *writer, const char *format, ...)

   Similar to "PyBytes_FromFormat()", but write the output directly at
   the writer end. Grow the writer internal buffer on demand. Then add
   the written size to the writer size.

   On success, return "0". On error, set an exception and return "-1".


Getters
=======

Py_ssize_t PyBytesWriter_GetSize(PyBytesWriter *writer)

   Get the writer size.

   The function does not invalidate pointers returned by
   "PyBytesWriter_GetData()".

   The function cannot fail.

void *PyBytesWriter_GetData(PyBytesWriter *writer)

   Get the writer data: start of the internal buffer.

   The pointer remains valid until a "PyBytesWriter" function other
   than "PyBytesWriter_GetData()" or "PyBytesWriter_GetSize()" is
   called on *writer*.

   The function cannot fail.


Low-level API
=============

int PyBytesWriter_Resize(PyBytesWriter *writer, Py_ssize_t size)

   Resize the writer to *size* bytes. It can be used to enlarge or to
   shrink the writer. This function typically overallocates to achieve
   amortized performance when resizing multiple times.

   Newly allocated bytes are left uninitialized.

   On success, return "0". On error, set an exception and return "-1".

   *size* must be positive or zero.

int PyBytesWriter_Grow(PyBytesWriter *writer, Py_ssize_t grow)

   Resize the writer by adding *grow* bytes to the current writer
   size. This function typically overallocates to achieve amortized
   performance when resizing multiple times.

   Newly allocated bytes are left uninitialized.

   On success, return "0". On error, set an exception and return "-1".

   *grow* can be negative to shrink the writer.

void *PyBytesWriter_GrowAndUpdatePointer(PyBytesWriter *writer, Py_ssize_t size, void *buf)

   Similar to "PyBytesWriter_Grow()", but update also the *buf*
   pointer.

   The *buf* pointer is moved if the internal buffer is moved in
   memory. The *buf* relative position within the internal buffer is
   left unchanged.

   On error, set an exception and return "NULL".

   *buf* must not be "NULL".

   Function pseudo-code:

      Py_ssize_t pos = (char*)buf - (char*)PyBytesWriter_GetData(writer);
      if (PyBytesWriter_Grow(writer, size) < 0) {
          return NULL;
      }
      return (char*)PyBytesWriter_GetData(writer) + pos;


Example creating the string "b'abc'"
====================================

Example creating the bytes string "b"abc"", with a fixed size of 3
bytes:

   PyObject* create_abc(void)
   {
       PyBytesWriter *writer = PyBytesWriter_Create(3);
       if (writer == NULL) {
           return NULL;
       }

       char *str = PyBytesWriter_GetData(writer);
       memcpy(str, "abc", 3);
       return PyBytesWriter_Finish(writer);
   }

Variant using a pointer to compute the final size:

   PyObject* create_abc_ptr(void)
   {
       PyBytesWriter *writer = PyBytesWriter_Create(3);
       if (writer == NULL) {
           return NULL;
       }

       char *str = PyBytesWriter_GetData(writer);
       memcpy(str, "abc", 3);
       str += 3;
       return PyBytesWriter_FinishWithPointer(writer, str);
   }


Update "PyBytes_FromStringAndSize()" code
=========================================

Example of code using the soft deprecated
"PyBytes_FromStringAndSize(NULL, size)" API:

   int copy_bytes(char *dest, const char *src, Py_ssize_t num_bytes)
   {
       ...
   }

   PyObject* create_string(const char *start, Py_ssize_t num_bytes)
   {
       PyObject *result = PyBytes_FromStringAndSize(NULL, num_bytes);
       if (result == NULL) {
           return NULL;
       }
       if (copy_bytes(PyBytes_AS_STRING(result), start, num_bytes) < 0) {
           Py_CLEAR(result);
       }
       return result;
   }

It can now be updated to:

   PyObject* create_string(const char *start, Py_ssize_t num_bytes)
   {
       PyBytesWriter *writer = PyBytesWriter_Create(num_bytes);
       if (writer == NULL) {
           return NULL;
       }
       if (copy_bytes(PyBytesWriter_GetData(writer), start, num_bytes) < 0) {
           PyBytesWriter_Discard(writer);
           return NULL;
       }
       return PyBytesWriter_Finish(writer);
   }


Update "_PyBytes_Resize()" code
===============================

Example of code using the soft deprecated "_PyBytes_Resize()" API:

   PyObject* create_string(Py_ssize_t size)
   {
       PyObject *bytes = PyBytes_FromStringAndSize(NULL, size);
       if (bytes == NULL) {
           return NULL;
       }
       char *str = PyBytes_AS_STRING(bytes);

       // ... write data into str ...

       if (_PyBytes_Resize(&bytes, (str - PyBytes_AS_STRING(bytes)))) {
           return NULL;
       }
       return bytes;
   }

It can now be updated to:

   PyObject* create_string(Py_ssize_t size)
   {
       PyBytesWriter *writer = PyBytesWriter_Create(size);
       if (writer == NULL) {
           return NULL;
       }
       char *str = PyBytesWriter_GetData(writer);

       // ... write data into str ...

       return PyBytesWriter_FinishWithPointer(writer, str);
   }
