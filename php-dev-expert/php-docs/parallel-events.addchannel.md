# Alvos

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-events.addchannel.php

---

# parallel\Events::addChannel

(0.9.0)

parallel\Events::addChannel — Alvos

### Descrição

public function **parallel\Events::addChannel**([parallel\Channel](class.parallel-channel.md) `$channel`): [void](language.types.void.md)

Observa eventos no canal informado em `channel`.

### Exceptions

**Aviso**

Lança uma exceção parallel\Events\Error\Existence se o canal já tiver sido adicionado.

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
