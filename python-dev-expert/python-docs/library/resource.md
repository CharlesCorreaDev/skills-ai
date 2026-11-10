"resource" --- Informação de uso de recursos
********************************************

======================================================================

Este módulo fornece mecanismos básicos para medir e controlar os
recursos do sistema usados por um programa.

Disponibilidade: Unix, not WASI.

Constantes simbólicas são usadas para especificar recursos específicos
do sistema e para solicitar informações de uso sobre o processo atual
ou seus filhos.

Uma exceção "OSError" é levantada em caso de falha de chamada de
sistema.

exception resource.error

   Um apelido descontinuado de "OSError".

   Alterado na versão 3.3: Seguindo a **PEP 3151**, esta classe foi
   transformada em um apelido de "OSError".


Limites de recursos
===================

O uso de recursos pode ser limitado usando a função "setrlimit()"
descrita abaixo. Cada recurso é controlado por um par de limites: um
limite suave e um limite rígido. O limite suave é o limite atual e
pode ser reduzido ou aumentado por um processo ao longo do tempo. O
limite suave nunca pode exceder o limite rígido. O limite rígido pode
ser reduzido para qualquer valor maior que o limite suave, mas não
aumentado. (Somente processos com o UID efetivo do superusuário podem
aumentar um limite rígido.)

Os recursos específicos que podem ser limitados dependem do sistema.
Eles são descritos na página man *getrlimit(2)*. Os recursos listados
abaixo são suportados quando o sistema operacional subjacente os
suporta; recursos que não podem ser verificados ou controlados pelo
sistema operacional não são definidos neste módulo para essas
plataformas.

resource.RLIM_INFINITY

   Constante usada para representar o limite de um recurso ilimitado.

   Alterado na versão 3.15: It is now always positive. Previously, it
   could be negative, such as -1 or -3.

resource.RLIM_SAVED_CUR

resource.RLIM_SAVED_MAX

   Constants used to represent the soft and hard limit values if they
   cannot be represented in the "rlim_t" value in C. Can be equal to
   "RLIM_INFINITY".

   Adicionado na versão 3.15.

resource.getrlimit(resource)

   Retorna uma tupla "(suave, rígido)" com os limites soft e hard
   atuais de *resource*. Levanta "ValueError" se um recurso inválido
   for especificado, ou "error" se a chamada do sistema subjacente
   falhar inesperadamente.

resource.setrlimit(resource, limits)

   Define novos limites de consumo de *resource*. O argumento *limits*
   deve ser uma tupla "(suave, rígido)" de dois inteiros descrevendo
   os novos limites. Um valor de "RLIM_INFINITY" pode ser usado para
   solicitar um limite ilimitado.

   Levanta "ValueError" se um recurso inválido for especificado, se o
   novo limite suave exceder o limite rígido ou se um processo tentar
   aumentar seu limite rígido. Especificar um limite de
   "RLIM_INFINITY" quando o limite rígido ou do sistema para esse
   recurso não for ilimitado resultará em uma exceção "ValueError". Um
   processo com o UID efetivo de superusuário pode solicitar qualquer
   valor limite válido, incluindo ilimitado, mas "ValueError" ainda
   será levantada se o limite solicitado exceder o limite imposto pelo
   sistema.

   "setrlimit" também pode levantar "error" se a chamada do sistema
   subjacente falhar.

   VxWorks só oferece suporte a definir "RLIMIT_NOFILE".

   Levanta um evento de auditoria "resource.setrlimit" com os
   argumentos "resource", "limits".

resource.prlimit(pid, resource[, limits])

   Combina "setrlimit()" e "getrlimit()" em uma única função e permite
   obter e definir os limites de recursos de um processo arbitrário.
   Se *pid* for 0, a chamada se aplica ao processo atual. *resource* e
   *limits* têm o mesmo significado que em "setrlimit()", exceto que
   *limits* é opcional.

   Quando *limits* não é fornecido, a função retorna o limite de
   *resource* do processo *pid*. Quando *limits* é fornecido, o limite
   de *resource* do processo é definido e o limite de recurso anterior
   é retornado.

   Levanta "ProcessLookupError" quando *pid* não pode ser encontrado e
   "PermissionError" quando o usuário não tem "CAP_SYS_RESOURCE" para
   o processo.

   Levanta um evento de auditoria "resource.prlimit" com os argumentos
   "pid", "resource", "limits".

   Disponibilidade: Linux >= 2.6.36 with glibc >= 2.13.

   Adicionado na versão 3.4.

Esses símbolos definem recursos cujo consumo pode ser controlado
usando as funções "setrlimit()" e "getrlimit()" descritas abaixo. Os
valores desses símbolos são exatamente as constantes usadas por
programas em C.

A página man do Unix para *getrlimit(2)* lista os recursos
disponíveis. Observe que nem todos os sistemas usam o mesmo símbolo ou
o mesmo valor para denotar o mesmo recurso. Este módulo não tenta
mascarar diferenças de plataforma --- símbolos não definidos para uma
plataforma não estarão disponíveis neste módulo para essa plataforma.

resource.RLIMIT_CORE

   O tamanho máximo (em bytes) de um arquivo de núcleo (core file) que
   o processo atual pode criar. Isso pode resultar na criação de um
   arquivo de núcleo parcial se um núcleo maior for necessário para
   conter a imagem completa do processo.

resource.RLIMIT_CPU

   O tempo máximo de processador (em segundos) que um processo pode
   usar. Se esse limite for excedido, um sinal "SIGXCPU" é enviado ao
   processo. (Consulte a documentação do módulo "signal" para obter
   informações sobre como capturar esse sinal e fazer algo útil, por
   exemplo, liberar arquivos abertos no disco.)

resource.RLIMIT_FSIZE

   O tamanho máximo de um arquivo que o processo pode criar.

resource.RLIMIT_DATA

   O tamanho máximo (em bytes) da heap do processo.

resource.RLIMIT_STACK

   O tamanho máximo (em bytes) da pilha de chamadas para o processo
   atual. Isso afeta apenas a pilha da thread principal em um processo
   multithread.

resource.RLIMIT_RSS

   O tamanho máximo do conjunto de residentes que deve ser
   disponibilizado para o processo.

resource.RLIMIT_NPROC

   O número máximo de processos que o processo atual pode criar.

resource.RLIMIT_NOFILE

   O número máximo de descritores de arquivo abertos para o processo
   atual.

resource.RLIMIT_OFILE

   O nome BSD para "RLIMIT_NOFILE".

resource.RLIMIT_MEMLOCK

   O espaço máximo de endereço que pode ser travado na memória.

resource.RLIMIT_VMEM

   A maior área de memória mapeada que o processo pode ocupar.
   Geralmente um apelido de "RLIMIT_AS".

   Disponibilidade: Solaris, FreeBSD, NetBSD.

resource.RLIMIT_AS

   A área máxima (em bytes) de espaço de endereço que pode ser ocupada
   pelo processo.

resource.RLIMIT_MSGQUEUE

   O número de bytes que podem ser alocados para filas de mensagens
   POSIX.

   Disponibilidade: Linux >= 2.6.8.

   Adicionado na versão 3.4.

resource.RLIMIT_NICE

   O teto para o nível agradável do processo (calculado como 20 -
   rlim_cur).

   Disponibilidade: Linux >= 2.6.12.

   Adicionado na versão 3.4.

resource.RLIMIT_RTPRIO

   O teto da prioridade em tempo real.

   Disponibilidade: Linux >= 2.6.12.

   Adicionado na versão 3.4.

resource.RLIMIT_RTTIME

   O limite de tempo (em microssegundos) no tempo de CPU que um
   processo pode gastar sob agendamento em tempo real sem fazer uma
   chamada de sistema de bloqueio.

   Disponibilidade: Linux >= 2.6.25.

   Adicionado na versão 3.4.

resource.RLIMIT_SIGPENDING

   O número de sinais que o processo pode enfileirar.

   Disponibilidade: Linux >= 2.6.8.

   Adicionado na versão 3.4.

resource.RLIMIT_SBSIZE

   O tamanho máximo (em bytes) de uso do buffer de soquete para este
   usuário. Isso limita a quantidade de memória de rede e, portanto, a
   quantidade de mbufs que este usuário pode armazenar a qualquer
   momento.

   Disponibilidade: FreeBSD, NetBSD.

   Adicionado na versão 3.4.

resource.RLIMIT_SWAP

   O tamanho máximo (em bytes) do espaço de swap que pode ser
   reservado ou utilizado por todos os processos deste ID de usuário.
   Este limite é aplicado somente se o bit 1 do sysctl vm.overcommit
   estiver definido. Consulte tuning(7) para uma descrição completa
   deste sysctl.

   Disponibilidade: FreeBSD >= 8.

   Adicionado na versão 3.4.

resource.RLIMIT_NPTS

   O número máximo de pseudoterminais criados por este ID de usuário.

   Disponibilidade: FreeBSD >= 8.

   Adicionado na versão 3.4.

resource.RLIMIT_KQUEUES

   O número máximo de kqueues que esse ID de usuário tem permissão
   para criar.

   Disponibilidade: FreeBSD >= 11.

   Adicionado na versão 3.10.

resource.RLIMIT_NTHR

   The maximum number of threads for this user id, not counting the
   main and kernel threads.

   Disponibilidade: NetBSD >= 7.0.

   Adicionado na versão 3.15.

resource.RLIMIT_PIPEBUF

   The maximum total size of in-kernel buffers for bi-directional
   pipes/fifos that this user id is allowed to consume.

   Disponibilidade: FreeBSD >= 14.2.

   Adicionado na versão 3.15.

resource.RLIMIT_THREADS

   The maximum number of threads each process can create.

   Disponibilidade: AIX.

   Adicionado na versão 3.15.

resource.RLIMIT_UMTXP

   The limit of the number of process-shared Posix thread library
   objects allocated by user id.

   Disponibilidade: FreeBSD >= 11.

   Adicionado na versão 3.15.


Uso de recursos
===============

Essas funções são usadas para recuperar informações de uso de
recursos:

resource.getrusage(who)

   Esta função retorna um objeto que descreve os recursos consumidos
   pelo processo atual ou seus filhos, conforme especificado pelo
   parâmetro *who*. O parâmetro *who* deve ser especificado usando uma
   das constantes "RUSAGE_*" descritas abaixo.

   Um exemplo simples:

      from resource import *
      import time

      # uma tarefa não vinculada à CPU
      time.sleep(3)
      print(getrusage(RUSAGE_SELF))

      # uma tarefa vinculada à CPU
      for i in range(10 ** 8):
         _ = 1 + 1
      print(getrusage(RUSAGE_SELF))

   Os campos do valor de retorno descrevem como um recurso específico
   do sistema foi utilizado, por exemplo, a quantidade de tempo gasto
   em execução no modo de usuário ou o número de vezes que o processo
   foi trocado da memória principal. Alguns valores dependem do
   intervalo de tique do relógio, por exemplo, a quantidade de memória
   que o processo está usando.

   Para retrocompatibilidade, o valor de retorno também pode ser
   acessado como uma tupla de 16 elementos.

   Os campos "ru_utime" e "ru_stime" do valor de retorno são valores
   de ponto flutuante que representam o tempo gasto na execução no
   modo usuário e o tempo gasto na execução no modo sistema,
   respectivamente. Os valores restantes são inteiros. Consulte a
   página man *getrusage(2)* para obter informações detalhadas sobre
   esses valores. Um breve resumo é apresentado aqui:

   +----------+------------------------+-----------------------------------------+
   | Índice   | Campo                  | Recurso                                 |
   |==========|========================|=========================================|
   | "0"      | "ru_utime"             | tempo no modo de usuário (segundos em   |
   |          |                        | pontos flutuantes)                      |
   +----------+------------------------+-----------------------------------------+
   | "1"      | "ru_stime"             | tempo no modo de sistema (segundos em   |
   |          |                        | pontos flutuantes)                      |
   +----------+------------------------+-----------------------------------------+
   | "2"      | "ru_maxrss"            | tamanho máximo do conjunto residente    |
   +----------+------------------------+-----------------------------------------+
   | "3"      | "ru_ixrss"             | tamanho da memória compartilhada        |
   +----------+------------------------+-----------------------------------------+
   | "4"      | "ru_idrss"             | tamanho da memória não compartilhada    |
   +----------+------------------------+-----------------------------------------+
   | "5"      | "ru_isrss"             | tamanho da pilha não compartilhada      |
   +----------+------------------------+-----------------------------------------+
   | "6"      | "ru_minflt"            | falhas de página que não requerem E/S   |
   +----------+------------------------+-----------------------------------------+
   | "7"      | "ru_majflt"            | falhas de página que requerem E/S       |
   +----------+------------------------+-----------------------------------------+
   | "8"      | "ru_nswap"             | número de trocas para a memórias de     |
   |          |                        | swap                                    |
   +----------+------------------------+-----------------------------------------+
   | "9"      | "ru_inblock"           | operações de entrada de bloco           |
   +----------+------------------------+-----------------------------------------+
   | "10"     | "ru_oublock"           | operações de saída de bloco             |
   +----------+------------------------+-----------------------------------------+
   | "11"     | "ru_msgsnd"            | mensagens enviadas                      |
   +----------+------------------------+-----------------------------------------+
   | "12"     | "ru_msgrcv"            | mensagens recebidas                     |
   +----------+------------------------+-----------------------------------------+
   | "13"     | "ru_nsignals"          | sinais recebidos                        |
   +----------+------------------------+-----------------------------------------+
   | "14"     | "ru_nvcsw"             | trocas voluntárias de contexto          |
   +----------+------------------------+-----------------------------------------+
   | "15"     | "ru_nivcsw"            | trocas involuntárias de contexto        |
   +----------+------------------------+-----------------------------------------+

   Esta função levantará uma "ValueError" se um parâmetro *who*
   inválido for especificado. Também pode levantar uma exceção "error"
   em circunstâncias incomuns.

resource.getpagesize()

   Retorna o número de bytes em uma página do sistema. (Não precisa
   ser o mesmo que o tamanho da página de hardware.)

Os seguintes símbolos "RUSAGE_*" são passados para a função
"getrusage()" para especificar quais informações de processos devem
ser fornecidas.

resource.RUSAGE_SELF

   Passeapara "getrusage()" para solicitar recursos consumidos pelo
   processo de chamada, que é a soma dos recursos usados por todas as
   threads no processo.

resource.RUSAGE_CHILDREN

   Passa para "getrusage()" para solicitar recursos consumidos por
   processos filhos do processo de chamada que foram encerrados e
   aguardados.

resource.RUSAGE_BOTH

   Passa para "getrusage()" para solicitar recursos consumidos pelo
   processo atual e pelos processos filhos. Pode não estar disponível
   em todos os sistemas.

resource.RUSAGE_THREAD

   Passa para "getrusage()" para solicitar recursos consumidos pela
   thread atual. Pode não estar disponível em todos os sistemas.

   Adicionado na versão 3.2.
