# Configurações de Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.configuration.php

---

## Configurações de Execução

O comportamento destas funções é afetado pelas configurações do php.ini.

**Opções de Configuração do PDO**

| Nome | Padrão | Modificável | Registro de Alterações |
| --- | --- | --- | --- |
| [pdo.dsn.\*](pdo.configuration.md#ini.pdo.dsn) |  | Somente php.ini |  |

Aqui está uma breve explicação das
diretivas de configuração.

`pdo.dsn.*` [string](language.types.string.md)
:   Define um sinônimo DSN. Veja [PDO::\_\_construct()](pdo.construct.md) para
    uma explicação completa.

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
