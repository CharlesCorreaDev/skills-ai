"optparse" --- Analisador sintático para opções de linha de comando
*******************************************************************

**Código-fonte:** Lib/optparse.py

======================================================================


Escolhendo uma biblioteca de análise de linha de comando
========================================================

A biblioteca padrão inclui três bibliotecas de análise de argumentos:

* "getopt": a module that closely mirrors the procedural C "getopt"
  API.

* "optparse": a declarative replacement for "getopt" that provides
  equivalent functionality without requiring each application to
  implement its own procedural option parsing logic.

* "argparse": a more opinionated alternative to "optparse" that
  provides more functionality by default, at the expense of reduced
  application flexibility in controlling exactly how arguments are
  processed.

Na ausência de restrições de design de análise de argumentos mais
específicas, "argparse" é a escolha recomendada para implementar
aplicações de linha de comando, pois oferece o mais alto nível de
funcionalidade básica com o mínimo de código em nível de aplicação.

"getopt" é mantido quase inteiramente por razões de
retrocompatibilidade. No entanto, ele também serve como um caso de uso
de nicho como uma ferramenta para prototipagem e teste de manipulação
de argumentos de linha de comando em aplicações C baseadas em
"getopt".

"optparse" should be considered as an alternative to "argparse" in the
following cases:

* an application is already using "optparse" and doesn't want to risk
  the subtle behavioural changes that may arise when migrating to
  "argparse"

* a aplicação requer controle adicional sobre a maneira como as opções
  e os parâmetros posicionais são intercalados na linha de comando
  (incluindo a capacidade de desabilitar completamente o recurso de
  intercalação)

* a aplicação requer controle adicional sobre a análise incremental de
  elementos de linha de comando (embora "argparse" suporte isso, a
  maneira exata como ele funciona na prática é indesejável para alguns
  casos de uso)

* a aplicação requer controle adicional sobre o tratamento de opções
  que aceitam valores de parâmetros que podem começar com "-" (como
  opções delegadas a serem passadas para subprocessos invocados)

* a aplicação requer algum outro comportamento de processamento de
  parâmetros de linha de comando que "argparse" não suporta, mas que
  pode ser implementado em termos da interface de nível inferior
  oferecida por "optparse"

These considerations also mean that "optparse" is likely to provide a
better foundation for library authors writing third party command line
argument processing libraries.

Como exemplo concreto, considere as duas configurações de análise de
argumentos de linha de comando a seguir, a primeira usando "optparse"
e a segunda usando "argparse":

   import optparse

   if __name__ == '__main__':
       parser = optparse.OptionParser()
       parser.add_option('-o', '--output')
       parser.add_option('-v', dest='verbose', action='store_true')
       opts, args = parser.parse_args()
       process(args, output=opts.output, verbose=opts.verbose)

   import argparse

   if __name__ == '__main__':
       parser = argparse.ArgumentParser()
       parser.add_argument('-o', '--output')
       parser.add_argument('-v', dest='verbose', action='store_true')
       parser.add_argument('rest', nargs='*')
       args = parser.parse_args()
       process(args.rest, output=args.output, verbose=args.verbose)

A diferença mais óbvia é que na versão "optparse", os argumentos não
opcionais são processados separadamente pelo aplicativo após o
processamento da opção ser concluído. Na versão "argparse", os
argumentos posicionais são declarados e processados da mesma forma que
as opções nomeadas.

No entanto, a versão "argparse" também manipulará algumas combinações
de parâmetros de forma diferente da forma como a versão "optparse" as
manipularia. Por exemplo (entre outras diferenças):

* fornecer "-o -v" retorna "output="-v"" e "verbose=False" ao usar
  "optparse", mas um erro de uso com "argparse" (reclamando que nenhum
  valor foi fornecido para "-o/--output", já que "-v" é interpretado
  como significando o sinalizador de verbosidade)

* da mesma forma, fornecer "-o --" retorna "output="--"" e "args=()"
  ao usar "optparse", mas um erro de uso com "argparse" (também
  reclamando que nenhum valor foi fornecido para "-o/--output", já que
  "--" é interpretado como o término do processamento da opção e o
  tratamento de todos os valores restantes como argumentos
  posicionais)

* fornecer "-o=foo" retorna "output="=foo"" ao usar "optparse", mas
  retorna "output="foo"" com "argparse" (já que "=" é um caso especial
  como um separador alternativo para valores de parâmetros de opção)

Se esses comportamentos diferentes na versão "argparse" são
considerados desejáveis ou um problema dependerá do caso de uso
específico da aplicação de linha de comando.

Ver também:

  click é uma biblioteca de processamento de argumentos de terceiros
  (originalmente baseada em "optparse"), que permite que aplicações de
  linha de comando sejam desenvolvidas como um conjunto de funções de
  implementação de comando decoradas.

  Outras bibliotecas de terceiros, como typer ou msgspec-click,
  permitem que interfaces de linha de comando sejam especificadas de
  maneiras que se integrem de forma mais eficaz com a verificação
  estática de anotações de tipo Python.


Introdução
==========

"optparse" is a more convenient, flexible, and powerful library for
parsing command-line options than the minimalist "getopt" module.
"optparse" uses a more declarative style of command-line parsing: you
create an instance of "OptionParser", populate it with options, and
parse the command line. "optparse" allows users to specify options in
the conventional GNU/POSIX syntax, and additionally generates usage
and help messages for you.

Here's an example of using "optparse" in a simple script:

   from optparse import OptionParser
   ...
   parser = OptionParser()
   parser.add_option("-f", "--file", dest="filename",
                     help="write report to FILE", metavar="FILE")
   parser.add_option("-q", "--quiet",
                     action="store_false", dest="verbose", default=True,
                     help="don't print status messages to stdout")

   (options, args) = parser.parse_args()

Com essas poucas linhas de código, os usuários do seu script agora
podem fazer "coisas comuns" na linha de comando, por exemplo:

   <seuscript> --file=outfile -q

As it parses the command line, "optparse" sets attributes of the
"options" object returned by "parse_args()" based on user-supplied
command-line values.  When "parse_args()" returns from parsing this
command line, "options.filename" will be ""outfile"" and
"options.verbose" will be "False".  "optparse" supports both long and
short options, allows short options to be merged together, and allows
options to be associated with their arguments in a variety of ways.
Thus, the following command lines are all equivalent to the above
example:

   <seuscript> -f outfile --quiet
   <seuscript> --quiet --file outfile
   <seuscript> -q -foutfile
   <seuscript> -qfoutfile

Além disso, os usuários podem executar um dos seguintes:

   <seuscript> -h
   <seuscript> --help

and "optparse" will print out a brief summary of your script's
options:

   Usage: <seuscript> [options]

   Options:
     -h, --help            show this help message and exit
     -f FILE, --file=FILE  write report to FILE
     -q, --quiet           don't print status messages to stdout

onde o valor de *seuscript* é determinado em tempo de execução
(normalmente de "sys.argv[0]").


Contexto
========

"optparse" was explicitly designed to encourage the creation of
programs with straightforward command-line interfaces that follow the
conventions established by the "getopt()" family of functions
available to C developers. To that end, it supports only the most
common command-line syntax and semantics conventionally used under
Unix.  If you are unfamiliar with these conventions, reading this
section will allow you to acquaint yourself with them.


Terminologia
------------

argumento
   uma string inserida na linha de comando e passada pelo shell para
   "execl()" ou "execv()". Em Python, argumentos são elementos de
   "sys.argv[1:]" ("sys.argv[0]" é o nome do programa que está sendo
   executado). Shells Unix também usam o termo "word".

   Ocasionalmente, é desejável substituir uma lista de argumentos
   diferente de "sys.argv[1:]", então você deve ler "argumento" como
   "um elemento de "sys.argv[1:]", ou de alguma outra lista fornecida
   como um substituto para "sys.argv[1:]"".

opção
   an argument used to supply extra information to guide or customize
   the execution of a program.  There are many different syntaxes for
   options; the traditional Unix syntax is a hyphen ("-") followed by
   a single letter, e.g. "-x" or "-F".  Also, traditional Unix syntax
   allows multiple options to be merged into a single argument, e.g.
   "-x -F" is equivalent to "-xF".  The GNU project introduced "--"
   followed by a series of hyphen-separated words, e.g. "--file" or "
   --dry-run".  These are the only two option syntaxes provided by
   "optparse".

   Algumas outras sintaxes de opções que o mundo viu incluem:

   * um hífen seguido por algumas letras, por exemplo "-pf" (isso
     *não* é o mesmo que várias opções mescladas em um único
     argumento)

   * um hífen seguido por uma palavra completa, por exemplo "-file"
     (isso é tecnicamente equivalente à sintaxe anterior, mas eles
     geralmente não são vistos no mesmo programa)

   * um sinal de mais seguido por uma única letra, ou algumas letras,
     ou uma palavra, por exemplo "+f", "+rgb"

   * uma barra seguida de uma letra, ou algumas letras, ou uma
     palavra, por exemplo "/f", "/file"

   These option syntaxes are not supported by "optparse", and they
   never will be.  This is deliberate: the first three are non-
   standard on any environment, and the last only makes sense if
   you're exclusively targeting Windows or certain legacy platforms
   (e.g. VMS, MS-DOS).

argumento de opção
   an argument that follows an option, is closely associated with that
   option, and is consumed from the argument list when that option is.
   With "optparse", option arguments may either be in a separate
   argument from their option:

      -f foo
      --file foo

   ou incluídos no mesmo argumento:

      -ffoo
      --file=foo

   Typically, a given option either takes an argument or it doesn't.
   Lots of people want an "optional option arguments" feature, meaning
   that some options will take an argument if they see it, and won't
   if they don't.  This is somewhat controversial, because it makes
   parsing ambiguous: if "-a" takes an optional argument and "-b" is
   another option entirely, how do we interpret "-ab"?  Because of
   this ambiguity, "optparse" does not support this feature.

argumento posicional
   algo que sobrou na lista de argumentos depois que as opções foram
   analisadas, ou seja, depois que as opções e seus argumentos foram
   analisados e removidos da lista de argumentos.

opção obrigatória
   an option that must be supplied on the command-line; note that the
   phrase "required option" is self-contradictory in English.
   "optparse" doesn't prevent you from implementing required options,
   but doesn't give you much help at it either.

Por exemplo, considere esta linha de comando hipotética:

   prog -v --report report.txt foo bar

"-v" e "--report" são ambas opções. Supondo que "--report" receba um
argumento, "report.txt" é um argumento de opção. "foo" e "bar" são
argumentos posicionais.


Para que servem as opções?
--------------------------

As opções são usadas para fornecer informações extras para ajustar ou
personalizar a execução de um programa. Caso não tenha ficado claro,
as opções geralmente são *opcionais*. Um programa deve ser capaz de
executar muito bem sem nenhuma opção. (Escolha um programa aleatório
dos conjuntos de ferramentas Unix ou GNU. Ele pode ser executado sem
nenhuma opção e ainda fazer sentido? As principais exceções são
"find", "tar" e "dd" --- todos eles são mutantes excêntricos que foram
corretamente criticados por sua sintaxe não padrão e interfaces
confusas.)

Muitas pessoas querem que seus programas tenham "opções obrigatórias".
Pense nisso. Se é obrigatório, então *não é opcional*! Se há uma
informação que seu programa absolutamente requer para ser executado
com sucesso, é para isso que servem os argumentos posicionais.

Como um exemplo de bom design de interface de linha de comando,
considere o humilde utilitário "cp", para copiar arquivos. Não faz
muito sentido tentar copiar arquivos sem fornecer um destino e pelo
menos uma fonte. Portanto, "cp" falha se você executá-lo sem
argumentos. No entanto, ele tem uma sintaxe flexível e útil que não
requer nenhuma opção:

   cp ORIGEM DESTINO
   cp ORIGEM ... DIRETÓRIO

Você pode ir bem longe só com isso. A maioria das implementações de
"cp" fornece um monte de opções para ajustar exatamente como os
arquivos são copiados: você pode preservar o modo e o tempo de
modificação, evitar seguir links simbólicos, perguntar antes de
destruir arquivos existentes, etc. Mas nada disso distrai da missão
principal de "cp", que é copiar um arquivo para outro, ou vários
arquivos para outro diretório.


Para que servem os argumentos posicionais?
------------------------------------------

Argumentos posicionais são para aquelas informações que seu programa
absolutamente e positivamente requer para ser executado.

Uma boa interface de usuário deve ter o mínimo de requisitos absolutos
possível. Se seu programa requer 17 informações distintas para ser
executado com sucesso, não importa muito *como* você obtém essas
informações do usuário --- a maioria das pessoas desistirá e irá
embora antes de executar o programa com sucesso. Isso se aplica se a
interface de usuário for uma linha de comando, um arquivo de
configuração ou uma GUI: se você fizer tantas exigências aos seus
usuários, a maioria deles simplesmente desistirá.

Em resumo, tente minimizar a quantidade de informações que os usuários
são absolutamente obrigados a fornecer --- use padrões sensatos sempre
que possível. Claro, você também quer tornar seus programas
razoavelmente flexíveis. É para isso que servem as opções. Novamente,
não importa se são entradas em um arquivo de configuração, widgets no
diálogo "Preferências" de uma GUI ou opções de linha de comando ---
quanto mais opções você implementar, mais flexível será seu programa e
mais complicada se tornará sua implementação. Muita flexibilidade
também tem desvantagens, é claro; muitas opções podem sobrecarregar os
usuários e tornar seu código muito mais difícil de manter.


Tutorial
========

While "optparse" is quite flexible and powerful, it's also
straightforward to use in most cases.  This section covers the code
patterns that are common to any "optparse"-based program.

Primeiro, você precisa importar a classe OptionParser; então, no
início do programa principal, crie uma instância de OptionParser:

   from optparse import OptionParser
   ...
   parser = OptionParser()

Então você pode começar a definir opções. A sintaxe básica é:

   parser.add_option(opt_str, ...,
                     attr=value, ...)

Each option has one or more option strings, such as "-f" or "--file",
and several option attributes that tell "optparse" what to expect and
what to do when it encounters that option on the command line.

Normalmente, cada opção terá uma sequência de opções curta e uma
sequência de opções longa, por exemplo:

   parser.add_option("-f", "--file", ...)

Você tem a liberdade de definir quantas strings de opções curtas e
longas quiser (incluindo zero), desde que haja pelo menos uma string
de opção no geral.

The option strings passed to "OptionParser.add_option()" are
effectively labels for the option defined by that call.  For brevity,
we will frequently refer to *encountering an option* on the command
line; in reality, "optparse" encounters *option strings* and looks up
options from them.

Once all of your options are defined, instruct "optparse" to parse
your program's command line:

   (options, args) = parser.parse_args()

(Se desejar, você pode passar uma lista de argumentos personalizada
para "parse_args()", mas isso raramente é necessário: por padrão, ele
usa "sys.argv[1:]".)

"parse_args()" retorna dois valores:

* "options", um objeto que contém valores para todas as suas opções
  --- por exemplo, se "--file" receber um único argumento de string,
  então "options.file" será o nome do arquivo fornecido pelo usuário,
  ou "None" se o usuário não forneceu essa opção

* "args", a lista de argumentos posicionais restantes após a análise
  de opções

Esta seção do tutorial abrange apenas os quatro atributos de opção
mais importantes: "action", "type", "dest" (destino) e "help". Destes,
"action" é o mais fundamental.


Compreendendo as ações de opções
--------------------------------

Actions tell "optparse" what to do when it encounters an option on the
command line.  There is a fixed set of actions hard-coded into
"optparse"; adding new actions is an advanced topic covered in section
Extending optparse.  Most actions tell "optparse" to store a value in
some variable---for example, take a string from the command line and
store it in an attribute of "options".

If you don't specify an option action, "optparse" defaults to "store".


A ação store
------------

The most common option action is "store", which tells "optparse" to
take the next argument (or the remainder of the current argument),
ensure that it is of the correct type, and store it to your chosen
destination.

Por exemplo:

   parser.add_option("-f", "--file",
                     action="store", type="string", dest="filename")

Now let's make up a fake command line and ask "optparse" to parse it:

   args = ["-f", "foo.txt"]
   (options, args) = parser.parse_args(args)

When "optparse" sees the option string "-f", it consumes the next
argument, "foo.txt", and stores it in "options.filename".  So, after
this call to "parse_args()", "options.filename" is ""foo.txt"".

Some other option types supported by "optparse" are "int" and "float".
Here's an option that expects an integer argument:

   parser.add_option("-n", type="int", dest="num")

Note que esta opção não tem uma string de opção longa, o que é
perfeitamente aceitável. Além disso, não há nenhuma ação explícita, já
que o padrão é "store".

Vamos analisar outra linha de comando falsa. Desta vez, vamos colocar
o argumento de opção bem perto da opção: já que "-n42" (um argumento)
equivale a "-n 42" (dois argumentos), o código

   (options, args) = parser.parse_args(["-n42"])
   print(options.num)

vai exibir "42".

If you don't specify a type, "optparse" assumes "string".  Combined
with the fact that the default action is "store", that means our first
example can be a lot shorter:

   parser.add_option("-f", "--file", dest="filename")

If you don't supply a destination, "optparse" figures out a sensible
default from the option strings: if the first long option string is "
--foo-bar", then the default destination is "foo_bar".  If there are
no long option strings, "optparse" looks at the first short option
string: the default destination for "-f" is "f".

"optparse" also includes the built-in "complex" type.  Adding types is
covered in section Extending optparse.


Manipulando opções (sinalizadores) booleanas
--------------------------------------------

Flag options---set a variable to true or false when a particular
option is seen---are quite common.  "optparse" supports them with two
separate actions, "store_true" and "store_false".  For example, you
might have a "verbose" flag that is turned on with "-v" and off with
"-q":

   parser.add_option("-v", action="store_true", dest="verbose")
   parser.add_option("-q", action="store_false", dest="verbose")

Aqui temos duas opções diferentes com o mesmo destino, o que é
perfeitamente OK. (Isso significa apenas que você tem que ter um pouco
de cuidado ao definir valores padrão — veja abaixo.)

When "optparse" encounters "-v" on the command line, it sets
"options.verbose" to "True"; when it encounters "-q",
"options.verbose" is set to "False".


Outras ações
------------

Some other actions supported by "optparse" are:

""store_const""
   armazena um valor constante, predefinido via "Option.const"

""append""
   anexa o argumento desta opção a uma lista

""count""
   incrementa um contador em um

""callback""
   chama uma função especificada

Elas são abordadas na seção Guia de referência e na seção Funções de
retorno de opção.


Valores padrão
--------------

All of the above examples involve setting some variable (the
"destination") when certain command-line options are seen.  What
happens if those options are never seen?  Since we didn't supply any
defaults, they are all set to "None".  This is usually fine, but
sometimes you want more control.  "optparse" lets you supply a default
value for each destination, which is assigned before the command line
is parsed.

First, consider the verbose/quiet example.  If we want "optparse" to
set "verbose" to "True" unless "-q" is seen, then we can do this:

   parser.add_option("-v", action="store_true", dest="verbose", default=True)
   parser.add_option("-q", action="store_false", dest="verbose")

Como os valores padrão se aplicam ao *destino* e não a qualquer opção
específica, e essas duas opções têm o mesmo destino, isso é exatamente
equivalente:

   parser.add_option("-v", action="store_true", dest="verbose")
   parser.add_option("-q", action="store_false", dest="verbose", default=True)

Considere isso:

   parser.add_option("-v", action="store_true", dest="verbose", default=False)
   parser.add_option("-q", action="store_false", dest="verbose", default=True)

Novamente, o valor padrão para "verbose" será "True": o último valor
padrão fornecido para qualquer destino específico é o que conta.

Uma maneira mais clara de especificar valores padrão é o método
"set_defaults()" do OptionParser, que você pode chamar a qualquer
momento antes de chamar "parse_args()":

   parser.set_defaults(verbose=True)
   parser.add_option(...)
   (options, args) = parser.parse_args()

Como antes, o último valor especificado para um destino de opção dado
é o que conta. Para maior clareza, tente usar um método ou outro de
configuração de valores padrão, não ambos.


Gerando texto de ajuda
----------------------

"optparse"'s ability to generate help and usage text automatically is
useful for creating user-friendly command-line interfaces.  All you
have to do is supply a "help" value for each option, and optionally a
short usage message for your whole program.  Here's an OptionParser
populated with user-friendly (documented) options:

   usage = "usage: %prog [options] arg1 arg2"
   parser = OptionParser(usage=usage)
   parser.add_option("-v", "--verbose",
                     action="store_true", dest="verbose", default=True,
                     help="make lots of noise [default]")
   parser.add_option("-q", "--quiet",
                     action="store_false", dest="verbose",
                     help="be vewwy quiet (I'm hunting wabbits)")
   parser.add_option("-f", "--filename",
                     metavar="FILE", help="write output to FILE")
   parser.add_option("-m", "--mode",
                     default="intermediate",
                     help="interaction mode: novice, intermediate, "
                          "or expert [default: %default]")

If "optparse" encounters either "-h" or "--help" on the command-line,
or if you just call "parser.print_help()", it prints the following to
standard output:

   Usage: <yourscript> [options] arg1 arg2

   Options:
     -h, --help            show this help message and exit
     -v, --verbose         make lots of noise [default]
     -q, --quiet           be vewwy quiet (I'm hunting wabbits)
     -f FILE, --filename=FILE
                           write output to FILE
     -m MODE, --mode=MODE  interaction mode: novice, intermediate, or
                           expert [default: intermediate]

(If the help output is triggered by a help option, "optparse" exits
after printing the help text.)

There's a lot going on here to help "optparse" generate the best
possible help message:

* o script define sua própria mensagem de uso:

     usage = "usage: %prog [options] arg1 arg2"

  "optparse" expands "%prog" in the usage string to the name of the
  current program, i.e. "os.path.basename(sys.argv[0])".  The expanded
  string is then printed before the detailed option help.

  If you don't supply a usage string, "optparse" uses a bland but
  sensible default: ""Usage: %prog [options]"", which is fine if your
  script doesn't take any positional arguments.

* every option defines a help string, and doesn't worry about line-
  wrapping---"optparse" takes care of wrapping lines and making the
  help output look good.

* opções que assumem um valor indicam esse fato em sua mensagem de
  ajuda gerada automaticamente, por exemplo, para a opção "mode":

     -m MODE, --mode=MODE

  Here, "MODE" is called the meta-variable: it stands for the argument
  that the user is expected to supply to "-m"/"--mode".  By default,
  "optparse" converts the destination variable name to uppercase and
  uses that for the meta-variable.  Sometimes, that's not what you
  want---for example, the "--filename" option explicitly sets
  "metavar="FILE"", resulting in this automatically generated option
  description:

     -f FILE, --filename=FILE

  Isso é importante para mais do que apenas economizar espaço: o texto
  de ajuda escrito manualmente usa a metavariável "FILE" para dar uma
  pista ao usuário de que há uma conexão entre a sintaxe semiformal
  "-f FILE" e a descrição semântica informal como, por exemplo, "write
  output to FILE". Essa é uma maneira simples, mas eficaz, de tornar
  seu texto de ajuda muito mais claro e útil para usuários finais.

* options that have a default value can include "%default" in the help
  string---"optparse" will replace it with "str()" of the option's
  default value.  If an option has no default value (or the default
  value is "None"), "%default" expands to "none".


Agrupando opções
~~~~~~~~~~~~~~~~

Ao lidar com muitas opções, é conveniente agrupar essas opções para
melhor saída de ajuda. Um "OptionParser" pode conter vários grupos de
opções, cada um dos quais pode conter várias opções.

Um grupo de opções é obtido usando a classe "OptionGroup":

class optparse.OptionGroup(parser, title, description=None)

   onde

   * *parser* é a instância "OptionParser" na qual o grupo será
     inserido

   * *title* é o título do grupo

   * *description*, opcional, é uma descrição longa do grupo

"OptionGroup" herda de "OptionContainer" (como "OptionParser") e,
portanto, o método "add_option()" pode ser usado para adicionar uma
opção ao grupo.

Depois que todas as opções são declaradas, usando o método
"OptionParser" "add_option_group()" o grupo é adicionado ao analisador
definido anteriormente.

Continuando com o analisador definido na seção anterior, adicionar um
"OptionGroup" a um analisador é fácil:

   group = OptionGroup(parser, "Dangerous Options",
                       "Caution: use these options at your own risk.  "
                       "It is believed that some of them bite.")
   group.add_option("-g", action="store_true", help="Group option.")
   parser.add_option_group(group)

Isso resultaria na seguinte saída de texto de ajuda:

   Usage: <yourscript> [options] arg1 arg2

   Options:
     -h, --help            show this help message and exit
     -v, --verbose         make lots of noise [default]
     -q, --quiet           be vewwy quiet (I'm hunting wabbits)
     -f FILE, --filename=FILE
                           write output to FILE
     -m MODE, --mode=MODE  interaction mode: novice, intermediate, or
                           expert [default: intermediate]

     Dangerous Options:
       Caution: use these options at your own risk.  It is believed that some
       of them bite.

       -g                  Group option.

Um exemplo um pouco mais completo pode envolver o uso de mais de um
grupo: ainda estendendo o exemplo anterior:

   group = OptionGroup(parser, "Dangerous Options",
                       "Caution: use these options at your own risk.  "
                       "It is believed that some of them bite.")
   group.add_option("-g", action="store_true", help="Group option.")
   parser.add_option_group(group)

   group = OptionGroup(parser, "Debug Options")
   group.add_option("-d", "--debug", action="store_true",
                    help="Print debug information")
   group.add_option("-s", "--sql", action="store_true",
                    help="Print all SQL statements executed")
   group.add_option("-e", action="store_true", help="Print every action done")
   parser.add_option_group(group)

que resulta na seguinte saída:

   Usage: <yourscript> [options] arg1 arg2

   Options:
     -h, --help            show this help message and exit
     -v, --verbose         make lots of noise [default]
     -q, --quiet           be vewwy quiet (I'm hunting wabbits)
     -f FILE, --filename=FILE
                           write output to FILE
     -m MODE, --mode=MODE  interaction mode: novice, intermediate, or expert
                           [default: intermediate]

     Dangerous Options:
       Caution: use these options at your own risk.  It is believed that some
       of them bite.

       -g                  Group option.

     Debug Options:
       -d, --debug         Print debug information
       -s, --sql           Print all SQL statements executed
       -e                  Print every action done

Outro método interessante, especialmente ao trabalhar
programaticamente com grupos de opções, é:

OptionParser.get_option_group(opt_str)

   Retorna o objeto "OptionGroup" ao qual a string de opção curta ou
   longa *opt_str* (por exemplo, "'-o'" ou "'--option'") pertence. Se
   não houver tal "OptionGroup", retorna "None".


Exibindo uma string de versão
-----------------------------

Similar to the brief usage string, "optparse" can also print a version
string for your program.  You have to supply the string as the
"version" argument to OptionParser:

   parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")

"%prog" is expanded just like it is in "usage".  Apart from that,
"version" can contain anything you like.  When you supply it,
"optparse" automatically adds a "--version" option to your parser. If
it encounters this option on the command line, it expands your
"version" string (by replacing "%prog"), prints it to stdout, and
exits.

Por exemplo, se o seu script for chamado "/usr/bin/foo":

   $ /usr/bin/foo --version
   foo 1.0

Os dois métodos a seguir podem ser usados para exibir e obter a string
"version":

OptionParser.print_version(file=None)

   Exibe a mensagem de versão para o programa atual ("self.version")
   em *file* (stdout padrão). Assim como em "print_usage()", qualquer
   ocorrência de "%prog" em "self.version" é substituída pelo nome do
   programa atual. Não faz nada se "self.version" estiver vazio ou
   indefinido.

OptionParser.get_version()

   O mesmo que "print_version()", mas retorna a string da versão em
   vez de exibi-la.


How "optparse" handles errors
-----------------------------

There are two broad classes of errors that "optparse" has to worry
about: programmer errors and user errors.  Programmer errors are
usually erroneous calls to "OptionParser.add_option()", e.g. invalid
option strings, unknown option attributes, missing option attributes,
etc.  These are dealt with in the usual way: raise an exception
(either "optparse.OptionError" or "TypeError") and let the program
crash.

Handling user errors is much more important, since they are guaranteed
to happen no matter how stable your code is.  "optparse" can
automatically detect some user errors, such as bad option arguments
(passing "-n 4x" where "-n" takes an integer argument), missing
arguments ("-n" at the end of the command line, where "-n" takes an
argument of any type).  Also, you can call "OptionParser.error()" to
signal an application-defined error condition:

   (options, args) = parser.parse_args()
   ...
   if options.a and options.b:
       parser.error("options -a and -b are mutually exclusive")

In either case, "optparse" handles the error the same way: it prints
the program's usage message and an error message to standard error and
exits with error status 2.

Considere o primeiro exemplo acima, onde o usuário passa "4x" para uma
opção que aceita um inteiro:

   $ /usr/bin/foo -n 4x
   Usage: foo [options]

   foo: error: option -n: invalid integer value: '4x'

Ou, quando o usuário não passa nenhum valor:

   $ /usr/bin/foo -n
   Usage: foo [options]

   foo: error: -n option requires an argument

"optparse"-generated error messages take care always to mention the
option involved in the error; be sure to do the same when calling
"OptionParser.error()" from your application code.

If "optparse"'s default error-handling behaviour does not suit your
needs, you'll need to subclass OptionParser and override its "exit()"
and/or "error()" methods.


Juntando tudo
-------------

Here's what "optparse"-based scripts usually look like:

   from optparse import OptionParser
   ...
   def main():
       usage = "usage: %prog [options] arg"
       parser = OptionParser(usage)
       parser.add_option("-f", "--file", dest="filename",
                         help="read data from FILENAME")
       parser.add_option("-v", "--verbose",
                         action="store_true", dest="verbose")
       parser.add_option("-q", "--quiet",
                         action="store_false", dest="verbose")
       ...
       (options, args) = parser.parse_args()
       if len(args) != 1:
           parser.error("incorrect number of arguments")
       if options.verbose:
           print("reading %s..." % options.filename)
       ...

   if __name__ == "__main__":
       main()


Guia de referência
==================


Criando o analisador sintático
------------------------------

The first step in using "optparse" is to create an OptionParser
instance.

class optparse.OptionParser(...)

   O construtor do OptionParser não tem argumentos obrigatórios, mas
   vários argumentos nomeados opcionais. Você deve sempre passá-los
   como argumentos nomeados, ou seja, não confie na ordem em que os
   argumentos são declarados.

   "usage" (padrão: ""%prog [options]"")
      The usage summary to print when your program is run incorrectly
      or with a help option.  When "optparse" prints the usage string,
      it expands "%prog" to "os.path.basename(sys.argv[0])" (or to
      "prog" if you passed that keyword argument).  To suppress a
      usage message, pass the special value "optparse.SUPPRESS_USAGE".

   "option_list" (padrão: "[]")
      Uma lista de objetos Option para preencher o analisador
      sintático. As opções em "option_list" são adicionadas após
      quaisquer opções em "standard_option_list" (um atributo de
      classe que pode ser definido por subclasses de OptionParser),
      mas antes de quaisquer opções de versão ou ajuda. Descontinuado;
      use "add_option()" após criar o analisador sintático.

   "option_class" (padrão: optparse.Option)
      Classe para usar ao adicionar opções ao analisador sintático em
      "add_option()".

   "version" (padrão: "None")
      A version string to print when the user supplies a version
      option. If you supply a true value for "version", "optparse"
      automatically adds a version option with the single option
      string "--version".  The substring "%prog" is expanded the same
      as for "usage".

   "conflict_handler" (padrão: ""error"")
      Especifica o que fazer quando opções com strings de opções
      conflitantes são adicionadas ao analisador sintático; consulte a
      seção Conflitos entre opções.

   "description" (padrão: "None")
      A paragraph of text giving a brief overview of your program.
      "optparse" reformats this paragraph to fit the current terminal
      width and prints it when the user requests help (after "usage",
      but before the list of options).

   "formatter" (padrão: um novo "IndentedHelpFormatter")
      An instance of optparse.HelpFormatter that will be used for
      printing help text.  "optparse" provides two concrete classes
      for this purpose: IndentedHelpFormatter and TitledHelpFormatter.

   "add_help_option" (padrão: "True")
      If true, "optparse" will add a help option (with option strings
      "-h" and "--help") to the parser.

   "prog"
      A string a ser usada ao expandir "%prog" em "usage" e "version"
      em vez de "os.path.basename(sys.argv[0])".

   "epilog" (padrão: "None")
      Um parágrafo de texto de ajuda para exibir após a ajuda da
      opção.


Preenchendo o analisador sintático
----------------------------------

Há várias maneiras de preencher o analisador sintático com opções. A
maneira preferida é usando "OptionParser.add_option()", como mostrado
na seção Tutorial. "add_option()" pode ser chamado de uma das duas
maneiras:

* passar uma instância de Option (conforme retornado por
  "make_option()")

* passar qualquer combinação de argumentos nomeados e posicionais que
  sejam aceitáveis para "make_option()" (ou seja, para o construtor de
  Option), e ela criará a instância de Option para você

A outra alternativa é passar uma lista de instâncias de Option
pré-construídas para o construtor de OptionParser, como em:

   option_list = [
       make_option("-f", "--filename",
                   action="store", type="string", dest="filename"),
       make_option("-q", "--quiet",
                   action="store_false", dest="verbose"),
       ]
   parser = OptionParser(option_list=option_list)

("make_option()" is a factory function for creating Option instances;
currently it is an alias for the Option constructor.  A future version
of "optparse" may split Option into several classes, and
"make_option()" will pick the right class to instantiate.  Do not
instantiate Option directly.)


Definindo as opções
-------------------

Cada instância de Option representa um conjunto de strings de opções
de linha de comando sinônimas, por exemplo, "-f" e "--file". Você pode
especificar qualquer número de strings de opções curtas ou longas, mas
deve especificar pelo menos uma string de opção geral.

A maneira canônica de criar uma instância de "Option" é com o método
"add_option()" de "OptionParser".

OptionParser.add_option(option)
OptionParser.add_option(*opt_str, attr=value, ...)

   Para definir uma opção com apenas uma sequência de opções curta:

      parser.add_option("-f", attr=value, ...)

   E para definir uma opção com apenas uma longa sequência de opções:

      parser.add_option("--foo", attr=value, ...)

   The keyword arguments define attributes of the new Option object.
   The most important option attribute is "action", and it largely
   determines which other attributes are relevant or required.  If you
   pass irrelevant option attributes, or fail to pass required ones,
   "optparse" raises an "OptionError" exception explaining your
   mistake.

   An option's *action* determines what "optparse" does when it
   encounters this option on the command-line.  The standard option
   actions hard-coded into "optparse" are:

   ""store""
      armazena o argumento desta opção (padrão)

   ""store_const""
      armazena um valor constante, predefinido via "Option.const"

   ""store_true""
      armazena "True"

   ""store_false""
      armazena "False"

   ""append""
      anexa o argumento desta opção a uma lista

   ""append_const""
      anexar um valor constante a uma lista, predefinido via
      "Option.const"

   ""count""
      incrementa um contador em um

   ""callback""
      chama uma função especificada

   ""help""
      exibe uma mensagem de uso incluindo todas as opções e a
      documentação para elas

   (Se você não fornecer uma ação, o padrão é ""store"". Para esta
   ação, você também pode fornecer os atributos de opção "type" e
   "dest"; consulte Ações de opção padrão.)

As you can see, most actions involve storing or updating a value
somewhere. "optparse" always creates a special object for this,
conventionally called "options", which is an instance of
"optparse.Values".

class optparse.Values

   Um objeto que contém nomes e valores de argumentos analisados como
   atributos. Normalmente criado chamando ao chamar
   "OptionParser.parse_args()", e pode ser substituído por uma
   subclasse personalizada passada para o argumento *values* de
   "OptionParser.parse_args()" (conforme descrito em Análise de
   argumentos).

Argumentos de opção (e vários outros valores) são armazenados como
atributos deste objeto, de acordo com o atributo de opção "dest"
(destino).

Por exemplo, quando você chama

   parser.parse_args()

one of the first things "optparse" does is create the "options"
object:

   options = Values()

Se uma das opções neste analisador sintático for definida com

   parser.add_option("-f", "--file", action="store", type="string", dest="filename")

e a linha de comando que está sendo analisada inclui qualquer um dos
seguintes:

   -ffoo
   -f foo
   --file=foo
   --file foo

then "optparse", on seeing this option, will do the equivalent of

   options.filename = "foo"

Os atributos de opção "type" e "dest" são quase tão importantes quanto
"action", mas "action" é o único que faz sentido para *todas* as
opções.


Atributos da classe Option
--------------------------

class optparse.Option

   Um único argumento de linha de comando, com vários atributos
   passados como nomeados para o construtor. Normalmente criado com
   "OptionParser.add_option()" em vez de diretamente, e pode ser
   substituído por uma classe personalizada por meio do argumento
   *option_class* para "OptionParser".

The following option attributes may be passed as keyword arguments to
"OptionParser.add_option()".  If you pass an option attribute that is
not relevant to a particular option, or fail to pass a required option
attribute, "optparse" raises "OptionError".

Option.action

   (padrão: ""store"")

   Determines "optparse"'s behaviour when this option is seen on the
   command line; the available options are documented here.

Option.type

   (padrão: ""string"")

   O tipo de argumento esperado por esta opção (por exemplo,
   ""string"" ou ""int""); os tipos de opções disponíveis estão
   documentados aqui.

Option.dest

   (padrão: derivado de strings de opção)

   If the option's action implies writing or modifying a value
   somewhere, this tells "optparse" where to write it: "dest" names an
   attribute of the "options" object that "optparse" builds as it
   parses the command line.

Option.default

   O valor para usar para o destino desta opção se a opção não for
   vista na linha de comando. Veja também
   "OptionParser.set_defaults()".

Option.nargs

   (padrão: 1)

   How many arguments of type "type" should be consumed when this
   option is seen.  If > 1, "optparse" will store a tuple of values to
   "dest".

Option.const

   Para ações que armazenam um valor constante, o valor constante a
   ser armazenado.

Option.choices

   Para opções do tipo ""choice"", a lista de strings que o usuário
   pode escolher.

Option.callback

   Para opções com ação ""callback"", o chamável para chamar quando
   esta opção for vista. Veja a seção Funções de retorno de opção para
   detalhes sobre os argumentos passados para o chamável.

Option.callback_args
Option.callback_kwargs

   Argumentos nomeados e posicionais adicionais para passar para
   "callback" após os quatro argumentos de retorno de chamada padrão.

Option.help

   Texto de ajuda para exibir para esta opção ao listar todas as
   opções disponíveis após o usuário fornecer uma opção "help" (como "
   --help"). Se nenhum texto de ajuda for fornecido, a opção será
   listada sem texto de ajuda. Para ocultar esta opção, use o valor
   especial "optparse.SUPPRESS_HELP".

Option.metavar

   (padrão: derivado de strings de opção)

   Substituto para o(s) argumento(s) de opção a ser(em) usado(s) ao
   exibir texto de ajuda. Veja a seção Tutorial para um exemplo.


Ações de opção padrão
---------------------

The various option actions all have slightly different requirements
and effects. Most actions have several relevant option attributes
which you may specify to guide "optparse"'s behaviour; a few have
required attributes, which you must specify for any option using that
action.

* ""store"" [relevante: "type", "dest", "nargs", "choices"]

  A opção deve ser seguida por um argumento, que é convertido em um
  valor de acordo com "type" e armazenado em "dest". Se "nargs" > 1,
  vários argumentos serão consumidos da linha de comando; todos serão
  convertidos de acordo com "type" e armazenados em "dest" como uma
  tupla. Veja a seção Tipos de opção padrão.

  Se "choices" for fornecido (uma lista ou tupla de strings), o tipo
  padrão será ""choice"".

  Se "type" não for fornecido, o padrão será ""string"".

  If "dest" is not supplied, "optparse" derives a destination from the
  first long option string (e.g., "--foo-bar" implies "foo_bar"). If
  there are no long option strings, "optparse" derives a destination
  from the first short option string (e.g., "-f" implies "f").

  Exemplo:

     parser.add_option("-f")
     parser.add_option("-p", type="float", nargs=3, dest="point")

  Como ele analisa a linha de comando

     -f foo.txt -p 1 -3.5 4 -fbar.txt

  "optparse" will set

     options.f = "foo.txt"
     options.point = (1.0, -3.5, 4.0)
     options.f = "bar.txt"

* ""store_const"" [obrigatório: "const"; relevante: "dest"]

  O valor de "const" é armazenado em "dest".

  Exemplo:

     parser.add_option("-q", "--quiet",
                       action="store_const", const=0, dest="verbose")
     parser.add_option("-v", "--verbose",
                       action="store_const", const=1, dest="verbose")
     parser.add_option("--noisy",
                       action="store_const", const=2, dest="verbose")

  If "--noisy" is seen, "optparse" will set

     options.verbose = 2

* ""store_true"" [relevante: "dest"]

  Um caso especial de ""store_const"" que armazena "True" em "dest".

* ""store_false"" [relevante: "dest"]

  Como ""store_true"", mas armazenad "False".

  Exemplo:

     parser.add_option("--clobber", action="store_true", dest="clobber")
     parser.add_option("--no-clobber", action="store_false", dest="clobber")

* ""append"" [relevante: "type", "dest", "nargs", "choices"]

  The option must be followed by an argument, which is appended to the
  list in "dest".  If no default value for "dest" is supplied, an
  empty list is automatically created when "optparse" first encounters
  this option on the command-line.  If "nargs" > 1, multiple arguments
  are consumed, and a tuple of length "nargs" is appended to "dest".

  Os padrões para "type" e "dest" são os mesmos da ação ""store"".

  Exemplo:

     parser.add_option("-t", "--tracks", action="append", type="int")

  If "-t3" is seen on the command-line, "optparse" does the equivalent
  of:

     options.tracks = []
     options.tracks.append(int("3"))

  Se, um pouco mais tarde, "--tracks=4" for encontrado, ele faz:

     options.tracks.append(int("4"))

  A ação "append" chama o método "append" no valor atual da opção.
  Isso significa que qualquer valor padrão especificado deve ter um
  método "append". Isso também significa que se o valor padrão não for
  vazio, os elementos padrão estarão presentes no valor analisado para
  a opção, com quaisquer valores da linha de comando anexados após
  esses valores padrão:

     >>> parser.add_option("--files", action="append", default=['~/.mypkg/defaults'])
     >>> opts, args = parser.parse_args(['--files', 'overrides.mypkg'])
     >>> opts.files
     ['~/.mypkg/defaults', 'overrides.mypkg']

* ""append_const"" [obrigatório: "const"; relevante: "dest"]

  Como ""store_const"", mas o valor de "const" é anexado a "dest";
  assim como em ""append"", "dest" assume como padrão "None", e uma
  lista vazia é criada automaticamente na primeira vez que a opção é
  encontrada.

* ""count"" [relevante: "dest"]

  Incrementa o inteiro armazenado em "dest". Se nenhum valor padrão
  for fornecido, "dest" é definido como zero antes de ser incrementado
  pela primeira vez.

  Exemplo:

     parser.add_option("-v", action="count", dest="verbosity")

  The first time "-v" is seen on the command line, "optparse" does the
  equivalent of:

     options.verbosity = 0
     options.verbosity += 1

  Cada ocorrência subsequente de "-v" resulta em

     options.verbosity += 1

* ""callback"" [obrigatório: "callback"; relevante: "type", "nargs",
  "callback_args", "callback_kwargs"]

  Chama a função especificada por "callback", que é chamada como

     func(option, opt_str, value, parser, *args, **kwargs)

  Veja a seção Funções de retorno de opção para mais detalhes.

* ""help""

  Exibe uma mensagem de ajuda completa para todas as opções no
  analisador sintático de opções atual. A mensagem de ajuda é
  construída a partir da string "usage" passada para o construtor do
  OptionParser e da string "help" passada para cada opção.

  Se nenhuma string de "help" for fornecida para uma opção, ela ainda
  será listada na mensagem de ajuda. Para omitir uma opção
  completamente, use o valor especial "optparse.SUPPRESS_HELP".

  "optparse" automatically adds a "help" option to all OptionParsers,
  so you do not normally need to create one.

  Exemplo:

     from optparse import OptionParser, SUPPRESS_HELP

     # geralmente, uma opção de ajuda é adicionada
     # automaticamente, mas que podem ser suprimida
     # usando o argumento add_help_option
     parser = OptionParser(add_help_option=False)

     parser.add_option("-h", "--help", action="help")
     parser.add_option("-v", action="store_true", dest="verbose",
                       help="Be moderately verbose")
     parser.add_option("--file", dest="filename",
                       help="Input file to read data from")
     parser.add_option("--secret", help=SUPPRESS_HELP)

  If "optparse" sees either "-h" or "--help" on the command line, it
  will print something like the following help message to stdout
  (assuming "sys.argv[0]" is ""foo.py""):

     Usage: foo.py [options]

     Options:
       -h, --help        Show this help message and exit
       -v                Be moderately verbose
       --file=FILENAME   Input file to read data from

  After printing the help message, "optparse" terminates your process
  with "sys.exit(0)".

* ""version""

  Prints the version number supplied to the OptionParser to stdout and
  exits. The version number is actually formatted and printed by the
  "print_version()" method of OptionParser.  Generally only relevant
  if the "version" argument is supplied to the OptionParser
  constructor.  As with "help" options, you will rarely create
  "version" options, since "optparse" automatically adds them when
  needed.


Tipos de opção padrão
---------------------

"optparse" has five built-in option types: ""string"", ""int"",
""choice"", ""float"" and ""complex"".  If you need to add new option
types, see section Extending optparse.

Os argumentos para opções de string não são verificados ou convertidos
de forma alguma: o texto na linha de comando é armazenado no destino
(ou passado para a função de retorno) como está.

Argumentos inteiros (tipo ""int"") são analisados da seguinte forma:

* se o número começar com "0x", ele será analisado como um número
  hexadecimal

* se o número começar com "0", ele será analisado como um número octal

* se o número começar com "0b", ele será analisado como um número
  binário

* caso contrário, o número é analisado como um número decimal

The conversion is done by calling "int()" with the appropriate base
(2, 8, 10, or 16).  If this fails, so will "optparse", although with a
more useful error message.

Os argumentos de opção ""float"" e ""complex"" são convertidos
diretamente com "float()" e "complex()", com tratamento de erros
semelhante.

As opções ""choice"" são um subtipo das opções ""string"". O atributo
da opção "choices" (uma sequência de strings) define o conjunto de
argumentos de opção permitidos. "optparse.check_choice()" compara os
argumentos de opção fornecidos pelo usuário com esta lista mestre e
levanta "OptionValueError" se uma string inválida for fornecida.


Análise de argumentos
---------------------

O objetivo de criar e preencher uma instância de OptionParser é chamar
seu método "parse_args()".

OptionParser.parse_args(args=None, values=None)

   Analisa as opções de linha de comando encontradas em *args*.

   Os parâmetros de entrada são

   "args"
      a lista de argumentos para processar (padrão: "sys.argv[1:]")

   "values"
      um objeto "Values" para armazenar argumentos de opção (padrão:
      uma nova instância de "Values") -- se você fornecer um objeto
      existente, os padrões de opção não serão inicializados nele

   e o valor de retorno é um par "(options, args)" sendo

   "options"
      the same object that was passed in as *values*, or the
      "optparse.Values" instance created by "optparse"

   "args"
      os argumentos posicionais restantes depois que todas as opções
      foram processadas

O uso mais comum é não fornecer nenhum argumento nomeado. Se você
fornecer "values", ele será modificado com chamadas repetidas de
"setattr()" (aproximadamente uma para cada argumento de opção
armazenado em um destino de opção) e retornado por "parse_args()".

Se "parse_args()" encontrar algum erro na lista de argumentos, ele
chama o método "error()" da instância de OptionParser com uma mensagem
de erro apropriada para o usuário final. Isso, em última análise,
encerra seu processo com um status de saída 2 (o status de saída
tradicional do Unix para erros de linha de comando).


Consultando e manipulando seu analisador sintático de opções
------------------------------------------------------------

O comportamento padrão do analisador sintático de opções pode ser
ligeiramente personalizado, e você também pode dar uma olhada no seu
analisador de opções e ver o que há lá. A classe OptionParser fornece
vários métodos para ajudar você:

OptionParser.disable_interspersed_args()

   Set parsing to stop on the first non-option.  For example, if "-a"
   and "-b" are both simple options that take no arguments, "optparse"
   normally accepts this syntax:

      prog -a arg1 -b arg2

   e trata-a como equivalente a

      prog -a -b arg1 arg2

   Para desabilitar esse recurso, chame "disable_interspersed_args()".
   Isso restaura a sintaxe Unix tradicional, onde a análise de opções
   para com o primeiro argumento não-opcional.

   Use isto se você tiver um processador de comando que executa outro
   comando que tem opções próprias e você quer ter certeza de que
   essas opções não fiquem confusas. Por exemplo, cada comando pode
   ter um conjunto diferente de opções.

OptionParser.enable_interspersed_args()

   Define a análise para não parar na primeira não opção, permitindo
   intercalar alternadores com argumentos de comando. Esse é o
   comportamento padrão.

OptionParser.get_option(opt_str)

   Retorna a instância de Option com a string de opção *opt_str*, ou
   "None" se nenhuma opção tiver essa string de opção.

OptionParser.has_option(opt_str)

   Retorna "True" se o objeto OptionParser tiver uma opção com string
   de opção *opt_str* (por exemplo, "-q" ou "--verbose").

OptionParser.remove_option(opt_str)

   Se o "OptionParser" tiver uma opção correspondente a *opt_str*,
   essa opção será removida. Se essa opção fornecer quaisquer outras
   strings de opção, todas essas strings de opção se tornarão
   inválidas. Se *opt_str* não ocorrer em nenhuma opção pertencente a
   este "OptionParser", levanta "ValueError".


Conflitos entre opções
----------------------

Se você não tomar cuidado, é fácil definir opções com strings de
opções conflitantes:

   parser.add_option("-n", "--dry-run", ...)
   ...
   parser.add_option("-n", "--noisy", ...)

(Isto é particularmente verdadeiro se você definiu sua própria
subclasse de OptionParser com algumas opções padrão.)

Every time you add an option, "optparse" checks for conflicts with
existing options.  If it finds any, it invokes the current conflict-
handling mechanism. You can set the conflict-handling mechanism either
in the constructor:

   parser = OptionParser(..., conflict_handler=handler)

ou com uma chamada separada:

   parser.set_conflict_handler(handler)

Os manipuladores de conflitos disponíveis são:

   ""error"" (padrão)
      presume que os conflitos de opções são um erro de programação e
      levanta "OptionConflictError"

   ""resolve""
      resolve conflitos de opções de forma inteligente (veja abaixo)

Como exemplo, vamos definir um "OptionParser" que resolve conflitos de
forma inteligente e adiciona opções conflitantes a ele:

   parser = OptionParser(conflict_handler="resolve")
   parser.add_option("-n", "--dry-run", ..., help="do no harm")
   parser.add_option("-n", "--noisy", ..., help="be noisy")

At this point, "optparse" detects that a previously added option is
already using the "-n" option string.  Since "conflict_handler" is
""resolve"", it resolves the situation by removing "-n" from the
earlier option's list of option strings.  Now "--dry-run" is the only
way for the user to activate that option.  If the user asks for help,
the help message will reflect that:

   Options:
     --dry-run     do no harm
     ...
     -n, --noisy   be noisy

It's possible to whittle away the option strings for a previously
added option until there are none left, and the user has no way of
invoking that option from the command-line.  In that case, "optparse"
removes that option completely, so it doesn't show up in help text or
anywhere else. Carrying on with our existing OptionParser:

   parser.add_option("--dry-run", ..., help="new dry-run option")

At this point, the original "-n"/"--dry-run" option is no longer
accessible, so "optparse" removes it, leaving this help text:

   Options:
     ...
     -n, --noisy   be noisy
     --dry-run     new dry-run option


Limpeza
-------

As instâncias de OptionParser têm várias referências cíclicas. Isso
não deve ser um problema para o coletor de lixo do Python, mas você
pode desejar quebrar as referências cíclicas explicitamente chamando
"destroy()" no seu OptionParser quando terminar de usá-lo. Isso é
particularmente útil em aplicações de longa execução, onde gráficos de
objetos grandes podem ser acessados do seu OptionParser.


Outros métodos
--------------

OptionParser provê vários outros métodos públicos:

OptionParser.set_usage(usage)

   Defina a string de uso de acordo com as regras descritas acima para
   o argumento nomeado do construtor "usage". Passar "None" define a
   string de uso padrão; use "optparse.SUPPRESS_USAGE" para suprimir
   uma mensagem de uso.

OptionParser.print_usage(file=None)

   Exibe a mensagem de uso para o programa atual ("self.usage") em
   *file* (stdout padrão). Qualquer ocorrência da string "%prog" em
   "self.usage" é substituída pelo nome do programa atual. Não faz
   nada se "self.usage" estiver vazio ou não definido.

OptionParser.get_usage()

   O mesmo que "print_usage()", mas retorna a string de uso em vez de
   exibi-la.

OptionParser.set_defaults(dest=value, ...)

   Define valores padrão para vários destinos de opção de uma vez.
   Usar "set_defaults()" é a maneira preferida de definir valores
   padrão para opções, já que várias opções podem compartilhar o mesmo
   destino. Por exemplo, se várias opções de "modo" definirem o mesmo
   destino, qualquer uma delas pode definir o padrão, e a última
   vence:

      parser.add_option("--advanced", action="store_const",
                        dest="mode", const="advanced",
                        default="novice")    # substituída abaixo
      parser.add_option("--novice", action="store_const",
                        dest="mode", const="novice",
                        default="advanced")  # substitui a configuração acima

   Para evitar essa confusão, use "set_defaults()":

      parser.set_defaults(mode="advanced")
      parser.add_option("--advanced", action="store_const",
                        dest="mode", const="advanced")
      parser.add_option("--novice", action="store_const",
                        dest="mode", const="novice")


Funções de retorno de opção
===========================

When "optparse"'s built-in actions and types aren't quite enough for
your needs, you have two choices: extend "optparse" or define a
callback option. Extending "optparse" is more general, but overkill
for a lot of simple cases.  Quite often a simple callback is all you
need.

Há duas etapas para definir uma opção de retorno de chamada:

* definir a opção em si usando a ação ""callback""

* escrever o função de retorno; esta é uma função (ou método) que
  recebe pelo menos quatro argumentos, conforme descrito abaixo


Definindo uma opção de retorno de chamada
-----------------------------------------

Como sempre, a maneira mais fácil de definir uma opção de retorno de
chamada é usando o método "OptionParser.add_option()". Além de
"action", o único atributo de opção que você deve especificar é
"callback", a função a ser chamada:

   parser.add_option("-c", action="callback", callback=my_callback)

"callback" is a function (or other callable object), so you must have
already defined "my_callback()" when you create this callback option.
In this simple case, "optparse" doesn't even know if "-c" takes any
arguments, which usually means that the option takes no arguments---
the mere presence of "-c" on the command-line is all it needs to know.
In some circumstances, though, you might want your callback to consume
an arbitrary number of command-line arguments.  This is where writing
callbacks gets tricky; it's covered later in this section.

"optparse" always passes four particular arguments to your callback,
and it will only pass additional arguments if you specify them via
"callback_args" and "callback_kwargs".  Thus, the minimal callback
function signature is:

   def my_callback(option, opt, value, parser):

Os quatro argumentos para um retorno de chamada são descritos abaixo.

Há vários outros atributos de opção que você pode fornecer ao definir
uma opção de retorno de chamada:

"type"
   has its usual meaning: as with the ""store"" or ""append"" actions,
   it instructs "optparse" to consume one argument and convert it to
   "type".  Rather than storing the converted value(s) anywhere,
   though, "optparse" passes it to your callback function.

"nargs"
   also has its usual meaning: if it is supplied and > 1, "optparse"
   will consume "nargs" arguments, each of which must be convertible
   to "type".  It then passes a tuple of converted values to your
   callback.

"callback_args"
   uma tupla de argumentos posicionais extras para passar para a
   função de retorno

"callback_kwargs"
   um dicionário de argumentos nomeados extras para passar para a
   função de retorno


Como os retornos de chamada são chamados
----------------------------------------

Todos os retornos de chamada são chamados da seguinte forma:

   func(option, opt_str, value, parser, *args, **kwargs)

onde

"option"
   é a instância de Option que está chamando o retorno de chamada

"opt_str"
   é a string de opção vista na linha de comando que está acionando o
   retorno de chamada. (Se uma opção longa abreviada foi usada,
   "opt_str" será a string de opção canônica completa --- por exemplo,
   se o usuário colocar "--foo" na linha de comando como uma
   abreviação para "--foobar", então "opt_str" será ""--foobar"".)

"value"
   is the argument to this option seen on the command-line.
   "optparse" will only expect an argument if "type" is set; the type
   of "value" will be the type implied by the option's type.  If
   "type" for this option is "None" (no argument expected), then
   "value" will be "None".  If "nargs" > 1, "value" will be a tuple of
   values of the appropriate type.

"parser"
   é a instância OptionParser que controla tudo, útil principalmente
   porque você pode acessar alguns outros dados interessantes por meio
   de seus atributos de instância:

   "parser.largs"
      a lista atual de argumentos restantes, ou seja, argumentos que
      foram consumidos, mas não são opções nem argumentos de opção.
      Sinta-se à vontade para modificar "parser.largs", por exemplo,
      adicionando mais argumentos a ele. (Esta lista se tornará
      "args", o segundo valor de retorno de "parse_args()".)

   "parser.rargs"
      a lista atual de argumentos restantes, ou seja, com "opt_str" e
      "value" (se aplicável) removidos, e apenas os argumentos que os
      seguem ainda lá. Sinta-se à vontade para modificar
      "parser.rargs", por exemplo, consumindo mais argumentos.

   "parser.values"
      the object where option values are by default stored (an
      instance of optparse.OptionValues).  This lets callbacks use the
      same mechanism as the rest of "optparse" for storing option
      values; you don't need to mess around with globals or closures.
      You can also access or modify the value(s) of any options
      already encountered on the command-line.

"args"
   é uma tupla de argumentos posicionais arbitrários fornecidos por
   meio do atributo de opção "callback_args".

"kwargs"
   é um dicionário de argumentos nomeados arbitrários fornecidos via
   "callback_kwargs".


Levantando erros em uma função de retorno
-----------------------------------------

The callback function should raise "OptionValueError" if there are any
problems with the option or its argument(s).  "optparse" catches this
and terminates the program, printing the error message you supply to
stderr.  Your message should be clear, concise, accurate, and mention
the option at fault. Otherwise, the user will have a hard time
figuring out what they did wrong.


Exemplo de função de retorno 1: retorno de chamada trivial
----------------------------------------------------------

Aqui está um exemplo de uma opção de retorno de chamada que não aceita
argumentos e simplesmente registra que a opção foi vista:

   def record_foo_seen(option, opt_str, value, parser):
       parser.values.saw_foo = True

   parser.add_option("--foo", action="callback", callback=record_foo_seen)

Claro, você pode fazer isso com a ação ""store_true"".


Exemplo de função de retorno 2: verificar a ordem das opções
------------------------------------------------------------

Aqui está um exemplo um pouco mais interessante: registra o fato de
que "-a" é visto, mas explode se ele vier depois de "-b" na linha de
comando.

   def check_order(option, opt_str, value, parser):
       if parser.values.b:
           raise OptionValueError("can't use -a after -b")
       parser.values.a = 1
   ...
   parser.add_option("-a", action="callback", callback=check_order)
   parser.add_option("-b", action="store_true", dest="b")


Exemplo 3 de função de retorno: verificar a ordem das opções (generalizada)
---------------------------------------------------------------------------

Se você quiser reutilizar essa função de retorno para várias opções
semelhantes (definir um sinalizador, mas explodir se "-b" já tiver
sido visto), será preciso um pouco de trabalho: a mensagem de erro e o
sinalizador que ele define devem ser generalizados.

   def check_order(option, opt_str, value, parser):
       if parser.values.b:
           raise OptionValueError("can't use %s after -b" % opt_str)
       setattr(parser.values, option.dest, 1)
   ...
   parser.add_option("-a", action="callback", callback=check_order, dest='a')
   parser.add_option("-b", action="store_true", dest="b")
   parser.add_option("-c", action="callback", callback=check_order, dest='c')


Exemplo de função de retorno 4: verificar uma condição arbitrária
-----------------------------------------------------------------

Claro, você pode colocar qualquer condição ali---você não está
limitado a verificar os valores de opções já definidas. Por exemplo,
se você tem opções que não devem ser chamadas quando a lua está cheia,
tudo o que você tem a fazer é isto:

   def check_moon(option, opt_str, value, parser):
       if is_moon_full():
           raise OptionValueError("%s option invalid when moon is full"
                                  % opt_str)
       setattr(parser.values, option.dest, 1)
   ...
   parser.add_option("--foo",
                     action="callback", callback=check_moon, dest="foo")

(A definição de "is_moon_full()" é deixada como um exercício para o
leitor.)


Exemplo de função de retorno 5: argumentos fixos
------------------------------------------------

As coisas ficam um pouco mais interessantes quando você define opções
de retorno de chamada que aceitam um número fixo de argumentos.
Especificar que uma opção de retorno de chamada aceita argumentos é
semelhante a definir uma opção ""store"" ou ""append"": se você
definir "type", então a opção aceita um argumento que deve ser
conversível para esse tipo; se você definir ainda "nargs", então a
opção aceita argumentos "nargs".

Aqui está um exemplo que apenas emula a ação padrão ""store"":

   def store_value(option, opt_str, value, parser):
       setattr(parser.values, option.dest, value)
   ...
   parser.add_option("--foo",
                     action="callback", callback=store_value,
                     type="int", nargs=3, dest="foo")

Note that "optparse" takes care of consuming 3 arguments and
converting them to integers for you; all you have to do is store them.
(Or whatever; obviously you don't need a callback for this example.)


Exemplo de função de retorno 6: argumentos variáveis
----------------------------------------------------

Things get hairy when you want an option to take a variable number of
arguments. For this case, you must write a callback, as "optparse"
doesn't provide any built-in capabilities for it.  And you have to
deal with certain intricacies of conventional Unix command-line
parsing that "optparse" normally handles for you.  In particular,
callbacks should implement the conventional rules for bare "--" and
"-" arguments:

* "--" ou "-" podem ser argumentos de opção

* "--" apenas (se não for o argumento para alguma opção): interrompe o
  processamento da linha de comando e descarta o "--"

* "-" apenas (se não for o argumento para alguma opção): interrompe o
  processamento da linha de comando, mas mantém o "-" (anexa-o a
  "parser.largs")

If you want an option that takes a variable number of arguments, there
are several subtle, tricky issues to worry about.  The exact
implementation you choose will be based on which trade-offs you're
willing to make for your application (which is why "optparse" doesn't
support this sort of thing directly).

No entanto, aqui vai uma tentativa de função de retorno para uma opção
com argumentos variáveis:

   def vararg_callback(option, opt_str, value, parser):
       assert value is None
       value = []

       def floatable(str):
           try:
               float(str)
               return True
           except ValueError:
               return False

       for arg in parser.rargs:
           # para em --foo como opções
           if arg[:2] == "--" and len(arg) > 2:
               break
           # para em -a, mas não em -3 ou -3.0
           if arg[:1] == "-" and len(arg) > 1 and not floatable(arg):
               break
           value.append(arg)

       del parser.rargs[:len(value)]
       setattr(parser.values, option.dest, value)

   ...
   parser.add_option("-c", "--callback", dest="vararg_attr",
                     action="callback", callback=vararg_callback)


Extending "optparse"
====================

Since the two major controlling factors in how "optparse" interprets
command-line options are the action and type of each option, the most
likely direction of extension is to add new actions and new types.


Adicionando novos tipos
-----------------------

To add new types, you need to define your own subclass of "optparse"'s
"Option" class.  This class has a couple of attributes that define
"optparse"'s types: "TYPES" and "TYPE_CHECKER".

Option.TYPES

   Uma tupla de nomes de tipos; na sua subclasse, basta definir uma
   nova tupla "TYPES" que se baseia na tupla padrão.

Option.TYPE_CHECKER

   Um dicionário que mapeia nomes de tipos para funções de verificação
   de tipos. Uma função de verificação de tipos tem a seguinte
   assinatura:

      def check_mytype(option, opt, value)

   sendo "option" uma instância "Option", "opt" é uma string de opção
   (por exemplo, "-f"), e "value" é a string da linha de comando que
   deve ser verificada e convertida para o tipo desejado.
   "check_mytype()" deve retornar um objeto do tipo hipotético
   "mytype". O valor retornado por uma função de verificação de tipo
   acabará na instância OptionValues retornada por
   "OptionParser.parse_args()", ou será passado para uma função de
   retorno como o parâmetro "value".

   Sua função de verificação de tipo deve levantar "OptionValueError"
   se encontrar algum problema. "OptionValueError" recebe um único
   argumento de string, que é passado como está para o método
   "error()" do "OptionParser", que por sua vez adiciona o nome do
   programa e a string ""error:"" e exibe tudo no stderr antes de
   encerrar o processo.

Here's a silly example that demonstrates adding a ""complex"" option
type to parse Python-style complex numbers on the command line.  (This
is even sillier than it used to be, because "optparse" 1.3 added
built-in support for complex numbers, but never mind.)

Primeiro, as importações necessárias:

   from copy import copy
   from optparse import Option, OptionValueError

Você precisa definir seu verificador de tipo primeiro, pois ele será
referenciado mais tarde (no atributo de classe "TYPE_CHECKER" da sua
subclasse de Option):

   def check_complex(option, opt, value):
       try:
           return complex(value)
       except ValueError:
           raise OptionValueError(
               "option %s: invalid complex value: %r" % (opt, value))

Finalmente, a subclasse de Option:

   class MyOption (Option):
       TYPES = Option.TYPES + ("complex",)
       TYPE_CHECKER = copy(Option.TYPE_CHECKER)
       TYPE_CHECKER["complex"] = check_complex

(If we didn't make a "copy()" of "Option.TYPE_CHECKER", we would end
up modifying the "TYPE_CHECKER" attribute of "optparse"'s Option
class.  This being Python, nothing stops you from doing that except
good manners and common sense.)

That's it!  Now you can write a script that uses the new option type
just like any other "optparse"-based script, except you have to
instruct your OptionParser to use MyOption instead of Option:

   parser = OptionParser(option_class=MyOption)
   parser.add_option("-c", type="complex")

Como alternativa, você pode criar sua própria lista de opções e
passá-la para o OptionParser; se você não usar "add_option()" da
maneira acima, não precisa informar ao OptionParser qual classe de
opção usar:

   option_list = [MyOption("-c", action="store", type="complex", dest="c")]
   parser = OptionParser(option_list=option_list)


Adicionando novas ações
-----------------------

Adding new actions is a bit trickier, because you have to understand
that "optparse" has a couple of classifications for actions:

Ações "store"
   actions that result in "optparse" storing a value to an attribute
   of the current OptionValues instance; these options require a
   "dest" attribute to be supplied to the Option constructor.

Ações "typed"
   Ações que pegam um valor da linha de comando e esperam que ele seja
   de um certo tipo; ou melhor, uma string que pode ser convertida
   para um certo tipo. Essas opções requerem um atributo "type" para o
   construtor Option.

Esses são conjuntos sobrepostos: algumas ações "store" padrão são
""store"", ""store_const"", ""append"" e ""count"", enquanto as ações
"typed" padrão são ""store"", ""append"" e ""callback"".

Ao adicionar uma ação, você precisa categorizá-la listando-a em pelo
menos um dos seguintes atributos de classe de Option (todos são listas
de strings):

Option.ACTIONS

   Todas as ações devem ser listadas em ACTIONS.

Option.STORE_ACTIONS

   As ações "store" também são listadas aqui.

Option.TYPED_ACTIONS

   As ações "typed" também são listadas aqui.

Option.ALWAYS_TYPED_ACTIONS

   Actions that always take a type (i.e. whose options always take a
   value) are additionally listed here.  The only effect of this is
   that "optparse" assigns the default type, ""string"", to options
   with no explicit type whose action is listed in
   "ALWAYS_TYPED_ACTIONS".

Para realmente implementar sua nova ação, você deve substituir o
método "take_action()" de Option e adicionar um caso que reconheça sua
ação.

Por exemplo, vamos adicionar uma ação ""extend"". Isso é semelhante à
ação padrão ""append"", mas em vez de pegar um único valor da linha de
comando e anexá-lo a uma lista existente, ""extend"" pegará vários
valores em uma única string delimitada por vírgulas e estenderá uma
lista existente com eles. Ou seja, se "--names" for uma opção
""extend"" do tipo ""string"", a linha de comando

   --names=foo,bar --names blah --names ding,dong

resultaria em uma lista

   ["foo", "bar", "blah", "ding", "dong"]

Novamente, nós definimos uma subclasse de Option:

   class MyOption(Option):

       ACTIONS = Option.ACTIONS + ("extend",)
       STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
       TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)
       ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

       def take_action(self, action, dest, opt, value, values, parser):
           if action == "extend":
               lvalue = value.split(",")
               values.ensure_value(dest, []).extend(lvalue)
           else:
               Option.take_action(
                   self, action, dest, opt, value, values, parser)

Características de nota:

* ""extend"" espera um valor na linha de comando e armazena esse valor
  em algum lugar, então ele vai em "STORE_ACTIONS" e "TYPED_ACTIONS".

* to ensure that "optparse" assigns the default type of ""string"" to
  ""extend"" actions, we put the ""extend"" action in
  "ALWAYS_TYPED_ACTIONS" as well.

* "MyOption.take_action()" implements just this one new action, and
  passes control back to "Option.take_action()" for the standard
  "optparse" actions.

* "values" é uma instância da classe optparse_parser.Values, que
  fornece o método muito útil "ensure_value()". "ensure_value()" é
  essencialmente "getattr()" com uma válvula de segurança; é chamado
  como

     values.ensure_value(attr, value)

  Se o atributo "attr" de "values" não existir ou for "None", então
  ensure_value() primeiro o define como "value" e então retorna
  "value". Isso é muito útil para ações como ""extend"", ""append"" e
  ""count"", todas as quais acumulam dados em uma variável e esperam
  que essa variável seja de um certo tipo (uma lista para as duas
  primeiras, um inteiro para a última). Usar "ensure_value()"
  significa que os scripts que usam sua ação não precisam se preocupar
  em definir um valor padrão para os destinos de opção em questão;
  eles podem simplesmente deixar o padrão como "None" e
  "ensure_value()" cuidará de acertar quando for necessário.


Exceções
========

exception optparse.OptionError

   Levantada se uma instância de "Option" for criada com argumentos
   inválidos ou inconsistentes.

exception optparse.OptionConflictError

   Levantada se opções conflitantes forem adicionadas a um instância
   de "OptionParser".

exception optparse.OptionValueError

   Levantada se um valor de opção inválido for encontrado na linha de
   comando.

exception optparse.BadOptionError

   Levantada se uma opção inválida for passada na linha de comando.

exception optparse.AmbiguousOptionError

   Levantada se uma opção ambígua for passada na linha de comando.
