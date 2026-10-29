# Grava dados no objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.write.php

---

# OCILob::write

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::write — Grava dados no objeto grande

### Descrição

public function **OCILob::write**([string](language.types.string.md) `$data`, [?](language.types.null.md)[int](language.types.integer.md) `$length` = **`null`**): [int](language.types.integer.md)|[false](language.types.singleton.md)

Grava dados do parâmetro `data` na
posição atual do ponteiro interno do LOB.

### Parâmetros

`data`
:   Os dados a serem gravados no LOB.

`length`
:   Se este parâmetro for um inteiro, a escrita será interrompida após
    `length` bytes terem sido escritos ou o fim de
    `data` for atingido, o que ocorrer primeiro.

### Valor Retornado

Retorna o número de bytes gravados ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | `length` agora é anulável. |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::read](ocilob.read.md)

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
