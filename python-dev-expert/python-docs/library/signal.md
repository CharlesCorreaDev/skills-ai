"signal" --- Define manipuladores para eventos assíncronos
**********************************************************

**Código-fonte:** Lib/signal.py

======================================================================

Este módulo fornece mecanismos para usar manipuladores de sinal em
Python.


Regras gerais
=============

A função "signal.signal()" permite definir manipuladores
personalizados a serem executados quando um sinal é recebido. Um
pequeno número de manipuladores padrão são instalados: "SIGPIPE" é
ignorado (então erros de gravação em encadeamentos e sockets podem ser
relatados como exceções comuns do Python) e "SIGINT" é traduzido em
uma exceção "KeyboardInterrupt" se o processo pai não a tiver
alterado.

Um manipulador para um sinal específico, uma vez definido, permanece
instalado até ser explicitamente redefinido (o Python emula a
interface de estilo BSD independentemente da implementação
subjacente), com exceção do manipulador para "SIGCHLD", que segue a
implementação subjacente.

Em plataformas WebAssembly, os sinais são emulados e, portanto, se
comportam de forma diferente. Várias funções e sinais não estão
disponíveis nessas plataformas.


Execução de manipuladores de sinais Python
------------------------------------------

A Python signal handler does not get executed inside the low-level (C)
signal handler.  Instead, the low-level signal handler sets a flag
which tells the *virtual machine* to execute the corresponding Python
signal handler at a later point (for example, at the next *bytecode*
instruction). This has consequences:

* Faz pouco sentido capturar erros síncronos como "SIGFPE" ou
  "SIGSEGV" que são causados por uma operação inválida no código C. O
  Python retornará do manipulador de sinais para o código C, o que
  provavelmente levantará o mesmo sinal novamente, fazendo com que o
  Python aparentemente trave. Do Python 3.3 em diante, você pode usar
  o módulo "faulthandler" para relatar erros síncronos.

* Um cálculo de longa duração implementado puramente em C (como
  correspondência de expressão regular em um grande corpo de texto)
  pode ser executado ininterruptamente por um período de tempo
  arbitrário, independentemente de quaisquer sinais recebidos. Os
  manipuladores de sinal do Python serão chamados quando o cálculo
  terminar.

* Se o manipulador levantar uma exceção, ela será levantada "do nada"
  na thread principal. Veja a nota abaixo para uma discussão.


Sinais e threads
----------------

Os manipuladores de sinais Python são sempre executados na thread
principal do Python do interpretador principal, mesmo se o sinal foi
recebido em outra thread. Isso significa que os sinais não podem ser
usados como um meio de comunicação entre threads. Você pode usar as
primitivas de sincronização do módulo "threading" em vez disso.

Além disso, somente a thread principal do interpretador principal tem
permissão para definir um novo manipulador de sinal.

Aviso:

  Synchronization primitives such as "threading.Lock" should not be
  used within signal handlers.  Doing so can lead to unexpected
  deadlocks.


Conteúdo do módulo
==================

Alterado na versão 3.5: As constantes relacionadas a sinal (SIG*),
manipulador ("SIG_DFL", "SIG_IGN") e sigmask ("SIG_BLOCK",
"SIG_UNBLOCK", "SIG_SETMASK") listadas abaixo foram transformadas em
"enums" ("Signals", "Handlers" e "Sigmasks" respectivamente). As
funções "getsignal()", "pthread_sigmask()", "sigpending()" e
"sigwait()" retornam "enums" legíveis por humanos como objetos
"Signals".

O módulo de sinal define três enumerações:

class signal.Signals

   Coleção de "enum.IntEnum" de constantes SIG* e constantes CTRL_*.

   Adicionado na versão 3.5.

class signal.Handlers

   "enum.IntEnum" collection of the constants "SIG_DFL" and "SIG_IGN".

   Adicionado na versão 3.5.

class signal.Sigmasks

   "enum.IntEnum" collection of the constants "SIG_BLOCK",
   "SIG_UNBLOCK" and "SIG_SETMASK".

   Disponibilidade: Unix.

   Veja a página man *sigprocmask(2)* e *pthread_sigmask(3)* para mais
   informações.

   Adicionado na versão 3.5.

The variables defined in the "signal" module are:

signal.SIG_DFL

   Esta é uma das duas opções de manipulação de sinal padrão; ela
   simplesmente executará a função padrão para o sinal. Por exemplo,
   na maioria dos sistemas, a ação padrão para "SIGQUIT" é despejar o
   núcleo e sair, enquanto a ação padrão para "SIGCHLD" é simplesmente
   ignorá-lo.

signal.SIG_IGN

   Este é outro manipulador de sinal padrão, que simplesmente ignorará
   o sinal fornecido.

signal.SIGABRT

   Sinal de abortar de *abort(3)*.

signal.SIGALRM

   Sinal do temporizador de *alarm(2)*.

   Disponibilidade: Unix.

signal.SIGBREAK

   Interrupção do teclado (CTRL + BREAK).

   Disponibilidade: Windows.

signal.SIGBUS

   Erro de barramento (acesso incorreto à memória).

   Disponibilidade: Unix.

signal.SIGCHLD

   Processo filho interrompido ou encerrado.

   Disponibilidade: Unix.

signal.SIGCLD

   Apelido para "SIGCHLD".

   Disponibilidade: not macOS.

signal.SIGCONT

   Continua o processo se ele estiver parado no momento

   Disponibilidade: Unix.

signal.SIGFPE

   Exceção de ponto flutuante. Por exemplo, divisão por zero.

   Ver também:

     "ZeroDivisionError" é levatanda quando o segundo argumento de uma
     operação de divisão ou módulo é zero.

signal.SIGHUP

   Travamento detectado no terminal de controle ou morte do processo
   de controle.

   Disponibilidade: Unix.

signal.SIGILL

   Instrução ilegal.

signal.SIGINT

   Interrupção do teclado (CTRL + C).

   A ação padrão é levantar "KeyboardInterrupt".

signal.SIGKILL

   Sinal para encerrar forçadamente.

   Ele não pode ser capturado, bloqueado ou ignorado.

   Disponibilidade: Unix.

signal.SIGPIPE

   Encadeamento quebrado: escreve no encadeamento sem leitores.

   A ação padrão é ignorar o sinal.

   Disponibilidade: Unix.

signal.SIGPROF

   Temporizador de perfilamento expirado.

   Disponibilidade: Unix.

signal.SIGQUIT

   Sinal de saída do terminal.

   Disponibilidade: Unix.

signal.SIGSEGV

   Falha de segmentação: referência de memória inválida.

signal.SIGSTOP

   Para a execução (não pode ser capturado ou ignorado).

   Disponibilidade: Unix.

signal.SIGSTKFLT

   Falha de pilha no coprocessador. O kernel Linux não levanta esse
   sinal: ele só pode ser emitido no espaço do usuário.

   Disponibilidade: Linux.

   Em arquiteturas onde o sinal está disponível. Veja a página man
   *signal(7)* para mais informações.

   Adicionado na versão 3.11.

signal.SIGTERM

   Sinal de encerramento.

signal.SIGUSR1

   Sinal definido pelo usuário 1.

   Disponibilidade: Unix.

signal.SIGUSR2

   Sinal definido pelo usuário 2.

   Disponibilidade: Unix.

signal.SIGVTALRM

   Temporizador virtual expirou.

   Disponibilidade: Unix.

signal.SIGWINCH

   Sinal de redimensionamento do Windows.

   Disponibilidade: Unix.

signal.SIGXCPU

   Limite de tempo da CPU excedido.

   Disponibilidade: Unix.

SIG*

   Todos os números de sinal são definidos simbolicamente. Por
   exemplo, o sinal de desligamento é definido como "signal.SIGHUP";
   os nomes das variáveis são idênticos aos usados em programas C,
   como encontrados em "<signal.h>". A página man do Unix para
   '"signal"' lista os sinais existentes (em alguns sistemas, é
   *signal(2)*, em outros, a lista está em *signal(7)*). Observe que
   nem todos os sistemas definem o mesmo conjunto de nomes de sinais;
   apenas os nomes definidos pelo sistema são definidos por este
   módulo.

signal.CTRL_C_EVENT

   O sinal correspondente ao evento de pressionamento de tecla
   "Ctrl"+"C". Este sinal só pode ser usado com "os.kill()".

   Disponibilidade: Windows.

   Adicionado na versão 3.2.

signal.CTRL_BREAK_EVENT

   O sinal correspondente ao evento de pressionamento de tecla
   "Ctrl"+"Break". Este sinal só pode ser usado com "os.kill()".

   Disponibilidade: Windows.

   Adicionado na versão 3.2.

signal.NSIG

   Um a mais que o número do sinal mais alto. Use "valid_signals()"
   para obter números de sinais válidos.

signal.ITIMER_REAL

   Diminui o intervalo do temporizador em tempo real e entrega
   "SIGALRM" ao expirar.

signal.ITIMER_VIRTUAL

   Diminui o intervalo do temporizador somente quando o processo está
   em execução e entrega SIGVTALRM após a expiração.

signal.ITIMER_PROF

   Diminui o temporizador de intervalo tanto quando o processo é
   executado quanto quando o sistema está executando em nome do
   processo. Juntamente com o ITIMER_VIRTUAL, este temporizador é
   geralmente usado para criar um perfil do tempo gasto pelo
   aplicativo nos espaços do usuário e do kernel. O SIGPROF é
   fornecido após a expiração.

signal.SIG_BLOCK

   Um possível valor para o parâmetro *how* para "pthread_sigmask()"
   indicando que os sinais devem ser bloqueados.

   Adicionado na versão 3.3.

signal.SIG_UNBLOCK

   Um possível valor para o parâmetro *how* para "pthread_sigmask()"
   indicando que os sinais devem ser desbloqueados.

   Adicionado na versão 3.3.

signal.SIG_SETMASK

   Um possível valor para o parâmetro *how* para "pthread_sigmask()"
   indicando que a máscara de sinal deve ser substituída.

   Adicionado na versão 3.3.

The "signal" module defines one exception:

exception signal.ItimerError

   Levantada para sinalizar um erro da implementação subjacente de
   "setitimer()" ou "getitimer()". Espere este erro se um temporizador
   de intervalo inválido ou um tempo negativo for passado para
   "setitimer()". Este erro é um subtipo de "OSError".

   Adicionado na versão 3.3: Este erro costumava ser um subtipo de
   "IOError", que agora é um apelido de "OSError".

The "signal" module defines the following functions:

signal.alarm(time)

   Se *time* for diferente de zero, esta função solicita que um sinal
   "SIGALRM" seja enviado ao processo em *time* segundos. Qualquer
   alarme previamente agendado será cancelado (apenas um alarme pode
   ser agendado por vez). O valor retornado será o número de segundos
   antes de qualquer alarme previamente configurado ter sido emitido.
   Se *time* for zero, nenhum alarme será agendado e qualquer alarme
   agendado será cancelado. Se o valor retornado for zero, nenhum
   alarme será agendado no momento.

   Disponibilidade: Unix.

   Veja a página man *alarm(2)* para mais informações.

signal.getsignal(signalnum)

   Retorna o manipulador de sinal atual para o sinal *signalnum*. O
   valor retornado pode ser um objeto Python invocável ou um dos
   valores especiais "signal.SIG_IGN", "signal.SIG_DFL" ou "None".
   Aqui, "signal.SIG_IGN" significa que o sinal foi ignorado
   anteriormente, "signal.SIG_DFL" significa que a maneira padrão de
   manipular o sinal estava em uso anteriormente e "None" significa
   que o manipulador de sinal anterior não foi instalado a partir do
   Python.

signal.strsignal(signalnum)

   Retorna a descrição do sinal *signalnum*, como "Interrupt" para
   "SIGINT". Retorna "None" se *signalnum* não tiver descrição.
   Levanta "ValueError" se *signalnum* for inválido.

   Adicionado na versão 3.8.

signal.valid_signals()

   Retorna o conjunto de números de sinais válidos nesta plataforma.
   Pode ser menor que "range(1, NSIG)" se alguns sinais forem
   reservados pelo sistema para uso interno.

   Adicionado na versão 3.8.

signal.pause()

   Faz o processo hibernar até que um sinal seja recebido; o
   manipulador apropriado será então chamado. Não retorna nada.

   Disponibilidade: Unix.

   Veja a página man *signal(2)* para mais informações.

   veja também "sigwait()", "sigwaitinfo()", "sigtimedwait()" e
   "sigpending()".

signal.raise_signal(signum)

   Envia um sinal para o processo de chamada. Não retorna nada.

   Adicionado na versão 3.8.

signal.pidfd_send_signal(pidfd, sig, siginfo=None, flags=0)

   Envia o sinal *sig* para o processo referenciado pelo descritor de
   arquivo *pidfd*. Atualmente, o Python não suporta o parâmetro
   *siginfo*; ele deve ser "None". O argumento *flags* é fornecido
   para futuras extensões; nenhum valor de sinalizador está definido
   no momento.

   Veja a página man *pidfd_send_signal(2)* para mais informações.

   Disponibilidade: Linux >= 5.1, Android >= "build-time" API level 31

   Adicionado na versão 3.9.

signal.pthread_kill(thread_id, signalnum)

   Envia o sinal *signalnum* para a thread *thread_id*, outra thread
   no mesmo processo que a chamadora. A thread alvo pode estar
   executando qualquer código (Python ou não). No entanto, se a thread
   alvo estiver executando o interpretador Python, os manipuladores de
   sinal Python serão executados pela thread principal do
   interpretador principal. Portanto, o único objetivo de enviar um
   sinal para uma thread Python específica seria forçar uma chamada de
   sistema em execução a falhar com "InterruptedError".

   Utilize a "threading.get_ident()" ou o atributo "ident" dos objetos
   "threading.Thread" para obter um valor adequado para *thread_id*.

   Se *signalnum* for 0, nenhum sinal será enviado, mas a verificação
   de erros ainda será realizada; isso pode ser usado para verificar
   se a thread de destino ainda está em execução.

   Levanta um evento de auditoria "signal.pthread_kill" com os
   argumentos "thread_id", "signalnum".

   Disponibilidade: Unix.

   Veja a página man *pthread_kill(3)* para mais informações.

   Veja também "os.kill()".

   Adicionado na versão 3.3.

signal.pthread_sigmask(how, mask)

   Busca e/ou altera a máscara de sinal da thread chamadora. A máscara
   de sinal é o conjunto de sinais cuja entrega está atualmente
   bloqueada para o chamador. Retorna a máscara de sinal antiga como
   um conjunto de sinais.

   O comportamento da chamada depende do valor de *how*, como segue.

   * "SIG_BLOCK": O conjunto de sinais bloqueados é a união do
     conjunto atual e do argumento *mask*.

   * "SIG_UNBLOCK": Os sinais em *mask* são removidos do conjunto
     atual de sinais bloqueados. É permitido tentar desbloquear um
     sinal que não esteja bloqueado.

   * "SIG_SETMASK": O conjunto de sinais bloqueados é definido como o
     argumento *mask*.

   *mask* é um conjunto de números de sinais (ex.: {"signal.SIGINT",
   "signal.SIGTERM"}). Use "valid_signals()" para uma máscara
   completa, incluindo todos os sinais.

   Por exemplo, "signal.pthread_sigmask(signal.SIG_BLOCK, [])" lê a
   máscara de sinal da thread de chamada.

   "SIGKILL" e "SIGSTOP" não podem ser bloqueados.

   Disponibilidade: Unix.

   Veja a página man *sigprocmask(2)* e *pthread_sigmask(3)* para mais
   informações.

   Veja também "pause()", "sigpending()" e "sigwait()".

   Adicionado na versão 3.3.

signal.setitimer(which, seconds, interval=0)

   Sets given interval timer (one of "signal.ITIMER_REAL",
   "signal.ITIMER_VIRTUAL" or "signal.ITIMER_PROF") specified by
   *which* to fire after *seconds* (rounded up to microseconds,
   different from "alarm()") and after that every *interval* seconds
   (if *interval* is non-zero). The interval timer specified by
   *which* can be cleared by setting *seconds* to zero.

   Quando um temporizador de intervalo dispara, um sinal é enviado ao
   processo. O sinal enviado depende do temporizador utilizado;
   "signal.ITIMER_REAL" enviará "SIGALRM", "signal.ITIMER_VIRTUAL"
   enviará "SIGVTALRM" e "signal.ITIMER_PROF" enviará "SIGPROF".

   The old values are returned as a two-tuple of floats: ("delay",
   "interval").

   Tentar passar um intervalo de tempo inválido causará uma
   "ItimerError".

   Disponibilidade: Unix.

   Alterado na versão 3.15: Accepts any real numbers as *seconds* and
   *interval*, not only integers or floats.

signal.getitimer(which)

   Retorna o valor atual de um intervalo de tempo especificado por
   *which*.

   Disponibilidade: Unix.

signal.set_wakeup_fd(fd, *, warn_on_full_buffer=True)

   Define o descritor de arquivo de ativação como *fd*. Quando um
   sinal para o qual seu programa registrou um manipulador de sinais é
   recebido, o número do sinal é escrito como um único byte no fd. Se
   você não registrou um manipulador de sinais para os sinais de seu
   interesse, nada será escrito no fd de ativação. Isso pode ser usado
   por uma biblioteca para ativar uma chamada de poll ou seleção,
   permitindo que o sinal seja totalmente processado.

   O antigo fd de ativação é retornado (ou -1 se a ativação do
   descritor de arquivo não estava habilitada). Se *fd* for -1, a
   ativação do descritor de arquivo está desabilitada. Se não for -1,
   *fd* deve ser não bloqueante. Cabe à biblioteca remover quaisquer
   bytes de *fd* antes de chamar poll ou select novamente.

   Quando threads estão habilitadas, esta função só pode ser chamada
   da thread principal do interpretador principal; tentar chamá-la de
   outras threads levantará uma exceção "ValueError".

   Há duas maneiras comuns de usar esta função. Em ambas as
   abordagens, você usa o fd para despertar quando um sinal chega, mas
   elas diferem na forma como determinam *which* sinal ou sinais
   chegaram.

   Na primeira abordagem, lemos os dados do buffer do fd, e os valores
   dos bytes fornecem os números dos sinais. Isso é simples, mas em
   casos raros pode apresentar um problema: geralmente, o fd terá um
   espaço de buffer limitado e, se muitos sinais chegarem muito
   rápido, o buffer pode ficar cheio e alguns sinais podem ser
   perdidos. Se você usar essa abordagem, defina
   "warn_on_full_buffer=True", o que pelo menos fará com que um aviso
   seja impresso no stderr quando os sinais forem perdidos.

   Na segunda abordagem, usamos o fd de ativação *apenas* para
   ativações e ignoramos os valores de bytes reais. Nesse caso, tudo o
   que importa é se o buffer do fd está vazio ou não; um buffer cheio
   não indica nenhum problema. Se você usar essa abordagem, defina
   "warn_on_full_buffer=False" para que seus usuários não sejam
   confundidos por mensagens de aviso falsas.

   Alterado na versão 3.5: No Windows, a função agora também suporta
   manipuladores de socket.

   Alterado na versão 3.7: Adiciona o parâmetro "warn_on_full_buffer".

signal.siginterrupt(signalnum, flag)

   Altera o comportamento de reinicialização de chamadas de sistema:
   se *flag* for "False", as chamadas de sistema serão reiniciadas
   quando interrompidas pelo sinal *signalnum*; caso contrário, as
   chamadas de sistema serão interrompidas. Não retorna nada.

   Disponibilidade: Unix.

   Veja a página man *siginterrupt(3)* para mais informações.

   Note that installing a signal handler with "signal()" will reset
   the restart behaviour to interruptible by implicitly calling
   "siginterrupt()" with a true *flag* value for the given signal.

signal.signal(signalnum, handler)

   Define o manipulador do sinal *signalnum* para a função *handler*.
   *handler* pode ser um objeto Python invocável que recebe dois
   argumentos (veja abaixo), ou um dos valores especiais
   "signal.SIG_IGN" ou "signal.SIG_DFL". O manipulador de sinal
   anterior será retornado (veja a descrição de "getsignal()" acima).
   (Consulte a página man do Unix *signal(2)* para mais informações.)

   Quando threads estão habilitadas, esta função só pode ser chamada
   da thread principal do interpretador principal; tentar chamá-la de
   outras threads levantará uma exceção "ValueError".

   O *handler* é chamado com dois argumentos: o número do sinal e o
   quadro de pilha atual ("None" ou um objeto quadro; para uma
   descrição dos objetos quadro, consulte a descrição na hierarquia de
   tipo ou consulte as descrições de atributo no módulo "inspect").

   On Windows, "signal()" can only be called with "SIGABRT", "SIGFPE",
   "SIGILL", "SIGINT", "SIGSEGV", "SIGTERM", or "SIGBREAK". A
   "ValueError" will be raised in any other case. Note that not all
   systems define the same set of signal names; an "AttributeError"
   will be raised if a signal name is not defined as "SIG*" module
   level constant.

signal.sigpending()

   Examine o conjunto de sinais pendentes para entrega ao thread de
   chamada (ou seja, os sinais que foram gerados enquanto bloqueados).
   Retorne o conjunto de sinais pendentes.

   Disponibilidade: Unix.

   Veja a página man *sigpending(2)* para mais informações.

   Veja também "pause()", "pthread_sigmask()" e "sigwait()".

   Adicionado na versão 3.3.

signal.sigwait(sigset)

   Suspende a execução do thread de chamada até a entrega de um dos
   sinais especificados no conjunto de sinais *sigset*. A função
   aceita o sinal (remove-o da lista de sinais pendentes) e retorna o
   número do sinal.

   Disponibilidade: Unix.

   Veja a página man *sigwait(3)* para mais informações.

   Veja também "pause()", "pthread_sigmask()", "sigpending()",
   "sigwaitinfo()" e "sigtimedwait()".

   Adicionado na versão 3.3.

signal.sigwaitinfo(sigset)

   Suspende a execução da thread chamadora até a entrega de um dos
   sinais especificados no conjunto de sinais *sigset*. A função
   aceita o sinal e o remove da lista de sinais pendentes. Se um dos
   sinais em *sigset* já estiver pendente para a thread chamadora, a
   função retornará imediatamente com informações sobre esse sinal. O
   manipulador de sinais não é chamado para o sinal entregue. A função
   levanta "InterruptedError" se for interrompida por um sinal que não
   esteja em *sigset*.

   O valor de retorno é um objeto que representa os dados contidos na
   estrutura de "siginfo_t", a saber: "si_signo", "si_code",
   "si_errno", "si_pid", "si_uid", "si_status", "si_band".

   Disponibilidade: Unix.

   Veja a página man *sigwaitinfo(2)* para mais informações.

   Veja também "pause()", "sigwait()" e "sigtimedwait()".

   Adicionado na versão 3.3.

   Alterado na versão 3.5: A função agora é tentada novamente se
   interrompida por um sinal que não esteja em *sigset* e o
   manipulador de sinal não levanta uma exceção (veja **PEP 475** para
   a justificativa).

signal.sigtimedwait(sigset, timeout)

   Semelhante a "sigwaitinfo()", mas recebe um argumento *timeout*
   adicional que especifica um tempo limite. Se *timeout* for
   especificado como "0", uma consulta será realizada. Retorna "None"
   se ocorrer um tempo limite.

   Disponibilidade: Unix.

   Veja a página man *sigtimedwait(2)* para mais informações.

   Veja também "pause()", "sigwait()" e "sigwaitinfo()".

   Adicionado na versão 3.3.

   Alterado na versão 3.5: A função agora é tentada novamente com o
   *timeout* recalculado se interrompida por um sinal que não esteja
   em *sigset* e o manipulador de sinal não levanta uma exceção (veja
   **PEP 475** para a justificativa).

   Alterado na versão 3.15: Accepts any real number as *timeout*, not
   only integer or float.


Exemplos
========

Aqui está um programa de exemplo mínimo. Ele usa a função "alarm()"
para limitar o tempo gasto esperando para abrir um arquivo; isso é
útil se o arquivo for para um dispositivo serial que pode não estar
ligado, o que normalmente faria com que o "os.open()" travasse
indefinidamente. A solução é definir um alarme de 5 segundos antes de
abrir o arquivo; se a operação demorar muito, o sinal de alarme será
enviado e o manipulador levantará uma exceção.

   import signal, os

   def handler(signum, frame):
       signame = signal.Signals(signum).name
       print(f'Signal handler called with signal {signame} ({signum})')
       raise OSError("Couldn't open device!")

   # Define o manipulador de sinal e um alarme de 5 segundos
   signal.signal(signal.SIGALRM, handler)
   signal.alarm(5)

   # Este open() pode travar indefinidamente
   fd = os.open('/dev/ttyS0', os.O_RDWR)

   signal.alarm(0)          # Desabilita o alarme


Nota sobre SIGPIPE
==================

Canalizar a saída do seu programa para ferramentas como *head(1)* fará
com que um sinal "SIGPIPE" seja enviado ao seu processo quando o
receptor da saída padrão fechar antes do tempo. Isso resulta em uma
exceção como "BrokenPipeError: [Errno 32] Broken pipe". Para lidar com
esse caso, envolva seu ponto de entrada para capturar essa exceção da
seguinte maneira:

   import os
   import sys

   def main():
       try:
           # simula uma saída grande (seu código substitui este loop)
           for x in range(10000):
               print("y")
           # limpa a saída aqui para forçar o acionamento do SIGPIPE
           # enquanto estiver dentro deste bloco try.
           sys.stdout.flush()
       except BrokenPipeError:
           # Python libera fluxos padrão na saída; redireciona a saída restante
           # para devnull para evitar outro BrokenPipeError no desligamento
           devnull = os.open(os.devnull, os.O_WRONLY)
           os.dup2(devnull, sys.stdout.fileno())
           sys.exit(1)  # Python exits with error code 1 on EPIPE

   if __name__ == '__main__':
       main()

Não defina a disposição de "SIGPIPE" como "SIG_DFL" para evitar
"BrokenPipeError". Isso faria com que seu programa encerrasse
inesperadamente sempre que qualquer conexão de soquete fosse
interrompida enquanto o programa ainda estivesse escrevendo nele.


Nota sobre manipuladores de sinais e exceções
=============================================

Se um manipulador de sinais levantar uma exceção, a exceção será
propagada para a thread principal e poderá ser levantada após qualquer
instrução *bytecode*. Mais notavelmente, uma "KeyboardInterrupt" pode
aparecer a qualquer momento durante a execução. A maioria dos códigos
Python, incluindo a biblioteca padrão, não pode ser robusta contra
isso, e, portanto, uma "KeyboardInterrupt" (ou qualquer outra exceção
resultante de um manipulador de sinais) pode, em raras ocasiões,
colocar o programa em um estado inesperado.

Para ilustrar esse problema, considere o seguinte código:

   class SpamContext:
       def __init__(self):
           self.lock = threading.Lock()

       def __enter__(self):
           # Se ocorrer KeyboardInterrupt aqui, está tudo bem
           self.lock.acquire()
           # Se KeyboardInterrupt ocorrer aqui, __exit__ não será chamado
           ...
           # KeyboardInterrupt pode ocorrer logo antes do retorno da função

       def __exit__(self, exc_type, exc_val, exc_tb):
           ...
           self.lock.release()

Para muitos programas, especialmente aqueles que simplesmente desejam
encerrar em "KeyboardInterrupt", isso não é um problema, mas
aplicações complexos ou que exigem alta confiabilidade devem evitar
levantar exceções de manipuladores de sinal. Eles também devem evitar
capturar "KeyboardInterrupt" como forma de encerrar o programa sem
problemas. Em vez disso, devem instalar seu próprio manipulador
"SIGINT". Abaixo está um exemplo de um servidor HTTP que evita
"KeyboardInterrupt":

   import signal
   import socket
   from selectors import DefaultSelector, EVENT_READ
   from http.server import HTTPServer, SimpleHTTPRequestHandler

   interrupt_read, interrupt_write = socket.socketpair()

   def handler(signum, frame):
       print('Signal handler called with signal', signum)
       interrupt_write.send(b'\0')
   signal.signal(signal.SIGINT, handler)

   def serve_forever(httpd):
       sel = DefaultSelector()
       sel.register(interrupt_read, EVENT_READ)
       sel.register(httpd, EVENT_READ)

       while True:
           for key, _ in sel.select():
               if key.fileobj == interrupt_read:
                   interrupt_read.recv(1)
                   return
               if key.fileobj == httpd:
                   httpd.handle_request()

   print("Serving on port 8000")
   httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
   serve_forever(httpd)
   print("Shutdown...")
