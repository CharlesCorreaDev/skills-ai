7. Usando Python no iOS
***********************

Autores:
   Russell Keith-Magee (2024-03)

Python no iOS é diferente do Python em plataformas de desktop. Em uma
plataforma desktop, o Python geralmente é instalado como um recurso do
sistema que pode ser usado por qualquer usuário daquele computador. Os
usuários então interagem com o Python executando um executável
**python** e inserindo comandos em um prompt interativo ou executando
um script Python.

No iOS, não existe o conceito de instalação como recurso do sistema. A
única unidade de distribuição de software é uma aplicação, ou "app".
Também não há console onde você possa executar um executável
**python** ou interagir com um REPL do Python.

Como resultado, a única maneira de usar Python no iOS é no modo
incorporado -- ou seja, escrevendo uma aplicação iOS nativo e
incorporando um interpretador Python usando "libPython" e invocando o
código Python usando API de incorporação do Python. O interpretador
Python completo, a biblioteca padrão e todo o seu código Python são
então empacotados como um pacote independente que pode ser distribuído
pela iOS App Store.

Se você deseja experimentar pela primeira vez escrever uma aplicação
iOS em Python, projetos como BeeWare, Kivy e Flet irão fornecer uma
experiência de usuário muito mais acessível. Esses projetos gerenciam
as complexidades associadas à execução de um projeto iOS, portanto,
você só precisa lidar com o próprio código Python.


7.1. Python em tempo de execução no iOS
=======================================


7.1.1. Compatibilidade com a versão do iOS
------------------------------------------

A versão mínima suportada do iOS é especificada em tempo de
compilação, usando a opção "--host" do "configure". Por padrão, quando
compilado para iOS, Python será compilado com uma versão iOS mínima
suportada de 13.0. Para usar uma versão mínima diferente do iOS,
forneça o número da versão como parte do argumento "--host" - por
exemplo, "--host=arm64-apple-ios15.4-simulator" compilaria um
simulador ARM64 construído com uma meta de implantação de 15.4.


7.1.2. Identificação da plataforma
----------------------------------

Ao executar no iOS, "sys.platform" reportará como "ios". Este valor
será retornado em um iPhone ou iPad, independentemente da aplicação
estar executando no simulador ou em um dispositivo físico.

Informações sobre o ambiente de execução específico, incluindo a
versão do iOS, modelo do dispositivo e se o dispositivo é um
simulador, podem ser obtidas usando "platform.ios_ver()".
"platform.system()" reportará "iOS" ou "iPadOS", dependendo do
dispositivo.

"os.uname()" reporta detalhes em nível de kernel; ele reportará o nome
"Darwin".


7.1.3. Disponibilidade da biblioteca padrão
-------------------------------------------

A biblioteca padrão do Python tem algumas omissões e restrições
notáveis no iOS. Consulte o guia de disponibilidade de API para iOS
para obter detalhes.


7.1.4. Módulos de extensão binária
----------------------------------

Uma diferença notável sobre o iOS como plataforma é que a distribuição
da App Store impõe requisitos rígidos ao empacotamento de uma
aplicação. Um desses requisitos rege como os módulos de extensão
binária são distribuídos.

A iOS App Store exige que *todos* os módulos binários em uma aplicação
iOS sejam bibliotecas dinâmicas, contidas em um framework com
metadados apropriados, armazenados na pasta "Frameworks" da aplicação
empacotada. Pode haver apenas um único binário por framework, e não
pode haver nenhum material binário executável fora da pasta
"Frameworks".

Isto entra em conflito com a abordagem usual do Python para
distribuição de binários, que permite que um módulo de extensão
binária seja carregado de qualquer local em "sys.path". Para garantir
a conformidade com as políticas da App Store, um projeto iOS deve pós-
processar quaisquer pacotes Python, convertendo módulos binários ".so"
em estruturas independentes individuais com metadados e assinatura
apropriados. Para obter detalhes sobre como realizar esse pós-
processamento, consulte o guia para adicionar Python ao seu projeto.

Para ajudar o Python a descobrir binários em seu novo local, o arquivo
".so" original em "sys.path" é substituído por um arquivo ".fwork".
Este arquivo é um arquivo texto que contém a localização do binário do
framework, relativo ao pacote de aplicações. Para permitir que o
framework retorne ao local original, o framework deve conter um
arquivo ".origin" que contém a localização do arquivo ".fwork",
relativo ao pacote da aplicação.

Por exemplo, considere o caso de uma importação "from foo.bar import
_whiz", onde "_whiz" é implementado com o módulo binário
"sources/foo/bar/_whiz.abi3.so", com "sources" sendo o local
registrado em "sys.path", relativo ao pacote da aplicação. Este módulo
*deve* ser distribuído como
"Frameworks/foo.bar._whiz.framework/foo.bar._whiz" (criando o nome do
framework a partir do caminho de importação completo do módulo), com
um arquivo "Info.plist" no diretório ".framework" identificando o
binário como um framework. O módulo "foo.bar._whiz" seria representado
no local original com um arquivo marcador
"sources/foo/bar/_whiz.abi3.fwork", contendo o caminho
"Frameworks/foo.bar._whiz/foo.bar._whiz". O framework também conteria
"Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin", contendo o
caminho para o arquivo ".fwork".

Ao executar no iOS, o interpretador Python instalará um
"AppleFrameworkLoader" que é capaz de ler e importar arquivos
".fwork". Uma vez importado, o atributo "__file__" do módulo binário
reportará como a localização do arquivo ".fwork". Entretanto, o
"ModuleSpec" para o módulo carregado reportará a "origin" como a
localização do binário na pasta do framework.


7.1.5. Binários stub do compilador
----------------------------------

O Xcode não expõe compiladores explícitos para iOS; em vez disso, ele
usa um script "xcrun" que resolve um caminho  do compilador (por
exemplo, "xcrun --sdk iphoneos clang" para obter o "clang" para um
dispositivo iPhone). No entanto, usar este script apresenta dois
problemas:

* A saída de "xcrun" inclui caminhos que são específicos da máquina,
  resultando em um módulo sysconfig que não pode ser compartilhado
  entre usuários; e

* Isso resulta em definições "CC"/"CPP"/"LD"/"AR" que incluem espaços.
  Existem muitas ferramentas do ecossistema C que pressupõem que você
  pode dividir uma linha de comando no primeiro espaço para obter o
  caminho para o executável do compilador; este não é o caso ao usar
  "xcrun".

Para evitar esses problemas, o Python forneceu stubs para essas
ferramentas. Esses stubs são wrappers de script de shell em torno das
ferramentas subjacentes "xcrun", distribuídos em uma pasta "bin"
distribuída junto com a estrutura iOS compilada. Esses scripts são
relocáveis e sempre serão resolvidos para os caminhos apropriados do
sistema local. Ao incluir esses scripts na pasta bin que acompanha um
framework, o conteúdo do módulo "sysconfig" se torna útil para
usuários finais compilarem seus próprios módulos. Ao compilar módulos
Python de terceiros para iOS, você deve garantir que esses binários
stub estejam no seu caminho.


7.2. Instalando Python no iOS
=============================


7.2.1. Ferramentas para construir aplicações de iOS
---------------------------------------------------

A construção para iOS requer o uso das ferramentas Xcode da Apple. É
altamente recomendável que você use a versão estável mais recente do
Xcode. Isso exigirá o uso da versão mais recente (ou segunda) do macOS
lançada recentemente, já que a Apple não mantém o Xcode para versões
mais antigas do macOS. As ferramentas de linha de comando do Xcode não
são suficientes para o desenvolvimento iOS; você precisa de uma
instalação *completa* do Xcode.

Se quiser executar seu código no simulador iOS, você também precisará
instalar um iOS Simulator Platform. Você deverá ser solicitado a
selecionar um iOS Simulator Platform ao executar o Xcode pela primeira
vez. Alternativamente, você pode adicionar um iOS Simulator Platform
selecionando na guia Platforms do painel Settings do Xcode.


7.2.2. Adicionando Python a um projeto iOS
------------------------------------------

Python pode ser adicionado a qualquer projeto iOS, usando Swift ou
Objective C. Os exemplos a seguir usarão Objective C; se você estiver
usando Swift, poderá achar uma biblioteca como PythonKit útil.

Para adicionar Python a um projeto Xcode de iOS:

1. Construa ou obtenha um "XCFramework" em Python. Veja as instruções
   em Platforms/Apple/iOS/README.md (na distribuição fonte do CPython)
   para detalhes sobre como construir um "XCFramework" em Python. No
   mínimo, você precisará de uma construção que tenha suporte "arm64
   -apple-ios", além de "arm64-apple-ios-simulator" ou "x86_64-apple-
   ios-simulator".

2. Arraste o "XCframework" para o seu projeto iOS. Nas instruções a
   seguir, presumiremos que você colocou o "XCframework" na raiz do
   seu projeto; no entanto, você pode usar qualquer outro local
   desejado ajustando os caminhos conforme necessário.

3. Adicione o código da sua aplicação como uma pasta no seu projeto
   Xcode. Nas instruções a seguir, presumiremos que seu código de
   usuário está em uma pasta chamada "app" na raiz do seu projeto;
   você pode usar qualquer outro local ajustando os caminhos conforme
   necessário. Certifique-se de que esta pasta esteja associada ao
   destino da sua aplicação.

4. Selecione o destino da aplicação selecionando o nó raiz do seu
   projeto Xcode e, em seguida, o nome do destino na barra lateral que
   aparece.

5. Nas configurações de "General", em "Frameworks, Libraries and
   Embedded Content", adicione "Python.xcframework", com "Embed &
   Sign" selecionado.

6. Na guia "Build Settings", modifique o seguinte:

   * Build Options

     * User Script Sandboxing: No

     * Enable Testability: Yes

   * Search Paths

     * Framework Search Paths: "$(PROJECT_DIR)"

     * Header Search Paths:
       ""$(BUILT_PRODUCTS_DIR)/Python.framework/Headers""

   * Apple Clang - Warnings - All languages

     * Quoted Include In Framework Header: No

7. Adicione uma etapa de construção que processa a biblioteca padrão
   do Python e suas dependências de binários Python. Na aba "Build
   Phases", adicione uma nova etapa de construção "Run Script" *antes*
   da etapa "Embed Frameworks", mas *depois* da etapa "Copy Bundle
   Resources". Nomeie a etapa como "Process Python libraries",
   desative a caixa de seleção "Based on dependency analysis" e defina
   o conteúdo do script como:

      set -e
      source $PROJECT_DIR/Python.xcframework/build/build_utils.sh
      install_python Python.xcframework app

   Se você colocou seu XCframework em algum lugar diferente da raiz do
   seu projeto, modifique o caminho para o primeiro argumento.

8. Adicione código Objective C para inicializar e usar um
   interpretador Python em modo embarcado. Você deve garantir que:

   * Modo UTF-8 ("PyPreConfig.utf8_mode") esteja habilitado;

   * Stdio buffered ("PyConfig.buffered_stdio") esteja desabilitado;

   * Escrita de bytecode ("PyConfig.write_bytecode") esteja
     desabilitada;

   * Manipuladores de sinais ("PyConfig.install_signal_handlers")
     estejam habilitados;

   * Registro de logs do sistema ("PyConfig.use_system_logger") esteja
     desabilitado (opcional, mas fortemente recomendado; isso está
     habilitado por padrão);

   * "PYTHONHOME" para o interpretador esteja configurado para apontar
     para a subpasta "python" do pacote da sua aplicação; e

   * O "PYTHONPATH" para o interpretador inclui:

     * a subpasta "python/lib/python3.X" do pacote da sua aplicação,

     * a subpasta "python/lib/python3.X/lib-dynload" do pacote da sua
       aplicação, e

     * a subpasta "app" do pacote da sua aplicação

   O local do pacote da sua aplicação pode ser determinada usando
   "[[NSBundle mainBundle] resourcePath]".

Os passos 7 e 8 destas instruções presumem que você tem uma única
pasta de código de aplicação Python puro, chamada "app". Se você tiver
módulos binários de terceiros em sua aplicação, serão necessárias
algumas etapas adicionais:

* Você precisa garantir que todas as pastas que contenham binários de
  terceiros sejam associadas ao destino da aplicação ou sejam
  explicitamente copiadas como parte da etapa 7. A etapa 7 também deve
  limpar quaisquer binários que não sejam apropriados para a
  plataforma que uma construção específica está direcionando (ou seja,
  exclua todos os binários do dispositivo se estiver criando uma
  aplicação direcionado ao simulador).

* Se você estiver usando uma pasta separada para pacotes de terceiros,
  certifique-se de que essa pasta seja adicionada ao final da chamada
  de "install_python" no passo 7 e que seja parte da configuração
  "PYTHONPATH" no passo 8.

* Se alguma das pastas que contêm pacotes de terceiros contiver
  arquivos ".pth", você deverá adicionar essa pasta como um *diretório
  de site* (usando "site.addsitedir()"), em vez de adicioná-la
  diretamente a "PYTHONPATH" ou "sys.path".


7.2.3. Testando um pacote Python
--------------------------------

A árvore de fontes do CPython contém um projeto de banco de testes que
é usado para executar o conjunto de testes do CPython no simulador do
iOS. Este banco de testes também pode ser usado como um projeto de
banco de testes para executar o conjunto de testes da sua biblioteca
Python no iOS.

Depois de criar ou obter um iOS XCFramework (consulte
Platforms/Apple/iOS/README.md para obter detalhes), crie um clone do
projeto de banco de testes de iOS do Python. Se você usou o script de
construção "Platforms/Apple" para construir o XCframework, você pode
executar:

   $ python cross-build/iOS/testbed clone --app <caminho/para/módulo1> --app <caminho/para/módulo2> app-testbed

Ou, se você tiver criado seu próprio XCframework, execute:

   $ python Platforms/Apple/testbed clone --platform iOS --framework <caminho/para/Python.xcframework> --app <caminho/para/módulo1> --app <caminho/para/módulo2> app-testbed

Todas as pastas especificadas com o sinalizador "--app" serão copiadas
para o projeto de banco de testes clonado. O banco de testes
resultante será criado na pasta "app-testbed". Neste exemplo,
"módulo1" e "módulo2" seriam módulos importáveis em tempo de execução.
Se seu projeto tiver dependências adicionais, elas podem ser
instaladas na pasta "app-testbed/Testbed/app_packages" (usando "pip
install --target app-testbed/Testbed/app_packages" ou similar).

Você pode então usar a pasta "app-testbed" para executar o conjunto de
testes para seu aplicativo. Por exemplo, se "módulo1.tests" fosse o
ponto de entrada para seu conjunto de testes, você poderia executar:

   $ python app-testbed run -- módulo1.tests

Isso é o equivalente a executar "python -m módulo1.tests" em uma
compilação Python de desktop. Quaisquer argumentos após "--" serão
passados para o banco de testes como se fossem argumentos para "python
-m" em uma máquina de desktop.

Você também pode abrir o projeto de teste no Xcode executando:

   $ open app-testbed/iOSTestbed.xcodeproj

Isso permitirá que você use o conjunto completo de ferramentas do
Xcode para depuração.

Os argumentos usados para executar o conjunto de testes são definidos
como parte do plano de teste. Para modificar o plano de teste,
selecione o nó do plano de teste na árvore do projeto (deve ser o
primeiro filho do nó raiz) e selecione a aba "Configurations".
Modifique o valor "Arguments Passed On Launch" para alterar os
argumentos de teste.

O plano de teste também desabilita os testes paralelos e especifica o
uso do arquivo "Testbed.lldbinit" para fornecer a configuração do
depurador. A configuração padrão do depurador desabilita pontos de
interrupção automáticos nos sinais "SIGINT", "SIGUSR1", "SIGUSR2" e
"SIGXFSZ".


7.3. Conformidade com a App Store
=================================

O único mecanismo para distribuir aplicações para dispositivos iOS de
terceiros é enviar a aplicação para a App Store do iOS; as aplicações
enviadas para distribuição devem passar pelo processo de revisão de
aplicações da Apple. Esse processo inclui um conjunto de regras de
validação automatizadas que inspecionam o pacote de aplicação enviado
em busca de código problemático. Há alguns passos que devem ser
seguidas para garantir que sua aplicação consiga passar por esses
passos de validação.


7.3.1. Código incompatível na biblioteca padrão
-----------------------------------------------

A biblioteca padrão do Python contém alguns códigos que violam essas
regras automatizadas. Embora essas violações pareçam ser falsos
positivos, as regras de revisão da Apple não podem ser contestadas;
portanto, é necessário modificar a biblioteca padrão do Python para
que uma aplicação passe na revisão da App Store.

A árvore de fontes do Python contém um arquivo de patch que removerá
todo o código que é conhecido por causar problemas no processo de
revisão da App Store. Este patch é aplicado automaticamente quando o
ao construir para o iOS.


7.3.2. Manifestos de privacidade
--------------------------------

Em abril de 2025, a Apple introduziu um requisito para que
determinadas bibliotecas de terceiros forneçam um Manifesto de
Privacidade. Como resultado, se você tiver um módulo binário que usa
uma das bibliotecas afetadas, deverá fornecer um arquivo ".xcprivacy"
para essa biblioteca. O OpenSSL é uma biblioteca afetada por esse
requisito, mas existem outras.

Se você produzir um módulo binário chamado "meumódulo.so" e usar o
script de construção do Xcode descrito no passo 7 acima, poderá
colocar um arquivo "meumódulo.xcprivacy" ao lado de "meumódulo.so", e
o manifesto de privacidade será instalado no local necessário quando o
módulo binário for convertido em um framework.
