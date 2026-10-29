# Salva dados no objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.save.php

---

# OCILob::save

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::save — Salva dados no objeto grande

### Descrição

public function **OCILob::save**([string](language.types.string.md) `$data`, [int](language.types.integer.md) `$offset` = 0): [bool](language.types.boolean.md)

Salva os dados informados em `data` no objeto grande.

### Parâmetros

`data`
:   Os dados a serem salvos.

`offset`
:   Pode ser usado para indicar a posição de início no objeto grande.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::write](ocilob.write.md)
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
