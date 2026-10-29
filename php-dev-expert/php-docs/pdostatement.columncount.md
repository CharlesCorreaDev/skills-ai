# Retorna o número de colunas no conjunto de resultados

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.columncount.php

---

# PDOStatement::columnCount

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.2.0)

PDOStatement::columnCount — 
Retorna o número de colunas no conjunto de resultados

### Descrição

public function **PDOStatement::columnCount**(): [int](language.types.integer.md)

Use **PDOStatement::columnCount()** para retornar o número
de colunas no conjunto de resultados representado pelo objeto PDOStatement.

Se o objeto PDOStatement foi retornado por [PDO::query()](pdo.query.md),
a contagem de colunas estará disponível imediatamente.

Se o objeto PDOStatement foi retornado por
[PDO::prepare()](pdo.prepare.md), uma contagem precisa de colunas não estará
disponível até que o método [PDOStatement::execute()](pdostatement.execute.md) seja chamado.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o número de colunas no conjunto de resultados representado pelo
objeto PDOStatement, mesmo se o conjunto de resultados estiver vazio. Se não houver conjunto de resultados,
**PDOStatement::columnCount()** retornará `0`.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Contando colunas**

Este exemplo demonstra como **PDOStatement::columnCount()**
opera com e sem um conjunto de resultados.

```
<?php
$dbh = new PDO('odbc:sample', 'db2inst1', 'ibmdb2');

$sth = $dbh->prepare("SELECT name, colour FROM fruit");

/* Conta o número de colunas no conjunto de resultados (não existente) */
$colcount = $sth->columnCount();
print "Antes de execute(), o resultado tem $colcount colunas (deve ser 0)\n";

$sth->execute();

/* Conta o número de colunas no conjunto de resultados */
$colcount = $sth->columnCount();
print "Depois de execute(), o resultado tem $colcount colunas (devem ser 2)\n";

?>
```

O exemplo acima produzirá:

```
Antes de execute(), o resultado tem 0 colunas (deve ser 0)
Depois de execute(), o resultado tem 2 colunas (devem ser 2)
```

### Veja também

- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
- [PDOStatement::execute()](pdostatement.execute.md) - Executa ums instrução preparada
- [PDOStatement::rowCount()](pdostatement.rowcount.md) - Retorna o número de registros afetados pela última instrução SQL

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
