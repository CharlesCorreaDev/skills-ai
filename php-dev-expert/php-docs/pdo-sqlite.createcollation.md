# Registra uma função definida pelo usuário para uso como função de agrupamento em instruções SQL

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-sqlite.createcollation.php

---

# Pdo\Sqlite::createCollation

(PHP 8 >= 8.4.0)

Pdo\Sqlite::createCollation — 
Registra uma função definida pelo usuário para uso como função de agrupamento em instruções SQL

### Descrição

public function **Pdo\Sqlite::createCollation**([string](language.types.string.md) `$name`, [callable](language.types.callable.md) `$callback`): [bool](language.types.boolean.md)

Este método é semelhante a [Pdo\Sqlite::createFunction()](pdo-sqlite.createfunction.md)
exceto que ele registra funções que são usadas para agrupar strings.

### Parâmetros

`name`
:   Nome da função de agrupamento SQL a ser criada ou redefinida.

`callback`
:   Função de retorno de chamada que define o comportamento de um agrupamento.
    Ele deve aceitar duas [string](language.types.string.md)s e retornar
    `-1`, `0` ou `1`
    se a primeira string for classificada antes, ordenada de forma idêntica ou ordenada depois
    da segunda string, respectivamente.
    Uma função interna que se comporta assim é [strcmp()](function.strcmp.md).

    Esta função precisa ser definida como:

    function collation([string](language.types.string.md) `$string1`, [string](language.types.string.md) `$string2`): [int](language.types.integer.md)

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Examples

**Exemplo #1 Exemplo de **Pdo\Sqlite::createCollation()****

```
<?php
$db = new Pdo\Sqlite('sqlite::memory:');
$db->exec("CREATE TABLE test (col1 string)");
$db->exec("INSERT INTO test VALUES ('a1')");
$db->exec("INSERT INTO test VALUES ('a10')");
$db->exec("INSERT INTO test VALUES ('a2')");

$db->sqliteCreateCollation('NATURAL_CMP', 'strnatcmp');
foreach ($db->query("SELECT col1 FROM test ORDER BY col1") as $row) {
    echo $row['col1'] . "\n";
}
echo "\n";
foreach ($db->query("SELECT col1 FROM test ORDER BY col1 COLLATE NATURAL_CMP") as $row) {
    echo $row['col1'] . "\n";
}
?>
```

O exemplo acima produzirá:

```
a1
a10
a2

a1
a2
a10
```

### Veja também

- [Pdo\Sqlite::createFunction()](pdo-sqlite.createfunction.md) - Registra uma função definida pelo usuário para uso em instruções SQL
- [Pdo\Sqlite::createAggregate()](pdo-sqlite.createaggregate.md) - Registra uma função de agregação definida pelo usuário para uso em instruções SQL
- **sqlite\_create\_function()**
- **sqlite\_create\_aggregate()**

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
