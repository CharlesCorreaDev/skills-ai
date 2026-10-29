# Opções Passadas aos Manipuladores de Saída

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.flags-passed-to-output-handlers.php

---

## Opções Passadas aos Manipuladores de Saída

A máscara de bits passada para o segundo parâmetro `phase`
do manipulador de saída fornece informações sobre a invocação do manipulador.

> **Nota**:
>
> A máscara de bits pode incluir mais de uma opção
> e o operador binário `&` deve ser usado
> para verificar se uma opção está definida.

**Aviso**

O valor de **`PHP_OUTPUT_HANDLER_WRITE`** e seu apelido
**`PHP_OUTPUT_HANDLER_CONT`** é `0`
portanto, se ele está definido ou não só pode ser determinado
usando-se um
[operador de igualdade](language.operators.comparison.md)
(`==` ou `===`).

As seguintes opções são definidas em uma fase específica do ciclo de vida do manipulador:
**`PHP_OUTPUT_HANDLER_START`** é definida
quando um manipulador é invocado pela primeira vez.
**`PHP_OUTPUT_HANDLER_FINAL`**
ou seu apelido **`PHP_OUTPUT_HANDLER_END`**
é definida quando um manipulador é invocado pela última vez,
ou seja, ele está sendo desligado. Esta opção também é definida
quando os buffers estão sendo desligados pelo processo de desligamento do PHP.

As seguintes opções são definidas por uma invocação específica do manipulador:
**`PHP_OUTPUT_HANDLER_FLUSH`** é definida
quando o manipulador é invocado chamando-se [ob\_flush()](function.ob-flush.md).
**`PHP_OUTPUT_HANDLER_WRITE`**
ou seu apelido **`PHP_OUTPUT_HANDLER_CONT`**
é definida quando o tamanho de seu conteúdo é igual ou excede o tamanho do buffer
e o manipulador é invocado enquanto o buffer está sendo descarregado automaticamente.
**`PHP_OUTPUT_HANDLER_FLUSH`** é definida
quando o manipulador é invocado chamando-se [ob\_clean()](function.ob-clean.md),
[ob\_end\_clean()](function.ob-end-clean.md) ou [ob\_get\_clean()](function.ob-get-clean.md).
Quando [ob\_end\_clean()](function.ob-end-clean.md) ou [ob\_get\_clean()](function.ob-get-clean.md)
são chamados, **`PHP_OUTPUT_HANDLER_FINAL`** também é definida.

> **Nota**:
>
> Quando [ob\_end\_flush()](function.ob-end-flush.md) ou [ob\_get\_flush()](function.ob-get-flush.md)
> são chamadas, **`PHP_OUTPUT_HANDLER_FINAL`** é definida
> mas **`PHP_OUTPUT_HANDLER_FLUSH`** não é.

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
