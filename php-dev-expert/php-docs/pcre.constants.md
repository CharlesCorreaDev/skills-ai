# Constantes predefinidas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pcre.constants.php

---

# Constantes predefinidas

As constantes abaixo são definidas por esta extensão e
só estarão disponíveis quando a extensão tiver sido compilada no PHP
ou tiver sido carregada dinamicamente em tempo de execução.

**Constantes PREG**

| Constantes | Descrição | Desde |
| --- | --- | --- |
| **`PREG_PATTERN_ORDER`** ([int](language.types.integer.md)) | Ordena os resultados de modo que $matches[0] seja um array de todas as correspondências da expressão, $matches[1] seja um array de strings combinadas pela primeira sub-expressão, e assim por diante. Esta opção é somente usada com [preg\_match\_all()](function.preg-match-all.md). |  |
| **`PREG_SET_ORDER`** ([int](language.types.integer.md)) | Ordena os resultados de modo que $matches[0] seja um array do primeiro conjunto de correspondências, $matches[1] seja um array do segundo conjunto de correspondências, e assim por diante. Esta opção é somente usada com [preg\_match\_all()](function.preg-match-all.md). |  |
| **`PREG_OFFSET_CAPTURE`** ([int](language.types.integer.md)) | Se esta opção for definida, para cada correspondência a posição do byte também será retornada. Observe que isto muda os valores de retorno para um array onde cada elemento é um array consistindo da string correspondida no elemento 0 e sua posição na string de entrada no elemento 1. |  |
| **`PREG_SPLIT_NO_EMPTY`** ([int](language.types.integer.md)) | Esta opção configura [preg\_split()](function.preg-split.md) para retornar apenas pedaços não vazios. |  |
| **`PREG_SPLIT_DELIM_CAPTURE`** ([int](language.types.integer.md)) | Esta opção configura [preg\_split()](function.preg-split.md) para capturar expressões entre parênteses em expressões delimitadas. |  |
| **`PREG_SPLIT_OFFSET_CAPTURE`** ([int](language.types.integer.md)) | Veja a descrição de **`PREG_OFFSET_CAPTURE`**. Esta opção é usada somente para [preg\_split()](function.preg-split.md). |  |
| **`PREG_UNMATCHED_AS_NULL`** ([int](language.types.integer.md)) | Esta opção informa a [preg\_match()](function.preg-match.md) e [preg\_match\_all()](function.preg-match-all.md) para incluir sub-expressões não correspondidas em $matches como **`null`**. Sem esta opção, sub-expressões sem correspondência são reportadas como strings vazias, como se fossem correspondências vazias. Informar esta opção permite diferenciar entre esses dois casos. Com [preg\_match()](function.preg-match.md), subpadrões não correspondidos no final são omitidos de $matches completamente, a menos que esta opção seja usada; a partir do PHP 7.4.0, a opção os reporta como **`null`**, de modo que $matches sempre tenha o mesmo tamanho. | 7.2.0 |
| **`PREG_NO_ERROR`** ([int](language.types.integer.md)) | Retornada pela [preg\_last\_error()](function.preg-last-error.md) se não houver erros. | 5.2.0 |
| **`PREG_INTERNAL_ERROR`** ([int](language.types.integer.md)) | Retornada pela [preg\_last\_error()](function.preg-last-error.md) se houver um erro interno na PCRE. | 5.2.0 |
| **`PREG_BACKTRACK_LIMIT_ERROR`** ([int](language.types.integer.md)) | Retornada pela [preg\_last\_error()](function.preg-last-error.md) se o [limite de rastreamento retroativo](pcre.configuration.md#ini.pcre.backtrack-limit) tiver sido ultrapassado. | 5.2.0 |
| **`PREG_RECURSION_LIMIT_ERROR`** ([int](language.types.integer.md)) | Retornada pela [preg\_last\_error()](function.preg-last-error.md) se o [limite de recursividade](pcre.configuration.md#ini.pcre.recursion-limit) tiver sido ultrapassado. | 5.2.0 |
| **`PREG_BAD_UTF8_ERROR`** ([int](language.types.integer.md)) | Retornada pela [preg\_last\_error()](function.preg-last-error.md) se o último erro foi causado por dados UTF-8 mal formados (somente ao usar uma expressão regular em [modo UTF-8](reference.pcre.pattern.modifiers.md)). | 5.2.0 |
| **`PREG_BAD_UTF8_OFFSET_ERROR`** ([int](language.types.integer.md)) | Retornada pela [preg\_last\_error()](function.preg-last-error.md) se o deslocamento não tiver correspondido ao início de um ponto de código UTF-8 válido (somente ao usar uma expressão regular em [modo UTF-8](reference.pcre.pattern.modifiers.md)). | 5.3.0 |
| **`PREG_JIT_STACKLIMIT_ERROR`** ([int](language.types.integer.md)) | Retornada por [preg\_last\_error()](function.preg-last-error.md) se a última função PCRE falhou por falta de espaço em pilha do JIT. | 7.0.0 |
| **`PCRE_VERSION`** ([string](language.types.string.md)) | Versão da PCRE e data de lançamento (e.g. "`7.0 18-Dec-2006`"). | 5.2.4 |
| **`PCRE_VERSION_MAJOR`** ([int](language.types.integer.md)) | Número de versão principal do PCRE. |  |
| **`PCRE_VERSION_MINOR`** ([int](language.types.integer.md)) | Número de versão secundária do PCRE. |  |
| **`PCRE_JIT_SUPPORT`** ([bool](language.types.boolean.md)) | Indica se o suporte PCRE JIT está disponível. |  |
| **`PREG_GREP_INVERT`** ([int](language.types.integer.md)) | Retorna os elementos que não correspondem à expressão informada. |  |

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
