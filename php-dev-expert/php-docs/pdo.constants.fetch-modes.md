# Modos de Busca

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.constants.fetch-modes.php

---

## Modos de Busca

Consulte as [constantes de cursores](pdo.constants.md#pdo.constants.cursors) para as
constantes `PDO::FETCH_ORI_*`.

## Modos de Busca Básicos

| Modo de Busca | Resumo |
| --- | --- |
| **`PDO::FETCH_DEFAULT`** | Especifica que o modo de busca padrão deve ser usado. |
| **`PDO::FETCH_ASSOC`** | Array indexado somente pelo nome da coluna. |
| **`PDO::FETCH_BOTH`** (Padrão) | Array indexado tanto pelo nome quanto pelo número da coluna. |
| **`PDO::FETCH_NAMED`** | Variante de **`PDO::FETCH_ASSOC`** que retém colunas duplicadas. |
| **`PDO::FETCH_NUM`** | Array indexado somente pelo número da coluna. |
| **`PDO::FETCH_COLUMN`** | Uma única coluna. |
| **`PDO::FETCH_KEY_PAIR`** | Pares de chave-valor, indexados pela primeira coluna. |
| **`PDO::FETCH_FUNC`** | Usa uma função para criar o valor de retorno. ([PDOStatement::fetchAll()](pdostatement.fetchall.md) somente) |
| **`PDO::FETCH_OBJ`** | Objeto anônimo ([stdClass](class.stdclass.md)). |
| **`PDO::FETCH_CLASS`** | Um objeto de uma classe especificada. |

## Opções de PDO::FETCH\_CLASS

Estes modos são usados para implementar opções ao usar
**`PDO::FETCH_CLASS`**.

| Modo de busca | Resumo |
| --- | --- |
| **`PDO::FETCH_CLASSTYPE`** | Usa a primeira coluna como o nome da classe. |
| **`PDO::FETCH_PROPS_LATE`** | Chama o construtor antes de definir as propriedades. |
| **`PDO::FETCH_SERIALIZE`** | Usa dados serializados do PHP. Descontinuado a partir do PHP 8.1.0. |

## Modos de resultado único

Os modos a seguir não podem ser usados com
[PDOStatement::fetchAll()](pdostatement.fetchall.md).

| Modo de busca | Resumo |
| --- | --- |
| **`PDO::FETCH_BOUND`** | Vincula valores a variáveis especificadas. |
| **`PDO::FETCH_INTO`** | Atualiza um objeto existente. |
| **`PDO::FETCH_LAZY`** | Busca lenta via [PDORow](class.pdorow.md) para acessos como array e objetos. |

## Sinalizadores de comportamento especiais para [PDOStatement::fetchAll()](pdostatement.fetchall.md)

Os seguintes modos especiais para múltiplos resultados funcionam apenas com
[PDOStatement::fetchAll()](pdostatement.fetchall.md) e não funcionam com alguns outros
modos de busca. Consulte a documentação completa para obter detalhes.

| Modo de busca | Resumo |
| --- | --- |
| **`PDO::FETCH_GROUP`** | Os resultados estão agrupados pela primeira coluna. |
| **`PDO::FETCH_UNIQUE`** | Os resultados são indexados (exclusivamente) pela primeira coluna. |

## Tratamento de nomes de colunas duplicados

É possível que os resultados contenham várias colunas com o mesmo nome.
Por exemplo, ao unir duas tabelas que contêm uma coluna com o mesmo
nome.

Como as estruturas do PHP, como arrays e objetos, não suportam múltiplas chaves
ou propriedades com o mesmo nome, o array ou objeto retornado
conterá apenas 1 dos valores com o mesmo nome.

O valor retornado para um determinado nome duplicado deve ser considerado
indefinido.

Para evitar esse problema, nomeie as colunas explicitamente usando um sinônimo. Por exemplo:

```
SELECT table1.created_at AS t1_created_at,
       table2.created_at AS t2_created_at
FROM table1
JOIN table2 ON table1.table2id = table2.id
```

Consulte também **`PDO::FETCH_NAMED`**,
**`PDO::ATTR_FETCH_TABLE_NAMES`** e
**`PDO::ATTR_FETCH_CATALOG_NAMES`**.

## Definindo o modo de busca padrão

É possível definir o modo de busca padrão para todas as consultas usando
**`PDO::ATTR_DEFAULT_FETCH_MODE`** com
[PDO::\_\_construct()](pdo.construct.md) ou
[PDO::setAttribute()](pdo.setattribute.md).

É possível definir o modo de busca padrão para uma instrução específica usando
[PDOStatement::setFetchMode()](pdostatement.setfetchmode.md).
Isso afeta a reutilização como uma instrução preparada e a iteração (usando
[`foreach`](control-structures.foreach.md)).

**Cuidado**

[PDOStatement::setAttribute()](pdostatement.setattribute.md) não pode ser usado para definir o
modo de busca padrão. Ele aceita apenas atributos específicos do driver e ignora silenciosamente
os atributos que não são reconhecidos.

## PDO::FETCH\_DEFAULT ([int](language.types.integer.md))

Disponível a partir do PHP 8.0.7.

Este é um valor especial que usa o modo de busca padrão atual para um
[PDOStatement](class.pdostatement.md). É particularmente útil como o valor padrão
para parâmetros de método ao estender
[PDOStatement](class.pdostatement.md) para uso com
**`PDO::ATTR_STATEMENT_CLASS`**.

Este valor não pode ser usado com
**`PDO::ATTR_DEFAULT_FETCH_MODE`**.

## PDO::FETCH\_ASSOC ([int](language.types.integer.md))

**`PDO::FETCH_ASSOC`** retorna um array indexado apenas pelo nome da
coluna.

```
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users");
$row = $stmt->fetch(\PDO::FETCH_ASSOC);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [userid] => 104
    [name] => Chris
    [country] => Ukraine
)
```

## PDO::FETCH\_BOTH ([int](language.types.integer.md))

Este é o modo de busca padrão.

**`PDO::FETCH_BOTH`** retorna uma matriz indexada tanto pelo número da coluna quanto pelo nome.
Isso significa que cada valor retornado é duplicado para cada
linha de resultado.

O número da coluna começa em 0 e é determinado pela ordem da coluna de resultado na
consulta, não (por exemplo) pela ordem em que as colunas são definidas na tabela.

> **Nota**:
>
> Não é recomendável usar o índice numérico de coluna, pois ele pode mudar quando
> a consulta for alterada ou quando o esquema da tabela for alterado ao usar
> `SELECT *`.

> **Nota**:
>
> O número de entradas indexadas por nome pode não corresponder ao número de entradas
> indexadas por número nos casos em que várias colunas retornadas usam o mesmo
> nome.

```
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users");
$row = $stmt->fetch(\PDO::FETCH_BOTH);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [id] => 104,
    [0] => 104,
    [name] => Chris,
    [1] => Chris,
    [country] => Ukraine,
    [2] => Ukraine
)
```

## PDO::FETCH\_NAMED ([int](language.types.integer.md))

**`PDO::FETCH_NAMED`** retorna resultados no mesmo formato que
**`PDO::FETCH_ASSOC`** exceto que, quando várias colunas usam
o mesmo nome, todos os valores são retornados como uma lista.

Para obter mais informações sobre o tratamento de nomes de colunas duplicados e alternativas,
consulte a seção [tratamento de
nomes duplicados](pdo.constants.fetch-modes.md#pdo.fetch-modes.duplicate-names) acima.

A ordem em que os valores duplicados são retornados deve ser considerada
indefinida. Não há como saber de onde cada valor veio.

```
<?php
$stmt = $pdo->query(
    "SELECT users.*, referrer.name
     FROM users
     LEFT JOIN users AS referrer ON users.referred_by = referrer.userid
     WHERE userid = 109"
);
$row = $stmt->fetch(\PDO::FETCH_NUM);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [userid] => 109
    [name] => Array
        (
            [0] => Toni
            [1] => Chris
        )
    [country] => Germany
    [referred_by] = 104
)
```

## PDO::FETCH\_NUM ([int](language.types.integer.md))

**`PDO::FETCH_NUM`** retorna um array indexado apenas pelo número da coluna.
O número da coluna começa em 0 e é determinado pela ordem da coluna de resultado na
consulta, não (por exemplo) pela ordem em que as colunas são definidas na tabela.

> **Nota**:
>
> Não é recomendável usar o índice de coluna numérica, pois ele pode mudar quando
> a consulta for alterada ou quando o esquema da tabela for alterado ao usar
> `SELECT *`.

```
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users");
$row = $stmt->fetch(\PDO::FETCH_NUM);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [0] => 104
    [1] => Chris
    [2] => Ukraine
)
```

## PDO::FETCH\_COLUMN ([int](language.types.integer.md))

**`PDO::FETCH_COLUMN`** retorna valores de uma única coluna.
Use o segundo argumento de [PDOStatement::setFetchMode()](pdostatement.setfetchmode.md)
ou [PDOStatement::fetchAll()](pdostatement.fetchall.md) para especificar qual coluna será
retornada.

Se a coluna especificada não existir, será lançado um
[ValueError](class.valueerror.md).

```
<?php
$stmt = $pdo->query("SELECT name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_COLUMN);
print_r($row);

$stmt = $pdo->query("SELECT name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_COLUMN, 1);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [0] => Chris
    [1] => Jamie
    [2] => Robin
)

Array
(
    [0] => Ukraine
    [1] => England
    [2] => Germany
)
```

## PDO::FETCH\_KEY\_PAIR ([int](language.types.integer.md))

**`PDO::FETCH_KEY_PAIR`** retorna pares de valores, indexados pela
primeira coluna. Os resultados devem conter apenas 2 colunas. Este modo de busca
só faz sentido com [PDOStatement::fetchAll()](pdostatement.fetchall.md).

> **Nota**:
>
> Se a primeira coluna não for única, valores serão perdidos.
> Quais valores serão perdidos devem ser considerados indefinidos.

```
<?php
$stmt = $pdo->query("SELECT name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_KEY_PAIR);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [Chris] => Ukraine
    [Jamie] => England
    [Robin] => Germany
)
```

## PDO::FETCH\_FUNC ([int](language.types.integer.md))

Especifique uma função para criar o valor retornado. Este modo só pode ser usado
com [PDOStatement::fetchAll()](pdostatement.fetchall.md).

A função recebe os valores como parâmetros.
Não há como recuperar o nome da coluna à qual um determinado valor estava associado.
É crucial garantir que a ordem das colunas na consulta corresponda à
esperada pela função.

> **Nota**:
>
> Os efeitos de **`PDO::FETCH_GROUP`** e
> **`PDO::FETCH_UNIQUE`** são aplicados aos resultados antes da
> função ser chamada.

```
<?php
function valueCreator($col1, $col2, $col3)
{
    return [
        'col1' => $col1,
        'col2' => strtoupper($col2),
        'col3' => $col3,
        'customKey' => 'customValue',
    ];
}

$stmt = $pdo->query("SELECT userid, name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_FUNC, valueCreator(...));
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [0] => Array
        (
            [col1] => 104
            [col2] => SAM
            [col3] => Ukraine
            [customKey] => customValue
        )

    [1] => Array
        (
            [col1] => 105
            [col2] => JAMIE
            [col3] => England
            [customKey] => customValue
        )

    [2] => Array
        (
            [col1] => 107
            [col2] => ROBIN
            [col3] => Germany
            [customKey] => customValue
        )

)
```

## PDO::FETCH\_OBJ ([int](language.types.integer.md))

**`PDO::FETCH_OBJ`** retorna um objeto
[stdClass](class.stdclass.md).

Consulte também [PDOStatement::fetchObject()](pdostatement.fetchobject.md) e
**`PDO::FETCH_CLASS`**.

```
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users");
$row = $stmt->fetch(\PDO::FETCH_OBJ);
print_r($row);
```

O exemplo acima produzirá:

```
stdClass Object
(
    [userid] => 104
    [name] => Chris
    [country] => Ukraine
)
```

## PDO::FETCH\_CLASS ([int](language.types.integer.md))

Retorna um objeto de uma classe especificada. Para comportamentos adicionais, consulte os sinalizadores de opções:
[sinalizadores de opções](pdo.constants.fetch-modes.md#pdo.fetch-modes.class-flags).

Se uma propriedade com o nome de uma coluna retornada não existir, ela será
declarada dinamicamente. Esse comportamento foi descontinuado e causará um erro
a partir do PHP 9.0.

Consulte também [PDOStatement::fetchObject()](pdostatement.fetchobject.md).

```
<?php
class TestEntity
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;

    public function __construct()
    {
        print "Construtor chamado com ". count(func_get_args()) ." argumentos\n";
        print "Propriedades definidas quando o construtor foi chamado? "
            . (isset($this->name) ? 'Sim' : 'Não') . "\n";
    }
}

$stmt = $db->query(
    "SELECT userid, name, country, referred_by_userid FROM users"
);
$stmt->setFetchMode(PDO::FETCH_CLASS, TestEntity::class);
$result = $stmt->fetch();
var_dump($result);
```

O exemplo acima produzirá
algo semelhante a:

```
Construtor chamado com 0 argumentoss
Propriedades definidas quando o construtor foi chamado? Sim
object(TestEntity)#3 (4) {
  ["userid"]=>
  int(104)
  ["name"]=>
  string(5) "Chris"
  ["country"]=>
  string(7) "Ukraine"
  ["referred_by_userid"]=>
  NULL
}
```

## PDO::FETCH\_CLASSTYPE ([int](language.types.integer.md))

Este modo de busca só pode ser usado em combinação com
**`PDO::FETCH_CLASS`** (e
[suas outras opções](pdo.constants.fetch-modes.md#pdo.fetch-modes.class-flags)).

Quando este modo de busca é usado, o PDO usará a primeira coluna retornada como o
nome da classe a ser retornada.

Se a classe especificada não for encontrada, um objeto [stdClass](class.stdclass.md)
será retornado, sem aviso ou erro.

```
<?php
class TestEntity
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;

    public function __construct()
    {
        print "Construtor chamado com ". count(func_get_args()) ." argumentos\n";
        print "Propriedades definidas quando o construtor foi chamado? "
            . (isset($this->name) ? 'Sim' : 'Não') . "\n";
    }
}

$stmt = $db->query(
    "SELECT 'TestEntity', userid, name, country, referred_by_userid FROM users"
);
$stmt->setFetchMode(PDO::FETCH_CLASS | PDO::FETCH_CLASSTYPE);
$result = $stmt->fetch();
var_dump($result);
```

O exemplo acima produzirá
algo semelhante a:

```
Construtor chamado com 0 argumentos
Propriedades definidas quando o construtor foi chamado? Sim
object(TestEntity)#3 (4) {
  ["userid"]=>
  int(104)
  ["name"]=>
  string(5) "Chris"
  ["country"]=>
  string(7) "Ukraine"
  ["referred_by_userid"]=>
  NULL
}
```

## PDO::FETCH\_PROPS\_LATE ([int](language.types.integer.md))

Este modo de busca só pode ser usado em combinação com
**`PDO::FETCH_CLASS`** (e
[suas outras opções](pdo.constants.fetch-modes.md#pdo.fetch-modes.class-flags)).

Quando este modo de busca é usado, o construtor será chamado antes que as
propriedades sejam definidas.

```
<?php
class TestEntity
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;

    public function __construct()
    {
        print "Construtor chamado com ". count(func_get_args()) ." argumentos\n";
        print "Propriedades definidas quando o construtor foi chamado? "
            . (isset($this->name) ? 'Sim' : 'Não') . "\n";
    }
}

$stmt = $db->query(
    "SELECT userid, name, country, referred_by_userid FROM users"
);
$stmt->setFetchMode(PDO::FETCH_CLASS | PDO::FETCH_PROPS_LATE, TestEntity::class);
$result = $stmt->fetch();
var_dump($result);
```

O exemplo acima produzirá
algo semelhante a:

```
Construtor chamado com 0 argumentos
Propriedades definidas quando o construtor foi chamado? Não
object(TestEntity)#3 (4) {
  ["userid"]=>
  int(104)
  ["name"]=>
  string(5) "Chris"
  ["country"]=>
  string(7) "Ukraine"
  ["referred_by_userid"]=>
  NULL
}
```

## PDO::FETCH\_SERIALIZE ([int](language.types.integer.md))

**Aviso**

Este recurso foi
*DESCONTINUADO* a partir do PHP 8.1.0. O uso deste recurso
é fortemente desencorajado.

Este modo de busca só pode ser usado em combinação com
**`PDO::FETCH_CLASS`** (e
[suas outras opções](pdo.constants.fetch-modes.md#pdo.fetch-modes.class-flags)).

Quando este modo de busca é utilizado, a classe especificada deve ser
[Serializable](class.serializable.md).

**Cuidado**

Este recurso não suporta uma string que contenha um objeto serializado completo
(com [serialize()](function.serialize.md)).

**Cuidado**

Este modo de busca não chama o construtor.

```
<?php
class TestEntity implements Serializable
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;

    public function __construct()
    {
        print "Construtor chamado com " . count(func_get_args()) . " argumentos\n";
        print "Propriedades definidas quando o construtor é chamado? "
            . (isset($this->name) ? 'Sim' : 'Não') . "\n";
    }

    public function serialize()
    {
        return join(
            "|",
            [$this->userid, $this->name, $this->country, $this->referred_by_userid]
        );
    }

    public function unserialize(string $data)
    {
        $parts = explode("|", $data);
        $this->userid = (int) $parts[0];
        $this->name = $parts[1];
        $this->country = $parts[2];

        $refId = $parts[3];
        $this->referred_by_userid = ($refId === "" ? null : (int) $refId);
    }
}

print "Definindo o registro (construtor chamado manualmente):\n";
$db->exec(
    "CREATE TABLE serialize (
        sdata TEXT
    )"
);

$origObj = new TestEntity();
$origObj->userid = 200;
$origObj->name = 'Seri';
$origObj->country = 'Syria';
$origObj->referred_by_userid = null;

$insert = $db->prepare("INSERT INTO serialize (sdata) VALUES (:sdata)");
$insert->execute(['sdata' => $origObj->serialize()]);

print "\nRecuperando o resultado:\n";
$query = "SELECT sdata FROM serialize";
$stmt = $db->query($query);
// NOTA: O construtor nunca é chamado!
$stmt->setFetchMode(PDO::FETCH_CLASS | PDO::FETCH_SERIALIZE, TestEntity::class);
$result = $stmt->fetch();
var_dump($result);
```

O exemplo acima produzirá
algo semelhante a:

```
Deprecated: TestEntity implements the Serializable interface, which is deprecated. Implement __serialize() and __unserialize() instead (or in addition, if support for old PHP versions is necessary) in Standard input code on line 2
Definindo o registro (construtor chamado manualmente):
Construtor chamado com 0 argumentos
Propriedades definidas quando o construtor é chamado? Não

Recuperando o resultado:
Deprecated: PDOStatement::setFetchMode(): The PDO::FETCH_SERIALIZE mode is deprecated in Standard input code on line 58

Deprecated: PDOStatement::fetch(): The PDO::FETCH_SERIALIZE mode is deprecated in Standard input code on line 59
object(TestEntity)#5 (4) {
  ["userid"]=>
  int(200)
  ["name"]=>
  string(4) "Seri"
  ["country"]=>
  string(5) "Syria"
  ["referred_by_userid"]=>
  NULL
}
```

## PDO::FETCH\_BOUND ([int](language.types.integer.md))

Este modo de busca não pode ser usado com
[PDOStatement::fetchAll()](pdostatement.fetchall.md).

Este modo de busca não retorna um resultado diretamente, mas associa valores a
variáveis ​​especificadas com [PDOStatement::bindColumn()](pdostatement.bindcolumn.md). O
método de busca chamado retorna **`true`**.

> **Nota**:
>
> Ao usar instruções preparadas, para funcionar corretamente, as variáveis ​​devem ser vinculadas
> após a execução da consulta.

```
<?php
$query = "SELECT users.userid, users.name, users.country, referrer.name
    FROM users
    LEFT JOIN users AS referrer ON users.referred_by_userid = referrer.userid";
$stmt = $db->prepare($query);
$stmt->execute();

$stmt->bindColumn('userid', $userId);
$stmt->bindColumn('name', $name);
$stmt->bindColumn('country', $country);
// Vincule pela posição da coluna para resolver nomes de coluna duplicados
// Para evitar que isso cause problemas se a consulta for alterada, use um sinônimo SQL.
// Por exemplo: referrer.name AS referrer_name
$stmt->bindColumn(4, $referrerName);

while ($stmt->fetch(\PDO::FETCH_BOUND)) {
    print join("\t", [$userId, $name, $country, ($referrerName ?? 'NULL')]) . "\n";
}
```

O exemplo acima produzirá:

```
104	Chris	Ukraine	NULL
105	Jamie	England	NULL
107	Robin	Germany	Chris
108	Sean	Ukraine	NULL
109	Toni	Germany	NULL
110	Toni	Germany	NULL
```

## PDO::FETCH\_INTO ([int](language.types.integer.md))

Este modo de busca não pode ser usado com
[PDOStatement::fetchAll()](pdostatement.fetchall.md).

Este modo de busca atualiza as propriedades do objeto especificado. O objeto é
retornado em caso de sucesso.

Se uma propriedade com o nome de uma coluna retornada não existir, ela será
declarada dinamicamente. Esse comportamento está obsoleto e causará um erro
a partir do PHP 9.0.

Propriedades precisam ser `public` e não podem ser
`readonly`.

**Cuidado**

Não há como alterar o objeto a ser atualizado sem usar
[PDOStatement::setFetchMode()](pdostatement.setfetchmode.md) entre a recuperação de cada
registro.

```
<?php

class TestEntity
{
    public $userid;

    public $name;

    public $country;

    public $referred_by_userid;
}

$obj = new TestEntity();

$stmt = $db->query("SELECT userid, name, country, referred_by_userid FROM users");

$stmt->setFetchMode(\PDO::FETCH_INTO, $obj);
$result = $stmt->fetch();

var_dump($result);
```

O exemplo acima produzirá
algo semelhante a:

```
object(TestEntity)#3 (4) {
  ["userid"]=>
  int(104)
  ["name"]=>
  string(5) "Chris"
  ["country"]=>
  string(7) "Ukraine"
  ["referred_by_userid"]=>
  NULL
}
```

## PDO::FETCH\_LAZY ([int](language.types.integer.md))

Este modo de busca não pode ser usado com
[PDOStatement::fetchAll()](pdostatement.fetchall.md).

Este modo de busca retorna um objeto [PDORow](class.pdorow.md) que fornece
acesso a valores tanto no formato de array quanto no formato de objeto (ou seja, combina o comportamento de
**`PDO::FETCH_BOTH`** e
**`PDO::FETCH_OBJ`**), recuperados de forma lenta.

Isso pode fornecer acesso eficiente em termos de memória (no lado do PHP) a resultados não armazenados em buffer
no servidor de banco de dados. Se o PDO usa buffer no lado do cliente para resultados
depende do driver específico do banco de dados usado (e de sua configuração).

**Cuidado**

[PDORow](class.pdorow.md) retornará **`null`** sem
qualquer erro ou aviso ao acessar propriedades ou chaves que não estejam definidas.
Isso pode dificultar a detecção e depuração de erros como erros de digitação ou consultas
que não retornam os dados esperados.

**Cuidado**

O objeto [PDORow](class.pdorow.md) retornado é atualizado cada vez que um
resultado é recuperado.

```
<?php
$stmt = $db->query("SELECT userid, name, country, referred_by_userid FROM users");
$result = $stmt->fetch(\PDO::FETCH_LAZY);

print "ID: ". $result[0] ."\n";
print "Nome: {$result->name}\n";
print "País: " . $result['country'] ."\n";
// Retorna NULL. Nenhum aviso ou erro é emitido.
print "Não existe: " . var_export($result->does_not_exist, true) . "\n";

$differentResult = $stmt->fetch(\PDO::FETCH_LAZY);
// O PDORow recuperado anteriormente agora aponta para o resultado recém-recuperado.
print "ID: ". $result[0] ."\n";
```

O exemplo acima produzirá:

```
ID: 104
Nome: Chris
País: Ukraine
Não existe: NULL
ID: 105
```

## PDO::FETCH\_GROUP ([int](language.types.integer.md))

**`PDO::FETCH_GROUP`** retorna listas de arrays associativos,
indexados por uma coluna (não única). Este modo de busca funciona apenas com
[PDOStatement::fetchAll()](pdostatement.fetchall.md).

Quando combinado com **`PDO::FETCH_UNIQUE`**, ambos os modos
usarão a mesma coluna, tornando a combinação desses modos inútil.

Esta busca deve ser combinada com uma das seguintes constantes:
**`PDO::FETCH_ASSOC`**, **`PDO::FETCH_BOTH`**,
**`PDO::FETCH_NAMED`**, **`PDO::FETCH_NUM`**,
**`PDO::FETCH_COLUMN`** ou
**`PDO::FETCH_FUNC`**.

Se nenhum modo de busca da lista acima for fornecido, o modo de busca padrão atual
para o [PDOStatement](class.pdostatement.md) será usado.

```
<?php
$stmt = $pdo->query("SELECT country, userid, name FROM users");
$row = $stmt->fetchAll(\PDO::FETCH_GROUP | \PDO::FETCH_ASSOC);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [Ukraine] => Array
        (
            [0] => Array
                (
                    [userid] => 104
                    [name] => Chris
                )

            [1] => Array
                (
                    [userid] => 108
                    [name] => Sean
                )

        )
    [England] => Array
        (
            [0] => Array
                (
                    [userid] => 105
                    [name] => Jamie
                )

        )

    [Germany] => Array
        (
            [0] => Array
                (
                    [userid] => 107
                    [name] => Robin
                )

            [1] => Array
                (
                    [userid] => 109
                    [name] => Toni
                )
        )
)
```

No exemplo acima, pode ser observado que a primeira coluna é omitida do
array de cada linha, estando disponível apenas como chave. Ela pode ser incluída
repetindo a coluna, como no exemplo a seguir:

```
<?php
$stmt = $pdo->query("SELECT country, userid, name, country FROM users");
$row = $stmt->fetchAll(\PDO::FETCH_GROUP | \PDO::FETCH_ASSOC);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [Ukraine] => Array
        (
            [0] => Array
                (
                    [userid] => 104
                    [name] => Chris
                    [country] => Ukraine
                )

            [1] => Array
                (
                    [userid] => 108
                    [name] => Sean
                    [country] => Ukraine
                )

        )
    [England] => Array
        (
            [0] => Array
                (
                    [userid] => 105
                    [name] => Jamie
                    [country] => England
                )

        )

    [Germany] => Array
        (
            [0] => Array
                (
                    [userid] => 107
                    [name] => Robin
                    [country] => Germany
                )

            [1] => Array
                (
                    [userid] => 109
                    [name] => Toni
                    [country] => Germany
                )
        )
)
```

## PDO::FETCH\_UNIQUE ([int](language.types.integer.md))

**`PDO::FETCH_UNIQUE`** usa a primeira coluna para indexar registros,
retornando 1 registro por valor de índice. Este modo de busca funciona apenas com
[PDOStatement::fetchAll()](pdostatement.fetchall.md).

Quando combinado com **`PDO::FETCH_GROUP`**, ambos os modos usarão
a mesma coluna, tornando a combinação desses modos inútil.

Esta busca deve ser combinada com uma das seguintes constantes
**`PDO::FETCH_ASSOC`**, **`PDO::FETCH_BOTH`**,
**`PDO::FETCH_NAMED`**, **`PDO::FETCH_NUM`**,
**`PDO::FETCH_COLUMN`** ou
**`PDO::FETCH_FUNC`**.

Se nenhum modo de busca da lista acima for fornecido, o modo de busca padrão atual
para o [PDOStatement](class.pdostatement.md) será usado.

Quando usado com uma coluna que se sabe ser única (como o ID do registro), este
modo oferece a capacidade de retornar rapidamente resultados indexados por esse valor.

> **Nota**:
>
> Se a primeira coluna não for única, valores serão perdidos.
> Quais valores serão perdidos devem ser considerados indefinidos.

**Cuidado**

A filtragem de registros deve ser feita em SQL sempre que possível.
O banco de dados usará índices para otimizar esse processo e retornar apenas os registros necessários.
Selecionar mais registros do que o necessário do banco de dados pode aumentar significativamente o
uso de memória e o tempo de consulta para conjuntos de resultados maiores.

```
<?php
$stmt = $pdo->query("SELECT userid, name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_UNIQUE | \PDO::FETCH_ASSOC);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [104] => Array
        (
            [name] => Chris
            [country] => Ukraine
        )

    [105] => Array
        (
            [name] => Jamie
            [country] => England
        )

    [107] => Array
        (
            [name] => Robin
            [country] => Germany
        )

)
```

No exemplo acima, pode ser observado que a primeira coluna é omitida do
array de cada linha, estando disponível apenas como chave. Ela pode ser incluída
repetindo a coluna, como no exemplo a seguir:

```
<?php
$stmt = $pdo->query("SELECT userid, userid, name, country FROM users LIMIT 3");
$row = $stmt->fetchAll(\PDO::FETCH_UNIQUE | \PDO::FETCH_ASSOC);
print_r($row);
```

O exemplo acima produzirá:

```
Array
(
    [104] => Array
        (
            [userid] => 104
            [name] => Chris
            [country] => Ukraine
        )

    [105] => Array
        (
            [userid] => 105
            [name] => Jamie
            [country] => England
        )

    [107] => Array
        (
            [userid] => 107
            [name] => Robin
            [country] => Germany
        )

)
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
