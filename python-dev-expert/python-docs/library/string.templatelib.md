"string.templatelib" --- Suporte para literais de string template
*****************************************************************

**Código-fonte:** Lib/string/templatelib.py

======================================================================

Ver também:

  * Strings de formatação

  * Sintaxe de literal de string template (t-string)

  * **PEP 750**


Strings template
================

Adicionado na versão 3.14.

Strings template são um mecanismo para processamento personalizado de
strings. Elas têm toda a flexibilidade das Literais de strings
formatadas do Python, mas retornam uma instância "Template" que dá
acesso às partes estáticas e interpoladas (entre chaves) de uma string
*antes* de serem combinadas.

Para escrever uma t-string, use um prefixo "'t'" em vez de "'f'",
assim:

   >>> pi = 3.14
   >>> t't-strings são novas no Python {pi!s}!'
   Template(
      strings=('t-strings são novas no Python ', '!'),
      interpolations=(Interpolation(3.14, 'pi', 's', ''),)
   )


Tipos
=====

class string.templatelib.Template

   A classe "Template" descreve o conteúdo de uma string template. Ela
   é imutável, o que significa que os atributos de um template não
   podem ser reatribuídos.

   A maneira mais comum de criar uma instância de "Template" é usar a
   sintaxe de literal de string template. Essa sintaxe é idêntica à de
   f-strings, exceto pelo fato de usar um prefixo "t" no lugar de um
   "f":

   >>> cheese = 'Red Leicester'
   >>> template = t"We're fresh out of {cheese}, sir."
   >>> type(template)
   <class 'string.templatelib.Template'>

   Os templates são armazenados como sequências de literais "strings"
   e dinâmicos "interpolations". Um atributo "values" contém os
   valores das interpolações:

   >>> cheese = 'Camembert'
   >>> template = t'Ah! We do have {cheese}.'
   >>> template.strings
   ('Ah! We do have ', '.')
   >>> template.interpolations
   (Interpolation('Camembert', ...),)
   >>> template.values
   ('Camembert',)

   A tupla "strings" tem um elemento a mais que "interpolations" e
   "values"; as interpolações "pertencem" às strings. Isso pode ser
   mais fácil de entender quando as tuplas estão alinhadas

      template.strings:  ('Ah! We do have ',              '.')
      template.values:   (                   'Camembert',    )

   -[ Atributos ]-

   strings: tuple[str, ...]

      Uma "tuple" das strings estáticas no template.

      >>> cheese = 'Camembert'
      >>> template = t'Ah! We do have {cheese}.'
      >>> template.strings
      ('Ah! We do have ', '.')

      Strings vazias *estão* incluídas na tupla:

      >>> response = 'We do have '
      >>> cheese = 'Camembert'
      >>> template = t'Ah! {response}{cheese}.'
      >>> template.strings
      ('Ah! ', '', '.')

      A tupla "strings" nunca está vazia e sempre contém uma string a
      mais que as tuplas "interpolations" e "values":

      >>> t''.strings
      ('',)
      >>> t''.values
      ()
      >>> t'{'cheese'}'.strings
      ('', '')
      >>> t'{'cheese'}'.values
      ('cheese',)

   interpolations: tuple[Interpolation, ...]

      Uma "tuple" das interpolações no template.

      >>> cheese = 'Camembert'
      >>> template = t'Ah! We do have {cheese}.'
      >>> template.interpolations
      (Interpolation('Camembert', 'cheese', None, ''),)

      A tupla "interpolações" pode estar vazia e sempre contém um
      valor a menos que a tupla "strings":

      >>> t'Red Leicester'.interpolations
      ()

   values: tuple[object, ...]

      Uma tupla de todos os valores interpolados no template.

      >>> cheese = 'Camembert'
      >>> template = t'Ah! We do have {cheese}.'
      >>> template.values
      ('Camembert',)

      A tupla "values" sempre tem o mesmo comprimento que a tupla
      "interpolations". Isso sempre equivale a "tuple(i.value for i in
      template.interpolations)".

   -[ Métodos ]-

   __new__(*args: str | Interpolation)

      Embora a sintaxe de literal seja a maneira mais comum de criar
      um "Template", também é possível criá-las diretamente usando o
      construtor:

      >>> from string.templatelib import Interpolation, Template
      >>> cheese = 'Camembert'
      >>> template = Template(
      ...     'Ah! We do have ', Interpolation(cheese, 'cheese'), '.'
      ... )
      >>> list(template)
      ['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']

      Se várias strings forem passadas consecutivamente, elas serão
      concatenadas em um único valor no atributo "strings". Por
      exemplo, o código a seguir cria uma "Template" com uma única
      string final:

      >>> from string.templatelib import Template
      >>> template = Template('Ah! We do have ', 'Camembert', '.')
      >>> template.strings
      ('Ah! We do have Camembert.',)

      Se várias interpolações forem passadas consecutivamente, elas
      serão tratadas como interpolações separadas e uma string vazia
      será inserida entre elas. Por exemplo, o código a seguir cria um
      modelo com espaços reservados vazios no atributo "strings":

      >>> from string.templatelib import Interpolation, Template
      >>> template = Template(
      ...     Interpolation('Camembert', 'cheese'),
      ...     Interpolation('.', 'punctuation'),
      ... )
      >>> template.strings
      ('', '', '')

   iter(template)

      Itera sobre o template, produzindo cada string não-vazia e
      "Interpolation" em ordem correta.

      >>> cheese = 'Camembert'
      >>> list(t'Ah! We do have {cheese}.')
      ['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']

      Cuidado:

        Strings vazias *não* são incluídas na iteração:

        >>> response = 'We do have '
        >>> cheese = 'Camembert'
        >>> list(t'Ah! {response}{cheese}.')
        ['Ah! ',
         Interpolation('We do have ', 'response', None, ''),
         Interpolation('Camembert', 'cheese', None, ''),
         '.']

   template + other
   template += other

      Concatena este template com outro, retornando uma nova instância
      "Template":

      >>> cheese = 'Camembert'
      >>> list(t'Ah! ' + t'We do have {cheese}.')
      ['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']

      A concatenação de uma "Template" e uma "str" **não** é
      suportada. Isso ocorre porque não está claro se a string deve
      ser tratada como uma string estática ou uma interpolação. Se
      você quiser concatenar uma "Template" com uma string, você deve
      encapsular a string diretamente em uma "Template" (para tratá-la
      como uma string estática) ou usar uma "Interpolation" (para
      tratá-la como dinâmica):

      >>> from string.templatelib import Interpolation, Template
      >>> template = t'Ah! '
      >>> # Treat 'We do have ' as a static string
      >>> template += Template('We do have ')
      >>> # Treat cheese as an interpolation
      >>> cheese = 'Camembert'
      >>> template += Template(Interpolation(cheese, 'cheese'))
      >>> list(template)
      ['Ah! We do have ', Interpolation('Camembert', 'cheese', None, '')]

class string.templatelib.Interpolation

   O tipo "Interpolation" representa uma expressão dentro de uma
   string template. É imutável, o que significa que os atributos de
   uma interpolação não podem ser reatribuídos.

   As interpolações oferecem suporte à correspondência de padrões,
   permitindo que você compare seus atributos com a instrução match:

   >>> from string.templatelib import Interpolation
   >>> interpolation = t'{1. + 2.:.2f}'.interpolations[0]
   >>> interpolation
   Interpolation(3.0, '1. + 2.', None, '.2f')
   >>> match interpolation:
   ...     case Interpolation(value, expression, conversion, format_spec):
   ...         print(value, expression, conversion, format_spec, sep=' | ')
   ...
   3.0 | 1. + 2. | None | .2f

   As interpolações são genéricas em relação aos tipos dos seus
   valores.

   -[ Atributos ]-

   value: object

      O valor avaliado da interpolação.

      >>> t'{1 + 2}'.interpolations[0].value
      3

   expression: str

      Para interpolações criadas por literais de t-string,
      "expression" é o texto da expressão encontrado dentro das chaves
      ("{" e "}"), incluindo quaisquer espaços em branco, excluindo as
      próprias chaves e terminando antes do primeiro "!", ":" ou "=",
      se houver algum. Para interpolações criadas manualmente,
      "expression" é a string arbitrária fornecida ao construir a
      instância de interpolação.

      Recomendamos usar expressões Python válidas ou a string vazia
      para o campo "expression" de instâncias "Interpolation" criadas
      manualmente, embora isso não seja imposto em tempo de execução.

      >>> t'{1 + 2}'.interpolations[0].expression
      '1 + 2'

   conversion: Literal['a', 'r', 's'] | None

      A conversão a ser aplicada ao valor, ou "None".

      O "conversion" é a conversão opcional a ser aplicada ao valor:

      >>> t'{1 + 2!a}'.interpolations[0].conversion
      'a'

      Nota:

        Ao contrário das f-strings, onde as conversões são aplicadas
        automaticamente, o comportamento esperado com t-strings é que
        o código que *processa* o "Template" decidirá como interpretar
        e se aplicará o "conversion". Por conveniência, a função
        "convert()" pode ser usada para imitar a semântica de
        conversão de f-strings.

   format_spec: str

      A especificação de formato a ser aplicada ao valor.

      O "format_spec" é uma string arbitrária opcional usada como
      especificação de formato para apresentar o valor:

      >>> t'{1 + 2:.2f}'.interpolations[0].format_spec
      '.2f'

      Nota:

        Ao contrário das f-strings, onde as especificações de formato
        são aplicadas automaticamente por meio do protocolo
        "format()", o comportamento esperado com t-strings é que o
        código que *processa* a interpolação decida como interpretar e
        se a especificação de formato deve ser aplicada. Como
        resultado, os valores "format_spec" em interpolações podem ser
        strings arbitrárias, incluindo aquelas que não estão em
        conformidade com o protocolo de "format()".

   -[ Métodos ]-

   __new__(value: object, expression: str, conversion: Literal['a', 'r', 's'] | None = None, format_spec: str = '')

      Cria um novo objeto "Interpolation" a partir de partes do
      componente.

      Parâmetros:
         * **value** -- O resultado avaliado e dentro do escopo da
           interpolação.

         * **expression** -- O texto de uma expressão Python válida ou
           uma string vazia.

         * **conversion** -- A conversão a ser usada, uma entre
           "None", "'a'", "'r'" ou "'s'".

         * **format_spec** -- Uma string arbitrária opcional usada
           como especificação de formato para apresentar o valor.


Funções auxiliares
==================

string.templatelib.convert(obj, /, conversion)

   Aplica a semântica de conversão de literal de string formatada ao
   objeto *obj* fornecido. Isso é frequentemente útil para lógica de
   processamento de string template personalizada.

   Atualmente, há três sinalizadores de conversão suportados:

   * "'s'" que chama "str()" no valor (como "!s"),

   * "'r'" que chama "repr()" (como "!r") e

   * "'a'" que chama "ascii()" (como "!a").

   Se o sinalizador de conversão é "None", *obj* é retornado sem
   alterações.
