"zlib" --- Compactação compatível com **gzip**
**********************************************

======================================================================

Para aplicações que requerem compactação de dados, as funções neste
módulo permitem compactação e descompactação, utilizando a biblioteca
zlib.

Este é um *módulo opcional*. Se ele estiver faltando na sua cópia do
CPython, procure a documentação do seu distribuidor (ou seja, quem lhe
forneceu o Python). Se você for o distribuidor, consulte Requisitos
para módulos opcionais.

As funções do zlib têm muitas opções e geralmente precisam ser usadas
em uma ordem específica. Esta documentação não tenta cobrir todas as
permutações; consulte o manual do zlib para obter informações
oficiais.

Para leitura e escrita de arquivos ".gz", consulte o módulo "gzip".

A exceção e as funções disponíveis neste módulo são:

exception zlib.error

   Exceção levantada em erros de compactação e descompactação.

zlib.adler32(data, value=1, /)

   Calcula uma soma de verificação Adler-32 de *data*. (Uma soma de
   verificação Adler-32 é quase tão confiável quanto uma CRC32, mas
   pode ser calculada muito mais rapidamente.) O resultado é um número
   inteiro sem sinal de 32 bits. Se *value* estiver presente, ele será
   usado como o valor inicial da soma de verificação; caso contrário,
   um valor padrão de 1 é usado. A passagem de *value* permite
   calcular uma soma de verificação em execução através da
   concatenação de várias entradas. O algoritmo não é
   criptograficamente forte e não deve ser usado para autenticação ou
   assinaturas digitais. Como o algoritmo foi projetado para uso como
   um algoritmo de soma de verificação, não é adequado para uso como
   um algoritmo de hash geral.

   Alterado na versão 3.0: O resultado é sempre sem sinal.

zlib.adler32_combine(adler1, adler2, len2, /)

   Combine two Adler-32 checksums into one.

   Given the Adler-32 checksum *adler1* of a sequence "A" and the
   Adler-32 checksum *adler2* of a sequence "B" of length *len2*,
   return the Adler-32 checksum of "A" and "B" concatenated.

   This function is typically useful to combine Adler-32 checksums
   that were concurrently computed. To compute checksums sequentially,
   use "adler32()" with the running checksum as the "value" argument.

   Adicionado na versão 3.15.

zlib.compress(data, /, level=Z_DEFAULT_COMPRESSION, wbits=MAX_WBITS)

   Compacta os bytes em *data*, retornando um objeto bytes contendo
   dados compactados. *level* é um inteiro de "0" a "9" ou "-1" que
   controla o nível de compactação; Consulte "Z_BEST_SPEED" ("1"),
   "Z_BEST_COMPRESSION" ("9"), "Z_NO_COMPRESSION" ("0") e o padrão,
   "Z_DEFAULT_COMPRESSION" ("-1") para obter mais informações sobre
   esses valores.

   O argumento *wbits* controla o tamanho do buffer do histórico (ou o
   "tamanho da janela") usado ao compactar dados e se um cabeçalho e
   um trailer estão incluídos na saída. Pode levar vários intervalos
   de valores, padronizando para "15" ("MAX_WBITS"):

   * +9 a +15: o logaritmo de base dois do tamanho da janela, que
     varia entre 512 e 32768. Valores maiores produzem melhor
     compactação às custas de maior uso de memória. A saída resultante
     incluirá um cabeçalho e uma sequência específicos para zlib.

   * -9 a -15: Usa o valor absoluto de *wbits* como o logaritmo do
     tamanho da janela, enquanto produz um fluxo de saída bruto sem
     cabeçalho ou soma de verificação à direita.

   * +25 a +31 = 16 + (9 a 15): Usa os 4 bits baixos do valor como
     logaritmo do tamanho da janela, incluindo um cabeçalho básico
     **gzip** e a soma de verificação à direita na saída.

   Levanta uma exceção do tipo "error", se ocorrer algum erro.

   Alterado na versão 3.6: *level* pode agora ser usado como um
   palavra reservada nomeada.

   Alterado na versão 3.11: O parâmetro *wbits* agora está disponível
   para definir janelas de bits e tipo de compactação.

zlib.compressobj(level=Z_DEFAULT_COMPRESSION, method=DEFLATED, wbits=MAX_WBITS, memLevel=DEF_MEM_LEVEL, strategy=Z_DEFAULT_STRATEGY[, zdict])

   Retorna um objeto de compactação, a ser usado para compactar fluxos
   de dados que não cabem na memória de uma só vez.

   *level* é um nível de compactação -- um inteiro de "0" a "9" ou
   "-1". Consulte "Z_BEST_SPEED" ("1"), "Z_BEST_COMPRESSION" ("9"),
   "Z_NO_COMPRESSION" ("0") e o padrão, "Z_DEFAULT_COMPRESSION" ("-1")
   para obter mais informações sobre esses valores.

   *method* é o algoritmo de compactação. Atualmente, o único valor
   suportado é "DEFLATED".

   O parâmetro *wbits* controla o tamanho do histórico buffer (ou o
   "tamanho da janela do buffer") e qual o formato do cabeçalho e do
   trailer serão usados. Ele tem o mesmo significado que o descrito
   para compress().

   O argumento *memLevel* controla a quantidade de memória usada para
   o estado de compactação interno. Os valores válidos variam de "1" a
   "9". Valores mais altos usam mais memória, mas são mais rápidos e
   produzem uma saída menor.

   *strategy* é usado para ajustar o algoritmo de compactação. Os
   valores possíveis são "Z_DEFAULT_STRATEGY", "Z_FILTERED",
   "Z_HUFFMAN_ONLY", "Z_RLE" e "Z_FIXED".

   *zdict* é um dicionário de compactação predefinido. Esta é uma
   sequência de bytes (como um objeto "bytes") que contém
   subsequências que se espera que ocorram com frequência nos dados a
   serem compactados. As subsequências que se espera serem mais comuns
   devem aparecer no final do dicionário.

   Alterado na versão 3.3: Adicionado o suporte ao parâmetro e
   argumento nomeado *zdict*.

zlib.crc32(data, value=0, /)

   Calcula uma soma de verificação CRC (Cyclic Redundancy Check) de
   *data*. O resultado é um número inteiro sem sinal de 32 bits. Se
   *value* estiver presente, ele será usado como o valor inicial da
   soma de verificação; caso contrário, um valor padrão de 1 é usado.
   A passagem de *value* permite calcular uma soma de verificação em
   execução através da concatenação de várias entradas. O algoritmo
   não é criptograficamente forte e não deve ser usado para
   autenticação ou assinaturas digitais. Como o algoritmo foi
   projetado para uso como um algoritmo de soma de verificação, não é
   adequado para uso como um algoritmo de hash geral.

   Alterado na versão 3.0: O resultado é sempre sem sinal.

zlib.crc32_combine(crc1, crc2, len2, /)

   Combine two CRC-32 checksums into one.

   Given the CRC-32 checksum *crc1* of a sequence "A" and the CRC-32
   checksum *crc2* of a sequence "B" of length *len2*, return the
   CRC-32 checksum of "A" and "B" concatenated.

   This function is typically useful to combine CRC-32 checksums that
   were concurrently computed. To compute checksums sequentially, use
   "crc32()" with the running checksum as the "value" argument.

   Adicionado na versão 3.15.

zlib.decompress(data, /, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE)

   Descompacta os bytes em *data*, retornando um objeto de bytes que
   contém os dados não compactados. O parâmetro *wbits* depende do
   formato de *data* e é discutido mais abaixo. Se *bufsize* for
   fornecido, ele será usado como o tamanho inicial do buffer de
   saída. Levanta a exceção "error" se ocorrer algum erro.

   O parâmetro *wbits* controla o tamanho do buffer do histórico (ou
   "tamanho da janela") e qual formato de cabeçalho e sequência é
   esperado. É semelhante ao parâmetro para "compressobj()", mas
   aceita mais intervalos de valores:

   * +8 a +15: O logaritmo de base dois do tamanho da janela. A
     entrada deve incluir um cabeçalho e uma sequência de zlib.

   * 0: Determina automaticamente o tamanho da janela no cabeçalho
     zlib. Suportado apenas desde o zlib 1.2.3.5.

   * −8 a −15: Usa o valor absoluto de *wbits* como o logaritmo do
     tamanho da janela. A entrada deve ser um fluxo bruto sem
     cabeçalho ou sequência.

   * +24 a +31 = 16 + (8 a 15): Usa os 4 bits baixos do valor como
     logaritmo do tamanho da janela. A entrada deve incluir um
     cabeçalho e sequência de gzip.

   * +40 a +47 = 32 + (8 a 15): Usa os 4 bits baixos do valor como
     logaritmo do tamanho da janela e aceita automaticamente o formato
     zlib ou gzip.

   Ao descompactar um fluxo, o tamanho da janela não deve ser menor
   que o tamanho originalmente usado para compactar o fluxo; o uso de
   um valor muito pequeno pode resultar em uma exceção "error". O
   valor padrão *wbits* corresponde ao maior tamanho da janela e
   requer que um cabeçalho e uma sequência de zlib sejam incluídos.

   *bufsize* é o tamanho inicial do buffer usado para armazenar dados
   descompactados. Se for necessário mais espaço, o tamanho do buffer
   será aumentado conforme necessário, para que você não precise obter
   esse valor exatamente correto; sintonizando, apenas algumas
   chamadas serão salvas em "malloc()".

   Alterado na versão 3.6: *wbits* e *bufsize* podem ser usados como
   argumentos nomeados.

zlib.decompressobj(wbits=MAX_WBITS, zdict=b'')

   Retorna um objeto descompactado, a ser usado para descompactar
   fluxos de dados que não cabem na memória de uma só vez.

   O parâmetro *wbits* controla o tamanho do histórico do buffer (ou o
   "tamanho da janela do buffer") e qual formato do cabeçalho e
   trailer são esperados. Ele tem o mesmo significado que o descrito
   para decompress().

   O parâmetro *zdict* especifica uma dicionário predefinido de
   compactação. Se fornecido, deve ser o mesmo dicionário usado pelo
   compactador que produziu os dados a serem descompactados.

   Nota:

     Se *zdict* for um objeto mutável (como um "bytearray"), você não
     deve modificar seu conteúdo entre a chamada de "decompressobj()"
     e a primeira chamada para o método de descompatação
     "decompress()".

   Alterado na versão 3.3: Adicionado o parâmetro *zdict*.

Um objeto do tipo Compress oferece suporte aos seguintes métodos:

Compress.compress(data, /)

   Comprime *data*, retornando um objeto de bytes que contém dados
   compactados para pelo menos parte dos dados em *data*.  Esses dados
   devem ser concatenados à saída produzida por quaisquer chamadas
   anteriores ao método "compress()". Algumas entradas podem ser
   mantidas em buffers internos para processamento posterior.

Compress.flush(mode=Z_FINISH, /)

   Toda a entrada pendente é processada e um objeto de bytes contendo
   a saída compactada restante é retornado.  O *mode* pode ser
   selecionado entre constantes "Z_NO_FLUSH" , "Z_PARTIAL_FLUSH",
   "Z_SYNC_FLUSH", "Z_FULL_FLUSH", "Z_BLOCK" ou "Z_FINISH", com o
   padrão sendo "Z_FINISH". Exceto "Z_FINISH", todas as demais
   constantes permitem a compactação de mais bytestrings de dados,
   enquanto "Z_FINISH" finaliza o fluxo compactado e impede a
   compactação de mais dados.  Depois de chamar "flush()" com *mode*
   definido como "Z_FINISH", o método "compress()" não pode ser
   chamado novamente; a única ação restante possível é excluir o
   objeto.

Compress.copy()

   Retorna uma cópia do objeto de compactação.  Isso pode ser usado
   para compactar com eficiência um conjunto de dados que compartilham
   um prefixo inicial comum.

Alterado na versão 3.8: As funções "copy.copy()" e "copy.deepcopy()"
foram adicionadas como suporte para a compactação de objetos.

Um objeto de descompactação oferece suporte aos seguintes métodos:

Decompress.unused_data

   Um objeto de bytes que contém todos os bytes após o final dos dados
   compactados. Ou seja, ele permanece "b""" até que o último byte que
   contém dados compactados esteja disponível.  Se todo o bytestring
   contiver dados compactados, este será "b""", um objeto de bytes
   vazio.

Decompress.unconsumed_tail

   Um objeto de bytes que contém todos os dados que não foram
   consumidos pela última chamada "decompress()" porque excederam o
   limite dos dados não compactados no buffer.  Esses dados ainda não
   foram vistos pela zlib, portanto, você deve alimentá-los
   (possivelmente com outros dados concatenados a eles) em uma chamada
   subsequente para o método "decompress()" e, com isso, obter a saída
   correta.

Decompress.eof

   Um booleano indicando se o fim do fluxo de dados compactados foi
   alcançado.

   Isso permite distinguir entre um fluxo compactado formado
   corretamente e um fluxo incompleto ou truncado.

   Adicionado na versão 3.3.

Decompress.decompress(data, /, max_length=0)

   Descompacta *data*, retornando um objeto de bytes que contém os
   dados não compactados correspondentes a pelo menos uma parte dos
   dados em *string*. Esses dados devem ser concatenados com a saída
   produzida por quaisquer chamadas anteriores ao método
   "decompress()" . Alguns dos dados de entrada podem ser preservados
   em buffers internos para processamento posterior.

   If the optional parameter *max_length* is non-zero then the return
   value will be no longer than *max_length*. This may mean that not
   all of the compressed input can be processed; and unconsumed data
   will be stored in the attribute "unconsumed_tail". This bytestring
   must be passed to a subsequent call to "decompress()" if
   decompression is to continue.  If *max_length* is zero then the
   whole input is decompressed, and "unconsumed_tail" is empty. For
   example, the full content could be read like:

      process_output(d.decompress(data, max_length))
      while chunk := d.decompress(d.unconsumed_tail, max_length):
          process_output(chunk)

   Alterado na versão 3.6: *max_length* pode ser usado como argumento
   nomeado.

Decompress.flush(length=DEF_BUF_SIZE, /)

   Toda a entrada que estiver pendente é processada e um objeto de
   bytes contendo a saída descompactada restante é retornado.  Depois
   de chamar "flush()", o método "decompress()" não pode ser chamado
   novamente; a única ação possível é excluir o objeto.

   O parâmetro opcional *comprimento* define o tamanho inicial da
   saída do buffer.

Decompress.copy()

   Retorna uma cópia do objeto de descompactação. Isso pode ser usado
   para salvar o estado do descompactador no meio do fluxo de dados, a
   fim de acelerar as buscas aleatórias no fluxo em um ponto futuro.

Alterado na versão 3.8: As funções "copy.copy()" e "copy.deepcopy()"
foram adicionadas como suporte para a objetos de descompactação.

As constantes a seguir estão disponíveis para configurar o
comportamento de compactação e descompactação:

zlib.DEFLATED

   O método de compactação de deflação.

zlib.MAX_WBITS

   O tamanho máximo da janela, expresso como uma potência de 2. Por
   exemplo, se "MAX_WBITS" for "15", isso resultará em um tamanho de
   janela de "32 KiB".

zlib.DEF_MEM_LEVEL

   O nível de memória padrão para objetos de compactação.

zlib.DEF_BUF_SIZE

   O tamanho padrão do buffer para operações de descompactação.

zlib.Z_NO_COMPRESSION

   Nível de compactação "0"; sem compactação.

   Adicionado na versão 3.6.

zlib.Z_BEST_SPEED

   Nível de compactação "1"; mais rápido e produz a menor compactação.

zlib.Z_BEST_COMPRESSION

   Nível de compactação "9"; mais lento e produz a maior compactação.

zlib.Z_DEFAULT_COMPRESSION

   Nível de compactação padrão ("-1"); um meio-termo entre velocidade
   e compactação. Atualmente equivalente ao nível de compactação "6".

zlib.Z_DEFAULT_STRATEGY

   Estratégia de compactação padrão, para dados normais.

zlib.Z_FILTERED

   Estratégia de compactação para dados produzidos por um filtro (ou
   preditor).

zlib.Z_HUFFMAN_ONLY

   Estratégia de compactação que força codificação Huffman apenas.

zlib.Z_RLE

   Estratégia de compactação que limita distâncias de correspondência
   a um (codificação run-length).

   Esta constante só estará disponível se o Python foi construído com
   zlib 1.2.0.1 ou superior.

   Adicionado na versão 3.6.

zlib.Z_FIXED

   Estratégia de compactação que impede o uso de códigos dinâmicos de
   Huffman.

   Esta constante só estará disponível se o Python foi construído com
   zlib 1.2.2.2 ou superior.

   Adicionado na versão 3.6.

zlib.Z_NO_FLUSH

   Modo de saída "0". Nenhum comportamento especial de saída.

   Adicionado na versão 3.6.

zlib.Z_PARTIAL_FLUSH

   Modo de saída "1". Emite o máximo de saída possível.

zlib.Z_SYNC_FLUSH

   Modo de saída "2". Toda saída é emitida e é alinhada a um limite de
   bytes.

zlib.Z_FULL_FLUSH

   Modo de saída "3". Toda a saída é emitida e o estado de compactação
   é redefinido.

zlib.Z_FINISH

   Modo de saída "4". Toda entrada pendente é processada, nenhuma
   outra entrada é esperada.

zlib.Z_BLOCK

   Modo de saída "5". Um bloco de deflação é concluído e emitido.

   Esta constante só estará disponível se o Python foi construído com
   zlib 1.2.2.2 ou superior.

   Adicionado na versão 3.6.

zlib.Z_TREES

   Modo de saída "6", para operações de inflação. Instrui a inflação a
   retornar ao atingir o próximo limite do bloco de desinflação.

   Esta constante está disponível apenas se o Python foi compilado com
   zlib 1.2.3.4 ou superior.

   Adicionado na versão 3.6.

As informações sobre o versão da biblioteca zlib em uso estão
disponíveis no seguinte constantes:

zlib.ZLIB_VERSION

   Uma string com a versão da biblioteca zlib que foi usada para
   construir o módulo. Isso pode ser diferente da biblioteca zlib
   realmente usada no tempo de execução, que está disponível como
   "ZLIB_RUNTIME_VERSION".

zlib.ZLIB_RUNTIME_VERSION

   Uma string com a versão da biblioteca zlib atualmente utilizada
   pelo interpretador.

   Adicionado na versão 3.3.

zlib.ZLIBNG_VERSION

   A string de versão da biblioteca zlib-ng que foi usada para
   construir o módulo, caso o zlib-ng tenha sido usado. Quando
   presentes, as constantes "ZLIB_VERSION" e "ZLIB_RUNTIME_VERSION"
   refletem a versão da API zlib fornecida pelo zlib-ng.

   Se zlib-ng não foi usado para construir o módulo, esta constante
   estará ausente.

   Adicionado na versão 3.14.

Ver também:

  módulo "gzip"
     Leia e escreva arquivos no formato **gzip**

  https://www.zlib.net
     A página inicial da biblioteca zlib.

  https://www.zlib.net/manual.html
     O manual da zlib explica a semântica e uso de diversas funções
     desta biblioteca.

  Caso a (des)compactação do gzip seja um gargalo, o pacote python-
  isal acelera a (des)compactação com uma API quase sempre compatível.
