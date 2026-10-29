# Trunca objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.truncate.php

---

# OCILob::truncate

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::truncate — Trunca objeto grande

### Descrição

public function **OCILob::truncate**([int](language.types.integer.md) `$length` = 0): [bool](language.types.boolean.md)

Trunca o LOB.

### Parâmetros

`length`
:   Se fornecido, este método truncará o LOB para
    `length` bytes. Caso contrário, ele irá
    limpar completamente o LOB.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::erase](ocilob.erase.md)

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
