# Exclui os metadados da entrada

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pharfileinfo.delmetadata.php

---

# PharFileInfo::delMetadata

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.2.0)

PharFileInfo::delMetadata — Exclui os metadados da entrada

### Descrição

public function **PharFileInfo::delMetadata**(): [true](language.types.singleton.md)

Exclui os metadados da entrada, se existirem.

### Parâmetros

Sem parâmetros.

### Valor Retornado

Sempre retorna **`true`**.
Assim como acontece com todas as funcionalidades que modificam o conteúdo de
um phar, a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
deve estar desativada para funcionar se o arquivo estiver dentro de um arquivo [Phar](class.phar.md).
Arquivos dentro de arquivos [PharData](class.phardata.md) não têm
essa restrição.

### Erros/Exceções

Lança [PharException](class.pharexception.md) se ocorrerem erros ao liberar
as alterações no disco e [BadMethodCallException](class.badmethodcallexception.md) se
o acesso de gravação estiver desabilitado.

### Examples

**Exemplo #1 Um exemplo de **PharFileInfo::delMetaData()****

```
<?php
try {
    $a = new Phar('meuphar.phar');
    $a['olá'] = 'olá';
    var_dump($a['olá']->delMetadata());
    $a['olá']->setMetadata('pessoal');
    var_dump($a['olá']->delMetadata());
    var_dump($a['olá']->delMetadata());
} catch (Exception $e) {
    // lida com erros
}
?>
```

O exemplo acima produzirá:

```
bool(false)
bool(true)
bool(false)
```

### Veja também

- [PharFileInfo::setMetadata()](pharfileinfo.setmetadata.md) - Define metadados específicos de arquivo salvos com um arquivo
- [PharFileInfo::hasMetadata()](pharfileinfo.hasmetadata.md) - Retorna os metadados da entrada
- [PharFileInfo::getMetadata()](pharfileinfo.getmetadata.md) - Retorna metadados específicos do arquivo salvos com um arquivo
- [Phar::setMetadata()](phar.setmetadata.md) - Define metadados do arquivo phar
- [Phar::hasMetadata()](phar.hasmetadata.md) - Informa se o phar tem metadados globais
- [Phar::getMetadata()](phar.getmetadata.md) - Retorna metadados do arquivo phar

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
