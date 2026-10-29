# Escapa uma string para uso como identificador SQL

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.escapeidentifier.php

---

# Pdo\Pgsql::escapeIdentifier

(PHP 8 >= 8.4.0)

Pdo\Pgsql::escapeIdentifier — Escapa uma string para uso como identificador SQL

### Descrição

public function **Pdo\Pgsql::escapeIdentifier**([string](language.types.string.md) `$input`): [string](language.types.string.md)

Escapa uma string para uso como um identificador SQL, como uma tabela, coluna ou nome de função.
Isso é útil quando um identificador fornecido pelo usuário pode conter caracteres especiais
que de outra forma não seriam interpretados como parte do identificador pelo analisador SQL
ou quando o identificador pode conter caracteres em maiúsculas que precisam ser preservadas.

### Parâmetros

`input`
:   Uma [string](language.types.string.md) contendo texto a ser escapado.

### Valor Retornado

Uma [string](language.types.string.md) contendo os dados escapados.

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::escapeIdentifier()****

```
<?php
$pdo = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);

$unescapedTableName = 'UnescapedTableName';
$pdo->exec("CREATE TABLE $unescapedTableName ()");

$escapedTableName = $pdo->escapeIdentifier('EscapedTableName');
$pdo->exec("CREATE TABLE $escapedTableName ()");

$statement = $pdo->query(
    "SELECT relname FROM pg_stat_user_tables WHERE relname ilike '%tablename'"
);

var_export($statement->fetchAll(PDO::FETCH_COLUMN, 0));

$tableNameWithSymbols = 'Table-Name-With-Symbols';
$pdo->exec("CREATE TABLE $tableNameWithSymbols ()");
?>
```

O exemplo acima produzirá
algo semelhante a:

```
array (
  0 => 'unescapedtablename',
  1 => 'EscapedTableName',
)
Fatal error: Uncaught PDOException: SQLSTATE[42601]: Syntax error: 7 ERROR:  syntax error at or near "Table"
LINE 1: CREATE TABLE Table-Name-With-Symbols ()
```

### Veja também

- [PDO::quote()](pdo.quote.md) - Inclui aspas em uma string para uso em uma consulta

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
