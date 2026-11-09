# Lê parte do objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.read.php

---

# OCILob::read

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::read — Lê parte do objeto grande

### Descrição

public function **OCILob::read**([int](language.types.integer.md) `$length`): [string](language.types.string.md)|[false](language.types.singleton.md)

Lê o número de bytes (BLOB) ou caracteres (CLOB) especificado em `length`
a partir da posição atual do ponteiro interno do LOB.

A leitura para quando `length` bytes foram lidos para um BLOB,
quando `length` caracteres foram lidos para um CLOB,
ou quando o fim do objeto grande é alcançado. O ponteiro interno do objeto grande
será deslocado na quantidade de bytes/caracteres lidos.

### Parâmetros

`length`
:   O comprimento dos dados a serem lidos, em bytes (BLOB) ou caracteres (CLOB).
    Valores grandes serão arredondados para 1 MB.

### Valor Retornado

Retorna o conteúdo como uma string, ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::load](ocilob.load.md)
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
