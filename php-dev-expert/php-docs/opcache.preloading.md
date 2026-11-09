# Preloading

> **Fonte / Source:** https://www.php.net/manual/pt_BR/opcache.preloading.php

---

# Preloading

A partir do PHP 7.4.0, o PHP pode ser configurado para pré-carregar scripts no opcache quando o mecanismo
é iniciado. Quaisquer funções, classes, interfaces ou traits (mas não constantes) nestes arquivos ficarão
globalmente disponíveis para todas as solicitações sem precisar ser incluídas explicitamente. Isso troca conveniência
e desempenho (porque o código está sempre disponível) para uso de memória de linha de base. Também requer
a reinicialização do processo PHP para limpar os scripts pré-carregados, o que significa que esse recurso
é prático apenas para uso em produção, não em um ambiente de desenvolvimento.

Observe que a compensação ideal entre desempenho e memória pode variar de acordo com o aplicativo.
"Pré-carregar tudo" pode ser a estratégia mais fácil, mas não necessariamente a melhor estratégia. Além disso,
o pré-carregamento só é útil quando há um processo persistente de uma solicitação para outra. Isso significa que,
embora possa funcionar em um script CLI se o opcache estiver ativado, geralmente é inútil. A exceção
é ao usar o pré-carregamento em [bibliotecas FFI](ffi.examples-complete.md).

> **Nota**:
>
> O pré-carregamento não é suportado no Windows.

A configuração do pré-carregamento envolve duas etapas e requer que o opcache esteja ativado.
Primeiro, defina o valor [opcache.preload](opcache.configuration.md#ini.opcache.preload)
em php.ini:

```
opcache.preload=preload.php
```

preload.php é um arquivo arbitrário que será executado uma vez na inicialização do servidor
(PHP-FPM, mod\_php, etc.) e carregará o código na memória persistente. Em servidores que iniciam como
root antes de alternar para um usuário de sistema sem privilégios, ou se o PHP for executado como root
(não recomendado), o valor [opcache.preload\_user](opcache.configuration.md#ini.opcache.preload-user)
pode especificar o usuário do sistema para executar o pré-carregamento. A execução do pré-carregamento como root
não é permitida por padrão. Configure `opcache.preload_user=root` para permiti-lo explicitamente.

No script preload.php, qualquer arquivo referenciado por [include](function.include.md),
[include\_once](function.include-once.md), [require](function.require.md), [require\_once](function.require-once.md) ou
[opcache\_compile\_file()](function.opcache-compile-file.md) será analisado na memória persistente. No exemplo a seguir,
todos os arquivos .php no diretório src serão pré-carregados, a menos que
sejam um arquivo `Test`.

```
<?php
$directory = new RecursiveDirectoryIterator(__DIR__ . '/src');
$fullTree = new RecursiveIteratorIterator($directory);
$phpFiles = new RegexIterator($fullTree, '/.+((?<!Test)+\.php$)/i', RecursiveRegexIterator::GET_MATCH);

foreach ($phpFiles as $key => $file) {
    require_once $file[0];
}
?>
```

Ambos [include](function.include.md) e [opcache\_compile\_file()](function.opcache-compile-file.md) funcionarão, mas têm implicações
diferentes sobre como o código é tratado.

- [include](function.include.md) executará o código no arquivo,
  enquanto [opcache\_compile\_file()](function.opcache-compile-file.md) não. Isso significa que apenas o primeiro suporta
  declaração condicional (funções declaradas dentro de um bloco if).
- Como [include](function.include.md) executará o código, os arquivos [include](function.include.md)s
  aninhados também serão analisados e suas declarações pré-carregadas.
- [opcache\_compile\_file()](function.opcache-compile-file.md) pode carregar arquivos em qualquer ordem. Ou seja, se
  a.php define a classe `A` e b.php define a classe
  `B` que estende `A`, então [opcache\_compile\_file()](function.opcache-compile-file.md) pode
  carregar esses dois arquivos em qualquer ordem. Ao usar [include](function.include.md), no entanto, a.php
  *deve* ser incluído primeiro.
- Em ambos os casos, se um script posterior incluir um arquivo que já foi pré-carregado,
  seu conteúdo ainda será executado, mas quaisquer símbolos que ele definir não serão redefinidos. O uso de
  [include\_once](function.include-once.md) não impedirá que o arquivo seja incluído uma segunda vez. Pode
  ser necessário carregar um arquivo novamente para incluir as constantes globais definidas nele, pois elas não são
  tratadas pelo pré-carregamento.

Qual abordagem é melhor, portanto, depende do comportamento desejado. Com código que, de outra forma, usaria um
autoloader, [opcache\_compile\_file()](function.opcache-compile-file.md) permite maior flexibilidade. Com o código que seria
carregado manualmente, [include](function.include.md) será mais robusta.

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
