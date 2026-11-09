# Obtém o ID do token

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.tokenid.php

---

# Parle\RParser::tokenId

(PECL parle >= 0.7.0)

Parle\RParser::tokenId — Obtém o ID do token

### Descrição

public function **Parle\RParser::tokenId**([string](language.types.string.md) `$tok`): [int](language.types.integer.md)

Recupera o ID do token nomeado.

### Parâmetros

`tok`
:   Nome do token como utilizado em [Parle\RParser::token()](parle-rparser.token.md).

### Valor Retornado

Retorna um [int](language.types.integer.md) representando o ID do token.

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
