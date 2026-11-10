"importlib.metadata" -- Acessando metadados do pacote
*****************************************************

Adicionado na versão 3.8.

Alterado na versão 3.10: "importlib.metadata" não é mais provisório.

**Código-fonte:** Lib/importlib/metadata/__init__.py

"importlib.metadata" é uma biblioteca que fornece acesso aos metadados
de um Pacote de Distribuição instalado, como seus pontos de entrada ou
seus nomes de nível superior (Pacotes de Importação, módulos, se
houver). Construída em parte no sistema de importação do Python, esta
biblioteca fornece as APIs de ponto de entrada e de metadados que eram
anteriormente expostas pelo agora removido pacote "pkg_resources".
Junto com "importlib.resources", agora substitui "pkg_resources".

"importlib.metadata" opera em *pacotes de distribuição* de terceiros
instalados no diretório "site-packages" do Python através de
ferramentas como pip. Especificamente, ele funciona com distribuições
com diretórios "dist-info" ou "egg-info" detectáveis, e metadados
definidos pelas Especificações de metadados principais.

Importante:

  Eles *não* são necessariamente equivalentes ou correspondem 1:1 aos
  nomes de *pacotes de importação* de nível superior que podem ser
  importados dentro do código Python. Um *pacote de distribuição* pode
  conter vários *pacotes de importação* (e módulos únicos), e um
  *pacote de importação* de nível superior pode ser mapeado para
  vários *pacotes de distribuição* se for um pacote de espaço de
  nomes. Você pode usar packages_distributions() para obter um
  mapeamento entre eles.

Por padrão, os metadados de distribuição podem residir no sistema de
arquivos ou em arquivos zip em "sys.path". Através de um mecanismo de
extensão, os metadados podem residir em praticamente qualquer lugar.

Ver também:

  https://importlib-metadata.readthedocs.io/
     A documentação para "importlib_metadata", que fornece um backport
     de "importlib.metadata". Isso inclui uma referência de API para
     as classes e funções deste módulo, bem como um guia de migração
     para usuários existentes de "pkg_resources".


Visão Geral
===========

Digamos que você queira obter a string da versão de um Pacote de
Distribuição que você instalou usando "pip". Começamos criando um
ambiente virtual e instalando algo nele:

   $ python -m venv exemplo
   $ source exemplo/bin/activate
   (exemplo) $ python -m pip install wheel

Você pode obter a string de versão para "wheel" executando o seguinte:

   (example) $ python
   >>> from importlib.metadata import version
   >>> version('wheel')
   '0.32.3'

Você também pode obter uma coleção de pontos de entrada selecionáveis
pelas propriedades do EntryPoint (normalmente 'group' ou 'name'), como
"console_scripts", "distutils.commands" e outros. Cada grupo contém
uma coleção de objetos EntryPoint.

Você pode obter os metadados para uma distribuição:

   >>> from importlib.metadata import metadata
   >>> list(metadata('wheel'))
   ['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author', 'Author-email', 'Maintainer', 'Maintainer-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL', 'Keywords', 'Platform', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python', 'Provides-Extra', 'Requires-Dist', 'Requires-Dist']

Você também pode obter uma número da versão da distribuição, listar
seus arquivos constituintes e obter uma lista dos Requisitos de
distribuição da distribuição.

exception importlib.metadata.PackageNotFoundError

   Subclasse de "ModuleNotFoundError" levantada por diversas funções
   neste módulo quando consultada sobre um pacote de distribuição que
   não está instalado no ambiente Python atual.

exception importlib.metadata.MetadataNotFound

   Subclass of "FileNotFoundError" raised when attempting to load
   metadata from a distribution folder that is empty or otherwise does
   not contain a metadata file.


API funcional
=============

Este pacote fornece a seguinte funcionalidade por meio de sua API
pública.


Pontos de entrada
-----------------

importlib.metadata.entry_points(**select_params)

   Retorna uma instância de "EntryPoints" descrevendo pontos de
   entrada para o ambiente atual. Quaisquer parâmetros nomeados
   fornecidos são passados para o método "select()" para comparação
   com os atributos das definições de pontos de entrada individuais.

   Note: to query for entry points based on "EntryPoint.dist"
   attribute, use "Distribution.entry_points()" instead (as different
   "Distribution" instances do not currently compare equal, even if
   they have the same attributes)

class importlib.metadata.EntryPoints

   Detalhes de uma coleção de pontos de entrada instalados.

   Também fornece um atributo ".groups" que relata todos os grupos de
   pontos de entrada identificados e um atributo ".names" que relata
   todos os nomes de pontos de entrada identificados.

class importlib.metadata.EntryPoint

   Detalhes de um ponto de entrada instalado.

   Cada instância de "EntryPoint" tem os atributos ".name", ".group" e
   ".value" e um método ".load()" para resolver o valor. Há também os
   atributos ".module", ".attr" e ".extras" para obter os componentes
   do atributo ".value" e ".dist" para obter informações sobre o
   pacote de distribuição que fornece o ponto de entrada.

Consultar todos os pontos de entrada:

   >>> eps = entry_points()

A função "entry_points()" retorna um objeto "EntryPoints", uma coleção
de todos os objetos "EntryPoint" com atributos "names" e "groups" por
conveniência:

   >>> sorted(eps.groups)
   ['console_scripts', 'distutils.commands', 'distutils.setup_keywords', 'egg_info.writers', 'setuptools.installation']

"EntryPoints" possui um método "select()" para selecionar pontos de
entrada correspondendo a propriedades específicas. Selecione pontos de
entrada no grupo "console_scripts":

   >>> scripts = eps.select(group='console_scripts')

Equivalentemente, já que "entry_points()" passa argumentos nomeados
para a seleção:

   >>> scripts = entry_points(group='console_scripts')

Escolha um script específico chamado "wheel" (encontrado no projeto
wheel):

   >>> 'wheel' in scripts.names
   True
   >>> wheel = scripts['wheel']

De forma equivalente, consulte esse ponto de entrada durante a
seleção:

   >>> (wheel,) = entry_points(group='console_scripts', name='wheel')
   >>> (wheel,) = entry_points().select(group='console_scripts', name='wheel')

Inspecione o ponto de entrada resolvido:

   >>> wheel
   EntryPoint(name='wheel', value='wheel.cli:main', group='console_scripts')
   >>> wheel.module
   'wheel.cli'
   >>> wheel.attr
   'main'
   >>> wheel.extras
   []
   >>> main = wheel.load()
   >>> main
   <function main at 0x103528488>

O "group" e "name" são valores arbitrários definidos pelo autor do
pacote e normalmente um cliente desejará resolver todos os pontos de
entrada para um grupo específico. Leia a documentação do setuptools
para obter mais informações sobre pontos de entrada, sua definição e
uso.

Alterado na versão 3.12: Os pontos de entrada "selecionáveis" foram
introduzidos em "importlib_metadata" 3.6 e Python 3.10. Antes dessas
mudanças, "entry_points" não aceitava parâmetros e sempre retornava um
dicionário de pontos de entrada, chaveado por grupo. Com
"importlib_metadata" 5.0 e Python 3.12, "entry_points" sempre retorna
um objeto "EntryPoints". Veja backports.entry_points_selectable para
opções de compatibilidade.

Alterado na versão 3.13: Objetos "EntryPoint" não apresentam mais uma
interface tupla ou similar ("__getitem__()").


Metadados de distribuição
-------------------------

importlib.metadata.metadata(distribution_name)

   Retorna os metadados de distribuição correspondentes ao pacote de
   distribuição nomeado como uma instância de "PackageMetadata".

   Levanta "PackageNotFoundError" se o pacote de distribuição nomeado
   não estiver instalado no ambiente Python atual.

   Raises "MetadataNotFound" if a distribution package is present but
   no METADATA file is present.

class importlib.metadata.PackageMetadata

   Uma implementação concreta do protocolo PackageMetadata.

   Além de fornecer os métodos e atributos de protocolo definidos,
   subscrever a instância é equivalente a chamar o método "get()".

Cada Pacote de Distribuição inclui alguns metadados, que você pode
extrair usando a função "metadata()":

   >>> wheel_metadata = metadata('wheel')

As chaves da estrutura de dados retornada nomeiam as palavras
reservadas dos metadados, e os valores são retornados sem análise dos
metadados de distribuição:

   >>> wheel_metadata['Requires-Python']
   '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

"PackageMetadata" também apresenta um atributo "json" que retorna
todos os metadados em um formato compatível com JSON pela **PEP 566**:

   >>> wheel_metadata.json['requires_python']
   '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

O conjunto completo de metadados disponíveis não é descrito aqui.
Consulte a especificação de metadados principais do PyPA para obter
detalhes adicionais.

Alterado na versão 3.15: Previously and incidentally, if a METADATA
file was missing from a distribution, an empty "PackageMetadata" would
be returned, indistinguishable from an empty METADATA file. Now, a
missing METADATA file triggers a "MetadataNotFound" exception.

Alterado na versão 3.10: A "Description" agora é incluída nos
metadados quando apresentada através do payload. Os caracteres de
continuação de linha foram removidos.O atributo "json" foi adicionado.


Versões de distribuição
-----------------------

importlib.metadata.version(distribution_name)

   Retorna a versão do pacote de distribuição instalado para o pacote
   de distribuição nomeado.

   Levanta "PackageNotFoundError" se o pacote de distribuição nomeado
   não estiver instalado no ambiente Python atual.

A função "version()" é a maneira mais rápida de obter o número de
versão de um Pacote de Distribuição, como uma string:

   >>> version('wheel')
   '0.32.3'


Arquivos de distribuição
------------------------

importlib.metadata.files(distribution_name)

   Return the full set of files contained within the named
   distribution package as "PackagePath" instances.

   Levanta "PackageNotFoundError" se o pacote de distribuição nomeado
   não estiver instalado no ambiente Python atual.

   Retorna "None" se a distribuição for encontrada, mas os registros
   do banco de dados de instalação que relatam os arquivos associados
   ao pacote de distribuição estiverem ausentes.

class importlib.metadata.PackagePath

   A "pathlib.PurePath" derived object with additional "dist", "size",
   and "hash" properties corresponding to the distribution package's
   installation metadata for that file, also:

   locate()

      If possible, return the concrete "SimplePath" allowing to access
      data, or raise a "NotImplementedError" otherwise.

class importlib.metadata.SimplePath

   A protocol representing a minimal subset of "pathlib.Path" that
   allows to check if it "exists()", to traverse using "joinpath()"
   and "parent", and to retrieve data using "read_text()" and
   "read_bytes()".

The "files()" function takes a Distribution Package name and returns
all of the files installed by this distribution. For example:

   >>> util = [p for p in files('wheel') if 'util.py' in str(p)][0]
   >>> util
   PackagePath('wheel/util.py')
   >>> util.size
   859
   >>> util.dist
   <importlib.metadata._hooks.PathDistribution object at 0x101e0cef0>
   >>> util.hash
   <FileHash mode: sha256 value: bYkw5oMccfazVCoYQwKkkemoVyMAFoR34mmKBx8R1NI>

Uma vez que tenha o arquivo, você também pode ler seu conteúdo:

   >>> print(util.read_text())
   import base64
   import sys
   ...
   def as_bytes(s):
       if isinstance(s, text_type):
           return s.encode('utf-8')
       return s

Você também pode usar o método "locate()" para obter o caminho
absoluto para o arquivo:

   >>> util.locate()
   PosixPath('/home/gustav/example/lib/site-packages/wheel/util.py')

No caso em que o arquivo de metadados que lista os arquivos ("RECORD"
ou "SOURCES.txt") estiver faltando, "files()" retornará "None". O
chamador pode querer agrupar chamadas para "files()" em
always_iterable ou de outra forma se proteger contra isso condição se
a distribuição de destino não for conhecida por ter os metadados
presentes.


Requisitos de distribuição
--------------------------

importlib.metadata.requires(distribution_name)

   Retorna os especificadores de dependência declarados para o pacote
   de distribuição nomeado.

   Levanta "PackageNotFoundError" se o pacote de distribuição nomeado
   não estiver instalado no ambiente Python atual.

Para obter o conjunto completo de requisitos para um Pacote de
Distribuição, use a função "requires()":

   >>> requires('wheel')
   ["pytest (>=3.0.0) ; extra == 'test'", "pytest-cov ; extra == 'test'"]


Mapeando importação pra pacotes de distribuição
-----------------------------------------------

importlib.metadata.packages_distributions()

   Retorna um mapeamento do módulo de nível superior e importa os
   nomes dos pacotes encontrados via "sys.meta_path" para os nomes dos
   pacotes de distribuição (se houver) que fornecem os arquivos
   correspondentes.

   Para permitir pacotes de espaço de nomes (que podem ter membros
   fornecidos por vários pacotes de distribuição), cada nome de
   importação de nível superior é mapeado para uma lista de nomes de
   distribuição em vez de mapear diretamente para um único nome.

Um método conveniente para resolver o nome do Pacote de Distribuição
(ou nomes, no caso de um pacote de espaço de nomes) que fornece cada
módulo Python de nível superior importável ou Pacote de Importação:

   >>> packages_distributions()
   {'importlib_metadata': ['importlib-metadata'], 'yaml': ['PyYAML'], 'jaraco': ['jaraco.classes', 'jaraco.functools'], ...}

Algumas instalações editáveis não fornecem nomes de nível superior e,
portanto, esta função não é confiável com tais instalações.

Adicionado na versão 3.10.


Distribuições
=============

While the module level API described above is the most common and
convenient usage, all that information is accessible from the
"Distribution" class. "Distribution" is an abstract object that
represents the metadata for a Python Distribution Package. Get the
concrete "Distribution" subclass instance for an installed
distribution package by calling the "distribution()" function:

   >>> from importlib.metadata import distribution
   >>> dist = distribution('wheel')
   >>> type(dist)
   <class 'importlib.metadata.PathDistribution'>

importlib.metadata.distribution(distribution_name)

   Retorna uma instância de "Distribution" descrevendo o pacote de
   distribuição nomeado.

   Levanta "PackageNotFoundError" se o pacote de distribuição nomeado
   não estiver instalado no ambiente Python atual.

Thus, an alternative way to get e.g. the version number is through the
"Distribution.version" attribute:

   >>> dist.version
   '0.32.3'

The same applies for "entry_points()" and "files()".

class importlib.metadata.Distribution

   Detalhes de um pacote de distribuição instalado.

   Observação: instâncias diferentes de "Distribution" não são
   atualmente consideradas iguais em uma comparação, mesmo que estejam
   relacionadas à mesma distribuição instalada e, portanto, tenham os
   mesmos atributos.

   static at(path)

   classmethod from_name(name)

      Return a "Distribution" instance at the given path or with the
      given name.

   classmethod discover(*, context=None, **kwargs)

      Returns an iterable of "Distribution" instances for all packages
      (see distribution-discovery).

      The optional argument *context* is a
      "DistributionFinder.Context" instance, used to modify the search
      for distributions. Alternatively, *kwargs* may contain keyword
      arguments for constructing a new "DistributionFinder.Context".

   metadata: PackageMetadata

      Raises "MetadataNotFound" if the METADATA file is not present in
      the distribution.

      There are all kinds of additional metadata available on
      "Distribution" instances as a "PackageMetadata" instance:

         >>> dist.metadata['Requires-Python']
         '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
         >>> dist.metadata['License']
         'MIT'

      O conjunto completo de metadados disponíveis não é descrito
      aqui. Consulte a especificação de metadados principais do PyPA
      para obter detalhes adicionais.

   name: str

   requires: list[str]

   version: str

      A few metadata fields are also available as shortcut properties.

      Adicionado na versão 3.10: The "name" shortcut was added.

   origin

      For editable packages, an "origin" property may present **PEP
      610** metadata (for non-editable packages, "origin" is "None"):

         >>> dist.origin.url
         'file:///caminho/para/wheel-0.32.3.editable-py3-none-any.whl'

      The "origin" object follows the Direct URL Data Structure.

      Adicionado na versão 3.13.

   entry_points: EntryPoints

      The entry points provided by this distribution package.

   files: list[PackagePath] | None

      All files contained in this distribution package. Like
      "files()", this returns "None" if there are no records.

   The following two abstract methods need to be implemented when
   implementing-custom-providers:

   locate_file(path)

      Like "PackagePath.locate()", return a "SimplePath" for the given
      path. Takes a "os.PathLike" or a "str".

   read_text(filename)

      A shortcut for "distribution.locate_file(filename).read_text()".


Descoberta de distribuição
==========================

Por padrão, este pacote fornece suporte embutido para descoberta de
metadados para sistema de arquivos e arquivo zip Pacotes de
Distribuição. Esta pesquisa do localizador de metadados tem como
padrão "sys.path", mas varia um pouco na maneira como ela interpreta
esses valores em relação a outras mecanismo de importação. Em
particular:

* "importlib.metadata" não honra objetos "bytes" em "sys.path".

* "importlib.metadata" irá incidentalmente honrar objetos
  "pathlib.Path" em "sys.path" mesmo que tais valores sejam ignorados
  para importações.

class importlib.metadata.DistributionFinder

   A "MetaPathFinder" subclass capable of discovering installed
   distributions.

   Custom providers should implement this interface in order to supply
   metadata.

      class Context(**kwargs)

         A "Context" gives a custom provider a means to solicit
         additional details from the callers of distribution discovery
         functions like "distributions()" or "Distribution.discover()"
         beyond ".name" and ".path" when searching for distributions.

         For example, a provider could expose suites of packages in
         either a "public" or "private" "realm". A caller of
         distribution discovery functions may wish to query only for
         distributions in a particular realm and could call
         "distributions(realm="private")" to signal to the custom
         provider to only include distributions from that realm.

         Each "DistributionFinder" must expect any parameters and
         should attempt to honor the canonical parameters defined
         below when appropriate.

         See the section on Implementando provedores personalizados
         for more details.

         name

            Specific name for which a distribution finder should
            match.

            A ".name" of "None" matches all distributions.

         path

            A property providing the sequence of directory paths that
            a distribution finder should search.

            Typically refers to Python installed package paths such as
            "site-packages" directories and defaults to "sys.path".

importlib.metadata.distributions(**kwargs)

   Returns an iterable of "Distribution" instances for all packages.

   The *kwargs* argument may contain either a keyword argument
   "context", a "DistributionFinder.Context" instance, or pass keyword
   arguments for constructing a new "DistributionFinder.Context". The
   "DistributionFinder.Context" is used to modify the search for
   distributions.


Implementando provedores personalizados
=======================================

"importlib.metadata" aborda duas superfícies de API, uma para
*consumidores* e outra para *provedores*. A maioria dos usuários são
consumidores, consumindo metadados fornecidos pelos pacotes. Existem
outros casos de uso, no entanto, em que os usuários desejam expor
metadados por meio de algum outro mecanismo, como junto com um
importador personalizado. Esse caso de uso exige um *provedor
personalizado*.

Como os metadados de Pacote de Distribuição não estão disponíveis por
meio de pesquisas a "sys.path" ou carregadores de pacotes diretamente,
os metadados de uma distribuição são encontrados através de
localizadores do sistema de importação. Para encontrar os metadados de
um pacote de distribuição, "importlib.metadata" consulta a lista de
*localizadores de metacaminho* em "sys.meta_path".

A implementação possui ganchos integrados ao "PathFinder", servindo
metadados para pacotes de distribuição encontrados no sistema de
arquivos.

The abstract class "importlib.abc.MetaPathFinder" defines the
interface expected of finders by Python's import system.
"importlib.metadata" extends this protocol by looking for an optional
"find_distributions" callable on the finders from "sys.meta_path" and
presents this extended interface as the "DistributionFinder" abstract
base class, which defines this abstract method:

   @abc.abstractmethod
   def find_distributions(context=DistributionFinder.Context()) -> Iterable[Distribution]:
       """Return an iterable of all Distribution instances capable of
       loading the metadata for packages for the indicated ``context``.
       """

The "DistributionFinder.Context" object provides "path" and "name"
properties indicating the path to search and name to match and may
supply other relevant context sought by the consumer.

In practice, to support finding distribution package metadata in
locations other than the file system, subclass "Distribution" and
implement the abstract methods. Then from a custom finder, return
instances of this derived "Distribution" in the "find_distributions()"
method.


Exemplo
-------

Imagine um localizador personalizado que carrega módulos Python de um
banco de dados:

   class DatabaseImporter(importlib.abc.MetaPathFinder):
       def __init__(self, db):
           self.db = db

       def find_spec(self, fullname, target=None) -> ModuleSpec:
           return self.db.spec_from_name(fullname)

   sys.meta_path.append(DatabaseImporter(connect_db(...)))

That importer now presumably provides importable modules from a
database, but it provides no metadata or entry points. For this custom
importer to provide metadata, it would also need to implement
"DistributionFinder":

   from importlib.metadata import DistributionFinder

   class DatabaseImporter(DistributionFinder):
       ...

       def find_distributions(self, context=DistributionFinder.Context()):
           query = dict(name=context.name) if context.name else {}
           for dist_record in self.db.query_distributions(query):
               yield DatabaseDistribution(dist_record)

Desta forma, "query_distributions" retornaria registros para cada
distribuição servida pelo banco de dados correspondente à consulta.
Por exemplo, se "requests-1.0" estiver no banco de dados,
"find_distributions" produziria um "DatabaseDistribution" para
"Context(name='requests')" ou "Context(name=None)".

Por uma questão de simplicidade, este exemplo ignora "context.path". O
atributo "path" tem como padrão "sys.path" e é o conjunto de caminhos
de importação a serem considerados na pesquisa. Um "DatabaseImporter"
poderia funcionar potencialmente sem qualquer preocupação com um
caminho de pesquisa. Supondo que o importador não faça
particionamento, o caminho “path” seria irrelevante. Para ilustrar o
propósito de "path", o exemplo precisaria ilustrar um
"DatabaseImporter" mais complexo cujo comportamento variasse
dependendo de "sys.path"/"PYTHONPATH". Nesse caso,
"find_distributions" deve respeitar o "context.path" e produzir apenas
"Distribution"s pertinentes a esse caminho.

"DatabaseDistribution", então, se pareceria com algo como:

   class DatabaseDistribution(importlib.metadata.Distribution):
       def __init__(self, record):
           self.record = record

       def read_text(self, filename):
           """
           Lê um arquivo como "METADATA" para a atual distribuição.
           """
           if filename == "METADATA":
               return f"""Name: {self.record.name}
   Version: {self.record.version}
   """
           if filename == "entry_points.txt":
               return "\n".join(
                 f"""[{ep.group}]\n{ep.name}={ep.value}"""
                 for ep in self.record.entry_points)

       def locate_file(self, path):
           raise RuntimeError("This distribution has no file system")

Esta implementação básica deve fornecer metadados e pontos de entrada
para pacotes servidos pelo "DatabaseImporter", presumindo que o
"record" forneça os atributos ".name", ".version" e ".entry_points"
adequados.

The "DatabaseDistribution" may also provide other metadata files, like
"RECORD" (required for "Distribution.files") or override the
implementation of "Distribution.files". See the source for more
inspiration.
