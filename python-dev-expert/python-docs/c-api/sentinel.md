Objetos sentinel
****************

PyTypeObject PySentinel_Type

   Esta instância do "PyTypeObject" representa o tipo "sentinel" do
   Python. Este é o mesmo objeto que "sentinel".

   Adicionado na versão 3.15.

int PySentinel_Check(PyObject *o)

   Retorna verdadeiro se *o* for um objeto "sentinel" ou um subtipo. O
   tipo "sentinel" atualmente não permite subclasses, portanto, essa
   verificação é exata. Versões futuras do Python poderão permitir a
   criação de subtipos. Esta função sempre tem sucesso.

   Adicionado na versão 3.15.

int PySentinel_CheckExact(PyObject *o)

   Retorna verdadeiro se *o* for um objeto "sentinel", mas não um
   subtipo. O tipo "sentinel" atualmente não permite subclasses.
   Versões futuras do Python poderão permitir a criação de subtipos.
   Esta função sempre tem sucesso.

   Adicionado na versão 3.15.

PyObject *PySentinel_New(const char *name, const char *module_name, const char *repr)
    *Retorna valor: Nova referência.*

   Retorna um novo objeto "sentinel" com "__name__" definido como
   *name* e "__module__" definido como *module_name*. *nome* não deve
   ser "NULL". Se *module_name* for "NULL", "__module__" será definido
   como "None". Se *repr* for "NULL", "repr()" retornará "__name__".
   Retorna "NULL" com uma exceção definida em caso de falha.

   Para que a serialização com *pickle* funcione, *module_name* deve
   ser o nome de um módulo importável, e o *sentinel* deve estar
   acessível a partir desse módulo por meio de um caminho que
   corresponda a *name*. O *pickle* trata *name* como o nome de uma
   variável global em *module_name* (veja "object.__reduce__()").

   Adicionado na versão 3.15.
