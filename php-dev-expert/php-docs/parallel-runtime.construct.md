# Construção de Runtime

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-runtime.construct.php

---

# parallel\Runtime::\_\_construct

(0.8.0)

parallel\Runtime::\_\_construct — Construção de Runtime

### Descrição

public function **parallel\Runtime::\_\_construct**()

Contrói um novo Runtime sem inicialização.

public function **parallel\Runtime::\_\_construct**([string](language.types.string.md) `$bootstrap`)

Contrói um novo Runtime com inicialização.

### Parâmetros

`bootstrap`
:   A localização de um arquivo de inicialização, geralmente um carregador automático.

### Exceptions

**Aviso**

Lança uma exceção parallel\Runtime\Error se a thread não puder ser criada.

**Aviso**

Lança uma exceção parallel\Runtime\Bootstrap se a inicialização falhar.

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
