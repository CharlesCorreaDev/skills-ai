# Vincula uma coluna a uma variável PHP

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.bindcolumn.php

---

# PDOStatement::bindColumn

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDOStatement::bindColumn — 
Vincula uma coluna a uma variável PHP

### Descrição

public function **PDOStatement::bindColumn**(  
    [string](language.types.string.md)|[int](language.types.integer.md) `$column`,  
    [mixed](language.types.mixed.md) `&$var`,  
    [int](language.types.integer.md) `$type` = **`PDO::PARAM_STR`**,  
    [int](language.types.integer.md) `$maxLength` = 0,  
    [mixed](language.types.mixed.md) `$driverOptions` = **`null`**  
): [bool](language.types.boolean.md)

**PDOStatement::bindColumn()** faz com que
uma variável em particular seja vinculada a uma coluna informada, no conjunto de resultados de
uma consulta. Cada chamada a [PDOStatement::fetch()](pdostatement.fetch.md) ou
[PDOStatement::fetchAll()](pdostatement.fetchall.md) irá atualizar todas as variáveis
que estejam vinculadas a colunas.

> **Nota**:
>
> Como as informações sobre a coluna não estão sempre disponíveis ao PDO até que
> a instrução seja executada, aplicações portáteis devem chamar esta
> função *após* [PDOStatement::execute()](pdostatement.execute.md).
>
> Entretanto, para que seja possível vincular uma coluna LOB como um fluxo ao usar o
> *driver PgSQL*, aplicações devem chamar este método
> *antes* de chamada a [PDOStatement::execute()](pdostatement.execute.md),
> caso contrário o OID de objeto grande será retornado como um inteiro.

### Parâmetros

`column`
:   Número da coluna (índices iniciando em 1) ou nome da coluna no conjunto de resultados.
    Se o nome da coluna estiver sendo usado, o nome deve ter as maiúsculas/minúsculas correspondentes
    à coluna, como retornada pelo driver.

`var`
:   Nome da variável PHP à qual a coluna será vinculada.

`type`
:   Tipo de dado do parâmetro, especificado pelas [constantes `PDO::PARAM_*`](pdo.constants.md).

`maxLength`
:   Um dica para pré-alocação.

`driverOptions`
:   Um ou mais parâmetros opcionais para o driver.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Vinculando a saída do conjunto de resultados a variáveis PHP**

Vincular colunas no conjunto de resultados a variáveis PHP é uma maneira
eficaz de fazer com que os dados contidos em cada linha estejam imediatamente disponíveis para
a aplicação. O exemplo a seguir demonstra como o PDO permite
que se vincule e se recupere colunas com uma variedade de opções e com
padrões inteligentes.

```
<?php
$stmt = $dbh->prepare('SELECT name, colour, calories FROM fruit');
$stmt->execute();

/* Vincula por número da coluna */
$stmt->bindColumn(1, $name);
$stmt->bindColumn(2, $colour);

/* Vincula por nome da coluna */
$stmt->bindColumn('calories', $cals);

while ($stmt->fetch(PDO::FETCH_BOUND)) {
    print $name . "\t" . $colour . "\t" . $cals . "\n";
}
```

O exemplo acima produzirá
algo semelhante a:

```
apple   red     150
banana  yellow  175
kiwi    green   75
orange  orange  150
mango   red     200
strawberry      red     25
```

### Veja também

- [PDOStatement::execute()](pdostatement.execute.md) - Executa ums instrução preparada
- [PDOStatement::fetch()](pdostatement.fetch.md) - Busca a próxima linha de um resultado
- [PDOStatement::fetchAll()](pdostatement.fetchall.md) - Busca as linhas remanescentes de um conjunto de resultados
- [PDOStatement::fetchColumn()](pdostatement.fetchcolumn.md) - Retorna uma única coluna do próximo registro de um resultado

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
