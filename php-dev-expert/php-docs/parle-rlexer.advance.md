# Processa a próxima regra do analisador léxico

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rlexer.advance.php

---

# Parle\RLexer::advance

(PECL parle >= 0.5.1)

Parle\RLexer::advance — Processa a próxima regra do analisador léxico

### Descrição

public function **Parle\RLexer::advance**(): [void](language.types.void.md)

Processa a próxima regra e prepara os dados de token resultantes.

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
