# Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel-runtime.run.php

---

# parallel\Runtime::run

(0.8.0)

parallel\Runtime::run — Execução

### Descrição

public function **parallel\Runtime::run**([Closure](class.closure.md) `$task`): [?](language.types.null.md)Future

Agenda a tarefa `task` para execução em paralelo.

public function **parallel\Runtime::run**([Closure](class.closure.md) `$task`, [array](language.types.array.md) `$argv`): [?](language.types.null.md)Future

Agenda a tarefa `task` para execução em paralelo, passando `argv` no momento da execução.

### Parâmetros

`task`
:   Uma [Closure](class.closure.md) com características específicas.

`argv`
:   Um [array](language.types.array.md) de argumentos com características específicas a ser passado para `task` no momento da execução.

### Características da tarefa

As Closures programadas para execução paralela não devem:

- aceitar ou retornar por referência
- aceitar ou retornar objetos internos (ver notas)
- executar um conjunto limitado de instruções

As instruções proibidas em Closures destinadas à execução paralela são:

- yield
- uso de referência
- declaração de classe
- declaração de função nomeada

> **Nota**:
>
> Fechamentos aninhados podem usar yield ou referências, mas não devem conter declarações de classe ou funções nomeadas.

> **Nota**:
>
> Nenhuma instrução é proibida nos arquivos que a tarefa pode incluir.

### Características dos Argumentos

Os argumentos não devem conter:

- referências
- recursos
- objetos internos (veja notas)

> **Nota**:
>
> No caso de recursos de fluxo de arquivo, o recurso será convertido para o descritor de arquivo e passado como [int](language.types.integer.md) sempre que possível. Isso não é suportado no Windows.

### Notas sobre Objetos Internos

Objetos internos geralmente usam uma estrutura personalizada que não pode ser copiada por valor com segurança. Atualmente, o PHP não possui o mecanismo necessário para fazer isso (sem serialização).
Portanto, apenas objetos que não usam uma estrutura personalizada podem ser compartilhados.

Alguns objetos internos não usam uma estrutura personalizada, por exemplo [parallel\Events\Event](class.parallel-events-event.md) e, portanto, podem ser compartilhados.

Closures são um tipo especial de objeto interno e suporte que estão sendo copiados por valor e, portanto, podem ser compartilhadas.

Os canais são essenciais para escrever código paralelo e oferecem suporte ao acesso e execução simultâneos por necessidade e, portanto, podem ser compartilhados.

**Aviso**

Uma classe de usuário que estende uma classe interna pode usar uma estrutura personalizada, conforme definida pela classe interna, e nesse caso não pode ser copiada por valor com segurança,
e, portanto, não pode ser compartilhada.

### Valor Retornado

**Aviso**

O [parallel\Future](class.parallel-future.md) retornado não deve ser ignorado quando a tarefa contém uma instrução return ou throw.

### Exceções

**Aviso**

Lança uma exceção parallel\Runtime\Error\Closed se [parallel\Runtime](class.parallel-runtime.md) tiver sido fechada.

**Aviso**

Lança uma exceção parallel\Runtime\Error\IllegalFunction se `task` é uma closure criada a partir de uma função interna.

**Aviso**

Lança uma exceção parallel\Runtime\Error\IllegalInstruction se `task` contiver instruções ilegais.

**Aviso**

Lança uma exceção parallel\Runtime\Error\IllegalParameter se `task` aceitar ou `argv` contiver variáveis ilegais.

**Aviso**

Lança uma exceção parallel\Runtime\Error\IllegalReturn se `task` retornar ilegalmente.

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
