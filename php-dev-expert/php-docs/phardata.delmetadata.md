# Exclui os metadados globais de um arquivo zip

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.delmetadata.php

---

# PharData::delMetadata

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::delMetadata — Exclui os metadados globais de um arquivo zip

### Descrição

public function **PharData::delMetadata**(): [true](language.types.singleton.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Exclui os metadados globais de um arquivo zip.

### Parâmetros

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança [PharException](class.pharexception.md) se ocorrerem erros durante a descarga
de alterações no disco.

### Examples

**Exemplo #1 Um exemplo de **PharData::delMetaData()****

```
<?php
try {
    $phar = new PharData('meuphar.zip');
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
