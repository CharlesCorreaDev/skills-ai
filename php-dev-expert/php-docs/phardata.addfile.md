# Adiciona um arquivo do sistema de arquivos ao arquivo tar/zip

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.addfile.php

---

# PharData::addFile

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::addFile — Adiciona um arquivo do sistema de arquivos ao arquivo tar/zip

### Descrição

public function **PharData::addFile**([string](language.types.string.md) `$filename`, [?](language.types.null.md)[string](language.types.string.md) `$localName` = **`null`**): [void](language.types.void.md)

Com este método, qualquer arquivo ou URL pode ser adicionado ao arquivo tar/zip. Se
o segundo parâmetro opcional `localname` for especificado,
o arquivo será armazenado no arquivo com esse nome; caso contrário, o
parâmetro `file` será usado como caminho para armazenamento
no arquivo. URLs devem ter um localname, ou uma exceção será lançada.
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

**Exemplo #1 Um exemplo de **PharData::addFile()****

```
<?php
try {
    $a = new PharData('/caminho/para/meu.tar');

    $a->addFile('/caminho/completo/para/arquivo');
    // demonstra como este arquivo é armazenado
    $b = $a['/caminho/completo/para/arquivo']->getContent();

    $a->addFile('/caminho/completo/para/arquivo', 'meu/arquivo.txt');
    $c = $a['meu/arquivo.txt']->getContent();

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
> **PharData::addFile()**, [PharData::addFromString()](phardata.addfromstring.md) e [PharData::offsetSet()](phardata.offsetset.md)
> salvam um novo arquivo phar cada vez que são chamadas. Se o desempenho for uma preocupação,
> [PharData::buildFromDirectory()](phardata.buildfromdirectory.md) ou [PharData::buildFromIterator()](phardata.buildfromiterator.md)
> devem ser usadas.

### Veja também

- [PharData::offsetSet()](phardata.offsetset.md) - Define o conteúdo de um arquivo dentro do tar/zip para o de um arquivo externo ou string
- [Phar::addFile()](phar.addfile.md) - Adiciona um arquivo do sistema de arquivos ao arquivo phar
- [PharData::addFromString()](phardata.addfromstring.md) - Adiciona um arquivo de uma string ao arquivo tar/zip
- [PharData::addEmptyDir()](phardata.addemptydir.md) - Adiciona um diretório vazio ao arquivo tar/zip

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
