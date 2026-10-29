# Define o conteúdo de um arquivo interno para o de um arquivo externo

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.offsetset.php

---

# Phar::offsetSet

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::offsetSet — Define o conteúdo de um arquivo interno para o de um arquivo externo

### Descrição

public function **Phar::offsetSet**([string](language.types.string.md) `$localName`, [resource](language.types.resource.md)|[string](language.types.string.md) `$value`): [void](language.types.void.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Esta é uma implementação da interface [ArrayAccess](class.arrayaccess.md) que permite
a manipulação direta do conteúdo de um arquivo Phar usando
colchetes de acesso a arrays. offsetSet é usado para modificar um
arquivo existente ou adicionar um novo arquivo a um arquivo Phar.

### Parâmetros

`localName`
:   O nome do arquivo (caminho relativo) a ser modificado em um Phar.

`value`
:   Conteúdo do arquivo.

### Valor Retornado

Sem valores de retorno.

### Erros/Exceções

Se [phar.readonly](phar.configuration.md#ini.phar.readonly) for `1`,
[BadMethodCallException](class.badmethodcallexception.md) será lançada, pois modificar um Phar
só é permitido quando phar.readonly estiver definido como `0`. Lança
[PharException](class.pharexception.md) se houver algum problema ao liberar
as alterações feitas no arquivo Phar para o disco.

### Examples

**Exemplo #1 Um exemplo de **Phar::offsetSet()****

offsetSet não deve ser acessado diretamente, mas sim usado
por meio de acesso a array com o operador `[]`.

```
<?php
$p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar');
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
> [Phar::addFile()](phar.addfile.md), [Phar::addFromString()](phar.addfromstring.md) e **Phar::offsetSet()**
> salvam um novo arquivo phar cada vez que são chamadas. Se o desempenho for uma preocupação,
> [Phar::buildFromDirectory()](phar.buildfromdirectory.md) ou [Phar::buildFromIterator()](phar.buildfromiterator.md)
> devem ser usadas.

### Veja também

- [Phar::offsetExists()](phar.offsetexists.md) - Determina se um arquivo existe no phar
- [Phar::offsetGet()](phar.offsetget.md) - Obtém um objeto PharFileInfo para um arquivo específico
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
