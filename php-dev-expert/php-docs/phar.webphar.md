# Encaminha uma solicitação de um navegador da web para um arquivo interno dentro do arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.webphar.php

---

# Phar::webPhar

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

Phar::webPhar — Encaminha uma solicitação de um navegador da web para um arquivo interno dentro do arquivo phar

### Descrição

final public static function **Phar::webPhar**(  
    [?](language.types.null.md)[string](language.types.string.md) `$alias` = **`null`**,  
    [?](language.types.null.md)[string](language.types.string.md) `$index` = **`null`**,  
    [?](language.types.null.md)[string](language.types.string.md) `$fileNotFoundScript` = **`null`**,  
    [array](language.types.array.md) `$mimeTypes` = [],  
    [?](language.types.null.md)[callable](language.types.callable.md) `$rewrite` = **`null`**  
): [void](language.types.void.md)

**Phar::webPhar()** serve como [Phar::mapPhar()](phar.mapphar.md) para
phars baseados na web. Este método analisa [$\_SERVER['REQUEST\_URI']](reserved.variables.server.md) e
encaminha uma solicitação de um navegador web para um arquivo interno dentro do arquivo phar.
Ele simula um servidor web, encaminhando solicitações para o arquivo correto, ecoando os cabeçalhos
corretos e analisando arquivos PHP conforme necessário. Combinado com [Phar::mungServer()](phar.mungserver.md)
e [Phar::interceptFileFuncs()](phar.interceptfilefuncs.md), qualquer aplicação web pode ser usada
sem modificações a partir de um arquivo phar.

**Phar::webPhar()** só deve ser
chamado a partir do stub de um arquivo phar (veja [aqui](phar.fileformat.stub.md)
para mais informações sobre o que é um stub).

### Parâmetros

`alias`
:   O apelido que pode ser usado em URLs `phar://` para
    se referir a este arquivo, em vez do seu caminho completo.

`index`
:   A localização dentro do phar do índice do diretório.

`fileNotFoundScript`
:   O local do script a ser executado quando um arquivo não for encontrado. Este
    script deve gerar os cabeçalhos HTTP 404 corretos.

`mimeTypes`
:   Um array mapeando extensões de arquivo adicionais para o tipo MIME.
    Se o mapeamento padrão for suficiente, passe um array vazio.
    Por padrão, essas extensões são mapeadas para os seguintes tipos MIME:

    ```
    <?php
    $mimes = array(
        'phps' => Phar::PHPS, // passado para highlight_file()
        'c' => 'text/plain',
        'cc' => 'text/plain',
        'cpp' => 'text/plain',
        'c++' => 'text/plain',
        'dtd' => 'text/plain',
        'h' => 'text/plain',
        'log' => 'text/plain',
        'rng' => 'text/plain',
        'txt' => 'text/plain',
        'xsd' => 'text/plain',
        'php' => Phar::PHP, // interpretado como PHP
        'inc' => Phar::PHP, // interpretado como PHP
        'avi' => 'video/avi',
        'bmp' => 'image/bmp',
        'css' => 'text/css',
        'gif' => 'image/gif',
        'htm' => 'text/html',
        'html' => 'text/html',
        'htmls' => 'text/html',
        'ico' => 'image/x-ico',
        'jpe' => 'image/jpeg',
        'jpg' => 'image/jpeg',
        'jpeg' => 'image/jpeg',
        'js' => 'application/x-javascript',
        'midi' => 'audio/midi',
        'mid' => 'audio/midi',
        'mod' => 'audio/mod',
        'mov' => 'movie/quicktime',
        'mp3' => 'audio/mp3',
        'mpg' => 'video/mpeg',
        'mpeg' => 'video/mpeg',
        'pdf' => 'application/pdf',
        'png' => 'image/png',
        'swf' => 'application/shockwave-flash',
        'tif' => 'image/tiff',
        'tiff' => 'image/tiff',
        'wav' => 'audio/wav',
        'xbm' => 'image/xbm',
        'xml' => 'text/xml',
    );
    ?>
    ```

`rewrite`
:   Uma função que recebe uma string como seu único parâmetro e deve retornar uma [string](language.types.string.md) ou **`false`**.

    Se fast-cgi ou cgi estiverem sendo usados, o parâmetro passado para a função será o valor da
    variável [$\_SERVER['PATH\_INFO']](reserved.variables.server.md). Caso contrário, o parâmetro passado para a função será o valor
    da variável [$\_SERVER['REQUEST\_URI']](reserved.variables.server.md).

    Se uma string for retornada, ela será usada como caminho interno do arquivo. Se **`false`** for retornado, webPhar() enviará
    um código HTTP 403 Forbidden (Proibido).

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

Lança [PharException](class.pharexception.md) quando não for possível abrir o arquivo
interno para saída, ou se
for chamado de um arquivo não stub. Se um valor de array inválido for passado para
`mimeTypes` ou uma função de retorno inválida for passado para `rewrite`, uma
[UnexpectedValueException](class.unexpectedvalueexception.md) será lançada.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `fileNotFoundScript` e `rewrite` agora são anuláveis. |

### Examples

**Exemplo #1 Um exemplo de **Phar::webPhar()****

Com o exemplo abaixo, o phar criado exibirá `Hello World`
se alguém navegar para `/myphar.phar/index.php` ou para
`/myphar.phar`, e exibirá a fonte de
`index.phps` se alguém navegar para `/myphar.phar/index.phps`.

```
<?php
// criando o arquivo phar:
try {
    $phar = new Phar('myphar.phar');
    $phar['index.php'] = '<?php echo "Olá Mundo"; ?>';
    $phar['index.phps'] = '<?php echo "Olá Mundo"; ?>';
    $phar->setStub('<?php
Phar::webPhar();
__HALT_COMPILER(); ?>');
} catch (Exception $e) {
    // lida com erros
}
?>
```

### Veja também

- [Phar::mungServer()](phar.mungserver.md) - Define uma lista de até 4 variáveis ​​$\_SERVER que devem ser modificadas para execução
- [Phar::interceptFileFuncs()](phar.interceptfilefuncs.md) - Instrui phar a interceptar fopen, file\_get\_contents, opendir e todas as funções relacionadas a stat

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
