"multiprocessing" --- Paralelismo baseado em processo
*****************************************************

**Código-fonte:** Lib/multiprocessing/

======================================================================

Disponibilidade: not Android, not iOS, not WASI.

Este módulo não tem suporte em plataformas móveis ou plataformas
WebAssembly.


Introdução
==========

"multiprocessing" is a package that supports spawning processes using
an API similar to the "threading" module.  The "multiprocessing"
package offers both local and remote concurrency, effectively side-
stepping the *Global Interpreter Lock* by using subprocesses instead
of threads.  Due to this, the "multiprocessing" module allows the
programmer to fully leverage multiple processors on a given machine.
It runs on both POSIX and Windows.

The "multiprocessing" module also introduces the "Pool" object which
offers a convenient means of parallelizing the execution of a function
across multiple input values, distributing the input data across
processes (data parallelism).  The following example demonstrates the
common practice of defining such functions in a module so that child
processes can successfully import that module.  This basic example of
data parallelism using "Pool",

   from multiprocessing import Pool

   def f(x):
       return x*x

   if __name__ == '__main__':
       with Pool(5) as p:
           print(p.map(f, [1, 2, 3]))

vai exibir na saída padrão

   [1, 4, 9]

The "multiprocessing" module also introduces APIs which do not have
analogs in the "threading" module, like the ability to "terminate",
"interrupt" or "kill" a running process.

Ver também:

  "concurrent.futures.ProcessPoolExecutor" oferece uma interface de
  nível mais alto para enviar tarefas para um processo em segundo
  plano sem bloquear a execução do processo de chamada. Comparado ao
  uso direto da interface "Pool", a API "concurrent.futures" permite
  mais prontamente que o envio de trabalho para o pool de processos
  subjacente seja separado da espera pelos resultados.


A classe "Process"
------------------

In "multiprocessing", processes are spawned by creating a "Process"
object and then calling its "start()" method.  "Process" follows the
API of "threading.Thread".  A trivial example of a multiprocess
program is

   from multiprocessing import Process

   def f(name):
       print('hello', name)

   if __name__ == '__main__':
       p = Process(target=f, args=('bob',))
       p.start()
       p.join()

Para mostrar os IDs de processo individuais envolvidos, aqui está um
exemplo expandido:

   from multiprocessing import Process
   import os

   def info(title):
       print(title)
       print('module name:', __name__)
       print('parent process:', os.getppid())
       print('process id:', os.getpid())

   def f(name):
       info('function f')
       print('hello', name)

   if __name__ == '__main__':
       info('main line')
       p = Process(target=f, args=('bob',))
       p.start()
       p.join()

Para uma explicação do porquê a parte "if __name__ == '__main__'" é
necessária, veja Programming guidelines.

The arguments to "Process" usually need to be picklable so they can be
passed to the child process. If you tried typing the above example
directly into a REPL it could lead to an "AttributeError" in the child
process trying to locate the *f* function in the "__main__" module.


Contextos e métodos de inicialização
------------------------------------

Depending on the platform, "multiprocessing" supports three ways to
start a process.  These *start methods* are

   *spawn*
      O processo pai inicia um novo processo do interpretador Python.
      O processo filho herdará apenas os recursos necessários para
      executar o método "run()" do objeto do processo. Em particular,
      descritores de arquivo e identificadores desnecessários do
      processo pai não serão herdados. Iniciar um processo usando esse
      método é bem lento comparado a usar *fork* ou *forkserver*.

      Disponível em plataformas POSIX e Windows. O padrão no Windows e
      macOS.

   *fork*
      O processo pai usa "os.fork()" para criar um fork do
      interpretador Python. O processo filho, quando começa, é
      efetivamente idêntico ao processo pai. Todos os recursos do pai
      são herdados pelo processo filho. Observe que criar um fork com
      segurança de um processo multithread é problemático.

      Disponível em sistemas POSIX.

      Alterado na versão 3.14: Esse não é mais o método de
      inicialização padrão em nenhuma plataforma. O código que requer
      *fork* deve especificar explicitamente isso por meio de
      "get_context()" ou "set_start_method()".

      Alterado na versão 3.12: Se o Python for capaz de detectar que
      seu processo tem várias threads, a função "os.fork()" que esse
      método de inicialização chama internamente levantará
      "DeprecationWarning". Use um método de inicialização diferente.
      Veja a documentação de "os.fork()" para mais explicações.

   *forkserver*
      Quando o programa é inicializado e seleciona o método
      *forkserver*, um processo de servidor é gerado. A partir disso,
      sempre que um novo processo é necessário, o processo pai
      conecta-se ao servidor e solicita que um novo processo seja
      feito um fork. O processo fork do servidor é de thread única, a
      menos que bibliotecas do sistema ou importações pré-carregadas
      gerem threads como um efeito colateral; neste sentido,
      geralmente é seguro usar "os.fork()". Nenhum recurso
      desnecessário é herdado.

      Available on POSIX platforms which support passing file
      descriptors over Unix pipes such as Linux.  The default on
      those, unless there is no writable temporary directory (see
      "tempfile.gettempdir()"), which the fork server requires;
      *spawn* is the default in that case.

      Alterado na versão 3.14: Isso se tornou o método de
      inicialização padrão nas plataformas POSIX.

      Alterado na versão 3.15.1: *spawn* is now the default start
      method when there is no writable temporary directory, for
      example on a read-only file system. Previously *forkserver*
      remained the default there and starting a process failed with an
      "OSError".  The default is determined when it is first needed
      rather than when "multiprocessing" is imported.  See gh-155717.

Alterado na versão 3.4: *spawn* adicionado em todas as plataformas
POSIX, e *forkserver* adicionado para algumas plataformas POSIX.
Processos filhos não herdam mais todos os identificadores herdáveis
dos pais no Windows.

Alterado na versão 3.8: No macOS, o método de inicialização *spawn*
agora é o padrão. O método *fork* deve ser considerado inseguro, pois
pode levar a travamentos do subprocesso, uma vez que as bibliotecas do
sistema macOS podem iniciar threads. Consulte bpo-33725.

Alterado na versão 3.14: Nas plataformas POSIX, o método de
inicialização padrão foi alterado de *fork* para *forkserver* para
manter o desempenho, mas evitar incompatibilidades comuns de processos
multithreads. Consulte gh-84559.

No POSIX, usar os métodos de inicialização *spawn* ou *forkserver*
também iniciará um processo *rastreador de recursos* que rastreia os
recursos de sistema nomeados não vinculados (como semáforos nomeados
ou objetos "SharedMemory") criados por processos do programa. Quando
todos os processos tiverem saído, o rastreador de recursos desvincula
qualquer objeto rastreado restante. Normalmente, não deve haver
nenhum, mas se um processo foi morto por um sinal, pode haver alguns
recursos "vazados". (Nem os semáforos vazados nem os segmentos de
memória compartilhada serão desvinculados automaticamente até a
próxima reinicialização do sistema. Isso é problemático para ambos os
objetos porque o sistema permite apenas um número limitado de
semáforos nomeados, e os segmentos de memória compartilhada ocupam
algum espaço na memória principal.)

Para selecionar um método de inicialização, você usa
"set_start_method()" na cláusula "if __name__ == '__main__'" do módulo
principal. Por exemplo:

   import multiprocessing as mp

   def foo(q):
       q.put('hello')

   if __name__ == '__main__':
       mp.set_start_method('spawn')
       q = mp.Queue()
       p = mp.Process(target=foo, args=(q,))
       p.start()
       print(q.get())
       p.join()

"set_start_method()" não deve ser usada mais de uma vez no programa.

Alternativamente, você pode usar "get_context()" para obter um objeto
de contexto. Objetos de contexto têm a mesma API que o módulo
multiprocessing e permitem que se usem vários métodos de inicialização
no mesmo programa.

   import multiprocessing as mp

   def foo(q):
       q.put('hello')

   if __name__ == '__main__':
       ctx = mp.get_context('spawn')
       q = ctx.Queue()
       p = ctx.Process(target=foo, args=(q,))
       p.start()
       print(q.get())
       p.join()

Note que objetos relacionados a um contexto podem não ser compatíveis
com processos para um contexto diferente. Em particular, travas
criadas usando o contexto *fork* não podem ser passados para processos
iniciados usando os métodos de inicialização *spawn* ou *forkserver*.

Libraries using "multiprocessing" or "ProcessPoolExecutor" should be
designed to allow their users to provide their own multiprocessing
context.  Using a specific context of your own within a library can
lead to incompatibilities with the rest of the library user's
application.  Always document if your library requires a specific
start method.

Aviso:

  Os métodos de inicialização "'spawn'" e "'forkserver'" geralmente
  não podem ser usadas com executáveis "congelados" (por exemplo,
  binários produzidos por pacotes como **PyInstaller** e
  **cx_Freeze**) em sistemas POSIX. O método de inicialização "'fork'"
  pode funcionar se o código não usar threads.


Trocando objetos entre processos
--------------------------------

"multiprocessing" supports two types of communication channel between
processes:

**Filas**

   A classe "Queue" é quase um clone de "queue.Queue". Por exemplo:

      from multiprocessing import Process, Queue

      def f(q):
          q.put([42, None, 'hello'])

      if __name__ == '__main__':
          q = Queue()
          p = Process(target=f, args=(q,))
          p.start()
          print(q.get())    # prints "[42, None, 'hello']"
          p.join()

   Queues are thread and process safe. Any object put into a
   "multiprocessing" queue will be serialized.

**Encadeamentos**

   A função "Pipe()" retorna um par de objetos de conexão conectados
   por um encadeamento que por padrão é duplex (bidirecional). Por
   exemplo:

      from multiprocessing import Process, Pipe

      def f(conn):
          conn.send([42, None, 'hello'])
          conn.close()

      if __name__ == '__main__':
          parent_conn, child_conn = Pipe()
          p = Process(target=f, args=(child_conn,))
          p.start()
          print(parent_conn.recv())   # exibe "[42, None, 'hello']"
          p.join()

   Os dois objetos de conexão retornados por "Pipe()" representam as
   duas extremidades do encadeamento. Cada objeto de conexão tem os
   métodos "send()" e "recv()" (entre outros). Observe que os dados em
   um encadeamento podem ser corrompidos se dois processos (ou
   threads) tentarem ler ou gravar na *mesma* extremidade do
   encadeamento ao mesmo tempo. Claro que não há risco de corrupção de
   processos usando extremidades diferentes do encadeamento ao mesmo
   tempo.

   O método "send()" serializa o objeto e "recv()" recria o objeto.


Sincronização entre processos
-----------------------------

"multiprocessing" contains equivalents of all the synchronization
primitives from "threading".  For instance one can use a lock to
ensure that only one process prints to standard output at a time:

   from multiprocessing import Process, Lock

   def f(l, i):
       l.acquire()
       try:
           print('hello world', i)
       finally:
           l.release()

   if __name__ == '__main__':
       lock = Lock()

       for num in range(10):
           Process(target=f, args=(lock, num)).start()

Sem utilizar a saída da trava dos diferentes processos, é possível que
tudo fique confuso.


Compartilhando estado entre processos
-------------------------------------

Conforme mencionado acima, ao fazer programação concorrente,
geralmente é melhor evitar o uso de estado compartilhado, tanto quanto
possível. Isso é particularmente verdadeiro ao utilizar múltiplos
processos.

However, if you really do need to use some shared data then
"multiprocessing" provides a couple of ways of doing so.

**Memória compartilhada**

   Os dados podem ser armazenados em um mapa de memória compartilhado
   utilizando "Value" ou "Array". Por exemplo, o código a seguir

      from multiprocessing import Process, Value, Array

      def f(n, a):
          n.value = 3.1415927
          for i in range(len(a)):
              a[i] = -a[i]

      if __name__ == '__main__':
          num = Value('d', 0.0)
          arr = Array('i', range(10))

          p = Process(target=f, args=(num, arr))
          p.start()
          p.join()

          print(num.value)
          print(arr[:])

   vai exibir

      3.1415927
      [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

   Os argumentos "'d'" e "'i'" usados ao criar "num" e "arr" são
   typecodes do tipo usado pelo módulo "array": "'d'" indica um ponto
   flutuante de precisão dupla e "'i'" indica um inteiro com sinal.
   Esses objetos compartilhados serão seguros para thread e processo.

   Para mais flexibilidade no uso de memória compartilhada, pode-se
   utilizar o módulo "multiprocessing.sharedctypes", que suporta a
   criação de objetos ctypes arbitrários alocados da memória
   compartilhada.

**Processo de servidor**

   Um objeto gerenciador retornado por "Manager()" controla um
   processo de servidor que contém objetos Python e permite que outros
   processos os manipulem usando proxies.

   A manager returned by "Manager()" will support types "list",
   "dict", "set", "Namespace", "Lock", "RLock", "Semaphore",
   "BoundedSemaphore", "Condition", "Event", "Barrier", "Queue",
   "Value" and "Array".  For example,

      from multiprocessing import Process, Manager

      def f(d, l, s):
          d[1] = '1'
          d['2'] = 2
          d[0.25] = None
          l.reverse()
          s.add('a')
          s.add('b')

      if __name__ == '__main__':
          with Manager() as manager:
              d = manager.dict()
              l = manager.list(range(10))
              s = manager.set()

              p = Process(target=f, args=(d, l, s))
              p.start()
              p.join()

              print(d)
              print(l)
              print(s)

   vai exibir

      {0.25: None, 1: '1', '2': 2}
      [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
      {'a', 'b'}

   Os gerenciadores de processos de servidor são mais flexíveis do que
   usar objetos de memória compartilhada porque podem ser feitos para
   oferecer suporte a tipos de objetos arbitrários. Além disso, um
   único gerenciador pode ser compartilhado por processos em
   diferentes computadores em uma rede. Eles são, no entanto, mais
   lentos do que usar memória compartilhada.


Usando um pool de workers
-------------------------

A classe "Pool" representa um pool de processos de worker. Ela tem
métodos que permitem que tarefas sejam descarregadas para os processos
de worker de algumas maneiras diferentes.

Por exemplo:

   from multiprocessing import Pool, TimeoutError
   import time
   import os

   def f(x):
       return x*x

   if __name__ == '__main__':
       # inicia 4 processos de trabalhador
       with Pool(processes=4) as pool:

           # exibe "[0, 1, 4,..., 81]"
           print(pool.map(f, range(10)))

           # exibe mesmo números em ordem arbitrária
           for i in pool.imap_unordered(f, range(10)):
               print(i)

           # calcula "f(20)" assincronamente
           res = pool.apply_async(f, (20,))      # executa em *apenas* um processo
           print(res.get(timeout=1))             # exibe "400"

           # calcula "os.getpid()" assincronamente
           res = pool.apply_async(os.getpid, ()) # executa em *apenas* um procsso
           print(res.get(timeout=1))             # exibe o PID daquele processo

           # iniciando vários cálculos de forma assíncrona *pod* usar mais procssos
           multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
           print([res.get(timeout=1) for res in multiple_results])

           # faz um único worker dormir por 10 segundos
           res = pool.apply_async(time.sleep, (10,))
           try:
               print(res.get(timeout=1))
           except TimeoutError:
               print("We lacked patience and got a multiprocessing.TimeoutError")

           print("For the moment, the pool remains available for more work")

       # saindo o bloco 'with' parou o pool
       print("Now the pool is closed and no longer available")

Observe que os métodos de um pool só devem ser usados pelo processo
que o criou.

Nota:

  A funcionalidade dentro deste pacote requer que o módulo "__main__"
  seja importável pelos filhos. Isso é abordado em Programming
  guidelines, mas vale a pena apontar aqui. Isso significa que alguns
  exemplos, como os exemplos "multiprocessing.pool.Pool" não
  funcionarão no interpretador interativo. Por exemplo:

     >>> from multiprocessing import Pool
     >>> p = Pool(5)
     >>> def f(x):
     ...     return x*x
     ...
     >>> with p:
     ...     p.map(f, [1,2,3])
     Process PoolWorker-1:
     Process PoolWorker-2:
     Process PoolWorker-3:
     Traceback (most recent call last):
     Traceback (most recent call last):
     Traceback (most recent call last):
     AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
     AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
     AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>

  (Se você tentar isso, na verdade, serão gerados três tracebacks
  completos intercalados de forma semi-aleatória, e então você pode
  ter que interromper o processo pai de alguma forma.)


Referência
==========

The "multiprocessing" package mostly replicates the API of the
"threading" module.


Global start method
-------------------

Python supports several ways to create and initialize a process. The
global start method sets the default mechanism for creating a process.

Several multiprocessing functions and methods that may also
instantiate certain objects will implicitly set the global start
method to the system's default, if it hasn’t been set already. The
global start method can only be set once. If you need to change the
start method from the system default, you must proactively set the
global start method before calling functions or methods, or creating
these objects.


"Process" e exceções
--------------------

class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

   Objetos processo representam atividades que são executadas em um
   processo separado. A classe "Process" possui equivalentes de todos
   os métodos de "threading.Thread".

   O construtor deve sempre ser chamado com argumentos nomeados.
   *group* deve sempre ser "None"; ele existe somente para
   compatibilidade com "threading.Thread". *target* é o objeto
   chamável a ser invocado pelo método "run()". O padrão é "None", o
   que significa que nada é chamado. *name* é o nome do processo (veja
   "name" para mais detalhes). *args* é a tupla de argumento para a
   invocação de destino. *kwargs* é um dicionário de argumentos
   nomeados para a invocação de destino. Se fornecido, o argumento
   somente-nomeados *daemon* define o sinalizador do processo "daemon"
   como "True" ou "False". Se "None" (o padrão), este sinalizador será
   herdado do processo de criação.

   Por padrão, nenhum argumento é passado para *target*. O argumento
   *args*, que tem como padrão "()", pode ser usado para especificar
   uma lista ou tupla de argumentos a serem passados para *target*.

   If a subclass overrides the constructor, it must make sure it
   invokes the base class constructor ("super().__init__()") before
   doing anything else to the process.

   Nota:

     In general, all arguments to "Process" must be picklable.  This
     is frequently observed when trying to create a "Process" or use a
     "concurrent.futures.ProcessPoolExecutor" from a REPL with a
     locally defined *target* function.Passing a callable object
     defined in the current REPL session causes the child process to
     die via an uncaught "AttributeError" exception when starting as
     *target* must have been defined within an importable module in
     order to be loaded during unpickling.Example of this uncatchable
     error from the child:

        >>> import multiprocessing as mp
        >>> def knigit():
        ...     print("Ni!")
        ...
        >>> process = mp.Process(target=knigit)
        >>> process.start()
        >>> Traceback (most recent call last):
          File ".../multiprocessing/spawn.py", line ..., in spawn_main
          File ".../multiprocessing/spawn.py", line ..., in _main
        AttributeError: module '__main__' has no attribute 'knigit'
        >>> process
        <SpawnProcess name='SpawnProcess-1' pid=379473 parent=378707 stopped exitcode=1>

     See The spawn and forkserver start methods.  While this
     restriction is not true if using the ""fork"" start method, as of
     Python "3.14" that is no longer the default on any platform.  See
     Contextos e métodos de inicialização. See also gh-132898.

   Alterado na versão 3.3: Adicionado o parâmetro *daemon*.

   run()

      Método que representa a atividade do processo.

      Você pode substituir esse método em uma subclasse. O método
      padrão "run()" invoca o objeto chamável passado ao construtor do
      objeto como o argumento alvo, se houver, com argumentos nomeados
      e sequenciais retirados dos argumentos *args* e *kwargs*,
      respectivamente.

      Usar uma lista ou tupla como argumento *args* passado para
      "Process" obtém o mesmo efeito.

      Exemplo:

         >>> from multiprocessing import Process
         >>> p = Process(target=print, args=[1])
         >>> p.run()
         1
         >>> p = Process(target=print, args=(1,))
         >>> p.run()
         1

   start()

      Inicia a atividade do processo.

      Isso deve ser chamado no máximo uma vez por objeto processo. Ele
      organiza para que o método "run()" do objeto seja invocado em um
      processo separado.

   join([timeout])

      Se o argumento opcional *timeout* for "None" (o padrão), o
      método bloqueia até que o processo cujo método "join()" é
      chamado termine. Se *timeout* for um número positivo, ele
      bloqueia no máximo *timeout* segundos. Observe que o método
      retorna "None" se seu processo terminar ou se o método tiver
      tempo limite. Verifique o "exitcode" do processo para determinar
      se ele terminou.

      Um processo pode ser usar "join" muitas vezes.

      Um processo não pode se unir porque isso causaria um impasse. É
      um erro tentar se unir a um processo antes que ele tenha sido
      iniciado.

   name

      O nome do processo. O nome é uma string usada apenas para fins
      de identificação. Não tem semântica. Vários processos podem
      receber o mesmo nome.

      O nome inicial é definido pelo construtor. Se nenhum nome
      explícito for fornecido ao construtor, um nome do formato
      'Processo-N_1:N_2:...:N_k' é construído, onde cada N_k é o
      N-ésimo filho de seu pai.

   is_alive()

      Retorna se o processo está ativo.

      Em termos gerais, um objeto processo está ativo desde o momento
      em que o método "start()" retorna até o término do processo
      filho.

   daemon

      O sinalizador daemon do processo, um valor Booleano. Isso deve
      ser definido antes de "start()" ser chamado.

      O valor inicial é herdado do processo de criação.

      Quando um processo sai, ele tenta encerrar todos os seus
      processos filhos daemônicos.

      Note que um processo daemônico não tem permissão para criar
      processos filhos. Caso contrário, um processo daemônico deixaria
      seus filhos órfãos se ele fosse encerrado quando seu processo
      pai saísse. Além disso, esses **não** são daemons ou serviços
      Unix, eles são processos normais que serão encerrados (e em vez
      de usar "join") se processos não daemônicos tiverem saído.

   Além da API "threading.Thread", os objetos "Process" também
   oferecem suporte aos seguintes atributos e métodos:

   pid

      Retorna o ID do processo. Antes do processo ser gerado, este
      será "None".

   exitcode

      O código de saída da criança. Este será "None" se o processo
      ainda não tiver terminado.

      Se o método "run()" da criança retornar normalmente, o código de
      saída será 0. Se ele terminar via "sys.exit()" com um argumento
      inteiro *N*, o código de saída será *N*.

      Se a criança for encerrada devido a uma exceção não capturada em
      "run()", o código de saída será 1. Se ela for encerrada pelo
      sinal *N*, o código de saída será o valor negativo *-N*.

   authkey

      A chave de autenticação do processo (uma string de bytes).

      When "multiprocessing" is initialized the main process is
      assigned a random string using "os.urandom()".

      Quando um objeto "Process" é criado, ele herda a chave de
      autenticação do seu processo pai, embora isso possa ser alterado
      definindo "authkey" para outra sequência de bytes.

      Veja Authentication keys.

   sentinel

      Um identificador numérico de um objeto do sistema que ficará
      "pronto" quando o processo terminar.

      Você pode usar esse valor se quiser esperar por vários eventos
      ao mesmo tempo usando "multiprocessing.connection.wait()". Caso
      contrário, chamar "join()" é mais simples.

      No Windows, este é um identificador de sistema operacional
      utilizável com a família de chamadas de API
      "WaitForSingleObject" e "WaitForMultipleObjects". No POSIX, este
      é um descritor de arquivo utilizável com primitivos do módulo
      "select".

      Adicionado na versão 3.3.

   interrupt()

      Encerra o processo. Funciona em POSIX usando o sinal "SIGINT". O
      comportamento no Windows é indefinido.

      Por padrão, isso encerra o processo filho levantando
      "KeyboardInterrupt". Esse comportamento pode ser alterado com a
      configuração do respectivo sinal manipulador no processo filho
      "signal.signal()" para "SIGINT".

      Observação: se o processo filho capturar e descartar
      "KeyboardInterrupt", o processo não será encerrado.

      Observação: o comportamento padrão também definirá "exitcode"
      para "1" como se um exceção não-capturada fosse levantada no
      filho processo. Para ter um "exitcode" diferente, você pode
      simplesmente capturar "KeyboardInterrupt" e chamar
      "exit(your_code)".

      Adicionado na versão 3.14.

   terminate()

      Encerra o processo. No POSIX isso é feito usando o sinal
      "SIGTERM"; no Windows é usado "TerminateProcess()". Note que os
      manipuladores de saída e cláusulas finally, etc., não serão
      executados.

      Observe que os processos descendentes do processo *não* serão
      encerrados — eles simplesmente ficarão órfãos.

      Aviso:

        Se esse método for usado quando o processo associado estiver
        usando um encadeamento ou fila, então o encadeamento ou fila é
        passível de ser corrompido e pode se tornar inutilizável por
        outro processo. Similarmente, se o processo adquiriu um trava
        ou semáforo etc., então encerrá-lo é passível de causar
        impasse em outros processos.

   kill()

      O mesmo que "terminate()", mas usando o sinal "SIGKILL" no
      POSIX.

      Adicionado na versão 3.7.

   close()

      Fecha o objeto "Process", liberando todos os recursos associados
      a ele. "ValueError" é levantado se o processo subjacente ainda
      estiver em execução. Uma vez que "close()" retorne com sucesso,
      a maioria dos outros métodos e atributos do objeto "Process"
      levantará "ValueError".

      Adicionado na versão 3.7.

   Observe que os métodos "start()", "join()", "is_alive()",
   "terminate()" e "exitcode" devem ser chamados somente pelo processo
   que criou o objeto processo.

   Exemplo de uso de alguns dos métodos de "Process":

      >>> import multiprocessing, time, signal
      >>> mp_context = multiprocessing.get_context('spawn')
      >>> p = mp_context.Process(target=time.sleep, args=(1000,))
      >>> print(p, p.is_alive())
      <...Process ... initial> False
      >>> p.start()
      >>> print(p, p.is_alive())
      <...Process ... started> True
      >>> p.terminate()
      >>> time.sleep(0.1)
      >>> print(p, p.is_alive())
      <...Process ... stopped exitcode=-SIGTERM> False
      >>> p.exitcode == -signal.SIGTERM
      True

exception multiprocessing.ProcessError

   The base class of all "multiprocessing" exceptions.

exception multiprocessing.BufferTooShort

   Exceção levantada por "Connection.recv_bytes_into()" quando o
   objeto buffer fornecido é muito pequeno para a mensagem lida.

   Se "e" for uma instância de "BufferTooShort", então "e.args[0]"
   retornará a mensagem como uma string de bytes.

exception multiprocessing.AuthenticationError

   Levantada quando há um erro de autenticação.

exception multiprocessing.TimeoutError

   Levantada por métodos com um tempo limite quando o tempo limite
   expira.


Encadeamentos e filas
---------------------

Ao usar vários processos, geralmente é usada a passagem de mensagens
para comunicação entre processos e evita-se ter que usar quaisquer
primitivas de sincronização, como travas.

Para passar mensagens, pode-se usar "Pipe()" (para uma conexão entre
dois processos) ou uma fila (que permite múltiplos produtores e
consumidores).

Os tipos "Queue", "SimpleQueue" e "JoinableQueue" são filas FIFO
(first-in, first-out) multiprodutoras e multiconsumidoras modeladas na
classe "queue.Queue" da biblioteca padrão. Elas diferem porque "Queue"
não tem os métodos "task_done()" e "join()" introduzidos na classe
"queue.Queue" do Python 2.5.

Se você usar "JoinableQueue", então você **deve** chamar
"JoinableQueue.task_done()" para cada tarefa removida da fila, caso
contrário, o semáforo usado para contar o número de tarefas não
concluídas pode eventualmente transbordar, levantando uma exceção.

One difference from other Python queue implementations, is that
"multiprocessing" queues serializes all objects that are put into them
using "pickle". The object returned by the get method is a re-created
object that does not share memory with the original object.

Observe que também é possível criar uma fila compartilhada usando um
objeto gerenciador — veja Gerenciadores.

Nota:

  "multiprocessing" uses the usual "queue.Empty" and "queue.Full"
  exceptions to signal a timeout.  They are not available in the
  "multiprocessing" namespace so you need to import them from "queue".

Nota:

  Quando um objeto é colocado em uma fila, o objeto é serializado com
  pickle e uma thread em segundo plano depois descarrega os dados
  serializados com pickle para um encadeamento subjacente. Isso tem
  algumas consequências que são um pouco surpreendentes, mas não devem
  causar nenhuma dificuldade prática -- se elas realmente o incomodam,
  então você pode usar uma fila criada com um gerenciador.

  1. Depois de colocar um objeto em uma fila vazia, pode haver um
     atraso infinitesimal antes que o método "empty()" da fila retorne
     "False" e "get_nowait()" possa retornar sem levantar
     "queue.Empty".

  2. Se vários processos estiverem enfileirando objetos, é possível
     que os objetos sejam recebidos na outra extremidade fora de
     ordem. No entanto, objetos enfileirados pelo mesmo processo
     sempre estarão na ordem esperada em relação uns aos outros.

Aviso:

  Se um processo for morto usando "Process.terminate()" ou "os.kill()"
  enquanto estiver tentando usar uma "Queue", os dados na fila
  provavelmente serão corrompidos. Isso pode fazer com que qualquer
  outro processo obtenha uma exceção quando tentar usar a fila mais
  tarde.

Aviso:

  Conforme mencionado acima, se um processo filho tiver colocado itens
  em uma fila (e não tiver usado "JoinableQueue.cancel_join_thread"),
  esse processo não será encerrado até que todos os itens armazenados
  em buffer tenham sido liberados para o encadeamento.Isso significa
  que se você tentar juntar esse processo, poderá obter um impasse, a
  menos que tenha certeza de que todos os itens que foram colocados na
  fila foram consumidos. Da mesma forma, se o processo filho não for
  daemônico, o processo pai pode travar na saída quando tentar juntar
  todos os seus filhos não daemônicos.Note que uma fila criada usando
  um gerenciador não tem esse problema. Veja Programming guidelines.

Para um exemplo do uso de filas para comunicação entre processos, veja
Exemplos.

multiprocessing.Pipe(duplex=True)

   Retorna um par "(conn1, conn2)" de objetos "Connection"
   representando as extremidades de um encadeamento.

   Se *duplex* for "True" (o padrão), então o encadeamento é
   bidirecional. Se *duplex* for "False", então o encadeamento é
   unidirecional: "conn1" pode ser usado somente para receber
   mensagens e "conn2" pode ser usado somente para enviar mensagens.

   O método "send()" serializa o objeto usando "pickle" e "recv()"
   recria o objeto.

class multiprocessing.Queue([maxsize])

   Retorna uma fila compartilhada de processo implementada usando um
   encadeamento e algumas travas/semáforos. Quando um processo coloca
   um item na fila pela primeira vez, uma thread alimentadora é
   iniciada, a qual transfere objetos de um buffer para o
   encadeamento.

   Instantiating this class may set the global start method. See
   Global start method for more details.

   As exceções usuais "queue.Empty" e "queue.Full" do módulo "queue"
   da biblioteca padrão são levantadas para sinalizar tempos limite.

   "Queue" implements all the methods of "queue.Queue" except for
   "task_done()", "join()", and "shutdown()".

   qsize()

      Retorna o tamanho aproximado da fila. Devido à semântica de
      multithreading/multiprocessamento, esse número não é confiável.

      Observe que isso pode levantar "NotImplementedError" em
      plataformas como macOS, onde "sem_getvalue()" não está
      implementado.

   empty()

      Retorna "True" se a fila estiver vazia, "False" caso contrário.
      Devido à semântica de multithreading/multiprocessamento, isso
      não é confiável.

      Pode levantar uma exceção "OSError" em filas fechadas. (não
      garantido)

   full()

      Retorna "True" se a fila estiver cheia, "False" caso contrário.
      Devido à semântica de multithreading/multiprocessamento, isso
      não é confiável.

   put(obj[, block[, timeout]])

      Coloca *obj* na fila. Se o argumento opcional *block* for "True"
      (o padrão) e *timeout* for "None" (o padrão), bloqueia se
      necessário até que um slot livre esteja disponível. Se *timeout*
      for um número positivo, ele bloqueia no máximo *timeout*
      segundos e levanta a exceção "queue.Full" se nenhum slot livre
      estiver disponível dentro desse tempo. Caso contrário (*block* é
      "False"), coloca um item na fila se um slot livre estiver
      imediatamente disponível, senão levanta a exceção "queue.Full"
      (*timeout* é ignorado nesse caso).

      Alterado na versão 3.8: Se a fila for fechada, "ValueError" será
      levantada em vez de "AssertionError".

   put_nowait(obj)

      Equivalente  a "put(obj, False)".

   get([block[, timeout]])

      Remove e retorna um item da fila. Se os argumentos opcionais
      *block* forem "True" (o padrão) e *timeout* forem "None" (o
      padrão), bloqueia se necessário até que um item esteja
      disponível. Se *timeout* for um número positivo, ele bloqueia no
      máximo *timeout* segundos e levantada a exceção "queue.Empty" se
      nenhum item estiver disponível dentro desse tempo. Caso
      contrário (block for "False"), retorna um item se um estiver
      imediatamente disponível, senão levantada a exceção
      "queue.Empty" (*timeout* é ignorado nesse caso).

      Alterado na versão 3.8: Se a fila for fechada, "ValueError" será
      levantada em vez de "OSError".

   get_nowait()

      Equivalente a "get(False)".

   "multiprocessing.Queue" tem alguns métodos adicionais não
   encontrados em "queue.Queue". Esses métodos geralmente são
   desnecessários para a maioria dos códigos:

   close()

      Fecha a fila: libera recursos internos.

      A queue must not be used anymore after it is closed. For
      example, "get()", "put()" and "empty()" methods must no longer
      be called.

      The background thread will quit once it has flushed all buffered
      data to the pipe.  This is called automatically when the queue
      is garbage collected.

   join_thread()

      Junta a thread de segundo plano. Isso só pode ser usado depois
      que "close()" for chamado. Isso bloqueia até que a thread de
      segundo plano saia, garantindo que todos os dados no buffer
      tenham sido liberados para o encadeamento.

      Por padrão, se um processo não for o criador da fila, ao sair,
      ele tentará se juntar ao thread de segundo plano da fila. O
      processo pode chamar "cancel_join_thread()" para fazer
      "join_thread()" não fazer nada.

   cancel_join_thread()

      Impede que "join_thread()" bloqueie. Em particular, isso impede
      que o thread de segundo plano seja unido automaticamente quando
      o processo sai -- veja "join_thread()".

      Um nome melhor para esse método pode ser
      "allow_exit_without_flush()". É provável que ele faça com que
      dados enfileirados sejam perdidos, e você quase certamente não
      precisará usá-lo. Ele está realmente lá somente se você precisar
      que o processo atual saia imediatamente sem esperar para liberar
      dados enfileirados para o encadeamento subjacente, e você não se
      importa com dados perdidos.

   Nota:

     A funcionalidade desta classe requer uma implementação de
     semáforo compartilhado funcional no sistema operacional host. Sem
     uma, a funcionalidade nesta classe será desabilitada, e as
     tentativas de instanciar uma "Queue" resultarão em um
     "ImportError". Veja bpo-3770 para informações adicionais. O mesmo
     vale para qualquer um dos tipos de fila especializados listados
     abaixo.

class multiprocessing.SimpleQueue

   É um tipo "Queue" simplificado, muito próximo de um "Pipe" travado.

   Instantiating this class may set the global start method. See
   Global start method for more details.

   close()

      Fecha a fila: libera recursos internos.

      Uma fila não deve mais ser usada depois de fechada. Por exemplo,
      os métodos "get()", "put()" e "empty()" não devem mais ser
      chamados.

      Adicionado na versão 3.9.

   empty()

      Retorna "True" se a fila estiver vazia, "False" caso contrário.

      Sempre levanta "OSError" se a SimpleQueue estiver fechada.

   get()

      Remove e retorna um item da fila.

   put(item)

      Coloca *item* na fila.

class multiprocessing.JoinableQueue([maxsize])

   "JoinableQueue", uma subclasse de "Queue", é uma fila que também
   possui os métodos "task_done()" e "join()".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   task_done()

      Indica que a tarefa anteriormente enfileirado está concluída.
      Para cada "get()" usado para buscar uma tarefa, uma chamada
      subsequente para "task_done()" avisa à fila, que o processamento
      na tarefa está concluído.

      Se um "join()" estiver causando bloqueio no momento, ele irá
      continuar quando todos os itens tiverem sido processados
      (significando que uma chamada "task_done()" foi recebida para
      cada item que foi chamado o método "put()" para colocar na
      fila).

      Levanta "ValueError" se for chamado mais vezes do que o número
      de itens colocados na fila.

   join()

      Bloqueia até que todos os itens na fila tenham sido obtidos e
      processados.

      A contagem de tarefas inacabadas aumenta sempre que um item é
      adicionado à fila. A contagem diminui sempre que uma consumidora
      chama "task_done()" para indicar que o item foi recuperado e
      todo o trabalho nele foi concluído. Quando a contagem de tarefas
      inacabadas chega a zero, "join()" desbloqueia.


Diversos
--------

multiprocessing.active_children()

   Retorna a lista de todos os filhos ativos do processo atual.

   Chamar isso tem o efeito colateral de "juntar" quaisquer processos
   que já tenham sido concluídos.

multiprocessing.cpu_count()

   Retorna o número de CPUs no sistema.

   Este número não equivale ao número de CPUs que o processo atual
   pode usar. O número de CPUs utilizáveis pode ser obtido com
   "os.process_cpu_count()" (ou "len(os.sched_getaffinity(0))").

   Quando o número de CPUs não pode ser determinado, uma
   "NotImplementedError" é levantada.

   Ver também: "os.cpu_count()" "os.process_cpu_count()"

   Alterado na versão 3.13: O valor de retorno também pode ser
   substituído usando o sinalizador "-X cpu_count" ou
   "PYTHON_CPU_COUNT", pois este é apenas um invólucro em torno das
   APIs de contagem de CPU do "os".

multiprocessing.current_process()

   Retorna o objeto "Process" correspondente ao processo atual.

   Um análogo de "threading.current_thread()".

multiprocessing.parent_process()

   Retorna o objeto "Process" correspondente ao processo pai do
   "current_process()". Para o processo principal, "parent_process"
   será "None".

   Adicionado na versão 3.8.

multiprocessing.freeze_support()

   Add support for when a program which uses "multiprocessing" has
   been frozen to produce an executable.  (Has been tested with
   **py2exe**, **PyInstaller** and **cx_Freeze**.)

   É preciso chamar esta função logo após a linha "if __name__ ==
   '__main__'" do módulo principal. Por exemplo:

      from multiprocessing import Process, freeze_support

      def f():
          print('hello world!')

      if __name__ == '__main__':
          freeze_support()
          Process(target=f).start()

   Se a linha "freeze_support()" for omitida, tentar executar o
   executável congelado levantará "RuntimeError".

   Calling "freeze_support()" has no effect when the start method is
   not *spawn*. In addition, if the module is being run normally by
   the Python interpreter (the program has not been frozen), then
   "freeze_support()" has no effect.

multiprocessing.get_all_start_methods()

   Retorna uma lista dos métodos de inicialização suportados, o
   primeiro dos quais é o padrão. Os métodos possíveis são "'fork'",
   "'spawn'" e "'forkserver'". Nem todas as plataformas suportam todos
   os métodos. Consulte Contextos e métodos de inicialização.

   Adicionado na versão 3.4.

multiprocessing.get_context(method=None)

   Return a context object which has the same attributes as the
   "multiprocessing" module.

   If *method* is "None" then the default context is returned. Note
   that if the global start method has not been set, this will set it
   to the system default See Global start method for more details.
   Otherwise *method* should be "'fork'", "'spawn'", "'forkserver'".
   "ValueError" is raised if the specified start method is not
   available.  See Contextos e métodos de inicialização.

   Adicionado na versão 3.4.

multiprocessing.get_start_method(allow_none=False)

   Retorna o nome do método de inicialização usado para iniciar
   processos.

   If the global start method is not set and *allow_none* is "False",
   the global start method is set to the default, and its name is
   returned. See Global start method for more details.

   O valor de retorno pode ser "'fork'", "'spawn'", "'forkserver'" ou
   "None". Veja Contextos e métodos de inicialização.

   Adicionado na versão 3.4.

   Alterado na versão 3.8: No macOS, o método de inicialização *spawn*
   agora é o padrão. O método de inicialização *fork* deve ser
   considerado inseguro, pois pode levar a travamentos do subprocesso.
   Consulte bpo-33725.

multiprocessing.set_executable(executable)

   Set the path of the Python interpreter to use when starting a child
   process. (By default "sys.executable" is used).  Embedders will
   probably need to do something like

      set_executable(os.path.join(sys.exec_prefix, 'pythonw.exe'))

   antes que eles possam criar processos filho.

   Alterado na versão 3.4: Agora com suporte no POSIX quando o método
   de inicialização "'spawn'" é usado.

   Alterado na versão 3.11: Aceita um *objeto caminho ou similar*.

multiprocessing.set_forkserver_preload(module_names, *, on_error='ignore')

   Set a list of module names for the forkserver main process to
   attempt to import so that their already imported state is inherited
   by forked processes. This can be used as a performance enhancement
   to avoid repeated work in every process.

   Para que isso aconteça, trabalho deve ser chamado antes que o
   forkserver processar tenha sido iniciado (antes de criar um "Pool"
   ou iniciar um "Process").

   The *on_error* parameter controls how "ImportError" exceptions
   during module preloading are handled: ""ignore"" (default) silently
   ignores failures, ""warn"" causes the forkserver subprocess to emit
   an "ImportWarning" to stderr, and ""fail"" causes the forkserver
   subprocess to exit with the exception traceback on stderr, making
   subsequent process creation fail with "EOFError" or
   "ConnectionError".

   Só é significativo ao usar o método de inicialização
   "'forkserver'". Consulte Contextos e métodos de inicialização.

   Adicionado na versão 3.4.

   Alterado na versão 3.15: Added the *on_error* parameter.

multiprocessing.set_start_method(method, force=False)

   Define o método que deve ser usado para iniciar processos filhos. O
   argumento *method* pode ser "'fork'", "'spawn'" ou "'forkserver'".
   Levanta "RuntimeError" se o método de inicialização já tiver sido
   definido e *force* não for "True". Se *method* for "None" e *force*
   for "True", o método de inicialização será definido como "None". Se
   *method* for "None" e *force* for "False", o contexto será definido
   como o contexto padrão.

   Observe que isso deve ser chamado no máximo uma vez e deve ser
   protegido dentro da cláusula "if __name__ == '__main__'" do módulo
   principal.

   Veja Contextos e métodos de inicialização.

   Adicionado na versão 3.4.

Nota:

  "multiprocessing" contains no analogues of
  "threading.active_count()", "threading.enumerate()",
  "threading.settrace()", "threading.setprofile()", "threading.Timer",
  or "threading.local".


Objetos de conexão
------------------

Objetos de conexão permitem o envio e recebimento de strings e objetos
que podem ser serializados com pickle. Eles podem ser pensados como
sockets conectados orientados a mensagens.

Objetos de conexão geralmente são criados usando "Pipe" -- veja também
Listeners and Clients.

class multiprocessing.connection.Connection

   send(obj)

      Envia um objeto para a outra extremidade da conexão que deve ser
      lido usando "recv()".

      O objeto deve poder ser serializado com pickle. Serializações
      muito grandes com pickles (aproximadamente 32 MiB+, embora isso
      dependa do sistema operacional) podem levantar uma exceção
      "ValueError".

   recv()

      Retorna um objeto enviado a partir da outra extremidade da
      conexão usando "send()". Bloqueia até que haja algo para
      receber. Levanta "EOFError" se não houver mais nada para receber
      e a outra extremidade tenha sido fechada.

   fileno()

      Retorna o descritor de arquivo ou identificador usado pela
      conexão.

   close()

      Fecha a conexão.

      Isso é chamado automaticamente quando a conexão é coletada como
      lixo.

   poll([timeout])

      Retorna se há algum dado disponível para leitura.

      Se *timeout* não for especificado, ele retornará imediatamente.
      Se *timeout* for um número, isso especificará o tempo máximo em
      segundos para bloquear. Se *timeout* for "None", um tempo limite
      infinito será usado.

      Observe que vários objetos de conexão podem ser pesquisados ao
      mesmo tempo usando "multiprocessing.connection.wait()".

   send_bytes(buf[, offset[, size]])

      Enviar dados de bytes de um *objeto bytes ou similar* como uma
      mensagem completa.

      If *offset* is given then data is read from that position in
      *buf*.  If *size* is given then that many bytes will be read
      from *buf*.  Very large buffers (approximately 32 MiB+, though
      it depends on the OS) may raise a "ValueError" exception

   recv_bytes([maxlength])

      Retorna uma mensagem completa de dados como bytes enviados a
      partir da outra extremidade da conexão como uma string. Bloqueia
      até que haja algo para receber. Levanta "EOFError" se não houver
      mais nada para receber e a outra extremidade tenha sido fechada.

      Se *maxlength* for especificado e a mensagem for maior que
      *maxlength*, "OSError" será levantada e a conexão não será mais
      legível.

      Alterado na versão 3.3: Esta função costumava levantada
      "IOError", que agora é um apelido de "OSError".

   recv_bytes_into(buf[, offset])

      Read into *buf* a complete message of byte data sent from the
      other end of the connection and return the number of bytes in
      the message.  Blocks until there is something to receive.
      Raises "EOFError" if there is nothing left to receive and the
      other end was closed.

      *buf* must be a writable *bytes-like object*.  If *offset* is
      given then the message will be written into the buffer from that
      position.  Offset must be a non-negative integer less than the
      length of *buf* (in bytes).

      Se o buffer for muito curto, uma exceção "BufferTooShort" será
      levantada e a mensagem completa estará disponível como
      "e.args[0]", onde "e" é a instância da exceção.

   Alterado na versão 3.3: Os próprios objetos de conexão agora podem
   ser transferidos entre processos usando "Connection.send()" e
   "Connection.recv()".Objetos de conexão agora também oferecem
   suporte ao protocolo de gerenciamento de contexto — veja Tipos de
   Gerenciador de Contexto. "__enter__()" retorna o objeto de conexão,
   e "__exit__()" chama "close()".

Por exemplo:

   >>> from multiprocessing import Pipe
   >>> a, b = Pipe()
   >>> a.send([1, 'hello', None])
   >>> b.recv()
   [1, 'hello', None]
   >>> b.send_bytes(b'thank you')
   >>> a.recv_bytes()
   b'thank you'
   >>> import array
   >>> arr1 = array.array('i', range(5))
   >>> arr2 = array.array('i', [0] * 10)
   >>> a.send_bytes(arr1)
   >>> count = b.recv_bytes_into(arr2)
   >>> assert count == len(arr1) * arr1.itemsize
   >>> arr2
   array('i', [0, 1, 2, 3, 4, 0, 0, 0, 0, 0])

Aviso:

  O método "Connection.recv()" deserializa com picke automaticamente
  os dados recebidos, o que pode ser um risco à segurança, a menos que
  você possa confiar no processo que enviou a mensagem.Portanto, a
  menos que o objeto de conexão tenha sido produzido usando "Pipe()",
  você deve usar apenas os métodos "recv()" e "send()" após executar
  algum tipo de autenticação. Veja Authentication keys.

Aviso:

  Se um processo for encerrado enquanto estiver tentando ler ou
  escrever em um encadeamento, os dados no encadeamento provavelmente
  serão corrompidos, porque pode se tornar impossível ter certeza de
  onde estão os limites do encadeamento da mensagem.


Primitivas de sincronização
---------------------------

Geralmente, primitivas de sincronização não são tão necessárias em um
programa multiprocesso quanto em um programa multithread. Veja a
documentação do módulo "threading".

Observe que também é possível criar primitivas de sincronização usando
um objeto gerenciador — veja Gerenciadores.

class multiprocessing.Barrier(parties[, action[, timeout]])

   Um objeto de barreira: um clone de "threading.Barrier".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Adicionado na versão 3.3.

class multiprocessing.BoundedSemaphore([value])

   Um objeto semáforo delimitado: um análogo próximo de
   "threading.BoundedSemaphore".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Existe uma única diferença em relação ao seu análogo próximo: o
   primeiro argumento do método "acquire" é chamado *block*, como é
   consistente com "Lock.acquire()".

   locked()

      Return a boolean indicating whether this object is locked right
      now.

      Adicionado na versão 3.14.

   Nota:

     No macOS, isso é indistinguível de "Semaphore" porque
     "sem_getvalue()" não está implementado nessa plataforma.

class multiprocessing.Condition([lock])

   Uma variável de condição: um apelido para "threading.Condition".

   If *lock* is specified then it should be a "Lock" or "RLock" object
   from "multiprocessing".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Alterado na versão 3.3: O método "wait_for()" foi adicionado.

class multiprocessing.Event

   Um clone de "threading.Event".

   Instantiating this class may set the global start method. See
   Global start method for more details.

class multiprocessing.Lock

   Um objeto de trava não recursivo: um análogo próximo de
   "threading.Lock". Uma vez que um processo ou thread tenha adquirido
   um trava, tentativas subsequentes de adquiri-la de qualquer
   processo ou thread bloquearão até que ele seja liberada; qualquer
   processo ou thread pode liberá-la. Os conceitos e comportamentos de
   "threading.Lock" conforme se aplica a threads são replicados aqui
   em "multiprocessing.Lock" conforme se aplica a processos ou
   threads, exceto conforme observado.

   Observe que "Lock" é na verdade uma função de fábrica que retorna
   uma instância de "multiprocessing.synchronize.Lock" inicializada
   com um contexto padrão.

   Instantiating this class may set the global start method. See
   Global start method for more details.

   "Lock" oferece suporte ao protocolo *gerenciador de contexto* e,
   portanto, pode ser usado em instruções "with".

   acquire(block=True, timeout=None)

      Adquire uma trava, bloqueante ou não.

      Com o argumento *block* definido como "True" (o padrão), a
      chamada do método bloqueará até que a trava esteja em um estado
      destravado, então o definirá como travada e retornará "True".
      Observe que o nome deste primeiro argumento difere daquele em
      "threading.Lock.acquire()".

      Com o argumento *block* definido como "False", a chamada do
      método não bloqueia. Se a trava estiver atualmente em um estado
      travado, retorna "False"; caso contrário, defina a trava para um
      estado travado e retorna "True".

      Quando invocado com um valor positivo de ponto flutuante para
      *timeout*, bloqueie por no máximo o número de segundos
      especificado por *timeout* enquanto a trava não puder ser
      adquirida. Invocações com um valor negativo para *timeout* são
      equivalentes a um *timeout* de zero. Invocações com um valor
      *timeout* de "None" (o padrão) definem o período de tempo limite
      como infinito. Observe que o tratamento de valores negativos ou
      "None" para *timeout* difere do comportamento implementado em
      "threading.Lock.acquire()". O argumento *timeout* não tem
      implicações práticas se o argumento *block* for definido como
      "False" e, portanto, for ignorado. Retorna "True" se a trava
      tiver sido adquirida ou "False" se o período de tempo limite
      tiver decorrido.

   release()

      Libera uma trava. Isso pode ser chamado de qualquer processo ou
      thread, não apenas do processo ou thread que originalmente
      adquiriu a trava.

      O comportamento é o mesmo de "threading.Lock.release()", exceto
      que quando invocado em uma trava desatravada, uma "ValueError" é
      levantada.

   locked()

      Return a boolean indicating whether this object is locked right
      now.

      Adicionado na versão 3.14.

class multiprocessing.RLock

   Um objeto de trava recursiva: um análogo próximo de
   "threading.RLock". Uma trava recursiva deve ser liberada pelo
   processo ou thread que o adquiriu. Uma vez que um processo ou
   thread tenha adquirido uma trava recursiva, o mesmo processo ou
   thread pode adquiri-la novamente sem trava; esse processo ou thread
   deve liberá-la uma vez para cada vez que ela foi adquirida.

   Observe que "RLock" é na verdade uma função de fábrica que retorna
   uma instância de "multiprocessing.synchronize.RLock" inicializada
   com um contexto padrão.

   Instantiating this class may set the global start method. See
   Global start method for more details.

   "RLock" oferece suporte ao protocolo *gerenciador de contexto* e,
   portanto, pode ser usado em instruções "with".

   acquire(block=True, timeout=None)

      Adquire uma trava, bloqueante ou não.

      Quando invocado com o argumento *block* definido como "True",
      bloqueia até que a trava esteja em um estado destravado (não
      pertencente a nenhum processo ou thread), a menos que a trava já
      seja de propriedade do processo ou thread atual. O processo ou
      thread atual então assume a propriedade da trava (se ainda não
      tiver propriedade) e o nível de recursão dentro de incrementos
      por um da trava, resultando em um valor de retorno de "True".
      Observe que há várias diferenças no comportamento deste primeiro
      argumento em comparação com a implementação de
      "threading.RLock.acquire()", começando pelo nome do argumento em
      si.

      Quando invocado com o argumento *block* definido como "False",
      não bloqueie. Se a trava já tiver sido adquirida (e, portanto,
      for de propriedade) por outro processo ou thread, o processo ou
      thread atual não assume a propriedade e o nível de recursão
      dentro da trava não é alterada, resultando em um valor de
      retorno de "False". Se a trava estiver em um estado destravado,
      o processo ou thread atual assume a propriedade e o nível de
      recursão é incrementado, resultando em um valor de retorno de
      "True".

      O uso e os comportamentos do argumento *timeout* são os mesmos
      que em "Lock.acquire()". Observe que alguns desses
      comportamentos de *timeout* diferem dos comportamentos
      implementados em "threading.RLock.acquire()".

   release()

      Libera uma trava, decrementando o nível de recursão. Se após o
      decremento o nível de recursão for zero, redefine a trava para
      destravada (não pertencente a nenhum processo ou thread) e se
      quaisquer outros processos ou threads estiverem bloqueados
      esperando a trava ser destravada, permita que exatamente um
      deles prossiga. Se após o decremento o nível de recursão ainda
      for diferente de zero, o trava permanece travada e pertencente
      ao processo ou thread de chamada.

      Somente chame esse método quando o processo ou thread de chamada
      for proprietária da trava. Uma "AssertionError" é levantada se
      esse método for chamado por um processo ou thread diferente do
      proprietário ou se a trava estiver em um estado destravado (sem
      proprietário). Observe que o tipo de exceção levantada nessa
      situação difere do comportamento implementado em
      "threading.RLock.release()".

   locked()

      Return a boolean indicating whether this object is locked right
      now.

      Adicionado na versão 3.14.

class multiprocessing.Semaphore([value])

   Um objeto semáforo: um análogo próximo de "threading.Semaphore".

   Instantiating this class may set the global start method. See
   Global start method for more details.

   Existe uma única diferença em relação ao seu análogo próximo: o
   primeiro argumento do método "acquire" é chamado *block*, como é
   consistente com "Lock.acquire()".

   get_value()

      Return the current value of semaphore.

      Observe que isso pode levantar "NotImplementedError" em
      plataformas como macOS, onde "sem_getvalue()" não está
      implementado.

   locked()

      Return a boolean indicating whether this object is locked right
      now.

      Adicionado na versão 3.14.

Nota:

  No macOS, não há suporte a "sem_timedwait", então chamar "acquire()"
  com um tempo limite emulará o comportamento dessa função usando um
  laço de suspensão.

Nota:

  Algumas das funcionalidades deste pacote exibem uma implementação de
  semáforo compartilhado funcional no sistema operacional host. Sem
  uma, o módulo "multiprocessing.synchronize" será desabilitado e as
  tentativas de importação dele resultarão em um "ImportError". Veja
  bpo-3770 para informações adicionais.


Objetos "ctypes" compartilhados
-------------------------------

É possível criar objetos compartilhados usando memória compartilhada
que pode ser herdada por processos filhos.

multiprocessing.Value(typecode_or_type, *args, lock=True)

   Retorna um objeto "ctypes" alocado da memória compartilhada. Por
   padrão, o valor de retorno é, na verdade, um invólucro sincronizado
   para o objeto. O objeto em si pode ser acessado por meio do
   atributo *value* de um "Value".

   *typecode_or_type* determina o tipo do objeto retornado: é um tipo
   ctypes ou um typecode de um caractere do tipo usado pelo módulo
   "array". **args* é passado para o construtor para o tipo.

   Se *lock* for "True" (o padrão), então um novo objeto de trava
   recursiva é criado para sincronizar o acesso ao valor. Se *lock*
   for um objeto "Lock" ou "RLock", então ele será usado para
   sincronizar o acesso ao valor. Se *lock* for "False", então o
   acesso ao objeto retornado não será protegido automaticamente por
   uma trava, então ele não será necessariamente "seguro para
   processo".

   Operações como "+=" que envolvem uma leitura e escrita não são
   atômicas. Então se, por exemplo, você quiser incrementar
   atomicamente um valor compartilhado, não é suficiente apenas fazer

      counter.value += 1

   Supondo que a trava associada seja recursiva (o que é por padrão),
   você pode fazer

      with counter.get_lock():
          counter.value += 1

   Observe que *lock* é um argumento somente-nomeado.

multiprocessing.Array(typecode_or_type, size_or_initializer, *, lock=True)

   Retorna um vetor de ctypes alocado da memória compartilhada. Por
   padrão, o valor de retorno é, na verdade, um invólucro sincronizado
   para o vetor.

   *typecode_or_type* determines the type of the elements of the
   returned array: it is either a ctypes type or a one character
   typecode of the kind used by the "array" module with the exception
   of "'w'", which is not supported.  In addition, the "'c'" typecode
   is an alias for "ctypes.c_char".  If *size_or_initializer* is an
   integer, then it determines the length of the array, and the array
   will be initially zeroed. Otherwise, *size_or_initializer* is a
   sequence which is used to initialize the array and whose length
   determines the length of the array.

   Se *lock* for "True" (o padrão), então um novo objeto de trava é
   criado para sincronizar o acesso ao valor. Se *lock* for um objeto
   "Lock" ou "RLock", então ele será usado para sincronizar o acesso
   ao valor. Se *lock* for "False", então o acesso ao objeto retornado
   não será protegido automaticamente por uma trava, então ele não
   será necessariamente "seguro para processo".

   Observe que *lock* é um argumento somente-nomeado.

   Note that an array of "ctypes.c_char" has *value* and *raw*
   attributes which can both be used to store and retrieve byte
   strings. While *raw* allows interaction with a "bytes" object the
   full size of the array, reading *value* will terminate after a null
   byte, like most programming languages handle strings.


The "multiprocessing.sharedctypes" module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "multiprocessing.sharedctypes" module provides functions for
allocating "ctypes" objects from shared memory which can be inherited
by child processes.

Nota:

  Embora seja possível armazenar um ponteiro na memória compartilhada,
  lembre-se de que isso se referirá a um local no espaço de endereço
  de um processo específico. No entanto, é bem provável que o ponteiro
  seja inválido no contexto de um segundo processo e tentar
  desreferenciar o ponteiro do segundo processo pode causar um
  travamento.

multiprocessing.sharedctypes.RawArray(typecode_or_type, size_or_initializer)

   Retorna um vetor de ctypes alocado da memória compartilhada.

   *typecode_or_type* determina o tipo dos elementos do vetor
   retornado: é um tipo ctypes ou um typecode de um caractere do tipo
   usado pelo módulo "array". Se *size_or_initializer* for um inteiro,
   então ele determina o comprimento do vetor, e o vetor será
   inicialmente zerado. Caso contrário, *size_or_initializer* é uma
   sequência que é usada para inicializar o vetor e cujo comprimento
   determina o comprimento do vetor.

   Observe que definir e obter um elemento é potencialmente não
   atômico -- use "Array()" para garantir que o acesso seja
   sincronizado automaticamente usando uma trava.

multiprocessing.sharedctypes.RawValue(typecode_or_type, *args)

   Retorna um objeto ctypes alocado da memória compartilhada.

   *typecode_or_type* determina o tipo do objeto retornado: é um tipo
   ctypes ou um typecode de um caractere do tipo usado pelo módulo
   "array". **args* é passado para o construtor para o tipo.

   Observe que definir e obter o valor é potencialmente não atômico --
   use "Value()" para garantir que o acesso seja sincronizado
   automaticamente usando uma trava.

   Observe que um vetor de "ctypes.c_char" tem atributos "value" e
   "raw" que permitem usá-la para armazenar e recuperar strings --
   veja a documentação de "ctypes".

multiprocessing.sharedctypes.Array(typecode_or_type, size_or_initializer, *, lock=True, ctx=None)

   O mesmo que "RawArray()", exceto que dependendo do valor de *lock*,
   um invólucro de sincronização seguro para processo pode ser
   retornado em vez de um vetor de ctypes brutos.

   Se *lock* for "True" (o padrão), então um novo objeto de trava é
   criado para sincronizar o acesso ao valor. Se *lock* for um objeto
   "Lock" ou "RLock", então ele será usado para sincronizar o acesso
   ao valor. Se *lock* for "False", então o acesso ao objeto retornado
   não será protegido automaticamente por uma trava, então ele não
   será necessariamente "seguro para processo".

   *ctx* is a context object, or "None" (use the current context). If
   "None", calling this may set the global start method. See Global
   start method for more details.

   Note that *lock* and *ctx* are keyword-only parameters.

multiprocessing.sharedctypes.Value(typecode_or_type, *args, lock=True, ctx=None)

   O mesmo que "RawValue()", exceto que dependendo do valor de *lock*,
   um invólucro de sincronização seguro para processo pode ser
   retornado em vez de um objeto ctypes brutos.

   Se *lock* for "True" (o padrão), então um novo objeto de trava é
   criado para sincronizar o acesso ao valor. Se *lock* for um objeto
   "Lock" ou "RLock", então ele será usado para sincronizar o acesso
   ao valor. Se *lock* for "False", então o acesso ao objeto retornado
   não será protegido automaticamente por uma trava, então ele não
   será necessariamente "seguro para processo".

   *ctx* is a context object, or "None" (use the current context). If
   "None", calling this may set the global start method. See Global
   start method for more details.

   Note that *lock* and *ctx* are keyword-only parameters.

multiprocessing.sharedctypes.copy(obj)

   Retorna um objeto ctypes alocado da memória compartilhada que é uma
   cópia do objeto ctypes *obj*.

multiprocessing.sharedctypes.synchronized(obj, lock=None, ctx=None)

   Retorna um objeto invólucro seguro para o processo para um objeto
   ctypes que usa *lock* para sincronizar o acesso. Se *lock* for
   "None" (o padrão), então um objeto "multiprocessing.RLock" é criado
   automaticamente.

   *ctx* is a context object, or "None" (use the current context). If
   "None", calling this may set the global start method. See Global
   start method for more details.

   A synchronized wrapper will have two methods in addition to those
   of the object it wraps: "get_obj()" returns the wrapped object and
   "get_lock()" returns the lock object used for synchronization.

   Note that accessing the ctypes object through the wrapper can be a
   lot slower than accessing the raw ctypes object.

   Alterado na versão 3.5: Synchronized objects support the *context
   manager* protocol.

The table below compares the syntax for creating shared ctypes objects
from shared memory with the normal ctypes syntax.  (In the table
"MyStruct" is some subclass of "ctypes.Structure".)

+----------------------+----------------------------+-----------------------------+
| ctypes               | sharedctypes using type    | sharedctypes using typecode |
|======================|============================|=============================|
| c_double(2.4)        | RawValue(c_double, 2.4)    | RawValue('d', 2.4)          |
+----------------------+----------------------------+-----------------------------+
| MyStruct(4, 6)       | RawValue(MyStruct, 4, 6)   |                             |
+----------------------+----------------------------+-----------------------------+
| (c_short * 7)()      | RawArray(c_short, 7)       | RawArray('h', 7)            |
+----------------------+----------------------------+-----------------------------+
| (c_int * 3)(9, 2, 8) | RawArray(c_int, (9, 2, 8)) | RawArray('i', (9, 2, 8))    |
+----------------------+----------------------------+-----------------------------+

Below is an example where a number of ctypes objects are modified by a
child process:

   from multiprocessing import Process, Lock
   from multiprocessing.sharedctypes import Value, Array
   from ctypes import Structure, c_double

   class Point(Structure):
       _fields_ = [('x', c_double), ('y', c_double)]

   def modify(n, x, s, A):
       n.value **= 2
       x.value **= 2
       s.value = s.value.upper()
       for a in A:
           a.x **= 2
           a.y **= 2

   if __name__ == '__main__':
       lock = Lock()

       n = Value('i', 7)
       x = Value(c_double, 1.0/3.0, lock=False)
       s = Array('c', b'hello world', lock=lock)
       A = Array(Point, [(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock=lock)

       p = Process(target=modify, args=(n, x, s, A))
       p.start()
       p.join()

       print(n.value)
       print(x.value)
       print(s.value)
       print([(a.x, a.y) for a in A])

The results printed are

   49
   0.1111111111111111
   HELLO WORLD
   [(3.515625, 39.0625), (33.0625, 4.0), (5.640625, 90.25)]


Gerenciadores
-------------

Managers provide a way to create data which can be shared between
different processes, including sharing over a network between
processes running on different machines. A manager object controls a
server process which manages *shared objects*.  Other processes can
access the shared objects by using proxies.

multiprocessing.Manager()

   Retorna um objeto "SyncManager" inicializado que pode ser usado
   para compartilhar objetos entre processos. O objeto gerenciador
   retornado corresponde a um processo filho gerado e tem métodos que
   criarão objetos compartilhados e retornarão proxies
   correspondentes.

Manager processes will be shutdown as soon as they are garbage
collected or their parent process exits.  The manager classes are
defined in the "multiprocessing.managers" module:

class multiprocessing.managers.BaseManager(address=None, authkey=None, serializer='pickle', ctx=None, *, shutdown_timeout=1.0)

   Criando um objeto BaseManager.

   Once created one should call "start()" or
   "get_server().serve_forever()" to ensure that the manager object
   refers to a started manager process.

   *address* is the address on which the manager process listens for
   new connections.  If *address* is "None" then an arbitrary one is
   chosen.

   *authkey* is the authentication key which will be used to check the
   validity of incoming connections to the server process.  If
   *authkey* is "None" then "current_process().authkey" is used.
   Otherwise *authkey* is used and it must be a byte string.

   *serializer* must be "'pickle'" (use "pickle" serialization) or
   "'xmlrpclib'" (use "xmlrpc.client" serialization).

   *ctx* is a context object, or "None" (use the current context). If
   "None", calling this may set the global start method. See Global
   start method for more details.

   *shutdown_timeout* is a timeout in seconds used to wait until the
   process used by the manager completes in the "shutdown()" method.
   If the shutdown times out, the process is terminated. If
   terminating the process also times out, the process is killed.

   Alterado na versão 3.11: Added the *shutdown_timeout* parameter.

   start([initializer[, initargs]])

      Start a subprocess to start the manager.  If *initializer* is
      not "None" then the subprocess will call
      "initializer(*initargs)" when it starts.

   get_server()

      Returns a "Server" object which represents the actual server
      under the control of the Manager. The "Server" object supports
      the "serve_forever()" method:

         >>> from multiprocessing.managers import BaseManager
         >>> manager = BaseManager(address=('', 50000), authkey=b'abc')
         >>> server = manager.get_server()
         >>> server.serve_forever()

      "Server" additionally has an "address" attribute.

   connect()

      Connect a local manager object to a remote manager process:

         >>> from multiprocessing.managers import BaseManager
         >>> m = BaseManager(address=('127.0.0.1', 50000), authkey=b'abc')
         >>> m.connect()

   shutdown()

      Stop the process used by the manager.  This is only available if
      "start()" has been used to start the server process.

      This can be called multiple times.

   register(typeid[, callable[, proxytype[, exposed[, method_to_typeid[, create_method]]]]])

      A classmethod which can be used for registering a type or
      callable with the manager class.

      *typeid* is a "type identifier" which is used to identify a
      particular type of shared object.  This must be a string.

      *callable* is a callable used for creating objects for this type
      identifier.  If a manager instance will be connected to the
      server using the "connect()" method, or if the *create_method*
      argument is "False" then this can be left as "None".

      *proxytype* is a subclass of "BaseProxy" which is used to create
      proxies for shared objects with this *typeid*.  If "None" then a
      proxy class is created automatically.

      *exposed* is used to specify a sequence of method names which
      proxies for this typeid should be allowed to access using
      "BaseProxy._callmethod()".  (If *exposed* is "None" then
      "proxytype._exposed_" is used instead if it exists.)  In the
      case where no exposed list is specified, all "public methods" of
      the shared object will be accessible.  (Here a "public method"
      means any attribute which has a "__call__()" method and whose
      name does not begin with "'_'".)

      *method_to_typeid* is a mapping used to specify the return type
      of those exposed methods which should return a proxy.  It maps
      method names to typeid strings.  (If *method_to_typeid* is
      "None" then "proxytype._method_to_typeid_" is used instead if it
      exists.)  If a method's name is not a key of this mapping or if
      the mapping is "None" then the object returned by the method
      will be copied by value.

      *create_method* determines whether a method should be created
      with name *typeid* which can be used to tell the server process
      to create a new shared object and return a proxy for it.  By
      default it is "True".

   "BaseManager" instances also have one read-only property:

   address

      The address used by the manager.

   Alterado na versão 3.3: Manager objects support the context
   management protocol -- see Tipos de Gerenciador de Contexto.
   "__enter__()" starts the server process (if it has not already
   started) and then returns the manager object.  "__exit__()" calls
   "shutdown()".In previous versions "__enter__()" did not start the
   manager's server process if it was not already started.

class multiprocessing.managers.SyncManager

   A subclass of "BaseManager" which can be used for the
   synchronization of processes.  Objects of this type are returned by
   "multiprocessing.Manager()".

   Its methods create and return Objetos proxies for a number of
   commonly used data types to be synchronized across processes. This
   notably includes shared lists and dictionaries.

   Barrier(parties[, action[, timeout]])

      Create a shared "threading.Barrier" object and return a proxy
      for it.

      Adicionado na versão 3.3.

   BoundedSemaphore([value])

      Create a shared "threading.BoundedSemaphore" object and return a
      proxy for it.

   Condition([lock])

      Create a shared "threading.Condition" object and return a proxy
      for it.

      If *lock* is supplied then it should be a proxy for a
      "threading.Lock" or "threading.RLock" object.

      Alterado na versão 3.3: O método "wait_for()" foi adicionado.

   Event()

      Create a shared "threading.Event" object and return a proxy for
      it.

   Lock()

      Create a shared "threading.Lock" object and return a proxy for
      it.

   Namespace()

      Create a shared "Namespace" object and return a proxy for it.

   Queue([maxsize])

      Create a shared "queue.Queue" object and return a proxy for it.

   RLock()

      Create a shared "threading.RLock" object and return a proxy for
      it.

   Semaphore([value])

      Create a shared "threading.Semaphore" object and return a proxy
      for it.

   Array(typecode, sequence)

      Create an array and return a proxy for it.

   Value(typecode, value)

      Create an object with a writable "value" attribute and return a
      proxy for it.

   dict()
   dict(mapping)
   dict(sequence)

      Create a shared "dict" object and return a proxy for it.

   list()
   list(sequence)

      Create a shared "list" object and return a proxy for it.

   set()
   set(sequence)
   set(mapping)

      Cria um objeto "set" compartilhado e retorna um proxy para ele.

      Adicionado na versão 3.14: Foi adicionado suporte para "set".

   Alterado na versão 3.6: Objetos compartilhados podem ser aninhados.
   Por exemplo, em um objeto contêiner compartilhado, como uma lista
   compartilhada, é possível conter outros objeto compartilhados que
   serão gerenciados e sincronizados pelo "SyncManager".

class multiprocessing.managers.Namespace

   A type that can register with "SyncManager".

   A namespace object has no public methods, but does have writable
   attributes. Its representation shows the values of its attributes.

   However, when using a proxy for a namespace object, an attribute
   beginning with "'_'" will be an attribute of the proxy and not an
   attribute of the referent:

      >>> mp_context = multiprocessing.get_context('spawn')
      >>> manager = mp_context.Manager()
      >>> Global = manager.Namespace()
      >>> Global.x = 10
      >>> Global.y = 'hello'
      >>> Global._z = 12.3    # this is an attribute of the proxy
      >>> print(Global)
      Namespace(x=10, y='hello')


Customized managers
~~~~~~~~~~~~~~~~~~~

To create one's own manager, one creates a subclass of "BaseManager"
and uses the "register()" classmethod to register new types or
callables with the manager class.  For example:

   from multiprocessing.managers import BaseManager

   class MathsClass:
       def add(self, x, y):
           return x + y
       def mul(self, x, y):
           return x * y

   class MyManager(BaseManager):
       pass

   MyManager.register('Maths', MathsClass)

   if __name__ == '__main__':
       with MyManager() as manager:
           maths = manager.Maths()
           print(maths.add(4, 3))         # prints 7
           print(maths.mul(7, 8))         # prints 56


Using a remote manager
~~~~~~~~~~~~~~~~~~~~~~

It is possible to run a manager server on one machine and have clients
use it from other machines (assuming that the firewalls involved allow
it).

Running the following commands creates a server for a single shared
queue which remote clients can access:

   >>> from multiprocessing.managers import BaseManager
   >>> from queue import Queue
   >>> queue = Queue()
   >>> class QueueManager(BaseManager): pass
   >>> QueueManager.register('get_queue', callable=lambda:queue)
   >>> m = QueueManager(address=('', 50000), authkey=b'abracadabra')
   >>> s = m.get_server()
   >>> s.serve_forever()

One client can access the server as follows:

   >>> from multiprocessing.managers import BaseManager
   >>> class QueueManager(BaseManager): pass
   >>> QueueManager.register('get_queue')
   >>> m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra')
   >>> m.connect()
   >>> queue = m.get_queue()
   >>> queue.put('hello')

Another client can also use it:

   >>> from multiprocessing.managers import BaseManager
   >>> class QueueManager(BaseManager): pass
   >>> QueueManager.register('get_queue')
   >>> m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra')
   >>> m.connect()
   >>> queue = m.get_queue()
   >>> queue.get()
   'hello'

Local processes can also access that queue, using the code from above
on the client to access it remotely:

   >>> from multiprocessing import Process, Queue
   >>> from multiprocessing.managers import BaseManager
   >>> class Worker(Process):
   ...     def __init__(self, q):
   ...         self.q = q
   ...         super().__init__()
   ...     def run(self):
   ...         self.q.put('local hello')
   ...
   >>> queue = Queue()
   >>> w = Worker(queue)
   >>> w.start()
   >>> class QueueManager(BaseManager): pass
   ...
   >>> QueueManager.register('get_queue', callable=lambda: queue)
   >>> m = QueueManager(address=('', 50000), authkey=b'abracadabra')
   >>> s = m.get_server()
   >>> s.serve_forever()


Objetos proxies
---------------

Um proxy é um objeto que *refere-se* a um objeto compartilhado que
reside (presumivelmente) em um processo diferente.  Dizemos que o
objeto compartilhado é o *referente* do proxy.  Vários objetos proxies
podem ter o mesmo referente.

Um proxy objeto tem métodos que invocam métodos correspondes de seu
referente (embora nem todo método do referente esteja necessariamente
disponível por meio do proxy).  Dessa forma, um proxy pode ser usado
da mesma forma que seu referente:

   >>> mp_context = multiprocessing.get_context('spawn')
   >>> manager = mp_context.Manager()
   >>> l = manager.list([i*i for i in range(10)])
   >>> print(l)
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   >>> print(repr(l))
   <ListProxy object, typeid 'list' at 0x...>
   >>> l[4]
   16
   >>> l[2:5]
   [4, 9, 16]

Observe que, ao aplicar "str()" a um proxy, o retorno representará o
referente, enquanto que ao aplicar o "repr()", o retorno representará
o proxy.

Um aspecto importante dos objetos proxies é o fato de que eles podem
ser serializados com pickle, portanto podem ser transferidos entre
processos.  Dessa forma, um referente pode conter Objetos proxies.
Isso permite o aninhamento dessas listas e dicionários gerenciados e
outros Objetos proxies:

   >>> a = manager.list()
   >>> b = manager.list()
   >>> a.append(b)         # referente de a agora contém referente de b
   >>> print(a, b)
   [<ListProxy object, typeid 'list' at ...>] []
   >>> b.append('hello')
   >>> print(a[0], b)
   ['hello'] ['hello']

Da mesma forma, os proxies de dicionários e listas podem ser aninhados
um dentro do outro:

   >>> l_outer = manager.list([ manager.dict() for i in range(2) ])
   >>> d_first_inner = l_outer[0]
   >>> d_first_inner['a'] = 1
   >>> d_first_inner['b'] = 2
   >>> l_outer[1]['c'] = 3
   >>> l_outer[1]['z'] = 26
   >>> print(l_outer[0])
   {'a': 1, 'b': 2}
   >>> print(l_outer[1])
   {'c': 3, 'z': 26}

Se objetos padrões (não-proxy) de "list" ou "dict" estiverem contidos
em um referente, as modificações nesses mutáveis não serão propagadas
pelo gerente porque o proxy não tem como saber quando os valores
contidos nele são modificados.  No entanto, o armazenamento de um
valor em um proxy contêiner (que aciona um "__setitem__" no objeto
proxy) se propaga pelo gerenciador e, portanto, para modificar
efetivamente esse item, é possível reatribuir o valor modificado ao
proxy contêiner:

   # cria um proxy para uma lista e adicionar um objeto mutável (um dicionário)
   lproxy = manager.list()
   lproxy.append({})
   # agora modifica o dicionário
   d = lproxy[0]
   d['a'] = 1
   d['b'] = 2
   # neste ponto, as mudanças em d não estão ainda sincronizadas, mas
   # atualizando o dicionário, o proxy é notificado da mudança
   lproxy[0] = d

Essa abordagem talvez seja menos conveniente do que usar Objetos
proxies aninhados para a maioria dos casos de uso, mas também
demonstra um nível de controle sobre a sincronização.

Nota:

  The proxy types in "multiprocessing" do nothing to support
  comparisons by value.  So, for instance, we have:

     >>> manager.list([1,2,3]) == [1,2,3]
     False

  Em vez disso, deve-se usar uma cópia do referente ao fazer
  comparações.

class multiprocessing.managers.BaseProxy

   Proxy objects are instances of subclasses of "BaseProxy".

   _callmethod(methodname[, args[, kwds]])

      Call and return the result of a method of the proxy's referent.

      If "proxy" is a proxy whose referent is "obj" then the
      expression

         proxy._callmethod(methodname, args, kwds)

      will evaluate the expression

         getattr(obj, methodname)(*args, **kwds)

      in the manager's process.

      The returned value will be a copy of the result of the call or a
      proxy to a new shared object -- see documentation for the
      *method_to_typeid* argument of "BaseManager.register()".

      If an exception is raised by the call, then is re-raised by
      "_callmethod()".  If some other exception is raised in the
      manager's process then this is converted into a "RemoteError"
      exception and is raised by "_callmethod()".

      Note in particular that an exception will be raised if
      *methodname* has not been *exposed*.

      An example of the usage of "_callmethod()":

         >>> l = manager.list(range(10))
         >>> l._callmethod('__len__')
         10
         >>> l._callmethod('__getitem__', (slice(2, 7),)) # equivalent to l[2:7]
         [2, 3, 4, 5, 6]
         >>> l._callmethod('__getitem__', (20,))          # equivalent to l[20]
         Traceback (most recent call last):
         ...
         IndexError: list index out of range

   _getvalue()

      Return a copy of the referent.

      If the referent is unpicklable then this will raise an
      exception.

   __repr__()

      Return a representation of the proxy object.

   __str__()

      Return the representation of the referent.


Limpeza
~~~~~~~

A proxy object uses a weakref callback so that when it gets garbage
collected it deregisters itself from the manager which owns its
referent.

A shared object gets deleted from the manager process when there are
no longer any proxies referring to it.


Process Pools
-------------

One can create a pool of processes which will carry out tasks
submitted to it with the "Pool" class.

class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])

   A process pool object which controls a pool of worker processes to
   which jobs can be submitted.  It supports asynchronous results with
   timeouts and callbacks and has a parallel map implementation.

   *processes* is the number of worker processes to use.  If
   *processes* is "None" then the number returned by
   "os.process_cpu_count()" is used.

   If *initializer* is not "None" then each worker process will call
   "initializer(*initargs)" when it starts.

   *maxtasksperchild* is the number of tasks a worker process can
   complete before it will exit and be replaced with a fresh worker
   process, to enable unused resources to be freed. The default
   *maxtasksperchild* is "None", which means worker processes will
   live as long as the pool.

   *context* can be used to specify the context used for starting the
   worker processes.  Usually a pool is created using the function
   "multiprocessing.Pool()" or the "Pool()" method of a context
   object.  In both cases *context* is set appropriately. If "None",
   calling this function will have the side effect of setting the
   current global start method if it has not been set already. See the
   "get_context()" function.

   Note that the methods of the pool object should only be called by
   the process which created the pool.

   Aviso:

     "Pool" objects have internal resources that need to be properly
     managed (like any other resource) by using the pool as a context
     manager or by calling "close()" and "terminate()" manually.
     Failure to do this can lead to the process hanging on
     finalization.Note that it is **not correct** to rely on the
     garbage collector to destroy the pool as CPython does not assure
     that the finalizer of the pool will be called (see
     "object.__del__()" for more information).

   Alterado na versão 3.2: Added the *maxtasksperchild* parameter.

   Alterado na versão 3.4: Adicionado o parâmetro *context*.

   Alterado na versão 3.13: *processes* uses "os.process_cpu_count()"
   by default, instead of "os.cpu_count()".

   Nota:

     Worker processes within a "Pool" typically live for the complete
     duration of the Pool's work queue. A frequent pattern found in
     other systems (such as Apache, mod_wsgi, etc) to free resources
     held by workers is to allow a worker within a pool to complete
     only a set amount of work before exiting, being cleaned up and a
     new process spawned to replace the old one. The
     *maxtasksperchild* argument to the "Pool" exposes this ability to
     the end user.

   apply(func[, args[, kwds]])

      Call *func* with arguments *args* and keyword arguments *kwds*.
      It blocks until the result is ready. Given this blocks,
      "apply_async()" is better suited for performing work in
      parallel. Additionally, *func* is only executed in one of the
      workers of the pool.

   apply_async(func[, args[, kwds[, callback[, error_callback]]]])

      A variant of the "apply()" method which returns a "AsyncResult"
      object.

      If *callback* is specified then it should be a callable which
      accepts a single argument.  When the result becomes ready
      *callback* is applied to it, that is unless the call failed, in
      which case the *error_callback* is applied instead.

      If *error_callback* is specified then it should be a callable
      which accepts a single argument.  If the target function fails,
      then the *error_callback* is called with the exception instance.

      Callbacks should complete immediately since otherwise the thread
      which handles the results will get blocked.

   map(func, iterable[, chunksize])

      A parallel equivalent of the "map()" built-in function (it
      supports only one *iterable* argument though, for multiple
      iterables see "starmap()"). It blocks until the result is ready.

      This method chops the iterable into a number of chunks which it
      submits to the process pool as separate tasks.  The
      (approximate) size of these chunks can be specified by setting
      *chunksize* to a positive integer.

      Note that it may cause high memory usage for very long
      iterables. Consider using "imap()" or "imap_unordered()" with
      explicit *chunksize* option for better efficiency.

   map_async(func, iterable[, chunksize[, callback[, error_callback]]])

      A variant of the "map()" method which returns a "AsyncResult"
      object.

      If *callback* is specified then it should be a callable which
      accepts a single argument.  When the result becomes ready
      *callback* is applied to it, that is unless the call failed, in
      which case the *error_callback* is applied instead.

      If *error_callback* is specified then it should be a callable
      which accepts a single argument.  If the target function fails,
      then the *error_callback* is called with the exception instance.

      Callbacks should complete immediately since otherwise the thread
      which handles the results will get blocked.

   imap(func, iterable[, chunksize])

      An iterator-based version of "map()".

      The *chunksize* argument is the same as the one used by the
      "map()" method.  For very long iterables using a large value for
      *chunksize* can make the job complete **much** faster than using
      the default value of "1".

      Also if *chunksize* is "1" then the "next()" method of the
      iterator returned by the "imap()" method has an optional
      *timeout* parameter: "next(timeout)" will raise
      "multiprocessing.TimeoutError" if the result cannot be returned
      within *timeout* seconds.

   imap_unordered(func, iterable[, chunksize])

      The same as "imap()" except that the ordering of the results
      from the returned iterator should be considered arbitrary.
      (Only when there is only one worker process is the order
      guaranteed to be "correct".)

   starmap(func, iterable[, chunksize])

      Like "map()" except that the elements of the *iterable* are
      expected to be iterables that are unpacked as arguments.

      Hence an *iterable* of "[(1,2), (3, 4)]" results in "[func(1,2),
      func(3,4)]".

      Adicionado na versão 3.3.

   starmap_async(func, iterable[, chunksize[, callback[, error_callback]]])

      A combination of "starmap()" and "map_async()" that iterates
      over *iterable* of iterables and calls *func* with the iterables
      unpacked. Returns a result object.

      Adicionado na versão 3.3.

   close()

      Prevents any more tasks from being submitted to the pool.  Once
      all the tasks have been completed the worker processes will
      exit.

   terminate()

      Stops the worker processes immediately without completing
      outstanding work.  When the pool object is garbage collected
      "terminate()" will be called immediately.

   join()

      Wait for the worker processes to exit.  One must call "close()"
      or "terminate()" before using "join()".

   Alterado na versão 3.3: Pool objects now support the context
   management protocol -- see Tipos de Gerenciador de Contexto.
   "__enter__()" returns the pool object, and "__exit__()" calls
   "terminate()".

class multiprocessing.pool.AsyncResult

   The class of the result returned by "Pool.apply_async()" and
   "Pool.map_async()".

   get([timeout])

      Return the result when it arrives.  If *timeout* is not "None"
      and the result does not arrive within *timeout* seconds then
      "multiprocessing.TimeoutError" is raised.  If the remote call
      raised an exception then that exception will be reraised by
      "get()".

   wait([timeout])

      Wait until the result is available or until *timeout* seconds
      pass.

   ready()

      Return whether the call has completed.

   successful()

      Return whether the call completed without raising an exception.
      Will raise "ValueError" if the result is not ready.

      Alterado na versão 3.7: If the result is not ready, "ValueError"
      is raised instead of "AssertionError".

The following example demonstrates the use of a pool:

   from multiprocessing import Pool
   import time

   def f(x):
       return x*x

   if __name__ == '__main__':
       with Pool(processes=4) as pool:         # start 4 worker processes
           result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
           print(result.get(timeout=1))        # prints "100" unless your computer is *very* slow

           print(pool.map(f, range(10)))       # prints "[0, 1, 4,..., 81]"

           it = pool.imap(f, range(10))
           print(next(it))                     # prints "0"
           print(next(it))                     # prints "1"
           print(it.next(timeout=1))           # prints "4" unless your computer is *very* slow

           result = pool.apply_async(time.sleep, (10,))
           print(result.get(timeout=1))        # raises multiprocessing.TimeoutError


Listeners and Clients
---------------------

Usually message passing between processes is done using queues or by
using "Connection" objects returned by "Pipe()".

However, the "multiprocessing.connection" module allows some extra
flexibility.  It basically gives a high level message oriented API for
dealing with sockets or Windows named pipes.  It also has support for
*digest authentication* using the "hmac" module, and for polling
multiple connections at the same time.

multiprocessing.connection.deliver_challenge(connection, authkey)

   Send a randomly generated message to the other end of the
   connection and wait for a reply.

   If the reply matches the digest of the message using *authkey* as
   the key then a welcome message is sent to the other end of the
   connection.  Otherwise "AuthenticationError" is raised.

multiprocessing.connection.answer_challenge(connection, authkey)

   Receive a message, calculate the digest of the message using
   *authkey* as the key, and then send the digest back.

   If a welcome message is not received, then "AuthenticationError" is
   raised.

multiprocessing.connection.Client(address[, family[, authkey]])

   Attempt to set up a connection to the listener which is using
   address *address*, returning a "Connection".

   The type of the connection is determined by *family* argument, but
   this can generally be omitted since it can usually be inferred from
   the format of *address*. (See Formatos de Endereços)

   If *authkey* is given and not "None", it should be a byte string
   and will be used as the secret key for an HMAC-based authentication
   challenge. No authentication is done if *authkey* is "None".
   "AuthenticationError" is raised if authentication fails. See
   Authentication keys.

class multiprocessing.connection.Listener([address[, family[, backlog[, authkey]]]])

   A wrapper for a bound socket or Windows named pipe which is
   'listening' for connections.

   *address* is the address to be used by the bound socket or named
   pipe of the listener object.

   Nota:

     If an address of '0.0.0.0' is used, the address will not be a
     connectable end point on Windows. If you require a connectable
     end-point, you should use '127.0.0.1'.

   *family* is the type of socket (or named pipe) to use.  This can be
   one of the strings "'AF_INET'" (for a TCP socket), "'AF_UNIX'" (for
   a Unix domain socket) or "'AF_PIPE'" (for a Windows named pipe).
   Of these only the first is guaranteed to be available.  If *family*
   is "None" then the family is inferred from the format of *address*.
   If *address* is also "None" then a default is chosen.  This default
   is the family which is assumed to be the fastest available.  See
   Formatos de Endereços.  Note that if *family* is "'AF_UNIX'" and
   address is "None" then the socket will be created in a private
   temporary directory created using "tempfile.mkstemp()".

   If the listener object uses a socket then *backlog* (1 by default)
   is passed to the "listen()" method of the socket once it has been
   bound.

   If *authkey* is given and not "None", it should be a byte string
   and will be used as the secret key for an HMAC-based authentication
   challenge. No authentication is done if *authkey* is "None".
   "AuthenticationError" is raised if authentication fails. See
   Authentication keys.

   accept()

      Accept a connection on the bound socket or named pipe of the
      listener object and return a "Connection" object. If
      authentication is attempted and fails, then
      "AuthenticationError" is raised.

   close()

      Close the bound socket or named pipe of the listener object.
      This is called automatically when the listener is garbage
      collected.  However it is advisable to call it explicitly.

   Listener objects have the following read-only properties:

   address

      The address which is being used by the Listener object.

   last_accepted

      The address from which the last accepted connection came.  If
      this is unavailable then it is "None".

   Alterado na versão 3.3: Listener objects now support the context
   management protocol -- see Tipos de Gerenciador de Contexto.
   "__enter__()" returns the listener object, and "__exit__()" calls
   "close()".

multiprocessing.connection.wait(object_list, timeout=None)

   Wait till an object in *object_list* is ready.  Returns the list of
   those objects in *object_list* which are ready.  If *timeout* is a
   float then the call blocks for at most that many seconds.  If
   *timeout* is "None" then it will block for an unlimited period. A
   negative timeout is equivalent to a zero timeout.

   For both POSIX and Windows, an object can appear in *object_list*
   if it is

   * a readable "Connection" object;

   * a connected and readable "socket.socket" object; or

   * the "sentinel" attribute of a "Process" object.

   A connection or socket object is ready when there is data available
   to be read from it, or the other end has been closed.

   **POSIX**: "wait(object_list, timeout)" almost equivalent
   "select.select(object_list, [], [], timeout)".  The difference is
   that, if "select.select()" is interrupted by a signal, it can raise
   "OSError" with an error number of "EINTR", whereas "wait()" will
   not.

   **Windows**: An item in *object_list* must either be an integer
   handle which is waitable (according to the definition used by the
   documentation of the Win32 function "WaitForMultipleObjects()") or
   it can be an object with a "fileno()" method which returns a socket
   handle or pipe handle.  (Note that pipe handles and socket handles
   are **not** waitable handles.)

   Adicionado na versão 3.3.

**Examples**

The following server code creates a listener which uses "'secret
password'" as an authentication key.  It then waits for a connection
and sends some data to the client:

   from multiprocessing.connection import Listener
   from array import array

   address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

   with Listener(address, authkey=b'secret password') as listener:
       with listener.accept() as conn:
           print('connection accepted from', listener.last_accepted)

           conn.send([2.25, None, 'junk', float])

           conn.send_bytes(b'hello')

           conn.send_bytes(array('i', [42, 1729]))

The following code connects to the server and receives some data from
the server:

   from multiprocessing.connection import Client
   from array import array

   address = ('localhost', 6000)

   with Client(address, authkey=b'secret password') as conn:
       print(conn.recv())                  # => [2.25, None, 'junk', float]

       print(conn.recv_bytes())            # => 'hello'

       arr = array('i', [0, 0, 0, 0, 0])
       print(conn.recv_bytes_into(arr))    # => 8
       print(arr)                          # => array('i', [42, 1729, 0, 0, 0])

The following code uses "wait()" to wait for messages from multiple
processes at once:

   from multiprocessing import Process, Pipe, current_process
   from multiprocessing.connection import wait

   def foo(w):
       for i in range(10):
           w.send((i, current_process().name))
       w.close()

   if __name__ == '__main__':
       readers = []

       for i in range(4):
           r, w = Pipe(duplex=False)
           readers.append(r)
           p = Process(target=foo, args=(w,))
           p.start()
           # We close the writable end of the pipe now to be sure that
           # p is the only process which owns a handle for it.  This
           # ensures that when p closes its handle for the writable end,
           # wait() will promptly report the readable end as being ready.
           w.close()

       while readers:
           for r in wait(readers):
               try:
                   msg = r.recv()
               except EOFError:
                   readers.remove(r)
               else:
                   print(msg)


Formatos de Endereços
~~~~~~~~~~~~~~~~~~~~~

* Um endereço "'AF_INET'" é uma tupla na forma de "(hostname, port)"
  sendo *hostname* uma string e *port* um inteiro.

* An "'AF_UNIX'" address is a string representing a filename on the
  filesystem.

* An "'AF_PIPE'" address is a string of the form
  "r'\\.\pipe\*PipeName*'".  To use "Client()" to connect to a named
  pipe on a remote computer called *ServerName* one should use an
  address of the form "r'\\*ServerName*\pipe\*PipeName*'" instead.

Note that any string beginning with two backslashes is assumed by
default to be an "'AF_PIPE'" address rather than an "'AF_UNIX'"
address.


Authentication keys
-------------------

When one uses "Connection.recv", the data received is automatically
unpickled. Unfortunately unpickling data from an untrusted source is a
security risk. Therefore "Listener" and "Client()" use the "hmac"
module to provide digest authentication.

An authentication key is a byte string which can be thought of as a
password: once a connection is established both ends will demand proof
that the other knows the authentication key.  (Demonstrating that both
ends are using the same key does **not** involve sending the key over
the connection.)

If authentication is requested but no authentication key is specified
then the return value of "current_process().authkey" is used (see
"Process").  This value will be automatically inherited by any
"Process" object that the current process creates. This means that (by
default) all processes of a multi-process program will share a single
authentication key which can be used when setting up connections
between themselves.

Suitable authentication keys can also be generated by using
"os.urandom()".

This authentication protects "Listener" and "Client()" connections,
which are reachable by address.  It is not applied to the anonymous
pipes created by "Pipe()" or used internally by "Queue".
"multiprocessing" treats all local processes running as the same user
as trusted; on most operating systems such processes can access each
other's pipe file descriptors regardless.  Applications that require
isolation between processes of the same user must arrange it at the
operating-system level -- for example, by running workers under a
different user account or in a sandbox.


Gerando logs
------------

Some support for logging is available.  Note, however, that the
"logging" package does not use process shared locks so it is possible
(depending on the handler type) for messages from different processes
to get mixed up.

multiprocessing.get_logger()

   Returns the logger used by "multiprocessing".  If necessary, a new
   one will be created.

   When first created the logger has level "logging.NOTSET" and no
   default handler. Messages sent to this logger will not by default
   propagate to the root logger.

   Note that on Windows child processes will only inherit the level of
   the parent process's logger -- any other customization of the
   logger will not be inherited.

multiprocessing.log_to_stderr(level=None)

   This function performs a call to "get_logger()" but in addition to
   returning the logger created by get_logger, it adds a handler which
   sends output to "sys.stderr" using format
   "'[%(levelname)s/%(processName)s] %(message)s'". You can modify
   "levelname" of the logger by passing a "level" argument.

Below is an example session with logging turned on:

   >>> import multiprocessing, logging
   >>> logger = multiprocessing.log_to_stderr()
   >>> logger.setLevel(logging.INFO)
   >>> logger.warning('doomed')
   [WARNING/MainProcess] doomed
   >>> m = multiprocessing.Manager()
   [INFO/SyncManager-...] child process calling self.run()
   [INFO/SyncManager-...] created temp directory /.../pymp-...
   [INFO/SyncManager-...] manager serving at '/.../listener-...'
   >>> del m
   [INFO/MainProcess] sending shutdown message to manager
   [INFO/SyncManager-...] manager exiting with exitcode 0

For a full table of logging levels, see the "logging" module.


The "multiprocessing.dummy" module
----------------------------------

"multiprocessing.dummy" replicates the API of "multiprocessing" but is
no more than a wrapper around the "threading" module.

In particular, the "Pool" function provided by "multiprocessing.dummy"
returns an instance of "ThreadPool", which is a subclass of "Pool"
that supports all the same method calls but uses a pool of worker
threads rather than worker processes.

class multiprocessing.pool.ThreadPool([processes[, initializer[, initargs]]])

   A thread pool object which controls a pool of worker threads to
   which jobs can be submitted.  "ThreadPool" instances are fully
   interface compatible with "Pool" instances, and their resources
   must also be properly managed, either by using the pool as a
   context manager or by calling "close()" and "terminate()" manually.

   *processes* is the number of worker threads to use.  If *processes*
   is "None" then the number returned by "os.process_cpu_count()" is
   used.

   If *initializer* is not "None" then each worker process will call
   "initializer(*initargs)" when it starts.

   Unlike "Pool", *maxtasksperchild* and *context* cannot be provided.

   Nota:

     A "ThreadPool" shares the same interface as "Pool", which is
     designed around a pool of processes and predates the introduction
     of the "concurrent.futures" module.  As such, it inherits some
     operations that don't make sense for a pool backed by threads,
     and it has its own type for representing the status of
     asynchronous jobs, "AsyncResult", that is not understood by any
     other libraries.Users should generally prefer to use
     "concurrent.futures.ThreadPoolExecutor", which has a simpler
     interface that was designed around threads from the start, and
     which returns "concurrent.futures.Future" instances that are
     compatible with many other libraries, including "asyncio".


Programming guidelines
======================

There are certain guidelines and idioms which should be adhered to
when using "multiprocessing".


All start methods
-----------------

The following applies to all start methods.

Avoid shared state

   As far as possible one should try to avoid shifting large amounts
   of data between processes.

   It is probably best to stick to using queues or pipes for
   communication between processes rather than using the lower level
   synchronization primitives.

Picklability

   Ensure that the arguments to the methods of proxies are picklable.

Thread safety of proxies

   Do not use a proxy object from more than one thread unless you
   protect it with a lock.

   (There is never a problem with different processes using the *same*
   proxy.)

Joining zombie processes

   On POSIX when a process finishes but has not been joined it becomes
   a zombie. There should never be very many because each time a new
   process starts (or "active_children()" is called) all completed
   processes which have not yet been joined will be joined.  Also
   calling a finished process's "Process.is_alive" will join the
   process.  Even so it is probably good practice to explicitly join
   all the processes that you start.

Better to inherit than pickle/unpickle

   When using the *spawn* or *forkserver* start methods many types
   from "multiprocessing" need to be picklable so that child processes
   can use them.  However, one should generally avoid sending shared
   objects to other processes using pipes or queues. Instead you
   should arrange the program so that a process which needs access to
   a shared resource created elsewhere can inherit it from an ancestor
   process.

Avoid terminating processes

   Using the "Process.terminate" method to stop a process is liable to
   cause any shared resources (such as locks, semaphores, pipes and
   queues) currently being used by the process to become broken or
   unavailable to other processes.

   Therefore it is probably best to only consider using
   "Process.terminate" on processes which never use any shared
   resources.

Joining processes that use queues

   Bear in mind that a process that has put items in a queue will wait
   before terminating until all the buffered items are fed by the
   "feeder" thread to the underlying pipe.  (The child process can
   call the "Queue.cancel_join_thread" method of the queue to avoid
   this behaviour.)

   This means that whenever you use a queue you need to make sure that
   all items which have been put on the queue will eventually be
   removed before the process is joined.  Otherwise you cannot be sure
   that processes which have put items on the queue will terminate.
   Remember also that non-daemonic processes will be joined
   automatically.

   An example which will deadlock is the following:

      from multiprocessing import Process, Queue

      def f(q):
          q.put('X' * 1000000)

      if __name__ == '__main__':
          queue = Queue()
          p = Process(target=f, args=(queue,))
          p.start()
          p.join()                    # this deadlocks
          obj = queue.get()

   A fix here would be to swap the last two lines (or simply remove
   the "p.join()" line).

Explicitly pass resources to child processes

   On POSIX using the *fork* start method, a child process can make
   use of a shared resource created in a parent process using a global
   resource.  However, it is better to pass the object as an argument
   to the constructor for the child process.

   Apart from making the code (potentially) compatible with Windows
   and the other start methods this also ensures that as long as the
   child process is still alive the object will not be garbage
   collected in the parent process.  This might be important if some
   resource is freed when the object is garbage collected in the
   parent process.

   So for instance

      from multiprocessing import Process, Lock

      def f():
          ... do something using "lock" ...

      if __name__ == '__main__':
          lock = Lock()
          for i in range(10):
              Process(target=f).start()

   should be rewritten as

      from multiprocessing import Process, Lock

      def f(l):
          ... do something using "l" ...

      if __name__ == '__main__':
          lock = Lock()
          for i in range(10):
              Process(target=f, args=(lock,)).start()

Beware of replacing "sys.stdin" with a "file like object"

   "multiprocessing" originally unconditionally called:

      os.close(sys.stdin.fileno())

   in the "multiprocessing.Process._bootstrap()" method --- this
   resulted in issues with processes-in-processes. This has been
   changed to:

      sys.stdin.close()
      sys.stdin = open(os.open(os.devnull, os.O_RDONLY), closefd=False)

   Which solves the fundamental issue of processes colliding with each
   other resulting in a bad file descriptor error, but introduces a
   potential danger to applications which replace "sys.stdin()" with a
   "file-like object" with output buffering.  This danger is that if
   multiple processes call "close()" on this file-like object, it
   could result in the same data being flushed to the object multiple
   times, resulting in corruption.

   If you write a file-like object and implement your own caching, you
   can make it fork-safe by storing the pid whenever you append to the
   cache, and discarding the cache when the pid changes. For example:

      @property
      def cache(self):
          pid = os.getpid()
          if pid != self._pid:
              self._pid = pid
              self._cache = []
          return self._cache

   For more information, see bpo-5155, bpo-5313 and bpo-5331


The *spawn* and *forkserver* start methods
------------------------------------------

There are a few extra restrictions which don't apply to the *fork*
start method.

More picklability

   Ensure that all arguments to "Process" are picklable.  Also, if you
   subclass "Process.__init__", you must make sure that instances will
   be picklable when the "Process.start" method is called.

Global variables

   Bear in mind that if code run in a child process tries to access a
   global variable, then the value it sees (if any) may not be the
   same as the value in the parent process at the time that
   "Process.start" was called.

   However, global variables which are just module level constants
   cause no problems.

Safe importing of main module

   Make sure that the main module can be safely imported by a new
   Python interpreter without causing unintended side effects (such as
   starting a new process).

   For example, using the *spawn* or *forkserver* start method running
   the following module would fail with a "RuntimeError":

      from multiprocessing import Process

      def foo():
          print('hello')

      p = Process(target=foo)
      p.start()

   Instead one should protect the "entry point" of the program by
   using "if __name__ == '__main__':" as follows:

      from multiprocessing import Process, freeze_support, set_start_method

      def foo():
          print('hello')

      if __name__ == '__main__':
          freeze_support()
          set_start_method('spawn')
          p = Process(target=foo)
          p.start()

   (The "freeze_support()" line can be omitted if the program will be
   run normally instead of frozen.)

   This allows the newly spawned Python interpreter to safely import
   the module and then run the module's "foo()" function.

   Similar restrictions apply if a pool or manager is created in the
   main module.


Exemplos
========

Demonstration of how to create and use customized managers and
proxies:

   from multiprocessing import freeze_support
   from multiprocessing.managers import BaseManager, BaseProxy
   import operator

   ##

   class Foo:
       def f(self):
           print('you called Foo.f()')
       def g(self):
           print('you called Foo.g()')
       def _h(self):
           print('you called Foo._h()')

   # A simple generator function
   def baz():
       for i in range(10):
           yield i*i

   # Proxy type for generator objects
   class GeneratorProxy(BaseProxy):
       _exposed_ = ['__next__']
       def __iter__(self):
           return self
       def __next__(self):
           return self._callmethod('__next__')

   # Function to return the operator module
   def get_operator_module():
       return operator

   ##

   class MyManager(BaseManager):
       pass

   # register the Foo class; make `f()` and `g()` accessible via proxy
   MyManager.register('Foo1', Foo)

   # register the Foo class; make `g()` and `_h()` accessible via proxy
   MyManager.register('Foo2', Foo, exposed=('g', '_h'))

   # register the generator function baz; use `GeneratorProxy` to make proxies
   MyManager.register('baz', baz, proxytype=GeneratorProxy)

   # register get_operator_module(); make public functions accessible via proxy
   MyManager.register('operator', get_operator_module)

   ##

   def test():
       manager = MyManager()
       manager.start()

       print('-' * 20)

       f1 = manager.Foo1()
       f1.f()
       f1.g()
       assert not hasattr(f1, '_h')
       assert sorted(f1._exposed_) == sorted(['f', 'g'])

       print('-' * 20)

       f2 = manager.Foo2()
       f2.g()
       f2._h()
       assert not hasattr(f2, 'f')
       assert sorted(f2._exposed_) == sorted(['g', '_h'])

       print('-' * 20)

       it = manager.baz()
       for i in it:
           print('<%d>' % i, end=' ')
       print()

       print('-' * 20)

       op = manager.operator()
       print('op.add(23, 45) =', op.add(23, 45))
       print('op.pow(2, 94) =', op.pow(2, 94))
       print('op._exposed_ =', op._exposed_)

   ##

   if __name__ == '__main__':
       freeze_support()
       test()

Using "Pool":

   import multiprocessing
   import time
   import random
   import sys

   #
   # Functions used by test code
   #

   def calculate(func, args):
       result = func(*args)
       return '%s says that %s%s = %s' % (
           multiprocessing.current_process().name,
           func.__name__, args, result
           )

   def calculatestar(args):
       return calculate(*args)

   def mul(a, b):
       time.sleep(0.5 * random.random())
       return a * b

   def plus(a, b):
       time.sleep(0.5 * random.random())
       return a + b

   def f(x):
       return 1.0 / (x - 5.0)

   def pow3(x):
       return x ** 3

   def noop(x):
       pass

   #
   # Test code
   #

   def test():
       PROCESSES = 4
       print('Creating pool with %d processes\n' % PROCESSES)

       with multiprocessing.Pool(PROCESSES) as pool:
           #
           # Tests
           #

           TASKS = [(mul, (i, 7)) for i in range(10)] + \
                   [(plus, (i, 8)) for i in range(10)]

           results = [pool.apply_async(calculate, t) for t in TASKS]
           imap_it = pool.imap(calculatestar, TASKS)
           imap_unordered_it = pool.imap_unordered(calculatestar, TASKS)

           print('Ordered results using pool.apply_async():')
           for r in results:
               print('\t', r.get())
           print()

           print('Ordered results using pool.imap():')
           for x in imap_it:
               print('\t', x)
           print()

           print('Unordered results using pool.imap_unordered():')
           for x in imap_unordered_it:
               print('\t', x)
           print()

           print('Ordered results using pool.map() --- will block till complete:')
           for x in pool.map(calculatestar, TASKS):
               print('\t', x)
           print()

           #
           # Test error handling
           #

           print('Testing error handling:')

           try:
               print(pool.apply(f, (5,)))
           except ZeroDivisionError:
               print('\tGot ZeroDivisionError as expected from pool.apply()')
           else:
               raise AssertionError('expected ZeroDivisionError')

           try:
               print(pool.map(f, list(range(10))))
           except ZeroDivisionError:
               print('\tGot ZeroDivisionError as expected from pool.map()')
           else:
               raise AssertionError('expected ZeroDivisionError')

           try:
               print(list(pool.imap(f, list(range(10)))))
           except ZeroDivisionError:
               print('\tGot ZeroDivisionError as expected from list(pool.imap())')
           else:
               raise AssertionError('expected ZeroDivisionError')

           it = pool.imap(f, list(range(10)))
           for i in range(10):
               try:
                   x = next(it)
               except ZeroDivisionError:
                   if i == 5:
                       pass
               except StopIteration:
                   break
               else:
                   if i == 5:
                       raise AssertionError('expected ZeroDivisionError')

           assert i == 9
           print('\tGot ZeroDivisionError as expected from IMapIterator.next()')
           print()

           #
           # Testing timeouts
           #

           print('Testing ApplyResult.get() with timeout:', end=' ')
           res = pool.apply_async(calculate, TASKS[0])
           while 1:
               sys.stdout.flush()
               try:
                   sys.stdout.write('\n\t%s' % res.get(0.02))
                   break
               except multiprocessing.TimeoutError:
                   sys.stdout.write('.')
           print()
           print()

           print('Testing IMapIterator.next() with timeout:', end=' ')
           it = pool.imap(calculatestar, TASKS)
           while 1:
               sys.stdout.flush()
               try:
                   sys.stdout.write('\n\t%s' % it.next(0.02))
               except StopIteration:
                   break
               except multiprocessing.TimeoutError:
                   sys.stdout.write('.')
           print()
           print()


   if __name__ == '__main__':
       multiprocessing.freeze_support()
       test()

An example showing how to use queues to feed tasks to a collection of
worker processes and collect the results:

   import time
   import random

   from multiprocessing import Process, Queue, current_process, freeze_support

   #
   # Function run by worker processes
   #

   def worker(input, output):
       for func, args in iter(input.get, 'STOP'):
           result = calculate(func, args)
           output.put(result)

   #
   # Function used to calculate result
   #

   def calculate(func, args):
       result = func(*args)
       return '%s says that %s%s = %s' % \
           (current_process().name, func.__name__, args, result)

   #
   # Functions referenced by tasks
   #

   def mul(a, b):
       time.sleep(0.5*random.random())
       return a * b

   def plus(a, b):
       time.sleep(0.5*random.random())
       return a + b

   #
   #
   #

   def test():
       NUMBER_OF_PROCESSES = 4
       TASKS1 = [(mul, (i, 7)) for i in range(20)]
       TASKS2 = [(plus, (i, 8)) for i in range(10)]

       # Create queues
       task_queue = Queue()
       done_queue = Queue()

       # Submit tasks
       for task in TASKS1:
           task_queue.put(task)

       # Start worker processes
       for i in range(NUMBER_OF_PROCESSES):
           Process(target=worker, args=(task_queue, done_queue)).start()

       # Get and print results
       print('Unordered results:')
       for i in range(len(TASKS1)):
           print('\t', done_queue.get())

       # Add more tasks using `put()`
       for task in TASKS2:
           task_queue.put(task)

       # Get and print some more results
       for i in range(len(TASKS2)):
           print('\t', done_queue.get())

       # Tell child processes to stop
       for i in range(NUMBER_OF_PROCESSES):
           task_queue.put('STOP')


   if __name__ == '__main__':
       freeze_support()
       test()
