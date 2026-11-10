"locale" --- Serviços de internacionalização
********************************************

**Código-fonte:** Lib/locale.py

======================================================================

O módulo "locale" abre o acesso ao banco de dados de localidade POSIX
e funcionalidade. O mecanismo de localidade POSIX permite que os
programadores lidem com certas questões culturais em uma aplicação,
sem exigir que o programador conheça todas as especificidades de cada
país onde o software é executado.

O módulo "locale" é implementado em cima do módulo "_locale", que por
sua vez usa uma implementação a localidade ANSI C se disponível.

O módulo "locale" define a seguinte exceção e funções:

exception locale.Error

   Exceção levantada quando a localidade passada para "setlocale()"
   não é reconhecida.

locale.setlocale(category, locale=None)

   Se *locale* for fornecido e não "None", "setlocale()" modifica a
   configuração de locale para a *category*. As categorias disponíveis
   estão listadas na descrição dos dados abaixo. *locale* pode ser uma
   string ou um par, código de idioma e codificação. Uma string vazia
   especifica as configurações padrão do usuário. Se a modificação da
   localidade falhar, a exceção "Error" é levantada. Se for bem-
   sucedido, a nova configuração de localidade será retornada.

   Se *locale* for um par, ele será convertido em um nome de
   localidade usando o mecanismo de apelidamento de localidade. O
   código de idioma tem o mesmo formato de nome da localidade, mas sem
   codificação. O código de idioma e a codificação podem ser "None".

   Se *locale* for omitido ou "None", a configuração atual para
   *category* é retornada.

   Exemplo:

      >>> import locale
      >>> loc = locale.setlocale(locale.LC_ALL)  # obtém localidade atual
      # usa localidade de alemão; nome e disponibilidade pode variar conforme plataforma
      >>> locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
      >>> locale.strcoll('f\xe4n', 'foo')  # compara uma string contendo um umlaut
      >>> locale.setlocale(locale.LC_ALL, '')   # usa a localidade preferida do usuário
      >>> locale.setlocale(locale.LC_ALL, 'C')  # usa localidade padrão (C)
      >>> locale.setlocale(locale.LC_ALL, loc)  # restaura localidade salva

   "setlocale()" não é seguro para thread na maioria dos sistemas. As
   aplicações normalmente começam com uma chamada de:

      import locale
      locale.setlocale(locale.LC_ALL, '')

   Isso define a localidade de todas as categorias para a configuração
   padrão do usuário (normalmente especificada na variável de ambiente
   "LANG"). Se a localidade não for alterada depois disso, o uso de
   multithreading não deve causar problemas.

   Alterado na versão 3.15: Oferece suporte a códigos de idiomas com
   modificadores "@".

locale.localeconv()

   Retorna o banco de dados das convenções locais como um dicionário.
   Este dicionário possui as seguintes strings como chaves:

   +------------------------+---------------------------------------+----------------------------------+
   | Categoria              | Chave                                 | Significado                      |
   |========================|=======================================|==================================|
   | "LC_NUMERIC"           | "'decimal_point'"                     | Caractere de ponto decimal.      |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'grouping'"                          | Sequência de números             |
   |                        |                                       | especificando quais posições     |
   |                        |                                       | relativas os "'thousands_sep'"   |
   |                        |                                       | são esperados. Se a sequência    |
   |                        |                                       | for terminada com "CHAR_MAX",    |
   |                        |                                       | nenhum agrupamento adicional é   |
   |                        |                                       | realizado. Se a sequência        |
   |                        |                                       | termina com um "0", o tamanho do |
   |                        |                                       | último grupo é usado             |
   |                        |                                       | repetidamente.                   |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'thousands_sep'"                     | Caractere usado entre grupos.    |
   +------------------------+---------------------------------------+----------------------------------+
   | "LC_MONETARY"          | "'int_curr_symbol'"                   | Símbolo internacional de moeda.  |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'currency_symbol'"                   | Símbolo local de moeda.          |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'p_cs_precedes/n_cs_precedes'"       | Se o símbolo da moeda precede o  |
   |                        |                                       | valor (para valores positivos ou |
   |                        |                                       | negativos).                      |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'p_sep_by_space/n_sep_by_space'"     | Se o símbolo monetário está      |
   |                        |                                       | separado do valor por um espaço  |
   |                        |                                       | (para valores positivos ou       |
   |                        |                                       | negativos).                      |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'mon_decimal_point'"                 | Ponto decimal usado para valores |
   |                        |                                       | monetários.                      |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'frac_digits'"                       | Número de dígitos fracionários   |
   |                        |                                       | usados na formatação local de    |
   |                        |                                       | valores monetários.              |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'int_frac_digits'"                   | Número de dígitos fracionários   |
   |                        |                                       | usados na formatação             |
   |                        |                                       | internacional de valores         |
   |                        |                                       | monetários.                      |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'mon_thousands_sep'"                 | Separador de grupo usado para    |
   |                        |                                       | valores monetários.              |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'mon_grouping'"                      | Equivalente a "'grouping'",      |
   |                        |                                       | usado para valores monetários.   |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'positive_sign'"                     | Símbolo usado para anotar um     |
   |                        |                                       | valor monetário positivo.        |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'negative_sign'"                     | Símbolo usado para anotar um     |
   |                        |                                       | valor monetário negativo.        |
   +------------------------+---------------------------------------+----------------------------------+
   |                        | "'p_sign_posn/n_sign_posn'"           | A posição do sinal (para valores |
   |                        |                                       | positivos resp. negativos), veja |
   |                        |                                       | abaixo.                          |
   +------------------------+---------------------------------------+----------------------------------+

   Todos os valores numéricos podem ser definidos como "CHAR_MAX" para
   indicar que não há valor especificado nesta localidade.

   Os valores possíveis para "'p_sign_posn'" e "'n_sign_posn'" são
   dados abaixo.

   +----------------+-------------------------------------------+
   | Valor          | Explicação                                |
   |================|===========================================|
   | "0"            | A moeda e o valor estão entre parênteses. |
   +----------------+-------------------------------------------+
   | "1"            | O sinal deve preceder o valor e o símbolo |
   |                | da moeda.                                 |
   +----------------+-------------------------------------------+
   | "2"            | O sinal deve seguir o valor e o símbolo   |
   |                | da moeda.                                 |
   +----------------+-------------------------------------------+
   | "3"            | O sinal deve preceder imediatamente o     |
   |                | valor.                                    |
   +----------------+-------------------------------------------+
   | "4"            | O sinal deve seguir imediatamente o       |
   |                | valor.                                    |
   +----------------+-------------------------------------------+
   | "CHAR_MAX"     | Nada é especificado nesta localidade.     |
   +----------------+-------------------------------------------+

   A função define temporariamente a localidade de "LC_CTYPE" para a
   localidade de "LC_NUMERIC" ou a localidade de "LC_MONETARY" se as
   localidades forem diferentes e as strings numéricas ou monetárias
   não forem ASCII. Esta mudança temporária afeta outras threads.

   Alterado na versão 3.7: A função agora define temporariamente a
   localidade de "LC_CTYPE" para a localidade de "LC_NUMERIC" em
   alguns casos.

locale.nl_langinfo(option)

   Retorna algumas informações específicas da localidade em uma
   string. Esta função não está disponível em todos os sistemas e o
   conjunto de opções possíveis também pode variar entre as
   plataformas. Os valores de argumento possíveis são números, para os
   quais constantes simbólicas estão disponíveis no módulo da
   localidade.

   A função "nl_langinfo()" aceita uma das seguintes chaves. A maioria
   das descrições são tiradas da descrição correspondente na
   biblioteca GNU C.

   locale.CODESET

      Obtém uma string com o nome da codificação de caracteres usada
      na localidade selecionado.

   locale.D_T_FMT

      Obtém uma string que pode ser usada como uma string de formato
      para "time.strftime()" para representar a data e a hora de uma
      maneira específica da localidade.

   locale.D_FMT

      Obtém uma string que pode ser usada como uma string de formato
      para "time.strftime()" para representar uma data de uma maneira
      específica da localidade.

   locale.T_FMT

      Obtém uma string que pode ser usada como uma string de formato
      para "time.strftime()" para representar uma hora de uma maneira
      específica da localidade.

   locale.T_FMT_AMPM

      Obtém uma string de formato para "time.strftime()" para
      representar a hora no formato am/pm.

   locale.DAY_1
   locale.DAY_2
   locale.DAY_3
   locale.DAY_4
   locale.DAY_5
   locale.DAY_6
   locale.DAY_7

      Obtém o nome do enésimo dia da semana.

      Nota:

        Isso segue a convenção dos EUA de "DAY_1" ser no domingo, não
        a convenção internacional (ISO 8601) que segunda-feira é o
        primeiro dia da semana.

   locale.ABDAY_1
   locale.ABDAY_2
   locale.ABDAY_3
   locale.ABDAY_4
   locale.ABDAY_5
   locale.ABDAY_6
   locale.ABDAY_7

      Obtém o nome abreviado do enésimo dia da semana.

   locale.MON_1
   locale.MON_2
   locale.MON_3
   locale.MON_4
   locale.MON_5
   locale.MON_6
   locale.MON_7
   locale.MON_8
   locale.MON_9
   locale.MON_10
   locale.MON_11
   locale.MON_12

      Obtém o nome do enésimo dia do mês.

   locale.ABMON_1
   locale.ABMON_2
   locale.ABMON_3
   locale.ABMON_4
   locale.ABMON_5
   locale.ABMON_6
   locale.ABMON_7
   locale.ABMON_8
   locale.ABMON_9
   locale.ABMON_10
   locale.ABMON_11
   locale.ABMON_12

      Obtém o nome abreviado do enésimo dia do mês.

   locale.RADIXCHAR

      Obtém o caractere separador decimal (ponto decimal, vírgula
      decimal etc.).

   locale.THOUSEP

      Obtém o caractere separador para milhares (grupos de três
      dígitos).

   locale.YESEXPR

      Obtém uma expressão regular que pode ser usada com a função
      regex para reconhecer uma resposta positiva a uma pergunta
      sim/não.

   locale.NOEXPR

      Obtém uma expressão regular que pode ser usada com a função
      "regex(3)" para reconhecer uma resposta negativa a uma pergunta
      sim/não.

      Nota:

        As expressões regulares para "YESEXPR" e "NOEXPR" usam uma
        sintaxe adequada para a função "regex" da biblioteca C, que
        pode ser diferente da sintaxe usada em "re".

   locale.CRNCYSTR

      Obtém o símbolo da moeda, precedido por "-" se o símbolo deve
      aparecer antes do valor, "+" se o símbolo deve aparecer após o
      valor ou "." se o símbolo deve substituir o caractere separador
      decimal.

   locale.ERA

      Obtém uma string que descreva como os anos são contados e
      exibidos para cada era em um localidade.

      A maioria das localidades não define esse valor. Um exemplo de
      localidade que define esse valor é o japonês. No Japão, a
      representação tradicional de datas inclui o nome da época
      correspondente ao reinado do então imperador.

      Normalmente, não deve ser necessário usar esse valor
      diretamente. Especificar o modificador "E" em suas strings de
      formato faz com que a função "time.strftime()" use essas
      informações. O formato da string retornada é especificado em
      *The Open Group Base Specifications Issue 8*, parágrafo 7.3.5.2
      LC_TIME C-Language Access.

   locale.ERA_D_T_FMT

      Obtém uma string de formato para "time.strftime()" para
      representar a data e a hora de uma forma baseada na era
      específica da localidade.

   locale.ERA_D_FMT

      Obtém uma string de formato para "time.strftime()" para
      representar uma data em uma forma baseada em era específica da
      localidade.

   locale.ERA_T_FMT

      Obtém uma string de formato para "time.strftime()" para
      representar uma hora em uma forma baseada em era específica da
      localidade.

   locale.ALT_DIGITS

      Obtém uma string consistindo de até 100 símbolos separados por
      ponto e vírgula usados para representar os valores de 0 a 99 de
      uma forma específica de localidade. Na maioria das localidades,
      esta é uma string vazia.

   A função define temporariamente a localidade "LC_CTYPE" para a
   localidade da categoria que determina o valor solicitado
   ("LC_TIME", "LC_NUMERIC", "LC_MONETARY" ou "LC_MESSAGES") se as
   localidades forem diferentes e a string resultante não for ASCII.
   Essa alteração temporária afeta outras threads.

   Alterado na versão 3.14: A função agora define temporariamente a
   localidade de "LC_CTYPE" em alguns casos.

locale.getdefaultlocale([envvars])

   Tenta determinar as configurações de localidade padrão e as retorna
   como uma tupla na forma "(language code, encoding)".

   De acordo com POSIX, um programa que não chamou "setlocale(LC_ALL,
   '')" executa usando a localidade portátil "'C'". Chamar
   "setlocale(LC_ALL, '')" permite que ele use a localidade padrão
   conforme definido pela variável "LANG". Como não queremos
   interferir com a configuração de localidade atual, emulamos o
   comportamento da maneira descrita acima.

   Para manter a compatibilidade com outras plataformas, não apenas a
   variável "LANG" é testada, mas uma lista de variáveis fornecida
   como parâmetro envvars. Será utilizado o primeiro encontrado a ser
   definido. *envvars* padroniza para o caminho de pesquisa usado no
   GNU gettext; deve sempre conter o nome da variável "'LANG'". O
   caminho de pesquisa do GNU gettext contém "'LC_ALL'", "'LC_CTYPE'",
   "'LANG'" e "'LANGUAGE'", nesta ordem.

   O código de idioma tem o mesmo formato de nome de localidade, mas
   sem codificação e modificador "@". O código de idioma e a
   codificação podem ser "None" se seus valores não puderem ser
   determinados. O locale "C" é representado como "(None, None)".

locale.getlocale(category=LC_CTYPE)

   Retorna a configuração atual para a categoria de localidade
   fornecida como uma tupla contendo o código de idioma e a
   codificação. *category* pode ser um dos valores "LC_*", exceto
   "LC_ALL". O padrão é "LC_CTYPE".

   O código de idioma tem o mesmo formato de nome de localidade, mas
   sem codificação. O código de idioma e a codificação podem ser
   "None" se seus valores não puderem ser determinados. A localidade
   "C" é representada como "(None, None)".

   Alterado na versão 3.15: Modificadores "@" não são mais removidos
   silenciosamente, mas incluídos no código do idioma.

locale.getpreferredencoding(do_setlocale=True)

   Retorna a *codificação da localidade* usada para dados de texto, de
   acordo com as preferências do usuário. As preferências do usuário
   são expressas de maneira diferente em sistemas diferentes e podem
   não estar disponíveis programaticamente em alguns sistemas,
   portanto, essa função retorna apenas uma estimativa.

   Em alguns sistemas, é necessário invocar "setlocale()" para obter
   as preferências do usuário, portanto, esta função não é segura para
   thread. Se invocar setlocale não for necessário ou desejado,
   *do_setlocale* deve ser definido como "False".

   No Android ou se o Modo UTF-8 do Python é retornado, sempre retorna
   "'utf-8'", a *codificação da localidade* e o argumento
   *do_setlocale* são ignorados.

   A pré-inicialização do Python configura a localidade LC_CTYPE. Veja
   também *tratador de erros e codificação do sistema de arquivos*.

   Alterado na versão 3.7: A função agora sempre retorna ""utf-8"" no
   Android ou se o Modo UTF-8 do Python estiver habilitado.

locale.getencoding()

   Obtém a atual *codificação da localidade*:

   * No Android e no VxWorks, retorna ""utf-8"".

   * No Unix, retorna a codificação da localidade "LC_CTYPE" atual.
     Retorna ""utf-8"" se "nl_langinfo(CODESET)" retornar uma string
     vazia: por exemplo, se a localidade LC_CTYPE atual não for
     compatível.

   * No Windows, retorna a página de código ANSI.

   A pré-inicialização do Python configura a localidade LC_CTYPE. Veja
   também *tratador de erros e codificação do sistema de arquivos*.

   Este função é semelhante a "getpreferredencoding(False)", exceto
   pelo fato de que esta função ignora o Modo UTF-8 do Python.

   Adicionado na versão 3.11.

locale.normalize(localename)

   Retorna um código de localidade normalizado para o nome de
   localidade fornecido. O código de localidade retornado é formatado
   para uso com "setlocale()". Se a normalização falhar, o nome
   original será retornado inalterado.

   Se a codificação fornecida não for conhecida, o padrão da função é
   a codificação padrão para o código da localidade, assim como
   "setlocale()".

locale.strcoll(string1, string2)

   Compara duas strings de acordo com a configuração atual
   "LC_COLLATE". Como qualquer outra função de comparação, retorna um
   valor negativo ou positivo, ou "0", dependendo se *string1* agrupa
   antes ou depois de *string2* ou é igual a ele.

locale.strxfrm(string)

   Transforma uma string em uma que pode ser usada em comparações com
   reconhecimento de localidade. Por exemplo, "strxfrm(s1) <
   strxfrm(s2)" é equivalente a "strcoll(s1, s2) < 0". Esta função
   pode ser usada quando a mesma string é comparada repetidamente, por
   exemplo, ao agrupar uma sequência de strings.

locale.format_string(format, val, grouping=False, monetary=False)

   Formata um número *val* de acordo com a configuração atual do
   "LC_NUMERIC". O formato segue as convenções do operador "%". Para
   valores de ponto flutuante, o ponto decimal é modificado, se
   apropriado. Se *grouping* for "True", também levará em conta o
   agrupamento.

   Se *monetary* for verdadeiro, a conversão usa o separador de
   milhares monetários e strings de agrupamento.

   Processa especificadores de formatação como em "format % val", mas
   leva as configurações de localidade atuais em consideração.

   Alterado na versão 3.7: O parâmetro nomeado *monetary* foi
   adicionado.

locale.currency(val, symbol=True, grouping=False, international=False)

   Formata um número *val* de acordo com as configurações atuais de
   "LC_MONETARY".

   A string retornada inclui o símbolo da moeda se *symbol* for
   verdadeiro, que é o padrão. Se *grouping* for "True" (o que não é o
   padrão), o agrupamento é feito com o valor. Se *international* for
   "True" (o que não é o padrão), o símbolo da moeda internacional
   será usado.

   Nota:

     Esta função não funcionará com a localidade 'C', então você deve
     definir uma localidade via "setlocale()" primeiro.

locale.str(float)

   Formata um número de ponto flutuante usando o mesmo formato da
   função embutida "str(float)", mas leva o ponto decimal em
   consideração.

locale.delocalize(string)

   Converte uma string em uma string numérica normalizada, seguindo as
   configurações de "LC_NUMERIC".

   Adicionado na versão 3.5.

locale.localize(string, grouping=False, monetary=False)

   Converte uma string numérica normalizada em uma string formatada,
   seguindo as configurações de "LC_NUMERIC".

   Adicionado na versão 3.10.

locale.atof(string, func=float)

   Converte uma string para um número, de acordo com o valor da
   constante "LC_NUMERIC", chamando *func* com o resultado da chamada
   à "delocalize()" em *string*.

locale.atoi(string)

   Converte uma string em um número inteiro, seguindo as convenções de
   "LC_NUMERIC".

locale.LC_CTYPE

   Categoria da localidade para as funções de tipo de caracteres. Mais
   importante ainda, essa categoria define a codificação do texto, ou
   seja, como os bytes são interpretado como pontos de código Unicode.
   Consulte **PEP 538** e **PEP 540** para saber como essa variável
   pode ser automaticamente coagida para "C.UTF-8" para evitar
   problemas criados por configurações inválidas em contêineres ou
   configurações incompatíveis passadas por conexões remotas com SSH.

   O Python não usa internamente funções de transformação de
   caracteres dependente de localidade do "ctype.h". Em vez disso,
   "pyctype.h" fornece equivalentes independentes de localidade como
   "Py_TOLOWER".

locale.LC_COLLATE

   Categoria da localidade para classificação de strings. As funções
   "strcoll()" e "strxfrm()" do módulo "locale" são afetadas.

locale.LC_TIME

   Categoria da localidade para a formatação de hora. A função
   "time.strftime()" segue essas convenções.

locale.LC_MONETARY

   Categoria da localidade para formatação de valores monetários. As
   opções disponíveis estão disponíveis na função "localeconv()".

locale.LC_MESSAGES

   Categoria da localidade para exibição de mensagens. Python
   atualmente não oferece suporte a mensagens com reconhecimento de
   localidade específicas da aplicação. Mensagens exibidas pelo
   sistema operacional, como aquelas retornadas por "os.strerror()"
   podem ser afetadas por esta categoria.

   Esse valor pode não estar disponível em sistemas operacionais que
   não estejam em conformidade com o padrão POSIX, principalmente o
   Windows.

locale.LC_NUMERIC

   Categoria da localidade para formatação de números. As funções
   "format_string()", "atoi()", "atof()" e "str()" do módulo "locale"
   são afetadas por essa categoria. Todas as outras operações de
   formatação numérica não são afetadas.

locale.LC_ALL

   Combinação de todas as configurações da localidade. Se este
   sinalizador for usado quando a localidade for alterada, a
   configuração da localidade para todas as categorias será tentada.
   Se isso falhar para qualquer categoria, nenhuma categoria é
   alterada. Quando a localidade é recuperada usando este sinalizador,
   uma string indicando a configuração para todas as categorias é
   retornada. Esta string pode ser usada posteriormente para restaurar
   as configurações.

locale.CHAR_MAX

   Esta é uma constante simbólica usada para diferentes valores
   retornados por "localeconv()".


Histórico, detalhes, dicas, dicas e advertências
================================================

O padrão C define a localidade como uma propriedade de todo o programa
que pode ser relativamente cara para alterar. Além disso, algumas
implementações são interrompidas de forma que mudanças frequentes de
localidade podem causar despejos de memória. Isso torna a localidade
um tanto dolorosa de usar corretamente.

Inicialmente, quando um programa é iniciado, a localidade é a
localidade "C", não importa qual a localidade preferida do usuário. Há
uma exceção: a categoria "LC_CTYPE" é alterada na inicialização para
definir a codificação de localidade atual para a codificação de
localidade preferida do usuário. O programa deve dizer explicitamente
que deseja as configurações de localidade preferidas do usuário para
outras categorias chamando "setlocale(LC_ALL, '')".

Geralmente é uma má ideia chamar "setlocale()" em alguma rotina de
biblioteca, já que como efeito colateral afeta todo o programa. Salvar
e restaurar é quase tão ruim: é caro e afeta outras threads que são
executadas antes de as configurações serem restauradas.

Se, ao codificar um módulo para uso geral, você precisa de uma versão
independente da localidade de uma operação que é afetada pela
localidade (como certos formatos usados com "time.strftime()"), você
terá que encontrar uma maneira de faça isso sem usar a rotina de
biblioteca padrão. Melhor ainda é se convencer de que não há problema
em usar as configurações da localidade. Apenas como último recurso,
você deve documentar que seu módulo não é compatível com configurações
de localidade não-"C".

A única maneira de realizar operações numéricas de acordo com a
localidade é usar as funções especiais definidas por este módulo:
"atof()", "atoi()", "format_string()", "str()".

Não há como realizar conversões de maiúsculas e minúsculas e
classificações de caracteres de acordo com a localidade. Para strings
de texto (Unicode), isso é feito de acordo com o valor do caractere
apenas, enquanto para strings de byte, as conversões e classificações
são feitas de acordo com o valor ASCII do byte e bytes cujo bit alto
está definido (ou seja, bytes não ASCII ) nunca são convertidos ou
considerados parte de uma classe de caracteres, como letras ou espaços
em branco.


Nomes de localidades
====================

O formato do nome de localidade depende da plataforma, e o conjunto de
locais suportados pode depender da configuração do sistema.

Em plataformas Posix, isso geralmente tem o formato [1]:

     language ["_" territory] ["." charset] ["@" modifier]

onde *language* é um código de idioma de duas ou três letras da ISO
639, *territory* é um código de país ou região de duas letras da ISO
3166, *charset* é uma codificação de localidade e *modifier* é um nome
de script, uma subtag de idioma, um identificador de ordem de
classificação ou outro modificador de localidade (por exemplo,
"latin", "valencia", "stroke" e "euro").

No Windows, vários formatos são suportados. [2] [3] Um subconjunto de
tags IETF BCP 47:

     language ["-" script] ["-" territory] ["." charset]
     language ["-" script] "-" territory "-" modifier

onde *language* e *territory* têm o mesmo significado que em Posix,
*script* é um código de script de quatro letras da ISO 15924 e
*modifier* é uma subtag de idioma, um identificador de ordem de
classificação ou modificador personalizado (por exemplo, "valencia",
"stroke" ou "x-python"). São aceitos os separadores hífen ("'-'") e
sublinhado ("'_'"). Somente a codificação UTF-8 é permitida para tags
BCP 47.

O Windows também oferece suporte a nomes de localidade no formato:

     language ["_" territory] ["." charset]

onde *language* e *territory* são nomes completos, como "English" e
"United States", e *charset* é um número de página de código (por
exemplo, "1252") ou UTF-8. Só é aceito o separador sublinhado neste
formato.

A localidade "C" é aceita em todas as plataformas.

[1] IEEE Std 1003.1-2024; 8.2 Internationalization Variables

[2] Nomes de localidade, idiomas e strings de país/região do UCRT

[3] Nomes de localidade


Para escritores de extensão e programas que incorporam Python
=============================================================

Módulos de extensão nunca devem chamar "setlocale()", exceto para
descobrir qual é a localidade atual. Mas uma vez que o valor de
retorno só pode ser usado portavelmente para restaurá-lo, isso não é
muito útil (exceto talvez para descobrir se a localidade é ou não
"C").

Quando o código Python usa o módulo "locale" para alterar a
localidade, isso também afeta a aplicação de incorporação. Se a
aplicação de incorporação não quiser que isso aconteça, ele deve
remover o módulo de extensão "_locale" (que faz todo o trabalho) da
tabela de módulos embutidos no arquivo "config.c" e certificar-se de
que o módulo "_locale" não está acessível como uma biblioteca
compartilhada.


Acesso a catálogos de mensagens
===============================

locale.gettext(msg)

locale.dgettext(domain, msg)

locale.dcgettext(domain, msg, category)

locale.textdomain(domain)

locale.bindtextdomain(domain, dir)

locale.bind_textdomain_codeset(domain, codeset)

The locale module exposes the C library's gettext interface on systems
that provide this interface.  It consists of the functions
"gettext()", "dgettext()", "dcgettext()", "textdomain()",
"bindtextdomain()", and "bind_textdomain_codeset()".  These are
similar to the same functions in the "gettext" module, but use the C
library's binary format for message catalogs, and the C library's
search algorithms for locating message catalogs.

As aplicações Python normalmente não precisam invocar essas funções e
devem usar "gettext" em seu lugar. Uma exceção conhecida a esta regra
são os aplicativos que se vinculam a bibliotecas C adicionais que
invocam internamente "gettext" ou "dcgettext". Para essas aplicações,
pode ser necessário vincular o domínio de texto, para que as
bibliotecas possam localizar adequadamente seus catálogos de
mensagens.
