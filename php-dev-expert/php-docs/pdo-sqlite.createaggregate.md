# Registra uma função de agregação definida pelo usuário para uso em instruções SQL

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-sqlite.createaggregate.php

---

# Pdo\Sqlite::createAggregate

(PHP 8 >= 8.4.0)

Pdo\Sqlite::createAggregate — 
Registra uma função de agregação definida pelo usuário para uso em instruções SQL

### Descrição

public function **Pdo\Sqlite::createAggregate**(  
    [string](language.types.string.md) `$name`,  
    [callable](language.types.callable.md) `$step`,  
    [callable](language.types.callable.md) `$finalize`,  
    [int](language.types.integer.md) `$numArgs` = -1  
): [bool](language.types.boolean.md)

Este método é semelhante a [Pdo\Sqlite::createFunction()](pdo-sqlite.createfunction.md)
exceto que registra funções que podem ser usadas para calcular um
resultado agregado em todas as linhas de uma consulta.

A principal diferença entre este método e
[Pdo\Sqlite::createFunction()](pdo-sqlite.createfunction.md)
é que duas funções são necessárias para gerenciar a agregação.

**Dica**

Usando este método é possível substituir funções SQL nativas.

### Parâmetros

`name`
:   O nome da função usada nas instruções SQL.

`step`
:   Função de retorno de chamada chamada para cada linha do conjunto de resultados.
    O retorno de chamada deve acumular o resultado e armazená-lo no contexto de agregação.

    Esta função precisa ser definida como:

    function step(  
        [mixed](language.types.mixed.md) `$context`,  
        [int](language.types.integer.md) `$rownumber`,  
        [mixed](language.types.mixed.md) `$value`,  
        [mixed](language.types.mixed.md) `...$values`  
    ): [mixed](language.types.mixed.md)

    `context`
    :   **`null`** para a primeira linha; nas linhas subsequentes terá o valor
        que foi retornado anteriormente da função step; deve-se usar
        isso para manter o estado agregado.

    `rownumber`
    :   O número da linha atual.

    `value`
    :   O primeiro argumento passado para o agregado.

    `values`
    :   Outros argumentos passados ​​para o agregado.

    O valor de retorno desta função será usado como argumento
    `context` na próxima chamada das funções step
    ou finalize.

`finalize`
:   Função de retorno de chamada para agregar os dados "escalonados" de cada linha.
    Depois que todas as linhas forem processadas, esta função será chamada,
    devendo então pegar os dados do contexto de agregação e retornar o resultado.
    Esta função de retorno de chamada deve retornar um tipo compreendido pelo SQLite
    (ou seja, [tipo escalar](language.types.intro.md)).

    Esta função precisa ser definida como:

    function fini([mixed](language.types.mixed.md) `$context`, [int](language.types.integer.md) `$rowcount`): [mixed](language.types.mixed.md)

    `context`
    :   Contém o valor de retorno da última chamada para a função step.

    `rowcount`
    :   Contém o número de linhas nas quais a agregação foi executada.

    O valor de retorno desta função será usado como valor de retorno
    da agregação.

`numArgs`
:   Dica para o analisador SQLite se a função de retorno de chamada
    aceita um número predeterminado de argumentos.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Examples

**Exemplo #1 Exemplo de **Pdo\Sqlite::createAggregate()****

Neste exemplo, criaremos uma função agregada personalizada chamada
`max_length` que pode ser usada em consultas SQL.

Neste exemplo, estamos criando uma função agregadora,
chamada `max_length`, que calculará o comprimento
da string mais longa em uma das colunas da tabela.
Para cada linha, a função `max_len_step` é chamada e
passa um parâmetro `$context`.
O parâmetro context é como qualquer outra variável PHP e pode ser configurado para
conter um [array](language.types.array.md) ou até mesmo um [object](language.types.object.md).
Neste exemplo, estamos usando-o para manter o comprimento máximo que vimos até agora;
se $string tiver um comprimento maior que o máximo atual,
atualizamos o contexto para manter esse novo comprimento máximo.

Após todas as linhas terem sido processadas,
o SQLite chama a função `max_len_finalize` para determinar
o resultado agregado.
É possível realizar algum tipo de cálculo baseado nos dados em `$context`.
Neste exemplo básico o resultado foi calculado à medida que a consulta avançava,
para que o valor do contexto pudesse ser retornado diretamente.

```
<?php
$data = [
   'one',
   'two',
   'three',
   'four',
   'five',
   'six',
   'seven',
   'eight',
   'nine',
   'ten',
];
$db = new Pdo\Sqlite('sqlite::memory:');
$db->exec("CREATE TABLE strings(a)");
$insert = $db->prepare('INSERT INTO strings VALUES (?)');
foreach ($data as $str) {
    $insert->execute(array($str));
}
$insert = null;

function max_len_step($context, $row_number, $string)
{
    if (strlen($string) > $context) {
        $context = strlen($string);
    }
    return $context;
}

function max_len_finalize($context, $row_count)
{
    return $context === null ? 0 : $context;
}

$db->createAggregate('max_len', 'max_len_step', 'max_len_finalize');

var_dump($db->query('SELECT max_len(a) from strings')->fetchAll());

?>
```

**Dica**

NÃO é recomendado que se armazene uma cópia dos valores no contexto
e depois processe-os no final, pois faria com que o SQLite usasse muita
memória para processar a consulta - basta pensar em quanta memória seria necessárias
se um milhão de linhas fossem armazenadas na memória, cada uma contendo uma string de 32 bytes
de comprimento.

### Veja também

- [Pdo\Sqlite::createFunction()](pdo-sqlite.createfunction.md) - Registra uma função definida pelo usuário para uso em instruções SQL
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
