# Informa se o phar foi modificado

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.getmodified.php

---

# Phar::getModified

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::getModified — Informa se o phar foi modificado

### Descrição

public function **Phar::getModified**(): [bool](language.types.boolean.md)

Este método pode ser usado para determinar se um phar teve
um arquivo interno excluído ou o conteúdo de um arquivo alterado de
alguma forma.

### Parâmetros

Sem parâmetros.

### Valor Retornado

**`true`** se o phar foi modificado desde que foi aberto, **`false`** caso contrário.

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
