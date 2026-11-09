# Cria um stup de formato específico de arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.createdefaultstub.php

---

# Phar::createDefaultStub

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::createDefaultStub — Cria um stup de formato específico de arquivo phar

### Descrição

final public static function **Phar::createDefaultStub**([?](language.types.null.md)[string](language.types.string.md) `$index` = **`null`**, [?](language.types.null.md)[string](language.types.string.md) `$webIndex` = **`null`**): [string](language.types.string.md)

Este método destina-se à criação de stubs específicos para o formato de arquivo phar e não
se destina ao uso com arquivos phar baseados em tar ou zip.

Os arquivos Phar contêm um carregador de inicialização, ou `stub`
escrito em PHP que é executado quando o arquivo é executado em PHP, seja por meio de
include:

```
<?php
include 'meuphar.phar';
?>
```

ou por execução direta:

```
php meuphar.phar
```

Este método fornece uma maneira simples e fácil de criar um stub que irá
executar um arquivo de inicialização a partir do arquivo phar. Além disso, arquivos diferentes podem
ser especificados para executar o arquivo phar a partir da linha de comando ou através
de um servidor web. O stub do carregador também chama [Phar::interceptFileFuncs()](phar.interceptfilefuncs.md)
para permitir o agrupamento fácil de uma aplicação PHP que acessa o sistema de arquivos. Se a
extensão phar não estiver presente, o stub do carregador extrairá o arquivo phar
para um diretório temporário e, em seguida, operará nos arquivos. Uma função de desligamento
apaga os arquivos temporários ao sair.

### Parâmetros

`index`
:   Caminho relativo dentro do arquivo phar para execução se acessado na linha de comando

`webIndex`
:   Caminho relativo dentro do arquivo phar para ser executado se acessado por meio de um navegador da web

### Valor Retornado

Retorna uma string contendo o conteúdo de um carregador de inicialização personalizado (stub)
que permite que o arquivo Phar criado funcione com ou sem a extensão Phar
habilitada.

### Erros/Exceções

Lança [UnexpectedValueException](class.unexpectedvalueexception.md) se qualquer parâmetro for maior
que 400 bytes.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `index` e `webIndex` agora são anuláveis. |

### Examples

**Exemplo #1 Um exemplo de **Phar::createDefaultStub()****

```
<?php
try {
    $phar = new Phar('meuphar.phar');
    $phar->setStub($phar->createDefaultStub('cli.php', 'web/index.php'));
} catch (Exception $e) {
    // lida com os erros
}
?>
```

### Veja também

- [Phar::setStub()](phar.setstub.md) - Usado para definir o carregador PHP ou o stub de inicialização de um arquivo Phar
- [Phar::getStub()](phar.getstub.md) - Retorna o carregador PHP ou o stub de inicialização de um arquivo Phar

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
