# Retorna metadados para uma coluna no resultado

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.getcolumnmeta.php

---

# PDOStatement::getColumnMeta

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.2.0)

PDOStatement::getColumnMeta — 
Retorna metadados para uma coluna no resultado

### Descrição

public function **PDOStatement::getColumnMeta**([int](language.types.integer.md) `$column`): [array](language.types.array.md)|[false](language.types.singleton.md)

Retorna metadados para uma coluna no resultado, indexada a partir de 0, como um
array associativo.

**Aviso**

Alguns drivers podem não implementar o método
**PDOStatement::getColumnMeta()**,
já que ele é opcional. Entretanto, todos os
[drivers PDO](pdo.drivers.md)
documentados neste manual implementam este método.

### Parâmetros

`column`
:   A coluna no resultado, indexada a partir de 0.

### Valor Retornado

Retorna um array associativo contendo os seguintes valores que representam
os metadados para uma única coluna:

**Metadados de coluna**

| Nome | Valor |
| --- | --- |
| `native_type` | O tipo de dados nativo do PHP usado para representar o valor da coluna. |
| `driver:decl_type` | O tipo de dados SQL usado para representar o valor da coluna no banco de dados. Se a coluna for resultado de uma função, este valor não será retornado por **PDOStatement::getColumnMeta()**. |
| `flags` | Quaisquer opções configuradas para esta coluna. |
| `name` | O nome desta coluna como retornado pelo banco de dados. |
| `table` | O nome da tabela desta coluna como retornado pelo banco de dados. |
| `len` | O comprimento desta coluna. Normalmente `-1` para tipos que não sejam números com decimais. |
| `precision` | A precisão numérica desta coluna. Normalmente `0` para tipos que não sejam números decimais. |
| `pdo_type` | O tipo desta coluna como representado pelas [constantes `PDO::PARAM_*`](pdo.constants.md). |

Retorna **`false`** se a coluna requisitada não existir no resultado
ou se não existir resultado.

### Examples

**Exemplo #1 Recuperando metadados de coluna**

O exemplo a seguir mostra o resultado da recuperação de metadados para uma
única coluna gerada por uma função (COUNT) em um driver PDO\_SQLITE.

```
<?php
$select = $DB->query('SELECT COUNT(*) FROM fruit');
$meta = $select->getColumnMeta(0);
var_dump($meta);
?>
```

O exemplo acima produzirá:

```
array(6) {
  ["native_type"]=>
  string(7) "integer"
  ["flags"]=>
  array(0) {
  }
  ["name"]=>
  string(8) "COUNT(*)"
  ["len"]=>
  int(-1)
  ["precision"]=>
  int(0)
  ["pdo_type"]=>
  int(2)
}
```

### Veja também

- [PDOStatement::columnCount()](pdostatement.columncount.md) - Retorna o número de colunas no conjunto de resultados
- [PDOStatement::rowCount()](pdostatement.rowcount.md) - Retorna o número de registros afetados pela última instrução SQL

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
