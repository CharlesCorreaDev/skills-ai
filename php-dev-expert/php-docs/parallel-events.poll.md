# Pesquisa

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events.poll.php

---

# parallel\Events::poll

(0.9.0)

parallel\Events::poll — Pesquisa

### Descrição

public function **parallel\Events::poll**(): [?](language.types.null.md)[parallel\Events\Event](class.parallel-events-event.md)

Pesquisa pelo próximo evento.

### Valor Retornado

Caso não haja alvos restantes, **`null`** será retornado.

Caso este seja um laço não bloqueante e ocorra bloqueio, **`null`** deverá ser retornado.

Caso contrário, o [parallel\Events\Event](class.parallel-events-event.md) retornado descreve o evento.

### Exceptions

**Aviso**

Lança uma exceção parallel\Events\Error\Timeout se o tempo limite for usado e tiver sido alcançado.

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
