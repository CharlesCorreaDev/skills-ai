"getpass" --- Entrada de senha portátil
***************************************

**Código-fonte:** Lib/getpass.py

======================================================================

Disponibilidade: not WASI.

Este módulo não funciona ou não está disponível em WebAssembly. Veja
Plataformas WebAssembly para mais informações.

O módulo "getpass" fornece duas funções:

getpass.getpass(prompt='Password: ', stream=None, *, echo_char=None)

   Solicita uma senha do usuário sem emiti-la. O usuário é solicitado
   usando a string *prompt*, cujo padrão é "'Password: '". No Unix, o
   prompt é escrito no objeto arquivo ou similar *stream* usando o
   tratador de erros de substituição, se necessário. O *stream* padrão
   para o terminal de controle ("/dev/tty") ou se não estiver
   disponível para "sys.stderr" (este argumento é ignorado no
   Windows).

   O argumento *echo_char* controla como a entrada do usuário é
   exibida durante a digitação. Se *echo_char* for "None" (padrão), a
   entrada permanece oculta. Caso contrário, *echo_char* deve ser um
   único caractere ASCII imprimível e cada caractere digitado será
   substituído por ela. Por exemplo, "echo_char='*'" exibirá
   asteriscos em vez da entrada real.

   If echo-free input is unavailable, "getpass()" falls back to
   printing a warning message to *stream* and reading from "sys.stdin"
   and issuing a "GetPassWarning".

   Nota:

     If you call "getpass()" from within IDLE, the input may be done
     in the terminal you launched IDLE from rather than the idle
     window itself.

   Nota:

     On Unix systems, when *echo_char* is set, the terminal will be
     configured to operate in *noncanonical mode*. Common terminal
     control characters are supported:

     * "Ctrl"+"A" - Move cursor to beginning of line

     * "Ctrl"+"E" - Move cursor to end of line

     * "Ctrl"+"K" - Kill (delete) from cursor to end of line

     * "Ctrl"+"U" - Kill (delete) entire line

     * "Ctrl"+"W" - Erase previous word

     * "Ctrl"+"V" - Insert next character literally (quote)

     * "Backspace"/"DEL" - Delete character before cursor

     These shortcuts work by reading the terminal's configured control
     character mappings from termios settings.

   Alterado na versão 3.14: Adicionado o parâmetro *echo_char* para
   feedback do teclado.

   Alterado na versão 3.15: When using non-empty *echo_char* on Unix,
   keyboard shortcuts (including cursor movement and line editing) are
   now properly handled using the terminal's control character
   configuration.

exception getpass.GetPassWarning

   A subclasse "UserWarning" é levantada quando a entrada de senha
   pode acabar sendo exibida na tela.

getpass.getuser()

   Retorna o "nome de login" do usuário.

   Esta função verifica as variáveis de ambiente "LOGNAME", "USER",
   "LNAME" e "USERNAME", nesta ordem, e retorna o valor da primeiro
   que estiver definida como uma string não vazia. Se nenhuma estiver
   definida, o nome de login do banco de dados de senhas é retornado
   em sistemas que oferecem suporte ao módulo "pwd", caso contrário,
   uma exceção "OSError" é levantada.

   Em geral, esta função deve ter preferência sobre "os.getlogin()".

   Alterado na versão 3.13: Anteriormente, várias exceções além de
   apenas "OSError" eram levantadas.
