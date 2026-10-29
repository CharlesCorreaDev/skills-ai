# Registra uma função definida pelo usuário para uso em instruções SQL

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-sqlite.createfunction.php

---

# Pdo\Sqlite::createFunction

(PHP 8 >= 8.4.0)

Pdo\Sqlite::createFunction — 
Registra uma função definida pelo usuário para uso em instruções SQL

### Descrição

public function **Pdo\Sqlite::createFunction**(  
    [string](language.types.string.md) `$function_name`,  
    [callable](language.types.callable.md) `$callback`,  
    [int](language.types.integer.md) `$num_args` = -1,  
    [int](language.types.integer.md) `$flags` = 0  
): [bool](language.types.boolean.md)

Este método permite que a função PHP seja registrada no SQLite como uma
função definida pelo usuário, para que possa ser chamada em consultas SQL.
A função definida pode ser usada em qualquer consulta SQL que permita chamadas de função,
por exemplo `SELECT`, `UPDATE` ou gatilhos.

**Dica**

Usando este método é possível substituir funções SQL nativas.

### Parâmetros

`function_name`
:   O nome da função usada nas instruções SQL.

`callback`
:   Função de retorno de chamada para lidar com a função SQL definida.

    > **Nota**:
    >
    > As funções de retorno de chamada devem retornar um tipo compreendido pelo SQLite (ou seja,
    > [tipo escalar](language.types.intro.md)).

    Esta função precisa ser definida como:

    function callback([mixed](language.types.mixed.md) `$value`, [mixed](language.types.mixed.md) `...$values`): [mixed](language.types.mixed.md)

    `value`
    :   O primeiro argumento passado para a função SQL.

    `values`
    :   Argumentos adicionais passados ​​para a função SQL.

`num_args`
:   O número de argumentos que a função SQL utiliza.
    Se este parâmetro for `-1`,
    a função SQL poderá receber qualquer número de argumentos.

`flags`
:   Uma máscara de bits de opções.
    Atualmente, apenas **`Pdo\Sqlite::DETERMINISTIC`** é suportada,
    o que especifica que a função sempre retorna o mesmo resultado dadas
    as mesmas entradas em uma única instrução SQL.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Examples

**Exemplo #1 Exemplo de **Pdo\Sqlite::createFunction()****

Neste exemplo, temos uma função que calcula a soma SHA256 de uma
string e depois a inverte. Quando a instrução SQL é executada, ela
retorna o valor do nome do arquivo transformado pela nossa função.
Os dados retornados em $rows contêm o resultado processado.

A beleza desta técnica é que não há necessidade de processar
o resultado usando um laço [`foreach`](control-structures.foreach.md) após a consulta.

```
<?php
function sha256_and_reverse($string)
{
    return strrev(hash('sha256', $string));
}

$db = new Pdo\Sqlite('sqlite::sqlitedb');
$db->createFunction('sha256rev', 'sha256_and_reverse', 1);
$rows = $db->query('SELECT sha256rev(filename) FROM files')->fetchAll();
?>
```

### Veja também

- [Pdo\Sqlite::createAggregate()](pdo-sqlite.createaggregate.md) - Registra uma função de agregação definida pelo usuário para uso em instruções SQL
- [Pdo\Sqlite::createCollation()](pdo-sqlite.createcollation.md) - Registra uma função definida pelo usuário para uso como função de agrupamento em instruções SQL
- **sqlite\_create\_function()**
- **sqlite\_create\_aggregate()**

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
