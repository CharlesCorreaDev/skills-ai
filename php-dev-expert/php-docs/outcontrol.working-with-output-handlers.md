# Trabalhando com Manipuladores de Saída

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.working-with-output-handlers.php

---

## Trabalhando com Manipuladores de Saída

Quando invocados, os manipuladores de saída recebem o conteúdo do buffer
e uma máscara de bits indicando o status do buffer de saída.

function 
handler
(
[string](language.types.string.md) `$buffer`
, 
[int](language.types.integer.md) `$phase`
 = ?): [string](language.types.string.md)

`buffer`
:   Conteúdo do buffer de saída.

`phase`
:   Máscara de bits das
    constantes
    [**`PHP_OUTPUT_HANDLER_*`**](outcontrol.constants.md#constant.php-output-handler-start).

**Aviso**

Chamar qualquer das funções a seguir de dentro de um manipulador de saída
resultará em um erro fatal:
[ob\_clean()](function.ob-clean.md), [ob\_end\_clean()](function.ob-end-clean.md),
[ob\_end\_flush()](function.ob-end-flush.md), [ob\_flush()](function.ob-flush.md),
[ob\_get\_clean()](function.ob-get-clean.md), [ob\_get\_flush()](function.ob-get-flush.md) ou
[ob\_start()](function.ob-start.md).

> **Nota**:
>
> Se a constante **`PHP_OUTPUT_HANDLER_DISABLED`** de um manipulador estiver definida,
> ele não será invocado chamando
> [ob\_end\_clean()](function.ob-end-clean.md), [ob\_end\_flush()](function.ob-end-flush.md),
> [ob\_get\_clean()](function.ob-get-clean.md), [ob\_get\_flush()](function.ob-get-flush.md),
> [ob\_clean()](function.ob-clean.md),
> [ob\_flush()](function.ob-flush.md)
> ou durante o processo de desligamento do PHP.
> Antes do PHP 8.4.0 esta opção não tinha efeito ao chamar [ob\_clean()](function.ob-clean.md)
> ou [ob\_flush()](function.ob-flush.md).

> **Nota**:
>
> O diretório de trabalho do script pode mudar dentro da função de desligamento
> em alguns servidores web, por ex. Apache ou o servidor web integrado.

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
