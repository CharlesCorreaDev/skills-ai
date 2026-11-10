"bisect" --- Algoritmo de bisseção de vetor
*******************************************

**Código-fonte:** Lib/bisect.py

======================================================================

Este módulo fornece suporte para manter uma lista em ordem de
classificação sem ter que classificar a lista após cada inserção. Para
longas listas de itens com operações de comparação caras, isso pode
ser uma melhoria em relação a pesquisas lineares ou recorrência
frequente.

The module is called "bisect" because it uses a basic bisection
algorithm to do its work.  Unlike other bisection tools that search
for a specific value, the functions in this module are designed to
locate an insertion point. Accordingly, the functions never call an
"__eq__()" method to determine whether a value has been found.
Instead, the functions only call the "__lt__()" method and will return
an insertion point between values in an array.

Nota:

  The functions in this module are not thread-safe. If multiple
  threads concurrently use "bisect" functions on the same sequence,
  this may result in undefined behaviour. Likewise, if the provided
  sequence is mutated by a different thread while a "bisect" function
  is operating on it, the result is undefined. For example, using
  "insort_left()" on the same list from multiple threads may result in
  the list becoming unsorted.

As seguintes funções são fornecidas:

bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)

   Localiza o ponto de inserção de *x* em *a* para manter a ordem de
   classificação. Os parâmetros *lo* e *hi* podem ser usados para
   especificar um subconjunto da lista que deve ser considerado; por
   padrão, toda a lista é usada. Se *x* já estiver presente em *a*, o
   ponto de inserção estará antes (à esquerda) de qualquer entrada
   existente. O valor de retorno é adequado para uso como o primeiro
   parâmetro para "list.insert()" supondo que *a* já esteja ordenado.

   O ponto de inserção retornado *ip* particiona o vetor *a* em duas
   fatias de forma que "all(elem < x for elem in a[lo : ip])" seja
   verdadeiro para a fatia esquerda e "all(elem >= x for elem in a[ip
   : hi])" é verdadeiro para a fatia certa.

   *key* especifica uma *função chave* de um argumento que é usado
   para extrair uma chave de comparação de cada elemento no vetor.
   Para oferecer suporte à pesquisa de registros complexos, a função
   chave não é aplicada ao valor *x*.

   Se *key* for "None", os elementos serão comparados diretamente e
   nenhuma função chave será chamada.

   Alterado na versão 3.10: Adicionado o  parâmetro *key*.

bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)
bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)

   Semelhante a "bisect_left()", mas retorna um ponto de inserção que
   vem depois (à direita de) qualquer entrada existente de *x* em *a*.

   O ponto de inserção retornado *ip* particiona o vetor *a* em duas
   fatias de forma que "all(elem <= x for elem in a[lo : ip])" seja
   verdadeiro para a fatia esquerda e "all(elem > x for elem in a[ip :
   hi])" é verdadeiro para a fatia certa.

   Alterado na versão 3.10: Adicionado o  parâmetro *key*.

bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)

   Insere *x* em *a* na ordem de classificação.

   Esta função primeiro executa "bisect_left()" para localizar um
   ponto de inserção. Em seguida, executa o método "insert()" em *a*
   para inserir *x* na posição apropriada para manter a ordem de
   classificação.

   Para oferecer suporte à inserção de registros em uma tabela, a
   função *key* (se houver) é aplicada a *x* para a etapa de pesquisa,
   mas não para a etapa de inserção.

   Tenha em mente que a busca *O*(log *n*) é dominada pelo etapa de
   inserção lenta O(n).

   Alterado na versão 3.10: Adicionado o  parâmetro *key*.

bisect.insort_right(a, x, lo=0, hi=len(a), *, key=None)
bisect.insort(a, x, lo=0, hi=len(a), *, key=None)

   Semelhante a "insort_left()", mas inserindo *x* em *a* após
   qualquer entrada existente de *x*.

   Esta função primeiro executa "bisect_right()" para localizar um
   ponto de inserção. Em seguida, executa o método "insert()" em *a*
   para inserir *x* na posição apropriada para manter a ordem de
   classificação.

   Para oferecer suporte à inserção de registros em uma tabela, a
   função *key* (se houver) é aplicada a *x* para a etapa de pesquisa,
   mas não para a etapa de inserção.

   Tenha em mente que a busca *O*(log *n*) é dominada pelo etapa de
   inserção lenta O(n).

   Alterado na versão 3.10: Adicionado o  parâmetro *key*.


Observações sobre desempenho
============================

Ao escrever um código sensível ao tempo usando *bisect()* e
*insort()*, lembre-se do seguinte:

* A bisseção é eficaz para pesquisar intervalos de valores. Para
  localizar valores específicos, os dicionários são mais eficientes.

* As funções *insort()* são *O*(*n*) porque a etapa de busca
  logarítmica é dominada pela etapa de inserção de tempo linear.

* The search functions are stateless and discard key function results
  after they are used.  Consequently, if the search functions are used
  in a loop, the key function may be called again and again on the
  same array elements. If the key function isn't fast, consider
  wrapping it with "@functools.cache" to avoid duplicate computations.
  Alternatively, consider searching an array of precomputed keys to
  locate the insertion point (as shown in the examples section below).

Ver também:

  * Sorted Collections é um módulo de alto desempenho que usa bisseção
    para gerenciar coleções de dados classificadas.

  * A receita de SortedCollection usa bisseção para construir uma
    classe de coleção completa com métodos de busca diretos e suporte
    para uma função chave. As chaves são pré-calculadas para
    economizar em chamadas desnecessárias para a função chave durante
    as buscas.


Buscando em listas ordenadas
============================

As funções de bisseção acima são úteis para encontrar pontos de
inserção, mas podem ser complicadas ou difíceis de usar para tarefas
comuns de busca. As cinco funções a seguir mostram como transformá-las
nas buscas padrão para listas ordenadas:

   def index(a, x):
       'Encontra o valor mais à esquerda exatamente igual a x'
       i = bisect_left(a, x)
       if i != len(a) and a[i] == x:
           return i
       raise ValueError

   def find_lt(a, x):
       'Encontra o valor mais à direita menor que x'
       i = bisect_left(a, x)
       if i:
           return a[i-1]
       raise ValueError

   def find_le(a, x):
       'Encontra o valor mais à direita menor ou igual a x'
       i = bisect_right(a, x)
       if i:
           return a[i-1]
       raise ValueError

   def find_gt(a, x):
       'Encontra o valor mais à esquerda maior que x'
       i = bisect_right(a, x)
       if i != len(a):
           return a[i]
       raise ValueError

   def find_ge(a, x):
       'Encontra o item mais à esquerda maior ou igual a x'
       i = bisect_left(a, x)
       if i != len(a):
           return a[i]
       raise ValueError


Exemplos
========

A função "bisect()" pode ser útil para buscas em tabelas numéricas.
Este exemplo usa "bisect()" para buscar uma nota em letra para uma
pontuação de exame (digamos) com base em um conjunto de pontos de
interrupção numéricos ordenados: 90 e acima é um "A", 80 a 89 é um "B"
e por aí vai:

   >>> def grade(score):
   ...     i = bisect([60, 70, 80, 90], score)
   ...     return "FDCBA"[i]
   ...
   >>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
   ['F', 'A', 'C', 'C', 'B', 'A', 'A']

As funções "bisect()" e "insort()" também funcionam com listas de
tuplas. O argumento *key* pode servir para extrair o campo usado para
ordenar registros em uma tabela:

   >>> from collections import namedtuple
   >>> from operator import attrgetter
   >>> from bisect import bisect, insort
   >>> from pprint import pprint

   >>> Movie = namedtuple('Movie', ('name', 'released', 'director'))

   >>> movies = [
   ...     Movie('Jaws', 1975, 'Spielberg'),
   ...     Movie('Titanic', 1997, 'Cameron'),
   ...     Movie('The Birds', 1963, 'Hitchcock'),
   ...     Movie('Aliens', 1986, 'Cameron')
   ... ]

   >>> # Encontra o primeiro filme lançado após 1960
   >>> by_year = attrgetter('released')
   >>> movies.sort(key=by_year)
   >>> movies[bisect(movies, 1960, key=by_year)]
   Movie(name='The Birds', released=1963, director='Hitchcock')

   >>> # Insere um filme enquanto mantém a ordem de classificação
   >>> romance = Movie('Love Story', 1970, 'Hiller')
   >>> insort(movies, romance, key=by_year)
   >>> pprint(movies)
   [Movie(name='The Birds', released=1963, director='Hitchcock'),
    Movie(name='Love Story', released=1970, director='Hiller'),
    Movie(name='Jaws', released=1975, director='Spielberg'),
    Movie(name='Aliens', released=1986, director='Cameron'),
    Movie(name='Titanic', released=1997, director='Cameron')]

Se a função chave for custosa, é possível evitar chamadas de função
repetidas buscando uma lista de chaves pré-calculadas para encontrar o
índice de um registro:

   >>> data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
   >>> data.sort(key=lambda r: r[1])       # Ou use operator.itemgetter(1).
   >>> keys = [r[1] for r in data]         # Pré-calcula uma lista de chaves.
   >>> data[bisect_left(keys, 0)]
   ('black', 0)
   >>> data[bisect_left(keys, 1)]
   ('blue', 1)
   >>> data[bisect_left(keys, 5)]
   ('red', 5)
   >>> data[bisect_left(keys, 8)]
   ('yellow', 8)
