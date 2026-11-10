"fnmatch" --- Correspondência de padrões de nome de arquivo Unix
****************************************************************

**Código-fonte:** Lib/fnmatch.py

======================================================================

Este módulo fornece suporte para curingas no estilo shell do Unix, que
*não* são iguais às expressões regulares (documentadas no módulo
"re"). Os caracteres especiais usados nos curingas no estilo de shell
são:

+--------------+--------------------------------------+
| Padrão       | Significado                          |
|==============|======================================|
| "*"          | corresponde a tudo                   |
+--------------+--------------------------------------+
| "?"          | Corresponde a qualquer caractere     |
|              | único                                |
+--------------+--------------------------------------+
| "[seq]"      | corresponde a qualquer caractere em  |
|              | *seq*                                |
+--------------+--------------------------------------+
| "[!seq]"     | corresponde a qualquer caractere     |
|              | ausente em *seq*                     |
+--------------+--------------------------------------+

Para uma correspondência literal, coloque os metacaracteres entre
colchetes. Por exemplo, "'[?]'" corresponde ao caractere "'?'".

Note que o separador de nome de arquivo ("'/'" no Unix) *não* é
especial para este módulo. Veja o módulo "glob" para expansão do nome
do caminho ("glob" usa "filter()" para corresponder aos segmentos do
nome do caminho). Da mesma forma, os nomes de arquivos que começam com
um ponto final não são especiais para este módulo e são correspondidos
pelos padrões "*" e "?".

A menos que indicado de outra forma, "string de nome de arquivo" e
"string de padrão" referem-se a objetos "str" ou "bytes" codificados
em "ISO-8859-1". Observe que as funções documentadas abaixo não
permitem misturar um padrão "bytes" com um nome de arquivo "str" e
vice-versa.

Finally, note that "@functools.lru_cache" with a *maxsize* of 32768 is
used to cache the (typed) compiled regex patterns in the following
functions: "fnmatch()", "fnmatchcase()", "filter()", "filterfalse()".

fnmatch.fnmatch(name, pat)

   Testa se a string do nome de arquivo *name* corresponde à string de
   padrão *pat*, retornando "True" ou "False". Ambos os parâmetros são
   normalizados em maiúsculas e minúsculas usando
   "os.path.normcase()". "fnmatchcase()" pode ser usado para realizar
   uma comparação com distinção entre maiúsculas e minúsculas,
   independentemente de ser padrão para o sistema operacional.

   Este exemplo vai exibir todos os nomes de arquivos no diretório
   atual com a extensão ".txt":

      import fnmatch
      import os

      for arquivo in os.listdir('.'):
          if fnmatch.fnmatch(arquivo, '*.txt'):
              print(arquivo)

fnmatch.fnmatchcase(name, pat)

   Testa se a string do nome de arquivo *name* corresponde à string de
   padrão *pat*, retornando "True" ou "False"; a comparação diferencia
   maiúsculas de minúsculas e não se aplica a "os.path.normcase()".

fnmatch.filter(names, pat)

   Constrói uma lista a partir daqueles elementos do *iterável* de
   strings de nome de arquivo *names* que correspondem à string de
   padrão *pat*. É o mesmo que "[n for n in names if fnmatch(n,
   pat)]", mas implementado com mais eficiência.

fnmatch.filterfalse(names, pat)

   Constrói uma lista a partir daqueles elementos do *iterável* de
   strings de nome de arquivo *names* que não correspondem à string de
   padrão *pat*. É o mesmo que "[n for n in names if not fnmatch(n,
   pat)]", mas implementado com mais eficiência.

   Adicionado na versão 3.14.

fnmatch.translate(pat)

   Retorna o padrão *pat* no estilo shell convertido em uma expressão
   regular para usar com "re.prefixmatch()". O padrão é esperado ser
   um "str".

   Exemplo:

   >>> import fnmatch, re
   >>>
   >>> regex = fnmatch.translate('*.txt')
   >>> regex
   '(?s:.*\\.txt)\\z'
   >>> reobj = re.compile(regex)
   >>> reobj.prefixmatch('foobar.txt')
   <re.Match object; span=(0, 10), match='foobar.txt'>

Ver também:

  Módulo "glob"
     Expansão de caminho no estilo shell do Unix.
