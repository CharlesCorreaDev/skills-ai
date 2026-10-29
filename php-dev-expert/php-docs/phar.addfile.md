# Adiciona um arquivo do sistema de arquivos ao arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.addfile.php

---

# Phar::addFile

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::addFile — Adiciona um arquivo do sistema de arquivos ao arquivo phar

### Descrição

public function **Phar::addFile**([string](language.types.string.md) `$filename`, [?](language.types.null.md)[string](language.types.string.md) `$localName` = **`null`**): [void](language.types.void.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Com este método, qualquer arquivo ou URL pode ser adicionado ao arquivo phar. Se
o segundo parâmetro opcional `localName` for uma [string](language.types.string.md),
o arquivo será armazenado no arquivo com esse nome; caso contrário, o
parâmetro `file` será usado como o caminho para armazenar
o arquivo. URLs devem ter um nome local ou uma exceção será lançada.
Este método é semelhante a [ZipArchive::addFile()](ziparchive.addfile.md).

### Parâmetros

`filename`
:   Caminho completo ou relativo para um arquivo no disco a ser adicionado
    ao arquivo phar.

`localName`
:   Caminho onde o arquivo será armazenado no arquivo compactado.

### Valor Retornado

Nenhum valor de retorno, exceção é lançada em caso de falha.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `localName` agora é anulável. |

### Examples

**Exemplo #1 Um exemplo de **Phar::addFile()****

```
<?php
try {
    $a = new Phar('/path/to/phar.phar');

    $a->addFile('/full/path/to/file');
    // demonstra como este arquivo é armazenado
    $b = $a['full/path/to/file']->getContent();

    $a->addFile('/full/path/to/file', 'my/file.txt');
    $c = $a['my/file.txt']->getContent();

    // demonstra o uso de URL
    $a->addFile('http://www.example.com', 'example.html');
} catch (Exception $e) {
    // manipula erros aqui
}
?>
```

### Notas

> **Nota**:
>
> **Phar::addFile()**, [Phar::addFromString()](phar.addfromstring.md) e [Phar::offsetSet()](phar.offsetset.md)
> salvam um novo arquivo phar cada vez que são chamadas. Se o desempenho for uma preocupação,
> [Phar::buildFromDirectory()](phar.buildfromdirectory.md) ou [Phar::buildFromIterator()](phar.buildfromiterator.md)
> devem ser usadas.

### Veja também

- [Phar::offsetSet()](phar.offsetset.md) - Define o conteúdo de um arquivo interno para o de um arquivo externo
- [PharData::addFile()](phardata.addfile.md) - Adiciona um arquivo do sistema de arquivos ao arquivo tar/zip
- [Phar::addFromString()](phar.addfromstring.md) - Adiciona um arquivo a partir de uma string ao arquivo phar
- [Phar::addEmptyDir()](phar.addemptydir.md) - Adiciona um diretório vazio ao arquivo phar

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
