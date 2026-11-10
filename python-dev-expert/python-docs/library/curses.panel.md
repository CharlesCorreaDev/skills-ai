"curses.panel" --- Uma extensão de pilha de painéis para o curses
*****************************************************************

======================================================================

Painéis são janelas com o recurso adicional de profundidade, então
eles podem ser empilhados uns sobre os outros, e somente as partes
visíveis de cada janela serão exibidas. Painéis podem ser adicionados,
movidos para cima ou para baixo na pilha, e removidos.


Funções
=======

The module "curses.panel" defines the following exception:

exception curses.panel.error

   Exception raised when a curses panel library function returns an
   error.

O módulo "curses.panel" define as seguintes funções:

curses.panel.bottom_panel()

   Retorna o painel inferior da pilha de painéis.

curses.panel.new_panel(win)

   Returns a panel object, associating it with the given window *win*
   and placing the new panel on top of the panel stack.  Be aware that
   you need to keep the returned panel object referenced explicitly.
   If you don't, the panel object is garbage collected and removed
   from the panel stack.

curses.panel.top_panel()

   Retorna o painel superior da pilha de painéis.

curses.panel.update_panels()

   Atualiza a tela virtual após alterações na pilha de painéis. Isso
   não chama "curses.doupdate()", então você terá que fazer isso
   sozinho.


Panel objects
=============

class curses.panel.panel

   Panel objects, as returned by "new_panel()" above, are windows with
   a stacking order.  There's always a window associated with a panel
   which determines the content, while the panel methods are
   responsible for the window's depth in the panel stack.

   Objetos painel possuem os seguintes métodos:

panel.above()

   Retorna o painel acima do painel atual.

panel.below()

   Retorna o painel abaixo do painel atual.

panel.bottom()

   Insere o painel para o fundo da pilha.

panel.hidden()

   Retorna "True" se o painel estiver oculto (não visível), "False"
   caso contrário.

panel.hide()

   Oculta o painel. Isso não exclui o objeto, apenas torna a janela
   invisível na tela.

panel.move(y, x)

   Move o painel para as coordenadas "(y, x)" da tela.

panel.replace(win)

   Altera a janela associada ao painel para a janela *win*.

panel.set_userptr(obj)

   Define o ponteiro do usuário do painel para *obj*. Isso é usado
   para associar um pedaço arbitrário de dados ao painel, e pode ser
   qualquer objeto Python.

panel.show()

   Display the panel (which might have been hidden), placing it on top
   of the panel stack.

panel.top()

   Insere o painel para o topo da pilha.

panel.userptr()

   Retorna o ponteiro do usuário para o painel. Pode ser qualquer
   objeto Python.

panel.window()

   Retorna o objeto de janela associado ao painel.
