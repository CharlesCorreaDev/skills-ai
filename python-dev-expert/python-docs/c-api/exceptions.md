Tratamento de exceções
**********************

As funções descritas nesse capítulo permitem você tratar e gerar
exceções em Python. É importante entender alguns princípios básicos no
tratamento de exceções no Python. Funciona de forma parecida com a
variável POSIX "errno": existe um indicador global (por thread) do
último erro ocorrido. A maioria das funções da API C não o zera ao
obter sucesso, mas o define para indicar a causa do erro ao falhar. A
maioria das funções da API retorna um indicador de erro, geralmente,
"NULL" se eles devem retornar um ponteiro, ou "-1" se retornarem um
inteiro (exceção: as funções "PyArg_*" retornam "1" para sucesso e "0"
para falha).

De forma concreta, o indicador de erro consiste em três ponteiros de
objeto: o tipo da exceção, o valor da exceção e o objeto de traceback.
Qualquer um desses ponteiros pode ser "NULL" se não definido (embora
algumas combinações sejam proibidas, por exemplo, você não pode ter um
retorno não "NULL" se o tipo de exceção for "NULL").

Quando uma função deve falhar porque devido à falha de alguma função
que ela chamou, ela geralmente não define o indicador de erro; a
função que ela chamou já o definiu. Ela é responsável por manipular o
erro e limpar a exceção ou retornar após limpar todos os recursos que
possui (como referências a objetos ou alocações de memória); ela *não*
deve continuar normalmente se não estiver preparada para lidar com o
erro. Se estiver retornando devido a um erro, é importante indicar ao
chamador que um erro foi definido. Se o erro não for manipulado ou
propagado com cuidado, chamadas adicionais para a API Python/C podem
não se comportar conforme o esperado e podem falhar de maneiras
misteriosas.

Nota:

  O indicador de erro **não** é resultado de "sys.exc_info()". O
  primeiro corresponde a uma exceção que ainda não foi capturada (e,
  portanto, ainda está se propagando), enquanto o segundo retorna uma
  exceção após ser capturada (e, portanto, parou de se propagar).


Impressão e limpeza
===================

void PyErr_Clear()
    * Parte da ABI Estável.*

   Limpe o indicador de erro. Se o indicador de erro não estiver
   definido, não haverá efeito.

void PyErr_PrintEx(int set_sys_last_vars)
    * Parte da ABI Estável.*

   Exibe um traceback padrão para "sys.stderr" e limpe o indicador de
   erro. **A menos que** o erro seja um "SystemExit", nesse caso,
   nenhum traceback será impresso e o processo Python será encerrado
   com o código de erro especificado pela instância "SystemExit".

   Chame esta função **apenas** quando o indicador de erro estiver
   definido. Caso contrário, causará um erro fatal!

   Se *set_sys_last_vars* for diferente de zero, a variável
   "sys.last_exc" será definida com a exceção exibida. Para manter a
   retrocompatibilidade, as variáveis descontinuadas "sys.last_type",
   "sys.last_value" e "sys.last_traceback" também serão definidas com
   o tipo, valor e traceback dessa exceção, respectivamente.

   Alterado na versão 3.12: A configuração de "sys.last_exc" foi
   adicionada.

void PyErr_Print()
    * Parte da ABI Estável.*

   Apelido para "PyErr_PrintEx(1)".

void PyErr_WriteUnraisable(PyObject *obj)
    * Parte da ABI Estável.*

   Chama "sys.unraisablehook()" usando a exceção atual e o argumento
   *obj*.

   Esta função utilitária imprime uma mensagem de aviso para
   "sys.stderr" quando uma exceção foi definida, mas é impossível para
   o interpretador realmente gerar a exceção. É usada, por exemplo,
   quando ocorre uma exceção em um método "__del__()".

   A função é chamada com um único argumento *obj* que identifica o
   contexto em que ocorreu a exceção não gerável. Se possível, o repr
   de *obj* será impresso na mensagem de aviso. Se *obj* for "NULL",
   apenas o traceback será impresso.

   Uma exceção deve ser definida ao chamar essa função.

   Alterado na versão 3.4: Exibe o traceback (situação da pilha de
   execução). Exibe apenas o traceback se *obj* for "NULL".

   Alterado na versão 3.8: Utiliza "sys.unraisablehook()".

void PyErr_FormatUnraisable(const char *format, ...)

   Similar a "PyErr_WriteUnraisable()", mas *format* e parâmetros
   subsequentes ajudam a formatar a mensagem de aviso; eles têm o
   mesmo significado e valores que em "PyUnicode_FromFormat()".
   "PyErr_WriteUnraisable(obj)" é aproximadamente equivalente à
   "PyErr_FormatUnraisable("Exception ignored in: %R", obj)". Se
   *format* é "NULL", somente o rastreamento é impresso.

   Adicionado na versão 3.13.

void PyErr_DisplayException(PyObject *exc)
    * Parte da ABI Estável desde a versão 3.12.*

   Imprime a exibição padrão do traceback de "exc" em "sys.stderr",
   incluindo as exceções encadeadas e notas.

   Adicionado na versão 3.12.

void PyErr_Display(PyObject *unused, PyObject *value, PyObject *tb)
    * Parte da ABI Estável.*

   Legacy variant of "PyErr_DisplayException()".

   Print the exception *value* with its traceback to "sys.stderr". If
   *value* has no traceback set, *tb* is used as its traceback. The
   first argument is ignored.

   If "sys.stderr" is "None", nothing is printed. If "sys.stderr" is
   not set, the exception is dumped to the C "stderr" stream instead.

   Descontinuado desde a versão 3.12: Use "PyErr_DisplayException()"
   instead.


Levantando exceções
===================

Essas funções ajudam a definir o indicador de erro do thread. Por
conveniência, algumas dessas funções sempre retornam um ponteiro
"NULL" ao usar instrução com "return".

void PyErr_SetString(PyObject *type, const char *message)
    * Parte da ABI Estável.*

   Esse é o modo mais comum de definir o indicador de erro. O primeiro
   argumento especifica o tipo da exceção; é normalmente uma das
   exceções padrão, como "PyExc_RuntimeError".  Você não precisa criar
   um novo *strong reference* para ela (como em "Py_INCREF()"). O
   segundo argumento é uma mensagem de erro; ela é codificada com
   "'utf-8'".

void PyErr_SetObject(PyObject *type, PyObject *value)
    * Parte da ABI Estável.*

   Essa função é semelhante à "PyErr_SetString()" mas permite
   especificar um objeto Python arbitrário para o valor da exceção.

PyObject *PyErr_Format(PyObject *exception, const char *format, ...)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável.*

   Essa função define o indicador de erro e retorna "NULL".
   *exception* deve ser uma classe Python de exceção. O *format* e
   parâmetros subsequentes ajudam a formatar a mensagem de erro; eles
   têm o mesmo significado e valores que em "PyUnicode_FromFormat()".
   *format* é uma string codificada em ASCII.

PyObject *PyErr_FormatV(PyObject *exception, const char *format, va_list vargs)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável desde a versão
   3.5.*

   Igual a "PyErr_Format()", mas usando o argumento "va_list" em vez
   de um número variável de argumentos.

   Adicionado na versão 3.5.

void PyErr_SetNone(PyObject *type)
    * Parte da ABI Estável.*

   Isso é uma abreviação para "PyErr_SetObject(type, Py_None)".

int PyErr_BadArgument()
    * Parte da ABI Estável.*

   Essa é uma abreviação de "PyErr_SetString(PyExc_TypeError,
   message)", na qual *message* indica que uma operação embutida foi
   invocada com um argumento ilegal. Ela é principalmente para uso
   interno.

PyObject *PyErr_NoMemory()
    *Retorna valor: Sempre NULL.** Parte da ABI Estável.*

   Essa é uma abreviação para "PyErr_SetNone(PyExc_MemoryError)"; que
   retorna "NULL"  para que uma função de alocação de objeto possa
   escrever "return PyErr_NoMemory();"  quando ficar sem memória.

PyObject *PyErr_SetFromErrno(PyObject *type)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável.*

   Esta é uma função conveniente para levantar uma exceção quando uma
   função da biblioteca C retornou um erro e definir a variável C
   "errno". Ela constrói um objeto tupla cujo primeiro item é o valor
   inteiro "errno" e cujo segundo item é a mensagem de erro
   correspondente (obtida de "strerror()"), e então chama
   "PyErr_SetObject(type, object)". No Unix, quando o valor "errno" é
   "EINTR", indicando uma chamada de sistema interrompida, isso chama
   "PyErr_CheckSignals()", e se isso definir o indicador de erro,
   deixa-o definido como tal. A função retorna sempre "NULL", de forma
   que uma função que envolve uma chamada de sistema pode retornar
   "return PyErr_SetFromErrno(type);" quando a chamada de sistema
   retornar um erro.

PyObject *PyErr_SetFromErrnoWithFilenameObject(PyObject *type, PyObject *filenameObject)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável.*

   Similar à "PyErr_SetFromErrno()", com o comportamento adicional de
   que, se *filenameObject* não é "NULL", ele é passado para o
   construtor de *type* como um terceiro parâmetro. No caso da exceção
   "OSError", isso é usado para definir o atributo "filename" da
   instância da exceção.

PyObject *PyErr_SetFromErrnoWithFilenameObjects(PyObject *type, PyObject *filenameObject, PyObject *filenameObject2)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável desde a versão
   3.7.*

   Similar à "PyErr_SetFromErrnoWithFilenameObject()", mas recebe um
   segundo objeto filename, para levantar erros quando uma função que
   recebe dois nomes de arquivos falha.

   Adicionado na versão 3.4.

PyObject *PyErr_SetFromErrnoWithFilename(PyObject *type, const char *filename)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável.*

   Similar à "PyErr_SetFromErrnoWithFilenameObject()", mas o nome do
   arquivo é fornecido como uma string C. *filename* é decodificado do
   *filesystem encoding and error handler*.

PyObject *PyErr_SetFromWindowsErr(int ierr)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Essa é uma função conveniente para levantar "OSError". Se chamada
   com *ierr* de "0", o código de erro retornado por uma chamada para
   "GetLastError()" é usado instantaneamente. Ela chama a função Win32
   "FormatMessage()" para retornar a descrição Windows do código de
   erro dado por *ierr* ou "GetLastError()", e então constrói um
   objeto "OSError" com o atributo "winerror" definido para o código
   de erro, o atributo "strerror" definido para a mensagem de erro
   correspondente (lida de "FormatMessage()"), e então chama
   "PyErr_SetObject(PyExc_OSError, object)". Essa função sempre
   retorna "NULL".

   Disponibilidade: Windows.

PyObject *PyErr_SetExcFromWindowsErr(PyObject *type, int ierr)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Semelhante a "PyErr_SetFromWindowsErr()", com um parâmetro
   adicional que especifica o tipo de exceção a ser levantada.

   Disponibilidade: Windows.

PyObject *PyErr_SetFromWindowsErrWithFilename(int ierr, const char *filename)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Semelhante a "PyErr_SetFromWindowsErr()", com o comportamento
   adicional de que, se *filename* não for "NULL", ele é decodificado
   a partir da codificação do sistema de arquivos ("os.fsdecode()") e
   passado para o construtor de "OSError" como um terceiro parâmetro a
   ser usado para definir o atributo "filename" da instância da
   exceção.

   Disponibilidade: Windows.

PyObject *PyErr_SetExcFromWindowsErrWithFilenameObject(PyObject *type, int ierr, PyObject *filename)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Semelhante a "PyErr_SetExcFromWindowsErr()", com o comportamento
   adicional de que, se *filename* não for "NULL", ele é passado para
   o construtor de "OSError" como um terceiro parâmetro a ser usado
   para definir o atributo "filename" da instância da exceção.

   Disponibilidade: Windows.

PyObject *PyErr_SetExcFromWindowsErrWithFilenameObjects(PyObject *type, int ierr, PyObject *filename, PyObject *filename2)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Similar à "PyErr_SetExcFromWindowsErrWithFilenameObject()", mas
   aceita um segundo caminho do objeto.

   Disponibilidade: Windows.

   Adicionado na versão 3.4.

PyObject *PyErr_SetExcFromWindowsErrWithFilename(PyObject *type, int ierr, const char *filename)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável on Windows
   desde a versão 3.7.*

   Similar à "PyErr_SetFromWindowsErrWithFilename()", com um parâmetro
   adicional especificando o tipo de exceção a ser gerado.

   Disponibilidade: Windows.

PyObject *PyErr_SetImportError(PyObject *msg, PyObject *name, PyObject *path)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável desde a versão
   3.7.*

   Essa é uma função conveniente para levantar "ImportError". *msg*
   será definido como a string da mensagem de exceção. *name* e
   *path*, ambos os quais podem ser "NULL", serão definidos como,
   respectivamente, os atributos "name" e "path" de "ImportError".

   Adicionado na versão 3.3.

PyObject *PyErr_SetImportErrorSubclass(PyObject *exception, PyObject *msg, PyObject *name, PyObject *path)
    *Retorna valor: Sempre NULL.** Parte da ABI Estável desde a versão
   3.6.*

   Muito parecido com "PyErr_SetImportError()" mas a função permite
   especificar uma subclasse de "ImportError" para levantar uma
   exceção.

   Adicionado na versão 3.6.

void PyErr_SyntaxLocationObject(PyObject *filename, int lineno, int col_offset)

   Define informações de arquivo, linha e deslocamento para a atual
   exceção. Se a exceção não é "SyntaxError", define atributos
   adicionais, os quais fazem o subsistema de impressão de exceções
   pensar que trata-se de um "SyntaxError".

   Adicionado na versão 3.4.

void PyErr_RangedSyntaxLocationObject(PyObject *filename, int lineno, int col_offset, int end_lineno, int end_col_offset)

   Similar a "PyErr_SyntaxLocationObject()", mas também define as
   informações *end_lineno* e *end_col_offset* para a exceção atual.

   Adicionado na versão 3.10.

void PyErr_SyntaxLocationEx(const char *filename, int lineno, int col_offset)
    * Parte da ABI Estável desde a versão 3.7.*

   Como "PyErr_SyntaxLocationObject()", mas *filename* é uma
   bytestring descodificada a partir do *tratador de erros e
   codificação do sistema de arquivos*.

   Adicionado na versão 3.2.

void PyErr_SyntaxLocation(const char *filename, int lineno)
    * Parte da ABI Estável.*

   Como "PyErr_SyntaxLocationEx()", mas o parâmetro *col_offset* é
   omitido.

void PyErr_BadInternalCall()
    * Parte da ABI Estável.*

   Essa é uma abreviação de "PyErr_SetString(PyExc_SystemError,
   message)", onde *message* indica que uma operação interna (por
   exemplo, uma função API C/Python) foi invocada com um argumento
   ilegal. Ela é principalmente para uso interno.

PyObject *PyErr_ProgramTextObject(PyObject *filename, int lineno)

   Obtém a linha de código-fonte em *filename* na linha *lineno*.
   *filename* deve ser um objeto "str" Python.

   Em caso de sucesso, esta função retorna um objeto string do Python
   com a linha encontrada. Em caso de falha, esta função retorna
   "NULL" sem definir uma exceção.

PyObject *PyErr_ProgramText(const char *filename, int lineno)
    * Parte da ABI Estável.*

   Semelhante a "PyErr_ProgramTextObject()", mas *filename* é um const
   char*, que é decodificado com *tratador de erros e codificação do
   sistema de arquivos*, em vez de uma referência de objeto Python.


Emitindo avisos
===============

Use essas funções para emitir avisos a partir de código C. Elas
espelham funções semelhantes exportadas pelo módulo "warnings" do
Python. Normalmente, elas exibem uma mensagem de aviso em
*sys.stderr*; no entanto, também é possível que o usuário tenha
especificado que os avisos devem ser transformados em erros, e nesse
caso, uma exceção será lançada. Também é possível que as funções
levantem uma exceção devido a um problema com o mecanismo de avisos. O
valor de retorno é "0" se nenhuma exceção for lançada, ou "-1" se uma
exceção for lançada. (Não é possível determinar se uma mensagem de
aviso é realmente impressa, nem qual é o motivo da exceção; isso é
intencional.) Se uma exceção for levantada, a função que chamou a
função deve realizar seu tratamento de exceções normal (por exemplo,
liberar as referências pertencentes a "Py_DECREF()" e retornar um
valor de erro).

int PyErr_WarnEx(PyObject *category, const char *message, Py_ssize_t stack_level)
    * Parte da ABI Estável.*

   Emite uma mensagem de aviso. O argumento *category* é uma categoria
   de aviso (veja abaixo) ou "NULL"; o argumento *message* é uma
   string codificada em UTF-8. *stack_level* é um número positivo que
   indica o número de quadros da pilha; o aviso será emitido a partir
   da linha de código atualmente em execução nesse quadro da pilha. Um
   *stack_level* de 1 é a função que chama "PyErr_WarnEx()", 2 é a
   função acima dessa e assim por diante.

   As categorias de aviso devem ser subclasses de "PyExc_Warning";
   "PyExc_Warning" é uma subclasse de "PyExc_Exception"; a categoria
   de aviso padrão é "PyExc_RuntimeWarning". As categorias de aviso
   padrão do Python estão disponíveis como variáveis globais cujos
   nomes estão enumerados em Warning types.

   Para obter informações sobre o controle de avisos, consulte a
   documentação do módulo "warnings" e a opção "-W" na documentação da
   linha de comando. Não existe uma API C para o controle de avisos.

int PyErr_Warn(PyObject *category, const char *message)

   Equivalent to PyErr_WarnEx(category, message, 1).

int PyErr_WarnExplicitObject(PyObject *category, PyObject *message, PyObject *filename, int lineno, PyObject *module, PyObject *registry)

   Emite uma mensagem de aviso com controle explícito sobre todos os
   atributos de aviso. Trata-se de um invólucro simples em torno da
   função Python "warnings.warn_explicit()"; consulte-a para obter
   mais informações. Os argumentos *module* e *registry* podem ser
   definidos como "NULL" para obter o efeito padrão descrito nessa
   função.

   Adicionado na versão 3.4.

int PyErr_WarnExplicit(PyObject *category, const char *message, const char *filename, int lineno, const char *module, PyObject *registry)
    * Parte da ABI Estável.*

   Semelhante a "PyErr_WarnExplicitObject()", exceto que *message* e
   *module* são strings codificadas em UTF-8 e *filename* é
   decodificado a partir do *tratador de erros e codificação do
   sistema de arquivos*.

int PyErr_WarnFormat(PyObject *category, Py_ssize_t stack_level, const char *format, ...)
    * Parte da ABI Estável.*

   Function similar to "PyErr_WarnEx()", but uses
   "PyUnicode_FromFormat()" to format the warning message.  *format*
   is an ASCII-encoded string.

   Adicionado na versão 3.2.

int PyErr_WarnExplicitFormat(PyObject *category, const char *filename, int lineno, const char *module, PyObject *registry, const char *format, ...)

   Similar to "PyErr_WarnExplicit()", but uses
   "PyUnicode_FromFormat()" to format the warning message. *format* is
   an ASCII-encoded string.

   Adicionado na versão 3.2.

int PyErr_ResourceWarning(PyObject *source, Py_ssize_t stack_level, const char *format, ...)
    * Parte da ABI Estável desde a versão 3.6.*

   Função similar a "PyErr_WarnFormat()", mas a *category* é
   "ResourceWarning" e ela passa *source* para
   "warnings.WarningMessage".

   Adicionado na versão 3.6.


Consultando o indicador de erro
===============================

PyObject *PyErr_Occurred()
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Test whether the error indicator is set.  If set, return the
   exception *type* (the first argument to the last call to one of the
   "PyErr_Set*" functions or to "PyErr_Restore()").  If not set,
   return "NULL".  You do not own a reference to the return value, so
   you do not need to "Py_DECREF()" it.

   O chamador deve ter um *estado de thread anexado*.

   Nota:

     Do not compare the return value to a specific exception; use
     "PyErr_ExceptionMatches()" instead, shown below.  (The comparison
     could easily fail since the exception may be an instance instead
     of a class, in the case of a class exception, or it may be a
     subclass of the expected exception.)

int PyErr_ExceptionMatches(PyObject *exc)
    * Parte da ABI Estável.*

   Equivalent to "PyErr_GivenExceptionMatches(PyErr_Occurred(), exc)".
   This should only be called when an exception is actually set; a
   memory access violation will occur if no exception has been raised.

int PyErr_GivenExceptionMatches(PyObject *given, PyObject *exc)
    * Parte da ABI Estável.*

   Return true if the *given* exception matches the exception type in
   *exc*.  If *exc* is a class object, this also returns true when
   *given* is an instance of a subclass.  If *exc* is a tuple, all
   exception types in the tuple (and recursively in subtuples) are
   searched for a match.

PyObject *PyErr_GetRaisedException(void)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.12.*

   Return the exception currently being raised, clearing the error
   indicator at the same time. Return "NULL" if the error indicator is
   not set.

   This function is used by code that needs to catch exceptions, or
   code that needs to save and restore the error indicator
   temporarily.

   Por exemplo:

      {
         PyObject *exc = PyErr_GetRaisedException();

         /* ... code that might produce other errors ... */

         PyErr_SetRaisedException(exc);
      }

   Ver também:

     "PyErr_GetHandledException()", to save the exception currently
     being handled.

   Adicionado na versão 3.12.

void PyErr_SetRaisedException(PyObject *exc)
    * Parte da ABI Estável desde a versão 3.12.*

   Set *exc* as the exception currently being raised, clearing the
   existing exception if one is set.  If *exc* is "NULL", just clear
   the existing exception.

   *exc* must be a valid exception or "NULL".

   This call "*steals*" a reference to *exc*.

   Adicionado na versão 3.12.

void PyErr_Fetch(PyObject **ptype, PyObject **pvalue, PyObject **ptraceback)
    * Parte da ABI Estável.*

   Descontinuado desde a versão 3.12: Use "PyErr_GetRaisedException()"
   em vez disso.

   Retrieve the error indicator into three variables whose addresses
   are passed. If the error indicator is not set, set all three
   variables to "NULL".  If it is set, it will be cleared and you own
   a reference to each object retrieved.  The value and traceback
   object may be "NULL" even when the type object is not.

   Nota:

     This function is normally only used by legacy code that needs to
     catch exceptions or save and restore the error indicator
     temporarily.Por exemplo:

        {
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);

        /* ... código que pode reproduzir outros erros ... */

        PyErr_Restore(type, value, traceback);
        }

void PyErr_Restore(PyObject *type, PyObject *value, PyObject *traceback)
    * Parte da ABI Estável.*

   Descontinuado desde a versão 3.12: Use "PyErr_SetRaisedException()"
   em vez disso.

   Set the error indicator from the three objects, *type*, *value*,
   and *traceback*, clearing the existing exception if one is set. If
   the objects are "NULL", the error indicator is cleared.  Do not
   pass a "NULL" type and non-"NULL" value or traceback.  The
   exception type should be a class.  Do not pass an invalid exception
   type or value. (Violating these rules will cause subtle problems
   later.)  This call takes away a reference to each object: you must
   own a reference to each object before the call and after the call
   you no longer own these references.  (If you don't understand this,
   don't use this function.  I warned you.)

   Nota:

     This function is normally only used by legacy code that needs to
     save and restore the error indicator temporarily. Use
     "PyErr_Fetch()" to save the current error indicator.

void PyErr_NormalizeException(PyObject **exc, PyObject **val, PyObject **tb)
    * Parte da ABI Estável.*

   Descontinuado desde a versão 3.12: Use "PyErr_GetRaisedException()"
   em vez disso, para evitar qualquer possível desnormalização.

   Under certain circumstances, the values returned by "PyErr_Fetch()"
   below can be "unnormalized", meaning that "*exc" is a class object
   but "*val" is not an instance of the  same class.  This function
   can be used to instantiate the class in that case.  If the values
   are already normalized, nothing happens. The delayed normalization
   is implemented to improve performance.

   Nota:

     This function *does not* implicitly set the "__traceback__"
     attribute on the exception value. If setting the traceback
     appropriately is desired, the following additional snippet is
     needed:

        if (tb != NULL) {
        PyException_SetTraceback(val, tb);
        }

PyObject *PyErr_GetHandledException(void)
    * Parte da ABI Estável desde a versão 3.11.*

   Retrieve the active exception instance, as would be returned by
   "sys.exception()". This refers to an exception that was *already
   caught*, not to an exception that was freshly raised. Returns a new
   reference to the exception or "NULL". Does not modify the
   interpreter's exception state.

   Nota:

     This function is not normally used by code that wants to handle
     exceptions. Rather, it can be used when code needs to save and
     restore the exception state temporarily.  Use
     "PyErr_SetHandledException()" to restore or clear the exception
     state.

   Adicionado na versão 3.11.

void PyErr_SetHandledException(PyObject *exc)
    * Parte da ABI Estável desde a versão 3.11.*

   Set the active exception, as known from "sys.exception()".  This
   refers to an exception that was *already caught*, not to an
   exception that was freshly raised. To clear the exception state,
   pass "NULL".

   Nota:

     This function is not normally used by code that wants to handle
     exceptions. Rather, it can be used when code needs to save and
     restore the exception state temporarily.  Use
     "PyErr_GetHandledException()" to get the exception state.

   Adicionado na versão 3.11.

void PyErr_GetExcInfo(PyObject **ptype, PyObject **pvalue, PyObject **ptraceback)
    * Parte da ABI Estável desde a versão 3.7.*

   Retrieve the old-style representation of the exception info, as
   known from "sys.exc_info()".  This refers to an exception that was
   *already caught*, not to an exception that was freshly raised.
   Returns new references for the three objects, any of which may be
   "NULL".  Does not modify the exception info state.  This function
   is kept for backwards compatibility. Prefer using
   "PyErr_GetHandledException()".

   Nota:

     This function is not normally used by code that wants to handle
     exceptions. Rather, it can be used when code needs to save and
     restore the exception state temporarily.  Use
     "PyErr_SetExcInfo()" to restore or clear the exception state.

   Adicionado na versão 3.3.

void PyErr_SetExcInfo(PyObject *type, PyObject *value, PyObject *traceback)
    * Parte da ABI Estável desde a versão 3.7.*

   Set the exception info, as known from "sys.exc_info()".  This
   refers to an exception that was *already caught*, not to an
   exception that was freshly raised.  This function "*steals*" the
   references of the arguments. To clear the exception state, pass
   "NULL" for all three arguments. This function is kept for backwards
   compatibility. Prefer using "PyErr_SetHandledException()".

   Nota:

     This function is not normally used by code that wants to handle
     exceptions. Rather, it can be used when code needs to save and
     restore the exception state temporarily.  Use
     "PyErr_GetExcInfo()" to read the exception state.

   Adicionado na versão 3.3.

   Alterado na versão 3.11: The "type" and "traceback" arguments are
   no longer used and can be NULL. The interpreter now derives them
   from the exception instance (the "value" argument). The function
   still "*steals*" references of all three arguments.


Tratamento de sinal
===================

int PyErr_CheckSignals()
    * Parte da ABI Estável.*

   Handle external interruptions, such as signals or activating a
   debugger, whose processing has been delayed until it is safe to run
   Python code and/or raise exceptions.

   For example, pressing "Ctrl"-"C" causes a terminal to send the
   "signal.SIGINT" signal. This function executes the corresponding
   Python signal handler, which, by default, raises the
   "KeyboardInterrupt" exception.

   "PyErr_CheckSignals()" should be called by long-running C code
   frequently enough so that the response appears immediate to humans.

   Handlers invoked by this function currently include:

   * Signal handlers, including Python functions registered using the
     "signal" module.

     Signal handlers are only run in the main thread of the main
     interpreter.

     (This is where the function got the name: originally, signals
     were the only way to interrupt the interpreter.)

   * Running the garbage collector, if necessary.

   * Executing a pending remote debugger script.

   * Raise the exception set by "PyThreadState_SetAsyncExc()".

   If any handler raises an exception, immediately return "-1" with
   that exception set. Any remaining interruptions are left to be
   processed on the next "PyErr_CheckSignals()" invocation, if
   appropriate.

   If all handlers finish successfully, or there are no handlers to
   run, return "0".

   Alterado na versão 3.12: This function may now invoke the garbage
   collector.

   Alterado na versão 3.14: This function may now execute a remote
   debugger script, if remote debugging is enabled.

   Alterado na versão 3.15: The exception set by
   "PyThreadState_SetAsyncExc()" is now raised.

void PyErr_SetInterrupt()
    * Parte da ABI Estável.*

   Simula o efeito de um sinal "SIGINT" chegando. Isto é equivalente a
   "PyErr_SetInterruptEx(SIGINT)".

   Nota:

     This function is async-signal-safe.  It can be called without an
     *attached thread state* and from a C signal handler.

int PyErr_SetInterruptEx(int signum)
    * Parte da ABI Estável desde a versão 3.10.*

   Simulate the effect of a signal arriving. The next time
   "PyErr_CheckSignals()" is called,  the Python signal handler for
   the given signal number will be called.

   This function can be called by C code that sets up its own signal
   handling and wants Python signal handlers to be invoked as expected
   when an interruption is requested (for example when the user
   presses Ctrl-C to interrupt an operation).

   Se o sinal fornecido não for tratado pelo Python (foi definido como
   "signal.SIG_DFL" ou "signal.SIG_IGN"), ele será ignorado.

   If *signum* is outside of the allowed range of signal numbers, "-1"
   is returned.  Otherwise, "0" is returned.  The error indicator is
   never changed by this function.

   Nota:

     This function is async-signal-safe.  It can be called without an
     *attached thread state* and from a C signal handler.

   Adicionado na versão 3.10.

int PySignal_SetWakeupFd(int fd)

   This utility function specifies a file descriptor to which the
   signal number is written as a single byte whenever a signal is
   received. *fd* must be non-blocking. It returns the previous such
   file descriptor.

   O valor "-1" desabilita o recurso; este é o estado inicial. Isso é
   equivalente à "signal.set_wakeup_fd()" em Python, mas sem nenhuma
   verificação de erro. *fd* deve ser um descritor de arquivo válido.
   A função só deve ser chamada a partir da thread principal.

   Alterado na versão 3.5: No Windows, a função agora também suporta
   manipuladores de socket.


Classes de exceção
==================

PyObject *PyErr_NewException(const char *name, PyObject *base, PyObject *dict)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   This utility function creates and returns a new exception class.
   The *name* argument must be the name of the new exception, a C
   string of the form "module.classname".  The *base* and *dict*
   arguments are normally "NULL". This creates a class object derived
   from "Exception" (accessible in C as "PyExc_Exception").

   The "__module__" attribute of the new class is set to the first
   part (up to the last dot) of the *name* argument, and the class
   name is set to the last part (after the last dot).  The *base*
   argument can be used to specify alternate base classes; it can
   either be only one class or a tuple of classes. The *dict* argument
   can be used to specify a dictionary of class variables and methods.

PyObject *PyErr_NewExceptionWithDoc(const char *name, const char *doc, PyObject *base, PyObject *dict)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Same as "PyErr_NewException()", except that the new exception class
   can easily be given a docstring: If *doc* is non-"NULL", it will be
   used as the docstring for the exception class.

   Adicionado na versão 3.2.

int PyExceptionClass_Check(PyObject *ob)

   Return non-zero if *ob* is an exception class, zero otherwise. This
   function always succeeds.

const char *PyExceptionClass_Name(PyObject *ob)
    * Parte da ABI Estável desde a versão 3.8.*

   Retorna "tp_name" da classe de exceção *ob*.

PyException_HEAD

   This is a macro including the base fields for an exception object.

   This was included in Python's C API by mistake and is not designed
   for use in extensions. For creating custom exception objects, use
   "PyErr_NewException()" or otherwise create a class inheriting from
   "PyExc_BaseException".

   Suavemente descontinuado desde a versão 3.15.


Objeto Exceção
==============

int PyExceptionInstance_Check(PyObject *op)

   Return true if *op* is an instance of "BaseException", false
   otherwise. This function always succeeds.

PyExceptionInstance_Class(op)

   Equivalent to "Py_TYPE(op)".

PyObject *PyException_GetTraceback(PyObject *ex)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return the traceback associated with the exception as a new
   reference, as accessible from Python through the "__traceback__"
   attribute. If there is no traceback associated, this returns
   "NULL".

int PyException_SetTraceback(PyObject *ex, PyObject *tb)
    * Parte da ABI Estável.*

   Defina o retorno traceback (situação da pilha de execução)
   associado à exceção como *tb*. Use "Py_None" para limpá-lo.

PyObject *PyException_GetContext(PyObject *ex)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return the context (another exception instance during whose
   handling *ex* was raised) associated with the exception as a new
   reference, as accessible from Python through the "__context__"
   attribute. If there is no context associated, this returns "NULL".

void PyException_SetContext(PyObject *ex, PyObject *ctx)
    * Parte da ABI Estável.*

   Set the context associated with the exception to *ctx*.  Use "NULL"
   to clear it.  There is no type check to make sure that *ctx* is an
   exception instance. This "*steals*" a reference to *ctx*.

PyObject *PyException_GetCause(PyObject *ex)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Return the cause (either an exception instance, or "None", set by
   "raise ... from ...") associated with the exception as a new
   reference, as accessible from Python through the "__cause__"
   attribute.

void PyException_SetCause(PyObject *ex, PyObject *cause)
    * Parte da ABI Estável.*

   Set the cause associated with the exception to *cause*.  Use "NULL"
   to clear it.  There is no type check to make sure that *cause* is
   either an exception instance or "None". This "*steals*" a reference
   to *cause*.

   O atributo "__suppress_context__" é implicitamente definido como
   "True" por esta função.

PyObject *PyException_GetArgs(PyObject *ex)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.12.*

   Retorna "args" da exceção *ex*.

void PyException_SetArgs(PyObject *ex, PyObject *args)
    * Parte da ABI Estável desde a versão 3.12.*

   Set "args" of exception *ex* to *args*.

PyObject *PyUnstable_Exc_PrepReraiseStar(PyObject *orig, PyObject *excs)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Implement part of the interpreter's implementation of "except*".
   *orig* is the original exception that was caught, and *excs* is the
   list of the exceptions that need to be raised. This list contains
   the unhandled part of *orig*, if any, as well as the exceptions
   that were raised from the "except*" clauses (so they have a
   different traceback from *orig*) and those that were reraised (and
   have the same traceback as *orig*). Return the "ExceptionGroup"
   that needs to be reraised in the end, or "None" if there is nothing
   to reraise.

   Adicionado na versão 3.12.


Objetos de exceção Unicode
==========================

As seguintes funções são usadas para criar e modificar exceções
Unicode de C.

PyObject *PyUnicodeDecodeError_Create(const char *encoding, const char *object, Py_ssize_t length, Py_ssize_t start, Py_ssize_t end, const char *reason)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Cria um objeto "UnicodeDecodeError" com os atributos *encoding*,
   *object*, *length*, *start*, *end* e *reason*. O *encoding* e
   *reason* são strings codificadas em UTF-8.

PyObject *PyUnicodeDecodeError_GetEncoding(PyObject *exc)
PyObject *PyUnicodeEncodeError_GetEncoding(PyObject *exc)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o atributo * encoding* dado no objeto da exceção.

PyObject *PyUnicodeDecodeError_GetObject(PyObject *exc)
PyObject *PyUnicodeEncodeError_GetObject(PyObject *exc)
PyObject *PyUnicodeTranslateError_GetObject(PyObject *exc)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o atributo *object* dado no objeto da exceção.

int PyUnicodeDecodeError_GetStart(PyObject *exc, Py_ssize_t *start)
int PyUnicodeEncodeError_GetStart(PyObject *exc, Py_ssize_t *start)
int PyUnicodeTranslateError_GetStart(PyObject *exc, Py_ssize_t *start)
    * Parte da ABI Estável.*

   Obtém o atributo *start* do objeto da exceção coloca-o em **start*.
   *start* não deve ser "NULL". Retorna "0" se não der erro, "-1" caso
   dê erro.

   If the "UnicodeError.object" is an empty sequence, the resulting
   *start* is "0". Otherwise, it is clipped to "[0, len(object) - 1]".

   Ver também: "UnicodeError.start"

int PyUnicodeDecodeError_SetStart(PyObject *exc, Py_ssize_t start)
int PyUnicodeEncodeError_SetStart(PyObject *exc, Py_ssize_t start)
int PyUnicodeTranslateError_SetStart(PyObject *exc, Py_ssize_t start)
    * Parte da ABI Estável.*

   Set the *start* attribute of the given exception object to *start*.
   Return "0" on success, "-1" on failure.

   Nota:

     While passing a negative *start* does not raise an exception, the
     corresponding getters will not consider it as a relative offset.

int PyUnicodeDecodeError_GetEnd(PyObject *exc, Py_ssize_t *end)
int PyUnicodeEncodeError_GetEnd(PyObject *exc, Py_ssize_t *end)
int PyUnicodeTranslateError_GetEnd(PyObject *exc, Py_ssize_t *end)
    * Parte da ABI Estável.*

   Obtenha o atributo *end* dado no objeto de exceção e coloque
   **end*. O *end* não deve ser "NULL". Em caso de sucesso, retorna
   "0", em caso de falha, retorna "-1".

   If the "UnicodeError.object" is an empty sequence, the resulting
   *end* is "0". Otherwise, it is clipped to "[1, len(object)]".

int PyUnicodeDecodeError_SetEnd(PyObject *exc, Py_ssize_t end)
int PyUnicodeEncodeError_SetEnd(PyObject *exc, Py_ssize_t end)
int PyUnicodeTranslateError_SetEnd(PyObject *exc, Py_ssize_t end)
    * Parte da ABI Estável.*

   Defina o atributo *end* do objeto de exceção fornecido para *end*.
   Retorna "0" em caso de sucesso e "-1" em caso de falha.

   Ver também: "UnicodeError.end"

PyObject *PyUnicodeDecodeError_GetReason(PyObject *exc)
PyObject *PyUnicodeEncodeError_GetReason(PyObject *exc)
PyObject *PyUnicodeTranslateError_GetReason(PyObject *exc)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna o atributo *reason* dado no objeto da exceção.

int PyUnicodeDecodeError_SetReason(PyObject *exc, const char *reason)
int PyUnicodeEncodeError_SetReason(PyObject *exc, const char *reason)
int PyUnicodeTranslateError_SetReason(PyObject *exc, const char *reason)
    * Parte da ABI Estável.*

   Defina o atributo *reason* do objeto de exceção fornecido para
   *reason*. Retorna "0" em caso de sucesso e "-1" em caso de falha.


Controle de recursão
====================

These two functions provide a way to perform safe recursive calls at
the C level, both in the core and in extension modules.  They are
needed if the recursive code does not necessarily invoke Python code
(which tracks its recursion depth automatically). They are also not
needed for *tp_call* implementations because the call protocol takes
care of recursion handling.

int Py_EnterRecursiveCall(const char *where)
    * Parte da ABI Estável desde a versão 3.9.*

   Marca um ponto em que a chamada recursiva em nível C está prestes a
   ser executada.

   The function then checks if the stack limit is reached.  If this is
   the case, a "RecursionError" is set and a nonzero value is
   returned. Otherwise, zero is returned.

   The check is based on the remaining C stack space of the current
   thread, not on a count of calls, so it is unaffected by
   "Py_SetRecursionLimit()" and "sys.setrecursionlimit()".

   *where* should be a UTF-8 encoded string such as "" in instance
   check"" to be concatenated to the "RecursionError" message caused
   by the recursion depth limit.

   Ver também:

     The "PyUnstable_ThreadState_SetStackProtection()" function.

   Alterado na versão 3.9: Esta função agora também está disponível na
   API limitada.

   Alterado na versão 3.14: The check is based on the remaining C
   stack space.  Previously, a separate counter of C-level calls was
   used.

void Py_LeaveRecursiveCall(void)
    * Parte da ABI Estável desde a versão 3.9.*

   Termina com "Py_EnterRecursiveCall()". Deve ser chamada  uma vez
   para cada invocação *successful* de "Py_EnterRecursiveCall()".

   Alterado na versão 3.9: Esta função agora também está disponível na
   API limitada.

Properly implementing "tp_repr" for container types requires special
recursion handling.  In addition to protecting the stack, "tp_repr"
also needs to track objects to prevent cycles.  The following two
functions facilitate this functionality.  Effectively, these are the C
equivalent to "@reprlib.recursive_repr".

int Py_ReprEnter(PyObject *object)
    * Parte da ABI Estável.*

   Chamado no início da implementação "tp_repr" para detectar ciclos.

   If the object has already been processed, the function returns a
   positive integer.  In that case the "tp_repr" implementation should
   return a string object indicating a cycle.  As examples, "dict"
   objects return "{...}" and "list" objects return "[...]".

   A função retornará um inteiro negativo se o limite da recursão for
   atingido. Nesse caso a implementação "tp_repr" deverá,
   normalmente,. retornar "NULL".

   Caso contrário, a função retorna zero e a implementação "tp_repr"
   poderá continuar normalmente.

void Py_ReprLeave(PyObject *object)
    * Parte da ABI Estável.*

   Termina a "Py_ReprEnter()". Deve ser chamado uma vez para cada
   chamada de "Py_ReprEnter()" que retorna zero.

int Py_GetRecursionLimit(void)
    * Parte da ABI Estável.*

   Get the recursion limit for the current interpreter. It can be set
   with "Py_SetRecursionLimit()". The recursion limit prevents the
   Python interpreter stack from growing infinitely.

   This function cannot fail, and the caller must hold an *attached
   thread state*.

   Ver também: "sys.getrecursionlimit()"

void Py_SetRecursionLimit(int new_limit)
    * Parte da ABI Estável.*

   Set the recursion limit for the current interpreter.

   This function cannot fail, and the caller must hold an *attached
   thread state*.

   Ver também: "sys.setrecursionlimit()"


Exception and warning types
===========================

All standard Python exceptions and warning categories are available as
global variables whose names are "PyExc_" followed by the Python
exception name. These have the type PyObject*; they are all class
objects.

For completeness, here are all the variables:


Tipos de exceção
----------------

These pointers are part of the Stable ABI since the version in the
*S.ABI* column (or since 3.2 when *S.ABI* is empty). Exceptions marked
N/A are *not* part of the Stable ABI.

+-----------------------------------+-----------------------------------+-----------------------------------+
| Nome C                            | S.ABI                             | Nome Python                       |
|===================================|===================================|===================================|
| PyObject *PyExc_BaseException     |                                   | "BaseException"                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          | 3.11                              | "BaseExceptionGroup"              |
| *PyExc_BaseExceptionGroup         |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_Exception         |                                   | "Exception"                       |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ArithmeticError   |                                   | "ArithmeticError"                 |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_AssertionError    |                                   | "AssertionError"                  |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_AttributeError    |                                   | "AttributeError"                  |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_BlockingIOError   | 3.7                               | "BlockingIOError"                 |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_BrokenPipeError   | 3.7                               | "BrokenPipeError"                 |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_BufferError       |                                   | "BufferError"                     |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ChildProcessError | 3.7                               | "ChildProcessError"               |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          | 3.7                               | "ConnectionAbortedError"          |
| *PyExc_ConnectionAbortedError     |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ConnectionError   | 3.7                               | "ConnectionError"                 |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          | 3.7                               | "ConnectionRefusedError"          |
| *PyExc_ConnectionRefusedError     |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          | 3.7                               | "ConnectionResetError"            |
| *PyExc_ConnectionResetError       |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_EOFError          |                                   | "EOFError"                        |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_FileExistsError   | 3.7                               | "FileExistsError"                 |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_FileNotFoundError | 3.7                               | "FileNotFoundError"               |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          |                                   | "FloatingPointError"              |
| *PyExc_FloatingPointError         |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_GeneratorExit     |                                   | "GeneratorExit"                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ImportCycleError  | N/D                               | "ImportCycleError"                |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ImportError       |                                   | "ImportError"                     |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_IndentationError  |                                   | "IndentationError"                |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_IndexError        |                                   | "IndexError"                      |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_InterruptedError  | 3.7                               | "InterruptedError"                |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_IsADirectoryError | 3.7                               | "IsADirectoryError"               |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_KeyError          |                                   | "KeyError"                        |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_KeyboardInterrupt |                                   | "KeyboardInterrupt"               |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_LookupError       |                                   | "LookupError"                     |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_MemoryError       |                                   | "MemoryError"                     |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          | 3.6                               | "ModuleNotFoundError"             |
| *PyExc_ModuleNotFoundError        |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_NameError         |                                   | "NameError"                       |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          | 3.7                               | "NotADirectoryError"              |
| *PyExc_NotADirectoryError         |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          |                                   | "NotImplementedError"             |
| *PyExc_NotImplementedError        |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_OSError           |                                   | "OSError"                         |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_OverflowError     |                                   | "OverflowError"                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_PermissionError   | 3.7                               | "PermissionError"                 |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          | 3.7                               | "ProcessLookupError"              |
| *PyExc_ProcessLookupError         |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          |                                   | "PythonFinalizationError"         |
| *PyExc_PythonFinalizationError    |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_RecursionError    | 3.7                               | "RecursionError"                  |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ReferenceError    |                                   | "ReferenceError"                  |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_RuntimeError      |                                   | "RuntimeError"                    |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          | 3.7                               | "StopAsyncIteration"              |
| *PyExc_StopAsyncIteration         |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_StopIteration     |                                   | "StopIteration"                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_SyntaxError       |                                   | "SyntaxError"                     |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_SystemError       |                                   | "SystemError"                     |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_SystemExit        |                                   | "SystemExit"                      |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_TabError          |                                   | "TabError"                        |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_TimeoutError      | 3.7                               | "TimeoutError"                    |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_TypeError         |                                   | "TypeError"                       |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_UnboundLocalError |                                   | "UnboundLocalError"               |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          |                                   | "UnicodeDecodeError"              |
| *PyExc_UnicodeDecodeError         |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          |                                   | "UnicodeEncodeError"              |
| *PyExc_UnicodeEncodeError         |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_UnicodeError      |                                   | "UnicodeError"                    |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          |                                   | "UnicodeTranslateError"           |
| *PyExc_UnicodeTranslateError      |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ValueError        |                                   | "ValueError"                      |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ZeroDivisionError |                                   | "ZeroDivisionError"               |
+-----------------------------------+-----------------------------------+-----------------------------------+

Adicionado na versão 3.3: "PyExc_BlockingIOError",
"PyExc_BrokenPipeError", "PyExc_ChildProcessError",
"PyExc_ConnectionError", "PyExc_ConnectionAbortedError",
"PyExc_ConnectionRefusedError", "PyExc_ConnectionResetError",
"PyExc_FileExistsError", "PyExc_FileNotFoundError",
"PyExc_InterruptedError", "PyExc_IsADirectoryError",
"PyExc_NotADirectoryError", "PyExc_PermissionError",
"PyExc_ProcessLookupError" e "PyExc_TimeoutError" foram introduzidos
seguindo a **PEP 3151**.

Adicionado na versão 3.5: "PyExc_StopAsyncIteration" e
"PyExc_RecursionError".

Adicionado na versão 3.6: "PyExc_ModuleNotFoundError".

Adicionado na versão 3.11: "PyExc_BaseExceptionGroup".


OSError aliases
---------------

The following are a compatibility aliases to "PyExc_OSError".

Alterado na versão 3.3: Esses aliases costumavam ser tipos de exceção
separados.

+-----------------------------------+-----------------------------------+-----------------------------------+
| Nome C                            | Nome Python                       | Notas                             |
|===================================|===================================|===================================|
| PyObject *PyExc_EnvironmentError  | "OSError"                         |                                   |
| * Parte da ABI Estável.*          |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_IOError  * Parte  | "OSError"                         |                                   |
| da ABI Estável.*                  |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_WindowsError  *   | "OSError"                         | [win]                             |
| Parte da ABI Estável on Windows   |                                   |                                   |
| desde a versão 3.7.*              |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+

Notas:

[win] "PyExc_WindowsError" is only defined on Windows; protect code
      that uses this by testing that the preprocessor macro
      "MS_WINDOWS" is defined.


Warning types
-------------

These pointers are part of the Stable ABI since the version in the
*S.ABI* column (or since 3.2 when *S.ABI* is empty).

+-----------------------------------+-----------------------------------+-----------------------------------+
| Nome C                            | S.ABI                             | Nome Python                       |
|===================================|===================================|===================================|
| PyObject *PyExc_Warning           |                                   | "Warning"                         |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_BytesWarning      |                                   | "BytesWarning"                    |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          |                                   | "DeprecationWarning"              |
| *PyExc_DeprecationWarning         |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_EncodingWarning   | 3.10                              | "EncodingWarning"                 |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_FutureWarning     |                                   | "FutureWarning"                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ImportWarning     |                                   | "ImportWarning"                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject                          |                                   | "PendingDeprecationWarning"       |
| *PyExc_PendingDeprecationWarning  |                                   |                                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_ResourceWarning   | 3.7                               | "ResourceWarning"                 |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_RuntimeWarning    |                                   | "RuntimeWarning"                  |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_SyntaxWarning     |                                   | "SyntaxWarning"                   |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_UnicodeWarning    |                                   | "UnicodeWarning"                  |
+-----------------------------------+-----------------------------------+-----------------------------------+
| PyObject *PyExc_UserWarning       |                                   | "UserWarning"                     |
+-----------------------------------+-----------------------------------+-----------------------------------+

Adicionado na versão 3.2: "PyExc_ResourceWarning".

Adicionado na versão 3.10: "PyExc_EncodingWarning".


Tracebacks
==========

PyTypeObject PyTraceBack_Type
    * Parte da ABI Estável.*

   Type object for traceback objects. This is available as
   "types.TracebackType" in the Python layer.

int PyTraceBack_Check(PyObject *op)

   Return true if *op* is a traceback object, false otherwise. This
   function does not account for subtypes.

int PyTraceBack_Here(PyFrameObject *f)
    * Parte da ABI Estável.*

   Replace the "__traceback__" attribute on the current exception with
   a new traceback prepending *f* to the existing chain.

   Calling this function without an exception set is undefined
   behavior.

   Esta função retorna "0" em caso de sucesso e retorna "-1" com uma
   exceção definida em caso de falha.

int PyTraceBack_Print(PyObject *tb, PyObject *f)
    * Parte da ABI Estável.*

   Write the traceback *tb* into the file *f*.

   Esta função retorna "0" em caso de sucesso e retorna "-1" com uma
   exceção definida em caso de falha.

const char *PyUnstable_DumpTraceback(int fd, PyThreadState *tstate)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Write a trace of the Python stack in *tstate* into the file *fd*.
   The format looks like:

      Traceback (most recent call first):
        File "xxx", line xxx in <xxx>
        File "xxx", line xxx in <xxx>
        ...
        File "xxx", line xxx in <xxx>

   This function is meant to debug situations such as segfaults, fatal
   errors, and similar. The file and function names it outputs are
   encoded to ASCII with backslashreplace and truncated to 500
   characters. It writes only the first 100 frames; further frames are
   truncated with the line "...".

   This function will return "NULL" on success, or an error message on
   error.

   This function is intended for use in crash scenarios such as signal
   handlers for SIGSEGV, where the interpreter may be in an
   inconsistent state. Given that it reads interpreter data structures
   that may be partially modified, the function might produce
   incomplete output or it may even crash itself.

   The caller does not need to hold an *attached thread state*, nor
   does *tstate* need to be attached.

   Adicionado na versão 3.15.

const char *PyUnstable_DumpTracebackThreads(int fd, PyInterpreterState *interp, PyThreadState *current_tstate, Py_ssize_t max_threads)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Write the traces of all Python threads in *interp* into the file
   *fd*.

   If *interp* is "NULL" then this function will try to identify the
   current interpreter using thread-specific storage. If it cannot, it
   will return an error.

   If *current_tstate* is not "NULL" then it will be used to identify
   what the current thread is in the written output. If it is "NULL"
   then this function will identify the current thread using thread-
   specific storage. It is not an error if the function is unable to
   get the current Python thread state.

   This function will return "NULL" on success, or an error message on
   error.

   This function is meant to debug situations such as segfaults, fatal
   errors, and similar. It calls "PyUnstable_DumpTraceback()" for each
   thread. It only writes the tracebacks of the first *max_threads*
   threads, further output is truncated with the line "...". If
   *max_threads* is 0, the function will use a default value of 100
   for the argument.

   This function is intended for use in crash scenarios such as signal
   handlers for SIGSEGV, where the interpreter may be in an
   inconsistent state. Given that it reads interpreter data structures
   that may be partially modified, the function might produce
   incomplete output or it may even crash itself.

   The caller does not need to hold an *attached thread state*, nor
   does *current_tstate* need to be attached.

   Aviso:

     On the *free-threaded build*, this function is not thread-safe.
     If another thread deletes its *thread state* while this function
     is being called, the process will likely crash.

   Adicionado na versão 3.15.
