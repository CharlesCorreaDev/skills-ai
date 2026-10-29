# Constrói um arquivo phar a partir dos arquivos dentro de um diretório

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.buildfromdirectory.php

---

# Phar::buildFromDirectory

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::buildFromDirectory — Constrói um arquivo phar a partir dos arquivos dentro de um diretório

### Descrição

public function **Phar::buildFromDirectory**([string](language.types.string.md) `$directory`, [string](language.types.string.md) `$pattern` = ""): [array](language.types.array.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Preenche um arquivo phar a partir do conteúdo do diretório. O segundo parâmetro
opcional é uma expressão regular (pcre) usada para excluir arquivos.
Qualquer nome de arquivo que corresponda à expressão regular será incluído, todos os outros serão
excluídos. Para um controle mais refinado, use [Phar::buildFromIterator()](phar.buildfromiterator.md).

### Parâmetros

`directory`
:   O caminho completo ou relativo para o diretório que contém todos os arquivos
    a serem adicionados ao arquivo.

`pattern`
:   Uma expressão regular pcre opcional usada para filtrar a
    lista de arquivos. Somente caminhos de arquivo que correspondam à expressão regular
    serão incluídos no arquivo.

### Valor Retornado

**Phar::buildFromDirectory()** retorna um array associativo
mapeando o caminho interno do arquivo para o caminho completo do arquivo no
sistema de arquivos.

### Erros/Exceções

Este método lança [BadMethodCallException](class.badmethodcallexception.md) quando não é possível
instanciar os iteradores de diretório interno,
ou uma [PharException](class.pharexception.md) se houver erros
ao salvar o arquivo phar.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.1.0 | **Phar::buildFromDirectory()** não retorna mais **`false`**. |

### Examples

**Exemplo #1 Um exemplo de **Phar::buildFromDirectory()****

```
<?php
// cria com o apelido "project.phar"
$phar = new Phar('project.phar', 0, 'project.phar');
// adiciona todos os arquivos no projeto
$phar->buildFromDirectory(dirname(__FILE__) . '/project');
$phar->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));

$phar2 = new Phar('project2.phar', 0, 'project2.phar');
// adiciona todos os arquivos do projeto, inclui apenas arquivos php
$phar2->buildFromDirectory(dirname(__FILE__) . '/project', '/\.php$/');
$phar2->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));
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
