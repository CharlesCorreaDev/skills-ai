API C de monitoramento
**********************

Adicionada na versão 3.13.

Uma extensão pode precisar interagir com o sistema de monitoramento de
eventos. É possível registrar funções de retorno e se inscrever para
receber eventos através da API Python exposta em "sys.monitoring".


Gerando eventos de execução
***************************

As funções abaixo permitem que extensões dispararem eventos de
monitoramento emulando a execução de código Python. Cada uma dessas
funções recebe uma estrutura "PyMonitoringState" que contém informação
concisa sobre o estado de ativação de eventos, bem como os argumentos
dos eventos, que incluem um "PyObject*" representando o objeto de
código, a posição da instrução no bytecode, e, em alguns casos,
argumentos adicionais específicos para o evento (veja "sys.monitoring"
para detalhes sobre as assinaturas das funções de retorno de
diferentes eventos). O argumento "codelike" deve ser uma instância da
classe "types.CodeType" ou de um tipo que a emule.

A VM desabilita o rastreamento quando dispara um evento, de forma que
não há necessidade do código do usuário fazer isso.

Funções de monitoramento não devem ser chamadas com uma exceção
definida, exceto as marcadas abaixo como funções que trabalham com a
exceção atual.

type PyMonitoringState

   Representação do estado de um tipo de evento. Alocada pelo usuário,
   enquanto o seu conteúdo é mantido pelas funções da API de
   monitoramento descritas abaixo.

Todas as funções abaixo retornam 0 para indicar sucesso e -1 (com uma
exceção definida) para indicar erro.

Veja "sys.monitoring" para descrições dos eventos.

int PyMonitoring_FirePyStartEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset)

   Dispara um evento "PY_START".

int PyMonitoring_FirePyResumeEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset)

   Dispara um evento "PY_RESUME".

int PyMonitoring_FirePyReturnEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, PyObject *retval)

   Dispara um evento "PY_RETURN".

int PyMonitoring_FirePyYieldEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, PyObject *retval)

   Dispara um evento "PY_YIELD".

int PyMonitoring_FireCallEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, PyObject *callable, PyObject *arg0)

   Dispara um evento "CALL".

int PyMonitoring_FireLineEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, int lineno)

   Dispara um evento "LINE".

int PyMonitoring_FireJumpEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, PyObject *target_offset)

   Dispara um evento "JUMP".

int PyMonitoring_FireBranchLeftEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, PyObject *target_offset)

   Dispara um evento "BRANCH_LEFT".

int PyMonitoring_FireBranchRightEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, PyObject *target_offset)

   Dispara um evento "BRANCH_RIGHT".

int PyMonitoring_FireCReturnEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, PyObject *retval)

   Dispara um evento "C_RETURN".

int PyMonitoring_FirePyThrowEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset)

   Dispara um evento "PY_THROW" com a exceção atual (conforme
   retornada por "PyErr_GetRaisedException()").

int PyMonitoring_FireRaiseEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset)

   Dispara um evento "RAISE" com a exceção atual (conforme retornada
   por "PyErr_GetRaisedException()").

int PyMonitoring_FireCRaiseEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset)

   Dispara um evento "C_RAISE" com a exceção atual (conforme retornada
   por "PyErr_GetRaisedException()").

int PyMonitoring_FireReraiseEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset)

   Dispara um evento "RERAISE" com a exceção atual (conforme retornada
   por "PyErr_GetRaisedException()").

int PyMonitoring_FireExceptionHandledEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset)

   Dispara um evento "EXCEPTION_HANDLED" com a exceção atual (conforme
   retornada por "PyErr_GetRaisedException()").

int PyMonitoring_FirePyUnwindEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset)

   Dispara um evento "PY_UNWIND" com a exceção atual (conforme
   retornada por "PyErr_GetRaisedException()").

int PyMonitoring_FireStopIterationEvent(PyMonitoringState *state, PyObject *codelike, int32_t offset, PyObject *value)

   Dispara um evento "STOP_ITERATION". Se "value" for uma instância de
   "StopIteration", ele é usado. Caso contrário, uma nova instância de
   "StopIteration" é criada com "value" como o argumento.


Gerenciando o Estado de um Monitoramento
========================================

Estados de monitoramento podem ser gerenciados com a ajuda de escopos
de monitoramento. Um escopo corresponderia tipicamente a um função
Python.

int PyMonitoring_EnterScope(PyMonitoringState *state_array, uint64_t *version, const uint8_t *event_types, Py_ssize_t length)

   Insere um escopo monitorado. "event_types" é um vetor de IDs de
   eventos para eventos que podem ser disparados do escopo. Por
   exemplo, a ID de um evento "PY_START" é o valor
   "PY_MONITORING_EVENT_PY_START", que é numericamente igual ao
   logaritmo de base 2 de "sys.monitoring.events.PY_START".
   "state_array" é um vetor com uma entrada de estado de monitoramento
   para cada evento em "event_types", é alocado pelo usuário, mas
   preenchido por "PyMonitoring_EnterScope()" com informações sobre o
   estado de ativação do evento. O tamanho de "event_types" (e,
   portanto, também de "state_array") é fornecido em "length".

   O argumento "version" é um ponteiro para um valor que deve ser
   alocado pelo usuário junto com "state_array" e inicializado como 0,
   e então definido somente pelo próprio "PyMonitoring_EnterScope()".
   Ele permite que esta função determine se os estados de eventos
   mudaram desde a chamada anterior, e retorne rapidamente se não
   mudaram.

   Os escopos mencionados aqui são escopos lexicais: uma função,
   classe ou método. "PyMonitoring_EnterScope()" deve ser chamada
   sempre que o escopo lexical for inserido. Os escopos podem ser
   inseridos novamente, reutilizando o mesmo *state_array* e
   *version*, em situações como ao emular uma função Python recursiva.
   Quando a execução de um código semelhante é pausada, como ao emular
   um gerador, o escopo precisa ser encerrado e inserido novamente.

   As macros para *event_types* são:

   +----------------------------------------------------+---------------------------------------+
   | Macro                                              | Evento                                |
   |====================================================|=======================================|
   | PY_MONITORING_EVENT_BRANCH_LEFT                    | "BRANCH_LEFT"                         |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_BRANCH_RIGHT                   | "BRANCH_RIGHT"                        |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_CALL                           | "CALL"                                |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_C_RAISE                        | "C_RAISE"                             |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_C_RETURN                       | "C_RETURN"                            |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_EXCEPTION_HANDLED              | "EXCEPTION_HANDLED"                   |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_INSTRUCTION                    | "INSTRUCTION"                         |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_JUMP                           | "JUMP"                                |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_LINE                           | "LINE"                                |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_PY_RESUME                      | "PY_RESUME"                           |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_PY_RETURN                      | "PY_RETURN"                           |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_PY_START                       | "PY_START"                            |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_PY_THROW                       | "PY_THROW"                            |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_PY_UNWIND                      | "PY_UNWIND"                           |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_PY_YIELD                       | "PY_YIELD"                            |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_RAISE                          | "RAISE"                               |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_RERAISE                        | "RERAISE"                             |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_STOP_ITERATION                 | "STOP_ITERATION"                      |
   +----------------------------------------------------+---------------------------------------+
   | PY_MONITORING_EVENT_BRANCH  Descontinuado desde a  | "BRANCH_LEFT" e "BRANCH_RIGHT"        |
   | versão 3.14: Use "PY_MONITORING_EVENT_BRANCH_LEFT" |                                       |
   | e "PY_MONITORING_EVENT_BRANCH_RIGHT".              |                                       |
   +----------------------------------------------------+---------------------------------------+

int PyMonitoring_ExitScope(void)

   Sai do último escopo no qual se entrou com
   "PyMonitoring_EnterScope()".

int PY_MONITORING_IS_INSTRUMENTED_EVENT(uint8_t ev)

   Retorna verdadeiro se o evento correspondente ao ID do evento *ev*
   for um evento local.

   Adicionado na versão 3.13.

   Suavemente descontinuado desde a versão 3.14.
