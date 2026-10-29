# Usado para definir o carregador PHP ou o stub de bootstrap de um arquivo Phar para o carregador padrão

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.setdefaultstub.php

---

# Phar::setDefaultStub

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::setDefaultStub — Usado para definir o carregador PHP ou o stub de bootstrap de um arquivo Phar para o carregador padrão

### Descrição

public function **Phar::setDefaultStub**([?](language.types.null.md)[string](language.types.string.md) `$index` = **`null`**, [?](language.types.null.md)[string](language.types.string.md) `$webIndex` = **`null`**): [true](language.types.singleton.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Este método é um método de conveniência que combina a funcionalidade de
[Phar::createDefaultStub()](phar.createdefaultstub.md) e [Phar::setStub()](phar.setstub.md).

### Parâmetros

`index`
:   Caminho relativo dentro do arquivo phar para execução se acessado na linha de comando

`webIndex`
:   Caminho relativo dentro do arquivo phar para ser executado se acessado por meio de um navegador da web

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

[UnexpectedValueException](class.unexpectedvalueexception.md) é lançada se
[phar.readonly](phar.configuration.md#ini.phar.readonly) estiver habilitado
no php.ini.
[PharException](class.pharexception.md) é lançada se algum problema for encontrado
ao liberar alterações no disco.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.4.0 | **Phar::setDefaultStub()** agora tem um retorno provisório de [true](language.types.singleton.md). |
| 8.0.0 | `webIndex` agora é anulável. |

### Examples

**Exemplo #1 Um exemplo de **Phar::setDefaultStub()****

```
<?php
try {
    $phar = new Phar('meuphar.phar');
    $phar->setDefaultStub('cli.php', 'web/index.php');
    // isso é o mesmo que:
    // $phar->setStub($phar->createDefaultStub('cli.php', 'web/index.php'));
} catch (Exception $e) {
    // lida com erros
}
?>
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
