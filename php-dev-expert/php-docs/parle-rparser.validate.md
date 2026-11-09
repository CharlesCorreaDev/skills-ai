# Valida entrada

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.validate.php

---

# Parle\RParser::validate

(PECL parle >= 0.7.0)

Parle\RParser::validate — Valida entrada

### Descrição

public function **Parle\RParser::validate**([string](language.types.string.md) `$data`, [Parle\RLexer](class.parle-rlexer.md) `$lexer`): [bool](language.types.boolean.md)

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
