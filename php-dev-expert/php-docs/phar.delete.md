# Exclui um arquivo dentro de um arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.delete.php

---

# Phar::delete

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::delete — Exclui um arquivo dentro de um arquivo phar

### Descrição

public function **Phar::delete**([string](language.types.string.md) `$localName`): [true](language.types.singleton.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Exclui um arquivo dentro de um arquivo compactado. Este é o equivalente funcional de
chamar [unlink()](function.unlink.md) no equivalente do empacotador de fluxo,
como mostrado no exemplo abaixo.

### Parâmetros

`localName`
:   Caminho dentro de um arquivo para o arquivo a ser excluído.

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança [PharException](class.pharexception.md) se ocorrerem erros durante a descarga
de alterações no disco.

### Examples

**Exemplo #1 Um exemplo de **Phar::delete()****

```
<?php
try {
    $phar = new Phar('meuphar.phar');
    $phar->delete('unlink/eu.php');
    // isso é equivalente a:
    unlink('phar://meuphar.phar/unlink/eu.php');
} catch (Exception $e) {
    // lida com erros
}
?>
```

### Veja também

- [PharData::delete()](phardata.delete.md) - Exclui um arquivo dentro de um arquivo tar/zip
- [Phar::unlinkArchive()](phar.unlinkarchive.md) - Remove completamente um arquivo phar do disco e da memória

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
