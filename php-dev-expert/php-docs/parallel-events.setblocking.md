# Comportamento

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events.setblocking.php

---

# parallel\Events::setBlocking

(0.9.0)

parallel\Events::setBlocking — Comportamento

### Descrição

Por padrão, quando eventos são pesquisados, o bloqueio ocorrerá (no nível do PHP) até que o primeiro evento possa ser retornado: definir o modo de bloqueio como **`false`** fará com que
a pesquisa retorne o controle se o primeiro alvo pesquisado não estiver pronto.

Isso difere de definir um tempo limite de 0 com [parallel\Events::setTimeout()](parallel-events.settimeout.md), pois um tempo limite de 0, embora permitido, fará com que uma exceção seja gerada,
o que pode ser extremamente lento ou um desperdício se o que realmente se deseja é um comportamento não bloqueante.

Um laço não bloqueante afeta o valor de retorno de [parallel\Events::poll()](parallel-events.poll.md), de modo que ele pode ser **`null`** antes que todos os eventos tenham sido processados.

public function **parallel\Events::setBlocking**([bool](language.types.boolean.md) `$blocking`): [void](language.types.void.md)

Define o modo de bloqueio.

### Exceptions

**Aviso**

Lança uma exceção parallel\Events\Error se o laço tiver tempo limite definido.

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
