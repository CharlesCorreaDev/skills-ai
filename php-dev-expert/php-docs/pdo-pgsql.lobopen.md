# Abre um fluxo de objetos grandes existente

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.lobopen.php

---

# Pdo\Pgsql::lobOpen

(PHP 8 >= 8.4.0)

Pdo\Pgsql::lobOpen — Abre um fluxo de objetos grandes existente

### Descrição

public function **Pdo\Pgsql::lobOpen**([string](language.types.string.md) `$oid`, [string](language.types.string.md) `$mode` = "rb"): [resource](language.types.resource.md)|[false](language.types.singleton.md)

**Pdo\Pgsql::lobOpen()** abre um fluxo para acessar
os dados referenciados por `oid`.
Todas as funções usuais do sistema de arquivos, como [fread()](function.fread.md),
[fwrite()](function.fwrite.md) ou [fgets()](function.fgets.md) podem ser usadas
para manipular o conteúdo do fluxo.

> **Nota**:
>
> Esta função e todas as manipulações de objeto grande
> devem ser chamadas e executadas dentro de uma transação.

### Parâmetros

`oid`
:   Um identificador de objeto grande.

`mode`
:   O modo de acesso. Se `mode` contiver
    `w` ou `+`, o fluxo é aberto para
    leitura e escrita; caso contrário é aberto somente-leitura. Um sinalizador
    `b` (binário) não tem efeito. O padrão
    `"rb"` abre o fluxo para leitura.

### Valor Retornado

Retorna um recurso de fluxo em caso de sucesso, ou **`false`** em caso de falha.

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::lobOpen()****

Seguindo o exemplo de [Pdo\Pgsql::lobCreate()](pdo-pgsql.lobcreate.md),
este trecho de código recupera o objeto grande do
banco de dados e o envia para o navegador.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$db->beginTransaction();
$stmt = $db->prepare("SELECT oid FROM BLOBS WHERE ident = ?");
$stmt->execute([$some_id]);
$stmt->bindColumn('oid', $oid, PDO::PARAM_STR);
$stmt->fetch(PDO::FETCH_BOUND);
$stream = $db->lobOpen($oid, 'r');
header("Content-type: application/octet-stream");
fpassthru($stream);
?>
```

### Veja também

- [Pdo\Pgsql::lobCreate()](pdo-pgsql.lobcreate.md) - Cria um novo objeto grande
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
