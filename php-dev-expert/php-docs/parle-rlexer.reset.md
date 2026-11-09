# Redefine o analisador léxico

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rlexer.reset.php

---

# Parle\RLexer::reset

(PECL parle >= 0.7.1)

Parle\RLexer::reset — Redefine o analisador léxico

### Descrição

public function **Parle\RLexer::reset**([int](language.types.integer.md) `$pos`): [void](language.types.void.md)

Redefine o analisador léxico fornecendo, opcionalmente, a posição desejada.

### Parâmetros

`pos`
:   Posição de redefinição.

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
