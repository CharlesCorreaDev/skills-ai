# Constrói um objeto de arquivo tar ou zip não executável

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.construct.php

---

# PharData::\_\_construct

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::\_\_construct — Constrói um objeto de arquivo tar ou zip não executável

### Descrição

public function **PharData::\_\_construct**(  
    [string](language.types.string.md) `$filename`,  
    [int](language.types.integer.md) `$flags` = FilesystemIterator::SKIP\_DOTS | FilesystemIterator::UNIX\_PATHS,  
    [?](language.types.null.md)[string](language.types.string.md) `$alias` = **`null`**,  
    [int](language.types.integer.md) `$format` = 0  
)

### Parâmetros

`filename`
:   Caminho para um arquivo tar/zip existente ou arquivo a ser criado

`flags`
:   Sinalizadores a serem passados ​​para a classe pai [Phar](class.phar.md),
    [RecursiveDirectoryIterator](class.recursivedirectoryiterator.md).

`alias`
:   Apelido ​​com o qual este arquivo Phar deve ser referenciado em chamadas para funcionalidade
    de fluxo.

`format`
:   Uma das
    [constantes de formato de arquivo](phar.constants.md#phar.constants.fileformat)
    disponíveis na classe [Phar](class.phar.md).

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se chamado duas vezes;
[UnexpectedValueException](class.unexpectedvalueexception.md) se o arquivo Phar não puder
ser aberto.

### Examples

**Exemplo #1 Um exemplo de **PharData::\_\_construct()****

```
<?php
try {
    $p = new PharData('/caminho/para/meu.tar', Phar::CURRENT_AS_FILEINFO | Phar::KEY_AS_FILENAME);
} catch (UnexpectedValueException $e) {
    die('Não foi possível abrir meu.tar');
} catch (BadMethodCallException $e) {
    echo 'Tecnicamente, isto não pode acontecer';
}
echo file_get_contents('phar:///caminho/para/meu.tar/exemplo.txt');
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
