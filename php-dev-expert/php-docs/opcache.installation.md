# Instalação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/opcache.installation.php

---

## Instalação

OPcache só pode ser compilado como uma extensão compartilhada. Se você desativou
a construção de extensões padrão com
**--disable-all**, você deve compilar o PHP com a
opção **--enable-opcache** para que o OPcache
esteja disponível.

Uma vez compilado, você pode usar a diretiva de configuração
[zend\_extension](ini.core.md#ini.zend-extension) para carregar
a extensão OPcache no PHP. Isso pode ser feito com
`zend_extension=/full/path/to/opcache.so` em plataformas não Windows
e `zend_extension=C:\path\to\php_opcache.dll`
no Windows.

> **Nota**:
>
> Se você quiser usar o OPcache com
> [» Xdebug](https://xdebug.org/), você deve carregar o OPcache antes
> do Xdebug.

### Configurações recomendadas do php.ini

As seguintes configurações são geralmente recomendadas para fornecer um bom
desempenho:

```
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=60
opcache.fast_shutdown=1 ; prior to PHP 7.2.0
opcache.enable_cli=1
```

Você também pode querer considerar desabilitar
[opcache.save\_comments](opcache.configuration.md#ini.opcache.save-comments)
e habilitar
[opcache.enable\_file\_override](opcache.configuration.md#ini.opcache.enable-file-override),
no entanto, observe que você terá que testar seu código antes de usá-los na
produção, pois eles são conhecidos por quebrar algumas estruturas e aplicativos,
particularmente nos casos em que são usadas anotações de comentários na documentação.

No Windows, [opcache.file\_cache\_fallback](opcache.configuration.md#ini.opcache.file-cache-fallback)
deve ser habilitado e [opcache.file\_cache](opcache.configuration.md#ini.opcache.file-cache)
deve ser definido como um diretório já existente e gravável.

Uma lista completa de diretivas de configuração suportadas pelo OPcache
[também está disponível](opcache.configuration.md).

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
