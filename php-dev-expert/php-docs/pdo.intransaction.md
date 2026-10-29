# Verifica se está dentro de uma transação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.intransaction.php

---

# PDO::inTransaction

(PHP 5 >= 5.3.3, Bundled pdo\_pgsql, PHP 7, PHP 8)

PDO::inTransaction — 
Verifica se está dentro de uma transação

### Descrição

public function **PDO::inTransaction**(): [bool](language.types.boolean.md)

Verifica se uma transação está atualmente ativa no driver. Este método
funciona somente para drivers de banco de dados que suportam transações.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** se uma transação estiver ativa, e **`false`** caso contrário.

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
