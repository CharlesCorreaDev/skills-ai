# Descompacta todo o arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.decompress.php

---

# PharData::decompress

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::decompress — Descompacta todo o arquivo Phar

### Descrição

public function **PharData::decompress**([?](language.types.null.md)[string](language.types.string.md) `$extension` = **`null`**): [?](language.types.null.md)[PharData](class.phardata.md)

Para arquivos baseados em tar, esse método descompacta o arquivo inteiro.

Para arquivos Zip, este método falha com uma exceção.
A extensão [zlib](ref.zlib.md) deve ser habilitada para descompactar
um arquivo compactado com gzip, e a
[bzip2](ref.bzip2.md) deve ser
habilitada para descompactar um arquivo compactado com bzip2.

Além disso, este método renomeia automaticamente a extensão do arquivo compactado,
`.tar` por padrão.
Como alternativa, uma extensão de arquivo pode ser especificada com o parâmetro
`extension`.

### Parâmetros

`extension`
:   Para descompactação, a extensão de arquivo padrão
    é `.tar`.
    Use este parâmetro para especificar outra extensão de arquivo. Esteja ciente de que
    apenas arquivos executáveis ​​podem conter `.phar` em seus nomes.

### Valor Retornado

Um objeto [PharData](class.phardata.md) é retornado em caso de sucesso,
ou **`null`** em caso de falha.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se
a extensão [zlib](ref.zlib.md)
não estiver disponível ou se a extensão [bzip2](ref.bzip2.md)
não estiver habilitada.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `extension` agora é anulável. |

### Examples

**Exemplo #1 Um exemplo de **PharData::decompress()****

```
<?php
$p = new PharData('/caminho/para/meu.tar.gz');
$p->decompress(); // cria /caminho/para/meu.tar
?>
```

### Veja também

- [PharFileInfo::getCompressedSize()](pharfileinfo.getcompressedsize.md) - Retorna o tamanho real do arquivo (com compactação) dentro do arquivo Phar
- [PharFileInfo::isCompressed()](pharfileinfo.iscompressed.md) - Informa se a entrada está compactada
- [PharFileInfo::compress()](pharfileinfo.compress.md) - Compacta a entrada Phar atual com zlib ou bzip2
- [PharFileInfo::decompress()](pharfileinfo.decompress.md) - Descompacta a entrada Phar atual dentro do phar
- [PharData::compress()](phardata.compress.md) - Compacta todo o arquivo tar/zip usando Gzip ou Bzip2
- [Phar::canCompress()](phar.cancompress.md) - Retorna se a extensão phar suporta compactação usando zlib ou bzip2
- [Phar::isCompressed()](phar.iscompressed.md) - Retorna Phar::GZ ou PHAR::BZ2 se todo o arquivo phar estiver compactado (.tar.gz/tar.bz e assim por diante)
- [PharData::compress()](phardata.compress.md) - Compacta todo o arquivo tar/zip usando Gzip ou Bzip2
- [Phar::getSupportedCompression()](phar.getsupportedcompression.md) - Retorna um array de algoritmos de compactação suportados
- [PharData::compressFiles()](phardata.compressfiles.md) - Compacta todos os arquivos no arquivo tar/zip atual
- [PharData::decompressFiles()](phardata.decompressfiles.md) - Descompacta todos os arquivos no arquivo zip atual

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
