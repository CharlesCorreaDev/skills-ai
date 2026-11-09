# Declara um token

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.token.php

---

# Parle\RParser::token

(PECL parle >= 0.7.0)

Parle\RParser::token — Declara um token

### Descrição

public function **Parle\RParser::token**([string](language.types.string.md) `$tok`): [void](language.types.void.md)

Declara um terminal a ser usado na gramática.

### Parâmetros

`tok`
:   Nome do token.

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
