# Compacta todo o arquivo Phar usando compactação Gzip ou Bzip2

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.compress.php

---

# Phar::compress

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::compress — Compacta todo o arquivo Phar usando compactação Gzip ou Bzip2

### Descrição

public function **Phar::compress**([int](language.types.integer.md) `$compression`, [?](language.types.null.md)[string](language.types.string.md) `$extension` = **`null`**): [?](language.types.null.md)[Phar](class.phar.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Para arquivos PHAR baseados em tar e PHAR, este método compacta o arquivo inteiro usando
compactação gzip ou bzip2. O arquivo resultante pode ser processado com o comando
gunzip/bunzip ou acessado direta e transparentemente com a
extensão Phar.

Para arquivos phar baseados em Zip, este método falha com uma exceção.
A extensão [zlib](ref.zlib.md) deve estar habilitada para compactar
com compactação gzip, a extensão [bzip2](ref.bzip2.md) deve estar
habilitada para compactar com compactação bzip2.
Como acontece com todas as funcionalidades que modificam o conteúdo de um phar, a variável INI
[phar.readonly](phar.configuration.md#ini.phar.readonly) deve estar desativada
para funcionar.

Além disso, este método renomeia automaticamente o arquivo, anexando `.gz`,
`.bz2` ou removendo a extensão se `Phar::NONE` for passado para
remover a compactação. Alternativamente, uma extensão de arquivo pode ser especificada com o segundo
parâmetro.

### Parâmetros

`compression`
:   A compactação deve ser `Phar::GZ`,
    `Phar::BZ2` para adicionar compactação ou `Phar::NONE`
    para remover compactação.

`extension`
:   Por padrão, a extensão é `.phar.gz`
    ou `.phar.bz2` para compactar arquivos phar, e
    `.phar.tar.gz` ou `.phar.tar.bz2` para
    compactar arquivos tar. Para descompactação, as extensões de arquivo padrão
    são `.phar` e `.phar.tar`.

### Valor Retornado

Retorna um objeto [Phar](class.phar.md) ou **`null`** em caso de falha.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se
a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
estiver ativada, a extensão [zlib](ref.zlib.md)
não estiver disponível ou a extensão [bzip2](ref.bzip2.md)
não estiver habilitada.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `extension` agora é anulável. |

### Examples

**Exemplo #1 Um exemplo de **Phar::compress()****

```
<?php
$p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar');
$p['meuarquivo.txt'] = 'olá';
$p['meuarquivo2.txt'] = 'olá';
$p1 = $p->compress(Phar::GZ); // copia para /caminho/para/meu.phar.gz
$p2 = $p->compress(Phar::BZ2); // copia para /caminho/para/meu.phar.bz2
$p3 = $p2->compress(Phar::NONE); // exceção: /caminho/para/meu.phar já existe
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
- [Phar::decompress()](phar.decompress.md) - Descompacta todo o arquivo Phar
- [Phar::getSupportedCompression()](phar.getsupportedcompression.md) - Retorna um array de algoritmos de compactação suportados
- [Phar::compressFiles()](phar.compressfiles.md) - Compacta todos os arquivos no arquivo Phar atual
- [Phar::decompressFiles()](phar.decompressfiles.md) - Descompacta todos os arquivos no arquivo Phar atual

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
