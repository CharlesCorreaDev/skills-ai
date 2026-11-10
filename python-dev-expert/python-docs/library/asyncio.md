"asyncio" --- E/S assíncrona
****************************

======================================================================


Olá Mundo!
^^^^^^^^^^

   import asyncio

   async def main():
       print('Olá ...')
       await asyncio.sleep(1)
       print('... Mundo!')

   asyncio.run(main())

asyncio é uma biblioteca para escrever código **simultâneo** usando a
sintaxe **async/await**.

O asyncio é usado como uma base para várias estruturas assíncronas do
Python que fornecem rede e servidores web de alto desempenho,
bibliotecas de conexão de banco de dados, filas de tarefas
distribuídas etc.

asyncio geralmente serve perfeitamente para código de rede
**estruturado** de alto nível e vinculado a E/S.

Ver também:

  Uma visão geral conceitual de asyncio
     Explicação dos fundamentos do asyncio.

asyncio fornece um conjunto de APIs de **alto nível** para:

* executar corrotinas do Python simultaneamente e ter controle total
  sobre sua execução;

* realizar IPC e E/S de rede;

* controlar subprocessos;

* distribuir tarefas por meio de filas;

* sincronizar código simultâneo;

For **introspection**, asyncio provides APIs and tools for:

* inspecting the async call graph of tasks and futures;

* inspecting tasks in another running Python process with command-line
  tools;

Além disso, há APIs de **baixo nível** para *desenvolvedores de
biblioteca e framework* para:

* criar e gerenciar laços de eventos, que fornecem APIs assíncronas
  para rede, execução de subprocessos, tratamento de sinais de
  sistemas operacionais etc;

* implementar protocolos eficientes usando transportes;

* fazer uma ponte sobre bibliotecas baseadas em chamadas e codificar
  com a sintaxe de async/await.

Disponibilidade: not WASI.

Este módulo não funciona ou não está disponível em WebAssembly. Veja
Plataformas WebAssembly para mais informações.

-[ REPL de asyncio ]-

Você pode experimentar um contexto atual "asyncio" no *REPL*:

   $ python -m asyncio
   asyncio REPL ...
   Use "await" directly instead of "asyncio.run()".
   Type "help", "copyright", "credits" or "license" for more information.
   >>> import asyncio
   >>> await asyncio.sleep(10, result='hello')
   'hello'

Este REPL oferece compatibilidade limitada com a variável de ambiente
"PYTHON_BASIC_REPL". Recomenda-se o uso do REPL padrão para obter
todas as funcionalidades e os recursos mais recentes.

Levanta um evento de auditoria "cpython.run_stdin" sem argumentos.

Alterado na versão 3.12.5: (também 3.11.10, 3.10.15, 3.9.20 e 3.8.20)
Emite eventos de auditoria.

Alterado na versão 3.13: Usa PyrePL, se possível, nesse caso
"PYTHONSTARTUP" também é executado. Emite eventos de auditoria.

-[ Referência ]-


APIs de alto nível
^^^^^^^^^^^^^^^^^^

* Runners

* Coroutines and tasks

* Streams

* Synchronization Primitives

* Subprocessos

* Filas

* Exceções


Introspection APIs
^^^^^^^^^^^^^^^^^^

* Call graph introspection

* Command-line introspection tools


APIs de baixo nível
^^^^^^^^^^^^^^^^^^^

* Laço de eventos

* Futuros

* Transports e Protocols

* Políticas

* Suporte a plataformas

* Extensão


Guias e tutoriais
^^^^^^^^^^^^^^^^^

* Índice da API de alto nível

* Índice de APIs de baixo nível

* Desenvolvendo com asyncio

* asyncio and free-threaded Python

Nota:

  O código-fonte para o asyncio pode ser encontrado em Lib/asyncio/.
