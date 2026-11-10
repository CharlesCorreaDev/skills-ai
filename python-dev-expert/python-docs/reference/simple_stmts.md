7. Instruções simples
*********************

Uma instrução simples consiste uma única linha lógica. Várias
instruções simples podem ocorrer em uma única linha separada por ponto
e vírgula. A sintaxe para instruções simples é:

   simple_stmt: expression_stmt
                | assert_stmt
                | assignment_stmt
                | augmented_assignment_stmt
                | annotated_assignment_stmt
                | pass_stmt
                | del_stmt
                | return_stmt
                | yield_stmt
                | raise_stmt
                | break_stmt
                | continue_stmt
                | import_stmt
                | future_stmt
                | global_stmt
                | nonlocal_stmt
                | type_stmt


7.1. Instruções de expressão
============================

As instruções de expressão são usadas (principalmente interativamente)
para calcular e escrever um valor, ou (geralmente) para chamar um
procedimento (uma função que não retorna nenhum resultado
significativo; em Python, os procedimentos retornam o valor "None").
Outros usos de instruções de expressão são permitidos e ocasionalmente
úteis. A sintaxe para uma instrução de expressão é:

   expression_stmt: starred_expression

Uma instrução de expressão avalia a lista de expressões (que pode ser
uma única expressão).

No modo interativo, se o valor não for "None", ele será convertido em
uma string usando a função embutida "repr()" e a string resultante
será gravada na saída padrão em uma linha sozinha (exceto se o
resultado é "None", de modo que as chamadas de procedimento não causam
nenhuma saída.)


7.2. Instruções de atribuição
=============================

As instruções de atribuição são usadas para (re)vincular nomes a
valores e modificar atributos ou itens de objetos mutáveis:

   assignment_stmt: (target_list "=")+ (starred_expression | yield_expression)
   target_list:     target ("," target)* [","]
   target:          identifier
                    | "(" [target_list] ")"
                    | "[" [target_list] "]"
                    | attributeref
                    | subscription
                    | "*" target

(See section Primárias for the syntax definitions for *attributeref*
and *subscription*.)

Uma instrução de atribuição avalia a lista de expressões (lembre-se de
que pode ser uma única expressão ou uma lista separada por vírgulas, a
última produzindo uma tupla) e atribui o único objeto resultante a
cada uma das listas alvos, da esquerda para a direita.

Assignment is defined recursively depending on the form of the target
(list). When a target is part of a mutable object (an attribute
reference or subscription), the mutable object must ultimately perform
the assignment and decide about its validity, and may raise an
exception if the assignment is unacceptable.  The rules observed by
various types and the exceptions raised are given with the definition
of the object types (see section A hierarquia de tipos padrão).

A atribuição de um objeto a uma lista alvo, opcionalmente entre
parênteses ou colchetes, é definida recursivamente da maneira a
seguir.

* Se a lista alvo contiver um único alvo sem vírgula à direita,
  opcionalmente entre parênteses, o objeto será atribuído a esse alvo.

* Senão:

  * Se a lista alvo contiver um alvo prefixado com um asterisco,
    chamado de alvo "com estrela" *(starred)*: o objeto deve ser um
    iterável com pelo menos tantos itens quantos os alvos na lista
    alvo, menos um. Os primeiros itens do iterável são atribuídos, da
    esquerda para a direita, aos alvos antes do alvo com estrela. Os
    itens finais do iterável são atribuídos aos alvos após o alvo com
    estrela. Uma lista dos itens restantes no iterável é então
    atribuída ao alvo com estrela (a lista pode estar vazia).

  * Senão: o objeto deve ser um iterável com o mesmo número de itens
    que existem alvos na lista alvos, e os itens são atribuídos, da
    esquerda para a direita, aos alvos correspondentes.

A atribuição de um objeto a um único alvo é definida recursivamente da
maneira a seguir.

* Se o alvo for um identificador (nome):

  * Se o nome não ocorrer em uma instrução "global" ou "nonlocal" no
    bloco de código atual: o nome está vinculado ao objeto no espaço
    de nomes local atual.

  * Caso contrário: o nome é vinculado ao objeto no espaço de nomes
    global global ou no espaço de nomes global externo determinado por
    "nonlocal", respectivamente.

  O nome é vinculado novamente se já estiver vinculado. Isso pode
  fazer com que a contagem de referências para o objeto anteriormente
  vinculado ao nome chegue a zero, fazendo com que o objeto seja
  desalocado e seu destrutor (se houver) seja chamado.

* Se o alvo for uma referência de atributo: a expressão primária na
  referência é avaliada. Deve produzir um objeto com atributos
  atribuíveis; se este não for o caso, a exceção "TypeError" é
  levanta. Esse objeto é então solicitado a atribuir o objeto
  atribuído ao atributo fornecido; se não puder executar a atribuição,
  ele levanta uma exceção (geralmente, mas não necessariamente
  "AttributeError").

  Nota: Se o objeto for uma instância de classe e a referência de
  atributo ocorrer em ambos os lados do operador de atribuição, a
  expressão do lado direito, "a.x" pode acessar um atributo de
  instância ou (se não existir nenhum atributo de instância) uma
  classe atributo. O alvo do lado esquerdo "a.x" é sempre definido
  como um atributo de instância, criando-o se necessário. Assim, as
  duas ocorrências de "a.x" não necessariamente se referem ao mesmo
  atributo: se a expressão do lado direito se refere a um atributo de
  classe, o lado esquerdo cria um novo atributo de instância como alvo
  da atribuição:

     class Cls:
         x = 3             # variável de classe
     inst = Cls()
     inst.x = inst.x + 1   # escreve inst.x como 4 deixando Cls.x como 3

  This description does not necessarily apply to descriptor
  attributes, such as properties created with "@property".

* If the target is a subscription: The primary expression in the
  reference is evaluated. Next, the subscript expression is evaluated.
  Then, the primary's "__setitem__()" method is called with two
  arguments: the subscript and the assigned object.

  Typically, "__setitem__()" is defined on mutable sequence objects
  (such as lists) and mapping objects (such as dictionaries), and
  behaves as follows.

  Se o primário for um objeto de sequência mutável (como uma lista), o
  subscrito deverá produzir um inteiro. Se for negativo, o comprimento
  da sequência é adicionado a ela. O valor resultante deve ser um
  inteiro não negativo menor que o comprimento da sequência, e a
  sequência é solicitada a atribuir o objeto atribuído ao seu item com
  esse índice. Se o índice estiver fora do intervalo, a exceção
  "IndexError" será levantada (a atribuição a uma sequência subscrita
  não pode adicionar novos itens a uma lista).

  Se o primário for um objeto de mapeamento (como um dicionário), o
  subscrito deve ter um tipo compatível com o tipo de chave do
  mapeamento, e o mapeamento é solicitado a criar um par chave/valore
  que mapeia o subscrito para o objeto atribuído. Isso pode substituir
  um par de chave/valor existente pelo mesmo valor de chave ou inserir
  um novo par de chave/valor (se não existir nenhuma chave com o mesmo
  valor).

  If the target is a slicing: The primary expression should evaluate
  to a mutable sequence object (such as a list). The assigned object
  should be *iterable*. The slicing's lower and upper bounds should be
  integers; if they are "None" (or not present), the defaults are zero
  and the sequence's length. If either bound is negative, the
  sequence's length is added to it.  The resulting bounds are clipped
  to lie between zero and the sequence's length, inclusive.  Finally,
  the sequence object is asked to replace the slice with the items of
  the assigned sequence.  The length of the slice may be different
  from the length of the assigned sequence, thus changing the length
  of the target sequence, if the target sequence allows it.

Embora a definição de atribuição implique que as sobreposições entre o
lado esquerdo e o lado direito sejam "simultâneas" (por exemplo, "a, b
= b, a" troca duas variáveis), sobreposições *dentro* da coleção de
variáveis atribuídas ocorrem da esquerda para a direita, às vezes
resultando em confusão. Por exemplo, o programa a seguir imprime "[0,
2]":

   x = [0, 1]
   i = 0
   i, x[i] = 1, 2         # i é atualizado e, em seguida, x[i] é atualizado
   print(x)

Ver também:

  **PEP 3132** - Desempacotamento estendido de iterável
     A especificação para o recurso "*target".


7.2.1. Instruções de atribuição aumentada
-----------------------------------------

A atribuição aumentada é a combinação, em uma única instrução, de uma
operação binária e uma instrução de atribuição:

   augmented_assignment_stmt: augtarget augop (expression_list | yield_expression)
   augtarget:                 identifier | attributeref | subscription
   augop:                     "+=" | "-=" | "*=" | "@=" | "/=" | "//=" | "%=" | "**="
                              | ">>=" | "<<=" | "&=" | "^=" | "|="

(Veja a seção Primárias para as definições de sintaxe dos últimos três
símbolos.)

Uma atribuição aumentada avalia o alvo (que, diferentemente das
instruções de atribuição normais, não pode ser um desempacotamento) e
a lista de expressões, executa a operação binária específica para o
tipo de atribuição nos dois operandos e atribui o resultado ao alvo
original. O alvo é avaliado apenas uma vez.

Uma instrução de atribuição aumentada como "x += 1" pode ser reescrita
como "x = x + 1" para obter um efeito semelhante, mas não exatamente
igual. Na versão aumentada, "x" é avaliado apenas uma vez. Além disso,
quando possível, a operação real é executada *no local*, o que
significa que, em vez de criar um novo objeto e atribuí-lo ao alvo, o
objeto antigo é modificado.

Ao contrário das atribuições normais, as atribuições aumentadas
avaliam o lado esquerdo *antes* de avaliar o lado direito. Por
exemplo, "a[i] += f(x)" primeiro procura "a[i]", então avalia "f(x)" e
executa a adição e, por último, escreve o resultado de volta para
"a[i]".

Com exceção da atribuição a tuplas e vários alvos em uma única
instrução, a atribuição feita por instruções de atribuição aumentada é
tratada da mesma maneira que atribuições normais. Da mesma forma, com
exceção do possível comportamento *in-place*, a operação binária
executada por atribuição aumentada é a mesma que as operações binárias
normais.

Para alvos que são referências de atributos, a mesma advertência sobre
atributos de classe e instância se aplica a atribuições regulares.


7.2.2. instruções de atribuição anotado
---------------------------------------

A atribuição de *anotação* é a combinação, em uma única instrução, de
uma anotação de variável ou atributo e uma instrução de atribuição
opcional:

   annotated_assignment_stmt: augtarget ":" expression
                              ["=" (starred_expression | yield_expression)]

A diferença para as Instruções de atribuição normal é que apenas um
único alvo é permitido.

O alvo da atribuição é considerado "simples" se consistir em um único
nome que não esteja entre parênteses. Para alvos de atribuição
simples, se estiverem no escopo de classe ou módulo, as anotações são
reunidas em um escopo de anotação avaliado preguiçosamente. As
anotações podem ser avaliadas usando o atributo "__annotations__" de
uma classe ou módulo, ou usando os recursos do módulo "annotationlib".

Se o alvo da atribuição não for simples (um atributo, nó subscrito ou
nome entre parênteses), a anotação nunca será avaliada.

Se um nome for anotado em um escopo de função, esse nome será local
para esse escopo. As anotações nunca são avaliadas e armazenadas em
escopos de função.

Se o lado direito estiver presente, uma atribuição anotada executa a
atribuição real como se não houvesse uma anotação presente. Se o lado
direito não estiver presente para um alvo de expressão, então o
interpretador avalia o alvo, exceto para a última chamada
"__setitem__()" ou "__setattr__()".

Ver também:

  **PEP 526** - Sintaxe para Anotações de Variáveis
     A proposta que adicionou sintaxe para anotar os tipos de
     variáveis (incluindo variáveis de classe e variáveis de
     instância), em vez de expressá-las por meio de comentários.

  **PEP 484** - Dicas de tipo
     A proposta que adicionou o módulo "typing" para fornecer uma
     sintaxe padrão para anotações de tipo que podem ser usadas em
     ferramentas de análise estática e IDEs.

Alterado na versão 3.8: Agora, as atribuições anotadas permitem as
mesmas expressões no lado direito que as atribuições regulares.
Anteriormente, algumas expressões (como expressões de tupla sem
parênteses) causavam um erro de sintaxe.

Alterado na versão 3.14: As anotações agora têm avaliação preguiçosa
em um escopo de anotação separado. Se o alvo da atribuição não for
simples, as anotações nunca serão avaliadas.


7.3. A instrução "assert"
=========================

As instruções assert são uma maneira conveniente de inserir asserções
de depuração em um programa:

   assert_stmt: "assert" expression ["," expression]

A forma simples, "assert expression", é equivalente a

   if __debug__:
       if not expression: raise AssertionError

A forma estendida, "assert expression1, expression2", é equivalente a

   if __debug__:
       if not expression1: raise AssertionError(expression2)

Essas equivalências presumem que "__debug__" e "AssertionError"
referem-se às variáveis embutidas com esses nomes. Na implementação
atual, a variável embutida "__debug__" é "True" em circunstâncias
normais, "False" quando a otimização é solicitada (opção de linha de
comando "-O"). O gerador de código atual não emite código para uma
instrução "assert" quando a otimização é solicitada em tempo de
compilação. Observe que não é necessário incluir o código-fonte da
expressão que falhou na mensagem de erro; ele será exibido como parte
do stack trace (situação da pilha de execução).

Atribuições a "__debug__" são ilegais. O valor da variável embutida é
determinado quando o interpretador é iniciado.


7.4. A instrução "pass"
=======================

   pass_stmt: "pass"

"pass" é uma operação nula --- quando é executada, nada acontece. É
útil como um espaço reservado quando uma instrução é necessária
sintaticamente, mas nenhum código precisa ser executado, por exemplo:

   def f(arg): pass    # uma função que faz nada (ainda)

   class C: pass       # uma classe com nenhum método (ainda)


7.5. A instrução "del"
======================

   del_stmt: "del" target_list

A exclusão é definida recursivamente de maneira muito semelhante à
maneira como a atribuição é definida. Em vez de explicar em detalhes,
aqui estão algumas dicas.

A exclusão de uma lista alvo exclui recursivamente cada alvo, da
esquerda para a direita.

A exclusão de um nome remove a ligação desse nome do espaço de nomes
local ou global, dependendo se o nome ocorre em uma instrução "global"
no mesmo bloco de código. Tentar excluir um nome  desvinculado levanta
uma exceção "NameError".

Deletion of attribute references and subscriptions is passed to the
primary object involved; deletion of a slicing is in general
equivalent to assignment of an empty slice of the right type (but even
this is determined by the sliced object).

Alterado na versão 3.2: Anteriormente, era ilegal excluir um nome do
espaço de nomes local se ele ocorresse como uma variável livre em um
bloco aninhado.


7.6. A instrução "return"
=========================

   return_stmt: "return" [expression_list]

"return" só pode ocorrer sintaticamente aninhado em uma definição de
função, não em uma definição de classe aninhada.

Se uma lista de expressões estiver presente, ela será avaliada, caso
contrário, será usado o valor "None".

"return" deixa a chamada da função atual com a lista de expressões (ou
"None") como valor de retorno.

Quando "return" passa o controle de uma instrução "try" com uma
cláusula "finally", essa cláusula "finally" é executada antes de
realmente sair da função.

Em uma função geradora, a instrução "return" indica que o gerador está
pronto e fará com que uma exceção "StopIteration" seja levantada. O
valor retornado (se houver) é usado como argumento para construir
"StopIteration" e se torna o atributo "StopIteration.value".

Em uma função de gerador assíncrono, uma instrução "return" vazia
indica que o gerador assíncrono está pronto e fará com que uma exceção
"StopAsyncIteration" seja levantada. Uma instrução "return" não vazia
é um erro de sintaxe em uma função de gerador assíncrono.


7.7. A instrução "yield"
========================

   yield_stmt: yield_expression

Uma instrução "yield" é semanticamente equivalente a uma expressão
yield. A instrução "yield" pode ser usada para omitir os parênteses
que, de outra forma, seriam necessários na instrução de expressão
yield equivalente. Por exemplo, as instruções yield

   yield <expr>
   yield from <expr>

são equivalentes às instruções de expressão yield

   (yield <expr>)
   (yield from <expr>)

Expressões e instruções yield são usadas apenas ao definir uma função
*geradora* e são usadas apenas no corpo da função geradora. Usar
"yield" em uma definição de função é suficiente para fazer com que
essa definição crie uma função geradora em vez de uma função normal.

Para detalhes completos da semântica "yield", consulte a seção
Expressões yield.


7.8. A instrução "raise"
========================

   raise_stmt: "raise" [expression ["from" expression]]

Se nenhuma expressão estiver presente, "raise" reativa a exceção em
tratamento no momento, também conhecida como *exceção ativa*. Se não
houver uma exceção ativa no momento, uma exceção "RuntimeError" é
levantada indicando que isso é um erro.

Caso contrário, "raise" avalia a primeira expressão como o objeto de
exceção. Deve ser uma subclasse ou uma instância de "BaseException".
Se for uma classe, a instância de exceção será obtida quando
necessário, instanciando a classe sem argumentos.

O *tipo* da exceção é a classe da instância de exceção, o *valor* é a
própria instância.

Um objeto traceback (situação da pilha de execução) normalmente é
criado automaticamente quando uma exceção é levantada e anexada a ele
como o atributo "__traceback__". Você pode criar uma exceção e definir
seu próprio traceback em uma etapa usando o método de exceção
"with_traceback()" (que retorna a mesma instância de exceção, com seu
traceback definido para seu argumento), assim:

   raise Exception("ocorreu foo").with_traceback(tracebackobj)

A cláusula "from" é usada para encadeamento de exceções: se fornecida,
a segunda expressão, *expression*, deve ser outra classe ou instância
de exceção. Se a segunda expressão for uma instância de exceção, ela
será anexada à exceção levantada como o atributo "__cause__" (que é
gravável). Se a expressão for uma classe de exceção, a classe será
instanciada e a instância resultante será anexada à exceção levantada
como o atributo "__cause__". Se a exceção levantada não for tratada,
ambas as exceções serão impressas:

   >>> try:
   ...     print(1 / 0)
   ... except Exception as exc:
   ...     raise RuntimeError("Something bad happened") from exc
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       print(1 / 0)
             ~~^~~
   ZeroDivisionError: division by zero

   The above exception was the direct cause of the following exception:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError("Something bad happened") from exc
   RuntimeError: Something bad happened

Um mecanismo semelhante funciona implicitamente quando uma nova
exceção for levantada enquanto outra já estiver sendo tratada. Uma
exceção pode ser tratada quando uma cláusula "except" ou "finally", ou
uma instrução "with", é usada. A exceção anterior é então anexada como
o atributo "__context__" da nova exceção:

   >>> try:
   ...     print(1 / 0)
   ... except:
   ...     raise RuntimeError("Something bad happened")
   ...
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
       print(1 / 0)
             ~~^~~
   ZeroDivisionError: division by zero

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
       raise RuntimeError("Something bad happened")
   RuntimeError: Something bad happened

O encadeamento de exceção pode ser explicitamente suprimido
especificando "None" na cláusula "from":

   >>> try:
   ...     print(1 / 0)
   ... except:
   ...     raise RuntimeError("Something bad happened") from None
   ...
   Traceback (most recent call last):
     File "<stdin>", line 4, in <module>
   RuntimeError: Something bad happened

Informações adicionais sobre exceções podem ser encontradas na seção
Exceções, e informações sobre como lidar com exceções estão na seção A
instrução try.

Alterado na versão 3.3: "None" agora é permitido como "Y" em "raise X
from Y".Adicionado o atributo "__suppress_context__" para suprimir a
exibição automática do contexto de exceção.

Alterado na versão 3.11: Se o traceback da exceção ativa for
modificado em uma cláusula "except", uma instrução "raise" subsequente
levantará novamente a exceção com o traceback modificado.
Anteriormente, a exceção era levantada novamente com o traceback que
tinha quando foi capturada.


7.9. A instrução "break"
========================

   break_stmt: "break"

"break" só pode ocorrer sintaticamente aninhado em um laço "for" ou
"while", mas não aninhado em uma função ou definição de classe dentro
desse laço.

Ele termina o laço de repetição mais próximo, pulando a cláusula
opcional "else" se o laço tiver uma.

Se um laço "for" é encerrado por "break", o alvo de controle do laço
mantém seu valor atual.

Quando "break" passa o controle de uma instrução "try" com uma
cláusula "finally", essa cláusula "finally" é executada antes de
realmente sair do laço.


7.10. A instrução "continue"
============================

   continue_stmt: "continue"

"continue" só pode ocorrer sintaticamente aninhado em um laço "for" ou
"while", mas não em uma função ou definição de classe dentro desse
laço. Ele continua com o próximo ciclo do laço de repetição mais
próximo.

Quando "continue" passa o controle de uma instrução "try" com uma
cláusula "finally", essa cláusula "finally" é executada antes de
realmente iniciar o próximo ciclo do laço.


7.11. A instrução "import"
==========================

   import_stmt:     ["lazy"] "import" module ["as" identifier] ("," module ["as" identifier])*
                    | ["lazy"] "from" relative_module "import" identifier ["as" identifier]
                    ("," identifier ["as" identifier])*
                    | ["lazy"] "from" relative_module "import" "(" identifier ["as" identifier]
                    ("," identifier ["as" identifier])* [","] ")"
                    | "from" relative_module "import" "*"
   module:          (identifier ".")* identifier
   relative_module: "."* module | "."+

A instrução de importação básica (sem cláusula "from") é executada em
duas etapas:

1. encontra um módulo, carregando e inicializando-o se necessário

2. define a name or names in the current namespace for the scope where
   the "import" statement occurs, just as an assignment statement
   would (including "global" and "nonlocal" semantics).

Quando a instrução contém várias cláusulas (separadas por vírgulas),
as duas etapas são executadas separadamente para cada cláusula, como
se as cláusulas tivessem sido separadas em instruções de importação
individuais.

Os detalhes da primeira etapa, encontrar e carregar módulos, estão
descritos com mais detalhes na seção sobre o sistema de importação,
que também descreve os vários tipos de pacotes e módulos que podem ser
importados, bem como todos os os ganchos que podem ser usados para
personalizar o sistema de importação. Observe que falhas nesta etapa
podem indicar que o módulo não pôde ser localizado *ou* que ocorreu um
erro durante a inicialização do módulo, o que inclui a execução do
código do módulo.

Se o módulo solicitado for recuperado com sucesso, ele será
disponibilizado no espaço de nomes local de três maneiras:

* Se o nome do módulo é seguido pela palavra reservada "as", o nome a
  seguir é vinculado diretamente ao módulo importado.

* Se nenhum outro nome for especificado e o módulo que está sendo
  importado for um módulo de nível superior, o nome do módulo será
  vinculado ao espaço de nomes local como uma referência ao módulo
  importado

* Se o módulo que está sendo importado *não* for um módulo de nível
  superior, o nome do pacote de nível superior que contém o módulo
  será vinculado ao espaço de nomes local como uma referência ao
  pacote de nível superior. O módulo importado deve ser acessado
  usando seu nome completo e não diretamente

O formulário "from" usa um processo um pouco mais complexo:

1. encontra o módulo especificado na cláusula "from", carregando e
   inicializando-o se necessário;

2. para cada um dos identificadores especificados nas cláusulas
   "import":

   1. verifica se o módulo importado tem um atributo com esse nome

   2. caso contrário, tenta importar um submódulo com esse nome e
      verifica o módulo importado novamente para esse atributo

   3. se o atributo não for encontrado, a exceção "ImportError" é
      levantada.

   4. otherwise, a reference to that value is stored in the current
      namespace, using the name in the "as" clause if it is present,
      otherwise using the attribute name

Exemplos:

   import foo                 # foo importado e vinculado localmente
   import foo.bar.baz         # foo, foo.bar e foo.bar.baz importados, foo vinculado localmente
   import foo.bar.baz as fbb  # foo, foo.bar e foo.bar.baz importados, foo.bar.baz vinculado como fbb
   from foo.bar import baz    # foo, foo.bar e foo.bar.baz importados, foo.bar.baz vinculado como baz
   from foo import attr       # foo importado e foo.attr vinculado como attr

Se a lista de identificadores for substituída por uma estrela ("'*'"),
todos os nomes públicos definidos no módulo serão vinculados ao espaço
de nomes local para o escopo onde ocorre a instrução "import".

The *public names* defined by a module are determined by checking the
module's namespace for a variable named "__all__"; if defined, it must
be a sequence of strings which are names defined or imported by that
module. Names containing non-ASCII characters must be in the
normalization form NFKC; see Caracteres não ASCII em nomes for
details.  The names given in "__all__" are all considered public and
are required to exist.  If "__all__" is not defined, the set of public
names includes all names found in the module's namespace which do not
begin with an underscore character ("'_'").  "__all__" should contain
the entire public API. It is intended to avoid accidentally exporting
items that are not part of the API (such as library modules which were
imported and used within the module).

A forma curinga de importação --- "from module import *" --- só é
permitida no nível do módulo. Tentar usá-lo em definições de classe ou
função irá levantar uma "SyntaxError".

Ao especificar qual módulo importar, você não precisa especificar o
nome absoluto do módulo. Quando um módulo ou pacote está contido em
outro pacote, é possível fazer uma importação relativa dentro do mesmo
pacote superior sem precisar mencionar o nome do pacote. Usando pontos
iniciais no módulo ou pacote especificado após "from" você pode
especificar quão alto percorrer a hierarquia de pacotes atual sem
especificar nomes exatos. Um ponto inicial significa o pacote atual
onde o módulo que faz a importação existe. Dois pontos significam um
nível de pacote acima. Três pontos são dois níveis acima, etc. Então,
se você executar "from . import mod" de um módulo no pacote "pkg"
então você acabará importando o "pkg.mod". Se você executar "from
..subpkg2 import mod" de dentro de "pkg.subpkg1" você irá importar
"pkg.subpkg2.mod". A especificação para importações relativas está
contida na seção Importações relativas ao pacote.

"importlib.import_module()" é fornecida para dar suporte a aplicações
que determinam dinamicamente os módulos a serem carregados.

Levanta um evento de auditoria "import" com os argumentos "module",
"filename", "sys.path", "sys.meta_path", "sys.path_hooks".


7.11.1. Lazy imports
--------------------

The "lazy" keyword is a soft keyword that only has special meaning
when it appears immediately before an "import" or "from" statement.
When an import statement is preceded by the "lazy" keyword, the import
becomes *lazy*: the module is not loaded immediately at the import
statement. Instead, a lazy proxy object is created and bound to the
name. The actual module is loaded on first use of that name.

Lazy imports are only permitted at module scope. Using "lazy" inside a
function, class body, or "try"/"except"/"finally" block raises a
"SyntaxError". Star imports cannot be lazy ("lazy from module import
*" is a syntax error), and future statements cannot be lazy.

When using "lazy from ... import", each imported name is bound to a
lazy proxy object. The first access to any of these names triggers
loading of the entire module and resolves only that specific name to
its actual value. Other names remain as lazy proxies until they are
accessed.

Exemplo:

   lazy import json
   import sys

   print('json' in sys.modules)  # False - json module not yet loaded

   # First use triggers loading
   result = json.dumps({"hello": "world"})

   print('json' in sys.modules)  # True - now loaded

If an error occurs during module loading (such as "ImportError" or
"SyntaxError"), it is raised at the point where the lazy import is
first used, not at the import statement itself.

See **PEP 810** for the full specification of lazy imports.

Adicionado na versão 3.15.


7.11.1.1. Compatibility via "__lazy_modules__"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an alternative to using the "lazy" keyword, a module can opt into
lazy loading for specific imports by defining a module-level
"__lazy_modules__" variable.  When present, it must be a container of
fully qualified module name strings.  Any regular (non-"lazy")
"import" statement at module scope whose target appears in
"__lazy_modules__" is treated as a lazy import, exactly as if the
"lazy" keyword had been used.

This provides a way to enable lazy loading for specific dependencies
without changing individual "import" statements. This is useful when
supporting Python versions older than 3.15 while using lazy imports in
3.15+:

   __lazy_modules__ = ["json", "pathlib"]

   import json     # loaded lazily (name is in __lazy_modules__)
   import os       # loaded eagerly (name not in __lazy_modules__)

   import pathlib  # loaded lazily

Relative imports are resolved to their absolute name before the
lookup, so "__lazy_modules__" must always contain fully qualified
module names.

For "from"-style imports, the relevant name is the module following
"from", not the names of its members:

   # In mypackage/mymodule.py
   __lazy_modules__ = ["mypackage", "mypackage.sub.utils"]

   from . import helper         # loaded lazily: . resolves to mypackage
   from .sub.utils import func  # loaded lazily: .sub.utils resolves to mypackage.sub.utils
   import json                  # loaded eagerly (not in __lazy_modules__)

Imports inside functions, class bodies, or "try"/"except"/"finally"
blocks are always eager, regardless of "__lazy_modules__".

Adicionado na versão 3.15.


7.11.2. Instruções future
-------------------------

Uma *instrução future* é uma diretiva para o compilador de que um
determinado módulo deve ser compilado usando sintaxe ou semântica que
estará disponível em uma versão futura especificada do Python, onde o
recurso se tornará padrão.

A instrução future destina-se a facilitar a migração para versões
futuras do Python que introduzem alterações incompatíveis na
linguagem. Ele permite o uso dos novos recursos por módulo antes do
lançamento em que o recurso se torna padrão.

   future_stmt: "from" "__future__" "import" feature ["as" identifier]
                ("," feature ["as" identifier])*
                | "from" "__future__" "import" "(" feature ["as" identifier]
                ("," feature ["as" identifier])* [","] ")"
   feature:     identifier

Uma instrução future deve aparecer perto do topo do módulo. As únicas
linhas que podem aparecer antes de uma instrução future são:

* o módulo docstring (se houver),

* comentários,

* linhas vazias e

* outras instruções future.

O único recurso que requer o uso da instrução future é "annotations"
(veja **PEP 563**).

Todos os recursos históricos habilitados pela instrução future ainda
são reconhecidos pelo Python 3. A lista inclui "absolute_import",
"division", "generators", "generator_stop", "unicode_literals",
"print_function", "nested_scopes" e "with_statement". Eles são todos
redundantes porque estão sempre habilitados e mantidos apenas para
compatibilidade com versões anteriores.

Uma instrução future é reconhecida e tratada especialmente em tempo de
compilação: as alterações na semântica das construções principais são
frequentemente implementadas gerando código diferente. Pode até ser o
caso de um novo recurso introduzir uma nova sintaxe incompatível (como
uma nova palavra reservada), caso em que o compilador pode precisar
analisar o módulo de maneira diferente. Tais decisões não podem ser
adiadas até o tempo de execução.

Para qualquer versão, o compilador sabe quais nomes de recursos foram
definidos e levanta um erro em tempo de compilação se uma instrução
future contiver um recurso desconhecido.

A semântica do tempo de execução direto é a mesma de qualquer
instrução de importação: existe um módulo padrão "__future__",
descrito posteriormente, e será importado da maneira usual no momento
em que a instrução future for executada.

A semântica interessante do tempo de execução depende do recurso
específico ativado pela instrução future.

Observe que não há nada de especial sobre a instrução:

   import __future__ [as name]

Essa não é uma instrução future; é uma instrução de importação comum
sem nenhuma semântica especial ou restrições de sintaxe.

O código compilado por chamadas para as funções embutidas "exec()" e
"compile()" que ocorrem em um módulo "M" contendo uma instrução future
usará, por padrão, a nova sintaxe ou semântica associada com a
instrução future. Isso pode ser controlado por argumentos opcionais
para "compile()" -- veja a documentação dessa função para detalhes.

Uma instrução future tipada digitada em um prompt do interpretador
interativo terá efeito no restante da sessão do interpretador. Se um
interpretador for iniciado com a opção "-i", for passado um nome de
script para ser executado e o script incluir uma instrução future, ela
entrará em vigor na sessão interativa iniciada após a execução do
script.

Ver também:

  **PEP 236** - De volta ao __future__
     A proposta original para o mecanismo do __future__.


7.12. A instrução "global"
==========================

   global_stmt: "global" identifier ("," identifier)*

A instrução "global" faz com que os identificadores listados a serem
interpretados como globais. Seria impossível atribuir a uma variável
global sem "global", embora variáveis livres possam se referir a
globais sem serem declaradas globais.

A instrução "global" se aplica a todo o escopo atual (módulo, corpo da
função ou definição de classe). Uma exceção "SyntaxError" é levantada
se uma variável for usada ou atribuída antes de sua declaração global
no escopo.

No nível do módulo, todas as variáveis são globais, portanto, uma
instrução "global" não tem efeito. No entanto, as variáveis ainda não
devem ser usadas ou atribuídas antes de sua declaração "global". Este
requisito é flexibilizado no prompt interativo (*REPL*).

**Nota do programador:** "global" é uma diretiva para o analisador
sintático. Aplica-se apenas ao código analisado ao mesmo tempo que a
instrução "global". Em particular, uma instrução "global" contida em
uma string ou objeto código fornecido à função embutida "exec()" não
afeta o bloco de código *contendo* a chamada da função e o código
contido em tal uma string não é afetada por instruções "global" no
código que contém a chamada da função. O mesmo se aplica às funções
"eval()" e "compile()".


7.13. A instrução "nonlocal"
============================

   nonlocal_stmt: "nonlocal" identifier ("," identifier)*

Quando a definição de uma função ou classe está aninhada (incluída)
nas definições de outras funções, seus escopos não locais são os
escopos locais das funções envolventes. A instrução "nonlocal" faz com
que os identificadores listados se refiram a nomes previamente
vinculados a escopos não locais. Ele permite que o código encapsulado
religue esses identificadores não locais. Se um nome estiver ligado a
mais de um escopo não local, a ligação mais próxima será usada. Se um
nome não estiver vinculado a nenhum escopo não local, ou se não houver
escopo não local, uma exceção "SyntaxError" será levantada.

A instrução "nonlocal" se aplica a todo o escopo de uma função ou
corpo da classe. Uma exceção "SyntaxError" é levantada se uma variável
for usada ou atribuída antes de sua declaração nonlocal no escopo.

Ver também:

  **PEP 3104** - Acesso a nomes em escopos externos
     A especificação para a instrução "nonlocal".

**Nota do programador:** "nonlocal" é uma diretiva para o analisador
sintático e se aplica apenas ao código analisado junto com ele. Veja a
nota para a instrução "global".


7.14. A instrução "type"
========================

   type_stmt: 'type' identifier [type_params] "=" expression

A instrução "type" declara um apelido de tipo, que é uma instância de
"typing.TypeAliasType".

Por exemplo, a instrução a seguir cria um apelido de tipo:

   type Point = tuple[float, float]

Este código é aproximadamente equivalente a:

   annotation-def VALUE_OF_Point():
       return tuple[float, float]
   Point = typing.TypeAliasType("Point", VALUE_OF_Point())

"annotation-def" indica um escopo de anotação, que se comporta
principalmente como uma função, mas com diversas pequenas diferenças.

O valor do apelido de tipo é avaliado no escopo de anotação. Ele não é
avaliado quando o apelido de tipo é criado, mas somente quando o valor
é acessado através do atributo "__value__" do apelido de tipo (veja
Avaliação preguiçosa). Isso permite que o apelido de tipo se refira a
nomes que ainda não estão definidos.

Apelidos de tipo podem se tornar genéricos adicionando uma lista de
parâmetros de tipo após o nome. Veja Apelidos de tipo genérico para
mais.

"type" é uma palavra reservada contextual.

Adicionado na versão 3.12.

Ver também:

  **PEP 695** - Sintaxe de parâmetros de tipo
     Introduziu a instrução "type" e sintaxe para classes e funções
     genéricas.
