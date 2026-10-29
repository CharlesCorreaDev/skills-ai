# Busca as linhas remanescentes de um conjunto de resultados

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.fetchall.php

---

# PDOStatement::fetchAll

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDOStatement::fetchAll — 
Busca as linhas remanescentes de um conjunto de resultados

### Descrição

public function **PDOStatement::fetchAll**([int](language.types.integer.md) `$mode` = PDO::FETCH\_DEFAULT): [array](language.types.array.md)

public function **PDOStatement::fetchAll**([int](language.types.integer.md) `$mode` = PDO::FETCH\_COLUMN, [int](language.types.integer.md) `$column`): [array](language.types.array.md)

public function **PDOStatement::fetchAll**([int](language.types.integer.md) `$mode` = PDO::FETCH\_CLASS, [string](language.types.string.md) `$class`, [?](language.types.null.md)[array](language.types.array.md) `$constructorArgs`): [array](language.types.array.md)

public function **PDOStatement::fetchAll**([int](language.types.integer.md) `$mode` = PDO::FETCH\_FUNC, [callable](language.types.callable.md) `$callback`): [array](language.types.array.md)

### Parâmetros

`mode`
:   Controla o conteúdo do array retornado como documentado em
    [PDOStatement::fetch()](pdostatement.fetch.md).
    O padrão é **`PDO::ATTR_DEFAULT_FETCH_MODE`**
    (cujo padrão é **`PDO::FETCH_BOTH`**).

    Para retornar um array que consiste em todos os valores de uma única coluna do
    conjunto de resultados, especifique **`PDO::FETCH_COLUMN`**. Pode-se
    especificar uma coluna qualquer com o parâmetro
    `column`.

    Para indexar o array resultante pelo valor de uma determinada coluna (em vez de
    números consecutivos), coloque o nome desta coluna primeiro na lista de
    colunas no SQL e use **`PDO::FETCH_UNIQUE`**.
    Esta coluna deve conter apenas valores exclusivos ou alguns dados serão perdidos.

    Para agrupar resultados na forma de um array tridimensional indexado por valores
    de uma coluna especificada, coloque o nome desta coluna primeiro na
    lista de colunas no SQL e use **`PDO::FETCH_GROUP`**.

    Para agrupar resultados na forma de um array bidimensional,
    use a operação OR binária com **`PDO::FETCH_GROUP`** e
    **`PDO::FETCH_COLUMN`**.
    Os resultados serão agrupados pela primeira coluna, com o valor do elemento do array
    sendo um array de lista das entradas correspondentes da segunda coluna.

A lista a seguir apresenta parâmetros dinâmicos que dependem do modo de busca.
Eles não podem ser usados com parâmetros nomeados.

`column`
:   Usado com **`PDO::FETCH_COLUMN`**. Retorna a coluna indicada
    com índice iniciando em 0.

`class`
:   Usado com **`PDO::FETCH_CLASS`**. Retorna instâncias da classe
    especificada, mapeando colunas de cada linha a propriedades nomeadas na classe.

`constructorArgs`
:   Argumentos de construtor de classe customizado quando o parâmetro `mode`
    for **`PDO::FETCH_CLASS`**.

`callback`
:   Usado com **`PDO::FETCH_FUNC`**. Retorna os resultados da chamada à
    função especificada, usando cada coluna do registro como parâmetro na chamada.

### Valor Retornado

**PDOStatement::fetchAll()** retorna um array contendo
todas os registros remanescentes no conjunto de resultados O array representa cada
registro como um array de valores de coluna ou um objeto com propriedades
correspondentes a cada nome de coluna. Um array vazio é retornado se não
houver resultados na busca.

Usar este método para burcar conjuntos de resultados grandes resultará em uma alta
demanda no sistema e possivelmente em recursos de rede. Ao invés de recuperar
todos os dados e manipulá-los no PHP, deve ser considerado usar o servidor de
banco de dados para manipular os conjuntos de resultados. Por exemplo, usando as cláusulas
WHERE e ORDER BY no SQL para restringir resultados antes de recuperá-los e
processá-los com o PHP.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | Este método agora sempre retornará um [array](language.types.array.md), enquanto antes poderia retornar **`false`** em caso de falha. |

### Examples

**Exemplo #1 Buscando todos os registros remanescentes em um conjunto de resultados**

```
<?php
$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

/* Busca todos os registros remanescentes em um conjunto de resultados */
print "Busca todos os registros remanescentes em um conjunto de resultados:\n";
$result = $sth->fetchAll();
print_r($result);
?>
```

O exemplo acima produzirá
algo semelhante a:

```
Busca todos os registros remanescentes em um conjunto de resultados:
Array
(
    [0] => Array
        (
            [name] => apple
            [0] => apple
            [colour] => red
            [1] => red
        )

    [1] => Array
        (
            [name] => pear
            [0] => pear
            [colour] => green
            [1] => green
        )

    [2] => Array
        (
            [name] => watermelon
            [0] => watermelon
            [colour] => pink
            [1] => pink
        )

)
```

**Exemplo #2 Buscando todos os valores de uma única coluna de um resultado**

O exemplo a seguir demonstra como retornar todos os valores de uma
única coluna de um resultado, mesmo que a instrução SQL em si
possa retornar múltiplas colunas por registro.

```
<?php
$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

/* Busca todos os valores da primeira coluna */
$result = $sth->fetchAll(PDO::FETCH_COLUMN, 0);
var_dump($result);
?>
```

O exemplo acima produzirá
algo semelhante a:

```
Array(3)
(
    [0] =>
    string(5) => apple
    [1] =>
    string(4) => pear
    [2] =>
    string(10) => watermelon
)
```

**Exemplo #3 Agrupando todos os valores por uma única coluna**

O exemplo a seguir demonstra como retornar um array associativo
agrupado pelos valores da coluna especificada no resultado. O
array contém três chaves: valores `apple` e
`pear` são retornados como arrays que contêm duas
cores diferentes, enquanto `watermelon` é
retornado como um array qye contém apenas uma cor.

```
<?php
$insert = $dbh->prepare("INSERT INTO fruit(name, colour) VALUES (?, ?)");
$insert->execute(array('apple', 'green'));
$insert->execute(array('pear', 'yellow'));

$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

/* Agrupa valores pela primeira coluna */
var_dump($sth->fetchAll(PDO::FETCH_COLUMN|PDO::FETCH_GROUP));
?>
```

O exemplo acima produzirá
algo semelhante a:

```
array(3) {
  ["apple"]=>
  array(2) {
    [0]=>
    string(5) "green"
    [1]=>
    string(3) "red"
  }
  ["pear"]=>
  array(2) {
    [0]=>
    string(5) "green"
    [1]=>
    string(6) "yellow"
  }
  ["watermelon"]=>
  array(1) {
    [0]=>
    string(5) "pink"
  }
}
```

**Exemplo #4 Instanciando uma classe para cada resultado**

O exemplo a seguir demonstra o comportamento do
estilo de busca **`PDO::FETCH_CLASS`**.

```
<?php
class fruit {
    public $name;
    public $colour;
}

$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

$result = $sth->fetchAll(PDO::FETCH_CLASS, "fruit");
var_dump($result);
?>
```

O exemplo acima produzirá
algo semelhante a:

```
array(3) {
  [0]=>
  object(fruit)#1 (2) {
    ["name"]=>
    string(5) "apple"
    ["colour"]=>
    string(5) "green"
  }
  [1]=>
  object(fruit)#2 (2) {
    ["name"]=>
    string(4) "pear"
    ["colour"]=>
    string(6) "yellow"
  }
  [2]=>
  object(fruit)#3 (2) {
    ["name"]=>
    string(10) "watermelon"
    ["colour"]=>
    string(4) "pink"
  }
  [3]=>
  object(fruit)#4 (2) {
    ["name"]=>
    string(5) "apple"
    ["colour"]=>
    string(3) "red"
  }
  [4]=>
  object(fruit)#5 (2) {
    ["name"]=>
    string(4) "pear"
    ["colour"]=>
    string(5) "green"
  }
}
```

**Exemplo #5 Chamando uma função para cada resultado**

O exemplo a seguir demonstra o comportamento do
estilo de busca **`PDO::FETCH_FUNC`**.

```
<?php
function fruit($name, $colour) {
    return "{$name}: {$colour}";
}

$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

$result = $sth->fetchAll(PDO::FETCH_FUNC, "fruit");
var_dump($result);
?>
```

O exemplo acima produzirá
algo semelhante a:

```
array(3) {
  [0]=>
  string(12) "apple: green"
  [1]=>
  string(12) "pear: yellow"
  [2]=>
  string(16) "watermelon: pink"
  [3]=>
  string(10) "apple: red"
  [4]=>
  string(11) "pear: green"
}
```

### Veja também

- [PDO::query()](pdo.query.md) - Prepara e executa uma instrução SQL sem marcadores
- [PDOStatement::fetch()](pdostatement.fetch.md) - Busca a próxima linha de um resultado
- [PDOStatement::fetchColumn()](pdostatement.fetchcolumn.md) - Retorna uma única coluna do próximo registro de um resultado
- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
- [PDOStatement::setFetchMode()](pdostatement.setfetchmode.md) - Define o modo de carga de dados para esta instrução

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
