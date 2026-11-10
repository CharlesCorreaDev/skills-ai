FAQ sobre programação
*********************


General questions
=================


Is there a source code-level debugger with breakpoints and single-stepping?
---------------------------------------------------------------------------

Sim.

Vários depuradores para Python estão descritos abaixo, e a função
embutida "breakpoint()" permite que você caia em qualquer um desses
pontos.

O módulo pdb é um depurador em modo Console simples, mas adequado,
para o Python. Faz parte da biblioteca padrão do Python e está
documentado no "manual de referencia da biblioteca". Você também pode
construir do seu próprio depurador usando o código do pdb como um
exemplo.

The IDLE interactive development environment, which is part of the
standard Python distribution (normally available as "idlelib"),
includes a graphical debugger.

O PythonWin é uma IDE feita para o Python que inclui um depurador
gráfico baseado no pdb. O depurador do PythonWin colore os pontos de
interrupção e tem alguns recursos legais, como a depuração de
programas que não são PythonWin. O PythonWin está disponível como
parte do projeto pywin32 e como parte da distribuição ActivePython.

Eric é uma IDE construída com PyQt e o componente de edição Scintilla.

trepan3k é um depurador similar ao gdb.

Visual Studio Code é uma IDE com ferramentas de depuração integrada
com softwares de controle de versão.

Há uma série de IDE comerciais para desenvolvimento com o Python que
inclui depuradores gráficos. Dentre tantas temos:

* Wing IDE

* PyCharm


Existem ferramentas para ajudar a encontrar bugs ou fazer análise estática de desempenho?
-----------------------------------------------------------------------------------------

Sim.

Ruff, Pylint and Pyflakes do basic checking that will help you catch
bugs sooner.

Static type checkers such as mypy, ty, Pyrefly, and pytype can check
type hints in Python source code.


Como posso criar um binário independente a partir de um script Python?
----------------------------------------------------------------------

Você não precisa possuir a capacidade de compilar o código Python para
C se o que deseja é um programa autônomo que os usuários possam baixar
e executar sem ter que instalar a distribuição Python primeiro.
Existem várias ferramentas que determinam o conjunto de módulos
exigidos por um programa e vinculam esses módulos ao binário do Python
para produzir um único executável.

One is to use the freeze tool, which is included in the Python source
tree as Tools/freeze. It converts Python byte code to C arrays; with a
C compiler you can embed all your modules into a new program, which is
then linked with the standard Python modules.

A *freeze* trabalha percorrendo seu código recursivamente, procurando
por instruções de importação (ambas as formas), e procurando por
módulos tanto no caminho padrão do Python, quanto por módulos
embutidos no diretório fonte. Ela então transforma o *bytecode* de
módulos Python em código C (inicializadores de vetor que podem ser
transformados em objetos código usando o módulo *marshal*), e depois
cria um arquivo de configurações personalizado que só contém os
módulos embutidos usados no programa. A ferramenta então compila os
códigos C e os vincula como o resto do interpretador Python, formando
um binário autônomo que funciona exatamente como seu *script*.

Os pacotes a seguir podem ajudar com a criação dos executáveis do
console e da GUI:

* Nuitka (Multiplataforma)

* PyInstaller (Multiplataforma)

* PyOxidizer (Multiplataforma)

* cx_Freeze (Multiplataforma)

* py2app (somente macOS)

* py2exe (somente Windows)


Existem padrões para a codificação ou um guia de estilo utilizado pela comunidade Python?
-----------------------------------------------------------------------------------------

Sim. O guia de estilo esperado para módulos e biblioteca padrão possui
o nome de PEP8 e você pode acessar a sua documentação em **PEP 8**.


Core language
=============


Porque recebo o erro UnboundLocalError quando a variável possui um valor associado?
-----------------------------------------------------------------------------------

Pode ser uma surpresa obter a exceção "UnboundLocalError" em um código
previamente funcional quando adicionamos uma instrução de atribuição
em algum lugar no corpo de uma função.

Este código:

>>> x = 10
>>> def bar():
...     print(x)
...
>>> bar()
10

funciona, mas este código:

>>> x = 10
>>> def foo():
...     print(x)
...     x += 1

resulta em uma "UnboundLocalError":

>>> foo()
Traceback (most recent call last):
  ...
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

Isso acontece porque, quando atribuímos um valor a uma variável em
determinado escopo, essa variável torna-se local desse escopo,
acabando por esconder qualquer outra variável de mesmo nome no escopo
externo. Como a última instrução em foo atribui um novo valor a "x", o
interpretador a reconhece como uma variável local. Consequentemente,
quando o "print(x)" anterior tentar exibir a variável local não
inicializada, um erro aparece.

No exemplo acima, podemos acessar a variável do escopo externo
declarando-a como global:

>>> x = 10
>>> def foobar():
...     global x
...     print(x)
...     x += 1
...
>>> foobar()
10

Esta declaração explícita é necessária para lembrarmos que estamos
modificando o valor da variável no escopo externo (ao contrário da
situação superficialmente análoga com variáveis de classe e
instância):

>>> print(x)
11

Podemos fazer algo parecido num escopo aninhado usando a palavra
reservada "nonlocal":

>>> def foo():
...    x = 10
...    def bar():
...        nonlocal x
...        print(x)
...        x += 1
...    bar()
...    print(x)
...
>>> foo()
10
11


Quais são as regras para variáveis locais e globais em Python?
--------------------------------------------------------------

Em Python, as variáveis que são apenas utilizadas (referenciadas)
dentro de uma função são implicitamente globais. Se uma variável for
associada a um valor em qualquer lugar dentro do corpo da função,
presume-se que a mesma seja local, a menos que seja explicitamente
declarada como global.

Embora um pouco surpreendente no início, um momento de consideração
explica isso. Por um lado, exigir "global" para variáveis atribuídas
fornece uma barreira contra efeitos colaterais indesejados. Por outro
lado, se "global" fosse necessário para todas as referências globais,
você estaria usando "global" o tempo todo. Você teria que declarar
como global todas as referências a uma função embutida ou a um
componente de um módulo importado. Essa desordem anularia a utilidade
da declaração de "global" para identificar efeitos colaterais.


Por que os lambdas definidos em um laço com valores diferentes retornam o mesmo resultado?
------------------------------------------------------------------------------------------

Assume you use a for loop to define a few different lambdas (or even
plain functions), for example:

   >>> squares = []
   >>> for x in range(5):
   ...     squares.append(lambda: x**2)

Isso oferece uma lista que contém 5 lambdas que calculam "x**2". Você
pensar que, quando invocado, os mesmos retornam, respectivamente, "0",
"1", "4", "9", e "16". No entanto, quando realmente tentar, vai ver
que todos retornam "16":

   >>> squares[2]()
   16
   >>> squares[4]()
   16

This happens because "x" is not local to the lambdas, but is defined
in the outer scope, and it is accessed when the lambda is called ---
not when it is defined.  At the end of the loop, the value of "x" is
"4", so all the functions now return "4**2", that is "16".  You can
also verify this by changing the value of "x" and see how the results
of the lambdas change:

   >>> x = 8
   >>> squares[2]()
   64

Para evitar isso, é necessário salvar os valores nas variáveis locais
para os lambdas, para que eles não dependam do valor de "x" global:

   >>> squares = []
   >>> for x in range(5):
   ...     squares.append(lambda n=x: n**2)

Aqui, "n=x" cria uma nova variável "n" local para o lambda e é
calculada quando o lambda é definido para que ele tenha o mesmo valor
que "x" tem nesse ponto no laço. Isso significa que o valor de "n"
será "0" no primeiro "ciclo" do lambda, "1" no segundo "ciclo", "2" no
terceiro, e assim por diante. Portanto, cada lambda agora retornará o
resultado correto:

   >>> squares[2]()
   4
   >>> squares[4]()
   16

Observe que esse comportamento não é peculiar dos lambdas, o mesmo
também ocorre com as funções regulares.


Como definir variáveis globais dentro de módulos?
-------------------------------------------------

A maneira canônica de compartilhar informações entre módulos dentro de
um único programa é criando um módulo especial (geralmente chamado de
config ou cfg). Basta importar o módulo de configuração em todos os
módulos da sua aplicação; o módulo ficará disponível como um nome
global. Como há apenas uma instância de cada módulo, todas as
alterações feitas no objeto do módulo se refletem em todos os lugares.
Por exemplo:

config.py:

   x = 0   # Valor padrão para a configuração de 'x'

mod.py:

   import config
   config.x = 1

main.py:

   import config
   import mod
   print(config.x)

Note que usar um módulo também é a base para a implementação do padrão
de projeto Singleton, pela mesma razão.


Quais são as "melhores práticas" quando fazemos uso da importação de módulos?
-----------------------------------------------------------------------------

Em geral, não use "from nomemódulo import *". Isso desorganiza o
espaço de nomes do importador e torna muito mais difícil para as
ferramentas de análise estática detectarem nomes indefinidos.

Faça a importação de módulos na parte superior do arquivo. Isso deixa
claro quais outros módulos nosso código necessita e evita dúvidas
sobre, por exemplo, se o nome do módulo está no escopo. Usar uma
importação por linha facilita a adição e exclusão de importações de
módulos, porém, usar várias importações num única linha, ocupa menos
espaço da tela.

É uma boa prática importar os módulos na seguinte ordem:

1. standard library modules -- such as "sys", "os", "argparse", "re"

2. third-party library modules (anything installed in Python's site-
   packages directory) -- such as dateutil, requests, tzdata

3. módulos desenvolvidos localmente

Às vezes, é necessário transferir as importações para uma função ou
classe para evitar problemas com importação circular. Gordon McMillan
diz:

   As importações circulares vão bem onde ambos os módulos utilizam a
   forma de importação "import <módulo>". Elas falham quando o 2º
   módulo quer pegar um nome do primeiro ("from módulo import nome") e
   a importação está no nível superior. Isso porque os nomes no
   primeiro ainda não estão disponíveis, porque o 1º módulo está
   ocupado importando o 2º.

Nesse caso, se o segundo módulo for usado apenas numa função, a
importação pode ser facilmente movida para dentro do escopo dessa
função. No momento em que a importação for chamada, o primeiro módulo
terá finalizado a inicialização e o segundo módulo poderá ser
importado sem maiores complicações.

Também poderá ser necessário mover as importações para fora do nível
superior do código se alguns dos módulos forem específicos de uma
determinada plataforma (SO). Nesse caso, talvez nem seja possível
importar todos os módulos na parte superior do arquivo. Nessas
situações devemos importar os módulos que são específicos de cada
plataforma antes de necessitar utilizar os mesmos.

Apenas mova as importações para um escopo local, como dentro da
definição de função, se for necessário resolver algum tipo de
problema, como, por exemplo, evitar importações circulares ou tentar
reduzir o tempo de inicialização do módulo. Esta técnica é
especialmente útil se muitas das importações forem desnecessárias,
dependendo de como o programa é executado. Também podemos desejar
mover as importações para uma função se os módulos forem usados
somente nessa função. Note que carregar um módulo pela primeira vez
pode ser demorado devido ao tempo de inicialização de cada módulo, no
entanto, carregar um módulo várias vezes é praticamente imperceptível,
tendo somente o custo de processamento de pesquisas no dicionário de
nomes. Mesmo que o nome do módulo tenha saído do escopo, o módulo
provavelmente estará disponível em "sys.modules".


Por que os valores padrão são compartilhados entre objetos?
-----------------------------------------------------------

Este tipo de erro geralmente pega programadores neófitos. Considere
esta função:

   def foo(meudict={}):  # Perigo: referência compartilhada a um dicionário para todas as chamadas
       ... faz alguma coisa ...
       meudict[chave] = valor
       return meudict

Na primeira vez que chamar essa função, "meudict" vai conter um único
item. Na segunda vez, "meudict" vai conter dois itens porque, quando
"foo()" começar a ser executado, "meudict" começará com um item já
existente.

Muitas vezes, espera-se que ao invocar uma função sejam criados novos
objetos referente aos valores padrão. Isso não é o que acontece. Os
valores padrão são criados exatamente uma vez, quando a função está
sendo definida. Se esse objeto for alterado, como o dicionário neste
exemplo, as chamadas subsequentes para a essa função se referirão a
este objeto alterado.

Por definição, objetos imutáveis, como números, strings, tuplas e o
"None", estão protegidos de sofrerem alteração. Alterações em objetos
mutáveis, como dicionários, listas e instâncias de classe, podem levar
à confusão.

Por causa desse recurso, é uma boa prática de programação para evitar
o uso de objetos mutáveis contendo valores padrão. Em vez disso,
utilize "None" como o valor padrão e dentro da função, verifique se o
parâmetro é "None" e crie uma nova lista, dicionário ou o que quer que
seja. Por exemplo, escreva o seguinte código:

   def foo(meudict={}):
       ...

mas:

   def foo(meudict=None):
       if meudict is None:
           meudict = {}  # cria um novo dicionário para o espaço de nomes local

Esse recurso pode ser útil. Quando se tem uma função que consome muito
tempo para calcular, uma técnica comum é armazenar em cache os
parâmetros e o valor resultante de cada chamada para a função e
retornar o valor em cache se o mesmo valor for solicitado novamente.
Isso se chama "memoizar", e pode ser implementado da seguinte forma:

   # Chamadores só podem fornecer dois parâmetros e opcionalmente passar _cache como parâmetro nomeado
   def expensive(arg1, arg2, *, _cache={}):
       if (arg1, arg2) in _cache:
           return _cache[(arg1, arg2)]

       # Cacula o valor
       result = ... cálculo custoso ...
       _cache[(arg1, arg2)] = result           # Armazena o resultado no cache
       return result

Pode-se usar uma variável global contendo um dicionário ao invés do
valor padrão; isso é uma questão de gosto.


Como passo parâmetros opcionais ou parâmetros nomeados de uma função para outra?
--------------------------------------------------------------------------------

Colete os argumentos usando os especificadores "*" ou "**" na lista de
parâmetros da função. Isso faz com que os argumentos posicionais como
tupla e os argumentos nomeados sejam passados como um dicionário. Você
pode, também, passar esses argumentos ao invocar outra função usando
"*" e "**":

   def f(x, *args, **kwargs):
       ...
       kwargs['width'] = '14.3c'
       ...
       g(x, *args, **kwargs)


Qual a diferença entre argumentos e parâmetros?
-----------------------------------------------

*Parâmetros* são definidos pelos nomes que aparecem na definição da
função, enquanto *argumentos* são os valores que serão passados para a
função no momento em que esta estiver sendo invocada. Os parâmetros
irão definir quais os *tipos de argumentos* que uma função pode
receber. Por exemplo, dada a definição da função:

   def func(foo, bar=None, **kwargs):
       pass

*foo*, *bar* e *kwargs* são parâmetros de "func". Dessa forma, ao
invocar "func", por exemplo:

   func(42, bar=314, extra=algumvalor)

os valores "42", "314", e "algumvalor" são os argumentos.


Por que ao alterar a lista 'y' também altera a lista 'x'?
---------------------------------------------------------

Se você escreveu um código como:

   >>> x = []
   >>> y = x
   >>> y.append(10)
   >>> y
   [10]
   >>> x
   [10]

pode estar se perguntando por que acrescentar um elemento a "y" também
mudou "x".

Há dois fatores que produzem esse resultado:

1. As variáveis são simplesmente nomes que referem-se a objetos. Usar
   "y = x" não cria uma cópia da lista. Isso cria uma nova variável
   "y" que faz referência ao mesmo objeto ao qual "x" está se
   referindo. Isso significa que existe apenas um objeto (a lista) e
   que ambos "x" e "y" fazem referência a ele.

2. Listas são objetos *mutáveis*, o que significa que você pode
   alterar o seu conteúdo.

Após a chamada para "append()", o conteúdo do objeto mutável mudou de
"[]" para "[10]". Uma vez que ambas as variáveis referem-se ao mesmo
objeto, usar qualquer um dos nomes acessará o valor modificado "[10]".

Se por acaso, atribuímos um objeto imutável a "x":

   >>> x = 5  # ints são imutáveis
   >>> y = x
   >>> x = x + 1  # 5 não pode ser mutado, estamos criando um novo objeto aqui
   >>> x
   6
   >>> y
   5

podemos ver que nesse caso "x" e "y" não são mais iguais. Isso ocorre
porque os números inteiros são *imutáveis*, e quando fazemos "x = x +
1" não estamos mudando o int "5" e incrementando o seu valor. Em vez
disso, estamos criando um novo objeto (o int "6") e atribuindo-o a "x"
(isto é, mudando para o objeto no qual "x" se refere). Após esta
atribuição, temos dois objetos (os ints "6" e "5") e duas variáveis
que referem-se a elas ("x" agora se refere a "6", mas "y" ainda
refere-se a "5").

Algumas operações (por exemplo, "y.append(10)" e "y.sort()") alteram o
objeto, enquanto operações superficialmente semelhantes (por exemplo,
"y = y + [10]" e "sorted(y)") criam um novo objeto. Em geral, em
Python (e em todos os casos na biblioteca padrão) um método que causa
mutação em um objeto retornará "None" para ajudar a evitar confundir
os dois tipos de operações. Portanto, se você escrever por engano
"y.sort()" pensando que lhe dará uma cópia ordenada de "y", você
terminará com "None", o que provavelmente fará com que seu programa
gere um erro facilmente diagnosticado.

No entanto, há uma classe de operações em que a mesma operação às
vezes tem comportamentos diferentes com tipos diferentes: os
operadores de atribuição aumentada. Por exemplo, "+=" transforma
listas, mas não tuplas ou ints ("uma_lista += [1, 2, 3]" equivale a
"uma_lista.extend([1, 2, 3])" a transforma "uma_lista", sendo que
"alguma_tupla += (1, 2, 3)" e "algum_int += 1" cria novos objetos).

Em outras palavras:

* If we have a mutable object (such as "list", "dict", "set"), we can
  use some specific operations to mutate it and all the variables that
  refer to it will see the change.

* If we have an immutable object (such as "str", "int", "tuple"), all
  the variables that refer to it will always see the same value, but
  operations that transform that value into a new value always return
  a new object.

Caso queira saber se duas variáveis fazem referência ao mesmo objeto
ou não, pode-se usar o operador "is" ou a função embutida "id()".


Como escrevo uma função com parâmetros de saída (chamada por referência)?
-------------------------------------------------------------------------

Remember that arguments are passed by assignment in Python.  Since
assignment just creates references to objects, there's no alias
between an argument name in the caller and callee, and consequently no
call-by-reference.  You can achieve the desired effect in a number of
ways.

1. Retornando um tupla com os resultados:

      >>> def func1(a, b):
      ...     a = 'valor-novo'       # a e b são nomes locais
      ...     b = b + 1              # atribuídos a novos objetos
      ...     return a, b            # retorna novos valores
      ...
      >>> x, y = 'valor-antigo', 99
      >>> func1(x, y)
      ('valor-novo', 100)

   Esta é quase sempre a solução mais clara.

2. Utilizando variáveis globais. Essa forma não é segura para thread
   e, portanto, não é recomendada.

3. Pela passagem de um objeto mutável (que possa ser alterado
   internamente):

      >>> def func2(a):
      ...     a[0] = 'valor-novo'    # 'a' referencia uma lista mutável
      ...     a[1] = a[1] + 1        # altera um objeto compartilhado
      ...
      >>> args = ['valor-antigo', 99]
      >>> func2(args)
      >>> args
      ['valor-novo', 100]

4. Pela passagem de um dicionário que sofra mutação:

      >>> def func3(args):
      ...     args['a'] = 'valor-novo'     # args é um dicionário mutável
      ...     args['b'] = args['b'] + 1   # alteração local, nele mesmo
      ...
      >>> args = {'a': 'valor-antigo', 'b': 99}
      >>> func3(args)
      >>> args
      {'a': 'valor-novo', 'b': 100}

5. Ou agrupando valores numa instância de classe:

      >>> class Namespace:
      ...     def __init__(self, /, **args):
      ...         for key, value in args.items():
      ...             setattr(self, key, value)
      ...
      >>> def func4(args):
      ...     args.a = 'valor-novo'        # args é um Namespace mutável
      ...     args.b = args.b + 1         # alteração local do objeto, nele mesmo
      ...
      >>> args = Namespace(a='valor-antigo', b=99)
      >>> func4(args)
      >>> vars(args)
      {'a': 'valor-novo', 'b': 100}

   Quase nunca existe uma boa razão para complicar isso.

A sua melhor escolha será retornar uma tupla contendo os múltiplos
resultados.


Como fazer uma função de ordem superior em Python?
--------------------------------------------------

Existem duas opções: pode-se usar escopos aninhados ou usar objetos
chamáveis. Por exemplo, suponha que queira definir "linear(a,b)", o
qual retorna uma função "f(x)" que calcula o valor "a*x+b". Usando
escopos aninhados, temos:

   def linear(a, b):
       def result(x):
           return a * x + b
       return result

Ou utilizando um objeto chamável:

   class linear:

       def __init__(self, a, b):
           self.a, self.b = a, b

       def __call__(self, x):
           return self.a * x + self.b

Em ambos os casos:

   taxas = linear(0.3, 2)

resulta em um objeto chamável, onde "taxes(10e6) == 0.3 * 10e6 + 2".

A abordagem do objeto chamável tem a desvantagem de que é um pouco
mais lenta e resulta num código ligeiramente mais longo. No entanto,
note que uma coleção de chamáveis pode compartilhar sua assinatura via
herança:

   class exponential(linear):
       # __init__ herdado
       def __call__(self, x):
           return self.a * (x ** self.b)

Objetos podem encapsular o estado para vários métodos:

   class counter:

       value = 0

       def set(self, x):
           self.value = x

       def up(self):
           self.value = self.value + 1

       def down(self):
           self.value = self.value - 1

   count = counter()
   inc, dec, reset = count.up, count.down, count.set

Aqui "inc()", "dec()" e "reset()" funcionam como funções que
compartilham a mesma variável contadora.


Como faço para copiar um objeto no Python?
------------------------------------------

Basicamente, tente utilizar a função "copy.copy()" ou a função
"copy.deepcopy()" para casos gerais. Nem todos os objetos podem ser
copiados, mas a maioria poderá.

Alguns objetos podem ser copiados com mais facilidade. Os dicionários
têm um método "copy()":

   novodict = antigodict.copy()

As sequências podem ser copiadas através do uso de fatiamento:

   nova_l = l[:]


Como posso encontrar os métodos ou atributos de um objeto?
----------------------------------------------------------

Para uma instância "x" de uma classe definida pelo usuário, "dir(x)"
retorna uma lista organizada alfabeticamente dos nomes contidos, os
atributos da instância e os métodos e atributos definidos por sua
classe.


Como que o meu código pode descobrir o nome de um objeto?
---------------------------------------------------------

De um modo geral, não pode, porque os objetos realmente não têm nomes.
Essencialmente, a atribuição sempre liga um nome a um valor; o mesmo é
verdade para as instruções "def" e "class", mas nesse caso o valor é
um chamável. Considere o seguinte código:

   >>> class A:
   ...     pass
   ...
   >>> B = A
   >>> a = B()
   >>> b = a
   >>> print(b)
   <__main__.A object at 0x16D07CC>
   >>> print(a)
   <__main__.A object at 0x16D07CC>

Provavelmente, a classe tem um nome: mesmo que seja vinculada a dois
nomes e invocada através do nome "B", a instância criada ainda é
relatada como uma instância da classe "A". No entanto, é impossível
dizer se o nome da instância é "a" ou "b", uma vez que ambos os nomes
estão vinculados ao mesmo valor.

De um modo geral, não deveria ser necessário que o seu código "conheça
os nomes" de valores específicos. A menos que se escreva
deliberadamente programas introspectivos, isso geralmente é uma
indicação de que uma mudança de abordagem pode ser benéfica.

Em comp.lang.python, Fredrik Lundh deu uma excelente analogia em
resposta a esta pergunta:

   Da mesma forma que você pega o nome daquele gato que encontrou na
   sua varanda: o próprio gato (objeto) não pode lhe dizer o seu nome,
   e ele realmente não se importa -- então, a única maneira de
   descobrir como ele se chama é perguntar a todos os seus vizinhos
   (espaços de nomes) se é o gato deles (objeto)...

   ....e não fique surpreso se você descobrir que é conhecido por
   muitos nomes, ou até mesmo nenhum nome.


O que há com a precedência do operador vírgula?
-----------------------------------------------

A vírgula não é um operador em Python. Considere este código:

   >>> "a" in "b", "a"
   (False, 'a')

Uma vez que a vírgula não seja um operador, mas um separador entre as
expressões acima, o código será avaliado como se tivéssemos entrado:

   ("a" in "b"), "a"

não:

   "a" in ("b", "a")

The same is true of the various assignment operators ("=", "+=", and
so on). They are not truly operators but syntactic delimiters in
assignment statements.


Existe um equivalente ao operador ternário "?:" do C?
-----------------------------------------------------

Sim, existe. A sintaxe é a seguinte:

   [quando_verdadeiro] if [expressão] else [quando_falso]

   x, y = 50, 25
   small = x if x < y else y

Antes que essa sintaxe fosse introduzida no Python 2.5, uma expressão
comum era usar operadores lógicos:

   [expressão] and [quando_verdadeiro] or [quando_falso]

No entanto, essa forma não é segura, pois pode dar resultados
inesperados quando *quando_verdadeiro* tiver um valor booleano falso.
Portanto, é sempre melhor usar a forma "... if ... else ...".


É possível escrever instruções de uma só linha ofuscadas em Python?
-------------------------------------------------------------------

Sim. Normalmente, isso é feito aninhando "lambda" dentro de "lambda".
Veja os três exemplos a seguir, ligeiramente adaptados de Ulf Bartelt:

   from functools import reduce

   # Primos < 1000
   print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
   map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))))

   # Primeiros 10 números de Fibonacci
   print(list(map(lambda x,f=lambda x,f:(f(x-1,f)+f(x-2,f)) if x>1 else 1:
   f(x,f), range(10))))

   # Conjunto de Mandelbrot
   print((lambda Ru,Ro,Iu,Io,IM,Sx,Sy:reduce(lambda x,y:x+'\n'+y,map(lambda y,
   Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,Sy=Sy,L=lambda yc,Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,i=IM,
   Sx=Sx,Sy=Sy:reduce(lambda x,y:x+y,map(lambda x,xc=Ru,yc=yc,Ru=Ru,Ro=Ro,
   i=i,Sx=Sx,F=lambda xc,yc,x,y,k,f=lambda xc,yc,x,y,k,f:(k<=0)or (x*x+y*y
   >=4.0) or 1+f(xc,yc,x*x-y*y+xc,2.0*x*y+yc,k-1,f):f(xc,yc,x,y,k,f):chr(
   64+F(Ru+x*(Ro-Ru)/Sx,yc,0,0,i)),range(Sx))):L(Iu+y*(Io-Iu)/Sy),range(Sy
   ))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 24))
   #    \___ ___/  \___ ___/  |   |   |__ linhas na tela
   #        V          V      |   |______ colunas na tela
   #        |          |      |__________ máximo de "interações"
   #        |          |_________________ faixa no eixo y
   #        |____________________________ faixa no eixo x

Não tente isso em casa, crianças!


O que a barra(/) na lista de parâmetros de uma função significa?
----------------------------------------------------------------

Uma barra na lista de argumentos de uma função indica que os
parâmetros anteriores a ela são somente-posicionais. Os parâmetros
somente-posicionais são aqueles que não têm nome utilizável
externamente. Ao chamar uma função que aceita parâmetros somente-
posicionais, os argumentos são mapeados para parâmetros com base
apenas em sua posição. Por exemplo, "divmod()" é uma função que aceita
parâmetros somente-posicionais. Sua documentação tem esta forma:

   >>> help(divmod)
   Help on built-in function divmod in module builtins:

   divmod(x, y, /)
       Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.

A barra no final da lista de parâmetros significa que ambos os
parâmetros são somente-posicionais. Assim, chamar "divmod()" com
argumentos nomeados levaria a um erro:

   >>> divmod(x=3, y=4)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: divmod() takes no keyword arguments


Números e strings
=================


Como faço para especificar números inteiros hexadecimais e octais?
------------------------------------------------------------------

Para especificar um dígito no formato octal, preceda o valor octal com
um zero e, em seguida, um "o" minúsculo ou maiúsculo. Por exemplo,
para definir a variável "a" para o valor octal "10" (8 em decimal),
digite:

   >>> a = 0o10
   >>> a
   8

Hexadecimal é bem fácil. Basta preceder o número hexadecimal com um
zero e, em seguida, um "x" minúsculo ou maiúsculo. Os dígitos
hexadecimais podem ser especificados em letras maiúsculas e
minúsculas. Por exemplo, no interpretador Python:

   >>> a = 0xa5
   >>> a
   165
   >>> b = 0XB2
   >>> b
   178


Por que -22 // 10 retorna -3?
-----------------------------

Esta dúvida é primariamente direcionado pelo desejo de que "i % j"
tenha o mesmo sinal que "j". Se quiser isso, e também quiser:

   i == (i // j) * j + (i % j)

então a divisão inteira deve retornar o piso. C também requer que essa
identidade seja mantida, e então os compiladores que truncarem "i //
j" precisam fazer com que "i % j" tenham o mesmo sinal que "i".

Existem poucos casos de uso reais para "i % j" quando "j" é negativo.
Quando "j" é positivo, existem muitos, e em virtualmente todos eles é
mais útil para "i % j" ser ">= 0". Se o relógio marca 10 agora, o que
dizia há 200 horas? "-190 % 12 == 2" é útil, enquanto "-190 % 12 ==
-10" é um bug esperando para morder.


Como obtenho um atributo de um literal int em vez de SyntaxError?
-----------------------------------------------------------------

Tentar obter um atributo de um literal "int" da maneira normal retorna
um "SyntaxError" porque o ponto é visto como um ponto decimal:

   >>> 1.__class__
     File "<stdin>", line 1
     1.__class__
      ^
   SyntaxError: invalid decimal literal

A solução é separar o literal do ponto com um espaço ou parênteses.

>>> 1 .__class__
<class 'int'>
>>> (1).__class__
<class 'int'>


Como faço para converter uma string em um número?
-------------------------------------------------

For integers, use the built-in "int()" type constructor, for example,
"int('144') == 144".  Similarly, "float()" converts to a floating-
point number, for example, "float('144') == 144.0".

Por padrão, eles interpretam o número como decimal, de modo que
"int('0144') == 144" é verdadeiro e "int('0x144')" levanta
"ValueError". "int(string, base)" toma a base para converter como um
segundo argumento opcional, então "int( '0x144', 16) == 324". Se a
base for especificada como 0, o número é interpretado usando as regras
do Python: um "0o" à esquerda indica octal e "0x" indica um número
hexadecimal.

Não use a função embutida "eval()" se tudo que você precisa é
converter strings em números. "eval()" será significativamente mais
lento e apresenta um risco de segurança: alguém pode passar a você uma
expressão Python que pode ter efeitos colaterais indesejados. Por
exemplo, alguém poderia passar "__import__('os').system("rm -rf
$HOME")" que apagaria seu diretório pessoal.

"eval()" also has the effect of interpreting numbers as Python
expressions, so that, for example, "eval('09')" gives a syntax error
because Python does not allow leading '0' in a decimal number (except
'0').


Como faço para converter um número em uma string?
-------------------------------------------------

For example, to convert the number "144" to the string "'144'", use
the built-in type constructor "str()".  If you want a hexadecimal or
octal representation, use the built-in functions "hex()" or "oct()".
For fancy formatting, see the Literais de strings formatadas and
Sintaxe das strings de formato sections. For example,
""{:04d}".format(144)" yields "'0144'" and ""{:.3f}".format(1.0/3.0)"
yields "'0.333'".


Como faço para modificar uma string internamente?
-------------------------------------------------

You can't, because strings are immutable.  In most situations, you
should simply construct a new string from the various parts you want
to assemble it from.  However, if you need an object with the ability
to modify in-place Unicode data, try using an "io.StringIO" object or
the "array" module:

   >>> import io
   >>> s = "Hello, world"
   >>> sio = io.StringIO(s)
   >>> sio.getvalue()
   'Hello, world'
   >>> sio.seek(7)
   7
   >>> sio.write("there!")
   6
   >>> sio.getvalue()
   'Hello, there!'

   >>> import array
   >>> a = array.array('w', s)
   >>> print(a)
   array('w', 'Hello, world')
   >>> a[0] = 'y'
   >>> print(a)
   array('w', 'yello, world')
   >>> a.tounicode()
   'yello, world'


Como faço para invocar funções/métodos através de strings?
----------------------------------------------------------

Existem várias técnicas.

* A melhor forma é usar um dicionário que mapeie strings para funções.
  A principal vantagem desta técnica é que estas strings não precisam
  corresponder aos nomes das funções. Esta é também a principal
  técnica utilizada para emular uma construção de instrução estilo
  *case*:

     def a():
         pass

     def b():
         pass

     dispatch = {'go': a, 'stop': b}  # Note a falta de parênteses para funções

     dispatch[get_input()]()  # Note os parênteses ao final para chamar a função

* Usar a função embutida "getattr()":

     import foo
     getattr(foo, 'bar')()

  Observe que a função "getattr()" funciona com qualquer objeto,
  incluindo classes, instâncias de classe, módulos e assim por diante.

  A mesma é usado em vários lugares na biblioteca padrão, como este:

     class Foo:
         def faz_foo(self):
             ...

         def faz_bar(self):
             ...

     f = getattr(instancia_foo, 'faz_' + opname)
     f()

* Use "locals()" para determinar o nome da função:

     def minhaFunc():
         print("hello")

     fname = "minhaFunc"

     f = locals()[fname]
     f()


Existe um equivalente em Perl "chomp()" para remover linhas novas ao final de strings?
--------------------------------------------------------------------------------------

Pode-se utilizar "S.rstrip("\r\n")" para remover todas as ocorrência
de qualquer terminador de linha que esteja no final da string "S" sem
remover os espaços em branco. Se a string "S" representar mais de uma
linha, contendo várias linhas vazias no final, os terminadores de
linha de todas linhas em branco serão removidos:

   >>> linhas = ("linha 1 \r\n"
   ...          "\r\n"
   ...          "\r\n")
   >>> linhas.rstrip("\n\r")
   'linha 1 '

Geralmente isso só é desejado ao ler um texto linha por linha, usando
"S.rstrip()" dessa maneira funciona bem.


Existe uma função "scanf()" ou "sscanf()" ou algo equivalente?
--------------------------------------------------------------

Não como tal.

Para a análise de entrada simples, a abordagem mais fácil geralmente é
dividir a linha em palavras delimitadas por espaços em branco usando o
método "split()" de objetos strings e, em seguida, converter as
strings decimais para valores numéricos usando a função "int()" ou a
função "float()". O método "split()" aceita um parâmetro "sep"
opcional que é útil se a linha utilizar algo diferente de espaço em
branco como separador.

Para análise de entradas de textos mais complicadas, as expressões
regulares são mais poderosas do que a "sscanf" do C e mais adequadas
para essa tarefa.


O que significa o erro "UnicodeDecodeError" ou "UnicodeEncodeError"?
--------------------------------------------------------------------

Consulte Unicode.


Posso terminar uma string bruta com um número ímpar de contrabarras?
--------------------------------------------------------------------

Uma string bruta terminando com um número ímpar de contrabarras vai
escapar as aspas da string:

   >>> r'C:\isso\não\vai\funcionar\'
     File "<stdin>", line 1
       r'C:\isso\não\vai\funcionar\'
       ^
   SyntaxError: unterminated string literal (detected at line 1)

Há várias soluções alternativas para isso. Uma delas é usar strings
regulares e duplicar as contrabarras:

   >>> 'C:\\isso\\vai\\funcionar\\'
   'C:\\isso\\vai\\funcionar\\'

Outra é concatenar uma string regular contendo uma contrabarra de
escape à string bruta:

   >>> r'C:\isso\vai\funcionar' '\\'
   'C:\\isso\\vai\\funcionar\\'

Também é possível usar "os.path.join()" para acrescentar uma
contrabarra no Windows:

   >>> os.path.join(r'C:\isso\vai\funcionar', '')
   'C:\\isso\\vai\\funcionar\\'

Note que, embora uma contrabarra vai "escapar" uma aspa para fins de
determinar onde a string bruta termina, nenhum escape ocorre ao
interpretar o valor da string bruta. Ou seja, a contrabarra permanece
presente no valor da string bruta:

   >>> r'contrabarra\'preservada'
   "contrabarra\\'preservada"

Veja também a especificação na referência da linguagem.


Desempenho
==========


Meu programa está muito lento. Como faço para melhorar o desempenho?
--------------------------------------------------------------------

That's a tough one, in general.  First, here is a list of things to
remember before diving further:

* As características da desempenho podem variar conforme a
  implementação do Python. Esse FAQ se concentra no *CPython*.

* O comportamento pode variar em cada sistemas operacionais,
  especialmente quando estivermos tratando de E/S ou multi-threading.

* Sempre devemos encontrar os hot spots em nosso programa *antes de*
  tentar otimizar qualquer código (veja o módulo "profile").

* Escrever scripts de benchmark permitirá iterar rapidamente buscando
  melhorias (veja o módulo "timeit").

* É altamente recomendável ter boa cobertura de código (através de
  testes de unidade ou qualquer outra técnica) antes de potencialmente
  apresentar regressões escondidas em otimizações sofisticadas.

Dito isto, existem muitos truques para acelerar nossos códigos Python.
Aqui estão alguns dos principais tópicos e que geralmente ajudam a
atingir níveis de desempenho aceitáveis:

* Fazer seus algoritmos rápidos (ou mudando para mais rápidos) podem
  produzir benefícios maiores que tentar encaixar várias micro-
  otimizações no seu código.

* Usar as estruturas de dados corretas. Estude a documentação para
  Tipos embutidos e o módulo "collections".

* Quando a biblioteca padrão fornecer um tipo primitivo para fazer
  algo, é provável (embora não garantido) que isso seja mais rápido do
  que qualquer alternativa que possa surgir. Isso geralmente é verdade
  para os tipos primitivos escritos em C, como os embutidos e alguns
  tipos de extensão. Por exemplo, certifique-se de usar o método
  embutido "list.sort()" ou a função relacionada "sorted()" para fazer
  a ordenação (e veja Técnicas de ordenação para exemplos de uso
  moderadamente avançado).

* As abstrações tendem a criar indireções e forçar o interpretador a
  trabalhar mais. Se os níveis de indireção superarem a quantidade de
  trabalho útil feito, seu programa ficará mais lento. Você deve
  evitar a abstração excessiva, especialmente sob a forma de pequenas
  funções ou métodos (que também são muitas vezes prejudiciais à
  legibilidade).

Se você atingiu o limite do que Python puro pode permitir, existem
ferramentas para levá-lo mais longe. Por exemplo, o Cython pode
compilar uma versão ligeiramente modificada do código Python numa
extensão C e pode ser usado em muitas plataformas diferentes. O Cython
pode tirar proveito da compilação (e anotações tipo opcional) para
tornar o seu código significativamente mais rápido do que quando
interpretado. Se você está confiante em suas habilidades de
programação C, também pode escrever um módulo de extensão de C.

Ver também: A página wiki dedicada a dicas de desempenho.


Qual é a maneira mais eficiente de concatenar muitas strings?
-------------------------------------------------------------

"str" and "bytes" objects are immutable, therefore concatenating many
strings together is inefficient as each concatenation creates a new
object.  In the general case, the total runtime cost is quadratic in
the total string length.  See Complexidade de tempo de operações em
tipos embutidos for more information.

Para juntar vários objetos "str", a linguagem recomendada colocá-los
numa lista e invocar o método "str.join()":

   chunks = []
   for s in my_strings:
       chunks.append(s)
   result = ''.join(chunks)

(Another reasonably efficient idiom is to use "io.StringIO".)

Para juntar vários objetos "bytes", a forma recomendada é estender uma
classe "bytearray" usando a concatenação local (com o operador "+="):

   result = bytearray()
   for b in my_bytes_objects:
       result += b


Sequences (tuples/lists)
========================


Como faço para converter tuplas em listas?
------------------------------------------

O construtor de tipo "tuple(seq)" converte qualquer sequência (na
verdade, qualquer iterável) numa tupla com os mesmos itens na mesma
ordem.

Por exemplo, "tuple([1, 2, 3])" produz "(1, 2, 3)" e "tuple('abc')"
produz "('a', 'b', 'c')". Se o argumento for uma tupla, a mesma não
faz uma cópia, mas retorna o mesmo objeto, por isso é barato invocar a
função "tuple()" quando você não tiver certeza que determinado objeto
já é uma tupla.

O construtor de tipos "list(seq)" converte qualquer sequência ou
iterável em uma lista com os mesmos itens na mesma ordem. Por exemplo,
"list((1, 2, 3))" produz "[1, 2, 3]" e "list('abc')" produz "['a',
'b', 'c']". Se o argumento for uma lista, o meso fará uma cópia como
em "seq[:]".


O que é um índice negativo?
---------------------------

Sequências em Python são indexadas com números positivos e números
negativos. Para números positivos, 0 é o índice do primeiro elemento,
1 é o índice do segundo elemento e assim por diante. Para números
negativos, -1 é índice do último elemento e -2 é o penúltimo (anterior
ao último) índice e assim por diante. Pense em "seq[-n]" como o mesmo
que "seq[len(seq)-n]".

Usar índices negativos pode ser muito conveniente. Por exemplo,
"S[:-1]" é a string inteira exceto pelo seu último caractere, o que é
útil para remover o caractere de nova linha no final de uma string.


Como que eu itero uma sequência na ordem inversa?
-------------------------------------------------

Use a função embutida "reversed()":

   for x in reversed(sequence):
       ...  # faz alguma coisa com x ...

Isso não vai alterar sua sequência original, mas construir uma nova
cópia com a ordem inversa para iteração.


Como que removo itens duplicados de uma lista?
----------------------------------------------

Veja o Python Cookbook para uma longa discussão de várias formas de
fazer isso:

   https://code.activestate.com/recipes/52560/

Se você não se importar em reordenar a lista, ordene-a e depois
examine a partir do final da lista, excluindo duplicatas conforme
avança:

   if mylist:
       mylist.sort()
       last = mylist[-1]
       for i in range(len(mylist)-2, -1, -1):
           if last == mylist[i]:
               del mylist[i]
           else:
               last = mylist[i]

If all elements of the list may be used as set keys (that is, they are
all *hashable*) this is often faster:

   mylist = list(set(mylist))

Isso converte a lista em um conjunto, deste modo removendo itens
duplicados, e depois de volta em uma lista.


How do you remove multiple items from a list?
---------------------------------------------

As with removing duplicates, explicitly iterating in reverse with a
delete condition is one possibility.  However, it is easier and faster
to use slice replacement with an implicit or explicit forward
iteration. Here are three variations:

   mylist[:] = filter(keep_function, mylist)
   mylist[:] = (x for x in mylist if keep_condition)
   mylist[:] = [x for x in mylist if keep_condition]

A compreensão de lista pode ser a mais rápida.


Como fazer um vetor em Python?
------------------------------

Utilize uma lista:

   ["isto", 1, "é", "um", "vetor"]

Listas são equivalentes aos vetores de C ou Pascal em termos de
complexidade de tempo; a diferença primária é que uma lista em Python
pode conter objetos de tipos diferentes.

The "array" module also provides methods for creating arrays of fixed
types with compact representations, but they are slower to index than
lists.  Also note that NumPy and other third-party packages define
array-like structures with various characteristics as well.

Para obter listas ligadas no estilo Lisp, você pode emular *células
cons* usando tuplas:

   lista_lisp = ("como",  ("este",  ("exemplo", None) ) )

Se mutabilidade é desejada, você pode usar listas no lugar de tuplas.
Aqui o análogo de um *car* Lisp é  "lista_lisp[0]" e o análogo de
*cdr* é "lista_lisp[1]".  Faça isso somente se você tem certeza que
precisa disso, porque isso é usualmente muito mais lento que usar
listas Python.


Como faço para criar uma lista multidimensional?
------------------------------------------------

Você provavelmente tentou fazer um vetor multidimensional assim:

   >>> A = [[None] * 2] * 3

Isso parece correto se você imprimir:

   >>> A
   [[None, None], [None, None], [None, None]]

Mas quando atribuíres um valor, o mesmo aparecerá em vários lugares:

   >>> A[0][0] = 5
   >>> A
   [[5, None], [5, None], [5, None]]

A razão é que replicar uma lista com "*" não cria cópias, ela apenas
cria referências aos objetos existentes. O "*3" cria uma lista
contendo 3 referências para a mesma lista que contém 2 itens cada.
Mudanças numa linha serão mostradas em todas as linhas, o que
certamente não é o que você deseja.

A abordagem sugerida é criar uma lista com o comprimento desejado
primeiro e, em seguida, preencher cada elemento com uma lista recém-
criada:

   A = [None] * 3
   for i in range(3):
       A[i] = [None] * 2

Isso gera uma lista contendo 3 listas diferentes contendo 2 itens
cada. Você também pode usar uma compreensão de lista:

   w, h = 2, 3
   A = [[None] * w for i in range(h)]

Ou você pode usar uma extensão que provê um tipo de dados matrix;
NumPy é o mais conhecido.


Como eu aplico um método ou função para uma sequência de objetos?
-----------------------------------------------------------------

To call a method or function and accumulate the return values in a
list, a *list comprehension* is an elegant solution:

   result = [obj.method() for obj in mylist]

   result = [function(obj) for obj in mylist]

Para apenas chamar o método ou função sem salvar os valores
retornados, um laço "for" será o suficiente:

   for obj in mylist:
       obj.method()

   for obj in mylist:
       function(obj)


Porque uma_tupla[i] += ['item'] levanta uma exceção quando a adição funciona?
-----------------------------------------------------------------------------

Isso se deve a uma combinação do fato de que os operadores de
atribuição aumentada são operadores de *atribuição* e à diferença
entre objetos mutáveis e imutáveis no Python.

Essa discussão se aplica em geral quando operadores de atribuição
aumentada são aplicados a elementos de uma tupla que aponta para
objetos mutáveis, mas usaremos uma "lista"  e "+=" como exemplo.

Se você escrever:

   >>> a_tuple = (1, 2)
   >>> a_tuple[0] += 1
   Traceback (most recent call last):
      ...
   TypeError: 'tuple' object does not support item assignment

O motivo da exceção deve ser imediatamente claro: "1" é adicionado ao
objeto que "a_tuple[0]" aponta para ("1"), produzindo o objeto de
resultado, "2", mas quando tentamos atribuir o resultado do cálculo,
"2", ao elemento "0" da tupla, recebemos um erro porque não podemos
alterar o que um elemento de uma tupla aponta.

Por baixo, o que a instrução de atribuição aumentada está fazendo é
aproximadamente isso:

   >>> result = a_tuple[0] + 1
   >>> a_tuple[0] = result
   Traceback (most recent call last):
     ...
   TypeError: 'tuple' object does not support item assignment

Essa é a parte da atribuição da operação que produz o erro, já que a
tupla é imutável.

Quando você escreve algo como:

   >>> a_tuple = (['foo'], 'bar')
   >>> a_tuple[0] += ['item']
   Traceback (most recent call last):
     ...
   TypeError: 'tuple' object does not support item assignment

A exceção é um pouco mais surpreendente, e ainda mais surpreendente é
o fato de que, embora tenha havido um erro, o acréscimo à lista
funcionou:

   >>> a_tuple[0]
   ['foo', 'item']

Para entender por que isso acontece, você precisa saber que (a) se um
objeto implementa um método mágico "__iadd__()", ele é chamado quando
a atribuição aumentada "+=" é executada, e seu valor de retorno é o
que é usado na instrução de atribuição; e (b) para listas,
"__iadd__()" é equivalente a chamar "extend()" na lista e retornar a
lista. É por isso que dizemos que, para listas, "+=" é uma
“abreviação” para "list.extend()":

   >>> a_list = []
   >>> a_list += [1]
   >>> a_list
   [1]

Isso equivale a:

   >>> result = a_list.__iadd__([1])
   >>> a_list = result

O objeto apontado por a_list foi alterado e o ponteiro para o objeto
alterado é atribuído novamente a "a_list". O resultado final da
atribuição é um no-op, pois é um ponteiro para o mesmo objeto para o
qual "a_list" estava apontando anteriormente, mas a atribuição ainda
acontece.

Portanto, em nosso exemplo da tupla, o que está acontecendo é
equivalente a:

   >>> result = a_tuple[0].__iadd__(['item'])
   >>> a_tuple[0] = result
   Traceback (most recent call last):
     ...
   TypeError: 'tuple' object does not support item assignment

O "__iadd__()" é bem-sucedido e, portanto, a lista é estendida, mas
mesmo que "result" aponte para o mesmo objeto para o qual "a_tuple[0]"
já aponta, essa atribuição final ainda resulta em um erro, pois as
tuplas são imutáveis.


Quero fazer uma ordenação confusa: você pode fazer uma transformação schwartziana em Python?
--------------------------------------------------------------------------------------------

A técnica, atribuída a Randal Schwartz da comunidade Perl, ordena os
elementos de uma lista por uma métrica que mapeia cada elemento para
seu “valor de ordem”. Em Python, use o argumento "key" para o método
"list.sort()":

   Isorted = L[:]
   Isorted.sort(key=lambda s: int(s[10:15]))


Como eu posso ordenar uma lista pelos valores de outra lista?
-------------------------------------------------------------

Merge them into an iterator of tuples, sort the resulting list, and
then pick out the element you want.

>>> list1 = ["what", "I'm", "sorting", "by"]
>>> list2 = ["something", "else", "to", "sort"]
>>> pairs = zip(list1, list2)
>>> pairs = sorted(pairs)
>>> pairs
[("I'm", 'else'), ('by', 'sort'), ('sorting', 'to'), ('what', 'something')]
>>> result = [x[1] for x in pairs]
>>> result
['else', 'sort', 'to', 'something']


Objetos
=======


O que é uma classe?
-------------------

Uma classe é o tipo de objeto específico criado pela execução da
instrução class. Os objetos classe são usados como modelos para criar
objetos instância, que incorporam os dados (atributos) e o código
(métodos) específicos de um tipo de dado.

Uma classe pode ser baseada em uma ou mais outras classes, chamadas de
classe(s) base(s), herdando seus atributos e métodos. Isso permite que
um modelo de objeto seja sucessivamente refinado por herança.  Você
pode ter uma classe genérica "Mailbox" que fornece métodos básicos
para uma caixa de correio e subclasses como "MboxMailbox",
"MaildirMailbox", "OutlookMailbox" que manipula vários formatos
específicos de caixa de correio.


O que é um método?
------------------

Um método é uma função em algum objeto "x" que você normalmente chama
com "x.name(arguments...)". Métodos são definidos como funções dentro
da definição da classe:

   class C:
       def meth(self, arg):
           return arg * 2 + self.attribute


O que é o self?
---------------

Self é apenas um nome convencional para o primeiro argumento de um
método. Um método definido como "meth(self, a, b, c)" deve ser chamado
com "x.meth(a, b, c)" para alguma instância "x" da classe em que a
definição ocorre; o método chamado pensará que é chamado com "meth(x,
a, b, c)".

Veja também Por que o 'self' deve ser usado explicitamente em
definições de método e chamadas?.


Como eu verifico se um objeto é uma instância de uma dada classe ou de uma subclasse dela?
------------------------------------------------------------------------------------------

Use the built-in function "isinstance(obj, cls)".  You can check if an
object is an instance of any of a number of classes by providing a
tuple instead of a single class, for example, "isinstance(obj,
(class1, class2, ...))", and can also check whether an object is one
of Python's built-in types, for example, "isinstance(obj, str)" or
"isinstance(obj, (int, float, complex))".

Note that "isinstance()" also checks for virtual inheritance from an
*abstract base class*.  So, the test will return "True" for a
registered class even if hasn't directly or indirectly inherited from
it.  To test for "true inheritance", scan the *method resolution
order* (MRO) of the class:

   from collections.abc import Mapping

   class P:
        pass

   class C(P):
       pass

   Mapping.register(P)

   >>> c = C()
   >>> isinstance(c, C)        # direta
   True
   >>> isinstance(c, P)        # indireta
   True
   >>> isinstance(c, Mapping)  # virtual
   True

   # Cadeira de herança real
   >>> type(c).__mro__
   (<class 'C'>, <class 'P'>, <class 'object'>)

   # Teste pela "herança verdadeira"
   >>> Mapping in type(c).__mro__
   False

Observe que a maioria dos programas não usa "isinstance()" em classes
definidas pelo usuário com muita frequência. Se você estiver
desenvolvendo as classes por conta própria, um estilo orientado a
objetos mais adequado é definir métodos nas classes que encapsulam um
comportamento específico, em vez de verificar a classe do objeto e
fazer uma coisa diferente com base na classe que ele é. Por exemplo,
se você tiver uma função que faz algo:

   def search(obj):
       if isinstance(obj, Mailbox):
           ...  # código para pesquisar uma caixa de correio
       elif isinstance(obj, documento):
           ...  # código para pesquisar um documento
       elif ...

Uma abordagem melhor é definir um método "search()" em todas as
classes e apenas chamá-lo:

   class Mailbox:
       def search(self):
           ...  # código para pesquisar uma caixa de correio

   class documento:
       def search(self):
           ...  # código para pesquisar um documento

   obj.search()


O que é delegação?
------------------

Delegation is an object-oriented technique (also called a design
pattern). Let's say you have an object "x" and want to change the
behaviour of just one of its methods.  You can create a new class that
provides a new implementation of the method you're interested in
changing and delegates all other methods to the corresponding method
of "x".

Com Python, você pode implementar delegação facilmente. Por exemplo, o
trecho de código a seguir implementa uma classe que se comporta como
um arquivo, mas converte todos os dados gravados em letras maiúsculas:

   class UpperOut:

       def __init__(self, outfile):
           self._outfile = outfile

       def write(self, s):
           self._outfile.write(s.upper())

       def __getattr__(self, name):
           return getattr(self._outfile, name)

Aqui, a classe "UpperOut" redefine o método "write()" para converter o
argumento string em maiúsculas antes de chamar o método
"self._outfile.write()" subjacente.  Todos os outros métodos são
delegados ao objeto "self._outfile" subjacente.  A delegação é
realizada por meio do método "__getattr__()"; consulte a referência da
linguagem para obter mais informações sobre o controle de acesso a
atributo.

Observe que, em casos mais gerais, a delegação pode se tornar mais
complicada. Quando o atributo precisa ser definido e recuperado, a
classe deve definir um método "__setattr__()"  também, e deve fazê-lo
com cuidado.  A implementação básica do "__setattr__()" é
aproximadamente equivalente ao seguinte:

   class X:
       ...
       def __setattr__(self, name, value):
           self.__dict__[name] = value
       ...

Muitas implementações do método "__setattr__()" chamam o
"object.__setattr__()" para definir um atributo em si mesmo sem causar
recursão infinita:

   class X:
       def __setattr__(self, name, value):
           # Lógica personalizada aqui...
           object.__setattr__(self, name, value)

Como alternativa, é possível definir atributos inserindo entradas em
"self.__dict__" diretamente.


Como eu chamo um método definido em uma classe base a partir de uma classe derivada que a estende?
--------------------------------------------------------------------------------------------------

Use a função embutida "super()":

   class Derived(Base):
       def meth(self):
           super().meth()  # chama Base.meth

No exemplo, "super()" determinará automaticamente a instância da qual
foi chamado (o valor de "self"), procura a *ordem de resolução de
métodos* (MRO) com "type(self).__mro__" e então retorna o próximo na
linha após "Derived" no MRO: "Base".


Como eu posso organizar meu código para facilitar a troca da classe base?
-------------------------------------------------------------------------

You could assign the base class to an alias and derive from the alias.
Then all you have to change is the value assigned to the alias.
Incidentally, this trick is also handy if you want to decide
dynamically (such as depending on availability of resources) which
base class to use.  Example:

   class Base:
       ...

   BaseAlias = Base

   class Derived(BaseAlias):
       ...


Como faço para criar dados de classe estáticos e métodos de classe estáticos?
-----------------------------------------------------------------------------

Tanto dados estáticos quanto métodos estáticos (no sentido de C++ ou
Java) são possíveis com Python.

Para dados estáticos, basta definir um atributo de classe. Para
atribuir um novo valor ao atributo, você precisa usar explicitamente o
nome da classe na atribuição:

   class C:
       count = 0 # número de vezes que C.__init__ foi chamado

       def __init__(self):
           C.count = C.count + 1

       def getcount(self):
           return C.count # ou return self.count

"c.count" também se refere a "C.count" para qualquer "c" de modo que
"isinstance(c, C)" seja válido, a menos que seja substituído pelo
próprio "c" ou por alguma classe no caminho de busca da classe base de
"c.__class__" até "C".

Cuidado: em um método de C, uma atribuição como "self.count = 42" cria
uma instância nova e não-relacionada chamada "count" no próprio
dicionário de "self".  A revinculação de um nome de dado de classe
estático deve sempre especificar a classe, seja dentro de um método ou
não:

   C.count = 314

Métodos estáticos são possíveis:

   class C:
       @staticmethod
       def static(arg1, arg2, arg3):
           # Sem parâmetro 'self'!
           ...

No entanto, uma maneira muito mais direta de obter o efeito de um
método estático é por meio de uma simples função em nível de módulo:

   def getcount():
       return C.count

Se o seu código está estruturado de modo a definir uma classe (ou uma
hierarquia de classes estreitamente relacionada) por módulo, isso
fornecerá o encapsulamento desejado.


Como eu posso sobrecarregar construtores (ou métodos) em Python?
----------------------------------------------------------------

Essa resposta na verdade se aplica para todos os métodos, mas a
pergunta normalmente aparece primeiro no contexto de construtores.

In C++ you'd write:

   class C {
       C() { cout << "Sem argumentos\n"; }
       C(int i) { cout << "Argumento é igual a " << i << "\n"; }
   }

Em Python, você tem que escrever um único construtor que pega todos os
casos usando argumentos padrão. Por exemplo:

   class C:
       def __init__(self, i=None):
           if i is None:
               print("Sem argumentos")
           else:
               print("Argumento é igual a", i)

Isso não é inteiramente equivalente, mas já está bem próximo.

You could also try a variable-length argument list, for example:

   def __init__(self, *args):
       ...

A mesma abordagem funciona para todas as definições de métodos.


Eu tentei usar __spam e recebi um erro sobre _SomeClassName__spam.
------------------------------------------------------------------

Os nomes de variáveis com dois sublinhados à esquerda são
"manipulados" para fornecer uma maneira simples, mas eficaz, de
definir variáveis privadas de classe.  Qualquer identificador no
formato "__spam" (pelo menos dois sublinhados à esquerda, no máximo um
sublinhado à direita) é textualmente substituído por
"_classname__spam", em que "classname" é o nome da classe atual sem
nenhum sublinhado à esquerda.

O identificador pode ser usado normalmente dentro da classe, mas para
acessá-lo fora da classe, deve ser usado o nome manipulado:

   class A:
       def __one(self):
           return 1
       def two(self):
           return 2 * self.__one()

   class B(A):
       def three(self):
           return 3 * self._A__one()

   four = 4 * A()._A__one()

Em particular, isso não garante a privacidade, pois um usuário externo
ainda pode acessar deliberadamente o atributo privado; muitas pessoas
que usam Python nunca se preocuparam em usar nomes de variáveis
privadas.

Ver também:

  As especificações de desfiguração de nome privado para detalhes e
  casos especiais.


Minha classe define __del__, mas o mesmo não é chamado quando eu excluo o objeto.
---------------------------------------------------------------------------------

Há várias razões possíveis para isto.

A instrução "del" não necessariamente chama o método "__del__()" - ele
simplesmente diminui o contagem de referências do objeto e, se ele
chegar a zero, o "__del__()" é chamado.

If your data structures contain circular links (for example, a tree
where each child has a parent reference and each parent has a list of
children) the reference counts will never go back to zero.  Once in a
while Python runs an algorithm to detect such cycles, but the garbage
collector might run some time after the last reference to your data
structure vanishes, so your "__del__()" method may be called at an
inconvenient and random time. This is inconvenient if you're trying to
reproduce a problem. Worse, the order in which object's "__del__()"
methods are executed is arbitrary.  You can run "gc.collect()" to
force a collection, but there *are* pathological cases where objects
will never be collected.

Apesar do coletor de ciclos, ainda é uma boa ideia definir um método
"close()" explícito nos objetos a ser chamado sempre que você terminar
de usá-los.  O método "close()" pode então remover o atributo que se
refere a subobjetos.  Não chame "__del__()" diretamente - "__del__()"
deve chamar "close()" e "close()" deve garantir que ele possa ser
chamado mais de uma vez para o mesmo objeto.

Outra forma de evitar referências cíclicas é usar o módulo "weakref",
que permite apontar para objetos sem incrementar o contagem de
referências. As estruturas de dados em árvore, por exemplo, devem usar
o referência fraca para referenciar seus pais e irmãos (se precisarem
deles!).

Por fim, se seu método "__del__()" levanta uma exceção, uma mensagem
de alerta será enviada para "sys.stderr".


Como eu consigo pegar uma lista de todas as instâncias de uma dada classe?
--------------------------------------------------------------------------

Python não mantém o controle de todas as instâncias de uma classe (ou
de um tipo embutido). Você pode programar o construtor da classe para
manter o controle de todas as instâncias, mantendo uma lista de
referências fracas para cada instância.


Por que o resultado de "id()" aparenta não ser único?
-----------------------------------------------------

A função embutida "id()" retorna um inteiro que é garantido ser único
durante a vida útil do objeto.  Como em CPython esse número é o
endereço de memória do objeto, acontece com frequência que, depois que
um objeto é excluído da memória, o próximo objeto recém-criado é
alocado na mesma posição na memória.  Isso é ilustrado por este
exemplo:

>>> id(1000)
13901272
>>> id(2000)
13901272

Os dois ids pertencem a diferentes objetos inteiros que são criados
antes e excluídos imediatamente após a execução da chamada de "id()".
Para ter certeza de que os objetos cujo id você deseja examinar ainda
estão vivos, crie outra referencia para o objeto:

>>> a = 1000; b = 2000
>>> id(a)
13901272
>>> id(b)
13891296


Quando eu posso depender dos testes de identidade com o operador *is*?
----------------------------------------------------------------------

O operador "is" testa a identidade do objeto. O teste "a is b"
equivale a "id(a) == id(b)".

A propriedade mais importante de um teste de identidade é que um
objeto é sempre idêntico a si mesmo, "a is a" sempre retorna "True".
Testes de identidade são geralmente mais rápidos do que os testes de
igualdade. E, ao contrário dos testes de igualdade, teste de
identidade garante que retorno seja um booleano "True" ou "False".

Entretanto, o teste de identidade *somente* pode ser substituído por
testes de igualdade quando a identidade do objeto é garantida. Em
geral, há três circunstâncias em que a identidade é garantida:

1. Atribuições criam novos nomes, mas não alteram a identidade do
   objeto. Após a atribuição "new = old", é garantido que "new is
   old".

2. Colocar um objeto em um contêiner que armazena referências de
   objetos não altera a identidade do objeto. Após a lista atribuição
   "s[0] = x", é garantido que "s[0] is x".

3. Se um objeto for um Singleton, isso significa que só pode existir
   uma instância desse objeto. Depois de atribuição "a = None" e "b =
   None", é garantido que "a is b" porque "None" é um Singleton.

Na maioria das outras circunstâncias, o teste de identidade é
desaconselhável e os testes de igualdade são preferíveis. Em
particular, teste de identidade não deve ser usado para verificar
constantes, como "int" e "str", que não têm garantia de serem
Singletons:

   >>> a = 10_000_000
   >>> b = 5_000_000
   >>> c = b + 5_000_000
   >>> a is c
   False

   >>> a = 'Python'
   >>> b = 'Py'
   >>> c = b + 'thon'
   >>> a is c
   False

Do mesmo jeito, novas instâncias de contêineres mutáveis nunca são
idênticas:

   >>> a = []
   >>> b = []
   >>> a is b
   False

No código da biblioteca padrão, você encontrará vários padrões comuns
para usar corretamente o teste de identidade:

1. Conforme recomendado por **PEP 8**, um teste de identidade é a
   maneira preferida de verificar "None".  Isso é lido como se fosse
   inglês simples no código e evita confusão com outros objetos que
   podem ter valor booleano avaliado para falso.

2. A detecção de argumento opcional pode ser complicada quando "None"
   é uma valor de entrada válido.  Nessas situações, você pode criar
   um objeto Singleton sinalizador com garantia de ser distinto de
   outros objetos. Por exemplo, veja como implementar um método que se
   comporta como "dict.pop()":

      _sentinel = sentinel('_sentinel')

      def pop(self, key, default=_sentinel):
          if key in self:
              value = self[key]
              del self[key]
              return value
          if default is _sentinel:
              raise KeyError(key)
          return default

3. Implementações de contêiner às vezes precisam combinar testes de
   igualdade com testes de identidade. Isso evita que o código seja
   confundido por objetos como "float('NaN')" que não são iguais a si
   mesmos.

Por exemplo, aqui está a implementação de
"collections.abc.Sequence.__contains__()":

   def __contains__(self, value):
       for v in self:
           if v is value or v == value:
               return True
       return False


Como uma subclasse pode controlar quais dados são armazenados em uma instância imutável?
----------------------------------------------------------------------------------------

Quando estender um tipo imutável, sobrescreva o método "__new__()" em
vez do método "__init__()".  O último só é executado *depois* que uma
instância é criada, o que é tarde demais para alterar os dados em uma
instância imutável.

Todas essas classes imutáveis têm um assinatura diferente da sua
classe base:

   import datetime as dt

   class FirstOfMonthDate(dt.date):
       "Always choose the first day of the month"
       def __new__(cls, year, month, day):
           return super().__new__(cls, year, month, 1)

   class NamedInt(int):
       "Allow text names for some numbers"
       xlat = {'zero': 0, 'one': 1, 'ten': 10}
       def __new__(cls, value):
           value = cls.xlat.get(value, value)
           return super().__new__(cls, value)

   class TitleStr(str):
       "Convert str to name suitable for a URL path"
       def __new__(cls, s):
           s = s.lower().replace(' ', '-')
           s = ''.join([c for c in s if c.isalnum() or c == '-'])
           return super().__new__(cls, s)

As classes podem ser usadas da seguinte forma:

   >>> FirstOfMonthDate(2012, 2, 14)
   FirstOfMonthDate(2012, 2, 1)
   >>> NamedInt('ten')
   10
   >>> NamedInt(20)
   20
   >>> TitleStr('Blog: Porque Python domina')
   'blog-porque-python-domina'


Como faço para armazenar em cache as chamadas de um método?
-----------------------------------------------------------

The two principal tools for caching methods are
"@functools.cached_property" and "@functools.lru_cache".  The former
stores results at the instance level and the latter at the class
level.

The "cached_property" approach only works with methods that do not
take any arguments.  It does not create a reference to the instance.
The cached method result will be kept only as long as the instance is
alive.

A vantagem é que, quando um instância não for mais usada, o resultado
do método armazenado em cache será liberado imediatamente.  A
desvantagem é que, se as instâncias se acumularem, os resultados do
método também serão acumulados. Eles podem crescer sem limites.

The "lru_cache" approach works with methods that have *hashable*
arguments.  It creates a reference to the instance unless special
efforts are made to pass in weak references.

A vantagem do algoritmo menos recentemente usado é que o cache é
limitado pelo *maxsize* especificado.  A desvantagem é que as
instâncias são mantidas vivas até que saiam do cache ou até que o
cache seja limpo.

Esse exemplo mostra as várias técnicas:

   class Weather:
       "Procura informações de tempo em sites governamentais"

       def __init__(self, station_id):
           self._station_id = station_id
           # O _station_id é privado e imutável

       def current_temperature(self):
           "Última observação horária"
           # Não armazena isso em cache porque os dados anteriores
           # podem estar desatualizados.

       @cached_property
       def location(self):
           "Retornas as coordenadas longitude/latitude coordinates da estação"
           # Resultado depende apenas de station_id

       @lru_cache(maxsize=20)
       def historic_rainfall(self, date, units='mm'):
           "Precipitação em uma determinada data"
           # Depende de station_id, date, e units.

The above example assumes that the *station_id* never changes.  If the
relevant instance attributes are mutable, the "cached_property"
approach can't be made to work because it cannot detect changes to the
attributes.

To make the "lru_cache" approach work when the *station_id* is
mutable, the class needs to define the "__eq__()" and "__hash__()"
methods so that the cache can detect relevant attribute updates:

   class Weather:
       "Exemplo com um identificador de estação mutável"

       def __init__(self, station_id):
           self.station_id = station_id

       def change_station(self, station_id):
           self.station_id = station_id

       def __eq__(self, other):
           return self.station_id == other.station_id

       def __hash__(self):
           return hash(self.station_id)

       @lru_cache(maxsize=20)
       def historic_rainfall(self, date, units='cm'):
           "Precipitação em uma determinada data"
           # Depende de station_id, date, e units.


Módulos
=======


Como faço para criar um arquivo .pyc?
-------------------------------------

Quando um módulo é importado pela primeira vez (ou quando o arquivo de
origem foi alterado desde que o arquivo compilado atual foi criado),
um arquivo ".pyc" contendo o código compilado deve ser criado em um
subdiretório "__pycache__" do diretório que contém o arquivo ".py".  O
arquivo ".pyc" terá um nome de arquivo que começa com o mesmo nome do
arquivo ".py" e termina com ".pyc", com um componente intermediário
que depende do binário "python" específico que o criou.  (Consulte
**PEP 3147** para obter detalhes.)

Um dos motivos pelos quais um arquivo ".pyc" pode não ser criado é um
problema de permissões no diretório que contém o arquivo de origem, o
que significa que o subdiretório "__pycache__" não pode ser criado.
Isso pode acontecer, por exemplo, se você desenvolver como um usuário,
mas executar como outro, como se estivesse testando em um servidor
web.

Unless the "PYTHONDONTWRITEBYTECODE" environment variable is set,
creation of a .pyc file is automatic if you're importing a module and
Python has the ability (permissions, free space, and so on) to create
a "__pycache__" subdirectory and write the compiled module to that
subdirectory.

Running Python on a top-level script is not considered an import and
no ".pyc" will be created.  For example, if you have a top-level
module "foo.py" that imports another module "xyz.py", when you run
"foo" (by typing "python foo.py" as a shell command), a ".pyc" will be
created for "xyz" because "xyz" is imported, but no ".pyc" file will
be created for "foo" since "foo.py" isn't being imported.

Se você precisar criar um arquivo ".pyc" para "foo", ou seja, criar um
arquivo ".pyc" para um módulo que não é importado, você pode usar os
módulos "py_compile" e "compileall".

O módulo "py_compile" pode compilar manualmente qualquer módulo.  Uma
maneira é usar interativamente a função "compile()" nesse módulo:

   >>> import py_compile
   >>> py_compile.compile('foo.py')

This will write the ".pyc" to a "__pycache__" subdirectory in the same
location as "foo.py" (or you can override that with the optional
parameter *cfile*).

Você também pode compilar automaticamente todos os arquivos em um
diretório ou diretórios usando o módulo "compileall".  Você pode fazer
isso no console do SO executando "compileall.py" e fornecendo o
caminho de um diretório que contenha os arquivos Python a serem
compilados:

   python -m compileall .


Como encontro o nome do módulo atual?
-------------------------------------

Um módulo pode descobrir seu próprio nome consultando a variável
global predefinida "__name__" .  Se ela tiver o valor "'__main__'" , o
programa estará sendo executado como um script.  Muitos módulos que
são normalmente usados ao serem importados também fornecem uma
interface de linha de comando ou um autoteste, e só executam esse
código depois de verificar "__name__":

   def main():
       print('Executando teste...')
       ...

   if __name__ == '__main__':
       main()


Como posso ter módulos que se importam mutuamente?
--------------------------------------------------

Suponha que tenhas os seguintes módulos:

"foo.py":

   from bar importar bar_var
   foo_var = 1

"bar.py":

   from foo import foo_var
   bar_var = 2

O problema é que o interpretador vai realizar os seguintes passos:

* Programa principal importa "foo"

* São criados globais vazios para "foo"

* "foo" é compilado e começa a ser executado

* "foo" importa "bar"

* São criados globais vazios para "bar"

* "bar" é compilado e começa a ser executado

* "bar" importa "foo" (o que não é executado de fato, pois já existe
  um módulo chamado "foo")

* O mecanismo de importação tenta ler "foo_var" do "foo" em globais,
  para definir "bar.foo_var = foo.foo_var"

A última etapa falha, pois Python ainda não terminou de interpretar
"foo" e o dicionário de símbolos global para "foo" ainda está vazio.

O mesmo acontece quando você usa "import foo" e, em seguida, tenta
acessar "foo.foo_var" no código global.

Há (pelo menos) três possíveis soluções alternativas para esse
problema.

Guido van Rossum recomenda evitar todos os usos de "from <module>
import ..." e colocar todo o código dentro de funções.  As
inicializações de variáveis globais e variáveis de classe devem usar
apenas constantes ou funções embutidas.  Isso significa que tudo de um
módulo importado é referenciado como "<module>.<name>".

Jim Roskind sugere a execução das etapas na seguinte ordem em cada
módulo:

* exportações (globais, função e classes que não precisam de classes
  base importadas)

* instruções "import"

* código ativo (incluindo globais que são inicializadas de valores
  importados)

Van Rossum não gosta muito dessa abordagem porque a importação aparece
em um lugar estranho, mas ela funciona.

Matthias Urlichs recomenda reestruturar seu código para que importação
recursiva não seja necessária em primeiro lugar.

Essas soluções não são mutuamente exclusivas.


__import__('x.y.z') retorna <módulo 'x'>; como faço para obter z?
-----------------------------------------------------------------

Em vez disso, considere usar a conveniente função "import_module()" de
"importlib":

   z = importlib.import_module('x.y.z')


Quando eu edito um módulo importado e o reimporto, as mudanças não aparecem. Por que isso acontece?
---------------------------------------------------------------------------------------------------

Por motivos de eficiência e consistência, o Python só lê o arquivo do
módulo na primeira vez em que um módulo é importado.  Caso contrário,
em um programa que consiste em muitos módulos em que cada um importa o
mesmo módulo básico, o módulo básico seria analisado e reanalisado
várias vezes.  Para forçar a releitura de um módulo alterado, faça o
seguinte:

   import importlib
   import modname
   importlib.reload(modname)

Warning: this technique is not 100% fool-proof.  In particular,
modules containing statements like:

   from modname import some_objects

continuará com a versão antiga dos objetos importados.  Se o módulo
contiver definições de classe, as instâncias de classe existentes
*não* serão atualizadas para usar a nova definição da classe.  Isso
pode resultar no seguinte comportamento paradoxal:

   >>> import importlib
   >>> import cls
   >>> c = cls.C()                # Cria uma instância de C
   >>> importlib.reload(cls)
   <module 'cls' from 'cls.py'>
   >>> isinstance(c, cls.C)       # isinstance é falso?!?
   False

A natureza do problema fica clara se você exibir a "identidade" dos
objetos da classe:

   >>> hex(id(c.__class__))
   '0x7352a0'
   >>> hex(id(cls.C))
   '0x4198d0'
