# Envia uma transação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.commit.php

---

# PDO::commit

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDO::commit — 
Envia uma transação

### Descrição

public function **PDO::commit**(): [bool](language.types.boolean.md)

Envia uma transação, retornando a conexão com o banco de dados para o modo de
envio automático até que a próxima chamada a
[PDO::beginTransaction()](pdo.begintransaction.md) inicie uma nova transação.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

Lança uma [PDOException](class.pdoexception.md) se não houver transação ativa.

> **Nota**:
>
> Uma exceção será lançada mesmo quando o atributo **`PDO::ATTR_ERRMODE`** não for **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Enviando uma transação básica**

```
<?php
/* Inicia uma transação, desligando o envio automático */
$dbh->beginTransaction();

/* Insere múltiplos registros na base do tudo-ou-nada */
$sql = 'INSERT INTO fruit
    (name, colour, calories)
    VALUES (?, ?, ?)';

$sth = $dbh->prepare($sql);

foreach ($fruits as $fruit) {
    $sth->execute(array(
        $fruit->name,
        $fruit->colour,
        $fruit->calories,
    ));
}

/* Envia as alterações */
$dbh->commit();

/* A conexão do banco agora está de volta o modo de envio automático */
?>
```

**Exemplo #2 Enviando uma transação DDL**

```
<?php
/* Inicia uma transação, desligando o envio automático */
$dbh->beginTransaction();

/* Altera esquema do banco */
$sth = $dbh->exec("DROP TABLE fruit");

/* Envia as alterações */
$dbh->commit();

/* A conexão do banco agora está de volta o modo de envio automático */
?>
```

> **Nota**:
>
> Nem todos os bancos de dados permitirão que as transações operem em
> instruções DDL: alguns gerarão erros, enquanto outros (incluindo o MySQL)
> enviarão automaticamente a transação após a primeira instrução DDL ter
> sido encontrada.

### Veja também

- [PDO::beginTransaction()](pdo.begintransaction.md) - Inicia uma transação
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
