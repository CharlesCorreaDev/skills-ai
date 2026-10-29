# Define um atributo

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.setattribute.php

---

# PDO::setAttribute

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDO::setAttribute — 
Define um atributo

### Descrição

public function **PDO::setAttribute**([int](language.types.integer.md) `$attribute`, [mixed](language.types.mixed.md) `$value`): [bool](language.types.boolean.md)

Define um atributo no identificador do banco de dados. Alguns atributos genéricos
disponíveis estão listados abaixo; alguns drivers podem fazer uso de
atributos adicionais específicos do driver.
Observe que os atributos específicos do driver *não devem* ser usados
​​com outros drivers.

**`PDO::ATTR_CASE`**
:   Força os nomes das colunas para uma combinação específica de maiúsculas/minúsculas.
    Pode ser um dos seguintes valores:

    **`PDO::CASE_LOWER`**
    :   Força os nomes das colunas para minúsculas.

    **`PDO::CASE_NATURAL`**
    :   Deixa os nomes das colunas como retornados pelo driver do banco de dados.

    **`PDO::CASE_UPPER`**
    :   Força os nomes das colunas para maiúsculas.

**`PDO::ATTR_ERRMODE`**
:   Modo de relatório de erros do PDO.
    Pode ser um dos seguintes valores:

    **`PDO::ERRMODE_SILENT`**
    :   Define somente códigos de erro.

    **`PDO::ERRMODE_WARNING`**
    :   Emite diagnósticos **`E_WARNING`**.

    **`PDO::ERRMODE_EXCEPTION`**
    :   Lança exceções [PDOException](class.pdoexception.md).

**`PDO::ATTR_ORACLE_NULLS`**
:   > **Nota**:
    >
    > Este atributo está disponível em todos os drivers, não somente no Oracle.

    Determina se e como strings **`null`** e vazias devem ser convertidas.
    Pode ser um dos seguintes valores:

    **`PDO::NULL_NATURAL`**
    :   Nenhuma conversão acontece.

    **`PDO::NULL_EMPTY_STRING`**
    :   Strings vazias são convertidas para **`null`**.

    **`PDO::NULL_TO_STRING`**
    :   **`null`** é convertido para uma string vazia.

**`PDO::ATTR_STRINGIFY_FETCHES`**
:   Controla se os valores buscados (exceto **`null`**) são convertidos para strings.
    Aceita um valor do tipo [bool](language.types.boolean.md): **`true`** para habilitar e **`false`** para
    desabilitar (padrão).
    Valores **`null`** permanecem inalterados a menos que **`PDO::ATTR_ORACLE_NULLS`**
    esteja definida para **`PDO::NULL_TO_STRING`**.

**`PDO::ATTR_STATEMENT_CLASS`**
:   Defina a classe de instrução fornecida pelo usuário derivada de PDOStatement.
    Requer `array(string classname, array(mixed constructor_args))`.

    **Cuidado**

    Não pode ser usado com instâncias persistentes de PDO.

**`PDO::ATTR_TIMEOUT`**
:   Especifica a duração do tempo limite em segundos.
    Recebe um valor do tipo [int](language.types.integer.md).

    > **Nota**:
    >
    > Nem todos os drivers suportam esta opção e seu significado pode variar de
    > driver para driver. Por exemplo, o SQLite irá esperar até esse valor de
    > tempo antes de desistir de obter uma trava para escrita, mas outros drivers
    > podem interpretar isso como intervalo de tempo limite de conexão ou de leitura.

**`PDO::ATTR_AUTOCOMMIT`**
:   > **Nota**:
    >
    > Disponível apenas para drivers OCI, Firebird e MySQL.

    Define se cada instrução deve ser confirmada automaticamente.
    Recebe um valor do tipo [bool](language.types.boolean.md): **`true`** para habilitar e
    **`false`** para desabilitar. Por padrão, **`true`**.

**`PDO::ATTR_EMULATE_PREPARES`**
:   > **Nota**:
    >
    > Disponível apenas para drivers OCI, Firebird e MySQL.

    Define se a emulação de instruções preparadas será habilitada ou desabilitada.
    Alguns drivers não oferecem suporte nativo a instruções preparadas ou têm
    suporte limitado para elas.
    Se definido como **`true`** O PDO sempre emulará instruções preparadas,
    caso contrário, o PDO tentará usar instruções preparadas nativas.
    Caso o driver não consiga preparar com êxito a instrução atual,
    o PDO sempre voltará a emular a instrução preparada.

**`PDO::MYSQL_ATTR_USE_BUFFERED_QUERY`**
:   > **Nota**:
    >
    > Disponível apenas para o driver MySQL.

    Define se consultas com buffer devem ser usadas.
    Recebe um valor do tipo [bool](language.types.boolean.md): **`true`** para habilitar e
    **`false`** para desabilitar. Por padrão, **`true`**.

**`PDO::ATTR_DEFAULT_FETCH_MODE`**
:   Define o modo de busca padrão.
    Uma descrição dos modos e de como utilizá-los está disponível na
    documentação do método [PDOStatement::fetch()](pdostatement.fetch.md).

### Parâmetros

`attribute`
:   O atributo a modificar.

`value`
:   O valor para o qual o `attribute` será definido,
    pode requerer um tipo específico dependendo do atributo.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Veja também

- [PDO::getAttribute()](pdo.getattribute.md) - Recuperar um atributo da conexão com o banco de dados
- [PDOStatement::getAttribute()](pdostatement.getattribute.md) - Recupera um atributo da instrução
- [PDOStatement::setAttribute()](pdostatement.setattribute.md) - Define um atributo na instrução

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
