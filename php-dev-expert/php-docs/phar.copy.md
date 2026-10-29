# Copia um arquivo interno do arquivo phar para outro novo arquivo dentro do phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.copy.php

---

# Phar::copy

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::copy — Copia um arquivo interno do arquivo phar para outro novo arquivo dentro do phar

### Descrição

public function **Phar::copy**([string](language.types.string.md) `$from`, [string](language.types.string.md) `$to`): [true](language.types.singleton.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Copia um arquivo interno do arquivo phar para outro novo arquivo dentro do phar.
Esta é uma alternativa orientada a objetos ao uso de [copy()](function.copy.md) com
o empacotador de fluxo phar.

### Parâmetros

`from`

`to`

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança uma [UnexpectedValueException](class.unexpectedvalueexception.md) se o arquivo de origem não
existir, se o arquivo de destino já existir, se o acesso de gravação estiver desabilitado, se a abertura
do arquivo falhar, se a leitura do arquivo de origem falhar ou uma [PharException](class.pharexception.md)
se a gravação das alterações no arquivo phar falhar.

### Examples

**Exemplo #1 Um exemplo de **Phar::copy()****

Este exemplo mostra o uso de **Phar::copy()** e o
desempenho equivalente do empacotador de fluxo para a mesma coisa. A principal
diferença entre as duas abordagens é o tratamento de erros. Todos os métodos Phar
geram exceções, enquanto o empacotador de fluxo usa [trigger\_error()](function.trigger-error.md).

```
<?php

try {
    $phar = new Phar('meuphar.phar');

    $phar['a'] = 'olá';
    $phar->copy('a', 'b');

    echo $phar['b']; // Exibe "phar://meuphar.phar/b"
} catch (Exception $e) {
    // Lida com o erro
}

// O empacotador de fluxo equivalente ao código acima.
// E_WARNING são acionados em caso de erro em vez de uma exceção
copy('phar://meuphar.phar/a', 'phar//meuphar.phar/c');
echo file_get_contents('phar://meuphar.phar/c'); // Exibe "olá"

?>
```

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
