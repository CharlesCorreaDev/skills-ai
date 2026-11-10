Objetos números complexos
*************************

type PyComplexObject

   Este subtipo de "PyObject" representa um objeto Python de número
   complexo.

   Py_complex cval

      The complex number value, using the C "Py_complex"
      representation.

      Descontinuado desde a versão 3.15, será removido na versão 3.20:
      Use "PyComplex_AsCComplex()" and "PyComplex_FromCComplex()" to
      convert a Python complex number to/from the C "Py_complex"
      representation.

PyTypeObject PyComplex_Type
    * Parte da ABI Estável.*

   Esta instância de "PyTypeObject" representa o tipo de número
   complexo Python. É o mesmo objeto que "complex" na camada Python.

int PyComplex_Check(PyObject *p)

   Retorna true se seu argumento é um "PyComplexObject" ou um subtipo
   de "PyComplexObject". Esta função sempre tem sucesso.

int PyComplex_CheckExact(PyObject *p)

   Retorna true se seu argumento é um "PyComplexObject", mas não um
   subtipo de "PyComplexObject". Esta função sempre tem sucesso.

PyObject *PyComplex_FromDoubles(double real, double imag)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo objeto "PyComplexObject" de *real* e *imag*.
   Retorna "NULL" com uma exceção definida ao ocorrer um erro.

double PyComplex_RealAsDouble(PyObject *op)
    * Parte da ABI Estável.*

   Retorna a parte real de *op* como um double C.

   Se *op* não é um objeto de número complexo Python, mas tem um
   método "__complex__()", este método será primeiro chamado para
   converter *op* em um objeto de número complexo Python. Se
   "__complex__()" não estiver definido, ele volta a chamar
   "PyFloat_AsDouble()" e retorna seu resultado.

   Em caso de falha, este método retorna "-1.0" com uma exceção
   definida, então deve-se chamar "PyErr_Occurred()" para verificar se
   há erros.

   Alterado na versão 3.13: Usa "__complex__()", se disponível.

double PyComplex_ImagAsDouble(PyObject *op)
    * Parte da ABI Estável.*

   Retorna a parte imaginária de *op* como um double C.

   Se *op* não é um objeto de número complexo Python, mas tem um
   método "__complex__()", este método será primeiro chamado para
   converter *op* em um objeto de número complexo Python. Se
   "__complex__()" não estiver definido, ele volta a chamar
   "PyFloat_AsDouble()" e retorna "0.0" em caso de sucesso.

   Em caso de falha, este método retorna "-1.0" com uma exceção
   definida, então deve-se chamar "PyErr_Occurred()" para verificar se
   há erros.

   Alterado na versão 3.13: Usa "__complex__()", se disponível.

type Py_complex

   This C structure defines an export format for a Python complex
   number object.

   double real
   double imag

   A estrutura é definida como:

      typedef struct {
          double real;
          double imag;
      } Py_complex;

PyObject *PyComplex_FromCComplex(Py_complex v)
    *Retorna valor: Nova referência.*

   Cria um novo objeto de número complexo Python a partir de um valor
   C "Py_complex". Retorna "NULL" com uma exceção definida ao ocorrer
   um erro.

Py_complex PyComplex_AsCComplex(PyObject *op)

   Retorna o valor "Py_complex" do número complexo *op*.

   Se *op* não é um objeto de número complexo Python, mas tem um
   método "__complex__()", este método será primeiro chamado para
   converter *op* em um objeto de número complexo Python. Se
   "__complex__()" não for definido, então ele recorre a
   "__float__()". Se "__float__()" não estiver definido, então ele
   volta para "__index__()".

   Em caso de falha, este método retorna "Py_complex" com "real"
   definido para "-1.0" e com uma exceção definida, então deve-se
   chamar "PyErr_Occurred()" para verificar se há erros.

   Alterado na versão 3.8: Usa "__index__()", se disponível.


Números complexos como estruturas C.
====================================

The API also provides functions for working with complex numbers,
using the "Py_complex" representation.  Note that the functions which
accept these structures as parameters and return them as results do so
*by value* rather than dereferencing them through pointers.

Please note, that these functions are *soft deprecated* since Python
3.15.  Avoid using this API in a new code to do complex arithmetic:
either use the Number Protocol API or use native complex types, like
double complex.

Py_complex _Py_c_sum(Py_complex left, Py_complex right)

   Retorna a soma de dois números complexos, utilizando a
   representação C "Py_complex".

   Descontinuado desde a versão 3.15.

Py_complex _Py_c_diff(Py_complex left, Py_complex right)

   Retorna a diferença entre dois números complexos, utilizando a
   representação C "Py_complex".

   Descontinuado desde a versão 3.15.

Py_complex _Py_c_neg(Py_complex num)

   Retorna a negação do número complexo *num*, utilizando a
   representação C "Py_complex".

   Descontinuado desde a versão 3.15.

Py_complex _Py_c_prod(Py_complex left, Py_complex right)

   Retorna o produto de dois números complexos, utilizando a
   representação C "Py_complex".

   Descontinuado desde a versão 3.15.

Py_complex _Py_c_quot(Py_complex dividend, Py_complex divisor)

   Retorna o quociente de dois números complexos, utilizando a
   representação C "Py_complex".

   Se *divisor* é nulo, este método retorna zero e define "errno" para
   "EDOM".

   Descontinuado desde a versão 3.15.

Py_complex _Py_c_pow(Py_complex num, Py_complex exp)

   Retorna a exponenciação de *num* por *exp*, utilizando a
   representação C "Py_complex"

   Se *num* for nulo e *exp* não for um número real positivo, este
   método retorna zero e define "errno" para "EDOM".

   Define "errno" para "ERANGE" em caso de estouros.

   Descontinuado desde a versão 3.15.

double _Py_c_abs(Py_complex num)

   Return the absolute value of the complex number *num*.

   Define "errno" para "ERANGE" em caso de estouros.

   Descontinuado desde a versão 3.15.
