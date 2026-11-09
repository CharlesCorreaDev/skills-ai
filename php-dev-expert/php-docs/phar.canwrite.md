# Retorna se a extensão phar suporta a escrita e criação de phars

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.canwrite.php

---

# Phar::canWrite

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::canWrite — Retorna se a extensão phar suporta a escrita e criação de phars

### Descrição

final public static function **Phar::canWrite**(): [bool](language.types.boolean.md)

Este método estático determina se o acesso de gravação foi desabilitado no
sistema php.ini por meio da variável ini
[phar.readonly](phar.configuration.md#ini.phar.readonly).

### Parâmetros

### Valor Retornado

**`true`** se o acesso de gravação estiver habilitado, **`false`** se estiver desabilitado.

### Examples

**Exemplo #1 Um exemplo de **Phar::canWrite()****

```
<?php
if (Phar::canWrite()) {
    file_put_contents('phar://meuphar.phar/arquivo.txt', 'olá mundo');
}
?>
```

### Veja também

- [phar.readonly](phar.configuration.md#ini.phar.readonly)
- [Phar::isWritable()](phar.iswritable.md) - Informa se o arquivo phar pode ser modificado

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
