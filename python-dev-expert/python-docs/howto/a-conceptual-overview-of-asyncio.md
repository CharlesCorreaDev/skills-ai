Uma visão geral conceitual de "asyncio"
***************************************

Este artigo COMOFAZER tem como objetivo ajudá-lo a construir um modelo
mental sólido de como "asyncio" funciona fundamentalmente, ajudando-
lhe a compreender o como e o porquê por trás dos padrões recomendados.

Você pode estar curioso sobre alguns conceitos-chave de "asyncio". Ao
final deste artigo, você será capaz de responder confortavelmente a
estas perguntas:

* O que acontece nos bastidores quando um objeto é aguardado?

* Como o "asyncio" diferencia uma tarefa que não precisa de tempo de
  CPU (como uma solicitação de rede ou leitura de arquivo) de uma
  tarefa que precisa (como calcular n-fatorial)?

* Como escrever uma variante assíncrona de uma operação, como uma
  suspensão assíncrona ou uma solicitação de banco de dados.

Ver também:

  * O guia que inspirou este artigo COMOFAZER, por Alexander Nordin.

  * Esta série de tutoriais detalhados do YouTube sobre "asyncio" foi
    criada pelo membro da equipe principal do Python, Łukasz Langa.

  * 500 linhas ou menos: um rastreador da Web com corrotinas asyncio
    (em inglês) por A. Jesse Jiryu Davis e Guido van Rossum.


Uma visão geral conceitual parte 1: o alto nível
================================================

Na parte 1, abordaremos os principais blocos de construção de alto
nível de "asyncio": o laço de eventos, funções de corrotina, objetos
de corrotina, tarefas e "await".


Laço de eventos
---------------

Tudo no "asyncio" acontece em relação ao laço de eventos (*event
loop*). Ele é a estrela do espetáculo, mas prefere atuar nos
bastidores, gerenciando e coordenando recursos. É como um maestro de
orquestra: alguns poderes lhe são explicitamente conferidos, mas
grande parte de sua capacidade de realizar tarefas advém do respeito e
da cooperação dos integrantes da orquestra.

Em termos mais técnicos, o laço de eventos contém uma coleção de
tarefas a serem executadas. Algumas tarefas são adicionadas
diretamente por você e outras indiretamente por "asyncio". O laço de
eventos pega uma tarefa do seu backlog de tarefas e a invoca (ou "dá a
ela o controle"), semelhante a chamar uma função, e então essa tarefa
é executada. Uma vez pausada ou concluída, ela retorna o controle para
o laço de eventos. O laço de eventos então seleciona outra tarefa do
seu pool e a invoca. Você pode *aproximadamente* pensar na coleção de
tarefas como uma fila: as tarefas são adicionadas e processadas uma de
cada vez, geralmente (mas nem sempre) em ordem. Esse processo se
repete indefinidamente, com o laço de eventos em ciclos infinitos. Se
não houver mais tarefas pendentes de execução, o laço de eventos é
inteligente o suficiente para descansar e evitar o desperdício
desnecessário de ciclos de CPU, e retornará quando houver mais
trabalho a ser feito, tal como quando operações E/S são concluídas ou
seu tempo expira.

A execução eficaz depende do bom compartilhamento e da cooperação
entre as tarefas; uma tarefa gananciosa pode monopolizar o controle e
deixar as outras tarefas na miséria, tornando a abordagem geral do
laço de eventos inútil.

   import asyncio

   # Isso cria um laço de eventos e percorre indefinidamente
   # sua coleção de trabalhos
   event_loop = asyncio.new_event_loop()
   event_loop.run_forever()


Funções assíncronas e corrotinas
--------------------------------

Esta é uma função básica e chata do Python:

   def hello_printer():
       print(
           "Olá, sou uma impressora humilde e simples, embora tenha tudo "
           "que preciso na vida: -- \npapel novo e meu querido e amado "
           "parceiro no crime, o polvo."
       )

Chamar uma função regular invoca sua lógica ou corpo:

   >>> hello_printer()
   Olá, sou uma impressora humilde e simples, embora tenha tudo o que preciso na vida:
   papel novo e meu querido e amado parceiro no crime, o polvo.

O async def, em oposição a um simples "def", torna esta uma função
assíncrona (ou "função de corrotina"). Chamá-la cria e retorna um
objeto corrotina.

   async def loudmouth_penguin(magic_number: int):
       print(
        "Eu sou um pinguim falante superespecial. Muito mais legal que aquela impressora. "
        f"Aliás, meu número da sorte é: {magic_number}."
       )

Chamar a função assíncrona, "loudmouth_penguin", não executa a
instrução de impressão; em vez disso, cria um objeto corrotina:

   >>> loudmouth_penguin(magic_number=3)
   <coroutine object loudmouth_penguin at 0x104ed2740>

Os termos "função de corrotina" e "objeto corrotina" são
frequentemente confundidos com corrotina. Isso pode ser confuso! Neste
artigo, corrotina se refere especificamente a um objeto corrotina, ou
mais precisamente, a uma instância de "types.CoroutineType" (corrotina
nativa). Observe que corrotinas também podem existir como instâncias
de "collections.abc.Coroutine" — uma distinção importante para a
verificação de tipos.

Uma corrotina representa o corpo ou a lógica da função. Uma corrotina
precisa ser iniciada explicitamente; novamente, a mera criação da
corrotina não a inicia. Notavelmente, a corrotina pode ser pausada e
retomada em vários pontos do corpo da função. Essa capacidade de
pausar e retomar é o que permite o comportamento assíncrono!

Corrotinas e funções de corrotina foram criadas aproveitando a
funcionalidade de *geradores* e *funções geradoras*. Lembre-se: uma
função geradora é uma função que executa "yield", como esta:

   def get_random_number():
       # Este seria um gerador de número aleatório ruim!
       print("Oi")
       yield 1
       print("Olá")
       yield 7
       print("E aí")
       yield 4
       ...

Semelhante a uma função de corrotina, chamar uma função geradora não a
executa. Em vez disso, ela cria um objeto gerador:

   >>> get_random_number()
   <generator object get_random_number at 0x1048671c0>

Você pode prosseguir para o próximo "yield" de um gerador usando a
função embutida "next()". Em outras palavras, o gerador é executado e,
em seguida, pausado. Por exemplo:

   >>> generator = get_random_number()
   >>> next(generator)
   Oi
   1
   >>> next(generator)
   Olá
   7


Tarefas
-------

Em termos gerais, tarefas são corrotinas (não funções de corrotina)
vinculadas a um laço de eventos. Uma tarefa também mantém uma lista de
funções de retorno de chamada cuja importância ficará clara em breve,
quando discutirmos "await".

A criação de uma tarefa a agenda automaticamente para execução
(adicionando um retorno de chamada para executá-la na lista de tarefas
do laço de eventos, ou seja, coleção de tarefas). A forma recomendada
é criar tarefas por meio de "asyncio.create_task()".

"asyncio" associa automaticamente as tarefas ao laço de eventos. Essa
associação automática foi propositalmente incorporada ao "asyncio"
para simplificar o processo. Sem ela, você teria que controlar o
objeto laço de eventos e passá-lo para qualquer função de corrotina
que queira criar tarefas, adicionando código redundante ao seu
projeto.

   coroutine = loudmouth_penguin(magic_number=5)
   # Isso cria um objeto Task e agenda sua execução por meio do laço de eventos.
   task = asyncio.create_task(coroutine)

Anteriormente, criamos manualmente o laço de eventos e o configuramos
para ser executado indefinidamente. Na prática, é recomendado (e
comum) usar "asyncio.run()", que gerencia o laço de eventos e garante
que a corrotina fornecida termine antes de avançar. Por exemplo,
muitos programas assíncronos seguem esta configuração:

   import asyncio

   async def main():
       # Faz todo tipo de coisas malucas, selvagens e assíncronas...
       ...

   if __name__ == "__main__":
       asyncio.run(main())
       # O programa não alcançará a seguinte instrução de exibição
       # até que o main() da corrotina seja finalizado.
       print("main() da corrotina concluiu!")

É importante estar ciente de que a tarefa em si não é adicionada ao
laço de eventos, apenas um retorno de chamada para a tarefa. Isso é
importante se o objeto de tarefa que você criou for coletado como lixo
antes de ser chamado pelo laço de eventos. Por exemplo, considere este
programa:

   async def hello():
       print("hello!")

   async def main():
       asyncio.create_task(hello())
       # Outras instruções assíncronas que são executadas por
       # um tempo e cedem o controle ao laço de eventos...
       ...

   asyncio.run(main())

Como não há referência ao objeto tarefa criado na linha 5, ele *pode*
ser coletado como lixo antes que o laço de eventos o invoque.
Instruções posteriores na corrotina "main()" transferem o controle de
volta para o laço de eventos para que ele possa invocar outras
tarefas. Quando o laço de eventos eventualmente tenta executar a
tarefa, pode falhar e descobrir que o objeto task não existe! Isso
também pode acontecer mesmo que uma corrotina mantenha uma referência
a uma tarefa, mas seja concluída antes que ela termine. Quando a
corrotina termina, as variáveis locais saem do escopo e podem estar
sujeitas à coleta de lixo. Na prática, "asyncio" e o coletor de lixo
do Python trabalham arduamente para garantir que esse tipo de coisa
não aconteça. Mas isso não é motivo para ser imprudente!


await
-----

"await" é uma palavra reservada do Python comumente usada de duas
maneiras diferentes:

   await task
   await coroutine

De maneira crucial, o comportamento de "await" depende do tipo de
objeto que está sendo aguardado.


Aguardando por tarefas
~~~~~~~~~~~~~~~~~~~~~~

Aguardar uma tarefa cederá o controle da tarefa ou corrotina atual
para o laço de eventos. No processo de cessão de controle, algumas
coisas importantes acontecem. Usaremos o seguinte exemplo de código
para ilustrar:

   async def plant_a_tree():
       dig_the_hole_task = asyncio.create_task(dig_the_hole())
       await dig_the_hole_task

       # Outras instruções associadas com plantar uma árvore.
       ...

Neste exemplo, imagine que o laço de eventos passou o controle para o
início da corrotina "plant_a_tree()". Como visto acima, a corrotina
cria uma tarefa e a aguarda. A instrução "await dig_the_hole_task"
adiciona um retorno de chamada (que retomará "plant_a_tree()") à lista
de retornos de chamada do objeto "dig_the_hole_task". E então, a
instrução cede o controle para o laço de eventos. Algum tempo depois,
o laço de eventos passará o controle para "dig_the_hole_task" e a
tarefa concluirá o que for necessário. Assim que a tarefa for
concluída, ela adicionará seus vários retornos de chamada ao laço de
eventos, neste caso, uma chamada para retomar "plant_a_tree()".

De modo geral, quando a tarefa aguardada termina
("dig_the_hole_task"), a tarefa original ou corrotina
("plant_a_tree()") é adicionada novamente à lista de tarefas do laço
de eventos para ser retomada.

Este é um modelo mental básico, porém confiável. Na prática, as
transferências de controle são um pouco mais complexas, mas não muito.
Na parte 2, abordaremos os detalhes que tornam isso possível.


Aguardando por corrotinas
~~~~~~~~~~~~~~~~~~~~~~~~~

**Ao contrário de tarefas, aguardar uma corrotina não devolve o
controle ao laço de eventos!** Envolver uma corrotina em uma tarefa
primeiro e depois aguardar isso cederia o controle. O comportamento de
"await coroutine" é efetivamente o mesmo que invocar uma função Python
síncrona comum. Considere este programa:

   import asyncio

   async def coro_a():
      print("Sou coro_a(). Oi!")

   async def coro_b():
      print("Sou coro_b(). Espero que ninguém monopolize o laço de eventos...")

   async def main():
      task_b = asyncio.create_task(coro_b())
      num_repeats = 3
      for _ in range(num_repeats):
         await coro_a()
      await task_b

   asyncio.run(main())

A primeira instrução na corrotina "main()" cria "task_b" e a agenda
para execução via laço de eventos. Em seguida, "coro_a()" é aguardado
repetidamente. O controle nunca cede ao laço de eventos, e é por isso
que vemos a saída de todas as três invocações de "coro_a()" antes da
saída de "coro_b()":

   Sou coro_a(). Oi!
   Sou coro_a(). Oi!
   Sou coro_a(). Oi!
   Sou coro_b(). Espero que ninguém monopolize o laço de eventos...

Se alterarmos "await coro_a()" para "await
asyncio.create_task(coro_a())", o comportamento muda. A corrotina
"main()" cede o controle ao laço de eventos com essa instrução. O laço
de eventos então prossegue com seu backlog de trabalho, chamando
"task_b" e, em seguida, a tarefa que encerra "coro_a()" antes de
retomar a corrotina "main()".

   Sou coro_b(). Espero que ninguém monopolize o laço de eventos...
   Sou coro_a(). Oi!
   Sou coro_a(). Oi!
   Sou coro_a(). Oi!

Esse comportamento de "await coroutine" pode confundir muita gente!
Este exemplo destaca como usar apenas "await coroutine" pode,
involuntariamente, monopolizar o controle de outras tarefas e
efetivamente paralisar o laço de eventos. "asyncio.run()" pode ajudar
a detectar tais ocorrências por meio do sinalizador "debug=True", que
habilita o modo de depuração. Entre outras coisas, ele registrará
quaisquer corrotinas que monopolizem a execução por 100 ms ou mais.

O design intencionalmente troca alguma clareza conceitual em torno do
uso de "await" por melhor desempenho. Cada vez que uma tarefa é
aguardada, o controle precisa ser passado por toda a pilha de chamadas
até o laço de eventos. O laço de eventos precisa gerenciar seu estado
interno e resolver seu processamento lógico para continuar a próxima
tarefas. Isso pode parecer insignificante, mas em um programa grande
com muitas instruções "await"s essa sobrecarga pode representar um
significativo prejuízo ao desempenho.


Uma visão geral conceitual, parte 2: os detalhes
================================================

A parte 2 detalha os mecanismos que "asyncio" usa para gerenciar o
fluxo de controle. É aqui que a mágica acontece. Você sairá desta
seção sabendo o que "await" faz nos bastidores e como criar seus
próprios operadores assíncronos.


O funcionamento interno das corrotinas
--------------------------------------

"asyncio" utiliza quatro componentes do Python para passar o controle.

"coroutine.send(arg)" é o método usado para iniciar ou retomar uma
corrotina. Se a corrotina foi pausada e agora está sendo retomada, o
argumento "arg" será enviado como valor de retorno da instrução
"yield" que a pausou originalmente. Se a corrotina estiver sendo usada
pela primeira vez (em vez de ser retomada), "arg" deve ser "None".

   class Rock:
       def __await__(self):
           value_sent_in = yield 7
           print(f"Rock.__await__ resumindo com o valor: {value_sent_in}.")
           return value_sent_in

   async def main():
       print("Iniciando main() da corrotina.")
       rock = Rock()
       print("Aguardando rock...")
       value_from_rock = await rock
       print(f"Corrotina recebeu valor: {value_from_rock} de rock.")
       return 23

   coroutine = main()
   intermediate_result = coroutine.send(None)
   print(f"Corrotina pausou e retornou o valor intermediário: {intermediate_result}.")

   print(f"Resumindo corrotina e enviando o valor: 42.")
   try:
       coroutine.send(42)
   except StopIteration as e:
       returned_value = e.value
   print(f"O main() da corrotina finalizou e forneceu o valor: {returned_value}.")

yield, como de costume, pausa a execução e retorna o controle ao
chamador. No exemplo acima, "yield", na linha 3, é chamado por "... =
await rock" na linha 11. Em termos mais gerais, "await" chama o método
"__await__()" do objeto fornecido. "await" também faz algo muito
especial: ele propaga (ou "repassa") quaisquer "yield"s que recebe na
cadeia de chamadas. Neste caso, voltamos a "... =
coroutine.send(None)" na linha 16.

A corrotina é retomada por meio da chamada "coroutine.send(42)" na
linha 21. A corrotina continua de onde foi executada (ou pausada) com
"yield" na linha 3 e executa as instruções restantes em seu corpo.
Quando uma corrotina termina, ela levanta uma exceção "StopIteration"
com o valor de retorno anexado ao atributo "value".

Esse trecho de código produz esta saída:

   Iniciando main() da corrotina.
   Aguardando rock...
   Corrotina pausou e retornou o valor intermediário: 7.
   Resumindo coroutine e enviando o valor: 42.
   Rock.__await__ resumindo com o valor: 42.
   Corrotina recebeu valor: 42 de rock.
   O main() da corrotina finalizou e forneceu o valor: 23.

Vale a pena parar um momento aqui e certificar-se de que você seguiu
as diversas maneiras pelas quais o fluxo de controle e os valores
foram passados. Muitas ideias importantes foram abordadas e vale a
pena garantir que seu entendimento esteja firme.

A única maneira de ceder (ou efetivamente ceder o controle) de uma
corrotina é "await" um objeto que "yield" está em seu método
"__await__". Isso pode parecer estranho para você. Você pode estar
pensando:

   1. What about a "yield" directly within the coroutine function? The
   coroutine function becomes an async generator function, a different
   beast entirely.

   2. What about a yield from within the coroutine function to a
   (plain) generator? That causes the error: "SyntaxError: yield from
   not allowed in a coroutine." This was intentionally designed for
   the sake of simplicity -- mandating only one way of using
   coroutines. Despite that, "yield from" and "await" effectively do
   the same thing. Initially "yield" was barred as well, but was re-
   accepted to allow for async generators.


Futuros
-------

Um future é um objeto que representa o status e o resultado de uma
computação. O termo é uma referência à ideia de algo que ainda está
por vir ou que ainda não aconteceu, e o objeto é uma forma de ficar de
olho nesse algo.

Um future possui alguns atributos importantes. Um deles é o seu
estado, que pode ser "pending", "cancelled", or "done" ("pendente",
"cancelado" ou "concluído", respectivamente). Outro é o seu resultado,
que é definido quando o estado transita para concluído. Ao contrário
de uma corrotina, um future não representa a computação real a ser
realizada; em vez disso, representa o status e o resultado dessa
computação, como uma espécie de luz de status (vermelha, amarela ou
verde) ou indicador.

"asyncio.Task" estende "asyncio.Future" para obter esses vários
recursos. A seção anterior dizia que as tarefas armazenam uma lista de
retornos de chamada, o que não era totalmente preciso. Na verdade, é a
classe "Future" que implementa essa lógica, que "Task" herda.

Instruções future também podem ser usados diretamente (não por meio de
tarefas). As tarefas se marcam como concluídas quando sua corrotina é
concluída. Instruções future são muito mais versáteis e serão marcados
como concluídos quando você informar. Dessa forma, eles são a
interface flexível para você definir suas próprias condições de espera
e retomada.


Um asyncio.sleep caseiro
------------------------

Veremos um exemplo de como você pode aproveitar um future para criar
sua própria variante de suspensão assíncrona ("async_sleep") que imita
"asyncio.sleep()".

Este trecho de código registra algumas tarefas no laço de eventos e,
em seguida, aguarda a tarefa criada por "asyncio.create_task", que
envolve a corrotina "async_sleep(3)". Queremos que essa tarefa termine
somente após três segundos, mas sem impedir a execução de outras
tarefas.

   async def other_work():
       print("Eu gosto de trabalhar. Trabalhar, trabalhar.")

   async def main():
       # Adiciona algumas tarefas ao laço de eventos, de forma que
       # haja algo para fazer durante a suspensão assíncrona.
       work_tasks = [
           asyncio.create_task(other_work()),
           asyncio.create_task(other_work()),
           asyncio.create_task(other_work())
       ]
       print(
           "Começando a suspensão assíncrona no horário: "
           f"{datetime.datetime.now().strftime("%H:%M:%S")}."
       )
       await asyncio.create_task(async_sleep(3))
       print(
           "Concluí a suspensão assíncrona no horário: "
           f"{datetime.datetime.now().strftime("%H:%M:%S")}."
       )
       # asyncio.gather efetivamente espera cada tarefa na coleção.
       await asyncio.gather(*work_tasks)

A seguir, usamos um future para permitir o controle personalizado
sobre quando essa tarefa será marcada como concluída. Se
"future.set_result()" (o método responsável por marcar o future como
concluído) nunca for chamado, essa tarefa nunca terminará. Também
contamos com a ajuda de outra tarefa, que veremos em breve, que
monitorará o tempo decorrido e, consequentemente, chamará
"future.set_result()".

   async def async_sleep(seconds: float):
       future = asyncio.Future()
       time_to_wake = time.time() + seconds
       # Adiciona uma tarefa de monitoramento ao laço de eventos.
       watcher_task = asyncio.create_task(_sleep_watcher(future, time_to_wake))
       # Bloqueia até future ser marcado como concluído.
       await future

A seguir, usamos um objeto "YieldToEventLoop()" bastante simples para
"yield" do seu método "__await__", cedendo o controle ao laço de
eventos. Isso é efetivamente o mesmo que chamar "asyncio.sleep(0)",
mas essa abordagem oferece mais clareza, sem mencionar que é um tanto
quanto trapaça usar "asyncio.sleep" ao demonstrar como implementá-lo!

Como de costume, o laço de eventos percorre suas tarefas, concedendo-
lhes o controle e recebendo-o de volta quando elas pausam ou terminam.
A tarefa "watcher_task", que executa a corrotina
"_sleep_watcher(...)", será invocada uma vez por ciclo completo do
laço de eventos. A cada retomada, ela verificará o tempo e, se não
tiver decorrido tempo suficiente, pausará novamente e devolverá o
controle ao laço de eventos. Assim que o tempo suficiente tiver
decorrido, "_sleep_watcher(...)" marcará o futuro como concluído e
finalizará, saindo de seu laço "while" infinito. Dado que essa tarefa
auxiliar é invocada apenas uma vez por ciclo do laço de eventos, você
está correto ao observar que essa suspensão assíncrona durará *pelo
menos* três segundos, em vez de exatamente três segundos. Observe que
isso também se aplica a "asyncio.sleep".

   class YieldToEventLoop:
       def __await__(self):
           yield

   async def _sleep_watcher(future, time_to_wake):
       while True:
           if time.time() >= time_to_wake:
               # Isso marca future como concluído.
               future.set_result(None)
               break
           else:
               await YieldToEventLoop()

Aqui está a saída completa do programa:

   $ python custom-async-sleep.py
   Começando a suspensão assíncrona no horário: 14:52:22.
   Eu gosto de trabalhar. Trabalhar, trabalhar.
   Eu gosto de trabalhar. Trabalhar, trabalhar.
   Eu gosto de trabalhar. Trabalhar, trabalhar.
   Concluí a suspensão assíncrona no horário: 14:52:25.

Você pode achar que esta implementação de suspensão assíncrona foi
desnecessariamente complexa. E, bem, foi mesmo. O exemplo tinha como
objetivo demonstrar a versatilidade dos futures com um exemplo simples
que poderia ser replicado para necessidades mais complexas. Para
referência, você poderia implementá-lo sem futures, assim:

   async def simpler_async_sleep(seconds):
       time_to_wake = time.time() + seconds
       while True:
           if time.time() >= time_to_wake:
               return
           else:
               await YieldToEventLoop()

Mas por agora é tudo. Espero que agora esteja pronto para mergulhar
com mais confiança na programação assíncrona ou consultar tópicos
avançados no "restante da documentação".
