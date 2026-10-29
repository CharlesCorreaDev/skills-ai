# Instalação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/odbc.installation.php

---

## Instalação

**--with-adabas[=DIR]**
:   Inclui suporte a Adabas D. DIR é o diretório base da instalação do Adabas,
    o padrão é /usr/local.

**--with-sapdb[=DIR]**
:   Inclui suporte a SAP DB. DIR é o diretório base SAP DB,
    o padrão é /usr/local.

**--with-solid[=DIR]**
:   Inclui o suporte Solid. DIR é o diretório base da instalação Solid,
    o padrão é /usr/local/solid.

**--with-ibm-db2[=DIR]**
:   Inclui suporte ao IBM DB2. DIR é o diretório base da instalaçação do DB2,
    o padrão é /home/db2inst1/sqllib.

**--with-empress[=DIR]**
:   Inclui suporte a Empress. DIR é o diretório base da instalação do Empress,
    o padrão é $EMPRESSPATH. Esta
    opção suporta apenas o Empress Versão 8.60 e posteriores.

**--with-empress-bcs[=DIR]**
:   Inclui suporte a `"Empress Local Access"`. DIR é o diretório base da
    instalação do Empress, o padrão é $EMPRESSPATH.
    Esta opção suporta apenas o Empress Version 8.60 e posteriores.

**--with-birdstep[=DIR]**
:   Inclui suporte Birdstep. DIR é o diretório base da instalação do Birdstep,
    o padrão é /usr/local/birdstep.

**--with-custom-odbc[=DIR]**
:   Inclui um suporte ODBC definido pelo usuário. DIR é o diretório base da instalação do ODBC,
    o padrão é /usr/local. Tenha certeza de definir
    CUSTOM\_ODBC\_LIBS e ter algum odbc.h nos seus diretórios
    de inclusão. Ex., você deve definir o seguinte para Sybase SQL Anywhere 5.5.00 no
    QNX, antes de executar o script "configure":

    ```
       CPPFLAGS="-DODBC_QNX -DSQLANY_BUG"
       LDFLAGS=-lunix
       CUSTOM_ODBC_LIBS="-ldblib -lodbc".
    ```

**--with-iodbc[=DIR]**
:   Inclui o suporte a iODBC. DIR é o diretório base da instalação do iODBC,
    o pardrão é /usr/local.

**--with-esoob[=DIR]**
:   Inclui suporte a Easysoft OOB. DIR é o diretório base da instalação OOB,
    o padrão é /usr/local/easysoft/oob/client.

**--with-unixODBC[=DIR]**
:   Inclui suporte a unixODBC. DIR é o diretório base da instalação unixODBC,
    o padrão é /usr/local.

**--with-openlink[=DIR]**
:   Inclui suporte a OpenLink ODBC. DIR é o diretório base da instalação do OpenLink,
    o padrão é /usr/local. Este é o mesmo que iODBC.

**--with-dbmaker[=DIR]**
:   Inclui suporte a DBMaker. DIR é o diretório base da instalação do DBMaker,
    o padrão é o local da instalação mais recente do DBMaker
    (algo como /home/dbmaker/3.6).

Usuários do Windows precisam habilitar a
php\_odbc.dll para usar esta extensão.

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
