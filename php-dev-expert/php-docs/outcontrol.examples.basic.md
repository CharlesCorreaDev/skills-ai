# Uso básico

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.examples.basic.php

---

## Uso básico

**Exemplo #1 Exemplo de Controle de Saída**

```
<?php

ob_start();
echo "Hello\n";

setcookie("cookiename", "cookiedata");

ob_end_flush();

?>
```

No exemplo acima, a saída de [echo](function.echo.md)
seria armazenada no buffer de saída até que
[ob\_end\_flush()](function.ob-end-flush.md) fosse chamada. Neste meio tempo,
a chamada a [setcookie()](function.setcookie.md) armazenou com sucesso um
cookie sem causar um erro. (Normalmente não se pode enviar cabeçalhos
ao navegador depois que dados já foram enviados.)

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
