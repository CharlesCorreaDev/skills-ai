# Despeja a máquina de estados

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-lexer.dump.php

---

# Parle\Lexer::dump

(PECL parle >= 0.5.1)

Parle\Lexer::dump — Despeja a máquina de estados

### Descrição

public function **Parle\Lexer::dump**(): [void](language.types.void.md)

Despeja a máquina de estados atual na saída padrão.

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
