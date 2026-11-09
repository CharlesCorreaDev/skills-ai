# Declara um token com associatividade à esquerda

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.left.php

---

# Parle\Parser::left

(PECL parle >= 0.5.1)

Parle\Parser::left — Declara um token com associatividade à esquerda

### Descrição

public function **Parle\Parser::left**([string](language.types.string.md) `$tok`): [void](language.types.void.md)

Declara um terminal com associatividade à esquerda.

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
