3. Uma introdução informal ao Python
************************************

Nos exemplos seguintes, pode-se distinguir entrada e saída pela
presença ou ausência dos prompts (*>>>* e *...*): para repetir o
exemplo, você deve digitar tudo após o prompt, quando o mesmo aparece;
linhas que não começarem com um prompt são na verdade as saídas
geradas pelo interpretador. Observe que quando aparece uma linha
contendo apenas o prompt secundário você deve digitar uma linha em
branco; é assim que se encerra um comando de múltiplas linhas.

Muitos exemplos neste manual, mesmo aqueles inscritos na linha de
comando interativa, incluem comentários. Comentários em Python começam
com o caractere cerquilha "#" e estende até o final da linha. Um
comentário pode aparecer no inicio da linha ou após espaço em branco
ou código, mas não dentro de uma string literal. O caractere cerquilha
dentro de uma string literal é apenas uma cerquilha. Como os
comentários são para esclarecer o código e não são interpretados pelo
Python, eles podem ser omitidos ao digitar exemplos.

Alguns exemplos:

   # este é o primeiro comentário
   spam = 1  # e este é o segundo comentário
             # ... e agora um terceiro!
   texto = "# Este não é um comentário por estar entre aspas."


3.1. Usando Python como uma calculadora
=======================================

Vamos experimentar alguns comandos simples em Python. Inicie o
interpretador e aguarde o prompt primário, ">>>". (Não deve demorar
muito.)


3.1.1. Números
--------------

O interpretador funciona como uma calculadora bem simples: você pode
digitar uma expressão nele e o resultado será apresentado. A sintaxe
de expressões é a usual: operadores "+", "-", "*" e "/" podem ser
usadas para realizar operações aritméticas; parênteses ("()") podem
ser usados para agrupar expressões. Por exemplo:

   >>> 2 + 2
   4
   >>> 50 - 5*6
   20
   >>> (50 - 5*6) / 4
   5.0
   >>> 8 / 5  # divisão sempre retorna um número de ponto flutuante
   1.6

Os números inteiros (por exemplo, "2", "4" e "20") são do tipo "int",
aqueles com parte fracionária (por exemplo, "5.0" e "1.6") são do tipo
"float". Veremos mais sobre tipos numéricos posteriormente neste
tutorial.

Divisão ("/") sempre retorna ponto flutuante (float). Para fazer uma
*divisão pelo piso* e receber um inteiro como resultado você pode usar
o operador "//"; para calcular o resto você pode usar o "%":

   >>> 17 / 3  # divisão clássica retorna um ponto flutuante
   5.666666666666667
   >>>
   >>> 17 // 3  # divisão pelo piso descarta a parte fracionária
   5
   >>> 17 % 3  # o operador % retorna o resto da divisão
   2
   >>> 5 * 3 + 2  # quociente do piso * divisor + restante
   17

Com Python, é possível usar o operador "**" para calcular potências
[1]:

   >>> 5 ** 2  # 5 ao quadrado
   25
   >>> 2 ** 7  # 2 à potência de 7
   128

O sinal de igual ("'='") é usado para atribuir um valor a uma
variável. Depois de uma atribuição, nenhum resultado é exibido antes
do próximo prompt:

   >>> largura = 20
   >>> altura = 5 * 9
   >>> largura * altura
   900

Se uma variável não é "definida" (não tem um valor atribuído), tentar
utilizá-la levantará um erro:

   >>> n  # tenta acessar uma variável não definida
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'n' is not defined

Há suporte completo para ponto flutuante (*float*); operadores com
operandos de diferentes tipos convertem o inteiro para ponto
flutuante:

   >>> 4 * 3.75 - 1
   14.0

No modo interativo, o valor da última expressão exibida é atribuída a
variável "_". Assim, ao utilizar Python como uma calculadora, fica
mais fácil prosseguir com os cálculos, por exemplo:

   >>> taxa = 12.5 / 100
   >>> preço = 100.50
   >>> preço * taxa
   12.5625
   >>> preço + _
   113.0625
   >>> round(_, 2)
   113.06

Essa variável especial deve ser tratada como *somente para leitura*
pelo usuário. Nunca lhe atribua explicitamente um valor --- do
contrário, estaria criando uma outra variável (homônima) independente,
que mascararia a variável especial com seu comportamento mágico.

Além de "int" e "float", o Python oferece suporte a outros tipos de
números, tais como "Decimal" e "Fraction". O Python também possui
suporte embutido a números complexos, e usa os sufixos "j" ou "J" para
indicar a parte imaginária (por exemplo, "3+5j").


3.1.2. Texto
------------

Python pode manipular texto (representado pelo tipo "str", também
chamado de "strings"), bem como números. Isso inclui caracteres ""!"",
palavras ""coelho"", nomes ""Paris"", frases ""Eu te protejo."", etc.
""Oba! :)"". Eles podem ser colocados entre aspas simples ("'...'") ou
aspas duplas (""..."") com o mesmo resultado [2].

   >>> 'spam eggs'  # aspas simples
   'spam eggs'
   >>> "Coelho de Paris, eu te projeto :)! Viva!"  # aspas duplas
   'Coelho de Paris, eu te projeto :)! Viva!'
   >>> '1975'  # dígitos e numerais envoltos em aspas também são strings
   '1975'

Para colocar aspas entre aspas, precisamos "escapá-la", precedendo-as
com "\". Alternativamente, podemos usar o outro tipo de aspas:

   >>> 'd\'água'  # use \' para escapar a aspa simples...
   "d'água"
   >>> "d'água"  # ...ou use aspas duplas
   "d'água"
   >>> '"Sim", eles disseram.'
   '"Sim", eles disseram.'
   >>> "\"Sim\", eles disseram."
   '"Sim", eles disseram.'
   >>> '"Copo d\'água", eles pediram.'
   '"Copo d'água", eles pediram.'

No shell do Python, a definição de string e a string de saída podem
parecer diferentes. A função "print()" produz uma saída mais legível,
omitindo as aspas delimitadoras e imprimindo caracteres de escape e
especiais:

   >>> s = 'Primeira linha.\nSegunda linha.'  # \n significa nova linha
   >>> s  # sem print(), caracteres especiais são incluídos na string
   'Primeira linha.\nSegunda linha.'
   >>> print(s)  # com print(), caracteres especiais são interpretados, então \n produz nova linha
   Primeira linha.
   Segunda linha.

Caso não queira que os caracteres precedidos por "\" sejam
interpretados como caracteres especiais, você pode usar *strings
brutas* (*raw*, em inglês) adicionando um "r" antes da primeira aspa:

   >>> print('C:\this\name')  # aqui \t significa tabulação, \n significa nova linha
   C:      his
   ame
   >>> print(r'C:\this\name')  # note o r antes da aspa
   C:\this\name

Há um aspecto sutil nas strings brutas: uma string bruta não pode
terminar em um número ímpar de caracteres "\"; consulte o FAQ
relacionado para mais informações e soluções alternativas.

As strings literais podem abranger várias linhas. Uma maneira é usar
as aspas triplas: """"..."""" ou "'''...'''". Caracteres de fim de
linha são incluídos automaticamente na string, mas é possível evitar
isso adicionando uma "\" no final. No exemplo a seguir, a nova linha
no início não é incluída:

   >>> print("""\
   ... Uso: coisinha [OPÇÕES]
   ...      -h                        Exibe esta mensagem de uso
   ...      -H hostname               Hostname para se conectar
   ... """)
   Usage: coisinha [OPÇÕES]
        -h                        Exibe esta mensagem de ajuda
        -H hostname               Hostname para se conectar

   >>>

Strings podem ser concatenadas (coladas) com o operador "+", e
repetidas com "*":

   >>> # 3 vezes 'un', seguido por 'ium'
   >>> 3 * 'un' + 'ium'
   'unununium'

Duas ou mais *strings literais* (ou seja, entre aspas) ao lado da
outra são automaticamente concatenados.

   >>> 'Py' 'thon'
   'Python'

Esse recurso é particularmente útil quando você quer quebrar strings
longas:

   >>> texto = ('Coloque várias strings dentro de parênteses '
   ...          'para fazer com que elas sejam concatenadas.')
   >>> texto
   'Coloque várias strings dentro de parênteses para fazer com que elas sejam concatenadas.'

Isso só funciona com duas strings literais, não com variáveis ou
expressões:

   >>> prefixo = 'Py'
   >>> prefixo 'thon'  # não é possível concatenar uma variável e um literal de string
     File "<stdin>", line 1
       prefixi 'thon'
              ^^^^^^
   SyntaxError: invalid syntax
   >>> ('un' * 3) 'ium'
     File "<stdin>", line 1
       ('un' * 3) 'ium'
                  ^^^^^
   SyntaxError: invalid syntax

Se você quiser concatenar variáveis ou uma variável e uma literal, use
"+":

   >>> prefixo + 'thon'
   'Python'

As strings podem ser *indexadas* (subscritas), com o primeiro
caractere como índice 0. Não existe um tipo específico para
caracteres; um caractere é simplesmente uma string cujo tamanho é 1:

   >>> palavra = 'Python'
   >>> palavra[0]  # caractere na posição 0
   'P'
   >>> palavra[5]  # caractere na posição 5
   'n'

Índices também podem ser números negativos para iniciar a contagem
pela direita:

   >>> palavra[-1]  # último caractere
   'n'
   >>> palavra[-2]  # penúltimo caractere
   'o'
   >>> palavra[-6]
   'P'

Note que dado que -0 é o mesmo que 0, índices negativos começam em -1.

Além da indexação, o *fatiamento* também é permitido. Embora a
indexação seja usada para obter caracteres individuais, *fatiar*
permite que você obtenha uma substring:

   >>> palavra[0:2]  # caracteres da posição 0 (incluída) até 2 (excluída)
   'Py'
   >>> palavra[2:5]  # caracteres da posição 2 (incluída) até 5 (excluída)
   'tho'

Os índices do fatiamento possuem padrões úteis; um primeiro índice
omitido padrão é zero, um segundo índice omitido é por padrão o
tamanho da string sendo fatiada:

   >>> palavra[:2]   # caracteres do início até a posição 2 (excluída)
   'Py'
   >>> palavra[4:]   # caracteres da posição 4 (incluída) até o fim
   'on'
   >>> palavra[-2:]  # caracteres da penúltima (incluída) até o fim
   'on'

Observe como o início sempre está incluído, e o fim sempre é excluído.
Isso garante que "s[:i] + s[i:]" seja sempre igual a "s":

   >>> palavra[:2] + palavra[2:]
   'Python'
   >>> palavra[:4] + palavra[4:]
   'Python'

Uma maneira de lembrar como fatias funcionam é pensar que os índices
indicam posições *entre* caracteres, onde a borda esquerda do primeiro
caractere é 0. Assim, a borda direita do último caractere de uma
string de comprimento *n* tem índice *n*, por exemplo:

    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1

A primeira fileira de números indica a posição dos índices 0...6 na
string; a segunda fileira indica a posição dos respectivos índices
negativos. Uma fatia de *i* a *j* consiste em todos os caracteres
entre as bordas *i* e *j*, respectivamente.

Para índices positivos, o comprimento da fatia é a diferença entre os
índices, se ambos estão dentro dos limites da string. Por exemplo, o
comprimento de "word[1:3]" é 2.

A tentativa de usar um índice que seja muito grande resultará em um
erro:

   >>> palavra[42]  # a palavra só tem 6 caracteres
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: string index out of range

No entanto, os índices de fatiamento fora do alcance são tratados
graciosamente (N.d.T: o termo original “gracefully” indica robustez no
tratamento de erros) quando usados para fatiamento. Um índice maior
que o comprimento é trocado pelo comprimento, um limite superior menor
que o limite inferior produz uma string vazia:

   >>> palavra[4:42]
   'on'
   >>> palavra[42:]
   ''

As strings do Python não podem ser alteradas --- uma string é
*imutável*. Portanto, atribuir a uma posição indexada na sequência
resulta em um erro:

   >>> palavra[0] = 'J'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment
   >>> palavra[2:] = 'py'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment

Se você precisar de uma string diferente, deverá criar uma nova:

   >>> 'J' + palavra[1:]
   'Jython'
   >>> palavra[:2] + 'py'
   'Pypy'

A função embutida "len()" devolve o comprimento de uma string:

   >>> s = 'supercalifragilisticexpialidoce'
   >>> len(s)
   31

Ver também:

  Tipo sequência de texto --- str
     As strings são exemplos de *tipos de sequências* e suportam as
     operações comumente suportadas por esses tipos.

  String Methods
     As strings suportam uma grande quantidade de métodos para
     transformações básicas e busca.

  Literais de strings formatadas
     Strings literais que possuem expressões embutidas.

  Sintaxe das strings de formato
     Informações sobre formatação de string com o método
     "str.format()".

  Formatação de string no estilo printf
     As antigas operações de formatação invocadas quando as strings
     são o operando esquerdo do operador "%" são descritas com mais
     detalhes aqui.


3.1.3. Listas
-------------

Python inclui diversas estruturas de dados *compostas*, usadas para
agrupar outros valores. A mais versátil é *list* (lista), que pode ser
escrita como uma lista de valores (itens) separados por vírgula, entre
colchetes. Os valores contidos na lista não precisam ser todos do
mesmo tipo.

   >>> quadrados = [1, 4, 9, 16, 25]
   >>> quadrados
   [1, 4, 9, 16, 25]

Como strings (e todos os tipos embutidos de *sequência*), listas pode
ser indexados e fatiados:

   >>> quadrados[0]  # indexação retorna o item
   1
   >>> quadrados[-1]
   25
   >>> quadrados[-3:]  # fatiamento retorna uma nova lista
   [9, 16, 25]

As listas também suportam operações como concatenação:

   >>> quadrados + [36, 49, 64, 81, 100]
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Diferentemente de strings, que são *imutáveis*, listas são *mutáveis*,
ou seja, é possível alterar elementos individuais de uma lista:

   >>> cubos = [1, 8, 27, 65, 125]  # algo errado aqui
   >>> 4 ** 3  # o cubo de 4 é 64, não 65!
   64
   >>> cubos[3] = 64  # substitui o valor errado
   >>> cubos
   [1, 8, 27, 64, 125]

Você também pode adicionar novos itens no final da lista, usando o
*método* "list.append()" (estudaremos mais a respeito dos métodos
posteriormente):

   >>> cubos.append(216)  # adiciona o cubo de 6
   >>> cubos.append(7 ** 3)  # e o cubo de 7
   >>> cubos
   [1, 8, 27, 64, 125, 216, 343]

A atribuição simples em Python nunca copia dados. Quando você atribui
uma lista a uma variável, a variável se refere à *lista existente*.
Quaisquer alterações que você fizer na lista por meio de uma variável
serão vistas por todas as outras variáveis que se referem a ela:

   >>> rgb = ["Vermelho", "Verde", "Azul"]
   >>> rgba = rgb
   >>> id(rgb) == id(rgba)  # elas referenciam o mesmo objeto
   True
   >>> rgba.append("Alf")
   >>> rgb
   ["Vermelho", "Verde", "Azul", "Alf"]

Todas as operações de fatiamento devolvem uma nova lista contendo os
elementos solicitados. Isso significa que o seguinte fatiamento
devolve uma cópia rasa da lista:

   >>> rgba_correto = rgba[:]
   >>> rgba_correto[-1] = "Alfa"
   >>> rgba_correto
   ["Vermelho", "Verde", "Azul", "Alfa"]
   >>> rgba
   ["Vermelho", "Verde", "Azul", "Alf"]

Atribuição a fatias também é possível, e isso pode até alterar o
tamanho da lista ou remover todos os itens dela:

   >>> letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> letras
   ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> # substitui alguns valores
   >>> letras[2:5] = ['C', 'D', 'E']
   >>> letras
   ['a', 'b', 'C', 'D', 'E', 'f', 'g']
   >>> # agora remove-os
   >>> letras[2:5] = []
   >>> letras
   ['a', 'b', 'f', 'g']
   >>> # limpa a lista substituindo todos os elementos por uma lista vazia
   >>> letras[:] = []
   >>> letras
   []

A função embutida "len()" também se aplica a listas:

   >>> letras = ['a', 'b', 'c', 'd']
   >>> len(letras)
   4

É possível aninhar listas (criar listas contendo outras listas), por
exemplo:

   >>> a = ['a', 'b', 'c']
   >>> n = [1, 2, 3]
   >>> x = [a, n]
   >>> x
   [['a', 'b', 'c'], [1, 2, 3]]
   >>> x[0]
   ['a', 'b', 'c']
   >>> x[0][1]
   'b'


3.2. Primeiros passos para a programação
========================================

Claro, podemos usar o Python para tarefas mais complicadas do que
somar 2+2. Por exemplo, podemos escrever o início da sequência de
Fibonacci assim:

   >>> # Sequência de Fibonacci:
   >>> # a soma de dois elementos define a próxima
   >>> a, b = 0, 1
   >>> while a < 10:
   ...     print(a)
   ...     a, b = b, a+b
   ...
   0
   1
   1
   2
   3
   5
   8

Este exemplo introduz diversas características ainda não mencionadas.

* A primeira linha contém uma atribuição múltipla: as variáveis "a" e
  "b" recebem simultaneamente os novos valores 0 e 1. Na última linha
  há outro exemplo de atribuição múltipla demonstrando que expressões
  do lado direito são sempre avaliadas primeiro, antes da atribuição.
  As expressões do lado direito são avaliadas da esquerda para a
  direita.

* O laço de repetição "while" executa enquanto a condição (aqui: "a <
  10") permanece verdadeira. Em Python, como em C, qualquer valor
  inteiro que não seja zero é considerado verdadeiro; zero é
  considerado falso. A condição pode também ser uma cadeia de
  caracteres ou uma lista, ou qualquer sequência; qualquer coisa com
  um tamanho maior que zero é verdadeiro, enquanto sequências vazias
  são falsas. O teste usado no exemplo é uma comparação simples. Os
  operadores padrões de comparação são os mesmos de C: "<" (menor
  que), ">" (maior que), "==" (igual), "<=" (menor ou igual), ">="
  (maior ou igual) e "!=" (diferente).

* O *corpo* do laço é *indentado*: indentação em Python é a maneira de
  agrupar comandos em blocos. No console interativo padrão você terá
  que digitar tab ou espaços para indentar cada linha. Na prática você
  vai preparar scripts Python mais complicados em um editor de texto;
  a maioria dos editores de texto tem facilidades de indentação
  automática. Quando um comando composto é digitado interativamente,
  deve ser finalizado por uma linha em branco (já que o interpretador
  não tem como adivinhar qual é a última linha do comando). Observe
  que toda linha de um mesmo bloco de comandos deve ter a mesma
  indentação.

* A função "print()" escreve o valor dos argumentos fornecidos. É
  diferente de apenas escrever a expressão no interpretador (como
  fizemos anteriormente nos exemplos da calculadora) pela forma como
  lida com múltiplos argumentos, quantidades de ponto flutuante e
  strings. As strings são impressas sem aspas, e um espaço é inserido
  entre os itens, assim você pode formatar bem o resultado, dessa
  forma:

     >>> i = 256*256
     >>> print('O valor de i é', i)
     O valor de i é 65536

  O argumento nomeado *end* pode ser usado para evitar uma nova linha
  após a saída ou finalizar a saída com uma string diferente:

     >>> a, b = 0, 1
     >>> while a < 1000:
     ...     print(a, end=',')
     ...     a, b = b, a+b
     ...
     0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

-[ Notas de rodapé ]-

[1] Uma vez que "**" tem precedência mais alta que "-", "-3**2" será
    interpretado como "-(3**2)" e assim resultará em "-9". Para evitar
    isso e obter "9", você pode usar "(-3)**2".

[2] Ao contrário de outras linguagens, caracteres especiais como "\n"
    têm o mesmo significado com as aspas simples ("'...'") e duplas
    (""..."") . A única diferença entre as duas é que, dentro de aspas
    simples, você não precisa escapar o """ (mas você deve escapar a
    "\'") e vice-versa.
