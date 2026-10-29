# Atribui um valor de outra coleção existente a esta coleção

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocicollection.assign.php

---

# OCICollection::assign

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCICollection::assign — Atribui um valor de outra coleção existente a esta coleção

### Descrição

public function **OCICollection::assign**([OCICollection](class.ocicollection.md) `$from`): [bool](language.types.boolean.md)

Atribui um valor à coleção de outra coleção
previamente criada. Ambas as coleções devem ser criadas com
[oci\_new\_collection()](function.oci-new-collection.md) antes de serem usadas.

### Parâmetros

`from`
:   Uma instância de OCICollection.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Collection** foi renomeada para [OCICollection](class.ocicollection.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCICollection::append](ocicollection.append.md)

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
