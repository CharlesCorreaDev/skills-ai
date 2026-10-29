# Obtém informação do erro

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.errorinfo.php

---

# Parle\RParser::errorInfo

(PECL parle >= 0.7.0)

Parle\RParser::errorInfo — Obtém informação do erro

### Descrição

public function **Parle\RParser::errorInfo**(): [Parle\ErrorInfo](class.parle-errorinfo.md)

Obtém informação do erro caso **Parle\RParser::action()** tenha retornado a ação de erro.

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
