# Inicialização

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel.bootstrap.php

---

# parallel\bootstrap

(1.0.0)

parallel\bootstrap — Inicialização

### Descrição

function **parallel\bootstrap**([string](language.types.string.md) `$file`): [void](language.types.void.md)

Usa o arquivo informado em `file` para inicializar todas as variáveis em tempo de execução criadas para agendamento automático via [parallel\run()](parallel.run.md).

### Parâmetros

`file`
:   Caminho para o arquivo para inicializar todas as variáveis.

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

**Aviso**

Lança uma exceção parallel\Runtime\Error\Bootstrap se o método já tiver sido chamado para este processo.

**Aviso**

Lança uma exceção parallel\Runtime\Error\Bootstrap se chamado após [parallel\run()](parallel.run.md).

### Veja também

- [parallel\Runtime::run](parallel-runtime.run.md)

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
