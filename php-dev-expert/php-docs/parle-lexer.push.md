# Adiciona uma regra de análise léxica

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-lexer.push.php

---

# Parle\Lexer::push

(PECL parle >= 0.5.1)

Parle\Lexer::push — Adiciona uma regra de análise léxica

### Descrição

public function **Parle\Lexer::push**([string](language.types.string.md) `$regex`, [int](language.types.integer.md) `$id`): [void](language.types.void.md)

Insere na pilha um padrão de reconhecimento de lexema.

### Parâmetros

`regex`
:   Expressão regular usada para correspondência de tokens.

`id`
:   ID do token. Se a instância do analisador léxico for destinada a ser usada de forma independente, este pode ser um número arbitrário. Se a instância do analisador léxico for passada para o analisador, deve ser um ID retornado por [Parle\Parser::tokenid()](parle-parser.tokenid.md).

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
