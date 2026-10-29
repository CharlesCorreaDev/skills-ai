# Encerramento de Runtime

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-runtime.kill.php

---

# parallel\Runtime::kill

(0.8.0)

parallel\Runtime::kill — Encerramento de Runtime

### Descrição

public function **parallel\Runtime::kill**(): [void](language.types.void.md)

Tenta forçar o Runtime a encerrar.

> **Nota**:
>
> Tarefas agendadas para execução não serão executadas, a tarefa em execução no momento será interrompida.

**Aviso**

Chamadas de funções internas em andamento não podem ser interrompidas.

### Exceptions

**Aviso**

Lança uma exceção parallel\Runtime\Error\Closed se Runtime tiver sido fechada.

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
