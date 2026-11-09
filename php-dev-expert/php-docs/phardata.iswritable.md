# Informa se o arquivo tar/zip pode ser modificado

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.iswritable.php

---

# PharData::isWritable

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::isWritable — Informa se o arquivo tar/zip pode ser modificado

### Descrição

public function **PharData::isWritable**(): [bool](language.types.boolean.md)

Este método retorna **`true`** se o arquivo tar/zip no disco não for somente leitura.
Ao contrário de [Phar::isWritable()](phar.iswritable.md), arquivos tar/zip somente dados
podem ser modificados mesmo se `phar.readonly` estiver definido como `1`.

### Parâmetros

Sem parâmetros.

### Valor Retornado

Retorna **`true`** se o arquivo tar/zip puder ser modificado.

### Veja também

- [Phar::canWrite()](phar.canwrite.md) - Retorna se a extensão phar suporta a escrita e criação de phars
- [Phar::isWritable()](phar.iswritable.md) - Informa se o arquivo phar pode ser modificado

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
