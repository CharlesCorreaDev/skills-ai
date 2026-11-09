# Entradas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events-input.remove.php

---

# parallel\Events\Input::remove

(0.9.0)

parallel\Events\Input::remove — Entradas

### Descrição

public function **parallel\Events\Input::remove**([string](language.types.string.md) `$target`): [void](language.types.void.md)

Remove a entrada do alvo especificado.

### Exceptions

**Aviso**

Lança uma exceção parallel\Events\Input\Error\Existence se a entrada para o alvo não existir.

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
