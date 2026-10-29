# Constantes predefinidas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.constants.php

---

# Constantes predefinidas

## Índice

- [Modos de Busca](pdo.constants.fetch-modes.md)

As constantes abaixo são definidas por esta extensão e
só estarão disponíveis quando a extensão tiver sido compilada no PHP
ou tiver sido carregada dinamicamente em tempo de execução.

## Cursores

Veja também **`PDO::ATTR_CURSOR_NAME`**.

**`PDO::FETCH_ORI_NEXT`** ([int](language.types.integer.md))
:   Busca a próxima linha no conjunto de resultados. Válido apenas para cursores roláveis.

**`PDO::FETCH_ORI_PRIOR`** ([int](language.types.integer.md))
:   Busca a linha anterior no conjunto de resultados. Válido apenas para
    cursores roláveis.

**`PDO::FETCH_ORI_FIRST`** ([int](language.types.integer.md))
:   Busca a primeira linha no conjunto de resultados. Válido apenas para cursores roláveis.

**`PDO::FETCH_ORI_LAST`** ([int](language.types.integer.md))
:   Busca a última linha no conjunto de resultados. Válido apenas para cursores roláveis.

**`PDO::FETCH_ORI_ABS`** ([int](language.types.integer.md))
:   Busca a linha solicitada pelo número da linha do conjunto de resultados. Válida somente
    para cursores roláveis.

**`PDO::FETCH_ORI_REL`** ([int](language.types.integer.md))
:   Busca a linha solicitada pela posição relativa à posição atual
    do cursor no conjunto de resultados. Válida somente para cursores roláveis.

**`PDO::CURSOR_FWDONLY`** ([int](language.types.integer.md))
:   Cria um objeto [PDOStatement](class.pdostatement.md) com um cursor somente para frente. Esta é a
    escolha de cursor padrão, pois é o padrão mais rápido e comum de acesso a
    dados em PHP.

**`PDO::CURSOR_SCROLL`** ([int](language.types.integer.md))
:   Cria um objeto [PDOStatement](class.pdostatement.md) com um cursor rolável.
    Passe as constantes **`PDO::FETCH_ORI_*`**
    para controlar as linhas buscadas do conjunto de resultados.

## Outras constantes

**`PDO::PARAM_BOOL`** ([int](language.types.integer.md))
:   Representa um tipo de dado booleano.

**`PDO::PARAM_NULL`** ([int](language.types.integer.md))
:   Representa o tipo de dado SQL NULL.

**`PDO::PARAM_INT`** ([int](language.types.integer.md))
:   Representa o tipo de dados SQL INTEGER.

**`PDO::PARAM_STR`** ([int](language.types.integer.md))
:   Representa o tipo de dados SQL CHAR, VARCHAR ou outra string.

**`PDO::PARAM_STR_NATL`** ([int](language.types.integer.md))
:   Sinaliza que uma string usa o conjunto de caracteres nacional.

    Disponível a partir do PHP 7.2.0

**`PDO::PARAM_STR_CHAR`** ([int](language.types.integer.md))
:   Sinaliza que uma string usa o conjunto de caracteres regular.

    Disponível a partir do PHP 7.2.0

**`PDO::PARAM_LOB`** ([int](language.types.integer.md))
:   Representa o tipo de dados SQL large object.

**`PDO::PARAM_STMT`** ([int](language.types.integer.md))
:   Representa um tipo de conjunto de registros. Atualmente não suportado por nenhum driver.

**`PDO::PARAM_INPUT_OUTPUT`** ([int](language.types.integer.md))
:   Especifica que o parâmetro é um parâmetro INOUT para um
    procedimento armazenado. Esse valor deve ser combinado através de OR binário com uma das constantes
    **`PDO::PARAM_*`**.

**`PDO::ATTR_AUTOCOMMIT`** ([bool](language.types.boolean.md))
:   Se esse valor for **`false`**, o PDO tenta desativar o autocommit para que a
    conexão inicie uma transação.

    A partir do PHP 8.4.0, esta constante é tipada como [bool](language.types.boolean.md);
    anteriormente, era tipada como [int](language.types.integer.md).

**`PDO::ATTR_PREFETCH`** ([int](language.types.integer.md))
:   Definir o tamanho da pré-busca permite balancear entre velocidade e uso de memória
    em uma aplicação. Nem todas as combinações de banco de dados e drivers suportam
    a definição do tamanho do pré-busca. Um tamanho de pré-busca maior resulta em
    um aumento de desempenho com o custo de um uso maior de memória.

    O driver PDO\_PGSQL, por sua vez, trata esse atributo como uma opção: a partir do PHP 8.5.0,
    o valor `0` habilita a busca lenta (linha única);
    consulte a
    [documentação do driver PDO\_PGSQL](class.pdo-pgsql.md#pdo-pgsql.constants.attr-prefetch)
    para obter detalhes.

**`PDO::ATTR_TIMEOUT`** ([int](language.types.integer.md))
:   Define o valor de tempo limite em segundos para comunicações com o banco de dados.

**`PDO::ATTR_ERRMODE`** ([int](language.types.integer.md))
:   Consulte a seção [Erros e tratamento de
    erros](pdo.error-handling.md) para obter mais informações sobre este atributo.

**`PDO::ATTR_SERVER_VERSION`** ([int](language.types.integer.md))
:   Este é um atributo somente leitura; ele retornará informações sobre a
    versão do servidor de banco de dados ao qual o PDO está conectado.

**`PDO::ATTR_CLIENT_VERSION`** ([int](language.types.integer.md))
:   Este é um atributo somente leitura; ele retornará informações sobre a
    versão das bibliotecas de cliente que o driver PDO está usando.

**`PDO::ATTR_SERVER_INFO`** ([int](language.types.integer.md))
:   Este é um atributo somente leitura; ele retornará algumas informações meta sobre o
    servidor de banco de dados ao qual o PDO está conectado.

**`PDO::ATTR_CONNECTION_STATUS`** ([int](language.types.integer.md))

**`PDO::ATTR_CASE`** ([int](language.types.integer.md))
:   Força os nomes das colunas para um caso específico
    definido pelas constantes
    **`PDO::CASE_*`**.

**`PDO::ATTR_CURSOR_NAME`** ([int](language.types.integer.md))
:   Obtém ou define o nome a ser usado para um cursor. Mais útil ao usar
    cursores roláveis e atualizações posicionadas.

**`PDO::ATTR_CURSOR`** ([int](language.types.integer.md))
:   Seleciona o tipo de cursor. O PDO atualmente suporta
    **`PDO::CURSOR_FWDONLY`** ou
    **`PDO::CURSOR_SCROLL`**.
    A menos que haja necessidade de cursores roláveis, deve-se usar
    o modo de cursor **`PDO::CURSOR_FWDONLY`**.

**`PDO::ATTR_DRIVER_NAME`** ([int](language.types.integer.md))
:   Retorna o nome do driver.

    **Exemplo #1 using **`PDO::ATTR_DRIVER_NAME`****

    ```
    <?php
     if ($db->getAttribute(PDO::ATTR_DRIVER_NAME) == 'mysql') {
       echo "Running on mysql; doing something mysql specific here\n";
     }
     ?>
    ```

**`PDO::ATTR_ORACLE_NULLS`** ([int](language.types.integer.md))
:   Converte strings vazias em valores SQL NULL em buscas de dados.

**`PDO::ATTR_PERSISTENT`** ([int](language.types.integer.md))
:   Solicita uma conexão persistente, em vez de criar uma nova conexão.
    Consulte [Conexões e Gerenciamento de
    Conexões](pdo.connections.md) para obter mais informações sobre este atributo.

**`PDO::ATTR_STATEMENT_CLASS`** ([int](language.types.integer.md))
:   Define o nome da classe e os argumentos do construtor para a extensão do
    objeto [PDOStatement](class.pdostatement.md). O primeiro
    elemento do array é o nome da classe, e o segundo elemento é um
    array de argumentos do construtor.

**`PDO::ATTR_FETCH_CATALOG_NAMES`** ([int](language.types.integer.md))
:   Adiciona o nome do catálogo contenedor a cada nome de coluna retornado no
    conjunto de resultados. O nome do catálogo e o nome da coluna são separados por um caractere
    de ponto (.). O suporte deste atributo é no nível do driver; pode não
    ser suportado pelo driver em uso.

**`PDO::ATTR_FETCH_TABLE_NAMES`** ([int](language.types.integer.md))
:   Adiciona o nome da tabela contenedora a cada nome de coluna retornado no
    conjunto de resultados. O nome da tabela e o nome da coluna são separados por um caractere
    de ponto (.). O suporte deste atributo é no nível do driver; pode
    não ser suportado pelo driver em uso.

**`PDO::ATTR_STRINGIFY_FETCHES`** ([int](language.types.integer.md))
:   Força todos os valores buscados (exceto **`null`**) a serem tratados como strings.
    Valores **`null`** permanecem inalterados a menos que **`PDO::ATTR_ORACLE_NULLS`**
    esteja definida para **`PDO::NULL_TO_STRING`**.

**`PDO::ATTR_MAX_COLUMN_LEN`** ([int](language.types.integer.md))
:   Define o comprimento máximo do nome da coluna.

**`PDO::ATTR_DEFAULT_FETCH_MODE`** ([int](language.types.integer.md))

**`PDO::ATTR_EMULATE_PREPARES`** ([bool](language.types.boolean.md))
:   Se deve habilitar ou desabilitar a emulação de instruções preparadas.
    Alguns drivers não suportam instruções preparadas nativas ou têm suporte
    apenas limitado a elas. Quando definido como **`true`**, o PDO sempre emula
    instruções preparadas; quando definido como **`false`**, ele usa as
    instruções preparadas nativas do driver.

    A partir do PHP 8.4.0, esta constante é tipada como [bool](language.types.boolean.md);
    anteriormente, era tipada como [int](language.types.integer.md).

**`PDO::ATTR_DEFAULT_STR_PARAM`** ([int](language.types.integer.md))
:   Define o tipo de parâmetro de string padrão, que pode ser uma
    das constantes **`PDO::PARAM_STR_NATL`**
    ou **`PDO::PARAM_STR_CHAR`**.

    Disponível a partir do PHP 7.2.0.

**`PDO::ERRMODE_SILENT`** ([int](language.types.integer.md))
:   Não gera um erro ou exceção se ocorrer um erro.
    É esperado que o próprio desenvolvedor verifique explicitamente os erros.
    Anteriormente ao PHP 8.0.0, este era o modo padrão.
    Consulte [Erros e tratamento de erros](pdo.error-handling.md)
    para mais informações sobre este atributo.

**`PDO::ERRMODE_WARNING`** ([int](language.types.integer.md))
:   Emite uma mensagem PHP **`E_WARNING`** se ocorrer um erro.
    Consulte [Erros e tratamento de erros](pdo.error-handling.md)
    para mais informações sobre este atributo.

**`PDO::ERRMODE_EXCEPTION`** ([int](language.types.integer.md))
:   Lança uma [PDOException](class.pdoexception.md) se ocorrer um erro.
    Este é o modo padrão a partir do PHP 8.0.0.
    Consulte [Erros e tratamento de erros](pdo.error-handling.md)
    para mais informações sobre este atributo.

**`PDO::CASE_NATURAL`** ([int](language.types.integer.md))
:   Deixa os nomes das colunas como retornados pelo driver do banco de dados.

**`PDO::CASE_LOWER`** ([int](language.types.integer.md))
:   Força os nomes das colunas em minúsculas.

**`PDO::CASE_UPPER`** ([int](language.types.integer.md))
:   Força os nomes das colunas em maiúsculas.

**`PDO::NULL_NATURAL`** ([int](language.types.integer.md))

**`PDO::NULL_EMPTY_STRING`** ([int](language.types.integer.md))

**`PDO::NULL_TO_STRING`** ([int](language.types.integer.md))

**`PDO::ERR_NONE`** ([string](language.types.string.md))
:   Corresponde a SQLSTATE `'00000'`, significando que a instrução SQL foi
    emitida com sucesso sem erros ou avisos.
    Esta constante é uma conveniência ao verificar
    [PDO::errorCode()](pdo.errorcode.md) ou
    [PDOStatement::errorCode()](pdostatement.errorcode.md) para determinar se ocorreu
    um erro.
    De qualquer forma, isto geralmente é determinado pela verificação do código de retorno do método
    que gerou a condição de erro.

**`PDO::PARAM_EVT_ALLOC`** ([int](language.types.integer.md))
:   Evento de alocação

**`PDO::PARAM_EVT_FREE`** ([int](language.types.integer.md))
:   Evento de desalocação

**`PDO::PARAM_EVT_EXEC_PRE`** ([int](language.types.integer.md))
:   Evento acionado antes da execução de uma instrução preparada.

**`PDO::PARAM_EVT_EXEC_POST`** ([int](language.types.integer.md))
:   Evento acionado após a execução de uma instrução preparada.

**`PDO::PARAM_EVT_FETCH_PRE`** ([int](language.types.integer.md))
:   Evento acionado antes de buscar um resultado de um conjunto de resultados.

**`PDO::PARAM_EVT_FETCH_POST`** ([int](language.types.integer.md))
:   Evento acionado após buscar um resultado de um conjunto de resultados.

**`PDO::PARAM_EVT_NORMALIZE`** ([int](language.types.integer.md))
:   Evento acionado durante o registro de parâmetro vinculado,
    permitindo ao driver normalizar o nome do parâmetro.

**`PDO::SQLITE_DETERMINISTIC`** ([int](language.types.integer.md))
:   **Aviso**

    Esta constante foi *DESCONTINUADA* a partir do PHP 8.5.0.
    Use **`Pdo\Sqlite::DETERMINISTIC`** em seu lugar.

    Especifica que uma função criada com [PDO::sqliteCreateFunction()](pdo.sqlitecreatefunction.md)
    é determinística, ou seja, ela sempre retorna o mesmo resultado dados os mesmos inputs dentro
    de uma única instrução SQL. (Disponível a partir do PHP 7.1.4.)

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
