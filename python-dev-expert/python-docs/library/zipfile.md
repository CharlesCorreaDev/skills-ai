"zipfile" --- Trabalha com arquivos ZIP
***************************************

**Código-fonte:** Lib/zipfile/

======================================================================

O formato de arquivo ZIP é um padrão de compactação e arquivamento.
Este módulo fornece ferramentas para criar, ler, escrever, adicionar,
e listar um arquivo ZIP. Qualquer uso avançado deste módulo vai exigir
um entendimento do formato, como definido nas Notas de Aplicação do
PKZIP.

Esse módulo não trata arquivos ZIP multiparte. Ele pode manipular
arquivos ZIP que usam as extensões ZIP64 (ou seja arquivos ZIP com
tamanho maior do que 4 Gb). Ele suporta descriptografia de arquivos
criptografados dentro do ZIP, mas atualmente não pode criar um arquivo
criptografado. A descriptografia é extremamente lenta pois é
implementada em Python nativo ao invés de C.

Lidar com arquivos compactados requer *módulos opcionais*. tal como
"zlib", "bz2", "lzma" e "compression.zstd". Se algumo desses estiver
faltando na sua cópia do CPython, procure a documentação do seu
distribuidor (ou seja, quem lhe forneceu o Python). Se você for o
distribuidor, consulte Requisitos para módulos opcionais.

Este módulo define os seguintes itens:

exception zipfile.BadZipFile

   Este erro é levantado para arquivos ZIP corrompidos.

   Adicionado na versão 3.2.

exception zipfile.BadZipfile

   Alias para "BadZipFile", para compatibilidade com versões mais
   antigas de Python.

   Descontinuado desde a versão 3.2.

exception zipfile.LargeZipFile

   Este erro é levantado quando um arquivo ZIP precisa da
   funcionalidade ZIP64 que não está habilitada.

class zipfile.ZipFile

   A classe para ler e escrever arquivos ZIP. Veja a seção Objetos
   ZipFile para detalhes do construtor.

class zipfile.Path

   Classe que implementa um subconjunto da interface fornecida por
   "pathlib.Path", incluindo a interface completa
   "importlib.resources.abc.Traversable".

   Adicionado na versão 3.8.

class zipfile.PyZipFile

   Classe para criar arquivos ZIP contendo bibliotecas Python.

class zipfile.ZipInfo(filename='NoName', date_time=(1980, 1, 1, 0, 0, 0))

   Class used to represent information about a member of an archive.
   Instances of this class are returned by the "getinfo()" and
   "infolist()" methods of "ZipFile" objects.  Most users of the
   "zipfile" module will not need to create these, but only use those
   created by this module. *filename* should be the full name of the
   archive member, and *date_time* should be a tuple containing six
   fields which describe the time of the last modification to the
   file; the fields are described in section Objetos ZipInfo.

   Alterado na versão 3.13: Um atributo público "compress_level" foi
   adicionado para expor o "_compresslevel" anteriormente protegido. O
   nome protegido mais antigo continua a funcionar como uma
   propriedade para compatibilidade com versões anteriores.

   _for_archive(archive)

      Resolve os atributos date_time, compression e external para
      padrões adequados, conforme usado por "ZipFile.writestr()".

      Retorna self para encadeamento.

      Adicionado na versão 3.14.

zipfile.is_zipfile(filename)

   Retorna "True" se *filename* é um arquivo ZIP válido baseado no seu
   "magic number", caso contrário retorna "False". *filename* pode ser
   um arquivo ou um objeto arquivo ou similar também.

   Alterado na versão 3.1: Suporte para arquivo e objetos arquivo ou
   similares.

zipfile.ZIP_STORED

   Código numérico para um membro de um arquivo descompactado

zipfile.ZIP_DEFLATED

   Código numérico para o método de compactação usual. Requer o módulo
   "zlib" .

zipfile.ZIP_BZIP2

   Código numérico para o método de compactação BZIP2. Requer o módulo
   "bz2".

   Adicionado na versão 3.3.

zipfile.ZIP_LZMA

   Código numérico para o método de compactação LZMA. Requer o módulo
   "lzma".

   Adicionado na versão 3.3.

zipfile.ZIP_ZSTANDARD

   Código numérico para a compactação com Zstandard. Requer o módulo
   "compression.zstd".

   Nota:

     No APPNOTE 6.3.7, o ID do método "20" foi atribuído à compactação
     Zstandard. No APPNOTE 6.3.8, esse ID foi alterado para o ID do
     método "93" para evitar conflitos, com o ID do método "20" sendo
     descontinuado. Para compatibilidade, o módulo "zipfile" lê ambos
     os IDs de método, mas gravará apenas dados com o ID do método
     "93".

   Adicionado na versão 3.14.

Nota:

  A especificação do formato ZIP incluiu suporte para compactação
  bzip2 desde 2001, para compactação LZMA desde 2006 e para
  compactação Zstandard desde 2020. Porém, algumas ferramentas
  (incluindo versões mais antigas de Python) não suportam esses
  métodos de compactação, e podem recusar processar o arquivo ZIP como
  um todo, ou falhar em extrair arquivos individuais.

Ver também:

  Notas da Aplicação do PKZIP
     Documentação do formato de arquivo ZIP feita por Phil Katz,
     criador do formato e dos algoritmos usados.

  Site do Info-ZIP
     Informações sobre o programas de arquivamento e desenvolvimento
     de bibliotecas do projeto Info-ZIP.


Objetos ZipFile
===============

class zipfile.ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=None, *, strict_timestamps=True, metadata_encoding=None)

   Abre um arquivo ZIP, onde *file* pode ser um caminho para um
   arquivo (uma string), um objeto arquivo ou similar, ou um *objeto
   caminho ou similar*.

   O parâmetro *mode* deve ser "'r'" para ler um arquivo existente,
   "'w'" para truncar e gravar um novo arquivo, "'a'" para adicionar a
   um arquivo existente, ou "'x'" exclusivamente para criar e gravar
   um novo arquivo. Se o *mode* é "'x'" e *file* se refere a um
   arquivo existente, um "FileExistsError" vai ser levantado. Se o
   *mode* é "'a'" e *file* se refere a um arquivo ZIP existente, então
   arquivos adicionais são adicionados ao mesmo. Se *file* não se
   refere a um arquivo ZIP, então um novo arquivo ZIP é adicionado ao
   arquivo. Isso diz respeito a adicionar um arquivo ZIP a um outro
   arquivo (como por exemplo "python.exe"). Se o *mode* é "'a'" e o
   arquivo não existe, ele será criado. Se o *mode* é "'r'" ou "'a'",
   o arquivo deve ser percorrível.

   *compression* é o método de compactação ZIP para usar ao escrever o
   arquivo, e deve ser "ZIP_STORED", "ZIP_DEFLATED", "ZIP_BZIP2",
   "ZIP_LZMA" e "ZIP_ZSTANDARD"; valores desconhecidos devem causar
   "NotImplementedError" ser levantada. Se "ZIP_DEFLATED",
   "ZIP_BZIP2", "ZIP_LZMA" ou "ZIP_ZSTANDARD" for especificado mas o
   módulo correspondente ("zlib", "bz2", "lzma" e "compression.zstd")
   não estiver disponível, é levantada uma exceção "RuntimeError". O
   valor padrão é "ZIP_STORED".

   If *allowZip64* is "True" (the default) zipfile will create ZIP
   files that use the ZIP64 extensions when the zipfile is larger than
   4 GiB. If it is "false" "zipfile" will raise an exception when the
   ZIP file would require ZIP64 extensions.

   O parâmetro *compresslevel* controla o nível de compactação para
   usar ao gravar no arquivo ZIP. Quando usado "ZIP_STORED" ou
   "ZIP_LZMA" não tem efeito. Quando usado "ZIP_DEFLATED" inteiros de
   "0" a "9" são aceitos (veja "zlib" para mais informações). Quando
   usado "ZIP_BZIP2" inteiros de "1" a "9" são aceitos (veja "bz2"
   para mais informações). Ao usar "ZIP_ZSTANDARD", os inteiros
   "-131072" a "22" são comumente aceitos (consulte
   "CompressionParameter.compression_level" para obter mais
   informações sobre como recuperar valores válidos e seus
   significados).

   O argumento *strict_timestamps*, quando definido como "False",
   permite compactar arquivos anteriores a 1980-01-01 com o custo de
   definir o carimbo de data/hora para 1980-01-01. Comportamento
   semelhante ocorre com arquivos mais recentes que 2107-12-31, o
   carimbo de data/hora também é definido como o limite.

   Quando o modo é "'r'", *metadata_encoding* pode ser definido como o
   nome de um codec, que será usado para decodificar metadados, como
   os nomes dos membros e comentários ZIP.

   Se o arquivo é criado com modo "'w'", "'x'" ou "'a'" e então
   "closed" sem adicionar nada ao arquivo, a estrutura própria para um
   arquivo vazio será escrita no arquivo.

   ZipFile também é um gerenciador de contexto e portanto suporta a
   instrução "with". Neste exemplo, *myzip* é fechado ao final da
   execução da instrução "with" -- mesmo que ocorra uma exceção:

      with ZipFile('spam.zip', 'w') as myzip:
          myzip.write('eggs.txt')

   Nota:

     *metadata_encoding* é uma configuração em toda a instância para o
     ZipFile. Não é possível definir isso em uma base por membro.Este
     atributo é uma solução alternativa para implementações legadas
     que produzem arquivos com nomes na codificação da localidade
     atual ou página de código (principalmente no Windows). De acordo
     com o padrão .ZIP, a codificação dos metadados pode ser
     especificada como página de código IBM (padrão) ou UTF-8 por meio
     de um sinalizador no cabeçalho do arquivo. Esse sinalizador tem
     precedência sobre *metadata_encoding*, que é uma extensão
     específica do Python.

   Alterado na versão 3.2: Adicionado o uso de "ZipFile" como um
   gerenciador de contexto.

   Alterado na versão 3.3: Adicionado suporte para compactação "bzip2"
   e "lzma".

   Alterado na versão 3.4: Extensões ZIP64 são habilitadas por padrão.

   Alterado na versão 3.5: Adicionado suporte para escrever em streams
   não percorríveis. Adicionado suporte ao modo "'x'".

   Alterado na versão 3.6: Anteriormente, um simples "RuntimeError"
   era levantado para valores de compactação desconhecidos.

   Alterado na versão 3.6.2: O parâmetro *file* aceita um *objeto
   caminho ou similar*.

   Alterado na versão 3.7: Adicionado o parâmetro *compresslevel*.

   Alterado na versão 3.8: O parâmetro somente-nomeado
   *strict_timestamps*.

   Alterado na versão 3.11: Adicionado suporte para especificar a
   codificação do nome do membro ao ler metadados no diretório e
   cabeçalhos de arquivo do arquivo zip.

ZipFile.close()

   Fecha o arquivo. Você deve chamar "close()" antes de sair do seu
   programa ou registros essenciais não serão gravados.

ZipFile.getinfo(name)

   Retorna um objeto "ZipInfo" com informações sobre o *name* do
   membro do arquivo. Chamar "getinfo()" para um nome não encontrado
   no arquivo levanta um "KeyError".

ZipFile.infolist()

   Retorna uma lista contendo um objeto "ZipInfo" para cada membro do
   arquivo. Os objetos estão na mesma ordem das entradas no arquivo
   ZIP em disco se um arquivo existente foi aberto.

ZipFile.namelist()

   Retorna uma lista de membros do arquivo por nome.

ZipFile.open(name, mode='r', pwd=None, *, force_zip64=False)

   Acessa um membro do arquivo como um objeto binário arquivo ou
   similar. *name* pode ser o nome de um arquivo membro ou um objeto
   "ZipInfo". O parâmetro *mode*, se informado, deve ser "'r'" (valor
   padrão) or "'w'". *pwd* é a senha usada para descriptografar
   arquivos ZIP criptografados como um objeto "bytes".

   "open()" também é um gerenciador de contexto e, portanto, suporta a
   instrução "with":

      with ZipFile('spam.zip') as myzip:
          with myzip.open('eggs.txt') as myfile:
              print(myfile.read())

   Com *mode* "'r'" o objeto arquivo ou similar ("ZipExtFile") é
   somente leitura e fornece os seguintes métodos: "read()",
   "readline()", "readlines()", "seek()", "tell()", "__iter__()",
   "__next__()". Esses objetos podem operar independentemente do
   ZipFile.

   Com "mode='w'", é retornado um manipulador de arquivo, que suporta
   o método "write()". Quando um manipulador de arquivo modificável é
   aberto, tentativas de ler ou gravar outros arquivos no arquivo ZIP
   levanta um "ValueError".

   Em ambos os casos o objeto arquivo ou similar também possui
   atributos "name", que é equivalente ao nome de um arquivo dentro do
   arquivo, e "mode", que é "'rb'" ou "'wb'" dependendo do modo de
   entrada.

   Ao gravar um arquivo, se o tamanho do arquivo não é conhecido mas
   pode exceder 2 GiB, passe "force_zip64=True" para assegurar que o
   formato do header é capaz de suportar arquivos grandes. Se o
   tamanho do arquivo é conhecido, construa um objeto "ZipInfo" com
   "file_size" informado, então use-o como parâmetro *name*.

   Nota:

     Os métodos "open()", "read()" e "extract()" podem receber um nome
     de arquivo ou um objeto "ZipInfo". Você vai gostar disso quando
     tentar ler um arquivo ZIP que contém membros com nomes
     duplicados.

   Alterado na versão 3.6: Removido suporte ao "mode='U'". Uso de
   "io.TextIOWrapper" para leitura de arquivos texto compactados em
   modo de *novas linhas universais*.

   Alterado na versão 3.6: "ZipFile.open()" agora pode ser usado para
   escrever arquivos no aquivo compactado com a opção "mode='w'".

   Alterado na versão 3.6: Chama "open()" em um ZipFile fechado
   levanta um "ValueError". Anteriormente, um "RuntimeError" era
   levantado.

   Alterado na versão 3.13: Adicionados atributos "name" e "mode" para
   o objeto arquivo ou similar gravável. O valor do atributo "mode"
   para o objeto arquivo ou similar legível foi alterado de "'r'" para
   "'rb'".

ZipFile.extract(member, path=None, pwd=None)

   Extrai um membro do arquivo para o diretório atual; *member* deve
   ser o nome completo ou um objeto "ZipInfo". A informação do arquivo
   é extraída com maior precisão possível. *path* especifica um outro
   diretório em que deve ser gravado. *member* pode ser um nome de
   arquivo ou um objeto "ZipInfo". *pwd* é a senha usada para
   criptografar arquivos como um objeto "bytes".

   Retorna o caminho normalizado criado (um diretório ou novo
   arquivo).

   Nota:

     Se um nome de arquivo membro é um caminho absoluto, o drive/UNC e
     (contra)barras no início serão removidos, por exemplo:
     "///foo/bar" se torna "foo/bar" no Unix, e "C:\foo\bar" vira
     "foo\bar" no Windows. E todos os componentes "".."" no nome de um
     arquivo membro serão removidos, por exemplo:
     "../../foo../../ba..r" vira "foo../ba..r". No Windows caracteres
     ilegais (":", "<", ">", "|", """, "?", and "*") são substituídos
     por underscore ("_").

   Alterado na versão 3.6: Chama "extract()" em um ZipFile fechado
   levanto um "ValueError". Anteriormente, um "RuntimeError" era
   levantado.

   Alterado na versão 3.6.2: O parâmetro *path* aceita um *objeto
   caminho ou similar*.

ZipFile.extractall(path=None, members=None, pwd=None)

   Extrai todos os membros de um arquivo para o diretório atual.
   *path* especifica um diretório diferente para gravar os arquivos
   extraídos. *members* é opcional e deve ser um sub-conjunto da lista
   retornada por "namelist()". *pwd* é uma senha usada para
   criptografar arquivos como um objeto "bytes".

   Aviso:

     Never extract archives from untrusted sources without prior
     inspection. It is possible that files are created outside of
     *path*, for example, members that have absolute filenames or
     filenames with ".." components. This module attempts to prevent
     that. See "extract()" note.

   Alterado na versão 3.6: Chama "extractall()" em um ZipFile fechado
   levanta um "ValueError". Anteriormente, um "RuntimeError" era
   levantado.

   Alterado na versão 3.6.2: O parâmetro *path* aceita um *objeto
   caminho ou similar*.

ZipFile.printdir()

   Imprime a tabela de conteúdos de um arquivo para "sys.stdout".

ZipFile.setpassword(pwd)

   Define *pwd* (um objeto "bytes") como senha padrão para extrair
   arquivos criptografados.

ZipFile.read(name, pwd=None)

   Retorna os bytes do arquivo *name* no arquivo compactado. *name* é
   o nome do arquivo no arquivo compactado, ou um objeto "ZipInfo". O
   arquivo compactado deve estar aberto para leitura ou acréscimo.
   *pwd* é a senha usada para arquivos criptografados como um objeto
   "bytes" e, se especificada, substitui a senha padrão configurada
   com "setpassword()". Chamar "read()" em um ZipFile que use um
   método de compactação diferente de "ZIP_STORED", "ZIP_DEFLATED",
   "ZIP_BZIP2", "ZIP_LZMA" e "ZIP_ZSTANDARD" levanta um
   "NotImplementedError". Um erro também é levantado se o módulo de
   compactação correspondente não está disponível.

   Alterado na versão 3.6: Chama "read()" em um ZipFile fechado
   levanta um "ValueError". Anteriormente, um "RuntimeError" era
   levantado.

ZipFile.testzip()

   Lê todos os arquivos no arquivo compactado e verifica seus CRC's e
   cabeçalhos de arquivo. Retorna o nome do primeiro arquivo
   corrompido, or então retorna "None".

   Alterado na versão 3.6: Chama "testzip()" em um ZipFile fechado
   levanta um "ValueError". Anteriormente, um "RuntimeError" era
   levantado.

ZipFile.write(filename, arcname=None, compress_type=None, compresslevel=None)

   Grava o arquivo chamado *filename* no arquivo compactado, dando ao
   arquivo compactado o nome *arcname* (por padrão, este é o mesmo de
   *filename*, mas sem a letra do drive e com separadores removidos do
   início do nome). Se informado, *compress_type* sobrescreve o valor
   dado ao parâmetro *compression* do construtor para a nova entrada.
   Da mesma forma, *compresslevel* vai sobrescrever o construtor se
   informado. O arquivo compactado deve ser aberto em modo "'w'",
   "'x'" ou "'a'".

   Nota:

     O padrão de arquivo ZIP historicamente não especificava uma
     codificação de metadados, mas recomendava fortemente o CP437 (a
     codificação original do PC da IBM) para interoperabilidade.
     Versões recentes permitem o uso de (somente) UTF-8. Neste módulo,
     o UTF-8 será automaticamente usado para escrever os nomes dos
     membros se eles contiverem caracteres não ASCII. Não é possível
     escrever nomes de membros em qualquer codificação que não seja
     ASCII ou UTF-8.

   Nota:

     Nomes de arquivo compactado devem ser relativos a raiz do mesmo,
     isto é, não devem começar com um separador de caminho.

   Nota:

     Se "arcname" (ou "filename", se "arcname" não for informado)
     contém um byte nulo, o nome do arquivo no arquivo compactado será
     truncado no byte nulo.

   Nota:

     Uma barra inicial no nome do arquivo pode fazer com que o arquivo
     seja impossível de abrir em alguns programas zip em sistemas
     Windows.

   Alterado na versão 3.6: Chama "write()" em um ZipFile criado com
   modo "'r'" ou em um ZipFile fechado levanta um "ValueError".
   Anteriormente, um "RuntimeError" era levantado

ZipFile.writestr(zinfo_or_arcname, data, compress_type=None, compresslevel=None)

   Grava um arquivo no arquivo compactado. O conteúdo é *data*, que
   pode ser uma instância de "str" ou de "bytes"; Se é uma "str", ela
   é encodada como UTF-8 primeiro. *zinfo_or_arcname* é o nome que
   será dado ao arquivo no arquivo compactado, ou uma instância de
   "ZipInfo". Se é uma instância, pelo menos o nome do arquivo, a
   data, e a hora devem ser informados. Se é um nome, a data e hora
   recebem a data e hora atual. O arquivo compactado deve ser aberto
   em modo "'w'", "'x'" ou "'a'".

   Se informado, *compress_type* sobrescreve o valor do parâmetro
   *compression* do construtor para a nova entrada, ou no
   *zinfo_or_arcname* (se é uma instância de "ZipInfo"). Da mesma
   forma, *compresslevel* vai sobrescrever o construtor se informado.

   Nota:

     Quando é passada uma instância de "ZipInfo" ou o parâmetro
     *zinfo_or_arcname*, o método de compactação usado será aquele
     especificado no *compress_type* da instância de "ZipInfo". Por
     padrão, o construtor da classe "ZipInfo" seta este membro para
     "ZIP_STORED".

   Alterado na versão 3.2: O argumento *compress_type*.

   Alterado na versão 3.6: Chama "writestr()" em um ZipFile criado com
   modo "'r'" ou em um ZipFile fechado levanta um "ValueError".
   Anteriormente, um "RuntimeError" era levantado.

   Alterado na versão 3.14: Now respects the "SOURCE_DATE_EPOCH"
   environment variable. If set, it uses this value as the
   modification timestamp for the file written into the ZIP archive,
   instead of using the current time.

ZipFile.mkdir(zinfo_or_directory, mode=511)

   Cria um diretório dentro do arquivo. Se *zinfo_or_directory* for
   uma string, um diretório é criado dentro do arquivo com o modo
   especificado no argumento *mode*. No entanto, se
   *zinfo_or_directory* for uma instância "ZipInfo", o argumento
   *mode* é ignorado.

   O arquivo deve ser aberto com o modo "'w'", "'x'" ou "'a'".

   Adicionado na versão 3.11.

Os seguintes atributos de dados também estão disponíveis:

ZipFile.filename

   Nome do arquivo ZIP.

ZipFile.debug

   O nível de saída de debug para usar. Pode ser setado de "0" (valor
   padrão, sem nenhuma saída) a "3" (com mais saída). A informação de
   debug é escrita em "sys.stdout".

ZipFile.comment

   O comentário associado ao arquivo ZIP como um objeto "bytes". Se
   atribuir um comentário a uma instância "ZipFile" criada com o modo
   "'w'", "'x'" ou "'a'", não deve ser maior que 65535 bytes.
   Comentários mais longos do que isso serão truncados.


Objetos Path
============

class zipfile.Path(root, at='')

   Construir um objeto Path a partir de um arquivo zip "root" (que
   pode ser uma instância "ZipFile" ou "file" adequado para passar
   para o construtor "ZipFile").

   "at" especifica a localização deste caminho dentro do arquivo zip,
   por exemplo, "dir/arquivo.txt", "dir/" ou "". O padrão é a string
   vazia, indicando a raiz.

   Nota:

     The "Path" class does not sanitize filenames within the ZIP
     archive. Unlike the "ZipFile.extract()" and
     "ZipFile.extractall()" methods, it is the caller's responsibility
     to validate or sanitize filenames to prevent path traversal
     vulnerabilities (for example, absolute paths or paths with ".."
     components). When handling untrusted archives, consider resolving
     filenames using "os.path.abspath()" and checking against the
     target directory with "os.path.commonpath()".

Objetos Path expõem os seguintes recursos de objetos "pathlib.Path":

Objetos Path podem ser percorridos usando o operador "/" ou
"joinpath".

Path.name

   O componente final do caminho.

Path.open(mode='r', *, pwd, **)

   Invoca "ZipFile.open()" no caminho atual. Permite a abertura para
   leitura ou escrita, texto ou binário através dos modos suportados:
   "r", "w", "rb", "wb". Argumentos posicionais e argumentos nomeados
   são passados para "io.TextIOWrapper" quando abertos como texto e
   ignorados caso contrário. "pwd" é o parâmetro "pwd" para
   "ZipFile.open()".

   Alterado na versão 3.9: Adicionado suporte para modos de texto e
   binários para aberto. O modo padrão agora é texto.

   Alterado na versão 3.11.2: O parâmetro "encoding" pode ser
   fornecido como um argumento posicional sem causar um "TypeError".
   Como poderia em 3.9. O código que precisa ser compatível com as
   versões 3.10 e 3.11 não corrigidas deve passar todos os argumentos
   de "io.TextIOWrapper", incluindo "encoding", como palavras
   reservadas.

Path.iterdir()

   Enumera os filhos do diretório atual.

Path.is_dir()

   Retorna "True" se o contexto atual fizer referência a um diretório.

Path.is_file()

   Retorna "True" se o contexto atual fizer referência a um arquivo.

Path.is_symlink()

   Retorna "True" se o contexto atual fizer referência a um link
   simbólico.

   Adicionado na versão 3.12.

   Alterado na versão 3.13: Anteriormente, "is_symlink" retornava
   "False" incondicionalmente.

Path.exists()

   Retorna "True" se o contexto atual fizer referência a um arquivo ou
   diretório no arquivo zip.

Path.suffix

   A última parte separada por pontos do componente final, se houver.
   Isso é comumente chamado de extensão de arquivo.

   Adicionado na versão 3.11: Adicionada a propriedade "Path.suffix".

Path.stem

   O componente final do caminho, sem seu sufixo.

   Adicionado na versão 3.11: Adicionada a propriedade "Path.stem".

Path.suffixes

   Uma lista dos sufixos do caminho, comumente chamados de extensões
   de arquivo.

   Adicionado na versão 3.11: Adicionada a propriedade
   "Path.suffixes".

Path.read_text(*, **)

   Leia o arquivo atual como texto Unicode. Argumentos posicionais e
   argumentos nomeados são passados para "io.TextIOWrapper" (exceto
   "buffer", que está implícito no contexto).

   Alterado na versão 3.11.2: O parâmetro "encoding" pode ser
   fornecido como um argumento posicional sem causar um "TypeError".
   Como poderia em 3.9. O código que precisa ser compatível com as
   versões 3.10 e 3.11 não corrigidas deve passar todos os argumentos
   de "io.TextIOWrapper", incluindo "encoding", como palavras
   reservadas.

Path.read_bytes()

   Lê o arquivo atual como bytes.

Path.joinpath(*other)

   Retorna um novo objeto Path com cada um dos *outros* argumentos
   unidos. Os seguintes são equivalentes:

      >>> Path(...).joinpath('child').joinpath('grandchild')
      >>> Path(...).joinpath('child', 'grandchild')
      >>> Path(...) / 'child' / 'grandchild'

   Alterado na versão 3.10: Antes de 3.10, "joinpath" não estava
   documentado e aceitava exatamente um parâmetro.

O projeto zipp fornece backports da funcionalidade mais recente de
objeto caminho para versões mais antigas do Pythons. Use "zipp.Path"
internamente de "zipfile.Path" para acesso antecipado às alterações.


Objetos PyZipFile
=================

O construtor "PyZipFile" usa os mesmos parâmetros que o construtor
"ZipFile", e um parâmetro adicional, *otimize*.

class zipfile.PyZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, optimize=-1)

   Alterado na versão 3.2: Adicionado o parâmetro *optimize*.

   Alterado na versão 3.4: Extensões ZIP64 são habilitadas por padrão.

   As instâncias têm um método além daqueles dos objetos "ZipFile":

   writepy(pathname, basename='', filterfunc=None)

      Pesquisa por arquivos "*.py" e adiciona o arquivo correspondente
      ao arquivo.

      Se o parâmetro *optimize* para "PyZipFile" não foi fornecido ou
      "-1", o arquivo correspondente é um arquivo "*.pyc", compilando
      se necessário.

      Se o parâmetro *Optimize* para "PyZipFile" era "0", "1" ou "2",
      apenas arquivos com esse nível de otimização (ver "compile()")
      são adicionados ao o arquivo, compilando se necessário.

      Se *pathname* for um arquivo, o nome do arquivo deverá terminar
      com ".py", e apenas o arquivo ("*.pyc" correspondente) será
      adicionado no nível superior (sem informações do caminho). Se
      *pathname* for um arquivo que não termine com ".py", um
      "RuntimeError" será levantado. Se for um diretório, e o
      diretório não for um diretório de pacotes, todos os arquivos
      "*.pyc" serão adicionados no nível superior. Se o diretório for
      um diretório de pacotes, todos "*.pyc" serão adicionados sob o
      nome do pacote como um caminho de arquivo e, se algum
      subdiretório for um diretório de pacotes, todos serão
      adicionados recursivamente na ordem de classificação.

      *basename* destina-se apenas a uso interno.

      *filterfunc*, se fornecido, deve ser uma função que recebe um
      único argumento de string. Cada caminho será passado (incluindo
      cada caminho de arquivo completo individual) antes de ser
      adicionado ao arquivo. Se *filterfunc* retornar um valor falso,
      o caminho não será adicionado e, se for um diretório, seu
      conteúdo será ignorado. Por exemplo, se nossos arquivos de teste
      estão todos nos diretórios "test" ou começam com a string
      "test_", podemos usar um *filterfunc* para excluí-los:

         >>> zf = PyZipFile('myprog.zip', 'w')
         >>> def notests(s):
         ...     fn = os.path.basename(s)
         ...     return (not (fn == 'test' or fn.startswith('test_')))
         ...
         >>> zf.writepy('myprog', filterfunc=notests)

      O método "writepy()" faz arquivos com nomes de arquivo como
      este:

         string.pyc                   # Nome de nível superior
         test/__init__.pyc            # Diretório do pacote
         test/testall.pyc             # Módulo test.testall
         test/bogus/__init__.pyc      # Diretório do subpacote
         test/bogus/myfile.pyc        # Submódulo test.bogus.myfile

      Alterado na versão 3.4: Adicionado o parâmetro *filterfunc*.

      Alterado na versão 3.6.2: O parâmetro *pathname* aceita um
      *objeto caminho ou similar*.

      Alterado na versão 3.7: A recursão classifica as entradas de
      diretório.


Objetos ZipInfo
===============

Instâncias da classe "ZipInfo" são retornadas pelos métodos
"getinfo()" e "infolist()" dos objetos "ZipFile". Cada objeto armazena
informações sobre um único membro do arquivo ZIP.

Existe um método de classe para fazer uma instância "ZipInfo" para um
arquivo de sistema de arquivos:

classmethod ZipInfo.from_file(filename, arcname=None, *, strict_timestamps=True)

   Constrói uma instância "ZipInfo" para um arquivo no sistema de
   arquivos, em preparação para adicioná-lo a um arquivo zip.

   *filename* deve ser o caminho para um arquivo ou diretório no
   sistema de arquivos.

   Se *arcname* for especificado, ele será usado como o nome dentro do
   arquivo. Se *arcname* não for especificado, o nome será igual a
   *filename*, mas com qualquer letra de unidade e separadores de
   caminho removidos.

   O argumento *strict_timestamps*, quando definido como "False",
   permite compactar arquivos anteriores a 1980-01-01 com o custo de
   definir o carimbo de data/hora para 1980-01-01. Comportamento
   semelhante ocorre com arquivos mais recentes que 2107-12-31, o
   carimbo de data/hora também é definido como o limite.

   Adicionado na versão 3.6.

   Alterado na versão 3.6.2: O parâmetro *filename* aceita um *objeto
   caminho ou similar*.

   Alterado na versão 3.8: Adicionado o parâmetro somente-nomeado
   *strict_timestamps*.

As instâncias têm os seguintes métodos e atributos:

ZipInfo.is_dir()

   Retorna "True" se este membro do arquivo for um diretório.

   Isso usa o nome da entrada: os diretórios devem sempre terminar com
   "/".

   Adicionado na versão 3.6.

ZipInfo.filename

   Nome do arquivo no pacote.

ZipInfo.date_time

   A hora e a data da última modificação no membro do arquivo. Esta é
   uma tupla de seis valores que representam os campos "last
   [modified] file time" (última hora [de modificado] do arquivo) e
   "last [modified] file date" (última data [de modificação] do
   arquivo) do diretório central do arquivo ZIP.

   A tupla contém:

   +---------+----------------------------+
   | Índice  | Valor                      |
   |=========|============================|
   | "0"     | Ano (>= 1980)              |
   +---------+----------------------------+
   | "1"     | Mês (iniciado em 1)        |
   +---------+----------------------------+
   | "2"     | Dia do mês (iniciado em 1) |
   +---------+----------------------------+
   | "3"     | Horas (iniciado em 0)      |
   +---------+----------------------------+
   | "4"     | Minutos (base zero)        |
   +---------+----------------------------+
   | "5"     | Segundos (iniciado em 0)   |
   +---------+----------------------------+

   Nota:

     O formato ZIP oferece suporte a vários campos de registro de data
     e hora em diferentes locais (diretório central, campos extras
     para sistemas NTFS/UNIX, etc.). Este atributo retorna
     especificamente o registro de data e hora do diretório central. O
     formato de registro de data e hora do diretório central em
     arquivos ZIP não oferece suporte a registros de data e hora
     anteriores a 1980. Embora alguns formatos de campos extras (como
     registros de data e hora do UNIX) possam representar datas
     anteriores, este atributo retorna apenas o registro de data e
     hora do diretório central.O registro de data e hora do diretório
     central é interpretado como representando a hora local, em vez da
     hora UTC, para corresponder ao comportamento de outras
     ferramentas zip.

ZipInfo.compress_type

   Tipo de compressão do membro do pacote.

ZipInfo.comment

   Comentário para o membro individual do pacote como um objeto
   "bytes".

ZipInfo.extra

   Dados do campo de expansão. O PKZIP Application Note contém alguns
   comentários sobre a estrutura interna dos dados contidos neste
   objeto "bytes".

ZipInfo.create_system

   O sistema que criou o pacote ZIP.

ZipInfo.create_version

   A versão do PKZIP que criou o pacote ZIP.

ZipInfo.extract_version

   A versão do PKZIP necessária para extrair o pacote.

ZipInfo.reserved

   Deve ser zero

ZipInfo.flag_bits

   Bits de sinalizador do ZIP.

ZipInfo.volume

   Número de volume do cabeçalho do arquivo.

ZipInfo.internal_attr

   Atributos internos.

ZipInfo.external_attr

   Atributos de arquivo externo.

ZipInfo.header_offset

   Deslocamento de byte para o cabeçalho do arquivo.

ZipInfo.CRC

   CRC-32 do arquivo não comprimido.

ZipInfo.compress_size

   Tamanho dos dados comprimidos.

ZipInfo.file_size

   Tamanho do arquivo não comprimido.


Interface de linha de comando
=============================

The "zipfile" module provides a simple command-line interface to
interact with ZIP archives.

Se você deseja criar um novo arquivo ZIP, especifique seu nome após a
opção "-c" e, em seguida, liste os nomes dos arquivos que devem ser
incluídos:

   $ python -m zipfile -c monty.zip spam.txt eggs.txt

Passar um diretório também é aceitável:

   $ python -m zipfile -c monty.zip life-of-brian_1979/

Se você deseja extrair um arquivo ZIP para o diretório especificado,
use a opção "-e":

   $ python -m zipfile -e monty.zip target-dir/

Para obter uma lista dos arquivos em um arquivo ZIP, use a opção "-l":

   $ python -m zipfile -l monty.zip


Opções de linha de comando
--------------------------

-l <zipfile>
--list <zipfile>

   Lista arquivos em um arquivo zip.

-c <zipfile> <source1> ... <sourceN>
--create <zipfile> <source1> ... <sourceN>

   Cria um arquivo zip a partir dos arquivos fonte.

-e <zipfile> <output_dir>
--extract <zipfile> <output_dir>

   Extrai um arquivo zip para um diretório de destino.

-t <zipfile>
--test <zipfile>

   Testa se o arquivo zip é válido ou não.

--metadata-encoding <encoding>

   Especifica a codificação dos nomes dos membros para "-l", "-e" e
   "-t".

   Adicionado na versão 3.11.


Armadilhas de descompressão
===========================

A extração no módulo zipfile pode falhar devido a algumas armadilhas
listadas abaixo.


Do próprio arquivo
------------------

A descompactação pode falhar devido a senha / soma de verificação CRC
/ formato ZIP incorretos ou método de compactação / descriptografia
não compatível.


Limitações do sistema de arquivos
---------------------------------

Exceder as limitações em sistemas de arquivos diferentes pode causar
falha na descompactação. Como caracteres permitidos nas entradas do
diretório, comprimento do nome do arquivo, comprimento do caminho,
tamanho de um único arquivo e número de arquivos, etc.


Limitações de recursos
----------------------

A falta de memória ou volume de disco levaria a uma falha de
descompactação. Por exemplo, bombas de descompressão (também
conhecidas como ZIP bomb) aplicam-se à biblioteca de arquivos zip que
podem causar o esgotamento do volume do disco.


Interrupção
-----------

A interrupção durante a descompressão, como pressionar Control-C ou
interromper o processo de descompressão pode resultar na descompressão
incompleta do arquivo.


Comportamentos padrão da extração
---------------------------------

Não saber os comportamentos de extração padrão pode causar resultados
de descompressão inesperados. Por exemplo, ao extrair o mesmo arquivo
duas vezes, ele sobrescreve os arquivos sem perguntar.
