# Encerramento elegante de Runtime

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-runtime.close.php

---

# parallel\Runtime::close

(0.8.0)

parallel\Runtime::close — Encerramento elegante de Runtime

### Descrição

public function **parallel\Runtime::close**(): [void](language.types.void.md)

Solicita que a execução seja encerrada.

> **Nota**:
>
> As tarefas agendadas para execução serão executadas antes que o encerramento ocorra.

### Exceptions

**Aviso**

Lança uma exceção parallel\Runtime\Error\Closed se Runtime já tiver sido fechada.

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
