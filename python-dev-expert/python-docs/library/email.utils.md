"email.utils": Utilitários diversos
***********************************

**Código-fonte:** Lib/email/utils.py

======================================================================

Existem alguns utilitários úteis fornecidos no "email.utils" module:

email.utils.localtime(dt=None)

   Return local time as an aware datetime object.  If called without
   arguments, return the current time.  Otherwise the *dt* argument
   should be a "datetime" instance, and it is converted to the local
   time zone according to the system time zone database.  If *dt* is
   naive (that is, "dt.tzinfo" is "None"), it is assumed to be in
   local time.

   Adicionado na versão 3.3.

   Descontinuado desde a versão 3.12, removido na versão 3.14: O
   parâmetro *isdst*.

email.utils.make_msgid(idstring=None, domain=None)

   Returns a string suitable for an **RFC 2822**-compliant *Message-
   ID* header.  Optional *idstring*, if given, is a string used to
   strengthen the uniqueness of the message id.  Optional *domain*, if
   given, provides the portion of the msgid after the '@'.  The
   default is the local hostname.  It is normally not necessary to
   override this default, but may be useful in certain cases, such as
   constructing a distributed system that uses a consistent domain
   name across multiple hosts.

   Alterado na versão 3.2: Adicionada a palavra-chave *domain*.

As funções restantes fazem parte da API de e-mail herdada
("Compat32"). Não há necessidade de usá-las diretamente com a nova
API, pois a análise e a formatação fornecidas são feitas
automaticamente pelo mecanismo de análise de cabeçalhos da nova API.

email.utils.quote(str)

   Devolve uma nova string com barras invertidas em *str* substituídas
   por duas barras invertidas e aspas duplas substituídas por aspas
   duplas invertidas.

email.utils.unquote(str)

   Retorna uma nova string que é uma versão sem aspas de *str*. Se
   *str* terminar e começar com aspas duplas, elas serão removidas. Da
   mesma forma, se *str* termina e começa com colchetes angulares,
   eles são removidos.

email.utils.parseaddr(address, *, strict=True)

   Analisa o endereço -- que deve ser o valor de algum campo contendo
   endereço, como *To* ou *Cc* -- em suas partes constituinte
   *realname* e *email address*. Retorna uma tupla daquela informação,
   a menos que a análise falhe, caso em que uma tupla de 2 de "('',
   '')" é retornada.

   Se *strict* for verdadeiro, usa um analisador sintático estrito que
   rejeite entradas malformadas.

   Alterado na versão 3.13: Adiciona o parâmetro opcional *strict* e
   rejeita entradas malformadas por padrão.

email.utils.formataddr(pair, charset='utf-8')

   The inverse of "parseaddr()", this takes a 2-tuple of the form
   "(realname, email_address)" and returns the string value suitable
   for a *To* or *Cc* header.  If the first element of *pair* is
   false, then the second element is returned unmodified.

   O *charset* opcional é o conjunto de caracteres que será usado na
   codificação **RFC 2047** do "realname" se o "realname" contiver
   caracteres não-ASCII. Pode ser uma instância de "str" ou a
   "Charset". O padrão é "utf-8".

   Alterado na versão 3.3: Adicionada a opção *charset*.

email.utils.getaddresses(fieldvalues, *, strict=True)

   This function returns a list of 2-tuples of the form returned by
   "parseaddr()". *fieldvalues* is a sequence of header field values
   as might be returned by "Message.get_all()".

   Se *strict* for verdadeiro, usa um analisador sintático estrito que
   rejeite entradas malformadas.

   Aqui está um exemplo simples que recebe todos os destinatários de
   uma mensagem:

      from email.utils import getaddresses

      tos = msg.get_all('to', [])
      ccs = msg.get_all('cc', [])
      resent_tos = msg.get_all('resent-to', [])
      resent_ccs = msg.get_all('resent-cc', [])
      all_recipients = getaddresses(tos + ccs + resent_tos + resent_ccs)

   Alterado na versão 3.13: Adiciona o parâmetro opcional *strict* e
   rejeita entradas malformadas por padrão.

email.utils.parsedate(date)

   Attempts to parse a date according to the rules in **RFC 2822
   Section 3.3**. However, some mailers don't follow that format as
   specified, so "parsedate()" tries to guess correctly in such cases.
   *date* is a string containing an **RFC 2822** date, such as ""Mon,
   20 Nov 1995 19:12:08 -0500"".  If it succeeds in parsing the date,
   "parsedate()" returns a 9-tuple that can be passed directly to
   "time.mktime()"; otherwise "None" will be returned.  Note that
   indexes 6, 7, and 8 of the result tuple are not usable.

email.utils.parsedate_tz(date)

   Executa a mesma função que "parsedate()", mas retorna "None" ou uma
   tupla de 10; os primeiros 9 elementos formam uma tupla que pode ser
   passada diretamente para "time.mktime()", e o décimo é o
   deslocamento do fuso horário da data do UTC (que é o termo oficial
   para o horário de Greenwich) [1]. Se a string de entrada não tem
   fuso horário, o último elemento da tupla retornado é "0", que
   representa UTC. Observe que os índices 6, 7 e 8 da tupla de
   resultado não podem ser usados.

email.utils.parsedate_to_datetime(date)

   The inverse of "format_datetime()".  Performs the same function as
   "parsedate()", but on success returns a "datetime"; otherwise
   "ValueError" is raised if *date* contains an invalid value such as
   an hour greater than 23 or a timezone offset not between -24 and 24
   hours. If the input date has a timezone of "-0000", the "datetime"
   will be a naive "datetime", and if the date conforms to the RFCs it
   will represent a time in UTC but with no indication of the actual
   source timezone of the message the date comes from.  If the input
   date has any other valid timezone offset, the "datetime" will be an
   aware "datetime" whose corresponding "tzinfo" attribute is a
   "timezone" object.

   Adicionado na versão 3.3.

email.utils.mktime_tz(tuple)

   Transforma uma tupla de 10 conforme retornado por "parsedate_tz()"
   em um timestamp UTC (segundos desde a Era Unix). Se o item de fuso
   horário na tupla for "None", considera a hora local.

email.utils.formatdate(timeval=None, localtime=False, usegmt=False)

   Returns a date string as per **RFC 2822**, for example:

      Fri, 09 Nov 2001 01:08:47 -0000

   Optional *timeval*, if given, is a floating-point time value as
   accepted by "time.gmtime()" and "time.localtime()", otherwise the
   current time is used.

   Optional *localtime* is a flag that when "True", interprets
   *timeval*, and returns a date relative to the local timezone
   instead of UTC, properly taking daylight saving time into account.
   The default is "False" meaning UTC is used.

   Optional *usegmt* is a flag that when "True", outputs a date string
   with the timezone as an ASCII string "GMT", rather than a numeric
   "-0000". This is needed for some protocols (such as HTTP). This
   only applies when *localtime* is "False".  The default is "False".

email.utils.format_datetime(dt, usegmt=False)

   Like "formatdate()", but the input is a "datetime" instance. If it
   is a naive datetime, it is assumed to be "UTC with no information
   about the source timezone", and the conventional "-0000" is used
   for the timezone. If it is an aware "datetime", then the numeric
   timezone offset is used. If it is an aware timezone with offset
   zero, then *usegmt* may be set to "True", in which case the string
   "GMT" is used instead of the numeric timezone offset.  This
   provides a way to generate standards-conformant HTTP date headers.

   Adicionado na versão 3.3.

email.utils.decode_rfc2231(s)

   Decodifica a string *s* de acordo com **RFC 2231**.

email.utils.encode_rfc2231(s, charset=None, language=None)

   Encode the string *s* according to **RFC 2231**.  Optional
   *charset* and *language*, if given, are the character set name and
   language name to use.  If neither is given, *s* is returned as-is.
   If *charset* is given but *language* is not, the string is encoded
   using the empty string for *language*.

email.utils.collapse_rfc2231_value(value, errors='replace', fallback_charset='us-ascii')

   When a header parameter is encoded in **RFC 2231** format,
   "Message.get_param()" may return a 3-tuple containing the character
   set, language, and value.  "collapse_rfc2231_value()" turns this
   into a string.  Optional *errors* is passed to the *errors*
   argument of "str"'s "encode()" method; it defaults to "'replace'".
   Optional *fallback_charset* specifies the character set to use if
   the one in the **RFC 2231** header is not known by Python; it
   defaults to "'us-ascii'".

   Por conveniência, se *value* passado para
   "collapse_rfc2231_value()" não for uma tupla, deve ser uma string e
   é retornado sem aspas.

email.utils.decode_params(params)

   Decodifica a lista de parâmetros de acordo com **RFC 2231**.
   *params* é uma sequência de 2 tuplas contendo elementos do
   formulário "(content-type, string-value)".

-[ Notas de rodapé ]-

[1] Note that the sign of the timezone offset is the opposite of the
    sign of the "time.timezone" variable for the same timezone; the
    latter variable follows the POSIX standard while this module
    follows **RFC 2822**.
