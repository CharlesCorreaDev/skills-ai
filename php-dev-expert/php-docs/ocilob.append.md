# Acrescenta dados do objeto grande a outro objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.append.php

---

# OCILob::append

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::append — Acrescenta dados do objeto grande a outro objeto grande

### Descrição

public function **OCILob::append**([OCILob](class.ocilob.md) `$from`): [bool](language.types.boolean.md)

Acrescenta dados do objeto grande ao final de outro objeto grande.

Escrever no objeto grande com este método falhará se o buffer foi
habilitado anteriormente. Deve-se desabilitar o buffer antes de anexar. Pode
ser necessário liberar os buffers com [OCILob::flush](ocilob.flush.md) antes
de desabilitar o buffer.

### Parâmetros

`from`
:   O LOB copiado.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::flush](ocilob.flush.md)
- [OCILob::setBuffering](ocilob.setbuffering.md)
- [OCILob::getBuffering](ocilob.getbuffering.md)

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
