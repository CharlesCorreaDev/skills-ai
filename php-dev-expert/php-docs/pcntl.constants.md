# Constantes predefinidas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pcntl.constants.php

---

# Constantes predefinidas

A lista de sinais a seguir é suportada pelas funções de Controle de
Processo. Consulte a página man signal(7) do sistema operacional para obter detalhes
sobre o comportamento padrão desses sinais.

**Constantes de controle de processo**

**`WNOHANG`** ([int](language.types.integer.md))

**`WUNTRACED`** ([int](language.types.integer.md))

**`WCONTINUED`** ([int](language.types.integer.md))

**`WEXITED`** ([int](language.types.integer.md))

**`WSTOPPED`** ([int](language.types.integer.md))

**`WNOWAIT`** ([int](language.types.integer.md))

**Constantes SIG\_\***

**`SIG_IGN`** ([int](language.types.integer.md))

**`SIG_DFL`** ([int](language.types.integer.md))

**`SIG_ERR`** ([int](language.types.integer.md))

**`SIGHUP`** ([int](language.types.integer.md))

**`SIGINFO`** ([int](language.types.integer.md))

**`SIGINT`** ([int](language.types.integer.md))

**`SIGQUIT`** ([int](language.types.integer.md))

**`SIGILL`** ([int](language.types.integer.md))

**`SIGTRAP`** ([int](language.types.integer.md))

**`SIGABRT`** ([int](language.types.integer.md))

**`SIGIOT`** ([int](language.types.integer.md))

**`SIGBUS`** ([int](language.types.integer.md))

**`SIGFPE`** ([int](language.types.integer.md))

**`SIGKILL`** ([int](language.types.integer.md))

**`SIGUSR1`** ([int](language.types.integer.md))

**`SIGSEGV`** ([int](language.types.integer.md))

**`SIGUSR2`** ([int](language.types.integer.md))

**`SIGPIPE`** ([int](language.types.integer.md))

**`SIGALRM`** ([int](language.types.integer.md))

**`SIGTERM`** ([int](language.types.integer.md))

**`SIGSTKFLT`** ([int](language.types.integer.md))

**`SIGCLD`** ([int](language.types.integer.md))

**`SIGCHLD`** ([int](language.types.integer.md))

**`SIGCONT`** ([int](language.types.integer.md))

**`SIGSTOP`** ([int](language.types.integer.md))

**`SIGTSTP`** ([int](language.types.integer.md))

**`SIGTTIN`** ([int](language.types.integer.md))

**`SIGTTOU`** ([int](language.types.integer.md))

**`SIGURG`** ([int](language.types.integer.md))

**`SIGXCPU`** ([int](language.types.integer.md))

**`SIGXFSZ`** ([int](language.types.integer.md))

**`SIGVTALRM`** ([int](language.types.integer.md))

**`SIGPROF`** ([int](language.types.integer.md))

**`SIGWINCH`** ([int](language.types.integer.md))

**`SIGPOLL`** ([int](language.types.integer.md))

**`SIGIO`** ([int](language.types.integer.md))

**`SIGPWR`** ([int](language.types.integer.md))

**`SIGSYS`** ([int](language.types.integer.md))

**`SIGBABY`** ([int](language.types.integer.md))

**`SIGRTMIN`** ([int](language.types.integer.md))

**`SIGRTMAX`** ([int](language.types.integer.md))

**`SIG_BLOCK`** ([int](language.types.integer.md))

**`SIG_UNBLOCK`** ([int](language.types.integer.md))

**`SIG_SETMASK`** ([int](language.types.integer.md))

**`SIGCKPT`** ([int](language.types.integer.md))
:   Gera/restaura um ponto de verificação.
    Disponível a partir do PHP 8.4.0 (somente DragonFlyBSD).

**`SIGCKPTEXIT`** ([int](language.types.integer.md))
:   Gera/restaura um ponto de verificação e sai.
    Disponível a partir do PHP 8.4.0 (somente DragonFlyBSD).

**Constantes SI\_\***

**`SI_USER`** ([int](language.types.integer.md))

**`SI_NOINFO`** ([int](language.types.integer.md))

**`SI_KERNEL`** ([int](language.types.integer.md))

**`SI_QUEUE`** ([int](language.types.integer.md))

**`SI_TIMER`** ([int](language.types.integer.md))

**`SI_MSGGQ`** ([int](language.types.integer.md))

**`SI_ASYNCIO`** ([int](language.types.integer.md))

**`SI_SIGIO`** ([int](language.types.integer.md))

**`SI_TKILL`** ([int](language.types.integer.md))

**`SI_MESGQ`** ([int](language.types.integer.md))

**Constantes CLD\_\***

**`CLD_EXITED`** ([int](language.types.integer.md))

**`CLD_KILLED`** ([int](language.types.integer.md))

**`CLD_DUMPED`** ([int](language.types.integer.md))

**`CLD_TRAPPED`** ([int](language.types.integer.md))

**`CLD_STOPPED`** ([int](language.types.integer.md))

**`CLD_CONTINUED`** ([int](language.types.integer.md))

**Constantes TRAP\_\***

**`TRAP_BRKPT`** ([int](language.types.integer.md))

**`TRAP_TRACE`** ([int](language.types.integer.md))

**Constantes POLL\_\***

**`POLL_IN`** ([int](language.types.integer.md))

**`POLL_OUT`** ([int](language.types.integer.md))

**`POLL_MSG`** ([int](language.types.integer.md))

**`POLL_ERR`** ([int](language.types.integer.md))

**`POLL_PRI`** ([int](language.types.integer.md))

**`POLL_HUP`** ([int](language.types.integer.md))

**Constantes ILL\_\***

**`ILL_ILLOPC`** ([int](language.types.integer.md))

**`ILL_ILLOPN`** ([int](language.types.integer.md))

**`ILL_ILLADR`** ([int](language.types.integer.md))

**`ILL_ILLTRP`** ([int](language.types.integer.md))

**`ILL_PRVOPC`** ([int](language.types.integer.md))

**`ILL_PRVREG`** ([int](language.types.integer.md))

**`ILL_COPROC`** ([int](language.types.integer.md))

**`ILL_BADSTK`** ([int](language.types.integer.md))

**Constantes FPE\_\***

**`FPE_INTDIV`** ([int](language.types.integer.md))

**`FPE_INTOVF`** ([int](language.types.integer.md))

**`FPE_FLTDIV`** ([int](language.types.integer.md))

**`FPE_FLTOVF`** ([int](language.types.integer.md))

**`FPE_FLTUND`** ([int](language.types.integer.md))

**`FPE_FLTRES`** ([int](language.types.integer.md))

**`FPE_FLTINV`** ([int](language.types.integer.md))

**`FPE_FLTSUB`** ([int](language.types.integer.md))

**Constantes SEGV\_\***

**`SEGV_MAPERR`** ([int](language.types.integer.md))

**`SEGV_ACCERR`** ([int](language.types.integer.md))

**Constantes BUS\_\***

**`BUS_ADRALN`** ([int](language.types.integer.md))

**`BUS_ADRERR`** ([int](language.types.integer.md))

**`BUS_OBJERR`** ([int](language.types.integer.md))

**Constantes CLONE\_\***

**`CLONE_NEWNS`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 7.4.0

**`CLONE_NEWIPC`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 7.4.0

**`CLONE_NEWUTS`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 7.4.0

**`CLONE_NEWNET`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 7.4.0

**`CLONE_NEWPID`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 7.4.0

**`CLONE_NEWUSER`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 7.4.0

**`CLONE_NEWCGROUP`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 7.4.0

**Constantes PRIO\_\***

**`PRIO_PGRP`** ([int](language.types.integer.md))

**`PRIO_USER`** ([int](language.types.integer.md))

**`PRIO_PROCESS`** ([int](language.types.integer.md))

**`PRIO_DARWIN_BG`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 8.1.0.

**`PRIO_DARWIN_THREAD`** ([int](language.types.integer.md))
:   Disponível a partir do PHP 8.1.0.

| Constantes | Descrição |
| --- | --- |
**Constantes de erro de controle de processo**| **`PCNTL_E2BIG`** ([int](language.types.integer.md)) | Lista de argumentos muito longa |
| **`PCNTL_EACCES`** ([int](language.types.integer.md)) | Permissão negada |
| **`PCNTL_EAGAIN`** ([int](language.types.integer.md)) | Recurso temporariamente indisponivel |
| **`PCNTL_ECAPMODE`** ([int](language.types.integer.md)) | O processo tentou uma operação não permitida no modo de capacidade durante a execução no modo de capacidade. |
| **`PCNTL_ECHILD`** ([int](language.types.integer.md)) | Nenhum processo filho |
| **`PCNTL_EFAULT`** ([int](language.types.integer.md)) | Endereço incorreto |
| **`PCNTL_EINTR`** ([int](language.types.integer.md)) | Chamada de função interrompida |
| **`PCNTL_EINVAL`** ([int](language.types.integer.md)) | Argumento inválido |
| **`PCNTL_EIO`** ([int](language.types.integer.md)) | Erro de entrada/saída |
| **`PCNTL_EISDIR`** ([int](language.types.integer.md)) | É um diretório |
| **`PCNTL_ELIBBAD`** ([int](language.types.integer.md)) | Acessando uma biblioteca compartilhada corrompida. |
| **`PCNTL_ELOOP`** ([int](language.types.integer.md)) | Muitos níveis de links simbólicos |
| **`PCNTL_EMFILE`** ([int](language.types.integer.md)) | Muitos arquivos abertos. Geralmente causado por exceder o limite de recursos `RLIMIT_NOFILE`. Também pode ser causado por exceder o limite especificado em /proc/sys/fs/nr\_open. |
| **`PCNTL_ENAMETOOLONG`** ([int](language.types.integer.md)) | Nome do arquivo muito longo |
| **`PCNTL_ENFILE`** ([int](language.types.integer.md)) | Muitos arquivos abertos no sistema. No Linux, isso provavelmente é resultado de encontrar o limite /proc/sys/fs/file-max. |
| **`PCNTL_ENOENT`** ([int](language.types.integer.md)) | Não existe tal arquivo ou diretório. Normalmente, esse erro ocorre quando um nome de caminho especificado não existe, ou um dos componentes no prefixo de diretório de um nome de caminho não existe, ou o nome de caminho especificado é um link simbólico pendente. |
| **`PCNTL_ENOEXEC`** ([int](language.types.integer.md)) | Erro de formato Exec |
| **`PCNTL_ENOMEM`** ([int](language.types.integer.md)) | Espaço insuficiente/não é possível alocar memória |
| **`PCNTL_ENOSPC`** ([int](language.types.integer.md)) | Não há mais espaço no dispositivo |
| **`PCNTL_ENOTDIR`** ([int](language.types.integer.md)) | Não é um diretório |
| **`PCNTL_EPERM`** ([int](language.types.integer.md)) | Operação não permitida |
| **`PCNTL_ESRCH`** ([int](language.types.integer.md)) | Processo não existe |
| **`PCNTL_ETXTBSY`** ([int](language.types.integer.md)) | Arquivo de texto ocupado |
| **`PCNTL_EUSERS`** ([int](language.types.integer.md)) | Muitos usuários |

**Constantes FORK\_\***

**`FORK_NOSIGCHLD`** ([int](language.types.integer.md))

**`FORK_WAITPID`** ([int](language.types.integer.md))

**Constantes RF\***

**`RFCFDG`** ([int](language.types.integer.md))

**`RFFDG`** ([int](language.types.integer.md))

**`RFLINUXTHPN`** ([int](language.types.integer.md))

**`RFNOWAIT`** ([int](language.types.integer.md))

**`RFPROC`** ([int](language.types.integer.md))

**`RFTHREAD`** ([int](language.types.integer.md))

**`RFTSIGZMB`** ([int](language.types.integer.md))

**Primeiro arugmento para `waitid` (`idtype`)**

**`P_ALL`** ([int](language.types.integer.md))
:   Seleciona qualquer filho.

**`P_PID`** ([int](language.types.integer.md))
:   Seleciona por ID de processo.

**`P_PGID`** ([int](language.types.integer.md))
:   Seleciona por ID de grupo de processo.

**`P_PIDFD`** ([int](language.types.integer.md))
:   Seleciona por descritor de arquivo PID.
    Específico para Linux (desde o Linux 5.4).

**`P_UID`** ([int](language.types.integer.md))
:   Seleciona por ID de usuário efetivo.
    Específico para NetBSD e FreeBSD.

**`P_GID`** ([int](language.types.integer.md))
:   Seleciona por ID de grupo efetivo.
    Específico para NetBSD e FreeBSD.

**`P_SID`** ([int](language.types.integer.md))
:   Seleciona por ID de sessão.
    Específico para NetBSD e FreeBSD.

**`P_JAILID`** ([int](language.types.integer.md))
:   Seleciona por identificador de prisão.
    Específico para FreeBSD.

`↑` and `↓` to navigate •
`Enter` to select •
`Esc` to close • `/` to open

document.addEventListener("DOMContentLoaded", function() {
/\*{{{Search Modal\*/
const language = 'local';
initSearchModal();
initPHPSearch(language).then((searchCallback) => {
initSearchUI({language, searchCallback, limit: 30});
});
/\*}}}\*/
});
