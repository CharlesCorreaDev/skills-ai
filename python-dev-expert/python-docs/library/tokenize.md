"tokenize" --- Tokenizador para código-fonte Python
***************************************************

**Código-fonte:** Lib/tokenize.py

======================================================================

The "tokenize" module provides a lexical scanner for Python source
code, implemented in Python.  The scanner in this module returns
comments as tokens as well, making it useful for implementing "pretty-
printers", including colorizers for on-screen displays.

To simplify token stream handling, all operator and delimiter tokens
and "Ellipsis" are returned using the generic "OP" token type. The
"TokenInfo.exact_type" property gives the exact token type.

Aviso:

  Observe que as funções neste módulo são projetadas apenas para
  analisar código Python sintaticamente válido (código que não levanta
  exceção quando analisado usando "ast.parse()"). O comportamento das
  funções neste módulo é **indefinido** ao fornecer código Python
  inválido e pode mudar a qualquer momento.


Tokenizing input
================

O ponto de entrada principal é um *gerador*:

tokenize.tokenize(readline)

   O gerador "tokenize()" requer um argumento, *readline*, que deve
   ser um objeto chamável que fornece a mesma interface que o método
   "io.IOBase.readline()" de objetos arquivo. Cada chamada para a
   função deve retornar uma linha de entrada como bytes.

   The generator produces "TokenInfo" objects.

   Alterado na versão 3.1: Changed to yield "TokenInfo" objects
   instead of plain tuples.

   "tokenize()" determina a codificação de origem do arquivo
   procurando por um BOM UTF-8 ou cookie de codificação, de acordo com
   **PEP 263**.

tokenize.generate_tokens(readline)

   Tokeniza uma fonte lendo strings unicode em vez de bytes.

   Assim como "tokenize()", o argumento *readline* é um chamável que
   retorna uma única linha de entrada. No entanto, "generate_tokens()"
   espera que *readline* retorne um objeto str em vez de bytes.

   The result is an iterator yielding "TokenInfo" objects, exactly
   like "tokenize()". It does not yield an "ENCODING" token.

class tokenize.TokenInfo(type, string, start, end, line)

   A *named tuple* describing a token. It has five fields and an
   additional "exact_type" property.

   Adicionado na versão 3.1.

   type

      An integer identifying the token type, as defined by the
      constants in "token", such as "NAME" and "STRING". Operators and
      delimiters have type "OP"; use "exact_type" for their specific
      token type.

   string

      The token text as a "str". For "STRING" tokens, this includes
      the quotes, any prefix, and escape sequences, without evaluating
      them.

      For an "ENCODING" token, this is the encoding name. Tokens
      inserted without corresponding source text can have an empty
      string. In "FSTRING_MIDDLE" and "TSTRING_MIDDLE" tokens, doubled
      braces are replaced by single braces.

   start

      A 2-tuple "(srow, scol)" of ints specifying the inclusive start
      position of the token in the source. Rows are numbered from 1
      and columns from 0. Columns count Unicode code points; a tab
      counts as one column, without expanding it to a tab stop.

      For an "ENCODING" token, this is "(0, 0)".

   end

      A 2-tuple "(erow, ecol)" of ints specifying the exclusive end
      position of the token. Rows are numbered from 1 and columns from
      0. For a token spanning multiple lines, *erow* is the final row
      and *ecol* is the column on that row.

      For example, the name "spam" at the beginning of the first line
      has "start" equal to "(1, 0)" and "end" equal to "(1, 4)".

      For an "ENCODING" token, this is "(0, 0)". A "NEWLINE" or "NL"
      token inserted at the end of input without a final newline can
      have an end column one beyond the source text.

   line

      A "str" containing the full source line on which the token was
      found, including surrounding text and the line terminator if
      present. For a token spanning multiple lines, this can contain
      several source lines. It is empty for "ENCODING" and "ENDMARKER"
      tokens.

   exact_type

      An integer identifying the specific operator type for "OP"
      tokens, as defined by the constants in "token". For all other
      token types, this equals "type". For example, a "+" token has
      "type" equal to "OP" and "exact_type" equal to "PLUS".

      Adicionado na versão 3.3.

All constants from the "token" module are also exported from
"tokenize".

Outra função é fornecida para reverter o processo de tokenização. Isso
é útil para criar ferramentas que tokenizam um script, modificam o
fluxo de tokens e escrevem de volta o script modificado.

tokenize.untokenize(iterable)

   Converte tokens de volta para o código-fonte Python. O *iterable*
   deve retornar sequências com pelo menos dois elementos, o tipo de
   token e a string do token. Quaisquer elementos de sequência
   adicionais são ignorados.

   O resultado é garantido para tokenizar de volta para corresponder à
   entrada, de modo que a conversão seja sem perdas e as viagens de
   ida e volta sejam garantidas. A garantia se aplica somente ao tipo
   de token e à sequência de tokens, pois o espaçamento entre os
   tokens (posições de coluna) pode mudar.

   Retorna bytes, codificados usando o token "ENCODING", que é a
   primeira sequência de tokens gerada por "tokenize()". Se não houver
   nenhum token de codificação na entrada, ele retorna um str em vez
   disso.

"tokenize()" precisa detectar a codificação dos arquivos fonte que ele
tokeniza. A função que ele usa para fazer isso está disponível:

tokenize.detect_encoding(readline)

   A função "detect_encoding()" é usada para detectar a codificação
   que deve ser usada para decodificar um arquivo de origem Python.
   Ela requer um argumento, readline, da mesma forma que o gerador
   "tokenize()".

   Ele chamará readline no máximo duas vezes e retornará a codificação
   usada (como uma string) e uma lista de todas as linhas (não
   decodificadas de bytes) que ele leu.

   Ele detecta a codificação a partir da presença de um BOM UTF-8 ou
   um cookie de codificação conforme especificado em **PEP 263**. Se
   um BOM e um cookie estiverem presentes, mas discordarem, uma
   exceção "SyntaxError" será levantada. Observe que se o BOM for
   encontrado, "'utf-8-sig'" será retornado como uma codificação.

   Se nenhuma codificação for especificada, o padrão "'utf-8'" será
   retornado.

   Use "open()" para abrir arquivos de código-fonte Python: ele usa
   "detect_encoding()" para detectar a codificação do arquivo.

tokenize.open(filename)

   Abre um arquivo no modo somente leitura usando a codificação
   detectada por "detect_encoding()".

   Adicionado na versão 3.2.

exception tokenize.TokenError

   Levantada quando uma docstring ou expressão que pode ser dividida
   em várias linhas não é concluída em nenhum lugar do arquivo, por
   exemplo:

      """Início da
      docstring

   ou:

      [1,
       2,
       3


Uso na linha de comando
=======================

Adicionado na versão 3.3.

The "tokenize" module can be executed as a script from the command
line. It is as simple as:

   python -m tokenize [-e] [nome-do-arquivo.py]

As seguintes opções são aceitas:

-h, --help

   mostra esta mensagem de ajuda e sai

-e, --exact

   exibe nomes de tokens usando o tipo exato

Se "nome-de-arquivo.py" for especificado, seu conteúdo será tokenizado
para stdout. Caso contrário, a tokenização será realizada em stdin.

Adicionado na versão 3.15: A saída é colorida por padrão e ela pode
ser controlada usando variáveis de ambiente.


Exemplos
========

Exemplo de um reescritor de script que transforma literais float em
objetos Decimal:

   from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
   from io import BytesIO

   def decistmt(s):
       """Substitui Decimals por floats em uma string de instruções.

       >>> from decimal import Decimal
       >>> s = 'print(+21.3e-5*-.1234/81.7)'
       >>> decistmt(s)
       "print (+Decimal ('21.3e-5')*-Decimal ('.1234')/Decimal ('81.7'))"

       O formato do expoente é herdado da biblioteca da plataforma C. Casos
       conhecidos são "e-007" (Windows) e "e-07" (não Windows). Como estamos
       mostrando apenas 12 dígitos, e o 13º não está próximo de 5, o restante
       da saída deve ser independente da plataforma.

       >>> exec(s)  #doctest: +ELLIPSIS
       -3.21716034272e-0...7

       A saída dos cálculos com Decimal deve ser idêntica em todas as
       plataformas.

       >>> exec(decistmt(s))
       -3.217160342717258261933904529E-7
       """
       result = []
       g = tokenize(BytesIO(s.encode('utf-8')).readline)  # tokenize the string
       for toknum, tokval, _, _, _ in g:
           if toknum == NUMBER and '.' in tokval:  # replace NUMBER tokens
               result.extend([
                   (NAME, 'Decimal'),
                   (OP, '('),
                   (STRING, repr(tokval)),
                   (OP, ')')
               ])
           else:
               result.append((toknum, tokval))
       return untokenize(result).decode('utf-8')

Exemplo de tokenização a partir da linha de comando. O script:

   def say_hello():
       print("Hello, World!")

   say_hello()

will be tokenized to the following output where the first column is
the range of the line/column coordinates where the token is found, the
second column is the name of the token, and the final column is the
value of the token (if any):

   $ python -m tokenize hello.py
   0,0-0,0:            ENCODING       'utf-8'
   1,0-1,3:            NAME           'def'
   1,4-1,13:           NAME           'say_hello'
   1,13-1,14:          OP             '('
   1,14-1,15:          OP             ')'
   1,15-1,16:          OP             ':'
   1,16-1,17:          NEWLINE        '\n'
   2,0-2,4:            INDENT         '    '
   2,4-2,9:            NAME           'print'
   2,9-2,10:           OP             '('
   2,10-2,25:          STRING         '"Hello, World!"'
   2,25-2,26:          OP             ')'
   2,26-2,27:          NEWLINE        '\n'
   3,0-3,1:            NL             '\n'
   4,0-4,0:            DEDENT         ''
   4,0-4,9:            NAME           'say_hello'
   4,9-4,10:           OP             '('
   4,10-4,11:          OP             ')'
   4,11-4,12:          NEWLINE        '\n'
   5,0-5,0:            ENDMARKER      ''

Os nomes exatos dos tipos de token podem ser exibidos usando a opção
"-e":

   $ python -m tokenize -e hello.py
   0,0-0,0:            ENCODING       'utf-8'
   1,0-1,3:            NAME           'def'
   1,4-1,13:           NAME           'say_hello'
   1,13-1,14:          LPAR           '('
   1,14-1,15:          RPAR           ')'
   1,15-1,16:          COLON          ':'
   1,16-1,17:          NEWLINE        '\n'
   2,0-2,4:            INDENT         '    '
   2,4-2,9:            NAME           'print'
   2,9-2,10:           LPAR           '('
   2,10-2,25:          STRING         '"Hello, World!"'
   2,25-2,26:          RPAR           ')'
   2,26-2,27:          NEWLINE        '\n'
   3,0-3,1:            NL             '\n'
   4,0-4,0:            DEDENT         ''
   4,0-4,9:            NAME           'say_hello'
   4,9-4,10:           LPAR           '('
   4,10-4,11:          RPAR           ')'
   4,11-4,12:          NEWLINE        '\n'
   5,0-5,0:            ENDMARKER      ''

Exemplo de tokenização de um arquivo programaticamente, lendo strings
unicode em vez de bytes com "generate_tokens()":

   import tokenize

   with tokenize.open('hello.py') as f:
       tokens = tokenize.generate_tokens(f.readline)
       for token in tokens:
           print(token)

Ou lendo bytes diretamente com "tokenize()":

   import tokenize

   with open('hello.py', 'rb') as f:
       tokens = tokenize.tokenize(f.readline)
       for token in tokens:
           print(token)
