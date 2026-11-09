# Valida entrada

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.validate.php

---

# Parle\Parser::validate

(PECL parle >= 0.5.1)

Parle\Parser::validate — Valida entrada

### Descrição

public function **Parle\Parser::validate**([string](language.types.string.md) `$data`, [Parle\Lexer](class.parle-lexer.md) `$lexer`): [bool](language.types.boolean.md)

Valida uma string de entrada. A string é analisada internamente, portanto, este método é útil para validação rápida de entrada.

### Parâmetros

`data`
:   String a ser validada.

`lexer`
:   Um objeto Lexer contendo as regras de análise lexica preparadas para a gramática específica.

### Valor Retornado

Retorna [bool](language.types.boolean.md) informando se a entrada está em concordância ou não com as regras definidas.

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
