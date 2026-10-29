# Interrompe o buffer de solicitações de gravação no arquivo Phar e salva as alterações no disco

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.stopbuffering.php

---

# Phar::stopBuffering

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::stopBuffering — Interrompe o buffer de solicitações de gravação no arquivo Phar e salva as alterações no disco

### Descrição

public function **Phar::stopBuffering**(): [void](language.types.void.md)

**Phar::stopBuffering()** é usado em conjunto com o método
[Phar::startBuffering()](phar.startbuffering.md). [Phar::startBuffering()](phar.startbuffering.md)
pode proporcionar um aumento significativo de desempenho ao criar ou modificar um
arquivo Phar com um grande número de arquivos. Normalmente, sempre que um arquivo
dentro de um arquivo Phar é criado ou modificado de alguma forma, todo o arquivo Phar
será recriado com as alterações. Dessa forma, o arquivo
estará atualizado com a atividade realizada nele.

No entanto, isso pode ser desnecessário ao simplesmente criar um novo arquivo Phar,
quando faria mais sentido gravar o arquivo inteiro de uma só vez.
Da mesma forma, muitas vezes é necessário fazer uma série de alterações e garantir
que todas elas sejam possíveis antes de fazer qualquer alteração no disco, semelhante ao
conceito de transações de banco de dados relacional. O par de métodos
[Phar::startBuffering()](phar.startbuffering.md)/**Phar::stopBuffering()**
é fornecido para esse propósito.

O buffer de gravação Phar é por arquivo, o buffer ativo para o arquivo Phar
`foo.phar` não afeta as alterações
no arquivo Phar `bar.phar`.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

[PharException](class.pharexception.md) é lançada se algum problema for encontrado
ao liberar as alterações no disco.

### Examples

**Exemplo #1 Um exemplo de **Phar::stopBuffering()****

```
<?php
$p = new Phar(dirname(__FILE__) . '/novophar.phar', 0, 'novophar.phar');
$p['arquivo.txt'] = 'olá';
$p->startBuffering();
var_dump($p->getStub());
$p->setStub("<?php
function __autoload(\$class)
{
    include 'phar://novophar.phar/' . str_replace('_', '/', \$class) . '.php';
}
Phar::mapPhar('novophar.phar');
include 'phar://novophar.phar/startup.php';
__HALT_COMPILER();");
$p->stopBuffering();
var_dump($p->getStub());
?>
```

O exemplo acima produzirá:

```
string(24) "<?php __HALT_COMPILER();"
string(195) "<?php
function __autoload($class)
{
    include 'phar://' . str_replace('_', '/', $class);
}
Phar::mapPhar('novophar.phar');
include 'phar://novophar.phar/startup.php';
__HALT_COMPILER();"
```

### Veja também

- [Phar::startBuffering()](phar.startbuffering.md) - Inicia o buffer das operações de gravação Phar, não modifica o objeto Phar no disco
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
