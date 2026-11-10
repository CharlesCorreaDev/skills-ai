Dictionary objects
******************

type PyDictObject

   Este subtipo do "PyObject" representa um objeto dicionário Python.

PyTypeObject PyDict_Type
    * Parte da ABI Estável.*

   Esta instância do "PyTypeObject" representa o tipo do dicionário
   Python. Este é o mesmo objeto "dict" na camada do Python.

int PyDict_Check(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadeiro se *p* é um objeto dicionário ou uma instância
   de um subtipo do tipo dicionário. Esta função sempre tem sucesso.

int PyDict_CheckExact(PyObject *p)
    * Thread safety: Atomic.*

   Retorna verdadeiro se *p* é um objeto dicionário, mas não uma
   instância de um subtipo do tipo dicionário. Esta função sempre tem
   sucesso.

PyObject *PyDict_New()
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um novo dicionário vazio ou "NULL" em caso de falha.

PyObject *PyDictProxy_New(PyObject *mapping)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um objeto "types.MappingProxyType" para um mapeamento que
   reforça o comportamento somente leitura. Isso normalmente é usado
   para criar uma visão para evitar a modificação do dicionário para
   tipos de classes não dinâmicas.

   The first argument can be a "dict", a "frozendict", or a mapping.

   Alterado na versão 3.15: Also accept "frozendict".

PyTypeObject PyDictProxy_Type
    * Parte da ABI Estável.*

   O objeto de tipo para mapear objetos proxy criados por
   "PyDictProxy_New()" e para o atributo somente leitura "__dict__" de
   muitos tipos embutidos. Uma instância de "PyDictProxy_Type" fornece
   uma visão dinâmica e somente leitura de um dicionário subjacente:
   as alterações no dicionário subjacente são refletidas no proxy, mas
   o próprio proxy não oferece suporte a operações de mutação. Isso
   corresponde a "types.MappingProxyType" no Python.

void PyDict_Clear(PyObject *p)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Esvazia um dicionário existente de todos os pares chave-valor.

   Do nothing if the argument is not a "dict" or a "dict" subclass.

int PyDict_Contains(PyObject *p, PyObject *key)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Determina se o dicionário *p* contém *key*. Se um item em *p*
   corresponder à *key*, retorna "1", caso contrário, retorna "0". Em
   caso de erro, retorna "-1". Isso equivale à expressão Python "key
   in p".

   The first argument can be a "dict" or a "frozendict".

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

   Alterado na versão 3.15: Also accept "frozendict".

int PyDict_ContainsString(PyObject *p, const char *key)
    * Thread safety: Atomic.*

   É o mesmo que "PyDict_Contains()", mas *key* é especificada como
   uma string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

   The first argument can be a "dict" or a "frozendict".

   Adicionado na versão 3.13.

   Alterado na versão 3.15: Also accept "frozendict".

PyObject *PyDict_Copy(PyObject *p)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um novo dicionário que contém o mesmo chave-valor como *p*.

int PyDict_SetItem(PyObject *p, PyObject *key, PyObject *val)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Insere *val* no dicionário *p* com a chave *key*. *key* deve ser
   *hasheável*; se não for, "TypeError" será levantada. Retorna "0" em
   caso de sucesso ou "-1" em caso de falha. Esta função *não*
   "*rouba*" uma referência para *val*.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

int PyDict_SetItemString(PyObject *p, const char *key, PyObject *val)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   É o mesmo que "PyDict_SetItem()", mas *key* é especificada como uma
   string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

int PyDict_DelItem(PyObject *p, PyObject *key)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Remove a entrada no dicionário *p* com a chave *key*. *key* deve
   ser *hasheável*; se não for, "TypeError" é levantada. Se *key* não
   estiver no dicionário, "KeyError" é levantada. Retorna "0" em caso
   de sucesso ou "-1" em caso de falha.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

int PyDict_DelItemString(PyObject *p, const char *key)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   É o mesmo que "PyDict_DelItem()", mas *key* é especificada como uma
   string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

int PyDict_GetItemRef(PyObject *p, PyObject *key, PyObject **result)
    * Parte da ABI Estável desde a versão 3.13.** Thread safety: Safe
   for concurrent use on the same object.*

   Retorna uma nova *referência forte* para o objeto dicionário *p*
   que possui uma chave *key*:

   * Se a chave estiver presente, define **result* como uma nova
     *referência forte* para o valor e retorna "1".

   * Se a chave estiver ausente, define **result* como "NULL" e
     retorna "0".

   * Em caso de erro, levanta uma exceção, define **result* como
     "NULL" e retorna "-1".

   The first argument can be a "dict" or a "frozendict".

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

   Adicionado na versão 3.13.

   Alterado na versão 3.15: Also accept "frozendict".

   Veja também a função "PyObject_GetItem()".

PyObject *PyDict_GetItem(PyObject *p, PyObject *key)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Retorna um *referência emprestada* para o objeto do dicionário *p*
   que possui uma chave *key*. Retorna "NULL" se a chave *key* não
   estiver presente, mas *sem* definir uma exceção.

   The first argument can be a "dict" or a "frozendict".

   Nota:

     Exceções que ocorrem ao chamar os métodos "__hash__()" e
     "__eq__()" são ignoradas silenciosamente. Ao invés disso, use a
     função "PyDict_GetItemWithError()".

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the dictionary
     concurrently. Prefer "PyDict_GetItemRef()", which returns a
     *strong reference*.

   Alterado na versão 3.10: Chamar esta API sem um *estado de thread
   anexado* era permitido por motivos históricos. Não é mais
   permitido.

   Alterado na versão 3.15: Also accept "frozendict".

PyObject *PyDict_GetItemWithError(PyObject *p, PyObject *key)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Variante de "PyDict_GetItem()" que não suprime exceções. Retorna
   "NULL" **com** uma exceção definida se uma exceção ocorreu. Retorna
   "NULL" ** sem ** uma exceção definida se a chave não estiver
   presente.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the dictionary
     concurrently. Prefer "PyDict_GetItemRef()", which returns a
     *strong reference*.

   Alterado na versão 3.15: Also accept "frozendict".

PyObject *PyDict_GetItemString(PyObject *p, const char *key)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   É o mesmo que "PyDict_GetItem()", mas *key* é especificada como uma
   string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

   Nota:

     Exceções que ocorrem ao chamar os métodos "__hash__()" e
     "__eq__()" ou ao criar objetos temporários da classe "str" são
     ignoradas silenciosamente. Ao invés disso, prefira usar a função
     "PyDict_GetItemWithError()" com sua própria *key* de
     "PyUnicode_FromString()".

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the dictionary
     concurrently. Prefer "PyDict_GetItemStringRef()", which returns a
     *strong reference*.

   Alterado na versão 3.15: Also accept "frozendict".

int PyDict_GetItemStringRef(PyObject *p, const char *key, PyObject **result)
    * Parte da ABI Estável desde a versão 3.13.** Thread safety:
   Atomic.*

   Similar a "PyDict_GetItemRef()", mas *key* é especificada como uma
   string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

   Adicionado na versão 3.13.

   Alterado na versão 3.15: Also accept "frozendict".

PyObject *PyDict_SetDefault(PyObject *p, PyObject *key, PyObject *defaultobj)
    *Retorna valor: Referência emprestada.** Thread safety: Safe to
   call from multiple threads with external synchronization only.*

   Isso é o mesmo que o "dict.setdefault()" de nível Python. Se
   presente, ele retorna o valor correspondente a *key* do dicionário
   *p*. Se a chave não estiver no dict, ela será inserida com o valor
   *defaultobj* e *defaultobj* será retornado. Esta função avalia a
   função hash de *key* apenas uma vez, em vez de avaliá-la
   independentemente para a pesquisa e a inserção.

   Adicionado na versão 3.4.

   Nota:

     In the *free-threaded build*, the returned *borrowed reference*
     may become invalid if another thread modifies the dictionary
     concurrently. Prefer "PyDict_SetDefaultRef()", which returns a
     *strong reference*.

int PyDict_SetDefaultRef(PyObject *p, PyObject *key, PyObject *default_value, PyObject **result)
    * Parte da ABI Estável desde a versão 3.15.** Thread safety: Safe
   for concurrent use on the same object.*

   Insere *default_value* no dicionário *p* com uma chave *key* se a
   chave ainda não estiver presente no dicionário. Se *result* não for
   "NULL", então **result* é definido como uma *referência forte* para
   *default_value*, se a chave não estiver presente, ou para o valor
   existente, se *key* já estava presente no dicionário. Retorna "1"
   se a chave estava presente e *default_value* não foi inserido, ou
   "0" se a chave não estava presente e *default_value* foi inserido.
   Em caso de falha, retorna "-1", define uma exceção e define
   "*result" como "NULL".

   Para maior clareza: se você tiver uma referência forte para
   *default_value* antes de chamar esta função, então depois que ela
   retornar, você terá uma referência forte para *default_value* e
   **result* (se não for "NULL"). Estes podem referir-se ao mesmo
   objeto: nesse caso você mantém duas referências separadas para ele.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

   Adicionado na versão 3.13.

int PyDict_Pop(PyObject *p, PyObject *key, PyObject **result)
    * Thread safety: Safe for concurrent use on the same object.*

   Remove *key* do dicionário *p* e, opcionalmente, retorna o valor
   removido. Não levanta "KeyError" se a chave estiver ausente.

   * Se a chave estiver presente, define **result* como uma nova
     referência para o valor se *result* não for "NULL" e retorna "1".

   * Se a chave estiver ausente, define **result* como "NULL" se
     *result* não for "NULL" e retorna "0".

   * Em caso de erro, levanta uma exceção e retorna "-1".

   Similar a "dict.pop()", mas sem o valor padrão e sem levantar
   "KeyError" se a chave estiver ausente.

   Nota:

     The operation is atomic on *free threading* when *key* is "str",
     "int", "float", "bool" or "bytes".

   Adicionado na versão 3.13.

int PyDict_PopString(PyObject *p, const char *key, PyObject **result)
    * Thread safety: Atomic.*

   Similar a "PyDict_Pop()", mas *key* é especificada como uma string
   de bytes const char* codificada em UTF-8, em vez de um PyObject*.

   Adicionado na versão 3.13.

PyObject *PyDict_Items(PyObject *p)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um "PyListObject" contendo todos os itens do dicionário.

   The first argument can be a "dict" or a "frozendict".

   Alterado na versão 3.15: Also accept "frozendict".

PyObject *PyDict_Keys(PyObject *p)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um "PyListObject" contendo todas as chaves do dicionário.

   The first argument can be a "dict" or a "frozendict".

   Alterado na versão 3.15: Also accept "frozendict".

PyObject *PyDict_Values(PyObject *p)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um "PyListObject" contendo todos os valores do dicionário
   *p*.

   The first argument can be a "dict" or a "frozendict".

   Alterado na versão 3.15: Also accept "frozendict".

Py_ssize_t PyDict_Size(PyObject *p)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Retorna o número de itens no dicionário. Isso é equivalente a
   "len(p)" em um dicionário.

   The argument can be a "dict" or a "frozendict".

   Alterado na versão 3.15: Also accept "frozendict".

Py_ssize_t PyDict_GET_SIZE(PyObject *p)
    * Thread safety: Atomic.*

   Similar a "PyDict_Size()", mas sem verificação de erro.

   Alterado na versão 3.15: Also accept "frozendict".

int PyDict_Next(PyObject *p, Py_ssize_t *ppos, PyObject **pkey, PyObject **pvalue)
    * Parte da ABI Estável.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Itera todos os pares de valores-chave no dicionário *p*. O
   "Py_ssize_t" referido por *ppos* deve ser inicializado para "0"
   antes da primeira chamada para esta função para iniciar a iteração;
   a função retorna true para cada par no dicionário e false quando
   todos os pares forem relatados. Os parâmetros *pkey* e *pvalue*
   devem apontar para variáveis de PyObject* que serão preenchidas com
   cada chave e valor, respectivamente, ou podem ser "NULL". Todas as
   referências retornadas por meio deles são emprestadas. *ppos* não
   deve ser alterado durante a iteração. Seu valor representa
   deslocamentos dentro da estrutura do dicionário interno e, como a
   estrutura é esparsa, os deslocamentos não são consecutivos.

   The first argument can be a "dict" or a "frozendict".

   Por exemplo:

      PyObject *key, *value;
      Py_ssize_t pos = 0;

      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          /* fazer algo de interessante com os valores... */
          ...
      }

   O dicionário *p* não deve sofrer mutação durante a iteração. É
   seguro modificar os valores das chaves à medida que você itera no
   dicionário, mas apenas enquanto o conjunto de chaves não mudar. Por
   exemplo:

      PyObject *key, *value;
      Py_ssize_t pos = 0;

      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          long i = PyLong_AsLong(value);
          if (i == -1 && PyErr_Occurred()) {
              return -1;
          }
          PyObject *o = PyLong_FromLong(i + 1);
          if (o == NULL)
              return -1;
          if (PyDict_SetItem(self->dict, key, o) < 0) {
              Py_DECREF(o);
              return -1;
          }
          Py_DECREF(o);
      }

   The function is not thread-safe in the *free-threaded* build
   without external synchronization for a mutable "dict". You can use
   "Py_BEGIN_CRITICAL_SECTION" to lock the dictionary while iterating
   over it:

      Py_BEGIN_CRITICAL_SECTION(self->dict);
      while (PyDict_Next(self->dict, &pos, &key, &value)) {
          ...
      }
      Py_END_CRITICAL_SECTION();

   The function is thread-safe on a "frozendict".

   Nota:

     Na construção com threads livres, esta função pode ser usada com
     segurança dentro de uma seção crítica. No entanto, as referências
     retornadas para *pkey* e *pvalue* são *emprestadas* e só são
     válidas enquanto a seção crítica é mantida. Se precisar usar
     esses objetos fora da seção crítica ou quando a seção crítica
     puder ser suspensa, crie uma *referência forte* (por exemplo,
     usando "Py_NewRef()").

   Alterado na versão 3.15: Also accept "frozendict".

int PyDict_Merge(PyObject *a, PyObject *b, int override)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Itera sobre o objeto de mapeamento *b* adicionando pares de
   valores-chave ao dicionário *a*. *b* pode ser um dicionário, ou
   qualquer objeto que suporte "PyMapping_Keys()" e
   "PyObject_GetItem()". Se *override* for verdadeiro, os pares
   existentes em *a* serão substituídos se uma chave correspondente
   for encontrada em *b*, caso contrário, os pares serão adicionados
   apenas se não houver uma chave correspondente em *a*. Retorna "0"
   em caso de sucesso ou "-1" se uma exceção foi levantada.

   Nota:

     In the *free-threaded build*, when *b* is a "dict" (with the
     standard iterator), both *a* and *b* are locked for the duration
     of the operation. When *b* is a non-dict mapping, only *a* is
     locked; *b* may be concurrently modified by another thread.

int PyDict_Update(PyObject *a, PyObject *b)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   É o mesmo que "PyDict_Merge(a, b, 1)" em C, e é semelhante a
   "a.update(b)" em Python, exceto que "PyDict_Update()" não cai na
   iteração em uma sequência de pares de valores de chave se o segundo
   argumento não tiver o atributo "keys". Retorna "0" em caso de
   sucesso ou "-1" se uma exceção foi levantada.

   Nota:

     In the *free-threaded build*, when *b* is a "dict" (with the
     standard iterator), both *a* and *b* are locked for the duration
     of the operation. When *b* is a non-dict mapping, only *a* is
     locked; *b* may be concurrently modified by another thread.

int PyDict_MergeFromSeq2(PyObject *a, PyObject *seq2, int override)
    * Parte da ABI Estável.** Thread safety: Safe for concurrent use
   on the same object.*

   Atualiza ou mescla no dicionário *a*, a partir dos pares de chave-
   valor em *seq2*. *seq2* deve ser um objeto iterável produzindo
   objetos iteráveis de comprimento 2, vistos como pares chave-valor.
   No caso de chaves duplicadas, a última vence se *override* for
   verdadeiro, caso contrário, a primeira vence. Retorne "0" em caso
   de sucesso ou "-1" se uma exceção foi levantada. Python equivalente
   (exceto para o valor de retorno):

      def PyDict_MergeFromSeq2(a, seq2, override):
          for key, value in seq2:
              if override or key not in a:
                  a[key] = value

   Nota:

     In the *free-threaded* build, only *a* is locked. The iteration
     over *seq2* is not synchronized; *seq2* may be concurrently
     modified by another thread.

int PyDict_AddWatcher(PyDict_WatchCallback callback)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Registra *callback* como um observador de dicionário. Retorna um ID
   inteiro não negativo que deve ser passado para futuras chamadas a
   "PyDict_Watch()". Em caso de erro (por exemplo, não há mais IDs de
   observador disponíveis), retorna "-1" e define uma exceção.

   Nota:

     This function is not internally synchronized. In the *free-
     threaded* build, callers should ensure no concurrent calls to
     "PyDict_AddWatcher()" or "PyDict_ClearWatcher()" are in progress.

   Adicionado na versão 3.12.

int PyDict_ClearWatcher(int watcher_id)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Limpa o observador identificado por *watcher_id* retornado
   anteriormente de "PyDict_AddWatcher()". Retorna "0" em caso de
   sucesso, "-1" em caso de erro (por exemplo, se o *watcher_id*
   fornecido nunca foi registrado).

   Nota:

     This function is not internally synchronized. In the *free-
     threaded* build, callers should ensure no concurrent calls to
     "PyDict_AddWatcher()" or "PyDict_ClearWatcher()" are in progress.

   Adicionado na versão 3.12.

int PyDict_Watch(int watcher_id, PyObject *dict)
    * Thread safety: Safe to call without external synchronization on
   distinct objects.*

   Marca o dicionário *dict* como observado. A função de retorno
   concedida a *watcher_id* por "PyDict_AddWatcher()" será chamada
   quando *dict* for modificado ou desalocado. Retorna "0" em caso de
   sucesso ou "-1" em caso de erro.

   Adicionado na versão 3.12.

int PyDict_Unwatch(int watcher_id, PyObject *dict)
    * Thread safety: Safe to call without external synchronization on
   distinct objects.*

   Marca o dicionário *dict* como não mais observado. A função de
   retorno concedida a *watcher_id* por "PyDict_AddWatcher()" será
   chamada quando *dict* for modificado ou desalocado. O dicionário
   deve ter sido observado anteriormente por este observador. Retorna
   "0" em caso de sucesso ou "-1" em caso de erro.

   Adicionado na versão 3.12.

type PyDict_WatchEvent

   Enumeração de possíveis eventos de observador de dicionário:
   "PyDict_EVENT_ADDED", "PyDict_EVENT_MODIFIED",
   "PyDict_EVENT_DELETED", "PyDict_EVENT_CLONED",
   "PyDict_EVENT_CLEARED" ou "PyDict_EVENT_DEALLOCATED".

   Adicionado na versão 3.12.

PY_FOREACH_DICT_EVENT(V)

   Apply the macro *V* to each suffix of "PyDict_WatchEvent"
   constants. Currently expands to "V(ADDED) V(MODIFIED) V(DELETED)
   V(CLONED) V(CLEARED) V(DEALLOCATED)". The macro *V* must accept one
   event name and supply any punctuation needed between expansions.

typedef int (*PyDict_WatchCallback)(PyDict_WatchEvent event, PyObject *dict, PyObject *key, PyObject *new_value)

   Tipo de uma função de retorno de chamada de observador de
   dicionário.

   Se *event* for "PyDict_EVENT_CLEARED" ou
   "PyDict_EVENT_DEALLOCATED", tanto *key* quanto *new_value* serão
   "NULL". Se *event* for "PyDict_EVENT_ADDED" ou
   "PyDict_EVENT_MODIFIED", *new_value* será o novo valor de *key*. Se
   *event* for "PyDict_EVENT_DELETED", *key* estará sendo excluída do
   dicionário e *new_value* será "NULL".

   "PyDict_EVENT_CLONED" ocorre quando *dict* estava anteriormente
   vazio e outro dict é mesclado a ele. Para manter a eficiência dessa
   operação, os eventos "PyDict_EVENT_ADDED" por chave não são
   emitidos nesse caso; em vez disso, um único "PyDict_EVENT_CLONED" é
   emitido e *key* será o dicionário de origem.

   A função de retorno pode inspecionar, mas não deve modificar o
   *dict*; isso pode ter efeitos imprevisíveis, inclusive recursão
   infinita. Não acione a execução do código Python na função de
   retorno, pois isso poderia modificar o dict como um efeito
   colateral.

   Se *event* for "PyDict_EVENT_DEALLOCATED", a obtenção de uma nova
   referência na função de retorno para o dicionário prestes a ser
   destruído o ressuscitará e impedirá que ele seja liberado nesse
   momento. Quando o objeto ressuscitado for destruído mais tarde,
   quaisquer funções de retorno do observador ativos naquele momento
   serão chamados novamente.

   As funções de retorno ocorrem antes que a modificação notificada no
   *dict* ocorra, de modo que o estado anterior do *dict* possa ser
   inspecionado.

   Se a função de retorno definir uma exceção, ela deverá retornar
   "-1". Essa exceção será exibida como uma exceção não levantável
   usando "PyErr_WriteUnraisable()". Caso contrário, deverá retornar
   "0".

   É possível que já exista uma exceção pendente definida na entrada
   da função de retorno. Nesse caso, a função de retorno deve retornar
   "0" com a mesma exceção ainda definida. Isso significa que a função
   de retorno não pode chamar nenhuma outra API que possa definir uma
   exceção, a menos que salve e limpe o estado da exceção primeiro e
   restaure a exceção antes de retornar.

   Adicionado na versão 3.12.


Objetos de visão de dicionário
==============================

int PyDictViewSet_Check(PyObject *op)

   Retorna verdadeiro se *op* for uma visão de um conjunto dentro de
   um dicionário. Isso atualmente equivale a PyDictKeys_Check(op) ||
   PyDictItems_Check(op). Esta função sempre tem sucesso.

PyTypeObject PyDictKeys_Type
    * Parte da ABI Estável.*

   Objeto tipo para uma visualização das chaves do dicionário. Em
   Python, este é o tipo do objeto retornado por "dict.keys()".

int PyDictKeys_Check(PyObject *op)

   Retorna verdadeiro se *op* for uma instância de uma visualização de
   chaves de dicionário. Esta função sempre tem sucesso.

PyTypeObject PyDictValues_Type
    * Parte da ABI Estável.*

   Objeto tipo para uma visualização dos valores do dicionário. Em
   Python, este é o tipo do objeto retornado por "dict.values()".

int PyDictValues_Check(PyObject *op)

   Retorna verdadeiro se *op* for uma instância de uma visualização de
   valores de dicionário. Esta função sempre tem sucesso.

PyTypeObject PyDictItems_Type
    * Parte da ABI Estável.*

   Objeto tipo para uma visualização de itens de dicionário. Em
   Python, este é o tipo do objeto retornado por "dict.items()".

int PyDictItems_Check(PyObject *op)

   Retorna verdadeiro se *op* for uma instância de uma visualização de
   itens de dicionário. Esta função sempre tem sucesso.


Frozen dictionary objects
=========================

Adicionado na versão 3.15.

PyTypeObject PyFrozenDict_Type

   This instance of "PyTypeObject" represents the Python frozen
   dictionary type. This is the same object as "frozendict" in the
   Python layer.

int PyAnyDict_Check(PyObject *p)

   Return true if *p* is a "dict" object, a "frozendict" object, or an
   instance of a subtype of the "dict" or "frozendict" type. This
   function always succeeds.

int PyAnyDict_CheckExact(PyObject *p)

   Return true if *p* is a "dict" object or a "frozendict" object, but
   not an instance of a subtype of the "dict" or "frozendict" type.
   This function always succeeds.

int PyFrozenDict_Check(PyObject *p)

   Return true if *p* is a "frozendict" object or an instance of a
   subtype of the "frozendict" type. This function always succeeds.

int PyFrozenDict_CheckExact(PyObject *p)

   Return true if *p* is a "frozendict" object, but not an instance of
   a subtype of the "frozendict" type. This function always succeeds.

PyObject *PyFrozenDict_New(PyObject *iterable)

   Return a new "frozendict" from an iterable, or "NULL" on failure
   with an exception set.

   Create an empty dictionary if *iterable* is "NULL".


Ordered dictionaries
====================

A API C do Python fornece uma interface para "collections.OrderedDict"
do C. Desde o Python 3.7, os dicionários são ordenados por padrão,
então geralmente há pouca necessidade dessas funções; prefira
"PyDict*" sempre que possível.

PyTypeObject PyODict_Type

   Objeto de tipo para dicionários ordenados. Este é o mesmo objeto
   que "collections.OrderedDict" na camada Python.

int PyODict_Check(PyObject *od)

   Retorna verdadeiro se *od* for um objeto de dicionário ordenado ou
   uma instância de um subtipo do tipo "OrderedDict". Esta função
   sempre tem sucesso..

int PyODict_CheckExact(PyObject *od)

   Retorna verdadeiro se *od* for um objeto de dicionário ordenado,
   mas não uma instância de um subtipo do tipo "OrderedDict". Esta
   função sempre tem sucesso.

PyTypeObject PyODictKeys_Type

   Análogo a "PyDictKeys_Type" para dicionários ordenados.

PyTypeObject PyODictValues_Type

   Análogo a "PyDictValues_Type" para dicionários ordenados.

PyTypeObject PyODictItems_Type

   Análogo a "PyDictItems_Type" para dicionários ordenados.

PyObject *PyODict_New(void)

   Retorna um novo dicionário ordenado vazio ou "NULL" em caso de
   falha.

   Isso é análogo a "PyDict_New()".

int PyODict_SetItem(PyObject *od, PyObject *key, PyObject *value)

   Insere o valor *value* no dicionário ordenado *od* com a chave de
   *key*. Retorna "0" em caso de sucesso ou "-1" com uma exceção
   definida em caso de falha.

   Isso é análogo a "PyDict_SetItem()".

int PyODict_DelItem(PyObject *od, PyObject *key)

   Remove a entrada do dicionário ordenado *od* com a chave *key*.
   Retorna "0" em caso de sucesso ou "-1" com uma exceção definida em
   caso de falha.

   Isso é análogo a "PyDict_DelItem()".

Estes são apelidos *suavemente descontinuados* a APIs de "PyDict":

+----------------------------------------------------+----------------------------------------------------+
| "PyODict"                                          | "PyDict"                                           |
|====================================================|====================================================|
| PyODict_GetItem(od, key)                           | "PyDict_GetItem()"                                 |
+----------------------------------------------------+----------------------------------------------------+
| PyODict_GetItemWithError(od, key)                  | "PyDict_GetItemWithError()"                        |
+----------------------------------------------------+----------------------------------------------------+
| PyODict_GetItemString(od, key)                     | "PyDict_GetItemString()"                           |
+----------------------------------------------------+----------------------------------------------------+
| PyODict_Contains(od, key)                          | "PyDict_Contains()"                                |
+----------------------------------------------------+----------------------------------------------------+
| PyODict_Size(od)                                   | "PyDict_Size()"                                    |
+----------------------------------------------------+----------------------------------------------------+
| PyODict_SIZE(od)                                   | "PyDict_GET_SIZE()"                                |
+----------------------------------------------------+----------------------------------------------------+
