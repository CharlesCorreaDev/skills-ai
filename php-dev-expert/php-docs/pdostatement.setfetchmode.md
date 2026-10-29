# Define o modo de carga de dados para esta instrução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.setfetchmode.php

---

# PDOStatement::setFetchMode

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.2.0)

PDOStatement::setFetchMode — 
Define o modo de carga de dados para esta instrução

### Descrição

public function **PDOStatement::setFetchMode**([int](language.types.integer.md) `$mode`): [true](language.types.singleton.md)

public function **PDOStatement::setFetchMode**([int](language.types.integer.md) `$mode` = PDO::FETCH\_COLUMN, [int](language.types.integer.md) `$colno`): [true](language.types.singleton.md)

public function **PDOStatement::setFetchMode**([int](language.types.integer.md) `$mode` = PDO::FETCH\_CLASS, [string](language.types.string.md) `$class`, [?](language.types.null.md)[array](language.types.array.md) `$constructorArgs` = **`null`**): [true](language.types.singleton.md)

public function **PDOStatement::setFetchMode**([int](language.types.integer.md) `$mode` = PDO::FETCH\_INTO, [object](language.types.object.md) `$object`): [true](language.types.singleton.md)

### Parâmetros

`mode`
:   O modo de carga precisa ser uma das
    constantes
    [**`PDO::FETCH_*`**](pdo.constants.md).

`colno`
:   Número da coluna.

`class`
:   Nome da classe.

`constructorArgs`
:   Argumentos do construtor.

`object`
:   Objeto.

### Valor Retornado

Sempre retorna **`true`**.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.4.0 | O tipo do retorno agora é **`true`**; anteriormente, era [bool](language.types.boolean.md). |

### Examples

**Exemplo #1 Definindo um modo de carga**

O seguinte exemplo demonstra como o
**PDOStatement::setFetchMode()** altera o modo padrão de carga
em um objeto PDOStatement.

```
<?php
$stmt = $dbh->query('SELECT name, colour, calories FROM fruit');
$stmt->setFetchMode(PDO::FETCH_NUM);
foreach ($stmt as $row) {
    print $row[0] . "\t" . $row[1] . "\t" . $row[2] . "\n";
}
```

O exemplo acima produzirá
algo semelhante a:

```
apple   red     150
banana  yellow  250
orange  orange  300
kiwi    brown   75
lemon   yellow  25
pear    green   150
```

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
