# Retorna o número de registros afetados pela última instrução SQL

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.rowcount.php

---

# PDOStatement::rowCount

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDOStatement::rowCount — 
Retorna o número de registros afetados pela última instrução SQL

### Descrição

public function **PDOStatement::rowCount**(): [int](language.types.integer.md)

**PDOStatement::rowCount()** retorna o número de
registros afetados pela última instrução DELETE, INSERT ou UPDATE
executada pelo objeto `PDOStatement` correspondente.

Para instruções que produzem conjuntos de resultados, como `SELECT`,
o comportamento é indefinido e pode ser diferente para cada driver.
Alguns bancos de dados podem retornar o número de registros produzidos por essa instrução
(por exemplo, MySQL em modo buffer), mas este
comportamento não é garantido para todos os bancos de dados e não deve ser uma fonte confiável
para aplicações portáveis.

> **Nota**:
>
> Este método retorna "0" (zero) com o driver PostgreSQL ao definir
> o atributo de instrução **`PDO::ATTR_CURSOR`** para
> **`PDO::CURSOR_SCROLL`**.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o número de registros.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Retorna o número de registros apagados**

**PDOStatement::rowCount()** retorna o número de
registros afetados pelas instruções DELETE, INSERT ou UPDATE.

```
<?php
/* Apaga todos os registros da tabela FRUIT */
$del = $dbh->prepare('DELETE FROM fruit');
$del->execute();

/* Retorna o número de registros apagados */
print "Número retornado de registros apagados:\n";
$count = $del->rowCount();
print "$count registros apagados.\n";
?>
```

O exemplo acima produzirá
algo semelhante a:

```
Número retornado de registros apagados:
9 registros apagados.
```

**Exemplo #2 Contando registros retornados por uma instrução SELECT**

Para a maioria dos bancos de dados, o método **PDOStatement::rowCount()** não
retorna o número de registros afetados por uma instrução SELECT. Ao invés dele, o método
[PDO::query()](pdo.query.md) deve ser usado para emitir uma instrução SELECT COUNT(\*)
com os mesmos predicados da instrução SELECT requerida, e então
[PDOStatement::fetchColumn()](pdostatement.fetchcolumn.md) deve ser usado para recuperar o número
de registros correspondentes.

```
<?php
$sql = "SELECT COUNT(*) FROM fruit WHERE calories > 100";
$res = $conn->query($sql);
$count = $res->fetchColumn();

print "Há " .  $count . " registros correspondentes.";
```

O exemplo acima produzirá
algo semelhante a:

```
Há 2 registros correspondentes.
```

### Veja também

- [PDOStatement::columnCount()](pdostatement.columncount.md) - Retorna o número de colunas no conjunto de resultados
- [PDOStatement::fetchColumn()](pdostatement.fetchcolumn.md) - Retorna uma única coluna do próximo registro de um resultado
- [PDO::query()](pdo.query.md) - Prepara e executa uma instrução SQL sem marcadores

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
