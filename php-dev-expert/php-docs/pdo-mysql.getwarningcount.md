# Retorna o número de alertas da última consulta executada

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-mysql.getwarningcount.php

---

# Pdo\Mysql::getWarningCount

(PHP 8 >= 8.4.0)

Pdo\Mysql::getWarningCount — Retorna o número de alertas da última consulta executada

### Descrição

public function **Pdo\Mysql::getWarningCount**(): [int](language.types.integer.md)

Retorna o número de alertas da última consulta executada.

> **Nota**:
>
> Para recuperar mensagens de alerta, o seguinte comando SQL pode ser usado:
> `SHOW WARNINGS [limit row_count]`, onde "row\_count" é o número máximo de mensagens a serem retornadas.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna um [int](language.types.integer.md) representando o número de avisos gerados pela última consulta.

### Examples

**Exemplo #1 Exemplo de **Pdo\Mysql::getWarningCount()****

```
<?php

$conn = PDO::connect("mysql:host=localhost;dbname=test;charset=utf8mb4", 'user', 'password');

$conn->query('SELECT 42/0');
if ($conn->getWarningCount() > 0) {
    $result = $conn->query("SHOW WARNINGS");
    $row = $result->fetch();
    printf("%s (%d): %s\n", $row[0], $row[1], $row[2]);
}

?>
```

O exemplo acima produzirá:

```
Warning (1365): Division by 0
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
