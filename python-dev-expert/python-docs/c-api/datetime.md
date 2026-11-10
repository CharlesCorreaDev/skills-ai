Objetos DateTime
****************

Vários objetos de data e hora são fornecidos pelo módulo "datetime".
Antes de usar qualquer uma dessas funções, o arquivo de cabeçalho
"datetime.h" deve ser incluído na sua fonte (observe que isso não é
incluído por "Python.h") e a macro "PyDateTime_IMPORT" deve ser
chamada, geralmente como parte da função de inicialização do módulo. A
macro coloca um ponteiro para uma estrutura C em uma variável
estática, "PyDateTimeAPI", usada pelas macros a seguir.

PyDateTime_IMPORT

   Importa a API C de datetime.

   Em caso de sucesso, preenche o ponteiro "PyDateTimeAPI". Em caso de
   falha, define "PyDateTimeAPI" como "NULL" e lança uma exceção. O
   chamador deve verificar se ocorreu um erro através de
   "PyErr_Occurred()":

      PyDateTime_IMPORT;
      if (PyErr_Occurred()) { /* limpeza */ }

   Aviso:

     Isso não é compatível com subinterpretadores.

   Alterado na versão 3.15: Esta macro agora é seguro para thread.

type PyDateTime_CAPI

   Estrutura contendo os campos para a API C de datetime.

   Os campos desta estrutura são privados e sujeitos a alterações.

   Não use isto diretamente; prefira as APIs "PyDateTime_*".

PyDateTime_CAPI *PyDateTimeAPI

   Objeto alocado dinamicamente contendo a API C de datetime.

   Esta variável só estará disponível após a execução bem-sucedida de
   "PyDateTime_IMPORT".

   Alterado na versão 3.15: This variable should not be accessed
   directly as direct access is not thread-safe. Use
   "PyDateTime_IMPORT" instead.

type PyDateTime_Date

   Esta é uma instância de "PyObject" representando o objeto data do
   Python.

type PyDateTime_DateTime

   Esta é uma instância de "PyObject" representando o objeto datetime
   do Python.

type PyDateTime_Time

   Esta é uma instância de "PyObject" representando o objeto hora do
   Python.

type PyDateTime_Delta

   Esta é uma instância de "PyObject" representando a diferença entre
   dois valores de datetime.

PyTypeObject PyDateTime_DateType

   Esta instância de "PyTypeObject" representa o tipo data do Python;
   é o mesmo objeto que "datetime.date" na camada de Python.

PyTypeObject PyDateTime_DateTimeType

   Esta instância de "PyTypeObject" representa o tipo datetime do
   Python; é o mesmo objeto que "datetime.datetime" na camada de
   Python.

PyTypeObject PyDateTime_TimeType

   Esta instância de "PyTypeObject" representa o tipo hora do Python;
   é o mesmo objeto que "datetime.time" na camada de Python.

PyTypeObject PyDateTime_DeltaType

   Esta instância de "PyTypeObject" representa o tipo Python para a
   diferença entre dois valores de datetime; é o mesmo objeto que
   "datetime.timedelta" na camada de Python.

PyTypeObject PyDateTime_TZInfoType

   Esta instância de "PyTypeObject" representa o tipo fuso horário do
   Python; é o mesmo objeto que "datetime.tzinfo" na camada de Python.

Macro para acesso ao singleton UTC:

PyObject *PyDateTime_TimeZone_UTC

   Retorna um singleton do fuso horário representando o UTC, o mesmo
   objeto que "datetime.timezone.utc".

   Adicionado na versão 3.7.

Macros de verificação de tipo:

int PyDate_Check(PyObject *ob)

   Retorna verdadeiro se *ob* for do tipo "PyDateTime_DateType" ou um
   subtipo de "PyDateTime_DateType". *ob* não deve ser "NULL". Esta
   função sempre tem sucesso.

int PyDate_CheckExact(PyObject *ob)

   Retorna verdadeiro se *ob* for do tipo "PyDateTime_DateType". *ob*
   não deve ser "NULL". Esta função sempre tem sucesso.

int PyDateTime_Check(PyObject *ob)

   Retorna verdadeiro se *ob* é do tipo "PyDateTime_DateTimeType" ou
   um subtipo de "PyDateTime_DateTimeType". *ob* não deve ser "NULL".
   Esta função sempre tem sucesso.

int PyDateTime_CheckExact(PyObject *ob)

   Retorna verdadeiro se *ob* for do tipo "PyDateTime_DateTimeType".
   *ob* não deve ser "NULL". Esta função sempre tem sucesso.

int PyTime_Check(PyObject *ob)

   Retorna verdadeiro se *ob* é do tipo "PyDateTime_TimeType" ou um
   subtipo de "PyDateTime_TimeType". *ob* não deve ser "NULL". Esta
   função sempre tem sucesso.

int PyTime_CheckExact(PyObject *ob)

   Retorna verdadeiro se *ob* for do tipo "PyDateTime_TimeType". *ob*
   não deve ser "NULL". Esta função sempre tem sucesso.

int PyDelta_Check(PyObject *ob)

   Retorna verdadeiro se *ob* for do tipo "PyDateTime_DeltaType" ou um
   subtipo de "PyDateTime_DeltaType". *ob* não pode ser "NULL". Esta
   função sempre tem sucesso.

int PyDelta_CheckExact(PyObject *ob)

   Retorna verdadeiro se *ob* for do tipo "PyDateTime_DeltaType". *ob*
   não deve ser "NULL". Esta função sempre tem sucesso.

int PyTZInfo_Check(PyObject *ob)

   Retorna verdadeiro se *ob* for do tipo "PyDateTime_TZInfoType" ou
   um subtipo de "PyDateTime_TZInfoType". *ob* não pode ser "NULL".
   Esta função sempre tem sucesso.

int PyTZInfo_CheckExact(PyObject *ob)

   Retorna verdadeiro se *ob* for do tipo "PyDateTime_TZInfoType".
   *ob* não deve ser "NULL". Esta função sempre tem sucesso.

Macros para criar objetos:

PyObject *PyDate_FromDate(int year, int month, int day)
    *Retorna valor: Nova referência.*

   Retorna um objeto "datetime.date" com o ano, mês e dia
   especificados.

PyObject *PyDateTime_FromDateAndTime(int year, int month, int day, int hour, int minute, int second, int usecond)
    *Retorna valor: Nova referência.*

   Retorna um objeto "datetime.datetime" com o ano, mês, dia, hora,
   minuto, segundo, microssegundo especificados.

PyObject *PyDateTime_FromDateAndTimeAndFold(int year, int month, int day, int hour, int minute, int second, int usecond, int fold)
    *Retorna valor: Nova referência.*

   Retorna um objeto "datetime.datetime" com o ano, mês, dia, hora,
   minuto, segundo, microssegundo e a dobra especificados.

   Adicionado na versão 3.6.

PyObject *PyTime_FromTime(int hour, int minute, int second, int usecond)
    *Retorna valor: Nova referência.*

   Retorna um objeto "datetime.time" com a hora, minuto, segundo e
   microssegundo especificados.

PyObject *PyTime_FromTimeAndFold(int hour, int minute, int second, int usecond, int fold)
    *Retorna valor: Nova referência.*

   Retorna um objeto "datetime.time" com a hora, minuto, segundo,
   microssegundo e a dobra especificados.

   Adicionado na versão 3.6.

PyObject *PyDelta_FromDSU(int days, int seconds, int useconds)
    *Retorna valor: Nova referência.*

   Retorna um objeto "datetime.timedelta" representando o número
   especificado de dias, segundos e microssegundos. A normalização é
   realizada para que o número resultante de microssegundos e segundos
   esteja nos intervalos documentados para objetos de
   "datetime.timedelta".

PyObject *PyTimeZone_FromOffset(PyObject *offset)
    *Retorna valor: Nova referência.*

   Retorna um objeto "datetime.timezone" com um deslocamento fixo sem
   nome representado pelo argumento *offset*.

   Adicionado na versão 3.7.

PyObject *PyTimeZone_FromOffsetAndName(PyObject *offset, PyObject *name)
    *Retorna valor: Nova referência.*

   Retorna um objeto "datetime.timezone" com um deslocamento fixo
   representado pelo argumento *offset* e com tzname *name*.

   Adicionado na versão 3.7.

Macros para extrair campos de objetos *date*. O argumento deve ser uma
instância de "PyDateTime_Date", inclusive subclasses (como
"PyDateTime_DateTime"). O argumento não deve ser "NULL", e o tipo não
é verificado:

int PyDateTime_GET_YEAR(PyDateTime_Date *o)

   Retorna o ano, como um inteiro positivo.

int PyDateTime_GET_MONTH(PyDateTime_Date *o)

   Retorna o mês, como um inteiro de 1 a 12.

int PyDateTime_GET_DAY(PyDateTime_Date *o)

   Retorna o dia, como um inteiro de 1 a 31.

Macros para extrair campos de objetos *datetime*.  O argumento deve
ser uma instância de "PyDateTime_DateTime", inclusive subclasses. O
argumento não deve ser "NULL", e o tipo não é verificado:

int PyDateTime_DATE_GET_HOUR(PyDateTime_DateTime *o)

   Retorna a hora, como um inteiro de 0 a 23.

int PyDateTime_DATE_GET_MINUTE(PyDateTime_DateTime *o)

   Retorna o minuto, como um inteiro de 0 a 59.

int PyDateTime_DATE_GET_SECOND(PyDateTime_DateTime *o)

   Retorna o segundo, como um inteiro de 0 a 59.

int PyDateTime_DATE_GET_MICROSECOND(PyDateTime_DateTime *o)

   Retorna o microssegundo, como um inteiro de 0 a 999999.

int PyDateTime_DATE_GET_FOLD(PyDateTime_DateTime *o)

   Retorna a dobra, como um inteiro de 0 a 1.

   Adicionado na versão 3.6.

PyObject *PyDateTime_DATE_GET_TZINFO(PyDateTime_DateTime *o)

   Retorna o tzinfo (que pode ser "None").

   Adicionado na versão 3.10.

Macros para extrair campos de objetos *time*. O argumento deve ser uma
instância de "PyDateTime_Time", inclusive subclasses. O argumento não
deve ser "NULL", e o tipo não é verificado:

int PyDateTime_TIME_GET_HOUR(PyDateTime_Time *o)

   Retorna a hora, como um inteiro de 0 a 23.

int PyDateTime_TIME_GET_MINUTE(PyDateTime_Time *o)

   Retorna o minuto, como um inteiro de 0 a 59.

int PyDateTime_TIME_GET_SECOND(PyDateTime_Time *o)

   Retorna o segundo, como um inteiro de 0 a 59.

int PyDateTime_TIME_GET_MICROSECOND(PyDateTime_Time *o)

   Retorna o microssegundo, como um inteiro de 0 a 999999.

int PyDateTime_TIME_GET_FOLD(PyDateTime_Time *o)

   Retorna a dobra, como um inteiro de 0 a 1.

   Adicionado na versão 3.6.

PyObject *PyDateTime_TIME_GET_TZINFO(PyDateTime_Time *o)

   Retorna o tzinfo (que pode ser "None").

   Adicionado na versão 3.10.

Macros para extrair campos de objetos *time delta*. O argumento deve
ser uma instância de "PyDateTime_Delta", inclusive subclasses. O
argumento não deve ser "NULL", e o tipo não é verificado:

int PyDateTime_DELTA_GET_DAYS(PyDateTime_Delta *o)

   Retorna o número de dias, como um inteiro de -999999999 a
   999999999.

   Adicionado na versão 3.3.

int PyDateTime_DELTA_GET_SECONDS(PyDateTime_Delta *o)

   Retorna o número de segundos, como um inteiro de 0 a 86399.

   Adicionado na versão 3.3.

int PyDateTime_DELTA_GET_MICROSECONDS(PyDateTime_Delta *o)

   Retorna o número de microssegundos, como um inteiro de 0 a 999999.

   Adicionado na versão 3.3.

Macros para a conveniência de módulos implementando a API de DB:

PyObject *PyDateTime_FromTimestamp(PyObject *args)
    *Retorna valor: Nova referência.*

   Cria e retorna um novo objeto "datetime.datetime" dado uma tupla de
   argumentos que possa ser passada ao método
   "datetime.datetime.fromtimestamp()".

PyObject *PyDate_FromTimestamp(PyObject *args)
    *Retorna valor: Nova referência.*

   Cria e retorna um novo objeto "datetime.date" dado uma tupla de
   argumentos que possa ser passada ao método
   "datetime.date.fromtimestamp()".


Dados internos
**************

Os seguintes símbolos são expostos pela API C, mas devem ser
considerados apenas para uso interno.

PyDateTime_CAPSULE_NAME

   Nome da cápsula de datetime a ser passada para
   "PyCapsule_Import()".

   Uso interno apenas. Use "PyDateTime_IMPORT" em vez disso.
