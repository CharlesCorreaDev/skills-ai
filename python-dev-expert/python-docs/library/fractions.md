"fractions" --- Números racionais
*********************************

**Código-fonte:** Lib/fractions.py

======================================================================

O módulo "fractions" fornece suporte para aritmética de números
racionais.

Uma instância de Fraction pode ser construída a partir de um par de
números racionais, de um único número ou de uma string.

class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(number)
class fractions.Fraction(string)

   A primeira versão requer que *numerator* e *denominator* sejam
   instâncias de "numbers.Rational" e retorna uma nova instância de
   "Fraction" com um valor igual a "numerator/denominator". Se
   *denominator* for zero, ele levanta uma "ZeroDivisionError".

   A segunda versão requer que *number* seja uma instância de
   "numbers.Rational" ou tenha o método "as_integer_ratio()" (isso
   inclui "float" e "decimal.Decimal"). Ela retorna uma instância de
   "Fraction" com exatamente o mesmo valor. É presumido que o método
   "as_integer_ratio()" retorne um par de inteiros primos entre si e
   que o último seja positivo. Observe que, devido aos problemas
   comuns com pontos binários (consulte Aritmética de ponto flutuante:
   problemas e limitações), o argumento para "Fraction(1.1)" não é
   exatamente igual a 11/10 e, portanto, "Fraction(1.1)" *não* retorna
   "Fraction(11, 10)" como seria de se esperar. (Mas consulte a
   documentação do método "limit_denominator()" abaixo.)

   A última versão do construtor espera uma string. O formato usual
   para esta instância é:

      [sinal] numerador ['/' denominador]

   onde o "sign" opcional pode ser '+' ou '-' e "numerator" e
   "denominator" (se presente) são strings de dígitos decimais
   (sublinhados podem ser usados para delimitar dígitos como com
   literais integrais no código). Além disso, qualquer string que
   represente um valor finito e seja aceita pelo construtor "float"
   também é aceita pelo construtor "Fraction". Em qualquer forma, a
   string de entrada também pode ter espaços em branco à esquerda e/ou
   à direita. Aqui estão alguns exemplos:

      >>> from fractions import Fraction
      >>> Fraction(16, -10)
      Fraction(-8, 5)
      >>> Fraction(123)
      Fraction(123, 1)
      >>> Fraction()
      Fraction(0, 1)
      >>> Fraction('3/7')
      Fraction(3, 7)
      >>> Fraction(' -3/7 ')
      Fraction(-3, 7)
      >>> Fraction('1.414213 \t\n')
      Fraction(1414213, 1000000)
      >>> Fraction('-.125')
      Fraction(-1, 8)
      >>> Fraction('7e-6')
      Fraction(7, 1000000)
      >>> Fraction(2.25)
      Fraction(9, 4)
      >>> Fraction(1.1)
      Fraction(2476979795053773, 2251799813685248)
      >>> from decimal import Decimal
      >>> Fraction(Decimal('1.1'))
      Fraction(11, 10)

   A classe "Fraction" herda da classe base abstrata
   "numbers.Rational" e implementa todos os métodos e operações dessa
   classe. As instâncias de "Fraction" são *hasheável* e devem ser
   tratadas como imutáveis. Além disso, "Fraction" tem as seguintes
   propriedades e métodos:

   Alterado na versão 3.2: O construtor "Fraction" agora aceita
   instâncias "float" e "decimal.Decimal".

   Alterado na versão 3.9: A função "math.gcd()" agora é usada para
   normalizar o *numerator* e o *denominator*. "math.gcd()" sempre
   retorna um tipo "int". Anteriormente, o tipo GCD dependia do
   *numerator* e do *denominator*.

   Alterado na versão 3.11: Sublinhados agora são permitidos ao criar
   uma instância "Fraction" a partir de uma string, seguindo as regras
   **PEP 515**.

   Alterado na versão 3.11: "Fraction" implementa "__int__" agora para
   satisfazer verificações de instância "typing.SupportsInt".

   Alterado na versão 3.12: É permitido espaço ao redor da barra para
   entradas de string: "Fraction('2 / 3')".

   Alterado na versão 3.12: Instâncias de "Fraction" agora oferecem
   suporte à formatação no estilo float, com tipos de apresentação
   ""e"", ""E"", ""f"", ""F"", ""g"", ""G"" e ""%"".

   Alterado na versão 3.13: A formatação de instâncias "Fraction" sem
   um tipo de apresentação agora oferece suporte a preenchimento,
   alinhamento, tratamento de sinais, largura mínima e agrupamento.

   Alterado na versão 3.14: O construtor "Fraction" agora aceita
   qualquer objeto com o método "as_integer_ratio()".

   numerator

      Numerador de Fraction no menor termo.

   denominator

      Denominador de Fraction em termos mínimos. Garantidamente
      positivo.

   as_integer_ratio()

      Retorna uma tupla de dois inteiros, cuja razão é igual a
      Fraction original. A razão está em termos mais baixos e tem um
      denominador positivo.

      Adicionado na versão 3.8.

   is_integer()

      Retorna "True" se a Fraction for um inteiro.

      Adicionado na versão 3.12.

   classmethod from_float(f)

      Construtor alternativo que aceita apenas instâncias de "float"
      ou "numbers.Integral". Esteja ciente de que
      "Fraction.from_float(0.3)" não é o mesmo valor que "Fraction(3,
      10)".

      Nota:

        A partir do Python 3.2, você também pode construir uma
        instância "Fraction" diretamente de um "float".

   classmethod from_decimal(dec)

      Construtor alternativo que aceita somente instâncias de
      "decimal.Decimal" ou "numbers.Integral".

      Nota:

        A partir do Python 3.2, você também pode construir uma
        instância "Fraction" diretamente de uma instância de
        "decimal.Decimal".

   classmethod from_number(number)

      Construtor alternativo que aceita apenas instâncias de
      "numbers.Integral", "numbers.Rational", "float" ou
      "decimal.Decimal" e objetos com o método "as_integer_ratio()",
      mas não strings.

      Adicionado na versão 3.14.

   limit_denominator(max_denominator=1000000)

      Encontra e retorna o "Fraction" mais próximo de "self" que tem
      denominador no máximo max_denominator. Este método é útil para
      encontrar aproximações racionais para um dado número de ponto
      flutuante:

      >>> from fractions import Fraction
      >>> Fraction('3.1415926535897932').limit_denominator(1000)
      Fraction(355, 113)

      ou para recuperar um número racional que é representado como um
      ponto flutuante:

      >>> from math import pi, cos
      >>> Fraction(cos(pi/3))
      Fraction(4503599627370497, 9007199254740992)
      >>> Fraction(cos(pi/3)).limit_denominator()
      Fraction(1, 2)
      >>> Fraction(1.1).limit_denominator()
      Fraction(11, 10)

   __floor__()

      Retorna o maior "int" "<= self". Este método também pode ser
      acessado por meio da função "math.floor()":

      >>> from math import floor
      >>> floor(Fraction(355, 113))
      3

   __ceil__()

      Retorna o menor "int" ">= self". Este método também pode ser
      acessado por meio da função "math.ceil()".

   __round__()
   __round__(ndigits)

      A primeira versão retorna o "int" mais próximo de "self",
      arredondando a metade para par. A segunda versão arredonda
      "self" para o múltiplo mais próximo de "Fraction(1,
      10**ndigits)" (logicamente, se "ndigits" for negativo),
      novamente arredondando a metade para par. Este método também
      pode ser acessado por meio da função "round()".

   __format__(format_spec, /)

      Fornece suporte para formatação de instâncias de "Fraction" por
      meio do método "str.format()", da função embutida "format()" ou
      literais de strings formatadas.

      Se a string de especificação de formato "format_spec" não
      terminar com um dos tipos de apresentação "'e'", "'E'", "'f'",
      "'F'", "'g'", "'G'" ou "'%'", então a formatação segue as regras
      gerais para preenchimento, alinhamento, tratamento de sinais,
      largura mínima e agrupamento, conforme descrito na minilinguagem
      de especificação de formato. O sinalizador de "formato
      alternativo" "'#'" é suportado: se presente, ele força a string
      de saída a sempre incluir um denominador explícito, mesmo quando
      o valor que está sendo formatado é um inteiro exato. O
      sinalizador de preenchimento de zeros "'0'" não é suportado.

      Se a string de especificação de formato "format_spec" terminar
      com um dos tipos de apresentação "'e'", "'E'", "'f'", "'F'",
      "'g'", "'G'" ou "'%'", então a formatação segue as regras
      descritas para o tipo "float" na seção Minilinguagem de
      especificação de formato.

      Veja alguns exemplos:

         >>> from fractions import Fraction
         >>> format(Fraction(103993, 33102), '_')
         '103_993/33_102'
         >>> format(Fraction(1, 7), '.^+10')
         '...+1/7...'
         >>> format(Fraction(3, 1), '')
         '3'
         >>> format(Fraction(3, 1), '#')
         '3/1'
         >>> format(Fraction(1, 7), '.40g')
         '0.1428571428571428571428571428571428571429'
         >>> format(Fraction('1234567.855'), '_.2f')
         '1_234_567.86'
         >>> f"{Fraction(355, 113):*>20.6e}"
         '********3.141593e+00'
         >>> old_price, new_price = 499, 672
         >>> "{:.2%} price increase".format(Fraction(new_price, old_price) - 1)
         '34.67% price increase'

Ver também:

  Módulo "numbers"
     As classes base abstratas que compõem a torre numérica.
