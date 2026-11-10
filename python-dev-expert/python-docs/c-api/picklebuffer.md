Objetos buffer serializados com pickle
**************************************

Adicionado na versão 3.8.

Um objeto "pickle.PickleBuffer" encapsula um objeto provedor de buffer
para transferência de dados fora de banda com o módulo "pickle".

PyTypeObject PyPickleBuffer_Type

   Esta instância de "PyTypeObject" representa o tipo de buffer
   serializado com pickle do Python. Este é o mesmo objeto que
   "pickle.PickleBuffer" na camada Python.

int PyPickleBuffer_Check(PyObject *op)

   Retorna verdadeiro se *op* for uma instância de buffer serializado
   com pickle. Esta função sempre tem sucesso.

PyObject *PyPickleBuffer_FromObject(PyObject *obj)

   Cria um buffer serializado com pickle a partir do objeto *obj*.

   Esta função falhará se *obj* não oferecer suporte ao protocolo de
   buffer.

   Em caso de sucesso, retorna uma nova instância de buffer
   serializado com pickle. Em caso de falha, define uma exceção e
   retorna "NULL".

   Análogo a chamar "pickle.PickleBuffer" com *obj* em Python.

const Py_buffer *PyPickleBuffer_GetBuffer(PyObject *picklebuf)

   Obtém um ponteiro para o "Py_buffer" subjacente que o buffer
   serializado com pickle encapsula.

   O ponteiro retornado é válido enquanto *picklebuf* estiver ativo e
   não tiver sido liberado. O chamador não deve modificar ou liberar o
   "Py_buffer" retornado. Se o buffer serializado com pickle tiver
   sido liberado, levanta uma exceção "ValueError".

   Em caso de sucesso, retorna um ponteiro para a visualização do
   buffer. Em caso de falha, define uma exceção e retorna "NULL".

int PyPickleBuffer_Release(PyObject *picklebuf)

   Libera o buffer subjacente mantido pelo buffer serializado com
   pickle.

   Retorna "0" em caso de sucesso. Em caso de falha, define uma
   exceção e retorna "-1".

   Análogo a chamar "pickle.PickleBuffer.release()" em Python.
