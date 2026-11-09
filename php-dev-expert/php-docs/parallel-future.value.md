# Resolução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-future.value.php

---

# parallel\Future::value

(0.8.0)

parallel\Future::value — Resolução

### Descrição

public function **parallel\Future::value**(): [mixed](language.types.mixed.md)

Retorna (e se necessário espera pelo retorno) da tarefa.

### Exceptions

**Aviso**

Lança uma exceção parallel\Future\Error se a espera falhar (erro interno).

**Aviso**

Lança uma exceção parallel\Future\Error\Killed se a tarefa de execução de [parallel\Runtime](class.parallel-runtime.md) foi encerrada.

**Aviso**

Lança uma exceção parallel\Future\Error\Cancelled se a tarefa tiver sido cancelada.

**Aviso**

Lança uma exceção parallel\Future\Error\Foreign se a tarefa emitir uma exceção não capturável irreconhecível.

**Aviso**

Relança [Throwable](class.throwable.md) não capturada na tarefa.

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
