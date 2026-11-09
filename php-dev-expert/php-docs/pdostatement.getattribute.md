# Recupera um atributo da instrução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.getattribute.php

---

# PDOStatement::getAttribute

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.2.0)

PDOStatement::getAttribute — 
Recupera um atributo da instrução

### Descrição

public function **PDOStatement::getAttribute**([int](language.types.integer.md) `$name`): [mixed](language.types.mixed.md)

Obtém um atributo da instrução. Atualmente, não existem atributos genéricos mas apenas específicos de drivers:

- `PDO::ATTR_CURSOR_NAME`
  (específico do Firebird e do ODBC):
  Obtém o nome do cursor para `UPDATE ... WHERE CURRENT OF`.
- **`Pdo\Pgsql::ATTR_RESULT_MEMORY_SIZE`**
  (específico do PostgreSQL, disponível a partir do PHP 8.4.0):
  Obtém a quantidade de memória, em bytes, alocada para o resultado da consulta.

Observe que atributos específicos de drivers *não podem* ser usados
com outros drivers.

### Parâmetros

`name`
:   O atributo a ser consultado.

### Valor Retornado

Retorna o valor do atributo.

### Veja também

- [PDO::getAttribute()](pdo.getattribute.md) - Recuperar um atributo da conexão com o banco de dados
- [PDO::setAttribute()](pdo.setattribute.md) - Define um atributo
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
