"urllib.parse" --- Analisa URLs para componentes
************************************************

**Código-fonte:** Lib/urllib/parse.py

======================================================================

Este módulo define uma interface padrão para quebrar strings de
Uniform Resource Locator (URL) em componentes (esquema de
endereçamento, local de rede, caminho etc.), para combinar os
componentes de volta em uma string de URL e para converter uma "URL
relativo" em uma URL absoluta dado uma "URL base".

O módulo foi projetado para corresponder ao RFC da internet sobre
Localizadores de Recursos Uniformes Relativos, ou URL relativa. Ele
tem suporte aos seguintes esquemas de URL: "file", "ftp", "gopher",
"hdl", "http", "https", "imap", "itms-services", "mailto", "mms",
"news", "nntp", "prospero", "rsync", "rtsp", "rtsps",``rtspu``,
"sftp", "shttp", "sip", "sips", "snews", "svn", "svn+ssh", "telnet",
"wais", "ws", "wss".

A inclusão do esquema de URL "itms-services" pode impedir que uma
aplicação passe pelo processo de revisão da App Store da Apple para as
App Stores do macOS e iOS. O tratamento do esquema "itms-services" é
sempre removido no iOS; no macOS, ele *pode* ser removido se o CPython
tiver sido criado com a opção "--with-app-store-compliance".

The "urllib.parse" module defines functions that fall into two broad
categories: URL parsing and URL quoting. These are covered in detail
in the following sections.

As funções deste módulo usam o termo descontinuado "netloc" (ou
"net_loc"), que foi introduzido no **RFC 1808**. No entanto, este
termo foi descontinuado pelo **RFC 3986**, que introduziu o termo
"authority" como seu substituto. O uso de "netloc" continua para
compatibilidade com versões anteriores.


Análise de URL
==============

As funções de análise de URL se concentram na divisão de uma string de
URL em seus componentes ou na combinação de componentes de URL em uma
string de URL.

urllib.parse.urlsplit(urlstring, scheme=None, allow_fragments=True, *, missing_as_none=False)

   Parse a URL into five components, returning a 5-item *named tuple*
   "SplitResult" or "SplitResultBytes". This corresponds to the
   general structure of a URL: "scheme://netloc/path?query#fragment".
   Each tuple item is a string, possibly empty, or "None" if
   *missing_as_none* is true. Not defined component are represented an
   empty string (by default) or "None" if *missing_as_none* is true.
   The delimiters as shown above are not part of the result, except
   for a leading slash in the *path* component, which is retained if
   present.

   Additionally, the netloc property is broken down into these
   additional attributes added to the returned object: username,
   password, hostname, and port.

   Percent-encoded sequences are not decoded.

   Por exemplo:

      >>> from urllib.parse import urlsplit
      >>> urlsplit("scheme://netloc/path?query#fragment")
      SplitResult(scheme='scheme', netloc='netloc', path='/path',
                  query='query', fragment='fragment')
      >>> o = urlsplit("http://docs.python.org:80/3/library/urllib.parse.html?"
      ...              "highlight=params#url-parsing")
      >>> o
      SplitResult(scheme='http', netloc='docs.python.org:80',
                  path='/3/library/urllib.parse.html',
                  query='highlight=params', fragment='url-parsing')
      >>> o.scheme
      'http'
      >>> o.netloc
      'docs.python.org:80'
      >>> o.hostname
      'docs.python.org'
      >>> o.port
      80
      >>> o._replace(fragment="").geturl()
      'http://docs.python.org:80/3/library/urllib.parse.html?highlight=params'
      >>> urlsplit("http://docs.python.org?")
      SplitResult(scheme='http', netloc='docs.python.org', path='',
                  query='', fragment='')
      >>> urlsplit("http://docs.python.org?", missing_as_none=True)
      SplitResult(scheme='http', netloc='docs.python.org', path='',
                  query='', fragment=None)

   Following the syntax specifications in **RFC 1808**, "urlsplit()"
   recognizes a netloc only if it is properly introduced by '//'.
   Otherwise the input is presumed to be a relative URL and thus to
   start with a path component.

      >>> from urllib.parse import urlsplit
      >>> urlsplit('//www.cwi.nl:80/%7Eguido/Python.html')
      SplitResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')
      >>> urlsplit('www.cwi.nl/%7Eguido/Python.html')
      SplitResult(scheme='', netloc='', path='www.cwi.nl/%7Eguido/Python.html',
                  query='', fragment='')
      >>> urlsplit('help/Python.html')
      SplitResult(scheme='', netloc='', path='help/Python.html',
                  query='', fragment='')
      >>> urlsplit('help/Python.html', missing_as_none=True)
      SplitResult(scheme=None, netloc=None, path='help/Python.html',
                  query=None, fragment=None)

   The *scheme* argument gives the default addressing scheme, to be
   used only if the URL does not specify one.  It should be the same
   type (text or bytes) as *urlstring* or "None", except that the "''"
   is always allowed, and is automatically converted to "b''" if
   appropriate.

   If the *allow_fragments* argument is false, fragment identifiers
   are not recognized.  Instead, they are parsed as part of the path
   or query component, and "fragment" is set to "None" or the empty
   string (depending on the value of *missing_as_none*) in the return
   value.

   O valor de retorno é uma *tupla nomeada*, o que significa que seus
   itens podem ser acessados por índice ou como atributos nomeados,
   que são:

   +--------------------+---------+---------------------------+---------------------------------+
   | Atributo           | Índice  | Valor                     | Valor, se não presente          |
   |====================|=========|===========================|=================================|
   | "scheme"           | 0       | Especificador do esquema  | *scheme* parameter or empty     |
   |                    |         | da URL                    | string [1]                      |
   +--------------------+---------+---------------------------+---------------------------------+
   | "netloc"           | 1       | Parte da localização na   | "None" or empty string [1]      |
   |                    |         | rede                      |                                 |
   +--------------------+---------+---------------------------+---------------------------------+
   | "path"             | 2       | Caminho hierárquico       | string vazia                    |
   +--------------------+---------+---------------------------+---------------------------------+
   | "query"            | 3       | Componente da consulta    | "None" or empty string [1]      |
   +--------------------+---------+---------------------------+---------------------------------+
   | "fragment"         | 4       | Identificador do          | "None" or empty string [1]      |
   |                    |         | fragmento                 |                                 |
   +--------------------+---------+---------------------------+---------------------------------+
   | "username"         |         | Nome do usuário           | "None"                          |
   +--------------------+---------+---------------------------+---------------------------------+
   | "password"         |         | Senha                     | "None"                          |
   +--------------------+---------+---------------------------+---------------------------------+
   | "hostname"         |         | Nome de máquina (em       | "None"                          |
   |                    |         | minúsculo)                |                                 |
   +--------------------+---------+---------------------------+---------------------------------+
   | "port"             |         | Número da porta como      | "None"                          |
   |                    |         | inteiro, se presente      |                                 |
   +--------------------+---------+---------------------------+---------------------------------+

   [1] Depending on the value of the *missing_as_none* argument.

   Ler o atributo "port" irá levantar uma "ValueError" se uma porta
   inválida for especificada no URL. Veja a seção Structured Parse
   Results para mais informações sobre o objeto de resultado.

   Colchetes sem correspondência no atributo "netloc" levantará uma
   "ValueError".

   Caracteres no atributo "netloc" que se decompõem sob a normalização
   NFKC (como usado pela codificação IDNA) em qualquer um dos "/",
   "?", "#", "@" ou ":" vai levantar uma "ValueError". Se a URL for
   decomposta antes da análise, nenhum erro será levantado.

   Following some of the WHATWG spec that updates **RFC 3986**,
   leading C0 control and space characters are stripped from the URL.
   "\n", "\r" and tab "\t" characters are removed from the URL at any
   position.

   As is the case with all named tuples, the subclass has a few
   additional methods and attributes that are particularly useful. One
   such method is "_replace()". The "_replace()" method will return a
   new "SplitResult" object replacing specified fields with new
   values.

      >>> from urllib.parse import urlsplit
      >>> u = urlsplit('//www.cwi.nl:80/%7Eguido/Python.html')
      >>> u
      SplitResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')
      >>> u._replace(scheme='http')
      SplitResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')

   Aviso:

     "urlsplit()" não executa validação. Veja Segurança ao analisar
     URLs para detalhes.

   Alterado na versão 3.2: Adicionados recursos de análise de URL
   IPv6.

   Alterado na versão 3.3: O fragmento agora é analisado para todos os
   esquemas de URL (a menos que *allow_fragments* seja falso), de
   acordo com a **RFC 3986**. Anteriormente, existia uma lista de
   permitidos de esquemas que suportam fragmentos.

   Alterado na versão 3.6: Out-of-range port numbers now raise
   "ValueError", instead of returning "None".

   Alterado na versão 3.8: Os caracteres que afetam a análise de
   netloc sob normalização NFKC agora levantarão "ValueError".

   Alterado na versão 3.10: Caracteres de nova linha e tabulação ASCII
   são removidos do URL.

   Alterado na versão 3.12: Os caracteres iniciais de espaço e de
   controle WHATWG C0 são removidos do URL.

   Alterado na versão 3.15: Added the *missing_as_none* parameter.

urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&')

   Analisa uma string de consulta fornecida como um argumento de
   string (dados do tipo *application/x-www-form-urlencoded*). Os
   dados são retornados como um dicionário. As chaves de dicionário
   são os nomes de variáveis de consulta exclusivos e os valores são
   listas de valores para cada nome.

   O argumento opcional *keep_blank_values* é um sinalizador que
   indica se os valores em branco em consultas codificadas por
   porcentagem devem ser tratados como strings em branco. Um valor
   verdadeiro indica que os espaços em branco devem ser mantidos como
   strings em branco. O valor falso padrão indica que os valores em
   branco devem ser ignorados e tratados como se não tivessem sido
   incluídos.

   O argumento opcional *strict_parsing* é um sinalizador que indica o
   que fazer com os erros de análise. Se falso (padrão), os erros são
   ignorados silenciosamente. Se verdadeiro, os erros levantam uma
   exceção "ValueError".

   Os parâmetros opcionais *encoding* e *errors* especificam como
   decodificar sequências codificadas em porcentagem em caracteres
   Unicode, conforme aceito pelo método "bytes.decode()".

   O argumento opcional *max_num_fields* é o número máximo de campos a
   serem lidos. Se definido, então levanta um "ValueError" se houver
   mais de *max_num_fields* campos lidos.

   O argumento opcional *separador* é o símbolo a ser usado para
   separar os argumentos da consulta. O padrão é "&".

   Use a função "urllib.parse.urlencode()" (com o parâmetro "doseq"
   definido como "True") para converter esses dicionários em strings
   de consulta.

   Alterado na versão 3.2: Adicionado os parâmetros *encoding* e
   *errors*.

   Alterado na versão 3.8: Adicionado o parâmetro *max_num_fields*.

   Alterado na versão 3.10: Adicionado parâmetro *separator* com o
   valor padrão de "&". Versões do Python anteriores ao Python 3.10
   permitiam o uso de ";" e "&" como separador de parâmetro de
   consulta. Isso foi alterado para permitir apenas uma única chave
   separadora, com "&" como o separador padrão.

   Descontinuado desde a versão 3.14: Accepting objects with false
   values (like "0" and "[]") except empty strings and byte-like
   objects and "None" is now deprecated.

urllib.parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&')

   Analisa uma string de consulta fornecida como um argumento de
   string (dados do tipo *application/x-www-form-urlencoded*). Os
   dados são retornados como uma lista de pares de nome e valor.

   O argumento opcional *keep_blank_values* é um sinalizador que
   indica se os valores em branco em consultas codificadas por
   porcentagem devem ser tratados como strings em branco. Um valor
   verdadeiro indica que os espaços em branco devem ser mantidos como
   strings em branco. O valor falso padrão indica que os valores em
   branco devem ser ignorados e tratados como se não tivessem sido
   incluídos.

   O argumento opcional *strict_parsing* é um sinalizador que indica o
   que fazer com os erros de análise. Se falso (padrão), os erros são
   ignorados silenciosamente. Se verdadeiro, os erros levantam uma
   exceção "ValueError".

   Os parâmetros opcionais *encoding* e *errors* especificam como
   decodificar sequências codificadas em porcentagem em caracteres
   Unicode, conforme aceito pelo método "bytes.decode()".

   O argumento opcional *max_num_fields* é o número máximo de campos a
   serem lidos. Se definido, então levanta um "ValueError" se houver
   mais de *max_num_fields* campos lidos.

   O argumento opcional *separador* é o símbolo a ser usado para
   separar os argumentos da consulta. O padrão é "&".

   Use a função "urllib.parse.urlencode()" para converter essas listas
   pares de strings de consulta.

   Alterado na versão 3.2: Adicionado os parâmetros *encoding* e
   *errors*.

   Alterado na versão 3.8: Adicionado o parâmetro *max_num_fields*.

   Alterado na versão 3.10: Adicionado parâmetro *separator* com o
   valor padrão de "&". Versões do Python anteriores ao Python 3.10
   permitiam o uso de ";" e "&" como separador de parâmetro de
   consulta. Isso foi alterado para permitir apenas uma única chave
   separadora, com "&" como o separador padrão.

urllib.parse.urlunsplit(parts)
urllib.parse.urlunsplit(parts, *, keep_empty)

   Construct a URL from a tuple as returned by "urlsplit()". The
   *parts* argument can be any five-item iterable.

   This may result in a slightly different, but equivalent URL, if the
   URL that was parsed originally had unnecessary delimiters (for
   example, a "?" with an empty query; the RFC states that these are
   equivalent).

   If *keep_empty* is true, empty strings are kept in the result (for
   example, a "?" for an empty query), only "None" components are
   omitted. This allows rebuilding a URL that was parsed with option
   "missing_as_none=True". By default, *keep_empty* is true if *parts*
   is the result of the "urlsplit()" call with "missing_as_none=True".

   Alterado na versão 3.15: Added the *keep_empty* parameter.

urllib.parse.urlparse(urlstring, scheme=None, allow_fragments=True, *, missing_as_none=False)

   This is similar to "urlsplit()", but additionally splits the *path*
   component on *path* and *params*. This function returns a 6-item
   *named tuple* "ParseResult" or "ParseResultBytes". Its items are
   the same as for the "urlsplit()" result, except that *params* is
   inserted at index 3, between *path* and *query*.

   This function is based on obsoleted **RFC 1738** and **RFC 1808**,
   which listed *params* as the main URL component. The more recent
   URL syntax allows parameters to be applied to each segment of the
   *path* portion of the URL (see **RFC 3986**). "urlsplit()" should
   generally be used instead of "urlparse()". A separate function is
   needed to separate the path segments and parameters.

urllib.parse.urlunparse(parts)
urllib.parse.urlunparse(parts, *, keep_empty)

   Combine the elements of a tuple as returned by "urlparse()" into a
   complete URL as a string. The *parts* argument can be any six-item
   iterable.

   This may result in a slightly different, but equivalent URL, if the
   URL that was parsed originally had unnecessary delimiters (for
   example, a "?" with an empty query; the RFC states that these are
   equivalent).

   If *keep_empty* is true, empty strings are kept in the result (for
   example, a "?" for an empty query), only "None" components are
   omitted. This allows rebuilding a URL that was parsed with option
   "missing_as_none=True". By default, *keep_empty* is true if *parts*
   is the result of the "urlparse()" call with "missing_as_none=True".

   Alterado na versão 3.15: Added the *keep_empty* parameter.

urllib.parse.urljoin(base, url, allow_fragments=True)

   Constrói uma URL completa ("absoluta") combinando uma "URL base"
   (*base*) com outra URL (*url*). Informalmente, isso usa componentes
   da URL base, em particular o esquema de endereçamento, o local da
   rede e (parte do) caminho, para fornecer componentes ausentes na
   URL relativa. Por exemplo:

   >>> from urllib.parse import urljoin
   >>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
   'http://www.cwi.nl/%7Eguido/FAQ.html'

   The *allow_fragments* argument has the same meaning and default as
   for "urlsplit()".

   Nota:

     Se *url* for uma URL absoluta (ou seja, começa com "//" ou
     "scheme://"), o nome do host e/ou esquema da *url* estarão
     presentes no resultado. Por exemplo:

        >>> urljoin('http://www.cwi.nl/%7Eguido/Python.html',
        ...         '//www.python.org/%7Eguido')
        'http://www.python.org/%7Eguido'

     Se você não quiser esse comportamento, pré-processe a *url* com
     "urlsplit()" e "urlunsplit()", removendo possíveis partes
     *scheme* e *netloc*.

   Aviso:

     Como uma URL absoluta pode ser passada como o parâmetro "url",
     geralmente **não é seguro** usar "urljoin" com uma "url"
     controlada pelo invasor. Por exemplo, em
     "urljoin("https://website.com/users/", username)", se "username"
     puder conter uma URL absoluta, o resultado de "urljoin" será a
     URL absoluta.

   Alterado na versão 3.5: Comportamento atualizado para corresponder
   à semântica definida no **RFC 3986**.

urllib.parse.urldefrag(url, *, missing_as_none=False)

   If *url* contains a fragment identifier, return a modified version
   of *url* with no fragment identifier, and the fragment identifier
   as a separate string.  If there is no fragment identifier in *url*,
   return *url* unmodified and an empty string (by default) or "None"
   if *missing_as_none* is true.

   O valor de retorno é uma *tupla nomeada*, seus itens podem ser
   acessados por índice ou como atributos nomeados:

   +--------------------+---------+---------------------------+---------------------------------+
   | Atributo           | Índice  | Valor                     | Valor, se não presente          |
   |====================|=========|===========================|=================================|
   | "url"              | 0       | URL com nenhum fragmento  | string vazia                    |
   +--------------------+---------+---------------------------+---------------------------------+
   | "fragment"         | 1       | Identificador do          | "None" or empty string [3]      |
   |                    |         | fragmento                 |                                 |
   +--------------------+---------+---------------------------+---------------------------------+

   [3] Depending on the value of the *missing_as_none* argument.

   Veja a seção Structured Parse Results para obter mais informações
   sobre o objeto de resultado.

   Alterado na versão 3.2: O resultado é um objeto estruturado em vez
   de uma simples tupla de 2 elementos.

   Alterado na versão 3.15: Added the *missing_as_none* parameter.

urllib.parse.unwrap(url)

   Extrai a URL de uma URL encapsulada (ou seja, uma string formatada
   como "<URL:esquema://host/caminho>", "<esquema://host/caminho>",
   "URL:esquema://host/caminho" ou "esquema://host/caminho"). Se *url*
   não for uma URL encapsulada, ela será retornada sem alterações.


Segurança ao analisar URLs
==========================

As APIs "urlsplit()" e "urlparse()" não realizam **validação** de
entradas. Elas podem não levantar erros em entradas que outras
aplicações consideram inválidas. Elas também podem ter sucesso em
algumas entradas que podem não ser consideradas URLs em outros
lugares. Seu propósito é para funcionalidade prática em vez de pureza.

Instead of raising an exception on unusual input, they may instead
return some component parts as empty strings or "None" (depending on
the value of the *missing_as_none* argument). Or components may
contain more than perhaps they should.

Recomendamos que os usuários dessas APIs, onde os valores podem ser
usados em qualquer lugar com implicações de segurança, codifiquem
defensivamente. Faça alguma verificação dentro do seu código antes de
confiar em uma parte do componente retornada. Esse "esquema" faz
sentido? Esse "caminho" sensato? Há algo estranho sobre esse
"hostname"? etc.

O que constitui uma URL não é universalmente bem definido. Diferentes
aplicações têm diferentes necessidades e restrições desejadas. Por
exemplo, a especificação WHATWG descreve o que os clientes web
voltados para o usuário, como um navegador web, exigem. Por outro
lado, **RFC 3986** é mais geral. Essas funções incorporam alguns
aspectos de ambos, mas não podem ser reivindicadas como compatíveis
com nenhum deles. As APIs e o código de usuário existente com
expectativas sobre comportamentos específicos são anteriores a ambos
os padrões, o que nos leva a ser muito cautelosos ao fazer alterações
no comportamento da API.


Analisando bytes codificados em ASCII
=====================================

As funções de análise de URL foram originalmente projetadas para
operar somente em strings de caracteres. Na prática, é útil ser capaz
de manipular URLs corretamente citadas e codificadas como sequências
de bytes ASCII. Consequentemente, todas as funções de análise de URL
neste módulo operam em objetos "bytes" e "bytearray" além de objetos
"str".

Se dados "str" forem passados, o resultado também conterá apenas dados
"str". Se dados "bytes" ou "bytearray" forem passados, o resultado
conterá apenas dados "bytes".

Tentar misturar dados "str" com "bytes" ou "bytearray" em uma única
chamada de função resultará em uma "TypeError" sendo levantada,
enquanto tentar passar valores de bytes não-ASCII acionará
"UnicodeDecodeError".

Para prover uma conversão mais fácil de objetos de resultado entre
"str" e "bytes", todos os valores de retorno das funções de análise de
URL fornecem um método "encode()" (quando o resultado contém dados
"str") ou um método "decode()" (quando o resultado contém dados
"bytes"). As assinaturas desses métodos correspondem às dos métodos
"str" e "bytes" correspondentes (exceto que a codificação padrão é
"'ascii'" em vez de "'utf-8'"). Cada um produz um valor de um tipo
correspondente que contém dados "bytes" (para métodos "encode()") ou
dados "str" (para métodos "decode()").

Os aplicações que precisam operar em URLs possivelmente envolta em
aspas de forma incorreta, e que podem conter dados não ASCII,
precisarão fazer sua própria decodificação de bytes para caracteres
antes de invocar os métodos de análise de URL.

O comportamento descrito nesta seção se aplica somente às funções de
análise de URL. As funções de aplicação de aspas em URL usam suas
próprias regras ao produzir ou consumir sequências de bytes, conforme
detalhado na documentação das funções de citação de URL individuais.

Alterado na versão 3.2: As funções de análise de URL agora aceitam
sequências de bytes codificadas em ASCII


Structured Parse Results
========================

The result objects from the "urlsplit()", "urlparse()"  and
"urldefrag()" functions are subclasses of the "tuple" type. These
subclasses add the attributes listed in the documentation for those
functions, the encoding and decoding support described in the previous
section, as well as an additional method:

urllib.parse.SplitResult.geturl()

   Return the re-combined version of the original URL as a string.
   This may differ from the original URL in that the scheme may be
   normalized to lower case and empty components may be dropped.
   Specifically, empty parameters, queries, and fragment identifiers
   will be removed unless the URL was parsed with
   "missing_as_none=True".

   For "urldefrag()" results, only empty fragment identifiers will be
   removed. For "urlsplit()" and "urlparse()" results, all noted
   changes will be made to the URL returned by this method.

   The result of this method remains unchanged if passed back through
   the original parsing function:

   >>> from urllib.parse import urlsplit
   >>> url = 'HTTP://www.Python.org/doc/#'
   >>> r1 = urlsplit(url)
   >>> r1.geturl()
   'http://www.Python.org/doc/'
   >>> r2 = urlsplit(r1.geturl())
   >>> r2.geturl()
   'http://www.Python.org/doc/'
   >>> r3 = urlsplit(url, missing_as_none=True)
   >>> r3.geturl()
   'http://www.Python.org/doc/#'

The following classes provide the implementations of the structured
parse results when operating on "str" objects:

class urllib.parse.DefragResult(url, fragment)

   Concrete class for "urldefrag()" results containing "str" data. The
   "encode()" method returns a "DefragResultBytes" instance.

   Adicionado na versão 3.2.

class urllib.parse.ParseResult(scheme, netloc, path, params, query, fragment)

   Concrete class for "urlparse()" results containing "str" data. The
   "encode()" method returns a "ParseResultBytes" instance.

class urllib.parse.SplitResult(scheme, netloc, path, query, fragment)

   Concrete class for "urlsplit()" results containing "str" data. The
   "encode()" method returns a "SplitResultBytes" instance.

The following classes provide the implementations of the parse results
when operating on "bytes" or "bytearray" objects:

class urllib.parse.DefragResultBytes(url, fragment)

   Concrete class for "urldefrag()" results containing "bytes" data.
   The "decode()" method returns a "DefragResult" instance.

   Adicionado na versão 3.2.

class urllib.parse.ParseResultBytes(scheme, netloc, path, params, query, fragment)

   Concrete class for "urlparse()" results containing "bytes" data.
   The "decode()" method returns a "ParseResult" instance.

   Adicionado na versão 3.2.

class urllib.parse.SplitResultBytes(scheme, netloc, path, query, fragment)

   Concrete class for "urlsplit()" results containing "bytes" data.
   The "decode()" method returns a "SplitResult" instance.

   Adicionado na versão 3.2.


URL Quoting
===========

The URL quoting functions focus on taking program data and making it
safe for use as URL components by quoting special characters and
appropriately encoding non-ASCII text. They also support reversing
these operations to recreate the original data from the contents of a
URL component if that task isn't already covered by the URL parsing
functions above.

urllib.parse.quote(string, safe='/', encoding=None, errors=None)

   Replace special characters in *string* using the "%*xx*" escape.
   Letters, digits, and the characters "'_.-~'" are never quoted. By
   default, this function is intended for quoting the path section of
   a URL. The optional *safe* parameter specifies additional ASCII
   characters that should not be quoted --- its default value is
   "'/'".

   *string* may be either a "str" or a "bytes" object.

   Alterado na versão 3.7: Moved from **RFC 2396** to **RFC 3986** for
   quoting URL strings. "~" is now included in the set of unreserved
   characters.

   The optional *encoding* and *errors* parameters specify how to deal
   with non-ASCII characters, as accepted by the "str.encode()"
   method. Although these parameters default to "None" in the function
   signature, when processing "str" inputs, *encoding* effectively
   defaults to "'utf-8'" and *errors* to "'strict'", meaning
   unsupported characters raise a "UnicodeEncodeError". *encoding* and
   *errors* must not be supplied if *string* is a "bytes", or a
   "TypeError" is raised.

   Note that "quote(string, safe, encoding, errors)" is equivalent to
   "quote_from_bytes(string.encode(encoding, errors), safe)".

   Example: "quote('/El Niño/')" yields "'/El%20Ni%C3%B1o/'".

urllib.parse.quote_plus(string, safe='', encoding=None, errors=None)

   Like "quote()", but also replace spaces with plus signs, as
   required for quoting HTML form values when building up a query
   string to go into a URL. Plus signs in the original string are
   escaped unless they are included in *safe*.  It also does not have
   *safe* default to "'/'".

   Example: "quote_plus('/El Niño/')" yields "'%2FEl+Ni%C3%B1o%2F'".

urllib.parse.quote_from_bytes(bytes, safe='/')

   Like "quote()", but accepts a "bytes" object rather than a "str",
   and does not perform string-to-bytes encoding.

   Example: "quote_from_bytes(b'a&\xef')" yields "'a%26%EF'".

urllib.parse.unquote(string, encoding='utf-8', errors='replace')

   Replace "%*xx*" escapes with their single-character equivalent. The
   optional *encoding* and *errors* parameters specify how to decode
   percent-encoded sequences into Unicode characters, as accepted by
   the "bytes.decode()" method.

   *string* may be either a "str" or a "bytes" object.

   *encoding* defaults to "'utf-8'". *errors* defaults to "'replace'",
   meaning invalid sequences are replaced by a placeholder character.

   Example: "unquote('/El%20Ni%C3%B1o/')" yields "'/El Niño/'".

   Alterado na versão 3.9: *string* parameter supports bytes and str
   objects (previously only str).

urllib.parse.unquote_plus(string, encoding='utf-8', errors='replace')

   Like "unquote()", but also replace plus signs with spaces, as
   required for unquoting HTML form values.

   *string* must be a "str".

   Example: "unquote_plus('/El+Ni%C3%B1o/')" yields "'/El Niño/'".

urllib.parse.unquote_to_bytes(string)

   Replace "%*xx*" escapes with their single-octet equivalent, and
   return a "bytes" object.

   *string* may be either a "str" or a "bytes" object.

   If it is a "str", unescaped non-ASCII characters in *string* are
   encoded into UTF-8 bytes.

   Example: "unquote_to_bytes('a%26%EF')" yields "b'a&\xef'".

urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)

   Convert a mapping object or a sequence of two-element tuples, which
   may contain "str" or "bytes" objects, to a percent-encoded ASCII
   text string.  If the resultant string is to be used as a *data* for
   POST operation with the "urlopen()" function, then it should be
   encoded to bytes, otherwise it would result in a "TypeError".

   The resulting string is a series of "key=value" pairs separated by
   "'&'" characters, where both *key* and *value* are quoted using the
   *quote_via* function.  By default, "quote_plus()" is used to quote
   the values, which means spaces are quoted as a "'+'" character and
   '/' characters are encoded as "%2F", which follows the standard for
   GET requests ("application/x-www-form-urlencoded").  An alternate
   function that can be passed as *quote_via* is "quote()", which will
   encode spaces as "%20" and not encode '/' characters.  For maximum
   control of what is quoted, use "quote" and specify a value for
   *safe*.

   When a sequence of two-element tuples is used as the *query*
   argument, the first element of each tuple is a key and the second
   is a value. The value element in itself can be a sequence and in
   that case, if the optional parameter *doseq* evaluates to "True",
   individual "key=value" pairs separated by "'&'" are generated for
   each element of the value sequence for the key.  The order of
   parameters in the encoded string will match the order of parameter
   tuples in the sequence.

   The *safe*, *encoding*, and *errors* parameters are passed down to
   *quote_via* (the *encoding* and *errors* parameters are only passed
   when a query element is a "str").

   To reverse this encoding process, "parse_qs()" and "parse_qsl()"
   are provided in this module to parse query strings into Python data
   structures.

   Refer to urllib examples to find out how the
   "urllib.parse.urlencode()" method can be used for generating the
   query string of a URL or data for a POST request.

   Alterado na versão 3.2: *query* supports bytes and string objects.

   Alterado na versão 3.5: Added the *quote_via* parameter.

   Descontinuado desde a versão 3.14: Accepting objects with false
   values (like "0" and "[]") except empty strings and byte-like
   objects and "None" is now deprecated.

Ver também:

  WHATWG -  URL Living standard
     Working Group for the URL Standard that defines URLs, domains, IP
     addresses, the application/x-www-form-urlencoded format, and
     their API.

  **RFC 3986** - Uniform Resource Identifiers
     This is the current standard (STD66). Any changes to urllib.parse
     module should conform to this. Certain deviations could be
     observed, which are mostly for backward compatibility purposes
     and for certain de-facto parsing requirements as commonly
     observed in major browsers.

  **RFC 2732** - Format for Literal IPv6 Addresses in URL's.
     This specifies the parsing requirements of IPv6 URLs.

  **RFC 2396** - Uniform Resource Identifiers (URI): Generic Syntax
     Document describing the generic syntactic requirements for both
     Uniform Resource Names (URNs) and Uniform Resource Locators
     (URLs).

  **RFC 2368** - O esquema de URL mailto.
     Parsing requirements for mailto URL schemes.

  **RFC 1808** - Relative Uniform Resource Locators
     This Request For Comments includes the rules for joining an
     absolute and a relative URL, including a fair number of "Abnormal
     Examples" which govern the treatment of border cases.

  **RFC 1738** - Uniform Resource Locators (URL)
     This specifies the formal syntax and semantics of absolute URLs.
