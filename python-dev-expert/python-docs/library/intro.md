Introdução
**********

A biblioteca padrão consiste em uma coleção de módulos. Há muitas
formas de dissecar essa coleção. A maioria dos módulos são escritos em
Python, mas alguns são escritos em C. Todos podem ser importados em
seu programa para adicionar funcionalidade Alguns módulos fornecem
interfaces que são muito específicas do Python, como imprimir um stack
trace (situação da pilha de execução); alguns fornecem interfaces que
são específicas para um sistema operacional em particular, tais como
acessar hardware específico; outros fornecem interfaces que são
específicas de um domínio de aplicação em particular, como
desenvolvimento web. Alguns módulos estão disponíveis em todas as
versões do Python; outros estão apenas disponíveis quando o sistema
subjacente suporta ou necessita deles; e ainda outros estão
disponíveis apenas quando uma opção de configuração em particular foi
escolhida no momento em que o Python foi compilado e instalado.

Se você começar a ler este manual do início, e pular para o próximo
capítulo quando estiver entediado, você terá uma visão geral razoável
dos módulos disponíveis e áreas de aplicação que são suportadas pela
biblioteca Python. É claro, você não *tem* que ler como se fosse um
romance --- você também pode navegar pela tabela de conteúdos (no
início do manual), ou procurar por uma função, módulo ou termo
específicos no índice (na parte final). E finalmente, se você gostar
de aprender sobre assuntos diversos, você pode escolher uma página
aleatória e leia uma seção ou duas. Independente da ordem na qual você
leia as seções deste manual, ajuda primeiro ler Funções embutidas, já
que o resto desta seção requer familiaridade com este material.

Ver também:

  As funções e classes embutidas (que podem ser usadas sem uma
  instrução "import") estão descritas em Referência da bibliotecas
  embutidas do Python.


Observações sobre disponibilidade
=================================

* Uma observação "Disponibilidade: Unix" significa que essa função é
  comumente encontrada em sistemas Unix. Não faz nenhuma reivindicação
  sobre sua existência em um sistema operacional específico.

* Caso não seja definido separadamente, todas as funções que se
  definem como "Disponibilidade: Unix" são suportadas no macOS, IOS e
  Android, todas construídas em um Unix core.

* Se uma nota de disponibilidade contiver uma versão mínima do Kernel
  e uma versão mínima da libc, ambas as condições deverão ser
  atendidas. Por exemplo, um recurso com a observação
  *Disponibilidade: Linux >= 3.17 com glibc >= 2.27* requer Linux 3.17
  ou mais recente e glibc 2.27 ou mais recente.


Plataformas WebAssembly
-----------------------

As plataformas WebAssembly "wasm32-emscripten" (Emscripten) e
"wasm32-wasi" (WASI) fornecem um subconjunto de APIs POSIX. Os tempos
de execução e navegadores do WebAssembly são colocados em área
restrita e têm acesso limitado ao host e aos recursos externos.
Qualquer módulo de biblioteca padrão do Python que usa processos,
encadeamento, rede, sinais ou outras formas de comunicação entre
processos (IPC) não está disponível ou pode não funcionar como em
outros sistemas semelhantes ao Unix. E/S de arquivo, sistema de
arquivos e funções relacionadas à permissão do Unix também são
restritas. Emscripten não permite bloqueio de E/S. Outras operações de
bloqueio como "sleep()" bloqueiam o laço de eventos do navegador.

As propriedades e o comportamento do Python em plataformas WebAssembly
dependem da versão Emscripten-SDK ou WASI-SDK, tempos de execução WASM
(navegador, NodeJS, wasmtime) e sinalizadores de tempo de construção
do Python. WebAssembly, Emscripten e WASI são padrões em evolução;
alguns recursos como rede podem ser suportados no futuro.

Para Python no navegador, os usuários devem considerar Pyodide ou
PyScript. O PyScript é construído sobre o Pyodide, que por sua vez é
construído sobre o CPython e o Emscripten. O Pyodide fornece acesso às
APIs JavaScript e DOM dos navegadores, bem como recursos de rede
limitados com as APIs "XMLHttpRequest" e "Fetch" do JavaScript.

* As APIs relacionadas a processo não estão disponíveis ou sempre
  falham com um erro. Isso inclui APIs que geram novos processos
  ("fork()", "execve()"), aguardam processos ("waitpid()"), enviam
  sinais ("kill()"), ou interagir com processos. O "subprocess" é
  importável, mas não funciona.

* O módulo "socket" está disponível, mas é limitado e se comporta de
  maneira diferente de outras plataformas. No Emscripten, os soquetes
  são sempre não bloqueantes e requerem código JavaScript adicional e
  auxiliares no servidor para intermediar TCP por meio de WebSockets;
  veja Emscripten Networking para mais informações. A primeira
  snapshot de preview do WASI permite apenas soquetes de um descritor
  de arquivo existente.

* Algumas funções são esboço que não fazem nada e sempre retornam
  valores definidos no código.

* As funções relacionadas a descritores de arquivo, permissões de
  arquivo, propriedade de arquivo e links são limitadas e não suportam
  algumas operações. Por exemplo, WASI não permite links simbólicos
  com nomes de arquivo absolutos.


Plataformas móveis
------------------

O Android e o IOS são em linhas gerais sistemas operacionais POSIX.
File I/O, socket handling, e threading se comportam como em qualquer
sistema operacional POSIX. Entretanto, existem diversas diferenças:

* Plataformas móveis podem usar o Python apenas no modo "incorporado".
  Não existe um Python REPL, e não existe possibilidade para usar
  executáveis em separado como **python** ou **pip**. Para adicionar
  código Python para seu aplicativo móvel, você deve usar a API de
  incorporação do Python. Para maiores detalhes veja Utilizando Python
  no Android e Usando Python no iOS.

* Subprocessos:

  * No Android, criar subprocessos é possível mas oficialmente sem
    suporte. Em particular, Android não oferece suporte para nenhuma
    parte da API System V IPC, assim "multiprocessing" não está
    disponível.

  * Uma aplicação de iOS não pode usar qualquer forma de
    subprocessamento, multiprocessamento ou comunicação entre
    processos. Se uma aplicação de iOS tentar criar um subprocesso, o
    processo que cria o subprocesso será travado ou encerrado
    abruptamente. Uma aplicação de iOS não tem visibilidade de outras
    aplicações em execução, nem capacidade de comunicação com outras
    aplicações em execução, fora das APIs específicas do iOS que
    existem para essa finalidade.

* Aplicativos móveis possuem acesso limitado a recursos do sistema
  (como o relógio do sistema). Esses recursos serão em sua maioria
  apenas *leitura*, e tentativas de modificar esses recusos geralmente
  falhará.

* Entrada e saída do console:

  * No Android, o "stdout" e o "stderr" nativos não estão conectados a
    nada, então o Python instala seus próprios fluxos que redirecionam
    mensagens para o log do sistema. Esses podem ser vistos sob a tags
    "python.stdout" e "python.stderr", respectivamente.

  * As aplicações de iOS têm um conceito limitado de saída do console.
    "stdout" e "stderr" *existem*, e o conteúdo escrito em "stdout" e
    "stderr" será visível nos registros (logs) quando executado no
    Xcode, mas este conteúdo *não* será gravado no registro do
    sistema. Se um usuário que instalou sua aplicação fornecer os
    registros da aplicação como ajuda de diagnóstico, eles não
    incluirão nenhum detalhe escrito em "stdout" ou "stderr".

  * As aplicações para dispositivos móveis não têm nenhum conceito de
    "stdin". Embora essas aplicações possam exibir um teclado na tele,
    este é um recurso de software, não algo anexado ao "stdin".

    Como consequência, módulos Python que envolvem manipulação de
    console (como "curses" e "readline") não estão disponíveis em
    plataformas móveis.
