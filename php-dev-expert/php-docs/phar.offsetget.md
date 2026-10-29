# Obtém um objeto PharFileInfo para um arquivo específico

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.offsetget.php

---

# Phar::offsetGet

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::offsetGet — Obtém um objeto [PharFileInfo](class.pharfileinfo.md) para um arquivo específico

### Descrição

public function **Phar::offsetGet**([string](language.types.string.md) `$localName`): [SplFileInfo](class.splfileinfo.md)

Esta é uma implementação da interface [ArrayAccess](class.arrayaccess.md)
que permite a manipulação direta do conteúdo de um arquivo Phar usando
colchetes de acesso a arrays. **Phar::offsetGet()** é usado
para recuperar arquivos de um arquivo Phar.

### Parâmetros

`localName`
:   O nome do arquivo (caminho relativo) a ser procurado em um Phar.

### Valor Retornado

Um objeto [PharFileInfo](class.pharfileinfo.md) é retornado e pode ser usado para
iterar sobre o conteúdo de um arquivo ou recuperar informações sobre o arquivo atual.

### Erros/Exceções

Este método lança [BadMethodCallException](class.badmethodcallexception.md) se o arquivo
não existir no arquivo Phar.

### Examples

**Exemplo #1 Exemplo de **Phar::offsetGet()****

Assim como todas as classes que implementam a interface [ArrayAccess](class.arrayaccess.md),
**Phar::offsetGet()** é automaticamente
chamado ao usar o operador de colchetes angulares `[]`.

```
<?php
$p = new Phar(dirname(__FILE__) . '/meuphar.phar', 0, 'meuphar.phar');
$p['existe.txt'] = "arquivo existe\n";
try {
    // chama offsetGet() automaticamente
    echo $p['existe.txt'];
    echo $p['naoexiste.txt'];
} catch (BadMethodCallException $e) {
    echo $e;
}
?>
```

O exemplo acima produzirá:

```
arquivo existe
Entry naoexiste.txt does not exist
```

### Veja também

- [Phar::offsetExists()](phar.offsetexists.md) - Determina se um arquivo existe no phar
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
