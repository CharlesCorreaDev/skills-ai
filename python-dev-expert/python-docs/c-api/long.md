Objetos Inteiros
****************

Todos os inteiros são implementados como objetos inteiros "longos" de
tamanho arbitrário.

Em caso de erro, a maioria das APIs "PyLong_As*" retorna "(tipo de
retorno)-1" que não pode ser distinguido de um número. Use
"PyErr_Occurred()" para desambiguar.

type PyLongObject
    * Parte da ABI Estável (como uma estrutura opaca).*

   Este subtipo de "PyObject" representa um objeto inteiro Python.

PyTypeObject PyLong_Type
    * Parte da ABI Estável.*

   Esta instância de "PyTypeObject" representa o tipo inteiro Python.
   Este é o mesmo objeto que "int" na camada Python.

int PyLong_Check(PyObject *p)

   Retorna true se seu argumento é um "PyLongObject" ou um subtipo de
   "PyLongObject". Esta função sempre tem sucesso.

int PyLong_CheckExact(PyObject *p)

   Retorna true se seu argumento é um "PyLongObject", mas não um
   subtipo de "PyLongObject". Esta função sempre tem sucesso.

PyObject *PyLong_FromLong(long v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo objeto "PyLongObject" de *v* ou "NULL" em caso de
   falha.

   **Detalhes da implementação do CPython:** CPython keeps an array of
   integer objects for all integers between "-5" and "1024".  When you
   create an int in that range you actually just get back a reference
   to the existing object.

PyObject *PyLong_FromUnsignedLong(unsigned long v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo objeto "PyLongObject" de um unsigned long C ou
   "NULL" em caso de falha.

PyObject *PyLong_FromSsize_t(Py_ssize_t v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo objeto "PyLongObject" de um "Py_ssize_t" C ou
   "NULL" em caso de falha.

PyObject *PyLong_FromSize_t(size_t v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo objeto "PyLongObject" de um "size_t" C ou "NULL" em
   caso de falha.

PyObject *PyLong_FromLongLong(long long v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo objeto "PyLongObject" de um long long C ou "NULL"
   em caso de falha.

PyObject *PyLong_FromUnsignedLongLong(unsigned long long v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo objeto "PyLongObject" de um unsigned long long C ou
   "NULL" em caso de falha.

PyObject *PyLong_FromInt32(int32_t value)
PyObject *PyLong_FromInt64(int64_t value)
    * Parte da ABI Estável desde a versão 3.14.*

   Retorna um novo objeto "PyLongObject" de um int32_t ou int64_t C
   com sinal, ou "NULL" com uma exceção definida no caso de falha.

   Adicionado na versão 3.14.

PyObject *PyLong_FromUInt32(uint32_t value)
PyObject *PyLong_FromUInt64(uint64_t value)
    * Parte da ABI Estável desde a versão 3.14.*

   Retorna um novo objeto "PyLongObject" de um uint32_t ou uint64_t C
   sem sinal, ou "NULL" com uma exceção definida no caso de falha.

   Adicionado na versão 3.14.

PyObject *PyLong_FromDouble(double v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo objeto "PyLongObject" da parte inteira de *v* ou
   "NULL" em caso de falha.

PyObject *PyLong_FromString(const char *str, char **pend, int base)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo "PyLongObject" com base no valor da string em
   *str*, que é interpretado de acordo com a raiz em *base* ou "NULL"
   em caso de falha. Se *pend* não for "NULL", **pend* apontará para o
   fim do *str* em caso de sucesso ou para seu primeiro caractere que
   não pode ser processado em caso de erro. Se *base* for "0", *str* é
   interpretado usando a definição de Inteiros literais; neste caso,
   zeros à esquerda em um número decimal diferente de zero aumenta um
   "ValueError". Se *base* não for "0", deve estar entre "2" e "36",
   inclusive. Espaços em branco no início ou no final e sublinhados
   simples após um especificador de base e entre dígitos são
   ignorados. Se não houver dígitos ou *str* não for terminado em NULL
   após os dígitos e espaços em branco à direita, "ValueError" será
   levantada.

   Ver também:

     As funções "PyLong_AsNativeBytes()" e "PyLong_FromNativeBytes()"
     podem ser usadas para converter um "PyLongObject" de/para uma
     vetor de bytes na base "256".

PyObject *PyLong_FromUnicodeObject(PyObject *u, int base)
    *Retorna valor: Nova referência.*

   Converte uma sequência de dígitos Unicode na string *u* para um
   valor inteiro Python.

   Adicionado na versão 3.3.

PyObject *PyLong_FromVoidPtr(void *p)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Cria um inteiro Python a partir do ponteiro *p*. O valor do
   ponteiro pode ser recuperado do valor resultante usando
   "PyLong_AsVoidPtr()".

PyObject *PyLong_FromNativeBytes(const void *buffer, size_t n_bytes, int flags)
    * Parte da ABI Estável desde a versão 3.14.*

   Create a Python integer from the value contained in the first
   *n_bytes* of *buffer*, interpreted as a two's-complement signed
   number.

   *flags* are as for "PyLong_AsNativeBytes()". Passing "-1" will
   select the native endian that CPython was compiled with and assume
   that the most-significant bit is a sign bit. Passing
   "Py_ASNATIVEBYTES_UNSIGNED_BUFFER" will produce the same result as
   calling "PyLong_FromUnsignedNativeBytes()". Other flags are
   ignored.

   Adicionado na versão 3.13.

PyObject *PyLong_FromUnsignedNativeBytes(const void *buffer, size_t n_bytes, int flags)
    * Parte da ABI Estável desde a versão 3.14.*

   Create a Python integer from the value contained in the first
   *n_bytes* of *buffer*, interpreted as an unsigned number.

   *flags* are as for "PyLong_AsNativeBytes()". Passing "-1" will
   select the native endian that CPython was compiled with and assume
   that the most-significant bit is not a sign bit. Flags other than
   endian are ignored.

   Adicionado na versão 3.13.

PyLong_FromPid(pid)

   Macro for creating a Python integer from a process identifier.

   This can be defined as an alias to "PyLong_FromLong()" or
   "PyLong_FromLongLong()", depending on the size of the system's PID
   type.

   Adicionado na versão 3.2.

long PyLong_AsLong(PyObject *obj)
    * Parte da ABI Estável.*

   Return a C long representation of *obj*.  If *obj* is not an
   instance of "PyLongObject", first call its "__index__()" method (if
   present) to convert it to a "PyLongObject".

   Raise "OverflowError" if the value of *obj* is out of range for a
   long.

   Retorna "-1" no caso de erro.  Use "PyErr_Occurred()" para
   desambiguar.

   Alterado na versão 3.8: Usa "__index__()", se disponível.

   Alterado na versão 3.10: This function will no longer use
   "__int__()".

   long PyLong_AS_LONG(PyObject *obj)

      Exactly equivalent to the preferred "PyLong_AsLong". In
      particular, it can fail with "OverflowError" or another
      exception.

      Suavemente descontinuado desde a versão 3.14.

int PyLong_AsInt(PyObject *obj)
    * Parte da ABI Estável desde a versão 3.13.*

   Similar to "PyLong_AsLong()", but store the result in a C int
   instead of a C long.

   Adicionado na versão 3.13.

long PyLong_AsLongAndOverflow(PyObject *obj, int *overflow)
    * Parte da ABI Estável.*

   Return a C long representation of *obj*.  If *obj* is not an
   instance of "PyLongObject", first call its "__index__()" method (if
   present) to convert it to a "PyLongObject".

   If the value of *obj* is greater than "LONG_MAX" or less than
   "LONG_MIN", set **overflow* to "1" or "-1", respectively, and
   return "-1"; otherwise, set **overflow* to "0".  If any other
   exception occurs set **overflow* to "0" and return "-1" as usual.

   Retorna "-1" no caso de erro.  Use "PyErr_Occurred()" para
   desambiguar.

   Alterado na versão 3.8: Usa "__index__()", se disponível.

   Alterado na versão 3.10: This function will no longer use
   "__int__()".

long long PyLong_AsLongLong(PyObject *obj)
    * Parte da ABI Estável.*

   Return a C long long representation of *obj*.  If *obj* is not an
   instance of "PyLongObject", first call its "__index__()" method (if
   present) to convert it to a "PyLongObject".

   Raise "OverflowError" if the value of *obj* is out of range for a
   long long.

   Retorna "-1" no caso de erro.  Use "PyErr_Occurred()" para
   desambiguar.

   Alterado na versão 3.8: Usa "__index__()", se disponível.

   Alterado na versão 3.10: This function will no longer use
   "__int__()".

long long PyLong_AsLongLongAndOverflow(PyObject *obj, int *overflow)
    * Parte da ABI Estável.*

   Return a C long long representation of *obj*.  If *obj* is not an
   instance of "PyLongObject", first call its "__index__()" method (if
   present) to convert it to a "PyLongObject".

   If the value of *obj* is greater than "LLONG_MAX" or less than
   "LLONG_MIN", set **overflow* to "1" or "-1", respectively, and
   return "-1"; otherwise, set **overflow* to "0".  If any other
   exception occurs set **overflow* to "0" and return "-1" as usual.

   Retorna "-1" no caso de erro.  Use "PyErr_Occurred()" para
   desambiguar.

   Adicionado na versão 3.2.

   Alterado na versão 3.8: Usa "__index__()", se disponível.

   Alterado na versão 3.10: This function will no longer use
   "__int__()".

Py_ssize_t PyLong_AsSsize_t(PyObject *pylong)
    * Parte da ABI Estável.*

   Retorna uma representação de "Py_ssize_t" C de *pylong*. *pylong*
   deve ser uma instância de "PyLongObject".

   Levanta "OverflowError" se o valor de *pylong* estiver fora do
   intervalo de um "Py_ssize_t".

   Retorna "-1" no caso de erro.  Use "PyErr_Occurred()" para
   desambiguar.

unsigned long PyLong_AsUnsignedLong(PyObject *pylong)
    * Parte da ABI Estável.*

   Return a C unsigned long representation of *pylong*.  *pylong* must
   be an instance of "PyLongObject".

   Raise "OverflowError" if the value of *pylong* is out of range for
   a unsigned long.

   Retorna "(unsigned long)-1" no caso de erro.  Use
   "PyErr_Occurred()" para desambiguar.

size_t PyLong_AsSize_t(PyObject *pylong)
    * Parte da ABI Estável.*

   Retorna uma representação de "size_t" C de *pylong*. *pylong* deve
   ser uma instância de "PyLongObject".

   Levanta "OverflowError" se o valor de *pylong* estiver fora do
   intervalo de um "size_t".

   Retorna "(size)-1" no caso de erro.  Use "PyErr_Occurred()" para
   desambiguar.

unsigned long long PyLong_AsUnsignedLongLong(PyObject *pylong)
    * Parte da ABI Estável.*

   Return a C unsigned long long representation of *pylong*.  *pylong*
   must be an instance of "PyLongObject".

   Raise "OverflowError" if the value of *pylong* is out of range for
   an unsigned long long.

   Retorna "(unsigned long long)-1" no caso de erro.  Use
   "PyErr_Occurred()" para desambiguar.

   Alterado na versão 3.1: Um *pylong* negativo agora levanta
   "OverflowError", não "TypeError".

unsigned long PyLong_AsUnsignedLongMask(PyObject *obj)
    * Parte da ABI Estável.*

   Return a C unsigned long representation of *obj*.  If *obj* is not
   an instance of "PyLongObject", first call its "__index__()" method
   (if present) to convert it to a "PyLongObject".

   If the value of *obj* is out of range for an unsigned long, return
   the reduction of that value modulo "ULONG_MAX + 1".

   Retorna "(unsigned long)-1" no caso de erro.  Use
   "PyErr_Occurred()" para desambiguar.

   Alterado na versão 3.8: Usa "__index__()", se disponível.

   Alterado na versão 3.10: This function will no longer use
   "__int__()".

unsigned long long PyLong_AsUnsignedLongLongMask(PyObject *obj)
    * Parte da ABI Estável.*

   Return a C unsigned long long representation of *obj*.  If *obj* is
   not an instance of "PyLongObject", first call its "__index__()"
   method (if present) to convert it to a "PyLongObject".

   If the value of *obj* is out of range for an unsigned long long,
   return the reduction of that value modulo "ULLONG_MAX + 1".

   Retorna "(unsigned long long)-1" no caso de erro.  Use
   "PyErr_Occurred()" para desambiguar.

   Alterado na versão 3.8: Usa "__index__()", se disponível.

   Alterado na versão 3.10: This function will no longer use
   "__int__()".

int PyLong_AsInt32(PyObject *obj, int32_t *value)
int PyLong_AsInt64(PyObject *obj, int64_t *value)
    * Parte da ABI Estável desde a versão 3.14.*

   Set **value* to a signed C int32_t or int64_t representation of
   *obj*.

   If *obj* is not an instance of "PyLongObject", first call its
   "__index__()" method (if present) to convert it to a
   "PyLongObject".

   If the *obj* value is out of range, raise an "OverflowError".

   Set **value* and return "0" on success. Set an exception and return
   "-1" on error.

   *value* must not be "NULL".

   Adicionado na versão 3.14.

int PyLong_AsUInt32(PyObject *obj, uint32_t *value)
int PyLong_AsUInt64(PyObject *obj, uint64_t *value)
    * Parte da ABI Estável desde a versão 3.14.*

   Set **value* to an unsigned C uint32_t or uint64_t representation
   of *obj*.

   If *obj* is not an instance of "PyLongObject", first call its
   "__index__()" method (if present) to convert it to a
   "PyLongObject".

   * If *obj* is negative, raise a "ValueError".

   * If the *obj* value is out of range, raise an "OverflowError".

   Set **value* and return "0" on success. Set an exception and return
   "-1" on error.

   *value* must not be "NULL".

   Adicionado na versão 3.14.

double PyLong_AsDouble(PyObject *pylong)
    * Parte da ABI Estável.*

   Return a C double representation of *pylong*.  *pylong* must be an
   instance of "PyLongObject".

   Raise "OverflowError" if the value of *pylong* is out of range for
   a double.

   Retorna "-1.0" no caso de erro.  Use "PyErr_Occurred()" para
   desambiguar.

void *PyLong_AsVoidPtr(PyObject *pylong)
    * Parte da ABI Estável.*

   Convert a Python integer *pylong* to a C void pointer. If *pylong*
   cannot be converted, an "OverflowError" will be raised.  This is
   only assured to produce a usable void pointer for values created
   with "PyLong_FromVoidPtr()".

   Retorna "NULL" no caso de erro.  Use "PyErr_Occurred()" para
   desambiguar.

Py_ssize_t PyLong_AsNativeBytes(PyObject *pylong, void *buffer, Py_ssize_t n_bytes, int flags)
    * Parte da ABI Estável desde a versão 3.14.*

   Copy the Python integer value *pylong* to a native *buffer* of size
   *n_bytes*. The *flags* can be set to "-1" to behave similarly to a
   C cast, or to values documented below to control the behavior.

   Returns "-1" with an exception raised on error.  This may happen if
   *pylong* cannot be interpreted as an integer, or if *pylong* was
   negative and the "Py_ASNATIVEBYTES_REJECT_NEGATIVE" flag was set.

   Otherwise, returns the number of bytes required to store the value.
   If this is equal to or less than *n_bytes*, the entire value was
   copied. All *n_bytes* of the buffer are written: remaining bytes
   filled by copies of the sign bit.

   If the returned value is greater than *n_bytes*, the value was
   truncated: as many of the lowest bits of the value as could fit are
   written, and the higher bits are ignored. This matches the typical
   behavior of a C-style downcast.

   Nota:

     Overflow is not considered an error. If the returned value is
     larger than *n_bytes*, most significant bits were discarded.

   "0" will never be returned.

   Values are always copied as two's-complement.

   Usage example:

      int32_t value;
      Py_ssize_t bytes = PyLong_AsNativeBytes(pylong, &value, sizeof(value), -1);
      if (bytes < 0) {
          // Failed. A Python exception was set with the reason.
          return NULL;
      }
      else if (bytes <= (Py_ssize_t)sizeof(value)) {
          // Success!
      }
      else {
          // Overflow occurred, but 'value' contains the truncated
          // lowest bits of pylong.
      }

   Passing zero to *n_bytes* will return the size of a buffer that
   would be large enough to hold the value. This may be larger than
   technically necessary, but not unreasonably so. If *n_bytes=0*,
   *buffer* may be "NULL".

   Nota:

     Passing *n_bytes=0* to this function is not an accurate way to
     determine the bit length of the value.

   To get at the entire Python value of an unknown size, the function
   can be called twice: first to determine the buffer size, then to
   fill it:

      // Ask how much space we need.
      Py_ssize_t expected = PyLong_AsNativeBytes(pylong, NULL, 0, -1);
      if (expected < 0) {
          // Failed. A Python exception was set with the reason.
          return NULL;
      }
      assert(expected != 0);  // Impossible per the API definition.
      uint8_t *bignum = malloc(expected);
      if (!bignum) {
          PyErr_SetString(PyExc_MemoryError, "bignum malloc failed.");
          return NULL;
      }
      // Safely get the entire value.
      Py_ssize_t bytes = PyLong_AsNativeBytes(pylong, bignum, expected, -1);
      if (bytes < 0) {  // Exception has been set.
          free(bignum);
          return NULL;
      }
      else if (bytes > expected) {  // This should not be possible.
          PyErr_SetString(PyExc_RuntimeError,
              "Unexpected bignum truncation after a size check.");
          free(bignum);
          return NULL;
      }
      // The expected success given the above pre-check.
      // ... use bignum ...
      free(bignum);

   *flags* is either "-1" ("Py_ASNATIVEBYTES_DEFAULTS") to select
   defaults that behave most like a C cast, or a combination of the
   other flags in the table below. Note that "-1" cannot be combined
   with other flags.

   Currently, "-1" corresponds to "Py_ASNATIVEBYTES_NATIVE_ENDIAN |
   Py_ASNATIVEBYTES_UNSIGNED_BUFFER".

   These values are available when compiling for the Stable ABI since
   version 3.14.

   +-----------------------------------------------+--------+
   | Sinalizador                                   | Valor  |
   |===============================================|========|
   | Py_ASNATIVEBYTES_DEFAULTS                     | "-1"   |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_BIG_ENDIAN                   | "0"    |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_LITTLE_ENDIAN                | "1"    |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_NATIVE_ENDIAN                | "3"    |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_UNSIGNED_BUFFER              | "4"    |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_REJECT_NEGATIVE              | "8"    |
   +-----------------------------------------------+--------+
   | Py_ASNATIVEBYTES_ALLOW_INDEX                  | "16"   |
   +-----------------------------------------------+--------+

   Specifying "Py_ASNATIVEBYTES_NATIVE_ENDIAN" will override any other
   endian flags. Passing "2" is reserved.

   By default, sufficient buffer will be requested to include a sign
   bit. For example, when converting 128 with *n_bytes=1*, the
   function will return 2 (or more) in order to store a zero sign bit.

   If "Py_ASNATIVEBYTES_UNSIGNED_BUFFER" is specified, a zero sign bit
   will be omitted from size calculations. This allows, for example,
   128 to fit in a single-byte buffer. If the destination buffer is
   later treated as signed, a positive input value may become
   negative. Note that the flag does not affect handling of negative
   values: for those, space for a sign bit is always requested.

   Specifying "Py_ASNATIVEBYTES_REJECT_NEGATIVE" causes an exception
   to be set if *pylong* is negative. Without this flag, negative
   values will be copied provided there is enough space for at least
   one sign bit, regardless of whether
   "Py_ASNATIVEBYTES_UNSIGNED_BUFFER" was specified.

   If "Py_ASNATIVEBYTES_ALLOW_INDEX" is specified and a non-integer
   value is passed, its "__index__()" method will be called first.
   This may result in Python code executing and other threads being
   allowed to run, which could cause changes to other objects or
   values in use. When *flags* is "-1", this option is not set, and
   non-integer values will raise "TypeError".

   Nota:

     With the default *flags* ("-1", or *UNSIGNED_BUFFER*  without
     *REJECT_NEGATIVE*), multiple Python integers can map to a single
     value without overflow. For example, both "255" and "-1" fit a
     single-byte buffer and set all its bits. This matches typical C
     cast behavior.

   Adicionado na versão 3.13.

PyLong_AsPid(pid)

   Macro for converting a Python integer into a process identifier.

   This can be defined as an alias to "PyLong_AsLong()",
   "PyLong_FromLongLong()", or "PyLong_AsInt()", depending on the size
   of the system's PID type.

   Adicionado na versão 3.2.

int PyLong_GetSign(PyObject *obj, int *sign)

   Get the sign of the integer object *obj*.

   On success, set **sign* to the integer sign  (0, -1 or +1 for zero,
   negative or positive integer, respectively) and return 0.

   On failure, return -1 with an exception set.  This function always
   succeeds if *obj* is a "PyLongObject" or its subtype.

   Adicionado na versão 3.14.

int PyLong_IsPositive(PyObject *obj)

   Check if the integer object *obj* is positive ("obj > 0").

   If *obj* is an instance of "PyLongObject" or its subtype, return
   "1" when it's positive and "0" otherwise.  Else set an exception
   and return "-1".

   Adicionado na versão 3.14.

int PyLong_IsNegative(PyObject *obj)

   Check if the integer object *obj* is negative ("obj < 0").

   If *obj* is an instance of "PyLongObject" or its subtype, return
   "1" when it's negative and "0" otherwise.  Else set an exception
   and return "-1".

   Adicionado na versão 3.14.

int PyLong_IsZero(PyObject *obj)

   Check if the integer object *obj* is zero.

   If *obj* is an instance of "PyLongObject" or its subtype, return
   "1" when it's zero and "0" otherwise.  Else set an exception and
   return "-1".

   Adicionado na versão 3.14.

PyObject *PyLong_GetInfo(void)
    * Parte da ABI Estável.*

   On success, return a read only *named tuple*, that holds
   information about Python's internal representation of integers. See
   "sys.int_info" for description of individual fields.

   Em caso de falha, retorna "NULL" com uma exceção definida.

   Adicionado na versão 3.1.

int PyUnstable_Long_IsCompact(const PyLongObject *op)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Return 1 if *op* is compact, 0 otherwise.

   This function makes it possible for performance-critical code to
   implement a “fast path” for small integers. For compact values use
   "PyUnstable_Long_CompactValue()"; for others fall back to a
   "PyLong_As*" function or "PyLong_AsNativeBytes()".

   The speedup is expected to be negligible for most users.

   Exactly what values are considered compact is an implementation
   detail and is subject to change.

   Adicionado na versão 3.12.

Py_ssize_t PyUnstable_Long_CompactValue(const PyLongObject *op)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   If *op* is compact, as determined by "PyUnstable_Long_IsCompact()",
   return its value.

   Otherwise, the return value is undefined.

   Adicionado na versão 3.12.


Build configuration
===================

PYLONG_BITS_IN_DIGIT

   The number of bits in each digit of CPython's native representation
   of integers. The value can currently be either "30" (the default)
   or "15", selected with "--enable-big-digits" when building Python.

   To access the native representation of integers, use
   "PyLong_GetNativeLayout()" and its "bits_per_digit" member instead.


Export API
==========

Adicionado na versão 3.14.

type PyLongLayout
    * Parte da ABI Estável (incluindo todos os membros) desde a versão
   3.15.*

   Layout of an array of "digits" ("limbs" in the GMP terminology),
   used to represent absolute value for arbitrary precision integers.

   Use "PyLong_GetNativeLayout()" to get the native layout of Python
   "int" objects, used internally for integers with "big enough"
   absolute value.

   See also "sys.int_info" which exposes similar information in
   Python.

   uint8_t bits_per_digit

      Bits per digit. For example, a 15 bit digit means that bits 0-14
      contain meaningful information.

   uint8_t digit_size

      Digit size in bytes. For example, a 15 bit digit will require at
      least 2 bytes.

   int8_t digits_order

      Digits order:

      * "1" for most significant digit first

      * "-1" for least significant digit first

   int8_t digit_endianness

      Digit endianness:

      * "1" for most significant byte first (big endian)

      * "-1" for least significant byte first (little endian)

const PyLongLayout *PyLong_GetNativeLayout(void)
    * Parte da ABI Estável desde a versão 3.15.*

   Get the native layout of Python "int" objects.

   See the "PyLongLayout" structure.

   The function must not be called before Python initialization nor
   after Python finalization. The returned layout is valid until
   Python is finalized. The layout is the same for all Python sub-
   interpreters in a process, and so it can be cached.

type PyLongExport
    * Parte da ABI Estável (incluindo todos os membros) desde a versão
   3.15.*

   Export of a Python "int" object.

   There are two cases:

   * If "digits" is "NULL", only use the "value" member.

   * If "digits" is not "NULL", use "negative", "ndigits" and "digits"
     members.

   int64_t value

      The native integer value of the exported "int" object. Only
      valid if "digits" is "NULL".

   uint8_t negative

      "1" if the number is negative, "0" otherwise. Only valid if
      "digits" is not "NULL".

   Py_ssize_t ndigits

      Number of digits in "digits" array. Only valid if "digits" is
      not "NULL".

   const void *digits

      Read-only array of unsigned digits. Can be "NULL".

int PyLong_Export(PyObject *obj, PyLongExport *export_long)
    * Parte da ABI Estável desde a versão 3.15.*

   Export a Python "int" object.

   *export_long* must point to a "PyLongExport" structure allocated by
   the caller. It must not be "NULL".

   On success, fill in **export_long* and return "0". On error, set an
   exception and return "-1".

   "PyLong_FreeExport()" must be called when the export is no longer
   needed.

      **Detalhes da implementação do CPython:** This function always
      succeeds if *obj* is a Python "int" object or a subclass.

void PyLong_FreeExport(PyLongExport *export_long)
    * Parte da ABI Estável desde a versão 3.15.*

   Release the export *export_long* created by "PyLong_Export()".

   **Detalhes da implementação do CPython:** Calling
   "PyLong_FreeExport()" is optional if *export_long->digits* is
   "NULL".


PyLongWriter API
================

The "PyLongWriter" API can be used to import an integer.

Adicionado na versão 3.14.

type PyLongWriter
    * Parte da ABI Estável (como uma estrutura opaca) desde a versão
   3.15.*

   A Python "int" writer instance.

   The instance must be destroyed by "PyLongWriter_Finish()" or
   "PyLongWriter_Discard()".

PyLongWriter *PyLongWriter_Create(int negative, Py_ssize_t ndigits, void **digits)
    * Parte da ABI Estável desde a versão 3.15.*

   Create a "PyLongWriter".

   On success, allocate **digits* and return a writer. On error, set
   an exception and return "NULL".

   *negative* is "1" if the number is negative, or "0" otherwise.

   *ndigits* is the number of digits in the *digits* array. It must be
   greater than 0.

   *digits* must not be NULL.

   After a successful call to this function, the caller should fill in
   the array of digits *digits* and then call "PyLongWriter_Finish()"
   to get a Python "int". The layout of *digits* is described by
   "PyLong_GetNativeLayout()".

   Digits must be in the range ["0"; "(1 << bits_per_digit) - 1"]
   (where the "bits_per_digit" is the number of bits per digit). Any
   unused most significant digits must be set to "0".

   Alternately, call "PyLongWriter_Discard()" to destroy the writer
   instance without creating an "int" object.

PyObject *PyLongWriter_Finish(PyLongWriter *writer)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.15.*

   Finish a "PyLongWriter" created by "PyLongWriter_Create()".

   On success, return a Python "int" object. On error, set an
   exception and return "NULL".

   The function takes care of normalizing the digits and converts the
   object to a compact integer if needed.

   The writer instance and the *digits* array are invalid after the
   call.

void PyLongWriter_Discard(PyLongWriter *writer)
    * Parte da ABI Estável desde a versão 3.15.*

   Discard a "PyLongWriter" created by "PyLongWriter_Create()".

   If *writer* is "NULL", no operation is performed.

   The writer instance and the *digits* array are invalid after the
   call.


Deprecated API
==============

These macros are *soft deprecated*. They describe parameters of the
internal representation of "PyLongObject" instances.

Use "PyLong_GetNativeLayout()" instead, along with "PyLong_Export()"
to read integer data or "PyLongWriter" to write it. These currently
use the same layout, but are designed to continue working correctly
even if CPython's internal integer representation changes.

PyLong_SHIFT

   This is equivalent to "bits_per_digit" in the output of
   "PyLong_GetNativeLayout()".

PyLong_BASE

   This is currently equivalent to 1 << PyLong_SHIFT.

PyLong_MASK

   This is currently equivalent to (1 << PyLong_SHIFT) - 1
