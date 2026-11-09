# Descompacta a entrada Phar atual dentro do phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pharfileinfo.decompress.php

---

# PharFileInfo::decompress

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharFileInfo::decompress — Descompacta a entrada Phar atual dentro do phar

### Descrição

public function **PharFileInfo::decompress**(): [true](language.types.singleton.md)

Este método descompacta o arquivo dentro do arquivo Phar.
Dependendo de como o arquivo é compactado, as extensões [bzip2](ref.bzip2.md)
ou [zlib](ref.zlib.md) devem estar habilitadas para aproveitar
este recurso. Assim como acontece com todas as funcionalidades que modificam o conteúdo de
um phar, a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
deve estar desativada para funcionar se o arquivo estiver dentro de um arquivo [Phar](class.phar.md).
Arquivos dentro de arquivos [PharData](class.phardata.md) não têm
esta restrição.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se
a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
estiver ativada ou se a extensão [bzip2](ref.bzip2.md)/[zlib](ref.zlib.md)
não estiver disponível.

### Examples

**Exemplo #1 Um exemplo de **PharFileInfo::decompress()****

```
<?php
try {
    $p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar');
    $p['meuarquivo.txt'] = 'olá';
    $file = $p['meuarquivo.txt'];
    $file->compress(Phar::GZ);
    var_dump($file->isCompressed());
    $p['meuarquivo.txt']->decompress();
    var_dump($file->isCompressed());
} catch (Exception $e) {
    echo 'Criação/modificação falhou para meu.phar: ', $e;
}
?>
```

O exemplo acima produzirá:

```
int(4096)
bool(false)
```

### Veja também

- [PharFileInfo::getCompressedSize()](pharfileinfo.getcompressedsize.md) - Retorna o tamanho real do arquivo (com compactação) dentro do arquivo Phar
- [PharFileInfo::isCompressed()](pharfileinfo.iscompressed.md) - Informa se a entrada está compactada
- [PharFileInfo::compress()](pharfileinfo.compress.md) - Compacta a entrada Phar atual com zlib ou bzip2
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
