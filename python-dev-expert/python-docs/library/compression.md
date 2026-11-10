O pacote "compression"
**********************

Adicionado na versão 3.14.

O pacote "compression" contém os módulos de compressão canônicos, que
contêm interfaces para diversos algoritmos de compressão. Alguns
desses módulos historicamente estiveram disponíveis como módulos
separados; estes continuarão disponíveis com seus nomes originais por
motivos de compatibilidade e não serão removidos sem um ciclo de
descontinuação. O uso de módulos em "compression" é incentivado sempre
que possível.

* "compression.bz2" -- Re-exporta "bz2"

* "compression.gzip" -- Re-exporta "gzip"

* "compression.lzma" -- Re-exporta "lzma"

* "compression.zlib" -- Re-exporta "zlib"

* "compression.zstd" -- Invólucro para a biblioteca de compressão
  Zstandard
