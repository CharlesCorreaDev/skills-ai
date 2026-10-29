# Retorna a posição atual do ponteiro interno do objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.tell.php

---

# OCILob::tell

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::tell — Retorna a posição atual do ponteiro interno do objeto grande

### Descrição

public function **OCILob::tell**(): [int](language.types.integer.md)|[false](language.types.singleton.md)

Obtém a posição atual do ponteiro interno de um LOB.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna a posição atual do ponteiro interno de um LOB ou **`false`** se um
erro ocorreu.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::rewind](ocilob.rewind.md)
- [OCILob::size](ocilob.size.md)
- [OCILob::eof](ocilob.eof.md)

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
