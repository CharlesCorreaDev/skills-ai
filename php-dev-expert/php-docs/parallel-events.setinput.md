# Entrada

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events.setinput.php

---

# parallel\Events::setInput

(0.9.0)

parallel\Events::setInput — Entrada

### Descrição

public function **parallel\Events::setInput**(Input `$input`): [void](language.types.void.md)

Define a entrada informada em `input` para este laço de evento.

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
