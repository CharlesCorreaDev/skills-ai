"__future__" --- Definições de instruções future
************************************************

**Código-fonte:** Lib/__future__.py

======================================================================

Instruções do tipo "from __future__ import feature" são chamadas de
instruções future. Esses são casos especiais do compilador do Python
para permitir o uso de novos recursos do Python em módulos que contêm
a instrução future antes da versão em que o recurso se torna padrão.

Embora o compilador Python dê um significado especial adicional a
essas instruções future, elas ainda são executadas como qualquer outra
instrução de importação. O módulo "__future__" existe e é tratado pelo
sistema de importação da mesma forma que qualquer outro módulo Python.
Isso serve a três propósitos:

* Para evitar confundir as ferramentas existentes que analisam as
  instruções de importação e esperam encontrar os módulos  sendo
  importados.

* Para documentar quando as mudanças incompatíveis foram introduzidas
  e quando elas serão --- ou foram --- obrigatórias. Esta é uma forma
  de documentação executável e pode ser inspecionada programaticamente
  por meio da importação "__future__" e da análise de seus conteúdos.

* Para garantir que instruções future sejam executadas em versões
  anteriores a Python 2.1, pelo menos, processe exceções de tempo de
  execução (a importação de "__future__" falhará, porque não havia
  nenhum módulo com esse nome antes de 2.1).


Conteúdo do módulo
==================

Nenhuma descrição de característica será excluída de "__future__".
Desde a sua introdução no Python 2.1, os seguintes recursos
encontraram o caminho para o idioma usando esse mecanismo:

+---------------------------+---------------------------+---------------------------+---------------------------+
| característica            | opcional em               | obrigatório em            | efeito                    |
|===========================|===========================|===========================|===========================|
| __future__.nested_scopes  | 2.1.0b1                   | 2.2                       | **PEP 227**: *Statically  |
|                           |                           |                           | Nested Scopes*            |
+---------------------------+---------------------------+---------------------------+---------------------------+
| __future__.generators     | 2.2.0a1                   | 2.3                       | **PEP 255**: *Simple      |
|                           |                           |                           | Generators*               |
+---------------------------+---------------------------+---------------------------+---------------------------+
| __future__.division       | 2.2.0a2                   | 3.0                       | **PEP 238**: *Changing    |
|                           |                           |                           | the Division Operator*    |
+---------------------------+---------------------------+---------------------------+---------------------------+
| __future__.absolute_impo  | 2.5.0a1                   | 3.0                       | **PEP 328**: *Imports:    |
| rt                        |                           |                           | Multi-Line and            |
|                           |                           |                           | Absolute/Relative*        |
+---------------------------+---------------------------+---------------------------+---------------------------+
| __future__.with_statement | 2.5.0a1                   | 2.6                       | **PEP 343**: *The “with”  |
|                           |                           |                           | Statement*                |
+---------------------------+---------------------------+---------------------------+---------------------------+
| __future__.print_function | 2.6.0a2                   | 3.0                       | **PEP 3105**: *Make print |
|                           |                           |                           | a function*               |
+---------------------------+---------------------------+---------------------------+---------------------------+
| __future__.unicode_liter  | 2.6.0a2                   | 3.0                       | **PEP 3112**: *Bytes      |
| als                       |                           |                           | literals in Python 3000*  |
+---------------------------+---------------------------+---------------------------+---------------------------+
| __future__.generator_stop | 3.5.0b1                   | 3.7                       | **PEP 479**:              |
|                           |                           |                           | *StopIteration handling   |
|                           |                           |                           | inside generators*        |
+---------------------------+---------------------------+---------------------------+---------------------------+
| __future__.annotations    | 3.7.0b1                   | Nunca [1]                 | **PEP 563**: *Avaliação   |
|                           |                           |                           | adiada de anotações*,     |
|                           |                           |                           | **PEP 649**: *Avaliação   |
|                           |                           |                           | diferida de anotações     |
|                           |                           |                           | usando descritores*       |
+---------------------------+---------------------------+---------------------------+---------------------------+

class __future__._Feature

   Cada instrução em "__future__.py" é da forma:

      FeatureName = _Feature(OptionalRelease, MandatoryRelease,
                             CompilerFlag)

   Onde, normalmente, *OptionalRelease* é inferior a
   *MandatoryRelease*, e ambos são tuplas de 5 entradas da mesma forma
   que "sys.version_info":

      (PY_MAJOR_VERSION, # o 2 em 2.1.0a3; um int
       PY_MINOR_VERSION, # o 1; um int
       PY_MICRO_VERSION, # o 0; um int
       PY_RELEASE_LEVEL, # "alpha", "beta", "candidate" ou "final"; uma string
       PY_RELEASE_SERIAL # o 3; um int
      )

_Feature.getOptionalRelease()

   *OptionalRelease* registra o primeiro lançamento no qual o recurso
   foi aceito.

_Feature.getMandatoryRelease()

   No caso de um *MandatoryRelease* que ainda não ocorreu,
   *MandatoryRelease* prevê o lançamento em que o recurso se tornará
   parte da linguagem.

   Senão *MandatoryRelease* registra quando o recurso se tornou parte
   do idioma; Em versões em ou depois disso, os módulos não precisam
   mais de uma instrução future para usar o recurso em questão, mas
   podem continuar a usar essas importações.

   *MandatoryRelease* também pode ser "None", o que significa que uma
   característica planejada foi descartada ou que isso ainda não está
   decidido.

_Feature.compiler_flag

   *CompilerFlag* é o sinalizador (bitfield) que deve ser passado no
   quarto argumento para a função embutida "compile()" para habilitar
   o recurso no código compilado dinamicamente. Este sinalizador é
   armazenado no atributo "_Feature.compiler_flag" em instâncias de
   "_Feature".

[1] "from __future__ import annotations" estava programado para se
    tornar obrigatório no Python 3.10, mas a alteração foi adiada e,
    por fim, cancelada. Este recurso será eventualmente descontinuado
    e removido. Veja **PEP 649** e **PEP 749**.

Ver também:

  Instruções future
     Como o compilador trata as importações de future.

  **PEP 236** - De volta ao __future__
     A proposta original para o mecanismo do __future__.
