# Retorna o tamanho do objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.size.php

---

# OCILob::size

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::size — Retorna o tamanho do objeto grande

### Descrição

public function **OCILob::size**(): [int](language.types.integer.md)|[false](language.types.singleton.md)

Obtém o tamanho do objeto grande.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o comprimento do valor do objeto grande ou **`false`** em caso de falha.
Objetos vazios têm comprimento zero.

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
