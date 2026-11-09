# Define um retorno de chamada para lidar com mensagens de alerta e de aviso geradas pelo back-end

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.setnoticecallback.php

---

# Pdo\Pgsql::setNoticeCallback

(PHP 8 >= 8.4.0)

Pdo\Pgsql::setNoticeCallback — Define um retorno de chamada para lidar com mensagens de alerta e de aviso geradas pelo back-end

### Descrição

public function **Pdo\Pgsql::setNoticeCallback**([?](language.types.null.md)[callable](language.types.callable.md) `$callback`): [void](language.types.void.md)

Define um retorno de chamada para lidar com mensagens de aviso e aviso geradas pelo back-end.
Isto inclui mensagens emitidas pelo próprio PostgreSQL,
bem como aquelas geradas por funções SQL definidas pelo usuário usando `RAISE`.
Observe que o recebimento real dessas mensagens
depende da configuração de backend `client_min_messages`.

### Parâmetros

`callback`
:   Se **`null`** for passado, o manipulador será redefinido para seu estado padrão.

    Caso contrário, o manipulador será um retorno de chamada com a seguinte assinatura:

    function handler([string](language.types.string.md) `$message`): [void](language.types.void.md)

    `message`
    :   Uma mensagem gerada pelo backend.

### Valor Retornado

Nenhum valor é retornado.

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::setNoticeCallback()****

```
<?php
$pdo = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);

$pdo->exec('CREATE TABLE parent(id int primary key)');
$pdo->exec('CREATE TABLE child(id int references parent)');

$pdo->setNoticeCallback(function ($message) {
    echo $message;
});

$pdo->exec('TRUNCATE parent CASCADE');
?>
```

O exemplo acima produzirá
algo semelhante a:

```
NOTICE:  truncate cascades to table "child"
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
