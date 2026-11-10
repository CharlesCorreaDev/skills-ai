"zoneinfo" --- Suporte a fuso horário da IANA
*********************************************

Adicionado na versão 3.9.

**Código-fonte:** Lib/zoneinfo

======================================================================

The "zoneinfo" module provides a concrete time zone implementation to
support the IANA time zone database as originally specified in **PEP
615**. By default, "zoneinfo" uses the system's time zone data if
available; if no system time zone data is available, the library will
fall back to using the first-party tzdata package available on PyPI.

Ver também:

  Módulo: "datetime"
     Fornece os tipos "time" e "datetime" com os quais a classe
     "ZoneInfo" foi projetada para ser usada.

  Pacote tzdata
     Pacote próprio mantido pelos desenvolvedores principais do
     CPython para fornecer dados de fuso horário via PyPI.

Disponibilidade: not WASI.

Este módulo não funciona ou não está disponível em WebAssembly. Veja
Plataformas WebAssembly para mais informações.


Usando "ZoneInfo"
=================

"ZoneInfo" é uma implementação concreta da classe base abstrata
"datetime.tzinfo" e deve ser anexada a "tzinfo", por meio do
construtor, do método "datetime.replace" ou "datetime.astimezone":

   >>> from zoneinfo import ZoneInfo
   >>> import datetime as dt

   >>> when = dt.datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
   >>> print(when)
   2020-10-31 12:00:00-07:00

   >>> when.tzname()
   'PDT'

Datas e horas construídas dessa maneira são compatíveis com a
aritmética de data e hora e lidam com transições de horário de verão
sem intervenção adicional:

   >>> when_add = when + dt.timedelta(days=1)

   >>> print(when_add)
   2020-11-01 12:00:00-08:00

   >>> when_add.tzname()
   'PST'

Esses fusos horários também oferecem suporte ao atributo "fold"
introduzido em **PEP 495**. Durante transições de deslocamento que
induzem horários ambíguos (como uma transição do horário de verão para
o horário padrão), o deslocamento *anterior* à transição é usado
quando "fold=0", e o deslocamento *posterior* à transição é usado
quando "fold=1", por exemplo:

   >>> when = dt.datetime(2020, 11, 1, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
   >>> print(when)
   2020-11-01 01:00:00-07:00

   >>> print(when.replace(fold=1))
   2020-11-01 01:00:00-08:00

Ao converter de outro fuso horário, a dobra será definida para o valor
correto:

   >>> LOS_ANGELES = ZoneInfo("America/Los_Angeles")
   >>> when_utc = dt.datetime(2020, 11, 1, 8, tzinfo=dt.timezone.utc)

   >>> # Before the PDT -> PST transition
   >>> print(when_utc.astimezone(LOS_ANGELES))
   2020-11-01 01:00:00-07:00

   >>> # After the PDT -> PST transition
   >>> print((when_utc + dt.timedelta(hours=1)).astimezone(LOS_ANGELES))
   2020-11-01 01:00:00-08:00


Fontes de dados
===============

O módulo "zoneinfo" não fornece dados de fuso horário diretamente,
mas, em vez disso, extrai informações de fuso horário do banco de
dados de fuso horário do sistema ou do pacote PyPI original tzdata, se
disponível. Alguns sistemas, incluindo principalmente os Windows, não
possuem um banco de dados IANA disponível e, portanto, para projetos
que buscam compatibilidade multiplataforma e exigem dados de fuso
horário, recomenda-se declarar uma dependência em tzdata. Se nem os
dados do sistema nem o tzdata estiverem disponíveis, todas as chamadas
para "ZoneInfo" levantarão "ZoneInfoNotFoundError".


Configurando as fontes de dados
-------------------------------

Quando "ZoneInfo(key)" é chamado, o construtor primeiro pesquisa nos
diretórios especificados em "TZPATH" por um arquivo que corresponda a
"key" e, em caso de falha, procura uma correspondência no pacote
tzdata. Esse comportamento pode ser configurado de três maneiras:

1. O padrão "TZPATH", quando não especificado de outra forma, pode ser
   configurado em tempo de compilação.

2. "TZPATH" pode ser configurado usando uma variável de ambiente.

3. Em tempo de execução, o caminho de pesquisa pode ser manipulado
   usando a função "reset_tzpath()".


Configuração em tempo de compilação
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O "TZPATH" padrão inclui vários locais de implantação comuns para o
banco de dados de fuso horário (exceto no Windows, onde não há locais
"conhecidos" para dados de fuso horário). Em sistemas POSIX,
distribuidores downstream e aqueles que constroem o Python a partir do
código-fonte e que sabem onde os dados de fuso horário do sistema
estão implantados podem alterar o caminho do fuso horário padrão
especificando a opção de tempo de compilação "TZPATH" (ou, mais
provavelmente, o "sinalizador de configuração --with-tzpath"), que
deve ser uma string delimitada por "os.pathsep".

Em todas as plataformas, o valor configurado está disponível como a
chave "TZPATH" em "sysconfig.get_config_var()".


Configuração do ambiente
~~~~~~~~~~~~~~~~~~~~~~~~

Ao inicializar "TZPATH" (no momento da importação ou sempre que
"reset_tzpath()" for chamado sem argumentos), o módulo "zoneinfo"
usará a variável de ambiente "PYTHONTZPATH", se existir, para definir
o caminho de pesquisa.

PYTHONTZPATH

   Esta é uma string separada por "os.pathsep" contendo o caminho de
   pesquisa de fuso horário a ser usado. Ela deve consistir apenas em
   caminhos absolutos, e não relativos. Componentes relativos
   especificados em "PYTHONTZPATH" não serão usados, mas, caso
   contrário, o comportamento quando um caminho relativo é
   especificado é definido pela implementação; o CPython levantará
   "InvalidTZPathWarning", mas outras implementações podem ignorar
   silenciosamente o componente incorreto ou levantar uma exceção.

Para configurar o sistema para ignorar os dados do sistema e usar o
pacote tzdata, defina "PYTHONTZPATH=""".


Configuração em tempo de execução
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O caminho de busca TZ também pode ser configurado em tempo de execução
usando a função "reset_tzpath()". Geralmente, essa não é uma operação
aconselhável, embora seja razoável usá-la em funções de teste que
exigem o uso de um caminho de fuso horário específico (ou que exijam a
desativação do acesso aos fusos horários do sistema).


A classe "ZoneInfo"
===================

class zoneinfo.ZoneInfo(key)

   Uma subclasse concreta de "datetime.tzinfo" que representa um fuso
   horário IANA especificado pela string "key". Chamadas ao construtor
   primário sempre retornarão objetos que sejam idênticos em
   comparação; em outras palavras, exceto pela invalidação de cache
   via "ZoneInfo.clear_cache()", para todos os valores de "key", a
   seguinte asserção será sempre verdadeira:

      a = ZoneInfo(key)
      b = ZoneInfo(key)
      assert a is b

   "key" deve estar no formato de um caminho POSIX relativo e
   normalizado, sem referências de nível superior. O construtor
   levantará "ValueError" se uma chave não conforme for passada.

   Se nenhum arquivo correspondente a "key" for encontrado, o
   construtor levantará "ZoneInfoNotFoundError".

A classe "ZoneInfo" tem dois construtores alternativos:

classmethod ZoneInfo.from_file(file_obj, /, key=None)

   Constructs a "ZoneInfo" object from a file-like object returning
   bytes (e.g. a file opened in binary mode or an "io.BytesIO"
   object). Unlike the primary constructor, this always constructs a
   new object.

   The "key" parameter sets the name of the zone for the purposes of
   "__str__()" and "__repr__()".

   Objects created via this constructor cannot be pickled (see
   pickling).

   "ValueError" is raised if the data read from *file_obj* is not a
   valid TZif file.

classmethod ZoneInfo.no_cache(key)

   An alternate constructor that bypasses the constructor's cache. It
   is identical to the primary constructor, but returns a new object
   on each call. This is most likely to be useful for testing or
   demonstration purposes, but it can also be used to create a system
   with a different cache invalidation strategy.

   Objects created via this constructor will also bypass the cache of
   a deserializing process when unpickled.

   Cuidado:

     Using this constructor may change the semantics of your datetimes
     in surprising ways, only use it if you know that you need to.

The following class methods are also available:

classmethod ZoneInfo.clear_cache(*, only_keys=None)

   A method for invalidating the cache on the "ZoneInfo" class. If no
   arguments are passed, all caches are invalidated and the next call
   to the primary constructor for each key will return a new instance.

   If an iterable of key names is passed to the "only_keys" parameter,
   only the specified keys will be removed from the cache. Keys passed
   to "only_keys" but not found in the cache are ignored.

   Aviso:

     Invoking this function may change the semantics of datetimes
     using "ZoneInfo" in surprising ways; this modifies module state
     and thus may have wide-ranging effects. Only use it if you know
     that you need to.

A classe possui um atributo:

ZoneInfo.key

   This is a read-only *attribute* that returns the value of "key"
   passed to the constructor, which should be a lookup key in the IANA
   time zone database (e.g. "America/New_York", "Europe/Paris" or
   "Asia/Tokyo").

   For zones constructed from file without specifying a "key"
   parameter, this will be set to "None".

   Nota:

     Although it is a somewhat common practice to expose these to end
     users, these values are designed to be primary keys for
     representing the relevant zones and not necessarily user-facing
     elements.  Projects like CLDR (the Unicode Common Locale Data
     Repository) can be used to get more user-friendly strings from
     these keys.


String representations
----------------------

The string representation returned when calling "str" on a "ZoneInfo"
object defaults to using the "ZoneInfo.key" attribute (see the note on
usage in the attribute documentation):

   >>> zone = ZoneInfo("Pacific/Kwajalein")
   >>> str(zone)
   'Pacific/Kwajalein'

   >>> when = dt.datetime(2020, 4, 1, 3, 15, tzinfo=zone)
   >>> f"{when.isoformat()} [{when.tzinfo}]"
   '2020-04-01T03:15:00+12:00 [Pacific/Kwajalein]'

For objects constructed from a file without specifying a "key"
parameter, "str" falls back to calling "repr()". "ZoneInfo"'s "repr"
is implementation-defined and not necessarily stable between versions,
but it is guaranteed not to be a valid "ZoneInfo" key.


Pickle serialization
--------------------

Rather than serializing all transition data, "ZoneInfo" objects are
serialized by key, and "ZoneInfo" objects constructed from files (even
those with a value for "key" specified) cannot be pickled.

The behavior of a "ZoneInfo" file depends on how it was constructed:

1. "ZoneInfo(key)": When constructed with the primary constructor, a
   "ZoneInfo" object is serialized by key, and when deserialized, the
   deserializing process uses the primary and thus it is expected that
   these are the same object as other references to the same time
   zone.  For example, if "europe_berlin_pkl" is a string containing a
   pickle constructed from "ZoneInfo("Europe/Berlin")", one would
   expect the following behavior:

      >>> a = ZoneInfo("Europe/Berlin")
      >>> b = pickle.loads(europe_berlin_pkl)
      >>> a is b
      True

2. "ZoneInfo.no_cache(key)": When constructed from the cache-bypassing
   constructor, the "ZoneInfo" object is also serialized by key, but
   when deserialized, the deserializing process uses the cache
   bypassing constructor. If "europe_berlin_pkl_nc" is a string
   containing a pickle constructed from
   "ZoneInfo.no_cache("Europe/Berlin")", one would expect the
   following behavior:

      >>> a = ZoneInfo("Europe/Berlin")
      >>> b = pickle.loads(europe_berlin_pkl_nc)
      >>> a is b
      False

3. "ZoneInfo.from_file(file_obj, /, key=None)": When constructed from
   a file, the "ZoneInfo" object raises an exception on pickling. If
   an end user wants to pickle a "ZoneInfo" constructed from a file,
   it is recommended that they use a wrapper type or a custom
   serialization function: either serializing by key or storing the
   contents of the file object and serializing that.

This method of serialization requires that the time zone data for the
required key be available on both the serializing and deserializing
side, similar to the way that references to classes and functions are
expected to exist in both the serializing and deserializing
environments. It also means that no guarantees are made about the
consistency of results when unpickling a "ZoneInfo" pickled in an
environment with a different version of the time zone data.


Funções
=======

zoneinfo.available_timezones()

   Get a set containing all the valid keys for IANA time zones
   available anywhere on the time zone path. This is recalculated on
   every call to the function.

   This function only includes canonical zone names and does not
   include "special" zones such as those under the "posix/" and
   "right/" directories, the "posixrules"  or the "localtime" zone.

   Cuidado:

     This function may open a large number of files, as the best way
     to determine if a file on the time zone path is a valid time zone
     is to read the "magic string" at the beginning.

   Nota:

     These values are not designed to be exposed to end-users; for
     user facing elements, applications should use something like CLDR
     (the Unicode Common Locale Data Repository) to get more user-
     friendly strings. See also the cautionary note on "ZoneInfo.key".

zoneinfo.reset_tzpath(to=None)

   Sets or resets the time zone search path ("TZPATH") for the module.
   When called with no arguments, "TZPATH" is set to the default
   value.

   Calling "reset_tzpath" will not invalidate the "ZoneInfo" cache,
   and so calls to the primary "ZoneInfo" constructor will only use
   the new "TZPATH" in the case of a cache miss.

   The "to" parameter must be a *sequence* of strings or "os.PathLike"
   and not a string, all of which must be absolute paths. "ValueError"
   will be raised if something other than an absolute path is passed.


Globals
=======

zoneinfo.TZPATH

   A read-only sequence representing the time zone search path -- when
   constructing a "ZoneInfo" from a key, the key is joined to each
   entry in the "TZPATH", and the first file found is used.

   "TZPATH" may contain only absolute paths, never relative paths,
   regardless of how it is configured.

   The object that "zoneinfo.TZPATH" points to may change in response
   to a call to "reset_tzpath()", so it is recommended to use
   "zoneinfo.TZPATH" rather than importing "TZPATH" from "zoneinfo" or
   assigning a long-lived variable to "zoneinfo.TZPATH".

   For more information on configuring the time zone search path, see
   Configurando as fontes de dados.


Exceptions and warnings
=======================

exception zoneinfo.ZoneInfoNotFoundError

   Raised when construction of a "ZoneInfo" object fails because the
   specified key could not be found on the system. This is a subclass
   of "KeyError".

exception zoneinfo.InvalidTZPathWarning

   Raised when "PYTHONTZPATH" contains an invalid component that will
   be filtered out, such as a relative path.
