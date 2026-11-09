# Obtém o PID do processo subjacente que trata esta conexão

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.getpid.php

---

# Pdo\Pgsql::getPid

(PHP 8 >= 8.4.0)

Pdo\Pgsql::getPid — Obtém o PID do processo subjacente que trata esta conexão

### Descrição

public function **Pdo\Pgsql::getPid**(): [int](language.types.integer.md)

Retorna o PID do processo subjacente que trata esta conexão.
Observe que o PID pertence a um processo em execução no
host do servidor de banco de dados, não no host local.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o PID como um [int](language.types.integer.md).

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::getPid()****

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
echo $db->getPid();
?>
```

O exemplo acima produzirá
algo semelhante a:

```
12345
```

### Veja também

- [pg\_get\_pid()](function.pg-get-pid.md) - Obtém o ID do processo do backend

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
