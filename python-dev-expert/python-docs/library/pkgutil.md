"pkgutil" --- Utilitário de extensão de pacote
**********************************************

**Código-fonte:** Lib/pkgutil.py

======================================================================

Este módulo fornece utilitários para o sistema de importação, em
particular suporte a pacotes.

class pkgutil.ModuleInfo(module_finder, name, ispkg)

   Um namedtuple que contém um breve resumo das informações de um
   módulo.

   Adicionado na versão 3.6.

pkgutil.extend_path(path, name)

   Estende o caminho de pesquisa para os módulos que compõem um
   pacote. O uso pretendido é colocar o seguinte código no
   "__init__.py" de um pacote:

      from pkgutil import extend_path
      __path__ = extend_path(__path__, __name__)

   Para cada diretório em "sys.path" que tenha um subdiretório que
   corresponda ao nome do pacote, adiciona o subdiretório ao
   "__path__" do pacote. Isto é útil se quisermos distribuir
   diferentes partes de um único pacote lógico como múltiplos
   diretórios.

   Também procura por arquivos "*.pkg" que começam onde "*"
   corresponde ao argumento *name*. Este recurso é semelhante aos
   arquivos "*.pth" (consulte o módulo "site" para mais informações),
   exceto que não considera casos especiais para linhas que começam
   com "import". Um arquivo "*.pkg" é confiável por natureza: além de
   pular linhas em branco e ignorar comentários, todas as entradas
   encontradas em um arquivo "*.pkg" são adicionadas ao caminho,
   independentemente de existirem ou não no sistema de arquivos (este
   é um recurso).

   Se o caminho de entrada não for uma lista (como é o caso de pacotes
   congelados), ele será retornado inalterado. O caminho de entrada
   não é modificado; uma cópia estendida é retornada. Os itens são
   anexados à cópia apenas no final.

   Presume-se que "sys.path" seja uma sequência. Itens de "sys.path"
   que não sejam strings referentes a diretórios existentes são
   ignorados. Itens Unicode em "sys.path" que causam erros quando
   usados como nomes de arquivo podem fazer com que esta função
   levante uma exceção (em linha com o comportamento de
   "os.path.isdir()").

pkgutil.get_importer(path_item)

   Recupera um *localizador* para o *path_item* fornecido.

   O localizador retornado é armazenado em cache em
   "sys.path_importer_cache" se ele foi criado recentemente por um
   gancho de caminho.

   O cache (ou parte dele) pode ser limpo manualmente se uma nova
   varredura de "sys.path_hooks" for necessária.

   Alterado na versão 3.3: Atualizado para ser baseado diretamente em
   "importlib" em vez de depender da emulação de importação interna do
   pacote da **PEP 302**.

pkgutil.iter_importers(fullname='')

   Produz objetos *localizador* para o nome do módulo fornecido.

   Se *fullname* contiver "'.'", os localizadores serão para o pacote
   que contém *fullname*, caso contrário, serão todos os localizadores
   de nível superior registrados (ou seja, aqueles em "sys.meta_path"
   e "sys.path_hooks").

   Se o módulo nomeado estiver em um pacote, esse pacote será
   importado como um efeito colateral da invocação desta função.

   Se nenhum nome de módulo for especificado, todos os localizadores
   de nível superior serão produzidos.

   Alterado na versão 3.3: Atualizado para ser baseado diretamente em
   "importlib" em vez de depender da emulação de importação interna do
   pacote da **PEP 302**.

pkgutil.iter_modules(path=None, prefix='')

   Levanta "ModuleInfo" para todos os submódulos em *path* ou, se
   *path* for "None", todos os módulos de nível superior em
   "sys.path".

   *path* deve ser "None" ou uma lista de caminhos para procurar
   módulos.

   *prefix* é uma string a ser exibida na frente de cada nome de
   módulo na saída.

   Nota:

     Funciona apenas para um *localizador* que define um método
     "iter_modules()". Esta interface não é padrão, portanto, o módulo
     também fornece implementações para
     "importlib.machinery.FileFinder" e "zipimport.zipimporter".

   Alterado na versão 3.3: Atualizado para ser baseado diretamente em
   "importlib" em vez de depender da emulação de importação interna do
   pacote da **PEP 302**.

pkgutil.walk_packages(path=None, prefix='', onerror=None)

   Levanta "ModuleInfo" para todos os módulos recursivamente em
   *path*, ou, se *path* for "None", todos os módulos acessíveis.

   *path* deve ser "None" ou uma lista de caminhos para procurar
   módulos.

   *prefix* é uma string a ser exibida na frente de cada nome de
   módulo na saída.

   Observe que esta função deve importar todos os *pacotes* (*não*
   todos os módulos!) no caminho *path* fornecido, para acessar o
   atributo "__path__" para encontrar submódulos.

   *onerror* é uma função que é chamada com um argumento (o nome do
   pacote que estava sendo importado) caso ocorra alguma exceção
   durante a tentativa de importação de um pacote. Se nenhuma função
   *onerror* for fornecida, "ImportError"s são capturadas e ignoradas,
   enquanto todas as outras exceções são propagadas, encerrando a
   busca.

   Exemplos:

      # lista todos os módulos que o python consegue acessars
      walk_packages()

      # lista todos os submódulos de ctypes
      walk_packages(ctypes.__path__, ctypes.__name__ + '.')

   Nota:

     Funciona apenas para um *localizador* que define um método
     "iter_modules()". Esta interface não é padrão, portanto, o módulo
     também fornece implementações para
     "importlib.machinery.FileFinder" e "zipimport.zipimporter".

   Alterado na versão 3.3: Atualizado para ser baseado diretamente em
   "importlib" em vez de depender da emulação de importação interna do
   pacote da **PEP 302**.

pkgutil.get_data(package, resource)

   Obtém um recurso de um pacote.

   Este é um invólucro para a API "get_data" *carregadora*. O
   argumento *package* deve ser o nome de um pacote, no formato de
   módulo padrão ("foo.bar"). O argumento *resource* deve estar no
   formato de um nome de arquivo relativo, usando "/" como separador
   de caminho.

   A função retorna uma string binária que é o conteúdo do recurso
   especificado.

   Esta função utiliza o método *carregador* "get_data()" para dar
   suporte a módulos instalados no sistema de arquivos, mas também em
   arquivos zip, bancos de dados ou em outros locais.

   Para pacotes localizados no sistema de arquivos, que já foram
   importados, isso é o equivalente aproximado de:

      d = os.path.dirname(sys.modules[package].__file__)
      data = open(os.path.join(d, resource), 'rb').read()

   Assim como a função "open()", "get_data()" pode seguir diretórios
   pai ("../") e caminhos absolutos (começando com "/" ou "C:/", por
   exemplo). Ela pode abrir artefatos de compilação/instalação como
   arquivos ".py" e ".pyc" ou arquivos com "nomes reservados". Para
   ser compatível com carregadores que não utilizam o sistema de
   arquivos, evite usar esses recursos.

   Aviso:

     Esta função destina-se a entradas confiáveis. Ela não verifica se
     o *resource* "pertence" ao *package*.

   Se você usar um caminho de *resource* fornecido pelo usuário,
   considere verificá-lo. Por exemplo, exija um nome de arquivo
   alfanumérico com uma extensão conhecida ou instale e verifique uma
   lista de recursos conhecidos.

   Se o pacote não puder ser localizado ou carregado, ou se usar um
   *carregador* que não oferece suporte a "get_data", "None" será
   retornado. Em particular, o *carregador* para *pacotes de espaço de
   nomes* não oferece suporte a "get_data".

   Ver também:

     O módulo "importlib.resources" fornece acesso estruturado para
     recursos de módulo.

pkgutil.resolve_name(name, *, strict=False)

   Resolve um nome a um objeto.

   Essa funcionalidade é usada em vários lugares na biblioteca padrão
   (veja bpo-12915) - e funcionalidades equivalentes também estão
   amplamente utilizadas em pacotes de terceiros, como setuptools,
   Django e Pyramid.

   Espera-se que *name* seja uma string em um dos seguintes formatos,
   onde W é uma abreviação para um identificador Python válido e ponto
   representa um ponto literal nessas pseudo-regexes:

   * "W(.W)*"

   * "W(.W)*:(W(.W)*)?"

   * "W(.W)*:(W(.W)*)"

   A primeira forma destina-se apenas à retrocompatibilidade. Ela
   presume que parte do nome pontilhado seja um pacote e o restante
   seja um objeto em algum lugar dentro desse pacote, possivelmente
   aninhado dentro de outros objetos. Como o ponto onde o pacote
   termina e a hierarquia de objetos começa não pode ser inferido por
   inspeção, tentativas repetidas de importação devem ser feitas com
   esta forma.

   Na segunda forma, o chamador deixa claro o ponto de divisão por
   meio de um caractere de dois pontos: o nome pontilhado à esquerda
   do caractere de dois pontos representa um pacote a ser importado, e
   o nome pontilhado à direita representa a hierarquia de objetos
   dentro desse pacote. Apenas uma importação é necessária nesta
   forma. Se terminar com caractere de dois pontos, um objeto de
   módulo será retornado.

   As duas primeiras formas são aceitas quando "strict=False" (o
   padrão).

   A terceira forma requer tanto o nome do módulo quanto o objeto
   chamável, separados por dois-pontos. Apenas esta forma é aceita
   quando "strict=True".

   A função retornará um objeto (que pode ser um módulo) ou levantará
   uma das seguintes exceções:

   "ValueError" -- se *name* não estiver em um formato reconhecido.

   "ImportError" -- se uma importação falhou quando não deveria.

   "AttributeError" -- Se ocorrer uma falha ao percorrer a hierarquia
   de objetos dentro do pacote importado para chegar ao objeto
   desejado.

   Adicionado na versão 3.9.

   Alterado na versão 3.15: A opção "strict" somente-nomeada opcional
   foi adicionada.
