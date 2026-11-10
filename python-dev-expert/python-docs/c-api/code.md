Objetos código
**************

Os objetos código são um detalhe de baixo nível da implementação do
CPython. Cada um representa um pedaço de código executável que ainda
não foi vinculado a uma função.

type PyCodeObject

   A estrutura C dos objetos usados para descrever objetos código. Os
   campos deste tipo estão sujeitos a alterações a qualquer momento.

PyTypeObject PyCode_Type

   Esta é uma instância de "PyTypeObject" representando o objeto
   código Python.

int PyCode_Check(PyObject *co)

   Retorna verdadeiro se *co* for um objeto código. Esta função sempre
   tem sucesso.

Py_ssize_t PyCode_GetNumFree(PyCodeObject *co)

   Retorna o número de *variáveis livres (de clausura)* em um objeto
   código.

int PyUnstable_Code_GetFirstFree(PyCodeObject *co)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Retorna a posição da primeira *variável livre (de clausura)* em um
   objeto código.

   Alterado na versão 3.13: Renomeado de "PyCode_GetFirstFree" como
   parte da API C Instável. O nome antigo foi descontinuado, mas
   continuará disponível até que a assinatura mude novamente.

PyCodeObject *PyUnstable_Code_New(int argcount, int kwonlyargcount, int nlocals, int stacksize, int flags, PyObject *code, PyObject *consts, PyObject *names, PyObject *varnames, PyObject *freevars, PyObject *cellvars, PyObject *filename, PyObject *name, PyObject *qualname, int firstlineno, PyObject *linetable, PyObject *exceptiontable)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Devolve um novo objeto código. Se precisar de um objeto código
   vazio para criar um quadro, use "PyCode_NewEmpty()"

   Como a definição de bytecode muda constantemente, chamar
   "PyUnstable_Code_New()" diretamente pode vinculá-lo a uma versão de
   Python específica.

   Os vários argumentos desta função são inter-dependentes de maneiras
   complexas, significando que mesmo alterações discretas de valor tem
   chances de resultar em execução incorreta ou erros fatais de VM.
   Tenha extremo cuidado ao usar esta função.

   Alterado na versão 3.11: Adicionou os parâmetros "qualname" e
   "exceptiontable"

   Alterado na versão 3.12: Renomeado de "PyCode_New" como parte da
   API C Instável. O nome antigo foi descontinuado, mas continuará
   disponível até que a assinatura mude novamente.

PyCodeObject *PyUnstable_Code_NewWithPosOnlyArgs(int argcount, int posonlyargcount, int kwonlyargcount, int nlocals, int stacksize, int flags, PyObject *code, PyObject *consts, PyObject *names, PyObject *varnames, PyObject *freevars, PyObject *cellvars, PyObject *filename, PyObject *name, PyObject *qualname, int firstlineno, PyObject *linetable, PyObject *exceptiontable)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Similar a "PyUnstable_Code_New()", mas com um "posonlyargcount"
   extra para argumentos somente-posicionais. As mesmas ressalvas que
   se aplicam a "PyUnstable_Code_New" também se aplicam a essa função.

   Adicionado na versão 3.8: Como "PyCode_NewWithPosOnlyArgs"

   Alterado na versão 3.11: Adicionados os parâmetros "qualname" e
   "exceptiontable"

   Alterado na versão 3.12: Renomeado para
   "PyUnstable_Code_NewWithPosOnlyArgs". O nome antigo foi
   descontinuado, mas continuará disponível até que a assinatura mude
   novamente.

PyCodeObject *PyCode_NewEmpty(const char *filename, const char *funcname, int firstlineno)
    *Retorna valor: Nova referência.*

   Retorna um novo objeto código vazio com o nome de arquivo, nome da
   função e número da primeira linha especificados. O objeto código
   resultante irá levantar uma "Exception" se executado.

int PyCode_Addr2Line(PyCodeObject *co, int byte_offset)

   Return the line number of the instruction that occurs on or before
   "byte_offset" and ends after it.  This may be "O(N)" in the number
   of instructions in the code object, so it is not performant for
   iterating over all the line numbers in a code object.

   If you just need the line number of a frame, use
   "PyFrame_GetLineNumber()" instead.

int PyCode_Addr2Location(PyObject *co, int byte_offset, int *start_line, int *start_column, int *end_line, int *end_column)

   Define os ponteiros "int" passados para a linha do código-fonte e
   os números da coluna para a instrução em "byte_offset". Define o
   valor como "0" quando as informações não estão disponíveis para
   nenhum elemento em particular.

   Retorna "1" se a função for bem-sucedida e 0 caso contrário.

   Adicionado na versão 3.11.

PyObject *PyCode_GetCode(PyCodeObject *co)

   Equivalente ao código Python "getattr(co, 'co_code')". Retorna uma
   referência forte a um "PyBytesObject" representando o bytecode em
   um objeto código. Em caso de erro, "NULL" é retornado e uma exceção
   é levantada.

   Este "PyBytesObject" pode ser criado sob demanda pelo interpretador
   e não representa necessariamente o bytecode realmente executado
   pelo CPython. O caso de uso primário para esta função são
   depuradores e criadores de perfil.

   Adicionado na versão 3.11.

PyObject *PyCode_GetVarnames(PyCodeObject *co)

   Equivalente ao código Python "getattr(co, 'co_varnames')". Retorna
   uma nova referência a um "PyTupleObject" contendo os nomes das
   variáveis locais. Em caso de erro, "NULL" é retornado e uma exceção
   é levantada.

   Adicionado na versão 3.11.

PyObject *PyCode_GetCellvars(PyCodeObject *co)

   Equivalente ao código Python "getattr(co, 'co_cellvars')". Retorna
   uma nova referência a um "PyTupleObject" contendo os nomes das
   variáveis locais referenciadas por funções aninhadas. Em caso de
   erro, "NULL" é retornado e uma exceção é levantada.

   Adicionado na versão 3.11.

PyObject *PyCode_GetFreevars(PyCodeObject *co)

   Equivalente ao código Python "getattr(co, 'co_freevars')". Retorna
   uma nova referência a um "PyTupleObject" contendo os nomes das
   *variáveis livres (de clausura)*. Em caso de erro, "NULL" é
   retornado e uma exceção é levantada.

   Adicionado na versão 3.11.

int PyCode_AddWatcher(PyCode_WatchCallback callback)

   Registra *callback* como um observador do objeto código para o
   interpretador atual.  Devolve um ID que pode ser passado para
   "PyCode_ClearWatcher()". Em caso de erro (por exemplo, não há IDs
   de observadores disponíveis), devolve "-1" e define uma exceção.

   Adicionado na versão 3.12.

int PyCode_ClearWatcher(int watcher_id)

   Libera o observador identificado por *watcher_id* anteriormente
   retornado por "PyCode_AddWatcher()" para o interpretador atual.
   Retorna "0" em caso de sucesso ou "-1" em caso de erro e levanta
   uma exceção (ex., se o *watcher_id* dado não foi registrado.)

   Adicionado na versão 3.12.

type PyCodeEvent

   Enumeração dos possíveis eventos de observador do objeto código:
   "PY_CODE_EVENT_CREATE" - "PY_CODE_EVENT_DESTROY"

   Adicionado na versão 3.12.

PY_FOREACH_CODE_EVENT(V)

   Apply the macro *V* to each suffix of "PyCodeEvent" constants.
   Currently expands to "V(CREATE) V(DESTROY)". The macro *V* must
   accept one event name and supply any punctuation needed between
   expansions.

typedef int (*PyCode_WatchCallback)(PyCodeEvent event, PyCodeObject *co)

   Tipo de uma função de callback de observador de objeto código.

   Se *evento* é "PY_CODE_EVENT_CREATE", então a função de retorno é
   invocada após *co* ter sido completamente inicializado. Senão, a
   função de retorno é invocada antes que a destruição de *co* ocorra,
   para que o estado anterior de *co* possa ser inspecionado.

   Se *evento* for "PY_CODE_EVENT_DESTROY", obter uma referência para
   a função de retorno do objeto-a-ser-destruído irá reativá-lo e
   impedirá que o objeto seja liberado. Quando o objeto reativado é
   posteriormente destruído, qualquer observador de funções de retorno
   ativos naquele momento serão chamados novamente.

   Usuários desta API não devem depender de detalhes internos de
   implementação em tempo de execução. Tais detalhes podem incluir,
   mas não estão limitados a: o ordem e o momento exatos da criação e
   destruição de objetos código. Enquanto alterações nestes detalhes
   podem resultar em diferenças que são visíveis para os observadores
   (incluindo se uma função de retorno é chamada ou não), isso não
   muda a semântica do código Python executado.

   Se a função de retorno definir uma exceção, ela deverá retornar
   "-1"; essa exceção será impressa como uma exceção não reprovável
   usando "PyErr_WriteUnraisable()". Caso contrário, deverá retornar
   "0".

   É possível que já exista uma exceção pendente definida na entrada
   da função de retorno. Nesse caso, a função de retorno deve retornar
   "0" com a mesma exceção ainda definida. Isso significa que a função
   de retorno não pode chamar nenhuma outra API que possa definir uma
   exceção, a menos que salve e limpe o estado da exceção primeiro e o
   restaure antes de retornar.

   Adicionado na versão 3.12.

PyObject *PyCode_Optimize(PyObject *code, PyObject *consts, PyObject *names, PyObject *lnotab_obj)

   Esta é uma função que faz nada.

   Antes do Python 3.10, essa função realizava otimizações básicas em
   um objeto código.

   Alterado na versão 3.10: Esta função agora não faz nada.

   Suavemente descontinuado desde a versão 3.13.


Sinalizadores de objetos código
*******************************

Objetos código contêm um campo de bits de sinalizadores, que podem ser
recuperados como o atributo Python "co_flags" (por exemplo, usando
"PyObject_GetAttrString()") e definidos usando um argumento *flags*
para "PyUnstable_Code_New()" e funções semelhantes.

Os sinalizadores cujos nomes começam com "CO_FUTURE_" correspondem a
recursos normalmente selecionáveis por instruções future. Esses
sinalizadores podem ser usados em "PyCompilerFlags.cf_flags". Observe
que muitos sinalizadores "CO_FUTURE_" são obrigatórios nas versões
atuais do Python, e defini-los não tem efeito.

Os seguintes sinalizador estão disponíveis. Para saber o significado
delas, consulte a documentação vinculada de seus equivalentes em
Python.

+----------------------------------------------------+----------------------------------------------------+
| Sinalizador                                        | Significado                                        |
|====================================================|====================================================|
| CO_OPTIMIZED                                       | "inspect.CO_OPTIMIZED"                             |
+----------------------------------------------------+----------------------------------------------------+
| CO_NEWLOCALS                                       | "inspect.CO_NEWLOCALS"                             |
+----------------------------------------------------+----------------------------------------------------+
| CO_VARARGS                                         | "inspect.CO_VARARGS"                               |
+----------------------------------------------------+----------------------------------------------------+
| CO_VARKEYWORDS                                     | "inspect.CO_VARKEYWORDS"                           |
+----------------------------------------------------+----------------------------------------------------+
| CO_NESTED                                          | "inspect.CO_NESTED"                                |
+----------------------------------------------------+----------------------------------------------------+
| CO_GENERATOR                                       | "inspect.CO_GENERATOR"                             |
+----------------------------------------------------+----------------------------------------------------+
| CO_COROUTINE                                       | "inspect.CO_COROUTINE"                             |
+----------------------------------------------------+----------------------------------------------------+
| CO_ITERABLE_COROUTINE                              | "inspect.CO_ITERABLE_COROUTINE"                    |
+----------------------------------------------------+----------------------------------------------------+
| CO_ASYNC_GENERATOR                                 | "inspect.CO_ASYNC_GENERATOR"                       |
+----------------------------------------------------+----------------------------------------------------+
| CO_HAS_DOCSTRING                                   | "inspect.CO_HAS_DOCSTRING"                         |
+----------------------------------------------------+----------------------------------------------------+
| CO_METHOD                                          | "inspect.CO_METHOD"                                |
+----------------------------------------------------+----------------------------------------------------+
| CO_FUTURE_DIVISION                                 | sem efeito ("__future__.division")                 |
+----------------------------------------------------+----------------------------------------------------+
| CO_FUTURE_ABSOLUTE_IMPORT                          | sem efeito ("__future__.absolute_import")          |
+----------------------------------------------------+----------------------------------------------------+
| CO_FUTURE_WITH_STATEMENT                           | sem efeito ("__future__.with_statement")           |
+----------------------------------------------------+----------------------------------------------------+
| CO_FUTURE_PRINT_FUNCTION                           | sem efeito ("__future__.print_function")           |
+----------------------------------------------------+----------------------------------------------------+
| CO_FUTURE_UNICODE_LITERALS                         | sem efeito ("__future__.unicode_literals")         |
+----------------------------------------------------+----------------------------------------------------+
| CO_FUTURE_GENERATOR_STOP                           | sem efeito ("__future__.generator_stop")           |
+----------------------------------------------------+----------------------------------------------------+
| CO_FUTURE_ANNOTATIONS                              | "__future__.annotations"                           |
+----------------------------------------------------+----------------------------------------------------+


Informação adicional
********************

Para oferece suporte a extensões de baixo nível de avaliação de quadro
(frame), tais como compiladores "just-in-time", é possível anexar
dados arbitrários adicionais a objetos código.

Estas funções são parte da camada instável da API C: Essa
funcionalidade é um detalhe de implementação do CPython, e a API pode
mudar sem avisos de descontinuidade.

Py_ssize_t PyUnstable_Eval_RequestCodeExtraIndex(freefunc free)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Retorna um novo e opaco valor de índice usado para adicionar dados
   a objetos código.

   You generally call this function once (per interpreter). Use the
   result with "PyUnstable_Code_GetExtra()" and
   "PyUnstable_Code_SetExtra()" to manipulate data on individual code
   objects.

   Se *free* não for "NULL": quando o objeto código é desalocado,
   *free* será chamado em dados não-"NULL" armazenados sob o novo
   índice. Use "Py_DecRef()" quando armazenar "PyObject".

   Adicionado na versão 3.6: como "_PyEval_RequestCodeExtraIndex"

   Alterado na versão 3.12: Renomeado para
   "PyUnstable_Eval_RequestCodeExtraIndex". O nome antigo nome privado
   foi descontinuado, mas continuará disponível até a mudança da API.

int PyUnstable_Code_GetExtra(PyObject *code, Py_ssize_t index, void **extra)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Define *extra* para os dados adicionais armazenados sob o novo
   índice dado. Retorna 0 em caso de sucesso. Define uma exceção e
   retorna -1 em caso de erro.

   Se nenhum dado foi determinado sob o índice, define *extra* como
   "NULL" e retorna 0 sem definir nenhuma exceção.

   Adicionado na versão 3.6: como "_PyCode_GetExtra"

   Alterado na versão 3.12: Renomeado para "PyUnstable_Code_GetExtra".
   O nome antigo privado foi descontinuado, mas continuará disponível
   até a mudança da API.

int PyUnstable_Code_SetExtra(PyObject *code, Py_ssize_t index, void *extra)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Define os dados extras armazenados sob o índice dado a *extra*.
   Retorna 0 em caso de sucesso. Define uma exceção e retorna -1 em
   caso de erro.

   Adicionado na versão 3.6: como "_PyCode_SetExtra"

   Alterado na versão 3.12: Renomeado para "PyUnstable_Code_SetExtra".
   O nome antigo privado foi descontinuado, mas continuará disponível
   até a mudança da API.
