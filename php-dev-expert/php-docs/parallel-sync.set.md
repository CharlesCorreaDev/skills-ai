# Acesso

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-sync.set.php

---

# parallel\Sync::set

(1.1.0)

parallel\Sync::set — Acesso

### Descrição

public function **parallel\Sync::set**(scalar `$value`)

Define atomicamente o valor do objeto de sincronização.

### Exceptions

**Aviso**

Lança uma exceção parallel\Sync\Error\IllegalValue se `value` não for escalar.

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
