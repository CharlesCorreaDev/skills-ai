Objetos Função
**************

Existem algumas funções específicas para as funções do Python.

type PyFunctionObject

   A estrutura C usada para funções.

   In the free-threaded build, direct access to mutable fields
   requires synchronization if another thread may modify the function.
   See Suporte a extensões da API C para threads livres.

PyTypeObject PyFunction_Type

   Esta é uma instância de "PyTypeObject" e representa o tipo de
   função Python. Está exposta a programadores Python como
   "types.FunctionType".

int PyFunction_Check(PyObject *o)

   Retorna verdadeiro se *o* for um objeto função (tem tipo
   "PyFunction_Type"). O parâmetro não deve ser "NULL". Esta função
   sempre obtém sucesso.

PyObject *PyFunction_New(PyObject *code, PyObject *globals)
    *Retorna valor: Nova referência.*

   Retorna um novo objeto função associado ao objeto código *code*.
   *globals* deve ser um dicionário com as variáveis globais
   acessíveis à função.

   O nome e *docstring* da função são adquiridos pelo objeto código. O
   atributo "__module__" é adquirido por meio de *globals*. Os
   valores-padrão de argumentos, anotações, e fechamento são definidos
   como "NULL". O atributo "__qualname__" é definido com o mesmo valor
   do campo "co_qualname" de um objeto código.

PyObject *PyFunction_NewWithQualName(PyObject *code, PyObject *globals, PyObject *qualname)
    *Retorna valor: Nova referência.*

   Similar a "PyFunction_New()", mas também permite definir o atributo
   "__qualname__" do objeto função. *qualname* deve ser um objeto
   Unicode ou "NULL". Se "NULL", o atributo "__qualname__" é definido
   com o mesmo valor do campo "co_qualname" do objeto código.

   Adicionado na versão 3.3.

PyObject *PyFunction_GetCode(PyObject *op)
    *Retorna valor: Referência emprestada.*

   Retorna o objeto código associado ao objeto função *op*.

PyObject *PyFunction_GetGlobals(PyObject *op)
    *Retorna valor: Referência emprestada.*

   Retorna o dicionário global associado ao objeto função *op*.

PyObject *PyFunction_GetModule(PyObject *op)
    *Retorna valor: Referência emprestada.*

   Retorna uma *referência emprestada* ao atributo "__module__" do
   objeto função *op*. Pode ser *NULL*.

   Normalmente, trata-se de um "string" contendo o nome do módulo, mas
   pode ser definido como qualquer outro objeto pelo código Python.

   In the free-threaded build, if the attribute may be modified
   concurrently, convert the borrowed reference to a strong reference
   with "Py_XNewRef()" immediately, before calling any other Python
   API. The same applies to "PyFunction_GET_MODULE()".

PyObject *PyFunction_GetDefaults(PyObject *op)
    *Retorna valor: Referência emprestada.*

   Retorna os valores-padrão de argumentos do objeto função *op*. Pode
   ser uma tupla de argumentos ou "NULL".

int PyFunction_SetDefaults(PyObject *op, PyObject *defaults)

   Define os valores-padrão dos argumentos do objeto função *op*.
   *defaults* deve ser "Py_None" ou uma tupla.

   Levanta "SystemError" e retorna "-1" em caso de falha.

void PyFunction_SetVectorcall(PyFunctionObject *func, vectorcallfunc vectorcall)

   Define o campo *vectorcall* de um objeto função *func*.

   Atenção: extensões que usam essa API devem preservar o
   comportamento inalterado (padrão) de uma função *vectorcall*!

   Adicionado na versão 3.12.

PyObject *PyFunction_GetKwDefaults(PyObject *op)
    *Retorna valor: Referência emprestada.*

   Retorna os valores-padrão de argumentos somente-nomeados do objeto
   função *op*. Pode ser um dicionário de argumentos ou "NULL".

int PyFunction_SetKwDefaults(PyObject *op, PyObject *defaults)

   Define os valores padrão dos argumentos somente-nomeados do objeto
   função *op*. *defaults* deve ser um dicionário de argumentos
   somente-nomeados ou "Py_None".

   Esta função retorna "0" em caso de sucesso e retorna "-1" com uma
   exceção definida em caso de falha.

PyObject *PyFunction_GetClosure(PyObject *op)
    *Retorna valor: Referência emprestada.*

   Retorna o fechamento associado ao objeto função *op*. Pode ser
   "NULL" ou uma tupla de objetos célula.

int PyFunction_SetClosure(PyObject *op, PyObject *closure)

   Define o fechamento associado ao objeto função *op*. *closure* deve
   ser "Py_None" ou uma tupla de objetos de célula.

   Levanta "SystemError" e retorna "-1" em caso de falha.

PyObject *PyFunction_GetAnnotations(PyObject *op)
    *Retorna valor: Referência emprestada.*

   Retorna as anotações do objeto função *op*. Este pode ser um
   dicionário mutável ou "NULL".

int PyFunction_SetAnnotations(PyObject *op, PyObject *annotations)

   Define as anotações para o objeto função *op*. *annotations* deve
   ser um dicionário ou "Py_None".

   Levanta "SystemError" e retorna "-1" em caso de falha.

PyObject *PyFunction_GET_CODE(PyObject *op)
PyObject *PyFunction_GET_GLOBALS(PyObject *op)
PyObject *PyFunction_GET_MODULE(PyObject *op)
PyObject *PyFunction_GET_DEFAULTS(PyObject *op)
PyObject *PyFunction_GET_KW_DEFAULTS(PyObject *op)
PyObject *PyFunction_GET_CLOSURE(PyObject *op)
PyObject *PyFunction_GET_ANNOTATIONS(PyObject *op)
    *Retorna valor: Referência emprestada.*

   Essas funções são semelhantes às suas contrapartes
   "PyFunction_Get*", mas não realizam verificação de tipos. Passar
   qualquer coisa que não seja uma instância de "PyFunction_Type" é um
   comportamento indefinido.

int PyFunction_AddWatcher(PyFunction_WatchCallback callback)

   Registra *callback* como uma sentinela de função para o
   interpretador atual. Retorna um ID que pode ser passado para
   "PyFunction_ClearWatcher()". Em caso de erro (por exemplo, sem
   novos IDs de sentinelas disponíveis), retorna "-1" e define uma
   exceção.

   Adicionado na versão 3.12.

int PyFunction_ClearWatcher(int watcher_id)

   Cancela o registro da sentinela identificada pelo *watcher_id*
   retornado por "PyFunction_AddWatcher()" para o interpretador atual.
   Retorna "0" em caso de sucesso, ou "-1" e define uma exceção em
   caso de erro (por exemplo, ao receber um *watcher_id*
   desconhecido.)

   Adicionado na versão 3.12.

type PyFunction_WatchEvent

      Enumeração de possíveis eventos do observador de funções:

      * "PyFunction_EVENT_CREATE"

      * "PyFunction_EVENT_DESTROY"

      * "PyFunction_EVENT_MODIFY_CODE"

      * "PyFunction_EVENT_MODIFY_DEFAULTS"

      * "PyFunction_EVENT_MODIFY_KWDEFAULTS"

   Adicionado na versão 3.12:

   * "PyFunction_EVENT_MODIFY_QUALNAME"

   Adicionado na versão 3.15.

PY_FOREACH_FUNC_EVENT(V)

   Aplica a macro *V* a cada sufixo das constantes
   "PyFunction_WatchEvent". Atualmente, ela se expande para "V(CREATE)
   V(DESTROY) V(MODIFY_CODE) V(MODIFY_DEFAULTS) V(MODIFY_KWDEFAULTS)
   V(MODIFY_QUALNAME)". A macro *V* deve aceitar um nome de evento e
   fornecer a pontuação necessária entre as expansões.

typedef int (*PyFunction_WatchCallback)(PyFunction_WatchEvent event, PyFunctionObject *func, PyObject *new_value)

   Tipo de uma função de retorno de sentinela de função.

   Se *event* for "PyFunction_EVENT_CREATE" ou
   "PyFunction_EVENT_DESTROY", *new_value* será "NULL". Senão,
   *new_value* portará uma *referência emprestada* ao novo valor
   prestes a ser guardado em *func* para o atributo que está sendo
   modificado.

   A função de retorno poderá somente inspecionar, e não modificar
   *func*. Caso contrário, poderíamos ter efeitos imprevisíveis,
   incluindo recursão infinita.

   Se *event* for "PyFunction_EVENT_CREATE", a função de retorno será
   invocada após *func* ter sido completamente inicializada. Caso
   contrário, a função de retorno será invocada antes de modificar
   *func*, então o estado anterior de *func* poderá ser inspecionado.
   O ambiente de execução pode otimizar a criação de objetos função,
   quando possível, ao ignorá-las. Nesses casos, nenhum evento será
   emitido. Apesar de decisões de otimização criarem diferenças de
   comportamento em tempo de execução, elas não mudam a semântica do
   código Python sendo executado.

   Se *event* for "PyFunction_EVENT_DESTROY", então obter uma
   referência dentro da função de retorno para a função prestes a ser
   destruída irá revivê-la, impedindo que esta função seja liberada
   nesse tempo. Quando o objeto revivido for destruído, quaisquer
   funções de retorno sentinelas ativas nesse momento poderão ser
   chamadas novamente.

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
