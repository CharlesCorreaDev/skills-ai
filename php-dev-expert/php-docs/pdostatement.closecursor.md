# Fecha o cursor, permitindo que a instrução seja executada novamente

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.closecursor.php

---

# PDOStatement::closeCursor

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.9.0)

PDOStatement::closeCursor — 
Fecha o cursor, permitindo que a instrução seja executada novamente

### Descrição

public function **PDOStatement::closeCursor**(): [bool](language.types.boolean.md)

**PDOStatement::closeCursor()** libera a conexão
ao servidor de forma que outras instruções SQL possam ser emitidas, mas deixa a
instrução em um estado que permite que ela seja executada novamente.

Este método é útil para drivers de banco de dados que não suportam a execução de
um objeto PDOStatement quando um object PDOStatement executado anteriormente ainda
tem registros não recebidos. Se o driver do banco de dados sofrer desta limitação,
o problema pode se manifestar em um erro de "fora-de-sequência".

**PDOStatement::closeCursor()** é implementado como um
método opcional específico do driver (permitindo máxima eficiência), ou como
o método PDO genérico se nenhuma função específica do driver estiver instalada.
O método PDO genérico é semanticamente o mesmo que escrever o seguinte código no
script PHP:

```
<?php
do {
    while ($stmt->fetch())
        ;
    if (!$stmt->nextRowset())
        break;
} while (true);
?>
```

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Um exemplo de **PDOStatement::closeCursor()****

No exemplo a seguire, o objeto PDOStatement $stmt
retorna múltiplos registros mas a aplicação busca apenas a primeira
linha, deixando o objeto PDOStatement em um estado com linhas não recebidas.
Para assegurar que a aplicação irá funcionar com todos os drivers de banco de dados, o
autor insere uma chamada a **PDOStatement::closeCursor()**
na variável $stmt antes de executar o objeto
PDOStatement $otherStmt.

```
<?php
/* Cria um objeto PDOStatement */
$stmt = $dbh->prepare('SELECT foo FROM bar');

/* Cria um segundo objeto PDOStatement */
$otherStmt = $dbh->prepare('SELECT foobaz FROM foobar');

/* Executa a primeira instrução */
$stmt->execute();

/* Busca somente a primeira linha do resultado */
$stmt->fetch();

/* A chamada a closeCursor() pode ser requerida por alguns drivers */
$stmt->closeCursor();

/* Agora pode-se executar a segunda instrução */
$otherStmt->execute();
?>
```

### Veja também

- [PDOStatement::execute()](pdostatement.execute.md) - Executa ums instrução preparada

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
