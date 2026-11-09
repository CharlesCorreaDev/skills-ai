# Construção

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-sync.construct.php

---

# parallel\Sync::\_\_construct

(1.1.0)

parallel\Sync::\_\_construct — Construção

### Descrição

public function **parallel\Sync::\_\_construct**()

Constrói um novo objeto de sincronização sem nenhum valor.

public function **parallel\Sync::\_\_construct**(scalar `$value`)

Constrói um novo objeto de sincronização contendo o valor escalar fornecido.

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
