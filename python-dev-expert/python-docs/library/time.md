"time" --- Acesso e conversões de tempo
***************************************

======================================================================

Esse módulo provê várias funções relacionadas à tempo. Para
funcionalidades relacionadas veja também os módulos "datetime" e
"calendar"

Apesar desse módulo sempre estar disponível, nem todas as suas funções
estão disponíveis em todas as plataformas. A maioria das funções
definidas nesse módulo chamam funções da biblioteca da plataforma de C
com mesmo nome.  Pode ser útil consultar a documentação da plataforma,
pois da semântica dessas funções variam a depender da plataforma.

A seguir, uma explicação de algumas terminologias e convenções.

* O *era* (*epoch*) é o ponto onde o tempo começa, o valor de retorno
  de "time.gmtime(0)". É 1º de janeiro de 1970, 00:00:00 (UTC) em
  todas as plataformas.

* O termo *segundos desde a era* refere-se ao número total de segundos
  decorrido desde a era, tipicamente excluindo-se os segundos
  bissextos. Segundos bissextos são excluídos desse total em todas as
  plataformas compatíveis com POSIX.

* As funções desse módulo podem não conseguir tratar de datas e
  horários antes do epoch ou muito distantes no futuro. O limite no
  futuro é determinado pela biblioteca C; para sistemas de 32 bit,
  geralmente é 2038.

* A função "strptime()" pode analisar anos de 2 dígitos quando é
  passado o código de formato "%y". Quando anos de 2 dígitos são
  analisados, eles são convertidos de acordo com os padrões POSIX e
  ISO C: valores 69--99 são mapeados para 1969--1999, e valores 0--68
  são mapeados para 2000--2068.

* UTC é Coordinated Universal Time (em português, Horário Universal
  Coordenado) e substituiu o GMT ou Greenwich Mean Time (em português,
  Horário Médio de Greenwich) como base da cronometragem
  internacional. A sigla UTC não é um erro, mas está em conformidade
  com um esquema de nomenclatura anterior, independente de idioma,
  para padrões de tempo como UT0, UT1 e UT2.

* DST é Daylight Saving Time (Horário de Verão), um ajuste de fuso
  horário por (normalmente) uma hora durante parte do ano. As regras
  de Horário de Verão são mágicas (determinadas por leis locais) e
  podem mudar de ano a ano. A biblioteca C possui uma tabela contendo
  as regras locais (normalmente lidas de um arquivo de sistema por
  flexibilidade) e nesse contexto é a única fonte de Conhecimento
  Verdadeiro.

* A precisão de várias funções em tempo real podem ser menores do que
  o que pode estar sugerido pelas unidades nas quais seu valor ou
  argumento estão expressos. Por exemplo, na maioria dos sistemas
  Unix, o relógio "conta" apenas 50 ou 100 vezes por segundo.

* Por outro lado, a precisão de "time()" e "sleep()" é melhor do que
  suas equivalentes Unix: tempos são expressos como números em ponto
  flutuante, "time()" retorna o tempo mais preciso disponível
  (utilizando "gettimeofday()" do Unix, quando disponível) e "sleep()"
  irá aceitar qualquer tempo como uma fração não zero ("select()" do
  Unix é utilizada para implementar isto, quando disponível).

* O valor de tempo conforme retornado pelas "gmtime()", "localtime()",
  e "strptime()", e aceito pelas "asctime()", "mktime()" e
  "strftime()", é uma sequência de 9 inteiros. Os valores retornados
  das "gmtime()", "localtime()", e "strptime()" também oferecem nomes
  de atributo para campos individuais.

  Veja "struct_time" para a descrição desses objetos.

  Alterado na versão 3.3: O tipo "struct_time" foi estendido para
  prover os atributos "tm_gmtoff" e "tm_zone" quando a plataforma
  suporta os membros "struct tm" correspondentes

  Alterado na versão 3.6: Os atributos "tm_gmtoff" e "tm_zone" da
  classe "struct_time" estão disponíveis em todas as plataformas
  agora.

* Utilize as seguintes funções para converter entre representações de
  tempo:

  +---------------------------+---------------------------+---------------------------+
  | De                        | Para                      | Utilize                   |
  |===========================|===========================|===========================|
  | segundos desde a era      | "struct_time" em UTC      | "gmtime()"                |
  +---------------------------+---------------------------+---------------------------+
  | segundos desde a era      | "struct_time" em tempo    | "localtime()"             |
  |                           | local                     |                           |
  +---------------------------+---------------------------+---------------------------+
  | "struct_time" em UTC      | segundos desde a era      | "calendar.timegm()"       |
  +---------------------------+---------------------------+---------------------------+
  | "struct_time" em tempo    | segundos desde a era      | "mktime()"                |
  | local                     |                           |                           |
  +---------------------------+---------------------------+---------------------------+


Funções
=======

time.asctime([time_tuple])

   Converte a tupla ou "struct_time" representando um tempo como
   retornado pela "gmtime()" ou "localtime()" para uma string com o
   seguinte formato: "'Sun Jun 20 23:21:05 1993'". O campo dia contém
   dois caracteres e possui espaçamento se o dia é de apenas um
   dígito. Por exemplo, "'Wed Jun 9 04:26:40 1993'".

   Se *time_tuple* não é fornecido, o tempo atual como retornado por
   "localtime()" é utilizado. Informação de localidade não é utilizada
   por "asctime()".

   Nota:

     Diferentemente da função em C de mesmo nome, "asctime()" não
     adiciona uma nova linha em seguida.

time.pthread_getcpuclockid(thread_id, /)

   Retorna o *clk_id* do relógio de tempo de CPU específico da thread
   para a *thread_id* especificada.

   Utilize a "threading.get_ident()" ou o atributo "ident" dos objetos
   "threading.Thread" para obter um valor adequado para *thread_id*.

   Aviso:

     Passando um *thread_id* inválido ou expirado pode resultar em um
     comportamento indefinido, como, por exemplo, falha de
     segmentação.

   Disponibilidade: Unix

   Veja a página man para *pthread_getcpuclockid(3)* para mais
   informações.

   Adicionado na versão 3.7.

time.clock_getres(clk_id, /)

   Retorna a resolução (precisão) do relógio *clk_id* especificado.
   Confira Constantes de ID de Relógio para uma lista de valores
   aceitos para *clk_id*

   Disponibilidade: Unix.

   Adicionado na versão 3.3.

time.clock_gettime(clk_id, /) -> float

   Retorna o tempo to relógio *clk_id* especificado. Confira
   Constantes de ID de Relógio para uma lista de valores aceitos para
   *clk_id*.

   Use "clock_gettime_ns()" para evitar perda de precisão causada pelo
   tipo "float".

   Disponibilidade: Unix.

   Adicionado na versão 3.3.

time.clock_gettime_ns(clk_id, /) -> int

   Semelhante à "clock_gettime()", mas retorna o tempo em
   nanossegundos.

   Disponibilidade: Unix.

   Adicionado na versão 3.7.

time.clock_settime(clk_id, time, /)

   Define o tempo do relógio *clk_id* especificado. Atualmente,
   "CLOCK_REALTIME" é o único valor aceito para *clk_id*.

   Use "clock_settime_ns()" para evitar perda de precisão causada pelo
   tipo "float".

   Disponibilidade: Unix, not Android, not iOS.

   Adicionado na versão 3.3.

   Alterado na versão 3.15: Aceita qualquer número real como *time*, e
   não apenas inteiros (*integer*) ou números de vírgula flutuante
   (*float*).

time.clock_settime_ns(clk_id, time: int, /)

   Semelhante à "clock_settime()", mas define o tempo em
   nanossegundos.

   Disponibilidade: Unix, not Android, not iOS.

   Adicionado na versão 3.7.

time.ctime(seconds=None, /)

   Converte um tempo expresso em segundos desde o epoch para uma
   string de forma: "'Sun Jun 20 23:21:05 1993'" representando tempo
   local. O campo dia tem comprimento de dois caracteres e é deslocado
   por um espaço se o dia tem um único dígito. Por exemplo, "'Wed Jun
   9 04:26:40 1993'".

   Se *seconds* não é fornecido ou "None", o tempo atual como
   retornado por "time()" é utilizado. "ctime(seconds)" é equivalente
   a "asctime(localtime(seconds))". Informação de localidade não é
   utilizada por "ctime()".

   Alterado na versão 3.15: Aceita qualquer número real, e não apenas
   inteiros (*integer*) ou números de vírgula flutuante (*float*).

time.get_clock_info(name, /)

   Obtém informação do relógio específico como um objeto espaço de
   nomes. Nomes de relógios suportados e as funções correspondentes
   para ler seus valores são:

   * "'monotonic'": "time.monotonic()"

   * "'perf_counter'": "time.perf_counter()"

   * "'process_time'": "time.process_time()"

   * "'thread_time'": "time.thread_time()"

   * "'time'": "time.time()"

   O resultado tem os seguintes atributos:

   * *adjustable*: "True" se o relógio puder ser configurado para
     avançar ou retroceder no tempo, "False" caso contrário. Não se
     refere a ajustes graduais da taxa NTP.

   * *implementation*: O nome da função C subjacente utilizada para
     obter o valor do relógio. Confira Constantes de ID de Relógio
     para valores possíveis.

   * *monotonic*: "True" se o relógio não pode retornar a valores
     anteriores, backward, "False" contrário

   * *resolution*: A resolução do relógio em segundos ("float")

   Adicionado na versão 3.3.

time.gmtime(seconds=None, /)

   Converte um tempo expresso em segundos desde o epoch para uma
   "struct_time" em UTC onde o sinalizador de horário de verão é
   sempre zero. Se *seconds* não é fornecido ou "None", o tempo atual
   como retornado por "time()" é utilizado. Frações de segundo são
   ignoradas. Veja acima para uma descrição do objeto "struct_time".
   Veja "calendar.timegm()" para o inverso desta função.

   Alterado na versão 3.15: Aceita qualquer número real, e não apenas
   inteiros (*integer*) ou números de vírgula flutuante (*float*).

time.localtime(seconds=None, /)

   Como "gmtime()", mas converte para o tempo local. Se *seconds* não
   é fornecido ou "None", o tempo atual como retornado por "time()" é
   utilizado. O sinalizador de horário de verão é definido como "1"
   quando o Horário de verão for aplicável para o tempo fornecido.

   "localtime()" pode levantar "OverflowError", se o registro de data
   e hora estiver fora de valores suportados pelas funções
   "localtime()" or "gmtime()" da plataforma C, e "OSError" no caso de
   "localtime()" ou "gmtime()" falharem. É comum É comum que isso seja
   restrito a anos de 1970 a 2038.

   Alterado na versão 3.15: Aceita qualquer número real, e não apenas
   inteiros (*integer*) ou números de vírgula flutuante (*float*).

time.mktime(time_tuple, /)

   Esta é a função inversa de "localtime()". Seu argumento é a
   "struct_time" ou uma tupla com 9 itens (sendo o sinalizador de
   horário de verão necessário; utilize "-1" como sinalizador de
   horário de verão quando este for desconhecido) que expressa o tempo
   em tempo *local*, não UTC. Retorna um número em ponto flutuante,
   para ter compatibilidade com "time()". Se o valor de entrada não
   puder ser representado como um tempo válido, ou "OverflowError" ou
   "ValueError" serão levantadas (o que irá depender se o valor
   inválido é capturado pelo Python ou por bibliotecas C subjacentes).
   A data mais recente para qual um tempo pode ser gerado é dependente
   da plataforma.

time.monotonic() -> float

   Retorna o valor (em frações de segundos) de um relógio monotônico,
   i.e. um relógio que não pode voltar a valores anteriores. O relógio
   não é afetado por atualizações do relógio do sistema. O ponto de
   referência do valor retornado é indefinido, portanto apenas a
   diferença entre os resultados de duas chamadas é válida.

   Relógio:

   * No Windows, chama "QueryPerformanceCounter()" e
     "QueryPerformanceFrequency()".

   * No macOS, chama "mach_absolute_time()" e "mach_timebase_info()".

   * No HP-UX, chama "gethrtime()".

   * Chama "clock_gettime(CLOCK_HIGHRES)" se disponível.

   * Do contrário, chama "clock_gettime(CLOCK_MONOTONIC)".

   Use "monotonic_ns()" para evitar perda de precisão causada pelo
   tipo "float".

   Adicionado na versão 3.3.

   Alterado na versão 3.5: A função agora está sempre disponível e o
   relógio agora é o mesmo para todos os processos.

   Alterado na versão 3.10: No macOS, o relógio agora é o mesmo para
   todos os processos.

time.monotonic_ns() -> int

   Semelhante à "monotonic()", mas retorna tempo em nanossegundos.

   Adicionado na versão 3.7.

time.perf_counter() -> float

   Retorna o valor (em frações de segundo) de um contador de
   desempenho, i.e. um relógio com a maior resolução disponível para
   medir uma duração curta. Inclui o tempo decorrido durante a pausa.
   O relógio é o mesmo para todos os processos. O ponto de referência
   é do valor retornado é indefinido, portanto apenas a diferença
   entre resultados de duas chamadas é válida.

   No CPython, use o mesmo relógio que "time.monotonic()" e é um
   relógio monotônico, ou seja, um relógio que não pode retroceder.

   Use "perf_counter_ns()" para evitar perda de precisão causada pelo
   tipo "float".

   Adicionado na versão 3.3.

   Alterado na versão 3.10: No Windows, o relógio agora é o mesmo para
   todos os processos.

   Alterado na versão 3.13: Usa o mesmo relógio que
   "time.monotonic()".

time.perf_counter_ns() -> int

   Semelhante à "perf_counter()", mas retorna o tempo em
   nanossegundos.

   Adicionado na versão 3.7.

time.process_time() -> float

   Retorna o valor (em frações de segundo) da soma dos tempos do
   sistema e CPU de usuário do processo atual. Não inclui o tempo
   decorrido durante a pausa. É de todo o processo por definição. O
   ponto de referência do valor retornado é indefinido, então apenas a
   diferença dos resultados de duas chamadas é válida.

   Use "process_time_ns()" para evitar perda de precisão causada pelo
   tipo "float".

   Adicionado na versão 3.3.

time.process_time_ns() -> int

   Semelhante à "process_time()", mas retorna o tempo em
   nanossegundos.

   Adicionado na versão 3.7.

time.sleep(seconds, /)

   Suspende a execução da thread de chamada por um determinado número
   de segundos. O argumento pode ser um número não-inteiro para
   indicar um tempo de pausa mais preciso.

   Se a pausa for interrompida por um sinal e nenhuma exceção for
   levantada pelo manipulador de sinal, a pausa será reiniciada com um
   tempo limite recalculado.

   O tempo de suspensão pode ser maior do que o solicitado por um
   valor arbitrário, devido ao agendamento de outras atividades no
   sistema.

   -[ Implementação no Windows ]-

   No Windows, se *seconds* é zero, a thread renuncia ao restante de
   sua fatia de tempo para qualquer outra thread que esteja pronto
   para executar. Se nenhuma outra thread estiver pronta pra ser
   executada, a função retorna imediatamente, e a thread continua a
   execução. No Windows 8.1 e mais novos a implementação usa um
   temporizador de alta resolução que provê uma resolução de 100
   nanossegundos. Se *seconds* é zero, é usado "Sleep(0)".

   -[ Implementação no Unix ]-

   * Usa "clock_nanosleep()" se disponível (resolução: 1
     nanossegundo);

   * Ou usa "nanosleep()" se disponível (resolução: 1 nanossegunda);

   * Ou usa "select()" (resolução: 1 microssegundo).

   Nota:

     Para emular um "no-op", use "pass" em vez de "time.sleep(0)".Para
     abrir mão voluntariamente da CPU, especifique uma política de
     agendamento em tempo real e use "os.sched_yield()" em seu lugar.

   Levanta um evento de auditoria "time.sleep" com o argumento
   "seconds".

   Alterado na versão 3.5: A função agora pausa por pelo menos
   *seconds* mesmo se a pausa é interrompido por um sinal, exceto se o
   tratador de sinal levanta uma exceção (veja **PEP 475** para a
   explicação).

   Alterado na versão 3.11: No Unix, as funções "clock_nanosleep()" e
   "nanosleep()" são agora usadas se estiverem disponíveis. No
   Windows, um temporizador aguardável é agora usado.

   Alterado na versão 3.13: Levanta um evento de auditoria.

   Alterado na versão 3.15: Aceita qualquer número real, e não apenas
   inteiros (*integer*) ou números de vírgula flutuante (*float*).

time.strftime(format[, time_tuple])

   Converte a tupla ou "struct_time" representando um tempo como
   retornado por "gmtime()" ou "localtime()" para uma string como
   especificado pelo argumento *format*. Se *time_tuple* não é
   fornecido, o tempo atual como retornado pela "localtime()" é
   utilizado. *format* deve ser uma string. A exceção "ValueError" é
   levantada se qualquer campo em *time_tuple* está fora do intervalo
   permitido.

   0 é um argumento legal para qualquer posição na tupla de tempo; se
   é normalmente ilegal, o valor é formado a um valor correto.

   As diretivas a seguir podem ser incorporadas na string *format*.
   Elas estão mostradas sem os campos de comprimento e especificação
   de precisão opcionais, e estão substituídos pelos caracteres
   indicados no resultado da "strftime()":

   +-------------+--------------------------------------------------+---------+
   | Diretiva    | Significado                                      | Notas   |
   |=============|==================================================|=========|
   | "%a"        | Nome abreviado do dia da semana da localidade.   |         |
   +-------------+--------------------------------------------------+---------+
   | "%A"        | Nome completo do dia da semana da localidade.    |         |
   +-------------+--------------------------------------------------+---------+
   | "%b"        | Nome abreviado do mês da localidade.             |         |
   +-------------+--------------------------------------------------+---------+
   | "%B"        | Nome completo do mês da localidade.              |         |
   +-------------+--------------------------------------------------+---------+
   | "%c"        | Representação de data e hora apropriada da       |         |
   |             | localidade.                                      |         |
   +-------------+--------------------------------------------------+---------+
   | "%d"        | Dia do mês como um número decimal [01,31].       |         |
   +-------------+--------------------------------------------------+---------+
   | "%f"        | Microssegundos como um número decimal            | (1)     |
   |             | [000000,999999].                                 |         |
   +-------------+--------------------------------------------------+---------+
   | "%H"        | Hora (relógio 24 horas) como um número decimal   |         |
   |             | [00,23].                                         |         |
   +-------------+--------------------------------------------------+---------+
   | "%I"        | Hora (relógio 12 horas) como um número decimal   |         |
   |             | [01,12].                                         |         |
   +-------------+--------------------------------------------------+---------+
   | "%j"        | Dia do ano como um número decimal [001,366].     |         |
   +-------------+--------------------------------------------------+---------+
   | "%m"        | Mês como um número decimal [01,12].              |         |
   +-------------+--------------------------------------------------+---------+
   | "%M"        | Minuto como um número decimal [00,59].           |         |
   +-------------+--------------------------------------------------+---------+
   | "%p"        | Equivalente da localidade a AM ou PM.            | (2)     |
   +-------------+--------------------------------------------------+---------+
   | "%S"        | Segundo como um número decimal [00,61].          | (3)     |
   +-------------+--------------------------------------------------+---------+
   | "%U"        | Número da semana do ano (domingo como primeiro   | (4)     |
   |             | dia da semana) como um número decimal [00,53].   |         |
   |             | Todos os dias em um ano novo que precedem o      |         |
   |             | primeiro domingo são considerados como estando   |         |
   |             | na semana 0.                                     |         |
   +-------------+--------------------------------------------------+---------+
   | "%u"        | Dia da semana (segunda-feira é 1; domingo é 7)   |         |
   |             | como um número decimal [1, 7].                   |         |
   +-------------+--------------------------------------------------+---------+
   | "%w"        | Dia da semana como um número decimal             |         |
   |             | [0(Domingo),6]                                   |         |
   +-------------+--------------------------------------------------+---------+
   | "%W"        | Número da semana do ano (segunda-feira como o    | (4)     |
   |             | primeiro dia da semana) como um número decimal   |         |
   |             | [00,53]. Todos os dias do ano que precedem o     |         |
   |             | primeiro domingo serão considerados como estando |         |
   |             | na semana 0.                                     |         |
   +-------------+--------------------------------------------------+---------+
   | "%x"        | Representação de data apropriada de localidade.  |         |
   +-------------+--------------------------------------------------+---------+
   | "%X"        | Representação de hora apropriada da localidade.  |         |
   +-------------+--------------------------------------------------+---------+
   | "%y"        | Ano sem século como um número decimal [00,99].   |         |
   +-------------+--------------------------------------------------+---------+
   | "%Y"        | Ano com século como um número decimal.           |         |
   +-------------+--------------------------------------------------+---------+
   | "%z"        | Deslocamento de fuso horário indicando uma       |         |
   |             | diferença de tempo positiva ou negativa de       |         |
   |             | UTC/GMT formatado como +HHMM ou -HHMM, onde H    |         |
   |             | representa os dígitos decimais de hora e M       |         |
   |             | representa os dígitos decimais de minuto         |         |
   |             | [-23:59, +23:59]. [1]                            |         |
   +-------------+--------------------------------------------------+---------+
   | "%Z"        | Nome do fuso horário (nenhum caractere se nenhum |         |
   |             | fuso horário existe). Descontinuado. [1]         |         |
   +-------------+--------------------------------------------------+---------+
   | "%G"        | Ano ISO 8601 (semelhante a "%Y", mas segue as    |         |
   |             | regras para o ano calendário ISO 8601). O ano    |         |
   |             | começa com a semana que contém a primeira        |         |
   |             | quinta-feira do ano calendário.                  |         |
   +-------------+--------------------------------------------------+---------+
   | "%V"        | Número da semana ISO 8601 (como um número        |         |
   |             | decimal [01,53]). A primeira semana do ano é     |         |
   |             | aquela que contém a primeira quinta-feira do     |         |
   |             | ano. As semanas começam na segunda-feira.        |         |
   +-------------+--------------------------------------------------+---------+
   | "%%"        | Um caractere literal "'%'".                      |         |
   +-------------+--------------------------------------------------+---------+

   Notas:

   1. A diretiva de formatação "%f" é somente aplicada para
      "strptime()", não para "strftime()". Contudo, veja também
      "datetime.datetime.strptime()" e "datetime.datetime.strftime()"
      onde a diretiva de formatação "%f"  é aplicada para
      microssegundos.

   2. Quando utilizado com a função "strptime()", a diretiva "%p"
      apenas afeta a saída do campo se a diretiva "%I" é utilizada
      para analisar a hora.

   3. O intervalo é realmente "0" até "61"; o valor "60" é válido em
      registros de data e hora  representando segundos bissextos e o
      valor "61" é suportado por razões históricas.

   4. Quando utilizado co a função "strptime()", "%U" e "%W" são
      utilizados em cálculos apenas quando o dia da semana e ano são
      especificados.

   Veja este exemplo, um formato para datas compatível com as
   especificações dos padrões de e-mail **RFC 5322**. [1]

      >>> from time import gmtime, strftime
      >>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
      'Thu, 28 Jun 2001 14:17:15 +0000'

   Diretivas adicionais podem ser suportadas por algumas plataformas,
   mas apenas as listadas aqui possuem significado padronizado por
   ANSI C. Para ver a lista completa de códigos de formato suportados
   na sua plataforma, consulte a documentação *strftime(3)*.

   Em algumas plataformas, um campo adicional de comprimento e
   especificação de precisão podem seguir imediatamente após "'%'"
   como uma diretiva da seguinte ordem; isto também não é portátil. O
   campo comprimento normalmente é 2 exceto para "%j" quando é 3.

time.strptime(string[, format])

   Analisa a string representando um tempo de acordo com um formato. O
   valor retornado é um "struct_time" como retornado por "gmtime()" ou
   "localtime()".

   O parâmetro *format* utiliza as mesmas diretivas das utilizadas por
   "strftime()"; é definido por padrão para ""%a %b %d %H:%M:%S %Y""
   que corresponde com a formatação retornada por "ctime()". Se
   *string* não puder ser analisada de acordo com *format*, ou se
   possui excesso de dados após analisar, "ValueError" é levantado. Os
   valores padrão utilizados para preencher quaisquer dados faltantes
   quando valores mais precisos não puderem ser inferidos são "(1900,
   1, 1, 0, 0, 0, 0, 1, -1)". Ambos *string* e *format* devem ser
   strings.

   Por exemplo:

   >>> import time
   >>> time.strptime("30 Nov 00", "%d %b %y")
   time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
                    tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

   Suporte para a diretiva "%Z" é baseado nos valores contidos em
   "tzname" e se "daylight" é verdade.  Por causa disso, é específico
   de plataforma exceto por reconhecer UTC e GMT, que são sempre
   conhecidos (e considerados fuso horários sem horários de verão).

   Apenas as diretivas especificadas na documentação são suportadas.
   Como "strftime()" é implementada por plataforma, esta pode apenas
   as vezes oferecer mais diretivas do que as listadas aqui. Mas
   "strptime()" é independente de quaisquer plataformas e portanto não
   necessariamente suporta todas as diretivas disponíveis que não
   estão documentadas como suportadas.

class time.struct_time

   O tipo da sequência de valor de tempo retornado por "gmtime()",
   "localtime()", e "strptime()". É um objeto com uma interface *named
   tuple*: os valores podem ser acessados por um índice e por um nome
   de atributo. Os seguintes valores estão presentes:

   +-----------------------------------+-----------------------------------+-----------------------------------+
   | Índice                            | Atributo                          | Valores                           |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 0                                 | tm_year                           | (por exemplo, 1993)               |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 1                                 | tm_mon                            | intervalo [1,12]                  |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 2                                 | tm_mday                           | intervalo [1,31]                  |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 3                                 | tm_hour                           | intervalo [0,23]                  |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 4                                 | tm_min                            | intervalo [0,59]                  |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 5                                 | tm_sec                            | intervalo [0, 61]; veja Nota (2)  |
   |                                   |                                   | em "strftime()"                   |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 6                                 | tm_wday                           | intervalo [0, 6]; segunda-feira é |
   |                                   |                                   | 0                                 |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 7                                 | tm_yday                           | intervalo [1, 366]                |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | 8                                 | tm_isdst                          | 0, 1 ou -1; veja abaixo           |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | N/D                               | tm_zone                           | abreviação do nome do fuso        |
   |                                   |                                   | horário                           |
   +-----------------------------------+-----------------------------------+-----------------------------------+
   | N/D                               | tm_gmtoff                         | deslocamento a leste de UTC em    |
   |                                   |                                   | segundos                          |
   +-----------------------------------+-----------------------------------+-----------------------------------+

   Note que diferentemente da estrutura C, o valor do mês é um
   intervalo [1,12] e não [0,11].

   Em chamadas para "mktime()", "tm_isdst" pode ser definido como 1
   quando o horário de verão estiver em efeito, e 0 quando não. Um
   valor de -1 indica que esta informação não é conhecida, e
   geralmente resultará no preenchimento do estado correto.

   Quando uma tupla com comprimento incorreto é passada para uma
   função que espera por um "struct_time", ou por possuir elementos do
   tipo errado, um "TypeError" é levantado.

time.time() -> float

   Retorna o tempo em segundos desde o epoch como um número em ponto
   flutuante. A manipulação de segundos bissextos é dependente da
   plataforma. No Windows e na maioria dos sistemas Unix, o segundo
   bissexto não é contado para o tempo desde o epoch. Isso é comumente
   referido como epoch ou era Unix.

   Note que mesmo o tempo sendo retornado sempre como um número em
   ponto flutuante, nem todos os sistemas fornecem o tempo com
   precisão melhor que 1 segundo. Enquanto esta função normalmente
   retorna valores não decrescentes, pode retornar valores menores do
   que os de uma chamada anterior se o relógio do sistema foi
   redefinido entre duas chamadas.

   O número retornado por "time()" pode ser convertido a um formato de
   tempo mais comum (i.e. ano, mês, dia, hora etc...) em UTC por
   passá-lo para a função "gmtime()" ou em tempo local por passar para
   a função "localtime()". Em ambos os casos, o objeto "struct_time" é
   retornado, por onde os componentes de data do calendário podem ser
   acessados ou atribuídos.

   Relógio:

   * No Windows, chama "GetSystemTimePreciseAsFileTime()".

   * Chama "clock_gettime(CLOCK_REALTIME)" se disponível.

   * Caso contrário, chama "gettimeofday()".

   Use "time_ns()" para evitar perda de precisão causada pelo tipo
   "float".

Alterado na versão 3.13: No Windows, chama
"GetSystemTimePreciseAsFileTime()" em vez de
"GetSystemTimeAsFileTime()".

time.time_ns() -> int

   Semelhante à "time()", mas retorna o tempo como um número inteiro
   de nanossegundos desde o epoch.

   Adicionado na versão 3.7.

time.thread_time() -> float

   Retorna o valor (em fração de segundos) da soma dos tempos de
   sistema e CPU de usuário para a thread atual. Não inclui o tempo
   decorrido durante a pausa. É específico a thread por definição. O
   ponto de referência do valor retornado é indefinido, então apenas a
   diferença dos resultados de duas chamadas é válida.

   Use "thread_time_ns()" para evitar perda de precisão causada pelo
   tipo "float".

   Disponibilidade: Linux, Unix, Windows.

   Sistemas Unix possuem suporte para "CLOCK_THREAD_CPUTIME_ID".

   Adicionado na versão 3.7.

time.thread_time_ns() -> int

   Semelhante à "thread_time()", mas retorna o tempo em nanossegundos.

   Adicionado na versão 3.7.

time.tzset()

   Redefine as regras de conversão utilizadas pelas rotinas da
   biblioteca. A variável de ambiente "TZ" especifica como isto é
   feito. Também irá redefinir as variáveis "tzname" (da variável de
   ambiente "TZ"), "timezone" (segundos sem horário de verão a oeste
   de UTC), "altzone" (segundos com horário de verão a oeste de UTC) e
   "daylight" (para 0 se este fuso horário não possui nenhuma regra de
   horário de verão, ou diferente de zero se há um tempo, no presente,
   passado ou futuro quando o horário de verão se aplica).

   Disponibilidade: Unix.

   Nota:

     Embora em vários casos, alterar a variável de sistema "TZ" pode
     afetar a saída de funções como "localtime()" sem chamar
     "tzset()", este comportamento não deve ser confiado.A variável de
     sistema "TZ" não deve conter espaços em branco.

   O formato padrão da variável de sistema "TZ" é (espaços foram
   adicionados por motivos de clareza):

      std offset [dst [offset [,start[/time], end[/time]]]]

   Onde os componentes são:

   "std" e "dst"
      Três ou mais alfanuméricos fornecendo a abreviação do fuso
      horário. Estes serão propagados para time.tzname

   "offset"
      O deslocamento tem a forma: "± hh[:mm[:ss]]". Isso indica que o
      valor adicionado adicionou o horário local para chegar a UTC. Se
      precedido por um '-', o fuso horário está a leste do Meridiano
      Primário; do contrário, está a oeste. Se nenhum deslocamento
      segue o horário de verão, o tempo no verão é presumido como
      estando uma hora a frente do horário padrão.

   "start[/time], end[/time]"
      Indica quando mudar e voltar do Horário de Verão. O formato das
      datas de início e fim é um dos seguintes:

      "J*n*"
         I dia juliano *n* (1 <= *n* <= 365). Os dias bissextos não
         são contados, então, em todos os anos, 28 de fevereiro é o
         dia 59 e 1 de março é o dia 60.

      "*n*"
         O dia juliano baseado em zero (0 <= *n* <= 365). Dias
         bissextos são contados, e é possível fazer referência a 29 de
         fevereiro.

      "M*m*.*n*.*d*"
         O *d*-ésimo dia (0 <= *d* <= 6) da semana *n* do mês *m* do
         ano (1 <= *n* <= 5, 1 <= *m* <= 12, onde semana 5 significa
         "o último dia *d* no mês *m*" que pode ocorrer tanto na
         quarta como quinta semana). Semana 1 é a primeira semana na
         qual o *d*-ésimo dia ocorre. Dia zero é o domingo.

      "time" tem o mesmo formato que "offset", exceto que nenhum sinal
      no início é permitido ('-' ou '+'). O padrão, se o tempo não é
      dado, é 02:00:00.

      >>> os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
      >>> time.tzset()
      >>> time.strftime('%X %x %Z')
      '02:07:36 05/08/03 EDT'
      >>> os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
      >>> time.tzset()
      >>> time.strftime('%X %x %Z')
      '16:08:12 05/08/03 AEST'

   Em muitos sistemas Unix (incluindo *BSD, Linux, Solaris, e Darwin),
   é mais conveniente utilizar o banco de dados de informação de fuso
   do sistema (*tzfile(5)*) para especificar as regras de fuso
   horário. Para fazer isso, defina a variável de sistema "TZ" ao path
   do arquivo de dados requerido de fuso horários, relativo à raiz do
   banco de dados de fuso horário 'zoneinfo' do sistema, geralmente
   encontrado em "/usr/share/zoneinfo". Por exemplo, "'US/Eastern'",
   "'Australia/Melbourne'", "'Egypt'" ou "'Europe/Amsterdam'".

      >>> os.environ['TZ'] = 'US/Eastern'
      >>> time.tzset()
      >>> time.tzname
      ('EST', 'EDT')
      >>> os.environ['TZ'] = 'Egypt'
      >>> time.tzset()
      >>> time.tzname
      ('EET', 'EEST')


Constantes de ID de Relógio
===========================

Essas constantes são utilizadas como parâmetros para "clock_getres()"
e "clock_gettime()".

time.CLOCK_BOOTTIME

   Idêntica a "CLOCK_MONOTONIC", exceto por também incluir qualquer
   tempo que o sistema está suspenso.

   Isto permite que aplicações recebam um relógio monotônico
   consciente suspenso sem precisar lidar com as complicações de
   "CLOCK_REALTIME", que pode conter descontinuidades se o tempo é
   alterado utilizando "settimeofday()" ou algo semelhante.

   Disponibilidade: Linux >= 2.6.39.

   Adicionado na versão 3.7.

time.CLOCK_HIGHRES

   O Solaris OS possui um timer "CLOCK_HIGHRES" que tenta utilizar
   recursos otimizados do hardware, e pode fornecer resolução perto de
   nanossegundos. "CLOCK_HIGHRES" é o relógio nanoajustável de alta
   resolução.

   Disponibilidade: Solaris.

   Adicionado na versão 3.3.

time.CLOCK_MONOTONIC

   Relógio que não pode ser definido e representa um tempo monotônico
   desde um ponto de início não especificado.

   Disponibilidade: Unix.

   Adicionado na versão 3.3.

time.CLOCK_MONOTONIC_RAW

   Semelhante à "CLOCK_MONOTONIC", mas fornece acesso a um tempo bruto
   baseado em hardware que não está sujeito a ajustes NTP.

   Disponibilidade: Linux >= 2.6.28, macOS >= 10.12.

   Adicionado na versão 3.3.

time.CLOCK_MONOTONIC_RAW_APPROX

   Semelhante a "CLOCK_MONOTONIC_RAW", mas lê um armazenado pelo
   sistema no gerenciador de contexto e, portanto, tem menor precisão.

   Disponibilidade: macOS >= 10.12.

   Adicionado na versão 3.13.

time.CLOCK_PROCESS_CPUTIME_ID

   Timer de alta resolução por processo no CPU.

   Disponibilidade: Unix.

   Adicionado na versão 3.3.

time.CLOCK_PROF

   Timer de alta resolução por processo no CPU.

   Disponibilidade: FreeBSD, NetBSD >= 7, OpenBSD.

   Adicionado na versão 3.7.

time.CLOCK_TAI

   Tempo Atômico Internacional

   O sistema deve ter uma tabela de segundos bissextos para que possa
   fornecer a resposta correta. Softwares PTP ou NTP podem manter uma
   tabela de segundos bissextos.

   Disponibilidade: Linux.

   Adicionado na versão 3.9.

time.CLOCK_THREAD_CPUTIME_ID

   Relógio de tempo de CPU específico a thread.

   Disponibilidade: Unix.

   Adicionado na versão 3.3.

time.CLOCK_UPTIME

   Tempo cujo valor absoluto é o tempo que o sistema está sendo
   executado e não suspenso, fornecendo medidas de tempo de atividade
   precisas, tanto em valor absoluto quanto intervalo.

   Disponibilidade: FreeBSD, OpenBSD >= 5.5.

   Adicionado na versão 3.7.

time.CLOCK_UPTIME_RAW

   Relógio que incrementa de forma monotônica, contando o tempo desde
   um ponto arbitrário, não afetado pela frequência ou ajustes de
   tempo e não incrementado enquanto o sistema está dormindo.

   Disponibilidade: macOS >= 10.12.

   Adicionado na versão 3.8.

time.CLOCK_UPTIME_RAW_APPROX

   Semelhante a "CLOCK_UPTIME_RAW", mas o valor é armazenado pelo
   sistema no gerenciador de contexto e, portanto, tem menor precisão.

   Disponibilidade: macOS >= 10.12.

   Adicionado na versão 3.13.

A constante a seguir é o único parâmetro que pode ser enviado para
"clock_settime()".

time.CLOCK_REALTIME

   Relógio em tempo real. Configurar este relógio requer privilégios
   apropriados. O relógio é o mesmo para todos os processos.

   Disponibilidade: Unix.

   Adicionado na versão 3.3.


Constantes de Fuso Horário
==========================

time.altzone

   O deslocamento do fuso horário DST local, em segundos a oeste de
   UTC, se algum for fornecido. É negativo se o fuso horário DST local
   está a leste de UTC (como na Europa Ocidental, incluindo o Reino
   Unido). Somente utilize se "daylight" for diferente de zero. Veja a
   nota abaixo.

time.daylight

   Diferente de zero se um fuso horário DST é definido. Veja nota
   abaixo.

time.timezone

   O deslocamento para o fuso horário local (não DST), em segundos a
   oeste de UTC (negativo na maior parte da Europa Ocidental, positivo
   nos Estados Unidos e Brasil, zero no Reino Unido). Ver nota abaixo.

time.tzname

   A tupla de duas strings: A primeira é o nome do fuso horário local
   não DST, a segunda é o nome do fuso horário local DST. Se nenhum
   fuso horário DST for definido, a segunda string é usada. Veja nota
   abaixo.

Nota:

  Para as constantes de Fuso Horário acima ("altzone", "daylight",
  "timezone", e "tzname"), o valor é determinado pelas regras de fuso
  horário em efeito no módulo de carregamento de tempo ou a última vez
  que "tzset()" é chamada e pode estar incorreto para tempos no
  passado. É recomendado utilizar os resultados "tm_gmtoff" e
  "tm_zone" da "localtime()" para obter informação de fuso horário.

Ver também:

  Módulo "datetime"
     Mais interfaces orientada a objetos para datas e tempos.

  Módulo "locale"
     Serviços de internacionalização. A configuração de localidade
     afeta a interpretação de muitos especificadores de formato em
     "strftime()" e "strptime()".

  Módulo "calendar"
     Funções gerais relacionadas a calendários. "timegm()" é a função
     inversa de "gmtime()" deste módulo.

-[ Notas de rodapé ]-

[1] A utilização de "%Z" está descontinuada, mas o escape "%z" que
    expande para um deslocamento hora/minuto preferido não é suportado
    por todas as bibliotecas ANSI C. Além disso, a leitura do padrão
    original **RFC 822** de 1982 mostra que este pede um ano com dois
    dígitos ("%y" em vez de "%Y"), mas a prática consolidou a
    utilização de anos com 4 dígitos mesmo antes dos anos 2000. Após
    isso, o **RFC 822** tornou-se obsoleto e o ano de 4 dígitos foi
    primeiro recomendado por **RFC 1123** e depois obrigatório por
    **RFC 2822**, com **RFC 5322** continuando este requisito.
