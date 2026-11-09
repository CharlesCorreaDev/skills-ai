# Compacta a entrada Phar atual com zlib ou bzip2

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pharfileinfo.compress.php

---

# PharFileInfo::compress

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharFileInfo::compress — Compacta a entrada Phar atual com zlib ou bzip2

### Descrição

public function **PharFileInfo::compress**([int](language.types.integer.md) `$compression`): [true](language.types.singleton.md)

Este método compacta o arquivo dentro do arquivo Phar usando a compactação bzip2
ou zlib.
A extensão [bzip2](ref.bzip2.md) ou [zlib](ref.zlib.md)
deve estar habilitada para aproveitar
este recurso. Além disso, se o arquivo já estiver compactado,
a respectiva extensão deve ser habilitada para
descompactá-lo. Assim como acontece com todas as funcionalidades que modificam o conteúdo de
um arquivo Phar, a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
deve estar desativada para funcionar se o arquivo estiver dentro de um arquivo [Phar](class.phar.md).
Arquivos dentro de arquivos [PharData](class.phardata.md) não têm
essa restrição.

### Parâmetros

`compression`
:   A compactação deve ser **`Phar::GZ`** ou **`Phar::BZ2`**.

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se
a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
estiver ativada ou se a extensão [bzip2](ref.bzip2.md)/[zlib](ref.zlib.md)
não estiver disponível.

### Examples

**Exemplo #1 Um exemplo de **PharFileInfo::compress()****

```
<?php
try {
    $p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar');
    $p['meuarquivo.txt'] = 'olá';
    $file = $p['meuarquivo.txt'];
    var_dump($file->isCompressed(Phar::BZ2));
    $p['meuarquivo.txt']->compress(Phar::BZ2);
    var_dump($file->isCompressed(Phar::BZ2));
} catch (Exception $e) {
    echo 'Operações de criação/modificação em meu.phar falhou: ', $e;
}
?>
```

O exemplo acima produzirá:

```
bool(false)
bool(true)
```

### Veja também

- [PharFileInfo::getCompressedSize()](pharfileinfo.getcompressedsize.md) - Retorna o tamanho real do arquivo (com compactação) dentro do arquivo Phar
- [PharFileInfo::isCompressed()](pharfileinfo.iscompressed.md) - Informa se a entrada está compactada
- [PharFileInfo::decompress()](pharfileinfo.decompress.md) - Descompacta a entrada Phar atual dentro do phar
- [Phar::canCompress()](phar.cancompress.md) - Retorna se a extensão phar suporta compactação usando zlib ou bzip2
- [Phar::isCompressed()](phar.iscompressed.md) - Retorna Phar::GZ ou PHAR::BZ2 se todo o arquivo phar estiver compactado (.tar.gz/tar.bz e assim por diante)
- [Phar::compressFiles()](phar.compressfiles.md) - Compacta todos os arquivos no arquivo Phar atual
- [Phar::decompressFiles()](phar.decompressfiles.md) - Descompacta todos os arquivos no arquivo Phar atual
- [Phar::compress()](phar.compress.md) - Compacta todo o arquivo Phar usando compactação Gzip ou Bzip2
- [Phar::decompress()](phar.decompress.md) - Descompacta todo o arquivo Phar
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
