# Constrói um arquivo tar ou zip a partir de um iterador

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.buildfromiterator.php

---

# PharData::buildFromIterator

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::buildFromIterator — Constrói um arquivo tar ou zip a partir de um iterador

### Descrição

public function **PharData::buildFromIterator**([Traversable](class.traversable.md) `$iterator`, [?](language.types.null.md)[string](language.types.string.md) `$baseDirectory` = **`null`**): [array](language.types.array.md)

Preenche um arquivo tar ou zip a partir de um iterador. Dois estilos de iteradores são suportados:
iteradores que mapeiam o nome do arquivo dentro do tar/zip para o nome de um arquivo em disco,
e iteradores como DirectoryIterator, que retornam
objetos SplFileInfo. Para iteradores que retornam objetos SplFileInfo, o segundo
parâmetro é obrigatório.

### Parâmetros

`iterator`
:   Qualquer iterador que mapeia associativamente um arquivo tar/zip para um local ou
    retorna objetos SplFileInfo.

`baseDirectory`
:   Para iteradores que retornam objetos SplFileInfo, a parte do caminho completo de cada
    arquivo a ser removida ao adicionar ao arquivo tar/zip.

### Valor Retornado

**PharData::buildFromIterator()** retorna um array associativo
mapeando o caminho interno do arquivo para o caminho completo do arquivo no
sistema de arquivos.

### Erros/Exceções

Este método retorna [UnexpectedValueException](class.unexpectedvalueexception.md) quando o
iterador retorna valores incorretos, como uma chave inteira em vez de uma
string, uma [BadMethodCallException](class.badmethodcallexception.md) quando um
iterador baseado em SplFileInfo é passado sem um parâmetro `baseDirectory`
ou uma [PharException](class.pharexception.md) se houver erros
ao salvar o arquivo phar.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.1.0 | **PharData::buildFromIterator()** não retorna mais **`false`**. |
| 8.0.0 | `baseDirectory` agora é anulável. |

### Examples

**Exemplo #1 Um exemplo de **PharData::buildFromIterator()** com SplFileInfo**

Para a maioria dos arquivos tar/zip, o arquivo refletirá um layout de diretório real, e
o segundo estilo é o mais útil. Por exemplo, para criar um arquivo tar/zip
contendo os arquivos neste layout de diretório de exemplo:

```
/caminho/para/projeto/
                 config/
                        dist.xml
                        debug.xml
                 lib/
                     file1.php
                     file2.php
                 src/
                     processthing.php
                 www/
                     index.php
                 cli/
                     index.php
```

Este código pode ser usado para adicionar esses arquivos ao arquivo tar "projeto.tar":

```
<?php
$phar = new PharData('projeto.tar');
$phar->buildFromIterator(
    new RecursiveIteratorIterator(
     new RecursiveDirectoryIterator('/caminho/para/projeto')),
    '/caminho/para/projeto');
?>
```

O arquivo `projeto.tar` pode então ser usado imediatamente. **PharData::buildFromIterator()** não
define valores como compactação e metadados, e isso pode ser feito após a criação do
arquivo tar/zip.

Como observação interessante, **PharData::buildFromIterator()** também pode ser usado para
copiar o conteúdo de um arquivo phar, tar ou zip existente, já que o objeto PharData descende
de [DirectoryIterator](class.directoryiterator.md):

```
<?php
$phar = new PharData('projeto.tar');
$phar->buildFromIterator(
    new RecursiveIteratorIterator(
     new Phar('/caminho/para/outrophar.phar')),
    'phar:///caminho/parao/outrophar.phar/caminho/para/projeto');
$phar->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));
?>
```

**Exemplo #2 Um exemplo de **PharData::buildFromIterator()** com outros iteradores**

A segunda forma do iterador pode ser usada com qualquer iterador que retorne
um mapeamento chave => valor, como um [ArrayIterator](class.arrayiterator.md):

```
<?php
$phar = new PharData('projeto.tar');
$phar->buildFromIterator(
    new ArrayIterator(
     array(
        'internos/arquivo.php' => dirname(__FILE__) . '/algumarquivo.php',
        'outros/arquivo.jpg' => fopen('/caminho/para/arquivogrande.jpg', 'rb'),
     )));
?>
```

### Veja também

- [Phar::buildFromIterator()](phar.buildfromiterator.md) - Constrói um arquivo phar a partir de um iterador

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
