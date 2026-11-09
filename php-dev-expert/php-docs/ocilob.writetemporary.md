# Grava um objeto grande temporário

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.writetemporary.php

---

# OCILob::writeTemporary

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::writeTemporary — Grava um objeto grande temporário

### Descrição

public function **OCILob::writeTemporary**([string](language.types.string.md) `$data`, [int](language.types.integer.md) `$type` = **`OCI_TEMP_CLOB`**): [bool](language.types.boolean.md)

Cria um objeto grande temporário e grava os dados do parâmetro `data`
nele.

Deve ser usado [OCILob::close](ocilob.close.md) quando o trabalho com esse
objeto tiver terminado.

### Parâmetros

`data`
:   Os dados a serem gravados.

`type`
:   Pode ser um dos seguintes:

    - **`OCI_TEMP_BLOB`** é utilizado para criar BLOBs temporários
    - **`OCI_TEMP_CLOB`** é utilizado para criar CLOBs
      temporários

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para conformidade com padrões do PHP. |

### Veja também

- [OCILob::close](ocilob.close.md)

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
