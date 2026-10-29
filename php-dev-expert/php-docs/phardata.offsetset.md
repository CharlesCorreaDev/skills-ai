# Define o conteúdo de um arquivo dentro do tar/zip para o de um arquivo externo ou string

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.offsetset.php

---

# PharData::offsetSet

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::offsetSet — Define o conteúdo de um arquivo dentro do tar/zip para o de um arquivo externo ou string

### Descrição

public function **PharData::offsetSet**([string](language.types.string.md) `$localName`, [resource](language.types.resource.md)|[string](language.types.string.md) `$value`): [void](language.types.void.md)

Esta é uma implementação da interface [ArrayAccess](class.arrayaccess.md) que permite
a manipulação direta do conteúdo de um arquivo tar/zip usando
colchetes de acesso a arrays. offsetSet é usado para modificar um
arquivo existente ou adicionar um novo arquivo a um arquivo tar/zip.

### Parâmetros

`localName`
:   O nome do arquivo (caminho relativo) a ser modificado em um arquivo tar ou zip.

`value`
:   Conteúdo do arquivo.

### Valor Retornado

Sem valores de retorno.

### Erros/Exceções

Lança
[PharException](class.pharexception.md) se houver algum problema ao liberar
as alterações feitas no arquivo tar/zip para o disco.

### Examples

**Exemplo #1 Um exemplo de **PharData::offsetSet()****

offsetSet não deve ser acessado diretamente, mas sim usado
por meio de acesso a array com o operador `[]`.

```
<?php
$p = new PharData('/caminho/para/meu.tar');
try {
    // chama offsetSet
    $p['arquivo.txt'] = 'Olá mundo';
} catch (Exception $e) {
    echo 'Não foi possível modificar arquivo.txt:', $e;
}
?>
```

### Notas

> **Nota**:
>
> [PharData::addFile()](phardata.addfile.md), [PharData::addFromString()](phardata.addfromstring.md) e **PharData::offsetSet()**
> salvam um novo arquivo phar cada vez que são chamadas. Se o desempenho for uma preocupação,
> [PharData::buildFromDirectory()](phardata.buildfromdirectory.md) ou [PharData::buildFromIterator()](phardata.buildfromiterator.md)
> devem ser usadas.

### Veja também

- [Phar::offsetSet()](phar.offsetset.md) - Define o conteúdo de um arquivo interno para o de um arquivo externo

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
