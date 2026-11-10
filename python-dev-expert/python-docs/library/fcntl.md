"fcntl" --- as chamadas de sistema "fcntl" e "ioctl"
****************************************************

======================================================================

Este módulo executa o controle de arquivos e de E/S em descritores de
arquivos. É uma interface para as rotinas "fcntl()" e "ioctl()" do
Unix. Veja as páginas de manual do Unix  *fcntl(2)* e *ioctl(2)* para
mais detalhes.

Disponibilidade: Unix, not WASI.

Todas as funções neste módulo recebem um descritor de arquivo *fd*
como seu primeiro argumento. Este pode ser um descritor de arquivo
inteiro, como retornado por "sys.stdin.fileno()", ou um objeto
"io.IOBase", como o próprio "sys.stdin", que fornece um "fileno()" que
retorna um descritor de arquivo genuíno.

Alterado na versão 3.3: As operações neste módulo costumavam levantar
um "IOError", mas agora levantam um "OSError".

Alterado na versão 3.8: O módulo "fcntl" agora contém constantes
"F_ADD_SEALS", "F_GET_SEALS" e "F_SEAL_*" para selar descritores de
arquivo "os.memfd_create()".

Alterado na versão 3.9: No macOS, o módulo "fcntl" expõe a constante
"F_GETPATH", que obtém o caminho de um arquivo de um descritor de
arquivo. No Linux(>=3.15), o módulo "fcntl" expõe as constantes
"F_OFD_GETLK", "F_OFD_SETLK" e "F_OFD_SETLKW", que são usadas ao
trabalhar com travas de descrição de arquivo aberto.

Alterado na versão 3.10: No Linux >= 2.6.11, o módulo "fcntl" expõe as
constantes "F_GETPIPE_SZ" e "F_SETPIPE_SZ", que permitem verificar e
modificar o tamanho de um encadeamento, respectivamente.

Alterado na versão 3.11: No FreeBSD, o módulo "fcntl" expõe as
constantes "F_DUP2FD" e "F_DUP2FD_CLOEXEC", que permitem duplicar um
descritor de arquivo, sendo que esta última define também o
sinalizador "FD_CLOEXEC".

Alterado na versão 3.12: On Linux >= 4.5, the "fcntl" module exposes
the "FICLONE" and "FICLONERANGE" constants, which allow to share some
data of one file with another file by reflinking on some filesystems
(e.g., btrfs, OCFS2, and XFS). This behavior is commonly referred to
as "copy-on-write".

Alterado na versão 3.13: No Linux >= 2.6.32, o módulo "fcntl" expõe as
constantes "F_GETOWN_EX", "F_SETOWN_EX", "F_OWNER_TID", "F_OWNER_PID",
"F_OWNER_PGRP", que permitem direcionar sinais de disponibilidade de
E/S para uma thread, processo ou grupo de processos específico. No
Linux >= 4.13, o módulo "fcntl" expõe as constantes "F_GET_RW_HINT",
"F_SET_RW_HINT", "F_GET_FILE_RW_HINT", "F_SET_FILE_RW_HINT" e
"RWH_WRITE_LIFE_*", que permitem informar o kernel sobre o tempo de
vida relativo esperado de gravações em um determinado nó-i ou por meio
de uma descrição de arquivo aberto específica. No Linux >= 5.1 e
NetBSD, o módulo "fcntl" expõe a constante "F_SEAL_FUTURE_WRITE" para
uso com as operações "F_ADD_SEALS" e "F_GET_SEALS". No FreeBSD, o
módulo "fcntl" expõe as constantes "F_READAHEAD", "F_ISUNIONSTACK" e
"F_KINFO". No macOS e FreeBSD, o módulo "fcntl" expõe a constante
"F_RDAHEAD". No NetBSD e AIX, o módulo "fcntl" expõe a constante
"F_CLOSEM". No NetBSD, o módulo "fcntl" expõe a constante "F_MAXFD".
No macOS e no NetBSD, o módulo "fcntl" expõe as constantes
"F_GETNOSIGPIPE" e "F_SETNOSIGPIPE".

Alterado na versão 3.14: No Linux >= 6.1, o módulo "fcntl" expõe o
"F_DUPFD_QUERY" para consultar um descritor de arquivo apontando para
o mesmo arquivo.

O módulo define as seguintes funções:

fcntl.fcntl(fd, cmd, arg=0, /)

   Perform the operation *cmd* on file descriptor *fd* (file objects
   providing a "fileno()" method are accepted as well).  The values
   used for *cmd* are operating system dependent, and are available as
   constants in the "fcntl" module, using the same names as used in
   the relevant C header files. The argument *arg* can either be an
   integer value, a *bytes-like object*, or a string. The type and
   size of *arg* must match the type and size of the argument of the
   operation as specified in the relevant C documentation.

   Quando *arg* é um inteiro, a função retorna o valor de retorno
   inteiro da chamada C "fcntl()".

   When the argument is bytes-like object, it represents a binary
   structure, for example, created by "struct.pack()". A string value
   is encoded to binary using the UTF-8 encoding. The binary data is
   copied to a buffer whose address is passed to the C "fcntl()" call.
   The return value after a successful call is the contents of the
   buffer, converted to a "bytes" object. The length of the returned
   object will be the same as the length of the *arg* argument.

   Se a chamada a "fcntl()" falhar, um exceção "OSError" é levantada.

   Nota:

     If the type or size of *arg* does not match the type or size of
     the operation's argument (for example, if an integer is passed
     when a pointer is expected, or the information returned in the
     buffer by the operating system is larger than the size of *arg*),
     this is most likely to result in a segmentation violation or a
     more subtle data corruption.

   Levanta um evento de auditoria "fcntl.fcntl" com os argumentos
   "fd", "cmd", "arg".

   Alterado na versão 3.14: Adicione suporte a *objetos bytes ou
   similares* arbitrários, não apenas "bytes".

   Alterado na versão 3.15: The size of bytes-like objects is no
   longer limited to 1024 bytes.

fcntl.ioctl(fd, request, arg=0, mutate_flag=True, /)

   Esta função é idêntica à função "fcntl()", exceto que o tratamento
   de argumentos é ainda mais complicado.

   O parâmetro *request* é limitado a valores que cabem em 32 ou 64
   bits, dependendo da plataforma. Constantes adicionais de interesse
   para uso como argumento *request* podem ser encontradas no módulo
   "termios", com os mesmos nomes usados nos arquivos de cabeçalho C
   relevantes.

   O parâmetro *arg* pode ser um inteiro, um *objeto bytes ou similar*
   ou uma string. O tipo e o tamanho de *arg* devem corresponder ao
   tipo e ao tamanho do argumento da operação, conforme especificado
   na documentação C relevante.

   Se *arg* não oferecer suporte à interface de buffer de leitura e
   escrita ou o *mutate_flag* for falso, o comportamento será o mesmo
   da função "fcntl()".

   Se *arg* oferece suporte à interface de buffer de leitura e escrita
   (como "bytearray") e *mutate_flag* for true (o padrão), o buffer
   será (na prática) passado para a chamada de sistema subjacente
   "ioctl()", o código de retorno desta última será passado de volta
   para o Python que fez a chamada, e o novo conteúdo do buffer
   refletirá a ação de "ioctl()". Esta é uma pequena simplificação,
   pois se o buffer fornecido tiver menos de 1024 bytes, ele será
   primeiro copiado para um buffer estático de 1024 bytes, que será
   então passado para "ioctl()" e copiado de volta para o buffer
   fornecido.

   Se a chamada a "ioctl()" falhar, uma exceção "OSError" é levantada.

   Nota:

     If the type or size of *arg* does not match the type or size of
     the operation's argument (for example, if an integer is passed
     when a pointer is expected, or the information returned in the
     buffer by the operating system is larger than the size of *arg*),
     this is most likely to result in a segmentation violation or a
     more subtle data corruption.

   Um exemplo:

      >>> import array, fcntl, struct, termios, os
      >>> os.getpgrp()
      13341
      >>> struct.unpack('h', fcntl.ioctl(0, termios.TIOCGPGRP, "  "))[0]
      13341
      >>> buf = array.array('h', [0])
      >>> fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
      0
      >>> buf
      array('h', [13341])

   Levanta um evento de auditoria "fcntl.ioctl" com os argumentos
   "fd", "request", "arg".

   Alterado na versão 3.14: A GIL é sempre liberada durante uma
   chamada de sistema. Chamadas de sistema que falham com EINTR são
   repetidas automaticamente.

   Alterado na versão 3.15: The size of not mutated bytes-like objects
   is no longer limited to 1024 bytes.

fcntl.flock(fd, operation, /)

   Executa a operação de trava *operation* no descritor de arquivo
   *fd* (objetos arquivo que fornecem um método "fileno()" também são
   aceitos). Consulte o manual do Unix *flock(2)* para obter detalhes.
   (Em alguns sistemas, esta função é emulada usando "fcntl()".)

   Se a chamada "flock()" falhar, uma exceção "OSError" será
   levantada.

   Levanta um evento de auditoria "fcntl.flock" com os argumentos "fd"
   e "operation".

fcntl.lockf(fd, cmd, len=0, start=0, whence=0, /)

   Este é essencialmente um invólucro em torno das chamadas de trava
   "fcntl()". *fd* é o descritor de arquivo (objetos arquivo que
   fornecem um método "fileno()" também são aceitos) do arquivo para
   travar ou destravar, e *cmd* é um dos seguintes valores:

   fcntl.LOCK_UN

      Libera uma trava existente.

   fcntl.LOCK_SH

      Adquire uma trava compartilhada.

   fcntl.LOCK_EX

      Adquire uma trava exclusiva.

   fcntl.LOCK_NB

      Aplica OU (OR) bit a bit com qualquer uma das outras três
      constantes "LOCK_*" para tornar a solicitação não bloqueante.

   Se "LOCK_NB" for usado e a trava não puder ser obtido, uma exceção
   "OSError" será levantada e terá um atributo *errno* definido como
   "EACCES" ou "EAGAIN" (dependendo do sistema operacional; para
   portabilidade, verifique ambos os valores). Em pelo menos alguns
   sistemas, "LOCK_EX" só pode ser usado se o descritor de arquivo se
   referir a um arquivo aberto para escrita.

   *len* é o número de bytes para travar, *start* é o deslocamento de
   bytes em que a trava começa, em relação a *whence*, e *whence* é
   como em "io.IOBase.seek()", especificamente:

   * "0" -- relativo ao início do arquivo ("os.SEEK_SET")

   * "1" -- relativo à posição atual do buffer ("os.SEEK_CUR")

   * "2" -- relativo ao fim do arquivo ("os.SEEK_END")

   O padrão para *start* é 0, o que significa iniciar no início do
   arquivo. O padrão para *len* é 0, o que significa travar no final
   do arquivo. O padrão para *whence* também é 0.

   Levanta um evento de auditoria "fcntl.lockf" com os argumentos
   "fd", "cmd", "len", "start", "whence".

Exemplos (todos em um sistema compatível com SVR4):

   import struct, fcntl, os

   f = open(...)
   rv = fcntl.fcntl(f, fcntl.F_SETFL, os.O_NDELAY)

   lockdata = struct.pack('hhllhh', fcntl.F_WRLCK, 0, 0, 0, 0, 0)
   rv = fcntl.fcntl(f, fcntl.F_SETLKW, lockdata)

Observe que, no primeiro exemplo, a variável de valor de retorno *rv*
conterá um valor inteiro; no segundo exemplo, ela conterá um objeto
"bytes". O layout da estrutura da variável *lockdata* depende do
sistema --- portanto, usar a chamada "flock()" pode ser melhor.

Ver também:

  Módulo "os"
     Se os sinalizadores de trava "O_SHLOCK" e "O_EXLOCK" estiverem
     presentes no módulo "os" (somente no BSD), a função "os.open()"
     fornece uma alternativa às funções "lockf()" e "flock()".
