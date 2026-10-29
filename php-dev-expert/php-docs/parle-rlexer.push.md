# Adiciona uma regra de análise léxica

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle-rlexer.push.php

---

# Parle\RLexer::push

(PECL parle >= 0.5.1)

Parle\RLexer::push — Adiciona uma regra de análise léxica

### Descrição

public function **Parle\RLexer::push**([string](language.types.string.md) `$regex`, [int](language.types.integer.md) `$id`): [void](language.types.void.md)

public function **Parle\RLexer::push**(  
    [string](language.types.string.md) `$state`,  
    [string](language.types.string.md) `$regex`,  
    [int](language.types.integer.md) `$id`,  
    [string](language.types.string.md) `$newState`  
): [void](language.types.void.md)

public function **Parle\RLexer::push**([string](language.types.string.md) `$state`, [string](language.types.string.md) `$regex`, [string](language.types.string.md) `$newState`): [void](language.types.void.md)

Insere na pilha um padrão de reconhecimento de lexema.

Um 'estado inicial' e um 'estado de saída' podem ser especificados usando uma assinatura adequada.

### Parâmetros

`regex`
:   Expressão regular usada para correspondência de tokens.

`id`
:   ID do token. Se a instância do analisador léxico for destinada a ser usada de forma independente, este pode ser um número arbitrário. Se a instância do analisador léxico for passada para o analisador, deve ser um ID retornado por [Parle\RParser::tokenid()](parle-rparser.tokenid.md).

`state`
:   Nome do estado. Se '\*' for usado como estado inicial, a regra será aplicada a todos os estados do analisador léxico.

`newState`
:   Novo nome do estado, após a aplicação da regra.

    Se "." for especificado como o estado de saída, o estado do analisador léxico permanecerá inalterado quando essa regra corresponder. Um estado de saída com ">" antes do nome significa push. Use a assinatura sem ID para continuação ou para iniciar a correspondência, quando uma continuação ou recursão for necessária.

    Se '<' for especificado como estado de saída, significa remoção da pilha. Nesse caso, a assinatura contendo o ID pode ser usada para identificar a correspondência. Observe que, mesmo que um ID seja especificado, a regra será encerrada primeiro quando todos as inserções de pilha anteriores forem removidas.

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
