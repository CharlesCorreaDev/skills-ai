# Retorna o ID da última linha ou valor de sequência inserido

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.lastinsertid.php

---

# PDO::lastInsertId

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDO::lastInsertId — 
Retorna o ID da última linha ou valor de sequência inserido

### Descrição

public function **PDO::lastInsertId**([?](language.types.null.md)[string](language.types.string.md) `$name` = **`null`**): [string](language.types.string.md)|[false](language.types.singleton.md)

Retorna o ID da última linha inserida, ou o último valor de um
objeto de sequência, dependendo do driver subjacente. Por exemplo,
[PDO\_PGSQL](ref.pdo-pgsql.md) permite que o nome de qualquer
objeto de sequência seja especificado para o parâmetro `name`.

> **Nota**:
>
> Este método pode não retornar um resultado significativo ou consistente em
> diferentes drivers PDO, pois o banco de dados subjacente pode nem mesmo
> suportar a noção de campos ou sequências auto-incrementais.

### Parâmetros

`name`
:   Nome do objeto de sequência do qual o ID deve ser retornado.

### Valor Retornado

Se um nome de sequência não foi especificado para o parâmetro `name`,
**PDO::lastInsertId()** retornará uma
string representando o ID da última linha que foi inserida
no banco de dados.

Se um nome de sequência foi especificado para o parâmetro `name`,
**PDO::lastInsertId()** retornará uma
string representando o último valor recuperado do objeto de sequência
especificado.

Se o driver PDO não suportar este recurso,
**PDO::lastInsertId()** dispara um
SQLSTATE `IM001`.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

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
