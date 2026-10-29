# Constantes predefinidas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle.constants.php

---

# Constantes predefinidas

As constantes abaixo são definidas por esta extensão e
só estarão disponíveis quando a extensão tiver sido compilada no PHP
ou tiver sido carregada dinamicamente em tempo de execução.

**`Parle\INTERNAL_UTF32`** [bool](language.types.boolean.md)
:   Indica se o suporte interno UTF-32 foi compilado. Disponível desde o Parle 0.7.2.

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
