# Retorna o estado atual de buffer para o objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.getbuffering.php

---

# OCILob::getBuffering

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::getBuffering — Retorna o estado atual de buffer para o objeto grande

### Descrição

public function **OCILob::getBuffering**(): [bool](language.types.boolean.md)

Informa se o buffer para o objeto grande está ativado ou desativado.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`false`** se o buffer para o objeto grande estiver desativado e **`true`** se
o buffer for usado.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

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
