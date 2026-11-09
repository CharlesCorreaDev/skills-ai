# Copia dados da tabela para arquivo

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.copytofile.php

---

# Pdo\Pgsql::copyToFile

(PHP 8 >= 8.4.0)

Pdo\Pgsql::copyToFile — Copia dados da tabela para arquivo

### Descrição

public function **Pdo\Pgsql::copyToFile**(  
    [string](language.types.string.md) `$tableName`,  
    [string](language.types.string.md) `$filename`,  
    [string](language.types.string.md) `$separator` = "\t",  
    [string](language.types.string.md) `$nullAs` = "\\\\N",  
    [?](language.types.null.md)[string](language.types.string.md) `$fields` = **`null`**  
): [bool](language.types.boolean.md)

Copia dados da tabela para o arquivo especificado por `filename`
usando `separator` como delimitador de campos
e lista de campos no parâmetro `fields`.

### Parâmetros

`tableName`
:   String contendo o nome da tabela.

`filename`
:   Nome do arquivo para exportar dados.

`separator`
:   Delimitador usado para separar campos em uma entrada do
    array `rows`.

`nullAs`
:   Como interpretar valores SQL `NULL`.

`fields`
:   Lista de campos a serem exportados.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

Se `filename` não puder ser aberto para escrita ou não puder
ser gravado, a falha é reportada através da manipulação do erro de conexão
(consulte **`PDO::ATTR_ERRMODE`**); com
**`PDO::ERRMODE_EXCEPTION`** uma
[PDOException](class.pdoexception.md) é lançada.

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::copyToFile()****

A tabela é gravada em `filename`, um registro por
linha com os campos conectados por `separator`.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->exec('CREATE TABLE fruits (id int, name text, qty int)');
$db->exec("INSERT INTO fruits VALUES (1, 'apple', 10), (2, 'banana', 20)");

$db->copyToFile('fruits', '/tmp/fruits.tsv');
echo file_get_contents('/tmp/fruits.tsv');
?>
```

O exemplo acima produzirá:

```
1	apple	10
2	banana	20
```

### Veja também

- [Pdo\Pgsql::copyFromFile()](pdo-pgsql.copyfromfile.md) - Copia dados do arquivo para a tabela
- [Pdo\Pgsql::copyFromArray()](pdo-pgsql.copyfromarray.md) - Copia dados de um array PHP para uma tabela
- [Pdo\Pgsql::copyToArray()](pdo-pgsql.copytoarray.md) - Copia dados da tabela do banco de dados para o array PHP

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
