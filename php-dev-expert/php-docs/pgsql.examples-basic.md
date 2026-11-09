# Uso básico

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pgsql.examples-basic.php

---

## Uso básico

Este exemplo simples mostra como conectar, executar uma consulta, mostrar
linhas de resultados e desconectar de um banco de dados PostgreSQL.

**Exemplo #1 Exemplo geral da extensão PostgreSQL**

```
<?php

// Connectando, selectionando o banco
$dbconn = pg_connect("host=localhost dbname=publishing user=www password=foo")
    or die('Não foi possível conectar: ' . pg_last_error());

// Executando consulta SQL
$query = 'SELECT * FROM authors';
$result = pg_query($dbconn, $query) or die('A consulta falhou: ' . pg_last_error());

// Exibindo resultados em HTML
echo "<table>\n";
while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
    echo "\t<tr>\n";
    foreach ($line as $col_value) {
        echo "\t\t<td>$col_value</td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table>\n";

// Liberando o conjunto de resultados
pg_free_result($result);

// Fechando a conexão
pg_close($dbconn);

?>
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
