# Rastreia a operação do analisador

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.trace.php

---

# Parle\Parser::trace

(PECL parle >= 0.5.1)

Parle\Parser::trace — Rastreia a operação do analisador

### Descrição

public function **Parle\Parser::trace**(): [string](language.types.string.md)

Recupera a descrição da operação atual do analisador. Isso pode ser especialmente útil para estudar o analisador e otimizar a gramática.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna uma [string](language.types.string.md) com as informações de rastreamento.

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
