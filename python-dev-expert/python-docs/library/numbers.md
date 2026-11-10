"numbers" --- Classes base abstratas numéricas
**********************************************

**Código-fonte:** Lib/numbers.py

======================================================================

O módulo "numbers" (**PEP 3141**) define uma hierarquia de *classes
base abstratas* que progressivamente definem mais operações. Nenhum
dos tipos definidos neste módulo se destina a ser instanciado.

class numbers.Number

   A raiz da hierarquia numérica. Se você quiser apenas verificar se
   um argumento *x* é um número, sem se importar com o tipo, use
   "isinstance(x, Number)".


A torre numérica
================

class numbers.Complex

   As subclasses deste tipo descrevem números complexos e incluem as
   operações que funcionam no tipo embutido "complex". Elas são:
   conversões para "complex" e "bool", "real", "imag", "+", "-", "*",
   "/", "**", "abs()", "conjugate()", "==" e "!=". Todos exceto "-" e
   "!=" são abstratos.

   real

      Abstrata. Obtém o componente real deste número.

   imag

      Abstrata. Obtém o componente imaginário deste número.

   abstractmethod conjugate()

      Abstrata. Retorna o conjugado complexo. Por exemplo,
      "(1+3j).conjugate() == (1-3j)".

class numbers.Real

   Para "Complex", "Real" adiciona as operações que funcionam em
   números reais.

   Em suma, são: uma conversão para "float", "math.trunc()",
   "round()", "math.floor()", "math.ceil()", "divmod()", "//", "%",
   "<", "<=", ">" e ">=".

   Real também fornece padrão para "complex()", "real", "imag" e
   "conjugate()".

class numbers.Rational

   Estende "Real" e adiciona as propriedades "numerator" e
   "denominator". Ele fornece um padrão para "float()".

   Os valores "numerator" e "denominator" devem ser instâncias de
   "Integral" e devem estar nos termos mais baixos com "denominator"
   positivo.

   numerator

      Abstrato. O numerador deste número racional.

   denominator

      Abstrato. O denominador deste número racional.

class numbers.Integral

   Estende "Rational" e adiciona uma conversão para "int". Fornece
   padrões para "float()", "numerator" e "denominator". Adiciona
   métodos abstratos para "pow()" com operações de módulo e de string
   de bits: "<<", ">>", "&", "^", "|", "~".


Notas para implementadores de tipos
===================================

Os implementadores devem ter o cuidado de tornar iguais números iguais
e fazer hash deles com os mesmos valores. Isso pode ser sutil se
houver duas extensões diferentes dos números reais. Veja também
Hashing de tipos numéricos.


Adding more numeric ABCs
------------------------

Existem, é claro, mais ABCs possíveis para números, e isso seria uma
hierarquia pobre se excluísse a possibilidade de adicioná-los. Você
pode adicionar "MyFoo" entre "Complex" e "Real" com:

   class MyFoo(Complex): ...
   MyFoo.register(Real)


Implementando as operações aritméticas
--------------------------------------

Queremos implementar as operações aritméticas de forma que as
operações de modo misto chamem uma implementação cujo autor conhecia
os tipos de ambos os argumentos ou convertam ambos para o tipo
embutido mais próximo e façam a operação lá. Para subtipos de
"Integral", isso significa que "__add__()" e "__radd__()" devem ser
definidos com:

   class MyIntegral(Integral):

       def __add__(self, other):
           if isinstance(other, MyIntegral):
               return do_my_adding_stuff(self, other)
           elif isinstance(other, OtherTypeIKnowAbout):
               return do_my_other_adding_stuff(self, other)
           else:
               return NotImplemented

       def __radd__(self, other):
           if isinstance(other, MyIntegral):
               return do_my_adding_stuff(other, self)
           elif isinstance(other, OtherTypeIKnowAbout):
               return do_my_other_adding_stuff(other, self)
           elif isinstance(other, Integral):
               return int(other) + int(self)
           elif isinstance(other, Real):
               return float(other) + float(self)
           elif isinstance(other, Complex):
               return complex(other) + complex(self)
           else:
               return NotImplemented

There are 5 different cases for a mixed-type operation on subclasses
of "Complex". All of the above code that doesn't refer to "MyIntegral"
and "OtherTypeIKnowAbout" is referred to as "boilerplate".

In this description, "a" is an instance of "A" and "b" is an instance
of "B", where "A" and "B" are both subtypes of "Complex". Consider "a
+ b":

1. Se "A" define um "__add__()", que aceita "b", está tudo bem.

2. Se "A" voltar ao código padrão e tivesse que retornar um valor de
   "__add__()", perderíamos a possibilidade de que "B" definisse um
   "__radd__()" mais inteligente, então o código padrão deve retornar
   "NotImplemented" de "__add__()". (Ou "A" pode não implementar
   "__add__()".)

3. Então, "__radd__()" do "B" consegue uma chance. Se ele aceitar "a",
   está tudo bem.

4. Se ele recorrer ao padrão, não há mais métodos possíveis para
   tentar, então é aqui que a implementação padrão deve residir.

5. If "B" is a subtype of "A", Python tries "B.__radd__" before
   "A.__add__". This is ok, because it was implemented with knowledge
   of "A", so it can handle those instances before delegating to
   "Complex".

If "A" is a subtype of "Complex" and "B" is a subtype of "Real"
without sharing any other knowledge, then the appropriate shared
operation is the one involving the built in "complex", and both
"__radd__()" s land there, so "a+b == b+a".

Como a maioria das operações em qualquer tipo será muito semelhante,
pode ser útil definir uma função auxiliar que gera as instâncias de
avanço e reversão de qualquer operador. Por exemplo,
"fractions.Fraction" usa:

   def _operator_fallbacks(monomorphic_operator, fallback_operator):
       def forward(a, b):
           if isinstance(b, (int, Fraction)):
               return monomorphic_operator(a, b)
           elif isinstance(b, float):
               return fallback_operator(float(a), b)
           elif isinstance(b, complex):
               return fallback_operator(complex(a), b)
           else:
               return NotImplemented
       forward.__name__ = '__' + fallback_operator.__name__ + '__'
       forward.__doc__ = monomorphic_operator.__doc__

       def reverse(b, a):
           if isinstance(a, Rational):
               # Inclui ints.
               return monomorphic_operator(a, b)
           elif isinstance(a, Real):
               return fallback_operator(float(a), float(b))
           elif isinstance(a, Complex):
               return fallback_operator(complex(a), complex(b))
           else:
               return NotImplemented
       reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
       reverse.__doc__ = monomorphic_operator.__doc__

       return forward, reverse

   def _add(a, b):
       """a + b"""
       return Fraction(a.numerator * b.denominator +
                       b.numerator * a.denominator,
                       a.denominator * b.denominator)

   __add__, __radd__ = _operator_fallbacks(_add, operator.add)

   # ...
