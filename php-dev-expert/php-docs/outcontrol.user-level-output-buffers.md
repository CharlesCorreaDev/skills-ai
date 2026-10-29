# Buffers de Saída em Nível de Usuário

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.user-level-output-buffers.php

---

# Buffers de Saída em Nível de Usuário

## Índice

- [Que Saída é Armazenada em Buffer?](outcontrol.what-output-is-buffered.md)
- [Aninhando Buffers de Saída](outcontrol.nesting-output-buffers.md)
- [Tamanho do Buffer](outcontrol.buffer-size.md)
- [Operações permitidas em buffers](outcontrol.operations-on-buffers.md)
- [Manipuladores de Saída](outcontrol.output-handlers.md)
- [Trabalhando com Manipuladores de Saída](outcontrol.working-with-output-handlers.md)
- [Opções Passadas aos Manipuladores de Saída](outcontrol.flags-passed-to-output-handlers.md)
- [Valores de Retorno do Menipulador de Saída](outcontrol.output-handler-return-values.md)

Os buffers de saída no nível do usuário podem ser iniciados, manipulados
e finalizados a partir do código PHP.
Cada um desses buffers inclui um buffer de saída
e uma função de manipulador de saída associada.

## Ativando o buffer de saída

O buffer de saída pode ser ativado usando
a função [ob\_start()](function.ob-start.md) ou definindo
as configurações [output\_buffering](outcontrol.configuration.md#ini.output-buffering)
e [output\_handler](outcontrol.configuration.md#ini.output-handler)
do php.ini.
Embora ambas possam criar buffers de saída,
[ob\_start()](function.ob-start.md) é mais flexível,
pois aceita funções definidas pelo usuário como manipuladores de saída
e as operações permitidas no buffer (liberar, limpar, remover)
também podem ser definidas.
Buffers iniciados com [ob\_start()](function.ob-start.md) estarão ativos
a partir da linha em que a função foi chamada,
enquanto aqueles iniciados com
[output\_buffering](outcontrol.configuration.md#ini.output-buffering)
irão armazenar a saída em buffer a partir da primeira linha do script.

O PHP também é fornecido com um manipulador de saída `"URL-Rewriter"`
integrado que inicia seu próprio buffer de saída e permite
até no máximo duas instâncias dele em execução a qualquer momento
(uma para reescrita de URL no nível de usuário
e uma para suporte transparente ao ID de sessão).
Esses buffers podem ser iniciados chamando
a função [output\_add\_rewrite\_var()](function.output-add-rewrite-var.md)
e/ou ativando a configuração
[session.use\_trans\_sid](session.configuration.md#ini.session.use-trans-sid)
do php.ini.

A extensão `zlib` incluída tem seu próprio
buffer de saída que pode ser ativado usando a configuração
[zlib.output\_compression](zlib.configuration.md#ini.zlib.output-compression)
do php.ini.

> **Nota**:
>
> Embora `"URL-Rewriter"` seja especial
> porque permite apenas até duas instâncias dele em execução ao mesmo tempo,
> todos os buffers de saída em nível de usuário usam os mesmos buffers subjacentes
> usados ​​por [ob\_start()](function.ob-start.md)
> com sua funcionalidade implementada por uma função de manipulador de saída personalizada.
> Como tal, todas as suas funcionalidades podem ser emuladas pelo código do usuário.

## Descarregando, Acessando e Limpando o Conteúdo do Buffer

A descarga envia e descarta o conteúdo do buffer ativo.
Os buffers de saída são descarregados quando o tamanho da saída
excede o tamanho do buffer; quando o script termina; ou quando
[ob\_flush()](function.ob-flush.md), [ob\_end\_flush()](function.ob-end-flush.md)
ou [ob\_get\_flush()](function.ob-get-flush.md) são chamados.

**Cuidado**

Chamar [ob\_end\_flush()](function.ob-end-flush.md)
ou [ob\_get\_flush()](function.ob-get-flush.md) irá desligar o buffer ativo.

**Cuidado**

A descarga de buffers liberará o valor de retorno do manipulador de saída,
que pode ser diferente do conteúdo do buffer.
Por exemplo, usar [ob\_gzhandler()](function.ob-gzhandler.md) compactará
a saída e liberará a saída compactada.

O conteúdo do buffer ativo pode ser recuperado chamando
[ob\_get\_contents()](function.ob-get-contents.md), [ob\_get\_clean()](function.ob-get-clean.md)
ou [ob\_get\_flush()](function.ob-get-flush.md).

Se apenas o comprimento do conteúdo do buffer for necessário,
[ob\_get\_length()](function.ob-get-length.md) ou [ob\_get\_status()](function.ob-get-status.md)
retornação o comprimento do conteúdo em bytes.

**Cuidado**

Chamar [ob\_get\_clean()](function.ob-get-clean.md)
ou [ob\_get\_flush()](function.ob-get-flush.md) irá desligar o buffer ativo
depois de retornar seu conteúdo.

O conteúdo do buffer ativo pode ser limpo chamando
[ob\_clean()](function.ob-clean.md), [ob\_end\_clean()](function.ob-end-clean.md)
ou [ob\_get\_clean()](function.ob-get-clean.md).

**Cuidado**

Chamar [ob\_end\_clean()](function.ob-end-clean.md)
ou [ob\_get\_clean()](function.ob-get-clean.md) desligará o buffer ativo.

## Desligando Buffers

Buffers de saída podem ser desligados chamando
[ob\_end\_clean()](function.ob-end-clean.md), [ob\_end\_flush()](function.ob-end-flush.md),
[ob\_get\_flush()](function.ob-get-flush.md) ou [ob\_get\_clean()](function.ob-get-clean.md).

**Aviso**

Buffers de saída iniciados sem a opção
**`PHP_OUTPUT_HANDLER_REMOVABLE`**
não podem ser desligados e podem gerar um **`E_NOTICE`**.

Todo buffer de saída que não tiver sido fechado até o final do script,
ou quando a função [exit()](function.exit.md) for chamada, será descarregado
e desligado pelo processo de desligamento do PHP.
Os buffers serão descarregados e desligados na ordem inversa
de sua inicialização.
O último buffer iniciado será o primeiro,
o primeiro buffer iniciado será o último a ser descarregado e desligado.

**Cuidado**

Se a descarga do conteúdo do buffer não for desejada,
um manipulador de saída personalizado deverá ser usado para evitar a descarga durante o desligamento.

## Exceções Lançadas em Manipuladores de Saída

Se uma exceção não capturada é lançada em um manipulador de saída,
o programa termina e o manipulador é invocado
pelo processo de desligamento depois do qual
a mensagem de erro `"Uncaught Exception"` (exceção não capturada) é descarregada.

Se a exceção não capturada é lançada em um manipulador
invocado por [ob\_flush()](function.ob-flush.md),
[ob\_end\_flush()](function.ob-end-flush.md) ou [ob\_get\_flush()](function.ob-get-flush.md),
o conteúdo do buffer é descarregado antes da mensagem de erro.

Se uma exceção não capturada é lançada em um manipulador de saída durante o desligamento,
o manipulador é terminado e nem o conteúdo do buffer
nem a mensagem de erro são descarregados.

> **Nota**:
>
> Se um manipulador lança uma exceção,
> sua constante de estado **`PHP_OUTPUT_HANDLER_DISABLED`** é definida.

## Erros Emitidos em Manipuladores de Saída

Se um erro não fatal for gerado em um manipulador de saída,
o programa continuará a execução.

Se o erro não fatal for gerado em um manipulador invocado por
[ob\_flush()](function.ob-flush.md), [ob\_end\_flush()](function.ob-end-flush.md)
ou [ob\_get\_flush()](function.ob-get-flush.md),
o buffer descarrega determinados dados dependendo do valor de retorno do manipulador.
Se o manipulador retornar **`false`**, o buffer e a mensagem de erro são descarregados.
Se retornar qualquer outra coisa, o valor de retorno do manipulador será descarregado,
mas a mensagem de erro não.

> **Nota**:
>
> Se um manipulador retornar **`false`**,
> sua constante de estado **`PHP_OUTPUT_HANDLER_DISABLED`** será definida.

Se um erro fatal for gerado em um manipulador de saída,
o programa será encerrado e o manipulador será invocado
pelo processo de desligamento, após o qual a mensagem de erro será descarregada.

Se o erro fatal for gerado em um manipulador
invocado por [ob\_flush()](function.ob-flush.md),
[ob\_end\_flush()](function.ob-end-flush.md) ou [ob\_get\_flush()](function.ob-get-flush.md),
o conteúdo dos buffers será descarregado antes da mensagem de erro.

Se um erro fatal for gerado em um manipulador de saída durante o desligamento,
o programa será encerrado sem descarregar o buffer ou a mensagem de erro.

## Saída nos Manipuladores de Saída

Em circunstâncias específicas, a saída produzida no manipulador é descarregada
junto com o conteúdo do buffer.
Esta saída não é anexada ao buffer e não faz parte da string
retornada por [ob\_get\_flush()](function.ob-get-flush.md).

Durante operações de descarga (ao chamar [ob\_flush()](function.ob-flush.md),
[ob\_end\_flush()](function.ob-end-flush.md), [ob\_get\_flush()](function.ob-get-flush.md)
e durante o desligamento),
se o valor de retorno de um manipulador for **`false`**,
o conteúdo do buffer é descarregado seguido pela saída.
Se o manipulador não for invocado durante o desligamento,
o fato do manipulador lançar uma exceção ou chamar a função [exit()](function.exit.md)
resultará no mesmo comportamento.

> **Nota**:
>
> Se um manipulador retornar **`false`**,
> sua constante de estado **`PHP_OUTPUT_HANDLER_DISABLED`** é definida.

## Constantes de Estado do Manipulador de Saída

As
[constantes de estado de manipulador](outcontrol.constants.md#outcontrol.constants.flags-returned-by-handler) da máscara de bits `flags` do buffer
são definidas toda vez que o manipulador de saída é invocado
e são parte das `flags` retornadas por
[ob\_get\_status()](function.ob-get-status.md).
Se o manipulador executa com sucesso e não retorna **`false`**,
**`PHP_OUTPUT_HANDLER_STARTED`** e
**`PHP_OUTPUT_HANDLER_PROCESSED`** são definidas.
Se o manipulador retonar **`false`** ou lança uma exceção durante a execução,
**`PHP_OUTPUT_HANDLER_STARTED`** e
**`PHP_OUTPUT_HANDLER_DISABLED`** são definidas.

> **Nota**:
>
> Se a constante **`PHP_OUTPUT_HANDLER_DISABLED`** de um manipulador for definida,
> o manipulador não será invocado chamando-se
> [ob\_end\_clean()](function.ob-end-clean.md), [ob\_end\_flush()](function.ob-end-flush.md),
> [ob\_get\_clean()](function.ob-get-clean.md), [ob\_get\_flush()](function.ob-get-flush.md),
> [ob\_clean()](function.ob-clean.md),
> [ob\_flush()](function.ob-flush.md)
> ou durante o processo de desligamento do PHP.
> Antes do PHP 8.4.0, esta constante não tinha efeito ao chamar [ob\_clean()](function.ob-clean.md)
> ou [ob\_flush()](function.ob-flush.md).

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
