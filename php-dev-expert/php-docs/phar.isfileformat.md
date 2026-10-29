# Informa se o arquivo phar é baseado no formato de arquivo tar/phar/zip dependendo do parâmetro

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.isfileformat.php

---

# Phar::isFileFormat

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::isFileFormat — Informa se o arquivo phar é baseado no formato de arquivo tar/phar/zip dependendo do parâmetro

### Descrição

public function **Phar::isFileFormat**([int](language.types.integer.md) `$format`): [bool](language.types.boolean.md)

### Parâmetros

`format`
:   `Phar::PHAR`, `Phar::TAR` ou
    `Phar::ZIP` para testar o formato do arquivo.

### Valor Retornado

Retorna **`true`** se o arquivo phar corresponder ao formato de arquivo solicitado pelo parâmetro.

### Erros/Exceções

[PharException](class.pharexception.md) é lançada se o parâmetro for um especificador de formato de arquivo
desconhecido.

### Veja também

- [Phar::convertToExecutable()](phar.converttoexecutable.md) - Converte um arquivo phar em outro formato de arquivo executável phar
- [Phar::convertToData()](phar.converttodata.md) - Converte um arquivo phar em um arquivo tar ou zip não executável

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
