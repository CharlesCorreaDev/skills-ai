# Executa ums instrução preparada

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.execute.php

---

# PDOStatement::execute

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDOStatement::execute — 
Executa ums instrução preparada

### Descrição

public function **PDOStatement::execute**([?](language.types.null.md)[array](language.types.array.md) `$params` = **`null`**): [bool](language.types.boolean.md)

Executa a [instrução
preparada](pdo.prepared-statements.md). Se a instrução preparada inclui marcadores de parâmetros:

- [PDOStatement::bindParam()](pdostatement.bindparam.md) e/ou
  [PDOStatement::bindValue()](pdostatement.bindvalue.md) devem ser chamadas para vincular variáveis ou
  valores (respectivamente) aos marcadores de parâmetros. Variáveis vinculadas passam
  seus valores como entrada e recebem o valor de saída, se houver, de seus
  marcadores de parâmetros associados
- ou um array de valores de parâmetros, de entrada somente, deve ser passado

### Parâmetros

`params`
:   Um array de valores com tantos elementos quantos forem os
    parâmetros vinculados na instrução SQL sendo executada.
    Todos os valores são tratados como **`PDO::PARAM_STR`**.

    Valores múltiplos não podem ser vinculados a um parâmetro único; por exemplo,
    não é permitido vincular dois valores a um único parâmetro nomeado em uma cláusula
    IN().

    Vincular mais valores que o especificado não é possível; se existirem mais chaves em
    `params` que no SQL especificado
    em [PDO::prepare()](pdo.prepare.md), a instrução
    falhará e um erro será emitido.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Executa uma instrução preparada com variável e valor vinculados**

```
<?php
/* Executa uma instrução preparada vinculando uma variável e um valor */
$calorias = 150;
$cor = 'ver';
$sth = $dbh->prepare('SELECT nome, cor, calorias
    FROM frutas
    WHERE calorias < :calorias AND cor LIKE :cor');
$sth->bindParam('calorias', $calorias, PDO::PARAM_INT);
/* Nomes podem ser prefixados com dois-pontos ":" também (opcional) */
$sth->bindValue(':cor', "%$cor%");
$sth->execute();
?>
```

**Exemplo #2 Executa uma instrução preparada com um array de valores nomeados**

```
<?php
/* Executa uma instrução preparada passando um array de valores de inserção */
$calorias = 150;
$cor = 'vermelha';
$sth = $dbh->prepare('SELECT nome, cor, calorias
    FROM frutas
    WHERE calorias < :calorias AND cor = :cor');
$sth->execute(array('calorias' => $calorias, 'cor' => $cor));
/* Chaves de array podem ser prefixadas com dois-pontos ":" também (opcional) */
$sth->execute(array(':calorias' => $calorias, ':cor' => $cor));
?>
```

**Exemplo #3 Executa uma instrução preparada com um array de valores posicionais**

```
<?php
/* Executa uma instrução preparada passando um array de valores de inserção */
$calorias = 150;
$cor = 'vermelha';
$sth = $dbh->prepare('SELECT nome, cor, calorias
    FROM frutas
    WHERE calorias < ? AND cor = ?');
$sth->execute(array($calorias, $cor));
?>
```

**Exemplo #4 Executa uma instrução preparada com variáveis vinculadas a marcadores posicionais**

```
<?php
/* Executa uma instrução preparada vinculando variáveis PHP */
$calorias = 150;
$cor = 'vermelha';
$sth = $dbh->prepare('SELECT nome, cor, calorias
    FROM frutas
    WHERE calorias < ? AND cor = ?');
$sth->bindParam(1, $calorias, PDO::PARAM_INT);
$sth->bindParam(2, $cor, PDO::PARAM_STR, 12);
$sth->execute();
?>
```

**Exemplo #5 Executa uma instrução preparada usando array para cláusula IN**

```
<?php
/* Executa uma instrução preparada usando um array de valores para uma cláusula IN */
$params = array(1, 21, 63, 171);
/* Cria uma string para marcadores de parâmetros preenchidas com o número de parâmetros */
$place_holders = '?' . str_repeat(', ?', count($params) - 1);

/*
    Isto prepara a instrução com marcadores anônimos suficientes para cada valor
    no array $params. Os valores do array $params são então vinculados aos
    marcadores na instrução preparada quando ele é executada.
    Isto não é a mesma coisa que usar PDOStatement::bindParam() já que isso
    requer uma referência à variável. PDOStatement::execute() apenas vincula
    por valor.
*/
$sth = $dbh->prepare("SELECT id, nome FROM contatos WHERE id IN ($place_holders)");
$sth->execute($params);
?>
```

### Notas

> **Nota**:
>
> Alguns drivers requerem que o [cursor seja
> fechado](pdostatement.closecursor.md) antes da execução da próxima instrução.

### Veja também

- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
- [PDOStatement::bindParam()](pdostatement.bindparam.md) - Vincula um parâmetro ao nome de variável especificado
- [PDOStatement::fetch()](pdostatement.fetch.md) - Busca a próxima linha de um resultado
- [PDOStatement::fetchAll()](pdostatement.fetchall.md) - Busca as linhas remanescentes de um conjunto de resultados
- [PDOStatement::fetchColumn()](pdostatement.fetchcolumn.md) - Retorna uma única coluna do próximo registro de um resultado

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
