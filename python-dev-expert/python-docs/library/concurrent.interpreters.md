"concurrent.interpreters" --- Múltiplos interpretadores no mesmo processo
*************************************************************************

Adicionado na versão 3.14.

**Source code:** Lib/concurrent/interpreters

======================================================================

O módulo "concurrent.interpreters" constrói interfaces de nível mais
alto sobre o módulo de mais baixo nível "_interpreters".

O objetivo principal do módulo é fornecer uma API básica para
gerenciar interpretadores (também conhecidos como
"subinterpretadores") e executar operações neles. A execução envolve
principalmente a mudança para um interpretador (na thread atual) e a
chamada de uma função nesse contexto de execução.

For concurrency, interpreters themselves (and this module) don't
provide much more than isolation, which on its own isn't useful.
Actual concurrency is available separately through "threads" -- see
below.

Ver também:

  "InterpreterPoolExecutor"
     Combina threads com interpretadores em uma interface familiar.

  Isolando módulos de extensão
     Como atualizar um módulo de extensão para suporte a vários
     interpretadores.

  **PEP 554**

  **PEP 734**

  **PEP 684**

Disponibilidade: not WASI.

Este módulo não funciona ou não está disponível em WebAssembly. Veja
Plataformas WebAssembly para mais informações.


Detalhes chaves
===============

Antes de prosseguirmos, há um pequeno número de detalhes que devem ser
lembrados sobre o uso de múltiplos interpretadores:

* isolado, por padrão

* nenhuma thread implícita

* nem todos os pacotes PyPI oferecem suporte ao uso em múltiplos
  interpretadores ainda


Introdução
==========

An "interpreter" is effectively the execution context of the Python
runtime.  It contains all of the state the runtime needs to execute a
program.  This includes things like the import state and builtins.
(Each thread, even if there's only the main thread, has some extra
runtime state, in addition to the current interpreter, related to the
current exception and the bytecode eval loop.)

The concept and functionality of the interpreter have been a part of
Python since version 2.2, but the feature was only available through
the C-API and not well known, and the isolation was relatively
incomplete until version 3.12.


Multiple Interpreters and Isolation
-----------------------------------

A Python implementation may support using multiple interpreters in the
same process.  CPython has this support.  Each interpreter is
effectively isolated from the others (with a limited number of
carefully managed process-global exceptions to the rule).

That isolation is primarily useful as a strong separation between
distinct logical components of a program, where you want to have
careful control of how those components interact.

Nota:

  Interpreters in the same process can technically never be strictly
  isolated from one another since there are few restrictions on memory
  access within the same process.  The Python runtime makes a best
  effort at isolation but extension modules may easily violate that.
  Therefore, do not use multiple interpreters in security-sensitive
  situations, where they shouldn't have access to each other's data.


Running in an Interpreter
-------------------------

Running in a different interpreter involves switching to it in the
current thread and then calling some function.  The runtime will
execute the function using the current interpreter's state.  The
"concurrent.interpreters" module provides a basic API for creating and
managing interpreters, as well as the switch-and-call operation.

No other threads are automatically started for the operation. There is
a helper for that though. There is another dedicated helper for
calling the builtin "exec()" in an interpreter.

When "exec()" (or "eval()") are called in an interpreter, they run
using the interpreter's "__main__" module as the "globals" namespace.
The same is true for functions that aren't associated with any module.
This is the same as how scripts invoked from the command-line run in
the "__main__" module.


Concurrency and Parallelism
---------------------------

As noted earlier, interpreters do not provide any concurrency on their
own.  They strictly represent the isolated execution context the
runtime will use *in the current thread*.  That isolation makes them
similar to processes, but they still enjoy in-process efficiency, like
threads.

All that said, interpreters do naturally support certain flavors of
concurrency. There's a powerful side effect of that isolation.  It
enables a different approach to concurrency than you can take with
async or threads.  It's a similar concurrency model to CSP or the
actor model, a model which is relatively easy to reason about.

You can take advantage of that concurrency model in a single thread,
switching back and forth between interpreters, Stackless-style.
However, this model is more useful when you combine interpreters with
multiple threads.  This mostly involves starting a new thread, where
you switch to another interpreter and run what you want there.

Each actual thread in Python, even if you're only running in the main
thread, has its own *current* execution context.  Multiple threads can
use the same interpreter or different ones.

At a high level, you can think of the combination of threads and
interpreters as threads with opt-in sharing.

As a significant bonus, interpreters are sufficiently isolated that
they do not share the *GIL*, which means combining threads with
multiple interpreters enables full multi-core parallelism. (This has
been the case since Python 3.12.)


Communication Between Interpreters
----------------------------------

In practice, multiple interpreters are useful only if we have a way to
communicate between them.  This usually involves some form of message
passing, but can even mean sharing data in some carefully managed way.

With this in mind, the "concurrent.interpreters" module provides a
"queue.Queue" implementation, available through "create_queue()".


"Sharing" Objects
-----------------

Any data actually shared between interpreters loses the thread-safety
provided by the *GIL*.  There are various options for dealing with
this in extension modules.  However, from Python code the lack of
thread-safety means objects can't actually be shared, with a few
exceptions.  Instead, a copy must be created, which means mutable
objects won't stay in sync.

By default, most objects are copied with "pickle" when they are passed
to another interpreter.  Nearly all of the immutable builtin objects
are either directly shared or copied efficiently.  For example:

* "None"

* "bool" ("True" and "False")

* "bytes"

* "str"

* "int"

* "float"

* "tuple" (of similarly supported objects)

There are a small number of Python types that actually share mutable
data between interpreters:

* "memoryview"

* "Queue"


Referência
==========

Este módulo define as seguintes funções:

concurrent.interpreters.list_all()

   Retorna "list" de objetos "Interpreter", um para cada interpretador
   existente.

concurrent.interpreters.get_current()

   Retorna um objeto "Interpreter" para o interpretador em execução no
   momento.

concurrent.interpreters.get_main()

   Return an "Interpreter" object for the main interpreter. This is
   the interpreter the runtime created to run the *REPL* or the script
   given at the command-line.  It is usually the only one.

concurrent.interpreters.create()

   Inicializa um novo interpretador Python (ocioso) e retorna um
   objeto "Interpreter" para ele.

concurrent.interpreters.create_queue(maxsize=0)

   Initialize a new cross-interpreter queue and return a "Queue"
   object for it.

   *maxsize* is an integer that sets the upperbound limit on the
   number of items that can be placed in the queue. Insertion will be
   blocked once this size has been reached, until queue items are
   consumed. If *maxsize* is less than or equal to zero, the queue
   size is infinite.


Objetos interpretador
---------------------

class concurrent.interpreters.Interpreter(id)

   Um único interpretador no processo atual.

   Geralmente, "Interpreter" não deve ser chamado diretamente. Em vez
   disso, use "create()" ou uma das outras funções do módulo.

   id

      (somente leitura)

      The underlying interpreter's ID.

   whence

      (somente leitura)

      Uma string descrevendo de onde o interpretador veio.

   is_running()

      Retorna "True" se o interpretador estiver executando código em
      seu módulo "__main__" e "False" caso contrário.

   close()

      Finaliza e destrói o interpretador.

   prepare_main(ns=None, **kwargs)

      Bind objects in the interpreter's "__main__" module.

      Some objects are actually shared and some are copied
      efficiently, but most are copied via "pickle".  See "Sharing"
      Objects.

   exec(code, /)

      Executa o código-fonte fornecido no interpretador (na thread
      atual).

   call(callable, /, *args, **kwargs)

      Return the result of running the given function in the
      interpreter (in the current thread).

   call_in_thread(callable, /, *args, **kwargs)

      Executa a função fornecida no interpretador (em uma nova
      thread).


Exceções
--------

exception concurrent.interpreters.InterpreterError

   Esta exceção, uma subclasse de "Exception", é levantada quando
   ocorre um erro relacionado ao interpretador.

exception concurrent.interpreters.InterpreterNotFoundError

   Esta exceção, uma subclasse de "InterpreterError", é levantada
   quando o interpretador de destino não existe mais.

exception concurrent.interpreters.ExecutionFailed

   Esta exceção, uma subclasse de "InterpreterError", é levantada
   quando o código em execução levanta uma exceção não capturada.

   excinfo

      Um snapshot básico da exceção levantada no outro interpretador.

exception concurrent.interpreters.NotShareableError

   Esta exceção, uma subclasse de "TypeError", é levantada quando um
   objeto não pode ser enviado para outro interpretador.


Communicating Between Interpreters
----------------------------------

class concurrent.interpreters.Queue(id)

   A wrapper around a low-level, cross-interpreter queue, which
   implements all the methods of "queue.Queue" except for
   "task_done()", "join()" and "shutdown()".  The underlying queue can
   only be created through "create_queue()".

   Some objects are actually shared and some are copied efficiently,
   but most are copied via "pickle".  See "Sharing" Objects.

   id

      (somente leitura)

      The queue's ID.

   qsize()

      Retorna o número de itens na fila.

   empty()

      Retorna "True" se a fila estiver vazia, "False" caso contrário.

   full()

      Return "True" if the queue is full, "False" otherwise.

   put(obj, block=True, timeout=None)

      Put *obj* into the queue.  If optional args *block* is true and
      *timeout* is "None" (the default), block if necessary until a
      free slot is available.  If *timeout* is a positive number, it
      blocks at most *timeout* seconds and raises the "QueueFull"
      exception if no free slot was available within that time.
      Otherwise (*block* is false), put an object on the queue if a
      free slot is immediately available, else raise the "QueueFull"
      exception (*timeout* is ignored in that case).

   put_nowait(obj)

      Equivalent to "put(obj, block=False)".

   get(block=True, timeout=None)

      Remove and return an object from the queue.  If optional args
      *block* is true and *timeout* is "None" (the default), block if
      necessary until an object is available.  If *timeout* is a
      positive number, it blocks at most *timeout* seconds and raises
      the "QueueEmpty" exception if no object was available within
      that time.  Otherwise (*block* is false), return an object if
      one is immediately available, else raise the "QueueEmpty"
      exception (*timeout* is ignored in that case).

   get_nowait()

      Equivalent to "get(block=False)".

exception concurrent.interpreters.QueueEmpty

   This exception, a subclass of "queue.Empty", is raised from
   "Queue.get()" and "Queue.get_nowait()" when the queue is empty.

exception concurrent.interpreters.QueueFull

   This exception, a subclass of "queue.Full", is raised from
   "Queue.put()" and "Queue.put_nowait()" when the queue is full.


Uso básico
==========

Criando um interpretador e executando código nele:

   from concurrent import interpreters

   interp = interpreters.create()

   # Executa na thread atual do SO.

   interp.exec('print("spam!")')

   interp.exec("""if True:
       print('spam!')
       """)

   from textwrap import dedent
   interp.exec(dedent("""
       print('spam!')
       """))

   def run(arg):
       return arg

   res = interp.call(run, 'spam!')
   print(res)

   def run():
       print('spam!')

   interp.call(run)

   # Executa em uma nova thread do SO.

   t = interp.call_in_thread(run)
   t.join()

Communicating between interpreters with a queue:

   from concurrent import interpreters

   interp = interpreters.create()
   queue = interpreters.create_queue()

   def worker(queue):
       queue.put('spam!')

   t = interp.call_in_thread(worker, queue)
   print(queue.get())
   t.join()
