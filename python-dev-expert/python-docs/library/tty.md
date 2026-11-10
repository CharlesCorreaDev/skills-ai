"tty" --- Funções de controle de terminal
*****************************************

**Código-fonte:** Lib/tty.py

======================================================================

O módulo "tty" define funções para colocar o tty nos modos de cbreak e
não tratados (raw).

Disponibilidade: Unix.

Por requerer o módulo "termios", ele funcionará apenas no Unix.

O módulo "tty" define as seguintes funções:

tty.cfmakeraw(mode)

   Converte a lista de atributos de tty *mode*, que é uma lista como a
   retornada por "termios.tcgetattr()", para a de um tty em modo raw.

   Adicionado na versão 3.12.

tty.cfmakecbreak(mode)

   Converte a lista de atributos de tty *mode*, que é uma lista como a
   retornada por "termios.tcgetattr()", para a de um tty em modo
   cbreak.

   Isto limpa os sinalizadores de modo local "ECHO" e "ICANON" em
   *mode* bem como configura a entrada mínima para 1 byte sem atraso.

   Adicionado na versão 3.12.

   Alterado na versão 3.12.2: O sinalizador "ICRNL" não está mais
   limpo. Isso corresponde ao comportamento "stty cbreak" do Linux e
   macOS e ao que "setcbreak()" historicamente fez.

tty.setraw(fd, when=termios.TCSAFLUSH)

   Altera o modo do descritor de arquivo *fd* para raw. Se *when* for
   omitido, o padrão é "termios.TCSAFLUSH", e é passado para
   "termios.tcsetattr()". O retorna valor de "termios.tcgetattr()" é
   salvo antes de definir *fd* para o modo raw; esse valor é
   retornado.

   Alterado na versão 3.12: O valor de retorno agora é o atributos
   originais do tty, em vez de "None".

tty.setcbreak(fd, when=termios.TCSAFLUSH)

   Altera o modo de descritor de arquivo *fd* para cbreak. Se *when*
   for omitido, o padrão é "termios.TCSAFLUSH", e é passado para
   "termios.tcsetattr()". O retorna valor de "termios.tcgetattr()" é
   salvo antes de definir *fd* para o modo cbreak; esse valor é
   retornado.

   Isto limpa os sinalizadores de modo local "ECHO" e "ICANON" bem
   como configura a entrada mínima para 1 byte sem atraso.

   Alterado na versão 3.12: O valor de retorno agora é o atributos
   originais do tty, em vez de "None".

   Alterado na versão 3.12.2: O sinalizador "ICRNL" não está mais
   limpo. Isso restaura o comportamento do Python 3.11 e anteriores,
   além de corresponder ao que Linux, macOS e BSDs descrevem em suas
   páginas de manual "stty(1)" em relação ao modo cbreak.

Ver também:

  Módulo "termios"
     Interface baixo nível para controle de terminal.
