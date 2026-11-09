# Sinônimo de Pdo\Pgsql::copyFromArray

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.pgsqlcopyfromarray.php

---

# PDO::pgsqlCopyFromArray

(PHP 5 >= 5.3.3, PHP 7, PHP 8)

PDO::pgsqlCopyFromArray — 
Sinônimo de [Pdo\Pgsql::copyFromArray()](pdo-pgsql.copyfromarray.md)

**Aviso**

Esta função foi
*DESCONTINUADA* a partir do PHP 8.5.0. O uso desta função
é fortemente desencorajado.

### Descrição

#[[\Deprecated](class.deprecated.md)]  
public function **PDO::pgsqlCopyFromArray**(  
    [string](language.types.string.md) `$tableName`,  
    [array](language.types.array.md)|[Traversable](class.traversable.md) `$rows`,  
    [string](language.types.string.md) `$separator` = "\t",  
    [string](language.types.string.md) `$nullAs` = "\\\\N",  
    [?](language.types.null.md)[string](language.types.string.md) `$fields` = [null](reserved.constants.md#constant.null)  
): [bool](language.types.boolean.md)

Este método é um apelido para: [Pdo\Pgsql::copyFromArray()](pdo-pgsql.copyfromarray.md).

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.5.0 | O parâmetro `rows` agora aceita um [Traversable](class.traversable.md); anteriormente somente um [array](language.types.array.md) era aceito. |

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
