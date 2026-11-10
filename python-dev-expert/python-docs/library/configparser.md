"configparser" --- Analisador sintático de arquivo de configuração
******************************************************************

**Código-fonte:** Lib/configparser.py

======================================================================

Este módulo fornece a classe "ConfigParser", que implementa uma
linguagem de configuração básica, com uma estrutura semelhante à
encontrada nos arquivos INI do Microsoft Windows. Você pode usar isso
para escrever programas em Python que podem ser facilmente
personalizados pelos usuários finais.

Nota:

  Esta biblioteca *não* interpreta nem escreve os prefixos de tipo de
  valor usados na versão estendida da sintaxe INI do Registro do
  Windows.

Aviso:

  Tenha cuidado quando estiver analisando dados de fontes não-
  confiáveis. Uma arquivo INI malicioso pode fazer o decodificador
  consumir recursos consideráveis de CPU e memória. É recomendado
  limitar o tamanho do dado a ser analisado.

Ver também:

  Módulo "tomllib"
     TOML é um formato bem especificado para arquivos de configuração
     de aplicações. Ele foi projetado especificamente para ser uma
     versão melhorada do INI.

  Módulo "shlex"
     Suporte para criação de minilinguagens semelhantes a shell Unix
     que também podem ser usadas para arquivos de configuração de
     aplicações.

  Módulo "json"
     O módulo "json" implementa um subconjunto de sintaxe JavaScript
     que às vezes é usado para configuração, mas não suporta
     comentários.


Início rápido
=============

Vamos pegar um arquivo de configuração bem básico parecido com este:

   [DEFAULT]
   ServerAliveInterval = 45
   Compression = yes
   CompressionLevel = 9
   ForwardX11 = yes

   [forge.example]
   User = hg

   [topsecret.server.example]
   Port = 50022
   ForwardX11 = no

A estrutura dos arquivos INI é descrita na seção seguinte.
Essencialmente, o arquivo consiste em seções, cada uma contendo chaves
com valores. As classes "configparser" podem ler e escrever tais
arquivos. Vamos começar criando o arquivo de configuração acima
programaticamente.

   >>> import configparser
   >>> config = configparser.ConfigParser()
   >>> config['DEFAULT'] = {'ServerAliveInterval': '45',
   ...                      'Compression': 'yes',
   ...                      'CompressionLevel': '9'}
   >>> config['forge.example'] = {}
   >>> config['forge.example']['User'] = 'hg'
   >>> config['topsecret.server.example'] = {}
   >>> topsecret = config['topsecret.server.example']
   >>> topsecret['Port'] = '50022'     # mutates the parser
   >>> topsecret['ForwardX11'] = 'no'  # same here
   >>> config['DEFAULT']['ForwardX11'] = 'yes'
   >>> with open('example.ini', 'w') as configfile:
   ...   config.write(configfile)
   ...

Como você pode ver, podemos tratar um analisador sintático de
configuração como um dicionário. Existem diferenças, descritas
posteriormente, mas o comportamento é muito próximo do que você
esperaria de um dicionário.

Agora que criamos e salvamos um arquivo de configuração, vamos lê-lo e
explorar os dados que ele contém.

   >>> config = configparser.ConfigParser()
   >>> config.sections()
   []
   >>> config.read('example.ini')
   ['example.ini']
   >>> config.sections()
   ['forge.example', 'topsecret.server.example']
   >>> 'forge.example' in config
   True
   >>> 'python.org' in config
   False
   >>> config['forge.example']['User']
   'hg'
   >>> config['DEFAULT']['Compression']
   'yes'
   >>> topsecret = config['topsecret.server.example']
   >>> topsecret['ForwardX11']
   'no'
   >>> topsecret['Port']
   '50022'
   >>> for key in config['forge.example']:
   ...     print(key)
   user
   compressionlevel
   serveraliveinterval
   compression
   forwardx11
   >>> config['forge.example']['ForwardX11']
   'yes'

Como podemos ver acima, a API é bastante simples. A única mágica
envolve a seção "DEFAULT" que fornece valores padrão para todas as
outras seções [1]. Observe também que as chaves nas seções não
diferenciam maiúsculas de minúsculas e são armazenadas em letras
minúsculas [1].

É possível ler diversas configurações para um único "ConfigParser",
onde a configuração adicionada mais recentemente terá a maior
prioridade. Para quaisquer chaves repetidas serão usados os valores da
configuração mais recente, enquanto os valores das chaves anteriores
serão ignorados. O exemplo a seguir lê um arquivo chamado
"override.ini", que irá substituir chaves repetidas do arquivo
"example.ini".

   [DEFAULT]
   ServerAliveInterval = -1

   >>> config_override = configparser.ConfigParser()
   >>> config_override['DEFAULT'] = {'ServerAliveInterval': '-1'}
   >>> with open('override.ini', 'w') as configfile:
   ...     config_override.write(configfile)
   ...
   >>> config_override = configparser.ConfigParser()
   >>> config_override.read(['example.ini', 'override.ini'])
   ['example.ini', 'override.ini']
   >>> print(config_override.get('DEFAULT', 'ServerAliveInterval'))
   -1

Este comportamento é equivalente a uma chamada "ConfigParser.read()"
com vários arquivos passados para o parâmetro *filenames*.


Tipos de dados suportados
=========================

Os analisadores sintáticos de configuração não adivinham os tipos de
dados dos valores nos arquivos de configuração, sempre os armazenando
internamente como strings. Isso significa que se você precisar de
outros tipos de dados, deverá converter por conta própria:

   >>> int(topsecret['Port'])
   50022
   >>> float(topsecret['CompressionLevel'])
   9.0

Como essa tarefa é tão comum, os analisadores sintáticos de
configuração fornecem uma variedade de métodos getter úteis para
manipular com números inteiros, pontos flutuantes e booleanos. O
último é o mais interessante porque simplesmente passar o valor para
"bool()" não adiantaria nada já que "bool('False')" ainda é "True". É
por isso que os analisadores sintáticos de configuração também
fornecem "getboolean()". Este método não diferencia maiúsculas de
minúsculas e reconhece valores booleanos de "'yes'"/"'no'",
"'on'"/"'off'", "'true'" /"'false'" e "'1'"/"'0'" [1]. Por exemplo:

   >>> topsecret.getboolean('ForwardX11')
   False
   >>> config['forge.example'].getboolean('ForwardX11')
   True
   >>> config.getboolean('forge.example', 'Compression')
   True

Além de "getboolean()", os analisadores sintáticos de configuração
também fornecem métodos "getint()" e "getfloat()" equivalentes. Você
pode registrar seus próprios conversores e personalizar os fornecidos.
[1]


Valores reservas
================

Assim como acontece com um dicionário, você pode usar o método "get()"
de uma seção para fornecer valores reservas (fallback):

   >>> topsecret.get('Port')
   '50022'
   >>> topsecret.get('CompressionLevel')
   '9'
   >>> topsecret.get('Cipher')
   >>> topsecret.get('Cipher', '3des-cbc')
   '3des-cbc'

Observe que os valores padrão têm precedência sobre os valores
substitutos. Por exemplo, em nosso exemplo a chave
"'CompressionLevel'" foi especificada apenas na seção "'DEFAULT'". Se
tentarmos obtê-lo na seção "'topsecret.server.example'", sempre
obteremos o padrão, mesmo se especificarmos um substituto:

   >>> topsecret.get('CompressionLevel', '3')
   '9'

Mais uma coisa a ter em conta é que o método "get()" no nível do
analisador fornece uma interface personalizada e mais complexa,
mantida para compatibilidade com versões anteriores. Ao usar este
método, um valor substituto pode ser fornecido através do argumento
somente-nomeado "fallback":

   >>> config.get('forge.example', 'monster',
   ...            fallback='No such things as monsters')
   'No such things as monsters'

O mesmo argumento "fallback" pode ser usado com os métodos "getint()",
"getfloat()" e "getboolean()", por exemplo:

   >>> 'BatchMode' in topsecret
   False
   >>> topsecret.getboolean('BatchMode', fallback=True)
   True
   >>> config['DEFAULT']['BatchMode'] = 'no'
   >>> topsecret.getboolean('BatchMode', fallback=True)
   False


Estrutura dos arquivos INI
==========================

Um arquivo de configuração consiste em seções, cada uma liderada por
um cabeçalho "[section]", seguido por entradas de chave/valor
separadas por uma string específica ("=" ou ":" por padrão [1]) . Por
padrão, os nomes das seções diferenciam maiúsculas de minúsculas, mas
as chaves não [1]. Os espaços em branco à esquerda e à direita são
removidos das chaves e dos valores. Os valores podem ser omitidos se o
analisador sintático estiver configurado para permitir [1], caso em
que o delimitador chave/valor também pode ser omitido. Os valores
também podem abranger várias linhas, desde que sejam indentados de
forma mais profunda que a primeira linha do valor. Dependendo do modo
do analisador sintático, as linhas em branco podem ser tratadas como
partes de valores multilinhas ou ignoradas.

Por padrão, um nome de seção válido pode ser qualquer string que não
contenha '\n'. Para alterar isso, consulte "ConfigParser.SECTCRE".

O nome da primeira seção pode ser omitido se o analisador sintático
estiver configurado para permitir uma seção de nível superior sem nome
com "allow_unnamed_section=True". Neste caso, as chaves/valores podem
ser recuperadas por "UNNAMED_SECTION" como em
"config[UNNAMED_SECTION]".

Os arquivos de configuração podem incluir comentários, prefixados por
caracteres específicos ("#" e ";" por padrão [1]). Os comentários
podem aparecer sozinhos em uma linha vazia, possivelmente indentados.
[1]

Por exemplo:

   [Valores Simples]
   chave=valor
   espaços nas chaves=permitidos
   espaços nos valores=permitidos também
   espaços em volta do delimitador = obviamente
   você também pode usar : para delimitar chaves de valores

   [Todos Valores São Strings]
   valores como este: 1000000
   ou este: 3.14159265359
   são tratados como números? : não
   inteiros, pontos flutuantes e booleanos são considerados: strings
   pode usar a API para obter valores convertidos diretamente: verdadeiro

   [Valores multilinha]
   chorus: Eu sou um lenhador e estou bem
       Durmo a noite toda e trabalho o dia inteiro

   [Sem valores]
   chave_sem_valor
   valor string vazia aqui =

   [Você pode usar comentários]
   # como este
   ; ou este

   # Por padrão, apenas em uma linha vazia.
   # Comentários em linha podem ser prejudiciais porque eles
   # impedem os usuários de usar os caracteres delimitadores
   # como partes dos valores.
   # Isto posto, isso pode ser personalizado.

       [Seções Podem Ser Indentadas]
           podem_ser_valores_também = True
           isso_significa_algo_especial = False
           propósito = formatação para legibilidade
           valores_multilinha = são
               tratados sem problemas desde
               que eles estejam indentados
               mais profundamente do que a
               primeira linha de um valor
           # Mencionamos que também podemos indentar comentários?


Seções não nomeadas
===================

O nome da primeira seção (ou único) pode ser omitido e os valores
recuperados pelo atributo "UNNAMED_SECTION".

   >>> config = """
   ... option = value
   ...
   ... [  Section 2  ]
   ... another = val
   ... """
   >>> unnamed = configparser.ConfigParser(allow_unnamed_section=True)
   >>> unnamed.read_string(config)
   >>> unnamed.get(configparser.UNNAMED_SECTION, 'option')
   'value'


Interpolação de valores
=======================

Além da funcionalidade principal, "ConfigParser" oferece suporte a
interpolação. Isso significa que os valores podem ser pré-processados
antes de retorná-los das chamadas "get()".

class configparser.BasicInterpolation

   A implementação padrão usada por "ConfigParser". Ele permite que os
   valores contenham strings de formato que se referem a outros
   valores na mesma seção ou valores na seção padrão especial [1].
   Valores padrão adicionais podem ser fornecidos na inicialização.

   Por exemplo:

      [Paths]
      home_dir: /Users
      my_dir: %(home_dir)s/lumberjack
      my_pictures: %(my_dir)s/Pictures

      [Escape]
      # use um %% para escapar o sinal de % (% é o único caractere que precisa ser escapado):
      gain: 80%%

   No exemplo acima, "ConfigParser" com *interpolation* definido como
   "BasicInterpolation()" resolveria "%(home_dir)s" para o valor de
   "home_dir" ("/Users" neste caso). "%(my_dir)s" na verdade
   resolveria para "/Users/lumberjack". Todas as interpolações são
   feitas sob demanda, portanto as chaves usadas na cadeia de
   referências não precisam ser especificadas em nenhuma ordem
   específica no arquivo de configuração.

   Com "interpolation" definido como "None", o analisador sintático
   simplesmente retornaria "%(my_dir)s/Pictures" como o valor de
   "my_pictures" e "%(home_dir)s/lumberjack" como o valor de "my_dir".

class configparser.ExtendedInterpolation

   Um manipulador alternativo para interpolação que implementa uma
   sintaxe mais avançada, usada, por exemplo, em "zc.buildout". A
   interpolação estendida usa "${section:option}" para denotar um
   valor de uma seção estrangeira. A interpolação pode abranger vários
   níveis. Por conveniência, se a parte "section:" for omitida, a
   interpolação será padronizada para a seção atual (e possivelmente
   para os valores padrão da seção especial).

   Por exemplo, a configuração especificada acima com interpolação
   básica ficaria assim com interpolação estendida:

      [Paths]
      home_dir: /Users
      my_dir: ${home_dir}/lumberjack
      my_pictures: ${my_dir}/Pictures

      [Escape]
      # use a $$ para escapar o sinal de $ ($ é o único caractere que precisa ser escapado):
      cost: $$80

   Valores de outras seções também podem ser obtidos:

      [Common]
      home_dir: /Users
      library_dir: /Library
      system_dir: /System
      macports_dir: /opt/local

      [Frameworks]
      Python: 3.2
      path: ${Common:system_dir}/Library/Frameworks/

      [Arthur]
      nickname: Two Sheds
      last_name: Jackson
      my_dir: ${Common:home_dir}/twosheds
      my_pictures: ${my_dir}/Pictures
      python_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}


Acesso através do protocolo de mapeamento
=========================================

Adicionado na versão 3.2.

Acesso através do protocolo de mapeamento é um nome genérico para
funcionalidade que permite usar objetos personalizados como se fossem
dicionários. No caso de "configparser", a implementação da interface
de mapeamento está usando a notação "parser['section']['option']".

"parser['section']" em particular retorna um intermediário para os
dados da seção no analisador sintático. Isso significa que os valores
não são copiados, mas obtidos do analisador sintático original sob
demanda. O que é ainda mais importante é que quando os valores são
alterados em um intermediário de seção, eles são, na verdade,
modificados no analisador sintático original.

Os objetos "configparser" se comportam o mais próximo possível dos
dicionários reais. A interface de mapeamento é completa e segue a ABC
"MutableMapping". No entanto, existem algumas diferenças que devem ser
levadas em consideração:

* Por padrão, todas as chaves nas seções são acessíveis sem distinção
  entre maiúsculas e minúsculas [1]. Por exemplo. "for option in
  parser["section"]" produz apenas nomes de chaves de opção
  "optionxform"ada. Isso significa chaves em letras minúsculas por
  padrão. Ao mesmo tempo, para uma seção que contém a chave "'a'",
  ambas as expressões retornam "True":

     "a" in parser["section"]
     "A" in parser["section"]

* Todas as seções também incluem valores "DEFAULTSECT", o que
  significa que ".clear()" em uma seção não pode deixá-la visivelmente
  vazia. Isso ocorre porque os valores padrão não podem ser excluídos
  da seção (porque tecnicamente eles não estão lá). Se eles forem
  substituídos na seção, a exclusão fará com que o valor padrão fique
  visível novamente. Tentar excluir um valor padrão causa um
  "KeyError".

* "DEFAULTSECT" não pode ser removido do analisador sintático:

  * tentar excluí-lo levanta "ValueError",

  * "parser.clear()" deixa-o intacto,

  * "parser.popitem()" nunca o retorna.

* "parser.get(section, option, **kwargs)" - o segundo argumento
  **não** é um valor substituto. Observe, entretanto, que os métodos
  "get()" em nível de seção são compatíveis tanto com o protocolo de
  mapeamento quanto com a API clássica do configparser.

* "parser.items()" é compatível com o protocolo de mapeamento (retorna
  uma lista de pares *section_name*, *section_proxy* incluindo o
  DEFAULTSECT). Entretanto, este método também pode ser invocado com
  argumentos: "parser.items(section, raw, vars)". A última chamada
  retorna uma lista de pares *option*, *value* para uma "section"
  especificada, com todas as interpolações expandidas (a menos que
  "raw=True" seja fornecido).

O protocolo de mapeamento é implementado sobre a API legada existente
para que as subclasses que substituem a interface original ainda
tenham mapeamentos funcionando conforme o esperado.


Personalizando o comportamento do analisador sintático
======================================================

Existem quase tantas variantes de formato INI quanto aplicações que o
utilizam. "configparser" percorre um longo caminho para fornecer
suporte para o maior conjunto sensato de estilos INI disponíveis. A
funcionalidade padrão é determinada principalmente pelo histórico e é
muito provável que você queira personalizar alguns dos recursos.

A maneira mais comum de alterar a forma como um analisador sintático
de configuração específico funciona é usar as opções "__init__()":

* *defaults*, valor padrão: "None"

  Esta opção aceita um dicionário de pares chave-valor que será
  inicialmente colocado na seção "DEFAULT". Isso é uma maneira
  elegante de oferecer suporte a arquivos de configuração concisos que
  não especificam valores iguais ao padrão documentado.

  Dica: se você deseja especificar valores padrão para uma seção
  específica, use "read_dict()" antes de ler o arquivo real.

* *dict_type*, valor padrão: "dict"

  Esta opção tem um grande impacto no comportamento do protocolo de
  mapeamento e na aparência dos arquivos de configuração gravados. Com
  o dicionário padrão, cada seção é armazenada na ordem em que foram
  adicionadas ao analisador sintático. O mesmo vale para opções dentro
  das seções.

  Um tipo de dicionário alternativo pode ser usado, por exemplo, para
  ordenar as seções e opções ao fazer *write-back*.

  Observação: existem maneiras de adicionar um conjunto de pares de
  valores-chave em uma única operação. Quando você usa um dicionário
  regular nessas operações, a classificação das chaves será ordenada.
  Por exemplo:

     >>> parser = configparser.ConfigParser()
     >>> parser.read_dict({'seção1': {'chave1': 'valor1',
     ...                                'chave2': 'valor2',
     ...                                'chave3': 'valor3'},
     ...                   'seção2': {'chaveA': 'valorA',
     ...                                'chaveB': 'valorB',
     ...                                'chaveC': 'valorC'},
     ...                   'seção3': {'foo': 'x',
     ...                                'bar': 'y',
     ...                                'baz': 'z'}
     ... })
     >>> parser.sections()
     ['seção1', 'seção2', 'seção3']
     >>> [option for option in parser['seção3']]
     ['foo', 'bar', 'baz']

* *allow_no_value*, valor padrão: "False"

  Alguns arquivos de configuração são conhecidos por incluir
  configurações sem valores, mas que de outra forma estão em
  conformidade com a sintaxe suportada por "configparser". O parâmetro
  *allow_no_value* para o construtor pode ser usado para indicar que
  tais valores devem ser aceitos:

     >>> import configparser

     >>> sample_config = """
     ... [mysqld]
     ...   user = mysql
     ...   pid-file = /var/run/mysqld/mysqld.pid
     ...   skip-external-locking
     ...   old_passwords = 1
     ...   skip-bdb
     ...   # não precisamos de ACID hoje
     ...   skip-innodb
     ... """
     >>> config = configparser.ConfigParser(allow_no_value=True)
     >>> config.read_string(sample_config)

     >>> # Configurações com valores são tratados como antes:
     >>> config["mysqld"]["user"]
     'mysql'

     >>> # Configurações sem valores fornecem None:
     >>> config["mysqld"]["skip-bdb"]

     >>> # Configurações que não são especificadas ainda levantam um erro:
     >>> config["mysqld"]["não-existe"]
     Traceback (most recent call last):
       ...
     KeyError: 'não-existe'

* *delimiters*, valor padrão: "('=', ':')"

  Delimitadores são substrings que delimitam chaves de valores dentro
  de uma seção. A primeira ocorrência de uma substring delimitadora em
  uma linha é considerada um delimitador. Isso significa que os
  valores (mas não as chaves) podem conter os delimitadores.

  Veja também o argumento *space_around_delimiters* para
  "ConfigParser.write()".

* *comment_prefixes*, valor padrão: "('#', ';')"

* *inline_comment_prefixes*, valor padrão: "None"

  Prefixos de comentários são strings que indicam o início de um
  comentário válido em um arquivo de configuração. *comment_prefixes*
  são usados apenas em linhas vazias (opcionalmente indentadas),
  enquanto *inline_comment_prefixes* pode ser usado após cada valor
  válido (por exemplo, nomes de seções, opções e linhas vazias
  também). Por padrão, os comentários embutidos estão desabilitados e
  "'#'" e "';'" são usados como prefixos para comentários de linha
  inteira.

  Alterado na versão 3.2: Nas versões anteriores do "configparser", o
  comportamento correspondia a "comment_prefixes=('#',';')" e
  "inline_comment_prefixes=(';',)".

  Observe que os analisadores sintáticos de configuração não oferecem
  suporte a escape de prefixos de comentários, portanto, usar
  *inline_comment_prefixes* pode impedir que os usuários especifiquem
  valores de opção com caracteres usados como prefixos de comentários.
  Em caso de dúvida, evite definir *inline_comment_prefixes*. Em
  qualquer circunstância, a única maneira de armazenar caracteres de
  prefixo de comentário no início de uma linha em valores multilinha é
  interpolar o prefixo, por exemplo:

     >>> from configparser import ConfigParser, ExtendedInterpolation
     >>> parser = ConfigParser(interpolation=ExtendedInterpolation())
     >>> # the default BasicInterpolation could be used as well
     >>> parser.read_string("""
     ... [DEFAULT]
     ... hash = #
     ...
     ... [hashes]
     ... shebang =
     ...   ${hash}!/usr/bin/env python
     ...   ${hash} -*- coding: utf-8 -*-
     ...
     ... extensions =
     ...   enabled_extension
     ...   another_extension
     ...   #disabled_by_comment
     ...   yet_another_extension
     ...
     ... interpolation not necessary = if # is not at line start
     ... even in multiline values = line #1
     ...   line #2
     ...   line #3
     ... """)
     >>> print(parser['hashes']['shebang'])

     #!/usr/bin/env python
     # -*- coding: utf-8 -*-
     >>> print(parser['hashes']['extensions'])

     enabled_extension
     another_extension
     yet_another_extension
     >>> print(parser['hashes']['interpolation not necessary'])
     if # is not at line start
     >>> print(parser['hashes']['even in multiline values'])
     line #1
     line #2
     line #3

* *strict*, valor padrão: "True"

  Ao definir como "True", o analisador sintático não permitirá nenhuma
  seção ou opção duplicada durante a leitura de uma única fonte
  (usando "read_file()", "read_string()" ou "read_dict()"). Recomenda-
  se usar analisadores sintáticos estritos em novas aplicações.

  Alterado na versão 3.2: Nas versões anteriores do "configparser", o
  comportamento correspondia a "strict=False".

* *empty_lines_in_values*, valor padrão: "True"

  Em analisadores sintáticos de configuração, os valores podem
  abranger várias linhas, desde que sejam mais indentados do que a
  chave que os contém. Por padrão, os analisadores sintáticos também
  permitem que linhas vazias façam parte de valores. Ao mesmo tempo,
  as chaves podem ser indentados arbitrariamente para melhorar a
  legibilidade. Consequentemente, quando os arquivos de configuração
  ficam grandes e complexos, é fácil para o usuário perder o controle
  da estrutura do arquivo. Tomemos por exemplo:

     [Seção]
     chave = multilinha
       valor com uma pegadinha

      esta = ainda é parte do valor multilinha de 'chave'

  Isso pode ser especialmente problemático para o usuário ver se está
  usando uma fonte proporcional para editar o arquivo. É por isso que
  quando sua aplicação não precisa de valores com linhas vazias, você
  deve considerar proibi-los. Isso fará com que as linhas vazias
  dividam as chaves sempre. No exemplo acima, seriam produzidas duas
  chaves, "key" e "this".

* *default_section*, valor padrão: "configparser.DEFAULTSECT" (isto é:
  ""DEFAULT"")

  A convenção de permitir uma seção especial de valores padrão para
  outras seções ou fins de interpolação é um conceito poderoso desta
  biblioteca, permitindo aos usuários criar configurações declarativas
  complexas. Esta seção normalmente é chamada de ""DEFAULT"", mas pode
  ser personalizada para apontar para qualquer outro nome de seção
  válido. Alguns valores típicos incluem: ""general"" ou ""common"". O
  nome fornecido é usado para reconhecer seções padrão ao ler de
  qualquer fonte e é usado ao gravar a configuração em um arquivo. Seu
  valor atual pode ser recuperado usando o atributo
  "parser_instance.default_section" e pode ser modificado em tempo de
  execução (ou seja, para converter arquivos de um formato para
  outro).

* *interpolation*, valor padrão: "configparser.BasicInterpolation"

  O comportamento de interpolação pode ser personalizado fornecendo um
  manipulador personalizado por meio do argumento *interpolation*.
  "None" pode ser usado para desligar completamente a interpolação,
  "ExtendedInterpolation()" fornece uma variante mais avançada
  inspirada em "zc.buildout". Mais sobre o assunto na seção de
  documentação dedicada. "RawConfigParser" tem um valor padrão de
  "None".

* *converters*, valor padrão: não definido

  Os analisadores sintáticos de configuração fornecem getters de valor
  de opção que realizam conversão de tipo. Por padrão, "getint()",
  "getfloat()" e "getboolean()" são implementados. Caso outros getters
  sejam desejáveis, os usuários podem defini-los em uma subclasse ou
  passar um dicionário onde cada chave é um nome do conversor e cada
  valor é um chamável que implementa a referida conversão. Por
  exemplo, passar "{'decimal': decimal.Decimal}" adicionaria
  "getdecimal()" no objeto analisador sintático e em todos os proxies
  de seção. Em outras palavras, será possível escrever
  "parser_instance.getdecimal('section', 'key', fallback=0)" e
  "parser_instance['section'].getdecimal('key', 0)".

  Se o conversor precisar acessar o estado do analisador sintático,
  ele poderá ser implementado como um método em uma subclasse do
  analisador sintático de configuração. Se o nome deste método começar
  com "get", ele estará disponível em todos os intermediários de
  seção, na forma compatível com dict (veja o exemplo "getdecimal()"
  acima).

Uma personalização mais avançada pode ser obtida substituindo os
valores padrão desses atributos do analisador sintático. Os padrões
são definidos nas classes, portanto podem ser substituídos por
subclasses ou por atribuição de atributos.

ConfigParser.BOOLEAN_STATES

   Por padrão, ao usar "getboolean()", os analisadores sintáticos de
   configuração consideram os seguintes valores "True": "'1'",
   "'yes'", "'true'", "'on'" e os seguintes valores "False": "'0'",
   "'no'", "'false'", "'off'". Você pode substituir isso especificando
   um dicionário personalizado de strings e seus resultados booleanos.
   Por exemplo:

      >>> custom = configparser.ConfigParser()
      >>> custom['seção1'] = {'funky': 'nope'}
      >>> custom['seção1'].getboolean('funky')
      Traceback (most recent call last):
      ...
      ValueError: Not a boolean: nope
      >>> custom.BOOLEAN_STATES = {'sure': True, 'nope': False}
      >>> custom['seção1'].getboolean('funky')
      False

   Outros pares booleanos típicos incluem "accept"/"reject" ou
   "enabled"/"disabled".

ConfigParser.optionxform(option)

   Este método transforma nomes de opções em cada operação de leitura,
   obtenção ou definição. O padrão converte o nome em letras
   minúsculas. Isso também significa que quando um arquivo de
   configuração for gravado, todas as chaves estarão em letras
   minúsculas. Substitua esse método se for inadequado. Por exemplo:

      >>> config = """
      ... [Seção1]
      ... Chave = Valor
      ...
      ... [Seção2]
      ... OutraChave = Valor
      ... """
      >>> typical = configparser.ConfigParser()
      >>> typical.read_string(config)
      >>> list(typical['Seção1'].keys())
      ['chave']
      >>> list(typical['Seção2'].keys())
      ['outrachave']
      >>> custom = configparser.RawConfigParser()
      >>> custom.optionxform = lambda option: option
      >>> custom.read_string(config)
      >>> list(custom['Seção1'].keys())
      ['Chave']
      >>> list(custom['Seção2'].keys())
      ['OutraChave']

   Nota:

     A função optionxform transforma nomes de opções em um formato
     canônico. Esta deve ser uma função idempotente: se o nome já
     estiver na forma canônica, deverá ser retornado inalterado.

ConfigParser.SECTCRE

   Uma expressão regular compilada usada para analisar cabeçalhos de
   seção. O padrão corresponde a "[section]" para o nome ""section"".
   O espaço em branco é considerado parte do nome da seção, portanto
   "[  larch  ]" será lido como uma seção de nome ""  larch  "".
   Substitua esse atributo se for inadequado. Por exemplo:

      >>> import re
      >>> config = """
      ... [Seção 1]
      ... opção = valor
      ...
      ... [  Seção 2  ]
      ... outro = valor
      ... """
      >>> typical = configparser.ConfigParser()
      >>> typical.read_string(config)
      >>> typical.sections()
      ['Seção 1', '  Seção 2  ']
      >>> custom = configparser.ConfigParser()
      >>> custom.SECTCRE = re.compile(r"\[ *(?P<header>[^]]+?) *\]")
      >>> custom.read_string(config)
      >>> custom.sections()
      ['Seção 1', 'Seção 2']

   Nota:

     Embora os objetos ConfigParser também usem um atributo "OPTCRE"
     para reconhecer linhas de opção, não é recomendado substituí-lo
     porque isso interferiria nas opções do construtor
     *allow_no_value* e *delimiters*.


Exemplos de APIs legadas
========================

Principalmente por questões de retrocompatibilidade, "configparser"
fornece também uma API legada com métodos "get"/"set" explícitos.
Embora existam casos de uso válidos para os métodos descritos abaixo,
o acesso ao protocolo de mapeamento é preferido para novos projetos. A
API legada é às vezes mais avançada, de baixo nível e totalmente
contraintuitiva.

Um exemplo de escrita em um arquivo de configuração:

   import configparser

   config = configparser.RawConfigParser()

   # Observe que usando as funções set do RawConfigParser, você pode atribuir
   # valores não string a chaves internamente, mas receberá um erro ao tentar
   # gravar em um arquivo ou quando obtê-lo em modo não bruta. Definir valores
   # usando o protocolo de mapeamento ou set() do ConfigParser não permite que
   # tais atribuições ocorram.
   config.add_section('Seção1')
   config.set('Seção1', 'an_int', '15')
   config.set('Seção1', 'a_bool', 'true')
   config.set('Seção1', 'a_float', '3.1415')
   config.set('Seção1', 'baz', 'divertido')
   config.set('Seção1', 'bar', 'Python')
   config.set('Seção1', 'foo', '%(bar)s é %(baz)s!')

   # Escrevendo nosso arquivo de configuração em 'example.cfg'
   with open('example.cfg', 'w') as configfile:
       config.write(configfile)

Um exemplo de leitura do arquivo de configuração novamente:

   import configparser

   config = configparser.RawConfigParser()
   config.read('example.cfg')

   # getfloat() levanta uma exceção se o valor não for um ponto flutuante
   # getint() e getboolean() também fazem isso para seus respectivos tipos
   a_float = config.getfloat('Seção1', 'a_float')
   an_int = config.getint('Seção1', 'an_int')
   print(a_float + an_int)

   # Note que a próxima saída não interpola '%(bar)s' ou '%(baz)s'.
   # Isso ocorre porque estamos usando RawConfigParser().
   if config.getboolean('Seção1', 'a_bool'):
       print(config.get('Seção1', 'foo'))

Para obter interpolação, use "ConfigParser":

   import configparser

   cfg = configparser.ConfigParser()
   cfg.read('example.cfg')

   # Defina o argumento *raw* opcional de get() para True se você quiser desabilitar
   # interpolação em uma única operação de get.
   print(cfg.get('Seção1', 'foo', raw=False))  # -> "Python é divertido!"
   print(cfg.get('Seção1', 'foo', raw=True))   # -> "%(bar)s é %(baz)s!"

   # O argumento opcional *vars* é um dicionário com membros que vão aceitar
   # precedência na interpolação.
   print(cfg.get('Seção1', 'foo', vars={'bar': 'Documentação',
                                          'baz': 'maligna'}))

   # The optional *fallback* argument can be used to provide a fallback value
   print(cfg.get('Seção1', 'foo'))
         # -> "Python é divertido!"

   print(cfg.get('Seção1', 'foo', fallback='Monty não é.'))
         # -> "Python é divertido!"

   print(cfg.get('Seção1', 'monstro', fallback='Não existem monstros.'))
         # -> "Não existem monstros."

   # Um print(cfg.get('Seção1', 'monster')) levantaria NoOptionError,
   # mas nós também podemos usar:

   print(cfg.get('Seção1', 'mosntro', fallback=None))
         # -> None

Os valores padrão estão disponíveis em ambos os tipos de
ConfigParsers. Eles são usados em interpolação se uma opção usada não
estiver definida em outro lugar.

   import configparser

   # Nova instância com 'bar' e 'baz' padrão para 'A vida' e 'difícil' cada
   config = configparser.ConfigParser({'bar': 'A vida', 'baz': 'difícil'})
   config.read('example.cfg')

   print(config.get('Seção1', 'foo'))     # -> "Python é divertido!"
   config.remove_option('Seção1', 'bar')
   config.remove_option('Seção1', 'baz')
   print(config.get('Seção1', 'foo'))     # -> "A vida é difícil!"


Objetos ConfigParser
====================

class configparser.ConfigParser(defaults=None, dict_type=dict, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section=configparser.DEFAULTSECT, interpolation=BasicInterpolation(), converters={}, allow_unnamed_section=False)

   O principal analisador sintático de configuração. Quando *defaults*
   é fornecido, ele é inicializado no dicionário de padrões
   intrínsecos. Quando *dict_type* for fornecido, ele será usado para
   criar os objetos dicionário para a lista de seções, para as opções
   dentro de uma seção e para os valores padrão.

   Quando *delimiters* são fornecidos, eles são usados como o conjunto
   de substrings que dividem chaves de valores. Quando
   *comment_prefixes* for fornecido, ele será usado como o conjunto de
   substrings que prefixam comentários em linhas vazias. Os
   comentários podem ser indentados. Quando *inline_comment_prefixes*
   for fornecido, ele será usado como o conjunto de substrings que
   prefixam comentários em linhas não vazias.

   Quando *strict* for "True" (o padrão), o analisador sintático não
   permitirá nenhuma seção ou opção duplicada durante a leitura de uma
   única fonte (arquivo, string ou dicionário), levantando
   "DuplicateSectionError" ou "DuplicateOptionError". Quando
   *empty_lines_in_values* é "False" (padrão: "True"), cada linha
   vazia marca o fim de uma opção. Caso contrário, as linhas vazias
   internas de uma opção multilinha serão mantidas como parte do
   valor. Quando *allow_no_value* for "True" (padrão: "False"), opções
   sem valores serão aceitas; o valor mantido para estes é "None" e
   eles são serializados sem o delimitador final.

   Quando *default_section* é fornecido, ele especifica o nome da
   seção especial que contém valores padrão para outras seções e
   propósitos de interpolação (normalmente chamada de ""DEFAULT"").
   Este valor pode ser recuperado e alterado em tempo de execução
   usando o atributo de instância "default_section". Isso não
   reavaliará um arquivo de configuração já analisado, mas será usado
   ao escrever configurações analisadas em um novo arquivo de
   configuração.

   O comportamento de interpolação pode ser personalizado fornecendo
   um manipulador personalizado por meio do argumento *interpolation*.
   "None" pode ser usado para desligar completamente a interpolação,
   "ExtendedInterpolation()" fornece uma variante mais avançada
   inspirada em "zc.buildout". Mais sobre o assunto na seção de
   documentação dedicada.

   Todos os nomes de opções usados na interpolação serão passados
   através do método "optionxform()" assim como qualquer outra
   referência de nome de opção. Por exemplo, usando a implementação
   padrão de "optionxform()" (que converte nomes de opções para letras
   minúsculas), os valores "foo %(bar)s" e "foo %(BAR)s" são
   equivalentes.

   Quando *converters* é fornecido, deve ser um dicionário onde cada
   chave representa o nome de um conversor de tipo e cada valor é um
   chamável implementando a conversão de string para o tipo de dados
   desejado. Cada conversor obtém seu próprio método "get*()"
   correspondente no objeto analisador sintático e nos intermediários
   de seção.

   Quando *allow_unnamed_section* é "True" (padrão: "False"), o
   primeiro nome da seção pode ser omitido. Veja a seção "Seções não
   nomeadas".

   É possível ler diversas configurações para um único "ConfigParser",
   onde a configuração adicionada mais recentemente terá a maior
   prioridade. Para quaisquer chaves repetidas serão usados os valores
   da configuração mais recente, enquanto os valores das chaves
   anteriores serão ignorados. O exemplo a seguir lê um arquivo
   chamado "override.ini", que irá substituir chaves repetidas do
   arquivo "example.ini".

      [DEFAULT]
      ServerAliveInterval = -1

      >>> config_override = configparser.ConfigParser()
      >>> config_override['DEFAULT'] = {'ServerAliveInterval': '-1'}
      >>> with open('override.ini', 'w') as configfile:
      ...     config_override.write(configfile)
      ...
      >>> config_override = configparser.ConfigParser()
      >>> config_override.read(['example.ini', 'override.ini'])
      ['example.ini', 'override.ini']
      >>> print(config_override.get('DEFAULT', 'ServerAliveInterval'))
      -1

   Alterado na versão 3.1: O padrão *dict_type* é
   "collections.OrderedDict".

   Alterado na versão 3.2: *allow_no_value*, *delimiters*,
   *comment_prefixes*, *strict*, *empty_lines_in_values*,
   *default_section* e *interpolation* foram adicionados.

   Alterado na versão 3.5: O argumento *converters* foi adicionado.

   Alterado na versão 3.7: O argumento *defaults* é lido com
   "read_dict()", fornecendo um comportamento consistente em todo o
   analisador: chaves e valores que não são de string são convertidos
   implicitamente em strings.

   Alterado na versão 3.8: O *dict_type* padrão é "dict", pois agora
   preserva a ordem de inserção.

   Alterado na versão 3.13: Levanta "MultilineContinuationError"
   quando *allow_no_value* for "True", e uma chave sem valor continua
   com uma linha indentada.

   Alterado na versão 3.13: O argumento *allow_unnamed_section* foi
   adicionado.

   defaults()

      Retorna um dicionário contendo os padrões de toda a instância.

   sections()

      Retorna uma lista das seções disponíveis; a *seção padrão* não
      está incluída na lista.

   add_section(section)

      Adiciona uma seção de nome *section* à instância. Se já existir
      uma seção com o nome fornecido, "DuplicateSectionError" será
      levantada. Se o nome da *seção padrão* for passado, "ValueError"
      será levantada. O nome da seção deve ser uma string; caso
      contrário, "TypeError" será levantada.

      Alterado na versão 3.2: Nomes de seções sem string levantam
      "TypeError".

   has_section(section)

      Indica se a *section* nomeada está presente na configuração. A
      *seção padrão* não é reconhecida.

   options(section)

      Retorna uma lista de opções disponíveis na *section*
      especificada.

   has_option(section, option)

      Se a *section* fornecida existir e contiver a *option*
      fornecida, retorna "True"; caso contrário, retorna "False". Se a
      *section* especificada for "None" ou uma string vazia, DEFAULT
      será presumido.

   read(filenames, encoding=None)

      Tenta ler e analisar um iterável de nomes de arquivos,
      retornando uma lista de nomes de arquivos que foram analisados
      com sucesso.

      Se *filenames* for uma string, um objeto "bytes" ou um *objeto
      caminho ou similar*, este parâmetro será tratado como um único
      nome de arquivo. Se um arquivo nomeado em *filenames* não puder
      ser aberto, esse arquivo será ignorado. Isso foi projetado para
      que você possa especificar um iterável de possíveis locais de
      arquivo de configuração (por exemplo, o diretório atual, o
      diretório inicial do usuário e algum diretório de todo o
      sistema) e todos os arquivos de configuração existentes no
      iterável serão lidos.

      Se nenhum dos arquivos nomeados existir, a instância
      "ConfigParser" conterá um conjunto de dados vazio. Uma aplicação
      que requer que valores iniciais sejam carregados de um arquivo
      deve carregar o arquivo ou arquivos necessários usando
      "read_file()" antes de chamar "read()" para quaisquer arquivos
      opcionais:

         import configparser, os

         config = configparser.ConfigParser()
         config.read_file(open('defaults.cfg'))
         config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')],
                     encoding='cp1250')

      Alterado na versão 3.2: Adicionado o parâmetro *encoding*.
      Anteriormente, todos os arquivos eram lidos usando a codificação
      padrão para "open()".

      Alterado na versão 3.6.1: O parâmetro *filenames* aceita um
      *objeto caminho ou similar*.

      Alterado na versão 3.7: O parâmetro *filenames* aceita um objeto
      "bytes".

   read_file(f, source=None)

      Lê e analisa dados de configuração de *f* que devem ser
      iteráveis, produzindo strings Unicode (por exemplo, arquivos
      abertos em modo texto).

      O argumento opcional *source* especifica o nome do arquivo que
      está sendo lido. Se não for fornecido e *f* tiver um atributo
      "name", que é usado para *source*; o padrão é "'<???>'".

      Adicionado na versão 3.2: Substitui "readfp()".

   read_string(string, source='<string>')

      Analisa dados de configuração de uma string.

      O argumento opcional *source* especifica um nome específico do
      contexto da string passada. Se não for fornecido, "'<string>'"
      será usado. Geralmente deve ser um caminho do sistema de
      arquivos ou uma URL.

      Adicionado na versão 3.2.

   read_dict(dictionary, source='<dict>')

      Carrega a configuração de qualquer objeto que forneça um método
      "items()" dict ou similar. Chaves são nomes de seções, valores
      são dicionários com chaves e valores que devem estar presentes
      na seção. Se o tipo de dicionário usado preservar a ordem, as
      seções e suas chaves serão adicionadas em ordem. Os valores são
      convertidos automaticamente em strings.

      O argumento opcional *source* especifica um nome específico do
      contexto do dicionário passado. Se não for fornecido, "<dict>"
      será usado.

      Este método pode ser usado para copiar o estado entre
      analisadores sintáticos.

      Adicionado na versão 3.2.

   get(section, option, *, raw=False, vars=None[, fallback])

      Obtém um valor de *option* para a *section* nomeada. Se *vars*
      for fornecido, deverá ser um dicionário. A *option* é pesquisada
      em *vars* (se fornecido), *section* e em *DEFAULTSECT* nesta
      ordem. Se a chave não for encontrada e *fallback* for fornecido,
      ele será usado como um valor alternativo. "None" pode ser
      fornecido como um valor *fallback*.

      Todas as interpolações "'%'" são expandidas nos valores de
      retorno, a menos que o argumento *raw* seja verdadeiro. Os
      valores das chaves de interpolação são consultados da mesma
      maneira que a opção.

      Alterado na versão 3.2: Os argumentos *raw*, *vars* e *fallback*
      são palavras somente-nomeadas para proteger os usuários de
      tentarem usar o terceiro argumento como substituto *fallback*
      (especialmente ao usar o protocolo de mapeamento).

   getint(section, option, *, raw=False, vars=None[, fallback])

      Um método de conveniência que força a *option* na *section*
      especificada ser um número inteiro. Veja "get()" para explicação
      de *raw*, *vars* e *fallback*.

   getfloat(section, option, *, raw=False, vars=None[, fallback])

      Um método de conveniência que força a *option* na *section*
      especificada ser um número de ponto flutuante. Veja "get()" para
      explicação de *raw*, *vars* e *fallback*.

   getboolean(section, option, *, raw=False, vars=None[, fallback])

      Um método de conveniência que força a *option* na *section*
      especificada a um valor booleano. Observe que os valores aceitos
      para a opção são "'1'", "'yes'", "'true'", e "'on'", o que fazem
      com que este método retorne "True", e "'0'", "'no'", "'false'",
      e "'off'", o que fazem com que ele retorne "False". Esses
      valores de string são verificados sem distinção entre maiúsculas
      e minúsculas. Qualquer outro valor fará com que ele levante
      "ValueError". Veja "get()" para explicação de *raw*, *vars* e
      *fallback*.

   items(raw=False, vars=None)
   items(section, raw=False, vars=None)

      Quando *section* não é fornecido, retorna uma lista de pares
      *section_name*, *section_proxy*, incluindo DEFAULTSECT.

      Caso contrário, retorna uma lista de pares *name*, *value* para
      as opções na *section* fornecida. Argumentos opcionais têm o
      mesmo significado do método "get()".

      Alterado na versão 3.8: Os itens presentes em *vars* não
      aparecem mais no resultado. O comportamento anterior misturava
      opções reais do analisador sintático com variáveis fornecidas
      para interpolação.

   set(section, option, value)

      Se a seção fornecida existir, defina a opção fornecida com o
      valor especificado; caso contrário, levanta "NoSectionError".
      *option* e *value* devem ser strings; caso contrário,
      "TypeError" será levantada.

   write(fileobject, space_around_delimiters=True)

      Escreve uma representação da configuração no *objeto arquivo*
      especificado, que deve ser aberto em modo texto (aceitando
      strings). Esta representação pode ser analisada por uma futura
      chamada "read()". Se *space_around_delimiters* for verdadeiro,
      os delimitadores entre chaves e valores serão envoltos por
      espaços.

      Alterado na versão 3.14: Levanta InvalidWriteError se isso for
      gravar uma representação que não pode ser analisada com precisão
      por uma futura chamada "read()" deste analisador sintático.

   Nota:

     Os comentários no arquivo de configuração original não são
     preservados ao escrever a configuração. O que é considerado um
     comentário depende dos valores fornecidos para *comment_prefix* e
     *inline_comment_prefix*.

   remove_option(section, option)

      Remove a *option* especificada da *section* especificada. Se a
      seção não existir, levanta "NoSectionError". Se existisse a
      opção de ser removida, retorna "True"; caso contrário, retorna
      "False".

   remove_section(section)

      Remove a *section* especificada da configuração. Se a seção de
      fato existiu, retorna "True". Caso contrário, retorna "False".

   optionxform(option)

      Transforma o nome da opção *option* conforme encontrado em um
      arquivo de entrada ou conforme passado pelo código do cliente no
      formato que deve ser usado nas estruturas internas. A
      implementação padrão retorna uma versão em minúsculas de
      *option*; subclasses podem substituir isso ou o código do
      cliente pode definir um atributo com esse nome nas instâncias
      para afetar esse comportamento.

      Você não precisa criar uma subclasse do analisador sintático
      para usar esse método; você também pode configurá-lo em uma
      instância, para uma função que recebe um argumento de string e
      retorna uma string. Definir como "str", por exemplo, faria com
      que sejam diferenciadas as letras maiúsculas das minúsculas nos
      nomes das opções:

         cfgparser = ConfigParser()
         cfgparser.optionxform = str

      Observe que ao ler arquivos de configuração, os espaços em
      branco ao redor dos nomes das opções são removidos antes de
      "optionxform()" ser chamado.

configparser.UNNAMED_SECTION

   Um objeto especial que representa um nome de seção usado para
   referenciar a seção sem nome (veja Seções não nomeadas).

configparser.MAX_INTERPOLATION_DEPTH

   A profundidade máxima para interpolação recursiva para "get()"
   quando o parâmetro *raw* é falso. Isso é relevante apenas quando a
   *interpolation* padrão é usada.


Objetos RawConfigParser
=======================

class configparser.RawConfigParser(defaults=None, dict_type=dict, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section=configparser.DEFAULTSECT, interpolation=BasicInterpolation(), converters={}, allow_unnamed_section=False)

   Variante legada do "ConfigParser". Ela tem a interpolação
   desabilitada por padrão e permite nomes de seções não-string, nomes
   de opções e valores através de seus métodos inseguros "add_section"
   e "set", bem como o tratamento de argumentos nomeados legados
   "defaults=" .

   Alterado na versão 3.2: *allow_no_value*, *delimiters*,
   *comment_prefixes*, *strict*, *empty_lines_in_values*,
   *default_section* e *interpolation* foram adicionados.

   Alterado na versão 3.5: O argumento *converters* foi adicionado.

   Alterado na versão 3.8: O *dict_type* padrão é "dict", pois agora
   preserva a ordem de inserção.

   Alterado na versão 3.13: O argumento *allow_unnamed_section* foi
   adicionado.

   Nota:

     Considere usar "ConfigParser", que verifica os tipos de valores a
     serem armazenados internamente. Se você não quiser interpolação,
     você pode usar "ConfigParser(interpolation=None)".

   add_section(section)

      Adiciona uma seção chamada *section* ou "UNNAMED_SECTION" à
      instância.

      Se a seção com o nome fornecido já existir,
      "DuplicateSectionError" é levantada. Se o nome da *seção padrão*
      for passado, "ValueError" é levantada. Se "UNNAMED_SECTION" for
      passado e o suporte for desabilitado
      "UnnamedSectionDisabledError" é levantada.

      O tipo da *section* não está marcado, o que permite aos usuários
      criar seções nomeadas sem string. Este comportamento não é
      compatível e pode causar erros internos.

   Alterado na versão 3.14: Adicionado suporte a "UNNAMED_SECTION".

   set(section, option, value)

      Se a seção fornecida existir, defina a opção fornecida com o
      valor especificado; caso contrário, levanta "NoSectionError".
      Embora seja possível usar "RawConfigParser" (ou "ConfigParser"
      com parâmetros *raw* definidos como verdadeiro) para
      armazenamento *interno* de valores não-string, funcionalidade
      completa (incluindo interpolação e saída para arquivos) só pode
      ser alcançado usando valores de string.

      Este método permite que os usuários atribuam valores não-string
      às chaves internamente. Este comportamento não é suportado e
      causará erros ao tentar escrever em um arquivo ou obtê-lo no
      modo não bruto. **Use a API do protocolo de mapeamento** que não
      permite que tais atribuições ocorram.


Exceções
========

exception configparser.Error

   Classe base para todas as outras exceções do "configparser".

exception configparser.NoSectionError

   Exceção levantada quando uma seção especificada não é encontrada.

exception configparser.DuplicateSectionError

   Exceção levantada se "add_section()" for chamado com o nome de uma
   seção que já está presente ou em analisadores sintáticos estritos
   quando uma seção for encontrada mais de uma vez em um único arquivo
   de entrada, string ou dicionário.

   Alterado na versão 3.2: Adicionados os atributos e parâmetros
   opcionais *source* e *lineno* a "__init__()".

exception configparser.DuplicateOptionError

   Exceção levantada por analisadores sintáticos estritos se uma única
   opção aparecer duas vezes durante a leitura de um único arquivo,
   string ou dicionário. Isso detecta erros ortográficos e erros
   relacionados a diferenciação de letras maiúsculas e minúsculas
   como, p. ex., um dicionário pode ter duas chaves representando a
   mesma chave de configuração que não diferencia maiúsculas de
   minúsculas.

exception configparser.NoOptionError

   Exceção levantada quando uma opção especificada não é encontrada na
   seção especificada.

exception configparser.InterpolationError

   Classe base para exceções levantadas quando ocorrem problemas ao
   executar a interpolação de strings.

exception configparser.InterpolationDepthError

   Exceção levantada quando a interpolação de string não pode ser
   concluída porque o número de iterações excede
   "MAX_INTERPOLATION_DEPTH". Subclasse de "InterpolationError".

exception configparser.InterpolationMissingOptionError

   Exceção levantada quando uma opção referenciada a partir de um
   valor não existe. Subclasse de "InterpolationError".

exception configparser.InterpolationSyntaxError

   Exceção levantada quando o texto fonte no qual são feitas as
   substituições não está em conformidade com a sintaxe exigida.
   Subclasse de "InterpolationError".

exception configparser.MissingSectionHeaderError

   Exceção levantada ao tentar analisar um arquivo que não possui
   cabeçalhos de seção.

exception configparser.ParsingError

   Exceção levantada quando ocorrem erros ao tentar analisar um
   arquivo.

   Alterado na versão 3.12: O atributo "filename" e o argumento do
   construtor "__init__()" foram removidos. Eles estiveram disponíveis
   usando o nome "source" desde 3.2.

exception configparser.MultilineContinuationError

   Exceção levantada quando uma chave sem valor correspondente
   continua com uma linha indentada.

   Adicionado na versão 3.13.

exception configparser.UnnamedSectionDisabledError

   Exceção levantada ao tentar usar "UNNAMED_SECTION" sem habilitá-lo.

      Adicionado na versão 3.14.

exception configparser.InvalidWriteError

   Exceção levantada quando uma tentativa de "ConfigParser.write()"
   não seria analisada com precisão em uma futura chamada de
   "ConfigParser.read()".

   Ex: escrever uma chave que comece com o padrão
   "ConfigParser.SECTCRE" seria interpretado como um cabeçalho de
   seção ao ser lido. Tentar escrever isso levantará esta exceção.

   Adicionado na versão 3.14.

-[ Notas de rodapé ]-

[1] Os analisadores sintáticos de configuração permitem muitas
    personalizações. Caso você tenha interesse em alterar o
    comportamento descrito na referência da nota de rodapé, consulte a
    seção Personalizando o comportamento do analisador sintático.
