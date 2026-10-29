# Busca o próximo registro e retorna-o como um objeto

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.fetchobject.php

---

# PDOStatement::fetchObject

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.2.4)

PDOStatement::fetchObject — Busca o próximo registro e retorna-o como um objeto

### Descrição

public function **PDOStatement::fetchObject**([?](language.types.null.md)[string](language.types.string.md) `$class` = "stdClass", [array](language.types.array.md) `$constructorArgs` = []): [object](language.types.object.md)|[false](language.types.singleton.md)

Busca o próximo registro e retorna-o como um objeto. Esta função é uma
alternativa a [PDOStatement::fetch()](pdostatement.fetch.md) com estilo
**`PDO::FETCH_CLASS`** ou
**`PDO::FETCH_OBJ`**.

Quando um objeto é buscado, suas propriedades são atribuídas a partir dos respectivos
valores de colunas, e depois seu construtor é invocado.

### Parâmetros

`class`
:   Nome da classe a ter um objeto criado.

`constructorArgs`
:   Elementos deste array são passados para o construtor.

### Valor Retornado

Retorna uma instância da classe solicitada com nomes de propriedades que
correspondem aos nomes de colunas ou **`false`** em caso de falha.

### Erros/Exceções

Emite um erro de nível **`E_WARNING`** se o atributo **`PDO::ATTR_ERRMODE`** estiver definido
como **`PDO::ERRMODE_WARNING`**.

Lança uma exceção [PDOException](class.pdoexception.md) se o atributo **`PDO::ATTR_ERRMODE`**
estiver definido como **`PDO::ERRMODE_EXCEPTION`**.

### Veja também

- [PDOStatement::fetch()](pdostatement.fetch.md) - Busca a próxima linha de um resultado

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
