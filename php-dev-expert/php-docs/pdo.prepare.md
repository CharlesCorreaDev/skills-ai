# Prepara uma instrução para execução e retorna um objeto de instrução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.prepare.php

---

# PDO::prepare

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PHP 8,PECL pdo >= 0.1.0)

PDO::prepare — 
Prepara uma instrução para execução e retorna um objeto de instrução

### Descrição

public function **PDO::prepare**([string](language.types.string.md) `$query`, [array](language.types.array.md) `$options` = []): [PDOStatement](class.pdostatement.md)|[false](language.types.singleton.md)

Prepara uma instrução SQL para ser executada pelo
método [PDOStatement::execute()](pdostatement.execute.md). O modelo de instrução pode
conter zero ou mais marcadores de parâmetros nomeados (:name) ou pontos de interrogação (?)
para os quais os valores reais serão substituídos quando a instrução for executada.
Os marcadores de parâmetros nomeados e de ponto de interrogação não podem ser usados ​​no mesmo
modelo de instrução; apenas um ou outro estilo de parâmetro.
Use esses parâmetros para vincular qualquer entrada do usuário, não inclua a entrada do usuário
diretamente na consulta.

Deve-se incluir um marcador de parâmetro exclusivo para cada valor que se deseja passar
para a instrução ao chamar [PDOStatement::execute()](pdostatement.execute.md).
Um marcador de parâmetro nomeado com o mesmo nome não pode ser usado mais de uma vez em uma instrução
preparada, a menos que o modo de emulação esteja ativado.

> **Nota**:
>
> Os marcadores de parâmetro podem representar apenas um literal de dados completo.
> Nenhuma parte do literal, nem palavra-chave, nem identificador, nem qualquer parte arbitrária
> da consulta pode ser vinculada usando parâmetros. Por exemplo, não se pode vincular múltiplos valores
> a um único parâmetro na cláusula IN() de uma instrução SQL.

Chamar **PDO::prepare()** e
[PDOStatement::execute()](pdostatement.execute.md) para instruções que serão
emitidas diversas vezes com valores de parâmetros diferentes otimiza o
desempenho da aplicação, permitindo que o driver negocie
cache no lado do cliente e/ou do servidor do plano de consulta e metainformações. Além disso, chamar **PDO::prepare()** e
[PDOStatement::execute()](pdostatement.execute.md) ajuda a evitar ataques de injeção de SQL, eliminando a necessidade de
inserir aspas e escapar manualmente dos parâmetros.

O PDO irá emular instruções preparadas/parâmetros vinculados para drivers que
não os suportam nativamente, e também pode reescrever marcadores de parâmetros nomeados
ou no estilo ponto de interrogação para algo mais apropriado, se o driver
suportar um estilo, mas não o outro.

> **Nota**:
>
> Antes do PHP 8.4.0, o analisador usado para instruções preparadas emuladas e para
> reescrever parâmetros nomeados ou no estilo de ponto de interrogação suportava escapes
> de barra invertida não padrão para aspas simples e duplas. Isso significava que aspas
> de término imediatamente precedidas por uma barra invertida não eram reconhecidas como tal, o que
> poderia resultar na detecção incorreta de parâmetros, fazendo com que a instrução preparada
> falhasse quando fosse executada. Uma solução alternativa era não usar preparações emuladas para
> essas consultas SQL e evitar a reescrita de parâmetros usando um estilo de parâmetro
> que fosse suportado nativamente pelo driver.

A partir do PHP 7.4.0, os pontos de interrogação podem ser escapados duplicando-os. Isso significa que
a string `??` será traduzida para `?`
ao enviar a consulta ao banco de dados.

A partir do PHP 8.4.0, O PDO usa analisadores específicos do driver para localizar marcadores de
parâmetros, de forma que os marcadores que aparecem dentro de strings literais ou comentários não
são confundidos como marcadores de parâmetro. O analisador padrão reconhece literais de string entre
aspas simples e duplas, assim como
comentários de duas barras e comentários no estilo C não aninhados. Drivers individuais podem
fornecer um analisador que reconheça sintaxe adicional ou diferente; consulte a documentação
específica do driver para mais detalhes.

### Parâmetros

`query`
:   Este deve ser um modelo de instrução SQL válido para o servidor de banco de dados de destino.

`options`
:   Este array contém um ou mais pares chave=>valor para definir
    valores de atributos para o objeto PDOStatement que esse método
    retorna. Normalmente usa-se isso para definir o
    valor `PDO::ATTR_CURSOR` como
    `PDO::CURSOR_SCROLL` para solicitar um cursor rolável.
    Alguns drivers têm opções específicas que podem ser definidas no
    momento da preparação.

### Valor Retornado

Se o servidor de banco de dados preparar a instrução com sucesso,
**PDO::prepare()** retornará um
objeto [PDOStatement](class.pdostatement.md).
Se o servidor de banco de dados não conseguir preparar a instrução com sucesso,
**PDO::prepare()** retornará **`false`** ou emitirá
uma exceção [PDOException](class.pdoexception.md) (dependendo do [tratamento de erros](pdo.error-handling.md)).

> **Nota**:
>
> Instruções preparadas emuladas não se comunicam com o servidor de banco de dados,
> portanto **PDO::prepare()** não verifica a instrução.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Modelo de instrução SQL com parâmetros nomeados**

```
<?php
/* Executa uma instrução preparada passando um array de valores */
$sql = 'SELECT name, colour, calories
    FROM fruit
    WHERE calories < :calories AND colour = :colour';
$sth = $dbh->prepare($sql, [PDO::ATTR_CURSOR => PDO::CURSOR_FWDONLY]);
$sth->execute(['calories' => 150, 'colour' => 'red']);
$red = $sth->fetchAll();
/* Chaves de arrays podem ser prefizadas com dois-pontos ":" também (opcional) */
$sth->execute([':calories' => 175, ':colour' => 'yellow']);
$yellow = $sth->fetchAll();
?>
```

**Exemplo #2 Modelo de instrução SQL com parâmetros de ponto de interrogação**

```
<?php
/* Executa uma instrução preparada passando um array de valores */
$sth = $dbh->prepare('SELECT name, colour, calories
    FROM fruit
    WHERE calories < ? AND colour = ?');
$sth->execute([150, 'red']);
$red = $sth->fetchAll();
$sth->execute([175, 'yellow']);
$yellow = $sth->fetchAll();
?>
```

**Exemplo #3 Modelo de instrução SQL com ponto de interrogação escapado**

```
<?php
/* nota: isso só é válido em bancos de dados PostgreSQL */
$sth = $dbh->prepare('SELECT * FROM issues WHERE tag::jsonb ?? ?');
$sth->execute(['feature']);
$featureIssues = $sth->fetchAll();
$sth->execute(['performance']);
$performanceIssues = $sth->fetchAll();
?>
```

### Veja também

- [PDO::exec()](pdo.exec.md) - Executa uma instrução SQL e retorna o número de linhas afetadas
- [PDO::query()](pdo.query.md) - Prepara e executa uma instrução SQL sem marcadores
- [PDOStatement::execute()](pdostatement.execute.md) - Executa ums instrução preparada

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
