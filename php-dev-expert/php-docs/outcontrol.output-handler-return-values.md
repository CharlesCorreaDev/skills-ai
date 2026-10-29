# Valores de Retorno do Menipulador de Saída

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.output-handler-return-values.php

---

## Valores de Retorno do Menipulador de Saída

O valor de retorno do manipulador de saída é internamente forçado para uma string
seguindo a semântica padrão de tipos do PHP, com duas exceções:
[array](language.types.array.md)s e [bool](language.types.boolean.md)eanos.

Arrays são convertidos na string `"Array"`
mas o alerta `Array to string conversion` (conversão de array para string)
não é emitido.

Se o manipulador retorna **`false`**, o conteúdo do buffer é retornado.
Se o manipulador retorna **`true`**, uma string vazia é retornada.

> **Nota**:
>
> Se o manipulador retorna **`false`** ou lança uma exceção,
> sua constante de estado **`PHP_OUTPUT_HANDLER_DISABLED`** é definida.

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
