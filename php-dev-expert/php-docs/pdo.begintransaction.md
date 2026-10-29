# Inicia uma transação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.begintransaction.php

---

# PDO::beginTransaction

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDO::beginTransaction — 
Inicia uma transação

### Descrição

public function **PDO::beginTransaction**(): [bool](language.types.boolean.md)

Desativa o modo de envio automático. Enquanto o modo de envio automático estiver desativado,
modificações feitas no banco de dados por meio da instância do objeto PDO não
serão enviadas até que você finalize a transação chamando [PDO::commit()](pdo.commit.md).
Chamar [PDO::rollBack()](pdo.rollback.md) reverterá todas as alterações no
banco de dados e retornará a conexão para o modo de envio automático.

Alguns bancos de dados, incluindo o MySQL, emitem automaticamente um COMMIT
implícito quando uma instrução de linguagem de definição de banco de dados (DDL)
como DROP TABLE ou CREATE TABLE é emitida em uma transação. O COMMIT
implícito impedirá que você reverta quaisquer outras alterações dentro do
limite da transação.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

Lança uma [PDOException](class.pdoexception.md) se já houver uma transação iniciada ou se o driver não suportar transações.

> **Nota**:
>
> Uma exceção será lançada mesmo quando o atributo **`PDO::ATTR_ERRMODE`** não for **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Reverter uma transação**

O exemplo a seguir inicia uma transação e emite duas instruções que
modificam o banco de dados antes de reverter as alterações.
No MySQL, no entanto, a instrução DROP TABLE envia automaticamente
a transação de modo que nenhuma das alterações na transação é
revertida.

```
<?php
/* Inicia uma transação, desligando o envio automático */
$dbh->beginTransaction();

/* Altera esquema e dados do banco */
$sth = $dbh->exec("DROP TABLE fruit");
$sth = $dbh->exec("UPDATE dessert
    SET name = 'hamburger'");

/* Reconhece o engano e desfaz o envio das alterações */
$dbh->rollBack();

/* A conexão do banco agora está de volta o modo de envio automático */
?>
```

### Veja também

- [PDO::commit()](pdo.commit.md) - Envia uma transação
- [PDO::rollBack()](pdo.rollback.md) - Reverte uma transação
- [Transações e envio automático](pdo.transactions.md)

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
