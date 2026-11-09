# Adiciona um arquivo a partir de uma string ao arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.addfromstring.php

---

# Phar::addFromString

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::addFromString — Adiciona um arquivo a partir de uma string ao arquivo phar

### Descrição

public function **Phar::addFromString**([string](language.types.string.md) `$localName`, [string](language.types.string.md) `$contents`): [void](language.types.void.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Com este método, qualquer string pode ser adicionada ao arquivo phar.
O arquivo será armazenado no arquivo com `localname` como seu
caminho. Este método é semelhante a [ZipArchive::addFromString()](ziparchive.addfromstring.md).

### Parâmetros

`localName`
:   Caminho onde o arquivo será armazenado no arquivo compactado.

`contents`
:   O conteúdo do arquivo a ser armazenado

### Valor Retornado

Nenhum valor de retorno, exceção é lançada em caso de falha.

### Examples

**Exemplo #1 Um exemplo de **Phar::addFromString()****

```
<?php
try {
    $a = new Phar('/path/to/phar.phar');

    $a->addFromString('path/to/file.txt', 'my simple file');
    $b = $a['path/to/file.txt']->getContent();

    // para adicionar conteúdo de um identificador de fluxo para arquivos grandes, use offsetSet()
    $c = fopen('/path/to/hugefile.bin');
    $a['largefile.bin'] = $c;
    fclose($c);
} catch (Exception $e) {
    // manipula erros aqui
}
?>
```

### Notas

> **Nota**:
>
> [Phar::addFile()](phar.addfile.md), **Phar::addFromString()** e [Phar::offsetSet()](phar.offsetset.md)
> salvam um novo arquivo phar cada vez que são chamadas. Se o desempenho for uma preocupação,
> [Phar::buildFromDirectory()](phar.buildfromdirectory.md) ou [Phar::buildFromIterator()](phar.buildfromiterator.md)
> devem ser usadas.

### Veja também

- [Phar::offsetSet()](phar.offsetset.md) - Define o conteúdo de um arquivo interno para o de um arquivo externo
- [PharData::addFromString()](phardata.addfromstring.md) - Adiciona um arquivo de uma string ao arquivo tar/zip
- [Phar::addFile()](phar.addfile.md) - Adiciona um arquivo do sistema de arquivos ao arquivo phar
- [Phar::addEmptyDir()](phar.addemptydir.md) - Adiciona um diretório vazio ao arquivo phar

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
