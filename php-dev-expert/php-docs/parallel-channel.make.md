# Construção de canal

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-channel.make.php

---

# parallel\Channel::make

(0.9.0)

parallel\Channel::make — Construção de canal

### Descrição

public function **parallel\Channel::make**([string](language.types.string.md) `$name`): Channel

Constrói um canal sem buffer com o nome informado.

public function **parallel\Channel::make**([string](language.types.string.md) `$name`, [int](language.types.integer.md) `$capacity`): Channel

Constrói um canal sem buffer com o nome e a capacidade informados.

### Parâmetros

`name`
:   O nome do canal.

`capacity`
:   Pode ser Channel::Infinite ou um inteiro positivo.

### Exceptions

**Aviso**

Lança uma exceção parallel\Channel\Error\Existence se o canal já existir.

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
