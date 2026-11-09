# Busca o SQLSTATE associado com a última operação no objeto da instrução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.errorcode.php

---

# PDOStatement::errorCode

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDOStatement::errorCode — 
Busca o SQLSTATE associado com a última operação no objeto da instrução

### Descrição

public function **PDOStatement::errorCode**(): [?](language.types.null.md)[string](language.types.string.md)

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Idêntico a [PDO::errorCode()](pdo.errorcode.md), exceto que
**PDOStatement::errorCode()** somente recupera códigos de erro
para operações realizadas com objetos PDOStatement.

### Examples

**Exemplo #1 Recuperando o código SQLSTATE**

```
<?php
/* Provoca um erro -- a tabela OSSOS não existe */
$err = $dbh->prepare('SELECT cranio FROM ossos');
$err->execute();

echo "\nPDOStatement::errorCode(): ";
print $err->errorCode();
?>
```

O exemplo acima produzirá:

```
PDOStatement::errorCode(): 42S02
```

### Veja também

- [PDO::errorCode()](pdo.errorcode.md) - Busca o SQLSTATE associado com a última operação no identificador do banco de dados
- [PDO::errorInfo()](pdo.errorinfo.md) - Busca informação de erro estendida associada com a última operação no identificador do banco de dados
- [PDOStatement::errorInfo()](pdostatement.errorinfo.md) - Busca informação de erro estendida associada com a última operação no identificador da instrução

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
