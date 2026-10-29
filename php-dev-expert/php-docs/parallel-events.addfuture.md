# Alvos

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events.addfuture.php

---

# parallel\Events::addFuture

(0.9.0)

parallel\Events::addFuture — Alvos

### Descrição

public function **parallel\Events::addFuture**([string](language.types.string.md) `$name`, [parallel\Future](class.parallel-future.md) `$future`): [void](language.types.void.md)

Observa eventos no `future` informado.

### Exceptions

**Aviso**

Lança uma exceção parallel\Events\Error\Existence se o alvo com o nome informado já tiver sido adicionado.

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
