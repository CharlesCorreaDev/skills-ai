# Configurações de Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.configuration.php

---

## Configurações de Execução

O comportamento destas funções é afetado pelas configurações do php.ini.

**Opções de configuração de Controle de Saída**

| Nome | Padrão | Modificável | Registro de Alterações |
| --- | --- | --- | --- |
| [output\_buffering](outcontrol.configuration.md#ini.output-buffering) | `"0"` | **`INI_PERDIR`** |  |
| [output\_handler](outcontrol.configuration.md#ini.output-handler) | **`null`** | **`INI_PERDIR`** |  |
| [implicit\_flush](outcontrol.configuration.md#ini.implicit-flush) | `"0"` | **`INI_ALL`** |  |
| [url\_rewriter.tags](outcontrol.configuration.md#ini.url-rewriter.tags) | `"form="` | **`INI_ALL`** | A partir do PHP 7.1.0, esta configuração INI afeta somente [output\_add\_rewrite\_var()](function.output-add-rewrite-var.md). Antes do PHP 7.1.0, esta configuração INI habilitava duporte a ID de sessão transparente (veja [session.trans\_sid\_tags](session.configuration.md#ini.session.trans-sid-tags)). |
| [url\_rewriter.hosts](outcontrol.configuration.md#ini.url-rewriter.hosts) | `$_SERVER['HTTP_HOST']` é usado como padrão. | **`INI_ALL`** | Disponível a partir do PHP 7.1.0 |

Para mais detalhes e definições dos modos
INI\_\*, consulte os [Onde uma configuração deve ser definida](configuration.changes.modes.md).

Aqui está uma breve explicação das
diretivas de configuração.

`output_buffering` [bool](language.types.boolean.md)/[int](language.types.integer.md)
:   Buffer de saída para todos os arquivos pode ser habilitado configurando-se esta diretiva
    para `"On"`.
    Para limitar o tamanho do buffer, um número/quantidade correspondendo ao
    número máximo de bytes permitidos pode ser usado no lugar de
    `"On"` para o valor desta diretiva.
    Por exemplo, `output_buffering=4096`.
    Esta diretiva é sempre "Off" no PHP-CLI.

`output_handler` [string](language.types.string.md)
:   A saída de scripts pode ser redirecionada para uma função.
    Por exemplo, ao configurar `output_handler`
    para [mb\_output\_handler()](function.mb-output-handler.md), a codificação de caracteres será
    convertida de forma trasnparente para a codificação especificada.
    Configurar qualquer manipulador de saída automaticamente habilita o buffer de saída.

    > **Nota**:
    >
    > [mb\_output\_handler()](function.mb-output-handler.md) e
    > [ob\_iconv\_handler()](function.ob-iconv-handler.md) não podem ser usadas juntas;
    > e [ob\_gzhandler()](function.ob-gzhandler.md) e
    > [zlib.output\_compression](zlib.configuration.md#ini.zlib.output-compression)
    > não podem ser usadas com nenhuma das funções a seguir:
    > [mb\_output\_handler()](function.mb-output-handler.md),
    > [ob\_gzhandler()](function.ob-gzhandler.md),
    > [zlib.output\_compression](zlib.configuration.md#ini.zlib.output-compression),
    > o manipulador 'URL-Rewriter'
    > (veja [session.use\_trans\_sid](session.configuration.md#ini.session.use-trans-sid)
    > e [output\_add\_rewrite\_var()](function.output-add-rewrite-var.md)).

    > **Nota**:
    >
    > Apenas funções internas do PHP podem ser usadas com esta diretiva.
    > Para funções definidas pelo usuário, use [ob\_start()](function.ob-start.md).

`implicit_flush` [bool](language.types.boolean.md)
:   **`false`** por padrão. Alterar para **`true`** indica ao PHP que a
    camada de saída deve se descarregar automaticamente após cada bloco de saída.
    Isto é equivalente a chamar a função do PHP
    [flush()](function.flush.md) após cada chamada a
    qualquer função que produza saída (tal como
    [print](function.print.md) ou [echo](function.echo.md))
    e cada bloco HTML.

    Ao usar o PHP em um ambiente web, habilitar
    esta opção tem implicações sérias em desempenho e é geralmente
    recomendada apenas para depuração. O valor deste parâmetro é
    **`true`** ao operar sob o `CLI SAPI`.

    Consulte também [ob\_implicit\_flush()](function.ob-implicit-flush.md).

`url_rewriter.tags` [string](language.types.string.md)
:   `url_rewriter.tags` especifica etiquetas e atributos HTML
    cujas URLs são re-escritas pelos valores de [output\_add\_rewrite\_var()](function.output-add-rewrite-var.md).
    O padrão é `"form="`.

    Adicionar `"form="` ou qualquer atributo `form`
    irá adicionar um elemento `input` oculto ao `form`
    com um atributo de nome e valor para cada par de nome-valor passado para
    [output\_add\_rewrite\_var()](function.output-add-rewrite-var.md).

    **Cuidado**

    Caso seja adicionada a mesma etiqueta mais de uma vez a `url_rewriter.tags`,
    apenas a primeira será usada durante o processo de re-escrita da URL.

    > **Nota**:
    >
    > Antes do PHP 7.1.0, [url\_rewriter.tags](outcontrol.configuration.md#ini.url-rewriter.tags)
    > era usado para especificar [session.trans\_sid\_tags](session.configuration.md#ini.session.trans-sid-tags).

`url_rewriter.hosts` [string](language.types.string.md)
:   `url_rewriter.hosts` especifica quais hosts são
    re-escritos para incluir os valores [output\_add\_rewrite\_var()](function.output-add-rewrite-var.md).
    O padrão é `$_SERVER['HTTP_HOST']`.
    Múltiplos hosts podem ser especificados por uma lista separada por vírgulas
    que não contenha espaços.
    Por exemplo, `"php.net,wiki.php.net,bugs.php.net"`.

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
