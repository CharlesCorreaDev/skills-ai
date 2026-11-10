"shutil" --- Operações de arquivo de alto nível
***********************************************

**Código-fonte:** Lib/shutil.py

======================================================================

The "shutil" module offers a number of high-level operations on files
and collections of files.  In particular, functions are provided
which support file copying and removal. For operations on individual
files, see also the "os" module.

Aviso:

  Mesmo as funções de cópia de arquivos de nível mais alto
  ("shutil.copy()", "shutil.copy2()") não podem copiar todos os
  metadados do arquivo.Nas plataformas POSIX, isso significa que o
  proprietário e o grupo do arquivo são perdidos, bem como as ACLs. No
  Mac OS, a bifurcação de recursos e outros metadados não são usados.
  Isso significa que os recursos serão perdidos e o tipo de arquivo e
  os códigos do criador não estarão corretos. No Windows, os
  proprietários de arquivos, ACLs e fluxos de dados alternativos não
  são copiados.


Operações de diretório e arquivos
=================================

shutil.copyfileobj(fsrc, fdst[, length])

   Copia o conteúdo do *objeto arquivo ou similar* *fsrc* para o
   objeto arquivo ou similar *fdst*. O número inteiro *length*, se
   fornecido, é o tamanho do buffer. Em particular, um valor negativo
   *length* significa copiar os dados sem repetir os dados de origem
   em pedaços; por padrão, os dados são lidos em pedaços para evitar o
   consumo descontrolado de memória. Observe que, se a posição atual
   do arquivo do objeto *fsrc* não for 0, apenas o conteúdo da posição
   atual do arquivo até o final do arquivo será copiado.

   "copyfileobj()" *não* garante que o fluxo de destino tenha sido
   liberado após a conclusão da cópia. Se você quiser ler do destino
   após a conclusão da operação de cópia (por exemplo, ler o conteúdo
   de um arquivo temporário copiado de um fluxo HTTP), certifique-se
   de ter chamado "flush()" ou "close()" no objeto arquivo ou similar
   antes de tentar ler o arquivo de destino.

shutil.copyfile(src, dst, *, follow_symlinks=True)

   Copia o conteúdo (sem metadados) do arquivo chamado *src* para um
   arquivo chamado *dst* e retorna *dst* da maneira mais eficiente
   possível. *src* e *dst* são *objetos caminho ou similares* ou nomes
   de caminhos dados como strings.

   *dst* deve ser o nome completo do arquivo de destino; veja "copy()"
   para uma cópia que aceita um caminho de diretório de destino. Se
   *src* e *dst* especificarem o mesmo arquivo, "SameFileError" será
   levantada.

   O local de destino deve ser gravável; caso contrário, uma exceção
   "OSError" será levantada. Se o *dst* já existir, ele será
   substituído. Arquivos especiais como dispositivos de caractere ou
   bloco e encadeamentos (pipe) não podem ser copiados com esta
   função.

   Se *follow_symlinks* for falso e *src* for um link simbólico, um
   novo link simbólico será criado em vez de copiar o arquivo *src*
   para o qual o arquivo aponta.

   Levanta um evento de auditoria "shutil.copyfile" com os argumentos
   "src", "dst".

   Alterado na versão 3.3: "IOError" costumava ser levantada em vez de
   "OSError". Adicionado argumento *follow_symlinks*. Agora retorna
   *dst*.

   Alterado na versão 3.4: Levanta "SameFileError" em vez de "Error".
   Como a primeira é uma subclasse da última, essa alteração é
   compatível com versões anteriores.

   Alterado na versão 3.8: As chamadas de sistema de cópia rápida
   específicas da plataforma podem ser usadas internamente para copiar
   o arquivo com mais eficiência. Veja a seção Operações de cópia
   eficientes dependentes da plataforma.

exception shutil.SpecialFileError

   Esta exceção é levantada quando "copyfile()" ou "copytree()" tenta
   copiar um pipe nomeado.

   Adicionado na versão 2.7.

exception shutil.SameFileError

   Essa exceção é levantada se a origem e o destino em "copyfile()"
   forem o mesmo arquivo.

   Adicionado na versão 3.4.

shutil.copymode(src, dst, *, follow_symlinks=True)

   Copia os bits de permissão de *src* para *dst*. O conteúdo do
   arquivo, o proprietário e o grupo não são afetados. *src* e *dst*
   são *objetos caminho ou similares* ou nomes de caminhos dados como
   strings. Se *follow_symlinks* for falso e *src* e *dst* forem links
   simbólicos, "copymode()" tentará modificar o modo do *dst* (e não o
   arquivo para o qual ele aponta). Essa funcionalidade não está
   disponível em todas as plataformas; veja "copystat()" para mais
   informações. Se "copymode()" não puder modificar links simbólicos
   na plataforma local, e for solicitado a fazê-lo, não fará nada e
   retornará.

   Levanta um evento de auditoria "shutil.copymode" com os argumentos
   "src", "dst".

   Alterado na versão 3.3: Adicionado argumento *follow_symlinks*.

shutil.copystat(src, dst, *, follow_symlinks=True)

   Copia os bits de permissão, hora do último acesso, hora da última
   modificação e sinalizadores de *src* para *dst*. No Linux,
   "copystat()" também copia os "atributos estendidos" sempre que
   possível. O conteúdo do arquivo, o proprietário e o grupo não são
   afetados. *src* e *dst* são *objetos caminho ou similares* ou nomes
   de caminhos dados como strings.

   Se *follow_symlinks* for falso e *src* e *dst* se referirem a links
   simbólicos, "copystat()" operará nos próprios links simbólicos, e
   não nos arquivos aos quais os links simbólicos se referem - lendo
   as informações do link simbólico *src* e gravando as informações no
   link simbólico *dst*.

   Nota:

     Nem todas as plataformas oferecem a capacidade de examinar e
     modificar links simbólicos. O próprio Python pode dizer qual
     funcionalidade está disponível localmente.

     * Se "os.chmod in os.supports_follow_symlinks" for "True",
       "copystat()" pode modificar os bits de permissão de um link
       simbólico.

     * Se "os.utime in os.supports_follow_symlinks" for "True",
       "copystat()" pode modificar as horas da última modificação e do
       último acesso de um link simbólico.

     * Se "os.chflags in os.supports_follow_symlinks" for "True",
       "copystat()" pode modificar os sinalizadores de um link
       simbólico. ("os.chflags" não está disponível em todas as
       plataformas.)

     Nas plataformas em que algumas ou todas essas funcionalidades não
     estão disponíveis, quando solicitado a modificar um link
     simbólico, "copystat()" copiará tudo o que puder. "copystat()"
     nunca retorna falha.Por favor, veja "os.supports_follow_symlinks"
     para mais informações.

   Levanta um evento de auditoria "shutil.copystat" com os argumentos
   "src", "dst".

   Alterado na versão 3.3: Adicionado argumento *follow_symlinks* e
   suporte a atributos estendidos do Linux.

shutil.copy(src, dst, *, follow_symlinks=True)

   Copia o arquivo *src* para o arquivo ou diretório *dst*. *src* e
   *dst* devem ser *objetos arquivo ou similares* ou strings. Se *dst*
   especificar um diretório, o arquivo será copiado para *dst* usando
   o nome de arquivo base de *src*. Se *dst* especifica um arquivo que
   já existe, ele será substituído. Retorna o caminho para o arquivo
   recém-criado.

   Se *follow_symlinks* for falso e *src* for um link simbólico, *dst*
   será criado como um link simbólico. Se *follow_symlinks* for
   verdadeiro e *src* for um link simbólico, *dst* será uma cópia do
   arquivo ao qual *src* se refere.

   "copy()" copia os dados do arquivo e o modo de permissão do arquivo
   (consulte "os.chmod()"). Outros metadados, como os tempos de
   criação e modificação do arquivo, não são preservados. Para
   preservar todos os metadados do arquivo do original, use "copy2()".

   Levanta um evento de auditoria "shutil.copyfile" com os argumentos
   "src", "dst".

   Levanta um evento de auditoria "shutil.copymode" com os argumentos
   "src", "dst".

   Alterado na versão 3.3: Adicionado argumento *follow_symlinks*.
   Agora retorna o caminho para o arquivo recém-criado.

   Alterado na versão 3.8: As chamadas de sistema de cópia rápida
   específicas da plataforma podem ser usadas internamente para copiar
   o arquivo com mais eficiência. Veja a seção Operações de cópia
   eficientes dependentes da plataforma.

shutil.copy2(src, dst, *, follow_symlinks=True)

   Idêntico a "copy()", exceto que "copy2()" também tenta preservar os
   metadados do arquivo.

   Quando *follow_symlinks* for falso e *src* for um link simbólico,
   "copy2()" tenta copiar todos os metadados do link simbólico *src*
   para o link simbólico *dst* recém-criado. No entanto, essa
   funcionalidade não está disponível em todas as plataformas. Nas
   plataformas em que algumas ou todas essas funcionalidades não estão
   disponíveis, "copy2()" preservará todos os metadados que puder;
   "copy2()" nunca levanta uma exceção porque não pode preservar os
   metadados do arquivo.

   "copy2()" usa "copystat()" para copiar os metadados do arquivo. Por
   favor, veja "copystat()" para obter mais informações sobre o
   suporte da plataforma para modificar os metadados do link
   simbólico.

   Levanta um evento de auditoria "shutil.copyfile" com os argumentos
   "src", "dst".

   Levanta um evento de auditoria "shutil.copystat" com os argumentos
   "src", "dst".

   Alterado na versão 3.3: Adicionado argumento *follow_symlinks*,
   tenta copiar também atributos estendidos do sistema de arquivos
   (atualmente apenas no Linux). Agora retorna o caminho para o
   arquivo recém-criado.

   Alterado na versão 3.8: As chamadas de sistema de cópia rápida
   específicas da plataforma podem ser usadas internamente para copiar
   o arquivo com mais eficiência. Veja a seção Operações de cópia
   eficientes dependentes da plataforma.

shutil.ignore_patterns(*patterns)

   Esta função de fábrica cria uma função que pode ser usada como um
   chamável para o argumento *ignore* de "copytree()", ignorando
   arquivos e diretórios que correspondem a um dos padrões *patterns*
   de estilo glob fornecidos. Veja o exemplo abaixo.

shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

   Copia recursivamente uma árvore de diretórios inteira com raiz em
   *src* para um diretório chamado *dst* e retorna o diretório de
   destino. Todos os diretórios intermediários necessários para conter
   *dst* também serão criados por padrão.

   Permissões e horas dos diretórios são copiados com "copystat()",
   arquivos individuais são copiados usando "copy2()".

   Se *symlinks* for verdadeiro, os links simbólicos na árvore de
   origem são representados como links simbólicos na nova árvore e os
   metadados dos links originais serão copiados na medida do permitido
   pela plataforma; se falso ou omitido, o conteúdo e os metadados dos
   arquivos vinculados são copiados para a nova árvore.

   Quando *symlinks* for falso, se o arquivo apontado pelo link
   simbólico não existir, uma exceção será adicionada na lista de
   erros levantada em uma exceção "Error" no final do processo de
   cópia. Você pode definir o sinalizador opcional
   *ignore_dangling_symlinks* como true se desejar silenciar esta
   exceção. Observe que esta opção não tem efeito em plataformas que
   não possuem suporte a "os.symlink()".

   Se *ignore* for fornecido, deve ser um chamável que receberá como
   argumento o diretório que está sendo visitado por "copytree()", e
   uma lista de seu conteúdo, retornada por "os.listdir()". Como
   "copytree()" é chamada recursivamente, o chamável *ignore* será
   chamado uma vez para cada diretório que é copiado. O chamável deve
   retornar uma sequência de nomes de diretório e arquivo em relação
   ao diretório atual (ou seja, um subconjunto dos itens em seu
   segundo argumento); esses nomes serão ignorados no processo de
   cópia. "ignore_patterns()" pode ser usado para criar um chamável
   que ignore nomes com base em padrões de estilo glob.

   Se uma ou mais exceções ocorrerem, uma "Error" é levantada com uma
   lista dos motivos.

   Se *copy_function* for fornecida, deverá ser um chamável que será
   usado para copiar cada arquivo. Ele será chamado com o caminho de
   origem e o caminho de destino como argumentos. Por padrão,
   "copy2()" é usada, mas qualquer função que possua suporte à mesma
   assinatura (como "copy()") pode ser usada.

   Se *dirs_exist_ok* for false (o padrão) e *dst* já existir, uma
   "FileExistsError" será levantada. Se *dirs_exist_ok* for true, a
   operação de cópia continuará se encontrar diretórios existentes, e
   os arquivos dentro da árvore *dst* serão sobrescritos pelos
   arquivos correspondentes da árvore *src*.

   Levanta um evento de auditoria "shutil.copytree" com os argumentos
   "src", "dst".

   Alterado na versão 3.2: Adicionado o argumento *copy_function* para
   poder fornecer uma função de cópia personalizada. Adicionado o
   argumento *ignore_dangling_symlinks* para silenciar erros de links
   simbólicos quando *symlinks* for falso.

   Alterado na versão 3.3: Copia metadados quando *symlinks* for
   falso. Agora, retorna *dst*.

   Alterado na versão 3.8: As chamadas de sistema de cópia rápida
   específicas da plataforma podem ser usadas internamente para copiar
   o arquivo com mais eficiência. Veja a seção Operações de cópia
   eficientes dependentes da plataforma.

   Alterado na versão 3.8: Adicionado o parâmetro *dirs_exist_ok*.

shutil.rmtree(path, ignore_errors=False, onerror=None, *, onexc=None, dir_fd=None)

   Exclui uma árvore de diretório inteira; *path* deve apontar para um
   diretório (mas não um link simbólico para um diretório). Se
   *ignore_errors* for verdadeiro, os erros resultantes de remoções
   com falha serão ignorados; se falso ou omitido, tais erros são
   tratados chamando um manipulador especificado por *onexc* ou
   *onerror* ou, se ambos forem omitidos, exceções são propagadas para
   o chamador.

   If *path* is a symbolic link to a directory followed by a trailing
   path separator, such as "'link/'", the operating system resolves
   the link, so "rmtree()" deletes the contents of the directory it
   points to and then fails to remove *path* itself.  "pathlib.Path"
   strips trailing separators, so "rmtree(Path('link/'))" refuses the
   link as usual.

   Esta função tem suporte a caminhos relativos para descritores de
   diretório.

   Nota:

     Em plataformas que suportam as funções baseadas em descritores de
     arquivo necessárias, uma versão resistente a ataques de links
     simbólicos de "rmtree()" é usada por padrão. Em outras
     plataformas, a implementação "rmtree()" é suscetível a um ataque
     de link simbólico: dados o tempo e as circunstâncias apropriados,
     os invasores podem manipular links simbólicos no sistema de
     arquivos para excluir arquivos que eles não seriam capazes de
     acessar de outra forma. Os aplicativos podem usar o atributo de
     função "rmtree.avoids_symlink_attacks" para determinar qual caso
     se aplica.

   Se *onexc* for fornecido, deve ser um chamável que aceite três
   parâmetros: *function*, *path*, e *excinfo*.

   O primeiro parâmetro, *function*, é a função que levantou a
   exceção; depende da plataforma e da implementação. O segundo
   parâmetro, *path*, será o nome do caminho passado para a *função*.
   O terceiro parâmetro, *excinfo*, é a exceção que foi levantada.
   Exceções levantadas por *onexc* não serão capturadas.

   O descontinuado *onerror* é semelhante ao *onexc*, exceto que o
   terceiro parâmetro que ele recebe é a tupla retornada de
   "sys.exc_info()".

   Ver também:

     exemplo rmtree para um exemplo de tratamento da remoção de uma
     árvore de diretórios que contém arquivos somente leitura.

   Levanta um evento de auditoria "shutil.rmtree" com os argumentos
   "path", "dir_fd".

   Alterado na versão 3.3: Adicionada uma versão resistente a ataques
   de link simbólico que é usada automaticamente se a plataforma
   suportar funções baseadas em descritor de arquivo.

   Alterado na versão 3.8: No Windows, não excluirá mais o conteúdo de
   uma junção de diretório antes de remover a junção.

   Alterado na versão 3.11: Adicionado o parâmetro *dir_fd*.

   Alterado na versão 3.12: Adicionado o parâmetro *onexc*,
   descontinuado *onerror*.

   Alterado na versão 3.13: "rmtree()" agora ignora exceções
   "FileNotFoundError" para todos, exceto o caminho de nível superior.
   Exceções diferentes de "OSError" e subclasses de "OSError" agora
   são sempre propagadas para o chamador.

   rmtree.avoids_symlink_attacks

      Indica se a plataforma e implementação atuais fornecem uma
      versão resistente a ataques de link simbólico de "rmtree()".
      Atualmente, isso só é verdade para plataformas que suportam
      funções de acesso ao diretório baseadas em descritor de arquivo.

      Adicionado na versão 3.3.

shutil.move(src, dst, copy_function=copy2)

   Move recursivamente um arquivo ou diretório (*src*) para outro
   local e retorna ao destino.

   Se *dst* for um diretório existente ou um symlink para um
   diretório, então *src* é movido para dentro desse diretório. O
   caminho de destino nesse diretório não deve existir ainda.

   Se *dst* já existir, mas não for um diretório, ele poderá ser
   substituído dependendo da semântica de "os.rename()".

   "os.rename()" is preferably used internally when *src* and the
   destination are on the same filesystem. In case "os.rename()" fails
   due to "OSError" (e.g. the user has write permission to the
   destination file but not to its parent directory), this method
   falls back to using *copy_function*, in which case *src* is copied
   to the destination using *copy_function* and then removed.

   In case of symlinks, a new symlink pointing to the target of *src*
   will be created in or as the destination, and *src* will be
   removed.

   Se *copy_function* for fornecido, deve ser um chamável que leva
   dois argumentos *src* e a destinação, e será usado para copiar
   *src* para a destinação se "os.rename()" não puder ser usado. Se a
   fonte for um diretório, "copytree()" é chamado, passando
   *copy_function*. A *copy_function* padrão é "copy2()". Usar
   "copy()" como *copy_function* permite que a movimentação seja bem-
   sucedida quando não é possível copiar também os metadados, às
   custas de não copiar nenhum dos metadados.

   Levanta um evento de auditoria "shutil.move" com os argumentos
   "src", "dst".

   Alterado na versão 3.3: Adicionada manipulação de links simbólicos
   explícitos para sistemas de arquivos externos, adaptando-os ao
   comportamento do GNU **mv**. Agora retorna *dst*.

   Alterado na versão 3.5: Adicionado o argumento nomeado
   *copy_function*.

   Alterado na versão 3.8: As chamadas de sistema de cópia rápida
   específicas da plataforma podem ser usadas internamente para copiar
   o arquivo com mais eficiência. Veja a seção Operações de cópia
   eficientes dependentes da plataforma.

   Alterado na versão 3.9: Aceita um *objeto caminho ou similar* para
   *src* e *dst*.

shutil.disk_usage(path)

   Retorna estatísticas de uso de disco sobre o caminho fornecido como
   *tupla nomeada* com os atributos *total*, *used* e *free*, que são
   a quantidade de espaço total, usado e livre, em bytes. *path* pode
   ser um arquivo ou diretório.

   Nota:

     Em sistemas de arquivos Unix, *path* deve apontar para um caminho
     dentro de uma partição de sistema de arquivos **montada**. Nessas
     plataformas, o CPython não tenta recuperar informações de uso de
     disco de sistemas de arquivos não montados.

   Adicionado na versão 3.3.

   Alterado na versão 3.8: No Windows, *path* pode agora ser um
   arquivo ou diretório.

   Disponibilidade: Unix, Windows.

shutil.chown(path, user=None, group=None, *, dir_fd=None, follow_symlinks=True)

   Altera o proprietário *usuário* e/ou *group* do *path* fornecido.

   *user* pode ser um nome de usuário do sistema ou um uid; o mesmo se
   aplica ao *group*. É necessário pelo menos um argumento.

   Veja também "os.chown()", a função subjacente.

   Levanta um evento de auditoria "shutil.chown" com os argumentos
   "path", "user", "group".

   Disponibilidade: Unix.

   Adicionado na versão 3.3.

   Alterado na versão 3.13: Adicionados os parâmetros *dir_fd* e
   *follow_symlinks*.

shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)

   Retorna o caminho para um executável que seria executado se o *cmd*
   fornecido fosse chamado. Se nenhum *cmd* for chamado, retorna
   "None".

   *mode* é uma máscara de permissão passada para "os.access()", por
   padrão determinando se o arquivo existe e é executável.

   *path* é uma "string "PATH"" que especifica os diretórios a serem
   procurados, delimitados por "os.pathsep". Quando nenhum *path* é
   especificado, a variável de ambiente "PATH" é lida de "os.environ",
   retornando para "os.defpath" se não estiver definida.

   Se *cmd* contiver um componente de diretório, "which()" verificará
   apenas o caminho especificado diretamente e não pesquisará os
   diretórios listados em *path* ou na variável de ambiente "PATH" do
   sistema.

   No Windows, o diretório atual é prefixado ao *path* se o *mode* não
   incluir "os.X_OK". Quando o *mode* inclui "os.X_OK", a API do
   Windows "NeedCurrentDirectoryForExePathW" será consultada para
   determinar se o diretório atual deve ser prefixado ao *path*. Para
   evitar consultar o diretório de trabalho atual para executáveis:
   defina a variável de ambiente "NoDefaultCurrentDirectoryInExePath".

   Também no Windows, a variável de ambiente "PATHEXT" é usada para
   resolver comandos que podem não incluir uma extensão. Por exemplo,
   se você chamar "shutil.which("python")", "which()" pesquisará
   "PATHEXT" para saber que deve procurar por "python.exe" dentro dos
   diretórios *path*. Por exemplo, no Windows:

      >>> shutil.which("python")
      'C:\\Python33\\python.EXE'

   Isso também se aplica quando *cmd* é um caminho que contém um
   componente de diretório:

      >>> shutil.which("C:\\Python33\\python")
      'C:\\Python33\\python.EXE'

   Adicionado na versão 3.3.

   Alterado na versão 3.8: O tipo "bytes" é agora aceitado. Se o tipo
   de *cmd* é "bytes", o tipo resultante também é "bytes".

   Alterado na versão 3.12: No Windows, o diretório atual não é mais
   adicionado ao caminho de pesquisa se *mode* incluir "os.X_OK" e
   WinAPI "NeedCurrentDirectoryForExePathW(cmd)" for falso, caso
   contrário, o diretório atual será adicionado mesmo se já estiver no
   caminho de pesquisa; "PATHEXT" agora é usado mesmo quando *cmd*
   inclui um componente de diretório ou termina com uma extensão que
   está em "PATHEXT"; e nomes de arquivos que não têm extensão agora
   podem ser encontrados.

exception shutil.Error

   Subclass of "OSError" collecting exceptions raised during a multi-
   file operation. For "copytree()", the exception argument is a list
   of 3-tuples (*srcname*, *dstname*, *exception*).


Operações de cópia eficientes dependentes da plataforma
-------------------------------------------------------

A partir do Python 3.8, todas as funções envolvendo uma cópia de
arquivo ("copyfile()", "copy()", "copy2()", "copytree()" e "move()" )
podem usar chamadas do sistema de "cópia rápida" específicas da
plataforma para copiar o arquivo de forma mais eficiente (veja
bpo-33671). "cópia rápida" significa que a operação de cópia ocorre
dentro do kernel, evitando o uso de buffers de espaço de usuário em
Python como em ""outfd.write(infd.read())"".

No macOS, fcopyfile é usado para copiar o conteúdo do arquivo (não
metadados).

No Linux, "os.copy_file_range()" ou "os.sendfile()" é usado.

No Solaris, "os.sendfile()" é usado.

On Windows "shutil.copyfile()" uses a bigger default buffer size (1
MiB instead of 64 KiB) and a "memoryview()"-based variant of
"shutil.copyfileobj()" is used, which still reads and writes in a
loop. "shutil.copy2()" uses the native "CopyFile2" call on Windows,
which is the most efficient method, supports copy-on-write, and
preserves metadata.

If the fast-copy operation fails and no data was written in the
destination file then shutil will silently fall back to less efficient
"copyfileobj()" function internally.

Alterado na versão 3.8.

Alterado na versão 3.14: Solaris agora usa "os.sendfile()".

Alterado na versão 3.14: A cópia na gravação (copy-on-write) ou cópia
do lado do servidor podem ser usadas internamente via
"os.copy_file_range()" em sistemas de arquivos Linux suportados.


Exemplo de copytree
-------------------

Um exemplo que usa o auxiliar "ignore_patterns()":

   from shutil import copytree, ignore_patterns

   copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

Isso irá copiar tudo, exceto os arquivos ".pyc" e arquivos ou
diretórios cujo nome começa com "tmp".

Outro exemplo que usa o argumento *ignore* para adicionar uma chamada
de registro:

   from shutil import copytree
   import logging

   def _logpath(path, names):
       logging.info('Working in %s', path)
       return []   # nada será ignorado

   copytree(source, destination, ignore=_logpath)


exemplo rmtree
--------------

Este exemplo mostra como remover uma árvore de diretório no Windows
onde alguns dos arquivos têm seu conjunto de bits somente leitura. Ele
usa a função de retorno onexc para limpar o bit somente leitura e
tentar remover novamente. Qualquer falha subsequente se propagará.

   import os, stat
   import shutil

   def remove_readonly(func, path, _):
       "Clear the readonly bit and reattempt the removal"
       os.chmod(path, stat.S_IWRITE)
       func(path)

   shutil.rmtree(directory, onexc=remove_readonly)


Operações de arquivamento
=========================

Adicionado na versão 3.2.

Alterado na versão 3.5: Adicionado suporte ao formato *xztar*.

Utilitários de alto nível para criar e ler arquivos compactados e
arquivados também são fornecidos. Eles contam com os módulos "zipfile"
e "tarfile".

shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])

   Cria um arquivo compactado (como zip ou tar) e retorna seu nome.

   *base_name* is a string or *path-like object* specifying the name
   of the file to create, including the path, minus any format-
   specific extension.

   *format* é o formato do arquivo: um de "zip" (se o módulo "zlib"
   estiver disponível), "tar", "gztar" (se o módulo "zlib" estiver
   disponível), "bztar" (se o módulo "bz2" estiver disponível),
   "xztar" (se o módulo "lzma" estiver disponível) ou "zstdtar" (se o
   módulo "compression.zstd" estiver disponível).

   *root_dir* is a string or *path-like object* specifying a directory
   that will be the root directory of the archive, all paths in the
   archive will be relative to it; for example, we typically chdir
   into *root_dir* before creating the archive.

   *base_dir* is a string or *path-like object* specifying a directory
   where we start archiving from; i.e. *base_dir* will be the common
   prefix of all files and directories in the archive.  *base_dir*
   must be given relative to *root_dir*.  See Exemplo de arquivamento
   com base_dir for how to use *base_dir* and *root_dir* together.

   *root_dir* e *base_dir* têm com padrão o diretório atual.

   Se *dry_run* for verdadeiro, nenhum arquivo é criado, mas as
   operações que seriam executadas são registradas no *logger*.

   *owner* e *group* são usados ao criar um arquivo tar. Por padrão,
   usa o proprietário e grupo atuais.

   *logger* deve ser um objeto compatível com a **PEP 282**,
   geralmente uma instância de "logging.Logger".

   O argumento *verbose* não é usado e foi descontinuado.

   Levanta um evento de auditoria "shutil.make_archive" com os
   argumentos "base_name", "format", "root_dir", "base_dir".

   Nota:

     Esta função não é segura para thread quando arquivadores
     personalizados registrados com "register_archive_format()" não
     suportam o argumento *root_dir*. Neste caso, ele altera
     temporariamente o diretório de trabalho atual do processo para
     *root_dir* para executar o arquivamento.

   Alterado na versão 3.8: O formato pax moderno (POSIX.1-2001) agora
   é usado em vez do formato GNU legado para arquivos criados com
   "format="tar"".

   Alterado na versão 3.10.6: Esta função agora é segura para thread
   durante a criação de arquivos ".zip" e tar padrão.

   Alterado na versão 3.15: Accepts a *path-like object* for
   *base_name*, *root_dir* and *base_dir*.

shutil.get_archive_formats()

   Retorna uma lista de formatos suportados para arquivamento. Cada
   elemento da sequência retornada é uma tupla "(nome, descrição)".

   By default "shutil" provides these formats:

   * *zip*: arquivo ZIP (se o módulo "zlib" estiver disponível).

   * *tar*: Arquivo tar não compactado. Usa o formato POSIX.1-2001 pax
     para novos arquivos.

   * *gztar*: arquivo tar compactado com gzip (se o módulo "zlib"
     estiver disponível).

   * *bztar*: arquivo tar compactado com bzip2 (se o módulo "bz2"
     estiver disponível).

   * *xztar*: Arquivo tar compactado com xz (se o módulo "lzma"
     estiver disponível).

   * *zstdtar*: arquivo tar compactado com Zstandard (se o módulo
     "compression.zstd" estiver disponível).

   Você pode registrar novos formatos ou fornecer seu próprio
   arquivador para quaisquer formatos existentes, usando
   "register_archive_format()".

shutil.register_archive_format(name, function[, extra_args[, description]])

   Registra um arquivador para o formato *name*.

   *function* is the callable that will be used to create archives.
   The callable will receive the *base_name* of the file to create,
   followed by the *base_dir* (which defaults to "os.curdir") to start
   archiving from. Further arguments are passed as keyword arguments:
   *owner*, *group*, *dry_run* and *logger* (as passed in
   "make_archive()").

   Se *function* tiver o atributo personalizado
   "function.supports_root_dir" definido como "True", o argumento
   *root_dir* será passado como um argumento nomeado. Caso contrário,
   o diretório de trabalho atual do processo será temporariamente
   alterado para *root_dir* antes de chamar *function*. Nesse caso,
   "make_archive()" não é segura para thread.

   Se fornecido, *extra_args* é uma sequência de pares "(nome, valor)"
   que serão usados como argumentos nomeados extras quando o
   arquivador chamável for usado.

   *description* é usado por "get_archive_formats()" que retorna a
   lista de arquivadores. O padrão é uma string vazia.

   Alterado na versão 3.12: Adicionado suporte para funções que
   suportam o argumento *root_dir*.

shutil.unregister_archive_format(name)

   Remove o formato de arquivo *name* da lista de formatos suportados.

shutil.unpack_archive(filename[, extract_dir[, format[, filter]]])

   Desempacota um arquivo. *filename* é o caminho completo do arquivo.

   *extract_dir* é o nome do diretório de destino onde o arquivo é
   desempacotado. Se não for fornecido, o diretório de trabalho atual
   será usado.

   *format* é o formato do arquivo: um de "zip", "tar", "gztar",
   "bztar", "xztar" e "zstdtar". Ou qualquer outro formato registrado
   com "register_unpack_format()". Se não for fornecido,
   "unpack_archive()" irá usar a extensão do nome do arquivo e ver se
   um desempacotador foi registrado para essa extensão. Caso nenhum
   seja encontrado, uma "ValueError" é levantada.

   O argumento somente-nomeado *filter* é passado para a função de
   desempacotamento subjacente. Para arquivos zip, *filter* não é
   aceito. Para arquivos tar, é recomendado usar "'data'" (padrão
   desde o Python 3.14), a menos que esteja usando recursos
   específicos para tar e sistemas de arquivos do tipo UNIX. (Veja
   Filtros de extração para detalhes.)

   Levanta um evento de auditoria "shutil.unpack_archive" com os
   argumentos "filename", "extract_dir", "format".

   Aviso:

     Never extract archives from untrusted sources without prior
     inspection. It is possible that files are created outside of the
     path specified in the *extract_dir* argument, for example,
     members that have absolute filenames or filenames with ".."
     components.Desde o Python 3.14, os padrões para ambos os formatos
     embutidos (arquivos zip e tar) evitarão os problemas de segurança
     mais perigosos, mas não impedirão *todos* os comportamentos
     indesejados. Leia a seção Dicas para verificação adicional para
     detalhes específicos do tar.

   Alterado na versão 3.7: Aceita um *objeto caminho ou similar* para
   *filename* e *extract_dir*.

   Alterado na versão 3.12: Adicionado o argumento *filter*.

shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])

   Registra um formato de desempacotamento. *name* é o nome do formato
   e *extensions* é uma lista de extensões correspondentes ao formato,
   como ".zip" para arquivos Zip.

   *function* é o chamável que será usado para desempacotar arquivos.
   O chamável receberá:

   * o caminho do arquivo, como argumento posicional;

   * o diretório para o qual o arquivo deve ser extraído, como um
     argumento posicional;

   * possivelmente um argumento nomeado *filter*, se foi dado a
     "unpack_archive()";

   * argumentos nomeados adicionais, especificados por *extra_args*
     como uma sequência de tuplas "(nome, valor)".

   *description* pode ser fornecido para descrever o formato e será
   devolvido pela função "get_unpack_formats()".

shutil.unregister_unpack_format(name)

   Cancela o registro de um formato de desempacotamento. *name* é o
   nome do formato.

shutil.get_unpack_formats()

   Retorna uma lista de todos os formatos registrados para
   desempacotamento. Cada elemento da sequência retornada é uma tupla
   "(name, extensions, description)".

   By default "shutil" provides these formats:

   * *zip*: arquivo ZIP (desempacotar arquivos compactados funciona
     apenas se o módulo correspondente estiver disponível).

   * *tar*: arquivo tar não comprimido.

   * *gztar*: arquivo tar compactado com gzip (se o módulo "zlib"
     estiver disponível).

   * *bztar*: arquivo tar compactado com bzip2 (se o módulo "bz2"
     estiver disponível).

   * *xztar*: Arquivo tar compactado com xz (se o módulo "lzma"
     estiver disponível).

   * *zstdtar*: arquivo tar compactado com Zstandard (se o módulo
     "compression.zstd" estiver disponível).

   Você pode registrar novos formatos ou fornecer seu próprio
   desempacotador para quaisquer formatos existentes, usando
   "register_unpack_format()".


Exemplo de arquivo
------------------

Neste exemplo, criamos um arquivo tar compactado com gzip contendo
todos os arquivos encontrados no diretório ".ssh" do usuário:

   >>> from shutil import make_archive
   >>> import os
   >>> archive_name = os.path.expanduser(os.path.join('~', 'meuarquivo'))
   >>> root_dir = os.path.expanduser(os.path.join('~', '.ssh'))
   >>> make_archive(archive_name, 'gztar', root_dir)
   '/Users/tarek/meuarquivo.tar.gz'

O arquivo resultante contém:

   $ tar -tzvf /Users/tarek/meuarquivo.tar.gz
   drwx------ tarek/staff       0 2010-02-01 16:23:40 ./
   -rw-r--r-- tarek/staff     609 2008-06-09 13:26:54 ./authorized_keys
   -rwxr-xr-x tarek/staff      65 2008-06-09 13:26:54 ./config
   -rwx------ tarek/staff     668 2008-06-09 13:26:54 ./id_dsa
   -rwxr-xr-x tarek/staff     609 2008-06-09 13:26:54 ./id_dsa.pub
   -rw------- tarek/staff    1675 2008-06-09 13:26:54 ./id_rsa
   -rw-r--r-- tarek/staff     397 2008-06-09 13:26:54 ./id_rsa.pub
   -rw-r--r-- tarek/staff   37192 2010-02-06 18:23:10 ./known_hosts


Exemplo de arquivamento com *base_dir*
--------------------------------------

Neste exemplo, semelhante ao acima, mostramos como usar
"make_archive()", mas desta vez com o uso de *base_dir*. Agora temos a
seguinte estrutura de diretório:

   $ tree tmp
   tmp
   └── root
       └── estrutura
           ├── conteudo
               └── por_favor_adicionar.txt
           └── nao_adicionar.txt

No arquivo final, "please_add.txt" deve ser incluído, mas
"do_not_add.txt" não deve. Portanto, usamos o seguinte:

   >>> from shutil import make_archive
   >>> import os
   >>> archive_name = os.path.expanduser(os.path.join('~', 'meuarquivo'))
   >>> make_archive(
   ...     archive_name,
   ...     'tar',
   ...     root_dir='tmp/root',
   ...     base_dir='estrutura/conteudo',
   ... )
   '/Users/tarek/meu_arquivo.tar'

Listar os arquivos no arquivo resultante nos dá:

   $ python -m tarfile -l /Users/tarek/meuarquivo.tar
   estrutura/conteudo/
   estrutura/conteudo/por_favor_adicionar.txt


Consultando o tamanho do terminal de saída
==========================================

shutil.get_terminal_size(fallback=(columns, lines))

   Obtém o tamanho da janela do terminal.

   Para cada uma das duas dimensões, a variável de ambiente, "COLUMNS"
   e "LINES" respectivamente, é verificada. Se a variável estiver
   definida e o valor for um número inteiro positivo, ela será usada.

   Quando "COLUMNS" ou "LINES" não está definida, que é o caso comum,
   o terminal conectado a "sys.__stdout__" é consultado invocando
   "os.get_terminal_size()".

   Se o tamanho do terminal não pode ser consultado com sucesso, ou
   porque o sistema não tem suporte a consultas, ou porque não estamos
   conectados a um terminal, o valor dado no parâmetro "fallback" é
   usado. O padrão de "fallback" é "(80, 24)", que é o tamanho padrão
   usado por muitos emuladores de terminal.

   O valor retornado é uma tupla nomeada do tipo "os.terminal_size".

   Veja também: The Single UNIX Specification, Versão 2, Other
   Environment Variables.

   Adicionado na versão 3.3.

   Alterado na versão 3.11: Os valores "fallback" também são usados se
   "os.get_terminal_size()" retornar zeros.
