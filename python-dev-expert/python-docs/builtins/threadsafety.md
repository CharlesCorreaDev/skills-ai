Garantias de segurança de thread
********************************

Esta página documenta as garantias de segurança de thread para tipos
embutido na construção com threads livres do Python. As garantias aqui
descritas aplicam-se ao utilizar o Python com a *GIL* desativada (modo
threads livres). Quando a GIL está ativada, a maioria das operações é
serializada implicitamente.

Para orientações gerais sobre como escrever código seguro para thread
no Python com threads livres, consulte Suporte do Python para threads
livres.


Níveis de segurança de threads
==============================

A documentação da API C usa os seguintes níveis para descrever as
garantias de segurança de threads de cada função. Os níveis estão
listados do menos para o mais seguro.


Incompatível
------------

Uma função ou operação que não pode se tornar segura para uso
concorrente mesmo com sincronização externa. Código incompatível
normalmente acessa o estado global de maneira não sincronizada e deve
ser chamado apenas a partir de uma única thread durante todo o tempo
de vida do programa.

Exemplo: uma função que modifica o estado em todo o processo, como
manipuladores de sinais ou variáveis de ambiente, onde chamadas
concorrentes de quaisquer threads, mesmo com trava externo, podem
conflitar com o ambiente de execução (*runtime*) ou com outras
bibliotecas.


Compatível
----------

Uma função ou operação que é segura para ser chamada a partir de
múltiplas threads *desde que* o chamador forneça a sincronização
externa apropriada, por exemplo mantendo uma *trava* durante a duração
de cada chamada. Sem tal sincronização, chamadas concorrentes podem
produzir *condições de corrida* ou *corridas de dados*.

Exemplo: uma função que lê ou escreve em um objeto cujo estado interno
não é protegido por uma trava. Os chamadores devem garantir que duas
threads não acessem o mesmo objeto ao mesmo tempo.


Seguro em objetos distintos
---------------------------

Uma função ou operação que é segura para ser chamada a partir de
múltiplas threads sem sincronização externa, desde que cada thread
opere em um objeto **diferente**. Duas threads podem chamar a função
ao mesmo tempo, mas não devem passar o mesmo objeto (ou objetos que
compartilham estado subjacente) como argumentos.

Exemplo: uma função que modifica campos de uma struct usando escritas
não atômicas. Duas threads podem chamar a função cada uma em sua
própria instância de struct com segurança, mas chamadas concorrentes
na *mesma* instância exigem sincronização externa.


Seguro em objetos compartilhados
--------------------------------

Uma função ou operação que é segura para uso concorrente no **mesmo**
objeto. A implementação usa sincronização interna (como *travas por
objeto* ou seções críticas) para proteger o estado mutável
compartilhado, de modo que os chamadores não precisam fornecer sua
própria trava.

Exemplo: "PyList_GetItemRef()" pode ser chamada a partir de múltiplas
threads no mesmo "PyListObject" - ela usa sincronização interna para
serializar o acesso.


Atômica
-------

Uma função ou operação que parece *atômica* em relação a outras
threads - ela executa instantaneamente da perspectiva de outras
threads. Esta é a forma mais forte de segurança de threads.

Exemplo: "PyMutex_IsLocked()" realiza uma leitura atômica do estado do
mutex e pode ser chamada a partir de qualquer thread a qualquer
momento.


Segurança de threads para objetos lista
=======================================

Ler um único elemento de uma "list" é *atômico*:

   lst[i]   # list.__getitem__

Os seguintes métodos percorrem a lista e usam leituras *atômicas* de
cada item para realizar sua função. Isso significa que eles podem
retornar resultados afetados por modificações concorrentes:

   item in lst
   lst.index(item)
   lst.count(item)

Todas as operações acima evitam adquirir *travas por objeto*. Elas não
travam modificações concorrentes. Outras operações que mantêm uma
trava não impedirão que estas observem estados intermediários.

Todas as outras operações a partir daqui bloqueiam usando o *trava por
objeto*.

Escrever um único item via "lst[i] = x" é seguro para chamar a partir
de múltiplas threads e não corromperá a lista.

As seguintes operações retornam novos objetos e parecem *atômicas*
para outras threads:

   lst1 + lst2    # concatena duas listas em uma nova lista
   x * lst        # repete lst x vezes em uma nova lista
   lst.copy()     # retorna uma cópia rasa da lista

Os seguintes métodos que operam apenas em um único elemento sem
necessidade de deslocamento são *atômicos*:

   lst.append(x)  # acrescenta ao final da lista; não é necessário deslocar elementos
   lst.pop()      # remove o elemento do final da lista; não é necessário deslocar os demais elementos

O método "clear()" também é *atômico*. Outras threads não podem
observar elementos sendo removidos.

O método "sort()" não é *atômico*. Outras threads não podem observar
estados intermediários durante a ordenação, mas a lista parece vazia
durante a execução da ordenação.

As seguintes operações podem permitir que operações *livres de travas*
observem estados intermediários, pois modificam múltiplos elementos no
local (in-place):

   lst.insert(idx, item)  # desloca elementos
   lst.pop(idx)           # idx não no fim da lista, desloca elementos
   lst *= x               # cópia elementos no local

O método "remove()" pode permitir modificações concorrentes, pois a
comparação de elementos pode executar código Python arbitrário (via
"__eq__()").

"extend()" é seguro para chamar a partir de múltiplas threads. No
entanto, suas garantias dependem do iterável passado para ele. Se for
uma "list", uma "tuple", um "set", um "frozenset", um "dict" ou um
objeto de visão de dicionário (mas não suas subclasses), a operação
"extend" estará segura de modificações concorrentes no iterável. Caso
contrário, um iterador é criado, o qual pode ser modificado
concorrentemente por outra thread. O mesmo se aplica à concatenação no
local de uma lista com outros iteráveis ao usar "lst += iterable".

De forma semelhante, a atribuição a uma fatia de lista com "lst[i:j] =
iterable" é segura para ser chamada a partir de múltiplas threads, mas
"iterable" só é travado quando também for uma "list" (mas não suas
subclasses).

Operações que envolvem múltiplos acessos, assim como iteração, nunca
são atômicas. Por exemplo:

   # NÃO é atômico: lê-modifica-escreve
   lst[i] = lst[i] + 1

   # NÃO é atômico: verifica-e-então-age
   if lst:
       item = lst.pop()

   # NÃO é seguro para thread: iteração enquanto modifica
   for item in lst:
       process(item)  # outra thread pode modificar lst

Considere a sincronização externa ao compartilhar instâncias de "list"
entre threads.


Segurança de threads para objetos dict
======================================

Criar um dicionário com o construtor "dict" é atômico quando o
argumento passado for um "dict" ou uma "tuple". Ao usar o método
"dict.fromkeys()", a criação do dicionário é atômica quando o
argumento for um "dict", "tuple", "set" ou "frozenset".

As seguintes operações e funções são *livres de travas* e *atômicas*.

   d[key]       # dict.__getitem__
   d.get(key)   # dict.get
   key in d     # dict.__contains__
   len(d)       # dict.__len__

Todas as outras operações a partir daqui mantêm a *trava por objeto*.

Escrever ou remover um único item é seguro para chamar a partir de
múltiplas threads e não corromperá o dicionário:

   d[key] = value        # escreve
   del d[key]            # exclui
   d.pop(key)            # remove e retorna
   d.popitem()           # remove e retorna último item
   d.setdefault(key, v)  # insere se não existir

Essas operações podem comparar chaves usando "__eq__()", o que pode
executar código Python arbitrário. Durante tais comparações, o
dicionário pode ser modificado por outra thread. Para tipos embutidos
como "str", "int" e "float", que implementam "__eq__()" em C, o trava
subjacente não é liberado durante as comparações e isso não é uma
preocupação.

As seguintes operações retornam novos objetos e mantêm a *trava por
objeto* durante a duração da operação:

   d.copy()      # retorna uma cópia rasa do dicionário
   d | other     # combina dois dicionários em um novo dicionário
   d.keys()      # retorna um novo objeto de visão dict_keys
   d.values()    # retorna um novo objeto de visão dict_values
   d.items()     # retorna um novo objeto de visão dict_items

O método "clear()" mantém a trava durante sua execução. Outras threads
não podem observar elementos sendo removidos.

As seguintes operações travariam ambos os dicionários. Para "update()"
e "|=", isso se aplica apenas quando o outro operando for um "dict"
que usa o iterador de dicionário padrão (mas não subclasses que
substituem a iteração). Para comparação de igualdade, isso se aplica a
"dict" e suas subclasses:

   d.update(outro_dict)  # ambos travados quando outro_dict é um dict
   d |= outro_dict       # ambos travados quando outro_dict é um dict
   d == outro_dict       # ambos travados para dict e subclasses

Todas as operações de comparação também comparam valores usando
"__eq__()", portanto, para tipos não embutidos, a trava pode ser
liberada durante a comparação.

"fromkeys()" trava tanto o novo dicionário quanto o iterável quando o
iterável for exatamente um "dict", "set" ou "frozenset" (não
subclasses):

   dict.fromkeys(a_dict)      # trava ambas
   dict.fromkeys(a_set)       # trava ambas
   dict.fromkeys(a_frozenset) # trava ambas

Ao atualizar a partir de um iterável que não é dicionário, apenas o
dicionário de destino é travada. O iterável pode ser modificado
concorrentemente por outra thread:

   d.update(iterável)        # iterável não é um dict: somente d travado
   d |= iterável             # iterável não é um dict: somente d travado
   dict.fromkeys(iterável)   # iterável não é um dict/conjunto/frozenset: somente o resultado travado

Operações que envolvem múltiplos acessos, assim como iteração, nunca
são atômicas:

   # NÃO é atômico: lê-modifica-escreve
   d[key] = d[key] + 1

   # NÃO é atômico: verifica-e-então-age (TOCTOU)
   if key in d:
       del d[key]

   # NÃO é seguro para thread: iteração enquanto modifica
   for key, value in d.items():
       process(key)  # outa thread pode modificar d

Para evitar problemas de tempo de verificação para tempo de uso
(TOCTOU, do inglês *time-of-check to time-of-us*), use operações
atômicas ou trata exceções:

   # Usa pop() com um valor padrão em vez de verificar-e-então-excluir
   d.pop(key, None)

   # ou trata a exceção
   try:
       del d[key]
   except KeyError:
       pass

Para iterar com segurança sobre um dicionário que pode ser modificado
por outra thread, itere sobre uma cópia:

   # Faz uma cópia para iterar com segurança
   for key, value in d.copy().items():
       process(key)

Considere a sincronização externa ao compartilhar instâncias de "dict"
entre threads.


Segurança de thread para objetos conjunto
=========================================

A função "len()" é livre de trava e *atômica*.

A seguinte operação de leitura é livre de trava. Ela não bloqueia
modificações concorrentes e pode observar estados intermediários de
operações que mantêm a trava por objeto:

   elem in s    # set.__contains__

Esta operação pode comparar elementos usando "__eq__()", o que pode
executar código Python arbitrário. Durante tais comparações, o
conjunto pode ser modificado por outra thread. Para tipos embutidos
como "str", "int" e "float", "__eq__()" não libera a trava subjacente
durante as comparações e isso não é uma preocupação.

Todas as outras operações a partir daqui mantêm a trava por objeto.

Adicionar ou remover um único elemento é seguro para chamar a partir
de múltiplas threads e não corromperá o conjunto:

   s.add(elem)      # adiciona elemento
   s.remove(elem)   # remove elemento, levanta se estiver faltando
   s.discard(elem)  # remove elemento se estiver presente
   s.pop()          # remove e retorna elemento arbitrário

Essas operações também comparam elementos; portanto, aplicam-se as
mesmas considerações sobre "__eq__()" mencionadas acima.

O método "copy()" retorna um novo objeto e mantém a trava por objeto
durante toda a execução para que seja sempre atômico.

O método "clear()" mantém a trava durante sua execução. Outras threads
não podem observar elementos sendo removidos.

As seguintes operações aceitam apenas "set" ou "frozenset" como
operandos e sempre travam ambos os objetos:

   s |= outro                   # outro deve ser conjunto/frozenset
   s &= outro                   # outro deve ser conjunto/frozenset
   s -= outro                   # outro deve ser conjunto/frozenset
   s ^= outro                   # outro deve ser conjunto/frozenset
   s & outro                    # outro deve ser conjunto/frozenset
   s | outro                    # outro deve ser conjunto/frozenset
   s - outro                    # outro deve ser conjunto/frozenset
   s ^ outro                    # outro deve ser conjunto/frozenset

"set.update()", "set.union()", "set.intersection()" e
"set.difference()" podem receber múltiplos iteráveis como argumentos.
Todos eles iteram sobre todos os iteráveis fornecidos e realizam o
seguinte:

   * "set.update()" e "set.union()" travam objetos apenas quando o
     outro operando é um "set", "frozenset", ou "dict".

   * "set.intersection()" e "set.difference()" sempre tentam travar
     todos os objetos.

"set.symmetric_difference()" tenta travar ambos objetos.

As variantes de atualização dos métodos acima também apresentam
algumas diferenças entre si:

   * "set.difference_update()" e "set.intersection_update()" tentam
     travar todos os objetos um por um.

   * "set.symmetric_difference_update()" só trava os argumentos se
     forem do tipo "set", "frozenset" ou "dict".

Os métodos a seguir sempre tentam travar ambos objetos:

   s.isdisjoint(outro)          # ambos travados
   s.issubset(outro)            # ambos travados
   s.issuperset(outro)          # ambos travados

Operações que envolvem múltiplos acessos, assim como iteração, nunca
são atômicas:

   # NÃO é atômico: verifica-e-então-age
   if elem in s:
         s.remove(elem)

   # NÃO é seguro para thread: iteração enquanto modifica
   for elem in s:
         process(elem)  # outra thread pode modificar s

Considere a sincronização externa ao compartilhar instâncias de "set"
entre threads. Consulte Suporte do Python para threads livres para
mais informações.


Segurança para thread para objetos bytearray
============================================

   A função "len()" é livre de trava e *atômica*.

   A concatenação e as comparações utilizam o protocolo de buffer, o
   qual impede o redimensionamento, mas não mantém a trava por objeto.
   Essas operações podem observar estados intermediários resultantes
   de modificações concorrentes:

      ba + outro    # pode observar escritas simultâneas
      ba == outro   # pode observar escritas simultâneas
      ba < outro    # pode observar escritas simultâneas

   Todas as outras operações a partir daqui mantêm a trava por objeto.

   A leitura de um único elemento ou de uma fatia é segura para ser
   realizada a partir de múltiplas threads:

      ba[i]        # bytearray.__getitem__
      ba[i:j]      # fatia

   As seguintes operações são seguras para serem chamadas a partir de
   múltiplas threads e não corromperão o bytearray:

      ba[i] = x         # escreve um único byte
      ba[i:j] = valores # escreve uma fatia
      ba.append(x)      # junta um único byte ao final
      ba.extend(outro)  # estende com iterável
      ba.insert(i, x)   # insere um único byte
      ba.pop()          # remove e retorna o último byte
      ba.pop(i)         # remove e retorna o byte no índice
      ba.remove(x)      # remove a primeira ocorrência
      ba.reverse()      # inverte no local
      ba.clear()        # remove todos os bytes

   A atribuição de fatia TRAVA ambos objetos quando *valores* é um
   "bytearray":

      ba[i:j] = other_bytearray  # ambos travados

   As operações a seguir retornam novos objetos e mantêm a trava por
   objeto durante a execução:

      ba.copy()     # retorna uma cópia rasa
      ba * n        # repete em um novo bytearray

   O teste de pertinência mantém a trava durante a sua execução:

      x in ba       # bytearray.__contains__

   Todos os outros métodos de bytearray (como "find()", "replace()",
   "split()", "decode()", etc.) mantêm a trava específica do objeto
   durante sua execução.

   Operações que envolvem múltiplos acessos, assim como iteração,
   nunca são atômicas:

      # NÃO é atômico: verifica-e-então-age
      if x in ba:
          ba.remove(x)

      # NÃO é seguro para thread: iteração enquanto modifica
      for byte in ba:
          process(byte)  # outra thread por modificar ba

   Para iterar com segurança sobre um bytearray que possa ser
   modificado por outra thread, itere sobre uma cópia:

      # Faz uma cópia para iterar com segurança
      for byte in ba.copy():
          process(byte)

   Considere a sincronização externa ao compartilhar instâncias de
   "bytearray" entre threads. Consulte Suporte do Python para threads
   livres para obter mais informações.


Segurança para thread para objetos memoryview
=============================================

Objetos "memoryview" fornecem acesso aos dados internos de um objeto
subjacente sem realizar cópias. A segurança para thread depende tanto
do próprio memoryview quanto do exportador de buffer subjacente.

A implementação do memoryview utiliza operações atômicas para rastrear
suas próprias exportações na *construção com threads livres* (*free-
threaded build*). A criação e a liberação de um memoryview são seguras
para thread. O acesso a atributos (por exemplo, "shape", "format") lê
campos que são imutáveis durante todo o ciclo de vida do memoryview;
portanto, leituras concorrentes são seguras, desde que o memoryview
não tenha sido liberado.

No entanto, os dados reais acessados por meio do memoryview pertencem
ao objeto subjacente. O acesso concorrente a esses dados só é seguro
se o objeto subjacente o oferecer suporte a isso:

* Para objetos imutáveis como "bytes", leituras concorrentes por meio
  de múltiplos memoryviews são seguras.

* Para objetos mutáveis como "bytearray", a leitura e a escrita na
  mesma região de memória a partir de múltiplas threads, sem
  sincronização externa, não são seguras e podem resultar em corrupção
  de dados. Observe que mesmo *memoryviews* somente leitura de objetos
  mutáveis não impedem condições de corrida se o objeto subjacente for
  modificado por outra thread.

   # NÃO é seguro: escritas concorrentes ao mesmo buffer
   data = bytearray(1000)
   view = memoryview(data)
   # Thread 1: view[0:500] = b'x' * 500
   # Thread 2: view[0:500] = b'y' * 500

   # Seguro: usa uma trava para acesso concorrente
   import threading
   lock = threading.Lock()
   data = bytearray(1000)
   view = memoryview(data)

   with lock:
       view[0:500] = b'x' * 500

Redimensionar ou realocar o objeto subjacente (como ao chamar
"bytearray.resize()") enquanto um memoryview está exportado levanta
uma exceção "BufferError". Essa regra é aplicada independentemente do
uso de threads.
