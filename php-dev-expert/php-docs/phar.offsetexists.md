# Determina se um arquivo existe no phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.offsetexists.php

---

# Phar::offsetExists

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::offsetExists — Determina se um arquivo existe no phar

### Descrição

public function **Phar::offsetExists**([string](language.types.string.md) `$localName`): [bool](language.types.boolean.md)

Esta é uma implementação da interface [ArrayAccess](class.arrayaccess.md) que permite
a manipulação direta do conteúdo de um arquivo Phar usando
colchetes de acesso a arrays.

offsetExists() é chamado sempre que [isset()](function.isset.md) é chamado.

### Parâmetros

`localName`
:   O nome do arquivo (caminho relativo) a ser procurado em um Phar.

### Valor Retornado

Retorna **`true`** se o arquivo existe dentro do phar, ou **`false`** caso contrário.

### Examples

**Exemplo #1 Um exemplo de **Phar::offsetExists()****

```
<?php
$p = new Phar(dirname(__FILE__) . '/meu.phar', 0, 'meu.phar');
$p['primeiroarquivo.txt'] = 'primeiro arquivo';
$p['segundoarquivo.txt'] = 'segundo arquivo';
// o próximo conjunto de linhas chama offsetExists() indiretamente
var_dump(isset($p['primeiroarquivo.txt']));
var_dump(isset($p['naoexiste.txt']));
?>
```

O exemplo acima produzirá:

```
bool(true)
bool(false)
```

### Veja também

- [Phar::offsetGet()](phar.offsetget.md) - Obtém um objeto PharFileInfo para um arquivo específico
- [Phar::offsetSet()](phar.offsetset.md) - Define o conteúdo de um arquivo interno para o de um arquivo externo
- [Phar::offsetUnset()](phar.offsetunset.md) - Remove um arquivo de um phar

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
