# Declara uma regra de precedência

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.precedence.php

---

# Parle\Parser::precedence

(PECL parle >= 0.5.1)

Parle\Parser::precedence — Declara uma regra de precedência

### Descrição

public function **Parle\Parser::precedence**([string](language.types.string.md) `$tok`): [void](language.types.void.md)

Declara uma regra de precedência para um símbolo terminal fictício. Esta regra pode ser usada posteriormente nas regras gramaticais específicas.

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
