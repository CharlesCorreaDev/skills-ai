Objetos Iteradores
******************

O Python fornece dois objetos iteradores de propósito geral. O
primeiro, um iterador de sequência, trabalha com uma sequência
arbitrária suportando o método "__getitem__()". O segundo trabalha com
um objeto chamável e um valor de sentinela, chamando o chamável para
cada item na sequência e finalizando a iteração quando o valor de
sentinela é retornado.

PyTypeObject PySeqIter_Type
    * Parte da ABI Estável.*

   Objeto de tipo para objetos iteradores retornados por
   "PySeqIter_New()" e a forma de um argumento da função embutida
   "iter()" para os tipos de sequência embutidos.

int PySeqIter_Check(PyObject *op)

   Retorna true se o tipo de *op* for "PySeqIter_Type". Esta função
   sempre é bem-sucedida.

PyObject *PySeqIter_New(PyObject *seq)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um iterador que funcione com um objeto de sequência geral,
   *seq*. A iteração termina quando a sequência levanta "IndexError"
   para a operação de assinatura.

PyTypeObject PyCallIter_Type
    * Parte da ABI Estável.*

   Objeto de tipo para objetos iteradores retornados por
   "PyCallIter_New()" e a forma de dois argumentos da função embutida
   "iter()".

int PyCallIter_Check(PyObject *op)

   Retorna true se o tipo de *op* for "PyCallIter_Type". Esta função
   sempre é bem-sucedida.

PyObject *PyCallIter_New(PyObject *callable, PyObject *sentinel)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um novo iterador. O primeiro parâmetro, *callable*, pode
   ser qualquer objeto chamável do Python que possa ser chamado sem
   parâmetros; cada chamada deve retornar o próximo item na iteração.
   Quando *callable* retorna um valor igual a *sentinel*, a iteração
   será encerrada.


Objetos intervalo
=================

PyTypeObject PyRange_Type
    * Parte da ABI Estável.*

   O objeto tipo para objetos "range".

int PyRange_Check(PyObject *o)

   Retorna verdadeiro se o objeto *op* for uma instância de um objeto
   "range". Esta função sempre tem sucesso.


Tipos de iteradores embutidos
=============================

Esses são tipos de iteração embutidos que estão incluídos na API C do
Python, mas não fornecem funções adicionais. Eles estão aqui para fins
de completude.

Estes ponteiros são parte da ABI Estável.

+----------------------------------------------------+----------------------------------------------------+
| Tipo em C                                          | Tipo em Python                                     |
|====================================================|====================================================|
| PyTypeObject PyEnum_Type                           | "enumerate"                                        |
+----------------------------------------------------+----------------------------------------------------+
| PyTypeObject PyFilter_Type                         | "filter"                                           |
+----------------------------------------------------+----------------------------------------------------+
| PyTypeObject PyMap_Type                            | "map"                                              |
+----------------------------------------------------+----------------------------------------------------+
| PyTypeObject PyReversed_Type                       | "reversed"                                         |
+----------------------------------------------------+----------------------------------------------------+
| PyTypeObject PyZip_Type                            | "zip"                                              |
+----------------------------------------------------+----------------------------------------------------+


Outros objetos iteradores
=========================

PyTypeObject PyByteArrayIter_Type
    * Parte da ABI Estável.*

PyTypeObject PyBytesIter_Type
    * Parte da ABI Estável.*

PyTypeObject PyListIter_Type
    * Parte da ABI Estável.*

PyTypeObject PyListRevIter_Type
    * Parte da ABI Estável.*

PyTypeObject PySetIter_Type
    * Parte da ABI Estável.*

PyTypeObject PyTupleIter_Type
    * Parte da ABI Estável.*

PyTypeObject PyRangeIter_Type
    * Parte da ABI Estável.*

PyTypeObject PyLongRangeIter_Type
    * Parte da ABI Estável.*

PyTypeObject PyDictIterKey_Type
    * Parte da ABI Estável.*

PyTypeObject PyDictRevIterKey_Type
    * Parte da ABI Estável desde a versão 3.8.*

PyTypeObject PyDictIterValue_Type
    * Parte da ABI Estável.*

PyTypeObject PyDictRevIterValue_Type
    * Parte da ABI Estável desde a versão 3.8.*

PyTypeObject PyDictIterItem_Type
    * Parte da ABI Estável.*

PyTypeObject PyDictRevIterItem_Type
    * Parte da ABI Estável desde a versão 3.8.*

PyTypeObject PyODictIter_Type

   Objetos de tipo para iteradores de vários objetos embutidos.

   Não cria instâncias dessas diretamente; prefira chamar
   "PyObject_GetIter()" em vez disso.

   Note que não há garantia de que um determinado tipo embutido
   utilize um determinado tipo de iterador. Por exemplo, iterar sobre
   um "range" utilizará um de dois tipos de iterador, dependendo do
   tamanho do intervalo. Outros tipos podem começar a usar um esquema
   semelhante no futuro, sem aviso prévio.
