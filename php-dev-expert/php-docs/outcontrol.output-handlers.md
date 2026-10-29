# Manipuladores de Saída

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.output-handlers.php

---

## Manipuladores de Saída

Manipuladores de saída são funções do tipo [callable](language.types.callable.md) associadas com buffers de saída
que são invocados ao chamar [ob\_clean()](function.ob-clean.md),
[ob\_flush()](function.ob-flush.md), [ob\_end\_flush()](function.ob-end-flush.md),
[ob\_get\_flush()](function.ob-get-flush.md), [ob\_end\_clean()](function.ob-end-clean.md),
[ob\_get\_clean()](function.ob-get-clean.md) ou durante o processo de desligamento do PHP.

> **Nota**:
>
> O processo de desligamento irá descarregar o valor de retorno do manipulador.

Se omitido ou **`null`** ao iniciar o buffer de saída,
o `"default output handler"` (manipulador de saída padão) interno será usado,
retornando o conteúdo não modificado do buffer quando invocado.
Manipuladores de saída podem ser usados ​​para retornar uma versão modificada
do conteúdo do buffer e/ou ter efeitos colaterais (por exemplo, enviar cabeçalhos).

O PHP vem com dois manipuladores de saída internos:
`"default output handler"`
e `"URL-Rewriter"` (que é integrado em
seu próprio buffer de saída e no máximo duas instâncias dele podem ser iniciadas).

As extensões incluídas no PHP são equipadas com quatro manipuladores de saída adicionais:
[mb\_output\_handler()](function.mb-output-handler.md), [ob\_gzhandler()](function.ob-gzhandler.md),
[ob\_iconv\_handler()](function.ob-iconv-handler.md) e [ob\_tidyhandler()](function.ob-tidyhandler.md).

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
