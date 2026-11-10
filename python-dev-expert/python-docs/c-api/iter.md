Protocolo Iterador
******************

Existem duas funções especificas para trabalhar com iteradores.

int PyIter_Check(PyObject *o)
    * Parte da ABI Estável desde a versão 3.8.*

   Retorna valor diferente de zero se o objeto *o* puder ser passado
   com segurança para "PyIter_NextItem()", e "0" caso contrário. Esta
   função sempre tem sucesso.

int PyAIter_Check(PyObject *o)
    * Parte da ABI Estável desde a versão 3.10.*

   Retorna valor diferente de zero se o objeto *o* fornecer o
   protocolo "AsyncIterator" e "0" caso contrário. Esta função sempre
   é bem-sucedida.

   Adicionado na versão 3.10.

int PyIter_NextItem(PyObject *iter, PyObject **item)
    * Parte da ABI Estável desde a versão 3.14.*

   Retorna "1" e define *item* como uma *referência forte* do próximo
   valor do iterador *iter* em caso de sucesso. Retorna "0" e define
   *item* como "NULL" se não houver valores restantes. Retorna "-1",
   define *item* como "NULL" e define uma exceção em caso de erro.

   Adicionado na versão 3.14.

PyObject *PyIter_Next(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Esta é uma versão mais antiga de "PyIter_NextItem()", que foi
   mantida para retrocompatibilidade. Prefira "PyIter_NextItem()".

   Retorna o próximo valor do iterador *o*. O objeto deve ser um
   iterador de acordo com "PyIter_Check()" (cabe ao chamador verificar
   isso). Se não houver valores restantes, retorna "NULL" sem nenhuma
   exceção definida. Se ocorrer um erro ao recuperar o item, retorna
   "NULL" e passa a exceção.

type PySendResult

   O valor de enum usado para representar diferentes resultados de
   "PyIter_Send()".

   Adicionado na versão 3.10.

PySendResult PyIter_Send(PyObject *iter, PyObject *arg, PyObject **presult)
    * Parte da ABI Estável desde a versão 3.10.*

   Envia o valor *arg* para o iterador *iter*. Retorna:

   * "PYGEN_RETURN" se o iterador retornar. O valor de retorno é
     retornado via *presult*.

   * "PYGEN_NEXT" se o iterador render. O valor produzido é retornado
     via *presult*.

   * "PYGEN_ERROR" se o iterador tiver levantado uma exceção.
     *presult* é definido como "NULL".

   Adicionado na versão 3.10.
