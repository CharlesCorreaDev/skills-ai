# Libera recursos associados ao descritor do LOB

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.free.php

---

# OCILob::free

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::free — Libera recursos associados ao descritor do LOB

### Descrição

public function **OCILob::free**(): [bool](language.types.boolean.md)

Libera recursos associados ao descritor, previamente alocados com
[oci\_new\_descriptor()](function.oci-new-descriptor.md).

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

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
