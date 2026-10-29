# Adiciona uma regra gramatical

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.push.php

---

# Parle\Parser::push

(PECL parle >= 0.5.1)

Parle\Parser::push — Adiciona uma regra gramatical

### Descrição

public function **Parle\Parser::push**([string](language.types.string.md) `$name`, [string](language.types.string.md) `$rule`): [int](language.types.integer.md)

Insere na pilha uma regra gramatical. O ID de produção retornado pode ser usado posteriormente no processo de análise para identificar a regra correspondente.

### Parâmetros

`name`
:   Nome da regra.

`rule`
:   A regra a ser adicionada. A sintaxe é compatível com Bison.

### Valor Retornado

Retorna [int](language.types.integer.md) representando o índice da regra.

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
