# Configurações de Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/odbc.configuration.php

---

## Configurações de Execução

O comportamento destas funções é afetado pelas configurações do php.ini.

**Opções de configuração de Unified ODBC**

| Nome | Padrão | Modificável | Registro de Alterações |
| --- | --- | --- | --- |
| [odbc.allow\_persistent](odbc.configuration.md#ini.uodbc.allow-persistent) | "1" | **`INI_SYSTEM`** |  |
| [odbc.check\_persistent](odbc.configuration.md#ini.uodbc.check-persistent) | "1" | **`INI_SYSTEM`** |  |
| [odbc.max\_persistent](odbc.configuration.md#ini.uodbc.max-persistent) | "-1" | **`INI_SYSTEM`** |  |
| [odbc.max\_links](odbc.configuration.md#ini.uodbc.max-links) | "-1" | **`INI_SYSTEM`** |  |
| [odbc.defaultlrl](odbc.configuration.md#ini.uodbc.defaultlrl) | "4096" | **`INI_ALL`** |  |
| [odbc.defaultbinmode](odbc.configuration.md#ini.uodbc.defaultbinmode) | "1" | **`INI_ALL`** |  |
| [odbc.default\_cursortype](odbc.configuration.md#ini.uodbc.defaultcursortype) | "3" | **`INI_ALL`** |  |

Para mais detalhes e definições dos modos
INI\_\*, consulte os [Onde uma configuração deve ser definida](configuration.changes.modes.md).

Aqui está uma breve explicação das
diretivas de configuração.

`odbc.default_db` [string](language.types.string.md)
:   Fonte de dados ODBC que será usada se nenhuma for especificada em
    [odbc\_connect()](function.odbc-connect.md) ou
    [odbc\_pconnect()](function.odbc-pconnect.md).

`odbc.default_user` [string](language.types.string.md)
:   Nome de usuário que será usado se nenhum for especificado em
    [odbc\_connect()](function.odbc-connect.md) ou
    [odbc\_pconnect()](function.odbc-pconnect.md).

`odbc.default_pw` [string](language.types.string.md)
:   Senha que será usada se nenhuma for especificada em
    [odbc\_connect()](function.odbc-connect.md) ou
    [odbc\_pconnect()](function.odbc-pconnect.md).

`odbc.allow_persistent` [bool](language.types.boolean.md)
:   Define se serão permitidas conexões ODBC persistentes.

`odbc.check_persistent` [bool](language.types.boolean.md)
:   Verifica se uma conexão ainda está válida antes de seu reúso.

`odbc.max_persistent` [int](language.types.integer.md)
:   O número máximo de conexões ODBC persistentes por processo.

`odbc.max_links` [int](language.types.integer.md)
:   O número máximo de conexões ODBC por processo, incluindo
    conexões persistentes.

`odbc.defaultlrl` [int](language.types.integer.md)
:   Manipulação de campos LONG. Especifica o número de bytes retornados às
    variáveis.
    Veja [odbc\_longreadlen()](function.odbc-longreadlen.md) para detalhes.

    Quando um [int](language.types.integer.md) é usado, o
    valor é medido em bytes. A notação abreviada, como descrita
    [nesta FAQ](faq.using.md#faq.using.shorthandbytes), também pode ser usada.

`odbc.defaultbinmode` [int](language.types.integer.md)
:   Manipulação de dados binários.
    Veja [odbc\_binmode()](function.odbc-binmode.md) para detalhes.

`odbc.default_cursortype` [int](language.types.integer.md)
:   Controla o modelo de cursor ODBC.
    Valores possíveis são **`SQL_CURSOR_FORWARD_ONLY`**,
    **`SQL_CURSOR_KEYSET_DRIVEN`**,
    **`SQL_CURSOR_DYNAMIC`** e
    **`SQL_CURSOR_STATIC`** (padrão).

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
