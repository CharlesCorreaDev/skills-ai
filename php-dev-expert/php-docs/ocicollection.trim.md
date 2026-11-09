# Corta elementos do final da coleção

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocicollection.trim.php

---

# OCICollection::trim

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCICollection::trim — Corta elementos do final da coleção

### Descrição

public function **OCICollection::trim**([int](language.types.integer.md) `$num`): [bool](language.types.boolean.md)

Corta `num` elementos do final da
coleção.

### Parâmetros

`num`
:   O número de elementos a serem cortados.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Collection** foi renomeada para [OCICollection](class.ocicollection.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCICollection::size](ocicollection.size.md)

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
