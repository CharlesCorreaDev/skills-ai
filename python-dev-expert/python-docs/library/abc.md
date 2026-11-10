"abc" --- Classes base abstratas
********************************

**Código-fonte:** Lib/abc.py

======================================================================

Este módulo fornece a infraestrutura para definir *classes base
abstratas* (ABCs, do inglês *abstract base class*) em Python, como
delineado em **PEP 3119**; veja o PEP para entender o porquê isto foi
adicionado ao Python. (Veja também **PEP 3141** e o módulo "numbers"
sobre uma hierarquia de tipo para números baseado nas ABCs.)

O módulo "collections" tem algumas classes concretas que derivam de
ABCs; essas podem, evidentemente, ser ainda mais derivadas. Além
disso, o submódulo "collections.abc" tem algumas ABCs que podem ser
usadas para testar se uma classe ou instância oferece uma interface
particular, por exemplo, se é *hasheável* ou se é um *mapeamento*.

Este módulo fornece a metaclasse "ABCMeta" para definir ABCs e uma
classe auxiliar "ABC" para alternativamente definir ABCs através de
herança:

class abc.ABC

   Uma classe auxiliar que tem "ABCMeta" como sua metaclasse. Com essa
   classe, uma classe base abstrata pode ser criada simplesmente
   derivando da "ABC" evitando às vezes confundir o uso da metaclasse,
   por exemplo:

      from abc import ABC

      class MyABC(ABC):
          pass

   Note que o tipo da classe "ABC" ainda é "ABCMeta", portanto herdar
   da "ABC" requer as precauções usuais a respeito do uso da
   metaclasse, pois herança múltipla pode levar a conflitos de
   metaclasse. Pode-se também definir uma classe base abstrata ao
   passar a palavra reservada metaclasse e usar "ABCMeta" diretamente,
   por exemplo:

      from abc import ABCMeta

      class MyABC(metaclass=ABCMeta):
          pass

   Adicionado na versão 3.4.

class abc.ABCMeta

   Metaclasse para definir Classe Base Abstrata (ABCs).

   Use esta metaclasse para criar uma ABC. Uma ABC pode ser
   diretamente estendida, e então agir como uma classe misturada. Você
   também pode registrar classes concretas não relacionadas (até mesmo
   classes embutidas) e ABCs não relacionadas como "subclasses
   virtuais" -- estas e suas descendentes serão consideradas
   subclasses da ABC de registro pela função embutida "issubclass()",
   mas a ABC de registro não irá aparecer na MRO (Ordem de Resolução
   do Método) e nem as implementações do método definidas pela ABC de
   registro será chamável (nem mesmo via "super()"). [1]

   Classes criadas com a metaclasse de "ABCMeta" tem o seguinte
   método:

   register(subclass)

      Registra *subclass* como uma "subclasse virtual" desta ABC. Por
      exemplo:

         from abc import ABC

         class MyABC(ABC):
             pass

         MyABC.register(tuple)

         assert issubclass(tuple, MyABC)
         assert isinstance((), MyABC)

      Alterado na versão 3.3: Retorna a subclasse registrada, para
      permitir o uso como um decorador de classe.

      Alterado na versão 3.4: Para detectar chamadas para
      "register()", você pode usar a função "get_cache_token()".

   Você também pode sobrepor este método em uma classe base abstrata:

   __subclasshook__(subclass)

      (Deve obrigatoriamente ser definido como um método de classe.)

      Verifica se *subclass* é considerada uma subclasse desta ABC.
      Isto significa que você pode personalizar ainda mais o
      comportamento de "issubclass()" sem a necessidade de chamar
      "register()" em toda classe que você queira considerar uma
      subclasse da ABC. (Este método de classe é chamado do método
      "__subclasscheck__()" da ABC.)

      Este método deve retornar "True", "False" ou "NotImplemented".
      Se retornar "True", *subclass* é considerada uma subclasse desta
      ABC. Se retornar "False", *subclass* não é considerada uma
      subclasse desta ABC, mesmo que normalmente seria uma. Se
      retornar "NotImplemented", a verificação da subclasse é
      continuada com o mecanismo usual.

   Para uma demonstração destes conceitos, veja este exemplo de
   definição ABC:

      class Foo:
          def __getitem__(self, index):
              ...
          def __len__(self):
              ...
          def get_iterator(self):
              return iter(self)

      class MyIterable(ABC):

          @abstractmethod
          def __iter__(self):
              while False:
                  yield None

          def get_iterator(self):
              return self.__iter__()

          @classmethod
          def __subclasshook__(cls, C):
              if cls is MyIterable:
                  if any("__iter__" in B.__dict__ for B in C.__mro__):
                      return True
              return NotImplemented

      MyIterable.register(Foo)

   A "MyIterable" da ABC define o método iterável padrão,
   "__iter__()", como um método abstrato. A implementação dada aqui
   pode ainda ser chamada da subclasse. O método "get_iterator()" é
   também parte da classe base abstrata "MyIterable", mas não precisa
   ser substituído nas classes derivadas não abstratas.

   O método de classe "__subclasshook__()" definido aqui diz que
   qualquer classe que tenha um método "__iter__()" em seu "__dict__"
   (ou no de uma de suas classes base, acessados via lista "__mro__")
   é considerada uma "MyIterable" também.

   Finalmente, a última linha faz de "Foo" uma subclasse virtual da
   "MyIterable", apesar de não definir um método "__iter__()" (ela usa
   o protocolo iterável antigo, definido em termos de "__len__()" e
   "__getitem__()"). Note que isto não fará o "get_iterator"
   disponível como um método de "Foo", então ele é fornecido
   separadamente.

O módulo "abc" também fornece o seguinte decorador:

@abc.abstractmethod

   Um decorador indicando métodos abstratos.

   Using this decorator requires that the class's metaclass is
   "ABCMeta" or is derived from it.  A class that has a metaclass
   derived from "ABCMeta" cannot be instantiated unless all of its
   abstract methods and properties are overridden.  The abstract
   methods can be called using any of the normal 'super' call
   mechanisms.  "@abstractmethod" may be used to declare abstract
   methods for properties and descriptors.

   Dynamically adding abstract methods to a class, or attempting to
   modify the abstraction status of a method or class once it is
   created, are only supported using the "update_abstractmethods()"
   function.  The "@abstractmethod" only affects subclasses derived
   using regular inheritance; "virtual subclasses" registered with the
   ABC's "register()" method are not affected.

   When "@abstractmethod" is applied in combination with other method
   descriptors, it should be applied as the innermost decorator, as
   shown in the following usage examples:

      class C(ABC):
          @abstractmethod
          def my_abstract_method(self, arg1):
              ...
          @classmethod
          @abstractmethod
          def my_abstract_classmethod(cls, arg2):
              ...
          @staticmethod
          @abstractmethod
          def my_abstract_staticmethod(arg3):
              ...

          @property
          @abstractmethod
          def my_abstract_property(self):
              ...
          @my_abstract_property.setter
          @abstractmethod
          def my_abstract_property(self, val):
              ...

          @abstractmethod
          def _get_x(self):
              ...
          @abstractmethod
          def _set_x(self, val):
              ...
          x = property(_get_x, _set_x)

   In order to correctly interoperate with the abstract base class
   machinery, the descriptor must identify itself as abstract using
   "__isabstractmethod__". In general, this attribute should be "True"
   if any of the methods used to compose the descriptor are abstract.
   For example, Python's built-in "@property" does the equivalent of:

      class Descriptor:
          ...
          @property
          def __isabstractmethod__(self):
              return any(getattr(f, '__isabstractmethod__', False) for
                         f in (self._fget, self._fset, self._fdel))

   Nota:

     Diferente de métodos abstratos Java, esses métodos abstratos
     podem ter uma implementação. Esta implementação pode ser chamada
     via mecanismo da "super()" da classe que a substitui. Isto pode
     ser útil como um ponto final para uma super chamada em um
     framework que usa herança múltipla cooperativa.

O módulo "abc" também suporta os seguintes decoradores herdados:

@abc.abstractclassmethod

   Adicionado na versão 3.2.

   Descontinuado desde a versão 3.3: It is now possible to use
   "@classmethod" with "@abstractmethod", making this decorator
   redundant.

   A subclass of the built-in "classmethod", indicating an abstract
   classmethod. Otherwise it is similar to "@abstractmethod".

   This special case is deprecated, as the "@classmethod" decorator is
   now correctly identified as abstract when applied to an abstract
   method:

      class C(ABC):
          @classmethod
          @abstractmethod
          def my_abstract_classmethod(cls, arg):
              ...

@abc.abstractstaticmethod

   Adicionado na versão 3.2.

   Descontinuado desde a versão 3.3: It is now possible to use
   "@staticmethod" with "@abstractmethod", making this decorator
   redundant.

   A subclass of the built-in "staticmethod", indicating an abstract
   staticmethod. Otherwise it is similar to "@abstractmethod".

   This special case is deprecated, as the "@staticmethod" decorator
   is now correctly identified as abstract when applied to an abstract
   method:

      class C(ABC):
          @staticmethod
          @abstractmethod
          def my_abstract_staticmethod(arg):
              ...

@abc.abstractproperty

   Descontinuado desde a versão 3.3: It is now possible to use
   "@property", "@property.getter", "@property.setter" and
   "@property.deleter" with "@abstractmethod", making this decorator
   redundant.

   A subclass of the built-in "property", indicating an abstract
   property.

   This special case is deprecated, as the "@property" decorator is
   now correctly identified as abstract when applied to an abstract
   method:

      class C(ABC):
          @property
          @abstractmethod
          def my_abstract_property(self):
              ...

   O exemplo acima define uma propriedade somente leitura; você também
   pode definir uma propriedade abstrata de leitura e escrita marcando
   apropriadamente um ou mais dos métodos subjacentes como abstratos:

      class C(ABC):
          @property
          def x(self):
              ...

          @x.setter
          @abstractmethod
          def x(self, val):
              ...

   Se apenas alguns componentes são abstratos, apenas estes
   componentes precisam ser atualizados para criar uma propriedade
   concreta em uma subclasse:

      class D(C):
          @C.x.setter
          def x(self, val):
              ...

O módulo "abc" também fornece as seguintes funções:

abc.get_cache_token()

   Retorna o token de cache da classe base abstrata atual.

   O token é um objeto opaco (que suporta teste de igualdade)
   identificando a versão atual do cache da classe base abstrata para
   subclasses virtuais. O token muda a cada chamada ao
   "ABCMeta.register()" em qualquer CBA.

   Adicionado na versão 3.4.

abc.update_abstractmethods(cls)

   Uma função para recalcular o status de abstração de uma classe
   abstrata. Esta função deve ser chamada se os métodos abstratos de
   uma classe foram implementados ou alterados após sua criação.
   Normalmente, essa função deve ser chamada de dentro de um decorador
   de classe.

   Retorna *cls*, para permitir o uso como decorador de classe.

   Se *cls* não for uma instância de "ABCMeta", não faz nada.

   Nota:

     Esta função presume que as superclasses de *cls* já estão
     atualizadas. Ele não atualiza nenhuma subclasse.

   Adicionado na versão 3.10.

-[ Notas de rodapé ]-

[1] Programadores C++ devem notar que o conceito da classe base
    virtual do Python não é o mesmo que o de C++.
