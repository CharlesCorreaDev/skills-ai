4. Modelo de execução
*********************


4.1. Estrutura de um programa
=============================

Um programa Python é construído a partir de blocos de código. Um
*bloco* é um pedaço do texto do programa Python que é executado como
uma unidade. A seguir estão os blocos: um módulo, um corpo de função e
uma definição de classe. Cada comando digitado interativamente é um
bloco. Um arquivo de script (um arquivo fornecido como entrada padrão
para o interpretador ou especificado como argumento de linha de
comando para o interpretador) é um bloco de código. Um comando de
script (um comando especificado na linha de comando do interpretador
com a opção "-c") é um bloco de código. Um módulo executado sobre um
script de nível superior (como o módulo "__main__") a partir da linha
de comando usando um argumento "-m" também é um bloco de código. O
argumento da string passado para as funções embutidas "eval()" e
"exec()" é um bloco de código.

Um bloco de código é executado em um *quadro de execução*. Um quadro
contém algumas informações administrativas (usadas para depuração) e
determina onde e como a execução continua após a conclusão do bloco de
código.


4.2. Nomeação e ligação
=======================


4.2.1. Ligação de nomes
-----------------------

*Nomes* referem-se a objetos. Os nomes são introduzidos por operações
de ligação de nomes.

As seguintes construções ligam nomes:

* parâmetros formais para funções,

* definições de classe,

* definições de função,

* expressões de atribuição,

* alvos que são identificadores se ocorrerem em uma atribuição:

  * cabeçalho de laço "for",

  * depois de "as" em uma instrução "with", cláusula "except",
    cláusula "except*" ou no padrão as na correspondência de padrões
    estruturais,

  * em um padrão de captura na correspondência de padrões estruturais

* instruções "import".

* instruções "type".

* listas de parâmetros de tipo.

A instrução "import" no formato "from ... import *" liga todos os
nomes definidos no módulo importado, exceto aqueles que começam com um
sublinhado. Este formulário só pode ser usado no nível do módulo.

Um alvo ocorrendo em uma instrução "del" também é considerado ligado a
esse propósito (embora a semântica real seja para desligar do nome).

Cada atribuição ou instrução de importação ocorre dentro de um bloco
definido por uma definição de classe ou função ou no nível do módulo
(o bloco de código de nível superior).

Se um nome está ligado a um bloco, é uma variável local desse bloco, a
menos que declarado como "nonlocal" ou "global". Se um nome está
ligado a nível do módulo, é uma variável global. (As variáveis do
bloco de código do módulo são locais e globais.) Se uma variável for
usada em um bloco de código, mas não definida lá, é uma *variável
livre*.

Cada ocorrência de um nome no texto do programa se refere à *ligação*
daquele nome estabelecido pelas seguintes regras de resolução de nome.


4.2.2. Resolução de nomes
-------------------------

O *escopo* define a visibilidade de um nome dentro de um bloco. Se uma
variável local é definida em um bloco, seu escopo inclui esse bloco.
Se a definição ocorrer em um bloco de função, o escopo se estende a
quaisquer blocos contidos no bloco de definição, a menos que um bloco
contido introduza uma ligação diferente para o nome.

Quando um nome é usado em um bloco de código, ele é resolvido usando o
escopo envolvente mais próximo. O conjunto de todos esses escopos
visíveis a um bloco de código é chamado de *ambiente* do bloco.

Quando um nome não é encontrado, uma exceção "NameError" é levantada.
Se o escopo atual for um escopo de função e o nome se referir a uma
variável local que ainda não foi associada a um valor no ponto onde o
nome é usado, uma exceção "UnboundLocalError" é levantada.
"UnboundLocalError" é uma subclasse de "NameError".

Se a operação de ligação de nomes ocorre dentro de um bloco de código,
todos os usos do nome dentro do bloco são tratadas como referências
para o bloco atual. Isso pode. Isso pode levar a erros quando um nome
é usado em um bloco antes de ser vinculado.  Esta regra é sutil.
Python carece de declarações e permite que as operações de ligação de
nomes ocorram em qualquer lugar dentro de um bloco de código. As
variáveis locais de um bloco de código podem ser determinadas pela
varredura de todo o texto do bloco para operações de ligação de nome.
Veja o FAQ sobre UnboundLocalError para exemplos.

Se a instrução "global" ocorrer dentro de um bloco, todos os usos dos
nomes especificados na instrução referem-se às ligações desses nomes
no espaço de nomes de nível superior. Os nomes são resolvidos no
espaço de nomes de nível superior pesquisando o espaço de nomes
global, ou seja, o espaço de nomes do módulo que contém o bloco de
código, e o espaço de nomes embutido, o espaço de nomes do módulo
"builtins". O espaço de nomes global é pesquisado primeiro. Se os
nomes não forem encontrados lá, o espaço de nomes embutidos será
pesquisado em seguida. Se os nomes também não forem encontrados no
espaço de nomes embutido, novas variáveis são criadas no espaço de
nomes global. A instrução global deve preceder todos os usos dos nomes
listados.

A instrução "global" tem o mesmo escopo que uma operação de ligação de
nome no mesmo bloco. Se o escopo mais próximo de uma variável livre
contiver uma instrução global, a variável livre será tratada como
global.

A instrução "nonlocal" faz com que os nomes correspondentes se refiram
a variáveis previamente vinculadas no escopo da função delimitadora
mais próxima. A exceção "SyntaxError" é levantada em tempo de
compilação se o nome fornecido não existir em nenhum escopo de função
delimitador. Parâmetros de tipo não podem ser vinculadas novamente com
a instrução "nonlocal".

O espaço de nomes de um módulo é criado automaticamente na primeira
vez que um módulo é importado. O módulo principal de um script é
sempre chamado de "__main__".

Blocos de definição de classe e argumentos para "exec()" e "eval()"
são especiais no contexto de resolução de nome. Uma definição de
classe é uma instrução executável que pode usar e definir nomes. Essas
referências seguem as regras normais para resolução de nome, com
exceção de que variáveis locais não vinculadas são pesquisadas no
espaço de nomes global global. O espaço de nomes global da definição
de classe se torna o dicionário de atributos da classe. O escopo dos
nomes definidos em um bloco de classe é limitado ao bloco de classe;
ele não se estende aos blocos de código de métodos. Isso inclui
compreensões e expressões geradoras, mas não inclui escopos de
anotação, que têm acesso a seus escopos de classe delimitadores. Isso
significa que o seguinte falhará:

   class A:
       a = 42
       b = list(a + i for i in range(10))

Porém, o seguinte vai funcionar:

   class A:
       type Alias = Nested
       class Nested: pass

   print(A.Alias.__value__)  # <type 'A.Nested'>


4.2.3. Escopos de anotação
--------------------------

As instruções de *anotações*, listas de parâmetros de tipo e "type"
introduzem *escopos de anotação*, que se comportam principalmente como
escopos de função, mas com algumas exceções discutidas abaixo.

Os escopos de anotação são usados nos seguintes contextos:

* *Anotações de funções*.

* *Anotações de variável*.

* Listas de parâmetros de tipo para apelidos de tipo genérico.

* Listas de parâmetros de tipo para funções genéricas. As anotações de
  uma função genérica são executadas dentro do escopo de anotação, mas
  seus padrões e decoradores não.

* Listas de parâmetros de tipo para classes genéricas. As classes base
  e argumentos nomeados de uma classe genérica são executadas dentro
  do escopo de anotação, mas seus decoradores não.

* Os limites, restrições e valores padrão para parâmetros de tipo
  (avaliados preguiçosamente).

* O valor dos apelidos de tipo (avaliado preguiçosamente).

Escopos de anotação diferenciam-se de escopos de função nas seguintes
formas:

* Os escopos de anotação têm acesso ao espaço de nomes da classe
  delimitadora. Se um escopo de anotação estiver imediatamente dentro
  de um escopo de classe ou dentro de outro escopo de anotação que
  esteja imediatamente dentro de um escopo de classe, o código no
  escopo de anotação poderá usar nomes definidos no escopo de classe
  como se fosse executado diretamente no corpo da classe. Isto
  contrasta com funções regulares definidas dentro de classes, que não
  podem acessar nomes definidos no escopo da classe.

* Expressões em escopos de anotação não podem conter expressões
  "yield", "yield from", "await" ou ":=". (Essas expressões são
  permitidas em outros escopos contidos no escopo de anotação.)

* Nomes definidos em escopos de anotação não podem ser vinculados
  novamente com instruções "nonlocal" em escopos internos. Isso inclui
  apenas parâmetros de tipo, pois nenhum outro elemento sintático que
  pode aparecer nos escopos de anotação pode introduzir novos nomes.

* Embora os escopos de anotação tenham um nome interno, esse nome não
  é refletido no *nome qualificado* dos objetos definidos dentro do
  escopo. Em vez disso, o "__qualname__" de tais objetos é como se o
  objeto fosse definido no escopo delimitador.

Adicionado na versão 3.12: Escopos de anotação foram introduzidos no
Python 3.12 como parte da **PEP 695**.

Alterado na versão 3.13: Os escopos de anotação também são usados para
padrões de parâmetros de tipo, conforme introduzido pela **PEP 696**.

Alterado na versão 3.14: Os escopos de anotação agora também são
usados para anotações, conforme especificado na **PEP 649** e **PEP
749**.


4.2.4. Avaliação preguiçosa
---------------------------

A maioria dos escopos de anotação são *avaliados preguiçosamente*.
Isso inclui anotações, os valores de apelidos de tipo criados por meio
da instrução "type" e os limites, restrições e valores padrão de tipos
variáveis criados por meio da sintaxe de parâmetro de tipo sintaxe de
parâmetro de tipo. Isso significa que eles não são avaliados quando o
apelido de tipo ou a tipo variável é criado, ou quando o objeto que
contém as anotações é criado. Em vez disso, eles são avaliados apenas
quando necessário, por exemplo, quando o atributo "__value__" em um
apelido de tipo é acessado.

Exemplo:

   >>> type Alias = 1/0
   >>> Alias.__value__
   Traceback (most recent call last):
     ...
   ZeroDivisionError: division by zero
   >>> def func[T: 1/0](): pass
   >>> T = func.__type_params__[0]
   >>> T.__bound__
   Traceback (most recent call last):
     ...
   ZeroDivisionError: division by zero

Aqui a exceção é levantada apenas quando o atributo "__value__" do
apelido de tipo ou o atributo "__bound__" da variável de tipo é
acessado.

Esse comportamento é útil principalmente para referências a tipos que
ainda não foram definidos quando o alias de tipo ou variável de tipo é
criado. Por exemplo, a avaliação preguiçosa permite a criação de
apelidos de tipo mutuamente recursivos:

   from typing import Literal

   type SimpleExpr = int | Parenthesized
   type Parenthesized = tuple[Literal["("], Expr, Literal[")"]]
   type Expr = SimpleExpr | tuple[SimpleExpr, Literal["+", "-"], Expr]

Valores avaliados preguiçosamente são avaliados em escopo de anotação,
o que significa que os nomes que aparecem dentro do valor avaliado
preguiçosamente são pesquisados como se fossem usados no escopo
imediatamente envolvente.

Adicionado na versão 3.12.


4.2.5. Builtins e execução restrita
-----------------------------------

Os usuários não devem tocar em "__builtins__"; é estritamente um
detalhe de implementação. Usuários que desejam substituir valores no
espaço de nomes interno devem "import" o módulo "builtins" e modificar
seus atributos apropriadamente.

O espaço de nomes builtins associado com a execução de um bloco de
código é encontrado procurando o nome "__builtins__" em seu espaço de
nomes global; este deve ser um dicionário ou um módulo (no último
caso, o dicionário do módulo é usado). Por padrão, quando no módulo
"__main__", "__builtins__" é o módulo embutido "builtins"; quando em
qualquer outro módulo, "__builtins__" é um apelido para o dicionário
do próprio módulo "builtins".


4.2.6. Interação com recursos dinâmicos
---------------------------------------

A resolução de nome de variáveis livres ocorre em tempo de execução,
não em tempo de compilação. Isso significa que o código a seguir
imprimirá 42:

   i = 10
   def f():
       print(i)
   i = 42
   f()

As funções "eval()" e "exec()" não têm acesso ao ambiente completo
para resolução de nome. Os nomes podem ser resolvidos nos espaços de
nomes locais e globais do chamador. Variáveis livres não são
resolvidas no espaço de nomes mais próximo, mas no espaço de nomes
global. [1] As funções "exec()" e "eval()" possuem argumentos
opcionais para substituir o espaço de nomes global e local. Se apenas
um espaço de nomes for especificado, ele será usado para ambos.


4.3. Exceções
=============

As exceções são um meio de romper o fluxo normal de controle de um
bloco de código para tratar erros ou outras condições excepcionais.
Uma exceção é *levantada* no ponto em que o erro é detectado; ele pode
ser *tratado* pelo bloco de código circundante ou por qualquer bloco
de código que invocou direta ou indiretamente o bloco de código onde
ocorreu o erro.

O interpretador Python levanta uma exceção quando detecta um erro em
tempo de execução (como divisão por zero). Um programa Python também
pode levantar explicitamente uma exceção com a instrução "raise". Os
tratadores de exceção são especificados com a instrução "try" ...
"except". A cláusula "finally" de tal declaração pode ser usada para
especificar o código de limpeza que não trata a exceção, mas é
executado se uma exceção ocorreu ou não no código anterior.

Python usa o modelo de "terminação" da manipulação de erros: um
manipulador de exceção pode descobrir o que aconteceu e continuar a
execução em um nível externo, mas não pode reparar a causa do erro e
tentar novamente a operação com falha (exceto reinserindo a parte
incorreta de código de cima).

Quando uma exceção não é manipulada, o interpretador encerra a
execução do programa ou retorna ao seu laço principal interativo. Em
ambos os casos, ele exeibe um traceback (situação da pilha de
execução), exceto quando a exceção é "SystemExit".

As exceções são identificadas por instâncias de classe. A cláusula
"except" é selecionada dependendo da classe da instância: ela deve
referenciar a classe da instância ou uma *classe base não-virtual*
dela. A instância pode ser recebida pelo manipulador e pode conter
informações adicionais sobre a condição excepcional.

Nota:

  As mensagens de exceção não fazem parte da API do Python. Seu
  conteúdo pode mudar de uma versão do Python para outra sem aviso e
  não deve ser invocado pelo código que será executado em várias
  versões do interpretador.

Veja também a descrição da declaração "try" na seção A instrução try e
a instrução "raise" na seção A instrução raise.


4.4. Componentes do Ambiente de Execução
========================================


4.4.1. Modelo Geral de Computação
---------------------------------

O modelo de execução do Python não opera no vácuo. Ele é executado em
uma máquina hospedeira e através do ambiente de execução desse
hospedeiro, incluindo seu sistema operacional (SO), se houver um.
Quando um programa é executado, as camadas conceituais de como ele é
executado no hospedeiro têm esta forma:

      **máquina hospedeira**
         **processo** (recursos globais)
            **thread** (executa código de máquina)

Cada processo representa um programa rodando no hospdeiro. Pense em
cada processo em si como a parte do programa referente aos dados.
Pense nas threads do processo como a parte referente à execução. Essa
distinção será importante para entender o ambiente de execução do
Python.

O processo, enquanto parte referente a dados, é o contexto de execução
sobre o qual o programa roda. Ele consiste majoritariamente no
conjunto de recursos alocados paro programa pelo hospedeiro, incluindo
memória, sinais, identificadores de arquivos, soquetes, e variáveis de
ambiente.

Processos são isolados, e independentes uns dos outros. (O mesmo vale
para hospedeiros.) O hospedeiro gerencia o acesso do processo aos
recursos a ele alocados, além de orquestrar os vários processos.

Cada thread representa a execução em si do código de máquina do
programa, rodando relativamente aos recursos alocados ao processo.
Decidir como e quando essa execução acontecerá é prerrogativa
exclusiva do hospedeiro.

Do ponto de vista do Python, um programa sempre começa com exatamente
uma thread. Entretanto, o programa pode evoluir para rodar em
múltiplas threads simultâneas. Nem todo hospedeiro oferece suporte
para múltiplas threads por processo, mas a maioria oferece.
Diferentemente de processos, threads em um processo não são isoladas
nem independentes umas das outras. Especificamente, cada recurso de um
processo é compartilhado por todas as suas threads.

O princípio fundamental das threads é que cada uma delas *roda*
independentemente, ao mesmo tempo que as outras. Isso pode significar
uma simultaneidade conceitual ("concorrência") ou física
("paralelismo"). De qualquer modo, as threads rodam efetivamente em
passos não sincronizados.

Nota:

  Essa falta de sincronismo significa que não existe nenhuma garantia
  de consistência em qualquer parte da memória do processo, do ponto
  de vista do código rodando em qualquer thread. Portanto, programas
  multi-thread precisam tomar o cuidado de coordenar o acesso a
  recursos intencionalmente compartilhados. Da mesma forma, eles
  precisam ter o máximo cuidado para não acessar nenhum *outro*
  recurso a partir de múltiplas threads; caso contrário, duas threads
  rodando ao mesmo tempo podem acidentalmente interferir no uso umas
  das outras desses recursos compartilhados. Tudo isso vale tanto para
  programas Python quanto para o ambiente de execução do Python.Essa
  exigência ampla e não estruturada é o custo que precisamos pagar em
  contrapartida pela concorrência bruta que as threads proporcionam. A
  alternativa à disciplina necessária geralmente envolve lidar com
  bugs não determinísticos e corrupção de dados.


4.4.2. Modelo do Ambiente de Execução Python
--------------------------------------------

As mesmas camadas conceituais se aplicam a cada programa Python, com
algumas camadas de dados específicas para o Python:

      **máquina hospedeira**
         **processo** (recursos globais)
            Ambiente de execução global do Python (*estado*)
               Interpretador Python (*estado*)
                  **thread** (roda bytecode Python e a "API C")
                     *Estado* da thread Python

No nível conceitual: quando um programa Python começa, ele tem o
aspecto exato desse diagrama, com uma instância de cada linha. O
ambiente de execução pode evoluir para incluir múltiplos
interpretadores, e cada interpretador pode evoluir para incluir
múltiplos estados de thread.

Nota:

  Uma implementação do Python não necessariamente vai implementar
  essas camadas do ambiente de execução de forma distinta, ou mesmo
  concreta. A única exceção são os casos em que camadas distintas são
  diretamente especificadas ou expostas aos usuários, como através do
  módulo "threading".

Nota:

  O interpretador inicial é geralmente chamado de interpretador
  "principal". Algumas implementações do Python, como o CPython, dão
  papéis especiais ao interpretador principal.Da mesma forma, a thread
  do hospedeiro na qual o ambiente de execução foi inicializado é
  chamada de thread "principal". Ela pode ser diferente da thread
  inicial do processo, embora geralmente sejam a mesma. Em alguns
  casos, o termo "thread principal" pode ser ainda mais específico, e
  se referir ao estado de thread inicial. Um ambiente de execução
  Python pode atribuir responsabilidades especiais à thread principal,
  como por exemplo lidar com sinais.

Em sua totalidade, o ambiente de execução Python consiste no seu
estado global, seus interpretadores, e seus estados de thread. O
ambiente de execução garante que todo esse estado permaneça
consistente ao longo do seu tempo de vida, em particular quando usado
a partir de múltiplas threads do hospedeiro.

O ambiente de execução global, conceitualmente, é simplesmente um
conjunto de interpretadores. Esses interpretadores podem compartilhar
alguns dados e outros recursos, mas fora isso são isolados e
independentes uns dos outros. O ambiente de execução é responsável por
gerenciar esses recursos globais de forma segura. A natureza física
desses recursos, bem como o seu gerenciamento, é específica de cada
implementação. No fim das contas, a utilidade externa do ambiente de
execução global é limitada ao gerenciamento de interpretadores.

Em contraste, conceitualmente um "interpretador" é o que normalmente
consideraríamos como sendo o "ambiente de execução Python" (com todas
as suas funcionalidades). Quando código de máquina, sendo executado em
uma thread do hospedeiro, interage com o ambiente de execução Python,
ele chama o Python no contexto de um interpretador específico.

Nota:

  O termo interpretador aqui não é a mesma coisa que o "interpretador
  de bytecode", que é o que normalmente roda nas threads, executando
  código Python compilado.Em um mundo ideal, o termo "ambiente de
  execução Python" seria usado para se referir ao que atualmente
  chamamos de "interpretador". Entretanto, ele vem sendo chamado de
  "interpretador" pelo menos desde que foi introduzido em 1997
  (CPython:a027efa5b).

Cada interpretador encapsula completamente todo o estado necesssário
para o ambiente de execução do Python funcionar, que não seja global
do processo nem específico de threads. Notavelmente, o estado do
interpretador persiste entre usos. Ele inclui dados fundamentais, como
o "sys.modules". O ambiente de execução garante que múltiplas threads
usando o mesmo interpretador vão compartilhá-lo de maneira segura.

Uma implementação do Python pode oferecer suporte para usar múltiplos
interpretadores ao mesmo tempo no mesmo processo. Eles são
independentes e isolados uns dos outros. Por exemplo, cada
interpretador tem o seu próprio "sys.modules".

Quanto aos estados específicos ao ambiente de execução de cada thread,
cada interpretador gerencia um conjunto de estados de thread, da mesma
maneira que o ambiente de execução global contém um conjunto de
interpretadores. Cada interpretador pode ter estados de thread para
quantas threads do hospedeiro forem necessárias. Ele pode até mesmo
ter múltiplos estados de thread para uma mesma thread do hospedeiro,
embora isso não seja tão comum.

Conceitualmente, cada estado de thread contém os dados do ambiente de
execução específicos àquela thread que são necessários para o
interpretador operar em uma thread do hospedeiro. O estado de thread
inclui a exceção atualmente levantada e a pilha de chamadas Python da
thread. Ele pode incluir outros recursos específicos à thread.

Nota:

  O termo "thread Python" pode às vezes se referir ao estado de
  thread, mas normalmente significa uma thread criada a partir do
  módulo "threading".

Cada estado de thread, ao longo do seu tempo de vida, está sempre
atrelado a exatamente um interpretador e uma thread do hospedeiro. Ele
sempre vai ser usado somente naquela thread e com aquele
interpretador.

Múltiplos estados de thread podem estar atrelados à mesma thread do
hospedeiro, seja para diferentes interpretadores ou até mesmo para um
mesmo interpretador. Entretanto, dada qualquer thread do hospedeiro,
somente um dos estados de thread atrelados a ela pode ser usado por
ela de cada vez.

Estados de thread são isolados e independentes uns dos outros e não
compartilham dados, exceto que podem compartilhar o interpretador e
objetos ou outros recursos que pertencem ao interpretador.

Quando um programa está rodando, novas threads Python podem ser
criadas a partir do módulo "threading" (em plataformas e
implementações do Python que ofereçam suporte a threads). Processos
adicionais podem ser criados usando os módulos "os", "subprocess" e
"multiprocessing". Interpretadores podem ser criados e usados com o
módulo "interpreters". Corrotinas (async) podem ser executadas usando
"asyncio" em cada interpretador, tipicamente em uma única thread
(geralmente a thread principal).

-[ Notas de rodapé ]-

[1] Essa limitação ocorre porque o código executado por essas
    operações não está disponível no momento em que o módulo é
    compilado.
