Compressão de Dados e Arquivamento
**********************************

Os módulos descritos neste capítulo oferecem suporte à compressão de
dados com os algoritmos zlib, gzip, bzip2, lzma e zstd, e a criação de
arquivos no formato ZIP e tar. Veja também Operações de arquivamento
fornecido pelo módulo "shutil".

* O pacote "compression"

* "compression.zstd" --- Compactação compatível com o formato
  Zstandard

  * Exceções

  * Lendo e escrevendo arquivos compactados

  * Compactando e descompactando dados na memória

  * Dicionários de Zstandard

  * Controle avançado de parâmetros

  * Diversos

  * Exemplos

* "zlib" --- Compactação compatível com **gzip**

* "gzip" --- Suporte para arquivos **gzip**

  * Exemplos de uso

  * Interface de linha de comando

    * Opções de linha de comando

* "bz2" --- Suporte para compressão **bzip2**

  * (Des)compressão de arquivos

  * (Des)compressão incremental

  * (De)compressão de uma só vez (one-shot)

  * Exemplos de uso

* "lzma" --- Compressão usando o algoritmo LZMA

  * Lendo e escrevendo arquivos comprimidos

  * Comprimindo e descomprimindo dados na memória

  * Diversos

  * Especificando cadeias de filtros personalizadas

  * Constantes

  * Exemplos

* "zipfile" --- Trabalha com arquivos ZIP

  * Objetos ZipFile

  * Objetos Path

  * Objetos PyZipFile

  * Objetos ZipInfo

  * Interface de linha de comando

    * Opções de linha de comando

  * Armadilhas de descompressão

    * Do próprio arquivo

    * Limitações do sistema de arquivos

    * Limitações de recursos

    * Interrupção

    * Comportamentos padrão da extração

* "tarfile" --- Ler e gravar arquivos do tipo tar

  * Objetos TarFile

  * Objetos TarInfo

  * Filtros de extração

    * Default named filters

    * Filter errors

    * Dicas para verificação adicional

    * Suporte a versões mais antigas do Python

    * Stateful extraction filter example

  * Interface de Linha de Comando

    * Opções de linha de comando

  * Exemplos

    * Reading examples

    * Writing examples

  * Formatos tar suportados

  * Problemas de Unicode
