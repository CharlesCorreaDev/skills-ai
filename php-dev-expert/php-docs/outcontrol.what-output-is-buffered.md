# Que Saída é Armazenada em Buffer?

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.what-output-is-buffered.php

---

## Que Saída é Armazenada em Buffer?

Os buffers de saída em nível de usuário do PHP armazenam toda a saída após serem iniciados,
até que sejam desligados ou o script termine.
A saída no contexto do buffer de saída no nível do usuário do PHP
é tudo o que o PHP exibiria ou enviaria de volta ao navegador.
Em termos práticos, a saída são dados de comprimento diferente de zero que são:

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
> Os dados gravados diretamente em `stdout`
> ou passados ​​para uma função SAPI com funcionalidade semelhante
> não serão capturados pelos buffers de saída no nível do usuário.
> Isso inclui
> escrever dados em `stdout` com [fwrite()](function.fwrite.md)
> ou enviar cabeçalhos usando [header()](function.header.md)
> ou [setcookie()](function.setcookie.md).

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
