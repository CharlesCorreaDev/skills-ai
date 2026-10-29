# Entradas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events-input.add.php

---

# parallel\Events\Input::add

(0.9.0)

parallel\Events\Input::add — Entradas

### Descrição

public function **parallel\Events\Input::add**([string](language.types.string.md) `$target`, [mixed](language.types.mixed.md) `$value`): [void](language.types.void.md)

Define a entrada para o alvo especificado.

### Exceptions

**Aviso**

Lança uma exceção parallel\Events\Input\Error\Existence se a entrada para o alvo já existir.

**Aviso**

Lança uma exceção parallel\Events\Input\Error\IllegalValue se o valor for ilegal ([object](language.types.object.md), **`null`**).

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
