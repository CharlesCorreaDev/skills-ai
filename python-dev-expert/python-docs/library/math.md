"math" --- Funções matemáticas
******************************

======================================================================

Este módulo fornece acesso à constantes e funções matemáticas comuns,
incluindo aquelas definidas pelo padrão C.

Essas funções não podem ser usadas com números complexos; use as
funções de mesmo nome do módulo "cmath" se você precisar de suporte
para números complexos. A distinção entre funções que suportam números
complexos e aquelas que não suportam é feita uma vez que a maioria dos
usuários não quer aprender a matemática necessária para entender
números complexos. Receber uma exceção em vez de um resultado complexo
permite a detecção antecipada do número complexo inesperado usado como
parâmetro, para que o programador possa determinar como e por que ele
foi gerado em primeiro lugar.

As funções a seguir são fornecidas por este módulo. Exceto quando
explicitamente indicado de outra forma, todos os valores de retorno
são pontos flutuantes.

+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Arimética de ponto flutuante**                                                                                                                                              |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "ceil(x)"                                            | Teto de *x*, o menor número inteiro maior ou igual a *x*                                                               |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "fabs(x)"                                            | Valor absoluto de *x*                                                                                                  |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "floor(x)"                                           | Piso de *x*, o maior inteiro menor ou igual a *x*                                                                      |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "fma(x, y, z)"                                       | Operação de multiplicação e adição combinadas: "(x * y) + z"                                                           |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "fmax(x, y)"                                         | Máximo de dois valores de ponto flutuante                                                                              |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "fmin(x, y)"                                         | Mínimo de dois valores de ponto flutuante                                                                              |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "fmod(x, y)"                                         | Resto da divisão "x / y"                                                                                               |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "modf(x)"                                            | Partes fracionárias e inteiras de *x*                                                                                  |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "remainder(x, y)"                                    | Resto de *x* em relação a *y*                                                                                          |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "trunc(x)"                                           | Parte inteira de *x*                                                                                                   |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Funções de manipulação de ponto flutuante**                                                                                                                                 |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "copysign(x, y)"                                     | Magnitude (valor absoluto) de *x* com o sinal de *y*                                                                   |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "frexp(x)"                                           | Mantissa e expoente de *x*                                                                                             |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "isclose(a, b, rel_tol, abs_tol)"                    | Verifica se os valores *a* e *b* estão próximos um do outro                                                            |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "isfinite(x)"                                        | Verifica se *x* não é infinito e nem um NaN                                                                            |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "isnormal(x)"                                        | Verifica se *x* é um número normal                                                                                     |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "issubnormal(x)"                                     | Verifica se *x* é um número subnormal                                                                                  |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "isinf(x)"                                           | Verifica se *x* é um infinito positivo ou negativo                                                                     |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "isnan(x)"                                           | Verifica se *x* é um NaN (não um número)                                                                               |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "ldexp(x, i)"                                        | "x * (2**i)", inverso da função "frexp()"                                                                              |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "nextafter(x, y, steps)"                             | Valor de ponto flutuante de *steps* passos depois de *x* em direção a *y*                                              |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "signbit(x)"                                         | Verifica se *x* é um número negativo                                                                                   |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "ulp(x)"                                             | Valor do bit menos significativo de *x*                                                                                |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Funções de potências, exponenciais e logarítmicas**                                                                                                                         |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "cbrt(x)"                                            | Raiz cúbica de *x*                                                                                                     |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "exp(x)"                                             | *e* elevado à potência *x*                                                                                             |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "exp2(x)"                                            | *2* elevado a potência de *x*                                                                                          |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "expm1(x)"                                           | *e* elevado a potência de *x*, menos 1                                                                                 |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "log(x, base)"                                       | Logaritmo de *x* para a base fornecida (*e* por padrão)                                                                |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "log1p(x)"                                           | Logaritmo natural de *1+x* (base *e*)                                                                                  |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "log2(x)"                                            | Logaritmo de base 2 de *x*                                                                                             |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "log10(x)"                                           | Logaritmo de base 10 de *x*                                                                                            |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "pow(x, y)"                                          | *x* elevado à potência *y*                                                                                             |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "sqrt(x)"                                            | Raiz quadrada de *x*                                                                                                   |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Funções de soma e produto**                                                                                                                                                 |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "dist(p, q)"                                         | Distância euclidiana entre dois pontos *p* e *q* dada como um iterável de coordenadas                                  |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "fsum(iterable)"                                     | Soma dos valores na entrada *iterable*                                                                                 |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "hypot(*coordinates)"                                | Norma euclidiana de um iterável de coordenadas                                                                         |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "prod(iterable, start)"                              | Produto de elementos da entrada *iterable* com um valor *start*                                                        |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "sumprod(p, q)"                                      | Soma dos produtos de dois iteráveis *p* e *q*                                                                          |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Conversão angular**                                                                                                                                                         |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "degrees(x)"                                         | Converte o ângulo *x* de radianos para graus                                                                           |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "radians(x)"                                         | Converte o ângulo *x* de graus para radianos                                                                           |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Funções trigonométricas**                                                                                                                                                   |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "acos(x)"                                            | Arco cosseno de *x*                                                                                                    |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "asin(x)"                                            | Arco seno de *x*/                                                                                                      |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "atan(x)"                                            | Arco tangente de *x*                                                                                                   |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "atan2(y, x)"                                        | "atan(y / x)"                                                                                                          |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "cos(x)"                                             | Cosseno de *x*                                                                                                         |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "sin(x)"                                             | Seno de *x*                                                                                                            |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "tan(x)"                                             | Tangente de *x*                                                                                                        |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Funções hiperbólicas**                                                                                                                                                      |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "acosh(x)"                                           | Cosseno hiperbólico inverso de *x*                                                                                     |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "asinh(x)"                                           | Seno hiperbólico inverso de *x*                                                                                        |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "atanh(x)"                                           | Tangente hiperbólico inverso de *x*                                                                                    |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "cosh(x)"                                            | Cosseno hiperbólico de *x*                                                                                             |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "sinh(x)"                                            | Seno hiperbólico de *x*                                                                                                |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "tanh(x)"                                            | Tangente hiperbólico de *x*                                                                                            |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Funções especiais**                                                                                                                                                         |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "erf(x)"                                             | Função erro em *x*                                                                                                     |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "erfc(x)"                                            | Função erro complementar em *x*                                                                                        |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "gamma(x)"                                           | Função gama em *x*                                                                                                     |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "lgamma(x)"                                          | Logaritmo natural do valor absoluto da função gama em *x*                                                              |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| **Constantes**                                                                                                                                                                |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "pi"                                                 | *π* = 3.141592...                                                                                                      |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "e"                                                  | *e* = 2.718281...                                                                                                      |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "tau"                                                | *τ* = 2*π* = 6.283185...                                                                                               |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "inf"                                                | Infinito positivo                                                                                                      |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| "nan"                                                | "Not a number" (NaN)                                                                                                   |
+------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+


Arimética de ponto flutuante
============================

math.ceil(x)

   Retorna o teto de *x*, o menor inteiro maior ou igual que *x*. Se
   *x* não é um float, delega para "x.__ceil__", que deve retornar um
   valor do tipo "Integral".

math.fabs(x)

   Retorna o valor absoluto de *x*.

math.floor(x)

   Retorna o chão de *x*, o maior inteiro menor ou igual a *x*. Se *x*
   não é um ponto flutuante, delega para "x.__floor__", que deve
   retornar um valor do tipo "Integral"

math.fma(x, y, z)

   Operação de multiplicação-adição combinada. Retorna "(x * y) + z",
   calculado de forma a obter o mesmo resultado que seria obtido se o
   cálculo desfrutasse de precisão e limites infinitos, seguido de um
   único arredondamento para o formato "float". Esta operação
   frequentemente oferece acurácia melhor do que a expressão direta
   "(x * y) + z" ofereceria.

   Esta função segue a especificação da operação fusedMultiplyAdd
   descrita no padrão IEEE 754. O padrão deixa um caso a ser definido
   pela implementação, que são os resultados de "fma(0, inf, nan)" e
   "fma(inf, 0, nan)". Nestes casos, "math.fma" retorna NaN, e não
   levanta nenhuma exceção.

   Adicionado na versão 3.13.

math.fmax(x, y)

   Obtém o maior de dois valores de ponto flutuante, tratando NaNs
   como dados ausentes.

   Quando ambos os operandos forem NaNs (com sinal) ou zeros, retorna-
   se "nan" e "0", respectivamente, e o sinal do resultado é definido
   pela implementação; isto é, não se exige que "fmax()" leve em
   consideração o sinal de tais operandos (veja o Anexo F da norma
   C11, §F.10.0.3 e §F.10.9.2).

   Adicionado na versão 3.15.

math.fmin(x, y)

   Obtém o menor de dois valores de ponto flutuante, tratando NaNs
   como dados ausentes.

   Quando ambos os operandos forem NaNs (com sinal) ou zeros, retorna-
   se "nan" e "0", respectivamente, e o sinal do resultado é definido
   pela implementação; isto é, não se exige que "fmin()" leve em
   consideração o sinal de tais operandos (veja o Anexo F da norma
   C11, §F.10.0.3 e §F.10.9.2).

   Adicionado na versão 3.15.

math.fmod(x, y)

   Retorna o resto ponto flutuante de "x / y", conforme definido pela
   função "fmod(x, y)" da biblioteca C da plataforma. Observe que a
   expressão Python "x % y" pode não retornar o mesmo resultado. A
   intenção do padrão C é que "fmod(x, y)" seja exatamente
   (matematicamente; com precisão infinita) igual a "x - n*y" para
   algum inteiro *n* de modo que o resultado tenha o mesmo sinal que
   *x* e magnitude menor que "abs(y)". O "x % y" do Python retorna um
   resultado com o sinal de *y*, e pode não ser exatamente computável
   para argumentos de ponto flutuante. Por exemplo, "fmod(-1e-100,
   1e100)" é "-1e-100", mas o resultado de "-1e-100 % 1e100" do Python
   é "1e100-1e-100", que não pode ser representado exatamente como um
   ponto flutuante, e é arredondado para o surpreendente "1e100". Por
   esta razão, a função "fmod()" é geralmente preferida ao trabalhar
   com pontos flutuantes, enquanto o "x % y" do Python é preferido ao
   trabalhar com inteiros.

math.modf(x)

   Retorna as partes fracionárias e inteiras de *x*. Ambos os
   resultados carregam o sinal de *x* e são pontos flutuantes.

   Observe que "modf()" tem um padrão de chamada/retorno diferente de
   seu equivalente C: elas pegam um único argumento e retornam um par
   de valores, ao invés de retornar seu segundo valor de retorno por
   meio de um "parâmetro de saída" (não existe tal coisa em Python).

math.remainder(x, y)

   Retorna o resto no estilo IEEE 754 de *x* em relação a *y*. Para o
   finito *x* e o finito diferente de zero *y*, esta é a diferença "x
   - n*y", onde "n" é o número inteiro mais próximo do valor exato do
   quociente "x / y" . Se "x / y" está exatamente no meio do caminho
   entre dois inteiros consecutivos, o inteiro *par* mais próximo é
   usado para "n". O resto "r = remainder(x, y)" assim sempre satisfaz
   "abs(r) <= 0.5 * abs(y)".

   Casos especiais seguem IEEE 754: em particular, "remainder(x,
   math.inf)" é *x* para qualquer *x* finito, e "remainder(x, 0)" e
   "remainder(math.inf, x)" levantam "ValueError" para qualquer *x*
   não NaN. Se o resultado da operação "remainder" for zero, esse zero
   terá o mesmo sinal de *x*.

   Em plataformas que usam ponto flutuante binário do IEEE 754, o
   resultado dessa operação é sempre exatamente representável: nenhum
   erro de arredondamento é introduzido.

   Adicionado na versão 3.7.

math.trunc(x)

   Retorna *x* com a parte fracionária removida, deixando a parte
   inteira. Isso arredonda para 0: "trunc()" é equivalente a "floor()"
   para *x* positivos, e equivalentes a "ceil()" para *x* negativos.
   Se *x* não é um ponto flutuante, então delega para "x.__trunc__",
   cujo qual deve retornar um valor do tipo "Integral".

Para as funções "ceil()", "floor()" e "modf()", observe que *todos* os
números de ponto flutuante de magnitude suficientemente grande são
inteiros exatos. Os pontos flutuantes do Python normalmente não
carregam mais do que 53 bits de precisão (o mesmo que o tipo duplo da
plataforma C), caso em que qualquer ponto flutuante *x* com "abs(x) >=
2**52" necessariamente não tem bits fracionários.


Funções de manipulação de ponto flutuante
=========================================

math.copysign(x, y)

   Retorna um ponto flutuante com a magnitude (valor absoluto) de *x*,
   mas o sinal de *y*. Em plataformas que suportam zeros com sinal,
   "copysign(1.0, -0.0)" retorna *-1.0*.

math.frexp(x)

   Retorna a mantissa e o expoente de *x* como o par "(m, e)". Se *x*
   for um número finito diferente de zero, então *m* é um float com
   "0.5 <= abs(m) < 1.0" e um inteiro *e* é tal que "x == m * 2**e"
   exatamente. Caso contrário, retorna "(x, 0)". Isso é usado para
   "desmembrar" a representação interna de um float de maneira
   portátil.

   Observe que "frexp()" tem um padrão de chamada/retorno diferente de
   seu equivalente C: elas pegam um único argumento e retornam um par
   de valores, ao invés de retornar seu segundo valor de retorno por
   meio de um "parâmetro de saída" (não existe tal coisa em Python).

math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

   Retorna "True" se os valores *a* e *b* estiverem próximos e "False"
   caso contrário.

   Se dois valores são considerados próximos ou não é determinado de
   acordo com tolerâncias absolutas e relativas fornecidas. Se nenhum
   erro ocorrer, o resultado será: "abs(a-b) <= max(rel_tol *
   max(abs(a), abs(b)), abs_tol)".

   *rel_tol* é a tolerância relativa -- é a diferença máxima permitida
   entre *a* e *b*, em relação ao maior valor absoluto de *a* ou *b*.
   Por exemplo, para definir uma tolerância de 5%, passe
   "rel_tol=0.05". A tolerância padrão é "1e-09", o que garante que os
   dois valores sejam iguais em cerca de 9 dígitos decimais. *rel_tol*
   deve ser não negativo e menor que "1.0".

   *abs_tol* é a tolerância absoluta; o padrão é "0.0" e deve ser não
   negativo. Ao comparar "x" com "0.0", "isclose(x, 0)" é computado
   como "abs(x) <= rel_tol * abs(x)", que é "False" para qualquer "x"
   não zero e *rel_tol* menor que "1.0". Então adicione um argumento
   *abs_tol* positivo apropriado à chamada.

   Os valores especiais do IEEE 754 de "NaN", "inf" e "-inf" serão
   tratados de acordo com as regras do IEEE. Especificamente, "NaN"
   não é considerado próximo a qualquer outro valor, incluindo "NaN".
   "inf" e "-inf" são considerados apenas próximos a si mesmos.

   Adicionado na versão 3.5.

   Ver também:

     **PEP 485** -- Uma função para testar igualdade aproximada

math.isfinite(x)

   Retorna "True" se *x* não for um infinito nem um NaN, e "False"
   caso contrário.  (Observe que "0.0" *é* considerado finito.)

   Adicionado na versão 3.2.

math.isnormal(x)

   Retorna "True" se *x* for um número normal, isto é, um número
   finito e diferente de zero que não seja subnormal (veja
   "issubnormal()"). Retorna "False" caso contrário.

   Adicionado na versão 3.15.

math.issubnormal(x)

   Retorna "True" se *x* for um número subnormal, isto é, um número
   finito e diferente de zero com magnitude menor que
   "sys.float_info.min". Retorna "False" caso contrário.

   Adicionado na versão 3.15.

math.isinf(x)

   Retorna "True" se *x* for um infinito positivo ou negativo, e
   "False" caso contrário.

math.isnan(x)

   Retorna "True" se *x* for um NaN (não um número), e "False" caso
   contrário.

math.ldexp(x, i)

   Retorna "x * (2**i)". Este é essencialmente o inverso da função
   "frexp()".

math.nextafter(x, y, steps=1)

   Retorna o valor de ponto flutuante com *steps* passos após *x* em
   direção a *y*.

   Se *x* for igual a *y*, retorna *y*, a menos que *steps* seja zero.

   Exemplos:

   * "math.nextafter(x, math.inf)" sobe: em direção ao infinito
     positivo.

   * "math.nextafter(x, -math.inf)" desce: em direção ao menos
     infinito.

   * "math.nextafter(x, 0.0)" vai em direção a zero.

   * "math.nextafter(x, math.copysign(math.inf, x))" se afasta do
     zero.

   Veja também "math.ulp()".

   Adicionado na versão 3.9.

   Alterado na versão 3.12: Adicionado o argumento *steps*.

math.signbit(x)

   Retorna "True" se o sinal de *x* for negativo e "False" caso
   contrário.

   Isso é útil para detectar o bit de sinal de zeros, infinitos e
   NaNs.

   Adicionado na versão 3.15.

math.ulp(x)

   Retorna o valor do bit menos significativo do ponto flutuante *x*:

   * Se *x* for um NaN (não um número), retorna *x*.

   * Se *x* for negativo, retorna "ulp(-x)".

   * Se *x* for um infinito positivo, retorna *x*.

   * Se *x* for igual a zero, retorna o menor valor flutuante positivo
     *desnormalizado* representável (menor que o ponto flutuante de
     valor mínimo positivo *normalizado*, "sys.float_info.min").

   * Se *x* for igual ao maior ponto flutuante positivo representável,
     retorna o valor do bit menos significativo de *x*, tal que o
     primeiro ponto flutuante menor que *x* seja "x - ulp(x)".

   * Caso contrário (*x* é um número finito positivo), retorna o valor
     do bit menos significativo de *x*, de modo que o primeiro ponto
     flutuante maior que *x* seja "x + ulp(x)".

   ULP significa "Unit in the Last Place" ou, em português, unidade na
   última posição.

   Veja também "math.nextafter()" e "sys.float_info.epsilon".

   Adicionado na versão 3.9.


Funções de potências, exponenciais e logarítmicas
=================================================

math.cbrt(x)

   Retorna a raiz cúbica de *x*.

   Adicionado na versão 3.11.

math.exp(x)

   Retorna *e* elevado à potência *x*, onde *e* = 2.718281... é a base
   dos logaritmos naturais. Isso geralmente é mais preciso do que
   "math.e ** x" ou "pow(math.e, x)".

math.exp2(x)

   Retorna *2* elevado a *x*

   Adicionado na versão 3.11.

math.expm1(x)

   Retorna *e* elevado à potência *x*, menos 1. Aqui *e* é a base dos
   logaritmos naturais. Para pequenos pontos flutuantes *x*, a
   subtração em "exp(x) - 1" pode resultar em uma perda significativa
   de precisão; a função "expm1()" fornece uma maneira de calcular
   essa quantidade com precisão total:

   >>> from math import exp, expm1
   >>> exp(1e-5) - 1  # gives result accurate to 11 places
   1.0000050000069649e-05
   >>> expm1(1e-5)    # result accurate to full precision
   1.0000050000166668e-05

   Adicionado na versão 3.2.

math.log(x[, base])

   Com um argumento, retorna o logaritmo natural de *x* (para base
   *e*).

   Com dois argumentos, retorna o logaritmo de *x* para a *base*
   fornecida, calculada como "log(x)/log(base)".

math.log1p(x)

   Retorna o logaritmo natural de *1+x* (base *e*). O resultado é
   calculado de forma precisa para *x* próximo a zero.

math.log2(x)

   Retorna o logaritmo de base 2 de *x*. Isso geralmente é mais
   preciso do que "log(x, 2)".

   Adicionado na versão 3.3.

   Ver também:

     "int.bit_length()" retorna o número de bits necessários para
     representar um inteiro em binário, excluindo o sinal e os zeros à
     esquerda.

math.log10(x)

   Retorna o logaritmo de base 10 de *x*. Isso geralmente é mais
   preciso do que "log(x, 10)".

math.pow(x, y)

   Retorna *x* elevado a potência de *y*. Exceções seguem o padrão
   IEEE 754 o máximo possível. "pow(1.0, x)" e "pow(x, 0.0)" em
   particular sempre retornam "1.0", mesmo quando *x* é ZERO ou NaN.
   Se ambos *x* e *y* são números finitos, *x* é negativo, e *y* não é
   um inteiro então "pow(x, y)" é indefinido e levanta "ValueError".

   Ao contrário do operador embutido "**", "math.pow()" converte ambos
   os seus argumentos para o tipo "float". Use "**" ou a função
   embutida "pow()" para calcular potências inteiras exatas.

   Alterado na versão 3.11: Os casos especiais "pow(0.0, -inf)" e
   "pow(-0.0, -inf)" foram alterados para retornar "inf" ao invés de
   levantar "ValueError", para ter consistência com a IEEE 754.

math.sqrt(x)

   Retorna a raiz quadrada de *x*.


Funções de soma e produto
=========================

math.dist(p, q)

   Retorna a distância euclidiana entre dois pontos *p* e *q*, cada um
   dado como uma sequência (ou iterável) de coordenadas. Os dois
   pontos devem ter a mesma dimensão.

   Aproximadamente equivalente a:

      sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q, strict=True)))

   Adicionado na versão 3.8.

math.fsum(iterable)

   Retorna uma soma precisa dos valores de ponto flutuante no
   iterável. Evita perda de precisão rastreando várias somas parciais
   intermediárias.

   A precisão do algoritmo depende das garantias aritméticas do
   IEEE-754 e do caso típico em que o modo de arredondamento é meio
   par. Em algumas compilações que não são do Windows, a biblioteca C
   subjacente usa adição de precisão estendida e pode ocasionalmente
   arredondar uma soma intermediária fazendo com que ela introduza um
   erro no bit menos significativo.

   Para uma discussão mais aprofundada e duas abordagens alternativas,
   consulte o ASPN cookbook recipes for accurate floating point
   summation.

math.hypot(*coordinates)

   Retorna a norma euclidiana, "sqrt(sum(x**2 for x in coordinates))".
   Este é o comprimento do vetor da origem até o ponto dado pelas
   coordenadas.

   Para um ponto bidimensional "(x, y)", isso é equivalente a calcular
   a hipotenusa de um triângulo retângulo usando o teorema de
   Pitágoras, "sqrt(x*x + y*y)".

   Alterado na versão 3.8: Adicionado suporte para pontos
   n-dimensionais. Anteriormente, apenas o caso bidimensional era
   suportado.

   Alterado na versão 3.10: Melhorou a precisão do algoritmo para que
   o erro máximo seja inferior a 1 ulp (unidade no último lugar). Mais
   tipicamente, o resultado é quase sempre arredondado corretamente
   para 1/2 ulp.

math.prod(iterable, *, start=1)

   Calcula o produto de todos os elementos na entrada *iterable*. O
   valor *start* padrão para o produto é "1".

   Quando o iterável estiver vazio, retorna o valor de start. Esta
   função deve ser usada especificamente com valores numéricos e pode
   rejeitar tipos não numéricos.

   Adicionado na versão 3.8.

math.sumprod(p, q)

   Retorna a soma dos produtos dos valores de dois iteráveis *p* e
   *q*.

   Levanta "ValueError" se as entradas não tiverem o mesmo
   comprimento.

   Aproximadamente equivalente a:

      sum(map(operator.mul, p, q, strict=True))

   Para entradas float e mistas int/float, os produtos intermediários
   e as somas são calculados com precisão estendida.

   Adicionado na versão 3.12.


Conversão angular
=================

math.degrees(x)

   Converte o ângulo *x* de radianos para graus.

math.radians(x)

   Converte o ângulo *x* de graus para radianos.


Funções trigonométricas
=======================

math.acos(x)

   Retorna o arco cosseno de *x*, em radianos. O resultado está entre
   "0" e "pi".

math.asin(x)

   Retorna o arco seno de *x*, em radianos. O resultado está entre
   "-pi/2" e "pi/2".

math.atan(x)

   Retorna o arco tangente de *x*, em radianos. O resultado está entre
   "-pi/2" e "pi/2".

math.atan2(y, x)

   Retorna "atan(y / x)", em radianos. O resultado está entre "-pi" e
   "pi". O vetor no plano da origem ao ponto "(x, y)" faz este ângulo
   com o eixo X positivo. O ponto de "atan2()" é que os sinais de
   ambas as entradas são conhecidos por ele, então ele pode calcular o
   quadrante correto para o ângulo. Por exemplo, "atan(1)" e "atan2(1,
   1)" são ambos "pi/4", mas "atan2(-1, -1)" é "-3*pi/4".

math.cos(x)

   Retorna o cosseno de *x* radianos.

math.sin(x)

   Retorna o seno de *x* radianos.

math.tan(x)

   Retorna o tangente de *x* radianos.


Funções hiperbólicas
====================

Funções hiperbólicas são análogas às funções trigonométricas baseadas
em hipérboles em vez de círculos.

math.acosh(x)

   Retorna o cosseno hiperbólico inverso de *x*.

math.asinh(x)

   Retorna o seno hiperbólico inverso de *x*.

math.atanh(x)

   Retorna a tangente hiperbólica inversa de *x*.

math.cosh(x)

   Retorna o cosseno hiperbólico de *x*.

math.sinh(x)

   Retorna o seno hiperbólico de *x*.

math.tanh(x)

   Retorna a tangente hiperbólica de *x*.


Funções especiais
=================

math.erf(x)

   Retorna a função erro em *x*.

   A função "erf()" pode ser usada para calcular funções estatísticas
   tradicionais, como a distribuição normal padrão cumulativa:

      def phi(x):
          'Função de distribuição cumulativa para a distribuição normal padrão.'
          return (1.0 + erf(x / sqrt(2.0))) / 2.0

   Adicionado na versão 3.2.

math.erfc(x)

   Retorna a função erro complementar em *x*. A função erro
   complementar é definida como "1.0 - erf(x)". É usado para grandes
   valores de *x* onde uma subtração de um causaria uma perda de
   significância.

   Adicionado na versão 3.2.

math.gamma(x)

   Retorna a função gama em *x*.

   Adicionado na versão 3.2.

math.lgamma(x)

   Retorna o logaritmo natural do valor absoluto da função gama em
   *x*.

   Adicionado na versão 3.2.


Funções de teoria dos números
=============================

Para retrocompatibilidade, o módulo "math" também fornece apelidos
para as seguintes funções do módulo "math.integer":

+----------------------------------------------------+----------------------------------------------------+
| "comb(n, k)"                                       | Número de maneiras de escolher *k* itens a partir  |
|                                                    | de *n* itens sem repetição e sem ordem             |
+----------------------------------------------------+----------------------------------------------------+
| "factorial(n)"                                     | Fatorial de *n*                                    |
+----------------------------------------------------+----------------------------------------------------+
| "gcd(*integers)"                                   | Máximo divisor comum dos argumentos inteiros       |
+----------------------------------------------------+----------------------------------------------------+
| "isqrt(n)"                                         | Raiz quadrada inteira de um inteiro não negativo   |
|                                                    | *n*                                                |
+----------------------------------------------------+----------------------------------------------------+
| "lcm(*integers)"                                   | Mínimo múltiplo comum dos argumentos inteiros      |
+----------------------------------------------------+----------------------------------------------------+
| "perm(n, k)"                                       | Número de maneiras de escolher *k* itens de *n*    |
|                                                    | itens sem repetição e com ordem                    |
+----------------------------------------------------+----------------------------------------------------+

Adicionado na versão 3.5: A função "gcd()".

Adicionado na versão 3.8: As funções "comb()", "perm()" e "isqrt()".

Adicionado na versão 3.9: A função "lcm()".

Alterado na versão 3.9: Adicionado suporte para um número arbitrário
de argumentos na função "gcd()". Anteriormente, apenas dois argumentos
eram suportados.

Alterado na versão 3.10: Números de ponto flutuante com valor integral
(como "5.0") não são mais aceitos na função "factorial()".

Suavemente descontinuado desde a versão 3.15: Usa as funções de
"math.integer" ao invés desses apelidos.


Constantes
==========

math.pi

   A constante matemática *π* = 3.141592..., para a precisão
   disponível.

math.e

   A constante matemática *e* = 2.718281..., para a precisão
   disponível.

math.tau

   A constante matemática *τ* = 6.283185..., para a precisão
   disponível. Tau é uma constante de círculo igual a 2*π*, a razão
   entre a circunferência de um círculo e seu raio. Para saber mais
   sobre Tau, confira o vídeo Pi is (still) Wrong de Vi Hart, e comece
   a comemorar o dia do Tau comendo duas vezes mais torta!

   Adicionado na versão 3.6.

math.inf

   Um infinito positivo de ponto flutuante. (Para infinito negativo,
   use "-math.inf".) Equivalente à saída de "float('inf')".

   Adicionado na versão 3.5.

math.nan

   Um valor de ponto flutuante "não é um número" (NaN). Equivalente à
   saída de "float('nan')". Devido aos requisitos do padrão IEEE-754,
   "math.nan" e "float('nan')" não são considerados para ser igual a
   qualquer outro valor numérico, incluindo eles próprios. Para
   verificar se um número é NaN, use a função "isnan()" para testar
   NaNs em vez de "is" ou "==". Exemplo:

   >>> import math
   >>> math.nan == math.nan
   False
   >>> float('nan') == float('nan')
   False
   >>> math.isnan(math.nan)
   True
   >>> math.isnan(float('nan'))
   True

   Adicionado na versão 3.5.

   Alterado na versão 3.11: Agora está sempre disponível

O módulo "math" consiste principalmente em invólucros finos em torno
das funções da biblioteca matemática C da plataforma. O comportamento
em casos excepcionais segue o Anexo F da norma C99 quando apropriado.
A implementação atual levantará "ValueError" para operações inválidas
como "sqrt(-1.0)" ou "log(0.0)" (onde C99 Anexo F recomenda sinalizar
operação inválida ou divisão por zero), e "OverflowError" para
resultados que estouram (por exemplo, "exp(1000.0)"). Um NaN não será
retornado de nenhuma das funções acima, a menos que um ou mais dos
argumentos de entrada sejam um NaN; nesse caso, a maioria das funções
retornará um NaN, mas (novamente seguindo C99 Anexo F) há algumas
exceções a esta regra, por exemplo, "pow(float('nan'), 0.0)" ou
"hypot(float('nan'), float('inf'))".

Observe que o Python não faz nenhum esforço para distinguir NaNs de
sinalização de NaNs silenciosos, e o comportamento para NaNs de
sinalização permanece não especificado. O comportamento típico é
tratar todos os NaNs como se estivessem quietos.

Ver também:

  Módulo "cmath"
     Versões de números complexos de muitas dessas funções.

  Módulo "math.integer"
     Funções matemáticas específicas para inteiro.
