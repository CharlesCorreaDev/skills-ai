Objeto célula
*************

Objetos "cell" são usados para implementar variáveis referenciadas por
múltiplos escopos. Para cada variável, um objeto célula é criado para
armazenar o valor; as variáveis locais de cada quadro de pilha que
referencia o valor contêm uma referência para as células de escopos
externos que também usam essa variável. Quando o valor é acessado, o
valor contido na célula é usado em vez do próprio objeto da célula.
Essa des-referência do objeto da célula requer suporte do código de
bytes gerado; estes não são automaticamente desprezados quando
acessados. Objetos de células provavelmente não serão úteis em outro
lugar.

type PyCellObject

   A estrutura C usada para objetos célula.

PyTypeObject PyCell_Type

   O objeto de tipo correspondente aos objetos célula.

int PyCell_Check(PyObject *ob)

   Retorna verdadeiro se *ob* for um objeto célula; *ob* não deve ser
   "NULL". Esta função sempre tem sucesso.

PyObject *PyCell_New(PyObject *ob)
    *Retorna valor: Nova referência.*

   Cria e retorna um novo objeto célula contendo o valor *ob*. O
   parâmetro pode ser "NULL".

PyObject *PyCell_Get(PyObject *cell)
    *Retorna valor: Nova referência.*

   Retorna o conteúdo da célula *cell*, que pode ser "NULL". Se *cell*
   não for um objeto célula, retorna "NULL" com um conjunto de
   exceções.

PyObject *PyCell_GET(PyObject *cell)
    *Retorna valor: Referência emprestada.*

   Retorna o conteúdo da célula *cell*, mas sem verificar se *cell*
   não é "NULL" e um objeto célula.

int PyCell_Set(PyObject *cell, PyObject *value)

   Define o conteúdo do objeto da célula *cell* como *value*. Isso
   libera a referência a qualquer conteúdo atual da célula. *value*
   pode ser "NULL". *cell* não pode ser "NULL".

   Em caso de sucesso, retorna "0". Se *cell* não for um objeto
   célula, define uma exceção e retorna "-1".

void PyCell_SET(PyObject *cell, PyObject *value)

   Define o valor do objeto da célula *cell* como *value*. Nenhuma
   contagem de referência é ajustada e nenhuma verificação é feita
   quanto à segurança; *cell* não pode ser "NULL" e deve ser um objeto
   célula.
