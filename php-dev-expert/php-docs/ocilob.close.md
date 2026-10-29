# Fecha o descritor LOB

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.close.php

---

# OCILob::close

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::close — Fecha o descritor LOB

### Descrição

public function **OCILob::close**(): [bool](language.types.boolean.md)

Fecha o descritor de LOB ou de arquivo. Esta função deve ser usada somente com
[OCILob::writeTemporary](ocilob.writetemporary.md).

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::writeTemporary](ocilob.writetemporary.md)

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
