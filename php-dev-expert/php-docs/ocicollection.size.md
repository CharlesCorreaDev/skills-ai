# Retorna o tamanho da coleção

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocicollection.size.php

---

# OCICollection::size

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCICollection::size — Retorna o tamanho da coleção

### Descrição

public function **OCICollection::size**(): [int](language.types.integer.md)|[false](language.types.singleton.md)

Retorna o tamanho da coleção.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o número de elementos na coleção ou **`false`** em caso de erro.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Collection** foi renomeada para [OCICollection](class.ocicollection.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCICollection::max](ocicollection.max.md)

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
