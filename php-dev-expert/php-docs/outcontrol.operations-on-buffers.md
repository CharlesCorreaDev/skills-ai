# Operações permitidas em buffers

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.operations-on-buffers.php

---

## Operações permitidas em buffers

As operações permitidas em buffers podem ser controladas
passando uma das
[opções de controle de buffer](outcontrol.constants.md#outcontrol.constants.buffer-control-flags)
para o terceiro parâmetro `flags`
de [ob\_start()](function.ob-start.md).
Se omitido, todas as operações serão permitidas por padrão.
Se `0` for usado,
o buffer não poderá ser descarregado, limpo ou removido,
mas seu conteúdo ainda poderá ser recuperado.

**`PHP_OUTPUT_HANDLER_CLEANABLE`** permite que
[ob\_clean()](function.ob-clean.md) limpe o conteúdo do buffer.

**Aviso**

A ausência da opção **`PHP_OUTPUT_HANDLER_CLEANABLE`**
não impedirá que [ob\_end\_clean()](function.ob-end-clean.md)
ou [ob\_get\_clean()](function.ob-get-clean.md) limpem o conteúdo do buffer.

**`PHP_OUTPUT_HANDLER_FLUSHABLE`** permite que
[ob\_flush()](function.ob-flush.md) descarregue o conteúdo do buffer.

**Aviso**

A ausência da opção **`PHP_OUTPUT_HANDLER_FLUSHABLE`**
não impedriá que [ob\_end\_flush()](function.ob-end-flush.md)
ou [ob\_get\_flush()](function.ob-get-flush.md) descarreguem o conteúdo do buffer.

**`PHP_OUTPUT_HANDLER_REMOVABLE`** permite que
[ob\_end\_clean()](function.ob-end-clean.md), [ob\_end\_flush()](function.ob-end-flush.md),
[ob\_get\_clean()](function.ob-get-clean.md) ou [ob\_get\_flush()](function.ob-get-flush.md)
desliguem o buffer.

**`PHP_OUTPUT_HANDLER_STDFLAGS`**,
a combinação das três opções irá permitir que cada uma das três operações
seja realizada no buffer.

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
