Desenvolvendo com asyncio
*************************

A programação assíncrona é diferente da programação “sequencial”
clássica.

Esta página lista erros e armadilhas comuns e explica como evitá-los.


Modo de Depuração
=================

Por padrão, o asyncio é executado em modo de produção. Para facilitar
o desenvolvimento, o asyncio fornece um modo de depuração.

Há várias maneiras de habilitar o modo de depuração do asyncio:

* Definindo a variável de ambiente "PYTHONASYNCIODEBUG" como "1".

* Usando o Modo de Desenvolvimento do Python.

* Passando "debug=True" para "asyncio.run()".

* Chamando "loop.set_debug()".

Além de habilitar o modo de depuração, considere também:

* setting the log level of the asyncio logger to "logging.DEBUG", for
  example the following snippet of code can be run at startup of the
  application:

     logging.basicConfig(level=logging.DEBUG)

* configurando o módulo "warnings" para exibir avisos
  "ResourceWarning". Uma forma de fazer isso é usando a opção de linha
  de comando: "-W" "default".

Quando o modo de depuração está habilitado:

* Muitas APIs do asyncio que não são thread-safe (como os métodos
  "loop.call_soon()" e "loop.call_at()") levantam uma exceção se forem
  chamadas a partir de uma thread incorreta.

* O tempo de execução de um seletor de E/S é registrado se demorar
  muito para executar a operação E/S.

* Funções de retorno demorando mais do que 100 milissegundos são
  registradas. O atributo "loop.slow_callback_duration" pode ser usado
  para definir a duração de execução mínima em segundos para se
  considerada "devagar".


Concorrência e Múltiplas Threads
================================

Um laço de eventos é executado em uma thread (geralmente a thread
principal) e executa todos as funções de retorno e Tasks nessa mesma
thread. Enquanto uma Task está em execução no laço de eventos, nenhuma
outra Task pode ser executada na mesma thread. Quando uma Task executa
uma expressão "await", a Task em execução é suspensa, e o laço de
eventos passa a executar a próxima Task.

Para agendar uma *callback* de outra thread do SO, o método
"loop.call_soon_threadsafe()" deve ser usado. Exemplo:

   loop.call_soon_threadsafe(callback, *args)

Quase todos os objetos do asyncio não são seguros para threads, o que
normalmente não é um problema, a menos que exista código que funcione
com eles fora de uma Task ou de um callback. Se houver a necessidade
de esse tipo de código chamar uma API de baixo nível do asyncio, o
método "loop.call_soon_threadsafe()" deve ser usado, por exemplo:

   loop.call_soon_threadsafe(fut.cancel)

Para agendar um objeto corrotina a partir de uma thread diferente do
sistema operacional, a função "run_coroutine_threadsafe()" deve ser
usada. Ela retorna um "concurrent.futures.Future". para acessar o
resultado:

   async def coro_func():
        return await asyncio.sleep(1, 42)

   # Later in another OS thread:

   future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
   # Wait for the result:
   result = future.result()

Para manipular sinais, o laço de eventos deve ser executado na thread
principal.

O método "loop.run_in_executor()" pode ser usado com um
"concurrent.futures.ThreadPoolExecutor" ou "InterpreterPoolExecutor"
para executar o código de bloqueio em uma thread de sistema
operacional diferente, sem bloquear a thread de sistema operacional na
qual o laço de eventos é executado.

There is currently no way to schedule coroutines or callbacks directly
from a different process (such as one started with "multiprocessing").
The Event loop methods section lists APIs that can read from pipes and
watch file descriptors without blocking the event loop. In addition,
asyncio's Subprocess APIs provide a way to start a process and
communicate with it from the event loop. Lastly, the aforementioned
"loop.run_in_executor()" method can also be used with a
"concurrent.futures.ProcessPoolExecutor" to execute code in a
different process.


Executando código bloqueante
============================

O código bloqueante (vinculada à CPU) não deve ser chamado
diretamente. Por exemplo, se uma função executa um cálculo pesado de
CPU durante 1 segundo, todas as Tasks concorrentes do asyncio e as
operações de E/S serão atrasadas por 1 segundo.

Um executor pode ser usado para executar uma tarefa em uma thread
diferente, incluindo em um interpretador diferente, ou até mesmo em um
processo diferente, para evitar bloquear a thread do sistema
operacional onde o laço de eventos está sendo executado. Consulte o
método "loop.run_in_executor()" para mais detalhes.


Gerando logs
============

asyncio usa o módulo "logging" e todo registro é feito via o
registrador ""asyncio"".

O nível padrão de log é "logging.INFO", que pode ser facilmente
ajustado:

   logging.getLogger("asyncio").setLevel(logging.WARNING)

Logging de rede pode bloquear o laço de eventos. Recomenda-se usar uma
thread separada para lidar com os logs ou usar E/S não bloqueante. Por
exemplo, veja Dealing with handlers that block.


Detectar corrotinas nunca aguardadas
====================================

Quando uma função de corrotina é chamada, mas não é aguardada (por
exemplo, "coro()" em vez de "await coro()") ou a corrotina não é
agendada com "asyncio.create_task()", o asyncio emitirá um
"RuntimeWarning":

   import asyncio

   async def test():
       print("never scheduled")

   async def main():
       test()

   asyncio.run(main())

Saída:

   test.py:7: RuntimeWarning: coroutine 'test' was never awaited
     test()

Saída no modo de depuração:

   test.py:7: RuntimeWarning: coroutine 'test' was never awaited
   Coroutine created at (most recent call last)
     File "../t.py", line 9, in <module>
       asyncio.run(main(), debug=True)

     < .. >

     File "../t.py", line 7, in main
       test()
     test()

A correção usual é aguardar a corrotina ou chamar a função
"asyncio.create_task()":

   async def main():
       await test()


Detectar exceções nunca recuperadas
===================================

Se um "Future.set_exception()" é chamado, mas o objeto Future nunca é
aguardado, a exceção nunca será propagada para o código do usuário.
Nesse caso, o asyncio emitirá uma mensagem de log quando o objeto
Future for coletado pela coleta de lixo.

Exemplo de uma exceção não tratada:

   import asyncio

   async def bug():
       raise Exception("not consumed")

   async def main():
       asyncio.create_task(bug())

   asyncio.run(main())

Saída:

   Task exception was never retrieved
   future: <Task finished coro=<bug() done, defined at test.py:3>
     exception=Exception('not consumed')>

   Traceback (most recent call last):
     File "test.py", line 4, in bug
       raise Exception("not consumed")
   Exception: not consumed

Enable the debug mode to get the traceback where the task was created:

   asyncio.run(main(), debug=True)

Saída no modo de depuração:

   Task exception was never retrieved
   future: <Task finished coro=<bug() done, defined at test.py:3>
       exception=Exception('not consumed') created at asyncio/tasks.py:321>

   source_traceback: Object created at (most recent call last):
     File "../t.py", line 9, in <module>
       asyncio.run(main(), debug=True)

   < .. >

   Traceback (most recent call last):
     File "../t.py", line 4, in bug
       raise Exception("not consumed")
   Exception: not consumed


Asynchronous generators best practices
======================================

Writing correct and efficient asyncio code requires awareness of
certain pitfalls. This section outlines essential best practices that
can save you hours of debugging.


Close asynchronous generators explicitly
----------------------------------------

It is recommended to manually close the *asynchronous generator*. If a
generator exits early - for example, due to an exception raised in the
body of an "async for" loop - its asynchronous cleanup code may run in
an unexpected context. This can occur after the tasks it depends on
have completed, or during the event loop shutdown when the async-
generator's garbage collection hook is called.

To avoid this, explicitly close the generator by calling its
"aclose()" method, or use the "contextlib.aclosing()" context manager:

   import asyncio
   import contextlib

   async def gen():
     yield 1
     yield 2

   async def func():
     async with contextlib.aclosing(gen()) as g:
       async for x in g:
         break  # Don't iterate until the end

   asyncio.run(func())

As noted above, the cleanup code for these asynchronous generators is
deferred. The following example demonstrates that the finalization of
an asynchronous generator can occur in an unexpected order:

   import asyncio
   work_done = False

   async def cursor():
       try:
           yield 1
       finally:
           assert work_done

   async def rows():
       global work_done
       try:
           yield 2
       finally:
           await asyncio.sleep(0.1) # imitate some async work
           work_done = True


   async def main():
       async for c in cursor():
           async for r in rows():
               break
           break

   asyncio.run(main())

For this example, we get the following output:

   unhandled exception during asyncio.run() shutdown
   task: <Task finished name='Task-3' coro=<<async_generator_athrow without __name__>()> exception=AssertionError()>
   Traceback (most recent call last):
     File "example.py", line 6, in cursor
       yield 1
   asyncio.exceptions.CancelledError

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "example.py", line 8, in cursor
       assert work_done
              ^^^^^^^^^
   AssertionError

The "cursor()" asynchronous generator was finalized before the "rows"
generator - an unexpected behavior.

The example can be fixed by explicitly closing the "cursor" and "rows"
async-generators:

   async def main():
       async with contextlib.aclosing(cursor()) as cursor_gen:
           async for c in cursor_gen:
               async with contextlib.aclosing(rows()) as rows_gen:
                   async for r in rows_gen:
                       break
               break


Create asynchronous generators only when the event loop is running
------------------------------------------------------------------

It is recommended to create *asynchronous generators* only after the
event loop has been created.

To ensure that asynchronous generators close reliably, the event loop
uses the "sys.set_asyncgen_hooks()" function to register callback
functions. These callbacks update the list of running asynchronous
generators to keep it in a consistent state.

When the "loop.shutdown_asyncgens()" function is called, the running
generators are stopped gracefully and the list is cleared.

The asynchronous generator invokes the corresponding system hook
during its first iteration. At the same time, the generator records
that the hook has been called and does not call it again.

Therefore, if iteration begins before the event loop is created, the
event loop will not be able to add the generator to its list of active
generators because the hooks are set after the generator attempts to
call them. Consequently, the event loop will not be able to terminate
the generator if necessary.

Considere o exemplo a seguir:

   import asyncio

   async def agenfn():
       try:
           yield 10
       finally:
           await asyncio.sleep(0)


   with asyncio.Runner() as runner:
       agen = agenfn()
       print(runner.run(anext(agen)))
       del agen

Saída:

   10
   Exception ignored while closing generator <async_generator object agenfn at 0x000002F71CD10D70>:
   Traceback (most recent call last):
     File "example.py", line 13, in <module>
       del agen
           ^^^^
   RuntimeError: async generator ignored GeneratorExit

This example can be fixed as follows:

   import asyncio

   async def agenfn():
       try:
           yield 10
       finally:
           await asyncio.sleep(0)

   async def main():
       agen = agenfn()
       print(await anext(agen))
       del agen

   asyncio.run(main())


Avoid concurrent iteration and closure of the same generator
------------------------------------------------------------

Async generators may be reentered while another "__anext__()" /
"athrow()" / "aclose()" call is in progress. This may lead to an
inconsistent state of the async generator and can cause errors.

Let's consider the following example:

   import asyncio

   async def consumer():
       for idx in range(100):
           await asyncio.sleep(0)
           message = yield idx
           print('received', message)

   async def amain():
       agenerator = consumer()
       await agenerator.asend(None)

       fa = asyncio.create_task(agenerator.asend('A'))
       fb = asyncio.create_task(agenerator.asend('B'))
       await fa
       await fb

   asyncio.run(amain())

Saída:

   received A
   Traceback (most recent call last):
     File "test.py", line 38, in <module>
       asyncio.run(amain())
       ~~~~~~~~~~~^^^^^^^^^
     File "Lib/asyncio/runners.py", line 204, in run
       return runner.run(main)
              ~~~~~~~~~~^^^^^^
     File "Lib/asyncio/runners.py", line 127, in run
       return self._loop.run_until_complete(task)
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
     File "Lib/asyncio/base_events.py", line 719, in run_until_complete
       return future.result()
              ~~~~~~~~~~~~~^^
     File "test.py", line 36, in amain
       await fb
   RuntimeError: anext(): asynchronous generator is already running

Therefore, it is recommended to avoid using asynchronous generators in
parallel tasks or across multiple event loops.
