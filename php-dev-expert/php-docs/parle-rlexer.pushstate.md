# Insere na pilha um novo estado inicial

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rlexer.pushstate.php

---

# Parle\RLexer::pushState

(PECL parle >= 0.5.1)

Parle\RLexer::pushState — Insere na pilha um novo estado inicial

### Descrição

public function **Parle\RLexer::pushState**([string](language.types.string.md) `$state`): [int](language.types.integer.md)

Este tipo de analisador léxico pode ter mais de uma máquina de estados. Isso permite analisar diferentes tokens dependendo do contexto, facilitando a análise sintática. Uma vez que um estado é enviado, ele pode ser usado com uma variante de assinatura [Parle\RLexer::push()](parle-rlexer.push.md) adequada.

### Parâmetros

`state`
:   Nome do estado.

### Valor Retornado

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
