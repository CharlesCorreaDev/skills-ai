# Executa uma instrução SQL e retorna o número de linhas afetadas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.exec.php

---

# PDO::exec

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDO::exec — 
Executa uma instrução SQL e retorna o número de linhas afetadas

### Descrição

public function **PDO::exec**([string](language.types.string.md) `$statement`): [int](language.types.integer.md)|[false](language.types.singleton.md)

**PDO::exec()** executa uma instrução SQL em
uma única chamada de função, retornando o número de linhas afetadas pela
instrução.

**PDO::exec()** não retorna resultados de uma instrução
SELECT. Para uma instrução SELECT que você só precisa emitir uma vez
durante seu programa, considere a emissão de [PDO::query()](pdo.query.md).
Para uma instrução que você precisa emitir várias vezes, prepare um objeto
PDOStatement com [PDO::prepare()](pdo.prepare.md) e emita a
instrução com [PDOStatement::execute()](pdostatement.execute.md).

### Parâmetros

`statement`
:   A instrução SQL para preparar e executar.

    Os dados dentro da consulta devem ser [adequadamente escapados](pdo.quote.md).

### Valor Retornado

**PDO::exec()** retorna o número de linhas que foram
modificadas ou excluídas pela instrução SQL que você emitiu. Se nenhuma linha
for afetada, **PDO::exec()** retorna `0`.

**Aviso**

Esta função pode
retornar o valor booleano **`false`**, mas também pode retornar um valor não booleano que pode ser
avaliado como **`false`**. Leia a seção sobre [Booleanos](language.types.boolean.md) para mais
informações. Use o [operador
===](language.operators.comparison.md) para testar o valor retornado por esta
função.

O exemplo a seguir depende incorretamente do valor de retorno de
**PDO::exec()**, em que uma instrução que afetou 0 linhas
resulta em uma chamada para [die()](function.die.md):

```
<?php
$db->exec() or die(print_r($db->errorInfo(), true)); // incorreto
?>
```

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Emitindo uma instrução DELETE**

Conte o número de linhas excluídas por uma instrução DELETE sem
cláusula WHERE.

```
<?php
$dbh = new PDO('odbc:sample', 'db2inst1', 'ibmdb2');

/* Apaga todas as linhas da tabela FRUIT */
$count = $dbh->exec("DELETE FROM fruit");

/* Retorna o número de linhas apagadas */
print "Apagada(s) $count linha(s).\n";
?>
```

O exemplo acima produzirá:

```
Apagada(s) 1 linha(s).
```

### Veja também

- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
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
