"msvcrt" --- Rotinas úteis do runtime MS VC++
*********************************************

**Código-fonte:** PC/msvcrtmodule.c

======================================================================

These functions provide access to some useful capabilities on Windows
platforms. Some higher-level modules use these functions to build the
Windows implementations of their services. For example, the "getpass"
module uses this in the implementation of the "getpass()" function.

Mais documentação sobre essas funções pode ser encontrada na
documentação da API da plataforma.

O módulo implementa as variantes normal e ampla de caracteres da API
de E/S do console. A API normal lida apenas com caracteres ASCII e é
de uso limitado para aplicativos internacionalizados. A API ampla de
caracteres deve ser usada sempre que possível.

Disponibilidade: Windows.

Alterado na versão 3.3: As operações neste módulo agora levantam
"OSError" onde "IOError" foi levantado.


Operações com arquivos
======================

msvcrt.locking(fd, mode, nbytes)

   Trava parte de um arquivo com base no descritor de arquivo *fd* do
   runtime do C. Levanta "OSError" em caso de falha. A região travada
   do arquivo se estende da posição atual do arquivo por *nbytes*
   bytes e pode continuar além do final do arquivo. *mode* deve ser
   uma das constantes "LK_*" listadas abaixo. Várias regiões em um
   arquivo podem ser travadas ao mesmo tempo, mas não podem se
   sobrepor. Regiões adjacentes não são mescladas; elas devem ser
   destravadas individualmente.

   Levanta um evento de auditoria "msvcrt.locking" com os argumentos
   "fd", "mode", "nbytes".

msvcrt.LK_LOCK
msvcrt.LK_RLCK

   Trava os bytes especificados. Se os bytes não puderem ser travados,
   o programa tenta novamente imediatamente após 1 segundo. Se, após
   10 tentativas, os bytes não puderem ser travados, "OSError" é
   levantada.

msvcrt.LK_NBLCK
msvcrt.LK_NBRLCK

   Trava os bytes especificados. Se os bytes não puderem ser travados,
   uma exceção "OSError" é levantada.

msvcrt.LK_UNLCK

   Destrava os bytes especificados, que devem ter sido travados
   anteriormente.

msvcrt.setmode(fd, flags)

   Defina o modo de conversão de final de linha para o descritor de
   arquivo *fd*. Para configurá-lo no modo de texto, *flags* deve ser
   "os.O_TEXT"; para binário, deve ser "os.O_BINARY".

msvcrt.open_osfhandle(handle, flags)

   Crie um descritor de arquivo de tempo de execução do C a partir do
   identificador de arquivo *handle*. O parâmetro *flags* deve ser um
   OU bit a bit de "os.O_APPEND", "os.O_RDONLY", "os.O_TEXT" e
   "os.O_NOINHERIT". O descritor de arquivo retornado pode ser usado
   como parâmetro para "os.fdopen()" para criar um objeto de arquivo.

   O descritor de arquivo é herdável por padrão. Passe o sinalizador
   "os.O_NOINHERIT" para torná-lo não herdável.

   Levanta um evento de auditoria "msvcrt.open_osfhandle" com os
   argumentos "handle", "flags".

msvcrt.get_osfhandle(fd)

   Retorna o identificador de arquivo para o descritor de arquivo
   *fd*. Levanta "OSError" se *fd* não for reconhecido.

   Levanta um evento de auditoria "msvcrt.get_osfhandle" com o
   argumento "fd".


E/S de console
==============

msvcrt.kbhit()

   Retorna um valor diferente de zero se houver uma tecla pressionada
   aguardando leitura. Caso contrário, retorna 0.

msvcrt.getch()

   Lê um pressionamento de tecla e retorna o caractere resultante como
   uma sequência de bytes. Nada é ecoado no console. Essa chamada será
   bloqueada se um pressionamento de tecla ainda não estiver
   disponível, mas não esperará que "Enter" seja pressionado. Se a
   tecla pressionada for uma tecla de função especial, ela retornará
   "'\000'" ou "'\xe0'"; a próxima chamada retornará o código da
   chave. A tecla "Control"-"C" não pode ser lida com esta função.

msvcrt.getwch()

   Variante com caractere largo de "getch()", retornando um valor
   Unicode.

msvcrt.getche()

   Semelhante a "getch()", mas o pressionamento de tecla será repetido
   se representar um caractere imprimível.

msvcrt.getwche()

   Variante com caractere largo de "getche()", retornando um valor
   Unicode.

msvcrt.putch(char)

   Imprime a string de bytes *char* no console sem armazenar em
   buffer.

msvcrt.putwch(unicode_char)

   Variante com caractere largo de "putch()", retornando um valor
   Unicode.

msvcrt.ungetch(char)

   Faz com que a string de bytes *char* seja "empurrada" para o buffer
   do console; será o próximo caractere lido por "getch()" ou
   "getche()".

msvcrt.ungetwch(unicode_char)

   Variante com caractere largo de "ungetch()", retornando um valor
   Unicode.


Outras funções
==============

msvcrt.heapmin()

   Força o heap "malloc()" a ser limpado e retorna os blocos não
   utilizados ao sistema operacional. Em caso de falha, isso levanta
   "OSError".

msvcrt.set_error_mode(mode)

   Altera o local onde o ambiente de execução C grava uma mensagem de
   erro para um erro que pode encerrar o programa. *mode* deve ser uma
   das constantes "OUT_*" listadas abaixo ou "REPORT_ERRMODE". Retorna
   a configuração anterior ou -1 se ocorrer um erro. Disponível apenas
   na construção de depuração do Python.

msvcrt.OUT_TO_DEFAULT

   O destino dos erros é determinado pelo tipo da aplicação.
   Disponível apenas na construção de depuração do Python.

msvcrt.OUT_TO_STDERR

   O destino dos erros é um de erro padrão. Disponível apenas na
   construção de depuração do Python.

msvcrt.OUT_TO_MSGBOX

   O destino dos erros é um de caixa de mensagem. Disponível apenas na
   construção de depuração do Python.

msvcrt.REPORT_ERRMODE

   Relata o valor atual do modo de erro. Disponível apenas na
   construção de depuração do Python.

msvcrt.CrtSetReportMode(type, mode)

   Especifica o destino ou destinos para um tipo de relatório
   específico gerado por "_CrtDbgReport()" no ambiente de execução do
   MS VC++. *type* deve ser uma das constantes "CRT_*" listadas
   abaixo. *mode* deve ser uma das constantes "CRTDBG_*" listadas
   abaixo. Disponível apenas na construção de depuração do Python.

msvcrt.CrtSetReportFile(type, file)

   Após usar "CrtSetReportMode()" para especificar "CRTDBG_MODE_FILE",
   você pode especificar o identificador do arquivo que receberá o
   texto da mensagem. *type* deve ser uma das constantes "CRT_*"
   listadas abaixo. *file* deve ser o identificador do arquivo que
   você deseja especificar. Disponível apenas na construção de
   depuração do Python.

msvcrt.CRT_WARN

   Avisos, mensagens e informações que não exigem atenção imediata.

msvcrt.CRT_ERROR

   Erros, problemas irrecuperáveis e questões que exigem atenção
   imediata.

msvcrt.CRT_ASSERT

   Falhas de asserção.

msvcrt.CRTDBG_MODE_DEBUG

   Escreve a mensagem na janela de saída do depurador.

msvcrt.CRTDBG_MODE_FILE

   Escreve a mensagem em um descritor de arquivo fornecido pelo
   usuário. "CrtSetReportFile()" deve ser chamada para definir o
   arquivo ou fluxo específico a ser usado como destino.

msvcrt.CRTDBG_MODE_WNDW

   Cria uma caixa de mensagem para exibir a mensagem juntamente com os
   botões "Abort", "Retry" e "Ignore".

msvcrt.CRTDBG_REPORT_MODE

   Retorna o *modole* atual para o *type* especificado.

msvcrt.CRT_ASSEMBLY_VERSION

   A versão do CRT Assembly, do arquivo de cabeçalho "crtassem.h".

msvcrt.VC_ASSEMBLY_PUBLICKEYTOKEN

   O token da chave pública do VC Assembly, do arquivo de cabeçalho
   "crtassem.h".

msvcrt.LIBRARIES_ASSEMBLY_NAME_PREFIX

   O prefixo do nome de Libraries Assembly, do arquivo de cabeçalho
   "crtassem.h".
