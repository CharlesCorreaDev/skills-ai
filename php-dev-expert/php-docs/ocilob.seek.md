# Define o ponteiro interno do objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.seek.php

---

# OCILob::seek

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::seek — Define o ponteiro interno do objeto grande

### Descrição

public function **OCILob::seek**([int](language.types.integer.md) `$offset`, [int](language.types.integer.md) `$whence` = **`OCI_SEEK_SET`**): [bool](language.types.boolean.md)

Define o ponteiro interno do objeto grande.

### Parâmetros

`offset`
:   Indica a quantidade de bytes, na qual o ponteiro interno deve ser
    movido a partir da posição apontada por `whence`.

`whence`
:   Pode ser um dos seguintes:

    - **`OCI_SEEK_SET`** - define a posição igual a
      `offset`
    - **`OCI_SEEK_CUR`** - adiciona `offset`
      bytes à posição atual
    - **`OCI_SEEK_END`** - adiciona `offset`
      bytes ao final do objeto grande (use valor negativo para mover para uma posição
      antes do fim do objeto grande)

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::rewind](ocilob.rewind.md)
- [OCILob::tell](ocilob.tell.md)
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
