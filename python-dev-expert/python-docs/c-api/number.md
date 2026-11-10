Protocolo de número
*******************

int PyNumber_Check(PyObject *o)
    * Parte da ABI Estável.*

   Retorna "1" se o objeto *o* fornece protocolos numéricos; caso
   contrário, retorna falso. Esta função sempre tem sucesso.

   Alterado na versão 3.8: Retorna "1" se *o* for um número inteiro de
   índice.

PyObject *PyNumber_Add(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado da adição de *o1* e *o2*, ou "NULL" em caso de
   falha. Este é o equivalente da expressão Python "o1 + o2".

PyObject *PyNumber_Subtract(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado da subtração de *o2* por *o1*, ou "NULL" em
   caso de falha. Este é o equivalente da expressão Python "o1 - o2".

PyObject *PyNumber_Multiply(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado da multiplicação de *o1* e *o2*, ou "NULL" em
   caso de falha. Este é o equivalente da expressão Python "o1 * o2".

PyObject *PyNumber_MatrixMultiply(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Retorna o resultado da multiplicação da matriz em *o1* e *o2*, ou
   "NULL" em caso de falha. Este é o equivalente da expressão Python
   "o1 @ o2".

   Adicionado na versão 3.5.

PyObject *PyNumber_FloorDivide(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o piso de *o1* dividido por *o2* ou "NULL" em caso de
   falha. Isso é equivalente à expressão Python "o1 // o2".

PyObject *PyNumber_TrueDivide(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna uma aproximação razoável para o valor matemático de *o1*
   dividido por *o2*, ou "NULL" em caso de falha. O valor devolvido é
   "aproximado" porque os números binários de ponto flutuante são
   aproximados; não é possível representar todos os números reais na
   base dois. Esta função pode devolver um valor de ponto flutuante
   quando lhe são passados dois inteiros. Isso é o equivalente à
   expressão Python "o1 / o2".

PyObject *PyNumber_Remainder(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resto da divisão de *o1* por *o2* ou "NULL" em caso de
   falha. Isso é equivalente à expressão Python "o1 % o2".

PyObject *PyNumber_Divmod(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Consulte a função embutida "divmod()". Retorna "NULL" em caso de
   falha. Isso é equivalente à expressão Python "divmod(o1, o2)".

PyObject *PyNumber_Power(PyObject *o1, PyObject *o2, PyObject *o3)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Consulte a função embutida "pow()". Retorna "NULL" em caso de
   falha. Isso é equivalente à expressão Python "pow(o1, o2, o3)", na
   qual *o3* é opcional. Se *o3* deve ser ignorado, passe "Py_None" em
   seu lugar (passar "NULL" para *o3* causaria um acesso ilegal à
   memória).

PyObject *PyNumber_Negative(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna a negação de *o* em caso de sucesso ou "NULL" em caso de
   falha. Isso é equivalente à expressão Python "-o".

PyObject *PyNumber_Positive(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna *o* em caso de sucesso ou "NULL" em caso de falha. Isso é
   equivalente à expressão Python "+o".

PyObject *PyNumber_Absolute(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o valor absoluto de *o* ou "NULL" em caso de falha. Isso é
   equivalente à expressão Python "abs(o)".

PyObject *PyNumber_Invert(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna a negação bit a bit de *o* em caso de sucesso, ou "NULL" em
   caso de falha. Isso é equivalente à expressão Python "~o".

PyObject *PyNumber_Lshift(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado do deslocamento à esquerda de *o1* por *o2* em
   caso de sucesso ou "NULL" em caso de falha. Isso é equivalente à
   expressão Python "o1 << o2".

PyObject *PyNumber_Rshift(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado do deslocamento à direita de *o1* por *o2* em
   caso de sucesso ou "NULL" em caso de falha. Isso é equivalente à
   expressão Python "o1 >> o2".

PyObject *PyNumber_And(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o bit a bit "e" de *o1* e *o2* em caso de sucesso e "NULL"
   em caso de falha. Isso é equivalente à expressão Python "o1 & o2".

PyObject *PyNumber_Xor(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o bit a bit "ou exclusivo" de *o1* por *o2* em caso de
   sucesso ou "NULL" em caso de falha. Isso é equivalente à expressão
   Python "o1 ^ o2".

PyObject *PyNumber_Or(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o bit a bit "ou" de *o1* e *o2* em caso de sucesso ou
   "NULL" em caso de falha. Isto é equivalente à expressão Python "o1
   | o2".

PyObject *PyNumber_InPlaceAdd(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado da adição de *o1* e *o2* ou "NULL" em caso de
   falha. A operação é feita *no local* quando *o1* dá suporte a isso.
   Isto é equivalente à instrução Python "o1 += o2".

PyObject *PyNumber_InPlaceSubtract(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado da subtração de *o2* de *o1* ou "NULL" em caso
   de falha. A operação é feita *no local* quando *o1*  dá suporte a
   isso. Isto é equivalente à instrução Python "o1 -= o2".

PyObject *PyNumber_InPlaceMultiply(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado da multiplicação de *o1* e *o2* ou "NULL" em
   caso de falha. A operação é feita *no local* quando *o1* dá suporte
   a isso. Isto é equivalente à instrução Python "o1 *= o2".

PyObject *PyNumber_InPlaceMatrixMultiply(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.7.*

   Retorna o resultado da multiplicação de matrizes entre *o1* e *o2*,
   ou "NULL" em caso de falha. A operação é realizada no local quando
   *o1* oferece suporte a isso. Isso é equivalente à instrução Python
   "o1 @= o2".

   Adicionado na versão 3.5.

PyObject *PyNumber_InPlaceFloorDivide(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o valor matemático mínimo da divisão de *o1* por *o2* ou
   "NULL" em caso de falha. A operação é feita *no local* quando *o1*
   dá suporte a isso. Isto é equivalente à instrução Python "o1 //=
   o2".

PyObject *PyNumber_InPlaceTrueDivide(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna uma aproximação razoável para o valor matemático de *o1*
   dividido por *o2*, ou "NULL" em caso de falha. O valor de retorno é
   "aproximado" porque os números binários de ponto flutuante são
   aproximados; não é possível representar todos os números reais na
   base dois. Esta função pode retornar um valor de ponto flutuante
   quando lhe são passados dois inteiros. A operação é feita no local
   quando *o1* oferece suporte a isso. Isso é o equivalente à
   instrução Python "o1 /= o2".

PyObject *PyNumber_InPlaceRemainder(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resto da divisão de *o1* por *o2* ou "NULL" em caso de
   falha. A operação é feita *no local* quando *o1* dá suporte a isso.
   Isto é equivalente à instrução Python "o1 %= o2".

PyObject *PyNumber_InPlacePower(PyObject *o1, PyObject *o2, PyObject *o3)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Consulte a função embutida "pow()". Retorna "NULL" em caso de
   falha. A operação é feita no lugar quando *o1* oferece suporte a
   isso. Isso é equivalente à instrução Python "o1 **= o2" quando o3 é
   "Py_None" ou, do contrário, uma variante no local "pow(o1, o2,
   o3)". Se *o3* deve ser ignorado, passe "Py_None" em seu lugar
   (passar "NULL" para *o3* causaria um acesso ilegal à memória).

PyObject *PyNumber_InPlaceLshift(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado do deslocamento à esquerda de *o1* por *o2* em
   caso de sucesso, ou "NULL" em caso de falha. A operação é feita no
   local quando *o1* oferece suporte a isso. Isto é equivalente à
   instrução Python "o1 <<= o2".

PyObject *PyNumber_InPlaceRshift(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado do deslocamento à direita de *o1* por *o2* em
   caso de sucesso, ou "NULL" em caso de falha. A operação é feita no
   local quando *o1* oferece suporte a isso. Isto é equivalente à
   instrução Python "o1 >>= o2".

PyObject *PyNumber_InPlaceAnd(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o "bitwise and" de *o1* e *o2* em caso de sucesso e "NULL"
   em caso de falha. A operação é feita no local quando *o1* oferece
   suporte a isso. Isto é equivalente à instrução Python "o1 &= o2".

PyObject *PyNumber_InPlaceXor(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o "bitwise exclusive or" de *o1* por *o2* em caso de
   sucesso, ou "NULL" em caso de falha. A operação é feita no local
   quando *o1* oferece suporte a isso. Isto é equivalente à instrução
   Python "o1 ^= o2".

PyObject *PyNumber_InPlaceOr(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o "bitwise or" de *o1* e *o2* em caso de sucesso, ou "NULL"
   em caso de falha. A operação é feita no local quando *o1* oferece
   suporte a isso. Isto é equivalente à instrução Python "o1 |= o2".

PyObject *PyNumber_Long(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o *o* convertido para um objeto inteiro em caso de sucesso
   ou "NULL" em caso de falha. Isto é equivalente à expressão Python
   "int(o)".

PyObject *PyNumber_Float(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o *o* convertido para um objeto float em caso de sucesso ou
   "NULL" em caso de falha. Isto é equivalente à expressão Python
   "float(o)".

PyObject *PyNumber_Index(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna *o* convertido para int Python  em caso de sucesso ou
   "NULL" com um "TypeError" exceção levantada ao falhar.

   Alterado na versão 3.10: O resultado sempre tem o tipo exato "int".
   Anteriormente, o resultado poderia ter sido uma instância de uma
   subclasse de "int".

PyObject *PyNumber_ToBase(PyObject *n, int base)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o inteiro *n* convertido para a base *base* como uma
   string. O argumento *base* deve ser 2, 8, 10 ou 16. Para as bases
   2, 8 ou 16, a string retornada é prefixada com um marcador de base
   "'0b'", "'0o'" ou "'0x'", respectivamente. Se *n* não for um
   inteiro Python, ele é convertido primeiro com "PyNumber_Index()".

Py_ssize_t PyNumber_AsSsize_t(PyObject *o, PyObject *exc)
    * Parte da ABI Estável.*

   Retorna *o* convertido para um valor "Py_ssize_t" se *o* puder ser
   interpretado como um inteiro. Se a chamada falhar, uma exceção é
   levantada e "-1" é retornado.

   Se *o* puder ser convertido para um int Python, mas a tentativa de
   conversão para um valor "Py_ssize_t" levantar um "OverflowError",
   então o argumento *exc* é o tipo de exceção que será gerada
   (geralmente "IndexError" ou "OverflowError"). Se *exc* for "NULL",
   então a exceção é limpa e o valor é cortado para "PY_SSIZE_T_MIN"
   para um inteiro negativo ou "PY_SSIZE_T_MAX" para um inteiro
   positivo.

int PyIndex_Check(PyObject *o)
    * Parte da ABI Estável desde a versão 3.8.*

   Retorna "1" se *o* for um índice inteiro (tem o slot "nb_index" da
   estrutura "tp_as_number" preenchido) e "0" caso contrário. Esta
   função sempre tem sucesso.
