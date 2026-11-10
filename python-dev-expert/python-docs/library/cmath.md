"cmath" --- Funções matemáticas para números complexos
******************************************************

======================================================================

Este módulo fornece acesso a funções matemáticas para números
complexos. As funções neste módulo aceitam inteiros, números de ponto
flutuante ou números complexos como argumentos. Eles também aceitarão
qualquer objeto Python que tenha um método "__complex__()" ou
"__float__()": esses métodos são usados para converter o objeto em um
número complexo ou de ponto flutuante, respectivamente, e a função é
então aplicada ao resultado da conversão.

Nota:

  Para funções que envolvem cortes de ramificação, temos o problema de
  decidir como definir essas funções no próprio corte. Seguindo o
  artigo de Kahan intitulado "Branch cuts for complex elementary
  functions" (em tradução livre, "Cortes de ramificação para funções
  complexas elementares"), bem como o Anexo G do C99 e padrões C
  posteriores, usamos o sinal de zero para distinguir um lado do outro
  no corte de ramificação: para um corte de ramificação ao longo (de
  uma porção) do eixo real olhamos para o sinal da parte imaginária,
  enquanto para um corte de ramificação ao longo do eixo imaginário
  olhamos para o sinal da parte real.Por exemplo, a função
  "cmath.sqrt()" tem um corte de ramificação ao longo do eixo real
  negativo. Um argumento de "-2-0j" é tratado como se estivesse
  *abaixo* do corte de ramificação, e assim dá um resultado no eixo
  imaginário negativo:

     >>> cmath.sqrt(-2-0j)
     -1.4142135623730951j

  Mas um argumento de "-2+0j" é tratado como se estivesse acima do
  corte de ramificação:

     >>> cmath.sqrt(-2+0j)
     1.4142135623730951j

+------------------------------------------------------+--------------------------------------------------------------------+
| **Conversões de e para coordenadas polares**                                                                              |
+------------------------------------------------------+--------------------------------------------------------------------+
| "phase(z)"                                           | Retorna a fase de *z*                                              |
+------------------------------------------------------+--------------------------------------------------------------------+
| "polar(z)"                                           | Retorna a representação de *z* em coordenadas polares              |
+------------------------------------------------------+--------------------------------------------------------------------+
| "rect(r, phi)"                                       | Retorna o número complexo *z* com coordenadas polares *r* e *phi*  |
+------------------------------------------------------+--------------------------------------------------------------------+
| **Funções de potência e logarítmicas**                                                                                    |
+------------------------------------------------------+--------------------------------------------------------------------+
| "exp(z)"                                             | Retorna *e* elevado à potência *z*                                 |
+------------------------------------------------------+--------------------------------------------------------------------+
| "log(z[, base])"                                     | Retorna o logaritmo de *z* para a *base* fornecida (*e* por        |
|                                                      | padrão)                                                            |
+------------------------------------------------------+--------------------------------------------------------------------+
| "log10(z)"                                           | Retorna o logaritmo de base 10 de *z*                              |
+------------------------------------------------------+--------------------------------------------------------------------+
| "sqrt(z)"                                            | Retorna a raiz quadrada de *z*                                     |
+------------------------------------------------------+--------------------------------------------------------------------+
| **Funções trigonométricas**                                                                                               |
+------------------------------------------------------+--------------------------------------------------------------------+
| "acos(z)"                                            | Retorna o arco cosseno de *z*                                      |
+------------------------------------------------------+--------------------------------------------------------------------+
| "asin(z)"                                            | Retorna o arco seno de *z*                                         |
+------------------------------------------------------+--------------------------------------------------------------------+
| "atan(z)"                                            | Retorna o arco tangente de *z*                                     |
+------------------------------------------------------+--------------------------------------------------------------------+
| "cos(z)"                                             | Retorna o cosseno de *z*                                           |
+------------------------------------------------------+--------------------------------------------------------------------+
| "sin(z)"                                             | Retorna o seno de *z*                                              |
+------------------------------------------------------+--------------------------------------------------------------------+
| "tan(z)"                                             | Retorna a tangente de *z*                                          |
+------------------------------------------------------+--------------------------------------------------------------------+
| **Funções hiperbólicas**                                                                                                  |
+------------------------------------------------------+--------------------------------------------------------------------+
| "acosh(z)"                                           | Retorna o cosseno hiperbólico inverso de *z*                       |
+------------------------------------------------------+--------------------------------------------------------------------+
| "asinh(z)"                                           | Retorna o seno hiperbólico inverso de *z*                          |
+------------------------------------------------------+--------------------------------------------------------------------+
| "atanh(z)"                                           | Retorna a tangente hiperbólica inversa de *z*                      |
+------------------------------------------------------+--------------------------------------------------------------------+
| "cosh(z)"                                            | Retorna o cosseno hiperbólico de *z*                               |
+------------------------------------------------------+--------------------------------------------------------------------+
| "sinh(z)"                                            | Retorna o seno hiperbólico de *z*                                  |
+------------------------------------------------------+--------------------------------------------------------------------+
| "tanh(z)"                                            | Retorna a tangente hiperbólica de *z*                              |
+------------------------------------------------------+--------------------------------------------------------------------+
| **Funções de classificação**                                                                                              |
+------------------------------------------------------+--------------------------------------------------------------------+
| "isfinite(z)"                                        | Verifica se todos os componentes de *z* são finitos                |
+------------------------------------------------------+--------------------------------------------------------------------+
| "isinf(z)"                                           | Verifica se algum componente de *z* é infinito                     |
+------------------------------------------------------+--------------------------------------------------------------------+
| "isnan(z)"                                           | Verifica se algum componente de *z* é NaN                          |
+------------------------------------------------------+--------------------------------------------------------------------+
| "isclose(a, b, *, rel_tol, abs_tol)"                 | Verifica se os valores *a* e *b* estão próximos um do outro        |
+------------------------------------------------------+--------------------------------------------------------------------+
| **Constantes**                                                                                                            |
+------------------------------------------------------+--------------------------------------------------------------------+
| "pi"                                                 | *π* = 3.141592...                                                  |
+------------------------------------------------------+--------------------------------------------------------------------+
| "e"                                                  | *e* = 2.718281...                                                  |
+------------------------------------------------------+--------------------------------------------------------------------+
| "tau"                                                | *τ* = 2*π* = 6.283185...                                           |
+------------------------------------------------------+--------------------------------------------------------------------+
| "inf"                                                | Infinito positivo                                                  |
+------------------------------------------------------+--------------------------------------------------------------------+
| "infj"                                               | Infinito imaginário puro                                           |
+------------------------------------------------------+--------------------------------------------------------------------+
| "nan"                                                | "Not a number" (NaN)                                               |
+------------------------------------------------------+--------------------------------------------------------------------+
| "nanj"                                               | NaN imaginário puro                                                |
+------------------------------------------------------+--------------------------------------------------------------------+


Conversões de e para coordenadas polares
========================================

Um número complexo Python "z" é armazenado internamente usando
coordenadas *retangulares* ou *cartesianas*. É completamente
determinado por sua *parte real* "z.real" e sua *parte imaginária*
"z.imag".

*Coordenadas polares* fornecem uma forma alternativa de representar um
número complexo. Em coordenadas polares, um número complexo *z* é
definido pelo módulo *r* e pelo ângulo de fase *phi*. O módulo *r* é a
distância de *z* à origem, enquanto a fase *phi* é o ângulo anti-
horário, medido em radianos, do eixo x positivo ao segmento de reta
que une a origem a *z*.

As funções a seguir podem ser usadas para converter coordenadas
retangulares nativas em coordenadas polares e vice-versa.

cmath.phase(z)

   Retorna a fase de *z* (também conhecido como *argumento* de *z*),
   como um ponto flutuante. "phase(z)" equivale a "math.atan2(z.imag,
   z.real)". O resultado está no intervalo [-*π*, *π*], e o corte de
   ramificação para esta operação está ao longo do eixo real negativo.
   O sinal do resultado é igual ao sinal de "z.imag", mesmo quando
   "z.imag" é zero:

      >>> phase(-1+0j)
      3.141592653589793
      >>> phase(-1-0j)
      -3.141592653589793

Nota:

  O módulo (valor absoluto) de um número complexo *z* pode ser
  calculado usando a função embutida "abs()". Não há função do módulo
  "cmath" separada para esta operação.

cmath.polar(z)

   Retorna a representação de *z* em coordenadas polares. Retorna um
   par "(r, phi)" onde *r* é o módulo de *z* e phi é a fase de *z*.
   "polar(z)" equivale a "(abs(z), phase(z))".

cmath.rect(r, phi)

   Retorna o número complexo *z* com coordenadas polares *r* e *phi*.
   Equivale a "complex(r * math.cos(phi), r * math.sin(phi))".


Funções de potência e logarítmicas
==================================

cmath.exp(z)

   Retorna *e* elevado à potência *z*, onde *e* é a base de logaritmos
   naturais.

cmath.log(z[, base])

   Retorna o logaritmo de *z* para a *base* fornecida. Se a *base* não
   for especificada, retorna o logaritmo natural de *z*. Há um corte
   de ramificação, de 0 ao longo do eixo real negativo até -∞.

cmath.log10(z)

   Retorna o logaritmo de *z* na base 10. Este tem o mesmo corte de
   ramificação que "log()".

cmath.sqrt(z)

   Retorna a raiz quadrada de *z*. Este tem o mesmo corte de
   ramificação que "log()".


Funções trigonométricas
=======================

cmath.acos(z)

   Retorna o arco cosseno de *z*. Existem dois cortes de ramificação:
   um se estende desde 1 ao longo do eixo real até ∞. O outro se
   estende para a esquerda de -1 ao longo do eixo real até -∞.

cmath.asin(z)

   Retorna o arco seno de *z*. Tem os mesmos cortes de ramificação que
   "acos()".

cmath.atan(z)

   Retorna o arco tangente de *z*. Existem dois cortes de ramificação:
   Um se estende de "1j" ao longo do eixo imaginário até "∞j". O outro
   se estende de "-1j" ao longo do eixo imaginário até "-∞j".

cmath.cos(z)

   Retorna o cosseno de *z*.

cmath.sin(z)

   Retorna o seno de *z*.

cmath.tan(z)

   Retorna a tangente de *z*.


Funções hiperbólicas
====================

cmath.acosh(z)

   Retorna o cosseno hiperbólico inverso de *z*. Há um corte de
   ramificação, estendendo-se para a esquerda de 1 ao longo do eixo
   real até -∞.

cmath.asinh(z)

   Retorna o seno hiperbólico inverso de *z*. Existem dois cortes de
   ramificação: Um se estende de "1j" ao longo do eixo imaginário até
   "∞j". O outro se estende de "-1j" ao longo do eixo imaginário até
   "-∞j".

cmath.atanh(z)

   Retorna a tangente hiperbólica inversa de *z*. Existem dois cortes
   de ramificação: Um se estende de "1" ao longo do eixo real até "∞".
   O outro se estende de "-1" ao longo do eixo real até "-∞".

cmath.cosh(z)

   Retorna o cosseno hiperbólico de *z*.

cmath.sinh(z)

   Retorna o seno hiperbólico de *z*.

cmath.tanh(z)

   Retorna a tangente hiperbólica de *z*.


Funções de classificação
========================

cmath.isfinite(z)

   Retorna "True" se ambas as partes real e imaginária de *z* forem
   finitas, e "False" caso contrário.

   Adicionado na versão 3.2.

cmath.isinf(z)

   Retorna "True" se ou a parte real ou a imaginária de *z* for
   infinita, e "False" caso contrário.

cmath.isnan(z)

   Retorna "True" se ou a parte real ou a imaginária de *z* for NaN, e
   "False" caso contrário.

cmath.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

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
   e rel_tol menor que "1.0". Então adicione um argumento abs_tol
   positivo apropriado à chamada.

   Os valores especiais do IEEE 754 de "NaN", "inf" e "-inf" serão
   tratados de acordo com as regras do IEEE. Especificamente, "NaN"
   não é considerado próximo a qualquer outro valor, incluindo "NaN".
   "inf" e "-inf" são considerados apenas próximos a si mesmos.

   Adicionado na versão 3.5.

   Ver também:

     **PEP 485** -- Uma função para testar igualdade aproximada


Constantes
==========

cmath.pi

   A constante matemática *π*, como um ponto flutuante.

cmath.e

   A constante matemática *e*, como um ponto flutuante.

cmath.tau

   A constante matemática *τ*, como um ponto flutuante.

   Adicionado na versão 3.6.

cmath.inf

   Infinito positivo de ponto flutuante. Equivale a "float('inf')".

   Adicionado na versão 3.6.

cmath.infj

   Número complexo com parte real zero e parte imaginária infinita
   positiva. Equivale a "complex(0.0, float('inf'))".

   Adicionado na versão 3.6.

cmath.nan

   Um valor de ponto flutuante "não um número" (NaN). Equivale a
   "float('nan')". Veja também "math.nan".

   Adicionado na versão 3.6.

cmath.nanj

   Número complexo com parte real zero e parte imaginária NaN.
   Equivale a "complex(0.0, float('nan'))".

   Adicionado na versão 3.6.

Observe que a seleção de funções é semelhante, mas não idêntica,
àquela no módulo "math". A razão para ter dois módulos é que alguns
usuários não estão interessados em números complexos e talvez nem
saibam o que são. Eles preferem que "math.sqrt(-1)" gere uma exceção
do que retorne um número complexo. Observe também que as funções
definidas em "cmath" sempre retornam um número complexo, mesmo que a
resposta possa ser expressa como um número real (nesse caso o número
complexo tem uma parte imaginária de zero).

Uma nota sobre cortes de ramificação: são curvas ao longo das quais a
função dada não é contínua. Eles são um recurso necessário de muitas
funções complexas. Presume-se que se você precisar calcular com
funções complexas, você entenderá sobre cortes de ramificação.
Consulte quase qualquer livro (não muito elementar) sobre variáveis
complexas para obter esclarecimento. Para informações sobre a escolha
adequada dos cortes de ramificação para fins numéricos, uma boa
referência deve ser a seguinte:

Ver também:

  Kahan, W:  Branch cuts for complex elementary functions; or, Much
  ado about nothing's sign bit.  Em Iserles, A. e Powell, M. (eds.),
  The state of the art in numerical analysis. Clarendon Press (1987)
  pp165--211.
