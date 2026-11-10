"glob" --- Expansão de padrão de nome de arquivo no estilo Unix
***************************************************************

**Código-fonte:** Lib/glob.py

======================================================================

O módulo "glob" encontra caminhos usando regras de correspondência de
padrões semelhante a do shell Unix. Nenhuma expansão de til é feita,
mas "*", "?" e os intervalos de caracteres expressos com "[]" serão
correspondidos corretamente. Isso é feito usando as funções
"os.scandir()" e "fnmatch.fnmatch()" em conjunto, e não invocando
realmente um subshell.

Nota:

  Os caminhos são retornados sem uma ordem específica. Se precisar de
  uma ordem específica, classifique os resultados.

By default, files beginning with a dot (".") can only be matched by
patterns that also start with a dot, unlike "fnmatch.fnmatch()" or
"pathlib.Path.glob()". For tilde and shell variable expansion, use
"os.path.expanduser()" and "os.path.expandvars()".

Para uma correspondência literal, coloque os metacaracteres entre
colchetes. Por exemplo, "'[?]'" corresponde ao caractere "'?'".

O módulo "glob" define as seguintes funções:

glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)

   Retorna uma lista possivelmente vazia de nomes de caminho que
   correspondem a *pathname*, que deve ser uma string contendo uma
   especificação de caminho. *pathname* pode ser absoluto (como
   "/usr/src/Python-1.5/Makefile") ou relativo (como
   "../../Tools/*/*.gif") e pode conter curingas no estilo shell.
   Links simbólicos quebrados são incluídos nos resultados (como no
   shell). Se os resultados são classificados ou não depende do
   sistema de arquivos. Se um arquivo que satisfaz as condições for
   removido ou adicionado durante a chamada desta função, não é
   especificado se um nome de caminho para esse arquivo será incluído.

   Se *root_dir* não for "None", deve ser um *objeto caminho ou
   similar* especificando o diretório raiz para pesquisa. Tem o mesmo
   efeito em "glob()" que alterar o diretório atual antes de chamá-lo.
   Se *pathname* for relativo, o resultado conterá caminhos relativos
   a *root_dir*.

   Esta função oferece suporte para caminhos relativos aos descritores
   de diretório com o parâmetro *dir_fd*.

   Se *recursive* for verdadeiro, o padrão ""**"" corresponderá a
   qualquer arquivo e zero ou mais diretórios, subdiretórios e links
   simbólicos para diretórios. Se o padrão for seguido por um "os.sep"
   ou "os.altsep", então os arquivos não irão corresponder.

   If *include_hidden* is true, wildcards can match path segments that
   begin with a dot (".").

   Levanta um evento de auditoria "glob.glob" com os argumentos
   "pathname", "recursive".

   Levanta um evento de auditoria "glob.glob/2" com os argumentos
   "pathname", "recursive", "root_dir", "dir_fd".

   Nota:

     Usar o padrão ""**"" em grandes árvores de diretório pode
     consumir uma quantidade excessiva de tempo.

   Nota:

     Esta função pode retornar nomes de caminhos duplicados se
     *pathname* contiver vários padrões ""**"" e *recursive* for
     verdadeiro.

   Nota:

     Qualquer exceção "OSError" levantada durante a varredura do
     sistema de arquivos é ignorada. Isso inclui "PermissionError" ao
     acessar diretórios sem permissão de leitura.

   Alterado na versão 3.5: Suporte a globs recursivos usando ""**"".

   Alterado na versão 3.10: Adicionados os parâmetros *root_dir* e
   *dir_fd*.

   Alterado na versão 3.11: Adicionado o parâmetro *include_hidden*.

glob.iglob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)

   Return an *iterator* which yields the same values as "glob()"
   without actually storing them all simultaneously.

   Levanta um evento de auditoria "glob.glob" com os argumentos
   "pathname", "recursive".

   Levanta um evento de auditoria "glob.glob/2" com os argumentos
   "pathname", "recursive", "root_dir", "dir_fd".

   Nota:

     Esta função pode retornar nomes de caminhos duplicados se
     *pathname* contiver vários padrões ""**"" e *recursive* for
     verdadeiro.

   Nota:

     Qualquer exceção "OSError" levantada durante a varredura do
     sistema de arquivos é ignorada. Isso inclui "PermissionError" ao
     acessar diretórios sem permissão de leitura.

   Alterado na versão 3.5: Suporte a globs recursivos usando ""**"".

   Alterado na versão 3.10: Adicionados os parâmetros *root_dir* e
   *dir_fd*.

   Alterado na versão 3.11: Adicionado o parâmetro *include_hidden*.

glob.escape(pathname)

   Escape all special characters ("'?'", "'*'" and "'['"). This is
   useful if you want to match an arbitrary literal string that may
   have special characters in it.  Special characters in drive/UNC
   sharepoints are not escaped, for example on Windows
   "escape('//?/c:/Quo vadis?.txt')" returns "'//?/c:/Quo
   vadis[?].txt'".

   Adicionado na versão 3.4.

glob.translate(pathname, *, recursive=False, include_hidden=False, seps=None)

   Convert the given path specification to a regular expression for
   use with "re.prefixmatch()". The path specification can contain
   shell-style wildcards.

   Por exemplo:

   >>> import glob, re
   >>>
   >>> regex = glob.translate('**/*.txt', recursive=True, include_hidden=True)
   >>> regex
   '(?s:(?:.+/)?[^/]*\\.txt)\\z'
   >>> reobj = re.compile(regex)
   >>> reobj.prefixmatch('foo/bar/baz.txt')
   <re.Match object; span=(0, 15), match='foo/bar/baz.txt'>

   Separadores de caminho e segmentos são significativos para esta
   função, diferentemente de "fnmatch.translate()". Por padrão,
   curingas não correspondem a separadores de caminho, e segmentos de
   padrão "*" correspondem precisamente a um segmento de caminho.

   Se *recursive* for verdadeiro, o segmento de padrão ""**""
   corresponderá a qualquer número de segmentos de caminho.

   Se *include_hidden* for verdadeiro, os curingas poderão
   corresponder a segmentos de caminho que começam com um ponto (".").

   Uma sequência de separadores de caminho pode ser fornecida ao
   argumento *seps*. Se não for fornecido, "os.sep" e "altsep" (se
   disponível) são usados.

   Ver também:

     Os métodos "pathlib.PurePath.full_match()" e
     "pathlib.Path.glob()", que chamam esta função para implementar
     correspondência de padrões e globbing.

   Adicionado na versão 3.13.


Exemplos
========

Consider a directory containing the following files: "1.gif", "2.txt",
"card.gif" and a subdirectory "sub" which contains only the file
"3.txt".  "glob()" will produce the following results.  Notice how any
leading components of the path are preserved.

   >>> import glob
   >>> glob.glob('./[0-9].*')
   ['./1.gif', './2.txt']
   >>> glob.glob('*.gif')
   ['1.gif', 'card.gif']
   >>> glob.glob('?.gif')
   ['1.gif']
   >>> glob.glob('**/*.txt', recursive=True)
   ['2.txt', 'sub/3.txt']
   >>> glob.glob('./**/', recursive=True)
   ['./', './sub/']

Se o diretório contém arquivos começando com "." eles não serão
correspondidos por padrão. Por exemplo, considere um diretório
contendo "card.gif" e ".card.gif"

   >>> import glob
   >>> glob.glob('*.gif')
   ['card.gif']
   >>> glob.glob('.c*')
   ['.card.gif']

Ver também:

  O módulo "fnmatch" oferece expansão de nome de arquivo (não caminho)
  no estilo shell.

Ver também:

  O módulo "pathlib" oferece objetos de caminho de alto nível.
