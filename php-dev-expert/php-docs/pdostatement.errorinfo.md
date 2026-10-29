# Busca informação de erro estendida associada com a última operação no identificador da instrução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.errorinfo.php

---

# PDOStatement::errorInfo

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDOStatement::errorInfo — 
Busca informação de erro estendida associada com a última operação no identificador da instrução

### Descrição

public function **PDOStatement::errorInfo**(): [array](language.types.array.md)

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

**PDOStatement::errorInfo()** retorna um array de
informações de erro sobre a última operação realizada por este
objeto de instrução. O array consiste de pelo menos os campos a seguir:

| Elemento | Informação |
| --- | --- |
| 0 | Código de erro SQLSTATE (um identificador alfanumérico de cinco caracteres definido no padrão ANSI SQL). |
| 1 | Código de erro específico do driver. |
| 2 | Mensagem de erro específica do driver. |

### Examples

**Exemplo #1 Mostrando campos de errorInfo() para uma conexão PDO\_ODBC a um banco de dados DB2**

```
<?php
/* Provoca um erro -- a tabela OSSOS não existe */
$sth = $dbh->prepare('SELECT cranio FROM ossos');
$sth->execute();

echo "\nPDOStatement::errorInfo():\n";
$arr = $sth->errorInfo();
print_r($arr);
?>
```

O exemplo acima produzirá:

```
PDOStatement::errorInfo():
Array
(
    [0] => 42S02
    [1] => -204
    [2] => [IBM][CLI Driver][DB2/LINUX] SQL0204N  "LUCY.OSSOS" is an undefined name.  SQLSTATE=42704
)
```

### Veja também

- [PDO::errorCode()](pdo.errorcode.md) - Busca o SQLSTATE associado com a última operação no identificador do banco de dados
- [PDO::errorInfo()](pdo.errorinfo.md) - Busca informação de erro estendida associada com a última operação no identificador do banco de dados
- [PDOStatement::errorCode()](pdostatement.errorcode.md) - Busca o SQLSTATE associado com a última operação no objeto da instrução

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
