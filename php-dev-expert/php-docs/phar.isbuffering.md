# Usado para determinar se as operações de gravação Phar estão sendo armazenadas em buffer ou estão sendo liberadas diretamente no disco

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.isbuffering.php

---

# Phar::isBuffering

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::isBuffering — Usado para determinar se as operações de gravação Phar estão sendo armazenadas em buffer ou estão sendo liberadas diretamente no disco

### Descrição

public function **Phar::isBuffering**(): [bool](language.types.boolean.md)

Este método pode ser usado para determinar se um Phar salvará as alterações
no disco imediatamente ou se uma chamada para [Phar::stopBuffering()](phar.stopbuffering.md)
é necessária para permitir o salvamento das alterações.

O buffer de gravação Phar é por arquivo, o buffer ativo para o arquivo Phar
`foo.phar` não afeta as alterações
no arquivo Phar `bar.phar`.

### Parâmetros

Esta função não possui parâmetros.

### Valor Retornado

Retorna **`true`** se as operações de gravação estão sendo armazenadas em buffer, **`false`** caso contrário.

### Examples

**Exemplo #1 Um exemplo de **Phar::isBuffering()****

```
<?php
$p = new Phar(dirname(__FILE__) . '/novo.phar', 0, 'novo.phar');
$p2 = new Phar('pharexistente.phar');
$p['arquivo1.txt'] = 'olá';
var_dump($p->isBuffering());
var_dump($p2->isBuffering());
?>
=2=
<?php
$p->startBuffering();
var_dump($p->isBuffering());
var_dump($p2->isBuffering());
$p->stopBuffering();
?>
=3=
<?php
var_dump($p->isBuffering());
var_dump($p2->isBuffering());
?>
```

O exemplo acima produzirá:

```
bool(false)
bool(false)
=2=
bool(true)
bool(false)
=3=
bool(false)
bool(false)
```

### Veja também

- [Phar::startBuffering()](phar.startbuffering.md) - Inicia o buffer das operações de gravação Phar, não modifica o objeto Phar no disco
- [Phar::stopBuffering()](phar.stopbuffering.md) - Interrompe o buffer de solicitações de gravação no arquivo Phar e salva as alterações no disco

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
