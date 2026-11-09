# Instrui phar a interceptar fopen, file_get_contents, opendir e todas as funções relacionadas a stat

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.interceptfilefuncs.php

---

# Phar::interceptFileFuncs

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::interceptFileFuncs — Instrui phar a interceptar fopen, file\_get\_contents, opendir e todas as funções relacionadas a stat

### Descrição

final public static function **Phar::interceptFileFuncs**(): [void](language.types.void.md)

Instrui o phar a interceptar [fopen()](function.fopen.md), [readfile()](function.readfile.md),
[file\_get\_contents()](function.file-get-contents.md), [opendir()](function.opendir.md) e todas as
funções relacionadas a stat. Se qualquer uma dessas funções for chamada de dentro
de um arquivo phar com um caminho relativo, a chamada será modificada para acessar um arquivo
dentro do arquivo phar. Caminhos absolutos são considerados tentativas de carregar
arquivos externos do sistema de arquivos.

Esta função possibilita executar aplicações PHP projetadas para rodar em um disco
rígido como uma aplicação PHAR.

### Parâmetros

Sem parâmetros.

### Valor Retornado

### Examples

**Exemplo #1 Um exemplo de **Phar::interceptFileFuncs()****

```
<?php
Phar::interceptFileFuncs();
include 'phar://' . __FILE__ . '/file.php';
?>
```

Supondo que este phar esteja em `/path/to/myphar.phar` e
contenha `file.php` e
`file2.txt`, se `file.php` contiver este código:

**Exemplo #2 Um exemplo de **Phar::interceptFileFuncs()****

```
<?php
echo file_get_contents('file2.txt');
?>
```

Normalmente, o PHP pesquisaria o diretório atual por `file2.txt`,
que seria traduzido como o diretório de file.php ou o diretório atual de
um usuário de linha de comando. **Phar::interceptFileFuncs()** instrui
o PHP a considerar o diretório atual como `phar:///path/to/myphar.phar/`
e, assim, abre `phar:///path/to/myphar.phar/file2.txt` no código
de exemplo acima.

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
