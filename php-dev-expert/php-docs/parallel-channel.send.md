# Compartilhamento

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-channel.send.php

---

# parallel\Channel::send

(0.9.0)

parallel\Channel::send — Compartilhamento

### Descrição

public function **parallel\Channel::send**([mixed](language.types.mixed.md) `$value`): [void](language.types.void.md)

Envia neste canal o valor informado.

### Exceptions

**Aviso**

Lança uma exceção parallel\Channel\Error\Closed se o canal estiver fechado.

**Aviso**

Lança uma exceção parallel\Channel\Error\IllegalValue se o valor for ilegal.

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
