Utilitários do sistema operacional
**********************************

PyObject *PyOS_FSPath(PyObject *path)
    *Retorna valor: Nova referência.** Parte da ABI Estável desde a
   versão 3.6.*

   Retorna a representação do sistema de arquivos para *path*. Se o
   objeto for um objeto "str" ou "bytes", então uma nova *referência
   forte* é retornada. Se o objeto implementa a interface
   "os.PathLike", então "__fspath__()" é retornado desde que seja um
   objeto "str" ou "bytes". Caso contrário, "TypeError" é levantada e
   "NULL" é retornado.

   Adicionado na versão 3.6.

int Py_FdIsInteractive(FILE *fp, const char *filename)

   Retorna verdadeiro (não zero) se o arquivo padrão de E/S *fp* com o
   nome *filename* for considerado interativo. Este é o caso dos
   arquivos para os quais "isatty(fileno(fp))" é verdade. Se
   "PyConfig.interactive" for não zero, esta função também retorna
   true se o ponteiro *filename* for "NULL" ou se o nome for igual a
   uma das strings "'<stdin>'" ou "'???'".

   Esta função não deve ser chamada antes da inicialização do Python.

void PyOS_BeforeFork()
    * Parte da ABI Estável on platforms with fork() desde a versão
   3.7.*

   Função para preparar algum estado interno antes de ser feito um
   fork do processo. Isso deve ser chamado antes de chamar "fork()" ou
   qualquer função semelhante que clone o processo atual. Disponível
   apenas em sistemas onde "fork()" é definido.

   Aviso:

     A chamada C "fork()" só deve ser feita a partir da thread "main"
     (do interpretador "main"). O mesmo vale para "PyOS_BeforeFork()".

   Adicionado na versão 3.7.

void PyOS_AfterFork_Parent()
    * Parte da ABI Estável on platforms with fork() desde a versão
   3.7.*

   Função para atualizar algum estado interno depois de ser feito um
   fork do processo. Isso deve ser chamado a partir do processo pai
   depois de chamar "fork()" ou qualquer função semelhante que clone o
   processo atual, independentemente da clonagem do processo ter sido
   bem-sucedida ou não. Disponível apenas em sistemas onde "fork()" é
   definido.

   Aviso:

     A chamada C "fork()" só deve ser feita a partir da thread "main"
     (do interpretador "main"). O mesmo vale para
     "PyOS_AfterFork_Parent()".

   Adicionado na versão 3.7.

void PyOS_AfterFork_Child()
    * Parte da ABI Estável on platforms with fork() desde a versão
   3.7.*

   Função para atualizar o estado interno do interpretador depois de
   ser feito um fork do processo. Isso deve ser chamado a partir do
   processo filho depois de chamar "fork()" ou qualquer função
   semelhante que clone o processo atual, se houver alguma chance do
   processo ter uma chamada de retorno para o interpretador Python.
   Disponível apenas em sistemas onde "fork()" é definido.

   Aviso:

     A chamada C "fork()" só deve ser feita a partir da thread "main"
     (do interpretador "main"). O mesmo vale para
     "PyOS_AfterFork_Child()".

   Adicionado na versão 3.7.

   Ver também:

     "os.register_at_fork()" permite registrar funções personalizadas
     do Python para serem chamadas por "PyOS_BeforeFork()",
     "PyOS_AfterFork_Parent()" e  "PyOS_AfterFork_Child()".

void PyOS_AfterFork()
    * Parte da ABI Estável on platforms with fork().*

   Função para atualizar algum estado interno após ser feito um fork
   de processo; isso deve ser chamado no novo processo se o
   interpretador do Python continuar a ser usado. Se um novo
   executável é carregado no novo processo, esta função não precisa
   ser chamada.

   Descontinuado desde a versão 3.7: Esta função foi sucedida por
   "PyOS_AfterFork_Child()".

int PyOS_CheckStack()
    * Parte da ABI Estável on platforms with USE_STACKCHECK desde a
   versão 3.7.*

   Retorna verdadeiro quando o interpretador fica sem espaço na pilha.
   Esta é uma verificação confiável, mas só está disponível quando
   "USE_STACKCHECK" é definido (atualmente em certas versões do
   Windows usando o compilador Microsoft Visual C++). "USE_STACKCHECK"
   será definido automaticamente; você nunca deve alterar a definição
   em seu próprio código.

typedef void (*PyOS_sighandler_t)(int)
    * Parte da ABI Estável.*

PyOS_sighandler_t PyOS_getsig(int i)
    * Parte da ABI Estável.*

   Retorna o manipulador de sinal atual para o sinal *i*. Este é um
   invólucro fino em torno de "sigaction()" ou "signal()". Não chame
   essas funções diretamente!

PyOS_sighandler_t PyOS_setsig(int i, PyOS_sighandler_t h)
    * Parte da ABI Estável.*

   Define o manipulador de sinal para o sinal *i* como *h*; retornar o
   manipulador de sinal antigo. Este é um invólucro fino em torno de
   "sigaction()" ou "signal()". Não chame essas funções diretamente!

int PyOS_InterruptOccurred(void)
    * Parte da ABI Estável.*

   Verifica se um sinal "SIGINT" foi recebido.

   Retorna "1" se um "SIGINT" ocorreu e limpa o sinalizador de sinal,
   ou "0" caso contrário.

   Na maioria dos casos, você deve preferir "PyErr_CheckSignals()" em
   vez desta função. "PyErr_CheckSignals()" invoca os manipuladores de
   sinal apropriados para todos os sinais pendentes, permitindo que o
   código Python lide com o sinal corretamente. Esta função detecta
   apenas "SIGINT" e não invoca nenhum manipulador de sinal do Python.

   Esta função é segura para sinais de async e não pode falhar. O
   chamador deve manter um *estado de thread anexado*.

wchar_t *Py_DecodeLocale(const char *arg, size_t *size)
    * Parte da ABI Estável desde a versão 3.7.*

   Aviso:

     Esta função não deve ser chamada diretamente: use a API
     "PyConfig" com a função "PyConfig_SetBytesString()" que garante
     que Python esteja pré-inicializado.Esta função não deve ser
     chamada antes de Python estar pré-inicializado e para que a
     localidade LC_CTYPE seja configurada corretamente: consulte a
     função "Py_PreInitialize()".

   Decodifica uma string de bytes do *tratador de erros e codificação
   do sistema de arquivos*. Se o tratador de erros for o tratador de
   errors surrogateescape, bytes não decodificáveis são decodificados
   como caracteres no intervalo U+DC80..U+DCFF; e se uma string de
   bytes puder ser decodificada como um caractere substituto, os bytes
   são escapados usando o tratador de erros surrogateescape em vez de
   decodificá-los.

   Retorna um ponteiro para uma string de caracteres largos recém-
   alocada, usa "PyMem_RawFree()" para liberar a memória. Se o tamanho
   não for "NULL", escreve o número de caracteres largos excluindo o
   caractere nulo em "*size"

   Retorna "NULL" em erro de decodificação ou erro de alocação de
   memória. Se *size* não for "NULL", "*size" é definido como
   "(size_t)-1" em erro de memória ou definido como "(size_t)-2" em
   erro de decodificação.

   *tratador de erros e codificação do sistema de arquivos* são
   selecionados por "PyConfig_Read()": veja os membros
   "filesystem_encoding" e "filesystem_errors" de "PyConfig".

   Erros de decodificação nunca devem acontecer, a menos que haja um
   bug na biblioteca C.

   Use a função "Py_EncodeLocale()" para codificar a string de
   caracteres de volta para uma string de bytes.

   Ver também:

     As funções "PyUnicode_DecodeFSDefaultAndSize()" e
     "PyUnicode_DecodeLocaleAndSize()".

   Adicionado na versão 3.5.

   Alterado na versão 3.7: A função agora usa a codificação UTF-8 no
   Modo UTF-8 do Python.

   Alterado na versão 3.8: A função agora usa a codificação UTF-8 no
   Windows se "PyPreConfig.legacy_windows_fs_encoding" for zero;

char *Py_EncodeLocale(const wchar_t *text, size_t *error_pos)
    * Parte da ABI Estável desde a versão 3.7.*

   Codifica uma string de caracteres largos para o *tratador de erros
   e codificação do sistema de arquivos*. Se o tratador de erros for
   um tratador de erros substituto, os caracteres substitutos no
   intervalo U+DC80..U+DCFF são convertidos em bytes 0x80..0xFF.

   Retorna um ponteiro para uma string de bytes recém-alocada; use
   "PyMem_Free()" para liberar a memória. Retorna "NULL" em caso de
   erro de codificação ou de erro de alocação de memória.

   Se error_pos não for "NULL", "*error_pos" será definido como
   "(size_t)-1" em caso de sucesso, ou definido como o índice do
   caractere inválido em caso de erro de codificação.

   *tratador de erros e codificação do sistema de arquivos* são
   selecionados por "PyConfig_Read()": veja os membros
   "filesystem_encoding" e "filesystem_errors" de "PyConfig".

   Use a função "Py_DecodeLocale()" para decodificar a string de bytes
   de volta para uma string de caracteres largos.

   Aviso:

     Esta função não deve ser chamada antes de Python estar
     pré-inicializado e para que a localidade LC_CTYPE seja
     configurada corretamente: consulte a função "Py_PreInitialize()".

   Ver também:

     As funções "PyUnicode_EncodeFSDefault()" e
     "PyUnicode_EncodeLocale()".

   Adicionado na versão 3.5.

   Alterado na versão 3.7: A função agora usa a codificação UTF-8 no
   Modo UTF-8 do Python.

   Alterado na versão 3.8: A função agora usa a codificação UTF-8 no
   Windows se "PyPreConfig.legacy_windows_fs_encoding" for zero.

FILE *Py_fopen(PyObject *path, const char *mode)

   Semelhante a "fopen()", mas *path* é um objeto Python e uma exceção
   é definida em caso de erro.

   *path* deve ser um objeto "str", um objeto "bytes" ou um *objeto
   caminho ou similar*.

   Em caso de sucesso, retorna um novo ponteiro para arquivo. Em caso
   de erro, define uma exceção e retorna "NULL".

   O arquivo deve ser fechado por "Py_fclose()" em vez de chamar
   diretamente "fclose()".

   O descritor de arquivo é criado não herdável (**PEP 446**).

   O chamador deve ter um *estado de thread anexado*.

   Adicionado na versão 3.14.

int Py_fclose(FILE *file)

   Feche um arquivo que foi aberto por "Py_fopen()".

   Em caso de sucesso, retorna "0". Em caso de erro, retorna "EOF" e
   "errno" é definido para indicar o erro. Em ambos os casos, qualquer
   acesso subsequente (incluindo outra chamada a "Py_fclose()") ao
   fluxo resulta em comportamento indefinido.

   Adicionado na versão 3.14.


Funções de sistema
******************

Essas são funções utilitárias que tornam a funcionalidade do módulo
"sys" acessível ao código C. Todas elas funcionam com o dicionário do
módulo "sys" da thread do interpretador atual, que está contido na
estrutura interna do estado de thread.

PyObject *PySys_GetAttr(PyObject *name)
    * Parte da ABI Estável desde a versão 3.15.*

   Obtém o atributo *name* do módulo "sys". Retorna uma *referência
   forte*. Levanta "RuntimeError" e retorna "NULL" se ele não existir
   ou se o módulo "sys" não puder ser encontrado.

   Se o objeto inexistente não deve ser tratado como uma falha, você
   pode usar "PySys_GetOptionalAttr()" em vez disso.

   Adicionado na versão 3.15.

PyObject *PySys_GetAttrString(const char *name)
    * Parte da ABI Estável desde a versão 3.15.*

   Isso é o mesmo que "PySys_GetAttr()", mas *name* é especificado
   como uma string de bytes codificada em UTF-8 do tipo const char*,
   em vez de um PyObject*.

   Se o objeto inexistente não deve ser tratado como uma falha, você
   pode usar "PySys_GetOptionalAttrString()" em vez disso.

   Adicionado na versão 3.15.

int PySys_GetOptionalAttr(PyObject *name, PyObject **result)
    * Parte da ABI Estável desde a versão 3.15.*

   Variante de "PySys_GetAttr()" que não levanta uma exceção se o
   objeto não existir.

   * Define **result* como uma nova *referência forte* para o objeto e
     retorna "1" se o objeto existir.

   * Define **result* como "NULL" e retorna "0" sem definir uma
     exceção caso o objeto não exista.

   * Define uma exceção, atribui "NULL" a **result* e retorna "-1" se
     ocorrer um erro.

   Adicionado na versão 3.15.

int PySys_GetOptionalAttrString(const char *name, PyObject **result)
    * Parte da ABI Estável desde a versão 3.15.*

   Isso é o mesmo que "PySys_GetOptionalAttr()", mas *name* é
   especificado como uma string de bytes codificada em UTF-8 do tipo
   const char*, em vez de um PyObject*.

   Adicionado na versão 3.15.

PyObject *PySys_GetObject(const char *name)
    *Retorna valor: Referência emprestada.** Parte da ABI Estável.*

   Semelhante a "PySys_GetAttrString()", mas retorna uma *referência
   emprestada* e retorna "NULL" *sem* definir uma exceção em caso de
   falha.

   Preserva a exceção que foi definida antes da chamada.

int PySys_SetObject(const char *name, PyObject *v)
    * Parte da ABI Estável.*

   Define *name* no módulo "sys" como *v*, a menos que *v* seja
   "NULL", caso em que *name* é excluído do módulo sys. Retorna "0" em
   caso de sucesso e "-1" em caso de erro.

void PySys_WriteStdout(const char *format, ...)
    * Parte da ABI Estável.*

   Escreve a string de saída descrita por *format* em "sys.stdout".
   Nenhuma exceção será levantada, mesmo que ocorra truncamento (veja
   abaixo).

   *format* deve limitar o tamanho total da string de saída formatada
   a 1000 bytes ou menos -- após 1000 bytes, a string de saída é
   truncada. Em particular, isso significa que não devem ocorrer
   formatos "%s" irrestritos; estes devem ser limitados usando "%.1s",
   onde 2 é um número decimal calculado de forma que 3 mais o tamanho
   máximo de outros textos formatados não exceda 1000 bytes. Também
   fique atento a "%f", que pode exibir centenas de dígitos para
   números muito grandes.

   Se ocorrer um problema, ou se "sys.stdout" não estiver definido, a
   mensagem formatada será escrita na saída padrão (nível C) *stdout*.

void PySys_WriteStderr(const char *format, ...)
    * Parte da ABI Estável.*

   Como "PySys_WriteStdout()", mas escreve em "sys.stderr" ou *stderr*
   em vez disso.

void PySys_FormatStdout(const char *format, ...)
    * Parte da ABI Estável.*

   Função semelhante a PySys_WriteStdout(), mas formata a mensagem
   usando "PyUnicode_FromFormatV()" e não trunca a mensagem para um
   comprimento arbitrário.

   Adicionado na versão 3.2.

void PySys_FormatStderr(const char *format, ...)
    * Parte da ABI Estável.*

   Como "PySys_FormatStdout()", mas escreve em "sys.stderr" ou
   *stderr* em vez disso.

   Adicionado na versão 3.2.

PyObject *PySys_GetXOptions()
    *Retorna valor: Referência emprestada.** Parte da ABI Estável
   desde a versão 3.7.*

   Retorna o dicionário atual de opções "-X", de forma semelhante a
   "sys._xoptions". Em caso de erro, retorna "NULL" e uma exceção é
   definida.

   Adicionado na versão 3.2.

int PySys_Audit(const char *event, const char *format, ...)
    * Parte da ABI Estável desde a versão 3.13.*

   Levanta um evento de auditoria com todos os ganchos ativos. Retorna
   zero em caso de sucesso e um valor diferente de zero com uma
   exceção definida em caso de falha.

   O argumento de string *event* não pode ser *NULL*.

   Se algum gancho tiver sido adicionado, o argumento *format* e
   outros serão usados para construir uma tupla a ser passada. Além de
   "N", os mesmos caracteres de formatação usados  em
   "Py_BuildValue()" estão disponíveis. Se o valor construído não for
   uma tupla, ele será adicionado a uma tupla de um único elemento.

   A opção de formato "N" não deve ser usada. Ela consome uma
   referência, mas como não há como saber se os argumentos dessa
   função serão consumidos, usá-la pode causar vazamentos de
   referência.

   Observe que os caracteres de formato "#" devem sempre ser tratados
   como "Py_ssize_t", independentemente de "PY_SSIZE_T_CLEAN" ter sido
   definido.

   "sys.audit()" executa a mesma função a partir do código Python.

   Veja também "PySys_AuditTuple()".

   Adicionado na versão 3.8.

   Alterado na versão 3.8.2: É necessário o tipo "Py_ssize_t" para
   caracteres de formato "#". Anteriormente, um aviso de
   descontinuação era levantado.

int PySys_AuditTuple(const char *event, PyObject *args)
    * Parte da ABI Estável desde a versão 3.13.*

   Semelhante a "PySys_Audit()", mas passa argumentos como um objeto
   Python. *args* deve ser uma "tuple". Para não passar argumentos,
   *args* pode ser *NULL*.

   Adicionado na versão 3.13.

int PySys_AddAuditHook(Py_AuditHookFunction hook, void *userData)

   Adiciona o *gancho* chamável à lista de ganchos de auditoria
   ativos. Retorna zero em caso de sucesso e um valor diferente de
   zero em caso de falha. Se o ambiente de execução já tiver sido
   inicializado, também define um erro em caso de falha. Os ganchos
   adicionados por meio desta API são chamados para todos os
   interpretadores criados pelo ambiente de execução.

   O ponteiro *userData* é passado para a função de gancho. Como as
   funções de gancho podem ser chamadas de diferentes tempos de
   execução, esse ponteiro não deve se referir diretamente ao estado
   do Python.

   Esta função pode ser chamada com segurança antes de
   "Py_Initialize()". Quando chamada após a inicialização em tempo de
   execução, os ganchos de auditoria existentes são notificados e
   podem abortar silenciosamente a operação, levantando um erro da
   classe "Exception" (outros erros não serão silenciados).

   A função de gancho é sempre chamada com um *estado de thread
   anexado* pelo interpretador Python que levantou o evento.

   Consulte a **PEP 578** para uma descrição detalhada da auditoria.
   As funções no ambiente de execução e na biblioteca padrão que
   levantam eventos estão listadas na tabela de eventos de auditoria.
   Os detalhes estão na documentação de cada função.

   Se o interpretador estiver inicializado, esta função levanta um
   evento de auditoria "sys.addaudithook" sem argumentos. Se algum
   gancho existente levantar uma exceção derivada de "Exception", o
   novo gancho não será adicionado e a exceção será tratada.
   Consequentemente, os chamadores não podem presumir que seu gancho
   foi adicionado, a menos que controlem todos os ganchos existentes.

   typedef int (*Py_AuditHookFunction)(const char *event, PyObject *args, void *userData)

      O tipo da função de gancho. *event* é o argumento de evento em
      string C passado para "PySys_Audit()" ou "PySys_AuditTuple()".
      *args* tem a garantia de ser um "PyTupleObject". *userData* é o
      argumento passado para PySys_AddAuditHook().

   Adicionado na versão 3.8.


Controle de processos
*********************

void Py_FatalError(const char *message)
    * Parte da ABI Estável.*

   Exibe uma mensagem de erro fatal e encerra forçadamente o processo.
   Nenhuma limpeza é realizada. Esta função só deve ser invocada
   quando uma condição for detectada que torne perigoso continuar
   usando o interpretador Python; por exemplo, quando a administração
   de objetos parecer estar corrompida. No Unix, a função da
   biblioteca padrão C "abort()" é chamada, que tentará produzir um
   arquivo "core".

   A função "Py_FatalError()" é substituída por uma macro que registra
   automaticamente o nome da função atual, a menos que a macro
   "Py_LIMITED_API" esteja definida.

   Alterado na versão 3.9: Registra o nome da função automaticamente.

void Py_Exit(int status)
    * Parte da ABI Estável.*

   Encerra o processo atual. Isso chama "Py_FinalizeEx()" e, em
   seguida, chama a função da biblioteca padrão C "exit(status)". Se
   "Py_FinalizeEx()" indicar um erro, o código de status de saída será
   definido como 120.

   Alterado na versão 3.6: Erros da finalização não são mais
   ignorados.

int Py_AtExit(void (*func)())
    * Parte da ABI Estável.*

   Registra uma função de limpeza para ser chamada por
   "Py_FinalizeEx()". A função de limpeza será chamada sem argumentos
   e não deve retornar nenhum valor. No máximo 32 funções de limpeza
   podem ser registradas. Quando o registro for bem-sucedido,
   "Py_AtExit()" retorna "0"; em caso de falha, retorna "-1". A última
   função de limpeza registrada é chamada primeiro. Cada função de
   limpeza será chamada no máximo uma vez. Como a finalização interna
   do Python terá sido concluída antes da função de limpeza, nenhuma
   API do Python deve ser chamada por *func*.

   Ver também:

     "PyUnstable_AtExit()" para passar um argumento "void *data".
