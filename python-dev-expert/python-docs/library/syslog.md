"syslog" --- Rotinas da biblioteca syslog do Unix
*************************************************

======================================================================

Este módulo fornece uma interface para as rotinas da biblioteca
"syslog" do Unix. Consulte as páginas de manual do Unix para uma
descrição detalhada do recurso "syslog".

Disponibilidade: Unix, not WASI, not iOS.

Este módulo é uma camada para a família de rotinas "syslog" do
sistema. Uma biblioteca Python pura que pode se comunicar com um
servidor syslog está disponível no módulo "logging.handlers" como
"SysLogHandler".

O módulo define as seguintes funções:

syslog.syslog(message)
syslog.syslog(priority, message)

   Envia a string *message* para o registrador do sistema. Uma nova
   linha final é adicionada, se necessário. Cada mensagem é marcada
   com uma prioridade composta por um *facility* e um *level*. O
   argumento opcional *priority*, cujo padrão é "LOG_INFO", determina
   a prioridade da mensagem. Se a facilidade não está codificada em
   *priority* usando o OU lógico ("LOG_INFO | LOG_USER"), o valor dado
   na chamada "openlog()" é usado.

   If "openlog()" has not been called prior to the call to "syslog()",
   "openlog()" will be called with no arguments.

   Levanta um evento de auditoria "syslog.syslog" com os argumentos
   "priority", "message".

   Alterado na versão 3.2: In previous versions, "openlog()" would not
   be called automatically if it wasn't called prior to the call to
   "syslog()", deferring to the syslog implementation to call
   "openlog()".

   Alterado na versão 3.12: This function is restricted in
   subinterpreters. (Only code that runs in multiple interpreters is
   affected and the restriction is not relevant for most users.)
   "openlog()" must be called in the main interpreter before
   "syslog()" may be used in a subinterpreter.  Otherwise it will
   raise "RuntimeError".

syslog.openlog([ident[, logoption[, facility]]])

   Logging options of subsequent "syslog()" calls can be set by
   calling "openlog()".  "syslog()" will call "openlog()" with no
   arguments if the log is not currently open.

   O argumento nomeado opcional *ident* é uma string que é prefixada a
   cada mensagem, e o padrão é "sys.argv[0]" com os componentes do
   caminho inicial removidos. O argumento nomeado opcional *logoption*
   (o padrão é 0) é um campo de bits -- veja abaixo os valores
   possíveis para combinar. O argumento nomeado opcional *facility* (o
   padrão é "LOG_USER") define o recurso padrão para mensagens que não
   possuem um recurso explicitamente codificado.

   Levanta um evento de auditoria "syslog.openlog" com os argumentos
   "ident", "logoption", "facility".

   Alterado na versão 3.2: Nas versões anteriores, os argumentos
   nomeados não eram permitidos e *ident* era obrigatório.

   Alterado na versão 3.12: Esta função é restrita em
   subinterpretadores. (Apenas o código que executa em vários
   interpretadores é afetado e a restrição não é relevante para a
   maioria dos usuários.) Isso deve ser chamado no interpretador
   principal.Vai levantar "RuntimeError" se chamado em um
   subinterpretador.

syslog.closelog()

   Redefine os valores do módulo syslog e chama a biblioteca de
   sistema "closelog()".

   This causes the module to behave as it does when initially
   imported.  For example, "openlog()" will be called on the first
   "syslog()" call (if "openlog()" hasn't already been called), and
   *ident* and other "openlog()" parameters are reset to defaults.

   Levanta um evento de auditoria "syslog.closelog" sem argumentos.

   Alterado na versão 3.12: Esta função é restrita em
   subinterpretadores. (Apenas o código que executa em vários
   interpretadores é afetado e a restrição não é relevante para a
   maioria dos usuários.) Isso deve ser chamado no interpretador
   principal.Vai levantar "RuntimeError" se chamado em um
   subinterpretador.

syslog.setlogmask(maskpri)

   Set the priority mask to *maskpri* and return the previous mask
   value.  Calls to "syslog()" with a priority level not set in
   *maskpri* are ignored. The default is to log all priorities.  The
   function "LOG_MASK(pri)" calculates the mask for the individual
   priority *pri*.  The function "LOG_UPTO(pri)" calculates the mask
   for all priorities up to and including *pri*.

   Levanta um evento de auditoria "syslog.setlogmask" com o argumento
   "maskpri".

O módulo define as seguintes constantes:

syslog.LOG_EMERG
syslog.LOG_ALERT
syslog.LOG_CRIT
syslog.LOG_ERR
syslog.LOG_WARNING
syslog.LOG_NOTICE
syslog.LOG_INFO
syslog.LOG_DEBUG

   Níveis de prioridade (alto a baixo).

syslog.LOG_AUTH
syslog.LOG_AUTHPRIV
syslog.LOG_CRON
syslog.LOG_DAEMON
syslog.LOG_FTP
syslog.LOG_INSTALL
syslog.LOG_KERN
syslog.LOG_LAUNCHD
syslog.LOG_LPR
syslog.LOG_MAIL
syslog.LOG_NETINFO
syslog.LOG_NEWS
syslog.LOG_RAS
syslog.LOG_REMOTEAUTH
syslog.LOG_SYSLOG
syslog.LOG_USER
syslog.LOG_UUCP
syslog.LOG_LOCAL0
syslog.LOG_LOCAL1
syslog.LOG_LOCAL2
syslog.LOG_LOCAL3
syslog.LOG_LOCAL4
syslog.LOG_LOCAL5
syslog.LOG_LOCAL6
syslog.LOG_LOCAL7

   Facilidades, dependendo da disponibilidade em "<syslog.h>" para
   "LOG_AUTHPRIV", "LOG_FTP", "LOG_NETINFO", "LOG_REMOTEAUTH",
   "LOG_INSTALL" e "LOG_RAS".

   Alterado na versão 3.13: Adicionados "LOG_FTP", "LOG_NETINFO",
   "LOG_REMOTEAUTH", "LOG_INSTALL", "LOG_RAS" e "LOG_LAUNCHD".

syslog.LOG_PID
syslog.LOG_CONS
syslog.LOG_NDELAY
syslog.LOG_ODELAY
syslog.LOG_NOWAIT
syslog.LOG_PERROR

   Opções de log, dependendo da disponibilidade em "<syslog.h>" para
   "LOG_ODELAY", "LOG_NOWAIT" e "LOG_PERROR".


Exemplos
========


Exemplo simples
---------------

Um conjunto simples de exemplos:

   import syslog

   syslog.syslog('Processing started')
   if error:
       syslog.syslog(syslog.LOG_ERR, 'Processing started')

Um exemplo de configuração de algumas opções de log, isso incluiria o
ID do processo nas mensagens registradas e escreveria as mensagens no
recurso de destino usado para o log de correio:

   syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_MAIL)
   syslog.syslog('E-mail processing initiated...')
