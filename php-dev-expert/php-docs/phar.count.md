# Retorna o número de entradas (arquivos) no arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.count.php

---

# Phar::count

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::count — Retorna o número de entradas (arquivos) no arquivo Phar

### Descrição

public function **Phar::count**([int](language.types.integer.md) `$mode` = **`COUNT_NORMAL`**): [int](language.types.integer.md)

### Parâmetros

`mode`
:   `mode` é um valor inteiro que especifica o modo de contagem a ser usado.
    Por padrão, é definido como **`COUNT_NORMAL`**,
    que conta apenas o número de itens no arquivo que não foram excluídos ou ocultados.
    Quando definido como **`COUNT_RECURSIVE`**, conta todos os itens no arquivo,
    incluindo aqueles que foram excluídos ou ocultados.

### Valor Retornado

O número de arquivos contidos neste phar, ou `0` (o número zero)
se não houver nenhum.

### Examples

**Exemplo #1 Um exemplo de **Phar::count()****

```
<?php
// garantindo que o arquivo não existe
@unlink('brandnewphar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/brandnewphar.phar', 0, 'brandnewphar.phar');
} catch (Exception $e) {
    echo 'Não foi possível criar o phar:', $e;
}
echo 'O novo phar tem ' . $p->count() . " entradas\n";
$p['file.txt'] = 'olá';
echo 'O novo phar tem ' . $p->count() . " entradas\n";
?>
```

O exemplo acima produzirá:

```
O novo phar tem 0 entradas
O novo phar tem 1 entradas
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
