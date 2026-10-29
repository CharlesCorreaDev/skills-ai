# Remove completamente um arquivo phar do disco e da memória

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.unlinkarchive.php

---

# Phar::unlinkArchive

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::unlinkArchive — Remove completamente um arquivo phar do disco e da memória

### Descrição

final public static function **Phar::unlinkArchive**([string](language.types.string.md) `$filename`): [true](language.types.singleton.md)

Remove um arquivo phar do disco e da memória.

### Parâmetros

`filename`
:   O caminho no disco para o arquivo phar.

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

[PharException](class.pharexception.md) é lançada se houver algum ponteiro de arquivo aberto para
o arquivo phar, ou qualquer objeto [Phar](class.phar.md), [PharData](class.phardata.md),
ou [PharFileInfo](class.pharfileinfo.md) existente que faça referência ao arquivo phar.

### Examples

**Exemplo #1 Um exemplo de **Phar::unlinkArchive()****

```
<?php
// uso simples
Phar::unlinkArchive('/caminho/para/meu.phar');

// mais um exemplo comum:
$p = new Phar('meu.phar');
$fp = fopen('phar://meu.phar/arquivo.txt', 'r');
// isto cria 'meu.phar.gz'
$gp = $p->compress(Phar::GZ);
// remove todas as referências ao arquivo
unset($p);
fclose($fp);
// agora remove todos os vestígios do arquivo
Phar::unlinkArchive('meu.phar');
?>
```

### Veja também

- [Phar::delete()](phar.delete.md) - Exclui um arquivo dentro de um arquivo phar
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
