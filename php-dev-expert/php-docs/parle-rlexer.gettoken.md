# Obtém o token atual

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rlexer.gettoken.php

---

# Parle\RLexer::getToken

(PECL parle >= 0.5.1)

Parle\RLexer::getToken — Obtém o token atual

### Descrição

public function **Parle\RLexer::getToken**(): [Parle\Token](class.parle-token.md)

Obtém o token atual.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna uma instância de [Parle\Token](class.parle-token.md).

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
