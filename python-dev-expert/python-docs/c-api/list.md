Objeto List
***********

type PyListObject

   Este subtipo de "PyObject" representa um objeto de lista Python.

PyTypeObject PyList_Type
    * Parte da ABI Estável.*

   Esta instância de "PyTypeObject" representa o tipo de lista Python.
   Este é o mesmo objeto que "list" na camada Python.

int PyList_Check(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadeiro se *p* é um objeto lista ou uma instância de um
   subtipo do tipo lista. Esta função sempre tem sucesso.

int PyList_CheckExact(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadeiro se *p* é um objeto lista, mas não uma instância
   de um subtipo do tipo lista. Esta função sempre tem sucesso.

PyObject *PyList_New(Py_ssize_t len)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna uma nova lista de comprimento *len* em caso de sucesso, ou
   "NULL" em caso de falha.

   Nota:

     Se *len* for maior que zero, os itens do objeto da lista
     retornada são definidos como "NULL". Portanto, você não pode usar
     funções API abstratas, como "PySequence_SetItem()" ou expor o
     objeto ao código Python antes de definir todos os itens para um
     objeto real com "PyList_SetItem()" ou "PyList_SET_ITEM()". As
     seguintes APIs são seguras desde que antes as listas tenham sido
     inicializadas: "PyList_SetItem()" e "PyList_SET_ITEM()".

Py_ssize_t PyList_Size(PyObject *list)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Retorna o comprimento do objeto de lista em *list*; isto é
   equivalente a "len(list)" em um objeto lista.

Py_ssize_t PyList_GET_SIZE(PyObject *list)
    * Thread safety: Atomic.*

   Similar a "PyList_Size()", mas sem verificação de erro.

PyObject *PyList_GetItemRef(PyObject *list, Py_ssize_t index)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.13.** Thread safety: Atomic.*

   Retorna o objeto na posição *index* na lista apontada por *list*. A
   posição deve ser não negativa; não há suporte à indexação do final
   da lista. Se *index* estiver fora dos limites ("<0 or
   >=len(list)"), retorna "NULL" e levanta uma exceção "IndexError".

   Adicionado na versão 3.13.

PyObject *PyList_GetItem(PyObject *list, Py_ssize_t index)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Como "PyList_GetItemRef()", mas retorna uma *referência emprestada*
   em vez de uma *referência forte*.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the list
     concurrently. Prefer "PyList_GetItemRef()", which returns a
     *strong reference*.

PyObject *PyList_GET_ITEM(PyObject *list, Py_ssize_t i)
    *Retorna valor: Referência emprestada.** Thread safety: Safe to
   call from multiple threads with external synchronization only.*

   Similar a "PyList_GetItem()", mas sem verificação de erro.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the list
     concurrently. Prefer "PyList_GetItemRef()", which returns a
     *strong reference*.

int PyList_SetItem(PyObject *list, Py_ssize_t index, PyObject *item)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Define o item no índice *index* na lista como *item*. Retorna "0"
   em caso de sucesso. Se *index* estiver fora dos limites, retorna
   "-1" e levanta uma exceção "IndexError".

   Nota:

     This function "*steals*" a reference to *item*, even on error. On
     success, it discards a reference to an item already in the list
     at the affected position (unless it was "NULL").

void PyList_SET_ITEM(PyObject *list, Py_ssize_t i, PyObject *o)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Forma macro de "PyList_SetItem()" sem verificação de erro. Este é
   normalmente usado apenas para preencher novas listas onde não há
   conteúdo anterior.

   A verificação de limites é realizada como uma asserção se o Python
   for construído em modo de depuração ou "com asserções".

   Nota:

     This macro "*steals*" a reference to *item*, and, unlike
     "PyList_SetItem()", does *not* discard a reference to any item
     that is being replaced; any reference in *list* at position *i*
     will be leaked.

   Nota:

     In the *free-threaded build*, this macro has no internal
     synchronization. It is normally only used to fill in new lists
     where no other thread has a reference to the list. If the list
     may be shared, use "PyList_SetItem()" instead, which uses a *per-
     object lock*.

int PyList_Insert(PyObject *list, Py_ssize_t index, PyObject *item)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Insere o item *item* na lista *list* na frente do índice *index*.
   Retorna "0" se for bem-sucedido; retorna "-1" e levanta uma exceção
   se malsucedido. Análogo a "list.insert(index, item)".

int PyList_Append(PyObject *list, PyObject *item)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Adiciona o item *item* ao final da lista *list*. Retorna "0" se for
   bem-sucedido; retorna "-1" e levanta uma exceção se malsucedido.
   Análogo a "list.insert(index, item)".

PyObject *PyList_GetSlice(PyObject *list, Py_ssize_t low, Py_ssize_t high)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna uma lista dos objetos em *list* contendo os objetos *entre*
   *low* e *alto*. Retorne "NULL" e levanta uma exceção se
   malsucedido. Análogo a "list[low:high]". Não há suporte à indexação
   do final da lista.

int PyList_SetSlice(PyObject *list, Py_ssize_t low, Py_ssize_t high, PyObject *itemlist)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Define a fatia de *list* entre *low* e *high* para o conteúdo de
   *itemlist*. Análogo a "list[low:high] = itemlist". *itemlist* pode
   ser "NULL", indicando a atribuição de uma lista vazia (exclusão de
   fatia). Retorna "0" em caso de sucesso, "-1" em caso de falha. Não
   há suporte à indexação do final da lista.

   Nota:

     In the *free-threaded build*, when *itemlist* is a "list", both
     *list* and *itemlist* are locked for the duration of the
     operation. For other iterables (or "NULL"), only *list* is
     locked.

int PyList_Extend(PyObject *list, PyObject *iterable)
    * Thread safety: Safe for concurrent use on the same object.*

   Estende *list* com o conteúdo de *iterable*. Isto é o mesmo que
   "PyList_SetSlice(list, PY_SSIZE_T_MAX, PY_SSIZE_T_MAX, iterable)" e
   análogo a "list.extend(iterable)" ou "list += iterable".

   Levanta uma exceção e retorna "-1" se *list* não for um objeto
   "list". Retorna 0 em caso de sucesso.

   Adicionado na versão 3.13.

   Nota:

     In the *free-threaded build*, when *iterable* is a "list", "set",
     "dict", or dict view, both *list* and *iterable* (or its
     underlying dict) are locked for the duration of the operation.
     For other iterables, only *list* is locked; *iterable* may be
     concurrently modified by another thread.

int PyList_Clear(PyObject *list)
    * Thread safety: Atomic.*

   Remove todos os itens da *lista*. Isto é o mesmo que
   "PyList_SetSlice(list, 0, PY_SSIZE_T_MAX, NULL)" e análogo a
   "list.clear()" ou "del list[:]".

   Levanta uma exceção e retorna "-1" se *list* não for um objeto
   "list". Retorna 0 em caso de sucesso.

   Adicionado na versão 3.13.

int PyList_Sort(PyObject *list)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Ordena os itens de *list* no mesmo lugar. Retorna "0" em caso de
   sucesso, e "-1" em caso de falha. Isso é o equivalente de
   "list.sort()".

   Nota:

     In the *free-threaded build*, element comparison via "__lt__()"
     can execute arbitrary Python code, during which the *per-object
     lock* may be temporarily released. For built-in types ("str",
     "int", "float"), the lock is not released during comparison.

int PyList_Reverse(PyObject *list)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Inverte os itens de *list* no mesmo lugar. Retorna "0" em caso de
   sucesso, e "-1" em caso de falha. Isso é o equivalente de
   "list.reverse()".

PyObject *PyList_AsTuple(PyObject *list)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um novo objeto tupla contendo os conteúdos de *list*;
   equivale a "tuple(list)".
