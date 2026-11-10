A biblioteca padrão do Python
*****************************

Este manual de referência de bibliotecas descreve a biblioteca padrão
que é distribuída com o Python. Ele também descreve alguns dos
componentes opcionais que são comumente incluídos nas distribuições do
Python.

Em outra parte, A Referência da Linguagem Python descreve a sintaxe e
a semântica exatas da linguagem Python, e Referência da bibliotecas
embutidas do Python descreve as funções embutidas.

A biblioteca padrão do Python é extensa, oferecendo uma ampla gama de
recursos, conforme indicado pelo longo índice listado abaixo. A
biblioteca contém módulos embutidos (escritos em C) que fornecem
acesso à funcionalidade do sistema, como E/S de arquivos que de outra
forma seriam inacessíveis para programadores Python, bem como módulos
escritos em Python que fornecem soluções padronizadas para muitos
problemas que ocorrem em programação cotidiana. Alguns desses módulos
são explicitamente projetados para incentivar e aprimorar a
portabilidade de programas em Python, abstraindo os detalhes da
plataforma em APIs neutras em plataforma.

Os instaladores do Python para a plataforma Windows geralmente incluem
toda a biblioteca padrão e muitas vezes também incluem muitos
componentes adicionais. Para sistemas operacionais semelhantes a Unix,
o Python é normalmente fornecido como uma coleção de pacotes,
portanto, pode ser necessário usar as ferramentas de empacotamento
fornecidas com o sistema operacional para obter alguns ou todos os
componentes opcionais.

Além da biblioteca padrão, há uma coleção ativa de centenas de
milhares de componentes (de programas e módulos individuais a pacotes
e frameworks de desenvolvimento de aplicativos inteiros), disponíveis
no Python Package Index.

* Introdução

  * Observações sobre disponibilidade

* Serviços de Processamento de Texto

  * "string" --- Operações comuns de strings

  * "string.templatelib" --- Suporte para literais de string template

  * "re" --- Operações com expressões regulares

  * "difflib" --- Helpers for computing deltas

  * "textwrap" --- Quebra automática e preenchimento de texto

  * "unicodedata" --- Banco de dados de Unicode

  * "stringprep" --- Preparação de string para internet

  * "readline" --- Interface para o GNU readline

  * "rlcompleter" --- Função de autocomplemento para GNU readline

* Serviços de Dados Binários

  * "struct" --- Interpreta bytes como dados binários empacotados

  * "codecs" --- Codec registry and base classes

* Tipos de Dados

  * "datetime" --- Tipos básicos de data e hora

  * "zoneinfo" --- Suporte a fuso horário da IANA

  * "calendar" --- Funções gerais relacionadas ao calendário

  * "collections" --- Tipos de dados de contêineres

  * "collections.abc" --- Classes Base Abstratas para Contêineres

  * "heapq" --- Algoritmo de fila heap

  * "bisect" --- Algoritmo de bisseção de vetor

  * "array"--- Vetores eficientes de valores numéricos

  * "weakref" --- Referências fracas

  * "types" --- Criação de tipos dinâmicos e nomes para tipos
    embutidos

  * "copy" --- Operações de cópia profunda e cópia rasa

  * "pprint" --- Impressão bonita de dados

  * "reprlib" --- Implementação alternativa à "repr()"

  * "enum" --- Suporte a enumerações

  * "graphlib" --- Funcionalidade para operar com estruturas do tipo
    grafo

* Módulos Matemáticos e Numéricos

  * "numbers" --- Classes base abstratas numéricas

  * "math" --- Funções matemáticas

  * "math.integer" --- integer-specific mathematics functions

  * "cmath" --- Funções matemáticas para números complexos

  * "decimal" --- Aritmética de ponto fixo decimal e ponto flutuante

  * "fractions" --- Números racionais

  * "random" --- Gera números pseudoaleatórios

  * "statistics" --- Funções estatísticas

* Módulos de Programação Funcional

  * "itertools" --- Funções que criam iteradores para laços eficientes

  * "functools" --- Funções e operações de ordem superior em objetos
    chamáveis

  * "operator" --- Operadores padrões como funções

* Acesso a arquivos e diretórios

  * "pathlib" --- Caminhos do sistema de arquivos orientados a objetos

  * "os.path" --- Manipulações comuns de nomes de caminhos

  * "stat" --- Interpretando resultados de "stat()"

  * "filecmp" --- Comparações de arquivos e diretórios

  * "tempfile" --- Gera arquivos temporários e diretórios

  * "glob" --- Expansão de padrão de nome de arquivo no estilo Unix

  * "fnmatch" --- Correspondência de padrões de nome de arquivo Unix

  * "linecache" --- Acesso aleatório a linhas de texto

  * "shutil" --- Operações de arquivo de alto nível

* Persistência de Dados

  * "pickle" --- Serialização de objetos Python

  * "copyreg" --- Registra funções de suporte "pickle"

  * "shelve" --- Python object persistence

  * "marshal" --- Serialização interna de objetos Python

  * "dbm" --- Interfaces para "banco de dados" Unix

  * "sqlite3" ---- interface DB-API 2.0 interface para bancos de dados
    SQLite

* Compressão de Dados e Arquivamento

  * O pacote "compression"

  * "compression.zstd" --- Compactação compatível com o formato
    Zstandard

  * "zlib" --- Compactação compatível com **gzip**

  * "gzip" --- Suporte para arquivos **gzip**

  * "bz2" --- Suporte para compressão **bzip2**

  * "lzma" --- Compressão usando o algoritmo LZMA

  * "zipfile" --- Trabalha com arquivos ZIP

  * "tarfile" --- Ler e gravar arquivos do tipo tar

* Formatos de Arquivo

  * "csv" --- Leitura e escrita de arquivos CSV

  * "configparser" --- Analisador sintático de arquivo de configuração

  * "tomllib" --- Analisa arquivos TOML

  * "netrc" --- Arquivo de processamento netrc

  * "plistlib" --- Gera e analisa arquivos Apple ".plist"

* Serviços Criptográficos

  * "hashlib" --- Resumos de mensagens e hashes seguros

  * "hmac" --- Código de autenticação de mensagem com chave hash

  * "secrets" --- Gera números aleatórios seguros para gerenciar
    segredos

* Serviços Genéricos do Sistema Operacional

  * "os" --- Diversas interfaces de sistema operacional

  * "io" --- Ferramentas essenciais para trabalhar com fluxos

  * "time" --- Acesso e conversões de tempo

  * "logging" --- Recursos de registro de eventos para Python

  * "logging.config" --- Configuração do módulo logging

  * "logging.handlers" --- Manipuladores de logging

  * "platform" ---  Acesso aos dados de identificação da plataforma
    subjacente

  * "errno" --- Símbolos padrão do sistema errno

  * "ctypes" --- Uma biblioteca de funções externas para Python

* Bibliotecas de interface de linha de comando

  * "argparse" --- Analisador sintático para opções de linha de
    comando, argumentos e subcomandos

  * "optparse" --- Analisador sintático para opções de linha de
    comando

  * "getpass" --- Entrada de senha portátil

  * "fileinput" --- Itera sobre linhas de múltiplos fluxos de entrada

  * "curses" --- Gerenciador de terminal para visualizadores de
    células de caracteres.

  * "curses.textpad" --- Text input widget for curses programs

  * "curses.ascii" --- Utilitários para caracteres ASCII

  * "curses.panel" --- Uma extensão de pilha de painéis para o curses

  * "cmd" --- Suporte para interpretadores de comando orientado a
    linhas

* Execução Concorrente

  * "threading" --- Paralelismo baseado em threads

  * "multiprocessing" --- Paralelismo baseado em processo

  * "multiprocessing.shared_memory" --- Memória compartilhada para
    acesso direto entre processos

  * O pacote "concurrent"

  * "concurrent.futures" --- Launching parallel tasks

  * "concurrent.interpreters" --- Múltiplos interpretadores no mesmo
    processo

  * "subprocess" --- Gerenciamento de subprocessos

  * "sched" --- Agendador de eventos

  * "queue" --- Uma classe de fila sincronizada

  * "contextvars" --- Variáveis de contexto

  * "_thread"--- API de segmentação de baixo nível

* Comunicação em Rede e Interprocesso

  * "asyncio" --- E/S assíncrona

  * "socket" --- Interface de rede de baixo nível

  * "ssl" --- Invólucro de TLS/SSL para objetos socket

  * "select" --- Waiting for I/O completion

  * "selectors" --- High-level I/O multiplexing

  * "signal" --- Define manipuladores para eventos assíncronos

  * "mmap" --- Suporte a arquivos mapeados na memória

* Manuseio de Dados na Internet

  * "email" --- Um e-mail e um pacote MIME manipulável

  * "json" --- Codificador e decodificador JSON

  * "mailbox" --- Manipule caixas de entradas em vários formatos

  * "mimetypes" --- Mapeia nomes de arquivos para tipos MIME

  * "base64" --- Base16, Base32, Base64, Base85 Data Encodings

  * "binascii" --- Converte entre binário e ASCII

  * "quopri" --- Codifica e decodifica dados MIME imprimidos entre
    aspas

* Ferramentas de Processamento de Markup Estruturado

  * "html" --- Suporte HTML (HyperText Markup Language)

  * "html.parser" --- Analisador simples de HTML e XHTML

  * "html.entities" --- Definições de entidades gerais de HTML

  * Módulos de Processamento de XML

  * "xml.etree.ElementTree" --- A API XML ElementTree

  * "xml.dom" --- The Document Object Model API

  * "xml.dom.minidom" --- Minimal DOM implementation

  * "xml.dom.pulldom" --- Suporte para construir árvores parciais de
    DOM

  * "xml.sax" --- Support for SAX2 parsers

  * "xml.sax.handler" --- Classes base para manipuladores de SAX

  * "xml.sax.saxutils" --- Utilitários de SAX

  * "xml.sax.xmlreader" --- Interface for XML parsers

  * "xml.parsers.expat" --- Fast XML parsing using Expat

* Protocolos de Internet e Suporte

  * "webbrowser" --- Controlador de navegador web conveniente

  * "wsgiref" --- Implementação de referência e utilitários WSGI

  * "urllib" --- Módulos de manipulação de URL

  * "urllib.request" --- Biblioteca extensível para abrir URLs

  * "urllib.response" --- Response classes used by urllib

  * "urllib.parse" --- Analisa URLs para componentes

  * "urllib.error" --- Classes de exceção levantadas por
    urllib.request

  * "urllib.robotparser" ---  Analisador sintático de robots.txt

  * "http" --- Módulos HTTP

  * "http.client" --- HTTP protocol client

  * "ftplib" --- FTP protocol client

  * "poplib" --- Cliente de protocolo POP3

  * "imaplib" --- IMAP4 protocol client

  * "smtplib" --- Cliente de protocolo SMTP

  * "uuid" --- Objetos UUID conforme **RFC 9562**

  * "socketserver" --- Um framework para servidores de rede

  * "http.server" --- HTTP servers

  * "http.cookies" --- HTTP state management

  * "http.cookiejar" --- Cookie handling for HTTP clients

  * "xmlrpc" --- Módulos de servidor e cliente XMLRPC

  * "xmlrpc.client" --- Cliente XML-RPC

  * "xmlrpc.server" --- Servidores XML-RPC básicos

  * "ipaddress" --- Biblioteca de manipulação de IPv4/IPv6

* Serviços Multimídia

  * "wave" --- Read and write WAV files

  * "colorsys" --- Conversões entre sistemas de cores

* Internacionalização

  * "gettext" --- Serviços de internacionalização multilíngues

  * "locale" --- Serviços de internacionalização

* Interfaces gráficas de usuário com Tk

  * "tkinter" --- Interface Python para Tcl/Tk

  * "tkinter.colorchooser" --- Diálogo de escolha de cor

  * "tkinter.font" --- Invólucro de fontes Tkinter

  * Tkinter dialogs

  * "tkinter.messagebox" --- Prompts de mensagem do Tkinter

  * "tkinter.scrolledtext" --- Widget de texto com *scrollbar*

  * "tkinter.dnd" --- Suporte para arrastar e soltar

  * "tkinter.ttk" --- Widgets temáticos do Tk

  * IDLE --- Editor e console Python

  * "turtle" --- Gráficos tartaruga

* Ferramentas de Desenvolvimento

  * "typing" --- Suporte para dicas de tipo

  * "pydoc" --- Gerador de documentação e sistema de ajuda online

  * Modo de Desenvolvimento do Python

  * "doctest" --- Teste exemplos interativos de Python

  * "unittest" --- Framework de testes unitários

  * "unittest.mock" --- mock object library

  * "unittest.mock" --- primeiros passos

  * "test" --- Pacote de Testes de Regressão do Python

  * "test.support" --- Utilities for the Python test suite

  * "test.support.socket_helper" --- Utilities for socket tests

  * "test.support.script_helper" --- Utilities for the Python
    execution tests

  * "test.support.bytecode_helper" --- Support tools for testing
    correct bytecode generation

  * "test.support.threading_helper" --- Utilities for threading tests

  * "test.support.os_helper" --- Utilities for os tests

  * "test.support.import_helper" --- Utilities for import tests

  * "test.support.warnings_helper" --- Utilities for warnings tests

* Depuração e perfilamento

  * Tabela de eventos de auditoria

  * "bdb" --- Framework do depurador

  * "faulthandler" --- Dump the Python traceback

  * "pdb" --- O depurador do Python

  * "profiling" --- Python profilers

  * "pstats" --- Statistics for profilers

  * "timeit" --- Mede o tempo de execução de pequenos trechos de
    código

  * "trace" --- Rastreia ou acompanha a execução de instruções Python

  * "tracemalloc" --- Trace memory allocations

* Empacotamento e Distribuição de Software

  * "ensurepip" --- Inicialização do instalador do "pip"

  * "venv" --- Criação de ambientes virtuais

  * "zipapp" --- Gerencia arquivos zip executáveis do Python

* Serviços de Tempo de Execução Python

  * "sys" --- Parâmetros e funções específicas do sistema

  * "sys.monitoring" --- Monitoramento de eventos de execução

  * "sysconfig" --- Fornece acesso às informações de configuração do
    Python

  * "builtins" --- Objetos embutidos

  * "__main__" --- Ambiente de código principal

  * "warnings" --- Controle de avisos

  * "dataclasses" --- Data Classes

  * "contextlib" --- Utilitários para contextos da instrução "with"

  * "abc" --- Classes base abstratas

  * "atexit" --- Manipuladores de saída

  * "traceback" --- Imprime ou recupera um traceback da pilha

  * "__future__" --- Definições de instruções future

  * "gc" --- Interface para o coletor de lixo

  * "inspect" --- Inspecione objetos vivos

  * "annotationlib" --- Funcionalidade para introspecção de anotações

  * "site" --- Gancho de configuração específico do site

* Interpretadores Python Personalizados

  * "code" --- Classes bases do interpretador

  * "codeop" --- Compila código Python

* Importando módulos

  * "zipimport" - Importa módulos de arquivos Zip

  * "pkgutil" --- Utilitário de extensão de pacote

  * "modulefinder" --- Procura módulos usados por um script

  * "runpy" --- Localizando e executando módulos Python

  * "importlib" --- A implementação de "import"

  * "importlib.resources" -- Leitura, abertura e acesso a recursos de
    pacotes

  * "importlib.resources.abc" -- Classes base abstratas para recursos

  * "importlib.metadata" -- Acessando metadados do pacote

  * A inicialização do caminho de pesquisa de módulos "sys.path"

* Serviços da Linguagem Python

  * "ast" --- Árvores de sintaxe abstrata

  * "symtable" --- Acesso a tabela de símbolos do compilador

  * "token" --- Constantes usadas com árvores de análises do Python

  * "keyword" --- Testando palavras reservadas do Python

  * "tokenize" --- Tokenizador para código-fonte Python

  * "tabnanny" --- Detecção de indentação ambígua

  * "pyclbr" --- Suporte a navegador de módulos do Python

  * "py_compile" --- Compila arquivos fonte do Python

  * "compileall" --- Compilar bibliotecas do Python para bytecode

  * "dis" --- Disassembler de bytecode do Python

  * "pickletools" --- Ferramentas para desenvolvedores pickle

* Serviços Específicos do MS Windows

  * "msvcrt" --- Rotinas úteis do runtime MS VC++

  * "winreg" --- Acesso aos registros do Windows

  * "winsound" --- Interface de reprodução de som para o Windows

* Serviços específicos do Unix

  * "shlex" --- Simple lexical analysis

  * "posix" --- As chamadas de sistema mais comuns do POSIX

  * "pwd" --- A senha do banco de dados

  * "grp" --- O banco de dados de grupos

  * "termios" --- Controle de tty no estilo POSIX

  * "tty" --- Funções de controle de terminal

  * "pty" --- Utilitários de pseudoterminal

  * "fcntl" --- as chamadas de sistema "fcntl" e "ioctl"

  * "resource" --- Informação de uso de recursos

  * "syslog" --- Rotinas da biblioteca syslog do Unix

* Interface de linha de comando (CLI) de módulos

* Módulos substituídos

  * "getopt" --- Analisador sintático no estilo C para opções de linha
    de comando

  * "profile" --- Pure Python profiler

* Módulos removidos

* Considerações de segurança
