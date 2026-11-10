Reflexão
********

PyObject *PyEval_GetBuiltins(void)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Descontinuado desde a versão 3.13: Use "PyEval_GetFrameBuiltins()".

   Retorna um dicionário dos componentes embutidos no quadro de
   execução atual ou o interpretador do estado da thread, se nenhum
   quadro estiver em execução no momento.

PyObject *PyEval_GetLocals(void)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Descontinuado desde a versão 3.13: Use "PyEval_GetFrameLocals()"
   para obter o mesmo comportamento que chamar "locals()" no código
   Python, ou então chame "PyFrame_GetLocals()" no resultado de
   "PyEval_GetFrame()" para acessar o atributo "f_locals" do quadro
   atualmente em execução.

   Retorna um mapeamento fornecendo acesso às variáveis locais no
   quadro de execução atual ou "NULL" se nenhum quadro estiver sendo
   executado no momento.

   Consulte "locals()" para detalhes do mapeamento retornado em
   diferentes escopos.

   Como esta função retorna uma *referência emprestada*, o dicionário
   retornado para *escopos otimizados* é armazenado em cache no objeto
   frame e permanecerá ativo enquanto o objeto frame o fizer. Ao
   contrário de "PyEval_GetFrameLocals()" e "locals()", chamadas
   subsequentes para esta função no mesmo quadro atualizarão o
   conteúdo do dicionário em cache para refletir as mudanças no estado
   das variáveis locais em vez de retornar um novo snapshot.

   Alterado na versão 3.13: Como parte da **PEP 667**,
   "PyFrame_GetLocals()", "locals()" e "FrameType.f_locals" não fazem
   mais uso do dicionário de cache compartilhado. Consulte a entrada
   de O Que Há de Novo para detalhes adicionais.

PyObject *PyEval_GetGlobals(void)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Descontinuado desde a versão 3.13: Use "PyEval_GetFrameGlobals()".

   Retorna um dicionário das variáveis globais no quadro de execução
   atual ou "NULL" se nenhum quadro estiver sendo executado no
   momento.

PyFrameObject *PyEval_GetFrame(void)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Retorna o quadro do *estado de thread anexado*, que é "NULL" se
   nenhum quadro estiver em execução no momento.

   Veja também "PyThreadState_GetFrame()".

PyObject *PyEval_GetFrameBuiltins(void)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.13.*

   Retorna um dicionário dos componentes embutidos no quadro de
   execução atual ou o interpretador do estado da thread, se nenhum
   quadro estiver em execução no momento.

   Adicionado na versão 3.13.

PyObject *PyEval_GetFrameLocals(void)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.13.*

   Retorna um dicionário das variáveis locais no quadro de execução
   atual ou "NULL" se nenhum quadro estiver sendo executado no
   momento. Equivalente a chamar "locals()" em código Python.

   Para acessar "f_locals" no quadro atual sem fazer um snapshot
   independente em *escopos otimizados*, chame "PyFrame_GetLocals()"
   no resultado de "PyEval_GetFrame()".

   Adicionado na versão 3.13.

PyObject *PyEval_GetFrameGlobals(void)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.13.*

   Retorna um dicionário das variáveis globais no quadro de execução
   atual ou "NULL" se nenhum quadro estiver sendo executado no
   momento. Equivalente a chamar "globals()" em código Python.

   Adicionado na versão 3.13.

const char *PyEval_GetFuncName(PyObject *func)
    * Parte da ABI Estável.*

   Retorna o nome de *func* se for uma função, classe ou objeto de
   instância, senão o nome do tipo da *func*.

   For a Python function or method, the returned pointer refers to the
   function's name and must not be retained across operations that may
   change that name. In the free-threaded build, copy the string
   before detaching the thread state or executing Python code if the
   name may be modified concurrently.

const char *PyEval_GetFuncDesc(PyObject *func)
    * Parte da ABI Estável.*

   Retorna uma sequência de caracteres de descrição, dependendo do
   tipo de *func*. Os valores de retorno incluem "()" para funções e
   métodos, " constructor", " instance" e " object".. Concatenado com
   o resultado de "PyEval_GetFuncName()", o resultado será uma
   descrição de *func*.
