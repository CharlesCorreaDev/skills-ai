"tarfile" --- Ler e gravar arquivos do tipo tar
***********************************************

**Código-fonte:** Lib/tarfile.py

======================================================================

The "tarfile" module makes it possible to read and write tar archives,
including those using gzip, bz2 and lzma compression. Use the
"zipfile" module to read or write ".zip" files, or the higher-level
functions in shutil.

Alguns fatos e números:

* lê e grava arquivos compactados com "gzip", "bz2",
  "compression.zstd" e "lzma" se os respectivos módulos estiverem
  disponíveis.

  Se algum desses *módulos opcionais* estiverem faltando na sua cópia
  do CPython, procure a documentação do seu distribuidor (ou seja,
  quem lhe forneceu o Python). Se você for o distribuidor, consulte
  Requisitos para módulos opcionais.

* suporte de leitura/gravação para o formato POSIX.1-1988 (ustar).

* suporte de leitura/gravação para o formato GNU tar, incluindo
  extensões *longname* e *longlink*, suporte somente leitura para
  todas as variantes da extensão *sparse*, incluindo restauração de
  arquivos esparsos.

* suporte de leitura/gravação para o formato POSIX.1-2001 (pax).

* manipula diretórios, arquivos regulares, links físicos, links
  simbólicos, fifos, dispositivos de caracteres e dispositivos de
  bloco e é capaz de adquirir e restaurar informações de arquivo, como
  registro de data e hora, permissões de acesso e proprietário.

Alterado na versão 3.3: Adicionado suporte para compactação "lzma".

Alterado na versão 3.12: Os arquivos são extraídos usando um filtro, o
que torna possível limitar recursos surpreendentes/perigosos ou
reconhecer que eles são esperados e que o arquivo é totalmente
confiável.

Alterado na versão 3.14: Define o filtro de extração padrão como
"data", o que desabilita alguns recursos perigosos, como links para
caminhos absolutos ou caminhos fora do destino. Anteriormente, a
estratégia de filtro era equivalente a "fully_trusted".

Alterado na versão 3.14: Adicionado suporte para a compactação com
Zstandard usando "compression.zstd".

tarfile.open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)

   Retorna um objeto "TarFile" para o caminho *name*. Para obter
   informações detalhadas sobre objetos "TarFile" e os argumentos
   nomeados permitidos, consulte Objetos TarFile.

   *mode* deve ser uma string no formato "'filemode[:compression]'", o
   padrão é "'r'". Aqui está uma lista completa de combinações de
   modos:

   +--------------------+-----------------------------------------------+
   | modo               | ação                                          |
   |====================|===============================================|
   | "'r'" ou "'r:*'"   | Abre para leitura com compactação             |
   |                    | transparente (recomendado).                   |
   +--------------------+-----------------------------------------------+
   | "'r:'"             | Abre para leitura exclusivamente sem          |
   |                    | compactação.                                  |
   +--------------------+-----------------------------------------------+
   | "'r:gz'"           | Abre para leitura com compactação gzip.       |
   +--------------------+-----------------------------------------------+
   | "'r:bz2'"          | Abre para leitura com compactação bzip2.      |
   +--------------------+-----------------------------------------------+
   | "'r:xz'"           | Abre para leitura com compactação lzma.       |
   +--------------------+-----------------------------------------------+
   | "'r:zst'"          | Abre para leitura com compactação Zstandard.  |
   +--------------------+-----------------------------------------------+
   | "'x'" ou "'x:'"    | Cria um arquivo tar exclusivamente sem        |
   |                    | compactação. Levanta uma exceção              |
   |                    | "FileExistsError" se ele já existir.          |
   +--------------------+-----------------------------------------------+
   | "'x:gz'"           | Cria um arquivo tar com compactação gzip.     |
   |                    | Levanta uma exceção "FileExistsError" se ele  |
   |                    | já existir.                                   |
   +--------------------+-----------------------------------------------+
   | "'x:bz2'"          | Cria um arquivo tar com compactação bzip2.    |
   |                    | Levanta uma exceção "FileExistsError" se ele  |
   |                    | já existir.                                   |
   +--------------------+-----------------------------------------------+
   | "'x:xz'"           | Cria um arquivo tar com compactação lzma.     |
   |                    | Levanta uma exceção "FileExistsError" se ele  |
   |                    | já existir.                                   |
   +--------------------+-----------------------------------------------+
   | "'x:zst'"          | Cria um arquivo tar com compactação           |
   |                    | Zstandard. Levanta uma exceção                |
   |                    | "FileExistsError" se ele já existir.          |
   +--------------------+-----------------------------------------------+
   | "'a'" ou "'a:'"    | Aberto para acrescentar conteúdo sem          |
   |                    | compactação. O arquivo é criado se não        |
   |                    | existir.                                      |
   +--------------------+-----------------------------------------------+
   | "'w'" ou "'w:'"    | Abre para gravação descompactada.             |
   +--------------------+-----------------------------------------------+
   | "'w:gz'"           | Abre para gravação compactada com gzip.       |
   +--------------------+-----------------------------------------------+
   | "'w:bz2'"          | Abre para gravação compactada com bzip2.      |
   +--------------------+-----------------------------------------------+
   | "'w:xz'"           | Abre para gravação compactada com lzma.       |
   +--------------------+-----------------------------------------------+
   | "'w:zst'"          | Abre para gravação compactada com Zstandard.  |
   +--------------------+-----------------------------------------------+

   Observe que "'a:gz'", "'a:bz2'" ou "'a:xz'" não são possíveis. Se o
   *mode* não for adequado para abrir um determinado arquivo
   (compactado) para leitura, "ReadError" será levantada. Use o *mode*
   "'r'" para evitar isso. Se um método de compactação não for
   suportado, "CompressionError" será levantada.

   Se *fileobj* for especificado, ele será usado como alternativa a um
   *objeto arquivo* aberto em modo binário para *name*. Ele deve estar
   na posição 0.

   For modes "'w:gz'", "'x:gz'", "'w|gz'", "'w:bz2'", "'x:bz2'",
   "'w|bz2'", "tarfile.open()" accepts the keyword argument
   *compresslevel* (default "6") to specify the compression level of
   the file.

   Para os modos "'w:xz'", "'x:xz'" e "'w|xz'", "tarfile.open()"
   aceita o argumento nomeado *preset* para especificar o nível de
   compactação do arquivo.

   Para os modos "'w:zst'", "'x:zst'" e "'w|zst'", "tarfile.open()"
   aceita o argumento nomeado *level* para especificar o nível de
   compactação do arquivo. O argumento nomeado *options* também pode
   ser passado, fornecendo parâmetros avançados de compactação
   Zstandard descritos por "CompressionParameter". O argumento nomeado
   *zstd_dict* pode ser passado para fornecer um "ZstdDict", um
   dicionário Zstandard usado para melhorar a compactação de pequenas
   quantidades de dados.

   For modes "'w:gz'" and "'w|gz'", "tarfile.open()" accepts the
   keyword argument *mtime* to create a gzip archive header with that
   mtime. By default, the mtime is set to the time of creation of the
   archive. Use *mtime* "0" to generate a compressed stream that does
   not depend on creation time, for reproducible output.

   Para fins especiais, existe um segundo formato para *mode*:
   "'filemode|[compression]'". "tarfile.open()" retornará um objeto
   "TarFile" que processa seus dados como um fluxo de blocos. Nenhuma
   busca aleatória será realizada no arquivo. Se fornecido, *fileobj*
   pode ser qualquer objeto que tenha um método "read()" ou "write()"
   (dependendo do *mode*) que funcione com bytes. *bufsize* especifica
   o tamanho do bloco e o padrão é "20 * 512" bytes. Use esta variante
   em combinação com, por exemplo, "sys.stdin.buffer", um *objeto
   arquivo* de soquete ou um dispositivo de fita. No entanto, tal
   objeto "TarFile" é limitado, pois não permite acesso aleatório;
   consulte Exemplos. Os modos atualmente possíveis:

   +---------------+----------------------------------------------+
   | Modo          | Ação                                         |
   |===============|==============================================|
   | "'r|*'"       | Abre um *stream* de blocos tar para leitura  |
   |               | com compactação transparente.                |
   +---------------+----------------------------------------------+
   | "'r|'"        | Abre um *stream* de blocos tar não           |
   |               | compactados para leitura.                    |
   +---------------+----------------------------------------------+
   | "'r|gz'"      | Abre um *stream* compactado com gzip para    |
   |               | leitura.                                     |
   +---------------+----------------------------------------------+
   | "'r|bz2'"     | Abre um *stream* compactado com bzip2 para   |
   |               | leitura.                                     |
   +---------------+----------------------------------------------+
   | "'r|xz'"      | Abre um *stream* compactado com lzma para    |
   |               | leitura.                                     |
   +---------------+----------------------------------------------+
   | "'r|zst'"     | Abre um *stream* compactado com Zstandard    |
   |               | para leitura.                                |
   +---------------+----------------------------------------------+
   | "'w|'"        | Abre um *stream* descompactado para          |
   |               | gravação.                                    |
   +---------------+----------------------------------------------+
   | "'w|gz'"      | Abre um *stream* compactado com gzip para    |
   |               | gravação.                                    |
   +---------------+----------------------------------------------+
   | "'w|bz2'"     | Abre um *stream* compactado com bzip2 para   |
   |               | gravação.                                    |
   +---------------+----------------------------------------------+
   | "'w|xz'"      | Abre um *stream* compactado com lzma para    |
   |               | gravação.                                    |
   +---------------+----------------------------------------------+
   | "'w|zst'"     | Abre um *stream* compactado com Zstandard    |
   |               | para gravação.                               |
   +---------------+----------------------------------------------+

   Alterado na versão 3.5: O modo "'x'" (criação exclusiva) foi
   adicionado.

   Alterado na versão 3.6: O parâmetro *name* aceita um *objeto
   caminho ou similar*.

   Alterado na versão 3.12: O argumento nomeado *compresslevel* também
   funciona para fluxos.

   Alterado na versão 3.14: O argumento nomeado *preset* também
   funciona para fluxos.

   Alterado na versão 3.15: O nível de compressão padrão foi reduzido
   para 6 (antes era 9). Esse é o nível padrão utilizado pela maioria
   das ferramentas de compressão e oferece um equilíbrio melhor entre
   velocidade e desempenho.

class tarfile.TarFile

   Classe para ler e escrever arquivos tar. Não use esta classe
   diretamente: use "tarfile.open()" em vez disso. Veja Objetos
   TarFile.

tarfile.is_tarfile(name)

   Return "True" if *name* is a tar archive file, that the "tarfile"
   module can read. *name* may be a "str", file, or file-like object.

   Alterado na versão 3.9: Suporte para arquivo e objetos arquivo ou
   similares.

The "tarfile" module defines the following exceptions:

exception tarfile.TarError

   Base class for all "tarfile" exceptions.

exception tarfile.ReadError

   Is raised when a tar archive is opened, that either cannot be
   handled by the "tarfile" module or is somehow invalid.

exception tarfile.CompressionError

   É levantada quando um método de compactação não é suportado ou
   quando os dados não podem ser decodificados corretamente.

exception tarfile.StreamError

   É levantada para as limitações típicas de objetos "TarFile" do tipo
   fluxo.

exception tarfile.ExtractError

   É levantada para erros *não fatais* ao usar "TarFile.extract()",
   mas somente se "TarFile.errorlevel""== 2".

exception tarfile.HeaderError

   É levantada por "TarInfo.frombuf()" se o buffer obtido for
   inválido.

exception tarfile.FilterError

   Classe base para membros recusados por filtros.

   tarinfo

      Informações sobre o membro que o filtro se recusou a extrair,
      como TarInfo.

exception tarfile.AbsolutePathError

   Levantada para recusar a extração de um membro com um caminho
   absoluto.

exception tarfile.OutsideDestinationError

   Levantada para recusar a extração de um membro fora do diretório de
   destino.

exception tarfile.SpecialFileError

   Levantada para recusar a extração de um arquivo especial (por
   exemplo, um dispositivo ou encadeamento).

exception tarfile.AbsoluteLinkError

   Levantada para recusar a extração de um link simbólico com um
   caminho absoluto.

exception tarfile.LinkOutsideDestinationError

   Levantada para recusar a extração de um link simbólico apontando
   para fora do diretório de destino.

exception tarfile.LinkFallbackError

   Levantada para recusar a emulação de um link (físico ou simbólico)
   extraindo outro membro do arquivo, quando esse membro seria
   rejeitado pelo local do filtro. A exceção levantada para rejeitar o
   membro substituto está disponível como "BaseException.__context__".

   Adicionado na versão 3.15.

As seguintes constantes estão disponíveis a nível de módulo:

tarfile.ENCODING

   A codificação de caracteres padrão: "'utf-8'" no Windows, o valor
   retornado por "sys.getfilesystemencoding()", caso contrário.

tarfile.REGTYPE
tarfile.AREGTYPE

   Um arquivo normal "type".

tarfile.LNKTYPE

   Um link (dentro do arquivo tar) "type".

tarfile.SYMTYPE

   Um link simbólico "type".

tarfile.CHRTYPE

   Um dispositivo especial de caracteres "type".

tarfile.BLKTYPE

   Um dispositivo especial de bloco "type".

tarfile.DIRTYPE

   Um diretório "type".

tarfile.FIFOTYPE

   Um dispositivo especial de FIFO "type".

tarfile.CONTTYPE

   Um arquivo contíguo "type".

tarfile.GNUTYPE_LONGNAME

   Um "type" de longname de GNU tar.

tarfile.GNUTYPE_LONGLINK

   Um "type" de longlink de GNU tar.

tarfile.GNUTYPE_SPARSE

   Um "type" de arquivo esparso de GNU tar.

Each of the following constants defines a tar archive format that the
"tarfile" module is able to create. See section Formatos tar
suportados for details.

tarfile.USTAR_FORMAT

   formato POSIX.1-1988 (ustar).

tarfile.GNU_FORMAT

   Formato tar GNU

tarfile.PAX_FORMAT

   formato POSIX.1-2001 (pax).

tarfile.DEFAULT_FORMAT

   O formato padrão para criação de arquivos. Atualmente, é
   "PAX_FORMAT".

   Alterado na versão 3.8: O formato padrão para novos arquivos foi
   alterado de "GNU_FORMAT" para "PAX_FORMAT".

Ver também:

  Módulo "zipfile"
     Documentação do módulo padrão "zipfile".

  Operações de arquivamento
     Documentação das funcionalidades de arquivamento de nível mais
     alto fornecidas pelo módulo padrão "shutil".

  Manual do GNU tar, Formato Básico do Tar
     Documentação para arquivos tar, incluindo extensões GNU tar.


Objetos TarFile
===============

O objeto "TarFile" fornece uma interface para um arquivo tar. Um
arquivo tar é uma sequência de blocos. Um membro do arquivo (um
arquivo armazenado) é composto por um bloco de cabeçalho seguido por
blocos de dados. É possível armazenar um arquivo em um arquivo tar
várias vezes. Cada membro do arquivo é representado por um objeto
"TarInfo", veja Objetos TarInfo para mais detalhes.

Um objeto "TarFile" pode ser usado como gerenciador de contexto em uma
instrução "with". Ele será fechado automaticamente quando o bloco for
concluído. Observe que, em caso de exceção, um arquivo aberto para
gravação não será finalizado; apenas o objeto arquivo usado
internamente será fechado. Consulte a seção Exemplos para um exemplo
de uso.

Adicionado na versão 3.2: Adicionado suporte para o protocolo de
gerenciamento de contexto.

class tarfile.TarFile(name=None, mode='r', fileobj=None, format=DEFAULT_FORMAT, tarinfo=TarInfo, dereference=False, ignore_zeros=False, encoding=ENCODING, errors='surrogateescape', pax_headers=None, debug=0, errorlevel=1, stream=False)

   Todos os argumentos a seguir são opcionais e também podem ser
   acessados como atributos de instância.

   *name* é o caminho do arquivo. *name* pode ser um *objeto caminho
   ou similar*. Pode ser omitido se *fileobj* for fornecido. Nesse
   caso, o atributo "name" do objeto arquivo será usado, se existir.

   O parâmetro *mode* pode ser "'r'" para ler de um arquivo existente,
   "'a'" para adicionar dados a um arquivo existente, "'w'" para criar
   um novo arquivo sobrescrevendo um existente ou "'x'" para criar um
   novo arquivo somente se ele ainda não existir.

   Se *fileobj* for fornecido, ele será usado para leitura ou gravação
   de dados. Se for possível determinar, *mode* será substituído pelo
   modo de *fileobj*. *fileobj* será usado a partir da posição 0.

   Nota:

     *fileobj* não é fechado quando "TarFile" é fechado.

   *format* controla o formato de gravação do arquivo. Deve ser uma
   das constantes "USTAR_FORMAT", "GNU_FORMAT" ou "PAX_FORMAT"
   definidas no nível do módulo. Durante a leitura, o formato será
   detectado automaticamente, mesmo que diferentes formatos estejam
   presentes em um único arquivo.

   O argumento *tarinfo* pode ser usado para substituir a classe
   padrão "TarInfo" por uma diferente.

   Se *dereference* for "False", adiciona links físicos e simbólicos
   ao arquivo. Se for "True", adiciona o conteúdo dos arquivos de
   destino ao arquivo. Isso não tem efeito em sistemas que não
   oferecem suporte a links simbólicos.

   Se *ignore_zeros* for "False", trata um bloco vazio como o fim do
   arquivo. Se for "True", ignora blocos vazios (e inválidos) e tenta
   obter o máximo de membros possível. Isso só é útil para ler
   arquivos concatenados ou corrompidos.

   O parâmetro *debug* pode ser configurado de "0" (nenhuma mensagem
   de depuração) até "3" (todas as mensagens de depuração). As
   mensagens são gravadas em "sys.stderr".

   *errorlevel* controla como os erros de extração são tratados, veja
   "o atributo correspondente".

   Os argumentos *encoding* e *errors* definem a codificação de
   caracteres a ser usada para leitura ou gravação do arquivo e como
   os erros de conversão serão tratados. As configurações padrão
   funcionarão para a maioria dos usuários. Consulta a seção Problemas
   de Unicode para obter informações detalhadas.

   O argumento *pax_headers* é um dicionário opcional de strings que
   será adicionado como um cabeçalho global pax se *format* for
   "PAX_FORMAT".

   Se *stream* estiver definido como "True", então, durante a leitura
   do arquivo, as informações sobre os arquivos no arquivo não serão
   armazenadas em cache, economizando memória.

   Alterado na versão 3.2: Usa "'surrogateescape'" como padrão para o
   argumento *errors*.

   Alterado na versão 3.5: O modo "'x'" (criação exclusiva) foi
   adicionado.

   Alterado na versão 3.6: O parâmetro *name* aceita um *objeto
   caminho ou similar*.

   Alterado na versão 3.13: Adiciona o parâmetro *stream*.

classmethod TarFile.open(...)

   Construtor alternativo. A função "tarfile.open()" é, na verdade, um
   atalho para este método de classe.

TarFile.getmember(name)

   Retorna um objeto "TarInfo" para o membro *name*. Se *name* não for
   encontrado no arquivo, uma exceção "KeyError" será levantada.

   Nota:

     Se um membro aparecer mais de uma vez no arquivo, presume-se que
     sua última ocorrência seja a versão mais atualizada.

TarFile.getmembers()

   Retorna os membros do arquivo como uma lista de objetos "TarInfo".
   A lista tem a mesma ordem que os membros no arquivo.

TarFile.getnames()

   Retorna os membros como uma lista com seus nomes. A lista está na
   mesma ordem que a lista retornada por "getmembers()".

TarFile.list(verbose=True, *, members=None)

   Envia um índice para "sys.stdout". Se *verbose* for "False", apenas
   os nomes dos membros serão exibidos. Se for "True", a saída será
   semelhante à do comando **ls -l**. Se o parâmetro opcional
   *members* for fornecido, ele deverá ser um subconjunto da lista
   retornada pelo método "getmembers()".

   Alterado na versão 3.5: Adicionado o parâmetro *members*.

TarFile.next()

   Retorna o próximo membro do arquivo como um objeto "TarInfo",
   quando "TarFile" é aberto para leitura. Retorna "None" se não
   houver mais nenhum disponível.

TarFile.extractall(path='.', members=None, *, numeric_owner=False, filter=None)

   Extract all members from the archive to the current working
   directory or directory *path*. If optional *members* is given, it
   must be a subset of the list returned by "getmembers()". Directory
   information like owner, modification time and permissions are set
   after all members have been extracted. This is done to work around
   two problems: A directory's modification time is reset each time a
   file is created in it. And, if a directory's permissions do not
   allow writing, extracting files to it will fail.

   If *numeric_owner* is "True", the uid and gid numbers from the
   tarfile are used to set the owner/group for the extracted files.
   Otherwise, the named values from the tarfile are used.

   The *filter* argument specifies how "members" are modified or
   rejected before extraction. See Filtros de extração for details. It
   is recommended to set this explicitly only if specific *tar*
   features are required, or as "filter='data'" to support Python
   versions with a less secure default (3.13 and lower).

   Aviso:

     Never extract archives from untrusted sources without prior
     inspection.Since Python 3.14, the default ("data") will prevent
     the most dangerous security issues. However, it will not prevent
     *all* unintended or insecure behavior. Read the Filtros de
     extração section for details.

   Alterado na versão 3.5: Adicionado o parâmetro *numeric_owner*.

   Alterado na versão 3.6: O parâmetro *path* aceita um *objeto
   caminho ou similar*.

   Alterado na versão 3.12: Adicionado o parâmetro *filter*.

   Alterado na versão 3.14: The *filter* parameter now defaults to
   "'data'".

TarFile.extract(member, path='', set_attrs=True, *, numeric_owner=False, filter=None)

   Extract a member from the archive to the current working directory,
   using its full name. Its file information is extracted as
   accurately as possible. *member* may be a filename or a "TarInfo"
   object. You can specify a different directory using *path*. *path*
   may be a *path-like object*. File attributes (owner, mtime, mode)
   are set unless *set_attrs* is false.

   The *numeric_owner* and *filter* arguments are the same as for
   "extractall()".

   Nota:

     The "extract()" method does not take care of several extraction
     issues. In most cases you should consider using the
     "extractall()" method.

   Aviso:

     Never extract archives from untrusted sources without prior
     inspection. See the warning for "extractall()" for details.

   Alterado na versão 3.2: Added the *set_attrs* parameter.

   Alterado na versão 3.5: Adicionado o parâmetro *numeric_owner*.

   Alterado na versão 3.6: O parâmetro *path* aceita um *objeto
   caminho ou similar*.

   Alterado na versão 3.12: Adicionado o parâmetro *filter*.

TarFile.extractfile(member)

   Extract a member from the archive as a file object. *member* may be
   a filename or a "TarInfo" object. If *member* is a regular file or
   a link, an "io.BufferedReader" object is returned. For all other
   existing members, "None" is returned. If *member* does not appear
   in the archive, "KeyError" is raised.

   Alterado na versão 3.3: Return an "io.BufferedReader" object.

   Alterado na versão 3.13: The returned "io.BufferedReader" object
   has the "mode" attribute which is always equal to "'rb'".

TarFile.errorlevel: int

   Se *errorlevel* for "0", os erros serão ignorados ao usar
   "TarFile.extract()" e "TarFile.extractall()". No entanto, eles
   aparecem como mensagens de erro na saída de depuração quando
   *debug* for maior que 0. Se "1" (o padrão), todos os erros *fatais*
   serão levantados como exceções "OSError" ou "FilterError". Se "2",
   todos os erros *não fatais* também serão levantados como exceções
   "TarError".

   Some exceptions, e.g. ones caused by wrong argument types or data
   corruption, are always raised.

   Custom extraction filters should raise "FilterError" for *fatal*
   errors and "ExtractError" for *non-fatal* ones.

   Note that when an exception is raised, the archive may be partially
   extracted. It is the user’s responsibility to clean up.

TarFile.extraction_filter

   Adicionado na versão 3.12.

   O filtro de extração usado como um padrão para o argumento *filter*
   de "extract()" e "extractall()".

   The attribute may be "None" or a callable. String names are not
   allowed for this attribute, unlike the *filter* argument to
   "extract()".

   If "extraction_filter" is "None" (the default), extraction methods
   will use the "data" filter by default.

   The attribute may be set on instances or overridden in subclasses.
   It also is possible to set it on the "TarFile" class itself to set
   a global default, although, since it affects all uses of *tarfile*,
   it is best practice to only do so in top-level applications or
   "site configuration". To set a global default this way, a filter
   function needs to be wrapped in "@staticmethod" to prevent
   injection of a "self" argument.

   Alterado na versão 3.14: The default filter is set to "data", which
   disallows some dangerous features such as links to absolute paths
   or paths outside of the destination. Previously, the default was
   equivalent to "fully_trusted".

TarFile.add(name, arcname=None, recursive=True, *, filter=None)

   Add the file *name* to the archive. *name* may be any type of file
   (directory, fifo, symbolic link, etc.). If given, *arcname*
   specifies an alternative name for the file in the archive.
   Directories are added recursively by default. This can be avoided
   by setting *recursive* to "False". Recursion adds entries in sorted
   order. If *filter* is given, it should be a function that takes a
   "TarInfo" object argument and returns the changed "TarInfo" object.
   If it instead returns "None" the "TarInfo" object will be excluded
   from the archive. See Exemplos for an example.

   Alterado na versão 3.2: Adicionado o parâmetro *filter*.

   Alterado na versão 3.7: Recursion adds entries in sorted order.

TarFile.addfile(tarinfo, fileobj=None)

   Add the "TarInfo" object *tarinfo* to the archive. If *tarinfo*
   represents a non zero-size regular file, the *fileobj* argument
   should be a *binary file*, and "tarinfo.size" bytes are read from
   it and added to the archive.  You can create "TarInfo" objects
   directly, or by using "gettarinfo()".

   Alterado na versão 3.13: *fileobj* must be given for non-zero-sized
   regular files.

TarFile.gettarinfo(name=None, arcname=None, fileobj=None)

   Create a "TarInfo" object from the result of "os.stat()" or
   equivalent on an existing file.  The file is either named by
   *name*, or specified as a *file object* *fileobj* with a file
   descriptor. *name* may be a *path-like object*.  If given,
   *arcname* specifies an alternative name for the file in the
   archive, otherwise, the name is taken from *fileobj*’s "name"
   attribute, or the *name* argument.  The name should be a text
   string.

   You can modify some of the "TarInfo"’s attributes before you add it
   using "addfile()". If the file object is not an ordinary file
   object positioned at the beginning of the file, attributes such as
   "size" may need modifying.  This is the case for objects such as
   "GzipFile". The "name" may also be modified, in which case
   *arcname* could be a dummy string.

   Alterado na versão 3.6: O parâmetro *name* aceita um *objeto
   caminho ou similar*.

TarFile.close()

   Close the "TarFile". In write mode, two finishing zero blocks are
   appended to the archive.

TarFile.pax_headers: dict

   Um dicionário contendo pares de chave-valor de cabeçalhos globais
   pax.


Objetos TarInfo
===============

A "TarInfo" object represents one member in a "TarFile". Aside from
storing all required attributes of a file (like file type, size, time,
permissions, owner etc.), it provides some useful methods to determine
its type. It does *not* contain the file's data itself.

"TarInfo" objects are returned by "TarFile"'s methods "getmember()",
"getmembers()" and "gettarinfo()".

Modifying the objects returned by "getmember()" or "getmembers()" will
affect all subsequent operations on the archive. For cases where this
is unwanted, you can use "copy.copy()" or call the "replace()" method
to create a modified copy in one step.

Several attributes can be set to "None" to indicate that a piece of
metadata is unused or unknown. Different "TarInfo" methods handle
"None" differently:

* The "extract()" or "extractall()" methods will ignore the
  corresponding metadata, leaving it set to a default.

* "addfile()" falhará.

* "list()" imprimirá uma string como um espaço reservado.

class tarfile.TarInfo(name='')

   Cria um objeto "TarInfo".

classmethod TarInfo.frombuf(buf, encoding, errors)

   Cria e retorna um objeto "TarInfo" a partir do buffer de string do
   parâmetro *buf*.

   Levanta "HeaderError" se o buffer for inválido.

classmethod TarInfo.fromtarfile(tarfile)

   Read the next member from the "TarFile" object *tarfile* and return
   it as a "TarInfo" object.

TarInfo.tobuf(format=DEFAULT_FORMAT, encoding=ENCODING, errors='surrogateescape')

   Create a string buffer from a "TarInfo" object. For information on
   the arguments see the constructor of the "TarFile" class.

   Alterado na versão 3.2: Usa "'surrogateescape'" como padrão para o
   argumento *errors*.

A "TarInfo" object has the following public data attributes:

TarInfo.name: str

   Nome do arquivo.

TarInfo.size: int

   Tamanho em bytes.

TarInfo.mtime: int | float

   Time of last modification in seconds since the epoch, as in
   "os.stat_result.st_mtime".

   Alterado na versão 3.12: Can be set to "None" for "extract()" and
   "extractall()", causing extraction to skip applying this attribute.

TarInfo.mode: int

   Permission bits, as for "os.chmod()".

   Alterado na versão 3.12: Can be set to "None" for "extract()" and
   "extractall()", causing extraction to skip applying this attribute.

TarInfo.type

   File type.  *type* is usually one of these constants: "REGTYPE",
   "AREGTYPE", "LNKTYPE", "SYMTYPE", "DIRTYPE", "FIFOTYPE",
   "CONTTYPE", "CHRTYPE", "BLKTYPE", "GNUTYPE_SPARSE".  To determine
   the type of a "TarInfo" object more conveniently, use the "is*()"
   methods below.

TarInfo.linkname: str

   Name of the target file name, which is only present in "TarInfo"
   objects of type "LNKTYPE" and "SYMTYPE".

   For symbolic links ("SYMTYPE"), the *linkname* is relative to the
   directory that contains the link. For hard links ("LNKTYPE"), the
   *linkname* is relative to the root of the archive.

TarInfo.uid: int

   ID do usuário do usuário que originalmente armazenou este membro.

   Alterado na versão 3.12: Can be set to "None" for "extract()" and
   "extractall()", causing extraction to skip applying this attribute.

TarInfo.gid: int

   ID do grupo do usuário que originalmente armazenou este membro.

   Alterado na versão 3.12: Can be set to "None" for "extract()" and
   "extractall()", causing extraction to skip applying this attribute.

TarInfo.uname: str

   Nome do usuário.

   Alterado na versão 3.12: Can be set to "None" for "extract()" and
   "extractall()", causing extraction to skip applying this attribute.

TarInfo.gname: str

   Nome do grupo.

   Alterado na versão 3.12: Can be set to "None" for "extract()" and
   "extractall()", causing extraction to skip applying this attribute.

TarInfo.chksum: int

   Cabeçalho de soma de verificação.

TarInfo.devmajor: int

   Número principal do dispositivo.

TarInfo.devminor: int

   Número menor do dispositivo.

TarInfo.offset: int

   O cabeçalho do tar começa aqui.

TarInfo.offset_data: int

   Os dados do arquivo começam aqui.

TarInfo.sparse

   Sparse member information.

TarInfo.pax_headers: dict

   A dictionary containing key-value pairs of an associated pax
   extended header.

TarInfo.replace(name=..., mtime=..., mode=..., linkname=..., uid=..., gid=..., uname=..., gname=..., deep=True)

   Adicionado na versão 3.12.

   Return a *new* copy of the "TarInfo" object with the given
   attributes changed. For example, to return a "TarInfo" with the
   group name set to "'staff'", use:

      new_tarinfo = old_tarinfo.replace(gname='staff')

   By default, a deep copy is made. If *deep* is false, the copy is
   shallow, i.e. "pax_headers" and any custom attributes are shared
   with the original "TarInfo" object.

A "TarInfo" object also provides some convenient query methods:

TarInfo.isfile()

   Return "True" if the "TarInfo" object is a regular file.

TarInfo.isreg()

   Igual a "isfile()".

TarInfo.isdir()

   Retorna "True" se for um diretório.

TarInfo.issym()

   Retorna "True" se for um link simbólico.

TarInfo.islnk()

   Retorna "True" se for um link físico.

TarInfo.ischr()

   Retorna "True" se for um caractere.

TarInfo.isblk()

   Return "True" if it is a block device.

TarInfo.isfifo()

   Retorna "True" se for um FIFO.

TarInfo.isdev()

   Return "True" if it is one of character device, block device or
   FIFO.


Filtros de extração
===================

Adicionado na versão 3.12.

The *tar* format is designed to capture all details of a UNIX-like
filesystem, which makes it very powerful. Unfortunately, the features
make it easy to create tar files that have unintended -- and possibly
malicious -- effects when extracted. For example, extracting a tar
file can overwrite arbitrary files in various ways (e.g.  by using
absolute paths, ".." path components, or symlinks that affect later
members).

In most cases, the full functionality is not needed. Therefore,
*tarfile* supports extraction filters: a mechanism to limit
functionality, and thus mitigate some of the security issues.

Aviso:

  None of the available filters blocks *all* dangerous archive
  features. Never extract archives from untrusted sources without
  prior inspection. See also Dicas para verificação adicional.

Ver também:

  **PEP 706**
     Contém a motivação e lógica escolhida para este design.

The *filter* argument to "TarFile.extract()" or "extractall()" can be:

* the string "'fully_trusted'": Honor all metadata as specified in the
  archive. Should be used if the user trusts the archive completely,
  or implements their own complex verification.

* the string "'tar'": Honor most *tar*-specific features (i.e.
  features of UNIX-like filesystems), but block features that are very
  likely to be surprising or malicious. See "tar_filter()" for
  details.

* the string "'data'": Ignore or block most features specific to UNIX-
  like filesystems. Intended for extracting cross-platform data
  archives. See "data_filter()" for details.

* "None" (default): Use "TarFile.extraction_filter".

  If that is also "None" (the default), the "'data'" filter will be
  used.

     Alterado na versão 3.14: The default filter is set to "data".
     Previously, the default was equivalent to "fully_trusted".

* A callable which will be called for each extracted member with a
  TarInfo describing the member and the destination path to where the
  archive is extracted (i.e. the same path is used for all members):

     filter(member: TarInfo, path: str, /) -> TarInfo | None

  The callable is called just before each member is extracted, so it
  can take the current state of the disk into account. It can:

  * return a "TarInfo" object which will be used instead of the
    metadata in the archive, or

  * return "None", in which case the member will be skipped, or

  * raise an exception to abort the operation or skip the member,
    depending on "errorlevel". Note that when extraction is aborted,
    "extractall()" may leave the archive partially extracted. It does
    not attempt to clean up.


Default named filters
---------------------

The pre-defined, named filters are available as functions, so they can
be reused in custom filters:

tarfile.fully_trusted_filter(member, path)

   Retorna *member* inalterado.

   This implements the "'fully_trusted'" filter.

tarfile.tar_filter(member, path)

   Implements the "'tar'" filter.

   * Strip leading slashes ("/" and "os.sep") from filenames.

   * Refuse to extract files with absolute paths (in case the name is
     absolute even after stripping slashes, e.g. "C:/foo" on Windows).
     This raises "AbsolutePathError".

   * Normalize filenames ("TarInfo.name") that contain ".." components
     using "os.path.normpath()". Note that this removes internal ".."
     components, which may change the meaning of the name if it
     traverses symbolic links.

   * Refuse to extract files whose absolute path (after following
     symlinks) would end up outside the destination. This raises
     "OutsideDestinationError".

   * Refuse to extract links (hard or soft) whose name refers to the
     destination directory itself. This raises
     "OutsideDestinationError". Note that such files are refused even
     on platforms that do not support symbolic links.

   * Clear high mode bits (setuid, setgid, sticky) and group/other
     write bits ("S_IWGRP" | "S_IWOTH").

   Return the modified "TarInfo" member.

   Alterado na versão 3.15: Filenames containing ".." components are
   now normalized.

tarfile.data_filter(member, path)

   Implements the "'data'" filter. In addition to what "tar_filter"
   does:

   * Normalize link targets ("TarInfo.linkname") using
     "os.path.normpath()". Note that this removes internal ".."
     components, which may change the meaning of the link if the path
     in "TarInfo.linkname" traverses symbolic links.

   * Refuse to extract links (hard or soft) that link to absolute
     paths, or ones that link outside the destination.

     This raises "AbsoluteLinkError" or "LinkOutsideDestinationError".

     Note that such files are refused even on platforms that do not
     support symbolic links.

   * Refuse to extract device files (including pipes). This raises
     "SpecialFileError".

   * Para arquivos comuns, incluindo links físicos:

     * Set the owner read and write permissions ("S_IRUSR" |
       "S_IWUSR").

     * Remove the group & other executable permission ("S_IXGRP" |
       "S_IXOTH") if the owner doesn’t have it ("S_IXUSR").

   * For other files (directories), set "mode" to "None", so that
     extraction methods skip applying permission bits.

   * Set user and group info ("uid", "gid", "uname", "gname") to
     "None", so that extraction methods skip setting it.

   Return the modified "TarInfo" member.

   Note that this filter does not block *all* dangerous archive
   features. See Dicas para verificação adicional  for details.

   Alterado na versão 3.15: Link targets are now normalized.


Filter errors
-------------

When a filter refuses to extract a file, it will raise an appropriate
exception, a subclass of "FilterError". This will abort the extraction
if "TarFile.errorlevel" is 1 or more. With "errorlevel=0" the error
will be logged and the member will be skipped, but extraction will
continue.


Dicas para verificação adicional
--------------------------------

Even with "filter='data'", *tarfile* is not suited for extracting
untrusted files without prior inspection. Among other issues, the pre-
defined filters do not prevent denial-of-service attacks. Users should
do additional checks.

Aqui está uma lista incompleta de itens a serem considerados:

* Extract to a "new temporary directory" to prevent e.g. exploiting
  pre-existing links, and to make it easier to clean up after a failed
  extraction.

* Disallow symbolic links if you do not need the functionality.

* When working with untrusted data, use external (e.g. OS-level)
  limits on disk, memory and CPU usage.

* Check filenames against an allow-list of characters (to filter out
  control characters, confusables, foreign path separators, and so
  on).

* Check that filenames have expected extensions (discouraging files
  that execute when you “click on them”, or extension-less files like
  Windows special device names).

* Limit the number of extracted files, total size of extracted data,
  filename length (including symlink length), and size of individual
  files.

* Check for files that would be shadowed on case-insensitive
  filesystems.

Observe também que:

* Tar files may contain multiple versions of the same file. Later ones
  are expected to overwrite any earlier ones. This feature is crucial
  to allow updating tape archives, but can be abused maliciously.

* *tarfile* does not protect against issues with “live” data, e.g. an
  attacker tinkering with the destination (or source) directory while
  extraction (or archiving) is in progress.


Suporte a versões mais antigas do Python
----------------------------------------

Extraction filters were added to Python 3.12, but may be backported to
older versions as security updates. To check whether the feature is
available, use e.g. "hasattr(tarfile, 'data_filter')" rather than
checking the Python version.

The following examples show how to support Python versions with and
without the feature. Note that setting "extraction_filter" will affect
any subsequent operations.

* Fully trusted archive:

     my_tarfile.extraction_filter = (lambda member, path: member)
     my_tarfile.extractall()

* Use the "'data'" filter if available, but revert to Python 3.11
  behavior ("'fully_trusted'") if this feature is not available:

     my_tarfile.extraction_filter = getattr(tarfile, 'data_filter',
                                            (lambda member, path: member))
     my_tarfile.extractall()

* Use o filtro "'data'"; *fail* se ele não estiver disponível:

     my_tarfile.extractall(filter=tarfile.data_filter)

  ou:

     my_tarfile.extraction_filter = tarfile.data_filter
     my_tarfile.extractall()

* Use o filtro "'data'"; *warn* se ele não estiver disponível:

     if hasattr(tarfile, 'data_filter'):
         my_tarfile.extractall(filter='data')
     else:
         # remove this when no longer needed
         warn_the_user('Extracting may be unsafe; consider updating Python')
         my_tarfile.extractall()


Stateful extraction filter example
----------------------------------

While *tarfile*'s extraction methods take a simple *filter* callable,
custom filters may be more complex objects with an internal state. It
may be useful to write these as context managers, to be used like
this:

   with StatefulFilter() as filter_func:
       tar.extractall(path, filter=filter_func)

Such a filter can be written as, for example:

   class StatefulFilter:
       def __init__(self):
           self.file_count = 0

       def __enter__(self):
           return self

       def __call__(self, member, path):
           self.file_count += 1
           return member

       def __exit__(self, *exc_info):
           print(f'{self.file_count} files extracted')


Interface de Linha de Comando
=============================

Adicionado na versão 3.4.

The "tarfile" module provides a simple command-line interface to
interact with tar archives.

If you want to create a new tar archive, specify its name after the
"-c" option and then list the filename(s) that should be included:

   $ python -m tarfile -c monty.tar  spam.txt eggs.txt

Passar um diretório também é aceito:

   $ python -m tarfile -c monty.tar life-of-brian_1979/

If you want to extract a tar archive into the current directory, use
the "-e" option:

   $ python -m tarfile -e monty.tar

You can also extract a tar archive into a different directory by
passing the directory's name:

   $ python -m tarfile -e monty.tar  other-dir/

For a list of the files in a tar archive, use the "-l" option:

   $ python -m tarfile -l monty.tar


Opções de linha de comando
--------------------------

-l <tarfile>
--list <tarfile>

   Lista os arquivos em um arquivo tar.

-c <tarfile> <source1> ... <sourceN>
--create <tarfile> <source1> ... <sourceN>

   Cria um arquivo tar a partir dos arquivos de origem.

-e <tarfile> [<output_dir>]
--extract <tarfile> [<output_dir>]

   Extract tarfile into the current directory if *output_dir* is not
   specified.

-t <tarfile>
--test <tarfile>

   Test whether the tarfile is valid or not.

-v, --verbose

   Saída detalhada.

--filter <filtername>

   Specifies the *filter* for "--extract". See Filtros de extração for
   details. Only string names are accepted (that is, "fully_trusted",
   "tar", and "data").


Exemplos
========


Reading examples
----------------

How to extract an entire tar archive to the current working directory:

   import tarfile
   tar = tarfile.open("sample.tar.gz")
   tar.extractall(filter='data')
   tar.close()

How to extract a subset of a tar archive with "TarFile.extractall()"
using a generator function instead of a list:

   import os
   import tarfile

   def py_files(members):
       for tarinfo in members:
           if os.path.splitext(tarinfo.name)[1] == ".py":
               yield tarinfo

   tar = tarfile.open("sample.tar.gz")
   tar.extractall(members=py_files(tar))
   tar.close()

How to read a gzip compressed tar archive and display some member
information:

   import tarfile
   tar = tarfile.open("sample.tar.gz", "r:gz")
   for tarinfo in tar:
       print(tarinfo.name, "is", tarinfo.size, "bytes in size and is ", end="")
       if tarinfo.isreg():
           print("a regular file.")
       elif tarinfo.isdir():
           print("a directory.")
       else:
           print("something else.")
   tar.close()


Writing examples
----------------

How to create an uncompressed tar archive from a list of filenames:

   import tarfile
   tar = tarfile.open("sample.tar", "w")
   for name in ["foo", "bar", "quux"]:
       tar.add(name)
   tar.close()

The same example using the "with" statement:

   import tarfile
   with tarfile.open("sample.tar", "w") as tar:
       for name in ["foo", "bar", "quux"]:
           tar.add(name)

How to create and write an archive to stdout using "sys.stdout.buffer"
in the *fileobj* parameter in "TarFile.add()":

   import sys
   import tarfile
   with tarfile.open("sample.tar.gz", "w|gz", fileobj=sys.stdout.buffer) as tar:
       for name in ["foo", "bar", "quux"]:
           tar.add(name)

How to create an archive and reset the user information using the
*filter* parameter in "TarFile.add()":

   import tarfile
   def reset(tarinfo):
       tarinfo.uid = tarinfo.gid = 0
       tarinfo.uname = tarinfo.gname = "root"
       return tarinfo
   tar = tarfile.open("sample.tar.gz", "w:gz")
   tar.add("foo", filter=reset)
   tar.close()


Formatos tar suportados
=======================

There are three tar formats that can be created with the "tarfile"
module:

* The POSIX.1-1988 ustar format ("USTAR_FORMAT"). It supports
  filenames up to a length of at best 256 characters and linknames up
  to 100 characters. The maximum file size is 8 GiB. This is an old
  and limited but widely supported format.

* The GNU tar format ("GNU_FORMAT"). It supports long filenames and
  linknames, files bigger than 8 GiB and sparse files. It is the de
  facto standard on GNU/Linux systems. "tarfile" fully supports the
  GNU tar extensions for long names, sparse file support is read-only.

* The POSIX.1-2001 pax format ("PAX_FORMAT"). It is the most flexible
  format with virtually no limits. It supports long filenames and
  linknames, large files and stores pathnames in a portable way.
  Modern tar implementations, including GNU tar, bsdtar/libarchive and
  star, fully support extended *pax* features; some old or
  unmaintained libraries may not, but should treat *pax* archives as
  if they were in the universally supported *ustar* format. It is the
  current default format for new archives.

  It extends the existing *ustar* format with extra headers for
  information that cannot be stored otherwise. There are two flavours
  of pax headers: Extended headers only affect the subsequent file
  header, global headers are valid for the complete archive and affect
  all following files. All the data in a pax header is encoded in
  *UTF-8* for portability reasons.

There are some more variants of the tar format which can be read, but
not created:

* The ancient V7 format. This is the first tar format from Unix
  Seventh Edition, storing only regular files and directories. Names
  must not be longer than 100 characters, there is no user/group name
  information. Some archives have miscalculated header checksums in
  case of fields with non-ASCII characters.

* The SunOS tar extended format. This format is a variant of the
  POSIX.1-2001 pax format, but is not compatible.


Problemas de Unicode
====================

The tar format was originally conceived to make backups on tape drives
with the main focus on preserving file system information. Nowadays
tar archives are commonly used for file distribution and exchanging
archives over networks. One problem of the original format (which is
the basis of all other formats) is that there is no concept of
supporting different character encodings. For example, an ordinary tar
archive created on a *UTF-8* system cannot be read correctly on a
*Latin-1* system if it contains non-*ASCII* characters. Textual
metadata (like filenames, linknames, user/group names) will appear
damaged. Unfortunately, there is no way to autodetect the encoding of
an archive. The pax format was designed to solve this problem. It
stores non-ASCII metadata using the universal character encoding
*UTF-8*.

The details of character conversion in "tarfile" are controlled by the
*encoding* and *errors* keyword arguments of the "TarFile" class.

*encoding* defines the character encoding to use for the metadata in
the archive. The default value is "sys.getfilesystemencoding()" or
"'ascii'" as a fallback. Depending on whether the archive is read or
written, the metadata must be either decoded or encoded. If *encoding*
is not set appropriately, this conversion may fail.

The *errors* argument defines how characters are treated that cannot
be converted. Possible values are listed in section Error Handlers.
The default scheme is "'surrogateescape'" which Python also uses for
its file system calls, see Nomes de arquivos, argumentos de linha de
comando e variáveis de ambiente.

For "PAX_FORMAT" archives (the default), *encoding* is generally not
needed because all the metadata is stored using *UTF-8*. *encoding* is
only used in the rare cases when binary pax headers are decoded or
when strings with surrogate characters are stored.
