# Expressões PCRE

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pcre.pattern.php

---

# Expressões PCRE

## Índice

- [Sintaxe das expressões regulares PCRE](reference.pcre.pattern.syntax.md)
- [Possíveis modificadores em expressões regulares](reference.pcre.pattern.modifiers.md)
- [Diferenças para o Perl](reference.pcre.pattern.differences.md)

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
