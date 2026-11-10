8. Erros e exceções
*******************

Até agora mensagens de erro foram apenas mencionadas, mas se você
testou os exemplos, talvez tenha esbarrado em algumas. Existem pelo
menos dois tipos distintos de erros: *erros de sintaxe* e *exceções*.


8.1. Erros de sintaxe
=====================

Erros de sintaxe, também conhecidos como erros de parse, são
provavelmente os mais frequentes entre aqueles que ainda estão
aprendendo Python:

   >>> while True print('Olá mundo')
     File "<stdin>", line 1
       while True print('Olá mundo')
                  ^^^^^
   SyntaxError: invalid syntax

O analisador sintático repete a linha ofensiva e exibe pequenas setas
apontando para o local onde o erro foi detectado. Note que esse nem
sempre é o local que precisa ser corrigido. No exemplo, o erro é
detectado na função "print()", já que dois pontos ("':'") estão
faltando logo antes dele.

O nome do arquivo ("<stdin>" no nosso exemplo) e o número da linha são
impressos para que você saiba onde procurar caso a entrada tenha vindo
de um arquivo.


8.2. Exceções
=============

Mesmo que um comando ou expressão estejam sintaticamente corretos,
talvez ocorra um erro na hora de sua execução. Erros detectados
durante a execução são chamados *exceções* e não são necessariamente
fatais: logo veremos como tratá-las em programas Python. A maioria das
exceções não são tratadas pelos programas e acabam resultando em
mensagens de erro:

   >>> 10 * (1/0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       10 * (1/0)
             ~^~
   ZeroDivisionError: division by zero
   >>> 4 + spam*3
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       4 + spam*3
           ^^^^
   NameError: name 'spam' is not defined
   >>> '2' + 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       '2' + 2
       ~~~~^~~
   TypeError: can only concatenate str (not "int") to str

A última linha da mensagem de erro indica o que aconteceu. Exceções
surgem com diferentes tipos, e o tipo é exibido como parte da
mensagem: os tipos no exemplo são "ZeroDivisionError", "NameError" e
"TypeError". A string exibida como sendo o tipo da exceção é o nome da
exceção embutida que ocorreu. Isso é verdade para todas exceções
pré-definidas em Python, mas não é necessariamente verdade para
exceções definidas pelo usuário (embora seja uma convenção útil). Os
nomes das exceções padrões são identificadores embutidos (não palavras
reservadas).

O resto da linha é um detalhamento que depende do tipo da exceção
ocorrida e sua causa.

A parte anterior da mensagem de erro apresenta o contexto onde ocorreu
a exceção. Essa informação é denominada *stack traceback* (situação da
pilha de execução). Em geral, contém uma lista de linhas do código-
fonte, sem apresentar, no entanto, linhas lidas da entrada padrão.

Exceções embutidas lista as exceções pré-definidas e seus
significados.


8.3. Tratamento de exceções
===========================

É possível escrever programas que tratam exceções específicas. Observe
o exemplo seguinte, que pede dados ao usuário até que um inteiro
válido seja fornecido, ainda permitindo que o programa seja
interrompido (utilizando "Control"-"C" ou seja lá o que o sistema
operacional suporte); note que uma interrupção gerada pelo usuário
será sinalizada pela exceção "KeyboardInterrupt".

   >>> while True:
   ...     try:
   ...         x = int(input("Insira um número: "))
   ...         break
   ...     except ValueError:
   ...         print("Ops! Esse não é um número válido. Tente novamente...")
   ...

A instrução "try" funciona da seguinte maneira:

* Primeiramente, a *cláusula try* (o conjunto de instruções entre as
  palavras reservadas "try" e "except" ) é executada.

* Se nenhuma exceção ocorrer, a *cláusula except* é ignorada e a
  execução da instrução "try" é finalizada.

* Se ocorrer uma exceção durante a execução de uma cláusula "try", as
  instruções remanescentes nela são ignoradas. Se o tipo da exceção
  ocorrida tiver sido previsto em algum "except", essa *cláusula
  except* é executada, e então depois a execução continua após o bloco
  try/except.

* Se a exceção levantada não corresponder a nenhuma exceção listada na
  *cláusula de exceção*, ela é encaminhada a uma instrução "try" mais
  externa. Se não houver nenhum tratador previsto para essa exceção,
  trata-se de uma *exceção não tratada* e a execução do programa
  termina com uma mensagem de erro.

A instrução "try" pode ter uma ou mais *cláusulas de exceção*, para
especificar múltiplos tratadores para diferentes exceções. No máximo
um único tratador será executado. Tratadores só são sensíveis às
exceções levantadas no interior da *cláusula de tentativa*, e não às
que tenham ocorrido no interior de outro tratador numa mesma instrução
"try". Uma *cláusula de exceção* pode ser sensível a múltiplas
exceções, por exemplo:

   ... except RuntimeError, TypeError, NameError:
   ...     pass

Uma classe em uma cláusula "except" corresponde a exceções que são
instâncias da própria classe ou de uma de suas classes derivadas (mas
o contrário não é válido --- uma *cláusula except* listando uma classe
derivada não corresponde a instâncias de suas classes base). Por
exemplo, o seguinte código irá mostrar B, C, D nessa ordem:

   class B(Exception):
       pass

   class C(B):
       pass

   class D(C):
       pass

   for cls in [B, C, D]:
       try:
           raise cls()
       except D:
           print("D")
       except C:
           print("C")
       except B:
           print("B")

Se a ordem das *cláusulas de exceção* fosse invertida ("except B" no
início), seria exibido B, B, B --- somente a primeira *cláusula de
exceção* compatível é ativada.

Quando uma exceção ocorre, ela pode estar associada a valores chamados
*argumentos* da exceção. A presença e os tipos dos argumentos dependem
do tipo da exceção.

A *cláusula except* pode especificar uma variável após o nome da
exceção. A variável está vinculada à instância de exceção que
normalmente possui um atributo "args" que armazena os argumentos. Por
conveniência, os tipos de exceção embutidos definem "__str__()" para
exibir todos os argumentos sem acessar explicitamente ".args".

   >>> try:
   ...     raise Exception('spam', 'ovos')
   ... except Exception as inst:
   ...     print(type(inst))    # o tipo da exceção
   ...     print(inst.args)     # argumentos armazenados em .args
   ...     print(inst)          # __str__ permite imprimir args diretamente,
   ...                          # mas pode ser substituído em subclasses de exceção
   ...     x, y = inst.args     # desempacota args
   ...     print('x =', x)
   ...     print('y =', y)
   ...
   <class 'Exception'>
   ('spam', 'ovos')
   ('spam', 'ovos')
   x = spam
   y = ovos

A saída "__str__()" da exceção é exibida como a última parte
("detalhe") da mensagem para exceções não tratadas.

"BaseException" é a classe base comum de todas as exceções. Uma de
suas subclasses, "Exception", é a classe base de todas as exceções não
fatais. Exceções que não são subclasses de "Exception" normalmente não
são tratadas, pois são usadas para indicar que o programa deve
terminar. Elas incluem "SystemExit", levantada por "sys.exit()", e
"KeyboardInterrupt", levantada quando um usuário deseja interromper o
programa.

"Exception" pode ser usada como um curinga que captura (quase) tudo.
No entanto, é uma boa prática ser o mais específico possível quanto
aos tipos de exceções que pretendemos manipular, evitando que
quaisquer exceções inesperadas se propaguem.

O padrão mais comum para lidar com "Exception" é imprimir ou registrar
a exceção e então levantá-la novamente (permitindo que um chamador
lide com a exceção também):

   import sys

   try:
       f = open('meuarquivo.txt')
       s = f.readline()
       i = int(s.strip())
   except OSError as err:
       print("Erro de E/S:", err)
   except ValueError:
       print("Não foi possível converter dados para um inteiro.")
   except Exception as err:
       print(f"Não esperava {err=}, {type(err)=}")
       raise

A construção "try" ... "except" possui uma *cláusula else* opcional
que, quando presente, deve ser colocada após todas as demais
cláusulas. É útil para um código que precisa ser executado se nenhuma
exceção foi levantada. Por exemplo:

   for arg in sys.argv[1:]:
       try:
           f = open(arg, 'r')
       except OSError:
           print('não foi possível abrir', arg)
       else:
           print(arg, 'tem', len(f.readlines()), 'linhas')
           f.close()

É melhor usar a cláusula "else" do que colocar código adicional na
cláusula "try", porque ela evita que, acidentalmente, seja tratada uma
exceção que não foi levantada pelo código protegido pela construção
com as instruções "try" ... "except".

Os manipuladores de exceção não tratam apenas exceções que ocorrem
imediatamente na *cláusula try*, mas também as que ocorrem dentro de
funções chamadas (mesmo indiretamente) na *cláusula try*. Por exemplo:

   >>> def this_fails():
   ...     x = 1/0
   ...
   >>> try:
   ...     isso_aqui_falha()
   ... except ZeroDivisionError as err:
   ...     print('Tratando o erro de tempo de execução:', err)
   ...
   Tratando o erro de tempo de execução: division by zero


8.4. Levantando exceções
========================

A instrução "raise" permite ao programador forçar a ocorrência de um
determinado tipo de exceção. Por exemplo:

   >>> raise NameError('Olá')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       raise NameError('Olá')
   NameError: Olá

O argumento de "raise" indica a exceção a ser levantada. Esse
argumento deve ser uma instância de exceção ou uma classe de exceção
(uma classe que deriva de "BaseException", tal como "Exception" ou uma
de suas subclasses). Se uma classe de exceção for passada, será
implicitamente instanciada invocando o seu construtor sem argumentos:

   raise ValueError  # abreviação para 'raise ValueError()'

Caso você precise determinar se uma exceção foi levantada ou não, mas
não quer manipular o erro, uma forma simples de instrução "raise"
permite que você levante-a novamente:

   >>> try:
   ...     raise NameError('Olá')
   ... except NameError:
   ...     print('Uma exceção passou por aqui!')
   ...     raise
   ...
   Uma exceção passou por aqui!
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise NameError('Olá')
   NameError: Olá


8.5. Encadeamento de exceções
=============================

Se uma exceção não tratada ocorrer dentro de uma seção "except", ela
terá a exceção sendo tratada anexada a ela e incluída na mensagem de
erro:

   >>> try:
   ...     open("database.sqlite")
   ... except OSError:
   ...     raise RuntimeError("unable to handle error")
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       open("database.sqlite")
       ~~~~^^^^^^^^^^^^^^^^^^^
   FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError("unable to handle error")
   RuntimeError: unable to handle error

Para indicar que uma exceção é uma consequência direta de outra, a
instrução "raise" permite uma cláusula opcional "from":

   # exc deve ser uma instância de exceção ou None.
   raise RuntimeError from exc

Isso pode ser útil quando você está transformando exceções. Por
exemplo:

   >>> def func():
   ...     raise ConnectionError
   ...
   >>> try:
   ...     func()
   ... except ConnectionError as exc:
   ...     raise RuntimeError('Failed to open database') from exc
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       func()
       ~~~~^^
     File "<stdin>", line 2, in func
   ConnectionError

   The above exception was the direct cause of the following exception:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError('Failed to open database') from exc
   RuntimeError: Failed to open database

Ele também permite desabilitar o encadeamento automático de exceções
usando o idioma "from None":

   >>> try:
   ...     open('bancodedados.sqlite')
   ... except OSError:
   ...     raise RuntimeError from None
   ...
   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError from None
   RuntimeError

Para mais informações sobre os mecanismos de encadeamento, veja
Exceções embutidas.


8.6. Exceções definidas pelo usuário
====================================

Programas podem definir novos tipos de exceções, através da criação de
uma nova classe (veja Classes para mais informações sobre classes
Python). Exceções devem ser derivadas da classe "Exception", direta ou
indiretamente.

As classes de exceção podem ser definidas para fazer qualquer coisa
que qualquer outra classe pode fazer, mas geralmente são mantidas
simples, geralmente oferecendo apenas um número de atributos que
permitem que informações sobre o erro sejam extraídas por
manipuladores para a exceção.

É comum que novas exceções sejam definidas com nomes terminando em
"Error", semelhante a muitas exceções embutidas.

Muitos módulos padrão definem suas próprias exceções para relatar
erros que podem ocorrer nas funções que definem.


8.7. Definindo ações de limpeza
===============================

A instrução "try" possui outra cláusula opcional, cuja finalidade é
permitir a implementação de ações de limpeza, que sempre devem ser
executadas independentemente da ocorrência de exceções. Como no
exemplo:

   >>> try:
   ...     raise KeyboardInterrupt
   ... finally:
   ...     print('Adeus, mundo!')
   ...
   Adeus, mundo!
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise KeyboardInterrupt
   KeyboardInterrupt

Se uma cláusula "finally" estiver presente, a cláusula "finally" será
executada como a última tarefa antes da conclusão da instrução "try".
A cláusula "finally" executa se a instrução "try" produz uma exceção.
Os pontos a seguir discutem casos mais complexos quando ocorre uma
exceção:

* Se ocorrer uma exceção durante a execução da cláusula "try", a
  exceção poderá ser tratada por uma cláusula "except". Se a exceção
  não for tratada por uma cláusula "except", a exceção será gerada
  novamente após a execução da cláusula "finally".

* Uma exceção pode ocorrer durante a execução de uma cláusula "except"
  ou "else". Novamente, a exceção é re-levantada depois que "finally"
  é executada.

* Se a cláusula "finally" executar uma instrução "break", "continue"
  ou "return", as exceções não serão levantadas novamente. Isso pode
  ser confuso e, portanto, não é recomendado. A partir da versão 3.14,
  o compilador emite um "SyntaxWarning" para isso (consulte **PEP
  765**).

* Se a instrução "try" atingir uma instrução "break", "continue" ou
  "return", a cláusula "finally" será executada imediatamente antes da
  execução da instrução "break", "continue" ou "return".

* Se uma cláusula "finally" incluir uma instrução "return", o valor
  retornado será aquele da instrução "return" da cláusula "finally",
  não o valor da instrução "return" da cláusula "try". A partir da
  versão 3.14, o compilador emite um "SyntaxWarning" para ela (veja
  **PEP 765**).

Por exemplo:

   >>> def retorna_booleano():
   ...     try:
   ...         return True
   ...     finally:
   ...         return False
   ...
   >>> retorna_booleano()
   False

Um exemplo mais complicado:

   >>> def divide(x, y):
   ...     try:
   ...         result = x / y
   ...     except ZeroDivisionError:
   ...         print("division by zero!")
   ...     else:
   ...         print("result is", result)
   ...     finally:
   ...         print("executing finally clause")
   ...
   >>> divide(2, 1)
   result is 2.0
   executing finally clause
   >>> divide(2, 0)
   division by zero!
   executing finally clause
   >>> divide("2", "1")
   executing finally clause
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       divide("2", "1")
       ~~~~~~^^^^^^^^^^
     File "<stdin>", line 3, in divide
       result = x / y
                ~~^~~
   TypeError: unsupported operand type(s) for /: 'str' and 'str'

Como você pode ver, a cláusula "finally" é executada em todos os
casos. A exceção "TypeError" levantada pela divisão de duas strings
não é tratada pela cláusula "except" e portanto é re-levantada depois
que a cláusula "finally" é executada.

Em aplicação do mundo real, a cláusula "finally" é útil para liberar
recursos externos (como arquivos ou conexões de rede),
independentemente do uso do recurso ter sido bem sucedido ou não.


8.8. Ações de limpeza predefinidas
==================================

Alguns objetos definem ações de limpeza padrões para serem executadas
quando o objeto não é mais necessário, independentemente da operação
que estava usando o objeto ter sido ou não bem sucedida. Veja o
exemplo a seguir, que tenta abrir um arquivo e exibir seu conteúdo na
tela.

   for linha in open("meuarquivo.txt"):
       print(linha, end="")

O problema com esse código é que ele deixa o arquivo aberto um período
indeterminado depois que o código é executado. Isso não chega a ser
problema em scripts simples, mas pode ser um problema para grandes
aplicações. A palavra reservada "with" permite que objetos como
arquivos sejam utilizados com a certeza de que sempre serão
prontamente e corretamente finalizados.

   with open("meuarquivo.txt") as f:
       for linha in f:
           print(linha, end="")

Depois que a instrução é executada, o arquivo *f* é sempre fechado,
mesmo se ocorrer um problema durante o processamento das linhas.
Outros objetos que, como arquivos, fornecem ações de limpeza
predefinidas as indicarão em suas documentações.


8.9. Criando e tratando várias exceções não relacionadas
========================================================

Existem situações em que é necessário relatar várias exceções que
ocorreram. Isso geralmente ocorre em estruturas de simultaneidade,
quando várias tarefas podem ter falhado em paralelo, mas também há
outros casos de uso em que é desejável continuar a execução e coletar
vários erros em vez de levantar a primeira exceção.

O "ExceptionGroup" integrado envolve uma lista de instâncias de
exceção para que elas possam ser levantadas juntas. É uma exceção em
si, portanto, pode ser capturada como qualquer outra exceção.

   >>> def f():
   ...     excs = [OSError('error 1'), SystemError('error 2')]
   ...     raise ExceptionGroup('houve problemas', excs)
   ...
   >>> f()
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 1, in <module>
     |     f()
     |     ~^^
     |   File "<stdin>", line 3, in f
     | ExceptionGroup: houve problemas (2 sub-exceptions)
     +-+---------------- 1 ----------------
       | OSError: error 1
       +---------------- 2 ----------------
       | SystemError: error 2
       +------------------------------------
   >>> try:
   ...     f()
   ... except Exception as e:
   ...     print(f'capturada {type(e)}: {e}')
   ...
   caught <class 'ExceptionGroup'>: houve problemas (2 sub-exceptions)
   >>>

Usando "except*" em vez de "except", podemos manipular seletivamente
apenas as exceções no grupo que correspondem a um determinado tipo. No
exemplo a seguir, que mostra um grupo de exceção aninhado, cada
cláusula "except*" extrai do grupo exceções de um certo tipo enquanto
permite que todas as outras exceções se propaguem para outras
cláusulas e eventualmente sejam levantadas novamente.

   >>> def f():
   ...     raise ExceptionGroup(
   ...         "group1",
   ...         [
   ...             OSError(1),
   ...             SystemError(2),
   ...             ExceptionGroup(
   ...                 "group2",
   ...                 [
   ...                     OSError(3),
   ...                     RecursionError(4)
   ...                 ]
   ...             )
   ...         ]
   ...     )
   ...
   >>> try:
   ...     f()
   ... except* OSError as e:
   ...     print("Houve OSErrors")
   ... except* SystemError as e:
   ...     print("Houve SystemErrors")
   ...
   Houve OSErrors
   Houve SystemErrors
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 2, in <module>
     |     f()
     |     ~^^
     |   File "<stdin>", line 2, in f
     |     raise ExceptionGroup(
     |     ...<12 lines>...
     |     )
     | ExceptionGroup: group1
     +-+---------------- 1 ----------------
       | ExceptionGroup: group2
       +-+---------------- 1 ----------------
         | RecursionError: 4
         +------------------------------------
   >>>

Observe que as exceções aninhadas em um grupo de exceções devem ser
instâncias, não tipos. Isso ocorre porque, na prática, as exceções
normalmente seriam aquelas que já foram levantadas e capturadas pelo
programa, seguindo o seguinte padrão:

   >>> excs = []
   >>> for test in tests:
   ...     try:
   ...         test.run()
   ...     except Exception as e:
   ...         excs.append(e)
   ...
   >>> if excs:
   ...    raise ExceptionGroup("Test Failures", excs)
   ...


8.10. Enriquecendo exceções com notas
=====================================

Quando uma exceção é criada para ser levantada, geralmente é
inicializada com informações que descrevem o erro ocorrido. Há casos
em que é útil adicionar informações após a captura da exceção. Para
este propósito, as exceções possuem um método "add_note(note)" que
aceita uma string e a adiciona à lista de notas da exceção. A
renderização de traceback padrão inclui todas as notas, na ordem em
que foram adicionadas, após a exceção.

   >>> try:
   ...     raise TypeError('tipo inválido')
   ... except Exception as e:
   ...     e.add_note('Adiciona algumas informações')
   ...     e.add_note('Adiciona mais algumas informações')
   ...     raise
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       raise TypeError('tipo inválido')
   TypeError: tipo inválido
   Adiciona algumas informações
   Adiciona mais algumas informações
   >>>

Por exemplo, ao coletar exceções em um grupo de exceções, podemos
querer adicionar informações de contexto para os erros individuais. A
seguir, cada exceção no grupo tem uma nota indicando quando esse erro
ocorreu.

   >>> def f():
   ...     raise OSError('operação falhou')
   ...
   >>> excs = []
   >>> for i in range(3):
   ...     try:
   ...         f()
   ...     except Exception as e:
   ...         e.add_note(f'Aconteceu na iteração {i+1}')
   ...         excs.append(e)
   ...
   >>> raise ExceptionGroup('Nós temos alguns problemas', excs)
     + Exception Group Traceback (most recent call last):
     |   File "<stdin>", line 1, in <module>
     |     raise ExceptionGroup('Nós temos alguns problemas', excs)
     | ExceptionGroup: Nós temos alguns problemas (3 sub-exceptions)
     +-+---------------- 1 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operação falhou')
       | OSError: operação falhou
       | Aconteceu na iteração 1
       +---------------- 2 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operação falhou')
       | OSError: operação falhou
       | Aconteceu na iteração 2
       +---------------- 3 ----------------
       | Traceback (most recent call last):
       |   File "<stdin>", line 3, in <module>
       |     f()
       |     ~^^
       |   File "<stdin>", line 2, in f
       |     raise OSError('operação falhou')
       | OSError: operação falhou
       | Aconteceu na iteração 3
       +------------------------------------
   >>>
