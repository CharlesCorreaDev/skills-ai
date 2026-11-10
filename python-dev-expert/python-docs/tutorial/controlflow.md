4. Mais ferramentas de controle de fluxo
****************************************

Assim como a instrução "while" que acabou de ser apresentada, o Python
usa mais algumas que encontraremos neste capítulo.


4.1. Instruções "if"
====================

Provavelmente a mais conhecida instrução de controle de fluxo é o
"if". Por exemplo:

   >>> x = int(input("Insira um número inteiro: "))
   Insira um número inteiro: 42
   >>> if x < 0:
   ...     x = 0
   ...     print('Negativo alterado para zero')
   ... elif x == 0:
   ...     print('Zero')
   ... elif x == 1:
   ...     print('Um')
   ... else:
   ...     print('Mais')
   ...
   Mais

Pode haver zero ou mais partes "elif", e a parte "else" é opcional. A
palavra-chave '"elif"' é uma abreviação para 'else if', e é útil para
evitar indentação excessiva. Uma sequência "if" ... "elif" ... "elif"
... substitui as instruções "switch" ou "case", encontrados em outras
linguagens.

Se você está comparando o mesmo valor com várias constantes, ou
verificando por tipos ou atributos específicos, você também pode achar
a instrução "match" útil. Para mais detalhes veja Instruções match.


4.2. Instruções "for"
=====================

A instrução "for" em Python é um pouco diferente do que costuma ser em
C ou Pascal. Ao invés de sempre iterar sobre uma progressão aritmética
de números (como no Pascal), ou permitir ao usuário definir o passo de
iteração e a condição de parada (como C), a instrução "for" do Python
itera sobre os itens de qualquer sequência (seja uma lista ou uma
string), na ordem que aparecem na sequência. Por exemplo:

   >>> # Mede algumas strings:
   >>> palavras = ['gato', 'janela', 'defenestrar']
   >>> for p in palavras:
   ...     print(p, len(p))
   ...
   gato 4
   janela 6
   defenestrar 11

Código que modifica uma coleção sobre a qual está iterando pode ser
inseguro. No lugar disso, usualmente você deve iterar sobre uma cópia
da coleção ou criar uma nova coleção:

   # Cria uma amostra de coleção
   users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

   # Estratégia: iterar por uma cópia
   for user, status in users.copy().items():
       if status == 'inactive':
           del users[user]

   # Estratégia: criar uma nova coleção
   active_users = {}
   for user, status in users.items():
       if status == 'active':
           active_users[user] = status


4.3. A função "range()"
=======================

Se você precisa iterar sobre sequências numéricas, a função embutida
"range()" é a resposta. Ela gera progressões aritméticas:

   >>> for i in range(5):
   ...     print(i)
   ...
   0
   1
   2
   3
   4

O ponto de parada fornecido nunca é incluído na lista; "range(10)"
gera uma lista com 10 valores, exatamente os índices válidos para uma
sequência de comprimento 10. É possível iniciar o intervalo com outro
número, ou alterar a razão da progressão (inclusive com passo
negativo):

   >>> list(range(5, 10))
   [5, 6, 7, 8, 9]

   >>> list(range(0, 10, 3))
   [0, 3, 6, 9]

   >>> list(range(-10, -100, -30))
   [-10, -40, -70]

Para iterar sobre os índices de uma sequência, combine "range()" e
"len()" da seguinte forma:

   >>> a = ['Maria', 'tinha', 'um', 'carneirinho']
   >>> for i in range(len(a)):
   ...     print(i, a[i])
   ...
   0 Maria
   1 tinha
   2 um
   3 carneirinho

Na maioria dos casos, porém, é mais conveniente usar a função
"enumerate()", veja Técnicas de iteração.

Uma coisa estranha acontece se você imprime um intervalo:

   >>> range(10)
   range(0, 10)

Em muitos aspectos, o objeto retornado pela função "range()" se
comporta como se fosse uma lista, mas na verdade não é. É um objeto
que retorna os itens sucessivos da sequência desejada quando você
itera sobre a mesma, mas na verdade ele não gera a lista, economizando
espaço.

Dizemos que um objeto é *iterável*, isso é, candidato a ser alvo de
uma função ou construção que espera alguma coisa capaz de retornar
sucessivamente seus elementos um de cada vez até ser *esgotado*. Nós
vimos que a instrução "for" é um exemplo de construção, enquanto que
um exemplo de função que recebe um iterável é "sum()":

   >>> sum(range(4))  # 0 + 1 + 2 + 3
   6

Mais tarde, veremos mais funções que retornam iteráveis e tomam
iteráveis como argumentos. No capítulo Estruturas de dados, iremos
discutir "list()" em mais detalhes.


4.4. Instruções "break" e "continue"
====================================

A instrução "break" sai imediatamente do laço de repetição mais
interno, seja "for" ou "while":

   >>> for n in range(2, 10):
   ...     for x in range(2, n):
   ...         if n % x == 0:
   ...             print(f"{n} igual a {x} * {n//x}")
   ...             break
   ...
   4 igual a 2 * 2
   6 igual a 2 * 3
   8 igual a 2 * 4
   9 equals 3 * 3

A instrução "continue" continua com a próxima iteração do laço:

   >>> for num in range(2, 10):
   ...     if num % 2 == 0:
   ...         print(f"Encontrado um número par {num}")
   ...         continue
   ...     print(f"Encontrado um número ímpar {num}")
   ...
   Encontrado um número par 2
   Encontrado um número ímpar 3
   Encontrado um número par 4
   Encontrado um número ímpar 5
   Encontrado um número par 6
   Encontrado um número ímpar 7
   Encontrado um número par 8
   Encontrado um número ímpar 9


4.5. Cláusulas "else" em laços
==============================

Em um laço "for" ou "while" a instrução "break" pode ser pareada com
uma cláusula "else". Se o laço terminar sem executar o "break", a
cláusula "else" será executada.

Em um laço "for", a cláusula "else" é executada após o laço finalizar
sua iteração final, ou seja, se não ocorrer nenhuma interrupção.

Em um laço "while", ele é executado após a condição do laço se tornar
falsa.

Em qualquer tipo de laço, a cláusula "else" **não** é executada se o
laço foi encerrado por um "break". Claro, outras maneiras de encerrar
o laço mais cedo, como um "return" ou uma exceção levantada, também
pularão a execução da cláusula "else".

Isso é exemplificado no seguinte laço "for", que procura por números
primos:

   >>> for n in range(2, 10):
   ...     for x in range(2, n):
   ...         if n % x == 0:
   ...             print(n, 'igual a', x, '*', n//x)
   ...             break
   ...     else:
   ...         # a iteração passou direto sem encontrar um fator
   ...         print(n, 'é um número primo')
   ...
   2 é um número primo
   3 é um número primo
   4 igual a 2 * 2
   5 é um número primo
   6 igual a 2 * 3
   7 é um número primo
   8 igual a 2 * 4
   9 igual a 3 * 3

(Sim, este é o código correto. Observe atentamente: a cláusula "else"
pertence ao laço "for", **não** à instrução "if".)

Uma maneira de pensar na cláusula else é imaginá-la pareada com o "if"
dentro do laço. Conforme o laço é executado, ele executará uma
sequência como if/if/if/else. O "if" está dentro do laço, encontrado
várias vezes. Se a condição for verdadeira, um "break" acontecerá. Se
a condição nunca for verdadeira, a cláusula "else" fora do laço será
executada.

Quando usado em um laço, a cláusula "else" tem mais em comum com a
cláusula "else" de uma instrução "try" do que com a de instruções
"if": a cláusula "else" de uma instrução "try" é executada quando não
ocorre exceção, e a cláusula "else" de um laço é executada quando não
ocorre um "break". Para mais informações sobre instrução "try" e
exceções, veja Tratamento de exceções.


4.6. Instruções "pass"
======================

A instrução "pass" não faz nada. Pode ser usada quando a sintaxe exige
uma instrução, mas a semântica do programa não requer nenhuma ação.
Por exemplo:

   >>> while True:
   ...     pass  # Ocupado, aguardando interrupção por teclado (Ctrl+C)
   ...

Isto é usado muitas vezes para se definir classes mínimas:

   >>> class MinhaClasseVazia:
   ...     pass
   ...

Outra ocasião em que o "pass" pode ser usado é como um substituto
temporário para uma função ou bloco condicional, quando se está
trabalhando com código novo, ainda indefinido, permitindo que
mantenha-se o pensamento num nível mais abstrato. O "pass" é
silenciosamente ignorado:

   >>> def initlog(*args):
   ...     pass   # Lembre-se de implementar isso!
   ...

Para este último caso, muitas pessoas usam o literal de reticências
"..." em vez de "pass". Este uso não tem significado especial para
Python e não faz parte da definição da linguagem (você pode usar
qualquer expressão constante aqui), mas "..." também é usado
convencionalmente como um espaço reservado. Consulte O Objeto
Ellipsis.


4.7. Instruções "match"
=======================

Uma instrução "match" pega uma expressão e compara seu valor com
padrões sucessivos fornecidos como um ou mais blocos de case. Isso é
superficialmente semelhante a uma instrução switch em C, Java ou
JavaScript (e muitas outras linguagens), mas muito mais parecido com a
correspondência de padrões em linguages como Rust ou Haskell. Apenas o
primeiro padrão que corresponder será executado, podendo também
extrair componentes (elementos de sequência ou atributos de objetos)
do valor para variáveis. Se nenhum caso corresponder, nenhuma das
ramificações será executada.

A forma mais simples compara um valor de assunto com um ou mais
literais:

   def http_error(status):
       match status:
           case 400:
               return "Bad request"
           case 404:
               return "Not found"
           case 418:
               return "I'm a teapot"
           case _:
               return "Something's wrong with the internet"

Observe o último bloco: o "nome da variável" "_" atua como um
*curinga* e nunca falha em corresponder.

Você pode combinar vários literais em um único padrão usando "|"
("ou"):

   case 401 | 403 | 404:
       return "Não permitido"

Os padrões podem se parecer com atribuições de desempacotamento e
podem ser usados para vincular variáveis:

   # ponto é uma tupla (x, y)
   match ponto:
       case (0, 0):
           print("Origem")
       case (0, y):
           print(f"Y={y}")
       case (x, 0):
           print(f"X={x}")
       case (x, y):
           print(f"X={x}, Y={y}")
       case _:
           raise ValueError("Não é um ponto")

Estude isso com cuidado! O primeiro padrão tem dois literais e pode
ser considerado uma extensão do padrão literal mostrado acima. Mas os
próximos dois padrões combinam um literal e uma variável, e a variável
*vincula* um valor do assunto ("ponto"). O quarto padrão captura dois
valores, o que o torna conceitualmente semelhante à atribuição de
desempacotamento "(x, y) = ponto".

Se você estiver usando classes para estruturar seus dados, você pode
usar o nome da classe seguido por uma lista de argumentos semelhante a
um construtor, mas com a capacidade de capturar atributos em
variáveis:

   class Ponto:
       def __init__(self, x, y):
           self.x = x
           self.y = y

   def onde_está(ponto):
       match ponto:
           case Ponto(x=0, y=0):
               print("Origem")
           case Ponto(x=0, y=y):
               print(f"Y={y}")
           case Ponto(x=x, y=0):
               print(f"X={x}")
           case Ponto():
               print("Em outro lugar")
           case _:
               print("Não é um ponto")

Você pode usar parâmetros posicionais com algumas classes embutidas
que fornecem uma ordem para seus atributos (por exemplo, classes de
dados). Você também pode definir uma posição específica para atributos
em padrões configurando o atributo especial "__match_args__" em suas
classes. Se for definido como ("x", "y"), os seguintes padrões são
todos equivalentes (e todos vinculam o atributo "y" à variável "var"):

   Ponto(1, var)
   Ponto(1, y=var)
   Ponto(x=1, y=var)
   Ponto(y=var, x=1)

Uma maneira recomendada de ler padrões é vê-los como uma forma
estendida do que você colocaria à esquerda de uma atribuição, para
entender quais variáveis seriam definidas para quê. Apenas os nomes
autônomos (como "var" acima) são atribuídos por uma instrução de
correspondência. Nomes pontilhados (como "foo.bar"), nomes de
atributos (o "x=" e "y=" acima) ou nomes de classes (reconhecidos pelo
"(...)" próximo a eles, como "Ponto" acima) nunca são atribuídos.

Os padrões podem ser aninhados arbitrariamente. Por exemplo, se
tivermos uma pequena lista de Pontos, com "__match_args__" adicionado,
poderíamos correspondê-la assim:

   class Ponto:
       __match_args__ = ('x', 'y')
       def __init__(self, x, y):
           self.x = x
           self.y = y

   match pontos:
       case []:
           print("Sem pontos")
       case [Ponto(0, 0)]:
           print("A origem")
       case [Ponto(x, y)]:
           print(f"Ponto único {x}, {y}")
       case [Ponto(0, y1), Ponto(0, y2)]:
           print(f"Dois do eixo Y em {y1}, {y2}")
       case _:
           print("Outra coisa")

Podemos adicionar uma cláusula "if" a um padrão, conhecido como
"guarda". Se a guarda for falsa, "match" continua para tentar o
próximo bloco de caso. Observe que a captura de valor ocorre antes que
a guarda seja avaliada:

   match ponto:
       case Ponto(x, y) if x == y:
           print(f"Y=X at {x}")
       case Ponto(x, y):
           print(f"Não está na diagonal")

Vários outros recursos importantes desta instrução:

* Assim como desempacotar atribuições, os padrões de tupla e lista têm
  exatamente o mesmo significado e realmente correspondem a sequências
  arbitrárias. Uma exceção importante é que eles não correspondem a
  iteradores ou strings.

* Os padrões de sequência têm suporte ao desempacotamento estendido:
  "[x, y, *rest]" e "(x, y, *rest)" funcionam de forma semelhante ao
  desempacotamento de atribuições. O nome depois de "*" também pode
  ser "_", então "(x, y, *_)" corresponde a uma sequência de pelo
  menos dois itens sem ligar os itens restantes.

* Padrões de mapeamento: "{"bandwidth": b, "latency": l}" captura os
  valores ""bandwidth"" e ""latency"" de um dicionário. Diferente dos
  padrões de sequência, chaves extra são ignoradas.  Um
  desempacotamento como "**rest" também é permitido.  (Mas "**_" seria
  redundante, então não é permitido.)

* Subpadrões podem ser capturados usando a palavra reservada "as":

     case (Ponto(x1, y1), Ponto(x2, y2) as p2): ...

  Vai capturar o segundo elemento da entrada como "p2" (se a entrada
  for uma sequência de dois pontos)

* A maioria dos literais são comparados por igualdade, no entanto os
  singletons "True", "False" e "None" são comparados por identidade.

* Padrões podem usar constantes nomeadas. Estas devem ser nomes
  pontilhados para prevenir que sejam interpretadas como variáveis de
  captura:

     from enum import Enum
     class Cor(Enum):
         VERMELHO = 'vermelho'
         VERDE = 'verde'
         AZUL = 'azul'

     cor = Cor(input("Insira sua escolha de 'vermelho, 'azul' ou 'verde': "))

     match color:
         case Cor.VERMELHO:
             print("Eu vejo vermelho!")
         case Cor.VERDE:
             print("Grama é verde")
         case Cor.AZUL:
             print("O céu é azul :)")

Para uma explicação mais detalhada e exemplos adicionais, você pode
olhar **PEP 636** que foi escrita em formato de tutorial.


4.8. Definindo funções
======================

Podemos criar uma função que escreve a série de Fibonacci até um
limite arbitrário:

   >>> def fib(n):    # escreve série de Fibonacci menor que n
   ...     """Imprime uma série de Fibonacci menor que n."""
   ...     a, b = 0, 1
   ...     while a < n:
   ...         print(a, end=' ')
   ...         a, b = b, a+b
   ...     print()
   ...
   >>> # Agora chamamos a função que acabamos de definir:
   >>> fib(2000)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

A palavra reservada "def" inicia a *definição* de uma função. Ela deve
ser seguida do nome da função e da lista de parâmetros formais entre
parênteses. As instruções que formam o corpo da função começam na
linha seguinte e devem ser indentados.

Opcionalmente, a primeira linha do corpo da função pode ser uma
literal string, cujo propósito é documentar a função. Se presente,
essa string chama-se *docstring*. (Há mais informação sobre docstrings
na seção Strings de documentação.) Existem ferramentas que utilizam
docstrings para produzir automaticamente documentação online ou para
imprimir, ou ainda, permitir que o usuário navegue interativamente
pelo código. É uma boa prática incluir sempre docstrings em suas
funções, portanto, tente fazer disso um hábito.

A *execução* de uma função cria uma nova tabela de símbolos para as
variáveis locais da função. Mais precisamente, todas as atribuições de
variáveis numa função são armazenadas na tabela de símbolos local;
referências a variáveis são buscadas primeiro na tabela de símbolos
local, em seguida na tabela de símbolos locais de funções
delimitadoras ou circundantes, depois na tabela de símbolos global e,
finalmente, na tabela de nomes da própria linguagem. Embora possam ser
referenciadas, variáveis globais e de funções externas não podem ter
atribuições (a menos que seja utilizada a instrução "global", para
variáveis globais, ou "nonlocal", para variáveis de funções externas).

Os parâmetros reais (argumentos) de uma chamada de função são
introduzidos na tabela de símbolos local da função no momento da
chamada; portanto, argumentos são passados *por valor* (onde o *valor*
é sempre uma *referência* para objeto, não o valor do objeto). [1]
Quando uma função chama outra função, ou chama a si mesma
recursivamente, uma nova tabela de símbolos é criada para tal chamada.

Uma definição de função associa o nome da função com o objeto função
na tabela de símbolos atual. O interpretador reconhece o objeto
apontado pelo nome como uma função definida pelo usuário. Outros nomes
também podem apontar para o mesmo objeto função e também pode ser
usados pra acessar a função:

   >>> fib
   <function fib at 10042ed0>
   >>> f = fib
   >>> f(100)
   0 1 1 2 3 5 8 13 21 34 55 89

Conhecendo outras linguagens, pode-se questionar que "fib" não é uma
função, mas um procedimento, pois ela não devolve um valor. Na
verdade, mesmo funções que não usam a instrução "return" devolvem um
valor, ainda que pouco interessante. Esse valor é chamado "None" (é um
nome embutido). O interpretador interativo evita escrever "None"
quando ele é o único resultado de uma expressão. Mas se quiser vê-lo
pode usar a função "print()":

   >>> fib(0)
   >>> print(fib(0))
   None

É fácil escrever uma função que retorna uma lista de números da série
de Fibonacci, ao invés de exibi-los:

   >>> def fib2(n):  # retorna série de  Fibonacci até n
   ...     """Retorna uma lista contendo a série de Fibonacci até n."""
   ...     resultado = []
   ...     a, b = 0, 1
   ...     while a < n:
   ...         resultado.append(a)    # veja abaixo
   ...         a, b = b, a+b
   ...     return resultado
   ...
   >>> f100 = fib2(100)    # chama-o
   >>> f100                # escreve o resultado
   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Este exemplo demonstra novos recursos de Python:

* A instrução "return" finaliza a execução e retorna um valor da
  função. "return" sem qualquer expressão como argumento retorna
  "None". Atingir o final da função também retorna "None".

* A instrução "result.append(a)" chama um *método* do objeto lista
  "result". Um método é uma função que 'pertence' a um objeto, e é
  chamada "obj.nomemetodo", onde "obj" é um objeto qualquer (pode ser
  uma expressão), e "nomemetodo" é o nome de um método que foi
  definido pelo tipo do objeto. Tipos diferentes definem métodos
  diferentes. Métodos de diferentes tipos podem ter o mesmo nome sem
  ambiguidade. (É possível definir seus próprios tipos de objetos e
  métodos, utilizando *classes*, veja em Classes) O método "append()",
  mostrado no exemplo é definido para objetos do tipo lista; adiciona
  um novo elemento ao final da lista. Neste exemplo, ele equivale a
  "result = result + [a]", só que mais eficiente.


4.9. Mais sobre definição de funções
====================================

É possível definir funções com um número variável de argumentos.
Existem três formas, que podem ser combinadas.


4.9.1. Argumentos com valor padrão
----------------------------------

A mais útil das três é especificar um valor padrão para um ou mais
argumentos. Isso cria uma função que pode ser invocada com menos
argumentos do que os que foram definidos. Por exemplo:

   def pergunta_ok(mensagem, tentativas=4, lembrete='Por favor, tente novamente!'):
       while True:
           resposta = input(mensagem)
           if resposta in {'s', 'sim', 'é'}:
               return True
           if resposta in {'n', 'não', 'nah'}:
               return False
           tentativas = tentativas - 1
           if tentativas < 0:
               raise ValueError('resposta inválida de usuário')
           print(lembrete)

Essa função pode ser chamada de várias formas:

* fornecendo apenas o argumento obrigatório: "ask_ok('Do you really
  want to quit?')"

* fornecendo um dos argumentos opcionais: "ask_ok('OK to overwrite the
  file?', 2)"

* ou fornecendo todos os argumentos: "ask_ok('OK to overwrite the
  file?', 2, 'Come on, only yes or no!')"

Este exemplo também introduz a palavra-chave "in", que verifica se uma
sequência contém ou não um determinado valor.

Os valores padrões são avaliados no momento da definição da função, e
no escopo em que a função foi *definida*, portanto:

   i = 5

   def f(arg=i):
       print(arg)

   i = 6
   f()

irá exibir "5".

**Aviso importante:** Valores padrões são avaliados apenas uma vez.
Isso faz diferença quando o valor é um objeto mutável, como uma lista,
dicionário, ou instâncias de classes. Por exemplo, a função a seguir
acumula os argumentos passados, nas chamadas subsequentes:

   def f(a, L=[]):
       L.append(a)
       return L

   print(f(1))
   print(f(2))
   print(f(3))

Isso exibirá:

   [1]
   [1, 2]
   [1, 2, 3]

Se não quiser que o valor padrão seja compartilhado entre chamadas
subsequentes, pode reescrever a função assim:

   def f(a, L=None):
       if L is None:
           L = []
       L.append(a)
       return L


4.9.2. Argumentos nomeados
--------------------------

Funções também podem ser chamadas usando *argumentos nomeados* da
forma "chave=valor". Por exemplo, a função a seguir:

   def papagaio(voltagem, estado='é um cadáver', ação='voar', tipo='Azul Norueguês'):
       print("-- Este papagaio não conseguiria", ação, end=' ')
       print("nem se você desse um choque de", voltagem, "de volts nele.")
       print("-- Plumagem formosa, o", tipo)
       print("-- Ele", estado, "!")

aceita um argumento obrigatório ("voltagem") e três argumentos
opcionais ("estado", "ação", e "tipo"). Esta função pode ser chamada
de qualquer uma dessas formas:

   papagaio(1000)                                        # 1 argumento posicional
   papagaio(voltagem=1000)                               # 1 argumento nomeado
   papagaio(voltagem=1000000, ação='fazer VOOOOOM')      # 2 argumentos nomeados
   papagaio(ação='fazer VOOOOOM', voltagem=1000000)      # 2 argumentos nomeados
   papagaio('um milhão', 'sem vida', 'pular')            # 3 argumentos posicionais
   papagaio('mil', estado='estaria no céu')              # 1 posicional, 1 argumento

mas todas as formas a seguir seriam inválidas:

   papagaio()                       # faltando argumento obrigatório
   papagaio(voltagem=5.0, 'morto')  # argumento não nomeado após um argumento nomeado
   papagaio(110, voltagem=220)      # valor duplicado para o mesmo argumento
   papagaio(ator='John Cleese')     # argumento nomeado desconhecido

Em uma chamada de função, argumentos nomeados devem vir depois dos
argumentos posicionais. Todos os argumentos nomeados passados devem
corresponder com argumentos aceitos pela função (ex. "ator" não é um
argumento nomeado válido para a função "papagaio"), mas sua ordem é
irrelevante. Isto também inclui argumentos obrigatórios (ex.:
"papagaio(voltagem=1000)" funciona). Nenhum argumento pode receber
mais de um valor. Eis um exemplo que não funciona devido a esta
restrição:

   >>> def função(a):
   ...     pass
   ...
   >>> função(0, a=0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: função() got multiple values for argument 'a'

Quando um último parâmetro formal no formato "**nome" está presente,
ele recebe um dicionário (veja Tipos mapeamentos --- dict, frozendict)
contendo todos os argumentos nomeados, exceto aqueles que correspondem
a um parâmetro formal. Isto pode ser combinado com um parâmetro formal
no formato "*nome" (descrito na próxima subseção) que recebe uma tupla
contendo os argumentos posicionais, além da lista de parâmetros
formais. ("*nome" deve ocorrer antes de "**nome".) Por exemplo, se
definirmos uma função assim:

   def loja_de_queijos(tipo, *argumentos, **argumentos_nomeados):
       print("-- Você tem algum", tipo, "?")
       print("-- Lamento, acabou o", tipo)
       for arg in argumentos:
           print(arg)
       print("-" * 40)
       for kw in argumentos_nomeados:
           print(kw, ":", argumentos_nomeados[kw])

Pode ser chamada assim:

   loja_de_queijos("Limburger", "Está muito mole, senhor",
              "Está realmente muito, MUITO mole, senhor.",
              vendedor="Michael Palin",
              cliente="John Cleese",
              sketch="Sketch da Loja de Queijos")

e, claro, exibiria:

   -- Você tem algum Limburger ?
   -- Lamento, acabou o Limburger
   Está muito mole, senhor.
   Está realmente muito, MUITO mole, senhor.
   ----------------------------------------
   vendedor : Michael Palin
   cliente : John Cleese
   sketch : Cheese Shop Sketch

Observe que a ordem em que os argumentos nomeados são exibidos é
garantida para corresponder à ordem em que foram fornecidos na chamada
da função.


4.9.3. Parâmetros especiais
---------------------------

Por padrão, argumentos podem ser passadas para uma função Python tanto
por posição quanto explicitamente pelo nome. Para uma melhor
legibilidade e desempenho, faz sentido restringir a maneira pelo qual
argumentos possam ser passados, assim um desenvolvedor precisa apenas
olhar para a definição da função para determinar se os itens são
passados por posição, por posição e nome, ou por nome.

A definição de uma função pode parecer com:

   def f(pos1, pos2, /, pos_ou_kwd, *, kwd1, kwd2):
         -----------    ----------     ----------
           |             |                  |
           |        Posicional ou nomeado   |
           |                                - Somente nomeado
            -- Somente posicional

onde "/" e "*" são opcionais. Se usados, esses símbolos indicam o tipo
de parâmetro pelo qual os argumentos podem ser passados para as
funções: somente-posicional, posicional-ou-nomeado, e somente-nomeado.
Parâmetros nomeados são também conhecidos como parâmetros palavra-
chave.


4.9.3.1. Argumentos posicional-ou-nomeados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se "/" e "*" não estão presentes na definição da função, argumentos
podem ser passados para uma função por posição ou por nome.


4.9.3.2. Parâmetros somente-posicionais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Olhando com um pouco mais de detalhes, é possível definir certos
parâmetros como *somente-posicional*. Se *somente-posicional*, a ordem
do parâmetro importa, e os parâmetros não podem ser passados por nome.
Parâmetros somente-posicional são colocados antes de "/" (barra). A
"/" é usada para logicamente separar os argumentos somente-posicional
dos demais parâmetros. Se não existe uma "/" na definição da função,
não existe parâmetros somente-posicionais.

Parâmetros após a "/" podem ser *posicional-ou-nomeado* ou *somente-
nomeado*.


4.9.3.3. Argumentos somente-nomeados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para definir parâmetros como *somente-nomeado*, indicando que o
parâmetro deve ser passado por argumento nomeado, colocamos um "*" na
lista de argumentos imediatamente antes do primeiro parâmetro
*somente-nomeado*.


4.9.3.4. Exemplos de funções
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Considere o seguinte exemplo de definição de função com atenção
redobrada para os marcadores "/" e "*":

   >>> def arg_padrão(arg):
   ...     print(arg)
   ...
   >>> def arg_somente_pos(arg, /):
   ...     print(arg)
   ...
   >>> def arg_somente_nom(*, arg):
   ...     print(arg)
   ...
   >>> def exemplo_combinado(somente_pos, /, padrão, *, somente_nom):
   ...     print(somente_pos, padrão, somente_nom)

A definição da primeira função, "arg_padrão", a forma mais familiar,
não coloca nenhuma restrição para a chamada da função e argumentos
podem ser passados por posição ou nome:

   >>> arg_padrão(2)
   2

   >>> arg_padrão(arg=2)
   2

A segunda função "arg_somente_pos" está restrita ao uso de parâmetros
somente posicionais, uma vez que existe uma "/" na definição da
função:

   >>> arg_somente_pos(1)
   1

   >>> arg_somente_pos(arg=1)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: arg_somente_pos() got some positional-only arguments passed as keyword arguments: 'arg'

A terceira função "arg_somente_nom" permite somente argumentos
nomeados como indicado pelo "*" na definição da função:

   >>> arg_somente_nom(3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: arg_somente_nom() takes 0 positional arguments but 1 was given

   >>> arg_somente_nom(arg=3)
   3

E a última usa as três convenções de chamada na mesma definição de
função:

   >>> exemplo_combinado(1, 2, 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: exemplo_combinado() takes 2 positional arguments but 3 were given

   >>> exemplo_combinado(1, 2, somente_nom=3)
   1 2 3

   >>> exemplo_combinado(1, padrão=2, somente_nom=3)
   1 2 3

   >>> exemplo_combinado(somente_pos=1, padrão=2, somente_nom=3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: exemplo_combinado() got some positional-only arguments passed as keyword arguments: 'somente_pos'

Finalmente, considere essa definição de função que possui uma
potencial colisão entre o argumento posicional "nome" e "**kwds" que
possui "nome" como uma chave:

   def foo(nome, **kwds):
       return 'nome' in kwds

Não é possível essa chamada devolver "True", uma vez que o argumento
nomeado "'nome'" sempre será aplicado para o primeiro parâmetro. Por
exemplo:

   >>> foo(1, **{'nome': 2})
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: foo() got multiple values for argument 'nome'
   >>>

Mas usando "/" (argumentos somente-posicionais), isso é possível já
que permite "nome" como um argumento posicional e "'nome'" como uma
chave nos argumentos nomeados:

   >>> def foo(nome, /, **kwds):
   ...     return 'nome' in kwds
   ...
   >>> foo(1, **{'nome': 2})
   True

Em outras palavras, o nome de parâmetros somente-posicional podem ser
usados em "**kwds" sem ambiguidade.


4.9.3.5. Recapitulando
~~~~~~~~~~~~~~~~~~~~~~

A situação irá determinar quais parâmetros usar na definição da
função:

   def f(pos1, pos2, /, pos_ou_nom *, nom1, nom2):

Como guia:

* Use somente-posicional se você não quer que o nome do parâmetro
  esteja disponível para o usuário. Isso é útil quando nomes de
  parâmetros não tem um significado real, se você quer forçar a ordem
  dos argumentos da função quando ela é chamada ou se você precisa ter
  alguns parâmetros posicionais e alguns nomeados.

* Use somente-nomeado quando os nomes tem significado e a definição da
  função fica mais clara deixando esses nomes explícitos ou se você
  quer evitar que usuários confiem na posição dos argumentos que estão
  sendo passados.

* Para uma API, use somente-posicional para evitar quebras na mudança
  da API se os nomes dos parâmetros forem alterados no futuro.


4.9.4. Listas de argumentos arbitrárias
---------------------------------------

Finalmente, a opção menos usada é especificar que a função pode ser
chamada com um número arbitrário de argumentos. Esses argumentos serão
empacotados em uma tupla (ver Tuplas e Sequências). Antes dos
argumentos em número variável, zero ou mais argumentos normais podem
estar presentes.

   def escreve_vários_itens(arquivo, separador, *args):
       file.write(separador.join(args))

Normalmente, esses argumentos *variádicos* estarão no final da lista
de parâmetros formais, porque eles englobam todos os argumentos de
entrada restantes, que são passados para a função. Quaisquer
parâmetros formais que ocorrem após o parâmetro "*args" são argumentos
'somente-nomeados' , o que significa que eles só podem ser usados como
chave-valor, em vez de argumentos posicionais:

   >>> def concat(*args, sep="/"):
   ...     return sep.join(args)
   ...
   >>> concat("terra", "marte", "vênus")
   'terra/marte/vênus'
   >>> concat("terra", "marte", "vênus", sep=".")
   'terra.marte.vênus'


4.9.5. Desempacotando listas de argumentos
------------------------------------------

A situação inversa ocorre quando os argumentos já estão numa lista ou
tupla mas ela precisa ser explodida para invocarmos uma função que
requer argumentos posicionais separados. Por exemplo, a função
"range()" espera argumentos separados, *start* e *stop*. Se os valores
já estiverem juntos em uma lista ou tupla, escreva a chamada de função
com o operador "*" para desempacotá-los da sequência:

   >>> list(range(3, 6))            # chamada normal com argumentos separados
   [3, 4, 5]
   >>> args = [3, 6]
   >>> list(range(*args))           # chamada com argumentos desempacotados a partir de uma lista
   [3, 4, 5]

Da mesma forma, dicionários podem produzir argumentos nomeados com o
operador "**":

   >>> def papagaio(voltagem, estado='um cadáver', ação='voar'):
   ...     print("-- Este papagaio não conseguiria", ação, end=' ')
   ...     print("nem se você desse um choque de", voltagem, "de volts nele.", end=' ')
   ...     print("Ele", estado, "!")
   ...
   >>> d = {"voltagem": "quatro milhões", "estado": "está realmente morto", "ação": "voar"}
   >>> papagaio(**d)
   -- Este papagaio não conseguiria voar nem se você desse um choque de quatro milhões de volts nele. Ele está realmente morto !


4.9.6. Expressões lambda
------------------------

Pequenas funções anônimas podem ser criadas com a palavra-chave
"lambda". Esta função retorna a soma de seus dois argumentos: "lambda
a, b: a+b". As funções lambda podem ser usadas sempre que objetos
função forem necessários. Eles são sintaticamente restritos a uma
única expressão. Semanticamente, eles são apenas açúcar sintático para
uma definição de função normal. Como definições de funções aninhadas,
as funções lambda podem referenciar variáveis contidas no escopo:

   >>> def cria_incrementador(n):
   ...     return lambda x: x + n
   ...
   >>> f = cria_incrementador(42)
   >>> f(0)
   42
   >>> f(1)
   43

O exemplo acima usa uma expressão lambda para retornar uma função.
Outro uso é passar uma pequena função como um argumento. Por exemplo,
"list.sort()" recebe uma função chave de ordenação *key* que pode ser
uma função lambda:

   >>> pairs = [(1, 'um'), (2, 'dois'), (3, 'três), (4, 'quatro')]
   >>> pairs.sort(key=lambda pair: pair[1])
   >>> pairs
   [(4, 'quatro'), (1, 'um'), (3, 'três'), (2, 'dois')]


4.9.7. Strings de documentação
------------------------------

Aqui estão algumas convenções sobre o conteúdo e formatação de strings
de documentação, também conhecidas como docstrings.

A primeira linha deve sempre ser curta, um resumo conciso do propósito
do objeto. Por brevidade, não deve explicitamente se referir ao nome
ou tipo do objeto, uma vez que estas informações estão disponíveis por
outros meios (exceto se o nome da função for o próprio verbo que
descreve a finalidade da função). Essa linha deve começar com letra
maiúscula e terminar com ponto.

Se existem mais linhas na string de documentação, a segunda linha deve
estar em branco, separando visualmente o resumo do resto da descrição.
As linhas seguintes devem conter um ou mais parágrafos descrevendo as
convenções de chamada ao objeto, seus efeitos colaterais, etc.

A analisador sintático do Python remove a indentação de literais de
string multilinha quando estas servem como docstrings de módulos,
classes ou funções.

Eis um exemplo de uma string de documentação multilinha:

   >>> def minha_função():
   ...     """Faz nada, mas documentemos-a.
   ...
   ...     Falando sério, ele faz nada:
   ...
   ...         >>> minha_função()
   ...         >>>
   ...     """
   ...     pass
   ...
   >>> print(minha_função.__doc__)
   Faz nada, mas documentemos-a.

   Falando sério, ele faz nada:

       >>> minha_função()
       >>>


4.9.8. Anotações de função
--------------------------

Anotações de função são informações de metadados completamente
opcionais sobre os tipos usados pelas funções definidas pelo usuário
(veja **PEP 3107** e **PEP 484** para mais informações).

*Anotações* são armazenadas no atributo "__annotations__" da função
como um dicionário e não tem nenhum efeito em qualquer outra parte da
função. Anotações de parâmetro são definidas por dois-pontos (":")
após o nome do parâmetro, seguida por uma expressão que quando
avaliada determina o valor da anotação. Anotações do tipo do retorno
são definidas por um literal "->", seguida por uma expressão, entre a
lista de parâmetro e os dois-pontos que marcam o fim da instrução
"def" . O exemplo a seguir possui um argumento obrigatório, um
argumento opcional e o valor de retorno anotados:

   >>> def f(ham: str, ovos: str = 'ovos') -> str:
   ...     print("Anotações:", f.__annotations__)
   ...     print("Argumentos:", ham, ovos)
   ...     return ham + ' e ' + ovos
   ...
   >>> f('spam')
   Anotações: {'ham': <class 'str'>, 'return': <class 'str'>, 'ovos': <class 'str'>}
   Argumentos: spam ovos
   'spam e ovos'


4.10. Intermezzo: estilo de codificação
=======================================

Agora que está prestes a escrever códigos mais longos e complexos em
Python, é um bom momento para falar sobre *estilo de codificação*. A
maioria das linguagens podem ser escritas (ou *formatadas*) em
diferentes estilos; alguns são mais legíveis do que outros. Tornar o
seu código mais fácil de ler, para os outros, é sempre uma boa ideia,
e adotar um estilo de codificação agradável ajuda bastante.

Em Python, a **PEP 8** tornou-se o guia de estilo adotado pela maioria
dos projetos; promove um estilo de codificação muito legível e
visualmente agradável. Todo desenvolvedor Python deve lê-lo em algum
momento; eis os pontos mais importantes, selecionados para você:

* Use indentação com 4 espaços, e não use tabulações.

  4 espaços são um bom meio termo entre indentação estreita (permite
  maior profundidade de aninhamento) e indentação larga (mais fácil de
  ler). Tabulações trazem complicações, e o melhor é não usar.

* Quebre as linhas de modo que não excedam 79 caracteres.

  Isso ajuda os usuários com telas pequenas e torna possível abrir
  vários arquivos de código lado a lado em telas maiores.

* Deixe linhas em branco para separar funções e classes, e blocos de
  código dentro de funções.

* Quando possível, coloque comentários em uma linha própria.

* Escreva strings de documentação.

* Use espaços ao redor de operadores e após vírgulas, mas não
  diretamente dentro de parênteses, colchetes e chaves: "a = f(1, 2) +
  g(3, 4)".

* Nomeie suas classes e funções de forma consistente; a convenção é
  usar "MaiusculoCamelCase" para classes e "minusculo_com_sublinhado"
  para funções e métodos. Sempre use "self" como o nome para o
  primeiro argumento dos métodos (veja Uma primeira olhada nas classes
  para mais informações sobre classes e métodos).

* Não use codificações exóticas se o seu código é feito para ser usado
  em um contexto internacional. O padrão do Python, UTF-8, ou mesmo
  ASCII puro funciona bem em qualquer caso.

* Da mesma forma, não use caracteres não-ASCII em identificadores se
  houver apenas a menor chance de pessoas falando um idioma diferente
  ler ou manter o código.

-[ Notas de rodapé ]-

[1] Na verdade, *passagem por referência para objeto* seria uma
    descrição melhor, pois, se um objeto mutável for passado, quem
    chamou verá as alterações feitas por quem foi chamado (por
    exemplo, a inclusão de itens em uma lista).
