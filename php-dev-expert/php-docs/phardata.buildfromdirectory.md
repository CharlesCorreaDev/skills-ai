# Constrói um arquivo tar/zip a partir dos arquivos dentro de um diretório

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.buildfromdirectory.php

---

# PharData::buildFromDirectory

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::buildFromDirectory — Constrói um arquivo tar/zip a partir dos arquivos dentro de um diretório

### Descrição

public function **PharData::buildFromDirectory**([string](language.types.string.md) `$directory`, [string](language.types.string.md) `$pattern` = ""): [array](language.types.array.md)

Preenche um arquivo tar/zip a partir do conteúdo do diretório. O segundo parâmetro
opcional é uma expressão regular (pcre) usada para excluir arquivos.
Qualquer nome de arquivo que corresponda à expressão regular será incluído, todos os outros serão
excluídos. Para um controle mais refinado, use [PharData::buildFromIterator()](phardata.buildfromiterator.md).

### Parâmetros

`directory`
:   O caminho completo ou relativo para o diretório que contém todos os arquivos
    a serem adicionados ao arquivo.

`pattern`
:   Uma expressão regular pcre opcional usada para filtrar a
    lista de arquivos. Somente caminhos de arquivo que correspondam à expressão regular
    serão incluídos no arquivo.

### Valor Retornado

[Phar::buildFromDirectory()](phar.buildfromdirectory.md) retorna um array associativo
mapeando o caminho interno do arquivo para o caminho completo do arquivo no
sistema de arquivos, ou **`false`** em caso de falha.

### Erros/Exceções

Este método lança [BadMethodCallException](class.badmethodcallexception.md) quando não é possível
instanciar os iteradores de diretório interno,
ou uma [PharException](class.pharexception.md) se houver erros
ao salvar o arquivo phar.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.1.0 | **PharData::buildFromDirectory()** não retorna mais **`false`**. |

### Examples

**Exemplo #1 Um exemplo de **PharData::buildFromDirectory()****

```
<?php
$phar = new PharData('project.tar');
// adiciona todos os arquivos no projeto
$phar->buildFromDirectory(dirname(__FILE__) . '/project');

$phar2 = new PharData('project2.zip');
// adiciona todos os arquivos no projeto, inclui somente arquivos php
$phar2->buildFromDirectory(dirname(__FILE__) . '/project', '/\.php$/');
?>
```

### Veja também

- [Phar::buildFromDirectory()](phar.buildfromdirectory.md) - Constrói um arquivo phar a partir dos arquivos dentro de um diretório
- [PharData::buildFromIterator()](phardata.buildfromiterator.md) - Constrói um arquivo tar ou zip a partir de um iterador

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
