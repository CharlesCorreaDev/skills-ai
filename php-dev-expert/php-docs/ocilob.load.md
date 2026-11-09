# Retorna o conteúdo de um objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.load.php

---

# OCILob::load

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::load — Retorna o conteúdo de um objeto grande

### Descrição

public function **OCILob::load**(): [string](language.types.string.md)|[false](language.types.singleton.md)

Retorna o conteúdo do objeto grande. Como a execução do script é encerrada
quando o limite de memória definido em [memory\_limit](ini.core.md#ini.memory-limit) é atingido,
garanta que o LOB não exceda esse limite. Na maioria dos casos, é
recomendado usar [OCILob::read](ocilob.read.md) em vez disso.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna o conteúdo do objeto, ou **`false`** em caso de erros.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::read](ocilob.read.md)

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
