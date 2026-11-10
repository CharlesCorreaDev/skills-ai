Alocando objetos na heap
************************

PyObject *_PyObject_New(PyTypeObject *type)
    *Retorna valor: Nova referência.*

PyVarObject *_PyObject_NewVar(PyTypeObject *type, Py_ssize_t size)
    *Retorna valor: Nova referência.*

PyObject *PyObject_Init(PyObject *op, PyTypeObject *type)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Inicializa um objeto *op* recém-alocado com seu tipo e referência
   inicial. Retorna o objeto inicializado. Outros campos do objeto não
   são inicializados. Apesar do nome, esta função não tem relação com
   o método "__init__()" do objeto (slot "tp_init"). Especificamente,
   esta função **não** chama o método "__init__()" do objeto.

   Em geral, considere esta função como uma rotina de baixo nível. Use
   "tp_alloc" sempre que possível. Para implementar "tp_alloc" para o
   seu tipo, prefira "PyType_GenericAlloc()" ou "PyObject_New()".

   Nota:

     Esta função inicializa apenas a memória do objeto correspondente
     à estrutura inicial "PyObject". Não zera o restante.

PyVarObject *PyObject_InitVar(PyVarObject *op, PyTypeObject *type, Py_ssize_t size)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Isto faz tudo que o "PyObject_Init()" faz e também inicializa a
   informação de comprimento para um objeto de tamanho variável.

   Nota:

     Esta função inicializa apenas parte da memória do objeto. Não
     zera o restante.

PyObject_New(TYPE, typeobj)

   Aloca um novo objeto Python usando o tipo de estrutura C *TYPE* e o
   objeto de tipo Python *typeobj* ("PyTypeObject*") chamando
   "PyObject_Malloc()" para alocar memória e inicializando-o como
   "PyObject_Init()". O chamador possuirá a única referência ao objeto
   (ou seja, sua contagem de referências será um).

   Evite chamar isso diretamente para alocar memória para um objeto;
   em vez disso, chame o slot "tp_alloc" do tipo.

   Ao preencher o slot "tp_alloc" de um tipo, "PyType_GenericAlloc()"
   é preferível a uma função personalizada que simplesmente chama esta
   macro.

   Esta macro não chama "tp_alloc", "tp_new" ("__new__()") ou
   "tp_init" ("__init__()").

   Isso não pode ser usado para objetos com "Py_TPFLAGS_HAVE_GC"
   definido em "tp_flags"; use "PyObject_GC_New" em vez disso.

   A memória alocada por esta macro deve ser liberada com
   "PyObject_Free()" (geralmente chamado por meio do slot "tp_free" do
   objeto).

   Nota:

     Não há garantia de que a memória retornada tenha sido
     completamente zerada antes de ser inicializada.

   Nota:

     Esta macro não constrói um objeto totalmente inicializado do tipo
     fornecido; ela apenas aloca memória e a prepara para
     inicialização posterior por "tp_init". Para construir um objeto
     totalmente inicializado, chame *typeobj*. Por exemplo:

        PyObject *foo = PyObject_CallNoArgs((PyObject *)&PyFoo_Type);

   Ver também:

     * "PyObject_Free()"

     * "PyObject_GC_New"

     * "PyType_GenericAlloc()"

     * "tp_alloc"

PyObject_NewVar(TYPE, typeobj, size)

   Como "PyObject_New", exceto que:

   * Ela aloca memória suficiente para a estrutura *TYPE* mais os
     *size* ("Py_ssize_t") campos do tamanho fornecido pelo campo
     "tp_itemsize" de *typeobj*.

   * A memória é inicializada como "PyObject_InitVar()".

   Isso é útil para implementar objetos como tuplas, que conseguem
   determinar seu tamanho em tempo de construção. Incorporar o vetor
   de campos na mesma alocação diminui o número de alocações,
   melhorando a eficiência do gerenciamento de memória.

   Evite chamar isso diretamente para alocar memória para um objeto;
   em vez disso, chame o slot "tp_alloc" do tipo.

   Ao preencher o slot "tp_alloc" de um tipo, "PyType_GenericAlloc()"
   é preferível a uma função personalizada que simplesmente chama esta
   macro.

   Isso não pode ser usado para objetos com "Py_TPFLAGS_HAVE_GC"
   definido em "tp_flags"; use "PyObject_GC_NewVar" em vez disso.

   A memória alocada por esta função deve ser liberada com
   "PyObject_Free()" (geralmente chamado por meio do slot "tp_free" do
   objeto).

   Nota:

     Não há garantia de que a memória retornada tenha sido
     completamente zerada antes de ser inicializada.

   Nota:

     Esta macro não constrói um objeto totalmente inicializado do tipo
     fornecido; ela apenas aloca memória e a prepara para
     inicialização posterior por "tp_init". Para construir um objeto
     totalmente inicializado, chame *typeobj*. Por exemplo:

        PyObject *list_instance = PyObject_CallNoArgs((PyObject *)&PyList_Type);

   Ver também:

     * "PyObject_Free()"

     * "PyObject_GC_NewVar"

     * "PyType_GenericAlloc()"

     * "tp_alloc"

PyObject _Py_NoneStruct

   Objeto o qual é visível no Python como "None". Isto só deve ser
   acessado usando a macro "Py_None", o qual avalia como um ponteiro
   para este objeto.

Ver também:

  Objetos do Módulo
     Para alocar e criar módulos de extensão.


Apelidos suavemente descontinuados
==================================

Suavemente descontinuado desde a versão 3.15.

Esses são apelidos para funções e macros existentes. Eles existem
unicamente para fins de retrocompatibilidade.

+----------------------------------------------------+----------------------------------------------------+
| Apelido suavemente descontinuado                   | Função                                             |
|====================================================|====================================================|
| PyObject_NEW(type, typeobj)                        | "PyObject_New"                                     |
+----------------------------------------------------+----------------------------------------------------+
| PyObject_NEW_VAR(type, typeobj, n)                 | "PyObject_NewVar"                                  |
+----------------------------------------------------+----------------------------------------------------+
| PyObject_INIT(op, typeobj)                         | "PyObject_Init()"                                  |
+----------------------------------------------------+----------------------------------------------------+
| PyObject_INIT_VAR(op, typeobj, n)                  | "PyObject_InitVar()"                               |
+----------------------------------------------------+----------------------------------------------------+
| PyObject_MALLOC(n)                                 | "PyObject_Malloc()"                                |
+----------------------------------------------------+----------------------------------------------------+
| PyObject_REALLOC(p, n)                             | "PyObject_Realloc()"                               |
+----------------------------------------------------+----------------------------------------------------+
| PyObject_FREE(p)                                   | "PyObject_Free()"                                  |
+----------------------------------------------------+----------------------------------------------------+
| PyObject_DEL(p)                                    | "PyObject_Free()"                                  |
+----------------------------------------------------+----------------------------------------------------+
| PyObject_Del(p)                                    | "PyObject_Free()"                                  |
+----------------------------------------------------+----------------------------------------------------+
