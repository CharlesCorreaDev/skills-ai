FAQ sobre design e histórico
****************************


Por que o Python usa indentação para agrupamento de instruções?
===============================================================

Guido van Rossum acredita que usar indentação para agrupamento é
extremamente elegante e contribui muito para a clareza de programa
Python mediano. Muitas pessoas aprendem a amar esta ferramenta depois
de um tempo.

Uma vez que não há colchetes de início / fim, não pode haver um
desacordo entre o agrupamento percebido pelo analisador sintático e
pelo leitor humano. Ocasionalmente, programadores C irão encontrar um
fragmento de código como este:

   if (x <= y)
           x++;
           y--;
   z++;

Somente a instrução "x++" é executada se a condição for verdadeira,
mas a indentação leva muitos a acreditarem no contrário. Com
frequência, até programadores C experientes a observam fixamente por
um longo tempo, perguntando-se por que "y" está sendo decrementada até
mesmo para "x > y".

Como não há chaves de início / fim, o Python é muito menos propenso a
conflitos no estilo de codificação. Em C, existem muitas maneiras
diferentes de colocar as chaves. Depois de se tornar habitual a
leitura e escrita de código usando um estilo específico, é normal
sentir-se um pouco receoso ao ler (ou precisar escrever) em um estilo
diferente.

Muitos estilos de codificação colocam chaves de início / fim em uma
linha sozinhos. Isto torna os programas consideravelmente mais longos
e desperdiça espaço valioso na tela, dificultando a obtenção de uma
boa visão geral de um programa. Idealmente, uma função deve caber em
uma tela (digamos, 20 a 30 linhas). 20 linhas de Python podem fazer
muito mais trabalho do que 20 linhas de C. Isso não se deve apenas à
falta de colchetes de início/fim -- a falta de declarações e os tipos
de dados de alto nível também são responsáveis -- mas a sintaxe
baseada em indentação certamente ajuda.


Por que eu estou recebendo resultados estranhos com simples operações aritméticas?
==================================================================================

Veja a próxima questão.


Por que o cálculo de pontos flutuantes são tão imprecisos?
==========================================================

Usuários são frequentemente surpreendidos por resultados como este:

   >>> 1.2 - 1.0
   0.19999999999999996

e pensam que isto é um bug do Python. Não é não. Isto tem pouco a ver
com o Python, e muito mais a ver com como a estrutura da plataforma
lida com números em ponto flutuante.

O tipo "float" no CPython usa um "double" do C para armazenamento. O
valor de um objeto "float" é armazenado em ponto flutuante binário com
uma precisão fixa (normalmente 53 bits) e Python usa operações C, que
por sua vez dependem da implementação de hardware no processador, para
realizar operações de ponto flutuante. Isso significa que, no que diz
respeito às operações de ponto flutuante, Python se comporta como
muitas linguagens populares, incluindo C e Java.

Muitos números podem ser escritos facilmente em notação decimal, mas
não podem ser expressados exatamente em ponto flutuante binário. Por
exemplo, após:

   >>> x = 1.2

o valor armazenado para "x" é uma (ótima) aproximação para o valor
decimal "1.2", mas não é exatamente igual. Em uma máquina típica, o
valor real armazenado é:

   1.0011001100110011001100110011001100110011001100110011 (binário)

que é exatamente:

   1.1999999999999999555910790149937383830547332763671875 (decimal)

A precisão típica de 53 bits fornece floats do Python com precisão de
15 a 16 dígitos decimais.

Para uma explicação mais completa, consulte o capítulo de aritmética
de ponto flutuante no tutorial Python.


Por que strings do Python são imutáveis?
========================================

Existem várias vantagens.

Uma delas é o desempenho: saber que uma string é imutável significa
que podemos alocar espaço para ela no momento da criação, e os
requisitos de armazenamento são fixos e imutáveis. Esta é também uma
das razões para a distinção entre tuplas e listas.

Outra vantagem é que strings em Python são consideradas tão
“elementares” quanto números. Nenhuma atividade alterará o valor 8
para qualquer outra coisa e, em Python, nenhuma atividade alterará a
string “oito” para qualquer outra coisa.


Por que o 'self' deve ser usado explicitamente em definições de método e chamadas?
==================================================================================

A ideia foi emprestada do Modula-3. Acontece dela ser muito útil, por
vários motivos.

Primeiro, é mais óbvio que você está usando um método ou atributo de
instância em vez de uma variável local. Ler "self.x" ou "self.meth()"
deixa absolutamente claro que uma variável de instância ou método é
usado mesmo se você não souber a definição da classe de cor. Em C++,
você pode perceber pela falta de uma declaração de variável local
(presumindo que globais são raras ou facilmente reconhecíveis) -- mas
no Python não há declarações de variáveis locais, então você teria que
procurar a definição de classe para tenha certeza. Alguns padrões de
codificação C++ e Java exigem que atributos de instância tenham um
prefixo "m_", portanto, essa explicitação ainda é útil nessas
linguagens também.

Segundo, significa que nenhuma sintaxe especial é necessária se você
quiser referenciar ou chamar explicitamente o método de uma classe
específica. Em C++, se você quiser usar um método de uma classe base
que é substituído em uma classe derivada, você deve usar o operador
"::" -- no Python, você pode escrever "baseclass.methodname(self,
<lista de argumentos>)". Isto é particularmente útil para métodos
"__init__()" e, em geral, em casos onde um método de classe derivada
deseja estender o método da classe base de mesmo nome e, portanto,
precisa chamar o método da classe base de alguma forma.

Finalmente, por exemplo, variáveis, ele resolve um problema sintático
com atribuição: uma vez que variáveis locais em Python são (por
definição!) aquelas variáveis às quais um valor é atribuído em um
corpo de função (e que não são explicitamente declaradas globais), é
necessário deve haver alguma forma de dizer ao interpretador que uma
atribuição deveria ser atribuída a uma variável de instância em vez de
a uma variável local, e deve ser preferencialmente sintática (por
razões de eficiência). C++ faz isso através de declarações, mas Python
não possui declarações e seria uma pena ter que introduzi-las apenas
para esse fim. Usar o "self.var" explícito resolve isso muito bem. Da
mesma forma, para usar variáveis de instância, ter que escrever
"self.var" significa que referências a nomes não qualificados dentro
de um método não precisam pesquisar nos diretórios da instância. Em
outras palavras, variáveis locais e variáveis de instância residem em
dois espaço de nomes diferentes, e você precisa informar ao Python
qual espaço de nomes usar.


Por que não posso usar uma atribuição em uma expressão?
=======================================================

A partir do Python 3.8, você pode!

Expressões de atribuição usando o operador morsa ":=" atribuem uma
variável em uma expressão:

   while chunk := fp.read(200):
      print(chunk)

Veja **PEP 572** para mais informações.


Por que o Python usa métodos para algumas funcionalidades (ex: lista.index()) mas funções para outras (ex: len(lista))?
=======================================================================================================================

Como Guido disse:

   (a) For some operations, prefix notation just reads better than
   postfix -- prefix (and infix!) operations have a long tradition in
   mathematics which likes notations where the visuals help the
   mathematician thinking about a problem. Compare the easy with which
   we rewrite a formula like x*(a+b) into x*a + x*b to the clumsiness
   of doing the same thing using a raw OO notation.

   (b) When I read code that says len(x) I *know* that it is asking
   for the length of something. This tells me two things: the result
   is an integer, and the argument is some kind of container. To the
   contrary, when I read x.len(), I have to already know that x is
   some kind of container implementing an interface or inheriting from
   a class that has a standard len(). Witness the confusion we
   occasionally have when a class that is not implementing a mapping
   has a get() or keys() method, or something that isn't a file has a
   write() method.

   -- https://mail.python.org/pipermail/python-3000/2006-November/004
   643.html


Por que o join() é um método de string em vez de ser um método de lista ou tupla?
=================================================================================

Strings se tornaram muito parecidas com outros tipos padrão a partir
do Python 1.6, quando métodos que dão a mesma funcionalidade que
sempre esteve disponível utilizando as funções do módulo de string
foram adicionados. A maior parte desses novos métodos foram amplamente
aceitos, mas o que parece deixar alguns programadores desconfortáveis
é:

   ", ".join(['1', '2', '4', '8', '16'])

que dá o resultado:

   "1, 2, 4, 8, 16"

Existem dois argumentos comuns contra esse uso.

O primeiro segue as linhas de: "Parece muito feio usar um método de
uma string literal (constante de string)", para o qual a resposta é
que pode, mas uma string literal é apenas um valor fixo. Se os métodos
devem ser permitidos em nomes vinculados a strings, não há razão
lógica para torná-los indisponíveis em literais.

A segunda objeção é normalmente formulada como: "Na verdade, estou
dizendo a uma sequência para unir seus membros com uma constante de
string". Infelizmente, você não está. Por alguma razão parece haver
muito menos dificuldade em ter "split()" como um método string, já que
nesse caso é fácil ver que

   "1, 2, 4, 8, 16".split(", ")

é uma instrução para uma string literal para retornar as substrings
delimitadas pelo separador fornecido (ou, por padrão, execuções
arbitrárias de espaço em branco).

"join()" é um método de string porque ao usá-lo você está dizendo à
string separadora para iterar sobre uma sequência de strings e se
inserir entre elementos adjacentes. Este método pode ser usado com
qualquer argumento que obedeça às regras para objetos sequência,
incluindo quaisquer novas classes que você mesmo possa definir.
Existem métodos semelhantes para bytes e objetos bytearray.


Quão rápidas são as exceções?
=============================

Um bloco "try"/"except" é extremamente eficiente se nenhuma exceção
for levantada. Na verdade, capturar uma exceção é caro. Nas versões do
Python anteriores à 2.0 era comum usar esta expressão:

   try:
       value = mydict[key]
   except KeyError:
       mydict[key] = getvalue(key)
       value = mydict[key]

Isso somente fazia sentido quando você esperava que o dicionário
tivesse uma chave quase que toda vez. Se esse não fosse o caso, você
escrevia desta maneira:

   if key in mydict:
       value = mydict[key]
   else:
       value = mydict[key] = getvalue(key)

Para este caso específico, você também pode usar "value =
dict.setdefault(key, getvalue(key))", mas apenas se a chamada
"getvalue()" tiver pouco custosa o suficiente porque é avaliada em
todos os casos.


Por que não existe uma instrução de switch ou case no Python?
=============================================================

Em geral, as instruções switch estruturadas executam um bloco de
código quando uma expressão possui um valor ou conjunto de valores
específico. Desde o Python 3.10 é possível combinar facilmente valores
literais, ou constantes dentro de um espaço de nomes, com uma
instrução "match ... case". Veja a especificação e o tutorial para
mais informações sobre instruções "match". Uma alternativa mais antiga
é uma sequência de "if... elif... elif... else".

Para casos em que você precisa escolher entre um grande número de
possibilidades, você pode criar um dicionário mapeando valores de caso
para funções a serem chamadas. Por exemplo:

   functions = {'a': function_1,
                'b': function_2,
                'c': self.method_1}

   func = functions[value]
   func()

Para chamar métodos em objetos, você pode simplificar ainda mais
usando olá função embutida "getattr()" para recuperar métodos com um
nome específico:

   class MyVisitor:
       def visit_a(self):
           ...

       def dispatch(self, value):
           method_name = 'visit_' + str(value)
           method = getattr(self, method_name)
           method()

É sugerido que você use um prefixo para os nomes dos métodos, como
"visit_" neste exemplo. Sem esse prefixo, se os valores vierem de uma
fonte não confiável, um invasor poderá chamar qualquer método no seu
objeto.

Imitar o comportamento do switch no C, em que a execução atravessa as
instruções de um case para outro caso não seja interrompida, é
possível, mais difícil, e menos necessário.


Você não pode emular threads no interpretador em vez de confiar em uma implementação de thread específica do sistema operacional?
=================================================================================================================================

Resposta 1: Infelizmente, o interpretador envia pelo menos um quadro
de pilha C para cada quadro de pilha Python. Além disso, as extensões
podem retornar ao Python em momentos quase aleatórios. Portanto, uma
implementação completa de threads requer suporte de thread para C.

Resposta 2: Felizmente, existe o Stackless Python, que tem um laço de
interpretador completamente redesenhado que evita a pilha C.


Por que expressões lambda não podem conter instruções?
======================================================

Expressões lambda no Python não podem conter instruções porque o
framework sintático do Python não consegue manipular instruções
aninhadas dentro de expressões. No entanto, no Python, isso não é um
problema sério. Diferentemente das formas de lambda em outras
linguagens, onde elas adicionam funcionalidade, lambdas de Python são
apenas notações simplificadas se você tiver muita preguiça de definir
uma função.

Funções já são objetos de primeira classe em Python, e podem ser
declaradas em um escopo local. Portanto a única vantagem de usar um
lambda em vez de uma função definida localmente é que você não precisa
inventar um nome para a função -- mas esta só é uma variável local
para a qual o objeto da função (que é exatamente do mesmo tipo de um
objeto que uma expressão lambda carrega) é atribuído!


O Python pode ser compilado para linguagem de máquina, C ou alguma outra linguagem?
===================================================================================

O Cython compila uma versão modificada do Python com anotações
opcionais em extensões C. Nuitka é um compilador emergente de Python
em código C++, com o objetivo de oferecer suporte à linguagem Python
completa.


Como o Python gerencia memória?
===============================

Os detalhes do gerenciamento de memória Python dependem da
implementação. A implementação padrão do Python, *CPython*, usa
contagem de referências para detectar objetos inacessíveis, e outro
mecanismo para coletar ciclos de referência, executando periodicamente
um algoritmo de detecção de ciclo que procura por ciclos inacessíveis
e exclui os objetos envolvidos. O módulo "gc" fornece funções para
realizar uma coleta de lixo, obter estatísticas de depuração e ajustar
os parâmetros do coletor.

Outras implementações (como Jython ou PyPy), no entanto, podem contar
com um mecanismo diferente, como um coletor de lixo maduro. Essa
diferença pode causar alguns problemas sutis de portabilidade se o seu
código Python depender do comportamento da implementação de contagem
de referências.

Em algumas implementações do Python, o código a seguir (que funciona
bem no CPython) provavelmente ficará sem descritores de arquivo:

   for file in very_long_list_of_files:
       f = open(file)
       c = f.read(1)

Na verdade, usando o esquema de contagem de referências e destrutor de
referências do CPython, cada nova atribuição a "f" fecha o arquivo
anterior. Com um GC tradicional, entretanto, esses objetos arquivo só
serão coletados (e fechados) em intervalos variados e possivelmente
longos.

Se você quiser escrever um código que funcione com qualquer
implementação Python, você deve fechar explicitamente o arquivo ou
usar a instrução "with"; isso funcionará independentemente do esquema
de gerenciamento de memória:

   for file in very_long_list_of_files:
       with open(file) as f:
           c = f.read(1)


Por que o CPython não usa uma forma mais tradicional de esquema de coleta de lixo?
==================================================================================

Por um lado, este não é um recurso padrão C e, portanto, não é
portátil. (Sim, sabemos sobre a biblioteca Boehm GC. Ela possui
pedaços de código assembler para a *maioria* das plataformas comuns,
não para todas elas, e embora seja em sua maioria transparente, não é
completamente transparente; são necessários patches para obter Python
para trabalhar com isso.)

O GC tradicional também se torna um problema quando o Python é
incorporado em outros aplicativos. Embora em um Python independente
seja bom substituir o padrão "malloc()" e "free()" por versões
fornecidas pela biblioteca GC, uma aplicação que incorpora Python pode
querer ter seu *próprio* substituto para "malloc()" e "free()", e
podem não querer Python. No momento, CPython funciona com qualquer
coisa que implemente "malloc()" e "free()" corretamente.


Por que toda memória não é liberada quando o CPython fecha?
===========================================================

Os objetos referenciados nos espaço de nomes globais dos módulos
Python nem sempre são desalocados quando o Python é encerrado. Isso
pode acontecer se houver referências circulares. Existem também certos
bits de memória alocados pela biblioteca C que são impossíveis de
liberar (por exemplo, uma ferramenta como o Purify reclamará disso).
Python é, no entanto, agressivo quanto à limpeza de memória na saída e
tenta destruir todos os objetos.

Se você quiser forçar o Python a excluir certas coisas na desalocação,
use o módulo "atexit" para executar uma função que forçará essas
exclusões.


Por que existem tipos de dados separados para tuplas e listas?
==============================================================

Listas e tuplas, embora semelhantes em muitos aspectos, geralmente são
usadas de maneiras fundamentalmente diferentes. Tuplas podem ser
consideradas semelhantes a "records" de Pascal ou "structs" de C; são
pequenas coleções de dados relacionados que podem ser de diferentes
tipos e operados como um grupo. Por exemplo, uma coordenada cartesiana
é representada apropriadamente como uma tupla de dois ou três números.

As listas, por outro lado, são mais parecidas com arrays em outras
linguagens. Eles tendem a conter um número variável de objetos, todos
do mesmo tipo e operados um por um. Por exemplo, "os.listdir('.')"
retorna uma lista de strings representando os arquivos no diretório
atual. Funções que operam nesta saída geralmente não seriam
interrompidas se você adicionasse outro arquivo ou dois ao diretório.

Tuplas são *imutáveis*, o que significa que, uma vez criada uma tupla,
não é possível substituir nenhum de seus elementos por um novo valor.
Listas são *mutáveis*, o que significa que você pode sempre alterar os
elementos de uma lista. Apenas objetos *hasheáveis* (que permitem o
cálculo de um *hash*) podem ser usados como chaves de dicionário. A
maioria dos tipos imutáveis é hasheável; por isso, tuplas — mas não
listas — podem ser usadas como chaves. Observe, no entanto, que uma
tupla só é hasheável se todos os seus elementos também o forem.


Como as listas são implementadas no CPython?
============================================

As listas do CPython são, na verdade, vetores de comprimento variável,
listas vinculadas não no estilo Lisp. A implementação usa um vetor
contíguo de referências a outros objetos e mantém um ponteiro para
esse vetor e o comprimento de vetor em uma estrutura de cabeçalho de
lista.

Isso torna a indexação de uma lista "a[i]" uma operação cujo custo é
independente do tamanho da lista ou do valor do índice.

Quando itens são anexados ou inseridos, o vetor de referências é
redimensionado. Alguma inteligência é aplicada para melhorar o
desempenho de anexar itens repetidamente; quando o vetor precisa ser
aumentado, algum espaço extra é alocado para que as próximas vezes não
exijam um redimensionamento real.

Consulte Complexidade de tempo de operações em tipos embutidos para os
custos das várias operações de lista.


Como são os dicionários implementados no CPython?
=================================================

Os dicionários do CPython são implementados como tabelas hash
redimensionáveis. Em comparação com árvores B, isso oferece melhor
desempenho para pesquisa (de longe a operação mais comum) na maioria
das circunstâncias, e a implementação é mais simples.

Os dicionários funcionam calculando um código hash para cada chave
armazenada no dicionário usando a função embutida "hash()". O código
hash varia amplamente dependendo da chave e da semente por processo;
por exemplo, "'Python'" poderia fazer hash para "-539294296" enquanto
"'python'", uma string que difere por um único bit, poderia fazer hash
para "1142331976". O código hash é então usado para calcular um local
em um vetor interno onde o valor será armazenado. Supondo que você
esteja armazenando chaves com valores de hash diferentes, isso
significa que os dicionários levam um tempo constante -- *O*(1), na
notação Big-O -- para recuperar uma chave.

Consulte Complexidade de tempo de operações em tipos embutidos para os
custos das várias operações de dicionário.


Por que chaves de dicionário devem ser imutáveis?
=================================================

A implementação da tabela hash de dicionários usa um valor hash
calculado a partir do valor da chave para encontrar a chave. Se a
chave fosse um objeto mutável, seu valor poderia mudar e, portanto,
seu hash também poderia mudar. Mas como quem altera o objeto-chave não
pode saber que ele estava sendo usado como chave de dicionário, ele
não pode mover a entrada no dicionário. Então, quando você tentar
procurar o mesmo objeto no dicionário, ele não será encontrado porque
seu valor de hash é diferente. Se você tentasse procurar o valor
antigo, ele também não seria encontrado, porque o valor do objeto
encontrado naquele hash seria diferente.

Se você deseja que um dicionário seja indexado com uma lista,
simplesmente converta primeiro a lista em uma tupla; a função
"tuple(L)" cria uma tupla com as mesmas entradas da lista "L". As
tuplas são imutáveis e, portanto, podem ser usadas como chaves de
dicionário.

Algumas soluções inaceitáveis que foram propostas:

* Listas de hash por endereço (ID do objeto). Isto não funciona porque
  se você construir uma nova lista com o mesmo valor ela não será
  encontrada; por exemplo.:

     mydict = {[1, 2]: '12'}
     print(mydict[[1, 2]])

  levantaria uma exceção "KeyError" porque o id do "[1, 2]" usado na
  segunda linha difere daquele da primeira linha. Em outras palavras,
  as chaves de dicionário devem ser comparadas usando "==", não usando
  "is".

* Fazer uma cópia ao usar uma lista como chave. Isso não funciona
  porque a lista, sendo um objeto mutável, poderia conter uma
  referência a si mesma e então o código copiado entraria em um laço
  infinito.

* Permitir listas como chaves, mas dizer ao usuário para não
  modificá-las. Isso permitiria uma classe de bugs difíceis de
  rastrear em programas quando você esquecesse ou modificasse uma
  lista por acidente. Também invalida uma importante invariante dos
  dicionários: todo valor em "d.keys()" pode ser usado como chave do
  dicionário.

* Marcar listas como somente leitura quando forem usadas como chave de
  dicionário. O problema é que não é apenas o objeto de nível superior
  que pode alterar seu valor; você poderia usar uma tupla contendo uma
  lista como chave. Inserir qualquer coisa como chave em um dicionário
  exigiria marcar todos os objetos acessíveis a partir daí como
  somente leitura -- e, novamente, objetos autorreferenciais poderiam
  causar um laço infinito.

Existe um truque para contornar isso se você precisar, mas use-o por
sua própria conta e risco: você pode agrupar uma estrutura mutável
dentro de uma instância de classe que tenha um método "__eq__()" e um
método "__hash__()". Você deve então certificar-se de que o valor de
hash para todos os objetos invólucros que residem em um dicionário (ou
outra estrutura baseada em hash) permaneça fixo enquanto o objeto
estiver no dicionário (ou outra estrutura).

   class ListWrapper:
       def __init__(self, the_list):
           self.the_list = the_list

       def __eq__(self, other):
           return self.the_list == other.the_list

       def __hash__(self):
           l = self.the_list
           result = 98767 - len(l)*555
           for i, el in enumerate(l):
               try:
                   result = result + (hash(el) % 9999999) * 1001 + i
               except Exception:
                   result = (result % 7777777) + i * 333
           return result

Observe que o cálculo do hash é complicado pela possibilidade de que
alguns membros da lista possam ser não não-hasheável e também pela
possibilidade de estouro aritmético.

Além disso, deve ser sempre o caso que se "o1 == o2" (ou seja,
"o1.__eq__(o2) is True") então "hash(o1) == hash(o2)" (ou seja,
"o1.__hash__() == o2.__hash__()"), independentemente de o objeto estar
em um dicionário ou não. Se você não cumprir essas restrições, os
dicionários e outras estruturas baseadas em hash se comportarão mal.

No caso de "ListWrapper", sempre que o objeto invólucro estiver em um
dicionário, a lista agrupada não deve ser alterada para evitar
anomalias. Não faça isso a menos que esteja preparado para pensar
muito sobre os requisitos e as consequências de não atendê-los
corretamente. Considere-se avisado.


Por que lista.sort() não retorna a lista ordenada?
==================================================

Em situações nas quais desempenho importa, fazer uma cópia da lista só
para ordenar seria desperdício. Portanto, "list.sort()" ordena a
lista. De forma a lembrá-lo desse fato, isso não retorna a lista
ordenada. Desta forma, você não vai ser confundido a acidentalmente
sobrescrever uma lista quando você precisar de uma cópia ordenada mas
também precisar manter a versão não ordenada.

Se você quiser retornar uma nova lista, use a função embutida
"sorted()" ao invés. Essa função cria uma nova lista a partir de um
iterável provido, o ordena e retorna. Por exemplo, aqui é como se
itera em cima das chaves de um dicionário de maneira ordenada:

   for key in sorted(mydict):
       ...  # use mydict[key] conforme quiser...


Como você especifica e aplica um spec de interface no Python?
=============================================================

Uma especificação de interface para um módulo fornecida por linguagens
como C++ e Java descreve os protótipos para os métodos e funções do
módulo. Muitos acham que a aplicação de especificações de interface em
tempo de compilação ajuda na construção de programas grandes.

Python 2.6 adiciona um módulo "abc" que permite definir Classes Base
Abstratas (ABCs). Você pode então usar "isinstance()" e "issubclass()"
para verificar se uma instância ou classe implementa um ABC
específico. O módulo "collections.abc" define um conjunto de ABCs
úteis como "Iterable", "Container" e "MutableMapping"

Para Python, muitas das vantagens das especificações de interface
podem ser obtidas por uma disciplina de teste apropriada para
componentes.

Um bom conjunto de testes para um módulo pode fornecer um teste de
regressão e servir como uma especificação de interface do módulo e um
conjunto de exemplos. Muitos módulos Python podem ser executados como
um script para fornecer um simples "autoteste". Mesmo módulos que usam
interfaces externas complexas muitas vezes podem ser testados
isoladamente usando emulações triviais da interface externa. Os
módulos "doctest" e "unittest" ou estruturas de teste de terceiros
podem ser usados para construir conjuntos de testes exaustivos que
exercitam cada linha de código em um módulo.

Uma disciplina de teste apropriada pode ajudar a construir aplicações
grandes e complexas no Python, assim como ter especificações de
interface. Na verdade, pode ser melhor porque uma especificação de
interface não pode testar certas propriedades de um programa. Por
exemplo, espera-se que o método "list.append()" adicione novos
elementos ao final de alguma lista interna; uma especificação de
interface não pode testar se sua implementação "list.append()"
realmente fará isso corretamente, mas é trivial verificar esta
propriedade em um conjunto de testes.

Escrever conjuntos de testes é muito útil e você pode querer projetar
seu código para torná-lo facilmente testável. Uma técnica cada vez
mais popular, o desenvolvimento orientado a testes, exige a escrita de
partes do conjunto de testes primeiro, antes de escrever qualquer
parte do código real. É claro que o Python permite que você seja
desleixado e nem escreva casos de teste.


Por que não há goto?
====================

Na década de 1970, as pessoas perceberam que o goto irrestrito poderia
levar a um código "espaguete" confuso, difícil de entender e revisar.
Em uma linguagem de alto nível, também é desnecessário, desde que
existam maneiras de ramificar (em Python, com instruções "if" e "or",
"and" e expressões "if"/"else") e iterar (com instruções "while" e
"for", possivelmente contendo "continue" e "break").

Também é possível usar exceções para fornecer um "goto estruturado"
que funcione mesmo em chamadas de função. Muitos acham que as exceções
podem convenientemente emular todos os usos razoáveis das construções
"go" ou "goto" de C, Fortran e outras linguagens. Por exemplo:

   class label(Exception): pass  # declara um label

   try:
       ...
       if condition: raise label()  # goto label
       ...
   except label:  # destino do goto
       pass
   ...

Isso não permite que você pule para o meio de um laço, mas isso
geralmente é considerado um abuso de "goto" de qualquer maneira. Use
com moderação.


Por que strings brutas (r-strings) não podem terminar com uma contrabarra?
==========================================================================

Mais precisamente, eles não podem terminar com um número ímpar de
contrabarras: a contrabarra não pareada no final escapa do caractere
de aspa de fechamento, deixando uma string não terminada.

Strings brutas foram projetadas para facilitar a criação de entrada
para processadores (principalmente mecanismos de expressão regular)
que desejam fazer seu próprio processamento de escape de contrabarra.
De qualquer forma, esses processadores consideram uma contrabarra
incomparável como um erro, portanto, as strings brutas não permitem
isso. Em troca, eles permitem que você transmita o caractere de aspas
da string escapando dele com uma contrabarra. Essas regras funcionam
bem quando r-strings são usadas para a finalidade pretendida.

Se você estiver tentando criar nomes de caminho do Windows, observe
que todas as chamadas do sistema do Windows também aceitam barras:

   f = open("/mydir/file.txt")  # funciona normalmente!

Se você estiver tentando construir um nome de caminho para um comando
DOS, tente, por exemplo, algum desses

   dir = r"\this\is\my\dos\dir" "\\"
   dir = r"\this\is\my\dos\dir\ "[:-1]
   dir = "\\this\\is\\my\\dos\\dir\\"


Por que o Python não tem uma instrução "with" para atribuição de atributos?
===========================================================================

Python tem uma instrução "with" que envolve a execução de um bloco,
chamando o código na entrada e na saída do bloco. Algumas linguagens
têm uma construção desta forma:

   with obj:
       a = 1               # equivalente a obj.a = 1
       total = total + 1   # obj.total = obj.total + 1

Em Python, tal construção seria ambígua.

Outras linguagens, como Object Pascal, Delphi, e C++, usam tipos
estáticos, então é possível saber, de maneira não ambígua, que membro
está sendo atribuído. Esse é o principal ponto da tipagem estática --
o compilador *sempre* sabe o escopo de toda variável em tempo de
compilação.

O Python usa tipos dinâmicos. É impossível saber com antecedência que
atributo vai ser referenciado em tempo de execução. Atributos membro
podem ser adicionados ou removidos de objetos dinamicamente. Isso
torna impossível saber, de uma leitura simples, que atributo está
sendo referenciado: um atributo local, um atributo global ou um
atributo membro?

Por exemplo, pegue o seguinte trecho incompleto:

   def foo(a):
       with a:
           print(x)

O trecho presume que "a" deve ter um atributo de membro chamado "x".
No entanto, não há nada em Python que diga isso ao interpretador. O
que deveria acontecer se "a" for, digamos, um número inteiro? Se
houver uma variável global chamada "x", ela será usada dentro do bloco
"with"? Como você pode ver, a natureza dinâmica do Python torna essas
escolhas muito mais difíceis.

O principal benefício de "with" e recursos de linguagem semelhantes
(redução do volume de código) pode, no entanto, ser facilmente
alcançado em Python por atribuição. Em vez de:

   function(args).mydict[index][index].a = 21
   function(args).mydict[index][index].b = 42
   function(args).mydict[index][index].c = 63

escreva isso:

   ref = function(args).mydict[index][index]
   ref.a = 21
   ref.b = 42
   ref.c = 63

Isso também tem o efeito colateral de aumentar a velocidade de
execução porque as ligações de nome são resolvidas a tempo de execução
em Python, e a segunda versão só precisa performar a resolução uma
vez.

Propostas semelhantes que introduziriam sintaxe para reduzir ainda
mais o volume do código, como o uso de um 'ponto inicial', foram
rejeitadas em favor da explicitação (consulte
https://mail.python.org/pipermail/python-ideas/2016-May/040070.html).


Por que os geradores não suportam a instrução with?
===================================================

Por razões técnicas, um gerador usado diretamente como gerenciador de
contexto não funcionaria corretamente. Quando, como é mais comum, um
gerador é usado como um iterador executado até a conclusão, nenhum
fechamento é necessário. Quando estiver, envolva-o como
"contextlib.closing(generator)" na instrução "with".


Por que dois pontos são necessários para as instruções de if/while/def/class?
=============================================================================

Os dois pontos são obrigatórios primeiramente para melhorar a leitura
(um dos resultados da linguagem experimental ABC). Considere isso:

   if a == b
       print(a)

versus

   if a == b:
       print(a)

Note como a segunda é ligeiramente mais fácil de ler. Note com mais
atenção como os dois pontos iniciam o exemplo nessa resposta de FAQ; é
um uso padrão em inglês.

Outro motivo menor é que os dois pontos deixam mais fácil para os
editores com realce de sintaxe; eles podem procurar por dois pontos
para decidir quando a recuo precisa ser aumentada em vez de precisarem
fazer uma análise mais elaborada do texto do programa.


Por que o Python permite vírgulas ao final de listas e tuplas?
==============================================================

O Python deixa você adicionar uma vírgula ao final de listas, tuplas e
dicionários:

   [1, 2, 3,]
   ('a', 'b', 'c',)
   d = {
       "A": [1, 5],
       "B": [6, 7],  # a vírgula ao final é opcional, mas é bom estilo
   }

Existem várias razões para permitir isso.

Quando você possui um valor literal para uma lista, tupla, ou
dicionário disposta através de múltiplas linhas, é mais fácil
adicionar mais elementos porque você não precisa lembrar de adicionar
uma vírgula na linha anterior. As linhas também podem ser reordenadas
sem criar um erro de sintaxe.

Acidentalmente omitir a vírgula pode levar a erros que são difíceis de
diagnosticar. Por exemplo:

   x = [
     "fee",
     "fie"
     "foo",
     "fum"
   ]

Essa lista parece ter quatro elementos, mas na verdade contém três:
"fee", "fiefoo" e "fum". Sempre adicionar a vírgula evita essa fonte
de erro.

Permitir a vírgula no final também pode deixar a geração de código
programático mais fácil.
