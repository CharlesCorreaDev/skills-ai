# Configurações de Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pgsql.configuration.php

---

## Configurações de Execução

O comportamento destas funções é afetado pelas configurações do php.ini.

**Opções de configuração PostgreSQL**

| Nome | Padrão | Modificável | Registro de Alterações |
| --- | --- | --- | --- |
| [pgsql.allow\_persistent](pgsql.configuration.md#ini.pgsql.allow-persistent) | "1" | **`INI_SYSTEM`** |  |
| [pgsql.max\_persistent](pgsql.configuration.md#ini.pgsql.max-persistent) | "-1" | **`INI_SYSTEM`** |  |
| [pgsql.max\_links](pgsql.configuration.md#ini.pgsql.max-links) | "-1" | **`INI_SYSTEM`** |  |
| [pgsql.auto\_reset\_persistent](pgsql.configuration.md#ini.pgsql.auto-reset-persistent) | "0" | **`INI_SYSTEM`** |  |
| [pgsql.ignore\_notice](pgsql.configuration.md#ini.pgsql.ignore-notice) | "0" | **`INI_ALL`** |  |
| [pgsql.log\_notice](pgsql.configuration.md#ini.pgsql.log-notice) | "0" | **`INI_ALL`** |  |

Para mais detalhes e definições dos modos
INI\_\*, consulte os [Onde uma configuração deve ser definida](configuration.changes.modes.md).

Aqui está uma breve explicação das
diretivas de configuração.

`pgsql.allow_persistent` [bool](language.types.boolean.md)
:   Define se serão permitidas conexões Postgres persistentes.

`pgsql.max_persistent` [int](language.types.integer.md)
:   O número máximo de conexões Postgres persistentes por
    processo.

`pgsql.max_links` [int](language.types.integer.md)
:   O número máximo de conexões Postgres por processo,
    incluindo conexões persistentes.

`pgsql.auto_reset_persistent` [int](language.types.integer.md)
:   Detecta conexões persistentes quebradas com [pg\_pconnect()](function.pg-pconnect.md).
    Precisa de um pequeno oberhead.

`pgsql.ignore_notice` [int](language.types.integer.md)
:   Define se as notas do processo interno do PostgreSQL devem ser ignoradas.

`pgsql.log_notice` [int](language.types.integer.md)
:   Define se as mensagens e notas do processo interno do PostgreSQL serão registradas. A diretiva
    do PHP [pgsql.ignore\_notice](pgsql.configuration.md#ini.pgsql.ignore-notice) deve estar em "Off" para que as mensagens
    sejam registradas.

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
