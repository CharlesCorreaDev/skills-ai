# Exclui os metadados globais do phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.delmetadata.php

---

# Phar::delMetadata

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.2.0)

Phar::delMetadata — Exclui os metadados globais do phar

### Descrição

public function **Phar::delMetadata**(): [true](language.types.singleton.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Exclui os metadados globais do phar.

### Parâmetros

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança [PharException](class.pharexception.md) se ocorrerem erros durante a descarga
de alterações no disco.

### Examples

**Exemplo #1 Um exemplo de **Phar::delMetaData()****

```
<?php
try {
    $phar = new Phar('meuphar.phar');
    var_dump($phar->getMetadata());
    $phar->setMetadata("olá mundo");
    var_dump($phar->getMetadata());
    $phar->delMetadata();
    var_dump($phar->getMetadata());
} catch (Exception $e) {
    // lida com erros
}
?>
```

O exemplo acima produzirá:

```
NULL
string(9) "olá mundo"
NULL
```

### Veja também

- [Phar::getMetadata()](phar.getmetadata.md) - Retorna metadados do arquivo phar
- [Phar::setMetadata()](phar.setmetadata.md) - Define metadados do arquivo phar
- [Phar::hasMetadata()](phar.hasmetadata.md) - Informa se o phar tem metadados globais

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
