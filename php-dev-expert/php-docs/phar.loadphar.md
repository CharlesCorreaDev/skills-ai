# Carrega qualquer arquivo phar com um apelido

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.loadphar.php

---

# Phar::loadPhar

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::loadPhar — Carrega qualquer arquivo phar com um apelido

### Descrição

final public static function **Phar::loadPhar**([string](language.types.string.md) `$filename`, [?](language.types.null.md)[string](language.types.string.md) `$alias` = **`null`**): [bool](language.types.boolean.md)

Isto pode ser usado para ler o conteúdo de um arquivo Phar externo. Isto
é mais útil para atribuir um apelido a um phar para que referências subsequentes
ao phar possam usar o apelido mais curto, ou para carregar arquivos Phar que
contêm apenas dados e não se destinam à execução/inclusão em scripts PHP.

### Parâmetros

`filename`
:   O caminho completo ou relativo do arquivo phar a ser aberto.

`alias`
:   O apelido que pode ser usado para se referir ao arquivo phar. Observe
    que muitos arquivos phar especificam um apelido explícito dentro do
    arquivo phar, e uma [PharException](class.pharexception.md) será lançada se
    um novo apelido for especificado neste caso.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

[PharException](class.pharexception.md) é lançada se um apelido for passado e o arquivo phar
já tiver um apelido explícito.

### Examples

**Exemplo #1 Um exemplo de **Phar::loadPhar()****

Phar::loadPhar pode ser usado em qualquer lugar para carregar um arquivo Phar externo, enquanto
Phar::mapPhar deve ser usado em um stub de carregador para um Phar.

```
<?php
try {
    Phar::loadPhar('/caminho/para/phar.phar', 'meu.phar');
    echo file_get_contents('phar://meu.phar/arquivo.txt');
} catch (PharException $e) {
    echo $e;
}
?>
```

### Veja também

- [Phar::mapPhar()](phar.mapphar.md) - Lê o arquivo atualmente em execução (um phar) e registra seu manifesto

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
