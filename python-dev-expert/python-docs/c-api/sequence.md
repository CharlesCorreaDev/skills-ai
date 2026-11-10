Protocolo de sequência
**********************

int PySequence_Check(PyObject *o)
    * Parte da ABI Estável.*

   Retorna "1" se o objeto fornecer o protocolo de sequência e "0"
   caso contrário. Note que ele retorna "1" para classes Python com um
   método "__getitem__()" a menos que sejam subclasses de "dict" já
   que no caso geral é impossível determinar que tipo de chaves a
   classe provê. Esta função sempre obtém sucesso.

Py_ssize_t PySequence_Size(PyObject *o)
Py_ssize_t PySequence_Length(PyObject *o)
    * Parte da ABI Estável.*

   Retorna o número de objetos na sequência *o* em caso de sucesso, ou
   "-1" em caso de falha. Equivale à expressão Python "len(o)".

PyObject *PySequence_Concat(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna a concatenação de *o1* e *o2* em caso de sucesso, e "NULL"
   em caso de falha. Equivale à expressão Python "o1 + o2".

PyObject *PySequence_Repeat(PyObject *o, Py_ssize_t count)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado da repetição do objeto sequência *o* *count*
   vezes ou "NULL" em caso de falha. Equivale à expressão Python "o *
   count".

PyObject *PySequence_InPlaceConcat(PyObject *o1, PyObject *o2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna a concatenação de *o1* e *o2* em caso de sucesso, e "NULL"
   em caso de falha. A operação é feita *localmente* se *o1* permitir.
   Equivale à expressão Python "o1 += o2".

PyObject *PySequence_InPlaceRepeat(PyObject *o, Py_ssize_t count)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o resultado da repetição do objeto sequência *o* *count*
   vezes ou "NULL" em caso de falha. A operação é feita *localmente*
   se *o* permitir. Equivale à expressão Python "o *= count".

PyObject *PySequence_GetItem(PyObject *o, Py_ssize_t i)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o elemento *i* de *o* ou "NULL" em caso de falha. Equivale
   à expressão Python "o[i]".

PyObject *PySequence_GetSlice(PyObject *o, Py_ssize_t i1, Py_ssize_t i2)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna a fatia do objeto sequência *o* entre *i1* e *i2*, ou
   "NULL" em caso de falha. Equivale à expressão Python "o[i1:i2]".

int PySequence_SetItem(PyObject *o, Py_ssize_t i, PyObject *v)
    * Parte da ABI Estável.*

   Atribui o objeto *v* ao elemento *i* de *o*. Levanta uma exceção e
   retorna "-1" em caso de falha; retorna "0" em caso de sucesso. Isso
   é o equivalente à instrução Python "o[i] = v". Esta função *não*
   "*rouba*" uma referência a *v*.

   Se *v* for "NULL", o elemento será removido, mas este recurso foi
   descontinuado em favor do uso de "PySequence_DelItem()".

int PySequence_DelItem(PyObject *o, Py_ssize_t i)
    * Parte da ABI Estável.*

   Exclui o elemento *i* do objeto *o*. Retorna "-1" em caso de falha.
   Equivale à instrução Python "del o[i]".

int PySequence_SetSlice(PyObject *o, Py_ssize_t i1, Py_ssize_t i2, PyObject *v)
    * Parte da ABI Estável.*

   Atribui o objeto sequência *v* à fatia no objeto sequência *o* de
   *i1* a *i2*. Equivale à instrução Python "o[i1:i2] = v".

int PySequence_DelSlice(PyObject *o, Py_ssize_t i1, Py_ssize_t i2)
    * Parte da ABI Estável.*

   Exclui a fatia no objeto sequência *o* de *i1* a *i2*. Retorna "-1"
   em caso de falha. Equivale à instrução Python "del o[i1:i2]".

Py_ssize_t PySequence_Count(PyObject *o, PyObject *value)
    * Parte da ABI Estável.*

   Retorna a quantidade de ocorrências de *value* em *o*, isto é,
   retorna a quantidade de chaves onde "o[key] == value". Em caso de
   falha, retorna "-1". Equivale à expressão Python "o.count(value)".

int PySequence_Contains(PyObject *o, PyObject *value)
    * Parte da ABI Estável.*

   Determina se *o* contém *value*. Se um item em *o* for igual a
   *value*, retorna "1", senão, retorna "0". Em caso de erro, retorna
   "-1". Equivale à expressão Python "value in o".

int PySequence_In(PyObject *o, PyObject *value)
    * Parte da ABI Estável.*

   Apelido para "PySequence_Contains()".

   Suavemente descontinuado desde a versão 3.14: A função não deve
   mais ser usada para escrever novos códigos.

Py_ssize_t PySequence_Index(PyObject *o, PyObject *value)
    * Parte da ABI Estável.*

   Retorna o primeiro índice *i* tal que "o[i] == value". Em caso de
   erro, retorna "-1". Equivale à expressão Python "o.index(value)".

PyObject *PySequence_List(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um objeto lista com o mesmo conteúdo da sequência ou
   iterável *o*, ou "NULL" em caso de falha. Garante-se que a lista
   retornada será nova. Equivale à expressão Python "list(o)".

PyObject *PySequence_Tuple(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o objeto tupla com o mesmo conteúdo da sequência ou
   iterável *o*, ou "NULL" em caso de falha. Se *o* for uma tupla,
   retorna uma nova referência. Senão, uma tupla será construída com o
   conteúdo apropriado. Equivale à expressão Python "tuple(o)".

PyObject *PySequence_Fast(PyObject *o, const char *m)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna a sequência ou iterável *o* como um objeto usável por
   outras funções da família "PySequence_Fast*". Se o objeto não for
   uma sequência ou iterável, levanta "TypeError" com *m* sendo o
   texto da mensagem. Retorna "NULL" em caso de falha.

   As funções "PySequence_Fast*" têm esse nome porque presumem que *o*
   é um "PyTupleObject" ou um "PyListObject" e porque acessam os
   campos de dados de *o* diretamente.

   Como detalhe de implementação de CPython, se *o* já for uma
   sequência ou lista, ele será retornado.

Py_ssize_t PySequence_Fast_GET_SIZE(PyObject *o)

   Retorna o comprimento de *o*, presumindo que *o* foi retornado por
   "PySequence_Fast()" e que *o* não seja "NULL". O tamanho também
   pode ser obtido ao chamar "PySequence_Size()" em *o*, mas
   "PySequence_Fast_GET_SIZE()" é mais rápida, ao supor que *o* é uma
   lista ou tupla.

PyObject *PySequence_Fast_GET_ITEM(PyObject *o, Py_ssize_t i)
    *Retorna valor: Referência emprestada.*

   Retorna o elemento *i* de *o*, presumindo que *o* foi retornado por
   "PySequence_Fast()", que *o* seja "NULL", e que *i* esteja nos
   limites.

PyObject **PySequence_Fast_ITEMS(PyObject *o)

   Retorna o vetor subjacente de ponteiros PyObject. Presume que *o*
   foi retornado por "PySequence_Fast()" e que *o* não seja "NULL".

   Note que, se uma lista for redimensionada, a realocação poderá
   reposicionar o vetor de itens. Portanto, só use o ponteiro de vetor
   subjacente em contextos onde a sequência não mudará.

PyObject *PySequence_ITEM(PyObject *o, Py_ssize_t i)
    *Retorna valor: Nova referência.*

   Retorna o elemento *i* de *o*, ou "NULL" em caso de falha. É uma
   forma mais rápida de "PySequence_GetItem()", mas sem verificar se
   "PySequence_Check()" em *o* é verdadeiro e sem ajustar índices
   negativos.
