Suporte do Python para threads livres
*************************************

A partir da versão 3.13, o CPython tem suporte para uma compilação do
Python chamada *threads livres* (em inglês, free threading), onde a
*trava global do interpretador* (GIL) está desabilitada. A execução
com threads livres permite a utilização total do poder de
processamento disponível, executando threads em paralelo nos núcleos
de CPU disponíveis. Embora nem todos os softwares se beneficiem disso
automaticamente, os programas projetados com uso de threads em mente
serão executados mais rapidamente em hardware com vários núcleos.

Alguns pacotes de terceiros, em particular aqueles com um *módulo de
extensão*, podem não estar prontos para uso em uma construção com
threads livres e habilitarão novamente a *GIL*.

Este documento descreve as implicações de threads livres para o código
Python. Veja Suporte a extensões da API C para threads livres para
informações sobre como escrever extensões C que oferecem suporte à
construção com threads livres.

Ver também:

  **PEP 703** – Tornando a trava global do interpretador opcional no
  CPython para uma descrição geral do Python com threads livres.


Instalação
==========

A partir do Python 3.13, os instaladores oficiais do macOS e do
Windows oferecem suporte opcional à instalação de binários Python com
threads livres. Os instaladores estão disponíveis em
https://www.python.org/downloads/.

Para obter informações sobre outras plataformas, consulte Instalando
um Python com threads livres, um guia de instalação mantido pela
comunidade para instalar o Python com threads livres.

Ao construir o CPython a partir do código-fonte, a opção de
configuração "--disable-gil" deve ser usada para construir um
interpretador Python com threads livres.


Identificando um Python com threads livres
==========================================

Para verificar se o interpretador atual oferece suporte a threads
livres, "python -VV" e "sys.version" contêm "free-threading build". A
nova função "sys._is_gil_enabled()" pode ser usada para verificar se a
GIL está realmente desabilitada no processo em execução.

A variável de configuração
"sysconfig.get_config_var("Py_GIL_DISABLED")" pode ser usada para
determinar se a compilação tem suporte a threads livres. Se a variável
for definida como "1", a compilação tem suporte a threads livres. Este
é o mecanismo recomendado para decisões relacionadas à configuração da
construção.


A trava global do interpretador no Python com threads livres
============================================================

Construções com threads livres do CPython oferecem suporte a
opcionalmente executar com a GIL habilitada em tempo de execução
usando a variável de ambiente "PYTHON_GIL" ou a opção de linha de
comando "-X gil".

A GIL também pode ser habilitada automaticamente ao importar um módulo
de extensão da API C que não esteja explicitamente marcado como
oferecendo suporte a threads livres. Um aviso será impresso neste
caso.

Além da documentação de pacotes individuais, os seguintes sites
rastreiam o status do suporte de pacotes populares para threads
livres:

* https://py-free-threading.github.io/tracking/

* https://hugovk.github.io/free-threaded-wheels/


Segurança nas threads
=====================

A construção com threads livres do CPython visa fornecer comportamento
de segurança às threads semelhante no nível do Python à construção
padrão com GIL habilitada. Tipos embutidos como "dict", "list" e "set"
usam travas internas para proteger contra modificações simultâneas de
maneiras que se comportam de forma semelhante à GIL. Veja Garantias de
segurança de thread para as garantias fornecidas por tipos embutidos.

Nota:

  É recomendável usar "threading.Lock" ou outras primitivas de
  sincronização em vez de depender de travas internas de tipos
  embutidos, quando possível.


Limitações conhecidas
=====================

Esta seção descreve as limitações conhecidas da construção do Python
com threads livres.


Imortalização
-------------

Na construção com threads livres, alguns objetos são *imortais*.
Objetos imortais não são desalocados e têm contagens de referência que
nunca são modificadas. Isso é feito para evitar contenção de contagem
de referências que impediria o dimensionamento multithread eficiente.

A partir da versão 3.14, a imortalização está limitada a:

* Constantes de código: literais numéricos, literais de string e
  literais de tupla compostos por outras constantes.

* Strings internadas por "sys.intern()".


Objetos quadro
--------------

Não é seguro acessar "frame.f_locals" a partir de um objeto frame se
esse frame estiver sendo executado em outra thread, e fazê-lo pode
causar a falha do interpretador.


Iteradores
----------

Geralmente, não é seguro para thread acessar o mesmo objeto iterador a
partir de múltiplas threads simultaneamente, e as threads podem
encontrar elementos duplicados ou ausentes.


Desempenho com thread única
---------------------------

A construção com threads livres apresenta sobrecarga adicional na
execução de código Python em comparação com a construção padrão com
GIL habilitado. A quantidade de sobrecarga depende da carga de
trabalho e do hardware. No conjunto de benchmarks pyperformance, a
sobrecarga média varia de cerca de 1% no macOS aarch64 a 8% em
sistemas Linux x86-64.


Mudanças comportamentais
========================

Esta seção descreve as mudanças comportamentais do CPython com a
construção com threads livres.


Variáveis de contexto
---------------------

Na construção com threads livres, o sinalizador
"thread_inherit_context" é definido como true por padrão, o que faz
com que threads criadas com "threading.Thread" iniciem com uma cópia
de "Context()" do chamador de "start()". Na construção padrão com GIL
habilitada, o sinalizador é definido como false por padrão, então as
threads iniciam com um "Context()" vazio.


Filtros de aviso
----------------

Na construção com threads livres, o sinalizador
"context_aware_warnings" é definido como verdadeiro por padrão. Na
construção com GIL habilitada, o sinalizador é definido como falso por
padrão. Se o sinalizador for verdadeiro, o gerenciador de contexto
"warnings.catch_warnings" usa uma variável de contexto para filtros de
aviso. Se o sinalizador for falso, "catch_warnings" modifica a lista
de filtros globais, o que não é seguro para thread. Consulte o módulo
"warnings" para obter mais detalhes.


Aumento do consumo de memória
-----------------------------

A construção com threads livres geralmente consome mais memória do que
a construção padrão. Isso ocorre por vários motivos, principalmente
devido a decisões de projeto.


Todas as strings internadas são imortais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nas versões modernas do Python (desde a versão 2.3), internar uma
string (por exemplo, com "sys.intern()") não a torna imortal. Em vez
disso, se a última referência a essa string deixar de existir, ela
será removida da tabela de strings internadas. Isso não ocorre na
construção com threads livres, na qual qualquer string internada
torna-se imortal, persistindo até o desligamento do interpretador.


Objetos não-GC têm um cabeçalho de objeto maior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The free-threaded build uses a different "PyObject" structure.
Instead of having the GC related information allocated before the
"PyObject" structure, like in the default build, the GC related info
is part of the normal object header.  For example, on the AMD64
platform, "None" uses 32 bytes on the free-threaded build vs 16 bytes
for the default build.  GC objects (such as dicts and lists) are the
same size for both builds since the free-threaded build does not use
additional space for the GC info.


QSBR can delay freeing of memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to safely implement lock-free data structures, a safe memory
reclamation (SMR) scheme is used, known as quiescent state-based
reclamation (QSBR).  This means that the memory backing data
structures allowing lock-free access will use QSBR, which defers the
free operation, rather than immediately freeing the memory.  Two
examples of these data structures are the list object and the
dictionary keys object.  See "InternalDocs/qsbr.md" in the CPython
source tree for more details on how QSBR is implemented.  Running
"gc.collect()" should cause all memory being held by QSBR to be
actually freed.  Note that even when QSBR frees the memory, the
underlying memory allocator may not immediately return that memory to
the OS and so the resident set size (RSS) of the process might not
decrease.


mimalloc allocator vs pymalloc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default build will normally use the "pymalloc" memory allocator
for small allocations (512 bytes or smaller).  The free-threaded build
does not use pymalloc and allocates all Python objects using the
"mimalloc" allocator.  The pymalloc allocator has the following
properties that help keep memory usage low: small per-allocated-block
overhead, effective memory fragmentation prevention, and quick return
of free memory to the operating system.  The mimalloc allocator does
quite well in these respects as well but can have some more overhead.

In the free-threaded build, mimalloc manages memory in a number of
separate heaps (currently four).  For example, all GC supporting
objects are allocated from their own heap.  Using separate heaps means
that free memory in one heap cannot be used for an allocation that
uses another heap.  Also, some heaps are configured to use QSBR
(quiescent-state based reclamation) when freeing the memory that backs
up the heap (known as "pages" in mimalloc terminology).  The use of
QSBR creates a delay between all memory blocks for a page being freed
and the memory page being released, either for new allocations or back
to the OS.

The mimalloc allocator also defers returning freed memory back to the
OS.  You can reduce that delay by setting the environment variable
"MIMALLOC_PURGE_DELAY" to "0".  Note that this will likely reduce the
performance of the allocator.


Free-threaded reference counting can cause objects to live longer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the default build, when an object's reference count reaches zero,
it is normally deallocated.  The free-threaded build uses "biased
reference counting", with a fast-path for objects "owned" by the
current thread and a slow path for other objects.  See **PEP 703** for
additional details.  Any time an object's reference count ends up in a
"queued" state, deallocation can be deferred.  The queued state is
cleared from the "eval breaker" section of the bytecode evaluator.

The free-threaded build also allows a different mode of reference
counting, known as "deferred reference counting".  This mode is
enabled by setting a flag on a per-object basis.  Deferred reference
counting is enabled for the following types:

* module objects

* module top-level functions

* class methods defined in the class scope

* descriptor objects

* thread-local objects, created by "threading.local"

When deferred reference counting is enabled, references from Python
function stacks are not added to the reference count.  This scheme
reduces the overhead of reference counting, especially for objects
used from multiple threads. Because the stack references are not
counted, objects with deferred reference counting are not immediately
freed when their internal reference count goes to zero.  Instead, they
are examined by the next GC run and, if no stack references to them
are found, they are freed.  This means these objects are freed by the
GC and not when their reference count goes to zero, as is typical.


Per-thread reference counting can delay freeing objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To avoid contention on the reference count fields of frequently shared
objects, the free-threaded build also uses "per-thread reference
counting" for a few selected object types.  Rather than updating a
single shared reference count, each thread maintains its own local
reference count array, indexed by a unique id assigned to the object.
The true reference count is only computed by summing the per-thread
counts when the object's local count drops to zero.  Per-thread
reference counting is currently used for:

* heap type objects (classes created in Python)

* code objects

* the "__dict__" of module objects

Because the per-thread counts must be merged back to the object before
it can be deallocated, objects using per-thread reference counting are
typically freed later than they would be in the default build.  In
particular, such an object is usually not freed until the thread that
referenced it reaches a safe point (for example, in the "eval breaker"
section of the bytecode evaluator) or exits.  Running "gc.collect()"
will merge the per-thread counts and allow these objects to be freed.
