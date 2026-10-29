# Testa o fim de arquivo no descritor de um objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.eof.php

---

# OCILob::eof

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::eof — Testa o fim de arquivo no descritor de um objeto grande

### Descrição

public function **OCILob::eof**(): [bool](language.types.boolean.md)

Informa se o ponteiro interno do objeto grande está no final do LOB.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** se o ponteiro interno do objeto grande estiver no final do LOB.
Caso contrário, retorna **`false`**.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Notas

> **Nota**:
>
> Esta função retornará um erro Oracle se [OCILob::setBuffering](ocilob.setbuffering.md) estiver habilitado no LOB.

### Veja também

- [OCILob::size](ocilob.size.md)

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
