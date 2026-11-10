Objetos de ponto flutuante
**************************

type PyFloatObject

   Este subtipo de "PyObject" representa um objeto de ponto flutuante
   do Python.

PyTypeObject PyFloat_Type
    * Parte da ABI Estável.*

   Esta instância do "PyTypeObject" representa o tipo de ponto
   flutuante do Python. Este é o mesmo objeto "float" na camada do
   Python.

int PyFloat_Check(PyObject *p)

   Retorna true se seu argumento é um "PyFloatObject" ou um subtipo de
   "PyFloatObject". Esta função sempre tem sucesso.

int PyFloat_CheckExact(PyObject *p)

   Retorna true se seu argumento é um "PyFloatObject", mas um subtipo
   de "PyFloatObject". Esta função sempre tem sucesso.

PyObject *PyFloat_FromString(PyObject *str)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Cria um objeto "PyFloatObject" baseado em uma string de valor "str"
   ou "NULL" em falha.

PyObject *PyFloat_FromDouble(double v)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Cria um objeto "PyFloatObject" de *v* ou "NULL" em falha.

double PyFloat_AsDouble(PyObject *pyfloat)
    * Parte da ABI Estável.*

   Retorna uma representação C double do conteúdo de *pyfloat*. Se
   *pyfloat* não é um objeto de ponto flutuante do Python, mas possui
   o método "__float__()", esse método será chamado primeiro para
   converter *pyfloat* em um ponto flutuante. Se "__float__()" não
   estiver definido, será usado "__index__()". Este método retorna
   "-1.0" em caso de falha, portanto, deve-se chamar
   "PyErr_Occurred()" para verificar se há erros.

   Alterado na versão 3.8: Usa "__index__()", se disponível.

double PyFloat_AS_DOUBLE(PyObject *pyfloat)

   Retorna uma representação C double do conteúdo de *pyfloat*, mas
   sem verificação de erro.

PyObject *PyFloat_GetInfo(void)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna uma instância de structseq que contém informações sobre a
   precisão, os valores mínimo e máximo de um ponto flutuante. É um
   invólucro fino em torno do arquivo de cabeçalho "float.h".

double PyFloat_GetMax()
    * Parte da ABI Estável.*

   Retorna o ponto flutuante finito máximo representável *DBL_MAX*
   como double do C.

double PyFloat_GetMin()
    * Parte da ABI Estável.*

   Retorna o ponto flutuante positivo mínimo normalizado *DBL_MIN*
   como double do C.

Py_INFINITY

   This macro expands to a constant expression of type double, that
   represents the positive infinity.

   It is equivalent to the "INFINITY" macro from the C11 standard
   "<math.h>" header.

   Suavemente descontinuado desde a versão 3.15.

Py_NAN

   This macro expands to a constant expression of type double, that
   represents a quiet not-a-number (qNaN) value.

   Na maioria das plataformas, isso equivale à macro "NAN" do
   cabeçalho "<math.h>" do padrão C11.

Py_HUGE_VAL

   Equivalente a "INFINITY".

   Suavemente descontinuado desde a versão 3.14.

Py_MATH_E

   A definição (precisa para um tipo double) da constante "math.e".

Py_MATH_El

   Definição de alta precisão (long double) da constante "e".

   Descontinuado desde a versão 3.15, será removido na versão 3.20.

Py_MATH_PI

   A definição (precisa para um tipo double) da constante "math.pi".

Py_MATH_PIl

   Definição de alta precisão (long double) da constante "pi".

   Descontinuado desde a versão 3.15, será removido na versão 3.20.

Py_MATH_TAU

   A definição (precisa para um tipo double) da constante "math.tau".

   Adicionado na versão 3.6.

Py_RETURN_NAN

   Retorna "math.nan" de uma função.

   Na maioria das plataformas, isso equivale a "return
   PyFloat_FromDouble(NAN)".

Py_RETURN_INF(sign)

   Retorna "math.inf" ou "-math.inf" de uma função, dependendo do
   sinal de *sign*.

   Na maioria das plataformas, isso equivale ao seguinte:

      return PyFloat_FromDouble(copysign(INFINITY, sign));

Py_IS_FINITE(X)

   Retorna "1" se o número de ponto flutuante *X* fornecido for
   finito, ou seja, for normal, subnormal ou zero, mas não infinito ou
   NaN. Caso contrário, retorna "0".

   Suavemente descontinuado desde a versão 3.14: Use "isfinite"
   instead.

Py_IS_INFINITY(X)

   Retorna "1" se o número de ponto flutuante *X* fornecido for
   infinito positivo ou negativo. Caso contrário, retorna "0".

   Suavemente descontinuado desde a versão 3.14: Use "isinf" instead.

Py_IS_NAN(X)

   Retorna "1" se o número de ponto flutuante fornecido *X* for um
   valor não numérico (NaN). Caso contrário, retorna "0".

   Suavemente descontinuado desde a versão 3.14: Use "isnan" instead.


As funções Pack e Unpack
========================

The pack and unpack functions provide an efficient platform-
independent way to store floating-point values as byte strings. The
Pack routines produce a bytes string from a C double, and the Unpack
routines produce a C double from such a bytes string. The suffix (2, 4
or 8) specifies the number of bytes in the bytes string:

* The 2-byte format is the IEEE 754 binary16 half-precision format.

* The 4-byte format is the IEEE 754 binary32 single-precision format.

* The 8-byte format is the IEEE 754 binary64 double-precision format.

The NaN type may not be preserved on some platforms while unpacking
(signaling NaNs become quiet NaNs), for example on x86 systems in
32-bit mode.

It's assumed that the double type has the IEEE 754 binary64 double
precision format.  What happens if it's not true is partly accidental
(alas). On non-IEEE platforms with more precision, or larger dynamic
range, than IEEE 754 supports, not all values can be packed; on non-
IEEE platforms with less precision, or smaller dynamic range, not all
values can be unpacked.  The packing of special numbers like INFs and
NaNs (if such things exist on the platform) may not be handled
correctly, and attempting to unpack a bytes string containing an IEEE
INF or NaN may raise an exception.

Adicionado na versão 3.11.


Funções Pack
------------

The pack routines write 2, 4 or 8 bytes, starting at *p*. *le* is an
int argument, non-zero if you want the bytes string in little-endian
format (exponent last, at "p+1", "p+3", or "p+6" and "p+7"), zero if
you want big-endian format (exponent first, at *p*). Use the
"PY_LITTLE_ENDIAN" constant to select the native endian: it is equal
to "0" on big endian processor, or "1" on little endian processor.

Valor de retorno: "0" se tudo estiver OK, "-1" se houver erro (e uma
exceção for definida, provavelmente "OverflowError").

int PyFloat_Pack2(double x, char *p, int le)

   Empacota um C duplo como o formato de meia precisão binário16 IEEE
   754.

int PyFloat_Pack4(double x, char *p, int le)

   Empacota um C duplo como o formato de precisão simples binário32
   IEEE 754.

int PyFloat_Pack8(double x, char *p, int le)

   Empacota um C duplo como o formato de precisão dupla binária 64
   IEEE 754.


Funções de Unpack
-----------------

The unpack routines read 2, 4 or 8 bytes, starting at *p*.  *le* is an
int argument, non-zero if the bytes string is in little-endian format
(exponent last, at "p+1", "p+3" or "p+6" and "p+7"), zero if big-
endian (exponent first, at *p*). Use the "PY_LITTLE_ENDIAN" constant
to select the native endian: it is equal to "0" on big endian
processor, or "1" on little endian processor.

Valor de retorno: O double descompactado. Em caso de erro, é "-1.0" e
"PyErr_Occurred()" é verdadeiro (e uma exceção é definida,
provavelmente "OverflowError").

double PyFloat_Unpack2(const char *p, int le)

   Descompacta o formato de meia precisão IEEE 754 binary16 como um
   double C.

double PyFloat_Unpack4(const char *p, int le)

   Descompacta o formato IEEE 754 binary32 de precisão simples como um
   C double.

double PyFloat_Unpack8(const char *p, int le)

   Descompacta o formato IEEE 754 binary64 de precisão dupla como um C
   double.
