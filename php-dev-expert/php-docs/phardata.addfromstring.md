# Adiciona um arquivo de uma string ao arquivo tar/zip

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.addfromstring.php

---

# PharData::addFromString

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::addFromString — Adiciona um arquivo de uma string ao arquivo tar/zip

### Descrição

public function **PharData::addFromString**([string](language.types.string.md) `$localName`, [string](language.types.string.md) `$contents`): [void](language.types.void.md)

Com este método, qualquer string pode ser adicionada ao arquivo tar/zip.
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

**Exemplo #1 Um exemplo de **PharData::addFromString()****

```
<?php
try {
    $a = new PharData('/caminho/para/meu.tar');

    $a->addFromString('caminho/para/arquivo.txt', 'meu arquivo simples');
    $b = $a['caminho/para/arquivo.txt']->getContent();

    // para adicionar conteúdo de um identificador de fluxo para arquivos grandes, use offsetSet()()
    $c = fopen('/caminho/para/arquivogigante.bin');
    $a['arquivogigante.bin'] = $c;
    fclose($c);
} catch (Exception $e) {
    // manipula erros aqui
}
?>
```

### Notas

> **Nota**:
>
> [PharData::addFile()](phardata.addfile.md), **PharData::addFromString()** e [PharData::offsetSet()](phardata.offsetset.md)
> salvam um novo arquivo phar cada vez que são chamadas. Se o desempenho for uma preocupação,
> [PharData::buildFromDirectory()](phardata.buildfromdirectory.md) ou [PharData::buildFromIterator()](phardata.buildfromiterator.md)
> devem ser usadas.

### Veja também

- [PharData::offsetSet()](phardata.offsetset.md) - Define o conteúdo de um arquivo dentro do tar/zip para o de um arquivo externo ou string
- [Phar::addFromString()](phar.addfromstring.md) - Adiciona um arquivo a partir de uma string ao arquivo phar
- [PharData::addFile()](phardata.addfile.md) - Adiciona um arquivo do sistema de arquivos ao arquivo tar/zip
- [PharData::addEmptyDir()](phardata.addemptydir.md) - Adiciona um diretório vazio ao arquivo tar/zip

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
