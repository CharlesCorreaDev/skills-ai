"logging.config" --- Configuração do módulo logging
***************************************************

**Código-fonte:** Lib/logging/config.py


Important
^^^^^^^^^

Esta página contém apenas informações de referência. Para tutoriais,
por favor consulte

* Tutorial básico

* Tutorial avançado

* Livro de receitas do logging

======================================================================

Esta seção descreve a API para configuração do módulo logging.


Funções de configuração
=======================

As funções a seguir configuram o módulo logging. Elas estão
localizadas no módulo "logging.config". Seu uso é opcional --- você
pode configurar o módulo logging usando essas funções ou fazendo
chamadas para a API principal (definido no próprio "logging") e
definindo manipuladores que são declarados em "logging" ou em
"logging.handlers".

logging.config.dictConfig(config)

   Obtém a configuração de logging de um dicionário. Os conteúdos
   desse dicionário estão descritos abaixo em Esquema do Dicionário de
   Configuração.

   Se um erro for encontrado durante a configuração, esta função
   levantará uma exceção "ValueError", "TypeError", "AttributeError"
   ou "ImportError" com uma mensagem adequadamente descritiva.  A
   seguir está uma lista (possivelmente incompleta) de condições que
   levantarão um erro:

   * Um "level" que não seja uma string ou que seja uma string que não
     corresponda a um nível de logging atual

   * Um valor "propagate" que não seja um booleano.

   * Um id que não tenha um destino correspondente.

   * Um id de manipulador inexistente encontrado durante uma chamada
     incremental.

   * Um nome de logger inválido.

   * Incapacidade de resolver para um objeto interno ou externo.

   A análise é realizada pela classe "DictConfigurator", cujo
   construtor recebe o dicionário usado para a configuração e possui
   um método "configure()". O módulo "logging.config" tem um atributo
   chamável "dictConfigClass" que é inicialmente definido como
   "DictConfigurator". Você pode substituir o valor de
   "dictConfigClass" por uma implementação adequada de sua autoria.

   A função "dictConfig()" chama "dictConfigClass" passando o
   dicionário especificado e, em seguida, chama o método "configure()"
   no objeto devolvido para colocar a configuração em efeito:

      def dictConfig(config):
          dictConfigClass(config).configure()

   Por exemplo, uma subclasse de "DictConfigurator" poderia chamar
   "DictConfigurator.__init__()" no seu próprio "__init__()", em
   seguida, configurar prefixos personalizados que seriam utilizáveis
   na chamada "configure()" subsequente.  "dictConfigClass" seria
   ligado a esta nova subclasse, e então "dictConfig()" poderia ser
   chamado exatamente como no estado padrão, sem personalização.

   Adicionado na versão 3.2.

logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True, encoding=None)

   Lê a configuração de logging de um arquivo no formato
   "configparser". O formato do arquivo deve ser como descrito em
   Formato do arquivo de configuração. Esta função pode ser chamada
   várias vezes a partir de uma aplicação, permitindo que um usuário
   final selecione entre várias configurações pré-prontas (se o
   desenvolvedor fornecer um mecanismo para apresentar as escolhas e
   carregar a configuração escolhida).

   A função levantará uma exceção "FileNotFoundError" se o arquivo não
   existir e "RuntimeError" se o arquivo for inválido ou vazio.

   Parâmetros:
      * **fname** -- Um nome de arquivo, ou um objeto arquivo, ou uma
        instância derivada de "RawConfigParser". Se uma instância
        derivada de "RawConfigParser" for passada, ela é usada como
        está. Caso contrário, uma instância de "ConfigParser" é
        criada, e a configuração é lida por ela a partir do objeto
        passado em "fname". Se esse objeto tiver um método
        "readline()", ele é presumido como um objeto arquivo ou
        similar e lido usando "read_file()"; caso contrário, é
        presumido como um nome de arquivo e passado para "read()".

      * **defaults** -- Os defaults a serem passados para o
        "ConfigParser" podem ser especificados nesse argumento.

      * **disable_existing_loggers** -- Se especificado como "False",
        os loggers que existem quando esta chamada é feita são
        deixados habilitados. O padrão é "True" porque isso habilita o
        comportamento antigo de forma retrocompatível. Este
        comportamento é para desabilitar quaisquer loggers não-raiz
        existentes, a menos que eles ou seus ancestrais sejam
        explicitamente nomeados na configuração de logging.

      * **encoding** -- A codificação usada para abrir o arquivo
        quando fname é um nome de arquivo.

   Alterado na versão 3.4: Uma instância de uma subclasse de
   "RawConfigParser" agora é aceita como um valor para "fname". Isso
   facilita:

      * Uso de um arquivo de configuração onde a configuração de
        logging é apenas parte da configuração geral da aplicação.

      * Uso de uma configuração lida de um arquivo, e então modificada
        pela aplicação que a usa (por exemplo, baseada em parâmetros
        de linha de comando ou outros aspectos do ambiente de tempo de
        execução) antes de ser passada para "fileConfig".

   Alterado na versão 3.10: Adicionado o parâmetro encoding.

   Alterado na versão 3.12: Uma exceção será levantada se o arquivo
   fornecido não existir ou for inválido ou for vazio.

logging.config.listen(port=DEFAULT_LOGGING_CONFIG_PORT, verify=None)

   Inicia um servidor soquete na porta especificada e escuta por novas
   configurações. Se nenhuma porta for especificada, o padrão do
   módulo "DEFAULT_LOGGING_CONFIG_PORT" é usado. As configurações de
   logging serão enviadas como um arquivo adequado para processamento
   por "dictConfig()" ou por "fileConfig()". Retorna uma instância de
   "Thread" na qual você pode chamar "start()" para iniciar o
   servidor, e à qual você pode "join()" quando apropriado. Para
   interromper o servidor, chame "stopListening()".

   O argumento "verify", se especificado, deve ser um chamável que
   verifique se os bytes recebidos através do soquete são válidos e
   devem ser processados. Isso pode ser feito criptografando e/ou
   assinando o que é enviado através do soquete, de modo que o
   chamável "verify" possa realizar a verificação de assinatura e/ou a
   descriptografia. O chamável "verify" é chamado com um único
   argumento – os bytes recebidos através do soquete – e deve retornar
   os bytes a serem processados, ou "None" para indicar que os bytes
   devem ser descartados. Os bytes devolvidos podem ser os mesmos que
   os bytes passados (por exemplo, quando apenas a verificação é
   feita), ou podem ser completamente diferentes (talvez se a
   descriptografia for realizada).

   Para enviar uma configuração para o soquete, leia o arquivo de
   configuração e o envie para o soquete como uma sequência de bytes
   precedida por uma string de comprimento de quatro bytes empacotada
   em binário usando "struct.pack('>L', n)".

   Nota:

     Como partes da configuração são passadas por "eval()", o uso
     dessa função pode expor seus usuários a um risco de segurança.
     Embora a função apenas se vincule a um soquete em "localhost" e,
     portanto, não aceite conexões de máquinas remotas, existem
     cenários em que código não confiável pode ser executado sob a
     conta do processo que chama "listen()". Especificamente, se o
     processo que chama "listen()" estiver sendo executado em uma
     máquina multiusuário onde os usuários não confiam uns nos outros,
     um usuário malicioso pode conseguir executar essencialmente
     código arbitrário no processo de um usuário vítima, simplesmente
     conectando-se ao soquete "listen()" da vítima e enviando uma
     configuração que execute qualquer código que o atacante queira
     que seja executado no processo da vítima. Isso é especialmente
     fácil de fazer se a porta padrão for usada, mas não é difícil
     mesmo se uma porta diferente for utilizada. Para evitar o risco
     de isso acontecer, use o argumento "verify" de "listen()" para
     prevenir que configurações não reconhecidas sejam aplicadas.

   Alterado na versão 3.4: O argumento "verify" foi adicionado.

   Nota:

     Se você deseja enviar configurações para o listener que não
     desabilitem os loggers existentes, você precisará usar um formato
     JSON para a configuração, que usará "dictConfig()" para
     configuração. Este método permite que você especifique
     "disable_existing_loggers" como "False" na configuração que você
     envia.

logging.config.stopListening()

   Interrompe o servidor de escuta que foi criado com uma chamada para
   "listen()". Essa função é tipicamente chamada antes de chamar
   "join()" no valor de retorno de "listen()".


Considerações de segurança
==========================

A funcionalidade de configuração de logging tenta oferecer
conveniência, e em parte isso é feito ao oferecer a capacidade de
converter texto presente em arquivos de configuração em objetos Python
usados na configuração de logging — por exemplo, conforme descrito em
Objetos definidos pelo usuário. No entanto, esses mesmos mecanismos
(importar chamáveis de módulos definidos pelo usuário e chamá-los com
parâmetros da configuração) poderiam ser usados para invocar qualquer
código que você desejar, e por essa razão você deve tratar arquivos de
configuração de fontes não confiáveis com extrema cautela e
certificar-se de que nada de ruim pode acontecer se você carregá-los,
antes de realmente carregá-los.


Esquema do Dicionário de Configuração
=====================================

Descrever uma configuração de logging requer listar os vários objetos
a serem criados e as conexões entre eles; por exemplo, você pode criar
um manipulador nomeado 'console' e, em seguida, dizer que o logger
nomeado 'startup' enviará suas mensagens para o manipulador 'console'.
Estes objetos não se limitam àqueles fornecidos pelo módulo "logging",
pois você pode escrever sua própria classe de formatador ou de
manipulador. Os parâmetros para essas classes também podem precisar
incluir objetos externos, como "sys.stderr".  A sintaxe para descrever
esses objetos e conexões é definida abaixo em Conexões de objeto.


Detalhes do Esquema de Dicionário
---------------------------------

O dicionário passado para "dictConfig()" deve conter as chaves a
seguir:

* version - deve ser definido como um valor inteiro representando a
  versão do esquema. O único valor válido atualmente é 1, mas ter esta
  chave permite que o esquema evolua, preservando ainda a
  retrocompatibilidade.

Todas as outras chaves são opcionais, mas se estiverem presentes,
serão interpretadas conforme descrito abaixo. Em todos os casos abaixo
onde um 'dicionário de configuração' é mencionado, ele será verificado
quanto à chave especial "'()'" para consultar se uma instanciação
personalizada é necessária. Se for o caso, o mecanismo descrito em
Objetos definidos pelo usuário abaixo é usado para criar uma
instância; caso contrário, o contexto é usado para determinar o que
instanciar.

* formatters - o valor correspondente será um dicionário em que cada
  chave é um id de formatador e cada valor é um dicionário que
  descreve como configurar a instância correspondente de "Formatter".

  O dicionário de configuração é buscado pelas chaves opcionais a
  seguir que correspondem aos argumentos passados para criar um objeto
  "Formatter":

  * "format"

  * "datefmt"

  * "style"

  * "validate" (desde a versão >=3.8)

  * "defaults" (desde versão >=3.12)

  Uma chave opcional "class" indica o nome da classe do formatador
  (como um módulo pontilhado e nome da classe).  Os argumentos de
  instanciação são os mesmos que para "Formatter" portanto, esta chave
  é mais útil para instanciar uma subclasse personalizada de
  :"Formatter".  Por exemplo, a classe alternativa pode apresentar
  tracebacks de exceção em um formato expandido ou condensado. Se o
  seu formatter exigir chaves de configuração diferentes ou extras,
  você deve usar Objetos definidos pelo usuário.

* filters - o valor correspondente será um dicionário no qual cada
  chave é um id de filter e cada valor é um dicionário que descreve
  como configurar a instância Filter correspondente.

  O dicionário de configuração é pesquisado pela chave "name" (que
  assume como padrão a string vazia) e esta é usada para construir uma
  instância de "logging.Filter".

* handlers - o valor correspondente será um dicionário no qual cada
  chave é um id de manipulador e cada valor é um dicionário que
  descreve como configurar a instância de Manipulador correspondente.

  O dicionário de configuração é pesquisado para as chaves a seguir:

  * "class" (obrigatório). Esse é o nome qualificado completo da
    classe do handler.

  * "level" (opcional).  O nível do manipulador.

  * "formatter" (opcional).  O id do formatador para esse manipulador.

  * "filters" (opcional).  Uma lista de ids dos filtros para esse
    manipulador.

    Alterado na versão 3.11: "filters" podem receber instâncias de
    filtro além de ids.

  Todas as *outras* chaves são transmitidas como argumento nomeado
  para o construtor do manipulador.  Por exemplo, dado o trecho:

     handlers:
       console:
         class : logging.StreamHandler
         formatter: brief
         level   : INFO
         filters: [allow_foo]
         stream  : ext://sys.stdout
       file:
         class : logging.handlers.RotatingFileHandler
         formatter: precise
         filename: logconfig.log
         maxBytes: 1024
         backupCount: 3

  o manipulador com o id "console" é instanciado como um
  "logging.StreamHandler", usando "sys.stdout" como o fluxo
  subjacente. O manipulador com o id "file" é instanciado como um
  "logging.handlers.RotatingFileHandler" com os argumentos nomeados
  "filename='logconfig.log', maxBytes=1024, backupCount=3".

* *loggers*  -  o valor correspondente será um dicionário no qual cada
  chave é o nome de um registradores e cada valor é um dicionário que
  descreve como configurar a instância de Registrador correspondente.

  O dicionário de configuração é pesquisado para as chaves a seguir:

  * "level" (opcional).  O nível do logger.

  * "propagate" (opcional).  A configuração de propagação do logger.

  * "filters" (opcional).  Uma lista de ids dos filtros para esse
    logger.

    Alterado na versão 3.11: "filters" podem receber instâncias de
    filtro além de ids.

  * "handlers" (opcional).  Uma lista de ids dos manipuladores para
    esse logger.

  Os loggers especificados serão configurados de acordo com o nível, a
  propagação, os filtros e os manipuladores especificados.

* *root* - essa será a configuração para o logger raiz. O
  processamento da configuração será igual ao de qualquer logger,
  exceto pelo fato de que a configuração "propagate" não será
  aplicável.

* *incremental* - se a configuração deve ser interpretada como
  incremental à configuração existente.  O padrão deste valor é
  "False", o que significa que a configuração especificada substitui a
  configuração existente com a mesma semântica usada pela configuração
  da API existente "fileConfig()".

  Se o valor especificado for "True", a configuração será processada
  conforme descrito na seção Configuração Incremental.

* *disable_existing_loggers* - se quaisquer loggers não raiz
  existentes devem ser desabilitados. Essa configuração reflete o
  parâmetro de mesmo nome em "fileConfig()". Se ausente, o padrão
  deste parâmetro é "True". Este valor é ignorado se *incremental* for
  "True".


Configuração Incremental
------------------------

É difícil oferecer total flexibilidade para a configuração
incremental.  Por exemplo, como objetos, assim como filtros e
formatadores, são anônimos, depois que uma configuração é definida,
não é possível fazer referência a esse objeto anônimo ao ampliar uma
configuração.

Além disso, não há um argumento convincente para alterar
arbitrariamente o grafo de objetos de loggers, manipuladores, filtros
e formatadores em tempo de execução, depois que uma configuração é
definida; a verbosidade de loggers e manipuladores pode ser controlada
simplesmente ajustando os níveis (e, no caso de loggers, os
sinalizadores de propagação). Alterar o grafo de objetos
arbitrariamente de forma segura é problemático em um ambiente
multithread; embora não seja impossível, os benefícios não compensam a
complexidade que isso acrescentaria à implementação.

Assim, quando a chave "incremental" de um dicionário de configuração
estiver presente e for "True", o sistema ignorará completamente
quaisquer entradas "formatters" e "filters", e processará apenas as
configurações de "level" nas entradas "handlers", e as configurações
de "level" e "propagate" nas entradas "loggers" e "root".

Usar um valor no dicionário de configuração permite que configurações
sejam enviadas pela rede como dicionários pickled para um listener
soquete. Assim, a verbosidade de logging de uma aplicação de longa
execução pode ser alterada ao longo do tempo sem a necessidade de
parar e reiniciar a aplicação.


Conexões de objeto
------------------

O esquema descreve um conjunto de objetos de logging — loggers,
manipuladores, formatadores, filtros — que são conectados uns aos
outros em um grafo de objetos. Assim, o esquema precisa representar
conexões entre os objetos. Por exemplo, suponha que, após configurado,
um determinado logger tenha anexado a si um determinado manipulador.
Para os propósitos desta discussão, podemos dizer que o logger
representa a origem e o manipulador representa o destino de uma
conexão entre os dois. É claro que, nos objetos configurados, isso é
representado pelo logger mantendo uma referência ao manipulador. No
dicionário de configuração, isso é feito atribuindo a cada objeto de
destino um id que o identifica de forma inequívoca e, em seguida,
usando esse id na configuração do objeto de origem para indicar que
existe uma conexão entre o objeto de origem e o objeto de destino com
aquele id.

Então, por exemplo, considere o seguinte trecho de YAML:

   formatters:
     brief:
       # configuration for formatter with id 'brief' goes here
     precise:
       # configuration for formatter with id 'precise' goes here
   handlers:
     h1: #This is an id
      # configuration of handler with id 'h1' goes here
      formatter: brief
     h2: #This is another id
      # configuration of handler with id 'h2' goes here
      formatter: precise
   loggers:
     foo.bar.baz:
       # other configuration for logger 'foo.bar.baz'
       handlers: [h1, h2]

(Observação: o YAML é usado aqui porque é um pouco mais legível do que
o formulário de origem Python equivalente para o dicionário.)

Os ids para loggers são os nomes dos loggers que seriam usados
programaticamente para obter uma referência a esses loggers, por
exemplo, "foo.bar.baz". Os ids para Formatadores e Filtros podem ser
qualquer valor de string (como "brief", "precise" acima) e são
transitórios, no sentido de que só têm significado durante o
processamento do dicionário de configuração e são usados para
determinar conexões entre objetos, não sendo persistidos em nenhum
lugar após a conclusão da chamada de configuração.

O trecho acima indica que o logger nomeado "foo.bar.baz" deve ter dois
manipuladores anexados a ele, que são descritos pelos IDs de
manipulador "h1" e "h2". O formatador para "h1" é o descrito pelo id
"brief", e o formatador para "h2" é o descrito pelo id "precise".


Objetos definidos pelo usuário
------------------------------

O esquema oferece suporte a objetos definidos pelo usuário para
manipuladores, filtros e formatadores.  (Os loggers não precisam ter
tipos diferentes para instâncias diferentes, portanto este esquema de
configuração não provê suporte às classes de loggers definidas pelo
usuário.)

Objetos a serem configurados são descritos por dicionários que
detalham sua configuração. Em alguns casos, o sistema de logging
consegue inferir pelo contexto como um objeto deve ser instanciado,
mas, quando se trata de um objeto definido pelo usuário, o sistema não
saberá como fazer isso. Para oferecer total flexibilidade na
instanciação desses objetos definidos pelo usuário, é necessário
fornecer uma factory — um chamável que recebe um dicionário de
configuração e retorna o objeto instanciado. Isso é sinalizado por um
caminho de importação absoluto para a factory, disponibilizado sob a
chave especial "'()'". Aqui está um exemplo concreto:

   formatters:
     brief:
       format: '%(message)s'
     default:
       format: '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
       datefmt: '%Y-%m-%d %H:%M:%S'
     custom:
         (): my.package.customFormatterFactory
         bar: baz
         spam: 99.9
         answer: 42

O trecho YAML acima define três formatadores. O primeiro, com id
"brief", é uma instância padrão de "logging.Formatter" com a string de
formato especificado. O segundo, com id "default", tem um formato mais
longo e também define explicitamente o formato de tempo, e resultará
em um "logging.Formatter" inicializado com essas duas strings de
formatação. Em código-fonte Python, os formatadores "brief" e
"default" têm subdicionários de configuração:

   {
     'format' : '%(message)s'
   }

e:

   {
     'format' : '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
     'datefmt' : '%Y-%m-%d %H:%M:%S'
   }

respectivamente; e como esses dicionários não contêm a chave especial
"'()'", a instanciação é inferida pelo contexto. Como resultado, são
criadas instâncias padrão de "logging.Formatter". O subdicionário de
configuração do terceiro formatador, com o id "custom", é:

   {
     '()' : 'my.package.customFormatterFactory',
     'bar' : 'baz',
     'spam' : 99.9,
     'answer' : 42
   }

e isso contém a chave especial "'()'", o que significa que se deseja
uma instanciação definida pelo usuário. Nesse caso, a função factory
especificada será usada. Se for um chamável real, ele será usado
diretamente — caso contrário, se você especificar uma string (como no
exemplo), o chamável real será localizado usando os mecanismos normais
de importação. O callable será chamado com os itens restantes no
subdicionário de configuração como argumentos nomeados. No exemplo
acima, assume-se que o formatter com id "custom" seja retornado pela
chamada:

   my.package.customFormatterFactory(bar='baz', spam=99.9, answer=42)

Aviso:

  Os valores de chaves como "bar", "spam" e "answer" no exemplo acima
  não devem ser dicionários de configuração nem referências como
  "cfg://foo", ou "ext://bar" porque eles não serão processados pelo
  maquinário de configuração — serão simplesmente passados para a
  função callable como estão.

A chave "'()'" foi usada como chave especial porque não é um nome
válido de parâmetro nomeado e, portanto, não conflita com os nomes dos
argumentos nomeados usados na chamada. O "'()'" também serve como um
mnemônico de que o valor correspondente é um chamável.

Alterado na versão 3.11: O membro "filters" de "handlers" e "loggers"
pode receber instâncias de filtro, além de ids.

Você também pode especificar uma chave especial "'.'" cujo valor é um
mapeamento de nomes de atributos para valores. Se essa chave for
encontrada, os atributos especificados serão definidos no objeto
definido pelo usuário antes que ele seja retornado. Assim, com a
seguinte configuração:

   {
     '()' : 'my.package.customFormatterFactory',
     'bar' : 'baz',
     'spam' : 99.9,
     'answer' : 42,
     '.' : {
       'foo': 'bar',
       'baz': 'bozz'
     }
   }

o formatador retornado terá o atributo "foo" definido como "'bar'" e o
atributo "baz" definido como "'bozz'".

Aviso:

  Os valores de atributos como "foo" e "baz" no exemplo acima não
  devem ser dicionários de configuração nem referências como
  "cfg://foo" ou "ext://bar" porque eles não serão processados pelo
  maquinário de configuração, mas definidos como valores de atributo
  exatamente como foram fornecidos.


Ordem de configuração de manipuladores
--------------------------------------

Os manipuladores são configurados em ordem alfabética de suas chaves,
e um manipulador configurado substitui o dicionário de configuração no
(cópia de trabalho do) dicionário "handlers" no esquema. Se você usar
uma construção como "cfg://handlers.foo", então inicialmente
"handlers['foo']" aponta para o dicionário de configuração do
manipulador nomeado "foo" e, posteriormente (quando esse manipulador
tiver sido configurado), passa a apontar para a instância configurada
do manipulador. Assim, "cfg://handlers.foo" pode ser resolvido tanto
como um dicionário quanto como uma instância de manipulador. Em geral,
é prudente nomear os manipuladores de modo que os manipuladores
dependentes sejam configurados depois de quaisquer manipuladores dos
quais dependam; isso permite que algo como "cfg://handlers.foo" seja
usado na configuração de um manipulador que depende do handler "foo".
Se esse manipulador dependente fosse nomeado "bar", surgiriam
problemas, pois a configuração de "bar" seria tentada antes da de
"foo", e "foo" ainda não teria sido configurado. No entanto, se o
manipulador dependente fosse nomeado "foobar", ele seria configurado
após "foo", com o resultado de que "cfg://handlers.foo" seria
resolvido para o manipulador "foo" configurado, e não para o seu
dicionário de configuração.


Acesso a objetos externos
-------------------------

Há momentos em que uma configuração precisa se referir a objetos
externos à configuração, por exemplo "sys.stderr". Se o dicionário de
configuração for construído usando código Python, isso é simples, mas
surge um problema quando a configuração é fornecida por meio de um
arquivo texto (por exemplo, JSON, YAML). Em um arquivo texto, não há
uma forma padrão de distinguir "sys.stderr" da string literal
"'sys.stderr'".  Para facilitar essa distinção, o sistema de
configuração procura por determinados prefixos especiais em valores de
string e os trata de forma especial. Por exemplo, se a string literal
"'ext://sys.stderr'" for fornecida como um valor na configuração,
então o prefixo "ext://" será removido e o restante do valor será
processado usando os mecanismos normais de importação.

O tratamento desses prefixos é feito de forma análoga ao tratamento de
protocolos: existe um mecanismo genérico para procurar prefixos que
correspondam à expressão regular ^(?P<prefix>[a-z]+)://(?P<suffix>.*),
de modo que, se o "prefix" for reconhecido, o "suffix" é processado de
uma forma dependente do prefixo e o resultado desse processamento
substitui o valor da string. Se o prefixo não for reconhecido, então o
valor da string é mantido como está.


Acesso a objetos internos
-------------------------

Além de objetos externos, às vezes também é necessário fazer
referência a objetos na configuração. Isso será feito de forma
implícita pelo sistema de configuração para coisas que ele conhece.
Por exemplo, o valor em forma de string "'DEBUG'" para um "level" em
um logger ou manipulador será automaticamente convertido para o valor
"logging.DEBUG", e as entradas "handlers", "filters" e "formatter"
receberão um identificador de objeto e o resolverão para o objeto de
destino apropriado.

No entanto, é necessário um mecanismo mais genérico para objetos
definidos pelo usuário que não são conhecidos pelo módulo "logging".
Por exemplo, considere "logging.handlers.MemoryHandler", que recebe um
argumento "target" que é outro manipulador para o qual delegar. Como o
sistema já conhece essa classe, então, na configuração, o "target"
fornecido só precisa ser o id do objeto do manipulador de destino
relevante, e o sistema resolverá esse id para o manipulador
correspondente. Se, porém, um usuário definir um
"my.package.MyHandler" que tenha um manipulador "alternate", o sistema
de configuração não saberia que "alternate" se refere a um
manipulador. Para atender a esse caso, um sistema genérico de
resolução permite que o usuário especifique:

   handlers:
     file:
       # configuration of file handler goes here

     custom:
       (): my.package.MyHandler
       alternate: cfg://handlers.file

A cadeia literal "'cfg://handlers.file'" será resolvida de maneira
análoga às strings com o prefixo "ext://" mas procurando na própria
configuração em vez do espaço de nomes de importação. O mecanismo
permite acesso por ponto ou por índice, de forma semelhante ao que é
fornecido por "str.format". Assim, dado o seguinte trecho:

   handlers:
     email:
       class: logging.handlers.SMTPHandler
       mailhost: localhost
       fromaddr: my_app@domain.tld
       toaddrs:
         - support_team@domain.tld
         - dev_team@domain.tld
       subject: Houston, we have a problem.

Na configuração, a string "'cfg://handlers'" seria resolvida para o
dicionário com a chave "handlers", a string "'cfg://handlers.email"
seria resolvida para o dicionário com a chave "email" dentro do
dicionário "handlers", e assim por diante. A string
"'cfg://handlers.email.toaddrs[1]" seria resolvida para
"'dev_team@domain.tld'" e a string "'cfg://handlers.email.toaddrs[0]'"
seria resolvida para o valor "'support_team@domain.tld'". O valor de
"subject" poderia ser acessado usando "'cfg://handlers.email.subject'"
ou, de forma equivalente, "'cfg://handlers.email[subject]'". Esta
última forma só precisa ser utilizada se a chave contiver espaços ou
caracteres não alfanuméricos. Observe que os caracteres "[" e "]" não
são permitidos nas chaves. Se um valor de índice consistir apenas em
dígitos decimais, o acesso será tentado usando o valor inteiro
correspondente, recorrendo ao valor de string caso necessário.

Dada uma string "cfg://handlers.myhandler.mykey.123", ela será
resolvida como "config_dict['handlers']['myhandler']['mykey']['123']".
Se a string for especificada como
"cfg://handlers.myhandler.mykey[123]", o sistema tentará obter o valor
de "config_dict['handlers']['myhandler']['mykey'][123]" e, caso isso
falhe, recorrerá a
"config_dict['handlers']['myhandler']['mykey']['123']".


Resolução de importações e importadores personalizados
------------------------------------------------------

Por padrão, a resolução de importação utiliza a função embutida
"__import__()" para realizar as importações. Caso deseje substituir
esse comportamento por seu próprio mecanismo de importação, você pode
alterar o atributo "importer" da classe "DictConfigurator" ou de sua
superclasse, "BaseConfigurator". No entanto, é preciso ter cuidado
devido à forma como funções são acessadas a partir de classes por meio
de descritores. Se você estiver utilizando um objeto chamável do
Python para realizar as importações e quiser defini-lo em nível de
classe, em vez de em nível de instância, deverá envolvê-lo com
"staticmethod()". Por exemplo:

   from importlib import import_module
   from logging.config import BaseConfigurator

   BaseConfigurator.importer = staticmethod(import_module)

Você não precisa envolver com "staticmethod()" se estiver definindo o
chamável de importação em uma *instância* do configurador.


Configurando QueueHandler e QueueListener
-----------------------------------------

Se você deseja configurar um "QueueHandler" — lembrando que ele é
normalmente utilizado em conjunto com um "QueueListener" —, pode
configurar ambos simultaneamente. Após a configuração, a instância do
"QueueListener" estará disponível como o atributo "listener" do
manipulador criado; este, por sua vez, poderá ser acessado utilizando
"getHandlerByName()" e passando o nome atribuído ao "QueueHandler" na
sua configuração. O esquema de dicionário para configurar o par é
apresentado no exemplo de trecho YAML abaixo.

   handlers:
     qhand:
       class: logging.handlers.QueueHandler
       queue: my.module.queue_factory
       listener: my.package.CustomListener
       handlers:
         - hand_name_1
         - hand_name_2
         ...

As chaves "queue" e "listener" são opcionais.

Se a chave "queue" estiver presente, o valor correspondente pode ser
um dos seguintes:

* Um objeto que implementa a API pública "Queue.put_nowait" e
  "Queue.get". Por exemplo, pode ser uma instância real de
  "queue.Queue" ou uma subclasse dela, ou um proxy obtido por meio de
  "multiprocessing.managers.SyncManager.Queue()".

  É claro que isso só é possível se você estiver construindo ou
  modificando o dicionário de configuração no código.

* Uma string que é resolvida para um chamável que, quando chamado sem
  argumentos, retorna a instância de fila a ser usada. Esse chamável
  pode ser uma subclasse de "queue.Queue" ou uma função que retorna
  uma instância de fila adequada, como "my.module.queue_factory()".

* Um dicionário com a chave "'()'" que é construído da forma usual
  discutida em Objetos definidos pelo usuário O resultado dessa
  construção deve ser uma instância de "queue.Queue".

Se a chave "queue" estiver ausente, uma instância padrão e não
limitada de "queue.Queue" será criada e usada.

Se a chave "listener" estiver presente, o valor correspondente pode
ser um dos seguintes:

* Uma subclasse de "logging.handlers.QueueListener". Isso,
  naturalmente, só é possível se você estiver construindo ou
  modificando o dicionário de configuração em código.

* Uma string que é resolvida para uma classe que seja uma subclasse de
  "QueueListener" como "'my.package.CustomListener'".

* Um dicionário com a chave "'()'", construído da maneira usual
  conforme discutido em Objetos definidos pelo usuário O resultado
  dessa construção deve ser um chamável com a mesma assinatura do
  inicializador de "QueueListener".

Se a chave "listener" estiver ausente, será usada
"logging.handlers.QueueListener".

Os valores sob a chave "handlers" são os nomes de outros manipuladores
na configuração (não mostrados no trecho acima) que serão passados ao
queue listener.

Quaisquer classes personalizadas de manipulador de filas e de listener
precisarão ser definidas com as mesmas assinaturas de inicialização
que "QueueHandler" e "QueueListener".

Adicionado na versão 3.12.


Formato do arquivo de configuração
==================================

O formato do arquivo de configuração reconhecido por "fileConfig()"
baseia-se na funcionalidade do módulo "configparser". O arquivo deve
conter seções chamadas "[loggers]", "[handlers]" e "[formatters]", que
identificam pelo nome as entidades de cada tipo definidas no arquivo.
Para cada uma dessas entidades, existe uma seção separada que
especifica como a entidade está configurada. Assim, para um logger
chamado "log01" na seção "[loggers]", os detalhes de configuração
relevantes são mantidos em uma seção "[logger_log01]". Da mesma forma,
um handler chamado "hand01" na seção "[handlers]" terá sua
configuração mantida em uma seção chamada "[handler_hand01]", enquanto
um formatador chamado "form01" na seção "[formatters]" terá sua
configuração especificada em uma seção chamada "[formatter_form01]". A
configuração do logger raiz deve ser especificada em uma seção chamada
"[logger_root]".

Nota:

  A API "fileConfig()" é mais antiga que a API "dictConfig()" e não
  oferece funcionalidade para cobrir certos aspectos do registro de
  logs (*logging*). Por exemplo, não é possível configurar objetos
  "Filter" — que permitem filtrar mensagens além dos simples níveis
  numéricos (inteiros) — utilizando a "fileConfig()". Se você precisar
  de instâncias de "Filter" em sua configuração de log, deverá
  utilizar a "dictConfig()". Vale ressaltar que futuros aprimoramentos
  nas funcionalidades de configuração serão incorporados à
  "dictConfig()"; portanto, considere migrar para essa API mais
  recente quando for conveniente.

Exemplos dessas seções no arquivo são fornecidos abaixo.

   [loggers]
   keys=root,log02,log03,log04,log05,log06,log07

   [handlers]
   keys=hand01,hand02,hand03,hand04,hand05,hand06,hand07,hand08,hand09

   [formatters]
   keys=form01,form02,form03,form04,form05,form06,form07,form08,form09

O logger raiz deve especificar um nível e uma lista de manipuladores.
Um exemplo de seção de logger raiz é dado abaixo.

   [logger_root]
   level=NOTSET
   handlers=hand01

A entrada "level" pode ser "DEBUG, INFO, WARNING, ERROR, CRITICAL" ou
"NOTSET". Apenas para o logger raiz, "NOTSET" significa que todas as
mensagens serão registradas. Os valores de nível são avaliados no
contexto do espaço de nomes do pacote "logging".

A entrada "handlers" é uma lista separada por vírgulas com os nomes
dos manipuladores, que devem aparecer na seção "[handlers]". Esses
nomes precisam aparecer na seção "[handlers]" e ter seções
correspondentes no arquivo de configuração.

Para loggers que não sejam o logger raiz, são necessárias algumas
informações adicionais. Isso é ilustrado pelo exemplo a seguir.

   [logger_parser]
   level=DEBUG
   handlers=hand01
   propagate=1
   qualname=compiler.parser

As entradas "level" e "handlers" são interpretadas da mesma forma que
o logger raiz, exceto que, se o nível de um logger não raiz for
especificado como "NOTSET", o sistema consulta os loggers situados
acima na hierarquia para determinar o nível efetivo do logger. O item
"propagate" é definido como 1 para indicar que as mensagens devem ser
propagadas para os manipuladores acima na hierarquia de loggers a
partir deste logger, ou 0 para indicar que as mensagens não são
propagadas para manipuladores acima na hierarquia. O item "qualname" é
o nome de canal hierárquico do logger, ou seja, o nome usado pela
aplicação para obter o logger.

As seções que especificam a configuração de manipuladores são
exemplificadas pelo seguinte.

   [handler_hand01]
   class=StreamHandler
   level=NOTSET
   formatter=form01
   args=(sys.stdout,)

A entrada "class" indica a classe do manipulador (conforme determinada
por "eval()" no espaço de nomes do pacote "logging"). O "level" é
interpretado da mesma forma que para loggers, e "NOTSET" é entendido
como “registrar tudo”.

A entrada "formatter" indica o nome da chave do formatador para esse
manipulador. Se estiver em branco, um formatador padrão
("logging._defaultFormatter") será usado. Se um nome for especificado,
ele deve aparecer na seção "[formatters]" e ter uma seção
correspondente no arquivo de configuração.

A entrada "args", quando avaliada no contexto do espaço de nomes do
pacote "logging", é a lista de argumentos para o construtor da classe
de manipulador (*handler*). Consulte os construtores dos manipuladores
relevantes, ou os exemplos abaixo, para ver como as entradas típicas
são construídas. Se não for fornecida, o padrão é "()".

A entrada opcional "kwargs", quando avaliada no contexto do espaço de
nomes do pacote "logging", é o dicionário de argumentos nomeados para
o construtor da classe de manipulador (*handler*). Se não for
fornecida, o padrão é "{}".

   [handler_hand02]
   class=FileHandler
   level=DEBUG
   formatter=form02
   args=('python.log', 'w')

   [handler_hand03]
   class=handlers.SocketHandler
   level=INFO
   formatter=form03
   args=('localhost', handlers.DEFAULT_TCP_LOGGING_PORT)

   [handler_hand04]
   class=handlers.DatagramHandler
   level=WARN
   formatter=form04
   args=('localhost', handlers.DEFAULT_UDP_LOGGING_PORT)

   [handler_hand05]
   class=handlers.SysLogHandler
   level=ERROR
   formatter=form05
   args=(('localhost', handlers.SYSLOG_UDP_PORT), handlers.SysLogHandler.LOG_USER)

   [handler_hand06]
   class=handlers.NTEventLogHandler
   level=CRITICAL
   formatter=form06
   args=('Python Application', '', 'Application')

   [handler_hand07]
   class=handlers.SMTPHandler
   level=WARN
   formatter=form07
   args=('localhost', 'from@abc', ['user1@abc', 'user2@xyz'], 'Logger Subject')
   kwargs={'timeout': 10.0}

   [handler_hand08]
   class=handlers.MemoryHandler
   level=NOTSET
   formatter=form08
   target=
   args=(10, ERROR)

   [handler_hand09]
   class=handlers.HTTPHandler
   level=NOTSET
   formatter=form09
   args=('localhost:9022', '/log', 'GET')
   kwargs={'secure': True}

As seções que especificam a configuração do formatador são
caracterizadas pelo seguinte.

   [formatter_form01]
   format=F1 %(asctime)s %(levelname)s %(message)s %(customfield)s
   datefmt=
   style=%
   validate=True
   defaults={'customfield': 'defaultvalue'}
   class=logging.Formatter

Os argumentos para a configuração do formatador são os mesmos que as
chaves no esquema do dicionário da seção de formatadores.

A entrada "defaults", quando avaliada no contexto do espaço de nomes
do pacote "logging", é um dicionário de valores padrão para campos de
formatação personalizados. Se não for fornecida, o padrão é "None".

Nota:

  Devido ao uso de "eval()" conforme descrito acima, há riscos de
  segurança potenciais decorrentes do uso de "listen()" para enviar e
  receber configurações por meio de soquetes. Os riscos se limitam a
  situações em que vários usuários sem confiança mútua executam código
  na mesma máquina; consulte a documentação de "listen()" para mais
  informações.

Ver também:

  Módulo "logging"
     Referência da API para o módulo de logging.

  Módulo "logging.handlers"
     Manipuladores úteis incluídos no módulo logging.
