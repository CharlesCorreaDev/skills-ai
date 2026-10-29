# Busca o SQLSTATE associado com a última operação no identificador do banco de dados

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.errorcode.php

---

# PDO::errorCode

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDO::errorCode — 
Busca o SQLSTATE associado com a última operação no identificador do banco de dados

### Descrição

public function **PDO::errorCode**(): [?](language.types.null.md)[string](language.types.string.md)

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna um SQLSTATE, um identificador alfanumérico de cinco caracteres definido no
padrão ANSI SQL-92. Resumidamente, um SQLSTATE consiste em um
valor de classe de dois caracteres seguido por um valor de subclasse de três caracteres. Um
valor de classe de '01' indica um alerta e é acompanhado por um código de retorno
de SQL\_SUCCESS\_WITH\_INFO. Valores de classe diferentes de '01', exceto pela
classe 'IM', indicam um erro. A classe 'IM' é específica para alertas
e erros que derivam da implementação do próprio PDO (ou talvez do ODBC,
se estiver em uso). O valor de subclasse '000' em qualquer
classe indica que não há subclasse para aquele SQLSTATE.

**PDO::errorCode()** somente busca códigos de erro para operações
realizadas diretamente no identificador do banco de dados. Se for criado um objeto
PDOStatement através de [PDO::prepare()](pdo.prepare.md) ou
[PDO::query()](pdo.query.md) e for invocado um erro no identificador da
instrução, **PDO::errorCode()** não refletirá esse erro.
Deve-se chamar [PDOStatement::errorCode()](pdostatement.errorcode.md) para retornar o código de
erro para uma operação realizada em um identificador de instrução em particular.

Retorna **`null`** se nenhuma operação foi executada no identificador do banco de dados.

### Examples

**Exemplo #1 Buscando um código SQLSTATE**

```
<?php
/* Provoca um erro -- a tabela OSSOS não existe */
$dbh->exec("INSERT INTO ossos(cranio) VALUES ('lucy')");

echo "\nPDO::errorCode(): ", $dbh->errorCode();
?>
```

O exemplo acima produzirá:

```
PDO::errorCode(): 42S02
```

### Veja também

- [PDO::errorInfo()](pdo.errorinfo.md) - Busca informação de erro estendida associada com a última operação no identificador do banco de dados
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
