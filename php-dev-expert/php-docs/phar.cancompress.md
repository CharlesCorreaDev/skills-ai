# Retorna se a extensão phar suporta compactação usando zlib ou bzip2

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.cancompress.php

---

# Phar::canCompress

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::canCompress — Retorna se a extensão phar suporta compactação usando zlib ou bzip2

### Descrição

final public static function **Phar::canCompress**([int](language.types.integer.md) `$compression` = 0): [bool](language.types.boolean.md)

Isso deve ser usado para testar se a compactação é possível antes de
carregar um arquivo phar contendo arquivos compactados.

### Parâmetros

`compression`
:   Tanto `Phar::GZ` quanto `Phar::BZ2` podem ser
    usados ​​para testar se a compressão é possível com um algoritmo de compressão
    específico (zlib ou bzip2).

### Valor Retornado

**`true`** se a compactação/descompactação estiver disponível, **`false`** caso contrário.

### Examples

**Exemplo #1 Um exemplo de **Phar::canCompress()****

```
<?php
if (Phar::canCompress()) {
    echo file_get_contents('phar://pharcompactado.phar/internos/arquivo.txt');
} else {
    echo 'nenhuma compactação disponível';
}
?>
```

### Veja também

- [PharFileInfo::getCompressedSize()](pharfileinfo.getcompressedsize.md) - Retorna o tamanho real do arquivo (com compactação) dentro do arquivo Phar
- [PharFileInfo::isCompressed()](pharfileinfo.iscompressed.md) - Informa se a entrada está compactada
- [PharFileInfo::compress()](pharfileinfo.compress.md) - Compacta a entrada Phar atual com zlib ou bzip2
- [PharFileInfo::decompress()](pharfileinfo.decompress.md) - Descompacta a entrada Phar atual dentro do phar
- [Phar::isCompressed()](phar.iscompressed.md) - Retorna Phar::GZ ou PHAR::BZ2 se todo o arquivo phar estiver compactado (.tar.gz/tar.bz e assim por diante)
- [Phar::compressFiles()](phar.compressfiles.md) - Compacta todos os arquivos no arquivo Phar atual
- [Phar::decompressFiles()](phar.decompressfiles.md) - Descompacta todos os arquivos no arquivo Phar atual
- [Phar::getSupportedCompression()](phar.getsupportedcompression.md) - Retorna um array de algoritmos de compactação suportados
- [Phar::convertToExecutable()](phar.converttoexecutable.md) - Converte um arquivo phar em outro formato de arquivo executável phar
- [Phar::convertToData()](phar.converttodata.md) - Converte um arquivo phar em um arquivo tar ou zip não executável

`↑` and `↓` to navigate •
`Enter` to select •
`Esc` to close • `/` to open

document.addEventListener("DOMContentLoaded", function() {
/\*{{{Search Modal\*/
const language = 'local';
initSearchModal();
initPHPSearch(language).then((searchCallback) => {
initSearchUI({language, searchCallback, limit: 30});
});
/\*}}}\*/
});
