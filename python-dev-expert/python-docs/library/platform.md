"platform" ---  Acesso aos dados de identificação da plataforma subjacente
**************************************************************************

**Código-fonte:** Lib/platform.py

======================================================================

Nota:

  Plataformas específicas listadas em ordem alfabética, com Linux
  incluído na seção Unix.


Multiplataforma
===============

platform.architecture(executable=sys.executable, bits='', linkage='')

   Consulta o executável fornecido (o padrão é o binário do
   interpretador Python) para obter várias informações de arquitetura.

   Retorna uma tupla "(bits, linkage)" que contém informações sobre a
   arquitetura de bits e o formato de linkage usado para o executável.
   Ambos os valores são retornados como strings.

   Valores que não podem ser determinados são retornados como
   fornecidos pelas predefinições de parâmetros. Se bits for fornecido
   como "''", o "sizeof(pointer)" (ou "sizeof(long)" na versão Python
   < 1.5.2) é usado como indicador para o tamanho de ponteiro
   suportado.

   A função depende do comando "file" do sistema para fazer o trabalho
   real. Isso está disponível na maioria, se não em todas as
   plataformas Unix e algumas plataformas não Unix e somente se o
   executável apontar para o interpretador Python. Padrões razoáveis
   são usados quando as necessidades acima não são atendidas.

   Nota:

     No macOS (e talvez em outras plataformas), arquivos executáveis
     podem ser arquivos universais contendo diversas arquiteturas.Para
     obter a "característica de 64 bits" do interpretador atual, é
     mais confiável consultar o atributo "sys.maxsize":

        is_64bits = sys.maxsize > 2**32

platform.machine()

   Retorna o tipo de máquina, por exemplo, "'AMD64'". Uma string vazia
   é retornada se o valor não puder ser determinado.

   A saída depende da plataforma e pode diferir nas convenções de
   nomenclatura e uso de maiúsculas e minúsculas.

platform.node()

   Retorna o nome de rede do computador (pode não ser totalmente
   qualificado!). Uma string vazia é retornada se o valor não puder
   ser determinado.

platform.platform(aliased=False, terse=False)

   Retorna uma única string identificando a plataforma subjacente com
   o máximo de informações úteis possível.

   A saída é pretendida para ser *legível por humanos* em vez de
   analisável por máquinas. Pode parecer diferente em diferentes
   plataformas e isso é intencional.

   Se *aliased* for true, a função usará apelidos para várias
   plataformas que relatam nomes de sistemas que diferem de seus nomes
   comuns, por exemplo, SunOS será relatado como Solaris. A função
   "system_alias()" é usada para implementar isso.

   Definir *terse* como true faz com que a função retorne apenas o
   mínimo absoluto de informações necessárias para identificar a
   plataforma.

   Alterado na versão 3.8: No macOS, a função agora usa "mac_ver()",
   se retornar uma string de versão não vazia, para obter a versão do
   macOS em vez da versão do darwin.

platform.processor()

   Retorna o nome (real) do processador, por exemplo "'amdk6'".

   Uma string vazia é retornada se o valor não puder ser determinado.
   Note que muitas plataformas não fornecem essas informações ou
   simplesmente retornam o mesmo valor que para "machine()". O NetBSD
   faz isso.

platform.python_build()

   Retorna uma tupla "(buildno, builddate)" informando o número e a
   data da construção do Python como strings.

platform.python_compiler()

   Retorna uma string identificando o compilador usado para compilar
   Python.

platform.python_branch()

   Retorna uma string identificando a branch SCM da implementação do
   Python.

platform.python_implementation()

   Retorna uma string identificando a implementação do Python. Os
   valores de retorno possíveis são: 'CPython', 'IronPython',
   'Jython', 'PyPy'.

platform.python_revision()

   Retorna uma string que identifica a revisão do SCM da implementação
   Python.

platform.python_version()

   Retorna a versão do Python como string "'major.minor.patchlevel'".

   Observe que, diferentemente do "sys.version" do Python, o valor
   retornado sempre incluirá o patchlevel (o padrão é 0).

platform.python_version_tuple()

   Retorna a versão do Python como tupla "(major, minor, patchlevel)"
   de strings.

   Observe que, diferentemente do "sys.version" do Python, o valor
   retornado sempre incluirá o patchlevel (o padrão é "'0'").

platform.release()

   Retorna a versão do sistema, por exemplo, "'2.2.0'" ou "'NT'". Uma
   string vazia é retornada se o valor não puder ser determinado.

   No iOS e Android, esta é a versão do SO voltada para o usuário.
   Para obter a versão do kernel Darwin ou Linux, use "os.uname()".

platform.system()

   Retorna o nome do sistema/SO, como "'Linux'", "'Darwin'", "'Java'",
   "'Windows'". Uma string vazia é retornada se o valor não puder ser
   determinado.

   No iOS e Android, isso retorna o nome do SO voltado para o usuário
   (por exemplo, "'iOS", "'iPadOS'" ou "'Android'"). Para obter o nome
   do kernel ("'Darwin'" ou "'Linux'"), use "os.uname()".

platform.system_alias(system, release, version)

   Retorna "(sistema, release, versão)" com apelido para nomes comuns
   de marketing usados para alguns sistemas. Ele também faz alguma
   reordenação das informações em alguns casos em que, de outra forma,
   causaria confusão.

platform.version()

   Retorna a versão de lançamento do sistema, por exemplo, "'#3 on
   degas'". Uma string vazia é retornada se o valor não puder ser
   determinado.

platform.uname()

   Interface para uname razoavelmente portátil. Retorna um
   "namedtuple()" contendo seis atributos: "system", "node",
   "release", "version", "machine" e "processor".

   "processor" é resolvido tardiamente, sob demanda.

   Nota: os dois primeiros nomes de atributos diferem dos nomes
   apresentados por "os.uname()", onde são chamados "sysname" e
   "nodename".

   As entradas que não podem ser determinadas são definidas como "''".

   Alterado na versão 3.3: O resultado mudou de uma tupla para
   "namedtuple()".

   Alterado na versão 3.9: "processor" é resolvido tarde em vez de
   imediatamente.

platform.invalidate_caches()

   Limpa o cache interno de informações, como "uname()". Isso
   normalmente é útil quando o "node()" da plataforma é alterado por
   um processo externo e é necessário recuperar o valor atualizado.

   Adicionado na versão 3.14.


Plataforma Windows
==================

platform.win32_ver(release='', version='', csd='', ptype='')

   Obtém informações adicionais sobre a versão do Registro do Windows
   e retorna uma tupla "(release, version, csd, ptype)" referente à
   versão do SO, número da versão, nível do CSD (service pack) e tipo
   de sistema operacional (processador múltiplo/único). Os valores que
   não podem ser determinados são definidos para os padrões fornecidos
   como parâmetros (que são todos padrão para uma string vazia).

   Como dica: *ptype* é "'Uniprocessor Free'" em máquinas NT de
   processador único e "'Multiprocessor Free'" em máquinas de
   multiprocessador. O "'Free'" se refere à versão do sistema
   operacional que está livre de código de depuração. Ele também pode
   declarar "'Checked'", o que significa que a versão do sistema
   operacional usa código de depuração, ou seja, código que verifica
   argumentos, intervalos, etc.

platform.win32_edition()

   Retorna uma string representando a edição atual do Windows, ou
   "None" se o valor não puder ser determinado. Os valores possíveis
   incluem, mas não estão limitados a "'Enterprise'", "'IoTUAP'",
   "'ServerStandard'" e "'nanoserver'".

   Adicionado na versão 3.8.

platform.win32_is_iot()

   Retorna "True" se a edição do Windows retornada por
   "win32_edition()" for reconhecida como uma edição IoT.

   Adicionado na versão 3.8.


Plataforma macOS
================

platform.mac_ver(release='', versioninfo=('', '', ''), machine='')

   Obtém informações sobre a versão do macOS e retorna-as como tupla
   "(release, versioninfo, machine)", sendo *versioninfo* uma tupla
   "(version, dev_stage, non_release_version)".

   Entradas que não podem ser determinadas são definidas como "''".
   Todas as entradas de tupla são strings.


Plataforma iOS
==============

platform.ios_ver(system='', release='', model='', is_simulator=False)

   Obtém informações sobre a versão do iOS e retorna-as como
   "namedtuple()" com os seguintes atributos:

   * "system" é o nome do sistema operacional; "'iOS'" ou "'iPadOS'".

   * "release" é o número da versão do iOS como uma string (por
     exemplo, "'17.2'").

   * "model" é o identificador do modelo do dispositivo; será uma
     string como "'iPhone13,2'" para um dispositivo físico ou
     "'iPhone'" em um simulador.

   * "is_simulator" é um booleano que descreve se o aplicativo está
     sendo executado em um simulador ou em um dispositivo físico.

   As entradas que não podem ser determinadas são definidas para os
   padrões fornecidos como parâmetros.


Plataformas Unix
================

platform.libc_ver(executable=sys.executable, lib='', version='', chunksize=16384)

   Tenta determinar a versão libc contra a qual o executável do
   arquivo (padrão para o interpretador Python) está vinculado.
   Retorna uma tupla de strings "(lib, version)" que tem como padrão
   os parâmetros fornecidos caso a pesquisa falhe.

   Observe que esta função tem conhecimento profundo de como
   diferentes versões da libc adicionam símbolos ao executável e
   provavelmente só pode ser usada para executáveis compilados usando
   **gcc**.

   O arquivo é lido e escaneado em blocos de *chunksize* bytes.


Plataformas Linux
=================

platform.freedesktop_os_release()

   Obtém a identificação do sistema operacional do arquivo "os-
   release" e retorna-a como um dict. O arquivo "os-release" é um
   padrão freedesktop.org e está disponível na maioria das
   distribuições Linux. Uma exceção notável é o Android e as
   distribuições baseadas em Android.

   Levanta "OSError" ou subclasse quando nem "/etc/os-release" nem
   "/usr/lib/os-release" podem ser lidos.

   Em caso de sucesso, a função retorna um dicionário onde chaves e
   valores são strings. Valores têm seus caracteres especiais como """
   e "$" sem aspas. Os campos "NAME", "ID" e "PRETTY_NAME" são sempre
   definidos de acordo com o padrão. Todos os outros campos são
   opcionais. Os fornecedores podem incluir campos adicionais.

   Note que campos como "NAME", "VERSION" e "VARIANT" são strings
   adequadas para apresentação aos usuários. Os programas devem usar
   campos como "ID", "ID_LIKE", "VERSION_ID" ou "VARIANT_ID" para
   identificar distribuições Linux.

   Exemplo:

      def get_like_distro():
          info = platform.freedesktop_os_release()
          ids = [info["ID"]]
          if "ID_LIKE" in info:
              # ids são separados por espaço e ordenado por precedência
              ids.extend(info["ID_LIKE"].split())
          return ids

   Adicionado na versão 3.10.


Plataforma Android
==================

platform.android_ver(release='', api_level=0, manufacturer='', model='', device='', is_emulator=False)

   Obtém informações do dispositivo Android. Retorna um "namedtuple()"
   com os seguintes atributos. Valores que não podem ser determinados
   são definidos para os padrões fornecidos como parâmetros.

   * "release" - Versão do Android, como uma string (por exemplo,
     ""14"").

   * "api_level" - Nível de API do dispositivo em execução, como um
     inteiro (por exemplo, "34" para Android 14). Para obter o nível
     de API contra o qual o Python foi criado, consulte
     "sys.getandroidapilevel()".

   * "manufacturer" - Nome do fabricante.

   * "model" - Nome do modelo – normalmente o nome de marketing ou o
     número do modelo.

   * "device" - Nome do dispositivo – normalmente o número do modelo
     ou um codinome.

   * "is_emulator" - "True" se o dispositivo for um emulador; "False"
     se for um dispositivo físico.

   O Google mantém uma lista de nomes de modelos e dispositivos
   conhecidos.

   Adicionado na versão 3.13.


Uso na linha de comando
=======================

"platform" também pode ser invocado diretamente usando a opção "-m" do
interpretador:

   python -m platform [--terse] [--nonaliased] [{nonaliased,terse} ...]

As seguintes opções são aceitas:

--terse

   Exibe informações concisas sobre a plataforma. Isso equivale a
   chamar "platform.platform()" com o argumento *terse* definido como
   "True".

--nonaliased

   Exibe informações da plataforma sem alias de nome do sistema/SO.
   Isso equivale a chamar "platform.platform()" com o argumento
   *aliased* definido como "True".

Você também pode passar um ou mais argumentos posicionais ("terse",
"nonaliased") para controlar explicitamente o formato de saída. Eles
se comportam de forma semelhante às suas opções correspondentes.
