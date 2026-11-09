# Examples

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pcre.examples.php

---

# Examples

**Exemplo #1 Exemplos de expressões válidas**

- `/<\/\w+>/`
- `|(\d{3})-\d+|Sm`
- `/^(?i)php[34]/`
- `{^\s+(\s+)?$}`

**Exemplo #2 Exemplos de expressões inválidas**

- `/href='(.*)'` - faltando o delimitador final
- `/\w+\s*\w+/J` - modificador 'J' desconhecido
- `1-\d3-\d3-\d4|` - faltando delimitador inicial

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
