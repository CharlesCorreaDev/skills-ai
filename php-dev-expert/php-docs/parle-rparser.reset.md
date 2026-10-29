# Redefine estado do analisador

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.reset.php

---

# Parle\RParser::reset

(PECL parle >= 0.7.1)

Parle\RParser::reset — Redefine estado do analisador

### Descrição

public function **Parle\RParser::reset**([int](language.types.integer.md) `$tokenId` = ?): [void](language.types.void.md)

Redefine o estado do analisador usando o ID do token fornecido.

### Parâmetros

`tokenId`
:   ID do token.

### Valor Retornado

Nenhum valor é retornado.

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
