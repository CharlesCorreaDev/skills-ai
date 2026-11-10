"datetime" --- Tipos básicos de data e hora
*******************************************

**Código-fonte:** Lib/datetime.py

======================================================================

O módulo "datetime" fornece classes para manipulação de datas e horas.

Ainda que a aritmética de data e hora seja suportada, o foco da
implementação é a extração eficiente de atributos para a formatação e
manipulação da saída.

Dica:

  Pule para os códigos de formatação.

Ver também:

  Módulo "calendar"
     Funções gerais relacionadas ao calendário.

  Módulo "time"
     Acesso e conversões de tempo

  Módulo "zoneinfo"
     Fusos horários concretos que representam o banco de dados de
     fusos horários da IANA.

  Pacote dateutil
     Biblioteca de terceiros com fuso horário expandido e suporte à
     análise.

  Pacote DateType
     Biblioteca de terceiros que apresenta tipos estáticos distintos
     para, por exemplo, permitir que *verificadores de tipo estático*
     diferenciem datas ingênuas e conscientes.


Aware and naive objects
=======================

Objetos de data e hora podem ser categorizados como "consciente" ou
"ingênuo" dependendo se eles incluem ou não informação sobre fuso
horário.

Com conhecimento suficiente dos ajustes de tempo algorítmicos e
políticos aplicáveis, como informações de fuso horário e horário de
verão, um objeto **consciente** pode se localizar em relação a outros
objetos conscientes. Um objeto consciente representa um momento
específico no tempo que não está aberto à interpretação. [1]

Um objeto **ingênuo** não contém informações suficientes para se
localizar inequivocamente em relação a outros objetos de data/hora. Se
um objeto ingênuo representa o Coordinated Universal Time (UTC), a
hora local, ou a hora em algum outro fuso horário, isso depende
exclusivamente do programa, assim como é tarefa do programa decidir se
um número específico representa metros, milhas ou massa. Objetos
ingênuos são fáceis de entender e trabalhar, com o custo de ignorar
alguns aspectos da realidade.

For applications requiring aware objects, "datetime" and "time"
objects have an optional time zone information attribute, "tzinfo",
that can be set to an instance of a subclass of the abstract "tzinfo"
class. These "tzinfo" objects capture information about the offset
from UTC time, the time zone name, and whether daylight saving time is
in effect.

Somente uma classe concreta "tzinfo", a classe "timezone", é fornecida
pelo módulo "datetime". A classe "timezone" pode representar fusos
horários simples com diferenças fixas do UTC, como o próprio UTC, ou
os fusos horários norte-americanos EST e EDT. O suporte a fusos
horários em níveis mais detalhados depende da aplicação. As regras
para ajuste de tempo em todo o mundo são mais políticas do que
racionais, mudam com frequência e não há um padrão adequado para todas
as aplicações além da UTC.


Constantes
==========

O módulo "datetime" exporta as seguintes constantes:

datetime.MINYEAR

   O menor número de ano permitido em um objeto "date" ou "datetime".
   "MINYEAR" é 1.

datetime.MAXYEAR

   O maior número de ano permitido no objeto "date" ou "datetime".
   "MAXYEAR" é 9999.

datetime.UTC

   Apelido para o singleton de fuso horário UTC
   "datetime.timezone.utc".

   Adicionado na versão 3.11.


Available types
===============

class datetime.date

   Uma data ingênua idealizada, presumindo que o atual calendário
   Gregoriano sempre foi, e sempre estará em vigor. Atributos: "year",
   "month" e "day".

class datetime.time

   Um horário ideal, independente de qualquer dia em particular,
   presumindo que todos os dias tenham exatamente 24*60*60 segundos.
   (Não há noção de "segundos bissextos" aqui.) Atributos: "hour",
   "minute", "second", "microsecond" e "tzinfo".

class datetime.datetime

   Uma combinação de uma data e uma hora. Atributos: "year", "month",
   "day", "hour", "minute", "second", "microsecond" e "tzinfo".

class datetime.timedelta

   Uma duração que expressa a diferença entre duas instâncias
   "datetime" ou "date" para resolução de microssegundos.

class datetime.tzinfo

   Uma classe base abstrata para objetos de informações de fuso
   horário. Eles são usados pelas classes "datetime" e "time" para
   fornecer uma noção personalizável de ajuste de horário (por
   exemplo, para considerar o fuso horário e/ou o horário de verão).

class datetime.timezone

   Uma classe que implementa a classe base abstrata "tzinfo" como uma
   diferença fixa do UTC.

   Adicionado na versão 3.2.

Objetos desse tipo são imutáveis.

Subclass relationships:

   [imagem: timedelta, tzinfo, time, and date inherit from object;
   timezone inherits from tzinfo; and datetime inherits from
   date.][imagem]


Common properties
-----------------

Os tipos "date", "datetime", "time" e "timezone" compartilham esses
recursos comuns:

* Objetos desse tipo são imutáveis.

* Objetos desses tipos são *hasheáveis*, o que significa que podem ser
  usados como chaves de dicionário.

* Objetos desse tipo suportam decapagem eficiente através do módulo
  "pickle".


Determining if an object is aware or naive
------------------------------------------

Objetos do tipo "date" são sempre ingênuos.

Um objeto do tipo "time" ou "datetime" pode ser consciente ou ingênuo.

A "datetime" object "d" is aware if "d.utcoffset()" does not return
"None". Otherwise, "d" is naive.

A "time" object "t" is aware if "t.utcoffset()" does not return
"None". Otherwise, "t" is naive.

A distinção entre consciente e ingênuo não se aplica a objetos
"timedelta".


"timedelta" objects
===================

O objeto "timedelta" representa uma duração, a diferença entre duas
instâncias "datetime" ou "date".

class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

   Todos os argumentos são opcionais e o padrão é 0. Os argumentos
   podem ser números inteiros ou ponto flutuantes, e podem ser
   positivos ou negativos.

   Apenas *days*, *seconds* e *microseconds* são armazenados
   internamente. Os argumentos são convertidos para essas unidades:

   * Um milissegundo é convertido em 1000 microssegundos.

   * Um minuto é convertido em 60 segundos.

   * Uma hora é convertida em 3600 segundos.

   * Uma semana é convertida para 7 dias.

   e dias, segundos e microssegundos são normalizados para que a
   representação seja única, com

   * "0 <= microseconds < 1000000"

   * "0 <= seconds < 3600*24" (o número de segundos em um dia)

   * "-999999999 <= days <= 999999999"

   O exemplo a seguir ilustra como quaisquer argumentos além de
   *days*, *seconds* e *microseconds* são "mesclados" e normalizados
   nos três atributos resultantes:

      >>> import datetime as dt
      >>> delta = dt.timedelta(
      ...     days=50,
      ...     seconds=27,
      ...     microseconds=10,
      ...     milliseconds=29000,
      ...     minutes=5,
      ...     hours=8,
      ...     weeks=2
      ... )
      >>> # Only days, seconds, and microseconds remain
      >>> delta
      datetime.timedelta(days=64, seconds=29156, microseconds=10)

   Dica:

     "import datetime as dt" instead of "import datetime" or "from
     datetime import datetime" to avoid confusion between the module
     and the class. See How I Import Python’s datetime Module.

   Se qualquer argumento for um ponto flutuante e houver
   microssegundos fracionários, os microssegundos fracionários
   restantes de todos os argumentos serão combinados e sua soma será
   arredondada para o microssegundo mais próximo usando o desempatador
   de metade da metade para o par. Se nenhum argumento é ponto
   flutuante, os processos de conversão e normalização são exatos
   (nenhuma informação é perdida).

   Se o valor normalizado de dias estiver fora do intervalo indicado,
   a exceção "OverflowError" é levantada.

   Observe que a normalização de valores negativos pode ser
   surpreendente a princípio. Por exemplo:

      >>> import datetime as dt
      >>> d = dt.timedelta(microseconds=-1)
      >>> (d.days, d.seconds, d.microseconds)
      (-1, 86399, 999999)

   Como a representação de string dos objetos "timedelta" pode ser
   confusa, use a seguinte receita para produzir um formato mais
   legível:

      >>> def pretty_timedelta(td):
      ...     if td.days >= 0:
      ...         return str(td)
      ...     return f'-({-td!s})'
      ...
      >>> d = timedelta(hours=-1)
      >>> str(d)  # not human-friendly
      '-1 day, 23:00:00'
      >>> pretty_timedelta(d)
      '-(1:00:00)'

Atributos de classe:

timedelta.min

   O mais negativo objeto "timedelta", "timedelta(-999999999)".

timedelta.max

   O mais positivo objeto "timedelta", "timedelta(days=999999999,
   hours=23, minutes=59, seconds=59, microseconds=999999)".

timedelta.resolution

   A menor diferença possível entre objetos não iguais "timedelta",
   "timedelta(microseconds=1)".

Observe que, devido à normalização, "timedelta.max" é maior que
"-timedelta.min". "-timedelta.max" não é representável como um objeto
"timedelta".

Atributos de instância (somente leitura):

timedelta.days

   Entre -999.999.999 e 999.999.999 inclusive

timedelta.seconds

   Entre 0 e 86.399 inclusive.

   Cuidado:

     É um bug relativamente comum utilizar este atributo de forma não
     intencional quando, na verdade, o objetivo é obter o valor de
     "total_seconds()":

        >>> import datetime as dt
        >>> duration = dt.timedelta(seconds=11235813)
        >>> duration.days, duration.seconds
        (130, 3813)
        >>> duration.total_seconds()
        11235813.0

timedelta.microseconds

   Entre 0 e 999.999 inclusive.

Operações suportadas:

+----------------------------------+-------------------------------------------------+
| Operação                         | Resultado                                       |
|==================================|=================================================|
| "t1 = t2 + t3"                   | Soma de "t2" e "t3". Depois "t1 - t2 == t3" e   |
|                                  | "t1 - t3 == t2" são verdadeiros. (1)            |
+----------------------------------+-------------------------------------------------+
| "t1 = t2 - t3"                   | Diferença de "t2" e "t3". Depois "t1 == t2 -    |
|                                  | t3" e "t2 == t1 + t3" são verdadeiros (1)(6)    |
+----------------------------------+-------------------------------------------------+
| "t1 = t2 * i or t1 = i * t2"     | Delta multiplicado por um número inteiro.       |
|                                  | Depois "t1 // i == t2" é verdadeiro, desde que  |
|                                  | "i != 0".                                       |
+----------------------------------+-------------------------------------------------+
|                                  | Em geral, "t1 * i == t1 * (i-1) + t1" é         |
|                                  | verdadeiro. (1)                                 |
+----------------------------------+-------------------------------------------------+
| "t1 = t2 * f or t1 = f * t2"     | Delta multiplicado por um float, ponto          |
|                                  | flutuante. O resultado é arredondado para o     |
|                                  | múltiplo mais próximo de timedelta.resolution   |
|                                  | usando a metade da metade para o par.           |
+----------------------------------+-------------------------------------------------+
| "f = t2 / t3"                    | Divisão (3) da duração total "t2" por unidade   |
|                                  | de intervalo "t3". Retorna um objeto "float".   |
+----------------------------------+-------------------------------------------------+
| "t1 = t2 / f or t1 = t2 / i"     | Delta dividido por um float ou um int. O        |
|                                  | resultado é arredondado para o múltiplo mais    |
|                                  | próximo de timedelta.resolution usando a metade |
|                                  | da metade para o par.                           |
+----------------------------------+-------------------------------------------------+
| "t1 = t2 // i" ou "t1 = t2 //    | O piso é calculado e o restante (se houver) é   |
| t3"                              | jogado fora. No segundo caso, um número inteiro |
|                                  | é retornado. (3)                                |
+----------------------------------+-------------------------------------------------+
| "t1 = t2 % t3"                   | O restante é calculado como um objeto           |
|                                  | "timedelta". (3)                                |
+----------------------------------+-------------------------------------------------+
| "q, r = divmod(t1, t2)"          | Calcula o quociente e o resto: "q = t1 // t2"   |
|                                  | (3) e "r = t1 % t2". "q" é um inteiro e "r" é   |
|                                  | um objeto "timedelta".                          |
+----------------------------------+-------------------------------------------------+
| "+t1"                            | Retorna um objeto "timedelta" com o mesmo       |
|                                  | valor. (2)                                      |
+----------------------------------+-------------------------------------------------+
| "-t1"                            | Equivalente a "timedelta(-t1.days, -t1.seconds, |
|                                  | -t1.microseconds)" e a "t1 * -1". (1)(4)        |
+----------------------------------+-------------------------------------------------+
| "abs(t)"                         | Equivalente a "+t" quando "t.days >= 0" e a     |
|                                  | "-t" quando "t.days < 0". (2)                   |
+----------------------------------+-------------------------------------------------+
| "str(t)"                         | Retorna uma string no formato "[D day[s],       |
|                                  | ][H]H:MM:SS[.UUUUUU]", onde D é negativo para   |
|                                  | "t" negativo. (5)                               |
+----------------------------------+-------------------------------------------------+
| "repr(t)"                        | Retorna uma representação em string do objeto   |
|                                  | "timedelta" como uma chamada do construtor com  |
|                                  | valores de atributos canônicos.                 |
+----------------------------------+-------------------------------------------------+

Notas:

1. Isso é exato, mas pode transbordar.

2. Isso é exato e não pode transbordar.

3. A divisão por zero levanta "ZeroDivisionError".

4. "-timedelta.max" não é representável como um objeto "timedelta".

5. As representações de string de objetos "timedelta" são normalizadas
   de maneira semelhante à sua representação interna. Isso leva a
   resultados um tanto incomuns para timedeltas negativos. Por
   exemplo:

      >>> timedelta(hours=-5)
      datetime.timedelta(days=-1, seconds=68400)
      >>> print(_)
      -1 day, 19:00:00

6. A expressão "t2 - t3" sempre será igual à expressão "t2 + (-t3)"
   exceto quando t3 for igual a "timedelta.max"; nesse caso, o
   primeiro produzirá um resultado enquanto o último transbordará.

Além das operações listadas acima, os objetos "timedelta" suportam
certas adições e subtrações com os objetos "date" e "datetime" (veja
abaixo).

Alterado na versão 3.2: Floor division and true division of a
"timedelta" object by another "timedelta" object are now supported, as
are remainder operations and the "divmod()" function. True division
and multiplication of a "timedelta" object by a "float" object are now
supported.

Objetos "timedelta" dão suporte a comparações de igualdade e ordem.

Em contexto booleano, um objeto "timedelta" é considerado verdadeiro
se, e somente se, não for igual a "timedelta(0)".

Métodos de instância:

timedelta.total_seconds()

   Return the total number of seconds contained in the duration.
   Equivalent to "td / timedelta(seconds=1)". For interval units other
   than seconds, use the division form directly (for example, "td /
   timedelta(microseconds=1)").

   Observe que, em intervalos de tempo muito grandes (mais de 270 anos
   na maioria das plataformas), esse método perde a precisão de
   microssegundos.

   Adicionado na versão 3.2.


Examples of usage: "timedelta"
------------------------------

Um exemplo adicional de normalização:

   >>> # Components of another_year add up to exactly 365 days
   >>> import datetime as dt
   >>> year = dt.timedelta(days=365)
   >>> another_year = dt.timedelta(weeks=40, days=84, hours=23,
   ...                             minutes=50, seconds=600)
   >>> year == another_year
   True
   >>> year.total_seconds()
   31536000.0

Exemplos de aritmética com "timedelta":

   >>> import datetime as dt
   >>> year = dt.timedelta(days=365)
   >>> ten_years = 10 * year
   >>> ten_years
   datetime.timedelta(days=3650)
   >>> ten_years.days // 365
   10
   >>> nine_years = ten_years - year
   >>> nine_years
   datetime.timedelta(days=3285)
   >>> three_years = nine_years // 3
   >>> three_years, three_years.days // 365
   (datetime.timedelta(days=1095), 3)


Objetos "date"
==============

Um objeto "date" representa uma data (ano, mês e dia) em um calendário
idealizado, o calendário gregoriano atual, estendido indefinidamente
em ambas as direções.

1º de janeiro do ano 1 é chamado de dia número 1, 2º de janeiro do ano
1 é chamado de dia número 2, e assim por diante. [2]

class datetime.date(year, month, day)

   Todos os argumentos são obrigatórios. Os argumentos devem ser
   números inteiros nos seguintes intervalos:

   * "MINYEAR <= year <= MAXYEAR"

   * "1 <= month <= 12"

   * "1 <= day <= número de dias no mês e ano fornecidos"

   Se um argumento fora desses intervalos for fornecido, a exceção
   "ValueError" é levantada.

Outros construtores, todos os métodos de classe:

classmethod date.today()

   Retorna a data local atual.

   Isso é equivalente a "date.fromtimestamp(time.time())".

classmethod date.fromtimestamp(timestamp)

   Return the local date corresponding to the POSIX *timestamp*, such
   as is returned by "time.time()".

   Isso pode levantar "OverflowError", se o registro de data e hora
   estiver fora do intervalo de valores suportados pela função C
   "localtime()" da plataforma, e em caso de falha "OSError" em
   "localtime()". É comum que isso seja restrito a anos de 1970 a
   2038. Observe que, em sistemas não POSIX que incluem segundos
   bissextos na sua notação de registro de data e hora, os segundos
   bissextos são ignorados por "fromtimestamp()".

   Alterado na versão 3.3: Levanta "OverflowError" ao invés de
   "ValueError" se o registro de data e hora estiver fora do intervalo
   de valores suportados pela plataforma C "localtime()" função.
   Levanta "OSError" ao invés de "ValueError" em falha de
   "localtime()" .

   Alterado na versão 3.15: Accepts any real number as *timestamp*,
   not only integer or float.

classmethod date.fromordinal(ordinal)

   Return the date corresponding to the proleptic Gregorian *ordinal*,
   where January 1 of year 1 has ordinal 1.

   "ValueError" é levantado a menos que "1 <= ordinal <=
   date.max.toordinal()". Para qualquer data "d",
   "date.fromordinal(d.toordinal()) == d".

classmethod date.fromisoformat(date_string)

   Retorna um "date" correspondendo a *date_string* dada em qualquer
   formato válido de ISO 8601, com as seguintes exceções:

   1. Datas de precisão reduzida não são atualmente suportadas ("YYYY-
      MM", "YYYY").

   2. Representações de data estendidas não são atualmente suportadas
      ("±YYYYYY-MM-DD").

   3. Atualmente, as datas ordinais não são suportadas ("YYYY-OOO").

   Exemplos:

      >>> import datetime as dt
      >>> dt.date.fromisoformat('2019-12-04')
      datetime.date(2019, 12, 4)
      >>> dt.date.fromisoformat('20191204')
      datetime.date(2019, 12, 4)
      >>> dt.date.fromisoformat('2021-W01-1')
      datetime.date(2021, 1, 4)

   Adicionado na versão 3.7.

   Alterado na versão 3.11: Anteriormente, este método tinha suporte
   apenas ao formato "YYYY-MM-DD".

classmethod date.fromisocalendar(year, week, day)

   Return a "date" corresponding to the ISO calendar date specified by
   *year*, *week* and *day*. This is the inverse of the function
   "date.isocalendar()".

   Adicionado na versão 3.8.

classmethod date.strptime(date_string, format)

   Retorna um "date" correspondente ao *date_string*, analisado
   conforme *format*. Isso equivale a:

      date(*(time.strptime(date_string, format)[0:3]))

   "ValueError" é levantado se o date_string e o format não puderem
   ser interpretados por "time.strptime()" ou se este retornar um
   valor que não é uma tupla temporal. Veja também strftime() and
   strptime() behavior e "date.fromisoformat()".

   Nota:

     If *format* specifies a day of month ("%d") without a year,
     "ValueError" is raised.  This is to avoid a quadrennial leap year
     bug in code seeking to parse only a month and day as the default
     year used in absence of one in the format is not a leap year. The
     workaround is to always include a year in your *format*.  If
     parsing *date_string* values that do not have a year, explicitly
     add a year that is a leap year before parsing:

        >>> import datetime as dt
        >>> date_string = "02/29"
        >>> when = dt.date.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
        >>> when.strftime("%B %d")
        'February 29'

   Adicionado na versão 3.14.

Atributos de classe:

date.min

   A data representável mais antiga, "date(MINYEAR, 1, 1)".

date.max

   A data representável mais tardia, "date(MAXYEAR, 12, 31)".

date.resolution

   A menor diferença possível entre objetos date não iguais,
   "timedelta(days=1)".

Atributos de instância (somente leitura):

date.year

   Entre "MINYEAR" e "MAXYEAR", incluindo os extremos.

date.month

   Entre 1 e 12, incluindo os extremos.

date.day

   Entre 1 e o número de dias do mês especificado no ano especificado.

Operações suportadas:

+---------------------------------+------------------------------------------------+
| Operação                        | Resultado                                      |
|=================================|================================================|
| "date2 = date1 + timedelta"     | "date2" terá "timedelta.days" dias após        |
|                                 | "date1". (1)                                   |
+---------------------------------+------------------------------------------------+
| "date2 = date1 - timedelta"     | Calcula "date2" de modo que "date2 + timedelta |
|                                 | == date1". (2)                                 |
+---------------------------------+------------------------------------------------+
| "timedelta = date1 - date2"     | (3)                                            |
+---------------------------------+------------------------------------------------+
| "date1 == date2" "date1 !=      | Comparação de igualdade. (4)                   |
| date2"                          |                                                |
+---------------------------------+------------------------------------------------+
| "date1 < date2" "date1 > date2" | Comparação de ordem. (5)                       |
| "date1 <= date2" "date1 >=      |                                                |
| date2"                          |                                                |
+---------------------------------+------------------------------------------------+

Notas:

1. *date2* é movida para frente no tempo se "timedelta.days > 0", ou
   para trás se "timedelta.days < 0". Posteriormente "date2 - date1 ==
   timedelta.days". "timedelta.seconds" e "timedelta.microseconds" são
   ignorados. A exceção "OverflowError" é levantada se "date2.year"
   for menor que "MINYEAR" ou maior que "MAXYEAR".

2. "timedelta.seconds" e "timedelta.microseconds" são ignoradas.

3. Isso é exato e não pode estourar. "timedelta.seconds" e
   "timedelta.microseconds" são 0, e "date2 + timedelta == date1"
   depois.

4. Objetos "date" são iguais se representam a mesma data.

   Objetos "date" que não são também instâncias "datetime" nunca são
   iguais a objetos "datetime", mesmo que representem a mesma data.

5. *date1* é considerado menor que *date2* quando *date1* precede
   *date2* no tempo. Em outras palavras, "date1 < date2" se e somente
   se "date1.toordinal() < date2.toordinal()".

   Order comparison between a "date" object that is not also a
   "datetime" instance and a "datetime" object raises "TypeError".

Alterado na versão 3.13: A comparação entre o objeto "datetime" e uma
instância da subclasse "date" que não é uma subclasse de "datetime"
não converte mais a última em "date", ignorando a parte horária e o
fuso horário. O comportamento padrão pode ser alterado substituindo os
métodos especiais de comparação nas subclasses.

Em contextos booleanos, todo objeto "date" é considerado verdadeiro.

Métodos de instância:

date.replace(year=self.year, month=self.month, day=self.day)

   Retorna um novo objeto "date" com os mesmos valores, mas com os
   parâmetros especificados atualizados.

   Exemplo:

      >>> import datetime as dt
      >>> d = dt.date(2002, 12, 31)
      >>> d.replace(day=26)
      datetime.date(2002, 12, 26)

   A função genérica "copy.replace()" também oferece suporte a objetos
   "date".

date.timetuple()

   Retorna uma "time.struct_time" tal como retornado por
   "time.localtime()".

   As horas, minutos e segundos são 0, e o sinalizador de horário de
   verão é -1.

   "d.timetuple()" é equivalente a:

      time.struct_time((d.year, d.month, d.day, 0, 0, 0, d.weekday(), yday, -1))

   sendo "yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1" o
   número do dia no ano atual, começando com 1 para 1º de janeiro.

date.toordinal()

   Retorna o ordinal proléptico gregoriano da data, considerando que
   1º de janeiro do ano 1 tem o ordinal 1. Para qualquer objeto "date"
   "d", "date.fromordinal(d.toordinal()) == d".

date.weekday()

   Retorna o dia da semana como um inteiro, onde Segunda é 0 e Domingo
   é 6. Por exemplo, "date(2002, 12, 4).weekday() == 2", uma Quarta-
   feira. Veja também "isoweekday()".

date.isoweekday()

   Retorna o dia da semana como um inteiro, onde Segunda é 1 e Domingo
   é 7. Por exemplo, "date(2002, 12, 4).isoweekday() == 3", uma
   Quarta-feira. Veja também "weekday()", "isocalendar()".

date.isocalendar()

   Retorna um objeto *tupla nomeada* com três componentes: "year",
   "week" e "weekday".

   O calendário ISO é uma variação amplamente usada do calendário
   gregoriano. [3]

   O ano ISO consiste de 52 ou 53 semanas completas, e onde uma semana
   começa na segunda-feira e termina no domingo. A primeira semana de
   um ano ISO é a primeira semana no calendário (Gregoriano) de um ano
   contendo uma quinta-feira. Isso é chamado de semana número 1, e o
   ano ISO dessa quinta-feira é o mesmo que o seu ano Gregoriano.

   Por exemplo, 2004 começa em uma quinta-feira, então a primeira
   semana do ano ISO 2004 começa na segunda-feira, 29 de dezembro de
   2003, e termina no domingo, 4 de janeiro de 2004:

      >>> import datetime as dt
      >>> dt.date(2003, 12, 29).isocalendar()
      datetime.IsoCalendarDate(year=2004, week=1, weekday=1)
      >>> dt.date(2004, 1, 4).isocalendar()
      datetime.IsoCalendarDate(year=2004, week=1, weekday=7)

   Alterado na versão 3.9: Resultado alterado de uma tupla para uma
   *tupla nomeada*.

date.isoformat()

   Retorna uma string representando a data no formato ISO 8601, "YYYY-
   MM-DD":

      >>> import datetime as dt
      >>> dt.date(2002, 12, 4).isoformat()
      '2002-12-04'

date.__str__()

   Para um data "d", "str(d)" é equivalente a "d.isoformat()".

date.ctime()

   Retorna uma string representando a data:

      >>> import datetime as dt
      >>> dt.date(2002, 12, 4).ctime()
      'Wed Dec  4 00:00:00 2002'

   "d.ctime()" é equivalente a:

      time.ctime(time.mktime(d.timetuple()))

   em plataformas em que a função C nativa "ctime()" (que é invocada
   pela função "time.ctime()", mas não pelo método "date.ctime()") se
   conforma com o padrão C.

date.strftime(format)

   Retorna uma string representando a data, controlado por uma string
   explícita de formatação. Códigos de formatação referenciando horas,
   minutos ou segundos irão ver valores 0. Veja também strftime() and
   strptime() behavior e "date.isoformat()".

date.__format__(format)

   O mesmo que "date.strftime()". Isso torna possível especificar uma
   string de formatação para o objeto "date" em literais de string
   formatados e ao usar "str.format()". Veja também strftime() and
   strptime() behavior e "date.isoformat()".


Examples of usage: "date"
-------------------------

Exemplo de contagem de dias para um evento:

   >>> import time
   >>> import datetime as dt
   >>> today = dt.date.today()
   >>> today
   datetime.date(2007, 12, 5)
   >>> today == dt.date.fromtimestamp(time.time())
   True
   >>> my_birthday = dt.date(today.year, 6, 24)
   >>> if my_birthday < today:
   ...     my_birthday = my_birthday.replace(year=today.year + 1)
   ...
   >>> my_birthday
   datetime.date(2008, 6, 24)
   >>> time_to_birthday = abs(my_birthday - today)
   >>> time_to_birthday.days
   202

Mais exemplos de uso da classe "date":

   >>> import datetime as dt
   >>> d = dt.date.fromordinal(730920) # 730920th day after 1. 1. 0001
   >>> d
   datetime.date(2002, 3, 11)

   >>> # Methods related to formatting string output
   >>> d.isoformat()
   '2002-03-11'
   >>> d.strftime("%d/%m/%y")
   '11/03/02'
   >>> d.strftime("%A %d. %B %Y")
   'Monday 11. March 2002'
   >>> d.ctime()
   'Mon Mar 11 00:00:00 2002'
   >>> 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
   'The day is 11, the month is March.'

   >>> # Methods for extracting 'components' under different calendars
   >>> t = d.timetuple()
   >>> for i in t:
   ...     print(i)
   2002                # year
   3                   # month
   11                  # day
   0
   0
   0
   0                   # weekday (0 = Monday)
   70                  # 70th day in the year
   -1
   >>> ic = d.isocalendar()
   >>> for i in ic:
   ...     print(i)
   2002                # ISO year
   11                  # ISO week number
   1                   # ISO day number ( 1 = Monday )

   >>> # A date object is immutable; all operations produce a new object
   >>> d.replace(year=2005)
   datetime.date(2005, 3, 11)


"datetime" objects
==================

Um objeto "datetime" é um único objeto contendo todas as informações
de um objeto "date" e um objeto "time".

Like a "date" object, "datetime" assumes the current Gregorian
calendar extended in both directions; like a "time" object, "datetime"
assumes there are exactly 3600*24 seconds in every day.

Construtor:

class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

   Os argumentos *year*, *month* e *day* são obrigatórios. *tzinfo*
   pode ser "None", ou uma instância de subclasse de "tzinfo". Os
   argumentos remanescentes devem ser inteiros nos seguintes
   intervalos:

   * "MINYEAR <= year <= MAXYEAR",

   * "1 <= month <= 12",

   * "1 <= day <= número de dias no mês e ano fornecidos",

   * "0 <= hour < 24",

   * "0 <= minute < 60",

   * "0 <= second < 60",

   * "0 <= microsecond < 1000000",

   * "fold in [0, 1]".

   Se um argumento fora desses intervalos for fornecido, a exceção
   "ValueError" é levantada.

   Alterado na versão 3.6: Adicionado o parâmetro *fold*.

Outros construtores, todos os métodos de classe:

classmethod datetime.today()

   Retorna a data e hora local atual, com o atributo "tzinfo" definido
   para "None".

   Equivalente a:

      datetime.fromtimestamp(time.time())

   Veja também "now()", "fromtimestamp()".

   Este método é funcionalmente equivalente a "now()", mas sem um
   parâmetro "tz".

classmethod datetime.now(tz=None)

   Retorna a data e hora local atual.

   Se o argumento opcional *tz* é "None" ou não especificado, isto é o
   mesmo que "today()", mas, se possível, fornece mais precisão do que
   pode ser obtido indo por um registro de data e hora da função
   "time.time()" (por exemplo, isto pode ser possível em plataformas
   que fornecem a função C "gettimeofday()").

   Se *tz* não for "None", ele deve ser uma instância de uma subclasse
   de "tzinfo", e a data e hora local atual são convertidas para o
   fuso horário de *tz*.

   Esta função é preferida ao invés de "today()" e "utcnow()".

   Nota:

     Chamadas subsequentes para "datetime.now()" podem retornar o
     mesmo instante, dependendo da precisão do relógio subjacente.

classmethod datetime.utcnow()

   Retorna a data e hora atual em UTC, com "tzinfo" como "None".

   Este é similar a "now()", mas retorna a data e hora atual em UTC,
   como um objeto "datetime" ingênuo. Um datetime UTC consciente pode
   ser obtido chamando "datetime.now(timezone.utc)". Veja também
   "now()".

   Aviso:

     Devido ao fato de objetos "datetime" ingênuos serem tratados por
     muitos métodos "datetime" como hora local, é preferível usar
     datetimes conscientes para representar horas em UTC. De tal
     forma, a maneira recomendada para criar um objeto representando a
     hora local em UTC é chamando "datetime.now(timezone.utc)".

   Descontinuado desde a versão 3.12: Use "datetime.now()" com "UTC".

classmethod datetime.fromtimestamp(timestamp, tz=None)

   Retorna a data e hora local correspondente ao registro de data e
   hora POSIX, como é retornado por "time.time()". Se o argumento
   opcional *tz* é "None" ou não especificado, o registro de data e
   hora é convertido para a data e hora local da plataforma, e o
   objeto "datetime" retornado é ingênuo.

   Se *tz* não for "None", ela deve ser uma instância de uma subclasse
   de "tzinfo", e o registro de data e hora é convertido para o fuso
   horário de *tz*.

   "fromtimestamp()" pode levantar "OverflowError", se o registro de
   data e hora estiver fora do intervalo de valores suportados pelas
   funções em C "localtime()" ou "gmtime()" da plataforma, e ocorrer
   uma falha de "OSError" em "localtime()" ou "gmtime()". É comum para
   isso ser restrito aos anos 1970 até 2038. Perceba que em sistemas
   não-POSIX que incluem segundos bissextos na sua notação de registro
   de data e hora, segundos bissextos são ignorados por
   "fromtimestamp()", e então é possível ter dois registros de data e
   hora com diferença de um segundo que apresentam objetos "datetime"
   idênticos. Este método é preferido sobre "utcfromtimestamp()".

   Alterado na versão 3.3: Levanta um "OverflowError" ao invés de
   "ValueError" se o registro de data e hora estiver fora do intervalo
   dos valores suportados pelas funções C "localtime()" ou "gmtime()"
   da plataforma. Levanta "OSError" ao invés de "ValueError" em falhas
   de "localtime()" ou "gmtime()".

   Alterado na versão 3.6: "fromtimestamp()" pode retornar instâncias
   com "fold" igual a 1.

   Alterado na versão 3.15: Accepts any real number as *timestamp*,
   not only integer or float.

classmethod datetime.utcfromtimestamp(timestamp)

   Retorna o "datetime" UTC correspondente ao registro de data e hora
   POSIX, com "tzinfo" setado para "None". (O objeto resultante é
   ingênuo.)

   Isso pode levantar "OverflowError", se o registro de data e hora
   estiver fora do intervalo de valores suportados pela função C
   "gmtime()" da plataforma, e em caso de falha "OSError" em
   "gmtime()". É comum que isso seja restrito a anos de 1970 a 2038.

   Para conseguir um objeto "datetime" consciente, chame
   "fromtimestamp()":

      datetime.fromtimestamp(timestamp, timezone.utc)

   Nas plataformas compatíveis com POSIX, é equivalente à seguinte
   expressão:

      datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=timestamp)

   com a exceção de que a última fórmula sempre dá suporte ao
   intervalo completo de anos: entre "MINYEAR" e "MAXYEAR" inclusive.

   Aviso:

     Devido ao fato de objetos "datetime" ingênuos serem tratados por
     muitos métodos "datetime" como hora local, é preferível usar
     datetimes conscientes para representar horas em UTC. De tal
     forma, a maneira recomendada para criar um objeto representando
     um registro de data e hora específico em UTC é chamando
     "datetime.fromtimestamp(timestamp, tz=timezone.utc)".

   Alterado na versão 3.3: Levanta "OverflowError" ao invés de
   "ValueError" se o registro de data e hora estiver fora do intervalo
   de valores suportados pela função C "gmtime()" da plataforma.
   Levanta "OSError" ao invés de "ValueError" em caso de falha
   "gmtime()".

   Alterado na versão 3.15: Accepts any real number as *timestamp*,
   not only integer or float.

   Descontinuado desde a versão 3.12: Use "datetime.fromtimestamp()"
   com "UTC".

classmethod datetime.fromordinal(ordinal)

   Retorna um "datetime" correspondente ao ordinal proléptico
   Gregoriano, onde 1º de janeiro do ano 1 tem ordinal 1. "ValueError"
   é levantado a não ser que "1 <= ordinal <=
   datetime.max.toordinal()". As horas, minutos, segundos e micro
   segundos do resultado são todos 0, e "tzinfo" é "None".

classmethod datetime.combine(date, time, tzinfo=time.tzinfo)

   Return a new "datetime" object whose date components are equal to
   the given "date" object's, and whose time components are equal to
   the given "time" object's. If the *tzinfo* argument is provided,
   its value is used to set the "tzinfo" attribute of the result,
   otherwise the "tzinfo" attribute of the *time* argument is used.
   If the *date* argument is a "datetime" object, its time components
   and "tzinfo" attributes are ignored.

   Para qualquer objeto "datetime" "d", "d ==
   datetime.combine(d.date(), d.time(), d.tzinfo)".

   Alterado na versão 3.6: Adicionado o argumento *tzinfo*.

classmethod datetime.fromisoformat(date_string)

   Retorna um "datetime" correspondendo a *date_string* em qualquer
   formato válido de ISO 8601, com as seguintes exceções:

   1. Os deslocamentos de fuso horário podem ter segundos
      fracionários.

   2. O separador "T" pode ser substituído por qualquer caractere
      unicode único.

   3. Horas e minutos fracionários não são suportados.

   4. Datas de precisão reduzida não são atualmente suportadas ("YYYY-
      MM", "YYYY").

   5. Representações de data estendidas não são atualmente suportadas
      ("±YYYYYY-MM-DD").

   6. Atualmente, as datas ordinais não são suportadas ("YYYY-OOO").

   Exemplos:

      >>> import datetime as dt
      >>> dt.datetime.fromisoformat('2011-11-04')
      datetime.datetime(2011, 11, 4, 0, 0)
      >>> dt.datetime.fromisoformat('20111104')
      datetime.datetime(2011, 11, 4, 0, 0)
      >>> dt.datetime.fromisoformat('2011-11-04T00:05:23')
      datetime.datetime(2011, 11, 4, 0, 5, 23)
      >>> dt.datetime.fromisoformat('2011-11-04T00:05:23Z')
      datetime.datetime(2011, 11, 4, 0, 5, 23, tzinfo=datetime.timezone.utc)
      >>> dt.datetime.fromisoformat('20111104T000523')
      datetime.datetime(2011, 11, 4, 0, 5, 23)
      >>> dt.datetime.fromisoformat('2011-W01-2T00:05:23.283')
      datetime.datetime(2011, 1, 4, 0, 5, 23, 283000)
      >>> dt.datetime.fromisoformat('2011-11-04 00:05:23.283')
      datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
      >>> dt.datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
      datetime.datetime(2011, 11, 4, 0, 5, 23, 283000, tzinfo=datetime.timezone.utc)
      >>> dt.datetime.fromisoformat('2011-11-04T00:05:23+04:00')
      datetime.datetime(2011, 11, 4, 0, 5, 23,
          tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))

   Adicionado na versão 3.7.

   Alterado na versão 3.11: Anteriormente, este método suportava
   apenas formatos que podiam ser emitidos por "date.isoformat()" ou
   "datetime.isoformat()".

classmethod datetime.fromisocalendar(year, week, day)

   Return a "datetime" corresponding to the ISO calendar date
   specified by *year*, *week* and *day*. The non-date components of
   the datetime are populated with their normal default values. This
   is the inverse of the function "datetime.isocalendar()".

   Adicionado na versão 3.8.

classmethod datetime.strptime(date_string, format)

   Retorna um "datetime" correspondente ao *date_string*, analisado de
   acordo com *format*.

   Se *format* não contiver microssegundos ou informações de fuso
   horário, isso é equivalente a:

      datetime(*(time.strptime(date_string, format)[0:6]))

   "ValueError" é levantado se o date_string e o format não puderem
   ser interpretados por "time.strptime()" ou se ele retorna um valor
   o qual não é uma tupla temporal. Veja também strftime() and
   strptime() behavior e "datetime.fromisoformat()".

   Alterado na versão 3.15: If *format* specifies a day of month
   ("%d") without a year, "ValueError" is raised.  This is to avoid a
   quadrennial leap year bug in code seeking to parse only a month and
   day as the default year used in absence of one in the format is not
   a leap year. The workaround is to always include a year in your
   *format*.  If parsing *date_string* values that do not have a year,
   explicitly add a year that is a leap year before parsing:

      >>> import datetime as dt
      >>> date_string = "02/29"
      >>> when = dt.datetime.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
      >>> when.strftime("%B %d")
      'February 29'

Atributos de classe:

datetime.min

   O primeiro "datetime" representável, "datetime(MINYEAR, 1, 1,
   tzinfo=None)".

datetime.max

   O último "datetime" representável, "datetime(MAXYEAR, 12, 31, 23,
   59, 59, 999999, tzinfo=None)".

datetime.resolution

   A menor diferença possível entre objetos "datetime" diferentes,
   "timedelta(microseconds=1)".

Atributos de instância (somente leitura):

datetime.year

   Entre "MINYEAR" e "MAXYEAR", incluindo os extremos.

datetime.month

   Entre 1 e 12, incluindo os extremos.

datetime.day

   Entre 1 e o número de dias do mês especificado no ano especificado.

datetime.hour

   No intervalo "range(24)".

datetime.minute

   No intervalo "range(60)".

datetime.second

   No intervalo "range(60)".

datetime.microsecond

   No intervalo "range(1000000)".

datetime.tzinfo

   O objeto passado como o argumento *tzinfo* do construtor
   "datetime", ou "None" se nada foi passado.

datetime.fold

   Entre "[0, 1]". Usado para desambiguar tempos reais durante um
   intervalo repetido. (Um intervalo repetido ocorre quando relógios
   são atrasados ao final do horário de verão ou quando a diferença
   UTC para o fuso horário atual é reduzida por razões políticas.) Os
   valores 0 e 1 representam, respectivamente, o primeiro e o segundo
   dos dois momentos com a mesma representação de tempo real.

   Adicionado na versão 3.6.

Operações suportadas:

+-----------------------------------------+----------------------------------+
| Operação                                | Resultado                        |
|=========================================|==================================|
| "datetime2 = datetime1 + timedelta"     | (1)                              |
+-----------------------------------------+----------------------------------+
| "datetime2 = datetime1 - timedelta"     | (2)                              |
+-----------------------------------------+----------------------------------+
| "timedelta = datetime1 - datetime2"     | (3)                              |
+-----------------------------------------+----------------------------------+
| "datetime1 == datetime2" "datetime1 !=  | Comparação de igualdade. (4)     |
| datetime2"                              |                                  |
+-----------------------------------------+----------------------------------+
| "datetime1 < datetime2" "datetime1 >    | Comparação de ordem. (5)         |
| datetime2" "datetime1 <= datetime2"     |                                  |
| "datetime1 >= datetime2"                |                                  |
+-----------------------------------------+----------------------------------+

1. "datetime2" representa a duração de "timedelta" removido de
   "datetime1", movendo o tempo para frente se "timedelta.days > 0",
   ou para trás se "timedelta.days < 0". O resultado tem o mesmo
   atributo "tzinfo" que o datetime de entrada, e "datetime2 -
   datetime1 == timedelta" após. "OverflowError" é levantada se
   "datetime2.year" fosse menor que "MINYEAR" ou maior que "MAXYEAR".
   Perceba que nenhum ajuste no fuso horário é feito mesmo se a
   entrada é um objeto consciente disso.

2. Computa o "datetime2" tal que "datetime2 + timedelta == datetime1".
   Assim como para adição, o resultado tem o mesmo atributo "tzinfo"
   que datetime de entrada, e nenhum ajuste de fuso horário é feito
   mesmo que a entrada seja consciente disso.

3. Subtraction of a "datetime" from a "datetime" is defined only if
   both operands are naive, or if both are aware. If one is aware and
   the other is naive, "TypeError" is raised.

   Se ambos são ingênuos, ou ambos são conscientes e tiverem o mesmo
   atributo "tzinfo", os atributos "tzinfo" são ignorados, e o
   resultado é um objeto "t" do tipo "timedelta", tal que "datetime2 +
   t == datetime1". Nenhum ajuste de fuso horário é feito neste caso.

   Se ambas são conscientes e têm atributos "tzinfo" diferentes, "a-b"
   age como se "a" e "b" tivessem sido primeiro convertidos para
   datetimes ingênuas em UTC. O resultado é "(a.replace(tzinfo=None) -
   a.utcoffset()) - (b.replace(tzinfo=None) - b.utcoffset())" exceto
   que a implementação nunca estoura.

4. Objetos "datetime" são iguais se representarem a mesma data e hora,
   levando em consideração o fuso horário.

   Naive and aware "datetime" objects are never equal.

   If both comparands are aware, and have the same "tzinfo" attribute,
   the "tzinfo" and "fold" attributes are ignored and the base
   datetimes are compared. If both comparands are aware and have
   different "tzinfo" attributes, the comparison acts as comparands
   were first converted to UTC datetimes except that the
   implementation never overflows. "datetime" instances in a repeated
   interval are never equal to "datetime" instances in other time
   zone.

5. *datetime1* é considerado menor que *datetime2* quando *datetime1*
   precede *datetime2* no tempo. levando em consideração o fuso
   horário.

   A comparação de ordens entre objetos "datetime" ingênuos e
   conscientes levanta "TypeError".

   Se ambos os comparandos forem conscientes e tiverem o mesmo
   atributo "tzinfo", os atributos "tzinfo" e "fold" serão ignorados e
   os datetimes base serão comparados. Se ambos os comparandos forem
   conscientes e tiverem atributos "tzinfo" diferentes, a comparação
   atua como se os comparandos fossem primeiro convertidos para
   datetimes UTC, exceto que a implementação nunca estoura.

Alterado na versão 3.3: Comparações de igualdade entre instâncias de
"datetime" conscientes e nativas não levantam "TypeError".

Alterado na versão 3.13: A comparação entre o objeto "datetime" e uma
instância da subclasse "date" que não é uma subclasse de "datetime"
não converte mais a última em "date", ignorando a parte horária e o
fuso horário. O comportamento padrão pode ser alterado substituindo os
métodos especiais de comparação nas subclasses.

Métodos de instância:

datetime.date()

   Retorna um objeto "date" com o mesmo ano, mês e dia.

datetime.time()

   Retorna um objeto "time" com a mesma hora, minuto, segundo,
   microssegundo e fold. O atributo "tzinfo" é "None". Veja também o
   método "timetz()".

   Alterado na versão 3.6: O valor fold é copiado para o objeto "time"
   retornado.

datetime.timetz()

   Retorna um objeto "time" com os mesmos atributos de hora, minuto,
   segundo, microssegundo, fold e tzinfo. Veja também o método
   "time()".

   Alterado na versão 3.6: O valor fold é copiado para o objeto "time"
   retornado.

datetime.replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)

   Return a new "datetime" object with the same attributes, but with
   specified parameters updated. Note that "tzinfo=None" can be
   specified to create a naive datetime from an aware datetime with no
   conversion of date and time data.

   Objetos "datetime" também são suportados pela função genérica
   "copy.replace()".

   Alterado na versão 3.6: Adicionado o parâmetro *fold*.

datetime.astimezone(tz=None)

   Retorna um objeto "datetime" com novo atributo "tzinfo" definido
   por *tz*, ajustando a data e hora de forma que o resultado seja o
   mesmo horário UTC que *self*, mas na hora local de *tz*.

   Se fornecido, *tz* deve ser uma instância de uma subclasse
   "tzinfo", e seus métodos "utcoffset()" e "dst()" não devem retornar
   "None". Se *self* for ingênuo, é presumido que ele representa o
   tempo no fuso horário do sistema.

   Se for chamado sem argumentos (ou com "tz=None") o fuso horário do
   sistema local é presumido como o fuso horário desejado. O atributo
   ".tzinfo" da instância datetime convertida será definido para uma
   instância de "timezone" com o nome da zona e um deslocamento obtido
   a partir do sistema operacional.

   Se "self.tzinfo" for *tz*, "self.astimezone(tz)" é igual a *self*:
   nenhum ajuste nos dados de data ou hora é realizado. Caso contrário
   o resultado é a hora local no fuso horário *tz*, representando a
   mesma hora UTC que *self*: depois "astz = dt.astimezone(tz)", "astz
   - astz.utcoffset()" terá os mesmos dados de data e hora que "dt -
   dt.utcoffset()".

   Se você quer meramente anexar um objeto "timezone" *tz* a um
   datetime *dt* sem ajustes de dados de data e hora, use
   "dt.replace(tzinfo=tz)". Se você meramente quer remover o objeto
   "timezone" de um datetime consciente *dt* sem conversão de dados de
   data e hora, use "dt.replace(tzinfo=None)".

   Perceba que o método padrão "tzinfo.fromutc()" pode ser substituído
   em uma subclasse "tzinfo" para afetar o resultado retornado por
   "astimezone()". Ignorando erros de letras maiúsculas/minúsculas,
   "astimezone()" funciona como:

      def astimezone(self, tz):
          if self.tzinfo is tz:
              return self
          # Converte self para UTC e anexa o novo objeto timezone.
          utc = (self - self.utcoffset()).replace(tzinfo=tz)
          # Converte o horário local de UTC para tz.
          return tz.fromutc(utc)

   Alterado na versão 3.3: *tz* agora pode ser omitido.

   Alterado na versão 3.6: O método "astimezone()" agora pode ser
   chamado em instâncias ingênuas que presumidamente representam a
   hora local do sistema.

datetime.utcoffset()

   Se "tzinfo" for "None", retorna "None", caso contrário retorna
   "self.tzinfo.utcoffset(self)", e levanta uma exceção se o segundo
   não retornar "None" ou um objeto "timedelta" com magnitude menor
   que um dia.

   Alterado na versão 3.7: A diferença UTC não é restrita a um número
   completo de minutos.

datetime.dst()

   Se "tzinfo" for "None", retorna "None", caso contrário retorna
   "self.tzinfo.dst(self)", e levanta uma exceção se o segundo não
   retornar "None" ou um objeto "timedelta" com magnitude menor que um
   dia.

   Alterado na versão 3.7: A diferença de horário de verão não é
   restrita a um número completo de minutos.

datetime.tzname()

   Se "tzinfo" for "None", retorna "None", caso contrário retorna
   "self.tzinfo.tzname(self)", levanta uma exceção se o segundo não
   retornar "None" ou um objeto string.

datetime.timetuple()

   Retorna uma "time.struct_time" tal como retornado por
   "time.localtime()".

   "d.timetuple()" é equivalente a:

      time.struct_time((d.year, d.month, d.day,
                        d.hour, d.minute, d.second,
                        d.weekday(), yday, dst))

   onde "yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1" é
   o número de dias dentro do ano atual, começando com 1 para 1º de
   janeiro. O sinalizador "tm_isdst" do resultado é definido conforme
   o método "dst()": "tzinfo" é "None" ou "dst()" retorna "None",
   "tm_isdst" é definido para "-1"; caso contrário se "dst()" retornar
   um valor diferente de zero, "tm_isdst" é definido para 1; caso
   contrário "tm_isdst" é definido para 0.

datetime.utctimetuple()

   Se a instância "datetime" "d" é ingênua, isto é o mesmo que
   "d.timetuple()", exceto que "tm_isdst" é forçado para 0,
   independentemente do que "d.dst()" retornar. O horário de verão
   nunca é afetado por um horário UTC.

   Se "d" é consciente, "d" é normalizado para horário UTC, subtraindo
   "d.utcoffset()", e um "time.struct_time" para o horário normalizado
   é retornado. "tm_isdst" é forçado para 0. Observe que uma exceção
   "OverflowError" pode ser levantada se "d.year" for "MINYEAR" ou
   "MAXYEAR" e os ajustes UTC ultrapassar o limite de um ano.

   Aviso:

     Por causa que objetos "datetime" ingênuos são tratados por muitos
     métodos "datetime" como hora local, é preferido usar datetimes
     conscientes para representar horários em UTC; como resultado,
     usar "datetime.utctimetuple()" pode dar resultados enganosos. Se
     você tem um "datetime" ingênuo representando UTC, use
     "datetime.replace(tzinfo=timezone.utc)" para torná-lo consciente,
     ponto no qual você pode usar "datetime.timetuple()".

datetime.toordinal()

   Retorna o ordinal proléptico gregoriano da data. o mesmo que
   "self.date().toordinal()".

datetime.timestamp()

   Retorna o registro de data e hora POSIX correspondente a instância
   "datetime". O valor de retorno é um "float" similar aquele
   retornado por "time.time()".

   Naive "datetime" instances are assumed to represent local time and
   this method relies on platform C functions to perform the
   conversion. Since "datetime" supports a wider range of values than
   the platform C functions on many platforms, this method may raise
   "OverflowError" or "OSError" for times far in the past or far in
   the future.

   Para instâncias conscientes de "datetime", o valor retornado é
   computado como:

      (dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()

   Nota:

     Não existe método para obter o timestamp POSIX diretamente de uma
     instância "datetime" ingênua representando tempo em UTC. Se a sua
     aplicação usa esta convenção e o fuso horário do seu sistema não
     está setado para UTC, você pode obter o registro de data e hora
     POSIX fornecendo "tzinfo=timezone.utc":

        timestamp = dt.replace(tzinfo=timezone.utc).timestamp()

     ou calculando o registro de data e hora diretamente:

        timestamp = (dt - datetime(1970, 1, 1)) / timedelta(seconds=1)

   Adicionado na versão 3.3.

   Alterado na versão 3.6: O método "timestamp()" usa o atributo
   "fold" para desambiguar os tempos durante um intervalo repetido.

   Alterado na versão 3.6: This method no longer relies on the
   platform C "mktime()" function to perform conversions.

datetime.weekday()

   Retorna o dia da semana como um inteiro, em que segunda-feira é 0 e
   domingo é 6. O mesmo que "self.date().weekday()". Veja também
   "isoweekday()".

datetime.isoweekday()

   Retorna o dia da semana como um inteiro, em que segunda-feira é 1 e
   domingo é 7. O mesmo que "self.date().isoweekday()". Veja também
   "weekday()", "isocalendar()".

datetime.isocalendar()

   Retorna uma *tupla nomeada* com três componentes: "year", "week" e
   "weekday". O mesmo que  "self.date().isocalendar()".

datetime.isoformat(sep='T', timespec='auto')

   Retorna uma string representando a data e o tempo no formato ISO
   8601:

   * "YYYY-MM-DDTHH:MM:SS.ffffff", se "microsecond" não é 0

   * "YYYY-MM-DDTHH:MM:SS", se "microsecond" é 0

   Se "utcoffset()" não retorna "None", uma string é adicionada com a
   diferença UTC:

   * "YYYY-MM-DDTHH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]", se
     "microsecond" não é 0

   * "YYYY-MM-DDTHH:MM:SS+HH:MM[:SS[.ffffff]]",  se "microsecond" é 0

   Exemplos:

      >>> import datetime as dt
      >>> dt.datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat()
      '2019-05-18T15:17:08.132263'
      >>> dt.datetime(2019, 5, 18, 15, 17, tzinfo=dt.timezone.utc).isoformat()
      '2019-05-18T15:17:00+00:00'

   O argumento opcional *sep* (por padrão, "'T'") é um separador de
   caractere único, colocado entre as porções de data e tempo do
   resultado. Por exemplo:

      >>> import datetime as dt
      >>> class TZ(dt.tzinfo):
      ...     """A time zone with an arbitrary, constant -06:39 offset."""
      ...     def utcoffset(self, when):
      ...         return dt.timedelta(hours=-6, minutes=-39)
      ...
      >>> dt.datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
      '2002-12-25 00:00:00-06:39'
      >>> dt.datetime(2009, 11, 27, microsecond=100, tzinfo=TZ()).isoformat()
      '2009-11-27T00:00:00.000100-06:39'

   O argumento opcional *timespec* especifica o número de componentes
   adicionais do tempo a incluir (o padrão é "'auto'"). Pode ser uma
   das seguintes strings:

   * "'auto'": O mesmo que "'seconds'" se "microsecond" é 0, o mesmo
     que "'microseconds'" caso contrário.

   * "'hours'": Inclui o atributo "hour" no formato de dois dígitos
     "HH".

   * "'minutes'": Inclui os atributos "hour" e "minute" no formato
     "HH:MM".

   * "'seconds'": Inclui os atributos  "hour", "minute" e "second" no
     formato "HH:MM:SS".

   * "'milliseconds'": Inclui o tempo completo, mas trunca a parte
     fracional dos segundos em milissegundos. Formato "HH:MM:SS.sss".

   * "'microseconds'": Inclui o tempo completo no formato
     "HH:MM:SS.ffffff".

   Nota:

     Componentes do tempo excluídos são truncados, não arredondados.

   A exceção "ValueError" vai ser levantada no caso de um argumento
   *timespec* inválido:

      >>> import datetime as dt
      >>> dt.datetime.now().isoformat(timespec='minutes')
      '2002-12-25T00:00'
      >>> my_datetime = dt.datetime(2015, 1, 1, 12, 30, 59, 0)
      >>> my_datetime.isoformat(timespec='microseconds')
      '2015-01-01T12:30:59.000000'

   Alterado na versão 3.6: Adicionado o  parâmetro *timespec*.

datetime.__str__()

   Para uma instância "datetime" "d", "str(d)" é equivalente a
   "d.isoformat(' ')".

datetime.ctime()

   Retorna uma string representando a data e hora:

      >>> import datetime as dt
      >>> dt.datetime(2002, 12, 4, 20, 30, 40).ctime()
      'Wed Dec  4 20:30:40 2002'

   A string de saída *não* irá incluir informações de fuso horário,
   independente de a entrada ser consciente ou ingênua.

   "d.ctime()" é equivalente a:

      time.ctime(time.mktime(d.timetuple()))

   em plataformas onde a função nativa em C "ctime()" (a qual
   "time.ctime()" invoca, mas a qual "datetime.ctime()" não invoca)
   conforma com o padrão C.

datetime.strftime(format)

   Retorna uma string representando a data e hora, controladas por uma
   string com formato explícito. Veja também strftime() and strptime()
   behavior e "datetime.isoformat()".

datetime.__format__(format)

   O mesmo que "datetime.strftime()". Isso torna possível especificar
   uma string de formatação para o objeto "datetime" em literais de
   string formatados e ao usar "str.format()". Veja também strftime()
   and strptime() behavior e "datetime.isoformat()".


Examples of usage: "datetime"
-----------------------------

Exemplos para trabalhar com objetos "datetime":

   >>> import datetime as dt

   >>> # Using datetime.combine()
   >>> d = dt.date(2005, 7, 14)
   >>> t = dt.time(12, 30)
   >>> dt.datetime.combine(d, t)
   datetime.datetime(2005, 7, 14, 12, 30)

   >>> # Using datetime.now()
   >>> dt.datetime.now()
   datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
   >>> dt.datetime.now(dt.timezone.utc)
   datetime.datetime(2007, 12, 6, 15, 29, 43, 79060, tzinfo=datetime.timezone.utc)

   >>> # Using datetime.strptime()
   >>> my_datetime = dt.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
   >>> my_datetime
   datetime.datetime(2006, 11, 21, 16, 30)

   >>> # Using datetime.timetuple() to get tuple of all attributes
   >>> tt = my_datetime.timetuple()
   >>> for it in tt:
   ...     print(it)
   ...
   2006    # year
   11      # month
   21      # day
   16      # hour
   30      # minute
   0       # second
   1       # weekday (0 = Monday)
   325     # number of days since 1st January
   -1      # dst - method tzinfo.dst() returned None

   >>> # Date in ISO format
   >>> ic = my_datetime.isocalendar()
   >>> for it in ic:
   ...     print(it)
   ...
   2006    # ISO year
   47      # ISO week
   2       # ISO weekday

   >>> # Formatting a datetime
   >>> my_datetime.strftime("%A, %d. %B %Y %I:%M%p")
   'Tuesday, 21. November 2006 04:30PM'
   >>> 'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(my_datetime, "day", "month", "time")
   'The day is 21, the month is November, the time is 04:30PM.'

O exemplo abaixo define uma subclasse "tzinfo" capturando informações
de fuso horário para Kabul, Afeganistão, o qual usou +4 UTC até 1945 e
depois +4:30 UTC após esse período:

   import datetime as dt

   class KabulTz(dt.tzinfo):
       # Kabul used +4 until 1945, when they moved to +4:30
       UTC_MOVE_DATE = dt.datetime(1944, 12, 31, 20, tzinfo=dt.timezone.utc)

       def utcoffset(self, when):
           if when.year < 1945:
               return dt.timedelta(hours=4)
           elif (1945, 1, 1, 0, 0) <= when.timetuple()[:5] < (1945, 1, 1, 0, 30):
               # An ambiguous ("imaginary") half-hour range representing
               # a 'fold' in time due to the shift from +4 to +4:30.
               # If when falls in the imaginary range, use fold to decide how
               # to resolve. See PEP 495.
               return dt.timedelta(hours=4, minutes=(30 if when.fold else 0))
           else:
               return dt.timedelta(hours=4, minutes=30)

       def fromutc(self, when):
           # Follow same validations as in datetime.tzinfo
           if not isinstance(when, dt.datetime):
               raise TypeError("fromutc() requires a datetime argument")
           if when.tzinfo is not self:
               raise ValueError("when.tzinfo is not self")

           # A custom implementation is required for fromutc as
           # the input to this function is a datetime with utc values
           # but with a tzinfo set to self.
           # See datetime.astimezone or fromtimestamp.
           if when.replace(tzinfo=dt.timezone.utc) >= self.UTC_MOVE_DATE:
               return when + dt.timedelta(hours=4, minutes=30)
           else:
               return when + dt.timedelta(hours=4)

       def dst(self, when):
           # Kabul does not observe daylight saving time.
           return dt.timedelta(0)

       def tzname(self, when):
           if when >= self.UTC_MOVE_DATE:
               return "+04:30"
           return "+04"

Uso de "KabulTz" mostrado acima:

   >>> tz1 = KabulTz()

   >>> # Datetime before the change
   >>> dt1 = dt.datetime(1900, 11, 21, 16, 30, tzinfo=tz1)
   >>> print(dt1.utcoffset())
   4:00:00

   >>> # Datetime after the change
   >>> dt2 = dt.datetime(2006, 6, 14, 13, 0, tzinfo=tz1)
   >>> print(dt2.utcoffset())
   4:30:00

   >>> # Convert datetime to another time zone
   >>> dt3 = dt2.astimezone(dt.timezone.utc)
   >>> dt3
   datetime.datetime(2006, 6, 14, 8, 30, tzinfo=datetime.timezone.utc)
   >>> dt2
   datetime.datetime(2006, 6, 14, 13, 0, tzinfo=KabulTz())
   >>> dt2 == dt3
   True


Objetos "time"
==============

Um objeto "time" representa a hora (local) do dia, independentemente
de um dia em particular, e sujeito a ajustes através de um objeto
"tzinfo".

class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

   Todos os argumentos são opcionais. *tzinfo* pode ser "None", ou uma
   instância de uma subclasse de "tzinfo". Os argumentos remanescentes
   devem ser inteiros nos seguintes intervalos:

   * "0 <= hour < 24",

   * "0 <= minute < 60",

   * "0 <= second < 60",

   * "0 <= microsecond < 1000000",

   * "fold in [0, 1]".

   Se um argumento fora desses intervalos for fornecido, "ValueError"
   é levantada. Todos têm o valor 0 como padrão, exceto *tzinfo*, que
   tem o valor padrão "None".

Atributos de classe:

time.min

   O "time" mais cedo que pode ser representado, "time(0, 0, 0, 0)".

time.max

   O "time" mais tardio que pode ser representado, "time(23, 59, 59,
   999999)".

time.resolution

   A menor diferença possível entre objetos "time" diferentes,
   "timedelta(microseconds=1)", embora perceba que aritmética sobre
   objetos "time" não é suportada.

Atributos de instância (somente leitura):

time.hour

   No intervalo "range(24)".

time.minute

   No intervalo "range(60)".

time.second

   No intervalo "range(60)".

time.microsecond

   No intervalo "range(1000000)".

time.tzinfo

   O objeto passado como argumento tzinfo para o construtor da classe
   "time", ou "None" se nada foi passado.

time.fold

   Entre "[0, 1]". Usado para desambiguar tempos reais durante um
   intervalo repetido. (Um intervalo repetido ocorre quando relógios
   são atrasados ao final do horário de verão ou quando a diferença
   UTC para o fuso horário atual é reduzida por razões políticas.) Os
   valores 0 e 1 representam, respectivamente, o primeiro e o segundo
   dos dois momentos com a mesma representação de tempo real.

   Adicionado na versão 3.6.

Objetos "time" oferecem suporte para comparações de igualdade e ordem,
onde "a" é considerado menor que "b" quando "a" precede "b" no tempo.

Objetos "time" ingênuos e conscientes nunca são iguais. A comparação
de ordem entre objetos "time" ingênuos e conscientes levanta
"TypeError".

Se ambos os comparandos são conscientes, e tem o mesmo atributo
"tzinfo", os atributos "tzinfo" e "fold" são ignorados e os tempos
base são comparados. Se ambos os comparandos são conscientes e tem
atributos "tzinfo" diferentes, os comparandos são primeiro ajustados
subtraindo sua diferença em UTC (obtida através de
"self.utcoffset()").

Alterado na versão 3.3: Comparações de igualdade entre instâncias de
"time" conscientes e nativas não levantam "TypeError".

Em contextos Booleanos, um objeto "time" é sempre considerado como
verdadeiro.

Alterado na versão 3.5: Before Python 3.5, a "time" object was
considered to be false if it represented midnight in UTC. This
behavior was considered obscure and error-prone and has been removed
in Python 3.5. See bpo-13936 for more information.

Outros construtores:

classmethod time.fromisoformat(time_string)

   Retorna um "time" correspondendo a *time_string* em qualquer
   formato válido de ISO 8601, com as seguintes exceções:

   1. Os deslocamentos de fuso horário podem ter segundos
      fracionários.

   2. O "T" inicial, normalmente exigido nos casos em que pode haver
      ambiguidade entre uma data e uma hora, não é necessário.

   3. Segundos fracionários podem ter qualquer número de dígitos (algo
      além de 6 será truncado).

   4. Horas e minutos fracionários não são suportados.

   Exemplos:

      >>> import datetime as dt
      >>> dt.time.fromisoformat('04:23:01')
      datetime.time(4, 23, 1)
      >>> dt.time.fromisoformat('T04:23:01')
      datetime.time(4, 23, 1)
      >>> dt.time.fromisoformat('T042301')
      datetime.time(4, 23, 1)
      >>> dt.time.fromisoformat('04:23:01.000384')
      datetime.time(4, 23, 1, 384)
      >>> dt.time.fromisoformat('04:23:01,000384')
      datetime.time(4, 23, 1, 384)
      >>> dt.time.fromisoformat('04:23:01+04:00')
      datetime.time(4, 23, 1, tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))
      >>> dt.time.fromisoformat('04:23:01Z')
      datetime.time(4, 23, 1, tzinfo=datetime.timezone.utc)
      >>> dt.time.fromisoformat('04:23:01+00:00')
      datetime.time(4, 23, 1, tzinfo=datetime.timezone.utc)

   Adicionado na versão 3.7.

   Alterado na versão 3.11: Anteriormente, este método suportava
   apenas formatos que podiam ser emitidos por "time.isoformat()".

classmethod time.strptime(date_string, format)

   Retorna um "time" correspondente ao *date_string*, analisado de
   acordo com *format*.

   Se *format* não contiver microssegundos ou informações de fuso
   horário, isso é equivalente a:

      time(*(time.strptime(date_string, format)[3:6]))

   "ValueError" é levantado se o *date_string* e o *format* não
   puderem ser interpretados por "time.strptime()" ou se ele retorna
   um valor o qual não é uma tupla temporal. Veja também strftime()
   and strptime() behavior e "time.fromisoformat()".

   Adicionado na versão 3.14.

Métodos de instância:

time.replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)

   Return a new "time" with the same values, but with specified
   parameters updated. Note that "tzinfo=None" can be specified to
   create a naive "time" from an aware "time", without conversion of
   the time data.

   Objetos "time" também são suportados pela função genérica
   "copy.replace()".

   Alterado na versão 3.6: Adicionado o parâmetro *fold*.

time.isoformat(timespec='auto')

   Retorna uma string representando a hora em formato ISO 8601, um
   destes:

   * "HH:MM:SS.ffffff", se "microsecond" não é 0

   * "HH:MM:SS", se "microsecond" é 0

   * "HH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]", se "utcoffset()" não
     retorna "None"

   * "HH:MM:SS+HH:MM[:SS[.ffffff]]", se "microsecond" é 0 e
     "utcoffset()" não retorna "None"

   O argumento opcional *timespec* especifica o número de componentes
   adicionais do tempo a incluir (o padrão é "'auto'"). Pode ser uma
   das seguintes strings:

   * "'auto'": O mesmo que "'seconds'" se "microsecond" é 0, o mesmo
     que "'microseconds'" caso contrário.

   * "'hours'": Inclui o atributo "hour" no formato de dois dígitos
     "HH".

   * "'minutes'": Inclui os atributos "hour" e "minute" no formato
     "HH:MM".

   * "'seconds'": Inclui os atributos  "hour", "minute" e "second" no
     formato "HH:MM:SS".

   * "'milliseconds'": Inclui o tempo completo, mas trunca a parte
     fracional dos segundos em milissegundos. Formato "HH:MM:SS.sss".

   * "'microseconds'": Inclui o tempo completo no formato
     "HH:MM:SS.ffffff".

   Nota:

     Componentes do tempo excluídos são truncados, não arredondados.

   "ValueError" será levantado com um argumento *timespec* inválido.

   Exemplo:

      >>> import datetime as dt
      >>> dt.time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')
      '12:34'
      >>> my_time = dt.time(hour=12, minute=34, second=56, microsecond=0)
      >>> my_time.isoformat(timespec='microseconds')
      '12:34:56.000000'
      >>> my_time.isoformat(timespec='auto')
      '12:34:56'

   Alterado na versão 3.6: Adicionado o  parâmetro *timespec*.

time.__str__()

   Para um tempo "t", "str(t)" é equivalente a "t.isoformat()".

time.strftime(format)

   Retorna uma string representando a hora, controladas por uma string
   com formato explícito. Veja também strftime() and strptime()
   behavior e "time.isoformat()".

time.__format__(format)

   O mesmo que "time.strftime()". Isso torna possível especificar uma
   string de formatação para o objeto "time" em literais de string
   formatados e ao usar "str.format()". Veja também strftime() and
   strptime() behavior e "time.isoformat()".

time.utcoffset()

   Se "tzinfo" for "None", retorna "None", caso contrário retorna
   "self.tzinfo.utcoffset(None)", e levanta uma exceção se o segundo
   não retornar "None" ou um objeto "timedelta" com magnitude menor
   que um dia.

   Alterado na versão 3.7: A diferença UTC não é restrita a um número
   completo de minutos.

time.dst()

   Se "tzinfo" for "None", retorna "None", caso contrário retorna
   "self.tzinfo.dst(None)", e levanta uma exceção se o segundo não
   retornar "None", ou um objeto "timedelta" com magnitude menor que
   um dia.

   Alterado na versão 3.7: A diferença de horário de verão não é
   restrita a um número completo de minutos.

time.tzname()

   Se "tzinfo" for "None", retorna "None", caso contrário retorna
   "self.tzinfo.tzname(None)", ou levanta uma exceção se o último caso
   não retornar "None" ou um objeto string.


Examples of usage: "time"
-------------------------

Exemplos para trabalhar com um objeto "time":

   >>> import datetime as dt
   >>> class TZ1(dt.tzinfo):
   ...     def utcoffset(self, when):
   ...         return dt.timedelta(hours=1)
   ...     def dst(self, when):
   ...         return dt.timedelta(0)
   ...     def tzname(self, when):
   ...         return "+01:00"
   ...     def  __repr__(self):
   ...         return f"{self.__class__.__name__}()"
   ...
   >>> t = dt.time(12, 10, 30, tzinfo=TZ1())
   >>> t
   datetime.time(12, 10, 30, tzinfo=TZ1())
   >>> t.isoformat()
   '12:10:30+01:00'
   >>> t.dst()
   datetime.timedelta(0)
   >>> t.tzname()
   '+01:00'
   >>> t.strftime("%H:%M:%S %Z")
   '12:10:30 +01:00'
   >>> 'The {} is {:%H:%M}.'.format("time", t)
   'The time is 12:10.'


"tzinfo" objects
================

class datetime.tzinfo

   This is an *abstract base class*, meaning that this class should
   not be instantiated directly.  Define a subclass of "tzinfo" to
   capture information about a particular time zone.

   An instance of (a concrete subclass of) "tzinfo" can be passed to
   the constructors for "datetime" and "time" objects. The latter
   objects view their attributes as being in local time, and the
   "tzinfo" object supports methods revealing offset of local time
   from UTC, the name of the time zone, and DST offset, all relative
   to a date or time object passed to them.

   You need to derive a concrete subclass, and (at least) supply
   implementations of the standard "tzinfo" methods needed by the
   "datetime" methods you use. The "datetime" module provides
   "timezone", a simple concrete subclass of "tzinfo" which can
   represent time zones with fixed offset from UTC such as UTC itself
   or North American EST and EDT.

   Requisito especial para preservação: uma subclasse "tzinfo" deve
   ter um método "__init__()" que pode ser chamado sem nenhum
   argumento, caso contrário ele pode ser conservado, mas não alterado
   novamente. Isso é um requisito técnico que pode ser relaxado no
   futuro.

   Uma subclasse concreta de "tzinfo" pode precisar implementar os
   seguintes métodos. Exatamente quais métodos são necessários depende
   do uso feito de objetos "datetime" conscientes. Se estiver em
   dúvida, simplesmente implemente todos eles.

tzinfo.utcoffset(dt)

   Retorna a diferença da hora local a partir do UTC, como um objeto
   "timedelta", que é positivo a leste do UTC. Se a hora local está a
   oeste do UTC, isto deve ser negativo.

   Isto representa a diferença *total* a partir de UTC; por exemplo,
   se um objeto "tzinfo" representa fuso horário e ajustes de horário
   de verão, "utcoffset()" deve retornar a soma deles. Se a diferença
   UTC não é conhecida, retorna "None". Caso contrário o valor
   retornado deve ser um objeto "timedelta" estritamente contido entre
   "-timedelta(hours=24)" e "timedelta(hours=24)" (a magnitude da
   diferença deve ser menor que um dia). A maior parte das
   implementações de "utcoffset()" irá provavelmente parecer com um
   destes dois:

      return CONSTANT                 # classe de posição fixa
      return CONSTANT + self.dst(dt)  # classe consciente de horário de verão

   Se "utcoffset()" não retorna "None", "dst()" também não deve
   retornar "None".

   A implementação padrão de "utcoffset()" levanta
   "NotImplementedError".

   Alterado na versão 3.7: A diferença UTC não é restrita a um número
   completo de minutos.

tzinfo.dst(dt)

   Retorna o ajuste para o horário de verão (DST - daylight saving
   time), como um objeto "timedelta" ou "None" se informação para o
   horário de verão é desconhecida.

   Retorna "timedelta(0)" se o horário de verão não estiver ativo. Se
   o horário de verão estiver ativo, retorna a diferença como um
   objeto "timedelta" (veja "utcoffset()" para detalhes). Perceba que
   a diferença do horário de verão, se aplicável, já foi adicionada a
   diferença UTC retornada por "utcoffset()", então não existe
   necessidade de consultar "dst()" a não ser que você esteja
   interessado em obter a informação de horário de verão
   separadamente. Por exemplo, "datetime.timetuple()" chama o método
   "dst()" do seu atributo "tzinfo" para determinar como o flag
   "tm_isdst" deve ser definido, e "tzinfo.fromutc()" chama "dst()"
   para contabilizar as mudanças de horário de verão quando ocorrem
   mudanças de fuso horário.

   Uma instância *tz* de uma subclasse "tzinfo" que modela tanto
   horário padrão quanto horário de verão deve ser consistente neste
   sentido:

   "tz.utcoffset(dt) - tz.dst(dt)"

   must return the same result for every "datetime" *dt* with
   "dt.tzinfo == tz". For sane "tzinfo" subclasses, this expression
   yields the time zone's "standard offset", which should not depend
   on the date or the time, but only on geographic location. The
   implementation of "datetime.astimezone()" relies on this, but
   cannot detect violations; it's the programmer's responsibility to
   ensure it. If a "tzinfo" subclass cannot guarantee this, it may be
   able to override the default implementation of "tzinfo.fromutc()"
   to work correctly with "astimezone()" regardless.

   Maior parte das implementações de "dst()" provavelmente irá parecer
   com um destes dois:

      import datetime as dt

      def dst(self, when):
          # a fixed-offset class:  doesn't account for DST
          return dt.timedelta(0)

   ou:

      import datetime as dt

      def dst(self, when):
          # Code to set dston and dstoff to the time zone's DST
          # transition times based on the input when.year, and expressed
          # in standard local time.

          if dston <= when.replace(tzinfo=None) < dstoff:
              return dt.timedelta(hours=1)
          else:
              return dt.timedelta(0)

   A implementação padrão de "dst()" levanta "NotImplementedError".

   Alterado na versão 3.7: A diferença de horário de verão não é
   restrita a um número completo de minutos.

tzinfo.tzname(dt)

   Return the time zone name corresponding to the "datetime" object
   *dt*, as a string. Nothing about string names is defined by the
   "datetime" module, and there's no requirement that it mean anything
   in particular. For example, ""GMT"", ""UTC"", ""-500"", ""-5:00"",
   ""EDT"", ""US/Eastern"", ""America/New York"" are all valid
   replies. Return "None" if a string name isn't known. Note that this
   is a method rather than a fixed string primarily because some
   "tzinfo" subclasses will wish to return different names depending
   on the specific value of *dt* passed, especially if the "tzinfo"
   class is accounting for daylight time.

   A implementação padrão de "tzname()" levanta "NotImplementedError".

These methods are called by a "datetime" or "time" object, in response
to their methods of the same names. A "datetime" object passes itself
as the argument, and a "time" object passes "None" as the argument. A
"tzinfo" subclass's methods should therefore be prepared to accept a
*dt* argument of "None", or of class "datetime".

Quando "None" é passado, cabe ao projetista da classe decidir a melhor
resposta. Por exemplo, retornar "None" é apropriado se a classe deseja
dizer que objetos time não participam nos protocolos da classe
"tzinfo". Pode ser mais útil para "utcoffset(None)" retornar a
diferença UTC padrão, como não existe outra convenção para descobrir a
diferença padrão.

When a "datetime" object is passed in response to a "datetime" method,
"dt.tzinfo" is the same object as *self*. "tzinfo" methods can rely on
this, unless user code calls "tzinfo" methods directly. The intent is
that the "tzinfo" methods interpret *dt* as being in local time, and
not need worry about objects in other time zones.

Existe mais um método "tzinfo" que uma subclasse pode desejar
substituição:

tzinfo.fromutc(dt)

   Isto é chamado a partir do padrão implementação de
   "datetime.astimezone()". Quando chamado a partir dele, "dt.tzinfo"
   é *self*, e os dados de data e hora de *dt* devem ser vistos como
   expressando um Horário Universal Coordenado (UTC). O propósito de
   "fromutc()" é ajustar os dados de data e hora, retornando um
   *datetime* equivalente na hora local de *self*.

   A maioria das subclasses de "tzinfo" deve ser capaz de herdar a
   implementação padrão de "fromutc()" sem problemas. Ela é robusta o
   suficiente para lidar com fusos horários de deslocamento fixo, e
   fusos horários que contabilizam tanto o horário padrão quanto o
   horário de verão, sendo que este último é tratado mesmo que os
   horários de transição do horário de verão sejam diferentes em anos
   distintos. Um exemplo de fuso horário que a implementação padrão de
   "fromutc()" pode não lidar corretamente em todos os casos é aquele
   onde o deslocamento padrão (de UTC) depende da data e hora
   específicas passadas, o que pode acontecer por razões políticas. As
   implementações padrão de "astimezone()" e "fromutc()" podem não
   produzir o resultado desejado se o resultado estiver entre as horas
   que abrangem o momento em que o deslocamento padrão muda.

   Ignorando o código para casos de erros, a implementação padrão
   "fromutc()" funciona como:

      import datetime as dt

      def fromutc(self, when):
          # raise ValueError error if when.tzinfo is not self
          dtoff = when.utcoffset()
          dtdst = when.dst()
          # raise ValueError if dtoff is None or dtdst is None
          delta = dtoff - dtdst  # this is self's standard offset
          if delta:
              when += delta   # convert to standard local time
              dtdst = when.dst()
              # raise ValueError if dtdst is None
          if dtdst:
              return when + dtdst
          else:
              return when

No seguinte arquivo "tzinfo_examples.py" existem alguns exemplos de
classes "tzinfo":

   import datetime as dt

   # A class capturing the platform's idea of local time.
   # (May result in wrong values on historical times in
   #  timezones where UTC offset and/or the DST rules had
   #  changed in the past.)
   import time

   ZERO = dt.timedelta(0)
   HOUR = dt.timedelta(hours=1)
   SECOND = dt.timedelta(seconds=1)

   STDOFFSET = dt.timedelta(seconds=-time.timezone)
   if time.daylight:
       DSTOFFSET = dt.timedelta(seconds=-time.altzone)
   else:
       DSTOFFSET = STDOFFSET

   DSTDIFF = DSTOFFSET - STDOFFSET


   class LocalTimezone(dt.tzinfo):

       def fromutc(self, when):
           assert when.tzinfo is self
           stamp = (when - dt.datetime(1970, 1, 1, tzinfo=self)) // SECOND
           args = time.localtime(stamp)[:6]
           dst_diff = DSTDIFF // SECOND
           # Detect fold
           fold = (args == time.localtime(stamp - dst_diff))
           return dt.datetime(*args, microsecond=when.microsecond,
                              tzinfo=self, fold=fold)

       def utcoffset(self, when):
           if self._isdst(when):
               return DSTOFFSET
           else:
               return STDOFFSET

       def dst(self, when):
           if self._isdst(when):
               return DSTDIFF
           else:
               return ZERO

       def tzname(self, when):
           return time.tzname[self._isdst(when)]

       def _isdst(self, when):
           tt = (when.year, when.month, when.day,
                 when.hour, when.minute, when.second,
                 when.weekday(), 0, 0)
           stamp = time.mktime(tt)
           tt = time.localtime(stamp)
           return tt.tm_isdst > 0


   Local = LocalTimezone()


   # A complete implementation of current DST rules for major US time zones.

   def first_sunday_on_or_after(when):
       days_to_go = 6 - when.weekday()
       if days_to_go:
           when += dt.timedelta(days_to_go)
       return when


   # US DST Rules
   #
   # This is a simplified (i.e., wrong for a few cases) set of rules for US
   # DST start and end times. For a complete and up-to-date set of DST rules
   # and timezone definitions, visit the Olson Database (or try pytz):
   # http://www.twinsun.com/tz/tz-link.htm
   # https://sourceforge.net/projects/pytz/ (might not be up-to-date)
   #
   # In the US, since 2007, DST starts at 2am (standard time) on the second
   # Sunday in March, which is the first Sunday on or after Mar 8.
   DSTSTART_2007 = dt.datetime(1, 3, 8, 2)
   # and ends at 2am (DST time) on the first Sunday of Nov.
   DSTEND_2007 = dt.datetime(1, 11, 1, 2)
   # From 1987 to 2006, DST used to start at 2am (standard time) on the first
   # Sunday in April and to end at 2am (DST time) on the last
   # Sunday of October, which is the first Sunday on or after Oct 25.
   DSTSTART_1987_2006 = dt.datetime(1, 4, 1, 2)
   DSTEND_1987_2006 = dt.datetime(1, 10, 25, 2)
   # From 1967 to 1986, DST used to start at 2am (standard time) on the last
   # Sunday in April (the one on or after April 24) and to end at 2am (DST time)
   # on the last Sunday of October, which is the first Sunday
   # on or after Oct 25.
   DSTSTART_1967_1986 = dt.datetime(1, 4, 24, 2)
   DSTEND_1967_1986 = DSTEND_1987_2006


   def us_dst_range(year):
       # Find start and end times for US DST. For years before 1967, return
       # start = end for no DST.
       if 2006 < year:
           dststart, dstend = DSTSTART_2007, DSTEND_2007
       elif 1986 < year < 2007:
           dststart, dstend = DSTSTART_1987_2006, DSTEND_1987_2006
       elif 1966 < year < 1987:
           dststart, dstend = DSTSTART_1967_1986, DSTEND_1967_1986
       else:
           return (dt.datetime(year, 1, 1), ) * 2

       start = first_sunday_on_or_after(dststart.replace(year=year))
       end = first_sunday_on_or_after(dstend.replace(year=year))
       return start, end


   class USTimeZone(dt.tzinfo):

       def __init__(self, hours, reprname, stdname, dstname):
           self.stdoffset = dt.timedelta(hours=hours)
           self.reprname = reprname
           self.stdname = stdname
           self.dstname = dstname

       def __repr__(self):
           return self.reprname

       def tzname(self, when):
           if self.dst(when):
               return self.dstname
           else:
               return self.stdname

       def utcoffset(self, when):
           return self.stdoffset + self.dst(when)

       def dst(self, when):
           if when is None or when.tzinfo is None:
               # An exception may be sensible here, in one or both cases.
               # It depends on how you want to treat them.  The default
               # fromutc() implementation (called by the default astimezone()
               # implementation) passes a datetime with when.tzinfo is self.
               return ZERO
           assert when.tzinfo is self
           start, end = us_dst_range(when.year)
           # Can't compare naive to aware objects, so strip the timezone from
           # when first.
           when = when.replace(tzinfo=None)
           if start + HOUR <= when < end - HOUR:
               # DST is in effect.
               return HOUR
           if end - HOUR <= when < end:
               # Fold (an ambiguous hour): use when.fold to disambiguate.
               return ZERO if when.fold else HOUR
           if start <= when < start + HOUR:
               # Gap (a non-existent hour): reverse the fold rule.
               return HOUR if when.fold else ZERO
           # DST is off.
           return ZERO

       def fromutc(self, when):
           assert when.tzinfo is self
           start, end = us_dst_range(when.year)
           start = start.replace(tzinfo=self)
           end = end.replace(tzinfo=self)
           std_time = when + self.stdoffset
           dst_time = std_time + HOUR
           if end <= dst_time < end + HOUR:
               # Repeated hour
               return std_time.replace(fold=1)
           if std_time < start or dst_time >= end:
               # Standard time
               return std_time
           if start <= std_time < end - HOUR:
               # Daylight saving time
               return dst_time


   Eastern  = USTimeZone(-5, "Eastern",  "EST", "EDT")
   Central  = USTimeZone(-6, "Central",  "CST", "CDT")
   Mountain = USTimeZone(-7, "Mountain", "MST", "MDT")
   Pacific  = USTimeZone(-8, "Pacific",  "PST", "PDT")

Perceba que existem sutilezas inevitáveis duas vezes por ano em uma
subclasse "tzinfo" contabilizando tanto hora normal e horário de
verão, nos pontos de transição do horário de verão. Para concretude,
considere a costa leste dos EUA (UTC -0500), onde o horário de verão
EDT começa no minuto após 1:59 (EST, hora padrão) no segundo domingo
de Março, e termina no minuto posterior a 1:59 (EDT, horário de verão)
no primeiro domingo de Novembro:

     UTC   3:MM  4:MM  5:MM  6:MM  7:MM  8:MM
     EST  22:MM 23:MM  0:MM  1:MM  2:MM  3:MM
     EDT  23:MM  0:MM  1:MM  2:MM  3:MM  4:MM

   start  22:MM 23:MM  0:MM  1:MM  3:MM  4:MM

     end  23:MM  0:MM  1:MM  1:MM  2:MM  3:MM

Quando o horário de verão inicia (a linha de "início"), o relógio de
parede local salta de 1:59 para 3:00. Um horário de parede da forma
2:MM realmente não faz sentido nesse dia, então "astimezone(Eastern)"
não irá entregar um resultado com "hour == 2" no dia que o horário de
verão começar. Por exemplo, na primavera de transição para frente em
2016, nós tivemos:

   >>> import datetime as dt
   >>> from tzinfo_examples import HOUR, Eastern
   >>> u0 = dt.datetime(2016, 3, 13, 5, tzinfo=dt.timezone.utc)
   >>> for i in range(4):
   ...     u = u0 + i*HOUR
   ...     t = u.astimezone(Eastern)
   ...     print(u.time(), 'UTC =', t.time(), t.tzname())
   ...
   05:00:00 UTC = 00:00:00 EST
   06:00:00 UTC = 01:00:00 EST
   07:00:00 UTC = 03:00:00 EDT
   08:00:00 UTC = 04:00:00 EDT

Quando o horário de verão termina (a linha "end"), há um problema
potencialmente pior: existe uma hora que não pode ser expressa de
forma inequívoca no horário local: a última hora do horário de verão.
No fuso Eastern, isso corresponde a horários no formato 5:MM UTC no
dia em que o horário de verão termina. O relógio de parede local salta
de 1:59 (horário de verão) para 1:00 (horário padrão) novamente.
Horários locais no formato 1:MM são ambíguos. "astimezone()" imita o
comportamento do relógio local mapeando então duas horas UTC
adjacentes para a mesma hora local. No exemplo do fuso Eastern,
horários UTC no formato 5:MM e 6:MM ambos se transformam em 1:MM
quando convertidos para o fuso Eastern, mas os horários anteriores têm
o atributo "fold" definido como 0 e os horários posteriores têm o
atributo definido como 1. Por exemplo, na transição de retorno de
2016, obtemos:

   >>> import datetime as dt
   >>> from tzinfo_examples import HOUR, Eastern
   >>> u0 = dt.datetime(2016, 11, 6, 4, tzinfo=dt.timezone.utc)
   >>> for i in range(4):
   ...     u = u0 + i*HOUR
   ...     t = u.astimezone(Eastern)
   ...     print(u.time(), 'UTC =', t.time(), t.tzname(), t.fold)
   ...
   04:00:00 UTC = 00:00:00 EDT 0
   05:00:00 UTC = 01:00:00 EDT 0
   06:00:00 UTC = 01:00:00 EST 1
   07:00:00 UTC = 02:00:00 EST 0

Observe que as instâncias de "datetime" que diferem apenas pelo valor
do atributo "fold" são consideradas iguais nas comparações.

Applications that can't bear wall-time ambiguities should explicitly
check the value of the "fold" attribute or avoid using hybrid "tzinfo"
subclasses; there are no ambiguities when using "timezone", or any
other fixed-offset "tzinfo" subclass (such as a class representing
only EST (fixed offset -5 hours), or only EDT (fixed offset -4
hours)).

Ver também:

     "zoneinfo"
        O módulo "datetime" possui uma classe básica "timezone" (para
        lidar com deslocamentos fixos arbitrários do UTC) e seu
        atributo "timezone.utc" (uma instância UTC "timezone" ).

        "zoneinfo" traz o *banco de dados de fuso horário IANA*
        (também conhecido como banco de dados Olson) para Python, e
        seu uso é recomendado.

  Banco de dados de fuso horário da IANA
     O banco de dados de fuso horário (comumente chamado de tz, tzdata
     ou zoneinfo) contém código e dados que representam o histórico de
     hora local para muitas localizações representativas ao redor do
     globo. Ele é atualizado periodicamente para refletir mudanças
     feitas por corpos políticos para limites de fuso horário,
     diferenças UTC, e regras de horário de verão.


"timezone" objects
==================

A classe "timezone" é uma subclasse de "tzinfo", cada instância da
qual representa um fuso horário definido por um deslocamento fixo do
UTC.

Objetos desta classe não podem ser usados para representar informações
de fuso horário em locais onde diferentes deslocamentos são usados em
diferentes dias do ano ou onde mudanças históricas foram feitas no
horário civil.

class datetime.timezone(offset[, name])

   O argumento *offset* deve ser especificado como um objeto
   "timedelta" representando a diferença entre o tempo local e o UTC.
   Ele deve estar estritamente entre "-timedelta(hours=24)" e
   "timedelta(hous=24)", caso contrário a exceção "ValueError" será
   provocada.

   O argumento *name* é opcional. Se especificado, deve ser uma string
   que será usada como o valor retornado pelo método
   "datetime.tzname()".

   Adicionado na versão 3.2.

   Alterado na versão 3.7: A diferença UTC não é restrita a um número
   completo de minutos.

timezone.utcoffset(dt)

   Retorna o valor fixo especificado quando a instância "timezone" é
   construída.

   O argumento *dt* é ignorado. O valor de retorno é uma instância
   "timedelta" equivalente à diferença entre o tempo local e o UTC.

   Alterado na versão 3.7: A diferença UTC não é restrita a um número
   completo de minutos.

timezone.tzname(dt)

   Retorna o valor fixo especificado quando a instância "timezone" é
   construída.

   Se *name* não é passado ao construtor, o nome retornado por
   "tzname(dt)" é gerado a partir do valor de "offset" do seguinte
   modo: Se *offset* é "timedelta(0)", o nome é "UTC", caso contrário
   é uma string no formato "UTC±HH:MM", na qual ± é o sinal do
   "offset", HH e MM são dois dígitos de "offset.hours" e
   "offset.minutes" respectivamente.

   Alterado na versão 3.6: Nome gerado de "offset=timedelta(0)" é
   agora simplesmente "'UTC'", não "'UTC+00:00'".

timezone.dst(dt)

   Sempre retorna "None".

timezone.fromutc(dt)

   Retorna "dt + offset". O argumento *dt* deve ser uma instância
   "datetime" consciente, com "tzinfo" definida para "self".

Atributos de classe:

timezone.utc

   O fuso horário UTC, "timezone(timedelta(0))".


"strftime()" and "strptime()" behavior
======================================

Todos os objetos "date", "datetime" e "time" dão suporte ao método
"strftime(format)", para criar uma string representando o tempo sob o
controle de uma string de formatação explícita.

Em recíproca, os métodos de classe "date.strptime()",
"datetime.strptime()" e "time.strptime()" criam um objeto a partir de
uma string representando o tempo e uma string de formatação
correspondente.

A tabela abaixo fornece uma comparação de alto nível entre
"strftime()" e "strptime()":

+------------------+----------------------------------------------------------+--------------------------------------------------------------+
|                  | "strftime"                                               | "strptime"                                                   |
|==================|==========================================================|==============================================================|
| Uso              | Converte objeto para uma string conforme um formato      | Interpreta uma string como um objeto dado um formato         |
|                  | fornecido                                                | correspondente                                               |
+------------------+----------------------------------------------------------+--------------------------------------------------------------+
| Tipo de método   | Método de instância                                      | Método de classe                                             |
+------------------+----------------------------------------------------------+--------------------------------------------------------------+
| Assinatura       | "strftime(format)"                                       | "strptime(date_string, format)"                              |
+------------------+----------------------------------------------------------+--------------------------------------------------------------+


"strftime()" and "strptime()" format codes
------------------------------------------

Esses métodos aceitam códigos de formato que podem ser usados para
analisar e formatar datas:

   >>> import datetime as dt
   >>> dt.datetime.strptime('31/01/22 23:59:59.999999',
   ...                      '%d/%m/%y %H:%M:%S.%f')
   datetime.datetime(2022, 1, 31, 23, 59, 59, 999999)
   >>> _.strftime('%a %d %b %Y, %I:%M%p')
   'Mon 31 Jan 2022, 11:59PM'

The following is a list of all the format codes that the 2011 C
standard requires, and these work on all supported platforms.

+-------------+----------------------------------+--------------------------+---------+
| Diretiva    | Significado                      | Exemplo                  | Notas   |
|=============|==================================|==========================|=========|
| "%a"        | Dias da semana como nomes        | Sun, Mon, ..., Sat       | (1)     |
|             | abreviados da localidade.        | (en_US); So, Mo, ..., Sa |         |
|             |                                  | (de_DE)                  |         |
+-------------+----------------------------------+--------------------------+---------+
| "%A"        | Dia da semana como nome completo | Sunday, Monday, ...,     | (1)     |
|             | da localidade.                   | Saturday (en_US);        |         |
|             |                                  | Sonntag, Montag, ...,    |         |
|             |                                  | Samstag (de_DE)          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%b"        | Mês como nome da localidade      | Jan, Feb, ..., Dec       | (1)     |
|             | abreviado.                       | (en_US); Jan, Feb, ...,  |         |
|             |                                  | Dez (de_DE)              |         |
+-------------+----------------------------------+--------------------------+---------+
| "%B"        | Mês como nome completo da        | January, February, ...,  | (1)     |
|             | localidade.                      | December (en_US);        |         |
|             |                                  | janeiro, fevereiro, ..., |         |
|             |                                  | dezembro (pt_BR)         |         |
+-------------+----------------------------------+--------------------------+---------+
| "%c"        | Representação de data e hora     | Tue Aug 16 21:30:00 1988 | (1)     |
|             | apropriada da localidade.        | (en_US); Di 16 Aug       |         |
|             |                                  | 21:30:00 1988 (de_DE)    |         |
+-------------+----------------------------------+--------------------------+---------+
| "%C"        | The year divided by 100 and      | 01, 02, ..., 99          | (0)     |
|             | truncated to an integer as a     |                          |         |
|             | zero-padded decimal number.      |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%d"        | Dia do mês como um número        | 01, 02, ..., 31          | (9),    |
|             | decimal com zeros a esquerda.    |                          | (10)    |
+-------------+----------------------------------+--------------------------+---------+
| "%D"        | Equivalent to "%m/%d/%y".        | 11/28/25                 | (9)     |
+-------------+----------------------------------+--------------------------+---------+
| "%e"        | The day of the month as a space- | ␣1, ␣2, ..., 31          | (10)    |
|             | padded decimal number.           |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%F"        | Equivalent to "%Y-%m-%d", the    | 2025-10-11, 1001-12-30   |         |
|             | ISO 8601 format.                 |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%g"        | Last 2 digits of ISO 8601 year   | 00, 01, ..., 99          | (0)     |
|             | representing the year that       |                          |         |
|             | contains the greater part of the |                          |         |
|             | ISO week ("%V").                 |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%G"        | Ano ISO 8601 com o século        | 0001, 0002, ..., 2013,   | (8)     |
|             | representando o ano que a maior  | 2014, ..., 9998, 9999    |         |
|             | parte da semana ISO ("%V").      |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%h"        | Equivalent to "%b".              | See "%b".                | (0)     |
+-------------+----------------------------------+--------------------------+---------+
| "%H"        | Hora (relógio de 24 horas) como  | 00, 01, ..., 23          | (9)     |
|             | um número decimal com zeros a    |                          |         |
|             | esquerda.                        |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%I"        | Hora (relógio de 12 horas) como  | 01, 02, ..., 12          | (9)     |
|             | um número decimal com zeros a    |                          |         |
|             | esquerda.                        |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%j"        | Dia do ano como um número        | 001, 002, ..., 366       | (9)     |
|             | decimal, com zeros a esquerda.   |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%m"        | Mês como um número decimal com   | 01, 02, ..., 12          | (9)     |
|             | zeros a esquerda.                |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%M"        | Minutos como um número decimal,  | 00, 01, ..., 59          | (9)     |
|             | com zeros a esquerda.            |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%n"        | The newline character ("'\n'").  | "\n"                     |         |
|             | For "strptime()", zero or more   |                          |         |
|             | whitespace.                      |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%p"        | Equivalente da localidade a AM   | AM, PM (en_US); am, pm   | (1),    |
|             | ou PM.                           | (de_DE)                  | (3)     |
+-------------+----------------------------------+--------------------------+---------+
| "%r"        | Locale's 12-hour clock time.     | 12:00:00 AM              | (1),    |
|             |                                  |                          | (0)     |
+-------------+----------------------------------+--------------------------+---------+
| "%R"        | Equivalent to "%H:%M".           | 10:01                    |         |
+-------------+----------------------------------+--------------------------+---------+
| "%S"        | Segundos como um número decimal, | 00, 01, ..., 59          | (4),    |
|             | com zeros a esquerda.            |                          | (9)     |
+-------------+----------------------------------+--------------------------+---------+
| "%t"        | The tab character ("'\t'"). For  | "\t"                     |         |
|             | "strptime()", zero or more       |                          |         |
|             | whitespace.                      |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%T"        | ISO 8601 time format, equivalent | 10:01:59                 |         |
|             | to "%H:%M:%S".                   |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%u"        | Dia de semana ISO 8601 como um   | 1, 2, ..., 7             |         |
|             | número decimal onde 1 é segunda- |                          |         |
|             | feira.                           |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%U"        | Número da semana do ano (Domingo | 00, 01, ..., 53          | (7),    |
|             | como o primeiro dia da semana)   |                          | (9)     |
|             | como um número decimal, com      |                          |         |
|             | zeros a esquerda. Todos os dias  |                          |         |
|             | em um ano novo precedendo o      |                          |         |
|             | primeiro domingo são             |                          |         |
|             | considerados como estando na     |                          |         |
|             | semana 0.                        |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%V"        | Semana ISO 8601 como um número   | 01, 02, ..., 53          | (8),    |
|             | decimal, com segunda-feira como  |                          | (9)     |
|             | o primeiro dia da semana. A      |                          |         |
|             | semana 01 é a semana contendo o  |                          |         |
|             | dia 4 de Janeiro.                |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%w"        | Dia da semana como um número     | 0, 1, ..., 6             |         |
|             | decimal, onde 0 é domingo e 6 é  |                          |         |
|             | sábado.                          |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%W"        | Número da semana do ano          | 00, 01, ..., 53          | (7),    |
|             | (Segunda-feira como o primeiro   |                          | (9)     |
|             | dia da semana) como um número    |                          |         |
|             | decimal, com zeros a esquerda.   |                          |         |
|             | Todos os dias em um ano novo     |                          |         |
|             | precedendo a primeira segunda-   |                          |         |
|             | feira são considerados como      |                          |         |
|             | estando na semana 0.             |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%x"        | Representação de data apropriada | 08/16/88 (None);         | (1)     |
|             | de localidade.                   | 08/16/1988 (en_US);      |         |
|             |                                  | 16.08.1988 (de_DE)       |         |
+-------------+----------------------------------+--------------------------+---------+
| "%X"        | Representação de hora apropriada | 21:30:00 (en_US);        | (1)     |
|             | da localidade.                   | 21:30:00 (de_DE)         |         |
+-------------+----------------------------------+--------------------------+---------+
| "%y"        | Ano sem século como um número    | 00, 01, ..., 99          | (9)     |
|             | decimal com zeros a esquerda.    |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%Y"        | Ano com século como um número    | 0001, 0002, ..., 2013,   | (2)     |
|             | decimal.                         | 2014, ..., 9998, 9999    |         |
+-------------+----------------------------------+--------------------------+---------+
| "%z"        | Diferença UTC no formato         | (vazio), +0000, -0400,   | (6)     |
|             | "±HHMM[SS[.ffffff]]" (string     | +1030, +063415,          |         |
|             | vazia se o objeto é ingênuo).    | -030712.345216           |         |
+-------------+----------------------------------+--------------------------+---------+
| "%Z"        | Nome do fuso horário (string     | (vazio), UTC, GMT        | (6)     |
|             | vazia se o objeto é ingênuo).    |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%%"        | Um caractere literal "'%'".      | %                        |         |
+-------------+----------------------------------+--------------------------+---------+

The ISO 8601 year and ISO 8601 week directives are not interchangeable
with the year and week number directives above. Calling "strptime()"
with incomplete or ambiguous ISO 8601 directives will raise a
"ValueError".

Several additional directives not required by the C11 standard are
included for convenience.

+-------------+----------------------------------+--------------------------+---------+
| Diretiva    | Significado                      | Exemplo                  | Notas   |
|=============|==================================|==========================|=========|
| "%f"        | Microssegundos como um número    | 000000, 000001, ...,     | (5)     |
|             | decimal, com zeros à esquerda    | 999999                   |         |
|             | até completar 6 dígitos.         |                          |         |
+-------------+----------------------------------+--------------------------+---------+
| "%:z"       | Diferença UTC no formato         | (vazio), +00:00, -04:00, | (6)     |
|             | "±HH:MM[:SS[.ffffff]]" (string   | +10:30, +06:34:15,       |         |
|             | vazia se o objeto é ingênuo).    | -03:07:12.345216         |         |
+-------------+----------------------------------+--------------------------+---------+

O conjunto completo de códigos de formato suportados varia entre as
plataformas, porque o Python chama a função "strftime()" da biblioteca
C da plataforma, e variações de plataforma são comuns. Para ver o
conjunto completo de códigos de formato suportados em sua plataforma,
consulte a documentação *strftime(3)*. Também existem diferenças entre
plataformas no tratamento de especificadores de formato não
suportados.

Adicionado na versão 3.6: "%G", "%u" e "%V" foram adicionados.

Adicionado na versão 3.12: "%:z" was added for "strftime()".

Adicionado na versão 3.15: "%D", "%F", "%n", "%t", and "%:z" were
added for "strptime()".


Technical detail
----------------

Em termos gerais, "d.strftime(fmt)" age como "time.strftime(fmt,
d.timetuple())" do módulo "time", embora nem todos os objetos suportem
um método "timetuple()".

For the "datetime.strptime()" and "date.strptime()" class methods, the
default value is "1900-01-01T00:00:00.000": any components not
specified in the format string will be pulled from the default value.

Nota:

  Format strings without separators can be ambiguous for parsing. For
  example, with "%Y%m%d", the string "2026111" may be parsed either as
  "2026-11-01" or as "2026-01-11". Use separators to ensure the input
  is parsed as intended.

Nota:

  When used to parse partial dates lacking a year,
  "datetime.strptime()" and "date.strptime()" will raise when
  encountering February 29 because the default year of 1900 is *not* a
  leap year.  Always add a default leap year to partial date strings
  before parsing.

Nota:

  If a "strptime()" format string contains more than one directive for
  the same field, for example both "%Y" and "%y", every directive must
  still match the input, but only the value of the last one is used.
  For example, parsing "200099" with "%Y%y" gives the year 1999.
  Repeating the same directive, like "%Y%Y", raises an error.

   >>> import datetime as dt
   >>> value = "2/29"
   >>> dt.datetime.strptime(value, "%m/%d")
   Traceback (most recent call last):
   ...
   ValueError: day 29 must be in range 1..28 for month 2 in year 1900
   >>> dt.datetime.strptime(f"1904 {value}", "%Y %m/%d")
   datetime.datetime(1904, 2, 29, 0, 0)

Usar "datetime.strptime(date_string, format)" é equivalente a:

   datetime(*(time.strptime(date_string, format)[0:6]))

exceto quando o formato inclui componentes de sub-segundos ou
informações de deslocamento de fuso horário, que são suportados em
"datetime.strptime" mas são descartados por "time.strptime".

Para objetos "time", os códigos de formato para ano, mês e dia não
devem ser usados, pois objetos "time" não têm tais valores. Se forem
usados de qualquer forma, o ano é substituído por 1900, e o mês e dia
por 1.

Para objetos "date", os códigos de formato para horas, minutos,
segundos e microssegundos não devem ser usados, pois objetos "date"
não têm tais valores. Se forem usados de qualquer forma, são
substituídos por 0.

Pela mesma razão, o tratamento de formato de strings contendo pontos
de código Unicode que não podem ser representados no conjunto de
caracteres da localidade atual também é dependente da plataforma. Em
algumas plataformas, tais pontos de código são preservados intactos na
saída, enquanto em outros "strftime" pode levantar "UnicodeError" ou
retornar uma string vazia ao invés.

Notas:

* This format code is currently unsupported by "strptime()".

* Como o formato depende da localidade atual, deve-se tomar cuidado ao
  fazer suposições sobre o valor de saída. A ordenação dos campos irá
  variar (por exemplo, "mês/dia/ano" versus "dia/mês/ano") e a saída
  pode conter caracteres não ASCII.

* O método "strptime()" pode analisar anos no intervalo completo de
  [1, 9999], mas anos < 1000 devem ser preenchidos com zeros até uma
  largura de 4 dígitos.

  Alterado na versão 3.2: Em versões anteriores, o método "strftime()"
  era limitado a anos >= 1900.

  Alterado na versão 3.3: Na versão 3.2, o método "strftime()" era
  limitado a anos >= 1000.

* Quando usado com o método "strptime()", a diretiva "%p" afeta
  somente o campo de hora de saída se a diretiva "%I" for usada para
  analisar a hora.

* Ao contrário do módulo "time", o módulo "datetime" não oferece
  suporte para segundos intercalares.

* Quando usado com o método "strptime()", a diretiva "%f" aceita de um
  a seis dígitos e zeros à direita. "%f" é uma extensão do conjunto de
  caracteres de formato no padrão do C (mas implementado separadamente
  em objetos datetime e, portanto, sempre disponível).

* Para um objeto ingênuo, os códigos de formatação "%z", "%:z" e "%Z"
  são substituídos por strings vazias.

  Para um objeto consciente:

  "%z"
     "utcoffset()" é transformado em uma string do formato
     "±HHMM[SS[.ffffff]]", onde "HH" é uma string de 2 dígitos que
     fornece o número de horas de deslocamento UTC, "MM" é uma string
     de 2 dígitos que fornece o número de minutos de deslocamento UTC,
     "SS" é uma string de 2 dígitos que fornece o número de segundos
     de deslocamento UTC e "ffffff" é uma string de 6 dígitos que
     fornece o número de microssegundos de deslocamento UTC. A parte
     "ffffff" é omitida quando o deslocamento é um número inteiro de
     segundos e tanto a parte "ffffff" quanto a parte "SS" são
     omitidas quando o deslocamento é um número inteiro de minutos.
     Por exemplo, se "utcoffset()" retornar "timedelta(hours=-3,
     minutes=-30)", "%z" será substituído pela string "'-0330'".

  Alterado na versão 3.7: A diferença UTC não é restrita a um número
  completo de minutos.

  Alterado na versão 3.7: When the "%z" directive is provided to the
  "strptime()" method, the UTC offsets can have a colon as a separator
  between hours, minutes and seconds. For example, both "'+010000'"
  and "'+01:00:00'" will be parsed as an offset of one hour. In
  addition, providing "'Z'" is identical to "'+00:00'".

  "%:z"
     When used with "strftime()", behaves exactly as "%z", except that
     a colon separator is added between hours, minutes and seconds.

     When used with "strptime()", the UTC offset is *required* to have
     a colon as a separator between hours, minutes and seconds. For
     example, "'+01:00:00'" (but *not* "'+010000'") will be parsed as
     an offset of one hour. In addition, providing "'Z'" is identical
     to "'+00:00'".

  "%Z"
     Em "strftime()", "%Z" é substituído por uma string vazia se
     "tzname()" retornar "None"; caso contrário, "%Z" é substituído
     pelo valor retornado, que deve ser uma string.

     "strptime()" aceita apenas certos valores para "%Z":

     1. qualquer valor em "time.tzname" para a localidade da sua
        máquina

     2. os valores codificados "UTC" e "GMT"

     Então alguém vivendo no Japão pode ter "JST", "UTC", e "GMT" como
     valores válidos, mas provavelmente não "EST". Isso levantará
     "ValueError" para valores inválidos.

  Alterado na versão 3.2: Quando a diretiva "%z" é fornecida ao método
  "strptime()", um objeto "datetime" consciente será produzido. O
  "tzinfo" do resultado será definido para uma instância "timezone".

* Quando utilizados com o método "strptime()", "%U" e "%W" são usados
  somente em cálculos quando o dia da semana e o ano ("%Y") são
  especificados.

* Semelhante a "%U" e "%W", "%V" é usado apenas em cálculos quando o
  dia da semana e o ano ISO ("%G") são especificados em um formato de
  string "strptime()". Observe também que "%G" e "%Y" não são
  intercambiáveis.

* Quando usado com o método "strptime()", o zero à esquerda é opcional
  para os formatos "%d", "%m", "%H", "%I", "%M", "%S", "%j", "%U",
  "%W" e "%V". O formato "%y" requer um zero à esquerda.

* When parsing a month and day using "strptime()", always include a
  year in the format.  If the value you need to parse lacks a year,
  append an explicit dummy leap year.  Otherwise your code will raise
  an exception when it encounters leap day because the default year
  used by the parser (1900) is not a leap year.  Users run into that
  bug every leap year.

     >>> month_day = "02/29"
     >>> dt.datetime.strptime(f"{month_day};1984", "%m/%d;%Y")  # No leap year bug.
     datetime.datetime(1984, 2, 29, 0, 0)

  Alterado na versão 3.15: Using "%d" without a year now raises
  "ValueError".

  Descontinuado desde a versão 3.15, será removido na versão 3.17:
  "strptime()" calls using a format string containing "%e" without a
  year now emit a "DeprecationWarning".

-[ Notas de rodapé ]-

[1] If, that is, we ignore the effects of relativity.

[2] Isso combina com a definição do calendário "proléptico Gregoriano"
    no livro *Cálculos Calendáricos* de Dershowitz e Reingold, onde
    ele é o calendário base para todas as computações. Veja o livro
    para algoritmos para conversão entre ordinais proléptico
    Gregoriano e muitos outros sistemas de calendário.

[3] Veja O guia para a matemática de calendário ISO 8601 de R. H. van
    Gent para uma boa explicação.
