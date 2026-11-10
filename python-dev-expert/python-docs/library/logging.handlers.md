"logging.handlers" --- Manipuladores de logging
***********************************************

**Código-fonte:** Lib/logging/handlers.py


Important
^^^^^^^^^

Esta página contém apenas informações de referência. Para tutoriais,
por favor consulte

* Tutorial básico

* Tutorial avançado

* Livro de receitas de logging

======================================================================

Os seguintes tratadores úteis são fornecidos neste pacote. Observe que
três dos tratadores ("StreamHandler", "FileHandler" e "NullHandler")
são, na verdade, definidos no próprio módulo "logging", mas foram
documentados aqui junto com os outros tratadores.


StreamHandler
=============

A classe "StreamHandler" localizada no pacote principal "logging",
envia a saída de log para fluxos como *sys.stdout*, *sys.stderr* ou
qualquer objeto arquivo ou similar (ou, mais precisamente, qualquer
objeto que provê os métodos "write()" e "flush()").

class logging.StreamHandler(stream=None)

   Retorna uma nova instância da classe "StreamHandler" Se *stream*
   for especificado, a instância irá utilizá-lo para a saída de log;
   caso contrário, *sys.stderr* será usado.

   emit(record)

      Se um formatador for especificado, ele será usado para formatar
      o registro. Em seguida, o registro é escrito no fluxo, seguido
      por "terminator" Se houver informações de exceção, elas são
      formatadas usando "traceback.print_exception()" e anexadas ao
      fluxo.

   flush()

      Esvazia o fluxo chamando seu método "flush()". Observe que o
      método "close()" é herdado de "Handler" e, portanto, não produz
      nenhuma saída, de modo que uma chamada explícita a "flush()"
      pode ser necessária em alguns casos.

   setStream(stream)

      Define o fluxo da instância para o valor especificado, caso seja
      diferente. O fluxo antigo é esvaziado antes que o novo fluxo
      seja definido.

      Parâmetros:
         **stream** -- O fluxo que o manipulador deve usar.

      Retorna:
         o fluxo antigo, se o fluxo tiver sido alterado, ou "None", se
         não tiver sido.

      Adicionado na versão 3.7.

   terminator

      String usada como terminador ao gravar um registro formatado em
      um fluxo. O valor padrão é "'\n'".

      Se você não quiser uma terminação com nova linha, pode definir o
      atributo "terminator" da instância do manipulador como uma
      string vazia.

      Nas versões anteriores, o terminador era codificado diretamente
      como "'\n'".

      Adicionado na versão 3.2.


FileHandler
===========

A classe "FileHandler", localizada no pacote principal "logging",
envia a saída de logging para um arquivo em disco. Ela herda a
funcionalidade de saída da classe "StreamHandler".

class logging.FileHandler(filename, mode='a', encoding=None, delay=False, errors=None)

   Retorna uma nova instância da classe "FileHandler". O arquivo
   especificado é aberto e usado como o fluxo para logging. Se *mode*
   não for especificado, "'a'" é usado. Se *encoding* não for "None",
   ele é usado para abrir o arquivo com essa codificação. Se *delay*
   for verdadeiro, então a abertura do arquivo é adiada até a primeira
   chamada de "emit()" Por padrão, o arquivo cresce indefinidamente.
   Se *errors* for especificado, ele é usado para determinar como os
   erros de codificação serão tratados.

   Alterado na versão 3.6: Além de valores do tipo string, objetos
   "Path" também são aceitos para o argumento *filename*.

   Alterado na versão 3.9: O parâmetro *errors* foi adicionado.

   close()

      Fecha o arquivo.

   emit(record)

      Envia o registro para o arquivo.

      Observe que, se o arquivo tiver sido fechado devido ao
      encerramento do sistema de logging na saída e o modo do arquivo
      for 'w', o registro não será emitido (veja bpo-42378).


NullHandler
===========

Adicionado na versão 3.1.

A classe "NullHandler", localizada no pacote principal "logging", não
realiza qualquer formatação ou saída. Ela é essencialmente um
manipulador 'no-op', destinado ao uso por desenvolvedores de
bibliotecas.

class logging.NullHandler

   Retorna uma nova instância da classe "NullHandler".

   emit(record)

      Esse método não faz nada.

   handle(record)

      Esse método não faz nada.

   createLock()

      Este método retorna "None" para a trava, pois não há E/S
      subjacente cujo acesso precise ser serializado.

Consulte Configurando logging para uma biblioteca para obter mais
informações sobre como usar "NullHandler".


WatchedFileHandler
==================

The "WatchedFileHandler" class, located in the "logging.handlers"
module, is a "FileHandler" which watches the file it is logging to. If
the file changes, it is closed and reopened using the file name.

Uma alteração no arquivo pode ocorrer devido ao modo de usar de
programas como *newsyslog* e *logrotate*, que realizam a rotação de
arquivos de log. Este manipulador, destinado ao uso em Unix/Linux,
monitora o arquivo para verificar se ele foi alterado desde a última
chamada a emit. (Considera-se que um arquivo foi alterado se o seu
dispositivo ou nó-i tiverem mudado.) Se o arquivo tiver sido alterado,
o fluxo do arquivo antigo é fechado, e o arquivo é aberto novamente
para obter um novo fluxo.

Este manipulador não é apropriado para uso no Windows, porque, nesse
sistema, arquivos de log abertos não podem ser movidos ou renomeados —
o logging abre os arquivos com travas exclusivas — e, portanto, não há
necessidade desse tipo de manipulador. Além disso, *ST_INO* não é
suportado no Windows; "stat()" sempre retorna zero para esse valor.

class logging.handlers.WatchedFileHandler(filename, mode='a', encoding=None, delay=False, errors=None)

   Retorna uma nova instância da classe "WatchedFileHandler". O
   arquivo especificado é aberto e usado como o fluxo para registro de
   logs. Se *mode* não for especificado, "'a'" será usado. Se encoding
   não for "None", ele será usado para abrir o arquivo com essa
   codificação. Se *delay* for verdadeiro, a abertura do arquivo é
   adiada até a primeira chamada a "emit()". Por padrão, o arquivo
   cresce indefinidamente. Se *errors* for fornecido, ele determina
   como erros de codificação são tratados.

   Alterado na versão 3.6: Além de valores do tipo string, objetos
   "Path" também são aceitos para o argumento *filename*.

   Alterado na versão 3.9: O parâmetro *errors* foi adicionado.

   reopenIfNeeded()

      Verifica se o arquivo foi alterado. Se tiver sido, o fluxo
      existente é descarregado e fechado, e o arquivo é aberto
      novamente, normalmente como um passo preliminar antes de enviar
      o registro para o arquivo.

      Adicionado na versão 3.6.

   emit(record)

      Emite o registro para o arquivo, mas antes chama
      "reopenIfNeeded()" para reabrir o arquivo caso ele tenha sido
      alterado.


BaseRotatingHandler
===================

The "BaseRotatingHandler" class, located in the "logging.handlers"
module, is the base class for the rotating file handlers,
"RotatingFileHandler" and "TimedRotatingFileHandler". You should not
need to instantiate this class, but it has attributes and methods you
may need to override.

class logging.handlers.BaseRotatingHandler(filename, mode, encoding=None, delay=False, errors=None)

   Os parâmetros são os mesmos de "FileHandler". Os atributos são:

   namer

      Se esse atributo for definido como um chamável, o método
      "rotation_filename()" delega a ele. Os parâmetros passados ao
      chamável são os mesmos passados para "rotation_filename()".

      Nota:

        A função namer é chamada muitas vezes durante a rotação,
        portanto deve ser a mais simples e rápida possível. Ela também
        deve retornar sempre o mesmo resultado para uma dada entrada;
        caso contrário, o comportamento da rotação pode não funcionar
        como esperado.Também vale observar que é preciso ter cuidado
        ao usar um namer para preservar certos atributo no nome do
        arquivo que são usados durante a rotação. Por exemplo,
        "RotatingFileHandler" espera ter um conjunto de arquivos de
        log cujos nomes contenham inteiros sucessivos, para que a
        rotação funcione como esperado, e "TimedRotatingFileHandler"
        remova arquivos de log antigos (com base no parâmetro
        "backupCount" passado ao inicializador do manipulador)
        determinando quais são os arquivos mais antigos a serem
        excluídos. Para que isso funcione, os nomes dos arquivos devem
        ser ordenáveis usando a porção de data/hora do nome, e um
        namer precisa respeitar isso. (Se for desejado um namer que
        não respeite esse esquema, ele deverá ser usado em uma
        subclasse de "TimedRotatingFileHandler" que substitua o método
        "getFilesToDelete()" para se adequar ao esquema de nomeação
        personalizado.)

      Adicionado na versão 3.3.

   rotator

      Se este atributo estiver definido como um chamável, o método
      "rotate()" delega a esse chamável. Os parâmetros passados ao
      chamável são os mesmos passados para "rotate()".

      Adicionado na versão 3.3.

   rotation_filename(default_name)

      Modifica o nome do arquivo de log durante a rotação.

      Isso é fornecido para que um nome de arquivo personalizado possa
      ser providenciado.

      A implementação padrão chama o atributo namer do manipulador, se
      ele for chamável, passando o nome padrão para ele. Se o atributo
      não for chamável (o padrão é "None"), o nome é devolvido sem
      alterações.

      Parâmetros:
         **default_name** -- O nome padrão para o arquivo de log.

      Adicionado na versão 3.3.

   rotate(source, dest)

      Quando ocorre a rotação, rotaciona o log atual.

      A implementação padrão chama o atributo rotator do manipulador,
      se ele for chamável, passando os argumentos source e dest para
      ele. Se o atributo não for chamável (o padrão é "None"), o
      arquivo de origem é simplesmente renomeado para o destino.

      Parâmetros:
         * **source** -- O nome do arquivo de origem. Normalmente,
           este é o nome base do arquivo, por exemplo, 'test.log'.

         * **dest** -- O nome do arquivo de destino. Normalmente, é
           para onde o arquivo de origem é rotacionado, por exemplo,
           'test.log.1'.

      Adicionado na versão 3.3.

O motivo da existência desses atributos é evitar que você precise
criar subclasses — é possível usar os mesmos chamáveis para instâncias
de "RotatingFileHandler" e "TimedRotatingFileHandler". Se o chamável
namer ou rotator levantar uma exceção, ela será tratada da mesma forma
que qualquer outra exceção durante uma chamada a "emit()", isto é, por
meio do método "handleError()" do manipulador.

Se precisar fazer alterações mais significativas no processamento de
rotação, você pode substituir os métodos.

Para um exemplo, consulte Using a rotator and namer to customize log
rotation processing.


RotatingFileHandler
===================

The "RotatingFileHandler" class, located in the "logging.handlers"
module, supports rotation of disk log files.

class logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False, errors=None)

   Retorna uma nova instância da classe "RotatingFileHandler". O
   arquivo especificado é aberto e usado como o stream para logging.
   Se *mode* não for especificado, "'a'" é usado. Se *encoding* não
   for "None", ele é usado para abrir o arquivo com essa codificação.
   Se *delay* for verdadeiro, a abertura do arquivo é adiada até a
   primeira chamada a "emit()".  Por padrão, o arquivo cresce
   indefinidamente. Se *errors* for fornecido, ele é usado para
   determinar como erros de codificação são tratados.

   Você pode usar os valores *maxBytes* e *backupCount* para permitir
   que o arquivo faça *rollover* em um tamanho predeterminado. Quando
   o tamanho está prestes a ser excedido, o arquivo é fechado e um
   novo arquivo é aberto silenciosamente para saída. A rotação ocorre
   sempre que o arquivo de log atual está próximo de *maxBytes* em
   comprimento; mas, se *maxBytes* ou *backupCount* for zero, a
   rotação nunca ocorre, portanto, em geral, você deve definir
   *backupCount* como pelo menos 1 e usar um *maxBytes* diferente de
   zero. Quando *backupCount* é diferente de zero, o sistema salva
   arquivos de log antigos acrescentando as extensões '.1', '.2' etc.
   ao nome do arquivo. Por exemplo, com um *backupCount* de 5 e um
   nome de arquivo base "app.log", você terá "app.log", "app.log.1",
   "app.log.2", até "app.log.5". O arquivo no qual se escreve é sempre
   "app.log". Quando esse arquivo é preenchido, ele é fechado e
   renomeado para "app.log.1" e, se existirem os arquivos "app.log.1",
   "app.log.2" etc., eles são renomeados para "app.log.2", "app.log.3"
   etc., respectivamente.

   Alterado na versão 3.6: Além de valores do tipo string, objetos
   "Path" também são aceitos para o argumento *filename*.

   Alterado na versão 3.9: O parâmetro *errors* foi adicionado.

   doRollover()

      Realiza uma rotação, conforme descrito acima.

   emit(record)

      Grava o registro no arquivo, tratando a rotação conforme
      descrito anteriormente.

   shouldRollover(record)

      Verifica se o registro fornecido faria o arquivo exceder o
      limite de tamanho configurado.


TimedRotatingFileHandler
========================

The "TimedRotatingFileHandler" class, located in the
"logging.handlers" module, supports rotation of disk log files at
certain timed intervals.

class logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None, errors=None)

   Retorna uma nova instância da classe "TimedRotatingFileHandler". O
   arquivo especificado é aberto e usado como fluxo para o logging.
   Durante a rotação, o sufixo do nome do arquivo também é definido. A
   rotação ocorre com base no produto de *when* e *interval*.

   Você pode usar o *when* para especificar o tipo de *intervalo*. A
   lista de possíveis valores está abaixo.  Observe que eles não
   diferenciam maiúsculas de minúsculas.

   +------------------+------------------------------+---------------------------+
   | Valor            | Tipo de intervalo            | Se/como *atTime* é usado  |
   |==================|==============================|===========================|
   | "'S'"            | Segundos                     | Ignorado                  |
   +------------------+------------------------------+---------------------------+
   | "'M'"            | Minutos                      | Ignorado                  |
   +------------------+------------------------------+---------------------------+
   | "'H'"            | Horas                        | Ignorado                  |
   +------------------+------------------------------+---------------------------+
   | "'D'"            | Dias                         | Ignorado                  |
   +------------------+------------------------------+---------------------------+
   | "'W0'-'W6'"      | Dia da semana (0=Segunda)    | Usado para calcular o     |
   |                  |                              | tempo inicial de rotação  |
   +------------------+------------------------------+---------------------------+
   | "'midnight'"     | Faz a rotação à meia-noite,  | Usado para calcular o     |
   |                  | se *atTime* não for          | tempo inicial de rotação  |
   |                  | especificado; caso           |                           |
   |                  | contrário, no horário        |                           |
   |                  | *atTime*.                    |                           |
   +------------------+------------------------------+---------------------------+

   Ao usar rotação baseada em dia da semana, especifique 'W0' para
   segunda-feira, 'W1' para terça-feira, e assim por diante até 'W6'
   para domingo. Nesse caso, o valor passado para *interval* não é
   utilizado.

   O sistema salvará arquivos de log antigos acrescentando extensões
   ao nome do arquivo. As extensões são baseadas em data e hora,
   usando o formato strftime "%Y-%m-%d_%H-%M-%S" ou uma porção inicial
   dele, dependendo do intervalo de rollover.

   Quando a próximo rotação é calculada pela primeira vez (no momento
   em que o manipulador é criado), o tempo da última modificação de um
   arquivo de log existente — ou, caso contrário, o tempo atual — é
   usado para determinar quando a próxima rotação ocorrerá.

   Se o argumento *utc* for verdadeiro, serão usados horários em
   Horário Universal Coordenado (UTC); caso contrário, será usado o
   horário local.

   Se *backupCount* for diferente de zero, no máximo *backupCount*
   arquivos serão mantidos, e, se mais arquivos fossem criados quando
   ocorrer a rotação, o mais antigo será excluído. A lógica de
   exclusão usa o interval para determinar quais arquivos devem ser
   removidos; assim, alterar o intervalo pode deixar arquivos antigos
   remanescentes.

   Se *delay* for verdadeiro, a abertura do arquivo será adiada até a
   primeira chamada para "emit()".

   Se *atTime* não for "None", ele deve ser uma instância de
   "datetime.time" que especifica a hora do dia em que ocorre a
   rotação, nos casos em que a rotação está configurada para acontecer
   “à meia-noite” ou “em um determinado dia da semana”. Observe que,
   nesses casos, o valor de *atTime* é efetivamente usado para
   calcular a rotação inicial, e as rotações subsequentes são
   calculadas por meio do cálculo normal do intervalo.

   Se *erros* for especificado, ele será usado para determinar como
   erros de codificação são tratados.

   Nota:

     O cálculo do tempo da rotação inicial é feito quando o
     manipulador é inicializado. O cálculo dos tempos de rotações
     subsequentes é feito apenas quando ocorre uma rotação, e a
     rotação ocorre somente quando há emissão de saída. Se isso não
     for levado em consideração, pode causar alguma confusão. Por
     exemplo, se for definido um intervalo de “a cada minuto”, isso
     não significa que você sempre verá arquivos de log com horários
     (no nome do arquivo) separados por um minuto; se, durante a
     execução da aplicação, a saída de log for gerada com maior
     frequência do que uma vez por minuto, então você pode esperar
     observar arquivos de log com horários separados por um minuto.
     Se, por outro lado, as mensagens de log forem emitidas apenas uma
     vez a cada cinco minutos (por exemplo), então haverá lacunas nos
     horários dos arquivos correspondentes aos minutos em que não
     houve saída (e, portanto, nenhuma rotação).

   Alterado na versão 3.4: parâmetro *atTime* foi adicionado.

   Alterado na versão 3.6: Além de valores do tipo string, objetos
   "Path" também são aceitos para o argumento *filename*.

   Alterado na versão 3.9: O parâmetro *errors* foi adicionado.

   doRollover()

      Realiza uma rotação, conforme descrito acima.

   emit(record)

      Emite o registro para o arquivo, com a preparação para a
      rotação, conforme descrito acima.

   getFilesToDelete()

      Retorna uma lista de nomes de arquivos que devem ser excluídos
      como parte da rotação. Esses são os caminhos absolutos dos
      arquivos de log de backup mais antigos gravados pelo
      manipulador.

   shouldRollover(record)

      Verifica se passou tempo suficiente para que a rotação ocorra e,
      se for o caso, calcula o próximo horário da rotação.


SocketHandler
=============

The "SocketHandler" class, located in the "logging.handlers" module,
sends logging output to a network socket. The base class uses a TCP
socket.

class logging.handlers.SocketHandler(host, port)

   Retorna uma nova instância da classe "SocketHandler", destinada a
   se comunicar com uma máquina remota cujo endereço é fornecido por
   *host* e *port*.

   Alterado na versão 3.4: Se "port" for especificado como "None", um
   Soquete de domínio Unix será criado usando o valor em "host" - caso
   contrário, um soquete TCP será criado.

   close()

      Fecha o soquete.

   emit()

      Serializa com pickle o dicionário de atributos do registro e o
      grava no soquete em formato binário. Se houver um erro com o
      soquete, o pacote é descartado silenciosamente. Se a conexão
      tiver sido perdida anteriormente, ela é restabelecida. Para
      desserializar com pickle o registro no lado receptor em um
      "LogRecord", use a função "makeLogRecord()".

   handleError()

      Trata um erro ocorrido durante "emit()". A causa mais provável é
      a perda da conexão. Fecha o soquete para que seja possível
      tentar novamente no próximo evento.

   makeSocket()

      Este é um método de fábrica que permite que subclasses definam o
      tipo exato de soquete que desejam. A implementação padrão cria
      um soquete TCP ("socket.SOCK_STREAM").

   makePickle(record)

      Serializa com pickle o dicionário de atributos do registro em
      formato binário com um prefixo de comprimento e o retorna pronto
      para transmissão através do socket. Os detalhes dessa operação
      são equivalentes a:

         data = pickle.dumps(record_attr_dict, 1)
         datalen = struct.pack('>L', len(data))
         return datalen + data

      Observe que os pickles não são completamente seguros. Se você
      estiver preocupado com a segurança, pode ser necessário
      substituir este método para implementar um mecanismo mais
      seguro. Por exemplo, você pode assinar os pickles usando HMAC e
      depois verificá-los no lado receptor, ou alternativamente pode
      desativar a desserialização com pickle de objetos globais no
      lado receptor.

   send(packet)

      Envia para o soquete uma string de bytes serializada com pickle
      denominada *packet*. O formato da string de bytes enviada é o
      descrito na documentação de "makePickle()".

      Este função permite envios parciais, que podem ocorrer quando a
      rede está ocupada.

   createSocket()

      Tenta criar um soquete; em caso de falha, utiliza um algoritmo
      de back-off exponencial. Na falha inicial, o manipulador
      descarta a mensagem que estava tentando enviar. Quando mensagens
      subsequentes são tratadas pela mesma instância, ela não tentará
      se reconectar até que algum tempo tenha passado. Os parâmetros
      padrão são tais que o atraso inicial é de um segundo e, se após
      esse atraso a conexão ainda não puder ser estabelecida, o
      manipulador dobrará o atraso a cada tentativa, até um máximo de
      30 segundos.

      Este comportamento é controlado pelo seguintes atributos do
      manipulador:

      * "retryStart" (atraso inicial, padrão de 1,0 segundo).

      * "retryFactor" (multiplicador, com padrão de 2,0).

      * "retryMax" (atraso máximo, padrão de 30,0 segundos).

      Isso significa que, se o ouvinte remoto iniciar após o
      manipulador já ter sido utilizado, mensagens podem ser perdidas
      (pois o manipulador nem sequer tentará estabelecer uma conexão
      até que o atraso tenha decorrido, apenas descartando
      silenciosamente as mensagens durante esse período de atraso).


DatagramHandler
===============

The "DatagramHandler" class, located in the "logging.handlers" module,
inherits from "SocketHandler" to support sending logging messages over
UDP sockets.

class logging.handlers.DatagramHandler(host, port)

   Retorna uma nova instância da classe "DatagramHandler", destinada a
   se comunicar com uma máquina remota cujo endereço é fornecido por
   *host* e *port*.

   Nota:

     Como o UDP não é um protocolo de fluxo contínuo, não há uma
     conexão persistente entre uma instância deste manipulador e host.
     Por esse motivo, ao usar um soquete de rede, pode ser necessário
     realizar uma consulta DNS a cada vez que um evento é registrado,
     o que pode introduzir alguma latência no sistema. Se isso for um
     problema para você, pode realizar a consulta manualmente e
     inicializar este manipulador usando o endereço IP obtido, em vez
     do nome do host.

   Alterado na versão 3.4: Se "port" for especificado como "None", um
   soquete de domínio Unix é criado usando o valor de "host"; caso
   contrário, é criado um soquete UDP.

   emit()

      Serializa com pickle o dicionário de atributos do registro e o
      grava no soquete em formato binário. Se houver um erro com o
      soquete, o pacote é descartado silenciosamente. Para
      desserializar com pickle o registro no lado receptor em um
      "LogRecord", use a função "makeLogRecord()".

   makeSocket()

      A método de fábrica de "SocketHandler" aqui é substituído para
      criar um soquete UDP ("socket.SOCK_DGRAM").

   send(s)

      Envia uma sequência de bytes serializada com pickle para um
      soquete. O formato da sequência de bytes enviada é conforme
      descrito na documentação de "SocketHandler.makePickle()".


SysLogHandler
=============

The "SysLogHandler" class, located in the "logging.handlers" module,
supports sending logging messages to a remote or local Unix syslog.

class logging.handlers.SysLogHandler(address=('localhost', SYSLOG_UDP_PORT), facility=LOG_USER, socktype=socket.SOCK_DGRAM, timeout=None)

   Returns a new instance of the "SysLogHandler" class intended to
   communicate with a remote Unix machine whose address is given by
   *address* in the form of a "(host, port)" tuple.  If *address* is
   not specified, "('localhost', 514)" is used.  The address is used
   to open a socket.  An alternative to providing a "(host, port)"
   tuple is providing an address as a string, for example '/dev/log'.
   In this case, a Unix domain socket is used to send the message to
   the syslog. If *facility* is not specified, "LOG_USER" is used. The
   type of socket opened depends on the *socktype* argument, which
   defaults to "socket.SOCK_DGRAM" and thus opens a UDP socket. To
   open a TCP socket (for use with the newer syslog daemons such as
   rsyslog), specify a value of "socket.SOCK_STREAM". If *timeout* is
   specified, it sets a timeout (in seconds) for the socket
   operations. This can help prevent the program from hanging
   indefinitely if the syslog server is unreachable. By default,
   *timeout* is "None", meaning no timeout is applied.

   Observe que, se o seu servidor não estiver escutando na porta UDP
   514, o "SysLogHandler" pode parecer não funcionar. Nesse caso,
   verifique qual endereço deve ser usado para um soquete de domínio —
   isso depende do sistema. Por exemplo, no Linux geralmente é
   '/dev/log', enquanto no OS/X é '/var/run/syslog'. Será necessário
   verificar a sua plataforma e usar o endereço apropriado (talvez
   seja preciso fazer essa verificação em tempo de execução se a
   aplicação precisar rodar em várias plataformas). No Windows,
   praticamente é necessário usar a opção UDP.

   Nota:

     No macOS 12.x (Monterey), a Apple alterou o comportamento do
     daemon syslog — ele não escuta mais em um soquete de domínio.
     Portanto, não é possível esperar que "SysLogHandler" funcione
     nesse sistema.Consulte gh-91070 para obter mais informações.

   Alterado na versão 3.2: *socktype* foi adicionado.

   Alterado na versão 3.14: *timeout* foi adicionado.

   close()

      Fecha o soquete para o host remoto.

   createSocket()

      Tenta criar um soquete e, se ele não for um soquete de
      datagrama, conectá-lo à outra extremidade. Este método é chamado
      durante a inicialização do manipulador, mas não é considerado um
      erro se a outra extremidade não estiver escutando nesse momento
      — o método será chamado novamente ao emitir um evento, caso não
      haja um soquete nesse ponto.

      Adicionado na versão 3.11.

   emit(record)

      O registro é formatado e, em seguida, enviado ao servidor
      syslog. Se houver informações de exceção, elas *não* são
      enviadas ao servidor.

      Alterado na versão 3.2.1: (Veja: bpo-12168.) Em versões
      anteriores, a mensagem enviada aos daemons syslog era sempre
      terminada com um byte NUL, porque versões antigas desses daemons
      esperavam uma mensagem terminada em NUL — embora isso não conste
      na especificação relevante (**RFC 5424**). Versões mais recentes
      desses daemons não esperam o byte NUL, mas o removem caso esteja
      presente, e daemons ainda mais recentes (que aderem mais de
      perto à RFC 5424) repassam o byte NUL como parte da
      mensagem.Para facilitar o tratamento de mensagens do syslog
      diante de todos esses comportamentos distintos dos daemons, a
      adição do byte NUL tornou-se configurável por meio de um
      atributo em nível de classe, "append_nul" O valor padrão é
      "True" (preservando o comportamento existente), mas pode ser
      definido como "False" em uma instância de "SysLogHandler" para
      que essa instância não acrescente o terminador NUL.

      Alterado na versão 3.3: (Consulte: bpo-12419) Em versões
      anteriores, não havia uma instalação para um prefixo "ident" ou
      "tag" para identificar a origem da mensagem. Isso agora pode ser
      especificado usando um atributo de nível de classe, que por
      padrão é """" para preservar o comportamento existente, mas pode
      ser substituído em uma instância de "SysLogHandler" para que
      essa instância adicione o ident a cada mensagem manipulada.
      Observe que o ident fornecido deve ser texto, não bytes, e é
      adicionado à mensagem exatamente como está.

   encodePriority(facility, priority)

      Codifica a instalação e a prioridade em um inteiro. Você pode
      passar strings ou inteiros — se strings forem passadas,
      dicionários de mapeamento internos são usados para convertê-las
      em inteiros.

      Os valores simbólicos "LOG_" são definidos em "SysLogHandler" e
      espelham os valores definidos no arquivo de cabeçalho
      "sys/syslog.h".

      **Prioridades**

      +----------------------------+-----------------+
      | Nome (string)              | Valor simbólico |
      |============================|=================|
      | "alert"                    | LOG_ALERT       |
      +----------------------------+-----------------+
      | "crit" ou "critical"       | LOG_CRIT        |
      +----------------------------+-----------------+
      | "debug"                    | LOG_DEBUG       |
      +----------------------------+-----------------+
      | "emerg" or "panic"         | LOG_EMERG       |
      +----------------------------+-----------------+
      | "err" ou "error"           | LOG_ERR         |
      +----------------------------+-----------------+
      | "info"                     | LOG_INFO        |
      +----------------------------+-----------------+
      | "notice"                   | LOG_NOTICE      |
      +----------------------------+-----------------+
      | "warn" or "warning"        | LOG_WARNING     |
      +----------------------------+-----------------+

      **Facilities**

      +-----------------+-----------------+
      | Nome (string)   | Valor simbólico |
      |=================|=================|
      | "auth"          | LOG_AUTH        |
      +-----------------+-----------------+
      | "authpriv"      | LOG_AUTHPRIV    |
      +-----------------+-----------------+
      | "cron"          | LOG_CRON        |
      +-----------------+-----------------+
      | "daemon"        | LOG_DAEMON      |
      +-----------------+-----------------+
      | "ftp"           | LOG_FTP         |
      +-----------------+-----------------+
      | "kern"          | LOG_KERN        |
      +-----------------+-----------------+
      | "lpr"           | LOG_LPR         |
      +-----------------+-----------------+
      | "mail"          | LOG_MAIL        |
      +-----------------+-----------------+
      | "news"          | LOG_NEWS        |
      +-----------------+-----------------+
      | "syslog"        | LOG_SYSLOG      |
      +-----------------+-----------------+
      | "user"          | LOG_USER        |
      +-----------------+-----------------+
      | "uucp"          | LOG_UUCP        |
      +-----------------+-----------------+
      | "local0"        | LOG_LOCAL0      |
      +-----------------+-----------------+
      | "local1"        | LOG_LOCAL1      |
      +-----------------+-----------------+
      | "local2"        | LOG_LOCAL2      |
      +-----------------+-----------------+
      | "local3"        | LOG_LOCAL3      |
      +-----------------+-----------------+
      | "local4"        | LOG_LOCAL4      |
      +-----------------+-----------------+
      | "local5"        | LOG_LOCAL5      |
      +-----------------+-----------------+
      | "local6"        | LOG_LOCAL6      |
      +-----------------+-----------------+
      | "local7"        | LOG_LOCAL7      |
      +-----------------+-----------------+

   mapPriority(levelname)

      Maps a logging level name to a syslog priority name. You may
      need to override this if you are using custom levels, or if the
      default algorithm is not suitable for your needs. The default
      algorithm maps "DEBUG", "INFO", "WARNING", "ERROR" and
      "CRITICAL" to the equivalent syslog names, and all other level
      names to 'warning'.


NTEventLogHandler
=================

The "NTEventLogHandler" class, located in the "logging.handlers"
module, supports sending logging messages to a local Windows NT,
Windows 2000 or Windows XP event log. Before you can use it, you need
Mark Hammond's Win32 extensions for Python installed.

class logging.handlers.NTEventLogHandler(appname, dllname=None, logtype='Application')

   Returns a new instance of the "NTEventLogHandler" class. The
   *appname* is used to define the application name as it appears in
   the event log. An appropriate registry entry is created using this
   name. The *dllname* should give the fully qualified pathname of a
   .dll or .exe which contains message definitions to hold in the log
   (if not specified, "'win32service.pyd'" is used - this is installed
   with the Win32 extensions and contains some basic placeholder
   message definitions. Note that use of these placeholders will make
   your event logs big, as the entire message source is held in the
   log. If you want slimmer logs, you have to pass in the name of your
   own .dll or .exe which contains the message definitions you want to
   use in the event log). The *logtype* is one of "'Application'",
   "'System'" or "'Security'", and defaults to "'Application'".

   close()

      At this point, you can remove the application name from the
      registry as a source of event log entries. However, if you do
      this, you will not be able to see the events as you intended in
      the Event Log Viewer - it needs to be able to access the
      registry to get the .dll name. The current version does not do
      this.

   emit(record)

      Determines the message ID, event category and event type, and
      then logs the message in the NT event log.

   getEventCategory(record)

      Returns the event category for the record. Override this if you
      want to specify your own categories. This version returns 0.

   getEventType(record)

      Returns the event type for the record. Override this if you want
      to specify your own types. This version does a mapping using the
      handler's typemap attribute, which is set up in "__init__()" to
      a dictionary which contains mappings for "DEBUG", "INFO",
      "WARNING", "ERROR" and "CRITICAL". If you are using your own
      levels, you will either need to override this method or place a
      suitable dictionary in the handler's *typemap* attribute.

   getMessageID(record)

      Returns the message ID for the record. If you are using your own
      messages, you could do this by having the *msg* passed to the
      logger being an ID rather than a format string. Then, in here,
      you could use a dictionary lookup to get the message ID. This
      version returns 1, which is the base message ID in
      "win32service.pyd".


SMTPHandler
===========

The "SMTPHandler" class, located in the "logging.handlers" module,
supports sending logging messages to an email address via SMTP.

class logging.handlers.SMTPHandler(mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None, timeout=1.0)

   Returns a new instance of the "SMTPHandler" class. The instance is
   initialized with the from and to addresses and subject line of the
   email. The *toaddrs* should be a list of strings. To specify a non-
   standard SMTP port, use the (host, port) tuple format for the
   *mailhost* argument. If you use a string, the standard SMTP port is
   used. If your SMTP server requires authentication, you can specify
   a (username, password) tuple for the *credentials* argument.

   To specify the use of a secure protocol (TLS), pass in a tuple to
   the *secure* argument. This will only be used when authentication
   credentials are supplied. The tuple should be either an empty
   tuple, or a single-value tuple with the name of a keyfile, or a
   2-value tuple with the names of the keyfile and certificate file.
   (This tuple is passed to the "smtplib.SMTP.starttls()" method.)

   A timeout can be specified for communication with the SMTP server
   using the *timeout* argument.

   Alterado na versão 3.3: Added the *timeout* parameter.

   emit(record)

      Formats the record and sends it to the specified addressees.

   getSubject(record)

      If you want to specify a subject line which is record-dependent,
      override this method.


MemoryHandler
=============

The "MemoryHandler" class, located in the "logging.handlers" module,
supports buffering of logging records in memory, periodically flushing
them to a *target* handler. Flushing occurs whenever the buffer is
full, or when an event of a certain severity or greater is seen.

"MemoryHandler" is a subclass of the more general "BufferingHandler",
which is an abstract class. This buffers logging records in memory.
Whenever each record is added to the buffer, a check is made by
calling "shouldFlush()" to see if the buffer should be flushed.  If it
should, then "flush()" is expected to do the flushing.

class logging.handlers.BufferingHandler(capacity)

   Initializes the handler with a buffer of the specified capacity.
   Here, *capacity* means the number of logging records buffered.

   emit(record)

      Append the record to the buffer. If "shouldFlush()" returns
      true, call "flush()" to process the buffer.

   flush()

      For a "BufferingHandler" instance, flushing means that it sets
      the buffer to an empty list. This method can be overwritten to
      implement more useful flushing behavior.

   shouldFlush(record)

      Return "True" if the buffer is up to capacity. This method can
      be overridden to implement custom flushing strategies.

class logging.handlers.MemoryHandler(capacity, flushLevel=ERROR, target=None, flushOnClose=True)

   Returns a new instance of the "MemoryHandler" class. The instance
   is initialized with a buffer size of *capacity* (number of records
   buffered). If *flushLevel* is not specified, "ERROR" is used. If no
   *target* is specified, the target will need to be set using
   "setTarget()" before this handler does anything useful. If
   *flushOnClose* is specified as "False", then the buffer is *not*
   flushed when the handler is closed. If not specified or specified
   as "True", the previous behaviour of flushing the buffer will occur
   when the handler is closed.

   Alterado na versão 3.6: The *flushOnClose* parameter was added.

   close()

      Calls "flush()", sets the target to "None" and clears the
      buffer.

   flush()

      For a "MemoryHandler" instance, flushing means just sending the
      buffered records to the target, if there is one. The buffer is
      also cleared when buffered records are sent to the target.
      Override if you want different behavior.

   setTarget(target)

      Sets the target handler for this handler.

   shouldFlush(record)

      Checks for buffer full or a record at the *flushLevel* or
      higher.


HTTPHandler
===========

The "HTTPHandler" class, located in the "logging.handlers" module,
supports sending logging messages to a web server, using either "GET"
or "POST" semantics.

class logging.handlers.HTTPHandler(host, url, method='GET', secure=False, credentials=None, context=None)

   Returns a new instance of the "HTTPHandler" class. The *host* can
   be of the form "host:port", should you need to use a specific port
   number.  If no *method* is specified, "GET" is used. If *secure* is
   true, a HTTPS connection will be used. The *context* parameter may
   be set to a "ssl.SSLContext" instance to configure the SSL settings
   used for the HTTPS connection. If *credentials* is specified, it
   should be a 2-tuple consisting of userid and password, which will
   be placed in a HTTP 'Authorization' header using Basic
   authentication. If you specify credentials, you should also specify
   secure=True so that your userid and password are not passed in
   cleartext across the wire.

   Alterado na versão 3.5: The *context* parameter was added.

   mapLogRecord(record)

      Provides a dictionary, based on "record", which is to be URL-
      encoded and sent to the web server. The default implementation
      just returns "record.__dict__". This method can be overridden if
      e.g. only a subset of "LogRecord" is to be sent to the web
      server, or if more specific customization of what's sent to the
      server is required.

   emit(record)

      Sends the record to the web server as a URL-encoded dictionary.
      The "mapLogRecord()" method is used to convert the record to the
      dictionary to be sent.

   Nota:

     Since preparing a record for sending it to a web server is not
     the same as a generic formatting operation, using
     "setFormatter()" to specify a "Formatter" for a "HTTPHandler" has
     no effect. Instead of calling "format()", this handler calls
     "mapLogRecord()" and then "urllib.parse.urlencode()" to encode
     the dictionary in a form suitable for sending to a web server.


QueueHandler
============

Adicionado na versão 3.2.

The "QueueHandler" class, located in the "logging.handlers" module,
supports sending logging messages to a queue, such as those
implemented in the "queue" or "multiprocessing" modules.

Along with the "QueueListener" class, "QueueHandler" can be used to
let handlers do their work on a separate thread from the one which
does the logging. This is important in web applications and also other
service applications where threads servicing clients need to respond
as quickly as possible, while any potentially slow operations (such as
sending an email via "SMTPHandler") are done on a separate thread.

class logging.handlers.QueueHandler(queue)

   Returns a new instance of the "QueueHandler" class. The instance is
   initialized with the queue to send messages to. The *queue* can be
   any queue-like object; it's used as-is by the "enqueue()" method,
   which needs to know how to send messages to it. The queue is not
   *required* to have the task tracking API, which means that you can
   use "SimpleQueue" instances for *queue*.

   Nota:

     If you are using "multiprocessing", you should avoid using
     "SimpleQueue" and instead use "multiprocessing.Queue".

   Aviso:

     The "multiprocessing" module uses an internal logger created and
     accessed via "get_logger()". "multiprocessing.Queue" will log
     "DEBUG" level messages upon items being queued. If those log
     messages are processed by a "QueueHandler" using the same
     "multiprocessing.Queue" instance, it will cause a deadlock or
     infinite recursion.

   emit(record)

      Enqueues the result of preparing the LogRecord. Should an
      exception occur (e.g. because a bounded queue has filled up),
      the "handleError()" method is called to handle the error. This
      can result in the record silently being dropped (if
      "logging.raiseExceptions" is "False") or a message printed to
      "sys.stderr" (if "logging.raiseExceptions" is "True").

   prepare(record)

      Prepares a record for queuing. The object returned by this
      method is enqueued.

      The base implementation formats the record to merge the message,
      arguments, exception and stack information, if present.  It also
      removes unpickleable items from the record in-place.
      Specifically, it overwrites the record's "msg" and "message"
      attributes with the merged message (obtained by calling the
      handler's "format()" method), and sets the "args", "exc_info"
      and "exc_text" attributes to "None".

      You might want to override this method if you want to convert
      the record to a dict or JSON string, or send a modified copy of
      the record while leaving the original intact.

      Nota:

        The base implementation formats the message with arguments,
        sets the "message" and "msg" attributes to the formatted
        message and sets the "args" and "exc_text" attributes to
        "None" to allow pickling and to prevent further attempts at
        formatting. This means that a handler on the "QueueListener"
        side won't have the information to do custom formatting, e.g.
        of exceptions. You may wish to subclass "QueueHandler" and
        override this method to e.g. avoid setting "exc_text" to
        "None". Note that the "message" / "msg" / "args" changes are
        related to ensuring the record is pickleable, and you might or
        might not be able to avoid doing that depending on whether
        your "args" are pickleable. (Note that you may have to
        consider not only your own code but also code in any libraries
        that you use.)

   enqueue(record)

      Enqueues the record on the queue using "put_nowait()"; you may
      want to override this if you want to use blocking behaviour, or
      a timeout, or a customized queue implementation.

   listener

      When created via configuration using "dictConfig()", this
      attribute will contain a "QueueListener" instance for use with
      this handler. Otherwise, it will be "None".

      Adicionado na versão 3.12.


QueueListener
=============

Adicionado na versão 3.2.

The "QueueListener" class, located in the "logging.handlers" module,
supports receiving logging messages from a queue, such as those
implemented in the "queue" or "multiprocessing" modules. The messages
are received from a queue in an internal thread and passed, on the
same thread, to one or more handlers for processing. While
"QueueListener" is not itself a handler, it is documented here because
it works hand-in-hand with "QueueHandler".

Along with the "QueueHandler" class, "QueueListener" can be used to
let handlers do their work on a separate thread from the one which
does the logging. This is important in web applications and also other
service applications where threads servicing clients need to respond
as quickly as possible, while any potentially slow operations (such as
sending an email via "SMTPHandler") are done on a separate thread.

class logging.handlers.QueueListener(queue, *handlers, respect_handler_level=False)

   Returns a new instance of the "QueueListener" class. The instance
   is initialized with the queue to send messages to and a list of
   handlers which will handle entries placed on the queue. The queue
   can be any queue-like object; it's passed as-is to the "dequeue()"
   method, which needs to know how to get messages from it. The queue
   is not *required* to have the task tracking API (though it's used
   if available), which means that you can use "SimpleQueue" instances
   for *queue*.

   Nota:

     If you are using "multiprocessing", you should avoid using
     "SimpleQueue" and instead use "multiprocessing.Queue".

   If "respect_handler_level" is "True", a handler's level is
   respected (compared with the level for the message) when deciding
   whether to pass messages to that handler; otherwise, the behaviour
   is as in previous Python versions - to always pass each message to
   each handler.

   Alterado na versão 3.5: The "respect_handler_level" argument was
   added.

   Alterado na versão 3.14: "QueueListener" can now be used as a
   context manager via "with". When entering the context, the listener
   is started. When exiting the context, the listener is stopped.
   "__enter__()" returns the "QueueListener" object.

   dequeue(block)

      Dequeues a record and return it, optionally blocking.

      The base implementation uses "get()". You may want to override
      this method if you want to use timeouts or work with custom
      queue implementations.

   prepare(record)

      Prepare a record for handling.

      This implementation just returns the passed-in record. You may
      want to override this method if you need to do any custom
      marshalling or manipulation of the record before passing it to
      the handlers.

   handle(record)

      Handle a record.

      This just loops through the handlers offering them the record to
      handle. The actual object passed to the handlers is that which
      is returned from "prepare()".

   start()

      Starts the listener.

      This starts up a background thread to monitor the queue for
      LogRecords to process.

      Alterado na versão 3.14: Raises "RuntimeError" if called and the
      listener is already running.

   stop()

      Stops the listener.

      This asks the thread to terminate, and then waits for it to do
      so. Note that if you don't call this before your application
      exits, there may be some records still left on the queue, which
      won't be processed.

   enqueue_sentinel()

      Writes a sentinel to the queue to tell the listener to quit.
      This implementation uses "put_nowait()".  You may want to
      override this method if you want to use timeouts or work with
      custom queue implementations.

      Adicionado na versão 3.3.

Ver também:

  Módulo "logging"
     Referência da API para o módulo de logging.

  Módulo "logging.config"
     API de configuração para o módulo logging.
