API C PyTime
************

Adicionado na versão 3.13.

A API C de relógios provê acesso a relógios do sistema. Ela é similar
ao módulo Python "time".

Para uma API C relacionada ao módulo "datetime", veja Objetos
DateTime.


Tipos
=====

type PyTime_t

   Um registro de data e hora ou uma duração em nanossegundos,
   representados como um inteiro de 64 bits com sinal.

   O ponto de referência para registros de data e hora depende do
   relógio usado. Por exemplo, "PyTime_Time()" retorna registros
   relativos à época UNIX.

   É suportada uma amplitude em torno de [-292.3 anos; +292.3 anos].
   Usando o início da época UNIX (1º de Janeiro de 1970) como
   referência, a gama de datas suportadas é em torno de [1677-09-21;
   2262-04-11]. Os limites exatos são expostos como constantes:

PyTime_t PyTime_MIN

   Valor mínimo de "PyTime_t".

PyTime_t PyTime_MAX

   Valor máximo de "PyTime_t".


Funções de relógio
==================

As funções a seguir aceitam um ponteiro para PyTime_t ao qual elas
atribuem o valor de um determinado relógio. Detalhes de cada relógio
estão disponíveis nas documentações das funções Python
correspondentes.

As funções retornam "0" em caso de sucesso, ou "-1" (com uma exceção
definida) em caso de falha.

Em caso de estouro de inteiros, elas definem a exceção
"PyExc_OverflowError" e definem "*result" como o valor limitado ao
intervalo "[PyTime_MIN; PyTime_MAX]". (Em sistemas atuais, estouros de
inteiros são provavelmente causados por uma má configuração do tempo
do sistema).

Como qualquer outra API C (se não especificado o contrário), as
funções devem ser chamadas com um *estado de thread anexado*.

int PyTime_Monotonic(PyTime_t *result)

   Lê o relógio monótono. Veja "time.monotonic()" para detalhes
   importantes sobre este relógio.

int PyTime_PerfCounter(PyTime_t *result)

   Lê o contador de desempenho. Veja "time.perf_counter()" para
   detalhes importantes sobre este relógio.

int PyTime_Time(PyTime_t *result)

   Lê o "relógio de parede". Veja "time.time()" para detalhes
   importantes sobre este relógio.


Funções de relógio brutas
=========================

Similar às funções de relógio, mas não definem uma exceção em
condições de erro, e não requerem que o chamador tenha um *estado de
thread anexado*.

Em caso de sucesso, as funções retornam "0".

Em caso de falha, elas definem "*result" como "0" e retornam "-1",
*sem* definir uma exceção. Para acessar a causa do erro, *anexe* um
*estado de thread* e chame a função regular (sem o sufixo "Raw").
Observe que a função regular pode ser bem-sucedida mesmo após o "Raw"
falhar.

int PyTime_MonotonicRaw(PyTime_t *result)

   Similar a "PyTime_Monotonic()", mas não define uma exceção em caso
   de erro, e não exige um *estado de thread anexado*.

int PyTime_PerfCounterRaw(PyTime_t *result)

   Similar a "PyTime_PerfCounter()", mas não define uma exceção em
   caso de erro e não requer um *estado de thread anexado*.

int PyTime_TimeRaw(PyTime_t *result)

   Similar a "PyTime_Time()", mas não define uma exceção em caso de
   erro e não requer um *estado de thread anexado*.


Funções de conversão
====================

double PyTime_AsSecondsDouble(PyTime_t t)

   Converte um registro de data e hora para uma quantidade de segundos
   como um double C.

   Esta função nunca falha, mas note que double tem acurácia limitada
   para valores grandes.
