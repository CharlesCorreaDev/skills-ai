# Define bits de permissão específicos do arquivo

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pharfileinfo.chmod.php

---

# PharFileInfo::chmod

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

PharFileInfo::chmod — Define bits de permissão específicos do arquivo

### Descrição

public function **PharFileInfo::chmod**([int](language.types.integer.md) `$perms`): [void](language.types.void.md)

**PharFileInfo::chmod()** permite a configuração do bit de permissão
do arquivo executável, bem como bits somente leitura. Os bits graváveis ​​são
ignorados e definidos em tempo de execução com base na
variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly).
Assim como acontece com todas as funcionalidades que modificam o conteúdo de
um phar, a variável INI [phar.readonly](phar.configuration.md#ini.phar.readonly)
deve estar desativada para funcionar se o arquivo estiver dentro de um arquivo [Phar](class.phar.md).
Arquivos dentro de arquivos [PharData](class.phardata.md) não têm
essa restrição.

### Parâmetros

`perms`
:   permissões (consulte [chmod()](function.chmod.md))

### Valor Retornado

Nenhum valor é retornado.

### Examples

**Exemplo #1 Um exemplo de **PharFileInfo::chmod()****

```
<?php
// garantindo que o arquivo não existe
@unlink('novophar.phar');
try {
    $p = new Phar('novophar.phar', 0, 'novophar.phar');
    $p['arquivo.sh'] = '#!/usr/local/lib/php
    <?php echo "olá"; ?>';
    // define o bit executável
    $p['arquivo.sh']->chmod(0555);
    var_dump($p['arquivo.sh']->isExecutable());
} catch (Exception $e) {
    echo 'Não foi possível criar/modificar o phar: ', $e;
}
?>
```

O exemplo acima produzirá:

```
bool(true)
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
