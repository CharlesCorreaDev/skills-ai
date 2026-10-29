# Exporta o conteúdo do LOB para um arquivo

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.export.php

---

# OCILob::export

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::export — Exporta o conteúdo do LOB para um arquivo

### Descrição

public function **OCILob::export**([string](language.types.string.md) `$filename`, [?](language.types.null.md)[int](language.types.integer.md) `$offset` = **`null`**, [?](language.types.null.md)[int](language.types.integer.md) `$length` = **`null`**): [bool](language.types.boolean.md)

Exporta o conteúdo do LOB para um arquivo.

### Parâmetros

`filename`
:   Caminho para o arquivo.

`offset`
:   Indica de onde a exportação deve começar.

`length`
:   Indica o comprimento dos dados a serem exportados.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | `offset` e `length` agora são anuláveis. |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::import](ocilob.import.md)

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
