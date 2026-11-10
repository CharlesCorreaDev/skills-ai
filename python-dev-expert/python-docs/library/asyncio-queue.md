Filas
*****

**Código-fonte:** Lib/asyncio/queues.py

======================================================================

Filas asyncio são projetadas para serem similar a classes do módulo
"queue". Apesar de filas asyncio não serem seguras para thread, elas
são projetadas para serem usadas especificamente em código
async/await.

Perceba que métodos de filas asyncio não possuem um parâmetro
*timeout*; use a função "asyncio.wait_for()" para realizar operações
de fila com um tempo limite timeout.

Veja também a seção Exemplos abaixo.


Queue
=====

class asyncio.Queue(maxsize=0)

   Uma fila onde o primeiro a entrar, é o primeiro a sair (FIFO -
   First In First Out).

   Se *maxsize* for menor que ou igual a zero, o tamanho da fila é
   infinito. Se ele for um inteiro maior que "0", então "await put()"
   bloqueia quando a fila atingir *maxsize* até que um item seja
   removido por "get()".

   Ao contrário da biblioteca padrão de threading "queue", o tamanho
   da fila é sempre conhecido e pode ser obtido através da chamada do
   método "qsize()".

   Alterado na versão 3.10: Removido o parâmetro *loop*.

   Esta classe não é segura para thread.

   maxsize

      Número de itens permitidos na fila.

   empty()

      Retorna "True" se a fila estiver vazia, "False" caso contrário.

   full()

      Retorna "True" se existem "maxsize" itens na fila.

      Se a fila foi inicializada com "maxsize=0" (o padrão), então
      "full()" nunca retorna "True".

   async get()

      Remove e retorna um item da fila. Se a fila estiver vazia,
      aguarda até que um item esteja disponível.

      Levanta "QueueShutDown" se a fila foi encerrada e está vazia, ou
      se a fila foi encerrada imediatamente.

   get_nowait()

      Retorna um item se houver um imediatamente disponível, caso
      contrário levanta "QueueEmpty".

      Levanta "QueueShutDown" se a fila foi encerrada e está vazia.

   async join()

      Bloqueia até que todos os itens na fila tenham sido recebidos e
      processados.

      A contagem de tarefas inacabadas aumenta sempre que um item é
      adicionado à fila. A contagem diminui sempre que uma corrotina
      consumidora chama "task_done()" para indicar que o item foi
      recuperado e todo o trabalho nele foi concluído. Quando a
      contagem de tarefas inacabadas chega a zero, "join()"
      desbloqueia.

   async put(item)

      Coloca um item na fila. Se a fila estiver cheia, aguarda até que
      uma posição livre esteja disponível antes de adicionar o item.

      Levanta "QueueShutDown" se a fila foi encerrada.

   put_nowait(item)

      Coloca um item na fila sem bloqueá-la.

      Se nenhuma posição livre estiver imediatamente disponível,
      levanta "QueueFull".

      Levanta "QueueShutDown" se a fila foi encerrada.

   qsize()

      Retorna o número de itens na fila.

   shutdown(immediate=False)

      Coloca uma instância de "Queue" em modo de desligamento.

      A fila não pode mais crescer. Chamadas futuras a "put()"
      levantam "QueueShutDown". Chamadores de "put()" atualmente
      bloqueados serão desbloqueados e levantarão "QueueShutDown" na
      tarefa que estava aguardando anteriormente.

      Se *immediate* for falso (o padrão), a fila pode ser encerrada
      normalmente com chamadas "get()" para extrair tarefas que já
      foram carregadas.

      E se "task_done()" for chamado para cada tarefa restante, um
      "join()" pendente será desbloqueado normalmente.

      Assim que a fila estiver vazia, chamadas futuras para "get()"
      vão levantar "QueueShutDown".

      Se *immediate* for verdadeiro, a fila é encerrada imediatamente.
      A fila é esvaziada completamente e a contagem de tarefas não
      concluídas é reduzida pelo número de tarefas concluídas. Se o
      número de tarefas não concluídas for zero, as chamadas de
      "join()" são desbloqueadas. Além disso, as chamadas bloqueadas
      de "get()" são desbloqueadas e levantarão uma exceção
      "QueueShutDown" porque a fila está vazia.

      Tenha cuidado ao usar "join()" com a opção *immediate* definida
      como verdadeiro. Isso desbloqueia a junção mesmo quando nenhuma
      tarefa foi executada, violando a invariante usual para a junção
      de uma fila.

      Adicionado na versão 3.13.

   task_done()

      Indica que o item de trabalho anteriormente enfileirado está
      concluído.

      Usada por consumidores de fila. Para cada "get()" usado para
      buscar um item de trabalho, uma chamada subsequente para
      "task_done()" avisa à fila, que o processamento no item de
      trabalho está concluído.

      Se um "join()" estiver sendo bloqueado no momento, ele irá
      continuar quando todos os itens tiverem sido processados
      (significando que uma chamada "task_done()" foi recebida para
      cada item que foi chamado o método "put()" para colocar na
      fila).

      Levanta "ValueError" se chamada mais vezes do que a quantidade
      de itens existentes na fila.


Fila de prioridade
==================

class asyncio.PriorityQueue

   Uma variante de "Queue"; recupera entradas em ordem de prioridade
   (mais baixas primeiro).

   Entradas são tipicamente tuplas no formato "(priority_number,
   data)".


Filas LIFO (último a entrar, primeiro a sair)
=============================================

class asyncio.LifoQueue

   Uma variante de "Queue" que recupera as entradas adicionadas mais
   recentemente primeiro (último a entrar, primeiro a sair).


Exceções
========

exception asyncio.QueueEmpty

   Esta exceção é levantada quando o método "get_nowait()" é chamado
   em uma fila vazia.

exception asyncio.QueueFull

   Exceção levantada quando o método "put_nowait()" é chamado em uma
   fila que atingiu seu *maxsize*.

exception asyncio.QueueShutDown

   Exceção levantada quando "put()", "put_nowait()", "get()" ou
   "get_nowait()" é chamado em uma fila que foi desligada.

   Adicionado na versão 3.13.


Exemplos
========

Filas podem ser usadas para distribuir cargas de trabalho entre
diversas tarefas concorrentes:

   import asyncio
   import random
   import time


   async def worker(nome, fila):
       while True:
           # Retira um "item de trabalho" da fila.
           dormir_por = await queue.get()

           # Dorme por "dormir_por" segundos.
           await asyncio.sleep(dormir_por)

           # Notifica a fila de que o "item de trabalho" foi processado.
           fila.task_done()

           print(f'{nome} dormiu por {dormir_por:.2f} segundos')


   async def main():
       # Cria uma fila para armazenar nossa "carga de trabalho".
       fila = asyncio.Queue()

       # Gera tempos aleatórios e os insere na fila.
       tempo_total_de_sono = 0
       for _ in range(20):
           dormir_por = random.uniform(0.05, 1.0)
           tempo_total_de_sono += dormir_por
           fila.put_nowait(dormir_por)

       # Cria três tarefas "worker" para processarem a fila concorrentemente.
       tarefas = []
       for i in range(3):
           tarefa = asyncio.create_task(worker(f'worker-{i}', fila))
           tarefas.append(tarefa)

       # Espera até a fila ser completamente processada.
       comecou_em = time.monotonic()
       await fila.join()
       tempo_dormido = time.monotonic() - comecou_em

       # Cancela nossas tarefas.
       for tarefa in tarefas:
           tarefa.cancel()
       # Espera até todas as tarefas serem canceladas.
       await asyncio.gather(*tarefas, return_exceptions=True)

       print('====')
       print(f'3 trabalhadoras dormiram em paralelo por {tempo_dormido:.2f} segundos')
       print(f'Tempo total de sono esperado: {tempo_total_de_sono:.2f} segundos')


   asyncio.run(main())
