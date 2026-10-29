# Exclui o objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.lobunlink.php

---

# Pdo\Pgsql::lobUnlink

(PHP 8 >= 8.4.0)

Pdo\Pgsql::lobUnlink — Exclui o objeto grande

### Descrição

public function **Pdo\Pgsql::lobUnlink**([string](language.types.string.md) `$oid`): [bool](language.types.boolean.md)

Exclui um objeto grande do banco de dados identificado pelo OID.

> **Nota**:
>
> Esta função e todas as manipulações de objeto grande
> devem ser chamadas e executadas dentro de uma transação.

### Parâmetros

`oid`
:   Um identificador de objeto grande.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::lobUnlink()****

Este exemplo desvincula um objeto grande do banco de dados antes de excluir
a linha que o referencia. Ele usa a tabela de blobs dos exemplos de
[Pdo\Pgsql::lobCreate()](pdo-pgsql.lobcreate.md) e
[Pdo\Pgsql::lobOpen()](pdo-pgsql.lobopen.md).

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->beginTransaction();
$db->lobUnlink($oid);
$stmt = $db->prepare("DELETE FROM BLOBS where ident = ?");
$stmt->execute([$some_id]);
$db->commit();
?>
```

### Veja também

- [Pdo\Pgsql::lobCreate()](pdo-pgsql.lobcreate.md) - Cria um novo objeto grande
- [Pdo\Pgsql::lobOpen()](pdo-pgsql.lobopen.md) - Abre um fluxo de objetos grandes existente
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
