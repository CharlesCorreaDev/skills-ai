# Finaliza as regras gramaticais

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-parser.build.php

---

# Parle\Parser::build

(PECL parle >= 0.5.1)

Parle\Parser::build — Finaliza as regras gramaticais

### Descrição

public function **Parle\Parser::build**(): [void](language.types.void.md)

Todos os tokens e regras gramaticais adicionados anteriormente são finalizados. O conjunto de regras torna-se somente leitura e o analisador está pronto para iniciar.

### Parâmetros

Esta função não possui parâmetros.

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
