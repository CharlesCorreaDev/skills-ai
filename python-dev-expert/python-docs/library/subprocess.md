"subprocess" --- Gerenciamento de subprocessos
**********************************************

**Código-fonte:** Lib/subprocess.py

======================================================================

The "subprocess" module allows you to spawn new processes, connect to
their input/output/error pipes, and obtain their return codes.  This
module intends to replace several older modules and functions:

   os.system
   os.spawn*

Information about how the "subprocess" module can be used to replace
these modules and functions can be found in the following sections.

Ver também: **PEP 324** -- PEP propondo o módulo subprocess

Disponibilidade: not Android, not iOS, not WASI.

Este módulo não tem suporte em plataformas móveis ou plataformas
WebAssembly.


Using the "subprocess" Module
=============================

A abordagem recomendada para invocar subprocessos é usar a função
"run()" para todos os casos de uso que ela pode manipular. Para casos
de uso mais avançados, a interface subjacente "Popen" pode ser usada
diretamente.

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)

   Executa o comando descrito por *args*. Aguarda a conclusão do
   comando e retorna uma instância de "CompletedProcess".

   Os argumentos mostrados acima são meramente os mais comuns,
   descritos abaixo em Argumentos usados frequentemente (daí o uso de
   notação somente-nomeado na assinatura abreviada). A assinatura da
   função completa é basicamente a mesma do construtor "Popen" - a
   maioria dos argumentos para esta função são passados para aquela
   interface. (*timeout*, *input*, *check* e *capture_output* não
   são.)

   Se *capture_output* for verdadeiro, *stdout* e *stderr* serão
   capturados. Quando usado, o objeto interno "Popen" é
   automaticamente criado com *stdout* and *stderr* definidos como
   "PIPE". Os argumentos *stdout * e *stderr* não podem ser fornecidos
   ao mesmo tempo que *capture_output*. Se você deseja capturar e
   combinar ambos os fluxos em um, defina *stdout* para "PIPE" e
   *stderr* para "STDOUT", ao invés de usar *capture_output*.

   Um *timeout* pode ser especificado em segundos, ele é passado
   internamente para "Popen.communicate()". Se o tempo limite expirar,
   o processo filho será eliminado e aguardado. A exceção
   "TimeoutExpired" será levantada novamente após o término do
   processo filho. A criação inicial do processo em si não pode ser
   interrompida em muitas APIs de plataforma, portanto, não há
   garantia de que você verá uma exceção de tempo limite até, pelo
   menos, o tempo que a criação do processo demorar.

   O argumento *input* é passado para "Popen.communicate()" e,
   portanto, para o stdin do subprocesso. Se usado, deve ser uma
   sequência de bytes ou uma string se *encoding* ou *errors* forem
   especificados ou *text* for verdadeiro. Quando usado, o objeto
   internal "Popen" é automaticamente criado com "PIPE", e o argumento
   *stdin* também não pode ser usado.

   Se *check* for verdadeiro, e o processo sair com um código de saída
   diferente de zero, uma exceção "CalledProcessError" será levantada.
   Os atributos dessa exceção contêm os argumentos, o código de saída
   e stdout e stderr se eles foram capturados.

   Se *encoding* ou *errors* forem especificados, ou *text* for
   verdadeiro, os objetos arquivo para stdin, stdout e stderr são
   abertos em modo de texto usando a *encoding* e *errors*
   especificados ou o "io.TextIOWrapper" padrão. O argumento
   *universal_newlines* é equivalente a *text* e é fornecido para
   compatibilidade com versões anteriores. Por padrão, os objetos
   arquivo são abertos no modo binário.

   Se *env* não for "None", deve ser um mapeamento que defina as
   variáveis de ambiente para o novo processo; elas são usadas em vez
   do comportamento padrão de herdar o ambiente do processo atual. É
   passado diretamente para "Popen". Este mapeamento pode ser str para
   str em qualquer plataforma ou bytes para bytes em plataformas POSIX
   como "os.environ" ou "os.environb".

   Exemplos:

      >>> subprocess.run(["ls", "-l"])  # não captura a saída
      CompletedProcess(args=['ls', '-l'], returncode=0)

      >>> subprocess.run("exit 1", shell=True, check=True)
      Traceback (most recent call last):
        ...
      subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

      >>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
      CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
      stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')

   Adicionado na versão 3.5.

   Alterado na versão 3.6: Adicionados os parâmetros *encoding* e
   *errors*.

   Alterado na versão 3.7: Adicionado o parâmetro *text*, como um
   apelido mais compreensível que *universal_newlines*. Adicionado o
   parâmetro *capture_output*.

   Alterado na versão 3.12: Ordem de pesquisa do shell do Windows
   alterada para "shell=True". O diretório atual e "%PATH%" são
   substituídos por "%COMSPEC%" e "%SystemRoot%\System32\cmd.exe".
   Como resultado, colocar um programa malicioso chamado "cmd.exe" em
   um diretório atual não funciona mais.

class subprocess.CompletedProcess

   O valor de retorno de "run()", representando um processo que foi
   concluído.

   args

      Os argumentos usados para iniciar o processo. Pode ser uma lista
      ou uma string.

   returncode

      Status de saída do processo filho. Normalmente, um status de
      saída 0 indica que foi executado com êxito.

      Um valor negativo "-N" indica que o filho foi terminado pelo
      sinal "N" (POSIX apenas).

   stdout

      Stdout capturado do processo filho. Uma sequência de bytes ou
      uma string se "run()" foi chamada com uma codificação, erros ou
      text=True. "None" se stdout não foi capturado.

      Se você executou o processo com "stderr=subprocess.STDOUT",
      stdout e stderr serão combinados neste atributo, e "stderr" será
      "None".

   stderr

      Stderr capturado do processo filho. Uma sequência de bytes ou
      uma string se "run()" foi chamada com uma codificação, erros ou
      text=True. "None" se stderr não foi capturado.

   check_returncode()

      Se "returncode" é diferente de zero, levantar um
      "CalledProcessError".

   Adicionado na versão 3.5.

subprocess.DEVNULL

   Valor especial que pode ser usado como o argumento *stdin*,
   *stdout* ou *stderr* para "Popen" e indica que o arquivo especial
   "os.devnull" será usado.

   Adicionado na versão 3.3.

subprocess.PIPE

   Valor especial que pode ser usado como o argumento *stdin*,
   *stdout* ou *stderr* para "Popen" e indica que um encadeamento para
   o fluxo padrão deve ser aberto. Mais útil com
   "Popen.communicate()".

subprocess.STDOUT

   Valor especial que pode ser usado como o argumento *stderr* para
   "Popen" e indica que o erro padrão deve ir para o mesmo manipulador
   que a saída padrão.

exception subprocess.SubprocessError

   Classe base para todas as outras exceções deste módulo.

   Adicionado na versão 3.3.

exception subprocess.TimeoutExpired

   Subclasse de "SubprocessError", levantada quando um tempo limite
   expira enquanto espera por um processo filho.

   cmd

      Comando que foi usado para gerar o processo filho.

   timeout

      Tempo limite em segundos.

   output

      Saída do processo filho se ele foi capturado por "run()" ou
      "check_output()". Caso contrário, "None". Isto é sempre "bytes"
      quando qualquer saída foi capturada independente da configuração
      "text=True". Pode permanecer "None" em vez de "b''" quando
      nenhuma saída foi observada.

   stdout

      Apelido para a saída, para simetria com "stderr".

   stderr

      Saída de stderr do processo filho se ele foi capturado por
      "run()". Caso contrário, "None". Isto é sempre "bytes" quando a
      saída de stderr foi capturada independente da configuração
      "text=True". Pode permanecer "None" em vez de "b''" quando
      nenhuma saída de stderr foi observada.

   Adicionado na versão 3.3.

   Alterado na versão 3.5: Adicionados os atributos *stdout* e
   *stderr*

exception subprocess.CalledProcessError

   Subclasse de "SubprocessError", levantada quando um processo
   executado por "check_call()", "check_output()" ou "run()" (com
   "check=True") retorna um status de saída diferente de zero.

   returncode

      Exit status of the child process, an integer.  If the process
      exited due to a signal, this will be the negative signal number.

   cmd

      Comando que foi usado para gerar o processo filho.

   output

      Saída do processo filho se ele foi capturado por "run()" ou
      "check_output()". Caso contrário, "None".

   stdout

      Apelido para a saída, para simetria com "stderr".

   stderr

      Saída stderr do processo filho se ele foi capturado por "run()".
      Caso contrário, "None".

   Alterado na versão 3.5: Adicionados os atributos *stdout* e
   *stderr*


Argumentos usados frequentemente
--------------------------------

Para suportar uma ampla variedade de casos de uso, o construtor
"Popen" (e as funções de conveniência) aceita muitos argumentos
opcionais. Para a maioria dos casos de uso típicos, muitos desses
argumentos podem ser seguramente deixados em seus valores padrão. Os
argumentos mais comumente necessários são:

   *args* é necessário para todas as chamadas e deve ser uma string ou
   uma sequência de argumentos do programa. Fornecer uma sequência de
   argumentos geralmente é preferível, pois permite que o módulo cuide
   de qualquer escape e aspas em argumentos que forem necessários (por
   exemplo, para permitir espaços em nomes de arquivo). Se for passada
   uma única string, *shell* deve ser "True" (veja abaixo) ou então a
   string deve apenas nomear o programa a ser executado sem
   especificar nenhum argumento.

   *stdin*, *stdout* e *stderr* especificam a entrada padrão, a saída
   padrão e a saída de erro do programa executado, respectivamente. Os
   valores válidos são "None", "PIPE", "DEVNULL", um descritor de
   arquivo existente (um número inteiro positivo) e um *objeto
   arquivo* existente com um descritor de arquivo válido. Com as
   configurações padrão de "None", nenhum redirecionamento ocorrerá.
   "PIPE" indica que um novo canal para o filho deve ser criado.
   "DEVNULL" indica que o arquivo especial "os.devnull" será usado.
   Além disso, *stderr* pode ser "STDOUT", o que indica que os dados
   de stderr do processo filho devem ser capturados no mesmo
   identificador de arquivo que para *stdout*.

   Se *encoding* ou *errors* forem especificados, ou *text* (também
   conhecido como *universal_newlines*) for verdadeiro, os objetos
   arquivo *stdin*, *stdout* e *stderr* serão abertos em modo de texto
   usando a *encoding* e *errors* especificados na chamada ou os
   valores padrão para "io.TextIOWrapper".

   Para *stdin*, os caracteres de fim de linha "'\n'" na entrada serão
   convertidos para o separador de linha padrão "os.linesep". Para
   *stdout* e *stderr*, todas as terminações de linha na saída serão
   convertidas para "'\n'". Para obter mais informações, consulte a
   documentação da classe "io.TextIOWrapper" quando o argumento
   *newline* para seu construtor é "None".

   Se o modo de texto não for usado, *stdin*, *stdout* e *stderr*
   serão abertos como fluxos binários. Nenhuma codificação ou
   conversão de final de linha é executada.

   Alterado na versão 3.6: Adicionados os parâmetros *encoding* e
   *errors*.

   Alterado na versão 3.7: Adicionado o parâmetro *text* como um
   apelido para *universal_newlines*.

   Nota:

     O atributo newlines dos objetos arquivo "Popen.stdin",
     "Popen.stdout" e "Popen.stderr" não são atualizados pelo método
     "Popen.communicate()".

   Se *shell* for "True", o comando especificado será executado
   através do shell. Isso pode ser útil se você estiver usando Python
   principalmente para o fluxo de controle aprimorado que ele oferece
   sobre a maioria dos shells do sistema e ainda deseja acesso
   conveniente a outros recursos do shell, como canais de shell,
   caracteres curinga de nome de arquivo, expansão de variável de
   ambiente e expansão de "~" para o diretório inicial de um usuário.
   No entanto, observe que o próprio Python oferece implementações de
   muitos recursos semelhantes a shell (em particular, "glob",
   "fnmatch", "os.walk()", "os.path.expandvars()",
   "os.path.expanduser()" e "shutil").

   Alterado na versão 3.3: Quando *universal_newlines* é "True", a
   classe usa a codificação "locale.getpreferredencoding(False)" em
   vez de "locale.getpreferredencoding()".  Veja a classe
   "io.TextIOWrapper" para mais informações sobre esta alteração.

   Nota:

     Leia a seção Security Considerations antes de usar "shell=True".

Essas opções, junto com todas as outras opções, são descritas em mais
detalhes na documentação do construtor "Popen".


Construtor Popen
----------------

A criação e gerenciamento do processo subjacente neste módulo é
manipulado pela classe "Popen". Ela oferece muita flexibilidade para
que os desenvolvedores sejam capazes de lidar com os casos menos
comuns não cobertos pelas funções de conveniência.

class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, group=None, extra_groups=None, user=None, umask=-1, encoding=None, errors=None, text=None, pipesize=-1, process_group=None)

   Executa um programa filho em um novo processo. No POSIX, a classe
   usa o comportamento de "os.execvpe()" para executar o programa
   filho. No Windows, a classe usa a função Windows "CreateProcess()".
   Os argumentos para "Popen" são os seguintes.

   *args* deve ser uma sequência de argumentos do programa ou então
   uma única string ou *objeto caminho ou similar*. Por padrão, o
   programa a ser executado é o primeiro item em *args* se *args* for
   uma sequência. Se *args* for uma string, a interpretação depende da
   plataforma e é descrita abaixo. Consulte os argumentos *shell* e
   *executable* para obter diferenças adicionais em relação ao
   comportamento padrão. Salvo indicação em contrário, é recomendado
   passar *args* como uma sequência.

   Aviso:

     Para confiabilidade máxima, use um caminho totalmente qualificado
     para o executável. Para procurar um nome não qualificado no
     "PATH", use "shutil.which()". Em todas as plataformas, passar
     "sys.executable" é a maneira recomendada de relançar o
     interpretador Python atual, e usar o formato de linha de comando
     "-m" para iniciar um módulo instalado.Resolver o caminho do
     executável (ou o primeiro item de *args*) depende da plataforma.
     Para POSIX, veja "os.execvpe()", e note que ao resolver ou
     procurar o caminho do executável, *cwd* substitui o diretório de
     trabalho atual e *env* pode substituir a variável de ambiente
     "PATH". Para Windows, veja a documentação dos parâmetros
     "lpApplicationName" e "lpCommandLine" do WinAPI "CreateProcess",
     e note que ao resolver ou procurar o caminho do executável com
     "shell=False", *cwd* não substitui o diretório de trabalho atual
     e *env* não pode substituir a variável de ambiente "PATH". Usar
     um caminho completo evita todas essas variações.

   Um exemplo de passagem de alguns argumentos para um programa
   externo como uma sequência é:

      Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])

   No POSIX, se *args* for uma string, a string é interpretada como o
   nome ou caminho do programa a ser executado. No entanto, isso só
   pode ser feito se não forem passados argumentos para o programa.

   Nota:

     Pode não ser óbvio como quebrar um comando shell em uma sequência
     de argumentos, especialmente em casos complexos. "shlex.split()"
     pode ilustrar como determinar a tokenização correta para *args*:

        >>> import shlex, subprocess
        >>> command_line = input()
        /bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
        >>> args = shlex.split(command_line)
        >>> print(args)
        ['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
        >>> p = subprocess.Popen(args) # Successo!

     Observe em particular que as opções (como *-input*) e argumentos
     (como *eggs.txt*) que são separados por espaços em branco no
     shell vão em elementos de lista separados, enquanto os argumentos
     que precisam de aspas ou escape de contrabarra quando usados no
     shell (como nomes de arquivos contendo espaços ou o comando
     *echo* mostrado acima) são um único elemento de lista.

   No Windows, se *args* for uma sequência, será convertido em uma
   string da maneira descrita em Converter uma sequência de argumentos
   em uma string no Windows. Isso ocorre porque o "CreateProcess()"
   subjacente opera em strings.

   Alterado na versão 3.6: O parâmetro *args* aceita um *objeto
   caminho ou similar* se *shell* é "False" e uma sequência contendo
   objetos caminho ou similares no POSIX.

   Alterado na versão 3.8: O parâmetro *args* aceita um *objeto
   caminho ou similar* se *shell* for "False" e uma sequência contendo
   bytes e objetos caminho ou similares no Windows.

   O argumento *shell* (que por padrão é "False") especifica se deve
   usar o *shell* como o programa a ser executado. Se *shell* for
   "True", é recomendado passar *args* como uma string em vez de uma
   sequência.

   Em POSIX com "shell=True", o *shell* padrão é "/bin/sh". Se *args*
   for uma string, a *string* especifica o comando a ser executado
   através do *shell*. Isso significa que a *string* deve ser
   formatada exatamente como seria ao ser digitada no prompt do
   *shell*. Isso inclui, por exemplo, citar ou escapar com contrabarra
   nomes de arquivos que contenham espaços. Se *args* for uma
   sequência, o primeiro item especifica a *string* do comando, e
   quaisquer itens adicionais serão tratados como argumentos
   adicionais para o próprio *shell*. Ou seja, "Popen" faz o
   equivalente a:

      Popen(['/bin/sh', '-c', args[0], args[1], ...])

   No Windows com "shell=True", a variável de ambiente "COMSPEC"
   especifica o shell padrão. A única vez que você precisa especificar
   "shell=True" no Windows é quando o comando que você deseja executar
   é construído no shell (por exemplo, **dir** ou **copy**). Você não
   precisa de "shell=True" para executar um arquivo em lote ou
   executável baseado em console.

   Nota:

     Leia a seção Security Considerations antes de usar "shell=True".

   *bufsize* será fornecido como o argumento correspondente à função
   "open()" ao criar os objetos arquivo de encadeamento
   stdin/stdout/stderr:

   * "0" significa sem buffer (leitura e gravação são uma chamada de
     sistema e podem retornar curto)

   * "1" significa buffer de linha (utilizável somente se "text=True"
     ou "universal_newlines=True")

   * qualquer outro valor positivo significa usar um buffer de
     aproximadamente esse tamanho

   * bufsize negativo (o padrão) significa que o padrão do sistema
     io.DEFAULT_BUFFER_SIZE será usado.

   Alterado na versão 3.3.1: *bufsize* agora assume o padrão -1 para
   habilitar o buffer por padrão para corresponder ao comportamento
   que a maioria dos códigos espera. Em versões anteriores ao Python
   3.2.4 e 3.3.1, ele assumia incorretamente o padrão "0", que não
   tinha buffer e permitia leituras curtas. Isso não foi intencional e
   não correspondeu ao comportamento do Python 2, como a maioria dos
   códigos esperava.

   O argumento *executable* especifica um programa de substituição
   para executar. Ele é muito raramente necessário. Quando
   "shell=False", *executable* substitui o programa a ser executado
   especificado por *args*. No entanto, o *args* original ainda é
   passado para o programa. A maioria dos programas trata o programa
   especificado por *args* como o nome do comando, que pode então ser
   diferente do programa realmente executado. No POSIX, o nome *args*
   se torna o nome de exibição para o executável em utilitários como
   **ps**. Se "shell=True", no POSIX o argumento *executable*
   especifica um shell de substituição para o padrão "/bin/sh".

   Alterado na versão 3.6: O parâmetro *executable* aceita um *objeto
   caminho ou similar* no POSIX.

   Alterado na versão 3.8: O parâmetro *executable* aceita um *objeto
   caminho ou similar* bytes no Windows.

   Alterado na versão 3.12: Ordem de pesquisa do shell do Windows
   alterada para "shell=True". O diretório atual e "%PATH%" são
   substituídos por "%COMSPEC%" e "%SystemRoot%\System32\cmd.exe".
   Como resultado, colocar um programa malicioso chamado "cmd.exe" em
   um diretório atual não funciona mais.

   *stdin*, *stdout* e *stderr* especificam a entrada padrão, a saída
   padrão e a saída de erro do programa executado, respectivamente. Os
   valores válidos são "None", "PIPE", "DEVNULL", um descritor de
   arquivo existente (um número inteiro positivo) e um *objeto
   arquivo* existente com um descritor de arquivo válido. Com as
   configurações padrão de "None", nenhum redirecionamento ocorrerá.
   "PIPE" indica que um novo canal para o filho deve ser criado.
   "DEVNULL" indica que o arquivo especial "os.devnull" será usado.
   Além disso, *stderr* pode ser "STDOUT", o que indica que os dados
   de stderr da aplicação devem ser capturados no mesmo identificador
   de arquivo que para *stdout*.

   Se *preexec_fn* for definido como um objeto chamável, esse objeto
   será chamado no processo filho pouco antes de o filho ser
   executado. (Somente POSIX)

   Aviso:

     O parâmetro *preexec_fn* NÃO É SEGURO para uso na presença de
     threads em sua aplicação. O processo filho pode travar antes de
     exec ser chamado.

   Nota:

     Se você precisar modificar o ambiente para o filho, use o
     parâmetro *env* em vez de fazer isso em um *preexec_fn*. Os
     parâmetros *start_new_session* e *process_group* devem tomar o
     lugar do código usando *preexec_fn* para chamar "os.setsid()" ou
     "os.setpgid()" no filho.

   Alterado na versão 3.8: O parâmetro *preexec_fn* não é mais
   suportado em subinterpretadores. O uso do parâmetro em um
   subinterpretador levanta "RuntimeError". A nova restrição pode
   afetar aplicações que são implantadas em mod_wsgi, uWSGI e outros
   ambientes incorporados.

   If *close_fds* is true, all file descriptors except "0", "1" and
   "2" will be closed before the child process is executed.  Otherwise
   when *close_fds* is false, file descriptors obey their inheritable
   flag as described in Herança de descritores de arquivos.

   On Windows, if *close_fds* is true then no handles will be
   inherited by the child process unless explicitly passed in the
   "handle_list" element of "STARTUPINFO.lpAttributeList", or by
   standard handle redirection.

   Alterado na versão 3.2: The default for *close_fds* was changed
   from "False" to what is described above.

   Alterado na versão 3.7: On Windows the default for *close_fds* was
   changed from "False" to "True" when redirecting the standard
   handles. It's now possible to set *close_fds* to "True" when
   redirecting the standard handles.

   *pass_fds* is an optional sequence of file descriptors to keep open
   between the parent and child.  Providing any *pass_fds* forces
   *close_fds* to be "True".  (POSIX only)

   Alterado na versão 3.2: O parâmetro *pass_fds* foi adicionado.

   If *cwd* is not "None", the function changes the working directory
   to *cwd* before executing the child.  *cwd* can be a string, bytes
   or *path-like* object.  On POSIX, the function looks for
   *executable* (or for the first item in *args*) relative to *cwd* if
   the executable path is a relative path.

   Alterado na versão 3.6: *cwd* parameter accepts a *path-like
   object* on POSIX.

   Alterado na versão 3.7: *cwd* parameter accepts a *path-like
   object* on Windows.

   Alterado na versão 3.8: *cwd* parameter accepts a bytes object on
   Windows.

   If *restore_signals* is true (the default) all signals that Python
   has set to SIG_IGN are restored to SIG_DFL in the child process
   before the exec. Currently this includes the SIGPIPE, SIGXFZ and
   SIGXFSZ signals. (POSIX only)

   Alterado na versão 3.2: *restore_signals* foi adicionado.

   If *start_new_session* is true the "setsid()" system call will be
   made in the child process prior to the execution of the subprocess.

   Disponibilidade: POSIX

   Alterado na versão 3.2: *start_new_session* foi adicionado.

   If *process_group* is a non-negative integer, the "setpgid(0,
   value)" system call will be made in the child process prior to the
   execution of the subprocess.

   Disponibilidade: POSIX

   Alterado na versão 3.11: *process_group* was added.

   If *group* is not "None", the setregid() system call will be made
   in the child process prior to the execution of the subprocess. If
   the provided value is a string, it will be looked up via
   "grp.getgrnam()" and the value in "gr_gid" will be used. If the
   value is an integer, it will be passed verbatim. (POSIX only)

   Disponibilidade: POSIX

   Adicionado na versão 3.9.

   If *extra_groups* is not "None", the setgroups() system call will
   be made in the child process prior to the execution of the
   subprocess. Strings provided in *extra_groups* will be looked up
   via "grp.getgrnam()" and the values in "gr_gid" will be used.
   Integer values will be passed verbatim. (POSIX only)

   Disponibilidade: POSIX

   Adicionado na versão 3.9.

   If *user* is not "None", the setreuid() system call will be made in
   the child process prior to the execution of the subprocess. If the
   provided value is a string, it will be looked up via
   "pwd.getpwnam()" and the value in "pw_uid" will be used. If the
   value is an integer, it will be passed verbatim. (POSIX only)

   Nota:

     Specifying *user* will not drop existing supplementary group
     memberships! The caller must also pass "extra_groups=()" to
     reduce the group membership of the child process for security
     purposes.

   Disponibilidade: POSIX

   Adicionado na versão 3.9.

   If *umask* is not negative, the umask() system call will be made in
   the child process prior to the execution of the subprocess.

   Disponibilidade: POSIX

   Adicionado na versão 3.9.

   If *env* is not "None", it must be a mapping that defines the
   environment variables for the new process; these are used instead
   of the default behavior of inheriting the current process'
   environment. This mapping can be str to str on any platform or
   bytes to bytes on POSIX platforms much like "os.environ" or
   "os.environb".

   Nota:

     If specified, *env* must provide any variables required for the
     program to execute.  On Windows, in order to run a side-by-side
     assembly the specified *env* **must** include a valid
     "%SystemRoot%".

   If *encoding* or *errors* are specified, or *text* is true, the
   file objects *stdin*, *stdout* and *stderr* are opened in text mode
   with the specified *encoding* and *errors*, as described above in
   Argumentos usados frequentemente. The *universal_newlines* argument
   is equivalent  to *text* and is provided for backwards
   compatibility. By default, file objects are opened in binary mode.

   Adicionado na versão 3.6: *encoding* e *errors* foram adicionados.

   Adicionado na versão 3.7: *text* foi adicionado como um atalho mais
   legível para *universal_newlines*.

   If given, *startupinfo* will be a "STARTUPINFO" object, which is
   passed to the underlying "CreateProcess" function.

   If given, *creationflags*, can be one or more of the following
   flags:

   * "CREATE_NEW_CONSOLE"

   * "CREATE_NEW_PROCESS_GROUP"

   * "ABOVE_NORMAL_PRIORITY_CLASS"

   * "BELOW_NORMAL_PRIORITY_CLASS"

   * "HIGH_PRIORITY_CLASS"

   * "IDLE_PRIORITY_CLASS"

   * "NORMAL_PRIORITY_CLASS"

   * "REALTIME_PRIORITY_CLASS"

   * "CREATE_NO_WINDOW"

   * "DETACHED_PROCESS"

   * "CREATE_DEFAULT_ERROR_MODE"

   * "CREATE_BREAKAWAY_FROM_JOB"

   *pipesize* can be used to change the size of the pipe when "PIPE"
   is used for *stdin*, *stdout* or *stderr*. The size of the pipe is
   only changed on platforms that support this (only Linux at this
   time of writing). Other platforms will ignore this parameter.

   Alterado na versão 3.10: Added the *pipesize* parameter.

   Popen objects are supported as context managers via the "with"
   statement: on exit, standard file descriptors are closed, and the
   process is waited for.

      with Popen(["ifconfig"], stdout=PIPE) as proc:
          log.write(proc.stdout.read())

   Popen and the other functions in this module that use it raise an
   auditing event "subprocess.Popen" with arguments "executable",
   "args", "cwd", and "env". The value for "args" may be a single
   string or a list of strings, depending on platform.

   Alterado na versão 3.2: Adicionado suporte a gerenciador de
   contexto.

   Alterado na versão 3.6: O destruidor Popen agora emite um aviso
   "ResourceWarning" se o processo filho ainda estiver em execução.

   Alterado na versão 3.8: Popen can use "os.posix_spawn()" in some
   cases for better performance. On Windows Subsystem for Linux and
   QEMU User Emulation, Popen constructor using "os.posix_spawn()" no
   longer raise an exception on errors like missing program, but the
   child process fails with a non-zero "returncode".


Exceções
--------

Exceções levantadas no processo filho, antes que o novo programa
comece a ser executado, serão levantadas novamente no pai.

The most common exception raised is "OSError".  This occurs, for
example, when trying to execute a non-existent file.  Applications
should prepare for "OSError" exceptions. Note that, when "shell=True",
"OSError" will be raised by the child only if the selected shell
itself was not found. To determine if the shell failed to find the
requested application, it is necessary to check the return code or
output from the subprocess.

A exceção "ValueError" será levantada se "Popen" for chamado com
argumentos inválidos.

"check_call()" e "check_output()" levantarão "CalledProcessError" se o
processo chamado retornar um código de retorno diferente de zero.

All of the functions and methods that accept a *timeout* parameter,
such as "run()" and "Popen.communicate()" will raise "TimeoutExpired"
if the timeout expires before the process exits.

Todas as exceções definidas neste módulo herdam de "SubprocessError".

Adicionado na versão 3.3: A classe base "SubprocessError" foi
adicionada.


Considerações de Segurança
==========================

Unlike some other popen functions, this library will not implicitly
choose to call a system shell.  This means that all characters,
including shell metacharacters, can safely be passed to child
processes. If the shell is invoked explicitly, via "shell=True", it is
the application's responsibility to ensure that all whitespace and
metacharacters are quoted appropriately to avoid shell injection
vulnerabilities. On some platforms, it is possible to use
"shlex.quote()" for this escaping.

On Windows, batch files ("*.bat" or "*.cmd") may be launched by the
operating system in a system shell regardless of the arguments passed
to this library. This could result in arguments being parsed according
to shell rules, but without any escaping added by Python. If you are
intentionally launching a batch file with arguments from untrusted
sources, consider passing "shell=True" to allow Python to escape
special characters. See gh-114539 for additional discussion.


Objetos Popen
=============

Instâncias da classe "Popen" têm os seguintes métodos:

Popen.poll()

   Check if child process has terminated.  Set and return "returncode"
   attribute. Otherwise, returns "None".

Popen.wait(timeout=None)

   Wait for child process to terminate.  Set and return "returncode"
   attribute.

   If the process does not terminate after *timeout* seconds, raise a
   "TimeoutExpired" exception.  It is safe to catch this exception and
   retry the wait.

   Nota:

     This will deadlock when using "stdout=PIPE" or "stderr=PIPE" and
     the child process generates enough output to a pipe such that it
     blocks waiting for the OS pipe buffer to accept more data. Use
     "Popen.communicate()" when using pipes to avoid that.

   Nota:

     When "timeout" is not "None" and the platform supports it, an
     efficient event-driven mechanism is used to wait for process
     termination:

     * Linux >= 5.3 uses "os.pidfd_open()" + "select.poll()"

     * macOS and other BSD variants use "select.kqueue()" +
       "KQ_FILTER_PROC" + "KQ_NOTE_EXIT"

     * Windows uses "WaitForSingleObject"

     If none of these mechanisms are available, the function falls
     back to a busy loop (non-blocking call and short sleeps).

   Nota:

     Use the "asyncio" module for an asynchronous wait: see
     "asyncio.create_subprocess_exec".

   Alterado na versão 3.3: *timeout* foi adicionado.

   Alterado na versão 3.15: if *timeout* is not "None", use efficient
   event-driven implementation on Linux >= 5.3 and macOS / BSD.

Popen.communicate(input=None, timeout=None)

   Interact with process: Send data to stdin.  Read data from stdout
   and stderr, until end-of-file is reached.  Wait for process to
   terminate and set the "returncode" attribute.  The optional *input*
   argument should be data to be sent to the child process, or "None",
   if no data should be sent to the child.  If streams were opened in
   text mode, *input* must be a string. Otherwise, it must be bytes.

   "communicate()" returns a tuple "(stdout_data, stderr_data)". The
   data will be strings if streams were opened in text mode;
   otherwise, bytes.

   Note that if you want to send data to the process's stdin, you need
   to create the Popen object with "stdin=PIPE".  Similarly, to get
   anything other than "None" in the result tuple, you need to give
   "stdout=PIPE" and/or "stderr=PIPE" too.

   If the process does not terminate after *timeout* seconds, a
   "TimeoutExpired" exception will be raised.  Catching this exception
   and retrying communication will not lose any output.  Supplying
   *input* to a subsequent post-timeout "communicate()" call is in
   undefined behavior and may become an error in the future.

   The child process is not killed if the timeout expires, so in order
   to cleanup properly a well-behaved application should kill the
   child process and finish communication:

      proc = subprocess.Popen(...)
      try:
          outs, errs = proc.communicate(timeout=15)
      except TimeoutExpired:
          proc.kill()
          outs, errs = proc.communicate()

   After a call to "communicate()" raises "TimeoutExpired", do not
   call "wait()". Use an additional "communicate()" call to finish
   handling pipes and populate the "returncode" attribute.

   Nota:

     The data read is buffered in memory, so do not use this method if
     the data size is large or unlimited.

   Alterado na versão 3.3: *timeout* foi adicionado.

Popen.send_signal(signal)

   Envia o sinal *signal* para o filho.

   Não faz nada se o processo for concluído.

   Nota:

     On Windows, SIGTERM is an alias for "terminate()". CTRL_C_EVENT
     and CTRL_BREAK_EVENT can be sent to processes started with a
     *creationflags* parameter which includes
     "CREATE_NEW_PROCESS_GROUP".

Popen.terminate()

   Stop the child. On POSIX OSs the method sends "SIGTERM" to the
   child. On Windows the Win32 API function "TerminateProcess()" is
   called to stop the child.

Popen.kill()

   Kills the child. On POSIX OSs the function sends SIGKILL to the
   child. On Windows "kill()" is an alias for "terminate()".

The following attributes are also set by the class for you to access.
Reassigning them to new values is unsupported:

Popen.args

   O argumento *args* conforme foi passado para "Popen" - uma
   sequência de argumentos do programa ou então uma única string.

   Adicionado na versão 3.3.

Popen.stdin

   If the *stdin* argument was "PIPE", this attribute is a writeable
   stream object as returned by "open()". If the *encoding* or
   *errors* arguments were specified or the *text* or
   *universal_newlines* argument was "True", the stream is a text
   stream, otherwise it is a byte stream. If the *stdin* argument was
   not "PIPE", this attribute is "None".

Popen.stdout

   If the *stdout* argument was "PIPE", this attribute is a readable
   stream object as returned by "open()". Reading from the stream
   provides output from the child process. If the *encoding* or
   *errors* arguments were specified or the *text* or
   *universal_newlines* argument was "True", the stream is a text
   stream, otherwise it is a byte stream. If the *stdout* argument was
   not "PIPE", this attribute is "None".

Popen.stderr

   If the *stderr* argument was "PIPE", this attribute is a readable
   stream object as returned by "open()". Reading from the stream
   provides error output from the child process. If the *encoding* or
   *errors* arguments were specified or the *text* or
   *universal_newlines* argument was "True", the stream is a text
   stream, otherwise it is a byte stream. If the *stderr* argument was
   not "PIPE", this attribute is "None".

Aviso:

  Use "communicate()" rather than ".stdin.write", ".stdout.read" or
  ".stderr.read" to avoid deadlocks due to any of the other OS pipe
  buffers filling up and blocking the child process.

Popen.pid

   O ID de processo do processo filho.

   Observe que se você definir o argumento *shell* como "True", este é
   o ID do processo do shell gerado.

Popen.returncode

   The child return code. Initially "None", "returncode" is set by a
   call to the "poll()", "wait()", or "communicate()" methods if they
   detect that the process has terminated.

   A "None" value indicates that the process hadn't yet terminated at
   the time of the last method call.

   Um valor negativo "-N" indica que o filho foi terminado pelo sinal
   "N" (POSIX apenas).

   When "shell=True", the return code reflects the exit status of the
   shell itself (e.g. "/bin/sh"), which may map signals to codes such
   as "128+N". See the documentation of the shell (for example, the
   Bash manual's Exit Status) for details.


Windows Popen Helpers
=====================

The "STARTUPINFO" class and following constants are only available on
Windows.

class subprocess.STARTUPINFO(*, dwFlags=0, hStdInput=None, hStdOutput=None, hStdError=None, wShowWindow=0, lpAttributeList=None)

   Partial support of the Windows STARTUPINFO structure is used for
   "Popen" creation.  The following attributes can be set by passing
   them as keyword-only arguments.

   Alterado na versão 3.7: Keyword-only argument support was added.

   dwFlags

      A bit field that determines whether certain "STARTUPINFO"
      attributes are used when the process creates a window.

         si = subprocess.STARTUPINFO()
         si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW

   hStdInput

      If "dwFlags" specifies "STARTF_USESTDHANDLES", this attribute is
      the standard input handle for the process. If
      "STARTF_USESTDHANDLES" is not specified, the default for
      standard input is the keyboard buffer.

   hStdOutput

      If "dwFlags" specifies "STARTF_USESTDHANDLES", this attribute is
      the standard output handle for the process. Otherwise, this
      attribute is ignored and the default for standard output is the
      console window's buffer.

   hStdError

      If "dwFlags" specifies "STARTF_USESTDHANDLES", this attribute is
      the standard error handle for the process. Otherwise, this
      attribute is ignored and the default for standard error is the
      console window's buffer.

   wShowWindow

      If "dwFlags" specifies "STARTF_USESHOWWINDOW", this attribute
      can be any of the values that can be specified in the "nCmdShow"
      parameter for the ShowWindow function, except for
      "SW_SHOWDEFAULT". Otherwise, this attribute is ignored.

      "SW_HIDE" is provided for this attribute. It is used when
      "Popen" is called with "shell=True".

   lpAttributeList

      A dictionary of additional attributes for process creation as
      given in "STARTUPINFOEX", see UpdateProcThreadAttribute.

      Atributos suportados:

      **handle_list**
         Sequence of handles that will be inherited. *close_fds* must
         be true if non-empty.

         The handles must be temporarily made inheritable by
         "os.set_handle_inheritable()" when passed to the "Popen"
         constructor, else "OSError" will be raised with Windows error
         "ERROR_INVALID_PARAMETER" (87).

         Aviso:

           In a multithreaded process, use caution to avoid leaking
           handles that are marked inheritable when combining this
           feature with concurrent calls to other process creation
           functions that inherit all handles such as "os.system()".
           This also applies to standard handle redirection, which
           temporarily creates inheritable handles.

      Adicionado na versão 3.7.


Constantes do Windows
---------------------

The "subprocess" module exposes the following constants.

subprocess.STD_INPUT_HANDLE

   The standard input device. Initially, this is the console input
   buffer, "CONIN$".

subprocess.STD_OUTPUT_HANDLE

   The standard output device. Initially, this is the active console
   screen buffer, "CONOUT$".

subprocess.STD_ERROR_HANDLE

   The standard error device. Initially, this is the active console
   screen buffer, "CONOUT$".

subprocess.SW_HIDE

   Oculta a janela. Outra janela será ativada.

subprocess.STARTF_USESTDHANDLES

   Specifies that the "STARTUPINFO.hStdInput",
   "STARTUPINFO.hStdOutput", and "STARTUPINFO.hStdError" attributes
   contain additional information.

subprocess.STARTF_USESHOWWINDOW

   Specifies that the "STARTUPINFO.wShowWindow" attribute contains
   additional information.

subprocess.STARTF_FORCEONFEEDBACK

   A "STARTUPINFO.dwFlags" parameter to specify that the *Working in
   Background* mouse cursor will be displayed while a process is
   launching. This is the default behavior for GUI processes.

   Adicionado na versão 3.13.

subprocess.STARTF_FORCEOFFFEEDBACK

   A "STARTUPINFO.dwFlags" parameter to specify that the mouse cursor
   will not be changed when launching a process.

   Adicionado na versão 3.13.

subprocess.CREATE_NEW_CONSOLE

   The new process has a new console, instead of inheriting its
   parent's console (the default).

subprocess.CREATE_NEW_PROCESS_GROUP

   A "Popen" "creationflags" parameter to specify that a new process
   group will be created. This flag is necessary for using "os.kill()"
   on the subprocess.

   This flag is ignored if "CREATE_NEW_CONSOLE" is specified.

subprocess.ABOVE_NORMAL_PRIORITY_CLASS

   A "Popen" "creationflags" parameter to specify that a new process
   will have an above average priority.

   Adicionado na versão 3.7.

subprocess.BELOW_NORMAL_PRIORITY_CLASS

   A "Popen" "creationflags" parameter to specify that a new process
   will have a below average priority.

   Adicionado na versão 3.7.

subprocess.HIGH_PRIORITY_CLASS

   A "Popen" "creationflags" parameter to specify that a new process
   will have a high priority.

   Adicionado na versão 3.7.

subprocess.IDLE_PRIORITY_CLASS

   A "Popen" "creationflags" parameter to specify that a new process
   will have an idle (lowest) priority.

   Adicionado na versão 3.7.

subprocess.NORMAL_PRIORITY_CLASS

   A "Popen" "creationflags" parameter to specify that a new process
   will have a normal priority. (default)

   Adicionado na versão 3.7.

subprocess.REALTIME_PRIORITY_CLASS

   A "Popen" "creationflags" parameter to specify that a new process
   will have realtime priority. You should almost never use
   REALTIME_PRIORITY_CLASS, because this interrupts system threads
   that manage mouse input, keyboard input, and background disk
   flushing. This class can be appropriate for applications that
   "talk" directly to hardware or that perform brief tasks that should
   have limited interruptions.

   Adicionado na versão 3.7.

subprocess.CREATE_NO_WINDOW

   A "Popen" "creationflags" parameter to specify that a new process
   will not create a window.

   Adicionado na versão 3.7.

subprocess.DETACHED_PROCESS

   A "Popen" "creationflags" parameter to specify that a new process
   will not inherit its parent's console. This value cannot be used
   with CREATE_NEW_CONSOLE.

   Adicionado na versão 3.7.

subprocess.CREATE_DEFAULT_ERROR_MODE

   A "Popen" "creationflags" parameter to specify that a new process
   does not inherit the error mode of the calling process. Instead,
   the new process gets the default error mode. This feature is
   particularly useful for multithreaded shell applications that run
   with hard errors disabled.

   Adicionado na versão 3.7.

subprocess.CREATE_BREAKAWAY_FROM_JOB

   A "Popen" "creationflags" parameter to specify that a new process
   is not associated with the job.

   Adicionado na versão 3.7.


API de alto nível mais antiga
=============================

Antes do Python 3.5, essas três funções constituíam a API de alto
nível para subprocesso. Agora você pode usar "run()" em muitos casos,
mas muitos códigos existentes chamam essas funções.

subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, **other_popen_kwargs)

   Run the command described by *args*.  Wait for command to complete,
   then return the "returncode" attribute.

   Code needing to capture stdout or stderr should use "run()"
   instead:

      run(...).returncode

   To suppress stdout or stderr, supply a value of "DEVNULL".

   The arguments shown above are merely some common ones. The full
   function signature is the same as that of the "Popen" constructor -
   this function passes all supplied arguments other than *timeout*
   directly through to that interface.

   Nota:

     Do not use "stdout=PIPE" or "stderr=PIPE" with this function.
     The child process will block if it generates enough output to a
     pipe to fill up the OS pipe buffer as the pipes are not being
     read from.

   Alterado na versão 3.3: *timeout* foi adicionado.

   Alterado na versão 3.12: Ordem de pesquisa do shell do Windows
   alterada para "shell=True". O diretório atual e "%PATH%" são
   substituídos por "%COMSPEC%" e "%SystemRoot%\System32\cmd.exe".
   Como resultado, colocar um programa malicioso chamado "cmd.exe" em
   um diretório atual não funciona mais.

subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, cwd=None, timeout=None, **other_popen_kwargs)

   Run command with arguments.  Wait for command to complete. If the
   return code was zero then return, otherwise raise
   "CalledProcessError". The "CalledProcessError" object will have the
   return code in the "returncode" attribute. If "check_call()" was
   unable to start the process it will propagate the exception that
   was raised.

   Code needing to capture stdout or stderr should use "run()"
   instead:

      run(..., check=True)

   To suppress stdout or stderr, supply a value of "DEVNULL".

   The arguments shown above are merely some common ones. The full
   function signature is the same as that of the "Popen" constructor -
   this function passes all supplied arguments other than *timeout*
   directly through to that interface.

   Nota:

     Do not use "stdout=PIPE" or "stderr=PIPE" with this function.
     The child process will block if it generates enough output to a
     pipe to fill up the OS pipe buffer as the pipes are not being
     read from.

   Alterado na versão 3.3: *timeout* foi adicionado.

   Alterado na versão 3.12: Ordem de pesquisa do shell do Windows
   alterada para "shell=True". O diretório atual e "%PATH%" são
   substituídos por "%COMSPEC%" e "%SystemRoot%\System32\cmd.exe".
   Como resultado, colocar um programa malicioso chamado "cmd.exe" em
   um diretório atual não funciona mais.

subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, cwd=None, encoding=None, errors=None, universal_newlines=None, timeout=None, text=None, **other_popen_kwargs)

   Executa o comando com argumentos e retorna sua saída.

   If the return code was non-zero it raises a "CalledProcessError".
   The "CalledProcessError" object will have the return code in the
   "returncode" attribute and any output in the "output" attribute.

   Isso equivale a:

      run(..., check=True, stdout=PIPE).stdout

   The arguments shown above are merely some common ones. The full
   function signature is largely the same as that of "run()" - most
   arguments are passed directly through to that interface. One API
   deviation from "run()" behavior exists: passing "input=None" will
   behave the same as "input=b''" (or "input=''", depending on other
   arguments) rather than using the parent's standard input file
   handle.

   By default, this function will return the data as encoded bytes.
   The actual encoding of the output data may depend on the command
   being invoked, so the decoding to text will often need to be
   handled at the application level.

   This behaviour may be overridden by setting *text*, *encoding*,
   *errors*, or *universal_newlines* to "True" as described in
   Argumentos usados frequentemente and "run()".

   To also capture standard error in the result, use
   "stderr=subprocess.STDOUT":

      >>> subprocess.check_output(
      ...     "ls non_existent_file; exit 0",
      ...     stderr=subprocess.STDOUT,
      ...     shell=True)
      'ls: non_existent_file: No such file or directory\n'

   Adicionado na versão 3.1.

   Alterado na versão 3.3: *timeout* foi adicionado.

   Alterado na versão 3.4: Support for the *input* keyword argument
   was added.

   Alterado na versão 3.6: *encoding* and *errors* were added.  See
   "run()" for details.

   Adicionado na versão 3.7: *text* foi adicionado como um atalho mais
   legível para *universal_newlines*.

   Alterado na versão 3.12: Ordem de pesquisa do shell do Windows
   alterada para "shell=True". O diretório atual e "%PATH%" são
   substituídos por "%COMSPEC%" e "%SystemRoot%\System32\cmd.exe".
   Como resultado, colocar um programa malicioso chamado "cmd.exe" em
   um diretório atual não funciona mais.


Replacing Older Functions with the "subprocess" Module
======================================================

In this section, "a becomes b" means that b can be used as a
replacement for a.

Nota:

  All "a" functions in this section fail (more or less) silently if
  the executed program cannot be found; the "b" replacements raise
  "OSError" instead.In addition, the replacements using
  "check_output()" will fail with a "CalledProcessError" if the
  requested operation produces a non-zero return code. The output is
  still available as the "output" attribute of the raised exception.

In the following examples, we assume that the relevant functions have
already been imported from the "subprocess" module.


Replacing **/bin/sh** shell command substitution
------------------------------------------------

   output=$(mycmd myarg)

torna-se:

   output = check_output(["mycmd", "myarg"])


Replacing shell pipeline
------------------------

   output=$(dmesg | grep hda)

torna-se:

   p1 = Popen(["dmesg"], stdout=PIPE)
   p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
   p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
   output = p2.communicate()[0]

The "p1.stdout.close()" call after starting the p2 is important in
order for p1 to receive a SIGPIPE if p2 exits before p1.

Alternatively, for trusted input, the shell's own pipeline support may
still be used directly:

   output=$(dmesg | grep hda)

torna-se:

   output = check_output("dmesg | grep hda", shell=True)


Substituindo "os.system()"
--------------------------

   sts = os.system("mycmd" + " myarg")
   # becomes
   retcode = call("mycmd" + " myarg", shell=True)

Notas:

* Calling the program through the shell is usually not required.

* The "call()" return value is encoded differently to that of
  "os.system()".

* The "os.system()" function ignores SIGINT and SIGQUIT signals while
  the command is running, but the caller must do this separately when
  using the "subprocess" module.

Um exemplo mais realista ficaria assim:

   try:
       retcode = call("mycmd" + " myarg", shell=True)
       if retcode < 0:
           print("Child was terminated by signal", -retcode, file=sys.stderr)
       else:
           print("Child returned", retcode, file=sys.stderr)
   except OSError as e:
       print("Execution failed:", e, file=sys.stderr)


Replacing the "os.spawn" family
-------------------------------

Exemplo P_NOWAIT:

   pid = os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg")
   ==>
   pid = Popen(["/bin/mycmd", "myarg"]).pid

Exemplo P_WAIT:

   retcode = os.spawnlp(os.P_WAIT, "/bin/mycmd", "mycmd", "myarg")
   ==>
   retcode = call(["/bin/mycmd", "myarg"])

Exemplo de vetor:

   os.spawnvp(os.P_NOWAIT, path, args)
   ==>
   Popen([path] + args[1:])

Exemplo de ambiente:

   os.spawnlpe(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg", env)
   ==>
   Popen(["/bin/mycmd", "myarg"], env={"PATH": "/usr/bin"})


Replacing "os.popen()"
----------------------

Return code handling translates as follows:

   pipe = os.popen(cmd, 'w')
   ...
   rc = pipe.close()
   if rc is not None and rc >> 8:
       print("There were some errors")
   ==>
   process = Popen(cmd, stdin=PIPE)
   ...
   process.stdin.close()
   if process.wait() != 0:
       print("There were some errors")


Legacy Shell Invocation Functions
=================================

This module also provides the following legacy functions from the 2.x
"commands" module. These operations implicitly invoke the system shell
and none of the guarantees described above regarding security and
exception handling consistency are valid for these functions.

subprocess.getstatusoutput(cmd, *, encoding=None, errors=None)

   Return "(exitcode, output)" of executing *cmd* in a shell.

   Execute the string *cmd* in a shell with "check_output()" and
   return a 2-tuple "(exitcode, output)". *encoding* and *errors* are
   used to decode output; see the notes on Argumentos usados
   frequentemente for more details.

   A trailing newline is stripped from the output. The exit code for
   the command can be interpreted as the return code of subprocess.
   Example:

      >>> subprocess.getstatusoutput('ls /bin/ls')
      (0, '/bin/ls')
      >>> subprocess.getstatusoutput('cat /bin/junk')
      (1, 'cat: /bin/junk: No such file or directory')
      >>> subprocess.getstatusoutput('/bin/junk')
      (127, 'sh: /bin/junk: not found')
      >>> subprocess.getstatusoutput('/bin/kill $$')
      (-15, '')

   Disponibilidade: Unix, Windows.

   Alterado na versão 3.3.4: Suporte ao Windows foi adicionado.The
   function now returns (exitcode, output) instead of (status, output)
   as it did in Python 3.3.3 and earlier.  exitcode has the same value
   as "returncode".

   Alterado na versão 3.11: Adicionados os parâmetros *encoding* e
   *errors*.

subprocess.getoutput(cmd, *, encoding=None, errors=None)

   Return output (stdout and stderr) of executing *cmd* in a shell.

   Like "getstatusoutput()", except the exit code is ignored and the
   return value is a string containing the command's output.  Example:

      >>> subprocess.getoutput('ls /bin/ls')
      '/bin/ls'

   Disponibilidade: Unix, Windows.

   Alterado na versão 3.3.4: Suporte para Windows adicionado.

   Alterado na versão 3.11: Adicionados os parâmetros *encoding* e
   *errors*.


Notas
=====


Timeout Behavior
----------------

When using the "timeout" parameter in functions like "run()",
"Popen.wait()", or "Popen.communicate()", users should be aware of the
following behaviors:

1. **Process Creation Delay**: The initial process creation itself
   cannot be interrupted on many platform APIs. This means that even
   when specifying a timeout, you are not guaranteed to see a timeout
   exception until at least after however long process creation takes.

2. **Extremely Small Timeout Values**: Setting very small timeout
   values (such as a few milliseconds) may result in almost immediate
   "TimeoutExpired" exceptions because process creation and system
   scheduling inherently require time.


Converter uma sequência de argumentos em uma string no Windows
--------------------------------------------------------------

On Windows, an *args* sequence is converted to a string that can be
parsed using the following rules (which correspond to the rules used
by the MS C runtime):

1. Arguments are delimited by white space, which is either a space or
   a tab.

2. A string surrounded by double quotation marks is interpreted as a
   single argument, regardless of white space contained within.  A
   quoted string can be embedded in an argument.

3. A double quotation mark preceded by a backslash is interpreted as a
   literal double quotation mark.

4. Backslashes are interpreted literally, unless they immediately
   precede a double quotation mark.

5. If backslashes immediately precede a double quotation mark, every
   pair of backslashes is interpreted as a literal backslash.  If the
   number of backslashes is odd, the last backslash escapes the next
   double quotation mark as described in rule 3.

Ver também:

  "shlex"
     Module which provides function to parse and escape command lines.


Disable use of "posix_spawn()"
------------------------------

On Linux, "subprocess" defaults to using the "vfork()" system call
internally when it is safe to do so rather than "fork()". This greatly
improves performance.

   subprocess._USE_POSIX_SPAWN = False  # See CPython issue gh-NNNNNN.

It is safe to set this to false on any Python version. It will have no
effect on older or newer versions where unsupported. Do not assume the
attribute is available to read. Despite the name, a true value does
not indicate the corresponding function will be used, only that it may
be.

Please file issues any time you have to use these private knobs with a
way to reproduce the issue you were seeing. Link to that issue from a
comment in your code.

Adicionado na versão 3.8: "_USE_POSIX_SPAWN"
