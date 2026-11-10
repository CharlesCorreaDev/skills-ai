"typing" --- Suporte para dicas de tipo
***************************************

Adicionado na versão 3.5.

**Código-fonte:** Lib/typing.py

Nota:

  O ambiente de execução do Python não força anotações de tipos de
  variáveis e funções. Elas podem ser usadas por ferramentas de
  terceiros como *verificadores de tipo*, IDEs, linters, etc.

======================================================================

Este módulo fornece suporte em tempo de execução para dicas de tipo.

Considere a função abaixo:

   def surface_area_of_cube(edge_length: float) -> str:
       return f"A área superficial de um cubo é {6 * edge_length ** 2}."

A função "surface_area_of_cube" recebe um argumento que se espera ser
uma instância de "float", conforme indicado pela *dica de tipo*
"edge_length: float". Espera-se que a função retorne uma instância de
"str", conforme indicado pela dica "-> str".

Embora as dicas de tipo possam ser classes simples como "float" ou
"str", elas também podem ser mais complexas. O módulo "typing" fornece
um vocabulário de dicas de tipo mais avançadas.

Novos recursos são frequentemente adicionados ao módulo "typing". O
pacote typing_extensions fornece backports desses novos recursos para
versões mais antigas do Python.

Ver também:

  Folha de dicas sobre tipagem
     Uma visão geral das dicas de tipo (hospedado por mypy docs, em
     inglês).

  Seção de referência do sistema de tipos da documentação do mypy
     O sistema de tipagem do Python é padronizado pelas PEPs, portanto
     esta  referência deve se aplicar a maioria do verificadores de
     tipo do Python. (Alguns trechos podem se referir especificamente
     ao mypy. Documento em inglês).

  Static Typing with Python
     Documentação independente de verificador de tipo escrita pela
     comunidade, detalhando os recursos do sistema de tipo,
     ferramentas úteis de tipagem e melhores práticas.


Especificação para o sistema de tipos do Python
===============================================

A especificação canônica e atualizada do sistema de tipos Python pode
ser encontrada em Specification for the Python type system.


Apelidos de tipo
================

Um apelido de tipo é definido utilizando a instrução "type", que por
sua vez cria uma instância da classe "TypeAliasType". Neste exemplo,
"Vector" e "list[float]" serão tratados de maneira equivalente pelos
verificadores de tipo estático:

   type Vector = list[float]

   def scale(scalar: float, vector: Vector) -> Vector:
       return [scalar * num for num in vector]

   # passa na verificação de tipos; uma lista de floats é qualificada como Vector.
   new_vector = scale(2.0, [1.0, -4.2, 5.4])

Apelidos de tipo são úteis para simplificar assinaturas de tipo
complexas. Por exemplo:

   from collections.abc import Sequence

   type ConnectionOptions = dict[str, str]
   type Address = tuple[str, int]
   type Server = tuple[Address, ConnectionOptions]

   def broadcast_message(message: str, servers: Sequence[Server]) -> None:
       ...

   # O verificador de tipo tratará a assinatura de tipo anterior
   # como exatamente equivalente à assinatura abaixo.
   def broadcast_message(
       message: str,
       servers: Sequence[tuple[tuple[str, int], dict[str, str]]]
   ) -> None:
       ...

A instrução "type" é nova no Python 3.12. Para manter
retrocompatibilidade, apelidos de tipo também podem ser criados usando
atribuição:

   Vector = list[float]

Ou marcado com "TypeAlias" para tornar explícito que se trata de um
apelido de tipo e não uma atribuição de variável comum:

   from typing import TypeAlias

   Vector: TypeAlias = list[float]


NewType
=======

Utilize o auxiliar "NewType" para criar tipos únicos:

   from typing import NewType

   UserId = NewType('UserId', int)
   some_id = UserId(524313)

O verificador de tipo estático tratará o novo tipo como se fosse uma
subclasse do tipo original. Isso é útil para ajudar a encontrar erros
de lógica:

   def get_user_name(user_id: UserId) -> str:
       ...

   # passa na verificação de tipo
   user_a = get_user_name(UserId(42351))

   # falha na verificação de tipo: um int não é um UserId
   user_b = get_user_name(-1)

Você ainda pode executar todas as operações "int" em uma variável do
tipo "UserId", mas o resultado sempre será do tipo "int". Isso permite
que você passe um "UserId" em qualquer ocasião que "int" possa ser
esperado, mas previne que você acidentalmente crie um "UserId" de uma
forma inválida:

   # 'output' é do tipo 'int', em vez de 'UserId'
   output = UserId(23413) + UserId(54341)

Note que essas verificações são aplicadas apenas pelo verificador de
tipo estático. Em tempo de execução, a instrução "Derived =
NewType('Derived', Base)" irá tornar "Derived" um chamável que
retornará imediatamente qualquer parâmetro que você passar. Isso
significa que a expressão "Derived(some_value)" não cria uma nova
classe ou introduz sobrecarga além de uma chamada regular de
função.instrução

Mais precisamente, a expressão "some_value is Derived(some_value)" é
sempre verdadeira em tempo de execução.

É inválido criar um subtipo de "Derived":

   from typing import NewType

   UserId = NewType('UserId', int)

   # Falha em tempo de execução e não passa na verificação de tipos
   class AdminUserId(UserId): pass

No entanto, é possível criar um "NewType" baseado em um 'derivado'
"NewType":

   from typing import NewType

   UserId = NewType('UserId', int)

   ProUserId = NewType('ProUserId', UserId)

e a verificação de tipos para "ProUserId" funcionará como esperado.

Veja **PEP 484** para mais detalhes.

Nota:

  Lembre-se que o uso de um apelido de tipo declara que dois tipos
  serão *equivalentes* entre si. Efetuar "type Alias = Original" fará
  o verificador de tipo estático tratar "Alias" como sendo *exatamente
  equivalente* a "Original" em todos os casos. Isso é útil quando você
  deseja simplificar assinaturas de tipo complexas.Em contraste,
  "NewType" declara que um tipo será *subtipo* de outro. Efetuando
  "Derived = NewType('Derived', Original)" irá fazer o verificador de
  tipo estático tratar "Derived" como uma *subclasse* de "Original", o
  que significa que um valor do tipo "Original" não pode ser utilizado
  onde um valor do tipo "Derived" é esperado. Isso é útil quando você
  deseja evitar erros de lógica com custo mínimo de tempo de execução.

Adicionado na versão 3.5.2.

Alterado na versão 3.10: "NewType" agora é uma classe em vez de uma
função. Consequentemente, existem alguns custos em tempo de execução
ao chamar "NewType" em vez de uma função comum.

Alterado na versão 3.11: O desempenho de chamar "NewType" voltou ao
mesmo nível da versão Python 3.9.


Anotações de objetos chamáveis
==============================

Funções -- ou outros objetos *chamáveis* -- podem ser anotados com
"collections.abc.Callable" ou com o tipo descontinuado
"typing.Callable". "Callable[[int], str]" expressa uma função que
recebe um único parâmetro de tipo "int" e retorna uma "str".

Por exemplo:

   from collections.abc import Callable, Awaitable

   def feeder(get_next_item: Callable[[], str]) -> None:
       ...  # Corpo

   def async_query(on_success: Callable[[int], None],
                   on_error: Callable[[int, Exception], None]) -> None:
       ...  # Corpo

   async def on_update(value: str) -> None:
       ...  # Corpo

   callback: Callable[[str], Awaitable[None]] = on_update

A sintaxe de subscrição deve sempre ser usada com exatamente dois
valores: a lista de argumentos e o tipo de retorno. A lista de
argumentos deve ser uma lista de tipos, uma "ParamSpec", "Concatenate"
ou reticências ("..."). O tipo de retorno deve ser um tipo único.

Se uma reticências literal "..." é passada no lugar de uma lista de
argumentos, ela indica que um chamável com uma lista de qualquer
parâmetro arbitrário seria aceita.

   def concat(x: str, y: str) -> str:
       return x + y

   x: Callable[..., str]
   x = str     # OK
   x = concat  # OK também

"Callable" não pode representar assinaturas complexas, como funções
que aceitam um número variado de argumentos, funções sobrecarregadas,
or funções que recebem apenas parâmetros somente-nomeados. No entanto,
essas assinaturas podem ser expressas ao se definir uma  "Protocol"
com um método "__call__()":

   from collections.abc import Iterable
   from typing import Protocol

   class Combiner(Protocol):
       def __call__(self, *vals: bytes, maxlen: int | None = None) -> list[bytes]: ...

   def batch_proc(data: Iterable[bytes], cb_results: Combiner) -> bytes:
       for item in data:
           ...

   def good_cb(*vals: bytes, maxlen: int | None = None) -> list[bytes]:
       ...
   def bad_cb(*vals: bytes, maxitems: int | None) -> list[bytes]:
       ...

   batch_proc([], good_cb)  # OK
   batch_proc([], bad_cb)   # Erro! Argumento 2 tem tipo incompatível por ter
                            # nome e tipo diferente do callback

Chamáveis que recebem outros chamáveis como argumentos podem indicar
que seus tipos de parâmetro dependem uns dos outros usando
"ParamSpec". Além disso, se esse chamável adiciona ou remove
argumentos de outros chamáveis, o operador "Concatenate" pode ser
usado.  Eles assumem a forma de "Callable[ParamSpecVariable,
ReturnType]" e "Callable[Concatenate[Arg1Type, Arg2Type, ...,
ParamSpecVariable], ReturnType]", respectivamente.

Alterado na versão 3.10: "Callable" agora oferece suporte a
"ParamSpec" e "Concatenate". Veja **PEP 612** para mais detalhes.

Ver também:

  A documentação para "ParamSpec" e "Concatenate" contém exemplos de
  uso em "Callable".


Genéricos
=========

Como a informação de tipo sobre objetos mantidos em contêineres não
pode ser inferida estaticamente de uma maneira genérica, muitas
classes de contêineres na biblioteca padrão permitem usar subscrição
para denotar o tipo esperado dos elementos dos contêineres.

   from collections.abc import Mapping, Sequence

   class Employee: ...

   # Sequence[Employee] indica que todos os elementos na sequência
   # devem ser instâncias de "Employee".
   # Mapping[str, str] indica que todas as chaves e valores no mapeamento
   # devem ser strings.
   def notify_by_email(employees: Sequence[Employee],
                       overrides: Mapping[str, str]) -> None: ...

Funções e classes genéricas podem ser parametrizadas utilizando a
sintaxe de parâmetro de tipos:

   from collections.abc import Sequence

   def first[T](l: Sequence[T]) -> T:  # Função é genérica sobre TypeVar "T"
       return l[0]

Ou utilizando a fábrica "TypeVar" diretamente:

   from collections.abc import Sequence
   from typing import TypeVar

   U = TypeVar('U')                  # Declara tipo variável "U"

   def second(l: Sequence[U]) -> U:  # Função é genérica sobre a TypeVar "U"
       return l[1]

Alterado na versão 3.12: O suporte sintático para genéricos é novo no
Python 3.12.


Anotando tuplas
===============

Para a maior parte dos tipos contêineres em Python, o sistema de
tipagem presume que todos os elementos do contêiner são do mesmo tipo.
Por exemplo:

   from collections.abc import Mapping

   # Verificador de tipos irá inferir que todos os elementos em ``x`` devem ser ints
   x: list[int] = []

   # Erro no verificador: ``list`` aceita um único tipo de argumento
   y: list[int, str] = [1, 'foo']

   # Verificador de tipos irá inferir que todas as chaves em ``z`` devem ser strings,
   # e todos os valores em ``z`` devem ser strings ou ints
   z: Mapping[str, str | int] = {}

"list" aceita apenas um tipo de argumento, e assim o verificador de
tipos emitirá um erro na atribuição "y" acima. Da mesma forma,
"Mapping" aceita apenas dois tipos de argumento: O primeiro indica o
tipo das chaves, e o segundo indica o tipo dos valores.

Ao contrário da maioria dos outros contêineres Python, é comum no
código Python idiomático que as tuplas tenham elementos que não sejam
todos do mesmo tipo. Por esse motivo, as tuplas têm um caso especial
no sistema de tipagem do Python. "tuple" aceita *qualquer quantidade*
de argumentos de tipo:

   # OK: ``x`` foi atribuída a uma tupla de comprimento 1, onde o único elemento é um int
   x: tuple[int] = (5,)

   # OK: ``y`` foi atribuída a uma tupla de comprimento 2;
   # o elemento 1 é um int, o elemento 2 é uma str
   y: tuple[int, str] = (5, "foo")

   # Erro: a anotação de tipo indica uma tupla de comprimento 1,
   # mas ``z`` foi atribuída a uma tupla de comprimento 3
   z: tuple[int] = (1, 2, 3)

Para denotar uma tupla que pode ter *qualquer* comprimento e na qual
todos os elementos são do mesmo tipo "T", use a literal de reticências
"...": "tuple[T, ...]". Para denotar uma tupla vazia, use "tuple[()]".
Usar "tuple" simples como anotação equivale a usar "tuple[Any, ...]":

   x: tuple[int, ...] = (1, 2)
   # Essas reatribuições são OK: ``tuple[int, ...]`` indica que x pode ter qualquer comprimento
   x = (1, 2, 3)
   x = ()
   # Essa reatribuição é um erro: todos os elementos de ``x`` devem ser ints
   x = ("foo", "bar")

   # ``y`` só pode ser atribuída a uma tupla vazia
   y: tuple[()] = ()

   z: tuple = ("foo", "bar")
   # Essas reatribuições são OK: o tipo ``tuple`` equivale a ``tuple[Any, ...]``
   z = (1, 2, 3)
   z = ()


O tipo de objetos de classe
===========================

Uma variável anotada com "C" pode aceitar um valor de tipo "C". Por
outro lado, uma variável anotada com "type[C]" (ou o tipo
descontinuado "typing.Type[C]") pode aceitar valores que são as
próprias classes -- mais especificamente, ela aceitará o *objeto
classe* de "C". Por exemplo:

   a = 3         # Tem tipo ``int``
   b = int       # Tem tipo ``type[int]``
   c = type(a)   # Também tem tipo ``type[int]``

Observe que "type[C]" é covariante:

   class User: ...
   class ProUser(User): ...
   class TeamUser(User): ...

   def make_new_user(user_class: type[User]) -> User:
       # ...
       return user_class()

   make_new_user(User)      # OK
   make_new_user(ProUser)   # Também OK: ``type[ProUser]`` é subtipo de ``type[User]``
   make_new_user(TeamUser)  # Tudo bem
   make_new_user(User())    # Erro: esperava-se ``type[User]`` mas retornou ``User``
   make_new_user(int)       # Erro: ``type[int]`` não é subtipo de ``type[User]``

Os únicos parâmetros válidos para "type" são classes, "Any", type
variables e uniões de qualquer um desses tipos. Por exemplo:

   def new_non_team_user(user_class: type[BasicUser | ProUser]): ...

   new_non_team_user(BasicUser)  # OK
   new_non_team_user(ProUser)    # OK
   new_non_team_user(TeamUser)   # Erro: ``type[TeamUser]`` não é subtipo
                                 # de ``type[BasicUser | ProUser]``
   new_non_team_user(User)       # Também é um erro

"type[Any]" é equivalente a "type", que é a raiz da hierarquia de
metaclasses do Python.


Anotando geradores e corrotinas
===============================

Um gerador pode ser anotado usando um tipo genérico
"Generator[YieldType, SendType, ReturnType]". Por exemplo:

   def echo_round() -> Generator[int, float, str]:
       sent = yield 0
       while sent >= 0:
           sent = yield round(sent)
       return 'Done'

Note que, diferentemente de outras classes genéricas na biblioteca
padrão, o "SendType" da classe "Generator" se comporta
contravariantemente, em vez de covariantemente ou invariantemente.

Os parâmetros "SendType" e "ReturnType" são "None" por padrão:

   def infinite_stream(start: int) -> Generator[int]:
       while True:
           yield start
           start += 1

Também é possível definir esses tipos explicitamente:

   def infinite_stream(start: int) -> Generator[int, None, None]:
       while True:
           yield start
           start += 1

Geradores simples que só produzem valores também podem ser anotados
com tipo de retorno "Iterable[YieldType]" ou "Iterator[YieldType]":

   def infinite_stream(start: int) -> Iterator[int]:
       while True:
           yield start
           start += 1

Geradores assíncronos são manipulados similarmente, mas não espere um
argumento de tipo "ReturnType" ("AsyncGenerator[YieldType,
SendType]"). O argumento "SendType" é "None" por padrão, então as
seguintes definições são equivalentes:

   async def infinite_stream(start: int) -> AsyncGenerator[int]:
       while True:
           yield start
           start = await increment(start)

   async def infinite_stream(start: int) -> AsyncGenerator[int, None]:
       while True:
           yield start
           start = await increment(start)

Como no caso síncrono, "AsyncIterable[YieldType]" e
"AsyncIterator[YieldType]" também estão disponíveis:

   async def infinite_stream(start: int) -> AsyncIterator[int]:
       while True:
           yield start
           start = await increment(start)

Corrotinas podem ser anotadas usando "Coroutine[YieldType, SendType,
ReturnType]". Argumentos genéricos correspondem àqueles da classe
"Generator", por exemplo:

   from collections.abc import Coroutine
   c: Coroutine[list[str], str, int]  # Uma corrotina defina em outro lugar
   x = c.send('hi')                   # Tipo inferido de 'x' é list[str]
   async def bar() -> None:
       y = await c                    # Tipo inferido de 'y' é int


Tipos genéricos definidos pelo usuário
======================================

Uma classe definida pelo usuário pode ser definida como uma classe
genérica.

   from logging import Logger

   class LoggedVar[T]:
       def __init__(self, value: T, name: str, logger: Logger) -> None:
           self.name = name
           self.logger = logger
           self.value = value

       def set(self, new: T) -> None:
           self.log('Set ' + repr(self.value))
           self.value = new

       def get(self) -> T:
           self.log('Get ' + repr(self.value))
           return self.value

       def log(self, message: str) -> None:
           self.logger.info('%s: %s', self.name, message)

Esta sintaxe indica que o classe "LoggedVar" é parametrizada em torno
de uma única  type variable "T". Isso também torna "T" válido como um
tipo dentro do corpo da classe.

Classes genéricas implicitamente herdar de "Generic". Para
compatibilidade com Python 3.11 e versões inferiores, também é
possível herdar explicitamente de "Generic" para indicar uma classe
genérica:

   from typing import TypeVar, Generic

   T = TypeVar('T')

   class LoggedVar(Generic[T]):
       ...

Classes genéricas têm métodos "__class_getitem__()", o que significa
que podem ser parametrizadas em tempo de execução (por exemplo,
"LoggedVar[int]" abaixo):

   from collections.abc import Iterable

   def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
       for var in vars:
           var.set(0)

Um tipo genérico pode ter qualquer número de tipos de variáveis. Todas
as variedades de "TypeVar" são permitidas como parâmetros para um tipo
genérico:

   from typing import TypeVar, Generic, Sequence

   class WeirdTrio[T, B: Sequence[bytes], S: (int, str)]:
       ...

   OldT = TypeVar('OldT', contravariant=True)
   OldB = TypeVar('OldB', bound=Sequence[bytes], covariant=True)
   OldS = TypeVar('OldS', int, str)

   class OldWeirdTrio(Generic[OldT, OldB, OldS]):
       ...

Cada tipo dos argumentos para "Generic" devem ser distintos. Assim, os
seguintes exemplos são inválidos:

   from typing import TypeVar, Generic
   ...

   class Pair[M, M]:  # SyntaxError
       ...

   T = TypeVar('T')

   class Pair(Generic[T, T]):   # INVÁLIDO
       ...

Classes genéricas podem também herdar de outras classes:

   from collections.abc import Sized

   class LinkedList[T](Sized):
       ...

Ao herdar das classes genérico, alguns tipos podem ser fixos:

   from collections.abc import Mapping

   class MyDict[T](Mapping[str, T]):
       ...

Neste caso "MyDict" possui um único parâmetro, "T".

O uso de uma classe genérica sem especificar tipos pressupõe "Any"
para cada posição. No exemplo a seguir, "MyIterable" não é genérico,
mas herda implicitamente de "Iterable[Any]":

   from collections.abc import Iterable

   class MyIterable(Iterable): # Igual a Iterable[Any]
       ...

Também há suporte para tipos genéricos definidos pelo usuário.
Exemplos:

   from collections.abc import Iterable

   type Response[S] = Iterable[S] | int

   # Tipo de retorno aqui é igual a Iterable[str] | int
   def response(query: str) -> Response[str]:
       ...

   type Vec[T] = Iterable[tuple[T, T]]

   def inproduct[T: (int, float, complex)](v: Vec[T]) -> T: # Igual a Iterable[tuple[T, T]]
       return sum(x*y for x, y in v)

Para manter retrocompatibilidade, os apelidos de tipos genéricos
também podem ser criados usando atribuição:

   from collections.abc import Iterable
   from typing import TypeVar

   S = TypeVar("S")
   Response = Iterable[S] | int

Alterado na versão 3.7: "Generic" não possui mais uma metaclasse
personalizada.

Alterado na versão 3.12: Suporte sintático para apelidos de tipo e
genéricos é novo na versão 3.12. Anteriormente, as classes genéricas
precisavam explicitamente herdar de "Generic" ou conter um tipo de
variável em uma de suas bases.

Genéricos definidos pelo usuário para expressões de parâmetros também
oferecem suporte por meio de variáveis de especificação de parâmetros
no formato "[**P]". O comportamento é consistente com as variáveis de
tipo descritas acima, pois as variáveis de especificação de parâmetro
são tratadas pelo módulo "typing" como uma variável de tipo
especializada. A única exceção a isso é que uma lista de tipos pode
ser usada para substituir um "ParamSpec":

   >>> class Z[T, **P]: ...  # T é um TypeVar; P é um ParamSpec
   ...
   >>> Z[int, [dict, float]]
   __main__.Z[int, [dict, float]]

Classes genéricas sobre um "ParamSpec" também podem ser criadas usando
herança explícita de "Generic". Neste caso, "**" não é usado:

   from typing import ParamSpec, Generic

   P = ParamSpec('P')

   class Z(Generic[P]):
       ...

Outra diferença entre "TypeVar" e "ParamSpec" é que um genérico com
apenas uma variável de especificação de parâmetro aceitará listas de
parâmetros nos formatos "X[[Type1, Type2, ...]]" e também "X[Type1,
Type2, ...]" por razões estéticas. Internamente, o último é convertido
no primeiro, portanto são equivalentes:

   >>> class X[**P]: ...
   ...
   >>> X[int, str]
   __main__.X[[int, str]]
   >>> X[[int, str]]
   __main__.X[[int, str]]

Observe que genéricos com "ParamSpec" podem não ter "__parameters__"
corretos após a substituição em alguns casos porque eles são
destinados principalmente à verificação de tipo estático.

Alterado na versão 3.10: "Generic" agora pode ser parametrizado
através de expressões de parâmetros. Veja "ParamSpec" e **PEP 612**
para mais detalhes.

Uma classe genérica definida pelo usuário pode ter ABCs como classes
base sem conflito de metaclasse. Não há suporte a metaclasses
genéricas. O resultado da parametrização de genéricos é armazenado em
cache, e a maioria dos tipos no módulo "typing" são *hasheáveis* e
comparáveis em termos de igualdade.


O tipo "Any"
============

A special kind of type is "Any". A static type checker will treat
every type as assignable to "Any" and "Any" as assignable to every
type.

Isso significa que é possível realizar qualquer operação ou chamada de
método sobre um valor do tipo "Any" e atribuí-lo a qualquer variável:

   from typing import Any

   a: Any = None
   a = []          # OK
   a = 2           # OK

   s: str = ''
   s = a           # OK

   def foo(item: Any) -> int:
       # Passa na verificação de tipos; 'item' pode ser qualquer tipo,
       # e esse tipo pode ter um método 'bar'
       item.bar()
       ...

Observe que nenhuma verificação de tipo é realizada ao atribuir um
valor do tipo "Any" a um tipo mais preciso. Por exemplo, o verificador
de tipo estático não relatou um erro ao atribuir "a" a "s" mesmo que
"s" tenha sido declarado como sendo do tipo "str" e receba um valor
"int" em tempo de execução!

Além disso, todas as funções sem um tipo de retorno ou tipos de
parâmetro terão como padrão implicitamente o uso de "Any":

   def legacy_parser(text):
       ...
       return data

   # Um verificador de tipo estático tratará a função acima
   # como tendo a mesma assinatura da função abaixo:
   def legacy_parser(text: Any) -> Any:
       ...
       return data

Este comportamento permite que "Any" seja usado como uma *saída de
emergência* quando você precisar misturar código tipado dinamicamente
e estaticamente.

Compare o comportamento de "Any" com o comportamento de "object".
Semelhante a "Any", todo tipo é um subtipo de "object". No entanto, ao
contrário de "Any", o inverso não é verdadeiro: "object" *não* é um
subtipo de qualquer outro tipo.

Isso significa que quando o tipo de um valor é "object", um
verificador de tipo rejeitará quase todas as operações nele, e
atribuí-lo a uma variável (ou usá-la como valor de retorno) de um tipo
mais especializado é um tipo erro. Por exemplo:

   def hash_a(item: object) -> int:
       # Fails type checking; an object does not have a 'magic' method.
       item.magic()
       ...

   def hash_b(item: Any) -> int:
       # Passes type checking
       item.magic()
       ...

   # Passes type checking, since ints and strs are subclasses of object
   hash_a(42)
   hash_a("foo")

   # Passes type checking, since Any is assignable to all types
   hash_b(42)
   hash_b("foo")

Use "object" para indicar que um valor pode ser de qualquer tipo de
maneira segura. Use "Any" para indicar que um valor é tipado
dinamicamente.


Subtipagem nominal vs estrutural
================================

Inicialmente a **PEP 484** definiu o sistema de tipos estáticos do
Python como usando *subtipagem nominal*. Isto significa que uma classe
"A" é permitida onde uma classe "B" é esperada se e somente se "A" for
uma subclasse de "B".

Este requisito anteriormente também se aplicava a classes base
abstratas, como "Iterable". O problema com essa abordagem é que uma
classe teve que ser marcada explicitamente para suportá-los, o que não
é pythônico e diferente do que normalmente seria feito em código
Python de tipo dinamicamente idiomático. Por exemplo, isso está em
conformidade com **PEP 484**:

   from collections.abc import Sized, Iterable, Iterator

   class Bucket(Sized, Iterable[int]):
       ...
       def __len__(self) -> int: ...
       def __iter__(self) -> Iterator[int]: ...

**PEP 544** solves this problem by allowing users to write the above
code without explicit base classes in the class definition, allowing
"Bucket" to be implicitly considered a subtype of both "Sized" and
"Iterable[int]" by static type checkers. This is known as *structural
subtyping* (or static duck-typing):

   from collections.abc import Iterator, Iterable

   class Bucket:  # Nota: sem classes base
       ...
       def __len__(self) -> int: ...
       def __iter__(self) -> Iterator[int]: ...

   def collect(items: Iterable[int]) -> int: ...
   result = collect(Bucket())  # Passa na verificação de tipo

Além disso, ao criar uma subclasse de uma classe especial "Protocol",
um usuário pode definir novos protocolos personalizados para
aproveitar ao máximo a subtipagem estrutural (veja exemplos abaixo).


Conteúdo do módulo
==================

O módulo "typing" define as seguintes classes, funções e decoracores.


Tipos primitivos especiais
--------------------------


Tipos especiais
~~~~~~~~~~~~~~~

Eles podem ser usados como tipos em anotações. Eles não oferecem
suporte a subscrição usando "[]".

typing.Any

   Tipo especial que indica um tipo irrestrito.

   * Every type is assignable to "Any".

   * "Any" is assignable to every type.

   Alterado na versão 3.11: "Any" agora pode ser usado como classe
   base. Isso pode ser útil para evitar erros do verificador de tipo
   com classes que podem digitar em qualquer lugar ou são altamente
   dinâmicas.

typing.AnyStr

   Uma tipo variável restrito.

   Definição:

      AnyStr = TypeVar('AnyStr', str, bytes)

   "AnyStr" deve ser usado para funções que podem aceitar argumentos
   "str" ou "bytes" mas não podem permitir que os dois se misturem.

   Por exemplo:

      def concat(a: AnyStr, b: AnyStr) -> AnyStr:
          return a + b

      concat("foo", "bar")    # OK: saída tem tipo 'str'
      concat(b"foo", b"bar")  # OK: saída tem tipo 'bytes'
      concat("foo", b"bar")   # Erro: não se mistura str com bytes

   Note que, apesar do nome, "AnyStr" não tem nada a ver com o tipo
   "Any", nem significa "qualquer string". Em particular, "AnyStr" e
   "str | bytes" são diferentes entre si e têm casos de uso
   diferentes:

      # Uso inválido de AnyStr:
      # A variável de tipo é usada somente uma vez na assinatura da função,
      # então não pode ser "resolvida" pelo verificador de tipo
      def greet_bad(cond: bool) -> AnyStr:
          return "hi there!" if cond else b"greetings!"

      # O jeito melhor de anotar esta função
      def greet_proper(cond: bool) -> str | bytes:
          return "hi there!" if cond else b"greetings!"

   Descontinuado desde a versão 3.13, será removido na versão 3.18:
   Descontinuado em favor da nova sintaxe de parâmetro de tipo. Use
   "class A[T: (str, bytes)]: ..." em vez de importar "AnyStr". Veja a
   **PEP 695** para mais detalhes.No Python 3.16, "AnyStr" será
   removido de "typing.__all__", e avisos de descontinuação serão
   emitidos em tempo de execução quando ele for acessado ou importado
   de "typing". "AnyStr" será removido do "typing" no Python 3.18.

typing.LiteralString

   Tipo especial que inclui apenas strings literais.

   Qualquer literal de string é compatível com "LiteralString", assim
   como outro "LiteralString". Entretanto, um objeto digitado apenas
   "str" não é. Uma string criada pela composição de objetos do tipo
   "LiteralString" também é aceitável como uma "LiteralString".

   Exemplo:

      def run_query(sql: LiteralString) -> None:
          ...

      def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
          run_query("SELECT * FROM students")  # OK
          run_query(literal_string)  # OK
          run_query("SELECT * FROM " + literal_string)  # OK
          run_query(arbitrary_string)  # erro no verificador
          run_query(  # erro no verificador
              f"SELECT * FROM students WHERE name = {arbitrary_string}"
          )

   "LiteralString" é útil para APIs sensíveis onde strings arbitrárias
   geradas pelo usuário podem gerar problemas. Por exemplo, os dois
   casos acima que geram erros no verificador de tipo podem ser
   vulneráveis a um ataque de injeção de SQL.

   Veja **PEP 675** para mais detalhes.

   Adicionado na versão 3.11.

typing.Never
typing.NoReturn

   "Never" e "NoReturn" representam o tipo inferior, um tipo que não
   possui membros.

   Eles podem ser usados para indicar que uma função nunca retorna,
   como "sys.exit()":

      from typing import Never  # ou NoReturn

      def stop() -> Never:
          raise RuntimeError('no way')

   Ou para definir uma função que nunca deve ser chamada, pois não
   existem argumentos válidos, como "assert_never()":

      from typing import Never  # or NoReturn

      def never_call_me(arg: Never) -> None:
          pass

      def int_or_str(arg: int | str) -> None:
          never_call_me(arg)  # erro no verificador
          match arg:
              case int():
                  print("It's an int")
              case str():
                  print("It's a str")
              case _:
                  never_call_me(arg)  # OK, arg é do tipo Never (ou NoReturn)

   "Never" e "NoReturn" têm o mesmo significado no sistema de tipos e
   os verificadores de tipo estático tratam ambos de forma
   equivalente.

   Adicionado na versão 3.6.2: Adicionado "NoReturn".

   Adicionado na versão 3.11: Adicionado "Never".

typing.Self

   Tipo especial para representar a classe atual inclusa.

   Por exemplo:

      from typing import Self, reveal_type

      class Foo:
          def return_self(self) -> Self:
              ...
              return self

      class SubclassOfFoo(Foo): pass

      reveal_type(Foo().return_self())  # Tipo revelado é "Foo"
      reveal_type(SubclassOfFoo().return_self())  # Tipo revelado é "SubclassOfFoo"

   Esta anotação é semanticamente equivalente à seguinte, embora de
   forma mais sucinta:

      from typing import TypeVar

      Self = TypeVar("Self", bound="Foo")

      class Foo:
          def return_self(self: Self) -> Self:
              ...
              return self

   Em geral, se algo retorna "self", como nos exemplos acima, você
   deve usar "Self" como anotação de retorno. Se "Foo.return_self" foi
   anotado como retornando ""Foo"", então o verificador de tipo
   inferiria o objeto retornado de "SubclassOfFoo.return_self" como
   sendo do tipo "Foo" em vez de "SubclassOfFoo".

   Outros casos de uso comuns incluem:

   * "classmethod"s que são usados como construtores alternativos e
     retornam instâncias do parâmetro "cls".

   * Anotando um método "__enter__()" que retorna self.

   Você não deveria usar "Self" como a anotação de retorno se não for
   garantido que o método retorne uma instância de uma subclasse
   quando a classe for subclassificada:

      class Eggs:
          # Self seria uma anotação de retorno incorreta aqui,
          # já que o objeto retornado sempre é instância de Eggs,
          # inclusive em subclasses
          def returns_eggs(self) -> "Eggs":
              return Eggs()

   Veja **PEP 673** para mais detalhes.

   Adicionado na versão 3.11.

typing.TypeAlias

   Anotações especiais para declarar explicitamente um apelido de
   tipo.

   Por exemplo:

      from typing import TypeAlias

      Factors: TypeAlias = list[int]

   "TypeAlias" é particularmente útil em versões mais antigas do
   Python para anotar apelidos que fazem uso de referências futuras,
   pois pode ser difícil para os verificadores de tipo distingui-los
   das atribuições normais de variáveis:

      from typing import Generic, TypeAlias, TypeVar

      T = TypeVar("T")

      # "Box" não existe ainda,
      # então temos que usar aspas para a referência futura em Python <3.12.
      # Usar ``TypeAlias`` diz ao verificador de tipo que isso é uma declaração de apelido de tipo,
      # e não uma atribuição de variável a string.
      BoxOfStrings: TypeAlias = "Box[str]"

      class Box(Generic[T]):
          @classmethod
          def make_box_of_strings(cls) -> BoxOfStrings: ...

   Veja **PEP 613** para mais detalhes.

   Adicionado na versão 3.10.

   Descontinuado desde a versão 3.12: "TypeAlias" foi descontinuado em
   favor da instrução "type", que cria instâncias de "TypeAliasType" e
   oferece suporte nativo a  referências futuras. Observe que embora
   "TypeAlias" e "TypeAliasType" sirvam propósitos semelhantes e
   tenham nomes semelhantes, eles são distintos e o último não é o
   tipo do primeiro. A remoção de "TypeAlias" não está planejada
   atualmente, mas os usuários são encorajados a migrar para
   instruções "type".


Formas especiais
~~~~~~~~~~~~~~~~

Eles podem ser usados como tipos em anotações. Todos eles oferecem
suporte a subscrição usando "[]", mas cada um tem uma sintaxe única.

class typing.Union

   Tipo de união;  "Union[X, Y]" é equivalente a "X | Y" e significa X
   ou Y.

   Para definir uma união, use, por exemplo. "Union[int, str]" ou a
   abreviatura "int | str". Usar essa abreviação é recomendado.
   Detalhes:

   * Os argumentos devem ser tipos e deve haver pelo menos um.

   * As uniões de uniões são achatadas, por exemplo:

        Union[Union[int, str], float] == Union[int, str, float]

     Entretanto, isso não se aplica a uniões referenciadas por meio de
     um apelido de tipo, para evitar forçar a avaliação da
     "TypeAliasType" subjacente:

        type A = Union[int, str]
        Union[A, float] != Union[int, str, float]

   * As uniões de um único argumento desaparecem, por exemplo:

        Union[int] == int  # O construtor retorna um int

   * Argumento redundantes são pulados, e.g.:

        Union[int, str, int] == Union[int, str] == int | str

   * Ao comparar uniões, a ordem de argumentos é ignorada. Por
     exemplo:

        Union[int, str] == Union[str, int]

   * Você não pode estender ou instanciar uma "Union"

   * Você não pode escrever "Union[X][Y]".

   Alterado na versão 3.7: Não remova subclasses explícitas de uniões
   em tempo de execução.

   Alterado na versão 3.10: Uniões agora podem ser escritas com "X |
   Y". Veja expressões de união de tipos.

   Alterado na versão 3.14: "types.UnionType" agora é um apelido para
   "Union", e tanto "Union[int, str]" quanto "int | str" criam
   instâncias da mesma classe. Para verificar se um objeto é um
   "Union" em tempo de execução, use "isinstance(obj, Union)". Para
   compatibilidade com versões anteriores do Python, use
   "get_origin(obj) is typing.Union or get_origin(obj) is
   types.UnionType".

typing.Optional

   "Optional[X]" equivale a "X | None" (ou "Union[X, None]").

   Note que isso não é o mesmo conceito de um argumento opcional, que
   possui um valor por padrão. Um argumento opcional com padrão não
   requer o qualificador "Optional" em sua anotação de tipo só por ser
   opcional. Por exemplo:

      def foo(arg: int = 0) -> None:
          ...

   Por outro lado, se um valor explícito de "None" for permitido, o
   uso de "Optional" é apropriado, seja o argumento opcional ou não.
   Por exemplo:

      def foo(arg: Optional[int] = None) -> None:
          ...

   Alterado na versão 3.10: Optional agora pode ser escrito como "X |
   None". Veja expressões de união de tipos.

typing.Concatenate

   Forma especial para anotar funções de ordem superior.

   "Concatenate" can be used in conjunction with Callable and
   "ParamSpec" to annotate a higher-order callable which adds,
   removes, or transforms parameters of another callable.  Usage is in
   the form "Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable]".
   "Concatenate" is valid when used in Callable type hints and when
   instantiating user-defined generic classes with "ParamSpec"
   parameters. The last parameter to "Concatenate" must be a
   "ParamSpec" or ellipsis ("...").

   Por exemplo, para anotar um decorador "with_lock" que oferece uma
   instância de "threading.Lock" para a função decorada, "Concatenate"
   pode ser usado para indicar que "with_lock" espera um chamável cujo
   primeiro argumento tem tipo "Lock", e retorna um chamável com uma
   assinatura de tipos diferente. Neste caso, o "ParamSpec" indica que
   os tipos dos parâmetros do chamável retornado dependem dos tipos
   dos parâmetros do chamável de entrada:

      from collections.abc import Callable
      from threading import Lock
      from typing import Concatenate

      # Use esta trava para se certificar de que
      # uma única thread a executa a qualquer momento.
      my_lock = Lock()

      def with_lock[**P, R](f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
          '''Um decorador com segurança de tipos que oferece uma trava.'''
          def inner(*args: P.args, **kwargs: P.kwargs) -> R:
              # Oferece a trava como primeiro argumento.
              return f(my_lock, *args, **kwargs)
          return inner

      @with_lock
      def sum_threadsafe(lock: Lock, numbers: list[float]) -> float:
          '''Somatório de uma lista de números de modo seguro para threads.'''
          with lock:
              return sum(numbers)

      # We don't need to pass in the lock ourselves thanks to the decorator.
      sum_threadsafe([1.1, 2.2, 3.3])

   Adicionado na versão 3.10.

   Ver também:

     * **PEP 612** -- Variáveis de especificação de parâmetro (a PEP
       que introduz "ParamSpec" e "Concatenate")

     * "ParamSpec"

     * Anotações de objetos chamáveis

typing.Literal

   Forma especial de tipagem para definir "tipos literais".

   "Literal" pode ser usado para indicar aos verificadores de tipo que
   o objeto anotado tem valor equivalente a algum dos literais
   oferecidos.

   Por exemplo:

      def validate_simple(data: Any) -> Literal[True]:  # sempre retorna True
          ...

      type Mode = Literal['r', 'rb', 'w', 'wb']
      def open_helper(file: str, mode: Mode) -> str:
          ...

      open_helper('/some/path', 'r')      # Passa verificação de tipos
      open_helper('/other/path', 'typo')  # Erro em verificação de tipos

   "Literal[...]" não é subclasse. Em tempo de execução, permite-se um
   valor arbitrário como argumento de tipo para "Literal[...]", mas
   verificadores de tipo podem impor restrições. Veja **PEP 586** para
   mais detalhes sobre tipos literais.

   Detalhes adicionais:

   * Os argumentos devem ser valores literais e deve haver pelo menos
     um.

   * Tipos "Literal" aninhados são achatados, por exemplo:

        assert Literal[Literal[1, 2], 3] == Literal[1, 2, 3]

     Entretanto, isso não se aplica a tipos "Literal" referenciadas
     por meio de um apelido de tipo, para evitar forçar a avaliação da
     "TypeAliasType" subjacente:

        type A = Literal[1, 2]
        assert Literal[A, 3] != Literal[1, 2, 3]

   * Argumento redundantes são pulados, e.g.:

        assert Literal[1, 2, 1] == Literal[1, 2]

   * Ao comparar literais, a ordem de argumentos é ignorada. Por
     exemplo:

        assert Literal[1, 2] == Literal[2, 1]

   * Você não pode estender ou instanciar uma "Literal".

   * Você não pode escrever "Literal[X][Y]".

   Adicionado na versão 3.8.

   Alterado na versão 3.9.1: "Literal" agora remove parâmetros
   duplicados. Comparações de igualdade entre objetos "Literal" não
   dependem da ordem. Objetos "Literal" agora levantam uma exceção
   "TypeError" durante comparações de igualdade se um de seus
   parâmetros não for *hasheável*.

typing.ClassVar

   Uma construção especial de tipagem para marcar variáveis de classe.

   Como introduzido na **PEP 526**, uma variável cuja anotação de tipo
   tem um invólucro ClassVar indica que um dado atributo deve ser
   usado como uma variável de classe, e que ele não deve ser definido
   em instâncias dessa classe. Modo de usar:

      class Starship:
          stats: ClassVar[dict[str, int]] = {} # variável de classe
          damage: int = 10                     # variável de instância

   "ClassVar" aceita apenas tipos e não pode ser subscrita
   posteriormente.

   "ClassVar" is not a class itself, and cannot be used with
   "isinstance()" or "issubclass()". "ClassVar" does not change Python
   runtime behavior, but it can be used by static type checkers. For
   example, a type checker might flag the following code as an error:

      enterprise_d = Starship(3000)
      enterprise_d.stats = {} # Erro: atribuindo valor a variável de classe de uma instância
      Starship.stats = {}     # Isso é OK

   Adicionado na versão 3.5.3.

   Alterado na versão 3.13: "ClassVar" agora pode ser aninhada em
   "Final" e vice-versa.

typing.Final

   Uma construção especial de tipagem para indicar nomes finais a
   verificadores de tipos

   Nomes finais não podem ser reatribuídos em qualquer escopo. Nomes
   finais declarados em escopos de classe não podem ser substituídos
   em subclasses.

   Por exemplo:

      MAX_SIZE: Final = 9000
      MAX_SIZE += 1  # Erro reportado pelo verificador de tipos

      class Connection:
          TIMEOUT: Final[int] = 10

      class FastConnector(Connection):
          TIMEOUT = 1  # Error reportado pelo verificador de tipos

   Não há verificação em tempo de execução dessas propriedades. Veja
   **PEP 591** para mais detalhes.

   Adicionado na versão 3.8.

   Alterado na versão 3.13: "Final" agora pode ser aninhada em
   "ClassVar" e vice-versa.

typing.Required

   Uma construção especial de tipagem para marcar uma chave de
   "TypedDict" como necessária.

   Isso é útil principalmente para TypedDicts com "total=False". Veja
   "TypedDict" e **PEP 655** para obter mais detalhes.

   Adicionado na versão 3.11.

typing.NotRequired

   Uma construção especial de tipagem para marcar uma chave de
   "TypedDict" como potencialmente ausente.

   Veja "TypedDict" e **PEP 655** para obter mais detalhes.

   Adicionado na versão 3.11.

typing.ReadOnly

   Uma construção especial de tipagem para marcar um item de um
   "TypedDict" como somente leitura.

   Por exemplo:

      class Movie(TypedDict):
         title: ReadOnly[str]
         year: int

      def mutate_movie(m: Movie) -> None:
         m["year"] = 1999  # allowed
         m["title"] = "The Matrix"  # type checker error

   Não há verificação em tempo de execução para esta propriedade.

   Consulte "TypedDict" e **PEP 705** para obter mais detalhes.

   Adicionado na versão 3.13.

typing.Annotated

   Forma especial de tipagem para adicionar metadados específicos de
   contexto para uma anotação.

   Adiciona metadados "x" a um determinado tipo "T" usando a anotação
   "Annotated[T, x]". Os metadados adicionados usando "Annotated"
   podem ser usados por ferramentas de análise estática ou em tempo de
   execução. Em tempo de execução, os metadados são armazenados em um
   atributo "__metadata__".

   Se uma biblioteca ou ferramenta encontrar uma anotação
   "Annotated[T, x]" e ela não tiver lógica especial para os
   metadados, ela deverá ignorar os metadados e simplesmente tratar a
   anotação como "T". Dessa forma, "Annotated" pode ser útil em
   códigos que desejarem usar a anotação para propósitos fora do
   sistema de tipagem estática do Python.

   Usar "Annotated[T, x]" como um anotação ainda permite a verificação
   estática do tipo de "T", pois os verificadores de tipo simplesmente
   ignoram os metadados em "x". Dessa forma, o "Annotated" difere do
   decorador "@no_type_check", que também pode ser usado para
   adicionar anotações fora do escopo do sistema de tipagem, mas
   desativa completamente a verificação de tipos para uma função ou
   classe.

   A responsabilidade de como interpretar os metadados é da ferramenta
   ou da biblioteca que encontrar uma anotação "Annotated". Uma
   ferramenta ou biblioteca que encontrar um tipo "Annotated" poderá
   examinar os elementos de metadados para determinar se eles são de
   interesse (por exemplo, usando "isinstance()").

   Annotated[<type>, <metadata>]

   Aqui está um exemplo de como você pode usar "Annotated" para
   adicionar metadados a anotações de tipos se estiver fazendo uma
   análise de intervalos:

      @dataclass
      class ValueRange:
          lo: int
          hi: int

      T1 = Annotated[int, ValueRange(-10, 5)]
      T2 = Annotated[T1, ValueRange(-20, 3)]

   O primeiro argumento para "Annotated" deve ser um tipo válido.
   Vários elementos de metadados podem ser fornecidos, pois
   "Annotated" suporta argumentos variádicos. A ordem dos elementos de
   metadados é preservada e importa para verificações de igualdade:

      @dataclass
      class ctype:
           kind: str

      a1 = Annotated[int, ValueRange(3, 10), ctype("char")]
      a2 = Annotated[int, ctype("char"), ValueRange(3, 10)]

      assert a1 != a2  # a ordem importa

   Cabe à ferramenta que consome as anotações decidir se o cliente tem
   permissão de adicionar vários elementos de metadados a uma anotação
   e como mesclar essas anotações.

   Os tipos "Annotated" aninhados são achatados. A ordem dos elementos
   de metadados começa com a anotação mais interna:

      assert Annotated[Annotated[int, ValueRange(3, 10)], ctype("char")] == Annotated[
          int, ValueRange(3, 10), ctype("char")
      ]

   Entretanto, isso não se aplica a tipos "Annotated" referenciadas
   por meio de um apelido de tipo, para evitar forçar a avaliação da
   "TypeAliasType" subjacente:

      type From3To10[T] = Annotated[T, ValueRange(3, 10)]
      assert Annotated[From3To10[int], ctype("char")] != Annotated[
         int, ValueRange(3, 10), ctype("char")
      ]

   Elementos duplicados de metadata não são removidos:

      assert Annotated[int, ValueRange(3, 10)] != Annotated[
          int, ValueRange(3, 10), ValueRange(3, 10)
      ]

   "Annotated" pode ser usado com apelidos aninhados e apelidos
   genéricos:

         @dataclass
         class MaxLen:
             value: int

         type Vec[T] = Annotated[list[tuple[T, T]], MaxLen(10)]

         # Quando usado em uma anotação de tipo, um verificador de tipos tratará "V" da mesma forma que
         # ``Annotated[list[tuple[int, int]], MaxLen(10)]``:
         type V = Vec[int]

   "Annotated" não pode ser usado com um "TypeVarTuple" desempacotado:

      type Variadic[*Ts] = Annotated[*Ts, Ann1] = Annotated[T1, T2, T3, ..., Ann1]  # NÃO válido

   onde "T1", "T2", ... são "TypeVars". Isso é inválido, pois somente
   um tipo deve ser passado para Annotated.

   Por padrão, "get_type_hints()" retira os metadados de anotações.
   Passe "include_extras=True" para preservar os metadados:

         >>> from typing import Annotated, get_type_hints
         >>> def func(x: Annotated[int, "metadata"]) -> None: pass
         ...
         >>> get_type_hints(func)
         {'x': <class 'int'>, 'return': <class 'NoneType'>}
         >>> get_type_hints(func, include_extras=True)
         {'x': typing.Annotated[int, 'metadata'], 'return': <class 'NoneType'>}

   Em tempo de execução, os metadados associados a um tipo "Annotated"
   podem ser recuperados por meio do atributo "__metadata__":

         >>> from typing import Annotated
         >>> X = Annotated[int, "very", "important", "metadata"]
         >>> X
         typing.Annotated[int, 'very', 'important', 'metadata']
         >>> X.__metadata__
         ('very', 'important', 'metadata')

   Se você quiser recuperar o tipo original envolvido por "Annotated",
   use o atributo "__origin__":

         >>> from typing import Annotated, get_origin
         >>> Password = Annotated[str, "secret"]
         >>> Password.__origin__
         <class 'str'>

   Note que usar "get_origin()" retornará o próprio "Annotated":

         >>> get_origin(Password)
         typing.Annotated

   Ver também:

     **PEP 593** - Anotações flexíveis para funções e variáveis
        A PEP que introduz "Annotated" à biblioteca padrão.

   Adicionado na versão 3.9.

typing.TypeForm

   A special form representing the value that results from evaluating
   a type expression.

   This value encodes the information supplied in the type expression,
   and it represents the type described by that type expression.

   When used in a type expression, "TypeForm" describes a set of type
   form objects. It accepts a single type argument, which must be a
   valid type expression. "TypeForm[T]" describes the set of all type
   form objects that represent the type "T" or types assignable to
   "T".

   "TypeForm(obj)" simply returns "obj" unchanged. This is useful for
   explicitly marking a value as a type form for static type checkers.

   Exemplo:

      from typing import Any, TypeForm

      def cast[T](typ: TypeForm[T], value: Any) -> T: ...

      reveal_type(cast(int, "x"))  # Revealed type is "int"

   See **PEP 747** for details.

   Adicionado na versão 3.15.

typing.TypeIs

   Uma construção especial de tipagem para marcar funções de predicado
   de tipo definidas pelo usuário.

   "TypeIs" pode ser usado para anotar o tipo de retorno de uma função
   de predicado de tipo definida pelo usuário. "TypeIs" aceita apenas
   um único argumento de tipo. Em tempo de execução, funções marcadas
   dessa forma devem retornar um booleano e receber, no mínimo, um
   argumento posicional.

   "TypeIs" visa beneficiar *estreitamento de tipo* -- uma técnica
   usada por verificador de tipo estático para determinar um tipo mais
   preciso de expressão dentro do fluxo de código de um programa.
   Normalmente, o estreitamento de tipo é feito por meio da análise do
   fluxo de código condicional e da aplicação do estreitamento a um
   bloquear código.  A condicional expressão aqui é às vezes chamada
   de "predicado de tipo":

      def is_str(val: str | float):
          # predicado de tipos "isinstance"
          if isinstance(val, str):
              # Tipo de ``val`` é restrito a ``str``
              ...
          else:
              # Senão, tipo de ``val`` é restrito a ``float``.
              ...

   Às vezes, seria conveniente usar uma função booleana definida pelo
   usuário como um predicado de tipo. Essa função deveria usar
   "TypeIs[...]" ou "TypeGuard" como seu tipo de retorno para alertar
   o verificador de tipo estático sobre essa intenção. "TypeIs"
   geralmente tem um comportamento mais intuitivo do que "TypeGuard",
   mas não pode ser usado quando os tipos de entrada e saída são
   incompatíveis (por exemplo, de "list[object]" para "list[int]") ou
   quando a função não retorna "True" para todas as instâncias do tipo
   restrito.

   Usar "-> TypeIs[NarrowedType]" informa ao verificador de tipo
   estático que, para uma determinada função:

   1. O valor de retorno é um booleano.

   2. Se o valor de retorno for "True", o tipo de seu argumento será a
      interseção entre o tipo original do argumento e o
      "NarrowedType".

   3. Se o valor de retorno for "False", o tipo de seu argumento será
      restrito para excluir "NarrowedType".

   Por exemplo:

      from typing import assert_type, final, TypeIs

      class Parent: pass
      class Child(Parent): pass
      @final
      class Unrelated: pass

      def is_parent(val: object) -> TypeIs[Parent]:
          return isinstance(val, Parent)

      def run(arg: Child | Unrelated):
          if is_parent(arg):
              # Tipo de ``arg`` é restrito à interseção
              # de ``Parent`` e ``Child``, o que equivale a
              # ``Child``.
              assert_type(arg, Child)
          else:
              # Tipo de ``arg`` é restrito para excluir ``Parent``,
              # então sobrou o tipo ``Unrelated``.
              assert_type(arg, Unrelated)

   O tipo dentro de "TypeIs" deve ser consistente com o tipo do
   argumento da função; caso contrário, o verificador de tipo estático
   levantará um erro. Uma função "TypeIs" escrita incorretamente pode
   ocasionar um comportamento insensato pelo sistema de tipos; é de
   responsabilidade do usuário escrever tais funções de forma segura
   para tipos.

   Se uma função "TypeIs" for um método de classe ou instância, então
   o tipo em "TypeIs" mapeia para o tipo do segundo parâmetro (depois
   de "cls" ou "self").

   Em resumo, a forma "def foo(arg: TypeA) -> TypeIs[TypeB]: ...",
   significa que se "foo(arg)" retorna "True", então "arg" é um
   instância de "TypeB", e se retorna "False", não é um instância de
   "TypeB".

   "TypeIs" também funciona com variáveis de tipo. Para mais
   informações, consulte a **PEP 742** (Restringindo tipos com
   "TypeIs").

   Adicionado na versão 3.13.

typing.TypeGuard

   Uma construção especial de tipagem para marcar funções de predicado
   de tipo definidas pelo usuário.

   Funções de predicados de tipo são funções definidas pelo usuário
   que retornam se seu argumento é uma instância de um tipo
   específico. O "TypeGuard" funciona como "TypeIs", mas tem efeitos
   sutilmente diferentes sobre o comportamento da verificação de tipos
   (veja abaixo).

   Usar "-> TypeGuard" informa ao verificador de tipo estático que,
   para uma determinada função:

   1. O valor de retorno é um booleano.

   2. Se o valor de retorno for "True", o tipo de seu argumento é o
      tipo dentro de "TypeGuard".

   "TypeGuard" também funciona com tipos variáveis. Consulte a **PEP
   647** para obter mais detalhes.

   Por exemplo:

      def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
          '''Determina se todos os objetos na lista são strings'''
          return all(isinstance(x, str) for x in val)

      def func1(val: list[object]):
          if is_str_list(val):
              # Tipo de ``val`` é restrito a ``list[str]``.
              print(" ".join(val))
          else:
              # Tipo de ``val`` continua sendo ``list[object]``.
              print("Not a list of strings!")

   "TypeIs" e "TypeGuard" diferem das seguintes maneiras:

   * "TypeIs" exige que o tipo restrito seja um subtipo do tipo de
     entrada, enquanto o "TypeGuard", não. O motivo principal é
     permitir coisas como restringir "list[object]" a "list[str]",
     embora este não seja um subtipo daquele, já que "list" é
     invariante.

   * Quando uma função "TypeGuard" retorna "True", os verificadores de
     tipo restringem o tipo da variável exatamente ao tipo
     "TypeGuard". Quando uma função "TypeIs" retorna "True", os
     verificadores de tipo podem inferir um tipo mais preciso
     combinando o tipo previamente conhecido da variável com o tipo
     "TypeIs". (Tecnicamente, isso é conhecido como um tipo de
     interseção).

   * Quando uma função "TypeGuard" retorna "False", os verificadores
     de tipo não podem restringir o tipo da variável. Quando uma
     função "TypeIs" retorna "False", os verificadores de tipo podem
     restringir o tipo da variável para excluir o tipo "TypeIs".

   Adicionado na versão 3.10.

typing.Unpack

   Operador de tipagem para marcar conceitualmente um objeto como
   tendo sido desempacotado.

   Por exemplo, usar o operador de desempacotamento "*" em uma tupla
   de tipos variáveis equivale a usar o "Unpack" para marcar a tupla
   de tipos variáveis como tendo sido desempacotada:

      Ts = TypeVarTuple('Ts')
      tup: tuple[*Ts]
      # Efetivamente faz:
      tup: tuple[Unpack[Ts]]

   Na verdade, "Unpack" pode ser usado de forma intercambiável com "*"
   no contexto dos tipos "typing.TypeVarTuple" e "builtins.tuple".
   Você pode ver "Unpack" sendo usado explicitamente em versões mais
   antigas do Python, onde "*" não podia ser usado em certos lugares:

      # Em versões mais antigas do Python, TypeVarTuple e Unpack
      # estão localizados no pacote de backports `typing_extensions`.
      from typing_extensions import TypeVarTuple, Unpack

      Ts = TypeVarTuple('Ts')
      tup: tuple[*Ts]         # Erro de sintaxe no Python <= 3.10!
      tup: tuple[Unpack[Ts]]  # Semanticamente equivalente e compatível com versões anteriores

   "Unpack" também pode ser usado com "typing.TypedDict" para a
   tipagem de "**kwargs" em uma assinatura de função:

      from typing import TypedDict, Unpack

      class Movie(TypedDict):
          name: str
          year: int

      # Esta função espera dois argumentos nomeados: `name` de tipo `str`
      # e `year` de tipo `int`.
      def foo(**kwargs: Unpack[Movie]): ...

   Consulte **PEP 692** para obter mais detalhes sobre como usar
   "Unpack" para tipagem de "**kwargs".

   Adicionado na versão 3.11.


Criando tipos genéricos e apelidos de tipo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As classes a seguir não devem ser usadas diretamente como anotações.
propósito O objetivo delas é construir bloquear para criar genérico e
digitar apelido.

Esses objetos podem ser criados por meio de sintaxe especial (listas
de parâmetros de tipo e a instrução "type"). Para compatibilidade com
Python 3.11 e versões anteriores, eles também podem ser criados sem a
sintaxe dedicada, como documentado abaixo.

class typing.Generic

   Classe base abstrata para tipos genéricos

   Normalmente, um tipo genérico é declarado adicionando-se uma lista
   de parâmetros de tipo após o nome da classe:

      class Mapping[KT, VT]:
          def __getitem__(self, key: KT) -> VT:
              ...
              # Etc.

   Essa classe herda implicitamente de "Generic". A semântica em tempo
   de execução dessa sintaxe é discutida na Referência da Linguagem.

   Esta classe pode ser utilizada como segue:

      def lookup_name[X, Y](mapping: Mapping[X, Y], key: X, default: Y) -> Y:
          try:
              return mapping[key]
          except KeyError:
              return default

   Aqui os colchetes depois no nome da função indica uma função
   genérica.

   Para manter retrocompatibilidade, as classes genéricas também podem
   ser declaradas herdando explicitamente de "Generic". Nesse caso, os
   parâmetros de tipo devem ser declarados separadamente:

      KT = TypeVar('KT')
      VT = TypeVar('VT')

      class Mapping(Generic[KT, VT]):
          def __getitem__(self, key: KT) -> VT:
              ...
              # Etc.

class typing.TypeVar(name, *constraints, bound=None, covariant=False, contravariant=False, infer_variance=False, default=typing.NoDefault)

   Tipo variável.

   A maneira preferida de construir um tipo variável é por meio da
   sintaxe dedicada para funções genéricas, classes genéricas e
   apelidos de tipo genérico:

      class Sequence[T]:  # T é um TypeVar
          ...

   Essa sintaxe também pode ser usada para criar tipos variáveis
   delimitados e tipos variáveis restritos:

      class StrSequence[S: str]:  # S é a TypeVar com como limite superior em `str`;
          ...                     # podemos dizer que S é "delimitada por `str`"


      class StrOrBytesSequence[A: (str, bytes)]:  # A é uma TypeVar restrita a str ou bytes
          ...

   No entanto, se desejado, tipos variáveis reutilizáveis também podem
   ser construídas manualmente, como:

      T = TypeVar('T') # Pode ser qualquer coisa
      S = TypeVar('S', bound=str) # Pode ser qualquer subtipo de str
      A = TypeVar('A', str, bytes) # Deve ser exatamente str ou bytes

   Tipos variáveis existem principalmente para o benefício de
   verificadores de tipo estático. Eles servem como parâmetros para
   tipos genéricos, bem como para definições de função genérica  e
   apelidos de tipo. Consulte "Generic" para obter mais informações
   sobre genérico. Funções genéricas funcionam da seguinte forma:

      def repeat[T](x: T, n: int) -> Sequence[T]:
          """Retorna uma lista contendo n referências para x."""
          return [x]*n


      def print_capitalized[S: str](x: S) -> S:
          """Exibe x capitalizado, e retorna x."""
          print(x.capitalize())
          return x


      def concatenate[A: (str, bytes)](x: A, y: A) -> A:
          """Concatena dois objetos string ou bytes."""
          return x + y

   Observe que tipos variáveis podem ser *delimitados*, *restritos*,
   nenhum dos dois, mas não podem ser *ambos*.

   A variância de tipos variáveis é inferida pelos verificadores de
   tipo quando eles são criados por meio do sintaxe de parâmetro de
   tipo ou quando "infer_variance=True" é passado. Os tipos variáveis
   criados manualmente podem ser explicitamente marcados como
   covariante ou contravariantes ao passar "covariant=True" ou
   "contravariant=True". Por padrão, os tipos variáveis criados
   manualmente são invariante. Consulte **PEP 484** e **PEP 695** para
   obter mais detalhes.

   Tipos variáveis delimitados e tipos variáveis restritos têm
   semânticas diferentes de várias formas importantes. Usar um tipo
   variável *delimitado* significa que a "TypeVar" será resolvido
   usando o tipo mais específico possível:

      x = print_capitalized('a string')
      reveal_type(x)  # tipo revelado é str

      class StringSubclass(str):
          pass

      y = print_capitalized(StringSubclass('another string'))
      reveal_type(y)  # tipo revelado é StringSubclass

      z = print_capitalized(45)  # erro: int não é subtipo de str

   O limite superior de um tipo variável pode ser um tipo concreto, um
   tipo abstrato (classe base abstrata ou protocolo) ou até mesmo uma
   união de tipos:

      # Pode ser qualquer coisa com um método __abs__
      def print_abs[T: SupportsAbs](arg: T) -> None:
          print("Absolute value:", abs(arg))

      U = TypeVar('U', bound=str|bytes)  # Pode ser qualquer subtipo com a união str | bytes
      V = TypeVar('V', bound=SupportsAbs)  # Pode ser qualquer coisa com um método __abs__

   Porém, usar um tipo variável *restrito* significa que a "TypeVar"
   só poderá ser resolvida como sendo exatamente uma das restrições
   dadas:

      a = concatenate('one', 'two')
      reveal_type(a) # o tipo revelado é str

      b = concatenate(StringSubclass('one'), StringSubclass('two'))
      reveal_type(b) # o tipo revelado é str, apesar de StringSubclass ter sido passado

      c = concatenate('one', b'two') # erro: tipo variável 'A' pode ser str ou bytes em uma chamada de função, mas não ambos

   Em tempo de execução, "isinstance(x, T)" levantará "TypeError".

   __name__

      O nome do tipo variável.

   __covariant__

      Se o tipo variável foi explicitamente marcado como covariante.

   __contravariant__

      Se o tipo variável foi explicitamente marcado como
      contravariante.

   __infer_variance__

      Se a variância de tipo variável deve ser inferida por
      verificadores de tipo.

      Adicionado na versão 3.12.

   __bound__

      A limite superior do tipo variável, se houver.

      Alterado na versão 3.12: Para tipos variáveis criado por meio da
      sintaxe de parâmetro de tipo , a limite é avaliado somente
      quando o atributo é acessado, não quando o tipo variável é
      criado (consulte Avaliação preguiçosa).

   evaluate_bound()

      Uma *função de avaliação* correspondente ao atributo
      "__bound__". Quando chamado diretamente, este método oferece
      suporte apenas ao formato "VALUE", que equivale a acessar o
      atributo "__bound__" diretamente, mas o objeto do método pode
      ser passado para "annotationlib.call_evaluate_function()" para
      avaliar o valor em um formato diferente.

      Adicionado na versão 3.14.

   __constraints__

      Um tupla contendo as restrições do tipo variável, se houver.

      Alterado na versão 3.12: Para tipos variáveis criado por meio da
      sintaxe de parâmetro de tipo , a restrição é avaliada somente
      quando o atributo é acessado, não quando o tipo variável é
      criado (consulte Avaliação preguiçosa).

   evaluate_constraints()

      Uma *função de avaliação* correspondente ao atributo
      "__constraints__". Quando chamado diretamente, este método
      oferece suporte apenas ao formato "VALUE", que equivale a
      acessar o atributo "__constraints__" diretamente, mas o objeto
      do método pode ser passado para
      "annotationlib.call_evaluate_function()" para avaliar o valor em
      um formato diferente.

      Adicionado na versão 3.14.

   __default__

      O padrão valor do tipo variável, ou "typing.NoDefault" se ele
      não tiver padrão.

      Adicionado na versão 3.13.

   evaluate_default()

      Uma *função de avaliação* correspondente ao atributo
      "__default__". Quando chamado diretamente, este método oferece
      suporte apenas ao formato "VALUE", que equivale a acessar o
      atributo "__default__" diretamente, mas o objeto do método pode
      ser passado para "annotationlib.call_evaluate_function()" para
      avaliar o valor em um formato diferente.

      Adicionado na versão 3.14.

   has_default()

      Retorna se o tipo variável tem ou não um valor padrão. Isso
      equivale a verificar se "__default__" não é o singleton
      "typing.NoDefault", exceto por não forçar a avaliação
      instantânea do valor padrão que é avaliado preguiçosamente.

      Adicionado na versão 3.13.

   Alterado na versão 3.12: Tipos variáveis agora podem ser declarados
   usando a sintaxe de parâmetro de tipo introduzida por **PEP 695**.
   O parâmetro "infer_variance" foi adicionado.

   Alterado na versão 3.13: Adiciona suporte a valores padrão.

class typing.TypeVarTuple(name, *, bound=None, covariant=False, contravariant=False, infer_variance=False, default=typing.NoDefault)

   Tupla de tipo variável. Uma forma especializada de tipo variável
   que permite genéricos *variádicos*.

   Tuplas de tipo variável podem ser declarada em listas de parâmetros
   de tipo usando um único asterisco ("*") antes do nome:

      def move_first_element_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
          return (*tup[1:], tup[0])

   Ou invocando o construtor "TypeVarTuple" explicitamente:

      T = TypeVar("T")
      Ts = TypeVarTuple("Ts")

      def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
          return (*tup[1:], tup[0])

   Um tipo variável normal permite a parametrização com um único tipo.
   Uma tupla de tipos variáveis, por outro lado, permite a
   parametrização com um número *arbitrário* de tipos, agindo como um
   número *arbitrário* de tipos variáveis envolvidos em um tupla. Por
   exemplo:

      # T é limitado a int, Ts é limitado a ()
      # Valor retornado é (1,), que tem tipo tuple[int]
      move_first_element_to_last(tup=(1,))

      # T é limitado a int, Ts é limitado a (str,)
      # Valor retornado é ('spam', 1), que tem tipo tuple[str, int]
      move_first_element_to_last(tup=(1, 'spam'))

      # T é limitado a int, Ts é limitado a (str, float)
      # Valor retornado é ('spam', 3.0, 1), que tem tipo tuple[str, float, int]
      move_first_element_to_last(tup=(1, 'spam', 3.0))

      # Isso é um erro para o verificador de tipos (e falha em tempo de execução)
      # pois tuple[()] não é compatível com tuple[T, *Ts]
      # (pelo menos um elemento é necessário)
      move_first_element_to_last(tup=())

   Observe o uso do operador de desempacotamento "*" em "tuple[T,
   *Ts]". Conceitualmente, você pode interpretar "Ts" como uma tupla
   de tipos variáveis "(T1, T2, ...)" . Então o tipo "tuple[T, *Ts]"
   se tornaria "tuple[T, *(T1, T2, ...)]", que equivale a "tuple[T,
   T1, T2, ...]". (Note que, em versões mais antigas de Python, você
   pode encontrar isso escrito com "Unpack" em vez de "Unpack[Ts]".)

   Tuplas de tipos variáveis devem *sempre* ser desempacotadas. Isso
   ajuda a distinguir entre tuplas de tipos variáveis e tipos
   variáveis normais:

      x: Ts          # Inválido
      x: tuple[Ts]   # Inválido
      x: tuple[*Ts]  # O jeito correto

   As tuplas de tipos variáveis podem ser usadas no mesmo contexto que
   tipos variáveis normais. Por exemplo, em argumentos, tipos de
   retorno e definições de classes:

      class Array[*Shape]:
          def __getitem__(self, key: tuple[*Shape]) -> float: ...
          def __abs__(self) -> "Array[*Shape]": ...
          def get_shape(self) -> tuple[*Shape]: ...

   As tuplas de tipos variáveis podem ser combinadas com tipos
   variáveis normais:

      class Array[DType, *Shape]:  # Tudo certo aqui
          pass

      class Array2[*Shape, DType]:  # Tudo certo aqui também
          pass

      class Height: ...
      class Width: ...

      float_array_1d: Array[float, Height] = Array()     # Totalmente certo
      int_array_2d: Array[int, Height, Width] = Array()  # Sim, certo também

   No entanto, observe que no máximo uma tupla de tipos variáveis pode
   aparecer em uma única lista de argumentos de tipo ou parâmetros de
   tipo:

      x: tuple[*Ts, *Ts]             # Inválido
      class Array[*Shape, *Shape]:  # Inválido
          pass

   Por fim, uma tupla de tipos variáveis desempacotada pode ser usada
   como anotação de tipo de "*args":

      def call_soon[*Ts](
          callback: Callable[[*Ts], None],
          *args: *Ts
      ) -> None:
          ...
          callback(*args)

   Ao contrário do que acontece com anotações não desempacotadas de
   "*args" - por exemplo, "*args: int", que especificaria que *todos*
   os argumentos são "int" -, "*args: *Ts" permite referenciar os
   tipos de cada argumento em "*args" *individualmente*. Isso nos
   permite garantir que os tipos em "*args" passados para "call_soon"
   correspondem aos tipos dos argumentos (posicionais) de "callback".

   Consulte a **PEP 646** para mais detalhes sobre tuplas de tipos
   variáveis.

   __name__

      O nome da tupla de tipos variáveis.

   __covariant__

      Whether the type variable tuple has been explicitly marked as
      covariant.

      Adicionado na versão 3.15.

   __contravariant__

      Whether the type variable tuple has been explicitly marked as
      contravariant.

      Adicionado na versão 3.15.

   __infer_variance__

      Whether the type variable tuple's variance should be inferred by
      type checkers.

      Adicionado na versão 3.15.

   __default__

      O valor padrão da tupla de tipos variáveis, ou
      "typing.NoDefault" se não existir padrão.

      Adicionado na versão 3.13.

   evaluate_default()

      Uma *função de avaliação* correspondente ao atributo
      "__default__". Quando chamado diretamente, este método oferece
      suporte apenas ao formato "VALUE", que equivale a acessar o
      atributo "__default__" diretamente, mas o objeto do método pode
      ser passado para "annotationlib.call_evaluate_function()" para
      avaliar o valor em um formato diferente.

      Adicionado na versão 3.14.

   has_default()

      Retorna se a tupla de tipos variáveis tem ou não um valor
      padrão. Isso equivale a verificar se "__default__" não é o
      singleton "typing.NoDefault", exceto por não forçar a avaliação
      instantânea do valor padrão que é avaliado preguiçosamente.

      Adicionado na versão 3.13.

   Type variable tuples created with "covariant=True" or
   "contravariant=True" can be used to declare covariant or
   contravariant generic types.  The "bound" argument is also
   accepted, similar to "TypeVar", but its actual semantics are yet to
   be decided.

   Adicionado na versão 3.11.

   Alterado na versão 3.12: Tuplas de tipos variáveis agora podem ser
   declaradas usando a sintaxe de parâmetros de tipo introduzido pela
   **PEP 695**.

   Alterado na versão 3.13: Adiciona suporte a valores padrão.

   Alterado na versão 3.15: Added support for the "bound",
   "covariant", "contravariant", and "infer_variance" parameters.

class typing.ParamSpec(name, *, bound=None, covariant=False, contravariant=False, infer_variance=False, default=typing.NoDefault)

   Variável de especificação de parâmetro. Uma versão especializada de
   tipos variáveis.

   Em listas de parâmetros de tipo as especificações de parâmetros
   podem ser declaradas com dois asteriscos ("**"):

      type IntFunc[**P] = Callable[P, int]

   Para compatibilidade com Python 3.11 e versões anteriores, os
   objetos "ParamSpec" também podem ser criados da seguinte forma:

      P = ParamSpec('P')

   Variáveis de especificação de parâmetro existem principalmente para
   o benefício de verificadores de tipo estático. São usadas para
   encaminhar os tipos de parâmetros de um chamável para outro
   chamável -- um padrão comumente encontrado em funções e decoradores
   de ordem superior. Só são válidas quando usados em "Concatenate",
   ou como o primeiro argumento para "Callable", ou como parâmetro
   para genéricos definidos pelo usuário. Consulte "Generic" para
   obter mais informações sobre tipos genéricos.

   Por exemplo, para adicionar um registro básico de eventos a uma
   função, é possível criar um decorador "add_logging" para registrar
   chamadas de função. A variável de especificação de parâmetro
   informa ao verificador de tipos que o chamável passado para o
   decorador e o novo chamável retornado por ele têm parâmetros de
   tipo interdependentes:

      from collections.abc import Callable
      import logging

      def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
          '''Um decorador com segurança de tipos que acrescenta registros de eventos (logs) a uma função.'''
          def inner(*args: P.args, **kwargs: P.kwargs) -> T:
              logging.info(f'{f.__name__} was called')
              return f(*args, **kwargs)
          return inner

      @add_logging
      def add_two(x: float, y: float) -> float:
          '''Soma dois números.'''
          return x + y

   Sem o "ParamSpec", a maneira mais simples de anotar isso
   anteriormente era usar um "TypeVar" com o limite superior
   "Callable[..., Any]".  No entanto, isso causa dois problemas:

   1. O verificador de tipos não consegue verificar a função "inner",
      porque "*args" e "**kwargs" precisam ter tipo "Any".

   2. "cast()" pode ser exigida no corpo do decorador "add_logging" ao
      retornar a função "inner", ou o verificador de tipo estático
      deverá ser instruído a ignorar o "return inner".

   args

   kwargs

      Como "ParamSpec" captura tanto parâmetros posicionais quanto
      parâmetros nomeados, "P.args" e "P.kwargs" podem ser usados para
      dividir um "ParamSpec" em seus componentes. "P.args" representa
      a tupla de parâmetros posicionais em uma determinada chamada e
      só deve ser usada para anotar "*args". "P.kwargs" representa o
      mapeamento de parâmetros nomeados para seus valores em uma
      determinada chamada, e só deve ser usado para anotar "**kwargs".
      Ambos os atributos exigem que o parâmetro anotado esteja em
      escopo. Em tempo de execução, "P.args" e "P.kwargs" são
      instâncias, respectivamente, de "ParamSpecArgs" e
      "ParamSpecKwargs".

   __name__

      O nome da especificação de parâmetros.

   __covariant__

      Whether the parameter specification has been explicitly marked
      as covariant.

   __contravariant__

      Whether the parameter specification has been explicitly marked
      as contravariant.

   __infer_variance__

      Whether the parameter specification's variance should be
      inferred by type checkers.

      Adicionado na versão 3.12.

   __default__

      O valor padrão da especificação de parâmetro, ou
      "typing.NoDefault" se não tiver padrão.

      Adicionado na versão 3.13.

   evaluate_default()

      Uma *função de avaliação* correspondente ao atributo
      "__default__". Quando chamado diretamente, este método oferece
      suporte apenas ao formato "VALUE", que equivale a acessar o
      atributo "__default__" diretamente, mas o objeto do método pode
      ser passado para "annotationlib.call_evaluate_function()" para
      avaliar o valor em um formato diferente.

      Adicionado na versão 3.14.

   has_default()

      Retorna se a especificação de parâmetros tem ou não um  valor
      padrão. Isso equivale a verificar se "__default__" não é o
      singleton "typing.NoDefault", exceto por não forçar a avaliação
      instantânea do valor padrão que é avaliado preguiçosamente.

      Adicionado na versão 3.13.

   Variáveis de especificação de parâmetros criadas com
   "covariant=True" ou "contravariant=True" podem ser usadas para
   declarar tipos genéricos covariantes ou contravariantes. O
   argumento "bound" também é aceito, semelhante ao "TypeVar". Porém,
   a semântica real dessas palavras reservadas ainda não foi decidida.

   Adicionado na versão 3.10.

   Alterado na versão 3.12: Especificações de parâmetros agora podem
   ser declaradas usando a sintaxe de parâmetros de tipo introduzido
   pela **PEP 695**.

   Alterado na versão 3.13: Adiciona suporte a valores padrão.

   Nota:

     Somente variáveis de especificação de parâmetro definidas em
     escopo global podem ser serializadas com pickle.

   Ver também:

     * **PEP 612** -- Variáveis de especificação de parâmetro (a PEP
       que introduz "ParamSpec" e "Concatenate")

     * "Concatenate"

     * Anotações de objetos chamáveis

class typing.ParamSpecArgs
class typing.ParamSpecKwargs

   Tipos dos argumentos e dos argumentos nomeados de um "ParamSpec". O
   atributo "P.args" de um "ParamSpec" é uma instância de
   "ParamSpecArgs", e o atributo "P.kwargs" é uma instância de
   "ParamSpecKwargs". São destinados à introspecção em tempo de
   execução, e não têm nenhum significado especial para o verificador
   de tipo estático.

   Chamar "get_origin()" em qualquer um desses objetos retornará o
   "ParamSpec" original:

      >>> from typing import ParamSpec, get_origin
      >>> P = ParamSpec("P")
      >>> get_origin(P.args) is P
      True
      >>> get_origin(P.kwargs) is P
      True

   Adicionado na versão 3.10.

class typing.TypeAliasType(name, value, *, type_params=(), qualname=None)

   O tipo de apelidos de tipo criados pela instrução "type".

   Exemplo:

      >>> type Alias = int
      >>> type(Alias)
      <class 'typing.TypeAliasType'>

   Adicionado na versão 3.12.

   __name__

      O nome do apelido de tipo:

         >>> type Alias = int
         >>> Alias.__name__
         'Alias'

   __qualname__

      The *qualified name* of the type alias:

         >>> class Class:
         ...     type Alias = int
         ...
         >>> Class.Alias.__qualname__
         'Class.Alias'

      Adicionado na versão 3.15.

   __module__

      O nome do módulo no qual o apelido de tipo foi definido:

         >>> type Alias = int
         >>> Alias.__module__
         '__main__'

      This attribute is writable.

      Alterado na versão 3.15: The attribute is now writable.

   __type_params__

      Os parâmetros de tipo do apelido de tipo, ou uma tupla vazia se
      o apelido não for genérico:

         >>> type ListOrSet[T] = list[T] | set[T]
         >>> ListOrSet.__type_params__
         (T,)
         >>> type NotGeneric = int
         >>> NotGeneric.__type_params__
         ()

   __value__

      O valor do apelido de tipo. Isso é uma avaliação preguiçosa,
      portanto, os nomes usados na definição do apelido não são
      resolvidos até que o atributo "__value__" seja acessado:

         >>> type Mutually = Recursive
         >>> type Recursive = Mutually
         >>> Mutually
         Mutually
         >>> Recursive
         Recursive
         >>> Mutually.__value__
         Recursive
         >>> Recursive.__value__
         Mutually

   evaluate_value()

      Uma *função de avaliação* correspondente ao atributo
      "__value__". Quando chamado diretamente, este método oferece
      suporte apenas ao formato "VALUE", que equivale a acessar o
      atributo "__value__" diretamente, mas o objeto do método pode
      ser passado para "annotationlib.call_evaluate_function()" para
      avaliar o valor em um formato diferente.

         >>> type Alias = undefined
         >>> Alias.__value__
         Traceback (most recent call last):
         ...
         NameError: name 'undefined' is not defined
         >>> from annotationlib import Format, call_evaluate_function
         >>> Alias.evaluate_value(Format.VALUE)
         Traceback (most recent call last):
         ...
         NameError: name 'undefined' is not defined
         >>> call_evaluate_function(Alias.evaluate_value, Format.FORWARDREF)
         ForwardRef('undefined')

      Adicionado na versão 3.14.

   -[ Descompactando ]-

   Apelidos de tipo oferecem suporte a desempacotamento em estrela
   usando a sintaxe "*Alias". Isso equivale a usar "Unpack[Alias]"
   diretamente:

      >>> type Alias = tuple[int, str]
      >>> type Unpacked = tuple[bool, *Alias]
      >>> Unpacked.__value__
      tuple[bool, typing.Unpack[Alias]]

   Adicionado na versão 3.14.


Outras diretivas especiais
~~~~~~~~~~~~~~~~~~~~~~~~~~

Essas funções e classes não devem ser usadas diretamente como
anotações. O objetivo é que sejam blocos de construção para criar e
declarar tipos.

class typing.NamedTuple

   Versão tipada de "collections.namedtuple()".

   Uso:

      class Employee(NamedTuple):
          name: str
          id: int

   Isso equivale a:

      Employee = collections.namedtuple('Employee', ['name', 'id'])

   Para dar um valor padrão a um campo, você pode atribuir um valor a
   ele no corpo da classe:

      class Employee(NamedTuple):
          name: str
          id: int = 3

      employee = Employee('Guido')
      assert employee.id == 3

   Campos com valor padrão devem vir depois de quaisquer campos sem
   valor padrão.

   The types for each field name can be retrieved by calling
   "annotationlib.get_annotations()" on the resulting class. (The
   field names are in the "_fields" attribute and the default values
   are in the "_field_defaults" attribute, both of which are part of
   the "namedtuple()" API.)

   Subclasses de "NamedTuple" também podem ter strings de documentação
   e métodos:

      class Employee(NamedTuple):
          """Representa um funcionário."""
          name: str
          id: int = 3

          def __repr__(self) -> str:
              return f'<Employee {self.name}, id={self.id}>'

   Subclasses de "NamedTuple" podem ser genéricas:

      class Group[T](NamedTuple):
          key: T
          group: list[T]

   Uso retrocompatível:

      # Para criar uma NamedTuple genérica em Python 3.11
      T = TypeVar("T")

      class Group(NamedTuple, Generic[T]):
          key: T
          group: list[T]

      # Também há suporte para a sintaxe funcional
      Employee = NamedTuple('Employee', [('name', str), ('id', int)])

   Alterado na versão 3.6: Adiciona suporte à sintaxe de anotação de
   variáveis da **PEP 526**.

   Alterado na versão 3.6.1: Adiciona suporte a valores padrões,
   métodos, e docstrings.

   Alterado na versão 3.8: Os atributos "_field_types" e
   "__annotations__" agora são dicionários regulares em vez de
   instâncias de "OrderedDict".

   Alterado na versão 3.9: Remove o atributo "_field_types" em favor
   do atributo mais padronizado "__annotations__" que tem as mesmas
   informações.

   Alterado na versão 3.9: "NamedTuple" is now a function rather than
   a class. It can still be used as a class base, as described above.

   Alterado na versão 3.11: Adiciona suporte a tuplas nomeadas
   genéricas.

   Alterado na versão 3.14: O uso de "super()" (e a *variável de
   clausura* "__class__") em métodos de subclasses de "NamedTuple" não
   é suportado e causa um "TypeError".

class typing.NewType(name, tp)

   Classe auxiliar para criar tipos únicos com baixo custo.

   A "NewType" is considered a distinct type by a type checker. At
   runtime, however, calling a "NewType" returns its argument
   unchanged.

   Uso:

      UserId = NewType('UserId', int) # Declare o NewType "UserId"
      first_user = UserId(1) # "UserId" retorna o argumento inalterado em tempo de execução

   __module__

      O nome do módulo no qual o novo tipo é definido.

   __name__

      O nome do novo tipo.

   __supertype__

      O tipo na qual o novo tipo é baseado.

   Adicionado na versão 3.5.2.

   Alterado na versão 3.10: "NewType" agora é uma classe em vez de uma
   função.

class typing.Protocol(Generic)

   Classe base para classes de protocolo.

   Classes de protocolo são definidas assim:

      class Proto(Protocol):
          def meth(self) -> int:
              ...

   Essas classes são usadas principalmente com verificadores de tipo
   estático que reconhecem a subtipagem estrutural (tipagem pato
   estática). Por exemplo:

      class C:
          def meth(self) -> int:
              return 0

      def func(x: Proto) -> int:
          return x.meth()

      func(C())  # Passa na verificação de tipos

   See **PEP 544** for more details. Protocol classes decorated with
   "@runtime_checkable" (described later) act as simple-minded runtime
   protocols that check only the presence of given attributes,
   ignoring their type signatures. Protocol classes without this
   decorator cannot be used as the second argument to "isinstance()"
   or "issubclass()".

   Classes de protocolo podem ser genéricas. Por exemplo:

      class GenProto[T](Protocol):
          def meth(self) -> T:
              ...

   Em códigos que precisam ser compatíveis com Python 3.11 ou versões
   anteriores, protocolos genéricos podem ser escritos da seguinte
   forma:

      T = TypeVar("T")

      class GenProto(Protocol[T]):
          def meth(self) -> T:
              ...

   Adicionado na versão 3.8.

   Descontinuado desde a versão 3.15, será removido na versão 3.20: It
   is deprecated to call "isinstance()" and "issubclass()" checks on
   protocol classes that were not explicitly decorated with
   "runtime_checkable()" but that inherit from a runtime-checkable
   protocol class. This will throw a "TypeError" in Python 3.20.

@typing.runtime_checkable

   Marca uma classe de protocolo como um protocolo de tempo de
   execução.

   Such a protocol can be used with "isinstance()" and "issubclass()".
   This allows a simple-minded structural check, very similar to "one-
   trick ponies" in "collections.abc" such as "Iterable".  For
   example:

      @runtime_checkable
      class Closable(Protocol):
          def close(self): ...

      assert isinstance(open('/some/file'), Closable)

      @runtime_checkable
      class Named(Protocol):
          name: str

      import threading
      assert isinstance(threading.Thread(name='Bob'), Named)

   Runtime checkability of protocols is not inherited. A subclass of a
   runtime-checkable protocol is only runtime-checkable if it is
   explicitly marked as such, regardless of class hierarchy:

      @runtime_checkable
      class Iterable(Protocol):
          def __iter__(self): ...

      # Without @runtime_checkable, Reversible would no longer be runtime-checkable.
      @runtime_checkable
      class Reversible(Iterable, Protocol):
          def __reversed__(self): ...

   Este decorador levanta "TypeError" quando aplicado a uma classe
   não-protocolo.

   Nota:

     "@runtime_checkable" will check only the presence of the required
     methods or attributes, not their type signatures or types. For
     example, "ssl.SSLObject" is a class, therefore it passes an
     "issubclass()" check against Callable. However, the
     "ssl.SSLObject.__init__" method exists only to raise a
     "TypeError" with a more informative message, therefore making it
     impossible to call (instantiate) "ssl.SSLObject".

   Nota:

     uma verificação com "isinstance()" sobre um protocolo verificável
     em tempo de execução pode ser surpreendentemente lenta se
     comparada a uma verificação "isinstance()" sobre outros tipos de
     classe. Considere usar expressões alternativas, como chamar a
     função "hasattr()" para realizar verificações estruturais em
     código sensível a desempenho.

   Adicionado na versão 3.8.

   Alterado na versão 3.12: A implementação interna do "isinstance()"
   agora verifica os protocolos verificáveis em tempo de execução
   usando "inspect.getattr_static()" para procurar o atributo
   (anteriormente, era usado "hasattr()"). Como resultado, alguns
   objetos que costumavam ser considerados instâncias de um protoloco
   verifiável em tempo de execução podem não ser mais considerados
   instâncias desse protocolo em Python 3.12+, e vice-versa. É
   improvável que a maioria dos usuários seja afetada por essa
   alteração.

   Alterado na versão 3.12: Os membros de um protocolo verificável em
   tempo de execução agora serão considerados "congelados" em tempo de
   execução assim que a classe for criada. A alteração dinâmica de
   atributos de um protocolo em tempo de execução ainda funcionará,
   mas não terá impacto nas verificações de "isinstance()" ao comparar
   objetos com o protocolo. Consulte o O que há de novo no Python 3.12
   para mais detalhes.

   Descontinuado desde a versão 3.15, será removido na versão 3.20: It
   is deprecated to call "isinstance()" and "issubclass()" checks on
   protocol classes that were not explicitly decorated with
   "runtime_checkable()" but that inherit from a runtime-checkable
   protocol class. This will throw a "TypeError" in Python 3.20.

class typing.TypedDict(dict)

   Special construct to add type hints to a dictionary. At runtime
   ""TypedDict" instances" are simply "dicts".

   "TypedDict" declara um tipo dicionário que espera que todas as suas
   instâncias tenham um determinado conjunto de chaves, onde cada
   chave está associada a um valor de um tipo consistente. Essa
   expectativa não é verificada em tempo de execução, mas é imposta
   apenas por verificadores de tipos. Modo de usar:

      class Point2D(TypedDict):
          x: int
          y: int
          label: str

      a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
      b: Point2D = {'z': 3, 'label': 'bad'}           # Falha na verificação de tipos

      assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')

   Um modo alternativo de criar um "TypedDict" é usando a sintaxe de
   chamada de função. O segundo argumento deve ser um "dict":

      Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})

   Esta sintaxe funcional permite definirmos chaves usando
   identificadores inválidos, por exemplo, por serem palavras-chave ou
   conterem hífens, ou quando os nomes das chaves não devem ser
   desconfigurados como nomes privados comuns:

      # levanta SyntaxError
      class Point2D(TypedDict):
          in: int  # 'in' é uma palavra reservada
          x-y: int  # nome com hífen

      class Definition(TypedDict):
          __schema: str  # desconfigurado para `_Definition__schema`

      # OK, sintaxe funcional
      Point2D = TypedDict('Point2D', {'in': int, 'x-y': int})
      Definition = TypedDict('Definition', {'__schema': str})  # não desconfigurado

   Por padrão, todas as chaves devem estar presentes em um
   "TypedDict". É possível marcar chaves individuais como não-
   obrigatórias usando "NotRequired":

      class Point2D(TypedDict):
          x: int
          y: int
          label: NotRequired[str]

      # Sintaxe alternativa
      Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': NotRequired[str]})

   Isso significa que um "TypedDict" "Point2D" pode ter a chave
   "label" omitida.

   Também é possível marcar todas as chaves como não necessárias por
   padrão, especificando a totalidade como "False":

      class Point2D(TypedDict, total=False):
          x: int
          y: int

      # Sintaxe alternativa
      Point2D = TypedDict('Point2D', {'x': int, 'y': int}, total=False)

   Isso significa que um "TypedDict" "Point2D"  pode ter qualquer uma
   de suas chaves omitidas. Espera-se que um verificador de tipos
   apenas permita os literais "False" ou "True" como valores do
   argumento "total". "True" é o padrão, e todos os itens definidos no
   corpo da classe tornam-se obrigatórios.

   As chaves individuais de um "TypedDict" com "total=False" podem ser
   marcadas como obrigatórias usando "Required":

      class Point2D(TypedDict, total=False):
          x: Required[int]
          y: Required[int]
          label: str

      # Sintaxe alternativa
      Point2D = TypedDict('Point2D', {
          'x': Required[int],
          'y': Required[int],
          'label': str
      }, total=False)

   É possível que um tipo "TypedDict" herde de um ou mais tipos
   "TypedDict" usando a sintaxe baseada em classes. Modo de usar:

      class Point3D(Point2D):
          z: int

   "Point3D" tem três itens: "x", "y" e "z". Equivale a esta
   definição:

      class Point3D(TypedDict):
          x: int
          y: int
          z: int

   By default, a "TypedDict" is open, meaning that it may contain
   additional keys at runtime beyond those defined in the class body.
   The *closed* class argument can be used to control this; if
   "closed=True", the "TypedDict" cannot contain additional keys.

      class ClosedPoint(TypedDict, closed=True):
          x: int
          y: int

      class ClosedPoint3D(ClosedPoint):  # type checker error: cannot add keys to a closed TypedDict
          z: int

   Setting "closed=False" explicitly requests the default open
   behavior. If the argument is not passed, this state is inherited
   from the parent class.

   In addition to being open or closed, a "TypedDict" can also be
   configured to have extra items. If the *extra_items* class argument
   is set to a type, the "TypedDict" can contain arbitrary additional
   keys, but the values of those keys must be of the specified type.

      class ExtraItemsPoint(TypedDict, extra_items=int):
          x: int
          y: int

      point: ExtraItemsPoint = {'x': 1, 'y': 2, 'anything': 3}  # OK

   The *extra_items* argument is also inherited through subclassing.
   It is unset by default, and it may not be used together with the
   *closed* argument.

   Um "TypedDict" não pode herdar de uma classe não "TypedDict",
   exceto "Generic". Por exemplo:

      class X(TypedDict):
          x: int

      class Y(TypedDict):
          y: int

      class Z(object): pass  # Uma classe não TypedDict

      class XY(X, Y): pass  # OK

      class XZ(X, Z): pass  # levanta TypeError

   Um "TypedDict" pode ser genérico:

      class Group[T](TypedDict):
          key: T
          group: list[T]

   Para criar um "TypedDict" genérico que seja compatível com Python
   3.11 ou inferior, herde de "Generic" explicitamente:

      T = TypeVar("T")

      class Group(TypedDict, Generic[T]):
          key: T
          group: list[T]

   A "TypedDict" can be introspected via
   "annotationlib.get_annotations()" (see Boas práticas para anotações
   for more information on annotations best practices) and the
   following attributes:

   __total__

      "Point2D.__total__" fornece o valor do argumento "total".
      Exemplo:

         >>> from typing import TypedDict
         >>> class Point2D(TypedDict): pass
         >>> Point2D.__total__
         True
         >>> class Point2D(TypedDict, total=False): pass
         >>> Point2D.__total__
         False
         >>> class Point3D(Point2D): pass
         >>> Point3D.__total__
         True

      Esse atributo reflete *apenas* o valor do argumento "total" para
      a classe "TypedDict" atual, e não que a classe é semanticamente
      total. Por exemplo, um "TypedDict" com "__total__" definido como
      "True" pode ter chaves marcadas com "NotRequired", ou pode
      herdar de outro "TypedDict" com "total=False". Portanto,
      geralmente é melhor usar "__required_keys__" e
      "__optional_keys__" para introspecção.

   __required_keys__

      Adicionado na versão 3.9.

   __optional_keys__

      "Point2D.__required_keys__" e "Point2D.__optional_keys__"
      retornam objetos "frozenset" contendo chaves obrigatórias e
      opcionais, respectivamente.

      As chaves marcadas com "Required" sempre aparecerão em
      "__required_keys__" e as chaves marcadas com "NotRequired"
      sempre aparecerão em "__optional_keys__".

      For backwards compatibility with Python 3.10 and below, it is
      also possible to use inheritance to declare both required and
      non-required keys in the same "TypedDict". This is done by
      declaring a "TypedDict" with one value for the "total" argument
      and then inheriting from it in another "TypedDict" with a
      different value for "total":

         >>> class Point2D(TypedDict, total=False):
         ...     x: int
         ...     y: int
         ...
         >>> class Point3D(Point2D):
         ...     z: int
         ...
         >>> Point3D.__required_keys__ == frozenset({'z'})
         True
         >>> Point3D.__optional_keys__ == frozenset({'x', 'y'})
         True

      Adicionado na versão 3.9.

      Nota:

        Se "from __future__ import annotations" for usado ou se
        anotações forem fornecidas como strings, as anotações não
        serão avaliadas quando o "TypedDict" for definido. Portanto, a
        introspecção em tempo de execução da qual "__required_keys__"
        e "__optional_keys__" dependem pode não funcionar
        corretamente, e os valores dos atributos podem estar
        incorretos.

   __readonly_keys__

      Um "frozenset" contendo os nomes de todas as chaves somente para
      leitura. As chaves são somente para leitura se tiverem o
      qualificador "ReadOnly".

      Adicionado na versão 3.13.

   __mutable_keys__

      Um "frozenset" contendo os nomes de todas as chaves mutáveis. As
      chaves são mutáveis se não tiverem o qualificador "ReadOnly".

      Adicionado na versão 3.13.

   __closed__

      The value of the *closed* class argument. It can be "True",
      "False", or "None".

   __extra_items__

      The value of the *extra_items* class argument. It can be a valid
      type or "NoExtraItems".

   Consulte a seção TypedDict na documentação de tipagem para obter
   mais exemplos e regras detalhadas.

   Adicionado na versão 3.8.

   Alterado na versão 3.9: "TypedDict" is now a function rather than a
   class. It can still be used as a class base, as described above.

   Alterado na versão 3.11: Adicionado suporte para marcar chaves
   individuais como "Required" ou "NotRequired". Consulte **PEP 655**.

   Alterado na versão 3.11: Adicionado suporte para "TypedDict"s
   genéricos.

   Alterado na versão 3.13: Removeu suporte para o método de argumento
   nomeado para criar "TypedDict"s.

   Alterado na versão 3.13: Support for the "ReadOnly" qualifier was
   added. See **PEP 705**.

   Alterado na versão 3.15: Support for the *closed* and *extra_items*
   class arguments was added. See **PEP 728**.


Protocolos
----------

Os protocolos a seguir são fornecidos pelo módulo "typing". Todos são
decorados com "@runtime_checkable".

class typing.SupportsAbs

   A protocol with one abstract method "__abs__" that is covariant in
   its return type.

class typing.SupportsBytes

   A protocol with one abstract method "__bytes__".

class typing.SupportsComplex

   A protocol with one abstract method "__complex__".

class typing.SupportsFloat

   A protocol with one abstract method "__float__".

class typing.SupportsIndex

   A protocol with one abstract method "__index__".

   Adicionado na versão 3.8.

class typing.SupportsInt

   A protocol with one abstract method "__int__".

class typing.SupportsRound

   A protocol with one abstract method "__round__" that is covariant
   in its return type.


ABCs e protocolos para trabalhar com E/S
----------------------------------------

class typing.IO[AnyStr]
class typing.TextIO
class typing.BinaryIO

   A classe genérica "IO[AnyStr]" e suas subclasses "TextIO(IO[str])"
   e "BinaryIO(IO[bytes])" representam os tipos de fluxos de E/S, como
   os retornados por "open()". Note que essas classes não são
   protocolos e sua interface é bem ampla.

Os protocolos "io.Reader" e "io.Writer" oferecem uma alternativa mais
simples para tipos de argumentos, quando apenas os métodos "read()" ou
"write()" são acessados, respectivamente:

   def read_and_write(reader: Reader[str], writer: Writer[bytes]):
       data = reader.read()
       writer.write(data.encode())

Considere também usar "collections.abc.Iterable" para iterar sobre as
linhas de um fluxo de entrada:

   def read_config(stream: Iterable[str]):
       for line in stream:
           ...


Funções e decoradores
---------------------

typing.cast(typ, val)

   Converta um valor em um tipo.

   Isso retorna o valor inalterado. Para o verificador de tipos, isso
   indica que o valor de retorno tem o tipo designado, mas em tempo de
   execução não verificamos nada intencionalmente (queremos que isso
   seja o mais rápido possível).

typing.assert_type(val, typ, /)

   Pede para um verificador de tipo estático confirmar se *val* tem
   tipo inferido *typ*.

   Essa função faz nada em tempo de execução: ela retorna o primeiro
   argumento inalterado, sem verificações ou efeitos colaterais,
   independentemente do tipo real do argumento.

   Quando um verificador de tipo estático encontra uma chamada para
   "assert_type()", ele emite um erro se o valor não for do tipo
   especificado:

      def greet(name: str) -> None:
          assert_type(name, str) # OK, o tipo inferido de `name` é `str`
          assert_type(name, int) # erro no verificador de tipos

   Esse função é útil para garantir que o verificador de tipos entende
   um script conforme as intenções do desenvolvedor:

      def complex_function(arg: object):
          # Realiza alguma lógica complexa de restrição de tipos
          # após a qual esperamos que o tipo seja `int`
          ...
          # Testa se o verificador de tipos entendeu nossa função corretamente
          assert_type(arg, int)

   Adicionado na versão 3.11.

typing.assert_never(arg, /)

   Pede ao verificador de tipo estático para confirmar se uma linha de
   código é inalcançável.

   Exemplo:

      def int_or_str(arg: int | str) -> None:
          match arg:
              case int():
                  print("É um int")
              case str():
                  print("É um str")
              case _ as unreachable:
                  assert_never(unreachable)

   Aqui, as anotações permitem que o verificador de tipos deduza que o
   último caso nunca será executado, pois "arg" é um "int" ou uma
   "str", e ambas as opções são cobertas por casos anteriores.

   Se um verificador de tipos descobrir que uma chamada para
   "assert_never()" é alcançável, ele emitirá um erro. Por exemplo, se
   a anotação de tipo para "arg" fosse "int | str | float", o
   verificador de tipos emitiria um erro indicando que "unreachable" é
   do tipo "float". Para que uma chamada para "assert_never" passe
   verificação de tipos, o tipo inferido do argumento passado deve ser
   o tipo inferior, "Never", e nada mais.

   Em tempo de execução, essa função levanta uma exceção quando
   chamada.

   Ver também:

     Unreachable Code and Exhaustiveness Checking tem mais informações
     sobre a verificação de exaustividade com tipagem estática.

   Adicionado na versão 3.11.

typing.reveal_type(obj, /)

   Pede para um verificador de tipo estático revelar o tipo inferido
   de uma expressão.

   Quando um verificador de tipo estático encontra uma chamada para
   essa função, ele emite um diagnóstico com o tipo inferido do
   argumento. Por exemplo:

      x: int = 1
      reveal_type(x) # O tipo revelado é "builtins.int"

   Isso pode ser útil quando você deseja depurar como o verificador de
   tipos lida com um determinado trecho de código.

   Em tempo de execução, esta função envia o tipo de seu argumento
   para "sys.stderr" e retorna o argumento inalterado (permitindo que
   a chamada seja usada em uma expressão):

      x = reveal_type(1)  # exibe "Runtime type is int"
      print(x)  # exibe "1"

   Observe que o tipo em tempo de execução pode ser diferente (mais ou
   menos específico) do tipo inferido estaticamente por um verificador
   de tipos.

   A maioria dos verificadores de tipos dá suporte a "reveal_type()"
   em qualquer lugar, mesmo que o nome não seja importado de "typing".
   Porém, importar o nome de "typing" permite que o código seja
   executado sem erros em tempo de execução e comunica a intenção com
   mais clareza.

   Adicionado na versão 3.11.

@typing.dataclass_transform(*, eq_default=True, order_default=False, kw_only_default=False, frozen_default=False, field_specifiers=(), **kwargs)

   Um decorador que marca um objeto como tendo comportamento similar a
   uma "dataclass".

   "@dataclass_transform" may be used to decorate a class, metaclass,
   or a function that is itself a decorator. The presence of
   "@dataclass_transform()" tells a static type checker that the
   decorated object performs runtime "magic" that transforms a class
   in a similar way to "@dataclasses.dataclass".

   Exemplo de uso com a função decoradora:

      @dataclass_transform()
      def create_model[T](cls: type[T]) -> type[T]:
          ...
          return cls

      @create_model
      class CustomerModel:
          id: int
          name: str

   Em uma classe base:

      @dataclass_transform()
      class ModelBase: ...

      class CustomerModel(ModelBase):
          id: int
          name: str

   Em uma metaclasse:

      @dataclass_transform()
      class ModelMeta(type): ...

      class ModelBase(metaclass=ModelMeta): ...

      class CustomerModel(ModelBase):
          id: int
          name: str

   As classes "CustomerModel" definidas acima serão tratadas pelos
   verificadores de tipos semelhantemente às classes criadas com
   "@dataclasses.dataclass". Por exemplo, os verificadores de tipo
   presumirão que essas classes têm métodos "__init__" que aceitam
   "id" e "name".

   A classe, metaclasse ou função decorada pode aceitar os seguintes
   argumentos booleanos tal que verificadores de tipo presumirão ter o
   mesmo efeito que teriam no decorador "@dataclasses.dataclass":
   "init", "eq", "order", "unsafe_hash", "frozen", "match_args",
   "kw_only", e "slots". É necessário que o valor desses argumentos
   ("True" ou "False") seja avaliado estaticamente.

   The arguments to the "@dataclass_transform" decorator can be used
   to customize the default behaviors of the decorated class,
   metaclass, or function:

   Parâmetros:
      * **eq_default** (*bool*) -- Indica se o parâmetro "eq" é
        presumido como "True" ou "False" se for omitido pelo chamador.
        O padrão é "True".

      * **order_default** (*bool*) -- Indica se o parâmetro "order" é
        presumido como "True" ou "False" se for omitido pelo chamador.
        O padrão é "False".

      * **kw_only_default** (*bool*) -- Indica se o parâmetro
        "kw_only" é presumido como "True" ou "False" se for omitido
        pelo chamador. O padrão é "False".

      * **frozen_default** (*bool*) -- Indica se o parâmetro "frozen"
        é presumido como "True" ou "False" se for omitido pelo
        chamador. O padrão é "False". Added in version 3.12

      * **field_specifiers** (*tuple**[**Callable**[**...**,
        **Any**]**, **...**]*) -- Especifica uma lista estática de
        classes ou funções compatíveis que descrevem campos,
        semelhante a "dataclasses.field()". O valor padrão é "()".

      * ****kwargs** (*Any*) -- Outros argumentos nomeados arbitrários
        são aceitos para permitir possíveis futuras extensões.

   Verificadores de tipo reconhecem os seguintes parâmetros opcionais
   em especificadores de campos:


   **Parâmetros reconhecidos para especificadores de campos**
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   +----------------------+----------------------------------------------------------------------------------+
   | Nome do parâmetro    | Descrição                                                                        |
   |======================|==================================================================================|
   | "init"               | Indica se o campo deve ser incluído no método "__init__" sintetizado. Se não for |
   |                      | especificado, o valor padrão de "init" é "True".                                 |
   +----------------------+----------------------------------------------------------------------------------+
   | "default"            | Fornece o valor padrão do campo.                                                 |
   +----------------------+----------------------------------------------------------------------------------+
   | "default_factory"    | Fornece uma função de retorno de tempo de execução que retorna o valor padrão do |
   |                      | campo. Se nem "default" nem "default_factory" forem especificados, o campo é     |
   |                      | presumido como sem valor padrão e deverá receber um valor quando a classe for    |
   |                      | instanciada.                                                                     |
   +----------------------+----------------------------------------------------------------------------------+
   | "factory"            | Um apelido para o parâmetro "default_factory" em especificadores de campos.      |
   +----------------------+----------------------------------------------------------------------------------+
   | "kw_only"            | Indicates whether the field should be marked as keyword-only. If "True", the     |
   |                      | field will be keyword-only. If "False", it will not be keyword-only. If          |
   |                      | unspecified, the value of the "kw_only" parameter on the object decorated with   |
   |                      | "@dataclass_transform" will be used, or if that is unspecified, the value of     |
   |                      | "kw_only_default" on "@dataclass_transform" will be used.                        |
   +----------------------+----------------------------------------------------------------------------------+
   | "alias"              | Fornece um nome alternativo para o campo. Esse nome alternativo é usado no       |
   |                      | método "__init__" sintetizado.                                                   |
   +----------------------+----------------------------------------------------------------------------------+

   Em tempo de execução, esse decorador registra seu argumento no
   atributo "__dataclass_transform__" no objeto decorado. Ele não tem
   nenhum outro efeito em tempo de execução.

   Consulte **PEP 681** para mais detalhes.

   Adicionado na versão 3.11.

@typing.overload

   Decorador para criar funções e métodos sobrecarregados.

   O decorador "@overload" permite descrever funções e métodos com
   suporte a várias combinações de tipos de argumento. Uma sequência
   de definições decoradas com "@overload" deve preceder uma única
   definição não decorada por "@overload" (para a mesma
   função/método).

   Definições decoradas com "@overload" são usadas somente para
   benefício do verificador de tipos, já que serão sobrescritas por
   definições sem decoração de "@overload". Enquanto isso, definições
   sem decoração de "@overload" serão usadas em tempo de execução, mas
   devem ser ignoradas pelo verificador de tipos. Em tempo de
   execução, chamar uma função decorada por "@overload" diretamente
   levantará "NotImplementedError".

   Um exemplo de sobrecarga que fornece um tipo mais preciso do que o
   expressar o tipo expresso por uma união ou um tipo variável:

      @overload
      def process(response: None) -> None:
          ...
      @overload
      def process(response: int) -> tuple[int, str]:
          ...
      @overload
      def process(response: bytes) -> str:
          ...
      def process(response):
          ...  # a implementação real vem aqui

   Consulte **PEP 484** para mais detalhes e uma comparação com outras
   semânticas de tipagem.

   Alterado na versão 3.11: Funções sobrecarregadas agora podem ser
   inspecionadas em tempo de execução usando "get_overloads()".

typing.get_overloads(func)

   Retorna uma sequência de definições de *func* decoradas com
   "@overload".

   *func* é o objeto função para a implementação da função
   sobrecarregada. Por exemplo, dada a definição de "process" na
   documentação de "@overload", "get_overloads(process)" retornará uma
   sequência de três objetos função para as três sobrecargas
   definidas. Se for chamada em uma função sem sobrecargas,
   "get_overloads()" retornará uma sequência vazia.

   A função "get_overloads()" pode ser usada em tempo de execução para
   introspecção de uma função sobrecarregada.

   Adicionado na versão 3.11.

typing.clear_overloads()

   Apaga todas as sobrecargas registradas no registro interno.

   Isso pode ser usado para recuperar a memória usada pelo registro.

   Adicionado na versão 3.11.

@typing.final

   Um decorador para indicar métodos e classes finais.

   Decorar um método com "@final" indica a um verificador de tipos que
   o método não pode ser substituído em uma subclasse. Decorar uma
   classe com "@final" indica que ela não pode ser herdada.

   Por exemplo:

      class Base:
          @final
          def done(self) -> None:
              ...
      class Sub(Base):
          def done(self) -> None:  # Erro reportado pelo verificador de tipos
              ...

      @final
      class Leaf:
          ...
      class Other(Leaf):  # Erro reportado pelo verificador de tipos
          ...

   Não há verificação em tempo de execução dessas propriedades. Veja
   **PEP 591** para mais detalhes.

   Adicionado na versão 3.8.

   Alterado na versão 3.11: O decorador tentará definir um atributo
   "__final__" como "True" no objeto decorado. Assim, uma verificação
   como "if getattr(obj, "__final__", False)" pode ser usada em tempo
   de execução para determinar se um objeto "obj" foi marcado como
   final. Se o objeto decorado não tem suporte a definição de
   atributos, o decorador retorna o objeto inalterado sem levantar uma
   exceção.

@typing.no_type_check

   Decorador para indicar que anotações não são dicas de tipo.

   Isso funciona como *decorator* de uma classe ou função. Com uma
   classe, ele se aplica recursivamente a todos os métodos e classes
   definidos nessa classe (mas não a métodos definidos em suas
   superclasses ou subclasses). Os verificadores de tipos ignorarão
   todas as anotações em uma função ou classe com este decorador.

   "@no_type_check" modifica o objeto decorado internamente.

@typing.override

   Decorador para indicar que um método em uma subclasse deve
   substituir um método ou atributo em uma superclasse.

   Os verificadores de tipo devem emitir um erro se um método decorado
   com "@override" substitui nada. Isso ajuda a evitar erros que podem
   ocorrer quando uma classe base muda sem uma mudança equivalente em
   uma classe filha.

   Por exemplo:

      class Base:
          def log_status(self) -> None:
              ...

      class Sub(Base):
          @override
          def log_status(self) -> None:  # OK: substitui Base.log_status
              ...

          @override
          def done(self) -> None:  # Erro reportado pelo verificador de tipos
              ...

   Não há verificação desta propriedade em tempo de execução.

   O decorador tentará definir um atributo "__override__" como "True"
   no objeto decorado. Assim, uma verificação como "if getattr(obj,
   "__override__", False)" poderá ser usada em tempo de execução para
   determinar se um objeto "obj" foi marcado como uma substituição. Se
   o objeto decorado não der suporte à atribuição de atributos, o
   decorador retorna o objeto inalterado sem levantar uma exceção.

   Consulte **PEP 698** para obter mais detalhes.

   Adicionado na versão 3.12.

@typing.disjoint_base

   Decorator to mark a class as a disjoint base.

   Type checkers do not allow child classes of a disjoint base "C" to
   inherit from other disjoint bases that are not parent or child
   classes of "C".

   Por exemplo:

      @disjoint_base
      class Disjoint1: pass

      @disjoint_base
      class Disjoint2: pass

      class Disjoint3(Disjoint1, Disjoint2): pass  # Type checker error

   Type checkers can use knowledge of disjoint bases to detect
   unreachable code and determine when two types can overlap.

   The corresponding runtime concept is a solid base (see Herança
   múltipla). Classes that are solid bases at runtime can be marked
   with "@disjoint_base" in stub files. Users may also mark other
   classes as disjoint bases to indicate to type checkers that
   multiple inheritance with other disjoint bases should not be
   allowed.

   Note that the concept of a solid base is a CPython implementation
   detail, and the exact set of standard library classes that are
   disjoint bases at runtime may change in future versions of Python.

   Adicionado na versão 3.15.

@typing.type_check_only

   Decorador para marcar uma classe ou função como indisponível em
   tempo de execução.

   Este decorador em si não está disponível em tempo de execução. Seu
   objetivo principal é marcar classes definidas em arquivos de tipo
   stub se uma implementação retornar uma instância de uma classe
   privada:

      @type_check_only
      class Response:  # privado ou indisponível em tempo de execução
          code: int
          def get_header(self, name: str) -> str: ...

      def fetch_response() -> Response: ...

   Observe que retornar instâncias de classes privadas não é
   recomendado. Normalmente, é preferível tornar essas classes
   públicas.


Auxiliares de introspecção
--------------------------

typing.get_type_hints(obj, globalns=None, localns=None, include_extras=False, *, format=Format.VALUE)

   Return a dictionary containing type hints for a function, method,
   module, class object, or other callable object.

   This is often the same as "annotationlib.get_annotations()", but
   this function makes the following changes to the annotations
   dictionary:

   * Referências futuras codificadas como literais de string ou
     objetos "ForwardRef" são tratados avaliando-as em *globalns*,
     *localns* e (quando aplicável) no espaço de nomes de parâmetro de
     tipo de *obj*. Se *globalns* ou *localns* não forem fornecidos,
     os dicionários de espaço de nomes apropriados serão inferidos de
     *obj*.

   * "None" é substituído por "types.NoneType".

   * Se "@no_type_check" tiver sido aplicada a *obj*, será retornado
     um dicionário vazio.

   * If *obj* is a class "C", the function returns a dictionary that
     merges annotations from "C"'s base classes with those on "C"
     directly. This is done by traversing "C.__mro__" and iteratively
     combining *annotations* of each base class. Annotations on
     classes appearing earlier in the *method resolution order* always
     take precedence over annotations on classes appearing later in
     the method resolution order.

   * A função substitui recursivamente todas as ocorrências de
     "Annotated[T, ...]", "Required[T]", "NotRequired[T]" e
     "ReadOnly[T]" por "T", a menos que *include_extras* seja definido
     como "True" (consulte "Annotated" para obter mais informações).

   Cuidado:

     Esta função pode executar código arbitrário contido em anotações.
     Consulte Implicações de segurança de anotações de introspecção
     para obter mais informações.

   Nota:

     If "Format.VALUE" is used and any forward references in the
     annotations of *obj* are not resolvable, a "NameError" exception
     is raised. For example, this can happen with names imported under
     "if TYPE_CHECKING". More generally, any kind of exception can be
     raised if an annotation contains invalid Python code.

   Nota:

     Calling "get_type_hints()" on an instance is not supported. To
     retrieve annotations for an instance, call "get_type_hints()" on
     the instance's class instead (for example,
     "get_type_hints(type(obj))").

   Alterado na versão 3.9: Adiciona o parâmetro "include_extras" como
   parte da **PEP 593**. Consulte a documentação em "Annotated" para
   mais informações.

   Alterado na versão 3.11: Anteriormente, "Optional[t]" era
   adicionado a anotações de funções e métodos se um valor padrão
   igual a "None" fosse definido. Agora, a anotação é retornada
   inalterada.

   Alterado na versão 3.14: Added the "format" parameter. See the
   documentation on "annotationlib.get_annotations()" for more
   information.

   Alterado na versão 3.14: Calling "get_type_hints()" on instances is
   no longer supported. Some instances were accepted in earlier
   versions as an undocumented implementation detail.

typing.get_origin(tp)

   Obtenha o versão sem subscrição de um tipo: para um objeto cujo
   tipo tem a forma "X[Y, Z, ...]", retorna "X" .

   Se "X" for um apelido do módulo typing para uma classe embutida ou
   classe de "collections", ele será normalizado para a classe
   original. Se "X" for uma instância de "ParamSpecArgs" ou
   "ParamSpecKwargs", retorna o "ParamSpec" subjacente. Retorna "None"
   para objetos incompatíveis.

   Exemplos:

      assert get_origin(str) is None
      assert get_origin(Dict[str, int]) is dict
      assert get_origin(Union[int, str]) is Union
      assert get_origin(Annotated[str, "metadata"]) is Annotated
      P = ParamSpec('P')
      assert get_origin(P.args) is P
      assert get_origin(P.kwargs) is P

   Adicionado na versão 3.8.

typing.get_args(tp)

   Obtenha os argumentos de tipos com todas as substituições
   realizadas: para um objeto cujo tipo tem a forma "X[Y, Z, ...]",
   retorna "(Y, Z, ...)" .

   Se "X" for uma união ou um "Literal", e estiver contido em outro
   tipo genérico, a ordem de "(Y, Z, ...)" poderá ser diferente da
   ordem dos argumentos originais "[Y, Z, ...]" devido ao
   armazenamento dos tipos em cache. Retorna "()" para objetos sem
   suporte.

   Exemplos:

      assert get_args(int) == ()
      assert get_args(Dict[int, str]) == (int, str)
      assert get_args(Union[int, str]) == (int, str)

   Adicionado na versão 3.8.

typing.get_protocol_members(tp)

   Retorna o conjunto de membros definidos em um "Protocol".

      >>> from typing import Protocol, get_protocol_members
      >>> class P(Protocol):
      ...     def a(self) -> str: ...
      ...     b: int
      >>> get_protocol_members(P) == frozenset({'a', 'b'})
      True

   Levanta "TypeError" para argumentos que não são protocolos.

   Adicionado na versão 3.13.

typing.is_protocol(tp)

   Determina se um tipo é um "Protocol".

   Por exemplo:

      class P(Protocol):
          def a(self) -> str: ...
          b: int

      assert is_protocol(P)
      assert not is_protocol(int)

   This function only returns true for "Protocol" classes, not for
   generic aliases of them:

      class GenericP[T](Protocol):
          def a(self) -> T: ...
          b: int

      assert not is_protocol(GenericP[int])

   Adicionado na versão 3.13.

typing.is_typeddict(tp)

   Verifica se um tipo é um "TypedDict".

   Por exemplo:

      class Film(TypedDict):
          title: str
          year: int

      assert is_typeddict(Film)
      assert not is_typeddict(list | str)

      # TypedDict é uma fábrica para criar dicionários tipados
      # e não um dicionário tipado em si.
      assert not is_typeddict(TypedDict)

   This function only returns true for "TypedDict" classes, not for
   generic aliases of them:

      class GenericFilm[T](TypedDict):
          title: str
          year: T

      assert not is_typeddict(GenericFilm[int])

   Adicionado na versão 3.10.

class typing.ForwardRef

   Classe usada para representação de tipagem interna de referências
   futuras como strings.

   Por exemplo, "List["AlgumaClasse"]" é implicitamente transformado
   em "List[ForwardRef("AlgumaClasse")]". "ForwardRef" não deve ser
   instanciada por um usuário, mas pode ser usada por ferramentas de
   introspecção.

   Nota:

     Tipos genéricos da **PEP 585** como "list["SomeClass"]" não serão
     transformados implicitamente em "list[ForwardRef("SomeClass")]"
     e, portanto, não serão resolvidos automaticamente para
     "list[SomeClass]".

   Adicionado na versão 3.7.4.

   Alterado na versão 3.14: Este agora é um apelido para
   "annotationlib.ForwardRef". Vários comportamentos não documentados
   desta classe foram alterados; por exemplo, após a avaliação de um
   "ForwardRef", o valor avaliado não é mais armazenado em cache.

typing.evaluate_forward_ref(forward_ref, *, owner=None, globals=None, locals=None, type_params=None, format=annotationlib.Format.VALUE)

   Avalia um "annotationlib.ForwardRef" como um *dica de tipo*.

   Isso é semelhante a chamar "annotationlib.ForwardRef.evaluate()",
   mas diferentemente desse método, "evaluate_forward_ref()" também
   avalia recursivamente referências futuras aninhadas dentro da dica
   de tipo.

   Consulte a documentação de "annotationlib.ForwardRef.evaluate()"
   para saber o significado dos parâmetros *owner*, *globals*,
   *locals*, *type_params* e *format*.

   Cuidado:

     Esta função pode executar código arbitrário contido em anotações.
     Consulte Implicações de segurança de anotações de introspecção
     para obter mais informações.

   Adicionado na versão 3.14.

typing.NoDefault

   Um objeto sinalizador usado para indicar que um parâmetro de tipo
   não possui valor-padrão. Por exemplo:

      >>> T = TypeVar("T")
      >>> T.__default__ is typing.NoDefault
      True
      >>> S = TypeVar("S", default=None)
      >>> S.__default__ is None
      True

   Adicionado na versão 3.13.

typing.NoExtraItems

   A "sentinel" object used to indicate that a "TypedDict" does not
   have the *extra_items* class argument.

      >>> from typing import TypedDict, NoExtraItems
      >>> class Point(TypedDict):
      ...     x: int
      ...     y: int
      ...
      >>> Point.__extra_items__ is NoExtraItems
      True


Constante
---------

typing.TYPE_CHECKING

   A special constant that is assumed to be "True" by static type
   checkers. It's "False" at runtime.

   Um módulo cuja importação é cara e que contém apenas tipos usados
   para anotações de tipagem pode ser importado com segurança dentro
   de um bloco "if TYPE_CHECKING:". Isso impede que o módulo seja
   importado em tempo de execução; anotações não são avaliadas de
   forma ansiosa (veja **PEP 649**), portanto, usar símbolos
   indefinidos em anotações é inofensivo -- desde que você não os
   examine posteriormente. Sua ferramenta de análise de tipos
   estáticos definirá "TYPE_CHECKING" como "True" durante a análise de
   tipos estáticos, o que significa que o módulo será importado e os
   tipos serão verificados corretamente durante essa análise.

   Uso:

      if TYPE_CHECKING:
          import expensive_mod

      def fun(arg: expensive_mod.SomeType) -> None:
          local_var: expensive_mod.AnotherType = other_fun()

   Se você ocasionalmente precisar examinar anotações de tipo em tempo
   de execução que podem conter símbolos indefinidos, use
   "annotationlib.get_annotations()" com um parâmetro "format" de
   "annotationlib.Format.STRING" ou "annotationlib.Format.FORWARDREF"
   para recuperar as anotações com segurança sem levantar "NameError".

   Adicionado na versão 3.5.2.


Apelidos descontinuados
-----------------------

Este módulo define vários apelidos descontinuados de classes
pré-existentes da biblioteca padrão. Originalmente, elas eram
incluídas no módulo "typing" para permitir a parametrização dessas
classes genéricas usando "[]". Porém, os apelidos se tornaram
redundantes no Python 3.9, quando as classes pré-existentes
correspondentes passaram a dar suporte a "[]" (consulte a **PEP
585**).

Os tipos redundantes estão descontinuados desde Python 3.9. No
entanto, enquanto os apelidos podem ser removidos em algum momento,
essa remoção desses apelidos não está planejada. Assim, nenhum aviso
de descontinuação será enviado pelo interpretador para esses apelidos.

Se em algum momento decidirem remover esses apelidos descontinuados, o
interpretador emitirá um aviso de descontinuação por, no mínimo, duas
versões de lançamento antes da remoção. Os apelidos são garantidos a
permanecerem no módulo "typing" sem avisos de descontinuação até, no
mínimo, Python 3.14.

Verificadores de tipos são encorajados a sinalizar o uso de tipos
descontinuados se o programa que estão verificando respeita uma versão
mínima de Python 3.9 ou mais nova.


Apelidos de tipos embutidos
~~~~~~~~~~~~~~~~~~~~~~~~~~~

class typing.Dict(dict, MutableMapping[KT, VT])

   Apelido descontinuado de "dict".

   Note que, para anotar argumentos, prefere-se usar um tipo de
   coleção abstrata como "Mapping" em vez de "dict" ou "typing.Dict".

   Descontinuado desde a versão 3.9: "builtins.dict" agora oferece
   suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo Generic
   Alias.

class typing.List(list, MutableSequence[T])

   Apelido descontinuado de "list".

   Note que, para anotar argumentos, é preferível usar um tipo de
   coleção abstrata, como "Sequence" ou "Iterable", em vez de "list"
   ou "typing.List".

   Descontinuado desde a versão 3.9: "builtins.list" agora oferece
   suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo Generic
   Alias.

class typing.Set(set, MutableSet[T])

   Apelido descontinuado de "builtins.set".

   Note que, para anotar argumentos, prefere-se usar um tipo de
   coleção abstrata como "collections.abc.Set" em vez de "set" ou
   "typing.Set".

   Descontinuado desde a versão 3.9: "builtins.set" agora oferece
   suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo Generic
   Alias.

class typing.FrozenSet(frozenset, AbstractSet[T_co])

   Apelido descontinuado de "builtins.frozenset".

   Descontinuado desde a versão 3.9: "builtins.frozenset" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

typing.Tuple

   Apelido descontinuado para "tuple".

   "tuple" e "Tuple" são casos especiais no sistema de tipos; consulte
   Anotando tuplas para obter mais detalhes.

   Descontinuado desde a versão 3.9: "builtins.tuple" agora oferece
   suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo Generic
   Alias.

class typing.Type(Generic[CT_co])

   Apelido descontinuado de "type".

   Consulte O tipo de objetos de classe para obter detalhes sobre como
   usar "type" ou "typing.Type" em anotações de tipos.

   Adicionado na versão 3.5.2.

   Descontinuado desde a versão 3.9: "builtins.type" agora oferece
   suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo Generic
   Alias.


Apelidos para tipos em "collections"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class typing.DefaultDict(collections.defaultdict, MutableMapping[KT, VT])

   Apelido descontinuado de "collections.defaultdict".

   Adicionado na versão 3.5.2.

   Descontinuado desde a versão 3.9: "collections.defaultdict" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.OrderedDict(collections.OrderedDict, MutableMapping[KT, VT])

   Apelido descontinuado de "collections.OrderedDict".

   Adicionado na versão 3.7.2.

   Descontinuado desde a versão 3.9: "collections.OrderedDict" agora
   oferece suporte a subscrição ("[]"). consulte **PEP 585** e Tipo
   Generic Alias.

class typing.ChainMap(collections.ChainMap, MutableMapping[KT, VT])

   Apelido descontinuado de "collections.ChainMap".

   Adicionado na versão 3.6.1.

   Descontinuado desde a versão 3.9: "collections.ChainMap" agora
   oferece suporte a subscrição ("[]"). consulte **PEP 585** e Tipo
   Generic Alias.

class typing.Counter(collections.Counter, Dict[T, int])

   Apelido descontinuado de "collections.Counter".

   Adicionado na versão 3.6.1.

   Descontinuado desde a versão 3.9: "collections.Counter" agora
   oferece suporte a subscrição ("[]"). consulte **PEP 585** e Tipo
   Generic Alias.

class typing.Deque(deque, MutableSequence[T])

   Apelido descontinuado de "collections.deque".

   Adicionado na versão 3.6.1.

   Descontinuado desde a versão 3.9: "collections.deque" agora oferece
   suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo Generic
   Alias.


Apelidos de outros tipos concretos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class typing.Pattern
class typing.Match

   Deprecated aliases corresponding to the return types from
   "re.compile()" and "re.search()".

   Esses tipos (e as funções correspondentes) são genéricas sobre
   "AnyStr". "Pattern" pode ser especializado como "Pattern[str]" ou
   "Pattern[bytes]"; "Match" pode ser especializado como "Match[str]"
   ou "Match[bytes]".

   Descontinuado desde a versão 3.9: Classes "Pattern" e "Match" de
   "re" agora suporte "[]". Consulte **PEP 585** e Tipo Generic Alias.

class typing.Text

   Apelido descontinuado de "str".

   "Text" é fornecida para servir como um caminho compatível com
   versões futuras para código em Python 2: no Python 2, "Text" é um
   apelido para "unicode".

   Use "Text" para indicar que um valor deve conter uma string unicode
   de forma compatível com Python 2 e Python 3:

      def add_unicode_checkmark(text: Text) -> Text:
          return text + u' \u2713'

   Adicionado na versão 3.5.2.

   Descontinuado desde a versão 3.11: Python 2 deixou de receber
   suporte, e a maioria dos verificadores de tipos também não oferece
   suporte à verificação de tipos de código de Python 2. A remoção do
   apelido não está planejada no momento, mas os usuários são
   incentivados a usar "str" em vez de "Text".


Apelidos de contêineres ABC em "collections.abc".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class typing.AbstractSet(Collection[T_co])

   Apelido descontinuado de "collections.abc.Set".

   Descontinuado desde a versão 3.9: "collections.abc.Set" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.ByteString(Sequence[int])

   Apelido descontinuado para "collections.abc.ByteString".

   Use "isinstance(obj, collections.abc.Buffer)" para testar se "obj"
   implementa o protocolo de buffer em tempo de execução. Para uso em
   anotações de tipo, use "Buffer" ou uma união que especifique
   explicitamente os tipos suportados pelo seu código (por exemplo,
   "bytes | bytearray | memoryview").

   "ByteString" foi originalmente concebido para ser uma classe
   abstrata que serviria como um supertipo de "bytes" e "bytearray".
   No entanto, como o ABC nunca teve métodos, saber que um objeto era
   uma instância de "ByteString" nunca lhe dizia nada de útil sobre o
   objeto. Outros tipos comuns de buffer, como "memoryview", também
   nunca foram entendidos como subtipos de "ByteString" (seja em tempo
   de execução ou por verificadores de tipo estáticos).

   See **PEP 688** for more details.

   Descontinuado desde a versão 3.9, será removido na versão 3.17.

class typing.Collection(Sized, Iterable[T_co], Container[T_co])

   Apelido descontinuado de "collections.abc.Collection".

   Adicionado na versão 3.6.

   Descontinuado desde a versão 3.9: "collections.abc.Collection"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

class typing.Container(Generic[T_co])

   Apelido descontinuado de "collections.abc.Container".

   Descontinuado desde a versão 3.9: "collections.abc.Container" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.ItemsView(MappingView, AbstractSet[tuple[KT_co, VT_co]])

   Apelido descontinuado de "collections.abc.ItemsView".

   Descontinuado desde a versão 3.9: "collections.abc.ItemsView" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.KeysView(MappingView, AbstractSet[KT_co])

   Apelido descontinuado de "collections.abc.KeysView".

   Descontinuado desde a versão 3.9: "collections.abc.KeysView" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.Mapping(Collection[KT], Generic[KT, VT_co])

   Apelido descontinuado de "collections.abc.Mapping".

   Descontinuado desde a versão 3.9: "collections.abc.Mapping" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.MappingView(Sized)

   Apelido descontinuado de "collections.abc.MappingView".

   Descontinuado desde a versão 3.9: "collections.abc.MappingView"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

class typing.MutableMapping(Mapping[KT, VT])

   Apelido descontinuado de "collections.abc.MutableMapping".

   Descontinuado desde a versão 3.9: "collections.abc.MutableMapping"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

class typing.MutableSequence(Sequence[T])

   Apelido descontinuado de "collections.abc.MutableSequence".

   Descontinuado desde a versão 3.9: "collections.abc.MutableSequence"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

class typing.MutableSet(AbstractSet[T])

   Apelido descontinuado de "collections.abc.MutableSet".

   Descontinuado desde a versão 3.9: "collections.abc.MutableSet"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

class typing.Sequence(Reversible[T_co], Collection[T_co])

   Apelido descontinuado de "collections.abc.Sequence".

   Descontinuado desde a versão 3.9: "collections.abc.Sequence" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.ValuesView(MappingView, Collection[_VT_co])

   Apelido descontinuado de "collections.abc.ValuesView".

   Descontinuado desde a versão 3.9: "collections.abc.ValuesView"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.


Apelidos para ABCs assíncronas em "collections.abc"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class typing.Coroutine(Awaitable[ReturnType], Generic[YieldType, SendType, ReturnType])

   Apelido descontinuado de "collections.abc.Coroutine".

   Consulte Anotando geradores e corrotinas para obter detalhes sobre
   como usar "collections.abc.Coroutine" e "typing.Coroutine" em
   anotações de tipos.

   Adicionado na versão 3.5.3.

   Descontinuado desde a versão 3.9: "collections.abc.Coroutine" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.AsyncGenerator(AsyncIterator[YieldType], Generic[YieldType, SendType])

   Apelido descontinuado de "collections.abc.AsyncGenerator".

   Consulte Anotando geradores e corrotinas para obter detalhes sobre
   como usar "collections.abc.AsyncGenerator" e
   "typing.AsyncGenerator" em anotações de tipos.

   Adicionado na versão 3.6.1.

   Descontinuado desde a versão 3.9: "collections.abc.AsyncGenerator"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

   Alterado na versão 3.13: O parâmetro "SendType" agora tem um valor-
   padrão.

class typing.AsyncIterable(Generic[T_co])

   Apelido descontinuado de "collections.abc.AsyncIterable".

   Adicionado na versão 3.5.2.

   Descontinuado desde a versão 3.9: "collections.abc.AsyncIterable"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

class typing.AsyncIterator(AsyncIterable[T_co])

   Apelido descontinuado de "collections.abc.AsyncIterator".

   Adicionado na versão 3.5.2.

   Descontinuado desde a versão 3.9: "collections.abc.AsyncIterator"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

class typing.Awaitable(Generic[T_co])

   Apelido descontinuado de "collections.abc.Awaitable".

   Adicionado na versão 3.5.2.

   Descontinuado desde a versão 3.9: "collections.abc.Awaitable" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.


Apelidos para outros ABCs em "collections.abc".
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class typing.Iterable(Generic[T_co])

   Apelido descontinuado de "collections.abc.Iterable".

   Descontinuado desde a versão 3.9: "collections.abc.Iterable" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

class typing.Iterator(Iterable[T_co])

   Apelido descontinuado de "collections.abc.Iterator".

   Descontinuado desde a versão 3.9: "collections.abc.Iterator" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

typing.Callable

   Apelido descontinuado de "collections.abc.Callable".

   Veja Anotações de objetos chamáveis para detalhes sobre como usar
   "collections.abc.Callable" e "typing.Callable" em anotações de
   tipo.

   Descontinuado desde a versão 3.9: "collections.abc.Callable" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

   Alterado na versão 3.10: "Callable" agora oferece suporte a
   "ParamSpec" e "Concatenate". Veja **PEP 612** para mais detalhes.

class typing.Generator(Iterator[YieldType], Generic[YieldType, SendType, ReturnType])

   Apelido descontinuado de "collections.abc.Generator".

   Consulte Anotando geradores e corrotinas para obter detalhes sobre
   como usar "collections.abc.Generator" e "typing.Generator" em
   anotações de tipos.

   Descontinuado desde a versão 3.9: "collections.abc.Generator" agora
   oferece suporte a subscrição ("[]"). Consulte **PEP 585** e Tipo
   Generic Alias.

   Alterado na versão 3.13: Adiciona valores-padrão para os tipos de
   envio e retorno.

class typing.Hashable

   Apelido descontinuado de "collections.abc.Hashable".

   Descontinuado desde a versão 3.12: Use "collections.abc.Hashable"
   diretamente.

class typing.Reversible(Iterable[T_co])

   Apelido descontinuado de "collections.abc.Reversible".

   Descontinuado desde a versão 3.9: "collections.abc.Reversible"
   agora oferece suporte a subscrição ("[]"). Consulte **PEP 585** e
   Tipo Generic Alias.

class typing.Sized

   Apelido descontinuado de "collections.abc.Sized".

   Descontinuado desde a versão 3.12: Use "collections.abc.Sized"
   diretamente.


Apelidos de ABCs da "contextlib"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class typing.ContextManager(Generic[T_co, ExitT_co])

   Apelido descontinuado de "contextlib.AbstractContextManager".

   O primeiro parâmetro de tipo, "T_co", representa o tipo retornado
   pelo método "__enter__()". O segundo parâmetro opcional de tipo,
   "ExitT_co", cujo valor-padrão é "bool | None", representa o tipo
   retornado pelo método "__exit__()".

   Adicionado na versão 3.5.4.

   Descontinuado desde a versão 3.9:
   "contextlib.AbstractContextManager" agora oferece suporte a
   subscrição ("[]"). Consulte **PEP 585** e Tipo Generic Alias.

   Alterado na versão 3.13: Adiciona o segundo parâmetro opcional de
   tipo, "ExitT_co".

class typing.AsyncContextManager(Generic[T_co, AExitT_co])

   Apelido descontinuado de "contextlib.AbstractAsyncContextManager".

   O primeiro parâmetro de tipo, "T_co", representa o tipo retornado
   pelo método "__aenter__()". O segundo parâmetro opcional de tipo,
   "AExitT_co", cujo valor-padrão é "bool | None", representa o tipo
   retornado pelo método "__aexit__()".

   Adicionado na versão 3.6.2.

   Descontinuado desde a versão 3.9:
   "contextlib.AbstractAsyncContextManager" agora oferece suporte a
   subscrição ("[]"). Consulte **PEP 585** e Tipo Generic Alias.

   Alterado na versão 3.13: Adiciona o segundo parâmetro opcional de
   tipo, "AExitT_co".


Cronograma de descontinuação dos principais recursos
====================================================

Alguns recursos em "typing" estão descontinuados e podem ser removidos
em uma versão futura de Python. A tabela a seguir resume as principais
descontinuações para sua conveniência. Ela está sujeita a alterações,
e nem todas as descontinuações estão listadas.

+---------------------------+---------------------------+---------------------------+---------------------------+
| Recurso                   | Descontinuado em          | Remoção planejada         | PEP/issue                 |
|===========================|===========================|===========================|===========================|
| versões "typing" de       | 3.9                       | Não definido (consulte    | **PEP 585**               |
| coleções-padrão           |                           | apelidos descontinuados   |                           |
|                           |                           | para mais informações)    |                           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "typing.ByteString"       | 3.9                       | 3.17                      | gh-91896                  |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "typing.Text"             | 3.11                      | Não definido              | gh-92332                  |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "typing.Hashable" e       | 3.12                      | Não definido              | gh-94309                  |
| "typing.Sized"            |                           |                           |                           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "typing.TypeAlias"        | 3.12                      | Não definido              | **PEP 695**               |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "typing.AnyStr"           | 3.13                      | 3.18                      | gh-105578                 |
+---------------------------+---------------------------+---------------------------+---------------------------+
