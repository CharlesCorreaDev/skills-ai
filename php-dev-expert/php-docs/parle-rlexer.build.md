# Finaliza o conjunto de regras do analisador léxico

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rlexer.build.php

---

# Parle\RLexer::build

(PECL parle >= 0.5.1)

Parle\RLexer::build — Finaliza o conjunto de regras do analisador léxico

### Descrição

public function **Parle\RLexer::build**(): [void](language.types.void.md)

As regras previamente adicionadas com [Parle\RLexer::push()](parle-rlexer.push.md) são finalizadas. Esta chamada de método deve ser feita após todas as regras necessárias serem inseridas na pilha. O conjunto de regras se torna somente leitura. A análise léxica então pode ser iniciada.

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
