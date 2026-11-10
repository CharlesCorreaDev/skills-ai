1. Linha de comando e ambiente
******************************

O interpretador CPython verifica a linha de comando e o ambiente em
busca de várias configurações.

Os esquemas de linha de comando de outras implementações podem ser
diferentes. Consulte Implementações Alternativas para mais recursos.


1.1. Linha de comando
=====================

Ao invocar o Python, você pode especificar qualquer uma destas opções:

   python [-bBdEhiIOPqRsSuvVWx?] [-c command | -m module-name | script | - ] [args]

O caso de uso mais comum é, obviamente, uma simples invocação de um
script:

   python meuscript.py


1.1.1. Opções de interface
--------------------------

A interface do interpretador é semelhante à do console do UNIX, mas
fornece alguns métodos adicionais de chamada:

* Quando chamado com a entrada padrão conectada a um dispositivo tty,
  ele solicita comandos e os executa até um EOF (um caractere de fim
  de arquivo, você pode produzi-lo com "Ctrl"-"D" no UNIX ou
  "Ctrl"-"Z," "Enter" no Windows) ser lido. Para mais informações
  sobre o modo interativo, veja Modo interativo.

* Quando chamado com um nome de arquivo como argumento ou com um
  arquivo como entrada padrão, ele lê e executa o script desse
  arquivo.

* Quando chamado com um nome de diretório como argumento, ele lê e
  executa um script adequadamente nomeado nesse diretório.

* Quando chamado com "-c command", ele executa as instruções Python
  fornecidas como *command*. Aqui *command* pode conter várias
  instruções separadas por novas linhas.

* Quando chamado com "-m module-name", o módulo especificado é
  localizado pelo mecanismo de importação padrão e executado como um
  script.

No modo não interativo, toda a entrada é analisada antes de ser
executada.

Uma opção de interface termina a lista de opções consumidas pelo
interpretador, todos os argumentos consecutivos terminam em "sys.argv"
-- observe que o primeiro elemento, índice zero ("sys.argv[0]") , é
uma string que reflete a fonte do programa.

-c <command>

   Executa o código Python em *command*. *command* pode ser uma ou
   mais instruções separadas por novas linhas, com espaços em branco à
   esquerda significativos, como em um código de um módulo normal.

   Se esta opção for fornecida, o primeiro elemento de "sys.argv" será
   ""-c"" e o diretório atual será adicionado ao início de "sys.path"
   (permitindo que módulos nesse diretório sejam importados como
   módulos de nível superior).

   Levanta um evento de auditoria "cpython.run_command" com o
   argumento "command".

   Alterado na versão 3.14: *command* é automaticamente desindentado
   antes da execução.

-m <module-name>

   Localiza o módulo usando o mecanismo de importação padrão e executa
   seu conteúdo como o módulo "__main__".

   Como o argumento é o nome de um *módulo*, você não deve fornecer
   uma extensão de arquivo (".py"). O nome do módulo deve ser um nome
   de módulo Python absoluto válido, mas a implementação nem sempre
   exige isso (por exemplo, pode permitir que você use um nome que
   inclua um hífen).

   Nomes de pacotes (incluindo pacotes de espaço de nomes) também são
   permitidos. Quando um nome de pacote é fornecido ao invés de um
   módulo normal, o interpretador irá executar "<pkg>.__main__" como o
   módulo principal. Esse comportamento é deliberadamente semelhante
   ao tratamento de diretórios e arquivos zip que são passados para o
   interpretador como o argumento do script.

   Nota:

     Esta opção não pode ser usada com módulos embutidos e com módulos
     de extensão escritos em C, pois não possuem arquivos de módulo em
     Python. No entanto, ele ainda pode ser usado para módulos
     pré-compilados, mesmo que o arquivo-fonte original não esteja
     disponível.

   Se esta opção for fornecida, o primeiro elemento de "sys.argv" será
   o caminho completo para o arquivo do módulo (enquanto o arquivo do
   módulo está sendo localizado, o primeiro elemento será definido
   como ""-m""). Como com a opção "-c", o diretório atual será
   adicionado ao início de "sys.path".

   A opção "-I" pode ser usada para executar o script em modo isolado,
   em que "sys.path" não contém nem o diretório atual nem o diretório
   de pacotes do usuário. Todas as variáveis de ambiente "PYTHON*" são
   ignoradas também.

   Muitos módulos de biblioteca padrão contêm código que é executado
   como um script. Um exemplo é o módulo "timeit":

      python -m timeit -s "configuração inicial aqui" "código a ser analisado aqui"
      python -m timeit -h # para detalhes

   Levanta um evento de auditoria "cpython.run_module" com o argumento
   "module-name".

   Ver também:

     "runpy.run_module()"
        Funcionalidade equivalente diretamente disponível para código
        Python

     **PEP 338** -- Executing modules as scripts

   Alterado na versão 3.1: Forneça o nome do pacote para executar um
   submódulo "__main__".

   Alterado na versão 3.4: Pacotes de espaço de nomes também são
   suportados

-

   Lê os comandos da entrada padrão ("sys.stdin"). Se a entrada padrão
   for um terminal, "-i" está implícito.

   Se esta opção for fornecida, o primeiro elemento de "sys.argv" será
   ""-"" e o diretório atual será adicionado ao início de "sys.path".

   Levanta um evento de auditoria "cpython.run_stdin" sem argumentos.

<script>

   Executa o código Python contido em *script*, que deve ser um
   caminho do sistema de arquivos (absoluto ou relativo) referindo-se
   a um arquivo Python, um diretório contendo um arquivo
   "__main__.py", ou um arquivo zip contendo um arquivo "__main__.py".

   Se esta opção for fornecida, o primeiro elemento de "sys.argv" será
   o nome do script conforme fornecido na linha de comando.

   Se o nome do script se referir diretamente a um arquivo Python, o
   diretório que contém esse arquivo é adicionado ao início de
   "sys.path", e o arquivo é executado como o módulo "__main__".

   Se o nome do script se referir a um diretório ou arquivo zip, o
   nome do script será adicionado ao início de "sys.path" e o arquivo
   "__main__.py" nesse local será executado como o módulo "__main__".

   A opção "-I" pode ser usada para executar o script em modo isolado
   onde "sys.path" não contém nem o diretório do script nem o
   diretório de pacotes do usuário. Todas as variáveis de ambiente
   "PYTHON*" são ignoradas também.

   Levanta um evento de auditoria "cpython.run_file" com o argumento
   "filename".

   Ver também:

     "runpy.run_path()"
        Funcionalidade equivalente diretamente disponível para código
        Python

Se nenhuma opção de interface for fornecida, "-i" está implícito,
"sys.argv[0]" é uma string vazia ("""") e o diretório atual será
adicionado ao início de "sys.path". Além disso, o preenchimento por
tab e a edição do histórico são habilitados automaticamente, se
disponíveis em sua plataforma (veja Configuração Readline).

Ver também: Chamando o interpretador

Alterado na versão 3.4: Ativação automática de preenchimento com tab e
edição de histórico.


1.1.2. Opções genéricas
-----------------------

-?
-h
--help

   Imprime uma breve descrição de todas as opções de linha de comando
   e variáveis de ambiente correspondentes e sai.

--help-env

   Imprime uma breve descrição das variáveis de ambiente específicas
   do Python e sai.

   Adicionado na versão 3.11.

--help-xoptions

   Imprime uma descrição das opções "-X" específicas da implementação
   e sai.

   Adicionado na versão 3.11.

--help-all

   Imprime as informações de uso completas e sai.

   Adicionado na versão 3.11.

-V
--version

   Exibe o número da versão do Python e sai. O exemplo de saída
   poderia ser:

      Python 3.8.0b2+

   Quando fornecido duas vezes, exibe mais informações sobre a
   construção, como:

      Python 3.8.0b2+ (3.8:0c076caaa8, Apr 20 2019, 21:55:00)
      [GCC 6.2.0 20161005]

   Adicionado na versão 3.6: A opção "-VV".


1.1.3. Opções diversas
----------------------

-b

   Emite um aviso ao converter "bytes" ou "bytearray" para "str" sem
   especificar a codificação, ou ao comparar "bytes" ou "bytearray"
   com "str", ou "bytes" com "int". Emite um erro quando a opção é
   fornecida duas vezes ("-bb").

   Alterado na versão 3.5: Afeta também as comparações de "bytes" com
   "int".

   Descontinuado desde a versão 3.15: Descontinua as opções "-b" e
   "-bb", planejando para se tornarem sem efeito em Python 3.17. Esses
   foram primariamente auxiliares da transição Python 2 -> 3. A partir
   de Python 3.17, nenhum "BytesWarning" será levantada para esses
   casos; em vez disso, use um verificador de tipos.

-B

   Se fornecido, Python não tentará escrever arquivos ".pyc" na
   importação de módulos fonte. Veja também "PYTHONDONTWRITEBYTECODE".

--check-hash-based-pycs default|always|never

   Controla o comportamento de validação de arquivos ".pyc" baseados
   em hash. Veja Invalidação de bytecode em cache. Quando definido
   como "default", os arquivos de cache de bytecode baseados em hash
   verificados e não verificados são validados de acordo com sua
   semântica padrão. Quando definido como "always", todos os arquivos
   ".pyc" baseados em hash, sejam verificados ou não verificados, são
   validados para seus arquivos fonte correspondentes. Quando definido
   como "never", os arquivos ".pyc" baseados em hash não são validados
   contra seus respectivos arquivos fonte.

   A semântica dos arquivos ".pyc" baseados em marca de tempo não é
   afetada por esta opção.

-d

   Ativa a saída do analisador sintático de depuração (uso avançado).
   Consulte também a variável de ambiente "PYTHONDEBUG".

   Essa opção requer uma construção de depuração do Python, caso
   contrário, será ignorada.

-E

   Ignora todas as variáveis de ambiente "PYTHON*", por exemplo
   "PYTHONPATH" e "PYTHONHOME", que podem ser definidas.

   Veja também as opções "-P" e "-I" (isolado).

-i

   Entra no modo interativo após a execução.

   Usar a opção "-i" vai entrar no modo interativo em qualquer uma das
   circunstâncias:

   * Quando um script é passado como primeiro argumento

   * Quando a opção "-c" é usada

   * Quando a opção "-m" é usada

   O modo interativo vai ser iniciado mesmo quando a "sys.stdin" não
   parecer ser um terminal. O arquivo "PYTHONSTARTUP" não é lido.

   Isso pode ser útil para inspecionar variáveis globais ou o stack
   trace (situação da pilha de execução) quando um script levanta uma
   exceção. Veja também "PYTHONINSPECT".

-I

   Executa o Python em modo isolado. Isso também implica nas opções
   "-E", "-P" e "-s".

   No modo isolado, "sys.path" não contém o diretório do script nem o
   diretório de pacotes do site do usuário. Todas as variáveis de
   ambiente "PYTHON*" também são ignoradas. Outras restrições podem
   ser impostas para evitar que o usuário injete código malicioso.

   Adicionado na versão 3.4.

-O

   Remove as instruções de asserção e qualquer código condicional que
   envolva o valor de "__debug__". Aumenta o nome do arquivo de
   arquivos compilados (*bytecode*) adicionando ".opt-1" antes da
   extensão ".pyc" (veja **PEP 488**). Veja também "PYTHONOPTIMIZE".

   Alterado na versão 3.5: Modifica nomes de arquivos ".pyc" conforme
   a **PEP 488**.

-OO

   Faz o mesmo que "-O" e também descarta as strings de documentação.
   Aumenta o nome dos arquivos de bytecode compilados (*bytecode*)
   adicionando ".opt-2" antes da extensão ".pyc" (veja **PEP 488**).

   Alterado na versão 3.5: Modifica nomes de arquivos ".pyc" conforme
   a **PEP 488**.

-P

   Não anexa um caminho potencialmente inseguro a "sys.path":

   * Linha de comando "python -m módulo": não anexa o diretório atual.

   * Linha de comando "python script.py": não anexa o diretório do
     próprio script. Se for um link simbólico, resolve links
     simbólicos.

   * Linhas de comando "python -c código" e "python" (REPL): não
     anexam uma string vazia, o que significa o diretório de trabalho
     atual.

   Veja também a variável de ambiente "PYTHONSAFEPATH" e as opções
   "-E" e "-I" (isolado).

   Adicionado na versão 3.11.

-q

   Não exibe as mensagens de direitos autorais e de versão nem mesmo
   no modo interativo.

   Adicionado na versão 3.2.

-R

   Habilita a aleatorização com hash. Esta opção só tem efeito se a
   variável de ambiente "PYTHONHASHSEED" estiver configurada para um
   valor diferente de "random", uma vez que a aleatorização com hash é
   habilitada por padrão.

   Em versões anteriores do Python, esta opção ativa a aleatorização
   com hash, para que os valores "__hash__()" dos objetos str e bytes
   sejam "salgados" com um valor aleatório imprevisível. Embora
   permaneçam constantes em um processo Python individual, eles não
   são previsíveis entre invocações repetidas de Python.

   A aleatorização com hash se destina a fornecer proteção contra uma
   negação de serviço causada por entradas cuidadosamente escolhidas
   que exploram o pior caso de desempenho de uma inserção de
   dicionário, de complexidade *O*(*n*^2). Consulte
   https://ocert.org/advisories/ocert-2011-003.html para obter
   detalhes.

   "PYTHONHASHSEED" permite definir um valor fixo para o hash da
   semente.

   Adicionado na versão 3.2.3.

   Alterado na versão 3.7: A opção não é mais ignorada.

-s

   Não adiciona o "diretório site-packages do usuário" a "sys.path".

   Veja também "PYTHONNOUSERSITE".

   Ver também: **PEP 370** -- Diretório site-packages por usuário.

-S

   Desabilita a importação do módulo "site" e as manipulações do
   "sys.path" que isso acarreta. Também desabilita essas manipulações
   se "site" for explicitamente importado mais tarde (chame
   "site.main()" se você quiser que eles sejam acionados).

-u

   Força os fluxos de saída e de erro padrão (stdout e stderr) a não
   terem buffer. Esta opção não tem efeito no fluxo de entrada padrão
   (stdin).

   Veja também "PYTHONUNBUFFERED".

   Alterado na versão 3.7: A camada de texto dos fluxos stdout e
   stderr agora é sem buffer.

-v

   Exibe uma mensagem cada vez que um módulo é inicializado, mostrando
   o local (nome do arquivo ou módulo embutido) de onde ele é
   carregado. Quando fornecido duas vezes ("-vv"), exibe uma mensagem
   para cada arquivo verificado durante a busca por um módulo. Também
   fornece informações sobre a limpeza do módulo na saída.

   Alterado na versão 3.10: O módulo "site" relata os caminhos
   específicos do site e os arquivos ".pth" sendo processados.

   Veja também "PYTHONVERBOSE".

-W arg

   Controle de advertência. O mecanismo de aviso do Python, por
   padrão, exibe mensagens de aviso para "sys.stderr".

   As configurações mais simples aplicam uma determinada ação
   incondicionalmente a todos os avisos emitidos por um processo
   (mesmo aqueles que são ignorados por padrão):

      -Wdefault  # Avisa uma vez por local de chamada
      -Werror    # Converte para exceções
      -Walways   # Avisa toda vez
      -Wall      # Mesmo que -Walways
      -Wmodule   # Avisa uma vez por módulo chamador
      -Wonce     # Avisa uma vez por processo do Python
      -Wignore   # Nunca avisa

   Os nomes das ações podem ser abreviados conforme desejado, e o
   interpretador irá resolvê-los para o nome da ação apropriado. Por
   exemplo, "-Wi" é equivalente a "-Wignore".

   A forma completa de argumento é:

      action:message:category:module:lineno

   Os campos vazios correspondem a todos os valores; campos vazios à
   direita podem ser omitidos. Por exemplo, "-W
   ignore::DeprecationWarning" ignora todos os avisos de
   DeprecationWarning.

   O campo *action* é explicado acima, mas aplica-se apenas aos avisos
   que correspondem aos campos restantes.

   O campo *message* deve corresponder a toda a mensagem de aviso;
   essa correspondência não diferencia maiúsculas de minúsculas. Se
   começar e terminar com uma barra ("/"), estará especificando uma
   expressão regular, caso contrário, é uma string literal.

   O campo *category* corresponde à categoria de aviso (ex.:
   "DeprecationWarning"). Deve ser um nome de classe; o teste de
   correspondência verifica se a categoria de aviso real da mensagem é
   subclasse da categoria de aviso especificada.

   O campo *module* corresponde ao nome do módulo (totalmente
   qualificado); esta correspondência diferencia maiúsculas de
   minúsculas. Se começar e terminar com uma barra ("/"), ele
   especifica uma expressão regular a qual o início do nome do módulo
   totalmente qualificado deve corresponder; caso contrário,
   especifica uma string literal à qual o nome do módulo totalmente
   qualificado deve ser igual.

   O campo *lineno* corresponde ao número da linha, em que zero
   corresponde a todos os números de linha e, portanto, é equivalente
   a um número de linha omitido.

   Múltiplas opções "-W" podem ser fornecidas; quando um aviso
   corresponde a mais de uma opção, a ação da última opção
   correspondente é executada. As opções "-W" inválidas são ignoradas
   (embora uma mensagem de aviso seja exibida sobre opções inválidas
   quando o primeiro aviso for emitido).

   Os avisos também podem ser controlados usando a variável de
   ambiente "PYTHONWARNINGS" e, dentro de um programa Python, usando o
   módulo "warnings". Por exemplo, a função
   "warnings.filterwarnings()" pode ser usada para aplicar uma
   expressão regular à mensagem de aviso.

   Veja O filtro de avisos e Descrevendo filtros de aviso para mais
   detalhes.

   Alterado na versão 3.15: Adicionado suporte para expressão regular
   em *message* e *module*.

-x

   Pula a primeira linha do código-fonte, permitindo o uso de formas
   não-Unix de "#!cmd".

   Isso pode ser usado para transformar um script Python em um arquivo
   de lote (bat) do Windows. De forma semelhante a adicionar uma linha
   *shebang* e definir o bit de execução no Unix, a extensão do script
   Python pode ser alterada para ".bat" e a seguinte linha pode ser
   adicionada ao início do script:

      @py -x "%~f0" %* & exit /b

   ou, para especificar ou caminho do interpretador do Python
   especificamente:

      @"C:\Caminho\para\python.exe" -x "%~f0" %* & exit /b

   Ao contrário da linha *shebang*, que é um comentário em Python,
   esta linha não é uma sintaxe Python válida, e a opção "-x" é
   necessária para ignorá-la.

-X

   Reservado para várias opções específicas de implementação. CPython
   atualmente define os seguintes valores possíveis:

   * "-X faulthandler" para habilitar "faulthandler". Veja também
     "PYTHONFAULTHANDLER".

     Adicionado na versão 3.3.

   * "-X showrefcount" para emitir a contagem de referências total e o
     número de blocos de memória usados quando o programa termina ou
     após cada instrução no interpretador interativo. Isso só funciona
     em construções de depuração.

     Adicionado na versão 3.4.

   * "-X tracemalloc" para começar a rastrear alocações de memória do
     Python usando o módulo "tracemalloc". Por padrão, apenas o quadro
     mais recente é armazenado no traceback (situação da pilha de
     execução) de um rastro. Use "-X tracemalloc=NFRAME" para iniciar
     o rastreamento com um limite de traceback de quadros *NFRAME*.
     Veja o "tracemalloc.start()" e "PYTHONTRACEMALLOC" para mais
     informações.

     Adicionado na versão 3.4.

   * "-X int_max_str_digits" configura a limitação de comprimento de
     string na conversão para inteiro. Veja também
     "PYTHONINTMAXSTRDIGITS".

     Adicionado na versão 3.11.

   * "-X importtime" para mostrar quanto tempo leva cada importação.
     Mostra o nome do módulo, tempo cumulativo (incluindo importações
     aninhadas) e tempo próprio (excluindo importações aninhadas).
     Observe que sua saída pode ser interrompida em aplicações
     multithread. O uso típico é "python -X importtime -c 'import
     asyncio'".

     "-X importtime=2" habilita uma saída adicional que indica quando
     um módulo importado já foi carregado. Nesses casos, a string
     "cached" será impressa em ambas as colunas de tempo.

     Veja também "PYTHONPROFILEIMPORTTIME".

     Adicionado na versão 3.7.

     Alterado na versão 3.14: Adicionado "-X importtime=2" para também
     rastrear importações de módulos carregados e valores reservados
     diferentes de "1" e "2" para uso futuro.

   * "-X dev": habilita Modo de Desenvolvimento do Python,
     introduzindo verificações adicionais de tempo de execução que são
     muito custosas para serem habilitadas por padrão. Veja também
     "PYTHONDEVMODE".

     Adicionado na versão 3.7.

   * "-X utf8" habilita o Modo UTF-8 do Python. "-X utf8=0"
     explicitamente desabilita o Modo UTF-8 do Python (mesmo quando de
     outra forma seria ativado automaticamente). Veja também
     "PYTHONUTF8".

     Adicionado na versão 3.7.

   * "-X pycache_prefix=PATH" permite a escrita de arquivos ".pyc" em
     uma árvore paralela enraizada em um determinado diretório em vez
     de na árvore de código. Veja também "PYTHONPYCACHEPREFIX".

     Adicionado na versão 3.8.

   * "-X warn_default_encoding" emite uma "EncodingWarning" quando a
     codificação padrão específica da localidade é usada para abrir
     arquivos. Veja também  "PYTHONWARNDEFAULTENCODING".

     Adicionado na versão 3.10.

   * "-X no_debug_ranges" desabilita a inclusão das tabelas que
     mapeiam informações de localização extra (linha final,
     deslocamento da coluna inicial e deslocamento da coluna final)
     para cada instrução em objetos código. Isso é útil quando objetos
     código menores e arquivos pyc são desejados, bem como suprimir os
     indicadores de localização visual extra quando o interpretador
     exibe tracebacks (situação da pilha de execução). Veja também
     "PYTHONNODEBUGRANGES".

     Adicionado na versão 3.11.

   * "-X frozen_modules" determina se os módulos congelados são ou não
     ignorados pelo maquinário de importação. Um valor de "on"
     significa que eles são importados e "off" significa que eles são
     ignorados. O padrão é "on" se este for um Python instalado (o
     caso normal). Se estiver em desenvolvimento (executando a partir
     da árvore de origem), o padrão é "off". Observe que os módulos
     congelados "importlib_bootstrap" e "importlib_bootstrap_external"
     são sempre usados, mesmo que esse sinalizador esteja definido
     como "off". Veja também "PYTHON_FROZEN_MODULES".

     Adicionado na versão 3.11.

   * "-X perf" habilita o suporte para o perfilador do Linux "perf".
     Quando essa opção for fornecida, o perfilador "perf" poderá
     relatar chamadas Python. Essa opção está disponível apenas em
     algumas plataformas e não fará nada se não for compatível com o
     sistema atual. O valor padrão é "off". Consulte também:
     "PYTHONPERFSUPPORT" e Python support for the perf map compatible
     profilers.

     Adicionado na versão 3.12.

   * "-X perf_jit" habilita o suporte para o perfilador do Linux
     "perf" com suporte a DWARF. Quando essa opção for fornecida, o
     perfilador "perf" poderá relatar chamadas Python usando
     informações de DWARF. Essa opção está disponível somente em
     algumas plataformas e não fará nada se não for compatível com o
     sistema atual. O valor padrão é "off". Veja também:
     "PYTHON_PERF_JIT_SUPPORT" e Python support for the perf map
     compatible profilers.

     Adicionado na versão 3.13.

   * "-X disable-remote-debug" desabilita o suporte à depuração
     remota, conforme descrito em **PEP 768**. Isso inclui tanto a
     funcionalidade de agendar código para execução em outro processo
     quanto a de receber código para execução no processo atual.

     Esta opção está disponível apenas em algumas plataformas e não
     fará nada se não for compatível com o sistema atual. Veja também
     "PYTHON_DISABLE_REMOTE_DEBUG" e **PEP 768**.

     Adicionado na versão 3.14.

   * "-X cpu_count=*n*" substitui "os.cpu_count()",
     "os.process_cpu_count()" e "multiprocessing.cpu_count()". *n*
     deve ser maior ou igual a 1. Esta opção pode ser útil para
     usuários que precisam limitar os recursos da CPU de um sistema
     contêiner. Veja também "PYTHON_CPU_COUNT". Se *n* for "default",
     nada será substituído.

     Adicionado na versão 3.13.

   * "-X presite=*módulo*" ou "-X presite=*módulo:função*" especifica
     um ponto de entrada que deve ser executado antes de o módulo
     "site" ser executado e antes de o módulo "__main__" existir.
     Portanto, o módulo importado não é "__main__". Isso pode ser
     usado para executar código antes da inicialização do Python.
     Python precisa ser construído no modo de depuração para que esta
     opção exista. Veja também "PYTHON_PRESITE".

     Alterado na versão 3.15: Aceita também o formato "módulo:função"
     como ponto de entrada.

     Adicionado na versão 3.13.

   * "-X gil=*0,1*" força a GIL a ser desabilitada ou habilitada,
     respectivamente. A definição para "0" está disponível apenas em
     construções configuradas com "--disable-gil". Veja também
     "PYTHON_GIL" e CPython com threads livres.

     Adicionado na versão 3.13.

   * "-X thread_inherit_context=*0,1*" faz com que "Thread" use, por
     padrão, uma cópia do contexto do chamador de "Thread.start()" ao
     iniciar. Caso contrário, as threads iniciarão com um contexto
     vazio. Se não definida, o valor padrão desta opção será "1" em
     construções com threads livres e "0" em outras. Veja também
     "PYTHON_THREAD_INHERIT_CONTEXT".

     Adicionado na versão 3.14.

   * "-X context_aware_warnings=*0,1*" faz com que o gerenciador de
     contexto "warnings.catch_warnings" use uma "ContextVar" para
     armazenar o estado do filtro de avisos. Se não definida, o valor
     padrão desta opção será "1" em construções com threads livres e
     "0" em outras. Veja também "PYTHON_CONTEXT_AWARE_WARNINGS".

     Adicionado na versão 3.14.

   * "-X pathconfig_warnings=*0,1*", se verdadeiro ("1"), permite que
     A inicialização do caminho de pesquisa de módulos sys.path
     registre alertas em stderr. Se falso ("0"), suprime estes
     alertas. Definido como verdadeiro por padrão. Veja também
     "PYTHON_PATHCONFIG_WARNINGS" .

     Adicionado na versão 3.15.

   * "-X tlbc=*0,1*" habilita (1, o padrão) ou desabilita (0) o
     bytecode local da thread em construções configuradas com "--
     disable-gil". Quando desabilitado, também desabilita o
     interpretador especializado. Veja também "PYTHON_TLBC".

     Adicionado na versão 3.14.

   * "-X lazy_imports=*all,normal*" controla o comportamento de
     importação preguiçosa. "all" torna todas as importações
     preguiçosas por padrão e "normal" (o padrão) respeita a palavra-
     chave "lazy" no código-fonte. Veja também "PYTHON_LAZY_IMPORTS" .

     Adicionado na versão 3.15.

   Também permite passar valores arbitrários e recuperá-los por meio
   do dicionário "sys._xoptions".

   Adicionado na versão 3.2.

   Alterado na versão 3.9: Removida a opção "-X showalloccount".

   Alterado na versão 3.10: Removida a opção "-X oldparser".

Removido na versão 3.14: "-J" não é mais reservado para uso por Jython
e agora não tem nenhum significado especial.


1.1.4. Controlando cores
------------------------

O interpretador Python é configurado por padrão para usar cores para
destacar a saída em determinadas situações, como ao exibir tracebacks
(situação da pilha de execução). Este comportamento pode ser
controlado ao definir diferentes variáveis de ambiente.

Definir a variável de ambiente "TERM" como "dumb" desativará a
exibição de cores.

Se a variável de ambiente "FORCE_COLOR" estiver definida, a cor será
habilitada independentemente do valor de TERM. Isso é útil em sistemas
CI que não são terminais, mas ainda podem exibir sequências de escape
ANSI.

Se a variável de ambiente "NO_COLOR" estiver definida, o Python
desativará todas as cores na saída. Isto tem precedência sobre
"FORCE_COLOR".

Todas essas variáveis de ambiente também são usadas por outras
ferramentas para controlar a saída de cores. Para controlar a saída de
cores apenas no interpretador Python, a variável de ambiente
"PYTHON_COLORS" pode ser usada. Esta variável tem precedência sobre
"NO_COLOR", que, por sua vez, tem precedência sobre "FORCE_COLOR".


1.2. Variáveis de ambiente
==========================

Essas variáveis de ambiente influenciam o comportamento do Python,
elas são processadas antes das opções de linha de comando diferentes
de -E ou -I. É comum que as opções de linha de comando substituam as
variáveis de ambiente em caso de conflito.

PYTHONHOME

   Altera a localização das bibliotecas padrão do  Python. Por padrão,
   as bibliotecas são pesquisadas em "*prefix*/lib/python*version*" e
   "*exec_prefix*/lib/python*version*", onde "*prefix*" e
   "*exec_prefix*" são diretórios dependentes da instalação, ambos
   padronizados para "/usr/local".

   Quando "PYTHONHOME" é definido como um único diretório, seu valor
   substitui "*prefix*" e "*exec_prefix*". Para especificar valores
   diferentes para estes, defina "PYTHONHOME" para
   "*prefix*:*exec_prefix*".

PYTHONPATH

   Aumenta o caminho de pesquisa padrão para arquivos de módulo. O
   formato é o mesmo da variável "PATH" do shell: um ou mais caminhos
   de diretório separados por "os.pathsep" (por exemplo, dois pontos
   no Unix ou ponto e vírgula no Windows). Os diretórios inexistentes
   são ignorados silenciosamente.

   Além dos diretórios normais, entradas individuais "PYTHONPATH"
   podem referir-se a arquivos zip contendo módulos Python puros
   (tanto no código-fonte quanto na forma compilada). Módulos de
   extensão não podem ser importados de arquivos zip.

   O caminho de pesquisa padrão depende da instalação, mas geralmente
   começa com "*prefix*/lib/python*version*" (veja "PYTHONHOME"
   acima). É *sempre* anexado a "PYTHONPATH".

   Um diretório adicional será inserido no caminho de pesquisa antes
   de "PYTHONPATH", conforme descrito acima em Opções de interface. O
   caminho de pesquisa pode ser manipulado de partir de um programa em
   Python, por meio da variável "sys.path".

PYTHONSAFEPATH

   Se for definido como uma string não vazia, não anexa um caminho
   potencialmente inseguro à "sys.path": consulte a opção "-P" para
   obter detalhes.

   Adicionado na versão 3.11.

PYTHONPLATLIBDIR

   Se for definida como uma string não vazia, ela substitui o valor de
   "sys.platlibdir".

   Adicionado na versão 3.9.

PYTHONSTARTUP

   Se este for o nome de um arquivo legível, os comandos Python nesse
   arquivo serão executados antes que o primeiro prompt seja exibido
   no modo interativo. O arquivo é executado no mesmo espaço de nomes
   em que os comandos interativos são executados, para que os objetos
   definidos ou importados nele possam ser usados sem qualificação na
   sessão interativa. Você também pode alterar os prompts "sys.ps1" e
   "sys.ps2", bem como o gancho "sys.__interactivehook__", neste
   arquivo.

   Levanta um evento de auditoria "cpython.run_startup" com o nome de
   arquivo como argumento quando chamado na inicialização.

PYTHONOPTIMIZE

   Se for definido como uma string não vazia, é equivalente a
   especificar a opção "-O". Se definido como um inteiro, é
   equivalente a especificar "-O" várias vezes.

PYTHONBREAKPOINT

   Se estiver definida, ela nomeia um chamável usando a notação de
   caminho com pontos. O módulo que contém o chamável será importado
   e, então, o chamável será executado pela implementação padrão de
   "sys.breakpointhook()", chamada pelo "breakpoint()" embutido. Se
   não for definido, ou definido como uma string vazia, é equivalente
   ao valor de "pdb.set_trace". Definir isso para a string "0" faz com
   que a implementação padrão de "sys.breakpointhook()" não faça mais
   nada além de retornar imediatamente.

   Adicionado na versão 3.7.

PYTHONDEBUG

   Se for definido como uma string não vazia, é equivalente a
   especificar a opção "-d". Se definido como um inteiro, é
   equivalente a especificar "-d" várias vezes.

   Essa variável de ambiente requer uma construção de depuração do
   Python, caso contrário, será ignorada.

PYTHONINSPECT

   Se for definido como uma string não vazia, é equivalente a
   especificar a opção "-i".

   Esta variável também pode ser modificada pelo código Python usando
   "os.environ" para forçar o modo de inspeção ao encerrar o programa.

   Levanta um evento de auditoria "cpython.run_stdin" sem argumentos.

   Alterado na versão 3.12.5: (também 3.11.10, 3.10.15, 3.9.20 e
   3.8.20) Emite eventos de auditoria.

   Alterado na versão 3.13: Usa PyrePL, se possível, nesse caso
   "PYTHONSTARTUP" também é executado. Emite eventos de auditoria.

PYTHONUNBUFFERED

   Se for definido como uma string não vazia, é equivalente a
   especificar a opção "-u".

PYTHONVERBOSE

   Se for definido como uma string não vazia, é equivalente a
   especificar a opção "-v". Se definido como um inteiro, é
   equivalente a especificar "-v" várias vezes.

PYTHONCASEOK

   Se estiver definido, Python não diferencia letras maiúsculas e
   minúsculas nas instruções "import". Isso só funciona no Windows e
   no OS X.

PYTHONDONTWRITEBYTECODE

   Se for definido como uma string não vazia, o Python não tentará
   escrever arquivos ".pyc" na importação de módulos-fonte. Isso
   equivale a especificar a opção "-B".

PYTHONPYCACHEPREFIX

   Se estiver definido, o Python escreverá os arquivos ".pyc" em uma
   árvore de diretório espelho neste caminho, em vez de nos diretórios
   "__pycache__" dentro da árvore de fontes. Isso equivale a
   especificar a opção "-X" "pycache_prefix=PATH".

   Adicionado na versão 3.8.

PYTHONHASHSEED

   Se esta variável não for definida ou definida como "random", um
   valor aleatório é usado para semear os hashes de objetos str e
   bytes.

   Se "PYTHONHASHSEED" for definido como um valor inteiro, ele é usado
   como semente fixa para gerar o hash() dos tipos cobertos pela
   aleatorização de hash.

   Sua finalidade é permitir hashes repetíveis, como em autotestes do
   próprio interpretador, ou permitir que um cluster de processos
   Python compartilhe valores de hash.

   O número inteiro deve ser um número decimal no intervalo
   [0,4294967295]. Especificar o valor 0 desabilitará a aleatorização
   de hash.

   Adicionado na versão 3.2.3.

PYTHONINTMAXSTRDIGITS

   Se esta variável estiver definida como um inteiro, é usada para
   configurar a limitação de comprimento de string na conversão para
   inteiro global do interpretador.

   Adicionado na versão 3.11.

PYTHONIOENCODING

   Se for definido antes de executar o interpretador, ele substitui a
   codificação usada para stdin/stdout/stderr, na sintaxe
   "encodingname:errorhandler". Ambas as partes "encodingname" e
   ":errorhandler" são opcionais e têm o mesmo significado que em
   "str.encode()".

   Para stderr, a parte ":errorhandler" é ignorada; o tratador sempre
   será "'backslashreplace'".

   Alterado na versão 3.4: A parte "encodingname" agora é opcional.

   Alterado na versão 3.6: No Windows, a codificação especificada por
   esta variável é ignorada para buffers de console interativo, a
   menos que "PYTHONLEGACYWINDOWSSTDIO" também seja especificado.
   Arquivos e canais redirecionados por meio de fluxos padrão não são
   afetados.

PYTHONNOUSERSITE

   Isso equivale a opção "-s". Se estiver definido, o Python não
   adicionará o "diretório site-packages do usuário" a "sys.path".

   Ver também: **PEP 370** -- Diretório site-packages por usuário.

PYTHONUSERBASE

   Define o "diretório base do usuário", que é usado para calcular o
   caminho do "diretório site-packages do usuário" e caminhos de
   instalação para "python -m pip install --user".

   Para desativar o diretório site-packages do usuário, consulte
   "PYTHONNOUSERSITE" ou a opção "-s".

   Ver também: **PEP 370** -- Diretório site-packages por usuário.

PYTHONEXECUTABLE

   Se esta variável de ambiente for definida, "sys.argv[0]" será
   definido com seu valor, em vez do valor obtido a partir do ambiente
   de execução C. Funciona apenas no macOS.

PYTHONWARNINGS

   Isso é equivalente à opção "-W". Se definido como uma string
   separada por vírgulas, é equivalente a especificar "-W" várias
   vezes, com os filtros posteriores na lista tendo precedência sobre
   os anteriores.

   As configurações mais simples aplicam uma determinada ação
   incondicionalmente a todos os avisos emitidos por um processo
   (mesmo aqueles que são ignorados por padrão):

      PYTHONWARNINGS=default  # Avisa uma vez por local de chamada
      PYTHONWARNINGS=error    # Converte para exceções
      PYTHONWARNINGS=always   # Avisa toda vez
      PYTHONWARNINGS=all      # Mesmo que PYTHONWARNINGS=always
      PYTHONWARNINGS=module   # Avisa uma vez por módulo chamador
      PYTHONWARNINGS=once     # Avisa uma vez por processo do Python
      PYTHONWARNINGS=ignore   # Nunca avisa

   Veja O filtro de avisos e Descrevendo filtros de aviso para mais
   detalhes.

   Alterado na versão 3.15: Adicionado suporte para expressão regular
   em *message* e *module*.

PYTHONFAULTHANDLER

   Se esta variável de ambiente for definida como uma string não
   vazia, "faulthandler.enable()" é chamado na inicialização: instala
   um tratador para os sinais "SIGSEGV", "SIGFPE", "SIGABRT", "SIGBUS"
   e "SIGILL" para despejar o traceback (situação da pilha de
   execução) do Python. Isso é equivalente à opção "-X"
   "faulthandler".

   Adicionado na versão 3.3.

PYTHONTRACEMALLOC

   Se esta variável de ambiente for definida como uma string não
   vazia, começa a rastrear as alocações de memória do Python usando o
   módulo "tracemalloc". O valor da variável é o número máximo de
   quadros armazenados em um traceback de um rastreamento. Por
   exemplo, "PYTHONTRACEMALLOC=1" armazena apenas o quadro mais
   recente. Veja a função "tracemalloc.start()" para mais informações.
   Isso é o equivalente a definir a opção "-X" "tracemalloc".

   Adicionado na versão 3.4.

PYTHONPROFILEIMPORTTIME

   Se esta variável de ambiente for definida como "1", o Python
   mostrará quanto tempo cada importação leva. Se definido como "2", o
   Python incluirá a saída para módulos importados que já foram
   carregados. Isso equivale a definir a opção "-X" "importtime".

   Adicionado na versão 3.7.

   Alterado na versão 3.14: Adicionado "PYTHONPROFILEIMPORTTIME=2"
   para também rastrear importações de módulos carregados.

PYTHONASYNCIODEBUG

   Se esta variável de ambiente for definida como uma string não
   vazia, habilita o modo de depuração do módulo "asyncio".

   Adicionado na versão 3.4.

PYTHONMALLOC

   Define os alocadores de memória do Python e/ou instala ganchos de
   depuração.

   Define a família de alocadores de memória usados pelo Python:

   * "default": usa os alocadores padrão de memória.

   * "malloc": usa a função "malloc()" da biblioteca C para todos os
     domínios ("PYMEM_DOMAIN_RAW", "PYMEM_DOMAIN_MEM",
     "PYMEM_DOMAIN_OBJ").

   * "pymalloc": usa o alocador pymalloc para domínios
     "PYMEM_DOMAIN_MEM" e "PYMEM_DOMAIN_OBJ" e usa a função "malloc()"
     para o domínio "PYMEM_DOMAIN_RAW".

   * "mimalloc": usa o alocador mimalloc para domínios
     "PYMEM_DOMAIN_MEM" e "PYMEM_DOMAIN_OBJ" e usa a função "malloc()"
     para o domínio "PYMEM_DOMAIN_RAW".

   Instala ganchos de depuração:

   * "debug": instala os ganchos de depuração sobre os alocadores de
     memória padrão.

   * "malloc_debug": o mesmo que "malloc", mas também instala ganchos
     de depuração.

   * "pymalloc_debug": o mesmo que "pymalloc", mas também instala
     ganchos de depuração.

   * "mimalloc_debug": o mesmo que "mimalloc", mas também instala
     ganchos de depuração.

   Nota:

     Na construção com *threads livres*, os valores "malloc",
     "malloc_debug", "pymalloc" e "pymalloc_debug" não são aceitos.
     Somente são aceitos "default", "debug", "mimalloc" e
     "mimalloc_debug".

   Adicionado na versão 3.6.

   Alterado na versão 3.7: Adicionado o alocador ""default"".

PYTHONMALLOCSTATS

   Se definido como uma string não vazia, o Python exibe estatísticas
   dos alocadores de memória pymalloc ou do mimalloc (o que estiver em
   uso) toda vez que uma nova arena de objeto é criada e ao
   desligamento.

   Esta variável é ignorada se a variável de ambiente "PYTHONMALLOC"
   for usada para forçar o alocador "malloc()" da biblioteca C, ou se
   Python estiver configurado sem suporte a "pymalloc" ou "mimalloc".

   Alterado na versão 3.6: Esta variável agora também pode ser usada
   em Python compilado no modo de lançamento. Agora não tem efeito se
   definido como uma string vazia.

PYTHON_PYMALLOC_HUGEPAGES

   Se definido como um valor inteiro diferente de zero, habilita o
   suporte a páginas enormes para as arenas pymalloc.  Defina como "0"
   ou não defina para desativar. Python deve ser compilado com "--
   with-pymalloc-hugepages" para que essa variável tenha efeito.

   Quando ativada, a alocação de arena usa "MAP_HUGETLB" (Linux) ou
   "MEM_LARGE_PAGES" (Windows) com retorno automático para páginas
   regulares se páginas enormes não estiverem disponíveis.

   Aviso:

     No Linux, se o pool de páginas enormes estiver esgotado, as
     falhas de página - inclusive as falhas de cópia na gravação
     acionadas por "os.fork()" - entregam "SIGBUS" e encerram o
     processo forçadamente. Só ative essa opção em ambientes em que o
     pool de páginas enormes tenha tamanho adequado e a segurança
     contra forks não seja uma preocupação.No Windows, você precisa de
     um privilégio especial. Consulte a documentação do Windows para
     páginas grandes para obter detalhes. Python falhará na
     inicialização se o privilégio necessário SeLockMemoryPrivilege
     não for concedido ao usuário.

   Adicionado na versão 3.15.

PYTHONLEGACYWINDOWSFSENCODING

   Se definido como uma string não vazia, o modo padrão do *tratador
   de erros e codificação do sistema de arquivos* irá reverter para
   seus valores pré-3.6 de "mbcs" e "replace", respectivamente. Caso
   contrário, os novos padrões "utf-8" e "surrogatepass" serão usados.

   Isso também pode ser habilitado em tempo de execução com
   "sys._enablelegacywindowsfsencoding()".

   Disponibilidade: Windows.

   Adicionado na versão 3.6: Veja **PEP 529** para mais detalhes.

PYTHONLEGACYWINDOWSSTDIO

   Se definido como uma string não vazia, não usa o novo leitor e
   escritor de console. Isso significa que os caracteres Unicode serão
   codificados de acordo com a página de código do console ativo, em
   vez de usar utf-8.

   Esta variável é ignorada se os fluxos padrão forem redirecionados
   (para arquivos ou canais) em vez de se referirem aos buffers do
   console.

   Disponibilidade: Windows.

   Adicionado na versão 3.6.

PYTHONCOERCECLOCALE

   Se definido como "0", faz com que a aplicação principal de linha de
   comando do Python ignore a coerção dos códigos de idioma legados C
   e POSIX baseados em ASCII para uma alternativa baseada em UTF-8
   mais capaz.

   Se esta variável *não* estiver definida (ou estiver definida para
   um valor diferente de "0"), a variável de ambiente de substituição
   de localidade "LC_ALL" também não será definida, e a localidade
   atual relatada para a categoria "LC_CTYPE" é a localidade "C"
   padrão, ou então a localidade "POSIX" explicitamente baseada em
   ASCII, então a CLI do Python tentará configurar as seguintes
   localidades para a categoria "LC_CTYPE" na ordem listada antes de
   carregar o ambiente de execução do interpretador:

   * "C.UTF-8"

   * "C.utf8"

   * "UTF-8"

   Se a configuração de uma dessas categorias de localidade for bem-
   sucedida, a variável de ambiente "LC_CTYPE" também será configurada
   de acordo no ambiente de processo atual antes que o ambiente de
   execução do Python seja inicializado. Isso garante que, além de ser
   visto pelo próprio interpretador e outros componentes com
   reconhecimento de localidade em execução no mesmo processo (como a
   biblioteca GNU "readline"), a configuração atualizada também é
   vista em subprocessos (independentemente ou não desses processos
   estarem executando um interpretador Python), bem como em operações
   que consultam o ambiente em vez da localidade C atual (como o
   "locale.getdefaultlocale()" do próprio Python).

   Configurar uma dessas localidades (explicitamente ou por meio da
   coerção de localidade implícita acima) habilita automaticamente o
   tratador de erros "surrogateescape" para "sys.stdin" e "sys.stdout"
   ("sys.stderr" continua a usar "backslashreplace", como em qualquer
   outra localidade). Este comportamento de tratamento de fluxo pode
   ser substituído usando "PYTHONIOENCODING" como de costume.

   Para fins de depuração, definir "PYTHONCOERCECLOCALE=warn" fará com
   que o Python emita mensagens de aviso em "stderr" se a coerção de
   localidade for ativada ou se uma localidade que *teria* acionado a
   coerção ainda estiver ativa quando o ambiente de execução do Python
   for inicializado.

   Observe também que, mesmo quando a coerção de localidade está
   desabilitada ou não consegue encontrar uma localidade de destino
   adequada, "PYTHONUTF8" ainda será ativado por padrão em localidades
   baseadas em ASCII legadas. Ambos os recursos devem ser
   desabilitados para forçar o interpretador a usar "ASCII" em vez de
   "UTF-8" nas interfaces de sistema.

   Disponibilidade: Unix.

   Adicionado na versão 3.7: Veja **PEP 538** para mais detalhes.

PYTHONDEVMODE

   Se esta variável de ambiente for definida como uma string não
   vazia, habilita Modo de Desenvolvimento do Python, introduzindo
   verificações adicionais em tempo de execução que são muito caras
   para serem habilitadas por padrão. Isso é o equivalente a definir a
   opção "-X" "dev".

   Adicionado na versão 3.7.

PYTHONUTF8

   Se definido para "1", habilita o modo UTF-8 do Python.

   Se definido para "0", desabilita o modo UTF-8 do Python.

   Definir qualquer outra string não vazia causa um erro durante a
   inicialização do interpretador.

   Adicionado na versão 3.7.

PYTHONWARNDEFAULTENCODING

   Se esta variável de ambiente for definida como uma string não
   vazia, emite uma "EncodingWarning" quando a codificação padrão
   específica da localidade é usada.

   Veja Ativar EncodingWarning para detalhes.

   Adicionado na versão 3.10.

PYTHONNODEBUGRANGES

   Se esta variável estiver definida, ela desabilita a inclusão das
   tabelas que mapeiam informações de localização extra (linha final,
   deslocamento da coluna inicial e deslocamento da coluna final) para
   cada instrução em objetos código. Isso é útil quando objetos código
   menores e arquivos pyc são desejados, bem como para suprimir os
   indicadores de localização visual extras quando o interpretador
   exibe tracebacks.

   Adicionado na versão 3.11.

PYTHONPERFSUPPORT

   Se essa variável for definida como um valor diferente de zero, ela
   habilitará o suporte ao perfilador do Linux "perf" para que as
   chamadas Python possam ser detectadas por ele.

   Se definido como "0", desativa o suporte ao perfilador do Linux
   "perf".

   Consulte também a opção de linha de comando "-X perf" e Python
   support for the perf map compatible profilers.

   Adicionado na versão 3.12.

PYTHON_PERF_JIT_SUPPORT

   Se essa variável for definida como um valor diferente de zero, ela
   habilitará o suporte do perfilador do Linux "perf" para que as
   chamadas Python possam ser detectadas por ele usando informações de
   DWARF.

   Se definido como "0", desativa o suporte ao perfilador do Linux
   "perf".

   Veja também a opção de linha de comando "-X perf_jit" e Python
   support for the perf map compatible profilers.

   Adicionado na versão 3.13.

PYTHON_DISABLE_REMOTE_DEBUG

   Se esta variável for definida como uma string não vazia, ela
   desabilitará o recurso de depuração remota descrito na **PEP 768**.
   Isso inclui tanto a funcionalidade de agendar código para execução
   em outro processo quanto a de receber código para execução no
   processo atual.

   Veja também a opção de linha de comando "-X disable-remote-debug".

   Adicionado na versão 3.14.

PYTHON_CPU_COUNT

   Se esta variável for definida como um número inteiro positivo, ela
   substituirá os valores de retorno de "os.cpu_count()" e
   "os.process_cpu_count()".

   Veja também a opção de linha de comando "-X cpu_count".

   Adicionado na versão 3.13.

PYTHON_FROZEN_MODULES

   Se esta variável for definida como "on" ou "off", ela determina se
   os módulos congelados serão ou não ignorados pelo maquinário de
   importação. Um valor "on" significa que eles serão importados e
   "off" significa que serão ignorados. O padrão é "on" para
   construções sem depuração (o caso normal) e "off" para construções
   com depuração. Observe que os módulos congelados
   "importlib_bootstrap" e "importlib_bootstrap_external" são sempre
   usados, mesmo que este sinalizador esteja definido como "off".

   Veja também a opção de linha de comando "-X frozen_modules".

   Adicionado na versão 3.13.

PYTHON_COLORS

   Se esta variável for definida como "1", o interpretador irá colorir
   vários tipos de saída. Definir como "0" desativa este
   comportamento. Veja também Controlando cores.

   Adicionado na versão 3.13.

PYTHON_BASIC_REPL

   Se esta variável for definida com qualquer valor, o interpretador
   não tentará carregar o *REPL* baseado em Python que requer
   "readline", e, em vez disso, usará o *REPL* com o analisador
   sintático tradicional.

   Adicionado na versão 3.13.

PYTHON_BASIC_COMPLETER

   Se essa variável for definida como qualquer valor, o PyREPL usará
   "rlcompleter" para implementar o auto-complemento com tab, em vez
   da padrão, que usa cores.

   Adicionado na versão 3.15.

PYTHON_HISTORY

   Esta variável de ambiente pode ser usada para definir a localização
   do arquivo ".python_history" (por padrão, ".python_history" está no
   diretório pessoal do usuário).

   Adicionado na versão 3.13.

PYTHON_GIL

   Se esta variável for definida como "1", a trava global do
   interpretador (GIL) será forçada. Definir como "0" força a GIL a
   desligar (precisa do Python configurado com a opção de construção "
   --disable-gil").

   Veja também a opção de linha de comando "-X gil", que tem
   precedência sobre esta variável, e CPython com threads livres.

   Adicionado na versão 3.13.

PYTHON_THREAD_INHERIT_CONTEXT

   Se esta variável for definida como "1", "Thread" usará, por padrão,
   uma cópia do contexto do chamador de "Thread.start()" ao iniciar.
   Caso contrário, novas threads serão iniciadas com um contexto
   vazio. Se não definida, esta variável assume como padrão "1" em
   construções com threads livres e "0" em outras. Veja também "-X
   thread_inherit_context".

   Adicionado na versão 3.14.

PYTHON_CONTEXT_AWARE_WARNINGS

   Se definido como "1", o gerenciador de contexto
   "warnings.catch_warnings" usará uma "ContextVar" para armazenar o
   estado do filtro de avisos. Se não for definido, o padrão desta
   variável será "1" em construções com threads livres e "0" em
   outras. Consulte "-X context_aware_warnings".

   Adicionado na versão 3.14.

PYTHON_PATHCONFIG_WARNINGS

   Se verdadeiro ("1"), então A inicialização do caminho de pesquisa
   de módulos sys.path tem permissão para registrar alertas em stderr.
   Se falso ("0"), suprime estes alertas. Definido como verdadeiro por
   padrão. Veja também "-X pathconfig_warnings".

   Adicionado na versão 3.15.

PYTHON_JIT

   Em construções em que a compilação experimental just-in-time está
   disponível, esta variável pode forçar o JIT a ser desabilitado
   ("0") ou habilitado ("1") na inicialização do interpretador.

   Adicionado na versão 3.13.

PYTHON_TLBC

   Se definido como "1", habilita o bytecode local da thread. Se
   definido como "0", o bytecode local da thread e o interpretador
   especializado são desabilitados. Aplica-se somente a construções
   configuradas com "--disable-gil".

   Veja também a opção de linha de comando "-X tlbc".

   Adicionado na versão 3.14.

PYTHON_LAZY_IMPORTS

   Controla o comportamento da importação preguiçosa. Aceita dois
   valores: "all" torna todas as importações preguiçosas por padrão, e
   "normal" (o padrão) respeita a palavra-chave "lazy" no código-
   fonte.

   Veja também a opção de linha de comando  "-X lazy_imports" .

   Adicionado na versão 3.15.


1.2.1. Variáveis de modo de depuração
-------------------------------------

PYTHONDUMPREFS

   Se definido, Python irá despejar objetos e contagens de referências
   ainda vivas após desligar o interpretador.

   Precisa do Python configurado com a opção de construção "--with-
   trace-refs".

PYTHONDUMPREFSFILE

   Se definido, o Python irá despejar objetos e contagens de
   referências ainda ativas após desligar o interpretador em um
   arquivo no caminho fornecido como valor desta variável de ambiente.

   Precisa do Python configurado com a opção de construção "--with-
   trace-refs".

   Adicionado na versão 3.11.

PYTHON_PRESITE

   Se esta variável for definida como um módulo, esse módulo será
   importado no início do ciclo de vida do interpretador, antes do
   módulo "site" ser executado, e antes do módulo "__main__" ser
   criado. Portanto, o módulo importado não é tratado como "__main__".

   Isso pode ser usado para executar código antecipadamente durante a
   inicialização do Python.

   Para importar um submódulo, use "pacote.módulo" como valor, como em
   uma instrução de importação.

   Veja também a opção de linha de comando "-X presite", que tem
   precedência sobre esta variável.

   Precisa do Python configurado com a opção de construção "--with-
   pydebug".

   Alterado na versão 3.15: Aceita também o formato "módulo:função"
   como ponto de entrada.

   Adicionado na versão 3.13.
