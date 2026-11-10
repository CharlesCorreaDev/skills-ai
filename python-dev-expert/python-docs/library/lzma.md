"lzma" --- Compressão usando o algoritmo LZMA
*********************************************

Adicionado na versão 3.3.

**Código-fonte:** Lib/lzma.py

======================================================================

Este módulo fornece classes e funções de conveniência para comprimir e
descomprimir dados usando o algoritmo de compressão LZMA. Também está
incluída uma interface de arquivo que oferece suporte aos formatos de
arquivo ".xz" e legado ".lzma" usados pelo utilitário **xz**, bem como
fluxos brutos comprimidos.

A interface fornecida por este módulo é muito semelhante à do módulo
"bz2". Observe que "LZMAFile" e "bz2.BZ2File" *não* são seguro para
thread, portanto, se você precisar usar uma única instância "LZMAFile"
de vários threads, é necessário protegê-la com uma trava.

Este é um *módulo opcional*. Se ele estiver faltando na sua cópia do
CPython, procure a documentação do seu distribuidor (ou seja, quem lhe
forneceu o Python). Se você for o distribuidor, consulte Requisitos
para módulos opcionais.

exception lzma.LZMAError

   Essa exceção é levantada quando ocorre um erro durante a compressão
   ou descompressão ou durante a inicialização do estado
   compressor/descompressor.


Lendo e escrevendo arquivos comprimidos
=======================================

lzma.open(filename, mode='rb', *, format=None, check=-1, preset=None, filters=None, encoding=None, errors=None, newline=None)

   Abre um arquivo comprimido com LZMA no modo binário ou texto,
   retornando um *objeto arquivo*.

   O argumento *filename* pode ser um nome de arquivo real (dado como
   um objeto "str", "bytes" ou *caminho ou similar*), neste caso o
   arquivo nomeado é aberto , ou pode ser um objeto arquivo existente
   para leitura ou escrita.

   O argumento *mode* pode ser qualquer um de ""r"", ""rb"", ""w"",
   ""wb"", ""x"", ""xb"", ""a"" ou ""ab"" para modo binário, ou
   ""rt"", ""wt"", ""xt"" , ou ""at"" para o modo de texto. O padrão é
   ""rb"".

   Ao abrir um arquivo para leitura, os argumentos *format* e
   *filters* têm os mesmos significados que em "LZMADecompressor".
   Neste caso, os argumentos *check* e *preset* não devem ser usados.

   Ao abrir um arquivo para escrita, os argumentos *format*, *check*,
   *preset* e *filters* têm os mesmos significados que em
   "LZMACompressor".

   Para o modo binário, esta função é equivalente ao construtor
   "LZMAFile": "LZMAFile(filename, mode, ...)". Nesse caso, os
   argumentos *encoding*, *errors* e *newline* não devem ser
   fornecidos.

   Para o modo texto, um objeto "LZMAFile" é criado e encapsulado em
   uma instância "io.TextIOWrapper" com a codificação especificada,
   comportamento de tratamento de erros e final(is) de linha.

   Alterado na versão 3.4: Adicionado suporte para os modos ""x"",
   ""xb"" e ""xt"".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

class lzma.LZMAFile(filename=None, mode='r', *, format=None, check=-1, preset=None, filters=None)

   Abre um arquivo comprimido com LZMA no modo binário.

   Um "LZMAFile" pode envolver um *objeto arquivo* já aberto, ou
   operar diretamente em um arquivo nomeado. O argumento *filename*
   especifica o objeto arquivo a ser encapsulado ou o nome do arquivo
   a ser aberto (como um objeto "str", "bytes" ou *objeto caminho ou
   similar*). Ao agrupar um objeto arquivo existente, o arquivo
   agrupado não será fechado quando o "LZMAFile" for fechado.

   O argumento *mode* pode ser ""r"" para leitura (padrão), ""w"" para
   substituição, ""x"" para criação exclusiva ou ""a"" para anexar.
   Estes podem ser equivalentemente dados como ""rb"", ""wb"", ""xb""
   e ""ab"" respectivamente.

   Se *filename* for um objeto arquivo (em vez de um nome de arquivo
   real), um modo de ""w"" não truncará o arquivo e será equivalente a
   ""a"".

   Ao abrir um arquivo para leitura, o arquivo de entrada pode ser a
   concatenação de vários fluxos comprimidos separados. Estes são
   decodificados de forma transparente como um único fluxo lógico.

   Ao abrir um arquivo para leitura, os argumentos *format* e
   *filters* têm os mesmos significados que em "LZMADecompressor".
   Neste caso, os argumentos *check* e *preset* não devem ser usados.

   Ao abrir um arquivo para escrita, os argumentos *format*, *check*,
   *preset* e *filters* têm os mesmos significados que em
   "LZMACompressor".

   "LZMAFile" suporta todos os membros especificados por
   "io.BufferedIOBase", exceto "detach()" e "truncate()". Iteração e a
   instrução "with" são suportadas.

   O método e os atributos a seguir também são fornecidos:

   peek(size=-1)

      Retorna dados armazenados em buffer sem avançar a posição do
      arquivo. Pelo menos um byte de dados será retornado, a menos que
      o EOF tenha sido atingido. O número exato de bytes retornados
      não é especificado (o argumento *size* é ignorado).

      Nota:

        Enquanto chamar "peek()" não altera a posição do arquivo de
        "LZMAFile", pode alterar a posição do objeto arquivo
        subjacente (por exemplo, se o "LZMAFile" foi construído
        passando um objeto arquivo para *nome do arquivo*).

   mode

      "'rb'" para leitura e "'wb'" para escrita.

      Adicionado na versão 3.13.

   name

      O nome do arquivo lzma. Equivalente ao atributo "name" do
      *objeto arquivo* subjacente.

      Adicionado na versão 3.13.

   Alterado na versão 3.4: Adicionado suporte para os modos ""x"" e
   ""xb"".

   Alterado na versão 3.5: O método "read()" agora aceita um argumento
   de "None".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.


Comprimindo e descomprimindo dados na memória
=============================================

class lzma.LZMACompressor(format=FORMAT_XZ, check=-1, preset=None, filters=None)

   Cria um objeto compressão, que pode ser usado para comprimir dados
   de forma incremental.

   Para uma maneira mais conveniente de comprimir um único bloco de
   dados, consulte "compress()".

   The *format* argument specifies what container format should be
   used. Possible values are "FORMAT_XZ" (the default), "FORMAT_ALONE"
   and "FORMAT_RAW".

   The *check* argument specifies the type of integrity check to
   include in the compressed data. This check is used when
   decompressing, to ensure that the data has not been corrupted.
   Possible values are "CHECK_NONE", "CHECK_CRC32", "CHECK_CRC64" (the
   default for "FORMAT_XZ") and "CHECK_SHA256".

   Se a verificação especificada não for suportada, uma exceção
   "LZMAError" será levantada.

   As configurações de compressão podem ser especificadas como um
   nível de compressão predefinido (com o argumento *preset*) ou em
   detalhes como uma cadeia de filtros personalizada (com o argumento
   *filters*).

   O argumento *preset* (se fornecido) deve ser um inteiro entre "0" e
   "9" (inclusive), opcionalmente com OR com a constante
   "PRESET_EXTREME". Se nem *preset* nem *filters* forem fornecidos, o
   comportamento padrão é usar "PRESET_DEFAULT" (nível predefinido
   "6"). Predefinições mais altas produzem uma saída menor, mas tornam
   o processo de compressão mais lento.

   Nota:

     Além de consumir mais CPU, a compressão com predefinições mais
     altas também requer muito mais memória (e produz uma saída que
     precisa de mais memória para descompressão). Com a predefinição
     "9" por exemplo, a sobrecarga para um objeto "LZMACompressor"
     pode chegar a 800 MiB. Por esse motivo, geralmente é melhor ficar
     com a predefinição padrão.

   O argumento *filters* (se fornecido) deve ser um especificador de
   cadeia de filtros. Veja Especificando cadeias de filtros
   personalizadas para detalhes.

   compress(data)

      Comprime *data* (um objeto "bytes"), retornando um objeto
      "bytes" contendo dados comprimidos para pelo menos parte da
      entrada. Alguns dos *data* podem ser armazenados internamente,
      para uso em chamadas posteriores para "compress()" e "flush()".
      Os dados retornados devem ser concatenados com a saída de
      quaisquer chamadas anteriores para "compress()".

   flush()

      Conclui o processo de compressão, retornando um objeto "bytes"
      contendo todos os dados armazenados nos buffers internos do
      compressor.

      O compressor não pode ser usado após a chamada deste método.

class lzma.LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)

   Cria um objeto descompressor, que pode ser usado para descomprimir
   dados de forma incremental.

   Para uma maneira mais conveniente de descomprimir um fluxo
   comprimido inteiro de uma só vez, consulte "decompress()".

   O argumento *format* especifica o formato do contêiner que deve ser
   usado. O padrão é "FORMAT_AUTO", que pode descomprimir os arquivos
   ".xz" e ".lzma". Outros valores possíveis são "FORMAT_XZ",
   "FORMAT_ALONE" e "FORMAT_RAW".

   O argumento *memlimit* especifica um limite (em bytes) na
   quantidade de memória que o descompressor pode usar. Quando esse
   argumento é usado, a descompressão falhará com um "LZMAError" se
   não for possível descomprimir a entrada dentro do limite de memória
   fornecido.

   O argumento *filters* especifica a cadeia de filtros que foi usada
   para criar o fluxo que está sendo descomprimido. Este argumento é
   necessário se *format* for "FORMAT_RAW", mas não deve ser usado
   para outros formatos. Veja Especificando cadeias de filtros
   personalizadas para mais informações sobre cadeias de filtros.

   Nota:

     Esta classe não manipula de forma transparente entradas contendo
     múltiplos fluxos comprimidos, diferentemente de "decompress()" e
     "LZMAFile". Para descomprimir uma entrada multi-fluxo com
     "LZMADecompressor", você deve criar um novo descompactador para
     cada fluxo.

   decompress(data, max_length=-1)

      Descomprime dados *data* (um *objeto bytes ou similar*),
      retornando dados não comprimidos como bytes. Alguns dos *data*
      podem ser armazenados em buffer internamente, para uso em
      chamadas posteriores para "decompress()". Os dados retornados
      devem ser concatenados com a saída de qualquer chamada anterior
      para "decompress()".

      Se *max_length* for não negativo, retornará no máximo
      *max_length* bytes de dados descomprimidos. Se este limite for
      atingido e mais saída puder ser produzida, o atributo
      "needs_input" será definido como "False". Neste caso, a próxima
      chamada para "decompress()" pode fornecer *data* como "b''" para
      obter mais saída.

      Se todos os dados de entrada foram descomprimidos e retornados
      (seja porque era menor que *max_length* bytes, ou porque
      *max_length* era negativo), o atributo "needs_input" será
      definido como "True" .

      A tentativa de descomprimir os dados após o final do fluxo ser
      atingido gera um "EOFError". Quaisquer dados encontrados após o
      final do fluxo são ignorados e salvos no atributo "unused_data".

      Alterado na versão 3.5: Adicionado o parâmetro *max_length*.

   check

      O ID da verificação de integridade usada pelo fluxo de entrada.
      Pode ser "CHECK_UNKNOWN" até que o suficiente da entrada tenha
      sido decodificado para determinar qual verificação de
      integridade ela usa.

   eof

      "True" se o marcador de fim de fluxo foi atingido.

   unused_data

      Dados encontrados após o término do fluxo comprimido.

      Antes do final do fluxo ser alcançado, isso será "b""".

   needs_input

      "False" se o método "decompress()" puder fornecer mais dados
      descomprimidos antes de exigir uma nova entrada não comprimida.

      Adicionado na versão 3.5.

lzma.compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)

   Comprime *data* (um objeto "bytes"), retornando os dados
   comprimidos como um objeto "bytes".

   Veja "LZMACompressor" acima para uma descrição dos argumentos
   *format*, *check*, *preset* e *filters*.

lzma.decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)

   Descomprime *data* (um objeto "bytes"), retornando os dados não
   comprimidos como um objeto "bytes".

   Se *data* forem a concatenação de vários fluxos comprimidos
   distintos, descomprime todos esses fluxos e retorna a concatenação
   dos resultados.

   Veja "LZMADecompressor" acima para uma descrição dos argumentos
   *format*, *memlimit* e *filters*.


Diversos
========

lzma.is_check_supported(check)

   Retorna "True" se a verificação de integridade fornecida for
   suportada neste sistema.

   "CHECK_NONE" e "CHECK_CRC32" são sempre suportados. "CHECK_CRC64" e
   "CHECK_SHA256" podem não estar disponíveis se você estiver usando
   uma versão do **liblzma** que foi compilada com um conjunto de
   recursos limitado.


Especificando cadeias de filtros personalizadas
===============================================

Um especificador de cadeia de filtros é uma sequência de dicionários,
onde cada dicionário contém o ID e as opções para um único filtro.
Cada dicionário deve conter a chave ""id"" e pode conter chaves
adicionais para especificar opções dependentes do filtro. Os IDs de
filtro válidos são os seguintes:

* Filtro Compression:

  * "FILTER_LZMA1" (para ser usado com "FORMAT_ALONE")

  * "FILTER_LZMA2" (para ser utilizado com "FORMAT_XZ" and
    "FORMAT_RAW")

* Filtro delta:

  * "FILTER_DELTA"

* Filtros Branch-Call-Jump (BCJ):

  * "FILTER_X86"

  * "FILTER_IA64"

  * "FILTER_ARM"

  * "FILTER_ARMTHUMB"

  * "FILTER_POWERPC"

  * "FILTER_SPARC"

Uma cadeia de filtros pode consistir em até 4 filtros e não pode estar
vazia. O último filtro na cadeia deve ser um filtro de compressão e
quaisquer outros filtros devem ser filtros delta ou BCJ.

Os filtros de compressão suportam as seguintes opções (especificadas
como entradas adicionais no dicionário que representa o filtro):

* "preset": Uma predefinição de compressão para usar como fonte de
  valores padrão para opções que não são especificadas explicitamente.

* "dict_size": Tamanho do dicionário em bytes. Deve estar entre 4 KiB
  e 1,5 GiB (inclusive).

* "lc": Número de bits de contexto literal.

* "lp": Número de bits de posição literal. A soma "lc + lp" deve ser
  no máximo 4.

* "pb": Número de bits de posição; deve ser no máximo 4.

* "mode": "MODE_FAST" ou "MODE_NORMAL".

* "nice_len": O que deve ser considerado um "tamanho agradável" para
  uma correspondência. Deve ser 273 ou menos.

* "mf": Qual localizador de correspondências usar -- "MF_HC3",
  "MF_HC4", "MF_BT2", "MF_BT3" ou "MF_BT4".

* "depth": Profundidade máxima de pesquisa usada pelo localizador de
  correspondências. 0 (padrão) significa selecionar automaticamente
  com base em outras opções de filtro.

O filtro delta armazena as diferenças entre bytes, produzindo uma
entrada mais repetitiva para o compressor em certas circunstâncias.
Ele suporta uma opção, "dist". Isso indica a distância entre bytes a
ser subtraída. O padrão é 1, ou seja, pega as diferenças entre bytes
adjacentes.

Os filtros BCJ são destinados a serem aplicados ao código de máquina.
Eles convertem ramificações relativas, chamadas e saltos no código
para usar endereçamento absoluto, com o objetivo de aumentar a
redundância que pode ser explorada pelo compressor. Esses filtros
suportam uma opção, "start_offset". Isso especifica o endereço que
deve ser mapeado para o início dos dados de entrada. O padrão é 0.


Constantes
==========

The following module-level constants are provided for use as the
*format*, *check*, *preset* and *filters* arguments of the classes and
functions above.

Container formats:

lzma.FORMAT_XZ

   The ".xz" container format.

lzma.FORMAT_ALONE

   The legacy ".lzma" container format.  This format is more limited
   than ".xz" -- it does not support integrity checks or multiple
   filters.

lzma.FORMAT_RAW

   A raw data stream, not using any container format.  This format
   specifier does not support integrity checks, and requires that you
   always specify a custom filter chain (for both compression and
   decompression).  Additionally, data compressed in this manner
   cannot be decompressed using "FORMAT_AUTO".

lzma.FORMAT_AUTO

   Used for decompression only.  The container format is detected
   automatically, so that both ".xz" and ".lzma" files can be
   decompressed.

Integrity checks:

lzma.CHECK_NONE

   No integrity check.  This is the default (and the only acceptable
   value) for "FORMAT_ALONE" and "FORMAT_RAW".

lzma.CHECK_CRC32

   A 32-bit Cyclic Redundancy Check.

lzma.CHECK_CRC64

   A 64-bit Cyclic Redundancy Check.  This is the default for
   "FORMAT_XZ".

lzma.CHECK_SHA256

   A 256-bit Secure Hash Algorithm.

lzma.CHECK_UNKNOWN

   The integrity check used by a stream could not yet be determined.
   This may be the value of the "LZMADecompressor.check" attribute
   until enough of the input has been decoded.

lzma.CHECK_ID_MAX

   The largest supported integrity-check ID.

Compression presets:

lzma.PRESET_DEFAULT

   The default compression preset, equivalent to preset level "6".

lzma.PRESET_EXTREME

   A flag that may be bitwise OR-ed with a preset level ("0" to "9")
   to select a slower but more thorough variant of that preset.

Filter IDs and options:

lzma.FILTER_LZMA1
lzma.FILTER_LZMA2

   The LZMA1 and LZMA2 compression filters.  "FILTER_LZMA1" is for use
   with "FORMAT_ALONE", while "FILTER_LZMA2" is for use with
   "FORMAT_XZ" and "FORMAT_RAW".

lzma.FILTER_DELTA

   The delta filter.

lzma.MODE_FAST
lzma.MODE_NORMAL

   Compression modes that may be used as the "mode" option of a filter
   specifier (see Especificando cadeias de filtros personalizadas).

lzma.MF_HC3
lzma.MF_HC4
lzma.MF_BT2
lzma.MF_BT3
lzma.MF_BT4

   Match finders that may be used as the "mf" option of a filter
   specifier (see Especificando cadeias de filtros personalizadas).


Exemplos
========

Lendo em um arquivo comprimido:

   import lzma
   with lzma.open("file.xz") as f:
       file_content = f.read()

Criando um arquivo comprimido:

   import lzma
   data = b"Insira dados aqui"
   with lzma.open("file.xz", "w") as f:
       f.write(data)

Comprimindo dados na memória:

   import lzma
   data_in = b"Insert Data Here"
   data_out = lzma.compress(data_in)

Compressão incremental:

   import lzma
   lzc = lzma.LZMACompressor()
   out1 = lzc.compress(b"Alguns dados\n")
   out2 = lzc.compress(b"Outro pedaço de dados\n")
   out3 = lzc.compress(b"Ainda mais dados\n")
   out4 = lzc.flush()
   # Concatena todos os resultados parciais:
   result = b"".join([out1, out2, out3, out4])

Escrevendo dados comprimidos em um arquivo já aberto:

   import lzma
   with open("file.xz", "wb") as f:
       f.write(b"Este dados serão comprimidos\n")
       with lzma.open(f, "w") as lzf:
           lzf.write(b"Isso *vai* ser comprimidos\n")
       f.write(b"Não comprimidos\n")

Criando um arquivo comprimido usando uma cadeia de filtros
personalizada:

   import lzma
   my_filters = [
       {"id": lzma.FILTER_DELTA, "dist": 5},
       {"id": lzma.FILTER_LZMA2, "preset": 7 | lzma.PRESET_EXTREME},
   ]
   with lzma.open("file.xz", "w", filters=my_filters) as f:
       f.write(b"blá blá blá")
