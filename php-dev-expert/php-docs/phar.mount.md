# Monta um caminho externo ou arquivo em um local virtual dentro do arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.mount.php

---

# Phar::mount

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::mount — Monta um caminho externo ou arquivo em um local virtual dentro do arquivo phar

### Descrição

final public static function **Phar::mount**([string](language.types.string.md) `$pharPath`, [string](language.types.string.md) `$externalPath`): [void](language.types.void.md)

Assim como o conceito do sistema de arquivos Unix de montar dispositivos externos em caminhos dentro da
árvore de diretórios, **Phar::mount()** permite referenciar arquivos
e diretórios externos como se estivessem dentro de um arquivo. Isso permite uma abstração
poderosa como, por exemplo, referenciar arquivos de configuração externos como se estivessem
dentro do arquivo.

### Parâmetros

`pharPath`
:   O caminho interno dentro do arquivo phar a ser usado como local do caminho montado.
    Este deve ser um caminho relativo dentro do arquivo phar e não deve existir ainda.

`externalPath`
:   Um caminho ou URL para um arquivo ou diretório externo para montar dentro do arquivo phar

### Valor Retornado

Sem retorno. [PharException](class.pharexception.md) é lançada em caso de falha.

### Erros/Exceções

Lança [PharException](class.pharexception.md) se ocorrer algum problema ao montar o caminho.

### Examples

**Exemplo #1 Um exemplo de **Phar::mount()****

O exemplo a seguir mostra o acesso a um arquivo de configuração externo como se fosse
um caminho dentro de um arquivo phar.

Primeiro, o código dentro de um arquivo phar:

```
<?php
$configuration = simplexml_load_string(file_get_contents(
    Phar::running(false) . '/config.xml'));
?>
```

A seguir, o código externo usado para montar o arquivo de configuração:

```
<?php
// primeiro configura a associação entre o config.xml abstrato
// e o real no disco
Phar::mount('phar://config.xml', '/etc/exemplo/config.xml');
// agora executa a aplicação
include '/caminho/para/arquivo.phar';
?>
```

Outro método é colocar o código de montagem dentro do stub do arquivo phar.
Aqui está um exemplo de configuração de um arquivo de configuração
padrão caso nenhuma configuração de usuário seja especificada:

```
<?php
// primeiro configura a associação entre o config.xml abstrato
// e o real no disco
if (defined('EXTERNAL_CONFIG')) {
    Phar::mount('config.xml', EXTERNAL_CONFIG);
    if (file_exists(__DIR__ . '/extra_config.xml')) {
        Phar::mount('extra.xml', __DIR__ . '/extra_config.xml');
    }
} else {
    Phar::mount('config.xml', 'phar://' . __FILE__ . '/config_padrao.xml');
    Phar::mount('extra.xml', 'phar://' . __FILE__ . '/extra_padrao.xml');
}
// agora executa a aplicação
include 'phar://' . __FILE__ . '/index.php';
__HALT_COMPILER();
?>
```

...e o código externo para carregar este arquivo phar:

```
<?php
define('EXTERNAL_CONFIG', '/etc/exemplo/config.xml');
// agora executa a aplicação
include '/caminho/para/arquivo.phar';
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
