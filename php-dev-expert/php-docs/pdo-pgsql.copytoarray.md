# Copia dados da tabela do banco de dados para o array PHP

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.copytoarray.php

---

# Pdo\Pgsql::copyToArray

(PHP 8 >= 8.4.0)

Pdo\Pgsql::copyToArray — Copia dados da tabela do banco de dados para o array PHP

### Descrição

public function **Pdo\Pgsql::copyToArray**(  
    [string](language.types.string.md) `$tableName`,  
    [string](language.types.string.md) `$separator` = "\t",  
    [string](language.types.string.md) `$nullAs` = "\\\\N",  
    [?](language.types.null.md)[string](language.types.string.md) `$fields` = **`null`**  
): [array](language.types.array.md)|[false](language.types.singleton.md)

Copia dados de `tableName` para um array usando `separator` como delimitador de campos e lista de campos no parâmetro `fields`.

### Parâmetros

`tableName`
:   String contendo o nome da tabela.

`separator`
:   Delimitador usado para separar campos em uma entrada do
    array `rows`.

`nullAs`
:   Como interpretar valores SQL `NULL`.

`fields`
:   Lista de campos a serem exportados.

### Valor Retornado

Retorna um array de linhas, ou **`false`** em caso de falha.

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::copyToArray()****

Cada elemento retornado é um registro com os campos conectados por
`separator` e uma nova linha no final.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('CREATE TABLE fruits (id int, name text, qty int)');
$db->exec("INSERT INTO fruits VALUES (1, 'apple', 10), (2, 'banana', 20)");

$rows = $db->copyToArray('fruits');
var_export($rows);
?>
```

O exemplo acima produzirá:

```
array (
  0 => '1	apple	10
',
  1 => '2	banana	20
',
)
```

### Veja também

- [Pdo\Pgsql::copyFromArray()](pdo-pgsql.copyfromarray.md) - Copia dados de um array PHP para uma tabela
- [Pdo\Pgsql::copyFromFile()](pdo-pgsql.copyfromfile.md) - Copia dados do arquivo para a tabela
- [Pdo\Pgsql::copyToFile()](pdo-pgsql.copytofile.md) - Copia dados da tabela para arquivo

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
