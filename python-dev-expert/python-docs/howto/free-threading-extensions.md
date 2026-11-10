Suporte a extensões da API C para threads livres
************************************************

A partir da versão 3.13, o CPython tem suporte para execução com a
*trava global do interpretador* (GIL) desabilitada em uma configuração
chamada *threads livres*. Este documento descreve como adaptar
extensões da API C para ter suporte a threads livres.


Identificando a construção com threads livres em C
==================================================

A API C do CPython expõe a macro "Py_GIL_DISABLED": na construção com
threads livres ela está definida como "1", e na construção regular ela
não está definida. Você pode usá-la para ativar o código que é
executado apenas na construção com threads livres:

   #ifdef Py_GIL_DISABLED
   /* código que só vai ser executado na construção com threads livres */
   #endif

Nota:

  No Windows, esta macro não é definida automaticamente, mas deve ser
  especificada ao compilador durante a compilação. A função
  "sysconfig.get_config_var()" pode ser usada para determinar se o
  interpretador em execução tinha a macro definida.


Inicialização de módulo
=======================

Os módulos de extensão precisam indicar explicitamente que têm suporte
à execução com a GIL desabilitada; caso contrário, importar a extensão
levantará um aviso e ativará a GIL em tempo de execução.

Há duas maneiras de indicar que um módulo de extensão tem suporte à
execução com a GIL desabilitada, dependendo se a extensão usa
inicialização monofásica ou multifásica.


Inicialização multifásica
-------------------------

Extensions that use multi-phase initialization (functions like
"PyModuleDef_Init()", "PyModExport_*" export hook,
"PyModule_FromSlotsAndSpec()") should add a "Py_mod_gil" slot in the
module definition. If your extension supports older versions of
CPython, you should guard the slot with a "PY_VERSION_HEX" check.

   static struct PyModuleDef_Slot module_slots[] = {
       ...
   #if PY_VERSION_HEX >= 0x030D0000
       {Py_mod_gil, Py_MOD_GIL_NOT_USED},
   #endif
       {0, NULL}
   };


Inicialização monofásica
------------------------

Extensions that use legacy single-phase initialization (that is,
"PyModule_Create()") should call "PyUnstable_Module_SetGIL()" to
indicate that they support running with the GIL disabled.  The
function is only defined in the free-threaded build, so you should
guard the call with "#ifdef Py_GIL_DISABLED" to avoid compilation
errors in the regular build.

   static struct PyModuleDef moduledef = {
       PyModuleDef_HEAD_INIT,
       ...
   };

   PyMODINIT_FUNC
   PyInit_mymodule(void)
   {
       PyObject *m = PyModule_Create(&moduledef);
       if (m == NULL) {
           return NULL;
       }
   #ifdef Py_GIL_DISABLED
       PyUnstable_Module_SetGIL(m, Py_MOD_GIL_NOT_USED);
   #endif
       return m;
   }


Diretrizes gerais de API
========================

A maior parte da API C é segura para thread, mas há algumas exceções.

* **Campos de structs**: acessar campos em objetos ou structs da API C
  do Python diretamente não é seguro para thread se o campo puder ser
  modificado simultaneamente.

* **Macros**: macros de acesso como "PyList_GET_ITEM",
  "PyList_SET_ITEM" e macros como "PySequence_Fast_GET_SIZE" que usam
  o objeto retornado por "PySequence_Fast()" não realizam nenhuma
  verificação de erro ou trava. Essas macros não são seguras para
  thread se o objeto contêiner puder ser modificado simultaneamente.

* **Referências emprestadas**: as funções da API C que retornam
  *referências emprestadas* podem não ser seguras para thread se o
  objeto que as contêm for modificado simultaneamente. Veja a seção
  sobre referências emprestadas para mais informações.


Segurança de threads de contêineres
-----------------------------------

Contêineres como "PyListObject", "PyDictObject" e "PySetObject"
executam uma trava interna na construção com threads livres. Por
exemplo, "PyList_Append()" irá travar a lista antes de anexar um item.


"PyDict_Next"
~~~~~~~~~~~~~

Uma exceção notável é "PyDict_Next()", que não trava o dicionário.
Você deve usar "Py_BEGIN_CRITICAL_SECTION" para proteger o dicionário
enquanto itera sobre ele se o dicionário puder ser modificado
simultaneamente:

   Py_BEGIN_CRITICAL_SECTION(dict);
   PyObject *key, *value;
   Py_ssize_t pos = 0;
   while (PyDict_Next(dict, &pos, &key, &value)) {
       ...
   }
   Py_END_CRITICAL_SECTION();


Referências emprestadas
=======================

Algumas funções da API C retornam *referências emprestadas*. Essas
APIs não são seguras para thread se o objeto que as contém for
modificado simultaneamente. Por exemplo, não é seguro usar
"PyList_GetItem()" se a lista puder ser modificada simultaneamente.

A tabela a seguir lista algumas APIs de referências emprestadas e suas
substituições que retornam *referências fortes*.

+-------------------------------------+-------------------------------------+
| API de referências emprestadas      | API de referências fortes           |
|=====================================|=====================================|
| "PyList_GetItem()"                  | "PyList_GetItemRef()"               |
+-------------------------------------+-------------------------------------+
| "PyList_GET_ITEM()"                 | "PyList_GetItemRef()"               |
+-------------------------------------+-------------------------------------+
| "PyDict_GetItem()"                  | "PyDict_GetItemRef()"               |
+-------------------------------------+-------------------------------------+
| "PyDict_GetItemWithError()"         | "PyDict_GetItemRef()"               |
+-------------------------------------+-------------------------------------+
| "PyDict_GetItemString()"            | "PyDict_GetItemStringRef()"         |
+-------------------------------------+-------------------------------------+
| "PyDict_SetDefault()"               | "PyDict_SetDefaultRef()"            |
+-------------------------------------+-------------------------------------+
| "PyDict_Next()"                     | nenhuma (veja PyDict_Next)          |
+-------------------------------------+-------------------------------------+
| "PyWeakref_GetObject()"             | "PyWeakref_GetRef()"                |
+-------------------------------------+-------------------------------------+
| "PyWeakref_GET_OBJECT()"            | "PyWeakref_GetRef()"                |
+-------------------------------------+-------------------------------------+
| "PyImport_AddModule()"              | "PyImport_AddModuleRef()"           |
+-------------------------------------+-------------------------------------+
| "PyCell_GET()"                      | "PyCell_Get()"                      |
+-------------------------------------+-------------------------------------+

Nem todas as APIs que retornam referências emprestadas são
problemáticas. Por exemplo, "PyTuple_GetItem()" é segura porque as
tuplas são imutáveis. Da mesma forma, nem todos os usos das APIs acima
são problemáticos. Por exemplo, "PyDict_GetItem()" é frequentemente
usado para analisar dicionários de argumentos nomeados em chamadas de
função; esses dicionários de argumentos nomeados efetivamente privados
(não acessíveis por outros threads), portanto, usar referências
emprestadas nesse contexto é seguro.

Algumas dessas funções foram adicionadas no Python 3.13. Você pode
usar o pacote pythoncapi-compat para fornecer implementações dessas
funções para versões mais antigas do Python.


APIs de alocação de memória
===========================

A API C de gerenciamento de memória do Python fornece funções em três
domínios de alocação diferentes: "raw", "mem" e "object". Para
segurança de thread, a construção com threads livres requer que apenas
objetos Python sejam alocados usando o domínio do objeto e que todos
os objetos Python sejam alocados usando esse domínio. Isso difere das
versões anteriores do Python, onde era apenas uma melhor prática e não
um requisito estrito.

Nota:

  Procure usos de "PyObject_Malloc()" em sua extensão e verifique se a
  memória alocada é usada para objetos Python. Use "PyMem_Malloc()"
  para alocar buffers em vez de "PyObject_Malloc()".


APIs da GIL e de estado de threads
==================================

Python fornece um conjunto de funções e macros para gerenciar o estado
de threads e a GIL, como:

* "PyThreadState_Ensure()", "PyThreadState_EnsureFromView()", and
  "PyThreadState_Release()"

* "PyGILState_Ensure()" e "PyGILState_Release()"

* "PyEval_SaveThread()" e "PyEval_RestoreThread()"

* "Py_BEGIN_ALLOW_THREADS" e "Py_END_ALLOW_THREADS"

These functions should still be used in the free-threaded build to
manage thread state even when the *GIL* is disabled.  For example, if
you create a thread outside of Python, you must call
"PyThreadState_Ensure()" before calling into the Python API to ensure
that the thread has a valid Python thread state.

Você deve continuar a chamar "PyEval_SaveThread()" ou
"Py_BEGIN_ALLOW_THREADS" em torno de operações de travamento, como E/S
ou aquisições de trava, para permitir que outras threads executem o
*coletor de lixo cíclico*.


Protegendo o estado interno das extensões
=========================================

Sua extensão pode ter um estado interno que foi previamente protegido
pela GIL. Talvez seja necessário adicionar uma trava para proteger
esse estado. A abordagem dependerá da sua extensão, mas alguns padrões
comuns incluem:

* **Caches**: caches globais são uma fonte comum de estado
  compartilhado. Considere usar uma trava para proteger o cache ou
  desativá-lo na construção com threads livres se o cache não for
  crítico para o desempenho.

* **Estado global**: o estado global pode precisar ser protegido por
  uma trava ou movido para o armazenamento local do thread. C11 e
  C++11 fornecem "thread_local" ou "_Thread_local" para armazenamento
  local de thread.


Seções críticas
===============

Na construção com threads livres, o CPython fornece um mecanismo
chamado "critical sections" (em português, "seções críticas") para
proteger dados que, de outra forma, seriam protegidos pela GIL. Embora
os autores da extensão possam não interagir diretamente com a
implementação da seção crítica interna, entender seu comportamento é
crucial ao usar determinadas funções da API C ou gerenciar o estado
compartilhado na construção com threads livres.


O que são seções críticas?
--------------------------

Conceitualmente, seções críticas atuam como uma camada de prevenção de
impasse construída sobre mutexes simples. Cada thread mantém uma pilha
de seções críticas ativas. Quando uma thread precisa adquirir uma
trava associada a uma seção crítica (por exemplo, implicitamente ao
chamar uma função de API C segura para thread como "PyDict_SetItem()",
ou explicitamente usando macros), ela tenta adquirir o mutex
subjacente.


Usando seções críticas
----------------------

As principais APIs para usar seções críticas são:

* "Py_BEGIN_CRITICAL_SECTION" e "Py_END_CRITICAL_SECTION" - Para
  travar um único objeto

* "Py_BEGIN_CRITICAL_SECTION2" e "Py_END_CRITICAL_SECTION2" - Para
  travar dois objetos simultaneamente

Essas macros devem ser usadas em pares correspondentes e devem
aparecer no mesmo escopo C, pois estabelecem um novo escopo local.
Essas macros são inoperantes em construções com threads livres,
portanto, podem ser adicionadas com segurança a códigos que precisam
suportar ambos os tipos de construção.

Um uso comum de uma seção crítica seria travar um objeto ao acessar um
atributo interno dele. Por exemplo, se um tipo de extensão tiver um
campo de contagem interno, você pode usar uma seção crítica ao ler ou
escrever nesse campo:

   // lê a contagem, retorna uma nova referência ao valor da contagem interna
   PyObject *result;
   Py_BEGIN_CRITICAL_SECTION(obj);
   result = Py_NewRef(obj->count);
   Py_END_CRITICAL_SECTION();
   return result;

   // escreve a contagem, consome referência de new_count
   Py_BEGIN_CRITICAL_SECTION(obj);
   obj->count = new_count;
   Py_END_CRITICAL_SECTION();


Como seções críticas funcionam
------------------------------

Ao contrário das travas tradicionais, as seções críticas não garantem
acesso exclusivo durante toda a sua duração. Se uma thread travar
enquanto mantém uma seção crítica (por exemplo, ao adquirir outro
bloqueio ou executar E/S), a seção crítica é temporariamente suspensa
— todas as travas são liberadas — e então retomada quando a operação
de bloqueio é concluída.

Esse comportamento é semelhante ao que ocorre com a GIL quando uma
thread faz uma chamada de bloqueio. As principais diferenças são:

* As seções críticas operam por objeto e não globalmente

* As seções críticas seguem uma disciplina de pilha dentro de cada
  thread (as macros "begin" e "end" impõem isso, pois devem ser
  pareadas e estar dentro do mesmo escopo)

* As seções críticas liberam e readquirem automaticamente travas em
  torno de potenciais operações de bloqueio


Prevenção de impasses
---------------------

Seções críticas ajudam a evitar impasses de duas maneiras:

1. Se uma thread tenta adquirir uma trava que já está sendo mantida
   por outra thread, ela primeiro suspende todas as suas seções
   críticas ativas, liberando temporariamente suas travas

2. Quando a operação de bloqueio for concluída, apenas a seção mais
   crítica será readquirida primeiro

Isso significa que você não pode depender de seções críticas aninhadas
para travar vários objetos simultaneamente, pois a seção crítica
interna pode suspender as externas. Em vez disso, use
"Py_BEGIN_CRITICAL_SECTION2" para travar dois objetos simultaneamente.

Observe que as travas descritas acima são apenas travas baseadas em
"PyMutex". A implementação da seção crítica não conhece ou afeta
outros mecanismos de trava que possam estar em uso, como mutexes
POSIX. Observe também que, embora o bloqueio em qualquer "PyMutex"
cause a suspensão das seções críticas, apenas os mutexes que fazem
parte delas são liberados. Se "PyMutex" for usado sem uma seção
crítica, ele não será liberado e, portanto, não terá a mesma
capacidade de evitar impasses.


Considerações importantes
-------------------------

* Seções críticas podem liberar temporariamente suas travas,
  permitindo que outras threads modifiquem os dados protegidos. Tenha
  cuidado ao fazer suposições sobre o estado dos dados após operações
  que possam causar bloqueios.

* Como as travas podem ser temporariamente liberadas (suspensas),
  entrar em uma seção crítica não garante acesso exclusivo ao recurso
  protegido durante toda a duração da seção. Se o código dentro de uma
  seção crítica chamar outra função que bloqueie (por exemplo,
  adquirir outra trava, executar E/S de bloqueio), todas as travas
  mantidas pela thread por meio de seções críticas serão liberadas.
  Isso é semelhante à forma como a GIL pode ser liberada durante
  chamadas de bloqueio.

* Somente a(s) trava(s) associada(s) à seção crítica mais recentemente
  inserida (superior) tem garantia de ser(em) mantida(s) em um
  determinado momento. As travas para seções críticas externas e
  aninhadas podem ter sido suspensas.

* Você pode travar no máximo dois objetos simultaneamente com essas
  APIs. Se precisar travar mais objetos, será necessário reestruturar
  seu código.

* Embora seções críticas não entrem em impasse se você tentar travar o
  mesmo objeto duas vezes, elas são menos eficientes do que travas
  reentrantes desenvolvidas especificamente para esse caso de uso.

* Ao usar "Py_BEGIN_CRITICAL_SECTION2", a ordem dos objetos não afeta
  a correção (a implementação lida com a prevenção de impasse), mas é
  uma boa prática sempre travar os objetos em uma ordem consistente.

* Lembre-se de que as macros de seção crítica servem principalmente
  para proteger o acesso a *objetos Python* que podem estar envolvidos
  em operações internas do CPython suscetíveis aos cenários de
  impasses descritos acima. Para proteger o estado de extensão
  puramente interno, mutexes padrão ou outras primitivas de
  sincronização podem ser mais apropriados.


Per-Object Locks ("ob_mutex")
-----------------------------

In the free-threaded build, each Python object contains a "ob_mutex"
field of type "PyMutex".  This mutex is **reserved for use by the
critical section API** ("Py_BEGIN_CRITICAL_SECTION" /
"Py_END_CRITICAL_SECTION").

Aviso:

  Do **not** lock "ob_mutex" directly with
  "PyMutex_Lock(&obj->ob_mutex)". Mixing direct "PyMutex_Lock" calls
  with the critical section API on the same mutex can cause deadlocks.

Even if your own code never uses critical sections on a particular
object type, **CPython internals may use the critical section API on
any Python object**.

If your extension type needs its own lock, add a separate "PyMutex"
field (or another synchronization primitive) to your object struct.
"PyMutex" is very lightweight, so there is negligible cost to having
an additional one.


Construindo extensões para a construção com threads livres
==========================================================

As extensões da API C precisam ser construídas especificamente para a
construção com threads livres. As wheels, bibliotecas compartilhadas e
binários são indicados por um sufixo "t".

* pypa/manylinux supports the free-threaded build, with the "t"
  suffix, such as "python3.14t".

* pypa/cibuildwheel supports building wheels for the free-threaded
  build of Python 3.14 and newer.


API C limitada e ABI estável
----------------------------

A construção com threads livres não tem suporte atualmente à API C
limitada ou à ABI estável. Se você usar setuptools para construir sua
extensão e atualmente definir "py_limited_api=True", você pode usar
"py_limited_api=not sysconfig.get_config_var("Py_GIL_DISABLED")" para
não usar a API limitada ao construir com a construção com threads
livres.

Nota:

  Você precisará construir wheels separadas especificamente para a
  construção com threads livres. Se você usa atualmente a ABI estável,
  poderá continuar a construir uma única wheel para várias versões do
  Python sem threads livres.


Windows
-------

Devido a uma limitação do instalador oficial do Windows, você
precisará definir manualmente "Py_GIL_DISABLED=1" ao construir
extensões a partir do código-fonte.

Ver também:

  Portando módulos de extensão para oferecer suporte a threads livres
  (em inglês): Um guia de portabilidade mantido pela comunidade para
  autores de extensões.
