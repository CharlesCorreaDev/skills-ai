8. Instruções compostas
***********************

Instruções compostas contém (grupos de) outras instruções; Elas afetam
ou controlam a execução dessas outras instruções de alguma maneira. Em
geral, instruções compostas abrangem múltiplas linhas, no entanto em
algumas manifestações simples uma instrução composta inteira pode
estar contida em uma linha.

As instruções "if", "while" e "for" implementam construções
tradicionais de controle do fluxo de execução. "try" especifica
tratadores de exceção e/ou código de limpeza para uma instrução ou
grupo de instruções, enquanto a palavra reservada "with" permite a
execução de código de inicialização e finalização em volta de um bloco
de código. Definições de função e classe também são sintaticamente
instruções compostas.

Uma instrução composta consiste em uma ou mais "cláusulas". Uma
cláusula consiste em um cabeçalho e um "conjunto". Os cabeçalhos das
cláusulas de uma instrução composta específica estão todos no mesmo
nível de indentação. Cada cabeçalho de cláusula começa com uma palavra
reservada de identificação exclusiva e termina com dois pontos. Um
conjunto é um grupo de instruções controladas por uma cláusula. Um
conjunto pode ser uma ou mais instruções simples separadas por ponto e
vírgula na mesma linha do cabeçalho, após os dois pontos do cabeçalho,
ou pode ser uma ou mais instruções indentadas nas linhas subsequentes.
Somente a última forma de conjunto pode conter instruções compostas
aninhadas; o seguinte é ilegal, principalmente porque não ficaria
claro a qual cláusula "if" a seguinte cláusula "else" pertenceria:

   if test1: if test2: print(x)

Observe também que o ponto e vírgula é mais vinculado que os dois
pontos neste contexto, de modo que no exemplo a seguir, todas ou
nenhuma das chamadas "print()" são executadas:

   if x < y < z: print(x); print(y); print(z)

Resumindo:

   compound_stmt: if_stmt
                  | while_stmt
                  | for_stmt
                  | try_stmt
                  | with_stmt
                  | match_stmt
                  | funcdef
                  | classdef
                  | async_with_stmt
                  | async_for_stmt
                  | async_funcdef
   suite:         stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
   statement:     stmt_list NEWLINE | compound_stmt
   stmt_list:     simple_stmt (";" simple_stmt)* [";"]

Note que instruções sempre terminam em uma "NEWLINE" possivelmente
seguida por uma "DEDENT". Note também que cláusulas opcionais de
continuação sempre começam com uma palavra reservada que não pode
iniciar uma instrução, desta forma não há ambiguidades (o problema do
""else" pendurado" é resolvido em Python obrigando que instruções "if"
aninhadas tenham indentação)

A formatação das regras de gramática nas próximas seções põe cada
cláusula em uma linha separada para as tornar mais claras.


8.1. A instrução "if"
=====================

A instrução "if" é usada para execução condicional:

   if_stmt: "if" assignment_expression ":" suite
            ("elif" assignment_expression ":" suite)*
            ["else" ":" suite]

Ela seleciona exatamente um dos conjuntos *suite* avaliando as
expressões *assigment_expression* uma por uma até que uma seja
considerada verdadeira (veja a seção Operações booleanas para a
definição de verdadeiro e falso); então esse conjunto é executado (e
nenhuma outra parte da instrução "if" é executada ou avaliada). Se
todas as expressões forem falsas, o *suite* da cláusula "else", se
presente, é executado.


8.2. A instrução "while"
========================

A instrução "while" é usada para execução repetida desde que uma
expressão seja verdadeira:

   while_stmt: "while" assignment_expression ":" suite
               ["else" ":" suite]

Isto testa repetidamente a expressão e, se for verdadeira, executa o
primeiro conjunto; se a expressão for falsa (o que pode ser a primeira
vez que ela é testada) o conjunto da cláusula "else", se presente, é
executado e o laço termina.

Uma instrução "break" executada no primeiro conjunto termina o laço
sem executar o conjunto da cláusula "else". Uma instrução "continue"
executada no primeiro conjunto ignora o resto do conjunto e volta a
testar a expressão.


8.3. A instrução "for"
======================

A instrução "for" é usada para iterar sobre os elementos de uma
sequência (como uma string, tupla ou lista) ou outro objeto iterável:

   for_stmt: "for" target_list "in" starred_expression_list ":" suite
             ["else" ":" suite]

A expressão "starred_expression_list" é avaliada uma vez e deve
produzir um objeto *iterável*. Um *iterador* é criado para esse
iterável. O primeiro item fornecido pelo iterador é então atribuído à
lista de destino usando as regras padrão de atribuição (veja
Instruções de atribuição), e o conjunto é executado. Isso se repete
para cada item fornecido pelo iterador. Quando o iterador está
*esgotado*, o conjunto na cláusula "else", se presente, é executado e
o laço termina.

Uma instrução "break" executada no primeiro conjunto termina o loop
sem executar o conjunto da cláusula "else". Uma instrução "continue"
executada no primeiro conjunto pula o resto do conjunto e continua com
o próximo item, ou com a cláusula "else" se não houver próximo item.

O laço for faz atribuições às variáveis na lista de destino. Isso
substitui todas as atribuições anteriores a essas variáveis, incluindo
aquelas feitas no conjunto do laço for:

   for i in range(10):
       print(i)
       i = 5             # não afeta o laço for, porque i será
                         # substituída pelo índice seguinte no range

Os nomes na lista de destinos não são excluídos quando o laço termina,
mas se a sequência estiver vazia, eles não serão atribuídos pelo laço.
Dica: o tipo embutido "range()" representa sequências aritméticas
imutáveis de inteiros. Por exemplo, iterar "range(3)" sucessivamente
produz 0, 1 e depois 2.

Alterado na versão 3.11: Elementos marcados com estrela agora são
permitidos na lista de expressões.


8.4. A instrução "try"
======================

A instrução "try" especifica manipuladores de exceção e/ou código de
limpeza para um grupo de instruções:

   try_stmt:  try1_stmt | try2_stmt | try3_stmt
   try1_stmt: "try" ":" suite
              ("except" [expression ["as" identifier]] ":" suite)+
              ["else" ":" suite]
              ["finally" ":" suite]
   try2_stmt: "try" ":" suite
              ("except" "*" expression ["as" identifier] ":" suite)+
              ["else" ":" suite]
              ["finally" ":" suite]
   try3_stmt: "try" ":" suite
              "finally" ":" suite

Informações adicionais sobre exceções podem ser encontradas na seção
Exceções, e informações sobre como usar a instrução "raise" para gerar
exceções podem ser encontradas na seção A instrução raise.

Alterado na versão 3.14: Suporte para a remoção opcional de parênteses
de agrupamento ao usar vários tipos de exceção. Veja **PEP 758**.


8.4.1. Cláusula "except"
------------------------

As cláusulas "except" especificam um ou mais manipuladores de exceção.
Quando nenhuma exceção ocorre na cláusula "try", nenhum manipulador de
exceção é executado. Quando uma exceção ocorre no bloco "try", uma
busca por um manipulador de exceção é iniciada. Essa busca inspeciona
as cláusulas "except" por vez até encontrar uma que corresponda à
exceção. Uma cláusula "except" sem expressão, se presente, deve ser a
última; ela corresponde a qualquer exceção.

Para uma cláusula "except" com uma expressão, a expressão deve ser
avaliada como um tipo de exceção ou como uma tupla de tipos de
exceção. Parênteses podem ser omitidos se vários tipos de exceção
forem fornecidos e a cláusula "as" não for usada. A exceção levantada
corresponde a uma cláusula "except" cuja expressão é avaliada como a
classe ou uma *classe base não virtual* do objeto exceção, ou como uma
tupla que contém tal classe.

Se nenhuma cláusula "except" corresponder à exceção, a busca por um
manipulador de exceção continua no código circundante e na pilha de
invocação. [1]

Se a avaliação de uma expressão no cabeçalho de uma cláusula "except"
levantar uma exceção, a busca original por um manipulador será
cancelada e uma busca pela nova exceção será iniciada no código
circundante e na pilha de chamadas (ela é tratada como se toda a
instrução "try" levantasse a exceção).

Quando uma cláusula "except" correspondente é encontrada, a exceção é
atribuída ao destino especificado após a palavra reservada "as" nessa
cláusula "except", se presente, e o conjunto da cláusula "except" é
executado. Todas as cláusulas "except" devem ter um bloco executável.
Quando o final deste bloco é atingido, a execução continua normalmente
após toda a instrução "try". (Isso significa que, se existirem dois
manipuladores aninhados para a mesma exceção e a exceção ocorrer na
cláusula "try" do manipulador interno, o manipulador externo não
tratará a exceção.)

Quando uma exceção é atribuída usando "as target", ela é limpa no
final da cláusula "except". É como se

   except E as N:
       foo

fosse traduzido para

   except E as N:
       try:
           foo
       finally:
           del N

Isso significa que a exceção deve ser atribuída a um nome diferente
para poder ser referenciada após a cláusula "except". As exceções são
limpas porque, com o traceback (situação da pilha de execução) anexado
a elas, formam um ciclo de referência com o quadro de pilha, mantendo
todos os locais nesse quadro vivos até que ocorra a próxima coleta de
lixo.

Antes de um conjunto de cláusulas "except" ser executado, a exceção é
armazenada no módulo "sys", onde pode ser acessada no corpo da
cláusula "except" chamando "sys.exception()". Ao sair de um
manipulador de exceções, a exceção armazenada no módulo "sys" é
redefinida para seu valor anterior:

   >>> print(sys.exception())
   None
   >>> try:
   ...     raise TypeError
   ... except:
   ...     print(repr(sys.exception()))
   ...     try:
   ...          raise ValueError
   ...     except:
   ...         print(repr(sys.exception()))
   ...     print(repr(sys.exception()))
   ...
   TypeError()
   ValueError()
   TypeError()
   >>> print(sys.exception())
   None


8.4.2. Cláusula "except*"
-------------------------

A cláusula "except*" especifica um ou mais manipuladores para grupos
de exceções (instâncias de "BaseExceptionGroup"). Uma instrução "try"
pode ter cláusulas "except" ou "except*", mas não ambas. O tipo de
exceção para correspondência é obrigatório no caso de "except*",
portanto, "except*:" resulta em um erro de sintaxe. O tipo é
interpretado como no caso de "except", mas a correspondência é
realizada com as exceções contidas no grupo que está sendo tratado.
Uma exceção "TypeError" é levantada se um tipo correspondente for uma
subclasse de "BaseExceptionGroup", pois isso teria uma semântica
ambígua.

Quando um grupo de exceções é levantado dentro de um bloco try, cada
cláusula "except*" o divide (consulte "split()") em subgrupos de
exceções correspondentes e não correspondentes. Se o subgrupo
correspondente não estiver vazio, ele se torna a exceção tratada (o
valor retornado por "sys.exception()") e é atribuído ao alvo da
cláusula "except*" (se houver). Em seguida, o corpo da cláusula
"except*" é executado. Se o subgrupo não correspondente não estiver
vazio, ele é processado pela próxima cláusula "except*" da mesma
maneira. Isso continua até que todas as exceções do grupo tenham sido
tratadas ou até que a última cláusula "except*" tenha sido executada.

Após a execução de todas as cláusulas "except*", o grupo de exceções
não tratadas é mesclado com quaisquer exceções que foram levantadas
uma ou mais vezes em cláusulas "except*". Esse grupo de exceções,
mesclado, se propaga:

   >>> try:
   ...     raise ExceptionGroup("eg",
   ...         [ValueError(1), TypeError(2), OSError(3), OSError(4)])
   ... except* TypeError as e:
   ...     print(f'caught {type(e)} with nested {e.exceptions}')
   ... except* OSError as e:
   ...     print(f'caught {type(e)} with nested {e.exceptions}')
   ...
   caught <class 'ExceptionGroup'> with nested (TypeError(2),)
   caught <class 'ExceptionGroup'> with nested (OSError(3), OSError(4))
     + Exception Group Traceback (most recent call last):
     |   File "<doctest default[0]>", line 2, in <module>
     |     raise ExceptionGroup("eg",
     |         [ValueError(1), TypeError(2), OSError(3), OSError(4)])
     | ExceptionGroup: eg (1 sub-exception)
     +-+---------------- 1 ----------------
       | ValueError: 1
       +------------------------------------

Se a exceção levantada do bloco "try" não for um grupo de exceções e
seu tipo corresponder a uma das cláusulas "except*", ela será
capturada e encapsulada por um grupo de exceções com uma string de
mensagem vazia. Isso garante que o tipo do alvo "e" seja
"BaseExceptionGroup" de forma consistente:

   >>> try:
   ...     raise BlockingIOError
   ... except* BlockingIOError as e:
   ...     print(repr(e))
   ...
   ExceptionGroup('', (BlockingIOError(),))

"break", "continue" e "return" não podem aparecer em uma cláusula
"except*".


8.4.3. Cláusula "else"
----------------------

A cláusula opcional "else" é executada se o fluxo de controle deixar o
conjunto "try", nenhuma exceção foi levantada e nenhuma instrução
"return", "continue" ou "break" foi executada. Exceções na cláusula
"else" não são manipuladas pelas cláusulas "except" precedentes.


8.4.4. Cláusula "finally"
-------------------------

Se "finally" estiver presente, especifica um manipulador de "limpeza".
A cláusula "try" é executada, incluindo quaisquer cláusulas "except" e
"else". Se uma exceção ocorrer em qualquer uma das cláusulas e não for
tratada, a exceção será salva temporariamente. A cláusula "finally" é
executada. Se houver uma exceção salva, ela será levantada novamente
no final da cláusula "finally". Se a cláusula "finally" levantar outra
exceção, a exceção salva será definida como o contexto da nova
exceção. Se a cláusula "finally" executar uma instrução "return",
"break" ou "continue", a exceção salva será descartada. Por exemplo,
esta função retorna 42.

   def f():
       try:
           1/0
       finally:
           return 42

As informações de exceção não estão disponíveis para o programa
durante a execução da cláusula "finally".

Quando uma instrução "return", "break" ou "continue" é executada no
conjunto "try" de uma instrução "try"..."finally", a cláusula
"finally" também é executada "na saída".

O valor de retorno de uma função é determinado pela última instrução
"return" executada. Como a cláusula "finally" sempre é executada, uma
instrução "return" executada na cláusula "finally" sempre será a
última executada. A função a seguir retorna "finally".

   def foo():
       try:
           return 'try'
       finally:
           return 'finally'

Alterado na versão 3.8: Antes do Python 3.8, uma instrução "continue"
era ilegal na cláusula "finally" devido a um problema com a
implementação.

Alterado na versão 3.14: O compilador emite uma exceção
"SyntaxWarning" quando um "return", "break" ou "continue" aparece em
um bloco "finally" (veja **PEP 765**).


8.5. A instrução "with"
=======================

A instrução "with" envolve a execução de um bloco com métodos
definidos por um gerenciador de contexto (veja a seção Gerenciadores
de contexto da instrução with). Isso permite que padrões comuns de uso
de "try"..."except"..."finally" sejam encapsulados para reutilização
conveniente.

   with_stmt:          "with" ( "(" with_stmt_contents ","? ")" | with_stmt_contents ) ":" suite
   with_stmt_contents: with_item ("," with_item)*
   with_item:          expression ["as" target]

A execução da instrução "with" com um "item" ocorre da seguinte
maneira:

1. A expressão de contexto (a expressão fornecida em "with_item") é
   avaliada para obter um gerenciador de contexto.

2. O método "__enter__()" do gerenciador de contexto é carregado para
   uso posterior.

3. O método "__exit__()" do gerenciador de contexto é carregado para
   uso posterior.

4. O método "__enter__()" do gerenciador de contexto é invocado.

5. Se um alvo foi incluído na instrução "with", o valor de retorno de
   "__enter__()" é atribuído a esse alvo.

   Nota:

     A instrução "with" garante que, se o método "__enter__()"
     retornar sem erro, "__exit__()" sempre será chamado. Assim, se
     ocorrer um erro durante a atribuição à lista de alvos, ele será
     tratado da mesma forma que um erro ocorrendo dentro do conjunto
     seria. Veja a etapa 7 abaixo.

6. O conjunto *suite* é executado.

7. O método "__exit__()" do gerenciador de contexto é invocado. Se uma
   exceção fez com que o conjunto fosse encerrado, seu tipo, valor e
   traceback são passados como argumentos para "__exit__()". Caso
   contrário, três argumentos "None" são fornecidos.

   Se o conjunto foi encerrado devido a uma exceção, e o valor de
   retorno do método "__exit__()" for falso, a exceção é levantada
   novamente. Se o valor de retorno era verdadeiro, a exceção é
   suprimida, e a execução continua com a instrução após a instrução
   "with".

   Se o conjunto foi encerrado por qualquer motivo diferente de uma
   exceção, o valor de retorno de "__exit__()" é ignorado e a execução
   prossegue no local normal para o tipo de saída que foi gerada.

O seguinte código:

   with EXPRESSION as TARGET:
       SUITE

é semanticamente equivalente a:

   manager = (EXPRESSION)
   enter = manager.__enter__
   exit = manager.__exit__
   value = enter()
   hit_except = False

   try:
       TARGET = value
       SUITE
   except:
       hit_except = True
       if not exit(*sys.exc_info()):
           raise
   finally:
       if not hit_except:
           exit(None, None, None)

exceto que a pesquisa de método especial é usada de forma implícita
para "__enter__()" e "__exit__()".

Com mais de um item, os gerenciadores de contexto são processados como
se várias instruções "with" estivessem aninhadas:

   with A() as a, B() as b:
       SUITE

é semanticamente equivalente a:

   with A() as a:
       with B() as b:
           SUITE

Você também pode escrever gerenciadores de contexto multi-item em
várias linhas se os itens estiverem entre parênteses. Por exemplo:

   with (
       A() as a,
       B() as b,
   ):
       SUITE

Alterado na versão 3.1: Suporte para múltiplas expressões de contexto.

Alterado na versão 3.10: Suporte para usar parênteses de agrupamento
para dividir a instrução em várias linhas.

Ver também:

  **PEP 343** - A instrução "with"
     A especificação, o histórico e os exemplos da instrução Python
     "with".


8.6. A instrução "match"
========================

Adicionado na versão 3.10.

A instrução match é usada para correspondência de padrões. Sintaxe:

   match_stmt:   'match' subject_expr ":" NEWLINE INDENT case_block+ DEDENT
   subject_expr: flexible_expression "," [flexible_expression_list [',']]
                 | assignment_expression
   case_block:   'case' patterns [guard] ":" suite

Nota:

  Esta seção usa aspas simples para denotar palavras reservadas
  contextuais.

A correspondência de padrões aceita um padrão como entrada (seguindo
"case") e um valor de sujeito (seguindo "match"). O padrão (que pode
conter subpadrões) é correspondido ao valor de assunto. Os resultados
são:

* Um sucesso ou falha de correspondência (também chamado de sucesso ou
  falha de padrão).

* Possível vinculação de valores correspondentes a um nome. Os
  pré-requisitos para isso são discutidos mais adiante.

As palavras reservadas "match" e "case" são palavras reservadas
contextuais.

Ver também:

  * **PEP 634** -- Structural Pattern Matching: Specification

  * **PEP 636** -- Correspondência de padrões estruturais: Tutorial


8.6.1. Visão Geral
------------------

Aqui está uma visão geral do fluxo lógico de uma instrução match:

1. A expressão de sujeito "subject_expr" é avaliada e um valor de
   sujeito resultante é obtido. Se a expressão de sujeito contiver uma
   vírgula, uma tupla é construída usando as regras padrão.

2. Cada padrão em um "case_block" é tentado para corresponder ao valor
   de sujeito. As regras específicas para sucesso ou falha são
   descritas abaixo. A tentativa de correspondência também pode
   vincular alguns ou todos os nomes autônomos dentro do padrão. As
   regras precisas de vinculação de padrão variam por tipo de padrão e
   são especificadas abaixo. **As vinculações de nome feitas durante
   uma correspondência de padrão bem-sucedida sobrevivem ao bloco
   executado e podem ser usadas após a instrução match**.

   Nota:

     Durante correspondências de padrões com falha, alguns subpadrões
     podem ter sucesso. Não confie em vinculações sendo feitas para
     uma correspondência com falha. Por outro lado, não confie em
     variáveis permanecendo inalteradas após uma correspondência com
     falha. O comportamento exato depende da implementação e pode
     variar. Esta é uma decisão intencional feita para permitir que
     diferentes implementações adicionem otimizações.

3. Se o padrão for bem-sucedido, o *guard* correspondente (se
   presente) é avaliado. Neste caso, todas as vinculações de nome são
   garantidas como tendo acontecido.

   * Se o *guard* for avaliado como verdadeiro ou estiver ausente, o
     "block" dentro de "case_block" será executado.

   * Caso contrário, o próximo "case_block" será tentado conforme
     descrito acima.

   * Se não houver mais blocos de caso, a instrução match será
     concluída.

Nota:

  Os usuários geralmente nunca devem confiar em um padrão sendo
  avaliado. Dependendo da implementação, o interpretador pode
  armazenar valores em cache ou usar outras otimizações que pulam
  avaliações repetidas.

Um exemplo de instrução match:

   >>> flag = False
   >>> match (100, 200):
   ...    case (100, 300):  # Não corresponde: 200 != 300
   ...        print('Case 1')
   ...    case (100, 200) if flag:  # Corresponde com sucesso, mas o guard falha...
           print('Case 2')
   ...    case (100, y):  # Corresponde e vincula y a 200
   ...        print(f'Case 3, y: {y}')
   ...    case _:  # Padrão não testado
   ...        print('Case 4, I match anything!')
   ...
   Case 3, y: 200

Neste caso, "if flag" é um *guard*. Leia mais sobre isso na próxima
seção.


8.6.2. Guards
-------------

   guard: "if" assignment_expression

Um "guard" (que faz parte do "case") deve ter sucesso para que o
código dentro do bloco "case" seja executado. Ele assume a forma: "if"
seguido por uma expressão.

O fluxo lógico de um bloco "case" com um "guard" é o seguinte:

1. Verifique se o padrão no bloco "case" foi bem-sucedido. Se o padrão
   falhou, o "guard" não é avaliado e o próximo bloco "case" é
   verificado.

2. Se o padrão for bem-sucedido, avalia o "guard".

   * Se a condição "guard" for avaliada como verdadeira, o bloco de
     caso será selecionado.

   * Se a condição "guard" for avaliada como falsa, o bloco de caso
     não será selecionado.

   * Se o "guard" levantar uma exceção durante a avaliação, a exceção
     surgirá.

Guards podem ter efeitos colaterais, pois são expressões. A avaliação
de guards deve prosseguir do primeiro ao último bloco de caso, um de
cada vez, pulando blocos de caso cujos padrões não são todos bem-
sucedidos. (Isto é, a avaliação de guardas deve acontecer em ordem.) A
avaliação de guards deve parar quando um bloco de caso for
selecionado.


8.6.3. Blocos irrefutáveis de case
----------------------------------

Um bloco irrefutável de case é um bloco de case que corresponde a
qualquer valor. Uma instrução match pode ter no máximo um bloco
irrefutável de case, e ele deve ser o último.

Um bloco de case é considerado irrefutável se não tiver guard e seu
padrão for irrefutável. Um padrão é considerado irrefutável se
pudermos provar somente por sua sintaxe que ele sempre terá sucesso.
Somente os seguintes padrões são irrefutáveis:

* Padrões AS cujo lado esquerdo é irrefutável

* Padrões OR contendo pelo menos um padrão irrefutável

* Padrões de captura

* Padrões curingas

* padrões irrefutáveis entre parêteses


8.6.4. Padrões
--------------

Nota:

  Esta seção usa notações de gramática para além do padrão de EBNF:

  * a notação "SEP.RULE+" é uma abreviação para "RULE (SEP RULE)*"

  * a notação "!RULE" é uma abreviação para uma asserção de negação
    antecipada.

Esta é a sintaxe de nível superior para "patterns" (padrões):

   patterns:       open_sequence_pattern | pattern
   pattern:        as_pattern | or_pattern
   closed_pattern: | literal_pattern
                   | capture_pattern
                   | wildcard_pattern
                   | value_pattern
                   | group_pattern
                   | sequence_pattern
                   | mapping_pattern
                   | class_pattern

As descrições abaixo incluirão uma descrição "em termos simples" de o
que o padrão faz para fins ilustrativos (créditos a Raymond Hettinger
pelo documento que inspirou a maioria das descrições). Note que essas
descrições são puramente para fins ilustrativos, e **não
necessariamente** refletem a implementação subjacente.  Além disso,
elas não cobrem todas as formas válidas.


8.6.4.1. Padrões OR
~~~~~~~~~~~~~~~~~~~

Um padrão OR é composto por dois ou mais padrões separados por barras
verticais "|".  Sintaxe:

   or_pattern: "|".closed_pattern+

Somente o último subpadrão pode ser irrefutável, e cada subpadrão deve
vincular o mesmo conjunto de nomes para evitar ambiguidades.

Um padrão OR testa a correspondência de cada um dos seus subpadrões,
em sequência, ao valor do sujeito, até que uma delas seja bem
sucedida.  O padrão OR é então considerado bem sucedido.  Caso
contrário, se todas elas falharam, o padrão OR falhou.

Em termos simples, "P1 | P2 | ..." vai tentar fazer corresponder "P1",
se falhar vai tentar "P2", declarando sucesso se houver sucesso em
qualquer uma das tentativas, e falhando caso contrário.


8.6.4.2. Padrões AS
~~~~~~~~~~~~~~~~~~~

Um padrão AS corresponde a um padrão OR à esquerda da palavra
reservada "as" de um assunto. Sintaxe:

   as_pattern: or_pattern "as" capture_pattern

Se o padrão OR falhar, o padrão AS falhará. Caso contrário, o padrão
AS vincula o assunto ao nome à direita da palavra-chave as e obtém
sucesso. "capture_pattern" não pode ser um "_".

Em termos simples, "P as NAME" corresponderá a "P" e, em caso de
sucesso, definirá "NAME = <assunto>".


8.6.4.3. Padrões literais
~~~~~~~~~~~~~~~~~~~~~~~~~

Um padrão literal corresponde à maioria dos literais em Python.
Sintaxe:

   literal_pattern: signed_number
                    | signed_number "+" NUMBER
                    | signed_number "-" NUMBER
                    | strings
                    | "None"
                    | "True"
                    | "False"
   signed_number:   ["+" | "-"] NUMBER

A regra "strings" e o token "NUMBER" são definidos na gramática padrão
do Python. Strings entre aspas triplas são suportadas. Strings brutas
e strings de bytes são suportadas. Literais de strings formatadas e
Literais de string template (t-strings) não são suportadas.

As formas "signed_number '+' NUMBER" e "signed_number '-' NUMBER" são
para expressar números complexos; elas requerem um número real à
esquerda e um número imaginário à direita. Por exemplo, "3 + 4j".

Em termos simples, "LITERAL" terá sucesso somente se "<assunto> ==
LITERAL". Para os singletons "None", "True" e "False", o operador "is"
é usado.


8.6.4.4. Padrões de captura
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um padrão de captura vincula o valor do assunto a um nome. Sintaxe:

   capture_pattern: !'_' NAME

Um único sublinhado "_" não é um padrão de captura (é o que "!'_'"
expressa). Em vez disso, ele é tratado como um "wildcard_pattern".

Em um determinado padrão, um determinado nome só pode ser vinculado
uma vez. Por exemplo, "case x, x: ..." é inválido enquanto "case [x] |
x: ..." é permitido.

Os padrões de captura sempre são bem-sucedidos. A vinculação segue
regras de escopo estabelecidas pelo operador de expressão de
atribuição na **PEP 572**; o nome se torna uma variável local no
escopo de função de contenção mais próximo, a menos que haja uma
instrução "global" ou "nonlocal" aplicável.

Em termos simples, "NAME" sempre terá sucesso e definirá "NAME =
<assunto>".


8.6.4.5. Padrões curingas
~~~~~~~~~~~~~~~~~~~~~~~~~

Um padrão curinga sempre tem sucesso (corresponde a qualquer coisa) e
não vincula nenhum nome. Sintaxe:

   wildcard_pattern: '_'

"_" é uma palavra reservada contextual dentro de qualquer padrão, mas
somente dentro de padrões. É um identificador, como de costume, mesmo
dentro de expressões de assunto "match"s, "guard"s e blocos "case".

Em termos simples, "_" sempre terá sucesso.


8.6.4.6. Padrões de valor
~~~~~~~~~~~~~~~~~~~~~~~~~

Um padrão de valor representa um valor nomeado em Python. Sintaxe:

   value_pattern: attr
   attr:          name_or_attr "." NAME
   name_or_attr:  attr | NAME

O nome pontilhado no padrão é pesquisado usando as regras de resolução
de nomes padrão do Python. O padrão é bem-sucedido se o valor
encontrado for comparado igual ao valor do assunto (usando o operador
de igualdade "==").

Em termos simples, "NAME1.NAME2" terá sucesso somente se "<assunto> ==
NAME1.NAME2"

Nota:

  Se o mesmo valor ocorrer várias vezes na mesma instrução match, o
  interpretador pode armazenar em cache o primeiro valor encontrado e
  reutilizá-lo em vez de repetir a mesma pesquisa. Esse cache é
  estritamente vinculado a uma determinada execução de uma determinada
  instrução match.


8.6.4.7. Padrões de grupo
~~~~~~~~~~~~~~~~~~~~~~~~~

Um padrão de grupo permite que os usuários adicionem parênteses em
torno de padrões para enfatizar o agrupamento pretendido. Caso
contrário, não há sintaxe adicional. Sintaxe:

   group_pattern: "(" pattern ")"

Em termos simples, "(P)" tem o mesmo efeito que "P".


8.6.4.8. Padrões de sequência
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um padrão de sequência contém vários subpadrões a serem correspondidos
com elementos de sequência. A sintaxe é similar ao desempacotamento de
uma lista ou tupla.

   sequence_pattern:       "[" [maybe_sequence_pattern] "]"
                           | "(" [open_sequence_pattern] ")"
   open_sequence_pattern:  maybe_star_pattern "," [maybe_sequence_pattern]
   maybe_sequence_pattern: ",".maybe_star_pattern+ ","?
   maybe_star_pattern:     star_pattern | pattern
   star_pattern:           "*" (capture_pattern | wildcard_pattern)

Não há diferença se parênteses ou colchetes são usados para padrões de
sequência (por exemplo, "(...)" vs "[...]").

Nota:

  Um único padrão entre parênteses sem uma vírgula final (por exemplo,
  "(3 | 4)") é um padrão de grupo. Enquanto um único padrão entre
  colchetes (por exemplo, "[3 | 4]") ainda é um padrão de sequência.

No máximo um subpadrão de estrela pode estar em um padrão de
sequência. O subpadrão de estrela pode ocorrer em qualquer posição. Se
nenhum subpadrão de estrela estiver presente, o padrão de sequência é
um padrão de sequência de comprimento fixo; caso contrário, é um
padrão de sequência de comprimento variável.

A seguir está o fluxo lógico para corresponder um padrão de sequência
com um valor de assunto:

1. Se o valor do assunto não for uma sequência [2], o padrão de
   sequência falhará.

2. Se o valor do assunto for uma instância de "str", "bytes" ou
   "bytearray", o padrão de sequência falhará.

3. As etapas subsequentes dependem se o padrão de sequência é fixo ou
   de comprimento variável.

   Se o padrão de sequência for de comprimento fixo:

   1. Se o comprimento da sequência do assunto não for igual ao número
      de subpadrões, o padrão da sequência falha

   2. Subpadrões no padrão de sequência são correspondidos aos seus
      itens correspondentes na sequência de assunto da esquerda para a
      direita. A correspondência para assim que um subpadrão falha. Se
      todos os subpadrões tiverem sucesso em corresponder ao seu item
      correspondente, o padrão de sequência é bem-sucedido.

   Caso contrário, se o padrão de sequência for de comprimento
   variável:

   1. Se o comprimento da sequência do assunto for menor que o número
      de subpadrões não-estrela, o padrão da sequência falha.

   2. Os principais subpadrões não estelares são correspondidos aos
      seus itens correspondentes, como nas sequências de comprimento
      fixo.

   3. Se a etapa anterior for bem-sucedida, o subpadrão estrela
      corresponde a uma lista formada pelos itens de assunto
      restantes, excluindo os itens restantes correspondentes aos
      subpadrões não-estrela que seguem o subpadrão estrela.

   4. Os subpadrões não-estrela restantes são correspondidos aos seus
      itens de assunto correspondentes, como em uma sequência de
      comprimento fixo.

   Nota:

     O comprimento da sequência de assunto é obtido via "len()" (ou
     seja, via protocolo "__len__()"). Esse comprimento pode ser
     armazenado em cache pelo interpretador de forma similar a padrões
     de valor.

Em termos simples, "[P1, P2, P3," ... ", P<N>]" corresponde somente se
tudo o seguinte acontecer:

* verifica se "<subject>" é uma sequência

* "len(subject) == <N>"

* "P1" corresponde a "<subject>[0]" (observe que esta correspondência
  também pode vincular nomes)

* "P2" corresponde a "<subject>[1]" (observe que esta correspondência
  também pode vincular nomes)

* ... e assim por diante para o padrão/elemento correspondente.


8.6.4.9. Padrões de mapeamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um padrão de mapeamento contém um ou mais padrões de chave-valor. A
sintaxe é similar à construção de um dicionário. Sintaxe:

   mapping_pattern:     "{" [items_pattern] "}"
   items_pattern:       ",".key_value_pattern+ ","?
   key_value_pattern:   (literal_pattern | value_pattern) ":" pattern
                        | double_star_pattern
   double_star_pattern: "**" capture_pattern

No máximo um padrão de estrela dupla pode estar em um padrão de
mapeamento. O padrão de estrela dupla deve ser o último subpadrão no
padrão de mapeamento.

Chaves duplicadas em padrões de mapeamento não são permitidas. Chaves
literais duplicadas levantarão um "SyntaxError". Duas chaves que de
outra forma têm o mesmo valor levantarão "ValueError" em tempo de
execução.

A seguir está o fluxo lógico para comparar um padrão de mapeamento com
um valor de assunto:

1. Se o valor do assunto não for um mapeamento [3], o padrão de
   mapeamento falhará.

2. Se cada chave fornecida no padrão de mapeamento estiver presente no
   mapeamento de assunto, e o padrão para cada chave corresponder ao
   item correspondente do mapeamento de assunto, o padrão de
   mapeamento será bem-sucedido.

3. Se chaves duplicadas forem detectadas no padrão de mapeamento, o
   padrão será considerado inválido. Uma exceção "SyntaxError" é
   levantada para valores literais duplicados; ou "ValueError" para
   chaves nomeadas do mesmo valor.

Nota:

  Os pares de chave-valor são correspondidos usando o formato de dois
  argumentos do método "get()" do assunto do mapeamento. Os pares de
  chave-valor correspondidos já devem estar presentes no mapeamento e
  não devem ser criados em tempo de uso via "__missing__()" ou
  "__getitem__()".

Em termos simples, "{KEY1: P1, KEY2: P2, ... }" corresponde somente se
tudo o seguinte acontecer:

* verifica se "<assunto>" é um mapeamento

* "KEY1 in <assunto>"

* "P1" corresponde a "<assunto>[KEY1]"

* ... e assim por diante para o par KEY/elemento correspondente.


8.6.4.10. Padrões de classe
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um padrão de classe representa uma classe e seus argumentos nomeados e
posicionais (se houver). Sintaxe:

   class_pattern:       name_or_attr "(" [pattern_arguments ","?] ")"
   pattern_arguments:   positional_patterns ["," keyword_patterns]
                        | keyword_patterns
   positional_patterns: ",".pattern+
   keyword_patterns:    ",".keyword_pattern+
   keyword_pattern:     NAME "=" pattern

O mesmo argumento nomeado não deve ser repetido em padrões de classe.

A seguir está o fluxo lógico para corresponder a um padrão de classe
com um valor de assunto:

1. Se "name_or_attr" não for uma instância do tipo embutido "type" ,
   levanta "TypeError".

2. Se o valor do assunto não for uma instância de "name_or_attr"
   (testado via "isinstance()"), o padrão de classe falhará.

3. Se nenhum argumento de padrão estiver presente, o padrão é bem-
   sucedido. Caso contrário, as etapas subsequentes dependem se os
   padrões de argumento posicional ou nomeado estão presentes.

   Para vários tipos embutidos (especificados abaixo), um único
   subpadrão posicional é aceito, o qual corresponderá a todo o
   assunto; para esses tipos, os padrões de argumentos nomeados também
   funcionam como para outros tipos.

   Se apenas padrões de argumentos nomeados estiverem presentes, eles
   serão processados da seguinte forma, um por um:

   1. A palavra reservada é procurada como um atributo no assunto.

      * Se isso levantar uma exceção diferente de "AttributeError", a
        exceção será exibida.

      * Se isso levantar "AttributeError", o padrão de classe falhou.

      * Caso contrário, o subpadrão associado ao padrão de argumento
        nomeado é correspondido ao valor de atributo do sujeito. Se
        isso falhar, o padrão de classe falha; se isso for bem-
        sucedido, a correspondência prossegue para o próximo argumento
        nomeado.

   2. Se todos os padrões de argumento nomeado forem bem-sucedidos, o
      padrão de classe será bem-sucedido.

   Se houver algum padrão posicional presente, ele será convertido em
   padrões de argumento nomeado usando o atributo "__match_args__" na
   classe "name_or_attr" antes da correspondência:

   1. O equivalente de "getattr(cls, "__match_args__", ())" é chamado.

      * Se isso levantar uma exceção, a exceção surgirá.

      * Se o valor retornado não for uma tupla, a conversão falhará e
        "TypeError" será levantada.

      * Se houver mais padrões posicionais do que
        "len(cls.__match_args__)", "TypeError" será levantada.

      * Caso contrário, o padrão posicional "i" é convertido em um
        padrão de argumento nomeado usando "__match_args__[i]" como
        argumento nomeado. "__match_args__[i]" deve ser uma string;
        caso contrário, "TypeError" é levantada.

      * Se houver argumentos nomeados duplicados, "TypeError" será
        levantada.

      Ver também:

        Customizando argumentos posicionais na classe correspondência
        de padrão

   2. Uma vez que todos os padrões posicionais foram convertidos em
      padrões de argumentos nomeados, a correspondência continua como
      se houvesse apenas padrões de palavras reservadas.

   Para os seguintes tipos embutidos, o tratamento de subpadrões
   posicionais é diferente:

   * "bool"

   * "bytearray"

   * "bytes"

   * "dict"

   * "float"

   * "frozendict"

   * "frozenset"

   * "int"

   * "list"

   * "set"

   * "str"

   * "tuple"

   Essas classes aceitam um único argumento posicional, e o padrão ali
   é correspondido ao objeto inteiro em vez de um atributo. Por
   exemplo, "int(0|1)" corresponde ao valor "0", mas não ao valor
   "0.0".

Em termos simples, "CLS(P1, attr=P2)" corresponde somente se o
seguinte acontecer:

* "isinstance(<assunto>, CLS)"

* converte "P1" em um padrão de argumento nomeado usando
  "CLS.__match_args__"

* Para cada argumento nomeado "attr=P2":

  * "hasattr(<assunto>, "attr")"

  * "P2" corresponde a "<assunto>.attr"

* ... e assim por diante para o par argumento nomeado/elemento
  correspondente.

Ver também:

  * **PEP 634** -- Structural Pattern Matching: Specification

  * **PEP 636** -- Correspondência de padrões estruturais: Tutorial


8.7. Definições de função
=========================

Uma definição de função define um objeto de função definido pelo
usuário (veja a seção A hierarquia de tipos padrão):

   funcdef:                   [decorators] "def" funcname [type_params] "(" [parameter_list] ")"
                              ["->" expression] ":" suite
   decorators:                decorator+
   decorator:                 "@" assignment_expression NEWLINE
   parameter_list:            defparameter ("," defparameter)* "," "/" ["," [parameter_list_no_posonly]]
                                | parameter_list_no_posonly
   parameter_list_no_posonly: defparameter ("," defparameter)* ["," [parameter_list_starargs]]
                              | parameter_list_starargs
   parameter_list_starargs:   "*" star_parameter ("," defparameter)* ["," [parameter_star_kwargs]]
                              | "*" ("," defparameter)+ ["," [parameter_star_kwargs]]
                              | parameter_star_kwargs
   parameter_star_kwargs:     "**" parameter [","]
   parameter:                 identifier [":" expression]
   star_parameter:            identifier [":" ["*"] expression]
   defparameter:              parameter ["=" expression]
   funcname:                  identifier

Uma definição de função é uma instrução executável. Sua execução
vincula o nome da função no espaço de nomes local atual a um objeto
função (um invólucro em torno do código executável para a função).
Este objeto função contém uma referência ao espaço de nomes global
atual como o espaço de nomes global a ser usado quando a função é
chamada.

A definição da função não executa o corpo da função; ela é executada
somente quando a função é chamada. [4]

Uma definição de função pode ser encapsulada por uma ou mais
expressões *decoradoras*. Expressões decoradoras são avaliadas quando
a função é definida, no escopo que contém a definição da função. O
resultado deve ser um chamável, que é invocado com o objeto de função
como o único argumento. O valor retornado é vinculado ao nome da
função em vez do objeto de função. Vários decoradores são aplicados de
forma aninhada. Por exemplo, o código a seguir

   @f1(arg)
   @f2
   def func(): pass

é aproximadamente equivalente a

   def func(): pass
   func = f1(arg)(f2(func))

exceto que a função original não está temporariamente vinculada ao
nome "func".

Alterado na versão 3.9: Funções podem ser decoradas com qualquer
"assignment_expression" válida. Anteriormente, a gramática era muito
mais restritiva; veja **PEP 614** para detalhes.

Uma lista de parâmetros de tipo pode ser dada entre colchetes entre o
nome da função e o parêntese de abertura para sua lista de parâmetros.
Isso indica aos verificadores de tipo estático que a função é
genérica. Em tempo de execução, os parâmetros de tipo podem ser
recuperados do atributo "__type_params__" da função. Veja Funções
genéricas para mais.

Alterado na versão 3.12: Listas de parâmetros de tipo são novas no
Python 3.12.

Quando um ou mais *parâmetros* têm a forma *parameter* "="
*expression*, diz-se que a função tem "valores de parâmetro padrão".
Para um parâmetro com um valor padrão, o *argumento* correspondente
pode ser omitido de uma chamada, em cujo caso o valor padrão do
parâmetro é substituído. Se um parâmetro tiver um valor padrão, todos
os parâmetros seguintes até ""*"" também devem ter um valor padrão ---
esta é uma restrição sintática que não é expressa pela gramática.

**Os valores dos parâmetros padrão são avaliados da esquerda para a
direita quando a definição da função é executada.** Isso significa que
a expressão é avaliada uma vez, quando a função é definida, e que o
mesmo valor "pré-calculado" é usado em cada chamada. Isso é
especialmente importante para entender quando um valor de parâmetro
padrão é um objeto mutável, como uma lista ou um dicionário: se a
função modificar o objeto (por exemplo, anexando um item a uma lista),
o valor do parâmetro padrão será efetivamente modificado. Isso
geralmente não é o que se pretendia. Uma maneira de contornar isso é
usar "None" como o padrão e testá-lo explicitamente no corpo da
função, por exemplo:

   def whats_on_the_telly(penguin=None):
       if penguin is None:
           penguin = []
       penguin.append("property of the zoo")
       return penguin

A semântica de chamada de função é descrita em mais detalhes na seção
Chamadas. Uma chamada de função sempre atribui valores a todos os
parâmetros mencionados na lista de parâmetros, seja de argumentos
posicionais, de argumentos nomeados ou de valores padrão. Se o formato
""*identifier"" estiver presente, ele será inicializado para uma tupla
que recebe quaisquer parâmetros posicionais excedentes, padronizando
para a tupla vazia. Se o formato ""**identifier"" estiver presente,
ele será inicializado para um novo mapeamento ordenado que recebe
quaisquer argumentos nomeados excedentes, padronizando para um novo
mapeamento vazio do mesmo tipo. Parâmetros após ""*"" ou
""*identifier"" são parâmetros somente-nomeados e podem ser passados
somente por argumentos nomeados. Parâmetros antes de ""/"" são
parâmetros somente-posicionais e podem ser passados somente por
argumentos posicionais.

Alterado na versão 3.8: A sintaxe do parâmetro de função "/" pode ser
usada para indicar parâmetros somente-posicionais. Veja a **PEP 570**
para detalhes.

Os parâmetros podem ter uma *anotação* do formato "": expressão"" após
o nome do parâmetro. Qualquer parâmetro pode ter uma anotação, mesmo
aqueles do formato "*identificador" ou "**identificador". (Como um
caso especial, parâmetros do formato "*identificador" podem ter uma
anotação "": *expressão"".) As funções podem ter uma anotação "return"
do formato ""-> expressão"" após a lista de parâmetros. Essas
anotações podem ser qualquer expressão Python válida. A presença de
anotações não altera a semântica de uma função. Veja Anotações para
mais informações sobre anotações.

Alterado na versão 3.11: Parâmetros do formato ""*identificador""
podem ter uma anotação "": *expressão"". Veja **PEP 646**.

Também é possível criar funções anônimas (funções não vinculadas a um
nome), para uso imediato em expressões. Isso usa expressões lambda,
descritas na seção Lambdas. Observe que a expressão lambda é meramente
uma abreviação para uma definição de função simplificada; uma função
definida em uma instrução ""def"" pode ser passada adiante ou
atribuída a outro nome, assim como uma função definida por uma
expressão lambda. O formato ""def"" é, na verdade, mais poderoso, pois
permite a execução de várias instruções e anotações.

**Nota do programador:** Funções são objetos de primeira classe. Uma
instrução ""def"" executada dentro de uma definição de função define
uma função local que pode ser retornada ou passada adiante. Variáveis
livres usadas na função aninhada podem acessar as variáveis locais da
função que contém o "def". Veja a seção Nomeação e ligação para
detalhes.

Ver também:

  **PEP 3107** - Anotações de função
     A especificação original para anotações de funções.

  **PEP 484** - Dicas de tipo
     Definição de um significado padrão para anotações: dicas de tipo.

  **PEP 526** - Sintaxe para anotações de variáveis
     Capacidade de fornecer dica de tipo para declarações de
     variáveis, incluindo variáveis de classe e variáveis de
     instância.

  **PEP 563** - Avaliação postergada de anotações
     Suporte para referências futuras dentro de anotações, preservando
     anotações em um formato de string em tempo de execução em vez de
     avaliação antecipada.

  **PEP 318** - Decoradores para funções e métodos
     Decoradores de função e método foram introduzidos. Decoradores de
     classe foram introduzidos na **PEP 3129**.


8.8. Definições de classe
=========================

Uma definição de classe define um objeto classe (veja a seção A
hierarquia de tipos padrão):

   classdef:    [decorators] "class" classname [type_params] [inheritance] ":" suite
   inheritance: "(" [argument_list] ")"
   classname:   identifier

Uma definição de classe é uma instrução executável. A lista de herança
geralmente fornece uma lista de classes base (veja Metaclasses para
usos mais avançados), então cada item na lista deve ser executada como
um objeto classe que permite extensão via subclasse. Classes sem uma
lista de herança herdam, por padrão, da classe base "object";
portanto,

   class Foo:
       pass

equivale a

   class Foo(object):
       pass

Pode haver uma ou mais classes base; veja Herança múltipla abaixo para
mais informações.

O conjunto da classe é então executado em um novo quadro de execução
(veja Nomeação e ligação), usando um espaço de nomes local recém-
criado e o espaço de nomes global original. (Normalmente, o conjunto
contém principalmente definições de função.) Quando o conjunto da
classe termina a execução, seu quadro de execução é descartado, mas
seu espaço de nomes local é salvo. [5] Um objeto classe é então criado
usando a lista de herança para as classes base e o espaço de nomes
local salvo para o dicionário de atributos. O nome da classe é
vinculado a este objeto classe no espaço de nomes local original.

A ordem em que os atributos são definidos no corpo da classe é
preservada no "__dict__" da nova classe. Observe que isso é confiável
somente logo após a classe ser criada e somente para classes que foram
definidas usando a sintaxe de definição.

A criação de classes pode ser bastante personalizada usando
metaclasses.

As classes também podem ser decoradas: assim como na decoração de
funções,

   @f1(arg)
   @f2
   class Foo: pass

é aproximadamente equivalente a

   class Foo: pass
   Foo = f1(arg)(f2(Foo))

As regras de execução para as expressões de decorador são as mesmas
que para decoradores de função. O resultado é então vinculado ao nome
da classe.

Alterado na versão 3.9: Classes podem ser decoradas com qualquer
"assignment_expression" válida. Anteriormente, a gramática era muito
mais restritiva; veja **PEP 614** para detalhes.

Uma lista de parâmetros de tipo pode ser dada entre colchetes
imediatamente após o nome da classe. Isso indica aos verificadores de
tipo estático que a classe é genérica. Em tempo de execução, os
parâmetros de tipo podem ser recuperados do atributo "__type_params__"
da classe. Veja Classes genéricas para mais.

Alterado na versão 3.12: Listas de parâmetros de tipo são novas no
Python 3.12.

**Nota do programador:** Variáveis definidas na definição de classe
são atributos de classe; elas são compartilhadas por instâncias.
Atributos de instância podem ser definidos em um método com "self.nome
= valor". Atributos de classe e instância são acessíveis por meio da
notação ""self.nome"", e um atributo de instância oculta um atributo
de classe com o mesmo nome quando acessado dessa forma. Atributos de
classe podem ser usados como padrões para atributos de instância, mas
usar valores mutáveis pode levar a resultados inesperados. Descritores
podem ser usados para criar variáveis de instância com diferentes
detalhes de implementação.

Ver também:

  **PEP 3115** - Metaclasses no Python 3000
     A proposta que alterou a declaração de metaclasses para a sintaxe
     atual e a semântica de como as classes com metaclasses são
     construídas.

  **PEP 3129** - Decoradores de classe
     A proposta que adicionou decoradores de classe. Decoradores de
     função e método foram introduzidos na **PEP 318**.


8.8.1. Herança múltipla
-----------------------

Classes Python podem ter várias classes base, uma técnica conhecida
como *herança múltipla*. As classes base são especificadas na
definição de classe, listadas entre parênteses após o nome da classe,
separadas por vírgulas. Por exemplo, a seguinte definição de classe:

   >>> class A: pass
   >>> class B: pass
   >>> class C(A, B): pass

define a classe "C" que herda das classes "A" e "B".

A *ordem de resolução de métodos* (MRO) é a ordem em que as classes
base são pesquisadas ao procurar um atributo em uma classe.  Veja A
Ordem de Resolução de Métodos do Python 2.3 para uma descrição de como
o Python determina a MRO de uma classe.

A herança múltipla nem sempre é permitida. Tentar definir uma classe
com herança múltipla levantará um erro se uma das bases não permitir a
criação de subclasses, se não for possível criar uma MRO consistente,
se nenhuma metaclasse válida puder ser determinada ou se houver um
conflito de layout de instância. Discutiremos cada um desses casos a
seguir.

Primeiramente, todas as classes base devem permitir subclasse. Embora
a maioria das classes permitam subclasse, algumas classes embutidas
não permitem, como, por exemplo, "bool":

   >>> class SubBool(bool):  # TypeError
   ...    pass
   Traceback (most recent call last):
      ...
   TypeError: type 'bool' is not an acceptable base type

Na MRO resolvida de uma classe, as bases da classe aparecem na ordem
em que foram especificadas na lista de bases da classe. Além disso, a
MRO sempre lista uma classe filha antes de qualquer uma de suas bases.
Uma definição de classe falhará se for impossível resolver, a partir
da lista de bases fornecida, uma MRO consistente que satisfaça essas
regras:

   >>> class Base: pass
   >>> class Child(Base): pass
   >>> class Grandchild(Base, Child): pass  # TypeError
   Traceback (most recent call last):
      ...
   TypeError: Cannot create a consistent method resolution order (MRO) for bases Base, Child

Na MRO de "Grandchild", "Base" deve aparecer antes de "Child" porque é
a primeira classe base na lista, mas também deve aparecer depois de
"Child" porque é pai de "Child". Isso é uma contradição; portanto, a
classe não pode ser definida.

Se algumas das bases tiverem uma *metaclasse* personalizada, a
metaclasse da classe resultante é escolhida entre as metaclasses das
bases e a metaclasse explicitamente especificada da classe filha. Ela
deve ser uma metaclasse que seja subclasse de todas as outras
metaclasses candidatas. Se não existir tal metaclasse entre as
candidatas, a classe não pode ser criada, conforme explicado em
Determinando a metaclasse apropriada.

Por fim, os layouts de instância das bases devem ser compatíveis entre
si. Isso significa que deve ser possível calcular uma *base sólida*
para a classe. Exatamente quais classes são consideradas bases sólidas
depende da implementação do Python.

No CPython, uma classe é uma base sólida se a definição de "__slots__"
não for vazia. Muitas, mas não todas, das classes definidas em C
também são bases sólidas, incluindo a maioria das embutidas (como
"int" ou "BaseException"), mas excluindo a maioria das classes
"Exception" concretas. Em geral, uma classe C é uma base sólida se sua
estrutura subjacente tiver um tamanho diferente do de sua classe base.

Toda classe tem uma base sólida. "object", a classe base de todas as
classes, é a sua própria base sólida. Quando há uma única base, a
classe filha é a sua própria base sólida se ela mesma for uma base
sólida. Se não for, ela herda a base sólida da classe base. Se houver
múltiplas bases, primeiro encontramos a base sólida de cada classe
base, o que gera uma lista de bases sólidas candidatas. Se exatamente
uma dessas candidatas for subclasse de todas as outras, ela será a
base sólida. Caso contrário, a criação da classe falha.

Exemplo:

   >>> class Solid1:
   ... __slots__ = ("solid1",)
   >>>
   >>> class Solid2:
   ... __slots__ = ("solid2",)
   >>>
   >>> class SolidChild(Solid1):
   ... __slots__ = ("solid_child",)
   >>>
   >>> class C1: # a base sólida é `object`
   ... pass
   >>>
   >>> # OK: as bases sólidas são `Solid1` e `object`, e `Solid1` é uma subclasse de `object`.
   >>> class C2(Solid1, C1): # a base sólida é `Solid1`
   ... pass
   >>>
   >>> # OK: as bases sólidas são `SolidChild` e `Solid1`, e `SolidChild` é uma subclasse de `Solid1`.
   >>> class C3(SolidChild, Solid1): # a base sólida é `SolidChild`
   ... pass
   >>>
   >>> # Erro: as bases sólidas são `Solid1` e `Solid2`, mas nenhuma é subclasse da outra.
   >>> class C4(Solid1, Solid2): # erro: não há uma única base sólida
   ... pass
   Traceback (most recent call last):
   ...
   TypeError: multiple bases have instance lay-out conflict


8.9. Corrotinas
===============

Adicionado na versão 3.5.


8.9.1. Definição de função de corrotina
---------------------------------------

   async_funcdef: [decorators] "async" "def" funcname "(" [parameter_list] ")"
                  ["->" expression] ":" suite

A execução de corrotinas do Python pode ser suspensa e retomada em
muitos pontos (consulte *coroutine*). As expressões "await", "async
for" e "async with" só podem ser usadas no corpo de uma função de
corrotina.

Funções definidas com a sintaxe "async def" são sempre funções de
corrotina, mesmo que não contenham palavras reservadas "await" ou
"async".

Ocorre uma "SyntaxError" se usada uma expressão "yield from" dentro do
corpo de uma função de corrotina.

Um exemplo de uma função de corrotina:

   async def func(param1, param2):
       faz_algo()
       await alguma_corrotina()

Alterado na versão 3.7: "await" e "async" agora são palavras
reservadas; anteriormente, elas só eram tratadas como tal dentro do
corpo de uma função de corrotina.


8.9.2. A instrução "async for"
------------------------------

   async_for_stmt: "async" for_stmt

Um *iterável assíncrono* fornece um método "__aiter__" que retorna
diretamente um *iterador assíncrono*, que pode chamar código
assíncrono em seu método "__anext__".

A instrução "async for" permite iteração conveniente sobre iteráveis
assíncronos.

O seguinte código:

   async for TARGET in ITER:
       SUITE
   else:
       SUITE2

É semanticamente equivalente a:

   iter = (ITER).__aiter__()
   running = True

   while running:
       try:
           TARGET = await iter.__anext__()
       except StopAsyncIteration:
           running = False
       else:
           SUITE
   else:
       SUITE2

exceto que a pesquisa de método especial  implícita é usada para
"__aiter__()" e "__anext__()".

Ocorre uma "SyntaxError" se usada uma instrução "async for" fora do
corpo de uma função de corrotina.


8.9.3. A instrução "async with"
-------------------------------

   async_with_stmt: "async" with_stmt

Um *gerenciador de contexto assíncrono* é um *gerenciador de contexto*
que é capaz de suspender a execução em seus métodos *enter* e *exit*.

O seguinte código:

   async with EXPRESSÃO as ALVO:
       COMANDOS

é semanticamente equivalente a:

   manager = (EXPRESSION)
   aenter = manager.__aenter__
   aexit = manager.__aexit__
   value = await aenter()
   hit_except = False

   try:
       TARGET = value
       SUITE
   except:
       hit_except = True
       if not await aexit(*sys.exc_info()):
           raise
   finally:
       if not hit_except:
           await aexit(None, None, None)

exceto que a pesquisa de método especial é usada de forma implícita
para "__aenter__()" e "__aexit__()".

Ocorre uma "SyntaxError" se usada uma instrução "async with" fora do
corpo de uma função de corrotina.

Ver também:

  **PEP 492** - Corrotina com sintaxe de async e wait
     A proposta que tornou as corrotinas um conceito autônomo em
     Python e adicionou sintaxe de suporte.


8.10. Listas de parâmetros de tipo
==================================

Adicionado na versão 3.12.

Alterado na versão 3.13: Foi adicionado suporte para valores padrão
(veja **PEP 696**).

   type_params:  "[" type_param ("," type_param)* "]"
   type_param:   typevar | typevartuple | paramspec
   typevar:      identifier (":" expression)? ("=" expression)?
   typevartuple: "*" identifier ("=" expression)?
   paramspec:    "**" identifier ("=" expression)?

Funções (incluindo corrotinas), classes e apelidos de tipo podem
conter uma lista de parâmetros de tipo:

   def max[T](args: list[T]) -> T:
       ...

   async def amax[T](args: list[T]) -> T:
       ...

   class Bag[T]:
       def __iter__(self) -> Iterator[T]:
           ...

       def add(self, arg: T) -> None:
           ...

   type ListOrSet[T] = list[T] | set[T]

Semanticamente, isso indica que a função, classe ou apelido de tipo é
genérico sobre uma variável de tipo. Essas informações são usadas
principalmente por verificadores de tipo estático e, em tempo de
execução, objetos genéricos se comportam muito como suas contrapartes
não genéricas.

Parâmetros de tipo são declarados entre colchetes ("[]") imediatamente
após o nome da função, classe ou apelido de tipo. Os parâmetros de
tipo são acessíveis dentro do escopo do objeto genérico, mas não em
outro lugar. Assim, após uma declaração "def func[T](): pass", o nome
"T" não está disponível no escopo do módulo. Abaixo, a semântica de
objetos genéricos é descrita com mais precisão. O escopo de parâmetros
de tipo é modelado com uma função especial (tecnicamente, um escopo de
anotação) que encapsula a criação do objeto genérico.

Funções genéricas, classes e apelidos de tipo têm um atributo
"__type_params__" listando seus parâmetros de tipo.

Existem três espécies de parâmetros de tipo:

* "typing.TypeVar", introduzido por um nome simples (por exemplo,
  "T"). Semanticamente, isso representa um único tipo para um
  verificador de tipos.

* "typing.TypeVarTuple", introduzido por um nome prefixado com um
  único asterisco (por exemplo, "*Ts"). Semanticamente, isso
  representa uma tupla de qualquer número de tipos.

* "typing.ParamSpec", introduzido por um nome prefixado com dois
  asteriscos (por exemplo, "**P"). Semanticamente, isso representa os
  parâmetros de um chamável.

As declarações de "typing.TypeVar" podem definir delimitações
(*bounds*) e restrições (*constraints*) com dois pontos (":") seguidos
por uma expressão. Uma única expressão após os dois pontos indica uma
delimitação (por exemplo, "T: int"). Semanticamente, isso significa
que o "typing.TypeVar" pode representar apenas tipos que são um
subtipo desse limite. Uma tupla de expressões entre parênteses após os
dois pontos indica um conjunto de restrições (por exemplo, "T: (str,
bytes)"). Cada membro da tupla deve ser um tipo (novamente, isso não é
imposto em tempo de execução). Variáveis de tipo restrito podem
assumir apenas um dos tipos na lista de restrições.

Para "typing.TypeVar"s declarados usando a sintaxe de lista de
parâmetros de tipo, a delimitação e as restrições não são avaliados
quando o objeto genérico é criado, mas somente quando o valor é
acessado explicitamente por meio dos atributos "__bound__" e
"__constraints__". Para fazer isso, as delimitações ou restrições são
avaliados em um escopo de anotação separado.

"typing.TypeVarTuple"s e "typing.ParamSpec"s não pode ter delimitações
e restrições.

Todas as três espécies de parâmetros de tipo também podem ter um
*valor padrão*, que é usado quando o parâmetro de tipo não é fornecido
explicitamente. Isso é adicionado anexando um único sinal de igual
("=") seguido por uma expressão. Como os limites e restrições de tipos
variáveis, o valor padrão não é avaliado quando o objeto é criado, mas
apenas quando o atributo "__default__" do parâmetro de tipo é
acessado. Para esse fim, o valor padrão é avaliado em um escopo de
anotação separado. Se nenhum valor padrão for especificado para um
parâmetro de tipo, o atributo "__default__" é definido como o objeto
sinalizador especial "typing.NoDefault".

O exemplo a seguir indica o conjunto completo de declarações de
parâmetros de tipo permitidas:

   def overly_generic[
      SimpleTypeVar,
      TypeVarWithBound: int,
      TypeVarWithConstraints: (str, bytes),
      TypeVarWithDefault = int,
      *SimpleTypeVarTuple = (int, float),
      **SimpleParamSpec = (str, bytearray),
   ](
      a: SimpleTypeVar,
      b: TypeVarWithDefault,
      c: TypeVarWithBound,
      d: Callable[SimpleParamSpec, TypeVarWithConstraints],
      *e: SimpleTypeVarTuple,
   ): ...


8.10.1. Funções genéricas
-------------------------

Funções genéricas são declaradas assim:

   def func[T](arg: T): ...

Essa sintaxe é equivalente a:

   annotation-def TYPE_PARAMS_OF_func():
       T = typing.TypeVar("T")
       def func(arg: T): ...
       func.__type_params__ = (T,)
       return func
   func = TYPE_PARAMS_OF_func()

Aqui, "annotation-def" indica um escopo de anotação, que não é
vinculado de verdade a nenhum nome em tempo de execução. (Uma outra
liberdade foi tomada na tradução: essa sintaxe não faz ocorrer um
acesso de atributo no módulo "typing"; ao invés disso é criada uma
instância de "typing.TypeVar" diretamente.)

As anotações das funções genéricas são lidas dentro do escopo de
anotação usado para declarar os parâmetros de tipo, mas os valores
padrão dos argumentos e decoradores da função não são.

Este exemplo ilustra as regras de escopo para estes casos, bem como
para outras espécies de parâmetros de tipo:

   @decorator
   def func[T: int, *Ts, **P](*args: *Ts, arg: Callable[P, T] = some_default):
       ...

Tirando a avaliação preguiçosa da delimitação da "TypeVar", isso é
equivalente a:

   DEFAULT_OF_arg = some_default

   annotation-def TYPE_PARAMS_OF_func():

       annotation-def BOUND_OF_T():
           return int
       # In reality, BOUND_OF_T() is evaluated only on demand.
       T = typing.TypeVar("T", bound=BOUND_OF_T())

       Ts = typing.TypeVarTuple("Ts")
       P = typing.ParamSpec("P")

       def func(*args: *Ts, arg: Callable[P, T] = DEFAULT_OF_arg):
           ...

       func.__type_params__ = (T, Ts, P)
       return func
   func = decorator(TYPE_PARAMS_OF_func())

Os nomes com maiúsculas como "DEFAULT_OF_arg" não são realmente
vinculados em tempo de execução.


8.10.2. Classes genéricas
-------------------------

Classes genéricas são declaradas assim:

   class Bag[T]: ...

Essa sintaxe é equivalente a:

   annotation-def TYPE_PARAMS_OF_Bag():
       T = typing.TypeVar("T")
       class Bag(typing.Generic[T]):
           __type_params__ = (T,)
           ...
       return Bag
   Bag = TYPE_PARAMS_OF_Bag()

Aqui novamente "annotation-def" (não é uma palavra reservada real)
indica um escopo de anotação, e o nome "TYPE_PARAMS_OF_Bag" não é
realmente vinculado em tempo de execução.

Classes genéricas herdam implicitamente de "typing.Generic". As
classes base e os argumentos nomeados de classes genéricas são
avaliados dentro do escopo de tipo para os parâmetros de tipo, e os
decoradores são avaliados fora desse escopo. Isso é ilustrado por este
exemplo:

   @decorator
   class Bag[T](Base[T], arg=T): ...

Isso equivale a:

   annotation-def TYPE_PARAMS_OF_Bag():
       T = typing.TypeVar("T")
       class Bag(Base[T], typing.Generic[T], arg=T):
           __type_params__ = (T,)
           ...
       return Bag
   Bag = decorator(TYPE_PARAMS_OF_Bag())


8.10.3. Apelidos de tipo genérico
---------------------------------

A instrução "type" também pode ser usada para criar um apelido de tipo
genérico:

   type ListOrSet[T] = list[T] | set[T]

Exceto pela avaliação preguiçosa do valor, isso é equivalente a:

   annotation-def TYPE_PARAMS_OF_ListOrSet():
       T = typing.TypeVar("T")

       annotation-def VALUE_OF_ListOrSet():
           return list[T] | set[T]
       # Na realidade, o valor é avaliado preguiçosamente
       return typing.TypeAliasType("ListOrSet", VALUE_OF_ListOrSet(), type_params=(T,))
   ListOrSet = TYPE_PARAMS_OF_ListOrSet()

Aqui, "annotation-def" (não é uma palavra reservada real) indica um
escopo de anotação. Os nomes em maiúsculas como
"TYPE_PARAMS_OF_ListOrSet" não são realmente vinculados em tempo de
execução.


8.11. Anotações
===============

Alterado na versão 3.14: Anotações são agora avaliados preguiçosamente
por padrão.

Variáveis e parâmetros de função podem conter *anotações*, criadas
adicionando dois pontos após o nome, seguidos de uma expressão:

   x: annotation = 1
   def f(param: annotation): ...

As funções também podem ter uma anotação de retorno seguindo uma seta:

   def f() -> annotation: ...

Anotações são convencionalmente usadas para *dicas de tipo*, mas isso
não é imposto pela linguagem e, em geral, anotações podem conter
expressões arbitrárias. A presença de anotações não altera a semântica
de tempo de execução do código, exceto se algum mecanismo for usado
para introspectar e utilizar as anotações (como "dataclasses" ou
"@functools.singledispatch").

Por padrão, as anotações são avaliadas preguiçosamente em um escopo de
anotações. Isso significa que elas não são avaliadas quando o código
que contém a anotação é avaliado. Em vez disso, o interpretador salva
informações que podem ser usadas para avaliar a anotação
posteriormente, se solicitado. O módulo "annotationlib" fornece
ferramentas para avaliar anotações.

Se instrução future "from __future__ import annotations" estiver
presente, todas as anotações serão armazenadas como strings:

   >>> from __future__ import annotations
   >>> def f(param: annotation): ...
   >>> f.__annotations__
   {'param': 'annotation'}

Esta instrução future será descontinuada e removida em uma versão
futura do Python, mas não antes do Python 3.13 chegar ao fim de sua
vida útil (consulte **PEP 749**). Quando usada, ferramentas de
introspecção como "annotationlib.get_annotations()" e
"typing.get_type_hints()" têm menor probabilidade de resolver
anotações em tempo de execução.

-[ Notas de rodapé ]-

[1] A exceção é propagada para a pilha de invocação, a menos que haja
    uma cláusula "finally" que por acaso levante outra exceção. Essa
    nova exceção faz com que a antiga seja perdida.

[2] Na correspondência de padrões, uma sequência é definida como uma
    das seguintes:

    * uma classe que herda de "collections.abc.Sequence"

    * uma classe Python que foi registrada como
      "collections.abc.Sequence"

    * uma classe embutida que tem seu bit "Py_TPFLAGS_SEQUENCE"
      (CPython) definido

    * uma classe que herda de qualquer uma das anteriores

    As seguintes classes de biblioteca padrão são sequências:

    * "array.array"

    * "collections.deque"

    * "list"

    * "memoryview"

    * "range"

    * "tuple"

    Nota:

      Valores de assunto do tipo "str", "bytes" e "bytearray" não
      correspondem aos padrões de sequência.

[3] Na correspondência de padrões, um mapeamento é definido como uma
    das seguintes:

    * uma classe que herda de "collections.abc.Mapping"

    * uma classe Python que foi registrada como
      "collections.abc.Mapping"

    * uma classe embutida que tem seu bit "Py_TPFLAGS_MAPPING"
      (CPython) definido

    * uma classe que herda de qualquer uma das anteriores

    As classes de biblioteca padrão "dict" e "types.MappingProxyType"
    são mapeamentos.

[4] Um literal de string que aparece como a primeira instrução no
    corpo da função é transformado no atributo "__doc__" da função e,
    portanto, no *docstring* da função.

[5] Um literal de string que aparece como a primeira instrução no
    corpo da classe é transformado no item "__doc__" do espaço de
    nomes e, portanto, no *docstring* da classe.
