# Avança para o próximo conjunto de registros em um identificados de instrução com múltiplos conjuntos de registros

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.nextrowset.php

---

# PDOStatement::nextRowset

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.2.0)

PDOStatement::nextRowset — 
Avança para o próximo conjunto de registros em um identificados de instrução com múltiplos conjuntos de registros

### Descrição

public function **PDOStatement::nextRowset**(): [bool](language.types.boolean.md)

Alguns servidores de bancos de dados suportam procedimentos armazenados que retornam mais de um
conjunto de registros (também conhecido como conjunto de resultados).
**PDOStatement::nextRowset()** habilita o acesso ao
segundo conjunto de registros, e subsequentes, associados com um objeto PDOStatement. Cada
conjunto de registros pode ter um conjunto diferente de colunas em relação ao conjunto anterior.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Examples

**Exemplo #1 Buscando múltiplos conjuntos de registros de um procedimento armazenado**

O exemplo a seguir mostra como chamar um procedimento armazenado,
`MULTIPLE_ROWSETS`, que retorna três conjuntos de registros. É usado um laço
[do-while](control-structures.do.while.md) para
chamar o método **PDOStatement::nextRowset()** até que ele
retorne **`false`** e termine o laço quando não houver mais conjuntos de registros disponíveis.

```
<?php
$sql = 'CALL multiple_rowsets()';
$stmt = $conn->query($sql);
$i = 1;
do {
    $rowset = $stmt->fetchAll(PDO::FETCH_NUM);
    if ($rowset) {
        printResultSet($rowset, $i);
    }
    $i++;
} while ($stmt->nextRowset());

function printResultSet(&$rowset, $i) {
    print "Conjunto de resultados $i:\n";
    foreach ($rowset as $row) {
        foreach ($row as $col) {
            print $col . "\t";
        }
        print "\n";
    }
    print "\n";
}
?>
```

O exemplo acima produzirá:

```
Conjunto de resultados 1:
apple    red
banana   yellow

Conjunto de resultados 2:
orange   orange    150
banana   yellow    175

Conjunto de resultados 3:
lime     green
apple    red
banana   yellow
```

### Veja também

- [PDOStatement::columnCount()](pdostatement.columncount.md) - Retorna o número de colunas no conjunto de resultados
- [PDOStatement::execute()](pdostatement.execute.md) - Executa ums instrução preparada
- [PDOStatement::getColumnMeta()](pdostatement.getcolumnmeta.md) - Retorna metadados para uma coluna no resultado
- [PDO::query()](pdo.query.md) - Prepara e executa uma instrução SQL sem marcadores

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
