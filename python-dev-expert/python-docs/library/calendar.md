"calendar" --- Funções gerais relacionadas ao calendário
********************************************************

**Código-fonte:** Lib/calendar.py

======================================================================

Este módulo permite que você exiba calendários como o programa Unix
**cal**, e fornece funções adicionais úteis relacionadas ao
calendário. Por padrão, esses calendários têm a segunda-feira como o
primeiro dia da semana, e domingo como o último (a convenção
europeia). Use "setfirstweekday()" para colocar o primeiro dia da
semana como domingo (6) ou para qualquer outro dia da semana.
Parâmetros que especificam datas são dados como inteiros. Para
funcionalidade relacionada, veja também os módulos "datetime" e
"time".

As funções e classes definidas neste módulo usam um calendário
idealizado, o calendário Gregoriano atual estendido indefinidamente
nas duas direções. Isso corresponde à definição do calendário
"proleptic Gregorian" (gregoriano proléptico) no livro "Calendrical
Calculations" de Dershowitz e Reingold, onde está o calendário base
para todas os cálculos. Anos com zero ou negativos são interpretados e
prescritos pelo padrão ISO 8601. Ano 0 é 1 A.C., ano -1 é 2 A.C, e de
assim em diante.

class calendar.Calendar(firstweekday=0)

   Cria um objeto "Calendar". *firstweekday* é um inteiro que
   especifica o primeiro dia da semana. "MONDAY" é "0" (o padrão),
   "SUNDAY" é "6".

   Um objeto "Calendar" fornece vários métodos que podem ser usados
   para preparar os dados do calendário para formatação. Esta classe
   não realiza nenhuma formatação por si mesma. Esse é o trabalho das
   subclasses.

   Instâncias de "Calendar" têm os seguintes métodos e atributos:

   firstweekday

      O primeiro dia da semana como um inteiro (0--6).

      Esta propriedade também pode ser definida e lida usando
      "setfirstweekday()" e "getfirstweekday()" respectivamente.

   getfirstweekday()

      Retorna um "int" correspondente ao primeiro dia da semana atual
      (0-6).

      Idêntico à leitura da propriedade "firstweekday".

   setfirstweekday(firstweekday)

      Define o primeiro dia da semana como *firstweekday*, passado
      como "int" (0--6).

      Idêntico à definição da propriedade "firstweekday".

   iterweekdays()

      Retorna um iterador dos números dos dias da semana que serão
      usados em uma semana. O primeiro valor do iterador será o mesmo
      que o da propriedade "firstweekday".

   itermonthdates(year, month)

      Retorna um iterador para o mês *month* (1--12) no ano *year*.
      Este iterador retornará todos os dias (como objetos
      "datetime.date") do mês, bem como os dias antes do início do mês
      ou após o final do mês, necessários para obter uma semana
      completa.

   itermonthdays(year, month)

      Retorna um iterador para o mês *month* no ano *year* semelhante
      a "itermonthdates()", mas não restrito pelo intervalo de
      "datetime.date". Os dias retornados serão simplesmente os
      números dos dias do mês. Para os dias fora do mês especificado,
      o número do dia será "0".

   itermonthdays2(year, month)

      Retorna um iterador para o mês *month* no ano *year* semelhante
      a "itermonthdates()", mas não restrito pelo intervalo de
      "datetime.date". Os dias retornados serão tuplas consistindo de
      um número de dia do mês e um número de dia da semana.

   itermonthdays3(year, month)

      Retorna um iterador para o mês *month* no ano *year* semelhante
      a "itermonthdates()", mas não restrito pelo intervalo de
      "datetime.date". Os dias retornados serão tuplas consistindo de
      números de um ano, um mês e um dia do mês.

      Adicionado na versão 3.7.

   itermonthdays4(year, month)

      Retorna um iterador para o mês *month* no ano *year* semelhante
      a "itermonthdates()", mas não restrito pelo intervalo de
      "datetime.date". Os dias retornados serão tuplas consistindo de
      números de um ano, um mês, um dia do mês e um dia da semana.

      Adicionado na versão 3.7.

   monthdatescalendar(year, month)

      Retorna uma lista das semanas do mês *month* do *year* como
      semanas completas. As semanas são listas de sete objetos
      "datetime.date".

   monthdays2calendar(year, month)

      Retorna uma lista das semanas do mês *month* do ano *year* como
      semanas completas. As semanas são listas de sete tuplas de
      números dias e de dias de semanas.

   monthdayscalendar(year, month)

      Retorna uma lista das semanas do mês *month* do ano *year* como
      semanas completas. As semanas são listas de números de sete
      dias.

   yeardatescalendar(year, width=3)

      Retorna os dados para o ano especificado prontos para
      formatação. O valor de retorno é uma lista de linhas de meses.
      Cada linha de mês contém até *width* meses (padrão é 3). Cada
      mês contém entre 4 e 6 semanas, e cada semana contém 1--7 dias.
      Os dias são objetos "datetime.date".

   yeardays2calendar(year, width=3)

      Retorna os dados para o ano especificado prontos para formatação
      (semelhante a "yeardatescalendar()"). Entradas nas listas
      semanais são tuplas de números de dias e números de dias de
      semana. Números de dias fora deste mês são zero.

   yeardayscalendar(year, width=3)

      Retorna a data para o ano especificado prontos para formatação
      (semelhante a "yeardatescalendar()"). Entradas nas listas de
      semanas são números de dias. Números de dias fora deste mês são
      zero.

class calendar.TextCalendar(firstweekday=0)

   Esta classe pode ser usada para gerar texto plano para calendários.

   Instâncias de "TextCalendar" têm os seguintes métodos:

   prweek(theweek, width)

      Imprime um calendário da semana conforme retornado pelo
      "formatweek()" e sem uma nova lonha ao final.

   formatday(theday, weekday, width)

      Retorna uma string representando um único dia formatado com a
      largura fornecida em *width*. Se *theday* for "0", retorna uma
      string de espaços da largura especificada, representando um dia
      vazio. O parâmetro *weekday* não é usado.

   formatweek(theweek, width)

      Retorna uma única semana em uma string sem nova linha. *width*
      especifica a largura das colunas de data, que são centrais.
      Dependendo do primeiro dia da semana conforme especificado no
      construtor ou configurado pelo método "setfirstweekday()".

   formatweekday(weekday, width)

      Retorna uma string representando o nome de um único dia da
      semana formatado para a largura especificada em *width*. O
      parâmetro *weekday* é um inteiro representando o dia da semana,
      onde "0" é segunda-feira e "6" é domingo.

   formatweekheader(width)

      Retorna uma string contendo a linha de cabeçalho dos nomes dos
      dias da semana, formatada com a largura fornecida por *width*
      para cada coluna. Os nomes dependem das configurações de
      localidade e são preenchidos até a largura especificada.

   formatmonth(theyear, themonth, w=0, l=0)

      Retorna o calendário do mês em uma string multilinha. Se *w* for
      providenciado, isto especifica a largura das colunas de data,
      que são centrais. Se *l* for dado, este especifica o número de
      linhas que cada semana vai usar. Dependendo do primeiro dia da
      semana conforme especificado no construtor ou configurado pelo
      método "setfirstweekday()".

   formatmonthname(theyear, themonth, width, withyear=True)

      Retorna uma string representando o nome do mês centralizado
      dentro da largura especificada em *width*. Se *withyear* for
      "True", inclui o ano na saída. Os parâmetros *theyear* e
      *themonth* especificam o ano e o mês para o nome a ser
      formatado, respectivamente.

   prmonth(theyear, themonth, w=0, l=0)

      Imprime um calendário do mês conforme retornado pelo
      "formatmonth()".

   formatyear(theyear, w=2, l=1, c=6, m=3)

      Retorna um calendário com *m* colunas para um ano inteiro
      conforme uma string multilinha. Parâmetros opcionais *w*, *l* e
      *c* definem a largura da coluna data, linhas por semana e
      números de espaços entre as colunas dos meses, respectivamente.
      Depende do primeiro dia da semana conforme especificado no
      construtor ou definido pelo método "setfirstweekday()". O ano
      mais novo para o qual o calendário pode ser gerado depende da
      plataforma.

   pryear(theyear, w=2, l=1, c=6, m=3)

      Imprime o calendário para um ano inteiro conforme retornado por
      "formatyear()".

class calendar.HTMLCalendar(firstweekday=0)

   Esta classse pode ser usada para gerar calendários HTML.

   Instâncias de "HTMLCalendar" têm os seguintes métodos:

   formatmonth(theyear, themonth, withyear=True)

      Retorna um calendário do mês como uma tabela HTML. Se *withyear*
      for verdadeiro, o ano será incluído no cabeçalho, senão apenas o
      nome do mês será utilizado.

   formatyear(theyear, width=3)

      Retorna um calendário do ano como uma tabela HTML. *width*
      (padronizada para 3) especifica o número de meses por linha.

   formatyearpage(theyear, width=3, css='calendar.css', encoding=None)

      Retorna o calendário de um ano como uma página HTML completa.
      *width* (padrão 3) especifica o número de meses por linha. *css*
      é o nome da folha de estilo em cascata a ser usada. "None" pode
      ser passado se nenhuma folha de estilo deve ser usada.
      *encoding* especifica a codificação a ser usada para a saída
      (padrão para "'utf-8'").

   formatmonthname(theyear, themonth, withyear=True)

      Retorna um nome de mês como uma linha de tabela HTML. Se
      *withyear* for verdadeiro, o ano será incluído na linha, senão
      apenas o nome do mês será utilizado.

   "HTMLCalendar" tem os seguintes atributos que você pode substituir
   para personalizar as classes CSS usadas pelo calendário:

   cssclasses

      Uma lista de classes CSS usadas para cada dia da semana. A lista
      de classes padrão é:

         cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

      mais estilos podem ser adicionados para cada dia:

         cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun red"]

      Observe que o comprimento desta lista deve ser de sete itens.

   cssclass_noday

      A classe CSS para um dia da semana que ocorre no mês anterior ou
      seguinte.

      Adicionado na versão 3.7.

   cssclasses_weekday_head

      Uma lista de classes CSS usadas para nomes de dias da semana na
      linha de cabeçalho. O padrão é o mesmo que "cssclasses".

      Adicionado na versão 3.7.

   cssclass_month_head

      A classe CSS principal do mês (usada por "formatmonthname()"). O
      valor padrão é ""month"".

      Adicionado na versão 3.7.

   cssclass_month

      A classe CSS para a tabela do mês inteiro (usada por
      "formatmonth()"). O valor padrão é ""month"".

      Adicionado na versão 3.7.

   cssclass_year

      A classe CSS para a tabela de tabelas do ano inteiro (usada por
      "formatyear()"). O valor padrão é ""year"".

      Adicionado na versão 3.7.

   cssclass_year_head

      A classe CSS para o cabeçalho da tabela para o ano inteiro
      (usado por "formatyear()"). O valor padrão é ""year"".

      Adicionado na versão 3.7.

   Observe que, embora a nomenclatura dos atributos de classe
   descritos acima seja singular (por exemplo, "cssclass_month"
   "cssclass_noday"), é possível substituir a única classe CSS por uma
   lista de classes CSS separadas por espaços, por exemplo:

      "text-bold text-red"

   Aqui está um exemplo de como "HTMLCalendar" pode ser personalizado:

      class CustomHTMLCal(calendar.HTMLCalendar):
          cssclasses = [style + " text-nowrap" for style in
                        calendar.HTMLCalendar.cssclasses]
          cssclass_month_head = "text-center month-head"
          cssclass_month = "text-center month"
          cssclass_year = "text-italic lead"

class calendar.LocaleTextCalendar(firstweekday=0, locale=None)

   Esta subclasse de "TextCalendar" pode receber um nome de localidade
   no construtor e retornará nomes de meses e dias da semana na
   localidade especificada.

class calendar.LocaleHTMLCalendar(firstweekday=0, locale=None)

   Esta subclasse de "HTMLCalendar" pode receber um nome de localidade
   no construtor e retornará nomes de meses e dias da semana na
   localidade especificada.

Nota:

  Os métodos construtores "formatweekday()" e "formatmonthname()"
  dessas duas classes alteram temporariamente a localidade "LC_TIME"
  para o *locale* fornecido. Como a localidade atual é uma
  configuração de todo o processo, eles não são seguros para threads.

Para calendários de texto simples, este módulo fornece as seguintes
funções.

calendar.setfirstweekday(firstweekday)

   Define o dia da semana ("0" é segunda-feira, "6" é domingo) para
   começar cada semana. Os valores "MONDAY", "TUESDAY", "WEDNESDAY",
   "THURSDAY", "FRIDAY", "SATURDAY" e "SUNDAY" são fornecidos para
   conveniência. Por exemplo, para definir o primeiro dia da semana
   como domingo:

      import calendar
      calendar.setfirstweekday(calendar.SUNDAY)

calendar.firstweekday()

   Retorna a configuração atual para o dia da semana que inicia cada
   semana.

calendar.isleap(year)

   Retorna "True" se *year* for um ano bissexto, caso contrário,
   "False".

calendar.leapdays(y1, y2)

   Retorna o número de anos bissextos no intervalo de *y1* a *y2*
   (exclusivo), onde *y1* e *y2* são anos.

   Esta função funciona para intervalos que abrangem uma mudança de
   século.

calendar.weekday(year, month, day)

   Retorna o dia da semana ("0" é segunda-feira) para *year*
   ("1970"--...), *month* ("1"--"12"), *day* ("1"--"31").

calendar.weekheader(width)

   Retorna um cabeçalho contendo nomes abreviados de dias da semana.
   *width* especifica a largura em caracteres para um dia da semana.

calendar.monthrange(year, month)

   Retorna o dia da semana do primeiro dia do mês e o número de dias
   do mês, para o *year* e *month* especificados.

calendar.monthcalendar(year, month)

   Retorna uma matriz representando o calendário de um mês. Cada linha
   representa uma semana; dias fora do mês são representados por
   zeros. Cada semana começa com segunda-feira, a menos que seja
   definida por "setfirstweekday()".

calendar.prmonth(theyear, themonth, w=0, l=0)

   Imprime um calendário do mês conforme retornado pelo "month()".

calendar.month(theyear, themonth, w=0, l=0)

   Retorna o calendário de um mês em uma string de várias linhas
   usando "formatmonth()" da classe "TextCalendar".

calendar.prcal(theyear, w=0, l=0, c=6, m=3)

   Prints the calendar for an entire year as returned by "calendar()".

calendar.calendar(theyear, w=2, l=1, c=6, m=3)

   Retorna um calendário de 3 colunas para um ano inteiro como uma
   string de várias linhas usando "formatyear()" da classe
   "TextCalendar".

calendar.timegm(tuple)

   Uma função não relacionada, mas útil, que pega uma tupla de tempo,
   como a retornada pela função "gmtime()" no módulo "time", e retorna
   o valor de registro de data e hora Unix correspondente, persumindo
   uma época de 1970 e a codificação POSIX. Na verdade,
   "time.gmtime()" e "timegm()" são inversos um do outro.

O módulo "calendar" exporta os seguintes atributos de dados:

calendar.day_name

   Uma sequência que representa os dias da semana no local atual, onde
   Monday é o dia número 0.

   >>> import calendar
   >>> list(calendar.day_name)
   ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

calendar.day_abbr

   Uma sequência que representa os dias abreviados da semana no local
   atual, onde Mon é o dia número 0.

   >>> import calendar
   >>> list(calendar.day_abbr)
   ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

calendar.MONDAY
calendar.TUESDAY
calendar.WEDNESDAY
calendar.THURSDAY
calendar.FRIDAY
calendar.SATURDAY
calendar.SUNDAY

   Apelidos para os dias da semana, onde "MONDAY" é "0" e "SUNDAY" é
   "6".

   Adicionado na versão 3.12.

class calendar.Day

   Enumeração que define os dias da semana como constantes inteiras.
   Os membros dessa enumeração são exportados para o escopo do módulo
   como "MONDAY" até "SUNDAY".

   Adicionado na versão 3.12.

calendar.month_name

   Uma sequência que representa os meses do ano na localidade atual.
   Isso segue a convenção normal de janeiro sendo o mês número 1,
   então tem um comprimento de 13 e "month_name[0]" é a string vazia.

   >>> import calendar
   >>> list(calendar.month_name)
   ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

   Cuidado:

     Em localidades que possuem formas alternativas para os nomes dos
     meses, a sequência "month_name" pode não ser adequada quando o
     nome de um mês aparece isoladamente, e não como parte de uma
     data. Por exemplo, em grego e em muitas línguas eslavas e
     bálticas, "month_name" apresentará o nome do mês no caso
     genitivo. Utilize "standalone_month_name" para obter uma forma
     adequada ao uso isolado.

calendar.month_abbr

   Uma sequência que representa os meses abreviados do ano na
   localidade atual. Isso segue a convenção normal de janeiro sendo o
   mês número 1, então tem um comprimento de 13 e "month_abbr[0]" é a
   string vazia.

   >>> import calendar
   >>> list(calendar.month_abbr)
   ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

   Cuidado:

     Em localidades que possuem formas alternativas para os nomes dos
     meses, a sequência "month_abbr" pode não ser adequada quando o
     nome de um mês aparece isoladamente, e não como parte de uma
     data. Utilize "standalone_month_abbr" para obter uma forma
     adequada ao uso isolado.

calendar.standalone_month_name

   Uma sequência que representa os meses do ano na localidade atual,
   na forma isolada, caso a localidade forneça uma. Caso contrário, é
   equivalente a "month_name".

   Adicionado na versão 3.15.

calendar.standalone_month_abbr

   Uma sequência que representa os meses abreviados do ano na
   localidade atual, na forma isolada, caso a localidade forneça uma.
   Caso contrário, é equivalente a "month_abbr".

   Adicionado na versão 3.15.

calendar.JANUARY
calendar.FEBRUARY
calendar.MARCH
calendar.APRIL
calendar.MAY
calendar.JUNE
calendar.JULY
calendar.AUGUST
calendar.SEPTEMBER
calendar.OCTOBER
calendar.NOVEMBER
calendar.DECEMBER

   Apelidos para os meses do ano, onde "JANUARY" é "1" e "DECEMBER" é
   "12".

   Adicionado na versão 3.12.

class calendar.Month

   Enumeração que define os meses do ano como constantes inteiras. Os
   membros dessa enumeração são exportados para o escopo do módulo
   como "JANUARY" até "DECEMBER".

   Adicionado na versão 3.12.

O módulo "calendar" define as seguintes exceções:

exception calendar.IllegalMonthError(month)

   Uma subclasse de "ValueError" e "IndexError", levantada quando o
   número do mês fornecido está fora do intervalo de 1 a 12
   (inclusive).

   Alterado na versão 3.12: "IllegalMonthError" agora também é uma
   subclasse de "ValueError". Novos códigos devem evitar capturar
   "IndexError".

   month

      O número de meses inválidos.

exception calendar.IllegalWeekdayError(weekday)

   Uma subclasse de "ValueError", levantada quando o número do dia da
   semana fornecido está fora do intervalo de 0 a 6 (inclusive).

   weekday

      O número de dias da semana inválidos.

Ver também:

  Módulo "datetime"
     Interface orientada a objetos para datas e horas com
     funcionalidade semelhante ao módulo "time".

  Módulo "time"
     Funções de baixo nível relacionadas ao tempo.


Uso na linha de comando
=======================

Adicionado na versão 2.5.

O módulo "calendar" pode ser executado como um script na linha de
comando para exibir um calendário interativamente.

   python -m calendar [-h] [-L LOCALE] [-e ENCODING] [-t {text,html}]                   [-w WIDTH] [-l LINES] [-s SPACING] [-m MONTHS] [-c CSS]                   [-f FIRST_WEEKDAY] [year] [month]

Por exemplo, para exibir um calendário para o ano 2000:

   $ python -m calendar 2000                                  2000      January                   February                   MarchMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su                1  2          1  2  3  4  5  6             1  2  3  4  5 3  4  5  6  7  8  9       7  8  9 10 11 12 13       6  7  8  9 10 11 1210 11 12 13 14 15 16      14 15 16 17 18 19 20      13 14 15 16 17 18 1917 18 19 20 21 22 23      21 22 23 24 25 26 27      20 21 22 23 24 25 2624 25 26 27 28 29 30      28 29                     27 28 29 30 3131       April                      May                       JuneMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su                1  2       1  2  3  4  5  6  7                1  2  3  4 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 1110 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 1817 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 2524 25 26 27 28 29 30      29 30 31                  26 27 28 29 30        July                     August                  SeptemberMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su                1  2          1  2  3  4  5  6                   1  2  3 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 1010 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 1717 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 2424 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 3031      October                   November                  DecemberMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su                   1             1  2  3  4  5                   1  2  3 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 1716 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 2423 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 3130 31

As seguintes opções são aceitas:

--help, -h

   Mostra a mensagem de ajuda e sai.

--locale LOCALE, -L LOCALE

   A localidade a ser usada para nomes de meses e dias da semana. O
   padrão é inglês.

--encoding ENCODING, -e ENCODING

   A codificação a ser usada na saída. "--encoding" é necessário se "
   --locale" estiver definido.

--type {text,html}, -t {text,html}

   Exibe o calendário no terminal como texto ou como um documento
   HTML.

--first-weekday FIRST_WEEKDAY, -f FIRST_WEEKDAY

   O dia da semana para começar cada semana. Deve ser um número entre
   0 (segunda-feira) e 6 (domingo). O padrão é 0.

   Adicionado na versão 3.13.

year

   O ano para exibir o calendário. O padrão é o ano atual.

month

   O mês do "year" especificado para exibir o calendário. Deve ser um
   número entre 1 e 12. O padrão é exibir um calendário para todo o
   ano.

*Opções de modo texto:*

--width WIDTH, -w WIDTH

   A largura da coluna de data no terminal. A data é exibida
   centralizada na coluna. Qualquer valor inferior a 2 é ignorado. O
   padrão é 2.

--lines LINES, -l LINES

   O número de linhas por semana no terminal. A data é exibida
   alinhada no topo. Qualquer valor inferior a 1 é ignorado. O padrão
   é 1.

--spacing SPACING, -s SPACING

   O espaço entre os meses nas colunas. Qualquer valor inferior a 2 é
   ignorado. O padrão é 6.

--months MONTHS, -m MONTHS

   O número de meses exibidos por linha. O padrão é 3.

Alterado na versão 3.14: Por padrão, dia de hoje é destacada em cor e
pode ser controlada usando variáveis de ambiente.

Alterado na versão 3.15: Por padrão, o mês agora também é destacado
com cor, e os dias da semana também aparecem coloridos. Esse
comportamento pode ser controlado por meio de variáveis de ambiente.

*Opções do modo HTML:*

--css CSS, -c CSS

   O caminho de uma folha de estilo CSS a ser usada no calendário.
   Isso deve ser relativo ao HTML gerado ou a um HTTP absoluto ou a
   uma URL "file:///".
