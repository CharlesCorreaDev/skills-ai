Objeto tupla
************

type PyTupleObject

   Este subtipo de "PyObject" representa um objeto tupla em Python.

PyTypeObject PyTuple_Type
    * Parte da ABI Estável.*

   Esta instância de "PyTypeObject" representa o tipo tupla de Python;
   é o mesmo objeto que "tuple" na camada Python.

int PyTuple_Check(PyObject *p)

   Retorna verdadeiro se *p* é um objeto tupla ou uma instância de um
   subtipo do tipo tupla. Esta função sempre tem sucesso.

int PyTuple_CheckExact(PyObject *p)

   Retorna verdadeiro se *p* é um objeto tupla, mas não uma instância
   de um subtipo do tipo tupla. Esta função sempre tem sucesso.

PyObject *PyTuple_New(Py_ssize_t len)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um novo objeto tupla de tamanho *len*, ou "NULL" com uma
   exceção definida em caso de falha.

PyObject *PyTuple_FromArray(PyObject *const *array, Py_ssize_t size)
    * Thread safety: Atomic.*

   Create a tuple of *size* items and copy references from *array* to
   the new tuple.

   *array* can be NULL if *size* is "0".

   On success, return a new reference. On error, set an exception and
   return "NULL".

   Adicionado na versão 3.15.

PyObject *PyTuple_Pack(Py_ssize_t n, ...)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna um novo objeto tupla de tamanho *n*, ou "NULL" com uma
   exceção em caso de falha. Os valores da tupla são inicializados
   para os *n* argumentos C subsequentes apontando para objetos
   Python. "`PyTuple_Pack(2, a, b)" é equivalente a
   "Py_BuildValue("(OO)", a, b)".

Py_ssize_t PyTuple_Size(PyObject *p)
    * Parte da ABI Estável.** Thread safety: Atomic.*

   Pega um ponteiro para um objeto tupla e retorna o tamanho dessa
   tupla. No erro, retorna "-1" com uma exceção definida.

Py_ssize_t PyTuple_GET_SIZE(PyObject *p)
    * Thread safety: Atomic.*

   Como "PyTuple_Size()", mas sem verificação de erro.

PyObject *PyTuple_GetItem(PyObject *p, Py_ssize_t pos)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Retorna o objeto na posição *pos* na tupla apontada por *p*. Se
   *pos* estiver fora dos limites, retorna "NULL" e define uma exceção
   "IndexError".

   A referência retornada é emprestada da tupla *p* (ou seja: ela só é
   válida enquanto você mantém uma referência a *p*). Para obter uma
   *referência forte*, use "Py_NewRef(PyTuple_GetItem(...))" ou
   "PySequence_GetItem()".

PyObject *PyTuple_GET_ITEM(PyObject *p, Py_ssize_t pos)
    *Retorna valor: Referência emprestada.** Thread safety: Safe to
   call from multiple threads with external synchronization only.*

   Como "PyTuple_GetItem()", mas faz nenhuma verificação de seus
   argumentos.

PyObject *PyTuple_GetSlice(PyObject *p, Py_ssize_t low, Py_ssize_t high)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Retorna a fatia da tupla apontada por *p* entre *low* e *high*, ou
   "NULL" com uma exceção definida em caso de falha.

   Isso é o equivalente da expressão Python "p[low:high]". A indexação
   do final da tupla não é suportada.

int PyTuple_SetItem(PyObject *p, Py_ssize_t pos, PyObject *o)
    * Parte da ABI Estável.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Insert a reference to object *o* at position *pos* of the tuple
   pointed to by *p*.  Return "0" on success.  If *pos* is out of
   bounds, return "-1" and set an "IndexError" exception. This
   function should only be used to fill in brand new tuples; using it
   on an existing tuple is thread-unsafe.

   Nota:

     This function "*steals*" a reference to *o* and discards a
     reference to an item already in the tuple at the affected
     position (unless it was NULL).

void PyTuple_SET_ITEM(PyObject *p, Py_ssize_t pos, PyObject *o)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Like "PyTuple_SetItem()", but does no error checking, and should
   *only* be used to fill in brand new tuples, using it on an existing
   tuple is thread-unsafe.

   A verificação de limites é realizada como uma asserção se o Python
   for construído em modo de depuração ou "com asserções".

   Nota:

     This function "*steals*" a reference to *o*, and, unlike
     "PyTuple_SetItem()", does *not* discard a reference to any item
     that is being replaced; any reference in the tuple at position
     *pos* will be leaked.

   Aviso:

     Esta macro deve ser usada *somente* em tuplas recém-criadas. Usar
     esta macro em uma tupla que já está em uso (ou, em outras
     palavras, com uma contagem de referências > 1) pode levar a um
     comportamento indefinido.

int _PyTuple_Resize(PyObject **p, Py_ssize_t newsize)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Pode ser usado para redimensionar uma tupla. *newsize* será o novo
   comprimento da tupla. Como as tuplas são *supostamente* imutáveis,
   isso só deve ser usado se houver apenas uma referência ao objeto.
   *Não* use isto se a tupla já for conhecida por alguma outra parte
   do código. A tupla sempre aumentará ou diminuirá no final. Pense
   nisso como destruir a tupla antiga e criar uma nova, mas com mais
   eficiência. Retorna "0" em caso de sucesso. O código do cliente
   nunca deve presumir que o valor resultante de "*p" será o mesmo de
   antes de chamar esta função. Se o objeto referenciado por "*p" for
   substituído, o "*p" original será destruído. Em caso de falha,
   retorna "-1" e define "*p" para "NULL", e levanta "MemoryError" ou
   "SystemError".


Objetos sequência de estrutura
******************************

A struct sequence object is a *named tuple*, that is, a sequence whose
items can also be accessed through attributes. It is similar to
"collections.namedtuple()", but provides a slightly different
interface.

To create a struct sequence, you first have to create a specific
struct sequence type.

PyTypeObject *PyStructSequence_NewType(PyStructSequence_Desc *desc)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Cria um novo tipo de sequência de estrutura a partir dos dados em
   *desc*, descrito abaixo. Instâncias do tipo resultante podem ser
   criadas com "PyStructSequence_New()".

   Retorna "NULL" com uma exceção definida em caso de falha.

void PyStructSequence_InitType(PyTypeObject *type, PyStructSequence_Desc *desc)
    * Thread safety: Safe to call without external synchronization on
   distinct objects.*

   Inicializa um tipo de sequência de estrutura *type* de *desc* no
   lugar.

int PyStructSequence_InitType2(PyTypeObject *type, PyStructSequence_Desc *desc)
    * Thread safety: Safe to call without external synchronization on
   distinct objects.*

   Como "PyStructSequence_InitType()", mas retorna "0" em caso de
   sucesso e "-1" com uma exceção definida em caso de falha.

   Adicionado na versão 3.4.

type PyStructSequence_Desc
    * Parte da ABI Estável (incluindo todos os membros).*

   Contém as metainformações de um tipo de sequência de estrutura a
   ser criado.

   const char *name

      Nome totalmente qualificado do tipo; codificado em UTF-8
      terminado em nulo. O nome deve conter o nome do módulo.

   const char *doc

      Ponteiro para docstring para o tipo ou "NULL" para omitir

   PyStructSequence_Field *fields

      Ponteiro para um vetor terminado em "NULL" com nomes de campos
      do novo tipo

   int n_in_sequence

      Número de campos visíveis para o lado Python (se usado como
      tupla)

type PyStructSequence_Field
    * Parte da ABI Estável (incluindo todos os membros).*

   Descreve um campo de uma sequência de estrutura. Como uma sequência
   de estrutura é modelada como uma tupla, todos os campos são
   digitados como PyObject*. O índice no vetor "fields" do
   "PyStructSequence_Desc" determina qual campo da sequência de
   estrutura é descrito.

   const char *name

      Nome do campo ou "NULL" para terminar a lista de campos
      nomeados; definida para "PyStructSequence_UnnamedField" para
      deixar sem nome.

   const char *doc

      Campo docstring ou "NULL" para omitir.

const char *const PyStructSequence_UnnamedField
    * Parte da ABI Estável desde a versão 3.11.*

   Valor especial para um nome de campo para deixá-lo sem nome.

   Alterado na versão 3.9: O tipo foi alterado de "char *".

PyObject *PyStructSequence_New(PyTypeObject *type)
    *Retorna valor: Nova referência.** Parte da ABI Estável.** Thread
   safety: Atomic.*

   Cria um instância de *type*, que deve ser criada com
   "PyStructSequence_NewType()".

   Retorna "NULL" com uma exceção definida em caso de falha.

PyObject *PyStructSequence_GetItem(PyObject *p, Py_ssize_t pos)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.**
   Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Return the object at position *pos* in the struct sequence pointed
   to by *p*. The returned reference is borrowed from the struct
   sequence *p* (that is: it is only valid as long as you hold a
   reference to *p*).

   A verificação de limites é realizada como uma asserção se o Python
   for construído em modo de depuração ou "com asserções".

PyObject *PyStructSequence_GET_ITEM(PyObject *p, Py_ssize_t pos)
    *Retorna valor: Referência emprestada.** Thread safety: Safe to
   call from multiple threads with external synchronization only.*

   Apelido para "PyStructSequence_GetItem()".

   Alterado na versão 3.13: Agora implementada como um apelido para
   "PyStructSequence_GetItem()".

void PyStructSequence_SetItem(PyObject *p, Py_ssize_t pos, PyObject *o)
    * Parte da ABI Estável.** Thread safety: Safe to call from
   multiple threads with external synchronization only.*

   Define o campo no índice *pos* da sequência de estrutura *p* para o
   valor *o*. Como "PyTuple_SET_ITEM()", isto só deve ser usado para
   preencher novas instâncias.

   A verificação de limites é realizada como uma asserção se o Python
   for construído em modo de depuração ou "com asserções".

   Nota:

     This function "*steals*" a reference to *o*.

void PyStructSequence_SET_ITEM(PyObject *p, Py_ssize_t *pos, PyObject *o)
    * Thread safety: Safe to call from multiple threads with external
   synchronization only.*

   Apelido para "PyStructSequence_SetItem()".

   Alterado na versão 3.13: Agora implementada como um apelido para
   "PyStructSequence_SetItem()".
