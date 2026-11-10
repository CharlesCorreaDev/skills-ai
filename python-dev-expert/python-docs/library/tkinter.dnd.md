"tkinter.dnd" --- Suporte para arrastar e soltar
************************************************

**Código-fonte:** Lib/tkinter/dnd.py

======================================================================

Nota:

  Isto é experimental e deverá ser descontinuado quando for
  substituído pelo Tk DND.

The "tkinter.dnd" module provides drag-and-drop support for objects
within a single application, within the same window or between
windows. To enable an object to be dragged, you must create an event
binding for it that starts the drag-and-drop process. Typically, you
bind a ButtonPress event to a callback function that you write (see
Bindings and events). The function should call "dnd_start()", where
*source* is the object to be dragged, and *event* is the event that
invoked the call (the argument to your callback function).

A seleção de um objeto de destino ocorre da seguinte forma:

1. Top-down search of the area under the mouse for a target widget:

   * the target widget should have a callable *dnd_accept* attribute;

   * if *dnd_accept* is not present or returns "None", the search
     moves to the parent widget;

   * if no target widget is found, the target object is "None".

2. Call to "<old_target>.dnd_leave(source, event)".

3. Call to "<new_target>.dnd_enter(source, event)".

4. Call to "<target>.dnd_commit(source, event)" to notify of the drop.

5. Call to "<source>.dnd_end(target, event)" to signal the end of
   drag-and-drop.

class tkinter.dnd.DndHandler(source, event)

   A classe *DndHandler* trata de eventos de arrastar e soltar que
   rastreiam eventos Motion e ButtonRelease na raiz do widget de
   evento.

   cancel(event=None)

      Cancela o processo de arrastar e soltar.

   finish(event, commit=0)

      Executa o fim das funções de arrastar e soltar.

   on_motion(event)

      Inspect area below mouse for target objects while a drag is
      performed.

   on_release(event)

      Sinaliza o fim do arrasto quando o padrão de liberação for
      acionado.

tkinter.dnd.dnd_start(source, event)

   Factory function for the drag-and-drop process. Return the
   "DndHandler" instance managing the drag, or "None" if a drag could
   not be started.

Ver também: Bindings and events
