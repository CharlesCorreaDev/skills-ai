# Recupera um nome de regra ou de token

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.sigilname.php

---

# Parle\RParser::sigilName

(PECL parle >= 0.8.4)

Parle\RParser::sigilName — Recupera um nome de regra ou de token

### Descrição

public function **Parle\RParser::sigilName**([int](language.types.integer.md) `$idx`): [string](language.types.string.md)

Recupera um nome de regra ou nome de token parcial correspondente ao índice de sigil.

### Parâmetros

`idx`
:   Índice de correspondência, baseado em zero.

### Valor Retornado

Retorna uma [string](language.types.string.md) com a parte correspondente.

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
