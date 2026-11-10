"collections.abc" --- Classes Base Abstratas para Contêineres
*************************************************************

Adicionado na versão 3.3: Anteriormente, esse módulo fazia parte do
módulo "collections".

**Código-fonte:** Lib/_collections_abc.py

======================================================================

Esse módulo fornece *classes base abstratas* que podem ser usadas para
testar se uma classe fornece uma interface específica; por exemplo, se
é *hasheável* ou se é um *mapeamento*.

Um teste "issubclass()" ou "isinstance()" para uma interface funciona
em uma das três formas.

1. Uma classe recém-escrita pode herdar diretamente de uma das classes
   base abstratas. A classe deve fornecer os métodos abstratos
   necessários. Os métodos mixin restantes vêm da herança e podem ser
   substituídos se desejado. Outros métodos podem ser adicionados
   conforme necessário:

      class C(Sequence):                      # Herança direta
          def __init__(self): ...             # Método extra não exigido pela ABC
          def __getitem__(self, index):  ...  # Método abstrato exigido
          def __len__(self):  ...             # Método abstrato exigido
          def count(self, value): ...         # Opcionalmente substitui um método mixin

      >>> issubclass(C, Sequence)
      True
      >>> isinstance(C(), Sequence)
      True

2. Classes existentes e classes embutidas podem ser registradas como
   "subclasses virtuais" dos ABCs. Essas classes devem definir a API
   completa, incluindo todos os métodos abstratos e todos os métodos
   mixin. Isso permite que os usuários confiem nos testes
   "issubclass()" ou "isinstance()" para determinar se a interface
   completa é suportada. A exceção a essa regra é para métodos que são
   automaticamente inferidos do restante da API:

      class D:                                 # Sem herança
          def __init__(self): ...              # Método extra exigido pela ABC
          def __getitem__(self, index):  ...   # Método abstrato
          def __len__(self):  ...              # Método abstrato
          def count(self, value): ...          # Método mixin
          def index(self, value): ...          # Método mixin

      Sequence.register(D)                     # Registra ao invés de herdar

      >>> issubclass(D, Sequence)
      True
      >>> isinstance(D(), Sequence)
      True

   Neste exemplo, a classe "D" não precisa definir "__contains__",
   "__iter__" e "__reversed__" porque o operador in, a lógica
   *iteration* e a função "reversed()" retornam automaticamente para o
   uso de "__getitem__" e "__len__".

3. Algumas interfaces simples são diretamente reconhecíveis pela
   presença dos métodos necessários (a menos que esses métodos tenham
   sido definidos como "None"):

      class E:
          def __iter__(self): ...
          def __next__(self): ...

      >>> issubclass(E, Iterable)
      True
      >>> isinstance(E(), Iterable)
      True

   Interfaces complexas não oferecem suporte a esta última técnica
   porque uma interface é mais do que apenas a presença de nomes de
   métodos. Interfaces especificam semântica e relacionamentos entre
   métodos que não podem ser inferidos somente da presença de nomes de
   métodos específicos. Por exemplo, saber que uma classe fornece
   "__getitem__", "__len__" e "__iter__" é insuficiente para
   distinguir uma "Sequence" de uma "Mapping".

Adicionado na versão 3.9: Essas classes abstratas agora oferecem
suporte a "[]". Veja Tipo Generic Alias e **PEP 585**.


Classes Base Abstratas de Coleções
==================================

O módulo de coleções oferece o seguinte *ABCs*:

+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| ABC                            | Herda de               | Métodos abstratos       | Métodos mixin                                        |
|================================|========================|=========================|======================================================|
| "Container" [1]                |                        | "__contains__"          |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Hashable" [1]                 |                        | "__hash__"              |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Iterable" [1] [2]             |                        | "__iter__"              |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Iterator" [1]                 | "Iterable"             | "__next__"              | "__iter__"                                           |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Reversible" [1]               | "Iterable"             | "__reversed__"          |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Generator"  [1]               | "Iterator"             | "send", "throw"         | "close", "__iter__", "__next__"                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Sized"  [1]                   |                        | "__len__"               |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Callable"  [1]                |                        | "__call__"              |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Collection"  [1]              | "Sized", "Iterable",   | "__contains__",         |                                                      |
|                                | "Container"            | "__iter__", "__len__"   |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Sequence"                     | "Reversible",          | "__getitem__",          | "__contains__", "__iter__", "__reversed__", "index", |
|                                | "Collection"           | "__len__"               | and "count"                                          |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "MutableSequence"              | "Sequence"             | "__getitem__",          | Herdados métodos de "Sequence" e "append", "clear",  |
|                                |                        | "__setitem__",          | "reverse", "extend", "pop", "remove" e "__iadd__"    |
|                                |                        | "__delitem__",          |                                                      |
|                                |                        | "__len__", "insert"     |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "ByteString"                   | "Sequence"             | "__getitem__",          | Métodos herdados de "Sequence"                       |
|                                |                        | "__len__"               |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Set"                          | "Collection"           | "__contains__",         | "__le__", "__lt__", "__eq__", "__ne__", "__gt__",    |
|                                |                        | "__iter__", "__len__"   | "__ge__", "__and__", "__or__", "__sub__",            |
|                                |                        |                         | "__rsub__", "__xor__", "__rxor__" e "isdisjoint"     |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "MutableSet"                   | "Set"                  | "__contains__",         | Herdado "Set" métodos e "clear", "pop", "remove",    |
|                                |                        | "__iter__", "__len__",  | "__ior__", "__iand__", "__ixor__", e "__isub__"      |
|                                |                        | "add", "discard"        |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Mapping"                      | "Collection"           | "__getitem__",          | "__contains__", "keys", "items", "values", "get",    |
|                                |                        | "__iter__", "__len__"   | "__eq__", e "__ne__"                                 |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "MutableMapping"               | "Mapping"              | "__getitem__",          | Herdado "Mapping" métodos e "pop", "popitem",        |
|                                |                        | "__setitem__",          | "clear", "update", e "setdefault"                    |
|                                |                        | "__delitem__",          |                                                      |
|                                |                        | "__iter__", "__len__"   |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "MappingView"                  | "Sized"                |                         | "__init__", "__len__" e "__repr__"                   |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "ItemsView"                    | "MappingView", "Set"   |                         | "__contains__", "__iter__"                           |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "KeysView"                     | "MappingView", "Set"   |                         | "__contains__", "__iter__"                           |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "ValuesView"                   | "MappingView",         |                         | "__contains__", "__iter__"                           |
|                                | "Collection"           |                         |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Awaitable" [1]                |                        | "__await__"             |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Coroutine" [1]                | "Awaitable"            | "send", "throw"         | "close"                                              |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "AsyncIterable" [1]            |                        | "__aiter__"             |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "AsyncIterator" [1]            | "AsyncIterable"        | "__anext__"             | "__aiter__"                                          |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "AsyncGenerator" [1]           | "AsyncIterator"        | "asend", "athrow"       | "aclose", "__aiter__", "__anext__"                   |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+
| "Buffer" [1]                   |                        | "__buffer__"            |                                                      |
+--------------------------------+------------------------+-------------------------+------------------------------------------------------+

-[ Notas de rodapé ]-

[1] Essas ABCs substituem "__subclasshook__()" para dar suporte ao
    teste de uma interface verificando se os métodos necessários estão
    presentes e não foram definidos como "None". Isso só funciona para
    interfaces simples. Interfaces mais complexas exigem registro ou
    subclassificação direta.

[2] A verificação "isinstance(obj, Iterable)" detecta classes que são
    registradas como "Iterable" ou que possuem um método "__iter__()",
    mas que não detecta classes que iteram com o método
    "__getitem__()". A única maneira confiável de determinar se um
    objeto é *iterável* é chamar "iter(obj)".


Classes Base Abstrata de Coleções -- Descrições Detalhadas
==========================================================

class collections.abc.Container

   ABC para classes que fornecem o método "__contains__()".

class collections.abc.Hashable

   ABC para classes que fornecem o método "__hash__()".

class collections.abc.Sized

   ABC para classes que fornecem o método "__len__()".

class collections.abc.Callable

   ABC para classes que fornecem o método "__call__()".

   Veja Anotações de objetos chamáveis para detalhes sobre como usar
   "Callable" em anotações de tipos.

class collections.abc.Iterable

   ABC para classes que fornecem o método "__iter__()".

   A verificação "isinstance(obj, Iterable)" detecta classes que são
   registradas como "Iterable" ou que possuem um método "__iter__()",
   mas que não detecta classes que iteram com o método
   "__getitem__()". A única maneira confiável de determinar se um
   objeto é *iterável* é chamar "iter(obj)".

class collections.abc.Collection

   ABC para classes de contêiner iterável de tamanho.

   Adicionado na versão 3.6.

class collections.abc.Iterator

   ABC para classes que fornecem os métodos "__iter__()" e métodos
   "__next__()". Veja também a definição de *iterator*.

class collections.abc.Reversible

   ABC para classes iteráveis que também fornecem o método
   "__reversed__()".

   Adicionado na versão 3.6.

class collections.abc.Generator

   ABC para classes *geradores* que implementam o protocolo definido
   em **PEP 342** que estende os *iteradores* com os métodos "send()",
   "throw()" e "close()".

   Consulte Anotando geradores e corrotinas para obter detalhes sobre
   como usar "Generator" em anotações de tipos.

   Adicionado na versão 3.5.

class collections.abc.Sequence
class collections.abc.MutableSequence
class collections.abc.ByteString

   ABCs para *sequências* somente de leitura e mutáveis.

   Nota de implementação: Alguns métodos mixin, como "__iter__()",
   "__reversed__()" e "index()", fazem chamadas repetidas ao método
   subjacente "__getitem__()". Consequentemente, se "__getitem__()"
   for implementado com velocidade de acesso constante, os métodos
   mixin terão desempenho linear; no entanto, se o método subjacente
   for linear (como seria com uma lista encadeada), os mixins terão
   desempenho quadrático e provavelmente precisarão ser substituídos.

   index(value, start=0, stop=None)

      Retorna o primeiro índice de *valor*.

      Levanta "ValueError" se o valor não estiver presente.

      Suporte aos argumentos *start* e *stop* é opcional, mas
      recomendado.

      Alterado na versão 3.5: O método "index()" ganhou suporte para
      os argumentos *stop* e *start*.

   Descontinuado desde a versão 3.12, será removido na versão 3.17: A
   ABC "ByteString" foi descontinuada.Use "isinstance(obj,
   collections.abc.Buffer)" para testar se "obj" implementa o
   protocolo de buffer em tempo de execução. Para uso em anotações de
   tipo, use "Buffer" ou uma união que especifique explicitamente os
   tipos suportados pelo seu código (por exemplo, "bytes | bytearray |
   memoryview")."ByteString" foi originalmente concebido para ser uma
   classe abstrata que serviria como um supertipo de "bytes" e
   "bytearray". No entanto, como o ABC nunca teve métodos, saber que
   um objeto era uma instância de "ByteString" nunca lhe dizia nada de
   útil sobre o objeto. Outros tipos comuns de buffer, como
   "memoryview", também nunca foram entendidos como subtipos de
   "ByteString" (seja em tempo de execução ou por verificadores de
   tipo estáticos).Consulte **PEP** para mais detalhes.

class collections.abc.Set
class collections.abc.MutableSet

   ABCs para conjuntos somente leitura e mutáveis.

class collections.abc.Mapping
class collections.abc.MutableMapping

   ABCs para somente leitura e mutável *mappings*.

class collections.abc.MappingView
class collections.abc.ItemsView
class collections.abc.KeysView
class collections.abc.ValuesView

   ABCs para mapeamento, itens, chaves e valores *views*.

class collections.abc.Awaitable

   ABC para objetos *aguardáveis*, que podem ser usados em expressões
   de "await". Implementações personalizadas devem fornecer o método
   "__await__()".

   Objetos e instâncias de *corrotina* da ABC "Coroutine" são todas
   instâncias dessa ABC.

   Nota:

     No CPython, as corrotinas baseados em gerador (*geradores*
     decorados com "@types.coroutine") são *aguardáveis*, embora não
     possuam o método "__await__()". Usar "isinstance(gencoro,
     Awaitable)" para eles retornará "False". Use
     "inspect.isawaitable()" para detectá-los.

   Adicionado na versão 3.5.

class collections.abc.Coroutine

   ABC para classes compatíveis com *corrotina*. Eles implementam os
   seguintes métodos, definidos em Objetos corrotina: "send()",
   "throw()", e "close()". Implementações personalizadas também devem
   implementar "__await__()". Todas as instâncias "Coroutine" também
   são instâncias de "Awaitable".

   Nota:

     No CPython, as corrotinas baseados em gerador (*geradores*
     decorados com "@types.coroutine") são *aguardáveis*, embora não
     possuam o método "__await__()". Usar "isinstance(gencoro,
     Coroutine)" para eles retornará "False". Use
     "inspect.isawaitable()" para detectá-los.

   Consulte Anotando geradores e corrotinas para obter detalhes sobre
   como usar "Coroutine" em anotações de tipos. A variância e a ordem
   dos parâmetros de tipo correspondem às de "Generator".

   Adicionado na versão 3.5.

class collections.abc.AsyncIterable

   ABC para classes que fornecem um método "__aiter__". Veja também a
   definição de *iterável assíncrono*.

   Adicionado na versão 3.5.

class collections.abc.AsyncIterator

   ABC para classes que fornecem os métodos "__aiter__" e "__anext__".
   Veja também a definição de *iterador assíncrono*.

   Adicionado na versão 3.5.

class collections.abc.AsyncGenerator

   ABC para classes de *gerador assíncrono* que implementam o
   protocolo definido em **PEP 525** e **PEP 492**.

   Consulte Anotando geradores e corrotinas para obter detalhes sobre
   como usar "AsyncGenerator" em anotações de tipos.

   Adicionado na versão 3.6.

class collections.abc.Buffer

   ABC para classes que fornecem o método "__buffer__()",
   implementando o protocolo buffer. Veja **PEP 688**.

   Adicionado na versão 3.12.


Exemplos e receitas
===================

ABCs nos permitem perguntar a classes ou instâncias se elas fornecem
funcionalidades específicas, por exemplo:

   size = None
   if isinstance(myvar, collections.abc.Sized):
       size = len(myvar)

Vários ABCs também são também úteis como mixins que facilitam o
desenvolvimento de classes que suportam APIs de contêiner. Por
exemplo, para escrever uma classe que suporte toda a API "Set" , é
necessário fornecer apenas os três métodos abstratos subjacentes:
"__contains__()", "__iter__()", e "__len__()". O ABC fornece os
métodos restantes, como "__and__()" e "isdisjoint()":

   class ListBasedSet(collections.abc.Set):
       ''' Alternate set implementation favoring space over speed
           and not requiring the set elements to be hashable. '''
       def __init__(self, iterable):
           self.elements = lst = []
           for value in iterable:
               if value not in lst:
                   lst.append(value)

       def __iter__(self):
           return iter(self.elements)

       def __contains__(self, value):
           return value in self.elements

       def __len__(self):
           return len(self.elements)

   s1 = ListBasedSet('abcdef')
   s2 = ListBasedSet('defghi')
   overlap = s1 & s2            # O método __and__() é automaticamente suportado

Notas sobre o uso de "Set" e "MutableSet" como um mixin:

1. Como algumas operações de conjunto criam novos conjuntos, os
   métodos de mixin padrão precisam de uma maneira de criar novas
   instâncias a partir de um *iterável*. Supõe-se que a classe
   construtor tenha uma assinatura no formato "ClassName(iterable)".
   Essa suposição é fatorada em um "classmethod" interno chamado
   "_from_iterable()" que chama "cls(iterable)" para produzir um novo
   conjunto. Se o mixin "Set" estiver sendo usado em uma classe com
   uma assinatura de construtor diferente, você precisará substituir
   "_from_iterable()" por um método de classe ou um método regular que
   possa construir novas instâncias a partir de um argumento iterável.

2. Para substituir as comparações (presumivelmente para velocidade, já
   que a semântica é fixa), redefina "__le__()" e "__ge__()", então as
   outras operações seguirão o exemplo automaticamente.

3. O mixin "Set" fornece um método "_hash()" para calcular um valor de
   hash para o conjunto; no entanto, "__hash__()" não é definido
   porque nem todos os conjuntos são *hasheáveis* ou imutáveis. Para
   adicionar hasheabilidade em conjuntos usando mixin, herde de ambos
   "Set" e "Hashable", e então defina "__hash__ = Set._hash".

Ver também:

  * OrderedSet receita para um exemplo baseado em "MutableSet".

  * Para mais informações sobre ABCs, consulte o módulo "abc" e **PEP
    3119**.
