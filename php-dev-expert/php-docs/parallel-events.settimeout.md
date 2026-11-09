# Comportamento

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events.settimeout.php

---

# parallel\Events::setTimeout

(0.9.0)

parallel\Events::setTimeout — Comportamento

### Descrição

Por padrão, quando eventos são pesquisados, o bloqueio ocorrerá (no nível do PHP) até que o primeiro evento possa ser retornado: Definir o tempo limite faz com que uma exceção seja
gerada quando o tempo limite for atingido.

Isso é diferente de definir o modo de bloqueio como **`false`** com [parallel\Events::setBlocking()](parallel-events.setblocking.md), o que não causará o lançamento de uma exceção.

public function **parallel\Events::setTimeout**([int](language.types.integer.md) `$timeout`): [void](language.types.void.md)

Define o limite de tempo em microssegundos.

### Exceções

**Aviso**

Lança uma exceção parallel\Events\Error se o laço for não bloqueante.

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
