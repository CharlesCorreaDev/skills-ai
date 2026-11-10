"errno" --- Símbolos padrão do sistema errno
********************************************

======================================================================

Este módulo disponibiliza símbolos de sistema padrão "errno". O valor
de cada símbolo é o valor inteiro correspondente. Os nomes e
descrições são emprestados de "linux/include/errno.h", que deve ser
tudo inclusivo.

errno.errorcode

   Dicionário que fornece um mapeamento do valor errno para o nome da
   string no sistema subjacente. Por exemplo,
   "errno.errorcode[errno.EPERM]" mapeia para "'EPERM'".

Para traduzir um código de erro numérico em uma mensagem de erro, use
"os.strerror()".

Da lista a seguir, símbolos que não são usados na plataforma atual não
são definidos pelo módulo. A lista específica de símbolos definidos
está disponível como "errno.errorcode.keys()". Os símbolos disponíveis
podem incluir:

errno.EPERM

   Operação não permitida. Este erro é mapeado para a exceção
   "PermissionError".

errno.ENOENT

   Arquivo ou diretório inexistente. Este erro é mapeado para a
   exceção "FileNotFoundError".

errno.ESRCH

   Processo inexistente. Este erro é mapeado para a exceção
   "ProcessLookupError".

errno.EINTR

   Chamada de sistema interrompida. Este erro é mapeado para a exceção
   "InterruptedError".

errno.EIO

   Erro de E/S

errno.ENXIO

   Endereço ou dispositivo inexistente

errno.E2BIG

   Lista de argumentos muito longa

errno.ENOEXEC

   Erro no formato exec

errno.EBADF

   Descritor de arquivo inválido

errno.ECHILD

   Não há processos filhos. Este erro é mapeado para a exceção
   "ChildProcessError".

errno.EAGAIN

   Tente novamente. Este erro é mapeado para a exceção
   "BlockingIOError".

errno.ENOMEM

   Memória insuficiente

errno.EACCES

   Permissão negada. Este erro é mapeado para a exceção
   "PermissionError".

errno.EFAULT

   Endereço inválido

errno.ENOTBLK

   Dispositivo de bloco requerido

errno.EBUSY

   Dispositivo ou recurso ocupado

errno.EEXIST

   Arquivo existe. Este erro é mapeado para a exceção
   "FileExistsError".

errno.EXDEV

   Link entre dispositivos inválido

errno.ENODEV

   Dispositivo inexistente

errno.ENOTDIR

   Não é um diretório. Este erro é mapeado para a exceção
   "NotADirectoryError".

errno.EISDIR

   É um diretório. Este erro é mapeado para a exceção
   "IsADirectoryError".

errno.EINVAL

   Argumento inválido

errno.ENFILE

   Estouro de tabela de arquivos

errno.EMFILE

   Muitos arquivos abertos

errno.ENOTTY

   Not a typewriter

errno.ETXTBSY

   Arquivo texto ocupado

errno.EFBIG

   Arquivo muito grande

errno.ENOSPC

   Não há espaço disponível no dispositivo

errno.ESPIPE

   Procura ilegal

errno.EROFS

   Sistema de arquivos de somente leitura

errno.EMLINK

   Muitos links

errno.EPIPE

   Pipe quebrado. Este erro é mapeado para a exceção
   "BrokenPipeError".

errno.EDOM

   Argumento matemático fora do domínio da função

errno.ERANGE

   Resultado matemático não representável

errno.EDEADLK

   Ocorreria um impasse (deadlock) de recursos

errno.ENAMETOOLONG

   Nome de arquivo muito longo

errno.ENOLCK

   Nenhuma trava de registro disponível

errno.ENOSYS

   Função não implementada

errno.ENOTEMPTY

   Diretório não vazio

errno.ELOOP

   Foram encontrados muitos links simbólicos

errno.EWOULDBLOCK

   Operation causaria bloqueio. Este erro é mapeado para a exceção
   "BlockingIOError".

errno.ENOMSG

   Nenhuma mensagem do tipo desejado

errno.EIDRM

   Identificador removido

errno.ECHRNG

   Número do canal fora do intervalo

errno.EL2NSYNC

   Não sincronizado nível 2

errno.EL3HLT

   Parada de sistema nível 3

errno.EL3RST

   Reinicialização nível 3

errno.ELNRNG

   Número de link fora da faixa

errno.EUNATCH

   Driver de protocolo não anexado

errno.ENOCSI

   Não há estrutura CSI disponível

errno.EL2HLT

   Parada de sistema nível 2

errno.EBADE

   Troca inválida

errno.EBADR

   Descritor de requisição inválido

errno.EXFULL

   Troca completa

errno.ENOANO

   Sem anode

errno.EBADRQC

   Código de requisição inválido

errno.EBADSLT

   Slot inválido

errno.EDEADLOCK

   Erro de impasse em travamento de arquivo

errno.EBFONT

   Formato inválido do arquivo de fonte

errno.ENOSTR

   Dispositivo não é um stream

errno.ENODATA

   Não há dados disponíveis

errno.ETIME

   Temporizador expirado

errno.ENOSR

   Sem recursos de streams

errno.ENONET

   A máquina não está na rede

errno.ENOPKG

   Pacote não instalado

errno.EREMOTE

   O objeto é remoto

errno.ENOLINK

   A conexão foi rompida

errno.EADV

   Erro de anúncio

errno.ESRMNT

   Erro Srmount

errno.ECOMM

   Erro de comunicação ao enviar

errno.EPROTO

   Erro de Protocolo

errno.EMULTIHOP

   Tentativa de hops múltiplos

errno.EDOTDOT

   Erro específico de RFS

errno.EBADMSG

   Não é uma mensagem de dados

errno.EOVERFLOW

   Valor muito grande para o tipo de dados definido

errno.ENOTUNIQ

   O nome não é único na rede

errno.EBADFD

   Descritor de arquivo em mal estado

errno.EREMCHG

   Endereço remoto mudou

errno.ELIBACC

   Não é possível acessar uma biblioteca compartilhada necessária

errno.ELIBBAD

   Acessando uma biblioteca compartilhado corrompida

errno.ELIBSCN

   Seção .lib corrompida em a.out

errno.ELIBMAX

   Tentando ligar em muitas bibliotecas compartilhadas

errno.ELIBEXEC

   Não é possível executar uma biblioteca compartilhada diretamente

errno.EILSEQ

   Sequência de bytes ilegal

errno.ERESTART

   Chamada de sistema interrompida deve ser reiniciada

errno.ESTRPIPE

   Erro de fluxos de pipe

errno.EUSERS

   Muitos usuários

errno.ENOTSOCK

   Operação socket em um arquivo não-socket

errno.EDESTADDRREQ

   Endereço de destino necessário

errno.EMSGSIZE

   Mensagem muito longa

errno.EPROTOTYPE

   Tipo errado de protocolo para socket

errno.ENOPROTOOPT

   Protocolo não disponível

errno.EPROTONOSUPPORT

   Protocolo sem suporte

errno.ESOCKTNOSUPPORT

   Tipo socket sem suporte

errno.EOPNOTSUPP

   Operação sem suporte na extremidade do transporte

errno.ENOTSUP

   Operação sem suporte

   Adicionado na versão 3.2.

errno.EPFNOSUPPORT

   Família de protocolo sem suporte

errno.EAFNOSUPPORT

   Família de endereços sem suporte pelo protocolo

errno.EADDRINUSE

   Endereço já em uso

errno.EADDRNOTAVAIL

   Não é possível acessar o endereço requisitado

errno.ENETDOWN

   A rede não responde

errno.ENETUNREACH

   A rede está fora de alcance

errno.ENETRESET

   A rede desconectou-se ao reiniciar

errno.ECONNABORTED

   O software causou a interrupção da conexão. Este erro é mapeado
   para a exceção "ConnectionAbortedError".

errno.ECONNRESET

   Conexão fechada pela outra ponta. Este erro é mapeado para a
   exceção "ConnectionResetError".

errno.ENOBUFS

   Não há espaço de buffer disponível

errno.EISCONN

   A extremidade do transporte já está conectada

errno.ENOTCONN

   A extremidade do transporte não está conectada

errno.ESHUTDOWN

   Cannot send after transport endpoint shutdown. This error is mapped
   to the exception "BrokenPipeError".

errno.ETOOMANYREFS

   Too many references: cannot splice

errno.ETIMEDOUT

   Connection timed out. This error is mapped to the exception
   "TimeoutError".

errno.ECONNREFUSED

   Connection refused. This error is mapped to the exception
   "ConnectionRefusedError".

errno.EHOSTDOWN

   Host is down

errno.EHOSTUNREACH

   No route to host

errno.EHWPOISON

   Memory page has hardware error.

   Adicionado na versão 3.14.

errno.EALREADY

   Operation already in progress. This error is mapped to the
   exception "BlockingIOError".

errno.EINPROGRESS

   Operation now in progress. This error is mapped to the exception
   "BlockingIOError".

errno.ESTALE

   Stale NFS file handle

errno.EUCLEAN

   Structure needs cleaning

errno.ENOTNAM

   Not a XENIX named type file

errno.ENAVAIL

   No XENIX semaphores available

errno.EISNAM

   É um arquivo de tipo nomeado

errno.EREMOTEIO

   Erro de E/S remoto

errno.EDQUOT

   Quota exceeded

errno.EQFULL

   Interface output queue is full

   Adicionado na versão 3.11.

errno.ENOMEDIUM

   No medium found

errno.EMEDIUMTYPE

   Wrong medium type

errno.ENOKEY

   Required key not available

errno.EKEYEXPIRED

   Key has expired

errno.EKEYREVOKED

   Key has been revoked

errno.EKEYREJECTED

   Key was rejected by service

errno.ERFKILL

   Operation not possible due to RF-kill

errno.ELOCKUNMAPPED

   Locked lock was unmapped

errno.ENOTACTIVE

   Facility is not active

errno.EAUTH

   Authentication error

   Adicionado na versão 3.2.

errno.EBADARCH

   Bad CPU type in executable

   Adicionado na versão 3.2.

errno.EBADEXEC

   Bad executable (or shared library)

   Adicionado na versão 3.2.

errno.EBADMACHO

   Malformed Mach-o file

   Adicionado na versão 3.2.

errno.EDEVERR

   Device error

   Adicionado na versão 3.2.

errno.EFTYPE

   Inappropriate file type or format

   Adicionado na versão 3.2.

errno.ENEEDAUTH

   Need authenticator

   Adicionado na versão 3.2.

errno.ENOATTR

   Attribute not found

   Adicionado na versão 3.2.

errno.ENOPOLICY

   Policy not found

   Adicionado na versão 3.2.

errno.EPROCLIM

   Too many processes

   Adicionado na versão 3.2.

errno.EPROCUNAVAIL

   Bad procedure for program

   Adicionado na versão 3.2.

errno.EPROGMISMATCH

   Program version wrong

   Adicionado na versão 3.2.

errno.EPROGUNAVAIL

   RPC prog. not avail

   Adicionado na versão 3.2.

errno.EPWROFF

   Device power is off

   Adicionado na versão 3.2.

errno.EBADRPC

   RPC struct is bad

   Adicionado na versão 3.2.

errno.ERPCMISMATCH

   RPC version wrong

   Adicionado na versão 3.2.

errno.ESHLIBVERS

   Shared library version mismatch

   Adicionado na versão 3.2.

errno.ENOTCAPABLE

   Capabilities insufficient. This error is mapped to the exception
   "PermissionError".

   Disponibilidade: WASI, FreeBSD

   Adicionado na versão 3.11.1.

errno.ECANCELED

   Operation canceled

   Adicionado na versão 3.2.

errno.EOWNERDEAD

   Owner died

   Adicionado na versão 3.2.

errno.ENOTRECOVERABLE

   State not recoverable

   Adicionado na versão 3.2.
