# Aninhando Buffers de Saída

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.nesting-output-buffers.php

---

## Aninhando Buffers de Saída

Se houver um buffer de saída ativo quando um novo buffer for iniciado,
o novo buffer será aninhado dentro do buffer ativo anteriormente.
O buffer interno se comportará da mesma maneira, independentemente de estar aninhado,
mas a saída armazenada em buffer por ele não será armazenada em buffer pelo buffer externo.
Somente a saída liberada pelo buffer interno será armazenada no buffer externo.

A maioria das funções `ob_*` só funcionam
com o buffer de saída ativo (o último iniciado),
portanto, apenas o buffer ativo pode ser descarregado, limpo e desligado.
As funções que funcionam com outros buffers são
[ob\_list\_handlers()](function.ob-list-handlers.md)
que retorna a lista de todos os manipuladores de saída em uso
e [ob\_get\_status()](function.ob-get-status.md)
que pode retornar informações apenas sobre o buffer ativo
ou sobre todos os buffers em uso .

Chamar [ob\_get\_level()](function.ob-get-level.md)
ou [ob\_get\_status()](function.ob-get-status.md) retornará
o nível de aninhamento do buffer de saída ativo.

**Cuidado**

O valor para níveis idênticos entre [ob\_get\_level()](function.ob-get-level.md)
e [ob\_get\_status()](function.ob-get-status.md) está desfasado em um.
Para [ob\_get\_level()](function.ob-get-level.md)
o primeiro nível é `1`,
enquanto para [ob\_get\_status()](function.ob-get-status.md)
o primeiro nível é `0`.

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
