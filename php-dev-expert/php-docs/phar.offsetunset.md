# Remove um arquivo de um phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.offsetunset.php

---

# Phar::offsetUnset

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::offsetUnset — Remove um arquivo de um phar

### Descrição

public function **Phar::offsetUnset**([string](language.types.string.md) `$localName`): [void](language.types.void.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Esta é uma implementação da interface [ArrayAccess](class.arrayaccess.md) que permite
a manipulação direta do conteúdo de um arquivo Phar usando
colchetes de acesso a arrays. offsetUnset é usado para excluir um
arquivo existente e é chamado pela construção de
linguagem [unset()](function.unset.md).

### Parâmetros

`localName`
:   O nome do arquivo (caminho relativo) a ser modificado em um Phar.

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

Se [phar.readonly](phar.configuration.md#ini.phar.readonly) for `1`,
[BadMethodCallException](class.badmethodcallexception.md) será lançada, pois modificar um Phar
só é permitido quando phar.readonly estiver definido como `0`. Lança
[PharException](class.pharexception.md) se houver algum problema ao liberar
as alterações feitas no arquivo Phar para o disco.

### Examples

**Exemplo #1 Um exemplo de **Phar::offsetUnset()****

```
<?php
$p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar');
try {
    // exclui arquivo.txt de meu.phar chamando offsetUnset
    unset($p['arquivo.txt']);
} catch (Exception $e) {
    echo 'Não foi possível excluir arquivo.txt: ', $e;
}
?>
```

### Veja também

- [Phar::offsetExists()](phar.offsetexists.md) - Determina se um arquivo existe no phar
- [Phar::offsetGet()](phar.offsetget.md) - Obtém um objeto PharFileInfo para um arquivo específico
- [Phar::offsetSet()](phar.offsetset.md) - Define o conteúdo de um arquivo interno para o de um arquivo externo
- [Phar::unlinkArchive()](phar.unlinkarchive.md) - Remove completamente um arquivo phar do disco e da memória
- [Phar::delete()](phar.delete.md) - Exclui um arquivo dentro de um arquivo phar

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
