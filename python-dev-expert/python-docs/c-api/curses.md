API C de curses
***************

"curses" expõe uma pequena interface C para módulos de extensão. Os
usuários devem incluir o arquivo de cabeçalho "py_curses.h" (que não é
incluído por padrão em "Python.h") e "import_curses()" deve ser
invocada, geralmente como parte da função de inicialização do módulo,
para popular "PyCurses_API".

Aviso:

  Nem a API C nem o módulo "curses" do Python puro são compatíveis com
  subinterpretadores.

import_curses()

   Importa a API C do curses. A macro não precisa de ponto e vírgula
   para ser chamada.

   Em caso de sucesso, popula o ponteiro "PyCurses_API".

   Em caso de falha, define "PyCurses_API" como NULL e levanta uma
   exceção. O chamador deve verificar se ocorreu um erro através de
   "PyErr_Occurred()":

      import_curses();  // O ponto e vírgula é opcional, mas recomendado.
      if (PyErr_Occurred()) { /* cleanup */ }

void **PyCurses_API

   Objeto alocado dinamicamente contendo a API C do curses. Esta
   variável só estará disponível após a execução bem-sucedida da macro
   "import_curses".

   "PyCurses_API[0]" corresponde a "PyCursesWindow_Type".

   "PyCurses_API[1]", "PyCurses_API[2]" e "PyCurses_API[3]" são
   ponteiros para funções predicativas do tipo "int (*)(void)".

   Quando chamados, esses predicados retornam se "curses.setupterm()",
   "curses.initscr()" e "curses.start_color()" foram chamados,
   respectivamente.

   Veja também as macros de conveniência "PyCursesSetupTermCalled",
   "PyCursesInitialised" e "PyCursesInitialisedColor".

   Nota:

     O número de entradas nesta estrutura está sujeito a alterações.
     Considere usar "PyCurses_API_pointers" para verificar se novos
     campos estão disponíveis.

PyCurses_API_pointers

   O número de campos acessíveis ("4") em "PyCurses_API". Esse número
   é incrementado sempre que novos campos são adicionados.

PyTypeObject PyCursesWindow_Type

   O tipo de heap correspondente a "curses.window".

int PyCursesWindow_Check(PyObject *op)

   Retorna verdadeiro se *op* for uma instância de "curses.window",
   falso caso contrário.

As macros a seguir são macros de conveniência que se expandem em
instruções C. Em particular, elas só podem ser usadas como "macro;" ou
"macro", mas não como "macro()" ou "macro();".

PyCursesSetupTermCalled

   Macro que verifica se "curses.setupterm()" foi chamada.

   A expansão de macro é aproximadamente equivalente a:

      {
          typedef int (*predicate_t)(void);
          predicate_t was_setupterm_called = (predicate_t)PyCurses_API[1];
          if (!was_setupterm_called()) {
              return NULL;
          }
      }

PyCursesInitialised

   Macro que verifica se "curses.initscr()" foi chamada.

   A expansão de macro é aproximadamente equivalente a:

      {
          typedef int (*predicate_t)(void);
          predicate_t was_initscr_called = (predicate_t)PyCurses_API[2];
          if (!was_initscr_called()) {
              return NULL;
          }
      }

PyCursesInitialisedColor

   Macro que verifica se "curses.start_color()" foi chamada.

   A expansão de macro é aproximadamente equivalente a:

      {
          typedef int (*predicate_t)(void);
          predicate_t was_start_color_called = (predicate_t)PyCurses_API[3];
          if (!was_start_color_called()) {
              return NULL;
          }
      }


Dados internos
**************

Os seguintes objetos são expostos pela API C, mas devem ser
considerados apenas para uso interno.

PyCurses_CAPSULE_NAME

   Nome da cápsula do curses a ser passada para "PyCapsule_Import()".

   Uso interno apenas. Use "import_curses" em vez disso.
