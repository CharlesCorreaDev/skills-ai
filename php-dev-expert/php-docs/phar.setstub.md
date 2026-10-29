# Usado para definir o carregador PHP ou o stub de inicialização de um arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.setstub.php

---

# Phar::setStub

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::setStub — Usado para definir o carregador PHP ou o stub de inicialização de um arquivo Phar

### Descrição

public function **Phar::setStub**([resource](language.types.resource.md)|[string](language.types.string.md) `$stub`, [int](language.types.integer.md) `$length` = -1): [true](language.types.singleton.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Este método é usado para adicionar um stub de carregador de inicialização PHP a um novo arquivo Phar, ou
para substituir o stub de carregador em um arquivo Phar existente.

O stub do carregador para um arquivo Phar é usado sempre que um arquivo é incluído diretamente
como neste exemplo:

```
<?php
include 'meuphar.phar';
?>
```

ou por execução simples:

```
php meuphar.phar
```

O carregador não é acessado ao incluir um arquivo por meio do empacotador de fluxo `phar`
como a seguir:

```
<?php
include 'phar://meuphar.phar/algumarquivo.php';
?>
```

### Parâmetros

`stub`
:   Uma string ou um identificador de fluxo aberto para usar como stub executável para este
    arquivo phar.

`length`
:   Comprimento de `stub` em bytes.

    **Aviso**

    Passar o argumento `length` com um [resource](language.types.resource.md) no
    primeiro argumento está *DESCONTINUADO* a partir do PHP 8.3.0.
    Em vez disso, use `$phar->setStub(stream_get_contents($resource))`.

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
| 8.4.0 | O tipo do retorno agora é **`true`**; anteriormente, era [bool](language.types.boolean.md). |
| 8.3.0 | Chamar **Phar::setStub()** com um [resource](language.types.resource.md) e um `length` agora está descontinuado. Tais chamadas devem ser substituídas por: `$phar->setStub(stream_get_contents($resource));` |

### Examples

**Exemplo #1 Um exemplo de **Phar::setStub()****

```
<?php

try {
    $p = new Phar(dirname(__FILE__) . '/novophar.phar', 0, 'novophar.phar');
    $p['a.php'] = '<?php var_dump("Olá");';
    $p->setStub('<?php var_dump("Primeiro"); Phar::mapPhar("novophar.phar"); __HALT_COMPILER(); ?>');
    include 'phar://novophar.phar/a.php';
    var_dump($p->getStub());

    $p['b.php'] = '<?php var_dump("Mundo");';
    $p->setStub('<?php var_dump("Segundo"); Phar::mapPhar("novophar.phar"); __HALT_COMPILER(); ?>');
    include 'phar://novophar.phar/b.php';
    var_dump($p->getStub());
} catch (Exception $e) {
    echo 'As operações de gravação falharam em novophar.phar: ', $e;
}
?>
```

O exemplo acima produzirá:

```
string(5) "Olá"
string(82) "<?php var_dump("Primeiro"); Phar::mapPhar("novophar.phar"); __HALT_COMPILER(); ?>"
string(5) "Mundo"
string(83) "<?php var_dump("Segundo"); Phar::mapPhar("novophar.phar"); __HALT_COMPILER(); ?>"
```

### Veja também

- [Phar::getStub()](phar.getstub.md) - Retorna o carregador PHP ou o stub de inicialização de um arquivo Phar
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
