# Adiciona elemento à coleção

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocicollection.append.php

---

# OCICollection::append

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCICollection::append — Adiciona elemento à coleção

### Descrição

public function **OCICollection::append**([string](language.types.string.md) `$value`): [bool](language.types.boolean.md)

Acrescenta elemento ao final da coleção.

### Parâmetros

`value`
:   O valor a ser adicionado à coleção.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Collection** foi renomeada para [OCICollection](class.ocicollection.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCICollection::assign](ocicollection.assign.md)

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
