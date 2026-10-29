# Retorna o iterador interno para a entrada atual

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outeriterator.getinneriterator.php

---

# OuterIterator::getInnerIterator

(PHP 5 >= 5.1.0, PHP 7, PHP 8)

OuterIterator::getInnerIterator — Retorna o iterador interno para a entrada atual

### Descrição

public function **OuterIterator::getInnerIterator**(): [?](language.types.null.md)[Iterator](class.iterator.md)

Retorna o iterador interno para a entrada atual do iterador.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o iterador interno para a entrada atual se existir, ou **`null`** caso contrário.

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
