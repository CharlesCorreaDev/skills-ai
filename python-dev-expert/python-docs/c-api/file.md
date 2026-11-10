File objects
************

Essas APIs são uma emulação mínima da API C do Python 2 para objetos
arquivo embutidos, que costumavam depender do suporte de E/S em buffer
(FILE*) da biblioteca C padrão. No Python 3, arquivos e streams usam o
novo módulo "io", que define várias camadas sobre a E/S sem buffer de
baixo nível do sistema operacional. As funções descritas a seguir são
invólucros de conveniência para o C sobre essas novas APIs e são
destinadas principalmente para relatórios de erros internos no
interpretador; código de terceiros é recomendado para acessar as APIs
de "io".

PyObject *PyFile_FromFd(int fd, const char *name, const char *mode, int buffering, const char *encoding, const char *errors, const char *newline, int closefd)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Cria um objeto arquivo Python a partir do descritor de arquivo de
   um arquivo já aberto *fd*. Os argumentos *name*, *encoding*,
   *errors* and *newline* podem ser "NULL" para usar os padrões;
   *buffering* pode ser *-1* para usar o padrão. *name* é ignorado e
   mantido para compatibilidade com versões anteriores. Retorna "NULL"
   em caso de falha. Para uma descrição mais abrangente dos
   argumentos, consulte a documentação da função "io.open()".

   Aviso:

     Como os streams do Python têm sua própria camada de buffer,
     combiná-los com os descritores de arquivo no nível do sistema
     operacional pode produzir vários problemas (como ordenação
     inesperada de dados).

   Alterado na versão 3.2: Ignora atributo *name*.

int PyObject_AsFileDescriptor(PyObject *p)
    * Parte da ABI Estável.*

   Retorna o descritor de arquivo associado a *p* como um int. Se o
   objeto for um inteiro, seu valor será retornado. Caso contrário, o
   método "fileno()" do objeto será chamado se existir; o método deve
   retornar um inteiro, que é retornado como o valor do descritor de
   arquivo. Define uma exceção e retorna "-1" em caso de falha.

PyObject *PyFile_GetLine(PyObject *p, int n)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Equivalente a "p.readline([n])", esta função lê uma linha do objeto
   *p*. *p* pode ser um objeto arquivo ou qualquer objeto com um
   método "readline()". Se *n* for "0", exatamente uma linha é lida,
   independentemente do comprimento da linha. Se *n* for maior que
   "0", não mais do que *n* bytes serão lidos do arquivo; uma linha
   parcial pode ser retornada. Em ambos os casos, uma string vazia é
   retornada se o final do arquivo for alcançado imediatamente. Se *n*
   for menor que "0", entretanto, uma linha é lida independentemente
   do comprimento, mas "EOFError" é levantada se o final do arquivo
   for alcançado imediatamente.

char *Py_UniversalNewlineFgets(char *buf, int n, FILE *stream, PyObject *fobj)

   Read a line from the C stream *stream* into the buffer *buf*, like
   the C standard library function "fgets()", but treating all of
   "\n", "\r" and "\r\n" as line endings (see *universal newlines*).
   Any "\r" or "\r\n" read from the stream is stored in *buf* as a
   single "\n".

   At most "n - 1" characters are stored in *buf*; reading stops after
   a newline has been stored or when the end of the file is reached.
   The result is always null-terminated. *stream* should be opened in
   binary mode, so that the C library does not perform its own newline
   translation.

   Return *buf* on success. Return "NULL" if no characters could be
   read, because *stream* is at end of file, a read error occurred, or
   *n* is less than 2. Like "fgets()", this function does not
   distinguish between end of file and a read error, and it does not
   set an exception.

   *fobj* exists only for backward compatibility and must be "NULL".

int PyFile_SetOpenCodeHook(Py_OpenCodeHookFunction handler)

   Substitui o comportamento normal de "io.open_code()" para passar
   seu parâmetro por meio do manipulador fornecido.

   O *handler* é uma função do tipo:

   typedef PyObject *(*Py_OpenCodeHookFunction)(PyObject*, void*)

      Equivalente de PyObject *(*)(PyObject *path, void *userData),
      sendo *path* garantido como sendo "PyUnicodeObject".

   O ponteiro *userData* é passado para a função de gancho. Como as
   funções de gancho podem ser chamadas de diferentes tempos de
   execução, esse ponteiro não deve se referir diretamente ao estado
   do Python.

   Como este gancho é usado intencionalmente durante a importação,
   evite importar novos módulos durante sua execução, a menos que eles
   estejam congelados ou disponíveis em "sys.modules".

   Uma vez que um gancho foi definido, ele não pode ser removido ou
   substituído, e chamadas posteriores para "PyFile_SetOpenCodeHook()"
   irão falhar. Em caso de falha, a função retorna -1 e define uma
   exceção se o interpretador foi inicializado.

   É seguro chamar esta função antes "Py_Initialize()".

   Levanta um evento de auditoria "setopencodehook" sem argumentos.

   Adicionado na versão 3.8.

PyObject *PyFile_OpenCodeObject(PyObject *path)

   Abre o arquivo *path* com o modo "'rb'". *path* deve ser um objeto
   Python da classe "str". O comportamento desta função pode ser
   substituído por "PyFile_SetOpenCodeHook()" para permitir algum
   pré-processamento do texto.

   Isso é análogo a "io.open_code()" no Python.

   Em caso de sucesso, esta função retorna uma *referência forte* a um
   objeto arquivo Python. Em caso de falha, esta função retorna "NULL"
   com uma exceção definida.

   Adicionado na versão 3.8.

PyObject *PyFile_OpenCode(const char *path)

   Semelhante a "PyFile_OpenCodeObject()", mas *path* é um const char*
   codificado em UTF-8.

   Adicionado na versão 3.8.

int PyFile_WriteObject(PyObject *obj, PyObject *p, int flags)
    * Parte da ABI Estável.*

   Write object *obj* to file object *p*.  The only supported flag for
   *flags* is "Py_PRINT_RAW"; if given, the "str()" of the object is
   written instead of the "repr()".

   If *obj* is "NULL", write the string ""<NULL>"".

   Return "0" on success or "-1" on failure; the appropriate exception
   will be set.

int PyFile_WriteString(const char *s, PyObject *p)
    * Parte da ABI Estável.*

   Escreve a string *s* no objeto arquivo *p*. Retorna "0" em caso de
   sucesso ou "-1" em caso de falha; a exceção apropriada será
   definida.


Soft-deprecated API
===================

These are APIs that were included in Python's C API by mistake. They
are documented solely for completeness; use other "PyFile*" APIs
instead.

PyObject *PyFile_NewStdPrinter(int fd)

   Use "PyFile_FromFd()" with defaults ("fd, NULL, "w", -1, NULL,
   NULL, NULL, 0") instead.

   Suavemente descontinuado desde a versão 3.15.

PyTypeObject PyStdPrinter_Type

   Type of file-like objects used internally at Python startup when
   "io" is not yet available. Use Python "open()" or "PyFile_FromFd()"
   to create file objects instead.

   Suavemente descontinuado desde a versão 3.15.

PY_STDIOTEXTMODE

   The string literal ""b"", used to open files in binary mode.
   Exposed for backwards compatibility only.

   Suavemente descontinuado desde a versão 3.15.2.
