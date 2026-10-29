# Constrói um objeto de entrada Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pharfileinfo.construct.php

---

# PharFileInfo::\_\_construct

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

PharFileInfo::\_\_construct — Constrói um objeto de entrada Phar

### Descrição

public function **PharFileInfo::\_\_construct**([string](language.types.string.md) `$filename`)

Este método não deve ser chamado diretamente. Em vez disso, um objeto PharFileInfo
é inicializado chamando [Phar::offsetGet()](phar.offsetget.md)
por meio de acesso a array.

### Parâmetros

`filename`
:   A URL completa para recuperar um arquivo. Se for necessário recuperar as informações
    do arquivo `meu/arquivo.php` do diretório `boo.phar`,
    a entrada deve ser `phar://boo.phar/meu/arquivo.php`.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se
[\_\_construct()](language.oop5.decon.md#object.construct) for chamado duas vezes.
Lança [UnexpectedValueException](class.unexpectedvalueexception.md) se
a URL do phar solicitada estiver incorreta, o phar solicitado
não puder ser aberto ou o arquivo não puder ser encontrado dentro do phar.

### Examples

**Exemplo #1 Um exemplo de **PharFileInfo::\_\_construct()****

```
<?php
try {
    $p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar');
    $p['arquivoteste.txt'] = "bom\ndia\npessoal";
    $file = $p['arquivoteste.txt'];
    foreach ($file as $line => $text) {
        echo "linha número $line: $text";
    }
    // isto também funciona
    $file = new PharFileInfo('phar:///caminho/para/meu.phar/arquivoteste.txt');
    foreach ($file as $line => $text) {
        echo "linha número $line: $text";
    }
} catch (Exception $e) {
    echo 'Operações Phar falharam: ', $e;
}
?>
```

O exemplo acima produzirá:

```
linha número 1: bom
linha número 2: dia
linha número 3: pessoal
linha número 1: bom
linha número 2: dia
linha número 3: pessoal
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
