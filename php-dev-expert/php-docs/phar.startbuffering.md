# Inicia o buffer das operações de gravação Phar, não modifica o objeto Phar no disco

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.startbuffering.php

---

# Phar::startBuffering

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::startBuffering — Inicia o buffer das operações de gravação Phar, não modifica o objeto Phar no disco

### Descrição

public function **Phar::startBuffering**(): [void](language.types.void.md)

Embora tecnicamente desnecessário, o método **Phar::startBuffering()**
pode proporcionar um aumento significativo de desempenho ao criar ou modificar um
arquivo Phar com um grande número de arquivos. Normalmente, sempre que um arquivo
dentro de um arquivo Phar é criado ou modificado de alguma forma, todo o arquivo Phar
será recriado com as alterações. Dessa forma, o arquivo
estará atualizado com a atividade realizada nele.

No entanto, isso pode ser desnecessário ao simplesmente criar um novo arquivo Phar,
quando faria mais sentido gravar o arquivo inteiro de uma só vez.
Da mesma forma, muitas vezes é necessário fazer uma série de alterações e garantir
que todas elas sejam possíveis antes de fazer qualquer alteração no disco, semelhante ao
conceito de transações de banco de dados relacional. O
par de métodos **Phar::startBuffering()**/[Phar::stopBuffering()](phar.stopbuffering.md)
é fornecido para esse propósito.

O buffer de gravação Phar é por arquivo, o buffer ativo para o arquivo Phar
`foo.phar` não afeta as alterações
no arquivo Phar `bar.phar`.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Nenhum valor é retornado.

### Examples

**Exemplo #1 Um exemplo de **Phar::startBuffering()****

```
<?php
// garantindo que o arquivo não existe
@unlink('novophar.phar');
try {
    $p = new Phar(dirname(__FILE__) . '/novophar.phar', 0, 'novophar.phar');
} catch (Exception $e) {
    echo 'Não foi possível criar o phar:', $e;
}
echo 'O novo phar tem ' . $p->count() . " entradas\n";
$p->startBuffering();
$p['arquivo.txt'] = 'olá';
$p['arquivo2.txt'] = 'pessoal';
$p['arquivo2.txt']->setCompressedGZ();
$p['arquivo3.txt'] = 'carafeliz';
$p['arquivo3.txt']->setMetadata(42);
$p->setStub("<?php
function __autoload($class)
{
    include 'phar://meuphar.phar/' . str_replace('_', '/', $class) . '.php';
}
Phar::mapPhar('meuphar.phar');
include 'phar://meuphar.phar/startup.php';
__HALT_COMPILER();");
$p->stopBuffering();
?>
```

### Veja também

- [Phar::stopBuffering()](phar.stopbuffering.md) - Interrompe o buffer de solicitações de gravação no arquivo Phar e salva as alterações no disco
- [Phar::isBuffering()](phar.isbuffering.md) - Usado para determinar se as operações de gravação Phar estão sendo armazenadas em buffer ou estão sendo liberadas diretamente no disco

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
