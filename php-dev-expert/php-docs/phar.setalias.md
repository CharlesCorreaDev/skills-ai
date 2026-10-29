# Define o apelido para o arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.setalias.php

---

# Phar::setAlias

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.2.1)

Phar::setAlias — Define o apelido para o arquivo Phar

### Descrição

public function **Phar::setAlias**([string](language.types.string.md) `$alias`): [true](language.types.singleton.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Define o apelido para o arquivo Phar e o grava como o apelido permanente
para este arquivo Phar. Um apelido pode ser usado internamente em um arquivo Phar para
garantir que o uso do empacotador de fluxo `phar` para acessar arquivos internos
sempre funcione, independentemente da localização do arquivo Phar no
sistema de arquivos. Outra alternativa é confiar na interceptação de Phar de
[include](function.include.md) ou usar [Phar::interceptFileFuncs()](phar.interceptfilefuncs.md)
e usar caminhos relativos.

### Parâmetros

`alias`
:   Uma string abreviada à qual este arquivo pode ser referenciado
    no acesso ao empacotador de fluxo `phar`.

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança [UnexpectedValueException](class.unexpectedvalueexception.md) quando o acesso de gravação
está desabilitado e [PharException](class.pharexception.md) se o apelido
já estiver em uso ou se algum problema for encontrado ao liberar as alterações no disco.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.4.0 | **Phar::setAlias()** agora tem um retorno provisório de [true](language.types.singleton.md). |

### Examples

**Exemplo #1 Um exemplo de **Phar::setAlias()****

```
<?php
try {
    $phar = new Phar('meuphar.phar');
    $phar->setAlias('mp.phar');
} catch (Exception $e) {
    // lida com erros
}
?>
```

### Veja também

- [Phar::\_\_construct()](phar.construct.md) - Constrói um objeto de arquivo Phar
- [Phar::interceptFileFuncs()](phar.interceptfilefuncs.md) - Instrui phar a interceptar fopen, file\_get\_contents, opendir e todas as funções relacionadas a stat

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
