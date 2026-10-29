# Configurações de Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pcre.configuration.php

---

## Configurações de Execução

O comportamento destas funções é afetado pelas configurações do php.ini.

**Opções de configuração da PCRE**

| Nome | Padrão | Modificável | Registro de Alterações |
| --- | --- | --- | --- |
| [pcre.backtrack\_limit](pcre.configuration.md#ini.pcre.backtrack-limit) | "1000000" | **`INI_ALL`** |  |
| [pcre.recursion\_limit](pcre.configuration.md#ini.pcre.recursion-limit) | "100000" | **`INI_ALL`** |  |
| [pcre.jit](pcre.configuration.md#ini.pcre.jit) | "1" | **`INI_ALL`** |  |

Para mais detalhes e definições dos modos
INI\_\*, consulte os [Onde uma configuração deve ser definida](configuration.changes.modes.md).

Aqui está uma breve explicação das
diretivas de configuração.

`pcre.backtrack_limit` [int](language.types.integer.md)
:   Limite de rastreamento retroativo da PCRE. Padrão é de 100000 para PHP < 5.3.7.

`pcre.recursion_limit` [int](language.types.integer.md)
:   Limite de recursões da PCRE. Nota que se você definir este valor para um número bem
    alto poderá consumir toda a pilha de processo disponível e eventualmente
    travar o PHP (devido a alcançar o limite do tamanho da pilha imposto pelo sistema
    operacional).

`pcre.jit` [bool](language.types.boolean.md)
:   Configura se a compilação just-in-time do PCRE será utilizada.

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
