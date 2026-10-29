# Declara um token com associatividade à direita

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.right.php

---

# Parle\RParser::right

(PECL parle >= 0.7.0)

Parle\RParser::right — Declara um token com associatividade à direita

### Descrição

public function **Parle\RParser::right**([string](language.types.string.md) `$tok`): [void](language.types.void.md)

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
