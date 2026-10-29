# Despeja a gramática

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.dump.php

---

# Parle\Parser::dump

(PECL parle >= 0.5.1)

Parle\Parser::dump — Despeja a gramática

### Descrição

public function **Parle\Parser::dump**(): [void](language.types.void.md)

Despeja a gramática atual na saída padrão.

### Parâmetros

Esta função não possui parâmetros.

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
