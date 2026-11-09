# Alvos

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events.remove.php

---

# parallel\Events::remove

(0.9.0)

parallel\Events::remove — Alvos

### Descrição

public function **parallel\Events::remove**([string](language.types.string.md) `$target`): [void](language.types.void.md)

Remove o alvo informado em `target`.

### Exceptions

**Aviso**

Lança uma exceção parallel\Events\Error\Existence se o alvo com o nome informado não for encontrado.

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
