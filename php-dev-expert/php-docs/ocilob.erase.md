# Apaga uma parte especificada dos dados internos do LOB

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.erase.php

---

# OCILob::erase

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::erase — Apaga uma parte especificada dos dados internos do LOB

### Descrição

public function **OCILob::erase**([?](language.types.null.md)[int](language.types.integer.md) `$offset` = **`null`**, [?](language.types.null.md)[int](language.types.integer.md) `$length` = **`null`**): [int](language.types.integer.md)|[false](language.types.singleton.md)

Apaga uma porção especificada dos dados internos do LOB começando em uma
posição especificada em `offset`. Se chamado sem parâmetros, ele
apaga todos os dados LOB.

Para BLOBs, apagar significa que o valor LOB existente é sobrescrito com
bytes zero. Para CLOBs, o valor LOB existente é sobrescrito com espaços.

### Parâmetros

`offset`

`length`

### Valor Retornado

Retorna o número real de caracteres/bytes apagados ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | `offset` e `length` agora são anuláveis. |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::truncate](ocilob.truncate.md)

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
