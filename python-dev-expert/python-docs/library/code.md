"code" --- Classes bases do interpretador
*****************************************

**Código-fonte:** Lib/code.py

======================================================================

O módulo "code" fornece facilidades para implementar laços de leitura-
execução-escrita no código Python. São incluídas duas classes e
funções de conveniência que podem ser usadas para criar aplicações que
fornecem um prompt de interpretador interativo.

class code.InteractiveInterpreter(locals=None)

   Esta classe trata de análise e estado do interpretador (espaço de
   nomes do usuário); o mesmo não lida com buffer de entrada ou
   solicitação ou nomeação de arquivo de entrada (o nome do arquivo é
   sempre passado explicitamente). O argumento opcional *locals*
   especifica um mapeamento para usar como espaço de nomes no qual o
   código será executado; ele é padrão para um dicionário recém-criado
   com a chave "'__name__'" definida com "'__console__'" e a chave
   "'__doc__'" definida com "None".

   Observe que objetos funções e classes criados sob uma instância
   "InteractiveInterpreter" pertencerão ao espaço de nomes
   especificado por *locals*. Só serão selecionáveis se *locals* for o
   espaço de nomes de um módulo existente.

class code.InteractiveConsole(locals=None, filename='<console>', *, local_exit=False)

   Emula de forma muito semelhante o comportamento do interpretador
   Python interativo. Esta classe baseia-se em
   "InteractiveInterpreter" e adiciona prompts usando os familiares
   "sys.ps1" e "sys.ps2", e buffer de entrada. Se *local_exit* for
   verdadeiro, "exit()" e "quit()" no console não levantarão
   "SystemExit", mas retornarão ao código de chamada.

   Alterado na versão 3.13: Adicionado o parâmetro *local_exit*.

code.interact(banner=None, readfunc=None, local=None, exitmsg=None, local_exit=False)

   Função de conveniência para executar um laço de leitura-execução-
   impressão. Isto cria uma nova instância de "InteractiveConsole" e
   define *readfunc* para ser usado como o método
   "InteractiveConsole.raw_input()", se fornecido. Se *local* for
   fornecido, ele será passado para o construtor "InteractiveConsole"
   para uso como espaço de nomes padrão para o laço do interpretador.
   Se *local_exit* for fornecido, ele será passado para o construtor
   "InteractiveConsole". O método "interact()" da instância é então
   executado com *banner* e *exitmsg* passados como banner e mensagem
   de saída a serem usados, se fornecidos. O objeto console é
   descartado após o uso.

   Alterado na versão 3.6: Parâmetro adicionado *exitmsg*.

   Alterado na versão 3.13: Adicionado o parâmetro *local_exit*.

code.compile_command(source, filename='<input>', symbol='single')

   Esta função é útil para programas que desejam emular o laço
   principal do interpretador Python (também conhecido como laço de
   leitura-execução-impressão). A parte complicada é determinar quando
   o usuário digitou um comando incompleto que pode ser concluído
   inserindo mais texto (em vez de um comando completo ou um erro de
   sintaxe). Esta função *quase* sempre toma a mesma decisão que o
   laço principal do interpretador real.

   *source* é a string fonte; *filename* é o nome do arquivo opcional
   do qual a fonte foi lida, sendo o padrão "'<input>'"; e *symbol* é
   o símbolo opcional de início da gramática, que deve ser "'single'"
   (o padrão), "'eval'" ou "'exec'".

   Retorna um objeto código (o mesmo que "compile(source, filename,
   symbol)") se o comando for completo e válido; "None" se o comando
   estiver incompleto; levanta "SyntaxError" se o comando estiver
   completo e contém um erro de sintaxe, ou levanta "OverflowError" ou
   "ValueError" se o comando contiver um literal inválido.


Objetos de interpretador interativo
===================================

InteractiveInterpreter.runsource(source, filename='<input>', symbol='single')

   Compila e executa alguma fonte no interpretador. Os argumentos são
   os mesmos de "compile_command()"; o padrão para *filename* é
   "'<input>'", e para *symbol* é "'single'". Uma de várias coisas
   pode acontecer:

   * A entrada está incorreta; "compile_command()" levantou uma
     exceção (geralmente "SyntaxError"). Um traceback da sintaxe será
     impresso chamando o método "showsyntaxerror()". "runsource()"
     retorna "False".

   * A entrada está incompleta e são necessárias mais entradas;
     "compile_command()" retornou "None". "runsource()" retorna
     "True".

   * A entrada está completa; "compile_command()" retornou um objeto
     código. O código é executado chamando "runcode()" (que também
     lida com exceções de tempo de execução, exceto "SystemExit").
     "runsource()" retorna "False".

   O valor de retorno pode ser usado para decidir se usar "sys.ps1" ou
   "sys.ps2" para solicitar a próxima linha.

InteractiveInterpreter.runcode(code)

   Executa um objeto código. Quando ocorre uma exceção,
   "showtraceback()" é chamado para exibir um traceback. Todas as
   exceções são capturadas, exceto "SystemExit", que pode ser
   propagada.

   Uma observação sobre "KeyboardInterrupt": esta exceção pode ocorrer
   em outro lugar neste código e nem sempre pode ser detectada. O
   chamador deve estar preparado para lidar com isso.

InteractiveInterpreter.showsyntaxerror(filename=None)

   Exibe o erro de sintaxe que acabou de ocorrer. Isso não exibe um
   stack trace (situação da pilha de execução) porque não há um para
   erros de sintaxe. Se *filename* for fornecido, ele será inserido na
   exceção em vez do nome de arquivo padrão fornecido pelo analisador
   sintático do Python, porque ele sempre usa "'<string>'" ao ler uma
   string. A saída é escrita pelo método "write()".

InteractiveInterpreter.showtraceback()

   Exibe a exceção que acabou de ocorrer. Removemos o primeiro item da
   pilha porque ele está dentro da implementação do objeto
   interpretador. A saída é escrita pelo método "write()".

   Alterado na versão 3.5: O traceback encadeado completo é exibido em
   vez de apenas o traceback primário.

InteractiveInterpreter.write(data)

   Escreve uma string no fluxo de erro padrão ("sys.stderr"). As
   classes derivadas devem substituir isso para fornecer o tratamento
   de saída apropriado conforme necessário.


Objetos de console Interativo
=============================

A classe "InteractiveConsole" é uma subclasse de
"InteractiveInterpreter" e, portanto, oferece todos os métodos dos
objetos interpretadores, bem como as seguintes adições.

InteractiveConsole.interact(banner=None, exitmsg=None)

   Emula de forma muito semelhante o console interativo do Python. O
   argumento opcional *banner* especifica o banner a ser impresso
   antes da primeira interação; por padrão ele imprime um banner
   semelhante ao impresso pelo interpretador Python padrão, seguido
   pelo nome da classe do objeto console entre parênteses (para não
   confundir isso com o interpretador real -- já que está tão
   próximo!).

   O argumento opcional *exitmsg* especifica uma mensagem de saída
   impressa ao sair. Passe a string vazia para suprimir a mensagem de
   saída. Se *exitmsg* não for fornecido ou "None", uma mensagem
   padrão será impressa.

   Alterado na versão 3.4: Para suprimir a impressão de qualquer
   banner, passe uma string vazia.

   Alterado na versão 3.6: Imprime uma mensagem de saída ao sair.

InteractiveConsole.push(line)

   Envia uma linha do texto fonte para o interpretador. A linha não
   deve ter uma nova linha à direita; pode ter novas linhas internas.
   A linha é anexada a um buffer e o método "runsource()" do
   interpretador é chamado com o conteúdo concatenado do buffer como
   fonte. Se isso indicar que o comando foi executado ou é inválido, o
   buffer será redefinido; caso contrário, o comando estará incompleto
   e o buffer permanecerá como estava após a linha ser anexada. O
   valor de retorno é "True" se mais entrada for necessária, "False"
   se a linha foi tratada de alguma forma (isto é o mesmo que
   "runsource()").

InteractiveConsole.resetbuffer()

   Remove qualquer texto fonte não tratado do buffer de entrada.

InteractiveConsole.raw_input(prompt='')

   Escreve um prompt e leia uma linha. A linha retornada não inclui a
   nova linha final. Quando o usuário insere a sequência de teclas de
   fim de linha, uma exceção "EOFError" é levantada. A implementação
   base lê "sys.stdin"; uma subclasse pode substituir isso por uma
   implementação diferente.
