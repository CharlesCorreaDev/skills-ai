"cmd" --- Suporte para interpretadores de comando orientado a linhas
********************************************************************

**Código-fonte:** Lib/cmd.py

======================================================================

A classe "Cmd" fornece um framework simples para escrever
interpretadores de comando orientados a linhas. Eles são
frequentemente úteis para melhorar testes, ferramentas administrativas
e protótipos que mais tarde serão encapsulados em uma interface mais
sofisticada.

Um interpretador de comandos criado com "Cmd" geralmente apresenta ao
usuário um prompt interativo, lê a entrada linha por linha e encaminha
cada comando para um método chamado "do_", seguido pelo nome do
comando. Por exemplo, o comando "help" é tratado pelo método
"do_help()". Além do comando "help" nativo, a maior parte do
comportamento do interpretador é definida pelos métodos "do_*" que
você adiciona em sua própria subclasse.

class cmd.Cmd(completekey='tab', stdin=None, stdout=None)

   Uma instância de "Cmd" ou instância de sua subclasse é um framework
   de interpretador orientado a linhas. Não há um bom motivo para
   instanciar "Cmd" em si; em vez disso, ele é útil como uma
   superclasse de uma classe de interpretador que você mesmo define
   para herdar os métodos de "Cmd" e encapsular métodos de ação.

   O argumento opcional *completekey* é o nome "readline" de uma chave
   de conclusão; o padrão é "Tab". Se *completekey* não for "None" e
   "readline" estiver disponível, a conclusão do comando será feita
   automaticamente.

   O padrão, "'tab'", é tratado especialmente, de modo que se refere à
   tecla "Tab" em cada "readline.backend". Especificamente, se
   "readline.backend" for "editline", "Cmd" usará "'^I'" em vez de
   "'tab'". Observe que outros valores não são tratados dessa forma e
   podem funcionar apenas com um backend específico.

   Os argumentos opcionais *stdin* e *stdout* especificam os objetos
   arquivo de entrada e saída que a instância Cmd ou instância de sua
   subclasse usará para entrada e saída. Se não forem especificados,
   eles serão padronizados para "sys.stdin" e "sys.stdout".

   Se você quiser que um determinado *stdin* seja usado, certifique-se
   de definir o atributo "use_rawinput" da instância como "False",
   caso contrário, *stdin* será ignorado.

   Alterado na versão 3.13: "completekey='tab'" é substituído por
   "'^I'" para "editline".


Objetos Cmd
===========

Uma instância "Cmd" tem os seguintes métodos:

Cmd.cmdloop(intro=None)

   Emite um prompt repetidamente, aceite a entrada, analise um prefixo
   inicial da entrada recebida e despache para métodos de ação,
   passando a eles o restante da linha como argumento.

   O argumento opcional é um banner ou uma string de introdução a ser
   emitida antes do primeiro prompt (isso substitui o atributo de
   classe "intro").

   Se o módulo "readline" for carregado, a entrada vai herdar
   automaticamente a edição de lista de histórico semelhante a
   **bash** (por exemplo, "Control"-"P" retorna ao último comando,
   "Control"-"N" avança para o próximo, "Control"-"F" move o cursor
   para a direita de forma não destrutiva, "Control"-"B" move o cursor
   para a esquerda de forma não destrutiva, etc.).

   Um fim de arquivo na entrada é retornado como a string "'EOF'".

   Uma instância de interpretador reconhecerá um comando chamado "foo"
   se e somente se ele tiver um método "do_foo()". Como um caso
   especial, uma linha começando com o caractere "'?'" é despachada
   para o método "do_help()". Como outro caso especial, uma linha
   começando com o caractere "'!'" é despachada para o método
   "do_shell()" (se tal método for definido).

   Este método retornará quando o método "postcmd()" retornar um valor
   true. O argumento *stop* para "postcmd()" é o valor de retorno do
   método "do_*()" correspondente do comando.

   Se o autocompletamento estiver habilitado, os comandos serão
   completados automaticamente, e o autocompletamento dos argumentos
   dos comandos será feito chamando "complete_foo()" com os argumentos
   *text*, *line*, *begidx* e *endidx*. *text* é o prefixo da string
   que estamos tentando corresponder: todas as correspondências
   retornadas devem começar com ele. *line* é a linha de entrada atual
   com os espaços em branco iniciais removidos, *begidx* e *endidx*
   são os índices inicial e final do texto de prefixo, que podem ser
   usados para fornecer diferentes autocompletamentos dependendo da
   posição em que o argumento está.

Cmd.do_help(arg)

   Todas as subclasses de "Cmd" herdam um "do_help()" predefinido.
   Este método, chamado com um argumento "'bar'", invoca o método
   correspondente "help_bar()", e se este não estiver presente,
   imprime a docstring de "do_bar()", se disponível. Sem argumento,
   "do_help()" lista todos os tópicos de ajuda disponíveis (isto é,
   todos os comandos com métodos "help_*()" correspondentes ou
   comandos que têm docstrings), e também lista quaisquer comandos não
   documentados.

Cmd.onecmd(str)

   Interpreta o argumento como se tivesse sido digitado em resposta ao
   prompt. Isso pode ser substituído, mas normalmente não precisa ser;
   veja os métodos "precmd()" e "postcmd()" para ganchos de execução
   úteis. O valor de retorno é um sinalizador que indica se a
   interpretação de comandos pelo interpretador deve parar. Se houver
   um método "do_*()" para o comando *str*, o valor de retorno desse
   método é retornado, caso contrário, o valor de retorno do método
   "default()" é retornado.

Cmd.emptyline()

   Método chamado quando uma linha vazia é inserida em resposta ao
   prompt. Se esse método não for substituído, ele repete o último
   comando não vazio inserido.

Cmd.default(line)

   Método chamado em uma linha de entrada quando o prefixo do comando
   não é reconhecido. Se esse método não for substituído, ele imprime
   uma mensagem de erro e retorna.

Cmd.completedefault(text, line, begidx, endidx)

   Método chamado para completar uma linha de entrada quando nenhum
   método "complete_*()" especificado pelo comando está disponível.
   Por padrão, ele retorna uma lista vazia.

Cmd.columnize(list, displaywidth=80)

   Método chamado para exibir uma lista de strings como um conjunto
   compacto de colunas. Cada coluna tem apenas a largura necessária.
   As colunas são separadas por dois espaços para legibilidade.

Cmd.precmd(line)

   Método gancho executado logo antes da linha de comando *line* ser
   interpretada, mas depois que o prompt de entrada é gerado e
   emitido. Este método é um stub em "Cmd"; ele existe para ser
   substituído por subclasses. O valor de retorno é usado como o
   comando que será executado pelo método "onecmd()"; a implementação
   "precmd()" pode reescrever o comando ou simplesmente retornar
   *line* inalterado.

Cmd.postcmd(stop, line)

   Método gancho executado logo após o término do despacho de um
   comando. Este método é um stub em "Cmd"; ele existe para ser
   substituído por subclasses. *line* é a linha de comando que foi
   executada, e *stop* é um sinalizador que indica se a execução será
   encerrada após a chamada para "postcmd()"; este será o valor de
   retorno do método "onecmd()". O valor de retorno deste método será
   usado como o novo valor para o sinalizador interno que corresponde
   a *stop*; retornar false fará com que a interpretação continue.

Cmd.preloop()

   Método gancho executado uma vez quando "cmdloop()" é chamado. Este
   método é um stub em "Cmd"; ele existe para ser substituído por
   subclasses.

Cmd.postloop()

   Método gancho executado uma vez quando "cmdloop()" está para ser
   retornado. Este método é um stub em "Cmd"; ele existe para ser
   substituído por subclasses.

Instâncias das subclasses "Cmd" têm algumas variáveis de instância
públicas:

Cmd.prompt

   O prompt emitido para solicitar informações.

Cmd.identchars

   A sequência de caracteres aceita para o prefixo do comando.

Cmd.lastcmd

   O último prefixo de comando não vazio visto.

Cmd.cmdqueue

   Uma lista de linhas de entrada enfileiradas. A lista cmdqueue é
   verificada em "cmdloop()" quando uma nova entrada é necessária; se
   não estiver vazia, seus elementos serão processados em ordem, como
   se tivessem sido inseridos no prompt.

Cmd.intro

   Uma string para emitir como uma introdução ou banner. Pode ser
   substituída dando ao método "cmdloop()" um argumento.

Cmd.doc_header

   O cabeçalho a ser emitido se a saída de ajuda tiver uma seção para
   comandos documentados.

Cmd.misc_header

   O cabeçalho a ser emitido se a saída de ajuda tiver uma seção para
   tópicos de ajuda diversos (ou seja, há métodos "help_*()" sem
   métodos "do_*()" correspondentes).

Cmd.undoc_header

   O cabeçalho a ser emitido se a saída de ajuda tiver uma seção para
   comandos não documentados (ou seja, houver métodos "do_*()" sem
   métodos "help_*()" correspondentes).

Cmd.ruler

   O caractere usado para desenhar linhas separadoras sob os
   cabeçalhos de mensagem de ajuda. Se estiver vazio, nenhuma linha de
   régua será desenhada. O padrão é "'='".

Cmd.use_rawinput

   Um sinalizador, com padrão true. Se true, "cmdloop()" usa "input()"
   para exibir um prompt e ler o próximo comando; se false,
   "sys.stdout.write()" e "sys.stdin.readline()" são usados. (Isso
   significa que ao importar "readline", em sistemas que o suportam, o
   interpretador suportará automaticamente edição de linha no estilo
   **Emacs** e pressionamentos de teclas de histórico de comando.)


Exemplo do Cmd
==============

O módulo "cmd" é útil principalmente para criar shells personalizados
que permitem ao usuário trabalhar com um programa interativamente.

Esta seção apresenta um exemplo simples de como construir um shell em
torno de alguns dos comandos do módulo "turtle".

Comandos básicos do turtle, como "forward()", são adicionados a uma
subclasse de "Cmd" com o método chamado "do_forward()". O argumento é
convertido em um número e despachado para o módulo turtle. A docstring
é usada no utilitário de ajuda fornecido pelo shell.

O exemplo também inclui um recurso básico de gravação e reprodução
implementado com o método "precmd()" que é responsável por converter a
entrada para minúsculas e gravar os comandos em um arquivo. O método
"do_playback()" lê o arquivo e adiciona os comandos gravados ao
"cmdqueue" para reprodução imediata:

   import cmd, sys
   from turtle import *

   class TurtleShell(cmd.Cmd):
       intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
       prompt = '(turtle) '
       file = None

       # ----- comandos básicos do turtle -----
       def do_forward(self, arg):
           'Move the turtle forward by the specified distance:  FORWARD 10'
           forward(*parse(arg))
       def do_right(self, arg):
           'Turn turtle right by given number of degrees:  RIGHT 20'
           right(*parse(arg))
       def do_left(self, arg):
           'Turn turtle left by given number of degrees:  LEFT 90'
           left(*parse(arg))
       def do_goto(self, arg):
           'Move turtle to an absolute position with changing orientation.  GOTO 100 200'
           goto(*parse(arg))
       def do_home(self, arg):
           'Return turtle to the home position:  HOME'
           home()
       def do_circle(self, arg):
           'Draw circle with given radius an options extent and steps:  CIRCLE 50'
           circle(*parse(arg))
       def do_position(self, arg):
           'Print the current turtle position:  POSITION'
           print('Current position is %d %d\n' % position())
       def do_heading(self, arg):
           'Print the current turtle heading in degrees:  HEADING'
           print('Current heading is %d\n' % (heading(),))
       def do_color(self, arg):
           'Set the color:  COLOR BLUE'
           color(arg.lower())
       def do_undo(self, arg):
           'Undo (repeatedly) the last turtle action(s):  UNDO'
       def do_reset(self, arg):
           'Clear the screen and return turtle to center:  RESET'
           reset()
       def do_bye(self, arg):
           'Stop recording, close the turtle window, and exit:  BYE'
           print('Thank you for using Turtle')
           self.close()
           bye()
           return True

       # ----- registra e reproduz -----
       def do_record(self, arg):
           'Save future commands to filename:  RECORD rose.cmd'
           self.file = open(arg, 'w')
       def do_playback(self, arg):
           'Playback commands from a file:  PLAYBACK rose.cmd'
           self.close()
           with open(arg) as f:
               self.cmdqueue.extend(f.read().splitlines())
       def precmd(self, line):
           line = line.lower()
           if self.file and 'playback' not in line:
               print(line, file=self.file)
           return line
       def close(self):
           if self.file:
               self.file.close()
               self.file = None

   def parse(arg):
       'Convert a series of zero or more numbers to an argument tuple'
       return tuple(map(int, arg.split()))

   if __name__ == '__main__':
       TurtleShell().cmdloop()

Aqui está uma sessão de exemplo com o shell do turtle mostrando as
funções de ajuda, usando linhas em branco para repetir comandos e o
recurso simples de gravação e reprodução:

   Welcome to the turtle shell.   Type help or ? to list commands.

   (turtle) ?

   Documented commands (type help <topic>):
   ========================================
   bye     color    goto     home  playback  record  right
   circle  forward  heading  left  position  reset   undo

   (turtle) help forward
   Move the turtle forward by the specified distance:  FORWARD 10
   (turtle) record spiral.cmd
   (turtle) position
   Current position is 0 0

   (turtle) heading
   Current heading is 0

   (turtle) reset
   (turtle) circle 20
   (turtle) right 30
   (turtle) circle 40
   (turtle) right 30
   (turtle) circle 60
   (turtle) right 30
   (turtle) circle 80
   (turtle) right 30
   (turtle) circle 100
   (turtle) right 30
   (turtle) circle 120
   (turtle) right 30
   (turtle) circle 120
   (turtle) heading
   Current heading is 180

   (turtle) forward 100
   (turtle)
   (turtle) right 90
   (turtle) forward 100
   (turtle)
   (turtle) right 90
   (turtle) forward 400
   (turtle) right 90
   (turtle) forward 500
   (turtle) right 90
   (turtle) forward 400
   (turtle) right 90
   (turtle) forward 300
   (turtle) playback spiral.cmd
   Current position is 0 0

   Current heading is 0

   Current heading is 180

   (turtle) bye
   Thank you for using Turtle
