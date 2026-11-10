"os.path" --- Manipulações comuns de nomes de caminhos
******************************************************

**Código-fonte:** Lib/genericpath.py, Lib/posixpath.py (para POSIX) e
Lib/ntpath.py (para Windows).

======================================================================

Este módulo implementa algumas funções úteis em nomes de caminho. Para
ler ou escrever arquivos veja "open()", e para acessar o sistema de
arquivos veja o módulo "os". Os parâmetros de caminho podem ser
passados como strings, ou bytes, ou qualquer objeto que implemente o
protocolo "os.PathLike".

Ao contrário de um shell Unix, Python não faz nenhuma expansão
*automática* de caminho. Funções como "expanduser()" e "expandvars()"
podem ser invocadas explicitamente quando uma aplicação deseja uma
expansão de caminho no estilo do shell. (Veja também o módulo "glob".)

Ver também:

  O módulo "pathlib" oferece objetos de caminho de alto nível.

Nota:

  Todas essas funções aceitam apenas bytes ou apenas objetos de string
  como seus parâmetros. O resultado é um objeto do mesmo tipo, se um
  caminho ou nome de arquivo for retornado.

Nota:

  Since different operating systems have different path name
  conventions, there are several versions of this module in the
  standard library.  The "os.path" module is always the path module
  suitable for the operating system Python is running on, and
  therefore usable for local paths.  However, you can also import and
  use the individual modules if you want to manipulate a path that is
  *always* in one of the different formats.  They all have the same
  interface:

  * "posixpath" para caminhos no estilo UNIX

  * "ntpath" para caminhos do Windows

Alterado na versão 3.8: "exists()", "lexists()", "isdir()",
"isfile()", "islink()" e "ismount()" agora retornam "False" em vez de
levantar uma exceção para caminhos que contêm caracteres ou bytes não
representáveis no nível de sistema de operacional.

os.path.abspath(path)

   Return a normalized absolutized version of the pathname *path*. On
   most platforms, this is equivalent to calling
   "normpath(join(os.getcwd(), path))".

   On Windows the path is normalized by the operating system,
   therefore the result can differ from "normpath(join(os.getcwd(),
   path))". A drive-relative path is resolved against the current
   directory of the specified drive, and the drive letter is
   capitalized. Trailing dots and spaces are stripped. For example:

      >>> os.path.abspath('c:spam')
      'C:\\Temp\\spam'
      >>> os.path.abspath('c:/temp/spam. . .')
      'c:\\temp\\spam'

   Ver também: "os.path.join()" and "os.path.normpath()".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.basename(path, /)

   Retorna o nome base do caminho *path*. Este é o segundo elemento do
   par retornado pela passagem de *path* para a função "split()".
   Observe que o resultado desta função é diferente do programa Unix
   **basename**; onde **basename** para "'/foo/bar/'" retorna "'bar'",
   a função "basename()" retorna uma string vazia ("''").

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.commonpath(paths)

   Retorna o subcaminho comum mais longo de cada nome de caminho no
   iterável *paths*. Levanta "ValueError" se *paths* contiverem nomes
   de caminho absolutos e relativos, os *paths* estiverem em unidades
   diferentes ou se *paths* estiverem vazios. Ao contrário de
   "commonprefix()", retorna um caminho válido.

   Adicionado na versão 3.5.

   Alterado na versão 3.6: Aceita uma sequência de *objetos caminho ou
   similares*.

   Alterado na versão 3.13: Qualquer iterável agora pode ser passado,
   em vez de apenas sequências.

os.path.commonprefix(list, /)

   Return the longest string prefix (taken character-by-character)
   that is a prefix of all strings in *list*.  If *list* is empty,
   return the empty string ("''").

   Aviso:

     This function may return invalid paths because it works a
     character at a time. If you need a **common path prefix**, then
     the algorithm implemented in this function is not secure. Use
     "commonpath()" for finding a common path prefix.

        >>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
        '/usr/l'

        >>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
        '/usr'

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

   Descontinuado desde a versão 3.15: Deprecated in favor of
   "os.path.commonpath()" for path prefixes. The
   "os.path.commonprefix()" function is being deprecated due to having
   a misleading name and module. The function is not safe to use for
   path prefixes despite being included in a module about path
   manipulation, meaning it is easy to accidentally introduce path
   traversal vulnerabilities into Python programs by using this
   function.

os.path.dirname(path, /)

   Retorna o nome do diretório do nome de caminho *path*. Este é o
   primeiro elemento do par retornado passando *path* para a função
   "split()".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.exists(path)

   Retorna "True" se *path* se referir a um caminho existente ou um
   descritor de arquivo aberto. Retorna "False" para links simbólicos
   quebrados. Em algumas plataformas, esta função pode retornar
   "False" se a permissão não for concedida para executar "os.stat()"
   no arquivo solicitado, mesmo se o *path* existir fisicamente.

   Alterado na versão 3.3: *path* agora pode ser um inteiro: "True" é
   retornado se for um descritor de arquivo aberto, "False" caso
   contrário.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.lexists(path)

   Retorna "True" se *path* se referir a um caminho existente,
   incluindo links simbólicos quebrados. Equivalente a "exists()" em
   plataformas sem "os.lstat()".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.expanduser(path)

   No Unix e no Windows, retorna o argumento com um componente inicial
   de "~" ou "~user" substituído pelo diretório inicial daquele
   usuário *user*.

   No Unix, um "~" no início é substituído pela variável de ambiente
   "HOME" se estiver definida; caso contrário, o diretório pessoal do
   usuário atual é procurado no diretório de senha através do módulo
   embutido "pwd". Um "~user" no início é procurado diretamente no
   diretório de senhas.

   No Windows, "USERPROFILE" será usada se definida; caso contrário,
   uma combinação de "HOMEPATH" e "HOMEDRIVE" será usada. Um "~user"
   inicial é tratado verificando se o último componente do diretório
   home do usuário atual corresponde a "USERNAME", e substituindo-o se
   for o caso.

   Se a expansão falhar ou se o caminho não começar com um til, o
   caminho será retornado inalterado.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

   Alterado na versão 3.8: Não usa mais "HOME" no Windows.

os.path.expandvars(path)

   Retorna o argumento com as variáveis de ambiente expandidas.
   Substrings da forma "$name" ou "${name}" são substituídas pelo
   valor da variável de ambiente *name*. Nomes de variáveis
   malformados e referências a variáveis não existentes permanecem
   inalterados.

   No Windows, expansões "%name%" são suportadas juntamente a "$name"
   e "${name}".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.getatime(path, /)

   Retorna a hora do último acesso de *path*. O valor de retorno é um
   número de ponto flutuante dando o número de segundos desde a Era
   Unix (veja o módulo "time"). Levanta "OSError" se o arquivo não
   existe ou está inacessível.

os.path.getmtime(path, /)

   Retorna a hora da última modificação de *path*. O valor de retorno
   é um número de ponto flutuante dando o número de segundos desde a
   Era Unix (veja o módulo "time"). Levanta "OSError" se o arquivo não
   existe ou está inacessível.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.getctime(path, /)

   Retorna o ctime do sistema que, em alguns sistemas (como Unix) é a
   hora da última alteração de metadados, e, em outros (como Windows),
   é a hora de criação de *path*. O valor de retorno é um número que
   fornece o número de segundos desde a Era Unix (veja o módulo
   "time"). Levanta "OSError" se o arquivo não existe ou está
   inacessível.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.getsize(path, /)

   Retorna o tamanho, em bytes, de *path*. Levanta "OSError" se o
   arquivo não existe ou está inacessível.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.isabs(path, /)

   Retorna "True" se *path* for um nome de caminho absoluto. No Unix,
   isso significa que começa com uma barra, no Windows começa com duas
   (contra)barras ou uma letra de unidade, caractere de dois pontos e
   (contra)barra juntos.

   Ver também: "abspath()"

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

   Alterado na versão 3.13: No Windows, retorna "False" se o caminho
   fornecido começar com exatamente uma (contra)barra.

os.path.isfile(path)

   Retorna "True" se *path* for um arquivo regular "existente". Isso
   segue links simbólicos, então "islink()" e "isfile()" podem ser
   verdadeiros para o mesmo caminho.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.isdir(path, /)

   Retorna "True" se *path* for um diretório "existente". Isso segue
   links simbólicos, então "islink()" e "isdir()" podem ser
   verdadeiros para o mesmo caminho.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.isjunction(path)

   Retorna "True" se *path* se referir a uma entrada de diretório
   "existente" que é uma junção. Sempre retorna "False" se junções não
   forem suportados na plataforma atual.

   Adicionado na versão 3.12.

os.path.islink(path)

   Retorna "True" se *path* se referir a uma entrada de diretório
   "existente" que é um link simbólico. Sempre "False" se links
   simbólicos não forem suportados pelo tempo de execução Python.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.ismount(path)

   Retorna "True" se o nome de caminho *path* for um *ponto de
   montagem*: um ponto em um sistema de arquivos onde um sistema de
   arquivos diferente foi montado. No POSIX, a função verifica se o
   pai de *path*, "*path*/..", está em um dispositivo diferente de
   *path*, ou se "*path*/.." e *path* apontam para o mesmo nó-i no
   mesmo dispositivo -- isso deve detectar pontos de montagem para
   todas as variantes Unix e POSIX. Não é capaz de detectar
   confiavelmente montagens bind no mesmo sistema de arquivos. Em
   sistemas Linux, sempre vai retornar "True" para subvolumes btrfs,
   mesmo se eles não forem pontos de montagem. No Windows, uma raiz de
   letra de unidade e um UNC de compartilhamento são sempre pontos de
   montagem e, para qualquer outro caminho, "GetVolumePathName" é
   chamado para ver se é diferente do caminho de entrada.

   Alterado na versão 3.4: Adicionado suporte para detecção de pontos
   de montagem não raiz no Windows.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.isdevdrive(path)

   Retorna "True" se o nome do caminho *path* estiver localizado em um
   Windows Dev Drive. Um Dev Drive é otimizado para cenários de
   desenvolvedor e oferece desempenho mais rápido para leitura e
   gravação de arquivos. É recomendado para uso em código-fonte,
   diretórios de construção temporários, caches de pacotes e outras
   operações com uso intensivo de ES.

   Pode levantar um erro para um caminho inválido, por exemplo, um sem
   uma unidade reconhecível, mas retorna "False" em plataformas que
   não provêm suporte a Dev Drives. Consulte a documentação do Windows
   para obter informações sobre como habilitar e criar Dev Drives.

   Adicionado na versão 3.12.

   Alterado na versão 3.13: A função já está disponível em todas as
   plataformas, e sempre retornará "False" naquelas que não possuem
   suporte para Dev Drives

os.path.isreserved(path)

   Retorna "True" se *path* for um caminho reservado no sistema atual.

   No Windows, os nomes de arquivos reservados incluem aqueles que
   terminam com espaço ou ponto; aqueles que contêm dois pontos (ou
   seja, fluxos de arquivos como "nome:fluxo"), caracteres curinga (ou
   seja, "'*?"<>'"), encadeamento (pipe) ou caracteres de controle
   ASCII; bem como nomes de dispositivos DOS, como "NUL", "CON",
   "CONIN$", "CONOUT$", "AUX", "PRN", "COM1" e "LPT1".

   Nota:

     Esta função aproxima regras para caminhos reservados na maioria
     dos sistemas Windows. Essas regras mudam com o tempo em diversas
     versões do Windows. Esta função pode ser atualizada em versões
     futuras do Python à medida que as alterações nas regras se
     tornarem amplamente disponíveis.

   Disponibilidade: Windows.

   Adicionado na versão 3.13.

os.path.join(path, /, *paths)

   Join one or more path segments intelligently.  The return value is
   the concatenation of *path* and all members of **paths*, with
   exactly one directory separator following each non-empty part,
   except the last. That is, the result will only end in a separator
   if the last part is either empty or ends in a separator.

   If a segment is an absolute path (which on Windows requires both a
   drive and a root), then all previous segments are ignored and
   joining continues from the absolute path segment. On Linux, for
   example:

      >>> os.path.join('/home/foo', 'bar')
      '/home/foo/bar'
      >>> os.path.join('/home/foo', '/home/bar')
      '/home/bar'

   On Windows, the drive is not reset when a rooted path segment
   (e.g., "r'\foo'") is encountered. If a segment is on a different
   drive or is an absolute path, all previous segments are ignored and
   the drive is reset. For example:

      >>> os.path.join('c:\\', 'foo')
      'c:\\foo'
      >>> os.path.join('c:\\foo', 'd:\\bar')
      'd:\\bar'

   Note that since there is a current directory for each drive,
   "os.path.join("c:", "foo")" represents a path relative to the
   current directory on drive "C:" ("c:foo"), not "c:\foo".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar* para
   *path* e *paths*.

os.path.normcase(path, /)

   Normaliza o estado de letras maiúsculas/minúsculas de um nome de
   caminho. No Windows, converte todos os caracteres do nome do
   caminho em minúsculas e também converte barras normais em barras
   invertidas. Em outros sistemas operacionais, retorna o caminho
   inalterado.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.normpath(path)

   Normaliza um nome de caminho retirando separadores redundantes e
   referências de nível superior para que "A//B", "A/B/", "A/./B" e
   "A/foo/../B" todos se tornem "A/B". Essa manipulação de string pode
   mudar o significado de um caminho que contém links simbólicos. No
   Windows, ele converte barras normais em barras invertidas. Para
   normalizar o estado de letras maiúsculas/minúsculas, use
   "normcase()".

   Nota:

     Em sistemas POSIX, de acordo com IEEE Std 1003.1 2013 Edition;
     4.13 Pathname Resolution, se um nome de caminho começa com
     exatamente duas barras, o primeiro componente após os caracteres
     iniciais pode ser interpretado em um forma definida pela
     implementação, embora mais de dois caracteres iniciais devam ser
     tratados como um único caractere.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.realpath(path, /, *, strict=False)

   Return the canonical path of the specified filename, eliminating
   any symbolic links encountered in the path (if they are supported
   by the operating system). On Windows, this function will also
   resolve MS-DOS (also called 8.3) style names such as "C:\\PROGRA~1"
   to "C:\\Program Files". The returned path uses the case reported by
   the operating system, which can differ from the case of *path*, in
   particular the drive letter is capitalized.

   Por padrão, o caminho é avaliado até o primeiro componente que não
   existe, é um laço de link simbólico ou cuja avaliação levanta
   "OSError". Todos esses componentes são anexados inalterados à parte
   existente do caminho.

   Alguns erros tratados dessa forma incluem "acesso negado", "não é
   um diretório" ou "argumento inválido para função interna". Assim, o
   caminho resultante pode estar ausente ou inacessível, ainda pode
   conter links ou laços e pode passar por diretórios não
   especificados.

   Esse comportamento pode ser modificado por argumentos nomeados:

   If *strict* is "True", the first error encountered when evaluating
   the path is re-raised. In particular, "FileNotFoundError" is raised
   if *path* does not exist, or another "OSError" if it is otherwise
   inaccessible. If *strict* is "ALL_BUT_LAST", the last component of
   the path is allowed to be missing, but all other errors are raised.

   Se *strict* for "os.path.ALLOW_MISSING", erros diferentes de
   "FileNotFoundError" serão levantados novamente (como em
   "strict=True"). Portanto, o caminho retornado não conterá nenhum
   link simbólico, mas o arquivo nomeado e alguns de seus diretórios
   pais podem estar ausentes.

   Nota:

     Esta função emula o procedimento do sistema operacional para
     tornar um caminho canônico, que difere ligeiramente entre o
     Windows e o UNIX  em relação a como links e componentes de
     caminho subsequentes interagem.As APIs do sistema operacional
     tornam os caminhos canônicos conforme necessário, portanto,
     normalmente não é necessário chamar esta função.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

   Alterado na versão 3.8: Links simbólicos e junções agora são
   resolvidos no Windows.

   Alterado na versão 3.10: O parâmetro *strict* foi adicionado.

   Alterado na versão 3.15: The "ALL_BUT_LAST" and "ALLOW_MISSING"
   values for the *strict* parameter was added.

os.path.ALL_BUT_LAST

   Valor especial usado para o argumento *strict* em "realpath()".

   Adicionado na versão 3.15.

os.path.ALLOW_MISSING

   Valor especial usado para o argumento *strict* em "realpath()".

   Adicionado na versão 3.15.

os.path.relpath(path, start=os.curdir)

   Retorna um caminho de arquivo relativo a *caminho* do diretório
   atual ou de um diretório *start* opcional. Este é um cálculo de
   caminho: o sistema de arquivos não é acessado para confirmar a
   existência ou natureza de *path* ou *start*. No Windows,
   "ValueError" é levantada quando *path* e *start* estão em unidades
   diferentes.

   *start* tem como padrão "os.curdir".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.samefile(path1, path2, /)

   Retorna "True" se ambos os argumentos de nome de caminho se referem
   ao mesmo arquivo ou diretório. Isso é determinado pelo número do
   dispositivo e número do nó-i e levanta uma exceção se uma chamada
   "os.stat()" em qualquer um dos caminhos falhar.

   Alterado na versão 3.2: Adicionado suporte ao Windows.

   Alterado na versão 3.4: O Windows agora usa a mesma implementação
   que todas as outras plataformas.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.sameopenfile(fp1, fp2)

   Retorna "True" se os descritores de arquivo *fp1* e *fp2* fazem
   referência ao mesmo arquivo.

   Alterado na versão 3.2: Adicionado suporte ao Windows.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.samestat(stat1, stat2, /)

   Retorna "True" se as tuplas de estatísticas *stat1* e *stat2* fazem
   referência ao mesmo arquivo. Essas estruturas podem ter sido
   retornadas por "os.fstat()", "os.lstat()" ou "os.stat()". Esta
   função implementa a comparação subjacente usada por "samefile()" e
   "sameopenfile()".

   Alterado na versão 3.4: Adicionado suporte ao Windows.

os.path.split(path, /)

   Split the pathname *path* into a pair, "(head, tail)" where *tail*
   is the last pathname component and *head* is everything leading up
   to that.  The *tail* part will never contain a slash; if *path*
   ends in a slash, *tail* will be empty.  If there is no slash in
   *path*, *head* will be empty.  If *path* is empty, both *head* and
   *tail* are empty.  Trailing slashes are stripped from *head* unless
   it is the root (one or more slashes only).  In all cases,
   "join(head, tail)" returns a path to the same location as *path*
   (but the strings may differ).  Also see the functions "join()",
   "dirname()" and "basename()".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.splitdrive(path, /)

   Divide o nome do caminho *path* em um par "(unidade, rabo)" onde
   *unidade* é um ponto de montagem ou uma string vazia. Em sistemas
   que não usam especificações de unidade, *unidade* sempre será a
   string vazia. Em todos os casos, "unidade + rabo" será o mesmo que
   *path*.

   No Windows, divide um nome de caminho em unidade/ponto de
   compartilhamento UNC e caminho relativo.

   Se o caminho contiver uma letra de unidade, a unidade conterá tudo,
   incluindo os dois pontos:

      >>> splitdrive("c:/dir")
      ("c:", "/dir")

   Se o caminho contiver um caminho UNC, a unidade conterá o nome do
   host e o compartilhamento:

      >>> splitdrive("//host/computador/diretório")
      ("//host/computador", "/diretório")

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.splitroot(path, /)

   Divide o nome de caminho *path* em uma tupla de 3 itens "(drive,
   root, tail)" onde *drive* é um nome de dispositivo ou ponto de
   montagem, *root* é uma string de separadores após a unidade e
   *tail* é tudo depois da raiz. Qualquer um desses itens pode ser uma
   string vazia. Em todos os casos, "drive + root + tail" será igual a
   *path*.

   Em sistemas POSIX, *drive* está sempre vazio. A *root* pode estar
   vazia (se *path* for relativo), uma única barra (se *path* for
   absoluto) ou duas barras (definidas pela implementação de acordo
   com IEEE Std 1003.1-2017; 4.13 Pathname Resolution.) Por exemplo:

      >>> splitroot('/home/sam')
      ('', '/', 'home/sam')
      >>> splitroot('//home/sam')
      ('', '//', 'home/sam')
      >>> splitroot('///home/sam')
      ('', '/', '//home/sam')

   No Windows, *drive* pode estar vazio, ser um nome de letra de
   unidade, um compartilhamento UNC ou um nome de dispositivo. *root*
   pode estar vazio, ser uma barra ou uma barra invertida. Por
   exemplo:

      >>> splitroot('C:/Users/Sam')
      ('C:', '/', 'Users/Sam')
      >>> splitroot('//Server/Share/Users/Sam')
      ('//Server/Share', '/', 'Users/Sam')

   Adicionado na versão 3.12.

os.path.splitext(path, /)

   Divida o nome do caminho *path* em um par "(root, ext)" de modo que
   "root + ext == path", e a extensão, *ext*, esteja vazia ou comece
   com um ponto e contenha no máximo um período.

   Se o caminho não contiver extensão, *ext* será "''":

      >>> splitext('bar')
      ('bar', '')

   Se o caminho contiver uma extensão, *ext* será definido para esta
   extensão, incluindo o ponto inicial. Observe que os períodos
   anteriores serão ignorados:

      >>> splitext('foo.bar.exe')
      ('foo.bar', '.exe')
      >>> splitext('/foo/bar.exe')
      ('/foo/bar', '.exe')

   Os períodos iniciais do último componente do caminho são
   considerados parte da raiz:

      >>> splitext('.cshrc')
      ('.cshrc', '')
      >>> splitext('/foo/....jpg')
      ('/foo/....jpg', '')

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

os.path.supports_unicode_filenames

   "True" se strings Unicode arbitrárias podem ser usadas como nomes
   de arquivo (dentro das limitações impostas pelo sistema de
   arquivos).
