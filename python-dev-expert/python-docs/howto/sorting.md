Técnicas de ordenação
*********************

As listas em Python possuem um método embutido "list.sort()" que
modifica a lista em si. Há também a função embutida "sorted()" que
constrói uma nova lista ordenada à partir de um iterável.

Neste documento, exploramos várias técnicas para ordenar dados
utilizando Python.


Básico de ordenação
===================

Uma ordenação ascendente simples é muito fácil: apenas chame a função
"sorted()". Você terá como retorno uma nova lista ordenada:

   >>> sorted([5, 2, 3, 1, 4])
   [1, 2, 3, 4, 5]

Você também pode utilizar o método "list.sort()". Ele modificará a
lista localmente (e retornará "None" para evitar confusão). Usualmente
este método é menos conveniente que a função "sorted()" - mas, se a
lista original não for posteriormente útil, esta maneira será
levemente mais eficiente.

   >>> a = [5, 2, 3, 1, 4]
   >>> a.sort()
   >>> a
   [1, 2, 3, 4, 5]

Outra diferença é que o método "list.sort()" é aplicável apenas às
listas. Em contrapartida, a função "sorted()" aceita qualquer
iterável.

   >>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
   [1, 2, 3, 4, 5]


Funções chave
=============

Tanto o método "list.sort()" quando as funções "sorted()", "min()",
"max()", "heapq.nsmallest()" e "heapq.nlargest()" possuem o parâmetro
*key*, que especifica uma função (ou outro chamável) a ser invocado
para cada elemento da lista antes de ser realizada a comparação.

Por exemplo, temos abaixo uma comparação de strings, sem distinção
entre caractéres maiúsculos e minúsculos, utilizando "str.casefold()":

   >>> sorted("Essa é uma string de teste do Andrew".split(), key=str.casefold)
   ['Andrew', 'de', 'do', 'Essa', 'string', 'teste', 'uma', 'é']

O valor do parâmetro *key* deve ser uma função (ou outro chamável) que
recebe um único argumento e retorna uma chave à ser utilizada na
ordenação. Como a função chave é chamada exatamente uma vez para cada
elemento, esta técnica é rápida.

Um padrão comum é ordenar objetos complexos utilizando um dos índices
do objeto como chave. Por exemplo:

   >>> tuplas_alunos = [
   ...     ('joão', 'A', 15),
   ...     ('joana', 'B', 12),
   ...     ('davi', 'B', 10),
   ... ]
   >>> sorted(tuplas_alunos, key=lambda aluno: aluno[2])   # ordena por idade
   [('davi', 'B', 10), ('joana', 'B', 12), ('joão', 'A', 15)]

A mesma técnica funciona com objetos que possuem atributos nomeados.
Por exemplo:

   >>> class Aluno:
   ...     def __init__(self, nome, nota, idade):
   ...         self.nome = nome
   ...         self.nota = nota
   ...         self.idade = idade
   ...     def __repr__(self):
   ...         return repr((self.nome, self.nota, self.idade))

   >>> objetos_alunos = [
   ...     Aluno('john', 'A', 15),
   ...     Aluno('jane', 'B', 12),
   ...     Aluno('dave', 'B', 10),
   ... ]
   >>> sorted(objetos_alunos, key=lambda aluno: aluno.idade)   # ordena por idade
   [('davi', 'B', 10), ('joana', 'B', 12), ('joão', 'A', 15)]

Objetos com atríbutos nomeados podem ser criados como uma classe
padrão, igual ao exemplo acima, podem ser instâncias de "dataclass" ou
mesmo uma *named tuple*.


Operator Module Functions and Partial Function Evaluation
=========================================================

O padrão de *função chave* mostrado acima é muito comum, por isso,
Python provê funções convenientes para tornar as funções de acesso
mais fáceis e rápidas. O módulo "operator" tem as funções
"itemgetter()", "attrgetter()" e "methodcaller()"

Usando estas funções, os exemplos acima se tornam mais simples e mais
rápidos:

   >>> from operator import itemgetter, attrgetter

   >>> sorted(student_tuples, key=itemgetter(2))
   [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

   >>> sorted(student_objects, key=attrgetter('age'))
   [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

As funções do módulo operator permite múltiplos níveis de ordenação.
Por exemplo, ordenar por *grade* e então por *age*:

   >>> sorted(student_tuples, key=itemgetter(1,2))
   [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

   >>> sorted(student_objects, key=attrgetter('grade', 'age'))
   [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

The "functools" module provides another helpful tool for making key-
functions.  The "partial()" function can reduce the arity of a multi-
argument function making it suitable for use as a key-function.

   >>> from functools import partial
   >>> from unicodedata import normalize

   >>> names = 'Zoë Åbjørn Núñez Élana Zeke Abe Nubia Eloise'.split()

   >>> sorted(names, key=partial(normalize, 'NFD'))
   ['Abe', 'Åbjørn', 'Eloise', 'Élana', 'Nubia', 'Núñez', 'Zeke', 'Zoë']

   >>> sorted(names, key=partial(normalize, 'NFC'))
   ['Abe', 'Eloise', 'Nubia', 'Núñez', 'Zeke', 'Zoë', 'Åbjørn', 'Élana']


Ascendente e descendente
========================

Tanto o método "list.sort()" quanto a função "sorted()" aceitam um
valor booleano para o parâmetro *reverse*. Essa flag é utilizada para
ordenações descendentes. Por exemplo, para retornar os dados de
estudantes pela ordem inversa de *age*:

   >>> sorted(student_tuples, key=itemgetter(2), reverse=True)
   [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

   >>> sorted(student_objects, key=attrgetter('age'), reverse=True)
   [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


Estabilidade de Ordenação e Ordenações Complexas
================================================

Ordenações são garantidas de serem estáveis. Isso significa que quando
múltiplos registros possuem a mesma chave, eles terão sua ordem
original preservada.

   >>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
   >>> sorted(data, key=itemgetter(0))
   [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]

Observe como os dois registros de *blue* permanecem em sua ordem
original de forma que "('blue',1)" é garantido de preceder
"('blue',2)".

Esta maravilhosa propriedade permite que você construa ordenações
complexas em uma série de passos de ordenação. Por exemplo, para
ordenar os registros de estudante por ordem descendente de *grade* e
então ascendente de *age*, primeiro ordene *age* e depois ordene
novamente utilizando *grade*:

   >>> s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
   >>> sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending
   [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

Isso pode ser abstrato no caso das funções invólucros que podem
receber uma lista e uma tupla com o campos e então ordená-los em
múltiplos passos.

   >>> def multisort(xs, specs):
   ...     for key, reverse in reversed(specs):
   ...         xs.sort(key=attrgetter(key), reverse=reverse)
   ...     return xs

   >>> multisort(list(student_objects), (('grade', True), ('age', False)))
   [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

O algoritmo Timsort utilizado no Python realiza múltiplas ordenações
de maneira eficiente, pois se aproveita de qualquer ordenação já
presente no conjunto de dados.


Decorate-Sort-Undecorate
========================

Esse item idiomático, chamado de Decorate-Sort-Undecorate, é realizado
em três passos:

* Primeiro, a lista inicial é decorada com novos valores que
  controlarão a ordem em que ocorrerá a ordenação

* Segundo, a lista decorada é ordenada.

* Finalmente, os valores decorados são removidos, criando uma lista
  que contém apenas os valores iniciais na nova ordenação.

Por exemplo, para ordenar os dados dos estudantes por *grade* usando a
abordagem DSU:

   >>> decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
   >>> decorated.sort()
   >>> [student for grade, i, student in decorated]               # undecorate
   [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

Esse padrão idiomático funciona porque tuplas são comparadas
lexicograficamente; os primeiros itens são comparados; se eles são
semelhantes, então os segundos itens são comparados e assim
sucessivamente.

Não é estritamente necessário incluir o índice *i* em todos os casos
de listas decoradas, mas fazer assim traz dois benefícios:

* A ordenação é estável - se dois itens tem a mesma chave, suas ordens
  serão preservadas na lista ordenada

* Os itens originais não precisarão ser comparados porque a ordenação
  de tuplas decoradas será determinada por no máximo os primeiros dois
  itens. Então, por exemplo, a lista original poderia conter números
  complexos que não poderão ser ordenados diretamente.

Outro nome para este padrão idiomático é Schwartzian transform de
Randal L. Schwartz, que popularizou isto entre os programadores Perl.

Agora que a ordenação do Python prevê funções-chave, essa técnica não
se faz mais necessária.


Funções de comparação
=====================

Unlike key functions that return an absolute value for sorting, a
comparison function computes the relative ordering for two inputs.

For example, a balance scale compares two samples giving a relative
ordering: lighter, equal, or heavier. Likewise, a comparison function
such as "cmp(a, b)" will return a negative value for less-than, zero
if the inputs are equal, or a positive value for greater-than.

It is common to encounter comparison functions when translating
algorithms from other languages.  Also, some libraries provide
comparison functions as part of their API.  For example,
"locale.strcoll()" is a comparison function.

To accommodate those situations, Python provides
"functools.cmp_to_key" to wrap the comparison function to make it
usable as a key function:

   sorted(words, key=cmp_to_key(strcoll))  # locale-aware sort order


Strategies For Unorderable Types and Values
===========================================

A number of type and value issues can arise when sorting. Here are
some strategies that can help:

* Convert non-comparable input types to strings prior to sorting:

   >>> data = ['twelve', '11', 10]
   >>> sorted(map(str, data))
   ['10', '11', 'twelve']

This is needed because most cross-type comparisons raise a
"TypeError".

* Remove special values prior to sorting:

   >>> from math import isnan
   >>> from itertools import filterfalse
   >>> data = [3.3, float('nan'), 1.1, 2.2]
   >>> sorted(filterfalse(isnan, data))
   [1.1, 2.2, 3.3]

This is needed because the IEEE-754 standard specifies that, "Every
NaN shall compare unordered with everything, including itself."

Likewise, "None" can be stripped from datasets as well:

   >>> data = [3.3, None, 1.1, 2.2]
   >>> sorted(x for x in data if x is not None)
   [1.1, 2.2, 3.3]

This is needed because "None" is not comparable to other types.

* Convert mapping types into sorted item lists before sorting:

   >>> data = [{'a': 1}, {'b': 2}]
   >>> sorted(data, key=lambda d: sorted(d.items()))
   [{'a': 1}, {'b': 2}]

This is needed because dict-to-dict comparisons raise a "TypeError".

* Convert set types into sorted lists before sorting:

   >>> data = [{'a', 'b', 'c'}, {'b', 'c', 'd'}]
   >>> sorted(map(sorted, data))
   [['a', 'b', 'c'], ['b', 'c', 'd']]

This is needed because the elements contained in set types do not have
a deterministic order.  For example, "list({'a', 'b'})" may produce
either "['a', 'b']" or "['b', 'a']".


Curiosidades e conclusões
=========================

* For locale aware sorting, use "locale.strxfrm()" for a key function
  or "locale.strcoll()" for a comparison function.  This is necessary
  because "alphabetical" sort orderings can vary across cultures even
  if the underlying alphabet is the same.

* O parâmetro *reverse* ainda mantém a estabilidade da ordenação (para
  que os registros com chaves iguais mantenham a ordem original).
  Curiosamente, esse efeito pode ser simulado sem o parâmetro usando a
  função embutida "reversed()" duas vezes:

     >>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
     >>> standard_way = sorted(data, key=itemgetter(0), reverse=True)
     >>> double_reversed = list(reversed(sorted(reversed(data), key=itemgetter(0))))
     >>> assert standard_way == double_reversed
     >>> standard_way
     [('red', 1), ('red', 2), ('blue', 1), ('blue', 2)]

* As rotinas de classificação usam "<" ao fazer comparações entre dois
  objetos. Portanto, é fácil adicionar uma ordem de classificação
  padrão a uma classe definindo um método "__lt__()":

     >>> Student.__lt__ = lambda self, other: self.age < other.age
     >>> sorted(student_objects)
     [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

  However, note that "<" can fall back to using "__gt__()" if
  "__lt__()" is not implemented (see "object.__lt__()" for details on
  the mechanics).  To avoid surprises, **PEP 8** recommends that all
  six comparison methods be implemented. The
  "@~functools.total_ordering" decorator is provided to make that task
  easier.

* As funções principais não precisam depender diretamente dos objetos
  que estão sendo ordenados. Uma função chave também pode acessar
  recursos externos. Por exemplo, se as notas dos alunos estiverem
  armazenadas em um dicionário, elas poderão ser usadas para ordenar
  uma lista separada de nomes de alunos:

     >>> students = ['dave', 'john', 'jane']
     >>> newgrades = {'john': 'F', 'jane':'A', 'dave': 'C'}
     >>> sorted(students, key=newgrades.__getitem__)
     ['jane', 'dave', 'john']


Ordenações parciais
===================

Some applications require only some of the data to be ordered.  The
standard library provides several tools that do less work than a full
sort:

* "min()" and "max()" return the smallest and largest values,
  respectively.  These functions make a single pass over the input
  data and require almost no auxiliary memory.

* "heapq.nsmallest()" and "heapq.nlargest()" return the *n* smallest
  and largest values, respectively.  These functions make a single
  pass over the data keeping only *n* elements in memory at a time.
  For values of *n* that are small relative to the number of inputs,
  these functions make far fewer comparisons than a full sort.

* "heapq.heappush()" and "heapq.heappop()" create and maintain a
  partially sorted arrangement of data that keeps the smallest element
  at position "0".  These functions are suitable for implementing
  priority queues which are commonly used for task scheduling.
