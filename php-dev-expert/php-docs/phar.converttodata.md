# Converte um arquivo phar em um arquivo tar ou zip não executável

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.converttodata.php

---

# Phar::convertToData

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::convertToData — Converte um arquivo phar em um arquivo tar ou zip não executável

### Descrição

public function **Phar::convertToData**([?](language.types.null.md)[int](language.types.integer.md) `$format` = **`null`**, [?](language.types.null.md)[int](language.types.integer.md) `$compression` = **`null`**, [?](language.types.null.md)[string](language.types.string.md) `$extension` = **`null`**): [?](language.types.null.md)[PharData](class.phardata.md)

Este método é usado para converter um arquivo executável phar em um arquivo
tar ou zip. Para tornar o tar ou zip não executável, o stub phar
e os arquivos de alias phar são removidos do arquivo recém-criado.

Se nenhuma alteração for especificada, este método lança uma [BadMethodCallException](class.badmethodcallexception.md)
se o arquivo estiver no formato phar. Para arquivos no formato tar ou zip,
este método converte o arquivo em um arquivo não executável.

Se bem-sucedido, o método cria um novo arquivo no disco e retorna um objeto [PharData](class.phardata.md).
O arquivo antigo não é removido do disco e deve ser removido manualmente após
a conclusão do processo.

### Parâmetros

`format`
:   Deve ser um dos seguintes: `Phar::TAR`
    ou `Phar::ZIP`. Se definido como **`null`**, o formato de arquivo existente
    será preservado.

`compression`
:   Deve ser um dos seguintes: `Phar::NONE` para nenhuma compactação de arquivo,
    `Phar::GZ` para compactação baseada em zlib e
    `Phar::BZ2` para compactação baseada em bzip.

`extension`
:   Este parâmetro é usado para substituir a extensão de arquivo padrão para um
    arquivo convertido. Observe que `.phar` não pode ser usado
    em nenhum lugar no nome do arquivo para um arquivo tar ou zip não executável.

    Ao converter para um arquivo phar baseado em tar, as
    extensões padrão são `.tar`, `.tar.gz`,
    e `.tar.bz2`, dependendo da compactação especificada.
    Para arquivos baseados em zip, a
    extensão padrão é `.zip`.

### Valor Retornado

O método retorna um objeto [PharData](class.phardata.md) em caso de sucesso,
ou **`null`** em caso de falha.

### Erros/Exceções

Este método lança [BadMethodCallException](class.badmethodcallexception.md) quando não é possível
compactar, um método de compactação desconhecido foi especificado, o arquivo solicitado
está armazenando em buffer com [Phar::startBuffering()](phar.startbuffering.md) e
não foi concluído com [Phar::stopBuffering()](phar.stopbuffering.md),
e uma [PharException](class.pharexception.md) se algum problema for encontrado
durante o processo de criação do phar.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `format`, `compression` e `extension` agora são anuláveis. |

### Examples

**Exemplo #1 Um exemplo de **Phar::convertToData()****

Using Phar::convertToData():

```
<?php
try {
    $tarphar = new Phar('meuphar.phar.tar');
    // observe que meuphar.phar.tar *não* é excluído
    // converte para o formato de arquivo tar não executável
    // cria meuphar.tar
    $tar = $tarphar->convertToData();
    // converte para formato zip não executável, cria meuphar.zip
    $zip = $tarphar->convertToData(Phar::ZIP);
    // cria meuphar.tbz
    $tgz = $tarphar->convertToData(Phar::TAR, Phar::BZ2, '.tbz');
    // cria meuphar.phar.tgz
    $phar = $tarphar->convertToData(Phar::PHAR); // lança exceção
} catch (Exception $e) {
    // manipula os erros aqui
}
?>
```

### Veja também

- [Phar::convertToExecutable()](phar.converttoexecutable.md) - Converte um arquivo phar em outro formato de arquivo executável phar
- [PharData::convertToExecutable()](phardata.converttoexecutable.md) - Converte um arquivo tar/zip não executável em um arquivo phar executável
- [PharData::convertToData()](phardata.converttodata.md) - Converte um arquivo phar em um arquivo tar ou zip não executável

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
