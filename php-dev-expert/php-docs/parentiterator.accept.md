# Determina a aceitabilidade

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parentiterator.accept.php

---

# ParentIterator::accept

(PHP 5 >= 5.1.0, PHP 7, PHP 8)

ParentIterator::accept — Determina a aceitabilidade

### Descrição

public function **ParentIterator::accept**(): [bool](language.types.boolean.md)

Determina se o elemento atual tem filhos.

**Aviso**

Esta função não
está documentada; apenas a lista de argumentos está disponível.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

**`true`** se o elemento atual for aceitável, caso contrário, **`false`**.

### Veja também

- [ParentIterator::hasChildren()](parentiterator.haschildren.md) - Verifica se o elemento atual do iterador interno tem ou não filhos
- [FilterIterator::accept()](filteriterator.accept.md) - Verifica se o elemento atual do iterador é aceitável

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
