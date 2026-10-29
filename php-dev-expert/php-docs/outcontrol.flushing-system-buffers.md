# Descarregando Buffers de Sistema

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.flushing-system-buffers.php

---

# Descarregando Buffers de Sistema

O PHP fornece duas maneiras relacionadas
para descarregar os buffers de sistema (enviar e descartar o conteúdo):
chamando-se a função [flush()](function.flush.md)
e habilitando o descarregamento implicitamente
com a função [ob\_implicit\_flush()](function.ob-implicit-flush.md)
ou com a configuração [implicit\_flush](outcontrol.configuration.md#ini.implicit-flush)
do php.ini.

## Comportamento do Descarregameto da Saída

Com o descarregamento implícito desabilitado, o PHP irá descarregar a saída somente
quendo [flush()](function.flush.md) for chamada ou quando o script terminar.

Com o descarregamento implícito habilitado, o PHP tentará descarregar
após cada bloco de código que resulte em uma saída.
A saída neste contexto é um dado de comprimento maior que zero que:

- esteja fora das tags `<?php ?>`
- seja exibido por construções de linguagem e funções
  cujo propósito explícito é mostrar variáveis fornecidas pelo usuário ou strings tais como
  [echo](function.echo.md), [print](function.print.md),
  [printf()](function.printf.md), [var\_dump()](function.var-dump.md),
  [var\_export()](function.var-export.md) e [vprintf()](function.vprintf.md)
- seja exibido por funções cujo propósito é coletar e mostrar
  dados/informações no script em execução ou no PHP tais como
  [debug\_print\_backtrace()](function.debug-print-backtrace.md), [phpcredits()](function.phpcredits.md) e
  [phpinfo()](function.phpinfo.md),
  [ReflectionExtension::info()](reflectionextension.info.md)
- seja mostrado pelo PHP em uma exceção não capturada ou erro não gerenciado
  (sujeitos às configurações de
  [display\_errors](errorfunc.configuration.md#ini.display-errors)
  e [error\_reporting](errorfunc.configuration.md#ini.error-reporting))
- seja qualquer coisa escrita em `php://output`

> **Nota**:
>
> Exibir strings vazias ou enviar cabeçalhos não é considerado saída
> e não resultará em operação de descarregamento.

**Aviso**

Se o descarregamento implícito estiver habilitado, caracteres de controle
(ex.: `"\n"`, `"\r"`,
`"\0"`)
também irão ativar o descarregamento.

## Limitações

Esta funcionalidade não pode descarregar buffers de saída no nível do usuário.
Para usá-los juntos, buffers de saída no nível do usuário devem ser descarregados
antes do descarregamento ds buffers de sistema para que o PHP produza qualquer saída.

**Aviso**

Chamar [flush()](function.flush.md) ou habilitar o descarregamento implícito
pode interferir com os manipuladores de saída de buffers no nível do usuário
que definem e enviam cabeçalhos em um contexto web
(ex.: [ob\_gzhandler()](function.ob-gzhandler.md))
enviando cabeçalhos antes que estes manipuladores o façam.

Buffer implementado pelo software/hardware subjacente
não podem ser substituídos pelo PHP e devem ser levados em consideração
ao se trabalhar com as funções de controle de buffer do PHP.
Verificar as configurações de buffer dos servidores web, navegadores e consoles
e trabalhar com elas pode aliviar possíveis problemas.
Trabalhar em um contexto web, tanto as configurações de buffer do servidor
quanto de buffer do script podem ser ajustadas para operar sequencialmente
enquanto que contornar as estratégias de buffer de vários navegadores
pode ser conseguido ajustando o buffer no script PHP.
Em consoles que implementam buffer de linha,
caracteres de nova linha podem ser inseridos nos locais
apropriados antes de liberar a saída.

## Diferenças SAPI No Descarregamento

Embora o descarregamento seja implementado por cada SAPI
de uma maneira ligeiramente diferente,
essas implementações se enquadram em uma de duas categorias:

- SAPIs usadas em um contexto web irão descarregar cabeçalhos primeiro,
  e depois a saída.
  `Apache2Handler`, `CGI`,
  `FastCGI` e `FPM`
  são tais SAPIs.
- Outras SAPIs
  tais como `CLI` e `embed`
  irão descarregar somente a saída.

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
