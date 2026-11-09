# Obtém o ID do token

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.tokenid.php

---

# Parle\Parser::tokenId

(PECL parle >= 0.5.1)

Parle\Parser::tokenId — Obtém o ID do token

### Descrição

public function **Parle\Parser::tokenId**([string](language.types.string.md) `$tok`): [int](language.types.integer.md)

Recupera o ID do token nomeado.

### Parâmetros

`tok`
:   Nome do token como usado em [Parle\Parser::token()](parle-parser.token.md).

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
