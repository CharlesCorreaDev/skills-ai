# Retorna Phar::GZ ou PHAR::BZ2 se todo o arquivo phar estiver compactado (.tar.gz/tar.bz e assim por diante)

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.iscompressed.php

---

# Phar::isCompressed

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::isCompressed — Retorna Phar::GZ ou PHAR::BZ2 se todo o arquivo phar estiver compactado (.tar.gz/tar.bz e assim por diante)

### Descrição

public function **Phar::isCompressed**(): [int](language.types.integer.md)|[false](language.types.singleton.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Retorna Phar::GZ ou PHAR::BZ2 se todo o arquivo phar estiver compactado
(.tar.gz/tar.bz e assim por diante). Arquivos phar baseados em ZIP não podem ser compactados como um
arquivo e, portanto, este método sempre retornará **`false`** se um arquivo phar baseado em ZIP for consultado.

### Parâmetros

Sem parâmetros.

### Valor Retornado

`Phar::GZ`, `Phar::BZ2` ou **`false`**.

### Examples

**Exemplo #1 Um exemplo de **Phar::isCompressed()****

```
<?php
try {
    $phar1 = new Phar('meuphar.zip.phar');
    var_dump($phar1->isCompressed());
    $phar2 = new Phar('meudescompactado.tar.phar');
    var_dump($phar2->isCompressed());
    $phar2->compress(Phar::GZ);
    var_dump($phar2->isCompressed() == Phar::GZ);
} catch (Exception $e) {
}
?>
```

O exemplo acima produzirá:

```
bool(false)
bool(false)
bool(true)
```

### Veja também

- [PharFileInfo::getCompressedSize()](pharfileinfo.getcompressedsize.md) - Retorna o tamanho real do arquivo (com compactação) dentro do arquivo Phar
- [PharFileInfo::isCompressed()](pharfileinfo.iscompressed.md) - Informa se a entrada está compactada
- [PharFileInfo::decompress()](pharfileinfo.decompress.md) - Descompacta a entrada Phar atual dentro do phar
- [PharFileInfo::compress()](pharfileinfo.compress.md) - Compacta a entrada Phar atual com zlib ou bzip2
- [Phar::decompress()](phar.decompress.md) - Descompacta todo o arquivo Phar
- [Phar::compress()](phar.compress.md) - Compacta todo o arquivo Phar usando compactação Gzip ou Bzip2
- [Phar::canCompress()](phar.cancompress.md) - Retorna se a extensão phar suporta compactação usando zlib ou bzip2
- [Phar::compressFiles()](phar.compressfiles.md) - Compacta todos os arquivos no arquivo Phar atual
- [Phar::decompressFiles()](phar.decompressfiles.md) - Descompacta todos os arquivos no arquivo Phar atual
- [Phar::getSupportedCompression()](phar.getsupportedcompression.md) - Retorna um array de algoritmos de compactação suportados

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
