# Retorna o valor do elemento

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocicollection.getelem.php

---

# OCICollection::getElem

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCICollection::getElem — Retorna o valor do elemento

### Descrição

public function **OCICollection::getElem**([int](language.types.integer.md) `$index`): [string](language.types.string.md)|[float](language.types.float.md)|[null](language.types.null.md)|[false](language.types.singleton.md)

Retorna o valor do elemento com o índice `index` (base 0).

### Parâmetros

`index`
:   O índice do elemento. O primeiro índice é 0.

### Valor Retornado

Retorna **`false`** se tal elemento não existir; **`null`** se o elemento for **`null`**
string se o elemento for uma coluna de um tipo de dado string ou número se o elemento for
campo numérico.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Collection** foi renomeada para [OCICollection](class.ocicollection.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCICollection::assignElem](ocicollection.assignelem.md)

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
