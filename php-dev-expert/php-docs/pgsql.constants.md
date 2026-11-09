# Constantes predefinidas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pgsql.constants.php

---

# Constantes predefinidas

As constantes abaixo são definidas por esta extensão e
só estarão disponíveis quando a extensão tiver sido compilada no PHP
ou tiver sido carregada dinamicamente em tempo de execução.

**`PGSQL_LIBPQ_VERSION`** ([string](language.types.string.md))
:   Versão curta da libpq, contendo apenas números e pontos.

**`PGSQL_LIBPQ_VERSION_STR`** ([string](language.types.string.md))
:   Antes do PHP 8.0.0, a versão longa da libpq que incluía informação de compilação.
    A partir do PHP 8.0.0, o valor é idêntico a **`PGSQL_LIBPQ_VERSION`**,
    e usar **`PGSQL_LIBPQ_VERSION_STR`** foi descontinuado.

**`PGSQL_ASSOC`** ([int](language.types.integer.md))
:   Usada em [pg\_fetch\_array()](function.pg-fetch-array.md). Retorna um array associativo contendo
    nomes dos campos e valores.

**`PGSQL_NUM`** ([int](language.types.integer.md))
:   Usada em [pg\_fetch\_array()](function.pg-fetch-array.md). Retorna um array com índice numérico contendo
    números dos campos e valores.

**`PGSQL_BOTH`** ([int](language.types.integer.md))
:   Usada em [pg\_fetch\_array()](function.pg-fetch-array.md). Retorna um array dos valores do campos
    com índice numérico (por número do campo) e associativo (por nome do campo).

**`PGSQL_CONNECT_FORCE_NEW`** ([int](language.types.integer.md))
:   Usado em [pg\_connect()](function.pg-connect.md) para forçar a criação de nova conexão,
    ao invés de reutilizar uma conexão idêntica existente.

**`PGSQL_CONNECT_ASYNC`** ([int](language.types.integer.md))
:   Passada para [pg\_connect()](function.pg-connect.md) para criar uma conexão
    assíncrona.

**`PGSQL_CONNECTION_AUTH_OK`** ([int](language.types.integer.md))

**`PGSQL_CONNECTION_AWAITING_RESPONSE`** ([int](language.types.integer.md))

**`PGSQL_CONNECTION_BAD`** ([int](language.types.integer.md))
:   Retornado pela [pg\_connection\_status()](function.pg-connection-status.md) indicando que a conexão
    com o banco de dados está em um estado inválido.

**`PGSQL_CONNECTION_MADE`** ([int](language.types.integer.md))

**`PGSQL_CONNECTION_OK`** ([int](language.types.integer.md))
:   Retornado pela [pg\_connection\_status()](function.pg-connection-status.md) indicando que a conexão
    com o banco de dados está em um estado válido.

**`PGSQL_CONNECTION_SETENV`** ([int](language.types.integer.md))

**`PGSQL_CONNECTION_SSL_STARTUP`** ([int](language.types.integer.md))

**`PGSQL_CONNECTION_STARTED`** ([int](language.types.integer.md))

**`PGSQL_SEEK_SET`** ([int](language.types.integer.md))
:   Passada para [pg\_lo\_seek()](function.pg-lo-seek.md). Operação de pesquisa deve iniciar
    a partir do início do objeto.

**`PGSQL_SEEK_CUR`** ([int](language.types.integer.md))
:   Passada para [pg\_lo\_seek()](function.pg-lo-seek.md). Operação de pesquisa deve iniciar
    a partir da posição atual.

**`PGSQL_SEEK_END`** ([int](language.types.integer.md))
:   Passada para [pg\_lo\_seek()](function.pg-lo-seek.md). Operação de pesquisa deve iniciar
    a partir do final do objeto.

**`PGSQL_EMPTY_QUERY`** ([int](language.types.integer.md))
:   Retornado pela [pg\_result\_status()](function.pg-result-status.md). A string enviada para o servidor
    estava vazia.

**`PGSQL_COMMAND_OK`** ([int](language.types.integer.md))
:   Retornado pela [pg\_result\_status()](function.pg-result-status.md). Conclusão bem sucedida de um
    comando que não retornou dados.

**`PGSQL_TUPLES_OK`** ([int](language.types.integer.md))
:   Retornado pela [pg\_result\_status()](function.pg-result-status.md).Conclusão bem sucedida de um
    retornando dados (como um `SELECT` ou `SHOW`).

**`PGSQL_TUPLES_CHUNK`** ([int](language.types.integer.md))
:   Retornada por [pg\_result\_status()](function.pg-result-status.md).
    Indica o término bem sucedido de um comando que retorna dados em modo fragmentado.
    Retornada para instruções `SELECT` quando
    [pg\_set\_chunked\_rows\_size()](function.pg-set-chunked-rows-size.md) está definida.
    O conjunto de resultados é dividido em múltiplos fragmentos, cada um contendo um número predefinido de linhas.
    Disponível a partir do PHP 8.4.0 e libpq 17.

**`PGSQL_COPY_OUT`** ([int](language.types.integer.md))
:   Retornado pela [pg\_result\_status()](function.pg-result-status.md). Transferência de dados "Copy Out"
    (do servidor) iniciada.

**`PGSQL_COPY_IN`** ([int](language.types.integer.md))
:   Retornado pela [pg\_result\_status()](function.pg-result-status.md). Transferência de dados "Copy In"
    (para o servidor) iniciada.

**`PGSQL_BAD_RESPONSE`** ([int](language.types.integer.md))
:   Retornado pela [pg\_result\_status()](function.pg-result-status.md). A resposta do servidor
    não foi entendida.

**`PGSQL_NONFATAL_ERROR`** ([int](language.types.integer.md))
:   Retornado pela [pg\_result\_status()](function.pg-result-status.md). Um erro não fatal
    (uma nota ou alerta) ocorreu.

**`PGSQL_FATAL_ERROR`** ([int](language.types.integer.md))
:   Retornado pela [pg\_result\_status()](function.pg-result-status.md). Um erro fatal
    ocorreu.

**`PGSQL_TRANSACTION_IDLE`** ([int](language.types.integer.md))
:   Retornado pela [pg\_transaction\_status()](function.pg-transaction-status.md). Conexão está
    atualmente ociosa, não em uma transação.

**`PGSQL_TRANSACTION_ACTIVE`** ([int](language.types.integer.md))
:   Retornado pela [pg\_transaction\_status()](function.pg-transaction-status.md). Um comando
    está em progresso na conexão. Uma consulta foi enviada pela conexão
    e ainda não foi concluída.

**`PGSQL_TRANSACTION_INTRANS`** ([int](language.types.integer.md))
:   Retornado pela [pg\_transaction\_status()](function.pg-transaction-status.md). A conexão
    está ociosa, em um bloco de transação.

**`PGSQL_TRANSACTION_INERROR`** ([int](language.types.integer.md))
:   Retornado pela [pg\_transaction\_status()](function.pg-transaction-status.md). A conexão
    está ociosa, em um bloco de transação com falha.

**`PGSQL_TRANSACTION_UNKNOWN`** ([int](language.types.integer.md))
:   Retornado pela [pg\_transaction\_status()](function.pg-transaction-status.md). A conexão
    está ruim.

**`PGSQL_DIAG_SEVERITY`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    A severidade; os conteúdos dos campos são `ERROR`,
    `FATAL` ou `PANIC` (em uma mensagem de erro); ou
    `WARNING`, `NOTICE`, `DEBUG`,
    `INFO` ou `LOG` (em uma nota), ou uma
    tradução de um desses. Sempre presente.

**`PGSQL_DIAG_SQLSTATE`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    O código SQLSTATE do erro. O código SQLSTATE identifica o tipo do erro
    ocorrido; ele pode ser usado por aplicações front-end para executar operações
    específicas (como manipulação de erro) em resposta a um erro particular do banco de dados.
    Esta campo não muda com a localidade, e está sempre presente.

**`PGSQL_DIAG_MESSAGE_PRIMARY`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    A mensagem de erro legível primária (tipicamente uma linha). Sempre presente.

**`PGSQL_DIAG_MESSAGE_DETAIL`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    Detalhe: uma mensagem de erro secundária trazendo mais detalhes sobre o problema. Pode conter múltiplas linhas.

**`PGSQL_DIAG_MESSAGE_HINT`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    Dica: um sugestão opcional sobre o que fazer em relação ao problema. Tem a intenção de ser diferente da mensagem detalhada
    de forma a oferecer conselhos (potencialmente inapropriados) ao invés de fatos concretos. Pode conter múltiplas linhas.

**`PGSQL_DIAG_STATEMENT_POSITION`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    Uma string contendo um inteiro decimal indicando uma posição de cursor de erro como um índice da string
    da declaração original. O primeiro caractere tem índice 1, e as posições são medidas em caracteres, não em bytes.

**`PGSQL_DIAG_INTERNAL_POSITION`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    Esta é definida da mesma forma que o campo **`PG_DIAG_STATEMENT_POSITION`**, mas
    ela é usado quando a posição do cursor refere-se a um comando gerado internamente
    ao invés do enviado pelo cliente. O campo
    **`PG_DIAG_INTERNAL_QUERY`** irá sempre aparecer quando este
    campo aparecer.

**`PGSQL_DIAG_INTERNAL_QUERY`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    O texto do comando gerado internamente que falhou. Poderá ser, por exemplo, uma
    consulta SQL emitida por uma função PL/pgSQL.

**`PGSQL_DIAG_CONTEXT`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    Um indicador de contexto no qual o erro ocorreu. Atualmente
    isto inclui um restreamento de pilha de chamadas de funções de linguagem
    procedural ativas e consultas geradas internamente. O rastreamento é uma entrada
    por linha, a mais recente primeiro.

**`PGSQL_DIAG_SOURCE_FILE`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    O nome do arquivo da localização do código-fonte PostgreSQL onde o
    erro foi reportado.

**`PGSQL_DIAG_SOURCE_LINE`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    O número da linha da localização do código-fonte PostgreSQL onde o
    erro foi reportado.

**`PGSQL_DIAG_SOURCE_FUNCTION`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_error\_field()](function.pg-result-error-field.md).
    O nome da função do código-fonte PostgreSQL que reportou o erro.

**`PGSQL_DIAG_SCHEMA_NAME`** ([int](language.types.integer.md))
:   Disponível desde o PHP 7.3.0.

**`PGSQL_DIAG_TABLE_NAME`** ([int](language.types.integer.md))
:   Disponível desde o PHP 7.3.0.

**`PGSQL_DIAG_COLUMN_NAME`** ([int](language.types.integer.md))
:   Disponível desde o PHP 7.3.0.

**`PGSQL_DIAG_DATATYPE_NAME`** ([int](language.types.integer.md))
:   Disponível desde o PHP 7.3.0.

**`PGSQL_DIAG_CONSTRAINT_NAME`** ([int](language.types.integer.md))
:   Disponível desde o PHP 7.3.0.

**`PGSQL_ERRORS_TERSE`** ([int](language.types.integer.md))
:   Passada para [pg\_set\_error\_verbosity()](function.pg-set-error-verbosity.md).
    Especifica que a mensagem retornada inclui severidade, texto primário
    e posição somente; normalmente em uma única linha.

**`PGSQL_ERRORS_DEFAULT`** ([int](language.types.integer.md))
:   Passada para [pg\_set\_error\_verbosity()](function.pg-set-error-verbosity.md).
    O modo padrão produz mensagens que incluem as informações do campo acima mais
    algum detalhe, dica, ou campos de contexto (estes podem ter
    múltiplas linhas).

**`PGSQL_ERRORS_VERBOSE`** ([int](language.types.integer.md))
:   Passada para [pg\_set\_error\_verbosity()](function.pg-set-error-verbosity.md).
    Este modo prolixo inclui todos os campos disponíveis.

**`PGSQL_ERRORS_SQLSTATE`** ([int](language.types.integer.md))
:   Passada para [pg\_set\_error\_verbosity()](function.pg-set-error-verbosity.md).
    Inclui apenas a severidade de erro e o código de erro `SQLSTATE`.
    Se não houver código de erro disponível, a saída é similar ao
    modo **`PGSQL_ERRORS_TERSE`**.
    Antes do PostgreSQL 11.1, a saída era sempre a mesma
    do modo **`PGSQL_ERRORS_TERSE`**.

**`PGSQL_NOTICE_LAST`** ([int](language.types.integer.md))
:   Usado por [pg\_last\_notice()](function.pg-last-notice.md).
    Disponível desde o PHP 7.1.0.

**`PGSQL_NOTICE_ALL`** ([int](language.types.integer.md))
:   Usado por [pg\_last\_notice()](function.pg-last-notice.md).
    Disponível desde o PHP 7.1.0.

**`PGSQL_NOTICE_CLEAR`** ([int](language.types.integer.md))
:   Usado por [pg\_last\_notice()](function.pg-last-notice.md).
    Disponível desde o PHP 7.1.0.

**`PGSQL_STATUS_LONG`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_status()](function.pg-result-status.md). Indica que
    é desejando um código de resultado numérico.

**`PGSQL_STATUS_STRING`** ([int](language.types.integer.md))
:   Passada para [pg\_result\_status()](function.pg-result-status.md). Indica que
    é desejado um resultado textual.

**`PGSQL_CONV_IGNORE_DEFAULT`** ([int](language.types.integer.md))
:   Passada para [pg\_convert()](function.pg-convert.md).
    Ignora valores padrão na tabela durante a conversão.

**`PGSQL_CONV_FORCE_NULL`** ([int](language.types.integer.md))
:   Passada para [pg\_convert()](function.pg-convert.md).
    Usa `NULL` da SQL no lugar de uma [string](language.types.string.md) vazia.

**`PGSQL_CONV_IGNORE_NOT_NULL`** ([int](language.types.integer.md))
:   Passada para [pg\_convert()](function.pg-convert.md).
    Ignora conversão de **`null`** em colunas SQL `NOT NULL`.

**`PGSQL_DML_NO_CONV`** ([int](language.types.integer.md))
:   Passada para [pg\_insert()](function.pg-insert.md), [pg\_select()](function.pg-select.md),
    [pg\_update()](function.pg-update.md) e [pg\_delete()](function.pg-delete.md).
    Todos os parâmetros passados como são. Escape manual é requeriso se
    os parâmentros contiverem dados fornecidos pelo usuário. Use [pg\_escape\_string()](function.pg-escape-string.md)
    para isto.

**`PGSQL_DML_EXEC`** ([int](language.types.integer.md))
:   Passada para [pg\_insert()](function.pg-insert.md), [pg\_select()](function.pg-select.md),
    [pg\_update()](function.pg-update.md) e [pg\_delete()](function.pg-delete.md).
    Executa consulta através dessas funções.

**`PGSQL_DML_ASYNC`** ([int](language.types.integer.md))
:   Passada para [pg\_insert()](function.pg-insert.md), [pg\_select()](function.pg-select.md),
    [pg\_update()](function.pg-update.md) e [pg\_delete()](function.pg-delete.md).
    Executa consulta assíncrona através dessas funções.

**`PGSQL_DML_STRING`** ([int](language.types.integer.md))
:   Passada para [pg\_insert()](function.pg-insert.md), [pg\_select()](function.pg-select.md),
    [pg\_update()](function.pg-update.md) e [pg\_delete()](function.pg-delete.md).
    Retorna a string da consulta executada.

**`PGSQL_DML_ESCAPE`** ([int](language.types.integer.md))
:   Passada para [pg\_insert()](function.pg-insert.md), [pg\_select()](function.pg-select.md),
    [pg\_update()](function.pg-update.md) e [pg\_delete()](function.pg-delete.md).
    Escapa todos os parâmetros ao invés de chamar [pg\_convert()](function.pg-convert.md)
    internamente. Esta opção omite pesquisa por metadados. A consulta pode ser tão rápida quanto
    [pg\_query()](function.pg-query.md) e [pg\_send\_query()](function.pg-send-query.md).

**`PGSQL_POLLING_FAILED`** ([int](language.types.integer.md))
:   Retornada por [pg\_connect\_poll()](function.pg-connect-poll.md) para indicar que a
    tentativa de conexão falhou.

**`PGSQL_POLLING_READING`** ([int](language.types.integer.md))
:   Retornada por [pg\_connect\_poll()](function.pg-connect-poll.md) para indicar que a
    conexão está esperando que o socket PostgreSQL possa ser lido.

**`PGSQL_POLLING_WRITING`** ([int](language.types.integer.md))
:   Retornada por [pg\_connect\_poll()](function.pg-connect-poll.md) para indicar que a
    conexão está esperando que o socket PostgreSQL possa ser escrito.

**`PGSQL_POLLING_OK`** ([int](language.types.integer.md))
:   Retornada por [pg\_connect\_poll()](function.pg-connect-poll.md) para indicar que a
    conexão está pronta para uso.

**`PGSQL_POLLING_ACTIVE`** ([int](language.types.integer.md))
:   Retornada por [pg\_connect\_poll()](function.pg-connect-poll.md) para indicar que a
    conexão está atualmente ativa.

**`PGSQL_DIAG_SEVERITY_NONLOCALIZED`** ([int](language.types.integer.md))
:   A severidade; os conteúdos dos campos são ERROR, FATAL ou PANIC (em uma mensagem de erro); ou WARNING, NOTICE, DEBUG, INFO, ou LOG (em uma nota). Isto é idêntico ao campo PG\_DIAG\_SEVERITY exceto que o conteúdo nunca é traduzido. Está presente somente em versões 9.6 e posteriores / PHP 7.3.0 e posteriores.

**`PGSQL_SHOW_CONTEXT_NEVER`** ([int](language.types.integer.md))
:   Para ser usada com [pg\_set\_error\_context\_visibility()](function.pg-set-error-context-visibility.md),
    o contexto nunca é mostrado.
    Disponível a partir do PHP 8.3.0.

**`PGSQL_SHOW_CONTEXT_ERRORS`** ([int](language.types.integer.md))
:   Para ser usada com [pg\_set\_error\_context\_visibility()](function.pg-set-error-context-visibility.md),
    os campos do contexto são incluídos apenas nas mensagens de erro.
    Este é o comportamento padrão.
    Disponível a partir do PHP 8.3.0.

**`PGSQL_SHOW_CONTEXT_ALWAYS`** ([int](language.types.integer.md))
:   Para ser usada com [pg\_set\_error\_context\_visibility()](function.pg-set-error-context-visibility.md),
    os campos do contexto são incluídos nas mensagens de erro, notas e alertas.
    Disponível a partir do PHP 8.3.0.

**`PGSQL_TRACE_SUPPRESS_TIMESTAMPS`** ([int](language.types.integer.md))
:   Para ser usada com [pg\_trace()](function.pg-trace.md),
    o timestamp não é incluído nas mensagens de rastreamento.
    Disponível a partir do PHP 8.4.20.

**`PGSQL_TRACE_REGRESS_MODE`** ([int](language.types.integer.md))
:   Para ser usada com [pg\_trace()](function.pg-trace.md),
    campos como OIDs são incluídos nas mensagens de rastreamento.
    Disponível a partir do PHP 8.3.0.

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
