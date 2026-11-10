Tkinter dialogs
***************


"tkinter.simpledialog" --- Standard Tkinter input dialogs
=========================================================

**Código-fonte:** Lib/tkinter/simpledialog.py

======================================================================

The "tkinter.simpledialog" module contains convenience classes and
functions for creating simple modal dialogs to get a value from the
user.

tkinter.simpledialog.askfloat(title, prompt, *, initialvalue=None, minvalue=None, maxvalue=None, parent=None)
tkinter.simpledialog.askinteger(title, prompt, *, initialvalue=None, minvalue=None, maxvalue=None, parent=None)
tkinter.simpledialog.askstring(title, prompt, *, initialvalue=None, show=None, parent=None)

   Prompt the user to enter a value of the desired type and return it,
   or "None" if the dialog is cancelled.

   *title* is the dialog title and *prompt* the message shown above
   the entry. *initialvalue* is the value initially placed in the
   entry. *parent* is the window over which the dialog is shown.
   "askinteger()" and "askfloat()" also accept *minvalue* and
   *maxvalue*, which bound the accepted value. "askstring()" also
   accepts *show*, a character used to mask the entered text, for
   example "'*'" to hide a password.

class tkinter.simpledialog.Dialog(parent, title=None)

   The base class for custom dialogs. Instantiating it shows the
   dialog modally and returns once the user closes it; the entered
   value is then available in the "result" attribute.

   result

      The value produced by "apply()", or "None" if the dialog was
      cancelled.

   body(master)

      Substitui para construir a interface da caixa de diálogo e
      retornar o widget que deve ter foco inicial.

   buttonbox()

      O comportamento padrão adiciona botões OK e Cancelar. Substitua
      para layouts de botão personalizados.

   validate()

      Validate the data entered by the user. Return true if it is
      valid, in which case the dialog proceeds to "apply()"; return
      false to keep the dialog open. The default implementation always
      returns true; override it to check the input.

   apply()

      Process the data entered by the user, for example by storing it
      in the "result" attribute. Called after "validate()" succeeds
      and just before the dialog is destroyed. The default
      implementation does nothing; override it to act on or store the
      result.

   destroy()

      Destroy the dialog window, clearing the reference to the widget
      that had the initial focus.

class tkinter.simpledialog.SimpleDialog(master, text='', buttons=[], default=None, cancel=None, title=None, class_=None)

   A simple modal dialog that displays the message *text* above a row
   of push buttons whose labels are given by *buttons*, and returns
   the index of the button the user presses. *default* is the index of
   the button activated by the Return key, *cancel* the index returned
   when the window is closed through the window manager, *title* the
   window title, and *class_* the Tk class name of the window.

   go()

      Display the dialog, wait until the user presses a button or
      closes the window, and return the index of the chosen button.


"tkinter.filedialog" --- File selection dialogs
===============================================

**Código-fonte:** Lib/tkinter/filedialog.py

======================================================================

The "tkinter.filedialog" module provides classes and factory functions
for creating file/directory selection windows.


Native load/save dialogs
------------------------

As seguintes classes e funções fornecem janelas de diálogo de arquivo
que combinam uma aparência nativa com opções de configuração para
personalizar o comportamento. Os seguintes argumentos nomeados são
aplicáveis às classes e funções listado abaixo:

      *parent* - a janela para colocar a caixa de diálogo no topo

      *title* - o título da janela

      *initialdir* - o diretório no qual a caixa de diálogo começa

      *initialfile* - o arquivo selecionado ao abrir a caixa de diálogo

      *filetypes* - uma sequência de tuplas (rótulo, padrão), o caractere curinga '*' é permitido

      *defaultextension* - extensão padrão para anexar ao arquivo (caixas de diálogo para salvar)

      *multiple* - quando verdadeiro, a seleção de vários itens é permitida

**Fábrica de funções estáticas**

The below functions when called create a modal, native look-and-feel
dialog, wait for the user's selection, and return it. The exact return
value depends on the function (see below); when the dialog is
cancelled it is an empty string, an empty tuple or "None". The precise
type of this empty value may vary between platforms and Tk versions,
so test the result for truth rather than comparing it with a specific
value.

tkinter.filedialog.askopenfile(mode='r', **options)
tkinter.filedialog.askopenfiles(mode='r', **options)

   Create an "Open" dialog. "askopenfile()" returns the opened file
   object, or "None" if the dialog is cancelled. "askopenfiles()"
   returns a list of the opened file objects, or an empty tuple if
   cancelled. The files are opened in mode *mode* (read-only "'r'" by
   default).

tkinter.filedialog.asksaveasfile(mode='w', **options)

   Create a "SaveAs" dialog and return the opened file object, or
   "None" if the dialog is cancelled. The file is opened in mode
   *mode* ("'w'" by default).

tkinter.filedialog.askopenfilename(**options)
tkinter.filedialog.askopenfilenames(**options)

   Create an "Open" dialog. "askopenfilename()" returns the selected
   filename as a string, or an empty string if the dialog is
   cancelled. "askopenfilenames()" returns a tuple of the selected
   filenames, or an empty tuple if cancelled.

tkinter.filedialog.asksaveasfilename(**options)

   Create a "SaveAs" dialog and return the selected filename as a
   string, or an empty string if the dialog is cancelled.

tkinter.filedialog.askdirectory(**options)

   Prompt the user to select a directory, and return its path as a
   string, or an empty string if the dialog is cancelled. Additional
   keyword option: *mustexist* - if true, the user may only select an
   existing directory (false by default).

class tkinter.filedialog.Open(master=None, **options)
class tkinter.filedialog.SaveAs(master=None, **options)
class tkinter.filedialog.Directory(master=None, **options)

   The above three classes provide native dialog windows for loading
   and saving files and for selecting a directory.

**Classes de conveniência**

As classes abaixo são usadas para criar janelas de arquivos/diretórios
desde o início. Elas não emulam a aparência nativa da plataforma.

Nota:

  A classe *FileDialog* deve ser uma subclasse para manipulação e
  comportamento de eventos personalizados.

class tkinter.filedialog.FileDialog(master, title=None)

   Cria uma caixa de diálogo básica de seleção de arquivo.

   cancel_command(event=None)

      Aciona o encerramento da janela de diálogo.

   dirs_double_event(event)

      Manipulador de eventos para evento de clique duplo no diretório.

   dirs_select_event(event)

      Manipulador de eventos para evento de clique no diretório.

   files_double_event(event)

      Manipulador de eventos para evento de clique duplo no arquivo.

   files_select_event(event)

      Manipulador de eventos para evento de clique único no arquivo.

   filter_command(event=None)

      Filtra os arquivos por diretório.

   get_filter()

      Recupera o filtro de arquivo atualmente em uso.

   get_selection()

      Recupera o item atualmente selecionado.

   go(dir_or_file=os.curdir, pattern='*', default='', key=None)

      Caixa de diálogo de renderização e inicia um laço de eventos.

   ok_event(event)

      Sai da caixa de diálogo retornando a seleção atual.

   ok_command()

      Called when the user confirms the current selection. The base
      implementation accepts the selection and closes the dialog;
      "LoadFileDialog" and "SaveFileDialog" override it to check the
      selection first.

   quit(how=None)

      Sai da caixa de diálogo retornando o nome do arquivo, se houver.

   set_filter(dir, pat)

      Define o filtro de arquivo.

   set_selection(file)

      Atualiza a seleção de arquivo atual para *file*.

class tkinter.filedialog.LoadFileDialog(master, title=None)

   Uma subclasse de FileDialog que cria uma janela de diálogo para
   selecionar um arquivo existente.

   ok_command()

      Testa se um arquivo é fornecido e se a seleção indica um já
      arquivo existente.

class tkinter.filedialog.SaveFileDialog(master, title=None)

   Uma subclasse de FileDialog que cria uma janela de diálogo para
   selecionar um arquivo de destino.

   ok_command()

      Testa se a seleção aponta ou não para um arquivo válido que não
      é um diretório. A confirmação é necessária se um arquivo já
      existente for selecionado.


"tkinter.commondialog" --- Dialog window templates
==================================================

**Código-fonte:** Lib/tkinter/commondialog.py

======================================================================

The "tkinter.commondialog" module provides the "Dialog" class that is
the base class for dialogs defined in other supporting modules.

class tkinter.commondialog.Dialog(master=None, **options)

   show(**options)

      Renderiza a janela de diálogo.


"tkinter.dialog" --- Classic Tk dialog boxes
============================================

**Source code:** Lib/tkinter/dialog.py

======================================================================

The "tkinter.dialog" module provides a simple modal dialog box built
on the classic (non-themed) Tk widgets.

tkinter.dialog.DIALOG_ICON

   The name of a bitmap ("'questhead'") suitable for use as the
   *bitmap* of a "Dialog".

class tkinter.dialog.Dialog(master=None, cnf={}, **kw)

   Display a modal dialog box built from the classic (non-themed) Tk
   widgets and wait for the user to press one of its buttons. The
   options, given through *cnf* or as keyword arguments, are all
   required: *title* (the window title), *text* (the message),
   *bitmap* (the name of a bitmap icon, such as "DIALOG_ICON"),
   *default* (the index of the default button) and *strings* (the
   sequence of button labels). After construction, the "num" attribute
   holds the index of the button the user pressed.

   destroy()

      Do nothing. The dialog window is destroyed automatically before
      the constructor returns, so there is nothing left for this
      method to do.

Ver também: Módulos "tkinter.messagebox", Lendo e escrevendo arquivos
