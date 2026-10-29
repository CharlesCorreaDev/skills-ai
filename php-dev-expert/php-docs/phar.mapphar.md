# Lê o arquivo atualmente em execução (um phar) e registra seu manifesto

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.mapphar.php

---

# Phar::mapPhar

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::mapPhar — Lê o arquivo atualmente em execução (um phar) e registra seu manifesto

### Descrição

final public static function **Phar::mapPhar**([?](language.types.null.md)[string](language.types.string.md) `$alias` = **`null`**, [int](language.types.integer.md) `$offset` = 0): [bool](language.types.boolean.md)

Este método estático só pode ser usado dentro do stub do carregador de um arquivo Phar
para inicializar o phar quando ele for executado diretamente ou quando
for incluído em outro script.

### Parâmetros

`alias`
:   O apelido que pode ser usado em URLs `phar://` para
    se referir a este arquivo, em vez do seu caminho completo.

`offset`
:   Variável não utilizada, serve apenas para compatibilidade com o PHP\_Archive do PEAR.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

[PharException](class.pharexception.md) é lançada se não for chamada diretamente na execução do PHP,
se nenhum token \_\_HALT\_COMPILER(); for encontrado no arquivo de origem atual ou se
o arquivo não puder ser aberto para leitura.

### Examples

**Exemplo #1 Um exemplo de **Phar::mapPhar()****

Este método deve ser usado apenas dentro do stub de carregamento de um Phar. Use
loadPhar para carregar um Phar externo na memória.

Aqui está um exemplo de stub do carregador Phar que usa mapPhar.

```
<?php
function __autoload($class)
{
    include 'phar://me.phar/' . str_replace('_', '/', $class) . '.php';
}
try {
    Phar::mapPhar('me.phar');
    include 'phar://me.phar/startup.php';
} catch (PharException $e) {
    echo $e->getMessage();
    die('Não foi possível inicializar o Phar');
}
__HALT_COMPILER();
```

### Veja também

- [Phar::loadPhar()](phar.loadphar.md) - Carrega qualquer arquivo phar com um apelido

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
