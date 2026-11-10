"mimetypes" --- Mapeia nomes de arquivos para tipos MIME
********************************************************

**Código-fonte:** Lib/mimetypes.py

======================================================================

O módulo "mimetypes" converte entre um nome de arquivo ou URL e o tipo
MIME associado à extensão do arquivo. As conversões são fornecidas do
nome do arquivo para o tipo MIME e da extensão do tipo MIME para o
nome do arquivo; codificações não são suportadas para a última
conversão.

O módulo fornece uma classe e várias funções convenientes. As funções
são a interface normal para este módulo, mas algumas aplicações também
podem estar interessadas na classe.

As funções descritas abaixo fornecem a interface principal para este
módulo. Se o módulo não foi inicializado, eles chamarão "init()" se
confiarem nas informações configuradas por "init()".

mimetypes.guess_type(url, strict=True)

   Adivinha o tipo de arquivo com base em seu nome de arquivo, caminho
   ou URL, fornecido por *url*. A URL pode ser uma string ou um
   *objeto caminho ou similar*.

   O valor de retorno é uma tupla "(type, encoding)" onde o *tipo* é
   "None" se o tipo não puder ser ser adivinhado (sufixo ausente ou
   desconhecido) ou uma string no formato "'type/subtype'", utilizável
   para um cabeçalho MIME *content-type*.

   *encoding* é "None" para nenhuma codificação ou o nome do programa
   usado para codificar (por exemplo **compress** ou **gzip**). A
   codificação é adequada para uso como cabeçalho *Content-Encoding* ,
   **não** como cabeçalho *Content-Transfer-Encoding*. Os mapeamentos
   são orientados por tabela. Os sufixos de codificação diferenciam
   maiúsculas de minúsculas; os sufixos de tipo são testados primeiro
   considerando maiúsculas e minúsculas e depois sem considerar.

   O argumento opcional *strict* é um sinalizador que especifica se a
   lista de tipos MIME conhecidos é limitada apenas aos tipos oficiais
   registrados na IANA. No entanto, o comportamento deste módulo
   também depende do sistema operacional subjacente. Somente tipos de
   arquivo reconhecidos pelo sistema operacional ou registrados
   explicitamente no banco de dados interno do Python podem ser
   identificados. Quando *strict* é "True" (o padrão), apenas os tipos
   IANA são suportados; quando *strict* é "False", alguns tipos MIME
   adicionais não padronizados, mas geralmente usados, também são
   reconhecidos.

   Alterado na versão 3.8: Adicionado suporte para que a *url* seja um
   *objeto caminho ou similar*.

   Suavemente descontinuado desde a versão 3.13: Passar um caminho de
   arquivo em vez de URL. Use "guess_file_type()" para isso.

mimetypes.guess_file_type(path, *, strict=True)

   Adivinha o tipo de um arquivo com base em seu caminho, dado por
   *path*. Semelhante à função "guess_type()", mas aceita um caminho
   em vez de URL. O caminho pode ser uma string, um objeto bytes ou um
   *objeto caminho ou similar*.

   Adicionado na versão 3.13.

mimetypes.guess_all_extensions(type, strict=True)

   Adivinha as extensões para um arquivo com base em seu tipo MIME,
   fornecido por *type*. O valor de retorno é uma lista de strings que
   fornecem todas as extensões possíveis de nome de arquivo, incluindo
   o ponto ("'.'"). Não é garantido que as extensões tenham sido
   associadas a qualquer fluxo de dados específico, mas seriam
   mapeadas para o tipo MIME *type* por "guess_type()" e
   "guess_file_type()".

   O argumento opcional *strict* tem o mesmo significado que usado com
   a função "guess_type()".

mimetypes.guess_extension(type, strict=True)

   Adivinha a extensão para um arquivo com base em seu tipo MIME,
   fornecido por *type*. O valor de retorno é uma string que fornece
   uma extensão de nome de arquivo, incluindo o ponto ("'.'"). Não é
   garantido que a extensão tenha sido associada a qualquer fluxo de
   dados específico, mas seria mapeada para o tipo MIME *type* por
   "guess_type()" e "guess_file_type()". Se nenhuma extensão puder ser
   adivinhada para *type*, "None" é retornado.

   O argumento opcional *strict* tem o mesmo significado que usado com
   a função "guess_type()".

Algumas funções e dados adicionais estão disponíveis para controlar o
comportamento do módulo.

mimetypes.init(files=None)

   Inicializa as estruturas de dados internas.  Se fornecido, *files*
   deverá ser uma sequência de nomes de arquivos que devem ser usados
   para aumentar o mapa de tipos padrão.  Se for omitido, os nomes de
   arquivos a serem usados serão retirados de "knownfiles"; no
   Windows, as configurações atuais do registro são carregadas.  Cada
   arquivo nomeado em *files* ou "knownfiles" tem precedência sobre os
   definidos anteriormente.  É permitido chamar "init()"
   repetidamente.

   Especificar uma lista vazia para *files* impedirá que os padrões do
   sistema sejam carregados: apenas os valores bem conhecidos estarão
   presentes em uma lista interna.

   Se *files* for "None", a estrutura de dados interna será
   completamente reconstruída com seu valor inicial padrão. Essa é uma
   operação estável e produzirá os mesmos resultados quando chamada
   várias vezes.

   Alterado na versão 3.2: Anteriormente, as configurações do registro
   do Windows eram ignoradas.

mimetypes.read_mime_types(file)

   Carrega o mapa de tipos fornecido no arquivo chamado *file*, se
   existir. *file* deve ser uma string que especifica o nome do
   arquivo a ser lido. O mapa de tipos é retornado como um dicionário
   que faz o mapeamento de extensões de arquivo, incluindo o ponto
   inicial ("'.'"), para strings no formato "'tipo/subtipo'". Se o
   arquivo não existir ou não puder ser lido, "None" é retornado.

mimetypes.add_type(type, ext, strict=True)

   Adiciona um mapeamento do tipo MIME *type* para a extensão *ext*.
   Quando a extensão já for conhecida, o novo tipo substituirá o
   antigo. Quando o tipo já for conhecido, a extensão será adicionada
   à lista de extensões conhecidas.

   Quando *strict* for "True" (o padrão), o mapeamento será adicionado
   aos tipos MIME oficiais, caso contrário, aos não-padrão.

mimetypes.inited

   Sinalizador indicando se as estruturas de dados globais foram
   inicializadas ou não. Isso é definido para "True" por "init()".

mimetypes.knownfiles

   Lista de nomes de arquivos de mapas de tipos comumente instalados.
   Esses arquivos são normalmente nomeado como "mime.types" e são
   instalados em diferentes locais por diferentes pacote.

mimetypes.suffix_map

   Dicionário mapeando sufixos para sufixos.  Isso é usado para
   permitir o reconhecimento de arquivos codificados para os quais a
   codificação e o tipo são indicados pela mesma extensão. Por
   exemplo, em um arquivo codificado, a extensão ".tgz" é mapeada para
   ".tar.gz" para permitir que a codificação e o tipo sejam
   reconhecidos separadamente.

mimetypes.encodings_map

   Dicionário mapeando extensões de nome de arquivo para os tipos de
   codificação.

mimetypes.types_map

   Dicionário mapeando extensões de nome do arquivo para tipos MIME.

mimetypes.common_types

   Dicionário mapeando extensões de nome de arquivo para tipos MIME
   não padronizados, mas comumente encontrados.

Um exemplo de uso do módulo:

   >>> import mimetypes
   >>> mimetypes.init()
   >>> mimetypes.knownfiles
   ['/etc/mime.types', '/etc/httpd/mime.types', ... ]
   >>> mimetypes.suffix_map['.tgz']
   '.tar.gz'
   >>> mimetypes.encodings_map['.gz']
   'gzip'
   >>> mimetypes.types_map['.tgz']
   'application/x-tar-gz'


Objetos MimeTypes
=================

A classe "MimeTypes" pode ser útil para aplicações que possam querer
mais de um banco de dados de tipos MIME; ela fornece uma interface
semelhante à do módulo "mimetypes".

class mimetypes.MimeTypes(filenames=(), strict=True)

   Esta classe representa um banco de dados de tipos MIME. Por padrão,
   ela fornece acesso ao mesmo banco de dados do restante deste
   módulo. O banco de dados inicial é criado a partir de tabelas de
   tipos MIME embutis no Python. Ele pode ser estendido ao carregar
   arquivos adicionais no formato "mime.types" no banco de dados,
   usando os métodos "read()" ou "readfp()". Os dicionários de
   mapeamento também podem ser limpos antes de carregar dados
   adicionais, caso os dados padrões não sejam desejados.

   O parâmetro opcional *filenames* pode ser usado para carregar
   arquivos adicionais "em cima" do banco de dados padrão.

   suffix_map

      Dicionário mapeando sufixo para sufixo. Isso é usado para
      permitir o reconhecimento de arquivos codificados para os quais
      a codificação e o tipo são indicados pela mesma extensão. Por
      exemplo, a extensão ".tgz" é mapeada para ".tar.gz" para
      permitir que a codificação e o tipo sejam reconhecidos
      separadamente.  Isso é inicializado com alguns valores
      predefinidos.

   encodings_map

      Dicionário que mapeia extensões de arquivo para tipos de
      codificação. Ele é inicializado com alguns valores predefinidos.

   types_map

      Tupla contendo dois dicionários, mapeando extensões de nomes de
      arquivo para tipos MIME: o primeiro dicionário é para tipos não
      padrão e o segundo, para tipos padrão. Eles são inicializados
      com alguns valores predefinidos e informações de tipo MIME
      carregadas a partir dos arquivos especificados pelo argumento
      *filenames*.

   types_map_inv

      Tupla contendo dois dicionários, mapeando tipos MIME para uma
      lista de extensões de nomes de arquivo: o primeiro dicionário é
      para tipos não padrão e o segundo, para tipos padrão. Eles são
      inicializados com alguns valores predefinidos e informações de
      tipo MIME carregadas a partir dos arquivos especificados pelo
      argumento *filenames*.

   guess_extension(type, strict=True)

      Similar à função "guess_extension()", usando as tabelas
      armazenadas como parte do objeto.

   guess_type(url, strict=True)

      Similar à função "guess_type()", usando as tabelas armazenadas
      como parte do objeto.

   guess_file_type(path, *, strict=True)

      Similar à função "guess_file_type()", usando as tabelas
      armazenadas como parte do objeto.

      Adicionado na versão 3.13.

   guess_all_extensions(type, strict=True)

      Similar à função "guess_all_extensions()", usando as tabelas
      armazenadas como parte do objeto.

   read(filename, strict=True)

      Carrega as informações do tipo MIME de um arquivo chamado
      *filename*.  Usa "readfp()" para analisar o arquivo.

      Se *strict* for "True", as informações serão adicionadas à lista
      de tipos padrão, caso contrário, à lista de tipos não padrão.

   readfp(fp, strict=True)

      Carrega as informações do tipo MIME de um arquivo aberto *fp*. O
      arquivo precisa estar no formato padrão dos arquivos
      "mime.types".

      Se *strict* for "True", as informações serão adicionadas à lista
      de tipos padrão, caso contrário, à lista de tipos não padrão.

   read_windows_registry(strict=True)

      Carrega as informações do tipo MIME a partir do registro do
      Windows.

      Disponibilidade: Windows.

      Se *strict* for "True", as informações serão adicionadas à lista
      de tipos padrão, caso contrário, à lista de tipos não padrão.

      Adicionado na versão 3.2.

   add_type(type, ext, strict=True)

      Adiciona um mapeamento do tipo MIME *type* para a extensão
      *ext*. As extensões válidas começam com um '.' ou são vazias.
      Quando a extensão já for conhecida, o novo tipo substituirá o
      antigo. Quando o tipo já for conhecido, a extensão será
      adicionada à lista de extensões conhecidas.

      Quando *strict* for "True" (o padrão), o mapeamento será
      adicionado aos tipos MIME oficiais, caso contrário, aos não-
      padrão.

      Descontinuado desde a versão 3.14, será removido na versão 3.16:
      Extensões inválidas e sem ponto levantarão uma exceção
      "ValueError" em Python 3.16.


Uso na linha de comando
=======================

O módulo "mimetypes" pode ser invocado como um script na linha de
comando:

   python -m mimetypes [-h] [-e] [-l] type [type ...]

As seguintes opções são aceitas:

-h
--help

   Mostra a mensagem de ajuda e sai.

-e
--extension

   Adivinha a extensão em vez do tipo.

-l
--lenient

   Adicionalmente, pesquisa alguns tipos comuns, mas não padronizados.

Por padrão, o script converte os tipos MIME em extensões de arquivo.
Entretanto, se "--extension" for especificado, ele converterá a
extensão do arquivo em tipos MIME.

Para cada entrada "type", o script grava uma linha no fluxo de saída
padrão. Se ocorrer um tipo desconhecido, ele gravará uma mensagem de
erro no fluxo padrão de saída e sairá com o código de retorno "1" .


Exemplos na linha de comando
============================

Aqui estão alguns exemplos de uso típico da interface de linha de
comando do "mimetypes":

   $ # obtém um tipo MIME a partir de um nome de arquivo
   $ python -m mimetypes filename.png
   type: image/png encoding: None

   $ # obtém um tipo MIME a partir de uma URL
   $ python -m mimetypes https://example.com/filename.txt
   type: text/plain enconding: None

   $ # obtém um tipo MIME complexo
   $ python -m mimetypes filename.tar.gz
   type: aplicação/x-tar codificação: gzip

   $ # obtém um tipo MIME para uma extensão de arquivo rara
   $ python -m mimetypes filename.pict
   error: unknown extension of filename.pict

   $ # agora procura no banco de dados estendido embutido no Python
   $ python -m mimetypes --lenient filename.pict
   type: image/pict encoding: None

   $ # obtém uma extensão de arquivo a partir de tipo MIME
   $ python -m mimetypes --extension text/javascript
   .js

   $ # obtém uma extensão de arquivo  a partir de um tipo MIME raro
   $ python -m mimetypes --extension text/xul
   error: unknown type text/xul

   $ # agora procura novamente no banco de dados estendido
   $ python -m mimetypes --extension --lenient text/xul
   .xul

   $ # tenta alimentar uma extensão de arquivo desconhecida
   $ python -m mimetypes filename.sh filename.nc filename.xxx filename.txt
   type: application/x-sh encoding: None
   type: application/x-netcdf encoding: None
   error: media type unknown for filename.xxx
   type: text/plain encoding: None

   $ # tenta alimentar um tipo MIME desconhecido
   $ python -m mimetypes --extension audio/aac audio/opus audio/future audio/x-wav
   .aac
   .opus
   error: unknown type audio/future
