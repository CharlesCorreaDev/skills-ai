Protocolo de anexação de depuração remota
*****************************************

Este protocolo permite que ferramentas externas se conectem a um
processo CPython em execução e executem código Python remotamente.

Anexar a outro processo Python pode exigir permissões ou configurações
adicionais, dependendo da plataforma.


Disabling remote debugging
==========================

To disable remote debugging support, use any of the following:

* Set the "PYTHON_DISABLE_REMOTE_DEBUG" environment variable to "1"
  before starting the interpreter.

* Use the "-X disable-remote-debug" command-line option.

* Compile Python with the "--without-remote-debug" build flag.


Requisitos de permissão
***********************

Attaching to a running Python process for remote debugging requires
special configuration on most platforms. The specific requirements and
troubleshooting steps depend on your operating system:

-[ Linux ]-

In general, you can debug your own processes, but there are several
common configurations that may disable this. Some Linux distributions
enable **ptrace restrictions**, aka "Yama," as a form of system
hardening. Recent versions of the "setpriv" command (util-linux 2.41,
released June 2025) let you loosen ptrace restrictions on a per-
process basis:

   "setpriv --ptracer any python3"

(This is configured on the process *being debugged*.) You can also
turn off ptrace restrictions for all processes until reboot with:

   "echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope"

This can also be configured persistently, usually in "/etc/sysctl.d".

Nota:

  Disabling "ptrace_scope" reduces system hardening and should only be
  done in low-security environments.

It is also possible that the "ptrace" system call is disabled because
of a security filter. In particular, this was common with older
versions of some container software. Docker 19.03 or newer (released
2019) and containerd 1.6.7 or newer (released 2022) will automatically
allow usage of the "ptrace" system call inside containers, when
running on Linux kernel 4.8 or higher. If you cannot upgrade to these
versions, you can create your container with an option like "--
security-opt seccomp=unconfined" to disable the system call security
filter for that container. This weakens the container's isolation and
should only be done in low-security environments.

If you need to trace a process that you *do not* own, you will need
superuser access or equivalent. This also applies to processes that
have changed their security credentials, e.g., set-user-ID or set-
group-ID processes (though this is unusual for Python). Try running
the debugging command with "sudo -E".

Nota:

  The "CAP_SYS_PTRACE" capability is equivalent to superuser access,
  in that it allows debugging *any* process, not just your own. You
  may see advice on the internet suggesting using it to work around
  ptrace restrictions or system call filters. This may work in
  practice, as would "sudo", but this gives the debugging process much
  more access than it needs and should only be done in low-security
  environments.

Finally, note that a process can only have one tracer at a time. If
you have already attached to a Python process under "strace", "gdb",
etc., you won't be able to simultaneously use remote debugging.
(Superuser access cannot get around this restriction.)

-[ macOS ]-

By default, macOS disables the ability to debug other processes.

You can modify your Python binary to opt in to being debugged by
giving it an **ad-hoc code signature** with an **entitlement**
enabling it to be debugged. (An ad-hoc "signature" is just a
configuration without any actual cryptographic signature or a need for
a certificate or anything else such as an Apple developer program
membership.)

The following commands will create a file "get-task-allow.plist" with
the necessary entitlement and add it to the Python binary:

   echo '{"com.apple.security.get-task-allow": true}' | plutil -convert xml1 -o get-task-allow.plist -
   codesign --sign - --entitlements get-task-allow.plist path/to/bin/python3

where "path/to/bin/python3" is the path to your Python binary, which
you can find by e.g. running "which python3" or evaluating
"sys.base_executable" at the Python REPL. (These instructions are for
a non-framework build of Python. Framework builds may need to be
configured differently.)

You should then be able to debug your own Python processes started
with that binary.

Alternatively, much as with Linux, processes with superuser privileges
e.g. "sudo" are not subject to this check and can debug any user's
process on the system (though there are additional checks on specific
binaries, such as OS-provided commands, due to System Integrity
Protection).

-[ Windows ]-

Para se conectar a outro processo, geralmente é necessário executar a
ferramenta de depuração com privilégios administrativos. Inicie o
prompt de comando ou o terminal como administrador.

Alguns processos ainda podem estar inacessíveis mesmo com direitos de
administrador, a menos que você tenha o privilégio "SeDebugPrivilege"
ativado.

Para resolver problemas de acesso a arquivos ou pastas, ajuste as
permissões de segurança:

   1. Clique com o botão direito do mouse no arquivo ou pasta e
      selecione **Propriedades**.

   2. Acesse a aba **Segurança** para visualizar usuários e grupos com
      acesso.

   3. Clique em **Editar** para modificar as permissões.

   4. Selecione sua conta de usuário.

   5. Em **Permissões**, marque **Leitura** ou **Controle total**
      conforme necessário.

   6. Clique em **Aplicar** e depois em **OK** para confirmar.

Nota:

  Certifique-se de ter atendido a todos os Requisitos de permissão
  antes de prosseguir.

Esta seção descreve o protocolo de baixo nível que permite que
ferramentas externas injetem e executem um script Python dentro de um
processo CPython em execução.

Este mecanismo forma a base da função "sys.remote_exec()", que instrui
um processo Python remoto a executar um arquivo ".py". No entanto,
esta seção não documenta o uso dessa função. Em vez disso, fornece uma
explicação detalhada do protocolo subjacente, que recebe como entrada
o "pid" de um processo Python de destino e o caminho para um arquivo-
fonte Python a ser executado. Essas informações permitem a
reimplementação independente do protocolo, independentemente da
linguagem de programação.

Aviso:

  A execução do script injetado depende de o interpretador atingir um
  ponto de avaliação seguro. Como resultado, a execução pode ser
  atrasada dependendo do estado de execução do processo de destino.

Uma vez injetado, o script é executado pelo interpretador dentro do
processo de destino na próxima vez que um ponto de avaliação seguro
for atingido. Essa abordagem permite recursos de execução remota sem
modificar o comportamento ou a estrutura da aplicação Python em
execução.

As seções subsequentes fornecem uma descrição passo a passo do
protocolo, incluindo técnicas para localizar estruturas do
interpretador na memória, acessar campos internos com segurança e
disparar a execução de código. Variações específicas da plataforma são
indicadas quando aplicável, e exemplos de implementação são incluídos
para esclarecer cada operação.


Localizando a estrutura de PyRuntime
************************************

O CPython coloca a estrutura "PyRuntime" em uma seção binária dedicada
para ajudar ferramentas externas a encontrá-la em tempo de execução. O
nome e o formato desta seção variam de acordo com a plataforma. Por
exemplo, ".PyRuntime" é usado em sistemas ELF, e "__DATA,__PyRuntime"
é usado no macOS. As ferramentas podem encontrar o deslocamento desta
estrutura examinando o binário no disco.

A estrutura "PyRuntime" contém o estado global do interpretador do
CPython e fornece acesso a outros dados internos, incluindo a lista de
interpretadores, estados de thread e campos de suporte do depurador.

Para trabalhar com um processo Python remoto, um depurador precisa
primeiro encontrar o endereço de memória da estrutura "PyRuntime" no
processo de destino. Este endereço não pode ser codificado ou
calculado a partir de um nome de símbolo, pois depende de onde o
sistema operacional carregou o binário.

O método para encontrar "PyRuntime" depende da plataforma, mas os
passos são os mesmos em geral:

1. Encontrar o endereço base onde o binário Python ou a biblioteca
   compartilhada foi carregada no processo de destino.

2. Usar o binário no disco para localizar o deslocamento da seção
   ".PyRuntime".

3. Adicionar o deslocamento da seção ao endereço base para calcular o
   endereço na memória.

As seções abaixo explicam como fazer isso em cada plataforma suportada
e incluem código de exemplo.

-[ Linux (ELF) ]-

Para encontrar a estrutura de "PyRuntime" no Linux:

1. Lê o mapa de memória do processo (por exemplo, "/proc/<pid>/maps")
   para encontrar o endereço onde o executável Python ou "libpython"
   foi carregado.

2. Analise os cabeçalhos da seção ELF no binário para obter o
   deslocamento da seção ".PyRuntime".

3. Adicione esse deslocamento ao endereço base da etapa 1 para obter o
   endereço de memória de "PyRuntime".

A seguir está um exemplo de implementação:

   def find_py_runtime_linux(pid: int) -> int:
       # Etapa 1: tenta encontrar o executável Python na memória
       binary_path, base_address = find_mapped_binary(
           pid, name_contains="python"
       )

       # Etapa 2: recorre à biblioteca compartilhada se não encontrar o executável
       if binary_path is None:
           binary_path, base_address = find_mapped_binary(
               pid, name_contains="libpython"
           )

       # Etapa 3: analisa os cabeçalhos ELF para obter o deslocamento da seção .PyRuntime
       section_offset = parse_elf_section_offset(
           binary_path, ".PyRuntime"
       )

       # Etapa 4: calcula o endereço de PyRuntime na memória
       return base_address + section_offset

Em sistemas Linux, existem duas abordagens principais para ler memória
de outro processo. A primeira é através do sistema de arquivos
"/proc", especificamente lendo de "/proc/[pid]/mem", que fornece
acesso direto à memória do processo. Isso requer permissões
apropriadas – seja o mesmo usuário do processo alvo ou ter acesso
root. A segunda abordagem é usar a chamada de sistema
"process_vm_readv()", que fornece uma maneira mais eficiente de copiar
memória entre processos. Embora a operação "PTRACE_PEEKTEXT" do ptrace
também possa ser usada para ler memória, ela é significativamente mais
lenta, pois lê apenas uma palavra por vez e requer múltiplas trocas de
contexto entre os processos rastreador e rastreado.

Para analisar seções ELF, o processo envolve a leitura e a
interpretação das estruturas do formato de arquivo ELF do arquivo
binário em disco. O cabeçalho ELF contém um ponteiro para a tabela de
cabeçalhos de seção. Cada cabeçalho de seção contém metadados sobre
uma seção, incluindo seu nome (armazenado em uma tabela de strings
separada), deslocamento e tamanho. Para encontrar uma seção
específica, como .PyRuntime, você precisa percorrer esses cabeçalhos e
encontrar o nome da seção. O cabeçalho de seção então fornece o
deslocamento onde essa seção existe no arquivo, que pode ser usado
para calcular seu endereço de tempo de execução quando o binário é
carregado na memória.

Você pode ler mais sobre o formato de arquivo ELF na especificação do
ELF.

-[ macOS (Mach-O) ]-

Para encontrar a estrutura de "PyRuntime" no macOS:

1. Chame "task_for_pid()" para obter a porta da tarefa "mach_port_t"
   para o processo de destino. Este identificador é necessário para
   ler memória usando APIs como "mach_vm_read_overwrite" e
   "mach_vm_region".

2. Examine as regiões da memória para encontrar aquela que contém o
   executável Python ou "libpython".

3. Carregue o arquivo binário do disco e analise os cabeçalhos do
   Mach-O para encontrar a seção chamada "PyRuntime" no segmento
   "__DATA". No macOS, os nomes dos símbolos são prefixados
   automaticamente com um sublinhado, de modo que o símbolo
   "PyRuntime" aparece como "_PyRuntime" na tabela de símbolos, mas o
   nome da seção não é afetado.

A seguir está um exemplo de implementação:

   def find_py_runtime_macos(pid: int) -> int:
       # Etapa 1: obtém acesso à memória do processo
       handle = get_memory_access_handle(pid)

       # Etapa 2: tenta encontrar o executável Python na memória
       binary_path, base_address = find_mapped_binary(
           handle, name_contains="python"
       )

       # Etapa 2: recorre à biblioteca compartilhada se não encontrar o executável
       if binary_path is None:
           binary_path, base_address = find_mapped_binary(
               handle, name_contains="libpython"
           )

       # Etapa 4: analisa os cabeçalhos Mach-O para obter o deslocamento da seção __DATA,__PyRuntime
       section_offset = parse_macho_section_offset(
           binary_path, "__DATA", "__PyRuntime"
       )

       # Etapa 5: calcula o endereço de PyRuntime na memória
       return base_address + section_offset

No macOS, acessar a memória de outro processo requer o uso de APIs e
formatos de arquivo específicos do Mach-O. O primeiro passo é obter um
identificador "task_port" via "task_for_pid()", que fornece acesso ao
espaço de memória do processo de destino. Esse identificador permite
operações de memória por meio de APIs como "mach_vm_read_overwrite()".

A memória do processo pode ser examinada usando "mach_vm_region()"
para varrer o espaço da memória virtual, enquanto
"proc_regionfilename()" ajuda a identificar quais arquivos binários
são carregados em cada região da memória. Quando o binário ou
biblioteca Python é encontrado, seus cabeçalhos Mach-O precisam ser
analisados para localizar a estrutura "PyRuntime".

O formato Mach-O organiza código e dados em segmentos e seções. A
estrutura "PyRuntime" reside em uma seção chamada "__PyRuntime" dentro
do segmento "__DATA". O cálculo do endereço de tempo de execução
envolve encontrar o segmento "__TEXT", que serve como endereço base do
binário, e então localizar o segmento "__DATA" que contém nossa seção
de destino. O endereço final é calculado combinando o endereço base
com os deslocamentos de seção apropriados dos cabeçalhos do Mach-O.

Observe que acessar a memória de outro processo no macOS normalmente
requer privilégios elevados — acesso root ou direitos de segurança
especiais concedidos ao processo de depuração.

-[ Windows (PE) ]-

Para encontrar a estrutura de "PyRuntime" no Windows:

1. Use a API ToolHelp para enumerar todos os módulos carregados no
   processo de destino. Isso é feito usando funções como
   CreateToolhelp32Snapshot, Module32First e Module32Next.

2. Identifique o módulo correspondente a "python.exe" ou
   "python*XY*.dll", onde "X" e "Y" são os números de versão principal
   e secundária do Python, e registre seu endereço base.

3. Localize a seção "PyRuntim". Devido ao limite de 8 caracteres do
   formato PE para nomes de seção (definido como
   "IMAGE_SIZEOF_SHORT_NAME"), o nome original "PyRuntime" está
   truncado. Esta seção contém a estrutura "PyRuntime".

4. Recupere o endereço virtual relativo (RVA) da seção e adicione-o ao
   endereço base do módulo.

A seguir está um exemplo de implementação:

   def find_py_runtime_windows(pid: int) -> int:
       # Etapa 1: tenta encontrar o executável Python na memória
       binary_path, base_address = find_loaded_module(
           pid, name_contains="python"
       )

       # Etapa 2: recorre à pythonXY.dll compartilhada se não encontrar
       # o executável
       if binary_path is None:
           binary_path, base_address = find_loaded_module(
               pid, name_contains="python3"
           )

       # Etapa 3: analisa os cabeçalhos da seção PE para obter o RVA
       # da seção .PyRuntime. O nome da seção aparece como "PyRuntim"
       # devido ao limite de 8 caracteres definido pelo formato PE
       # (IMAGE_SIZEOF_SHORT_NAME).
       section_rva = parse_pe_section_offset(binary_path, "PyRuntim")

       # Etapa 4: calcula o endereço de PyRuntime na memória
       return base_address + section_rva

No Windows, acessar a memória de outro processo requer o uso de
funções da API do Windows, como "CreateToolhelp32Snapshot()" e
"Module32First()/Module32Next()", para enumerar os módulos carregados.
A função "OpenProcess()" fornece um identificador para acessar o
espaço de memória do processo de destino, permitindo operações de
memória por meio de "ReadProcessMemory()".

A memória do processo pode ser examinada enumerando os módulos
carregados para encontrar o binário ou DLL Python. Quando encontrados,
seus cabeçalhos PE precisam ser analisados para localizar a estrutura
"PyRuntime".

O formato PE organiza código e dados em seções. A estrutura de
"PyRuntime" reside em uma seção chamada "PyRuntim" (truncado de
"PyRuntime" devido ao limite de 8 caracteres para nomes do PE). O
cálculo do endereço de tempo de execução envolve encontrar o endereço
base do módulo a partir da entrada do módulo e, em seguida, localizar
nossa seção de destino nos cabeçalhos do PE. O endereço final é
calculado combinando o endereço base com o endereço virtual da seção,
a partir dos cabeçalhos da seção do PE.

Observe que acessar a memória de outro processo no Windows normalmente
requer privilégios apropriados — acesso administrativo ou o privilégio
de "SeDebugPrivilege" concedidos ao processo de depuração.


Lendo _Py_DebugOffsets
**********************

Depois que o endereço da estrutura "PyRuntime" for determinado, o
próximo passo é ler a estrutura "_Py_DebugOffsets" localizada no
início do bloco "PyRuntime".

Esta estrutura fornece deslocamentos de campo específicos da versão,
necessários para ler com segurança a memória de estado de thread e do
interpretador. Esses deslocamentos variam entre as versões do CPython
e devem ser verificados antes do uso para garantir sua
compatibilidade.

Para ler e verificar os deslocamentos de depuração, siga estas etapas:

1. Lê a memória do processo de destino, começando no endereço
   "PyRuntime", cobrindo o mesmo número de bytes que a estrutura
   "_Py_DebugOffsets". Essa estrutura está localizada no início do
   bloco de memória "PyRuntime". Seu layout é definido nos cabeçalhos
   internos do CPython e permanece o mesmo em uma determinada versão
   secundária, mas pode mudar em versões principais.

2. Verifica se a estrutura contém dados válidos:

   * O campo "cookie" deve corresponder ao marcador de depuração
     esperado.

   * O campo "version" deve corresponder à versão do interpretador
     Python usado pelo depurador.

   * Se o depurador ou o processo de destino estiver usando uma versão
     de pré-lançamento (por exemplo, uma versão alfa, beta ou
     candidata a lançamento), as versões deverão corresponder
     exatamente.

   * O campo "free_threaded" deve ter o mesmo valor no depurador e no
     processo de destino.

3. Se a estrutura for válida, os deslocamentos que ela contém podem
   ser usados para localizar campos na memória. Se alguma verificação
   falhar, o depurador deve interromper a operação para evitar a
   leitura da memória no formato errado.

A seguir está um exemplo de implementação que lê e verifica
"_Py_DebugOffsets":

   def read_debug_offsets(pid: int, py_runtime_addr: int) -> DebugOffsets:
       # Etapa 1: lê a memória do processo de destino no endereço PyRuntime
       data = read_process_memory(
           pid, address=py_runtime_addr, size=DEBUG_OFFSETS_SIZE
       )

       # Etapa 2: desserializa os bytes brutos em uma estrutura _Py_DebugOffsets
       debug_offsets = parse_debug_offsets(data)

       # Etapa 3: valida o conteúdo da estrutura
       if debug_offsets.cookie != EXPECTED_COOKIE:
           raise RuntimeError("Invalid or missing debug cookie")
       if debug_offsets.version != LOCAL_PYTHON_VERSION:
           raise RuntimeError(
               "Mismatch between caller and target Python versions"
           )
       if debug_offsets.free_threaded != LOCAL_FREE_THREADED:
           raise RuntimeError("Mismatch in free-threaded configuration")

       return debug_offsets

Aviso:

  **Suspensão de processo recomendada**Para evitar condições de
  corrida e garantir a consistência da memória, é altamente
  recomendável suspender o processo de destino antes de executar
  qualquer operação que leia ou grave o estado interno do
  interpretador. O tempo de execução do Python pode, simultaneamente,
  alterar as estruturas de dados do interpretador — como criar ou
  destruir threads — durante a execução normal. Isso pode resultar em
  leituras ou gravações de memória inválidas.Um depurador pode
  suspender a execução anexando-se ao processo com "ptrace" ou
  enviando um sinal "SIGSTOP". A execução só deve ser retomada após a
  conclusão das operações de memória do lado do depurador.

  Nota:

    Algumas ferramentas, como perfiladores ou depuradores baseados em
    amostragem, podem operar em um processo em execução sem suspensão.
    Nesses casos, as ferramentas devem ser explicitamente projetadas
    para lidar com memória parcialmente atualizada ou inconsistente.
    Para a maioria das implementações de depuradores, suspender o
    processo continua sendo a abordagem mais segura e robusta.


Localizando o estado de thread e do interpretador
*************************************************

Antes que o código possa ser injetado e executado em um processo
Python remoto, o depurador deve escolher uma thread para agendar a
execução. Isso é necessário porque os campos de controle usados para
realizar a injeção remota de código estão localizados na estrutura
"_PyRemoteDebuggerSupport", que está incorporada em um objeto
"PyThreadState". Esses campos são modificados pelo depurador para
solicitar a execução dos scripts injetados.

A estrutura "PyThreadState" representa uma thread em execução dentro
de um interpretador Python. Ela mantém o contexto de avaliação da
thread e contém os campos necessários para a coordenação do depurador.
Localizar um "PyThreadState" válido é, portanto, um pré-requisito
essencial para acionar a execução remotamente.

Uma thread é normalmente selecionada com base em sua função ou ID. Na
maioria dos casos, a thread principal é usada, mas algumas ferramentas
podem direcionar uma thread específica por seu ID nativo. Uma vez
escolhida a thread de destino, o depurador deve localizar o
interpretador e as estruturas de estado de thread associadas na
memória.

As estruturas internas relevantes são definidas da seguinte forma:

* "PyInterpreterState" representa uma instância isolada de um
  interpretador Python. Cada interpretador mantém seu próprio conjunto
  de módulos importados, estado embutido e lista de estados de thread.
  Embora a maioria das aplicações Python use um único interpretador, o
  CPython oferece suporte a múltiplos interpretadores no mesmo
  processo.

* "PyThreadState" representa uma thread em execução dentro de um
  interpretador. Ele contém o estado de execução e os campos de
  controle usados pelo depurador.

Para localizar uma thread:

1. Use o offset "runtime_state.interpreters_head" para obter o
   endereço do primeiro interpretador na estrutura "PyRuntime". Este é
   o ponto de entrada para a lista vinculada de interpretadores
   ativos.

2. Use o deslocamento "interpreter_state.threads_main" para acessar o
   estado da thread principal associada ao interpretador selecionado.
   Normalmente, esta é a thread mais confiável para ser alvo.

3. Opcionalmente, use o deslocamento "interpreter_state.threads_head"
   para iterar pela lista encadeada de todos os estados de thread.
   Cada estrutura "PyThreadState" contém um campo "native_thread_id",
   que pode ser comparado a um ID da thread de destino para encontrar
   uma thread específica.

4. Depois que um "PyThreadState" válido for encontrado, seu endereço
   poderá ser usado em etapas posteriores do protocolo, como escrever
   campos de controle do depurador e agendar a execução.

A seguir está um exemplo de implementação que localiza o estado da
thread principal:

   def find_main_thread_state(
       pid: int, py_runtime_addr: int, debug_offsets: DebugOffsets,
   ) -> int:
       # Etapa 1: lê interpreters_head do PyRuntime
       interp_head_ptr = (
           py_runtime_addr + debug_offsets.runtime_state.interpreters_head
       )
       interp_addr = read_pointer(pid, interp_head_ptr)
       if interp_addr == 0:
           raise RuntimeError("No interpreter found in the target process")

       # Etapa 2: lê o ponteiro threads_main do interpretador
       threads_main_ptr = (
           interp_addr + debug_offsets.interpreter_state.threads_main
       )
       thread_state_addr = read_pointer(pid, threads_main_ptr)
       if thread_state_addr == 0:
           raise RuntimeError("Main thread state is not available")

       return thread_state_addr

O exemplo a seguir demonstra como localizar uma thread pelo seu ID de
thread nativo:

   def find_thread_by_id(
       pid: int,
       interp_addr: int,
       debug_offsets: DebugOffsets,
       target_tid: int,
   ) -> int:
       # Começa em threads_head e percorre a lista vinculada
       thread_ptr = read_pointer(
           pid,
           interp_addr + debug_offsets.interpreter_state.threads_head
       )

       while thread_ptr:
           native_tid_ptr = (
               thread_ptr + debug_offsets.thread_state.native_thread_id
           )
           native_tid = read_int(pid, native_tid_ptr)
           if native_tid == target_tid:
               return thread_ptr
           thread_ptr = read_pointer(
               pid,
               thread_ptr + debug_offsets.thread_state.next
           )

       raise RuntimeError("Thread with the given ID was not found")

Depois que um estado de thread válido for localizado, o depurador pode
prosseguir com a modificação de seus campos de controle e agendar a
execução, conforme descrito na próxima seção.


Escrevendo informações de controle
**********************************

Uma vez identificada uma estrutura "PyThreadState" válida, o depurador
pode modificar campos de controle dentro dela para agendar a execução
de um script Python especificado. Esses campos de controle são
verificados periodicamente pelo interpretador e, quando definidos
corretamente, acionam a execução do código remoto em um ponto seguro
no laço de avaliação.

Cada "PyThreadState" contém uma estrutura "_PyRemoteDebuggerSupport"
usada para comunicação entre o depurador e o interpretador. As
localizações de seus campos são definidas pela estrutura
"_Py_DebugOffsets" e incluem o seguinte:

* "debugger_script_path": Um buffer de tamanho fixo que detém o
  caminho completo para um arquivo-fonte Python (".py"). Este arquivo
  deve estar acessível e legível pelo processo de destino quando a
  execução for acionada.

* "debugger_pending_call": Um sinalizador inteiro. Definir como "1"
  informa ao interpretador que um script está pronto para ser
  executado.

* "eval_breaker": Um campo verificado pelo interpretador durante a
  execução. Definir o bit 5 ("_PY_EVAL_PLEASE_STOP_BIT", valor "1U <<
  5") neste campo faz com que o interpretador pause e verifique a
  atividade do depurador.

Para concluir a injeção, o depurador deve executar as seguintes
etapas:

1. Escreve o caminho completo do script no buffer
   "debugger_script_path".

2. Define "debugger_pending_call" com "1".

3. Lê o valor atual de "eval_breaker", define o bit 5
   ("_PY_EVAL_PLEASE_STOP_BIT") e grava o valor atualizado de volta.
   Isso sinaliza ao interpretador para verificar a atividade do
   depurador.

A seguir está um exemplo de implementação:

   def inject_script(
       pid: int,
       thread_state_addr: int,
       debug_offsets: DebugOffsets,
       script_path: str
   ) -> None:
       # Calcula o deslocamento base de _PyRemoteDebuggerSupport
       support_base = (
           thread_state_addr +
           debug_offsets.debugger_support.remote_debugger_support
       )

       # Etapa 1: Escreve o caminho do script em debugger_script_path
       script_path_ptr = (
           support_base +
           debug_offsets.debugger_support.debugger_script_path
       )
       write_string(pid, script_path_ptr, script_path)

       # Etapa 2: Define debugger_pending_call com 1
       pending_ptr = (
           support_base +
           debug_offsets.debugger_support.debugger_pending_call
       )
       write_int(pid, pending_ptr, 1)

       # Etapa 3: Define _PY_EVAL_PLEASE_STOP_BIT (bit 5, valor 1 << 5)
       # em eval_breaker
       eval_breaker_ptr = (
           thread_state_addr +
           debug_offsets.debugger_support.eval_breaker
       )
       breaker = read_int(pid, eval_breaker_ptr)
       breaker |= (1 << 5)
       write_int(pid, eval_breaker_ptr, breaker)

Após a configuração desses campos, o depurador pode retomar o processo
(caso tenha sido suspenso). O interpretador processará a solicitação
no próximo ponto de avaliação seguro, carregará o script do disco e o
executará.

É responsabilidade do depurador garantir que o arquivo de script
permaneça presente e acessível ao processo de destino durante a
execução.

Nota:

  A execução do script é assíncrona. O arquivo de script não pode ser
  excluído imediatamente após a injeção. O depurador deve aguardar até
  que o script injetado produza um efeito observável antes de remover
  o arquivo. Esse efeito depende do objetivo do script. Por exemplo,
  um depurador pode aguardar até que o processo remoto se conecte
  novamente a um soquete antes de remover o script. Uma vez observado
  esse efeito, é seguro presumir que o arquivo não é mais necessário.


Resumo
******

Para injetar e executar um script Python em um processo remoto:

1. Localize a estrutura "PyRuntime" na memória do processo de destino.

2. Lê e valida a estrutura "_Py_DebugOffsets" no início de
   "PyRuntime".

3. Usa os deslocamentos para localizar um "PyThreadState" válido.

4. Escreve o caminho para um script Python em "debugger_script_path".

5. Define o sinalizador "debugger_pending_call" com "1".

6. Define "_PY_EVAL_PLEASE_STOP_BIT" no campo "eval_breaker".

7. Retoma o processo (se suspenso). O script será executado no próximo
   ponto de avaliação seguro.


Security and threat model
*************************

The remote debugging protocol relies on the same operating system
primitives used by native debuggers such as GDB and LLDB.  Attaching
to a process requires the **same privileges** that those debuggers
require, for example "ptrace" / Yama LSM on Linux, "task_for_pid" on
macOS, and "SeDebugPrivilege" on Windows.  Python does not introduce
any new privilege escalation path; if an attacker already possesses
the permissions needed to attach to a process, they could equally use
GDB to read memory or inject code.

The following principles define what is, and is not, considered a
security vulnerability in this feature:

Attaching requires OS-level privileges
   On every supported platform the operating system gates cross-
   process memory access behind privilege checks ("CAP_SYS_PTRACE",
   root, or administrator rights).  A report that demonstrates an
   issue only after these privileges have already been obtained is
   **not** a vulnerability in CPython, since the OS security boundary
   was already crossed.

Crashes or memory errors when reading a compromised process are not
vulnerabilities
   A tool that reads internal interpreter state from a target process
   must trust that memory to be well-formed.  If the target process
   has been corrupted or is controlled by an attacker, the debugger or
   profiler may crash, produce garbage output, or behave
   unpredictably.  This is the same risk accepted by every
   "ptrace"-based debugger.  Bugs in this category (buffer overflows,
   segmentation faults, or undefined behaviour triggered by reading
   corrupted state) are **not** treated as security issues, though
   fixes that improve robustness are welcome.

Vulnerabilities in the target process are not in scope
   If the Python process being debugged has already been compromised,
   the attacker already controls execution in that process.
   Demonstrating further impact from that starting point does not
   constitute a vulnerability in the remote debugging protocol.


When to use "PYTHON_DISABLE_REMOTE_DEBUG"
=========================================

The environment variable "PYTHON_DISABLE_REMOTE_DEBUG" (and the
equivalent "-X disable-remote-debug" flag) allows operators to disable
the in-process side of the protocol as a **defence-in-depth** measure.
This may be useful in hardened or sandboxed deployment environments
where no debugging or profiling of the process is expected and
reducing attack surface is a priority, even though the OS-level
privilege checks already prevent unprivileged access.

Setting this variable does **not** affect other OS-level debugging
interfaces ("ptrace", "/proc", "task_for_pid", etc.), which remain
available according to their own permission models.
