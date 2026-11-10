6. Expressões
*************

Este capítulo explica o significado dos elementos das expressões em
Python.

**Notas sobre a sintaxe:** Neste capítulo e nos subsequentes, será
utilizada a notação de gramática para descrever a sintaxe, em vez da
análise léxica.

Quando (uma alternativa de) uma regra de sintaxe tem a forma:

   name: othername

e nenhuma semântica é fornecida, a semântica desta forma de "name" é a
mesma que para "othername".


6.1. Conversões aritméticas
===========================

Quando a descrição de um operador aritmético abaixo utiliza a frase
"os argumentos numéricos são convertidos para um tipo real comum",
isso significa que a implementação do operador para tipos numéricos
embutidos funciona conforme descrito na seção Tipos numéricos da
documentação da biblioteca padrão.

Algumas regras adicionais se aplicam a certos operadores e operadores
não-numéricos (por exemplo, uma string como um argumento à esquerda
para o operador "%"). As extensões devem definir seu próprio
comportamento de conversão.


6.2. Átomos
===========

Átomos são os elementos mais básicos de expressões. Os átomos mais
simples são constantes embutidas, nomes e literais. Átomos mais
complexos são delimitados por pares de delimitadores:

* "()" (parênteses): grupos, exibições de tuplas, átomos de yield e
  expressões geradoras;

* "[]" (colchetes): exibições de lista;

* "{}" (chaves): exibições de dicionário e conjunto.

Formalmente, a sintaxe para átomo é:

   atom:
      | builtin_constant
      | identifier
      | literal
      | parenthesized_enclosure
      | bracketed_enclosure
      | braced_enclosure
   parenthesized_enclosure:
      | group
      | tuple
      | yield_atom
      | generator_expression
   bracketed_enclosure:
      | listcomp
      | list
   braced_enclosure:
      | dictcomp
      | dict
      | setcomp
      | set


6.2.1. Constantes embutidas
---------------------------

As palavras reservadas "True", "False" e "None" nomeiam constantes
embutidas. O token "..." nomeia a constante "Ellipsis".

A avaliação desses átomos produz o valor correspondente.

Nota:

  Várias outras constantes embutidas estão disponíveis como variáveis
  globais, mas apenas aquelas mencionadas aqui são palavras
  reservadas. Em particular, esses nomes não podem ser reatribuídos
  nem usados como atributos:

     >>> False = 123
       File "<input>", line 1
        False = 123
        ^^^^^
     SyntaxError: cannot assign to False

Formalmente, a sintaxe para constantes embutidas é:

   builtin_constant: 'True' | 'False' | 'None' | '...'


6.2.2. Identificadores (Nomes)
------------------------------

Um identificador que ocorre como um átomo é um nome. Veja a seção
Nomes (identificadores e palavras reservadas) para a definição lexical
e a seção Nomeação e ligação para documentação de nomenclatura e
ligação.

Quando o nome está vinculado a um objeto, a avaliação do átomo produz
esse objeto. Quando um nome não está vinculado, uma tentativa de
avaliá-lo levanta uma exceção "NameError".


6.2.2.1. Desfiguração de nome privado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quando um identificador que ocorre textualmente em uma definição de
classe começa com dois ou mais caracteres de sublinhado e não termina
com dois ou mais sublinhados, ele é considerado um *nome privado*
daquela classe.

Ver também: As especificações de classe.

Mais precisamente, os nomes privados são transformados em um formato
mais longo antes que o código seja gerado para eles. Se o nome
transformado tiver mais de 255 caracteres, poderá ocorrer truncamento
definido pela implementação.

A transformação é independente do contexto sintático no qual o
identificador é usado, mas apenas os seguintes identificadores
privados são desfigurados:

* Qualquer nome usado como nome de uma variável que é atribuída ou
  lida ou qualquer nome de um atributo que está sendo acessado.

  O atributo "__name__" de funções aninhadas, classes e apelidos de
  tipo, entretanto, não é desfigurado.

* O nome dos módulos importados, por exemplo, "__spam" em "import
  __spam". Se o módulo faz parte de um pacote (ou seja, seu nome
  contém um ponto), o nome *não* é desfigurado, por exemplo, o "__foo"
  em "import __foo.bar" não é desfigurado.

* O nome de um membro importado, por exemplo, "__f" em "from spam
  import __f".

A regra de transformação está definida da seguinte forma:

* O nome da classe, com os sublinhados iniciais removidos e um único
  sublinhado inicial inserido, é inserido na frente do identificador,
  por exemplo, o identificador "__spam" ocorrendo em uma classe
  chamada "Foo", "_Foo" ou "__Foo" é transformado em "_Foo__spam".

* Se o nome da classe consiste apenas em sublinhados, a transformação
  é a identidade, por exemplo, o identificador "__spam" que ocorre em
  uma classe chamada "_" ou "__" é deixado como está.


6.2.3. Literais
---------------

Um *literal* é uma representação textual de um valor. O Python oferece
suporte a literais numéricos, de string e de bytes. strings de formato
e string template são tratados como literais de string.

Literais numéricos consistem em um único token "NUMBER", que
representa um número inteiro, um número de ponto flutuante ou um
número imaginário. Consulte a seção Literais numéricos na documentação
de análise léxica para obter detalhes.

Literais de string e de bytes podem consistir em vários tokens.
Consulte a seção Concatenação de literal de string para obter
detalhes.

Observe que números negativos e números complexos, como "-3" ou
"3+4.2j", não são sintaticamente literais, mas sim operações
aritméticas unárias ou binárias envolvendo o operador "-" ou "+".

A avaliação de um literal produz um objeto do tipo fornecido ("int",
"float", "complex", "str", "bytes" ou "Template") com o valor
fornecido. O valor pode ser aproximado no caso de literais de ponto
flutuante e imaginários.

A gramática formal para literais é:

   literal: strings | NUMBER


6.2.3.1. Identidade de objeto e literais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Todos os literais correspondem a tipos de dados imutáveis e, portanto,
a identidade do objeto é menos importante que seu valor. Múltiplas
avaliações de literais com o mesmo valor (seja a mesma ocorrência no
texto do programa ou uma ocorrência diferente) podem obter o mesmo
objeto ou um objeto diferente com o mesmo valor.

Detalhes da implementação do CPython:: Por exemplo, no CPython,
números inteiros *pequenos* com o mesmo valor são avaliados como o
mesmo objeto:

   >>> x = 7
   >>> y = 7
   >>> x is y
   True

No entanto, números inteiros grandes são avaliados como objetos
diferentes:

   >>> x = 123456789
   >>> y = 123456789
   >>> x is y
   False

Esse comportamento pode mudar em versões futuras do CPython. Em
particular, o limite entre números inteiros "pequenos" e "grandes" já
mudou no passado.O CPython emitirá um "SyntaxWarning" ao comparar
literais usando "is":

   >>> x = 7
   >>> x is 7
   <input>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
   True

Veja Quando eu posso depender dos testes de identidade com o operador
is? para mais informações.

Strings template são imutáveis, mas podem referenciar objetos mutáveis
como valores de "Interpolation". Para os fins desta seção, duas
t-strings têm o "mesmo valor" se tanto a sua estrutura quanto a
*identidade* dos valores coincidirem.

Atualmente, cada avaliação de uma string template resulta em um objeto
diferente.


6.2.3.2. Concatenação de literal de string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vários literais de strings ou bytes adjacentes, possivelmente usando
convenções de aspas diferentes, são permitidos, e seu significado é o
mesmo que sua concatenação:

   >>> "olá" 'mundo'
   "olámundo"

Este recurso é definido no nível sintático, portanto, funciona apenas
com literais. Para concatenar expressões de string em tempo de
execução, o operador '+' pode ser usado:

   >>> greeting = "Olá"
   >>> space = " "
   >>> name = "Blaise"
   >>> print(greeting + space + name)   # not: print(greeting space name)
   Olá Blaise

A concatenação de literais pode misturar livremente strings brutas,
strings entre aspas triplas e literais de strings formatadas. Por
exemplo:

   >>> "Olá" r', ' f"{name}!"
   "Olá, Blaise!"

Este recurso pode ser usado para reduzir o número de contrabarras
necessárias, para dividir strings longas convenientemente em linhas
longas ou até mesmo para adicionar comentários a partes de strings.
Por exemplo:

   re.compile("[A-Za-z_]"       # letra ou sublinhado
              "[A-Za-z0-9_]*"   # letra, dígito ou sublinhado
             )

No entanto, literais de bytes só podem ser combinados com outros
literais de bytes; não com literais de string de qualquer tipo. Além
disso, literais de strings templates só podem ser combinados com
outros literais de strings templates:

   >>> t"Olá" t"{name}!"
   Template(strings=('Olá', '!'), interpolations=(...))

Formalmente:

   strings: (STRING | fstring)+ | tstring+


6.2.4. Grupos de parênteses
---------------------------

Um *grupo de parênteses* é uma expressão delimitada por parênteses. O
grupo é avaliado com o mesmo valor da expressão contida nele.

Os grupos são usados para substituir ou esclarecer a precedência do
operador, da mesma forma que na notação matemática. Por exemplo:

   >>> 3 << 2 | 4
   12
   >>> 3 << (2 | 4)   # Substitui a precedência do | (OU bit a bit)
   192
   >>> (3 << 2) | 4   # Mesmo que sem parênteses (mas mais claro)
   12

Observe que nem tudo que está entre parênteses é um *grupo*.
Especificamente, um grupo entre parênteses deve conter exatamente uma
expressão e não pode terminar com uma vírgula. Consulte exibições de
tupla e expressões geradoras para outras formas entre parênteses.

Formalmente, a sintaxe para grupos é:

   group: '(' assignment_expression ')'


6.2.5. Exibições de contêiner
-----------------------------

For constructing builtin containers (lists, sets, tuples or
dictionaries), Python provides special syntax called *displays*. There
are subtle differences between the four kinds of displays, detailed in
the following sections. All displays, however, consist of comma-
separated items enclosed in paired delimiters.

For example, a *list display* is a series of expressions enclosed in
square brackets:

   >>> ["one", "two", "three"]
   ['one', 'two', 'three']
   >>> [1 + 2, 2 + 3]
   [3, 5]

In list, tuple and dictionary (but not set) displays, the series may
be empty:

   >>> []  # empty list
   []
   >>> ()  # empty tuple
   ()
   >>> {}  # empty dictionary
   {}

If the series is not empty, the items may be followed by an additional
comma, which has no effect:

   >>> ["one", "two", "three",]  # note comma after "three"
   ['one', 'two', 'three']

Nota:

  The trailing comma is often used for displays that span multiple
  lines (using implicit line joining), so when a future programmer
  adds a new entry at the end, they do not need to modify an existing
  line:

     >>> [
     ...     'one',
     ...     'two',
     ...     'three',
     ... ]
     ['one', 'two', 'three']

At runtime, when a display is evaluated, the listed items are
evaluated from left to right and placed into a new container of the
appropriate type.

For tuple, list and set (but not dict) displays, any item in the
display may be prefixed with an asterisk ("*"). This denotes iterable
unpacking. At runtime, the asterisk-prefixed expression must evaluate
to an iterable, whose contents are inserted into the container at the
location of the unpacking. For example:

   >>> numbers = (1, 2)
   >>> [*numbers, 'word', *numbers]
   [1, 2, 'word', 1, 2]

Dictionary displays use a similar mechanism called *dictionary
unpacking*, denoted with a double asterisk ("**"). See Sintaxes de
criação de dicionário for details.

A more advanced form of displays are *comprehensions*, where items are
computed via a set of looping and filtering instructions. See the
Compreensões section for details.

Adicionado na versão 3.5: Iterable and dictionary unpacking in
displays, originally proposed by **PEP 448**.


6.2.5.1. Sintaxes de criação de lista
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A *list display* is a possibly empty series of expressions enclosed in
square brackets. For example:

   >>> ["one", "two", "three"]
   ['one', 'two', 'three']
   >>> ["one"]  # One-element list
   ['one']
   >>> []       # empty list
   []

See Exibições de contêiner for general information on displays.

The formal grammar for list displays is:

   list: '[' [flexible_expression_list] ']'


6.2.5.2. Sintaxes de criação de conjunto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A *set display* is a *non-empty* series of expressions enclosed in
curly braces. For example:

   >>> {"one", "two", "three"}
   {'one', 'three', 'two'}
   >>> {"one"}  # One-element set
   {'one'}

See Exibições de contêiner for general information on displays.

There is no special syntax for the empty set. The "{}" literal is a
dictionary display that constructs an empty dictionary. Call "set()"
with no arguments to get an empty set.

The formal grammar for set displays is:

   set: '{' flexible_expression_list '}'


6.2.5.3. Tuple displays
~~~~~~~~~~~~~~~~~~~~~~~

A *tuple display* is a series of expressions enclosed in parentheses.
For example:

   >>> (1, 2)
   (1, 2)
   >>> ()  # uma tupla vazia
   ()

See Exibições de contêiner for general information on displays.

To avoid ambiguity, if a tuple display has exactly one element, it
requires a trailing comma. Without it, you get a parenthesized group:

   >>> ('single',)  # single-element tuple
   ('single',)
   >>> ('single')   # no comma: single string
   'single'

To put it in other words, a tuple display is a parenthesized list of
either:

* two or more comma-separated expressions, or

* zero or more expressions, each followed by a comma.

Since tuples are immutable, object identity rules for literals also
apply to tuples: at runtime, two occurrences of tuples with the same
values may or may not yield the same object.

Nota:

  Python's syntax also includes expression lists, where a comma-
  separated list of expressions is *not* enclosed in parentheses but
  evaluates to tuple.In other words, when it comes to tuple syntax,
  the comma is more important that the use of parentheses. Only the
  empty tuple is spelled without a comma.

The formal grammar for tuple displays is:

   tuple:
      | '(' flexible_expression (',' flexible_expression)+ [','] ')'
      | '(' flexible_expression ',' ')'
      | '(' ')'


6.2.5.4. Sintaxes de criação de dicionário
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A *dictionary display* is a possibly empty series of *dict items*
enclosed in curly braces. Each dict item is a colon-separated pair of
expressions: the *key* and its associated *value*. For example:

   >>> {1: 'one', 2: 'two'}
   {1: 'one', 2: 'two'}

At runtime, when a dictionary comprehension is evaluated, the
expressions are evaluated from left to right. Each key object is used
as a key into the dictionary to store the corresponding value. This
means that you can specify the same key multiple times in the
comprehension, and the final dictionary's value for a given key will
be the last one given. For example:

   >>> {
   ...     1: 'this will be overridden',
   ...     2: 'two',
   ...     1: 'also overridden',
   ...     1: 'one',
   ... }
   {1: 'one', 2: 'two'}

Instead of a key-value pair, a dict item may be an expression prefixed
by a double asterisk "**". This denotes *dictionary unpacking*. At
runtime, the expression must evaluate to a *mapping*; each item of the
mapping is added to the new dictionary. As with key-value pairs, later
values replace values already set by earlier items and unpackings.
This may be used to override a set of defaults:

   >>> defaults = {'color': 'blue', 'count': 8}
   >>> overrides = {'color': 'yellow'}
   >>> {**defaults, **overrides}
   {'color': 'yellow', 'count': 8}

Adicionado na versão 3.5: Desempacotando em sintaxes de criação de
dicionário, originalmente proposto pela **PEP 448**.

The formal grammar for dict displays is:

   dict:                   '{' [double_starred_kvpairs] '}'
   double_starred_kvpairs: ','.double_starred_kvpair+ [',']
   double_starred_kvpair:  '**' or_expr | kvpair
   kvpair:                 expression ':' expression


6.2.6. Compreensões
-------------------

List, set and dictionary *comprehensions* are a form of container
displays where items are computed via a set of looping and filtering
instructions rather than listed explicitly.

In its simplest form, a comprehension consists of a single expression
followed by a "for" clause. The "for" clause has the same syntax as
the header of a for statement, without a trailing colon.

For example, a list of the first ten squares is:

   >>> [x**2 for x in range(10)]
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

At run time, a list comprehension creates a new list. The expression
after "in" must evaluate to an *iterable*. For each element of this
iterable, the element is bound to the "for" clause's target as in a
"for" statement, then the expression before "for" is evaluated with
the target in scope and the result is added to the new list. Thus, the
example above is roughly equivalent to defining and calling the
following function:

   def make_list_of_squares(iterable):
       result = []
       for x in iterable:
           result.append(x**2)
       return result

   make_list_of_squares(range(10))

Set comprehensions work similarly. For example, here is a set of
lowercase letters:

   >>> {x.lower() for x in ['a', 'A', 'b', 'C']}
   {'c', 'a', 'b'}

At run time, this corresponds roughly to calling this function:

   def make_lowercase_set(iterable):
       result = set()
       for x in iterable:
           result.add(x.lower())
       return result

   make_lowercase_set(['a', 'A', 'b', 'C'])

Dictionary comprehensions start with a colon-separated key-value pair
instead of an expression. For example:

   >>> {func.__name__: func for func in [print, hex, any]}
   {'print': <built-in function print>,
    'hex': <built-in function hex>,
    'any': <built-in function any>}

At run time, this corresponds roughly to:

   def make_dict_mapping_names_to_functions(iterable):
       result = {}
       for func in iterable:
           result[func.__name__] = func
       return result

   make_dict_mapping_names_to_functions([print, hex, any])

As in other kinds of dictionary displays, the same key may be
specified multiple times. Earlier values are overwritten by ones that
are evaluated later.

There are no *tuple comprehensions*. A similar syntax is instead used
for generator expressions, from which you can construct a tuple like
this:

   >>> tuple(x**2 for x in range(10))
   (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

Alterado na versão 3.8: Antes do Python 3.8, em compreensões de dict,
a ordem de avaliação de chave e valor não era bem definida. No
CPython, o valor foi avaliado antes da chave. A partir de 3.8, a chave
é avaliada antes do valor, conforme proposto pela **PEP 572**.


6.2.6.1. Filtering in comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "for" clause may be followed by an "if" clause with an expression.

For example, a list of names from the "math" module that start with
"f" is:

   >>> [name for name in vars(math) if name.startswith('f')]
   ['fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum']

At run time, the expression after "if" is evaluated before each
element is added to the resulting container, and if it is false, the
element is skipped. Thus, the above example roughly corresponds to
defining and calling the following function:

   def get_math_f_names(iterable):
       result = []
       for name in iterable:
           if name.startswith('f'):
              result.append(name)
       return result

   get_math_f_names(vars(math))

Filtering is a special case of more complex comprehensions. See the
next section for a more formal description.


6.2.6.2. Complex comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generally, a comprehension's initial "for" clause may be followed by
zero or more additional "for" or "if" clauses. For example, here is a
list of names exposed by two Python modules, filtered to only include
names that start with "a":

   >>> import array
   >>> import math
   >>> [
   ...     name
   ...     for module in [array, math]
   ...     for name in vars(module)
   ...     if name.startswith('a')
   ... ]
   ['array', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh']

At run time, this roughly corresponds to defining and calling:

   def get_a_names(iterable):
       result = []
       for module in iterable:
           for name in vars(module):
               if name.startswith('a'):
                   result.append(name)
       return result

   get_a_names([array, math])

The elements of the new container are those that would be produced by
considering each of the "for" or "if" clauses a block, nesting from
left to right, and evaluating the expression to produce an element (or
dictionary entry) each time the innermost block is reached.

Aside from the iterable expression in the leftmost "for" clause, the
comprehension is executed in a separate implicitly nested scope. This
ensures that names assigned to in the target list don't "leak" into
the enclosing scope. For example:

   >>> x = 'old value'
   >>> [x**2 for x in range(10)]  # this `x` is local to the comprehension
   >>> x
   'old value'

The iterable expression in the leftmost "for" clause is evaluated
directly in the enclosing scope and then passed as an argument to the
implicitly nested scope.

Subsequent "for" clauses and any filter condition in the leftmost
"for" clause cannot be evaluated in the enclosing scope as they may
depend on the values obtained from the leftmost iterable.

Para garantir que a compreensão sempre resulte em um contêiner do tipo
apropriado, as expressões "yield" e "yield from" são proibidas no
escopo aninhado implicitamente.

Assignment expressions are not allowed inside comprehension iterable
expressions (that is, the expressions after the "in" keyword), nor
anywhere within comprehensions that appear directly in a class
definition.

Alterado na versão 3.8: "yield" e "yield from" proibidos no escopo
aninhado implícito.


6.2.6.3. Unpacking in comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the expression of a list or set comprehension is starred, the
result will be unpacked to produce zero or more elements.

This is often used for "flattening" lists, for example:

   >>> students = ['Petr', 'Blaise', 'Jarka']
   >>> teachers = ['Salim', 'Bartosz']
   >>> lists_of_people = [students, teachers]
   >>> [*people for people in lists_of_people]
   ['Petr', 'Blaise', 'Jarka', 'Salim', 'Bartosz']

At run time, this comprehension roughly corresponds to:

   def flatten_names(lists_of_people):
       result = []
       for people in lists_of_people:
           result.extend(people)
       return result

In dict comprehensions, a double-starred expression will be evaluated
and then unpacked using dictionary unpacking, inserting zero or more
key/value pairs into the new dictionary. As in other kinds of
dictionary displays, if the same key is specified multiple times, the
associated value in the resulting dictionary will be the last one
specified.

Por exemplo:

   >>> system_defaults = {'color': 'blue', 'count': 8}
   >>> user_defaults = {'color': 'yellow'}
   >>> overrides = {'count': 5}

   >>> configuration_sets = [system_defaults, user_defaults, overrides]

   >>> {**d for d in configuration_sets}
   {'color': 'yellow', 'count': 5}

Adicionado na versão 3.15: Unpacking in comprehensions using the "*"
and "**" operators was introduced in **PEP 798**.


6.2.6.4. Asynchronous comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In an "async def" function, an "async for" clause may be used to
iterate over a *asynchronous iterator*. A comprehension in an "async
def" function may consist of either a "for" or "async for" clause
following the leading expression, may contain additional "for" or
"async for" clauses, and may also use "await" expressions.

If a comprehension contains "async for" clauses, or if it contains
"await" expressions or other asynchronous comprehensions anywhere
except the iterable expression in the leftmost "for" clause, it is
called an *asynchronous comprehension*. An asynchronous comprehension
may suspend the execution of the coroutine function in which it
appears.

Adicionado na versão 3.6: Asynchronous comprehensions were introduced
in **PEP 530**.

Alterado na versão 3.11: Compreensões assíncronas agora são permitidas
dentro de compreensões em funções assíncronas. As compreensões
externas tornam-se implicitamente assíncronas.


6.2.6.5. Gramática formal para compreensões
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The formal grammar for comprehensions is:

   listcomp:      '[' comprehension ']'
   setcomp:       '{' comprehension '}'
   comprehension: flexible_expression for_if_clause+

   dictcomp:
       | '{' kvpair for_if_clause+ '}'
       | '{' '**' expression for_if_clause+ '}'

   for_if_clause:
       | ['async'] 'for' target_list 'in' or_test ('if' or_test)*


6.2.7. Expressões geradoras
---------------------------

The syntax for *generator expressions* is the same as for list
comprehensions, except that they are enclosed in parentheses instead
of brackets. For example:

   >>> iterator = (x ** 2 for x in range(10))
   >>> iterator
   <generator object <genexpr> at ...>

At runtime, a generator expression evaluates to a *generator iterator*
which yields the same values as the corresponding list comprehension:

   >>> list(iterator)
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Thus, the example above is roughly equivalent to defining and calling
the following generator function:

   def make_generator_of_squares(iterator):
       for x in iterator:
           yield x ** 2

   make_generator_of_squares(iter(range(10)))

The enclosing parentheses can be omitted in calls when the generator
expression is the only positional argument and there are no keyword
arguments. See the Calls section for details. For example:

   # The parentheses after `sum` are part of the call syntax:
   >>> sum(x ** 2 for x in range(10))
   285

   # The generator needs its own parentheses if it's not the only argument:
   >>> sum((x ** 2 for x in range(10)), start=1000)
   1285

The iterable expression in the leftmost "for" clause is evaluated
immediately, so that an error raised by this expression will be
emitted at the point where the generator expression is defined, rather
than at the point where the first value is retrieved:

   >>> (x ** 2 for x in nonexistent_iterable)
   Traceback (most recent call last):
     ...
   NameError: name 'nonexistent_iterable' is not defined

After the expression is evaluated, an iterator is created from the
result, as if "iter()" was called on it. Any error raised when
creating the iterator is also emitted immediately:

   >>> (x ** 2 for x in None)
   Traceback (most recent call last):
     ...
   TypeError: 'NoneType' object is not iterable

All other expressions are evaluated lazily, in the same fashion as
normal generators (that is, when the iterator is asked to yield a
value):

   >>> iterator = (nonexistent_value for x in range(10))
   >>> iterator
   <generator object <genexpr> at ...>
   >>> list(iterator)
   Traceback (most recent call last):
     ...
   NameError: name 'nonexistent_value' is not defined

   >>> iterator = (x * y for x in range(10) for y in nonexistent_iterable)
   >>> iterator
   <generator object <genexpr> at ...>
   >>> list(iterator)
   Traceback (most recent call last):
     ...
   NameError: name 'nonexistent_iterable' is not defined

To avoid interfering with the expected operation of the generator
expression itself, "yield" and "yield from" expressions are prohibited
inside the implicitly nested scope.

If a generator expression contains either "async for" clauses or
"await" expressions it is called an *asynchronous generator
expression*. An asynchronous generator expression returns a new
asynchronous generator object, which is an asynchronous iterator (see
Iteradores assíncronos).

The formal grammar for generator expressions is:

   generator_expression: "(" comprehension ")"

Adicionado na versão 3.6: Expressões geradoras assíncronas foram
introduzidas.

Alterado na versão 3.7: Antes do Python 3.7, as expressões geradoras
assíncronas só podiam aparecer em corrotinas "async def". A partir da
versão 3.7, qualquer função pode usar expressões geradoras
assíncronas.

Alterado na versão 3.8: "yield" e "yield from" proibidos no escopo
aninhado implícito.


6.2.8. Expressões yield
-----------------------

   yield_atom:       "(" yield_expression ")"
   yield_from:       "yield" "from" expression
   yield_expression: "yield" yield_list | yield_from

A expressão yield é usada ao definir uma função *geradora* ou uma
função *geradora assíncrona* e, portanto, só pode ser usada no corpo
de uma definição de função. Usar uma expressão yield no corpo de uma
função faz com que essa função seja uma função geradora, e usá-la no
corpo de uma função "async def" faz com que essa função de corrotina
seja uma função geradora assíncrona. Por exemplo:

   def gen():  # define uma função geradora
       yield 123

   async def agen(): # define uma função geradora assíncrona
       yield 123

Devido a seus efeitos colaterais no escopo recipiente, as expressões
"yield" não são permitidas como parte dos escopos definidos
implicitamente usados para implementar compreensões e expressões
geradoras.

Alterado na versão 3.8: Expressões yield proibidas nos escopos
aninhados implicitamente usados para implementar compreensões e
expressões geradoras.

As funções geradoras são descritas abaixo, enquanto as funções
geradoras assíncronas são descritas separadamente na seção Funções
geradoras assíncronas

Quando uma função geradora é chamada, ela retorna um iterador
conhecido como gerador. Esse gerador então controla a execução da
função geradora. A execução começa quando um dos métodos do gerador é
chamado. Nesse momento, a execução segue para a primeira expressão
yield, onde é suspensa novamente, retornando o valor de "yield_list"
ao chamador do gerador, ou "None" se "yield_list" é omitido. Por
suspenso, queremos dizer que todo o estado local é retido, incluindo
as chamadas atuais de variáveis locais, o ponteiro de instrução, a
pilha de avaliação interna e o estado de qualquer tratamento de
exceção. Quando a execução é retomada chamando um dos métodos do
gerador, a função pode prosseguir exatamente como se a expressão yield
fosse apenas outra chamada externa. O valor da expressão yield após a
retomada depende do método que retomou a execução. Se "__next__()" for
usado (tipicamente através de uma "for" ou do "next()" embutido) então
o resultado será "None". Caso contrário, se "send()" for usado, o
resultado será o valor passado para esse método.

Tudo isso torna as funções geradoras bastante semelhantes às
corrotinas; cedem múltiplas vezes, possuem mais de um ponto de entrada
e sua execução pode ser suspensa. A única diferença é que uma função
geradora não pode controlar onde a execução deve continuar após o seu
rendimento; o controle é sempre transferido para o chamador do
gerador.

Expressões yield são permitidas em qualquer lugar em uma construção
"try". Se o gerador não for retomado antes de ser finalizado (ao
atingir uma contagem de referências zero ou ao ser coletado como
lixo), o método "close()" do iterador de gerador será chamado,
permitindo que quaisquer cláusulas "finally" pendentes sejam
executadas.

Quando "yield from <expr>" é usado, a expressão fornecida deve ser
iterável. Os valores produzidos pela iteração desse iterável são
passados diretamente para o chamador dos métodos do gerador atual.
Quaisquer valores passados com "send()" e quaisquer exceções passadas
com "throw()" são passados para o iterador subjacente se ele tiver os
métodos apropriados. Se este não for o caso, então "send()" irá
levantar "AttributeError" ou "TypeError", enquanto "throw()" irá
apenas levantar a exceção passada imediatamente.

Quando o iterador subjacente estiver completo, o atributo "value" da
instância "StopIteration" gerada torna-se o valor da expressão yield.
Ele pode ser definido explicitamente ao levantar "StopIteration" ou
automaticamente quando o subiterador é um gerador (retornando um valor
do subgerador).

Alterado na versão 3.3: Adicionado "yield from <expr>" para delegar o
fluxo de controle a um subiterador.

Os parênteses podem ser omitidos quando a expressão yield é a única
expressão no lado direito de uma instrução de atribuição.

Ver também:

  **PEP 255** - Geradores simples
     A proposta para adicionar geradores e a instrução "yield" ao
     Python.

  **PEP 342** - Corrotinas via Geradores Aprimorados
     A proposta de aprimorar a API e a sintaxe dos geradores,
     tornando-os utilizáveis como simples corrotinas.

  **PEP 380** - Sintaxe para Delegar a um Subgerador
     A proposta de introduzir a sintaxe "yield_from", facilitando a
     delegação a subgeradores.

  **PEP 525** - Geradores assíncronos
     A proposta que se expandiu em **PEP 492** adicionando recursos de
     gerador a funções de corrotina.


6.2.8.1. Exemplos
~~~~~~~~~~~~~~~~~

Aqui está um exemplo simples que demonstra o comportamento de
geradores e funções geradoras:

   >>> def echo(value=None):
   ...     print("A execução inicia quando 'next()' é chamada pela primeira vez.")
   ...     try:
   ...         while True:
   ...             try:
   ...                 value = (yield value)
   ...             except Exception as e:
   ...                 value = e
   ...     finally:
   ...         print("Não se esqueça de fazer uma limpeza quando 'close()' for chamada.")
   ...
   >>> generator = echo(1)
   >>> print(next(generator))
   A execução inicia quando 'next()' é chamada pela primeira vez.
   1
   >>> print(next(generator))
   None
   >>> print(generator.send(2))
   2
   >>> generator.throw(TypeError, "spam")
   TypeError('spam',)
   >>> generator.close()
   Não se esqueça de fazer uma limpeza quando 'close()' for chamada.

Para exemplos usando "yield from", consulte a PEP 380: Syntax for
Delegating to a Subgenerator em "O que há de novo no Python."


6.2.8.2. Funções geradoras assíncronas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A presença de uma expressão yield em uma função ou método definido
usando a "async def" define ainda mais a função como uma função
*geradora assíncrona*.

Quando uma função geradora assíncrona é chamada, ela retorna um
iterador assíncrono conhecido como objeto gerador assíncrono. Esse
objeto controla a execução da função geradora. Um objeto gerador
assíncrono é normalmente usado em uma instrução "async for" em uma
função de corrotina de forma análoga a como um objeto gerador seria
usado em uma instrução "for".

A chamada de um dos métodos do gerador assíncrono retorna um objeto
*aguardável*, e a execução começa quando esse objeto é aguardado.
Nesse momento, a execução prossegue até a primeira expressão yield,
onde é suspensa novamente, retornando o valor de "yield_list" para a
corrotina em aguardo. Assim como ocorre com um gerador, a suspensão
significa que todo o estado local é mantido, inclusive as ligações
atuais das variáveis locais, o ponteiro de instruções, a pilha de
avaliação interna e o estado de qualquer tratamento de exceção. Quando
a execução é retomada, aguardando o próximo objeto retornado pelos
métodos do gerador assíncrono, a função pode prosseguir exatamente
como se a expressão de rendimento fosse apenas outra chamada externa.
O valor da expressão yield após a retomada depende do método que
retomou a execução.  Se "__anext__()" for usado, o resultado será
"None". Caso contrário, se "asend()" for usado, o resultado será o
valor passado para esse método.

Se um gerador assíncrono encerrar mais cedo por "break", pela tarefa
que fez sua chamada ser cancelada ou por outras exceções, o código de
limpeza assíncrona do gerador será executado e possivelmente levantará
alguma exceção ou acessará as variáveis de contexto em um contexto
inesperado -- talvez após o tempo de vida das tarefas das quais ele
depende, ou durante o laço de eventos de encerramento quando o gancho
de coleta de lixo do gerador assíncrono for chamado. Para prevenir
isso, o chamador deve encerrar explicitamente o gerador assíncrono
chamando o método "aclose()" para finalizar o gerador e, por fim,
desconectá-lo do laço de eventos.

Em uma função geradora assíncrona, expressões de yield são permitidas
em qualquer lugar em uma construção "try". No entanto, se um gerador
assíncrono não for retomado antes de ser finalizado (alcançando uma
contagem de referência zero ou sendo coletado pelo coletor de lixo),
então uma expressão de yield dentro de um construção "try" pode
resultar em uma falha na execução das cláusulas pendentes de
"finally". Nesse caso, é responsabilidade do laço de eventos ou
escalonador que executa o gerador assíncrono chamar o método
"aclose()" do gerador iterador assíncrono e executar o objeto
corrotina resultante, permitindo assim que quaisquer cláusulas
pendentes de "finally" sejam executadas.

Para cuidar da finalização após o término do laço de eventos, um laço
de eventos deve definir uma função *finalizer* que recebe um gerador
assíncrono e provavelmente chama "aclose()" e executa a corrotina.
Este *finalizer* pode ser registrado chamando
"sys.set_asyncgen_hooks()". Quando iterado pela primeira vez, um
gerador assíncrono armazenará o *finalizer* registrado para ser
chamado na finalização. Para um exemplo de referência de um método
*finalizer*, consulte a implementação de
"asyncio.Loop.shutdown_asyncgens" em Lib/asyncio/base_events.py.

O expressão "yield from <expr>" é um erro de sintaxe quando usado em
uma função geradora assíncrona.


6.3. Primárias
==============

Primárias representam as operações mais fortemente vinculadas da
linguagem. Sua sintaxe é:

   primary: atom | attributeref | subscription | call


6.3.1. Referências de atributo
------------------------------

Uma referência de atributo é um primário seguido de um ponto e um
nome.

   attributeref: primary "." identifier

A primária deve avaliar para um objeto de um tipo que tem suporte a
referências de atributo, o que a maioria dos objetos faz. Este objeto
é então solicitado a produzir o atributo cujo nome é o identificador.
O tipo e o valor produzido são determinados pelo objeto. Várias
avaliações da mesma referência de atributo podem produzir diferentes
objetos.

Esta produção pode ser personalizada substituindo o método
"__getattribute__()" ou o método "__getattr__()". O método
"__getattribute__()" é chamado primeiro e retorna um valor ou levanta
uma "AttributeError" se o atributo não estiver disponível.

Se for levantada uma "AttributeError" e o objeto tiver um método
"__getattr__()", esse método será chamado como alternativa.


6.3.2. Subscriptions and slicings
---------------------------------

The *subscription* syntax is usually used for selecting an element
from a container -- for example, to get a value from a "dict":

   >>> digits_by_name = {'one': 1, 'two': 2}
   >>> digits_by_name['two']  # Subscripting a dictionary using the key 'two'
   2

In the subscription syntax, the object being subscribed -- a primary
-- is followed by a *subscript* in square brackets. In the simplest
case, the subscript is a single expression.

Depending on the type of the object being subscribed, the subscript is
sometimes called a *key* (for mappings), *index* (for sequences), or
*type argument* (for *generic types*). Syntactically, these are all
equivalent:

   >>> colors = ['red', 'blue', 'green', 'black']
   >>> colors[3]  # Subscripting a list using the index 3
   'black'

   >>> list[str]  # Parameterizing the list type using the type argument str
   list[str]

At runtime, the interpreter will evaluate the primary and the
subscript, and call the primary's "__getitem__()" or
"__class_getitem__()" *special method* with the subscript as argument.
For more details on which of these methods is called, see
__class_getitem__ versus __getitem__.

To show how subscription works, we can define a custom object that
implements "__getitem__()" and prints out the value of the subscript:

   >>> class SubscriptionDemo:
   ...     def __getitem__(self, key):
   ...         print(f'subscripted with: {key!r}')
   ...
   >>> demo = SubscriptionDemo()
   >>> demo[1]
   subscripted with: 1
   >>> demo['a' * 3]
   subscripted with: 'aaa'

See "__getitem__()" documentation for how built-in types handle
subscription.

Subscriptions may also be used as targets in assignment or deletion
statements. In these cases, the interpreter will call the subscripted
object's "__setitem__()" or "__delitem__()" *special method*,
respectively, instead of "__getitem__()".

   >>> colors = ['red', 'blue', 'green', 'black']
   >>> colors[3] = 'white'  # Setting item at index
   >>> colors
   ['red', 'blue', 'green', 'white']
   >>> del colors[3]  # Deleting item at index 3
   >>> colors
   ['red', 'blue', 'green']

All advanced forms of *subscript* documented in the following sections
are also usable for assignment and deletion.


6.3.2.1. Fatiamentos
~~~~~~~~~~~~~~~~~~~~

A more advanced form of subscription, *slicing*, is commonly used to
extract a portion of a sequence. In this form, the subscript is a
*slice*: up to three expressions separated by colons. Any of the
expressions may be omitted, but a slice must contain at least one
colon:

   >>> number_names = ['zero', 'one', 'two', 'three', 'four', 'five']
   >>> number_names[1:3]
   ['one', 'two']
   >>> number_names[1:]
   ['one', 'two', 'three', 'four', 'five']
   >>> number_names[:3]
   ['zero', 'one', 'two']
   >>> number_names[:]
   ['zero', 'one', 'two', 'three', 'four', 'five']
   >>> number_names[::2]
   ['zero', 'two', 'four']
   >>> number_names[:-3]
   ['zero', 'one', 'two']
   >>> del number_names[4:]
   >>> number_names
   ['zero', 'one', 'two', 'three']

When a slice is evaluated, the interpreter constructs a "slice" object
whose "start", "stop" and "step" attributes, respectively, are the
results of the expressions between the colons. Any missing expression
evaluates to "None". This "slice" object is then passed to the
"__getitem__()" or "__class_getitem__()" *special method*, as above.

   # continuing with the SubscriptionDemo instance defined above:
   >>> demo[2:3]
   subscripted with: slice(2, 3, None)
   >>> demo[::'spam']
   subscripted with: slice(None, None, 'spam')


6.3.2.2. Comma-separated subscripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The subscript can also be given as two or more comma-separated
expressions or slices:

   # continuing with the SubscriptionDemo instance defined above:
   >>> demo[1, 2, 3]
   subscripted with: (1, 2, 3)
   >>> demo[1:2, 3]
   subscripted with: (slice(1, 2, None), 3)

This form is commonly used with numerical libraries for slicing multi-
dimensional data. In this case, the interpreter constructs a "tuple"
of the results of the expressions or slices, and passes this tuple to
the "__getitem__()" or "__class_getitem__()" *special method*, as
above.

The subscript may also be given as a single expression or slice
followed by a comma, to specify a one-element tuple:

   >>> demo['spam',]
   subscripted with: ('spam',)


6.3.2.3. "Starred" subscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adicionado na versão 3.11: Expressions in *tuple_slices* may be
starred. See **PEP 646**.

The subscript can also contain a starred expression. In this case, the
interpreter unpacks the result into a tuple, and passes this tuple to
"__getitem__()" or "__class_getitem__()":

   # continuing with the SubscriptionDemo instance defined above:
   >>> demo[*range(10)]
   subscripted with: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

Starred expressions may be combined with comma-separated expressions
and slices:

   >>> demo['a', 'b', *range(3), 'c']
   subscripted with: ('a', 'b', 0, 1, 2, 'c')


6.3.2.4. Formal subscription grammar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   subscription:     primary '[' subscript ']'
   subscript:        single_subscript | tuple_subscript
   single_subscript: proper_slice | assignment_expression
   proper_slice:     [expression] ":" [expression] [ ":" [expression] ]
   tuple_subscript:  ','.(single_subscript | starred_expression)+ [',']

Recall that the "|" operator denotes ordered choice. Specifically, in
"subscript", if both alternatives would match, the first
("single_subscript") has priority.


6.3.3. Chamadas
---------------

Uma chamada chama um objeto que é um chamável (por exemplo, uma
*função*) com uma série possivelmente vazia de *argumentos*:

   call:                 primary "(" [argument_list [","] | comprehension] ")"
   argument_list:        positional_arguments ["," starred_and_keywords]
                           ["," keywords_arguments]
                         | starred_and_keywords ["," keywords_arguments]
                         | keywords_arguments
   positional_arguments: positional_item ("," positional_item)*
   positional_item:      assignment_expression | "*" expression
   starred_and_keywords: ("*" expression | keyword_item)
                         ("," "*" expression | "," keyword_item)*
   keywords_arguments:   (keyword_item | "**" expression)
                         ("," keyword_item | "," "**" expression)*
   keyword_item:         identifier "=" expression

Uma vírgula final opcional pode estar presente após os argumentos
posicionais e nomeados, mas não afeta a semântica.

O primário deve ser avaliado como um objeto que pode ser chamado
(funções definidas pelo usuário, funções embutidas, métodos de objetos
embutidos, objetos de classe, métodos de instâncias de classe e todos
os objetos que possuem um método "__call__()" são chamáveis). Todas as
expressões de argumento são avaliadas antes da tentativa de chamada.
Consulte a seção Definições de função para a sintaxe das listas
formais de *parâmetros*.

Se houver argumentos nomeados, eles serão primeiro convertidos em
argumentos posicionais, como segue. Primeiro, é criada uma lista de
slots não preenchidos para os parâmetros formais. Se houver N
argumentos posicionais, eles serão colocados nos primeiros N slots. A
seguir, para cada argumento nomeado, o identificador é usado para
determinar o slot correspondente (se o identificador for igual ao
primeiro nome formal do parâmetro, o primeiro slot será usado e assim
por diante). Se o slot já estiver preenchido, uma exceção "TypeError"
será levantada. Caso contrário, o argumento é colocado no slot,
preenchendo-o (mesmo que a expressão seja "None", ela preenche o
slot). Quando todos os argumentos forem processados, os slots ainda
não preenchidos serão preenchidos com o valor padrão correspondente da
definição da função. (Os valores padrão são calculados, uma vez,
quando a função é definida; assim, um objeto mutável, como uma lista
ou dicionário usado como valor padrão, será compartilhado por todas as
chamadas que não especificam um valor de argumento para o slot
correspondente; isso deve geralmente ser evitado.) Se houver algum
slot não preenchido para o qual nenhum valor padrão for especificado,
uma exceção "TypeError" será levantada. Caso contrário, a lista de
slots preenchidos será usada como lista de argumentos para a chamada.

Uma implementação pode fornecer funções integradas cujos parâmetros
posicionais não possuem nomes, mesmo que sejam 'nomeados' para fins de
documentação e que, portanto, não possam ser fornecidos por nomes. No
CPython, este é o caso de funções implementadas em C que usam
"PyArg_ParseTuple()" para analisar seus argumentos.

Se houver mais argumentos posicionais do que slots de parâmetros
formais, uma exceção "TypeError" será levantada, a menos que um
parâmetro formal usando a sintaxe "*identificador" esteja presente;
neste caso, esse parâmetro formal recebe uma tupla contendo os
argumentos posicionais em excesso (ou uma tupla vazia se não houver
argumentos posicionais em excesso).

Se algum argumento nomeado não corresponder a um nome de parâmetro
formal, uma exceção "TypeError" é levantada, a menos que um parâmetro
formal usando a sintaxe "**identificador" esteja presente; neste caso,
esse parâmetro formal recebe um dicionário contendo os argumentos
nomeados em excesso (usando os nomes como chaves e os valores dos
argumentos como valores correspondentes), ou um (novo) dicionário
vazio se não houver argumentos nomeados em excesso.

Se a sintaxe "*expressão" aparecer na chamada da função, "expressão"
deverá ser avaliada como *iterável*. Os elementos desses iteráveis são
tratados como se fossem argumentos posicionais adicionais. Para a
chamada "f(x1, x2, *y, x3, x4)", se *y* for avaliado como uma
sequência *y1*, ..., *yM*, isso é equivalente a uma chamada com M+4
argumentos posicionais *x1*, *x2*, *y1*, ..., *yM*, *x3*, *x4*.

Uma consequência disso é que embora a sintaxe "*expressão" possa
aparecer *depois* de argumentos nomeados explícitos, ela é processada
*antes* dos argumentos nomeados (e de quaisquer argumentos de
"**expressão" -- veja abaixo). Então:

   >>> def f(a, b):
   ...     print(a, b)
   ...
   >>> f(b=1, *(2,))
   2 1
   >>> f(a=1, *(2,))
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: f() got multiple values for keyword argument 'a'
   >>> f(1, *(2,))
   1 2

É incomum que ambos os argumentos nomeados e a sintaxe "*expressão"
sejam usados na mesma chamada, portanto, na prática, essa confusão não
surge com frequência.

Se a sintaxe "**expressão" aparecer na chamada de função, "expressão"
deve ser avaliada como um *mapeamento*, cujo conteúdo é tratado como
argumentos nomeados adicionais. Se um parâmetro que corresponde a uma
chave já recebeu um valor (por um argumento nomeado explícito ou de
outro desempacotamento), uma exceção "TypeError" é levantada.

Quando "**expressão" é usada, cada chave neste mapeamento deve ser uma
string. Cada valor do mapeamento é atribuído ao primeiro parâmetro
formal elegível para atribuição de nomeas cujo nome é igual à chave.
Uma chave não precisa ser um identificador Python (por exemplo, ""max-
temp °F"" é aceitável, embora não corresponda a nenhum parâmetro
formal que possa ser declarado). Se não houver correspondência com um
parâmetro formal, o par chave-valor é coletado pelo parâmetro "**", se
houver, ou se não houver, uma exceção "TypeError" é levantada.

Parâmetros formais usando a sintaxe "*identificador" ou
"**identificador" não podem ser usados como slots de argumentos
posicionais ou como nomes de argumentos nomeados.

Alterado na versão 3.5: Chamadas de função aceitam qualquer número de
desempacotamentos "*" e "**", argumentos posicionais podem seguir
desempacotamentos iteráveis ("*") e argumentos nomeados podem seguir
desempacotamentos de dicionário ("**"). Originalmente proposto pela
**PEP 448**.

Uma chamada sempre retorna algum valor, possivelmente "None", a menos
que levanta uma exceção. A forma como esse valor é calculado depende
do tipo do objeto chamável.

Se for...

uma função definida por usuário:
   O bloco de código da função é executado, passando-lhe a lista de
   argumentos. A primeira coisa que o bloco de código fará é vincular
   os parâmetros formais aos argumentos; isso é descrito na seção
   Definições de função. Quando o bloco de código executa uma
   instrução "return", isso especifica o valor de retorno da chamada
   de função. Se a execução atingir o final do bloco de código sem
   executar uma instrução "return", o valor de retorno será "None".

um método embutido ou uma função embutida:
   O resultado fica por conta do interpretador; veja Funções embutidas
   para descrições de funções embutidas e métodos embutidos.

um objeto classe:
   Uma nova instância dessa classe é retornada.

um método de instância de classe:
   A função correspondente definida pelo usuário é chamada, com uma
   lista de argumentos que é maior que a lista de argumentos da
   chamada: a instância se torna o primeiro argumento.

uma instância de classe:
   A classe deve definir um método "__call__()"; o efeito é então o
   mesmo como se esse método fosse chamado.


6.4. Expressão await
====================

Suspende a execução de *corrotina* em um objeto *aguardável*. Só pode
ser usado dentro de uma *função de corrotina*.

   await_expr: "await" primary

Adicionado na versão 3.5.


6.5. O operador de potência
===========================

O operador de potência vincula-se com mais força do que os operadores
unários à sua esquerda; ele se vincula com menos força do que os
operadores unários à sua direita. A sintaxe é:

   power: (await_expr | primary) ["**" u_expr]

Assim, em uma sequência sem parênteses de operadores de potência e
unários, os operadores são avaliados da direita para a esquerda (isso
não restringe a ordem de avaliação dos operandos): "-1**2" resulta em
"-1" .

The power operator has the same semantics as the built-in "pow()"
function, when called with two arguments: it yields its left argument
raised to the power of its right argument. Numeric arguments are first
converted to a common type, and the result is of that type.

Para operandos int, o resultado tem o mesmo tipo que os operandos, a
menos que o segundo argumento seja negativo; nesse caso, todos os
argumentos são convertidos em ponto flutuante e um resultado ponto
flutuante é entregue. Por exemplo, "10**2" retorna "100", mas "10**-2"
retorna "0.01".

Elevar "0.0" a uma potência negativa resulta em uma exceção
"ZeroDivisionError". Elevar um número negativo a uma potência
fracionária resulta em um número "complex". (Em versões anteriores,
levantava "ValueError".)

Esta operação pode ser personalizada usando os métodos especial
"__pow__()" e "__rpow__()".


6.6. Operações aritméticas unárias e bit a bit
==============================================

Todas as operações aritméticas unárias e bit a bit têm a mesma
prioridade:

   u_expr: power | "-" u_expr | "+" u_expr | "~" u_expr

O operador unário "-" (menos) produz a negação de seu argumento
numérico; a operação pode ser substituída pelo método especial
"__neg__()".

O operador unário "+" (mais) produz seu argumento numérico inalterado;
a operação pode ser substituída pelo método especial "__pos__()".

O operador unário "~" (inverter) produz a inversão bit a bit de seu
argumento inteiro. A inversão bit a bit de "x" é definida como
"-(x+1)". Aplica-se apenas a números inteiros ou a objetos
personalizados que substituem o método especial "__invert__()".

Em todos os três casos, se o argumento não tiver o tipo adequado, uma
exceção "TypeError" é levantada.


6.7. Operações binárias aritméticas
===================================

As operações aritméticas binárias possuem os níveis de prioridade
convencionais. Observe que algumas dessas operações também se aplicam
a determinados tipos não numéricos. Além do operador potência, existem
apenas dois níveis, um para operadores multiplicativos e outro para
operadores aditivos:

   m_expr: u_expr | m_expr "*" u_expr | m_expr "@" m_expr |
           m_expr "//" u_expr | m_expr "/" u_expr |
           m_expr "%" u_expr
   a_expr: m_expr | a_expr "+" m_expr | a_expr "-" m_expr

The "*" (multiplication) operator yields the product of its arguments.
The arguments must either both be numbers, or one argument must be an
integer and the other must be a sequence. In the former case, the
numbers are converted to a common real type and then multiplied
together.  In the latter case, sequence repetition is performed; a
negative repetition factor yields an empty sequence.

Esta operação pode ser personalizada usando os métodos especial
"__mul__()" e "__rmul__()".

Alterado na versão 3.14: Se apenas um operando for um número complexo,
o outro operando será convertido em um número de ponto flutuante.

O operador "@" (arroba) deve ser usado para multiplicação de matrizes.
Nenhum tipo embutido do Python implementa este operador.

Esta operação pode ser personalizada usando os métodos especial
"__matmul__()" e "__rmatmul__()".

Adicionado na versão 3.5.

The "/" (division) and "//" (floor division) operators yield the
quotient of their arguments.  The numeric arguments are first
converted to a common type. Division of integers yields a float, while
floor division of integers results in an integer; the result is that
of mathematical division with the 'floor' function applied to the
result.  Division by zero raises the "ZeroDivisionError" exception.

A operação de divisão pode ser personalizada usando os métodos
especiais "__truediv__()" e "__rtruediv__()". A operação de divisão
pelo piso pode ser personalizada usando os métodos especiais
"__floordiv__()" e "__rfloordiv__()".

The "%" (modulo) operator yields the remainder from the division of
the first argument by the second.  The numeric arguments are first
converted to a common type. A zero right argument raises the
"ZeroDivisionError" exception.  The arguments may be floating-point
numbers, e.g., "3.14%0.7" equals "0.34" (since "3.14" equals "4*0.7 +
0.34".)  The modulo operator always yields a result with the same sign
as its second operand (or zero); the absolute value of the result is
strictly smaller than the absolute value of the second operand [1].

Os operadores de divisão pelo piso e módulo são conectados pela
seguinte identidade: "x == (x//y)*y + (x%y)". A divisão pelo piso e o
módulo também estão conectados com a função embutida "divmod()":
"divmod(x, y) == (x//y, x%y)". [2].

Além de realizar a operação de módulo em números, o operador "%"
também é sobrecarregado por objetos string para realizar a formatação
de string no estilo antigo (também conhecida como interpolação). A
sintaxe para formatação de string é descrita na Referência da
Biblioteca Python, seção Formatação de string no estilo printf.

A operação *módulo* pode ser personalizada usando os métodos especial
"__mod__()" e "__rmod__()".

O operador de divisão pelo piso, o operador de módulo e a função
"divmod()" não são definidos para números complexos. Em vez disso,
converta para um número de ponto flutuante usando a função "abs()" se
apropriado.

The "+" (addition) operator yields the sum of its arguments.  The
arguments must either both be numbers or both be sequences of the same
type.  In the former case, the numbers are converted to a common real
type and then added together. In the latter case, the sequences are
concatenated.

Esta operação pode ser personalizada usando os métodos especial
"__add__()" e "__radd__()".

Alterado na versão 3.14: Se apenas um operando for um número complexo,
o outro operando será convertido em um número de ponto flutuante.

The "-" (subtraction) operator yields the difference of its arguments.
The numeric arguments are first converted to a common real type.

Esta operação pode ser personalizada usando os métodos especial
"__sub__()" e "__rsub__()".

Alterado na versão 3.14: Se apenas um operando for um número complexo,
o outro operando será convertido em um número de ponto flutuante.


6.8. Operações de deslocamento
==============================

As operações de deslocamento têm menor prioridade que as operações
aritméticas:

   shift_expr: a_expr | shift_expr ("<<" | ">>") a_expr

Esses operadores aceitam números inteiros como argumentos. Eles
deslocam o primeiro argumento para a esquerda ou para a direita pelo
número de bits fornecido pelo segundo argumento.

A operação de deslocamento à esquerda pode ser personalizada usando os
métodos especiais "__lshift__()" e "__rlshift__()". A operação de
deslocamento à direita pode ser personalizada usando os métodos
especiais "__rshift__()" e "__rrshift__()".

Um deslocamento para a direita de *n* bits é definido como a divisão
pelo piso por "pow(2,n)". Um deslocamento à esquerda de *n* bits é
definido como a multiplicação por "pow(2,n)".


6.9. Operações binárias bit a bit
=================================

Cada uma das três operações bit a bit tem um nível de prioridade
diferente:

   and_expr: shift_expr | and_expr "&" shift_expr
   xor_expr: and_expr | xor_expr "^" and_expr
   or_expr:  xor_expr | or_expr "|" xor_expr

O operador "&" produz o E (AND) bit a bit de seus argumentos, que
devem ser inteiros ou um deles deve ser um objeto personalizado
substituindo os métodos especiais "__and__()" ou "__rand__()".

O operador "^" produz o XOR bit a bit (OU exclusivo) de seus
argumentos, que devem ser inteiros ou um deles deve ser um objeto
personalizado sobrescrevendo os métodos especiais "__xor__()" ou
"__rxor__()".

O operador "|" produz o OU (OR) bit a bit de seus argumentos, que
devem ser inteiros ou um deles deve ser um objeto personalizado
sobrescrevendo os métodos especiais "__or__()" ou "__ror__()".


6.10. Comparações
=================

Ao contrário de C, todas as operações de comparação em Python têm a
mesma prioridade, que é menor do que qualquer operação aritmética, de
deslocamento ou bit a bit. Também diferentemente de C, expressões como
"a < b < c" têm a interpretação que é convencional em matemática:

   comparison:    or_expr (comp_operator or_expr)*
   comp_operator: "<" | ">" | "==" | ">=" | "<=" | "!="
                  | "is" ["not"] | ["not"] "in"

Comparações produzem valores booleanos: "True" ou "False". *métodos de
comparação rica* personalizados podem retornar valores não booleanos.
Neste caso, o Python chamará "bool()" nesse valor em contextos
booleanos.

As comparações podem ser encadeadas arbitrariamente, por exemplo, "x <
y <= z" é equivalente a "x < y and y <= z", exceto que "y" é avaliado
apenas uma vez (mas em ambos os casos "z" não é avaliado quando "x <
y" é considerado falso).

Formalmente, se *a*, *b*, *c*, ..., *y*, *z* são expressões e *op1*,
*op2*, ..., *opN* são operadores de comparação, então "a op1 b op2 c
... y opN z" é equivalente a "a op1 b e b op2 c e ... y opN z", exceto
que cada expressão é avaliada no máximo uma vez.

Observe que "a op1 b op2 c" não implica qualquer tipo de comparação
entre *a* e *c*, de modo que, por exemplo, "x < y > z" é perfeitamente
válido (embora talvez não seja bonito).


6.10.1. Comparações de valor
----------------------------

Os operadores "<", ">", "==", ">=", "<=" e "!=" comparam os valores de
dois objetos. Os objetos não precisam ser do mesmo tipo.

O capítulo Objetos, valores e tipos afirma que os objetos possuem um
valor (além do tipo e da identidade). O valor de um objeto é uma noção
bastante abstrata em Python: por exemplo, não existe um método de
acesso canônico para o valor de um objeto. Além disso, não há
exigência de que o valor de um objeto seja construído de uma maneira
específica, por exemplo. composto por todos os seus atributos de
dados. Os operadores de comparação implementam uma noção específica de
qual é o valor de um objeto. Pode-se pensar neles como definindo o
valor de um objeto indiretamente, por meio de sua implementação de
comparação.

Como todos os tipos são subtipos (diretos ou indiretos) de "object",
eles herdam o comportamento de comparação padrão de "object". Os tipos
podem personalizar seu comportamento de comparação implementando
*métodos de comparação rica* como "__lt__()", descrito em
Personalização básica.

O comportamento padrão para comparação de igualdade ("==" e "!=") é
baseado na identidade dos objetos. Consequentemente, a comparação da
igualdade de instâncias com a mesma identidade resulta em igualdade, e
a comparação da igualdade de instâncias com identidades diferentes
resulta em desigualdade. Uma motivação para este comportamento padrão
é o desejo de que todos os objetos sejam reflexivos (ou seja, "x is y"
implica "x == y").

Uma comparação de ordem padrão ("<", ">", "<=" e ">=") não é
fornecida; uma tentativa levanta "TypeError". Uma motivação para este
comportamento padrão é a falta de um invariante semelhante ao da
igualdade.

O comportamento da comparação de igualdade padrão, de que instâncias
com identidades diferentes são sempre desiguais, pode contrastar com o
que os tipos precisarão ter uma definição sensata de valor de objeto e
igualdade baseada em valor. Esses tipos precisarão personalizar seu
comportamento de comparação e, de fato, vários tipos embutidos fizeram
isso.

A lista a seguir descreve o comportamento de comparação dos tipos
embutidos mais importantes.

* Números de tipos numéricos embutidos (Tipos numéricos --- int,
  float, complex) e dos tipos de biblioteca padrão
  "fractions.Fraction" e "decimal.Decimal" podem ser comparados dentro
  e entre seus tipos, com a restrição que os números complexos não
  oferecem suporte a comparação de ordens. Dentro dos limites dos
  tipos envolvidos, eles comparam matematicamente (algoritmicamente)
  corretos sem perda de precisão.

  Os valores não numéricos "float('NaN')" e "decimal.Decimal('NaN')"
  são especiais. Qualquer comparação ordenada de um número com um
  valor que não é um número é falsa. Uma implicação contraintuitiva é
  que os valores que não são numéricos não são iguais a si mesmos. Por
  exemplo, se "x = float('NaN')", "3 < x", "x < 3" e "x == x" são
  todos falsos, enquanto "x != x" é verdadeiro. Esse comportamento é
  compatível com IEEE 754.

* "None" e "NotImplemented" são singletons. **PEP 8** aconselha que
  comparações para singletons devem sempre ser feitas com "is" ou "is
  not", nunca com os operadores de igualdade.

* Sequências binárias (instâncias de "bytes" ou "bytearray") podem ser
  comparadas dentro e entre seus tipos. Eles comparam
  lexicograficamente usando os valores numéricos de seus elementos.

* Strings (instâncias de "str") são comparadas lexicograficamente
  usando os pontos de código Unicode numéricos (o resultado da função
  embutida "ord()") de seus caracteres. [3]

  Strings e sequências binárias não podem ser comparadas diretamente.

* Sequências (instâncias de "tuple", "list" ou "range") podem ser
  comparadas apenas dentro de cada um de seus tipos, com a restrição
  de que intervalos não oferecem suporte a comparação de ordem. A
  comparação de igualdade entre esses tipos resulta em desigualdade, e
  a comparação ordenada entre esses tipos levanta "TypeError".

  As sequências são comparadas lexicograficamente usando a comparação
  de elementos correspondentes. Os contêineres embutidos normalmente
  presumem que objetos idênticos são iguais a si mesmos. Isso permite
  ignorar testes de igualdade para objetos idênticos para melhorar o
  desempenho e manter seus invariantes internos.

  A comparação lexicográfica entre coleções embutidas funciona da
  seguinte forma:

  * Para que duas coleções sejam comparadas iguais, elas devem ser do
    mesmo tipo, ter o mesmo comprimento e cada par de elementos
    correspondentes deve ser comparado igual (por exemplo, "[1,2] ==
    (1,2)" é false porque o tipo não é o mesmo).

  * Coleções que oferecem suporte a comparação de ordem são ordenadas
    da mesma forma que seus primeiros elementos desiguais (por
    exemplo, "[1,2,x] <= [1,2,y]" tem o mesmo valor que "x <= y"). Se
    um elemento correspondente não existir, a coleção mais curta é
    ordenada primeiro (por exemplo, "[1,2] < [1,2,3]" é verdadeiro).

* Mapeamentos (instâncias de "dict") comparam iguais se e somente se
  eles tiverem pares "(chave, valor)" iguais. A comparação de
  igualdade das chaves e valores reforça a reflexividade.

  Comparações de ordem ("<", ">", "<=" e ">=") levantam "TypeError".

* Conjuntos (instâncias de "set" ou "frozenset") podem ser comparados
  dentro e entre seus tipos.

  Eles definem operadores de comparação de ordem para significar
  testes de subconjunto e superconjunto. Essas relações não definem
  ordenações totais (por exemplo, os dois conjuntos "{1,2}" e "{2,3}"
  não são iguais, nem subconjuntos um do outro, nem superconjuntos um
  do outro). Consequentemente, conjuntos não são argumentos
  apropriados para funções que dependem de ordenação total (por
  exemplo, "min()", "max()" e "sorted()" produzem resultados
  indefinidos dada uma lista de conjuntos como entradas) .

  A comparação de conjuntos reforça a reflexividade de seus elementos.

* A maioria dos outros tipos embutidos não possui métodos de
  comparação implementados, portanto, eles herdam o comportamento de
  comparação padrão.

As classes definidas pelo usuário que personalizam seu comportamento
de comparação devem seguir algumas regras de consistência, se
possível:

* A comparação da igualdade deve ser reflexiva. Em outras palavras,
  objetos idênticos devem ser comparados iguais:

     "x is y" implica em "x == y"

* A comparação deve ser simétrica. Em outras palavras, as seguintes
  expressões devem ter o mesmo resultado:

     "x == y" e "y == x"

     "x != y" e "y != x"

     "x < y" e "y > x"

     "x <= y" e "y >= x"

* A comparação deve ser transitiva. Os seguintes exemplos (não
  exaustivos) ilustram isso:

     "x > y and y > z" implica em "x > z"

     "x < y and y <= z" implica em "x < z"

* A comparação inversa deve resultar na negação booleana. Em outras
  palavras, as seguintes expressões devem ter o mesmo resultado:

     "x == y" e "not x != y"

     "x < y" e "not x >= y" (pra classificação total)

     "x > y" e "not x <= y" (pra classificação total)

  The last two expressions apply to totally ordered collections (e.g.
  to sequences, but not to sets or mappings). See also the
  "@~functools.total_ordering" decorator.

* O resultado "hash()" deve ser consistente com a igualdade. Objetos
  iguais devem ter o mesmo valor de hash ou ser marcados como não-
  hasheáveis.

Python não impõe essas regras de consistência. Na verdade, os valores
não numéricos são um exemplo de não cumprimento dessas regras.


6.10.2. Operações de teste de pertinência
-----------------------------------------

Os operadores "in" e "not in" testam se um operando é membro ou não de
outro. "x in s" é avaliado como "True" se *x* for membro de *s*, e
"False" caso contrário. "x not in s" retorna a negação de "x in s".
Todas as sequências e tipos de conjuntos embutidos oferecem suporte a
isso, assim como o dicionário, para o qual "in" testa se o dicionário
tem uma determinada chave. Para tipos de contêiner como list, tuple,
set, frozenset, dict ou Collections.deque, a expressão "x in y" é
equivalente a "any(x is e or x == e for e in y)".

Para os tipos string e bytes, "x in y" é "True" se e somente se *x*
for uma substring de *y*. Um teste equivalente é "y.find(x) != -1".
Strings vazias são sempre consideradas uma substring de qualquer outra
string, então """ in "abc"" retornará "True".

Para classes definidas pelo usuário que definem o método
"__contains__()", "x in y" retorna "True" se "y.__contains__(x)"
retorna um valor verdadeiro, e "False" caso contrário.

Para classes definidas pelo usuário que não definem "__contains__()",
mas definem "__iter__()", "x in y" é "True" se algum valor "z", para a
qual a expressão "x is z or x == z" é verdadeira, é produzida durante
a iteração sobre "y". Se uma exceção for levantada durante a iteração,
é como se "in" tivesse levantado essa exceção.

Por último, o protocolo de iteração de estilo antigo é tentado: se uma
classe define "__getitem__()", "x in y" é "True" se, e somente se,
houver um índice inteiro não negativo *i* tal que "x is y[i] or x ==
y[i]", e nenhum índice inteiro inferior levanta a exceção
"IndexError". (Se qualquer outra exceção for levantada, é como se "in"
levantasse essa exceção).

O operador "not in" é definido para ter o valor verdade inverso de
"in".


6.10.3. Comparações de identidade
---------------------------------

Os operadores "is" e "is not" testam a identidade de um objeto: "x is
y" é verdadeiro se, e somente se, *x* e *y* são o mesmo objeto. A
identidade de um objeto é determinada usando a função "id()". "x is
not y" produz o valor verdade inverso. [4]


6.11. Operações booleanas
=========================

   or_test:  and_test | or_test "or" and_test
   and_test: not_test | and_test "and" not_test
   not_test: comparison | "not" not_test

No contexto de operações booleanas, e também quando expressões são
usadas por instruções de fluxo de controle, os seguintes valores são
interpretados como falsos: "False", "None", zero numérico de todos os
tipos e strings e contêineres vazios (incluindo strings, tuplas,
listas, dicionários, conjuntos e frozensets). Todos os outros valores
são interpretados como verdadeiros. Objetos definidos pelo usuário
podem personalizar seu valor verdade fornecendo um método
"__bool__()".

O operador "not" produz "True" se seu argumento for falso, "False"
caso contrário.

A expressão "x and y" primeiro avalia *x*; se *x* for falso, seu valor
será retornado; caso contrário, *y* será avaliado e o valor resultante
será retornado.

A expressão "x or y" primeiro avalia *x*; se *x* for verdadeiro, seu
valor será retornado; caso contrário, *y* será avaliado e o valor
resultante será retornado.

Observe que nem "and" nem "or" restringem o valor e o tipo que
retornam para "False" e "True", mas sim retornam o último argumento
avaliado. Isso às vezes é útil, por exemplo, se "s" é uma string que
deve ser substituída por um valor padrão se estiver vazia, a expressão
"s or 'foo'" produz o valor desejado. Como "not" precisa criar um novo
valor, ele retorna um valor booleano independente do tipo de seu
argumento (por exemplo, "not 'foo'" produz "False" em vez de "''".)


6.12. Expressões de atribuição
==============================

   assignment_expression: [identifier ":="] expression

Uma expressão de atribuição (às vezes também chamada de "expressão
nomeada" ou "morsa") atribui uma "expression" a um "identifier", ao
mesmo tempo que retorna o valor de "expression".

Um caso de uso comum é ao lidar com expressões regulares
correspondentes:

   if matching := pattern.search(data):
       do_something(matching)

Ou, ao processar um fluxo de arquivos em partes:

   while chunk := file.read(9000):
       process(chunk)

As expressões de atribuição devem ser colocadas entre parênteses
quando usadas como instruções de expressão e quando usadas como
subexpressões em expressões de fatiamento, condicionais, de lambda, de
argumento nomeado e de "if" de compreensão e em instruções "assert",
"with" e "assignment". Em todos os outros lugares onde eles podem ser
usados, os parênteses não são necessários, inclusive nas instruções
"if" e "while".

Adicionado na versão 3.8: Veja **PEP 572** para mais detalhes sobre
expressões de atribuição.


6.13. Expressões condicionais
=============================

   conditional_expression: or_test ["if" or_test "else" expression]
   expression:             conditional_expression | lambda_expr

Uma expressão condicional (às vezes chamada de "operador ternário") é
uma alternativa à instrução if-else. Como é uma expressão, ela retorna
um valor e pode aparecer como uma subexpressão.

A expressão "x if C else y" primeiro avalia a condição, *C* em vez de
*x*. Se *C* for verdadeiro, *x* é avaliado e seu valor é retornado;
caso contrário, *y* será avaliado e seu valor será retornado.

Veja **PEP 308** para mais detalhes sobre expressões condicionais.


6.14. Lambdas
=============

   lambda_expr: "lambda" [parameter_list] ":" expression

Expressões lambda (às vezes chamadas de funções lambda) são usadas
para criar funções anônimas. A expressão "lambda parameters:
expression" produz um objeto função. O objeto sem nome se comporta
como um objeto de função definido com:

   def <lambda>(parâmetros):
       return expressão

Veja a seção Definições de função para a sintaxe das listas de
parâmetros. Observe que as funções criadas com expressões lambda não
podem conter instruções ou anotações.


6.15. Listas de expressões
==========================

   starred_expression:       "*" or_expr | expression
   flexible_expression:      assignment_expression | starred_expression
   flexible_expression_list: flexible_expression ("," flexible_expression)* [","]
   starred_expression_list:  starred_expression ("," starred_expression)* [","]
   expression_list:          expression ("," expression)* [","]
   yield_list:               expression_list | starred_expression "," [starred_expression_list]

Exceto quando parte de uma sintaxe de criação de lista ou conjunto,
uma lista de expressões contendo pelo menos uma vírgula produz uma
tupla. O comprimento da tupla é o número de expressões na lista. As
expressões são avaliadas da esquerda para a direita.

Uma vírgula final é necessária apenas para criar uma tupla de um item,
como "1,"; é opcional em todos os outros casos. Uma única expressão
sem vírgula final não cria uma tupla, mas produz o valor dessa
expressão. (Para criar uma tupla vazia, use um par vazio de
parênteses: "()".)


6.15.1. Iterable unpacking
--------------------------

In an expression list or tuple, list or set display, any expression
may be prefixed with an asterisk ("*"). This denotes *iterable
unpacking*.

At runtime, the asterisk-prefixed expression must evaluate to an
*iterable*. The iterable is expanded into a sequence of items, which
are included in the new tuple, list, or set, at the site of the
unpacking.

Adicionado na versão 3.5: Desempacotamento de iterável em listas de
expressões, originalmente proposta pela **PEP 448**.

Adicionado na versão 3.11: Qualquer item em uma lista de expressões
pode ser estrelado. Veja a **PEP 646**.


6.16. Ordem de avaliação
========================

Python avalia expressões da esquerda para a direita. Observe que ao
avaliar uma tarefa, o lado direito é avaliado antes do lado esquerdo.

Nas linhas a seguir, as expressões serão avaliadas na ordem aritmética
de seus sufixos:

   expr1, expr2, expr3, expr4
   (expr1, expr2, expr3, expr4)
   {expr1: expr2, expr3: expr4}
   expr1 + expr2 * (expr3 - expr4)
   expr1(expr2, expr3, *expr4, **expr5)
   expr3, expr4 = expr1, expr2


6.17. Precedência de operadores
===============================

A tabela a seguir resume a precedência de operadores no Python, da
precedência mais alta (mais vinculativa) à precedência mais baixa
(menos vinculativa). Os operadores na mesma caixa têm a mesma
precedência. A menos que a sintaxe seja fornecida explicitamente, os
operadores são binários. Os operadores na mesma caixa agrupam-se da
esquerda para a direita (exceto exponenciação e expressões
condicionais, que agrupam da direita para a esquerda).

Observe que comparações, testes de pertinência e testes de identidade
têm todos a mesma precedência e possuem um recurso de encadeamento da
esquerda para a direita, conforme descrito na seção Comparações.

+-------------------------------------------------+---------------------------------------+
| Operador                                        | Descrição                             |
|=================================================|=======================================|
| "(expressions...)",  "[expressões...]",         | Expressão entre parênteses ou de      |
| "{chave: valor...}", "{expressões...}"          | ligação, sintaxe de criação de lista, |
|                                                 | sintaxe de criação de dicionário,     |
|                                                 | sintaxe de criação de conjunto        |
+-------------------------------------------------+---------------------------------------+
| "x[index]", "x[index:index]" "x(arguments...)", | Subscription (including slicing),     |
| "x.attribute"                                   | call, attribute reference             |
+-------------------------------------------------+---------------------------------------+
| "await x"                                       | Expressão await                       |
+-------------------------------------------------+---------------------------------------+
| "**"                                            | Exponenciação [5]                     |
+-------------------------------------------------+---------------------------------------+
| "+x", "-x", "~x"                                | positivo, negativo, NEGAÇÃO (NOT) bit |
|                                                 | a bit                                 |
+-------------------------------------------------+---------------------------------------+
| "*", "@", "/", "//", "%"                        | Multiplicação, multiplicação de       |
|                                                 | matrizes, divisão, divisão pelo piso, |
|                                                 | resto [6]                             |
+-------------------------------------------------+---------------------------------------+
| "+", "-"                                        | Adição e subtração                    |
+-------------------------------------------------+---------------------------------------+
| "<<", ">>"                                      | Deslocamentos                         |
+-------------------------------------------------+---------------------------------------+
| "&"                                             | E (AND) bit a bit                     |
+-------------------------------------------------+---------------------------------------+
| "^"                                             | OU EXCLUSIVO (XOR) bit a bit          |
+-------------------------------------------------+---------------------------------------+
| "|"                                             | OU (OR) bit a bit                     |
+-------------------------------------------------+---------------------------------------+
| "in", "not in", "is", "is not", "<", "<=", ">", | Comparações, incluindo testes de      |
| ">=", "!=", "=="                                | pertinência e testes de identidade    |
+-------------------------------------------------+---------------------------------------+
| "not x"                                         | NEGAÇÃO (NOT) booleana                |
+-------------------------------------------------+---------------------------------------+
| "and"                                           | E (AND) booleano                      |
+-------------------------------------------------+---------------------------------------+
| "or"                                            | OU (OR) booleano                      |
+-------------------------------------------------+---------------------------------------+
| "if" -- "else"                                  | Expressão condicional                 |
+-------------------------------------------------+---------------------------------------+
| "lambda"                                        | Expressão lambda                      |
+-------------------------------------------------+---------------------------------------+
| ":="                                            | Expressão de atribuição               |
+-------------------------------------------------+---------------------------------------+

-[ Notas de rodapé ]-

[1] Embora "abs(x%y) < abs(y)" seja verdadeiro matematicamente, para
    números flutuantes pode não ser verdadeiro numericamente devido ao
    arredondamento. Por exemplo, e presumindo uma plataforma na qual
    um float Python seja um número de precisão dupla IEEE 754, para
    que "-1e-100 % 1e100" tenha o mesmo sinal que "1e100", o resultado
    calculado é "-1e-100 + 1e100", que é numericamente exatamente
    igual a "1e100". A função "math.fmod()" retorna um resultado cujo
    sinal corresponde ao sinal do primeiro argumento e, portanto,
    retorna "-1e-100" neste caso. Qual abordagem é mais apropriada
    depende da aplicação.

[2] Se x estiver muito próximo de um múltiplo inteiro exato de y, é
    possível que "x//y" seja maior que "(x-x%y)//y" devido ao
    arredondamento. Nesses casos, Python retorna o último resultado,
    para preservar que "divmod(x,y)[0] * y + x % y" esteja muito
    próximo de "x".

[3] O padrão Unicode distingue entre *pontos de código* (por exemplo,
    U+0041) e *caracteres abstratos* (por exemplo, "LATIN CAPITAL
    LETTER A"). Embora a maioria dos caracteres abstratos em Unicode
    sejam representados apenas por meio de um ponto de código, há
    vários caracteres abstratos que também podem ser representados por
    meio de uma sequência de mais de um ponto de código. Por exemplo,
    o caractere abstrato "LATIN CAPITAL LETTER C WITH CEDILLA" pode
    ser representado como um único *caractere pré-composto* na posição
    de código U+00C7, ou como uma sequência de um *caractere base* na
    posição de código U+0043 (LATIN CAPITAL LETTER C), seguido por um
    *caractere de combinação* na posição de código U+0327 (COMBINING
    CEDILLA).

    Os operadores de comparação em strings são comparados no nível dos
    pontos de código Unicode. Isso pode ser contraintuitivo para os
    humanos. Por exemplo, ""\u00C7" == "\u0043\u0327"" é "False",
    mesmo que ambas as strings representem o mesmo caractere abstrato
    "LATIN CAPITAL LETTER C WITH CEDILLA".

    Para comparar strings no nível de caracteres abstratos (ou seja,
    de uma forma intuitiva para humanos), use
    "unicodedata.normalize()".

[4] Devido à coleta de lixo automática, às listas livres e à natureza
    dinâmica dos descritores, você pode notar um comportamento
    aparentemente incomum em certos usos do operador "is", como
    aqueles que envolvem comparações entre métodos de instância ou
    constantes. Confira a documentação para obter mais informações.

[5] O operador de potência "**" liga-se com menos força do que um
    operador aritmético ou unário bit a bit à sua direita, ou seja,
    "2**-1" é "0.5".

[6] O operador "%" também é usado para formatação de strings; a mesma
    precedência se aplica.
