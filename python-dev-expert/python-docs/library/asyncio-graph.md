Call graph introspection
************************

**Código-fonte:** Lib/asyncio/grafo.py

======================================================================

O asyncio disponibiliza utilitários poderosos de introspeção do grafo
de chamadas em tempo de execução, que permitem traçar o grafo de
chamadas completo de uma *corrotina* ou *tarefa* em execução, ou de um
*futuro* suspenso. Estes utilitários e a respectiva maquinaria
subjacente podem ser utilizados em um programa Python ou por perfis
externos e depuradores.

Ver também:

  Command-line introspection tools
     Command-line tools for inspecting tasks in another running Python
     process.

Adicionado na versão 3.14.

asyncio.print_call_graph(future=None, /, *, file=None, depth=1, limit=None)

   Exibe o grafo de chamadas assíncronas para a tarefa atual ou para a
   "Task" ou "Future" fornecida.

   Esta função exibe as entradas a partir do quadro superior até ao
   ponto de invocação.

   A função recebe um argumento opcional *future*. Se não for
   fornecido, será utilizada a tarefa em execução atual.

   Se a função for chamada na *tarefa atual*, o argumento opcional
   somente-nomeado *depth* pode ser usado para ignorar o número
   especificado de quadros a partir do topo da pilha.

   Se o argumento opcional somente-nomeado *limit* for fornecido, cada
   pilha de chamadas no gráfico resultante será truncada para incluir
   no máximo "abs(limit)" entradas. Se *limit* for positivo, as
   entradas exibidas serão as mais próximas do ponto de invocação. Se
   *limit* for negativo, as entradas mais altas são exibidas. Se
   *limit* for omitido ou "None", todas as entradas são apresentadas.
   Se *limit* for "0", a pilha de chamadas não é exibida, apenas as
   informações "aguardadas por" são exibidas.

   Se *file* for omitido ou for "None", a saída da função será
   encaminhada para "sys.stdout".

   **Exemplo:**

   O seguinte código Python:

      import asyncioasync def test():    asyncio.print_call_graph()async def main():    async with asyncio.TaskGroup() as g:        g.create_task(test(), name='test')asyncio.run(main())

   irá exibir:

      * Task(name='test', id=0x1039f0fe0)+ Call stack:|   File 't2.py', line 4, in async test()+ Awaited by:   * Task(name='Task-1', id=0x103a5e060)      + Call stack:      |   File 'taskgroups.py', line 107, in async TaskGroup.__aexit__()      |   File 't2.py', line 7, in async main()

asyncio.format_call_graph(future=None, /, *, depth=1, limit=None)

   Semelhante a "print_call_graph()", mas retorna uma string. Se
   *future* for "None" e não houver nenhuma tarefa atual, a função
   retorna uma string vazia.

asyncio.capture_call_graph(future=None, /, *, depth=1, limit=None)

   Captura o grafo de chamadas assíncronas para a tarefa atual ou para
   a "Task" ou "Future" fornecida.

   A função recebe um argumento opcional *future*. Se não for
   fornecido, será utilizada a tarefa em execução atual. Se não
   existir nenhuma tarefa atual, a função retorna "None".

   Se a função for chamada na *tarefa atual*, o argumento opcional
   somente-nomeado *depth* pode ser usado para ignorar o número
   especificado de quadros a partir do topo da pilha.

   Retorna um objeto da classe de dados "FutureCallGraph":

   * "FutureCallGraph(future, call_stack, awaited_by)"

        Onde *future* é uma referência a um "Future" ou a uma "Task"
        (ou às suas subclasses).

        "call_stack" é uma tupla de objetos "FrameCallGraphEntry".

        "awaited_by" é uma tupla de objetos "FutureCallGraph".

   * "FrameCallGraphEntry(frame)"

        Onde *frame* é um objeto de quadro de uma função Python
        regular na pilha de chamadas.


Funções utilitárias de baixo nível
==================================

Para efetuar a introspeção de um grafo de chamadas assíncronas, o
asyncio requer a cooperação de estruturas de controle de fluxo, como
"shield()" ou "TaskGroup". Sempre que um objeto "Future" intermediário
com APIs de baixo nível, como "Future.add_done_callback()", estiver
envolvido, as duas funções seguintes devem ser utilizadas para
informar o asyncio sobre a forma como esses objetos *future*
intermédios estão ligados às tarefas que envolvem ou controlam.

asyncio.future_add_to_awaited_by(future, waiter, /)

   Registra que *future* está a ser aguardado por *waiter*.

   Tanto *future* quanto *waiter* devem ser instâncias de "Future" ou
   "Task" ou de suas subclasses; caso contrário, a chamada não terá
   efeito.

   Uma chamada a "future_add_to_awaited_by()" deve ser seguida por uma
   chamada eventual à função "future_discard_from_awaited_by()" com os
   mesmos argumentos.

asyncio.future_discard_from_awaited_by(future, waiter, /)

   Registra que *future* não está mais sendo aguardado por *waiter*.

   Tanto *future* quanto *waiter* devem ser instâncias de "Future" ou
   "Task" ou de suas subclasses; caso contrário, a chamada não terá
   efeito.
