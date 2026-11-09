# Compacta todos os arquivos no arquivo tar/zip atual

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.compressfiles.php

---

# PharData::compressFiles

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::compressFiles — Compacta todos os arquivos no arquivo tar/zip atual

### Descrição

public function **PharData::compressFiles**([int](language.types.integer.md) `$compression`): [void](language.types.void.md)

Para arquivos baseados em tar, este método lança uma
[BadMethodCallException](class.badmethodcallexception.md), pois a compactação de arquivos individuais
dentro de um arquivo tar não é suportada pelo formato de arquivo. Use
[PharData::compress()](phardata.compress.md) para compactar um arquivo inteiro baseado em tar.

Para arquivos Zip, este método compacta todos os arquivos
usando a compactação especificada.
As extensões [zlib](ref.zlib.md) ou [bzip2](ref.bzip2.md)
devem estar habilitadas para aproveitar este recurso. Além disso, se algum arquivo
já estiver compactado usando bzip2/zlib, a respectiva extensão deverá ser
habilitada para descompactar os arquivos antes de compactar novamente.

### Parâmetros

`compression`
:   A compactação. Deve ser `Phar::GZ` ou
    `Phar::BZ2` para adicionar compactação; ou `Phar::NONE`
    para remover compactação.

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se
a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
estiver ativada, a extensão [zlib](ref.zlib.md)
não estiver disponível ou se algum arquivo estiver compactado usando
a bzip2 e a extensão [bzip2](ref.bzip2.md)
não estiver habilitada.

### Examples

**Exemplo #1 Um exemplo de **PharData::compressFiles()****

```
<?php
$p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar');
$p['meuarquivo.txt'] = 'olá';
$p['meuarquivo2.txt'] = 'olá';
foreach ($p as $file) {
    var_dump($file->getFileName());
    var_dump($file->isCompressed());
    var_dump($file->isCompressed(Phar::BZ2));
    var_dump($file->isCompressed(Phar::GZ));
}
$p->compressFiles(Phar::GZ);
foreach ($p as $file) {
    var_dump($file->getFileName());
    var_dump($file->isCompressed());
    var_dump($file->isCompressed(Phar::BZ2));
    var_dump($file->isCompressed(Phar::GZ));
}
?>
```

O exemplo acima produzirá:

```
string(14) "meuarquivo.txt"
bool(false)
bool(false)
bool(false)
string(15) "meuarquivo2.txt"
bool(false)
bool(false)
bool(false)
string(14) "meuarquivo.txt"
int(4096)
bool(false)
bool(true)
string(15) "meuarquivo2.txt"
int(4096)
bool(false)
bool(true)
```

### Veja também

- [PharFileInfo::getCompressedSize()](pharfileinfo.getcompressedsize.md) - Retorna o tamanho real do arquivo (com compactação) dentro do arquivo Phar
- [PharFileInfo::isCompressed()](pharfileinfo.iscompressed.md) - Informa se a entrada está compactada
- [PharFileInfo::compress()](pharfileinfo.compress.md) - Compacta a entrada Phar atual com zlib ou bzip2
- [PharFileInfo::decompress()](pharfileinfo.decompress.md) - Descompacta a entrada Phar atual dentro do phar
- [Phar::canCompress()](phar.cancompress.md) - Retorna se a extensão phar suporta compactação usando zlib ou bzip2
- [Phar::isCompressed()](phar.iscompressed.md) - Retorna Phar::GZ ou PHAR::BZ2 se todo o arquivo phar estiver compactado (.tar.gz/tar.bz e assim por diante)
- [PharData::decompressFiles()](phardata.decompressfiles.md) - Descompacta todos os arquivos no arquivo zip atual
- [Phar::getSupportedCompression()](phar.getsupportedcompression.md) - Retorna um array de algoritmos de compactação suportados
- [PharData::compress()](phardata.compress.md) - Compacta todo o arquivo tar/zip usando Gzip ou Bzip2
- [PharData::decompress()](phardata.decompress.md) - Descompacta todo o arquivo Phar

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
