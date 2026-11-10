Serviços Genéricos do Sistema Operacional
*****************************************

Os módulos descritos neste capítulo fornecem interfaces aos recursos
do sistema operacional e que estão disponíveis em (quase) todos os
sistemas operacionais, como arquivos e um relógio. As interfaces
geralmente são modeladas após as interfaces Unix ou C, mas elas também
estão disponíveis na maioria dos outros sistemas. Aqui temos uma visão
geral:

* "os" --- Diversas interfaces de sistema operacional

  * Nomes de arquivos, argumentos de linha de comando e variáveis de
    ambiente

  * Modo UTF-8 do Python

  * Parâmetros de processo

  * Criação de objetos arquivos

  * Operações dos descritores de arquivos

    * Consultando o tamanho de um terminal

    * Herança de descritores de arquivos

  * Arquivos e diretórios

    * Descritores de arquivo de temporizador

    * Atributos estendidos do Linux

  * Gerenciamento de processo

  * Interface do agendador

  * Diversas informações de sistema

  * Números aleatórios

* "io" --- Ferramentas essenciais para trabalhar com fluxos

  * Visão Geral

    * E/S de texto

    * E/S binária

    * E/S bruta

  * Codificação do texto

    * Ativar EncodingWarning

  * Interface de alto nível do módulo

  * hierarquia de classe

    * I/O base classes

    * Raw file I/O

    * Buffered streams

    * E/S de texto

  * Static typing

  * Desempenho

    * E/S binária

    * E/S de texto

    * Multi-threading

    * Reentrancy

* "time" --- Acesso e conversões de tempo

  * Funções

  * Constantes de ID de Relógio

  * Constantes de Fuso Horário

* "logging" --- Recursos de registro de eventos para Python

  * Objetos Logger

  * Níveis de Logging

  * Objetos Handler

  * Formatter Objects

  * Filter Objects

  * LogRecord Objects

  * Atributos LogRecord

  * LoggerAdapter Objects

  * Thread Safety

  * Funções de Nível de Módulo

  * Module-Level Attributes

  * Integration with the warnings module

* "logging.config" --- Configuração do módulo logging

  * Funções de configuração

  * Considerações de segurança

  * Esquema do Dicionário de Configuração

    * Detalhes do Esquema de Dicionário

    * Configuração Incremental

    * Conexões de objeto

    * Objetos definidos pelo usuário

    * Ordem de configuração de manipuladores

    * Acesso a objetos externos

    * Acesso a objetos internos

    * Resolução de importações e importadores personalizados

    * Configurando QueueHandler e QueueListener

  * Formato do arquivo de configuração

* "logging.handlers" --- Manipuladores de logging

  * StreamHandler

  * FileHandler

  * NullHandler

  * WatchedFileHandler

  * BaseRotatingHandler

  * RotatingFileHandler

  * TimedRotatingFileHandler

  * SocketHandler

  * DatagramHandler

  * SysLogHandler

  * NTEventLogHandler

  * SMTPHandler

  * MemoryHandler

  * HTTPHandler

  * QueueHandler

  * QueueListener

* "platform" ---  Acesso aos dados de identificação da plataforma
  subjacente

  * Multiplataforma

  * Plataforma Windows

  * Plataforma macOS

  * Plataforma iOS

  * Plataformas Unix

  * Plataformas Linux

  * Plataforma Android

  * Uso na linha de comando

* "errno" --- Símbolos padrão do sistema errno

* "ctypes" --- Uma biblioteca de funções externas para Python

  * Tutorial do ctypes

    * Carregando bibliotecas de ligação dinâmica

    * Acessando funções de dlls carregadas

    * Chamando funções

    * Tipos de dados fundamentais

    * Chamando funções, continuação

    * Chamando funções variadas

    * Chamando funções com seus próprios tipos de dados personalizados

    * Especificando os tipos de argumentos necessários (protótipos de
      função)

    * Tipos de Retorno

    * Passando ponteiros (ou: passando parâmetros por referência)

    * Estruturas e uniões

    * Layout, alinhamento e ordem de bytes de estrutura/união

    * Campos de bit em estruturas e uniões

    * Vetores

    * Ponteiros

    * Segurança de thread (Thread safety) sem o GIL

    * Conversão de Tipos

    * Tipos Incompletos

    * Funções Callbacks

    * Acessando valores exportados de dlls

    * Surpresas

    * Tipos de dados de tamanho variável

  * Referência ctypes

    * Loading shared libraries

    * Encontrando bibliotecas compartilhadas

    * Listing loaded shared libraries

    * Foreign functions

    * Function prototypes

    * Funções utilitárias

    * Data types

    * Tipos de dados fundamentais

    * Windows data types

      * Simple types

      * Handle types

      * Structures

      * Pointer types

      * Constants and functions

    * Tipos de dados estruturados

    * Arrays and pointers

    * Exceções
