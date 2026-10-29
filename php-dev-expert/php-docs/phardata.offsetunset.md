# Remove um arquivo de um arquivo tar/zip

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.offsetunset.php

---

# PharData::offsetUnset

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::offsetUnset — Remove um arquivo de um arquivo tar/zip

### Descrição

public function **PharData::offsetUnset**([string](language.types.string.md) `$localName`): [void](language.types.void.md)

Esta é uma implementação da interface [ArrayAccess](class.arrayaccess.md) que permite
a manipulação direta do conteúdo de um arquivo tar/zip usando
colchetes de acesso a arrays. offsetUnset é usado para excluir um
arquivo existente e é chamado pela construção de linguagem
[unset()](function.unset.md).

### Parâmetros

`localName`
:   O nome do arquivo (caminho relativo) a ser modificado no arquivo tar/zip.

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

Lança
[PharException](class.pharexception.md) se houver algum problema ao liberar
as alterações feitas no arquivo tar/zip para o disco.

### Examples

**Exemplo #1 Um exemplo de **PharData::offsetUnset()****

```
<?php
$p = new PharData('/caminho/para/meu.zip');
try {
    // exclui arquivo.txt de meu.zip chamando offsetUnset
    unset($p['arquivo.txt']);
} catch (Exception $e) {
    echo 'Não foi possível excluir arquivo.txt: ', $e;
}
?>
```

### Veja também

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
