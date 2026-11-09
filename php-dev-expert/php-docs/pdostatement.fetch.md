# Busca a próxima linha de um resultado

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.fetch.php

---

# PDOStatement::fetch

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDOStatement::fetch — 
Busca a próxima linha de um resultado

### Descrição

public function **PDOStatement::fetch**([int](language.types.integer.md) `$mode` = **`PDO::FETCH_DEFAULT`**, [int](language.types.integer.md) `$cursorOrientation` = **`PDO::FETCH_ORI_NEXT`**, [int](language.types.integer.md) `$cursorOffset` = 0): [mixed](language.types.mixed.md)

Busca uma linha de um resultado associado com um objeto PDOStatement object. O
parâmetro `mode` determina como o PDO retorna
a linha.

### Parâmetros

`mode`
:   Controla como a próxima linha será retornada ao chamador. Este valor
    precisa ser uma das constantes `PDO::FETCH_*`,
    padronizado para o valor de `PDO::ATTR_DEFAULT_FETCH_MODE`
    (cujo padrão é `PDO::FETCH_BOTH`).

    - `PDO::FETCH_ASSOC`: retorna um array indexado pelo nome da
      coluna como retornada no resultado
    - `PDO::FETCH_BOTH` (padrão): retorna um array indexado tanto
      por nome de coluna quanto por número de coluna indexado em 0, como retornado no
      resultado
    - `PDO::FETCH_BOUND`: retorna **`true`** e atribui os
      valores das colunas no conjunto de resultados às variáveis PHP às quais
      eles foram vinculados com o método
      [PDOStatement::bindColumn()](pdostatement.bindcolumn.md)
    - `PDO::FETCH_CLASS`: retorna uma nova instância da classe
      solicitada. O objeto é inicializado mapeando as colunas do
      conjunto de resultados para propriedades na classe. Isso ocorre antes do
      construtor ser chamado, permitindo que as propriedades sejam preenchidas independentemente
      de sua visibilidade ou se estão marcadas como `readonly`.
      Se uma propriedade não existir na classe, o método mágico [\_\_set()](language.oop5.overloading.md#object.set)
      será invocado se existir; caso contrário, será criada uma propriedade
      pública dinâmica. Entretanto, quando **`PDO::FETCH_PROPS_LATE`**
      também é fornecido, o construtor é chamado *antes*
      de as propriedades serem preenchidas. Se `mode` incluir
      **`PDO::FETCH_CLASSTYPE`** (por exemplo,
      `PDO::FETCH_CLASS | PDO::FETCH_CLASSTYPE`), o nome
      da classe é determinado a partir do valor da primeira coluna.
    - `PDO::FETCH_INTO`: atualiza uma instância existente
      da classe solicitada, mapeando as colunas do conjunto de resultados às
      propriedades nomeadas na classe
    - `PDO::FETCH_LAZY`: combina
      `PDO::FETCH_BOTH` e `PDO::FETCH_OBJ`,
      e retorna um objeto [PDORow](class.pdorow.md)
      que cria os nomes das propriedades do objeto conforme elas são acessadas.
    - `PDO::FETCH_NAMED`: retorna um array com a mesma
      forma de `PDO::FETCH_ASSOC`, exceto que se houver
      múltiplas colunas com o mesmo nome, o valor referenciado pela
      chave será um array de todos os valores na linha que tiverem
      esse nome de coluna
    - `PDO::FETCH_NUM`: retorna um array indexado por número de
      coluna como retornado no conjunto de resultados, iniciando na coluna 0
    - `PDO::FETCH_OBJ`: retorna um objeto anônimo com
      nomes de propriedades que correspondem ao nomes de colunas retornados no
      conjunto de resultados
    - `PDO::FETCH_PROPS_LATE`: quando usado com
      `PDO::FETCH_CLASS`, o construtor da classe é
      chamado antes que as propriedades sejam atribuídas com os respectivos
      valores das colunas.

`cursorOrientation`
:   Para um objeto PDOStatement representando um cursor navegável, este
    valor determina que linha será retornada ao chamador. Este valor
    precisa ser uma das constantes `PDO::FETCH_ORI_*`,
    sendo o padrão igual a `PDO::FETCH_ORI_NEXT`. Para requisitar um
    cursor navegável para o objeto PDOStatement, o atributo
    `PDO::ATTR_CURSOR` precisa ser definido para
    `PDO::CURSOR_SCROLL` ao preparar a instrução
    SQL com [PDO::prepare()](pdo.prepare.md).

`cursorOffset`
:   Para um objeto PDOStatement representando um cursor navegável para o qual
    o parâmetro `cursorOrientation` esteja definido para
    `PDO::FETCH_ORI_ABS`, este valor especifica o
    número absoluto da linha no conjunto de resultados que deve ser buscada.

    Para um objeto PDOStatement representando um cursor navegável para o qual
    o parâmetro `cursorOrientation` esteja definido para
    `PDO::FETCH_ORI_REL`, este valor especifica a
    linha a ser buscada relativa à posição do cursor antes do método
    **PDOStatement::fetch()** ser chamado.

### Valor Retornado

O valor de retorno desta função em caso de sucesso depende do tipo de busca. Em
todos os casos, **`false`** é retornado em caso de falha ou se não houver mais linhas.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Buscando linhas usando estilos de busca diferentes**

```
<?php
$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

/* Exercita estilos de PDOStatement::fetch */
print "PDO::FETCH_ASSOC: ";
print "Retorna a próxima linha como um array indexado por nome de coluna\n";
$result = $sth->fetch(PDO::FETCH_ASSOC);
print_r($result);
print "\n";

print "PDO::FETCH_BOTH: ";
print "Retorna a próxima linha como um array indexado por nome de coluna e número\n";
$result = $sth->fetch(PDO::FETCH_BOTH);
print_r($result);
print "\n";

print "PDO::FETCH_LAZY: ";
print "Retorna a próxima linha como um objeto PDORow com nomes de colunas como propriedades\n";
$result = $sth->fetch(PDO::FETCH_LAZY);
print_r($result);
print "\n";

print "PDO::FETCH_OBJ: ";
print "Retorna a próxima linha como um objeto anônimo com nomes de coluna como propriedades\n";
$result = $sth->fetch(PDO::FETCH_OBJ);
print $result->name;
print "\n";
?>
```

O exemplo acima produzirá:

```
PDO::FETCH_ASSOC: Retorna a próxima linha como um array indexado por nome de coluna
Array
(
    [name] => apple
    [colour] => red
)

PDO::FETCH_BOTH: Retorna a próxima linha como um array indexado por nome de coluna e número
Array
(
    [name] => banana
    [0] => banana
    [colour] => yellow
    [1] => yellow
)

PDO::FETCH_LAZY: Retorna a próxima linha como um objeto PDORow com nomes de colunas como propriedades
PDORow Object
(
    [name] => orange
    [colour] => orange
)

PDO::FETCH_OBJ: Retorna a próxima linha como um objeto anônimo com nomes de coluna como propriedades
kiwi
```

**Exemplo #2 Buscando linhas com um cursor navegável**

```
<?php
function readDataForwards($dbh) {
    $sql = 'SELECT hand, won, bet FROM mynumbers ORDER BY BET';
    $stmt = $dbh->prepare($sql, array(PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL));
    $stmt->execute();
    while ($row = $stmt->fetch(PDO::FETCH_NUM, PDO::FETCH_ORI_NEXT)) {
        $data = $row[0] . "\t" . $row[1] . "\t" . $row[2] . "\n";
        print $data;
    }
}
function readDataBackwards($dbh) {
    $sql = 'SELECT hand, won, bet FROM mynumbers ORDER BY bet';
    $stmt = $dbh->prepare($sql, array(PDO::ATTR_CURSOR => PDO::CURSOR_SCROLL));
    $stmt->execute();
    $row = $stmt->fetch(PDO::FETCH_NUM, PDO::FETCH_ORI_LAST);
    do {
        $data = $row[0] . "\t" . $row[1] . "\t" . $row[2] . "\n";
        print $data;
    } while ($row = $stmt->fetch(PDO::FETCH_NUM, PDO::FETCH_ORI_PRIOR));
}

print "Lendo para a frente:\n";
readDataForwards($conn);

print "Lendo para trás:\n";
readDataBackwards($conn);
?>
```

O exemplo acima produzirá:

```
Reading forwards:
21    10    5
16    0     5
19    20    10

Reading backwards:
19    20    10
16    0     5
21    10    5
```

**Exemplo #3 Ordem de construção**

Quando objetos são buscados através de **`PDO::FETCH_CLASS`**, as propriedades
do objeto são atribuídas primeiro, e depois o construtor da classe é
invocado. Entretanto, quando **`PDO::FETCH_PROPS_LATE`** também for informada,
esta ordem é revertida, isto, é, primeiro o construtor é chamado, e
depois as propriedades são atribuídas.

```
<?php
class Person
{
    private $name;

    public function __construct()
    {
        $this->tell();
    }

    public function tell()
    {
        if (isset($this->name)) {
            echo "Eu sou {$this->name}.\n";
        } else {
            echo "Eu não tenho um nome ainda.\n";
        }
    }
}

$sth = $dbh->query("SELECT * FROM people");
$sth->setFetchMode(PDO::FETCH_CLASS, 'Person');
$person = $sth->fetch();
$person->tell();
$sth->setFetchMode(PDO::FETCH_CLASS|PDO::FETCH_PROPS_LATE, 'Person');
$person = $sth->fetch();
$person->tell();
?>
```

O exemplo acima produzirá
algo semelhante a:

```
Eu sou Alice.
Eu sou Alice.
Eu não tenho um nome ainda.
Eu sou Bob.
```

### Veja também

- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
- [PDOStatement::execute()](pdostatement.execute.md) - Executa ums instrução preparada
- [PDOStatement::fetchAll()](pdostatement.fetchall.md) - Busca as linhas remanescentes de um conjunto de resultados
- [PDOStatement::fetchColumn()](pdostatement.fetchcolumn.md) - Retorna uma única coluna do próximo registro de um resultado
- [PDOStatement::fetchObject()](pdostatement.fetchobject.md) - Busca o próximo registro e retorna-o como um objeto
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
