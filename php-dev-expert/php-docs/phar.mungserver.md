# Define uma lista de até 4 variáveis ​​$_SERVER que devem ser modificadas para execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.mungserver.php

---

# Phar::mungServer

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::mungServer — Define uma lista de até 4 variáveis ​​$\_SERVER que devem ser modificadas para execução

### Descrição

final public static function **Phar::mungServer**([array](language.types.array.md) `$variables`): [void](language.types.void.md)

**Phar::mungServer()** só deve ser chamado dentro do
stub de um arquivo phar.

Define uma lista de até 4 variáveis ​​[$\_SERVER](reserved.variables.server.md) que devem ser
modificadas para execução.
As variáveis ​​que podem ser modificadas para remover rastros da execução do PHAR são
`REQUEST_URI`, `PHP_SELF`,
`SCRIPT_NAME` e `SCRIPT_FILENAME`.

Por si só, este método não faz nada. Somente quando combinado com
[Phar::webPhar()](phar.webphar.md) ele entra em vigor, e somente quando o arquivo
solicitado é um arquivo PHP a ser analisado. Observe que as variáveis
`PATH_INFO` e `PATH_TRANSLATED`
são sempre modificadas.

Os valores originais das variáveis ​​modificadas são armazenados no array SERVER
com `PHAR_` prefixado, então, por exemplo,
`SCRIPT_NAME` seria salvo como `PHAR_SCRIPT_NAME`.

### Parâmetros

`variables`
:   Um array de qualquer uma das strings
    `REQUEST_URI`, `PHP_SELF`,
    `SCRIPT_NAME` e `SCRIPT_FILENAME`.
    Outros valores disparam uma exceção, e **Phar::mungServer()**
    diferencia maiúsculas de minúsculas.

### Valor Retornado

Sem retorno.

### Erros/Exceções

Lança [UnexpectedValueException](class.unexpectedvalueexception.md) se algum problema for
encontrado com os dados passados.

### Examples

**Exemplo #1 Um exemplo de **Phar::mungServer()****

```
<?php
// stub de exemplo
Phar::mungServer(array('REQUEST_URI'));
Phar::webPhar();
__HALT_COMPILER();
?>
```

### Veja também

- [Phar::webPhar()](phar.webphar.md) - Encaminha uma solicitação de um navegador da web para um arquivo interno dentro do arquivo phar
- [Phar::setStub()](phar.setstub.md) - Usado para definir o carregador PHP ou o stub de inicialização de um arquivo Phar

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
