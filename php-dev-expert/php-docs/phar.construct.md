# Constrói um objeto de arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.construct.php

---

# Phar::\_\_construct

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::\_\_construct — Constrói um objeto de arquivo Phar

### Descrição

public function **Phar::\_\_construct**([string](language.types.string.md) `$filename`, [int](language.types.integer.md) `$flags` = FilesystemIterator::SKIP\_DOTS | FilesystemIterator::UNIX\_PATHS, [?](language.types.null.md)[string](language.types.string.md) `$alias` = **`null`**)

### Parâmetros

`filename`
:   Caminho para um arquivo Phar existente ou um arquivo a ser criado. A extensão
    do nome do arquivo deve conter .phar.

`flags`
:   Sinalizadores a serem passados ​​para a classe pai [RecursiveDirectoryIterator](class.recursivedirectoryiterator.md).

`alias`
:   Apelido ​​com o qual este arquivo Phar deve ser referenciado em chamadas para
    funcionalidade de fluxo.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se chamado duas vezes, [UnexpectedValueException](class.unexpectedvalueexception.md)
se o arquivo phar não puder ser aberto.

### Examples

**Exemplo #1 Um exemplo de **Phar::\_\_construct()****

```
<?php
try {
    $p = new Phar('/caminho/para/meu.phar', FilesystemIterator::CURRENT_AS_FILEINFO | FilesystemIterator::KEY_AS_FILENAME,
                  'meu.phar');
} catch (UnexpectedValueException $e) {
    die('Não foi possível abrir meu.phar');
} catch (BadMethodCallException $e) {
    echo 'tecnicamente, isso não pode acontecer';
}
// isso funciona agora
echo file_get_contents('phar://meu.phar/exemplo.txt');
// e funciona como se tivesse sido digitado
echo file_get_contents('phar:///caminho/para/meu.phar/exemplo.txt');
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
