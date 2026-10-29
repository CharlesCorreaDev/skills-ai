# Vincula um valor a um parâmetro

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.bindvalue.php

---

# PDOStatement::bindValue

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 1.0.0)

PDOStatement::bindValue — 
Vincula um valor a um parâmetro

### Descrição

public function **PDOStatement::bindValue**([string](language.types.string.md)|[int](language.types.integer.md) `$param`, [mixed](language.types.mixed.md) `$value`, [int](language.types.integer.md) `$type` = **`PDO::PARAM_STR`**): [bool](language.types.boolean.md)

Vincula um valor a um marcador, nomeado ou de ponto de interrogação,
na instrução SQL que foi usada para preparar a instrução.

### Parâmetros

`param`
:   Identificador do parâmetro. Para uma instrução preparada que usa marcadores
    nomeados, será um nome de parâmetro na forma
    :name. Para uma instrução preparada que usa marcadores
    pontos de interrogação, será a posição indexada do parâmetro,
    iniciando em 1.

`value`
:   O valor a ser vinculado ao parâmetro.

`type`
:   Tipo de dado explícito para o parâmetro, usando as constantes [`PDO::PARAM_*`](pdo.constants.md).

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Executando uma instrução preparada com marcadores nomeados**

```
<?php
/* Executando uma instrução preparada vinculando variáveis do PHP */
$calories = 150;
$colour = 'red';
$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < :calories AND colour = :colour');

/* Define um valor para o parâmetro usando seu nome */
$sth->bindValue('calories', $calories, PDO::PARAM_INT);
/* Opcionalmente, os nomes de parâmetros podem ser prefixados com dois pontos ":" */
$sth->bindValue(':colour', $colour, PDO::PARAM_STR);
$sth->execute();
?>
```

**Exemplo #2 Executando uma instrução preparada com marcadores de ponto de interrogação**

```
<?php
/* Executando uma instrução preparada vinculando variáveis do PHP */
$calories = 150;
$colour = 'red';
$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < ? AND colour = ?');
$sth->bindValue(1, $calories, PDO::PARAM_INT);
$sth->bindValue(2, $colour, PDO::PARAM_STR);
$sth->execute();
?>
```

### Veja também

- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
- [PDOStatement::execute()](pdostatement.execute.md) - Executa ums instrução preparada
- [PDOStatement::bindParam()](pdostatement.bindparam.md) - Vincula um parâmetro ao nome de variável especificado

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
