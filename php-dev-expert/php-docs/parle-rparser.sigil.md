# Recupera uma parte correspondente de uma regra

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.sigil.php

---

# Parle\RParser::sigil

(PECL parle >= 0.7.0)

Parle\RParser::sigil — Recupera uma parte correspondente de uma regra

### Descrição

public function **Parle\RParser::sigil**([int](language.types.integer.md) `$idx` = ?): [string](language.types.string.md)

Recupera uma parte da correspondência por meio de uma regra. Este método é equivalente à funcionalidade de pseudovariável do Bison.

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
