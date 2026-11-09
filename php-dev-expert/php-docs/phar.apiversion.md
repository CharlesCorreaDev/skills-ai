# Retorna a versão da API

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.apiversion.php

---

# Phar::apiVersion

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::apiVersion — Retorna a versão da API

### Descrição

final public static function **Phar::apiVersion**(): [string](language.types.string.md)

Retorna a versão da API do formato de arquivo phar que será
usado ao criar phars. A extensão Phar suporta a leitura da API
versão 1.0.0 ou mais recente. A versão 1.1.0 da API é necessária para hashes SHA-256 e SHA-512
e a versão 1.1.1 da API é necessária para armazenar diretórios vazios.

### Parâmetros

### Valor Retornado

A string de versão da API como em `"1.0.0"`.

### Examples

**Exemplo #1 Um exemplo de **Phar::apiVersion()****

```
<?php
echo Phar::apiVersion();
?>
```

O exemplo acima produzirá:

```
1.1.1
```

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
