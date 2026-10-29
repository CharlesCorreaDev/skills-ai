# Busca informação de erro estendida associada com a última operação no identificador do banco de dados

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.errorinfo.php

---

# PDO::errorInfo

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDO::errorInfo — 
Busca informação de erro estendida associada com a última operação no identificador do banco de dados

### Descrição

public function **PDO::errorInfo**(): [array](language.types.array.md)

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

**PDO::errorInfo()** retorna um array de informações de erro
sobre a última operação realizada por este identificador de banco de dados. O array
consiste em pelo menos os campos a seguir:

| Elemento | Informação |
| --- | --- |
| 0 | Código de erro SQLSTATE (um identificador alfanumérico de cinco caracteres definido no padrão ANSI SQL). |
| 1 | Código de erro específico do driver. |
| 2 | Mensagem de erro específica do driver. |

> **Nota**:
>
> Se o código de erro SQLSTATE não estiver definido ou se não houver erro específico
> do driver, os elementos após o elemento 0 serão definidos para **`null`**.

**PDO::errorInfo()** somente busca informação de erro para
operações realizadas diretamente no identificador do banco de dados. Se for criado um objeto
PDOStatement através de [PDO::prepare()](pdo.prepare.md) ou
[PDO::query()](pdo.query.md) e for invocado um erro no identificador da
instrução, **PDO::errorInfo()** não refletirá o erro
do identificador da instrução. Deve-se chamar
[PDOStatement::errorInfo()](pdostatement.errorinfo.md) para retornar a informação de
erro para uma operação realizada em um identificador de instrução em particular.

### Examples

**Exemplo #1 Mostrando campos de errorInfo() para uma conexão PDO\_ODBC a um banco de dados DB2**

```
<?php
/* Provoca um erro -- sintaxe SQL incorreta */
$stmt = $dbh->prepare('bogus sql');
if (!$stmt) {
    echo "\nPDO::errorInfo():\n";
    print_r($dbh->errorInfo());
}
?>
```

O exemplo acima produzirá:

```
PDO::errorInfo():
Array
(
    [0] => HY000
    [1] => 1
    [2] => near "bogus": syntax error
)
```

### Veja também

- [PDO::errorCode()](pdo.errorcode.md) - Busca o SQLSTATE associado com a última operação no identificador do banco de dados
- [PDOStatement::errorCode()](pdostatement.errorcode.md) - Busca o SQLSTATE associado com a última operação no objeto da instrução
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
