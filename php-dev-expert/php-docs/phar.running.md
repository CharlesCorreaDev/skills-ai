# Retorna o caminho completo no disco ou a URL completa do arquivo Phar em execução no momento

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.running.php

---

# Phar::running

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::running — Retorna o caminho completo no disco ou a URL completa do arquivo Phar em execução no momento

### Descrição

final public static function **Phar::running**([bool](language.types.boolean.md) `$returnPhar` = **`true`**): [string](language.types.string.md)

Retorna o caminho completo para o arquivo phar em execução. Isso se destina a ser usado de forma muito semelhante
à constante mágica `__FILE__` e só tem efeito dentro
de um arquivo phar em execução.

Dentro do stub de um arquivo, **Phar::running()** retorna
`""`. Basta usar **`__FILE__`**
para acessar o phar em execução dentro de um stub.

### Parâmetros

`returnPhar`
:   Se **`false`**, o caminho completo no disco para o arquivo phar
    é retornado. Se **`true`**, uma URL phar completa é retornada.

### Valor Retornado

Retorna o nome do arquivo se válido, string vazia caso contrário.

### Examples

**Exemplo #1 Um exemplo de **Phar::running()****

Para o exemplo a seguir, suponha que o arquivo phar esteja localizado
em `/path/to/phar/my.phar`.

```
<?php
$a = Phar::running(); // $a é "phar:///path/to/phar/my.phar"
$b = Phar::running(false); // $b é "/path/to/phar/my.phar"
?>
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
