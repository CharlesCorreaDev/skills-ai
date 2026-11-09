# Vincula um parâmetro ao nome de variável especificado

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.bindparam.php

---

# PDOStatement::bindParam

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDOStatement::bindParam — 
Vincula um parâmetro ao nome de variável especificado

### Descrição

public function **PDOStatement::bindParam**(  
    [string](language.types.string.md)|[int](language.types.integer.md) `$param`,  
    [mixed](language.types.mixed.md) `&$var`,  
    [int](language.types.integer.md) `$type` = **`PDO::PARAM_STR`**,  
    [int](language.types.integer.md) `$maxLength` = 0,  
    [mixed](language.types.mixed.md) `$driverOptions` = **`null`**  
): [bool](language.types.boolean.md)

Vincula uma variável PHP a um marcador nomeado ou de ponto de interrogação correspondente
na instrução SQL que foi usada para preparar a instrução. Ao contrário de
[PDOStatement::bindValue()](pdostatement.bindvalue.md), a variável é vinculada como uma
referência e só será avaliada no momento em que
[PDOStatement::execute()](pdostatement.execute.md) for chamado.

A maioria dos parâmetros são parâmetros de entrada, ou seja, parâmetros que são usados
​​somente leitura para construir a consulta (mas podem, mesmo assim, ser convertidos
de acordo com o `type`). Alguns drivers suportam a
invocação de procedimentos armazenados que retornam dados como parâmetros de saída,
e alguns também como parâmetros de entrada/saída que tanto enviam dados quanto são
atualizados para recebê-los.

### Parâmetros

`param`
:   Identificador de parâmetro. Para uma instrução preparada usando marcadores
    nomeados, este será um nome de parâmetro no formato
    :name. Para uma instrução preparada usando
    marcadores de pontos de interrogação, esta será a posição indexada em 1
    do parâmetro.

`var`
:   Nome da variável PHP a ser vinculada ao parâmetro da instrução SQL.

`type`
:   Tipo explícito de dados para o parâmetro usando as [constantes
    `PDO::PARAM_*`](pdo.constants.md).
    Para retornar um parâmetro INOUT de um procedimento armazenado,
    deve-se usar o operador binário OR para definir os bits **`PDO::PARAM_INPUT_OUTPUT`**
    para o parâmetro `type`.

`maxLength`
:   Comprimento do tipo de dados. Para indicar que um parâmetro é um parâmetro
    OUT de um procedimento armazenado, deve-se definir explicitamente o
    comprimento.
    Significativo apenas quando o parâmetro `type` é **`PDO::PARAM_INPUT_OUTPUT`**.

`driverOptions`

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
/* Executa uma instrução preparada vinculando variáveis ​​PHP */
$calories = 150;
$colour = 'red';
$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < :calories AND colour = :colour');
$sth->bindParam('calories', $calories, PDO::PARAM_INT);
/* Os nomes podem ser prefixados com dois pontos ":" também (opcional) */
$sth->bindParam(':colour', $colour, PDO::PARAM_STR);
$sth->execute();
?>
```

**Exemplo #2 Executando uma instrução preparada com marcadores com pontos de interrogação**

```
<?php
/* Executa uma instrução preparada vinculando variáveis ​​PHP */
$calories = 150;
$colour = 'red';
$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < ? AND colour = ?');
$sth->bindParam(1, $calories, PDO::PARAM_INT);
$sth->bindParam(2, $colour, PDO::PARAM_STR);
$sth->execute();
?>
```

**Exemplo #3 Chamando um procedimento armazenado com um parâmetro INOUT**

```
<?php
/* Chamando um procedimento armazenado com um parâmetro INOUT */
$colour = 'red';
$sth = $dbh->prepare('CALL puree_fruit(?)');
$sth->bindParam(1, $colour, PDO::PARAM_STR|PDO::PARAM_INPUT_OUTPUT, 12);
$sth->execute();
print "Após fazer um purê com a fruta, a cor é: $colour";
?>
```

### Veja também

- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
- [PDOStatement::execute()](pdostatement.execute.md) - Executa ums instrução preparada
- [PDOStatement::bindValue()](pdostatement.bindvalue.md) - Vincula um valor a um parâmetro

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
