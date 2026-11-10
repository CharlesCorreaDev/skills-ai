"tkinter.colorchooser" --- Diálogo de escolha de cor
****************************************************

**Código-fonte:** Lib/tkinter/colorchooser.py

======================================================================

O módulo "tkinter.colorchooser" fornece a classe "Chooser" como uma
interface para o diálogo do seletor de cores nativo. "Chooser"
implementa uma janela de diálogo de escolha de cores modal. A classe
"Chooser" herda da classe "Dialog".

class tkinter.colorchooser.Chooser(master=None, **options)

   A classe que implementa a caixa de diálogo modal de seleção de
   cores. A maioria das aplicações utiliza a função de conveniência
   "askcolor()" em vez de instanciar essa classe diretamente.

tkinter.colorchooser.askcolor(color=None, **options)

   Exibe uma caixa de diálogo modal de seleção de cores e retorna a
   cor escolhida. *color* é a cor selecionada quando a caixa de
   diálogo é aberta. O valor de retorno é uma tupla "((r, g, b),
   hexstr)", onde "r", "g" e "b" são os componentes vermelho, verde e
   azul como números inteiros na faixa de 0 a 255, e *hexstr* é a
   string de cor equivalente do Tk, como "'#ff8000'". Se o usuário
   cancelar a caixa de diálogo, é retornado "(None, None)".

   Alterado na versão 3.10: Os valores RGB na cor retornada agora são
   números inteiros na faixa de 0 a 255, em vez de números de ponto
   flutuante.

Ver também:

  Módulo "tkinter.commondialog"
     Módulo de diálogo padrão do Tkinter
