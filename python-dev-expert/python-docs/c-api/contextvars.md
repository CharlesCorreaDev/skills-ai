Objetos de variáveis de contexto
********************************

Adicionado na versão 3.7.

Alterado na versão 3.7.1:

Nota:

  No Python 3.7.1, as assinaturas de todas as APIs C de variáveis de
  contexto foram **alteradas** para usar ponteiros "PyObject" em vez
  de "PyContext", "PyContextVar" e "PyContextToken". Por exemplo:

     // no 3.7.0:
     PyContext *PyContext_New(void);

     // no 3.7.1+:
     PyObject *PyContext_New(void);

  Veja bpo-34762 para mais detalhes.

Esta seção detalha a API C pública para o módulo "contextvars".

type PyContext

   A estrutura C usada para representar um objeto
   "contextvars.Context".

type PyContextVar

   A estrutura C usada para representar um objeto
   "contextvars.ContextVar".

type PyContextToken

   A estrutura C usada para representar um objeto "contextvars.Token"

PyTypeObject PyContext_Type

   O objeto de tipo que representa o tipo de *contexto*.

PyTypeObject PyContextVar_Type

   O objeto de tipo que representa o tipo de *variável de contexto*.

PyTypeObject PyContextToken_Type

   O objeto de tipo que representa o tipo de *token de variável de
   contexto*.

Macros de verificação de tipo:

int PyContext_CheckExact(PyObject *o)

   Retorna verdadeiro se *o* for do tipo "PyContext_Type". *o* não
   deve ser "NULL". Esta função sempre tem sucesso.

int PyContextVar_CheckExact(PyObject *o)

   Retorna verdadeiro se *o* for do tipo "PyContextVar_Type". *o* não
   deve ser "NULL". Esta função sempre tem sucesso.

int PyContextToken_CheckExact(PyObject *o)

   Retorna verdadeiro se *o* for do tipo "PyContextToken_Type". *o*
   não deve ser "NULL". Esta função sempre tem sucesso.

Funções de gerenciamento de objetos de contexto:

PyObject *PyContext_New(void)
    *Retorna valor: Nova referência.*

   Cria um novo objeto de contexto vazio. Retorna "NULL" se um erro
   ocorreu.

PyObject *PyContext_Copy(PyObject *ctx)
    *Retorna valor: Nova referência.*

   Cria uma cópia rasa do objeto de contexto *ctx* passado. Retorna
   "NULL" se um erro ocorreu.

PyObject *PyContext_CopyCurrent(void)
    *Retorna valor: Nova referência.*

   Cria uma cópia rasa do contexto da thread atual. Retorna "NULL" se
   um erro ocorreu.

int PyContext_Enter(PyObject *ctx)

   Defina *ctx* como o contexto atual para o thread atual. Retorna "0"
   em caso de sucesso e "-1" em caso de erro.

int PyContext_Exit(PyObject *ctx)

   Desativa  o contexto *ctx* e restaura o contexto anterior como o
   contexto atual para a thread atual. Retorna "0" em caso de sucesso
   e "-1" em caso de erro.

int PyContext_AddWatcher(PyContext_WatchCallback callback)

   Registra *callback* como um observador do objeto contexto para o
   interpretador atual.  Devolve um ID que pode ser passado para
   "PyContext_ClearWatcher()". Em caso de erro (por exemplo, não há
   IDs de observadores disponíveis), devolve "-1" e define uma
   exceção.

   Adicionado na versão 3.14.

int PyContext_ClearWatcher(int watcher_id)

   Libera o observador identificado por *watcher_id* anteriormente
   retornado por "PyContext_AddWatcher()" para o interpretador atual.
   Retorna "0" em caso de sucesso ou "-1" em caso de erro e levanta
   uma exceção (ex., se o *watcher_id* dado não foi registrado.)

   Adicionado na versão 3.14.

type PyContextEvent

   Enumeração de possíveis eventos do observador de objeto contexto:

   * "Py_CONTEXT_SWITCHED": O *contexto atual* foi alternado para um
     contexto diferente. O objeto passado para o retorno de chamada de
     observação é o objeto "contextvars.Context", que está atualmente
     em uso, ou None se não houver contexto atual.

   Adicionado na versão 3.14.

typedef int (*PyContext_WatchCallback)(PyContextEvent event, PyObject *obj)

   Função de retorno de chamada do observador de objetos contexto. O
   objeto passado para o retorno de chamada é específico do evento;
   consulte "PyContextEvent" para obter detalhes.

   Se o retorno de chamada retornar com uma exceção definida, ele
   deverá retornar "-1"; essa exceção será impressa como uma exceção
   não levantável usando "PyErr_FormatUnraisable()". Caso contrário,
   deverá retornar "0".

   É possível que já exista uma exceção pendente definida na entrada
   da função de retorno. Nesse caso, a função de retorno deve retornar
   "0" com a mesma exceção ainda definida. Isso significa que a função
   de retorno não pode chamar nenhuma outra API que possa definir uma
   exceção, a menos que salve e limpe o estado da exceção primeiro e
   restaure a exceção antes de retornar.

   Adicionado na versão 3.14.

Funções de variável de contexto:

PyObject *PyContextVar_New(const char *name, PyObject *def)
    *Retorna valor: Nova referência.*

   Cria um novo objeto "ContextVar". O parâmetro *name* é usado para
   fins de introspecção e depuração. O parâmetro *def* especifica um
   valor padrão para a variável de contexto, ou  "NULL" para nenhum
   padrão. Se ocorrer um erro, esta função retorna "NULL".

int PyContextVar_Get(PyObject *var, PyObject *default_value, PyObject **value)

   Obtém o valor de uma variável de contexto. Retorna "-1" se um erro
   ocorreu durante a pesquisa, e "0" se nenhum erro ocorreu, se um
   valor foi encontrado ou não.

   Se a variável de contexto foi encontrada, *value* será um ponteiro
   para ela. Se a variável de contexto *não* foi encontrada, *value*
   apontará para:

   * *default_value*, se não for "NULL";

   * o valor padrão de *var*, se não for "NULL";

   * "NULL"

   Exceto para "NULL", a função retorna uma nova referência.

PyObject *PyContextVar_Set(PyObject *var, PyObject *value)
    *Retorna valor: Nova referência.*

   Define o valor de *var* como *value* no contexto atual. Retorna um
   novo objeto token para esta alteração, ou "NULL" se um erro
   ocorreu.

int PyContextVar_Reset(PyObject *var, PyObject *token)

   Redefine o estado da variável de contexto *var* para o estado que
   anterior a "PyContextVar_Set()" que retornou o *token* foi chamado.
   Esta função retorna "0" em caso de sucesso e "-1" em caso de erro.
