"readline" --- Interface para o GNU readline
********************************************

======================================================================

O módulo "readline" define uma série de funções para facilitar o
autocomplemento e leitura/gravação de arquivos históricos do
interpretador Python. Este módulo pode ser usado diretamente ou
através do módulo "rlcompleter", que provê o autocomplemento de
identificadores Python no prompt interativo. As configurações feitas
usando este módulo afetam o comportamento do prompt interativo do
interpretador e dos prompts oferecidos pela função embutida "input()".

As combinações de teclas do Readline podem ser configuradas através de
um arquivo de inicialização, normalmente ".inputrc" em seu diretório
inicial. Consulte Readline Init File no manual do GNU Readline para
obter informações sobre o formato e construções permitidas desse
arquivo e os recursos da biblioteca do Readline em geral.

Disponibilidade: not Android, not iOS, not WASI.

Este módulo não tem suporte em plataformas móveis ou plataformas
WebAssembly.

Este é um *módulo opcional*. Se ele estiver faltando na sua cópia do
CPython, procure a documentação do seu distribuidor (ou seja, quem lhe
forneceu o Python). Se você for o distribuidor, consulte Requisitos
para módulos opcionais.

Disponibilidade: Unix.

Nota:

  A API da biblioteca subjacente do Readline pode ser implementada
  pela biblioteca "editline" ("libedit") em vez do GNU readline. No
  macOS, o módulo "readline" detecta qual biblioteca está sendo usada
  em tempo de execução.O arquivo de configuração do "editline" é
  diferente daquele do GNU readline. Se você carregar strings de
  configuração programaticamente, você pode usar "backend" para
  determinar qual biblioteca está sendo usada.Se você usar a emulação
  de readline do "editline"/"libedit" no macOS, o arquivo de
  inicialização localizado em seu diretório inicial será denominado
  ".editrc". Por exemplo, o seguinte conteúdo em "~/.editrc" ativará
  os atalhos de teclado *vi* e o autocomplemento de TAB:

     python:bind -v
     python:bind ^I rl_complete

  Observe também que bibliotecas diferentes podem usar formatos de
  arquivo de histórico diferentes. Ao alternar a biblioteca
  subjacente, os arquivos de histórico existentes podem se tornar
  inutilizáveis.

readline.backend

   O nome da biblioteca Readline subjacente que está sendo usada, seja
   ""readline"" ou ""editline"".

   Adicionado na versão 3.13.


Arquivo init
============

As seguintes funções estão relacionadas ao arquivo init e à
configuração do usuário:

readline.parse_and_bind(string)

   Executa a linha de init fornecida no argumento *string*. Isso chama
   "rl_parse_and_bind()" na biblioteca subjacente.

readline.read_init_file([filename])

   Executa um arquivo de inicialização readline. O nome de arquivo
   padrão é o último usado. Isso chama "rl_read_init_file()" na
   biblioteca subjacente. Ele levanta um evento de auditoria "open"
   com o nome do arquivo, se fornecido, e ""<readline_init_file>""
   caso contrário, independentemente de qual arquivo a biblioteca
   resolve.

   Alterado na versão 3.14: O evento de auditoria foi adicionado.


Buffer de linha
===============

As seguintes funções operam no buffer de linha:

readline.get_line_buffer()

   Retorna o conteúdo atual do buffer de linha ("rl_line_buffer" na
   biblioteca subjacente).

readline.insert_text(string)

   Insere texto no buffer de linha na posição do cursor. Isso chama
   "rl_insert_text()" na biblioteca subjacente, mas ignora o valor de
   retorno.

readline.redisplay()

   Altera o que é exibido na tela para refletir o conteúdo atual do
   buffer de linha. Isso chama "rl_redisplay()" na biblioteca
   subjacente.


Arquivo de histórico
====================

As seguintes funções operam em um arquivo histórico:

readline.read_history_file([filename])

   Carrega um arquivo de histórico do readline e anexa-o à lista de
   histórico. O nome do arquivo padrão é "~/.history". Isso chama
   "read_history()" na biblioteca subjacente e levanta um evento de
   auditoria "open" com o nome de arquivo se dado e, do contrário,
   ""~/.history"".

   Alterado na versão 3.14: O evento de auditoria foi adicionado.

readline.write_history_file([filename])

   Salva a lista de histórico para um arquivo de histórico do
   readline, sobrescrevendo qualquer arquivo existente. O nome do
   arquivo padrão é "~/.history". Isso chama "write_history()" na
   biblioteca subjacente e levanta um evento de auditoria "open" com o
   nome de arquivo se dado e, do contrário, ""~/.history"".

   Alterado na versão 3.14: O evento de auditoria foi adicionado.

readline.append_history_file(nelements[, filename])

   Anexa os últimos *nelements* itens do histórico a um arquivo. O
   nome do arquivo padrão é "~/.history". O arquivo já deve existir.
   Isso chama "append_history()" na biblioteca subjacente. Esta função
   só existe se o Python foi compilado para uma versão da biblioteca
   que a suporta. Ela levanta um evento de auditoria "open" com o nome
   de arquivo se dado e, do contrário, ""~/.history"".

   Adicionado na versão 3.5.

   Alterado na versão 3.14: O evento de auditoria foi adicionado.

readline.get_history_length()
readline.set_history_length(length)

   Define ou retorna o número desejado de linhas para salvar no
   arquivo de histórico. A função "write_history_file()" usa este
   valor para truncar o arquivo de histórico, chamando
   "history_truncate_file()" na biblioteca subjacente. Valores
   negativos implicam tamanho ilimitado do arquivo de histórico.


Lista de histórico
==================

As seguintes funções operam em uma lista de histórico global:

readline.clear_history()

   Limpa o histórico atual. Isso chama "clear_history()" na biblioteca
   subjacente. A função Python só existe se o Python foi compilado
   para uma versão da biblioteca que a suporta.

readline.get_current_history_length()

   Retorna o número de itens atualmente no histórico. (Isso é
   diferente de "get_history_length()", que retorna o número máximo de
   linhas que serão gravadas em um arquivo de histórico.)

readline.get_history_item(index)

   Retorna o conteúdo atual do item do histórico em *index*. O índice
   do item é baseado em um. Isso chama "history_get()" na biblioteca
   subjacente.

readline.remove_history_item(pos)

   Remove o item de histórico especificado por sua posição do
   histórico. A posição conta a partir de zero. Isso chama
   "remove_history()" na biblioteca subjacente.

readline.replace_history_item(pos, line)

   Substitui o item de histórico especificado pela sua posição por
   *linha*. A posição conta a partir do zero. Isso chama
   "replace_history_entry()" na biblioteca subjacente.

readline.add_history(line)

   Acrescenta *line* ao buffer do histórico, como se fosse a última
   linha digitada. Isso chama "add_history()" na biblioteca
   subjacente.

readline.set_auto_history(enabled)

   Habilita ou desabilita chamadas automáticas para "add_history()" ao
   ler a entrada via readline. O argumento *enabled* deve ser um valor
   booleano que, quando verdadeiro, ativa o histórico automático e,
   quando falso, desativa o histórico automático.

   Adicionado na versão 3.6.

   O histórico automático está ativado por padrão e as alterações não
   persistem em várias sessões.


Ganchos de inicialização
========================

readline.set_startup_hook([function])

   Define ou remove a função invocada pelo retorno de chamada
   "rl_startup_hook" da biblioteca subjacente. Se *function* for
   especificada, ela será usada como a nova função de gancho; se
   omitido ou "None", qualquer função já instalada será removida. O
   gancho é chamado sem argumentos antes de readline imprimir o
   primeiro prompt.

readline.set_pre_input_hook([function])

   Define ou remove a função invocada pelo retorno de chamada
   "rl_pre_input_hook" da biblioteca subjacente. Se *function* for
   especificada, ela será usada como a nova função de gancho; se
   omitida ou "None", qualquer função já instalada será removida. O
   gancho é chamado sem argumentos após a impressão do primeiro prompt
   e pouco antes de readline começar a ler os caracteres de entrada.
   Esta função só existe se o Python foi compilado para uma versão da
   biblioteca que a suporta.

readline.get_pre_input_hook()

   Obtém a função de gancho de pré-entrada atual, ou "None" caso
   nenhuma função de gancho de pré-entrada tenha sido definida. Esta
   função só existe se o Python tiver sido compilado para uma versão
   da biblioteca que ofereça suporte a ela.

   Adicionado na versão 3.15.


Autocomplemento
===============

As funções a seguir estão relacionadas à implementação de uma função
personalizada de autocomplemento ou *completion*, em inglês, de
palavras. Isso normalmente é operado pela tecla Tab e pode sugerir e
completar automaticamente uma palavra que está sendo digitada. Por
padrão, Readline está configurado para ser usado por "rlcompleter"
para completar identificadores Python para o interpretador interativo.
Se o módulo "readline" for usado com um autocomplemento personalizado,
um conjunto diferente de delimitadores de palavras deverá ser
definido.

readline.set_completer([function])

   Define ou remove a função de autocomplemento. Se *function* for
   especificada, ela será usada como a nova função de autocomplemento;
   se omitido ou "None", qualquer função de autocomplemento já
   instalada será removida. A função de autocomplemento é chamada como
   "function(text, state)", para *state* em "0", "1", "2", ..., até
   retornar um valor que não seja string. Deve retornar o próximo
   autocomplemento possível começando com *text*.

   A função de autocomplemento instalada é invocada pelo retorno de
   chamada *entry_func* passado para "rl_completion_matches()" na
   biblioteca subjacente. A string *text* vem do primeiro parâmetro
   para o retorno de chamada "rl_attempted_completion_function" da
   biblioteca subjacente.

readline.get_completer()

   Obtém a função de autocomplemento ou "None" se nenhuma função de
   autocomplemento tiver sido definida.

readline.get_completion_type()

   Obtém o tipo de autocomplemento que está sendo tentado. Isso
   retorna a variável "rl_completion_type" na biblioteca subjacente
   como um número inteiro.

readline.get_begidx()
readline.get_endidx()

   Obtém o índice inicial ou final do escopo de autocomplemento. Esses
   índices são os argumentos *start* e *end* passados para o retorno
   de chamada "rl_attempted_completion_function" da biblioteca
   subjacente. Os valores podem ser diferentes no mesmo cenário de
   edição de entrada com base na implementação de C readline
   subjacente. Por exemplo, sabe-se que o libedit se comporta de
   maneira diferente do libreadline.

readline.set_completer_delims(string)
readline.get_completer_delims()

   Define ou obtém os delimitadores de palavras para autocomplemento.
   Estes determinam o início da palavra a ser considerada para
   autocomplemento (o escopo de autocomplemento). Essas funções
   acessam a variável "rl_completer_word_break_characters" na
   biblioteca subjacente.

readline.set_completion_display_matches_hook([function])

   Define ou remove a função de exibição de autocomplemento. Se
   *function* for especificada, ela será usada como a nova função de
   exibição de autocomplemento; se omitida ou "None", qualquer função
   de exibição de autocomplemento já instalada será removida. Isso
   define ou limpa o retorno de chamada
   "rl_completion_display_matches_hook" na biblioteca subjacente. A
   função de exibição de autocomplemento é chamada como
   "function(substitution, [matches], longest_match_length)" uma vez
   que cada correspondência precisa ser exibida.


Exemplo
=======

O exemplo a seguir demonstra como usar as funções de leitura e
gravação de histórico do módulo "readline" para carregar e salvar
automaticamente um arquivo de histórico chamado ".python_history" do
diretório inicial do usuário. O código abaixo normalmente seria
executado automaticamente durante sessões interativas do arquivo
"PYTHONSTARTUP" do usuário.

   import atexit
   import os
   import readline

   histfile = os.path.join(os.path.expanduser("~"), ".python_history")
   try:
       readline.read_history_file(histfile)
       # comprimento padrão do histórico é -1 (infinito), que pode crescer sem controle
       readline.set_history_length(1000)
   except FileNotFoundError:
       pass

   atexit.register(readline.write_history_file, histfile)

Na verdade, este código é executado automaticamente quando o Python é
executado no modo interativo (veja Configuração Readline).

O exemplo a seguir atinge o mesmo objetivo, mas oferece suporte a
sessões interativas simultâneas, anexando apenas o novo histórico.

   import atexit
   import os
   import readline
   histfile = os.path.join(os.path.expanduser("~"), ".python_history")

   try:
       readline.read_history_file(histfile)
       h_len = readline.get_current_history_length()
   except FileNotFoundError:
       open(histfile, 'wb').close()
       h_len = 0

   def save(prev_h_len, histfile):
       new_h_len = readline.get_current_history_length()
       readline.set_history_length(1000)
       readline.append_history_file(new_h_len - prev_h_len, histfile)
   atexit.register(save, h_len, histfile)

O exemplo a seguir estende a classe "code.InteractiveConsole" para
prover salvamento/restauração do histórico.

   import atexit
   import code
   import os
   import readline

   class HistoryConsole(code.InteractiveConsole):
       def __init__(self, locals=None, filename="<console>",
                    histfile=os.path.expanduser("~/.console-history")):
           code.InteractiveConsole.__init__(self, locals, filename)
           self.init_history(histfile)

       def init_history(self, histfile):
           readline.parse_and_bind("tab: complete")
           if hasattr(readline, "read_history_file"):
               try:
                   readline.read_history_file(histfile)
               except FileNotFoundError:
                   pass
               atexit.register(self.save_history, histfile)

       def save_history(self, histfile):
           readline.set_history_length(1000)
           readline.write_history_file(histfile)

Nota:

  O novo *REPL* introduzido na versão 3.13 não oferece suporte a
  readline. No entanto, readline ainda pode ser usado definindo a
  variável de ambiente "PYTHON_BASIC_REPL".
