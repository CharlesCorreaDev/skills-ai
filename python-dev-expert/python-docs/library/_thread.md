"_thread"--- API de segmentação de baixo nível
**********************************************

======================================================================

Este módulo fornece primitivos de baixo nível para trabalhar com
vários threads (também chamados *processos leves* ou *tarefas*) ---
vários threads de controle compartilhando seu espaço de dados global.
Para sincronização, travas simples (também chamadas de *mutexes*,
*exclusão mútua* ou *semáforos binários*) são fornecidas. O módulo
"threading" fornece uma API de segmentação mais fácil de usar e de
nível mais alto, construída sobre este módulo.

Alterado na versão 3.7: Este módulo costumava ser opcional, agora está
sempre disponível.

Este módulo define as seguintes constantes e funções:

exception _thread.error

   Gerado em erros específicos de segmento.

   Alterado na versão 3.3: Agora este é um sinônimo da exceção
   embutida "RuntimeError".

_thread.start_new_thread(function, args[, kwargs])

   Começa uma nova thread e retorna seu identificador. A thread
   executa a função *function* com a lista de argumentos *args* (que
   deve ser uma tupla). O argumento opcional *kwargs* especifica um
   dicionário de argumentos nomeados.

   Quando a função retorna, a thread termina silenciosamente.

   Quando a função termina com uma exceção não processada,
   "sys.unraisablehook()" é chamada para lidar com a exceção. O
   atributo *object* do argumento do hook é *function*. Por padrão, um
   stack trace (situação da pilha de execução) é exibido e, em
   seguida, a thread termina (mas outras threads continuam a ser
   executadas).

   Quando a função gera uma exceção "SystemExit", ela é ignorada.

   Levanta um evento de auditoria "_thread.start_new_thread" com os
   argumentos "function", "args", "kwargs".

   Alterado na versão 3.8: "sys.unraisablehook()" agora é usada para
   tratar exceções não tratadas.

_thread.interrupt_main(signum=signal.SIGINT, /)

   Simula o efeito de um sinal chegando na thread principal. Uma
   thread pode usar esta função para interromper a thread principal,
   embora não haja garantia de que a interrupção ocorrerá
   imediatamente.

   Se fornecido, *signum* é o número do sinal a ser simulado. Se
   *signum* não for fornecido, "signal.SIGINT" será simulado.

   Se o sinal fornecido não for tratado pelo Python (o sinal foi
   definido como "signal.SIG_DFL" ou "signal.SIG_IGN"), esta função
   faz nada.

   Alterado na versão 3.10: O argumento *signum* é adicionado para
   personalizar o sinal de número.

   Nota:

     Isso não emite o sinal correspondente, mas agenda uma chamada
     para o tratador associado (se existir). Se você quer realmente
     emitir o sinal, use "signal.raise_signal()".

_thread.exit()

   Levanta a exceção "SystemExit". Quando não for detectada, a thread
   terminará silenciosamente.

_thread.allocate_lock()

   Retorna um novo objeto de trava. Métodos de trava são descritos
   abaixo. A trava é desativada inicialmente.

_thread.get_ident()

   Retorna o 'identificador de thread' da thread atual. Este é um
   número inteiro diferente de zero. Seu valor não tem significado
   direto; pretende-se que seja um cookie mágico para ser usado, por
   exemplo, para indexar um dicionário de dados específicos do thread.
   Identificadores de thread podem ser reciclados quando uma thread
   termina e outra é criada.

_thread.get_native_id()

   Retorna a ID de thread integral nativa da thread atual atribuída
   pelo kernel. Este é um número inteiro não negativo. Seu valor pode
   ser usado para identificar exclusivamente essa thread específica em
   todo o sistema (até que a thread termine, após o que o valor poderá
   ser reciclado pelo sistema operacional).

   Disponibilidade: Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD,
   AIX, DragonFlyBSD, GNU/kFreeBSD, Solaris.

   Adicionado na versão 3.8.

   Alterado na versão 3.13: Adicionado suporte a GNU/kFreeBSD.

   Alterado na versão 3.15: Adicionado suporte para Solaris.

_thread.stack_size([size])

   Retorna o tamanho da pilha de threads usado ao criar novas threads.
   O argumento opcional *size* especifica o tamanho da pilha a ser
   usado para threads criadas posteriormente e deve ser 0 (usar
   plataforma ou padrão configurado) ou um valor inteiro positivo de
   pelo menos 32.768 (32 KiB). Se *size* não for especificado, 0 será
   usado. Se a alteração do tamanho da pilha de threads não for
   permitida, uma "RuntimeError" será levantada. Se o tamanho da pilha
   especificado for inválido, um "ValueError" será levantado e o
   tamanho da pilha não será modificado. Atualmente, 0 KiB é o valor
   mínimo de tamanho de pilha suportado para garantir espaço
   suficiente para o próprio interpretador. Observe que algumas
   plataformas podem ter restrições específicas sobre valores para o
   tamanho da pilha, como exigir um tamanho mínimo de pilha > 32 KiB
   ou exigir alocação em múltiplos do tamanho da página de memória do
   sistema -- a documentação da plataforma deve ser consultada para
   obter mais informações (4 páginas KiB são comuns; usar múltiplos de
   4096 para o tamanho da pilha é a abordagem sugerida na ausência de
   informações mais específicas).

   Disponibilidade: Windows, pthreads.

   Plataformas Unix com suporte a threads POSIX.

_thread.TIMEOUT_MAX

   O valor máximo permitido para o parâmetro *timeout* de
   "Lock.acquire". A especificação de um tempo limite maior que esse
   valor vai levantar um "OverflowError".

   Adicionado na versão 3.2.

class _thread.LockType

   Este é o tipo de objetos de trava.

   Os objetos de trava têm os seguintes métodos:

   acquire(blocking=True, timeout=-1)

      Sem nenhum argumento opcional, esse método adquire a trava
      incondicionalmente, se necessário, aguardando até que seja
      liberada por outra thread (apenas uma thread por vez pode
      adquirir uma trava --- esse é o motivo da sua existência).

      Se o argumento inteiro *blocking* estiver presente, a ação
      dependerá do seu valor: se for falso, a trava será adquirida
      apenas se puder ser adquirida imediatamente sem aguardar,
      enquanto se for verdadeiro, a trava será adquirida
      incondicionalmente, conforme acima.

      Se o argumento de ponto flutuante *timeout* estiver presente e
      positivo, ele especificará o tempo máximo de espera em segundos
      antes de retornar. Um argumento negativo *timeout* especifica
      uma espera ilimitada. Você não pode especificar um *timeout* se
      *blocking* for falso.

      O valor de retorno é "True" se a trava for adquirida com
      sucesso, se não "False".

      Alterado na versão 3.2: O parâmetro *timeout* é novo.

      Alterado na versão 3.2: As aquisições de trava agora podem ser
      interrompidas por sinais no POSIX.

      Alterado na versão 3.14: As aquisições de trava agora podem ser
      interrompidas por sinais no Windows.

   release()

      Libera a trava. A trava deve ter sido adquirido anteriormente,
      mas não necessariamente pela mesma thread.

   locked()

      Retorna o status da trava: "True" se tiver sido adquirida por
      alguma thread, "False" se não for o caso.

   Além desses métodos, os objetos de trava também podem ser usados
   através da instrução "with", por exemplo:

      import _thread

      uma_trava = _thread.allocate_lock()

      with uma_trava:
          print("uma_trava está travada enquanto isto executa")

**Ressalvas:**

* Interrupções sempre vão para a thread principal (a exceção
  "KeyboardInterrupt" será recebida por essa thread).

* Chamar "sys.exit()" ou levantar a exceção "SystemExit" é o
  equivalente a chamar "_thread.exit()".

* Quando a thread principal se encerra, o fato de outras threads
  sobreviverem depende do sistema. Na maioria dos sistemas, elas são
  eliminadas sem executar cláusulas "try" ... "finally" ou
  destruidores de objetos.
