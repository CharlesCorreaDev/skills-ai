# Informa se o arquivo phar pode ser modificado

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.iswritable.php

---

# Phar::isWritable

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::isWritable — Informa se o arquivo phar pode ser modificado

### Descrição

public function **Phar::isWritable**(): [bool](language.types.boolean.md)

Este método retorna **`true`** se `phar.readonly` for `0`,
e o arquivo phar atual no disco não for somente leitura.

### Parâmetros

Sem parâmetros.

### Valor Retornado

Retorna **`true`** se o arquivo phar puder ser modificado.

### Veja também

- [Phar::canWrite()](phar.canwrite.md) - Retorna se a extensão phar suporta a escrita e criação de phars
- [PharData::isWritable()](phardata.iswritable.md) - Informa se o arquivo tar/zip pode ser modificado

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
