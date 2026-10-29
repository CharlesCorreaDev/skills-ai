# Cancelamento

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-future.cancel.php

---

# parallel\Future::cancel

(0.9.0)

parallel\Future::cancel — Cancelamento

### Descrição

public function **parallel\Future::cancel**(): [bool](language.types.boolean.md)

Tenta cancelar a tarefa.

> **Nota**:
>
> Se a tarefa estiver em execução, será interrompida.

**Aviso**

Chamadas de função internas em andamento não podem ser interrompidas.

### Exceptions

**Aviso**

Lança uma exceção parallel\Future\Error\Killed se a tarefa de execução de [parallel\Runtime](class.parallel-runtime.md) tiver sido encerrada.

**Aviso**

Lança uma exceção parallel\Future\Error\Cancelled se a tarefa já tiver sido cancelada.

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
