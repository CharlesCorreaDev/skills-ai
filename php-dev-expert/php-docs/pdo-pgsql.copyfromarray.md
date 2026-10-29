# Copia dados de um array PHP para uma tabela

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.copyfromarray.php

---

# Pdo\Pgsql::copyFromArray

(PHP 8 >= 8.4.0)

Pdo\Pgsql::copyFromArray — Copia dados de um array PHP para uma tabela

### Descrição

public function **Pdo\Pgsql::copyFromArray**(  
    [string](language.types.string.md) `$tableName`,  
    [array](language.types.array.md)|[Traversable](class.traversable.md) `$rows`,  
    [string](language.types.string.md) `$separator` = "\t",  
    [string](language.types.string.md) `$nullAs` = "\\\\N",  
    [?](language.types.null.md)[string](language.types.string.md) `$fields` = **`null`**  
): [bool](language.types.boolean.md)

Copia dados do array `rows` para a tabela
`tableName` usando `separator`
como delimitador de campos e uma lista de campos no parâmetro `fields`.

### Parâmetros

`tableName`
:   String contendo o nome da tabela.

`rows`
:   Um [array](language.types.array.md) indexado (ou [Traversable](class.traversable.md)) de
    [string](language.types.string.md)s com campos separados por
    `separator`.

`separator`
:   Delimitador usado para separar campos em uma entrada do
    array `rows`.

`nullAs`
:   Como interpretar valores SQL `NULL`.

`fields`
:   Lista de campos a serem inseridos.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.5.0 | `rows` agora aceira um [Traversable](class.traversable.md); anteriormente somente um [array](language.types.array.md) era aceito. |

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::copyFromArray()****

Cada elemento de `rows` é um registro cujos campos são
conectados por `separator` (uma tabulação por padrão).

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('CREATE TABLE fruits (id int, name text, qty int)');

$rows = [
    "1\tapple\t10",
    "2\tbanana\t20",
    "3\tcherry\t30",
];
$db->copyFromArray('fruits', $rows);

foreach ($db->query('SELECT * FROM fruits ORDER BY id') as $row) {
    echo "{$row['id']} {$row['name']} {$row['qty']}\n";
}
?>
```

O exemplo acima produzirá:

```
1 apple 10
2 banana 20
3 cherry 30
```

### Veja também

- [Pdo\Pgsql::copyToArray()](pdo-pgsql.copytoarray.md) - Copia dados da tabela do banco de dados para o array PHP
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
