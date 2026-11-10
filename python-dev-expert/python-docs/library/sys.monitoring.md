"sys.monitoring" --- Monitoramento de eventos de execução
*********************************************************

Adicionado na versão 3.12.

======================================================================

Nota:

  "sys.monitoring" é um espaço de nomes dentro do módulo "sys", não um
  módulo independente, e "import sys.monitoring" falharia com
  "ModuleNotFoundError". Em vez disso, basta usar "import sys" e então
  usar "sys.monitoring".

Esse espaço de nomes fornece acesso às funções e constantes
necessárias para ativar e controlar o monitoramento de eventos.

À medida que os programas são executados, ocorrem eventos que podem
ser de interesse para as ferramentas que monitoram a execução. O
espaço de nomes "sys.monitoring" fornece meios para receber retornos
de chamada quando ocorrem eventos de interesse.

A API de monitoramento consiste em três componentes:

* Identificadores de ferramenta

* Eventos

* Funções de retorno de chamadas


Identificadores de ferramenta
=============================

Um identificador de ferramenta é um número inteiro e o nome associado.
Os identificadores de ferramenta são usados para evitar que as
ferramentas interfiram umas nas outras e para permitir que várias
ferramentas operem ao mesmo tempo. Atualmente, as ferramentas são
totalmente independentes e não podem ser usadas para monitorar umas às
outras. Essa restrição poderá ser suspensa no futuro.

Antes de registrar ou ativar eventos, uma ferramenta deve escolher um
identificador. Os identificadores são números inteiros no intervalo de
0 a 5, inclusive.


Registro e uso de ferramentas
-----------------------------

sys.monitoring.use_tool_id(tool_id: int, name: str, /) -> None

   Deve ser chamado antes que *tool_id* possa ser usado. *tool_id*
   deve estar no intervalo de 0 a 5, inclusive. Levanta um
   "ValueError" se *tool_id* estiver em uso.

sys.monitoring.clear_tool_id(tool_id: int, /) -> None

   Cancela o registro de todos os eventos e funções de retorno de
   chamada associados a *tool_id*.

   Adicionado na versão 3.14.

sys.monitoring.free_tool_id(tool_id: int, /) -> None

   Deve ser chamado quando uma ferramenta não precisar mais de
   *tool_id*. Chamará "clear_tool_id()" antes de liberar *tool_id*.

   Alterado na versão 3.14: Agora chama "clear_tool_id()" antes de
   liberar *tool_id*. Anteriormente, não desabilitava eventos globais
   ou locais associados a *tool_id*, nem cancelava o registro de
   quaisquer funções de callback.

sys.monitoring.get_tool(tool_id: int, /) -> str | None

   Retorna o nome da ferramenta se *tool_id* estiver em uso; caso
   contrário, retorna "None". *tool_id* deve estar no intervalo de 0 a
   5, inclusive.

Todas as IDs são tratadas da mesma forma pela VM com relação aos
eventos, mas as seguintes IDs são predefinidas para facilitar a
cooperação entre as ferramentas:

   sys.monitoring.DEBUGGER_ID = 0
   sys.monitoring.COVERAGE_ID = 1
   sys.monitoring.PROFILER_ID = 2
   sys.monitoring.OPTIMIZER_ID = 5


Eventos
=======

Os seguintes eventos são suportados:

sys.monitoring.events.BRANCH_LEFT

   Uma ramificação condicional vai para a esquerda.

   Cabe à ferramenta determinar como apresentar os ramos "esquerdo" e
   "direito". Não há garantia de qual ramo é "esquerdo" e qual é
   "direito", exceto que será consistente durante toda a duração do
   programa.

sys.monitoring.events.BRANCH_RIGHT

   Uma ramificação condicional vai para a direita.

sys.monitoring.events.CALL

   Uma chamada no código Python (o evento ocorre antes da chamada).

sys.monitoring.events.C_RAISE

   Uma exceção levantada por qualquer chamável, exceto funções Python
   (o evento ocorre após a saída).

sys.monitoring.events.C_RETURN

   Retorno de qualquer chamável, exceto por funções Python (o evento
   ocorre após o retorno).

sys.monitoring.events.EXCEPTION_HANDLED

   Uma exceção é tratada.

sys.monitoring.events.INSTRUCTION

   Uma instrução VM está prestes a ser executada.

sys.monitoring.events.JUMP

   É feito um salto incondicional no gráfico do fluxo de controle.

sys.monitoring.events.LINE

   Está prestes a ser executada uma instrução que tem um número de
   linha diferente da instrução anterior.

sys.monitoring.events.PY_RESUME

   Retomada de uma função Python (para funções geradoras e de
   corrotina), exceto para chamadas "throw()".

sys.monitoring.events.PY_RETURN

   Retorno de uma função Python (ocorre imediatamente antes do
   retorno, o quadro do receptor estará na pilha).

sys.monitoring.events.PY_START

   Início de uma função Python (ocorre imediatamente após a chamada, o
   quadro do receptor da chamada estará na pilha)

sys.monitoring.events.PY_THROW

   Uma função Python é retomada por uma chamada "throw()".

sys.monitoring.events.PY_UNWIND

   Saída de uma função Python durante o desenrolamento de uma exceção.
   Isso inclui exceções levantadas diretamente na função e que podem
   continuar a se propagar.

sys.monitoring.events.PY_YIELD

   Produz de uma função Python (ocorre imediatamente antes do yield, o
   quadro do receptor estará na pilha).

sys.monitoring.events.RAISE

   Uma exceção é levantada, exceto aquelas que causam um evento
   "STOP_ITERATION".

sys.monitoring.events.RERAISE

   Uma exceção é levantada novamente, por exemplo, no final de um
   bloco "finally".

sys.monitoring.events.STOP_ITERATION

   Uma exceção artificial "StopIteration" é levantada; consulte o
   evento STOP_ITERATION.

Mais eventos poderão ser adicionados no futuro.

Esses eventos são atributos do espaço de nomes
"sys.monitoring.events". Cada evento é representado como uma constante
de potência de 2 inteiros. Para definir um conjunto de eventos, basta
aplicar OU (OR) bit a bit nos eventos individuais juntos. Por exemplo,
para especificar os eventos "PY_RETURN" e "PY_START", use a expressão
"PY_RETURN | PY_START".

sys.monitoring.events.NO_EVENTS

   Um apelido para "0" para que os usuários possam fazer comparações
   explícitas como:

      if get_events(DEBUGGER_ID) == NO_EVENTS:
          ...

   Definir este evento desativa todos os eventos.


Eventos locais
--------------

Os eventos locais estão associados à execução normal do programa e
ocorrem em locais claramente definidos. Todos os eventos locais podem
ser desativados por local. Os eventos locais são:

* "PY_START"

* "PY_RESUME"

* "PY_RETURN"

* "PY_YIELD"

* "CALL"

* "LINE"

* "INSTRUCTION"

* "JUMP"

* "BRANCH_LEFT"

* "BRANCH_RIGHT"

* "STOP_ITERATION"


Evento descontinuado
--------------------

* "BRANCH"

O evento "BRANCH" foi descontinuado na versão 3.14. Usar os eventos
"BRANCH_LEFT" e "BRANCH_RIGHT" proporcionará um desempenho muito
melhor, pois podem ser desabilitados independentemente.


Eventos auxiliares
------------------

Os eventos auxiliares podem ser monitorados como outros eventos, mas
são controlados por outro evento:

* "C_RAISE"

* "C_RETURN"

Os eventos "C_RETURN" e "C_RAISE" são controlados pelo evento "CALL".
Os eventos "C_RETURN" e "C_RAISE" só serão vistos se o evento "CALL"
correspondente estiver sendo monitorado.


Outros eventos
--------------

Outros eventos não estão necessariamente vinculados a um local
específico no programa e não podem ser desativados individualmente por
local.

Os outros eventos que podem ser monitorados são:

* "PY_THROW"

* "PY_UNWIND"

* "RAISE"

* "EXCEPTION_HANDLED"

* "RERAISE"

Alterado na versão 3.15: Outros eventos agora podem ser ativados e
desativados individualmente para cada objeto de código. Retornar
"DISABLE" a partir de um função de retorno (callback) desativa o
evento para todo o objeto de código (para a ferramenta atual).


O evento STOP_ITERATION
-----------------------

**PEP 380** especifica que uma exceção "StopIteration" é levantada ao
retornar um valor de um gerador ou corrotina. No entanto, essa é uma
maneira muito ineficiente de retornar um valor, portanto, algumas
implementações do Python, especialmente o CPython 3.12+, não levantam
uma exceção, a menos que ela seja visível para outro código.

Para permitir que as ferramentas monitorem exceções reais sem reduzir
a velocidade dos geradores e das corrotinas, o evento "STOP_ITERATION"
é fornecido. O "STOP_ITERATION" pode ser desativado localmente.

Observe que o evento "STOP_ITERATION" e o evento "RAISE" para uma
exceção "StopIteration" são equivalentes e tratados como
intercambiáveis ao gerar eventos. As implementações favorecerão
"STOP_ITERATION" por questões de desempenho, mas podem gerar um evento
"RAISE" com uma "StopIteration".


Ativação e desativação de eventos
=================================

Para monitorar um evento, ele deve ser ativado e uma função de retorno
correspondente deve ser registrada. Os eventos podem ser ativados ou
desativados definindo-os globalmente e/ou para um objeto código
específico. Um evento vai acionar apenas uma vez, mesmo se ele for
ligado globalmente e localmente.


Definir eventos globalmente
---------------------------

Os eventos podem ser controlados globalmente, modificando o conjunto
de eventos que estão sendo monitorados.

sys.monitoring.get_events(tool_id: int, /) -> int

   Retorna o endereço "int" que representa todos os eventos ativos.

sys.monitoring.set_events(tool_id: int, event_set: int, /) -> None

   Ativa todos os eventos definidos em *event_set*. Levanta um
   "ValueError" se *tool_id* não estiver em uso.

Nenhum evento está ativo por padrão.


Eventos por objeto código
-------------------------

Os eventos também podem ser controlados por objeto código. As funções
definidas abaixo que aceitam um "types.CodeType" devem estar
preparadas para aceitar um objeto semelhante de funções que não são
definidas no Python (veja API C de monitoramento).

sys.monitoring.get_local_events(tool_id: int, code: CodeType, /) -> int

   Retorna todos os eventos locais para *code*

sys.monitoring.set_local_events(tool_id: int, code: CodeType, event_set: int, /) -> None

   Ativa todos os eventos locais para *code* que estão definidos em
   *event_set*. Levanta a "ValueError" se *tool_id* não estiver em
   uso.


Desativação de eventos
----------------------

sys.monitoring.DISABLE

   Um valor especial que pode ser retornado de um função de retorno
   função para desativar eventos para o local do código atual.

Os eventos locais podem ser desativados para um local de código
específico, retornando "sys.monitoring.DISABLE" de uma função de
retorno de chamada. Isso não altera quais eventos são definidos ou
quaisquer outros locais de código para o mesmo evento.

Outros eventos podem ser desabilitados individualmente para cada
objeto código, fazendo com que uma função de retorno de chamada
(callback) retorne "sys.monitoring.DISABLE". Isso desabilita o evento
para todo o objeto código (para a ferramenta atual).

A desativação de eventos para locais específicos é muito importante
para o monitoramento de alto desempenho. Por exemplo, um programa pode
ser executado em um depurador sem sobrecarga se o depurador desativar
todo o monitoramento, exceto alguns pontos de interrupção.

sys.monitoring.restart_events() -> None

   Habilita todos os eventos que foram desabilitados por
   "sys.monitoring.DISABLE" para todas as ferramentas.


Registro de funções de retorno de chamada
=========================================

sys.monitoring.register_callback(tool_id: int, event: int, func: Callable | None, /) -> Callable | None

   Registra o chamável *func* para o *event* com o *tool_id* fornecido

   Se outra função de retorno tiver sido registrada para o *tool_id* e
   o *event* fornecidos, ela será cancelada e retornada. Caso
   contrário, "register_callback()" retorna "None".

   Levanta um evento de auditoria "sys.monitoring.register_callback"
   com o argumento "func".

As funções podem ser canceladas chamando
"sys.monitoring.register_callback(tool_id, event, None)".

As funções de retorno de chamada podem ser registradas e canceladas a
qualquer momento.

Os retornos de chamada são chamados apenas uma vez, independentemente
de o evento estar ativado global e localmente. Portanto, se um evento
puder ser ativado tanto para eventos globais quanto locais pelo seu
código, o retorno de chamada precisa ser escrito para lidar com
qualquer um dos gatilhos.


Argumentos da função de retorno de chamada
------------------------------------------

sys.monitoring.MISSING

   Um valor especial que é passado para uma função de retorno para
   indicar que não há argumento para a chamada.

Quando ocorre um evento ativo, a função de retorno de chamada
registrada é chamada. Funções de retorno retornando um objeto
diferente de "DISABLE" vai ter nenhum efeito. Eventos diferentes
fornecerão à função de retorno de chamada argumentos diferentes, como
segue:

* "PY_START" e "PY_RESUME":

     func(code: CodeType, instruction_offset: int) -> object

* "PY_RETURN" e "PY_YIELD":

     func(code: CodeType, instruction_offset: int, retval: object) -> object

* "CALL", "C_RAISE" e "C_RETURN" (*arg0* pode ser "MISSING"
  especificamente):

     func(code: CodeType, instruction_offset: int, callable: object, arg0: object) -> object

  *code* representa o objeto de código onde a chamada está sendo
  feita, enquanto *callable* é o objeto que está prestes a ser chamado
  (e, portanto, acionou o evento). Se não houver argumentos, *arg0* é
  definido como "sys.monitoring.MISSING".

  Para métodos de instância, *callable* será o objeto função
  encontrado na classe com *arg0* definido para a instância (ou seja,
  o argumento "self" para o método).

* "RAISE", "RERAISE", "EXCEPTION_HANDLED", "PY_UNWIND", "PY_THROW" e
  "STOP_ITERATION":

     func(code: CodeType, instruction_offset: int, exception: BaseException) -> object

* "LINE":

     func(code: CodeType, line_number: int) -> object

* "BRANCH_LEFT", "BRANCH_RIGHT" e "JUMP":

     func(code: CodeType, instruction_offset: int, destination_offset: int) -> object

  Observe que o *destination_offset* é onde o código será executado em
  seguida.

* "INSTRUCTION":

     func(code: CodeType, instruction_offset: int) -> object
