Suporte a Mapas do Perf
***********************

On supported platforms (Linux and macOS), the runtime can take
advantage of *perf map files* to make Python functions visible to an
external profiling tool (such as perf or samply). A running process
may create a file in the "/tmp" directory, which contains entries that
can map a section of executable code to a name. This interface is
described in the documentation of the Linux Perf tool.

Em Python, essas APIs auxiliares podem ser usadas por bibliotecas e
recursos que dependem da geração de código de máquina dinamicamente.

Observe que manter o *estado de thread anexado* não é necessário para
essas APIs.

int PyUnstable_PerfMapState_Init(void)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Abre o arquivo "/tmp/perf-$pid.map", a menos que já esteja aberto,
   e cria uma trava para garantir escritas seguras para thread no
   arquivo (desde que as escritas sejam feitas através de
   "PyUnstable_WritePerfMapEntry()" ). Normalmente, não há necessidade
   de chamar isso explicitamente; basta usar
   "PyUnstable_WritePerfMapEntry()" e ele inicializará o estado na
   primeira chamada.

   Retorna "0" em caso de sucesso, "-1" em caso de falha ao
   criar/abrir o arquivo de mapa de desempenho ou "-2" em caso de
   falha na criação de uma trava. Verifique "errno" para mais
   informações sobre a causa de uma falha.

int PyUnstable_WritePerfMapEntry(const void *code_addr, size_t code_size, const char *entry_name)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Escreve uma única entrada no arquivo "/tmp/perf-$pid.map". Esta
   função é segura para thread. Aqui está a aparência de um exemplo de
   entrada:

      # endereço  tamanho  nome
      7f3529fcf759 b     py::bar:/run/t.py

   Chamará "PyUnstable_PerfMapState_Init()" antes de escrever a
   entrada, se o arquivo de mapa de desempenho ainda não estiver
   aberto. Retorna "0" em caso de sucesso ou os mesmos códigos de erro
   que "PyUnstable_PerfMapState_Init()" em caso de falha.

void PyUnstable_PerfMapState_Fini(void)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Fecha o arquivo de mapa do perf aberto por
   "PyUnstable_PerfMapState_Init()". Isso é chamado pelo próprio tempo
   de execução durante o desligamento do interpretador. Em geral, não
   deve haver motivo para chamar isso explicitamente, exceto para
   lidar com cenários específicos, como bifurcação.

int PyUnstable_CopyPerfMapFile(const char *parent_filename)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Open the "/tmp/perf-$pid.map" file and append the content of
   *parent_filename* to it.

   This function is available on all platforms but only generates
   output on platforms that support perf maps (currently only Linux).
   On other platforms, it does nothing.

   Adicionado na versão 3.13.

int PyUnstable_PerfTrampoline_CompileCode(PyCodeObject *code)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Compile the given code object using the current perf trampoline.

   The "current" trampoline is the one set by the runtime or the most
   recent "PyUnstable_PerfTrampoline_SetPersistAfterFork()" call.

   If no trampoline is set, falls back to normal compilation (no perf
   map entry).

   Parâmetros:
      * **code** -- The code object to compile.

   Retorna:
      0 on success, -1 on failure.

   Adicionado na versão 3.13.

int PyUnstable_PerfTrampoline_SetPersistAfterFork(int enable)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Set whether the perf trampoline should persist after a fork.

   * If "enable" is true (non-zero): perf map file remains open/valid
     post-fork. Child process inherits all existing perf map entries.

   * If "enable" is false (zero): perf map closes post-fork. Child
     process gets empty perf map.

   Default: false (clears on fork).

   Parâmetros:
      * **enable** -- 1 to enable, 0 to disable.

   Retorna:
      0 on success, -1 on failure.

   Adicionado na versão 3.13.
