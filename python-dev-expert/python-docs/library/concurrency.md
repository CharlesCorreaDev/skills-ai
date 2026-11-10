Execução Concorrente
********************

Os módulos descritos neste capítulo fornecem suporte a execução
simultânea de código. A escolha apropriada da ferramenta dependerá da
tarefa a ser executada (CPU bound ou IO bound) e do estilo de
desenvolvimento preferencial (multitarefa cooperativa orientada a
eventos versus multitarefa preemptiva). Eis uma visão geral:

* "threading" --- Paralelismo baseado em threads

  * Introdução

  * GIL and performance considerations

  * Referência

    * Thread-local data

    * Thread objects

    * Lock objects

    * RLock objects

    * Condition objects

    * Semaphore objects

    * "Semaphore" example

    * Event objects

    * Timer objects

    * Barrier objects

  * Using locks, conditions, and semaphores in the "with" statement

  * Iterator synchronization

* "multiprocessing" --- Paralelismo baseado em processo

  * Introdução

    * A classe "Process"

    * Contextos e métodos de inicialização

    * Trocando objetos entre processos

    * Sincronização entre processos

    * Compartilhando estado entre processos

    * Usando um pool de workers

  * Referência

    * Global start method

    * "Process" e exceções

    * Encadeamentos e filas

    * Diversos

    * Objetos de conexão

    * Primitivas de sincronização

    * Objetos "ctypes" compartilhados

      * The "multiprocessing.sharedctypes" module

    * Gerenciadores

      * Customized managers

      * Using a remote manager

    * Objetos proxies

      * Limpeza

    * Process Pools

    * Listeners and Clients

      * Formatos de Endereços

    * Authentication keys

    * Gerando logs

    * The "multiprocessing.dummy" module

  * Programming guidelines

    * All start methods

    * The *spawn* and *forkserver* start methods

  * Exemplos

* "multiprocessing.shared_memory" --- Memória compartilhada para
  acesso direto entre processos

* O pacote "concurrent"

* "concurrent.futures" --- Launching parallel tasks

  * Executor Objects

  * ThreadPoolExecutor

    * Exemplo de ThreadPoolExecutor

  * InterpreterPoolExecutor

  * ProcessPoolExecutor

    * ProcessPoolExecutor Example

  * Future Objects

  * Module Functions

  * Exception classes

* "concurrent.interpreters" --- Múltiplos interpretadores no mesmo
  processo

  * Detalhes chaves

  * Introdução

    * Multiple Interpreters and Isolation

    * Running in an Interpreter

    * Concurrency and Parallelism

    * Communication Between Interpreters

    * "Sharing" Objects

  * Referência

    * Objetos interpretador

    * Exceções

    * Communicating Between Interpreters

  * Uso básico

* "subprocess" --- Gerenciamento de subprocessos

  * Using the "subprocess" Module

    * Argumentos usados frequentemente

    * Construtor Popen

    * Exceções

  * Considerações de Segurança

  * Objetos Popen

  * Windows Popen Helpers

    * Constantes do Windows

  * API de alto nível mais antiga

  * Replacing Older Functions with the "subprocess" Module

    * Replacing **/bin/sh** shell command substitution

    * Replacing shell pipeline

    * Substituindo "os.system()"

    * Replacing the "os.spawn" family

    * Replacing "os.popen()"

  * Legacy Shell Invocation Functions

  * Notas

    * Timeout Behavior

    * Converter uma sequência de argumentos em uma string no Windows

    * Disable use of "posix_spawn()"

* "sched" --- Agendador de eventos

  * Objetos Scheduler

* "queue" --- Uma classe de fila sincronizada

  * Objetos Queue

    * Waiting for task completion

    * Terminating queues

  * Objetos SimpleQueue

* "contextvars" --- Variáveis de contexto

  * Variáveis de contexto

  * Gerenciamento de contexto manual

  * Suporte a asyncio

A seguir, os módulos de suporte para alguns dos serviços acima:

* "_thread"--- API de segmentação de baixo nível
