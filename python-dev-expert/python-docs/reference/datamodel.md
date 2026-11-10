3. Modelo de dados
******************


3.1. Objetos, valores e tipos
=============================

*Objetos* são abstrações do Python para dados. Todos os dados em um
programa Python são representados por objetos ou por relações entre
objetos. Código também é representado por objetos.

Todo objeto tem uma identidade, um tipo e um valor. A *identidade* de
um objeto nunca muda depois de criado; você pode pensar nisso como
endereço de objetos em memória. O operador "is" compara as identidades
de dois objetos; a função "id()" retorna um inteiro representando sua
identidade.

Para CPython, "id(x)" é o endereço de memória em que "x" está
armazenado.

O tipo de um objeto determina as operações que o objeto implementa
(por exemplo, "ele tem um comprimento?") e também define os valores
possíveis para objetos desse tipo. A função "type()" retorna o tipo de
um objeto (que é também um objeto). Como sua identidade, o *tipo* do
objeto também é imutável. [1]

O *valor* de alguns objetos pode mudar. Objetos cujos valores podem
mudar são descritos como *mutáveis*, objetos cujo valor não pode ser
mudado uma vez que foram criados são chamados *imutáveis*. (O valor de
um objeto contêiner imutável que contém uma referência a um objeto
mutável pode mudar quando o valor deste último for mudado; no entanto
o contêiner é ainda assim considerada imutável, pois a coleção de
objetos que contém não pode ser mudada. Então a imutabilidade não é
estritamente o mesmo do que não haver mudanças de valor, é mais
sutil.) A mutabilidade de um objeto é determinada pelo seu tipo; por
exemplo, números, strings e tuplas são imutáveis, enquanto dicionários
e listas são mutáveis.

Os objetos nunca são destruídos explicitamente; no entanto, quando
eles se tornam inacessíveis, eles podem ser coletados como lixo. Uma
implementação tem permissão para adiar a coleta de lixo ou omiti-la
completamente -- é uma questão de detalhe de implementação como a
coleta de lixo é implementada, desde que nenhum objeto que ainda
esteja acessível seja coletado.

CPython atualmente usa um esquema de contagem de referências com
detecção atrasada (opcional) de lixo ligado ciclicamente, que coleta a
maioria dos objetos assim que eles se tornam inacessíveis, mas não é
garantido que coletará lixo contendo referências circulares. Veja a
documentação do módulo "gc" para informações sobre como controlar a
coleta de lixo cíclico. Outras implementações agem de forma diferente
e o CPython pode mudar. Não dependa da finalização imediata dos
objetos quando eles se tornarem inacessíveis (isto é, você deve sempre
fechar os arquivos explicitamente).

Observe que o uso dos recursos de rastreamento ou depuração da
implementação pode manter os objetos ativos que normalmente seriam
coletáveis. Observe também que capturar uma exceção com uma instrução
"try"..."except" pode manter os objetos vivos.

Alguns objetos contêm referências a recursos "externos", como arquivos
abertos ou janelas. Entende-se que esses recursos são liberados quando
o objeto é coletado como lixo, mas como a coleta de lixo não é
garantida, tais objetos também fornecem uma maneira explícita de
liberar o recurso externo, geralmente um método "close()". Os
programas são fortemente recomendados para fechar explicitamente esses
objetos. A instrução "try"..."finally" e a instrução "with" fornecem
maneiras convenientes de fazer isso.

Alguns objetos contêm referências a outros objetos; eles são chamados
de *contêineres*. Exemplos de contêineres são tuplas, listas e
dicionários. As referências fazem parte do valor de um contêiner. Na
maioria dos casos, quando falamos sobre o valor de um contêiner, nos
referimos aos valores, não às identidades dos objetos contidos;
entretanto, quando falamos sobre a mutabilidade de um contêiner,
apenas as identidades dos objetos contidos imediatamente estão
implícitas. Portanto, se um contêiner imutável (como uma tupla) contém
uma referência a um objeto mutável, seu valor muda se esse objeto
mutável for alterado.

Os tipos afetam quase todos os aspectos do comportamento do objeto.
Até mesmo a importância da identidade do objeto é afetada em algum
sentido: para tipos imutáveis, as operações que calculam novos valores
podem realmente retornar uma referência a qualquer objeto existente
com o mesmo tipo e valor, enquanto para objetos mutáveis isso não é
permitido. Por exemplo, após "a = 1; b = 1", *a* e *b* podem ou não se
referir ao mesmo objeto com o valor um, dependendo da implementação.
Isto ocorre porque "int" é um tipo imutável, então a referência a "1"
pode ser reutilizada. Este comportamento depende da implementação
usada, então não deve ser considerada confiável, mas é algo para se
estar ciente ao fazer uso de testes de identidade de objeto. No
entanto, após "c = []; d = []", *c* e *d* têm a garantia de referir-se
a duas listas vazias diferentes e únicas. (Observe que "e = f = []"
atribui o *mesmo* objeto para *e* e *f*.)


3.2. A hierarquia de tipos padrão
=================================

Abaixo está uma lista dos tipos que são embutidos no Python. Módulos
de extensão (escritos em C, Java ou outras linguagens, dependendo da
implementação) podem definir tipos adicionais. Versões futuras do
Python podem adicionar tipos à hierarquia de tipo (por exemplo,
números racionais, matrizes de inteiros armazenadas de forma
eficiente, etc.), embora tais adições sejam frequentemente fornecidas
por meio da biblioteca padrão.

Algumas das descrições de tipo abaixo contêm um parágrafo listando
"atributos especiais". Esses são atributos que fornecem acesso à
implementação e não se destinam ao uso geral. Sua definição pode mudar
no futuro.


3.2.1. None
-----------

Este tipo possui um único valor. Existe um único objeto com este
valor. Este objeto é acessado através do nome embutido "None". É usado
para significar a ausência de um valor em muitas situações, por
exemplo, ele é retornado de funções que não retornam nada
explicitamente. Seu valor verdade é falso.


3.2.2. NotImplemented
---------------------

Este tipo possui um único valor. Existe um único objeto com este
valor. Este objeto é acessado através do nome embutido
"NotImplemented". Os métodos numéricos e métodos de comparação rica
devem retornar esse valor se não implementarem a operação para os
operandos fornecidos. (O interpretador tentará então a operação
refletida ou alguma outra alternativa, dependendo do operador.) Não
deve ser avaliado em um contexto booleano.

Veja a documentação Implementando as operações aritméticas para mais
detalhes.

Alterado na versão 3.9: A avaliação de "NotImplemented" em um contexto
booleano foi descontinuada.

Alterado na versão 3.14: A avaliação de "NotImplemented" em um
contexto booleano agora levanta um "TypeError". Anteriormente, ele era
avaliado como "True" e emitia um "DeprecationWarning" desde o Python
3.9.


3.2.3. Ellipsis
---------------

Este tipo possui um único valor. Existe um único objeto com este
valor. Este objeto é acessado através do literal "..." ou do nome
embutido "Ellipsis" (reticências). Seu valor verdade é verdadeiro.


3.2.4. "numbers.Number"
-----------------------

Esses são criados por literais numéricos e retornados como resultados
por operadores aritméticos e funções aritméticas embutidas. Os objetos
numéricos são imutáveis; uma vez criado, seu valor nunca muda. Os
números do Python são, obviamente, fortemente relacionados aos números
matemáticos, mas sujeitos às limitações da representação numérica em
computadores.

As representações de string das classes numéricas, calculadas por
"__repr__()" e "__str__()", têm as seguintes propriedades:

* Elas são literais numéricos válidos que, quando passados para seu
  construtor de classe, produzem um objeto com o valor do numérico
  original.

* A representação está na base 10, quando possível.

* Os zeros à esquerda, possivelmente com exceção de um único zero
  antes de um ponto decimal, não são mostrados.

* Os zeros à direita, possivelmente com exceção de um único zero após
  um ponto decimal, não são mostrados.

* Um sinal é mostrado apenas quando o número é negativo.

Python distingue entre inteiros, números de ponto flutuante e números
complexos:


3.2.4.1. "numbers.Integral"
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Estes representam elementos do conjunto matemático de inteiros
(positivos e negativos).

Nota:

  As regras para representação de inteiros têm como objetivo fornecer
  a interpretação mais significativa das operações de deslocamento e
  máscara envolvendo inteiros negativos.

Existem dois tipos de inteiros:

Inteiros ("int")
   Estes representam números em um intervalo ilimitado, sujeito apenas
   à memória (virtual) disponível. Para o propósito de operações de
   deslocamento e máscara, uma representação binária é presumida e os
   números negativos são representados em uma variante do complemento
   de 2 que dá a ilusão de uma string infinita de bits de sinal
   estendendo-se para a esquerda.

Booleanos ("bool")
   Estes representam os valores da verdade Falsos e Verdadeiros. Os
   dois objetos que representam os valores "False" e "True" são os
   únicos objetos booleanos. O tipo booleano é um subtipo do tipo
   inteiro, e os valores booleanos se comportam como os valores 0 e 1,
   respectivamente, em quase todos os contextos, com exceção de que,
   quando convertidos em uma string, as strings ""False"" ou ""True""
   são retornados, respectivamente.


3.2.4.2. "numbers.Real" ("float")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Estes representam números de ponto flutuante de precisão dupla no
nível da máquina. Você está à mercê da arquitetura da máquina
subjacente (e implementação C ou Java) para o intervalo aceito e
tratamento de estouro. Python não oferece suporte a números de ponto
flutuante de precisão única; a economia no uso do processador e da
memória, que normalmente é o motivo de usá-los, é ofuscada pela
sobrecarga do uso de objetos em Python, portanto, não há razão para
complicar a linguagem com dois tipos de números de ponto flutuante.


3.2.4.3. "numbers.Complex" ("complex")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Estes representam números complexos como um par de números de ponto
flutuante de precisão dupla no nível da máquina. As mesmas
advertências se aplicam aos números de ponto flutuante. As partes
reais e imaginárias de um número complexo "z" podem ser obtidas
através dos atributos somente leitura "z.real" e "z.imag".


3.2.5. Sequências
-----------------

Estes representam conjuntos ordenados finitos indexados por números
não negativos. A função embutida "len()" retorna o número de itens de
uma sequência. Quando o comprimento de uma sequência é *n*, o conjunto
de índices contém os números 0, 1, ..., *n*-1. O item *i* da sequência
*a* é selecionado por "a[i]". Algumas sequências, incluindo sequências
embutidas, interpretam subscritos negativos adicionando o comprimento
da sequência. Por exemplo, "a[-2]" é igual a "a[n-2]", o penúltimo
item da sequência a com comprimento "n".

O valor resultante deve ser um número inteiro não negativo menor que o
número de itens na sequência. Caso contrário, uma "IndexError" é
levantada.

Sequências também suportam fatiamento: "a[start:stop]" seleciona todos
os itens com índice *k* tal que *start*``<=``*k* "<" *stop*. Quando
utilizada como expressão, uma fatia é uma sequência do mesmo tipo. O
comentário anterior sobre índices negativos também se aplica a
posições negativas em fatiamento. Observe que nenhum erro é gerado se
a posição da fatia for menor que zero ou maior que o comprimento da
sequência.

Se *start* estiver ausente ou for "None" , o fatiamento se comporta
como se *start* fosse zero. Se *stop* estiver ausente ou for "None" ,
o fatiamento se comporta como se *stop* fosse igual ao comprimento da
sequência.

Algumas sequências também suportam "fatiamento estendido" com um
terceiro parâmetro de "etapa": "a[i:j:k]" seleciona todos os itens de
*a* com índice *x* onde "x = i + n*k", *n* ">=" "0" e *i* "<=" *x* "<"
*j*.

As sequências são distinguidas de acordo com sua mutabilidade:


3.2.5.1. Sequências imutáveis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um objeto de um tipo de sequência imutável não pode ser alterado
depois de criado. (Se o objeto contiver referências a outros objetos,
esses outros objetos podem ser mutáveis e podem ser alterados; no
entanto, a coleção de objetos diretamente referenciada por um objeto
imutável não pode ser alterada.)

Os tipos a seguir são sequências imutáveis:

Strings
   Uma string ("str") é uma sequência de valores que representam
   *caracteres* ou, mais formalmente, *pontos de código Unicode*.
   Todos os pontos de código no intervalo de "0" a "0x10FFFF" podem
   ser representados em uma string.

   Python não possui um tipo de *caractere* dedicado. Em vez disso,
   cada ponto de código na string é representado como um objeto de
   string com comprimento "1".

   A função embutida "ord()" converte um ponto de código de sua forma
   de string para um inteiro no intervalo de "0" a "0x10FFFF"; "chr()"
   converte um inteiro no intervalo de "0" a "0x10FFFF" para o objeto
   de string de comprimento "1" correspondente. "str.encode()" pode
   ser usado para converter "str" em "bytes" usando a codificação do
   texto, e "bytes.decode()" pode ser usado para realizar a operação
   inversa.

Tuplas
   The items of a "tuple" are arbitrary Python objects. Tuples of two
   or more items are formed by comma-separated lists of expressions.
   A tuple of one item (a 'singleton') can be formed by affixing a
   comma to an expression (an expression by itself does not create a
   tuple, since parentheses must be usable for grouping of
   expressions).  An empty tuple can be formed by an empty pair of
   parentheses.

Bytes
   A "bytes" object is an immutable array.  The items are 8-bit bytes,
   represented by integers in the range 0 <= x < 256.  Bytes literals
   (like "b'abc'") and the built-in "bytes()" constructor can be used
   to create bytes objects.  Also, bytes objects can be decoded to
   strings via the "decode()" method.


3.2.5.2. Sequências mutáveis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As sequências mutáveis podem ser alteradas após serem criadas. As
notações de subscrição e fatiamento podem ser usadas como o destino da
atribuição e instruções "del" (*delete*, exclusão).

Nota:

  Os módulos "collections" e "array" fornecem exemplos adicionais de
  tipos de sequência mutáveis.

Atualmente, existem dois tipos de sequência mutável intrínseca:

Listas
   Os itens de uma lista são objetos Python arbitrários. As listas são
   formadas colocando uma lista de expressões separada por vírgulas
   entre colchetes. (Observe que não há casos especiais necessários
   para formar listas de comprimento 0 ou 1.)

Vetores de bytes
   Um objeto bytearray é um vetor mutável. Eles são criados pelo
   construtor embutido "bytearray()". Além de serem mutáveis (e,
   portanto, não-hasheável), os vetores de bytes fornecem a mesma
   interface e funcionalidade que os objetos imutáveis "bytes".


3.2.6. Tipos de conjuntos
-------------------------

Estes representam conjuntos finitos e não ordenados de objetos únicos
e imutáveis. Como tal, eles não podem ser indexados por nenhum
subscrito. No entanto, eles podem ser iterados, e a função embutida
"len()" retorna o número de itens em um conjunto. Os usos comuns para
conjuntos são testes rápidos de associação, remoção de duplicatas de
uma sequência e computação de operações matemáticas como interseção,
união, diferença e diferença simétrica.

Para elementos de conjunto, as mesmas regras de imutabilidade se
aplicam às chaves de dicionário. Observe que os tipos numéricos
obedecem às regras normais para comparação numérica: se dois números
forem iguais (por exemplo, "1" e "1.0"), apenas um deles pode estar
contido em um conjunto.

Atualmente, existem dois tipos de conjuntos intrínsecos:

Conjuntos
   Estes representam um conjunto mutável. Eles são criados pelo
   construtor embutido "set()" e podem ser modificados posteriormente
   por vários métodos, como "add()".

Conjuntos congelados
   Estes representam um conjunto imutável. Eles são criados pelo
   construtor embutido "frozenset()". Como um frozenset é imutável e
   *hasheável*, ele pode ser usado novamente como um elemento de outro
   conjunto, ou como uma chave de dicionário.


3.2.7. Mapeamentos
------------------

Eles representam conjuntos finitos de objetos indexados por conjuntos
de índices arbitrários. A notação subscrito "a[k]" seleciona o item
indexado por "k" do mapeamento "a"; isso pode ser usado em expressões
e como alvo de atribuições ou instruções "del". A função embutida
"len()" retorna o número de itens em um mapeamento.

Existem dois tipos de mapeamento intrínseco:


3.2.7.1. Dicionários
~~~~~~~~~~~~~~~~~~~~

Eles representam conjuntos finitos de objetos indexados por valores
quase arbitrários. Os únicos tipos de valores não aceitáveis como
chaves são os valores que contêm listas ou dicionários ou outros tipos
mutáveis que são comparados por valor em vez de por identidade de
objeto, o motivo é que a implementação eficiente de dicionários requer
que o valor de hash de uma chave permaneça constante. Os tipos
numéricos usados para chaves obedecem às regras normais para
comparação numérica: se dois números forem iguais (por exemplo, "1" e
"1.0"), eles podem ser usados alternadamente para indexar a mesma
entrada do dicionário.

Dicionários preservam a ordem de inserção, o que significa que as
chaves serão produzidas na mesma ordem em que foram adicionadas
sequencialmente no dicionário. Substituir uma chave existente não
altera a ordem, no entanto, remover uma chave e inseri-la novamente
irá adicioná-la ao final em vez de manter seu lugar anterior.

Os dicionários são mutáveis; eles podem ser criados pela notação "{}"
(veja a seção Sintaxes de criação de dicionário).

Os módulos de extensão "dbm.ndbm" e "dbm.gnu" fornecem exemplos
adicionais de tipos de mapeamento, assim como o módulo "collections".

Alterado na versão 3.7: Dicionários não preservavam a ordem de
inserção nas versões do Python anteriores à 3.6. No CPython 3.6, a
ordem de inserção foi preservada, mas foi considerada um detalhe de
implementação naquela época, em vez de uma garantia da linguagem.


3.2.7.2. Dicionários congelados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Estes representam um dicionário imutável. Eles são criados pelo
construtor embutido "frozendict()". Um frozendict é *hashable* se
todas as suas chaves e valores forem hasheável, caso em que pode ser
usado como um elemento de um conjunto, ou como uma chave em outro
mapeamento. "frozendict" não é uma subclasse de "dict" ; ele herda
diretamente de "object".

Adicionado na versão 3.15.


3.2.8. Tipos chamáveis
----------------------

Estes são os tipos aos quais a operação de chamada de função (veja a
seção Chamadas) pode ser aplicada:


3.2.8.1. Funções definidas pelo usuário
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um objeto função definido pelo usuário será criado pela definição de
função (veja a seção Definições de função). A mesma deverá ser
invocada com uma lista de argumentos contendo o mesmo número de itens
que a lista de parâmetros formais da função.


3.2.8.1.1. Atributos especiais de somente leitura
"""""""""""""""""""""""""""""""""""""""""""""""""

+----------------------------------------------------+----------------------------------------------------+
| Atributo                                           | Significado                                        |
|====================================================|====================================================|
| function.__builtins__                              | A reference to the "dictionary" that holds the     |
|                                                    | function's builtins namespace.  Adicionado na      |
|                                                    | versão 3.10.                                       |
+----------------------------------------------------+----------------------------------------------------+
| function.__globals__                               | Uma referência ao "dicionário" que contém as       |
|                                                    | variáveis globais da função -- o espaço de nomes   |
|                                                    | global do módulo no qual a função foi definida.    |
+----------------------------------------------------+----------------------------------------------------+
| function.__closure__                               | "None" ou uma "tuple" de células que contêm        |
|                                                    | ligação para os nomes especificados no atributo    |
|                                                    | "co_freevars" do "objeto código" da função.  Um    |
|                                                    | objeto de célula tem o atributo "cell_contents".   |
|                                                    | Isso pode ser usado para obter o valor da célula,  |
|                                                    | bem como definir o valor.                          |
+----------------------------------------------------+----------------------------------------------------+


3.2.8.1.2. Atributos especiais graváveis
""""""""""""""""""""""""""""""""""""""""

A maioria desses atributos verifica o tipo do valor atribuído:

+----------------------------------------------------+----------------------------------------------------+
| Atributo                                           | Significado                                        |
|====================================================|====================================================|
| function.__doc__                                   | A string de documentação da função, ou "None" se   |
|                                                    | indisponível.                                      |
+----------------------------------------------------+----------------------------------------------------+
| function.__name__                                  | O nome da função. Veja também: "atributos          |
|                                                    | __name__".                                         |
+----------------------------------------------------+----------------------------------------------------+
| function.__qualname__                              | O *nome qualificado* da função. Veja também:       |
|                                                    | "atributos __qualname__".  Adicionado na versão    |
|                                                    | 3.3.                                               |
+----------------------------------------------------+----------------------------------------------------+
| function.__module__                                | O nome do módulo em que a função foi definida ou   |
|                                                    | "None" se indisponível.                            |
+----------------------------------------------------+----------------------------------------------------+
| function.__defaults__                              | Uma "tuple" contendo valores de *parâmetro* padrão |
|                                                    | para aqueles parâmetros que possuem padrões, ou    |
|                                                    | "None" se nenhum parâmetro tiver um valor padrão.  |
+----------------------------------------------------+----------------------------------------------------+
| function.__code__                                  | O objeto código que representa o corpo da função   |
|                                                    | compilada.                                         |
+----------------------------------------------------+----------------------------------------------------+
| function.__dict__                                  | O espaço de nomes que provê atributos de função    |
|                                                    | arbitrários. Veja também: "atributos __dict__".    |
+----------------------------------------------------+----------------------------------------------------+
| function.__annotations__                           | Um "dicionário" contendo anotações de              |
|                                                    | *parâmetros*. As chaves do dicionário são os nomes |
|                                                    | dos parâmetros e "'return'" para a anotação de     |
|                                                    | retorno, se fornecida. Veja também:                |
|                                                    | "object.__annotations__".  Alterado na versão      |
|                                                    | 3.14: Anotações são agora avaliados                |
|                                                    | preguiçosamente. Veja a **PEP 649**.               |
+----------------------------------------------------+----------------------------------------------------+
| function.__annotate__                              | A *função de anotação* para esta função, ou "None" |
|                                                    | se a função não tiver anotações. Veja              |
|                                                    | "object.__annotate__".  Adicionado na versão 3.14. |
+----------------------------------------------------+----------------------------------------------------+
| function.__kwdefaults__                            | Um "dicionário" contendo padrões apenas para       |
|                                                    | *parâmetros* somente- nomeados.                    |
+----------------------------------------------------+----------------------------------------------------+
| function.__type_params__                           | Uma "tuple" contendo os parâmetros de tipo de uma  |
|                                                    | função genérica.  Adicionado na versão 3.12.       |
+----------------------------------------------------+----------------------------------------------------+

Os objetos de função também dão suporte à obtenção e definição de
atributos arbitrários, que podem ser usados, por exemplo, para anexar
metadados a funções. A notação de ponto de atributo regular é usada
para obter e definir tais atributos.

A implementação atual do CPython provê apenas atributos de função em
funções definidas pelo usuário. Atributos de função em funções
embutido podem ser suportados no futuro.

Informações adicionais sobre a definição de uma função podem ser
obtidas de seu objeto código (acessível através do atributo
"__code__").


3.2.8.2. Métodos de instância
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um objeto método de instância combina uma classe, uma instância de
classe e qualquer objeto chamável (normalmente uma função definida
pelo usuário).

Atributos especiais de somente leitura:

+----------------------------------------------------+----------------------------------------------------+
| method.__self__                                    | Refere-se ao objeto instância da classe ao qual o  |
|                                                    | método é vinculado                                 |
+----------------------------------------------------+----------------------------------------------------+
| method.__func__                                    | Refere-se ao objeto função original                |
+----------------------------------------------------+----------------------------------------------------+
| method.__doc__                                     | A documentação do método (igual a                  |
|                                                    | "method.__func__.__doc__"). Um "string" se a       |
|                                                    | função original tivesse uma docstring, caso        |
|                                                    | contrário "None".                                  |
+----------------------------------------------------+----------------------------------------------------+
| method.__name__                                    | O nome do método (mesmo que                        |
|                                                    | "method.__func__.__name__")                        |
+----------------------------------------------------+----------------------------------------------------+
| method.__module__                                  | O nome do módulo em que o método foi definido ou   |
|                                                    | "None" se indisponível.                            |
+----------------------------------------------------+----------------------------------------------------+

Os métodos também implementam o acesso (mas não a configuração) dos
atributos arbitrários da função no objeto função subjacente.

Objetos método definidos pelo usuário podem ser criados ao obter um
atributo de uma classe (talvez através de uma instância dessa classe),
se esse atributo for um objeto função definido pelo usuário ou um
objeto "classmethod" .

Quando um objeto método de instância é criado recuperando um objeto
função definido pelo usuário de uma classe por meio de uma de suas
instâncias, seu atributo "__self__" é a instância, e o objeto método é
considerado *vinculado*. O atributo "__func__" do novo método é o
objeto da função original.

Quando um objeto método de instância é criado obtendo um objeto
"classmethod" de uma classe ou instância, seu atributo "__self__" é a
própria classe, e seu atributo "__func__" é o objeto função subjacente
ao método de classe.

Quando um objeto método de instância é chamado, a função subjacente
("__func__") é chamada, inserindo a instância de classe ("__self__")
na frente da lista de argumentos. Por exemplo, quando "C" é uma classe
que contém uma definição para uma função "f()", e "x" é uma instância
de "C", chamando "x.f(1)" é equivalente a chamar "C.f(x, 1)".

Quando um objeto método de instância é derivado de um objeto
"classmethod", a "instância de classe" armazenada em "__self__" será,
na verdade, a própria classe, de modo que chamar "x.f(1)" ou "C.f(1)"
é equivalente a chamar "f(C,1)" sendo "f" a função subjacente.

É importante observar que funções definidas pelo usuário que são
atributos de uma instância de classe não são convertidas em métodos
vinculados; isso *somente* acontece quando a função é um atributo da
classe.


3.2.8.3. Funções geradoras
~~~~~~~~~~~~~~~~~~~~~~~~~~

A function or method which contains a "yield" expression (see section
Expressões yield) is called a *generator function*.  Such a function,
when called, always returns an *iterator* object which can be used to
execute the body of the function:  calling the iterator's
"iterator.__next__()" method will cause the function to execute until
it provides a value using the "yield" expression.  When the function
executes a "return" statement or falls off the end, a "StopIteration"
exception is raised and the iterator will have reached the end of the
set of values to be returned.


3.2.8.4. Funções de corrotina
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uma função ou um método que é definida(o) usando "async def" é chamado
de *função de corrotina*. Tal função, quando chamada, retorna um
objeto de *corrotina*. Ele pode conter expressões "await", bem como
instruções "async with" e "async for". Veja também a seção Objetos
corrotina.


3.2.8.5. Funções geradoras assíncronas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A function or method which is defined using "async def" and which
contains a "yield" expression is called a *asynchronous generator
function*.  Such a function, when called, returns an *asynchronous
iterator* object which can be used in an "async for" statement to
execute the body of the function.

Chamar o método "aiterator.__anext__" do iterador assíncrono retornará
um *aguardável* que, quando aguardado, será executado até fornecer um
valor usando a expressão "yield". Quando a função executa uma
instrução vazia "return" ou chega ao final, uma exceção
"StopAsyncIteration" é levantada e o iterador assíncrono terá
alcançado o final do conjunto de valores a serem produzidos.


3.2.8.6. Funções embutidas
~~~~~~~~~~~~~~~~~~~~~~~~~~

Um objeto função embutida é um wrapper em torno de uma função C.
Exemplos de funções embutidas são "len()" e "math.sin()" ("math" é um
módulo embutido padrão). O número e o tipo dos argumentos são
determinados pela função C. Atributos especiais de somente leitura:

* "__doc__" é a string de documentação da função, ou "None" se não
  estiver disponível. Veja "function.__doc__".

* "__name__" é o nome da função. Veja "function.__name__".

* "__self__" is the module object the function was defined in or
  "None" if unavailable.

* "__module__" é o nome do módulo no qual a função foi definida ou
  "None" se não estiver disponível. Veja "function.__module__".


3.2.8.7. Métodos embutidos
~~~~~~~~~~~~~~~~~~~~~~~~~~

Este é realmente um disfarce diferente de uma função embutida, desta
vez contendo um objeto passado para a função C como um argumento extra
implícito. Um exemplo de método embutido é "alist.append()",
presumindo que *alist* é um objeto de lista. Nesse caso, o atributo
especial de somente leitura "__self__" é definido como o objeto
denotado por *alist*. (O atributo tem a mesma semântica de "outros
métodos de instância".)


3.2.8.8. Classes
~~~~~~~~~~~~~~~~

Classes são chamáveis. Esses objetos normalmente agem como fábricas
para novas instâncias de si mesmos, mas variações são possíveis para
tipos de classe que substituem "__new__()". Os argumentos da chamada
são passados para "__new__()" e, no caso típico, para "__init__()"
para inicializar a nova instância.


3.2.8.9. Instâncias de classe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instâncias de classes arbitrárias podem ser tornados chamáveis
definindo um método "__call__()" em sua classe.


3.2.9. Módulos
--------------

Módulos são uma unidade organizacional básica do código Python, e são
criados pelo sistema de importação quando invocado pela instrução
"import", ou chamando funções como "importlib.import_module()" e a
embutida "__import__()". Um objeto módulo tem um espaço de nomes
implementado por um objeto "dicionário" (este é o dicionário
referenciado pelo atributo "__globals__" das funções definidas no
módulo). As referências de atributos são traduzidas para pesquisas
neste dicionário, por exemplo, "m.x" é equivalente a
"m.__dict__["x"]". Um objeto módulo não contém o objeto código usado
para inicializar o módulo (uma vez que não é necessário depois que a
inicialização é concluída).

A atribuição de atributo atualiza o dicionário de espaço de nomes do
módulo, por exemplo, "m.x = 1" é equivalente a "m.__dict__["x"] = 1".


3.2.9.1. Atributos relacionados à importação em objetos de módulo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objetos de módulo têm os seguintes atributos que se relacionam ao
sistema de importação. Quando um módulo é criado usando o maquinário
associado ao sistema de importação, esses atributos são preenchidos
com base no *spec* do módulo, antes que o *carregador* execute e
carregue o módulo.

Para criar um módulo dinamicamente em vez de usar o sistema de
importação, é recomendado usar "importlib.util.module_from_spec()",
que definirá os vários atributos controlados pela importação para
valores apropriados. Também é possível usar o construtor
"types.ModuleType" para criar módulos diretamente, mas essa técnica é
mais propensa a erros, pois a maioria dos atributos deve ser definida
manualmente no objeto do módulo após ele ter sido criado ao usar essa
abordagem.

Cuidado:

  Com exceção de "__name__", é **fortemente** recomendado que você
  confie no "__spec__" e seus atributos em vez de qualquer um dos
  outros atributos individuais listados nesta subseção. Observe que
  atualizar um atributo em "__spec__" não atualizará o atributo
  correspondente no próprio módulo:

     >>> import typing
     >>> typing.__name__, typing.__spec__.name
     ('typing', 'typing')
     >>> typing.__spec__.name = 'spelling'
     >>> typing.__name__, typing.__spec__.name
     ('typing', 'spelling')
     >>> typing.__name__ = 'keyboard_smashing'
     >>> typing.__name__, typing.__spec__.name
     ('keyboard_smashing', 'spelling')

module.__name__

   O nome usado para identificar exclusivamente o módulo no sistema de
   importação. Para um módulo executado diretamente, isso será
   definido como ""__main__"".

   Este atributo deve ser definido como o nome totalmente qualificado
   do módulo. Espera-se que ele corresponda ao valor de
   "module.__spec__.name".

module.__spec__

   Um registro do estado relacionado ao sistema de importação do
   módulo.

   Define com "spec de módulo" que foi usado ao importar o módulo.
   Veja Especificações de módulo para mais detalhes.

   Adicionado na versão 3.4.

module.__package__

   O *pacote* ao qual um módulo pertence.

   Se o módulo for de nível superior (ou seja, não fizer parte de
   nenhum pacote específico), o atributo deve ser definido como "''"
   (a string vazia). Caso contrário, deve ser definido como o nome do
   pacote do módulo (que pode ser igual a "module.__name__" se o
   módulo em si for um pacote). Veja **PEP 366** para mais detalhes.

   Este atributo é usado em vez de "__name__" para calcular
   importações relativas explícitas para módulos principais. O padrão
   é "None" para módulos criados dinamicamente usando o construtor
   "types.ModuleType"; use "importlib.util.module_from_spec()" em vez
   disso para garantir que o atributo seja definido como "str".

   É **fortemente** recomendado que você use "module.__spec__.parent"
   em vez de "module.__package__". "__package__" agora só é usado como
   fallback se "__spec__.parent" não estiver definido, e esse caminho
   de fallback está descontinuado.

   Alterado na versão 3.4: Este atributo agora presume o padrão "None"
   para módulos criados dinamicamente usando o construtor
   "types.ModuleType". Anteriormente, o atributo era opcional.

   Alterado na versão 3.6: Espera-se que o valor de "__package__" seja
   o mesmo que "__spec__.parent". "__package__" agora é usado apenas
   como fallback durante a resolução de importação se
   "__spec__.parent" não estiver definido.

   Alterado na versão 3.10: "ImportWarning" é levantada se uma
   resolução de importação retorna para "__package__" em vez de
   "__spec__.parent".

   Alterado na versão 3.12: Levanta "DeprecationWarning" em vez de
   "ImportWarning" ao retornar para "__package__" durante a resolução
   de importação.

   Descontinuado desde a versão 3.13, removido na versão 3.15:
   "__package__" deixará de ser definido ou levado em consideração
   pelo sistema de importação ou biblioteca padrão.

module.__loader__

   O objeto *carregador* que o maquinário de importação usou para
   carregar o módulo.

   Este atributo é útil principalmente para introspecção, mas pode ser
   usado para funcionalidades adicionais específicas do carregador,
   por exemplo, para obter dados associados a um carregador.

   "__loader__" assume como padrão "None" para módulos criados
   dinamicamente usando o construtor "types.ModuleType"; use
   "importlib.util.module_from_spec()" para garantir que o atributo
   seja definido como um objeto *carregador*.

   É **fortemetne** recomendado que você use "module.__spec__.loader"
   em vez de "module.__loader__".

   Alterado na versão 3.4: Este atributo agora presume o padrão "None"
   para módulos criados dinamicamente usando o construtor
   "types.ModuleType". Anteriormente, o atributo era opcional.

   Descontinuado desde a versão 3.12, será removido na versão 3.16: A
   definição "__loader__" em um módulo enquanto falha na definição de
   "__spec__.loader" está descontinuado. No Python 3.16, "__loader__"
   deixará de ser definido ou levado em consideração pelo sistema de
   importação ou pela biblioteca padrão.

module.__path__

   Uma *sequência* (possivelmente vazia) de strings enumerando os
   locais onde os submódulos do pacote serão encontrados. Módulos que
   não sejam de pacote não devem ter um atributo "__path__". Veja
   Atributo __path__ dos módulos para mais detalhes.

   É **fortemente** recomendado que você use
   "module.__spec__.submodule_search_locations" em vez de
   "module.__path__".

module.__file__

   "__file__" is an optional attribute that may or may not be set.
   Both attributes should be a "str" when they are available.

   An optional attribute, "__file__" indicates the pathname of the
   file from which the module was loaded (if loaded from a file), or
   the pathname of the shared library file for extension modules
   loaded dynamically from a shared library. It might be missing for
   certain types of modules, such as C modules that are statically
   linked into the interpreter, and the import system may opt to leave
   it unset if it has no semantic meaning (for example, a module
   loaded from a database).

Alterado na versão 3.15: The "__cached__" attribute is no longer set
on modules or taken into consideration by the import system or
standard library.


3.2.9.2. Outros atributos graváveis em objetos de módulo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Além dos atributos relacionados à importação listados acima, os
objetos de módulo também têm os seguintes atributos graváveis:

module.__doc__

   A string de documentação do módulo, ou "None" se indisponível. Veja
   também: "atributos __doc__".

module.__annotations__

   Um dicionário contendo *anotações de variável*  coletadas durante a
   execução do corpo do módulo. Para as melhores práticas sobre como
   trabalhar com "__annotations__". Veja "annotationlib".

   Alterado na versão 3.14: Anotações são agora avaliados
   preguiçosamente. Veja a **PEP 649**.

module.__annotate__

   A *função de anotação* para este módulo, ou "None" se o módulo não
   tiver anotações. Veja também: atributos "__annotate__".

   Adicionado na versão 3.14.

module.__lazy_modules__

   A container (an object implementing "__contains__()") of fully
   qualified module name strings.  When defined at module scope, any
   regular "import" statement in that module whose target module name
   appears in this container is treated as a lazy import, as if the
   "lazy" keyword had been used.  Imports inside functions, class
   bodies, or "try"/"except"/"finally" blocks are unaffected.

   See Compatibility via __lazy_modules__ for details and examples.

   Adicionado na versão 3.15.


3.2.9.3. Dicionários do módulo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Os objetos de módulo também têm o seguinte atributo especial somente
leitura:

module.__dict__

   O espaço de nomes do módulo como um objeto dicionário.
   Exclusivamente entre os atributos listados aqui, "__dict__" não
   pode ser acessado como uma variável global de dentro de um módulo;
   ele só pode ser acessado como um atributo em objetos de módulo.

   Por causa da maneira como CPython limpa dicionários de módulos, o
   dicionário do módulo será limpo quando o módulo sair do escopo,
   mesmo se o dicionário ainda tiver referências ativas. Para evitar
   isso, copie o dicionário ou mantenha o módulo por perto enquanto
   usa seu dicionário diretamente.


3.2.10. Classes personalizadas
------------------------------

Tipos de classe personalizados são tipicamente criados por definições
de classe (veja a seção Definições de classe). Uma classe possui um
espaço de nomes implementado por um objeto dicionário. As referências
de atributos de classe são traduzidas para pesquisas neste dicionário,
por exemplo, "C.x" é traduzido para "C.__dict__["x"]" (embora haja uma
série de ganchos que permitem outros meios de localizar atributos).
Quando o nome do atributo não é encontrado lá, a pesquisa do atributo
continua nas classes base. Essa pesquisa das classes base usa a ordem
de resolução de métodos C3, que se comporta corretamente mesmo na
presença de estruturas de herança em losango, onde há vários caminhos
de herança que levam de volta a um ancestral comum. Detalhes
adicionais sobre a ordem de resolução de métodos (MRO) C3 usado pelo
Python podem ser encontrados em A Ordem de Resolução de Métodos do
Python 2.3.

Quando uma referência de atributo de classe (para uma classe "C",
digamos) produziria um objeto método de classe, ele é transformado em
um objeto método de instância cujo atributo "__self__" é "C". Quando
produziria um objeto "staticmethod", ele é transformado no objeto
encapsulado pelo objeto método estático. Veja a seção Implementando
descritores para outra maneira em que os atributos recuperados de uma
classe podem diferir daqueles realmente contidos em seu "__dict__".

As atribuições de atributos de classe atualizam o dicionário da
classe, nunca o dicionário de uma classe base.

Um objeto classe pode ser chamado (veja acima) para produzir uma
instância de classe (veja abaixo).


3.2.10.1. Atributos especiais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+----------------------------------------------------+
| Atributo                                           | Significado                                        |
|====================================================|====================================================|
| type.__name__                                      | O nome da classe. Veja também: "atributos          |
|                                                    | __name__".                                         |
+----------------------------------------------------+----------------------------------------------------+
| type.__qualname__                                  | O *nome qualificado* da classe. Veja também:       |
|                                                    | "atributos __qualname__".                          |
+----------------------------------------------------+----------------------------------------------------+
| type.__module__                                    | O nome do módulo no qual a classe foi definida.    |
+----------------------------------------------------+----------------------------------------------------+
| type.__dict__                                      | Um "proxy de mapeamento" fornecendo uma visão      |
|                                                    | somente leitura do espaço de nomes da classe. Veja |
|                                                    | também: "atributos __dict__".                      |
+----------------------------------------------------+----------------------------------------------------+
| type.__bases__                                     | Uma "tuple" contendo as bases da classe. Na        |
|                                                    | maioria dos casos, para uma classe definida como   |
|                                                    | "class X(A, B, C)", "X.__bases__" será exatamente  |
|                                                    | igual a "(A, B, C)".                               |
+----------------------------------------------------+----------------------------------------------------+
| type.__base__                                      | A única classe base na cadeia de herança           |
|                                                    | responsável pelo layout de memória das instâncias. |
|                                                    | Este atributo corresponde a "tp_base" no nível C.  |
+----------------------------------------------------+----------------------------------------------------+
| type.__doc__                                       | A string de documentação da classe, ou "None" se   |
|                                                    | não estiver definida. Não herdado por subclasses.  |
+----------------------------------------------------+----------------------------------------------------+
| type.__annotations__                               | Um dicionário contendo *anotações de variáveis*    |
|                                                    | coletadas durante a execução do corpo da classe.   |
|                                                    | Veja também: "atributos __annotations__".  Para    |
|                                                    | melhores práticas sobre como trabalhar com         |
|                                                    | "__annotations__", consulte "annotationlib". Use   |
|                                                    | "annotationlib.get_annotations()" em vez de        |
|                                                    | acessar este atributo diretamente.  Aviso:         |
|                                                    | Acessar o atributo "__annotations__" diretamente   |
|                                                    | em um objeto classe pode retornar anotações para a |
|                                                    | classe errada, especialmente em certos casos em    |
|                                                    | que a classe, sua classe base ou uma metaclasse é  |
|                                                    | definida em "from __future__ import annotations".  |
|                                                    | Consulte a **749** para obter detalhes.Este        |
|                                                    | atributo não existe em certas classes embutidas.   |
|                                                    | Em classes definidas pelo usuário sem              |
|                                                    | "__annotations__", ele é um dicionário vazio.      |
|                                                    | Alterado na versão 3.14: Anotações são agora       |
|                                                    | avaliados preguiçosamente. Veja a **PEP 649**.     |
+----------------------------------------------------+----------------------------------------------------+
| type.__annotate__()                                | A *função de anotação* para esta classe, ou "None" |
|                                                    | se a classe não tiver anotações. Veja também:      |
|                                                    | "atributos __annotate__".  Adicionado na versão    |
|                                                    | 3.14.                                              |
+----------------------------------------------------+----------------------------------------------------+
| type.__type_params__                               | Uma "tuple" contendo os parâmetros de tipo de uma  |
|                                                    | classe genérica.  Adicionado na versão 3.12.       |
+----------------------------------------------------+----------------------------------------------------+
| type.__static_attributes__                         | Uma "tuple" contendo nomes de atributos dessa      |
|                                                    | classe que são atribuídos por meio de "self.X" de  |
|                                                    | qualquer função em seu corpo.  Adicionado na       |
|                                                    | versão 3.13.                                       |
+----------------------------------------------------+----------------------------------------------------+
| type.__firstlineno__                               | O número da primeira linha da definição de classe, |
|                                                    | incluindo decoradores. Definir o atributo          |
|                                                    | "__module__" remove o item "__firstlineno__" do    |
|                                                    | dicionário do tipo.  Adicionado na versão 3.13.    |
+----------------------------------------------------+----------------------------------------------------+
| type.__mro__                                       | A "tuple" de classes que são consideradas ao       |
|                                                    | procurar por classes bases durante resolução de    |
|                                                    | métodos.                                           |
+----------------------------------------------------+----------------------------------------------------+


3.2.10.2. Métodos especiais
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Além dos atributos especiais descritos acima, todas as classes Python
também têm os dois métodos a seguir disponíveis:

type.mro()

   Este método pode ser substituído por uma metaclasse para
   personalizar a ordem de resolução de métodos para suas instâncias.
   Ele é chamado na instanciação da classe, e o seu resultado é
   armazenado em "__mro__".

type.__subclasses__()

   Cada classe mantém uma lista de referências fracas para suas
   subclasses imediatas. Este método retorna uma lista de todas essas
   referências ainda vivas. A lista está na ordem que são definidas.
   Exemplo:

      >>> class A: pass
      >>> class B(A): pass
      >>> A.__subclasses__()
      [<class 'B'>]


3.2.11. Instâncias de classe
----------------------------

Uma instância de classe é criada chamando um objeto classe (veja
acima). Uma instância de classe tem um espaço de nomes implementado
como um dicionário que é o primeiro lugar no qual as referências de
atributos são pesquisadas. Quando um atributo não é encontrado lá, e a
classe da instância possui um atributo com esse nome, a pesquisa
continua com os atributos da classe. Se for encontrado um atributo de
classe que seja um objeto função definido pelo usuário, ele é
transformado em um objeto método de instância cujo atributo "__self__"
é a instância. Métodos estáticos e métodos de classe também são
transformados; veja acima em "Classes". Veja a seção Implementando
descritores para outra maneira em que os atributos de uma classe
recuperados através de suas instâncias podem diferir dos objetos
realmente armazenados no "__dict__" da classe. Se nenhum atributo de
classe for encontrado, e a classe do objeto tiver um método
"__getattr__()", este é chamado para satisfazer a pesquisa.

As atribuições e exclusões de atributos atualizam o dicionário da
instância, nunca o dicionário de uma classe. Se a classe tem um método
"__setattr__()" ou "__delattr__()", ele é chamado ao invés de
atualizar o dicionário da instância diretamente.

As instâncias de classe podem fingir ser números, sequências ou
mapeamentos se tiverem métodos com certos nomes especiais. Veja a
seção Nomes de métodos especiais.


3.2.11.1. Atributos especiais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

object.__class__

   A classe à qual pertence uma instância de classe.

object.__dict__

   Um dicionário ou outro objeto de mapeamento usado para armazenar
   atributos (graváveis) de um objeto. Nem todas as instâncias têm um
   atributo "__dict__"; veja a seção sobre __slots__ para mais
   detalhes.


3.2.12. Objetos de E/S (também conhecidos como objetos arquivo)
---------------------------------------------------------------

O *objeto arquivo* representa um arquivo aberto. Vários atalhos estão
disponíveis para criar objetos arquivos: a função embutida "open()", e
também "os.popen()", "os.fdopen()" e o método "makefile()" de objetos
soquete (e talvez por outras funções ou métodos fornecidos por módulos
de extensão).

File objects implement common methods, listed below, to simplify usage
in generic code. They are expected to be Gerenciadores de contexto da
instrução with.

Os objetos "sys.stdin", "sys.stdout" e "sys.stderr" são inicializados
para objetos arquivo que correspondem aos fluxos de entrada, saída e
erro padrão do interpretador; eles são todos abertos em modo texto e,
portanto, seguem a interface definida pela classe abstrata
"io.TextIOBase".

file.read(size=-1, /)

   Retrieve up to *size* data from the file. As a convenience if
   *size* is unspecified or -1 retrieve all data available.

file.write(data, /)

   Store *data* to the file.

file.close()

   Flush any buffers and close the underlying file.


3.2.13. Tipos internos
----------------------

Alguns tipos usados internamente pelo interpretador são expostos ao
usuário. Suas definições podem mudar com versões futuras do
interpretador, mas são mencionadas aqui para fins de integridade.


3.2.13.1. Objetos código
~~~~~~~~~~~~~~~~~~~~~~~~

Objetos código representam código Python executável *compilados em
bytes* ou *bytecode*. A diferença entre um objeto código e um objeto
função é que o objeto função contém uma referência explícita aos
globais da função (o módulo no qual foi definida), enquanto um objeto
código não contém nenhum contexto; também os valores de argumento
padrão são armazenados no objeto função, não no objeto código (porque
eles representam os valores calculados em tempo de execução). Ao
contrário dos objetos função, os objetos código são imutáveis e não
contêm referências (direta ou indiretamente) a objetos mutáveis.


3.2.13.1.1. Atributos especiais de somente leitura
""""""""""""""""""""""""""""""""""""""""""""""""""

+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_name                                 | O nome da função                                   |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_qualname                             | O nome completo da função  Adicionado na versão    |
|                                                    | 3.11.                                              |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_argcount                             | O número total de *parâmetros* posicionais         |
|                                                    | (incluindo parâmetros somente-posicionais e        |
|                                                    | parâmetros com valores padrão) que a função possui |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_posonlyargcount                      | O número de *parâmetros* somente-posicionais       |
|                                                    | (incluindo argumentos com valores padrão) que a    |
|                                                    | função possui                                      |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_kwonlyargcount                       | O número de *parâmetros* somente-nomeados          |
|                                                    | (incluindo argumentos com valores padrão) que a    |
|                                                    | função possui                                      |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_nlocals                              | O número de variáveis locais usadas pela função    |
|                                                    | (incluindo parâmetros)                             |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_varnames                             | Uma "tuple" contendo os nomes das variáveis locais |
|                                                    | na função (começando com os nomes dos parâmetros)  |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_cellvars                             | Uma "tuple" contendo os nomes de variáveis locais  |
|                                                    | que são referenciadas a partir de pelo menos um    |
|                                                    | *escopo aninhado* de dentro da função              |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_freevars                             | Uma "tuple" contendo os nomes de *variáveis livres |
|                                                    | (de clausura)* que um *escopo aninhado* referencia |
|                                                    | em um escopo externo. Veja também                  |
|                                                    | "function.__closure__".  Observação: referências a |
|                                                    | nomes globais e embutidos *não* estão incluídas.   |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_code                                 | Uma string representando a sequência de instruções |
|                                                    | *bytecode* na função                               |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_consts                               | Um "tuple" contendo os literais usados pelo        |
|                                                    | *bytecode* na função                               |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_names                                | Um "tuple" contendo os nomes usados pelo           |
|                                                    | *bytecode* na função                               |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_filename                             | O nome do arquivo do qual o código foi compilado   |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_firstlineno                          | O número da linha da primeira linha da função      |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_linetable                            | A "bytes" object containing encoded source         |
|                                                    | location information. The exact format is an       |
|                                                    | implementation detail and may change between       |
|                                                    | Python versions. Use "co_lines()" and              |
|                                                    | "co_positions()" for supported access to line and  |
|                                                    | position information. To create a modified copy of |
|                                                    | a code object, use "replace()".  Adicionado na     |
|                                                    | versão 3.10.                                       |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_stacksize                            | O tamanho de pilha necessário do objeto código     |
+----------------------------------------------------+----------------------------------------------------+
| codeobject.co_flags                                | Um número "inteiro" codificando uma série de       |
|                                                    | sinalizadores para o interpretador.                |
+----------------------------------------------------+----------------------------------------------------+

Os seguintes bits sinalizadores são definidos para "co_flags": o bit
"0x04" é definido se a função usa a sintaxe "*arguments" para aceitar
um número arbitrário de argumentos posicionais; o bit "0x08" é
definido se a função usa a sintaxe "**keywords" para aceitar
argumentos nomeados arbitrários; o bit "0x20" é definido se a função
for um gerador. Veja Code Objects Bit Flags para detalhes na semântica
de cada sinalizadores que podem estar presentes.

Declarações de recursos futuros (por exemplo, "from __future__ import
division") também usam bits em "co_flags" para indicar se um objeto
código foi compilado com um recurso específico habilitado. Veja
"compiler_flag".

Outros bits em "co_flags" são reservados para uso interno.

Se um objeto código representa uma função e tem uma docstring, o bit
"CO_HAS_DOCSTRING" é definido em "co_flags" e o primeiro item em
"co_consts" é a docstring da função.


3.2.13.1.2. Métodos de objetos código
"""""""""""""""""""""""""""""""""""""

codeobject.co_positions()

   Retorna um iterável das posições no código-fonte de cada instrução
   *bytecode* no objeto código.

   O iterador retorna "tuple"s contendo "(start_line, end_line,
   start_column, end_column)". A *i-nésima* tupla corresponde à
   posição do código-fonte que compilou para a *i-nésima* unidade de
   código. As informações da coluna são deslocamentos de bytes utf-8
   indexados em 0 na linha de código fornecida.

   A informação posicional pode estar ausente. Veja uma lista não-
   exaustiva de casos onde isso pode acontecer:

   * Executando o interpretador com "no_debug_ranges" "-X".

   * Carregando um arquivo pyc compilado com "no_debug_ranges" "-X".

   * Tuplas posicionais correspondendo a instruções artificiais.

   * Números de linha e coluna que não podem ser representados devido
     a limitações específicas de implementação.

   Quando isso ocorre, alguns ou todos elementos da tupla podem ser
   "None".

   Adicionado na versão 3.11.

   Nota:

     Esse recurso requer o armazenamento de posições de coluna no
     objeto código, o que pode resultar em um pequeno aumento no uso
     de memória do interpretador e no uso de disco para arquivos
     Python compilados. Para evitar armazenar as informações extras
     e/ou desativar a exibição das informações extras de rastreamento,
     use a opção de linha de comando "no_debug_ranges"  "-X" ou a
     variável de ambiente "PYTHONNODEBUGRANGES".

codeobject.co_lines()

   Retorna um iterador que produz informações sobre intervalos
   sucessivos de *bytecode*s. Cada item gerado é uma "tuple" de
   "(start, end, lineno)":

   * "start" (um "int") representa o deslocamento (inclusivo) do
     início do intervalo *bytecode*

   * "end" (um "int") representa o deslocamento (exclusivo) do fim do
     intervalo *bytecode*

   * "lineno" é um "int" representando o número da linha do intervalo
     do *bytecode*, ou "None" se os bytecodes no intervalo fornecido
     não tiverem número de linha

   Os itens gerados terão as seguintes propriedades:

   * O primeiro intervalo gerado terá um "start" de 0.

   * Os intervalos "(start, end)" serão não decrescentes e
     consecutivos. Ou seja, para qualquer par de "tuple"s, o "start"
     do segundo será igual ao "end" do primeiro.

   * Nenhum intervalo será inverso: "end >= start" para todos os
     trios.

   * A última "tuple" gerada terá "end" igual ao tamanho do
     *bytecode*.

   Intervalos de largura zero, onde "start == end", são permitidos.
   Intervalos de largura zero são usados para linhas que estão
   presentes no código-fonte, mas foram eliminadas pelo compilador de
   *bytecode*.

   Adicionado na versão 3.10.

   Ver também:

     **PEP 626** - Números de linha precisos para depuração e outras
     ferramentas.
        A PEP que introduziu o método "co_lines()".

codeobject.replace(**kwargs)

   Retorna uma cópia do objeto de código com novos valores para os
   campos especificados.

   Objetos de código também são suportados pela função genérica
   "copy.replace()".

   Adicionado na versão 3.8.


3.2.13.2. Objetos quadro
~~~~~~~~~~~~~~~~~~~~~~~~

Objetos quadro representam quadros de execução. Eles podem ocorrer em
objetos traceback e também são passados para funções de rastreamento
registradas.


3.2.13.2.1. Atributos especiais de somente leitura
""""""""""""""""""""""""""""""""""""""""""""""""""

+----------------------------------------------------+----------------------------------------------------+
| frame.f_back                                       | Aponta para o quadro de pilha anterior (em direção |
|                                                    | ao chamador), ou "None" se este for o quadro de    |
|                                                    | pilha mais abaixo.                                 |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_code                                       | O objeto código sendo executado neste quadro.      |
|                                                    | Acessar este atributo levanta um evento de         |
|                                                    | auditoria "object.__getattr__" com os argumentos   |
|                                                    | "obj" e ""f_code"".                                |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_locals                                     | O mapeamento usado pelo quadro para procurar       |
|                                                    | variáveis locais. Se o quadro se referir a um      |
|                                                    | *escopo otimizado*, isso pode retornar um objeto   |
|                                                    | proxy write-through.  Alterado na versão 3.13:     |
|                                                    | Retorna um proxy para escopos otimizados.          |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_globals                                    | O dicionário usado pelo quadro para procurar       |
|                                                    | variáveis globais                                  |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_builtins                                   | O dicionário usado pelo quadro para procurar nomes |
|                                                    | embutidos (intrínsecos)                            |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_lasti                                      | A "instrução precisa" do objeto quadro (este é um  |
|                                                    | índice na string *bytecode* do objeto código)      |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_generator                                  | O objeto *gerador* ou *corrotina* que possui este  |
|                                                    | quadro, ou "None" se o quadro for uma função       |
|                                                    | normal.  Adicionado na versão 3.14.                |
+----------------------------------------------------+----------------------------------------------------+


3.2.13.2.2. Atributos especiais graváveis
"""""""""""""""""""""""""""""""""""""""""

+----------------------------------------------------+----------------------------------------------------+
| frame.f_trace                                      | Se não for "None", esta é uma função chamada para  |
|                                                    | vários eventos durante a execução do código (isso  |
|                                                    | é usado por depuradores). Normalmente, um evento é |
|                                                    | disparado para cada nova linha de origem (veja     |
|                                                    | "f_trace_lines").                                  |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_trace_lines                                | Defina este atributo como "False" para desabilitar |
|                                                    | o acionamento de um evento de rastreamento para    |
|                                                    | cada linha de origem.                              |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_trace_opcodes                              | Defina este atributo para "True" para permitir que |
|                                                    | eventos por opcode sejam solicitados. Observe que  |
|                                                    | isso pode levar a um comportamento indefinido do   |
|                                                    | interpretador se as exceções levantadas pela       |
|                                                    | função de rastreamento escaparem para a função que |
|                                                    | está sendo rastreada.                              |
+----------------------------------------------------+----------------------------------------------------+
| frame.f_lineno                                     | O número da linha atual do quadro -- escrever para |
|                                                    | isso de dentro de uma função de rastreamento faz   |
|                                                    | saltar para a linha dada (apenas para o quadro     |
|                                                    | mais abaixo). Um depurador pode implementar um     |
|                                                    | comando Jump (também conhecido como Set Next       |
|                                                    | Statement) escrevendo para esse atributo.          |
+----------------------------------------------------+----------------------------------------------------+


3.2.13.2.3. Métodos de objetos quadro
"""""""""""""""""""""""""""""""""""""

Objetos quadro têm suporte a um método:

frame.clear()

   Este método limpa todas as referências a variáveis locais mantidas
   pelo quadro. Além disso, se o quadro pertencer a um *gerador*, o
   gerador é finalizado. Isso ajuda a quebrar os ciclos de referência
   que envolvem objetos quadro (por exemplo, ao capturar uma exceção e
   armazenar seu traceback para uso posterior).

   "RuntimeError" é levantada se o quadro estiver em execução ou
   suspenso.

   Adicionado na versão 3.4.

   Alterado na versão 3.13: Tentar limpar um quadro suspenso levanta
   "RuntimeError" (como sempre foi o caso para quadros em execução).


3.2.13.3. Objetos traceback
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objetos traceback representam o stack trace (situação da pilha de
execução) de uma exceção. Um objeto traceback é criado implicitamente
quando ocorre uma exceção e também pode ser criado explicitamente
chamando "types.TracebackType".

Alterado na versão 3.7: Objetos traceback agora podem ser instanciados
explicitamente a partir de código Python.

Para tracebacks criados implicitamente, quando a busca por um
manipulador de exceção desenrola a pilha de execução, em cada nível
desenrolado um objeto traceback é inserido na frente do traceback
atual. Quando um manipulador de exceção é inserido, o stack trace é
disponibilizado para o programa. (Veja a seção A instrução try.) É
acessível como o terceiro item da tupla retornada por
"sys.exc_info()", e como o atributo "__traceback__" da exceção
capturada.

Quando o programa não contém um manipulador adequado, o stack trace é
escrito (formatado de maneira adequada) no fluxo de erro padrão; se o
interpretador for interativo, ele também é disponibilizado ao usuário
como "sys.last_traceback".

Para tracebacks criados explicitamente, cabe ao criador do traceback
determinar como os atributos "tb_next" devem ser vinculados para
formar um stack trace completo.

Atributos especiais de somente leitura:

+----------------------------------------------------+----------------------------------------------------+
| traceback.tb_frame                                 | Aponta para o quadro de execução do nível atual.   |
|                                                    | Acessar este atributo levanta um evento de         |
|                                                    | auditoria "object.__getattr__" com os argumentos   |
|                                                    | "obj" e ""tb_frame"".                              |
+----------------------------------------------------+----------------------------------------------------+
| traceback.tb_lineno                                | Fornece o número da linha onde ocorreu a exceção   |
+----------------------------------------------------+----------------------------------------------------+
| traceback.tb_lasti                                 | Indica a "instrução precisa".                      |
+----------------------------------------------------+----------------------------------------------------+

O número da linha e a última instrução no traceback podem diferir do
número da linha do seu objeto quadro se a exceção ocorreu em uma
instrução "try" sem cláusula except correspondente ou com uma cláusula
"finally".

traceback.tb_next

   O atributo especial de escrita "tb_next" é o próximo nível no stack
   trace (em direção ao quadro onde a exceção ocorreu), ou "None" se
   não houver próximo nível.

   Alterado na versão 3.7: Este atributo agora é gravável


3.2.13.4. Objetos slice
~~~~~~~~~~~~~~~~~~~~~~~

Objetos slice são usados para representar fatias para métodos
"__getitem__()". Eles também são criados pela função embutida
"slice()".

Adicionado na versão 3.15: The "slice()" type now supports
subscription. For example, "slice[float]" may be used in type
annotations to indicate a slice containing "float" objects.

Atributos especiais de somente leitura: "start" é o limite inferior;
"stop" é o limite superior; "step" é o valor da diferença entre
elementos subjacentes; cada um desses atributos é "None" se omitido.
Esses atributos podem ter qualquer tipo.

Objetos slice têm suporte a um método:

slice.indices(self, length)

   Este método recebe um único argumento inteiro *length* e calcula
   informações sobre a fatia que o objeto slice descreveria se
   aplicado a uma sequência de itens de *length*. Ele retorna uma
   tupla de três inteiros; respectivamente, estes são os índices
   *start* e *stop* e o *step* ou comprimento de avanços da fatia.
   Índices ausentes ou fora dos limites são tratados de maneira
   consistente com fatias regulares.


3.2.13.5. Objetos método estático
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objetos método estático fornecem uma forma de transformar objetos
função em objetos métodos descritos acima. Um objeto método estático é
um invólucro em torno de qualquer outro objeto, comumente um objeto
método definido pelo usuário. Quando um objeto método estático é
recuperado de uma classe ou de uma instância de classe, o objeto
retornado é o objeto encapsulado, do qual não está sujeito a nenhuma
transformação adicional. Objetos método estático também são chamáveis.
Objetos método estático são criados pelo construtor embutido
"staticmethod()".


3.2.13.6. Objetos método de classe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um objeto método de classe, como um objeto método estático, é um
invólucro em torno de outro objeto que altera a maneira como esse
objeto é recuperado de classes e instâncias de classe. O comportamento
dos objetos método de classe após tal recuperação é descrito acima,
sob "métodos de instância". Objetos método de classe são criados pelo
construtor embutido "classmethod()".


3.3. Nomes de métodos especiais
===============================

Uma classe pode implementar certas operações que são chamadas por
sintaxe especial (como operações aritméticas ou indexação e
fatiamento), definindo métodos com nomes especiais. Esta é a abordagem
do Python para *sobrecarga de operador*, permitindo que as classes
definam seu próprio comportamento em relação aos operadores da
linguagem. Por exemplo, se uma classe define um método chamado
"__getitem__()", e "x" é uma instância desta classe, então "x[i]" é
aproximadamente equivalente a "type(x).__getitem__(x, i)". Exceto onde
mencionado, as tentativas de executar uma operação levantam uma
exceção quando nenhum método apropriado é definido (tipicamente
"AttributeError" ou "TypeError").

Definir um método especial para "None" indica que a operação
correspondente não está disponível. Por exemplo, se uma classe define
"__iter__()" para "None", a classe não é iterável, então chamar
"iter()" em suas instâncias irá levantar um "TypeError" (sem recorrer
a "__getitem__()"). [2]

Ao implementar uma classe que emula qualquer tipo embutido, é
importante que a emulação seja implementada apenas na medida em que
faça sentido para o objeto que está sendo modelado. Por exemplo,
algumas sequências podem funcionar bem com a recuperação de elementos
individuais, mas extrair uma fatia pode não fazer sentido. (Um exemplo
disso é a interface NodeList no Modelo de Objeto de Documento do W3C.)


3.3.1. Personalização básica
----------------------------

object.__new__(cls[, ...])

   Chamado para criar uma nova instância da classe *cls*. "__new__()"
   é um método estático (é um caso especial, então você não precisa
   declará-lo como tal) que recebe a classe da qual uma instância foi
   solicitada como seu primeiro argumento. Os argumentos restantes são
   aqueles passados para a expressão do construtor do objeto (a
   chamada para a classe). O valor de retorno de "__new__()" deve ser
   a nova instância do objeto (geralmente uma instância de *cls*).

   Implementações típicas criam uma nova instância da classe invocando
   o método "__new__()" da superclasse usando "super().__new__(cls[,
   ...])" com os argumentos apropriados e, em seguida, modificando a
   instância recém-criada conforme necessário antes de retorná-la.

   Se "__new__()" é chamado durante a construção do objeto e retorna
   uma instância de *cls*, então o método "__init__()" da nova
   instância será chamado como "__init__(self[, ...])", onde *self* é
   a nova instância e os argumentos restantes são os mesmos que foram
   passados para o construtor do objeto.

   Se "__new__()" não retornar uma instância de *cls*, então o método
   "__init__()" da nova instância não será invocado.

   "__new__()" destina-se principalmente a permitir que subclasses de
   tipos imutáveis (como int, str ou tupla) personalizem a criação de
   instâncias. Também é comumente substituído em metaclasses
   personalizadas para personalizar a criação de classes.

object.__init__(self[, ...])

   Chamado após a instância ter sido criada (por "__new__()"), mas
   antes de ser retornada ao chamador. Os argumentos são aqueles
   passados para a expressão do construtor da classe. Se uma classe
   base tem um método "__init__()", o método "__init__()" da classe
   derivada, se houver, deve chamá-lo explicitamente para garantir a
   inicialização apropriada da parte da classe base da instância; por
   exemplo: "super().__init__([args...])".

   Porque "__new__()" e "__init__()" trabalham juntos na construção de
   objetos ("__new__()" para criá-lo e "__init__()" para
   personalizá-lo), nenhum valor diferente de "None" pode ser
   retornado por "__init__()"; fazer isso fará com que uma "TypeError"
   seja levantada em tempo de execução.

object.__del__(self)

   Chamado quando a instância está prestes a ser destruída. Também é
   chamada de finalizador ou (incorretamente) de destruidor. Se uma
   classe base tem um método "__del__()", o método "__del__()" da
   classe derivada, se houver, deve chamá-lo explicitamente para
   garantir a exclusão adequada da parte da classe base da instância.

   É possível (embora não recomendado!) para o método "__del__()"
   adiar a destruição da instância criando uma nova referência a ela.
   Isso é chamado de *ressurreição* de objeto. Depende se a
   implementação de "__del__()" é chamado uma segunda vez quando um
   objeto ressuscitado está prestes a ser destruído; a implementação
   atual do *CPython* chama-o apenas uma vez.

   Não há garantia de que os métodos "__del__()" sejam chamados para
   objetos que ainda existem quando o interpretador sai.
   "weakref.finalize" fornece uma maneira direta de registrar uma
   função de limpeza a ser chamada quando um objeto é coletado como
   lixo.

   Nota:

     "del x" não chama diretamente "x.__del__()" -- o primeiro diminui
     a contagem de referências para "x" em um, e o segundo só é
     chamado quando a contagem de referências de "x" atinge zero.

   É possível que um ciclo de referência impeça que a contagem de
   referência de um objeto chegue a zero. Neste caso, mais tarde, o
   ciclo será detectado e deletado pelo *coletor de lixo cíclico*.
   Uma causa comum de referências cíclicas é quando uma exceção foi
   capturada em uma variável local. O locals do quadro então
   referencia a exceção, que referencia seu próprio traceback, que
   referencia o locals de todos os quadros capturados no traceback.

   Ver também: Documentação do módulo "gc".

   Aviso:

     Devido às circunstâncias precárias sob as quais os métodos
     "__del__()" são invocados, as exceções que ocorrem durante sua
     execução são ignoradas e um aviso é impresso em "sys.stderr" em
     seu lugar. Em particular:

     * "__del__()" pode ser chamado quando um código arbitrário está
       sendo executado, incluindo de qualquer thread arbitrária. Se
       "__del__()" precisa bloquear ou invocar qualquer outro recurso
       de bloqueio, pode ocorrer um impasse, pois o recurso já pode
       ter sido levado pelo código que é interrompido para executar
       "__del__()".

     * "__del__()" pode ser executado durante o encerramento do
       interpretador. Como consequência, as variáveis globais que ele
       precisa acessar (incluindo outros módulos) podem já ter sido
       excluídas ou definidas como "None". Python garante que os
       globais cujo nome comece com um único sublinhado sejam
       excluídos de seu módulo antes que outros globais sejam
       excluídos; se nenhuma outra referência a tais globais existir,
       isso pode ajudar a garantir que os módulos importados ainda
       estejam disponíveis no momento em que o método "__del__()" for
       chamado.

object.__repr__(self)

   Chamado pela função embutida "repr()" para calcular a representação
   da string "oficial" de um objeto. Se possível, isso deve parecer
   uma expressão Python válida que pode ser usada para recriar um
   objeto com o mesmo valor (dado um ambiente apropriado). Se isso não
   for possível, uma string no formato "<...alguma descrição útil...>"
   deve ser retornada. O valor de retorno deve ser um objeto string.
   Se uma classe define "__repr__()", mas não "__str__()", então
   "__repr__()" também é usado quando uma representação de string
   "informal" de instâncias daquela classe é necessária.

   Isso é normalmente usado para depuração, portanto, é importante que
   a representação seja rica em informações e inequívoca. Uma
   implementação padrão é fornecida pela própria classe "object".

object.__str__(self)

   Chamado por "str(object)", a implementação padrão de
   "__format__()", e as funções embutidas "print()", para calcular a
   representação da string "informal" ou agradável para exibição de um
   objeto. O valor de retorno deve ser um objeto str.

   Este método difere de "object.__repr__()" por não haver expectativa
   de que "__str__()" retorne uma expressão Python válida: uma
   representação mais conveniente ou concisa pode ser usada.

   A implementação padrão definida pelo tipo embutido "object" chama
   "object.__repr__()".

object.__bytes__(self)

   Chamado por bytes para calcular uma representação de string de
   bytes de um objeto. Isso deve retornar um objeto "bytes". A classe
   "object" em si não fornece este método.

object.__format__(self, format_spec)

   Chamado pela função embutida "format()" e, por extensão, avaliação
   de literais de string formatadas e o método "str.format()", para
   produzir uma representação de string "formatada" de um objeto. O
   argumento *format_spec* é uma string que contém uma descrição das
   opções de formatação desejadas. A interpretação do argumento
   *format_spec* depende do tipo que implementa "__format__()",
   entretanto a maioria das classes delegará a formatação a um dos
   tipos embutidos ou usará uma sintaxe de opção de formatação
   semelhante.

   Consulte Minilinguagem de especificação de formato para uma
   descrição da sintaxe de formatação padrão.

   O valor de retorno deve ser um objeto string.

   A implementação padrão pela classe "object" deve receber uma string
   *format_spec* vazia. Ela delega para "__str__()".

   Alterado na versão 3.4: O método __format__ do próprio "object"
   levanta uma "TypeError" se passada qualquer string não vazia.

   Alterado na versão 3.7: "object.__format__(x, '')" é agora
   equivalente a "str(x)" em vez de "format(str(x), '')".

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)

   Esses são os chamados métodos de "comparação rica". A
   correspondência entre os símbolos do operador e os nomes dos
   métodos é a seguinte: "x<y" chama "x.__lt__(y)", "x<=y" chama
   "x.__le__(y)", "x==y" chama "x.__eq__(y)", "x!=y" chama
   "x.__ne__(y)", "x>y" chama "x.__gt__(y)" e "x>=y" chama
   "x.__ge__(y)".

   Um método de comparação rica pode retornar o singleton
   "NotImplemented" se não implementar a operação para um determinado
   par de argumentos. Por convenção, "False" e "True" são retornados
   para uma comparação bem-sucedida. No entanto, esses métodos podem
   retornar qualquer valor, portanto, se o operador de comparação for
   usado em um contexto booleano (por exemplo, na condição de uma
   instrução "if"), Python irá chamar "bool()" no valor para
   determinar se o resultado for verdadeiro ou falso.

   By default, "object" implements "__eq__()" by using "is", returning
   "NotImplemented" in the case of a false comparison: "True if x is y
   else NotImplemented". For "__ne__()", by default it delegates to
   "__eq__()" and inverts the result unless it is "NotImplemented".
   There are no other implied relationships among the comparison
   operators or default implementations; for example, the truth of
   "(x<y or x==y)" does not imply "x<=y". To automatically generate
   ordering operations from a single root operation, see
   "@functools.total_ordering".

   Por padrão, a classe "object" fornece implementações consistentes
   com Comparações de valor: igualdade compara de acordo com a
   identidade do objeto, e comparações de ordem levantam "TypeError".
   Cada método padrão pode gerar esses resultados diretamente, mas
   também pode retornar "NotImplemented".

   Veja o parágrafo sobre "__hash__()" para algumas notas importantes
   sobre a criação de objetos *hasheáveis* que implementam operações
   de comparação personalizadas e são utilizáveis como chaves de
   dicionário.

   Não há versões de argumentos trocados desses métodos (a serem
   usados quando o argumento esquerdo não tem suporte à operação, mas
   o argumento direito sim); em vez disso, "__lt__()" e "__gt__()" são
   o reflexo um do outro, "__le__()" e "__ge__()" são o reflexo um do
   outro, e "__eq__()" e "__ne__()" são seu próprio reflexo. Se os
   operandos são de tipos diferentes e o tipo do operando direito é
   uma subclasse direta ou indireta do tipo do operando esquerdo, o
   método refletido do operando direito tem prioridade, caso
   contrário, o método do operando esquerdo tem prioridade. Subclasse
   virtual não é considerada.

   Quando nenhum método apropriado retorna qualquer valor diferente de
   "NotImplemented", os operadores "==" e "!=" retornarão para "is" e
   "is not", respectivamente.

object.__hash__(self)

   Called by built-in function "hash()" and for operations on members
   of hashed collections including "set", "frozenset", "dict", and
   "frozendict". The "__hash__()" method should return an integer. The
   only required property is that objects which compare equal have the
   same hash value; it is advised to mix together the hash values of
   the components of the object that also play a part in comparison of
   objects by packing them into a tuple and hashing the tuple.
   Example:

      def __hash__(self):
          return hash((self.name, self.nick, self.color))

   Nota:

     "hash()" trunca o valor retornado do método "__hash__()"
     personalizado de um objeto para o tamanho de um "Py_ssize_t".
     Isso é normalmente 8 bytes em compilações de 64 bits e 4 bytes em
     compilações de 32 bits. Se o "__hash__()" de um objeto deve
     interoperar em compilações de tamanhos de bits diferentes,
     certifique-se de verificar a largura em todas as compilações com
     suporte. Uma maneira fácil de fazer isso é com "python -c "import
     sys; print(sys.hash_info.width)"".

   Se uma classe não define um método "__eq__()", ela também não deve
   definir uma operação "__hash__()"; se define "__eq__()" mas não
   "__hash__()", suas instâncias não serão utilizáveis como itens em
   coleções hasheáveis. Se uma classe define objetos mutáveis e
   implementa um método "__eq__()", ela não deve implementar
   "__hash__()", uma vez que a implementação de coleções  *hasheáveis*
   requer que o valor hash de uma chave seja imutável (se o valor hash
   do objeto mudar, estará no balde de hash errado).

   As classes definidas pelo usuário têm os métodos "__eq__()" e
   "__hash__()" por padrão (herdados da classe "object"); com eles,
   todos os objetos se comparam desiguais (exceto com eles mesmos) e
   "x.__hash__()" retorna um valor apropriado tal que "x == y" implica
   que "x is y" e "hash(x) == hash(y)".

   Uma classe que sobrescreve "__eq__()" e não define "__hash__()"
   terá seu "__hash__()" implicitamente definido como "None". Quando o
   método "__hash__()" de uma classe é "None", as instâncias da classe
   levantam uma "TypeError" apropriada quando um programa tenta
   recuperar seu valor hash, e também será identificado corretamente
   como não-hasheável ao verificar "isinstance(obj,
   collections.abc.Hashable)".

   Se uma classe que substitui "__eq__()" precisa manter a
   implementação de "__hash__()" de uma classe base, o interpretador
   deve ser informado disso explicitamente pela configuração "__hash__
   = <ClasseBase>.__hash__".

   Se uma classe que não substitui "__eq__()" deseja suprimir o
   suporte a hash, deve incluir "__hash__ = None" na definição de
   classe. Uma classe que define seu próprio "__hash__()" que levanta
   explicitamente uma "TypeError" seria incorretamente identificada
   como hasheável por uma chamada "isinstance(obj,
   collections.abc.Hashable)".

   Nota:

     Por padrão, os valores "__hash__()" dos objetos str e bytes são
     "salgados" com um valor aleatório imprevisível. Embora permaneçam
     constantes em um processo individual do Python, eles não são
     previsíveis entre invocações repetidas do Python.This is intended
     to provide protection against a denial-of-service caused by
     carefully chosen inputs that exploit the worst case performance
     of a dict insertion, *O*(*n*^2) complexity.  See
     https://ocert.org/advisories/ocert-2011-003.html for
     details.Alterar os valores de hash afeta a ordem de iteração dos
     conjuntos. Python nunca deu garantias sobre essa ordem (e
     normalmente varia entre compilações de 32 e 64 bits).Consulte
     também "PYTHONHASHSEED".

   Alterado na versão 3.3: Aleatorização de hash está habilitada por
   padrão.

object.__bool__(self)

   Chamado para implementar o teste de valor verdade e a operação
   embutida "bool()"; deve retornar "False" ou "True". Quando este
   método não é definido, "__len__()" é chamado, se estiver definido,
   e o objeto é considerado verdadeiro se seu resultado for diferente
   de zero. Se uma classe não define "__len__()" nem "__bool__()" (o
   que é verdadeiro da classe "object" em si), todas as suas
   instâncias são consideradas verdadeiras.


3.3.2. Personalizando o acesso aos atributos
--------------------------------------------

Os seguintes métodos podem ser definidos para personalizar o
significado do acesso aos atributos (uso, atribuição ou exclusão de
"x.name") para instâncias de classe.

object.__getattr__(self, name)

   Chamado quando o acesso padrão ao atributo falha com um
   "AttributeError" (ou "__getattribute__()" levanta uma
   "AttributeError" porque *name* não é um atributo de instância ou um
   atributo na árvore de classes para "self"; ou "__get__()" de uma
   propriedade *name* levanta "AttributeError"). Este método deve
   retornar o valor do atributo (calculado) ou levantar uma exceção
   "AttributeError". A classe "object" em si não fornece este método.

   Observe que se o atributo for encontrado através do mecanismo
   normal, "__getattr__()" não é chamado. (Esta é uma assimetria
   intencional entre "__getattr__()" e "__setattr__()".) Isso é feito
   tanto por razões de eficiência quanto porque "__getattr__()" não
   teria como acessar outros atributos da instância. Observe que pelo
   menos para variáveis de instâncias, você pode obter controle total
   não inserindo nenhum valor no dicionário de atributos de instância
   (mas, em vez disso, inserindo-os em outro objeto). Veja o método
   "__getattribute__()" abaixo para uma maneira de realmente obter
   controle total sobre o acesso ao atributo.

object.__getattribute__(self, name)

   Chamado incondicionalmente para implementar acessos a atributo para
   instâncias da classe. Se a classe também define "__getattr__()", o
   último não será chamado a menos que "__getattribute__()" o chame
   explicitamente ou levante um "AttributeError". Este método deve
   retornar o valor do atributo (calculado) ou levantar uma exceção
   "AttributeError". Para evitar recursão infinita neste método, sua
   implementação deve sempre chamar o método da classe base com o
   mesmo nome para acessar quaisquer atributos de que necessita, por
   exemplo, "object.__getattribute__(self, name)".

   Nota:

     Este método ainda pode ser ignorado ao procurar métodos especiais
     como resultado de invocação implícita por meio da sintaxe da
     linguagem ou built-in functions. Consulte Pesquisa de método
     especial.

   Para acessos a certos atributos sensíveis, levanta um evento de
   auditoria "object.__getattr__" com os argumentos "obj" e "name".

object.__setattr__(self, name, value)

   Chamado quando se tenta efetuar uma atribuição de atributos. Esse
   método é chamado em vez do mecanismo normal (ou seja, armazena o
   valor no dicionário da instância). *name* é o nome do atributo,
   *value* é o valor a ser atribuído a ele.

   Se "__setattr__()" deseja atribuir a um atributo de instância, ele
   deve chamar o método da classe base com o mesmo nome, por exemplo,
   "object.__setattr__(self, name, value)".

   Para atribuições de certos atributos sensíveis, levanta um evento
   de auditoria "object.__setattr__" com os argumentos "obj", "name" e
   "value".

object.__delattr__(self, name)

   Como "__setattr__()", mas para exclusão de atributo em vez de
   atribuição. Este método só deve ser implementado se "del obj.name"
   for significativo para o objeto.

   Para exclusões a certos atributos sensíveis, levanta um evento de
   auditoria "object.__delattr__" com os argumentos "obj" e "name".

object.__dir__(self)

   Chamado quando "dir()" é chamado com o objeto como argumento. Um
   iterável deve ser retornada. "dir()" converte o iterável retornado
   em uma lista e o ordena.


3.3.2.1. Personalizando acesso a atributos de módulos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

module.__getattr__()
module.__dir__()

Os nomes especiais "__getattr__" e "__dir__" também podem ser usados
para personalizar o acesso aos atributos dos módulos. A função
"__getattr__" no nível do módulo deve aceitar um argumento que é o
nome de um atributo e retornar o valor calculado ou levantar uma
exceção "AttributeError". Se um atributo não for encontrado em um
objeto de módulo por meio da pesquisa normal, por exemplo
"object.__getattribute__()", então "__getattr__" é pesquisado no
módulo "__dict__" antes de levantar "AttributeError". Se encontrado,
ele é chamado com o nome do atributo e o resultado é retornado.

A função "__dir__" não deve aceitar nenhum argumento e retorna um
iterável de strings que representa os nomes acessíveis no módulo. Se
presente, esta função substitui a pesquisa padrão "dir()" em um
módulo.

module.__class__

Para uma personalização mais refinada do comportamento do módulo
(definição de atributos, propriedades etc.), pode-se definir o
atributo "__class__" de um objeto de módulo para uma subclasse de
"types.ModuleType". Por exemplo:

   import sys
   from types import ModuleType

   class VerboseModule(ModuleType):
       def __repr__(self):
           return f'Verbose {self.__name__}'

       def __setattr__(self, attr, value):
           print(f'Setting {attr}...')
           super().__setattr__(attr, value)

   sys.modules[__name__].__class__ = VerboseModule

Nota:

  Definir "__getattr__" no módulo e configurar o "__class__" do módulo
  só afeta as pesquisas feitas usando a sintaxe de acesso ao atributo
  -- acessar diretamente os globais do módulo (seja por código dentro
  do módulo, ou por meio de uma referência ao dicionário global do
  módulo) não tem efeito.

Alterado na versão 3.5: O atributo de módulo "__class__" pode agora
ser escrito.

Adicionado na versão 3.7: Atributos de módulo "__getattr__" e
"__dir__".

Ver também:

  **PEP 562** - __getattr__ e __dir__ de módulo
     Descreve as funções "__getattr__" e "__dir__" nos módulos.


3.3.2.2. Implementando descritores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Os métodos a seguir se aplicam apenas quando uma instância da classe
que contém o método (uma classe chamada *descritora*) aparece em uma
classe proprietária *owner* (o descritor deve estar no dicionário de
classe do proprietário ou no dicionário de classe para um dos seus
pais). Nos exemplos abaixo, "o atributo" refere-se ao atributo cujo
nome é a chave da propriedade no "__dict__" da classe proprietária. A
classe "object" em si não implementa quaisquer desses protocolos.

object.__get__(self, instance, owner=None)

   Chamado para obter o atributo da classe proprietária (acesso ao
   atributo da classe) ou de uma instância dessa classe (acesso ao
   atributo da instância). O argumento opcional *owner* é a classe
   proprietária, enquanto *instance* é a instância pela qual o
   atributo foi acessado, ou "None" quando o atributo é acessado por
   meio de *owner*.

   Este método deve retornar o valor do atributo calculado ou levantar
   uma exceção "AttributeError".

   **PEP 252** especifica que "__get__()" é um chamável com um ou dois
   argumentos. Os próprios descritores embutidos do Python implementam
   esta especificação; no entanto, é provável que algumas ferramentas
   de terceiros tenham descritores que requerem ambos os argumentos. A
   implementação de "__getattribute__()" do próprio Python sempre
   passa em ambos os argumentos sejam eles requeridos ou não.

object.__set__(self, instance, value)

   Chamado para definir o atributo em uma instância *instance* da
   classe proprietária para um novo valor, *value*.

   Observe que adicionar "__set__()" ou "__delete__()" altera o tipo
   de descritor para um "descritor de dados". Consulte Invocando
   descritores para mais detalhes.

object.__delete__(self, instance)

   Chamado para excluir o atributo em uma instância *instance* da
   classe proprietária.

Instâncias de descritores também podem ter o atributo "__objclass__"
presente:

object.__objclass__

   O atributo "__objclass__" é interpretado pelo módulo "inspect" como
   sendo a classe onde este objeto foi definido (configurar isso
   apropriadamente pode ajudar na introspecção em tempo de execução
   dos atributos dinâmicos da classe). Para chamáveis, pode indicar
   que uma instância do tipo fornecido (ou uma subclasse) é esperada
   ou necessária como o primeiro argumento posicional (por exemplo,
   CPython define este atributo para métodos não acoplados que são
   implementados em C).


3.3.2.3. Invocando descritores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Em geral, um descritor é um atributo de objeto com "comportamento de
ligação", cujo acesso ao atributo foi substituído por métodos no
protocolo do descritor: "__get__()", "__set__()" e "__delete__()". Se
qualquer um desses métodos for definido para um objeto, é considerado
um descritor.

O comportamento padrão para acesso ao atributo é obter, definir ou
excluir o atributo do dicionário de um objeto. Por exemplo, "a.x" tem
uma cadeia de pesquisa começando com "a.__dict__['x']", depois
"type(a).__dict__['x']", e continuando pelas classes bases de
"type(a)" excluindo metaclasses.

No entanto, se o valor pesquisado for um objeto que define um dos
métodos do descritor, Python pode substituir o comportamento padrão e
invocar o método do descritor. Onde isso ocorre na cadeia de
precedência depende de quais métodos descritores foram definidos e
como eles foram chamados.

O ponto de partida para a invocação do descritor é uma ligação, "a.x".
Como os argumentos são montados depende de "a":

Chamada direta
   A chamada mais simples e menos comum é quando o código do usuário
   invoca diretamente um método descritor: "x.__get__(a)".

Ligação de instâncias
   Se estiver ligando a uma instância de objeto, "a.x" é transformado
   na chamada: "type(a).__dict__['x'].__get__(a, type(a))".

Ligação de classes
   Se estiver ligando a uma classe, "A.x" é transformado na chamada:
   "A.__dict__['x'].__get__(None, A)".

Ligação de super
   Uma pesquisa pontilhada, ou *dotted lookup*, como "super(A, a).x"
   procura "a.__class__.__mro__" por uma classe base "B" seguindo "A"
   e então retorna "B.__dict__['x'].__get__(a, A)". Se não for um
   descritor, "x" é retornado inalterado.

Para ligações de instâncias, a precedência de invocação do descritor
depende de quais métodos do descritor são definidos. Um descritor pode
definir qualquer combinação de "__get__()", "__set__()" e
"__delete__()". Se ele não definir "__get__()", então acessar o
atributo retornará o próprio objeto descritor, a menos que haja um
valor no dicionário de instância do objeto. Se o descritor define
"__set__()" e/ou "__delete__()", é um descritor de dados; se não
definir nenhum, é um descritor sem dados. Normalmente, os descritores
de dados definem "__get__()" e "__set__()", enquanto os descritores
sem dados têm apenas o método "__get__()". Descritores de dados com
"__get__()" e "__set__()" (e/ou "__delete__()") definidos sempre
substituem uma redefinição em um dicionário de instância. Em
contraste, descritores sem dados podem ser substituídos por
instâncias.

Os métodos Python (incluindo aqueles decorados com "@staticmethod" e
"@classmethod") são implementados como descritores sem dados. Assim,
as instâncias podem redefinir e substituir métodos. Isso permite que
instâncias individuais adquiram comportamentos que diferem de outras
instâncias da mesma classe.

The "@property" decorator is implemented as a data descriptor.
Accordingly, instances cannot override the behavior of a property.


3.3.2.4. __slots__
~~~~~~~~~~~~~~~~~~

*__slots__* permite-nos declarar explicitamente membros de dados (como
propriedades) e negar a criação de "__dict__" e *__weakref__* (a menos
que explicitamente declarado em *__slots__* ou disponível em uma
classe base.)

O espaço economizado com o uso de "__dict__" pode ser significativo. A
velocidade de pesquisa de atributos também pode ser significativamente
melhorada.

object.__slots__

   Esta variável de classe pode ser atribuída a uma string, iterável
   ou sequência de strings com nomes de variáveis usados por
   instâncias. *__slots__* reserva espaço para as variáveis declaradas
   e evita a criação automática de "__dict__" e *__weakref__* para
   cada instância.

Observações ao uso de *__slots__*:

* Ao herdar de uma classe sem *__slots__*, os atributos "__dict__" e
  *__weakref__* das instâncias sempre estarão acessíveis.

* Sem uma variável "__dict__", as instâncias não podem ser atribuídas
  a novas variáveis não listadas na definição *__slots__*. As
  tentativas de atribuir a um nome de variável não listado levantam
  "AttributeError". Se a atribuição dinâmica de novas variáveis for
  desejada, então adicione "'__dict__'" à sequência de strings na
  declaração de *__slots__*.

* Sem uma variável *__weakref__* para cada instância, as classes que
  definem *__slots__* não suportam "referências fracas" para suas
  instâncias. Se for necessário um suporte de referência fraca,
  adicione "'__weakref__'" à sequência de strings na declaração
  *__slots__*.

* *__slots__* são implementados no nível de classe criando descritores
  para cada nome de variável. Como resultado, os atributos de classe
  não podem ser usados para definir valores padrão para variáveis de
  instância definidas por *__slots__*; caso contrário, o atributo de
  classe substituiria a atribuição do descritor.

* A ação de uma declaração *__slots__* se limita à classe em que é
  definida. *__slots__* declarados em uma classe base estão
  disponíveis nas subclasses. No entanto, instâncias de uma subclasse
  filha vai receber um "__dict__" e *__weakref__* a menos que a
  subclasse também defina *__slots__* (que deve conter apenas nomes de
  quaisquer slots *adicionais*).

* Se uma classe define um slot também definido em uma classe base, a
  variável de instância definida pelo slot da classe base fica
  inacessível (exceto por recuperar seu descritor diretamente da
  classe base). Isso torna o significado do programa indefinido. No
  futuro, uma verificação pode ser adicionada para evitar isso.

* "TypeError" will be raised if *__slots__* other than *__dict__* and
  *__weakref__* are defined for a class derived from a ""variable-
  length" built-in type" such as "int", "bytes", and "type", except
  "tuple".

* Qualquer *iterável* não string pode ser atribuído a *__slots__*.

* Se um "dicionário" for usado para atribuir *__slots__*, as chaves do
  dicionário serão usadas como os nomes dos slots. Os valores do
  dicionário podem ser usados para fornecer docstrings por atributo
  que serão reconhecidos por "inspect.getdoc()" e exibidos na saída de
  "help()".

* Atribuição de "__class__" funciona apenas se ambas as classes têm o
  mesmo *__slots__*.

* Multiple inheritance with multiple slotted parent classes can be
  used, but only one parent is allowed to have attributes created by
  slots (the other bases must have empty slot layouts) - violations
  raise "TypeError".

* Se um *iterador* for usado para *__slots__*, um *descritor* é criado
  para cada um dos valores do iterador. No entanto, o atributo
  *__slots__* será um iterador vazio.

Alterado na versão 3.15: Allowed defining the *__dict__* and
*__weakref__* *__slots__* for any class. Allowed defining any
*__slots__* for a class derived from "tuple".


3.3.3. Personalizando a criação de classe
-----------------------------------------

Sempre que uma classe herda de outra classe, "__init_subclass__()" é
chamado na classe base. Dessa forma, é possível escrever classes que
alteram o comportamento das subclasses. Isso está intimamente
relacionado aos decoradores de classe, mas onde decoradores de classe
afetam apenas a classe específica à qual são aplicados,
"__init_subclass__" aplica-se apenas a futuras subclasses da classe
que define o método.

classmethod object.__init_subclass__(cls)

   Este método é chamado sempre que a classe que contém é uma
   subclasse. *cls* é então a nova subclasse. Se definido como um
   método de instância normal, esse método é convertido implicitamente
   em um método de classe.

   Argumentos nomeados dados a uma nova classe são passados para
   "__init_subclass__" da classe base. Para compatibilidade com outras
   classes usando "__init_subclass__", deve-se retirar os argumentos
   nomeados necessários e passar os outros para a classe base, como
   em:

      class Philosopher:
          def __init_subclass__(cls, /, default_name, **kwargs):
              super().__init_subclass__(**kwargs)
              cls.default_name = default_name

      class AustralianPhilosopher(Philosopher, default_name="Bruce"):
          pass

   A implementação padrão de "object.__init_subclass__" não faz nada,
   mas levanta um erro se for chamada com quaisquer argumentos.

   Nota:

     A dica da metaclasse "metaclass" é consumida pelo resto da
     maquinaria de tipo, e nunca é passada para implementações
     "__init_subclass__". A metaclasse real (em vez da dica explícita)
     pode ser acessada como "type(cls)".

   Adicionado na versão 3.6.

Quando uma classe é criada, "type.__new__()" verifica as variáveis de
classe e faz retornos de chamada para elas com um gancho
"__set_name__()".

object.__set_name__(self, owner, name)

   Chamado automaticamente no momento em que a classe proprietária
   *owner* é criada. O objeto foi atribuído a *name* nessa classe:

      class A:
          x = C()  # Automaticamente chama: x.__set_name__(A, 'x')

   Se a variável de classe for atribuída após a criação da classe,
   "__set_name__()" não será chamado automaticamente. Se necessário,
   "__set_name__()" pode ser chamado diretamente:

      class A:
         pass

      c = C()
      A.x = c                  # O gancho não é chamado
      c.__set_name__(A, 'x')   # Invoca manualmente o gancho

   Consulte Criando o objeto classe para mais detalhes.

   Adicionado na versão 3.6.


3.3.3.1. Metaclasses
~~~~~~~~~~~~~~~~~~~~

Por padrão, as classes são construídas usando "type()". O corpo da
classe é executado em um novo espaço de nomes e o nome da classe é
vinculado localmente ao resultado de "type(name, bases, namespace)".

O processo de criação da classe pode ser personalizado passando o
argumento nomeado "metaclass" na linha de definição da classe, ou
herdando de uma classe existente que incluiu tal argumento. No exemplo
a seguir, "MyClass" e "MySubclass" são instâncias de "Meta":

   class Meta(type):
       pass

   class MyClass(metaclass=Meta):
       pass

   class MySubclass(MyClass):
       pass

Quaisquer outros argumentos nomeados especificados na definição de
classe são transmitidos para todas as operações de metaclasse
descritas abaixo.

Quando uma definição de classe é executada, as seguintes etapas
ocorrem:

* entradas de MRO são resolvidas;

* a metaclasse apropriada é determinada;

* o espaço de nomes da classe é preparada;

* o corpo da classe é executado;

* o objeto da classe é criado.


3.3.3.2. Resolvendo entradas de MRO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

object.__mro_entries__(self, bases)

   Se uma classe base que aparece em uma definição de classe não é uma
   instância de "type", então um método "__mro_entries__()" é
   procurado na base. Se um método "__mro_entries__()" é encontrado, a
   base é substituída pelo resultado de uma chamada para
   "__mro_entries__()" ao criar a classe. O método é chamado com a
   tupla de bases original passada como parâmetro *bases*, e deve
   retornar uma tupla de classes que serão usadas no lugar da base. A
   tupla retornada pode estar vazia: nesses casos, a base original é
   ignorada.

Ver também:

  "types.resolve_bases()"
     Dinamicamente resolve bases que não são instâncias de "type".

  "types.get_original_bases()"
     Recupera as "bases originais" de uma classe antes das
     modificações feitas por "__mro_entries__()".

  **PEP 560**
     Suporte básico para módulo typing e tipos genéricos.


3.3.3.3. Determinando a metaclasse apropriada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A metaclasse apropriada para uma definição de classe é determinada da
seguinte forma:

* se nenhuma classe base e nenhuma metaclasse explícita forem
  fornecidas, então "type()" é usada;

* se uma metaclasse explícita é fornecida e *não* é uma instância de
  "type()", então ela é usada diretamente como a metaclasse;

* se uma instância de "type()" é fornecida como a metaclasse
  explícita, ou classes bases são definidas, então a metaclasse mais
  derivada é usada.

A metaclasse mais derivada é selecionada a partir da metaclasse
explicitamente especificada (se houver) e das metaclasses (ou seja,
"type(cls)") de todas as classes bases especificadas. A metaclasse
mais derivada é aquela que é um subtipo de *todas* essas metaclasses
candidatas. Se nenhuma das metaclasses candidatas atender a esse
critério, a definição de classe falhará com "TypeError".


3.3.3.4. Preparando o espaço de nomes da classe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uma vez identificada a metaclasse apropriada, o espaço de nomes da
classe é preparado. Se a metaclasse tiver um atributo "__prepare__",
ela será chamada como "namespace = metaclass.__prepare__(name, bases,
**kwds)" (onde os argumentos nomeados adicionais, se houver, vêm da
definição de classe). O método "__prepare__" deve ser implementado
como um "classmethod". O espaço de nomes retornado por "__prepare__" é
passado para "__new__", mas quando o objeto classe final é criado, o
espaço de nomes é copiado para um novo "dict".

Se a metaclasse não tiver o atributo "__prepare__", então o espaço de
nomes da classe é inicializado como um mapeamento ordenado vazio.

Ver também:

  **PEP 3115** - Metaclasses no Python 3000
     Introduzido o gancho de espaço de nomes "__prepare__"


3.3.3.5. Executando o corpo da classe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O corpo da classe é executado (aproximadamente) como "exec(body,
globals(), namespace)". A principal diferença de uma chamada normal
para "exec()" é que o escopo léxico permite que o corpo da classe
(incluindo quaisquer métodos) faça referência a nomes dos escopos
atual e externo quando a definição de classe ocorre dentro de uma
função.

No entanto, mesmo quando a definição de classe ocorre dentro da
função, os métodos definidos dentro da classe ainda não podem ver os
nomes definidos no escopo da classe. Variáveis de classe devem ser
acessadas através do primeiro parâmetro de instância ou métodos de
classe, ou através da referência implícita com escopo léxico
"__class__" descrita na próxima seção.


3.3.3.6. Criando o objeto classe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uma vez que o espaço de nomes da classe tenha sido preenchido
executando o corpo da classe, o objeto classe é criado chamando
"metaclass(name, bases, namespace, **kwds)" (os argumentos adicionais
passados aqui são os mesmos passados para "__prepare__").

Este objeto classe é aquele que será referenciado pela chamada a
"super()" sem argumentos. "__class__" é uma referência de clausura
implícita criada pelo compilador se algum método no corpo da classe se
referir a "__class__" ou "super". Isso permite que a forma de
argumento zero de "super()" identifique corretamente a classe sendo
definida com base no escopo léxico, enquanto a classe ou instância que
foi usada para fazer a chamada atual é identificada com base no
primeiro argumento passado para o método.

No CPython 3.6 e posterior, a célula "__class__" é passada para a
metaclasse como uma entrada de "__classcell__" no espaço de nomes da
classe. Se estiver presente, deve ser propagado até a chamada a
"type.__new__" para que a classe seja inicializada corretamente. Não
fazer isso resultará em um "RuntimeError" no Python 3.8.

Quando usada a metaclasse padrão "type", ou qualquer metaclasse que
chame "type.__new__", as seguintes etapas de personalização adicionais
são executadas depois da criação do objeto classe:

1. O método "type.__new__" coleta todos os atributos no espaço de
   nomes da classe que definem um método "__set_name__()";

2. Esses métodos "__set_name__" são chamados com a classe sendo
   definida e o nome atribuído para este atributo específico;

3. O gancho "__init_subclass__()" é chamado na classe base imediata da
   nova classe em sua ordem de resolução de método.

Depois que o objeto classe é criado, ele é passado para os decoradores
de classe incluídos na definição de classe (se houver) e o objeto
resultante é vinculado ao espaço de nomes local como a classe
definida.

Quando uma nova classe é criada por "type.__new__", o objeto fornecido
como o parâmetro do espaço de nomes é copiado para um novo mapeamento
ordenado e o objeto original é descartado. A nova cópia é envolta em
um proxy de somente leitura, que se torna o atributo "__dict__" do
objeto classe.

Ver também:

  **PEP 3135** - Novo super
     Descreve a referência de clausura implícita de  "__class__"


3.3.3.7. Usos para metaclasses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Os usos potenciais para metaclasses são ilimitados. Algumas ideias que
foram exploradas incluem enumeradores, criação de log, verificação de
interface, delegação automática, criação automática de propriedade,
proxies, estruturas e travamento/sincronização automático/a de
recursos.


3.3.4. Personalizando verificações de instância e subclasse
-----------------------------------------------------------

Os seguintes métodos são usados para substituir o comportamento padrão
das funções embutidas "isinstance()" e "issubclass()".

Em particular, a metaclasse "abc.ABCMeta" implementa esses métodos a
fim de permitir a adição de classes base abstratas (ABCs) como
"classes base virtuais" para qualquer classe ou tipo (incluindo tipos
embutidos), incluindo outras ABCs.

type.__instancecheck__(self, instance)

   Retorna verdadeiro se *instance* deve ser considerada uma instância
   (direta ou indireta) da classe *class*. Se definido, chamado para
   implementar "isinstance(instance, class)".

type.__subclasscheck__(self, subclass)

   Retorna verdadeiro se *subclass* deve ser considerada uma subclasse
   (direta ou indireta) da classe *class*. Se definido, chamado para
   implementar "issubclass(subclass, class)".

Observe que esses métodos são pesquisados no tipo (metaclasse) de uma
classe. Eles não podem ser definidos como métodos de classe na classe
real. Isso é consistente com a pesquisa de métodos especiais que são
chamados em instâncias, apenas neste caso a própria instância é uma
classe.

Ver também:

  **PEP 3119** - Introduzindo classes base abstratas
     Inclui a especificação para personalizar o comportamento de
     "isinstance()" e "issubclass()" através de "__instancecheck__()"
     e "__subclasscheck__()", com motivação para esta funcionalidade
     no contexto da adição de classes base abstratas (veja o módulo
     "abc") para a linguagem.


3.3.5. Emulando tipos genéricos
-------------------------------

Quando estiver usando *anotações de tipo*, é frequentemente útil
*parametrizar* um *tipo genérico* usando a notação de colchetes do
Python. Por exemplo, a anotação "list[int]" pode ser usada para
indicar uma "list" em que todos os seus elementos são do tipo "int".

Ver também:

  **PEP 484** - Dicas de tipo
     Apresenta a estrutura do Python para anotações de tipo

  Tipos Generic Alias
     Documentação de objetos que representam classes genéricas
     parametrizadas

  Genéricos, genéricos definidos pelo usuário e "typing.Generic"
     Documentação sobre como implementar classes genéricas que podem
     ser parametrizadas em tempo de execução e compreendidas por
     verificadores de tipo estático.

Uma classe pode *geralmente* ser parametrizada somente se ela define o
método de classe especial "__class_getitem__()".

classmethod object.__class_getitem__(cls, key)

   Retorna um objeto que representa a especialização de uma classe
   genérica por argumentos de tipo encontrados em *key*.

   Quando definido em uma classe, "__class_getitem__()" é
   automaticamente um método de classe. Assim, não é necessário que
   seja decorado com "@classmethod" quando de sua definição.


3.3.5.1. O propósito de *__class_getitem__*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O propósito de "__class_getitem__()" é permitir a parametrização em
tempo de execução de classes genéricas da biblioteca padrão, a fim de
aplicar mais facilmente *dicas de tipo* a essas classes.

Para implementar classes genéricas personalizadas que podem ser
parametrizadas em tempo de execução e compreendidas por verificadores
de tipo estáticos, os usuários devem herdar de uma classe da
biblioteca padrão que já implementa "__class_getitem__()", ou herdar
de "typing.Generic", que possui sua própria implementação de
"__class_getitem__()".

Implementações personalizadas de "__class_getitem__()" em classes
definidas fora da biblioteca padrão podem não ser compreendidas por
verificadores de tipo de terceiros, como o mypy. O uso de
"__class_getitem__()" em qualquer classe para fins diferentes de dicas
de tipo é desencorajado.


3.3.5.2. *__class_getitem__* versus *__getitem__*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Normalmente, a subscription de um objeto usando colchetes chamará o
método de instância "__getitem__()" definido na classe do objeto. No
entanto, se o objeto sendo subscrito for ele mesmo uma classe, o
método de classe "__class_getitem__()" pode ser chamado em seu lugar.
"__class_getitem__()" deve retornar um objeto GenericAlias se estiver
devidamente definido.

Apresentado com a *expressão* "obj[x]", o interpretador de Python
segue algo parecido com o seguinte processo para decidir se
"__getitem__()" ou "__class_getitem__()" deve ser chamado:

   from inspect import isclass

   def subscribe(obj, x):
       """Return the result of the expression 'obj[x]'"""

       class_of_obj = type(obj)

       # Se a classe de  obj define __getitem__,
       # chama class_of_obj.__getitem__(obj, x)
       if hasattr(class_of_obj, '__getitem__'):
           return class_of_obj.__getitem__(obj, x)

       # Do contrário, se obj for uma classe e define __class_getitem__,
       # chama obj.__class_getitem__(x)
       elif isclass(obj) and hasattr(obj, '__class_getitem__'):
           return obj.__class_getitem__(x)

       # Do contrário, levanta uma exceção
       else:
           raise TypeError(
               f"'{class_of_obj.__name__}' object is not subscriptable"
           )

Em Python, todas as classes são elas mesmas instâncias de outras
classes. A classe de uma classe é conhecida como *metaclasse* dessa
classe, e a maioria das classes tem a classe "type" como sua
metaclasse. "type" não define "__getitem__()", o que significa que
expressões como "list[int]", "dict[str, float]" e "tuple[str, bytes]"
resultam em chamadas para "__class_getitem__()":

   >>> # lista tem a classe "type" como sua metaclasse, como a maioria das classes:
   >>> type(list)
   <class 'type'>
   >>> type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
   True
   >>> # "list[int]" chama "list.__class_getitem__(int)"
   >>> list[int]
   list[int]
   >>> # list.__class_getitem__ retorna um objeto GenericAlias:
   >>> type(list[int])
   <class 'types.GenericAlias'>

No entanto, se uma classe tiver uma metaclasse personalizada que
define "__getitem__()", subscrever a classe pode resultar em
comportamento diferente. Um exemplo disso pode ser encontrado no
módulo "enum":

   >>> from enum import Enum
   >>> class Menu(Enum):
   ...     """A breakfast menu"""
   ...     SPAM = 'spam'
   ...     BACON = 'bacon'
   ...
   >>> # Classes Enum têm uma metaclasses personalizada:
   >>> type(Menu)
   <class 'enum.EnumMeta'>
   >>> # EnumMeta define __getitem__,
   >>> # de forma que __class_getitem__ não é chamado,
   >>> # e o resultado não é um objeto GenericAlias:
   >>> Menu['SPAM']
   <Menu.SPAM: 'spam'>
   >>> type(Menu['SPAM'])
   <enum 'Menu'>

Ver também:

  **PEP 560** - Suporte básico para módulo typing e tipos genéricos
     Introduz "__class_getitem__()", e define quando uma subscrição
     resulta na chamada de "__class_getitem__()" em vez de
     "__getitem__()"


3.3.6. Emulando objetos chamáveis
---------------------------------

object.__call__(self[, args...])

   Chamado quando a instância é "chamada" como uma função; se este
   método for definido, "x(arg1, arg2, ...)" basicamente traduz para
   "type(x).__call__(x, arg1, ...)". A classe "object" em si não
   fornece este método.


3.3.7. Emulando tipos contêineres
---------------------------------

Os seguintes métodos podem ser definidos para implementar objetos
contêineres. Nenhum deles é fornecido pela própria classe "object".
Contêineres geralmente são *sequências* (como "listas" ou "tuplas") ou
*mapeamentos* (como *dicionários*), mas também podem representar
outros contêineres. O primeiro conjunto de métodos é usado para emular
uma sequência ou um mapeamento; a diferença é que, para uma sequência,
as chaves permitidas devem ser os inteiros *k* para os quais "0 <= k <
N", onde *N* é o comprimento da sequência, ou objetos "fatiamentos",
que definem um intervalo de itens. Também é recomendado que os
mapeamentos forneçam os métodos "keys()", "values()", "items()",
"get()", "clear()", "setdefault()", "pop()", "popitem()", "copy()" e
"update()" se comportando de forma semelhante aos dos objetos
"dicionário" padrão do Python. O módulo "collections.abc" fornece uma
*classe base abstrata* "MutableMapping" para ajudar a criar esses
métodos a partir de um conjunto base de "__getitem__()",
"__setitem__()", "__delitem__()" e "keys()".

Sequências mutáveis devem fornecer métodos "append()", "clear()",
"count()", "extend()", "index()", "insert()", "pop()", "remove()" e
"reverse()", como objetos "list" padrão do Python. Por fim, os tipos
de sequência devem implementar adição (ou seja, concatenação) e
multiplicação (ou seja, repetição) definindo os métodos "__add__()",
"__radd__()", "__iadd__()", "__mul__()", "__rmul__()" e "__imul__()"
descritos abaixo; eles não devem definir outros operadores numéricos.

Recomenda-se que tanto mapeamentos quanto sequências implementem o
método "__contains__()" para permitir o uso eficiente do operador
"in"; para mapeamentos, "in" deve pesquisar as chaves do mapeamento;
para sequências, deve pesquisar os valores. Recomenda-se ainda que
tanto mapeamentos quanto sequências implementem o método "__iter__()"
para permitir uma iteração eficiente pelo contêiner; para mapeamentos,
"__iter__()" deve iterar pelas chaves do objeto; para sequências, deve
iterar pelos valores.

object.__len__(self)

   Chamado para implementar a função embutida "len()". Deve retornar o
   comprimento do objeto, um inteiro ">=" 0. Além disso, um objeto que
   não define um método "__bool__()" e cujo método "__len__()" retorna
   zero é considerado como falso em um contexto booleano.

   No CPython, o comprimento deve ser no máximo "sys.maxsize". Se o
   comprimento for maior que "sys.maxsize", alguns recursos (como
   "len()") podem levantar "OverflowError". Para evitar levantar
   "OverflowError" pelo teste de valor de verdade, um objeto deve
   definir um método "__bool__()".

object.__length_hint__(self)

   Chamado para implementar "operator.length_hint()". Deve retornar um
   comprimento estimado para o objeto (que pode ser maior ou menor que
   o comprimento real). O comprimento deve ser um inteiro ">=" 0. O
   valor de retorno também pode ser "NotImplemented", que é tratado da
   mesma forma como se o método "__length_hint__" não existisse. Este
   método é puramente uma otimização e nunca é necessário para a
   correção.

   Adicionado na versão 3.4.

object.__getitem__(self, subscript)

   Called to implement *subscription*, that is, "self[subscript]". See
   Subscriptions and slicings for details on the syntax.

   There are two types of built-in objects that support subscription
   via "__getitem__()":

   * **sequences**, where *subscript* (also called *index*) should be
     an integer or a "slice" object. See the sequence documentation
     for the expected behavior, including handling "slice" objects and
     negative indices.

   * **mappings**, where *subscript* is also called the *key*. See
     mapping documentation for the expected behavior.

   If *subscript* is of an inappropriate type, "__getitem__()" should
   raise "TypeError". If *subscript* has an inappropriate value,
   "__getitem__()" should raise an "LookupError" or one of its
   subclasses ("IndexError" for sequences; "KeyError" for mappings).

   Nota:

     Slicing is handled by "__getitem__()", "__setitem__()", and
     "__delitem__()". A call like

        a[1:2] = b

     é traduzida com

        a[slice(1, 2, None)] = b

     and so forth. Missing slice items are always filled in with
     "None".

   Nota:

     The sequence iteration protocol (used, for example, in "for"
     loops), expects that an "IndexError" will be raised for illegal
     indexes to allow proper detection of the end of a sequence.

   Nota:

     When subscripting a *class*, the special class method
     "__class_getitem__()" may be called instead of "__getitem__()".
     See __class_getitem__ versus __getitem__ for more details.

object.__setitem__(self, key, value)

   Chamado para implementar a atribuição de "self[key]". Mesma nota
   que para "__getitem__()". Isso só deve ser implementado para
   mapeamentos se os objetos suportarem alterações nos valores das
   chaves, ou se novas chaves puderem ser adicionadas, ou para
   sequências se os elementos puderem ser substituídos. As mesmas
   exceções devem ser levantadas para valores *key* impróprios do
   método "__getitem__()".

object.__delitem__(self, key)

   Chamado para implementar a exclusão de "self[key]". Mesma nota que
   para "__getitem__()". Isso só deve ser implementado para
   mapeamentos se os objetos suportarem remoções de chaves, ou para
   sequências se os elementos puderem ser removidos da sequência. As
   mesmas exceções devem ser levantadas para valores *key* impróprios
   do método "__getitem__()".

object.__missing__(self, key)

   Chamado por "dict"."__getitem__()" para implementar "self[key]"
   para subclasses de dicionário quando a chave não estiver no
   dicionário.

object.__iter__(self)

   Este método é chamado quando um *iterador* é necessário para um
   contêiner. Este método deve retornar um novo objeto iterador que
   pode iterar sobre todos os objetos no contêiner. Para mapeamentos,
   ele deve iterar sobre as chaves do contêiner.

object.__reversed__(self)

   Chamado (se presente) pelo "reversed()" embutido para implementar a
   iteração reversa. Ele deve retornar um novo objeto iterador que
   itera sobre todos os objetos no contêiner na ordem reversa.

   Se o método "__reversed__()" não for fornecido, o "reversed()"
   embutido voltará a usar o protocolo de sequência ("__len__()" e
   "__getitem__()"). Objetos que suportam o protocolo de sequência só
   devem fornecer "__reversed__()" se eles puderem fornecer uma
   implementação que seja mais eficiente do que aquela fornecida por
   "reversed()".

Os operadores de teste de associação ("in" e "not in") são normalmente
implementados como uma iteração através de um contêiner. No entanto,
os objetos contêiner podem fornecer o seguinte método especial com uma
implementação mais eficiente, que também não requer que o objeto seja
iterável.

object.__contains__(self, item)

   Chamado para implementar operadores de teste de associação. Deve
   retornar verdadeiro se *item* estiver em *self*, falso caso
   contrário. Para objetos de mapeamento, isso deve considerar as
   chaves do mapeamento em vez dos valores ou pares de itens-chave.

   Para objetos que não definem "__contains__()", o teste de
   associação primeiro tenta a iteração via "__iter__()", depois o
   protocolo de iteração de sequência antigo via "__getitem__()",
   consulte esta seção em a referência da linguagem.


3.3.8. Emulando tipos numéricos
-------------------------------

Os métodos a seguir podem ser definidos para emular objetos numéricos.
Métodos correspondentes a operações que não são suportadas pelo tipo
particular de número implementado (por exemplo, operações bit a bit
para números não inteiros) devem ser deixados indefinidos.

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)

   Esses métodos são chamados para implementar as operações
   aritméticas binárias ("+", "-", "*", "@", "/", "//", "%",
   "divmod()", "pow()", "**", "<<", ">>", "&", "^", "|"). Por exemplo,
   para avaliar a expressão "x + y", onde *x* é uma instância de uma
   classe que tem um método "__add__()", "type(x).__add__(x, y)" é
   chamado. O método "__divmod__()" deve ser equivalente a usar
   "__floordiv__()" e "__mod__()"; não deve estar relacionado a
   "__truediv__()". Note que "__pow__()" deve ser definido para
   aceitar um terceiro argumento opcional se a versão de três
   argumentos da função embutida "pow()" for suportada.

   Se um desses métodos não suporta a operação com os argumentos
   fornecidos, ele deve retornar "NotImplemented".

object.__radd__(self, other)
object.__rsub__(self, other)
object.__rmul__(self, other)
object.__rmatmul__(self, other)
object.__rtruediv__(self, other)
object.__rfloordiv__(self, other)
object.__rmod__(self, other)
object.__rdivmod__(self, other)
object.__rpow__(self, other[, modulo])
object.__rlshift__(self, other)
object.__rrshift__(self, other)
object.__rand__(self, other)
object.__rxor__(self, other)
object.__ror__(self, other)

   Esses métodos são chamados para implementar as operações
   aritméticas binárias ("+", "-", "*", "@", "/", "//", "%",
   "divmod()", "pow()", "**", "<<", ">>", "&", "^", "|") com operandos
   refletidos (trocados). Essas funções são chamadas apenas se os
   operandos tiverem tipos diferentes, quando o operando esquerdo não
   oferecer suporte a operação correspondente [3], ou a classe do
   operando direito é derivada da classe do operando esquerdo. [4] Por
   exemplo, para avaliar a expressão "x - y", onde *y* é uma instância
   de uma classe que tem um método "__rsub__()", "type(y).__rsub__(y,
   x)" é chamado se "type(x).__sub__(x, y)" retorna "NotImplemented"
   ou "type(y)" é uma subclasse de "type(x)". [5]

   Observe que "__rpow__()" deve ser definido para aceitar um terceiro
   argumento opcional se a versão de três argumentos da função
   embutida "pow()" for suportada.

   Alterado na versão 3.14: "pow()" de três argumentos agora tenta
   chamar "__rpow__()" se necessário. Anteriormente, ele só era
   chamado em "pow()" de dois argumentos e no operador binário de
   potência.

   Nota:

     Se o tipo do operando direito for uma subclasse do tipo do
     operando esquerdo e essa subclasse fornecer uma implementação
     diferente do método refletido para a operação, este método será
     chamado antes do método não refletido do operando esquerdo. Esse
     comportamento permite que as subclasses substituam as operações
     de seus ancestrais.

object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__imatmul__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)

   Esses métodos são chamados para implementar as atribuições
   aritméticas aumentadas ("+=", "-=", "*=", "@=", "/=", "//=", "%=",
   "**=", "<<=", ">>=", "&=", "^=", "|="). Esses métodos devem tentar
   fazer a operação no local (modificando *self*) e retornar o
   resultado (que poderia ser, mas não precisa ser, *self*). Se um
   método específico não for definido, ou se esse método retorna
   "NotImplemented", a atribuição aumentada volta aos métodos normais.
   Por exemplo, se *x* é uma instância de uma classe com um método
   "__iadd__()", "x += y" equivale a "x = x.__iadd__(y)". Se
   "__iadd__()" não existe, ou se "x.__iadd__(y)" retorna
   "NotImplemented", "x.__add__(y)" e "y.__radd__(x)" são
   considerados, como com a avaliação de "x + y". Em certas situações,
   a atribuição aumentada pode resultar em erros inesperados (veja
   Porque uma_tupla[i] += ['item'] levanta uma exceção quando a adição
   funciona?), mas este comportamento é na verdade parte do modelo de
   dados.

object.__neg__(self)
object.__pos__(self)
object.__abs__(self)
object.__invert__(self)

   Chamado para implementar as operações aritméticas unárias ("-",
   "+", "abs()" e "~").

object.__complex__(self)
object.__int__(self)
object.__float__(self)

   Chamado para implementar as funções embutidas "complex()", "int()"
   e "float()". Deve retornar um valor do tipo apropriado.

object.__index__(self)

   Chamado para implementar "operator.index()", e sempre que o Python
   precisar converter sem perdas o objeto numérico em um objeto
   inteiro (como no fatiamento ou nas funções embutidas "bin()",
   "hex()" e "oct()"). A presença deste método indica que o objeto
   numérico é do tipo inteiro. Deve retornar um número inteiro.

   Se "__int__()", "__float__()" e "__complex__()" não estiverem
   definidos, funções embutidas correspondentes "int()", "float()" e
   "complex()" recorre a "__index__()".

object.__round__(self[, ndigits])
object.__trunc__(self)
object.__floor__(self)
object.__ceil__(self)

   Chamado para implementar as funções embutidas "round()" e
   "trunc()", "floor()" e "ceil()" de "math". A menos que *ndigits*
   sejam passados para "__round__()" todos estes métodos devem
   retornar o valor do objeto truncado para um "Integral" (tipicamente
   um "int").

   Alterado na versão 3.14: "int()" não delega mais ao método
   "__trunc__()".


3.3.9. Gerenciadores de contexto da instrução with
--------------------------------------------------

Um *gerenciador de contexto* é um objeto que define o contexto de
tempo de execução a ser estabelecido ao executar uma instrução "with".
O gerenciador de contexto lida com a entrada e a saída do contexto de
tempo de execução desejado para a execução do bloco de código. Os
gerenciadores de contexto são normalmente invocados usando a instrução
"with" (descrita na seção A instrução with), mas também podem ser
usados invocando diretamente seus métodos.

Os usos típicos de gerenciadores de contexto incluem salvar e
restaurar vários tipos de estado global, travar e destravar recursos,
fechar arquivos abertos, etc.

Para mais informações sobre gerenciadores de contexto, veja Tipos de
Gerenciador de Contexto. A classe "object" em si não fornece os
métodos do gerenciador de contexto.

object.__enter__(self)

   Insere o contexto de tempo de execução relacionado a este objeto. A
   instrução "with" vinculará o valor de retorno deste método ao(s)
   alvo(s) especificado(s) na cláusula "as" da instrução, se houver.

object.__exit__(self, exc_type, exc_value, traceback)

   Sai do contexto de tempo de execução relacionado a este objeto. Os
   parâmetros descrevem a exceção que fez com que o contexto fosse
   encerrado. Se o contexto foi encerrado sem exceção, todos os três
   argumentos serão "None".

   Se uma exceção for fornecida e o método desejar suprimir a exceção
   (ou seja, evitar que ela seja propagada), ele deve retornar um
   valor verdadeiro. Caso contrário, a exceção será processada
   normalmente ao sair deste método.

   Observe que os métodos "__exit__()" não devem relançar a exceção
   passada; esta é a responsabilidade do chamador.

Ver também:

  **PEP 343** - A instrução "with"
     A especificação, o histórico e os exemplos para a instrução
     Python "with".


3.3.10. Customizando argumentos posicionais na classe correspondência de padrão
-------------------------------------------------------------------------------

Ao usar um nome de classe em um padrão, argumentos posicionais não são
permitidos por padrão, ou seja, "case MyClass(x, y)" é tipicamente
inválida sem suporte especial em "MyClass". Para permitir a utilização
desse tipo de padrão, a classe precisa definir um atributo
*__match_args__*

object.__match_args__

   Essa variável de classe pode ser atribuída a uma tupla de strings.
   Quando essa classe é usada em uma classe padrão com argumentos
   posicionais, cada argumento posicional será convertido para um
   argumento nomeado, usando correspondência de valor em
   *__match_args__* como palavra reservada. A ausência desse atributo
   é equivalente a defini-lo como "()"

Por exemplo, se "MyClass.__match_args__" é "("left", "center",
"right")" significa que "case MyClass(x, y)" é equivalente a "case
MyClass(left=x, center=y)". Note que o número de argumentos no padrão
deve ser menor ou igual ao número de elementos em *__match_args__*;
caso seja maior, a tentativa de correspondência de padrão irá levantar
uma "TypeError".

Adicionado na versão 3.10.

Ver também:

  **PEP 634** - Correspondência de Padrão Estrutural
     A especificação para a instrução Python "match"


3.3.11. Emulando tipos buffer
-----------------------------

O protocolo buffer fornece uma maneira para objetos Python exporem
acesso eficiente a um vetor de memória de baixo nível. Este protocolo
é implementado por tipos embutido como "bytes" e "memoryview", e
bibliotecas de terceiros podem definir tipos de buffer adicionais.

Embora os tipos buffer sejam geralmente implementados em C, também é
possível implementar o protocolo em Python.

object.__buffer__(self, flags)

   Chamado quando um buffer é solicitado de *self* (por exemplo, pelo
   construtor de "memoryview"). O argumento *flags* é um inteiro que
   representa o tipo de buffer solicitado, afetando, por exemplo, se o
   buffer retornado é somente leitura ou gravável.
   "inspect.BufferFlags" fornece uma maneira conveniente de
   interpretar os sinalizadores. O método deve retornar um objeto
   "memoryview".

   **Thread safety:** In *free-threaded* Python, implementations must
   manage any internal export counter using atomic operations. The
   method must be safe to call concurrently from multiple threads, and
   the returned buffer's underlying data must remain valid until the
   corresponding "__release_buffer__()" call completes. See Segurança
   para thread para objetos memoryview for details.

object.__release_buffer__(self, buffer)

   Called when a buffer is no longer needed. The *buffer* argument is
   a "memoryview" object that was previously returned by
   "__buffer__()". The method must release any resources associated
   with the buffer. This method should return "None".

   **Thread safety:** In *free-threaded* Python, any export counter
   decrement must use atomic operations. Resource cleanup must be
   thread-safe, as the final release may race with concurrent releases
   from other threads.

   Buffer objects that do not need to perform any cleanup are not
   required to implement this method.

Adicionado na versão 3.12.

Ver também:

  **PEP 688** - Tornando o protocolo de buffer acessível no Python
     Introduz os métodos "__buffer__" e "__release_buffer__" no Python

  "collections.abc.Buffer"
     ABC para tipos buffer.


3.3.12. Anotações
-----------------

Funções, classes e módulos podem conter *anotações*, que são uma
maneira de associar informações (geralmente *dicas de tipo*) a um
símbolo.

object.__annotations__

   Este atributo contém as anotações de um objeto. Ele é avaliado
   preguiçosamente, portanto, acessá-lo pode executar código
   arbitrário e levantar exceções. Se a avaliação for bem-sucedida, o
   atributo é definido como um mapeamento de dicionário de nomes de
   variáveis para anotações.

   Alterado na versão 3.14: Anotações são agora avaliados
   preguiçosamente.

object.__annotate__(format)

   Uma *função de anotação*. Retorna um novo objeto dicionário
   mapeando nomes de atributos/parâmetros aos seus valores de
   anotação.

   Recebe um parâmetro de formato que especifica o formato em que os
   valores das anotações devem ser fornecidos. Deve ser um membro da
   enumeração "annotationlib.Format" ou um inteiro com um valor
   correspondente a um membro da enumeração.

   Se uma função de anotação não oferecer suporte ao formato
   solicitado, ela deverá levantar "NotImplementedError". Funções de
   anotação devem sempre oferecer suporte ao formato "VALUE"; elas não
   devem levantar "NotImplementedError()" quando chamadas com este
   formato.

   Quando chamada com o formato "VALUE", uma função de anotação pode
   levantar "NameError"; ela não deve levantar "NameError" quando
   chamada solicitando qualquer outro formato.

   Se um objeto não tiver nenhuma anotação, "__annotate__" deve ser
   preferencialmente definido como "None" (não pode ser excluído), em
   vez de ser definido como uma função que retorna um dicionário
   vazio.

   Adicionado na versão 3.14.

Ver também:

  **PEP 649** --- Avaliação diferida de anotação usando descritores
     Apresenta a avaliação preguiçosa de anotações e a função
     "__annotate__".


3.3.13. Pesquisa de método especial
-----------------------------------

Para classes personalizadas, as invocações implícitas de métodos
especiais só têm garantia de funcionar corretamente se definidas em um
tipo de objeto, não no dicionário de instância do objeto. Esse
comportamento é o motivo pelo qual o código a seguir levanta uma
exceção:

   >>> class C:
   ...     pass
   ...
   >>> c = C()
   >>> c.__len__ = lambda: 5
   >>> len(c)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: object of type 'C' has no len()

A justificativa por trás desse comportamento está em uma série de
métodos especiais como "__hash__()" e "__repr__()" que são
implementados por todos os objetos, incluindo objetos de tipo. Se a
pesquisa implícita desses métodos usasse o processo de pesquisa
convencional, eles falhariam quando invocados no próprio objeto do
tipo:

   >>> 1 .__hash__() == hash(1)
   True
   >>> int.__hash__() == hash(int)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: descriptor '__hash__' of 'int' object needs an argument

A tentativa incorreta de invocar um método não vinculado de uma classe
dessa maneira é às vezes referida como "confusão de metaclasse" e é
evitada ignorando a instância ao pesquisar métodos especiais:

   >>> type(1).__hash__(1) == hash(1)
   True
   >>> type(int).__hash__(int) == hash(int)
   True

Além de contornar quaisquer atributos de instância no interesse da
correção, a pesquisa de método especial implícita geralmente também
contorna o método "__getattribute__()" mesmo da metaclasse do objeto:

   >>> class Meta(type):
   ...     def __getattribute__(*args):
   ...         print("Metaclass getattribute invoked")
   ...         return type.__getattribute__(*args)
   ...
   >>> class C(object, metaclass=Meta):
   ...     def __len__(self):
   ...         return 10
   ...     def __getattribute__(*args):
   ...         print("Class getattribute invoked")
   ...         return object.__getattribute__(*args)
   ...
   >>> c = C()
   >>> c.__len__()                 # Explicit lookup via instance
   Class getattribute invoked
   10
   >>> type(c).__len__(c)          # Explicit lookup via type
   Metaclass getattribute invoked
   10
   >>> len(c)                      # Implicit lookup
   10

Ignorar a maquinaria de "__getattribute__()" desta forma fornece um
escopo significativo para otimizações de velocidade dentro do
interpretador, ao custo de alguma flexibilidade no tratamento de
métodos especiais (o método especial *deve* ser definido no próprio
objeto classe em ordem ser invocado de forma consistente pelo
interpretador).


3.4. Corrotinas
===============


3.4.1. Objetos aguardáveis
--------------------------

Um objeto *aguardável* geralmente implementa um método "__await__()".
Os *objetos corrotina* retornados das funções "async def" são
aguardáveis.

Nota:

  Os objetos *iteradores geradores* retornados de geradores decorados
  com "types.coroutine()" também são aguardáveis, mas eles não
  implementam "__await__()".

object.__await__(self)

   Deve retornar um *iterador*. Deve ser usado para implementar
   objetos *aguardáveis*. Por exemplo, "asyncio.Future" implementa
   este método para ser compatível com a expressão "await". A classe
   "object" em si não é aguardável e não fornece este método.

   Nota:

     A linguagem não impõe nenhuma restrição ao tipo ou valor dos
     objetos produzidos pelo iterador retornado por "__await__", pois
     isso é específico para a implementação da estrutura de execução
     assíncrona (por exemplo, "asyncio") que gerenciará o objeto
     *awaitable*.

Adicionado na versão 3.5.

Ver também:

  **PEP 492** para informações adicionais sobre objetos aguardáveis.


3.4.2. Objetos corrotina
------------------------

*Objetos corrotina* são objetos *aguardáveis*. A execução de uma
corrotina pode ser controlada chamando "__await__()" e iterando sobre
o resultado. Quando a corrotina termina a execução e retorna, o
iterador levanta "StopIteration", e o atributo "value" da exceção
contém o valor de retorno. Se a corrotina levantar uma exceção, ela
será propagada pelo iterador. As corrotinas não devem levantar
exceções "StopIteration" diretamente não tratadas.

As corrotinas também têm os métodos listados abaixo, que são análogos
aos dos geradores (ver Iteradores geradores). No entanto, ao contrário
dos geradores, as corrotinas não suportam diretamente a iteração.

Coroutines are generic over the types of their yield, send, and return
values, respectively.

Alterado na versão 3.5.2: É uma "RuntimeError" para aguardar uma
corrotina mais de uma vez.

coroutine.send(value)

   Inicia ou retoma a execução da corrotina. Se *value* for "None",
   isso equivale a avançar o iterador retornado por "__await__()". Se
   *value* não for "None", este método delega para o método "send()"
   do iterador que causou a suspensão da corrotina. O resultado (valor
   de retorno, "StopIteration" ou outra exceção) é o mesmo de iterar
   sobre o valor de retorno "__await__()", descrito acima.

coroutine.throw(value)
coroutine.throw(type[, value[, traceback]])

   Levanta a exceção especificada na corrotina. Este método delega ao
   método "throw()" do iterador que causou a suspensão da corrotina,
   se ela tiver tal método. Caso contrário, a exceção é levantada no
   ponto de suspensão. O resultado (valor de retorno, "StopIteration"
   ou outra exceção) é o mesmo de iterar sobre o valor de retorno
   "__await__()", descrito acima. Se a exceção não for capturada na
   corrotina, ela se propagará de volta para o chamador.

   Alterado na versão 3.12: A segunda assinatura (tipo[, valor[,
   traceback]]]) foi descontinuada e pode ser removida em uma versão
   futura do Python.

coroutine.close()

   Faz com que a corrotina se limpe e saia. Se a corrotina for
   suspensa, este método primeiro delega para o método "close()" do
   iterador que causou a suspensão da corrotina, se tiver tal método.
   Então ele levanta "GeneratorExit" no ponto de suspensão, fazendo
   com que a corrotina se limpe imediatamente. Por fim, a corrotina é
   marcada como tendo sua execução concluída, mesmo que nunca tenha
   sido iniciada.

   Objetos corrotina são fechados automaticamente usando o processo
   acima quando estão prestes a ser destruídos.


3.4.3. Iteradores assíncronos
-----------------------------

Um *iterador assíncrono* pode chamar código assíncrono em seu método
"__anext__".

Os iteradores assíncronos podem ser usados em uma instrução "async
for".

A classe "object" em si não fornece estes métodos.

object.__aiter__(self)

   Deve retornar um objeto *iterador assíncrono*.

object.__anext__(self)

   Deve retornar um *aguardável* resultando em um próximo valor do
   iterador. Deve levantar um erro "StopAsyncIteration" quando a
   iteração terminar.

Um exemplo de objeto iterável assíncrono:

   class Reader:
       async def readline(self):
           ...

       def __aiter__(self):
           return self

       async def __anext__(self):
           val = await self.readline()
           if val == b'':
               raise StopAsyncIteration
           return val

Adicionado na versão 3.5.

Alterado na versão 3.7: Antes do Python 3.7, "__aiter__()" poderia
retornar um *aguardável* que resolveria para um *iterador
assíncrono*.A partir do Python 3.7, "__aiter__()" deve retornar um
objeto iterador assíncrono. Retornar qualquer outra coisa resultará em
um erro "TypeError".


3.4.4. Gerenciadores de contexto assíncronos
--------------------------------------------

Um *gerenciador de contexto assíncrono* é um *gerenciador de contexto*
que é capaz de suspender a execução em seus métodos "__aenter__" e
"__aexit__".

Os gerenciadores de contexto assíncronos podem ser usados em uma
instrução "async with".

A classe "object" em si não fornece estes métodos.

object.__aenter__(self)

   Semanticamente semelhante a "__enter__()", a única diferença é que
   ele deve retornar um *aguardável*.

object.__aexit__(self, exc_type, exc_value, traceback)

   Semanticamente semelhante a "__exit__()", a única diferença é que
   ele deve retornar um *aguardável*.

Um exemplo de uma classe gerenciadora de contexto assíncrona:

   class AsyncContextManager:
       async def __aenter__(self):
           await log('entrando no contexto')

       async def __aexit__(self, exc_type, exc, tb):
           await log('saindo do contexto')

Adicionado na versão 3.5.

-[ Notas de rodapé ]-

[1] Em alguns casos, *é* possível alterar o tipo de um objeto, sob
    certas condições controladas. No entanto, geralmente não é uma boa
    ideia, pois pode levar a um comportamento muito estranho se for
    tratado incorretamente.

[2] Os métodos "__hash__()", "__iter__()", "__reversed__()" e
    "__contains__()", "__class_getitem__()" e "__fspath__()" têm um
    tratamento especial para isso. Outros ainda irão levantar um
    "TypeError", mas podem fazer isso contando com o comportamento de
    que "None" não é chamável.

[3] "Não suportar" aqui significa que a classe não possui tal método,
    ou o método retorna "NotImplemented". Não defina o método como
    "None" se quiser forçar o fallback para o método refletido do
    operando correto -- isso terá o efeito oposto de *bloquear*
    explicitamente esse fallback.

[4] Para operandos do mesmo tipo, presume-se que se o método não
    refletido (como "__add__()") falhar, a operação não será
    suportada, razão pela qual o método refletido não é chamado.

[5] Se o tipo do operando direito for uma subclasse do tipo do
    operando esquerdo, o método tendo precedência permite que as
    subclasses substituam as operações de seus ancestrais.
