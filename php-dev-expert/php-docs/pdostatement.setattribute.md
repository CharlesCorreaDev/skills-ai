# Define um atributo na instrução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdostatement.setattribute.php

---

# PDOStatement::setAttribute

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.2.0)

PDOStatement::setAttribute — 
Define um atributo na instrução

### Descrição

public function **PDOStatement::setAttribute**([int](language.types.integer.md) `$attribute`, [mixed](language.types.mixed.md) `$value`): [bool](language.types.boolean.md)

Define um atributo na instrução. Atualmente não há atributos genericos definidos, apenas atributos específicos do driver:

- `PDO::ATTR_CURSOR_NAME`
  (Específico do Firebird e do ODBC):
  Define o nome do cursor para `UPDATE ... WHERE CURRENT OF`.

Note que atributos específicos de drivers *não devem* ser usados
com outros drivers.

### Parâmetros

`attribute`
:   O atibuto a modificar.

`value`
:   O valor para definir o `attribute`,
    pode requerer um tipo específico dependendo do atributo.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Veja também

- [PDO::getAttribute()](pdo.getattribute.md) - Recuperar um atributo da conexão com o banco de dados
- [PDO::setAttribute()](pdo.setattribute.md) - Define um atributo
- [PDOStatement::getAttribute()](pdostatement.getattribute.md) - Recupera um atributo da instrução

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
