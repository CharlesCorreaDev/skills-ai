# Rastreia a operação do analisador

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.trace.php

---

# Parle\RParser::trace

(PECL parle >= 0.7.0)

Parle\RParser::trace — Rastreia a operação do analisador

### Descrição

public function **Parle\RParser::trace**(): [string](language.types.string.md)

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
