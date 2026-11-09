# Obtém informação do erro

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.errorinfo.php

---

# Parle\Parser::errorInfo

(PECL parle >= 0.5.1)

Parle\Parser::errorInfo — Obtém informação do erro

### Descrição

public function **Parle\Parser::errorInfo**(): [Parle\ErrorInfo](class.parle-errorinfo.md)

Recupera as informações de erro caso **Parle\Parser::action()** tenha retornado a ação de erro.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna uma instância de [Parle\ErrorInfo](class.parle-errorinfo.md).

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
