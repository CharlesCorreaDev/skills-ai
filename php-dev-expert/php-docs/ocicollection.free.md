# Libera os recursos associados ao objeto de coleção

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocicollection.free.php

---

# OCICollection::free

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCICollection::free — Libera os recursos associados ao objeto de coleção

### Descrição

public function **OCICollection::free**(): [bool](language.types.boolean.md)

Libera os recursos associados ao objeto de coleção.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Collection** foi renomeada para [OCICollection](class.ocicollection.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [oci\_new\_collection](function.oci-new-collection.md)

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
