# Retorna um array com os drivers PDO disponíveis

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.getavailabledrivers.php

---

# PDO::getAvailableDrivers

# pdo\_drivers

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 1.0.3)

PDO::getAvailableDrivers -- pdo\_drivers — 
Retorna um array com os drivers PDO disponíveis

### Descrição

public static function **PDO::getAvailableDrivers**(): [array](language.types.array.md)

function **pdo\_drivers**(): [array](language.types.array.md)

Esta função retorna todos os drivers PDO disponíveis que podem ser usados
no parâmetro `DSN` de
[PDO::\_\_construct()](pdo.construct.md).

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

**PDO::getAvailableDrivers()** retorna um array com os drivers PDO disponíveis. Se
nenhum driver estiver disponível então o retorno será um array vazio.

### Examples

**Exemplo #1 Exemplo de **PDO::getAvailableDrivers()****

```
<?php
print_r(PDO::getAvailableDrivers());
?>
```

O exemplo acima produzirá
algo semelhante a:

```
Array
(
    [0] => mysql
    [1] => sqlite
)
```

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
