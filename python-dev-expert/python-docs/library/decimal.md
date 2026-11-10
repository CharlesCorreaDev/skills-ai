"decimal" --- Aritmética de ponto fixo decimal e ponto flutuante
****************************************************************

**Código-fonte:** Lib/decimal.py

======================================================================

O módulo "decimal" fornece suporte à aritmética rápida de ponto
flutuante decimal, com arredondamento correto. Oferece várias
vantagens sobre o tipo de dados "float":

* Decimal "é baseado em um modelo de ponto flutuante que foi projetado
  com as pessoas em mente e necessariamente tem um princípio
  orientador primordial -- os computadores devem fornecer uma
  aritmética que funcione da mesma maneira que a aritmética que as
  pessoas aprendem na escola". -- Trecho da especificação aritmética
  decimal.

* Os números decimais podem ser representados exatamente. Por outro
  lado, números como "1.1" e "2.2" não têm representações exatas em
  ponto flutuante binário. Os usuários finais normalmente não esperam
  que "1.1 + 2.2" sejam exibidos como "3.3000000000000003", como
  ocorre com o ponto flutuante binário.

* A exatidão transita para a aritmética. No ponto flutuante decimal,
  "0.1 + 0.1 + 0.1 - 0.3" é exatamente igual a zero. No ponto
  flutuante binário, o resultado é "5.5511151231257827e-017". Embora
  próximas de zero, as diferenças impedem o teste de igualdade
  confiável, e podem se acumular. Por esse motivo, o decimal é
  preferido em aplicações de contabilidade que envolvem invariáveis
  estritos de igualdade.

* O módulo decimal incorpora uma noção de casas significativas para
  que "1.30 + 1.20" seja "2.50". O zero à direita é mantido para
  indicar significância. Esta é a apresentação habitual para
  aplicações monetárias. Para multiplicação, a abordagem "livro
  escolar" usa todas as figuras nos multiplicandos. Por exemplo, "1.3
  * 1.2" é igual a "1.56" enquanto "1.30 * 1.20" é igual a "1.5600".

* Diferentemente do ponto flutuante binário baseado em hardware, o
  módulo decimal possui uma precisão alterável pelo usuário (padrão de
  28 casas), que pode ser tão grande quanto necessário para um
  determinado problema:

  >>> from decimal import *
  >>> getcontext().prec = 6
  >>> Decimal(1) / Decimal(7)
  Decimal('0.142857')
  >>> getcontext().prec = 28
  >>> Decimal(1) / Decimal(7)
  Decimal('0.1428571428571428571428571429')

* O ponto flutuante binário e decimal é implementado em termos de
  padrões publicados. Enquanto o tipo ponto flutuante embutido expõe
  apenas uma parte modesta de seus recursos, o módulo decimal expõe
  todas as partes necessárias do padrão. Quando necessário, o
  programador tem controle total sobre o arredondamento e o manuseio
  do sinal. Isso inclui uma opção para impor aritmética exata usando
  exceções para bloquear quaisquer operações inexatas.

* O módulo decimal foi projetado para dar suporte, "sem prejuízo, à
  aritmética decimal não arredondada exata (às vezes chamada de
  aritmética de ponto fixo) e à aritmética arredondada de ponto
  flutuante". -- Trecho da especificação aritmética decimal.

O design do módulo é centrado em torno de três conceitos: o número
decimal, o contexto da aritmética e os sinais.

Um número decimal é imutável. Possui um sinal, dígitos de coeficiente
e um expoente. Para preservar a significância, os dígitos do
coeficiente não truncam zeros à direita. Os decimais também incluem
valores especiais, tais como "Infinity", "-Infinity" e "NaN". O padrão
também diferencia "-0" de "+0".

O contexto da aritmética é um ambiente que especifica precisão, regras
de arredondamento, limites de expoentes, sinalizadores indicando os
resultados das operações e ativadores de interceptação que determinam
se os sinais são tratados como exceções. As opções de arredondamento
incluem "ROUND_CEILING", "ROUND_DOWN", "ROUND_FLOOR",
"ROUND_HALF_DOWN", "ROUND_HALF_EVEN", "ROUND_HALF_UP", "ROUND_UP" e
"ROUND_05UP".

Sinais são grupos de condições excepcionais que surgem durante o curso
da computação. Dependendo das necessidades da aplicação, os sinais
podem ser ignorados, considerados informativos ou tratados como
exceções. Os sinais no módulo decimal são: "Clamped",
"InvalidOperation", "DivisionByZero", "Inexact", "Rounded",
"Subnormal", "Overflow", "Underflow" e "FloatOperation".

Para cada sinal, há um sinalizador e um ativador de interceptação.
Quando um sinal é encontrado, seu sinalizador é definido como um e, se
o ativador de interceptação estiver definido como um, uma exceção será
gerada. Os sinalizadores são fixos; portanto, o usuário precisa
redefini-los antes de monitorar um cálculo.

Ver também:

  * A especificação geral aritmética decimal da IBM, The General
    Decimal Arithmetic Specification.


Tutorial de início rápido
=========================

O início usual do uso de decimais é importar o módulo, exibir o
contexto atual com "getcontext()" e, se necessário, definir novos
valores para precisão, arredondamento ou armadilhas ativadas:

   >>> from decimal import *
   >>> getcontext()
   Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
           capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
           InvalidOperation])

   >>> getcontext().prec = 7       # Define uma nova precisão

Instâncias decimais podem ser construídas a partir de números
inteiros, strings, valores ponto flutuante ou tuplas. A construção a
partir de um número inteiro ou de um ponto flutuante realiza uma
conversão exata do valor desse número inteiro ou ponto flutuante. Os
números decimais incluem valores especiais como "NaN", que significa
"Não é um número", "Infinity" positivo e negativo e "-0":

   >>> getcontext().prec = 28
   >>> Decimal(10)
   Decimal('10')
   >>> Decimal('3.14')
   Decimal('3.14')
   >>> Decimal(3.14)
   Decimal('3.140000000000000124344978758017532527446746826171875')
   >>> Decimal((0, (3, 1, 4), -2))
   Decimal('3.14')
   >>> Decimal(str(2.0 ** 0.5))
   Decimal('1.4142135623730951')
   >>> Decimal(2) ** Decimal('0.5')
   Decimal('1.414213562373095048801688724')
   >>> Decimal('NaN')
   Decimal('NaN')
   >>> Decimal('-Infinity')
   Decimal('-Infinity')

Se o sinal "FloatOperation" está ativado, a mistura acidental de
decimais e pontos flutuantes em construtores ou comparações de
ordenação levanta uma exceção:

   >>> c = getcontext()
   >>> c.traps[FloatOperation] = True
   >>> Decimal(3.14)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
   >>> Decimal('3.5') < 3.7
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
   >>> Decimal('3.5') == 3.5
   True

Adicionado na versão 3.3.

A significância de um novo Decimal é determinada unicamente pelo
número de dígitos introduzidos. A precisão e o arredondamento do
contexto só entram em jogo nas operações aritméticas.

   >>> getcontext().prec = 6
   >>> Decimal('3.0')
   Decimal('3.0')
   >>> Decimal('3.1415926535')
   Decimal('3.1415926535')
   >>> Decimal('3.1415926535') + Decimal('2.7182818285')
   Decimal('5.85987')
   >>> getcontext().rounding = ROUND_UP
   >>> Decimal('3.1415926535') + Decimal('2.7182818285')
   Decimal('5.85988')

Se os limites internos da versão C forem excedidos, a construção de um
decimal levanta "InvalidOperation":

   >>> Decimal("1e9999999999999999999")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]

Alterado na versão 3.3.

Os decimais interagem bem com grande parte do resto do Python. Aqui
está um pequeno circo voador de ponto flutuante decimal:

   >>> data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
   >>> max(data)
   Decimal('9.25')
   >>> min(data)
   Decimal('0.03')
   >>> sorted(data)
   [Decimal('0.03'), Decimal('1.00'), Decimal('1.34'), Decimal('1.87'),
    Decimal('2.35'), Decimal('3.45'), Decimal('9.25')]
   >>> sum(data)
   Decimal('19.29')
   >>> a,b,c = data[:3]
   >>> str(a)
   '1.34'
   >>> float(a)
   1.34
   >>> round(a, 1)
   Decimal('1.3')
   >>> int(a)
   1
   >>> a * 5
   Decimal('6.70')
   >>> a * b
   Decimal('2.5058')
   >>> c % a
   Decimal('0.77')

Decimais podem ser formatados (com "format()"  ou Literais de strings
formatadas) em notação de ponto fixo ou científica, usando a mesma
sintaxe para formatação (consulte Minilinguagem de especificação de
formato ) do tipo embutido "float":

   >>> format(Decimal('2.675'), "f")
   '2.675'
   >>> format(Decimal('2.675'), ".2f")
   '2.68'
   >>> f"{Decimal('2.675'):.2f}"
   '2.68'
   >>> format(Decimal('2.675'), ".2e")
   '2.68e+0'
   >>> with localcontext() as ctx:
   ...     ctx.rounding = ROUND_DOWN
   ...     print(format(Decimal('2.675'), ".2f"))
   ...
   2.67

E algumas funções matemáticas também estão disponíveis para Decimal:

>>> getcontext().prec = 28
>>> Decimal(2).sqrt()
Decimal('1.414213562373095048801688724')
>>> Decimal(1).exp()
Decimal('2.718281828459045235360287471')
>>> Decimal('10').ln()
Decimal('2.302585092994045684017991455')
>>> Decimal('10').log10()
Decimal('1')

O método "quantize()" arredonda um número para um expoente fixo. Esse
método é útil para aplicações monetárias que geralmente arredondam os
resultados para um número fixo de casas:

>>> Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN)
Decimal('7.32')
>>> Decimal('7.325').quantize(Decimal('1.'), rounding=ROUND_UP)
Decimal('8')

Como mostrado acima, a função "getcontext()" acessa o contexto atual e
permite alterar as configurações. Essa abordagem atende às
necessidades da maioria das aplicações.

Para trabalhos mais avançados, pode ser útil criar contextos
alternativos usando o construtor "Context()". Para ativar uma
alternativa, use a função "setcontext()".

De acordo com o padrão, o módulo "decimal" fornece dois contextos
padrão prontos para uso, "BasicContext" e "ExtendedContext". O
primeiro é especialmente útil para depuração porque muitas das
armadilhas estão ativadas:

   >>> myothercontext = Context(prec=60, rounding=ROUND_HALF_DOWN)
   >>> setcontext(myothercontext)
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857142857142857142857142857142857142857142857142857142857')

   >>> ExtendedContext
   Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
           capitals=1, clamp=0, flags=[], traps=[])
   >>> setcontext(ExtendedContext)
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857143')
   >>> Decimal(42) / Decimal(0)
   Decimal('Infinity')

   >>> setcontext(BasicContext)
   >>> Decimal(42) / Decimal(0)
   Traceback (most recent call last):
     File "<pyshell#143>", line 1, in -toplevel-
       Decimal(42) / Decimal(0)
   DivisionByZero: x / 0

Os contextos também contêm sinalizadores para monitorar condições
excepcionais identificadas durante os cálculos. Os sinalizadores
permanecem definidos até que sejam explicitamente limpos, portanto, é
melhor limpar os sinalizadores antes de cada conjunto de cálculos
monitorados usando o método "clear_flags()".

   >>> setcontext(ExtendedContext)
   >>> getcontext().clear_flags()
   >>> Decimal(355) / Decimal(113)
   Decimal('3.14159292')
   >>> getcontext()
   Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
           capitals=1, clamp=0, flags=[Inexact, Rounded], traps=[])

A entrada *flags* indica que a aproximação racional de pi foi
arredondada (os dígitos além da precisão do contexto foram
descartados) e que o resultado é inexato (alguns desses dígitos
descartados eram diferentes de zero).

Armadilhas individuais são definidas usando o dicionário no atributo
"traps" de um contexto:

   >>> setcontext(ExtendedContext)
   >>> Decimal(1) / Decimal(0)
   Decimal('Infinity')
   >>> getcontext().traps[DivisionByZero] = 1
   >>> Decimal(1) / Decimal(0)
   Traceback (most recent call last):
     File "<pyshell#112>", line 1, in -toplevel-
       Decimal(1) / Decimal(0)
   DivisionByZero: x / 0

A maioria dos programas ajusta o contexto atual apenas uma vez, no
início. E, em muitas aplicações, os dados são convertidos para
"Decimal" em uma única conversão dentro de um loop. Com o conjunto de
contextos e decimais criados, a maior parte do programa manipula os
dados de maneira diferente da que se faz com outros tipos numéricos do
Python.


Objetos de Decimal
==================

class decimal.Decimal(value='0', context=None)

   Constrói um novo objeto de "Decimal" a partir de *value*.

   *value* pode ser um inteiro, uma string, uma tupla, um "float" ou
   outro objeto "Decimal". Se nenhum *value* for fornecido, retornará
   "Decimal('0')". Se *value* for uma string, ele deverá estar em
   conformidade com a sintaxe da string numérica decimal após
   caracteres de espaço em branco à esquerda e à direita, bem como
   sublinhados serem removidos:

      sign           ::=  '+' | '-'
      digit          ::=  '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
      indicator      ::=  'e' | 'E'
      digits         ::=  digit [digit]...
      decimal-part   ::=  digits '.' [digits] | ['.'] digits
      exponent-part  ::=  indicator [sign] digits
      infinity       ::=  'Infinity' | 'Inf'
      nan            ::=  'NaN' [digits] | 'sNaN' [digits]
      numeric-value  ::=  decimal-part [exponent-part] | infinity
      numeric-string ::=  [sign] numeric-value | [sign] nan

   Outros dígitos decimais Unicode também são permitidos onde "digit"
   aparece acima. Isso inclui dígitos decimais de vários outros
   alfabetos (por exemplo, dígitos em árabes-índicos e devanágaris),
   além dos dígitos de largura total "'\uff10'" a "'\uff19'". A
   capitalização não é significativa, então, por exemplo, "inf",
   "Inf", "INFINITY" e "iNfINity" são todas grafias aceitáveis para
   infinito positivo.

   Se *value* for uma "tupla", ela deverá ter três componentes: um
   sinal ("0" para positivo ou "1" para negativo), uma "tupla" de
   dígitos e um expoente inteiro. Por exemplo, "Decimal((0, (1, 4, 1,
   4), -3))" retorna "Decimal('1.414')".

   Se *value* é um "float", o valor do ponto flutuante binário é
   convertido sem perdas para o seu equivalente decimal exato. Essa
   conversão geralmente requer 53 ou mais dígitos de precisão. Por
   exemplo, "Decimal(float('1.1'))" converte para
   "Decimal('1.100000000000000088817841970012523233890533447265625')".

   A precisão *context* não afeta o número de dígitos armazenados.
   Isso é determinado exclusivamente pelo número de dígitos de
   *value*. Por exemplo, "Decimal('3.00000')" registra todos os cinco
   zeros, mesmo que a precisão do contexto seja de apenas três.

   O objetivo do argumento *context* é determinar o que fazer se
   *value* for uma string malformada. Se o contexto capturar
   "InvalidOperation", uma exceção será levantada; caso contrário, o
   construtor retornará um novo decimal com o valor "NaN".

   Uma vez construídos, objetos "Decimal" são imutáveis.

   Alterado na versão 3.2: O argumento para o construtor agora pode
   ser uma instância de "float".

   Alterado na versão 3.3: Os argumentos de "float" levantam uma
   exceção se a armadilha "FloatOperation" estiver definida. Por
   padrão, a armadilha está desativada.

   Alterado na versão 3.6: Sublinhados são permitidos para
   agrupamento, como nos literais de ponto flutuante e inteiros no
   código.

   Objetos decimais de ponto flutuante compartilham muitas
   propriedades com outros tipos numéricos embutidos, como "float" e
   "int". Todas as operações matemáticas usuais e métodos especiais se
   aplicam. Da mesma forma, objetos decimais podem ser copiados,
   separados, impressos, usados como chaves de dicionário, usados como
   elementos de conjunto, comparados, classificados e convertidos para
   outro tipo (como "float" ou "int").

   Existem algumas pequenas diferenças entre a aritmética de objetos
   decimais e a de números inteiros e flutuantes. Quando o operador de
   resto "%" é aplicado a objetos decimais, o sinal do resultado é o
   sinal do *dividendo* em vez do sinal do divisor:

      >>> (-7) % 4
      1
      >>> Decimal(-7) % Decimal(4)
      Decimal('-3')

   O operador de divisão inteira "//" se comporta de maneira análoga,
   retornando a parte inteira do quociente verdadeiro (truncando em
   direção a zero) em vez de seu resto, de modo a preservar a
   identidade usual "x == (x // y) * y + x % y":

      >>> -7 // 4
      -2
      >>> Decimal(-7) // Decimal(4)
      Decimal('-1')

   Os operadores "%" e "//" implementam as operações de "remainder" e
   "divide-integer" (respectivamente), conforme descrito na
   especificação.

   Objetos decimais geralmente não podem ser combinados com pontos
   flutuantes ou instâncias de "fractions.Fraction" em operações
   aritméticas: uma tentativa de adicionar um "Decimal" a um "float",
   por exemplo, vai levantar um "TypeError". No entanto, é possível
   usar os operadores de comparação do Python para comparar uma
   instância de "Decimal" "x" com outro número "y". Isso evita
   resultados confusos ao comparar números de tipos diferentes.

   Alterado na versão 3.2: As comparações de tipos mistos entre
   instâncias de "Decimal" e outros tipos numéricos agora estão
   totalmente implementadas.

   Além das propriedades numéricas padrões, os objetos de ponto
   flutuante decimal também possuem vários métodos especializados:

   adjusted()

      Retorna o expoente ajustado depois de deslocar os dígitos mais à
      direita do coeficiente até restar apenas o dígito principal:
      "Decimal('321e+5').adjusted()" retorna sete. Usado para
      determinar a posição do dígito mais significativo em relação ao
      ponto decimal.

   as_integer_ratio()

      Retorna um par "(n, d)" de números inteiros que representam a
      instância dada "Decimal" como uma fração, nos termos mais baixos
      e com um denominador positivo:

         >>> Decimal('-3.14').as_integer_ratio()
         (-157, 50)

      A conversão é exata. Levanta OverflowError em infinitos e
      ValueError em NaNs.

   Adicionado na versão 3.6.

   as_tuple()

      Retorna uma representação de *tupla nomeada* do número:
      "DecimalTuple(sign, digits, exponent)".

   canonical()

      Retorna a codificação canônica do argumento. Atualmente, a
      codificação de uma instância de "Decimal" é sempre canônica,
      portanto, esta operação retorna seu argumento inalterado.

   compare(other, context=None)

      Compara os valores de duas instâncias decimais. "compare()"
      retorna uma instância decimal, e se qualquer operando for um
      NaN, o resultado será um NaN:

         a or b is a NaN  ==> Decimal('NaN')
         a < b            ==> Decimal('-1')
         a == b           ==> Decimal('0')
         a > b            ==> Decimal('1')

   compare_signal(other, context=None)

      Esta operação é idêntica ao método "compare()", exceto que todos
      os NaNs sinalizam. Ou seja, se nenhum operando for um NaN
      sinalizador, qualquer operando NaN silencioso será tratado como
      se fosse um NaN sinalizador.

   compare_total(other, context=None)

      Compara dois operandos usando sua representação abstrata em vez
      de seu valor numérico. Semelhante ao método "compare()", mas o
      resultado fornece uma ordem total nas instâncias de "Decimal".
      Duas instâncias de "Decimal" com o mesmo valor numérico, mas
      diferentes representações, se comparam desiguais nesta ordem:

      >>> Decimal('12.0').compare_total(Decimal('12'))
      Decimal('-1')

      Os NaNs silenciosos e sinalizadores também estão incluídos no
      pedido total. O resultado dessa função é "Decimal('0')" se os
      dois operandos tiverem a mesma representação, "Decimal('-1')" se
      o primeiro operando for menor na ordem total que o segundo e
      "Decimal('1')" se o primeiro operando for maior na ordem total
      que o segundo operando. Veja a especificação para detalhes da
      ordem total.

      Esta operação não é afetada pelo contexto e é silenciosa: nenhum
      sinalizador é alterado e nenhum arredondamento é executado. Como
      uma exceção, a versão C pode levantar InvalidOperation se o
      segundo operando não puder ser convertido exatamente.

   compare_total_mag(other, context=None)

      Compara dois operandos usando sua representação abstrata em vez
      de seu valor, como em "compare_total()", mas ignorando o sinal
      de cada operando. "x.compare_total_mag(y)" é equivalente a
      "x.copy_abs().compare_total(y.copy_abs())".

      Esta operação não é afetada pelo contexto e é silenciosa: nenhum
      sinalizador é alterado e nenhum arredondamento é executado. Como
      uma exceção, a versão C pode levantar InvalidOperation se o
      segundo operando não puder ser convertido exatamente.

   conjugate()

      Apenas retorna a si próprio, sendo esse método apenas para
      atender à Especificação de Decimal.

   copy_abs()

      Retorna o valor absoluto do argumento. Esta operação não é
      afetada pelo contexto e é silenciosa: nenhum sinalizador é
      alterado e nenhum arredondamento é executado.

   copy_negate()

      Retorna a negação do argumento. Esta operação não é afetada pelo
      contexto e é silenciosa: nenhum sinalizador é alterado e nenhum
      arredondamento é executado.

   copy_sign(other, context=None)

      Retorna uma cópia do primeiro operando com o sinal definido para
      ser o mesmo que o sinal do segundo operando. Por exemplo:

      >>> Decimal('2.3').copy_sign(Decimal('-1.5'))
      Decimal('-2.3')

      Esta operação não é afetada pelo contexto e é silenciosa: nenhum
      sinalizador é alterado e nenhum arredondamento é executado. Como
      uma exceção, a versão C pode levantar InvalidOperation se o
      segundo operando não puder ser convertido exatamente.

   exp(context=None)

      Retorna o valor da função exponencial (natural) "e**x" no número
      especificado. O resultado é arredondado corretamente usando o
      modo de arredondamento "ROUND_HALF_EVEN".

      >>> Decimal(1).exp()
      Decimal('2.718281828459045235360287471')
      >>> Decimal(321).exp()
      Decimal('2.561702493119680037517373933E+139')

   classmethod from_float(f, /)

      Construtor alternativo que aceita apenas instâncias de "float"
      ou "int".

      Observe que "Decimal.from_float(0.1)" não é o mesmo que
      "Decimal('0.1')". Como 0.1 não é exatamente representável no
      ponto flutuante binário, o valor é armazenado como o valor
      representável mais próximo que é "0x1.999999999999ap-4".; Esse
      valor equivalente em decimal é
      "0.1000000000000000055511151231257827021181583404541015625".

      Nota:

        A partir do Python 3.2 em diante, uma instância de "Decimal"
        também pode ser construída diretamente a partir de um "float".

         >>> Decimal.from_float(0.1)
         Decimal('0.1000000000000000055511151231257827021181583404541015625')
         >>> Decimal.from_float(float('nan'))
         Decimal('NaN')
         >>> Decimal.from_float(float('inf'))
         Decimal('Infinity')
         >>> Decimal.from_float(float('-inf'))
         Decimal('-Infinity')

      Adicionado na versão 3.1.

   classmethod from_number(number, /)

      Construtor alternativo que aceita apenas instâncias de "float",
      "int" ou "Decimal", mas não de strings ou tuplas.

         >>> Decimal.from_number(314)
         Decimal('314')
         >>> Decimal.from_number(0.1)
         Decimal('0.1000000000000000055511151231257827021181583404541015625')
         >>> Decimal.from_number(Decimal('3.14'))
         Decimal('3.14')

      Adicionado na versão 3.14.

   fma(other, third, context=None)

      Multiplicação e adição fundidas. Retorna self*other+third sem
      arredondamento do produto intermediário self*other.

      >>> Decimal(2).fma(3, 5)
      Decimal('11')

   is_canonical()

      Retorna "True" se o argumento for canônico e "False" caso
      contrário. Atualmente, uma instância de "Decimal" é sempre
      canônica, portanto, esta operação sempre retorna "True".

   is_finite()

      Retorna "True" se o argumento for um número finito e "False" se
      o argumento for um infinito ou um NaN.

   is_infinite()

      Retorna "True" se o argumento for infinito positivo ou negativo
      e "False" caso contrário.

   is_nan()

      Retorna "True" se o argumento for NaN (silencioso ou sinalizado)
      e "False" caso contrário.

   is_normal(context=None)

      Retorna "True" se o argumento for um número finito *normal*.
      Retorna "False" se o argumento for zero, subnormal, infinito ou
      NaN.

   is_qnan()

      Retorna "True" se o argumento for um NaN silencioso e "False"
      caso contrário.

   is_signed()

      Retorna "True" se o argumento tiver um sinal negativo e "False"
      caso contrário. Observe que zeros e NaNs podem carregar sinais.

   is_snan()

      Retorna "True" se o argumento for um sinal NaN e "False" caso
      contrário.

   is_subnormal(context=None)

      Retorna "True" se o argumento for subnormal e "False" caso
      contrário.

   is_zero()

      Retorna "True" se o argumento for um zero (positivo ou negativo)
      e "False" caso contrário.

   ln(context=None)

      Retorna o logaritmo (base e) natural do operando. O resultado é
      arredondado corretamente usando o modo de arredondamento
      "ROUND_HALF_EVEN".

   log10(context=None)

      Retorna o logaritmo da base dez do operando. O resultado é
      arredondado corretamente usando o modo de arredondamento
      "ROUND_HALF_EVEN".

   logb(context=None)

      Para um número diferente de zero, retorna o expoente ajustado de
      seu operando como uma instância de "Decimal". Se o operando é
      zero, "Decimal('-Infinity')" é retornado e o sinalizador
      "DivisionByZero" é levantado. Se o operando for um infinito,
      "Decimal('Infinity')" será retornado.

   logical_and(other, context=None)

      "logical_and()" é uma operação lógica que leva dois *operandos
      lógicos* (consulte Operandos lógicos). O resultado é o "and"
      dígito a dígito dos dois operandos.

   logical_invert(context=None)

      "logical_invert()" é uma operação lógica. O resultado é a
      inversão dígito a dígito do operando.

   logical_or(other, context=None)

      "logical_or()" é uma operação lógica que leva dois *operandos
      lógicos* (consulte Operandos lógicos). O resultado é o "or"
      dígito a dígito dos dois operandos.

   logical_xor(other, context=None)

      "logical_xor()" é uma operação lógica que leva dois *operandos
      lógicos* (consulte Operandos lógicos). O resultado é o "ou
      exclusivo" dígito a dígito ou dos dois operandos.

   max(other, context=None)

      Como "max(self, other)", exceto que a regra de arredondamento de
      contexto é aplicada antes de retornar e que os valores "NaN" são
      sinalizados ou ignorados (dependendo do contexto e se estão
      sinalizando ou silenciosos).

   max_mag(other, context=None)

      Semelhante ao método "max()", mas a comparação é feita usando os
      valores absolutos dos operandos.

   min(other, context=None)

      Como "min(self, other)", exceto que a regra de arredondamento de
      contexto é aplicada antes de retornar e que os valores "NaN" são
      sinalizados ou ignorados (dependendo do contexto e se estão
      sinalizando ou silenciosos).

   min_mag(other, context=None)

      Semelhante ao método "min()", mas a comparação é feita usando os
      valores absolutos dos operandos.

   next_minus(context=None)

      Retorna o maior número representável no contexto fornecido (ou
      no contexto atual da thread, se nenhum contexto for fornecido)
      que seja menor que o operando especificado.

   next_plus(context=None)

      Retorna o menor número representável no contexto fornecido (ou
      no contexto atual da thread, se nenhum contexto for fornecido)
      que seja maior que o operando fornecido.

   next_toward(other, context=None)

      Se os dois operandos forem desiguais, retorna o número mais
      próximo ao primeiro operando na direção do segundo operando. Se
      os dois operandos forem numericamente iguais, retorna uma cópia
      do primeiro operando com o sinal configurado para ser o mesmo
      que o sinal do segundo operando.

   normalize(context=None)

      Usado para produzir valores canônicos de uma classe de
      equivalência no contexto atual ou no contexto especificado.

      Esta tem a mesma semântica que a operação unária mais, exceto
      que se o resultado final for finito, ele será reduzido à sua
      forma mais simples, com todos os zeros à direita removidos e seu
      sinal preservado. Ou seja, enquanto o coeficiente for diferente
      de zero e múltiplo de dez, o coeficiente é dividido por dez e o
      expoente é incrementado em 1. Caso contrário (o coeficiente é
      zero), o expoente é definido como 0. Em todos os casos, o sinal
      permanece inalterado. .

      Por exemplo, "Decimal('32.100')" e "Decimal('0.321000e+2')"
      ambos normalizam para o valor equivalente "Decimal('32.1')".

      Observe que o arredondamento é aplicado *antes* de reduzir para
      a forma mais simples.

      Nas versões mais recentes da especificação, esta operação também
      é conhecida como "reduce".

   number_class(context=None)

      Retorna uma string descrevendo a *classe* do operando. O valor
      retornado é uma das dez sequências a seguir.

      * ""-Infinity"", indicando que o operando é infinito negativo.

      * ""-Normal"", indicando que o operando é um número normal
        negativo.

      * ""-Subnormal"", indicando que o operando é negativo e
        subnormal.

      * ""-Zero"", indicando que o operando é um zero negativo.

      * ""+Zero"", indicando que o operando é um zero positivo.

      * ""+Subnormal"", indicando que o operando é positivo e
        subnormal.

      * ""+Normal"", indicando que o operando é um número normal
        positivo.

      * ""+Infinity"", indicando que o operando é infinito positivo.

      * ""NaN"", indicando que o operando é um NaN ("Not a Number")
        silencioso.

      * ""sNaN"", indicando que o operando é um NaN sinalizador.

   quantize(exp, rounding=None, context=None)

      Retorna um valor igual ao primeiro operando após o
      arredondamento e com o expoente do segundo operando.

      >>> Decimal('1.41421356').quantize(Decimal('1.000'))
      Decimal('1.414')

      Diferentemente de outras operações, se o comprimento do
      coeficiente após a operação de quantização for maior que a
      precisão, então "InvalidOperation" é sinalizado. Isso garante
      que, a menos que haja uma condição de erro, o expoente
      quantizado é sempre igual ao do operando do lado direito.

      Também, diferentemente de outras operações, a quantização nunca
      sinaliza Underflow, mesmo que o resultado seja subnormal e
      inexato.

      Se o expoente do segundo operando for maior que o do primeiro, o
      arredondamento poderá ser necessário. Nesse caso, o modo de
      arredondamento é determinado pelo argumento "rounding", se
      fornecido, ou pelo argumento "context" fornecido; se nenhum
      argumento for fornecido, o modo de arredondamento do contexto da
      thread atual será usado.

      Um erro é retornado sempre que o expoente resultante for maior
      que "Emax" ou menor que "Etiny()".

   radix()

      Retorna "Decimal(10)", a raiz (base) na qual a classe "Decimal"
      faz toda a sua aritmética. Incluído para compatibilidade com a
      especificação.

   remainder_near(other, context=None)

      Retorna o resto da divisão de *self* por *other*. Isso é
      diferente de "self % other", pois o sinal do resto é escolhido
      para minimizar seu valor absoluto. Mais precisamente, o valor de
      retorno é "self - n * other", onde "n" é o número inteiro mais
      próximo do valor exato de "self / other", e se dois números
      inteiros estiverem igualmente próximos, o par será é escolhido.

      Se o resultado for zero, seu sinal será o sinal de *self*.

      >>> Decimal(18).remainder_near(Decimal(10))
      Decimal('-2')
      >>> Decimal(25).remainder_near(Decimal(10))
      Decimal('5')
      >>> Decimal(35).remainder_near(Decimal(10))
      Decimal('-5')

   rotate(other, context=None)

      Retorna o resultado da rotação dos dígitos do primeiro operando
      em uma quantidade especificada pelo segundo operando. O segundo
      operando deve ser um número inteiro no intervalo - precisão
      através da precisão. O valor absoluto do segundo operando
      fornece o número de locais a serem rotacionados. Se o segundo
      operando for positivo, a rotação será para a esquerda; caso
      contrário, a rotação será para a direita. O coeficiente do
      primeiro operando é preenchido à esquerda com zeros na precisão
      do comprimento, se necessário. O sinal e o expoente do primeiro
      operando não são alterados.

   same_quantum(other, context=None)

      Testa se "self" e "other" têm o mesmo expoente ou se ambos são
      "NaN".

      Esta operação não é afetada pelo contexto e é silenciosa: nenhum
      sinalizador é alterado e nenhum arredondamento é executado. Como
      uma exceção, a versão C pode levantar InvalidOperation se o
      segundo operando não puder ser convertido exatamente.

   scaleb(other, context=None)

      Retorna o primeiro operando com o expoente ajustado pelo
      segundo. Da mesma forma, retorna o primeiro operando
      multiplicado por "10**other". O segundo operando deve ser um
      número inteiro.

   shift(other, context=None)

      Retorna o resultado da troca dos dígitos do primeiro operando em
      uma quantidade especificada pelo segundo operando. O segundo
      operando deve ser um número inteiro no intervalo - precisão
      através da precisão. O valor absoluto do segundo operando
      fornece o número de locais a serem deslocados. Se o segundo
      operando for positivo, o deslocamento será para a esquerda; caso
      contrário, a mudança é para a direita. Os dígitos deslocados
      para o coeficiente são zeros. O sinal e o expoente do primeiro
      operando não são alterados.

   sqrt(context=None)

      Retorna a raiz quadrada do argumento para a precisão total.

   to_eng_string(context=None)

      Converte em uma string, usando notação de engenharia, se for
      necessário um expoente.

      A notação de engenharia possui um expoente que é múltiplo de 3.
      Isso pode deixar até 3 dígitos à esquerda da casa decimal e pode
      exigir a adição de um ou dois zeros à direita.

      Por exemplo, isso converte "Decimal('123E+1')" para
      "Decimal('1.23E+3')".

   to_integral(rounding=None, context=None)

      Idêntico ao método "to_integral_value()". O nome "to_integral"
      foi mantido para compatibilidade com versões mais antigas.

   to_integral_exact(rounding=None, context=None)

      Arredonda para o número inteiro mais próximo, sinalizando
      "Inexact" ou "Rounded", conforme apropriado, se o arredondamento
      ocorrer. O modo de arredondamento é determinado pelo parâmetro
      "rounding", se fornecido, ou pelo "context" especificado. Se
      nenhum parâmetro for fornecido, o modo de arredondamento do
      contexto atual será usado.

   to_integral_value(rounding=None, context=None)

      Arredonda para o número inteiro mais próximo sem sinalizar
      "Inexact" ou "Rounded". Se fornecido, aplica *rounding*; caso
      contrário, usa o método de arredondamento no *context*
      especificado ou no contexto atual.

   Os números decimais podem ser arredondados usando a função
   "round()":

   round(number)

   round(number, ndigits)

      Se *ndigits* não for fornecido ou "None", retorna o "int" de
      *number* mais próximo, arredondando até chegar em par, e
      ignorando o modo de arredondamento do contexto "Decimal".
      Levanta "OverflowError" se *number* for um infinito ou
      "ValueError" se for um NaN (silencioso ou de sinalização).

      Se *ndigits* for um "int", o modo de arredondamento do contexto
      é respeitado e um "Decimal" representando *número* arredondado
      para o múltiplo mais próximo de "Decimal('1E-ndigits')" é
      retornado; neste caso, "round(number, ndigits)" é equivalente a
      "self.quantize(Decimal('1E-ndigits'))". Retorna "Decimal('NaN')"
      se *number* for um NaN silencioso. Levanta "InvalidOperation" se
      *number* for um infinito, uma sinalização NaN, ou se o
      comprimento do coeficiente após a operação de quantização for
      maior que a precisão do contexto atual. Em outras palavras, para
      os situações comuns:

      * se *ndigits* for positivo, retorna *number* arredondado para
        *ndigits* casas decimais;

      * se *ndigits* for zero, retorna *number* arredondado para o
        número inteiro mais próximo;

      * se *ndigits* for negativo, retorna *number* arredondado para o
        múltiplo mais próximo de "10**abs(ndigits)".

      Por exemplo:

         >>> from decimal import Decimal, getcontext, ROUND_DOWN
         >>> getcontext().rounding = ROUND_DOWN
         >>> round(Decimal('3.75'))     # arredondamento de contexto ignorado
         4
         >>> round(Decimal('3.5'))      # arredondamento para par mais próximo
         4
         >>> round(Decimal('3.75'), 0)  # usa o arredondamento de contexto
         Decimal('3')
         >>> round(Decimal('3.75'), 1)
         Decimal('3.7')
         >>> round(Decimal('3.75'), -1)
         Decimal('0E+1')


Operandos lógicos
-----------------

Os métodos "logical_and()", "logical_invert()", "logical_or()" e
"logical_xor()" esperam que seus argumentos sejam *operandos lógicos*.
Um *operando lógico* é uma instância de "Decimal" cujo expoente e
sinal são zero e cujos dígitos são todos "0" ou "1".


Objetos de contexto
===================

Contextos são ambientes para operações aritméticas. Eles governam a
precisão, estabelecem regras para arredondamento, determinam quais
sinais são tratados como exceções e limitam o intervalo dos expoentes.

Cada thread possui seu próprio contexto atual que é acessado ou
alterado usando as funções "getcontext()" e "setcontext()":

decimal.getcontext()

   Retorna o contexto atual para a thread ativa.

decimal.setcontext(c, /)

   Define o contexto atual para a thread ativa como *C*.

Você também pode usar a instrução "with" e a função "localcontext()"
para alterar temporariamente o contexto ativo.

decimal.localcontext(ctx=None, **kwargs)

   Retorna um gerenciador de contexto que vai definir o contexto atual
   da thread ativa para uma cópia de *ctx* na entrada da instrução
   "with" e restaurar o contexto anterior ao sair da instrução "with".
   Se nenhum contexto for especificado, uma cópia do contexto atual
   será usada. O argumento *kwargs* é usado para definir os atributos
   do novo contexto.

   Por exemplo, o código a seguir define a precisão decimal atual para
   42 casas, executa um cálculo e restaura automaticamente o contexto
   anterior:

      from decimal import localcontext

      with localcontext() as ctx:
          ctx.prec = 42   # Efetua um cálculo de alta precisão
          s = calculate_something()
      s = +s  # Arredonda o resultado final de volta para a precisão padrão

   Usando argumentos nomeados, o código seria o seguinte:

      from decimal import localcontext

      with localcontext(prec=42) as ctx:
          s = calculate_something()
      s = +s

   Levanta "TypeError" se *kwargs* fornecer um atributo que "Context"
   não oferecer suporte. Levanta "TypeError" ou "ValueError" se
   *kwargs* fornecer um valor inválido para um atributo.

   Alterado na versão 3.11: "localcontext()" agora tem suporte à
   configuração de atributos de contexto através do uso de argumentos
   nomeados.

decimal.IEEEContext(bits)

   Retorna um objeto de contexto inicializado com os valores
   apropriados para um dos formatos de intercâmbio IEEE. O argumento
   deve ser um múltiplo de 32 e menor que "IEEE_CONTEXT_MAX_BITS".

   Adicionado na versão 3.14.

Novos contextos também podem ser criados usando o construtor "Context"
descrito abaixo. Além disso, o módulo fornece três contextos
pré-criados:

decimal.BasicContext

   Este é um contexto padrão definido pela Especificação Aritmética
   Decimal Geral. A precisão está definida como nove. O arredondamento
   está definido como "ROUND_HALF_UP". Todos os sinalizadores estão
   limpos. Todos as armadilhas estão ativadas (tratadas como
   exceções), exceto por "Inexact", "Rounded" e "Subnormal".

   Como muitas das armadilhas estão ativadas, esse contexto é útil
   para depuração.

decimal.ExtendedContext

   Este é um contexto padrão definido pela Especificação Aritmética
   Decimal Geral. A precisão está definida como nove. O arredondamento
   está definido como "ROUND_HALF_EVEN". Todos os sinalizadores estão
   limpos. Nenhuma armadilha está ativada (de forma que exceções não
   são levantadas durante os cálculos).

   Como as armadilhas estão desativadas, esse contexto é útil para
   aplicativos que preferem ter o valor de resultado de "NaN" ou
   "Infinity" em vez de levantar exceções. Isso permite que uma
   aplicação conclua uma execução na presença de condições que
   interromperiam o programa.

decimal.DefaultContext

   Este contexto é usado pelo construtor "Context" como um protótipo
   para novos contextos. Alterar um campo (tal como precisão) tem o
   efeito de alterar o padrão para novos contextos criados pelo
   construtor "Context".

   Esse contexto é mais útil em ambientes multithread. A alteração de
   um dos campos antes do início das threads tem o efeito de definir
   os padrões para todo o sistema. Não é recomendável alterar os
   campos após o início das threads, pois exigiria sincronização de
   threads para evitar condições de corrida.

   Em ambientes de thread única, é preferível não usar esse contexto.
   Em vez disso, basta criar contextos explicitamente, conforme
   descrito abaixo.

   Os valores padrão são "Context.prec"="28",
   "Context.rounding"="ROUND_HALF_EVEN" e armadilhas ativadas para
   "Overflow", "InvalidOperation" e "DivisionByZero".

Além dos três contextos fornecidos, novos contextos podem ser criados
com o construtor "Context".

class decimal.Context(prec=None, rounding=None, Emin=None, Emax=None, capitals=None, clamp=None, flags=None, traps=None)

   Cria um novo contexto. Se um campo não for especificado ou for
   "None", os valores padrão serão copiados de "DefaultContext". Se o
   campo *flags* não for especificado ou for "None", todos os
   sinalizadores serão limpados.

   prec

      Um inteiro no intervalo ["1", "MAX_PREC"] que define a precisão
      para operações aritméticas no contexto.

   rounding

      Uma das constantes listadas na seção Modos de arredondamento.

   traps
   flags

      Listas de todos os sinais a serem configurados. Geralmente,
      novos contextos devem apenas definir armadilhas e deixar os
      sinalizadores limpos.

   Emin
   Emax

      Números inteiros que especificam os limites externos permitidos
      para expoentes. *Emin* deve estar no intervalo ["MIN_EMIN",
      "0"], *Emax* no intervalo ["0", "MAX_EMAX"].

   capitals

      Assume "0" ou "1" (o padrão). Se definido como "1", os expoentes
      serão impressos com um "E" maiúsculo; caso contrário, um "e"
      minúsculo é usado: "Decimal('6.02e+23')".

   clamp

      Assume "0" (o padrão) ou "1". Se definido como "1", o expoente
      "e" de uma instância de "Decimal" representável nesse contexto é
      estritamente limitado ao intervalo "Emin - prec + 1 <= e <= Emax
      - prec + 1". Se *clamp* for "0", uma condição mais fraca será
      mantida: o expoente ajustado da instância de "Decimal" é no
      máximo "Emax". Quando *clamp* é "1", um grande número normal
      terá, sempre que possível, seu expoente reduzido e um número
      correspondente de zeros adicionado ao seu coeficiente, para
      ajustar as restrições do expoente; isso preserva o valor do
      número, mas perde informações sobre zeros à direita
      significativos. Por exemplo:

         >>> Context(prec=6, Emax=999, clamp=1).create_decimal('1.23e999')
         Decimal('1.23000E+999')

      Um valor de *clamp* de "1" permite compatibilidade com os
      formatos de intercâmbio decimal de largura fixa especificados na
      IEEE 754.

   A classe "Context" define vários métodos de uso geral, bem como um
   grande número de métodos para fazer aritmética diretamente em um
   determinado contexto. Além disso, para cada um dos métodos de
   "Decimal" descritos acima (com exceção dos métodos "adjusted()" e
   "as_tuple()") existe um método correspondente em "Context". Por
   exemplo, para uma instância "C" de "Context" e uma instância "x" de
   "Decimal", "C.exp(x)" é equivalente a "x.exp(context=C)". Cada
   método de "Context" aceita um número inteiro do Python (uma
   instância de "int") em qualquer lugar em que uma instância de
   Decimal seja aceita.

   clear_flags()

      Redefine todos os sinalizadores para "0".

   clear_traps()

      Redefine todas as armadilhas para "0".

      Adicionado na versão 3.3.

   copy()

      Retorna uma duplicata do contexto.

   copy_decimal(num, /)

      Retorna uma cópia da instância de Decimal *num*.

   create_decimal(num='0', /)

      Cria uma nova instância decimal a partir de *num*, mas usando
      *self* como contexto. Diferentemente do construtor de "Decimal",
      a precisão do contexto, o método de arredondamento, os
      sinalizadores e as armadilhas são aplicadas à conversão.

      Isso é útil porque as constantes geralmente são fornecidas com
      uma precisão maior do que a necessária pela aplicação. Outro
      benefício é que o arredondamento elimina imediatamente os
      efeitos indesejados dos dígitos além da precisão atual. No
      exemplo a seguir, o uso de entradas não arredondadas significa
      que adicionar zero a uma soma pode alterar o resultado:

         >>> getcontext().prec = 3
         >>> Decimal('3.4445') + Decimal('1.0023')
         Decimal('4.45')
         >>> Decimal('3.4445') + Decimal(0) + Decimal('1.0023')
         Decimal('4.44')

      Este método implementa a operação "to-number" da especificação
      IBM. Se o argumento for uma string, nenhum espaço em branco à
      esquerda ou à direita ou sublinhado serão permitidos.

   create_decimal_from_float(f, /)

      Cria uma nova instância de Decimal a partir de um ponto
      flutuante *f*, mas arredondando usando *self* como contexto.
      Diferentemente do método da classe "Decimal.from_float()", a
      precisão do contexto, o método de arredondamento, os
      sinalizadores e as armadilhas são aplicados à conversão.

         >>> context = Context(prec=5, rounding=ROUND_DOWN)
         >>> context.create_decimal_from_float(math.pi)
         Decimal('3.1415')
         >>> context = Context(prec=5, traps=[Inexact])
         >>> context.create_decimal_from_float(math.pi)
         Traceback (most recent call last):
             ...
         decimal.Inexact: None

      Adicionado na versão 3.1.

   Etiny()

      Retorna um valor igual a "Emin - prec + 1", que é o valor mínimo
      do expoente para resultados subnormais. Quando ocorre o estouro
      negativo, o expoente é definido como "Etiny".

   Etop()

      Retorna um valor igual a "Emax - prec + 1".

   A abordagem usual para trabalhar com decimais é criar instâncias de
   "Decimal" e depois aplicar operações aritméticas que ocorrem no
   contexto atual da thread ativa. Uma abordagem alternativa é usar
   métodos de contexto para calcular dentro de um contexto específico.
   Os métodos são semelhantes aos da classe "Decimal" e são contados
   apenas brevemente aqui.

   abs(x, /)

      Retorna o valor absoluto de *x*.

   add(x, y, /)

      Retorna a soma de *x* e *y*.

   canonical(x, /)

      Retorna o mesmo objeto de Decimal *x*.

   compare(x, y, /)

      Compara *x* e *y* numericamente.

   compare_signal(x, y, /)

      Compara os valores dos dois operandos numericamente.

   compare_total(x, y, /)

      Compara dois operandos usando sua representação abstrata.

   compare_total_mag(x, y, /)

      Compara dois operandos usando sua representação abstrata,
      ignorando o sinal.

   copy_abs(x, /)

      Retorna uma cópia de *x* com o sinal definido para 0.

   copy_negate(x, /)

      Retorna uma cópia de *x* com o sinal invertido.

   copy_sign(x, y, /)

      Copia o sinal de *y* para *x*.

   divide(x, y, /)

      Retorna *x* dividido por *y*.

   divide_int(x, y, /)

      Retorna *x* dividido por *y*, truncado para um inteiro.

   divmod(x, y, /)

      Divide dois números e retorna a parte inteira do resultado.

   exp(x, /)

      Retorna "e ** x".

   fma(x, y, z, /)

      Retorna *x* multiplicado por *y*, mais *z*.

   is_canonical(x, /)

      Retorna "True" se *x* for canonical; caso contrário, retorna
      "False".

   is_finite(x, /)

      Retorna "True" se *x* for finito; caso contrário, retorna
      "False".

   is_infinite(x, /)

      Retorna "True" se *x* for infinito; caso contrário, retorna
      "False".

   is_nan(x, /)

      Retorna "True" se *x* for qNaN ou sNaN; caso contrário, retorna
      "False".

   is_normal(x, /)

      Retorna "True" se *x* for um número normal; caso contrário,
      retorna "False".

   is_qnan(x, /)

      Retorna "True" se *x* for um NaN silencioso; caso contrário,
      retorna "False".

   is_signed(x, /)

      Retorna "True" se *x* for negativo; caso contrário, retorna
      "False".

   is_snan(x, /)

      Retorna "True" se *x* for um NaN sinalizador; caso contrário,
      retorna "False".

   is_subnormal(x, /)

      Retorna "True" se *x* for subnormal; caso contrário, retorna
      "False".

   is_zero(x, /)

      Retorna "True" se *x* for zero; caso contrário, retorna "False".

   ln(x, /)

      Retorna o logaritmo natural (base e) de *x*.

   log10(x, /)

      Retorna o logaritmo de base 10 de *x*.

   logb(x, /)

      Retorna o expoente da magnitude do MSD do operando.

   logical_and(x, y, /)

      Aplica a operação lógica *e* entre cada dígito do operando.

   logical_invert(x, /)

      Inverte todos os dígitos em *x*.

   logical_or(x, y, /)

      Aplica a operação lógica *ou* entre cada dígito do operando.

   logical_xor(x, y, /)

      Aplica a operação lógica *ou exclusivo* entre cada dígito do
      operando.

   max(x, y, /)

      Compara dois valores numericamente e retorna o máximo.

   max_mag(x, y, /)

      Compara dois valores numericamente com seu sinal ignorado.

   min(x, y, /)

      Compara dois valores numericamente e retorna o mínimo.

   min_mag(x, y, /)

      Compara dois valores numericamente com seu sinal ignorado.

   minus(x, /)

      Minus corresponde ao operador de subtração de prefixo unário no
      Python.

   multiply(x, y, /)

      Retorna o produto de *x* e *y*.

   next_minus(x, /)

      Retorna o maior número representável menor que *x*.

   next_plus(x, /)

      Retorna o menor número representável maior que *x*.

   next_toward(x, y, /)

      Retorna o número mais próximo a *x*, em direção a *y*.

   normalize(x, /)

      Reduz *x* para sua forma mais simples.

   number_class(x, /)

      Retorna uma indicação da classe de *x*.

   plus(x, /)

      Plus corresponde ao operador de soma de prefixo unário no
      Python. Esta operação aplica a precisão e o arredondamento do
      contexto, portanto *não* é uma operação de identidade.

   power(x, y, modulo=None)

      Retorna "x" à potência de "y", com a redução de módulo "modulo"
      se fornecido.

      Com dois argumentos, calcula "x**y". Se "x" for negativo, "y"
      deve ser inteiro. O resultado será inexato, a menos que "y" seja
      inteiro e o resultado seja finito e possa ser expresso
      exatamente em "precisão" dígitos. O modo de arredondamento do
      contexto é usado. Os resultados são sempre arredondados
      corretamente na versão Python.

      "Decimal(0) ** Decimal(0)" resulta em "InvalidOperation", e se
      "InvalidOperation" não for capturado, resulta em
      "Decimal('NaN')".

      Alterado na versão 3.3: O módulo C calcula "power()" em termos
      das funções corretamente arredondadas "exp()" e "ln()". O
      resultado é bem definido, mas apenas "quase sempre corretamente
      arredondado".

      Com três argumentos, calcula "(x**y) % modulo". Para o
      formulário de três argumentos, as seguintes restrições nos
      argumentos são válidas:

      * todos os três argumentos devem ser inteiros

      * "y" não pode ser negativo

      * pelo menos um de "x" ou "y" não pode ser negativo

      * "modulo" não pode ser zero e deve ter pelo menos "precisão"
        dígitos

      O valor resultante de "Context.power(x, y, modulo)" é igual ao
      valor que seria obtido ao computar "(x**y) % modulo" com
      precisão ilimitada, mas é calculado com mais eficiência . O
      expoente do resultado é zero, independentemente dos expoentes de
      "x", "y" e "modulo". O resultado é sempre exato.

   quantize(x, y, /)

      Retorna um valor igual a *x* (arredondado), com o expoente de
      *y*.

   radix()

      Só retorna 10, já que isso é Decimal, :)

   remainder(x, y, /)

      Retorna o resto da divisão inteira.

      O sinal do resultado, se diferente de zero, é o mesmo que o do
      dividendo original.

   remainder_near(x, y, /)

      Retorna "x - y * n", onde *n* é o número inteiro mais próximo do
      valor exato de "x / y" (se o resultado for 0, seu sinal será o
      sinal de *x*).

   rotate(x, y, /)

      Retorna uma cópia re de *x*, *y* vezes.

   same_quantum(x, y, /)

      Retorna "True" se os dois operandos tiverem o mesmo expoente.

   scaleb(x, y, /)

      Retorna o primeiro operando após adicionar o segundo valor seu
      exp.

   shift(x, y, /)

      Retorna uma cópia deslocada de *x*, *y* vezes.

   sqrt(x, /)

      Raiz quadrada de um número não negativo para precisão do
      contexto.

   subtract(x, y, /)

      Retorna a diferença entre *x* e *y*.

   to_eng_string(x, /)

      Converte em uma string, usando notação de engenharia, se for
      necessário um expoente.

      A notação de engenharia possui um expoente que é múltiplo de 3.
      Isso pode deixar até 3 dígitos à esquerda da casa decimal e pode
      exigir a adição de um ou dois zeros à direita.

   to_integral_exact(x, /)

      Arredonda para um número inteiro.

   to_sci_string(x, /)

      Converte um número em uma string usando notação científica.


Constantes
==========

decimal.SPEC_VERSION

   A versão mais recente da Especificação de Aritmética Decimal Geral
   (General Decimal Arithmetic Specification) com a qual esta
   implementação está em conformidade. Consulte
   https://speleotrove.com/decimal/decarith.html para acessar a
   especificação.

   Adicionado na versão 3.15.

As seguintes constantes são relevantes apenas para o módulo C. Eles
também estão incluídos na versão pura do Python para compatibilidade.

+-----------------------------------+-----------------------+---------------------------------+
|                                   | 32 bits               | 64 bits                         |
|===================================|=======================|=================================|
| decimal.MAX_PREC                  | "425000000"           | "999999999999999999"            |
+-----------------------------------+-----------------------+---------------------------------+
| decimal.MAX_EMAX                  | "425000000"           | "999999999999999999"            |
+-----------------------------------+-----------------------+---------------------------------+
| decimal.MIN_EMIN                  | "-425000000"          | "-999999999999999999"           |
+-----------------------------------+-----------------------+---------------------------------+
| decimal.MIN_ETINY                 | "-849999999"          | "-1999999999999999997"          |
+-----------------------------------+-----------------------+---------------------------------+
| decimal.IEEE_CONTEXT_MAX_BITS     | "256"                 | "512"                           |
+-----------------------------------+-----------------------+---------------------------------+

decimal.HAVE_THREADS

   O valor é "True". Descontinuado porque o Python agora sempre tem
   threads.

   Descontinuado desde a versão 3.9.

decimal.HAVE_CONTEXTVAR

   O valor padrão é "True". Se o Python for "configurado usando a
   opção --without-decimal-contextvar", a versão C usará um contexto
   local de thread em vez de local de corrotina e o valor será
   "False". Isso é um pouco mais rápido em alguns cenários de contexto
   aninhados.

   Adicionado na versão 3.8.3.


Modos de arredondamento
=======================

decimal.ROUND_CEILING

   Arredonda para "Infinity".

decimal.ROUND_DOWN

   Arredonda para zero.

decimal.ROUND_FLOOR

   Arredonda para "-Infinity".

decimal.ROUND_HALF_DOWN

   Arrendonda para o mais próximo com empates tendendo a zero.

decimal.ROUND_HALF_EVEN

   Arredonda para o mais próximo com empates indo para o mais próximo
   inteiro par.

decimal.ROUND_HALF_UP

   Arrendonda para o mais próximo com empates se afastando de zero.

decimal.ROUND_UP

   Arredonda se afastando de zero.

decimal.ROUND_05UP

   Arredonda se afastando de zero se o último dígito após o
   arredondamento para zero fosse 0 ou 5; caso contrário, arredonda
   para zero.


Sinais
======

Sinais representam condições que surgem durante o cálculo. Cada um
corresponde a um sinalizador de contexto e um ativador de armadilha de
contexto.

O sinalizador de contexto é definido sempre que a condição é
encontrada. Após o cálculo, os sinalizadores podem ser verificados
para fins informativos (por exemplo, para determinar se um cálculo era
exato). Depois de verificar os sinalizadores, certifique-se de limpar
todos os sinalizadores antes de iniciar o próximo cálculo.

Se o ativador de armadilha de contexto estiver definido para o sinal,
a condição fará com que uma exceção Python seja levantada. Por
exemplo, se a armadilha "DivisionByZero" for configurada, uma exceção
"DivisionByZero" será levantada ao encontrar a condição.

class decimal.Clamped

   Altera um expoente para ajustar as restrições de representação.

   Normalmente, *clamping* ocorre quando um expoente fica fora dos
   limites do contexto "Emin" e "Emax". Se possível, o expoente é
   reduzido para caber adicionando zeros ao coeficiente.

class decimal.DecimalException

   Classe base para outros sinais e uma subclasse de
   "ArithmeticError".

class decimal.DivisionByZero

   Sinaliza a divisão de um número não infinito por zero.

   Pode ocorrer com divisão, divisão de módulo ou ao elevar um número
   a uma potência negativa. Se este sinal não for capturado, retornará
   "Infinity" ou "-Infinity" com o sinal determinado pelas entradas do
   cálculo.

class decimal.Inexact

   Indica que o arredondamento ocorreu e o resultado não é exato.

   Sinaliza quando dígitos diferentes de zero foram descartados
   durante o arredondamento. O resultado arredondado é retornado. O
   sinalizador ou armadilha de sinal é usado para detectar quando os
   resultados são inexatos.

class decimal.InvalidOperation

   Uma operação inválida foi realizada.

   Indica que uma operação foi solicitada que não faz sentido. Se não
   for capturado, retorna "NaN". As possíveis causas incluem:

      Infinity - Infinity
      0 * Infinity
      Infinity / Infinity
      x % 0
      Infinity % x
      sqrt(-x) and x > 0
      0 ** 0
      x ** (non-integer)
      x ** Infinity

class decimal.Overflow

   Estouro numérico.

   Indica que o expoente é maior que "Context.Emax" após o
   arredondamento ocorrer. Se não for capturado, o resultado depende
   do modo de arredondamento, puxando para dentro para o maior número
   finito representável ou arredondando para fora para "Infinity". Nos
   dois casos, "Inexact" e "Rounded" também são sinalizados.

class decimal.Rounded

   O arredondamento ocorreu, embora possivelmente nenhuma informação
   tenha sido perdida.

   Sinalizado sempre que o arredondamento descarta dígitos; mesmo que
   esses dígitos sejam zero (como arredondamento "5.00" a "5.0"). Se
   não for capturado, retorna o resultado inalterado. Este sinal é
   usado para detectar a perda de dígitos significativos.

class decimal.Subnormal

   O expoente foi menor que "Emin" antes do arredondamento.

   Ocorre quando um resultado da operação é subnormal (o expoente é
   muito pequeno). Se não for capturado, retorna o resultado
   inalterado.

class decimal.Underflow

   Estouro negativo numérico com resultado arredondado para zero.

   Ocorre quando um resultado subnormal é empurrado para zero
   arredondando. "Inexact" e "Subnormal" também são sinalizados.

class decimal.FloatOperation

   Ativa semânticas mais rigorosas para misturar objetos de float com
   de Decimal.

   Se o sinal não for capturado (padrão), a mistura de tipos float e
   Decimal será permitida no construtor "Decimal", "create_decimal()"
   e em todos os operadores de comparação. Tanto a conversão quanto as
   comparações são exatas. Qualquer ocorrência de uma operação mista é
   registrada silenciosamente pela configuração "FloatOperation" nos
   sinalizadores de contexto. Conversões explícitas com "from_float()"
   ou "create_decimal_from_float()" não definem o sinalizador.

   Caso contrário (o sinal é capturado), apenas comparações de
   igualdade e conversões explícitas são silenciosas. Todas as outras
   operações mistas levantam "FloatOperation".

A tabela a seguir resume a hierarquia de sinais:

   exceptions.ArithmeticError(exceptions.Exception)
       DecimalException
           Clamped
           DivisionByZero(DecimalException, exceptions.ZeroDivisionError)
           Inexact
               Overflow(Inexact, Rounded)
               Underflow(Inexact, Rounded, Subnormal)
           InvalidOperation
           Rounded
           Subnormal
           FloatOperation(DecimalException, exceptions.TypeError)


Observações sobre ponto flutuante
=================================


Atenuando o erro de arredondamento com  precisão maior
------------------------------------------------------

O uso do ponto flutuante decimal elimina o erro de representação
decimal (possibilitando representar "0.1" de forma exata); no entanto,
algumas operações ainda podem sofrer erros de arredondamento quando
dígitos diferentes de zero excederem a precisão fixa.

Os efeitos do erro de arredondamento podem ser amplificados pela soma
ou subtração de valores que se compensam quase por completo, o que
resulta em perda de significância. Knuth fornece dois exemplos
instrutivos em que a aritmética de ponto flutuante arredondado com
precisão insuficiente causa a quebra das propriedades associativas e
distributivas da adição:

   # Exemplos de Seminumerical Algorithms, Section 4.2.2.
   >>> from decimal import Decimal, getcontext
   >>> getcontext().prec = 8

   >>> u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
   >>> (u + v) + w
   Decimal('9.5111111')
   >>> u + (v + w)
   Decimal('10')

   >>> u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
   >>> (u*v) + (u*w)
   Decimal('0.01')
   >>> u * (v+w)
   Decimal('0.0060000')

O módulo "decimal" permite restaurar as identidades expandindo a
precisão o suficiente para evitar perda de significância:

   >>> getcontext().prec = 20
   >>> u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
   >>> (u + v) + w
   Decimal('9.51111111')
   >>> u + (v + w)
   Decimal('9.51111111')
   >>>
   >>> u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
   >>> (u*v) + (u*w)
   Decimal('0.0060000')
   >>> u * (v+w)
   Decimal('0.0060000')


Valores especiais
-----------------

O sistema numérico para o módulo "decimal" fornece valores especiais,
incluindo "NaN", "sNaN", "-Infinity", "Infinity", e dois zeros, "+0" e
"-0".

Os infinitos podem ser construídos diretamente com:
"Decimal('Infinity')". Além disso, eles podem resultar da divisão por
zero quando o sinal "DivisionByZero" não é capturado. Da mesma forma,
quando o sinal "Overflow" não é capturado, o infinito pode resultar do
arredondamento para além dos limites do maior número representável.

Os infinitos contêm sinais (afins) e podem ser usados em operações
aritméticas, nas quais são tratados como números muito grandes e
indeterminados. Por exemplo, adicionar uma constante ao infinito
resulta em outro infinito.

Algumas operações são indeterminadas e retornam "NaN" ou, se o sinal
"InvalidOperation" for capturado, levantam uma exceção. Por exemplo,
"0/0" retorna "NaN", que significa "não é um número" em inglês. Esta
variação de "NaN" é silenciosa e, uma vez criada, fluirá para outros
cálculos, sempre resultando em mais um "NaN". Esse comportamento pode
ser útil para uma série de cálculos que, ocasionalmente, têm entradas
ausentes --- ele permite que o cálculo continue enquanto sinaliza
resultados específicos como inválidos.

Uma variante é "sNaN", que sinaliza, em vez de permanecer em silêncio,
após cada operação. Esse é um valor de retorno útil quando um
resultado inválido precisa interromper um cálculo para tratamento
especial.

O comportamento dos operadores de comparação do Python pode ser um
pouco surpreendente quando há um "NaN" envolvido. Um teste de
igualdade em que um dos operandos é um "NaN" silencioso ou sinalizador
sempre retorna "False" (mesmo ao fazer
"Decimal('NaN')==Decimal('NaN')"), enquanto um teste de desigualdade
sempre retorna "True". Uma tentativa de comparar dois decimais usando
qualquer um dos operadores "<", "<=", ">" ou ">=" levantará o sinal
"InvalidOperation" se um dos operandos for um "NaN" e retornará
"False" se esse sinal não for capturado. Observe que a especificação
aritmética decimal geral não especifica o comportamento das
comparações diretas; as regras para comparações envolvendo um "NaN"
foram retiradas do padrão IEEE 854 (consulte a Tabela 3 na seção 5.7).
Para garantir uma conformidade rígida com os padrões, use os métodos
"compare()" e "compare_signal()".

Os zeros com sinais podem resultar de cálculos insuficientes. Eles
mantêm o sinal que teria resultado se o cálculo tivesse sido realizado
com maior precisão. Como sua magnitude é zero, os zeros positivos e
negativos são tratados como iguais e seu sinal é informacional.

Além dos dois zeros com sinais que são distintos e iguais, existem
várias representações de zero com diferentes precisões e ainda com
valor equivalente. Isso leva um pouco de tempo para se acostumar. Para
um olho acostumado a representações de ponto flutuante normalizadas,
não é imediatamente óbvio que o seguinte cálculo retorne um valor
igual a zero:

>>> 1 / Decimal('Infinity')
Decimal('0E-1000026')


Trabalhando com threads
=======================

A função "getcontext()" acessa um objeto "Context" diferente para cada
thread. Ter contextos de threads separadas significa que as threads
podem fazer alterações (como "getcontext().prec=10") sem interferir em
outras threads.

Da mesma forma, a função "setcontext()" atribui automaticamente seu
alvo à thread atual.

Se "setcontext()" não tiver sido chamado antes de "getcontext()",
então "getcontext()" criará automaticamente um novo contexto para uso
na thread atual. Novos objetos de contexto têm valores padrão
definidos a partir do objeto "decimal.DefaultContext".

O sinalizador "sys.flags.thread_inherit_context" afeta o contexto de
novas threads. Se o sinalizador for falso, as novas threads começarão
com um contexto vazio. Nesse caso, "getcontext()" criará um novo
objeto de contexto quando chamado e usará os valores padrão de
*DefaultContext*. Se o sinalizador for verdadeiro, as novas threads
começarão com uma cópia do contexto do chamador de
"threading.Thread.start()".

Para controlar os padrões para que cada thread, use os mesmos valores
em toda a aplicação, modifique diretamente o objeto *DefaultContext*.
Isso deve ser feito *antes* de qualquer thread ser iniciada, para que
não haja uma condição de corrida entre as threads chamando
"getcontext()". Por exemplo:

   # Define padrões para todo a aplicação para todas as threads prestes a serem iniciadas
   DefaultContext.prec = 12
   DefaultContext.rounding = ROUND_DOWN
   DefaultContext.traps = ExtendedContext.traps.copy()
   DefaultContext.traps[InvalidOperation] = 1
   setcontext(DefaultContext)

   # Depois, as threads podem ser iniciadas
   t1.start()
   t2.start()
   t3.start()
    . . .


Receitas
========

Aqui estão algumas receitas que servem como funções utilitárias e que
demonstram maneiras de trabalhar com a classe "Decimal":

   def moneyfmt(value, places=2, curr='', sep=',', dp='.',
                pos='', neg='-', trailneg=''):
       """Converte Decimal para uma string formatada de moeda.

       places:  número obrigatório de casas após o ponto decimal
       curr:    símbolo de moeda opcional antes do sinal (pode estar em branco)
       sep:     separador de agrupamento opcional (vírgula, ponto, espaço ou espaço em branco)
       dp:      indicador de ponto decimal (vírgula ou ponto)
                especificar como espaço em branco somente quando places for zero
       pos:     sinal opcional para números positivos: '+', espaço ou espaço em branco
       neg:     sinal opcional para números negativos: '-', '(', espaço ou espaço em branco
       trailneg:indicador de menos final opcional: '-', ')', espaço ou espaço em branco

       >>> d = Decimal('-1234567.8901')
       >>> moneyfmt(d, curr='$')
       '-$1,234,567.89'
       >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
       '1.234.568-'
       >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
       '($1,234,567.89)'
       >>> moneyfmt(Decimal(123456789), sep=' ')
       '123 456 789.00'
       >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
       '<0.02>'

       """
       q = Decimal(10) ** -places      # 2 casas --> '0.01'
       sign, digits, exp = value.quantize(q).as_tuple()
       result = []
       digits = list(map(str, digits))
       build, next = result.append, digits.pop
       if sign:
           build(trailneg)
       for i in range(places):
           build(next() if digits else '0')
       if places:
           build(dp)
       if not digits:
           build('0')
       i = 0
       while digits:
           build(next())
           i += 1
           if i == 3 and digits:
               i = 0
               build(sep)
       build(curr)
       build(neg if sign else pos)
       return ''.join(reversed(result))

   def pi():
       """Calcula Pi com a precisão atual.

       >>> print(pi())
       3.141592653589793238462643383

       """
       getcontext().prec += 2  # dígitos extras para casas intermediárias
       three = Decimal(3)      # substitui "three=3.0" para pontos flutuantes regulares
       lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
       while s != lasts:
           lasts = s
           n, na = n+na, na+8
           d, da = d+da, da+32
           t = (t * n) / d
           s += t
       getcontext().prec -= 2
       return +s               # unário com mais aplica a nova precisão

   def exp(x):
       """Retorna e elevado à potência de x. O tipo de resultado corresponde ao tipo de entrada.

       >>> print(exp(Decimal(1)))
       2.718281828459045235360287471
       >>> print(exp(Decimal(2)))
       7.389056098930650227230427461
       >>> print(exp(2.0))
       7.38905609893
       >>> print(exp(2+0j))
       (7.38905609893+0j)

       """
       getcontext().prec += 2
       i, lasts, s, fact, num = 0, 0, 1, 1, 1
       while s != lasts:
           lasts = s
           i += 1
           fact *= i
           num *= x
           s += num / fact
       getcontext().prec -= 2
       return +s

   def cos(x):
       """Retorna o cosseno de x medido em radianos.

       A aproximação da série de Taylor funciona melhor para um valor pequeno de x.
       Para valores maiores, primeiro calcule x = x % (2 * pi).

       >>> print(cos(Decimal('0.5')))
       0.8775825618903727161162815826
       >>> print(cos(0.5))
       0.87758256189
       >>> print(cos(0.5+0j))
       (0.87758256189+0j)

       """
       getcontext().prec += 2
       i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
       while s != lasts:
           lasts = s
           i += 2
           fact *= i * (i-1)
           num *= x * x
           sign *= -1
           s += num / fact * sign
       getcontext().prec -= 2
       return +s

   def sin(x):
       """Retorna o seno de x medido em radianos.

       A aproximação da série de Taylor funciona melhor para um valor pequeno de x.
       Para valores maiores, primeiro calcule x = x % (2 * pi).

       >>> print(sin(Decimal('0.5')))
       0.4794255386042030002732879352
       >>> print(sin(0.5))
       0.479425538604
       >>> print(sin(0.5+0j))
       (0.479425538604+0j)

       """
       getcontext().prec += 2
       i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
       while s != lasts:
           lasts = s
           i += 2
           fact *= i * (i-1)
           num *= x * x
           sign *= -1
           s += num / fact * sign
       getcontext().prec -= 2
       return +s


FAQ sobre Decimal
=================

P: É complicado digitar "decimal.Decimal('1234.5')". Existe uma
maneira de minimizar a digitação ao usar o interpretador interativo?

R: Alguns usuários abreviam o construtor para apenas uma única letra:

>>> D = decimal.Decimal
>>> D('1.23') + D('3.45')
Decimal('4.68')

P: Em uma aplicação de ponto fixo com duas casas decimais, algumas
entradas têm muitas casas e precisam ser arredondadas. Outros não
devem ter dígitos em excesso e precisam ser validados. Quais métodos
devem ser usados?

R: O método "quantize()" arredonda para um número fixo de casas
decimais. Se a armadilha "Inexact" estiver configurada, também será
útil para validação:

>>> TWOPLACES = Decimal(10) ** -2       # same as Decimal('0.01')

>>> # Round to two places
>>> Decimal('3.214').quantize(TWOPLACES)
Decimal('3.21')

>>> # Validate that a number does not exceed two places
>>> Decimal('3.21').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Decimal('3.21')

>>> Decimal('3.214').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Traceback (most recent call last):
   ...
Inexact: None

P: Assim que eu tiver entradas de duas casas válidas, como mantenho
essa invariante em uma aplicação?

R: Algumas operações como adição, subtração e multiplicação por um
número inteiro preservam automaticamente o ponto fixo. Outras
operações, como divisão e multiplicação não inteira, alteram o número
de casas decimais e precisam ser seguidas com uma etapa "quantize()":

>>> a = Decimal('102.72')           # Initial fixed-point values
>>> b = Decimal('3.17')
>>> a + b                           # Addition preserves fixed-point
Decimal('105.89')
>>> a - b
Decimal('99.55')
>>> a * 42                          # So does integer multiplication
Decimal('4314.24')
>>> (a * b).quantize(TWOPLACES)     # Must quantize non-integer multiplication
Decimal('325.62')
>>> (b / a).quantize(TWOPLACES)     # And quantize division
Decimal('0.03')

No desenvolvimento de aplicações de ponto fixo, é conveniente definir
funções para manipular a etapa "quantize()":

>>> def mul(x, y, fp=TWOPLACES):
...     return (x * y).quantize(fp)
...
>>> def div(x, y, fp=TWOPLACES):
...     return (x / y).quantize(fp)

>>> mul(a, b)                       # Automatically preserve fixed-point
Decimal('325.62')
>>> div(b, a)
Decimal('0.03')

P: Existem várias maneiras de expressar o mesmo valor. Os números
"200", "200.000", "2E2" e ".02E+4" têm todos o mesmo valor em várias
precisões. Existe uma maneira de transformá-los em um único valor
canônico reconhecível?

R: O método "normalize()" mapeia todos os valores equivalentes para um
único representativo:

>>> values = map(Decimal, '200 200.000 2E2 .02E+4'.split())
>>> [v.normalize() for v in values]
[Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2')]

P: Quando ocorre o arredondamento em um cálculo?

R: Ocorre *após* o cálculo. A filosofia da especificação decimal é que
os números são considerados exatos e criados independentemente do
contexto atual. Eles podem até ter maior precisão do que o contexto
atual. O processo de cálculo com essas entradas exatas e, em seguida,
o arredondamento (ou outras operações de contexto) é aplicado ao
*resultado* do cálculo:

   >>> getcontext().prec = 5
   >>> pi = Decimal('3.1415926535')   # Mais de 5 dígitos
   >>> pi                             # Todos os dígitos são retidos
   Decimal('3.1415926535')
   >>> pi + 0                         # Arredondado após uma adição
   Decimal('3.1416')
   >>> pi - Decimal('0.00005')        # Subtrai números não arredondados e depois arredonda
   Decimal('3.1415')
   >>> pi + 0 - Decimal('0.00005')    # Os valores intermediários são arredondados
   Decimal('3.1416')

P: Alguns valores decimais sempre são exibidas com notação
exponencial. Existe uma maneira de obter uma representação não
exponencial?

R: Para alguns valores, a notação exponencial é a única maneira de
expressar o número de casas significativas no coeficiente. Por
exemplo, expressar "5.0E+3" como "5000" mantém o valor constante, mas
não pode mostrar a significância de duas casa do original.

Se uma aplicação não se importa com o rastreamento da significância, é
fácil remover o expoente e os zeros à direita, perdendo a
significância, mas mantendo o valor inalterado:

>>> def remove_exponent(d):
...     return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

>>> remove_exponent(Decimal('5E+3'))
Decimal('5000')

P: Existe uma maneira de converter um float comum em um "Decimal"?

R: Sim, qualquer número de ponto flutuante binário pode ser expresso
exatamente como um Decimal, embora uma conversão exata possa exigir
mais precisão do que a intuição sugere:

   >>> Decimal(math.pi)
   Decimal('3.141592653589793115997963468544185161590576171875')

P: Em um cálculo complexo, como posso ter certeza de que não obtive um
resultado falso devido à precisão insuficiente ou a anomalias de
arredondamento.

R: O módulo decimal facilita o teste de resultados. Uma boa prática é
executar novamente os cálculos usando maior precisão e com vários
modos de arredondamento. Resultados amplamente diferentes indicam
precisão insuficiente, problemas no modo de arredondamento, entradas
mal condicionadas ou um algoritmo numericamente instável.

P: Notei que a precisão do contexto é aplicada aos resultados das
operações, mas não às entradas. Há algo a observar ao misturar valores
de diferentes precisões?

R: Sim. O princípio é que todos os valores são considerados exatos,
assim como a aritmética desses valores. Somente os resultados são
arredondados. A vantagem das entradas é que "o que você vê é o que
você obtém". Uma desvantagem é que os resultados podem parecer
estranhos se você esquecer que as entradas não foram arredondadas:

   >>> getcontext().prec = 3
   >>> Decimal('3.104') + Decimal('2.104')
   Decimal('5.21')
   >>> Decimal('3.104') + Decimal('0.000') + Decimal('2.104')
   Decimal('5.20')

A solução é aumentar a precisão ou forçar o arredondamento das
entradas usando a operação unária de mais:

   >>> getcontext().prec = 3
   >>> +Decimal('1.23456789')      # unary plus triggers rounding
   Decimal('1.23')

Como alternativa, as entradas podem ser arredondadas na criação usando
o método "Context.create_decimal()":

>>> Context(prec=5, rounding=ROUND_DOWN).create_decimal('1.2345678')
Decimal('1.2345')

P: A implementação do CPython é rápida para números grandes?

A: Sim. Nas implementações CPython e PyPy3, as versões C/CFFI do
módulo decimal integram a biblioteca de alta velocidade libmpdec para
precisão arbitrária de aritmética de ponto flutuante decimal
corretamente arredondado [1]. "libmpdec" usa a multiplicação de
Karatsuba para números com tamanho médio e a Transformada Numérica de
Fourier para números muito grandes.

O contexto deve ser adaptado para uma aritmética exata de precisão
arbitrária. "Emin" e "Emax" devem sempre ser configurados com os
valores máximos, "clamp" deve sempre ser 0 (o padrão). A configuração
de "prec" requer alguns cuidados.

A abordagem mais fácil para testar a aritmética do bignum é usar o
valor máximo para "prec" também [2]:

   >>> setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))
   >>> x = Decimal(2) ** 256
   >>> x / 128
   Decimal('904625697166532776746648320380374280103671755200316906558262375061821325312')

Para resultados inexatos, "MAX_PREC" é muito grande em plataformas de
64 bits e a memória disponível será insuficiente:

   >>> Decimal(1) / 3
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   MemoryError

Em sistemas com alocação excessiva (por exemplo, Linux), uma abordagem
mais sofisticada é ajustar "prec" à quantidade de RAM disponível.
Suponha que você tenha 8 GB de RAM e espere 10 operandos simultâneos
usando no máximo 500 MB cada:

   >>> import sys
   >>>
   >>> # Número máximo de dígitos para um único operando usando 500 MB
   >>> # em palavras de 8 bytes com 19 dígitos por palavra (4 bytes e 9 dígitos
   >>> # para a construção de 32 bits):
   >>> maxdigits = 19 * ((500 * 1024**2) // 8)
   >>>
   >>> # Confere que isso funciona:
   >>> c = Context(prec=maxdigits, Emax=MAX_EMAX, Emin=MIN_EMIN)
   >>> c.traps[Inexact] = True
   >>> setcontext(c)
   >>>
   >>> # Preenche a precisão disponível com noves:
   >>> x = Decimal(0).logical_invert() * 9
   >>> sys.getsizeof(x)
   524288112
   >>> x + 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     decimal.Inexact: [<class 'decimal.Inexact'>]

Em geral (e especialmente em sistemas sem alocação excessiva),
recomenda-se estimar limites ainda mais apertados e definir a
armadilha "Inexact" se for esperado que todos os cálculos sejam mais
precisos.

[1] Adicionado na versão 3.3.

[2] Alterado na versão 3.9: Esta abordagem agora funciona para todos
    os resultados exatos, exceto para potências de números que não
    sejam inteiros.
