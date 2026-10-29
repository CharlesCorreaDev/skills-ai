# Objetos Grandes (LOBs)

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.lobs.php

---

# Objetos Grandes (LOBs)

Em algum momento da aplicação, pode ser necessário armazenar
dados "grandes" em seu banco de dados. Grande geralmente significa "cerca de 4kb ou
mais", embora alguns bancos de dados possam lidar facilmente com até 32kb antes que os dados se tornem
"grandes". Objetos grandes podem ser de natureza textual ou binária. O PDO
permite que se trabalhe com esse tipo de dado grande usando o
código de tipo **`PDO::PARAM_LOB`**
nas chamadas a [PDOStatement::bindParam()](pdostatement.bindparam.md) ou
[PDOStatement::bindColumn()](pdostatement.bindcolumn.md).
**`PDO::PARAM_LOB`** diz
ao PDO para mapear os dados como um fluxo, para que seja possível manipulá-los usando a
[API de Fluxos do PHP](ref.stream.md).

**Exemplo #1 Exibindo uma imagem de um banco de dados**

Este exemplo vincula o LOB à variável chamada $lob e depois o envia
para o navegador usando [fpassthru()](function.fpassthru.md). Como o LOB
é representado como um fluxo, funções como
[fgets()](function.fgets.md), [fread()](function.fread.md) e
[stream\_get\_contents()](function.stream-get-contents.md) podem ser usadas nele.

```
<?php
$db = new PDO('odbc:SAMPLE', 'db2inst1', 'ibmdb2');
$stmt = $db->prepare("select contenttype, imagedata from images where id=?");
$stmt->execute(array($_GET['id']));
$stmt->bindColumn(1, $type, PDO::PARAM_STR, 256);
$stmt->bindColumn(2, $lob, PDO::PARAM_LOB);
$stmt->fetch(PDO::FETCH_BOUND);

header("Content-Type: $type");
fpassthru($lob);
?>
```

**Exemplo #2 Inserindo uma imagem em um banco de dados**

Este exemplo abre um arquivo e passa o identificador do arquivo para o PDO para inserir
como um LOB. O PDO fará o melhor possível para obter o conteúdo do arquivo até
o banco de dados da maneira mais eficiente possível.

```
<?php
$db = new PDO('odbc:SAMPLE', 'db2inst1', 'ibmdb2');
$stmt = $db->prepare("insert into images (id, contenttype, imagedata) values (?, ?, ?)");
$id = get_new_id(); // uma função para alocar um novo ID

// suponha que estamos executando como parte de um formulário de upload de arquivo
// Mais informações podem ser encontradas na documentação do PHP

$fp = fopen($_FILES['file']['tmp_name'], 'rb');

$stmt->bindParam(1, $id);
$stmt->bindParam(2, $_FILES['file']['type']);
$stmt->bindParam(3, $fp, PDO::PARAM_LOB);

$db->beginTransaction();
$stmt->execute();
$db->commit();
?>
```

**Exemplo #3 Inserindo uma imagem em um banco de dados: Oracle**

O Oracle requer uma sintaxe ligeiramente diferente para inserir um lob de um
arquivo. Também é essencial que você execute a inserção sob um
transação, caso contrário, seu LOB recém-inserido será comprometido com um
comprimento zero como parte do commit implícito que ocorre quando a consulta
é executada:

```
<?php
$db = new PDO('oci:', 'scott', 'tiger');
$stmt = $db->prepare("insert into images (id, contenttype, imagedata) " .
"VALUES (?, ?, EMPTY_BLOB()) RETURNING imagedata INTO ?");
$id = get_new_id(); // uma função para alocar um novo ID

// suponha que estamos executando como parte de um formulário de upload de arquivo
// Mais informações podem ser encontradas na documentação do PHP

$fp = fopen($_FILES['file']['tmp_name'], 'rb');

$stmt->bindParam(1, $id);
$stmt->bindParam(2, $_FILES['file']['type']);
$stmt->bindParam(3, $fp, PDO::PARAM_LOB);

$db->beginTransaction();
$stmt->execute();
$db->commit();
?>
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
