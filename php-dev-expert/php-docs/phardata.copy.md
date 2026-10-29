# Copia um arquivo interno do arquivo tar/zip para outro arquivo novo dentro do mesmo arquivo

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.copy.php

---

# PharData::copy

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::copy — Copia um arquivo interno do arquivo tar/zip para outro arquivo novo dentro do mesmo arquivo

### Descrição

public function **PharData::copy**([string](language.types.string.md) `$from`, [string](language.types.string.md) `$to`): [true](language.types.singleton.md)

Copia um arquivo interno do arquivo tar/zip para outro arquivo novo dentro do mesmo arquivo.
Esta é uma alternativa orientada a objetos ao uso de [copy()](function.copy.md) com
o empacotador de fluxo phar.

### Parâmetros

`from`

`to`

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança [UnexpectedValueException](class.unexpectedvalueexception.md) se o arquivo de origem não
existir, se o arquivo de destino já existir, se o acesso de gravação estiver desabilitado, se a abertura
do arquivo falhar, se a leitura do arquivo de origem falhar ou uma [PharException](class.pharexception.md)
se a gravação das alterações no arquivo phar falhar.

### Examples

**Exemplo #1 Um exemplo de **PharData::copy()****

Este exemplo mostra o uso de **PharData::copy()** e o
desempenho equivalente do empacotador de fluxo para a mesma coisa. A principal
diferença entre as duas abordagens é o tratamento de erros. Todos os métodos PharData
geram exceções, enquanto o empacotador de fluxo usa [trigger\_error()](function.trigger-error.md).

```
<?php

try {
    $phar = new PharData('meuphar.tar');

    $phar['a'] = 'olá';
    $phar->copy('a', 'b');

    echo $phar['b']; // Exibe "phar://meuphar.tar/b"
} catch (Exception $e) {
    // Lida com erros
}

// O equivalente em empacotador de fluxo para o código acima.
// E_WARNING é gerado em caso de erros em vez de exceções
copy('phar://meuphar.tar/a', 'phar//meuphar.tar/c');
echo file_get_contents('phar://meuphar.tar/c'); // Exibe "olá"

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
