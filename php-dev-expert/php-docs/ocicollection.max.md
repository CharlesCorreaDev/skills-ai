# Retorna o número máximo de elementos na coleção

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocicollection.max.php

---

# OCICollection::max

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCICollection::max — Retorna o número máximo de elementos na coleção

### Descrição

public function **OCICollection::max**(): [int](language.types.integer.md)|[false](language.types.singleton.md)

Retorna o número máximo de elementos na coleção.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o número máximo como um inteiro ou **`false`** em caso de erros.

Se o valor retornado for 0, o número de elementos não será limitado.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Collection** foi renomeada para [OCICollection](class.ocicollection.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCICollection::size](ocicollection.size.md)

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
