# Declara um token com associatividade à direita

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.right.php

---

# Parle\Parser::right

(PECL parle >= 0.5.1)

Parle\Parser::right — Declara um token com associatividade à direita

### Descrição

public function **Parle\Parser::right**([string](language.types.string.md) `$tok`): [void](language.types.void.md)

Declara um terminal com associatividade à direita.

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
