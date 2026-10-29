# Verifica se o elemento atual do iterador interno tem ou não filhos

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parentiterator.haschildren.php

---

# ParentIterator::hasChildren

(PHP 5 >= 5.1.0, PHP 7, PHP 8)

ParentIterator::hasChildren — Verifica se o elemento atual do iterador interno tem ou não filhos

### Descrição

public function **ParentIterator::hasChildren**(): [bool](language.types.boolean.md)

Verifica se o elemento atual do iterador interno tem filhos.

**Aviso**

Esta função não
está documentada; apenas a lista de argumentos está disponível.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

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
