# Adiciona um diretório vazio ao arquivo tar/zip

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.addemptydir.php

---

# PharData::addEmptyDir

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::addEmptyDir — Adiciona um diretório vazio ao arquivo tar/zip

### Descrição

public function **PharData::addEmptyDir**([string](language.types.string.md) `$directory`): [void](language.types.void.md)

Com este método, um diretório vazio é criado com o caminho `dirname`.
Este método é semelhante a [ZipArchive::addEmptyDir()](ziparchive.addemptydir.md).

### Parâmetros

`directory`
:   O nome do diretório vazio a ser criado no arquivo phar

### Valor Retornado

Nenhum valor de retorno, exceção é lançada em caso de falha.

### Examples

**Exemplo #1 Um exemplo de **PharData::addEmptyDir()****

```
<?php
try {
    $a = new PharData('/caminho/para/meu.tar');

    $a->addEmptyDir('/caminho/completo/para/diretorio');
    // demonstra como este diretório é armazenado
    $b = $a['/caminho/completo/para/diretorio']->isDir();
} catch (Exception $e) {
    // manipula erros aqui
}
?>
```

### Veja também

- [Phar::addEmptyDir()](phar.addemptydir.md) - Adiciona um diretório vazio ao arquivo phar
- [PharData::addFile()](phardata.addfile.md) - Adiciona um arquivo do sistema de arquivos ao arquivo tar/zip
- [PharData::addFromString()](phardata.addfromstring.md) - Adiciona um arquivo de uma string ao arquivo tar/zip

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
