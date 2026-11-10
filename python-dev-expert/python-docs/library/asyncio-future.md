Futuros
*******

**Código-fonte:** Lib/asyncio/futures.py, Lib/asyncio/base_futures.py

======================================================================

Objetos *Future* são usados para fazer a ponte entre **código baseado
em funções de retorno (callback) de baixo nível** e  código
async/await de alto nível.


Funções Future
==============

asyncio.isfuture(obj)

   Return "True" if *obj* is either of:

   * an instance of "asyncio.Future",

   * an instance of "asyncio.Task",

   * a Future-like object with a "_asyncio_future_blocking" attribute.

   Adicionado na versão 3.5.

asyncio.ensure_future(obj, *, loop=None)

   Retorna:

   * *obj* argument as is, if *obj* is a "Future", a "Task", or a
     Future-like object ("isfuture()" is used for the test.)

   * a "Task" object wrapping *obj*, if *obj* is a coroutine
     ("iscoroutine()" is used for the test); in this case the
     coroutine will be scheduled by "ensure_future()".

   * a "Task" object that would await on *obj*, if *obj* is an
     awaitable ("inspect.isawaitable()" is used for the test.)

   If *obj* is neither of the above a "TypeError" is raised.

   Importante:

     Save a reference to the result of this function, to avoid a task
     disappearing mid-execution.See also the "create_task()" function
     which is the preferred way for creating new tasks or use
     "asyncio.TaskGroup" which keeps reference to the task internally.

   Alterado na versão 3.5.1: The function accepts any *awaitable*
   object.

   Descontinuado desde a versão 3.10: Deprecation warning is emitted
   if *obj* is not a Future-like object and *loop* is not specified
   and there is no running event loop.

asyncio.wrap_future(future, *, loop=None)

   Wrap a "concurrent.futures.Future" object in a "asyncio.Future"
   object.

   Descontinuado desde a versão 3.10: Deprecation warning is emitted
   if *future* is not a Future-like object and *loop* is not specified
   and there is no running event loop.


Objeto Future
=============

class asyncio.Future(*, loop=None)

   Um Future representa um resultado eventual de uma operação
   assíncrona.  Não é seguro para thread.

   Future é um objeto *aguardável*. Corrotinas podem aguardar o objeto
   Future até que ele tenha um resultado ou um conjunto de exceções,
   ou até que seja cancelado. Um Future pode ser aguardado várias
   vezes e o resultado é sempre o mesmo.

   Normalmente, objetos Future são usados para permitir que o código
   baseado em funções de retorno de baixo nível (por exemplo, em
   protocolos implementados usando transportes asyncio) interopere com
   o código async/await de alto nível.

   A regra geral é nunca expor o objeto Future em API voltada para o
   usuário, e a maneira recomendada de criar um objeto Future objeto
   chamar "loop.create_future()".  Dessa forma, as implementações de
   laços de eventos alternativos podem injetar suas próprias versões
   otimizadas de um objeto Future.

   Futures are generic over the type of their results.

   Alterado na versão 3.7: Adicionado suporte ao módulo "contextvars".

   Descontinuado desde a versão 3.10: Aviso de descontinuidade é
   emitido se *loop* não é especificado e não existe nenhum laço de
   eventos em execução.

   result()

      Return the result of the Future.

      If the Future is *done* and has a result set by the
      "set_result()" method, the result value is returned.

      If the Future is *done* and has an exception set by the
      "set_exception()" method, this method raises the exception.

      Se o futuro foi *cancelled*, este método levanta uma exceção
      "CancelledError".

      If the Future's result isn't yet available, this method raises
      an "InvalidStateError" exception.

   set_result(result)

      Mark the Future as *done* and set its result.

      Raises an "InvalidStateError" error if the Future is already
      *done*.

   set_exception(exception)

      Mark the Future as *done* and set an exception.

      Raises an "InvalidStateError" error if the Future is already
      *done*.

   done()

      Return "True" if the Future is *done*.

      A Future is *done* if it was *cancelled* or if it has a result
      or an exception set with "set_result()" or "set_exception()"
      calls.

   cancelled()

      Return "True" if the Future was *cancelled*.

      The method is usually used to check if a Future is not
      *cancelled* before setting a result or an exception for it:

         if not fut.cancelled():
             fut.set_result(42)

   add_done_callback(callback, *, context=None)

      Add a callback to be run when the Future is *done*.

      The *callback* is called with the Future object as its only
      argument.

      If the Future is already *done* when this method is called, the
      callback is scheduled with "loop.call_soon()".

      Um argumento opcional somente-nomeado *context* permite
      especificar um "contextvars.Context" customizado para executar
      na *função de retorno*. O contexto atual é usado quando nenhum
      *context* é fornecido.

      "functools.partial()" can be used to pass parameters to the
      callback, e.g.:

         # Call 'print("Future:", fut)' when "fut" is done.
         fut.add_done_callback(
             functools.partial(print, "Future:"))

      Alterado na versão 3.7: O parâmetro somente-nomeado *context*
      foi adicionado. Veja **PEP 567** para mais detalhes.

   remove_done_callback(callback)

      Remove *callback* da lista de funções de retorno.

      Returns the number of callbacks removed, which is typically 1,
      unless a callback was added more than once.

   cancel(msg=None)

      Cancel the Future and schedule callbacks.

      If the Future is already *done* or *cancelled*, return "False".
      Otherwise, change the Future's state to *cancelled*, schedule
      the callbacks, and return "True".

      The optional string argument *msg* is passed as the argument to
      the "CancelledError" exception raised when a cancelled Future is
      awaited.

      Alterado na versão 3.9: Adicionado o  parâmetro *msg*.

   exception()

      Return the exception that was set on this Future.

      The exception (or "None" if no exception was set) is returned
      only if the Future is *done*.

      Se o futuro foi *cancelled*, este método levanta uma exceção
      "CancelledError".

      If the Future isn't *done* yet, this method raises an
      "InvalidStateError" exception.

   get_loop()

      Return the event loop the Future object is bound to.

      Adicionado na versão 3.7.

This example creates a Future object, creates and schedules an
asynchronous Task to set result for the Future, and waits until the
Future has a result:

   async def set_after(fut, delay, value):
       # Sleep for *delay* seconds.
       await asyncio.sleep(delay)

       # Set *value* as a result of *fut* Future.
       fut.set_result(value)

   async def main():
       # Get the current event loop.
       loop = asyncio.get_running_loop()

       # Create a new Future object.
       fut = loop.create_future()

       # Run "set_after()" coroutine in a parallel Task.
       # We are using the low-level "loop.create_task()" API here because
       # we already have a reference to the event loop at hand.
       # Otherwise we could have just used "asyncio.create_task()".
       loop.create_task(
           set_after(fut, 1, '... world'))

       print('hello ...')

       # Wait until *fut* has a result (1 second) and print it.
       print(await fut)

   asyncio.run(main())

Importante:

  The Future object was designed to mimic "concurrent.futures.Future".
  Key differences include:

  * unlike asyncio Futures, "concurrent.futures.Future" instances
    cannot be awaited.

  * "asyncio.Future.result()" and "asyncio.Future.exception()" do not
    accept the *timeout* argument.

  * "asyncio.Future.result()" and "asyncio.Future.exception()" raise
    an "InvalidStateError" exception when the Future is not *done*.

  * Callbacks registered with "asyncio.Future.add_done_callback()" are
    not called immediately.  They are scheduled with
    "loop.call_soon()" instead.

  * asyncio Future is not compatible with the
    "concurrent.futures.wait()" and
    "concurrent.futures.as_completed()" functions.

  * "asyncio.Future.cancel()" accepts an optional "msg" argument, but
    "concurrent.futures.Future.cancel()" does not.
