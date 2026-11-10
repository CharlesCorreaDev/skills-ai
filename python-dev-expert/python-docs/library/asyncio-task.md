Coroutines and tasks
********************

Esta seção descreve APIs assíncronas de alto nível para trabalhar com
corrotinas e tarefas.

* Corrotinas

* Aguardáveis

* Creating tasks

* Task cancellation

* Task groups

* Dormindo

* Running tasks concurrently

* Eager task factory

* Shielding from cancellation

* Tempo limite

* Waiting primitives

* Running in threads

* Scheduling from other threads

* Introspecção

* Task object


Corrotinas
==========

**Código-fonte:** Lib/asyncio/coroutines.py

======================================================================

*Corrotinas* declaradas com a sintaxe async/await é a forma preferida
de escrever aplicações assíncronas. Por exemplo, o seguinte trecho de
código imprime "hello", espera 1 segundo, e então imprime "world":

   >>> import asyncio

   >>> async def main():
   ...     print('hello')
   ...     await asyncio.sleep(1)
   ...     print('world')

   >>> asyncio.run(main())
   hello
   world

Perceba que simplesmente chamar uma corrotina não irá agendá-la para
ser executada:

   >>> main()
   <coroutine object main at 0x1053bb7c8>

To actually run a coroutine, asyncio provides the following
mechanisms:

* A função "asyncio.run()" para executar a função "main()" do ponto de
  entrada no nível mais alto (veja o exemplo acima.)

* Aguardando uma corrotina. O seguinte trecho de código exibirá
  "hello" após esperar por 1 segundo e, em seguida, exibirá "world"
  após esperar por *outros* 2 segundos:

     import asyncio
     import time

     async def say_after(delay, what):
         await asyncio.sleep(delay)
         print(what)

     async def main():
         print(f"started at {time.strftime('%X')}")

         await say_after(1, 'hello')
         await say_after(2, 'world')

         print(f"finished at {time.strftime('%X')}")

     asyncio.run(main())

  Resultado esperado:

     started at 17:13:52
     hello
     world
     finished at 17:13:55

* A função "asyncio.create_task()" para executar corrotinas
  concorrentemente como "Tasks" asyncio.

  Vamos modificar o exemplo acima e executar duas corrotinas
  "say_after" *concorrentemente*:

     async def main():
         task1 = asyncio.create_task(
             say_after(1, 'hello'))

         task2 = asyncio.create_task(
             say_after(2, 'world'))

         print(f"started at {time.strftime('%X')}")

         # Wait until both tasks are completed (should take
         # around 2 seconds.)
         await task1
         await task2

         print(f"finished at {time.strftime('%X')}")

  Perceba que a saída esperada agora mostra que o trecho de código é
  executado 1 segundo mais rápido do que antes:

     started at 17:14:32
     hello
     world
     finished at 17:14:34

* The "asyncio.TaskGroup" class provides a more modern alternative to
  "create_task()". Using this API, the last example becomes:

     async def main():
         async with asyncio.TaskGroup() as tg:
             task1 = tg.create_task(
                 say_after(1, 'hello'))

             task2 = tg.create_task(
                 say_after(2, 'world'))

             print(f"started at {time.strftime('%X')}")

         # The await is implicit when the context manager exits.

         print(f"finished at {time.strftime('%X')}")

  The timing and output should be the same as for the previous
  version.

  Adicionado na versão 3.11: "asyncio.TaskGroup".


Aguardáveis
===========

Dizemos que um objeto é um objeto **aguardável** se ele pode ser usado
em uma expressão "await". Muitas APIs asyncio são projetadas para
aceitar aguardáveis.

Existem três tipos principais de objetos *aguardáveis*:
**corrotinas**, **Tarefas**, e **Futuros**.

-[ Corrotinas ]-

Corrotinas Python são *aguardáveis* e portanto podem ser aguardadas a
partir de outras corrotinas:

   import asyncio

   async def nested():
       return 42

   async def main():
       # Nothing happens if we just call "nested()".
       # A coroutine object is created but not awaited,
       # so it *won't run at all*.
       nested()  # will raise a "RuntimeWarning".

       # Let's do it differently now and await it:
       print(await nested())  # will print "42".

   asyncio.run(main())

Importante:

  Nesta documentação, o termo "corrotina" pode ser usado para dois
  conceitos intimamente relacionados:

  * uma *função de corrotina*: uma função "async def";

  * um *objeto de corrotina*: um objeto retornado ao chamar uma
    *função de corrotina*.

-[ Tarefas ]-

*Tarefas* são usadas para agendar corrotinas *concorrentemente*.

Quando uma corrotina é envolta em uma *tarefa* com funções como
"asyncio.create_task()", a corrotina é automaticamente agendada para
executar em breve:

   import asyncio

   async def nested():
       return 42

   async def main():
       # Schedule nested() to run soon concurrently
       # with "main()".
       task = asyncio.create_task(nested())

       # "task" can now be used to cancel "nested()", or
       # can simply be awaited to wait until it is complete:
       await task

   asyncio.run(main())

-[ Futuros ]-

Um "Future" é um objeto aguardável especial de **baixo nível** que
representa um **resultado eventual** de uma operação assíncrona.

Quando um objeto Future é *aguardado* isso significa que a corrotina
irá esperar até que o Future seja resolvido em algum outro local.

Objetos Future em asyncio são necessários para permitir que código
baseado em função de retorno seja utilizado com async/await.

Normalmente **não existe necessidade** em criar objetos Future no
nível de código da aplicação.

Objetos Future, algumas vezes expostos por bibliotecas e algumas APIs
asyncio, podem ser aguardados:

   async def main():
       await function_that_returns_a_future_object()

       # this is also valid:
       await asyncio.gather(
           function_that_returns_a_future_object(),
           some_python_coroutine()
       )

Um bom exemplo de uma função de baixo nível que retorna um objeto
Future é "loop.run_in_executor()".


Creating tasks
==============

**Source code:** Lib/asyncio/tasks.py

======================================================================

asyncio.create_task(coro, *, name=None, context=None, eager_start=None, **kwargs)

   Envolve a corrotina *coro* em uma "Task" e agenda sua execução.
   Retorna o objeto Task.

   A assinatura completa da função é, em grande parte, a mesma que a
   do construtor (ou fábrica) de "Task" — todos os argumentos nomeados
   desta função são passados para essa interface.

   Um argumento opcional somente-nomeado *context* permite especificar
   um "contextvars.Context" personalizado para a *coro* ser executada.
   Uma cópia do contexto atual é criada quando nenhum *context* for
   fornecido.

   Um argumento opcional somente-nomeado *eager_start* permite
   especificar se a tarefa deve ser executada imediatamente durante a
   chamada para create_task ou ser agendada para mais tarde. Se
   *eager_start* não for fornecido, o modo definido por
   "loop.set_task_factory()" será utilizado.

   A tarefa é executada no laço e retornada por "get_running_loop()",
   "RuntimeError" é levantado se não existir um laço em execução na
   thread atual.

   Nota:

     "asyncio.TaskGroup.create_task()" é uma nova alternativa que
     aproveita a concorrência estruturada e permite aguardar um grupo
     de tarefas relacionadas, com fortes garantias de segurança.

   Importante:

     Mantenha uma referência para o resultado dessa função, evitando
     que uma tarefa desapareça durante a execução. O laço de eventos
     mantém apenas referências fracas para as tarefas. Uma tarefa que
     não é referenciada por nada mais pode ser removida pelo coletor
     de lixo a qualquer momento, antes mesmo da função ser finalizada.
     Para tarefas de segundo plano "atire-e-esqueça", junte-as em uma
     coleção:

        background_tasks = set()for i in range(10):    task = asyncio.create_task(some_coro(param=i))    # Adiciona tarefa ao conjunto. Isto cria uma referência forte.    background_tasks.add(task)    # Para evitar manter referências a tarefas concluídas para sempre,    # fazer com que cada tarefa remova a sua própria referência do conjunto após    # a conclusão:    task.add_done_callback(background_tasks.discard)

     Note that this approach never awaits the tasks, so if a task
     fails, its exception is never retrieved and asyncio logs a "Task
     exception was never retrieved" message when the task is garbage
     collected.  To avoid this, use "asyncio.TaskGroup" which keeps a
     strong reference to each task, awaits them and propagates their
     exceptions:

        async with asyncio.TaskGroup() as tg:
            for i in range(10):
                tg.create_task(some_coro(param=i))

   Adicionado na versão 3.7.

   Alterado na versão 3.8: Adicionado o parâmetro *name*.

   Alterado na versão 3.11: Adicionado o parâmetro *context*.

   Alterado na versão 3.14: Adicionado o parâmetro *eager_start*,
   passando todos os *kwargs*.


Task cancellation
=================

Tasks can easily and safely be cancelled. When a task is cancelled,
"asyncio.CancelledError" will be raised in the task at the next
opportunity.

It is recommended that coroutines use "try/finally" blocks to robustly
perform clean-up logic. In case "asyncio.CancelledError" is explicitly
caught, it should generally be propagated when clean-up is complete.
"asyncio.CancelledError" directly subclasses "BaseException" so most
code will not need to be aware of it.

The asyncio components that enable structured concurrency, like
"asyncio.TaskGroup" and "asyncio.timeout()", are implemented using
cancellation internally and might misbehave if a coroutine swallows
"asyncio.CancelledError". Similarly, user code should not generally
call "uncancel". However, in cases when suppressing
"asyncio.CancelledError" is truly desired, it is necessary to also
call "uncancel()" to completely remove the cancellation state.


Task groups
===========

Grupos de tarefas combinam uma API de criação de tarefas com uma forma
conveniente e confiável de aguardar que todas as tarefas do grupo
terminem.

class asyncio.TaskGroup

   Um gerenciador de contexto assíncrono que contém um grupo de
   tarefas. As tarefas podem ser adicionadas ao grupo usando
   "create_task()". Todas as tarefas são aguardadas quando o
   gerenciador de contexto sai.

   Adicionado na versão 3.11.

   create_task(coro, *, name=None, context=None, eager_start=None, **kwargs)

      Create a task in this task group. The signature matches that of
      "asyncio.create_task()". If the task group is inactive (e.g. not
      yet entered, already finished, or in the process of shutting
      down), we will close the given "coro" and raise "RuntimeError".

      Alterado na versão 3.13: Fecha a corrotina dada se o grupo de
      tarefas não estiver ativo.

      Alterado na versão 3.14: Passa todos os *kwargs* para
      "loop.create_task()"

   cancel()

      Cancel the task group.  This is a non-exceptional, early exit of
      the task group's lifetime -- useful once the group's goal has
      been met or its services no longer needed.

      "cancel()" will be called on any tasks in the group that aren't
      yet done, as well as the parent (body) of the group.  The task
      group context manager will exit *without*
      "asyncio.CancelledError" being raised.

      If "cancel()" is called before entering the task group, the
      group will be cancelled upon entry.  This is useful for patterns
      where one piece of code passes an unused "asyncio.TaskGroup"
      instance to another in order to have the ability to cancel
      anything run within the group.

      "cancel()" is idempotent and may be called after the task group
      has already exited.

      Some ways to use "cancel()":

      * call it from the task group body based on some condition or
        event

      * pass the task group instance to child tasks via
        "create_task()", allowing a child task to conditionally cancel
        the entire group

      * pass the task group instance or bound "cancel()" method to
        some other task *before* opening the task group, allowing
        remote cancellation

      Adicionado na versão 3.15.

Exemplo:

   async def main():    async with asyncio.TaskGroup() as tg:        task1 = tg.create_task(some_coro(...))        task2 = tg.create_task(another_coro(...))    print(f"Ambas as tarefas estão agora concluídas: {task1.result()}, {task2.result()}")

The "async with" statement will wait for all tasks in the group to
finish. While waiting, new tasks may still be added to the group (for
example, by passing "tg" into one of the coroutines and calling
"tg.create_task()" in that coroutine).  There is also opportunity to
request termination of the entire task group with "tg.cancel()", based
on some condition. Once the last task has finished and the "async
with" block is exited, no new tasks may be added to the group.

Na primeira vez que qualquer uma das tarefas do grupo falha com uma
exceção diferente de "asyncio.CancelledError", as tarefas restantes do
grupo são canceladas. Não podem ser adicionadas mais tarefas ao grupo.
Neste ponto, se o corpo da instrução "async with" ainda estiver ativo
(ou seja, "__aexit__()" ainda não foi chamado), a tarefa que contém
diretamente a instrução "async with" também é cancelada. A
"asyncio.CancelledError" resultante irá interromper um "await", mas
não se propagará para fora da instrução "async with".

Uma vez que todas as tarefas tenham terminado, se alguma tarefa falhou
com uma exceção diferente de "asyncio.CancelledError", essas exceções
são combinadas em uma "ExceptionGroup" ou "BaseExceptionGroup"
(conforme apropriado; veja a sua documentação), que é então levantada.

Duas exceções base são tratadas de forma especial: se alguma tarefa
falhar com "KeyboardInterrupt" ou "SystemExit", o grupo de tarefas
ainda cancela as tarefas restantes e aguarda por elas, mas depois a
"KeyboardInterrupt" ou "SystemExit" inicial é levantada novamente em
vez de "ExceptionGroup" ou "BaseExceptionGroup".

If the body of the "async with" statement exits with an exception (so
"__aexit__()" is called with an exception set), this is treated the
same as if one of the tasks failed: the remaining tasks are cancelled
and then waited for, and non-cancellation exceptions are grouped into
an exception group and raised. The exception passed into
"__aexit__()", unless it is "asyncio.CancelledError", is also included
in the exception group. The same special case is made for
"KeyboardInterrupt" and "SystemExit" as in the previous paragraph.
There is an additional special case made only for the body of the
"async with": if it raises "GeneratorExit" and none of the other tasks
raise exceptions that would be reported, then the "GeneratorExit" is
reraised.

Os grupos de tarefas tomam cuidado para não confundir o cancelamento
interno, usado para "acordar" o seu "__aexit__()", com pedidos de
cancelamento para a tarefa na qual estão a ser executados, feitos por
outras partes. Em particular, quando um grupo de tarefas está
sintaticamente aninhado noutro, e ambos experimentam uma exceção numa
das suas tarefas filhas simultaneamente, o grupo de tarefas interno
processará as suas exceções, e depois o grupo de tarefas externo
receberá outro cancelamento e processará as suas próprias exceções.

No caso de um grupo de tarefas ser cancelado externamente e também
precisar levantar uma "ExceptionGroup", chamará o método "cancel()" da
tarefa pai. Isto garante que um "asyncio.CancelledError" será
levantada no próximo "await", para que o cancelamento não se perca.

Os grupos de tarefas preservam a contagem de cancelamentos reportada
por "asyncio.Task.cancelling()".

Alterado na versão 3.13: Melhoria no tratamento de cancelamentos
internos e externos simultâneos e na preservação correta das contagens
de cancelamentos.

Alterado na versão 3.15: Addition of the special case for
"GeneratorExit".


Dormindo
========

async asyncio.sleep(delay, result=None)

   Bloqueia por *delay* segundos.

   Se *result* é fornecido, é retornado para o autor da chamada quando
   a corrotina termina.

   "sleep()" sempre suspende a tarefa atual, permitindo que outras
   tarefas sejam executadas.

   Configurando o delay para 0 fornece um caminho otimizado para
   permitir que outras tarefas executem. Isto pode ser usado por
   funções de longa execução para evitar que bloqueiem o laço de
   eventos por toda a duração da chamada da função.

   Exemplo de uma corrotina exibindo a data atual a cada segundo
   durante 5 segundos:

      import asyncio
      import datetime as dt

      async def display_date():
          loop = asyncio.get_running_loop()
          end_time = loop.time() + 5.0
          while True:
              print(dt.datetime.now())
              if (loop.time() + 1.0) >= end_time:
                  break
              await asyncio.sleep(1)

      asyncio.run(display_date())

   Alterado na versão 3.10: Removido o parâmetro *loop*.

   Alterado na versão 3.13: Raises "ValueError" if *delay* is "nan".


Running tasks concurrently
==========================

awaitable asyncio.gather(*aws, return_exceptions=False)

   Executa objetos aguardáveis na sequência *aws* de forma
   *concorrente*.

   Se qualquer aguardável em *aws* é uma corrotina, ele é
   automaticamente agendado como uma Tarefa.

   Se todos os aguardáveis forem concluídos com sucesso, o resultado é
   uma lista agregada de valores retornados. A ordem dos valores
   resultantes corresponde a ordem dos aguardáveis em *aws*.

   Se *return_exceptions* for "False" (valor padrão), a primeira
   exceção levantada é imediatamente propagada para a tarefa que
   espera em "gather()". Outros aguardáveis na sequência *aws* **não
   serão cancelados** e irão continuar a executar.

   Se *return_exceptions* for "True", exceções são tratadas da mesma
   forma que resultados com sucesso, e agregadas na lista de
   resultados.

   Se "gather()" for *cancelado*, todos os aguardáveis que foram
   submetidos (que não foram concluídos ainda) também são
   *cancelados*.

   Se qualquer Tarefa ou Futuro da sequência *aws* for *cancelado*,
   ele é tratado como se tivesse levantado "CancelledError" -- a
   chamada para "gather()" **não** é cancelada neste caso. Isso existe
   para prevenir que o cancelamento de uma Tarefa/Futuro submetida
   ocasione outras Tarefas/Futuros a serem cancelados.

   Nota:

     A new alternative to create and run tasks concurrently and wait
     for their completion is "asyncio.TaskGroup". *TaskGroup* provides
     stronger safety guarantees than *gather* for scheduling a nesting
     of subtasks: if a task (or a subtask, a task scheduled by a task)
     raises an exception, *TaskGroup* will, while *gather* will not,
     cancel the remaining scheduled tasks.

   Exemplo:

      import asyncio

      async def factorial(name, number):
          f = 1
          for i in range(2, number + 1):
              print(f"Task {name}: Compute factorial({number}), currently i={i}...")
              await asyncio.sleep(1)
              f *= i
          print(f"Task {name}: factorial({number}) = {f}")
          return f

      async def main():
          # Schedule three calls *concurrently*:
          L = await asyncio.gather(
              factorial("A", 2),
              factorial("B", 3),
              factorial("C", 4),
          )
          print(L)

      asyncio.run(main())

      # Expected output:
      #
      #     Task A: Compute factorial(2), currently i=2...
      #     Task B: Compute factorial(3), currently i=2...
      #     Task C: Compute factorial(4), currently i=2...
      #     Task A: factorial(2) = 2
      #     Task B: Compute factorial(3), currently i=3...
      #     Task C: Compute factorial(4), currently i=3...
      #     Task B: factorial(3) = 6
      #     Task C: Compute factorial(4), currently i=4...
      #     Task C: factorial(4) = 24
      #     [2, 6, 24]

   Nota:

     If *return_exceptions* is false, cancelling gather() after it has
     been marked done won't cancel any submitted awaitables. For
     instance, gather can be marked done after propagating an
     exception to the caller, therefore, calling "gather.cancel()"
     after catching an exception (raised by one of the awaitables)
     from gather won't cancel any other awaitables.

   Alterado na versão 3.7: Se *gather* por si mesmo for cancelado, o
   cancelamento é propagado independente de *return_exceptions*.

   Alterado na versão 3.10: Removido o parâmetro *loop*.

   Descontinuado desde a versão 3.10: Aviso de descontinuidade é
   emitido se nenhum argumento posicional for fornecido, ou nem todos
   os argumentos posicionais são objetos similar a Futuro, e não
   existe nenhum laço de eventos em execução.


Eager task factory
==================

asyncio.eager_task_factory(loop, coro, *, name=None, context=None)

   A task factory for eager task execution.

   When using this factory (via
   "loop.set_task_factory(asyncio.eager_task_factory)"), coroutines
   begin execution synchronously during "Task" construction. Tasks are
   only scheduled on the event loop if they block. This can be a
   performance improvement as the overhead of loop scheduling is
   avoided for coroutines that complete synchronously.

   A common example where this is beneficial is coroutines which
   employ caching or memoization to avoid actual I/O when possible.

   Nota:

     Immediate execution of the coroutine is a semantic change. If the
     coroutine returns or raises, the task is never scheduled to the
     event loop. If the coroutine execution blocks, the task is
     scheduled to the event loop. This change may introduce behavior
     changes to existing applications. For example, the application's
     task execution order is likely to change.

   Adicionado na versão 3.12.

asyncio.create_eager_task_factory(custom_task_constructor)

   Create an eager task factory, similar to "eager_task_factory()",
   using the provided *custom_task_constructor* when creating a new
   task instead of the default "Task".

   *custom_task_constructor* must be a *callable* with the signature
   matching the signature of "Task.__init__". The callable must return
   a "asyncio.Task"-compatible object.

   This function returns a *callable* intended to be used as a task
   factory of an event loop via "loop.set_task_factory(factory)").

   Adicionado na versão 3.12.


Shielding from cancellation
===========================

awaitable asyncio.shield(aw)

   Protege um objeto aguardável de ser "cancelado".

   Se *aw* é uma corrotina, ela é automaticamente agendada como uma
   Tarefa.

   A instrução:

      task = asyncio.create_task(something())
      res = await shield(task)

   é equivalente a:

      res = await something()

   *exceto* que se a corrotina contendo-a for cancelada, a Tarefa
   executando em "something()" não é cancelada. Do ponto de vista de
   "something()", o cancelamento não aconteceu. Apesar do autor da
   chamada ainda estar cancelado, então a expressão "await" ainda
   levanta um "CancelledError".

   Se "something()" é cancelada por outros meios (isto é, dentro ou a
   partir de si mesma) isso também iria cancelar "shield()".

   Se for desejado ignorar completamente os cancelamentos (não
   recomendado) a função "shield()" deve ser combinada com uma
   cláusula try/except, conforme abaixo:

      task = asyncio.create_task(something())
      try:
          res = await shield(task)
      except CancelledError:
          res = None

   Importante:

     Mantenha uma referência para as tarefas passadas para essa função
     função, evitando assim que uma tarefa desapareça durante a
     execução. O laço de eventos mantém apenas referências fracas para
     as tarefas. Uma tarefa que não é referenciada por nada mais pode
     ser removida pelo coletor de lixo a qualquer momento, antes mesmo
     da função ser finalizada.

   Alterado na versão 3.10: Removido o parâmetro *loop*.

   Descontinuado desde a versão 3.10: Aviso de descontinuidade é
   emitido se *aw* não é um objeto similar a Futuro, e não existe
   nenhum laço de eventos em execução.


Tempo limite
============

asyncio.timeout(delay)

   Return an asynchronous context manager that can be used to limit
   the amount of time spent waiting on something.

   *delay* can either be "None", or a float/int number of seconds to
   wait. If *delay* is "None", no time limit will be applied; this can
   be useful if the delay is unknown when the context manager is
   created.

   In either case, the context manager can be rescheduled after
   creation using "Timeout.reschedule()".

   Exemplo:

      async def main():
          async with asyncio.timeout(10):
              await long_running_task()

   If "long_running_task" takes more than 10 seconds to complete, the
   context manager will cancel the current task and handle the
   resulting "asyncio.CancelledError" internally, transforming it into
   a "TimeoutError" which can be caught and handled.

   Nota:

     The "asyncio.timeout()" context manager is what transforms the
     "asyncio.CancelledError" into a "TimeoutError", which means the
     "TimeoutError" can only be caught *outside* of the context
     manager.

   Example of catching "TimeoutError":

      async def main():
          try:
              async with asyncio.timeout(10):
                  await long_running_task()
          except TimeoutError:
              print("The long operation timed out, but we've handled it.")

          print("This statement will run regardless.")

   The context manager produced by "asyncio.timeout()" can be
   rescheduled to a different deadline and inspected.

   class asyncio.Timeout(when)

      An asynchronous context manager for cancelling overdue
      coroutines.

      Prefer using "asyncio.timeout()" or "asyncio.timeout_at()"
      rather than instantiating "Timeout" directly.

      "when" should be an absolute time at which the context should
      time out, as measured by the event loop's clock:

      * If "when" is "None", the timeout will never trigger.

      * If "when < loop.time()", the timeout will trigger on the next
        iteration of the event loop.

         when() -> float | None

            Return the current deadline, or "None" if the current
            deadline is not set.

         reschedule(when: float | None)

            Reschedule the timeout.

         expired() -> bool

            Return whether the context manager has exceeded its
            deadline (expired).

   Exemplo:

      async def main():
          try:
              # We do not know the timeout when starting, so we pass ``None``.
              async with asyncio.timeout(None) as cm:
                  # We know the timeout now, so we reschedule it.
                  new_deadline = get_running_loop().time() + 10
                  cm.reschedule(new_deadline)

                  await long_running_task()
          except TimeoutError:
              pass

          if cm.expired():
              print("Looks like we haven't finished on time.")

   Timeout context managers can be safely nested.

   Adicionado na versão 3.11.

asyncio.timeout_at(when)

   Similar to "asyncio.timeout()", except *when* is the absolute time
   to stop waiting, or "None".

   Exemplo:

      async def main():
          loop = get_running_loop()
          deadline = loop.time() + 20
          try:
              async with asyncio.timeout_at(deadline):
                  await long_running_task()
          except TimeoutError:
              print("The long operation timed out, but we've handled it.")

          print("This statement will run regardless.")

   Adicionado na versão 3.11.

async asyncio.wait_for(aw, timeout)

   Espera o aguardável *aw* concluir sem ultrapassar o tempo limite
   "timeout".

   *timeout* pode ser "None", ou um ponto flutuante, ou um número
   inteiro de segundos para aguardar. Se *timeout* é "None", aguarda
   até o future encerrar.

   If a timeout occurs, it cancels *aw* and raises "TimeoutError".

   To prevent *aw* from being cancelled, wrap it in "shield()".

   A função irá aguardar até o future ser realmente cancelado, então o
   tempo total de espera pode exceder o tempo limite *timeout*. Se uma
   exceção ocorrer durante o cancelamento, ela será propagada.

   Se ele for cancelado, o future *aw* também é cancelado.

   Exemplo:

      async def eternity():
          # Sleep for one hour
          await asyncio.sleep(3600)
          print('yay!')

      async def main():
          # Wait for at most 1 second
          try:
              await asyncio.wait_for(eternity(), timeout=1.0)
          except TimeoutError:
              print('timeout!')

      asyncio.run(main())

      # Expected output:
      #
      #     timeout!

   Alterado na versão 3.7: When *aw* is cancelled due to a timeout,
   "wait_for" waits for *aw* to be cancelled.  Previously, it raised
   "TimeoutError" immediately.

   Alterado na versão 3.10: Removido o parâmetro *loop*.

   Alterado na versão 3.11: Raises "TimeoutError" instead of
   "asyncio.TimeoutError".

   Alterado na versão 3.12: Implemented using "asyncio.timeout()", a
   coroutine passed as *aw* is no longer wrapped in a "Task" when
   *timeout* is positive.


Waiting primitives
==================

async asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)

   Run "Future" and "Task" instances in the *aws* iterable
   concurrently and block until the condition specified by
   *return_when*.

   O iterável *aws* não deve ser vazio.

   Retorna dois conjuntos de Tarefas/Futuros: "(done, pending)".

   Uso:

      done, pending = await asyncio.wait(aws)

   *timeout* (um ponto flutuante ou inteiro), se especificado, pode
   ser usado para controlar o número máximo de segundos para aguardar
   antes de retornar.

   Note that this function does not raise "TimeoutError". Futures or
   Tasks that aren't done when the timeout occurs are simply returned
   in the second set.

   *return_when* indica quando esta função deve retornar. Ele deve ser
   uma das seguintes constantes:

   +----------------------------------------------------+----------------------------------------------------+
   | Constante                                          | Descrição                                          |
   |====================================================|====================================================|
   | asyncio.FIRST_COMPLETED                            | A função irá retornar quando qualquer futuro       |
   |                                                    | terminar ou for cancelado.                         |
   +----------------------------------------------------+----------------------------------------------------+
   | asyncio.FIRST_EXCEPTION                            | The function will return when any future finishes  |
   |                                                    | by raising an exception. If no future raises an    |
   |                                                    | exception then it is equivalent to                 |
   |                                                    | "ALL_COMPLETED".                                   |
   +----------------------------------------------------+----------------------------------------------------+
   | asyncio.ALL_COMPLETED                              | A função irá retornar quando todos os futuros      |
   |                                                    | encerrarem ou forem cancelados.                    |
   +----------------------------------------------------+----------------------------------------------------+

   Diferente de "wait_for()", "wait()" não cancela os futuros quando
   um tempo limite é atingido.

   If "wait()" is cancelled, the futures in *aws* are not cancelled
   and continue to run.

   Alterado na versão 3.10: Removido o parâmetro *loop*.

   Alterado na versão 3.11: Passing coroutine objects to "wait()"
   directly is forbidden.

   Alterado na versão 3.12: Added support for generators yielding
   tasks.

asyncio.as_completed(aws, *, timeout=None)

   Run awaitable objects in the *aws* iterable concurrently. The
   returned object can be iterated to obtain the results of the
   awaitables as they finish.

   The object returned by "as_completed()" can be iterated as an
   *asynchronous iterator* or a plain *iterator*. When asynchronous
   iteration is used, the originally-supplied awaitables are yielded
   if they are tasks or futures. This makes it easy to correlate
   previously-scheduled tasks with their results. Example:

      ipv4_connect = create_task(open_connection("127.0.0.1", 80))
      ipv6_connect = create_task(open_connection("::1", 80))
      tasks = [ipv4_connect, ipv6_connect]

      async for earliest_connect in as_completed(tasks):
          # earliest_connect is done. The result can be obtained by
          # awaiting it or calling earliest_connect.result()
          reader, writer = await earliest_connect

          if earliest_connect is ipv6_connect:
              print("IPv6 connection established.")
          else:
              print("IPv4 connection established.")

   During asynchronous iteration, implicitly-created tasks will be
   yielded for supplied awaitables that aren't tasks or futures.

   When used as a plain iterator, each iteration yields a new
   coroutine that returns the result or raises the exception of the
   next completed awaitable. This pattern is compatible with Python
   versions older than 3.13:

      ipv4_connect = create_task(open_connection("127.0.0.1", 80))
      ipv6_connect = create_task(open_connection("::1", 80))
      tasks = [ipv4_connect, ipv6_connect]

      for next_connect in as_completed(tasks):
          # next_connect is not one of the original task objects. It must be
          # awaited to obtain the result value or raise the exception of the
          # awaitable that finishes next.
          reader, writer = await next_connect

   A "TimeoutError" is raised if the timeout occurs before all
   awaitables are done. This is raised by the "async for" loop during
   asynchronous iteration or by the coroutines yielded during plain
   iteration.

   "as_completed()" does not cancel the tasks running the supplied
   awaitables: if a timeout occurs or the iteration is cancelled, the
   remaining tasks continue to run.

   Alterado na versão 3.10: Removido o parâmetro *loop*.

   Descontinuado desde a versão 3.10: Aviso de descontinuidade é
   emitido se nem todos os objetos aguardáveis no iterável *aws* forem
   objetos similar a Futuro, e não existe nenhum laço de eventos em
   execução.

   Alterado na versão 3.12: Added support for generators yielding
   tasks.

   Alterado na versão 3.13: The result can now be used as either an
   *asynchronous iterator* or as a plain *iterator* (previously it was
   only a plain iterator).


Running in threads
==================

async asyncio.to_thread(func, /, *args, **kwargs)

   Executa a função *func* assincronamente em uma thread separada.

   Quaisquer *args e **kwargs fornecidos para esta função são
   diretamente passados para *func*. Além disso, o
   "contextvars.Context" atual é propagado, permitindo que variáveis
   de contexto da thread do laço de eventos sejam acessadas na thread
   separada.

   Retorna uma corrotina que pode ser aguardada para obter o resultado
   eventual de *func*.

   This coroutine function is primarily intended to be used for
   executing IO-bound functions/methods that would otherwise block the
   event loop if they were run in the main thread. For example:

      def blocking_io():
          print(f"start blocking_io at {time.strftime('%X')}")
          # Note that time.sleep() can be replaced with any blocking
          # IO-bound operation, such as file operations.
          time.sleep(1)
          print(f"blocking_io complete at {time.strftime('%X')}")

      async def main():
          print(f"started main at {time.strftime('%X')}")

          await asyncio.gather(
              asyncio.to_thread(blocking_io),
              asyncio.sleep(1))

          print(f"finished main at {time.strftime('%X')}")


      asyncio.run(main())

      # Expected output:
      #
      # started main at 19:50:53
      # start blocking_io at 19:50:53
      # blocking_io complete at 19:50:54
      # finished main at 19:50:54

   Chamar diretamente "blocking_io()" em qualquer corrotina iria
   bloquear o laço de eventos durante a sua duração, resultando em 1
   segundo adicional no tempo de execução. Ao invés disso, ao utilizar
   "asyncio.to_thread()", nós podemos executá-la em uma thread
   separada sem bloquear o laço de eventos.

   Nota:

     Devido à *GIL*, "asyncio.to_thread()" pode tipicamente ser usado
     apenas para fazer funções vinculadas a IO não-bloqueantes.
     Entretanto, para módulos de extensão que liberam o GIL ou
     implementações alternativas do Python que não tem um,
     "asyncio.to_thread()" também pode ser usado para funções
     vinculadas à CPU.

   Adicionado na versão 3.9.


Scheduling from other threads
=============================

asyncio.run_coroutine_threadsafe(coro, loop)

   Envia uma corrotina para o laço de eventos fornecido. Seguro para
   thread.

   Retorna um "concurrent.futures.Future" para aguardar pelo resultado
   de outra thread do sistema operacional.

   Esta função destina-se a ser chamada partir de uma thread diferente
   do sistema operacional, da qual o laço de eventos está executando.
   Exemplo:

      def in_thread(loop: asyncio.AbstractEventLoop) -> None:
          # Run some blocking IO
          pathlib.Path("example.txt").write_text("hello world", encoding="utf8")

          # Create a coroutine
          coro = asyncio.sleep(1, result=3)

          # Submit the coroutine to a given loop
          future = asyncio.run_coroutine_threadsafe(coro, loop)

          # Wait for the result with an optional timeout argument
          assert future.result(timeout=2) == 3

      async def amain() -> None:
          # Get the running loop
          loop = asyncio.get_running_loop()

          # Run something in a thread
          await asyncio.to_thread(in_thread, loop)

   It's also possible to run the other way around.  Example:

      @contextlib.contextmanager
      def loop_in_thread() -> Generator[asyncio.AbstractEventLoop]:
          loop_fut = concurrent.futures.Future[asyncio.AbstractEventLoop]()
          stop_event = asyncio.Event()

          async def main() -> None:
              loop_fut.set_result(asyncio.get_running_loop())
              await stop_event.wait()

          with concurrent.futures.ThreadPoolExecutor(1) as tpe:
              complete_fut = tpe.submit(asyncio.run, main())
              for fut in concurrent.futures.as_completed((loop_fut, complete_fut)):
                  if fut is loop_fut:
                      loop = loop_fut.result()
                      try:
                          yield loop
                      finally:
                          loop.call_soon_threadsafe(stop_event.set)
                  else:
                      fut.result()

      # Create a loop in another thread
      with loop_in_thread() as loop:
          # Create a coroutine
          coro = asyncio.sleep(1, result=3)

          # Submit the coroutine to a given loop
          future = asyncio.run_coroutine_threadsafe(coro, loop)

          # Wait for the result with an optional timeout argument
          assert future.result(timeout=2) == 3

   Se uma exceção for levantada na corrotina, o Futuro retornado será
   notificado. Isso também pode ser usado para cancelar a tarefa no
   laço de eventos:

      try:
          result = future.result(timeout)
      except TimeoutError:
          print('The coroutine took too long, cancelling the task...')
          future.cancel()
      except Exception as exc:
          print(f'The coroutine raised an exception: {exc!r}')
      else:
          print(f'The coroutine returned: {result!r}')

   Veja a seção concorrência e multithreading da documentação.

   Ao contrário de outras funções asyncio, esta função requer que o
   argumento *loop* seja passado explicitamente.

   Adicionado na versão 3.5.1.


Introspecção
============

asyncio.current_task(loop=None)

   Retorna a instância "Task" atualmente em execução, ou "None" se
   nenhuma tarefa estiver executando.

   Se *loop* for "None", então "get_running_loop()" é usado para obter
   o laço atual.

   Adicionado na versão 3.7.

asyncio.all_tasks(loop=None)

   Retorna um conjunto de objetos "Task" ainda não concluídos a serem
   executados pelo laço.

   Se *loop* for "None", então "get_running_loop()" é usado para obter
   o laço atual.

   Adicionado na versão 3.7.

asyncio.iscoroutine(obj)

   Return "True" if *obj* is a coroutine object.

   Adicionado na versão 3.4.


Task object
===========

class asyncio.Task(coro, *, loop=None, name=None, context=None, eager_start=False)

   Um objeto "similar a Futuro" que executa uma corrotina Python. Não
   é seguro para thread.

   Tarefas são usadas para executar corrotinas em laços de eventos. Se
   uma corrotina espera por um Futuro, a Tarefa suspende a execução da
   corrotina e aguarda a conclusão do Futuro. Quando o Futuro é
   *concluído*, a execução da corrotina contida é retomada.

   Laços de eventos usam agendamento cooperativo: um ciclo de evento
   executa uma Task de cada vez. Enquanto uma Task aguarda a conclusão
   de um Future, o laço de eventos executa outras Tasks, funções de
   retorno, ou executa operações de IO.

   Use a função de alto nível "asyncio.create_task()" para criar
   Tasks, ou as funções de baixo nível "loop.create_task()" ou
   "ensure_future()". Instanciação manual de Tasks é desencorajada.

   To cancel a running Task use the "cancel()" method.  Calling it
   will cause the Task to throw a "CancelledError" exception into the
   wrapped coroutine.  If a coroutine is awaiting on a future-like
   object during cancellation, the awaited object will be cancelled.

   "cancelled()" pode ser usado para verificar se a Task foi
   cancelada. O método retorna "True" se a corrotina envolvente não
   suprimiu a exceção "CancelledError" e, na verdade, foi cancelada.

   "asyncio.Task" herda de "Future" todas as suas APIs exceto
   "Future.set_result()" e "Future.set_exception()".

   An optional keyword-only *context* argument allows specifying a
   custom "contextvars.Context" for the *coro* to run in. If no
   *context* is provided, the Task copies the current context and
   later runs its coroutine in the copied context.

   Um argumento opcional somente-nomeado *eager_start* permite iniciar
   imediatamente a execução da "asyncio.Task" no momento da criação da
   tarefa. Se definido como "True" e o laço de eventos estiver em
   execução, a tarefa começará a executar a corrotina imediatamente,
   até à primeira vez que a corrotina bloquear. Se a corrotina
   devolver ou levantar uma exceção sem bloquear, a tarefa será
   concluída imediatamente e não será agendada para o laço de eventos.

   Tasks are generic over the return type of their wrapped coroutines.

   Alterado na versão 3.7: Adicionado suporte ao módulo "contextvars".

   Alterado na versão 3.8: Adicionado o parâmetro *name*.

   Descontinuado desde a versão 3.10: Aviso de descontinuidade é
   emitido se *loop* não for especificado e não existir nenhum laço de
   eventos em execução.

   Alterado na versão 3.11: Adicionado o parâmetro *context*.

   Alterado na versão 3.12: Adicionado o parâmetro *eager_start*.

   done()

      Retorna "True" se a Tarefa estiver *concluída*.

      Uma Tarefa está *concluída* quando a corrotina contida retornou
      um valor, ou levantou uma exceção, ou a Tarefa foi cancelada.

   result()

      Retorna o resultado da Tarefa.

      Se a Tarefa estiver *concluída*, o resultado da corrotina
      contida é retornado (ou se a corrotina levantou uma exceção,
      essa exceção é re-levantada.)

      Se a Tarefa foi *cancelada*, este método levanta uma exceção
      "CancelledError".

      If the Task's result isn't yet available, this method raises an
      "InvalidStateError" exception.

   exception()

      Retorna a exceção de uma Tarefa.

      Se a corrotina contida levantou uma exceção, essa exceção é
      retornada. Se a corrotina contida retornou normalmente, este
      método retorna "None".

      Se a Tarefa foi *cancelada*, este método levanta uma exceção
      "CancelledError".

      Se a Tarefa não estiver *concluída* ainda, este método levanta
      uma exceção "InvalidStateError".

   add_done_callback(callback, *, context=None)

      Adiciona uma função de retorno para ser executada quando a
      Tarefa estiver *concluída*.

      Este método deve ser usado apenas em código de baixo nível
      baseado em funções de retorno.

      Veja a documentação para "Future.add_done_callback()" para mais
      detalhes.

   remove_done_callback(callback)

      Remove *callback* da lista de funções de retorno.

      Este método deve ser usado apenas em código de baixo nível
      baseado em funções de retorno.

      Veja a documentação do método "Future.remove_done_callback()"
      para mais detalhes.

   get_stack(*, limit=None)

      Retorna a lista de frames da pilha para esta Tarefa.

      Se a corrotina contida não estiver concluída, isto retorna a
      pilha onde ela foi suspensa. Se a corrotina foi concluída com
      sucesso ou cancelada, isto retorna uma lista vazia. Se a
      corrotina foi interrompida por uma exceção, isso retorna a lista
      de frames do traceback (situação da pilha de execução).

      Os quadros são sempre ordenados dos mais antigos para os mais
      recentes.

      Apenas um frame da pilha é retornado para uma corrotina
      suspensa.

      O argumento opcional *limit* define o número máximo de frames a
      serem retornados; por padrão, todos os frames disponíveis são
      retornados. O ordenamento da lista retornada é diferente
      dependendo se uma pilha ou um traceback (situação da pilha de
      execução) é retornado: os frames mais recentes de uma pilha são
      retornados, mas os frames mais antigos de um traceback são
      retornados. (Isso combina com o comportamento do módulo
      traceback.)

   print_stack(*, limit=None, file=None)

      Exibe a pilha ou a situação da pilha de execução desta Task.

      Isto produz uma saída similar à do módulo traceback para frames
      recuperados por "get_stack()".

      O argumento *limit* é passado diretamente para "get_stack()".

      O argumento *file* é um fluxo de I/O para o qual a saída é
      escrita; por padrão, a saída é escrita para "sys.stdout".

   get_coro()

      Retorna o objeto corrotina contido pela "Task".

      Nota:

        Isto retornará "None" para Tasks que já tenham sido concluídas
        ansiosamente. Consulte fábrica de tarefas ansiosas.

      Adicionado na versão 3.8.

      Alterado na versão 3.12: A execução de tarefas recentemente
      adicionadas, ansiosas, pode resultar em "None".

   get_context()

      Retorna o objeto "contextvars.Context" associado à tarefa.

      Adicionado na versão 3.12.

   get_name()

      Retorna o nome da Tarefa.

      Se nenhum nome foi explicitamente designado para a Tarefa, a
      implementação padrão asyncio da classe Task gera um nome padrão
      durante a instanciação.

      Adicionado na versão 3.8.

   set_name(value)

      Define o nome da Tarefa.

      O argumento *value* pode ser qualquer objeto, que é então
      convertido em uma string.

      Na implementação padrão da Tarefa, o nome será visível na
      "repr()" de saída de um objeto task.

      Adicionado na versão 3.8.

   cancel(msg=None)

      Solicita o cancelamento da Tarefa.

      If the Task is already *done* or *cancelled*, return "False",
      otherwise, return "True".

      O método prepara para que uma exceção "CancelledError" seja
      lançada na corrotina contida no próximo ciclo do laço de
      eventos.

      The coroutine then has a chance to clean up or even deny the
      request by suppressing the exception with a "try" ... ...
      "except CancelledError" ... "finally" block. Therefore, unlike
      "Future.cancel()", "Task.cancel()" does not guarantee that the
      Task will be cancelled, although suppressing cancellation
      completely is not common and is actively discouraged.  Should
      the coroutine nevertheless decide to suppress the cancellation,
      it needs to call "Task.uncancel()" in addition to catching the
      exception.

      If the Task being cancelled is currently awaiting on a future-
      like object, that awaited object will also be cancelled. This
      cancellation propagates down the entire chain of awaited
      objects.

      Alterado na versão 3.9: Adicionado o  parâmetro *msg*.

      Alterado na versão 3.11: O parâmetro "msg" é propagado da tarefa
      cancelada para o seu aguardador.

      O seguinte exemplo ilustra como corrotinas podem interceptar o
      cancelamento de requisições:

         async def cancel_me():    print('cancel_me(): antes de dormir')    try:        # Aguardar 1 hora        await asyncio.sleep(3600)    except asyncio.CancelledError:        print('cancel_me(): cancelar sono')        raise    finally:        print('cancel_me(): depois de dormir')async def main():    # Criar uma Tarefa "cancel_me"    task = asyncio.create_task(cancel_me())    # Aguardar 1 segundo    await asyncio.sleep(1)    task.cancel()    try:        await task    except asyncio.CancelledError:        print("main(): cancel_me foi cancelado agora")asyncio.run(main())# Saída esperada:##     cancel_me(): antes de dormir#     cancel_me(): cancelar sono#     cancel_me(): depois de dormir#     main(): cancel_me foi cancelado agora

   cancelled()

      Retorna "True" se a Tarefa for *cancelada*.

      A Tarefa é *cancelada* quando o cancelamento foi requisitado com
      "cancel()" e a corrotina contida propagou a exceção
      "CancelledError" gerada nela.

   uncancel()

      Decrement the count of cancellation requests to this Task.

      Retorna o número restante de pedidos de cancelamento.

      Note que, uma vez concluída a execução de uma tarefa cancelada,
      chamadas adicionais para "uncancel()" são ineficazes.

      Adicionado na versão 3.11.

      This method is used by asyncio's internals and isn't expected to
      be used by end-user code.  In particular, if a Task gets
      successfully uncancelled, this allows for elements of structured
      concurrency like Task groups and "asyncio.timeout()" to continue
      running, isolating cancellation to the respective structured
      block. For example:

         async def make_request_with_timeout():    try:        async with asyncio.timeout(1):            # Bloco estruturado afetado pelo timeout:            await make_request()            await make_another_request()    except TimeoutError:        log("Ocorreu um timeout")    # Código externo não afetado pelo timeout:    await unrelated_code()

      Enquanto o bloco com "make_request()" e "make_another_request()"
      possa ser cancelado devido ao timeout, "unrelated_code()" deve
      continuar a executar mesmo em caso de timeout. Isto é
      implementado com "uncancel()". Os gerenciadores de contexto
      "TaskGroup" usam "uncancel()" de forma semelhante.

      Se o código do usuário final, por alguma razão, estiver
      suprimindo o cancelamento ao capturar "CancelledError", precisa
      chamar este método para remover o estado de cancelamento.

      Quando este método decrementa a contagem de cancelamentos para
      zero, verifica se uma chamada anterior a "cancel()" tinha
      preparado para que "CancelledError" fosse lançado na tarefa. Se
      ainda não tiver sido lançado, esse preparo será revogado
      (redefinindo o sinalizador interna "_must_cancel").

   Alterado na versão 3.13: Alterado para revogar os pedidos de
   cancelamento pendentes ao atingir zero.

   cancelling()

      Return the number of pending cancellation requests to this Task,
      i.e., the number of calls to "cancel()" less the number of
      "uncancel()" calls.

      Note that if this number is greater than zero but the Task is
      still executing, "cancelled()" will still return "False". This
      is because this number can be lowered by calling "uncancel()",
      which can lead to the task not being cancelled after all if the
      cancellation requests go down to zero.

      Este método é usado pelos internos do asyncio e não é esperado
      que seja usado por código do usuário final. Consulte
      "uncancel()" para mais detalhes.

      Adicionado na versão 3.11.
