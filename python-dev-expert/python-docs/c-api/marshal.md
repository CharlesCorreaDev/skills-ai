Suporte a *marshalling* de dados
********************************

Essas rotinas permitem que o código C trabalhe com objetos
serializados usando o mesmo formato de dados que o módulo "marshal".
Existem funções para gravar dados no formato de serialização e funções
adicionais que podem ser usadas para ler os dados novamente. Os
arquivos usados para armazenar dados empacotados devem ser abertos no
modo binário.

Os valores numéricos são armazenados primeiro com o byte menos
significativo.

O módulo oferece suporte a várias versões do formato de dados;
consulte a "documentação do módulo Python" para obter detalhes.

Py_MARSHAL_VERSION

   A versão atual do formato. Veja "marshal.version".

void PyMarshal_WriteLongToFile(long value, FILE *file, int version)

   Aplica *marshalling* em um inteiro long, *value*, para *file*. Isso
   escreverá apenas os 32 bits menos significativos de *value*;
   independentemente do tamanho do tipo nativo long. *version* indica
   o formato do arquivo.

   Esta função pode falhar, caso em que define o indicador de erro.
   Use "PyErr_Occurred()" para verificar isso.

   Nota:

     No Python 3.15 e versões anteriores, esta função não define o
     indicador de erro caso a escrita em *file* falhe. Aplica-se a
     mesma ressalva válida para "PyMarshal_WriteObjectToFile()".

void PyMarshal_WriteObjectToFile(PyObject *value, FILE *file, int version)

   Aplica *marshalling* em um objeto Python, *value*, para *file*.
   *version* indica o formato do arquivo.

   Esta função pode falhar, caso em que define o indicador de erro.
   Use "PyErr_Occurred()" para verificar isso.

   Nota:

     No Python 3.15 e versões anteriores, esta função pode gravar
     apenas parte dos dados em *file* e retornar sem definir o
     indicador de erro — por exemplo, se *value* contiver um objeto
     que não possa ser serializado (*marshalled*) ou se a gravação em
     *file* falhar (veja gh-155907). Códigos que precisam oferecer
     suporte a essas versões não podem depender apenas de
     "PyErr_Occurred()" para verificar se todos os dados foram
     gravados. É possível utilizar "PyMarshal_WriteObjectToString()" e
     realizar a gravação do resultado por conta própria, ou validar o
     que foi efetivamente gravado.

PyObject *PyMarshal_WriteObjectToString(PyObject *value, int version)
    *Retorna valor: Nova referência.*

   Retorna um objeto de bytes que contém a representação
   pós-*marshalling* de *value*. *version* indica o formato do
   arquivo.

As seguintes funções permitem que os valores pós-*marshalling* sejam
lidos novamente.

long PyMarshal_ReadLongFromFile(FILE *file)

   Retorna um long C do fluxo de dados em um FILE* aberto para
   leitura. Somente um valor de 32 bits pode ser lido usando essa
   função, independentemente do tamanho nativo de long.

   Em caso de erro, define a exceção apropriada ("EOFError") e retorna
   "-1".

int PyMarshal_ReadShortFromFile(FILE *file)

   Retorna um short C do fluxo de dados em um FILE* aberto para
   leitura. Somente um valor de 16 bits pode ser lido usando essa
   função, independentemente do tamanho nativo de short.

   Em caso de erro, define a exceção apropriada ("EOFError") e retorna
   "-1".

PyObject *PyMarshal_ReadObjectFromFile(FILE *file)
    *Retorna valor: Nova referência.*

   Retorna um objeto Python do fluxo de dados em um FILE* aberto para
   leitura.

   Em caso de erro, define a exceção apropriada ("EOFError",
   "ValueError" ou "TypeError") e retorna "NULL".

PyObject *PyMarshal_ReadLastObjectFromFile(FILE *file)
    *Retorna valor: Nova referência.*

   Retorna um objeto Python do fluxo de dados em um FILE* aberto para
   leitura. Diferentemente de "PyMarshal_ReadObjectFromFile()", essa
   função presume que nenhum objeto adicional será lido do arquivo,
   permitindo que ela carregue agressivamente os dados do arquivo na
   memória, para que a desserialização possa operar a partir de dados
   na memória em vez de ler um byte por vez do arquivo. Use essa
   variante apenas se tiver certeza de que não estará lendo mais nada
   do arquivo.

   Em caso de erro, define a exceção apropriada ("EOFError",
   "ValueError" ou "TypeError") e retorna "NULL".

PyObject *PyMarshal_ReadObjectFromString(const char *data, Py_ssize_t len)
    *Retorna valor: Nova referência.*

   Retorna um objeto Python do fluxo de dados em um buffer de bytes
   contendo *len* bytes apontados por *data*.

   Em caso de erro, define a exceção apropriada ("EOFError",
   "ValueError" ou "TypeError") e retorna "NULL".
