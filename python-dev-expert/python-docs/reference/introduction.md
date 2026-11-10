1. Introdução
*************

Este manual de referência descreve a linguagem de programação Python.
O mesmo não tem como objetivo de ser um tutorial.

Enquanto estou tentando ser o mais preciso possível, optei por usar
especificações em inglês e não formal para tudo, exceto para a sintaxe
e análise léxica. Isso deve tornar o documento mais compreensível para
o leitor intermediário, mas deixará margem para ambiguidades.
Consequentemente, caso estivesses vindo de Marte e tentasse
reimplementar o Python a partir deste documento, sozinho, talvez
precisarias adivinhar algumas coisas e, na verdade, provavelmente
acabaria por implementar um linguagem bem diferente. Por outro lado,
se estiveres usando o Python e se perguntando quais são as regras
precisas sobre uma determinada área da linguagem, você definitivamente
encontrá neste documento o que estás procurando. Caso queiras ver uma
definição mais formal do linguagem, talvez possas oferecer seu tempo
-- ou inventar uma máquina de clonagem :-).

É perigoso adicionar muitos detalhes de implementação num documento de
referência de uma linguagem -- a implementação pode mudar e outras
implementações da mesma linguagem podem funcionar de forma diferente.
Por outro lado, o CPython é a única implementação de Python em uso de
forma generalizada (embora as implementações alternativas continuem a
ganhar suporte), e suas peculiaridades e particulares são por vezes
dignas de serem mencionadas, especialmente quando a implementação
impõe limitações adicionais. Portanto, encontrarás poucas "notas sobre
a implementação" espalhadas neste documento.

Cada implementação do Python vem com vários módulos embutidos e por
padrão. Estes estão documentados em A biblioteca padrão do Python.
Alguns módulos embutidos são mencionados ao interagirem de forma
significativa com a definição da linguagem.


1.1. Implementações Alternativas
================================

Embora exista uma implementação do Python que seja, de longe, a mais
popular, existem algumas implementações alternativas que são de de
interesse particular e para públicos diferentes.

As implementações conhecidas são:

CPython
   Esta é a implementação original e a é a versão do Python que mais
   vem sendo sendo desenvolvido e a mesma está escrita com a linguagem
   C. Novas funcionalidades ou recursos da linguagem aparecerão por
   aqui primeiro.

Jython
   Versão do Python implementado em Java. Esta implementação pode ser
   usada como linguagem de Script em aplicações Java, ou pode ser
   usada para criar aplicativos usando as bibliotecas das classes do
   Java. Também vem sendo bastante utilizado para criar testes
   unitários para as bibliotecas do Java. Mais informações podem ser
   encontradas no the Jython website.

Python for .NET
   Essa implementação utiliza de fato a implementação CPython, mas é
   uma aplicação gerenciada .NET e disponibilizada como uma
   bibliotecas .NET. Foi desenvolvida por Brian Lloyd. Para obter mais
   informações, consulte o site do Python for .NET.

IronPython
   Um versão alternativa do Python para a plataforma .NET. Ao
   contrário do Python.NET, esta é uma implementação completa do
   Python que gera IL e compila o código Python diretamente para
   assemblies .NET. Foi desenvolvida por Jim Hugunin, o criador
   original do Jython. Para obter mais informações, consulte o site do
   IronPython.

PyPy
   Uma implementação do Python escrita completamente em Python. A
   mesma suporta vários recursos avançados não encontrados em outras
   implementações, como suporte sem pilhas e um compilador Just in
   Time. Um dos objetivos do projeto é incentivar a construção de
   experimentos com a própria linguagem, facilitando a modificação do
   interpretador (uma vez que o mesmos está escrito em Python).
   Informações adicionais estão disponíveis no site do projeto PyPy.

Cada uma dessas implementações varia em alguma forma a linguagem
conforme documentado neste manual, ou introduz informações específicas
além do que está coberto na documentação padrão do Python. Consulte a
documentação específica da implementação para determinar o que é
necessário sobre a implementação específica que você está usando.


1.2. Notação
============

As descrições de análise lexical e sintaxe utilizam uma notação
gramatical que é uma mistura de EBNF e GASE (em inglês, PEG). Por
exemplo:

   name:   letter (letter | digit | "_")*
   letter: "a"..."z" | "A"..."Z"
   digit:  "0"..."9"

Neste exemplo, a primeira linha diz que um "name" é uma "letter"
seguida por uma sequência de zero ou mais "letter"s, "digit"s e
sublinhados. Uma "letter", por sua vez, é qualquer um dos caracteres
simples de "'a'" a "'z'" e de "A" a "Z"; um "digit" é um caractere
simples de "0" a "9".

Cada regra começa com um nome (que identifica a regra que está sendo
definida) seguido por caractere de dois pontos, ":". A definição à
direita dos dois pontos utiliza os seguintes elementos de sintaxe:

* "name": Um nome se refere a outra regra. Sempre que possível, é um
  link para a definição da regra.

  * "TOKEN": Um nome em maiúsculas refere-se a um *token*. Para fins
    de definições gramaticais, tokens são o mesmo que regras.

* ""text"", "'text'": O texto entre aspas simples ou duplas deve ser
  escrito literalmente (sem as aspas). O tipo de citação é escolhido
  de acordo com o significado de "text":

  * "'if'": Um nome entre aspas simples denota uma palavra reservada.

  * ""case"": Um nome entre aspas duplas denota uma palavra reservada
    contextual.

  * "'@'": Um símbolo que não seja uma letra entre aspas simples
    denota um token "OP", ou seja, um delimitador ou operador.

* "e1 e2": Itens separados apenas por espaços em branco denotam uma
  sequência. Aqui, "e1" deve ser seguido por "e2".

* "e1 | e2": Uma barra vertical é usada para separar alternativas. Ela
  denota a "escolha ordenada" do GASE: se "e1" corresponder, "e2" não
  é considerado. Nas gramáticas GASE tradicionais, isso é escrito como
  uma barra, "/", em vez de uma barra vertical. Veja **PEP 617** para
  mais informações e detalhes.

* "e*": Uma estrela significa zero ou mais repetições do item
  anterior.

* "e+": Da mesma forma, um mais significa uma ou mais repetições.

* "[e]": Uma frase entre colchetes significa zero ou uma ocorrência.
  Em outras palavras, a frase entre colchetes é opcional.

* "e?": Um ponto de interrogação tem exatamente o mesmo significado
  que colchetes: o item anterior é opcional.

* "(e)": Parênteses são usados para agrupamento.

A notação a seguir é usada somente em definições lexicais.

* ""a"..."z"": Dois caracteres literais separados por três pontos
  significam uma escolha de qualquer caractere único no intervalo
  fornecido (inclusive) de caracteres ASCII.

* "<...>": Uma frase entre parênteses angulares fornece uma descrição
  informal do símbolo correspondente (por exemplo, "<qualquer
  caractere ASCII, exceto "\">") ou uma abreviação definida no texto
  próximo (por exemplo, "<Lu>").

Algumas definições também usam *lookaheads*, que indicam que um
elemento deve (ou não) corresponder a uma determinada posição, mas sem
consumir nenhuma entrada:

* "&e": um lookahead positivo (ou seja, "e" é necessário para
  corresponder)

* "!e": um lookahead negativo (ou seja, "e" *não* é necessário para
  corresponder)

Os operadores unários ("*", "+", "?") vinculam-se o mais firmemente
possível; a barra vertical ("|") vincula-se de forma mais frouxa.

O espaço em branco só tem significado para separar tokens.

As regras normalmente ficam contidas em uma única linha, mas regras
muito longas podem ser encapsuladas:

   literal: stringliteral | bytesliteral
            | integer | floatnumber | imagnumber

Alternativamente, as regras podem ser formatadas com a primeira linha
terminando com dois pontos e cada alternativa começando com uma barra
vertical em uma nova linha. Por exemplo:

   literal:
      | stringliteral
      | bytesliteral
      | integer
      | floatnumber
      | imagnumber

Isso *não* significa que exista uma primeira alternativa vazia.


1.2.1. Definições lexicais e sintáticas
---------------------------------------

Há algumas diferenças entre a análise *léxica* e a *sintática*: o
*analisador léxico* opera nos caracteres individuais da fonte de
entrada, enquanto o *parser* (analisador sintático) opera no fluxo de
*tokens* gerados pela análise léxica. No entanto, em alguns casos, o
limite exato entre as duas fases é um detalhe da implementação do
CPython.

A diferença prática entre os dois é que, em definições *léxicas*,
todos os espaços em branco são significativos. O analisador léxico
descarta todos os espaços em branco que não são convertidos em tokens
como "token.INDENT" ou "NEWLINE". Definições *sintáticas* então usam
esses tokens, em vez dos caracteres de origem.

Esta documentação utiliza a mesma gramática BNF para ambos os estilos
de definição. Todos os usos de BNF no próximo capítulo (Análise
léxica) são definições lexicais; os usos nos capítulos subsequentes
são definições sintáticas.
