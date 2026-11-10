Enum
****

Uma "Enum" é um conjunto de nomes simbólicos vinculados a valores
únicos. São similares a variáveis globais, mas eles oferecem uma
"repr()" mais útil, agrupamento, segurança de tipo e alguns outros
recursos.

Eles são mais úteis quando você tem uma variável que pode ter uma
seleção limitada de valores. Por exemplo, os dias da semana:

   >>> from enum import Enum
   >>> class DiaDaSemana(Enum):
   ...     SEGUNDA = 1
   ...     TERÇA = 2
   ...     QUARTA = 3
   ...     QUINTA = 4
   ...     SEXTA = 5
   ...     SÁBADO = 6
   ...     DOMINGO = 7

Ou talvez as cores primárias RGB:

   >>> from enum import Enum
   >>> class Cor(Enum):
   ...     RED = 1
   ...     GREEN = 2
   ...     BLUE = 3

Como você pode ver, criar um "Enum" é tão simples quanto escrever uma
classe que herda do próprio "Enum".

Nota:

  Maiúsculas em membros de EnumsComo os Enums são usados para
  representar constantes, e para ajudar a evitar problemas com nomes
  conflitando entre métodos/atributos de classes mixin e nomes enum,
  nós fortemente recomendamos o uso de nomes em UPPER_CASE (em caixa
  alta) para membros, e usaremos esse estilo em nossos exemplos.

Dependendo da natureza do enum, o valor de um membro pode ou não ser
importante. Mas, de qualquer forma, esse valor pode ser usado para
obter o membro correspondente:

   >>> DiaDaSemana(3)
   <DiaDaSemana.QUARTA: 3>

Como você pode ver, o "repr()" de um membro mostra o nome do enum, o
nome do membro e o valor. O "str()" de um membro mostra apenas o nome
do enum e o nome do membro:

   >>> print(DiaDaSemana.QUINTA)
   DiaDaSemana.QUINTA

O *tipo* de um membro de enumeração é o enum ao qual ele pertence:

   >>> type(DiaDaSemana.SEGUNDA)
   <enum 'DiaDaSemana'>
   >>> isinstance(DiaDaSemana.SEXTA, DiaDaSemana)
   True

Os membros do Enum têm um atributo que contém apenas seu "name":

   >>> print(DiaDaSemana.TERÇA.name)
   TERÇA

Da mesma forma, eles têm um atributo para seu "value":

   >>> DiaDaSemana.QUARTA.value
   3

Ao contrário de muitas linguagens que tratam enumerações apenas como
pares de nome/valor, Enums do Python podem ter comportamento
adicionado. Por exemplo, "datetime.date" tem dois métodos para
retornar o dia da semana: "weekday()" e "isoweekday()". A diferença é
que um deles conta de 0 a 6 e o outro de 1 a 7. Em vez de tomar conta
disso nós mesmos, podemos adicionar um método ao enum de "DiaDaSemana"
para extrair o dia da instância de "date" e retornar o membro enum
correspondente:

   @classmethod
   def from_date(cls, date):
       return cls(date.isoweekday())

A enum "DiaDaSemana" completa fica então assim:

   >>> class DiaDaSemana(Enum):
   ...     SEGUNDA = 1
   ...     TERÇA = 2
   ...     QUARTA = 3
   ...     QUINTA = 4
   ...     SEXTA = 5
   ...     SÁBADO = 6
   ...     DOMINGO = 7
   ...     #
   ...     @classmethod
   ...     def from_date(cls, date):
   ...         return cls(date.isoweekday())

Agora podemos descobrir que dia é hoje! Observe:

   >>> import datetime as dt
   >>> Weekday.from_date(dt.date.today())
   <Weekday.TUESDAY: 2>

Claro, se você estiver lendo isso em outro dia da semana, você verá
esse respectivo dia.

Essa enum "DiaDaSemana" é ótima se a nossa variável precisar somente
de um único dia, mas e se precisarmos de vários? Talvez estejamos
escrevendo uma função para organizar tarefas ao longo da semana, e não
queremos usar uma "list" -- poderíamos ao invés disso usar um tipo
diferente de "Enum":

   >>> from enum import Flag
   >>> class DiaDaSemana(Flag):
   ...     SEGUNDA = 1
   ...     TERÇA = 2
   ...     QUARTA = 4
   ...     QUINTA = 8
   ...     SEXTA = 16
   ...     SÁBADO = 32
   ...     DOMINGO = 64

Nós mudamos duas coisas: estamos herdando de "Flag" (sinalizador), e
os valores são todos potências de 2.

Assim como a enum "DiaDaSemana" original acima, podemos selecionar um
item de cada vez:

   >>> primeiro_dia_útil = DiaDaSemana.SEGUNDA
   >>> primeiro_dia_útil
   <DiaDaSemana.SEGUNDA: 1>

Porém, a "Flag" também nos permite combinar vários membros em uma
única variável:

   >>> fim_de_semana = DiaDaSemana.SÁBADO | DiaDaSemana.DOMINGO
   >>> fim_de_semana
   <DiaDaSemana.SÁBADO|DOMINGO: 96>

Você pode até mesmo iterar sobre uma variável "Flag":

   >>> for dia in fim_de_semana:
   ...     print(dia)
   DiaDaSemana.SÁBADO
   DiaDaSemana.DOMINGO

Certo, vamos configurar algumas tarefas domésticas:

   >>> tarefas_do_joão = {
   ...     'alimentar o gato': DiaDaSemana.SEGUNDA | DiaDaSemana.QUARTA | DiaDaSemana.SEXTA,
   ...     'lavar a louça': DiaDaSemana.TERÇA | DiaDaSemana.QUINTA,
   ...     'responder perguntas no SO': DiaDaSemana.SÁBADO,
   ...     }

E a função para mostrar as tarefas domésticas para um determinado dia:

   >>> def mostrar_tarefas(tarefas, dia):
   ...     for tarefa, dias in tarefas.items():
   ...         if dia in dias:
   ...             print(tarefa)
   ...
   >>> mostrar_tarefas(tarefas_do_joão, DiaDaSemana.SÁBADO)
   responder perguntas no SO

Quando os valores em si dos membros não forem importantes, você pode
economizar trabalho e usar "auto()" para eles:

   >>> from enum import auto
   >>> class DiaDaSemana(Flag):
   ...     SEGUNDA = auto()
   ...     TERÇA = auto()
   ...     QUARTA = auto()
   ...     QUINTA = auto()
   ...     SEXTA = auto()
   ...     SÁBADO = auto()
   ...     DOMINGO = auto()
   ...     FIM_DE_SEMANA = SÁBADO | DOMINGO


Acesso programático aos membros da enumeração e seus atributos.
===============================================================

Em alguns momentos, é util ter acesso aos membros na enumeração de
forma programática (ou seja, em situações em que "Cor.RED" não é
adequado porque a cor exata não é conhecida no momento da escrita do
programa). Classes "Enum" permitem esse tipo de acesso:

   >>> Cor(1)
   <Cor.RED: 1>
   >>> Cor(3)
   <Cor.BLUE: 3>

Se você deseja ter acesso aos membros do enum pelo *nome*, use o
acesso por itens:

   >>> Cor['VERMELHO']
   <Cor.VERMELHO: 1>
   >>> Color['VERDE']
   <Cor.VERDE: 2>

Dado um membro de um enum, se você precisar do seu "name" ou "value":

   >>> membro = Cor.VERMELHO
   >>> membro.name
   'VERMELHO'
   >>> membro.value
   1


Membros e valores duplicados em enums
=====================================

Ter dois membros de um enum com o mesmo nome é inválido:

   >>> class Forma(Enum):
   ...     QUADRADO = 2
   ...     QUADRADO = 3
   ...
   Traceback (most recent call last):
   ...
   TypeError: 'QUADRADO' already defined as 2

Porém, um membro do enum pode ter outros nomes associados a ele. Dados
dois membros "A" e "B" com o mesmo valor (e "A" definido primeiro),
"B" é um apelido para o membro "A". A busca pelo membro associado ao
valor de "A" retorna o membro "A". A busca pelo membro com o nome de
"A" retorna o membro "A". A busca pelo membro com o nome de "B" também
retorna o membro "A":

   >>> class Forma(Enum):
   ...     QUADRADO = 2
   ...     DIAMANTE = 1
   ...     CÍRCULO = 3
   ...     APELIDO_PARA_O_QUADRADO = 2
   ...
   >>> Forma.QUADRADO
   <Forma.QUADRADO: 2>
   >>> Forma.APELIDO_PARA_O_QUADRADO
   <Forma.QUADRADO: 2>
   >>> Forma(2)
   <Forma.QUADRADO: 2>

Nota:

  Tentar criar um membro com o mesmo nome de um atributo já definido
  (outro membro, um método, etc.) ou tentar criar um atributo com o
  mesmo nome de um membro não é permitido.


Garantindo valores únicos na enumeração
=======================================

By default, enumerations allow multiple names as aliases for the same
value. When this behavior isn't desired, you can use the "@unique"
decorator:

   >>> from enum import Enum, unique
   >>> @unique
   ... class Errado(Enum):
   ...     UM = 1
   ...     DOIS = 2
   ...     TRES = 3
   ...     QUATRO = 3
   ...
   Traceback (most recent call last):
   ...
   ValueError: duplicate values found in <enum 'Errado'>: QUATRO -> TRES


Usando valores automáticos
==========================

Se o valor em si não é importante, você pode usar "auto":

   >>> from enum import Enum, auto
   >>> class Cor(Enum):
   ...     RED = auto()
   ...     BLUE = auto()
   ...     GREEN = auto()
   ...
   >>> [membro.value for membro in Cor]
   [1, 2, 3]

Os valores são escolhidos pelo "_generate_next_value_()", que pode ser
substituído:

   >>> class AutoName(Enum):
   ...     @staticmethod
   ...     def _generate_next_value_(name, start, count, last_values):
   ...         return name
   ...
   >>> class Ordinal(AutoName):
   ...     NORTE = auto()
   ...     SUL = auto()
   ...     LESTE = auto()
   ...     OESTE = auto()
   ...
   >>> [membro.value for membro in Ordinal]
   ['NORTE', 'SUL', 'LESTE', 'OESTE']

Nota:

  O método "_generate_next_value_()" deve ser definido antes de
  qualquer membro.


Iteração
========

Iterar sobre os membros de um enum não fornece os apelidos:

   >>> list(Forma)
   [<Forma.QUADRADO: 2>, <Forma.DIAMANTE: 1>, <Forma.CÍRCULO: 3>]
   >>> list(DiaDaSemana)
   [<DiaDaSemana.SEGUNDA: 1>, <DiaDaSemana.TERÇA: 2>, <DiaDaSemana.QUARTA: 4>, <DiaDaSemana.QUINTA: 8>, <DiaDaSemana.SEXTA: 16>, <DiaDaSemana.SÁBADO: 32>, <DiaDaSemana.DOMINGO: 64>]

Note que os apelidos "Forma.APELIDO_PARA_O_QUADRADO" e
"DiaDaSemana.FIM_DE_SEMANA" não são mostrados.

O atributo especial "__members__" é um mapeamento ordenado de somente
leitura dos nomes para os membros. Isso inclui todos os nomes
definidos na enumeração, incluindo os apelidos:

   >>> for nome, membroin Forma.__members__.items():
   ...     nome, membro
   ...
   ('QUADRADO', <Forma.QUADRADO: 2>)
   ('DIAMANTE', <Forma.DIAMANTE: 1>)
   ('CÍRCULO', <Forma.CÍRCULO: 3>)
   ('APELIDO_PARA_O_QUADRADO', <Forma.QUADRADO: 2>)

O atributo "__members__" pode ser usado para um acesso programático
detalhado aos membros da enumeração. Por exemplo, achar todos os
apelidos:

   >>> [nome for nome, membro in Forma.__members__.items() if membro.name != nome]
   ['APELIDO_PARA_O_QUADRADO']

Nota:

  Apelidos em sinalizadores incluem valores com múltiplos itens ao
  mesmo tempo, como "3", e nenhum item definido, isto é, "0".


Comparações
===========

Membros de uma enumeração são comparados por identidade:

   >>> Color.VERMELHO is Color.VERMELHO
   True
   >>> Color.VERMELHO is Color.AZUL
   False
   >>> Color.VERMELHO is not Color.AZUL
   True

Comparações ordenadas entre valores de enumerações *não* são
suportadas. Membros Enum não são inteiros (porém, veja IntEnum
abaixo):

   >>> Color.VERMELHO < Color.AZUL
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: '<' not supported between instances of 'Color' and 'Color'

Entretanto, comparações de igualdade são definidas:

   >>> Color.AZUL == Color.VERMELHO
   False
   >>> Color.AZUL != Color.VERMELHO
   True
   >>> Color.AZUL == Color.AZUL
   True

Equality comparisons against non-enumeration values will always return
"False" (again, "IntEnum" was explicitly designed to behave
differently, see below):

   >>> Color.AZUL == 2
   False

Aviso:

  É possivel recarregar módulos -- se um módulo recarregado contém
  enums, eles serão recriados, e os novos membros não podem ser
  comparados de forma identifica/igual a membros originais.


Membros e atributos permitidos em enumerações
=============================================

A maioria dos exemplos acima usa inteiros como valores para os enums.
Usar inteiros é simples e prático (isso é disponibilizado como padrão
pela API funcional), mas não é a única aplicação. Na grande maioria
dos caso de uso, não importa o valor de fato que um enum possui. Mas
se o valor *é* importante, enums podem ser valores arbitrários.

Enumerações são classes Python, e podem ter métodos e até mesmo
métodos especiais como de usual. Se temos essa enumeração:

   >>> class Mood(Enum):
   ...     FUNKY = 1
   ...     HAPPY = 3
   ...
   ...     def describe(self):
   ...         # self is the member here
   ...         return self.name, self.value
   ...
   ...     def __str__(self):
   ...         return 'my custom str! {0}'.format(self.value)
   ...
   ...     @classmethod
   ...     def favorite_mood(cls):
   ...         # cls here is the enumeration
   ...         return cls.HAPPY
   ...

Então:

   >>> Mood.favorite_mood()
   <Mood.HAPPY: 3>
   >>> Mood.HAPPY.describe()
   ('HAPPY', 3)
   >>> str(Mood.FUNKY)
   'my custom str! 1'

As regras para o que é permitido são: nomes que começam e terminam com
underline único são reservados para enum e não podem ser usados; todos
os outros atributos definidos dentro de uma enumeração irão se tornar
membros dessa enumeração, com exceção dos métodos especiais (
"__str__()", "__add__()", etc.), descritores (métodos também são
descritores), e nomes de variáveis listadas em "_ignore_".

Nota: se a sua enumeração define "__new__()" e/ou "__init__()",
qualquer valor(es) dado ao membro da enum será passado para esses
métodos. Veja Planet, por exemplo.

Nota:

  O método "__new__()", se definido, é usado durante a criação dos
  membros do Enum; em seguida, ele é substituído pelo "__new__()" do
  Enum, que é usado após a criação da classe para buscar por membros
  existentes. Consulte When to use __new__() vs. __init__() para mais
  detalhes.


Herança restrita de Enum
========================

Uma nova classe "Enum" deve ter uma classe enum base, até um tipo de
dado concreto, e quantas classes mixin baseadas em "object" forem
necessárias. A ordem dessas classes base é:

   class EnumName([mix-in, ...,] [data-type,] base-enum):
       pass

Além disso, criar uma subclasse de uma enumeração é permitido apenas
se a enumeração não define nenhum membro. Portanto is,so é proibido:

   >>> class MoreColor(Color):
   ...     PINK = 17
   ...
   Traceback (most recent call last):
   ...
   TypeError: <enum 'MoreColor'> cannot extend <enum 'Color'>

Mas isso é permitido:

   >>> class Foo(Enum):
   ...     def some_behavior(self):
   ...         pass
   ...
   >>> class Bar(Foo):
   ...     HAPPY = 1
   ...     SAD = 2
   ...

Permitir a criação de subclasses de enums que definem membros levaria
a violação de alguns invariantes importantes de tipos e instâncias.
Por outro lado, faz sentido permitir o compartilhamento de algum
comportamento comum entre um grupo de enumerações. (Veja OrderedEnum,
por exemplo.)


Suporte a dataclass
===================

Ao herdar de uma "dataclass", o "__repr__()" omite o nome da classe
herdada. Por exemplo:

   >>> from dataclasses import dataclass, field
   >>> @dataclass
   ... class CreatureDataMixin:
   ...     size: str
   ...     legs: int
   ...     tail: bool = field(repr=False, default=True)
   ...
   >>> class Creature(CreatureDataMixin, Enum):
   ...     BEETLE = 'small', 6
   ...     DOG = 'medium', 4
   ...
   >>> Creature.DOG
   <Creature.DOG: size='medium', legs=4>

Use o argumento "repr=False" de "dataclass()" para utilizar o "repr()"
padrão.

Alterado na versão 3.12: Somente os campos da dataclass são exibidos
na área de valor, e não o nome da dataclass.

Nota:

  Adding "@~dataclasses.dataclass" decorator to "Enum" and its
  subclasses is not supported. It will not raise any errors, but it
  will produce very strange results at runtime, such as members being
  equal to each other:

     >>> @dataclass               # don't do this: it does not make any sense
     ... class Color(Enum):
     ...    RED = 1
     ...    BLUE = 2
     ...
     >>> Color.RED is Color.BLUE
     False
     >>> Color.RED == Color.BLUE  # problem is here: they should not be equal
     True


Pickling
========

Enumerações podem ser serializadas e desserializadas.

   >>> from test.test_enum import Fruit
   >>> from pickle import dumps, loads
   >>> Fruit.TOMATO is loads(dumps(Fruit.TOMATO))
   True

As restrições usuais para serialização se aplicam: enums serializáveis
devem ser definidas no nível mais alto de um módulo, já que para fazer
a desserialização eles devem ser importados daquele módulo.

Nota:

  With pickle protocol version 4 it is possible to easily pickle enums
  nested in other classes.

It is possible to modify how enum members are pickled/unpickled by
defining "__reduce_ex__()" in the enumeration class.  The default
method is by-value, but enums with complicated values may want to use
by-name:

   >>> import enum
   >>> class MyEnum(enum.Enum):
   ...     __reduce_ex__ = enum.pickle_by_enum_name

Nota:

  Using by-name for flags is not recommended, as unnamed aliases will
  not unpickle.


API funcional
=============

A classe "Enum" é chamável, fornecendo a API funcional a seguir:

   >>> Animal = Enum('Animal', 'ANT BEE CAT DOG')
   >>> Animal
   <enum 'Animal'>
   >>> Animal.ANT
   <Animal.ANT: 1>
   >>> list(Animal)
   [<Animal.ANT: 1>, <Animal.BEE: 2>, <Animal.CAT: 3>, <Animal.DOG: 4>]

The semantics of this API resemble "namedtuple". The first argument of
the call to "Enum" is the name of the enumeration.

The second argument is the *source* of enumeration member names.  It
can be a whitespace-separated string of names, a sequence of names, a
sequence of 2-tuples with key/value pairs, or a mapping (e.g.
dictionary) of names to values.  The last two options enable assigning
arbitrary values to enumerations; the others auto-assign increasing
integers starting with 1 (use the "start" parameter to specify a
different starting value).  A new class derived from "Enum" is
returned.  In other words, the above assignment to "Animal" is
equivalent to:

   >>> class Animal(Enum):
   ...     ANT = 1
   ...     BEE = 2
   ...     CAT = 3
   ...     DOG = 4
   ...

The reason for defaulting to "1" as the starting number and not "0" is
that "0" is "False" in a boolean sense, but by default enum members
all evaluate to "True".

Pickling enums created with the functional API can be tricky as frame
stack implementation details are used to try and figure out which
module the enumeration is being created in (e.g. it will fail if you
use a utility function in a separate module, and also may not work on
IronPython or Jython). The solution is to specify the module name
explicitly as follows:

   >>> Animal = Enum('Animal', 'ANT BEE CAT DOG', module=__name__)

Aviso:

  If "module" is not supplied, and Enum cannot determine what it is,
  the new Enum members will not be unpicklable; to keep errors closer
  to the source, pickling will be disabled.

The new pickle protocol 4 also, in some circumstances, relies on
"__qualname__" being set to the location where pickle will be able to
find the class.  For example, if the class was made available in class
SomeData in the global scope:

   >>> Animal = Enum('Animal', 'ANT BEE CAT DOG', qualname='SomeData.Animal')

A assinatura completa é:

   Enum(
       value='NewEnumName',
       names=<...>,
       *,
       module='...',
       qualname='...',
       type=<mixed-in class>,
       start=1,
       )

* *value*: What the new enum class will record as its name.

* *names*: The enum members.  This can be a whitespace- or comma-
  separated string (values will start at 1 unless otherwise
  specified):

     'RED GREEN BLUE' | 'RED,GREEN,BLUE' | 'RED, GREEN, BLUE'

  or an iterator of names:

     ['VERMELHO', 'VERDE', 'AZUL']

  or an iterator of (name, value) pairs:

     [('CYAN', 4), ('MAGENTA', 5), ('YELLOW', 6)]

  or a mapping:

     {'CHARTREUSE': 7, 'SEA_GREEN': 11, 'ROSEMARY': 42}

* *module*: name of module where new enum class can be found.

* *qualname*: where in module new enum class can be found.

* *type*: type to mix in to new enum class.

* *start*: number to start counting at if only names are passed in.

Alterado na versão 3.5: The *start* parameter was added.


Derived Enumerations
====================


IntEnum
-------

The first variation of "Enum" that is provided is also a subclass of
"int".  Members of an "IntEnum" can be compared to integers; by
extension, integer enumerations of different types can also be
compared to each other:

   >>> from enum import IntEnum
   >>> class Shape(IntEnum):
   ...     CIRCLE = 1
   ...     SQUARE = 2
   ...
   >>> class Request(IntEnum):
   ...     POST = 1
   ...     GET = 2
   ...
   >>> Shape == 1
   False
   >>> Shape.CIRCLE == 1
   True
   >>> Shape.CIRCLE == Request.POST
   True

However, they still can't be compared to standard "Enum" enumerations:

   >>> class Shape(IntEnum):
   ...     CIRCLE = 1
   ...     SQUARE = 2
   ...
   >>> class Color(Enum):
   ...     RED = 1
   ...     GREEN = 2
   ...
   >>> Shape.CIRCLE == Color.RED
   False

"IntEnum" values behave like integers in other ways you'd expect:

   >>> int(Shape.CIRCLE)
   1
   >>> ['a', 'b', 'c'][Shape.CIRCLE]
   'b'
   >>> [i for i in range(Shape.SQUARE)]
   [0, 1]


StrEnum
-------

The second variation of "Enum" that is provided is also a subclass of
"str".  Members of a "StrEnum" can be compared to strings; by
extension, string enumerations of different types can also be compared
to each other.

Adicionado na versão 3.11.


IntFlag
-------

The next variation of "Enum" provided, "IntFlag", is also based on
"int".  The difference being "IntFlag" members can be combined using
the bitwise operators (&, |, ^, ~) and the result is still an
"IntFlag" member, if possible.  Like "IntEnum", "IntFlag" members are
also integers and can be used wherever an "int" is used.

Nota:

  Any operation on an "IntFlag" member besides the bit-wise operations
  will lose the "IntFlag" membership.Bit-wise operations that result
  in invalid "IntFlag" values will lose the "IntFlag" membership.  See
  "FlagBoundary" for details.

Adicionado na versão 3.6.

Alterado na versão 3.11.

Sample "IntFlag" class:

   >>> from enum import IntFlag
   >>> class Perm(IntFlag):
   ...     R = 4
   ...     W = 2
   ...     X = 1
   ...
   >>> Perm.R | Perm.W
   <Perm.R|W: 6>
   >>> Perm.R + Perm.W
   6
   >>> RW = Perm.R | Perm.W
   >>> Perm.R in RW
   True

It is also possible to name the combinations:

   >>> class Perm(IntFlag):
   ...     R = 4
   ...     W = 2
   ...     X = 1
   ...     RWX = 7
   ...
   >>> Perm.RWX
   <Perm.RWX: 7>
   >>> ~Perm.RWX
   <Perm: 0>
   >>> Perm(7)
   <Perm.RWX: 7>

Nota:

  Combinações nomeadas são consideradas apelidos. Apelidos não
  aparecem durante uma iteração, mas podem ser retornados por
  pesquisas por valor.

Alterado na versão 3.11.

Another important difference between "IntFlag" and "Enum" is that if
no flags are set (the value is 0), its boolean evaluation is "False":

   >>> Perm.R & Perm.X
   <Perm: 0>
   >>> bool(Perm.R & Perm.X)
   False

Because "IntFlag" members are also subclasses of "int" they can be
combined with them (but may lose "IntFlag" membership:

   >>> Perm.X | 4
   <Perm.R|X: 5>

   >>> Perm.X + 8
   9

Nota:

  The negation operator, "~", always returns an "IntFlag" member with
  a positive value:

     >>> (~Perm.X).value == (Perm.R|Perm.W).value == 6
     True

"IntFlag" members can also be iterated over:

   >>> list(RW)
   [<Perm.R: 4>, <Perm.W: 2>]

Adicionado na versão 3.11.


Sinalizador
-----------

The last variation is "Flag".  Like "IntFlag", "Flag" members can be
combined using the bitwise operators (&, |, ^, ~).  Unlike "IntFlag",
they cannot be combined with, nor compared against, any other "Flag"
enumeration, nor "int".  While it is possible to specify the values
directly it is recommended to use "auto" as the value and let "Flag"
select an appropriate value.

Adicionado na versão 3.6.

Like "IntFlag", if a combination of "Flag" members results in no flags
being set, the boolean evaluation is "False":

   >>> from enum import Flag, auto
   >>> class Color(Flag):
   ...     RED = auto()
   ...     BLUE = auto()
   ...     GREEN = auto()
   ...
   >>> Color.RED & Color.GREEN
   <Color: 0>
   >>> bool(Color.RED & Color.GREEN)
   False

Individual flags should have values that are powers of two (1, 2, 4,
8, ...), while combinations of flags will not:

   >>> class Color(Flag):
   ...     RED = auto()
   ...     BLUE = auto()
   ...     GREEN = auto()
   ...     WHITE = RED | BLUE | GREEN
   ...
   >>> Color.WHITE
   <Color.WHITE: 7>

Giving a name to the "no flags set" condition does not change its
boolean value:

   >>> class Color(Flag):
   ...     BLACK = 0
   ...     RED = auto()
   ...     BLUE = auto()
   ...     GREEN = auto()
   ...
   >>> Color.BLACK
   <Color.BLACK: 0>
   >>> bool(Color.BLACK)
   False

"Flag" members can also be iterated over:

   >>> purple = Color.RED | Color.BLUE
   >>> list(purple)
   [<Color.RED: 1>, <Color.BLUE: 2>]

Adicionado na versão 3.11.

Nota:

  For the majority of new code, "Enum" and "Flag" are strongly
  recommended, since "IntEnum" and "IntFlag" break some semantic
  promises of an enumeration (by being comparable to integers, and
  thus by transitivity to other unrelated enumerations).  "IntEnum"
  and "IntFlag" should be used only in cases where "Enum" and "Flag"
  will not do; for example, when integer constants are replaced with
  enumerations, or for interoperability with other systems.


Outros
------

While "IntEnum" is part of the "enum" module, it would be very simple
to implement independently:

   class IntEnum(int, ReprEnum):   # or Enum instead of ReprEnum
       pass

This demonstrates how similar derived enumerations can be defined; for
example a "FloatEnum" that mixes in "float" instead of "int".

Algumas regras:

1. When subclassing "Enum", mix-in types must appear before the "Enum"
   class itself in the sequence of bases, as in the "IntEnum" example
   above.

2. Mix-in types must be subclassable. For example, "bool" and "range"
   are not subclassable and will throw an error during Enum creation
   if used as the mix-in type.

3. While "Enum" can have members of any type, once you mix in an
   additional type, all the members must have values of that type,
   e.g. "int" above.  This restriction does not apply to mix-ins which
   only add methods and don't specify another type.

4. When another data type is mixed in, the "value" attribute is *not
   the same* as the enum member itself, although it is equivalent and
   will compare equal.

5. A "data type" is a mixin that defines "__new__()", or a "dataclass"

6. %-style formatting:  "%s" and "%r" call the "Enum" class's
   "__str__()" and "__repr__()" respectively; other codes (such as
   "%i" or "%h" for IntEnum) treat the enum member as its mixed-in
   type.

7. Formatted string literals, "str.format()", and "format()" will use
   the enum's "__str__()" method.

Nota:

  Because "IntEnum", "IntFlag", and "StrEnum" are designed to be drop-
  in replacements for existing constants, their "__str__()" method has
  been reset to their data types' "__str__()" method.


When to use "__new__()" vs. "__init__()"
========================================

"__new__()" must be used whenever you want to customize the actual
value of the "Enum" member.  Any other modifications may go in either
"__new__()" or "__init__()", with "__init__()" being preferred.

For example, if you want to pass several items to the constructor, but
only want one of them to be the value:

   >>> class Coordinate(bytes, Enum):
   ...     """
   ...     Coordinate with binary codes that can be indexed by the int code.
   ...     """
   ...     def __new__(cls, value, label, unit):
   ...         obj = bytes.__new__(cls, [value])
   ...         obj._value_ = value
   ...         obj.label = label
   ...         obj.unit = unit
   ...         return obj
   ...     PX = (0, 'P.X', 'km')
   ...     PY = (1, 'P.Y', 'km')
   ...     VX = (2, 'V.X', 'km/s')
   ...     VY = (3, 'V.Y', 'km/s')
   ...

   >>> print(Coordinate['PY'])
   Coordinate.PY

   >>> print(Coordinate(3))
   Coordinate.VY

Aviso:

  *Do not* call "super().__new__()", as the lookup-only "__new__" is
  the one that is found; instead, use the data type directly.


Finer Points
============


Supported "__dunder__" and "_sunder_" names
-------------------------------------------

The supported "__dunder__" and "_sunder_" names can be found in the
Enum API documentation.


_Private__names
---------------

Private names are not converted to enum members, but remain normal
attributes.

Alterado na versão 3.11.


"Enum" member type
------------------

Enum members are instances of their enum class, and are normally
accessed as "EnumClass.member".  In certain situations, such as
writing custom enum behavior, being able to access one member directly
from another is useful, and is supported; however, in order to avoid
name clashes between member names and attributes/methods from mixed-in
classes, upper-case names are strongly recommended.

Alterado na versão 3.5.


Creating members that are mixed with other data types
-----------------------------------------------------

When subclassing other data types, such as "int" or "str", with an
"Enum", all values after the "=" are passed to that data type's
constructor.  For example:

   >>> class MyEnum(IntEnum):      # help(int) -> int(x, base=10) -> integer
   ...     example = '11', 16      # so x='11' and base=16
   ...
   >>> MyEnum.example.value        # and hex(11) is...
   17


Boolean value of "Enum" classes and members
-------------------------------------------

Enum classes that are mixed with non-"Enum" types (such as "int",
"str", etc.) are evaluated according to the mixed-in type's rules;
otherwise, all members evaluate as "True".  To make your own enum's
boolean evaluation depend on the member's value add the following to
your class:

   def __bool__(self):
       return bool(self.value)

Plain "Enum" classes always evaluate as "True".


"Enum" classes with methods
---------------------------

If you give your enum subclass extra methods, like the Planet class
below, those methods will show up in a "dir()" of the member, but not
of the class:

   >>> dir(Planet)
   ['EARTH', 'JUPITER', 'MARS', 'MERCURY', 'NEPTUNE', 'SATURN', 'URANUS', 'VENUS', '__class__', '__doc__', '__members__', '__module__']
   >>> dir(Planet.EARTH)
   ['__class__', '__doc__', '__module__', 'mass', 'name', 'radius', 'surface_gravity', 'value']


Combining members of "Flag"
---------------------------

Iterating over a combination of "Flag" members will only return the
members that are comprised of a single bit:

   >>> class Color(Flag):
   ...     RED = auto()
   ...     GREEN = auto()
   ...     BLUE = auto()
   ...     MAGENTA = RED | BLUE
   ...     YELLOW = RED | GREEN
   ...     CYAN = GREEN | BLUE
   ...
   >>> Color(3)  # named combination
   <Color.YELLOW: 3>
   >>> Color(7)      # not named combination
   <Color.RED|GREEN|BLUE: 7>


"Flag" and "IntFlag" minutia
----------------------------

Using the following snippet for our examples:

   >>> class Color(IntFlag):
   ...     BLACK = 0
   ...     RED = 1
   ...     GREEN = 2
   ...     BLUE = 4
   ...     PURPLE = RED | BLUE
   ...     WHITE = RED | GREEN | BLUE
   ...

the following are true:

* single-bit flags are canonical

* multi-bit and zero-bit flags are aliases

* only canonical flags are returned during iteration:

     >>> list(Color.WHITE)
     [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 4>]

* negating a flag or flag set returns a new flag/flag set with the
  corresponding positive integer value:

     >>> Color.BLUE
     <Color.BLUE: 4>

     >>> ~Color.BLUE
     <Color.RED|GREEN: 3>

* names of pseudo-flags are constructed from their members' names:

     >>> (Color.RED | Color.GREEN).name
     'RED|GREEN'

     >>> class Perm(IntFlag):
     ...     R = 4
     ...     W = 2
     ...     X = 1
     ...
     >>> (Perm.R & Perm.W).name is None  # effectively Perm(0)
     True

* multi-bit flags, aka aliases, can be returned from operations:

     >>> Color.RED | Color.BLUE
     <Color.PURPLE: 5>

     >>> Color(7)  # or Color(-1)
     <Color.WHITE: 7>

     >>> Color(0)
     <Color.BLACK: 0>

* membership / containment checking: zero-valued flags are always
  considered to be contained:

     >>> Color.BLACK in Color.WHITE
     True

  otherwise, only if all bits of one flag are in the other flag will
  True be returned:

     >>> Color.PURPLE in Color.WHITE
     True

     >>> Color.GREEN in Color.PURPLE
     False

There is a new boundary mechanism that controls how out-of-range /
invalid bits are handled: "STRICT", "CONFORM", "EJECT", and "KEEP":

* STRICT --> raises an exception when presented with invalid values

* CONFORM --> discards any invalid bits

* EJECT --> lose Flag status and become a normal int with the given
  value

* KEEP --> keep the extra bits

  * keeps Flag status and extra bits

  * extra bits do not show up in iteration

  * extra bits do show up in repr() and str()

The default for Flag is "STRICT", the default for "IntFlag" is
"EJECT", and the default for "_convert_" is "KEEP" (see "ssl.Options"
for an example of when "KEEP" is needed).


How are Enums and Flags different?
==================================

Enums have a custom metaclass that affects many aspects of both
derived "Enum" classes and their instances (members).


Enum Classes
------------

The "EnumType" metaclass is responsible for providing the
"__contains__()", "__dir__()", "__iter__()" and other methods that
allow one to do things with an "Enum" class that fail on a typical
class, such as "list(Color)" or "some_enum_var in Color".  "EnumType"
is responsible for ensuring that various other methods on the final
"Enum" class are correct (such as "__new__()", "__getnewargs__()",
"__str__()" and "__repr__()").


Flag Classes
------------

Flags have an expanded view of aliasing: to be canonical, the value of
a flag needs to be a power-of-two value, and not a duplicate name.
So, in addition to the "Enum" definition of alias, a flag with no
value (a.k.a. "0") or with more than one power-of-two value (e.g. "3")
is considered an alias.


Enum Members (aka instances)
----------------------------

The most interesting thing about enum members is that they are
singletons. "EnumType" creates them all while it is creating the enum
class itself, and then puts a custom "__new__()" in place to ensure
that no new ones are ever instantiated by returning only the existing
member instances.


Flag Members
------------

Flag members can be iterated over just like the "Flag" class, and only
the canonical members will be returned.  For example:

   >>> list(Color)
   [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 4>]

(Note that "BLACK", "PURPLE", and "WHITE" do not show up.)

Inverting a flag member returns the corresponding positive value,
rather than a negative value --- for example:

   >>> ~Color.RED
   <Color.GREEN|BLUE: 6>

Flag members have a length corresponding to the number of power-of-two
values they contain.  For example:

   >>> len(Color.PURPLE)
   2


Enum Cookbook
=============

While "Enum", "IntEnum", "StrEnum", "Flag", and "IntFlag" are expected
to cover the majority of use-cases, they cannot cover them all.  Here
are recipes for some different types of enumerations that can be used
directly, or as examples for creating one's own.


Omitting values
---------------

In many use-cases, one doesn't care what the actual value of an
enumeration is. There are several ways to define this type of simple
enumeration:

* use instances of "auto" for the value

* use instances of "object" as the value

* use a descriptive string as the value

* use a tuple as the value and a custom "__new__()" to replace the
  tuple with an "int" value

Using any of these methods signifies to the user that these values are
not important, and also enables one to add, remove, or reorder members
without having to renumber the remaining members.


Using "auto"
~~~~~~~~~~~~

Using "auto" would look like:

   >>> class Color(Enum):
   ...     RED = auto()
   ...     BLUE = auto()
   ...     GREEN = auto()
   ...
   >>> Color.GREEN
   <Color.GREEN: 3>


Using "object"
~~~~~~~~~~~~~~

Using "object" would look like:

   >>> class Color(Enum):
   ...     RED = object()
   ...     GREEN = object()
   ...     BLUE = object()
   ...
   >>> Color.GREEN
   <Color.GREEN: <object object at 0x...>>

This is also a good example of why you might want to write your own
"__repr__()":

   >>> class Color(Enum):
   ...     RED = object()
   ...     GREEN = object()
   ...     BLUE = object()
   ...     def __repr__(self):
   ...         return "<%s.%s>" % (self.__class__.__name__, self._name_)
   ...
   >>> Color.GREEN
   <Color.GREEN>


Using a descriptive string
~~~~~~~~~~~~~~~~~~~~~~~~~~

Using a string as the value would look like:

   >>> class Color(Enum):
   ...     RED = 'stop'
   ...     GREEN = 'go'
   ...     BLUE = 'too fast!'
   ...
   >>> Color.GREEN
   <Color.GREEN: 'go'>


Using a custom "__new__()"
~~~~~~~~~~~~~~~~~~~~~~~~~~

Using an auto-numbering "__new__()" would look like:

   >>> class AutoNumber(Enum):
   ...     def __new__(cls):
   ...         value = len(cls.__members__) + 1
   ...         obj = object.__new__(cls)
   ...         obj._value_ = value
   ...         return obj
   ...
   >>> class Color(AutoNumber):
   ...     RED = ()
   ...     GREEN = ()
   ...     BLUE = ()
   ...
   >>> Color.GREEN
   <Color.GREEN: 2>

To make a more general purpose "AutoNumber", add "*args" to the
signature:

   >>> class AutoNumber(Enum):
   ...     def __new__(cls, *args):      # this is the only change from above
   ...         value = len(cls.__members__) + 1
   ...         obj = object.__new__(cls)
   ...         obj._value_ = value
   ...         return obj
   ...

Then when you inherit from "AutoNumber" you can write your own
"__init__" to handle any extra arguments:

   >>> class Swatch(AutoNumber):
   ...     def __init__(self, pantone='unknown'):
   ...         self.pantone = pantone
   ...     AUBURN = '3497'
   ...     SEA_GREEN = '1246'
   ...     BLEACHED_CORAL = () # New color, no Pantone code yet!
   ...
   >>> Swatch.SEA_GREEN
   <Swatch.SEA_GREEN: 2>
   >>> Swatch.SEA_GREEN.pantone
   '1246'
   >>> Swatch.BLEACHED_CORAL.pantone
   'unknown'

Nota:

  The "__new__()" method, if defined, is used during creation of the
  Enum members; it is then replaced by Enum's "__new__()" which is
  used after class creation for lookup of existing members.

Aviso:

  *Do not* call "super().__new__()", as the lookup-only "__new__" is
  the one that is found; instead, use the data type directly -- e.g.:

     obj = int.__new__(cls, value)


OrderedEnum
-----------

An ordered enumeration that is not based on "IntEnum" and so maintains
the normal "Enum" invariants (such as not being comparable to other
enumerations):

   >>> class OrderedEnum(Enum):
   ...     def __ge__(self, other):
   ...         if self.__class__ is other.__class__:
   ...             return self.value >= other.value
   ...         return NotImplemented
   ...     def __gt__(self, other):
   ...         if self.__class__ is other.__class__:
   ...             return self.value > other.value
   ...         return NotImplemented
   ...     def __le__(self, other):
   ...         if self.__class__ is other.__class__:
   ...             return self.value <= other.value
   ...         return NotImplemented
   ...     def __lt__(self, other):
   ...         if self.__class__ is other.__class__:
   ...             return self.value < other.value
   ...         return NotImplemented
   ...
   >>> class Grade(OrderedEnum):
   ...     A = 5
   ...     B = 4
   ...     C = 3
   ...     D = 2
   ...     F = 1
   ...
   >>> Grade.C < Grade.A
   True


DuplicateFreeEnum
-----------------

Raises an error if a duplicate member value is found instead of
creating an alias:

   >>> class DuplicateFreeEnum(Enum):
   ...     def __init__(self, *args):
   ...         cls = self.__class__
   ...         if any(self.value == e.value for e in cls):
   ...             a = self.name
   ...             e = cls(self.value).name
   ...             raise ValueError(
   ...                 "aliases not allowed in DuplicateFreeEnum:  %r --> %r"
   ...                 % (a, e))
   ...
   >>> class Color(DuplicateFreeEnum):
   ...     RED = 1
   ...     GREEN = 2
   ...     BLUE = 3
   ...     GRENE = 2
   ...
   Traceback (most recent call last):
     ...
   ValueError: aliases not allowed in DuplicateFreeEnum:  'GRENE' --> 'GREEN'

Nota:

  This is a useful example for subclassing Enum to add or change other
  behaviors as well as disallowing aliases.  If the only desired
  change is disallowing aliases, the "unique()" decorator can be used
  instead.


MultiValueEnum
--------------

Supports having more than one value per member:

   >>> class MultiValueEnum(Enum):
   ...     def __new__(cls, value, *values):
   ...         self = object.__new__(cls)
   ...         self._value_ = value
   ...         for v in values:
   ...             self._add_value_alias_(v)
   ...         return self
   ...
   >>> class DType(MultiValueEnum):
   ...     float32 = 'f', 8
   ...     double64 = 'd', 9
   ...
   >>> DType('f')
   <DType.float32: 'f'>
   >>> DType(9)
   <DType.double64: 'd'>


Planet
------

If "__new__()" or "__init__()" is defined, the value of the enum
member will be passed to those methods:

   >>> class Planet(Enum):
   ...     MERCURY = (3.303e+23, 2.4397e6)
   ...     VENUS   = (4.869e+24, 6.0518e6)
   ...     EARTH   = (5.976e+24, 6.37814e6)
   ...     MARS    = (6.421e+23, 3.3972e6)
   ...     JUPITER = (1.9e+27,   7.1492e7)
   ...     SATURN  = (5.688e+26, 6.0268e7)
   ...     URANUS  = (8.686e+25, 2.5559e7)
   ...     NEPTUNE = (1.024e+26, 2.4746e7)
   ...     def __init__(self, mass, radius):
   ...         self.mass = mass       # in kilograms
   ...         self.radius = radius   # in meters
   ...     @property
   ...     def surface_gravity(self):
   ...         # universal gravitational constant  (m3 kg-1 s-2)
   ...         G = 6.67300E-11
   ...         return G * self.mass / (self.radius * self.radius)
   ...
   >>> Planet.EARTH.value
   (5.976e+24, 6378140.0)
   >>> Planet.EARTH.surface_gravity
   9.802652743337129


TimePeriod
----------

An example to show the "_ignore_" attribute in use:

   >>> import datetime as dt
   >>> class Period(dt.timedelta, Enum):
   ...     "different lengths of time"
   ...     _ignore_ = 'Period i'
   ...     Period = vars()
   ...     for i in range(367):
   ...         Period['day_%d' % i] = i
   ...
   >>> list(Period)[:2]
   [<Period.day_0: datetime.timedelta(0)>, <Period.day_1: datetime.timedelta(days=1)>]
   >>> list(Period)[-2:]
   [<Period.day_365: datetime.timedelta(days=365)>, <Period.day_366: datetime.timedelta(days=366)>]


Subclassing EnumType
====================

While most enum needs can be met by customizing "Enum" subclasses,
either with class decorators or custom functions, "EnumType" can be
subclassed to provide a different Enum experience.
