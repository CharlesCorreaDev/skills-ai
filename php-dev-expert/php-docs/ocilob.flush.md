# Libera/grava o buffer do LOB no servidor

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.flush.php

---

# OCILob::flush

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::flush — Libera/grava o buffer do LOB no servidor

### Descrição

public function **OCILob::flush**([int](language.types.integer.md) `$flag` = 0): [bool](language.types.boolean.md)

**OCILob::flush()** realmente grava dados no servidor.

### Parâmetros

`flag`
:   Por padrão, os recursos não são liberados, mas usando o sinalizador
    **`OCI_LOB_BUFFER_FREE`** isso pode ser feito explicitamente.
    Deve-se ter certeza do que se está fazendo - a próxima operação de leitura/gravação para a
    mesma parte do LOB envolverá uma viagem de ida e volta para o servidor e inicializará
    novos recursos de buffer. É recomendado usar o sinalizador
    **`OCI_LOB_BUFFER_FREE`** somente quando não haverá
    mais trabalho com o LOB.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

Retorna **`false`** se o buffer não foi habilitado ou ocorreu um erro.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::getBuffering](ocilob.getbuffering.md)
- [OCILob::setBuffering](ocilob.setbuffering.md)

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
