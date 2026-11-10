"enum" --- Suporte a enumerações
********************************

Adicionado na versão 3.4.

**Código-fonte:** Lib/enum.py


Important
^^^^^^^^^

Esta página contêm informação de referência da API. Para informação
tutorial e discussão de tópicos mais avançados, consulte

* Tutorial básico

* Tutorial avançado

* Livro de receitas de enum

======================================================================

Uma enumeração:

* é um conjunto de nomes simbólicos (membros) vinculados a valores
  únicos

* pode ser iterado para retornar seus membros canônicos (ou seja, não
  incluindo apelidos) na ordem de definição

* usa a sintaxe *call* para retornar membros por valor

* usa a sintaxe *index* para retornar membros por nome

As enumerações são criadas usando a sintaxe de "class" ou usando a
sintaxe de chamada de função:

   >>> from enum import Enum

   >>> # sintaxe de classe
   >>> class Color(Enum):
   ...     RED = 1
   ...     GREEN = 2
   ...     BLUE = 3

   >>> # sintaxe funcional
   >>> Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])

Embora possamos usar a sintaxe "class" para criar Enums, Enums não são
classes Python normais. Veja Como Enums são diferentes? para mais
detalhes.

Nota:

  Nomenclatura

  * A classe "Color" é uma *enumeração* (ou *enum*)

  * Os atributos "Color.RED", "Color.GREEN", etc., são *membros de
    enumeração* (ou *membros*) e são constantes funcionalmente.

  * Os membros enum têm *nomes* e *valores* (o nome de "Color.RED" é
    "RED", o valor de "Color.BLUE" é "3", etc.)

======================================================================


Conteúdo do módulo
==================

   "EnumType"

      O "type" para Enum e suas subclasses.

   "Enum"

      Classe base para criação de constantes enumeradas.

   "IntEnum"

      Classe base para criar constantes enumeradas que também são
      subclasses de "int". (Notas)

   "StrEnum"

      Classe base para criar constantes enumeradas que também são
      subclasses de "str". (Notas)

   "Flag"

      Classe base para criar constantes enumeradas que podem ser
      combinadas usando operações bit a bit sem perder sua associação
      "Flag".

   "IntFlag"

      Classe base para criar constantes enumeradas que podem ser
      combinadas usando operadores bit a bit sem perder sua associação
      "IntFlag". Membros de "IntFlag" também são subclasses de "int".
      (Notas)

   "ReprEnum"

      Usado por "IntEnum", "StrEnum" e "IntFlag" para manter o "str()"
      do tipo misto.

   "EnumCheck"

      Uma enumeração com os valores "CONTINUOUS", "NAMED_FLAGS" e
      "UNIQUE", para uso com "verify()" para garantir que várias
      restrições sejam atendidas por uma determinada enumeração.

   "FlagBoundary"

      Uma enumeração com os valores "STRICT", "CONFORM", "EJECT" e
      "KEEP" que permite um controle mais refinado sobre como valores
      inválidos são tratados em uma enumeração.

   "EnumDict"

      Uma subclasse de "dict" para uso ao criar subclasse de
      "EnumType".

   "auto"

      As instâncias são substituídas por um valor apropriado para
      membros Enum. "StrEnum" assume como padrão a versão em
      minúsculas do nome do membro, enquanto outros Enums assumem como
      padrão 1 e aumentam a partir daí.

   "@~enum.property"

      Permite que membros "Enum" tenham atributos sem conflitar com
      nomes de membros. Os atributos "value" e "name" são
      implementados dessa forma.

   "@unique"

      Decorador de classe Enum que garante que apenas um nome seja
      vinculado a cada valor.

   "@verify"

      Decorador de classe Enum que verifica restrições selecionáveis
      pelo usuário em uma enumeração.

   "@member"

      Torna "obj" um membro. Pode ser usado como um decorador.

   "@nonmember"

      Não torna "obj" um membro. Pode ser usado como um decorador.

   "@global_enum"

      Modifica "str()" e "repr()" de uma enumeração para mostrar seus
      membros como pertencentes ao módulo em vez de sua classe, e
      exporta os membros da enumeração para o espaço de nomes global.

   "show_flag_values()"

      Retorna uma lista de todos os inteiros de potência de dois
      contidos em um sinalizador.

   "enum.bin()"

      Like built-in "bin()", except negative values are represented in
      two's complement, and the leading bit always indicates sign ("0"
      implies positive, "1" implies negative).

Adicionado na versão 3.6: "Flag", "IntFlag", "auto"

Adicionado na versão 3.11: "StrEnum", "EnumCheck", "ReprEnum",
"FlagBoundary", "property", "member", "nonmember", "global_enum",
"show_flag_values"

Adicionado na versão 3.13: "EnumDict"

======================================================================


Data types
==========

class enum.EnumType

   *EnumType* é a *metaclasse* para enumerações *enum*. É possível
   criar subclasse de *EnumType* -- veja Criando subclasses de
   EnumType para detalhes.

   "EnumType" é responsável por definir os métodos "__repr__()",
   "__str__()", "__format__()" e "__reduce__()" corretos no *enum*
   final, bem como criar os membros do enum, manipular adequadamente
   as duplicatas, fornecer iteração sobre a classe do enum, etc.

   Adicionado na versão 3.11: Antes da versão 3.11, "EnumType" era
   chamado de "EnumMeta", que ainda está disponível como um apelido.

   __call__(cls, value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

      Este método é chamado de formas diferentes:

      * para procurar um membro existente:

           cls:
              A classe enum sendo chamada.

           value:
              O valor para procurar.

      * para usar a enumeração "cls" para criar uma nova enumeração
        (somente se a enumeração existente não tiver nenhum membro):

           cls:
              A classe enum sendo chamada.

           value:
              O nome do novo Enum para criar.

           names:
              Os nomes/valores dos membros para o novo Enum.

           module:
              O nome do módulo no qual o novo Enum é criado.

           qualname:
              O local real no módulo onde este Enum pode ser
              encontrado.

           type:
              Um tipo de mix-in para o novo Enum.

           start:
              O primeiro valor inteiro para o Enum (usado por "auto").

           boundary:
              Como lidar com valores fora do intervalo de operações de
              bits (somente "Flag").

   __contains__(cls, member)

      Retorna "True" se o membro pertencer a "cls":

         >>> some_var = Color.RED
         >>> some_var in Color
         True
         >>> Color.RED.value in Color
         True

      Alterado na versão 3.12: Antes do Python 3.12, um "TypeError"
      era levantado se um membro não Enum fosse usado em uma
      verificação de contenção.

   __dir__(cls)

      Retorna "['__class__', '__doc__', '__members__', '__module__']"
      e os nomes dos membros em *cls*:

         >>> dir(Color)
         ['BLUE', 'GREEN', 'RED', '__class__', '__contains__', '__doc__', '__getitem__', '__init_subclass__', '__iter__', '__len__', '__members__', '__module__', '__name__', '__qualname__']

   __getitem__(cls, name)

      Retorna o membro Enum em *cls* correspondente a *name* ou
      levanta "KeyError":

         >>> Color['BLUE']
         <Color.BLUE: 3>

   __iter__(cls)

      Retorna cada membro em *cls* na ordem de definição:

         >>> list(Color)
         [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

   __len__(cls)

      Returns the number of members in *cls*:

         >>> len(Color)
         3

   __members__

      Retorna um mapeamento de cada nome de enumeração para seu
      membro, incluindo apelidos

   __reversed__(cls)

      Retorna cada membro em *cls* na ordem inversa de definição:

         >>> list(reversed(Color))
         [<Color.BLUE: 3>, <Color.GREEN: 2>, <Color.RED: 1>]

class enum.Enum

   *Enum* é a classe base para todas as enumerações *enum*.

   name

      O nome usado para definir o membro "Enum":

         >>> Color.BLUE.name
         'BLUE'

   value

      O valor dado ao membro "Enum":

         >>> Color.RED.value
         1

      O valor do membro pode ser definido em "__new__()".

      Nota:

        Valores de membros de EnumOs valores dos membros podem ser
        qualquer coisa: "int", "str", etc. Se o valor exato não for
        importante, você pode usar instâncias de "auto" e um valor
        apropriado será escolhido para você. Consulte "auto" para
        obter detalhes.Embora valores mutáveis/não hasheáveis, como
        "dict", "list" ou um mutável "dataclass", possam ser usados,
        eles terão um impacto quadrático no desempenho durante a
        criação em relação ao número total de valores mutáveis/não
        hasheáveis na enumeração.

   _name_

      Nome do membro.

   _value_

      O valor do membro pode ser definido em "__new__()".

   _order_

      Não é mais usado, mantido para compatibilidade com versões
      anteriores. (atributo de classe, removido durante a criação da
      classe).

      The "_order_" attribute can be provided to help keep Python 2 /
      Python 3 code in sync. It will be checked against the actual
      order of the enumeration and raise an error if the two do not
      match:

         >>> class Color(Enum):
         ...     _order_ = 'RED GREEN BLUE'
         ...     RED = 1
         ...     BLUE = 3
         ...     GREEN = 2
         ...
         Traceback (most recent call last):
         ...
         TypeError: member order does not match _order_:
            ['RED', 'BLUE', 'GREEN']
            ['RED', 'GREEN', 'BLUE']

      Nota:

        In Python 2 code the "_order_" attribute is necessary as
        definition order is lost before it can be recorded.

      Adicionado na versão 3.6.

   _ignore_

      "_ignore_" é usado somente durante a criação e é removido da
      enumeração quando a criação é concluída.

      "_ignore_" é uma lista de nomes que não se tornarão membros e
      cujos nomes também serão removidos da enumeração concluída. Veja
      TimePeriod para um exemplo.

      Adicionado na versão 3.7.

   __dir__(self)

      Retorna "['__class__', '__doc__', '__module__', 'name',
      'value']" e quaisquer métodos públicos definidos em
      *self.__class__*:

         >>> from enum import Enum
         >>> import datetime as dt
         >>> class Weekday(Enum):
         ...     MONDAY = 1
         ...     TUESDAY = 2
         ...     WEDNESDAY = 3
         ...     THURSDAY = 4
         ...     FRIDAY = 5
         ...     SATURDAY = 6
         ...     SUNDAY = 7
         ...     @classmethod
         ...     def today(cls):
         ...         print(f'today is {cls(dt.date.today().isoweekday()).name}')
         ...
         >>> dir(Weekday.SATURDAY)
         ['__class__', '__doc__', '__eq__', '__hash__', '__module__', 'name', 'today', 'value']

   _generate_next_value_(name, start, count, last_values)

         nome:
            O nome do membro que está sendo definido (por exemplo,
            'RED').

         start:
            O valor inicial do Enum; o padrão é 1.

         count:
            O número de membros atualmente definido, sem incluir este.

         last_values:
            Uma lista de valores anteriores.

      A *staticmethod* that is used to determine the next value
      returned by "auto".

      Nota:

        For standard "Enum" classes the next value chosen is the
        highest value seen incremented by one.For "Flag" classes the
        next value chosen will be the next highest power-of-two.

      This method may be overridden, e.g.:

         >>> from enum import auto, Enum
         >>> class PowersOfThree(Enum):
         ...     @staticmethod
         ...     def _generate_next_value_(name, start, count, last_values):
         ...         return 3 ** (count + 1)
         ...     FIRST = auto()
         ...     SECOND = auto()
         ...
         >>> PowersOfThree.SECOND.value
         9

      Adicionado na versão 3.6.

      Alterado na versão 3.13: Versões anteriores usariam o último
      valor visualizado em vez do maior valor.

   __init__(self, *args, **kwds)

      Por padrão, não faz nada. Se vários valores forem fornecidos na
      atribuição de membro, esses valores se tornarão argumentos
      separados para "__init__"; por exemplo.:

      >>> from enum import Enum
      >>> class Weekday(Enum):
      ...     MONDAY = 1, 'Mon'

      "Weekday.__init__()" seria chamado como "Weekday.__init__(self,
      1, 'Mon')"

   __init_subclass__(cls, **kwds)

      Um *classmethod* usado para configurar subclasses subsequentes.
      Por padrão, não faz nada.

   _missing_(cls, value)

      Um *classmethod* para procurar valores não encontrados em *cls*.
      Por padrão, ele não faz nada, mas pode ser substituído para
      implementar um comportamento de pesquisa personalizado:

         >>> from enum import auto, StrEnum
         >>> class Build(StrEnum):
         ...     DEBUG = auto()
         ...     OPTIMIZED = auto()
         ...     @classmethod
         ...     def _missing_(cls, value):
         ...         value = value.lower()
         ...         for member in cls:
         ...             if member.value == value:
         ...                 return member
         ...         return None
         ...
         >>> Build.DEBUG.value
         'debug'
         >>> Build('deBUG')
         <Build.DEBUG: 'debug'>

      Adicionado na versão 3.6.

   __new__(cls, *args, **kwds)

      By default, doesn't exist.  If specified, either in the enum
      class definition or in a mixin class (such as "int"), all values
      given in the member assignment will be passed; e.g.

      >>> from enum import Enum
      >>> class MyIntEnum(int, Enum):
      ...     TWENTYSIX = '1a', 16

      results in the call "int('1a', 16)" and a value of "26" for the
      member.

      Nota:

        When writing a custom "__new__", do not use "super().__new__"
        -- call the appropriate "__new__" instead.

   __repr__(self)

      Returns the string used for *repr()* calls.  By default, returns
      the *Enum* name, member name, and value, but can be overridden:

         >>> from enum import auto, Enum
         >>> class OtherStyle(Enum):
         ...     ALTERNATE = auto()
         ...     OTHER = auto()
         ...     SOMETHING_ELSE = auto()
         ...     def __repr__(self):
         ...         cls_name = self.__class__.__name__
         ...         return f'{cls_name}.{self.name}'
         ...
         >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
         (OtherStyle.ALTERNATE, 'OtherStyle.ALTERNATE', 'OtherStyle.ALTERNATE')

   __str__(self)

      Returns the string used for *str()* calls.  By default, returns
      the *Enum* name and member name, but can be overridden:

         >>> from enum import auto, Enum
         >>> class OtherStyle(Enum):
         ...     ALTERNATE = auto()
         ...     OTHER = auto()
         ...     SOMETHING_ELSE = auto()
         ...     def __str__(self):
         ...         return f'{self.name}'
         ...
         >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
         (<OtherStyle.ALTERNATE: 1>, 'ALTERNATE', 'ALTERNATE')

   __format__(self)

      Returns the string used for *format()* and *f-string* calls.  By
      default, returns "__str__()" return value, but can be
      overridden:

         >>> from enum import auto, Enum
         >>> class OtherStyle(Enum):
         ...     ALTERNATE = auto()
         ...     OTHER = auto()
         ...     SOMETHING_ELSE = auto()
         ...     def __format__(self, spec):
         ...         return f'{self.name}'
         ...
         >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}"
         (<OtherStyle.ALTERNATE: 1>, 'OtherStyle.ALTERNATE', 'ALTERNATE')

   Nota:

     Using "auto" with "Enum" results in integers of increasing value,
     starting with "1".

   Alterado na versão 3.12: Added Suporte a dataclass.

   _add_alias_()

      Adds a new name as an alias to an existing member:

         >>> Color.RED._add_alias_("ERROR")
         >>> Color.ERROR
         <Color.RED: 1>

      Raises a "NameError" if the name is already assigned to a
      different member.

      Adicionado na versão 3.13.

   _add_value_alias_()

      Adds a new value as an alias to an existing member:

         >>> Color.RED._add_value_alias_(42)
         >>> Color(42)
         <Color.RED: 1>

         Raises a "ValueError" if the value is already linked with a different member.
         See MultiValueEnum for an example.

      Adicionado na versão 3.13.

class enum.IntEnum

   *IntEnum* is the same as "Enum", but its members are also integers
   and can be used anywhere that an integer can be used.  If any
   integer operation is performed with an *IntEnum* member, the
   resulting value loses its enumeration status.

   >>> from enum import IntEnum
   >>> class Number(IntEnum):
   ...     ONE = 1
   ...     TWO = 2
   ...     THREE = 3
   ...
   >>> Number.THREE
   <Number.THREE: 3>
   >>> Number.ONE + Number.TWO
   3
   >>> Number.THREE + 5
   8
   >>> Number.THREE == 3
   True

   Nota:

     Using "auto" with "IntEnum" results in integers of increasing
     value, starting with "1".

   Alterado na versão 3.11: "__str__()" is now "int.__str__()" to
   better support the *replacement of existing constants* use-case.
   "__format__()" was already "int.__format__()" for that same reason.

class enum.StrEnum

   *StrEnum* is the same as "Enum", but its members are also strings
   and can be used in most of the same places that a string can be
   used. The result of any string operation performed on or with a
   *StrEnum* member is not part of the enumeration.

   >>> from enum import StrEnum, auto
   >>> class Color(StrEnum):
   ...     RED = 'r'
   ...     GREEN = 'g'
   ...     BLUE = 'b'
   ...     UNKNOWN = auto()
   ...
   >>> Color.RED
   <Color.RED: 'r'>
   >>> Color.UNKNOWN
   <Color.UNKNOWN: 'unknown'>
   >>> str(Color.UNKNOWN)
   'unknown'

   Nota:

     There are places in the stdlib that check for an exact "str"
     instead of a "str" subclass (i.e. "type(unknown) == str" instead
     of "isinstance(unknown, str)"), and in those locations you will
     need to use "str(MyStrEnum.MY_MEMBER)".

   Nota:

     Using "auto" with "StrEnum" results in the lower-cased member
     name as the value.

   Nota:

     "__str__()" is "str.__str__()" to better support the *replacement
     of existing constants* use-case.  "__format__()" is likewise
     "str.__format__()" for that same reason.

   Adicionado na versão 3.11.

class enum.Flag

   "Flag" is the same as "Enum", but its members support the bitwise
   operators "&" (*AND*), "|" (*OR*), "^" (*XOR*), and "~" (*INVERT*);
   the results of those operations are (aliases of) members of the
   enumeration.

   __contains__(self, value)

      Returns *True* if value is in self:

         >>> from enum import Flag, auto
         >>> class Color(Flag):
         ...     RED = auto()
         ...     GREEN = auto()
         ...     BLUE = auto()
         ...
         >>> purple = Color.RED | Color.BLUE
         >>> white = Color.RED | Color.GREEN | Color.BLUE
         >>> Color.GREEN in purple
         False
         >>> Color.GREEN in white
         True
         >>> purple in white
         True
         >>> white in purple
         False

   __iter__(self)

      Returns all contained non-alias members:

         >>> list(Color.RED)
         [<Color.RED: 1>]
         >>> list(purple)
         [<Color.RED: 1>, <Color.BLUE: 4>]

      Adicionado na versão 3.11.

   __len__(self)

      Returns number of members in flag:

         >>> len(Color.GREEN)
         1
         >>> len(white)
         3

      Adicionado na versão 3.11.

   __bool__(self)

      Returns *True* if any members in flag, *False* otherwise:

         >>> bool(Color.GREEN)
         True
         >>> bool(white)
         True
         >>> black = Color(0)
         >>> bool(black)
         False

   __or__(self, other)

      Returns current flag binary or'ed with other:

         >>> Color.RED | Color.GREEN
         <Color.RED|GREEN: 3>

   __and__(self, other)

      Returns current flag binary and'ed with other:

         >>> purple & white
         <Color.RED|BLUE: 5>
         >>> purple & Color.GREEN
         <Color: 0>

   __xor__(self, other)

      Returns current flag binary xor'ed with other:

         >>> purple ^ white
         <Color.GREEN: 2>
         >>> purple ^ Color.GREEN
         <Color.RED|GREEN|BLUE: 7>

   __invert__(self)

      Returns all the flags in *type(self)* that are not in *self*:

         >>> ~white
         <Color: 0>
         >>> ~purple
         <Color.GREEN: 2>
         >>> ~Color.RED
         <Color.GREEN|BLUE: 6>

   _numeric_repr_()

      Function used to format any remaining unnamed numeric values.
      Default is the value's repr; common choices are "hex()" and
      "oct()".

   Nota:

     Using "auto" with "Flag" results in integers that are powers of
     two, starting with "1".

   Alterado na versão 3.11: The *repr()* of zero-valued flags has
   changed.  It is now:

   >>> Color(0)
   <Color: 0>

class enum.IntFlag

   "IntFlag" is the same as "Flag", but its members are also integers
   and can be used anywhere that an integer can be used.

   >>> from enum import IntFlag, auto
   >>> class Color(IntFlag):
   ...     RED = auto()
   ...     GREEN = auto()
   ...     BLUE = auto()
   ...
   >>> Color.RED & 2
   <Color: 0>
   >>> Color.RED | 2
   <Color.RED|GREEN: 3>

   If any integer operation is performed with an *IntFlag* member, the
   result is not an *IntFlag*:

      >>> Color.RED + 2
      3

   If a "Flag" operation is performed with an *IntFlag* member and:

   * the result is a valid *IntFlag*: an *IntFlag* is returned

   * the result is not a valid *IntFlag*: the result depends on the
     "FlagBoundary" setting

   The "repr()" of unnamed zero-valued flags has changed.  It is now:

      >>> Color(0)
      <Color: 0>

   Nota:

     Using "auto" with "IntFlag" results in integers that are powers
     of two, starting with "1".

   Alterado na versão 3.11: "__str__()" is now "int.__str__()" to
   better support the *replacement of existing constants* use-case.
   "__format__()" was already "int.__format__()" for that same
   reason.Inversion of an "IntFlag" now returns a positive value that
   is the union of all flags not in the given flag, rather than a
   negative value. This matches the existing "Flag" behavior.

class enum.ReprEnum

   "ReprEnum" uses the "repr()" of "Enum", but the "str()" of the
   mixed-in data type:

   * "int.__str__()" for "IntEnum" and "IntFlag"

   * "str.__str__()" for "StrEnum"

   Inherit from "ReprEnum" to keep the "str()" / "format()" of the
   mixed-in data type instead of using the "Enum"-default "str()".

   Adicionado na versão 3.11.

class enum.EnumCheck

   *EnumCheck* contains the options used by the "verify()" decorator
   to ensure various constraints; failed constraints result in a
   "ValueError".

   UNIQUE

      Ensure that each value has only one name:

         >>> from enum import Enum, verify, UNIQUE
         >>> @verify(UNIQUE)
         ... class Color(Enum):
         ...     RED = 1
         ...     GREEN = 2
         ...     BLUE = 3
         ...     CRIMSON = 1
         Traceback (most recent call last):
         ...
         ValueError: aliases found in <enum 'Color'>: CRIMSON -> RED

   CONTINUOUS

      Ensure that there are no missing values between the lowest-
      valued member and the highest-valued member:

         >>> from enum import Enum, verify, CONTINUOUS
         >>> @verify(CONTINUOUS)
         ... class Color(Enum):
         ...     RED = 1
         ...     GREEN = 2
         ...     BLUE = 5
         Traceback (most recent call last):
         ...
         ValueError: invalid enum 'Color': missing values 3, 4

   NAMED_FLAGS

      Ensure that any flag groups/masks contain only named flags --
      useful when values are specified instead of being generated by
      "auto()":

         >>> from enum import Flag, verify, NAMED_FLAGS
         >>> @verify(NAMED_FLAGS)
         ... class Color(Flag):
         ...     RED = 1
         ...     GREEN = 2
         ...     BLUE = 4
         ...     WHITE = 15
         ...     NEON = 31
         Traceback (most recent call last):
         ...
         ValueError: invalid Flag 'Color': aliases WHITE and NEON are missing combined values of 0x18 [use enum.show_flag_values(value) for details]

   Nota:

     CONTINUOUS and NAMED_FLAGS are designed to work with integer-
     valued members.

   Adicionado na versão 3.11.

class enum.FlagBoundary

   "FlagBoundary" controls how out-of-range values are handled in
   "Flag" and its subclasses.

   STRICT

      Out-of-range values cause a "ValueError" to be raised. This is
      the default for "Flag":

         >>> from enum import Flag, STRICT, auto
         >>> class StrictFlag(Flag, boundary=STRICT):
         ...     RED = auto()
         ...     GREEN = auto()
         ...     BLUE = auto()
         ...
         >>> StrictFlag(2**2 + 2**4)
         Traceback (most recent call last):
         ...
         ValueError: <flag 'StrictFlag'> invalid value 20
             given 0b0 10100
           allowed 0b0 00111

   CONFORM

      Out-of-range values have invalid values removed, leaving a valid
      "Flag" value:

         >>> from enum import Flag, CONFORM, auto
         >>> class ConformFlag(Flag, boundary=CONFORM):
         ...     RED = auto()
         ...     GREEN = auto()
         ...     BLUE = auto()
         ...
         >>> ConformFlag(2**2 + 2**4)
         <ConformFlag.BLUE: 4>

   EJECT

      Out-of-range values lose their "Flag" membership and revert to
      "int".

      >>> from enum import Flag, EJECT, auto
      >>> class EjectFlag(Flag, boundary=EJECT):
      ...     RED = auto()
      ...     GREEN = auto()
      ...     BLUE = auto()
      ...
      >>> EjectFlag(2**2 + 2**4)
      20

   KEEP

      Out-of-range values are kept, and the "Flag" membership is kept.
      This is the default for "IntFlag":

         >>> from enum import Flag, KEEP, auto
         >>> class KeepFlag(Flag, boundary=KEEP):
         ...     RED = auto()
         ...     GREEN = auto()
         ...     BLUE = auto()
         ...
         >>> KeepFlag(2**2 + 2**4)
         <KeepFlag.BLUE|16: 20>

   Adicionado na versão 3.11.

class enum.EnumDict

   *EnumDict* is a subclass of "dict" that is used as the namespace
   for defining enum classes (see Preparando o espaço de nomes da
   classe). It is exposed to allow subclasses of "EnumType" with
   advanced behavior like having multiple values per member. It should
   be called with the name of the enum class being created, otherwise
   private names and internal classes will not be handled correctly.

   Note that only the "MutableMapping" interface ("__setitem__()" and
   "update()") is overridden. It may be possible to bypass the checks
   using other "dict" operations like "|=".

   member_names

      A list of member names.

   Adicionado na versão 3.13.

======================================================================


Nomes "__dunder__" suportados
-----------------------------

"__members__" is a read-only ordered mapping of "member_name":"member"
items.  It is only available on the class.

"__new__()", if specified, must create and return the enum members; it
is also a very good idea to set the member's "_value_" appropriately.
Once all the members are created it is no longer used.


Nomes "_sunder_" suportados
---------------------------

* "_name_" -- name of the member

* "_value_" -- value of the member; can be set in "__new__"

* "_missing_()" -- a lookup function used when a value is not found;
  may be overridden

* "_ignore_" -- a list of names, either as a "list" or a "str", that
  will not be transformed into members, and will be removed from the
  final class

* "_order_" -- no longer used, kept for backward compatibility (class
  attribute, removed during class creation)

* "_generate_next_value_()" -- used to get an appropriate value for an
  enum member; may be overridden

* "_add_alias_()" -- adds a new name as an alias to an existing
  member.

* "_add_value_alias_()" -- adds a new value as an alias to an existing
  member.

* While "_sunder_" names are generally reserved for the further
  development of the "Enum" class and can not be used, some are
  explicitly allowed:

  * "_repr_*" (e.g. "_repr_html_"), as used in IPython's rich display

Adicionado na versão 3.6: "_missing_", "_order_",
"_generate_next_value_"

Adicionado na versão 3.7: "_ignore_"

Adicionado na versão 3.13: "_add_alias_", "_add_value_alias_",
"_repr_*"

======================================================================


Utilities and decorators
========================

class enum.auto

   *auto* can be used in place of a value.  If used, the *Enum*
   machinery will call an "Enum"'s "_generate_next_value_()" to get an
   appropriate value. For "Enum" and "IntEnum" that appropriate value
   will be the highest value seen plus one; for "Flag" and "IntFlag"
   it will be the first power-of-two greater than the highest value
   seen; for "StrEnum" it will be the lower-cased version of the
   member's name.  Care must be taken if mixing *auto()* with manually
   specified values.

   *auto* instances are only resolved when at the top level of an
   assignment, either by itself or as part of a tuple:

   * "FIRST = auto()" will work (auto() is replaced with "1");

   * "SECOND = auto(), -2" will work (auto is replaced with "2", so
     "2, -2" is used to create the "SECOND" enum member;

   * "THIRD = [auto(), -3]" will *not* work ("[<auto instance>, -3]"
     is used to create the "THIRD" enum member)

   Alterado na versão 3.11.1: In prior versions, "auto()" had to be
   the only thing on the assignment line to work properly.

   "_generate_next_value_" can be overridden to customize the values
   used by *auto*.

   Nota:

     In version 3.13 the default "_generate_next_value_" will always
     return the highest member value incremented by 1, and will fail
     if any member is an incompatible type.

@enum.property

   A decorator similar to the built-in "@property", but specifically
   for enumerations.  It allows member attributes to have the same
   names as members themselves.

   Nota:

     The *property* and the member must be defined in separate
     classes; for example, the *value* and *name* attributes are
     defined in the *Enum* class, and *Enum* subclasses can define
     members with the names "value" and "name".

   Adicionado na versão 3.11.

@enum.unique

   A "class" decorator specifically for enumerations.  It searches an
   enumeration's "__members__", gathering any aliases it finds; if any
   are found "ValueError" is raised with the details:

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

@enum.verify

   A "class" decorator specifically for enumerations.  Members from
   "EnumCheck" are used to specify which constraints should be checked
   on the decorated enumeration.

   Adicionado na versão 3.11.

@enum.member

   A decorator for use in enums: its target will become a member.

   Adicionado na versão 3.11.

@enum.nonmember

   A decorator for use in enums: its target will not become a member.

   Adicionado na versão 3.11.

@enum.global_enum

   A decorator to change the "str()" and "repr()" of an enum to show
   its members as belonging to the module instead of its class. Should
   only be used when the enum members are exported to the module
   global namespace (see "re.RegexFlag" for an example).

   Adicionado na versão 3.11.

enum.show_flag_values(value)

   Return a list of all power-of-two integers contained in a flag
   *value*.

   Adicionado na versão 3.11.

enum.bin(num, max_bits=None)

   Like built-in "bin()", except negative values are represented in
   two's complement, and the leading bit always indicates sign ("0"
   implies positive, "1" implies negative).

   >>> import enum
   >>> enum.bin(10)
   '0b0 1010'
   >>> enum.bin(~10)   # ~10 is -11
   '0b1 0101'

   Adicionado na versão 3.11.

======================================================================


Notas
=====

"IntEnum", "StrEnum", and "IntFlag"

   These three enum types are designed to be drop-in replacements for
   existing integer- and string-based values; as such, they have extra
   limitations:

   * "__str__" uses the value and not the name of the enum member

   * "__format__", because it uses "__str__", will also use the value
     of the enum member instead of its name

   If you do not need/want those limitations, you can either create
   your own base class by mixing in the "int" or "str" type yourself:

      >>> from enum import Enum
      >>> class MyIntEnum(int, Enum):
      ...     pass

   or you can reassign the appropriate "str()", etc., in your enum:

      >>> from enum import Enum, IntEnum
      >>> class MyIntEnum(IntEnum):
      ...     __str__ = Enum.__str__
