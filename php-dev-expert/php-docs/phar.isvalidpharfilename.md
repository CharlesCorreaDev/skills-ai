# Informa se o nome de arquivo fornecido é um nome de arquivo phar válido

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.isvalidpharfilename.php

---

# Phar::isValidPharFilename

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.2.0)

Phar::isValidPharFilename — Informa se o nome de arquivo fornecido é um nome de arquivo phar válido

### Descrição

final public static function **Phar::isValidPharFilename**([string](language.types.string.md) `$filename`, [bool](language.types.boolean.md) `$executable` = **`true`**): [bool](language.types.boolean.md)

Retorna se o nome de arquivo fornecido é um nome de arquivo PHAR válido que será reconhecido
como um arquivo PHAR pela extensão PHAR. Isso pode ser usado para testar um nome sem
precisar instanciar um arquivo PHAR e capturar a inevitável exceção que será
gerada se um nome inválido for especificado.

### Parâmetros

`filename`
:   O nome ou caminho completo para um arquivo phar ainda não criado

`executable`
:   Este parâmetro determina se o nome do arquivo deve ser tratado como
    um arquivo executável phar ou um arquivo não executável de dados.

### Valor Retornado

Retorna **`true`** se o nome do arquivo for válido, **`false`** caso contrário.

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
