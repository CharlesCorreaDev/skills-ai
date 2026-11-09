# Define metadados do arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.setmetadata.php

---

# Phar::setMetadata

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::setMetadata — Define metadados do arquivo phar

### Descrição

public function **Phar::setMetadata**([mixed](language.types.mixed.md) `$metadata`): [void](language.types.void.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

**Phar::setMetadata()** deve ser usado para armazenar dados personalizados
que descrevam algo sobre o arquivo phar como uma entidade completa.
[PharFileInfo::setMetadata()](pharfileinfo.setmetadata.md) deve ser usado para metadados específicos do arquivo.
Metadados podem reduzir o desempenho do carregamento de um arquivo phar se os dados forem grandes.

Alguns usos possíveis para metadados incluem especificar qual arquivo dentro do arquivo
deve ser usado para inicialização, ou a localização de um manifesto de arquivo
como o arquivo package.xml do [» PEAR](https://pear.php.net/).
No entanto, quaisquer dados úteis que descrevam o arquivo phar podem ser armazenados.

### Parâmetros

`metadata`
:   Qualquer variável PHP contendo informações para armazenar que descrevem o arquivo phar.

### Valor Retornado

Nenhum valor é retornado.

### Examples

**Exemplo #1 Um exemplo de **Phar::setMetadata()****

```
<?php
// garantindo que o arquivo não existe
@unlink('novophar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/novophar.phar', 0, 'novophar.phar');
    $p['arquivo.php'] = '<?php echo "olá"';
    $p->setMetadata(array('bootstrap' => 'arquivo.php'));
    var_dump($p->getMetadata());
} catch (Exception $e) {
    echo 'Não foi possível criar e/ou modificar o phar:', $e;
}
?>
```

O exemplo acima produzirá:

```
array(1) {
  ["bootstrap"]=>
  string(11) "arquivo.php"
}
```

### Veja também

- [Phar::getMetadata()](phar.getmetadata.md) - Retorna metadados do arquivo phar
- [Phar::delMetadata()](phar.delmetadata.md) - Exclui os metadados globais do phar
- [Phar::hasMetadata()](phar.hasmetadata.md) - Informa se o phar tem metadados globais

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
