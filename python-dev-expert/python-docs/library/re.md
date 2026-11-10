"re" --- Operações com expressões regulares
*******************************************

**Código-fonte:** Lib/re/

======================================================================

Este módulo fornece operações para correspondência de expressões
regulares semelhantes às encontradas em Perl. O nome do módulo vem das
iniciais do termo em inglês *regular expressions*, também
frequentemente chamadas de *regex*.

Tanto os padrões quanto as strings a serem pesquisados podem ser
strings Unicode ("str") assim como strings de 8 bits ("bytes"). No
entanto, strings Unicode e strings de 8 bits não podem ser misturadas:
ou seja, você não pode corresponder uma string Unicode com um padrão
de bytes ou vice-versa; da mesma forma, ao solicitar uma substituição,
a string de substituição deve ser do mesmo tipo que o padrão e a
string de pesquisa.

Expressões regulares usam o caractere de contrabarra ("'\'") para
indicar formas especiais ou para permitir que caracteres especiais
sejam usados sem invocar seu significado especial. Isso colide com o
uso em Python do mesmo caractere para o mesmo propósito em literais de
string; por exemplo, para corresponder a uma contrabarra literal,
pode-se ter que escrever "'\\\\'" como a string do padrão, porque a
expressão regular deve ser "\\", e cada contrabarra deve ser expressa
como "\\" dentro de um literal de string Python regular. Além disso,
observe que quaisquer sequências de escape inválidas no uso do Python
da contrabarra em literais de string agora levantam uma exceção
"SyntaxWarning" e no futuro isso se tornará um "SyntaxError". Esse
comportamento acontecerá mesmo se for uma sequência de escape válida
para uma expressão regular.

A solução é usar a notação de string bruta do Python para padrões de
expressão regular; as contrabarras não são tratadas de nenhuma maneira
especial em uma string literal com o prefixo "'r'". Portanto, "r"\n""
é uma string de dois caracteres contendo "'\'" e "'n'", enquanto
""\n"" é uma string de um caractere contendo uma nova linha.
Normalmente, os padrões serão expressos em código Python usando esta
notação de string bruta.

É importante notar que a maioria das operações de expressão regular
estão disponíveis como funções e métodos em nível de módulo em
expressões regulares compiladas. As funções são atalhos que não exigem
que você compile um objeto de expressão regular primeiro, mas perdem-
se alguns parâmetros de ajuste fino.

Ver também:

  O módulo de terceiros regex possui uma API compatível com o módulo
  da biblioteca padrão "re", mas oferece funcionalidades adicionais e
  um suporte mais completo a Unicode.


Sintaxe de expressão regular
============================

Uma expressão regular (ou ER) especifica um conjunto de strings que
corresponde a ela; as funções neste módulo permitem que você verifique
se uma determinada string corresponde a uma determinada expressão
regular (ou se uma determinada expressão regular corresponde a uma
determinada string, o que resulta na mesma coisa).

As expressões regulares podem ser concatenadas para formar novas
expressões regulares; se *A* e *B* forem expressões regulares, então
*AB* também será uma expressão regular. Em geral, se uma string *p*
corresponder a *A* e outra string *q* corresponder a *B*, a string
*pq* corresponderá a AB. Isso é válido, a menos que *A* ou *B*
contenham operações de baixa precedência; condições de contorno entre
*A* e *B*; ou ter referências de grupo numeradas. Assim, expressões
complexas podem ser facilmente construídas a partir de expressões
primitivas mais simples, como as descritas aqui. Para obter detalhes
sobre a teoria e implementação de expressões regulares, consulte o
livro de Friedl [Frie09], ou quase qualquer livro sobre construção de
compiladores.

Segue uma breve explicação do formato das expressões regulares. Para
mais informações e uma apresentação mais suave, consulte o tutorial de
Regular expression HOWTO.

As expressões regulares podem conter caracteres especiais e comuns. A
maioria dos caracteres comuns, como "'A'", "'a'" ou "'0'", são as
expressões regulares mais simples; eles simplesmente se correspondem.
Você pode concatenar caracteres comuns, de forma que "último"
corresponda à string "'último'". (No restante desta seção,
escreveremos ERs "neste estilo especial", geralmente sem aspas, e
strings para serem correspondidas "'entre aspas simples'".)

Alguns caracteres, como "'|'" ou "'('", são especiais. Os caracteres
especiais representam classes de caracteres comuns ou afetam como as
expressões regulares em torno deles são interpretadas.

Operadores de repetição ou quantificadores ("*", "+", "?", "{m,n}"
etc) não podem ser aninhados diretamente. Isso evita ambiguidade com o
sufixo modificador não guloso "?", e com outros modificadores em
outras implementações. Para aplicar uma segunda repetição a uma
repetição interna, podem ser usados parênteses. Por exemplo, a
expressão "(?:a{6})*" corresponde a qualquer múltiplo de seis
caracteres "'a'".


Special characters
------------------

Os caracteres especiais são:


"."
~~~

(Ponto.) No modo padrão, corresponde a qualquer caractere, exceto uma
nova linha. Se o sinalizador "DOTALL" foi especificado, ele
corresponde a qualquer caractere, incluindo uma nova linha. "(?s:.)"
corresponde a qualquer caractere independente de sinalizadores.


"^"
~~~

(Sinal de circunflexo.) Corresponde ao início da string, e no modo
"MULTILINE" também corresponde imediatamente após cada nova linha.


"$"
~~~

Corresponde ao final da string ou logo antes da nova linha no final da
string, e no modo "MULTILINE" também corresponde antes de uma nova
linha. "foo" corresponde a 'foo' e 'foobar', enquanto a expressão
regular "foo$" corresponde apenas a 'foo'. Mais interessante,
pesquisar por "foo.$" em "'foo1\nfoo2\n'" corresponde a 'foo2'
normalmente, mas 'foo1' no modo "MULTILINE"; procurando por um único
"$" em "'foo\n'" encontrará duas correspondências (vazias): uma logo
antes da nova linha e uma no final da string.


"*"
~~~

Faz a ER resultante corresponder a 0 ou mais repetições da ER
anterior, tantas repetições quantas forem possíveis. "ab*"
corresponderá a 'a', 'ab' ou 'a' seguido por uma quantidade qualquer
de 'b's.


"+"
~~~

Faz com que a ER resultante corresponda a 1 ou mais repetições da ER
anterior. "ab+" irá corresponder a 'a' seguido por qualquer número
diferente de zero de 'b's; não corresponderá apenas a 'a'.


"?"
~~~

Faz a ER resultante corresponder a 0 ou 1 repetição da ER anterior.
"ab?" irá corresponder a 'a' ou 'ab'.


"*?", "+?", "??"
~~~~~~~~~~~~~~~~

Os quantificadores "'*'", "'+'" e "'?'" são todos *gulosos*; eles
correspondem ao máximo de texto possível. Às vezes, esse comportamento
não é desejado; se a ER "<.*>" for correspondida com "'<a> b <c>'",
ela irá corresponder a toda a string, e não apenas "'<a>'". Adicionar
"?" após o quantificador faz com que ele execute a correspondência da
maneira *não gulosa* ou *minimalista*; tão *poucos* caracteres quanto
possível serão correspondidos. Usando a ER "<.*?>" irá corresponder
apenas "'<a>'".


"*+", "++", "?+"
~~~~~~~~~~~~~~~~

Como os quantificadores "'*'", "'+'" e "'?'", aqueles em que "'+'" é
anexado também correspondem tantas vezes quanto possível. No entanto,
ao contrário dos quantificadores realmente gulosos, eles não permitem
retrocesso quando a expressão que o segue não corresponde. Estes são
conhecidos como quantificadores *possessivos*. Por exemplo, "a*a"
corresponderá a "'aaaa'" porque o "a*" corresponderá a todos os 4
"'a'"s, mas, quando o final "'a'" for encontrado, a expressão é
retrocedida para que no final o "a*" acabe correspondendo a 3 "'a'"s
no total, e o quarto "'a'" seja correspondido por o final "'a'". No
entanto, quando "a*+a" é usado para corresponder a "'aaaa'", o "a*+"
corresponderá a todos os 4 "'a'", mas quando o "'a'" final não
encontrar mais caracteres para corresponder, a expressão não pode ser
retrocedida e, portanto, não corresponderá. "x*+", "x++" e "x?+" são
equivalentes a "(?>x*)", "(?>x+)" e "(?>x?)" respectivamente.

Adicionado na versão 3.11.


"{m}"
~~~~~

Especifica que exatamente *m* cópias da ER anterior devem ser
correspondidas; menos correspondências fazem com que toda a ER não
seja correspondida. Por exemplo, "a{6}" irá corresponder exatamente a
seis caracteres "'a'", mas não a cinco.


"{m,n}"
~~~~~~~

Faz a ER resultante corresponder de *m* a *n* repetições da ER
anterior, tentando corresponder ao máximo de repetições possível. Por
exemplo, "a{3,5}" irá corresponder de 3 a 5 caracteres "'a'". A
omissão de *m* especifica um limite inferior de zero e a omissão de
*n* especifica um limite superior infinito. Como exemplo, "a{4,}b" irá
corresponder a "'aaaab'" ou mil caracteres "'a'" seguidos por um
"'b'", mas não "'aaab'". A vírgula não pode ser omitida ou o
modificador será confundido com a forma descrita anteriormente.


"{m,n}?"
~~~~~~~~

Faz a ER resultante corresponder de *m* a *n* repetições da ER
anterior, tentando corresponder o *mínimo* de repetições possível.
Esta é a versão não gulosa do quantificador anterior. Por exemplo, na
string de 6 caracteres "'aaaaaa'", "a{3,5}" irá corresponder a 5
caracteres "'a'", enquanto "a{3,5}?" corresponderá apenas a 3
caracteres.


"{m,n}+"
~~~~~~~~

Faz a ER resultante corresponder de *m* a *n* repetições da ER
anterior, tentando corresponder o maior número possível de repetições
*sem* estabelecer nenhum ponto de retrocesso. Esta é a versão
possessiva do quantificador acima. Por exemplo, na string de 6
caracteres "'aaaaaa'", "a{3,5}+aa" tenta corresponder 5 caracteres
"'a'", então, requerer mais 2 "'a'"s, precisará de mais caracteres do
que os disponíveis e, portanto, falhará, enquanto "a{3,5}aa"
corresponderá a "a{3,5}" capturando 5, depois 4 "'a'"s por retrocesso
e então os 2 "'a'"s finais são combinados com o "aa" final no padrão.
"x{m,n}+" é equivalente a "(?>x{m,n})".

Adicionado na versão 3.11.


"\"
~~~

Ou anula o efeito de caracteres especiais (permitindo a você
corresponder caracteres como "'*'", "'?'" e assim por diante), ou
sinaliza uma sequência especial; sequências especiais são discutidas
abaixo.

Se você não estiver usando uma string bruta para expressar o padrão,
lembre-se de que o Python também usa a contrabarra como uma sequência
de escape em literais de string; se a sequência de escape não for
reconhecida pelo analisador sintático do Python, a contrabarra e o
caractere subsequente serão incluídos na string resultante. No
entanto, se Python reconhecer a sequência resultante, a contrabarra
deve ser repetida duas vezes. Isso é complicado e difícil de entender,
portanto, é altamente recomendável que você use strings brutas para
todas as expressões, exceto as mais simples.


"[]"
~~~~

Usado para indicar um conjunto de caracteres. Em um conjunto:

* Caracteres podem ser listados individualmente, por exemplo, "[amk]"
  vai corresponder a "'a'", "'m'" ou "'k'".

* Intervalos de caracteres podem ser indicados fornecendo dois
  caracteres e separando-os por "'-'", por exemplo "[a-z]" irá
  corresponder a qualquer letra ASCII minúscula, "[0-5][0-9]" irá
  corresponder a todos os números de dois dígitos de "00" a "59", e
  "[0-9A-Fa-f]" irá corresponder a qualquer dígito hexadecimal. Se "-"
  for precedido de uma contrabarra (por exemplo, "[a\-z]") ou se for
  colocado como o primeiro ou último caractere (por exemplo, "[-a]" ou
  "[a-]"), ele corresponderá a um literal "'-'".

* Os caracteres especiais, exceto contrabarra, perdem seu significado
  especial dentro dos conjuntos. Por exemplo, "[(+*)]" vai
  corresponder a qualquer um dos caracteres literais "'('", "'+'",
  "'*'" ou "')'".

* A contrabarra escapa caracteres que têm significado especial em um
  conjunto, como "'-'", "']'", "'^'" e "'\\'", ou sinaliza uma
  sequência especial que representa um único caractere, como "\xa0" ou
  "\n", ou uma classe de caracteres como "\w" ou "\S" (definida
  abaixo). Observe que "\b" representa um único caractere de
  "backspace", não um limite de palavra como fora de um conjunto, e
  escapes numéricos como "\1" são sempre escapes octais, não
  referências de grupo. Sequências especiais que não correspondem a um
  único caractere, como "\A" e "\z", não são permitidas.

* Os caracteres que não estão dentro de um intervalo podem ser
  correspondidos *complementando* o conjunto. Se o primeiro caractere
  do conjunto for "'^'", todos os caracteres que *não* estiverem no
  conjunto serão correspondidos. Por exemplo, "[^5]" irá corresponder
  a qualquer caractere exceto "'5'", e "[^^]" irá corresponder a
  qualquer caractere exceto "'^'". "^" não tem nenhum significado
  especial se não for o primeiro caractere do conjunto.

* Para corresponder a um "']'" literal dentro de um conjunto,
  preceda-o com uma contrabarra ou coloque-o no início do conjunto.
  Por exemplo, "[()[\]{}]" e "[]()[{}]" vai corresponder ao colchete à
  direita, assim como o colchete, chave ou parêntese à esquerda.

* Suporte para conjuntos aninhados e operações de conjunto como no
  Padrão Técnico do Unicode #18 podem ser adicionados no futuro. Isso
  mudaria a sintaxe, então para facilitar essa mudança uma
  "FutureWarning" será levantada em casos ambíguos por enquanto. Isso
  inclui conjuntos que começam com um "'['" literal ou contendo
  sequências de caracteres literais "'--'", "'&&'", "'~~'" e "'||'".
  Para evitar um aviso, use uma contrabarra antes deles.

Alterado na versão 3.7: "FutureWarning" é levantada se um conjunto de
caracteres contém construções que mudarão semanticamente no futuro.


"|"
~~~

"A|B", onde *A* e *B* podem ser ERs arbitrárias, cria uma expressão
regular que corresponderá a *A* ou *B*. Um número arbitrário de ERs
pode ser separado por "'|'" desta forma. Isso também pode ser usado
dentro de grupos (veja abaixo). Conforme a string alvo é percorrida,
ERs separadas por "'|'" são avaliadas da esquerda para a direita.
Quando um padrão corresponde completamente, essa ramificação é aceita.
Isso significa que, assim que *A* corresponder, *B* não será avaliado
posteriormente, mesmo que produza uma correspondência geral mais
longa. Em outras palavras, o operador "'|'" nunca é guloso. Para
corresponder a um "'|'" literal, use "\|", ou coloque-o dentro de uma
classe de caractere, como em "[|]".


"(...)"
~~~~~~~

Corresponde a qualquer expressão regular que esteja entre parênteses e
indica o início e o fim de um grupo; o conteúdo de um grupo pode ser
recuperado após uma correspondência ter sido realizada e pode ser
correspondido posteriormente na string com a sequência especial
"\número", descrita abaixo. Para corresponder aos literais "'('" ou
"')'", use "\(" ou "\)", ou coloque-os dentro de uma classe de
caracteres: "[(]", "[)]".


"(?...)"
~~~~~~~~

Esta é uma notação de extensão (um "'?'" após um "'('" não é
significativo de outra forma). O primeiro caractere após o "'?'"
determina qual o significado e sintaxe posterior da construção. As
extensões normalmente não criam um novo grupo; "(?P<nome>...)" é a
única exceção a esta regra. A seguir estão as extensões atualmente
implementadas.


"(?aiLmsux)"
~~~~~~~~~~~~

(Uma ou mais letras do conjunto "'a'", "'i'", "'L'", "'m'", "'s'",
"'u'", "'x'".) O grupo corresponde à string vazia; as letras definem
os sinalizadores correspondentes para toda a expressão regular:

* "re.A" (correspondência somente ASCII)

* "re.I" (ignorar maiúsculas/minúsculas)

* "re.L" (dependente da localidade)

* "re.M" (multi-linha)

* "re.S" (ponto corresponde a tudo)

* "re.U" (correspondência Unicode)

* "re.X" (verboso)

(Os sinalizadores são descritos em Conteúdo do módulo.) Isso é útil se
você deseja incluir os sinalizadores como parte da expressão regular,
em vez de passar um argumento *flag* para a função "re.compile()". Os
sinalizadores devem ser usados primeiro na string de expressão.

Alterado na versão 3.11: Esta construção só pode ser usada no início
da expressão.


"(?:...)"
~~~~~~~~~

Uma versão de não-captura de parênteses regulares. Corresponde a
qualquer expressão regular que esteja entre parênteses, mas a
substring correspondida pelo grupo *não pode* ser recuperada após
realizar uma correspondência ou referenciada posteriormente no padrão.


"(?aiLmsux-imsx:...)"
~~~~~~~~~~~~~~~~~~~~~

(Zero ou mais letras do conjunto "'a'", "'i'", "'L'", "'m'", "'s'",
"'u'", "'x'", opcionalmente seguidas por "'-'" seguido por uma ou mais
letras do conjunto "'i'", "'m'", "'s'", "'x'".) O conjunto de letras
define ou remove os sinalizadores correspondentes para a parte da
expressão:

* "re.A" (correspondência somente ASCII)

* "re.I" (ignorar maiúsculas/minúsculas)

* "re.L" (dependente da localidade)

* "re.M" (multi-linha)

* "re.S" (ponto corresponde a tudo)

* "re.U" (correspondência Unicode)

* "re.X" (verboso)

(Os sinalizadores são descritos em Conteúdo do módulo.)

As letras "'a'", "'L'" e "'u'" são mutuamente exclusivas quando usadas
como sinalizadores em linha, portanto, não podem ser combinadas ou
seguir "'-'". Em vez disso, quando um deles aparece em um grupo
embutido, ele substitui o modo de correspondência no grupo anexo. Em
padrões Unicode "(?a:...)" muda para correspondência somente ASCII, e
"(?u:...)" muda para correspondência Unicode (padrão). Em padrões de
bytes "(?L:...)" muda para a correspondência dependente da localidade,
e "(?a:...)" muda para correspondência apenas ASCII (padrão). Esta
substituição só tem efeito para o grupo estreito em linha e o modo de
correspondência original é restaurado fora do grupo.

Adicionado na versão 3.6.

Alterado na versão 3.7: As letras "'a'", "'L'" e "'u'" também podem
ser usadas em um grupo.


"(?>...)"
~~~~~~~~~

Tenta corresponder "..." como se fosse uma expressão regular separada
e, se for bem-sucedida, continua correspondendo ao restante do padrão
que a segue. Se o padrão subsequente não corresponder, a pilha só pode
ser desenrolada até um ponto *antes* do "(?>...)" porque, uma vez
encerrada, a expressão, conhecida como *grupo atômico*, jogou fora
todos os pontos de pilha dentro de si. Assim, "(?>.*)." nunca
corresponderia a nada porque primeiro o ".*" corresponderia a todos os
caracteres possíveis, então, não tendo mais nada para corresponder, o
"." final falharia em corresponder. Como não há pontos de pilha salvos
no Grupo Atômico e não há ponto de pilha antes dele, a expressão
inteira não corresponderia.

Adicionado na versão 3.11.


"(?P<nome>...)"
~~~~~~~~~~~~~~~

Semelhante aos parênteses regulares, mas a substring correspondida
pelo grupo é acessível por meio do nome de grupo simbólico *nome*. Os
nomes de grupo devem ser identificadores Python válidos e em padrões
"bytes" eles só podem conter bytes no intervalo ASCII. Cada nome de
grupo deve ser definido apenas uma vez em uma expressão regular. Um
grupo simbólico também é um grupo numerado, como se o grupo não
tivesse um nome.

Grupos nomeados podem ser referenciados em três contextos. Se o padrão
for "(?P<citação>['"]).*?(?P=citação)" (ou seja, corresponder a uma
string entre aspas simples ou duplas):

+-----------------------------------------+------------------------------------+
| Contexto de referência ao grupo         | Formas de referenciá-lo            |
| "citação"                               |                                    |
|=========================================|====================================|
| no mesmo padrão                         | * "(?P=citação)" (como mostrado)   |
|                                         | * "\1"                             |
+-----------------------------------------+------------------------------------+
| ao processar a correspondência do       | * "m.group('citação')"  *          |
| objeto *m*                              | "m.end('citação')" (etc.)          |
+-----------------------------------------+------------------------------------+
| em uma string passada para o argumento  | * "\g<citação>"  * "\g<1>"  * "\1" |
| *repl* de "re.sub()"                    |                                    |
+-----------------------------------------+------------------------------------+

Alterado na versão 3.12: Nos padrões "bytes", o grupo *nome* só pode
conter bytes no intervalo ASCII ("b'\x00'"-"b'\x7f'").


"(?P=nome)"
~~~~~~~~~~~

Uma referência anterior a um grupo nomeado; corresponde a qualquer
texto que corresponda ao grupo anterior denominado *nome*.


"(?#...)"
~~~~~~~~~

Um comentário; o conteúdo dos parênteses é simplesmente ignorado.


"(?=...)"
~~~~~~~~~

Corresponde se "..." corresponder a próxima, mas não consome nada da
string. Isso é chamado de *asserção preditiva*. Por exemplo, "Isaac
(?=Asimov)" corresponderá a "'Isaac '" apenas se for seguido por
"'Asimov'".


"(?!...)"
~~~~~~~~~

Corresponde se "..." não corresponder a próxima. Isso é uma *asserção
preditiva negativa*. Por exemplo, "Isaac (?!Asimov)" corresponderá a
"'Isaac '" apenas se *não* for seguido por "'Asimov'".


"(?<=...)"
~~~~~~~~~~

Corresponde se a posição atual na string for precedida por uma
correspondência para "..." que termina na posição atual. Isso é
chamado de *asserção retroativa positiva*. "(?<=abc)def" irá encontrar
uma correspondência em "'abcdef'", uma vez que a expressão regular vai
voltar 3 caracteres e verificar se o padrão contido corresponde. O
padrão contido deve corresponder apenas a strings de algum comprimento
fixo, o que significa que "abc" ou "a|b" são permitidos, mas "a*" e
"a{3,4}" não são. Observe que os padrões que começam com asserções
retroativas positivas não corresponderão ao início da string que está
sendo pesquisada; você provavelmente desejará usar a função "search()"
em vez da função "match()":

>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'

Este exemplo procura por uma palavra logo após um hífen:

>>> m = re.search(r'(?<=-)\w+', 'spam-egg')
>>> m.group(0)
'egg'

Alterado na versão 3.5: Adicionado suporte para referências de grupo
de comprimento fixo.


"(?<!...)"
~~~~~~~~~~

Corresponde se a posição atual na string não for precedida por uma
correspondência para "...". Isso é chamado de *asserção retroativa
negativa*. Semelhante às asserções retroativas positivas, o padrão
contido deve corresponder apenas a strings de algum comprimento fixo.
Os padrões que começam com asserções retroativas negativas podem
corresponder ao início da string que está sendo pesquisada.


"(?(id/nome)padrão-sim|padrão-não)"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tentará corresponder com "padrão-sim" se o grupo com determinado *id*
ou *nome* existir, e com "padrão-não" se não existir. "padrão-não" é
opcional e pode ser omitido. Por exemplo,
"(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)" é um padrão ruim de correspondência
de e-mail, que corresponde a "'<usuario@host.com>'" e a
"'usuario@host.com'", mas não corresponde a "'<usuario@host.com'" nem
"'usuario@host.com>'" totalmente ("re.search()" só encontra
"'usuario@host.com'" no primeiro caso).

Alterado na versão 3.12: O grupo *id* só podem conter dígitos ASCII.
Nos padrões "bytes", o grupo *nome* só pode conter bytes no intervalo
ASCII ("b'\x00'"-"b'\x7f'").


Special sequences
-----------------

As sequências especiais consistem em "'\'" e um caractere da lista
abaixo. Se o caractere comum não for um dígito ASCII ou uma letra
ASCII, a ER resultante corresponderá ao segundo caractere. Por
exemplo, "\$" corresponde ao caractere "'$'".


"\número"
~~~~~~~~~

Corresponde ao conteúdo do grupo de mesmo número. Os grupos são
numerados a partir de 1. Por exemplo, "(.+) \1" corresponde a "'de
de'" ou "'55 55'", mas não "'dede'" (note o espaço após o grupo). Esta
sequência especial só pode ser usada para corresponder a um dos
primeiros 99 grupos. Se o primeiro dígito de *número* for 0, ou
*número* tiver 3 dígitos octais de comprimento, ele não será
interpretado como uma correspondência de grupo, mas como o caractere
com *número* de valor octal. Dentro de "'['" e "']'" de uma classe de
caracteres, todos os escapes numéricos são tratados como caracteres.


"\A"
~~~~

Corresponde apenas ao início da string.


"\b"
~~~~

Corresponde à string vazia, mas apenas no início ou no final de uma
palavra. Uma palavra é definida como uma sequência de caracteres de
palavras. Observe que, formalmente, "\b" é definido como a fronteira
entre um caractere "\w" e um "\W" (ou vice-versa), ou entre "\w" e o
início/fim da string. Isso significa que "r'\bat\b'" corresponde a
"'at'", "'at.'", "'(at)'", "'as at ay'", mas não a "'attempt'" ou
"'atlas'".

Os caracteres de palavras predefinidos em padrões Unicode (str) são
alfanuméricos Unicode e o sublinhado, mas isso pode ser alterado
usando o sinalizador "ASCII". Os limites das palavras são determinados
pela localidade atual se o sinalizador "LOCALE" for usado.

Nota:

  Dentro de um intervalo de caracteres, "\b" representa o caractere
  backspace, para compatibilidade com strings literais do Python.


"\B"
~~~~

Corresponde à string vazia, mas apenas quando *não* estiver no início
ou no final de uma palavra. Isso significa que "r'at\B'" corresponde a
"'athens'", "'atom'", "'attorney'", mas não "'at'", "'at.'" ou
"'at!'". "\B" é exatamente o oposto de "\b", então caracteres de
palavras em padrões Unicode são alfanuméricos Unicode ou o sublinhado,
embora isso possa ser alterado usando o sinalizador "ASCII". Os
limites das palavras são determinados pela localidade atual se o
sinalizador "LOCALE" for usado.

Alterado na versão 3.14: "\B" agora corresponde string de entrada
vazia.


"\d"
~~~~

Para padrões Unicode (str):
   Corresponde a qualquer dígito decimal Unicode (ou seja, qualquer
   caractere na categoria de caractere Unicode [Nd]). Isso inclui
   "[0-9]", e também muitos outros caracteres de dígitos.

   Se o sinalizador "ASCII" for usado, apenas "[0-9]" será
   correspondido.

Para padrões de 8 bits (isto é, bytes):
   Corresponde a qualquer dígito decimal no conjunto de caracteres
   ASCII; isso é equivalente a "[0-9]".


"\D"
~~~~

Corresponde a qualquer caractere que não seja um dígito decimal. Isso
é o oposto de "\d".

Se o sinalizador "ASCII" for usado, apenas "[^0-9]" será
correspondido.


"\s"
~~~~

Para padrões Unicode (str):
   Corresponde a caracteres de espaço em branco Unicode (como definido
   por "str.isspace()") . Isso inclui "[ \t\n\r\f\v]", e também muitos
   outros caracteres, como, por exemplo, os espaços não separáveis
   exigidos pelas regras de tipografia em muitos idiomas.

   Se o sinalizador  "ASCII" for usado, apenas "[ \t\n\r\f\v]" é
   correspondido.

Para padrões de 8 bits (isto é, bytes):
   Corresponde a caracteres considerados espaços em branco no conjunto
   de caracteres ASCII; isso é equivalente a "[ \t\n\r\f\v]".


"\S"
~~~~

Corresponde a qualquer caractere que não seja um espaço em branco.
Isso é o oposto de "\s".

Se o sinalizador  "ASCII" for usado, apenas "[^ \t\n\r\f\v]" é
correspondido.


"\w"
~~~~

Para padrões Unicode (str):
   Corresponde a caracteres de palavras Unicode; isso inclui todos os
   caracteres alfanuméricos Unicode (conforme definido por
   "str.isalnum()"), bem como o sublinhado ("_").

   Se o sinalizador "ASCII" for usado, apenas "[a-zA-Z0-9_]" será
   correspondido.

Para padrões de 8 bits (isto é, bytes):
   Corresponde a caracteres considerados alfanuméricos no conjunto de
   caracteres ASCII; isso é equivalente a "[a-zA-Z0-9_]". Se o
   sinalizador "LOCALE" for usado, corresponde aos caracteres
   considerados alfanuméricos na localidade atual e o sublinhado.


"\W"
~~~~

Corresponde a qualquer caractere que não seja um caractere de palavra.
Isso é o oposto de "\w". Por padrão, corresponde a caracteres que não
são sublinhados ("_") para os quais "str.isalnum()" retorna "False".

Se o sinalizador "ASCII" for usado, apenas "[^a-zA-Z0-9_]" será
correspondido.

Se o sinalizador "LOCALE" for usado, corresponde a caracteres que não
são alfanuméricos na localidade atual nem ao sublinhado.


"\z"
~~~~

Corresponde apenas ao final da string.

Adicionado na versão 3.14.


"\Z"
~~~~

O mesmo que "\z". Para compatibilidade com versões mais antigas de
Python.


Standard escapes
----------------

A maioria das sequências de escape com suporte das literais de string
Python também são aceitos pelo analisador sintático de expressão
regular:

   \a      \b      \f      \n
   \N      \r      \t      \u
   \U      \v      \x      \\

(Observe que "\b" é usado para representar limites de palavras e
significa fazer "backspace" apenas dentro das classes de caracteres.)

As sequências de escape "'\u'", "'\U'" e "'\N'" são reconhecidas
apenas em padrões Unicode (str). Em padrões de bytes, eles são erros.
Escapes desconhecidos de letras ASCII são reservados para uso futuro e
tratados como erros.

Os escapes octais são incluídos em um formulário limitado. Se o
primeiro dígito for 0, ou se houver três dígitos octais, é considerado
um escape octal. Caso contrário, é uma referência de grupo. Quanto aos
literais de string, os escapes octais têm sempre no máximo três
dígitos.

Alterado na versão 3.3: As sequências de escape "'\u'" e "'\U'" foram
adicionadas.

Alterado na versão 3.6: Escapes desconhecidos consistindo em "'\'" e
uma letra ASCII agora são erros.

Alterado na versão 3.8: A sequência de escape "'\N{*name*}'" foi
adicionada. Como em literais de string, ela se expande para o
caractere Unicode nomeado (por exemplo, "'\N{EM DASH}'").


Conteúdo do módulo
==================

O módulo define várias funções, constantes e uma exceção. Algumas das
funções são versões simplificadas dos métodos completos para
expressões regulares compiladas. A maioria das aplicações não triviais
sempre usa a forma compilada.


Sinalizadores
-------------

Alterado na versão 3.6: Constantes de sinalizadores agora são
instâncias de "RegexFlag", que é uma subclasse de "enum.IntFlag".

class re.RegexFlag

   Uma subclasse de "enum.IntFlag" contendo as opções de expressão
   regular listadas abaixo.

   Adicionado na versão 3.11: - added to "__all__"

re.A
re.ASCII

   Faz com que "\w", "\W", "\b", "\B", "\d", "\D", "\s" e "\S"
   executem a correspondência somente ASCII em vez da correspondência
   Unicode completa. Isso é significativo apenas para padrões Unicode
   (str) e é ignorado para padrões de bytes.

   Corresponde ao sinalizador em linha "(?a)".

   Nota:

     O sinalizador "U" ainda existe para compatibilidade com versões
     anteriores, mas é redundante no Python 3, pois as
     correspondências são feitas em Unicode por padrão para padrões de
     "str" e correspondência Unicode não é permitida para padrões de
     "bytes". "UNICODE" e o sinalizador em linha "(?u)" são igualmente
     redundantes.

re.DEBUG

   Exibe informações de depuração sobre a expressão compilada.

   Nenhum sinalizador em linha correspondente.

re.I
re.IGNORECASE

   Faz uma correspondência que não diferencia maiúsculas de
   minúsculas; expressões como "[A-Z]" também corresponderão a letras
   minúsculas. A correspondência Unicode completa (como "Ü"
   correspondendo a "ü") também funciona, a menos que o sinalizador
   "ASCII" seja usado para desabilitar correspondências não ASCII. A
   localidade atual não muda o efeito deste sinalizador a menos que o
   sinalizador "LOCALE" também seja usado.

   Corresponde ao sinalizador em linha "(?i)".

   Observe que quando os padrões Unicode "[a-z]" ou "[A-Z]" são usados
   em combinação com o sinalizador "IGNORECASE", eles corresponderão
   às 52 letras ASCII e 4 letras não-ASCII adicionais: 'İ' (U+0130,
   letra latina I maiúscula com ponto em cima), 'ı' (U+0131, letra
   latina i minúscula sem ponto), 'ſ' (U+017F, letra latina s
   minúscula longa) e 'K' (U+212A, sinal de Kelvin). Se o sinalizador
   "ASCII" for usado, apenas as letras 'a' a 'z' e 'A' a 'Z' serão
   correspondidas.

re.L
re.LOCALE

   Faz com que "\w", "\W", "\b", "\B" e a correspondência sem
   diferenciação de maiúsculas e minúsculas dependam da localidade
   atual. Esse sinalizador só pode ser usado com padrões de bytes.

   Corresponde ao sinalizador em linha "(?L)".

   Aviso:

     Este sinalizador é desencorajado; considere usar correspondência
     Unicode em vez disso. O mecanismo de localidade é muito pouco
     confiável, pois só manipula uma "cultura" por vez e só funciona
     com localidades de 8 bits. A correspondência Unicode é habilitada
     por padrão para padrões Unicode (str) e é capaz de manipular
     diferentes localidades e idiomas.

   Alterado na versão 3.6: "LOCALE" pode ser usado apenas com padrões
   de bytes e não é compatível com "ASCII".

   Alterado na versão 3.7: Objetos de expressão regular compilados com
   o sinalizador "LOCALE" não dependem mais da localidade em tempo de
   compilação. Apenas a localidade no momento da correspondência afeta
   o resultado da correspondência.

re.M
re.MULTILINE

   Quando especificado, o caractere padrão "'^'" corresponde ao início
   da string e ao início de cada linha (imediatamente após cada nova
   linha); e o caractere padrão "'$'" corresponde ao final da string e
   ao final de cada linha (imediatamente antes de cada nova linha).
   Por padrão, "'^'" corresponde apenas no início da string, e "'$'"
   apenas no final da string e imediatamente antes da nova linha (se
   houver) no final da string.

   Corresponde ao sinalizador em linha "(?m)".

re.NOFLAG

   Indica que nenhum sinalizador está sendo aplicado, o valor é "0".
   Este sinalizador pode ser usado como um valor padrão para um
   argumento nomeado de função ou como um valor base que será
   condicionalmente OU com outros sinalizadores. Exemplo de uso como
   valor padrão:

      def minha_func(padrão, texto, sinalizador=re.NOFLAG):
          return re.search(padrão, texto, sinalizador)

   Adicionado na versão 3.11.

re.S
re.DOTALL

   Faz o caractere especial "'.'" corresponder com qualquer caractere
   que seja, incluindo uma nova linha; sem este sinalizador, "'.'" irá
   corresponder a qualquer coisa, *exceto* uma nova linha.

   Corresponde ao sinalizador em linha "(?s)".

re.U
re.UNICODE

   Em Python 3, os caracteres Unicode são correspondidos por padrão
   para padrões "str". Esse sinalizador é, portanto, redundante e
   **sem efeito**, sendo mantido apenas para compatibilidade com
   versões anteriores.

   Veja "ASCII" para restringir a correspondência apenas a caracteres
   ASCII.

re.X
re.VERBOSE

   Este sinalizador permite que você escreva expressões regulares que
   parecem mais agradáveis e são mais legíveis, permitindo que você
   separe visualmente seções lógicas do padrão e adicione comentários.
   O espaço em branco dentro do padrão é ignorado, exceto quando em
   uma classe de caractere, ou quando precedido por uma contrabarra
   sem escape, ou dentro de tokens como "*?", "(?:" ou "(?P<...>". Por
   exemplo, "(? :" e "* ?" não são permitidos. Quando uma linha contém
   um "#" que não está em uma classe de caractere e não é precedido
   por uma contrabarra sem escape, todos os caracteres a partir do "#"
   mais à esquerda até o final da linha são ignorados.

   Isso significa que os dois seguintes objetos expressão regular que
   correspondem a um número decimal são funcionalmente iguais:

      a = re.compile(r"""\d +  # a parte inteira
                         \.    # o ponto decimal
                         \d *  # alguns digitos fracionários""", re.X)
      b = re.compile(r"\d+\.\d*")

   Corresponde ao sinalizador em linha "(?x)".


Funções
-------

re.compile(pattern, flags=0)

   Compila um padrão de expressão regular em um objeto expressão
   regular, que pode ser usado para correspondência usando seu
   "prefixmatch()", "search()" e outros métodos, descritos abaixo.

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

   A sequência

      prog = re.compile(pattern)
      result = prog.search(string)

   é equivalente a

      result = re.search(pattern, string)

   mas usar "re.compile()" e salvar o objeto expressão regular
   resultante para reutilização é mais eficiente quando a expressão
   será usada várias vezes em um único programa.

   Nota:

     As versões compiladas dos padrões mais recentes passados para
     "re.compile()" e as funções de correspondência em nível de módulo
     são armazenadas em cache, de modo que programas que usam apenas
     algumas expressões regulares por vez não precisam se preocupar em
     compilar expressões regulares.

re.search(pattern, string, flags=0)

   Percorre a *string* procurando o primeiro local onde o padrão
   *pattern* de expressão regular produz uma correspondência e retorna
   um "Match" correspondente. Retorna "None" se nenhuma posição na
   string corresponder ao padrão; observe que isso é diferente de
   encontrar uma correspondência de comprimento zero em algum ponto da
   string.

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

re.prefixmatch(pattern, string, flags=0)

   Se zero ou mais caracteres no início da *string* corresponderem ao
   padrão *pattern* da expressão regular, retorna um "Match"
   correspondente. Retorna "None" se a string não corresponder ao
   padrão; observe que isso é diferente de uma correspondência de
   comprimento zero.

   Nota:

     Mesmo no modo "MULTILINE", isso irá corresponder apenas no início
     da string e não no início de cada linha.

   Se você quiser localizar uma correspondência em qualquer lugar em
   *string*, use "search()" (veja também search() vs. prefixmatch()).

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

   Esta função agora possui dois nomes e é conhecida há muito tempo
   como "match()". Utilize esse nome quando precisar manter a
   compatibilidade com versões mais antigas do Python.

   Adicionado na versão 3.15.

re.match(pattern, string, flags=0)

   Suavemente descontinuado desde a versão 3.15: "match()" has been
   *soft deprecated* in favor of the alternate "prefixmatch()" name of
   this API which is more explicitly descriptive. Use it to better
   express intent. The norm in other languages and regular expression
   implementations is to use the term *match* to refer to the behavior
   of what Python has always called "search()". See prefixmatch() vs.
   match().

re.fullmatch(pattern, string, flags=0)

   Se toda a *string* corresponder ao padrão *pattern* da expressão
   regular, retorna um "Match" correspondente. Retorna "None" se a
   string não corresponder ao padrão; observe que isso é diferente de
   uma correspondência de comprimento zero.

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

   Adicionado na versão 3.4.

re.split(pattern, string, maxsplit=0, flags=0)

   Divide a *string* pelas ocorrências do padrão *pattern*. Se
   parênteses de captura forem usados em *pattern*, o texto de todos
   os grupos no padrão também será retornado como parte da lista
   resultante. Se *maxsplit* for diferente de zero, no máximo
   *maxsplit* divisões ocorrerão e o restante da string será retornado
   como o elemento final da lista.

      >>> re.split(r'\W+', 'Palavras, palavras, palavras.')
      ['Palavras', 'palavras', 'palavras', '']
      >>> re.split(r'(\W+)', 'Palavras, palavras, palavras.')
      ['Palavras', ', ', 'palavras', ', ', 'palavras', '.', '']
      >>> re.split(r'\W+', 'Palavras, palavras, palavras.', maxsplit=1)
      ['Palavras', 'palavras, palavras.']
      >>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
      ['0', '3', '9']

   Se houver grupos de captura no separador e ele corresponder ao
   início da string, o resultado começará com uma string vazia. O
   mesmo vale para o final da string:

      >>> re.split(r'(\W+)', '...palavras, palavras...')
      ['', '...', 'palavras', ', ', 'palavras', '...', '']

   Dessa forma, os componentes do separador são sempre encontrados nos
   mesmos índices relativos na lista de resultados.

   Correspondências vazias adjacentes não são possíveis, mas uma
   correspondência vazia pode ocorrer imediatamente após uma
   correspondência não-vazia.

      >>> re.split(r'\b', 'Palavras, palavras, palavras.')
      ['', 'Palavras', ', ', 'palavras', ', ', 'palavras', '.']
      >>> re.split(r'\W*', '...palavras...')
      ['', '', 'p', 'a', 'l', 'a', 'v', 'r', 'a', 's', '', '']
      >>> re.split(r'(\W*)', '...palavras...')
      ['', '...', '', '', 'p', '', 'a', '', 'l', '', 'a', '', 'v', '', 'r', '', 'a', '', 's', '...', '', '', '']

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

   Alterado na versão 3.1: Adicionado o argumento de sinalizadores
   opcionais.

   Alterado na versão 3.7: Adicionado suporte de divisão em um padrão
   que pode corresponder a uma string vazia.

   Descontinuado desde a versão 3.13: Passar *maxsplit* e *flags* como
   argumentos posicionais foi descontinuado. Nas versões futuras do
   Python eles serão parâmetros somente-nomeados.

re.findall(pattern, string, flags=0)

   Retorna todas as correspondências não sobrepostas do padrão
   *pattern* em *string*, como uma lista de strings ou tuplas. A
   *string* é verificada da esquerda para a direita e as
   correspondências são retornadas na ordem encontrada.
   Correspondências vazias são incluídas no resultado.

   O resultado depende do número de grupos de captura no padrão. Se
   não houver grupos, retorna uma lista de strings que correspondem a
   todo o padrão. Se houver exatamente um grupo, retorna uma lista de
   strings correspondentes a esse grupo. Se vários grupos estiverem
   presentes, retorna uma lista de tuplas de strings correspondentes
   aos grupos. Grupos de não-captura não afetam a forma do resultado.

   >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
   ['foot', 'fell', 'fastest']
   >>> re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
   [('width', '20'), ('height', '10')]

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

   Alterado na versão 3.7: Correspondências não vazias agora podem
   começar logo após uma correspondência vazia anterior.

re.finditer(pattern, string, flags=0)

   Retorna um *iterador* produzindo objetos "Match" sobre todas as
   correspondências não sobrepostas para o padrão *pattern* em
   *string*. A *string* é percorrida da esquerda para a direita e as
   correspondências são retornadas na ordem encontrada.
   Correspondências vazias são incluídas no resultado.

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

   Alterado na versão 3.7: Correspondências não vazias agora podem
   começar logo após uma correspondência vazia anterior.

re.sub(pattern, repl, string, count=0, flags=0)

   Retorna a string obtida substituindo as ocorrências não sobrepostas
   da extremidade esquerda do padrão *pattern* na *string* por *repl*.
   Se o padrão não for encontrado, *string* será retornado inalterado.
   *repl* pode ser uma string ou uma função; se for uma string,
   qualquer escape de contrabarra será processado. Ou seja, "\n" é
   convertido em um único caractere de nova linha, "\r" é convertido
   em um retorno de carro e assim por diante. Escapes desconhecidos de
   letras ASCII são reservados para uso futuro e tratados como erros.
   Outros escapes desconhecidos como "\&" são deixados como estão.
   Referências anteriores, como "\6", são substituídos pela substring
   correspondida pelo grupo 6 no padrão. Por exemplo:

      >>> re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
      ...        r'static PyObject*\npy_\1(void)\n{',
      ...        'def myfunc():')
      'static PyObject*\npy_myfunc(void)\n{'

   Se *repl* for uma função, ela será chamada para cada ocorrência não
   sobreposta do padrão *pattern*. A função recebe um único argumento
   "Match" e retorna a string de substituição. Por exemplo:

      >>> def dashrepl(matchobj):
      ...     if matchobj.group(0) == '-': return ' '
      ...     else: return '-'
      ...
      >>> re.sub('-{1,2}', dashrepl, 'arquivos-de-pro----grama')
      'arquivos de pro--grama'
      >>> re.sub(r'\sE\s', ' & ', 'Feijões queimados e spam', flags=re.IGNORECASE)
      'Feijões queimados & spam'

   O padrão pode ser uma string ou um "Pattern".

   O argumento opcional "count" é o número máximo de ocorrências do
   padrão a ser substituído; "count" deve ser um número inteiro não
   negativo. Se omitido ou igual a zero, todas as ocorrências serão
   substituídas.

   Correspondências vazias adjacentes não são possíveis, mas uma
   correspondência vazia pode ocorrer imediatamente após uma
   correspondência não-vazia. Como resultado, "sub('x*', '-', 'abxd')"
   retorna "'-a-b--d-'" invés de "'-a-b-d-'".

   Em argumentos *repl* do tipo string, além dos escapes de caractere
   e referências anteriores descritas acima, "\g<nome>" usará a
   substring correspondida pelo grupo denominado "nome", conforme
   definido pela sintaxe "(?P<nome>...)". "\g<número>" usa o número do
   grupo correspondente; "\g<2>" é portanto equivalente a "\2", mas
   não é ambíguo em uma substituição como "\g<2>0". "\20" seria
   interpretado como uma referência ao grupo 20, não uma referência ao
   grupo 2 seguida pelo caractere literal "'0'". A referência anterior
   "\g6" substitui em toda a substring correspondida pela ER.

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

   Alterado na versão 3.1: Adicionado o argumento de sinalizadores
   opcionais.

   Alterado na versão 3.5: Grupos sem correspondência são substituídos
   por uma string vazia.

   Alterado na versão 3.6: Escapes desconhecidos no padrão *pattern*
   consistindo em "'\'" e uma letra ASCII agora são erros.

   Alterado na versão 3.7: Escapes desconhecidos em *repl* consistindo
   em "'\'" e uma letra ASCII agora são erros. Uma correspondência
   vazia pode ocorrer imediatamente após uma correspondência não-
   vazia.

   Alterado na versão 3.12: O grupo *id* só pode conter dígitos ASCII.
   Nas strings de substituição "bytes", o grupo *name* só pode conter
   bytes no intervalo ASCII ("b'\x00'"-"b'\x7f'").

   Descontinuado desde a versão 3.13: Passar *count* e *flags* como
   argumentos posicionais foi descontinuado. Nas versões futuras do
   Python eles serão parâmetros somente-nomeados.

re.subn(pattern, repl, string, count=0, flags=0)

   Executa a mesma operação que "sub()", mas retorna uma tupla
   "(nova_string, número_de_substituições_feitas)".

   O comportamento da expressão pode ser modificado especificando um
   valor para o parâmetro *flags*. Os valores podem ser qualquer um
   dos sinalizadores, combinados usando OU bit a bit (o operador "|").

re.escape(pattern)

   Escapa caracteres especiais no padrão *pattern*. Isso é útil se
   você deseja corresponder uma string literal arbitrária que pode
   conter metacaracteres de expressão regular. Por exemplo:

      >>> print(re.escape('https://www.python.org'))
      https://www\.python\.org

      >>> legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
      >>> print('[%s]+' % re.escape(legal_chars))
      [abcdefghijklmnopqrstuvwxyz0123456789!\#\$%\&'\*\+\-\.\^_`\|\~:]+

      >>> operators = ['+', '-', '*', '/', '**']
      >>> print('|'.join(map(re.escape, sorted(operators, reverse=True))))
      /|\-|\+|\*\*|\*

   Esta função não deve ser usada para a string de substituição em
   "sub()" e "subn()", apenas contrabarras devem ser escapadas. Por
   exemplo:

      >>> digits_re = r'\d+'
      >>> sample = '/usr/sbin/sendmail - 0 errors, 12 warnings'
      >>> print(re.sub(digits_re, digits_re.replace('\\', r'\\'), sample))
      /usr/sbin/sendmail - \d+ errors, \d+ warnings

   Alterado na versão 3.3: O caractere "'_'" não é mais escapado.

   Alterado na versão 3.7: Somente caracteres que podem ter um
   significado especial em uma expressão regular são escapados. Como
   resultado, "'!'", "'"'", "'%'", ""'"", "','", "'/'", "':'", "';'",
   "'<'", "'='", "'>'", "'@'", e ""`"" não são mais escapados.

re.purge()

   Limpa o cache da expressão regular.


Exceções
--------

exception re.PatternError(msg, pattern=None, pos=None)

   Exceção levantada quando uma string passada para uma das funções
   desde módulo não é uma expressão regular válida (por exemplo, ela
   pode conter parênteses não correspondentes) ou quando algum outro
   erro ocorre durante a compilação ou correspondência. Nunca é um
   erro se uma string não contém correspondência para um padrão. A
   instância de "PatternError" possui os seguintes atributos
   adicionais:

   msg

      A mensagem de erro não formatada.

   pattern

      O padrão da expressão regular.

   pos

      O índice no padrão *pattern* no qual a compilação falhou (pode
      ser "None").

   lineno

      A linha correspondente a *pos* (pode ser "None").

   colno

      A coluna correspondente a *pos* (pode ser "None").

   Alterado na versão 3.5: Adicionados os atributos adicionais.

   Alterado na versão 3.13: "PatternError" era originalmente chamado
   de "error"; o último é mantido como um apelido para compatibilidade
   com versões anteriores.


Regular expression objects
==========================

class re.Pattern

   Objeto expressão regular compilado retornado por "re.compile()".

   Patterns are generic over the type of string they handle ("str" or
   "bytes").

   Alterado na versão 3.9: "re.Pattern" tem suporte a "[]" para
   indicar um padrão Unicode (str) ou bytes. Veja Tipo Generic Alias.

Pattern.search(string[, pos[, endpos]])

   Percorre a *string* procurando o primeiro local onde esta expressão
   regular produz uma correspondência e retorna um "Match"
   correspondente. Retorna "None" se nenhuma posição na string
   corresponder ao padrão; observe que isso é diferente de encontrar
   uma correspondência de comprimento zero em algum ponto da string.

   O segundo parâmetro opcional *pos* fornece um índice na string onde
   a pesquisa deve começar; o padrão é "0". Isso não é totalmente
   equivalente a fatiar a string; o caractere padrão "'^'" corresponde
   no início real da string e nas posições logo após uma nova linha,
   mas não necessariamente no índice onde a pesquisa deve começar.

   O parâmetro opcional *endpos* limita o quão longe a string será
   pesquisada; será como se a string tivesse *endpos* caracteres,
   então apenas os caracteres de *pos* a "endpos - 1" serão procurados
   por uma correspondência. Se *endpos* for menor que *pos*, nenhuma
   correspondência será encontrada; caso contrário, se *rx* é um
   objeto de expressão regular compilado, "rx.search(string, 0, 50)" é
   equivalente a "rx.search(string[:50], 0)".

      >>> pattern = re.compile("d")
      >>> pattern.search("dog")     # Correspondeu no índice 0
      <re.Match object; span=(0, 1), match='d'>
      >>> pattern.search("dog", 1)  # Não correspondeu; a busca não inclui "d"

Pattern.prefixmatch(string[, pos[, endpos]])

   Se zero ou mais caracteres no início da *string* corresponderem a
   esta expressão regular, retorna um "Match" correspondente. Retorna
   "None" se a string não corresponder ao padrão; observe que isso é
   diferente de uma correspondência de comprimento zero.

   Note that even in "MULTILINE" mode, this will only match at the
   beginning of the string and not at the beginning of each line.

   Os parâmetros opcionais *pos* e *endpos* têm o mesmo significado
   que para o método "search()".

      >>> pattern = re.compile("o")
      >>> pattern.prefixmatch("dog")     # No match as "o" is not at the start of "dog".
      >>> pattern.prefixmatch("dog", 1)  # Match as "o" is the 2nd character of "dog".
      <re.Match object; span=(1, 2), match='o'>

   Se você quiser localizar uma correspondência em qualquer lugar em
   *string*, use "search()" ao invés (veja também search() vs.
   prefixmatch()).

   This method now has two names and has long been known as "match()".
   Use that name when you need to retain compatibility with older
   Python versions.

   Adicionado na versão 3.15.

Pattern.match(string[, pos[, endpos]])

   Suavemente descontinuado desde a versão 3.15: "match()" has been
   *soft deprecated* in favor of the alternate "prefixmatch()" name of
   this API which is more explicitly descriptive. Use it to better
   express intent. The norm in other languages and regular expression
   implementations is to use the term *match* to refer to the behavior
   of what Python has always called "search()". See prefixmatch() vs.
   match().

Pattern.fullmatch(string[, pos[, endpos]])

   Se toda a *string* corresponder a esta expressão regular, retorna
   um "Match" correspondente. Retorna "None" se a string não
   corresponder ao padrão; observe que isso é diferente de uma
   correspondência de comprimento zero.

   Os parâmetros opcionais *pos* e *endpos* têm o mesmo significado
   que para o método "search()".

      >>> pattern = re.compile("o[gh]")
      >>> pattern.fullmatch("dog")      # Não correspondeu, pois "o" não é o início de "dog".
      >>> pattern.fullmatch("ogre")     # Não correspondeu, pois não é uma correspondência da string inteira.
      >>> pattern.fullmatch("doggie", 1, 3)   # Corresponde dentro dos limites dados.
      <re.Match object; span=(1, 3), match='og'>

   Adicionado na versão 3.4.

Pattern.split(string, maxsplit=0)

   Idêntico à função "split()", usando o padrão compilado.

Pattern.findall(string[, pos[, endpos]])

   Semelhante à função "findall()", usando o padrão compilado, mas
   também aceita os parâmetros *pos* e *endpos* opcionais que limitam
   a região de pesquisa como para "search()".

Pattern.finditer(string[, pos[, endpos]])

   Semelhante à função "finditer()", usando o padrão compilado, mas
   também aceita os parâmetros *pos* e *endpos* opcionais que limitam
   a região de pesquisa como para "search()".

Pattern.sub(repl, string, count=0)

   Idêntico à função "sub()", usando o padrão compilado.

Pattern.subn(repl, string, count=0)

   Idêntico à função "subn()", usando o padrão compilado.

Pattern.flags

   Os sinalizadores de correspondência de expressões regulares. Esta é
   uma combinação dos sinalizadores fornecidos para "compile()",
   qualquer  sinalizador em linha "(?...)" no padrão e sinalizadores
   implícitos como "UNICODE" se o padrão for uma string Unicode.

Pattern.groups

   O número de grupos de captura no padrão.

Pattern.groupindex

   Um dicionário que mapeia qualquer nome de grupo simbólico definido
   por "(?P<id>)" para números de grupo. O dicionário estará vazio se
   nenhum grupo simbólico for usado no padrão.

Pattern.pattern

   A string de padrão da qual o objeto de padrão foi compilado.

Alterado na versão 3.7: Adicionado suporte de "copy.copy()" e
"copy.deepcopy()". Os objetos expressão regular compilados são
considerados atômicos.


Match objects
=============

Objetos correspondência sempre têm um valor booleano de "True". Como
"match()" e "search()" retornam "None" quando não há correspondência,
você pode testar se houve uma correspondência com uma simples
instrução "if":

   if match := re.search(pattern, string):
       process(match)

class re.Match

   Objeto correspondência retornado por "match"s e "search"s bem
   sucedidos.

   Matches are generic over the type of string which was matched
   ("str" or "bytes").

   Alterado na versão 3.9: "re.Match" tem suporte a "[]" para indicar
   uma correspondência Unicode (str) ou bytes. Veja Tipo Generic
   Alias.

Match.expand(template)

   Retorna a string obtida fazendo a substituição da contrabarra na
   string template *template*, como feito pelo método "sub()". Escapes
   como "\n" são convertidos para os caracteres apropriados, e
   referências anteriores numéricas ("\1", "\2") e referências
   anteriores nomeadas ("\g<1>", "\g<nome>") são substituídas pelo
   conteúdo do grupo correspondente. A referência anterior "\g<0>"
   será substituída pela correspondência completa.

   Alterado na versão 3.5: Grupos sem correspondência são substituídos
   por uma string vazia.

Match.group([group1, ...])

   Returns one or more subgroups of the match.  If there is a single
   argument, the result is a single string; if there are multiple
   arguments, the result is a tuple with one item per argument.
   Without arguments, *group1* defaults to zero (the whole match is
   returned). If a *groupN* argument is zero, the corresponding return
   value is the entire matching string; if it is a positive integer,
   it is the string matching the corresponding parenthesized group.
   If a group number is negative or larger than the number of groups
   defined in the pattern, an "IndexError" exception is raised. If a
   group is contained in a part of the pattern that did not match, the
   corresponding result is "None". If a group is contained in a part
   of the pattern that matched multiple times, the last match is
   returned.

      >>> m = re.search(r"\A(\w+) (\w+)", "Norwegian Blue, pining for the fjords")
      >>> m.group(0)       # The entire match
      'Norwegian Blue'
      >>> m.group(1)       # The first parenthesized subgroup.
      'Norwegian'
      >>> m.group(2)       # The second parenthesized subgroup.
      'Blue'
      >>> m.group(1, 2)    # Multiple arguments give us a tuple.
      ('Norwegian', 'Blue')

   Se a expressão regular usa a sintaxe "(?P<nome>...)", os argumentos
   *groupN* também podem ser strings que identificam grupos por seus
   nomes de grupo. Se um argumento string não for usado como um nome
   de grupo no padrão, uma exceção "IndexError" é levantada.

   Um exemplo moderadamente complicado:

      >>> m = re.search(r"(?P<adjective>\w+) (?P<animal>\w+)", "killer rabbit")
      >>> m.group('adjective')
      'killer'
      >>> m.group('animal')
      'rabbit'

   Grupos nomeados também podem ser referidos por seu índice:

      >>> m.group(1)
      'killer'
      >>> m.group(2)
      'rabbit'

   Se um grupo corresponder várias vezes, apenas a última
   correspondência estará acessível:

      >>> m = re.search(r"(..)+", "a1b2c3")  # Matches 3 times.
      >>> m.group(1)                         # Returns only the last match.
      'c3'

Match.__getitem__(g)

   Isso é idêntico a "m.group(g)". Isso permite acesso mais fácil a um
   grupo individual de uma correspondência:

      >>> m = re.search(r"(\w+) (\w+)", "Norwegian Blue, pining for the fjords")
      >>> m[0]       # The entire match
      'Norwegian Blue'
      >>> m[1]       # The first parenthesized subgroup.
      'Norwegian'
      >>> m[2]       # The second parenthesized subgroup.
      'Blue'

   Também há suporte para grupos nomeados:

      >>> m = re.search(r"(?P<adjective>\w+) (?P<animal>\w+)", "killer rabbit")
      >>> m['adjective']
      'killer'
      >>> m['animal']
      'rabbit'

   Adicionado na versão 3.6.

Match.groups(default=None)

   Retorna uma tupla contendo todos os subgrupos da correspondência,
   de 1 até quantos grupos estiverem no padrão. O argumento *default*
   é usado para grupos que não participaram da correspondência; o
   padrão é "None".

   Por exemplo:

      >>> m = re.search(r"(\d+)\.(\d+)", "24.1632")
      >>> m.groups()
      ('24', '1632')

   Se colocarmos a casa decimal e tudo depois dela opcional, nem todos
   os grupos podem participar da correspondência. Esses grupos serão
   padronizados como "None", a menos que o argumento *default* seja
   fornecido:

      >>> m = re.search(r"(\d+)\.?(\d+)?", "24")
      >>> m.groups()      # Second group defaults to None.
      ('24', None)
      >>> m.groups('0')   # Now, the second group defaults to '0'.
      ('24', '0')

Match.groupdict(default=None)

   Retorna um dicionário contendo todos os subgrupos *nomeados* da
   correspondência, tendo como chave o nome do subgrupo. O argumento
   *default* usado para grupos que não participaram da
   correspondência; o padrão é "None". Por exemplo:

      >>> m = re.search(r"(?P<adjective>\w+) (?P<animal>\w+)", "killer rabbit")
      >>> m.groupdict()
      {'adjective': 'killer', 'animal': 'rabbit'}

Match.start([group])
Match.end([group])

   Retorna os índices de início e fim da substring correspondida pelo
   grupo *group*; *group* tem como padrão  zero (o que significa que
   toda a substring é correspondida). Retorna "-1" se *group* existe,
   mas não contribuiu para a correspondência. Para um objeto
   correspondência *m* e um grupo *g* que contribuiu para a
   correspondência, a substring correspondida pelo grupo *g*
   (equivalente a "m.group(g)") é

      m.string[m.start(g):m.end(g)]

   Observe que "m.start(group)" será igual a "m.end(group)" se *group*
   correspondeu a uma string nula. Por exemplo, após "m =
   re.search('b(c?)', 'cba')", "m.start(0)" é 1, "m.end(0)" é 2,
   "m.start(1)" e "m.end(1)" são 2, e "m.start(2)" levanta uma exceção
   "IndexError".

   Um exemplo que removerá *remova_isto* dos endereços de e-mail:

      >>> email = "tony@tiremova_istoger.net"
      >>> m = re.search("remova_isto", email)
      >>> email[:m.start()] + email[m.end():]
      'tony@tiger.net'

Match.span([group])

   Para uma correspondência *m*, retorna a tupla com dois elementos
   "(m.start(group), m.end(group))". Observe que se *group* não
   contribuiu para a correspondência, isso é "(-1, -1)". *group* tem
   como padrão zero, a correspondência inteira.

Match.pos

   O valor de *pos* que foi passado para o método "search()" ou
   "match()" de um objeto expressão regular. Este é o índice da string
   na qual o mecanismo de ER começou a procurar uma correspondência.

Match.endpos

   O valor de *endpos* que foi passado para o método "search()" ou
   "match()" de um objeto expressão regular. Este é o índice da string
   após o qual o mecanismo de ER não vai chegar.

Match.lastindex

   O índice em número inteiro do último grupo de captura
   correspondido, ou "None" se nenhum grupo foi correspondido. Por
   exemplo, as expressões "(a)b", "((a)(b))" e "((ab))" terão
   "lastindex == 1" se aplicadas à string "'ab'", enquanto a expressão
   "(a)(b)" terá "lastindex == 2", se aplicada à mesma string.

Match.lastgroup

   O nome do último grupo de captura correspondido, ou "None" se o
   grupo não tinha um nome, ou se nenhum grupo foi correspondido.

Match.re

   O objeto expressão regular cujo método "match()" ou "search()"
   produziu esta instância de correspondência.

Match.string

   A string passada para "match()" ou "search()".

Alterado na versão 3.7: Adicionado suporte para "copy.copy()" e
"copy.deepcopy()". Objetos correspondência são considerados atômicos.


Regular expression examples
===========================


Checking for a pair
-------------------

Neste exemplo, usaremos a seguinte função auxiliar para exibir objetos
correspondência com um pouco mais de elegância:

   def displaymatch(match):
       if match is None:
           return None
       return '<Match: %r, groups=%r>' % (match.group(), match.groups())

Suponha que você esteja escrevendo um programa de pôquer onde a mão de
um jogador é representada como uma string de 5 caracteres com cada
caractere representando uma carta, "a" para ás, "k" para rei, "q" para
dama, "j" para valete, "t" para 10 e "2" a "9" representando a carta
com esse valor.

Para ver se uma determinada string é uma mão válida, pode-se fazer o
seguinte:

   >>> valid_hand_re = re.compile(r"^[a2-9tjqk]{5}$")
   >>> displaymatch(valid_hand_re.search("akt5q"))  # Valid.
   "<Match: 'akt5q', groups=()>"
   >>> displaymatch(valid_hand_re.search("akt5e"))  # Invalid.
   >>> displaymatch(valid_hand_re.search("akt"))    # Invalid.
   >>> displaymatch(valid_hand_re.search("727ak"))  # Valid.
   "<Match: '727ak', groups=()>"

Essa última mão, ""727ak"", continha um par, ou duas cartas com o
mesmo valor. Para combinar isso com uma expressão regular, pode-se
usar referências anteriores como:

   >>> pair_re = re.compile(r".*(.).*\1")
   >>> displaymatch(pair_re.prefixmatch("717ak"))     # Pair of 7s.
   "<Match: '717', groups=('7',)>"
   >>> displaymatch(pair_re.prefixmatch("718ak"))     # No pairs.
   >>> displaymatch(pair_re.prefixmatch("354aa"))     # Pair of aces.
   "<Match: '354aa', groups=('a',)>"

Para descobrir em que carta o par consiste, pode-se usar o método
"group()" do objeto correspondência da seguinte maneira:

   >>> pair_re = re.compile(r".*(.).*\1")
   >>> pair_re.prefixmatch("717ak").group(1)
   '7'

   # Error because prefixmatch() returns None, which doesn't have a group() method:
   >>> pair_re.prefixmatch("718ak").group(1)
   Traceback (most recent call last):
     File "<pyshell#23>", line 1, in <module>
       pair_re.prefixmatch("718ak").group(1)
   AttributeError: 'NoneType' object has no attribute 'group'

   >>> pair_re.prefixmatch("354aa").group(1)
   'a'


Simulando scanf()
-----------------

Atualmente, Python não possui um equivalente a "scanf()". Expressões
regulares são geralmente mais poderosas, embora também mais prolixas,
do que strings de formato "scanf()". A tabela abaixo oferece alguns
mapeamentos mais ou menos equivalentes entre strings de formato
"scanf()" e expressões regulares.

+----------------------------------+-----------------------------------------------+
| Símbolo do "scanf()"             | Expressão regular                             |
|==================================|===============================================|
| "%c"                             | "."                                           |
+----------------------------------+-----------------------------------------------+
| "%5c"                            | ".{5}"                                        |
+----------------------------------+-----------------------------------------------+
| "%d"                             | "[-+]?\d+"                                    |
+----------------------------------+-----------------------------------------------+
| "%e", "%E", "%f", "%g"           | "[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?"     |
+----------------------------------+-----------------------------------------------+
| "%i"                             | "[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)"         |
+----------------------------------+-----------------------------------------------+
| "%o"                             | "[-+]?[0-7]+"                                 |
+----------------------------------+-----------------------------------------------+
| "%s"                             | "\S+"                                         |
+----------------------------------+-----------------------------------------------+
| "%u"                             | "\d+"                                         |
+----------------------------------+-----------------------------------------------+
| "%x", "%X"                       | "[-+]?(0[xX])?[\dA-Fa-f]+"                    |
+----------------------------------+-----------------------------------------------+

To extract the filename and numbers from a string like:

   /usr/sbin/sendmail - 0 errors, 4 warnings

you would use a "scanf()" format like:

   %s - %d errors, %d warnings

The equivalent regular expression would be:

   (\S+) - (\d+) errors, (\d+) warnings


search() vs. prefixmatch()
--------------------------

Python oferece diferentes operações primitivas baseadas em expressões
regulares:

* "re.prefixmatch()" checks for a match only at the beginning of the
  string

* "re.search()" verifica uma correspondência em qualquer lugar na
  string (isso é o que o Perl faz por padrão)

* "re.fullmatch()" verifica toda a string para ser uma correspondência

Por exemplo:

   >>> re.prefixmatch("c", "abcdef")  # No match
   >>> re.search("c", "abcdef")       # Match
   <re.Match object; span=(2, 3), match='c'>
   >>> re.fullmatch("p.*n", "python") # Match
   <re.Match object; span=(0, 6), match='python'>
   >>> re.fullmatch("r.*n", "python") # No match

Expressões regulares começando com "'^'" podem ser usadas com
"search()" para restringir a correspondência no início da string:

   >>> re.prefixmatch("c", "abcdef")  # No match
   >>> re.search("^c", "abcdef")      # No match
   >>> re.search("^a", "abcdef")      # Match
   <re.Match object; span=(0, 1), match='a'>

Note however that in "MULTILINE" mode "prefixmatch()" only matches at
the beginning of the string, whereas using "search()" with a regular
expression beginning with "'^'" will match at the beginning of each
line.

   >>> re.prefixmatch("X", "A\nB\nX", re.MULTILINE)  # No match
   >>> re.search("^X", "A\nB\nX", re.MULTILINE)  # Match
   <re.Match object; span=(4, 5), match='X'>


prefixmatch() vs. match()
-------------------------

Why is the "match()" function and method discouraged in favor of the
longer "prefixmatch()" spelling?

Many other languages have gained regex support libraries since regular
expressions were added to Python. However in the most popular of
those, they use the term *match* in their APIs to mean the unanchored
behavior provided in Python by "search()". Thus use of the plain term
*match* can be unclear to those used to other languages when reading
or writing code and not familiar with the Python API's divergence from
what otherwise become the industry norm.

Quoting from the Zen Of Python ("python3 -m this"): *"Explicit is
better than implicit"*. Anyone reading the name "prefixmatch()" is
likely to understand the intended semantics. When reading "match()"
there remains a seed of doubt about the intended behavior to anyone
not already familiar with this old Python gotcha.

We **do not** plan to remove the older "match()" name, as it has been
used in code for over 30 years. It has been *soft deprecated*: code
supporting older versions of Python should continue to use "match()",
while new code should prefer "prefixmatch()".

Adicionado na versão 3.15: "prefixmatch()"

Suavemente descontinuado desde a versão 3.15: "match()"


Making a phonebook
------------------

"split()" divide uma string em uma lista delimitada pelo padrão
passado. O método é inestimável para converter dados textuais em
estruturas de dados que podem ser facilmente lidas e modificadas pelo
Python, conforme demonstrado no exemplo a seguir que cria uma lista
telefônica.

Primeiro, aqui está a entrada. Normalmente pode vir de um arquivo,
aqui estamos usando a sintaxe de string entre aspas triplas.

   >>> texto = """Ross McFluff: 834.345.1254 155 Elm Street
   ...
   ... Ronald Heathmore: 892.345.3428 436 Finley Avenue
   ... Frank Burger: 925.541.7625 662 South Dogwood Way
   ...
   ...
   ... Heather Albrecht: 548.326.4584 919 Park Place"""

Os registros são separados por uma ou mais novas linhas. Agora,
convertemos a string em uma lista com cada linha não vazia tendo seu
próprio registro:

   >>> registros = re.split("\n+", texto)
   >>> registros
   ['Ross McFluff: 834.345.1254 155 Elm Street',
   'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
   'Frank Burger: 925.541.7625 662 South Dogwood Way',
   'Heather Albrecht: 548.326.4584 919 Park Place']

Finalmente, divida cada registro em uma lista com nome, sobrenome,
número de telefone e endereço. Usamos o parâmetro "maxsplit" de
"split()" porque o endereço contém espaços, nosso padrão de divisão:

   >>> [re.split(":? ", registro, maxsplit=3) for registro in registros]
   [['Ross', 'McFluff', '834.345.1254', '155 Elm Street'],
   ['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'],
   ['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'],
   ['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]

O padrão ":?" corresponde ao caractere de dois pontos após o
sobrenome, de modo que não ocorre na lista de resultados. Com um
"maxsplit" de "4", podemos separar o número da casa do nome da rua:

   >>> [re.split(":? ", registro, maxsplit=4) for registro in registros]
   [['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'],
   ['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'],
   ['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'],
   ['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']]


Text munging
------------

"sub()" substitui cada ocorrência de um padrão por uma string ou o
resultado de uma função. Este exemplo demonstra o uso de "sub()" com
uma função para "mastigar" o texto ou aleatorizar a ordem de todos os
caracteres em cada palavra de uma frase, exceto o primeiro e o último
caracteres:

   >>> def repl(m):
   ...     inner_word = list(m.group(2))
   ...     random.shuffle(inner_word)
   ...     return m.group(1) + "".join(inner_word) + m.group(3)
   ...
   >>> text = "Professor Masanori, favor comunicar suas ausências imediatamente."
   >>> re.sub(r"(\w)(\w+)(\w)", repl, text)
   'Psesforor Mranoasi, favor cmounacir suas acaêiusns idaaeemttnmie.'
   >>> re.sub(r"(\w)(\w+)(\w)", repl, text)
   'Prfseosor Monsaari, fovar camonucir saus acuêsains ientdaammetie.'


Finding all adverbs
-------------------

"findall()" corresponde *todas* as ocorrências de um padrão, não
apenas a primeira como "search()" faz. Por exemplo, se uma pessoa
deseja encontrar todos os advérbios em algum texto, ela pode usar
"findall()" da seguinte maneira:

   >>> text = "Ele estava cuidadosamente disfarçado, mas foi rapidamente capturado pela polícia."
   >>> re.findall(r"\w+mente\b", text)
   ['cuidadosamente', 'rapidamente']


Finding all adverbs and their positions
---------------------------------------

Se alguém deseja obter mais informações sobre todas as
correspondências de um padrão além do texto correspondido,
"finditer()" é útil, pois fornece objetos "Match" em vez de strings.
Continuando com o exemplo anterior, se um escritor quisesse encontrar
todos os advérbios *e suas posições* em algum texto, ele usaria
"finditer()" da seguinte maneira:

   >>> text = "Ele estava cuidadosamente disfarçado, mas foi rapidamente capturado pela polícia."
   >>> for m in re.finditer(r"\w+mente\b", text):
   ... print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
   11-25: cuidadosamente
   46-57: rapidamente


Raw string notation
-------------------

A notação de string bruta ("r"texto"") mantém as expressões regulares
sãs. Sem ela, cada contrabarra ("'\'") em uma expressão regular teria
que ser prefixada com outra para ter seu efeito de caractere especial
anulado. Por exemplo, as duas linhas de código a seguir são
funcionalmente idênticas:

   >>> re.search(r"\W(.)\1\W", " ff ")
   <re.Match object; span=(0, 4), match=' ff '>
   >>> re.search("\\W(.)\\1\\W", " ff ")
   <re.Match object; span=(0, 4), match=' ff '>

Quando se deseja corresponder a uma contrabarra literal, ela deve ser
prefixada com outra contrabarra na expressão regular. Com a notação de
string bruta, isso significa "r"\\"". Sem a notação de string bruta,
deve-se usar ""\\\\"", tornando as seguintes linhas de código
funcionalmente idênticas:

   >>> re.search(r"\\", r"\\")
   <re.Match object; span=(0, 1), match='\\'>
   >>> re.search("\\\\", r"\\")
   <re.Match object; span=(0, 1), match='\\'>


Writing a tokenizer
-------------------

Um tokenizador ou scanner analisa uma string para categorizar grupos
de caracteres. Este é um primeiro passo útil para escrever um
compilador ou interpretador.

As categorias de texto são especificadas com expressões regulares. A
técnica é combiná-las em uma única expressão regular mestre e fazer um
laço em correspondências sucessivas:

   from typing import NamedTuple
   import re

   class Token(NamedTuple):
       type: str
       value: int | float | str
       line: int
       column: int

   def tokenize(code):
       keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
       token_specification = [
           ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
           ('ASSIGN',   r':='),           # Assignment operator
           ('END',      r';'),            # Statement terminator
           ('ID',       r'[A-Za-z]+'),    # Identifiers
           ('OP',       r'[+\-*/]'),      # Arithmetic operators
           ('NEWLINE',  r'\n'),           # Line endings
           ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
           ('MISMATCH', r'.'),            # Any other character
       ]
       tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
       line_num = 1
       line_start = 0
       for mo in re.finditer(tok_regex, code):
           kind = mo.lastgroup
           value = mo.group()
           column = mo.start() - line_start
           if kind == 'NUMBER':
               value = float(value) if '.' in value else int(value)
           elif kind == 'ID' and value in keywords:
               kind = value
           elif kind == 'NEWLINE':
               line_start = mo.end()
               line_num += 1
               continue
           elif kind == 'SKIP':
               continue
           elif kind == 'MISMATCH':
               raise RuntimeError(f'{value!r} unexpected on line {line_num}')
           yield Token(kind, value, line_num, column)

   statements = '''
       IF quantity THEN
           total := total + price * quantity;
           tax := price * 0.05;
       ENDIF;
   '''

   for token in tokenize(statements):
       print(token)

O tokenizador produz a seguinte saída:

   Token(type='IF', value='IF', line=2, column=4)
   Token(type='ID', value='quantity', line=2, column=7)
   Token(type='THEN', value='THEN', line=2, column=16)
   Token(type='ID', value='total', line=3, column=8)
   Token(type='ASSIGN', value=':=', line=3, column=14)
   Token(type='ID', value='total', line=3, column=17)
   Token(type='OP', value='+', line=3, column=23)
   Token(type='ID', value='price', line=3, column=25)
   Token(type='OP', value='*', line=3, column=31)
   Token(type='ID', value='quantity', line=3, column=33)
   Token(type='END', value=';', line=3, column=41)
   Token(type='ID', value='tax', line=4, column=8)
   Token(type='ASSIGN', value=':=', line=4, column=12)
   Token(type='ID', value='price', line=4, column=15)
   Token(type='OP', value='*', line=4, column=21)
   Token(type='NUMBER', value=0.05, line=4, column=23)
   Token(type='END', value=';', line=4, column=27)
   Token(type='ENDIF', value='ENDIF', line=5, column=4)
   Token(type='END', value=';', line=5, column=9)

[Frie09] Friedl, Jeffrey. Mastering Regular Expressions. 3ª ed.,
         O'Reilly Media, 2009. A terceira edição do livro não cobre
         mais o Python, mas a primeira edição cobriu a escrita de bons
         padrões de expressão regular em grandes detalhes.
