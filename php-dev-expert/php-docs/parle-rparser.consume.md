# Consome os dados para processamento

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rparser.consume.php

---

# Parle\RParser::consume

(PECL parle >= 0.7.0)

Parle\RParser::consume — Consome os dados para processamento

### Descrição

public function **Parle\RParser::consume**([string](language.types.string.md) `$data`, [Parle\RLexer](class.parle-rlexer.md) `$rlexer`): [void](language.types.void.md)

Consome os dados para análise.

### Parâmetros

`data`
:   Dados a serem analisados.

`lexer`
:   Um objeto Lexer contendo as regras de análise lexica preparadas para a gramática específica.

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
