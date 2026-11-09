# Compacta todo o arquivo tar/zip usando Gzip ou Bzip2

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.compress.php

---

# PharData::compress

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::compress — Compacta todo o arquivo tar/zip usando Gzip ou Bzip2

### Descrição

public function **PharData::compress**([int](language.types.integer.md) `$compression`, [?](language.types.null.md)[string](language.types.string.md) `$extension` = **`null`**): [?](language.types.null.md)[PharData](class.phardata.md)

Para arquivos tar, este método compacta o arquivo inteiro usando
gzip ou bzip2. O arquivo resultante pode ser processado com o comando
gunzip/comando bunzip ou acessado direta e transparentemente com a extensão
Phar.

Para arquivos zip, este método falha com uma exceção.
A extensão [zlib](ref.zlib.md) deve estar habilitada para compactar
com gzip, a extensão [bzip2](ref.bzip2.md) deve estar
habilitada para compactar com bzip2.

Além disso, este método renomeia automaticamente o arquivo, anexando `.gz`,
`.bz2` ou removendo a extensão se `Phar::NONE` for passado para
remover a compactação. Alternativamente, uma extensão de arquivo pode ser especificada com o segundo
parâmetro.

### Parâmetros

`compression`
:   A compactação. Deve ser `Phar::GZ`,
    `Phar::BZ2` para adicionar compactação ou `Phar::NONE`
    para remover compactação.

`extension`
:   Por padrão, a extensão é `.tar.gz` ou `.tar.bz2`
    para compactar um tar e `.tar` para descompactar.

### Valor Retornado

Um objeto [PharData](class.phardata.md) é retornado em caso de sucesso,
ou **`null`** em caso de falha.

### Erros/Exceções

Lança [BadMethodCallException](class.badmethodcallexception.md) se
a extensão [zlib](ref.zlib.md)
não estiver disponível ou se a extensão [bzip2](ref.bzip2.md)
não estiver habilitada.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `extension` agora é anulável. |

### Examples

**Exemplo #1 Um exemplo de **PharData::compress()****

```
<?php
$p = new PharData('/caminho/para/meu.tar');
$p['meuarquivo.txt'] = 'olá';
$p['meuarquivo2.txt'] = 'olá';
$p1 = $p->compress(Phar::GZ); // copia para /caminho/para/meu.tar.gz
$p2 = $p->compress(Phar::BZ2); // copia para /caminho/para/meu.tar.bz2
$p3 = $p2->compress(Phar::NONE); // exceção: /caminho/para/meu.tar já existe
?>
```

### Veja também

- [Phar::compress()](phar.compress.md) - Compacta todo o arquivo Phar usando compactação Gzip ou Bzip2

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
