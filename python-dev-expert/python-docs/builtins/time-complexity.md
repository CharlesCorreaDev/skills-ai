Complexidade de tempo de operações em tipos embutidos
*****************************************************

Esta página documenta a complexidade de tempo de várias operações em
tipos nativos no CPython. Outras implementações do Python podem
apresentar características de desempenho diferentes. Além disso, os
custos listados pressupõem os tipos nativos exatos, uma vez que
instâncias de subclasses podem ter custos diferentes.

Utilizamos a Big *O* notation para descrever como o tempo de execução
de uma operação cresce em função do tamanho de suas entradas. A menos
que indicado de outra forma, *n* representa o número de elementos
atualmente no contêiner, e *k* é o valor de um parâmetro numérico,
como um índice ou uma contagem de repetições.


"list"
======

Listas são sequências mutáveis; para mais detalhes sobre a
implementação, consulte Como as listas são implementadas no CPython?.
Os custos mais elevados ocorrem ao expandir a lista além do tamanho de
alocação atual (pois todos os elementos precisam ser movidos) ou ao
inserir ou remover itens próximos ao início (pois todos os elementos
subsequentes precisam ser movidos). Se você precisar adicionar ou
remover itens em ambas as extremidades, considere usar um
"collections.deque" em vez disso.

+----------------------------------------------------+----------------------------------------------------+
| Operação                                           | Complexidade                                       |
|====================================================|====================================================|
| Cópia ("l.copy()")                                 | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Anexação ao final ("l.append(x)") [1]              | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Pop ("l.pop(k)") [1] [2]                           | *O*(*n* - *k*)                                     |
+----------------------------------------------------+----------------------------------------------------+
| Inserção ("l.insert(k, x)") [1] [2]                | *O*(*n* - *k*)                                     |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de item ("l[k]")                          | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Definição de item ("l[k] = x")                     | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Exclusão de item ("del l[k]") [2]                  | *O*(*n* - *k*)                                     |
+----------------------------------------------------+----------------------------------------------------+
| Iteração                                           | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de fatia ("l[i:j]")                       | *O*(*j* - *i*)                                     |
+----------------------------------------------------+----------------------------------------------------+
| Definição de fatia ("l[i:j] = t") [1]              | *O*(*j* - *i*) if len(*t*) == *j* - *i*, do        |
|                                                    | contrário *O*(*n* - *i* + len(*t*))                |
+----------------------------------------------------+----------------------------------------------------+
| Exclusão de fatia ("del l[i:j]")                   | *O*(*n* - *i*)                                     |
+----------------------------------------------------+----------------------------------------------------+
| Estensão ("l.extend(t)") [1] [3]                   | *O*(len(*t*))                                      |
+----------------------------------------------------+----------------------------------------------------+
| Ordenação ("l.sort()") [4]                         | *O*(*n* log *n*)                                   |
+----------------------------------------------------+----------------------------------------------------+
| Concatenação ("l1 + l2")                           | *O*(len(*l1*) + len(*l2*))                         |
+----------------------------------------------------+----------------------------------------------------+
| Multiplicação ("l * k")                            | *O*(*nk*)                                          |
+----------------------------------------------------+----------------------------------------------------+
| "x in l"                                           | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| "min(l)", "max(l)"                                 | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de comprimento ("len(l)") [5]             | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+


"tuple"
=======

Uma "tuple" é uma sequência *imutável*. Como uma tupla nunca pode ser
alterada, não há custos de inserção ou remoção, e criar uma cópia
simplesmente retorna o mesmo objeto; portanto, a operação ocorre em
tempo constante (*O*(1)).

+----------------------------------------------------+----------------------------------------------------+
| Operação                                           | Complexidade                                       |
|====================================================|====================================================|
| Cópia ("tuple(t)")                                 | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de item ("t[k]")                          | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de fatia ("t[i:j]")                       | *O*(*j* - *i*)                                     |
+----------------------------------------------------+----------------------------------------------------+
| Concatenação ("t1 + t2")                           | *O*(len(*t1*) + len(*t2*))                         |
+----------------------------------------------------+----------------------------------------------------+
| Multiplicação ("t * k")                            | *O*(*nk*)                                          |
+----------------------------------------------------+----------------------------------------------------+
| Iteração                                           | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| "x in t"                                           | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| "min(t)", "max(t)"                                 | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de comprimento ("len(t)") [5]             | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+


"dict", "frozendict"
====================

Os tempos listados para objetos do tipo *dict* referem-se a casos
médios, pois pressupõem que a função de *hash* utilizada seja
suficientemente robusta para tornar incomuns as colisões. Também
pressupõem que as chaves estejam bem distribuídas no conjunto de
chaves possíveis. No pior caso — quando todas as chaves resultam no
mesmo valor de *hash* —, cada uma das operações *O*(1) listadas abaixo
passa a exigir tempo *O*(*n*). Além disso, eles pressupõem que as
operações de *hashing* e comparação de chaves ocorrem em tempo *O*(1).
Para mais detalhes sobre a implementação, consulte Como são os
dicionários implementados no CPython?.

Um "frozendict" é imutável; portanto, não oferece suporte à definição,
exclusão ou a atualização de itens. As outras operações listadas
abaixo aplicam-se a ele com os mesmos custos.

+----------------------------------------------------+----------------------------------------------------+
| Operação                                           | Complexidade                                       |
|====================================================|====================================================|
| "key in d"                                         | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Cópia ("d.copy()") [6] [7]                         | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de item ("d[key]", "d.get(key)")          | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Definição de item ("d[key] = value") [1]           | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Exclusão de item ("del d[key]", "d.pop(key)")      | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Atualização ("d.update(t)", "d |= t") [1] [3] [7]  | *O*(len(*t*))                                      |
+----------------------------------------------------+----------------------------------------------------+
| Iteração [7]                                       | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de comprimento ("len(d)") [5]             | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+


"set", "frozenset"
==================

Consulte "dict", pois as implementações de "set" e "frozenset" são
semelhantes e as mesmas ressalvas se aplicam. No pior caso, operações
de *O*(1) passam a levar tempo *O*(*n*), e operações que percorrem
todos os elementos sofrem uma degradação de desempenho correspondente.

Um "frozenset" é *imutável*, portanto, não oferece suporte a operações
de adição, descarte ou atualização local (*in-place*). As demais
operações listadas abaixo aplicam-se a ele com os mesmos custos.

+----------------------------------------------------+----------------------------------------------------+
| Operação                                           | Complexidade                                       |
|====================================================|====================================================|
| "x in s"                                           | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Cópia ("s.copy()") [6] [7]                         | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Adição ("s.add(x)") [1]                            | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Descarte ("s.discard(x)", "s.remove(x)")           | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| União ("s1 | s2", "s1.union(s2)") [7]              | *O*(len(*s1*) + len(*s2*))                         |
+----------------------------------------------------+----------------------------------------------------+
| Atualização ("s1 |= s2", "s1.update(s2)") [1] [7]  | *O*(len(*s2*))                                     |
+----------------------------------------------------+----------------------------------------------------+
| Interseção ("s1 & s2", "s1.intersection(s2)") [7]  | *O*(min(len(*s1*), len(*s2*)))                     |
| [8]                                                |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| Atualização de interseção ("s1 &= s2",             | *O*(min(len(*s1*), len(*s2*)))                     |
| "s1.intersection_update(s2)") [1] [7] [8]          |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| Diferença ("s1 - s2", "s1.difference(s2)") [7] [9] | *O*(len(*s1*))                                     |
+----------------------------------------------------+----------------------------------------------------+
| Atualização de diferença ("s1 -= s2",              | *O*(min(len(*s1*), len(*s2*)))                     |
| "s1.difference_update(s2)") [1] [7] [8]            |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| Diferença simétrica ("s1 ^ s2",                    | *O*(len(*s1*) + len(*s2*))                         |
| "s1.symmetric_difference(s2)") [7]                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| Atualização de diferença simétrica ("s1 ^= s2",    | *O*(len(*s2*))                                     |
| "s1.symmetric_difference_update(s2)") [1] [7]      |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de comprimento ("len(s)") [5]             | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+


"str", "bytes", "bytearray"
===========================

Objetos "str" e "bytes" são sequências imutáveis de caracteres e
bytes, respectivamente. Assim como ocorre com as tuplas, copiar um
deles retorna o objeto original. Um "bytearray" é mutável e, além
disso, oferece suporte às operações de modificação de "list" (exceto
"sort()"), com os mesmos custos. No entanto, a exclusão no início
utilizando "del" ("del b[0]", "del b[:k]") apenas avança o início do
buffer, em vez de mover os bytes restantes, resultando em uma
complexidade amortizada *O*(1).

+----------------------------------------------------+----------------------------------------------------+
| Operação                                           | Complexidade                                       |
|====================================================|====================================================|
| Obtenção de item ("s[k]")                          | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de fatia ("s[i:j]")                       | *O*(*j* - *i*)                                     |
+----------------------------------------------------+----------------------------------------------------+
| Concatenação ("s + t") [10]                        | *O*(len(*s*) + len(*t*))                           |
+----------------------------------------------------+----------------------------------------------------+
| Multiplicação ("s * k")                            | *O*(*nk*)                                          |
+----------------------------------------------------+----------------------------------------------------+
| Busca por substring ("x in s", "s.find(x)",        | *O*(*n*)                                           |
| "s.index(x)") [11]                                 |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| Busca inversa por substring ("s.rfind(x)",         | *O*(*n* × len(*x*))                                |
| "s.rindex(x)") [11] [12]                           |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| Codificação e decodificação [13]                   | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Iteração                                           | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de comprimento ("len(s)") [5]             | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+


"memoryview"
============

Objetos "memoryview" permitem que código Python acesse os dados
internos de um objeto que implemente o protocolo buffer sem copiá-lo.
Em especial, o fatiamento de uma view de memória retorna uma nova view
para o mesmo buffer.

+----------------------------------------------------+----------------------------------------------------+
| Operação                                           | Complexidade                                       |
|====================================================|====================================================|
| Criação ("memoryview(obj)")                        | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de item ("v[k]")                          | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de fatia ("v[i:j]")                       | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Índice ("v.index(x)") [11] [14]                    | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Contagem ("v.count(x)") [14]                       | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Conversão para bytes ("v.tobytes()", "bytes(v)")   | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de comprimento ("len(v)") [5]             | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+


"range"
=======

Um objeto "range" calcula seus itens sob demanda a partir de seus
valores de *start*, *stop* e *step*; portanto, a maioria das operações
não depende do comprimento do intervalo.

+----------------------------------------------------+----------------------------------------------------+
| Operação                                           | Complexidade                                       |
|====================================================|====================================================|
| Obtenção de item ("r[k]")                          | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de fatia ("r[i:j]")                       | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| "x in r" [15]                                      | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+
| Índice e contagem ("r.index(x)", "r.count(x)")     | *O*(1)                                             |
| [15]                                               |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| Iteração                                           | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| "min(r)", "max(r)"                                 | *O*(*n*)                                           |
+----------------------------------------------------+----------------------------------------------------+
| Obtenção de comprimento ("len(r)") [5]             | *O*(1)                                             |
+----------------------------------------------------+----------------------------------------------------+


Notas
=====

[1] Amortizado. Uma operação individual pode, ocasionalmente, ser
    *O*(*n*) quando o armazenamento subjacente é redimensionado, mas
    esse custo é distribuído por muitas operações, dependendo do
    histórico do contêiner.

[2] Retirar (*pop*) ou excluir o elemento no índice *k* de uma lista
    de tamanho *n* desloca todos os elementos após *k* uma posição
    para a esquerda, movimentando *n* - *k* - 1 elementos; inserir no
    índice *k* desloca os elementos a partir de *k* uma posição para a
    direita, movimentando *n* - *k* elementos. O pior caso ocorre no
    índice 0, onde todo o restante da lista precisa ser deslocado; o
    caso médio — um índice no meio da lista — requer *O*(*n*/2) =
    *O*(*n*) operações; e realizar a operação no final da lista não
    exige movimentação, sendo uma operação *O*(1).

[3] Além do custo de iterar sobre *t*, que pode ser elevado para um
    iterável arbitrário.

[4] Este é o pior cenário possível. A ordenação é adaptativa, e
    entradas já ordenadas ou ordenadas em ordem inversa requerem
    apenas *O*(*n*) comparações. Consulte Objects/listsort.txt para
    mais informações.

[5] O número de elementos é armazenado no objeto, portanto, "len()"
    não precisa contá-los.

[6] A cópia de um "frozendict" ou um "frozenset" é *O*(1), pois
    retorna o objeto original.

[7] Essas operações percorrem a tabela de hash interna do contêiner, a
    qual não é reduzida quando elementos são removidos. Mesmo após a
    remoção da maioria dos elementos, elas continuam levando um tempo
    proporcional ao tamanho anterior do contêiner, até que uma
    inserção posterior acione um redimensionamento.

[8] *O*(len(*t*)) se *t* não é um conjunto.

[9] *O*(len(*s*) + len(*t*)) se *t* não é um conjunto.

[10] Cada concatenação cria um novo objeto; portanto, construir uma
     string concatenando muitas partes em um laço tem complexidade
     quadrática em relação ao comprimento total. Consulte a nota sobre
     a concatenação de sequências imutáveis para ver alternativas.

[11] Com os argumentos *start* e *end*, *n* é o comprimento da região
     pesquisada, e não de *s*, e, ao contrário do fatiamento, nada é
     copiado.

[12] Este é o pior caso. As buscas inversas são *O*(*n*) para entradas
     típicas. Já as buscas diretas utilizam um algoritmo mais
     elaborado com complexidade linear no pior caso, descrito em
     Objects/stringlib/stringlib_find_two_way_notes.txt.

[13] Isso presume um codec que realiza uma quantidade constante de
     trabalho por caractere.

[14] Eles desempacotam e comparam cada elemento individualmente;
     portanto, são muito mais lentos do que os métodos equivalentes de
     "bytes".

[15] Presumindo os argumentos como sendo do tipo "int" ou "bool". Para
     outros tipos, o intervalo é pesquisado como qualquer outra
     sequência, em tempo *O*(*n*).
