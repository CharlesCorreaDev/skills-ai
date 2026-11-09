# Constrói um arquivo phar a partir de um iterador

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.buildfromiterator.php

---

# Phar::buildFromIterator

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::buildFromIterator — Constrói um arquivo phar a partir de um iterador

### Descrição

public function **Phar::buildFromIterator**([Traversable](class.traversable.md) `$iterator`, [?](language.types.null.md)[string](language.types.string.md) `$baseDirectory` = **`null`**): [array](language.types.array.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Preenche um arquivo phar a partir de um iterador. Dois estilos de iteradores são suportados:
iteradores que mapeiam o nome do arquivo dentro do phar para o nome de um arquivo em disco,
e iteradores como DirectoryIterator, que retornam
objetos SplFileInfo. Para iteradores que retornam objetos SplFileInfo, o segundo
parâmetro é obrigatório.

### Parâmetros

`iterator`
:   Qualquer iterador que mapeia associativamente o arquivo phar para um local ou
    que retorna objetos SplFileInfo.

`baseDirectory`
:   Para iteradores que retornam objetos SplFileInfo, a parte do caminho completo de cada
    arquivo a ser removida ao adicionar ao arquivo phar.

### Valor Retornado

**Phar::buildFromIterator()** retorna um array associativo
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
| 8.1.0 | **Phar::buildFromIterator()** não retorna mais **`false`**. |
| 8.0.0 | `baseDirectory` agora é anulável. |

### Examples

**Exemplo #1 Um exemplo de **Phar::buildFromIterator()** com SplFileInfo**

Para a maioria dos arquivos phar, o arquivo refletirá uma organização de diretório real, e
o segundo estilo é o mais útil. Por exemplo, para criar um arquivo phar
contendo os arquivos nesta organização de diretório de exemplo:

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

Este código poderia ser usado para adicionar esses arquivos ao arquivo phar "project.phar":

```
<?php
// cria com apelido "project.phar"
$phar = new Phar('project.phar', 0, 'project.phar');
$phar->buildFromIterator(
    new RecursiveIteratorIterator(
     new RecursiveDirectoryIterator('/caminho/para/projeto')),
    '/caminho/para/projeto');
$phar->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));
?>
```

O arquivo project.phar pode então ser usado imediatamente. **Phar::buildFromIterator()** não
define valores como compressão, metadados, e isso pode ser feito após a criação do
arquivo phar.

Como observação interessante, **Phar::buildFromIterator()** também pode ser usado para
copiar o conteúdo de um arquivo phar existente, já que o objeto Phar descende
de [DirectoryIterator](class.directoryiterator.md):

```
<?php
// cria com apelido "project.phar"
$phar = new Phar('project.phar', 0, 'project.phar');
$phar->buildFromIterator(
    new RecursiveIteratorIterator(
     new Phar('/caminho/para/outro_phar.phar')),
    'phar:///caminho/para/outro_phar.phar/caminho/para/projeto');
$phar->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));
?>
```

**Exemplo #2 Um exemplo de **Phar::buildFromIterator()** com outros iteradores**

A segunda forma do iterador pode ser usada com qualquer iterador que retorne
um mapeamento chave => valor, como um [ArrayIterator](class.arrayiterator.md):

```
<?php
// cria com apelido "project.phar"
$phar = new Phar('project.phar', 0, 'project.phar');
$phar->buildFromIterator(
    new ArrayIterator(
     array(
        'internos/arquivo.php' => dirname(__FILE__) . '/algum_arquivo.php',
        'outros/arquivo.jpg' => fopen('/caminho/para/arquivo_grande.jpg', 'rb'),
     )));
$phar->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));
?>
```

### Veja também

- [Phar::buildFromDirectory()](phar.buildfromdirectory.md) - Constrói um arquivo phar a partir dos arquivos dentro de um diretório

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
