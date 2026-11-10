"argparse" --- Analisador sintático para opções de linha de comando, argumentos e subcomandos
*********************************************************************************************

Adicionado na versão 3.2.

**Código-fonte:** Lib/argparse.py

Nota:

  Embora o "argparse" seja o módulo de biblioteca padrão recomendado
  para implementar aplicações de linha de comando básicas, autores com
  requisitos mais rigorosos sobre como exatamente suas aplicações de
  linha de comando se comportam podem descobrir que ele não fornece o
  nível de controle necessário. Consulte Escolhendo uma biblioteca de
  análise de linha de comando para alternativas a considerar quando
  "argparse" não oferece suporte a comportamentos que a aplicação
  requer (como desabilitar completamente o suporte a opções
  intercaladas e argumentos posicionais, ou aceitar valores de
  parâmetros de opção que começam com "-" mesmo quando correspondem a
  outra opção definida).

======================================================================


Tutorial
^^^^^^^^

Esta página contém informações da API de Referência. Para uma
introdução mais prática para o parser de linha de comando Python,
acesse o tutorial do argparse.

O módulo "argparse" torna fácil a escrita de interfaces de linha de
comando amigáveis. O programa define quais argumentos são necessários
e "argparse" descobrirá como analisá-lo e interpretá-los a partir do
"sys.argv". O módulo "argparse" também gera automaticamente o texto
ajuda e mensagens de uso. O módulo também vai emitir erros quando o
usuário prover argumentos inválidos para o programa.

O suporte do módulo "argparse" para interfaces de linha de comando é
construído em torno de uma instância de "argparse.ArgumentParser". É
um contêiner para especificações de argumentos e possui opções que se
aplicam ao analisador sintático como um todo:

   parser = argparse.ArgumentParser(
                       prog='NomePrograma',
                       description='O que o programa faz',
                       epilog='Texto na parte inferior da memsagem de ajuda')

O método "ArgumentParser.add_argument()" anexa especificações de
argumentos individuais ao analisador. Ele oferece suporte a argumentos
posicionais, opções que aceitam valores e sinalizadores de
ligar/desligar:

   parser.add_argument('filename')           # argumento posicional
   parser.add_argument('-c', '--count')      # a opção recebe um valor
   parser.add_argument('-v', '--verbose',
                       action='store_true')  # sinalizador de ligar/desligar

O método "ArgumentParser.parse_args()" executa o analisador e coloca
os dados extraídos em um objeto "argparse.Namespace":

   args = parser.parse_args()
   print(args.filename, args.count, args.verbose)

Nota:

  Se você estiver procurando um guia sobre como atualizar um código
  "optparse" para "argparse", veja Atualizando código optparse.


Objetos ArgumentParser
======================

class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True, *, suggest_on_error=True, color=True)

   Cria um novo objeto "ArgumentParser". Todos os parâmetros devem ser
   passados como argumentos nomeados. Cada parâmetro tem sua própria
   descrição mais detalhada abaixo, mas em resumo eles são:

   * prog - O nome do programa (padrão: gerado a partir de atributos
     de módulo "__main__" e de "sys.argv[0]")

   * usage - A string que descreve o uso do programa (padrão: gerado a
     partir de argumentos adicionados ao analisador sintático)

   * description - Texto para exibir antes da ajuda dos argumentos
     (por padrão, nenhum texto)

   * epilog - Texto para exibir após da ajuda dos argumentos (por
     padrão, nenhum texto)

   * parents - Uma lista de objetos "ArgumentParser" cujos argumentos
     também devem ser incluídos

   * formatter_class - Uma classe para personalizar a saída de ajuda

   * prefix_chars - O conjunto de caracteres que prefixam argumentos
     opcionais (padrão: "-")

   * fromfile_prefix_chars - O conjunto de caracteres que prefixam os
     arquivos dos quais os argumentos adicionais devem ser lidos
     (padrão: "None")

   * argument_default - O valor padrão global para argumentos (padrão:
     "None")

   * conflict_handler - A estratégia para resolver opcionais
     conflitantes (geralmente desnecessário)

   * add_help - Adiciona uma opção "-h/--help" para o analisador
     sintático (padrão: "True")

   * allow_abbrev - Permite que opções longas sejam abreviadas se a
     abreviação não for ambígua. (padrão: "True")

   * exit_on_error - Determina se "ArgumentParser" sai ou não com
     informações de erro quando ocorre um erro. (padrão: "True")

   * suggest_on_error - Habilita sugestões para escolhas de argumentos
     e nomes de subanalisadores digitados incorretamente (padrão:
     "True")

   * color - Permite saída colorida (padrão: "True")

   Alterado na versão 3.5: O parâmetro *allow_abbrev* foi adicionado.

   Alterado na versão 3.8: Em versões anteriores, *allow_abbrev*
   também desabilitava o agrupamento de sinalizadores curtos, como
   "-vv" para significar "-v -v".

   Alterado na versão 3.9: O parâmetro *exit_on_error* foi adicionado.

   Alterado na versão 3.14: Os parâmetros *suggest_on_error* e *color*
   foram adicionados.

   Alterado na versão 3.15: *suggest_on_error* teve seu padrão
   alterado para "True".

As seções a seguir descrevem como cada um deles é usado.


"prog"
------

Por padrão, "ArgumentParser" calcula o nome do programa a ser exibido
nas mensagens de ajuda dependendo da maneira como o interpretador
Python foi executado:

* O "nome base" de "sys.argv[0]" se um arquivo foi passado como
  argumento.

* O nome do interpretador Python seguido por "sys.argv[0]" se um
  diretório ou um arquivo zip foi passado como argumento.

* O nome do interpretador Python seguido por "-m" seguido pelo nome do
  módulo ou pacote se a opção "-m" foi usada.

Este padrão é quase sempre desejável porque fará com que as mensagens
de ajuda correspondam à string que foi usada para invocar o programa
na linha de comando. No entanto, para alterar esse comportamento
padrão, outro valor pode ser fornecido usando o argumento "prog=" para
"ArgumentParser":

   >>> parser = argparse.ArgumentParser(prog='meuprograma')
   >>> parser.print_help()
   usage: meuprograma [-h]

   options:
    -h, --help  show this help message and exit

Observe que o nome do programa, seja determinado a partir de
"sys.argv[0]", a partir de atributos de módulo "__main__" ou do
argumento "prog=", está disponível para mensagens de ajuda usando o
especificador de formato "%(prog)s".

   >>> parser = argparse.ArgumentParser(prog='meuprograma')>>> parser.add_argument('--foo', help='foo do programa %(prog)s')>>> parser.print_help()usage: meuprograma [-h] [--foo FOO]options: -h, --help  show this help message and exit --foo FOO   foo do programa meuprograma

Alterado na versão 3.14: O valor padrão "prog" agora reflete como
"__main__" foi realmente executado, em vez de ser sempre
"os.path.basename(sys.argv[0])".


"usage"
-------

Por padrão, "ArgumentParser" calcula a mensagem de uso a partir dos
argumentos que contém. A mensagem padrão pode ser substituída pelo
argumento nomeado "usage=":

   >>> parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
   >>> parser.add_argument('--foo', nargs='?', help='foo help')
   >>> parser.add_argument('bar', nargs='+', help='bar help')
   >>> parser.print_help()
   usage: PROG [options]

   positional arguments:
    bar          bar help

   options:
    -h, --help   show this help message and exit
    --foo [FOO]  foo help

O especificador de formato "%(prog)s" está disponível para preencher o
nome do programa em suas mensagens de uso.

Quando uma mensagem de uso personalizada é especificada para o
analisador sintático principal, você também pode considerar passar o
argumento "prog" para "add_subparsers()" ou os argumentos "prog" e
"usage" para "add_parser()", para garantir prefixos de comando e
informações de uso consistentes entre os subanalisadores.


"description"
-------------

A maioria das chamadas para o construtor "ArgumentParser" usará o
argumento nomeado  "description=". Este argumento fornece uma breve
descrição do que o programa faz e como funciona. Nas mensagens de
ajuda, a descrição é exibida entre a string de uso da linha de comando
e as mensagens de ajuda para os vários argumentos.

Por padrão, a descrição terá sua linha quebrada para que se encaixe no
espaço fornecido. Para alterar esse comportamento, consulte o
argumento formatter_class.


"epilog"
--------

Alguns programas gostam de exibir uma descrição adicional do programa
após a descrição dos argumentos. Esse texto pode ser especificado
usando o argumento "epilog=" para "ArgumentParser":

   >>> parser = argparse.ArgumentParser(
   ...     description='Um foo que faz bars',
   ...     epilog="E é assim que você faria foo de bar")
   >>> parser.print_help()
   usage: argparse.py [-h]

   Um foo que faz bars

   options:
    -h, --help  show this help message and exit

   E é assim que você faria foo de bar

Tal como acontece com o argumento description, o texto de "epilog="
tem sua quebra de linha habilitada por padrão, mas este comportamento
pode ser ajustado com o argumento formatter_class para
"ArgumentParser".


"parents"
---------

Às vezes, vários analisadores sintáticos compartilham um conjunto
comum de argumentos. Ao invés de repetir as definições desses
argumentos, um único analisador com todos os argumentos compartilhados
e passado para o argumento "parents=" para "ArgumentParser" pode ser
usado. O argumento "parents=" pega uma lista de objetos
"ArgumentParser", coleta todas as ações posicionais e opcionais deles,
e adiciona essas ações ao objeto "ArgumentParser" sendo construído:

   >>> parent_parser = argparse.ArgumentParser(add_help=False)>>> parent_parser.add_argument('--parent', type=int)>>> foo_parser = argparse.ArgumentParser(parents=[parent_parser])>>> foo_parser.add_argument('foo')>>> foo_parser.parse_args(['--parent', '2', 'XXX'])Namespace(foo='XXX', parent=2)>>> bar_parser = argparse.ArgumentParser(parents=[parent_parser])>>> bar_parser.add_argument('--bar')>>> bar_parser.parse_args(['--bar', 'YYY'])Namespace(bar='YYY', parent=None)

Observe que a maioria dos analisadores sintáticos pais especificará
"add_help=False". Caso contrário, o "ArgumentParser" verá duas opções
"-h/--help" (uma no pai e outra no filho) e levantará um erro.

Nota:

  Você deve inicializar totalmente os analisadores sintáticos antes de
  passá-los via "parents=". Se você alterar os analisadores pais após
  o analisador filho, essas mudanças não serão refletidas no filho.


"formatter_class"
-----------------

Objetos "ArgumentParser" permitem que a  formação do texto de ajuda
seja personalizada por meio da especificação de uma classe de
formatação alternativa. Atualmente, há quatro dessas classes:

class argparse.RawDescriptionHelpFormatter
class argparse.RawTextHelpFormatter
class argparse.ArgumentDefaultsHelpFormatter
class argparse.MetavarTypeHelpFormatter

"RawDescriptionHelpFormatter" e "RawTextHelpFormatter" dão mais
controle sobre como as descrições textuais são exibidas. Por padrão,
objetos "ArgumentParser" quebram em linha os textos description e
epilog nas mensagens de ajuda da linha de comando:

   >>> parser = argparse.ArgumentParser(
   ...     prog='PROG',
   ...     description='''esta descrição
   ...         foi indentada de forma estranha,
   ...             mas está tudo bem''',
   ...     epilog='''
   ...             da mesma forma para este epílogo, cujos espaços vão
   ...         ser apagados e cujas palavras serão quebradas
   ...         em algumas linhas''')
   >>> parser.print_help()
   usage: PROG [-h]

   esta descrição foi indentada de forma estranha, mas está tudo bem

   options:
    -h, --help  show this help message and exit

   da mesma forma para este epílogo, cujos espaços vão ser apagados e
   cujas palavras serão quebradas em algumas linhas

Passar "RawDescriptionHelpFormatter" como "formatter_class=" indica
que description e epilog já estão formatados corretamente e não devem
ter suas linhas quebradas:

   >>> parser = argparse.ArgumentParser(
   ...     prog='PROG',
   ...     formatter_class=argparse.RawDescriptionHelpFormatter,
   ...     description=textwrap.dedent('''\
   ...         Por favor, não bagunce este texto!
   ...         --------------------------------
   ...             Eu indentei o texto
   ...             exatamente na forma
   ...             que quero que fique
   ...         '''))
   >>> parser.print_help()
   usage: PROG [-h]

   Por favor, não bagunce este texto!
   --------------------------------
      Eu indentei o texto
      exatamente na forma
      que quero que fique

   options:
    -h, --help  show this help message and exit

"RawTextHelpFormatter" mantém espaços em branco para todos os tipos de
texto de ajuda, incluindo descrições de argumentos. No entanto, várias
novas linhas são substituídas por uma. Se você deseja preservar várias
linhas em branco, adicione espaços entre as novas linhas.

"ArgumentDefaultsHelpFormatter" adiciona automaticamente informações
sobre os valores padrão para cada uma das mensagens de ajuda do
argumento:

   >>> parser = argparse.ArgumentParser(
   ...     prog='PROG',
   ...     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
   >>> parser.add_argument('--foo', type=int, default=42, help='FOO!')
   >>> parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
   >>> parser.print_help()
   usage: PROG [-h] [--foo FOO] [bar ...]

   positional arguments:
    bar         BAR! (default: [1, 2, 3])

   options:
    -h, --help  show this help message and exit
    --foo FOO   FOO! (default: 42)

"MetavarTypeHelpFormatter" usa o nome de argumento type para cada
argumento como o nome de exibição para seus valores (em vez de usar o
dest como o formatador regular faz):

   >>> parser = argparse.ArgumentParser(
   ...     prog='PROG',
   ...     formatter_class=argparse.MetavarTypeHelpFormatter)
   >>> parser.add_argument('--foo', type=int)
   >>> parser.add_argument('bar', type=float)
   >>> parser.print_help()
   usage: PROG [-h] [--foo int] float

   positional arguments:
     float

   options:
     -h, --help  show this help message and exit
     --foo int


"prefix_chars"
--------------

A maioria das opções de linha de comando usará "-" como prefixo, por
exemplo, "-f/--foo". Analisadores sintáticos que precisam ter suporte
a caracteres de prefixo diferentes ou adicionais, por exemplo, para
opções como "+f" ou "/foo", podem especificá-las usando o argumento
"prefix_chars=" para o construtor "ArgumentParser":

   >>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
   >>> parser.add_argument('+f')
   >>> parser.add_argument('++bar')
   >>> parser.parse_args('+f X ++bar Y'.split())
   Namespace(bar='Y', f='X')

O argumento "prefix_chars=" é padronizado como "'-'". Fornecer um
conjunto de caracteres que não inclua "-" fará com que as opções
"-f/--foo" não sejam permitidas.


"fromfile_prefix_chars"
-----------------------

Às vezes ao lidar com uma lista de argumentos particularmente longa,
pode fazer sentido manter a lista de argumentos em um arquivo em vez
de digitá-la na linha de comando. Se o argumento
"fromfile_prefix_chars=" for dado ao construtor "ArgumentParser",
então os argumentos que começam com qualquer um dos caracteres
especificados serão tratados como arquivos e serão substituídos pelos
argumentos que eles contêm. Por exemplo:

   >>> with open('args.txt', 'w', encoding=sys.getfilesystemencoding()) as fp:
   ...     fp.write('-f\nbar')
   ...
   >>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
   >>> parser.add_argument('-f')
   >>> parser.parse_args(['-f', 'foo', '@args.txt'])
   Namespace(f='bar')

Por padrão, os argumentos lidos de um arquivo devem ser um por linha
(mas veja também "convert_arg_line_to_args()") e são tratados como se
estivessem no mesmo lugar que o argumento original que faz referência
ao arquivo na linha de comando. Portanto, no exemplo acima, a
expressão "['-f', 'foo', '@args.txt']" é considerada equivalente à
expressão "['-f', 'foo', '-f', 'bar']".

Nota:

  Cada linha é tratada como um único argumento; portanto, uma linha
  vazia é lida como uma string vazia ("''").

"ArgumentParser" usa *tratador de erros e codificação do sistema de
arquivos* para ler o arquivo que contém argumentos.

O argumento "fromfile_prefix_chars=" é padronizado como "None",
significando que os argumentos nunca serão tratados como referências
de arquivo.

Alterado na versão 3.12: "ArgumentParser" alterou a codificação e os
erros para ler arquivos de argumentos do padrão (por exemplo,
"locale.getpreferredencoding(False)" e ""strict"") para *tratador de
erros e codificação do sistema de arquivos*. O arquivo de argumentos
deve ser codificado em UTF-8 em vez de página de código ANSI no
Windows.


"argument_default"
------------------

Geralmente, os padrões dos argumentos são especificados passando um
padrão para "add_argument()" ou chamando os métodos "set_defaults()"
com um conjunto específico de pares nome-valor. Às vezes, no entanto,
pode ser útil especificar um único padrão para argumentos, válido em
todo o analisador. Isso pode ser feito passando o argumento nomeado
"argument_default=" para "ArgumentParser". Por exemplo, para suprimir
globalmente a criação de atributos em chamadas "parse_args()",
fornecemos "argument_default=SUPPRESS":

   >>> parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
   >>> parser.add_argument('--foo')
   >>> parser.add_argument('bar', nargs='?')
   >>> parser.parse_args(['--foo', '1', 'BAR'])
   Namespace(bar='BAR', foo='1')
   >>> parser.parse_args([])
   Namespace()


"allow_abbrev"
--------------

Normalmente, quando você passa uma lista de argumentos para o método
"parse_args()" de um "ArgumentParser", ele reconhece as abreviações de
opções longas.

Este recurso pode ser desabilitado configurando "allow_abbrev" para
"False":

   >>> parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
   >>> parser.add_argument('--foobar', action='store_true')
   >>> parser.add_argument('--foonley', action='store_false')
   >>> parser.parse_args(['--foon'])
   usage: PROG [-h] [--foobar] [--foonley]
   PROG: error: unrecognized arguments: --foon

Adicionado na versão 3.5.


"conflict_handler"
------------------

Objetos "ArgumentParser" não permitem duas ações com a mesma string de
opções. Por padrão, objetos "ArgumentParser" levantam uma exceção se
for feita uma tentativa de criar um argumento com uma string de opção
que já esteja em uso:

   >>> parser = argparse.ArgumentParser(prog='PROG')>>> parser.add_argument('-f', '--foo', help='ajuda antiga de foo')>>> parser.add_argument('--foo', help='nova ajuda de foo')Traceback (most recent call last): ..ArgumentError: argument --foo: conflicting option string(s): --foo

Às vezes (por exemplo, ao usar os parents) pode ser útil simplesmente
substituir quaisquer argumentos mais antigos com a mesma string de
opções. Para obter este comportamento, o valor "'resolve'" pode ser
fornecido ao argumento "conflict_handler=" de "ArgumentParser":

   >>> parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')>>> parser.add_argument('-f', '--foo', help='ajuda antiga de foo')>>> parser.add_argument('--foo', help='nova ajuda de foo')>>> parser.print_help()usage: PROG [-h] [-f FOO] [--foo FOO]options: -h, --help  show this help message and exit -f FOO      ajuda antiga de foo --foo FOO   nova ajuda de foo

Observe que os objetos "ArgumentParser" só removem uma ação se todas
as suas strings de opção forem substituídas. Assim, no exemplo acima,
a antiga ação "-f/--foo" é mantida como "-f", pois apenas a string de
opção "--foo" foi substituída.


"add_help"
----------

Por padrão, os objetos "ArgumentParser" adicionam uma opção que
simplesmente exibe a mensagem de ajuda do analisador sintático. Se
"-h" ou "--help" for fornecido na linha de comando, a ajuda do
"ArgumentParser" será exibida.

Às vezes, pode ser útil desabilitar o acréscimo desta opção de ajuda.
Isto pode ser feito passando "False" como o argumento "add_help=" para
a classe "ArgumentParser":

   >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
   >>> parser.add_argument('--foo', help='ajuda de foo')
   >>> parser.print_help()
   usage: PROG [--foo FOO]

   options:
    --foo FOO  ajuda de foo

A opção de ajuda é normalmente "-h/--help". A exceção a isso é se o
"prefix_chars=" for especificado e não incluir "-", neste caso "-h" e
"--help" não são opções válidas. Neste caso, o primeiro caractere em
"prefix_chars" é usado para prefixar as opções de ajuda:

   >>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='+/')
   >>> parser.print_help()
   usage: PROG [+h]

   options:
     +h, ++help  show this help message and exit


"exit_on_error"
---------------

Normalmente, quando você passa uma lista de argumentos inválidos para
o método "parse_args()" de uma instância de "ArgumentParser", ele vai
exibir uma *message* para "sys.stderr" e vai sair com o código de
status de 2.

Se o usuário quiser detectar erros manualmente, o recurso pode ser
habilitado configurando "exit_on_error" para "False":

   >>> parser = argparse.ArgumentParser(exit_on_error=False)
   >>> parser.add_argument('--integers', type=int)
   _StoreAction(option_strings=['--integers'], dest='integers', nargs=None, const=None, default=None, type=<class 'int'>, choices=None, help=None, metavar=None)
   >>> try:
   ...     parser.parse_args('--integers a'.split())
   ... except argparse.ArgumentError:
   ...     print('Capturando um argumentError')
   ...
   Capturando um argumentError

Adicionado na versão 3.9.


"suggest_on_error"
------------------

Por padrão, quando um usuário fornece uma opção de argumento inválida
ou um nome de subparser inválido, a "ArgumentParser" encerra a
execução exibindo informações de erro e sugestões para argumentos
digitados incorretamente. A mensagem de erro listará as opções de
argumento permitidas (se especificadas) ou os nomes de subparsers,
juntamente com uma sugestão do tipo "talvez você quisesse dizer" caso
seja encontrada uma correspondência próxima. Observe que isso se
aplica apenas a argumentos cujas opções especificadas sejam strings:

   >>> parser = argparse.ArgumentParser(suggest_on_error=True)
   >>> parser.add_argument('--action', choices=['debug', 'dryrun'])
   >>> parser.parse_args(['--action', 'debugg'])
   usage: tester.py [-h] [--action {debug,dryrun}]
   tester.py: error: argument --action: invalid choice: 'debugg', maybe you meant 'debug'? (choose from debug, dryrun)

Você pode desativar as sugestões definindo "suggest_on_error" como
"False".

Adicionado na versão 3.14.

Alterado na versão 3.15: O valor padrão de "suggest_on_error" foi
alterado de "False" para "True".


"color"
-------

Por padrão, a mensagem de ajuda é impressa em cores usando sequências
de escape ANSI. Se desejar mensagens de ajuda em texto simples, você
pode desabilitar esta no seu ambiente local ou no próprio analisador
de argumentos, definindo "color" como "False":

   >>> parser = argparse.ArgumentParser(description='Process some integers.',
   ...                                  color=False)
   >>> parser.add_argument('--action', choices=['sum', 'max'])
   >>> parser.add_argument('integers', metavar='N', type=int, nargs='+',
   ...                     help='an integer for the accumulator')
   >>> parser.parse_args(['--help'])

Note que, quando "color=True", a saída colorida depende tanto das
variáveis de ambiente quanto das capacidades do terminal. No entanto,
se "color=False", a saída colorida é sempre desativada, mesmo que
variáveis de ambiente como "FORCE_COLOR" estejam definidas.

Adicionado na versão 3.14.

Para destacar código em linha na sua descrição, no epílogo ou no texto
de "help" de um argumento, você pode usar crases simples ou duplas:

   >>> parser = argparse.ArgumentParser(
   ...     formatter_class=argparse.RawDescriptionHelpFormatter,
   ...     description='Execute ``python -m myapp`` para iniciar.',
   ...     epilog='''Exemplos:
   ...   `python -m myapp --verbose`
   ...   ``python -m myapp --config settings.json``
   ... ''')
   >>> parser.add_argument('--foo', help='define o valor de `foo`')

Quando as cores estão ativadas, o texto entre crases é exibido em uma
cor distinta para destacar os exemplos. Quando as cores estão
desativadas, as crases são preservadas como estão, o que permite a
leitura em texto simples.

Adicionado na versão 3.15.


O método add_argument()
=======================

ArgumentParser.add_argument(name or flags..., *[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest][, deprecated])

   Define como um único argumento de linha de comando deve ser
   analisado. Cada parâmetro tem sua própria descrição mais detalhada
   abaixo, mas resumidamente são eles:

   * name ou flags - Um nome ou uma lista de strings de opções, por
     exemplo. "'foo'" ou "'-f', '--foo'".

   * action - O tipo básico de ação a ser executada quando esse
     argumento é encontrado na linha de comando.

   * nargs - O número de argumentos de linha de comando que devem ser
     consumidos.

   * const - Um valor constante exigido por algumas seleções action e
     nargs.

   * default - O valor produzido se o argumento estiver ausente da
     linha de comando e se estiver ausente do objeto espaço de nomes.

   * type - O tipo para o qual o argumento de linha de comando deve
     ser convertido.

   * choices - Uma sequência de valores permitidos para o argumento.

   * required - Se a opção de linha de comando pode ser omitida ou não
     (somente opcionais).

   * help - Uma breve descrição do que o argumento faz.

   * metavar - Um nome para o argumento nas mensagens de uso.

   * dest - O nome do atributo a ser adicionado ao objeto retornado
     por "parse_args()".

   * deprecated - Se o uso do argumento foi descontinuado ou não.

   O método retorna um objeto "Action" que representa o argumento.

As seções a seguir descrevem como cada um deles é usado.


"name" ou "flags"
-----------------

O método "add_argument()" deve saber se um argumento opcional, como
"-f" ou "--foo", ou um argumento posicional, como uma lista de nomes
de arquivos, é esperado. Os primeiros argumentos passados para
"add_argument()" devem, portanto, ser uma série de sinalizadores ou um
único nome de argumento.

Por exemplo, um argumento opcional poderia ser criado como:

   >>> parser.add_argument('-f', '--foo')

enquanto um argumento posicional pode ser criado como:

   >>> parser.add_argument('bar')

Quando "parse_args()" é chamado, argumentos opcionais serão
identificados pelo prefixo "-", e os argumentos restantes serão
considerados posicionais:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-f', '--foo')
   >>> parser.add_argument('bar')
   >>> parser.parse_args(['BAR'])
   Namespace(bar='BAR', foo=None)
   >>> parser.parse_args(['BAR', '--foo', 'FOO'])
   Namespace(bar='BAR', foo='FOO')
   >>> parser.parse_args(['--foo', 'FOO'])
   usage: PROG [-h] [-f FOO] bar
   PROG: error: the following arguments are required: bar

Por padrão, "argparse" lida automaticamente com a nomenclatura interna
e os nomes de exibição dos argumentos, simplificando o processo sem
exigir configuração adicional. Dessa forma, você não precisa
especificar os parâmetros dest e metavar. Para argumentos opcionais, o
parâmetro dest assume por padrão o nome do argumento com sublinhados
"_" substituindo os hífens "-". O parâmetro metavar assume por padrão
o nome em letras maiúsculas. Por exemplo:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('--foo-bar')
   >>> parser.parse_args(['--foo-bar', 'FOO-BAR'])
   Namespace(foo_bar='FOO-BAR')
   >>> parser.print_help()
   usage:  [-h] [--foo-bar FOO-BAR]

   optional arguments:
    -h, --help  show this help message and exit
    --foo-bar FOO-BAR


"action"
--------

Objetos "ArgumentParser" associam argumentos de linha de comando com
ações. Essas ações podem fazer praticamente qualquer coisa com os
argumentos de linha de comando associados a elas, embora a maioria das
ações simplesmente adicione um atributo ao objeto retornado por
"parse_args()". O argumento nomeado "action" especifica como os
argumentos da linha de comando devem ser tratados. As ações fornecidas
são:

* "'store'" - Isso apenas armazena o valor do argumento. Esta é a ação
  padrão.

* "'store_const'" - Isso armazena o valor especificado pelo argumento
  nomeado const; observe que o argumento nomeado const tem como padrão
  "None". A ação "'store_const'" é mais comumente usada com argumentos
  opcionais que especificam algum tipo de sinalizador. Por exemplo:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', action='store_const', const=42)
     >>> parser.parse_args(['--foo'])
     Namespace(foo=42)

* "'store_true'" e "'store_false'" - Estes são casos especiais de
  "'store_const'" que armazenam respectivamente os valores "True" e
  "False" e com valores padrão de "False" e "True":

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', action='store_true')
     >>> parser.add_argument('--bar', action='store_false')
     >>> parser.add_argument('--baz', action='store_false')
     >>> parser.parse_args('--foo --bar'.split())
     Namespace(foo=True, bar=False, baz=True)

  Esses padrões se aplicam quando as opções estão ausentes. Eles podem
  ser substituídos por default ou argument_default.

* "'append'" - Isso anexa cada valor de argumento a uma lista. É útil
  permitir para permitir que uma opção seja especificada várias vezes.
  Se o valor padrão for uma lista não-vazia, o valor analisado vai
  iniciar com os elementos padrão da lista e quaisquer valores da
  linha de comando serão anexados após os valores padrão. Exemplo de
  uso:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', action='append', default=['0'])
     >>> parser.parse_args('--foo 1 --foo 2'.split())
     Namespace(foo=['0', '1', '2'])

* "'append_const'" - Isso anexa o valor especificado pelo argumento
  nomeado const a uma lista; observe que o argumento nomeado const tem
  como padrão "None". A ação "'append_const'" é normalmente útil
  quando vários argumentos precisam armazenar constantes na mesma
  lista. Por exemplo:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--str', dest='types', action='append_const', const=str)
     >>> parser.add_argument('--int', dest='types', action='append_const', const=int)
     >>> parser.parse_args('--str --int'.split())
     Namespace(types=[<class 'str'>, <class 'int'>])

* "'extend'" - Isso anexa cada item de um argumento multivalorado a
  uma lista. A ação "'extend'" é normalmente usada com o valor do
  argumento nomeado nargs "'+'" ou "'*'". Observe que quando nargs é
  "None" (o padrão) ou "'?'", cada caractere da string do argumento
  será anexado à lista. Exemplo de uso:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument("--foo", action="extend", nargs="+", type=str)
     >>> parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"])
     Namespace(foo=['f1', 'f2', 'f3', 'f4'])

  Adicionado na versão 3.8.

* "'count'" - Isso conta o número de vezes que um argumento ocorre.
  Por exemplo, isso é útil para aumentar os níveis de verbosidade:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--verbose', '-v', action='count', default=0)
     >>> parser.parse_args(['-vvv'])
     Namespace(verbose=3)

  A menos que seja definido explicitamente, o valor padrão será
  "None". Se o valor padrão for um número diferente de zero, a
  contagem começa a partir desse número, em vez de zero.

* "'help'" - Isso imprime uma mensagem de ajuda completa para todas as
  opções no analisador sintático atual e sai. Por padrão, uma ação de
  ajuda é adicionada automaticamente ao analisador sintático. Veja
  "ArgumentParser" para detalhes de como a saída é criada.

* "'version'" - Isso espera um argumento nomeado "version=" na chamada
  "add_argument()" e imprime informações de versão e sai quando
  invocado:

     >>> import argparse
     >>> parser = argparse.ArgumentParser(prog='PROG')
     >>> parser.add_argument('--version', action='version', version='%(prog)s 2.0')
     >>> parser.parse_args(['--version'])
     PROG 2.0

Você também pode especificar uma ação arbitrária passando uma
subclasse "Action" (por exemplo, "BooleanOptionalAction") ou outro
objeto que implemente a mesma interface. Somente ações que consomem
argumentos de linha de comando (por exemplo, "'store'", "'append'",
"'extend'" ou ações personalizadas com "nargs" diferentes de zero)
podem ser usadas com argumentos posicionais.

A maneira recomendada de criar uma ação personalizada é estender
"Action", substituindo o método "__call__()" e opcionalmente os
métodos "__init__()" e "format_usage()". Você também pode registrar
ações personalizadas usando o método "register()" e referenciá-las
pelo nome registrado.

Um exemplo de uma ação personalizada:

   >>> class FooAction(argparse.Action):
   ...     def __init__(self, option_strings, dest, nargs=None, **kwargs):
   ...         if nargs is not None:
   ...             raise ValueError("nargs not allowed")
   ...         super().__init__(option_strings, dest, **kwargs)
   ...     def __call__(self, parser, namespace, values, option_string=None):
   ...         print('%r %r %r' % (namespace, values, option_string))
   ...         setattr(namespace, self.dest, values)
   ...
   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', action=FooAction)
   >>> parser.add_argument('bar', action=FooAction)
   >>> args = parser.parse_args('1 --foo 2'.split())
   Namespace(bar=None, foo=None) '1' None
   Namespace(bar='1', foo=None) '2' '--foo'
   >>> args
   Namespace(bar='1', foo='2')

Para mais detalhes, veja "Action".


"nargs"
-------

Os objetos "ArgumentParser" geralmente associam um único argumento de
linha de comando a uma única ação a ser executada. O argumento nomeado
"nargs" associa um número diferente de argumentos de linha de comando
com uma única ação. Veja também Especificando argumentos ambíguos. Os
valores suportados são:

* "N" (um inteiro). Os argumentos "N" da linha de comando serão
  reunidos em uma lista. Por exemplo:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', nargs=2)
     >>> parser.add_argument('bar', nargs=1)
     >>> parser.parse_args('c --foo a b'.split())
     Namespace(bar=['c'], foo=['a', 'b'])

  Observe que "nargs=1" produz uma lista de um item. Isso é diferente
  do padrão, em que o item é produzido sozinho.

* "'?'". Um argumento será consumido da linha de comando, se possível,
  e produzido como um único item. Se nenhum argumento de linha de
  comando estiver presente, o valor de default será produzido. Observe
  que, para argumentos opcionais, há um caso adicional - a string de
  opções está presente, mas não é seguida por um argumento de linha de
  comando. Neste caso o valor de const será produzido. Alguns exemplos
  para ilustrar isso:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', nargs='?', const='c', default='d')
     >>> parser.add_argument('bar', nargs='?', default='d')
     >>> parser.parse_args(['XX', '--foo', 'YY'])
     Namespace(bar='XX', foo='YY')
     >>> parser.parse_args(['XX', '--foo'])
     Namespace(bar='XX', foo='c')
     >>> parser.parse_args([])
     Namespace(bar='d', foo='d')

  Um dos usos mais comuns de "nargs='?'" é permitir arquivos de
  entrada e saída opcionais:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('infile', nargs='?')
     >>> parser.add_argument('outfile', nargs='?')
     >>> parser.parse_args(['input.txt', 'output.txt'])
     Namespace(infile='input.txt', outfile='output.txt')
     >>> parser.parse_args(['input.txt'])
     Namespace(infile='input.txt', outfile=None)
     >>> parser.parse_args([])
     Namespace(infile=None, outfile=None)

* "'*'". Todos os argumentos de linha de comando presentes são
  reunidos em uma lista. Note que geralmente não faz muito sentido ter
  mais de um argumento posicional com "nargs='*'", mas vários
  argumentos opcionais com "nargs='*'" são possíveis. Por exemplo:

     >>> parser = argparse.ArgumentParser()
     >>> parser.add_argument('--foo', nargs='*')
     >>> parser.add_argument('--bar', nargs='*')
     >>> parser.add_argument('baz', nargs='*')
     >>> parser.parse_args('a b --foo x y --bar 1 2'.split())
     Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

* "'+'". Assim como "'*'", todos os argumentos de linha de comando
  presentes são reunidos em uma lista. Além disso, uma mensagem de
  erro será gerada se não houver pelo menos um argumento de linha de
  comando presente. Por exemplo:

     >>> parser = argparse.ArgumentParser(prog='PROG')
     >>> parser.add_argument('foo', nargs='+')
     >>> parser.parse_args(['a', 'b'])
     Namespace(foo=['a', 'b'])
     >>> parser.parse_args([])
     usage: PROG [-h] foo [foo ...]
     PROG: error: the following arguments are required: foo

Se o argumento nomeado "nargs" não for fornecido, o número de
argumentos consumidos é determinado por action. Geralmente, isso
significa que um único argumento de linha de comando será usado e um
único item (não uma lista) será produzido. Ações que não fazem uso de
argumentos da linha de comando (por exemplo, "'store_const'") definem
"nargs=0".


"const"
-------

O argumento "const" de "add_argument()" é usado para manter valores
constantes que não são lidos da linha de comando, mas são necessários
para as várias ações "ArgumentParser". Os dois usos mais comuns são:

* Quando "add_argument()" é chamado com "action='store_const'" ou
  "action='append_const'". Essas ações adicionam o valor "const" a um
  dos atributos do objeto retornado por "parse_args()". Consulte a
  descrição da action para obter exemplos. Se "const" não for
  fornecido "add_argument()", será recebido um valor padrão de "None".

* Quando "add_argument()" é chamado com strings de opções (como "-f"
  ou "--foo") e "nargs='?'". Isso cria um argumento opcional que pode
  ser seguido por zero ou um argumento de linha de comando. Ao
  analisar a linha de comando, se a string de opções for encontrada
  sem nenhum argumento de linha de comando seguindo, o valor de
  "const" será usado. Veja a descrição de nargs para exemplos.

Alterado na versão 3.11: "const=None" por padrão, incluindo quando
"action='append_const'" ou "action='store_const'".


"default"
---------

Todos os argumentos opcionais e alguns argumentos posicionais podem
ser omitidos na linha de comando. O argumento nomeado "default" de
"add_argument()" especifica qual valor deve ser usado se o argumento
de linha de comando não estiver presente. Por exemplo:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', default=42)
   >>> parser.parse_args(['--foo', '2'])
   Namespace(foo='2')
   >>> parser.parse_args([])
   Namespace(foo=42)

Se "default" for omitido, "add_argument()" utiliza um valor definido
anteriormente para o dest por meio de "set_defaults()", ou, na falta
deste, um argument_default que não seja "None". Se nenhum dos dois
estiver definido, utiliza-se o valor padrão da própria ação.

Se o espaço de nomes de destino já tiver um atributo definido, a ação
*default* não o substituirá:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', default=42)
   >>> parser.parse_args([], namespace=argparse.Namespace(foo=101))
   Namespace(foo=101)

Se o valor "default" for uma string, o analisador analisa o valor como
se fosse um argumento de linha de comando. Em particular, o analisador
aplica qualquer argumento de conversão type, se fornecido, antes de
definir o atributo no valor de retorno "Namespace". Caso contrário, o
analisador usa o valor como está:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--length', default='10', type=int)
   >>> parser.add_argument('--width', default=10.5, type=int)
   >>> parser.parse_args()
   Namespace(length=10, width=10.5)

Para argumentos posicionais com nargs igual a "?" ou "*", o valor
"default" é usado quando nenhum argumento de linha de comando estava
presente:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('foo', nargs='?', default=42)
   >>> parser.parse_args(['a'])
   Namespace(foo='a')
   >>> parser.parse_args([])
   Namespace(foo=42)

Como "nargs='*'" agrupa quaisquer valores fornecidos em uma lista, um
argumento posicional ausente produz em uma lista vazia ("[]"). Apenas
um *default* com valor diferente de "None" substitui esse
comportamento (portanto, "default=None" ainda resulta em "[]").

Para argumentos obrigatórios, isto é, marcados com required, o valor
"default" é ignorado. Por exemplo, isso se aplica a argumentos
posicionais com valores de nargs diferentes de "?" ou "*", ou
argumentos opcionais marcados como "required=True".

Fornecer "default=argparse.SUPPRESS" faz com que nenhum atributo seja
adicionado se o argumento da linha de comando não estiver presente:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', default=argparse.SUPPRESS)
   >>> parser.parse_args([])
   Namespace()
   >>> parser.parse_args(['--foo', '1'])
   Namespace(foo='1')


"type"
------

Por padrão, o analisador sintático lê os argumentos de linha de
comando como strings simples. No entanto, muitas vezes a string da
linha de comando deve ser interpretada como outro tipo, como "float"
ou "int". O argumento nomeado "type" para "add_argument()" permite que
qualquer verificação de tipo e conversões de tipo necessárias sejam
realizadas.

Se o argumento nomeado type for usado com default, o conversor de tipo
só será aplicado se o padrão for uma string.

O argumento para "type" pode ser um chamável que aceite uma única
string ou o nome de um tipo registrado (veja "register()"). Se a
função levantar "ArgumentTypeError", "TypeError" ou "ValueError", a
exceção será capturada e uma mensagem de erro bem formatada será
exibida. Nenhum outro tipo de exceção é tratado.

Tipos e funções embutidas comuns podem ser usados como conversores de
tipo:

   import argparse
   import pathlib

   parser = argparse.ArgumentParser()
   parser.add_argument('count', type=int)
   parser.add_argument('distance', type=float)
   parser.add_argument('street', type=ascii)
   parser.add_argument('code_point', type=ord)
   parser.add_argument('datapath', type=pathlib.Path)

Funções definidas pelo usuário também podem ser usadas:

   >>> def hyphenated(string):
   ...     return '-'.join([word[:4] for word in string.casefold().split()])
   ...
   >>> parser = argparse.ArgumentParser()
   >>> _ = parser.add_argument('short_title', type=hyphenated)
   >>> parser.parse_args(['"Um conto de duas cidades"'])
   Namespace(short_title='"um-cont-de-duas-cida')

A função "bool()" não é recomendada como conversor de tipo. Tudo o que
ele faz é converter strings vazias em "False" e strings não vazias em
"True". Geralmente não é isso que se deseja:

   >>> parser = argparse.ArgumentParser()
   >>> _ = parser.add_argument('--verbose', type=bool)
   >>> parser.parse_args(['--verbose', 'False'])
   Namespace(verbose=True)

Consulte "BooleanOptionalAction" ou "action='store_true'" para
alternativas comuns.

Em geral, o argumento nomeado "type" é uma conveniência a ser usada
apenas para conversões simples que geram apenas uma das três exceções
suportadas. Qualquer coisa com tratamento de erros ou gerenciamento de
recursos mais interessante deve ser feita posteriormente, após a
análise dos argumentos.

Por exemplo, conversões JSON ou YAML têm casos de erros complexos que
exigem relatórios melhores do que os fornecidos pelo argumento nomeado
"type". Um "JSONDecodeError" não seria bem formatado e uma exceção
"FileNotFoundError" não seria tratada.

Mesmo "FileType" tem suas limitações no uso com o argumento nomeado
"type". Se um argumento usar "FileType" e um argumento subsequente
falhar, um erro será relatado, mas o arquivo não será fechado
automaticamente. Neste caso, seria melhor esperar até que o analisador
tenha sido executado e então usar a instrução "with" para gerenciar os
arquivos.

Para verificadores de tipo que simplesmente verificam um conjunto fixo
de valores, considere usar o argumento nomeado choices.


"choices"
---------

Alguns argumentos de linha de comando devem ser selecionados em um
conjunto restrito de valores. Eles podem ser tratados passando um
objeto sequência como o argumento nomeado *choices* para
"add_argument()". Quando a linha de comando for analisada, os valores
dos argumentos serão verificados e uma mensagem de erro será exibida
se o argumento não for um dos valores aceitáveis:

   >>> parser = argparse.ArgumentParser(prog='game.py')
   >>> parser.add_argument('move', choices=['pedra', 'papel', 'tesoura'])
   >>> parser.parse_args(['padra'])
   Namespace(move='padr')
   >>> parser.parse_args(['fogo'])
   usage: game.py [-h] {pedra,papel,tesoura}
   game.py: error: argument move: invalid choice: 'fogo' (choose from 'pedra',
   'papel', 'tesoura')

Qualquer sequência pode ser passada como o valor *choices*, portanto
objetos "list", objetos "tuple" e sequências personalizadas são todos
suportados.

O uso de "enum.Enum" não é recomendado porque é difícil controlar sua
aparência no uso, na ajuda e nas mensagens de erro.

Observe que *choices* são verificadas após a realização de quaisquer
conversões de type, portanto, os objetos em *choices* devem
corresponder ao type especificado. Isso pode fazer com que *choices*
pareçam estranhos no uso, na ajuda ou em mensagens de erro.

Para manter *choices* fácel de usar, considere um invólucro de tipo
personalizado que converta e formate valores, ou omita type e lide com
a conversão no código da sua aplicação.

As opções formatadas substituem o *metavar* padrão que normalmente é
derivado de *dest*. Geralmente é isso que você deseja porque o usuário
nunca vê o parâmetro *dest*. Se esta exibição não for desejável
(talvez porque haja muitas opções), basta especificar um metavar
explícito.


"required"
----------

Em geral, o módulo "argparse" presume que sinalizadores como "-f" e "
--bar" indicam argumentos *opcionais*, que sempre podem ser omitidos
na linha de comando. Para tornar uma opção obrigatória, "True" pode
ser especificado para o argumento nomeado "required=" para
"add_argument()":

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', required=True)
   >>> parser.parse_args(['--foo', 'BAR'])
   Namespace(foo='BAR')
   >>> parser.parse_args([])
   usage: [-h] --foo FOO
   : error: the following arguments are required: --foo

Como mostra o exemplo, se uma opção estiver marcada como "required",
"parse_args()" reportará um erro se essa opção não estiver presente na
linha de comando.

Nota:

  As opções obrigatórias são geralmente consideradas inadequadas
  porque os usuários esperam que as *opções* sejam *opcionais* e,
  portanto, devem ser evitadas quando possível.


"help"
------

O valor "help" é uma string contendo uma breve descrição do argumento.
Quando um usuário solicita ajuda (geralmente usando "-h" ou "--help"
na linha de comando), estas descrições de "help" serão exibidas com
cada argumento.

As strings "help" podem incluir vários especificadores de formato para
evitar a repetição de coisas como o nome do programa ou o argumento
default. Os especificadores disponíveis incluem o nome do programa,
"%(prog)s" e a maioria dos argumentos nomeados para "add_argument()",
por exemplo. "%(default)s", "%(type)s", etc.:

   >>> parser = argparse.ArgumentParser(prog='frobble')
   >>> parser.add_argument('bar', nargs='?', type=int, default=42,
   ...                     help='the bar to %(prog)s (default: %(default)s)')
   >>> parser.print_help()
   usage: frobble [-h] [bar]

   positional arguments:
    bar     the bar to frobble (default: 42)

   options:
    -h, --help  show this help message and exit

Como a string de ajuda oferece suporte à formatação com %, se você
quiser que um literal "%" apareça na string de ajuda, você deve
escapá-lo como "%%".

"argparse" oferece suporte a silenciar a entrada de ajuda para certas
opções, definindo o valor "help" como "argparse.SUPPRESS":

   >>> parser = argparse.ArgumentParser(prog='frobble')
   >>> parser.add_argument('--foo', help=argparse.SUPPRESS)
   >>> parser.print_help()
   usage: frobble [-h]

   options:
     -h, --help  show this help message and exit


"metavar"
---------

Quando "ArgumentParser" gera mensagens de ajuda, ele precisa de alguma
forma de se referir a cada argumento esperado. Por padrão, os objetos
"ArgumentParser" usam o valor dest como o "nome" de cada objeto. Por
padrão, para ações de argumentos posicionais, o valor dest é usado
diretamente, e para ações de argumentos opcionais, o valor dest é
maiúsculo. Portanto, um único argumento posicional com "dest='bar'"
será referido como "bar". Um único argumento opcional "--foo" que deve
ser seguido por um único argumento de linha de comando será referido
como "FOO". Um exemplo:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo')
   >>> parser.add_argument('bar')
   >>> parser.parse_args('X --foo Y'.split())
   Namespace(bar='X', foo='Y')
   >>> parser.print_help()
   usage:  [-h] [--foo FOO] bar

   positional arguments:
    bar

   options:
    -h, --help  show this help message and exit
    --foo FOO

Um nome alternativo pode ser especificado com "metavar":

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', metavar='YYY')
   >>> parser.add_argument('bar', metavar='XXX')
   >>> parser.parse_args('X --foo Y'.split())
   Namespace(bar='X', foo='Y')
   >>> parser.print_help()
   usage:  [-h] [--foo YYY] XXX

   positional arguments:
    XXX

   options:
    -h, --help  show this help message and exit
    --foo YYY

Observe que "metavar" apenas altera o nome *exibido* - o nome do
atributo no objeto "parse_args()" ainda é determinado pelo valor dest.

Valores diferentes de "nargs" podem fazer com que o metavar seja usado
múltiplas vezes. Fornecer uma tupla para "metavar" especifica uma
exibição diferente para cada um dos argumentos:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x', nargs=2)
   >>> parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
   >>> parser.print_help()
   usage: PROG [-h] [-x X X] [--foo bar baz]

   options:
    -h, --help     show this help message and exit
    -x X X
    --foo bar baz


"dest"
------

A maioria das ações "ArgumentParser" adiciona algum valor como um
atributo do objeto retornado por "parse_args()". O nome deste atributo
é determinado pelo argumento nomeado "dest" de "add_argument()". Para
ações de argumento posicional, "dest" é normalmente fornecido como o
primeiro argumento para "add_argument()":

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('bar')
   >>> parser.parse_args(['XXX'])
   Namespace(bar='XXX')

Para ações de argumentos opcionais, o valor de "dest" é normalmente
inferido a partir das strings de opção. A classe "ArgumentParser" gera
o valor de "dest" pegando a primeira string de opção longa (que começa
com dois hifens) e removendo os caracteres "-" iniciais. Se nenhuma
string de opção longa com dois hifens for fornecida, "dest" será
derivado da primeira string de opção longa com um único hífen,
removendo o caractere "-" inicial. Se nenhuma string de opção longa
for fornecida, "dest" será derivado da primeira string de opção curta,
removendo o caractere "-" inicial. Quaisquer caracteres "-" internos
serão convertidos em caracteres "_", para garantir que a string seja
um nome de atributo válido. Os exemplos abaixo ilustram esse
comportamento:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('-f', '--foo-bar', '--foo')
   >>> parser.add_argument('-q', '-quz')
   >>> parser.add_argument('-x', '-y')
   >>> parser.parse_args('-f 1 -q 2 -x 3'.split())
   Namespace(foo_bar='1', quz='2', x='3')
   >>> parser.parse_args('--foo 1 -quz 2 -y 3'.split())
   Namespace(foo_bar='1', quz='2', x='2')

"dest" permite que um nome de atributo personalizado seja fornecido:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument('--foo', dest='bar')
   >>> parser.parse_args('--foo XXX'.split())
   Namespace(bar='XXX')

Múltiplos argumentos podem compartilhar o mesmo "dest". Por padrão, o
valor proveniente do último argumento desse tipo fornecido na linha de
comando prevalece. Em vez disso, utilize "action='append'" para
coletar os valores de todos eles em uma lista. Para casos de conflito
entre *strings* de opção, em vez de nomes de "dest", consulte
conflict_handler.

Alterado na versão 3.15: Opções longas precedidas por um único traço
agora têm precedência sobre as opções curtas.


"deprecated"
------------

Durante a vida de um projeto, alguns argumentos podem precisar ser
removidos da linha de comando. Antes de removê-los, você deve informar
aos seus usuários que os argumentos estão descontinuados e serão
removidos. O argumento nomeado "deprecated" de "add_argument()", cujo
padrão é "False", especifica se o argumento está descontinuado e será
removido no futuro. Para argumentos, se "deprecated" for "True", então
um aviso será enviado para "sys.stderr" (saída de erro) quando o
argumento for usado:

   >>> import argparse
   >>> parser = argparse.ArgumentParser(prog='snake.py')
   >>> parser.add_argument('--legs', default=0, type=int, deprecated=True)
   >>> parser.parse_args([])
   Namespace(legs=0)
   >>> parser.parse_args(['--legs', '4'])
   snake.py: warning: option '--legs' is deprecated
   Namespace(legs=4)

Adicionado na versão 3.13.


Classes de ação
---------------

As classes "Action" implementam a API de Action, um chamável que
retorna um chamável que processa argumentos da linha de comando.
Qualquer objeto que siga esta API pode ser passado como parâmetro
"action" para "add_argument()".

class argparse.Action(option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None)

   Objetos "Action" são usados por um "ArgumentParser" para
   representar as informações necessárias para analisar um único
   argumento de uma ou mais strings da linha de comando. A classe
   "Action" deve aceitar os dois argumentos posicionais mais quaisquer
   argumentos nomeados passados para "ArgumentParser.add_argument()",
   exceto o próprio "action".

   Instâncias de "Action" (ou valor de retorno de qualquer chamável
   para o parâmetro "action") devem ter atributos "dest",
   "option_strings", "default", "type", "required", "help", etc.
   definidos. A maneira mais fácil de garantir que esses atributos
   sejam definidos é chamar "Action.__init__()".

   __call__(parser, namespace, values, option_string=None)

      As instâncias de "Action" devem ser chamáveis, portanto, as
      subclasses devem substituir o método "__call__()", que deve
      aceitar quatro parâmetros:

      * *parser* - O objeto "ArgumentParser" que contém esta ação.

      * *namespace* - O objeto "Namespace" que será retornado por
        "parse_args()". A maioria das ações adicionam um atributo a
        este objeto usando "setattr()".

      * *values* - Os argumentos de linha de comando associados, com
        qualquer conversões de tipo aplicadas. Conversões de tipo são
        especificadas com o argumento nomeado type para
        "add_argument()".

      * *option_string* - A string da opção que foi usada para invocar
        esta ação. O argumento "option_string" é opcional e estará
        ausente se a ação estiver associada a um argumento posicional.

      O método "__call__()" pode executar ações arbitrárias, mas
      normalmente definirá atributos em "namespace" com base em "dest"
      e "values".

   format_usage()

      As subclasses de "Action" podem definir um método
      "format_usage()" que não recebe argumento e retorna uma string
      que será usada ao exibir a mensagem de uso do programa. Se tal
      método não for fornecido, um padrão sensato será usado.

class argparse.BooleanOptionalAction

   Uma subclasse de "Action" para manipular sinalizadores booleanos
   com opções positivas e negativas. Adicionar um único argumento,
   como "--foo", cria automaticamente as opções "--foo" e "--no-foo",
   armazenando "True" e "False" respectivamente:

      >>> import argparse
      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', action=argparse.BooleanOptionalAction)
      >>> parser.parse_args(['--no-foo'])
      Namespace(foo=False)

   Opções longas com um único hífen também são suportadas. Por
   exemplo, a opção negativa "-nofoo" é adicionada automaticamente
   para a opção positiva "-foo". No entanto, nenhuma opção adicional é
   criada para opções curtas, como "-f".

   Adicionado na versão 3.9.

   Alterado na versão 3.15: Adiciona suporte para opções de um único
   hífen.Adicionado suporte para prefix_chars alternativo.


O método parse_args()
=====================

ArgumentParser.parse_args(args=None, namespace=None)

   Converte strings de argumento em objetos e os atribui como
   atributos do espaço de nomes. Retorna o espaço de nomes preenchido.

   Chamadas anteriores para "add_argument()" determinam exatamente
   quais objetos são criados e como eles são atribuídos. Veja a
   documentação de "add_argument()" para detalhes.

   * args - Lista de strings para analisar. O padrão é obtido de
     "sys.argv".

   * namespace - Um objeto para receber os atributos. O padrão é um
     novo objeto "Namespace" vazio.


Sintaxe de valores da opção
---------------------------

O método "parse_args()" provê várias maneiras de especificar o valor
de uma opção (se ele pegar uma). No caso mais simples, a opção e seu
valor são passados como dois argumentos separados:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x')
   >>> parser.add_argument('--foo')
   >>> parser.parse_args(['-x', 'X'])
   Namespace(foo=None, x='X')
   >>> parser.parse_args(['--foo', 'FOO'])
   Namespace(foo='FOO', x=None)

Para opções longas (opções com nomes maiores que um único caractere),
a opção e o valor também podem ser passados como um único argumento de
linha de comando, usando "=" para separá-los:

   >>> parser.parse_args(['--foo=FOO'])
   Namespace(foo='FOO', x=None)

Para opções curtas (opções com apenas um caractere), a opção e seu
valor podem ser concatenados:

   >>> parser.parse_args(['-xX'])
   Namespace(foo=None, x='X')

Várias opções curtas podem ser unidas, usando apenas um único prefixo
"-", desde que apenas a última opção (ou nenhuma delas) exija um
valor:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x', action='store_true')
   >>> parser.add_argument('-y', action='store_true')
   >>> parser.add_argument('-z')
   >>> parser.parse_args(['-xyzZ'])
   Namespace(x=True, y=True, z='Z')


Argumentos inválidos
--------------------

Ao analisar a linha de comando, "parse_args()" verifica uma variedade
de erros, incluindo opções ambíguas, tipos inválidos, opções
inválidas, número incorreto de argumentos posicionais, etc. Quando
encontra tal erro, ele sai e imprime o erro junto com uma mensagem de
uso:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('--foo', type=int)
   >>> parser.add_argument('bar', nargs='?')

   >>> # tipo inválido
   >>> parser.parse_args(['--foo', 'spam'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: argument --foo: invalid int value: 'spam'

   >>> # opção inválida
   >>> parser.parse_args(['--bar'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: unrecognized arguments: --bar

   >>> # número errado de argumentos
   >>> parser.parse_args(['spam', 'badger'])
   usage: PROG [-h] [--foo FOO] [bar]
   PROG: error: unrecognized arguments: badger


Argumentos contendo "-"
-----------------------

O método "parse_args()" tenta mostrar erros sempre que o usuário
claramente cometeu um erro, mas algumas situações são inerentemente
ambíguas. Por exemplo, o argumento de linha de comando "-1" pode ser
uma tentativa de especificar uma opção ou uma tentativa de fornecer um
argumento posicional. O método "parse_args()" é cauteloso aqui:
argumentos posicionais só podem começar com "-" se eles se parecerem
com números negativos e não houver opções no analisador sintático que
se pareçam com números negativos:

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-x')
   >>> parser.add_argument('foo', nargs='?')

   >>> # nenhuma opção de número negativo, então -1 é um argumento posicional
   >>> parser.parse_args(['-x', '-1'])
   Namespace(foo=None, x='-1')

   >>> # nenhuma opção de número negativo, então -1 e -5 são argumentos posicionais
   >>> parser.parse_args(['-x', '-1', '-5'])
   Namespace(foo='-5', x='-1')

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-1', dest='one')
   >>> parser.add_argument('foo', nargs='?')

   >>> # opções de número negativo presentes, então -1 é uma opção
   >>> parser.parse_args(['-1', 'X'])
   Namespace(foo=None, one='X')

   >>> # opções de número negativo presentes, então -2 é uma opção
   >>> parser.parse_args(['-2'])
   usage: PROG [-h] [-1 ONE] [foo]
   PROG: error: unrecognized arguments: -2

   >>> # opções de número negativo presentes, então ambos -1s são opções
   >>> parser.parse_args(['-1', '-1'])
   usage: PROG [-h] [-1 ONE] [foo]
   PROG: error: argument -1: expected one argument

Se você tiver argumentos posicionais que devem começar com "-" e não
se parecem com números negativos, você pode inserir o pseudoargumento
"'--'" que informa "parse_args()" que tudo depois disso é um argumento
posicional:

   >>> parser.parse_args(['--', '-f'])
   Namespace(foo='-f', one=None)

Veja também o tutorial do argparse sobre argumentos ambíguos para mais
detalhes.

Alterado na versão 3.14: A correspondência de números negativos foi
expandida para incluir números em notação científica ("-2.5e-6"),
números que contêm sublinhados ("-1_234.5") e números complexos ("-1
.2e-3j").


Abreviações de argumento (correspondência de prefixo)
-----------------------------------------------------

O método "parse_args()" por padrão permite que opções longas sejam
abreviadas para um prefixo, se a abreviação não for ambígua (o prefixo
corresponde a uma opção única):

   >>> parser = argparse.ArgumentParser(prog='PROG')
   >>> parser.add_argument('-bacon')
   >>> parser.add_argument('-badger')
   >>> parser.parse_args('-bac MMM'.split())
   Namespace(bacon='MMM', badger=None)
   >>> parser.parse_args('-bad WOOD'.split())
   Namespace(bacon=None, badger='WOOD')
   >>> parser.parse_args('-ba BA'.split())
   usage: PROG [-h] [-bacon BACON] [-badger BADGER]
   PROG: error: ambiguous option: -ba could match -badger, -bacon

Um erro é produzido para argumentos que podem produzir mais de uma
opção. Este recurso pode ser desabilitado definindo allow_abbrev como
"False".


Além do "sys.argv"
------------------

Às vezes, pode ser útil ter uma instância de "ArgumentParser"
analisando argumentos diferentes daqueles de "sys.argv". Isso pode ser
feito passando uma lista de strings para "parse_args()". Isso é útil
para testar no prompt interativo:

   >>> parser = argparse.ArgumentParser()
   >>> parser.add_argument(
   ...     'integers', metavar='int', type=int, choices=range(10),
   ...     nargs='+', help='an integer in the range 0..9')
   >>> parser.add_argument(
   ...     '--sum', dest='accumulate', action='store_const', const=sum,
   ...     default=max, help='sum the integers (default: find the max)')
   >>> parser.parse_args(['1', '2', '3', '4'])
   Namespace(accumulate=<built-in function max>, integers=[1, 2, 3, 4])
   >>> parser.parse_args(['1', '2', '3', '4', '--sum'])
   Namespace(accumulate=<built-in function sum>, integers=[1, 2, 3, 4])


O objeto Namespace
------------------

class argparse.Namespace

   Classe simples usada por padrão por "parse_args()" para criar um
   objeto contendo atributos e retorná-lo.

   Esta classe é deliberadamente simples, apenas uma subclasse
   "object" com uma representação de string legível. Se você preferir
   ter uma visão dos atributos do tipo dict, você pode usar o idioma
   padrão do Python, "vars()":

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> args = parser.parse_args(['--foo', 'BAR'])
      >>> vars(args)
      {'foo': 'BAR'}

   Também pode ser útil ter um "ArgumentParser" atribuindo atributos a
   um objeto já existente, em vez de um novo objeto "Namespace". Isso
   pode ser obtido especificando o argumento nomeado "namespace=":

      >>> class C:
      ...     pass
      ...
      >>> c = C()
      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> parser.parse_args(args=['--foo', 'BAR'], namespace=c)
      >>> c.foo
      'BAR'


Outros utilitários
==================


Subcomandos
-----------

ArgumentParser.add_subparsers(*[, title][, description][, prog][, parser_class][, action][, dest][, required][, help][, metavar])

   Muitos programas dividem sua funcionalidade em vários subcomandos,
   por exemplo, o programa "svn" pode invocar subcomandos como "svn
   checkout", "svn update" e "svn commit". Dividir a funcionalidade
   dessa forma pode ser uma ideia particularmente boa quando um
   programa executa várias funções diferentes que exigem diferentes
   tipos de argumentos de linha de comando. "ArgumentParser" oferece
   suporte à criação de tais subcomandos por meio do método
   "add_subparsers()". O método "add_subparsers()" é normalmente
   chamado sem argumentos e retorna um objeto de ação especial. Este
   objeto tem um único método, "add_parser()", que recebe um nome de
   comando e quaisquer argumentos do construtor "ArgumentParser" e
   retorna um objeto "ArgumentParser" que pode ser modificado
   normalmente.

   Descrição de parâmetros:

   * *title* - título para o grupo de subanalisadores na saída de
     ajuda; por padrão "subcomandos" se a descrição for fornecida,
     caso contrário, usa o título para argumentos posicionais

   * *description* - descrição para o grupo de subanalisadores na
     saída de ajuda, por padrão "None"

   * *prog* - informações de uso que serão exibidas com a ajuda do
     subcomando, por padrão o nome do programa e quaisquer argumentos
     posicionais antes do argumento do subanalisador

   * *parser_class* - classe que será usada para criar instâncias de
     subanalisadores, por padrão a classe do analisador atual (por
     exemplo, "ArgumentParser")

   * action - o tipo básico de ação a ser executada quando esse
     argumento é encontrado na linha de comando

   * dest - nome do atributo sob o qual o nome do subcomando será
     armazenado; por padrão "None" e nenhum valor é armazenado

   * required - Se um subcomando deve ou não ser fornecido, por padrão
     "False" (adicionado em 3.7)

   * help - ajuda para o grupo de subanalisadores na saída de ajuda,
     por padrão "None"

   * metavar - string que apresenta os subcomandos disponíveis na
     ajuda; por padrão é "None" e apresenta os subcomandos no formato
     {cmd1, cmd2, ..}

   Alguns exemplos de uso:

      >>> # cria o analisador de nível superior>>> parser = argparse.ArgumentParser(prog='PROG')>>> parser.add_argument('--foo', action='store_true', help='foo help')>>> subparsers = parser.add_subparsers(help='subcommand help')>>>>>> # cria o analisador para o comando "a">>> parser_a = subparsers.add_parser('a', help='a help')>>> parser_a.add_argument('bar', type=int, help='bar help')>>>>>> # cria o analisador para o comando "b">>> parser_b = subparsers.add_parser('b', help='b help')>>> parser_b.add_argument('--baz', choices=('X', 'Y', 'Z'), help='baz help')>>>>>> # analisa algumas listas de argumentos>>> parser.parse_args(['a', '12'])Namespace(bar=12, foo=False)>>> parser.parse_args(['--foo', 'b', '--baz', 'Z'])Namespace(baz='Z', foo=True)

   Note que o objeto retornado por "parse_args()" conterá apenas
   atributos para o analisador principal e para o subanalisador
   selecionado pela linha de comando (e não para quaisquer outros
   subanalisadores). Então, no exemplo acima, quando o comando "a" é
   especificado, apenas os atributos "foo" e "bar" estão presentes, e
   quando o comando "b" é especificado, apenas os atributos "foo" e
   "baz" estão presentes.

   Se um sub-analisador definir um argumento com o mesmo "dest" que o
   analisador pai, ambos compartilharão um único atributo no espaço de
   nomes; portanto, o valor do analisador pai não será preservado. Os
   usuários devem atribuir valores "dest" distintos a eles para manter
   ambos.

   Similarmente, quando uma mensagem de ajuda é solicitada de um
   subanalisador, apenas a ajuda para aquele parser em particular será
   exibida. A mensagem de ajuda não incluirá mensagens do analisador
   sintático pai nem do analisador sintático irmão. (Uma mensagem de
   ajuda para cada comando do subanalisador pode, entretanto, ser
   fornecida passando o argumento "help=" para "add_parser()", como
   acima.)

      >>> parser.parse_args(['--help'])usage: PROG [-h] [--foo] {a,b} ...positional arguments:  {a,b}   subcommand help    a     a help    b     b helpoptions:  -h, --help  show this help message and exit  --foo   foo help>>> parser.parse_args(['a', '--help'])usage: PROG a [-h] barpositional arguments:  bar     bar helpoptions:  -h, --help  show this help message and exit>>> parser.parse_args(['b', '--help'])usage: PROG b [-h] [--baz {X,Y,Z}]options:  -h, --help     show this help message and exit  --baz {X,Y,Z}  baz help

   O método "add_subparsers()" também aceita os argumentos nomeados
   "title" e "description". Quando qualquer um deles estiver presente,
   os comandos do subanalisador aparecerão em seu próprio grupo na
   saída de ajuda. Por exemplo:

      >>> parser = argparse.ArgumentParser()>>> subparsers = parser.add_subparsers(title='subcommands',...                                    description='valid subcommands',...                                    help='additional help')>>> subparsers.add_parser('foo')>>> subparsers.add_parser('bar')>>> parser.parse_args(['-h'])usage:  [-h] {foo,bar} ...options:  -h, --help  show this help message and exitsubcommands:  valid subcommands  {foo,bar}   additional help

   Uma maneira particularmente eficaz de lidar com subcomandos é
   combinar o uso do método "add_subparsers()" com chamadas ao método
   "set_defaults()", para que cada subanalisador saiba qual função
   Python deve executar. Por exemplo:

      >>> # funções do subanalisador functions>>> def foo(args):...     print(args.x * args.y)...>>> def bar(args):...     print('((%s))' % args.z)...>>> # cria o analisador de nível superior>>> parser = argparse.ArgumentParser()>>> subparsers = parser.add_subparsers(required=True)>>>>>> # cria o analisador do comando "foo">>> parser_foo = subparsers.add_parser('foo')>>> parser_foo.add_argument('-x', type=int, default=1)>>> parser_foo.add_argument('y', type=float)>>> parser_foo.set_defaults(func=foo)>>>>>> # cria o analisador do comando "foo">>> parser_bar = subparsers.add_parser('bar')>>> parser_bar.add_argument('z')>>> parser_bar.set_defaults(func=bar)>>>>>> # analisa os argumentos e chama a função que for selecionada>>> args = parser.parse_args('foo 1 -x 2'.split())>>> args.func(args)2.0>>>>>> # analisa os argumentos e chama a função que foi selecionada>>> args = parser.parse_args('bar XYZYX'.split())>>> args.func(args)((XYZYX))

   Dessa forma, você pode deixar "parse_args()" fazer o trabalho de
   chamar a função apropriada após a análise sintática do argumento
   ser concluída. Associar funções a ações como essa é, normalmente, a
   maneira mais fácil de lidar com as diferentes ações de cada um dos
   seus subanalisadores. No entanto, se for necessário verificar o
   nome do subanalisador que foi invocado, o argumento nomeado "dest"
   para a chamada "add_subparsers()" funcionará:

      >>> parser = argparse.ArgumentParser()>>> subparsers = parser.add_subparsers(dest='subparser_name')>>> subparser1 = subparsers.add_parser('1')>>> subparser1.add_argument('-x')>>> subparser2 = subparsers.add_parser('2')>>> subparser2.add_argument('y')>>> parser.parse_args(['2', 'frobble'])Namespace(subparser_name='2', y='frobble')

   Alterado na versão 3.7: Novo parâmetro somente-nomeado *required*.

   Alterado na versão 3.14: O *prog* do subanalisador não é mais
   afetado por uma mensagem de uso personalizada no analisador
   principal.

_SubParsersAction.add_parser(name, *, help=None, aliases=None, deprecated=False, **kwargs)

   Cria e retorna um novo objeto "ArgumentParser" para o subcomando
   *name*.

   O argumento *name* é o nome do subcomando.

   O argumento *help* fornece uma descrição curta para este
   subcomando.

   O argumento *aliases* permite fornecer nomes alternativos para este
   subcomando. Por exemplo:

      >>> parser = argparse.ArgumentParser()>>> subparsers = parser.add_subparsers()>>> checkout = subparsers.add_parser('checkout', aliases=['co'])>>> checkout.add_argument('foo')>>> parser.parse_args(['co', 'bar'])Namespace(foo='bar')

   O argumento *deprecated*, se definido como "True", marca o
   subcomando como descontinuado e emitirá um aviso quando ele for
   utilizado. Por exemplo:

      >>> parser = argparse.ArgumentParser(prog='chicken.py')
      >>> subparsers = parser.add_subparsers()
      >>> fly = subparsers.add_parser('fly', deprecated=True)
      >>> args = parser.parse_args(['fly'])
      chicken.py: warning: command 'fly' is deprecated
      Namespace()

   Todos os demais argumentos nomeados são passados diretamente ao
   construtor de "ArgumentParser".

   Adicionado na versão 3.13: Adicionado o parâmetro *deprecated*.


Objetos FileType
----------------

class argparse.FileType(mode='r', bufsize=-1, encoding=None, errors=None)

   A fábrica "FileType" cria objetos que podem ser passados para o
   argumento de tipo de "ArgumentParser.add_argument()". Argumentos
   que têm objetos "FileType" como seu tipo abrirão argumentos de
   linha de comando como arquivos com os modos solicitados, tamanhos
   de buffer, codificações e tratamento de erros (veja a função
   "open()" para mais detalhes):

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--raw', type=argparse.FileType('wb', 0))
      >>> parser.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))
      >>> parser.parse_args(['--raw', 'raw.dat', 'file.txt'])
      Namespace(out=<_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>, raw=<_io.FileIO name='raw.dat' mode='wb'>)

   Objetos FileType entendem o pseudoargumento "'-'" e o convertem
   automaticamente em "sys.stdin" para objetos "FileType" legíveis e
   "sys.stdout" para objetos "FileType" graváveis:

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('infile', type=argparse.FileType('r'))
      >>> parser.parse_args(['-'])
      Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)

   Nota:

     Se um argumento usar *FileType* e um argumento subsequente
     falhar, um erro será relatado, mas o arquivo não será fechado
     automaticamente. Isso também pode danificar os arquivos de saída.
     Neste caso, seria melhor esperar até que o analisador sintático
     tenha sido executado e então usar a instrução "with" para
     gerenciar os arquivos.

   Alterado na versão 3.4: Adicionados os parâmetros *encoding* e
   *errors*.

   Descontinuado desde a versão 3.14.


Grupos de argumentos
--------------------

ArgumentParser.add_argument_group(title=None, description=None, *[, argument_default][, conflict_handler])

   Por padrão, "ArgumentParser" agrupa os argumentos de linha de
   comando em "argumentos posicionais" e "opções" ao exibir mensagens
   de ajuda. Quando há um melhor agrupamento conceitual de argumentos
   do que este padrão, grupos apropriados podem ser criados usando o
   método "add_argument_group()":

      >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
      >>> group = parser.add_argument_group('grupo')
      >>> group.add_argument('--foo', help='Ajuda de foo')
      >>> group.add_argument('bar', help='Ajuda de bar')
      >>> parser.print_help()
      usage: PROG [--foo FOO] bar

      grupo:
        bar    Ajuda de bar
        --foo FOO  Ajuda de foo

   O método "add_argument_group()" retorna um objeto de grupo de
   argumentos que tem o método "add_argument()" como um
   "ArgumentParser" regular. Quando um argumento é adicionado ao
   grupo, o analisador o trata como um argumento normal, mas o exibe
   em um grupo separado nas mensagens de ajuda. O método
   "add_argument_group()" aceita argumentos *title* e *description*
   que podem ser usados para personalizar esta exibição:

      >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
      >>> group1 = parser.add_argument_group('grupo1', 'Descrição do grupo1')
      >>> group1.add_argument('foo', help='Ajuda de foo')
      >>> group2 = parser.add_argument_group('grupo2', 'Descrição do grupo2')
      >>> group2.add_argument('--bar', help='Ajuda de bar')
      >>> parser.print_help()
      usage: PROG [--bar BAR] foo

      grupo1:
        Descrição de grupo1

        foo    Ajuda de foo

      grupo2:
        Descrição de grupo2

        --bar BAR  Ajuda de bar

   Os parâmetros opcionais somente-nomeados argument_default e
   conflict_handler permitem um controle mais refinado do
   comportamento do grupo de argumentos. Esses parâmetros têm o mesmo
   significado que no construtor "ArgumentParser", mas se aplicam
   especificamente ao grupo de argumentos em vez do analisador
   sintático inteiro.

   Observe que quaisquer argumentos que não estejam nos grupos
   definidos pelo usuário serão encaminhados às seções usuais de
   "argumentos posicionais" e "argumentos opcionais".

   Em cada grupo, os argumentos podem ser exibidos em ordem diferente
   da em que foram adicionados.

   Descontinuado desde a versão 3.11, removido na versão 3.14: Chamar
   "add_argument_group()" em um grupo de argumentos agora levanta uma
   exceção. Esse aninhamento nunca foi suportado, frequentemente não
   funcionava corretamente e era exposto involuntariamente por meio de
   herança.

   Descontinuado desde a versão 3.14: Passar prefix_chars para
   "add_argument_group()" agora está descontinuado.


Exclusão mútua
--------------

ArgumentParser.add_mutually_exclusive_group(required=False)

   Cria um grupo mutuamente exclusivo. "argparse" garantirá que apenas
   um dos argumentos no grupo mutuamente exclusivo esteja presente na
   linha de comando:

      >>> parser = argparse.ArgumentParser(prog='PROG')
      >>> group = parser.add_mutually_exclusive_group()
      >>> group.add_argument('--foo', action='store_true')
      >>> group.add_argument('--bar', action='store_false')
      >>> parser.parse_args(['--foo'])
      Namespace(bar=True, foo=True)
      >>> parser.parse_args(['--bar'])
      Namespace(bar=False, foo=False)
      >>> parser.parse_args(['--foo', '--bar'])
      usage: PROG [-h] [--foo | --bar]
      PROG: error: argument --bar: not allowed with argument --foo

   O método "add_mutually_exclusive_group()" também aceita um
   argumento *obrigatório*, para indicar que pelo menos um dos
   argumentos mutuamente exclusivos é necessário:

      >>> parser = argparse.ArgumentParser(prog='PROG')
      >>> group = parser.add_mutually_exclusive_group(required=True)
      >>> group.add_argument('--foo', action='store_true')
      >>> group.add_argument('--bar', action='store_false')
      >>> parser.parse_args([])
      usage: PROG [-h] (--foo | --bar)
      PROG: error: one of the arguments --foo --bar is required

   Observe que atualmente grupos de argumentos mutuamente exclusivos
   não oferecem suporte aos argumentos *title* e *description* de
   "add_argument_group()". No entanto, um grupo mutuamente exclusivo
   pode ser adicionado a um grupo de argumentos que tenha um título e
   uma descrição. Por exemplo:

      >>> parser = argparse.ArgumentParser(prog='PROG')
      >>> group = parser.add_argument_group('Título do grupo', 'Descrição do grupo')
      >>> exclusive_group = group.add_mutually_exclusive_group(required=True)
      >>> exclusive_group.add_argument('--foo', help='ajuda de foo')
      >>> exclusive_group.add_argument('--bar', help='ajuda de bar')
      >>> parser.print_help()
      usage: PROG [-h] (--foo FOO | --bar BAR)

      options:
        -h, --help  show this help message and exit

      Título do grupo:
        Descrição do grupo

        --foo FOO   foo help
        --bar BAR   bar help

   Descontinuado desde a versão 3.11, removido na versão 3.14: Chamar
   "add_argument_group()" ou "add_mutually_exclusive_group()" em um
   grupo mutuamente exclusivo agora levanta uma exceção. Esse
   aninhamento nunca foi suportado, frequentemente não funcionava
   corretamente e era exposto involuntariamente por meio de herança.


Padrões do analisador sintático
-------------------------------

ArgumentParser.set_defaults(**kwargs)

   Na maioria das vezes, os atributos do objeto retornado por
   "parse_args()" serão totalmente determinados pela inspeção dos
   argumentos da linha de comando e das ações dos argumentos.
   "set_defaults()" permite que alguns atributos adicionais que são
   determinados sem qualquer inspeção da linha de comando sejam
   adicionados:

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('foo', type=int)
      >>> parser.set_defaults(bar=42, baz='badger')
      >>> parser.parse_args(['736'])
      Namespace(bar=42, baz='badger', foo=736)

   Observe que os valores padrão podem ser definidos tanto no nível do
   analisador sintático usando "set_defaults()" quanto no nível do
   argumento usando "add_argument()". Se ambos forem chamados para o
   mesmo argumento, o último valor padrão definido para o argumento
   será usado.

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', default='bar')
      >>> parser.set_defaults(foo='spam')
      >>> parser.parse_args([])
      Namespace(foo='spam')

   Padrões de nível de analisador podem ser particularmente úteis ao
   trabalhar com vários analisadores. Veja o método "add_subparsers()"
   para um exemplo desse tipo.

ArgumentParser.get_default(dest)

   Obtém o valor padrão para um atributo de espaço de nomes, conforme
   definido por "add_argument()" ou por "set_defaults()":

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', default='badger')
      >>> parser.get_default('foo')
      'badger'


Imprimindo a ajuda
------------------

Na maioria das aplicações típicas, "parse_args()" cuidará da
formatação e da impressão de quaisquer mensagens de uso ou erro. No
entanto, vários métodos de formatação estão disponíveis:

ArgumentParser.print_usage(file=None)

   Imprime uma breve descrição de como o "ArgumentParser" deve ser
   invocado na linha de comando. Se *file* for "None", "sys.stdout"
   será presumido.

ArgumentParser.print_help(file=None)

   Imprime uma mensagem de ajuda, incluindo o uso do programa e
   informações sobre os argumentos registrados com o "ArgumentParser".
   Se *file* for "None", "sys.stdout" será presumido.

Também há variantes desses métodos que simplesmente retornam uma
string em vez de imprimi-la:

ArgumentParser.format_usage()

   Retorna uma string contendo uma breve descrição de como o
   "ArgumentParser" deve ser invocado na linha de comando.

ArgumentParser.format_help()

   Retorna uma string contendo uma mensagem de ajuda, incluindo o uso
   do programa e informações sobre os argumentos registrados com o
   "ArgumentParser".


Análise parcial
---------------

ArgumentParser.parse_known_args(args=None, namespace=None)

   Às vezes, um script precisa manipular apenas um conjunto específico
   de argumentos de linha de comando, deixando quaisquer argumentos
   não reconhecidos para outro script ou programa. Nesses casos, o
   método "parse_known_args()" pode ser útil.

   Este método funciona de forma semelhante a "parse_args()", mas não
   levanta erro para argumentos extras não reconhecidos. Em vez disso,
   ele analisa os argumentos conhecidos e retorna uma tupla de dois
   itens que contém o espaço de nomes preenchido e a lista de
   quaisquer argumentos não reconhecidos.

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo', action='store_true')
      >>> parser.add_argument('bar')
      >>> parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
      (Namespace(bar='BAR', foo=True), ['--badger', 'spam'])

Aviso:

  As regras de correspondência de prefixo se aplicam a
  "parse_known_args()". O analisador pode usar uma opção mesmo que
  seja apenas um prefixo de uma de suas opções conhecidas, em vez de
  deixá-la na lista de argumentos restantes.


Personalizando a análise de arquivos
------------------------------------

ArgumentParser.convert_arg_line_to_args(arg_line)

   Argumentos lidos de um arquivo (veja o argumento nomeado
   *fromfile_prefix_chars* para o construtor "ArgumentParser") são
   lidos com um argumento por linha. "convert_arg_line_to_args()" pode
   ser substituído para uma leitura mais sofisticada.

   Este método recebe um único argumento *arg_line* que é uma string
   lida do arquivo de argumentos. Ele retorna uma lista de argumentos
   analisados dessa string. O método é chamado uma vez por linha lida
   do arquivo de argumentos, em ordem.

   Uma substituição útil desse método é aquela que trata cada palavra
   separada por espaços como um argumento. O exemplo a seguir
   demonstra como fazer isso:

      class MyArgumentParser(argparse.ArgumentParser):
          def convert_arg_line_to_args(self, arg_line):
              return arg_line.split()

   Observe que, com essa substituição, um argumento não pode mais
   conter espaços, uma vez que cada palavra separada por espaços passa
   a ser um argumento distinto.


Métodos de saída
----------------

ArgumentParser.exit(status=0, message=None)

   Este método encerra o programa, saindo com o *status* especificado
   e, se fornecido, imprime uma *message* para "sys.stderr" antes
   disso. O usuário pode sobrescrever este método para lidar com essas
   etapas de forma diferente:

      class ErrorCatchingArgumentParser(argparse.ArgumentParser):
          def exit(self, status=0, message=None):
              if status:
                  raise Exception(f'Exiting because of an error: {message}')
              exit(status)

ArgumentParser.error(message)

   Este método imprime uma mensagem de uso, incluindo a *message*, em
   "sys.stderr" e encerra o programa com um código de status 2.


Análise misturada
-----------------

ArgumentParser.parse_intermixed_args(args=None, namespace=None)

ArgumentParser.parse_known_intermixed_args(args=None, namespace=None)

   Vários comandos Unix permitem que o usuário misture argumentos
   opcionais com argumentos posicionais. Os métodos
   "parse_intermixed_args()" e "parse_known_intermixed_args()"
   oferecem suporte a esse estilo de análise.

   Esses analisadores não oferecem suporte a todos os recursos do
   "argparse" e vão levantar exceções se recursos não suportados forem
   usados. Em particular, subanalisadores e grupos mutuamente
   exclusivos que incluem tanto opcionais quanto posicionais não são
   suportados.

   O exemplo a seguir mostra a diferença entre "parse_known_args()" e
   "parse_intermixed_args()": o primeiro retorna "['2', '3']" como
   argumentos não analisados, enquanto o último coleta todos os
   posicionais em "rest".

      >>> parser = argparse.ArgumentParser()
      >>> parser.add_argument('--foo')
      >>> parser.add_argument('cmd')
      >>> parser.add_argument('rest', nargs='*', type=int)
      >>> parser.parse_known_args('doit 1 --foo bar 2 3'.split())
      (Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
      >>> parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
      Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])

   "parse_known_intermixed_args()" retorna uma tupla de dois itens
   contendo o espaço de nomes preenchido e a lista de strings de
   argumentos restantes. "parse_intermixed_args()" levanta um erro se
   houver strings de argumentos não analisadas restantes.

   Adicionado na versão 3.7.


Registrando ações e tipos personalizados
----------------------------------------

ArgumentParser.register(registry_name, value, object)

   Às vezes, é desejável usar uma string personalizada em mensagens de
   erro para fornecer uma saída mais amigável ao usuário. Nesses
   casos, "register()" pode ser usado para registrar ações ou tipos
   personalizados com um analisador sintático e permitir que você faça
   referência ao tipo pelo nome registrado em vez do nome do chamável.

   O método "register()" aceita três argumentos - um *registry_name*,
   especificando o registro interno onde o objeto será armazenado (por
   exemplo, "action", "type"), *value*, que é a chave sob a qual o
   objeto será registrado, e object, o chamável a ser registrado.

   O exemplo a seguir mostra como registrar um tipo personalizado com
   um analisador:

      >>> import argparse
      >>> parser = argparse.ArgumentParser()
      >>> parser.register('type', 'hexadecimal integer', lambda s: int(s, 16))
      >>> parser.add_argument('--foo', type='hexadecimal integer')
      _StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type='hexadecimal integer', choices=None, required=False, help=None, metavar=None, deprecated=False)
      >>> parser.parse_args(['--foo', '0xFA'])
      Namespace(foo=250)
      >>> parser.parse_args(['--foo', '1.2'])
      usage: PROG [-h] [--foo FOO]
      PROG: error: argument --foo: invalid 'hexadecimal integer' value: '1.2'


Exceções
========

exception argparse.ArgumentError

   Um erro ao criar ou usar um argumento (opcional ou posicional).

   O valor da string dessa exceção é a mensagem, complementada com
   informações sobre o argumento que a causou.

exception argparse.ArgumentTypeError

   Levantada quando algo dá errado ao converter uma string de linha de
   comando em um tipo.

-[ Guias e tutoriais ]-

* Tutorial de Argparse

* Migrando código "optparse" para "argparse"
