Extensão
********

A direção principal para estender o módulo "asyncio" é escrever
classes de *laços de eventos* personalizados. O Asyncio tem funções
auxiliares que podem ser usadas para simplificar essa tarefa.

Nota:

  Third-parties should reuse existing asyncio code with caution, a new
  Python version is free to break backward compatibility in the
  *internal* part of the API.


Writing a custom event loop
===========================

"asyncio.AbstractEventLoop" declares very many methods. See Event loop
methods for the full list. Implementing them all from scratch is a
tedious job.

Um laço de eventos pode herdar várias implementações de métodos da
classe "asyncio.BaseEventLoop".

Por sua vez, o sucessor deve implementar um conjunto de métodos
*privados* declarados, porém não implementados, em
"asyncio.BaseEventLoop".

Por exemplo, "loop.create_connection()``verifica os argumentos,
resolve endereços DNS, e chama a função
``loop._make_socket_transport()", que deve ser implementada pela
classe herdada. O método``_make_socket_transport()`` não está
documentado, e é considerado parte de uma API *interna*.


Construtores privados de Future e Task
======================================

As classes "asyncio.Future" e "asyncio.Task" nunca deverão ser criadas
diretamente. Por favor, as substitua pelas *factories*
correspondentes: "loop.create_future()" e "loop.create_task()" ou
"asyncio.create_task()".

Porém, *laços de eventos* de terceiros podem *reutilizar* as
implementações embutidas de Future e Task, obtendo um código complexo
e altamente otimizado.

Por isso, segue a listagem de construtores *privados*:

Future.__init__(*, loop=None)

   Cria uma instância de Future embutida.

   *loop* é uma instância opcional do laço de eventos.

Task.__init__(coro, *, loop=None, name=None, context=None)

   Cria uma instância embutida de Task.

   *loop* é uma instância opcional do laço de eventos. Os outros
   argumentos estão descritos em "loop.create_task()".

   Alterado na versão 3.11: o argumento *context* foi adicionado


Suporte ao ciclo de vida de tarefas
===================================

Implementações de Task de terceiros devem chamar as seguintes funções
para manter uma tarefa visível para "asyncio.all_tasks()" e
"asyncio.current_task()":

asyncio._register_task(task)

   Registra uma nova *task* como gerenciada pelo *asyncio*.

   Chame esta função no construtor de uma tarefa.

asyncio._unregister_task(task)

   Cancela o registro de *task* nas estruturas internas do *asyncio*.

   Chame esta função quando a tarefa estiver terminando.

asyncio._enter_task(loop, task)

   Troca a tarefa atual para o argumento *task*.

   Chame esta função logo antes de executar uma porção da *corrotina*
   embutida ("coroutine.send()" ou "coroutine.throw()").

asyncio._leave_task(loop, task)

   Troca a tarefa atual de *task* para "None".

   Chame esta função logo após executar "coroutine.send()" ou
   "coroutine.throw()".
