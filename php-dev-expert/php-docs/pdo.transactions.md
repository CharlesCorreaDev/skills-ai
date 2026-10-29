# Transações e confirmação automática (auto-commit)

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.transactions.php

---

# Transações e confirmação automática (auto-commit)

Agora que você está conectado via PDO, é necessário entender como o PDO
gerencia transações antes de começar a emitir consultas. Se você nunca
encontrou transações antes, elas oferecem 4 recursos principais: Atomicidade,
Consistência, Isolamento e Durabilidade (ACID). Em termos simples, qualquer trabalho
realizado em uma transação, mesmo que seja feito em etapas, é
garantido de ser aplicado ao banco de dados com segurança e sem interferência
de outras conexões, quando é confirmado. O trabalho transacional também pode
ser desfeito automaticamente a seu pedido (desde que você ainda não tenha
confirmado), o que facilita o tratamento de erros em seus scripts.

As transações são tipicamente implementadas "salvando" seu lote de
alterações para serem aplicadas de uma vez; isso tem o efeito colateral agradável de
melhorar drasticamente a eficiência dessas atualizações. Em outras palavras,
transações podem tornar seus scripts mais rápidos e potencialmente mais robustos
(ainda é necessário usá-los corretamente para obter esse benefício).

Infelizmente, nem todos os bancos de dados suportam transações, então o PDO precisa
rodar no que é conhecido como modo "auto-commit" quando você abre a
conexão pela primeira vez. O modo auto-commit significa que cada consulta que você
executa tem sua própria transação implícita, se o banco de dados suportar, ou nenhuma transação
se o banco de dados não suportar transações. Se você precisar de uma transação,
você deve usar o método [PDO::beginTransaction()](pdo.begintransaction.md) para
iniciá-la. Se o driver subjacente não suportar transações, uma
PDOException será lançada (independentemente das suas configurações de tratamento de erro:
essa é sempre uma condição de erro grave). Uma vez que você está em uma transação,
você pode usar [PDO::commit()](pdo.commit.md) ou
[PDO::rollBack()](pdo.rollback.md) para finalizá-la, dependendo do sucesso
do código que você executou durante a transação.

**Aviso**

O PDO verifica apenas as capacidades de transação no nível do driver. Se certas
condições de tempo de execução significarem que transações estão indisponíveis,
[PDO::beginTransaction()](pdo.begintransaction.md) ainda retornará **`true`**
sem erro se o servidor de banco de dados aceitar a solicitação para iniciar uma
transação.

Um exemplo disso seria tentar usar transações em tabelas MyISAM em
um banco de dados MySQL.

**Aviso**

*Confirmações Implícitas com Instruções DDL:*
Alguns bancos de dados emitem automaticamente um
`COMMIT` implícito quando uma instrução de Linguagem de Definição
de Banco de Dados (DDL), como `DROP TABLE` ou `CREATE TABLE`,
é executada dentro de uma transação. Isto significa que quaisquer modificações feitas na
mesma transação serão *confirmadas automaticamente* e não poderão
ser revertidas.

`MySQL` e `Oracle` são exemplos de bancos de dados que
exibem este comportamento.

**Exemplo #1 Exemplo de Confirmação Implícita**

```
<?php
$pdo->beginTransaction();
$pdo->exec("INSERT INTO users (name) VALUES ('Rasmus')");
$pdo->exec("CREATE TABLE test (id INT PRIMARY KEY)"); // aqui ocorre um COMMIT implícito
$pdo->rollBack(); // Isto NÃO irá desfazer as instruções INSERT/CREATE no MySQL ou no Oracle
?>
```

*Melhores Práticas:* Evite executar instruções DDL dentro de transações
quando usar banco de dados que têm este comportamento. Se necessário, separe as operações DDL
da lógica das transações.

Quando o script termina ou quando uma conexão está prestes a ser fechada, se você
tiver uma transação pendente, o PDO automaticamente a reverterá.
Esta é uma medida de segurança para ajudar a evitar inconsistências nos casos em que
o script termina inesperadamente--se você não confirmou explicitamente a
transação, então é assumido que algo deu errado, então o rollback
é executado para a segurança de seus dados.

**Aviso**

O rollback automático só acontece se você iniciar a transação via
[PDO::beginTransaction()](pdo.begintransaction.md). Se você emitir manualmente uma
consulta que inicia uma transação, o PDO não tem como saber sobre isso e
assim não pode revertê-la se algo ruim acontecer.

**Exemplo #2 Executando um lote em uma transação**

No exemplo a seguir, vamos assumir que estamos criando um conjunto de
entradas para um novo funcionário, que recebeu um número de ID 23.
Além de inserir os dados básicos para essa pessoa, também precisamos
registrar seu salário. É bastante simples fazer duas atualizações separadas,
mas ao envolvê-las nas chamadas
[PDO::beginTransaction()](pdo.begintransaction.md) e
[PDO::commit()](pdo.commit.md), estamos garantindo que ninguém
mais poderá ver essas alterações até que elas estejam completas. Se
algo der errado, o bloco catch reverte todas as alterações feitas
desde que a transação foi iniciada e, em seguida, imprime uma
mensagem de erro.

```
<?php
try {
  $dbh = new PDO('odbc:SAMPLE', 'db2inst1', 'ibmdb2',
      array(PDO::ATTR_PERSISTENT => true));
  echo "Connected\n";
} catch (Exception $e) {
  die("Não foi possível conectar: " . $e->getMessage());
}

try {
  $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

  $dbh->beginTransaction();
  $dbh->exec("insert into staff (id, first, last) values (23, 'Joe', 'Bloggs')");
  $dbh->exec("insert into salarychange (id, amount, changedate)
      values (23, 50000, NOW())");
  $dbh->commit();

} catch (Exception $e) {
  $dbh->rollBack();
  echo "Falha: " . $e->getMessage();
}
?>
```

Você não está limitado a fazer atualizações em uma transação; você também pode emitir
consultas complexas para extrair dados e possivelmente usar essas informações para
construir mais atualizações e consultas; enquanto a transação estiver ativa, você
tem a garantia de que ninguém mais pode fazer alterações enquanto você está
no meio do seu trabalho. Para ler mais sobre transações, consulte a
documentação fornecida pelo seu servidor de banco de dados.

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
