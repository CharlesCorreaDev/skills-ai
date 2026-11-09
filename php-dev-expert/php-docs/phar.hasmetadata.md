# Informa se o phar tem metadados globais

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.hasmetadata.php

---

# Phar::hasMetadata

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.2.0)

Phar::hasMetadata — Informa se o phar tem metadados globais

### Descrição

public function **Phar::hasMetadata**(): [bool](language.types.boolean.md)

Informa se o phar tem metadados globais definidos.

### Parâmetros

Sem parâmetros.

### Valor Retornado

Retorna **`true`** se os metadados foram definidos e **`false`** caso contrário.

### Examples

**Exemplo #1 Um exemplo de **Phar::hasMetadata()****

```
<?php
try {
    $phar = new Phar('meuphar.phar');
    var_dump($phar->hasMetadata());
    $phar->setMetadata(array('teste' => 'olá'));
    var_dump($phar->hasMetadata());
    $phar->delMetadata();
    var_dump($phar->hasMetadata());
} catch (Exception $e) {
    // lida com erros
}
?>
```

O exemplo acima produzirá:

```
bool(false)
bool(true)
bool(false)
```

### Veja também

- [Phar::getMetadata()](phar.getmetadata.md) - Retorna metadados do arquivo phar
- [Phar::setMetadata()](phar.setmetadata.md) - Define metadados do arquivo phar
- [Phar::delMetadata()](phar.delmetadata.md) - Exclui os metadados globais do phar

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
