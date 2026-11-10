IDLE --- Editor e console Python
********************************

**Código-fonte:** Lib/idlelib/

======================================================================

IDLE é o Ambiente Integrado de Desenvolvimento e Aprendizagem (em
inglês, Integrated Development and Learning Environment) do Python.

O IDLE tem os seguintes recursos:

* multiplataforma: funciona basicamente da mesma forma no Windows,
  Unix e macOS

* janela de console do Python (interpretador interativo) com
  colorização de entrada de código, saída e mensagens de erro

* editor de texto multijanela com múltiplos desfazer, colorização
  Python, indentação inteligente, dicas de chamada, preenchimento
  automático e outros recursos

* pesquisa em qualquer janela, substituição nas janelas do editor e
  pesquisa em vários arquivos (grep)

* depurador com pontos de interrupção persistentes, etapas e
  visualização de espaço de nomes global e local

* configuração, navegadores e outros diálogos

A aplicação IDLE está implementada no pacote "idlelib".

Este é um *módulo opcional*. Se ele estiver faltando na sua cópia do
CPython, procure a documentação do seu distribuidor (ou seja, quem lhe
forneceu o Python). Se você for o distribuidor, consulte Requisitos
para módulos opcionais.


Menus
=====

O IDLE possui dois tipos principais de janelas: a janela do console e
a janela do editor. É possível ter várias janelas do editor abertas
simultaneamente. No Windows e no Linux, cada uma tem seu próprio menu
superior. Cada menu documentado abaixo indica a qual tipo de janela
está associado.

Janelas de saída, como as usadas para Edit => Find in Files, são um
subtipo de janela de editor. Atualmente, têm o mesmo menu superior,
mas um título predefinido e menu de contexto diferentes.

No macOS, há um menu de aplicações. Ele muda dinamicamente conforme a
janela selecionada no momento. Ele possui um menu de IDLE e algumas
entradas descritas abaixo foram movidas para atender às diretrizes da
Apple.


Menu File (Shell e Editor)
--------------------------

New File
   Cria uma nova janela de edição de arquivo.

Open...
   Abre um arquivo existente com uma caixa de diálogo Open.

Open Module...
   Abre um módulo existente (procura em sys.path).

Recent Files
   Abre uma lista de arquivos recentes. Clique em um para abri-lo.

Module Browser
   Mostra as funções, classes e métodos do arquivo atual do editor em
   uma estrutura de árvore. No console, abre primeiro um módulo.

Path Browser
   Mostra os diretórios do sys.path, módulos, funções, classes e
   métodos em uma estrutura de árvore.

Save
   Salva o conteúdo da janela atual no arquivo associado, se houver
   um. Janelas que foram alteradas desde que foram abertas ou salvas
   pela última vez têm um * antes e depois do título da janela. Se não
   houver um arquivo associado, executa Save As.

Save As...
   Salva a janela atual com uma caixa de diálogo Save As. O arquivo
   salvo torna-se o novo arquivo associado à janela. (Se o seu
   explorador de arquivos estiver configurado para ocultar extensões,
   a extensão atual será omitida na caixa de nome do arquivo. Se o
   novo nome do arquivo não tiver '.', '.py' e '.txt' serão
   adicionados a arquivos Python e de texto, exceto no macOS Aqua,
   onde '.py' é adicionado a todos os arquivos.)

Save Copy As...
   Salva a janela atual em um arquivo diferente sem alterar o arquivo
   associado.  (veja Save As acima sobre a extensão do nome do
   arquivo.)

Print Window
   Imprime a janela atual para a impressora padrão.

Close Window
   Fecha a janela atual (se for um editor não salvo, pergunta se quer
   salvar; se for um console não salvo, pergunta se quer sair da
   execução). Chamar "exit()" ou "close()" na janela do console também
   fecha o console. Se esta for a única janela, também sai do IDLE.

Exit IDLE
   Fecha todas as janelas e sai do IDLE (pergunta se quer salvar as
   janelas de edição não salvas).


Menu Edit (Shell e Editor)
--------------------------

Undo
   Desfaz a última alteração na janela atual. Um máximo de 1000
   alterações pode ser desfeito.

Redo
   Refaz a última alteração desfeita na janela atual.

Select All
   Seleciona todo o conteúdo da janela atual.

Cut
   Copia a seleção para a área de transferência do sistema; depois
   apaga a seleção.

Copy
   Copia a seleção para a área de transferência do sistema.

Paste
   Insere o conteúdo da área de transferência do sistema na janela
   atual.

As funções da área de transferência também estão disponíveis nos menus
de contexto.

Find...
   Abre uma caixa de diálogo de pesquisa com muitas opções

Find Again
   Repete a última pesquisa, se houver uma.

Find Selection
   Procura a string atualmente selecionada, se houver uma.

Find in Files...
   Abre uma caixa de diálogo de pesquisa de ficheiros. Coloca os
   resultados numa nova janela de saída.

Replace...
   Abre uma caixa de diálogo de pesquisa e substituição.

Go to Line
   Move o cursor para o início da linha solicitada e torna essa linha
   visível. Um pedido após o final do ficheiro vai para o final. Limpa
   qualquer seleção e atualiza o estado da linha e da coluna.

Show Completions
   Open a scrollable list allowing selection of existing names. See
   Completions in the Editing and Navigation section below.

Expand Word
   Expande um prefixo que você digitou para corresponder a uma palavra
   completa na mesma janela; repita o processo para obter uma expansão
   diferente.

Show Call Tip
   After an unclosed parenthesis for a function, open a small window
   with function parameter hints.  See Calltips in the Editing and
   Navigation section below.

Show Surrounding Parens
   Realça os parênteses envolventes.


Menu Format (somente na janela do Editor)
-----------------------------------------

Format Paragraph
   Rewrap the text block containing the text insert cursor. Avoid code
   lines.  See Format block in the Editing and Navigation section
   below.

Indent Region
   Desloca as linhas selecionadas à direita pela largura de indentação
   (4 espaços por padrão).

Dedent Region
   Desloca as linhas selecionadas à esquerda pela largura de
   indentação (4 espaços por padrão).

Comment Out Region
   Insere ## à frente das linhas selecionadas.

Uncomment Region
   Remove # ou ## iniciais das linhas selecionadas.

Tabify Region
   Converte sequências iniciais de espaços em tabs. (Nota:
   recomendamos usar blocos de 4 espaços para indentar código Python.)

Untabify Region
   Converte *todos* os tabs para o número correto de espaços.

Toggle Tabs
   Abre uma caixa de diálogo para alternar entre espaços e tabs para
   indentar.

New Indent Width
   Abre uma caixa de diálogo para alterar a largura de indentação. A
   largura predefinida aceita pela comunidade Python é de 4 espaços.

Strip Trailing Whitespace
   Remove espaços e outros caracteres de espaço em branco após o
   último caractere não branco de uma linha aplicando "str.rstrip()" a
   cada linha, incluindo linhas dentro de strings multilinhas. Exceto
   para as janelas Shell, remove as novas linhas extras no final do
   arquivo.


Menu Run (somente na janela do Editor)
--------------------------------------

Run Module
   Executa Check Module. Se não houver erros, reinicia o console para
   limpar o ambiente, depois executa o módulo. A saída é exibida na
   janela Shell. Note que a saída requer o uso de "print" ou "write".
   Quando a execução estiver completa, a Shell mantém o foco e exibe
   um prompt. Neste ponto, pode-se explorar interativamente o
   resultado da execução. Isto é semelhante a executar um ficheiro com
   "python -i file" na linha de comandos.

Run... Customized
   O mesmo que a Run Module, mas executa o módulo com configurações
   personalizadas. *Argumentos de Linha de Comandos* estendem
   "sys.argv" como se passados na linha de comandos. O módulo pode ser
   executado na Shell sem reiniciar.

Check Module
   Verifica a sintaxe do módulo atualmente aberto na janela do Editor.
   Se o módulo não tiver sido salvo, o IDLE perguntará se quer salvar
   ou salvará automaticamente, conforme configurado na aba General da
   caixa de diálogo Settings. Se houver um erro de sintaxe, a
   localização aproximada é indicada na janela do Editor.

Python Shell
   Abre ou ativa a janela do Shell Python.


Menu Shell (somente na janela do Shell)
---------------------------------------

View Last Restart
   Desloca a janela para o último reinício do Shell.

Restart Shell
   Reinicia o shell para limpar o ambiente e redefinir a apresentação
   e o tratamento de exceções.

Previous History
   Percorre os comandos anteriores no histórico que correspondam à
   entrada atual.

Next History
   Percorre os comandos posteriores no histórico que correspondam à
   entrada atual.

Interrupt Execution
   Interrompe um programa em execução.


Menu Debug (somente na janela do Shell)
---------------------------------------

Go to File/Line
   Procura na linha atual com o cursor e na linha acima por um nome de
   arquivo e um número de linha. Se encontrado, abre o arquivo se não
   estiver já aberto e mostra a linha. Use isto para ver as linhas de
   origem referenciadas num traceback de exceção e as linhas
   encontradas por Find in Files. Também está disponível no menu de
   contexto da janela Shell e das janelas de Saída.

Debugger (alternar)
   Quando ativado, o código introduzido na Shell ou executado a partir
   de um Editor será executado sob o depurador. No Editor, é possível
   definir pontos de interrupção pelo menu de contexto. Esta
   funcionalidade ainda está incompleta e é experimental.

Stack Viewer
   Mostra o traceback da pilha da última exceção em formato de árvore,
   incluindo acesso a locais e globais.

Auto-open Stack Viewer
   Alterna a abertura automática do visualizador de pilha para uma
   exceção não tratada.


Menu Options (Shell e Editor)
-----------------------------

Configure IDLE
   Abre uma caixa de diálogo de configuração e alteração de
   preferências, tais como: tipos de letra, indentação, atalhos de
   teclado, temas de cor de texto, janelas de inicialização e tamanho,
   fontes de ajuda adicionais e extensões. No macOS, abre a caixa de
   diálogo de configuração selecionando Preferences no menu da
   aplicação. Para mais detalhes, veja Configurando preferências em
   Ajuda e preferências.

A maioria das opções de configuração aplica-se a todas as janelas ou a
todas as janelas futuras. Os itens de opção abaixo aplicam-se apenas à
janela ativa.

Show/Hide Code Context (somente janela do Editor)
   Abre um painel no topo da janela de edição que mostra o contexto de
   bloco de código exibido no topo da janela. Veja Contexto de código
   na seção de Edição e navegação abaixo.

Show/Hide Line Numbers (somente janela do Editor)
   Abre uma coluna à esquerda da janela de edição que mostra o número
   de cada linha de texto. Por padrão, está desligado, o que pode ser
   alterado nas preferências (veja Configurando preferências).

Zoom/Restore Height
   Alterna a janela entre o tamanho normal e a altura máxima. O
   tamanho inicial é predefinido para 40 linhas por 80 caracteres, a
   menos que seja alterado na General da caixa de diálogo Configure
   IDLE. A altura máxima de uma tela é determinada ao maximizar
   momentaneamente uma janela pela primeira vez que ela é ampliada na
   tela. Alterar as configurações da tela pode invalidar a altura
   salva. Este alternar não tem efeito quando uma janela está
   maximizada.


Menu Window (Shell e Editor)
----------------------------

Lista os nomes de todas as janelas abertas; selecione uma para
trazê-la ao primeiro plano (restaurando-a, se necessário).


Menu Help (Shell e Editor)
--------------------------

About IDLE
   Exibe versão, direitos de autor, licença, créditos e mais.

IDLE Help
   Exibe este documento do IDLE, detalhando as opções de menu, edição
   básica e navegação, e outras dicas.

Python Docs
   Acessa a documentação local do Python, se instalada, ou inicia um
   navegador web e abre docs.python.org mostrando a documentação mais
   recente do Python.

Turtle Demo
   Executa o módulo turtledemo com exemplos de código Python e
   gráficos de tartaruga.

Fontes de ajuda adicionais podem ser adicionadas aqui com a caixa de
diálogo Configure IDLE na aba General. Veja a subsecção Fontes de
ajuda abaixo para mais informações sobre as escolhas do menu Help.


Menus de contexto
-----------------

Abra um menu de contexto clicando com o botão direito em uma janela
(Control+clique no macOS). Os menus de contexto também têm as funções
padrão da área de transferências no menu Edit.

Cut
   Copia a seleção para a área de transferência do sistema; depois
   apaga a seleção.

Copy
   Copia a seleção para a área de transferência do sistema.

Paste
   Insere o conteúdo da área de transferência do sistema na janela
   atual.

As janelas do Editor também têm funções de ponto de interrupção. As
linhas com um ponto de interrupção definido são especialmente
destacadas. Os pontos de interrupção só têm efeito quando executados
no depurador. Os pontos de interrupção de um ficheiro são guardados no
diretório ".idlerc" do usuário.

Set Breakpoint
   Define um ponto de interrupção na linha atual.

Clear Breakpoint
   Limpa o ponto de interrupção da linha.

As janelas Shell e de saída também têm os seguintes menus de contexto.

Go to file/line
   Igual ao menu Debug.

A janela Shell também tem uma funcionalidade de compressão de saída
explicada na subsecção *Janela Shell Python* abaixo.

Squeeze
   Se o cursor estiver sobre uma linha de saída, comprime toda a saída
   entre o código acima e o prompt abaixo em um rótulo 'Squeezed
   text'.


Edição e navegação
==================


Janelas do Editor
-----------------

O IDLE pode abrir janelas de editor ao iniciar, dependendo das
configurações e de como é iniciado. Depois, use o menu File. Só pode
haver uma janela de editor aberta para um determinado arquivo.

A barra de título contém o nome do arquivo, o caminho completo e as
versões do Python e do IDLE que estão sendo executadas na janela. A
barra de estado contém o número da linha ('Ln') e o da coluna ('Col').
Os números de linha começam em 1; os de coluna, em 0.

O IDLE presume que os arquivos com uma extensão  .py* conhecida contêm
código Python e que os demais não contêm. Execute o código Python pelo
menu Run.


Teclas de atalho
----------------

O cursor de inserção do IDLE é uma barra vertical fina entre posições
de caracteres. Quando os caracteres são introduzidos, o cursor de
inserção e tudo o que estiver à sua direita movem-se uma posição para
a direita, e o novo carácter é inserido no espaço criado.

Várias teclas não-caractere movem o cursor e podem apagar caracteres.
A eliminação não coloca texto na área de transferência, mas o IDLE tem
uma lista de cancelamento. Sempre que este documento discute teclas,
'C' refere-se à tecla "Control" no Windows e Unix e à tecla "Command"
no macOS. (E todas essas discussões assumem que as teclas não foram
reatribuídas a outra coisa.)

* As teclas de seta movem o cursor um caractere ou uma linha.

* "C"-"Seta"-"para"-"esquerda" e "C"-"Seta"-"para"-"direita" movem uma
  palavra para a esquerda ou para a direita.

* "Home" e "End" vão para o início ou fim da linha.

* "Page Up" e "Page Down" sobem ou descem uma tela.

* "C"-"Home" e "C"-"End" vão para o início ou fim do arquivo.

* "Backspace" e "Del" (ou "C"-"d") apagam o caractere anterior ou
  seguinte.

* "C"-"Backspace" e "C"-"Del" apagam uma palavra para a esquerda ou
  para a direita.

* "C"-"k" apaga ('mata') tudo à direita.

As associações de teclas padrão (como "C"-"c" para copiar e "C"-"v"
para colar) podem funcionar. As associações de teclas são selecionadas
na caixa de diálogo Configure IDLE.


Indentação automática
---------------------

Depois de uma instrução de abertura de bloco, a linha seguinte é
indentada por 4 espaços (na janela do console do Python por uma
tabulação). Depois de certas palavras-chave (como break, return etc.),
a linha seguinte é desindentada. Na indentação inicial, "Backspace"
apaga até 4 espaços se houver. "Tab" insere espaços (na janela do
console do Python, uma tabulação), o número depende da largura de
indentação. Atualmente, as tabulações estão limitadas a quatro espaços
devido a limitações do Tcl/Tk.

Veja também os comandos de indentar/desindentar região no menu Format.


Busca e substituição
--------------------

Qualquer seleção torna-se um alvo de pesquisa. No entanto, apenas
seleções dentro de uma linha funcionam, pois as pesquisas são
realizadas apenas dentro de linhas, com a quebra ao final removida. Se
"[x] Regular expression" estiver marcada, o alvo é interpretado de
acordo com o módulo re do Python.


Autocomplementos
----------------

Os autocomplementos são fornecidos, quando solicitados e disponíveis,
para nomes de módulos, atributos de classes ou funções, ou nomes de
arquivos. Cada método de solicitação exibe uma caixa de complementos
com os nomes disponíveis. (Veja os complementos de tabulação abaixo
para uma exceção.) Para qualquer caixa, altere o nome que está a ser
completado e o item realçado na caixa digitando e apagando caracteres;
pressionando as teclas "Up", "Down", "PageUp", "PageDown", "Home" e
"End"; e com um clique simples dentro da caixa. Feche a caixa com as
teclas "Escape", "Enter" e duplo "Tab" ou cliques fora da caixa. Um
duplo clique dentro da caixa seleciona e fecha.

Uma forma de abrir uma caixa é pressionar uma tecla de caractere e
aguardar um intervalo predefinido. Isto é predefinido para 2 segundos;
personalize-o na caixa de diálogo de configurações. (Para evitar pop-
ups automáticos, defina o atraso para um valor muito alto, como
100000000.) Para nomes de módulos importados, atributos de classes ou
de funções, digite '.'. Para nomes de arquivos no diretório raiz,
digite "os.sep" ou "os.altsep" imediatamente após uma aspa de
abertura. (No Windows, pode-se especificar uma unidade antes.) Mova-se
para subdiretórios digitando um nome de diretório seguido de um
separador.

Em vez de esperar, ou depois de uma caixa ser fechada, abra uma caixa
de autocomplemento imediatamente com Show Completions no menu Edit. A
tecla de atalho predefinida é "C"-"space". Se digitar um prefixo para
o nome desejado antes de abrir a caixa, a primeira correspondência ou
quase correspondência torna-se visível. O resultado é o mesmo que
inserir um prefixo depois que a caixa é exibida. Show Completions
depois de uma aspa completa nomes de arquivos no diretório atual em
vez do diretório raiz.

Pressionar "Tab" após um prefixo geralmente tem o mesmo efeito que
Show Completions. (Sem prefixo, faz indentação.) No entanto, se houver
apenas uma correspondência para o prefixo, ela é imediatamente
adicionada ao texto do editor, sem abrir uma caixa.

Invocar 'Show Completions', ou pressionar "Tab" após um prefixo, fora
de uma string e sem um '.' anterior, abre uma caixa com palavras
reservadas, nomes embutidos e nomes disponíveis ao nível do módulo.

Ao editar código em um editor (em oposição à Shell), expanda os nomes
disponíveis ao nível do módulo executando o seu código e não
reiniciando a Shell depois disso. Isto é especialmente útil depois de
adicionar importações no topo de um arquivo. Isto também amplia os
possíveis complementos de atributos.

As caixas de autocomplemento excluem inicialmente nomes que começam
com '_' ou, para módulos, não incluídos em '__all__'. Os nomes ocultos
podem ser acessados digitando '_' depois de '.', antes ou depois da
caixa ser aberta.


Dicas de chamada
----------------

Uma dica de chamada é exibida automaticamente quando se digita "("
após o nome de uma função *acessível*. Uma expressão de nome de função
pode incluir pontos e índices. Uma dica de chamada permanece até ser
clicada, o cursor ser movido para fora da área de argumentos, ou ")"
ser digitado. Sempre que o cursor estiver na parte de argumentos de
uma definição, selecione Edit e "Show Call Tip" no menu ou insira o
seu atalho para exibir uma dica de chamada.

A dica de chamada consiste na assinatura da função e na string de
documentação até a primeira linha em branco desta ou a quinta linha
não em branco. (Algumas funções embutidas não têm uma assinatura
acessível.) Uma '/' ou '*' na assinatura indica que os argumentos
precedentes ou seguintes são passados apenas por posição ou nome
(palavra-chave). Os detalhes estão sujeitos a alterações.

Na Shell, as funções acessíveis dependem de quais módulos foram
importados para o processo do usuário, incluindo aqueles importados
pelo próprio IDLE, e quais definições foram executadas, tudo desde o
último reinício.

Por exemplo, reinicie a Shell e introduza "itertools.count(". Uma dica
de chamada aparece porque o IDLE importa itertools para o processo do
utilizador para o seu próprio uso. (Isto pode mudar.) Introduza
"turtle.write(" e nada aparece. O IDLE não importa turtle por si só. A
entrada de menu e o atalho também não fazem nada. Introduza "import
turtle". Depois disso, "turtle.write(" exibirá uma dica de chamada.

Num editor, as instruções de importação não têm efeito até que o
arquivo seja executado. Pode-se querer executar um arquivo depois de
escrever instruções de importação, depois de adicionar definições de
funções, ou depois de abrir um arquivo existente.


Formatação de bloco
-------------------

A opção “Reformat Paragraph” reembrulha um bloco ('parágrafo') de
comentários não em branco igualmente indentados e contíguos, um bloco
semelhante de texto dentro de um string com várias linhas, ou um
subconjunto selecionado de qualquer um deles. Se necessário, adicione
uma linha em branco para separar string do código. Linhas parciais em
uma seleção são expandidas para formar linhas completas. As linhas
resultantes têm a mesma indentação de antes, mas apresentam um
comprimento total máximo de N colunas (caracteres). Altere o padrão N
de 72 na guia Windows da janela IDLE Settings.


Contexto de código
------------------

Dentro de uma janela de editor contendo código Python, o contexto de
código pode ser alternado para mostrar ou ocultar um painel no topo da
janela. Quando mostrado, este painel congela as linhas de abertura
para código de bloco, como aquelas que começam com as palavras-chave
"class", "def" ou "if", que de outra forma poderia passar despercebido
em uma rolagem de página. O tamanho do painel será expandido e
contraído conforme necessário para mostrar todos os níveis atuais de
contexto, até ao número máximo de linhas definido na caixa de diálogo
Configure IDLE (que é 15 por padrão). Se não houver linhas de contexto
atuais e a funcionalidade for ativada, uma única linha em branco será
exibida. Clicar numa linha no painel de contexto moverá essa linha
para o topo do editor.

As cores de texto e fundo para o painel de contexto podem ser
configuradas no separador Highlights na caixa de diálogo Configure
IDLE.


Janela Shell
------------

Na Shell do IDLE, introduza, edite e recupere instruções completas. (A
maioria dos terminais e consolas só funciona com uma única linha
física de cada vez).

Envie uma instrução de linha única para execução pressionando "Return"
com o cursor em qualquer lugar na linha. Se uma linha for estendida
com barra invertida ("\"), o cursor deve estar na última linha física.
Envie uma instrução composta de várias linhas inserindo uma linha em
branco após a instrução.

Quando se cola código na Shell, ele não é compilado e possivelmente
executado até que se pressione "Return", como especificado acima.
Pode-se editar o código colado primeiro. Se colar mais do que uma
instrução na Shell, o resultado será um "SyntaxError" quando várias
instruções são compiladas como se fossem uma.

Linhas contendo "RESTART" significam que o processo de execução do
usuário foi reiniciado. Isto ocorre quando o processo de execução do
usuário falhou, quando se solicita um reinício no menu Shell, ou
quando se executa código numa janela do editor.

As funcionalidades de edição descritas nas subsecções anteriores
funcionam ao introduzir código interativamente. A janela Shell do IDLE
também responde ao seguinte:

* "C"-"c" tenta interromper a execução da instrução (mas pode falhar).

* "C"-"d" fecha a Shell se digitado num prompt ">>>".

* "Alt"-"p" e "Alt"-"n" ("C"-"p" e "C"-"n" no macOS) recuperam para o
  prompt atual a instrução anterior ou seguinte anteriormente
  introduzida que corresponda a algo já digitado.

* "Return" enquanto o cursor está em qualquer instrução anterior anexa
  esta ao que já foi digitado no prompt.


Cores de texto
--------------

Por padrão, o Idle usa preto em texto branco, mas colore texto com
significados especiais. Para a shell, isso significa saída e erros da
shell, saída e erros do usuário. Para código Python, no prompt da
shell ou em um editor, isso significa palavras-chave, nomes de classes
e funções embutidas, nomes seguidos de "class" e "def", strings e
comentários. Para qualquer janela de texto, são o cursor (quando
presente), texto encontrado (quando possível) e texto selecionado.

O IDLE também destaca as palavras reservadas suaves "match", "case", e
"_" em declarações de correspondência de padrões. No entanto, este
destaque não é perfeito e estará incorreto em alguns casos raros,
incluindo alguns "_"-s em padrões de "case".

A coloração do texto é feita em segundo plano, por isso,
ocasionalmente, é possível ver partes do texto sem cor.  Para alterar
o esquema de cores, use a aba  Highlighting na caixa de diálogo
Configure IDLE. A marcação de linhas de ponto de interrupção do
depurador no editor e texto em pop-ups e caixas de diálogo não é
configurável pelo usuário.


Inicialização e execução de código
==================================

Ao iniciar com a opção "-s", o IDLE executará o arquivo referenciado
pelas variáveis de ambiente "IDLESTARTUP" ou "PYTHONSTARTUP". O IDLE
verifica primeiro "IDLESTARTUP"; se "IDLESTARTUP" estiver presente, o
arquivo referenciado é executado. Se "IDLESTARTUP" não estiver
presente, o IDLE verifica "PYTHONSTARTUP". Os arquivos referenciados
por estas variáveis de ambiente são locais convenientes para armazenar
funções que são usadas frequentemente a partir da shell do IDLE, ou
para executar instruções de importação para importar módulos comuns.

Além disso, "Tk" também carrega um arquivo de inicialização se estiver
presente. Note que o arquivo Tk é carregado incondicionalmente. Este
arquivo adicional é ".Idle.py" e é procurado no diretório pessoal do
usuário. As instruções neste arquivo serão executadas no espaço de
nomes do Tk, por isso este arquivo não é útil para importar funções a
serem usadas a partir da console Python do IDLE.


Uso na linha de comando
-----------------------

O IDLE pode ser invocado a partir da linha de comandos com várias
opções. A sintaxe geral é:

   python -m idlelib [opções] [arquivo ...]

As seguintes opções estão disponíveis:

-c <command>

   Executa o comando Python especificado na janela shell. Por exemplo,
   passe "-c "print('Hello, World!')"". No Windows, as aspas externas
   devem ser aspas duplas como mostrado.

-d

   Ativa o depurador e abre a janela shell.

-e

   Abre uma janela de editor.

-h

   Exibe uma mensagem de ajuda com combinações legais de opções e sai.

-i

   Abre uma janela shell.

-r <file>

   Executa o arquivo especificado na janela shell.

-s

   Executa o arquivo de inicialização (como definido pelas variáveis
   de ambiente "IDLESTARTUP" ou "PYTHONSTARTUP") antes de abrir a
   janela shell.

-t <title>

   Define o título da janela shell.

-

   Lê e executa a entrada padrão na janela shell. Esta opção deve ser
   a última antes de quaisquer argumentos.

Se forem fornecidos argumentos:

* Se "-", "-c" ou "-r" for usado, todos os argumentos são colocados em
  "sys.argv[1:]", e "sys.argv[0]" é definido para "''", "'-c'" ou
  "'-r'" respectivamente. Nenhuma janela de editor é aberta, mesmo que
  essa seja a padrão no diálogo *Options*.

* Caso contrário, os argumentos são tratados como arquivos a serem
  abertos para edição, e "sys.argv" reflete os argumentos passados ao
  próprio IDLE.


Falha na inicialização
----------------------

IDLE usa um soquete para comunicação entre o processo GUI do IDLE e o
processo de execução de código do usuário. Uma conexão deve ser
estabelecida sempre que a Shell inicia ou reinicia. (Este último é
indicado por uma linha divisória que diz 'RESTART'). Se o processo do
usuário falhar ao conectar-se ao processo GUI, geralmente exibe uma
caixa de erro "Tk" com uma mensagem 'não é possível conectar' que
direciona o usuário. Em seguida, sai.

Uma falha específica de conexão em sistemas Unix resulta de regras de
mascaramento mal configuradas em algum lugar na configuração de rede
do sistema. Quando o IDLE é iniciado a partir de um terminal, você
verá uma mensagem começando com "** Invalid host:". O valor válido é
"127.0.0.1 (idlelib.rpc.LOCALHOST)". Você pode conferir com
"tcpconnect -irv 127.0.0.1 6543" numa janela de terminal e "tcplisten
<same args>" noutra.

Uma causa comum de falha é um arquivo escrito pelo usuário com o mesmo
nome que um módulo da biblioteca padrão, como *random.py* e
*tkinter.py*. Quando tal arquivo está localizado no mesmo diretório
que um arquivo que está prestes a ser executado, o IDLE não consegue
importar o arquivo da biblioteca padrão. A solução atual é renomear o
arquivo do usuário.

Embora menos comum do que no passado, um programa antivírus ou
firewall pode interromper a conexão. Se o programa não puder ser
configurado para permitir a conexão, então deve ser desativado para
que o IDLE funcione. É seguro permitir esta conexão interna porque
nenhum dado é visível em portas externas. Um problema semelhante é uma
configuração errada de rede que bloqueia conexões.

Problemas na instalação do Python podem, por vezes, impedir o
funcionamento do IDLE: versões diferentes podem entrar em conflito, ou
uma instalação específica pode exigir privilégios de administrador. Se
não for possível resolver o conflito, ou caso o usuário não possa ou
não queira executar o programa como administrador, a solução mais
simples pode ser remover o Python completamente e realizar uma nova
instalação.

Um processo zombie pythonw.exe pode ser um problema. No Windows, use o
Gerenciador de Tarefas para verificar se existe um e pará-lo, se
houver. Às vezes, um reinício iniciado por uma falha do programa ou
Interrupção de Teclado (control-C) pode falhar ao conectar. Descartar
a caixa de erro ou usar Reiniciar Shell no menu Shell pode resolver um
problema temporário.

Quando o IDLE inicia pela primeira vez, ele tenta ler os arquivos de
configuração do usuário em "~/.idlerc/" (~ é o diretório pessoal). Se
houver um problema, uma mensagem de erro deve ser exibida. Deixando de
lado falhas aleatórias no disco, isto pode ser evitado nunca editando
os arquivos manualmente. Em vez disso, use a caixa de diálogo de
configuração, em Options. Uma vez que haja um erro num arquivo de
configuração do usuário, a melhor solução pode ser apagá-lo e começar
de novo com a caixa de diálogo de configurações.

Se o IDLE sair sem mensagem e não foi iniciado a partir de um console,
tente iniciá-lo a partir de um console ou terminal ("python -m
idlelib") e veja se isto resulta numa mensagem de erro.

Em sistemas baseados em Unix com tcl/tk mais antigo que "8.6.11" (veja
"About IDLE"), certos caracteres de certas fontes podem causar uma
falha tk com uma mensagem para o terminal. Isto pode acontecer se
iniciar o IDLE para editar um arquivo com tal caractere ou mais tarde
ao introduzir tal caractere. Se não puder atualizar tcl/tk, então
reconfigure o IDLE para usar uma fonte que funcione melhor.


Execução de código do usuário
-----------------------------

Com raras exceções, o resultado da execução de código Python com o
IDLE destina-se a ser o mesmo que executar o mesmo código pelo método
padrão, diretamente com o Python numa console de sistema em modo de
texto ou janela de terminal. No entanto, a interface e operação
diferentes afetam ocasionalmente os resultados visíveis. Por exemplo,
"sys.modules" começa com mais entradas, e "threading.active_count()"
retorna 2 em vez de 1.

Por padrão, o IDLE executa o código do usuário em um processo de SO
separado em vez de no processo de interface do usuário que executa a
shell e o editor. No processo de execução, substitui "sys.stdin",
"sys.stdout" e "sys.stderr" por objetos que obtêm entrada e enviam
saída para a janela Shell. Os valores originais armazenados em
"sys.__stdin__", "sys.__stdout__" e "sys.__stderr__" não são
alterados, mas podem ser "None".

Enviar saída de impressão  de um processo para um componente de texto
em outro processo é mais lento do que imprimir para um terminal de
sistema no mesmo processo. Isto tem mais efeito ao imprimir vários
argumentos, pois a string para cada argumento, cada separador e a nova
linha são enviados separadamente. Para desenvolvimento, isto
geralmente não é um problema, mas se quiser imprimir mais rápido no
IDLE, formate e junte tudo o que quer exibir e depois imprima uma
única string. Tanto strings de formato como "str.join()" podem ajudar
a combinar campos e linhas.

As substituições de fluxo padrão do IDLE não são herdadas por
subprocessos criados no processo de execução, quer diretamente pelo
código do usuário ou por módulos como multiprocessing. Se tais
subprocessos usarem "input" de sys.stdin ou "print" ou "write" para
sys.stdout ou sys.stderr, o IDLE deve ser iniciado numa janela de
linha de comandos. (No Windows, use "python" ou "py" em vez de
"pythonw" ou "pyw".) O subprocesso secundário será então anexado a
essa janela para entrada e saída.

Se "sys" for redefinido pelo código do usuário, como com
"importlib.reload(sys)", as alterações do IDLE são perdidas e a
entrada do teclado e a saída para a tela não funcionarão corretamente.

Quando a Shell tem o foco, controla o teclado e a tela. Isto é
normalmente transparente, mas funções que acessam diretamente ao
teclado e à tela não funcionarão. Isto inclui funções específicas do
sistema que determinam se uma tecla foi pressionada e, em caso
afirmativo, qual.

O código IDLE em execução no processo de execução adiciona quadros à
pilha de chamadas que não estariam lá de outra forma. O IDLE envolve
"sys.getrecursionlimit" e "sys.setrecursionlimit" para reduzir o
efeito dos quadros de pilha adicionais.

Quando o código do usuário levanta SystemExit diretamente ou chamando
sys.exit, o IDLE retorna a um prompt Shell em vez de sair.


Saída do usuário na Shell
-------------------------

Quando um programa produz texto, o resultado é determinado pelo
dispositivo de saída correspondente. Quando o IDLE executa código do
usuário, "sys.stdout" e "sys.stderr" estão ligados à área de exibição
da Shell do IDLE. Algumas das suas funcionalidades são herdadas do
widget de texto Tk subjacente. Outras são adições programadas. Onde
importa, a Shell é concebida para desenvolvimento em vez de execuções
de produção.

Por exemplo, a Shell nunca descarta saída. Um programa que envia saída
ilimitada para a Shell acabará por encher a memória, resultando num
erro de memória. Em contraste, algumas janelas de texto do sistema
mantêm apenas as últimas n linhas de saída. Um console Windows, por
exemplo, mantém um número configurável pelo utilizador de 1 a 9999
linhas, com 300 como padrão.

Um componente de texto Tk, e portanto a Shell do IDLE, exibe
caracteres (pontos de código) no subconjunto BMP (do inglês, Basic
Multilingual Plane ou Plano Multilíngue Básico) do Unicode. Quais
caracteres são exibidos com um glifo adequado e quais com uma caixa de
substituição depende do sistema operacional e das fontes instaladas.
Os caracteres de tabulação fazem com que o texto seguinte comece após
a próxima paragem de tabulação. (Ocorrem a cada 8 'caracteres'). Os
caracteres de nova linha fazem com que o texto seguinte apareça numa
nova linha. Outros caracteres de controle são ignorados ou exibidos
como um espaço, uma caixa ou outra coisa, dependendo do sistema
operacional e da fonte. (Mover o cursor de texto através de tal saída
com as teclas de seta pode exibir algum comportamento de espaçamento
surpreendente.)

   >>> s = 'a\tb\a<\x02><\r>\bc\nd'  # Contém 22 caracteres.
   >>> len(s)
   14
   >>> s  # Exibe repr(s)
   'a\tb\x07<\x02><\r>\x08c\nd'
   >>> print(s, end='')  # Exibe s como está.
   # Resultado varia conforme SO e fonte.  Experimente.

A função "repr" é usada para eco interativo de valores de expressão.
Retorna uma versão alterada da string de entrada na qual códigos de
controle, alguns pontos de código BMP e todos os pontos de código não-
BMP são substituídos por códigos de escape. Como demonstrado acima,
permite identificar os caracteres numa string, independentemente de
como são exibidos.

A saída normal e de erro são geralmente mantidas separadas (em linhas
separadas) da entrada de código e uma da outra. Cada uma recebe cores
de destaque diferentes.

Para tracebacks (situação da pilha de execução) de SyntaxError, a
marcação normal '^' onde o erro foi detectado é substituída pela
coloração do texto com um realce de erro. Quando o código executado a
partir de um arquivo causa outras exceções, você pode clicar com o
botão direito numa linha de traceback para saltar para a linha
correspondente num editor IDLE. O arquivo será aberto se necessário.

A Shell tem uma funcionalidade especial para comprimir linhas de saída
sob uma etiqueta 'Squeezed text'. Isto é feito automaticamente para
saída superior a N linhas (N = 50 por padrão). N pode ser alterado na
seção Shell Preferences da página Shell/Ed da caixa de diálogo de
Settings. A saída com menos linhas pode ser comprimida clicando com o
botão direito na saída. Isto pode ser útil para linhas suficientemente
longas para reduzir a rolagem.

A saída comprimida é expandida no local ao clicar duas vezes na
etiqueta. Também pode ser enviada para a área de transferência ou uma
janela de visualização separada clicando com o botão direito na
etiqueta.


Developing tkinter applications
-------------------------------

IDLE is intentionally different from standard Python in order to
facilitate development of tkinter programs.  Enter "import tkinter as
tk; root = tk.Tk()" in standard Python and nothing appears.  Enter the
same in IDLE and a tk window appears.  In standard Python, one must
also enter "root.update()" to see the window.  IDLE does the
equivalent in the background, about 20 times a second, which is about
every 50 milliseconds. Next enter "b = tk.Button(root, text='button');
b.pack()".  Again, nothing visibly changes in standard Python until
one enters "root.update()".

Most tkinter programs run "root.mainloop()", which usually does not
return until the tk app is destroyed.  If the program is run with
"python -i" or from an IDLE editor, a ">>>" shell prompt does not
appear until "mainloop()" returns, at which time there is nothing left
to interact with.

When running a tkinter program from an IDLE editor, one can comment
out the mainloop call.  One then gets a shell prompt immediately and
can interact with the live application.  One just has to remember to
re-enable the mainloop call when running in standard Python.


Running without a subprocess
----------------------------

By default, IDLE executes user code in a separate subprocess via a
socket, which uses the internal loopback interface.  This connection
is not externally visible and no data is sent to or received from the
internet. If firewall software complains anyway, you can ignore it.

If the attempt to make the socket connection fails, Idle will notify
you. Such failures are sometimes transient, but if persistent, the
problem may be either a firewall blocking the connection or
misconfiguration of a particular system.  Until the problem is fixed,
one can run Idle with the -n command line switch.

If IDLE is started with the -n command line switch it will run in a
single process and will not create the subprocess which runs the RPC
Python execution server.  This can be useful if Python cannot create
the subprocess or the RPC socket interface on your platform.  However,
in this mode user code is not isolated from IDLE itself.  Also, the
environment is not restarted when Run/Run Module (F5) is selected.  If
your code has been modified, you must reload() the affected modules
and re-import any specific items (e.g. from foo import baz) if the
changes are to take effect.  For these reasons, it is preferable to
run IDLE with the default subprocess if at all possible.

Descontinuado desde a versão 3.4.


Ajuda e preferências
====================


Help sources
------------

Help menu entry "IDLE Help" displays a formatted html version of the
IDLE chapter of the Library Reference.  The result, in a read-only
tkinter text window, is close to what one sees in a web browser.
Navigate through the text with a mousewheel, the scrollbar, or up and
down arrow keys held down. Or click the TOC (Table of Contents) button
and select a section header in the opened box.

Help menu entry "Python Docs" opens the extensive sources of help,
including tutorials, available at "docs.python.org/x.y", where 'x.y'
is the currently running Python version.  If your system has an off-
line copy of the docs (this may be an installation option), that will
be opened instead.

Selected URLs can be added or removed from the help menu at any time
using the General tab of the Configure IDLE dialog.


Configurando preferências
-------------------------

The font preferences, highlighting, keys, and general preferences can
be changed via Configure IDLE on the Option menu. Non-default user
settings are saved in a ".idlerc" directory in the user's home
directory.  Problems caused by bad user configuration files are solved
by editing or deleting one or more of the files in ".idlerc".

On the Font tab, see the text sample for the effect of font face and
size on multiple characters in multiple languages.  Edit the sample to
add other characters of personal interest.  Use the sample to select
monospaced fonts.  If particular characters have problems in Shell or
an editor, add them to the top of the sample and try changing first
size and then font.

On the Highlights and Keys tab, select a built-in or custom color
theme and key set.  To use a newer built-in color theme or key set
with older IDLEs, save it as a new custom theme or key set and it well
be accessible to older IDLEs.


IDLE on macOS
-------------

Under System Preferences: Dock, one can set "Prefer tabs when opening
documents" to "Always".  This setting is not compatible with the
tk/tkinter GUI framework used by IDLE, and it breaks a few IDLE
features.


Extensions
----------

IDLE contains an extension facility.  Preferences for extensions can
be changed with the Extensions tab of the preferences dialog. See the
beginning of config-extensions.def in the idlelib directory for
further information.  The only current default extension is zzdummy,
an example also used for testing.


idlelib --- implementation of IDLE application
==============================================

**Source code:** Lib/idlelib

======================================================================

The Lib/idlelib package implements the IDLE application.  See the rest
of this page for how to use IDLE.

The files in idlelib are described in idlelib/README.txt.  Access it
either in idlelib or click Help => About IDLE on the IDLE menu.  This
file also maps IDLE menu items to the code that implements the item.
Except for files listed under 'Startup', the idlelib code is 'private'
in sense that feature changes can be backported (see **PEP 434**).
