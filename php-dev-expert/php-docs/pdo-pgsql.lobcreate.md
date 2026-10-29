# Cria um novo objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.lobcreate.php

---

# Pdo\Pgsql::lobCreate

(PHP 8 >= 8.4.0)

Pdo\Pgsql::lobCreate — Cria um novo objeto grande

### Descrição

public function **Pdo\Pgsql::lobCreate**(): [string](language.types.string.md)|[false](language.types.singleton.md)

**Pdo\Pgsql::lobCreate()** cria um objeto grande
e retorna o OID que se refere a ele.
Ele pode ser aberto para ler ou gravar dados
com [Pdo\Pgsql::lobOpen()](pdo-pgsql.lobopen.md).

O OID pode ser armazenado em colunas do tipo OID e usado para fazer referência
ao objeto grande, sem fazer com que a linha cresça arbitrariamente.
O objeto grande continuará no banco de dados até ser removido
chamando [Pdo\Pgsql::lobUnlink()](pdo-pgsql.lobunlink.md).

Objetos grandes são complicados de usar.
Na verdade, é necessário que [Pdo\Pgsql::lobUnlink()](pdo-pgsql.lobunlink.md)
seja chamado antes de excluir a última linha que faz referência ao OID em todo o banco de dados;
caso contrário, objetos grandes não referenciados permanecerão no servidor indefinidamente.
Além disso, objetos grandes não possuem controles de acesso.
Uma alternativa é o tipo de coluna bytea, que pode ter até 1 GB de tamanho,
e esse tipo de coluna gerencia de forma transparente o armazenamento para obter o tamanho de linha ideal.

> **Nota**:
>
> Esta função e todas as manipulações de objeto grande
> devem ser chamadas e executadas dentro de uma transação.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o OID do objeto grande recém-criado em caso de sucesso,
ou **`false`** em caso de falha.

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::lobCreate()****

Este exemplo cria um novo objeto grande e copia nele o
conteúdo de um arquivo.
O OID é então armazenado em uma tabela.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->beginTransaction();
$oid = $db->lobCreate();
$stream = $db->lobOpen($oid, 'w');
$local = fopen($filename, 'rb');
stream_copy_to_stream($local, $stream);
$local = null;
$stream = null;
$stmt = $db->prepare("INSERT INTO BLOBS (ident, oid) VALUES (?, ?)");
$stmt->execute([$some_id, $oid]);
$db->commit();
?>
```

### Veja também

- [Pdo\Pgsql::lobOpen()](pdo-pgsql.lobopen.md) - Abre um fluxo de objetos grandes existente
- [Pdo\Pgsql::lobUnlink()](pdo-pgsql.lobunlink.md) - Exclui o objeto grande
- [pg\_lo\_create()](function.pg-lo-create.md) - Cria um objeto grande
- [pg\_lo\_open()](function.pg-lo-open.md) - Abra um objeto grande

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
