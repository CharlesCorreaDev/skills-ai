# Adiciona um diretório vazio ao arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.addemptydir.php

---

# Phar::addEmptyDir

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::addEmptyDir — Adiciona um diretório vazio ao arquivo phar

### Descrição

public function **Phar::addEmptyDir**([string](language.types.string.md) `$directory`): [void](language.types.void.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Com este método, um diretório vazio é criado com o caminho `dirname`.
Este método é semelhante a [ZipArchive::addEmptyDir()](ziparchive.addemptydir.md).

### Parâmetros

`directory`
:   O nome do diretório vazio a ser criado no arquivo phar

### Valor Retornado

Nenhum valor de retorno, exceção é lançada em caso de falha.

### Examples

**Exemplo #1 Um exemplo de **Phar::addEmptyDir()****

```
<?php
try {
    $a = new Phar('/caminho/para/phar.phar');

    $a->addEmptyDir('/caminho/completo/para/arquivo');
    // demonstra como este arquivo é armazenado
    $b = $a['full/path/to/file']->isDir();
} catch (Exception $e) {
    // manipula os erros aqui
}
?>
```

### Veja também

- [PharData::addEmptyDir()](phardata.addemptydir.md) - Adiciona um diretório vazio ao arquivo tar/zip
- [Phar::addFile()](phar.addfile.md) - Adiciona um arquivo do sistema de arquivos ao arquivo phar
- [Phar::addFromString()](phar.addfromstring.md) - Adiciona um arquivo a partir de uma string ao arquivo phar

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
