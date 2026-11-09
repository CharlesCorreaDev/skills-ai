# Extrai o conteúdo de um arquivo tar/zip para um diretório

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.extractto.php

---

# PharData::extractTo

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::extractTo — Extrai o conteúdo de um arquivo tar/zip para um diretório

### Descrição

public function **PharData::extractTo**([string](language.types.string.md) `$directory`, [array](language.types.array.md)|[string](language.types.string.md)|[null](language.types.null.md) `$files` = **`null`**, [bool](language.types.boolean.md) `$overwrite` = **`false`**): [bool](language.types.boolean.md)

Extrai todos os arquivos de um arquivo tar/zip para o disco. Os arquivos e diretórios extraídos preservam
as permissões conforme armazenadas no arquivo. Os parâmetros opcionais permitem controle opcional sobre
quais arquivos são extraídos e se os arquivos existentes no disco podem ser sobrescritos.
O segundo parâmetro `files` pode ser o nome de um arquivo ou
diretório a ser extraído, ou um array de nomes de arquivos e diretórios a serem extraídos. Por
padrão, este método não sobrescreve arquivos existentes; o terceiro parâmetro pode ser
definido como true para habilitar a sobrescrita de arquivos.
Este método é semelhante a [ZipArchive::extractTo()](ziparchive.extractto.md).

### Parâmetros

`directory`
:   Caminho para o qual devem ser extraídos os arquivos informados em `files`.

`files`
:   O nome de um arquivo ou diretório a ser extraído, ou um array de arquivos/diretórios a serem extraídos.

`overwrite`
:   Defina como **`true`** para habilitar a substituição de arquivos existentes.

### Valor Retornado

Retorna **`true`** em caso de sucesso, mas é melhor verificar se há exceções lançadas
e assumir sucesso se nenhuma for lançada.

### Erros/Exceções

Lança [PharException](class.pharexception.md) se ocorrerem erros durante a descarga
de alterações no disco.

### Examples

**Exemplo #1 Um exemplo de **PharData::extractTo()****

```
<?php
try {
    $phar = new PharData('meuphar.tar');
    $phar->extractTo('/caminho/completo'); // extrai todos os arquivos
    $phar->extractTo('/caminho/alternativo', 'arquivo.txt'); // extrai somente arquivo.txt
    $phar->extractTo('/este/caminho',
        array('arquivo1.txt', 'arquivo2.txt')); // extrai somente 2 arquivos
    $phar->extractTo('/terceiro/caminho', null, true); // extrai todos os arquivos e sobrescreve
} catch (Exception $e) {
    // lida com erros
}
?>
```

### Notas

> **Nota**:
>
> O sistema de arquivos NTFS do Windows
> não suporta alguns caracteres em nomes de arquivos, como `<|>*?":`. Nomes de arquivos que terminam com ponto
> também não são suportados. Ao contrário de algumas ferramentas de extração, este método não substitui estes caracteres por
> um sublinhado, mas falha ao extrair esses arquivos.

### Veja também

- [Phar::extractTo()](phar.extractto.md) - Extrai o conteúdo de um arquivo phar para um diretório

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
