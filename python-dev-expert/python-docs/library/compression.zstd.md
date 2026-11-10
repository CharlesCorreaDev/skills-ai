"compression.zstd" --- Compactação compatível com o formato Zstandard
*********************************************************************

Adicionado na versão 3.14.

**Código-fonte:** Lib/compression/zstd/__init__.py

======================================================================

Este módulo fornece classes e funções para compactar e descompactar
dados usando o algoritmo de compactação Zstandard (ou *zstd*). O
manual do zstd descreve o Zstandard como "um algoritmo de compactação
rápido e sem perdas, voltado para cenários de compactação em tempo
real, no nível de zlib, com taxas de compactação melhores". Também
está incluída uma interface de arquivo que oferece suporte à leitura e
à gravação do conteúdo de arquivos ".zst" criados pelo utilitário
**zstd**, bem como de fluxos compactados zstd brutos.

O módulo "compression.zstd" contém:

* A função "open()" e a classe "ZstdFile" para leitura e escrita de
  arquivos compactados.

* As classes "ZstdCompressor" e "ZstdDecompressor" para
  (des)compactação incremental.

* As funções "compress()" e "decompress()" para (des)compactação de
  uma só vez.

* As funções "train_dict()" e "finalize_dict()" e a classe "ZstdDict"
  para treinar e gerenciar dicionários Zstandard.

* As classes "CompressionParameter", "DecompressionParameter" e
  "Strategy" para definir parâmetros avançados de (des)compactação.

Este é um *módulo opcional*. Se ele estiver faltando na sua cópia do
CPython, procure a documentação do seu distribuidor (ou seja, quem lhe
forneceu o Python). Se você for o distribuidor, consulte Requisitos
para módulos opcionais.


Exceções
========

exception compression.zstd.ZstdError

   Essa exceção é levantada quando ocorre um erro durante a
   compactação ou descompactação ou durante a inicialização do estado
   (des)compactador.


Lendo e escrevendo arquivos compactados
=======================================

compression.zstd.open(file, /, mode='rb', *, level=None, options=None, zstd_dict=None, encoding=None, errors=None, newline=None)

   Abre um arquivo compactado com Zstandard em modo binário ou texto,
   retornando *objeto arquivo*.

   O argumento *file* pode ser um nome de arquivo (dado como um objeto
   "str", "bytes" ou *caminho ou similar*), neste caso o arquivo
   nomeado é aberto , ou pode ser um objeto arquivo existente para
   leitura ou escrita.

   O argumento mode pode ser "'rb'" para leitura (padrão), "'wb'" para
   sobrescrever, "'ab'" para anexar ou "'xb'" para criação exclusiva.
   Estes podem ser fornecidos como "'r'", "'w'", "'a'" e "'x'",
   respectivamente. Você também pode abrir em modo texto com "'rt'",
   "'wt'", "'at'" e "'xt'", respectivamente.

   Durante a leitura, o argumento *options* pode ser um dicionário que
   fornece parâmetros avançados de descompactação; consulte
   "DecompressionParameter" para obter informações detalhadas sobre os
   parâmetros suportados. O argumento *zstd_dict* é uma instância de
   "ZstdDict" a ser usada durante a descompactação. Durante a leitura,
   se o argumento *level* não for None, uma exceção "TypeError" será
   levantada.

   When writing, the *options* argument can be a dictionary providing
   advanced compression parameters; see "CompressionParameter" for
   detailed information about supported parameters. The *level*
   argument is the compression level to use when writing compressed
   data. Only one of *level* or *options* may be non-None. The
   *zstd_dict* argument is a "ZstdDict" instance to be used during
   compression.

   Em modo binário, esta função equivale ao construtor "ZstdFile":
   "ZstdFile(file, mode, ...)". Nesse caso, os parâmetros *encoding*,
   *errors* e *newline* não devem ser fornecidos.

   Em modo texto, um objeto "ZstdFile" é criado e encapsulado em uma
   instância "io.TextIOWrapper" com a codificação especificada,
   comportamento de tratamento de erros e fins de linha.

class compression.zstd.ZstdFile(file, /, mode='rb', *, level=None, options=None, zstd_dict=None)

   Abre um arquivo compactado com Zstandard no modo binário.

   Um "ZstdFile" pode envolver um *objeto arquivo* já aberto, ou
   operar diretamente em um arquivo nomeado. O argumento *file*
   especifica o objeto arquivo a ser envolvido ou o nome do arquivo a
   ser aberto (como um objeto "str", "bytes" ou *objeto caminho ou
   similar*). Se estiver envolvendo um objeto arquivo existente, o
   arquivo envolvido não será fechado quando o "ZstdFile" for fechado.

   O argumento *mode* pode ser "'rb'" para leitura (padrão), "'wb'"
   para substituição, "'xb'" para criação exclusiva ou "'ab'" para
   anexar. Estes podem ser equivalentemente dados como "'r'", "'w'",
   "'x'" e "'a'" respectivamente.

   Se *file* for um objeto arquivo (ao invés de um nome de arquivo
   real), um modo de "'w'" não truncará o arquivo e será equivalente a
   "'a'".

   Durante a leitura, o argumento *options* pode ser um dicionário que
   fornece parâmetros avançados de descompactação; consulte
   "DecompressionParameter" para obter informações detalhadas sobre os
   parâmetros suportados. O argumento *zstd_dict* é uma instância de
   "ZstdDict" a ser usada durante a descompactação. Durante a leitura,
   se o argumento *level* não for None, uma exceção "TypeError" será
   levantada.

   When writing, the *options* argument can be a dictionary providing
   advanced compression parameters; see "CompressionParameter" for
   detailed information about supported parameters. The *level*
   argument is the compression level to use when writing compressed
   data. Only one of *level* or *options* may be passed. The
   *zstd_dict* argument is a "ZstdDict" instance to be used during
   compression.

   "ZstdFile" oferece suporte a todos os membros especificados por
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
        "ZstdFile", pode alterar a posição do objeto arquivo
        subjacente (por exemplo, se o "ZstdFile" foi construído
        passando um objeto arquivo para *file*).

   mode

      "'rb'" para leitura e "'wb'" para escrita.

   name

      O nome do arquivo Zstandard. Equivalente ao atributo "name" do
      *objeto arquivo* subjacente.


Compactando e descompactando dados na memória
=============================================

compression.zstd.compress(data, level=None, options=None, zstd_dict=None)

   Compacta *data* (um *objeto bytes ou similar*), retornando os dados
   compactados como um objeto "bytes".

   O argumento *level* é um inteiro que controla o nível de
   compactação. *level* é uma alternativa à configuração
   "CompressionParameter.compression_level" em *options*. Use
   "bounds()" em "compression_level" para obter os valores que podem
   ser passados para *level*. Se opções avançadas de compactação forem
   necessárias, o argumento *level* deve ser omitido e, no dicionário
   *options*, o parâmetro "CompressionParameter.compression_level"
   deve ser definido.

   O argumento *options* é um dicionário Python que contém parâmetros
   de compactação avançados. As chaves e valores válidos para
   parâmetros de compactação estão documentados na documentação
   "CompressionParameter".

   O argumento *zstd_dict* é uma instância de "ZstdDict" contendo
   dados treinados para melhorar a eficiência da compactação. A função
   "train_dict()" pode ser usada para gerar um dicionário Zstandard.

compression.zstd.decompress(data, zstd_dict=None, options=None)

   Descompacta *data* (um *objeto bytes ou similar*), retornando os
   dados descompactados como um objeto "bytes".

   O argumento *options* é um dicionário Python que contém parâmetros
   de descompactação avançados. As chaves e valores válidos para
   parâmetros de compactação estão documentados na documentação
   "DecompressionParameter".

   O argumento *zstd_dict* é uma instância de "ZstdDict" contendo
   dados treinados usados durante a compactação. Este deve ser o mesmo
   dicionário Zstandard usado durante a compactação.

   Se *data* forem a concatenação de vários quadros compactados
   distintos, descompacta todos esses quadros e retorna a concatenação
   dos resultados.

class compression.zstd.ZstdCompressor(level=None, options=None, zstd_dict=None)

   Cria um objeto compactação, que pode ser usado para compactar dados
   de forma incremental.

   Para uma maneira mais conveniente de compactar um único bloco de
   dados, consulte a função a nível de módulo "compress()".

   O argumento *level* é um inteiro que controla o nível de
   compactação. *level* é uma alternativa à configuração
   "CompressionParameter.compression_level" em *options*. Use
   "bounds()" em "compression_level" para obter os valores que podem
   ser passados para *level*. Se opções avançadas de compactação forem
   necessárias, o argumento *level* deve ser omitido e, no dicionário
   *options*, o parâmetro "CompressionParameter.compression_level"
   deve ser definido.

   O argumento *options* é um dicionário Python que contém parâmetros
   de compactação avançados. As chaves e valores válidos para
   parâmetros de compactação estão documentados na documentação
   "CompressionParameter".

   O argumento *zstd_dict* é uma instância opcional de "ZstdDict"
   contendo dados treinados para melhorar a eficiência da compactação.
   A função "train_dict()" pode ser usada para gerar um dicionário
   Zstandard.

   compress(data, mode=ZstdCompressor.CONTINUE)

      Compacte *data* (um *objeto bytes ou similar*), retornando um
      objeto "bytes" com dados compactados, se possível, ou, caso
      contrário, um objeto "bytes" vazio. Alguns dos *data* podem ser
      armazenados internamente em buffer, para uso em chamadas
      posteriores a "compress()" e "flush()". Os dados retornados
      devem ser concatenados com a saída de quaisquer chamadas
      anteriores a "compress()".

      O argumento *mode* é um atributo "ZstdCompressor", podendo ser
      definido com "CONTINUE", "FLUSH_BLOCK" ou "FLUSH_FRAME".

      Quando todos os dados forem fornecidos ao compactador, chama o
      método "flush()" para finalizar o processo de compactação. Se
      "compress()" for chamado com *mode* definido como "FLUSH_FRAME",
      "flush()" não deve ser chamado, pois gravaria um novo quadro
      vazio.

   flush(mode=ZstdCompressor.FLUSH_FRAME)

      Conclui o processo de compactação, retornando um objeto "bytes"
      contendo todos os dados armazenados nos buffers internos do
      compressor.

      O argumento *mode* é um atributo "ZstdCompressor", podendo ser
      definido com "FLUSH_BLOCK" ou "FLUSH_FRAME".

   set_pledged_input_size(size)

      Especifica a quantidade de *size* dados descompactados que será
      fornecida para o próximo quadro. *size* será gravado no
      cabeçalho do quadro do próximo quadro, a menos que
      "CompressionParameter.content_size_flag" seja "False" ou "0". Um
      tamanho "0" significa que o quadro está vazio. Se *size* for
      "None", o cabeçalho do quadro omitirá o tamanho do quadro.
      Quadros que incluem o tamanho dos dados descompactados requerem
      menos memória para descompactação, especialmente em níveis de
      compactação mais altos.

      Se "last_mode" não for "FLUSH_FRAME", uma "ValueError" será
      levantada, pois o compactador não está no início de um quadro.
      Se o tamanho prometido não corresponder ao tamanho real dos
      dados fornecidos para "compress()", chamadas futuras para
      "compress()" ou "flush()" poderão levantar "ZstdError" e o
      último bloco de dados poderá ser perdido.

      Depois que "flush()" ou "compress()" são chamados com o modo
      "FLUSH_FRAME", o próximo quadro não incluirá o tamanho do quadro
      no cabeçalho, a menos que "set_pledged_input_size()" seja
      chamado novamente.

   CONTINUE

      Coleta mais dados para compactação, o que pode ou não gerar
      saída imediata. Este modo otimiza a taxa de compactação
      maximizando a quantidade de dados por bloco e quadro.

   FLUSH_BLOCK

      Conclui e grava um bloco no fluxo de dados. Os dados retornados
      até o momento podem ser descompactados imediatamente. Dados
      anteriores ainda podem ser referenciados em blocos futuros
      gerados por chamadas a "compress()", melhorando a compactação.

   FLUSH_FRAME

      Conclui e escreve um quadro. Dados futuros fornecidos a
      "compress()" serão gravados em um novo quadro e *não poderão*
      fazer referência a dados passados.

   last_mode

      O último modo passado para "compress()" ou "flush()". O valor
      pode ser "CONTINUE", "FLUSH_BLOCK" ou "FLUSH_FRAME". O valor
      inicial é "FLUSH_FRAME", significando que o compactador está no
      início de um novo quadro.

class compression.zstd.ZstdDecompressor(zstd_dict=None, options=None)

   Cria um objeto descompactador, que pode ser usado para descompactar
   dados de forma incremental.

   Para uma maneira mais conveniente de descompactar todo um fluxo
   compactado de uma só vez, consulte a função a nível de módulo
   "decompress()".

   O argumento *options* é um dicionário Python que contém parâmetros
   de descompactação avançados. As chaves e valores válidos para
   parâmetros de compactação estão documentados na documentação
   "DecompressionParameter".

   O argumento *zstd_dict* é uma instância de "ZstdDict" contendo
   dados treinados usados durante a compactação. Este deve ser o mesmo
   dicionário Zstandard usado durante a compactação.

   Nota:

     Esta classe não lidam de forma transparente entradas contendo
     múltiplos quadros compactados, ao contrário da função
     "decompress()" e da classe "ZstdFile". Para descompactar uma
     entrada com múltiplos quadros, você deve usar "decompress()",
     "ZstdFile" se estiver trabalhando com um *objeto arquivo* ou
     múltiplas instâncias de "ZstdDecompressor".

   decompress(data, max_length=-1)

      Descompacta dados *data* (um *objeto bytes ou similar*),
      retornando dados não compactados como bytes. Alguns dos *data*
      podem ser armazenados em buffer internamente, para uso em
      chamadas posteriores para "decompress()". Os dados retornados
      devem ser concatenados com a saída de qualquer chamada anterior
      para "decompress()".

      If *max_length* is non-negative, the method returns at most
      *max_length* bytes of decompressed data. If this limit is
      reached and further output can be produced (or EOF is reached),
      the "needs_input" attribute will be set to "False". In this
      case, the next call to "decompress()" may provide *data* as
      "b''" to obtain more of the output. The full content can thus be
      read like:

         process_output(d.decompress(data, max_length))
         while not d.eof and not d.needs_input:
             process_output(d.decompress(b"", max_length))

      Se todos os dados de entrada foram descompactados e retornados
      (seja porque era menor que *max_length* bytes, ou porque
      *max_length* era negativo), o atributo "needs_input" será
      definido como "True" .

      Attempting to decompress data after the end of a frame will
      raise a "EOFError". Any data found after the end of the frame is
      ignored and saved in the "unused_data" attribute.

   eof

      "True" se o marcador de fim de fluxo foi atingido.

   unused_data

      Dados encontrados após o término do fluxo compactado.

      Antes do final do fluxo ser alcançado, isso será "b''".

   needs_input

      "False" se o método "decompress()" puder fornecer mais dados
      descompactados antes de exigir uma nova entrada compactada.


Dicionários de Zstandard
========================

compression.zstd.train_dict(samples, dict_size)

   Treina um dicionário Zstandard, retornando uma instância
   "ZstdDict". Os dicionários Zstandard permitem uma compactação mais
   eficiente de dados menores, que tradicionalmente são difíceis de
   compactar devido à menor repetição. Se você estiver compactando
   vários grupos de dados semelhantes (como arquivos semelhantes), os
   dicionários Zstandard podem melhorar significativamente as taxas de
   compactação e a velocidade.

   O argumento *samples* (um iterável de objetos "bytes") é a
   população de amostras usada para treinar o dicionário Zstandard.

   O argumento *dict_size*, um inteiro, é o tamanho máximo (em bytes)
   que o dicionário Zstandard deve ter. A documentação do Zstandard
   sugere um máximo absoluto de no máximo 100 KB, mas o máximo pode
   ser menor dependendo dos dados. Dicionários maiores geralmente
   reduzem a compactação, mas melhoram as taxas de compactação.
   Dicionários menores levam a uma compactação mais rápida, mas
   reduzem a taxa de compactação.

compression.zstd.finalize_dict(zstd_dict, /, samples, dict_size, level)

   Uma função avançada para converter um dicionário Zstandard de
   "conteúdo bruto" em um dicionário Zstandard comum. Dicionários de
   "conteúdo bruto" são uma sequência de bytes que não precisa seguir
   a estrutura de um dicionário Zstandard comum.

   O argumento *zstd_dict* é uma instância "ZstdDict" com
   "dict_content" contendo o conteúdo bruto do dicionário.

   O argumento *samples* (um iterável de objetos "bytes") contém dados
   de amostra para gerar o dicionário Zstandard.

   O argumento *dict_size*, um inteiro, é o tamanho máximo (em bytes)
   que o dicionário Zstandard deve ter. Consulte "train_dict()" para
   sugestões sobre o tamanho máximo do dicionário.

   O argumento *level* (um inteiro) é o nível de compactação que se
   espera que seja passado aos compactadores usando este dicionário.
   As informações do dicionário variam para cada nível de compactação,
   portanto, ajustar o nível de compactação adequado pode tornar a
   compactação mais eficiente.

class compression.zstd.ZstdDict(dict_content, /, *, is_raw=False)

   Um invólucro para dicionários Zstandard. Dicionários podem ser
   usados para melhorar a compactação de muitos pequenos blocos de
   dados. Use "train_dict()" se precisar treinar um novo dicionário a
   partir de dados de amostra.

   O argumento *dict_content* (um *objeto bytes ou similar*) é a
   informação do dicionário já treinada.

   O argumento *is_raw*, um booleano, é um parâmetro avançado que
   controla o significado de *dict_content*. "True" significa que
   *dict_content* é um dicionário de "conteúdo bruto", sem nenhuma
   restrição de formato. "False" significa que *dict_content* é um
   dicionário Zstandard comum, criado a partir de funções Zstandard,
   por exemplo, "train_dict()" ou a CLI externa **zstd**.

   Ao passar um "ZstdDict" para uma função, os atributos
   "as_digested_dict" e "as_undigested_dict" podem controlar como o
   dicionário é carregado, passando-os como o argumento "zstd_dict",
   por exemplo, "compress(data, zstd_dict=zd.as_digested_dict)". A
   digestão de um dicionário é uma operação custosa que ocorre ao
   carregar um dicionário Zstandard. Ao fazer várias chamadas para
   compactação ou descompactação, passar um dicionário digerido
   reduzirá a sobrecarga de carregamento do dicionário.


      Diferença para compactação
      ^^^^^^^^^^^^^^^^^^^^^^^^^^

      +------------+----------------+------------+
      |            | Dicionário     | Dicionário |
      |            | resumido       | não        |
      |            |                | resumido   |
      |============|================|============|
      | Parâmetros | "window_log",  | None       |
      | avançados  | "hash_log",    |            |
      | do compac  | "chain_log",   |            |
      | tador que  | "search_log",  |            |
      | podem ser  | "min_match",   |            |
      | substituí  | "target_lengt  |            |
      | dos pelos  | h",            |            |
      | parâmetros | "strategy", "  |            |
      | do         | enable_long_d  |            |
      | dicionário | istance_match  |            |
      |            | ing", "ldm_ha  |            |
      |            | sh_log", "ldm  |            |
      |            | _min_match",   |            |
      |            | "ldm_bucket_s  |            |
      |            | ize_log", "ld  |            |
      |            | m_hash_rate_l  |            |
      |            | og" e alguns   |            |
      |            | parâmetros     |            |
      |            | não-públicos.  |            |
      +------------+----------------+------------+
      | "ZstdDict" | Sim. É mais    | Não. Se    |
      | armazena   | rápido         | você       |
      | em cache   | carregar um    | deseja     |
      | intername  | dicionário     | carregar   |
      | nte o      | resumido       | um         |
      | dicionário | novamente com  | dicionário |
      |            | o mesmo nível  | não        |
      |            | de             | digerido   |
      |            | compactação.   | várias     |
      |            |                | vezes,     |
      |            |                | considere  |
      |            |                | reutilizar |
      |            |                | um objeto  |
      |            |                | compresso  |
      |            |                | r.         |
      +------------+----------------+------------+

   Se passar um "ZstdDict" sem nenhum atributo, um dicionário não
   digerido será passado por padrão ao compactar e um dicionário
   digerido será gerado, se necessário, e passado por padrão ao
   descompactar.

      dict_content

         O conteúdo do dicionário Zstandard, um objeto "bytes". É o
         mesmo que o argumento *dict_content* no método "__init__".
         Pode ser usado com outros programas, como o programa de linha
         de comando "zstd".

      dict_id

         Identificador do dicionário Zstandard, um valor inteiro não
         negativo.

         Um valor diferente de zero significa que o dicionário é
         comum, criado por funções Zstandard e seguindo o formato
         Zstandard.

         "0" significa um dicionário de "conteúdo bruto", livre de
         qualquer restrição de formato, usado para usuários avançados.

         Nota:

           O significado de "0" para "ZstdDict.dict_id" é diferente do
           atributo "dictionary_id" da função "get_frame_info()".

      as_digested_dict

         Carrega como um dicionário resumido.

      as_undigested_dict

         Carrega como um dicionário não digerido.


Controle avançado de parâmetros
===============================

class compression.zstd.CompressionParameter

   Uma "IntEnum" contendo as chaves de parâmetros de compactação
   avançada que podem ser usadas ao compactar dados.

   O método "bounds()" pode ser usado em qualquer atributo para obter
   os valores válidos para esse parâmetro.

   Parameters are optional; any omitted parameter will have its value
   selected automatically.

   Exemplo de obtenção da delimitação inferior e superior de
   "compression_level":

      lower, upper = CompressionParameter.compression_level.bounds()

   Exemplo de configuração do atributo "window_log" para o tamanho
   máximo:

      _lower, upper = CompressionParameter.window_log.bounds()
      options = {CompressionParameter.window_log: upper}
      compress(b'venezuelan beaver cheese', options=options)

   bounds()

      Retorna a tupla de limites int, "(lower, upper)", de um
      parâmetro de compactação. Este método deve ser chamado no
      atributo cujos limites você deseja recuperar. Por exemplo, para
      obter os valores válidos para "compression_level", pode-se
      verificar o resultado de
      "CompressionParameter.compression_level.bounds()".

      Tanto o limite inferior quanto o superior são inclusivos.

   compression_level

      Um meio de alto nível para definir outros parâmetros de
      compactação que afetam a velocidade e a taxa de compactação de
      dados.

      Os níveis de compactação regulares são maiores que "0". Valores
      maiores que "20" são considerados compactação "ultra" e requerem
      mais memória do que outros níveis. Valores negativos podem ser
      usados para compensar uma compactação mais rápida por taxas de
      compactação piores.

      Define o nível como zero usa "COMPRESSION_LEVEL_DEFAULT".

   window_log

      Distância máxima de referência reversa permitida que o
      compactador pode usar ao compactar dados, expressa como potência
      de dois, "1 << window_log" bytes. Este parâmetro influencia
      bastante o uso de memória da compactação. Valores mais altos
      requerem mais memória, mas geram melhores valores de
      compactação.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   hash_log

      Tamanho da tabela de sondagem inicial, como uma potência de
      dois. O uso de memória resultante é "1 << (hash_log+2)" bytes.
      Tabelas maiores melhoram a taxa de compactação de estratégias <=
      "dfast" e melhoram a velocidade de compactação de estratégias >
      "dfast".

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   chain_log

      Tamanho da tabela de busca multiprobe, como uma potência de
      dois. O uso de memória resultante é "1 << (chain_log+2)" bytes.
      Tabelas maiores resultam em uma compactação melhor e mais lenta.
      Este parâmetro não tem efeito para a estratégia "fast". Ele
      ainda é útil ao usar a estratégia "dfast", caso em que define
      uma tabela de sondagem secundária.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   search_log

      Número de tentativas de busca, como uma potência de dois. Mais
      tentativas resultam em uma compactação melhor e mais lenta. Este
      parâmetro é inútil para as estratégias "fast" e "dfast".

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   min_match

      Tamanho mínimo das correspondências pesquisadas. Valores maiores
      aumentam a velocidade de compactação e descompactação, mas
      diminuem a taxa. Observe que o Zstandard ainda consegue
      encontrar correspondências de tamanho menor; ele apenas ajusta
      seu algoritmo de busca para procurar por esse tamanho e por
      tamanhos maiores. Para todas as estratégias < "btopt", o mínimo
      efetivo é "4"; para todas as estratégias > "fast", o máximo
      efetivo é "6".

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   target_length

      O impacto deste campo depende da "Strategy" selecionada.

      Para as estratégias "btopt", "btultra" e "btultra2", o valor é o
      comprimento de uma correspondência considerada "boa o
      suficiente" para interromper a busca. Valores maiores melhoram
      as taxas de compactação, mas a compactação é mais lenta.

      Para a estratégia "fast", é a distância entre as amostragens de
      correspondência. Valores maiores tornam a compactação mais
      rápida, mas com uma taxa de compactação pior.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   strategy

      Quanto maior o valor da estratégia selecionada, mais complexa
      será a técnica de compactação usada pelo zstd, resultando em
      taxas de compactação mais altas, mas em compactação mais lenta.

      Ver também: "Strategy"

   enable_long_distance_matching

      A correspondência de longa distância pode ser usada para
      melhorar a compactação de entradas grandes, encontrando
      correspondências maiores em distâncias maiores. Ela aumenta o
      uso de memória e o tamanho da janela.

      Os valores "True" ou "1" habilitam a correspondência a longa
      distância, enquanto os valores "False" ou "0" a desabilitam.

      Habilitar este parâmetro aumenta o tamanho padrão de
      "window_log" para 128 MiB, exceto quando expressamente definido
      com um valor diferente. Esta configuração é habilitada por
      padrão se "window_log" >= 128 MiB e a estratégia de compactação
      >= "btopt" (nível de compactação 16+).

   ldm_hash_log

      Tamanho da tabela para correspondência de longa distância, como
      uma potência de dois. Valores maiores aumentam o uso de memória
      e a taxa de compactação, mas diminuem a velocidade de
      compactação.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   ldm_min_match

      Tamanho mínimo de correspondência para correspondência de longa
      distância. Valores maiores ou muito pequenos podem
      frequentemente diminuir a taxa de compactação.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   ldm_bucket_size_log

      Tamanho do log de cada bucket na tabela hash do comparador de
      longa distância para resolução de colisões. Valores maiores
      melhoram a resolução de colisões, mas diminuem a velocidade de
      compactação.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   ldm_hash_rate_log

      Frequência de inserção/pesquisa de entradas na tabela hash do
      comparador de longa distância. Valores maiores melhoram a
      velocidade de compactação. Desvios muito grandes em relação ao
      valor padrão provavelmente resultarão em uma redução na taxa de
      compactação.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   content_size_flag

      Escreve o tamanho dos dados a serem compactados no cabeçalho do
      quadro Zstandard quando conhecido antes da compactação.

      Este sinalizador só entra em vigor nos seguintes cenários:

      * Chamando "compress()" para compactação única

      * Fornecendo todos os dados a serem compactados no quadro em uma
        única chamada "ZstdCompressor.compress()", com o modo
        "ZstdCompressor.FLUSH_FRAME".

      * Chamando "ZstdCompressor.set_pledged_input_size()" com a
        quantidade exata de dados que serão fornecidos ao compactador
        antes de qualquer chamada para "ZstdCompressor.compress()"
        para o quadro atual. "ZstdCompressor.set_pledged_input_size()"
        deve ser chamado para cada novo quadro.

      Todas as outras chamadas de compactação podem não escrever as
      informações de tamanho no cabeçalho do quadro.

      Os valores "True" ou "1" habilitam o sinalizador de tamanho de
      conteúdo, enquanto os valores "False" ou "0" o desabilitam.

   checksum_flag

      Uma soma de verificação de quatro bytes usando XXHash64 do
      conteúdo descompactado é estrita ao final de cada quadro. O
      código de descompactação do Zstandard verifica a soma de
      verificação. Se houver uma incompatibilidade, uma exceção
      "ZstdError" é levantada.

      Os valores "True" ou "1" habilitam a geração da soma de
      integridade, enquanto os valores "False" ou "0" a desabilitam.

   dict_id_flag

      Ao compactar com um "ZstdDict", o ID do dicionário é escrito no
      cabeçalho do quadro.

      Os valores "True" ou "1" habilitam o armazenamento do ID de
      dicionário, enquanto os valores "False" ou "0" o desabilitam.

   nb_workers

      Seleciona quantas threads serão geradas para compactação em
      paralelo. Quando "nb_workers" > 0, habilita a compactação
      multithread, um valor "1" significa "modo multithread de uma
      thread". Mais workers melhoram a velocidade, mas também aumentam
      o uso de memória e reduzem ligeiramente a taxa de compactação.

      Um valor zero desabilita multithreading.

   job_size

      Tamanho de um trabalho de compactação, em bytes. Este valor é
      aplicado somente quando "nb_workers" >= 1. Cada trabalho de
      compactação é concluído em paralelo, portanto, este valor pode
      impactar indiretamente o número de threads ativas.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

   overlap_log

      Define a quantidade de dados recarregados de trabalhos
      anteriores (threads) para novos trabalhos a serem usados pela
      janela "Look Behind" durante a compactação. Este valor só é
      usado quando "nb_workers" >= 1. Os valores aceitáveis variam de
      0 a 9.

         * 0 significa definir dinamicamente a quantidade de
           sobreposição

         * 1 significa nenhuma sobreposição

         * 9 significa usar o tamanho total da janela do trabalho
           anterior

      Cada incremento reduz pela metade/dobra o tamanho da
      sobreposição. "8" significa uma sobreposição de "window_size/2",
      "7" significa uma sobreposição de "window_size/4", etc.

class compression.zstd.DecompressionParameter

   An "IntEnum" containing the advanced decompression parameter keys
   that can be used when decompressing data. Parameters are optional;
   any omitted parameter will have its value selected automatically.

   O método "bounds()" pode ser usado em qualquer atributo para obter
   os valores válidos para esse parâmetro.

   Exemplo de configuração do atributo "window_log_max" para o tamanho
   máximo:

      data = compress(b'Some very long buffer of bytes...')

      _lower, upper = DecompressionParameter.window_log_max.bounds()

      options = {DecompressionParameter.window_log_max: upper}
      decompress(data, options=options)

   bounds()

      Retorna a tupla de limites int, "(lower, upper)", de um
      parâmetro de descompactação. Este método deve ser chamado no
      atributo cujos limites você deseja recuperar.

      Tanto o limite inferior quanto o superior são inclusivos.

   window_log_max

      O logaritmo na base dois do tamanho máximo da janela usada
      durante a descompactação. Isso pode ser útil para limitar a
      quantidade de memória usada ao descompactar. Um tamanho máximo
      de janela maior resulta em uma descompactação mais rápida.

      Um valor zero faz com que o valor seja selecionado
      automaticamente.

class compression.zstd.Strategy

   Um "IntEnum" contendo estratégias de compactação. Estratégias com
   números mais altos correspondem a compactações mais complexas e
   lentas.

   Nota:

     Os valores dos atributos de "Strategy" não são necessariamente
     estáveis entre as versões do zstd. Apenas a ordem dos atributos é
     confiável. Os atributos estão listados abaixo em ordem.

   As seguintes estratégias estão disponíveis:

   fast

   dfast

   greedy

   lazy

   lazy2

   btlazy2

   btopt

   btultra

   btultra2


Diversos
========

compression.zstd.get_frame_info(frame_buffer)

   Recupera um objeto "FrameInfo" contendo metadados sobre um quadro
   Zstandard. Os quadros contêm metadados relacionados aos dados
   compactados que eles armazenam.

class compression.zstd.FrameInfo

   Metadados relatados a um quadro Zstandard.

   decompressed_size

      O tamanho do conteúdo descompactado do quadro.

   dictionary_id

      Um número inteiro que representa o ID do dicionário Zstandard
      necessário para descompactar o quadro. "0" significa que o ID do
      dicionário não foi registrado no cabeçalho do quadro. Isso pode
      significar que um dicionário Zstandard não é necessário ou que o
      ID de um dicionário necessário não foi registrado.

compression.zstd.COMPRESSION_LEVEL_DEFAULT

   O nível de compactação padrão para Zstandard é: "3".

compression.zstd.zstd_version_info

   Número da versão da biblioteca zstd em tempo de execução,
   representada por uma tupla de inteiros (principal, secundária,
   lançamento).


Exemplos
========

Lendo em um arquivo compactado:

   from compression import zstd

   with zstd.open("file.zst") as f:
       file_content = f.read()

Criando um arquivo compactado:

   from compression import zstd

   data = b"Inserir dados arquivo"
   with zstd.open("file.zst", "w") as f:
       f.write(data)

Compactando dados em memória:

   from compression import zstd

   data_in = b"Insert Data Here"
   data_out = zstd.compress(data_in)

Compactação incremental:

   from compression import zstd

   comp = zstd.ZstdCompressor()
   out1 = comp.compress(b"Alguns dados\n")
   out2 = comp.compress(b"Outro pedaço de dados\n")
   out3 = comp.compress(b"Ainda mais dados\n")
   out4 = comp.flush()
   # Concatena todos os resultados parciais:
   result = b"".join([out1, out2, out3, out4])

Escrevendo dados compactados para um arquivo já aberto:

   from compression import zstd

   with open("myfile", "wb") as f:
       f.write(b"Estes dados não serão compactados\n")
       with zstd.open(f, "w") as zstf:
           zstf.write(b"Isso *vai* ser compactado\n")
       f.write(b"Não compactado\n")

Criando um arquivo compactado usando parâmetros de compactação:

   from compression import zstd

   options = {
      zstd.CompressionParameter.checksum_flag: 1
   }
   with zstd.open("file.zst", "w", options=options) as f:
       f.write(b"Se importa se eu me juntar?")
