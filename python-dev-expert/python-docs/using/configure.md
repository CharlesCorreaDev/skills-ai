3. Configurando o Python
************************


3.1. Requisitos de construção
=============================

Para construir o CPython, você precisará de:

* Um compilador C11. Não são necessários recursos opcionais do C11.

* No Windows, é necessário o Microsoft Visual Studio 2017 ou
  posterior.

* Suporte para números de ponto flutuante do IEEE 754 e Not-a-Number
  (NaN) de ponto flutuante.

* Suporte a threads.

Alterado na versão 3.5: No Windows, o Visual Studio 2015 ou posterior
agora é obrigatório.

Alterado na versão 3.6: Alguns recurso do C99, como as funções
"<stdint.h>" e "static inline", agora são obrigatórios.

Alterado na versão 3.7: Suporte a threads agora é obrigatório.

Alterado na versão 3.11: Compilador C11, suporte a IEEE 754 e NaN
agora são necessários. No Windows, é necessário o Visual Studio 2017
ou posterior.

Veja também **PEP 7** "Guia de estilo para código C" e **PEP 11**
"Suporte do CPython a plataformas".


3.1.1. Requisitos para módulos opcionais
----------------------------------------

Alguns *módulos opcionais* da biblioteca padrão exigem que bibliotecas
de terceiros estejam instaladas para o desenvolvimento (por exemplo,
os arquivos de cabeçalho devem estar disponíveis).

Requisitos ausentes são relatados na saída do comando "configure".
Módulos que estão faltando devido a dependências ausentes são listados
perto do final da saída do comando "make", às vezes usando um nome
interno, por exemplo, "_ctypes" para o módulo "ctypes".

Se você distribuir um interpretador do CPython sem módulos opcionais,
é uma boa prática avisar os usuários, que geralmente esperam que os
módulos da biblioteca padrão estejam disponíveis.

As dependências para construir módulos opcionais são:

+-----------------------------------+-----------------------------------+-----------------------------------+
| Dependência                       | Versão mínima                     | Módulo Python                     |
|===================================|===================================|===================================|
| libbz2                            |                                   | "bz2"                             |
+-----------------------------------+-----------------------------------+-----------------------------------+
| libffi                            | 3.3.0 recomendada                 | "ctypes"                          |
+-----------------------------------+-----------------------------------+-----------------------------------+
| liblzma                           |                                   | "lzma"                            |
+-----------------------------------+-----------------------------------+-----------------------------------+
| libmpdec                          | 2.5.0                             | "decimal" [1]                     |
+-----------------------------------+-----------------------------------+-----------------------------------+
| libreadline ou libedit [2]        |                                   | "readline"                        |
+-----------------------------------+-----------------------------------+-----------------------------------+
| libuuid                           |                                   | "_uuid" [3]                       |
+-----------------------------------+-----------------------------------+-----------------------------------+
| ncurses [4]                       |                                   | "curses"                          |
+-----------------------------------+-----------------------------------+-----------------------------------+
| OpenSSL                           | [6]                               | "ssl", "hashlib" [5]              |
+-----------------------------------+-----------------------------------+-----------------------------------+
| SQLite                            | 3.15.2                            | "sqlite3"                         |
+-----------------------------------+-----------------------------------+-----------------------------------+
| Tcl/Tk                            | 8.5.12                            | "tkinter", IDLE, "turtle"         |
+-----------------------------------+-----------------------------------+-----------------------------------+
| zlib                              | 1.2.2.1                           | "zlib", "gzip", "ensurepip"       |
+-----------------------------------+-----------------------------------+-----------------------------------+
| zstd                              | 1.4.5                             | "compression.zstd"                |
+-----------------------------------+-----------------------------------+-----------------------------------+

[1] Se a biblioteca *libmpdec* não estiver disponível, o módulo
    "decimal" usará uma implementação em Python puro. Consulte "--
    with-system-libmpdec" para obter detalhes.

[2] Consulte "--with-readline" para escolher o backend do módulo
    "readline".

[3] O módulo "uuid" usa "_uuid" para gerar UUIDs "seguros". Consulte a
    documentação do módulo para obter detalhes.

[4] O módulo "curses" requer a biblioteca "libncurses" ou
    "libncursesw". O módulo "curses.panel" requer adicionalmente a
    biblioteca "libpanel" ou "libpanelw".

[5] Caso o OpenSSL não esteja disponível, o módulo "hashlib" utilizará
    implementações integradas de diversas funções de hash. Consulte a
    "--with-builtin-hashlib-hashes" para *forçar* o uso do OpenSSL.

[6] O OpenSSL 1.1.1 é a versão mínima necessária para a construção,
    mas essa série chegou ao fim de sua vida útil e não recebe mais
    correções de segurança públicas. Utilize a versão de correção
    (*patch release*) mais recente de uma série LTS atualmente
    suportada (consulte o OpenSSL Roadmap) ou o pacote fornecido pelo
    seu sistema operacional, caso esteja disponível. Outras
    bibliotecas que ofereçam uma API compatível com o OpenSSL 1.1.1 ou
    superior podem funcionar, mas não são oficialmente suportadas.

Note que a tabela não inclui todos os módulos opcionais; em
particular, módulos específicos da plataforma, como "winreg", não
estão listados aqui.

Ver também:

  * O devguide inclui uma lista completa das dependências necessárias
    para construir todos os módulos e instruções sobre como
    instalá-las em plataformas comuns.

  * A "--with-system-expat" permite a construir com uma biblioteca
    externa libexpat.

  * Opções para dependências de terceiros

Alterado na versão 3.1: Tcl/Tk versão 8.3.1 agora é obrigatório para
"tkinter".

Alterado na versão 3.5: Tcl/Tk versão 8.4 agora é obrigatório para
"tkinter".

Alterado na versão 3.7: OpenSSL 1.0.2 agora é obrigatório para
"hashlib" e "ssl".

Alterado na versão 3.10: OpenSSL 1.1.1 agora é obrigatório para
"hashlib" e "ssl". SQLite 3.7.15 agora é obrigatório para "sqlite3".

Alterado na versão 3.11: Tcl/Tk versão 8.5.12 agora é obrigatório para
"tkinter".

Alterado na versão 3.13: SQLite 3.15.2 agora é obrigatório para
"sqlite3".


3.2. Arquivos gerados
=====================

Para reduzir as dependências de construção, o código-fonte do Python
contém vários arquivos gerados. Comandos para regenerar todos os
arquivos gerados:

   make regen-all
   make regen-stdlib-module-names
   make regen-limited-abi
   make regen-configure

O arquivo "Makefile.pre.in" documenta os arquivos gerados, suas
entradas e ferramentas usadas para regenerá-los. Procure por alvos
"regen-*" de make.


3.2.1. Script configure
-----------------------

O comando "make regen-configure" regera o arquivo "aclocal.m4" e o
script "configure" usando o shell script "Tools/build/regen-
configure.sh", o qual usa um contêiner Ubuntu para obter as mesmas
versões de ferramentas e ter uma saída reproduzível.

O contêiner é opcional, o seguinte comando pode ser executado
localmente:

   autoreconf -ivf -Werror

Os arquivos gerados podem variar dependendo das versões exatas das
ferramentas utilizadas. O contêiner usado pelo CPython possui o
Autoconf 2.72, o "aclocal" do Automake 1.16.5 e o pkg-config 1.8.1.

Alterado na versão 3.13: O Autoconf 2.71 e o aclocal 1.16.5 agora são
usados para regenerar o arquivo "configure".

Alterado na versão 3.14: O Autoconf 2.72 agora é usado para regenerar
o arquivo "configure".


3.3. Opções de configuração
===========================

Liste todas as opções do "configure" usando:

   ./configure --help

Veja também o "Misc/SpecialBuilds.txt" na distribuição de código-fonte
do Python.


3.3.1. Opções gerais
--------------------

--enable-loadable-sqlite-extensions

   Suporte a extensões carregáveis no módulo de extensão "_sqlite" (o
   padrão é não) do módulo "sqlite3".

   Veja o método "sqlite3.Connection.enable_load_extension()" do
   módulo "sqlite3".

   Adicionado na versão 3.6.

--disable-ipv6

   Desabilita suporte a IPv6 (habilitado por padrão se houver
   suporte), veja o módulo "socket".

--enable-big-digits=[15|30]

   Define o tamanho em bits dos dígitos de "int" do Python: 15 ou 30
   bits.

   Por padrão, o tamanho dos dígitos é 30.

   Define "PYLONG_BITS_IN_DIGIT" para "15" ou "30".

   Veja "sys.int_info.bits_per_digit".

--with-suffix=SUFFIX

   Define o sufixo do executável do Python para *SUFFIX*.

   O sufixo padrão é ".exe" no Windows e macOS (executável
   "python.exe"), ".js" em nó Emscripten, ".html" em navegador
   Emscripten, ".wasm" em WASI e uma string vazia em outras
   plataformas (executável "python").

   Alterado na versão 3.11: O sufixo padrão na plataforma WASM é um
   entre ".js", ".html" ou ".wasm"

--with-tzpath=<list of absolute paths separated by pathsep>

   Seleciona o caminho de pesquisa de fuso horário padrão para
   "zoneinfo.TZPATH". Veja a Configuração de tempo de compilação do
   módulo "zoneinfo".

   Padrão: "/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zone
   info:/etc/zoneinfo".

   Veja o separador de caminhos "os.pathsep".

   Adicionado na versão 3.9.

--without-decimal-contextvar

   Constrói o módulo de extensão "_decimal" usando um contexto local
   de thread ao invés de um contexto local de corrotina (padrão), veja
   o módulo "decimal".

   Veja "decimal.HAVE_CONTEXTVAR" e o módulo "contextvars".

   Adicionado na versão 3.9.

--with-dbmliborder=<list of backend names>

   Substitui a ordem de verificação de backends de banco de dados para
   o módulo "dbm"

   Um valor válido é uma string separada por dois pontos (":") com os
   nomes de backend:

   * "ndbm";

   * "gdbm";

   * "bdb".

--without-c-locale-coercion

   Desabilita a coerção de localidade C para uma localidade baseada em
   UTF-8 (ativada por padrão).

   Não define a macro "PY_COERCE_C_LOCALE".

   Consulte "PYTHONCOERCECLOCALE" e a **PEP 538**.

--with-platlibdir=DIRNAME

   Nome do diretório da biblioteca Python (o padrão é "lib").

   Fedora e SuSE usam "lib64" em plataformas de 64 bits.

   Veja "sys.platlibdir".

   Adicionado na versão 3.9.

--with-wheel-pkg-dir=PATH

   Diretório de pacotes de wheel usados pelo módulo "ensurepip"
   (nenhum por padrão).

   Algumas políticas de empacotamento de distribuição do Linux
   recomendam contra o empacotamento de dependências. Por exemplo, o
   Fedora instala pacotes wheel no diretório "/usr/share/python-
   wheels/" e não instala o pacote "ensurepip._bundled".

   Adicionado na versão 3.10.

--with-pkg-config=[check|yes|no]

   Se o configure deve usar **pkg-config** para detectar dependências
   de construção.

   * "check" (padrão): **pkg-config** é opcional

   * "yes": **pkg-config** é obrigatório

   * "no": configure não usa **pkg-config** mesmo quando presente

   Adicionado na versão 3.11.

--with-missing-stdlib-config=FILE

   Caminho para um arquivo de configuração JSON contendo mensagens de
   erro personalizadas para módulos da *biblioteca padrão* ausentes.

   Esta opção destina-se a distribuidores de Python que desejam
   fornecer orientações específicas da distribuição quando os usuários
   encontrarem módulos da biblioteca padrão que estejam ausentes ou
   empacotados separadamente.

   O arquivo JSON deve mapear nomes de módulos ausentes para strings
   de mensagens de erro personalizadas. Por exemplo, se a sua
   distribuição empacota "tkinter" e "_tkinter" separadamente e exclui
   "_gdbm" por motivos legais, a configuração poderia conter:

      {
          "_gdbm": "The '_gdbm' module is not available in this distribution",
          "tkinter": "Install the python-tk package to use tkinter",
          "_tkinter": "Install the python-tk package to use tkinter",
      }

   Adicionado na versão 3.15.

--enable-pystats

   Ativa a coleta de estatísticas internas de desempenho do Python.

   Por padrão, a coleta de estatísticas está desativada. Use o comando
   "python3 -X pystats" ou defina a variável de ambiente
   "PYTHONSTATS=1" para ativar a coleta de estatísticas na
   inicialização do Python.

   Na saída do Python, despeja as estatísticas se a coleta de
   estatísticas estiver ativada e não apagada.

   Efeitos:

   * Adiciona a opção de linha de comando "-X pystats".

   * Adiciona a variável de ambiente "PYTHONSTATS".

   * Define a macro "Py_STATS".

   * Adiciona funções ao módulo "sys":

     * "sys._stats_on()": Ativa a coleta de estatísticas.

     * "sys._stats_off()": Desativa a coleta de estatísticas.

     * "sys._stats_clear()": Apaga as estatísticas.

     * "sys._stats_dump()": Despeja as estatísticas no arquivo e apaga
       as estatísticas.

   As estatísticas serão despejadas em um arquivo arbitrário
   (provavelmente único) em "/tmp/py_stats/" (Unix) ou
   "C:\temp\py_stats\" (Windows). Se aquele diretório não existir, os
   resultados serão enviados para stderr.

   Use "Tools/scripts/summarize_stats.py" para ler as estatísticas.

   Estatísticas:

   * Código de operação:

     * Especialização: sucesso, fracasso, acerto, adiado, erro, deopt,
       falhas;

     * Contagem de execuções;

     * Contagem em pares.

   * Chamada:

     * Chamadas Python em linha;

     * Chamadas a PyEval;

     * Quadros enviados;

     * Objetos quadro criados;

     * Chamadas de Eval: vetor, gerador, legado, função VECTORCALL,
       classe de construção, slot, função "ex", API, método.

   * Objeto:

     * incref e decref;

     * incref e decref do interpretador;

     * alocações: tudo, 512 bytes, 4 kiB, big;

     * memória livre;

     * listas de memória livre para/de;

     * Dicionário materializado/desmaterializado;

     * cache de tipo;

     * tentativas de otimização;

     * rastros de otimização criados/executados;

     * uops executados.

   * Coletor de lixo:

     * Coletas de lixo;

     * Objetos visitados;

     * Objetos coletados.

   Adicionado na versão 3.11.

--disable-gil

   Habilita suporte para execução de Python sem a *trava global do
   interpretador* (GIL): *construção com threads livres*.

   Define a macro "Py_GIL_DISABLED" e adiciona ""t"" a "sys.abiflags".

   Veja CPython com threads livres para mais detalhes.

   Adicionado na versão 3.13.

--enable-experimental-jit=[no|yes|yes-off|interpreter]

   Indica como integrar o compilador just-in-time experimental.

   * "no": não constrói o JIT;

   * "yes": habilita o JIT. Para desabilitá-lo em tempo de execução,
     defina a variável de ambiente "PYTHON_JIT=0".

   * "yes-off": constrói o JIT, mas desabilita-o por padrão. Para
     habilitá-lo em tempo de execução, defina a variável de ambiente
     "PYTHON_JIT=1".

   * "interpreter": Habilita o "interpretador JIT" (útil apenas para
     quem está depurando o próprio JIT). Para desabilitá-lo em tempo
     de execução, defina a variável de ambiente "PYTHON_JIT=0".

   "--enable-experimental-jit=no" é o comportamento padrão se a opção
   não for fornecida, e "--enable-experimental-jit" é uma abreviação
   de "--enable-experimental-jit=yes". Consulte "Tools/jit/README.md"
   para mais informações, incluindo como instalar as dependências
   necessárias em tempo de construção.

   Nota:

     Ao construir o CPython com o JIT habilitado, certifique-se de que
     seu sistema tenha o Python 3.11 ou posterior instalado.

   Adicionado na versão 3.13.

PKG_CONFIG

   Caminho para o utilitário "pkg-config".

PKG_CONFIG_LIBDIR

PKG_CONFIG_PATH

   Opções do "pkg-config".

--disable-epoll

   Construir sem "epoll", o que significa que "select.epoll()" não
   estará presente, mesmo que o sistema forneça uma função
   *epoll_create*. Isso pode ser utilizado em sistemas onde
   *epoll_create* ou *epoll_create1* estão disponíveis, mas são
   incompatíveis com a semântica do Linux.

   Adicionado na versão 3.15.


3.3.2. Opções do compilador C
-----------------------------

CC

   Comando do compilador C.

CFLAGS

   Sinalizadores do compilador C.

CPP

   Comando do pré-processador C.

CPPFLAGS

   Sinalizadores do pré-processador C, p.ex., "-I*include_dir*".


3.3.3. Opções da ligação
------------------------

LDFLAGS

   Sinalizadores do vinculador. p.ex., "-L*library_directory*".

LIBS

   Bibliotecas para passar para o vinculador, p.ex. "-l*library*".

MACHDEP

   Nome para arquivos de biblioteca dependentes de máquina.


3.3.4. Opções para dependências de terceiros
--------------------------------------------

Adicionado na versão 3.11.

BZIP2_CFLAGS

BZIP2_LIBS

   Sinalizadores de compilador C e vinculador para vincular Python a
   "libbz2", usados pelo módulo "bz2", substituindo "pkg-config".

CURSES_CFLAGS

CURSES_LIBS

   Sinalizadores de compilador C e vinculador para "libncurses" ou
   "libncursesw", usados pelo módulo "curses", substituindo "pkg-
   config".

GDBM_CFLAGS

GDBM_LIBS

   Sinalizadores de compilador C e vinculador para "gdbm".

LIBEDIT_CFLAGS

LIBEDIT_LIBS

   Sinalizadores de compilador C e vinculador para "libedit", usados
   pelo módulo "readline", substituindo "pkg-config".

LIBFFI_CFLAGS

LIBFFI_LIBS

   Sinalizadores de compilador C e vinculador para "libffi", usados
   pelo módulo "ctypes", substituindo "pkg-config".

LIBMPDEC_CFLAGS

LIBMPDEC_LIBS

   Sinalizadores de compilador C e vinculador para "libmpdec", usados
   pelo módulo "decimal", substituindo "pkg-config".

   Nota:

     Estas variáveis de ambiente não têm efeito a menos que "--with-
     system-libmpdec" seja especificado.

LIBLZMA_CFLAGS

LIBLZMA_LIBS

   Sinalizadores de compilador C e vinculador para "liblzma", usados
   pelo módulo "lzma", substituindo "pkg-config".

LIBREADLINE_CFLAGS

LIBREADLINE_LIBS

   Sinalizadores de compilador C e vinculador para "libreadline",
   usados pelo módulo "readline", substituindo "pkg-config".

LIBSQLITE3_CFLAGS

LIBSQLITE3_LIBS

   Sinalizadores de compilador C e vinculador para "libsqlite3",
   usados pelo módulo "sqlite3", substituindo "pkg-config".

LIBUUID_CFLAGS

LIBUUID_LIBS

   Sinalizadores de compilador C e vinculador para "libuuid", usados
   pelo módulo "uuid", substituindo "pkg-config".

LIBZSTD_CFLAGS

LIBZSTD_LIBS

   Sinalizadores de compilador C e ligador para "libzstd", usados pelo
   módulo "compression.zstd", substituindo "pkg-config".

   Adicionado na versão 3.14.

PANEL_CFLAGS

PANEL_LIBS

   Sinalizadores de compilador C e vinculador para PANEL, substituindo
   "pkg-config".

   Sinalizadores de compilador C e vinculador para "libpanel" ou
   "libpanelw", usados pelo módulo "curses.panel", substituindo "pkg-
   config".

TCLTK_CFLAGS

TCLTK_LIBS

   Sinalizadores de compilador C e vinculador para TCLTK, substituindo
   "pkg-config".;

ZLIB_CFLAGS

ZLIB_LIBS

   Sinalizadores de compilador C e vinculador para "libzlib", usados
   pelo módulo "gzip", substituindo "pkg-config".


3.3.5. Opções de WebAssembly
----------------------------

--enable-wasm-dynamic-linking

   Ativa o suporte de vinculação dinâmica para WASM.

   A vinculação dinâmica permite "dlopen". O tamanho do arquivo
   executável aumenta devido à eliminação limitada de código morto e
   recursos adicionais.

   Adicionado na versão 3.11.

--enable-wasm-pthreads

   Ativa o suporte a pthreads para WASM.

   Adicionado na versão 3.11.


3.3.6. Opções de instalação
---------------------------

--prefix=PREFIX

   Instala arquivos independentes de arquitetura em PREFIX. No Unix, o
   padrão é "/usr/local".

   Este valor pode ser recuperado em tempo de execução usando
   "sys.prefix".

   Como exemplo, pode-se usar "--prefix="$HOME/.local/"" para instalar
   um Python em seu diretório pessoal (home).

--exec-prefix=EPREFIX

   Instala arquivos dependentes de arquitetura no EPREFIX, o padrão é
   "--prefix".

   Este valor pode ser recuperado em tempo de execução usando
   "sys.exec_prefix".

--disable-test-modules

   Não constrói nem instala módulos de teste, como o pacote "test" ou
   o módulo de extensão "_testcapi" (construído e instalado por
   padrão).

   Adicionado na versão 3.10.

--with-ensurepip=[upgrade|install|no]

   Seleciona o comando "ensurepip" executado na instalação do Python:

   * "upgrade" (padrão): executa o comando "python -m ensurepip
     --altinstall --upgrade".

   * "install": executa o comando "python -m ensurepip --altinstall";

   * "no": não executa ensurepip;

   Adicionado na versão 3.6.


3.3.7. Opções de desempenho
---------------------------

Configurar o Python usando "--enable-optimizations --with-lto" (PGO +
LTO) é o recomendado para melhor desempenho. O sinalizador
experimental "--enable-bolt" também pode ser usado para melhorar o
desempenho.

--enable-optimizations

   Habilita a otimização guiada por perfil (PGO, do inglês Profile
   Guided Optimization) usando "PROFILE_TASK" (desabilitado por
   padrão).

   O compilador C Clang requer o programa "llvm-profdata" para PGO. No
   macOS, o GCC também exige: o GCC é apenas um apelido para o Clang
   no macOS.

   Desabilita também a interposição semântica no libpython se "--
   enable-shared" e GCC forem usados: adiciona "-fno-semantic-
   interposition" aos sinalizadores do compilador e do vinculador.

   Nota:

     Durante a construção, você poderá encontrar avisos do compilador
     sobre a indisponibilidade de dados de perfil para alguns arquivos
     fonte. Esses avisos são inofensivos, pois apenas um subconjunto
     do código é exercido durante a aquisição de dados de perfil. Para
     desativar esses avisos no Clang, suprima-os manualmente
     adicionando "-Wno-profile-instr-unprofiled" a "CFLAGS".

   Adicionado na versão 3.6.

   Alterado na versão 3.10: Usa "-fno-semantic-interposition" no GCC.

PROFILE_TASK

   Variável de ambiente usada no Makefile: argumentos de linha de
   comando do Python para a tarefa de geração de PGO.

   Padrão: "-m test --pgo --timeout=$(TESTTIMEOUT)".

   Adicionado na versão 3.8.

   Alterado na versão 3.13: A falha da tarefa não é mais ignorada
   silenciosamente.

--with-lto=[full|thin|no|yes]

   Habilita o otimização em tempo de vinculação (LTO, do inglês Link
   Time Optimization) em qualquer construção (desabilitado por
   padrão).

   O compilador C Clang requer "llvm-ar" para LTO ("ar" no macOS), bem
   como um vinculador compatível com LTO ("ld.gold" ou "lld").

   Adicionado na versão 3.6.

   Adicionado na versão 3.11: Para usar o recurso ThinLTO, use "--
   with-lto=thin" no Clang.

   Alterado na versão 3.12: Usa ThinLTO como política de otimização
   padrão no Clang se o compilador aceitar o sinalizador.

--enable-bolt

   Habilita o uso do otimizador binário pós-vinculação BOLT
   (desabilitado por padrão).

   BOLT faz parte do projeto LLVM, mas nem sempre está incluído em
   suas distribuições binárias. Este sinalizador requer que "llvm-
   bolt" e "merge-fdata" estejam disponíveis.

   BOLT ainda é um projeto relativamente novo, então este sinalizador
   deve ser considerado experimental por enquanto. Como esta
   ferramenta opera em código de máquina, seu sucesso depende de uma
   combinação do ambiente de construção + os outros argumentos de
   configuração de otimização + a arquitetura da CPU, e nem todas as
   combinações são suportadas. Versões do BOLT anteriores ao LLVM 16
   são conhecidas por travar o BOLT em alguns cenários. O uso do LLVM
   16 ou mais recente para otimização do BOLT é fortemente
   incentivado.

   As variáveis "BOLT_INSTRUMENT_FLAGS" e "BOLT_APPLY_FLAGS" do
   **configure** podem ser definidas para substituir o conjunto padrão
   de argumentos para **llvm-bolt** para instrumentar e aplicar dados
   BOLT aos binários , respectivamente.

   Adicionado na versão 3.12.

BOLT_APPLY_FLAGS

   Argumentos para "llvm-bolt" ao criar um binário otimizado com BOLT.

   Adicionado na versão 3.12.

BOLT_INSTRUMENT_FLAGS

   Argumentos para "llvm-bolt" ao instrumentar binários.

   Adicionado na versão 3.12.

--with-computed-gotos

   Habilita "gotos" computados no laço de avaliação (habilitado por
   padrão em compiladores suportados).

--with-tail-call-interp

   Habilita interpretadores usando chamadas de cauda no CPython. Se
   habilitado, é altamente recomendável habilitar PGO ("--enable-
   optimizations"). Esta opção requer especificamente um compilador C
   com suporte adequado a chamadas de cauda e a convenção de chamada
   preserve_none. Por exemplo, o Clang 19 e versões mais recentes
   oferecem suporte a esse recurso.

   Adicionado na versão 3.14.

--without-frame-pointers

   Desabilita os ponteiros de quadro, que estão habilitados por padrão
   (veja **PEP 831**).

   Por padrão, o processo de construção acrescenta sinalizadores a
   "BASECFLAGS" para gerar ponteiros de quadro (*frame pointers*) ou
   de encadeamento (*backchain pointers*):

   * "-fno-omit-frame-pointer" e/ou "-mno-omit-leaf-frame-pointer" são
     adicionados quando o compilador oferece suporte a eles.

   * "-marm" e/ou "-mno-thumb" são adicionados em sistemas ARM de 32
     bits quando suportados.

   * em plataformas s390x, quando suportado, "-mbackchain" é
     adicionado *em vez* das flags de ponteiro de quadro mencionadas
     acima.

   * em plataformas ppc64le, não são necessárias sinalizadores de
     compilador, uma vez que a ABI Power exige que os compiladores
     mantenham um encadeamento (*back chain*) por padrão.

   Ponteiros de quadro (*frame pointers*) permitem que ferramentas de
   perfilamento, depuração e rastreamento do sistema (como "perf",
   "eBPF", "dtrace" e "gdb") percorram a pilha de chamadas em C sem a
   necessidade de metadados DWARF. Os sinalizadores são propagadas
   para extensões C de terceiros por meio do módulo "sysconfig". Em
   compiladores que não as reconhecem, o processo de construção as
   ignora silenciosamente.

   Empacotadores downstream e autores de bibliotecas nativas criadas
   com sistemas de construção personalizados devem definir as mesmas
   flags para que a cadeia de desenrolamento (unwind chain) permaneça
   ininterrupta em todos os frames nativos.

   Adicionado na versão 3.15.

--without-mimalloc

   Desativa o alocador rápido mimalloc (habilitado por padrão).

   Esta opção não pode ser usada junto com "--disable-gil" porque a
   construção com *threads livres* requer mimalloc.

   Veja também a variável de ambiente "PYTHONMALLOC".

--without-pymalloc

   Desabilita o alocador de memória especializado do Python pymalloc
   (habilitado por padrão).

   Veja também a variável de ambiente "PYTHONMALLOC".

--with-pymalloc-hugepages

   Habilita o suporte a *huge pages* para arenas do pymalloc
   (desabilitado por padrão). Quando habilitado, o tamanho da arena em
   plataformas de 64 bits é aumentado para 2 MiB e a alocação da arena
   utiliza "MAP_HUGETLB" (Linux) ou "MEM_LARGE_PAGES" (Windows), com
   *fallback* automático para páginas comuns.

   Mesmo quando compilado com essa opção, *huge pages* **não** são
   utilizadas em tempo de execução, a menos que a variável de ambiente
   "PYTHON_PYMALLOC_HUGEPAGES" esteja definida como "1". Essa ativação
   explícita é necessária porque *huge pages*

   * envolve riscos no Linux: se o pool de *huge pages* se esgotar,
     falhas de página (incluindo falhas de *copy-on-write* após
     "os.fork()") geram um sinal "SIGBUS" e encerram forçadamente o
     processo.

   * precisa de um privilégio especial no Windows. Consulte a
     documentação do Windows para páginas grandes para obter detalhes.
     Python falhará na inicialização se o privilégio necessário
     SeLockMemoryPrivilege não for concedido ao usuário.

   O script de configuração verifica se a plataforma oferece suporte a
   "MAP_HUGETLB" e emite um aviso caso não esteja disponível.

   No Windows, use o sinalizador "--pymalloc-hugepages" com o
   "build.bat" ou defina a propriedade MSBuild "UsePymallocHugepages".

   Adicionado na versão 3.15.

--without-doc-strings

   Desabilita as strings de documentação estática para reduzir o
   consumo de memória (habilitado por padrão). As strings de
   documentação definidas em Python não são afetadas.

   Não define a macro "WITH_DOC_STRINGS".

   WITH_DOC_STRINGS

      Defina esta macro para incluir strings de documentação estáticas
      na construção. Isso é definido por padrão, a menos que "--
      without-doc-strings" seja usada.

   Veja a macro "PyDoc_STRVAR()".

--enable-profiling

   Habilita o perfil de código a nível C com "gprof" (desabilitado por
   padrão).

--with-strict-overflow

   Adiciona "-fstrict-overflow" aos sinalizadores do compilador C (por
   padrão adicionamos "-fno-strict-overflow").

--without-remote-debug

   Desativa o suporte à depuração remota descrito na **PEP 768**
   (habilitado por padrão). Quando este sinalizador é fornecido, o
   código que permite ao interpretador agendar a execução de um
   arquivo Python em um processo separado, conforme descrito na **PEP
   768**, não é compilado. Isso inclui tanto a funcionalidade de
   agendar a execução do código quanto a funcionalidade de receber a
   execução do código.

   Py_REMOTE_DEBUG

      Esta macro é definida por padrão, a menos que o Python esteja
      configurado com "--without-remote-debug".

      Observe que, mesmo que a macro esteja definida, a depuração
      remota pode não estar disponível (por exemplo, em uma plataforma
      incompatível).

   Adicionado na versão 3.14.


3.3.8. Compilação de depuração do Python
----------------------------------------

Uma compilação de depuração é Python compilada com a opção de
configuração "--with-pydebug".

Efeitos de uma compilação de depuração:

* Exibe todos os avisos por padrão: a lista de filtros de aviso padrão
  está vazia no módulo "warnings".

* Adiciona "d" a "sys.abiflags".

* Adiciona a função "sys.gettotalrefcount()".

* Adiciona a opção de linha de comando "-X showrefcount".

* Adiciona a opção de linha de comando "-d" e a variável de ambiente
  "PYTHONDEBUG" para depurar o analisador sintático.

* Adiciona suporte para a variável "__lltrace__": habilita o
  rastreamento de baixo nível no laço de avaliação de bytecode se a
  variável estiver definida.

* Instala ganchos de depuração nos alocadores de memória para detectar
  estouro de buffer e outros erros de memória.

* Define as macros "Py_DEBUG" e "Py_REF_DEBUG".

* Adiciona verificações de tempo de execução: código cercado por
  "#ifdef Py_DEBUG" e "#endif". Habilita as asserções "assert(...)" e
  "_PyObject_ASSERT(...)": não define a macro "NDEBUG" (veja também a
  configuração "--with-assertions" opção). Principais verificações de
  tempo de execução:

  * Adiciona verificações de sanidade nos argumentos da função.

  * Objetos Unicode e int são criados com sua memória preenchida com
    um padrão para detectar o uso de objetos não inicializados.

  * Garante que as funções que podem limpar ou substituir a exceção
    atual não sejam chamadas com uma exceção levantada.

  * Verifica se as funções desalocadoras não alteram a exceção atual.

  * O coletor de lixo (função "gc.collect()") executa algumas
    verificações básicas na consistência dos objetos.

  * A macro "Py_SAFE_DOWNCAST()" verifica o underflow e o overflow de
    inteiros ao fazer o downcast de tipos largos para tipos estreitos.

Veja também o Modo de Desenvolvimento do Python e a opção de
configuração "--with-trace-refs".

Alterado na versão 3.8: Construções de lançamento agora são
compatíveis em ABI com construções de depuração: definir a macro
"Py_DEBUG" não implica mais na macro "Py_TRACE_REFS" (consulte a opção
"--with-trace-refs"). No entanto, construções de depuração ainda
expõem mais símbolos que as construções de lançamento e o código
construído no modo depuração não é necessariamente compatível com uma
construção de lançamento.


3.3.9. Opções de depuração
--------------------------

--with-pydebug

   Construção de depuração do Python: define a macro "Py_DEBUG"
   (desabilitada por padrão).

--with-trace-refs

   Habilita referências de rastreamento para fins de depuração
   (desabilitado por padrão).

   Efeitos:

   * Define a macro "Py_TRACE_REFS".

   * Adiciona a função "sys.getobjects()".

   * Adiciona a variável de ambiente "PYTHONDUMPREFS".

   A variável de ambiente "PYTHONDUMPREFS" pode ser usada para
   despejar objetos e contagens de referências ainda ativas na saída
   do Python.

   Objetos alocados estaticamente não são rastreados.

   Adicionado na versão 3.8.

   Alterado na versão 3.13: Esta construção agora é compatibilidade de
   ABI com a construção de lançamento e construção de depuração.

--with-assertions

   Constrói com asserções C habilitadas (o padrão é não):
   "assert(...);" e "_PyObject_ASSERT(...);".

   Se definido, a macro "NDEBUG" não é definida na variável do
   compilador "OPT".

   Veja também a opção "--with-pydebug" (construção de depuração) que
   também habilita asserções.

   Adicionado na versão 3.6.

--with-valgrind

   Habilita suporte ao Valgrind (o padrão é não).

--with-dtrace

   Habilita suporte ao DTrace (o padrão é não).

   Veja Instrumentando o CPython com DTrace e SystemTap.

   Adicionado na versão 3.6.

--with-address-sanitizer

   Habilita o detector de erros de memória AddressSanitizer, "asan" (o
   padrão é não). Para melhorar os recursos de detecção do ASan, você
   também pode combinar isso com "--without-pymalloc" para desabilitar
   o alocador especializado de pequenos objetos cujas alocações não
   são rastreadas pelo ASan.

   Adicionado na versão 3.6.

--with-memory-sanitizer

   Habilita o detector de erros de alocação do MemorySanitizer, "msan"
   (o padrão é não).

   O MSan relata falsos positivos para memórias inicializadas por
   bibliotecas que não foram compiladas com o MSan; portanto, compile
   todas as dependências com o MSan ou desabilite os módulos de
   extensão que as utilizam, em "Modules/Setup.local".

   Adicionado na versão 3.6.

--with-undefined-behavior-sanitizer

   Habilita o detector de comportamento indefinido
   UndefinedBehaviorSanitizer, "ubsan" (o padrão é não).

   Adicionado na versão 3.6.

--with-thread-sanitizer

   Habilita o detector de corrida de dados ThreadSanitizer, "tsan" (o
   padrão é não).

   Adicionado na versão 3.13.


3.3.10. Opções da ligação
-------------------------

--enable-shared

   Habilita a construção de uma biblioteca Python compartilhada:
   "libpython" (o padrão é não).

--without-static-libpython

   Não constrói "libpythonMAJOR.MINOR.a" e não instala "python.o"
   (construído e habilitado por padrão).

   Adicionado na versão 3.10.

--enable-static-libpython-for-interpreter

   Não vincula o binário do interpretador Python ("python3") à
   biblioteca compartilhada do Python; em vez disso, vincula o
   interpretador estaticamente à "libpython" como se a opção "--
   enable-shared" não tivesse sido utilizada, mas continua a construir
   a "libpython" compartilhada (para uso por outros programas).

   Esta opção faz nada se "--enable-shared" não for usada.

   O comportamento padrão (quando "-enable-shared" é utilizado) é
   vincular o interpretador Python à biblioteca compartilhada
   compilada.

   Adicionado na versão 3.15.


3.3.11. Opções da biblioteca
----------------------------

--with-libs='lib1 ...'

   Vincula bibliotecas adicionais (o padrão é não).

--with-system-expat

   Constrói o módulo "pyexpat" usando uma biblioteca "expat" instalada
   (o padrão é não).

--with-system-libmpdec

   Constrói o módulo de extensão "_decimal" usando uma biblioteca
   "mpdecimal" instalada, veja o módulo "decimal" (o padrão é sim).

   Adicionado na versão 3.3.

   Alterado na versão 3.13: O padrão é usar a biblioteca "mpdecimal"
   instalada.

   Alterado na versão 3.15: Uma cópia da biblioteca incluída no pacote
   não será mais selecionada implicitamente se uma biblioteca
   "mpdecimal" instalada não for encontrada. Somente no Python 3.15,
   ela ainda pode ser selecionada explicitamente usando "--with-
   system-libmpdec=no" ou "--without-system-libmpdec".

   Descontinuado desde a versão 3.13, será removido na versão 3.16:
   Uma cópia dos fontes da biblioteca "mpdecimal" não será mais
   distribuída com Python 3.16.

   Ver também: "LIBMPDEC_CFLAGS" e "LIBMPDEC_LIBS".

--with-readline=readline|editline

   Designa uma biblioteca backend para o módulo "readline".

   * readline: Usa readline como o backend.

   * editline: Usa editline como o backend.

   Adicionado na versão 3.10.

--without-readline

   Não constrói o módulo "readline" (construído por padrão).

   Não define a macro "HAVE_LIBREADLINE".

   Adicionado na versão 3.10.

--with-libm=STRING

   Substitui a biblioteca matemática "libm" por *STRING* (o padrão
   depende do sistema).

--with-libc=STRING

   Substitui a biblioteca C "libc" por *STRING* (o padrão depende do
   sistema).

--with-openssl=DIR

   Raiz do diretório OpenSSL.

   Adicionado na versão 3.7.

--with-openssl-rpath=[no|auto|DIR]

   Define o diretório da biblioteca de tempo de execução (rpath) para
   bibliotecas OpenSSL:

   * "no" (padrão): não define o rpath;

   * "auto": detecta automaticamente o rpath de "--with-openssl" e
     "pkg-config";

   * *DIR*: define um rpath explícito.

   Adicionado na versão 3.10.


3.3.12. Opções de segurança
---------------------------

--with-hash-algorithm=[fnv|siphash13|siphash24]

   Seleciona o algoritmo de hash para usar em "Python/pyhash.c":

   * "siphash13" (padrão);

   * "siphash24";

   * "fnv".

   Adicionado na versão 3.4.

   Adicionado na versão 3.11: "siphash13" é adicionado e é o novo
   padrão.

--with-builtin-hashlib-hashes=md5,sha1,sha256,sha512,sha3,blake2

   Módulos embutidos de hash

   * "md5";

   * "sha1";

   * "sha256";

   * "sha512";

   * "sha3" (com shake);

   * "blake2".

   Adicionado na versão 3.9.

--with-ssl-default-suites=[python|openssl|STRING]

   Substitui a string dos conjuntos de criptografia padrão do OpenSSL:

   * "python" (padrão): use a seleciona preferida do Python;

   * "openssl": mantém inalterados os padrões do OpenSSL;

   * *STRING*: usa uma string personalizada

   Veja o módulo "ssl".

   Adicionado na versão 3.7.

   Alterado na versão 3.10: As configurações "python" e *STRING*
   também definem TLS 1.2 como versão mínima do protocolo.

--disable-safety

   Desabilita as opções do compilador recomendadas pela OpenSSF por
   motivos de segurança, sem causar sobrecarga de desempenho. Se esta
   opção não estiver habilitada, o CPython será construído com base
   nas opções de segurança do compilador, sem causar lentidão. Quando
   esta opção estiver habilitada, o CPython não será construído com as
   opções do compilador listadas abaixo.

   As seguintes opções do compilador são desabilitadas com "--disable-
   safety":

   * -fstack-protector-strong: Habilita verificações em tempo de
     execução para estouros de buffer baseados em pilha.

   * -Wtrampolines: Habilita avisos sobre trampolins que exigem pilhas
     executáveis.

   Adicionado na versão 3.14.

--enable-slower-safety

   Habilita as opções do compilador recomendadas pela OpenSSF por
   motivos de segurança, o que causa sobrecarga. Se esta opção não
   estiver habilitada, o CPython não será construído com base nas
   opções de segurança do compilador, o que impacta o desempenho.
   Quando esta opção estiver habilitada, o CPython será construído com
   as opções do compilador listadas abaixo.

   As seguintes opções do compilador são habilitadas com "--enable-
   slower-safety":

   * -D_FORTIFY_SOURCE=3: Fortalece as fontes com verificações de
     tempo de compilação e execução para uso inseguro de libc e
     estouros de buffer.

   Adicionado na versão 3.14.


3.3.13. Opções do macOS
-----------------------

Veja Mac/README.rst.

--enable-universalsdk

--enable-universalsdk=SDKDIR

   Cria uma construção binária universal. *SDKDIR* especifica qual SDK
   do macOS deve ser usado para executar a construção (o padrão é
   não).

--enable-framework

--enable-framework=INSTALLDIR

   Cria um Python.framework em vez de uma instalação tradicional do
   Unix. O *INSTALLDIR* opcional especifica o caminho de instalação (o
   padrão é não).

--with-universal-archs=ARCH

   Especifica o tipo de binário universal que deve ser criado. Esta
   opção só é válida quando "--enable-universalsdk" está definido.

   Opções:

   * "universal2" (x86-64 e arm64);

   * "32-bit" (PPC e i386);

   * "64-bit"  (PPC64 e x86-64);

   * "3-way" (i386, PPC e x86-64);

   * "intel" (i386 e x86-64);

   * "intel-32" (i386);

   * "intel-64" (x86-64);

   * "all"  (PPC, i386, PPC64 e x86-64).

   Observe que os valores para este item de configuração *não* são os
   mesmos que os identificadores usados para rodas binárias universais
   no macOS. Veja o Guia de Empacotamento do Python para detalhes
   sobre as tags de compatibilidade de plataforma de empacotamento
   usadas no macOS

--with-framework-name=FRAMEWORK

   Especifica o nome do framework python no macOS válido apenas quando
   "--enable-framework" está definido (padrão: "Python").

--with-app-store-compliance

--with-app-store-compliance=PATCH-FILE

   A biblioteca padrão do Python contém strings que são conhecidas por
   acionar erros de ferramentas de inspeção automatizadas quando
   enviadas para distribuição pelas App Stores do macOS e do iOS. Se
   ativada, esta opção aplicará a lista de patches que corrigem a
   conformidade da app store. Um arquivo de patch personalizado também
   pode ser especificado. Esta opção está desativada por padrão.

   Adicionado na versão 3.13.


3.3.14. Opções do iOS
---------------------

Veja Platforms/Apple/iOS/README.md.

--enable-framework=INSTALLDIR

   Cria um Python.framework. Ao contrário do macOS, o argumento
   *INSTALLDIR* que especifica o caminho de instalação é obrigatório.

--with-framework-name=FRAMEWORK

   Especifica o nome do framework (padrão: "Python").


3.3.15. Opções de compilação cruzada
------------------------------------

A compilação cruzada, também conhecida como construção cruzada, pode
ser usada para construir Python para outra arquitetura ou plataforma
de CPU. A compilação cruzada requer um interpretador Python para a
plataforma de construção. A versão do Python para construção deve
corresponder à versão do Python da compilação cruzada do host.

--build=BUILD

   configura para construir em BUILD, geralmente adivinhado por
   **config.guess**.

--host=HOST

   faz compilação cruzada para construir programas para executar no
   HOST (plataforma de destino)

--with-build-python=path/to/python

   caminho para construir o binário "python" para compilação cruzada

   Adicionado na versão 3.11.

CONFIG_SITE=file

   Uma variável de ambiente que aponta para um arquivo com
   substituições de configuração.

   Exemplo de arquivo *config.site*:

      # config.site-aarch64
      ac_cv_buggy_getaddrinfo=no
      ac_cv_file__dev_ptmx=yes
      ac_cv_file__dev_ptc=no

HOSTRUNNER

   Programa para executar CPython para a plataforma host para
   compilação cruzada.

   Adicionado na versão 3.11.

Exemplo de compilação cruzada:

   CONFIG_SITE=config.site-aarch64 ../configure \
       --build=x86_64-pc-linux-gnu \
       --host=aarch64-unknown-linux-gnu \
       --with-build-python=../x86_64/python


3.4. Sistema de Construção Python
=================================


3.4.1. Arquivos principais do sistema de construção
---------------------------------------------------

* "configure.ac" => "configure";

* "Makefile.pre.in" => "Makefile" (criado por "configure");

* "pyconfig.h" (criado por "configure");

* "Modules/Setup": Extensões C construídas pelo Makefile usando o
  shell script "Module/makesetup";


3.4.2. Principais etapas de construção
--------------------------------------

* Arquivos C (".c") são construídos como arquivos objeto (".o").

* Uma biblioteca estática "libpython" (".a") é criada a partir de
  arquivos de objetos.

* "python.o" e a biblioteca estática "libpython" estão vinculadas ao
  programa final "python".

* Extensões C são construídas pelo Makefile (veja "Modules/Setup").


3.4.3. Alvos principais do Makefile
-----------------------------------


3.4.3.1. make
~~~~~~~~~~~~~

Na maioria das vezes, ao reconstruir após editar algum código ou
atualizar seu checkout do upstream, tudo que você precisa fazer é
executar "make", que (pela semântica do Make) constrói o alvo padrão,
o primeiro definido no Makefile. Por tradição (inclusive no projeto
CPython) este é geralmente o alvo "all". O script "configure" expande
uma variável "autoconf", "@DEF_MAKE_ALL_RULE@" para descrever
precisamente quais alvos "make all" serão construídos. As três opções
são:

* "profile-opt" (configurado com "--enable-optimizations")

* "build_wasm" (escolhido se a plataforma host corresponder a
  "wasm32-wasi*" ou "wasm32-emscripten")

* "build_all" (configurado sem usar explicitamente nenhum dos outros)

Dependendo das alterações mais recentes no arquivo fonte, o Make irá
reconstruir quaisquer alvos (arquivos objetos e executáveis)
considerados desatualizados, incluindo executar "configure" novamente
se necessário. As dependências de origem/alvo são muitas e mantidas
manualmente, portanto, às vezes, o Make não tem todas as informações
necessárias para detectar corretamente todos os alvos que precisam ser
reconstruídos. Dependendo de quais destinos não são reconstruídos,
você poderá enfrentar vários problemas. Se você tiver problemas de
construção ou teste que você não pode explicar de outra forma, "make
clean && make" deve resolver a maioria dos problemas de dependência,
às custas de tempos de construção mais longos.


3.4.3.2. make platform
~~~~~~~~~~~~~~~~~~~~~~

Constrói o programa "python", mas não constrói os módulos de extensão
da biblioteca padrão. Isto gera um arquivo chamado "platform" que
contém uma única linha descrevendo os detalhes da plataforma de
construção, por exemplo, "macosx-14.3-arm64-3.12" ou
"linux-x86_64-3.13".


3.4.3.3. make profile-opt
~~~~~~~~~~~~~~~~~~~~~~~~~

Constrói Python usando otimização guiada por perfil (PGO). Você pode
usar a opção "--enable-optimizations" do configure para tornar este o
alvo padrão do comando "make" ("make all" ou apenas "make").


3.4.3.4. make clean
~~~~~~~~~~~~~~~~~~~

Remove arquivos construídos.


3.4.3.5. make distclean
~~~~~~~~~~~~~~~~~~~~~~~

Além do trabalho feito por "make clean", remove os arquivos criados
pelo script configure. "configure" terá que ser executado antes de
construir novamente. [7]


3.4.3.6. make install
~~~~~~~~~~~~~~~~~~~~~

Constrói o alvo "all" e instala o Python.


3.4.3.7. make test
~~~~~~~~~~~~~~~~~~

Constrói o alvo "all" e execute o conjunto de testes Python com a
opção "--fast-ci" sem testes de GUI. Variáveis:

* "TESTOPTS": opções adicionais de linha de comando regrtest.

* "TESTPYTHONOPTS": opções adicionais de linha de comando do Python.

* "TESTTIMEOUT": tempo limite em segundos (padrão: 10 minutos).


3.4.3.8. make ci
~~~~~~~~~~~~~~~~

Isso é semelhante ao "make test", mas usa "-ugui" para também executar
testes de GUI.

Adicionado na versão 3.14.


3.4.3.9. make buildbottest
~~~~~~~~~~~~~~~~~~~~~~~~~~

Isto é semelhante ao "make test", mas usa a opção "--slow-ci" e o
tempo limite padrão de 20 minutos, em vez da opção "--fast-ci".


3.4.3.10. make regen-all
~~~~~~~~~~~~~~~~~~~~~~~~

Gera novamente (quase) todos os arquivos gerados. Isso inclui (mas não
está limitado a) casos de bytecode e arquivo gerador de analisador
sintático. "make regen-stdlib-module-names" e "autoconf" devem ser
executados separadamente para os restantes arquivos gerados.


3.4.4. Extensões C
------------------

Algumas extensões C são construídas como módulos embutidos, como o
módulo "sys". Eles são construídos com a macro "Py_BUILD_CORE_BUILTIN"
definida. Módulos embutidos não possuem nenhum atributo "__file__":

   >>> import sys
   >>> sys
   <module 'sys' (built-in)>
   >>> sys.__file__
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: module 'sys' has no attribute '__file__'

Outras extensões C são construídas como bibliotecas dinâmicas, como o
módulo "_asyncio". Eles são construídos com a macro
"Py_BUILD_CORE_MODULE" definida. Exemplo no Linux x86-64:

   >>> import _asyncio
   >>> _asyncio
   <module '_asyncio' from '/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'>
   >>> _asyncio.__file__
   '/usr/lib64/python3.9/lib-dynload/_asyncio.cpython-39-x86_64-linux-gnu.so'

"Modules/Setup" é usado para gerar alvos Makefile para construir
extensões C. No início dos arquivos, as extensões C são construídas
como módulos embutidos. Extensões definidas após o marcador "*shared*"
são construídas como bibliotecas dinâmicas.

As macros "PyAPI_FUNC()", "PyAPI_DATA()" e "PyMODINIT_FUNC" de
"Include/exports.h" são definidas de forma diferente dependendo se a
macro "Py_BUILD_CORE_MODULE" está definida:

* Usa "Py_EXPORTED_SYMBOL" se "Py_BUILD_CORE_MODULE" estiver definido

* Do contrário, usa "Py_IMPORTED_SYMBOL".

Se a macro "Py_BUILD_CORE_BUILTIN" for usada por engano em uma
extensão C construída como uma biblioteca compartilhada, sua função
"PyInit_*xxx*()" não será exportada, causando um "ImportError" na
importação.


3.5. Sinalizadores do compilador e do vinculador
================================================

Opções definidas pelo script "./configure" e variáveis de ambiente e
usadas por "Makefile".


3.5.1. Sinalizadores do pré-processador
---------------------------------------

CONFIGURE_CPPFLAGS

   Valor da variável "CPPFLAGS" passado para o script "./configure".

   Adicionado na versão 3.6.

CPPFLAGS

   Sinalizadores de pré-processador C++ / (Objective) C, p.ex.
   "-I*include_dir*" se você tiver cabeçalhos em um diretório não
   padrão *include_dir*.

   Tanto "CPPFLAGS" quanto "LDFLAGS" precisam conter o valor do shell
   para poder construir módulos de extensão usando os diretórios
   especificados nas variáveis de ambiente.

BASECPPFLAGS

   Adicionado na versão 3.4.

PY_CPPFLAGS

   Sinalizadores extras de pré-processador adicionados para construir
   os arquivos de objeto do interpretador.

   Padrão: "$(BASECPPFLAGS) -I. -I$(srcdir)/Include
   $(CONFIGURE_CPPFLAGS) $(CPPFLAGS)".

   Adicionado na versão 3.2.


3.5.2. Sinalizadores do compilador
----------------------------------

CC

   Comando do compilador C.

   Exemplo: "gcc -pthread".

CXX

   Comando do compilador C++.

   Exemplo: "g++ -pthread".

CFLAGS

   Sinalizadores do compilador C.

CFLAGS_NODIST

   "CFLAGS_NODIST" é usado para construir o interpretador e extensões
   C da stdlib. Use-o quando um sinalizador do compilador *não* deve
   fazer parte de "CFLAGS" depois que o Python estiver instalado
   (gh-65320).

   Em particular, "CFLAGS" não deve conter:

   * o sinalizador do compilador "-I" (para definir o caminho de
     pesquisa para arquivos incluídos). Os sinalizadores "-I" são
     processadas da esquerda para a direita, e quaisquer sinalizadores
     em "CFLAGS" terão precedência sobre os sinalizadores "-I"
     fornecidos pelo usuário e pelo pacote.

   * sinalizadores de segurança como "-Werror" porque as distribuições
     não podem controlar se os pacotes instalados pelos usuários estão
     em conformidade com esses padrões elevados.

   Adicionado na versão 3.5.

COMPILEALL_OPTS

   Opções passadas para a linha de comando "compileall" ao construir
   arquivos PYC em "make install". Padrão: "-j0".

   Adicionado na versão 3.12.

EXTRA_CFLAGS

   Sinalizadores extra do compilador C.

CONFIGURE_CFLAGS

   Valor da variável "CFLAGS" passado para o script "./configure".

   Adicionado na versão 3.2.

CONFIGURE_CFLAGS_NODIST

   Valor da variável "CFLAGS_NODIST" passado para o script
   "./configure".

   Adicionado na versão 3.5.

BASECFLAGS

   Sinalizadores base do compilador.

OPT

   Sinalizadores de otimização.

CFLAGS_ALIASING

   Sinalizadores de alias estritos ou não estritos usados para
   compilar "Python/dtoa.c".

   Adicionado na versão 3.7.

CFLAGS_CEVAL

   Sinalizadores usados para compilar "Python/ceval.c".

   Adicionado na versão 3.14.5.

CCSHARED

   Sinalizadores de compilador usados para construir uma biblioteca
   compartilhada.

   Por exemplo, "-fPIC" é usado no Linux e no BSD.

CFLAGSFORSHARED

   Sinalizadores extras de C adicionados para construir os arquivos de
   objeto do interpretador.

   Padrão: "$(CCSHARED)" quando "--enable-shared" é usado, ou uma
   string vazia caso contrário.

PY_CFLAGS

   Padrão: "$(BASECFLAGS) $(OPT) $(CONFIGURE_CFLAGS) $(CFLAGS)
   $(EXTRA_CFLAGS)".

PY_CFLAGS_NODIST

   Padrão: "$(CONFIGURE_CFLAGS_NODIST) $(CFLAGS_NODIST)
   -I$(srcdir)/Include/internal".

   Adicionado na versão 3.5.

PY_STDMODULE_CFLAGS

   Sinalizadores do C usados para construir os arquivos de objeto do
   interpretador.

   Padrão: "$(PY_CFLAGS) $(PY_CFLAGS_NODIST) $(PY_CPPFLAGS)
   $(CFLAGSFORSHARED)".

   Adicionado na versão 3.7.

PY_CORE_CFLAGS

   Padrão: "$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE".

   Adicionado na versão 3.2.

PY_BUILTIN_MODULE_CFLAGS

   Sinalizadores do compilador para construir um módulo de extensão de
   biblioteca padrão como um módulo embutido, como o módulo "posix".

   Padrão: "$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE_BUILTIN".

   Adicionado na versão 3.8.

PURIFY

   Comando de Purify. Purify é um programa depurador de memória.

   Padrão: string vazia (não usada).


3.5.3. Sinalizadores do vinculador
----------------------------------

LINKCC

   Comando do vinculador usado para construir programas como "python"
   e "_testembed".

   Padrão: "$(PURIFY) $(CC)".

CONFIGURE_LDFLAGS

   Valor da variável "LDFLAGS" passado para o script "./configure".

   Evite atribuir "CFLAGS", "LDFLAGS", etc. para que os usuários
   possam usá-los na linha de comando para anexar a esses valores sem
   pisotear os valores predefinidos.

   Adicionado na versão 3.2.

LDFLAGS_NODIST

   "LDFLAGS_NODIST" é usado da mesma maneira que "CFLAGS_NODIST".
   Use-o quando um sinalizador de vinculador *não* fizer parte de
   "LDFLAGS" depois que o Python estiver instalado (gh-65320).

   Em particular, "LDFLAGS" não deve conter:

   * o sinalizador do compilador "-L" (para definir o caminho de
     pesquisa para arquivos incluídos). Os sinalizadores "-L" são
     processadas da esquerda para a direita, e quaisquer sinalizadores
     em "LDFLAGS" terão precedência sobre os sinalizadores "-L"
     fornecidos pelo usuário e pelo pacote.

CONFIGURE_LDFLAGS_NODIST

   Valor da variável "LDFLAGS_NODIST" passado para o script
   "./configure".

   Adicionado na versão 3.8.

LDFLAGS

   Sinalizadores do vinculador, p.ex. "-L*lib_dir*", se você tiver
   bibliotecas em um diretório não padrão *lib_dir*.

   Tanto "CPPFLAGS" quanto "LDFLAGS" precisam conter o valor do shell
   para poder construir módulos de extensão usando os diretórios
   especificados nas variáveis de ambiente.

   Considere utilizar "EXE_LDFLAGS" se os sinalizadores do ligador
   fornecidas forem específicas para executáveis, como, por exemplo, o
   sinalizador "-pie" do GCC.

LIBS

   Sinalizadores do vinculador para passar bibliotecas para o
   vinculador ao vincular o executável Python.

   Exemplo: "-lrt".

LDSHARED

   Comando para construir uma biblioteca compartilhada.

   Padrão: "@LDSHARED@ $(PY_LDFLAGS)".

BLDSHARED

   Comando para construir a biblioteca compartilhada "libpython".

   Padrão: "@BLDSHARED@ $(PY_CORE_LDFLAGS)".

PY_LDFLAGS

   Padrão: "$(CONFIGURE_LDFLAGS) $(LDFLAGS)".

PY_LDFLAGS_NODIST

   Padrão: "$(CONFIGURE_LDFLAGS_NODIST) $(LDFLAGS_NODIST)".

   Adicionado na versão 3.8.

PY_CORE_LDFLAGS

   Sinalizadores de vinculador usados para construir os arquivos de
   objeto do interpretador.

   Adicionado na versão 3.8.

EXE_LDFLAGS

   Sinalizadores do ligador (linker) usadas para construir alvos
   executáveis, como o interpretador. Se fornecida, a variável
   "PY_CORE_EXE_LDFLAGS" será usada em substituição a
   "PY_CORE_LDFLAGS".

   Adicionado na versão 3.15.

CONFIGURE_EXE_LDFLAGS

   Valor da variável "EXE_LDFLAGS" passado ao script "./configure".

   Adicionado na versão 3.15.

PY_CORE_EXE_LDFLAGS

   Sinalizadores do ligador (linker) para construir os alvos do
   interpretador e do executável

   Padrão: "$(PY_CORE_LDFLAGS)"

   Adicionado na versão 3.15.

-[ Notas de rodapé ]-

[7] "git clean -fdx" é uma maneira ainda mais extrema de "limpar" seu
    checkout. Ele remove todos os arquivos não conhecidos pelo Git. Ao
    procurar bugs usando "git bisect", isso é recomendado entre testes
    para garantir uma construção completamente limpa. **Use com
    cuidado**, pois isso excluirá todos os arquivos não registrados no
    Git, incluindo seu trabalho novo e não confirmado.
