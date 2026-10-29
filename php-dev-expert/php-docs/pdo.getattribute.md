# Recuperar um atributo da conexão com o banco de dados

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.getattribute.php

---

# PDO::getAttribute

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.2.0)

PDO::getAttribute — 
Recuperar um atributo da conexão com o banco de dados

### Descrição

public function **PDO::getAttribute**([int](language.types.integer.md) `$attribute`): [mixed](language.types.mixed.md)

Esta função retorna o valor de um atributo da conexão com o banco de dados. Para
recuperar atributos de PDOStatement consulte
[PDOStatement::getAttribute()](pdostatement.getattribute.md).

Note que algumas combinações de banco de dados e drivers podem não suportar
todos os atributos da conexão com o banco de dados.

### Parâmetros

`attribute`
:   Uma das constantes `PDO::ATTR_*`. Os atributos genéricos que
    se aplicam a conexões com o banco de dados são os seguintes:

    - `PDO::ATTR_CASE`
    - `PDO::ATTR_DEFAULT_FETCH_MODE`
    - `PDO::ATTR_DRIVER_NAME`
    - `PDO::ATTR_ERRMODE`
    - `PDO::ATTR_ORACLE_NULLS`
    - `PDO::ATTR_PERSISTENT`
    - `PDO::ATTR_STATEMENT_CLASS`
    - `PDO::ATTR_STRINGIFY_FETCHES`

    Alguns drivers podem fazer uso de atributos específicos adicionais.
    Note que atributos específicos de drivers *não devem* ser usados
    com outros drivers.

### Valor Retornado

Uma chamada com sucesso retornará o valor do atributo PDO solicitado.
Uma chamada sem sucesso retornará **`null`**.

### Erros/Exceções

**PDO::getAttribute()** pode lançar uma [PDOException](class.pdoexception.md)
quando o driver subjacente não suportar o `attribute` requerido.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.4.0 | Agora é possível obter o valor do atributo **`PDO::ATTR_STRINGIFY_FETCHES`**. |

### Examples

**Exemplo #1 Recuperando atributos de uma conexão com o banco de dados**

```
<?php
$conn = new PDO('odbc:sample', 'db2inst1', 'ibmdb2');
$attributes = array(
    "AUTOCOMMIT", "ERRMODE", "CASE", "CLIENT_VERSION", "CONNECTION_STATUS",
    "ORACLE_NULLS", "PERSISTENT", "PREFETCH", "SERVER_INFO", "SERVER_VERSION",
    "TIMEOUT"
);

foreach ($attributes as $val) {
    echo "PDO::ATTR_$val: ";
    echo $conn->getAttribute(constant("PDO::ATTR_$val")) . "\n";
}
?>
```

### Veja também

- [PDO::setAttribute()](pdo.setattribute.md) - Define um atributo
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
