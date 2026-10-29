# Importa dados de arquivo para o LOB

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.import.php

---

# OCILob::import

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::import — Importa dados de arquivo para o LOB

### Descrição

public function **OCILob::import**([string](language.types.string.md) `$filename`): [bool](language.types.boolean.md)

Grava dados do arquivo em `filename` na posição atual
do objeto grande.

### Parâmetros

`filename`
:   Caminho para o arquivo.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::export](ocilob.export.md)
- [OCILob::write](ocilob.write.md)

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
