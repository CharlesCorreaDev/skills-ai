# Declara um token sem associatividade

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.nonassoc.php

---

# Parle\Parser::nonassoc

(PECL parle >= 0.5.1)

Parle\Parser::nonassoc — Declara um token sem associatividade

### Descrição

public function **Parle\Parser::nonassoc**([string](language.types.string.md) `$tok`): [void](language.types.void.md)

Declara um terminal, que não pode aparecer mais de uma vez na linha.

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
