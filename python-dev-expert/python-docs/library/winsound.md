"winsound" --- Interface de reprodução de som para o Windows
************************************************************

**Código-fonte:** PC/winsound.c

======================================================================

O módulo "winsound" fornece acesso ao mecanismo básico de reprodução
de som fornecido pelas plataformas Windows. Inclui funções e várias
constantes.

Disponibilidade: Windows.


Funções
=======

winsound.Beep(frequency, duration)

   Emite um bipe no alto-falante do PC. O parâmetro *frequency*
   especifica a frequência, em hertz, do som e deve estar no intervalo
   de 37 a 32.767. O parâmetro *duration* especifica o número de
   milissegundos que o som deve durar. Se o sistema não conseguir
   emitir um bipe no alto-falante, "RuntimeError" é levantado.

winsound.PlaySound(sound, flags)

   Chama a função subjacente "PlaySound()" da API da plataforma. O
   parâmetro *sound* pode ser um nome de arquivo, um apelido de som do
   sistema, dados de áudio como um *objeto bytes ou similar* ou
   "None". Sua interpretação depende do valor de *flags*, que pode ser
   uma combinação OU bit a bit das constantes descritas abaixo. Se o
   parâmetro *sound* for "None", qualquer som de forma de onda em
   execução no momento será interrompido. Se o sistema indicar um
   erro, "RuntimeError" será levantada.

winsound.MessageBeep(type=MB_OK)

   Chama a função subjacente "MessageBeep()" da API da plataforma.
   Isso reproduz um som conforme especificado no registro. O argumento
   *type* especifica qual som reproduzir; os valores possíveis são
   "-1", "MB_ICONASTERISK", "MB_ICONEXCLAMATION", "MB_ICONHAND",
   "MB_ICONQUESTION" e "MB_OK", todos descritos abaixo. O valor "-1"
   produz um "bipe simples"; este é o fallback final se um som não
   puder ser reproduzido de outra forma. Se o sistema indicar um erro,
   "RuntimeError" será levantada.


Constantes
==========

winsound.SND_FILENAME

   O parâmetro *sound* é o nome de um arquivo WAV. Não use com
   "SND_ALIAS".

winsound.SND_ALIAS

   O parâmetro *sound* é um nome de associação de som do registro. Se
   o registro não contiver tal nome, reproduza o som padrão do
   sistema, a menos que "SND_NODEFAULT" também seja especificado. Se
   nenhum som padrão for registrado, levanta "RuntimeError". Não use
   com "SND_FILENAME".

   Todos os sistemas Win32 oferecem suporte a pelo menos o seguinte; a
   maioria dos sistemas oferecem suporte a muito mais:

   +----------------------------+------------------------------------------+
   | *name* "PlaySound()"       | Nome do som correspondente no Painel de  |
   |                            | Controle                                 |
   |============================|==========================================|
   | "'SystemAsterisk'"         | Asterisco                                |
   +----------------------------+------------------------------------------+
   | "'SystemExclamation'"      | Exclamação                               |
   +----------------------------+------------------------------------------+
   | "'SystemExit'"             | Logoff do Windows                        |
   +----------------------------+------------------------------------------+
   | "'SystemHand'"             | Parada crítica                           |
   +----------------------------+------------------------------------------+
   | "'SystemQuestion'"         | Pergunta                                 |
   +----------------------------+------------------------------------------+

   Por exemplo:

      import winsound
      # Reproduz o som de logoff do Windows.
      winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

      # Provavelmente reproduz o som padrão do Windows, se algum
      # estiver registrado (porque "*" provavelmente não é o nome registrado
      # de algum som).
      winsound.PlaySound("*", winsound.SND_ALIAS)

winsound.SND_LOOP

   Reproduz o som repetidamente. O sinalizador "SND_ASYNC" também deve
   ser usado para evitar bloqueio. Não pode ser usado com
   "SND_MEMORY".

winsound.SND_MEMORY

   O parâmetro *sound* para "PlaySound()" é uma imagem de memória de
   um arquivo WAV, como um *objeto bytes ou similar*.

   Nota:

     Este módulo não oferece suporte à reprodução de uma imagem de
     memória de forma assíncrona, portanto, uma combinação deste
     sinalizador e "SND_ASYNC" levantará "RuntimeError".

winsound.SND_PURGE

   Para de reproduzir todas as instâncias do som especificado.

   Nota:

     Não há suporte a este sinalizador em plataformas Windows
     modernas.

winsound.SND_ASYNC

   Retorna imediatamente, permitindo que os sons sejam reproduzidos de
   forma assíncrona.

winsound.SND_NODEFAULT

   Se o som especificado não for encontrado, o som padrão do sistema
   não será reproduzido.

winsound.SND_NOSTOP

   Não interrompe os sons que estão sendo reproduzidos.

winsound.SND_NOWAIT

   Retorna imediatamente se o driver de som estiver ocupado.

   Nota:

     Não há suporte a este sinalizador em plataformas Windows
     modernas.

winsound.SND_APPLICATION

   O parâmetro *sound* é um apelido específico da aplicação no
   registro. Este sinalizador pode ser combinado com o sinalizador
   "SND_ALIAS" para especificar um apelido de som definido pela
   aplicação.

winsound.SND_SENTRY

   Aciona um evento SoundSentry quando o som é reproduzido.

   Adicionado na versão 3.14.

winsound.SND_SYNC

   O som é reproduzido de forma sincronizada. Este é o comportamento
   padrão.

   Adicionado na versão 3.14.

winsound.SND_SYSTEM

   Atribui o som à sessão de áudio para sons de notificação do
   sistema.

   Adicionado na versão 3.14.

winsound.MB_ICONASTERISK

   Reproduz o som "SystemDefault".

winsound.MB_ICONEXCLAMATION

   Reproduz o som "SystemExclamation".

winsound.MB_ICONHAND

   Reproduz o som "SystemHand".

winsound.MB_ICONQUESTION

   Reproduz o som "SystemQuestion".

winsound.MB_OK

   Reproduz o som "SystemDefault".

winsound.MB_ICONERROR

   Reproduz o som "SystemHand".

   Adicionado na versão 3.14.

winsound.MB_ICONINFORMATION

   Reproduz o som "SystemDefault".

   Adicionado na versão 3.14.

winsound.MB_ICONSTOP

   Reproduz o som "SystemHand".

   Adicionado na versão 3.14.

winsound.MB_ICONWARNING

   Reproduz o som "SystemExclamation".

   Adicionado na versão 3.14.
