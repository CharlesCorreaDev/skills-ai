# Retorna o carregador PHP ou o stub de inicialização de um arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.getstub.php

---

# Phar::getStub

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::getStub — Retorna o carregador PHP ou o stub de inicialização de um arquivo Phar

### Descrição

public function **Phar::getStub**(): [string](language.types.string.md)

Os arquivos Phar contêm um carregador bootstrap, ou `stub`
escrito em PHP que é executado quando o arquivo é executado em PHP, seja por meio de
include:

```
<?php
include 'meuphar.phar';
?>
```

ou por execução simples:

```
php meuphar.phar
```

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna uma string contendo o conteúdo do carregador bootstrap (stub) do
arquivo Phar atual.

### Erros/Exceções

Lança [RuntimeException](class.runtimeexception.md) se não for possível ler
o stub do arquivo Phar.

### Examples

**Exemplo #1 Um exemplo de **Phar::getStub()****

```
<?php
$p = new Phar('/caminho/para/meu.phar', 0, 'meu.phar');
echo $p->getStub();
echo "==NEXT==\n";
$p->setStub("<?php
function __autoload($class)
{
    include 'phar://' . str_replace('_', '/', $class);
}
Phar::mapPhar('meuphar.phar');
include 'phar://meuphar.phar/startup.php';
__HALT_COMPILER(); ?>");
echo $p->getStub();
?>
```

O exemplo acima produzirá:

```
<?php __HALT_COMPILER(); ?>
==NEXT==
<?php
function __autoload($class)
{
    include 'phar://' . str_replace('_', '/', $class);
}
Phar::mapPhar('meuphar.phar');
include 'phar://meuphar.phar/startup.php';
__HALT_COMPILER(); ?>
```

### Veja também

- [Phar::setStub()](phar.setstub.md) - Usado para definir o carregador PHP ou o stub de inicialização de um arquivo Phar
- [Phar::createDefaultStub()](phar.createdefaultstub.md) - Cria um stup de formato específico de arquivo phar

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
