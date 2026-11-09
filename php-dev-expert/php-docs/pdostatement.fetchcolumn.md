# Retorna uma única coluna do próximo registro de um resultado

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.fetchcolumn.php

---

# PDOStatement::fetchColumn

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.9.0)

PDOStatement::fetchColumn — 
Retorna uma única coluna do próximo registro de um resultado

### Descrição

public function **PDOStatement::fetchColumn**([int](language.types.integer.md) `$column` = 0): [mixed](language.types.mixed.md)

Retorna uma única coluna do próximo registro de um resultado ou **`false`** se
não houver mais registros.

> **Nota**:
>
> **PDOStatement::fetchColumn()** não deve ser usado para
> colunas do tipo booleano, já que é impossível distinguir um valor de
> **`false`** em relação à inexistência de mais registros a se recuperar. Use
> [PDOStatement::fetch()](pdostatement.fetch.md) em seu lugar.

### Parâmetros

`column`
:   Número da coluna que se deseja recuperar do registro, com índice iniciando em 0. Se
    nenhum valor for informado, **PDOStatement::fetchColumn()**
    busca a primeira coluna.

### Valor Retornado

**PDOStatement::fetchColumn()** retorna uma única coluna
do próximo registro do resultado ou **`false`** se não houver mais registros.

**Aviso**

Não há como retornar outra coluna do mesmo registro se o método
**PDOStatement::fetchColumn()** for usado para recuperar dados.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Examples

**Exemplo #1 Retorna a primeira coluna do próximo registro**

```
<?php
$sth = $dbh->prepare("SELECT name, colour FROM fruit");
$sth->execute();

print "Busca a primeira coluna da primeira linha do resultado:\n";
$result = $sth->fetchColumn();
print "name = $result\n";

print "Busca a segunda coluna da segunda linha do resultado:\n";
$result = $sth->fetchColumn(1);
print "colour = $result\n";
?>
```

O exemplo acima produzirá:

```
Busca a primeira coluna da primeira linha do resultado:
name = lemon
Busca a segunda coluna da segunda linha do resultado:
colour = red
```

### Veja também

- [PDO::query()](pdo.query.md) - Prepara e executa uma instrução SQL sem marcadores
- [PDOStatement::fetch()](pdostatement.fetch.md) - Busca a próxima linha de um resultado
- [PDOStatement::fetchAll()](pdostatement.fetchall.md) - Busca as linhas remanescentes de um conjunto de resultados
- [PDO::prepare()](pdo.prepare.md) - Prepara uma instrução para execução e retorna um objeto de instrução
- [PDOStatement::setFetchMode()](pdostatement.setfetchmode.md) - Define o modo de carga de dados para esta instrução

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
