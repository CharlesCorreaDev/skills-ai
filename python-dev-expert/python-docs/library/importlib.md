"importlib" --- A implementação de "import"
*******************************************

Adicionado na versão 3.1.

**Código-fonte:** Lib/importlib/__init__.py

======================================================================


Introdução
==========

The purpose of the "importlib" package is three-fold.

Uma é fornecer a implementação da instrução "import" (e, portanto, por
extensão, a função "__import__()") no código-fonte Python. Isso
fornece uma implementação de "import" que é portável para qualquer
interpretador Python. Isso também fornece uma implementação que é mais
fácil de compreender do que aquela implementada em uma linguagem de
programação diferente do Python.

Dois, os componentes para implementar "import" são expostos neste
pacote, tornando mais fácil para os usuários criarem seus próprios
objetos personalizados (conhecidos genericamente como *importador*)
para participar do processo de importação.

Terceiro, o pacote contém módulos que expõem funcionalidades
adicionais para gerenciar aspectos de pacotes Python:

* "importlib.metadata" apresenta acesso a metadados de distribuições
  de terceiros.

* "importlib.resources" fornece rotinas para acessar "recursos" não
  codificados de pacotes Python.

Ver também:

  A instrução import
     A referência da linguagem para a instrução "import".

  Especificação dos pacotes
     Especificação original dos pacotes. Algumas semânticas mudaram
     desde a redação deste documento (por exemplo, redirecionamento
     baseado em "None" em "sys.modules").

  A função "__import__()"
     A instrução "import" é um açúcar sintático para esta função.

  A inicialização do caminho de pesquisa de módulos sys.path
     A inicialização de "sys.path".

  **PEP 235**
     Importação em plataformas que diferenciam maiúsculo de minúsculo

  **PEP 263**
     Definindo codificações do código-fonte do Python

  **PEP 302**
     Novos ganchos de importação

  **PEP 328**
     Importações: Multilinha e Absoluto/Relativo

  **PEP 366**
     Importações relativas explícitas do módulo principal

  **PEP 420**
     Pacotes de espaço de nomes implícitos

  **PEP 451**
     Um tipo de ModuleSpec para o sistema de importação

  **PEP 488**
     Eliminação de arquivos PYO

  **PEP 489**
     Inicialização de módulo extensão multifase

  **PEP 552**
     pycs determinísticos

  **PEP 3120**
     Usando UTF-8 como fonte padrão de codificação

  **PEP 3147**
     Diretórios de repositório de PYC


Funções
=======

importlib.__import__(name, globals=None, locals=None, fromlist=(), level=0)

   Uma implementação da função embutida "__import__()".

   Nota:

     A importação programática de módulos deve usar "import_module()"
     em vez desta função.

importlib.import_module(name, package=None)

   Importa um módulo. O argumento *name* especifica qual módulo
   importar em termos absolutos ou relativos (por exemplo, "pkg.mod"
   ou "..mod"). Se o nome for especificado em termos relativos, então
   o argumento *package* deve ser definido como o nome do pacote que
   atuará como âncora para resolver o nome do pacote (por exemplo,
   "import_module('..mod', 'pkg.subpkg')" importará "pkg.mod").

   A função "import_module()" atua como um wrapper simplificador em
   torno de "importlib.__import__()". Isso significa que toda a
   semântica da função é derivada de "importlib.__import__()". A
   diferença mais importante entre essas duas funções é que
   "import_module()" retorna o pacote ou módulo especificado (por
   exemplo, "pkg.mod"), enquanto "__import__()" retorna o pacote ou
   módulo de nível superior (por exemplo, "pkg").

   Se você estiver importando dinamicamente um módulo que foi criado
   desde que o interpretador iniciou a execução (por exemplo, criou um
   arquivo fonte Python), você pode precisar chamar
   "invalidate_caches()" para que o novo módulo seja notado pelo
   sistema de importação.

   If the module cannot be imported, "import_module()" will raise
   "ImportError" or an appropriate subclass like
   "ModuleNotFoundError".

   Alterado na versão 3.3: Os pacotes pai são importados
   automaticamente.

importlib.invalidate_caches()

   Invalida os caches internos dos localizadores armazenados em
   "sys.meta_path". Se um localizador implementar
   "invalidate_caches()" então ele será chamado para realizar a
   invalidação. Esta função deve ser chamada se algum módulo for
   criado/instalado enquanto seu programa estiver em execução para
   garantir que todos os localizadores notarão a existência do novo
   módulo.

   Adicionado na versão 3.3.

   Alterado na versão 3.10: Pacotes de espaço de nomes
   criados/instalados em um local "sys.path" diferente após o mesmo
   espaço de nomes já ter sido importado são notados.

importlib.reload(module)

   Recarrega um *module* importado anteriormente. O argumento deve ser
   um objeto módulo, portanto deve ter sido importado com êxito antes.
   Isso é útil se você editou o arquivo fonte do módulo usando um
   editor externo e deseja experimentar a nova versão sem sair do
   interpretador Python. O valor de retorno é o objeto módulo (que
   pode ser diferente se a reimportação fizer com que um objeto
   diferente seja colocado em "sys.modules").

   Quando "reload()" é executado:

   * O código do módulo Python é recompilado e o código em nível de
     módulo é reexecutado, definindo um novo conjunto de objetos que
     são vinculados a nomes no dicionário do módulo reutilizando o
     *carregador* que originalmente carregou o módulo. A função "init"
     dos módulos de extensão não é chamada uma segunda vez.

   * Tal como acontece com todos os outros objetos em Python, os
     objetos antigos só são recuperados depois que suas contagens de
     referências caem para zero.

   * Os nomes no espaço de nomes do módulo são atualizados para
     apontar para quaisquer objetos novos ou alterados.

   * Outras referências aos objetos antigos (como nomes externos ao
     módulo) não são religadas para se referir aos novos objetos e
     devem ser atualizadas em cada espaço de nomes onde ocorrem, se
     isso for desejado.

   Existem várias outras ressalvas:

   Quando um módulo é recarregado, seu dicionário (contendo as
   variáveis globais do módulo) é retido. As redefinições de nomes vão
   substituir as definições antigas, portanto isso geralmente não é um
   problema. Se a nova versão de um módulo não definir um nome
   definido pela versão antiga, a definição antiga permanecerá. Este
   recurso pode ser usado para vantagem do módulo se ele mantiver uma
   tabela global ou cache de objetos -- com uma instrução "try" ele
   pode testar a presença da tabela e pular sua inicialização se
   desejar:

      try:
          cache
      except NameError:
          cache = {}

   Geralmente não é muito útil recarregar módulos embutidos ou
   carregados dinamicamente. Recarregar "sys", "__main__", "builtins"
   e outros módulos principais não é recomendado. Em muitos casos, os
   módulos de extensão não são projetados para serem inicializados
   mais de uma vez e podem falhar de maneiras arbitrárias quando
   recarregados.

   Se um módulo importa objetos de outro módulo usando "from" ...
   "import" ..., chamar "reload()" para o outro módulo não redefine os
   objetos importados dele -- uma maneira de contornar isso é executar
   novamente a instrução "from", outra é usar "import" e nomes
   qualificados (*module.name*).

   Se um módulo instancia instâncias de uma classe, recarregar o
   módulo que define a classe não afeta as definições de método das
   instâncias -- elas continuam a usar a definição de classe antiga. O
   mesmo se aplica às classes derivadas.

   Adicionado na versão 3.4.

   Alterado na versão 3.7: "ModuleNotFoundError" é levantada quando o
   módulo que está sendo recarregado não possui um "ModuleSpec".

   Aviso:

     This function is not thread-safe. Calling it from multiple
     threads can result in unexpected behavior. It's recommended to
     use the "threading.Lock" or other synchronization primitives for
     thread-safe module reloading.


"importlib.abc" -- Abstract base classes related to import
==========================================================

**Código-fonte:** Lib/importlib/abc.py

======================================================================

The "importlib.abc" module contains all of the core abstract base
classes used by "import". Some subclasses of the core abstract base
classes are also provided to help in implementing the core ABCs.

Hierarquia de ABC:

   object
    +-- MetaPathFinder
    +-- PathEntryFinder
    +-- Loader
         +-- ResourceLoader --------+
         +-- InspectLoader          |
              +-- ExecutionLoader --+
                                    +-- FileLoader
                                    +-- SourceLoader

class importlib.abc.MetaPathFinder

   Uma classe base abstrata que representa um *localizador de
   metacaminho*.

   Adicionado na versão 3.3.

   Alterado na versão 3.10: Não é mais uma subclasse de "Finder".

   find_spec(fullname, path, target=None)

      Um método abstrato para encontrar um *spec* para o módulo
      especificado. Se esta for uma importação de nível superior,
      *path* será "None". Caso contrário, esta é uma busca por um
      subpacote ou módulo e *path* será o valor de "__path__" do
      pacote pai. Se um spec não puder ser encontrado, "None" será
      retornado. Quando passado, "target" é um objeto de módulo que o
      localizador pode usar para fazer uma estimativa mais informada
      sobre qual spec retornar. "importlib.util.spec_from_loader()"
      pode ser útil para implementar "MetaPathFinders" concretos.

      Adicionado na versão 3.4.

   invalidate_caches()

      Um método opcional que, quando chamado, deve invalidar qualquer
      cache interno usado pelo localizador. Usado por
      "importlib.invalidate_caches()" ao invalidar os caches de todos
      os localizadores em "sys.meta_path".

      Alterado na versão 3.4: Retorna "None" quando chamado em vez de
      "NotImplemented".

   discover(parent=None)

      An optional method which searches for possible specs with given
      *parent* module spec. If *parent* is *None*,
      "MetaPathFinder.discover()" will search for top-level modules.

      Returns an iterable of possible specs.

      Raises "ValueError" if *parent* is not a package module.

      Aviso:

        This method can potentially yield a very large number of
        objects, and it may carry out IO operations when computing
        these values.Because of this, it will generally be desirable
        to compute the result values on-the-fly, as they are needed.
        As such, the returned object is only guaranteed to be an
        "iterable", instead of a "list" or other "collection" type.

      Adicionado na versão 3.15.

class importlib.abc.PathEntryFinder

   Uma classe base abstrata que representa um *localizador de entrada
   de caminho*. Embora tenha algumas semelhanças com "MetaPathFinder",
   "PathEntryFinder" deve ser usado apenas dentro do subsistema de
   importação baseado em caminho fornecido por
   "importlib.machinery.PathFinder".

   Adicionado na versão 3.3.

   Alterado na versão 3.10: Não é mais uma subclasse de "Finder".

   find_spec(fullname, target=None)

      Um método abstrato para encontrar um *spec* para o módulo
      especificado. O localizador irá procurar pelo módulo apenas
      dentro do *entrada de caminho* ao qual ele está atribuído. Se um
      spec não puder ser encontrado, "None" será retornado. Quando
      passado, "target" é um objeto de módulo que o localizador pode
      usar para fazer uma estimativa mais informada sobre qual spec
      retornar. "importlib.util.spec_from_loader()" pode ser útil para
      implementar "PathEntryFinders" concretos.

      Adicionado na versão 3.4.

   invalidate_caches()

      Um método opcional que, quando chamado, deve invalidar qualquer
      cache interno usado pelo localizador. Usado por
      "importlib.machinery.PathFinder.invalidate_caches()" ao
      invalidar os caches de todos os localizadores em cache.

   discover(parent=None)

      An optional method which searches for possible specs with given
      *parent* module spec. If *parent* is *None*,
      "PathEntryFinder.discover()" will search for top-level modules.

      Returns an iterable of possible specs.

      Raises "ValueError" if *parent* is not a package module.

      Aviso:

        This method can potentially yield a very large number of
        objects, and it may carry out IO operations when computing
        these values.Because of this, it will generally be desirable
        to compute the result values on-the-fly, as they are needed.
        As such, the returned object is only guaranteed to be an
        "iterable", instead of a "list" or other "collection" type.

      Adicionado na versão 3.15.

class importlib.abc.Loader

      Uma classe base abstrata para um *carregador*. Veja **PEP 302**
      para a definição exata de um carregador.

      Loaders that wish to support resource reading should implement a
      "get_resource_reader()" method as specified by
      "importlib.resources.abc.ResourceReader".

      Alterado na versão 3.7: Introduced the optional
      "get_resource_reader()" method.

   Alterado na versão 3.15: Removed the "load_module()" method.

   create_module(spec)

      Um método que retorna o objeto do módulo a ser usado ao importar
      um módulo. Este método pode retornar "None", indicando que a
      semântica padrão de criação do módulo deve ocorrer.

      Adicionado na versão 3.4.

      Alterado na versão 3.6: Este método não é mais opcional quando
      "exec_module()" é definido.

   exec_module(module)

      Um método abstrato que executa o módulo em seu próprio espaço de
      nomes quando um módulo é importado ou recarregado. O módulo já
      deve estar inicializado quando "exec_module()" for chamado.
      Quando este método existir, "create_module()" deve ser definido.

      Adicionado na versão 3.4.

      Alterado na versão 3.6: "create_module()" deve ser definido.

class importlib.abc.ResourceLoader

   *Substituída por TraversableResources*

      Uma classe base abstrata para um *carregador* que implementa o
      protocolo opcional **PEP 302** para carregar recursos
      arbitrários do back-end de armazenamento.

      Descontinuado desde a versão 3.7: This ABC is deprecated in
      favour of supporting resource loading through
      "importlib.resources.abc.TraversableResources". This class
      exists for backwards compatibility only with other ABCs in this
      module.

      abstractmethod get_data(path)

            Um método abstrato para retornar os bytes dos dados
            localizados em *path*. Carregadores que possuem um backend
            de armazenamento arquivo ou similar que permite o
            armazenamento de dados arbitrários podem implementar esse
            método abstrato para fornecer acesso direto aos dados
            armazenados. "OSError" deve ser levantada se o *path* não
            puder ser encontrado. Espera-se que o *path* seja
            construído usando o atributo "__file__" de um módulo ou um
            item de "__path__" de um pacote.

            Alterado na versão 3.4: Levanta "OSError" em vez de
            "NotImplementedError".

class importlib.abc.InspectLoader

   Uma classe base abstrata para um *carregador* que implementa o
   protocolo opcional da **PEP 302** para carregadores que inspecionam
   módulos.

   get_code(fullname)

      Retorna o objeto de código para um módulo, ou "None" se o módulo
      não tiver um objeto código (como seria o caso, por exemplo, para
      um módulo embutido). Levanta um "ImportError" se o carregador
      não conseguir encontrar o módulo solicitado.

      Nota:

        Embora o método tenha uma implementação padrão, sugere-se que
        ele seja substituído, se possível, para desempenho.

      Alterado na versão 3.4: Não é mais abstrato e uma implementação
      concreta é fornecida.

   abstractmethod get_source(fullname)

         Um método abstrato para retornar a fonte de um módulo. Ele é
         retornado como uma string de texto usando *novas linhas
         universais*, traduzindo todos os separadores de linha
         reconhecidos em caracteres "'\n'". Retorna "None" se nenhuma
         fonte estiver disponível (por exemplo, um módulo embutido).
         Levanta "ImportError" se o carregador não puder encontrar o
         módulo especificado.

         Alterado na versão 3.4: Levanta "ImportError" em vez de
         "NotImplementedError".

   is_package(fullname)

      Um método opcional para retornar um valor verdadeiro se o módulo
      for um pacote, um valor falso caso contrário. "ImportError" é
      levantada se o *carregador* não puder encontrar o módulo.

      Alterado na versão 3.4: Levanta "ImportError" em vez de
      "NotImplementedError".

   static source_to_code(data, path='<string>', fullname=None)

      Cria um objeto código a partir de código-fonte Python

      O argumento *data* pode ser qualquer coisa a qual a função
      "compile()" tenha suporte (por exemplo, string ou bytes). O
      argumento *path* deve ser o "caminho" de onde o código-fonte se
      originou, o que pode ser um conceito abstrato (por exemplo,
      local em um arquivo zip).

      Com o objeto de código subsequente, é possível executá-lo em um
      módulo executando "exec(code, module.__dict__)".

      The optional argument *fullname* specifies the module name. It
      is needed to unambiguous filter syntax warnings by module name.

      Adicionado na versão 3.4.

      Alterado na versão 3.5: O método foi tornado estático.

      Adicionado na versão 3.15: Added the *fullname* parameter.

   exec_module(module)

      Implementação de "Loader.exec_module()".

      Adicionado na versão 3.4.

class importlib.abc.ExecutionLoader

   Uma classe base abstrata que herda de "InspectLoader" que, quando
   implementada, ajuda um módulo a ser executado como um script. A ABC
   representa um protocolo opcional da **PEP 302**.

   abstractmethod get_filename(fullname)

         Um método abstrato que deve retornar o valor de "__file__"
         para o módulo especificado. Se nenhum caminho estiver
         disponível, "ImportError" é levantada.

         Se o código-fonte estiver disponível, o método deverá
         retornar o caminho para o arquivo fonte, independentemente de
         um bytecode ter sido usado para carregar o módulo.

         Alterado na versão 3.4: Levanta "ImportError" em vez de
         "NotImplementedError".

class importlib.abc.FileLoader(fullname, path)

   Uma classe base abstrata que herda de "ResourceLoader" e
   "ExecutionLoader", fornecendo implementações concretas de
   "ResourceLoader.get_data()" e "ExecutionLoader.get_filename()".

   O argumento *fullname* é um nome totalmente resolvido do módulo que
   o carregador deve manipular. O argumento *path* é o caminho para o
   arquivo do módulo.

   Adicionado na versão 3.3.

   Alterado na versão 3.15: Removed the "load_module()" method.

   name

      O nome do módulo que o carregador pode manipular.

   path

      Caminho para o arquivo do módulo

   abstractmethod get_filename(fullname)

      Retorna "path".

   abstractmethod get_data(path)

      Lê *caminho* como um arquivo binário e retorna os bytes dele.

class importlib.abc.SourceLoader

   Uma classe base abstrata para implementar o carregamento de arquivo
   fonte (e opcionalmente bytecode). A classe herda de
   "ResourceLoader" e "ExecutionLoader", exigindo a implementação de:

   * "ResourceLoader.get_data()"

   * "ExecutionLoader.get_filename()"
        Deve retornar apenas o caminho para o arquivo fonte; o
        carregamento sem fonte não é suportado.

   Os métodos abstratos definidos por esta classe são para adicionar
   suporte opcional ao arquivo bytecode. Não implementar esses métodos
   opcionais (ou fazer com que eles levantem "NotImplementedError")
   faz com que o carregador funcione apenas com código-fonte.
   Implementar os métodos permite que o carregador funcione com
   arquivos de código-fonte *e* bytecode; ele não permite carregamento
   *sem fonte* onde apenas o bytecode é fornecido. Arquivos de
   bytecode são uma otimização para acelerar o carregamento removendo
   a etapa de análise do compilador do Python e, portanto, nenhuma API
   específica de bytecode é exposta.

   Alterado na versão 3.15: Removed the "load_module()" method.

   path_stats(path)

      Método abstrato opcional que retorna um "dict" contendo
      metadados sobre o caminho especificado. As chaves de dicionário
      suportadas são:

      * "'mtime'" (obrigatório): um número inteiro ou de ponto
        flutuante que representa o tempo de modificação do código-
        fonte;

      * "'size'" (opcional): o tamanho em bytes do código-fonte.

      Quaisquer outras chaves no dicionário são ignoradas, para
      permitir extensões futuras. Se o caminho não puder ser
      manipulado, "OSError" é levantada.

      Adicionado na versão 3.3.

      Alterado na versão 3.4: Levanta "OSError" em vez de
      "NotImplementedError".

   path_mtime(path)

      Método abstrato opcional que retorna o horário de modificação do
      caminho especificado.

      Descontinuado desde a versão 3.3: Este método foi descontinuado
      em favor de "path_stats()". Você não precisa implementá-lo, mas
      ele ainda está disponível para fins de compatibilidade. Levanta
      "OSError" se o caminho não puder ser manipulado.

      Alterado na versão 3.4: Levanta "OSError" em vez de
      "NotImplementedError".

   set_data(path, data)

      Método abstrato opcional que grava os bytes especificados em um
      caminho de arquivo. Quaisquer diretórios intermediários que não
      existam devem ser criados automaticamente.

      Quando a gravação no caminho falhar porque o caminho é somente
      leitura ("errno.EACCES"/"PermissionError"), não propaga a
      exceção.

      Alterado na versão 3.4: Não mais levanta "NotImplementedError"
      quando chamado.

   get_code(fullname)

      Implementação concreta de "InspectLoader.get_code()".

   exec_module(module)

      Implementação concreta de "Loader.exec_module()".

      Adicionado na versão 3.4.

   get_source(fullname)

      Implementação concreta de "InspectLoader.get_source()".

   is_package(fullname)

      Implementação concreta de "InspectLoader.is_package()". Um
      módulo é determinado como um pacote se seu caminho de arquivo
      (conforme fornecido por "ExecutionLoader.get_filename()") for um
      arquivo chamado "__init__" quando a extensão do arquivo for
      removida **e** o nome do módulo em si não terminar em
      "__init__".


"importlib.machinery" -- Importers and path hooks
=================================================

**Código-fonte:** Lib/importlib/machinery.py

======================================================================

Este módulo contém vários objetos que ajudam o "import" a localizar e
carregar módulos.

importlib.machinery.SOURCE_SUFFIXES

   Uma lista de strings representando os sufixos de arquivo
   reconhecidos para módulos em código-fonte.

   Adicionado na versão 3.3.

importlib.machinery.DEBUG_BYTECODE_SUFFIXES

   Uma lista de strings representando os sufixos de arquivo para
   módulos em bytecode não otimizado.

   Adicionado na versão 3.3.

   Descontinuado desde a versão 3.5: Use "BYTECODE_SUFFIXES" instead.

importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES

   Uma lista de strings representando os sufixos de arquivo para
   módulos em bytecode otimizado.

   Adicionado na versão 3.3.

   Descontinuado desde a versão 3.5: Use "BYTECODE_SUFFIXES" instead.

importlib.machinery.BYTECODE_SUFFIXES

   Uma lista de strings representando os sufixos de arquivo
   reconhecidos para módulos em bytecode (incluindo com ponto no
   início).

   Adicionado na versão 3.3.

   Alterado na versão 3.5: O valor não mais depende de "__debug__".

importlib.machinery.EXTENSION_SUFFIXES

   Uma lista de strings representando os sufixos de arquivo
   reconhecidos para módulos de extensão.

   Adicionado na versão 3.3.

importlib.machinery.all_suffixes()

   Retorna uma lista combinada de strings representando todos os
   sufixos de arquivo para módulos reconhecidos pelo maquinário de
   importação padrão. Este é um auxiliar para código que simplesmente
   precisa saber se um caminho de sistema de arquivos potencialmente
   se refere a um módulo sem precisar de detalhes sobre o tipo de
   módulo (por exemplo, "inspect.getmodulename()").

   Adicionado na versão 3.3.

class importlib.machinery.BuiltinImporter

   Um *importador* para módulos embutidos. Todos os módulos embutidos
   conhecidos estão listados em "sys.builtin_module_names". Esta
   classe implementa os ABCs "importlib.abc.MetaPathFinder" e
   "importlib.abc.InspectLoader".

   Somente métodos de classe são definidos por esta classe para
   aliviar a necessidade de instanciação.

   Alterado na versão 3.5: As part of **PEP 489**, the builtin
   importer now implements "Loader.create_module" and
   "Loader.exec_module"

class importlib.machinery.FrozenImporter

   Um *importador* para módulos congelados. Esta classe implementa os
   ABCs "importlib.abc.MetaPathFinder" e
   "importlib.abc.InspectLoader".

   Somente métodos de classe são definidos por esta classe para
   aliviar a necessidade de instanciação.

   Alterado na versão 3.4: Gained "create_module()" and
   "exec_module()" methods.

class importlib.machinery.WindowsRegistryFinder

   *Localizador* para módulos declarados no registro do Windows. Esta
   classe implementa a ABC "importlib.abc.MetaPathFinder".

   Somente métodos de classe são definidos por esta classe para
   aliviar a necessidade de instanciação.

   Adicionado na versão 3.3.

   Descontinuado desde a versão 3.6: Use a configuração de "site" em
   vez disso. Versões futuras do Python podem não habilitar esse
   localizador por padrão.

class importlib.machinery.PathFinder

   Um *Localizador* para atributos "sys.path" e pacote "__path__".
   Esta classe implementa a ABC "importlib.abc.MetaPathFinder".

   Somente métodos de classe são definidos por esta classe para
   aliviar a necessidade de instanciação.

   classmethod find_spec(fullname, path=None, target=None)

      Método de classe que tenta encontrar um *spec* para o módulo
      especificado por *fullname* em "sys.path" ou, se definido, em
      *path*. Para cada entrada de caminho pesquisada,
      "sys.path_importer_cache" é verificado. Se um objeto não falso
      for encontrado, ele será usado como o *localizador de entrada de
      caminho* para procurar o módulo que está sendo pesquisado. Se
      nenhuma entrada for encontrada em "sys.path_importer_cache",
      então "sys.path_hooks" será pesquisado para um localizador para
      a entrada de caminho e, se encontrado, será armazenado em
      "sys.path_importer_cache" junto com a consulta sobre o módulo.
      Se nenhum localizador for encontrado, então "None" será
      armazenado no cache e retornado.

      Adicionado na versão 3.4.

      Alterado na versão 3.5: Se o diretório de trabalho atual —
      representado por uma string vazia — não for mais válido, "None"
      será retornado, mas nenhum valor será armazenado em cache em
      "sys.path_importer_cache".

   classmethod invalidate_caches()

      Chama "importlib.abc.PathEntryFinder.invalidate_caches()" em
      todos os localizadores armazenados em "sys.path_importer_cache"
      que definem o método. Caso contrário, as entradas em
      "sys.path_importer_cache" definidas como "None" são excluídas.

      Alterado na versão 3.7: Entradas de "None" em
      "sys.path_importer_cache" são excluídas.

   Alterado na versão 3.4: Chama objetos em "sys.path_hooks" com o
   diretório de trabalho atual para "''" (ou seja, a string vazia).

class importlib.machinery.FileFinder(path, *loader_details)

   Uma implementação concreta de "importlib.abc.PathEntryFinder" que
   armazena em cache os resultados do sistema de arquivos.

   O argumento *path* é o diretório que o localizador é responsável
   por pesquisar.

   O argumento *loader_details* é um número variável de tuplas de 2
   itens, cada uma contendo um carregador e uma sequência de sufixos
   de arquivo que o carregador reconhece. Espera-se que os
   carregadores sejam chamáveis que aceitam dois argumentos do nome do
   módulo e o caminho para o arquivo encontrado.

   O localizador armazenará em cache o conteúdo do diretório conforme
   necessário, fazendo chamadas de "stat" para cada pesquisa de módulo
   para verificar se o cache não está desatualizado. Como a
   obsolescência do cache depende da granularidade das informações de
   estado do sistema operacional do sistema de arquivos, há uma
   condição de corrida potencial de busca por um módulo, criação de um
   novo arquivo e, em seguida, busca pelo módulo que o novo arquivo
   representa. Se as operações ocorrerem rápido o suficiente para
   caber na granularidade das chamadas de "stat", a pesquisa do módulo
   falhará. Para evitar que isso aconteça, ao criar um módulo
   dinamicamente, certifique-se de chamar
   "importlib.invalidate_caches()".

   Adicionado na versão 3.3.

   path

      O caminho que o localizador irá procurar.

   find_spec(fullname, target=None)

      Tenta encontrar o spec para manipular *fullname* dentro de
      "path".

      Adicionado na versão 3.4.

   invalidate_caches()

      Limpa o cache interno.

   classmethod path_hook(*loader_details)

      Um método de classe que retorna uma clausura para uso em
      "sys.path_hooks". Uma instância de "FileFinder" é retornada pela
      clausura usando o argumento de caminho dado à clausura
      diretamente e *loader_details* indiretamente.

      Se o argumento para a clausura não for um diretório existente,
      "ImportError" será levantada.

class importlib.machinery.NamespacePath(name, path, path_finder)

   Represents a *namespace package*'s path ("module.__path__").

   When its "__path__" value is accessed it will be recomputed if
   necessary. This keeps it in-sync with the global state
   ("sys.modules").

   The *name* argument is the name of the namespace module.

   The *path* argument is the initial path value.

   The *path_finder* argument is the callable used to recompute the
   path value. The callable has the same signature as
   "importlib.abc.MetaPathFinder.find_spec()".

   When the parent's "module.__path__" attribute is updated, the path
   value is recomputed.

   If the parent module is missing from "sys.modules", then
   "ModuleNotFoundError" will be raised.

   For top-level modules, the parent module's path is "sys.path".

   Nota:

     "PathFinder.invalidate_caches()" invalidates "NamespacePath",
     forcing the path value to be recomputed next time it is accessed.

   Adicionado na versão 3.15.

class importlib.machinery.SourceFileLoader(fullname, path)

   Uma implementação concreta de "importlib.abc.SourceLoader"
   subclassificando "importlib.abc.FileLoader" e fornecendo algumas
   implementações concretas de outros métodos.

   Adicionado na versão 3.3.

   Alterado na versão 3.15: Removed the "load_module()" method.

   name

      O nome do módulo que este carregador irá manipular.

   path

      O caminho para o arquivo fonte.

   is_package(fullname)

      Retorna "True" se "path" parecer ser para um pacote.

   path_stats(path)

      Implementação concreta de
      "importlib.abc.SourceLoader.path_stats()".

   set_data(path, data)

      Implementação concreta de
      "importlib.abc.SourceLoader.set_data()".

class importlib.machinery.SourcelessFileLoader(fullname, path)

   Uma implementação concreta de "importlib.abc.FileLoader" que pode
   importar arquivos de bytecode (ou seja, não existem arquivos de
   código-fonte).

   Observe que o uso direto de arquivos de bytecode (e, portanto, não
   de arquivos de código-fonte) impede que seus módulos sejam
   utilizáveis por todas as implementações do Python ou novas versões
   do Python que alteram o formato do bytecode.

   Adicionado na versão 3.3.

   Alterado na versão 3.15: Removed the "load_module()" method.

   name

      O nome do módulo que o carregador vai manipular.

   path

      O caminho para o arquivo de bytecode.

   is_package(fullname)

      Determina se o módulo é um pacote baseado em "path".

   get_code(fullname)

      Retorna o objeto código para "name" criado a partir de "path".

   get_source(fullname)

      Retorna "None", pois os arquivos de bytecode não têm código-
      fonte quando este carregador é usado.

class importlib.machinery.ExtensionFileLoader(fullname, path)

   Uma implementação concreta de "importlib.abc.ExecutionLoader" para
   módulos de extensão.

   O argumento *fullname* especifica o nome do módulo ao qual o
   carregador deve dar suporte. O argumento *path* é o caminho para o
   arquivo do módulo de extensão.

   Observe que, por padrão, a importação de um módulo de extensão
   falhará em subinterpretadores se ele não implementar inicialização
   multifásica (consulte a **PEP 489**), mesmo que ele seja importado
   com sucesso.

   Adicionado na versão 3.3.

   Alterado na versão 3.12: A inicialização multifásica agora é
   necessária para uso em subinterpretadores.

   name

      Nome do módulo ao qual o carregador dá suporte.

   path

      Caminho para o módulo de extensão.

   create_module(spec)

      Cria o objeto do módulo a partir da especificação fornecida de
      acordo com a **PEP 489**.

      Adicionado na versão 3.5.

   exec_module(module)

      Inicializa o objeto do módulo fornecido de acordo com a **PEP
      489**.

      Adicionado na versão 3.5.

   is_package(fullname)

      Returns "True" if the file path points to a package's "__init__"
      module based on "EXTENSION_SUFFIXES".

   get_code(fullname)

      Retorna "None", pois os módulos de extensão não possuem um
      objeto código.

   get_source(fullname)

      Retorna "None" pois os módulos de extensão não possuem código-
      fonte.

   get_filename(fullname)

      Retorna "path".

      Adicionado na versão 3.4.

class importlib.machinery.NamespaceLoader(name, path, path_finder)

   Uma implementação concreta de "importlib.abc.InspectLoader" para
   pacotes de espaço de nomes. Este é um apelido para uma classe
   privada e só é tornado público para introspecção do atributo
   "__loader__" em pacotes de espaço de nomes:

      >>> from importlib.machinery import NamespaceLoader
      >>> import my_namespace
      >>> isinstance(my_namespace.__loader__, NamespaceLoader)
      True
      >>> import importlib.abc
      >>> isinstance(my_namespace.__loader__, importlib.abc.Loader)
      True

   Adicionado na versão 3.11.

class importlib.machinery.ModuleSpec(name, loader, *, origin=None, loader_state=None, is_package=None)

   A specification for a module's import-system-related state.  This
   is typically exposed as the module's "__spec__" attribute.  Many of
   these attributes are also available directly on a module: for
   example, "module.__spec__.origin == module.__file__".  Note,
   however, that while the *values* are usually equivalent, they can
   differ since there is no synchronization between the two objects.
   For example, it is possible to update the module's "__file__" at
   runtime and this will not be automatically reflected in the
   module's "__spec__.origin", and vice versa.

   Adicionado na versão 3.4.

   name

      The module's fully qualified name (see "module.__name__"). The
      *finder* should always set this attribute to a non-empty string.

   loader

      The *loader* used to load the module (see "module.__loader__").
      The *finder* should always set this attribute.

   origin

      The location the *loader* should use to load the module (see
      "module.__file__"). For example, for modules loaded from a ".py"
      file this is the filename. The *finder* should always set this
      attribute to a meaningful value for the *loader* to use.  In the
      uncommon case that there is not one (like for namespace
      packages), it should be set to "None".

   submodule_search_locations

      A (possibly empty) *sequence* of strings enumerating the
      locations in which a package's submodules will be found (see
      "module.__path__"). Most of the time there will only be a single
      directory in this list.

      The *finder* should set this attribute to a sequence, even an
      empty one, to indicate to the import system that the module is a
      package.  It should be set to "None" for non-package modules.
      It is set automatically later to a special object for namespace
      packages.

   loader_state

      The *finder* may set this attribute to an object containing
      additional, module-specific data to use when loading the module.
      Otherwise it should be set to "None".

   cached

      The filename of a compiled version of the module's code. The
      *finder* should always set this attribute but it may be "None"
      for modules that do not need compiled code stored.

   parent

      (Read-only) The fully qualified name of the package the module
      is in (or the empty string for a top-level module). See
      "module.__package__". If the module is a package then this is
      the same as "name".

   has_location

      "True" if the spec's "origin" refers to a loadable location,
      "False" otherwise.  This value impacts how "origin" is
      interpreted and how the module's "__file__" is populated.

class importlib.machinery.AppleFrameworkLoader(name, path)

   A specialization of "importlib.machinery.ExtensionFileLoader" that
   is able to load extension modules in Framework format.

   For compatibility with the iOS App Store, *all* binary modules in
   an iOS app must be dynamic libraries, contained in a framework with
   appropriate metadata, stored in the "Frameworks" folder of the
   packaged app. There can be only a single binary per framework, and
   there can be no executable binary material outside the Frameworks
   folder.

   To accommodate this requirement, when running on iOS, extension
   module binaries are *not* packaged as ".so" files on "sys.path",
   but as individual standalone frameworks. To discover those
   frameworks, this loader is registered against the ".fwork" file
   extension, with a ".fwork" file acting as a placeholder in the
   original location of the binary on "sys.path". The ".fwork" file
   contains the path of the actual binary in the "Frameworks" folder,
   relative to the app bundle. To allow for resolving a framework-
   packaged binary back to the original location, the framework is
   expected to contain a ".origin" file that contains the location of
   the ".fwork" file, relative to the app bundle.

   Por exemplo, considere o caso de uma importação "from foo.bar
   import _whiz", onde "_whiz" é implementado com o módulo binário
   "sources/foo/bar/_whiz.abi3.so", com "sources" sendo o local
   registrado em "sys.path", relativo ao pacote da aplicação. Este
   módulo *deve* ser distribuído como
   "Frameworks/foo.bar._whiz.framework/foo.bar._whiz" (criando o nome
   do framework a partir do caminho completo de importação do módulo),
   com um arquivo "Info.plist" no diretório ".framework" identificando
   o binário como um framework. O módulo "foo.bar._whiz" seria
   representado no local original com um arquivo marcador
   "sources/foo/bar/_whiz.abi3.fwork", contendo o caminho
   "Frameworks/foo.bar._whiz/foo.bar._whiz". O framework também
   conteria "Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin",
   contendo o caminho para o arquivo ".fwork".

   When a module is loaded with this loader, the "__file__" for the
   module will report as the location of the ".fwork" file. This
   allows code to use the "__file__" of a  module as an anchor for
   file system traversal. However, the spec origin will reference the
   location of the *actual* binary in the ".framework" folder.

   The Xcode project building the app is responsible for converting
   any ".so" files from wherever they exist in the "PYTHONPATH" into
   frameworks in the "Frameworks" folder (including stripping
   extensions from the module file, the addition of framework
   metadata, and signing the resulting framework), and creating the
   ".fwork" and ".origin" files. This will usually be done with a
   build step in the Xcode project; see the iOS documentation for
   details on how to construct this build step.

   Adicionado na versão 3.13.

   Disponibilidade: iOS.

   name

      Nome do módulo ao qual o carregador dá suporte.

   path

      Path to the ".fwork" file for the extension module.


"importlib.util" -- Utility code for importers
==============================================

**Source code:** Lib/importlib/util.py

======================================================================

This module contains the various objects that help in the construction
of an *importer*.

importlib.util.MAGIC_NUMBER

   The bytes which represent the bytecode version number. If you need
   help with loading/writing bytecode then consider
   "importlib.abc.SourceLoader".

   Adicionado na versão 3.4.

importlib.util.cache_from_source(path, *, optimization=None)

   Return the **PEP 3147**/**PEP 488** path to the byte-compiled file
   associated with the source *path*.  For example, if *path* is
   "/foo/bar/baz.py" the return value would be
   "/foo/bar/__pycache__/baz.cpython-32.pyc" for Python 3.2. The
   "cpython-32" string comes from the current magic tag (see
   "sys.implementation.cache_tag"; if it is not defined then
   "NotImplementedError" will be raised).

   The *optimization* parameter is used to specify the optimization
   level of the bytecode file. An empty string represents no
   optimization, so "/foo/bar/baz.py" with an *optimization* of "''"
   will result in a bytecode path of
   "/foo/bar/__pycache__/baz.cpython-32.pyc". "None" causes the
   interpreter's optimization level to be used. Any other value's
   string representation is used, so "/foo/bar/baz.py" with an
   *optimization* of "2" will lead to the bytecode path of
   "/foo/bar/__pycache__/baz.cpython-32.opt-2.pyc". The string
   representation of *optimization* can only be alphanumeric, else
   "ValueError" is raised.

   Adicionado na versão 3.4.

   Alterado na versão 3.5: The *optimization* parameter was added and
   the *debug_override* parameter was deprecated.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

   Alterado na versão 3.15: The *debug_override* parameter was
   removed.

importlib.util.source_from_cache(path)

   Given the *path* to a **PEP 3147** file name, return the associated
   source code file path.  For example, if *path* is
   "/foo/bar/__pycache__/baz.cpython-32.pyc" the returned path would
   be "/foo/bar/baz.py".  *path* need not exist, however if it does
   not conform to **PEP 3147** or **PEP 488** format, a "ValueError"
   is raised. If "sys.implementation.cache_tag" is not defined,
   "NotImplementedError" is raised.

   Adicionado na versão 3.4.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

importlib.util.decode_source(source_bytes)

   Decode the given bytes representing source code and return it as a
   string with universal newlines (as required by
   "importlib.abc.InspectLoader.get_source()").

   Adicionado na versão 3.4.

importlib.util.resolve_name(name, package)

   Resolve a relative module name to an absolute one.

   If  **name** has no leading dots, then **name** is simply returned.
   This allows for usage such as "importlib.util.resolve_name('sys',
   __spec__.parent)" without doing a check to see if the **package**
   argument is needed.

   "ImportError" is raised if **name** is a relative module name but
   **package** is a false value (e.g. "None" or the empty string).
   "ImportError" is also raised if a relative name would escape its
   containing package (e.g. requesting "..bacon" from within the
   "spam" package).

   Adicionado na versão 3.3.

   Alterado na versão 3.9: To improve consistency with import
   statements, raise "ImportError" instead of "ValueError" for invalid
   relative import attempts.

importlib.util.find_spec(name, package=None)

   Localiza o *spec* para um módulo, opcionalmente relativo ao nome do
   **package** especificado. Se o módulo estiver em "sys.modules",
   então "sys.modules[name].__spec__" será retornado (a menos que o
   spec seja "None" ou não esteja definido, nesse caso "ValueError" é
   levantada). Caso contrário, uma pesquisa usando "sys.meta_path" é
   feita. "None" é retornado se nenhum spec for encontrada.

   If **name** is for a submodule (contains a dot), the parent module
   is automatically imported.

   **name** and **package** work the same as for
   "importlib.import_module()".

   Adicionado na versão 3.4.

   Alterado na versão 3.7: Raises "ModuleNotFoundError" instead of
   "AttributeError" if **package** is in fact not a package (i.e.
   lacks a "__path__" attribute).

importlib.util.module_from_spec(spec)

   Create a new module based on **spec** and
   "spec.loader.create_module".

   If "spec.loader.create_module" does not return "None", then any
   pre-existing attributes will not be reset. Also, no
   "AttributeError" will be raised if triggered while accessing
   **spec** or setting an attribute on the module.

   This function is preferred over using "types.ModuleType" to create
   a new module as **spec** is used to set as many import-controlled
   attributes on the module as possible.

   Adicionado na versão 3.5.

importlib.util.spec_from_loader(name, loader, *, origin=None, is_package=None)

   A factory function for creating a "ModuleSpec" instance based on a
   loader.  The parameters have the same meaning as they do for
   ModuleSpec.  The function uses available *loader* APIs, such as
   "InspectLoader.is_package", to fill in any missing information on
   the spec.

   Adicionado na versão 3.4.

importlib.util.spec_from_file_location(name, location, *, loader=None, submodule_search_locations=None)

   A factory function for creating a "ModuleSpec" instance based on
   the path to a file.  Missing information will be filled in on the
   spec by making use of loader APIs and by the implication that the
   module will be file-based.

   Adicionado na versão 3.4.

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

importlib.util.source_hash(source_bytes)

   Return the hash of *source_bytes* as bytes. A hash-based ".pyc"
   file embeds the "source_hash()" of the corresponding source file's
   contents in its header.

   Adicionado na versão 3.7.

importlib.util._incompatible_extension_module_restrictions(*, disable_check)

   A context manager that can temporarily skip the compatibility check
   for extension modules.  By default the check is enabled and will
   fail when a single-phase init module is imported in a
   subinterpreter. It will also fail for a multi-phase init module
   that doesn't explicitly support a per-interpreter GIL, when
   imported in an interpreter with its own GIL.

   Note that this function is meant to accommodate an unusual case;
   one which is likely to eventually go away.  There's is a pretty
   good chance this is not what you were looking for.

   You can get the same effect as this function by implementing the
   basic interface of multi-phase init (**PEP 489**) and lying about
   support for multiple interpreters (or per-interpreter GIL).

   Aviso:

     Using this function to disable the check can lead to unexpected
     behavior and even crashes.  It should only be used during
     extension module development.

   Adicionado na versão 3.12.

class importlib.util.LazyLoader(loader)

   A class which postpones the execution of the loader of a module
   until the module has an attribute accessed.

   This class **only** works with loaders that define "exec_module()"
   as control over what module type is used for the module is
   required. For those same reasons, the loader's "create_module()"
   method must return "None" or a type for which its "__class__"
   attribute can be mutated along with not using *slots*. Finally,
   modules which substitute the object placed into "sys.modules" will
   not work as there is no way to properly replace the module
   references throughout the interpreter safely; "ValueError" is
   raised if such a substitution is detected.

   Nota:

     For projects where startup time is critical, this class allows
     for potentially minimizing the cost of loading a module if it is
     never used. For projects where startup time is not essential then
     use of this class is **heavily** discouraged due to error
     messages created during loading being postponed and thus
     occurring out of context.

   Adicionado na versão 3.5.

   Alterado na versão 3.6: Began calling "create_module()", removing
   the compatibility warning for "importlib.machinery.BuiltinImporter"
   and "importlib.machinery.ExtensionFileLoader".

   classmethod factory(loader)

      A class method which returns a callable that creates a lazy
      loader. This is meant to be used in situations where the loader
      is passed by class instead of by instance.

         suffixes = importlib.machinery.SOURCE_SUFFIXES
         loader = importlib.machinery.SourceFileLoader
         lazy_loader = importlib.util.LazyLoader.factory(loader)
         finder = importlib.machinery.FileFinder(path, (lazy_loader, suffixes))


Exemplos
========


Importing programmatically
--------------------------

To programmatically import a module, use "importlib.import_module()".

   import importlib

   itertools = importlib.import_module('itertools')


Checando se o módulo pode ser importado
---------------------------------------

If you need to find out if a module can be imported without actually
doing the import, then you should use "importlib.util.find_spec()".

Note that if "name" is a submodule (contains a dot),
"importlib.util.find_spec()" will import the parent module.

   import importlib.util
   import sys

   # For illustrative purposes.
   name = 'itertools'

   if name in sys.modules:
       print(f"{name!r} already in sys.modules")
   elif (spec := importlib.util.find_spec(name)) is not None:
       # If you chose to perform the actual import ...
       module = importlib.util.module_from_spec(spec)
       sys.modules[name] = module
       spec.loader.exec_module(module)
       print(f"{name!r} has been imported")
   else:
       print(f"can't find the {name!r} module")


Importa o arquivo de origem diretamente
---------------------------------------

This recipe should be used with caution: it is an approximation of an
import statement where the file path is specified directly, rather
than "sys.path" being searched. Alternatives should first be
considered first, such as modifying "sys.path" when a proper module is
required, or using "runpy.run_path()" when the global namespace
resulting from running a Python file is appropriate.

To import a Python source file directly from a path, use the following
recipe:

   import importlib.util
   import sys


   def import_from_path(module_name, file_path):
       spec = importlib.util.spec_from_file_location(module_name, file_path)
       module = importlib.util.module_from_spec(spec)
       sys.modules[module_name] = module
       spec.loader.exec_module(module)
       return module


   # For illustrative purposes only (use of `json` is arbitrary).
   import json
   file_path = json.__file__
   module_name = json.__name__

   # Similar outcome as `import json`.
   json = import_from_path(module_name, file_path)


Implementing lazy imports
-------------------------

The example below shows how to implement lazy imports:

   >>> import importlib.util
   >>> import sys
   >>> def lazy_import(name):
   ...     spec = importlib.util.find_spec(name)
   ...     loader = importlib.util.LazyLoader(spec.loader)
   ...     spec.loader = loader
   ...     module = importlib.util.module_from_spec(spec)
   ...     sys.modules[name] = module
   ...     loader.exec_module(module)
   ...     return module
   ...
   >>> lazy_typing = lazy_import("typing")
   >>> #lazy_typing is a real module object,
   >>> #but it is not loaded in memory yet.
   >>> lazy_typing.TYPE_CHECKING
   False


Setting up an importer
----------------------

For deep customizations of import, you typically want to implement an
*importer*. This means managing both the *finder* and *loader* side of
things. For finders there are two flavours to choose from depending on
your needs: a *meta path finder* or a *path entry finder*. The former
is what you would put on "sys.meta_path" while the latter is what you
create using a *path entry hook* on "sys.path_hooks" which works with
"sys.path" entries to potentially create a finder. This example will
show you how to register your own importers so that import will use
them (for creating an importer for yourself, read the documentation
for the appropriate classes defined within this package):

   import importlib.machinery
   import sys

   # For illustrative purposes only.
   SpamMetaPathFinder = importlib.machinery.PathFinder
   SpamPathEntryFinder = importlib.machinery.FileFinder
   loader_details = (importlib.machinery.SourceFileLoader,
                     importlib.machinery.SOURCE_SUFFIXES)

   # Setting up a meta path finder.
   # Make sure to put the finder in the proper location in the list in terms of
   # priority.
   sys.meta_path.append(SpamMetaPathFinder)

   # Setting up a path entry finder.
   # Make sure to put the path hook in the proper location in the list in terms
   # of priority.
   sys.path_hooks.append(SpamPathEntryFinder.path_hook(loader_details))


Approximating "importlib.import_module()"
-----------------------------------------

Import itself is implemented in Python code, making it possible to
expose most of the import machinery through importlib. The following
helps illustrate the various APIs that importlib exposes by providing
an approximate implementation of "importlib.import_module()":

   import importlib.util
   import sys

   def import_module(name, package=None):
       """An approximate implementation of import."""
       absolute_name = importlib.util.resolve_name(name, package)
       try:
           return sys.modules[absolute_name]
       except KeyError:
           pass

       path = None
       if '.' in absolute_name:
           parent_name, _, child_name = absolute_name.rpartition('.')
           parent_module = import_module(parent_name)
           path = parent_module.__spec__.submodule_search_locations
       for finder in sys.meta_path:
           spec = finder.find_spec(absolute_name, path)
           if spec is not None:
               break
       else:
           msg = f'No module named {absolute_name!r}'
           raise ModuleNotFoundError(msg, name=absolute_name)
       module = importlib.util.module_from_spec(spec)
       sys.modules[absolute_name] = module
       spec.loader.exec_module(module)
       if path is not None:
           setattr(parent_module, child_name, module)
       return module
