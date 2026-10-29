# Processa a próxima regra do analisador

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.advance.php

---

# Parle\Parser::advance

(PECL parle >= 0.5.1)

Parle\Parser::advance — Processa a próxima regra do analisador

### Descrição

public function **Parle\Parser::advance**(): [void](language.types.void.md)

Processa a próxima regra do analisador.

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
