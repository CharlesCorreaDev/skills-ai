"webbrowser" --- Controlador de navegador web conveniente
*********************************************************

**Código-fonte:** Lib/webbrowser.py

======================================================================

The "webbrowser" module provides a high-level interface to allow
displaying web-based documents to users. Under most circumstances,
simply calling the "open()" function from this module will do the
right thing.

No Unix, navegadores gráficos são preferidos no X11, mas navegadores
em modo texto serão usados se navegadores gráficos não estiverem
disponíveis ou um display X11 não estiver disponível. Se navegadores
em modo texto forem usados, o processo de chamada será bloqueado até
que o usuário saia do navegador.

Se a variável de ambiente "BROWSER" existir, ela será interpretada
como a lista separada por "os.pathsep" de navegadores a serem tentados
antes dos padrões da plataforma. Quando o valor de uma parte da lista
contém a string "%s", então ela é interpretada como uma linha de
comando literal do navegador a ser usada com o argumento URL
substituído por "%s"; se o valor for uma única palavra que se refere a
um dos navegadores já registrados, este navegador será adicionado à
frente da lista de pesquisa; se a parte não contiver "%s", ela será
simplesmente interpretada como o nome do navegador a ser iniciado. [1]

Alterado na versão 3.14: A variável "BROWSER" agora também pode ser
usada para reordenar a lista de padrões da plataforma. Isso é
particularmente útil no macOS, onde os padrões da plataforma não se
referem às ferramentas de linha de comando em "PATH".

Para plataformas não-Unix, ou quando um navegador remoto estiver
disponível no Unix, o processo de controle não esperará que o usuário
termine de usar o navegador, mas permitirá que o navegador remoto
mantenha suas próprias janelas na tela. Se os navegadores remotos não
estiverem disponíveis no Unix, o processo de controle iniciará um novo
navegador e aguardará.

On iOS, the "BROWSER" environment variable, as well as any arguments
controlling autoraise, browser preference, and new tab/window creation
will be ignored. Web pages will *always* be opened in the user's
preferred browser, in a new tab, with the browser being brought to the
foreground. The use of the "webbrowser" module on iOS requires the
"ctypes" module. If "ctypes" isn't available, calls to "open()" will
fail.


Interface de linha de comando
=============================

O script **webbrowser** pode ser usado como uma interface de linha de
comando para o módulo. Ele aceita uma URL como argumento. Ele aceita
os seguintes parâmetros opcionais:

-n, --new-window

   Abre a URL em uma nova janela do navegador, se possível.

-t, --new-tab

   Abre a URL em uma nova aba do navegador.

As opções são, naturalmente, mutuamente exclusivas. Exemplo de uso:

   python -m webbrowser -t "https://www.python.org"

Disponibilidade: not WASI, not Android.

A seguinte exceção é definida:

exception webbrowser.Error

   Exceção levantada quando ocorre um erro de controle do navegador.

As seguintes funções estão definidas:

webbrowser.open(url, new=0, autoraise=True)

   Exibe *url* usando o navegador padrão. Se *new* for 0, o *url* será
   aberto na mesma janela do navegador, se possível. Se *new* for 1,
   uma nova janela do navegador será aberta, se possível. Se *new* for
   2, uma nova página do navegador ("aba" ou "guia") será aberta, se
   possível. Se *autoraise* for "True", a janela será levantada, se
   possível (observe que, em muitos gerenciadores de janelas, isso
   ocorrerá independentemente da configuração dessa variável).

   Retorna "True" se um navegador foi iniciado com sucesso, "False"
   caso contrário.

   Note que em algumas plataformas, tentar abrir um nome de arquivo
   usando esta função pode funcionar e iniciar o programa associado do
   sistema operacional. No entanto, isso não é suportado nem portátil.

   Levanta um evento de auditoria "webbrowser.open" com o argumento
   "url".

webbrowser.open_new(url)

   Abre *url* em uma nova janela do navegador padrão, se possível;
   caso contrário, abre *url* na única janela do navegador.

   Retorna "True" se um navegador foi iniciado com sucesso, "False"
   caso contrário.

webbrowser.open_new_tab(url)

   Abre  *url* em uma nova página ("aba" ou "guia") do navegador
   padrão, se possível, caso contrário, equivalente a "open_new()".

   Retorna "True" se um navegador foi iniciado com sucesso, "False"
   caso contrário.

webbrowser.get(using=None)

   Retorna um objeto controlador para o tipo de navegador *using*. Se
   *using* for "None", retorna um controlador para um navegador padrão
   apropriado para o ambiente do chamador.

webbrowser.register(name, constructor, instance=None, *, preferred=False)

   Registra o tipo de navegador *name*. Uma vez que um tipo de
   navegador é registrado, a função "get()" pode retornar um
   controlador para esse tipo de navegador. Se *instance* não for
   fornecido, ou for "None", *constructor* será chamado sem parâmetros
   para criar uma instância quando necessário. Se *instance* for
   fornecido, *constructor* nunca será chamado, e pode ser "None".

   Definir *preferred* como "True" torna este navegador um resultado
   preferencial para uma chamada "get()" sem argumento. Caso
   contrário, este ponto de entrada só é útil se você planeja definir
   a variável "BROWSER" ou chamar "get()" com um argumento não vazio
   que corresponda ao nome de um manipulador que você declarar.

   Alterado na versão 3.7: Parâmetro somente-nomeado *preferred* foi
   adicionado.

Vários tipos de navegadores são predefinidos. Esta tabela fornece os
nomes de tipos que podem ser passados para a função "get()" e as
instanciações correspondentes para as classes do controlador, todas
definidas neste módulo.

+--------------------------+-------------------------------------------+---------+
| Nome do tipo             | Nome da classe                            | Notas   |
|==========================|===========================================|=========|
| "'mozilla'"              | "Mozilla('mozilla')"                      |         |
+--------------------------+-------------------------------------------+---------+
| "'firefox'"              | "Mozilla('mozilla')"                      |         |
+--------------------------+-------------------------------------------+---------+
| "'epiphany'"             | "Epiphany('epiphany')"                    |         |
+--------------------------+-------------------------------------------+---------+
| "'kfmclient'"            | "Konqueror()"                             | (1)     |
+--------------------------+-------------------------------------------+---------+
| "'konqueror'"            | "Konqueror()"                             | (1)     |
+--------------------------+-------------------------------------------+---------+
| "'kfm'"                  | "Konqueror()"                             | (1)     |
+--------------------------+-------------------------------------------+---------+
| "'opera'"                | "Opera()"                                 |         |
+--------------------------+-------------------------------------------+---------+
| "'links'"                | "GenericBrowser('links')"                 |         |
+--------------------------+-------------------------------------------+---------+
| "'elinks'"               | "Elinks('elinks')"                        |         |
+--------------------------+-------------------------------------------+---------+
| "'lynx'"                 | "GenericBrowser('lynx')"                  |         |
+--------------------------+-------------------------------------------+---------+
| "'w3m'"                  | "GenericBrowser('w3m')"                   |         |
+--------------------------+-------------------------------------------+---------+
| "'windows-default'"      | "WindowsDefault"                          | (2)     |
+--------------------------+-------------------------------------------+---------+
| "'macos'"                | "MacOS('default')"                        | (3)     |
+--------------------------+-------------------------------------------+---------+
| "'safari'"               | "MacOS('safari')"                         | (3)     |
+--------------------------+-------------------------------------------+---------+
| "'chrome'"               | "MacOS('google chrome')"                  | (3)     |
+--------------------------+-------------------------------------------+---------+
| "'firefox'"              | "MacOS('firefox')"                        | (3)     |
+--------------------------+-------------------------------------------+---------+
| "'google-chrome'"        | "Chrome('google-chrome')"                 |         |
+--------------------------+-------------------------------------------+---------+
| "'chromium'"             | "Chromium('chromium')"                    |         |
+--------------------------+-------------------------------------------+---------+
| "'chromium-browser'"     | "Chromium('chromium-browser')"            |         |
+--------------------------+-------------------------------------------+---------+
| "'iosbrowser'"           | "IOSBrowser"                              | (4)     |
+--------------------------+-------------------------------------------+---------+

Notas:

1. "Konqueror" é o gerenciador de arquivos para o ambiente de desktop
   KDE para Unix, e só faz sentido usar se estiver no KDE. Alguma
   maneira de detectar o KDE de forma confiável seria legal; a
   variável "KDEDIR" não é suficiente. Note também que o nome "kfm" é
   usado mesmo ao usar o comando **konqueror** com o KDE 2 --- a
   implementação seleciona a melhor estratégia para executar o
   Konqueror.

2. Somente em plataformas Windows.

3. Somente no macOS.

4. Somente no iOS.

Adicionado na versão 3.2: Uma nova classe "MacOSXOSAScript" foi
adicionada e é usada no Mac em vez da classe anterior "MacOSX". Isso
adiciona suporte para abrir navegadores que não estão definidos como
padrão do sistema operacional no momento.

Adicionado na versão 3.3: Foi adicionado suporte para Chrome/Chromium.

Alterado na versão 3.12: O suporte para vários navegadores obsoletos
foi removido. Os navegadores removidos incluem Grail, Mosaic,
Netscape, Galeon, Skipstone, Iceape e Firefox versões 35 e abaixo.

Alterado na versão 3.13: Foi adicionado suporte para iOS.

Adicionado na versão 3.15: "MacOS" has been added as a replacement for
"MacOSXOSAScript", opening browsers via **/usr/bin/open** instead of
**osascript**.

Descontinuado desde a versão 3.15, será removido na versão 3.17:
"MacOSXOSAScript" is deprecated in favour of "MacOS". Using
**/usr/bin/open** instead of **osascript** is a security and usability
improvement: **osascript** may be blocked on managed systems due to
its abuse potential as a general-purpose scripting interpreter.

Aqui estão alguns exemplos simples:

   url = 'https://docs.python.org/'

   # Abre a URL em uma nova aba, se uma janela do navegador já estiver aberta.
   webbrowser.open_new_tab(url)

   # Abre a URL em uma nova janela, aumentando a janela se possível.
   webbrowser.open_new(url)


Objetos controladores de navegador
==================================

Os controladores de navegador fornecem o atributo "name" e os três
métodos a seguir que são paralelos às funções de conveniência em nível
de módulo:

controller.name

   Nome dependente do sistema para o navegador.

controller.open(url, new=0, autoraise=True)

   Exibe *url* usando o navegador manipulado por este controlador. Se
   *new* for 1, uma nova janela do navegador será aberta, se possível.
   Se *new* for 2, uma nova página do navegador ("aba" ou "guia") será
   aberta, se possível.

controller.open_new(url)

   Abre *url* em uma nova janela do navegador manipulado por este
   controlador, se possível, caso contrário, abra *url* na única
   janela do navegador. Apelido para "open_new()".

controller.open_new_tab(url)

   Abre *url* em uma nova página ("aba" ou "guia") do navegador
   manipulado por este controlador, se possível, caso contrário,
   equivalente a "open_new()".

-[ Notas de rodapé ]-

[1] Executáveis nomeados aqui sem um caminho completo serão
    pesquisados nos diretórios fornecidos na variável de ambiente
    "PATH".
