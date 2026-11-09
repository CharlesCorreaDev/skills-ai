# Despeja uma instrução preparada SQL

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.debugdumpparams.php

---

# PDOStatement::debugDumpParams

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.9.0)

PDOStatement::debugDumpParams — 
Despeja uma instrução preparada SQL

### Descrição

public function **PDOStatement::debugDumpParams**(): [?](language.types.null.md)[bool](language.types.boolean.md)

Despeja a informação contida em uma instrução preparada diretamente na
saída. Fornece a consulta `SQL` em uso, o
número de parâmetros usados (`Params`), a lista
de parâmetros com seus nomes de chave ou posição, seus nomes, suas posições
na consulta (se for suportado pelo driver PDO, caso contrário será
-1), tipo (`param_type`) como um inteiro, e um valor
booleano `is_param`.

Esta é uma função de depuração, que despeja os dados diretamente na saída
padrão.

**Dica**

Assim como qualquer coisa que envia
seu resultado diretamente para o navegador, as [funções de controle de saída](book.outcontrol.md) podem ser usadas para capturar
a saída desta função e salvá-la em uma
[string](language.types.string.md), por exemplo.

Esta função somente despejará os parâmetros na instrução no momento
do despejo. Parâmetros extras não são armazenados na instrução,
e não serão mostrados.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`null`**, ou **`false`** em caso de erro.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 7.2.0 | **PDOStatement::debugDumpParams()** agora retorna o SQL enviado ao banco de dados, incluindo a consulta completa, bruta (incluindo os marcadores substituídos por seus valores vinculados). Observe que isto só estará disponível se as instrução preparadas emuladas estiverem habilitadas. |

### Examples

**Exemplo #1 Exemplo de **PDOStatement::debugDumpParams()** com parâmetros nomeados**

```
<?php
/* Executa uma instrução preparada vinculando variáveis PHP */
$calories = 150;
$colour = 'red';
$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < :calories AND colour = :colour');
$sth->bindParam(':calories', $calories, PDO::PARAM_INT);
$sth->bindValue(':colour', $colour, PDO::PARAM_STR, 12);
$sth->execute();

$sth->debugDumpParams();

?>
```

O exemplo acima produzirá:

```
SQL: [96] SELECT name, colour, calories
    FROM fruit
    WHERE calories < :calories AND colour = :colour
Params:  2
Key: Name: [9] :calories
paramno=-1
name=[9] ":calories"
is_param=1
param_type=1
Key: Name: [7] :colour
paramno=-1
name=[7] ":colour"
is_param=1
param_type=2
```

**Exemplo #2 Exemplo de **PDOStatement::debugDumpParams()** com parâmetros anônimos**

```
<?php

/* Executa uma instrução preparada vinculando variáveis PHP */
$calories = 150;
$colour = 'red';
$name = 'apple';

$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < ? AND colour = ?');
$sth->bindParam(1, $calories, PDO::PARAM_INT);
$sth->bindValue(2, $colour, PDO::PARAM_STR);
$sth->execute();

$sth->debugDumpParams();

?>
```

O exemplo acima produzirá:

```
SQL: [82] SELECT name, colour, calories
    FROM fruit
    WHERE calories < ? AND colour = ?
Params:  2
Key: Position #0:
paramno=0
name=[0] ""
is_param=1
param_type=1
Key: Position #1:
paramno=1
name=[0] ""
is_param=1
param_type=2
```

### Veja também

- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
- [PDOStatement::bindParam()](pdostatement.bindparam.md) - Vincula um parâmetro ao nome de variável especificado
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
