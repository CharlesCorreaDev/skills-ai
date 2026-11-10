"itertools" --- Funções que criam iteradores para laços eficientes
******************************************************************

======================================================================

Esse módulo implementa diversos blocos de instruções com *iteradores*,
inspirados por construções de APL, Haskell, e SML. Cada uma foi
adequadamente reformulada para Python.

Esse módulo padroniza um conjunto central de ferramentas rápidas e de
uso eficiente da memória, que podem ser utilizadas sozinhas ou
combinadas. Juntas, eles formam uma "álgebra de iteradores" tornando
possível construir ferramentas sucintas e eficientes em Python puro.

Por exemplo, SML fornece uma ferramenta para tabulação: "tabulate(f)"
que produz uma sequência "f(0), f(1), ...".  O mesmo efeito pode ser
obtido em Python combinando "map()" e "count()" para formar "map(f,
count())".

**General iterators:**

+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| Iterador                     | Argumentos                   | Resultado                                         | Exemplo                                                       |
|==============================|==============================|===================================================|===============================================================|
| "accumulate()"               | p [,func]                    | p0, p0+p1, p0+p1+p2, ...                          | "accumulate([1,2,3,4,5]) → 1 3 6 10 15"                       |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "batched()"                  | p, n                         | (p0, p1, ..., p_n-1), ...                         | "batched('ABCDEFG', n=3) → ABC DEF G"                         |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "chain()"                    | p, q, ...                    | p0, p1, ... último elemento de p, q0, q1, ...     | "chain('ABC', 'DEF') → A B C D E F"                           |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "chain.from_iterable()"      | iterável                     | p0, p1, ... último elemento de p, q0, q1, ...     | "chain.from_iterable(['ABC', 'DEF']) → A B C D E F"           |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "compress()"                 | data, selectors              | (d[0] if s[0]), (d[1] if s[1]), ...               | "compress('ABCDEF', [1,0,1,0,1,1]) → A C E F"                 |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "count()"                    | [start[, step]]              | start, start+step, start+2*step, ...              | "count(10) → 10 11 12 13 14 ..."                              |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "cycle()"                    | p                            | p0, p1, ... ultimo elemento de p, p0, p1, ...     | "cycle('ABCD') → A B C D A B C D ..."                         |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "dropwhile()"                | predicate, seq               | seq[n], seq[n+1], começando quando o predicate    | "dropwhile(lambda x: x<5, [1,4,6,3,8]) → 6 3 8"               |
|                              |                              | falha                                             |                                                               |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "filterfalse()"              | predicate, seq               | elementos de seq onde predicate(elem) falha       | "filterfalse(lambda x: x<5, [1,4,6,3,8]) → 6 8"               |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "groupby()"                  | iterable[, key]              | sub-iteradores agrupados pelo valor de key(v)     | "groupby(['A','B','DEF'], len) → (1, A B) (3, DEF)"           |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "islice()"                   | seq, [start,] stop [, step]  | elementos de seq[start:stop:step]                 | "islice('ABCDEFG', 2, None) → C D E F G"                      |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "pairwise()"                 | iterável                     | (p[0], p[1]), (p[1], p[2])                        | "pairwise('ABCDEFG') → AB BC CD DE EF FG"                     |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "repeat()"                   | elem [,n]                    | elem, elem, elem, ... repete infinitamente ou até | "repeat(10, 3) → 10 10 10"                                    |
|                              |                              | n vezes                                           |                                                               |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "starmap()"                  | func, seq                    | func(*seq[0]), func(*seq[1]), ...                 | "starmap(pow, [(2,5), (3,2), (10,3)]) → 32 9 1000"            |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "takewhile()"                | predicate, seq               | seq[0], seq[1], até predicate falhar              | "takewhile(lambda x: x<5, [1,4,6,3,8]) → 1 4"                 |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "tee()"                      | it, n                        | n iteradores it independentes                     | "tee('ABC', 2) → A B C, A B C"                                |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+
| "zip_longest()"              | p, q, ...                    | (p[0], q[0]), (p[1], q[1]), ...                   | "zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D-"      |
+------------------------------+------------------------------+---------------------------------------------------+---------------------------------------------------------------+

**Iteradores combinatórios:**

+------------------------------------------------+----------------------+---------------------------------------------------------------+
| Iterador                                       | Argumentos           | Resultado                                                     |
|================================================|======================|===============================================================|
| "product()"                                    | p, q, ... [repeat=1] | produto cartesiano, equivalente a laços "for" aninhados       |
+------------------------------------------------+----------------------+---------------------------------------------------------------+
| "permutations()"                               | p[, r]               | tuplas de tamanho r, com todas ordenações possíveis, sem      |
|                                                |                      | elementos repetidos                                           |
+------------------------------------------------+----------------------+---------------------------------------------------------------+
| "combinations()"                               | p, r                 | tuplas de tamanho r, ordenadas, sem elementos repetidos       |
+------------------------------------------------+----------------------+---------------------------------------------------------------+
| "combinations_with_replacement()"              | p, r                 | tuplas de tamanho r, ordenadas, com elementos repetidos       |
+------------------------------------------------+----------------------+---------------------------------------------------------------+

+------------------------------------------------+---------------------------------------------------------------+
| Exemplos                                       | Resultado                                                     |
|================================================|===============================================================|
| "product('ABCD', repeat=2)"                    | "AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD"             |
+------------------------------------------------+---------------------------------------------------------------+
| "permutations('ABCD', 2)"                      | "AB AC AD BA BC BD CA CB CD DA DB DC"                         |
+------------------------------------------------+---------------------------------------------------------------+
| "combinations('ABCD', 2)"                      | "AB AC AD BC BD CD"                                           |
+------------------------------------------------+---------------------------------------------------------------+
| "combinations_with_replacement('ABCD', 2)"     | "AA AB AC AD BB BC BD CC CD DD"                               |
+------------------------------------------------+---------------------------------------------------------------+


Funções do intertools
=====================

Todas as funções a seguir constroem e retornam iteradores. Algumas
fornecem fluxos de comprimento infinito, então elas devem ser
acessadas somente por funções ou laços que truncam o fluxo.

itertools.accumulate(iterable[, function, *, initial=None])

   Constrói um iterador que retorna somas acumuladas, ou resultados
   acumulados de outras funções binárias.

   A função *function* assume como padrão a adição. *function* deve
   aceitar dois argumentos, um total acumulado e um valor de
   *iterable*.

   Se um valor inicial *initial* for fornecido, o acúmulo começará com
   esse valor e a saída terá um elemento a mais que o iterável de
   entrada.

   Aproximadamente equivalente a:

      def accumulate(iterable, function=operator.add, *, initial=None):
          'Retorna totais atuais'
          # accumulate([1,2,3,4,5]) → 1 3 6 10 15
          # accumulate([1,2,3,4,5], initial=100) → 100 101 103 106 110 115
          # accumulate([1,2,3,4,5], operator.mul) → 1 2 6 24 120

          iterator = iter(iterable)
          total = initial
          if initial is None:
              try:
                  total = next(iterator)
              except StopIteration:
                  return

          yield total
          for element in iterator:
              total = function(total, element)
              yield total

   Para calcular um mínimo atual, defina *function* como "min()". Para
   um máximo atual, defina *function* como "max()". Ou para um produto
   atual, defina *function* como "operator.mul()". Para construir uma
   tabela de amortização, acumular os juros e aplicar os pagamentos:

      >>> data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
      >>> list(accumulate(data, max))              # máximo atual
      [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
      >>> list(accumulate(data, operator.mul))     # produto atual
      [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]

      # Amortiza um empréstimo de 5% de 1000 com 10 pagamentos anuais de 90
      >>> update = lambda balance, payment: round(balance * 1.05) - payment
      >>> list(accumulate(repeat(90, 10), update, initial=1_000))
      [1000, 960, 918, 874, 828, 779, 728, 674, 618, 559, 497]

   Veja "functools.reduce()" para uma função similar que devolve
   apenas o valor acumulado final.

   Adicionado na versão 3.2.

   Alterado na versão 3.3: Adicionado o parâmetro opcional *function*.

   Alterado na versão 3.8: Adicionado o parâmetro opcional *initial*.

itertools.batched(iterable, n, *, strict=False)

   Dados de lote do *iterable* em tuplas de comprimento *n*. O último
   lote pode ser menor que *n*.

   Se *strict* for verdadeiro, será levantada uma "ValueError" se o
   lote final for menor que *n*.

   Loops over the input iterable and accumulates data into tuples up
   to size *n*.  The input is consumed lazily, just enough to fill a
   batch. The result is yielded as soon as the batch is full or when
   the input iterable is *exhausted*:

      >>> flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
      >>> unflattened = list(batched(flattened_data, 2))
      >>> unflattened
      [('roses', 'red'), ('violets', 'blue'), ('sugar', 'sweet')]

   Aproximadamente equivalente a:

      def batched(iterable, n, *, strict=False):
          # batched('ABCDEFG', 3) → ABC DEF G
          if n < 1:
              raise ValueError('n must be at least one')
          iterator = iter(iterable)
          while batch := tuple(islice(iterator, n)):
              if strict and len(batch) != n:
                  raise ValueError('batched(): incomplete batch')
              yield batch

   Adicionado na versão 3.12.

   Alterado na versão 3.13: Adicionada a opção *strict*.

itertools.chain(*iterables)

   Make an iterator that returns elements from the first iterable
   until it is *exhausted*, then proceeds to the next iterable, until
   all of the iterables are exhausted.  This combines multiple data
   sources into a single iterator.  Roughly equivalent to:

      def chain(*iterables):
          # chain('ABC', 'DEF') → A B C D E F
          for iterable in iterables:
              yield from iterable

   Note that unpacking in comprehensions provides similar
   functionality so that "list(chain(p, q))" could be written as "[*s
   for s in (p, q)]".

classmethod chain.from_iterable(iterable)

   Construtor alternativo para "chain()". Obtém entradas encadeadas a
   partir de um único argumento iterável que avaliado preguiçosamente.
   Aproximadamente equivalente a:

      def from_iterable(iterables):
          # chain.from_iterable(['ABC', 'DEF']) → A B C D E F
          for iterable in iterables:
              yield from iterable

   Note that unpacking in comprehensions provides similar
   functionality so that "list(chain.from_iterable(iterables))" could
   be written as "[*s for s in iterables]".

itertools.combinations(iterable, r)

   Devolve subsequências de elementos com comprimento *r* a partir da
   entrada *iterável*

   A saída é uma subsequência de "product()" mantendo apenas entradas
   que são subsequências do *iterable*. O comprimento da saída é dado
   por "math.comb()" que calcula "n! / r! / (n - r)!" quando "0 ≤ r ≤
   n" ou zero quando "r > n".

   As tuplas das combinações são emitidas em ordem lexicográfica de
   acordo com a ordem do iterável de entrada. Se o iterável estiver
   ordenado, as tuplas de combinação serão produzidas em sequência
   ordenada.

   Os elementos são tratados como únicos baseado em suas posições, não
   em seus valores. Se os elementos de entrada são únicos, não haverá
   repetição de valores nas sucessivas combinações.

   Aproximadamente equivalente a:

      def combinations(iterable, r):
          # combinations('ABCD', 2) → AB AC AD BC BD CD
          # combinations(range(4), 3) → 012 013 023 123

          pool = tuple(iterable)
          n = len(pool)
          if r > n:
              return
          indices = list(range(r))

          yield tuple(pool[i] for i in indices)
          while True:
              for i in reversed(range(r)):
                  if indices[i] != i + n - r:
                      break
              else:
                  return
              indices[i] += 1
              for j in range(i+1, r):
                  indices[j] = indices[j-1] + 1
              yield tuple(pool[i] for i in indices)

itertools.combinations_with_replacement(iterable, r)

   Devolve subsequências de comprimento *r* de elementos do *iterável*
   de entrada permitindo que elementos individuais sejam repetidos
   mais de uma vez.

   A saída é uma subsequência de "product()" que mantém apenas
   entradas que são subsequências (com possíveis elementos repetidos)
   do *iterable*. O número de subsequências retornadas é "(n + r - 1)!
   / r! / (n - 1)!" quando "n > 0".

   As tuplas das combinações são emitidas em ordem lexicográfica de
   acordo com a ordem do iterável de entrada. Se o iterável estiver
   ordenado, as tuplas de combinação serão produzidas em sequência
   ordenada.

   Os elementos são tratados como únicos baseado em suas posições, não
   em seus valores. Se os elementos de entrada forem únicos, não
   haverá repetição de valores nas combinações geradas.

   Aproximadamente equivalente a:

      def combinations_with_replacement(iterable, r):
          # combinations_with_replacement('ABC', 2) → AA AB AC BB BC CC

          pool = tuple(iterable)
          n = len(pool)
          if not n and r:
              return
          indices = [0] * r

          yield tuple(pool[i] for i in indices)
          while True:
              for i in reversed(range(r)):
                  if indices[i] != n - 1:
                      break
              else:
                  return
              indices[i:] = [indices[i] + 1] * (r - i)
              yield tuple(pool[i] for i in indices)

   Adicionado na versão 3.1.

itertools.compress(data, selectors)

   Make an iterator that returns elements from *data* where the
   corresponding element in *selectors* is true.  Stops when either
   the *data* or *selectors* iterables have been *exhausted*.  Roughly
   equivalent to:

      def compress(data, selectors):
          # compress('ABCDEF', [1,0,1,0,1,1]) → A C E F
          return (datum for datum, selector in zip(data, selectors) if selector)

   Adicionado na versão 3.1.

itertools.count(start=0, step=1)

   Cria um iterador que retorne valores uniformemente espaçados
   começando com *start*. Pode ser usado com "map()" para gerar pontos
   de dados consecutivos ou com "zip()" para adicionar números de
   sequência. Aproximadamente equivalente a:

      def count(start=0, step=1):
          # count(10) → 10 11 12 13 14 ...
          # count(2.5, 0.5) → 2.5 3.0 3.5 ...
          n = start
          while True:
              yield n
              n += step

   Quando é feita uma contagem usando números de ponto flutuante, é
   possível ter melhor precisão substituindo código multiplicativo
   como  "(start + step * i for i in count())".

   Alterado na versão 3.1: Adicionou argumento *step* e permitiu
   argumentos não-inteiros.

itertools.cycle(iterable)

   Make an iterator returning elements from the *iterable* and saving
   a copy of each.  When the iterable is *exhausted*, return elements
   from the saved copy.  Repeats indefinitely.  Roughly equivalent to:

      def cycle(iterable):
          # cycle('ABCD') → A B C D A B C D A B C D ...

          saved = []
          for element in iterable:
              yield element
              saved.append(element)

          while saved:
              for element in saved:
                  yield element

   Esta itertool pode exigir armazenamento auxiliar significativo
   (dependendo do comprimento do iterável).

itertools.dropwhile(predicate, iterable)

   Cria um iterador que remove elementos do *iterable* enquanto o
   *predicate* for verdadeiro e, em seguida, retorna todos os
   elementos. Equivalente a:

      def dropwhile(predicate, iterable):
          # dropwhile(lambda x: x<5, [1,4,6,3,8]) → 6 3 8

          iterator = iter(iterable)
          for x in iterator:
              if not predicate(x):
                  yield x
                  break

          for x in iterator:
              yield x

   Observe que isso não produz *nenhuma* saída até que o predicado se
   torne falso, portanto, esta itertool pode ter um longo tempo de
   inicialização.

itertools.filterfalse(predicate, iterable)

   Cria um iterador que filtre elementos do *iterable*, retornando
   apenas aqueles para os quais o *predicate* retorna um valor falso.
   Se o *predicate* for "None", retorna os itens que são falsos.
   Equivalente aproximadamente a:

      def filterfalse(predicate, iterable):
          # filterfalse(lambda x: x<5, [1,4,6,3,8]) → 6 8

          if predicate is None:
              predicate = bool

          for x in iterable:
              if not predicate(x):
                  yield x

itertools.groupby(iterable, key=None)

   Cria um iterador que retorna chaves e grupos consecutivos do
   *iterable*. A *key* é uma função que calcula um valor-chave para
   cada elemento. Se não for especificado ou for "None", *key* assume
   como padrão uma função de identidade e retorna o elemento
   inalterado. Geralmente, o iterável precisa já estar ordenado na
   mesma função chave.

   O funcionamento de "groupby()" é semelhante ao filtro "uniq" no
   Unix. Ele gera uma quebra ou um novo grupo sempre que o valor da
   função da tecla muda (razão pela qual geralmente é necessário
   ordenar os dados usando a mesma função da tecla). Esse
   comportamento difere do GROUP BY do SQL, que agrega elementos
   comuns independentemente da ordem de entrada.

   O grupo retornado é, ele próprio, um iterador que compartilha o
   iterável subjacente com "groupby()". Como a origem é compartilhada,
   quando o objeto "groupby()" avança, o grupo anterior não fica mais
   visível. Portanto, se esses dados forem necessários posteriormente,
   eles devem ser armazenados como uma lista:

      groups = []
      uniquekeys = []
      data = sorted(data, key=keyfunc)
      for k, g in groupby(data, keyfunc):
          groups.append(list(g))      # armazena um iterador de grupo como uma lista
          uniquekeys.append(k)

   "groupby()" é aproximadamente equivalente a:

      def groupby(iterable, key=None):
          # [k for k, g in groupby('AAAABBBCCDAABBB')] → A B C D A B
          # [list(g) for k, g in groupby('AAAABBBCCD')] → AAAA BBB CC D

          keyfunc = (lambda x: x) if key is None else key
          iterator = iter(iterable)
          exhausted = False

          def _grouper(target_key):
              nonlocal curr_value, curr_key, exhausted
              yield curr_value
              for curr_value in iterator:
                  curr_key = keyfunc(curr_value)
                  if curr_key != target_key:
                      return
                  yield curr_value
              exhausted = True

          try:
              curr_value = next(iterator)
          except StopIteration:
              return
          curr_key = keyfunc(curr_value)

          while not exhausted:
              target_key = curr_key
              curr_group = _grouper(target_key)
              yield curr_key, curr_group
              if curr_key == target_key:
                  for _ in curr_group:
                      pass

itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step])

   Cria um iterador que retorna os elementos selecionados do iterável.
   Funciona como o fatiamento de sequência, mas não oferece suporte a
   valores negativos para *start*, *stop* ou *step*.

   Se *start* for zero ou "None", a iteração começa em zero. Caso
   contrário, os elementos do iterável são pulados até que *start*
   seja alcançado.

   If *stop* is "None", iteration continues until the input is
   *exhausted*, if at all.  Otherwise, it stops at the specified
   position.

   Se *step* for "None", o padrão do passo é 1. Os elementos são
   retornados consecutivamente, a menos que *step* seja definido como
   maior que um, o que resulta na omissão de itens.

   Aproximadamente equivalente a:

      def islice(iterable, *args):
          # islice('ABCDEFG', 2) → A B
          # islice('ABCDEFG', 2, 4) → C D
          # islice('ABCDEFG', 2, None) → C D E F G
          # islice('ABCDEFG', 0, None, 2) → A C E G

          s = slice(*args)
          start = 0 if s.start is None else s.start
          stop = s.stop
          step = 1 if s.step is None else s.step
          if start < 0 or (stop is not None and stop < 0) or step <= 0:
              raise ValueError

          indices = count() if stop is None else range(max(start, stop))
          next_i = start
          for i, element in zip(indices, iterable):
              if i == next_i:
                  yield element
                  next_i += step

   Se a entrada for um iterador, o consumo total do *islice* avança o
   iterador de entrada em "max(start, stop)" passos, independentemente
   do valor do *step*.

itertools.pairwise(iterable)

   Return successive overlapping pairs taken from the input
   *iterable*.

   The number of 2-tuples in the output iterator will be one fewer
   than the number of inputs.  It will be empty if the input iterable
   has fewer than two values.

   Aproximadamente equivalente a:

      def pairwise(iterable):
          # pairwise('ABCDEFG') → AB BC CD DE EF FG

          iterator = iter(iterable)
          a = next(iterator, None)

          for b in iterator:
              yield a, b
              a = b

   Adicionado na versão 3.10.

itertools.permutations(iterable, r=None)

   Return successive *r* length permutations of elements from the
   *iterable*.

   If *r* is not specified or is "None", then *r* defaults to the
   length of the *iterable* and all possible full-length permutations
   are generated.

   The output is a subsequence of "product()" where entries with
   repeated elements have been filtered out.  The length of the output
   is given by "math.perm()" which computes "n! / (n - r)!" when "0 ≤
   r ≤ n" or zero when "r > n".

   The permutation tuples are emitted in lexicographic order according
   to the order of the input *iterable*.  If the input *iterable* is
   sorted, the output tuples will be produced in sorted order.

   Elements are treated as unique based on their position, not on
   their value.  If the input elements are unique, there will be no
   repeated values within a permutation.

   Aproximadamente equivalente a:

      def permutations(iterable, r=None):
          # permutations('ABCD', 2) → AB AC AD BA BC BD CA CB CD DA DB DC
          # permutations(range(3)) → 012 021 102 120 201 210

          pool = tuple(iterable)
          n = len(pool)
          r = n if r is None else r
          if r > n:
              return

          indices = list(range(n))
          cycles = list(range(n, n-r, -1))
          yield tuple(pool[i] for i in indices[:r])

          while n:
              for i in reversed(range(r)):
                  cycles[i] -= 1
                  if cycles[i] == 0:
                      indices[i:] = indices[i+1:] + indices[i:i+1]
                      cycles[i] = n - i
                  else:
                      j = cycles[i]
                      indices[i], indices[-j] = indices[-j], indices[i]
                      yield tuple(pool[i] for i in indices[:r])
                      break
              else:
                  return

itertools.product(*iterables, repeat=1)

   Cartesian product of the input iterables.

   Aproximadamente equivalente a laços for aninhados em uma expressão
   geradora. Por exemplo, "product(A, B)" devolve o mesmo que "((x,y)
   for x in A for y in B)".

   Os laços aninhados circulam como um hodômetro com o elemento mais à
   direita avançando a cada iteração. Este padrão cria uma ordenação
   lexicográfica de maneira que se os iteráveis de entrada estiverem
   ordenados, as tuplas produzidas são emitidas de maneira ordenada.

   To compute the product of an iterable with itself, specify the
   number of repetitions with the optional *repeat* keyword argument.
   For example, "product(A, repeat=4)" means the same as "product(A,
   A, A, A)".

   This function is roughly equivalent to the following code, except
   that the actual implementation does not build up intermediate
   results in memory:

      def product(*iterables, repeat=1):
          # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
          # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111

          if repeat < 0:
              raise ValueError('repeat argument cannot be negative')
          pools = [tuple(pool) for pool in iterables] * repeat

          result = [[]]
          for pool in pools:
              result = [x+[y] for x in result for y in pool]

          for prod in result:
              yield tuple(prod)

   Before "product()" runs, it completely consumes the input
   iterables, keeping pools of values in memory to generate the
   products.  Accordingly, it is only useful with finite inputs.

itertools.repeat(object[, times])

   Make an iterator that returns *object* over and over again. Runs
   indefinitely unless the *times* argument is specified.

   Aproximadamente equivalente a:

      def repeat(object, times=None):
          # repeat(10, 3) → 10 10 10
          if times is None:
              while True:
                  yield object
          else:
              for i in range(times):
                  yield object

   Um uso comum de *repeat* é para fornecer um fluxo de valores
   constantes para *map* ou *zip*.

      >>> list(map(pow, range(10), repeat(2)))
      [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

itertools.starmap(function, iterable)

   Make an iterator that computes the *function* using arguments
   obtained from the *iterable*.  Used instead of "map()" when
   argument parameters have already been "pre-zipped" into tuples.

   The difference between "map()" and "starmap()" parallels the
   distinction between "function(a,b)" and "function(*c)". Roughly
   equivalent to:

      def starmap(function, iterable):
          # starmap(pow, [(2,5), (3,2), (10,3)]) → 32 9 1000
          for args in iterable:
              yield function(*args)

itertools.takewhile(predicate, iterable)

   Make an iterator that returns elements from the *iterable* as long
   as the *predicate* is true.  Roughly equivalent to:

      def takewhile(predicate, iterable):
          # takewhile(lambda x: x<5, [1,4,6,3,8]) → 1 4
          for x in iterable:
              if not predicate(x):
                  break
              yield x

   Note, the element that first fails the predicate condition is
   consumed from the input iterator and there is no way to access it.
   This could be an issue if an application wants to further consume
   the input iterator after *takewhile* has been run to *exhaustion*.
   To work around this problem, consider using more-itertools
   before_and_after() instead.

itertools.tee(iterable, n=2)

   Return *n* independent iterators from a single iterable.

   Aproximadamente equivalente a:

      def tee(iterable, n=2):
          if n < 0:
              raise ValueError
          if n == 0:
              return ()
          iterator = _tee(iterable)
          result = [iterator]
          for _ in range(n - 1):
              result.append(_tee(iterator))
          return tuple(result)

      class _tee:

          def __init__(self, iterable):
              it = iter(iterable)
              if isinstance(it, _tee):
                  self.iterator = it.iterator
                  self.link = it.link
              else:
                  self.iterator = it
                  self.link = [None, None]

          def __iter__(self):
              return self

          def __next__(self):
              link = self.link
              if link[1] is None:
                  link[0] = next(self.iterator)
                  link[1] = [None, None]
              value, self.link = link
              return value

   When the input *iterable* is already a tee iterator object, all
   members of the return tuple are constructed as if they had been
   produced by the upstream "tee()" call.  This "flattening step"
   allows nested "tee()" calls to share the same underlying data chain
   and to have a single update step rather than a chain of calls.

   The flattening property makes tee iterators efficiently peekable:

      def lookahead(tee_iterator):
           "Return the next value without moving the input forward"
           [forked_iterator] = tee(tee_iterator, 1)
           return next(forked_iterator)

      >>> iterator = iter('abcdef')
      >>> [iterator] = tee(iterator, 1)   # Make the input peekable
      >>> next(iterator)                  # Move the iterator forward
      'a'
      >>> lookahead(iterator)             # Check next value
      'b'
      >>> next(iterator)                  # Continue moving forward
      'b'

   "tee" iterators are not threadsafe. A "RuntimeError" may be raised
   when simultaneously using iterators returned by the same "tee()"
   call, even if the original *iterable* is threadsafe.

   This itertool may require significant auxiliary storage (depending
   on how much temporary data needs to be stored). In general, if one
   iterator uses most or all of the data before another iterator
   starts, it is faster to use "list()" instead of "tee()".

itertools.zip_longest(*iterables, fillvalue=None)

   Make an iterator that aggregates elements from each of the
   *iterables*.

   If the iterables are of uneven length, missing values are filled-in
   with *fillvalue*.  If not specified, *fillvalue* defaults to
   "None".

   Iteration continues until the longest iterable is *exhausted*.

   Aproximadamente equivalente a:

      def zip_longest(*iterables, fillvalue=None):
          # zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D-

          iterators = list(map(iter, iterables))
          num_active = len(iterators)
          if not num_active:
              return

          while True:
              values = []
              for i, iterator in enumerate(iterators):
                  try:
                      value = next(iterator)
                  except StopIteration:
                      num_active -= 1
                      if not num_active:
                          return
                      iterators[i] = repeat(fillvalue)
                      value = fillvalue
                  values.append(value)
              yield tuple(values)

   If one of the iterables is potentially infinite, then the
   "zip_longest()" function should be wrapped with something that
   limits the number of calls (for example "islice()" or
   "takewhile()").


Receitas com itertools
======================

Esta seção mostra receitas para criação de um ferramental ampliado
usando as ferramentas existentes de itertools como elementos
construtivos.

The primary purpose of the itertools recipes is educational.  The
recipes show various ways of thinking about individual tools — for
example, that "chain.from_iterable" is related to the concept of
flattening.  The recipes also give ideas about ways that the tools can
be combined — for example, how "starmap()" and "repeat()" can work
together.  The recipes also show patterns for using itertools with the
"operator" and "collections" modules as well as with the built-in
itertools such as "map()", "filter()", "reversed()", and
"enumerate()".

A secondary purpose of the recipes is to serve as an incubator.  The
"accumulate()", "compress()", and "pairwise()" itertools started out
as recipes.  Currently, the "sliding_window()", "derangements()", and
"sieve()" recipes are being tested to see whether they prove their
worth.

Substantially all of these recipes and many, many others can be
installed from the more-itertools project found on the Python Package
Index:

   python -m pip install more-itertools

Many of the recipes offer the same high performance as the underlying
toolset. Superior memory performance is kept by processing elements
one at a time rather than bringing the whole iterable into memory all
at once. Code volume is kept small by linking the tools together in a
functional style.  High speed is retained by preferring "vectorized"
building blocks over the use of for-loops and *generators* which incur
interpreter overhead.

   from itertools import (accumulate, batched, chain, combinations, compress,
        count, cycle, filterfalse, groupby, islice, permutations, product,
        repeat, starmap, tee, zip_longest)
   from collections import Counter, deque
   from contextlib import suppress
   from functools import reduce
   from heapq import heappush, heappushpop, heappush_max, heappushpop_max
   from math import comb, isqrt, prod, sumprod
   from operator import getitem, is_not, itemgetter, mul, neg, truediv


   # ==== Basic one liners ====

   def take(n, iterable):
       "Return first n items of the iterable as a list."
       return list(islice(iterable, n))

   def prepend(value, iterable):
       "Prepend a single value in front of an iterable."
       # prepend(1, [2, 3, 4]) → 1 2 3 4
       return chain([value], iterable)

   def repeatfunc(function, times=None, *args):
       "Repeat calls to a function with specified arguments."
       if times is None:
           return starmap(function, repeat(args))
       return starmap(function, repeat(args, times))

   def flatten(list_of_lists):
       "Flatten one level of nesting."
       return chain.from_iterable(list_of_lists)

   def ncycles(iterable, n):
       "Returns the sequence elements n times."
       return chain.from_iterable(repeat(tuple(iterable), n))

   def loops(n):
       "Loop n times. Like range(n) but without creating integers."
       # for _ in loops(100): ...
       return repeat(None, n)

   def tail(n, iterable):
       "Return an iterator over the last n items."
       # tail(3, 'ABCDEFG') → E F G
       return iter(deque(iterable, maxlen=n))

   def consume(iterator, n=None):
       "Advance the iterator n-steps ahead. If n is None, consume entirely."
       # Use functions that consume iterators at C speed.
       if n is None:
           deque(iterator, maxlen=0)
       else:
           next(islice(iterator, n, n), None)

   def nth(iterable, n, default=None):
       "Returns the nth item or a default value."
       return next(islice(iterable, n, None), default)

   def quantify(iterable, predicate=bool):
       "Given a predicate that returns True or False, count the True results."
       return sum(map(predicate, iterable))

   def first_true(iterable, default=False, predicate=None):
       "Returns the first true value or the *default* if there is no true value."
       # first_true([a, b, c], x) → a or b or c or x
       # first_true([a, b], x, f) → a if f(a) else b if f(b) else x
       return next(filter(predicate, iterable), default)

   def all_equal(iterable, key=None):
       "Returns True if all the elements are equal to each other."
       # all_equal('4٤௪౪໔', key=int) → True
       return len(take(2, groupby(iterable, key))) <= 1


   # ==== Data pipelines ====

   def unique_justseen(iterable, key=None):
       "Yield unique elements, preserving order. Remember only the element just seen."
       # unique_justseen('AAAABBBCCDAABBB') → A B C D A B
       # unique_justseen('ABBcCAD', str.casefold) → A B c A D
       if key is None:
           return map(itemgetter(0), groupby(iterable))
       return map(next, map(itemgetter(1), groupby(iterable, key)))

   def unique_everseen(iterable, key=None):
       "Yield unique elements, preserving order. Remember all elements ever seen."
       # unique_everseen('AAAABBBCCDAABBB') → A B C D
       # unique_everseen('ABBcCAD', str.casefold) → A B c D
       seen = set()
       if key is None:
           for element in filterfalse(seen.__contains__, iterable):
               seen.add(element)
               yield element
       else:
           for element in iterable:
               k = key(element)
               if k not in seen:
                   seen.add(k)
                   yield element

   def unique(iterable, key=None, reverse=False):
       "Yield unique elements in sorted order. Supports unhashable inputs."
       # unique([[1, 2], [3, 4], [1, 2]]) → [1, 2] [3, 4]
       sequenced = sorted(iterable, key=key, reverse=reverse)
       return unique_justseen(sequenced, key=key)

   def sliding_window(iterable, n):
       "Collect data into overlapping fixed-length chunks or blocks."
       # sliding_window('ABCDEFG', 3) → ABC BCD CDE DEF EFG
       iterator = iter(iterable)
       window = deque(islice(iterator, n - 1), maxlen=n)
       for x in iterator:
           window.append(x)
           yield tuple(window)

   def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
       "Collect data into non-overlapping fixed-length chunks or blocks."
       # grouper('ABCDEFG', 3, fillvalue='x')       → ABC DEF Gxx
       # grouper('ABCDEFG', 3, incomplete='strict') → ABC DEF ValueError
       # grouper('ABCDEFG', 3, incomplete='ignore') → ABC DEF
       iterators = [iter(iterable)] * n
       match incomplete:
           case 'fill':
               return zip_longest(*iterators, fillvalue=fillvalue)
           case 'strict':
               return zip(*iterators, strict=True)
           case 'ignore':
               return zip(*iterators)
           case _:
               raise ValueError('Expected fill, strict, or ignore')

   def roundrobin(*iterables):
       "Visit input iterables in a cycle until each is exhausted."
       # roundrobin('ABC', 'D', 'EF') → A D E B F C
       # Algorithm credited to George Sakkis
       iterators = map(iter, iterables)
       for num_active in range(len(iterables), 0, -1):
           iterators = cycle(islice(iterators, num_active))
           yield from map(next, iterators)

   def subslices(seq):
       "Return all contiguous non-empty subslices of a sequence."
       # subslices('ABCD') → A AB ABC ABCD B BC BCD C CD D
       slices = starmap(slice, combinations(range(len(seq) + 1), 2))
       return map(getitem, repeat(seq), slices)

   def derangements(iterable, r=None):
       "Produce r length permutations without fixed points."
       # derangements('ABCD') → BADC BCDA BDAC CADB CDAB CDBA DABC DCAB DCBA
       # Algorithm credited to Stefan Pochmann
       seq = tuple(iterable)
       pos = tuple(range(len(seq)))
       have_moved = map(map, repeat(is_not), repeat(pos), permutations(pos, r=r))
       valid_derangements = map(all, have_moved)
       return compress(permutations(seq, r=r), valid_derangements)

   def iter_index(iterable, value, start=0, stop=None):
       "Return indices where a value occurs in a sequence or iterable."
       # iter_index('AABCADEAF', 'A') → 0 1 4 7
       seq_index = getattr(iterable, 'index', None)
       if seq_index is None:
           iterator = islice(iterable, start, stop)
           for i, element in enumerate(iterator, start):
               if element is value or element == value:
                   yield i
       else:
           stop = len(iterable) if stop is None else stop
           i = start
           with suppress(ValueError):
               while True:
                   yield (i := seq_index(value, i, stop))
                   i += 1

   def iter_except(function, exception, first=None):
       "Convert a call-until-exception interface to an iterator interface."
       # iter_except(d.popitem, KeyError) → non-blocking dictionary iterator
       with suppress(exception):
           if first is not None:
               yield first()
           while True:
               yield function()


   # ==== Mathematical operations ====

   def multinomial(*counts):
       "Number of distinct arrangements of a multiset."
       # Counter('abracadabra').values() → 5 2 2 1 1
       # multinomial(5, 2, 2, 1, 1) → 83160
       return prod(map(comb, accumulate(counts), counts))

   def powerset(iterable):
       "Subsequences of the iterable from shortest to longest."
       # powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
       s = list(iterable)
       return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

   def sum_of_squares(iterable):
       "Add up the squares of the input values."
       # sum_of_squares([10, 20, 30]) → 1400
       return sumprod(*tee(iterable))


   # ==== Matrix operations ====

   def reshape(matrix, columns):
       "Reshape a 2-D matrix to have a given number of columns."
       # reshape([(0, 1), (2, 3), (4, 5)], 3) →  (0, 1, 2) (3, 4, 5)
       return batched(chain.from_iterable(matrix), columns, strict=True)

   def transpose(matrix):
       "Swap the rows and columns of a 2-D matrix."
       # transpose([(1, 2, 3), (11, 22, 33)]) → (1, 11) (2, 22) (3, 33)
       return zip(*matrix, strict=True)

   def matmul(m1, m2):
       "Multiply two matrices."
       # matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)]) → (49, 80) (41, 60)
       n = len(m2[0])
       return batched(starmap(sumprod, product(m1, transpose(m2))), n)


   # ==== Polynomial arithmetic ====

   def convolve(signal, kernel):
       """Discrete linear convolution of two iterables.
       Equivalent to polynomial multiplication.

       Convolutions are mathematically commutative; however, the inputs are
       evaluated differently.  The signal is consumed lazily and can be
       infinite. The kernel is fully consumed before the calculations begin.

       Article:  https://betterexplained.com/articles/intuitive-convolution/
       Video:    https://www.youtube.com/watch?v=KuXjwB4LzSA
       """
       # convolve([1, -1, -20], [1, -3]) → 1 -4 -17 60
       # convolve(data, [0.25, 0.25, 0.25, 0.25]) → Moving average (blur)
       # convolve(data, [1/2, 0, -1/2]) → 1st derivative estimate
       # convolve(data, [1, -2, 1]) → 2nd derivative estimate
       kernel = tuple(kernel)[::-1]
       n = len(kernel)
       padded_signal = chain(repeat(0, n-1), signal, repeat(0, n-1))
       windowed_signal = sliding_window(padded_signal, n)
       return map(sumprod, repeat(kernel), windowed_signal)

   def polynomial_from_roots(roots):
       """Compute a polynomial's coefficients from its roots.

          (x - 5) (x + 4) (x - 3)  expands to:   x³ -4x² -17x + 60
       """
       # polynomial_from_roots([5, -4, 3]) → [1, -4, -17, 60]
       factors = zip(repeat(1), map(neg, roots))
       return list(reduce(convolve, factors, [1]))

   def polynomial_eval(coefficients, x):
       """Evaluate a polynomial at a specific value.

       Computes with better numeric stability than Horner's method.
       """
       # Evaluate x³ -4x² -17x + 60 at x = 5
       # polynomial_eval([1, -4, -17, 60], x=5) → 0
       n = len(coefficients)
       if not n:
           return type(x)(0)
       powers = map(pow, repeat(x), reversed(range(n)))
       return sumprod(coefficients, powers)

   def polynomial_derivative(coefficients):
       """Compute the first derivative of a polynomial.

          f(x)  =  x³ -4x² -17x + 60
          f'(x) = 3x² -8x  -17
       """
       # polynomial_derivative([1, -4, -17, 60]) → [3, -8, -17]
       n = len(coefficients)
       powers = reversed(range(1, n))
       return list(map(mul, coefficients, powers))


   # ==== Number theory ====

   def sieve(n):
       "Primes less than n."
       # sieve(30) → 2 3 5 7 11 13 17 19 23 29
       if n > 2:
           yield 2
       data = bytearray((0, 1)) * (n // 2)
       for p in iter_index(data, 1, start=3, stop=isqrt(n) + 1):
           data[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
       yield from iter_index(data, 1, start=3)

   def factor(n):
       "Prime factors of n."
       # factor(99) → 3 3 11
       # factor(1_000_000_000_000_007) → 47 59 360620266859
       # factor(1_000_000_000_000_403) → 1000000000000403
       for prime in sieve(isqrt(n) + 1):
           while not n % prime:
               yield prime
               n //= prime
               if n == 1:
                   return
       if n > 1:
           yield n

   def is_prime(n):
       "Return True if n is prime."
       # is_prime(1_000_000_000_000_403) → True
       return n > 1 and next(factor(n)) == n

   def totient(n):
       "Count of natural numbers up to n that are coprime to n."
       # https://mathworld.wolfram.com/TotientFunction.html
       # totient(12) → 4 because len([1, 5, 7, 11]) == 4
       for prime in set(factor(n)):
           n -= n // prime
       return n


   # ==== Running statistics ====

   def running_mean(iterable):
       "Average of values seen so far."
       # running_mean([37, 33, 38, 28]) → 37 35 36 34
       return map(truediv, accumulate(iterable), count(1))

   def running_min(iterable):
       "Smallest of values seen so far."
       # running_min([37, 33, 38, 28]) → 37 33 33 28
       return accumulate(iterable, func=min)

   def running_max(iterable):
       "Largest of values seen so far."
       # running_max([37, 33, 38, 28]) → 37 37 38 38
       return accumulate(iterable, func=max)

   def running_median(iterable):
       "Median of values seen so far."
       # running_median([37, 33, 38, 28]) → 37 35 37 35
       read = iter(iterable).__next__
       lo = []  # max-heap
       hi = []  # min-heap the same size as or one smaller than lo
       with suppress(StopIteration):
           while True:
               heappush_max(lo, heappushpop(hi, read()))
               yield lo[0]
               heappush(hi, heappushpop_max(lo, read()))
               yield (lo[0] + hi[0]) / 2

   def running_statistics(iterable):
       "Aggregate statistics for values seen so far."
       # Generate tuples:  (size, minimum, median, maximum, mean)
       t0, t1, t2, t3 = tee(iterable, 4)
       return zip(
           count(1),
           running_min(t0),
           running_median(t1),
           running_max(t2),
           running_mean(t3),
       )
