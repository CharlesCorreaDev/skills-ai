# Move o ponteiro interno para o início do objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.rewind.php

---

# OCILob::rewind

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::rewind — Move o ponteiro interno para o início do objeto grande

### Descrição

public function **OCILob::rewind**(): [bool](language.types.boolean.md)

Define o ponteiro interno para o início do objeto grande.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::seek](ocilob.seek.md)
- [OCILob::tell](ocilob.tell.md)

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
