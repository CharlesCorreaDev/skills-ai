"collections" --- Tipos de dados de contêineres
***********************************************

**Código-fonte:** Lib/collections/__init__.py

======================================================================

Este módulo implementa tipos de dados de contêineres especializados
que fornecem alternativas aos contêineres embutidos do Python, "dict",
"list", "set" e "tuple".

+-----------------------+----------------------------------------------------------------------+
| "namedtuple()"        | função fábrica (*factory function*) para criar subclasses de tuplas  |
|                       | com campos nomeados                                                  |
+-----------------------+----------------------------------------------------------------------+
| "deque"               | contêiner lista ou similar com acréscimos e retiradas rápidas nas    |
|                       | duas extremidades                                                    |
+-----------------------+----------------------------------------------------------------------+
| "ChainMap"            | classe dict ou similar para criar uma visão única de vários          |
|                       | mapeamentos                                                          |
+-----------------------+----------------------------------------------------------------------+
| "Counter"             | subclasse de dict para contar objetos *hasheáveis*                   |
+-----------------------+----------------------------------------------------------------------+
| "OrderedDict"         | subclasse de dict que lembra a ordem que as entradas foram           |
|                       | adicionadas                                                          |
+-----------------------+----------------------------------------------------------------------+
| "defaultdict"         | subclasse de dict que chama uma função fábrica para fornecer valores |
|                       | não encontrados                                                      |
+-----------------------+----------------------------------------------------------------------+
| "UserDict"            | invólucro em torno de objetos dicionário para facilitar fazer        |
|                       | subclasse de dict                                                    |
+-----------------------+----------------------------------------------------------------------+
| "UserList"            | invólucro em torno de objetos lista para facilitar criação de        |
|                       | subclasse de lista                                                   |
+-----------------------+----------------------------------------------------------------------+
| "UserString"          | invólucro em torno de objetos string para uma facilitar criação de   |
|                       | subclasse de string                                                  |
+-----------------------+----------------------------------------------------------------------+


Objetos "ChainMap"
==================

Adicionado na versão 3.3.

Uma classe "ChainMap" é fornecida para ligar rapidamente uma série de
mapeamentos de forma que possam ser tratados como um só. O que é
frequentemente mais rápido do que criar um novo dicionário e executar
múltiplas chamadas de "update()".

A classe pode ser usada para simular escopos aninhados e é útil em
modelos.

class collections.ChainMap(*maps)

   "ChainMap" agrupa múltiplos dicts ou outros mapeamentos para criar
   uma única vista atualizável. Se nenhum *maps* for especificado, um
   dicionário vazio será fornecido para que uma nova cadeia tenha
   sempre pelo menos um mapeamento.

   Os mapeamentos subjacentes são armazenados em uma lista. Essa lista
   é pública e pode ser acessada ou atualizada usando o atributo
   *maps*. Não existe outro estado.

   Faz uma busca nos mapeamentos subjacentes sucessivamente até que
   uma chave seja encontrada. Em contraste, escrita, atualizações e
   remoções operam apenas no primeiro mapeamento.

   Uma "ChainMap" incorpora os mapeamentos subjacentes por referência.
   Então, se um dos mapeamentos subjacentes for atualizado, essas
   alterações serão refletidas na "ChainMap".

   Todos os métodos usuais do dicionário são suportados. Além disso,
   existe um atributo *maps*, um método para criar novos subcontextos
   e uma propriedade para acessar todos, exceto o primeiro mapeamento:

   maps

      Uma lista de mapeamentos atualizáveis pelo usuário. A lista é
      ordenada do primeiro ao último pesquisado. É o único estado
      armazenado e pode ser modificado para alterar quais mapeamentos
      são pesquisados. A lista deve sempre conter pelo menos um
      mapeamento.

   new_child(m=None, **kwargs)

      Retorna uma nova "ChainMap" contendo um novo mapa seguido de
      todos os mapas na instância atual. Se "m" for especificado,
      torna-se o novo mapa na frente da lista de mapeamentos; Se não
      especificado, é usado um dicionário vazio, de modo que chamar
      "d.new_child()" é equivalente a: "ChainMap({}, *d.maps)". Se
      algum argumento nomeado for especificado, ele atualizará o mapa
      passado ou o novo dicionário vazio. Esse método é usado para
      criar subcontextos que podem ser atualizados sem alterar valores
      em nenhum dos mapeamentos pai.

      Alterado na versão 3.4: O parâmetro opcional "m" foi adicionado.

      Alterado na versão 3.10: Suporte a argumentos nomeados foi
      adicionado.

   parents

      Propriedade que retorna um novo "ChainMap" contendo todos os
      mapas da instância atual, exceto o primeiro. Isso é útil para
      pular o primeiro mapa da pesquisa. Os casos de uso são
      semelhantes aos do argumento nomeado "nonlocal" usada em
      *escopos aninhados*. Os casos de uso também são paralelos aos da
      função embutida "super()". Uma referência a "d.parents" é
      equivalente a: "ChainMap(*d.maps[1:])".

   Observe, a ordem de iteração de um "ChainMap" é determinada pela
   varredura dos mapeamentos do último ao primeiro:

      >>> baseline = {'music': 'bach', 'art': 'rembrandt'}
      >>> adjustments = {'art': 'van gogh', 'opera': 'carmen'}
      >>> list(ChainMap(adjustments, baseline))
      ['music', 'art', 'opera']

   Isso dá a mesma ordem de uma série de chamadas de "dict.update()"
   começando com o último mapeamento:

      >>> combined = baseline.copy()
      >>> combined.update(adjustments)
      >>> list(combined)
      ['music', 'art', 'opera']

   Alterado na versão 3.9: Adicionado suporte para os operadores "|" e
   "|=", especificados na **PEP 584**.

Ver também:

  * A classe MultiContext no pacote CodeTools de Enthought tem opções
    para oferecer suporte à escrita em qualquer mapeamento na cadeia.

  * A classe Context do Django para modelos é uma cadeia de
    mapeamentos somente leitura. Ela também oferece o recurso de push
    e pop (inserir e retirar) contextos semelhantes ao método
    "new_child()" e a propriedade "parents".

  * A receita de Contextos Aninhados possui opções para controlar se
    escritas e outras mutações se aplicam a apenas o primeiro
    mapeamento ou para qualquer mapeamento na cadeia.

  * Uma versão muito simplificada somente leitura do Chainmap.


Exemplos e Receitas de "ChainMap"
---------------------------------

Esta seção mostra várias abordagens para trabalhar com mapas
encadeados.

Exemplo de simulação da cadeia de busca interna do Python:

   import builtins
   pylookup = ChainMap(locals(), globals(), vars(builtins))

Exemplo de como permitir que os argumentos de linha de comando
especificados pelo usuário tenham precedência sobre as variáveis de
ambiente que, por sua vez, têm precedência sobre os valores padrão:

   import os, argparse

   defaults = {'color': 'red', 'user': 'guest'}

   parser = argparse.ArgumentParser()
   parser.add_argument('-u', '--user')
   parser.add_argument('-c', '--color')
   namespace = parser.parse_args()
   command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

   combined = ChainMap(command_line_args, os.environ, defaults)
   print(combined['color'])
   print(combined['user'])

Padrões de exemplo para utilização da classe "ChainMap" para simular
contextos aninhados:

   c = ChainMap()        # Cria o contexto raiz
   d = c.new_child()     # Cria um contexto filho aninhado
   e = c.new_child()     # Filho de c, independente de d
   e.maps[0]             # Dicionário do contexto atual -- como locals() do Python
   e.maps[-1]            # Contexto raiz -- como globals() do Python
   e.parents             # Envolvendo cadeia de contexto -- como os nonlocals do Python

   d['x'] = 1            # Define valor no contexto atual
   d['x']                # Obtém a primeira chave na cadeia de contextos
   del d['x']            # Exclui do contexto atual
   list(d)               # Todos os valores aninhados
   k in d                # Verifica todos os valores aninhados
   len(d)                # Número de valores aninhados
   d.items()             # Todos os itens aninhados
   dict(d)               # Achata em um dicionário comum

A classe "ChainMap" só faz atualizações (escritas e remoções) no
primeiro mapeamento na cadeia, enquanto as pesquisas irão buscar em
toda a cadeia. Contudo, se há o desejo de escritas e remoções
profundas, é fácil fazer uma  subclasse que atualiza chaves
encontradas mais a fundo na cadeia:

   class DeepChainMap(ChainMap):
       'Variant of ChainMap that allows direct updates to inner scopes'

       def __setitem__(self, key, value):
           for mapping in self.maps:
               if key in mapping:
                   mapping[key] = value
                   return
           self.maps[0][key] = value

       def __delitem__(self, key):
           for mapping in self.maps:
               if key in mapping:
                   del mapping[key]
                   return
           raise KeyError(key)

   >>> d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
   >>> d['lion'] = 'orange'         # atualiza uma chave existente dois níveis abaixo
   >>> d['snake'] = 'red'           # novas chaves são adicionadas ao dict mais acima
   >>> del d['elephant']            # remove uma chave existente um nível abaixo
   >>> d                            # exibe o resultado
   DeepChainMap({'zebra': 'black', 'snake': 'red'}, {}, {'lion': 'orange'})


Objetos "Counter"
=================

Uma ferramenta de contagem é fornecida para apoiar contas rápidas e
convenientes. Por exemplo:

   >>> # Conta ocorrências de palavras em uma lista
   >>> cnt = Counter()
   >>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
   ...     cnt[word] += 1
   ...
   >>> cnt
   Counter({'blue': 3, 'red': 2, 'green': 1})

   >>> # Encontra as dez palavras mais comuns em Hamlet
   >>> import re
   >>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
   >>> Counter(words).most_common(10)
   [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
    ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

class collections.Counter(**kwargs)
class collections.Counter(iterable, /, **kwargs)
class collections.Counter(mapping, /, **kwargs)

   Um "Counter" é uma subclasse de "dict" subclass para contagem de
   objetos *hasheáveis*. É uma coleção na qual elementos são
   armazenados como chaves de dicionário e suas contagens são
   armazenadas como valores de dicionário.  Contagens podem ser
   qualquer valor inteiro incluindo zero e contagens negativas.  A
   classe "Counter" é similar a sacos ou multiconjuntos em outras
   linguagens.

   Os elementos são contados a partir de um iterável *iterable* ou
   inicializado a partir de um outro mapeamento *mapping* (ou
   contador):

   >>> c = Counter()                           # a new, empty counter
   >>> c = Counter('gallahad')                 # a new counter from an iterable
   >>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
   >>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args

   Objetos Counter tem uma interface de dicionário, com a diferença
   que devolvem uma contagem zero para itens que não estão presentes
   em vez de levantar a exceção "KeyError":

   >>> c = Counter(['eggs', 'ham'])
   >>> c['bacon']                              # count of a missing element is zero
   0

   Definir uma contagem como zero não remove um elemento do contador.
   Use "del" para o remover completamente.

   >>> c['sausage'] = 0                        # counter entry with a zero count
   >>> del c['sausage']                        # del actually removes the entry

   Adicionado na versão 3.1.

   Alterado na versão 3.7: Como uma subclasse de "dict", "Counter"
   herda a capacidade de lembrar a ordem de inserção. Operações
   matemáticas em objetos *Counter* também preservam ordem. Os
   resultados são ordenados de acordo com o momento que um elemento é
   encontrado pela primeira vez no operando da esquerda e, em seguida,
   pela ordem encontrada no operando da direita.

   Objetos Counter têm suporte a métodos adicionais além daqueles que
   já estão disponíveis para todos os dicionários:

   elements()

      Retorna um iterador sobre os elementos, repetindo cada um tantas
      vezes quanto sua contagem. Os elementos são retornados na ordem
      em que foram encontrados pela primeira vez. Se a contagem de um
      elemento é menor que um, ele será ignorado por "elements()" .

      >>> c = Counter(a=4, b=2, c=0, d=-2)
      >>> sorted(c.elements())
      ['a', 'a', 'a', 'a', 'b', 'b']

   most_common(n=None)

      Retorna uma lista dos *n* elementos mais comuns e suas
      contagens, do mais comum para o menos comum.  Se *n* for omitido
      ou igual a "None", "most_common()" retorna *todos* os elementos
      no contador. Elementos com contagens iguais são ordenados na
      ordem em que foram encontrados pela primeira vez:

      >>> Counter('abracadabra').most_common(3)
      [('a', 5), ('b', 2), ('r', 2)]

   subtract(**kwargs)
   subtract(iterable, /, **kwargs)
   subtract(mapping, /, **kwargs)

      Os elementos são subtraídos de um iterável *iterable* ou de
      outro mapeamento *mapping* (ou contador).  Funciona como
      "dict.update()", mas subtraindo contagens ao invés de
      substituí-las.  Tanto as entradas quanto as saídas podem ser
      zero ou negativas.

      >>> c = Counter(a=4, b=2, c=0, d=-2)
      >>> d = Counter(a=1, b=2, c=3, d=4)
      >>> c.subtract(d)
      >>> c
      Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

      Adicionado na versão 3.2.

   total()

      Calcula a soma das contagens.

      >>> c = Counter(a=10, b=5, c=0)
      >>> c.total()
      15

      Adicionado na versão 3.10.

   The usual dictionary methods are available for "Counter" objects
   except for these two which work differently for counters:

   fromkeys(iterable)

      Este método de classe não está implementado para objetos
      "Counter".

   update(**kwargs)
   update(iterable, /, **kwargs)
   update(mapping, /, **kwargs)

      Elementos são contados a partir de um iterável *iterable* ou
      adicionados de outro mapeamento *mapping* (ou contador).
      Funciona como "dict.update()", mas adiciona contagens em vez de
      substituí-las. Além disso, é esperado que o *iterable* seja uma
      sequência de elementos, e não uma sequência de pares "(key,
      value)".

Os contadores oferecem suporte a operadores de comparação rica para
relacionamentos de igualdade, subconjunto e superconjunto: "==", "!=",
"<", "<=", ">", ">=". Todos esses testes tratam os elementos ausentes
como tendo contagens zero para que "Counter(a=1) == Counter(a=1, b=0)"
retorne verdadeiro.

Alterado na versão 3.10: Foram adicionadas operações de rica
comparação.

Alterado na versão 3.10: Em testes de igualdade, os elementos ausentes
são tratados como tendo contagens zero. Anteriormente, "Counter(a=3)"
e "Counter(a=3, b=0)" eram considerados distintos.

Padrões comuns para trabalhar com objetos "Counter":

   c.total()                       # total de todas as contagens
   c.clear()                       # redefine todas as contagens
   list(c)                         # lista elementos únicos
   set(c)                          # converte para um conjunto
   dict(c)                         # converte para um dicionário comum
   c.items()                       # acessa os pares (elem, cnt)
   Counter(dict(list_of_pairs))    # converte de uma lista de pares (elem, cnt)
   c.most_common()[:-n-1:-1]       # n últimos elementos comuns
   +c                              # remove zero e contagens negativas

Several mathematical operations are provided for combining "Counter"
objects to produce multisets (counters that have counts greater than
zero). Addition and subtraction combine counters by adding or
subtracting the counts of corresponding elements.  Intersection and
union return the minimum and maximum of corresponding counts.
Symmetric difference returns the difference between the maximum and
minimum of the corresponding counts. Equality and inclusion compare
corresponding counts.  Each operation can accept inputs with signed
counts, but the output will exclude results with counts of zero or
below.

   >>> c = Counter(a=3, b=1)
   >>> d = Counter(a=1, b=2)
   >>> c + d                       # add two counters together:  c[x] + d[x]
   Counter({'a': 4, 'b': 3})
   >>> c - d                       # subtract (keeping only positive counts)
   Counter({'a': 2})
   >>> c & d                       # intersection:  min(c[x], d[x])
   Counter({'a': 1, 'b': 1})
   >>> c | d                       # union:  max(c[x], d[x])
   Counter({'a': 3, 'b': 2})
   >>> c ^ d                       # max(c[x], d[x]) - min(c[x], d[x])
   Counter({'a': 2, 'b': 1})
   >>> c == d                      # equality:  c[x] == d[x]
   False
   >>> c <= d                      # inclusion:  c[x] <= d[x]
   False

A adição e subtração unárias são atalhos para adicionar um contador
vazio ou subtrair de um contador vazio.

>>> c = Counter(a=2, b=-4)
>>> +c
Counter({'a': 2})
>>> -c
Counter({'b': 4})

Adicionado na versão 3.3: Adicionado suporte para operador unário
mais, unário menos e operações *in-place* em multiconjuntos.

Adicionado na versão 3.15: Added support for the symmetric difference
multiset operation, "c ^ d".

Nota:

  Os contadores foram projetados principalmente para funcionar com
  números inteiros positivos para representar contagens contínuas; no
  entanto, foi tomado cuidado para não impedir desnecessariamente os
  casos de uso que precisassem de outros tipos ou valores negativos.
  Para ajudar nesses casos de uso, esta seção documenta o intervalo
  mínimo e as restrições de tipo.

  * A própria classe "Counter" é uma subclasse de dicionário sem
    restrições em suas chaves e valores. Os valores pretendem ser
    números que representam contagens, mas você *pode* armazenar
    qualquer coisa no campo de valor.

  * O método "most_common()" requer apenas que os valores sejam
    ordenáveis.

  * Para operações in-place, como "c[key] += 1", o tipo de valor
    precisa oferecer suporte a apenas adição e subtração. Portanto,
    frações, números de ponto flutuante e decimais funcionariam e os
    valores negativos são suportados. O mesmo também é verdadeiro para
    "update()" e "subtract()" que permitem valores negativos e zero
    para entradas e saídas.

  * Os métodos de multiconjuntos são projetados apenas para casos de
    uso com valores positivos. As entradas podem ser negativas ou
    zero, mas apenas saídas com valores positivos são criadas. Não há
    restrições de tipo, mas o tipo de valor precisa suportar adição,
    subtração e comparação.

  * O método "elements()" requer contagens de inteiros. Ele ignora
    contagens zero e negativas.

Ver também:

  * Classe Bag do Smalltalk.

  * Entrada da Wikipédia para Multiconjuntos.

  * Tutorial com exemplos de multiconjuntos no C++.

  * Para operações matemáticas em multiconjuntos e seus casos de uso,
    consulte *Knuth, Donald. The Art of Computer Programming Volume
    II, Seção 4.6.3, Exercício 19*.

  * Para enumerar todos os multiconjuntos distintos de um determinado
    tamanho em um determinado conjunto de elementos, consulte
    "itertools.combinations_with_replacement()":

       map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC


Objetos "deque"
===============

class collections.deque([iterable[, maxlen]])

   Retorna um novo objeto deque inicializado da esquerda para a
   direita (usando "append()") com dados do iterável *iterable*. Se
   *iterable* não for especificado, o novo deque estará vazio.

   Deques são uma generalização de pilhas e filas (o nome é
   pronunciado "deck" e é abreviação de "double-ended queue",
   conhecida em português como "fila duplamente terminada"). Deques
   oferecem suporte para inclusões e remoções seguras para thread e
   eficientes em uso de memória de ambos os lados do deque com
   aproximadamente o mesmo desempenho *O*(1) em qualquer direção.

   Embora os objetos "list" ofereçam suporte a operações semelhantes,
   eles são otimizados para operações rápidas de comprimento fixo e
   sujeitam a custos de movimentação de memória *O*(*n*) para as
   operações "pop(0)" e "insert(0, v)" que alteram o tamanho e a
   posição da representação de dados subjacente.

   Se *maxlen* não for especificado ou for "None", deques podem
   crescer para um comprimento arbitrário. Caso contrário, o deque é
   limitado ao comprimento máximo especificado. Quando um deque de
   comprimento limitado está cheio, quando novos itens são
   adicionados, um número correspondente de itens é descartado da
   extremidade oposta. Deques de comprimento limitado fornecem
   funcionalidade semelhante ao filtro "tail" no Unix. Eles também são
   úteis para rastrear transações e outras pools de dados onde apenas
   a atividade mais recente é de interesse.

   Deques are generic over the type of their contents.

   Os objetos deque oferecem suporte aos seguintes métodos:

   append(item, /)

      Adiciona *item* ao lado direito do deque.

   appendleft(item, /)

      Adiciona *item* ao lado esquerdo do deque

   clear()

      Remove todos os elementos do deque deixando-o com comprimento 0.

   copy()

      Cria uma cópia rasa do deque.

      Adicionado na versão 3.5.

   count(value, /)

      Conta o número de elementos em deque igual a *value*.

      Adicionado na versão 3.2.

   extend(iterable, /)

      Estende o lado direito do deque anexando elementos do argumento
      iterável.

   extendleft(iterable, /)

      Estende o lado esquerdo do deque anexando elementos de
      *iterable*. Observe que a série de acréscimos à esquerda resulta
      na reversão da ordem dos elementos no argumento iterável.

   index(value[, start[, stop]])

      Retorna a posição de *value* no deque (no ou após o índice
      *start* e antes do índice *stop*). Retorna a primeira
      correspondência ou levanta "ValueError" se não for encontrado.

      Adicionado na versão 3.5.

   insert(index, value, /)

      Insere *value* no deque na posição *index*.

      Se a inserção fizer com que um deque limitado cresça além de
      *maxlen*, uma "IndexError" é levantada.

      Adicionado na versão 3.5.

   pop()

      Remove e devolve um elemento do lado direito do deque. Se nenhum
      elemento estiver presente, levanta um "IndexError".

   popleft()

      Remove e devolve um elemento do lado esquerdo do deque. Se
      nenhum elemento estiver presente, levanta um "IndexError".

   remove(value, /)

      Remove a primeira ocorrência de *value*. Se não for encontrado,
      levanta um "ValueError".

   reverse()

      Inverte os elementos do deque no local e, em seguida, retorna
      "None".

      Adicionado na versão 3.2.

   rotate(n=1, /)

      Gira o deque *n* passos para a direita. Se *n* for negativo,
      gire para a esquerda.

      Quando o deque não está vazio, girar um passo para a direita é
      equivalente a "d.appendleft(d.pop())" e girar um passo para a
      esquerda é equivalente a "d.append(d.popleft())".

   Os objetos Deque também fornecem um atributo somente leitura:

   maxlen

      Tamanho máximo de um deque ou "None" se ilimitado.

      Adicionado na versão 3.1.

Além do acima, deques oferecem suporte à iteração, à serialização com
pickle, "len(d)", "reversed(d)", "copy.copy(d)", "copy.deepcopy(d)" e
ao teste de associação com o operador "in" e a referências subscritas,
como "d[0]" para acessar o primeiro elemento. O acesso indexado é
*O*(1) em ambas as extremidades, mas diminui para *O*(*n*) no meio.
Para acesso rápido e aleatório, use listas.

A partir da versão 3.5, deques oferecem suporte a
"__add__()",``__mul__()`` e "__imul__()".

Exemplo:

   >>> from collections import deque
   >>> d = deque('ghi')                 # torna um novo deque com três itens
   >>> for elem in d:                   # itera os elementos do deque
   ...     print(elem.upper())
   G
   H
   I

   >>> d.append('j')                    # adiciona uma nova entrada ao lado direito
   >>> d.appendleft('f')                # adiciona uma nova entrada ao lado esquerdo
   >>> d                                # mostra a representação do deque
   deque(['f', 'g', 'h', 'i', 'j'])

   >>> d.pop()                          # retorna e remove o item mais à direita
   'j'
   >>> d.popleft()                      # retorna e remove o item mais à esquerda
   'f'
   >>> list(d)                          # lista o conteúdo do deque
   ['g', 'h', 'i']
   >>> d[0]                             # exibe o item mais à esquerda
   'g'
   >>> d[-1]                            # exibe o item mais à direita
   'i'

   >>> list(reversed(d))                # lista o conteúdo de um deque ao inverso
   ['i', 'h', 'g']
   >>> 'h' in d                         # pesquisa no deque
   True
   >>> d.extend('jkl')                  # adiciona vários elementos de uma só vez
   >>> d
   deque(['g', 'h', 'i', 'j', 'k', 'l'])
   >>> d.rotate(1)                      # rotação para direita
   >>> d
   deque(['l', 'g', 'h', 'i', 'j', 'k'])
   >>> d.rotate(-1)                     # rotação para esquerda
   >>> d
   deque(['g', 'h', 'i', 'j', 'k', 'l'])

   >>> deque(reversed(d))               # cria um novo deque na ordem inversa
   deque(['l', 'k', 'j', 'i', 'h', 'g'])
   >>> d.clear()                        # esvazia o deque
   >>> d.pop()                          # não é possível retirar um item de um deque vazio
   Traceback (most recent call last):
       File "<pyshell#6>", line 1, in -toplevel-
           d.pop()
   IndexError: pop from an empty deque

   >>> d.extendleft('abc')              # extendleft() inverte a ordem da entrada
   >>> d
   deque(['c', 'b', 'a'])


Receitas de "deque"
-------------------

Esta seção mostra várias abordagens para trabalhar com deques.

Deques de comprimento limitado fornecem funcionalidade semelhante ao
filtro "tail" em Unix:

   def tail(filename, n=10):
       'Return the last n lines of a file'
       with open(filename) as f:
           return deque(f, n)

Outra abordagem para usar deques é manter uma sequência de elementos
adicionados recentemente, acrescentando à direita e clicando à
esquerda:

   def moving_average(iterable, n=3):
       # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
       # https://en.wikipedia.org/wiki/Moving_average
       it = iter(iterable)
       d = deque(itertools.islice(it, n-1))
       d.appendleft(0)
       s = sum(d)
       for elem in it:
           s += elem - d.popleft()
           d.append(elem)
           yield s / n

A round-robin scheduler can be implemented with input iterators stored
in a "deque".  Values are yielded from the active iterator in position
zero.  If that iterator is *exhausted*, it can be removed with
"popleft()"; otherwise, it can be cycled back to the end with the
"rotate()" method:

   def roundrobin(*iterables):
       "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
       iterators = deque(map(iter, iterables))
       while iterators:
           try:
               while True:
                   yield next(iterators[0])
                   iterators.rotate(-1)
           except StopIteration:
               # Remove um iterador esgotado.
               iterators.popleft()

O método "rotate()" fornece uma maneira de implementar o fatiamento e
exclusão "deque". Por exemplo, uma implementação Python pura de "del
d[n]" depende do método "rotate()" para posicionar os elementos a
serem retirados:

   def delete_nth(d, n):
       d.rotate(-n)
       d.popleft()
       d.rotate(n)

Para implementar o fatiamento de "deque", use uma abordagem semelhante
aplicando "rotate()" para trazer um elemento alvo para o lado esquerdo
do deque. Remova as entradas antigas com "popleft()", adicione novas
entradas com "extend()", e, então, inverta a rotação. Com pequenas
variações dessa abordagem, é fácil implementar manipulações de pilha
de estilo Forth, como "dup", "drop", "swap", "over", "pick", "rot" e
"roll".


Objetos "defaultdict"
=====================

class collections.defaultdict(default_factory=None, /, **kwargs)
class collections.defaultdict(default_factory, mapping, /, **kwargs)
class collections.defaultdict(default_factory, iterable, /, **kwargs)

   Retorna um novo objeto dicionário ou similar. "defaultdict" é uma
   subclasse da classe embutida "dict". Ele substitui um método e
   adiciona uma variável de instância gravável. A funcionalidade
   restante é a mesma da classe "dict" e não está documentada aqui.

   O primeiro argumento fornece o valor inicial para o atributo
   "default_factory"; o padrão é "None". Todos os argumentos restantes
   são tratados da mesma forma como se fossem passados para o
   construtor "dict", incluindo argumentos nomeados.

   "defaultdict"s are generic over two types, signifying
   (respectively) the types of the dictionary's keys and values.

   Os objetos "defaultdict" oferecem suporta ao seguinte método além
   das operações padrão "dict":

   __missing__(key, /)

      Se o atributo "default_factory" for "None", isso levanta uma
      exceção "KeyError" com *key* como argumento.

      Se "default_factory" não for "None", ele é chamado sem
      argumentos para fornecer um valor padrão para a chave *key*
      fornecida, este valor é inserido no dicionário para *key* e
      retornado.

      Se chamar "default_factory" levanta uma exceção, esta exceção é
      propagada inalterada.

      Este método é chamado pelo método "__getitem__()" da classe
      "dict" quando a chave solicitada não é encontrada; tudo o que
      ele retorna ou levanta é então retornado ou levantado por
      "__getitem__()".

      Observe que "__missing__()" *não* é chamado para nenhuma
      operação além de "__getitem__()". Isso significa que "get()"
      irá, como dicionários normais, retornar "None" como padrão ao
      invés de usar "default_factory".

   Objetos "defaultdict" permitem a seguinte variável de instância:

   default_factory

      Este atributo é usado pelo método "__missing__()"; ele é
      inicializado a partir do primeiro argumento para o construtor,
      se presente, ou para "None", se ausente.

   Alterado na versão 3.9: Adicionado operadores de mesclagem ("|") e
   de atualização ("|="), especificados na **PEP 584**.


Exemplos de "defaultdict"
-------------------------

Usando "list" como "default_factory", se for fácil agrupar a sequencia
dos pares chave-valores num dicionário de listas

>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

Quando cada chave é encontrada pela primeira vez, ela ainda não está
no mapeamento; então uma entrada é criada automaticamente usando a
função "default_factory" que retorna uma "list" vazia. A operação
"list.append()" então anexa o valor à nova lista. Quando as chaves são
encontradas novamente, a pesquisa prossegue normalmente (retornando a
lista daquela chave) e a operação "list.append()" adiciona outro valor
à lista. Esta técnica é mais simples e rápida que uma técnica
equivalente usando "dict.setdefault()":

>>> d = {}
>>> for k, v in s:
...     d.setdefault(k, []).append(v)
...
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

Definir "default_factory" como "int" torna "defaultdict" útil para
contagem (como um multiconjunto em outras linguagens):

>>> s = 'mississippi'
>>> d = defaultdict(int)
>>> for k in s:
...     d[k] += 1
...
>>> sorted(d.items())
[('i', 4), ('m', 1), ('p', 2), ('s', 4)]

Quando uma letra é encontrada pela primeira vez, ela está ausente no
mapeamento, então a função "default_factory" chama "int()" para
fornecer uma contagem padrão de zero. A operação de incremento então
cria a contagem para cada letra.

A função "int()" que sempre retorna zero é apenas um caso especial de
funções constantes. Uma maneira mais rápida e flexível de criar
funções constantes é usar uma função lambda que pode fornecer qualquer
valor constante (não apenas zero):

>>> def constant_factory(value):
...     return lambda: value
...
>>> d = defaultdict(constant_factory('<missing>'))
>>> d.update(name='John', action='ran')
>>> '%(name)s %(action)s to %(object)s' % d
'John ran to <missing>'

Definir "default_factory" como "set" torna "defaultdict" útil para
construir um dicionário de conjuntos:

>>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
>>> d = defaultdict(set)
>>> for k, v in s:
...     d[k].add(v)
...
>>> sorted(d.items())
[('blue', {2, 4}), ('red', {1, 3})]


Função de fábrica para tuplas com campos nomeados "namedtuple()"
================================================================

Tuplas nomeadas determinam o significado de cada posição numa tupla e
permitem um código mais legível e autodocumentado. Podem ser usadas
sempre que tuplas regulares forem utilizadas, e adicionam a
possibilidade de acessar campos pelo nome ao invés da posição do
índice.

collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

   Retorna uma nova subclasse de tupla chamada *typename*. A nova
   subclasse é usada para criar objetos tupla ou similares que possuem
   campos acessíveis por pesquisa de atributos, além de serem
   indexáveis e iteráveis. As instâncias da subclasse também possuem
   uma docstring útil (com *typename* e *field_names*) e um método
   útil "__repr__()" que lista o conteúdo da tupla em um formato
   "nome=valor".

   *field_names* são uma sequência de strings como "['x', 'y']".
   Alternativamente, *field_names* pode ser uma única string com cada
   nome de campo separado por espaços em branco e/ou vírgulas como,
   por exemplo, "'x y'" ou "'x, y'".

   Qualquer identificador Python válido pode ser usado para um nome de
   campo, exceto para nomes que começam com um sublinhado.
   Identificadores válidos consistem em letras, dígitos e sublinhados,
   mas não começam com um dígito ou sublinhado e não podem ser uma
   "keyword" como *class*, *for*, *return*, *global*, *pass* ou
   *raise*.

   Se *rename* for verdadeiro, nomes de campos inválidos serão
   automaticamente substituídos por nomes posicionais. Por exemplo,
   "['abc', 'def', 'ghi', 'abc']" é convertido para "['abc', '_1',
   'ghi', '_3']", eliminando a palavra reservada "def" e o nome de
   campo duplicado "abc".

   *defaults* pode ser "None" ou um *iterável* de valores padrão. Como
   os campos com valor padrão devem vir depois de qualquer campo sem
   padrão, os *padrões* são aplicados aos parâmetros mais à direita.
   Por exemplo, se os nomes dos campos forem "['x', 'y', 'z']" e os
   padrões forem "(1, 2)", então "x" será um argumento obrigatório,
   "y" será o padrão "1", e "z" será o padrão "2".

   Se *module* for definido, o atributo "__module__" da tupla nomeada
   será definido com esse valor.

   As instâncias de tuplas nomeadas não possuem dicionários por
   instância, portanto são leves e não requerem mais memória do que as
   tuplas normais.

   Para prover suporte para a serialização com pickle, a classe de
   tupla nomeada deve ser atribuída a uma variável que corresponda a
   *typename*.

   Alterado na versão 3.1: Adicionado suporte a *rename*.

   Alterado na versão 3.6: Os parâmetros *verbose* e *rename*
   tornaram-se argumentos somente-nomeados.

   Alterado na versão 3.6: Adicionado o parâmetro *module*.

   Alterado na versão 3.7: Removido o parâmetro *verbose* e o atributo
   "_source".

   Alterado na versão 3.7: Adicionado o parâmetro *defaults* e o
   atributo "_field_defaults".

   >>> # Exemplo básico
   >>> Point = namedtuple('Point', ['x', 'y'])
   >>> p = Point(11, y=22)     # instancia com argumentos nomeados ou posicionais
   >>> p[0] + p[1]             # indexável como a tupla plana (11, 22)
   33
   >>> x, y = p                # desempacota como uma tupla normal
   >>> x, y
   (11, 22)
   >>> p.x + p.y               # campos também acessíveis pelo nome
   33
   >>> p                       # __repr__ legível com o estilo nome=valor
   Point(x=11, y=22)

Tuplas nomeadas são especialmente úteis para atribuir nomes de campos
a tuplas de resultados retornadas pelos módulos "csv" ou "sqlite3":

   EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

   import csv
   for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
       print(emp.name, emp.title)

   import sqlite3
   conn = sqlite3.connect('/companydata')
   cursor = conn.cursor()
   cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
   for emp in map(EmployeeRecord._make, cursor.fetchall()):
       print(emp.name, emp.title)

Além dos métodos herdados das tuplas, as tuplas nomeadas oferecem
suporte a três métodos adicionais e dois atributos. Para evitar
conflitos com nomes de campos, os nomes de métodos e atributos começam
com um sublinhado.

classmethod somenamedtuple._make(iterable, /)

   Método de classe que cria uma nova instância a partir de uma
   sequência existente ou iterável.

      >>> t = [11, 22]
      >>> Point._make(t)
      Point(x=11, y=22)

somenamedtuple._asdict()

   Retorna um novo "dict" que mapeia nomes de campo para seus
   respectivos valores:

      >>> p = Point(x=11, y=22)
      >>> p._asdict()
      {'x': 11, 'y': 22}

   Alterado na versão 3.1: Retorna um "OrderedDict" em vez de um
   "dict" normal.

   Alterado na versão 3.8: Retorna um "dict" regular em vez de um
   "OrderedDict". A partir do Python 3.7, é garantido que os
   dicionários regulares sejam ordenados. Se os recursos extras de
   "OrderedDict" forem necessários, a correção sugerida é converter o
   resultado para o tipo desejado: "OrderedDict(nt._asdict())".

somenamedtuple._replace(**kwargs)

   Retorna uma nova instância da tupla nomeada substituindo os campos
   especificados por novos valores:

      >>> p = Point(x=11, y=22)
      >>> p._replace(x=33)
      Point(x=33, y=22)

      >>> for partnum, record in inventory.items():
      ...     inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())

   Tuplas nomeadas também são suportados pela função genérica
   "copy.replace()".

   Alterado na versão 3.13: Levanta "TypeError" em vez de "ValueError"
   para argumentos nomeados inválidos.

somenamedtuple._fields

   Tupla de strings listando os nomes dos campos. Útil para
   introspecção e para criar novos tipos de tuplas nomeadas a partir
   de tuplas nomeadas existentes.

      >>> p._fields            # exibe os nomes de campos
      ('x', 'y')

      >>> Color = namedtuple('Color', 'red green blue')
      >>> Pixel = namedtuple('Pixel', Point._fields + Color._fields)
      >>> Pixel(11, 22, 128, 255, 0)
      Pixel(x=11, y=22, red=128, green=255, blue=0)

somenamedtuple._field_defaults

   Dicionário mapeando nomes de campos para valores padrão.

      >>> Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
      >>> Account._field_defaults
      {'balance': 0}
      >>> Account('premium')
      Account(type='premium', balance=0)

Para recuperar um campo cujo nome está armazenado em uma string, use a
função "getattr()":

>>> getattr(p, 'x')
11

Para converter um dicionário em uma tupla nomeada, use o operador
estrela dupla (conforme descrito em Desempacotando listas de
argumentos):

>>> d = {'x': 11, 'y': 22}
>>> Point(**d)
Point(x=11, y=22)

Como uma tupla nomeada é uma classe regular do Python, é fácil
adicionar ou alterar funcionalidades com uma subclasse. Veja como
adicionar um campo calculado e um formato de impressão de largura
fixa:

   >>> class Point(namedtuple('Point', ['x', 'y'])):
   ...     __slots__ = ()
   ...     @property
   ...     def hypot(self):
   ...         return (self.x ** 2 + self.y ** 2) ** 0.5
   ...     def __str__(self):
   ...         return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

   >>> for p in Point(3, 4), Point(14, 5/7):
   ...     print(p)
   Point: x= 3.000  y= 4.000  hypot= 5.000
   Point: x=14.000  y= 0.714  hypot=14.018

A subclasse mostrada acima define "__slots__" como uma tupla vazia.
Isso ajuda a manter baixos os requisitos de memória, evitando a
criação de dicionários de instância.

A criação de subclasse não é útil para adicionar novos campos
armazenados. Em vez disso, simplesmente crie um novo tipo de tupla
nomeado a partir do atributo "_fields":

>>> Point3D = namedtuple('Point3D', Point._fields + ('z',))

Docstrings podem ser personalizados fazendo atribuições diretas aos
campos "__doc__":

>>> Book = namedtuple('Book', ['id', 'title', 'authors'])
>>> Book.__doc__ += ': Hardcover book in active collection'
>>> Book.id.__doc__ = '13-digit ISBN'
>>> Book.title.__doc__ = 'Title of first printing'
>>> Book.authors.__doc__ = 'List of authors sorted by last name'

Alterado na versão 3.5: Os docstrings de propriedade tornaram-se
graváveis.

Ver também:

  * Veja "typing.NamedTuple" para uma maneira de adicionar dicas de
    tipo para tuplas nomeadas. Ele também fornece uma notação elegante
    usando a palavra reservada "class":

       class Component(NamedTuple):
           part_number: int
           weight: float
           description: Optional[str] = None

  * Veja "types.SimpleNamespace()" para um espaço de nomes mutável
    baseado em um dicionário subjacente em vez de uma tupla.

  * O módulo "dataclasses" fornece um decorador e funções para
    adicionar automaticamente métodos especiais gerados a classes
    definidas pelo usuário.


Objetos "OrderedDict"
=====================

Os dicionários ordenados são como os dicionários normais, mas possuem
alguns recursos extras relacionados às operações de pedido. Eles se
tornaram menos importantes agora que a classe embutida "dict" ganhou a
capacidade de lembrar a ordem de inserção (esse novo comportamento foi
garantido no Python 3.7).

Algumas diferenças de "dict" ainda permanecem:

* O "dict" regular foi projetado para ser muito bom em operações de
  mapeamento. O rastreamento do pedido de inserção era secundário.

* O "OrderedDict" foi projetado para ser bom em operações de
  reordenação. A eficiência de espaço, a velocidade de iteração e o
  desempenho das operações de atualização eram secundários.

* O algoritmo "OrderedDict" pode lidar com operações de reordenação
  frequentes melhor do que "dict". Conforme mostrado nas receitas
  abaixo, isso o torna adequado para implementar vários tipos de
  caches LRU.

* A operação de igualdade para "OrderedDict" verifica a ordem
  correspondente.

  Um "dict" regular pode emular o teste de igualdade sensível à ordem
  com "p == q and all(k1 == k2 for k1, k2 in zip(p, q))".

* O método "popitem()" de "OrderedDict" tem uma assinatura diferente.
  Ele aceita um argumento opcional para especificar qual item será
  exibido.

  Um "dict" normal pode emular o "od.popitem(last=True)" do
  OrderedDict com "d.popitem()" que é garantido para exibir o (último)
  item mais à direita.

  Um "dict" normal pode emular o "od.popitem(last=False)" do
  OrderedDict com "(k := next(iter(d)), d.pop(k))" que retornará e
  remova o item mais à esquerda (primeiro), se existir.

* "OrderedDict" possui um método "move_to_end()" para reposicionar
  eficientemente um elemento em um endpoint.

  Um "dict" normal pode emular o "od.move_to_end(k, last=True)" do
  OrderedDict com "d[k] = d.pop(k)" que moverá a chave e seu valor
  associado para a posição mais à direita (última).

  Um "dict" regular não tem um equivalente eficiente para o
  "od.move_to_end(k, last=False)" do OrderedDict, que move a chave e
  seu valor associado para a posição mais à esquerda (primeira).

* Até o Python 3.8, "dict" não tinha um método "__reversed__()".

class collections.OrderedDict(**kwargs)
class collections.OrderedDict(mapping, /, **kwargs)
class collections.OrderedDict(iterable, /, **kwargs)

   Retorna uma instância de uma subclasse "dict" que possui métodos
   especializados para reorganizar a ordem do dicionário.

   Adicionado na versão 3.1.

   popitem(last=True)

      O método "popitem()" para dicionários ordenados retorna e remove
      um par (chave, valor). Os pares são retornados na ordem LIFO
      (último a entrar, primeiro a sair) se *last* for verdadeiro ou
      na ordem FIFO (primeiro a entrar, primeiro a sair) se for falso.

   move_to_end(key, last=True)

      Move uma chave *key* existente para qualquer extremidade de um
      dicionário ordenado. O item é movido para a extremidade direita
      se *last* for verdadeiro (o padrão) ou para o início se *último*
      for falso. Levanta "KeyError" se a *key* não existir:

         >>> d = OrderedDict.fromkeys('abcde')
         >>> d.move_to_end('b')
         >>> ''.join(d)
         'acdeb'
         >>> d.move_to_end('b', last=False)
         >>> ''.join(d)
         'bacde'

      Adicionado na versão 3.2.

Além dos métodos usuais de mapeamento, dicionários ordenados também
oferecem suporte a iteração reversa usando a função "reversed()".

Testes de igualdade entre objetos "OrderedDict" são sensíveis à ordem
e são aproximadamente equivalentes a
"list(od1.items())==list(od2.items())".

Testes de igualdade entre objetos "OrderedDict" e outros objetos
"Mapping" não diferenciam a ordem como dicionários regulares. Isso
permite que objetos "OrderedDict" sejam substituídos em qualquer lugar
que um dicionário regular seja usado.

Alterado na versão 3.5: Os itens, chaves e valores de *visões* de
"OrderedDict" agora oferecem suporte a iteração reversa usando
"reversed()".

Alterado na versão 3.6: Com a aceitação da **PEP 468**, a ordem é
mantida para argumentos nomeados passados para o construtor
"OrderedDict" e seu método "update()".

Alterado na versão 3.9: Adicionado operadores de mesclagem ("|") e de
atualização ("|="), especificados na **PEP 584**.


Exemplos e receitas de "OrderedDict"
------------------------------------

É simples criar uma variante de dicionário ordenado que lembre a ordem
em que as chaves foram inseridas pela *última* vez. Se uma nova
entrada substituir uma entrada existente, a posição de inserção
original será alterada e movida para o final:

   class LastUpdatedOrderedDict(OrderedDict):
       'Store items in the order that the keys were last updated.'

       def __setitem__(self, key, value):
           super().__setitem__(key, value)
           self.move_to_end(key)

An "OrderedDict" would also be useful for implementing variants of
"@functools.lru_cache":

   from collections import OrderedDict
   from time import monotonic

   class TimeBoundedLRU:
       "LRU Cache that invalidates and refreshes old entries."

       def __init__(self, func, maxsize=128, maxage=30):
           self.cache = OrderedDict()      # { args : (timestamp, result)}
           self.func = func
           self.maxsize = maxsize
           self.maxage = maxage

       def __call__(self, *args):
           if args in self.cache:
               self.cache.move_to_end(args)
               timestamp, result = self.cache[args]
               if monotonic() - timestamp <= self.maxage:
                   return result
           result = self.func(*args)
           self.cache[args] = monotonic(), result
           if len(self.cache) > self.maxsize:
               self.cache.popitem(last=False)
           return result

   class MultiHitLRUCache:
       """ LRU cache that defers caching a result until
           it has been requested multiple times.

           To avoid flushing the LRU cache with one-time requests,
           we don't cache until a request has been made more than once.

       """

       def __init__(self, func, maxsize=128, maxrequests=4096, cache_after=1):
           self.requests = OrderedDict()   # { uncached_key : request_count }
           self.cache = OrderedDict()      # { cached_key : function_result }
           self.func = func
           self.maxrequests = maxrequests  # max number of uncached requests
           self.maxsize = maxsize          # max number of stored return values
           self.cache_after = cache_after

       def __call__(self, *args):
           if args in self.cache:
               self.cache.move_to_end(args)
               return self.cache[args]
           result = self.func(*args)
           self.requests[args] = self.requests.get(args, 0) + 1
           if self.requests[args] <= self.cache_after:
               self.requests.move_to_end(args)
               if len(self.requests) > self.maxrequests:
                   self.requests.popitem(last=False)
           else:
               self.requests.pop(args, None)
               self.cache[args] = result
               if len(self.cache) > self.maxsize:
                   self.cache.popitem(last=False)
           return result


Objetos "UserDict"
==================

A classe "UserDict" atua como um invólucro em torno de objetos do tipo
dicionário. A necessidade desta classe foi parcialmente suplantada
pela capacidade de criar subclasses diretamente de "dict"; entretanto,
essa classe pode ser mais fácil de trabalhar, pois o dicionário
subjacente é acessível como atributo.

class collections.UserDict(**kwargs)
class collections.UserDict(mapping, /, **kwargs)
class collections.UserDict(iterable, /, **kwargs)

   Classe que simula um dicionário. O conteúdo da instância é mantido
   em um dicionário regular, acessível pelo atributo "data" das
   instâncias "UserDict". Se forem fornecidos argumentos, serão usados
   para inicializar "data" como um dicionário regular.

   Além de prover suporte aos métodos e operações de mapeamentos, as
   instâncias de "UserDict" fornecem o seguinte atributo:

   data

      Um dicionário real usado para armazenar o conteúdo da classe
      "UserDict".

   "UserDict" instances also override the following method:

   popitem()

      Remove and return a "(key, value)" pair from the wrapped
      dictionary. Pairs are returned in the same order as
      "data.popitem()". (For the default "dict.popitem()", this order
      is LIFO (last-in, first-out).) If the dictionary is empty,
      raises a "KeyError".


Objetos "UserList"
==================

Esta classe atua como um invólucro em torno de objetos de lista. É uma
classe base útil para suas próprias classes semelhantes a listas, que
podem herdar delas e substituir métodos existentes ou adicionar novos.
Desta forma, é possível adicionar novos comportamentos às listas.

A necessidade desta classe foi parcialmente suplantada pela capacidade
de criar subclasses diretamente de "list"; no entanto, pode ser mais
fácil trabalhar com essa classe porque a lista subjacente pode ser
acessada como um atributo.

class collections.UserList([list])

   Classe que simula uma lista. O conteúdo da instância é mantido em
   uma lista regular, que é acessível através do atributo "data" das
   instâncias "UserList". O conteúdo da instância é inicialmente
   definido como uma cópia de *list*, padronizando a lista vazia "[]".
   *list* pode ser qualquer iterável, por exemplo, uma lista Python
   real ou um objeto "UserList".

   Além de prover suporte aos métodos e operações de sequências
   mutáveis, as instâncias "UserList" fornecem o seguinte atributo:

   data

      Um objeto "list" real usado para armazenar o conteúdo da classe
      "UserList".

**Requisitos para criar subclasse:** Espera-se que as subclasses de
"UserList" ofereçam um construtor que pode ser chamado sem argumentos
ou com um argumento. Listar operações que retornam uma nova sequência
tenta criar uma instância da classe de implementação real. Para isso,
presume que o construtor pode ser chamado com um único parâmetro, que
é um objeto de sequência usado como fonte de dados.

Se uma classe derivada não desejar atender a este requisito, todos os
métodos especiais suportados por esta classe precisarão ser
substituídos; consulte as fontes para obter informações sobre os
métodos que precisam ser fornecidos nesse caso.


Objetos "UserString"
====================

A classe "UserString" atua como um invólucro em torno de objetos
string. A necessidade desta classe foi parcialmente suplantada pela
capacidade de criar subclasses diretamente de "str"; entretanto, essa
classe pode ser mais fácil de trabalhar porque a string subjacente é
acessível como um atributo.

class collections.UserString(seq)

   Classe que simula um objeto string. O conteúdo da instância é
   mantido em um objeto string regular, que é acessível através do
   atributo "data" das instâncias "UserString". O conteúdo da
   instância é inicialmente definido como uma cópia de *seq*. O
   argumento *seq* pode ser qualquer objeto que possa ser convertido
   em uma string usando a função embutida "str()".

   Além de prover suporte aos métodos e operações de strings, as
   instâncias "UserString" fornecem o seguinte atributo:

   data

      Um objeto "str" real usado para armazenar o conteúdo da classe
      "UserString".

   Alterado na versão 3.5: Novos métodos "__getnewargs__", "__rmod__",
   "casefold", "format_map", "isprintable" e "maketrans".
