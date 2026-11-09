# Uso básico

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pcntl.example.php

---

## Uso básico

Este exemplo bifurca um processo daemon com um manipulador de sinal.

**Exemplo #1 Exemplo de controle de processo**

```
<?php
pcntl_async_signals(true);

$pid = pcntl_fork();
if ($pid == -1) {
     die("não pode bifurcar");
} else if ($pid) {
     exit(); // nós somos os pais
} else {
     // nós somos o filho
}

// desconecta do terminal de controle
if (posix_setsid() == -1) {
    die("não foi possível desconectar do terminal");
}

// configura manipuladores de sinal
pcntl_signal(SIGTERM, "sig_handler");
pcntl_signal(SIGHUP, "sig_handler");

// faz um loop para sempre executando tarefas
while (1) {

    // faça algo interessante aqui

}

function sig_handler($signo)
{

     switch ($signo) {
         case SIGTERM:
             // lida com tarefas de desligamento
             exit;
             break;
         case SIGHUP:
             // lida com tarefas de reinicialização
             break;
         default:
             // trata todos os outros sinais
     }

}

?>
```

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
