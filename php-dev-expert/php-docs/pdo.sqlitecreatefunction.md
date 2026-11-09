# Sinônimo de Pdo\Sqlite::createFunction

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.sqlitecreatefunction.php

---

# PDO::sqliteCreateFunction

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo\_sqlite >= 1.0.0)

PDO::sqliteCreateFunction — 
Sinônimo de [Pdo\Sqlite::createFunction()](pdo-sqlite.createfunction.md)

**Aviso**

Esta função foi
*DESCONTINUADA* a partir do PHP 8.5.0. O uso desta função
é fortemente desencorajado.

### Descrição

public function **PDO::sqliteCreateFunction**(  
    [string](language.types.string.md) `$function_name`,  
    [callable](language.types.callable.md) `$callback`,  
    [int](language.types.integer.md) `$num_args` = -1,  
    [int](language.types.integer.md) `$flags` = 0  
): [bool](language.types.boolean.md)

Este método é um apelido para: [Pdo\Sqlite::createFunction()](pdo-sqlite.createfunction.md).

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 7.1.4 | O parâmetro `flags` foi adicionado. |

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
