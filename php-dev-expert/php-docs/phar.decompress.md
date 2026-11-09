# Descompacta todo o arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.decompress.php

---

# Phar::decompress

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::decompress — Descompacta todo o arquivo Phar

### Descrição

public function **Phar::decompress**([?](language.types.null.md)[string](language.types.string.md) `$extension` = **`null`**): [?](language.types.null.md)[Phar](class.phar.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Para arquivos phar baseados em tar e phar, esse método descompacta o arquivo inteiro.

Para arquivos phar baseados em Zip, este método falha com uma exceção.
A extensão [zlib](ref.zlib.md) deve ser habilitada para descompactar
um arquivo compactado com compactação gzip, e a
extensão [bzip2](ref.bzip2.md) deve ser
habilitada para descompactar um arquivo compactado com compactação bzip2.
Como acontece com todas as funcionalidades que modificam o conteúdo de um phar, a
variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly) deve estar desativada
para ter sucesso.

Além disso, este método altera automaticamente a extensão do arquivo,
`.phar`
por padrão para arquivos phar, ou `.phar.tar` para arquivos phar baseados em tar.
Alternativamente, uma extensão de arquivo pode ser especificada com o segundo
parâmetro.

### Parâmetros

`extension`
:   Para descompactação, as extensões de arquivo padrão
    são `.phar` e `.phar.tar`.
    Use este parâmetro para especificar outra extensão de arquivo. Esteja ciente
    de que todos os arquivos executáveis ​​phar devem conter `.phar`
    em seus nomes.

### Valor Retornado

Um objeto [Phar](class.phar.md) é retornado em caso de sucesso e **`null`** em caso de falha.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se
a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
estiver ativada, se a extensão [zlib](ref.zlib.md)
não estiver disponível ou se a extensão [bzip2](ref.bzip2.md)
não estiver habilitada.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `extension` agora é anulável. |

### Examples

**Exemplo #1 Um exemplo de **Phar::decompress()****

```
<?php
$p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar.gz');
$p['meuarquivo.txt'] = 'olá';
$p['meuarquivo2.txt'] = 'olá';
$p3 = $p2->decompress(); // cria /caminho/para/meu.phar
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
- [Phar::compress()](phar.compress.md) - Compacta todo o arquivo Phar usando compactação Gzip ou Bzip2
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
