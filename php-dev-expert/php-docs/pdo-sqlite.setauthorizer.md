# Configures a callback to be used as an authorizer to limit what a statement can do

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-sqlite.setauthorizer.php

---

# Pdo\Sqlite::setAuthorizer

(PHP 8 >= 8.5.0)

Pdo\Sqlite::setAuthorizer — Configures a callback to be used as an authorizer to limit what a statement can do

### Descrição

public function **Pdo\Sqlite::setAuthorizer**([?](language.types.null.md)[callable](language.types.callable.md) `$callback`): [void](language.types.void.md)

Sets a callback that will be called by SQLite every time an action is performed
(reading, deleting, updating, etc.). This is used when preparing an SQL statement
from an untrusted source to ensure that the statement does not access data it is
not allowed to see or execute malicious statements that damage the database.

The authorizer is used only during the statement preparation phase.
It may be called several times for a single statement: a
`SELECT` or `UPDATE` query calls it for every
column that would be read or updated. It runs again whenever SQLite
re-prepares a statement, which may happen while the statement is being
executed, for instance after the schema has changed.

The authorizer is called with up to five arguments. The arguments received are
described at [SQLite3::setAuthorizer()](sqlite3.setauthorizer.md).

Only a single authorizer can be in place on a database connection at a time.
Each call to this method overrides the previous one. The authorizer is disabled
by default, and can be disabled again by setting a **`null`** callback.

The callback must not modify the database connection that invoked it.

More details can be found in the
[» SQLite documentation](https://sqlite.org/c3ref/set_authorizer.html).

> **Nota**:
>
> This method is the equivalent of [SQLite3::setAuthorizer()](sqlite3.setauthorizer.md),
> except that it returns [void](language.types.void.md) instead of [bool](language.types.boolean.md).

### Parâmetros

`callback`
:   The [callable](language.types.callable.md) to be invoked, or **`null`** to disable the current
    authorizer callback.

    It must return one of **`Pdo\Sqlite::OK`**,
    **`Pdo\Sqlite::DENY`**, or
    **`Pdo\Sqlite::IGNORE`**.
    When **`Pdo\Sqlite::DENY`** is returned, the statement that
    triggered the authorizer fails with an error stating that access is denied.
    When **`Pdo\Sqlite::IGNORE`** is returned for a read action,
    the statement is prepared so that a **`null`** value is substituted for the
    column that would have been read.

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

This method itself does not throw, but if the authorizer callback does not return
an [int](language.types.integer.md), or returns an [int](language.types.integer.md) which is not one of
**`Pdo\Sqlite::OK`**, **`Pdo\Sqlite::DENY`**, or
**`Pdo\Sqlite::IGNORE`**, the statement preparation throws a
[TypeError](class.typeerror.md) or a [ValueError](class.valueerror.md)
respectively.

### Examples

**Exemplo #1 **Pdo\Sqlite::setAuthorizer()** example**

Only read actions are allowed on the connection. The action codes are exposed
as [SQLite3](class.sqlite3.md) class constants, which requires the
[SQLite3](book.sqlite3.md) extension to be available; their
integer values may be used directly otherwise.

```
<?php
$db = new Pdo\Sqlite('sqlite::memory:');
$db->exec('CREATE TABLE users (id, name)');

$db->setAuthorizer(function (int $action, ...$args) {
    return match ($action) {
        SQLite3::SELECT, SQLite3::READ => Pdo\Sqlite::OK,
        default => Pdo\Sqlite::DENY,
    };
});

var_dump($db->query('SELECT name FROM users') instanceof PDOStatement);

try {
    $db->exec('DROP TABLE users');
} catch (PDOException $e) {
    echo $e->getMessage(), "\n";
}
?>
```

O exemplo acima produzirá
algo semelhante a:

```
bool(true)
SQLSTATE[HY000]: General error: 23 not authorized
```

### Veja também

- [SQLite3::setAuthorizer()](sqlite3.setauthorizer.md) - Configura um retorno de chamada a ser usado como um autorizador para limitar o que uma declaração pode fazer

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
