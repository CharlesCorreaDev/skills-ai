# Constantes predefinidas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.constants.php

---

# Constantes predefinidas

As constantes abaixo estão sempre disponíveis como parte do núcleo do PHP.

**Opções de status passadas ao manipulador de saída**

As opções a seguir são passadas no segundo parâmetro (`phase`) do manipulador de saída definido por [ob\_start()](function.ob-start.md) como parte de uma máscara de bits:

**`PHP_OUTPUT_HANDLER_START`** ([int](language.types.integer.md))
:   Indica que o buffer de saída iniciou.

**`PHP_OUTPUT_HANDLER_WRITE`** ([int](language.types.integer.md))
:   Indica que o buffer de saída está sendo despejado, e tinha dados para enviar.

**`PHP_OUTPUT_HANDLER_FLUSH`** ([int](language.types.integer.md))
:   Indica que o buffer de saída foi despejado.

**`PHP_OUTPUT_HANDLER_CLEAN`** ([int](language.types.integer.md))
:   Indica que o buffer de saída foi limpo.

**`PHP_OUTPUT_HANDLER_FINAL`** ([int](language.types.integer.md))
:   Indica que esta é a operação de buffer de saída final.

**`PHP_OUTPUT_HANDLER_CONT`** ([int](language.types.integer.md))
:   Indica que o buffer de saída foi despejado, mas que operação de buffer de saída irá
    continuar.

    Este é um apelido para
    **`PHP_OUTPUT_HANDLER_WRITE`**.

**`PHP_OUTPUT_HANDLER_END`** ([int](language.types.integer.md))
:   Indica que o buffer de saída terminou.

    Este é um apelido para
    **`PHP_OUTPUT_HANDLER_FINAL`**.

**Opções de controle de buffer de saída**

As opções a seguir podem ser passadas no terceiro parâmetro (`flags`) do manipulador de saída definido por [ob\_start()](function.ob-start.md) como uma máscara de bits.:

**`PHP_OUTPUT_HANDLER_CLEANABLE`** ([int](language.types.integer.md))
:   Controla se um buffer de saída criado por
    [ob\_start()](function.ob-start.md) pode ser limpo
    por [ob\_clean()](function.ob-clean.md).
    Esta opção não controla o comportamento de
    [ob\_end\_clean()](function.ob-end-clean.md) ou [ob\_get\_clean()](function.ob-get-clean.md).

**`PHP_OUTPUT_HANDLER_FLUSHABLE`** ([int](language.types.integer.md))
:   Controla se um buffer de saída criado por
    [ob\_start()](function.ob-start.md) pode ser despejado
    por [ob\_flush()](function.ob-flush.md).
    Esta opção não controla o comportamento de
    [ob\_end\_flush()](function.ob-end-flush.md) ou [ob\_get\_flush()](function.ob-get-flush.md).

**`PHP_OUTPUT_HANDLER_REMOVABLE`** ([int](language.types.integer.md))
:   Controla se um buffer de saída criado por
    [ob\_start()](function.ob-start.md) pode ser removido antes do final do script
    ou ao chamar [ob\_end\_clean()](function.ob-end-clean.md), [ob\_end\_flush()](function.ob-end-flush.md),
    [ob\_get\_clean()](function.ob-get-clean.md) ou [ob\_get\_flush()](function.ob-get-flush.md).

**`PHP_OUTPUT_HANDLER_STDFLAGS`** ([int](language.types.integer.md))
:   O conjunto padrão de opções de buffer de saída; atualmente equivalente a
    **`PHP_OUTPUT_HANDLER_CLEANABLE`** |
    **`PHP_OUTPUT_HANDLER_FLUSHABLE`** |
    **`PHP_OUTPUT_HANDLER_REMOVABLE`**.

**Opções de status do manipulador de saída**

As opções a seguir são parte da máscara de bits `flags`
retornada por [ob\_get\_status()](function.ob-get-status.md):

**`PHP_OUTPUT_HANDLER_STARTED`** ([int](language.types.integer.md))
:   Indica que um manipulador de saída foi chamado.

**`PHP_OUTPUT_HANDLER_DISABLED`** ([int](language.types.integer.md))
:   Indica que o manipulador de saída está desabilitado.
    Esta opção é definida quando o manipulador de saída retorna **`false`**
    ou falha durante o processamento do buffer.
    Antes do PHP 8.4.0, esta opção poderia ser definida ao iniciar um buffer de saída.

**`PHP_OUTPUT_HANDLER_PROCESSED`** ([int](language.types.integer.md))
:   Indica que o manipulador de saída processou o buffer com sucesso.
    Disponível a partir do PHP 8.4.0.

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
