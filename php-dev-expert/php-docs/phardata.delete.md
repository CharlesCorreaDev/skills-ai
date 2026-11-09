# Exclui um arquivo dentro de um arquivo tar/zip

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.delete.php

---

# PharData::delete

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::delete — Exclui um arquivo dentro de um arquivo tar/zip

### Descrição

public function **PharData::delete**([string](language.types.string.md) `$localName`): [true](language.types.singleton.md)

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

**Exemplo #1 Um exemplo de **PharData::delete()****

```
<?php
try {
    $phar = new PharData('meuphar.zip');
    $phar->delete('remova/me.php');
    // isto é equivalente a:
    unlink('phar://meuphar.phar/remova/me.php');
} catch (Exception $e) {
    // lida com erros
}
?>
```

### Veja também

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
