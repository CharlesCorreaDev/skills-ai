# Converte um arquivo phar em outro formato de arquivo executável phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.converttoexecutable.php

---

# Phar::convertToExecutable

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::convertToExecutable — Converte um arquivo phar em outro formato de arquivo executável phar

### Descrição

public function **Phar::convertToExecutable**([?](language.types.null.md)[int](language.types.integer.md) `$format` = **`null`**, [?](language.types.null.md)[int](language.types.integer.md) `$compression` = **`null`**, [?](language.types.null.md)[string](language.types.string.md) `$extension` = **`null`**): [?](language.types.null.md)[Phar](class.phar.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Este método é usado para converter um arquivo PHAR para outro formato de arquivo. Por exemplo,
ele pode ser usado para criar um arquivo PHAR executável baseado em tar a partir de um arquivo PHAR executável
em zip ou de um arquivo PHAR executável no formato PHAR. Além disso,
ele pode ser usado para aplicar compactação de todo o arquivo a um arquivo
baseado em tar ou PHAR.

Se nenhuma alteração for especificada, este método lançará uma [BadMethodCallException](class.badmethodcallexception.md).

Se bem-sucedido, o método cria um novo arquivo no disco e retorna um objeto [Phar](class.phar.md).
O arquivo antigo não é removido do disco e deve ser removido manualmente após
a conclusão do processo.

### Parâmetros

`format`
:   Deve ser um dos seguintes: `Phar::PHAR`, `Phar::TAR`,
    ou `Phar::ZIP`. Se definido como **`null`**, o formato de arquivo existente
    será preservado.

`compression`
:   Deve ser um dos seguintes: `Phar::NONE` para nenhuma compactação de arquivo inteiro,
    `Phar::GZ` para compactação baseada em zlib e
    `Phar::BZ2` para compactação baseada em bzip.

`extension`
:   Este parâmetro é usado para substituir a extensão de arquivo padrão para um
    arquivo convertido. Observe que todos os arquivos phar baseados em zip e tar devem conter
    `.phar` em sua extensão para serem processados ​​como um
    arquivo phar.

    Ao converter para um arquivo baseado em PHAR, as extensões padrão são
    `.phar`, `.phar.gz` ou `.phar.bz2`
    dependendo da compactação especificada. Para arquivos PHAR baseados em tar, as
    extensões padrão são `.phar.tar`, `.phar.tar.gz`
    e `.phar.tar.bz2`. Para arquivos PHAR baseados em ZIP, a
    extensão padrão é `.phar.zip`.

### Valor Retornado

O método retorna um objeto [Phar](class.phar.md) em caso de sucesso,
ou **`null`** em caso de falha.

### Erros/Exceções

Este método lança uma [BadMethodCallException](class.badmethodcallexception.md) quando não é possível
compactar, um método de compactação desconhecido foi especificado, o arquivo solicitado
está armazenando em buffer com [Phar::startBuffering()](phar.startbuffering.md) e
não foi concluído com [Phar::stopBuffering()](phar.stopbuffering.md); uma
[UnexpectedValueException](class.unexpectedvalueexception.md) se o suporte à gravação estiver desabilitado;
e uma [PharException](class.pharexception.md) se algum problema for encontrado
durante o processo de criação do phar.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `format`, `compression` e `extension` agora são anuláveis. |

### Examples

**Exemplo #1 Um exemplo de **Phar::convertToExecutable()****

Using Phar::convertToExecutable():

```
<?php
try {
    $tarphar = new Phar('meuphar.phar.tar');
    // converte para o formato de arquivo phar
    // observe que meuphar.phar.tar *não* é excluído
    $phar = $tarphar->convertToExecutable(Phar::PHAR); // cria meuphar.phar
    $phar->setStub($phar->createDefaultStub('cli.php', 'web/index.php'));
    // cria meuphar.phar.tgz
    $compressed = $phar->convertToExecutable(Phar::TAR, Phar::GZ, '.phar.tgz');
} catch (Exception $e) {
    // lida com o erro aqui
}
?>
```

### Veja também

- [Phar::convertToData()](phar.converttodata.md) - Converte um arquivo phar em um arquivo tar ou zip não executável
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
