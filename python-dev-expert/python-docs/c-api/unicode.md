Objetos Unicode e Codecs
************************


Objetos Unicode
===============

Desde a implementação da **PEP 393** no Python 3.3, os objetos Unicode
usam internamente uma variedade de representações para permitir o
processamento de toda a gama de caracteres Unicode, mantendo a
eficiência de memória. Há casos especiais para strings em que todos os
pontos de código estão abaixo de 128, 256 ou 65536; caso contrário, os
pontos de código devem estar abaixo de 1114112 (que é a gama completa
de caracteres Unicode).

A representação UTF-8 é criada sob demanda e armazenada em cache no
objeto Unicode.

**Detalhes da implementação do CPython:** The internal buffer always
includes an extra trailing null character for compatibility with null
terminated C strings. This extra character is not counted in
"PyUnicode_GetLength()" nor in the various *size* arguments of the
functions below.

Nota:

  A representação "Py_UNICODE" foi removida desde o Python 3.12 com
  APIs descontinuadas. Consulte **PEP 623** para obter mais
  informações.


Tipo Unicode
------------

Estes são os tipos básicos de objetos Unicode usados para a
implementação Unicode em Python:

PyTypeObject PyUnicode_Type
    * Parte da ABI Estável.*

   This instance of "PyTypeObject" represents the Python Unicode type.
   It is exposed to Python code as "str".

PyTypeObject PyUnicodeIter_Type
    * Parte da ABI Estável.*

   Esta instância de "PyTypeObject" representa o tipo iterador Unicode
   do Python. É usada para iterar sobre objetos string Unicode.

type Py_UCS4
type Py_UCS2
type Py_UCS1
    * Parte da ABI Estável.*

   Esses tipos são definições de tipo para tipos inteiros sem sinal,
   amplos o suficiente para conter caracteres de 32 bits, 16 bits e 8
   bits, respectivamente. Ao lidar com caracteres Unicode simples, use
   "Py_UCS4".

   Adicionado na versão 3.3.

type PyASCIIObject
type PyCompactUnicodeObject
type PyUnicodeObject

   Esses subtipos de "PyObject" representam um objeto Unicode do
   Python. Em quase todos os casos, eles não devem ser usados
   diretamente, pois todas as funções da API que lidam com objetos
   Unicode recebem e retornam ponteiros "PyObject".

   Adicionado na versão 3.3.

   The structure of a particular object can be determined using the
   following macros. The macros cannot fail; their behavior is
   undefined if their argument is not a Python Unicode object.

   PyUnicode_IS_COMPACT(o)

      True if *o* uses the "PyCompactUnicodeObject" structure.

      Adicionado na versão 3.3.

   PyUnicode_IS_COMPACT_ASCII(o)

      True if *o* uses the "PyASCIIObject" structure.

      Adicionado na versão 3.3.

As seguintes APIs são macros C e funções estáticas embutidas para
verificações rápidas e acesso a dados internos somente leitura de
objetos Unicode:

int PyUnicode_Check(PyObject *obj)

   Retorna verdadeiro se o objeto *obj* for um objeto Unicode ou uma
   instância de um subtipo Unicode. Esta função sempre tem sucesso.

int PyUnicode_CheckExact(PyObject *obj)

   Retorna verdadeiro se o objeto *obj* for um objeto Unicode, mas não
   uma instância de um subtipo. Esta função sempre tem sucesso.

Py_ssize_t PyUnicode_GET_LENGTH(PyObject *unicode)

   Retorna o comprimento da string Unicode, em pontos de código.
   *unicode* deve ser um objeto Unicode na representação "canônica"
   (não marcado).

   Adicionado na versão 3.3.

Py_UCS1 *PyUnicode_1BYTE_DATA(PyObject *unicode)
Py_UCS2 *PyUnicode_2BYTE_DATA(PyObject *unicode)
Py_UCS4 *PyUnicode_4BYTE_DATA(PyObject *unicode)

   Retorna um ponteiro para a representação canônica convertida para
   tipos inteiros UCS1, UCS2 ou UCS4 para acesso direto aos
   caracteres. Nenhuma verificação é realizada se a representação
   canônica tem o tamanho de caractere correto; use "PyUnicode_KIND()"
   para selecionar a função correta.

   Adicionado na versão 3.3.

PyUnicode_1BYTE_KIND
PyUnicode_2BYTE_KIND
PyUnicode_4BYTE_KIND

   Valores de retorno da macro "PyUnicode_KIND()".

   Adicionado na versão 3.3.

   Alterado na versão 3.12: "PyUnicode_WCHAR_KIND" foi removida.

int PyUnicode_KIND(PyObject *unicode)

   Retorna uma das constantes do tipo PyUnicode (veja acima) que
   indicam quantos bytes por caractere este objeto Unicode usa para
   armazenar seus dados. *unicode* precisa ser um objeto Unicode na
   representação "canônica" (não marcado).

   Adicionado na versão 3.3.

void *PyUnicode_DATA(PyObject *unicode)

   Retorna um ponteiro vazio para o buffer Unicode bruto. *unicode*
   deve ser um objeto Unicode na representação "canônica" (não
   marcado).

   Adicionado na versão 3.3.

void PyUnicode_WRITE(int kind, void *data, Py_ssize_t index, Py_UCS4 value)

   Write the code point *value* to the given zero-based *index* in a
   string.

   The *kind* value and *data* pointer must have been obtained from a
   string using "PyUnicode_KIND()" and "PyUnicode_DATA()"
   respectively. You must hold a reference to that string while
   calling "PyUnicode_WRITE()". All requirements of
   "PyUnicode_WriteChar()" also apply.

   The function performs no checks for any of its requirements, and is
   intended for usage in loops.

   Adicionado na versão 3.3.

Py_UCS4 PyUnicode_READ(int kind, void *data, Py_ssize_t index)

   Read a code point from a canonical representation *data* (as
   obtained with "PyUnicode_DATA()").  No checks are performed.

   **Detalhes da implementação do CPython:** Accept reading the
   trailing null character at index "PyUnicode_GetLength()".

   Adicionado na versão 3.3.

Py_UCS4 PyUnicode_READ_CHAR(PyObject *unicode, Py_ssize_t index)

   Lê um caractere de um objeto Unicode *unicode*, que deve estar na
   representação "canônica". Isso é menos eficiente do que
   "PyUnicode_READ()" se você fizer várias leituras consecutivas.

   **Detalhes da implementação do CPython:** Accept reading the
   trailing null character at index "PyUnicode_GetLength()".

   Adicionado na versão 3.3.

Py_UCS4 PyUnicode_MAX_CHAR_VALUE(PyObject *unicode)

   Retorna o ponto de código máximo adequado para criar outra string
   baseada em *unicode*, que deve estar na representação "canônica".
   Isso é sempre uma aproximação, mas é mais eficiente do que iterar
   sobre a string.

   Adicionado na versão 3.3.

int PyUnicode_IsIdentifier(PyObject *unicode)
    * Parte da ABI Estável.*

   Retorna "1" se a string é um identificador válido conforme a
   definição da linguagem, seção Nomes (identificadores e palavras
   reservadas). Do contrário, retorna "0".

   Alterado na versão 3.9: A função não chama mais "Py_FatalError()"
   se a string não estiver pronta.

unsigned int PyUnicode_IS_ASCII(PyObject *unicode)

   Return true if the string only contains ASCII characters.
   Equivalent to "str.isascii()".

   Adicionado na versão 3.2.

Py_hash_t PyUnstable_Unicode_GET_CACHED_HASH(PyObject *str)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   If the hash of *str*, as returned by "PyObject_Hash()", has been
   cached and is immediately available, return it. Otherwise, return
   "-1" *without* setting an exception.

   If *str* is not a string (that is, if "PyUnicode_Check(obj)" is
   false), the behavior is undefined.

   This function never fails with an exception.

   Note that there are no guarantees on when an object's hash is
   cached, and the (non-)existence of a cached hash does not imply
   that the string has any other properties.


Propriedade de caracteres Unicode
---------------------------------

O Unicode fornece muitas propriedades de caracteres diferentes. As
mais frequentemente necessárias estão disponíveis por meio destas
macros, que são mapeadas para funções C, dependendo da configuração do
Python.

int Py_UNICODE_ISSPACE(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere de espaço em
   branco.

int Py_UNICODE_ISLOWER(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere minúsculo.

int Py_UNICODE_ISUPPER(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere maiúsculo.

int Py_UNICODE_ISTITLE(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere em TitleCase.

int Py_UNICODE_ISLINEBREAK(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere de quebra de
   linha.

int Py_UNICODE_ISDECIMAL(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere decimal.

int Py_UNICODE_ISDIGIT(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere de dígito.

int Py_UNICODE_ISNUMERIC(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere numérico.

int Py_UNICODE_ISALPHA(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere alfabético.

int Py_UNICODE_ISALNUM(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere alfanumérico.

int Py_UNICODE_ISPRINTABLE(Py_UCS4 ch)

   Retorna "1" ou "0" dependendo se *ch* é um caractere imprimível, no
   sentido de "str.isprintable()".

These APIs can be used for fast direct character conversions:

Py_UCS4 Py_UNICODE_TOLOWER(Py_UCS4 ch)

   Return the character *ch* converted to lower case.

Py_UCS4 Py_UNICODE_TOUPPER(Py_UCS4 ch)

   Return the character *ch* converted to upper case.

Py_UCS4 Py_UNICODE_TOTITLE(Py_UCS4 ch)

   Return the character *ch* converted to title case.

int Py_UNICODE_TODECIMAL(Py_UCS4 ch)

   Return the character *ch* converted to a decimal positive integer.
   Return "-1" if this is not possible.  This function does not raise
   exceptions.

int Py_UNICODE_TODIGIT(Py_UCS4 ch)

   Return the character *ch* converted to a single digit integer.
   Return "-1" if this is not possible.  This function does not raise
   exceptions.

double Py_UNICODE_TONUMERIC(Py_UCS4 ch)

   Return the character *ch* converted to a double. Return "-1.0" if
   this is not possible.  This function does not raise exceptions.

These APIs can be used to work with surrogates:

int Py_UNICODE_IS_SURROGATE(Py_UCS4 ch)

   Check if *ch* is a surrogate ("0xD800 <= ch <= 0xDFFF").

int Py_UNICODE_IS_HIGH_SURROGATE(Py_UCS4 ch)

   Check if *ch* is a high surrogate ("0xD800 <= ch <= 0xDBFF").

int Py_UNICODE_IS_LOW_SURROGATE(Py_UCS4 ch)

   Check if *ch* is a low surrogate ("0xDC00 <= ch <= 0xDFFF").

Py_UCS4 Py_UNICODE_HIGH_SURROGATE(Py_UCS4 ch)

   Return the high UTF-16 surrogate ("0xD800" to "0xDBFF") for a
   Unicode code point in the range "[0x10000; 0x10FFFF]".

Py_UCS4 Py_UNICODE_LOW_SURROGATE(Py_UCS4 ch)

   Return the low UTF-16 surrogate ("0xDC00" to "0xDFFF") for a
   Unicode code point in the range "[0x10000; 0x10FFFF]".

Py_UCS4 Py_UNICODE_JOIN_SURROGATES(Py_UCS4 high, Py_UCS4 low)

   Join two surrogate code points and return a single "Py_UCS4" value.
   *high* and *low* are respectively the leading and trailing
   surrogates in a surrogate pair. *high* must be in the range
   "[0xD800; 0xDBFF]" and *low* must be in the range "[0xDC00;
   0xDFFF]".


Creating and accessing Unicode strings
--------------------------------------

To create Unicode objects and access their basic sequence properties,
use these APIs:

PyObject *PyUnicode_New(Py_ssize_t size, Py_UCS4 maxchar)
    *Retorna valor: Nova referência.*

   Create a new Unicode object.  *maxchar* should be the true maximum
   code point to be placed in the string.  As an approximation, it can
   be rounded up to the nearest value in the sequence 127, 255, 65535,
   1114111.

   On error, set an exception and return "NULL".

   After creation, the string can be filled by
   "PyUnicode_WriteChar()", "PyUnicode_CopyCharacters()",
   "PyUnicode_Fill()", "PyUnicode_WRITE()" or similar. Since strings
   are supposed to be immutable, take care to not “use” the result
   while it is being modified. In particular, before it's filled with
   its final contents, a string:

   * must not be hashed,

   * must not be "converted to UTF-8", or another non-"canonical"
     representation,

   * must not have its reference count changed,

   * must not be shared with code that might do one of the above.

   This list is not exhaustive. Avoiding these uses is your
   responsibility; Python does not always check these requirements.

   To avoid accidentally exposing a partially-written string object,
   prefer using the "PyUnicodeWriter" API, or one of the
   "PyUnicode_From*" functions below.

   Adicionado na versão 3.3.

PyObject *PyUnicode_FromKindAndData(int kind, const void *buffer, Py_ssize_t size)
    *Retorna valor: Nova referência.*

   Cria um novo objeto Unicode com o tipo *type* fornecido (os valores
   possíveis são "PyUnicode_1BYTE_KIND" etc., conforme retornado por
   "PyUnicode_KIND()"). O *buffer* deve apontar para um array de
   unidades com *size* de 1, 2 ou 4 bytes por caractere, conforme
   fornecido pelo tipo.

   If necessary, the input *buffer* is copied and transformed into the
   canonical representation.  For example, if the *buffer* is a UCS4
   string ("PyUnicode_4BYTE_KIND") and it consists only of codepoints
   in the UCS1 range, it will be transformed into UCS1
   ("PyUnicode_1BYTE_KIND").

   All characters must be in range [U+0000; U+10ffff]. If *kind* is
   "PyUnicode_4BYTE_KIND" and the string contains invalid characters,
   the behavior is undefined.

   Adicionado na versão 3.3.

PyObject *PyUnicode_FromStringAndSize(const char *str, Py_ssize_t size)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object from the char buffer *str*.  The bytes will
   be interpreted as being UTF-8 encoded.  The buffer is copied into
   the new object. The return value might be a shared object, i.e.
   modification of the data is not allowed.

   This function raises "SystemError" when:

   * *size* < 0,

   * *str* is "NULL" and *size* > 0

   Alterado na versão 3.12: *str* == "NULL" with *size* > 0 is not
   allowed anymore.

PyObject *PyUnicode_FromString(const char *str)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object from a UTF-8 encoded null-terminated char
   buffer *str*.

PyObject *PyUnicode_FromFormat(const char *format, ...)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Take a C "printf()"-style *format* string and a variable number of
   arguments, calculate the size of the resulting Python Unicode
   string and return a string with the values formatted into it.  The
   variable arguments must be C types and must correspond exactly to
   the format characters in the *format* ASCII-encoded string.

   Um especificador de conversão contém dois ou mais caracteres e tem
   os seguintes componentes, que devem aparecer nesta ordem:

   1. O caractere "'%'", que determina o início do especificador.

   2. Flags de conversão (opcional), que afetam o resultado de alguns
      tipos de conversão.

   3. Minimum field width (optional). If specified as an "'*'"
      (asterisk), the actual width is given in the next argument,
      which must be of type int, and the object to convert comes after
      the minimum field width and optional precision.

   4. Precision (optional), given as a "'.'" (dot) followed by the
      precision. If specified as "'*'" (an asterisk), the actual
      precision is given in the next argument, which must be of type
      int, and the value to convert comes after the precision.

   5. Modificador de comprimento (opcional).

   6. Tipo de conversão.

   Os caracteres flags de conversão são:

   +---------+---------------------------------------------------------------+
   | Sinali  | Significado                                                   |
   | zador   |                                                               |
   |=========|===============================================================|
   | "0"     | A conversão será preenchida por zeros para valores numéricos. |
   +---------+---------------------------------------------------------------+
   | "-"     | The converted value is left adjusted (overrides the "0" flag  |
   |         | if both are given).                                           |
   +---------+---------------------------------------------------------------+

   The length modifiers for following integer conversions ("d", "i",
   "o", "u", "x", or "X") specify the type of the argument (int by
   default):

   +------------+-------------------------------------------------------+
   | Modifier   | Tipos                                                 |
   |============|=======================================================|
   | "l"        | long or unsigned long                                 |
   +------------+-------------------------------------------------------+
   | "ll"       | long long or unsigned long long                       |
   +------------+-------------------------------------------------------+
   | "j"        | "intmax_t" or "uintmax_t"                             |
   +------------+-------------------------------------------------------+
   | "z"        | "size_t" or "ssize_t"                                 |
   +------------+-------------------------------------------------------+
   | "t"        | "ptrdiff_t"                                           |
   +------------+-------------------------------------------------------+

   The length modifier "l" for following conversions "s" or "V"
   specify that the type of the argument is const wchar_t*.

   The conversion specifiers are:

   +-----------------------------------+-----------------------------------+-----------------------------------+
   | Conversion Specifier              | Tipo                              | Comentário                        |
   |===================================|===================================|===================================|
   | "%"                               | *n/d*                             | The literal "%" character.        |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "d", "i"                          | Specified by the length modifier  | The decimal representation of a   |
   |                                   |                                   | signed C integer.                 |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "u"                               | Specified by the length modifier  | The decimal representation of an  |
   |                                   |                                   | unsigned C integer.               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "o"                               | Specified by the length modifier  | The octal representation of an    |
   |                                   |                                   | unsigned C integer.               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "x"                               | Specified by the length modifier  | The hexadecimal representation of |
   |                                   |                                   | an unsigned C integer             |
   |                                   |                                   | (lowercase).                      |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "X"                               | Specified by the length modifier  | The hexadecimal representation of |
   |                                   |                                   | an unsigned C integer             |
   |                                   |                                   | (uppercase).                      |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "c"                               | int                               | A single character.               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "s"                               | const char* or const wchar_t*     | Uma matriz de caracteres C com    |
   |                                   |                                   | terminação nula.                  |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "p"                               | const void*                       | The hex representation of a C     |
   |                                   |                                   | pointer. Mostly equivalent to     |
   |                                   |                                   | "printf("%p")" except that it is  |
   |                                   |                                   | guaranteed to start with the      |
   |                                   |                                   | literal "0x" regardless of what   |
   |                                   |                                   | the platform's "printf" yields.   |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "A"                               | PyObject*                         | The result of calling "ascii()".  |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "U"                               | PyObject*                         | A Unicode object.                 |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "V"                               | PyObject*, const char* or const   | A Unicode object (which may be    |
   |                                   | wchar_t*                          | "NULL") and a null-terminated C   |
   |                                   |                                   | character array as a second       |
   |                                   |                                   | parameter (which will be used, if |
   |                                   |                                   | the first parameter is "NULL").   |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "S"                               | PyObject*                         | The result of calling             |
   |                                   |                                   | "PyObject_Str()".                 |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "R"                               | PyObject*                         | The result of calling             |
   |                                   |                                   | "PyObject_Repr()".                |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "T"                               | PyObject*                         | Get the fully qualified name of   |
   |                                   |                                   | an object type; call              |
   |                                   |                                   | "PyType_GetFullyQualifiedName()". |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "#T"                              | PyObject*                         | Similar to "T" format, but use a  |
   |                                   |                                   | colon (":") as separator between  |
   |                                   |                                   | the module name and the qualified |
   |                                   |                                   | name.                             |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "N"                               | PyTypeObject*                     | Get the fully qualified name of a |
   |                                   |                                   | type; call                        |
   |                                   |                                   | "PyType_GetFullyQualifiedName()". |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | "#N"                              | PyTypeObject*                     | Similar to "N" format, but use a  |
   |                                   |                                   | colon (":") as separator between  |
   |                                   |                                   | the module name and the qualified |
   |                                   |                                   | name.                             |
   +-----------------------------------+-----------------------------------+-----------------------------------+

   Nota:

     The width formatter unit is number of characters rather than
     bytes. The precision formatter unit is number of bytes or
     "wchar_t" items (if the length modifier "l" is used) for ""%s""
     and ""%V"" (if the "PyObject*" argument is "NULL"), and a number
     of characters for ""%A"", ""%U"", ""%S"", ""%R"" and ""%V"" (if
     the "PyObject*" argument is not "NULL").

   Nota:

     Unlike to C "printf()" the "0" flag has effect even when a
     precision is given for integer conversions ("d", "i", "u", "o",
     "x", or "X").

   Alterado na versão 3.2: Suporte adicionado para ""%lld"" e
   ""%llu"".

   Alterado na versão 3.3: Support for ""%li"", ""%lli"" and ""%zi""
   added.

   Alterado na versão 3.4: Support width and precision formatter for
   ""%s"", ""%A"", ""%U"", ""%V"", ""%S"", ""%R"" added.

   Alterado na versão 3.12: Support for conversion specifiers "o" and
   "X". Support for length modifiers "j" and "t". Length modifiers are
   now applied to all integer conversions. Length modifier "l" is now
   applied to conversion specifiers "s" and "V". Support for variable
   width and precision "*". Support for flag "-".An unrecognized
   format character now sets a "SystemError". In previous versions it
   caused all the rest of the format string to be copied as-is to the
   result string, and any extra arguments discarded.

   Alterado na versão 3.13: Support for "%T", "%#T", "%N" and "%#N"
   formats added.

PyObject *PyUnicode_FromFormatV(const char *format, va_list vargs)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Identical to "PyUnicode_FromFormat()" except that it takes exactly
   two arguments.

PyObject *PyUnicode_FromObject(PyObject *obj)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Copy an instance of a Unicode subtype to a new true Unicode object
   if necessary. If *obj* is already a true Unicode object (not a
   subtype), return a new *strong reference* to the object.

   Objects other than Unicode or its subtypes will cause a
   "TypeError".

PyObject *PyUnicode_FromOrdinal(int ordinal)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode Object from the given Unicode code point
   *ordinal*.

   The ordinal must be in "range(0x110000)". A "ValueError" is raised
   in the case it is not.

PyObject *PyUnicode_FromEncodedObject(PyObject *obj, const char *encoding, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Decode an encoded object *obj* to a Unicode object.

   "bytes", "bytearray" and other *bytes-like objects* are decoded
   according to the given *encoding* and using the error handling
   defined by *errors*. Both can be "NULL" to have the interface use
   the default values (see Built-in Codecs for details).

   All other objects, including Unicode objects, cause a "TypeError"
   to be set.

   The API returns "NULL" if there was an error.  The caller is
   responsible for decref'ing the returned objects.

void PyUnicode_Append(PyObject **p_left, PyObject *right)
    * Parte da ABI Estável.*

   Append the string *right* to the end of *p_left*. *p_left* must
   point to a *strong reference* to a Unicode object;
   "PyUnicode_Append()" releases ("*steals*") this reference.

   On error, set **p_left* to "NULL" and set an exception.

   On success, set **p_left* to a new strong reference to the result.

void PyUnicode_AppendAndDel(PyObject **p_left, PyObject *right)
    * Parte da ABI Estável.*

   The function is similar to "PyUnicode_Append()", with the only
   difference being that it decrements the reference count of *right*
   by one.

PyObject *PyUnicode_BuildEncodingMap(PyObject *string)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return a mapping suitable for decoding a custom single-byte
   encoding. Given a Unicode string *string* of up to 256 characters
   representing an encoding table, returns either a compact internal
   mapping object or a dictionary mapping character ordinals to byte
   values. Raises a "TypeError" and return "NULL" on invalid input.

   Adicionado na versão 3.2.

const char *PyUnicode_GetDefaultEncoding(void)
    * Parte da ABI Estável.*

   Return the name of the default string encoding, ""utf-8"". See
   "sys.getdefaultencoding()".

   The returned string does not need to be freed, and is valid until
   interpreter shutdown.

Py_ssize_t PyUnicode_GetLength(PyObject *unicode)
    * Parte da ABI Estável desde a versão 3.7.*

   Return the length of the Unicode object, in code points.

   On error, set an exception and return "-1".

   **Detalhes da implementação do CPython:** The length does not count
   the trailing null character.

   Adicionado na versão 3.3.

Py_ssize_t PyUnicode_CopyCharacters(PyObject *to, Py_ssize_t to_start, PyObject *from, Py_ssize_t from_start, Py_ssize_t how_many)

   Copy characters from one Unicode object into another.  This
   function performs character conversion when necessary and falls
   back to "memcpy()" if possible.  Returns "-1" and sets an exception
   on error, otherwise returns the number of copied characters.

   The string must not have been “used” yet. See "PyUnicode_New()" for
   details.

   Adicionado na versão 3.3.

int PyUnicode_Resize(PyObject **unicode, Py_ssize_t length);
    * Parte da ABI Estável.*

   Resize a Unicode object **unicode* to the new *length* in code
   points.

   Try to resize the string in place (which is usually faster than
   allocating a new string and copying characters), or create a new
   string.

   **unicode* is modified to point to the new (resized) object and "0"
   is returned on success. Otherwise, "-1" is returned and an
   exception is set, and **unicode* is left untouched.

   The function doesn't check string content, the result may not be a
   string in canonical representation.

Py_ssize_t PyUnicode_Fill(PyObject *unicode, Py_ssize_t start, Py_ssize_t length, Py_UCS4 fill_char)

   Fill a string with a character: write *fill_char* into
   "unicode[start:start+length]".

   Fail if *fill_char* is bigger than the string maximum character, or
   if the string has more than 1 reference.

   The string must not have been “used” yet. See "PyUnicode_New()" for
   details.

   Return the number of written characters, or return "-1" and raise
   an exception on error.

   Adicionado na versão 3.3.

int PyUnicode_WriteChar(PyObject *unicode, Py_ssize_t index, Py_UCS4 character)
    * Parte da ABI Estável desde a versão 3.7.*

   Write a *character* to the string *unicode* at the zero-based
   *index*. Return "0" on success, "-1" on error with an exception
   set.

   This function checks that *unicode* is a Unicode object, that the
   index is not out of bounds, and that the object's reference count
   is one. See "PyUnicode_WRITE()" for a version that skips these
   checks, making them your responsibility.

   The string must not have been “used” yet. See "PyUnicode_New()" for
   details.

   Adicionado na versão 3.3.

Py_UCS4 PyUnicode_ReadChar(PyObject *unicode, Py_ssize_t index)
    * Parte da ABI Estável desde a versão 3.7.*

   Read a character from a string.  This function checks that
   *unicode* is a Unicode object and the index is not out of bounds,
   in contrast to "PyUnicode_READ_CHAR()", which performs no error
   checking.

   Return character on success, "-1" on error with an exception set.

   **Detalhes da implementação do CPython:** Do not accept reading the
   trailing null character at index "PyUnicode_GetLength()".

   Adicionado na versão 3.3.

PyObject *PyUnicode_Substring(PyObject *unicode, Py_ssize_t start, Py_ssize_t end)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Return a substring of *unicode*, from character index *start*
   (included) to character index *end* (excluded).  Negative indices
   are not supported. On error, set an exception and return "NULL".

   Adicionado na versão 3.3.

Py_UCS4 *PyUnicode_AsUCS4(PyObject *unicode, Py_UCS4 *buffer, Py_ssize_t buflen, int copy_null)
    * Parte da ABI Estável desde a versão 3.7.*

   Copy the string *unicode* into a UCS4 buffer, including a null
   character, if *copy_null* is set.  Returns "NULL" and sets an
   exception on error (in particular, a "SystemError" if *buflen* is
   smaller than the length of *unicode*).  *buffer* is returned on
   success.

   Adicionado na versão 3.3.

Py_UCS4 *PyUnicode_AsUCS4Copy(PyObject *unicode)
    * Parte da ABI Estável desde a versão 3.7.*

   Copy the string *unicode* into a new UCS4 buffer that is allocated
   using "PyMem_Malloc()".  If this fails, "NULL" is returned with a
   "MemoryError" set.  The returned buffer always has an extra null
   code point appended.

   Adicionado na versão 3.3.


Locale Encoding
---------------

The current locale encoding can be used to decode text from the
operating system.

PyObject *PyUnicode_DecodeLocaleAndSize(const char *str, Py_ssize_t length, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Decode a string from UTF-8 on Android and VxWorks, or from the
   current locale encoding on other platforms. The supported error
   handlers are ""strict"" and ""surrogateescape"" (**PEP 383**). The
   decoder uses ""strict"" error handler if *errors* is "NULL".  *str*
   must end with a null character but cannot contain embedded null
   characters.

   Use "PyUnicode_DecodeFSDefaultAndSize()" to decode a string from
   the *filesystem encoding and error handler*.

   This function ignores the Python UTF-8 Mode.

   Ver também: The "Py_DecodeLocale()" function.

   Adicionado na versão 3.3.

   Alterado na versão 3.7: The function now also uses the current
   locale encoding for the "surrogateescape" error handler, except on
   Android. Previously, "Py_DecodeLocale()" was used for the
   "surrogateescape", and the current locale encoding was used for
   "strict".

PyObject *PyUnicode_DecodeLocale(const char *str, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Similar to "PyUnicode_DecodeLocaleAndSize()", but compute the
   string length using "strlen()".

   Adicionado na versão 3.3.

PyObject *PyUnicode_EncodeLocale(PyObject *unicode, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Encode a Unicode object to UTF-8 on Android and VxWorks, or to the
   current locale encoding on other platforms. The supported error
   handlers are ""strict"" and ""surrogateescape"" (**PEP 383**). The
   encoder uses ""strict"" error handler if *errors* is "NULL". Return
   a "bytes" object. *unicode* cannot contain embedded null
   characters.

   Use "PyUnicode_EncodeFSDefault()" to encode a string to the
   *filesystem encoding and error handler*.

   This function ignores the Python UTF-8 Mode.

   Ver também: The "Py_EncodeLocale()" function.

   Adicionado na versão 3.3.

   Alterado na versão 3.7: The function now also uses the current
   locale encoding for the "surrogateescape" error handler, except on
   Android. Previously, "Py_EncodeLocale()" was used for the
   "surrogateescape", and the current locale encoding was used for
   "strict".


File System Encoding
--------------------

Functions encoding to and decoding from the *filesystem encoding and
error handler* (**PEP 383** and **PEP 529**).

To encode file names to "bytes" during argument parsing, the ""O&""
converter should be used, passing "PyUnicode_FSConverter()" as the
conversion function:

int PyUnicode_FSConverter(PyObject *obj, void *result)
    * Parte da ABI Estável.*

   PyArg_Parse* converter: encode "str" objects -- obtained directly
   or through the "os.PathLike" interface -- to "bytes" using
   "PyUnicode_EncodeFSDefault()"; "bytes" objects are output as-is.
   *result* must be an address of a C variable of type PyObject* (or
   PyBytesObject*). On success, set the variable to a new *strong
   reference* to a bytes object which must be released when it is no
   longer used and return a non-zero value ("Py_CLEANUP_SUPPORTED").
   Embedded null bytes are not allowed in the result. On failure,
   return "0" with an exception set.

   If *obj* is "NULL", the function releases a strong reference stored
   in the variable referred by *result* and returns "1".

   Adicionado na versão 3.1.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

To decode file names to "str" during argument parsing, the ""O&""
converter should be used, passing "PyUnicode_FSDecoder()" as the
conversion function:

int PyUnicode_FSDecoder(PyObject *obj, void *result)
    * Parte da ABI Estável.*

   PyArg_Parse* converter: decode "bytes" objects -- obtained either
   directly or indirectly through the "os.PathLike" interface -- to
   "str" using "PyUnicode_DecodeFSDefaultAndSize()"; "str" objects are
   output as-is. *result* must be an address of a C variable of type
   PyObject* (or PyUnicodeObject*). On success, set the variable to a
   new *strong reference* to a Unicode object which must be released
   when it is no longer used and return a non-zero value
   ("Py_CLEANUP_SUPPORTED"). Embedded null characters are not allowed
   in the result. On failure, return "0" with an exception set.

   If *obj* is "NULL", release the strong reference to the object
   referred to by *result* and return "1".

   Adicionado na versão 3.2.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

PyObject *PyUnicode_DecodeFSDefaultAndSize(const char *str, Py_ssize_t size)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Decode a string from the *filesystem encoding and error handler*.

   If you need to decode a string from the current locale encoding,
   use "PyUnicode_DecodeLocaleAndSize()".

   Ver também: The "Py_DecodeLocale()" function.

   Alterado na versão 3.6: The *filesystem error handler* is now used.

PyObject *PyUnicode_DecodeFSDefault(const char *str)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Decode a null-terminated string from the *filesystem encoding and
   error handler*.

   If the string length is known, use
   "PyUnicode_DecodeFSDefaultAndSize()".

   Alterado na versão 3.6: The *filesystem error handler* is now used.

PyObject *PyUnicode_EncodeFSDefault(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Encode a Unicode object to the *filesystem encoding and error
   handler*, and return "bytes". Note that the resulting "bytes"
   object can contain null bytes.

   If you need to encode a string to the current locale encoding, use
   "PyUnicode_EncodeLocale()".

   Ver também: The "Py_EncodeLocale()" function.

   Adicionado na versão 3.2.

   Alterado na versão 3.6: The *filesystem error handler* is now used.


wchar_t Support
---------------

"wchar_t" support for platforms which support it:

PyObject *PyUnicode_FromWideChar(const wchar_t *wstr, Py_ssize_t size)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object from the "wchar_t" buffer *wstr* of the
   given *size*. Passing "-1" as the *size* indicates that the
   function must itself compute the length, using "wcslen()". Return
   "NULL" on failure.

Py_ssize_t PyUnicode_AsWideChar(PyObject *unicode, wchar_t *wstr, Py_ssize_t size)
    * Parte da ABI Estável.*

   Copy the Unicode object contents into the "wchar_t" buffer *wstr*.
   At most *size* "wchar_t" characters are copied (excluding a
   possibly trailing null termination character).  Return the number
   of "wchar_t" characters copied or "-1" in case of an error.

   When *wstr* is "NULL", instead return the *size* that would be
   required to store all of *unicode* including a terminating null.

   Note that the resulting wchar_t* string may or may not be null-
   terminated.  It is the responsibility of the caller to make sure
   that the wchar_t* string is null-terminated in case this is
   required by the application. Also, note that the wchar_t* string
   might contain null characters, which would cause the string to be
   truncated when used with most C functions.

wchar_t *PyUnicode_AsWideCharString(PyObject *unicode, Py_ssize_t *size)
    * Parte da ABI Estável desde a versão 3.7.*

   Convert the Unicode object to a wide character string. The output
   string always ends with a null character. If *size* is not "NULL",
   write the number of wide characters (excluding the trailing null
   termination character) into **size*. Note that the resulting
   "wchar_t" string might contain null characters, which would cause
   the string to be truncated when used with most C functions. If
   *size* is "NULL" and the wchar_t* string contains null characters a
   "ValueError" is raised.

   Returns a buffer allocated by "PyMem_New" (use "PyMem_Free()" to
   free it) on success. On error, returns "NULL" and **size* is
   undefined. Raises a "MemoryError" if memory allocation is failed.

   Adicionado na versão 3.2.

   Alterado na versão 3.7: Raises a "ValueError" if *size* is "NULL"
   and the wchar_t* string contains null characters.


Built-in Codecs
===============

Python provides a set of built-in codecs which are written in C for
speed. All of these codecs are directly usable via the following
functions.

Many of the following APIs take two arguments encoding and errors, and
they have the same semantics as the ones of the built-in "str()"
string object constructor.

Setting encoding to "NULL" causes the default encoding to be used
which is UTF-8.  The file system calls should use
"PyUnicode_FSConverter()" for encoding file names. This uses the
*filesystem encoding and error handler* internally.

Error handling is set by errors which may also be set to "NULL"
meaning to use the default handling defined for the codec.  Default
error handling for all built-in codecs is "strict" ("ValueError" is
raised).

The codecs all use a similar interface.  Only deviations from the
following generic ones are documented for simplicity.


Generic Codecs
--------------

The following macro is provided:

Py_UNICODE_REPLACEMENT_CHARACTER

   The Unicode code point "U+FFFD" (replacement character).

   This Unicode character is used as the replacement character during
   decoding if the *errors* argument is set to "replace".

These are the generic codec APIs:

PyObject *PyUnicode_Decode(const char *str, Py_ssize_t size, const char *encoding, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object by decoding *size* bytes of the encoded
   string *str*. *encoding* and *errors* have the same meaning as the
   parameters of the same name in the "str()" built-in function.  The
   codec to be used is looked up using the Python codec registry.
   Return "NULL" if an exception was raised by the codec.

PyObject *PyUnicode_AsEncodedString(PyObject *unicode, const char *encoding, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Encode a Unicode object and return the result as Python bytes
   object. *encoding* and *errors* have the same meaning as the
   parameters of the same name in the Unicode "encode()" method. The
   codec to be used is looked up using the Python codec registry.
   Return "NULL" if an exception was raised by the codec.


UTF-8 Codecs
------------

These are the UTF-8 codec APIs:

PyObject *PyUnicode_DecodeUTF8(const char *str, Py_ssize_t size, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object by decoding *size* bytes of the UTF-8
   encoded string *str*. Return "NULL" if an exception was raised by
   the codec.

PyObject *PyUnicode_DecodeUTF8Stateful(const char *str, Py_ssize_t size, const char *errors, Py_ssize_t *consumed)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   If *consumed* is "NULL", behave like "PyUnicode_DecodeUTF8()". If
   *consumed* is not "NULL", trailing incomplete UTF-8 byte sequences
   will not be treated as an error. Those bytes will not be decoded
   and the number of bytes that have been decoded will be stored in
   *consumed*.

PyObject *PyUnicode_AsUTF8String(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Encode a Unicode object using UTF-8 and return the result as Python
   bytes object.  Error handling is "strict".  Return "NULL" if an
   exception was raised by the codec.

   The function fails if the string contains surrogate code points
   ("U+D800" - "U+DFFF").

const char *PyUnicode_AsUTF8AndSize(PyObject *unicode, Py_ssize_t *size)
    * Parte da ABI Estável desde a versão 3.10.*

   Return a pointer to the UTF-8 encoding of the Unicode object, and
   store the size of the encoded representation (in bytes) in *size*.
   The *size* argument can be "NULL"; in this case no size will be
   stored.  The returned buffer always has an extra null byte appended
   (not included in *size*), regardless of whether there are any other
   null code points.

   On error, set an exception, set *size* to "-1" (if it's not NULL)
   and return "NULL".

   The function fails if the string contains surrogate code points
   ("U+D800" - "U+DFFF").

   This caches the UTF-8 representation of the string in the Unicode
   object, and subsequent calls will return a pointer to the same
   buffer.  The caller is not responsible for deallocating the buffer.
   The buffer is deallocated and pointers to it become invalid when
   the Unicode object is garbage collected.

   Adicionado na versão 3.3.

   Alterado na versão 3.7: The return type is now "const char *"
   rather than "char *".

   Alterado na versão 3.10: This function is a part of the limited
   API.

const char *PyUnicode_AsUTF8(PyObject *unicode)

   As "PyUnicode_AsUTF8AndSize()", but does not store the size.

   Aviso:

     This function does not have any special behavior for null
     characters embedded within *unicode*. As a result, strings
     containing null characters will remain in the returned string,
     which some C functions might interpret as the end of the string,
     leading to truncation. If truncation is an issue, it is
     recommended to use "PyUnicode_AsUTF8AndSize()" instead.

   Adicionado na versão 3.3.

   Alterado na versão 3.7: The return type is now "const char *"
   rather than "char *".


UTF-32 Codecs
-------------

These are the UTF-32 codec APIs:

PyObject *PyUnicode_DecodeUTF32(const char *str, Py_ssize_t size, const char *errors, int *byteorder)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Decode *size* bytes from a UTF-32 encoded buffer string and return
   the corresponding Unicode object.  *errors* (if non-"NULL") defines
   the error handling. It defaults to "strict".

   If *byteorder* is non-"NULL", the decoder starts decoding using the
   given byte order:

      *byteorder == -1: little endian
      *byteorder == 0:  native order
      *byteorder == 1:  big endian

   If "*byteorder" is zero, and the first four bytes of the input data
   are a byte order mark (BOM), the decoder switches to this byte
   order and the BOM is not copied into the resulting Unicode string.
   If "*byteorder" is "-1" or "1", any byte order mark is copied to
   the output.

   After completion, **byteorder* is set to the current byte order at
   the end of input data.

   If *byteorder* is "NULL", the codec starts in native order mode.

   Return "NULL" if an exception was raised by the codec.

PyObject *PyUnicode_DecodeUTF32Stateful(const char *str, Py_ssize_t size, const char *errors, int *byteorder, Py_ssize_t *consumed)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   If *consumed* is "NULL", behave like "PyUnicode_DecodeUTF32()". If
   *consumed* is not "NULL", "PyUnicode_DecodeUTF32Stateful()" will
   not treat trailing incomplete UTF-32 byte sequences (such as a
   number of bytes not divisible by four) as an error. Those bytes
   will not be decoded and the number of bytes that have been decoded
   will be stored in *consumed*.

PyObject *PyUnicode_AsUTF32String(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return a Python byte string using the UTF-32 encoding in native
   byte order. The string always starts with a BOM mark.  Error
   handling is "strict". Return "NULL" if an exception was raised by
   the codec.


UTF-16 Codecs
-------------

These are the UTF-16 codec APIs:

PyObject *PyUnicode_DecodeUTF16(const char *str, Py_ssize_t size, const char *errors, int *byteorder)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Decode *size* bytes from a UTF-16 encoded buffer string and return
   the corresponding Unicode object.  *errors* (if non-"NULL") defines
   the error handling. It defaults to "strict".

   If *byteorder* is non-"NULL", the decoder starts decoding using the
   given byte order:

      *byteorder == -1: little endian
      *byteorder == 0:  native order
      *byteorder == 1:  big endian

   If "*byteorder" is zero, and the first two bytes of the input data
   are a byte order mark (BOM), the decoder switches to this byte
   order and the BOM is not copied into the resulting Unicode string.
   If "*byteorder" is "-1" or "1", any byte order mark is copied to
   the output (where it will result in either a "\ufeff" or a "\ufffe"
   character).

   After completion, "*byteorder" is set to the current byte order at
   the end of input data.

   If *byteorder* is "NULL", the codec starts in native order mode.

   Return "NULL" if an exception was raised by the codec.

PyObject *PyUnicode_DecodeUTF16Stateful(const char *str, Py_ssize_t size, const char *errors, int *byteorder, Py_ssize_t *consumed)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   If *consumed* is "NULL", behave like "PyUnicode_DecodeUTF16()". If
   *consumed* is not "NULL", "PyUnicode_DecodeUTF16Stateful()" will
   not treat trailing incomplete UTF-16 byte sequences (such as an odd
   number of bytes or a split surrogate pair) as an error. Those bytes
   will not be decoded and the number of bytes that have been decoded
   will be stored in *consumed*.

PyObject *PyUnicode_AsUTF16String(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return a Python byte string using the UTF-16 encoding in native
   byte order. The string always starts with a BOM mark.  Error
   handling is "strict". Return "NULL" if an exception was raised by
   the codec.


UTF-7 Codecs
------------

These are the UTF-7 codec APIs:

PyObject *PyUnicode_DecodeUTF7(const char *str, Py_ssize_t size, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object by decoding *size* bytes of the UTF-7
   encoded string *str*.  Return "NULL" if an exception was raised by
   the codec.

PyObject *PyUnicode_DecodeUTF7Stateful(const char *str, Py_ssize_t size, const char *errors, Py_ssize_t *consumed)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   If *consumed* is "NULL", behave like "PyUnicode_DecodeUTF7()".  If
   *consumed* is not "NULL", trailing incomplete UTF-7 base-64
   sections will not be treated as an error.  Those bytes will not be
   decoded and the number of bytes that have been decoded will be
   stored in *consumed*.


Unicode-Escape Codecs
---------------------

These are the "Unicode Escape" codec APIs:

PyObject *PyUnicode_DecodeUnicodeEscape(const char *str, Py_ssize_t size, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object by decoding *size* bytes of the Unicode-
   Escape encoded string *str*.  Return "NULL" if an exception was
   raised by the codec.

PyObject *PyUnicode_AsUnicodeEscapeString(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Encode a Unicode object using Unicode-Escape and return the result
   as a bytes object.  Error handling is "strict".  Return "NULL" if
   an exception was raised by the codec.


Raw-Unicode-Escape Codecs
-------------------------

These are the "Raw Unicode Escape" codec APIs:

PyObject *PyUnicode_DecodeRawUnicodeEscape(const char *str, Py_ssize_t size, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object by decoding *size* bytes of the Raw-
   Unicode-Escape encoded string *str*.  Return "NULL" if an exception
   was raised by the codec.

PyObject *PyUnicode_AsRawUnicodeEscapeString(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Encode a Unicode object using Raw-Unicode-Escape and return the
   result as a bytes object.  Error handling is "strict".  Return
   "NULL" if an exception was raised by the codec.


Latin-1 Codecs
--------------

These are the Latin-1 codec APIs: Latin-1 corresponds to the first 256
Unicode ordinals and only these are accepted by the codecs during
encoding.

PyObject *PyUnicode_DecodeLatin1(const char *str, Py_ssize_t size, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object by decoding *size* bytes of the Latin-1
   encoded string *str*.  Return "NULL" if an exception was raised by
   the codec.

PyObject *PyUnicode_AsLatin1String(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Encode a Unicode object using Latin-1 and return the result as
   Python bytes object.  Error handling is "strict".  Return "NULL" if
   an exception was raised by the codec.


ASCII Codecs
------------

These are the ASCII codec APIs.  Only 7-bit ASCII data is accepted.
All other codes generate errors.

PyObject *PyUnicode_DecodeASCII(const char *str, Py_ssize_t size, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object by decoding *size* bytes of the ASCII
   encoded string *str*.  Return "NULL" if an exception was raised by
   the codec.

PyObject *PyUnicode_AsASCIIString(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Encode a Unicode object using ASCII and return the result as Python
   bytes object.  Error handling is "strict".  Return "NULL" if an
   exception was raised by the codec.


Character Map Codecs
--------------------

This codec is special in that it can be used to implement many
different codecs (and this is in fact what was done to obtain most of
the standard codecs included in the "encodings" package). The codec
uses mappings to encode and decode characters.  The mapping objects
provided must support the "__getitem__()" mapping interface;
dictionaries and sequences work well.

These are the mapping codec APIs:

PyObject *PyUnicode_DecodeCharmap(const char *str, Py_ssize_t length, PyObject *mapping, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Create a Unicode object by decoding *size* bytes of the encoded
   string *str* using the given *mapping* object.  Return "NULL" if an
   exception was raised by the codec.

   If *mapping* is "NULL", Latin-1 decoding will be applied.  Else
   *mapping* must map bytes ordinals (integers in the range from 0 to
   255) to Unicode strings, integers (which are then interpreted as
   Unicode ordinals) or "None".  Unmapped data bytes -- ones which
   cause a "LookupError", as well as ones which get mapped to "None",
   "0xFFFE" or "'\ufffe'", are treated as undefined mappings and cause
   an error.

PyObject *PyUnicode_AsCharmapString(PyObject *unicode, PyObject *mapping)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Encode a Unicode object using the given *mapping* object and return
   the result as a bytes object.  Error handling is "strict".  Return
   "NULL" if an exception was raised by the codec.

   The *mapping* object must map Unicode ordinal integers to bytes
   objects, integers in the range from 0 to 255 or "None".  Unmapped
   character ordinals (ones which cause a "LookupError") as well as
   mapped to "None" are treated as "undefined mapping" and cause an
   error.

The following codec API is special in that maps Unicode to Unicode.

PyObject *PyUnicode_Translate(PyObject *unicode, PyObject *table, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Translate a string by applying a character mapping table to it and
   return the resulting Unicode object. Return "NULL" if an exception
   was raised by the codec.

   The mapping table must map Unicode ordinal integers to Unicode
   ordinal integers or "None" (causing deletion of the character).

   Mapping tables need only provide the "__getitem__()" interface;
   dictionaries and sequences work well.  Unmapped character ordinals
   (ones which cause a "LookupError") are left untouched and are
   copied as-is.

   *errors* has the usual meaning for codecs. It may be "NULL" which
   indicates to use the default error handling.


MBCS codecs for Windows
-----------------------

These are the MBCS codec APIs. They are currently only available on
Windows and use the Win32 MBCS converters to implement the
conversions.  Note that MBCS (or DBCS) is a class of encodings, not
just one.  The target encoding is defined by the user settings on the
machine running the codec.

PyObject *PyUnicode_DecodeMBCS(const char *str, Py_ssize_t size, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Create a Unicode object by decoding *size* bytes of the MBCS
   encoded string *str*. Return "NULL" if an exception was raised by
   the codec.

PyObject *PyUnicode_DecodeMBCSStateful(const char *str, Py_ssize_t size, const char *errors, Py_ssize_t *consumed)
    *Retorna valor: Nova referência.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   If *consumed* is "NULL", behave like "PyUnicode_DecodeMBCS()". If
   *consumed* is not "NULL", "PyUnicode_DecodeMBCSStateful()" will not
   decode trailing lead byte and the number of bytes that have been
   decoded will be stored in *consumed*.

PyObject *PyUnicode_DecodeCodePageStateful(int code_page, const char *str, Py_ssize_t size, const char *errors, Py_ssize_t *consumed)
    *Retorna valor: Nova referência.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Similar to "PyUnicode_DecodeMBCSStateful()", except uses the code
   page specified by *code_page*.

PyObject *PyUnicode_AsMBCSString(PyObject *unicode)
    *Retorna valor: Nova referência.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Encode a Unicode object using MBCS and return the result as Python
   bytes object.  Error handling is "strict".  Return "NULL" if an
   exception was raised by the codec.

PyObject *PyUnicode_EncodeCodePage(int code_page, PyObject *unicode, const char *errors)
    *Retorna valor: Nova referência.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Encode the Unicode object using the specified code page and return
   a Python bytes object.  Return "NULL" if an exception was raised by
   the codec. Use "CP_ACP" code page to get the MBCS encoder.

   Adicionado na versão 3.3.


Methods and Slot Functions
==========================

The following APIs are capable of handling Unicode objects and strings
on input (we refer to them as strings in the descriptions) and return
Unicode objects or integers as appropriate.

They all return "NULL" or "-1" if an exception occurs.

PyObject *PyUnicode_Concat(PyObject *left, PyObject *right)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Concat two strings giving a new Unicode string.

PyObject *PyUnicode_Split(PyObject *unicode, PyObject *sep, Py_ssize_t maxsplit)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Split a string giving a list of Unicode strings.  If *sep* is
   "NULL", splitting will be done at all whitespace substrings.
   Otherwise, splits occur at the given separator.  At most *maxsplit*
   splits will be done.  If negative, no limit is set.  Separators are
   not included in the resulting list.

   On error, return "NULL" with an exception set.

   Equivalent to "str.split()".

PyObject *PyUnicode_RSplit(PyObject *unicode, PyObject *sep, Py_ssize_t maxsplit)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Similar to "PyUnicode_Split()", but splitting will be done
   beginning at the end of the string.

   On error, return "NULL" with an exception set.

   Equivalent to "str.rsplit()".

PyObject *PyUnicode_Splitlines(PyObject *unicode, int keepends)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Split a Unicode string at line breaks, returning a list of Unicode
   strings. CRLF is considered to be one line break.  If *keepends* is
   "0", the Line break characters are not included in the resulting
   strings.

PyObject *PyUnicode_Partition(PyObject *unicode, PyObject *sep)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Split a Unicode string at the first occurrence of *sep*, and return
   a 3-tuple containing the part before the separator, the separator
   itself, and the part after the separator. If the separator is not
   found, return a 3-tuple containing the string itself, followed by
   two empty strings.

   *sep* must not be empty.

   On error, return "NULL" with an exception set.

   Equivalent to "str.partition()".

PyObject *PyUnicode_RPartition(PyObject *unicode, PyObject *sep)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Similar to "PyUnicode_Partition()", but split a Unicode string at
   the last occurrence of *sep*. If the separator is not found, return
   a 3-tuple containing two empty strings, followed by the string
   itself.

   *sep* must not be empty.

   On error, return "NULL" with an exception set.

   Equivalent to "str.rpartition()".

PyObject *PyUnicode_Join(PyObject *separator, PyObject *seq)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Join a sequence of strings using the given *separator* and return
   the resulting Unicode string.

Py_ssize_t PyUnicode_Tailmatch(PyObject *unicode, PyObject *substr, Py_ssize_t start, Py_ssize_t end, int direction)
    * Parte da ABI Estável.*

   Return "1" if *substr* matches "unicode[start:end]" at the given
   tail end (*direction* == "-1" means to do a prefix match,
   *direction* == "1" a suffix match), "0" otherwise. Return "-1" if
   an error occurred.

Py_ssize_t PyUnicode_Find(PyObject *unicode, PyObject *substr, Py_ssize_t start, Py_ssize_t end, int direction)
    * Parte da ABI Estável.*

   Return the first position of *substr* in "unicode[start:end]" using
   the given *direction* (*direction* == "1" means to do a forward
   search, *direction* == "-1" a backward search).  The return value
   is the index of the first match; a value of "-1" indicates that no
   match was found, and "-2" indicates that an error occurred and an
   exception has been set.

Py_ssize_t PyUnicode_FindChar(PyObject *unicode, Py_UCS4 ch, Py_ssize_t start, Py_ssize_t end, int direction)
    * Parte da ABI Estável desde a versão 3.7.*

   Return the first position of the character *ch* in
   "unicode[start:end]" using the given *direction* (*direction* ==
   "1" means to do a forward search, *direction* == "-1" a backward
   search).  The return value is the index of the first match; a value
   of "-1" indicates that no match was found, and "-2" indicates that
   an error occurred and an exception has been set.

   Adicionado na versão 3.3.

   Alterado na versão 3.7: *start* and *end* are now adjusted to
   behave like "unicode[start:end]".

Py_ssize_t PyUnicode_Count(PyObject *unicode, PyObject *substr, Py_ssize_t start, Py_ssize_t end)
    * Parte da ABI Estável.*

   Return the number of non-overlapping occurrences of *substr* in
   "unicode[start:end]".  Return "-1" if an error occurred.

PyObject *PyUnicode_Replace(PyObject *unicode, PyObject *substr, PyObject *replstr, Py_ssize_t maxcount)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Replace at most *maxcount* occurrences of *substr* in *unicode*
   with *replstr* and return the resulting Unicode object. *maxcount*
   == "-1" means replace all occurrences.

int PyUnicode_Compare(PyObject *left, PyObject *right)
    * Parte da ABI Estável.*

   Compare two strings and return "-1", "0", "1" for less than, equal,
   and greater than, respectively.

   This function returns "-1" upon failure, so one should call
   "PyErr_Occurred()" to check for errors.

   Ver também: The "PyUnicode_Equal()" function.

int PyUnicode_Equal(PyObject *a, PyObject *b)
    * Parte da ABI Estável desde a versão 3.14.*

   Test if two strings are equal:

   * Return "1" if *a* is equal to *b*.

   * Return "0" if *a* is not equal to *b*.

   * Set a "TypeError" exception and return "-1" if *a* or *b* is not
     a "str" object.

   The function always succeeds if *a* and *b* are "str" objects.

   The function works for "str" subclasses, but does not honor custom
   "__eq__()" method.

   Ver também: The "PyUnicode_Compare()" function.

   Adicionado na versão 3.14.

int PyUnicode_EqualToUTF8AndSize(PyObject *unicode, const char *string, Py_ssize_t size)
    * Parte da ABI Estável desde a versão 3.13.*

   Compare a Unicode object with a char buffer which is interpreted as
   being UTF-8 or ASCII encoded and return true ("1") if they are
   equal, or false ("0") otherwise. If the Unicode object contains
   surrogate code points ("U+D800" - "U+DFFF") or the C string is not
   valid UTF-8, false ("0") is returned.

   This function does not raise exceptions.

   Adicionado na versão 3.13.

int PyUnicode_EqualToUTF8(PyObject *unicode, const char *string)
    * Parte da ABI Estável desde a versão 3.13.*

   Similar to "PyUnicode_EqualToUTF8AndSize()", but compute *string*
   length using "strlen()". If the Unicode object contains null
   characters, false ("0") is returned.

   Adicionado na versão 3.13.

int PyUnicode_CompareWithASCIIString(PyObject *unicode, const char *string)
    * Parte da ABI Estável.*

   Compare a Unicode object, *unicode*, with *string* and return "-1",
   "0", "1" for less than, equal, and greater than, respectively. It
   is best to pass only ASCII-encoded strings, but the function
   interprets the input string as ISO-8859-1 if it contains non-ASCII
   characters.

   This function does not raise exceptions.

PyObject *PyUnicode_RichCompare(PyObject *left, PyObject *right, int op)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Rich compare two Unicode strings and return one of the following:

   * "NULL" in case an exception was raised

   * "Py_True" or "Py_False" for successful comparisons

   * "Py_NotImplemented" in case the type combination is unknown

   Possible values for *op* are "Py_GT", "Py_GE", "Py_EQ", "Py_NE",
   "Py_LT", and "Py_LE".

PyObject *PyUnicode_Format(PyObject *format, PyObject *args)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return a new string object from *format* and *args*; this is
   analogous to "format % args".

int PyUnicode_Contains(PyObject *unicode, PyObject *substr)
    * Parte da ABI Estável.*

   Check whether *substr* is contained in *unicode* and return true or
   false accordingly.

   *substr* has to coerce to a one element Unicode string. "-1" is
   returned if there was an error.

void PyUnicode_InternInPlace(PyObject **p_unicode)
    * Parte da ABI Estável.*

   Intern the argument *p_unicode in place.  The argument must be the
   address of a pointer variable pointing to a Python Unicode string
   object.  If there is an existing interned string that is the same
   as *p_unicode, it sets *p_unicode to it (releasing the reference to
   the old string object and creating a new *strong reference* to the
   interned string object), otherwise it leaves *p_unicode alone and
   interns it.

   (Clarification: even though there is a lot of talk about
   references, think of this function as reference-neutral. You must
   own the object you pass in; after the call you no longer own the
   passed-in reference, but you newly own the result.)

   This function never raises an exception. On error, it leaves its
   argument unchanged without interning it.

   Instances of subclasses of "str" may not be interned, that is,
   PyUnicode_CheckExact(*p_unicode) must be true. If it is not, then
   -- as with any other error -- the argument is left unchanged.

   Note that interned strings are not “immortal”. You must keep a
   reference to the result to benefit from interning.

PyObject *PyUnicode_InternFromString(const char *str)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   A combination of "PyUnicode_FromString()" and
   "PyUnicode_InternInPlace()", meant for statically allocated
   strings.

   Return a new ("owned") reference to either a new Unicode string
   object that has been interned, or an earlier interned string object
   with the same value.

   Python may keep a reference to the result, or make it *immortal*,
   preventing it from being garbage-collected promptly. For interning
   an unbounded number of different strings, such as ones coming from
   user input, prefer calling "PyUnicode_FromString()" and
   "PyUnicode_InternInPlace()" directly.

unsigned int PyUnicode_CHECK_INTERNED(PyObject *str)

   Return a non-zero value if *str* is interned, zero if not. The
   *str* argument must be a string; this is not checked. This function
   always succeeds.

   **Detalhes da implementação do CPython:** A non-zero return value
   may carry additional information about *how* the string is
   interned. The meaning of such non-zero values, as well as each
   specific string's intern-related details, may change between
   CPython versions.


PyUnicodeWriter
===============

The "PyUnicodeWriter" API can be used to create a Python "str" object.

Adicionado na versão 3.14.

type PyUnicodeWriter

   A Unicode writer instance.

   The instance must be destroyed by "PyUnicodeWriter_Finish()" on
   success, or "PyUnicodeWriter_Discard()" on error.

   The API is **not thread safe**. To share a writer with multiple
   threads, a critical section or a lock is needed.

PyUnicodeWriter *PyUnicodeWriter_Create(Py_ssize_t length)

   Create a Unicode writer instance.

   *length* must be greater than or equal to "0".

   If *length* is greater than "0", preallocate an internal buffer of
   *length* characters.

   Define uma exceção e retorna "NULL" em caso de erro.

PyObject *PyUnicodeWriter_Finish(PyUnicodeWriter *writer)

   Return the final Python "str" object and destroy the writer
   instance.

   Define uma exceção e retorna "NULL" em caso de erro.

   The writer instance is invalid after this call.

void PyUnicodeWriter_Discard(PyUnicodeWriter *writer)

   Discard the internal Unicode buffer and destroy the writer
   instance.

   If *writer* is "NULL", no operation is performed.

   The writer instance is invalid after this call.

int PyUnicodeWriter_WriteChar(PyUnicodeWriter *writer, Py_UCS4 ch)

   Write the single Unicode character *ch* into *writer*.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_WriteUTF8(PyUnicodeWriter *writer, const char *str, Py_ssize_t size)

   Decode the string *str* from UTF-8 in strict mode and write the
   output into *writer*.

   *size* is the string length in bytes. If *size* is equal to "-1",
   call "strlen(str)" to get the string length.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

   See also "PyUnicodeWriter_DecodeUTF8Stateful()".

int PyUnicodeWriter_WriteASCII(PyUnicodeWriter *writer, const char *str, Py_ssize_t size)

   Write the ASCII string *str* into *writer*.

   *size* is the string length in bytes. If *size* is equal to "-1",
   call "strlen(str)" to get the string length.

   *str* must only contain ASCII characters. The behavior is undefined
   if *str* contains non-ASCII characters.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_WriteWideChar(PyUnicodeWriter *writer, const wchar_t *str, Py_ssize_t size)

   Write the wide string *str* into *writer*.

   *size* is a number of wide characters. If *size* is equal to "-1",
   call "wcslen(str)" to get the string length.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_WriteUCS4(PyUnicodeWriter *writer, const Py_UCS4 *str, Py_ssize_t size)

   Write the UCS4 string *str* into *writer*.

   *size* is a number of UCS4 characters.

   All characters must be in range [U+0000; U+10ffff]. If the string
   contains invalid characters, the behavior is undefined.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_WriteStr(PyUnicodeWriter *writer, PyObject *obj)

   Call "PyObject_Str()" on *obj* and write the output into *writer*.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

   To write a "str" subclass which overrides the "__str__()" method,
   "PyUnicode_FromObject()" can be used to get the original string.

int PyUnicodeWriter_WriteRepr(PyUnicodeWriter *writer, PyObject *obj)

   Call "PyObject_Repr()" on *obj* and write the output into *writer*.

   If *obj* is "NULL", write the string ""<NULL>"" into *writer*.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

   Alterado na versão 3.14.4: Added support for "NULL".

int PyUnicodeWriter_WriteSubstring(PyUnicodeWriter *writer, PyObject *str, Py_ssize_t start, Py_ssize_t end)

   Write the substring "str[start:end]" into *writer*.

   *str* must be Python "str" object. *start* must be greater than or
   equal to 0, and less than or equal to *end*. *end* must be less
   than or equal to *str* length.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_Format(PyUnicodeWriter *writer, const char *format, ...)

   Similar to "PyUnicode_FromFormat()", but write the output directly
   into *writer*.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

int PyUnicodeWriter_DecodeUTF8Stateful(PyUnicodeWriter *writer, const char *string, Py_ssize_t length, const char *errors, Py_ssize_t *consumed)

   Decode the string *str* from UTF-8 with *errors* error handler and
   write the output into *writer*.

   *size* is the string length in bytes. If *size* is equal to "-1",
   call "strlen(str)" to get the string length.

   *errors* is an error handler name, such as ""replace"". If *errors*
   is "NULL", use the strict error handler.

   If *consumed* is not "NULL", set **consumed* to the number of
   decoded bytes on success. If *consumed* is "NULL", treat trailing
   incomplete UTF-8 byte sequences as an error.

   On success, return "0". On error, set an exception, leave the
   writer unchanged, and return "-1".

   See also "PyUnicodeWriter_WriteUTF8()".


Deprecated API
==============

The following API is deprecated.

type Py_UNICODE

   This is a typedef of "wchar_t", which is a 16-bit type or 32-bit
   type depending on the platform. Please use "wchar_t" directly
   instead.

   Alterado na versão 3.3: Em versões anteriores, esse era um tipo de
   16 bits ou de 32 bits, dependendo se você selecionava uma versão
   Unicode "estreita" ou "ampla" do Python no momento da construção.

   Descontinuado desde a versão 3.13, removido na versão 3.15.

int PyUnicode_READY(PyObject *unicode)

   Do nothing and return "0". This API is kept only for backward
   compatibility, but there are no plans to remove it.

   Adicionado na versão 3.3.

   Descontinuado desde a versão 3.10: This API does nothing since
   Python 3.12. Previously, this needed to be called for each string
   created using the old API ("PyUnicode_FromUnicode()" or similar).

unsigned int PyUnicode_IS_READY(PyObject *unicode)

   Do nothing and return "1". This API is kept only for backward
   compatibility, but there are no plans to remove it.

   Adicionado na versão 3.3.

   Descontinuado desde a versão 3.14: This API does nothing since
   Python 3.12. Previously, this could be called to check if
   "PyUnicode_READY()" is necessary.
