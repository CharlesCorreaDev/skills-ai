Índice da API de alto nível
***************************

Esta página lista todas as APIs asyncio de alto nível habilitadas por
async/await.


Tarefas
=======

Utilitários para executar programas asyncio, criar Tarefas, e esperar
por múltiplas coisas com tempos limites.

+----------------------------------------------------+----------------------------------------------------+
| "run()"                                            | Cria um laço de eventos, roda uma corrotina, fecha |
|                                                    | o laço.                                            |
+----------------------------------------------------+----------------------------------------------------+
| "Runner"                                           | Um gerenciador de contexto que simplifica várias   |
|                                                    | chamadas assíncronas de funções.                   |
+----------------------------------------------------+----------------------------------------------------+
| "Task"                                             | Objeto Task.                                       |
+----------------------------------------------------+----------------------------------------------------+
| "TaskGroup"                                        | Um gerenciador de contexto que mantém um grupo de  |
|                                                    | tarefas. Oferece uma maneira conveniente e         |
|                                                    | confiável de aguardar a conclusão de todas as      |
|                                                    | tarefas do grupo.                                  |
+----------------------------------------------------+----------------------------------------------------+
| "create_task()"                                    | Inicia uma Task asyncio e a retorna.               |
+----------------------------------------------------+----------------------------------------------------+
| "current_task()"                                   | Retorna para a Tarefa atual.                       |
+----------------------------------------------------+----------------------------------------------------+
| "all_tasks()"                                      | Retorna todas as tarefas que ainda não foram       |
|                                                    | concluídas em um laço de eventos.                  |
+----------------------------------------------------+----------------------------------------------------+
| "await" "sleep()"                                  | Dorme for um número de segundos.                   |
+----------------------------------------------------+----------------------------------------------------+
| "await" "gather()"                                 | Agenda e espera por coisas concorrentemente.       |
+----------------------------------------------------+----------------------------------------------------+
| "await" "wait_for()"                               | Executa com um tempo limite.                       |
+----------------------------------------------------+----------------------------------------------------+
| "await" "shield()"                                 | Protege contra cancelamento.                       |
+----------------------------------------------------+----------------------------------------------------+
| "await" "wait()"                                   | Monitora para conclusão.                           |
+----------------------------------------------------+----------------------------------------------------+
| "timeout()"                                        | Executa com um tempo limite. Útil nos casos em que |
|                                                    | o "wait_for" não é adequado.                       |
+----------------------------------------------------+----------------------------------------------------+
| "to_thread()"                                      | Executa uma função assincronamente em uma thread   |
|                                                    | separada.                                          |
+----------------------------------------------------+----------------------------------------------------+
| "run_coroutine_threadsafe()"                       | Agenda uma corrotina a partir de outra thread do   |
|                                                    | sistema operacional.                               |
+----------------------------------------------------+----------------------------------------------------+
| "for in" "as_completed()"                          | Monitora a conclusão com um loop "for".            |
+----------------------------------------------------+----------------------------------------------------+

-[ Exemplos ]-

* Usando asyncio.gather() para executar coisas em paralelo.

* Usando asyncio.wait_for() para forçar um tempo limite de execução.

* Cancelamento.

* Usando asyncio.sleep().

* Veja também a página principal de documentação sobre Tarefas.


Filas
=====

Filas devem ser usadas para distribuir trabalho entre múltiplas
Tarefas asyncio, implementar pools de conexão, e padrões pub/sub.

+----------------------------------------------------+----------------------------------------------------+
| "Queue"                                            | Uma fila FIFO - Primeiro que entra, é o primeiro   |
|                                                    | que sai.                                           |
+----------------------------------------------------+----------------------------------------------------+
| "PriorityQueue"                                    | Uma fila de prioridade.                            |
+----------------------------------------------------+----------------------------------------------------+
| "LifoQueue"                                        | Uma fila LIFO - Último que entra, é o primeiro que |
|                                                    | sai.                                               |
+----------------------------------------------------+----------------------------------------------------+

-[ Exemplos ]-

* Usando asyncio.Queue para distribuir cargas de trabalho entre
  diversas Tasks.

* Veja também a Página de documentação da classe Queue.


Subprocessos
============

Utilitários para iniciar subprocessos e executar comandos no console.

+----------------------------------------------------+----------------------------------------------------+
| "await" "create_subprocess_exec()"                 | Cria um subprocesso.                               |
+----------------------------------------------------+----------------------------------------------------+
| "await" "create_subprocess_shell()"                | Executa um comando no console.                     |
+----------------------------------------------------+----------------------------------------------------+

-[ Exemplos ]-

* Executando um comando no console.

* Veja também a documentação de subprocessos de APIs.


Streams
=======

APIs de alto nível para trabalhar com entrada e saída de rede.

+----------------------------------------------------+----------------------------------------------------+
| "await" "open_connection()"                        | Estabelece uma conexão TCP.                        |
+----------------------------------------------------+----------------------------------------------------+
| "await" "open_unix_connection()"                   | Estabelece uma conexão com soquete Unix.           |
+----------------------------------------------------+----------------------------------------------------+
| "await" "start_server()"                           | Inicia um servidor TCP.                            |
+----------------------------------------------------+----------------------------------------------------+
| "await" "start_unix_server()"                      | Inicia um servidor com soquete Unix.               |
+----------------------------------------------------+----------------------------------------------------+
| "StreamReader"                                     | Objeto async/await de alto nível para receber      |
|                                                    | dados de rede.                                     |
+----------------------------------------------------+----------------------------------------------------+
| "StreamWriter"                                     | Objeto async/await de alto nível para enviar dados |
|                                                    | pela rede.                                         |
+----------------------------------------------------+----------------------------------------------------+

-[ Exemplos ]-

* Exemplo de cliente TCP.

* Veja também a documentação das APIs de streams.


Sincronização
=============

Primitivas de sincronização similares a threads, que podem ser usadas
em tarefas.

+----------------------------------------------------+----------------------------------------------------+
| "Lock"                                             | Uma trava mutex.                                   |
+----------------------------------------------------+----------------------------------------------------+
| "Event"                                            | Um objeto de evento.                               |
+----------------------------------------------------+----------------------------------------------------+
| "Condition"                                        | Um objeto de condição.                             |
+----------------------------------------------------+----------------------------------------------------+
| "Semaphore"                                        | Um semáforo.                                       |
+----------------------------------------------------+----------------------------------------------------+
| "BoundedSemaphore"                                 | Um semáforo limitado.                              |
+----------------------------------------------------+----------------------------------------------------+
| "Barrier"                                          | Um objeto barreira.                                |
+----------------------------------------------------+----------------------------------------------------+

-[ Exemplos ]-

* Usando asyncio.Event.

* Usando asyncio.Barrier.

* Veja também a documentação das primitivas de sincronização de
  asyncio.


Exceções
========

+----------------------------------------------------+----------------------------------------------------+
| "asyncio.CancelledError"                           | Levantado quanto a Tarefa é cancelada. Veja também |
|                                                    | "Task.cancel()".                                   |
+----------------------------------------------------+----------------------------------------------------+
| "asyncio.BrokenBarrierError"                       | Levantado quando um Barreira é quebrada. veja      |
|                                                    | também "Barrier.wait()" .                          |
+----------------------------------------------------+----------------------------------------------------+

-[ Exemplos ]-

* Manipulando CancelledError para executar código no cancelamento de
  uma requisição.

* Veja também a lista completa de exceções específicas de asyncio.
