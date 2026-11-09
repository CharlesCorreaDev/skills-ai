# Retorna metadados do arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.getmetadata.php

---

# Phar::getMetadata

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::getMetadata — Retorna metadados do arquivo phar

### Descrição

public function **Phar::getMetadata**([array](language.types.array.md) `$unserializeOptions` = []): [mixed](language.types.mixed.md)

Recupera metadados de arquivo. Metadados podem ser qualquer variável PHP que possa ser serializada.

**Cuidado**

Accessar os metadados iniciará a desserialização, que pode ativar
a execução de código PHP arbitrário. Não use isso em arquivos
phar não confiáveis ou configure o parâmetro `unserializeOptions`
de maneira segura.

### Parâmetros

Sem parâmetros.

### Valor Retornado

Qualquer valor PHP que possa ser serializado e armazenado como metadados para o arquivo Phar,
ou **`null`** se nenhum metadado tiver sido armazenado.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | O parâmetro `unserializeOptions` foi adicionado. |

### Examples

**Exemplo #1 Um exemplo de **Phar::getMetadata()****

```
<?php
// garantindo que o arquivo não existe
@unlink('novophar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/novophar.phar', 0, 'novophar.phar');
    $p['arquivo.php'] = '<?php echo "olá";';
    $p->setMetadata(array('bootstrap' => 'arquivo.php'));
    var_dump($p->getMetadata());
} catch (Exception $e) {
    echo 'Não foi possível modificar o phar:', $e;
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

- [Phar::setMetadata()](phar.setmetadata.md) - Define metadados do arquivo phar
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
