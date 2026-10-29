# Converte um arquivo phar em um arquivo tar ou zip não executável

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.converttodata.php

---

# PharData::convertToData

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::convertToData — Converte um arquivo phar em um arquivo tar ou zip não executável

### Descrição

public function **PharData::convertToData**([?](language.types.null.md)[int](language.types.integer.md) `$format` = **`null`**, [?](language.types.null.md)[int](language.types.integer.md) `$compression` = **`null`**, [?](language.types.null.md)[string](language.types.string.md) `$extension` = **`null`**): [?](language.types.null.md)[PharData](class.phardata.md)

Este método é usado para converter um arquivo tar ou zip não executável para outro
formato não executável.

Se nenhuma alteração for especificada, este método lança uma [BadMethodCallException](class.badmethodcallexception.md).
Este método deve ser usado para converter um arquivo tar para o formato zip ou vice-versa. Embora
seja possível simplesmente alterar a compactação de um arquivo tar usando este método,
é melhor usar o método [PharData::compress()](phardata.compress.md) para consistência
lógica.

Se bem-sucedido, o método cria um novo arquivo no disco e retorna um objeto [PharData](class.phardata.md).
O arquivo antigo não é removido do disco e deve ser removido manualmente após
a conclusão do processo.

### Parâmetros

`format`
:   Deve ser um dos seguintes: `Phar::TAR`
    ou `Phar::ZIP`. Se definido como **`null`**, o formato de arquivo existente
    será preservado.

`compression`
:   Deve ser um dos seguintes: `Phar::NONE` para nenhuma compactação de arquivo inteiro,
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

Este método lança uma [BadMethodCallException](class.badmethodcallexception.md) quando não é possível
compactar, ou se um método de compactação desconhecido foi especificado, ou se o arquivo
solicitado está armazenando em buffer com [Phar::startBuffering()](phar.startbuffering.md) e
não foi concluído com [Phar::stopBuffering()](phar.stopbuffering.md), e uma
[PharException](class.pharexception.md) se algum problema for encontrado
durante o processo de criação do phar.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `format`, `compression` e `extension` agora são anuláveis. |

### Examples

**Exemplo #1 Um exemplo de **PharData::convertToData()****

Usando PharData::convertToData():

```
<?php
try {
    $tarphar = new PharData('meuphar.tar');
    // Observe que meuphar.tar *não* é excluído.
    // Converte para o formato tar não executável.
    // Cria meuphar.zip
    $zip = $tarphar->convertToData(Phar::ZIP);
    // Cria meuphar.tbz
    $tgz = $zip->convertToData(Phar::TAR, Phar::BZ2, '.tbz');
    // Cria meuphar.phar.tgz
    $phar = $tarphar->convertToData(Phar::PHAR); // lança exceção
} catch (Exception $e) {
    // lida com erros
}
?>
```

### Veja também

- [Phar::convertToExecutable()](phar.converttoexecutable.md) - Converte um arquivo phar em outro formato de arquivo executável phar
- [Phar::convertToData()](phar.converttodata.md) - Converte um arquivo phar em um arquivo tar ou zip não executável
- [PharData::convertToExecutable()](phardata.converttoexecutable.md) - Converte um arquivo tar/zip não executável em um arquivo phar executável

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
