# Insere macro de expressão regular

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-lexer.insertmacro.php

---

# Parle\Lexer::insertMacro

(PECL parle >= 0.5.1)

Parle\Lexer::insertMacro — Insere macro de expressão regular

### Descrição

public function **Parle\Lexer::insertMacro**([string](language.types.string.md) `$name`, [string](language.types.string.md) `$regex`): [void](language.types.void.md)

Insere uma macro de expressão regular, que pode ser usada posteriormente como um atalho e incluída em outras expressões regulares.

### Parâmetros

`name`
:   Nome das macros.

`regex`
:   Expressão regular.

### Valor Retornado

Nenhum valor é retornado.

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
