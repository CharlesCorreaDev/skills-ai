# Uso de re-escrita na saída

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.examples.rewrite.php

---

## Uso de re-escrita na saída

Desde o PHP 7.1.0, [output\_add\_rewrite\_var()](function.output-add-rewrite-var.md) e [output\_reset\_rewrite\_vars()](function.output-reset-rewrite-vars.md) usam buffer dedicado de saída, isto é, não usam o buffer de saída [trans sid](session.configuration.md#ini.session.use-trans-sid).

**Exemplo #1 Exemplo de re-escrita na saída**

```
<?php
// Este código funciona com PHP 7.1.0, 7.0.10, 5.6.25 e posteriores.

// HTTP_HOST é o servidor alvo padrão. Defina manualmente para fazer com o que o código de exemplo funcione.
$_SERVER['HTTP_HOST'] = 'php.net';

// Re-escrita na saída re-escreve apenas formulários. Adicione a=href.
// Etiquetas podem ser especificadas nome_da_etiqueta=atribulo_url, ex.: img=src,iframe=src
// Não é permitido espaço em branco entre as definições.
// Etiqueta 'form' é uma etiqueta especial que adiciona entrada oculta.
ini_set('url_rewriter.tags','a=href,form=');
var_dump(ini_get('url_rewriter.tags'));

// Isto é adicionado à URL e ao formulário
output_add_rewrite_var('test', 'value');
?>
<a href="//php.net/index.php?bug=1234">bug1234</a>
<form action="https://php.net/?bug=1234&edit=1" method="post">
 <input type="text" name="title" />
</form>
```

O exemplo acima produzirá:

```
<a href="//php.net/?bug=1234&test=value">bug1234</a>
<form action="https://php.net/?bug=1234&edit=1" method="post"><input type="hidden" name="test" value="value" />
 <input type="text" name="title" />
</form>
```

Desde o PHP 7.1.0, funções de re-escrita na saída têm suas próprias configurações INI, [url\_rewriter.tags](outcontrol.configuration.md#ini.url-rewriter.tags) e [url\_rewriter.hosts](outcontrol.configuration.md#ini.url-rewriter.hosts).

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
