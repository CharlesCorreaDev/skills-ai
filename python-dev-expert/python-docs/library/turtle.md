"turtle" --- Gráficos tartaruga
*******************************

**Código-fonte:** Lib/turtle.py

======================================================================


Turtle star
^^^^^^^^^^^

A tartaruga pode desenhar formas intrincadas usando programas que
repetem movimentos simples.

[imagem: Uma estrela amarela de pontas finas com contorno vermelho,
desenhada por turtle.][imagem]

Imagine uma tartaruga robótica começando em (0, 0) no plano x-y.
Depois de um "import turtle", execute o comando "turtle.forward(15)",
e ela moverá (na tela!) 15 pixels na direção em que está virada (para
frente), desenhando uma linha à medida que se move. Execute o comando
"turtle.right(25)", e ela fará uma rotação, de 25 graus no sentido
horário, sem sair do lugar.

Os gráficos tartaruga são uma implementação das ferramentas de desenho
introduzidas na linguagem Logo em 1967. A ferramenta foi criada para
fins educacionais, e seu feedback visual imediato a torna um meio
eficaz para os alunos entrarem em contato com conceitos de
programação. É também uma maneira prática de gerar saídas gráficas
simples sem a necessidade de bibliotecas externas.

Esse documento inclui quatro seções principais:

* Tutorial ensina os básicos do desenho tartaruga.

* Referência descreve as funções, métodos e classes que este módulo
  define.

* Guias de como fazer detalha como lidar com tarefas específicas.

* Explicação fornece informações básicas sobre a interface orientada a
  objetos.

Nota:

  Os gráficos tartaruga requerem o *módulo opcional* "tkinter". Os
  instaladores do python.org para Windows e macOS o incluem, mas
  algumas distribuições Linux e outras plataformas podem empacotá-lo
  separadamente. Se "import turtle" falhar com um erro mencionando
  "_tkinter", consulte a documentação da sua distribuidora (ou seja,
  de quem forneceu o Python para você). Verifique isso com
  antecedência se você planeja usar o gráficos tartaruga com um
  estudante.


Tutorial
========

As pessoas recém-chegadas devem começar por aqui. Neste tutorial,
exploraremos alguns dos conceitos básicos do desenho de tartarugas.


Iniciando um ambiente da tartaruga
----------------------------------

Em um console do Python, faça a importação de todos os objetos do
módulo "turtle":

   from turtle import *

Se você se deparar com a seguinte mensagem de erro "Standard library
module '_tkinter' was not found", será necessário instalar o "pacote
de interface gráfica Tk" em seu sistema.

Nothing appears yet. To open the turtle window, make the turtle
visible:

   showturtle()

A new window opens, with the turtle in the middle, shown as an arrow
heading East.


Desenho básico
--------------

Envie a tartaruga para frente 100 passos:

   forward(100)

You should see a line drawn by the turtle, heading East. Change the
direction of the turtle, so that it turns 120 degrees left (anti-
clockwise):

   left(120)

Vamos continuar desenhando um triângulo:

   forward(100)
   left(120)
   forward(100)

Observe como a tartaruga, representada por uma seta, aponta em
diferentes direções à medida que você a guia.

Experimente esses comandos, bem como "backward()" e "right()". Muitos
comandos também possuem apelidos mais curtos, como "fd()" para
"forward()".


Controle da Caneta
~~~~~~~~~~~~~~~~~~

Tente alterar a cor - por exemplo, "color('blue')" - e a largura da
linha - por exemplo, "width(3)" - e, em seguida, desenhe novamente.

Você também pode mover a tartaruga sem desenhar, levantando a caneta:
"up()" antes de mover. Para começar a desenhar novamente, use
"down()".


A posição da tartaruga
~~~~~~~~~~~~~~~~~~~~~~

Envie sua tartaruga de volta ao ponto de partida (útil se ela tiver
desaparecido da tela):

   home()

A posição inicial da tartaruga está no centro da tela. Se você
precisar conhecê-la, obtenha as coordenadas x-y da tartaruga com:

   pos()

A a posição inicial fica em "(0, 0)".

E, depois de um tempo, provavelmente vai querer ajudar a limpar a
janela aberta para que possamos começar de novo:

   clearscreen()


Criação de padrões algorítmicos
-------------------------------

Usando laços de repetição, é possível construir criar padrões
geométricos:

   for steps in range(100):
       for c in ('blue', 'red', 'green'):
           color(c)
           forward(steps)
           right(30)

- que, é claro, são limitados apenas pela imaginação!

Vamos desenhar o formato de estrela na parte superior da página.
Queremos linhas de contorno vermelhas, com preenchimento em amarelo:

   color('red')
   fillcolor('yellow')

Assim como "up()" e "down()" determinam se as linhas serão desenhadas,
o preenchimento pode ser ativado e desativado:

   begin_fill()

Em seguida, vamos criar um laço de repetição:

   start = pos()

   while True:
       forward(200)
       left(170)
       if distance(start) < 1:
           break

"distance(start) < 1" é uma boa maneira de saber quando a tartaruga
está de volta à sua posição inicial.

Por fim, complete o preenchimento:

   end_fill()

(Observe que o preenchimento só ocorre de fato quando você fornece o
comando "end_fill()" .)


Referência
==========


Métodos e funções Turtle
------------------------

A maioria dos exemplos desta seção referem-se a uma instância Turtle
chamada "turtle".


Movimento e desenho
~~~~~~~~~~~~~~~~~~~

turtle.forward(distance)
turtle.fd(distance)

   Parâmetros:
      **distance** -- um número

   Move a tartaruga para frente pela *distance* especificada, na
   direção em que a tartaruga está indo.

      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.forward(25)
      >>> turtle.position()
      (25.00,0.00)
      >>> turtle.forward(-75)
      >>> turtle.position()
      (-50.00,0.00)

turtle.back(distance)
turtle.bk(distance)
turtle.backward(distance)

   Parâmetros:
      **distance** -- um número

   Move a tartaruga para trás por *distance*, na direção oposta à
   direção em que a tartaruga está indo. A direção da tartaruga não
   muda.

      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.backward(30)
      >>> turtle.position()
      (-30.00,0.00)

turtle.right(angle)
turtle.rt(angle)

   Parâmetros:
      **angle** -- um número

   Gira a tartaruga para direita pelo ângulo *angle* especificado. Por
   padrão, o ângulo é medido em graus; a unidade pode ser alterada com
   "degrees()" ou "radians()". A forma como a direção é medida depende
   do modo da tartaruga; consulte "mode()".

      >>> turtle.heading()
      22.0
      >>> turtle.right(45)
      >>> turtle.heading()
      337.0

turtle.left(angle)
turtle.lt(angle)

   Parâmetros:
      **angle** -- um número

   Gira a tartaruga para esquerda pelo ângulo *angle* especificado.
   Por padrão, o ângulo é medido em graus; a unidade pode ser alterada
   com "degrees()" ou "radians()". A forma como a direção é medida
   depende do modo da tartaruga; consulte "mode()".

      >>> turtle.heading()
      22.0
      >>> turtle.left(45)
      >>> turtle.heading()
      67.0

turtle.goto(x, y=None)
turtle.setpos(x, y=None)
turtle.setposition(x, y=None)

   Parâmetros:
      * **x** -- um número ou um par/vetor de números

      * **y** -- um número ou "None"

   Move a tartaruga para uma posição absoluta. Se *y* for "None", *x*
   deve ser um par de coordenadas ou um "Vec2D", como, por exemplo, o
   valor retornado por "pos()". Se a caneta estiver abaixada, uma
   linha é desenhada. A orientação da tartaruga não muda.

      >>> tp = turtle.pos()
      >>> tp
      (0.00,0.00)
      >>> turtle.goto(60,30)
      >>> turtle.pos()
      (60.00,30.00)
      >>> turtle.goto((20,80))
      >>> turtle.pos()
      (20.00,80.00)
      >>> turtle.goto(tp)
      >>> turtle.pos()
      (0.00,0.00)

turtle.teleport(x=None, y=None, *, fill_gap=False)

   Parâmetros:
      * **x** -- um número ou "None"

      * **y** -- um número ou "None"

      * **fill_gap** -- um valor booleano

   Teleport, or instantly move, the turtle to an absolute position.
   Unlike "goto()", no line is drawn. If *x* or *y* is not given, that
   coordinate is kept as it is. The turtle's heading does not change.

   If the turtle is filling a shape, the shape drawn so far is
   finished and filled before teleporting, and filling starts again at
   the new position. Pass "fill_gap=True" to keep filling one shape
   instead. The teleport then counts as an edge of the shape, as it
   would with "goto()".

      >>> tp = turtle.pos()
      >>> tp
      (0.00,0.00)
      >>> turtle.teleport(60)
      >>> turtle.pos()
      (60.00,0.00)
      >>> turtle.teleport(y=10)
      >>> turtle.pos()
      (60.00,10.00)
      >>> turtle.teleport(20, 30)
      >>> turtle.pos()
      (20.00,30.00)

   Adicionado na versão 3.12.

turtle.setx(x)

   Parâmetros:
      **x** -- um número

   Define a coordenada x da tartaruga para *x*. A coordenada y
   permanece inalterada.

      >>> turtle.position()
      (0.00,240.00)
      >>> turtle.setx(10)
      >>> turtle.position()
      (10.00,240.00)

turtle.sety(y)

   Parâmetros:
      **y** -- um número

   Define a coordenada y da tartaruga para *y*. A coordenada x
   permanece inalterada.

      >>> turtle.position()
      (0.00,40.00)
      >>> turtle.sety(-10)
      >>> turtle.position()
      (0.00,-10.00)

turtle.setheading(to_angle)
turtle.seth(to_angle)

   Parâmetros:
      **to_angle** -- um número

   Define a direção da tartaruga para *to_angle*. Aqui estão algumas
   direções mais comuns em graus:

   +---------------------+----------------------+
   | modo padrão         | modo logo            |
   |=====================|======================|
   | 0 - leste           | 0 - norte            |
   +---------------------+----------------------+
   | 90 - norte          | 90 - leste           |
   +---------------------+----------------------+
   | 180 - oeste         | 180 - sul            |
   +---------------------+----------------------+
   | 270 - sul           | 270 - oeste          |
   +---------------------+----------------------+

      >>> turtle.setheading(90)
      >>> turtle.heading()
      90.0

turtle.home()

   Move a tartaruga para a origem, coordenadas (0,0). A direção da
   tartaruga é defina para sua orientação inicial, que depende do
   modo. Veja "mode()".

      >>> turtle.heading()
      90.0
      >>> turtle.position()
      (0.00,-10.00)
      >>> turtle.home()
      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.heading()
      0.0

turtle.circle(radius, extent=None, steps=None)

   Parâmetros:
      * **radius** -- um número

      * **extent** -- um número ou "None"

      * **steps** -- um inteiro ou "None"

   Desenha um círculo com o *radius* dado. O centro são as unidades de
   *radius* à esquerda da tartaruga; *extent*, um ângulo, determina
   qual parte do círculo é desenhada. Se *extent* não for fornecida,
   desenha o círculo inteiro. Se *extent* não for um círculo completo,
   uma extremidade do arco será a posição atual da caneta. Desenha o
   arco no sentido anti-horário se *radius* for positivo, caso
   contrário, no sentido horário. Finalmente, a direção da tartaruga é
   alterada da *extent*.

   Como o círculo é aproximado por um polígono regular inscrito,
   *steps* determina o número de passos a serem usados. Caso não seja
   informado, será calculado automaticamente. Pode ser usado para
   desenhar polígonos regulares.

      >>> turtle.home()
      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.heading()
      0.0
      >>> turtle.circle(50)
      >>> turtle.position()
      (-0.00,0.00)
      >>> turtle.heading()
      0.0
      >>> turtle.circle(120, 180)  # draw a semicircle
      >>> turtle.position()
      (0.00,240.00)
      >>> turtle.heading()
      180.0

turtle.dot()
turtle.dot(size)
turtle.dot(color, /)
turtle.dot(size, color, /)
turtle.dot(size, r, g, b, /)

   Parâmetros:
      * **size** -- a positive integer or "None"

      * **color** -- uma string de cores ou uma tupla de cores
        numéricas

   Draw a circular dot with diameter *size*, using *color*. If *size*
   is not given, the larger of "pensize + 4" and "2 * pensize" is
   used. If *color* is not given, the current pencolor is used.

      >>> turtle.home()
      >>> turtle.dot()
      >>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
      >>> turtle.position()
      (100.00,-0.00)
      >>> turtle.heading()
      0.0

turtle.stamp()

   Carimba uma cópia da forma da tartaruga na tela na posição atual da
   tartaruga. Retorna um stamp_id para esse carimbo, que pode ser
   usado para excluí-lo chamando "clearstamp(stamp_id)".

      >>> turtle.color("blue")
      >>> stamp_id = turtle.stamp()
      >>> turtle.fd(50)

turtle.clearstamp(stampid)

   Parâmetros:
      **stampid** -- um inteiro, deve ser o valor de retorno da
      chamada de "stamp()" anterior

   Exclui o carimbo com o *stamp* fornecido.

      >>> turtle.position()
      (150.00,-0.00)
      >>> turtle.color("blue")
      >>> astamp = turtle.stamp()
      >>> turtle.fd(50)
      >>> turtle.position()
      (200.00,-0.00)
      >>> turtle.clearstamp(astamp)
      >>> turtle.position()
      (200.00,-0.00)

turtle.clearstamps(n=None)

   Parâmetros:
      **n** -- um inteiro  (ou "None")

   Exclui todos ou o primeiro/último *n* dos selos da tartaruga. Se
   *n* for "None", exclui todos os carimbos, se *n* > 0 exclui os
   primeiros *n* carimbos, senão se *n* < 0 exclui os últimos *n*
   carimbos.

      >>> for i in range(8):
      ...     unused_stamp_id = turtle.stamp()
      ...     turtle.fd(30)
      >>> turtle.clearstamps(2)
      >>> turtle.clearstamps(-2)
      >>> turtle.clearstamps()

turtle.undo()

   Desfaz (repetidamente) a(s) última(s) ação(ões) da tartaruga. O
   número de ações de desfazer disponíveis é determinado pelo tamanho
   do buffer de desfazer.

      >>> for i in range(4):
      ...     turtle.fd(50); turtle.lt(80)
      ...
      >>> for i in range(8):
      ...     turtle.undo()

turtle.speed(speed=None)

   Parâmetros:
      **speed** -- an integer, a string or "None"

   Return or set the turtle's speed. If *speed* is not given, return
   the current speed. Otherwise set the turtle's speed to an integer
   from 0 to 10. If *speed* is a number greater than 10 or smaller
   than 0.5, the speed is set to 0. You can also use these names
   instead of numbers:

   * "fastest": 0

   * "fast": 10

   * "normal": 6

   * "slow": 3

   * "slowest": 1

   Speeds from 1 to 10 give increasingly faster animation of line
   drawing and turtle turning. A speed of 0 means that no animation
   takes place: "forward()" and "back()" make the turtle jump, and
   likewise "left()" and "right()" make the turtle turn instantly.

      >>> turtle.speed()
      3
      >>> turtle.speed('normal')
      >>> turtle.speed()
      6
      >>> turtle.speed(9)
      >>> turtle.speed()
      9


Fala o estado de Turtle
~~~~~~~~~~~~~~~~~~~~~~~

turtle.position()
turtle.pos()

   Retorna a localização atual da tartaruga (x,y) como um vetor
   "Vec2D".

      >>> turtle.pos()
      (440.00,-0.00)

turtle.towards(x, y=None)

   Parâmetros:
      * **x** -- um número ou um par/vetor de números ou uma instância
        de tartaruga

      * **y** -- um número caso *x* seja um número, senão "None"

   Retorna o ângulo da linha que vai da posição da tartaruga até
   (x,y). Se *y* for "None", *x* deve ser um par de coordenadas — um
   "Vec2D", por exemplo, como o retornado por "pos()" — ou outra
   tartaruga. O ângulo é medido a partir da orientação inicial da
   tartaruga, a qual depende do modo da tartaruga; consulte "mode()".

      >>> turtle.goto(10, 10)
      >>> turtle.towards(0,0)
      225.0

turtle.xcor()

   Retorna a coordenada X da tartaruga.

      >>> turtle.home()
      >>> turtle.left(50)
      >>> turtle.forward(100)
      >>> turtle.pos()
      (64.28,76.60)
      >>> print(round(turtle.xcor(), 5))
      64.27876

turtle.ycor()

   Retorna a coordenada Y da tartaruga.

      >>> turtle.home()
      >>> turtle.left(60)
      >>> turtle.forward(100)
      >>> print(turtle.pos())
      (50.00,86.60)
      >>> print(round(turtle.ycor(), 5))
      86.60254

turtle.heading()

   Retorna o título atual da tartaruga. O valor depende do modo da
   tartaruga, veja "mode()".

      >>> turtle.home()
      >>> turtle.left(67)
      >>> turtle.heading()
      67.0

turtle.distance(x, y=None)

   Parâmetros:
      * **x** -- um número ou um par/vetor de números ou uma instância
        de tartaruga

      * **y** -- um número caso *x* seja um número, senão "None"

   Retorna a distância da tartaruga para (x,y) em unidades de passo de
   tartaruga. Se *y* for "None", *x* deve ser um par de coordenadas ou
   um "Vec2D", como, por exemplo, o valor retornado por "pos()" ou
   outra tartaruga.

      >>> turtle.home()
      >>> turtle.distance(30,40)
      50.0
      >>> turtle.distance((30,40))
      50.0
      >>> joe = Turtle()
      >>> joe.forward(77)
      >>> turtle.distance(joe)
      77.0


Configurações de medida
~~~~~~~~~~~~~~~~~~~~~~~

turtle.degrees(fullcircle=360.0)

   Parâmetros:
      **fullcircle** -- um número

   Define as unidades de medida de ângulo como graus. O número de
   graus em um círculo completo é definido como *fullcircle*, cujo
   valor padrão é 360.

      >>> turtle.home()
      >>> turtle.left(90)
      >>> turtle.heading()
      90.0

      >>> # Alterar unidade de medida de ângulo para grad (também
      >>> # conhecido como gon, grau ou grado e é igual a 1/100
      >>> # do ângulo reto).
      >>> turtle.degrees(400.0)
      >>> turtle.heading()
      100.0
      >>> turtle.degrees(360)
      >>> turtle.heading()
      90.0

turtle.radians()

   Define as unidades de medida de ângulo para radianos. Equivalente a
   "degrees(2 * math.pi)".

      >>> turtle.home()
      >>> turtle.left(90)
      >>> turtle.heading()
      90.0
      >>> turtle.radians()
      >>> turtle.heading()
      1.5707963267948966


Controle da Caneta
~~~~~~~~~~~~~~~~~~


Estado do Desenho
"""""""""""""""""

turtle.pendown()
turtle.pd()
turtle.down()

   Lower the pen. The turtle draws a line when it moves.

turtle.penup()
turtle.pu()
turtle.up()

   Lift the pen. The turtle does not draw when it moves.

turtle.pensize(width=None)
turtle.width(width=None)

   Parâmetros:
      **width** -- a positive number or "None"

   Return or set the line thickness. If *width* is not given, return
   the current pensize. If resizemode is set to "auto" and the turtle
   shape is a polygon, that polygon is drawn with the same line
   thickness.

      >>> turtle.pensize()
      1
      >>> turtle.pensize(10)   # from here on lines of width 10 are drawn

turtle.pen(pen=None, **pendict)

   Parâmetros:
      * **pen** -- um dicionário com algumas ou todas as chaves
        listadas abaixo

      * **pendict** -- um ou mais argumentos nomeados com as chaves
        listadas abaixo como palavras-chave

   Retorna ou define os atributos da caneta em um "dicionário da
   caneta" com os seguintes pares de chave/valor:

   * "shown": True/False

   * "pendown": True/False

   * "pencolor": string de cores ou tupla de cores

   * "fillcolor": string de cores ou tupla de cores

   * "pensize": número positivo

   * "speed": número na faixa de 0..10.

   * "resizemode": "auto", "user" ou "noresize"

   * "stretchfactor": (número positivo, número positivo)

   * "outline": número positivo

   * "tilt": número

   Este dicionário pode ser usado como argumento para uma chamada
   subsequente para "pen()" para restaurar o estado da caneta
   anterior. Além disso, um ou mais desses atributos podem ser
   fornecidos como argumentos nomeados. Isso pode ser usado para
   definir vários atributos de caneta em uma instrução.

      >>> turtle.pen(fillcolor="black", pencolor="red", pensize=10)
      >>> sorted(turtle.pen().items())
      [('fillcolor', 'black'), ('outline', 1), ('pencolor', 'red'),
       ('pendown', True), ('pensize', 10), ('resizemode', 'noresize'),
       ('shearfactor', 0.0), ('shown', True), ('speed', 9),
       ('stretchfactor', (1.0, 1.0)), ('tilt', 0.0)]
      >>> penstate=turtle.pen()
      >>> turtle.color("yellow", "")
      >>> turtle.penup()
      >>> sorted(turtle.pen().items())[:3]
      [('fillcolor', ''), ('outline', 1), ('pencolor', 'yellow')]
      >>> turtle.pen(penstate, fillcolor="green")
      >>> sorted(turtle.pen().items())[:3]
      [('fillcolor', 'green'), ('outline', 1), ('pencolor', 'red')]

turtle.isdown()

   Return "True" if the pen is down, "False" if it's up.

      >>> turtle.penup()
      >>> turtle.isdown()
      False
      >>> turtle.pendown()
      >>> turtle.isdown()
      True


Controle da Cor
"""""""""""""""

turtle.pencolor()
turtle.pencolor(color, /)
turtle.pencolor(r, g, b, /)

   Retorna ou define a cor da caneta ou pencolor.

   São permitidos quatro formatos de entrada:

   "pencolor()"
      Return the current pencolor as color specification string or as
      a tuple (see example).  May be used as input to another
      "color()", "pencolor()", "fillcolor()" or "bgcolor()" call.

   "pencolor(colorstring)"
      Set the pencolor to *colorstring*, which is a Tk color
      specification string, such as ""red"", ""yellow"", or
      ""#33cc8c"".

   "pencolor((r, g, b))"
      Set the pencolor to the RGB color represented by the tuple of
      *r*, *g*, and *b*. Each of *r*, *g*, and *b* must be between 0
      and colormode, where colormode is either 1.0 or 255 (see
      "colormode()").

   "pencolor(r, g, b)"
      Set the pencolor to the RGB color represented by *r*, *g*, and
      *b*. Each of *r*, *g*, and *b* must be between 0 and colormode.

   If the turtle shape is a polygon, the outline of that polygon is
   drawn with the newly set pencolor.

      >>> colormode()
      1.0
      >>> turtle.pencolor()
      'red'
      >>> turtle.pencolor("brown")
      >>> turtle.pencolor()
      'brown'
      >>> tup = (0.2, 0.8, 0.55)
      >>> turtle.pencolor(tup)
      >>> turtle.pencolor()
      (0.2, 0.8, 0.5490196078431373)
      >>> colormode(255)
      >>> turtle.pencolor()
      (51.0, 204.0, 140.0)
      >>> turtle.pencolor('#32c18f')
      >>> turtle.pencolor()
      (50.0, 193.0, 143.0)

turtle.fillcolor()
turtle.fillcolor(color, /)
turtle.fillcolor(r, g, b, /)

   Retorna ou define o fillcolor.

   São permitidos quatro formatos de entrada:

   "fillcolor()"
      Return the current fillcolor as color specification string,
      possibly in tuple format (see example).  May be used as input to
      another "color()", "pencolor()", "fillcolor()" or "bgcolor()"
      call.

   "fillcolor(colorstring)"
      Set the fillcolor to *colorstring*, which is a Tk color
      specification string, such as ""red"", ""yellow"", or
      ""#33cc8c"".

   "fillcolor((r, g, b))"
      Set the fillcolor to the RGB color represented by the tuple of
      *r*, *g*, and *b*. Each of *r*, *g*, and *b* must be between 0
      and colormode, where colormode is either 1.0 or 255 (see
      "colormode()").

   "fillcolor(r, g, b)"
      Set the fillcolor to the RGB color represented by *r*, *g*, and
      *b*. Each of *r*, *g*, and *b* must be between 0 and colormode.

   If the turtle shape is a polygon, the interior of that polygon is
   drawn with the newly set fillcolor.

      >>> turtle.fillcolor("violet")
      >>> turtle.fillcolor()
      'violet'
      >>> turtle.pencolor()
      (50.0, 193.0, 143.0)
      >>> turtle.fillcolor((50, 193, 143))  # Inteiros, não pontos flutuantes
      >>> turtle.fillcolor()
      (50.0, 193.0, 143.0)
      >>> turtle.fillcolor('#ffffff')
      >>> turtle.fillcolor()
      (255.0, 255.0, 255.0)

turtle.color()
turtle.color(color, /)
turtle.color(r, g, b, /)
turtle.color(pencolor, fillcolor, /)

   Return or set the pencolor and fillcolor.

   Several input formats are allowed. They use 0 to 3 arguments as
   follows:

   "color()"
      Retorna os valores atuais de pencolor e fillcollor como um par
      de cores como strings ou tuplas conforme retornado por
      "pencolor()" e "fillcolor()".

   "color(colorstring)", "color((r,g,b))", "color(r,g,b)"
      Inputs as in "pencolor()". Set both the pencolor and the
      fillcolor to the given value.

   "color(colorstring1, colorstring2)", "color((r1,g1,b1),
   (r2,g2,b2))"
      Equivalente a "pencolor(colorstring1)" e
      "fillcolor(colorstring2)" e de forma análoga se a outra
      formatação de entrada for usada.

   If the turtle shape is a polygon, the outline and interior of that
   polygon are drawn with the newly set colors.

      >>> turtle.color("red", "green")
      >>> turtle.color()
      ('red', 'green')
      >>> color("#285078", "#a0c8f0")
      >>> color()
      ((40.0, 80.0, 120.0), (160.0, 200.0, 240.0))

Veja também: Método da tela "colormode()".


Preenchimento
"""""""""""""

turtle.filling()

   Return "True" if the turtle is filling, "False" otherwise.

      >>> turtle.begin_fill()
      >>> if turtle.filling():
      ...    turtle.pensize(5)
      ... else:
      ...    turtle.pensize(3)

turtle.fill()

   Preenche a forma desenhada no bloco "with turtle.fill():".

      >>> turtle.color("black", "red")
      >>> with turtle.fill():
      ...     turtle.circle(80)

   Usar "fill()" equivale a adicionar "begin_fill()" antes do bloco de
   preenchimento e "end_fill()" depois do bloco de preenchimento:

      >>> turtle.color("black", "red")
      >>> turtle.begin_fill()
      >>> turtle.circle(80)
      >>> turtle.end_fill()

   Adicionado na versão 3.14.

turtle.begin_fill()

   Deve ser chamado antes de desenhar uma forma a ser preenchida.

turtle.end_fill()

   Preenche a forma desenhada após a última chamada para
   "begin_fill()".

   O preenchimento ou não de regiões sobrepostas para polígonos que se
   cruzam ou formas múltiplas depende dos gráficos do sistema
   operacional, do tipo de sobreposição e do número de sobreposições.
   Por exemplo, a estrela da Tartaruga acima pode ser toda amarela ou
   ter algumas regiões brancas.

      >>> turtle.color("black", "red")
      >>> turtle.begin_fill()
      >>> turtle.circle(80)
      >>> turtle.end_fill()


Mais sobre o Controle do Desenho
""""""""""""""""""""""""""""""""

turtle.reset()

   Delete the turtle's drawings and re-center the turtle. The turtle's
   settings are restored to their default values.

      >>> turtle.goto(0,-22)
      >>> turtle.left(100)
      >>> turtle.position()
      (0.00,-22.00)
      >>> turtle.heading()
      100.0
      >>> turtle.reset()
      >>> turtle.position()
      (0.00,0.00)
      >>> turtle.heading()
      0.0

turtle.clear()

   Delete the turtle's drawings from the screen. The state and
   position of the turtle as well as the drawings of other turtles are
   not affected.

turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))

   Parâmetros:
      * **arg** -- objeto a ser escrito na TurtleScreen

      * **move** -- True/False

      * **align** -- uma das Strings "left", "center" ou right"

      * **font** -- a triple (fontname, fontsize, fonttype)

   Escreve o texto - a representação string de *arg* - na posição
   atual da tartaruga de acordo com *align* ("left", "center" ou
   "right") e com a fonte fornecida. Se *move* for verdadeiro, a
   caneta será movida para o canto inferior direito do texto.  Por
   padrão, *move* é "False".

      >>> turtle.write("Home = ", True, align="center")
      >>> turtle.write((0,0), True)


Estado da tartaruga
~~~~~~~~~~~~~~~~~~~


Visibilidade
""""""""""""

turtle.hideturtle()
turtle.ht()

   Make the turtle invisible. If the pen is down, movement still
   draws.

turtle.showturtle()
turtle.st()

   Tornar a tartaruga visível.

turtle.isvisible()

   Return "True" if the turtle is visible, "False" if it's hidden.

      >>> turtle.hideturtle()
      >>> turtle.isvisible()
      False
      >>> turtle.showturtle()
      >>> turtle.isvisible()
      True


Aparência
"""""""""

turtle.shape(name=None)

   Parâmetros:
      **name** -- a string or "None"

   Set the turtle shape to the named shape. If *name* is not given,
   return the name of the current shape. The shape must exist in the
   "TurtleScreen"'s shape dictionary. Initially there are the
   following shapes: "arrow", "turtle", "circle", "square", "triangle"
   and "classic". To add shapes, see the "Screen" method
   "register_shape()".

      >>> turtle.shape()
      'classic'
      >>> turtle.shape("turtle")
      >>> turtle.shape()
      'turtle'

turtle.resizemode(rmode=None)

   Parâmetros:
      **rmode** -- a string or "None"

   Set the resizemode to "auto", "user" or "noresize". If *rmode* is
   not given, return the current resizemode. The different resizemodes
   have the following effects:

   * "auto": the turtle is resized according to the value of
     "pensize()".

   * "user": the turtle is resized according to the stretch factors
     and outline width, which are set by "shapesize()".

   * "noresize": the turtle is not resized.

   "resizemode("user")" é chamado por "shapesize()" quando usado com
   argumentos.

      >>> turtle.resizemode()
      'noresize'
      >>> turtle.resizemode("auto")
      >>> turtle.resizemode()
      'auto'

turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
turtle.turtlesize(stretch_wid=None, stretch_len=None, outline=None)

   Parâmetros:
      * **stretch_wid** -- a positive number or "None"

      * **stretch_len** -- a positive number or "None"

      * **outline** -- a positive number or "None"

   Return or set the turtle's stretch factors and outline width. If no
   arguments are given, return the current values. Otherwise set
   resizemode to "user", so that the turtle is displayed stretched
   according to its stretch factors:

   * *stretch_wid*: the stretch factor perpendicular to the turtle's
     heading

   * *stretch_len*: the stretch factor in the direction of the
     turtle's heading

   * *outline*: the width of the shape's outline

   For example, "shapesize(2, 1)" makes the turtle twice as wide
   without changing its length. If only *stretch_wid* is given,
   *stretch_len* is set to the same value.

      >>> turtle.shapesize()
      (1.0, 1.0, 1)
      >>> turtle.resizemode("user")
      >>> turtle.shapesize(5, 5, 12)
      >>> turtle.shapesize()
      (5, 5, 12)
      >>> turtle.shapesize(outline=8)
      >>> turtle.shapesize()
      (5, 5, 8)

turtle.shearfactor(shear=None)

   Parâmetros:
      **shear** -- número (opcional)

   Define ou retorna o fator de shearfactor atual. Corta a forma de
   tartaruga de acordo com o fator de shearfactor fornecido, que é a
   tangente do ângulo de shearfactor. *Não* muda a direção da
   tartaruga (direção do movimento). Se o shearfactor não for
   fornecido: retorna o fator de shearfactor atual, i. Isso é. a
   tangente do ângulo de shearfactor, pelo qual as linhas paralelas à
   direção da tartaruga são cortadas.

      >>> turtle.shape("circle")
      >>> turtle.shapesize(5,2)
      >>> turtle.shearfactor(0.5)
      >>> turtle.shearfactor()
      0.5

turtle.tilt(angle)

   Parâmetros:
      **angle** -- um número

   Gira a forma de tartaruga em um *ângulo* a partir de seu ângulo de
   inclinação atual, mas *não* altera o rumo da tartaruga (direção do
   movimento).

      >>> turtle.reset()
      >>> turtle.shape("circle")
      >>> turtle.shapesize(5,2)
      >>> turtle.tilt(30)
      >>> turtle.fd(50)
      >>> turtle.tilt(30)
      >>> turtle.fd(50)

turtle.tiltangle(angle=None)

   Parâmetros:
      **angle** -- um número (opcional)

   Define ou retorna o ângulo de inclinação atual. Se o ângulo for
   fornecido, gira a forma de tartaruga para apontar na direção
   especificada pelo ângulo, independentemente do seu ângulo de
   inclinação atual. *Não* muda a direção da tartaruga (direção do
   movimento). Se o ângulo não for fornecido: retorna o ângulo de
   inclinação atual, que é o ângulo entre a orientação da forma da
   tartaruga e a direção da tartaruga (sua direção de movimento).

      >>> turtle.reset()
      >>> turtle.shape("circle")
      >>> turtle.shapesize(5,2)
      >>> turtle.tilt(45)
      >>> turtle.tiltangle()
      45.0

turtle.shapetransform(t11=None, t12=None, t21=None, t22=None)

   Parâmetros:
      * **t11** -- um número (opcional)

      * **t12** -- um número (opcional)

      * **t21** -- um número (opcional)

      * **t12** -- um número (opcional)

   Define ou retorna a matriz de transformação atual da forma da
   tartaruga.

   Se nenhum dos elementos da matriz for fornecido, retorna a matriz
   de transformação como uma tupla de 4 elementos. Caso contrário,
   define os elementos fornecidos e transforma a forma da tartaruga de
   acordo com a matriz que consiste na primeira linha t11, t12 e na
   segunda linha t21, t22. O resultado de t11 * t22 - t12 * t21 não
   deve ser zero, caso contrário será gerado um erro. Modifica
   stretchfactor, shearfactor e tiltangle de acordo com a matriz
   fornecida.

      >>> turtle = Turtle()
      >>> turtle.shape("square")
      >>> turtle.shapesize(4,2)
      >>> turtle.shearfactor(-0.5)
      >>> turtle.shapetransform()
      (4.0, -1.0, -0.0, 2.0)

turtle.get_shapepoly()

   Retorna o polígono da forma atual como uma tupla de pares de
   coordenadas. Isto pode ser usado para definir uma nova forma ou
   componentes de uma forma composta.

      >>> turtle.shape("square")
      >>> turtle.shapetransform(4, -1, 0, 2)
      >>> turtle.get_shapepoly()
      ((50, -20), (30, 20), (-50, 20), (-30, -20))


Eventos Utilizados
~~~~~~~~~~~~~~~~~~

turtle.onclick(fun, btn=1, add=None)

   Parâmetros:
      * **fun** -- a function with two arguments or "None"

      * **btn** -- an integer

      * **add** -- a boolean or "None"

   Bind *fun* to mouse-click events on this turtle. *fun* is called
   with the coordinates of the clicked point on the canvas. If *fun*
   is "None", existing bindings are removed. *btn* is the number of
   the mouse button and defaults to 1, the left mouse button. If *add*
   is "True", a new binding is added, otherwise it replaces a former
   binding. Example for the anonymous turtle, that is, the procedural
   way:

      >>> def turn(x, y):
      ...     left(180)
      ...
      >>> onclick(turn)  # Agora, clicar na tartaruga irá girá-la.
      >>> onclick(None)  # a associação de eventos será removida

turtle.onrelease(fun, btn=1, add=None)

   Parâmetros:
      * **fun** -- um função com dois argumento que serão chamados com
        as coordenadas do ponto clicado na tela

      * **btn** -- número do botão do mouse, o padrão é 1 (botão
        esquerdo do mouse)

      * **add** -- "True" ou "False" -- se "True", uma nova ligação
        será adicionada; caso contrário, ela substituirá uma ligação
        antiga

   Vincule *fun* aos eventos de liberação do botão do mouse nesta
   tartaruga.  Se *fun* for "None", as associações existentes serão
   removidas.

      >>> class MyTurtle(Turtle):
      ...     def glow(self,x,y):
      ...         self.fillcolor("red")
      ...     def unglow(self,x,y):
      ...         self.fillcolor("")
      ...
      >>> turtle = MyTurtle()
      >>> turtle.onclick(turtle.glow)     # clicar na tartaruga torna o preenchimento vermelho,
      >>> turtle.onrelease(turtle.unglow) # .liberar a transforma em transparente

turtle.ondrag(fun, btn=1, add=None)

   Parâmetros:
      * **fun** -- um função com dois argumento que serão chamados com
        as coordenadas do ponto clicado na tela

      * **btn** -- número do botão do mouse, o padrão é 1 (botão
        esquerdo do mouse)

      * **add** -- "True" ou "False" -- se "True", uma nova ligação
        será adicionada; caso contrário, ela substituirá uma ligação
        antiga

   Vincule *fun* a eventos de movimentação do mouse nessa tartaruga.
   Se *fun* for "None", as associações existentes serão removidas.

   Observação: Cada sequência de eventos de movimento do mouse em uma
   tartaruga é precedida por um evento de clique do mouse naquela
   tartaruga.

      >>> turtle.ondrag(turtle.goto)

   Posteriormente, clicar e arrastar a Tartaruga a moverá pela tela,
   produzindo desenhos à mão (se a caneta estiver deitada).


Métodos Especiais da Tartaruga
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

turtle.poly()

   Registra os vértices de um polígono desenhado no bloco "with
   turtle.poly():". O primeiro e o último vértices serão conectados.

      >>> with turtle.poly():
      ...     turtle.forward(100)
      ...     turtle.right(60)
      ...     turtle.forward(100)

   Adicionado na versão 3.14.

turtle.begin_poly()

   Start recording the vertices of a polygon. The current turtle
   position is the first vertex of the polygon.

turtle.end_poly()

   Stop recording the vertices of a polygon. The current turtle
   position is the last vertex of the polygon. This will be connected
   with the first vertex.

turtle.get_poly()

   Retorna o último polígono registrado.

      >>> turtle.home()
      >>> turtle.begin_poly()
      >>> turtle.fd(100)
      >>> turtle.left(20)
      >>> turtle.fd(30)
      >>> turtle.left(60)
      >>> turtle.fd(50)
      >>> turtle.end_poly()
      >>> p = turtle.get_poly()
      >>> register_shape("myFavouriteShape", p)

turtle.clone()

   Create and return a clone of the turtle. The clone has the same
   position, heading and turtle properties.

      >>> leonel = Turtle()
      >>> marco = leonel.clone()

turtle.getturtle()
turtle.getpen()

   Return the Turtle object itself.

   Call "getturtle()" to get the turtle used by functions such as
   "forward()" and "left()":

      >>> pet = getturtle()
      >>> pet.fd(50)
      >>> pet
      <turtle.Turtle object at 0x...>

turtle.getscreen()

   Retorna o objeto "TurtleScreen" no qual a tartaruga está sendo
   desenhada. Os métodos de TurtleScreen podem então ser chamados para
   este objeto.

      >>> ts = turtle.getscreen()
      >>> ts
      <turtle._Screen object at 0x...>
      >>> ts.bgcolor("pink")

turtle.setundobuffer(size)

   Parâmetros:
      **size** -- um inteiro ou "None"

   Set or disable the undo buffer. If *size* is an integer, an empty
   undo buffer of the given size is installed. *size* is the maximum
   number of turtle actions that can be undone by "undo()". If *size*
   is "None", the undo buffer is disabled.

      >>> turtle.setundobuffer(42)

turtle.undobufferentries()

   Return the number of entries in the undo buffer.

      >>> while undobufferentries():
      ...     undo()


Métodos e funções de janela
---------------------------

A maioria dos exemplos desta seção se refere a uma instância de
TurtleScreen chamada "screen".


Controle da Janela
~~~~~~~~~~~~~~~~~~

turtle.bgcolor()
turtle.bgcolor(color, /)
turtle.bgcolor(r, g, b, /)

   Retorna ou define a cor de fundo do TurtleScreen.

   São permitidos quatro formatos de entrada:

   "bgcolor()"
      Return the current background color as a color specification
      string or as a tuple (see example).  May be used as input to
      another "color()", "pencolor()", "fillcolor()" or "bgcolor()"
      call.

   "bgcolor(colorstring)"
      Define a cor de fundo como *colorstring*, que é uma string de
      especificação de cor Tk, como ""red"", ""yellow"" ou
      ""#33cc8c"".

   "bgcolor((r, g, b))"
      Set the background color to the RGB color represented by the
      tuple of *r*, *g*, and *b*. Each of *r*, *g*, and *b* must be
      between 0 and colormode, where colormode is either 1.0 or 255
      (see "colormode()").

   "bgcolor(r, g, b)"
      Set the background color to the RGB color represented by *r*,
      *g*, and *b*. Each of *r*, *g*, and *b* must be between 0 and
      colormode.

      >>> screen.bgcolor("orange")
      >>> screen.bgcolor()
      'orange'
      >>> screen.bgcolor("#800080")
      >>> screen.bgcolor()
      (128.0, 0.0, 128.0)

turtle.bgpic(picname=None)

   Parâmetros:
      **picname** -- um string, um nome de um arquivo de imagem (PNG,
      GIF, PGM e PPM) ou ""nopic"", ou "None"

   Configura a imagem de fundo ou retorna nome da imagem de fundo
   atual. Se *picname* for um nome de arquivo, definirá a imagem
   correspondente como plano de fundo. Se *picname* for ""nopic"",
   exclui a imagem de fundo, caso haja. Se *picname* for "None",
   retorna o nome do arquivo da imagem de fundo atual:

      >>> screen.bgpic()
      'nopic'
      >>> screen.bgpic("landscape.gif")
      >>> screen.bgpic()
      "landscape.gif"

turtle.clear()

   Nota:

     Este método de TurtleScreen está disponível como uma função
     global somente sob o nome "clearscreen". A função global "clear"
     é derivada de forma diferente do método de Turtle "clear" .

turtle.clearscreen()

   Remove todos os desenhos e todas as tartarugas da TurtleScreen.
   Redefine a TurtleScreen, agora vazia, para seu estado inicial:
   fundo branco, sem imagem de fundo, sem vínculos de eventos e
   rastreamento ativado.

turtle.reset()

   Nota:

     Este método de TurtleScreen está disponível como uma função
     global somente com o nome "resetscreen". A função global "reset"
     é outra derivada do método de Turtle "reset" .

turtle.resetscreen()

   Reset all turtles on the screen to their initial state.

turtle.screensize(canvwidth=None, canvheight=None, bg=None)

   Parâmetros:
      * **canvwidth** -- positivo inteiro, a nova largura da tela em
        pixels

      * **canvheight** -- positivo inteiro, a nova altura da tela em
        pixels

      * **bg** -- Uma string com a cor ou uma tupla, a nova cor de
        fundo

   Se nenhum argumento for fornecido, retorna o atual (canvaswidth,
   canvasheight). Caso contrário, redimensiona a tela em que as
   tartarugas estão desenhadas. Não altera a janela de desenho. Para
   observar as partes ocultas da tela, use as barras de rolagem. Com
   este método, é possível tornar visíveis as partes de um desenho que
   antes estavam fora da tela.

      >>> screen.screensize()
      (400, 300)
      >>> screen.screensize(2000,1500)
      >>> screen.screensize()
      (2000, 1500)

   Por exemplo, para procurar uma tartaruga que escapou por engano ;-)

turtle.setworldcoordinates(llx, lly, urx, ury)

   Parâmetros:
      * **llx** -- um número

      * **lly** -- um número

      * **urx** -- um número

      * **ury** -- um número

   Set up a user-defined coordinate system. *llx* and *lly* are the x
   and y coordinates of the lower left corner of the canvas. *urx* and
   *ury* are the x and y coordinates of the upper right corner. Switch
   to mode "world" if necessary, which performs a reset. If mode
   "world" is already active, all drawings are redrawn according to
   the new coordinates. In user-defined coordinate systems, angles may
   appear distorted, see "mode()".

      >>> screen.reset()
      >>> screen.setworldcoordinates(-50,-7.5,50,7.5)
      >>> for _ in range(72):
      ...     left(10)
      ...
      >>> for _ in range(8):
      ...     left(45); fd(2)   # a regular octagon


Controle da animação
~~~~~~~~~~~~~~~~~~~~

turtle.no_animation()

   Temporarily turn off turtle animation. The code inside the "with"
   block is not animated. Once the block is exited, the drawing
   appears. This is useful for drawing complex shapes where even the
   fastest speed setting is too slow.

      >>> with screen.no_animation():
      ...     for dist in range(2, 400, 2):
      ...         fd(dist)
      ...         rt(90)

   Adicionado na versão 3.14.

turtle.delay(delay=None)

   Parâmetros:
      **delay** -- a nonnegative integer or "None"

   Return or set the drawing delay in milliseconds. This is
   approximately the time interval between two consecutive canvas
   updates. The longer the drawing delay, the slower the animation.

      >>> screen.delay()
      10
      >>> screen.delay(5)
      >>> screen.delay()
      5

turtle.tracer(n=None, delay=None)

   Parâmetros:
      * **n** -- a nonnegative integer or "None"

      * **delay** -- a nonnegative integer or "None"

   Turn turtle animation on or off and set the drawing delay. If *n*
   is given, only every n-th regular screen update is performed, which
   can be used to speed up the drawing of complex graphics. If *n* is
   0, animation is turned off and the screen is only updated by
   calling "update()". If *delay* is given, it sets the drawing delay,
   see "delay()". When called without arguments, return the current
   value of *n*.

      >>> screen.tracer(8, 25)
      >>> dist = 2
      >>> for i in range(200):
      ...     fd(dist)
      ...     rt(90)
      ...     dist += 2

turtle.update()

   Executa uma atualização do TurtleScreen. Para ser usado quando o
   rastreador estiver desligado.

Veja também o método RawTurtle/Turtle "speed()".


Usando os eventos de tela
~~~~~~~~~~~~~~~~~~~~~~~~~

turtle.listen(xdummy=None, ydummy=None)

   Define o foco no TurtleScreen (para coletar eventos-chave).
   Argumentos fictícios são fornecidos para que seja possível passar
   "listen()" para o método onclick.

turtle.onkey(fun, key)
turtle.onkeyrelease(fun, key)

   Parâmetros:
      * **fun** -- uma função sem argumentos ou "None"

      * **key** -- uma string: uma tecla (por exemplo, "a") ou o nome
        de uma tecla (por exemplo, "space")

   Vincula *fun* ao evento de liberação da tecla. Se *fun* for "None",
   as ligações de eventos serão removidas. Observação: para poder
   registrar eventos-chave, o TurtleScreen deve ter o foco. (Veja o
   método "listen()".)

      >>> def f():
      ...     fd(50)
      ...     lt(60)
      ...
      >>> screen.onkey(f, "Up")
      >>> screen.listen()

turtle.onkeypress(fun, key=None)

   Parâmetros:
      * **fun** -- uma função sem argumentos ou "None"

      * **key** -- uma string: uma tecla (por exemplo, "a") ou o nome
        de uma tecla (por exemplo, "space")

   Vincula *fun* ao evento de pressionamento de tecla se a tecla for
   fornecida, ou a qualquer evento de pressionamento de tecla se
   nenhuma tecla for fornecida. Observação: para poder registrar
   eventos-chave, o TurtleScreen deve ter foco. (Veja o método
   "listen()".)

      >>> def f():
      ...     fd(50)
      ...
      >>> screen.onkey(f, "Up")
      >>> screen.listen()

turtle.onclick(fun, btn=1, add=None)
turtle.onscreenclick(fun, btn=1, add=None)

   Parâmetros:
      * **fun** -- a function with two arguments or "None"

      * **btn** -- an integer

      * **add** -- a boolean or "None"

   Bind *fun* to mouse-click events on this screen. *fun* is called
   with the coordinates of the clicked point on the canvas. If *fun*
   is "None", existing bindings are removed. *btn* is the number of
   the mouse button and defaults to 1, the left mouse button. If *add*
   is "True", a new binding is added, otherwise it replaces a former
   binding.

   Exemplo de uma instância de TurtleScreen chamada "screen" e uma
   instância de Turtle chamada "turtle":

      >>> screen.onclick(turtle.goto) # Em seguida, clicar no TurtleScreen
      >>>                             # fará a tartaruga se mover até o ponto clicado.
      >>> screen.onclick(None)        # remove associação de evento novamente

   Nota:

     Este método TurtleScreen está disponível como uma função global
     somente com o nome "onscreenclick". A função global "onclick" é
     outra derivada do método de Turtle "onclick" .

turtle.ontimer(fun, t=0)

   Parâmetros:
      * **fun** -- um função sem nenhum argumento

      * **t** -- um número >= 0

   Instala um cronômetro que chama *fun* após *t* milissegundos.

      >>> running = True
      >>> def f():
      ...     if running:
      ...         fd(50)
      ...         lt(60)
      ...         screen.ontimer(f, 250)
      >>> f()   ### faz a tartaruga marchar
      >>> running = False

turtle.mainloop()
turtle.done()

   Start the event loop by calling Tkinter's "mainloop()" method. Must
   be the last statement in a turtle graphics program. Must *not* be
   used if a script is run from within IDLE in -n mode (see Running
   without a subprocess).


Métodos de entrada
~~~~~~~~~~~~~~~~~~

turtle.textinput(title, prompt)

   Parâmetros:
      * **title** -- uma string

      * **prompt** -- uma string

   Pop up a dialog window for input of a string. *title* is the title
   of the dialog window and *prompt* is a text describing what
   information to input. Return the string entered. If the dialog is
   canceled, return "None".

      >>> screen.textinput("NIM", "Name of first player:")

turtle.numinput(title, prompt, default=None, minval=None, maxval=None)

   Parâmetros:
      * **title** -- uma string

      * **prompt** -- uma string

      * **default** -- um número ou "None"

      * **minval** -- um número ou "None"

      * **maxval** -- um número ou "None"

   Pop up a dialog window for input of a number. *title* is the title
   of the dialog window and *prompt* is a text describing what
   numerical information to input. *default* is the default value,
   *minval* and *maxval* are the minimum and maximum values for input.
   If these are given, the number entered must be between *minval* and
   *maxval*. If not, a hint is issued and the dialog remains open for
   correction. Return the number entered. If the dialog is canceled,
   return "None".

      >>> screen.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)


Configurações e métodos especiais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

turtle.mode(mode=None)

   Parâmetros:
      **mode** -- a string or "None"

   Set the turtle mode and perform a reset. *mode* is one of the
   strings "standard", "logo" or "world". If *mode* is not given,
   return the current mode.

   Mode "standard" is compatible with the old "turtle" module. Mode
   "logo" is compatible with most Logo turtle graphics. Mode "world"
   uses user-defined world coordinates, see "setworldcoordinates()".
   In this mode, angles appear distorted if the x and y units are not
   of equal length.

   +--------------+---------------------------+---------------------+
   | Modo         | Título inicial da         | ângulos positivos   |
   |              | tartaruga                 |                     |
   |==============|===========================|=====================|
   | "standard"   | para a direita (east)     | counterclockwise    |
   +--------------+---------------------------+---------------------+
   | "logo"       | upward (north)            | sentido horário     |
   +--------------+---------------------------+---------------------+

      >>> mode("logo")  # resets turtle heading to north
      >>> mode()
      'logo'

turtle.colormode(cmode=None)

   Parâmetros:
      **cmode** -- um número ou "None"

   Return the colormode or set it to 1.0 or 255. After setting it, the
   *r*, *g* and *b* values of color triples have to be between 0 and
   *cmode*.

      >>> screen.colormode(1)
      >>> turtle.pencolor(240, 160, 80)
      Traceback (most recent call last):
           ...
      TurtleGraphicsError: bad color sequence: (240, 160, 80)
      >>> screen.colormode()
      1.0
      >>> screen.colormode(255)
      >>> screen.colormode()
      255
      >>> turtle.pencolor(240,160,80)

turtle.getcanvas()

   Retorna a tela desse TurtleScreen.  Útil para pessoas que sabem o
   que fazer com uma tela do Tkinter.

      >>> cv = screen.getcanvas()
      >>> cv
      <turtle.ScrolledCanvas object ...>

turtle.getshapes()

   Retorna uma lista dos nomes de todas as formas de tartarugas
   disponíveis no momento.

      >>> screen.getshapes()
      ['arrow', 'blank', 'circle', ..., 'turtle']

turtle.register_shape(name, shape=None)
turtle.addshape(name, shape=None)

   Parâmetros:
      * **name** -- uma string

      * **shape** -- a string, a tuple of pairs of numbers, a "Shape"
        object or "None"

   Add a turtle shape to the TurtleScreen's shape list. It can be
   called in four different ways:

   1. *name* é o nome de um arquivo de imagem (PNG, GIF, PGM e PPM) e
      *shape* é "None": Instala a forma de imagem correspondente.

         >>> screen.register_shape("turtle.gif")

   2. *name* é uma string arbitrária e *shape* é o nome de um arquivo
      de imagem (PNG, GIF, PGM e PPM): Instala a forma de imagem
      correspondente.

         >>> screen.register_shape("turtle", "turtle.gif")

   3. *name* é uma string arbitrária e *shape* é um tupla de pares de
      coordenadas: Instala a forma de polígono correspondente.

         >>> screen.register_shape("triangle", ((5,-3), (0,5), (-5,-3)))

   4. *name* é uma string arbitrária e *shape* é um objeto (composto)
      "Shape": Instala a forma composta correspondente.

   Image shapes do not rotate when turning the turtle, so they do not
   display the heading of the turtle. To use a registered shape, call
   "shape()" with its name.

   Alterado na versão 3.14: Adicionado suporte para os formatos de
   imagem PNG, PGM e PPM. É possível especificar tanto o nome da forma
   quanto o nome do arquivo de imagem.

turtle.turtles()

   Retorne uma lista de tartarugas na tela.

      >>> for turtle in screen.turtles():
      ...     turtle.color("red")

turtle.window_height()

   Retorna a altura da janela da tartaruga.

      >>> screen.window_height()
      480

turtle.window_width()

   Retorna a largura da janela da tartaruga.

      >>> screen.window_width()
      640


Métodos apenas de janela
~~~~~~~~~~~~~~~~~~~~~~~~

turtle.bye()

   Close the turtle graphics window.

turtle.exitonclick()

   Vincula o método "bye()" aos cliques do mouse na tela.

   Se o valor "using_IDLE" na configuração dicionário for "False"
   (valor padrão), entra também no loop principal. Observação: Se IDLE
   for executado com a chave "-n" (sem subprocesso), esse valor deverá
   ser definido como "True" em "turtle.cfg". Nesse caso, o loop
   principal do próprio IDLE também estará ativo para o script do
   cliente.

turtle.save(filename, overwrite=False)

   Salva o desenho atual da tartaruga (e tartarugas) como um arquivo
   PostScript.

   Parâmetros:
      * **filename** -- o caminho do arquivo PostScript salvo

      * **overwrite** -- Se for "False" e já existir um arquivo com o
        nome fornecido, a função levantará uma "FileExistsError". Se
        for "True", o arquivo será sobrescrito.

      >>> screen.save("my_drawing.ps")
      >>> screen.save("my_drawing.ps", overwrite=True)

   Adicionado na versão 3.14.

turtle.setup(width=_CFG['width'], height=_CFG['height'], startx=_CFG['leftright'], starty=_CFG['topbottom'])

   Define o tamanho e a posição da janela principal. Os valores
   padrões dos argumentos são armazenados na configuração dicionário e
   podem ser alterados por meio de um arquivo "turtle.cfg".

   Parâmetros:
      * **width** -- se for um inteiro, o tamanho em pixels; se for um
        float, uma fração da tela; o padrão é 50% da tela

      * **height** -- se for um inteiro, a altura em pixels; se for um
        float, uma fração da tela; o padrão é 75% da tela

      * **startx** -- se positivo, este parâmetro define a posição
        inicial em pixels a partir da borda esquerda da tela; se
        negativo, define a partir da borda direita; se "None",
        centraliza a janela horizontalmente

      * **starty** -- se positivo, este parâmetro define a posição
        inicial, em pixels, a partir da borda superior da tela; se
        negativo, define a partir da borda inferior; se for "None",
        centraliza a janela verticalmente

      >>> screen.setup (width=200, height=200, startx=0, starty=0)
      >>>              # define a janela para 200x200 pixels, no canto superior esquerdo da tela
      >>> screen.setup(width=.75, height=0.5, startx=None, starty=None)
      >>>              # define a janela para 75% da tela por 50% da tela e centraliza

turtle.title(titlestring)

   Parâmetros:
      **titlestring** -- uma string

   Set the title of the turtle window to *titlestring*. The title is
   shown in the title bar of the turtle graphics window.

      >>> screen.title("Welcome to the turtle zoo!")


Classes Públicas
----------------

class turtle.RawTurtle(canvas)
class turtle.RawPen(canvas)

   Parâmetros:
      **canvas** -- um "tkinter.Canvas", um "ScrolledCanvas" ou um
      "TurtleScreen"

   Cria uma tartaruga.  A tartaruga tem todos os métodos descritos
   acima como "métodos de Turtle/RawTurtle".

class turtle.Turtle

   Subclasse do RawTurtle, tem a mesma interface, mas desenha em um
   objeto padrão "Screen", que é criado automaticamente, quando
   necessário, pela primeira vez.

class turtle.TurtleScreen(cv)

   Parâmetros:
      **cv** -- uma "tkinter.Canvas"

   Fornece métodos orientado para a tela, como "bgcolor()" etc., que
   são descritos acima.

class turtle.Screen

   Subclass of "TurtleScreen", with four methods added. Calling
   "Screen()" returns the single screen object. If it does not exist
   yet, it is created. Otherwise the existing one is returned.

class turtle.ScrolledCanvas(master)

   Parâmetros:
      **master** -- algum widget do Tkinter para conter o
      ScrolledCanvas. Exemplo: um Tkinter-canvas com barras de rolagem
      adicionadas

   Usado pela classe Screen, que, portanto, fornece automaticamente um
   ScrolledCanvas como playground para as tartarugas.

class turtle.Shape(type_, data)

   Parâmetros:
      * **type_** -- uma string

      * **data** -- depends on *type_*

   Data structure modeling shapes. *type_* is one of the strings
   "polygon", "image" or "compound". What *data* must be depends on
   *type_*: for "polygon" a tuple of pairs of coordinates, for "image"
   an image (only used internally), and for "compound" "None", as a
   compound shape is built up using the "addcomponent()" method.

   addcomponent(poly, fill, outline=None)

      Parâmetros:
         * **poly** -- a tuple of pairs of numbers

         * **fill** -- a color

         * **outline** -- a color or "None"

      Add a component to a shape of type "compound". *poly* is a
      polygon, a tuple of pairs of numbers. *fill* is the color the
      polygon is filled with and *outline* is the color of its
      outline. If *outline* is not given, *fill* is used for it as
      well.

      Exemplo:

         >>> poly = ((0,0), (10,-5), (0,10), (-10,-5))
         >>> s = Shape("compound")
         >>> s.addcomponent(poly, "red", "blue")
         >>> # ... add more components and then use register_shape()

      Veja How to use compound shapes.

class turtle.Vec2D(x, y)

   Uma classe de vetor bidimensional, usada como classe auxiliar para
   implementar gráficos de tartaruga. Pode ser útil também para
   programas de gráficos de tartaruga.  Derivado de uma tupla,
   portanto, um vetor é um tupla!

   Fornece (para vetores *a*, *b*, número *k*):

   * "a + b" vetor adicional

   * "a - b" subtração de vetor

   * "a * b" produto interno

   * "k * a" e "a * k" multiplicação com escalar

   * "abs(a)" valor absoluto de um

   * rotação "a.rotate(angle)"


Exceções
--------

O módulo "turtle" define a seguinte exceção:

exception turtle.TurtleGraphicsError

   Levantada para argumentos ou operações inválidas. Por exemplo, uma
   string de cor malformada:

      >>> turtle.color("blau")
      Traceback (most recent call last):
          ...
      turtle.TurtleGraphicsError: bad color string: blau


Guias de como fazer
===================

Esta seção aborda alguns casos de uso e abordagens típicos do módulo
"turtle".


How to automatically begin and end filling
------------------------------------------

A partir do Python 3.14, você pode usar o *gerenciador de contexto*
"fill()" em vez de "begin_fill()" e "end_fill()" para iniciar e
encerrar o preenchimento automaticamente. Aqui está um exemplo:

   with fill():
       for i in range(4):
           forward(100)
           right(90)

   forward(200)

O código acima equivale a:

   begin_fill()
   for i in range(4):
       forward(100)
       right(90)
   end_fill()

   forward(200)


How to use compound shapes
--------------------------

Para usar formas de tartaruga compostas, que consistem em vários
polígonos de cores diferentes, você deve usar a classe auxiliar
"Shape" explicitamente, conforme descrito abaixo:

1. Create an empty "Shape" object of type "compound".

2. Adicione quantos componentes desejar a esse objeto, usando o método
   "addcomponent()".

   Por exemplo:

      >>> s = Shape("compound")
      >>> poly1 = ((0,0), (10,-5), (0,10), (-10,-5))
      >>> s.addcomponent(poly1, "red", "blue")
      >>> poly2 = ((0,0), (10,-5), (-10,-5))
      >>> s.addcomponent(poly2, "blue", "red")

3. Agora, adicione o Shape à lista de formas da tela e use-o:

      >>> register_shape("myshape", s)
      >>> shape("myshape")


How to use the "turtle" module namespace
----------------------------------------

Usar "from turtle import *" é conveniente, mas lembre-se de que ele
importa um coleção bastante grande de objetos e, se você estiver
fazendo qualquer coisa no seu código que não esteja relacionada com o
módulo gráficos de tartaruga, corre o risco de um conflito de nomes de
objetos (isso se torna um problema ainda maior se você estiver usando
o módulo de gráficos de tartaruga em um script em que outros módulos
possam ser também importados).

A solução é usar o identificador/domínio do próprio módulo "import
turtle" sem o asterisco no final da importação - assim a chamada do
objeto/função "fd()" torna-se "turtle.fd()", da mesma forma como
"width()" torna-se "turtle.width()" e assim por diante.  (Se digitar
"turtle" várias vezes se tornar tedioso, use "import turtle as t", por
exemplo, para fornecer um apelido mais conciso e objetivo ao
identificador/domínio dentro do seu código).


How to use turtle graphics in a script
--------------------------------------

Recomenda-se usar o módulo "turtle" com uma apelido para
identificador/domínio, conforme descrito acima, por exemplo:

   import turtle as t
   from random import random

   for i in range(100):
       steps = int(random() * 100)
       angle = int(random() * 360)
       t.right(angle)
       t.fd(steps)

No entanto, outra etapa também é necessária ou o Python também fechará
a janela da tartaruga assim que o código acima terminar de ser
executado. Adicione:

   t.mainloop()

ao final do código anterior. Assim, o código anterior agora conterá
uma instrução que aguardará ser dispensado e não sairá até que seja
encerrado, por exemplo, fechando a janela aberta pelo módulo gráficos
da tartaruga.


How to use object-oriented turtle graphics
------------------------------------------

Ver também: Explicação de interface orientada a objetos

Exceto para fins introdutórios muito básicos ou para experimentar
coisas o mais rápido possível, é mais comum e muito mais eficiente
usar a abordagem orientada a objetos para gráficos de tartarugas. Por
exemplo, isso permite várias tartarugas na tela ao mesmo tempo.

Nessa abordagem, os vários comandos do módulo turtle são métodos de
objetos (principalmente objetos  de "Turtle"). Você *pode* usar a
abordagem orientada a objetos em console, mas ela seria mais típica em
um script Python.

O exemplo acima se torna então:

   from turtle import Turtle
   from random import random

   t = Turtle()
   for i in range(100):
       steps = int(random() * 100)
       angle = int(random() * 360)
       t.right(angle)
       t.fd(steps)

   t.screen.mainloop()

Observe a última linha. "t.screen" é um instância da subclasse
"Screen" que existe numa instância da classe tartaruga ou "turtle";
ela é criada automaticamente junto com a instância de tartaruga.

A tela da tartaruga pode ser personalizada, por exemplo:

   t.screen.title('Object-oriented turtle demo')
   t.screen.bgcolor("orange")


How to use "help()"
-------------------

Os métodos públicos das classes Screen e Turtle estão amplamente
documentado por meio de docstrings. Eles podem ser usados como ajuda
on-line por meio dos recursos de ajuda do Python:

* Ao usar o IDLE, as dicas de ferramentas mostram as assinaturas e as
  primeiras linhas das docstrings das chamadas de função/método
  digitadas.

* Chamar "help()" em métodos ou funções exibe o seguinte docstring:

     >>> help(Screen.bgcolor)
     Help on method bgcolor in module turtle:

     bgcolor(self, *args) unbound turtle.Screen method
         Set or return backgroundcolor of the TurtleScreen.

         Arguments (if given): a color string or three numbers
         in the range 0..colormode or a 3-tuple of such numbers.


         >>> screen.bgcolor("orange")
         >>> screen.bgcolor()
         "orange"
         >>> screen.bgcolor(0.5,0,0.5)
         >>> screen.bgcolor()
         "#800080"

     >>> help(Turtle.penup)
     Help on method penup in module turtle:

     penup(self) unbound turtle.Turtle method
         Pull the pen up -- no drawing when moving.

         Aliases: penup | pu | up

         No argument

         >>> turtle.penup()

* Os docstrings de funções que são derivados do métodos têm um formato
  diferente:

     >>> help(bgcolor)
     Help on function bgcolor in module turtle:

     bgcolor(*args)
         Set or return backgroundcolor of the TurtleScreen.

         Arguments (if given): a color string or three numbers
         in the range 0..colormode or a 3-tuple of such numbers.

         Example::

           >>> bgcolor("orange")
           >>> bgcolor()
           "orange"
           >>> bgcolor(0.5,0,0.5)
           >>> bgcolor()
           "#800080"

     >>> help(penup)
     Help on function penup in module turtle:

     penup()
         Pull the pen up -- no drawing when moving.

         Aliases: penup | pu | up

         No argument

         Example:
         >>> penup()

Esses docstrings modificados são criados automaticamente junto com as
definições de função que são derivadas de métodos ao importar.


Tradução de docstrings em diferentes idiomas
--------------------------------------------

Há um utilitário para criar a dicionário cujas chaves são os nomes de
método e cujos valores são os docstrings dos métodos públicos das
classes Screen e Turtle.

turtle.write_docstringdict(filename='turtle_docstringdict')

   Parâmetros:
      **filename** -- uma string, usado como nome de arquivo

   Cria e escreve um dicionário de docstring em um script Python com o
   nome de arquivo fornecido. Esta função deve ser chamada
   explicitamente (ela não é usada pelas classes gráficas da
   tartaruga). O dicionário docstring será gravado no script Python
   "*filename*.py". O objetivo é servir como modelo para traduzir os
   documentos para diferentes idiomas.

Se você (ou seus alunos) quiserem usar o "turtle" com a ajuda on-line
em seu idioma nativo, será necessário traduzir os docstrings e salvar
o arquivo resultante como, por exemplo,
"turtle_docstringdict_german.py".

Se você tiver uma entrada específica em seu arquivo "turtle.cfg", esse
dicionário será lido no momento do importar e substituirá as
documentações originais em inglês.

No momento da redação deste texto, há docstring dicionários em alemão
e italiano. (Pedidos devem ser enviados para glingl@aon.at.)


Como configurar Screen and Turtles
----------------------------------

A configuração padrão integrada imita a aparência e o comportamento do
antigo módulo Turtle para manter a melhor compatibilidade possível com
ele.

Se quiser usar uma configuração diferente que reflita melhor o recurso
deste módulo ou que se adapte melhor às suas necessidades, por
exemplo, para uso em uma sala de aula, você pode criar um arquivo de
configuração "turtle.cfg" que será lido no momento de importar e
modifica a configuração de acordo com suas definições.

A configuração que definida no arquivo "turtle.cfg":

   width = 0.5
   height = 0.75
   leftright = None
   topbottom = None
   canvwidth = 400
   canvheight = 300
   mode = standard
   colormode = 1.0
   delay = 10
   undobuffersize = 1000
   shape = classic
   pencolor = black
   fillcolor = black
   resizemode = noresize
   visible = True
   language = english
   exampleturtle = turtle
   examplescreen = screen
   title = Python Turtle Graphics
   using_IDLE = False

Breve explicação das entradas selecionadas:

* As quatro primeiras linhas correspondem aos argumentos do método
  "Screen.setup".

* As linhas 5 e 6 correspondem a argumento do método
  "Screen.screensize".

* *shape* pode ser qualquer uma das formas pré-definidas, como por
  exemplo: seta, tartaruga, etc. Para obter mais informações, consulte
  "help(shape)".

* Se você não quiser usar nenhuma cor de preenchimento (ou seja,
  tornar a tartaruga transparente), você deve usar "fillcolor = """
  (todas as strings não vazias não devem ter aspas no arquivo cfg).

* Se você quiser refletir o estado da tartaruga, você deve usar
  "resizemode = auto".

* Se você definir, por exemplo, "language = italian", o docstringdict
  "turtle_docstringdict_italian.py" será carregado ao importar (se
  estiver presente no caminho de importação, por exemplo, no mesmo
  diretório que "turtle").

* As entradas *exampleturtle* e *examplescreen* definem os nomes
  desses objetos conforme ocorrem nas docstrings. A transformação de
  "método-docstrings" para "função-docstrings" excluirá esses nomes
  dos docstrings.

* *using_IDLE*: Defina isso como "True" se você trabalha regularmente
  com IDLE e sua chave "-n" ("sem subprocesso"). Isso impedirá que o
  "exitonclick()" entre no loop principal.

Pode haver um arquivo "turtle.cfg" no diretório em que o "turtle" está
armazenado e um arquivo adicional no diretório de trabalho atual. O
arquivo armazenado no diretório de trabalho atual tem preferência e
vai substituir as configurações do primeiro.

O diretório "Lib/turtledemo" contém um arquivo chamado "turtle.cfg".
Você pode usá-lo como um exemplo e ver seus efeitos ao executar as
demonstrações (de preferência, não utilize visualizador de
demonstrações).


Explicação
==========

Um objeto tartaruga é baseado em um objeto canvas, e há uma série de
classes principais na interface orientada a objetos da tartaruga que
podem ser usadas para criá-los e relacioná-los entre si.

Uma instância da classe "Turtle" cria automaticamente uma nova
instância de "Screen", caso esta não esteja presente.

"Turtle" é um subclasse de "RawTurtle", que *não* cria automaticamente
uma superfície de desenho - uma *tela* precisará ser fornecida ou
criada para ele. A *tela* pode ser uma "tkinter.Canvas",
"ScrolledCanvas" ou "TurtleScreen".

"TurtleScreen" é a superfície de desenho básica para uma tartaruga.
"Screen" é uma subclasse de "TurtleScreen" e inclui alguns métodos
adicionais para gerenciar sua aparência (incluindo tamanho e título) e
comportamento. O construtor "TurtleScreen" precisa de um
"tkinter.Canvas" ou um "ScrolledCanvas" como um argumento.

A interface funcional para gráficos de tartaruga usa os vários métodos
de "Turtle" e "TurtleScreen"/"Screen". Nos bastidores, um objeto de
tela é criado automaticamente sempre que um função derivada de um
método de "Screen" é chamado. Da mesma forma, um objeto de tartaruga é
criado automaticamente sempre que qualquer uma das funções derivadas
de um método de tartaruga é chamado.

Para usar várias tartarugas em uma tela, a interface orientada a
objetos deve ser usada.


"turtledemo" --- Scripts de Demonstração
========================================

O pacote "turtledemo" inclui um conjunto de scripts de demonstração.
Esses scripts podem ser executados e visualizados usando o
visualizador de demonstração fornecido da seguinte forma:

   python -m turtledemo

Como alternativa, você pode executar os scripts de demonstração
individualmente.  Por exemplo,

   python -m turtledemo.bytedesign

O diretório do pacote "turtledemo" contém:

* Um arquivo de exemplo "__main__.py" que pode ser usado para
  visualizar o código-fonte dos scripts e executá-los ao mesmo tempo.

* Vários scripts que demonstram diferentes recursos do módulo
  "turtle". Os exemplos podem ser acessados no menu Exemplos. Eles
  também podem ser executados de forma isolada.

* Um arquivo "turtle.cfg" que serve como exemplo de como escrever e
  usar esse tipo de arquivos.

Os scripts de demonstração são:

+--------------------------+--------------------------------+----------------------------------------+
| Nome                     | Descrição                      | Recursos                               |
|==========================|================================|========================================|
| "bytedesign"             | Padrão de gráficos de          | "tracer()", "delay()", "update()"      |
|                          | tartaruga clássico complexo    |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "chaos"                  | gráficos do modelo de          | coordenadas mundiais                   |
|                          | Verhulst, mostram que os       |                                        |
|                          | cálculos do computador podem   |                                        |
|                          | gerar resultados às vezes      |                                        |
|                          | contra as expectativas do bom  |                                        |
|                          | senso                          |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "clock"                  | Relógio analógico que mostra o | tartarugas como ponteiros de relógio,  |
|                          | horário do seu computador      | "ontimer()"                            |
+--------------------------+--------------------------------+----------------------------------------+
| "colormixer"             | experimento com r, g, b        | "ondrag()"                             |
+--------------------------+--------------------------------+----------------------------------------+
| "forest"                 | 3 breadth-first trees          | randomização                           |
+--------------------------+--------------------------------+----------------------------------------+
| "fractalcurves"          | Curvas de Hilbert & Koch       | recursão                               |
+--------------------------+--------------------------------+----------------------------------------+
| "lindenmayer"            | ethnomathematics (indian       | L-System                               |
|                          | kolams)                        |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "minimal_hanoi"          | Torres de Hanoi                | Tartarugas retângulos como discos de   |
|                          |                                | Hanói ("shape()", "shapesize()")       |
+--------------------------+--------------------------------+----------------------------------------+
| "nim"                    | jogue o clássico jogo nim com  | tartarugas como gravetos, acionadas    |
|                          | três montes de gravetos contra | por eventos (mouse, teclado)           |
|                          | o computador.                  |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "paint"                  | programa de desenho super      | "onclick()"                            |
|                          | minimalista                    |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "peace"                  | elementar                      | tartaruga: aparência e animação        |
+--------------------------+--------------------------------+----------------------------------------+
| "penrose"                | ladrilhos irregulares com      | "stamp()"                              |
|                          | pipas e dardos                 |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "planet_and_moon"        | simulação de um sistema        | formas compostas, "Vec2D"              |
|                          | gravitacional                  |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "rosette"                | um padrão do artigo Wikipédia  | "clone()", "undo()"                    |
|                          | sobre gráficos de tartaruga    |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "round_dance"            | tartarugas dançantes girando   | formas compostas, "clone()"            |
|                          | em pares na direção oposta     | "shapesize()", "tilt()",               |
|                          |                                | "get_shapepoly()", "update()"          |
+--------------------------+--------------------------------+----------------------------------------+
| "sorting_animate"        | demonstração visual de         | alinhamento simples, randomização      |
|                          | diferentes tipos de métodos de |                                        |
|                          | ordenação                      |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "tree"                   | uma árvore (gráfica) da        | "clone()"                              |
|                          | largura inicial (usando        |                                        |
|                          | geradores)                     |                                        |
+--------------------------+--------------------------------+----------------------------------------+
| "two_canvases"           | desenho simples                | tartarugas em duas telas               |
+--------------------------+--------------------------------+----------------------------------------+
| "yinyang"                | outro exemplo elementar        | "circle()"                             |
+--------------------------+--------------------------------+----------------------------------------+

Divirta-se!
