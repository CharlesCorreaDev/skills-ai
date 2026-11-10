Objetos quadro
**************

type PyFrameObject
    * Parte da ABI Estável (como uma estrutura opaca).*

   A estrutura C dos objetos usados para descrever objetos frame.

   Não há membros públicos nesta estrutura.

   Alterado na versão 3.11: Os membros dessa estrutura foram removidos
   da API C pública. Consulte a entrada O Que há de Novo para
   detalhes.

As funções "PyEval_GetFrame()" e "PyThreadState_GetFrame()" podem ser
utilizadas para obter um objeto frame.

Veja também Reflexão.

PyTypeObject PyFrame_Type

   O tipo de objetos frame. É o mesmo objeto que "types.FrameType" na
   camada Python.

   Alterado na versão 3.11: Anteriormente, este tipo só estava
   disponível após incluir "<frameobject.h>".

PyFrameObject *PyFrame_New(PyThreadState *tstate, PyCodeObject *code, PyObject *globals, PyObject *locals)

   Cria um novo objeto quadro. Esta função retorna uma *referência
   forte* ao novo objeto quadro em caso de sucesso e retorna "NULL"
   com uma exceção definida em caso de falha.

int PyFrame_Check(PyObject *obj)

   Retorna diferente de zero se *obj* é um objeto frame

   Alterado na versão 3.11: Anteriormente, esta função só estava
   disponível após incluir "<frameobject.h>".

PyFrameObject *PyFrame_GetBack(PyFrameObject *frame)
    *Retorna valor: Nova referência.*

   Obtém o *frame* próximo ao quadro externo.

   Return a *strong reference*, or "NULL" if *frame* has no outer
   frame. This raises no exceptions.

   Adicionado na versão 3.9.

PyObject *PyFrame_GetBuiltins(PyFrameObject *frame)
    *Retorna valor: Nova referência.*

   Obtém o atributo "f_builtins" do *frame*.

   Retorna uma *referência forte*. O resultado não pode ser "NULL".

   Adicionado na versão 3.11.

PyCodeObject *PyFrame_GetCode(PyFrameObject *frame)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.10.*

   Obtém o código de *frame*.

   Retorna uma *referência forte*.

   O resultado (código do frame) não pode ser "NULL".

   Adicionado na versão 3.9.

PyObject *PyFrame_GetGenerator(PyFrameObject *frame)
    *Retorna valor: Nova referência.*

   Obtém o gerador, corrotina ou gerador assíncrono que possui este
   frame, ou "NULL" se o frame não pertence a um gerador. Não levanta
   exceção, mesmo que o valor retornado seja "NULL".

   Retorna uma *referência forte*, ou "NULL".

   Adicionado na versão 3.11.

PyObject *PyFrame_GetGlobals(PyFrameObject *frame)
    *Retorna valor: Nova referência.*

   Obtenha o atributo "f_globals" do *frame*.

   Retorna uma *referência forte*. O resultado não pode ser "NULL".

   Adicionado na versão 3.11.

int PyFrame_GetLasti(PyFrameObject *frame)

   Obtenha o atributo "f_lasti" do *frame*.

   Retorna -1 se "frame.f_lasti" é "None".

   Adicionado na versão 3.11.

PyObject *PyFrame_GetVar(PyFrameObject *frame, PyObject *name)
    *Retorna valor: Nova referência.*

   Obtém a variável *name* de *frame*.

   * Retorna uma *referência forte* ao valor da variável em caso de
     sucesso.

   * Levanta uma exceção "NameError" e retorna "NULL" se a variável
     não existir.

   * Levanta uma exceção e retorna "NULL" em caso de erro.

   Tipo de *name* deve ser um "str".

   Adicionado na versão 3.12.

PyObject *PyFrame_GetVarString(PyFrameObject *frame, const char *name)
    *Retorna valor: Nova referência.*

   Semelhante a "PyFrame_GetVar()", mas o nome da variável é uma
   string C codificada em UTF-8.

   Adicionado na versão 3.12.

PyObject *PyFrame_GetLocals(PyFrameObject *frame)
    *Retorna valor: Nova referência.*

   Obtém o atributo "f_locals" do *frame*. Se o quadro se referir a um
   *escopo otimizado*, isso retorna um objeto proxy de escrita direta
   que permite modificar as variáveis locais. Em todos os outros casos
   (classes, módulos, "exec()" e "eval()"), retorna o mapeamento que
   representa as variáveis locais do frame diretamente (como descrito
   para "locals()").

   Retorna uma *referência forte*.

   Adicionado na versão 3.11.

   Alterado na versão 3.13: Como parte de **PEP 667**, retorna uma
   instância de "PyFrameLocalsProxy_Type".

int PyFrame_GetLineNumber(PyFrameObject *frame)
    * Parte da ABI Estável desde a versão 3.10.*

   Retorna o número da linha do *frame* atualmente em execução.


Frame locals proxies
====================

Adicionado na versão 3.13.

The "f_locals" attribute on a frame object is an instance of a "frame-
locals proxy". The proxy object exposes a write-through view of the
underlying locals dictionary for the frame. This ensures that the
variables exposed by "f_locals" are always up to date with the live
local variables in the frame itself.

See **PEP 667** for more information.

PyTypeObject PyFrameLocalsProxy_Type

   The type of frame "locals()" proxy objects.

int PyFrameLocalsProxy_Check(PyObject *obj)

   Return non-zero if *obj* is a frame "locals()" proxy.


Legacy local variable APIs
==========================

These APIs are *soft deprecated*. As of Python 3.13, they do nothing.
They exist solely for backwards compatibility.

void PyFrame_LocalsToFast(PyFrameObject *f, int clear)

   Prior to Python 3.13, this function would copy the "f_locals"
   attribute of *f* to the internal "fast" array of local variables,
   allowing changes in frame objects to be visible to the interpreter.
   If *clear* was true, this function would process variables that
   were unset in the locals dictionary.

   Suavemente descontinuado desde a versão 3.13: Esta função agora não
   faz nada.

void PyFrame_FastToLocals(PyFrameObject *f)

   Prior to Python 3.13, this function would copy the internal "fast"
   array of local variables (which is used by the interpreter) to the
   "f_locals" attribute of *f*, allowing changes in local variables to
   be visible to frame objects.

   Suavemente descontinuado desde a versão 3.13: Esta função agora não
   faz nada.

int PyFrame_FastToLocalsWithError(PyFrameObject *f)

   Prior to Python 3.13, this function was similar to
   "PyFrame_FastToLocals()", but would return "0" on success, and "-1"
   with an exception set on failure.

   Suavemente descontinuado desde a versão 3.13: Esta função agora não
   faz nada.

Ver também: **PEP 667**


Internal frames
===============

Unless using **PEP 523**, you will not need this.

struct _PyInterpreterFrame

   The interpreter's internal frame representation.

   Adicionado na versão 3.11.

PyObject *PyUnstable_InterpreterFrame_GetCode(struct _PyInterpreterFrame *frame);

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

      Return a *strong reference* to the code object for the frame.

   Adicionado na versão 3.12.

int PyUnstable_InterpreterFrame_GetLasti(struct _PyInterpreterFrame *frame);

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Return the byte offset into the last executed instruction.

   Adicionado na versão 3.12.

int PyUnstable_InterpreterFrame_GetLine(struct _PyInterpreterFrame *frame);

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Return the currently executing line number, or -1 if there is no
   line number.

   Adicionado na versão 3.12.

const PyTypeObject *PyUnstable_ExecutableKinds

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   An array of executable kinds (executor types) for frames, used for
   internal debugging and tracing.

   Tools like debuggers and profilers can use this to identify the
   type of execution context associated with a frame (such as to
   filter out internal frames). The entries are indexed by the
   following constants:

   +----------------------------------------------------+----------------------------------------------------+
   | Constante                                          | Descrição                                          |
   |====================================================|====================================================|
   | PyUnstable_EXECUTABLE_KIND_SKIP  *Esta é uma API   | The frame is internal (For example: inlined) and   |
   | Instável. Isso pode se alterado sem aviso em       | should be skipped by tools.                        |
   | lançamentos menores.*                              |                                                    |
   +----------------------------------------------------+----------------------------------------------------+
   | PyUnstable_EXECUTABLE_KIND_PY_FUNCTION  *Esta é    | The frame corresponds to a standard Python         |
   | uma API Instável. Isso pode se alterado sem aviso  | function.                                          |
   | em lançamentos menores.*                           |                                                    |
   +----------------------------------------------------+----------------------------------------------------+
   | PyUnstable_EXECUTABLE_KIND_BUILTIN_FUNCTION  *Esta | The frame corresponds to a function defined in     |
   | é uma API Instável. Isso pode se alterado sem      | native code.                                       |
   | aviso em lançamentos menores.*                     |                                                    |
   +----------------------------------------------------+----------------------------------------------------+
   | PyUnstable_EXECUTABLE_KIND_METHOD_DESCRIPTOR       | The frame corresponds to a method on a class       |
   | *Esta é uma API Instável. Isso pode se alterado    | instance.                                          |
   | sem aviso em lançamentos menores.*                 |                                                    |
   +----------------------------------------------------+----------------------------------------------------+

   Note that reading the executable kind from a frame is currently
   only possible with undocumented internal APIs.

   Adicionado na versão 3.13.

PyUnstable_EXECUTABLE_KINDS

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   The number of entries in "PyUnstable_ExecutableKinds".

   Adicionado na versão 3.13.
