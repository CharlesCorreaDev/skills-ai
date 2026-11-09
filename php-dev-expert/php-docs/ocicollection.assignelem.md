# Atribui um valor ao elemento da coleção

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocicollection.assignelem.php

---

# OCICollection::assignElem

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCICollection::assignElem — Atribui um valor ao elemento da coleção

### Descrição

public function **OCICollection::assignElem**([int](language.types.integer.md) `$index`, [string](language.types.string.md) `$value`): [bool](language.types.boolean.md)

Atribui um valor ao elemento com índice `index`.

### Parâmetros

`index`
:   O índice do elemento. O primeiro índice é 0.

`value`
:   Pode ser uma string ou um número.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Collection** foi renomeada para [OCICollection](class.ocicollection.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCICollection::getElem](ocicollection.getelem.md)

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
