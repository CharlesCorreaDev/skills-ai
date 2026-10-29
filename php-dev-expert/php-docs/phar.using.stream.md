# Usando Arquivos Phar: o empacotador de fluxo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.using.stream.php

---

## Usando Arquivos Phar: o empacotador de fluxo phar

O empacotador de fluxo Phar suporta totalmente [fopen()](function.fopen.md) para
leitura e gravação (não anexação), [unlink()](function.unlink.md), [stat()](function.stat.md),
[fstat()](function.fstat.md), [fseek()](function.fseek.md), [rename()](function.rename.md)
e operações de fluxo de diretório [opendir()](function.opendir.md), [rmdir()](function.rmdir.md)
e [mkdir()](function.mkdir.md).

A compactação de arquivos individuais e os metadados por arquivo também podem ser manipulados
em um arquivo Phar usando contextos de fluxo:

```
<?php
$context = stream_context_create(array('phar' =>
                                    array('compress' => Phar::GZ)),
                                    array('metadata' => array('user' => 'cellog')));
file_put_contents('phar://meu.phar/algumarquivo.php', 0, $context);
?>
```

O empacotador de fluxo `phar` não opera em arquivos remotos,
e não pode operar em arquivos remotos, sendo, portanto, permitido mesmo quando as opções INI
[allow\_url\_fopen](filesystem.configuration.md#ini.allow-url-fopen) e
[allow\_url\_include](filesystem.configuration.md#ini.allow-url-include)
estão desabilitadas.

Embora seja possível criar arquivos PHAR do zero usando apenas
operações de fluxo, é melhor usar a funcionalidade incorporada
à classe Phar. O empacotador de fluxo é mais adequado para operações somente leitura.

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
