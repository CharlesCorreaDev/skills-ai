"sched" --- Agendador de eventos
********************************

**Código-fonte:** Lib/sched.py

======================================================================

O módulo "sched" define uma classe que implementa um agendador de
eventos de uso geral:

class sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)

   A classe "scheduler" define uma interface genérica para agendar
   eventos. Ela precisa de duas funções para lidar com o "mundo
   externo" --- *timefunc* deve ser chamável sem argumentos e retornar
   um número (o "tempo", em quaisquer unidades). A função *delayfunc*
   deve ser chamável com um argumento, compatível com a saída de
   *timefunc*, e deve atrasar a mesma quantidade de unidades de tempo.
   *delayfunc* também será chamada com o argumento "0" após a execução
   de cada evento para permitir que outras threads executem em
   aplicações multithread.

   Alterado na versão 3.3: Os parâmetros *timefunc* e *delayfunc* são
   opcionais.

   Alterado na versão 3.3: A classe "scheduler" pode ser usada com
   segurança em ambientes multithread.

Exemplo:

   >>> import sched, time
   >>> s = sched.scheduler(time.time, time.sleep)
   >>> def print_time(a='default'):
   ...     print("From print_time", time.time(), a)
   ...
   >>> def print_some_times():
   ...     print(time.time())
   ...     s.enter(10, 1, print_time)
   ...     s.enter(5, 2, print_time, argument=('positional',))
   ...     # apesar de ter prioridade mais alta, 'keyword' é executado depois de 'positional', pois enter() é relativo
   ...     s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
   ...     s.enterabs(1_650_000_000, 10, print_time, argument=("first enterabs",))
   ...     s.enterabs(1_650_000_000, 5, print_time, argument=("second enterabs",))
   ...     s.run()
   ...     print(time.time())
   ...
   >>> print_some_times()
   1652342830.3640375
   From print_time 1652342830.3642538 second enterabs
   From print_time 1652342830.3643398 first enterabs
   From print_time 1652342835.3694863 positional
   From print_time 1652342835.3696074 keyword
   From print_time 1652342840.369612 default
   1652342840.3697174


Objetos Scheduler
=================

As instâncias "scheduler" têm os seguintes métodos e atributos:

scheduler.enterabs(time, priority, action, argument=(), kwargs={})

   Agenda um novo evento. O argumento *time* deve ser um tipo numérico
   compatível com o valor de retorno da função *timefunc* passada ao
   construtor. Eventos agendados para o mesmo *time* serão executados
   na ordem de sua prioridade *priority*. Um número menor representa
   uma prioridade maior.

   Executa o evento significa executar "action(*argument, **kwargs)".
   *argument* é uma sequência que contém os argumentos posicionais
   para *action*. *kwargs* é um dicionário que contém os argumentos
   nomeados para *action*.

   O valor de retorno é um evento que pode ser usado para cancelamento
   posterior do evento (veja "cancel()").

   Alterado na versão 3.3: o parâmetro *argument* é opcional.

   Alterado na versão 3.3: o parâmetro *kwargs* foi adicionado.

scheduler.enter(delay, priority, action, argument=(), kwargs={})

   Agenda um evento para atrasar *delay* mais unidades de tempo. Além
   do tempo relativo, os outros argumentos, o efeito e o valor de
   retorno são os mesmos de "enterabs()".

   Alterado na versão 3.3: o parâmetro *argument* é opcional.

   Alterado na versão 3.3: o parâmetro *kwargs* foi adicionado.

scheduler.cancel(event)

   Remove o evento da fila. Se *event* não for um evento atualmente na
   fila, este método levantará uma "ValueError".

scheduler.empty()

   Retorna "True" se a fila de eventos estiver vazia.

scheduler.run(blocking=True)

   Executa todos os eventos agendados. Este método aguardará (usando a
   função *delayfunc* passada ao construtor) o próximo evento, depois
   o executará e assim por diante até que não haja mais eventos
   agendados.

   Se *blocking* for falso, executa imediatamente todos os eventos na
   fila que tenham um valor de tempo menor ou igual ao valor atual de
   *timefunc* (se houver) e retorna a diferença entre o valor atual de
   *timefunc* e o valor de tempo do próximo evento agendado na fila de
   eventos do agendador. Se a fila estiver vazia, retorna "None".

   Tanto *action* quanto *delayfunc* podem levantar uma exceção. Em
   ambos os casos, o agendador manterá um estado consistente e
   propagará a exceção. Se uma exceção for gerada por *action*, o
   evento não será tentado em chamadas futuras para "run()".

   Se uma sequência de eventos demorar mais para ser executada do que
   o tempo disponível antes do próximo evento, o agendador
   simplesmente ficará para trás. Nenhum evento será descartado; o
   código de chamada é responsável por cancelar eventos que não são
   mais pertinentes.

   Alterado na versão 3.3: O argumento *blocking* foi adicionado.

scheduler.queue

   Atributo somente leitura que retorna uma lista de eventos futuros
   na ordem em que serão executados. Cada evento é exibido como uma
   *tupla nomeada* com os seguintes campos: time, priority, action,
   argument, kwargs.
