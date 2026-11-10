5. O sistema de importação
**************************

O código Python em um *módulo* obtém acesso ao código em outro módulo
pelo processo de *importação* dele. A instrução "import" é a maneira
mais comum de invocar o mecanismo de importação, mas não é a única
maneira. Funções como "importlib.import_module()" e a função embutida
"__import__()" também podem ser usadas para chamar o mecanismo de
importação.

A instrução "import" combina duas operações; ela procura o módulo
nomeado e vincula os resultados dessa pesquisa a um nome no escopo
local. A operação de busca da instrução "import" é definida como uma
chamada para a função "__import__()", com os argumentos apropriados. O
valor de retorno de "__import__()" é usado para executar a operação de
ligação de nome da instrução "import". Veja a instrução "import" para
os detalhes exatos da operação de ligação desse nome.

Uma chamada direta para "__import__()" realiza apenas a pesquisa do
módulo e, se encontrada, a operação de criação do módulo. Embora
certos efeitos colaterais possam ocorrer, como a importação de pacotes
pai e a atualização de vários caches (incluindo "sys.modules"), apenas
a instrução "import" realiza uma operação de ligação de nome.

Quando uma instrução "import" é executada, a função embutida padrão
"__import__()" é chamada. Outros mecanismos para chamar o sistema de
importação (como "importlib.import_module()") podem optar por ignorar
"__import__()" e usar suas próprias soluções para implementar a
semântica de importação.

Quando um módulo é importado pela primeira vez, o Python procura pelo
módulo e, se encontrado, cria um objeto de módulo [1],
inicializando-o. Se o módulo nomeado não puder ser encontrado, uma
"ModuleNotFoundError" será levantada. O Python implementa várias
estratégias para procurar o módulo nomeado quando o mecanismo de
importação é chamado. Essas estratégias podem ser modificadas e
estendidas usando vários ganchos descritos nas seções abaixo.

Alterado na versão 3.3: O sistema de importação foi atualizado para
implementar completamente a segunda fase da **PEP 302**. Não há mais
um mecanismo de importação implícito -- o sistema completo de
importação é exposto através de "sys.meta_path". Além disso, o suporte
nativo a pacote de espaço de nomes foi implementado (consulte **PEP
420**).


5.1. "importlib"
================

O módulo "importlib" fornece uma API rica para interagir com o sistema
de importação. Por exemplo, "importlib.import_module()" fornece uma
API mais simples e recomendada do que a função embutida "__import__()"
para chamar o mecanismo de importação. Consulte a documentação da
biblioteca "importlib" para obter detalhes adicionais.


5.2. Pacotes
============

O Python possui apenas um tipo de objeto de módulo e todos os módulos
são desse tipo, independentemente de o módulo estar implementado em
Python, C ou qualquer outra coisa. Para ajudar a organizar os módulos
e fornecer uma hierarquia de nomes, o Python tem o conceito de
*pacotes*.

Você pode pensar em pacotes como os diretórios em um sistema de
arquivos e os módulos como arquivos nos diretórios, mas não tome essa
analogia muito literalmente, já que pacotes e módulos não precisam se
originar do sistema de arquivos. Para os fins desta documentação,
usaremos essa analogia conveniente de diretórios e arquivos. Como os
diretórios do sistema de arquivos, os pacotes são organizados
hierarquicamente e os próprios pacotes podem conter subpacotes e
módulos regulares.

É importante ter em mente que todos os pacotes são módulos, mas nem
todos os módulos são pacotes. Ou, dito de outra forma, os pacotes são
apenas um tipo especial de módulo. Especificamente, qualquer módulo
que contenha um atributo "__path__" é considerado um pacote.

Todo módulo tem um nome. Nomes de subpacotes são separados do nome do
pacote por um ponto, semelhante à sintaxe de acesso aos atributos
padrão do Python. Assim pode ter um pacote chamado "email", que por
sua vez tem um subpacote chamado "email.mime" e um módulo dentro dele
chamado "email.mime.text".


5.2.1. Pacotes regulares
------------------------

O Python define dois tipos de pacotes, *pacotes regulares* e *pacotes
de espaço de nomes*. Pacotes regulares são pacotes tradicionais, como
existiam no Python 3.2 e versões anteriores. Um pacote regular é
normalmente implementado como um diretório que contém um arquivo
"__init__.py". Quando um pacote regular é importado, esse arquivo
"__init__.py" é executado implicitamente, e os objetos que ele define
são vinculados aos nomes no espaço de nomes do pacote. O arquivo
"__init__.py" pode conter o mesmo código Python que qualquer outro
módulo pode conter, e o Python adicionará alguns atributos adicionais
ao módulo quando ele for importado.

Por exemplo, o layout do sistema de arquivos a seguir define um pacote
"parent" de nível superior com três subpacotes:

   parent/
       __init__.py
       one/
           __init__.py
       two/
           __init__.py
       three/
           __init__.py

A importação de "parent.one" vai executar implicitamente
"parent/__init__.py" e "parent/one/__init__.py".  Importações
subsequentes de "parent.two" ou "parent.three" vão executar
"parent/two/__init__.py" e "parent/three/__init__.py",
respectivamente.

Um subdiretório dentro de um pacote regular que não contém um arquivo
"__init__.py" é tratado como um pacote de espaço de nomes implícito
(um "subpacote de espaço de nomes") enraizado nesse pacote pai.
Consulte a **PEP 420** para a especificação subjacente.


5.2.2. Pacotes de espaço de nomes
---------------------------------

Um pacote de espaço de nomes é um composto de várias *porções*, em que
cada parte contribui com um subpacote para o pacote pai. Partes podem
residir em locais diferentes no sistema de arquivos. Partes também
podem ser encontradas em arquivos zip, na rede ou em qualquer outro
lugar que o Python pesquisar durante a importação. Os pacotes de
espaço de nomes podem ou não corresponder diretamente aos objetos no
sistema de arquivos; eles podem ser módulos virtuais que não têm
representação concreta.

Os pacotes de espaço de nomes não usam uma lista comum para o atributo
"__path__". Em vez disso, eles usam um tipo iterável personalizado que
executará automaticamente uma nova pesquisa por partes do pacote na
próxima tentativa de importação dentro desse pacote, se o caminho do
pacote pai (ou "sys.path" para um pacote de nível superior) for
alterado.

Com pacotes de espaço de nomes, não há arquivo "pai/__init__.py". De
fato, pode haver vários diretórios "pai" encontrados durante a
pesquisa de importação, onde cada um é fornecido por uma parte
diferente. Portanto, "pai/um" pode não estar fisicamente localizado
próximo a "pai/dois". Nesse caso, o Python criará um pacote de espaço
de nomes para o pacote "pai" de nível superior sempre que ele ou um de
seus subpacotes for importado.

Pacotes de espaços de nomes também podem estar aninhados dentro de um
pacote regular. Quando o sistema de importação pesquisa o "__path__"
de um pacote regular e encontra um subdiretório que não contém um
arquivo "__init__.py", esse subdiretório torna-se uma *porção* que
contribui para um subpacote de espaço de nomes do pacote regular que o
contém.

Veja também **PEP 420** para a especificação de pacotes de espaço de
nomes.


5.3. Caminho de busca
=====================

Para iniciar a busca, o Python precisa do nome *completo* do módulo
(ou pacote, mas para o propósito dessa exposição, não há diferença)
que se quer importar. Esse nome vem de vários argumentos passados para
a instrução "import", ou dos parâmetros das funções
"importlib.import_module()" ou "__import__()".

Esse nome será usado em várias fases da busca da importação, e pode
ser um nome com pontos para um submódulo como, por exemplo,
"foo.bar.baz". Nesse caso, Python primeiro tenta importar "foo",
depois "foo.bar" e, finalmente, "foo.bar.baz". Se alguma das
importações intermediárias falharem, uma exceção "ModuleNotFoundError"
é levantada.


5.3.1. O cache de módulos
-------------------------

A primeira verificação durante a busca da importação é feita no
"sys.modules". Esse mapeamento serve como um cache de todos os módulos
que já foram importados previamente, incluindo os caminhos
intermediários. Se "foo.bar.baz" foi previamente importado,
"sys.modules" conterá entradas para "foo", "foo.bar" e "foo.bar.baz".
Cada chave terá como valor um objeto módulo correspondente.

Durante a importação, o nome do módulo é procurado em "sys.modules" e,
se estiver presente, o valor associado é o módulo que satisfaz a
importação, e o processo termina. Entretanto, se o valor é "None", uma
exceção "ModuleNotFoundError" é levantada. Se o nome do módulo não foi
encontrado, Python continuará a busca pelo módulo.

É possível alterar "sys.modules". Apagar uma chave pode não destruir o
objeto módulo associado (outros módulos podem manter referências para
ele), mas a entrada do cache será invalidada para o nome daquele
módulo, fazendo Python executar nova busca na próxima importação. Pode
ser atribuído "None" para a chave, forçando que a próxima importação
do módulo resulte numa exceção "ModuleNotFoundError".

No entanto, tenha cuidado, pois se você mantiver uma referência para o
objeto módulo, invalidar sua entrada de cache em "sys.modules" e, em
seguida, reimportar do módulo nomeado, os dois módulo objetos *não*
serão os mesmos. Por outro lado, o "importlib.reload()" reutilizará o
*mesmo* objeto módulo e simplesmente reinicializará o conteúdo do
módulo executando novamente o código do módulo.


5.3.2. Localizadores e carregadores
-----------------------------------

Se o módulo nomeado não for encontrado em "sys.modules", então o
protocolo de importação do Python é invocado para localizar e carregar
o módulo. Este protocolo consiste em dois objetos conceituais,
*localizadores* e *carregadores*. O trabalho de um localizador é
determinar se ele pode localizar o módulo nomeado usando qualquer
estratégia que ele conheça. Objetos que implementam ambas essas
interfaces são referenciadas como *importadores* -- eles retornam a si
mesmos, quando eles descobrem que eles podem carregar o módulo
requisitado.

Python inclui um número de localizadores e carregadores padrões.  O
primeiro sabe como localizar módulos embutidos, e o segundo sabe como
localizar módulos congelados. Um terceiro localizador padrão procura
em um *caminho de importação* por módulos. O *caminho de importação* é
uma lista de localizações que podem nomear caminhos de sistema de
arquivo ou arquivos zip. Ele também pode ser estendido para buscar por
qualquer recurso localizável, tais como aqueles identificados por
URLs.

O mecanismo de importação é extensível, então novos localizadores
podem ser adicionados para estender o alcance e o escopo de buscar
módulos.

Localizadores na verdade não carregam módulos. Se eles conseguirem
encontrar o módulo nomeado, eles retornam um *spec de módulo*, um
encapsulamento da informação relacionada a importação do módulo, a
qual o mecanismo de importação então usa quando o módulo é carregado.

As seguintes seções descrevem o protocolo para localizadores e
carregadores em mais detalhes, incluindo como você pode criar e
registrar novos para estender o mecanismo de importação.

Alterado na versão 3.4: Em versões anteriores do Python, localizadores
retornavam *carregadores* diretamente, enquanto agora eles retornam
especificações de módulo, as qual *contêm* carregadores. Carregadores
ainda são usados durante a importação, mas possuem menos
responsabilidades.


5.3.3. Ganchos de importação
----------------------------

O mecanismo de importação é desenhado para ser extensível; o mecanismo
primário para isso são os *ganchos de importação*.  Existem dois tipos
de ganchos de importação: *metaganchos* e *ganchos de importação de
caminho*.

Metaganchos são chamados no início do processo de importação, antes
que qualquer outro processo de importação tenha ocorrido, que não seja
busca de cache de "sys.modules". Isso permite aos metaganchos
substituir processamento de "sys.path", módulos congelados ou mesmo
módulos embutidos. Metaganchos são registrados adicionando novos
objetos localizadores a "sys.meta_path", conforme descrito abaixo.

Ganchos de caminho de importação são chamados como parte do
processamento de "sys.path" (ou "package.__path__"), no ponto onde é
encontrado o item do caminho associado. Ganchos de caminho de
importação são registrados adicionando novos chamáveis para
"sys.path_hooks", conforme descrito abaixo.


5.3.4. O metacaminho
--------------------

Quando o módulo nomeado não é encontrado em "sys.modules", o Python em
seguida o busca em "sys.meta_path", o qual contém uma lista de objetos
localizadores de metacaminho. Esses localizadores são consultados a
fim de verificar se eles sabem como manipular o módulo nomeado. Os
localizadores de metacaminho devem implementar um método chamado
"find_spec()", o qual recebe três argumentos: um nome, um caminho de
importação, e (opcionalmente) um módulo alvo. O localizador de
metacaminho pode usar qualquer estratégia que ele quiser para
determinar se ele pode manipular o módulo nomeado ou não.

Se o localizador de metacaminho souber como tratar o módulo nomeado,
ele retorna um objeto spec. Se ele não puder tratar o módulo nomeado,
ele retorna "None". Se o processamento de "sys.meta_path" alcançar o
fim da sua lista sem retornar um spec, então "ModuleNotFoundError" é
levantada. Quaisquer outras exceções levantadas são simplesmente
propagadas para cima, abortando o processo de importação.

O método "find_spec()" dos localizadores de metacaminhos é chamado com
dois ou três argumentos. O primeiro é o nome totalmente qualificado do
módulo sendo importado, por exemplo "foo.bar.baz". O segundo argumento
são as entradas do caminho a ser usado na busca do módulo. Para
módulos de nível superior, o segundo argumento é "None", mas para
submódulos ou subpacotes, o segundo argumento é o valor do atributo
"__path__" do pacote pai. Se o atributo "__path__" apropriado não
puder ser acessado, uma exceção "ModuleNotFoundError" é levantada. O
terceiro argumento é um objeto módulo existente que será o alvo do
carregamento posteriormente. O sistema de importação passa um módulo
alvo apenas durante o recarregamento.

O metacaminho pode ser percorrido múltiplas vezes para uma requisição
de importação individual. Por exemplo, presumindo que nenhum dos
módulos envolvidos já tenha sido cacheado, importar "foo.bar.baz" irá
primeiro executar uma importação de alto nível, chamando
"mpf.find_spec("foo", None, None)" em cada localizador de metacaminho
("mpf"). Depois que "foo" foi importado, "foo.bar" será importado
percorrendo o metacaminho uma segunda vez, chamando
"mpf.find_spec("foo.bar", foo.__path__, None)". Uma vez que "foo.bar"
tenha sido importado, a travessia final irá chamar
"mpf.find_spec("foo.bar.baz", foo.bar.__path__, None)".

Alguns localizadores de metacaminho apenas dão suporte a importações
de alto nível. Estes importadores vão sempre retornar "None" quando
qualquer coisa diferente de "None" for passada como o segundo
argumento.

O "sys.meta_path" padrão do Python possui três localizador de
metacaminho, um que sabe como importar módulos embutidos, um que sabe
como importar módulos congelados, e outro que sabe como importar
módulos de um *caminho de importação* (isto é, o *localizador baseado
no caminho*).

Alterado na versão 3.4: O método "find_spec()" dos localizador de
metacaminho substituiu "find_module()", o qual agora foi
descontinuado. Embora continue a funcionar sem alterações, a mecanismo
de importação só tentará fazê-lo se o localizador não implementar
"find_spec()".

Alterado na versão 3.10: O uso de "find_module()" pelo sistema de
importação agora levanta "ImportWarning".

Alterado na versão 3.12: "find_module()" foi removido. Use
"find_spec()".


5.4. Carregando
===============

Se e quando uma spec de módulo é encontrada, o mecanismo de importação
vai usá-la (e o carregador que ela contém) durante o carregamento do
módulo. Esta é uma aproximação do que acontece durante a etapa de
carregamento de uma importação:

   module = None
   if spec.loader is not None and hasattr(spec.loader, 'create_module'):
       # Assume-se que 'exec_module' também estará definido no carregador..
       module = spec.loader.create_module(spec)
   if module is None:
       module = ModuleType(spec.name)
   # Os atributos de módulo relacionados à importação são definidos aqui:
   _init_module_attrs(spec, module)

   if spec.loader is None:
       # Não suportado
       raise ImportError

   sys.modules[spec.name] = module
   try:
       spec.loader.exec_module(module)
   except BaseException:
       try:
           del sys.modules[spec.name]
       except KeyError:
           pass
       raise
   return sys.modules[spec.name]

Perceba os seguintes detalhes:

* Se houver um objeto módulo existente com o nome fornecido em
  "sys.modules", a importação já tera retornado ele.

* O módulo irá existir em "sys.modules" antes do carregador executar o
  código do módulo. Isso é crucial porque o código do módulo pode
  (direta ou indiretamente) importar a si mesmo; adicioná-lo a
  "sys.modules" antecipadamente previne recursão infinita no pior caso
  e múltiplos carregamentos no melhor caso.

* Se o carregamento falhar, o módulo com falha -- e apenas o módulo
  com falha -- é removido de "sys.modules". Qualquer módulo já
  presente no cache de "sys.modules", e qualquer módulo que tenha sido
  carregado com sucesso como um efeito colateral, deve permanecer no
  cache. Isso contrasta com recarregamento, onde mesmo o módulo com
  falha é mantido em "sys.modules".

* Depois que o módulo é criado, mas antes da execução, o mecanismo de
  importação define os atributos de módulo relacionados a importação
  ("_init_module_attrs" no exemplo de pseudocódigo acima), assim como
  foi resumido em uma seção posterior.

* Execução de módulo é o momento chave do carregamento, no qual o
  espaço de nomes do módulo é populado.  Execução é inteiramente
  delegada para o carregador, o qual pode decidir o que será populado
  e como.

* O módulo criado durante o carregamento e passado para exec_module()
  pode não ser aquele retornado ao final da importação [2].

Alterado na versão 3.4: O sistema de importação tem tomado conta das
responsabilidades inerentes dos carregadores. Essas responsabilidades
eram anteriormente executadas pelo método
"importlib.abc.Loader.load_module".

Alterado na versão 3.15: O método "load_module" não é mais usado.


5.4.1. Carregadores
-------------------

Os carregadores de módulo fornecem a função crítica de carregamento:
execução do módulo. O mecanismo de importação chama o método
"importlib.abc.Loader.exec_module()" com um único argumento, o objeto
do módulo a ser executado. Qualquer valor retornado de "exec_module()"
é ignorado.

Os carregadores devem atender aos seguintes requisitos:

* Se o módulo for um módulo Python (em oposição a um módulo embutido
  ou uma extensão carregada dinamicamente), o carregador deve executar
  o código do módulo no espaço de nomes global do módulo
  ("module.__dict__").

* Se o carregador não puder executar o módulo, ele deve levantar uma
  exceção "ImportError", embora qualquer outra exceção levantada
  durante "exec_module()" será propagada.

Em muitos casos, o localizador e o carregador podem ser o mesmo
objeto; nesses casos o método "find_spec()" apenas retornaria um spec
com o carregador definido como "self".

Os carregadores de módulo podem optar por criar o objeto do módulo
durante o carregamento, implementando um método "create_module()".
Leva um argumento, o spec de módulo e retorna o novo objeto do módulo
para usar durante o carregamento. "create_module()" não precisa
definir nenhum atributo no objeto do módulo. Se o método retornar
"None", o mecanismo de importação criará ele mesmo o novo módulo.

Adicionado na versão 3.4: O método "create_module()" de carregadores.

Alterado na versão 3.4: O método "importlib.abc.Loader.load_module"
foi substituído por "exec_module()" e o mecanismo de importação
assumiu todas as responsabilidades inerentes de carregamento.Para
compatibilidade com carregadores existentes, o mecanismo de importação
usará o método "load_module()" de carregadores se ele existir e o
carregador também não implementar "exec_module()". No entanto,
"load_module()" foi descontinuado e os carregadores devem implementar
"exec_module()" em seu lugar.O método "load_module()" deve implementar
toda a funcionalidade inerente de carregamento descrita acima, além de
executar o módulo. Todas as mesmas restrições se aplicam, com alguns
esclarecimentos adicionais:

* Se houver um objeto de módulo existente com o nome fornecido em
  "sys.modules", o carregador deverá usar esse módulo existente. (Caso
  contrário, "importlib.reload()" não funcionará corretamente.) Se o
  módulo nomeado não existir em "sys.modules", o carregador deverá
  criar um novo objeto de módulo e adicioná-lo a "sys.modules".

* O módulo *deve* existir em "sys.modules" antes que o carregador
  execute o código do módulo, para evitar recursão ilimitada ou
  carregamento múltiplo.

* Se o carregamento falhar, o carregador deverá remover quaisquer
  módulos inseridos em "sys.modules", mas deverá remover **apenas**
  o(s) módulo(s) com falha, e somente se o próprio carregador tiver
  carregado o(s) módulo(s) explicitamente.

Alterado na versão 3.5: Uma exceção "DeprecationWarning" é levantada
quando "exec_module()" está definido, mas "create_module()" não.

Alterado na versão 3.6: Uma exceção "ImportError" é levantada quando
"exec_module()" está definido, mas "create_module()" não.

Alterado na versão 3.10: O uso de "load_module()" vai levantar
"ImportWarning".


5.4.2. Submódulos
-----------------

Quando um submódulo é carregado usando qualquer mecanismo (por
exemplo, APIs "importlib", as instruções "import" ou "import-from", ou
a função "__import__()" embutida) uma ligação é colocada no espaço de
nomes do módulo pai para o objeto submódulo. Por exemplo, se o pacote
"spam" tiver um submódulo "foo", após importar "spam.foo", "spam" terá
um atributo "foo" que está vinculado ao submódulo. Digamos que você
tenha a seguinte estrutura de diretórios:

   spam/
       __init__.py
       foo.py

e "spam/__init__.py" tem a seguinte linha:

   from .foo import Foo

então executar o seguinte coloca ligações de nome para "foo" e "Foo"
no módulo "spam":

   >>> import spam
   >>> spam.foo
   <module 'spam.foo' from '/tmp/imports/spam/foo.py'>
   >>> spam.Foo
   <class 'spam.foo.Foo'>

Dadas as conhecidas regras de ligação de nomes do Python, isso pode
parecer surpreendente, mas na verdade é um recurso fundamental do
sistema de importação. A propriedade invariante é que se você tiver
"sys.modules['spam']" e "sys.modules['spam.foo']" (como faria após a
importação acima), o último deve aparecer como o atributo "foo" do
primeiro.


5.4.3. Especificações de módulo
-------------------------------

O mecanismo de importação utiliza diversas informações sobre cada
módulo durante a importação, principalmente antes do carregamento. A
maior parte das informações é comum a todos os módulos. O propósito da
spec do módulo é encapsular essas informações relacionadas à
importação por módulo.

Usar um spec durante a importação permite que o estado seja
transferido entre componentes do sistema de importação, por exemplo
entre o localizador que cria o spec de módulo e o carregador que o
executa. Mais importante ainda, permite que o mecanismo de importação
execute as operações inerentes de carregamento, enquanto que sem um
spec de módulo o carregador tinha essa responsabilidade.

O spec do módulo é exposto no atributo "module.__spec__". A
configuração oportuna do "__spec__" se aplica igualmente aos módulos
inicializados durante a inicialização do interpretador. A única
exceção é o "__main__", cujo "__spec__" é definido como None em alguns
casos.

Consulte "ModuleSpec" para detalhes sobre o conteúdo do spec de
módulo.

Adicionado na versão 3.4.


5.4.4. Atributo __path__ dos módulos
------------------------------------

O atributo "__path__" deve ser uma *sequência* (possivelmente vazia)
de strings enumerando os locais onde os submódulos do pacote serão
encontrados. Por definição, um módulo que tenha um atributo "__path__"
é um *pacote*.

O atributo "__path__" de um pacote é usado durante as importações de
seus subpacotes. Dentro do mecanismo de importação, funciona da mesma
forma que "sys.path", ou seja, fornecendo uma lista de locais para
procurar módulos durante a importação. Entretanto, o "__path__"
normalmente é muito mais restrito que "sys.path".

As mesmas regras usadas para "sys.path" também se aplicam ao
"__path__" de um pacote. Os "sys.path_hooks" (descritos abaixo) são
consultados ao percorrer o "__path__" de um pacote.

O arquivo "__init__.py" de um pacote pode definir ou alterar o
atributo "__path__" do pacote, e esta era tipicamente a forma como os
pacotes de espaço de nomes eram implementados antes da **PEP 420**.
Com a adoção da **PEP 420**, os pacotes de espaço de nomes não
precisam mais fornecer arquivos "__init__.py" contendo apenas código
de manipulação do "__path__"; o mecanismo de importação define
automaticamente o "__path__" corretamente para o pacote de espaço de
nomes.


5.4.5. Representações do módulo
-------------------------------

Por padrão, todos os módulos têm uma representação (repr) utilizável,
no entanto, dependendo dos atributos definidos acima e do spec do
módulo, você pode controlar mais explicitamente a representação dos
objetos módulo.

Se o módulo tiver um spec ("__spec__"), o mecanismo de importação
tentará gerar uma representação a partir dele. Se isso falhar ou não
houver nenhuma especificação, o sistema de importação criará uma
representação padrão usando qualquer informação disponível no módulo.
Ele tentará usar "module.__name__", "module.__file__" e
"module.__loader__" como entrada para a representação, com padrões
para qualquer informação que esteja faltando.

Arquivo estão as exatas regras usadas:

* Se o módulo tiver um atributo "__spec__", a informação no spec é
  usada para gerar a representação. Os atributos "name", "loader",
  "origin" e "has_location" são consultados.

* Se o módulo tiver um atributo "__file__", ele será usado como parte
  da representação do módulo.

* Se o módulo não tem "__file__" mas tem um "__loader__" que não seja
  "None", então a representação do carregador é usado como parte da
  representação do módulo.

* Caso contrário, basta usar o "__name__" do módulo na representação.

Alterado na versão 3.12: O uso de "module_repr()", descontinuado desde
o Python 3.4, foi removido no Python 3.12 e não é mais chamado durante
a resolução da representação de um módulo.


5.4.6. Invalidação de bytecode em cache
---------------------------------------

Antes do Python carregar o bytecode armazenado em cache de um arquivo
".pyc", ele verifica se o cache está atualizado com o arquivo fonte
".py". Por padrão, o Python faz isso armazenando o registro de data e
hora da última modificação da fonte e o tamanho no arquivo de cache ao
escrevê-lo. No tempo de execução, o sistema de importação valida o
arquivo de cache verificando os metadados armazenados no arquivo de
cache em relação aos metadados do código-fonte.

Python também oferece suporte a arquivos de cache "baseados em hash",
que armazenam um hash do conteúdo do arquivo fonte em vez de seus
metadados. Existem duas variantes de arquivos ".pyc" baseados em hash:
verificados e não verificados. Para arquivos ".pyc" baseados em hash
verificados, o Python valida o arquivo de cache fazendo hash do
arquivo fonte e comparando o hash resultante com o hash no arquivo de
cache. Se um arquivo de cache baseado em hash verificado for inválido,
o Python o regenerará e gravará um novo arquivo de cache baseado em
hash verificado. Para arquivos ".pyc" baseados em hash não
verificados, o Python simplesmente presume que o arquivo de cache é
válido, se existir. O comportamento de validação de arquivos ".pyc"
baseados em hash pode ser substituído pelo sinalizador "--check-hash-
based-pycs".

Alterado na versão 3.7: Adicionados arquivos ".pyc" baseados em hash.
Anteriormente, o Python oferecia suporte apenas à invalidação de
caches de bytecode baseada em registro de data e hora.


5.5. O localizador baseado no caminho
=====================================

Conforme mencionado anteriormente, Python vem com vários localizadores
de metacaminho padrão. Um deles, chamado *localizador baseado no
caminho* ("PathFinder"), pesquisa um *caminho de importação*, que
contém uma lista de *entradas de caminho*. Cada entrada de caminho
nomeia um local para procurar módulos.

O próprio localizador baseado no caminho não sabe como importar nada.
Em vez disso, ele percorre as entradas de caminho individuais,
associando cada uma delas a um localizador de entrada de caminho que
sabe como lidar com esse tipo específico de caminho.

O conjunto padrão de localizadores de entrada de caminho implementa
toda a semântica para localizar módulos no sistema de arquivos,
manipulando tipos de arquivos especiais, como código-fonte Python
(arquivos ".py"), código de bytes Python (arquivos ".pyc") e
bibliotecas compartilhadas (por exemplo, arquivos ".so"). Quando
suportado pelo módulo "zipimport" na biblioteca padrão, os
localizadores de entrada de caminho padrão também lidam com o
carregamento de todos esses tipos de arquivos (exceto bibliotecas
compartilhadas) de arquivos zip.

As entradas de caminho não precisam ser limitadas aos locais do
sistema de arquivos. Eles podem referir-se a URLs, consultas de banco
de dados ou qualquer outro local que possa ser especificado como uma
string.

O localizador baseado no caminho fornece ganchos e protocolos
adicionais para que você possa estender e personalizar os tipos de
entradas de caminho pesquisáveis. Por exemplo, se você quiser oferecer
suporte a entradas de caminho como URLs de rede, poderá escrever um
gancho que implemente a semântica HTTP para localizar módulos na web.
Este gancho (um chamável) retornaria um *localizador de entrada de
caminho* suportando o protocolo descrito abaixo, que foi então usado
para obter um carregador para o módulo da web.

Uma palavra de advertência: esta seção e a anterior usam o termo
*localizador*, distinguindo-os usando os termos *localizador de
metacaminho* e *localizador de entrada de caminho*. Esses dois tipos
de localizadores são muito semelhantes, oferecem suporte a protocolos
semelhantes e funcionam de maneira semelhante durante o processo de
importação, mas é importante ter em mente que eles são sutilmente
diferentes. Em particular, os localizadores de metacaminho operam no
início do processo de importação, conforme a travessia de
"sys.meta_path".

Por outro lado, os localizadores de entrada de caminho são, em certo
sentido, um detalhe de implementação do localizador baseado no caminho
e, de fato, se o localizador baseado no caminho fosse removido de
"sys.meta_path", nenhuma semântica do localizador de entrada de
caminho seria ser invocado.


5.5.1. Localizadores de entrada de caminho
------------------------------------------

O *localizador baseado no caminho* é responsável por encontrar e
carregar módulos e pacotes Python cuja localização é especificada com
uma string *entrada de caminho*. A maioria das entradas de caminho
nomeiam locais no sistema de arquivos, mas não precisam ser limitadas
a isso.

Como um localizador de metacaminho, o *localizador baseado no caminho*
implementa o protocolo "find_spec()" descrito anteriormente, no
entanto, ele expõe ganchos adicionais que podem ser usados para
personalizar como os módulos são encontrados e carregado do *caminho
de importação*.

Três variáveis são usadas pelo *localizador baseado no caminho*,
"sys.path", "sys.path_hooks" e "sys.path_importer_cache". Os atributos
"__path__" em objetos de pacote também são usados. Eles fornecem
maneiras adicionais de personalizar o mecanismo de importação.

"sys.path" contém uma lista de strings fornecendo locais de pesquisa
para módulos e pacotes. Ele é inicializado a partir da variável de
ambiente "PYTHONPATH" e vários outros padrões específicos de
instalação e implementação. Entradas em "sys.path" podem nomear
diretórios no sistema de arquivos, arquivos zip e potencialmente
outros "locais" (veja o módulo "site") que devem ser pesquisados por
módulos, como URLs, ou consultas ao banco de dados. Apenas strings
devem estar presentes em "sys.path"; todos os outros tipos de dados
são ignorados.

O *localizador baseado no caminho* é um *localizador de metacaminho*,
então o mecanismo de importação inicia a pesquisa no *caminho de
importação* chamando o método "find_spec()" do localizador baseado no
caminho conforme descrito anteriormente. Quando o argumento "path"
para "find_spec()" for fornecido, será uma lista de caminhos de string
a serem percorridos -- normalmente o atributo "__path__" de um pacote
para uma importação dentro desse pacote. Se o argumento "path" for
"None", isso indica uma importação de nível superior e "sys.path" é
usado.

O localizador baseado no caminho itera sobre cada entrada no caminho
de pesquisa e, para cada uma delas, procura um *localizador de entrada
de caminho* ("PathEntryFinder") apropriado para a entrada do caminho.
Como esta pode ser uma operação custosa (por exemplo, pode haver
sobrecargas de chamada "stat()" para esta pesquisa), o localizador
baseado no caminho mantém um cache mapeando entradas de caminho para
localizadores de entrada de caminho. Este cache é mantido em
"sys.path_importer_cache" (apesar do nome, este cache na verdade
armazena objetos localizadores em vez de ser limitado a objetos
*importador*). Desta forma, a dispendiosa busca pelo *localizador de
entrada de caminho* de local específico de uma *entrada de caminho* só
precisa ser feita uma vez. O código do usuário é livre para remover
entradas de cache de "sys.path_importer_cache", forçando o localizador
baseado no caminho a realizar a pesquisa de entrada de caminho
novamente.

Se a entrada de caminho não estiver presente no cache, o localizador
baseado no caminho itera sobre cada chamável em "sys.path_hooks". Cada
um dos *ganchos de entrada de caminho* nesta lista é chamado com um
único argumento, a entrada de caminho a ser pesquisada. Este chamável
pode retornar um *localizador de entrada de caminho* que pode
manipular a entrada de caminho ou pode levantar "ImportError". Um
"ImportError" é usado pelo localizador baseado no caminho para
sinalizar que o gancho não consegue encontrar um *localizador de
entrada de caminho* para aquela *entrada de caminho*. A exceção é
ignorada e a iteração com o *caminho de importação* continua. O gancho
deve esperar um objeto string ou bytes; a codificação de objetos bytes
depende do gancho (por exemplo, pode ser uma codificação de sistema de
arquivos, UTF-8 ou outra coisa) e, se o gancho não puder decodificar o
argumento, ele deve levantar "ImportError".

Se a iteração "sys.path_hooks" terminar sem que nenhum *localizador de
entrada de caminho* seja retornado, o método "find_spec()" do
localizador baseado no caminho armazenará "None" em
"sys.path_importer_cache" (para indicar que não há um localizador para
esta entrada de caminho) e retornará "None", indicando que este
*localizador de metacaminho* não conseguiu encontrar o módulo.

Se um *localizador de entrada de caminho* *for* retornado por um dos
chamáveis de *gancho de entrada de caminho* em "sys.path_hooks", então
o seguinte protocolo é usado para solicitar ao localizador um spec de
módulo, que é então usada ao carregar o módulo.

O diretório de trabalho atual -- denotado por uma string vazia -- é
tratado de forma ligeiramente diferente de outras entradas em
"sys.path". Primeiro, se o diretório de trabalho atual não puder ser
determinado ou for considerado inexistente, nenhum valor será
armazenado em "sys.path_importer_cache". Segundo, o valor para o
diretório de trabalho atual é pesquisado novamente para cada pesquisa
de módulo. Terceiro, o caminho usado para "sys.path_importer_cache" e
retornado por "importlib.machinery.PathFinder.find_spec()" será o
diretório de trabalho atual real e não a string vazia.


5.5.2. Protocolo do localizador de entrada de caminho
-----------------------------------------------------

Para dar suporte a importações de módulos e pacotes inicializados e
também contribuir com partes para pacotes de espaço de nomes, os
localizadores de entrada de caminho devem implementar o método
"find_spec()".

"find_spec()" recebe dois argumentos: o nome totalmente qualificado do
módulo que está sendo importado e o módulo de destino (opcional).
"find_spec()" retorna um spec totalmente preenchido para o módulo.
Este spec sempre terá "loader" definido (com uma exceção).

Para indicar ao maquinário de importação que o spec representa uma
*porção* de espaço de nomes, o localizador de entrada de caminho
define "submodule_search_locations" como uma lista contendo a porção.

Alterado na versão 3.4: "find_spec()" substituiu "find_loader()" e
"find_module()", ambos descontinuados, mas serão usados se
"find_spec()" não estiver definido.Os localizadores de entrada de
caminho mais antigos podem implementar um desses dois métodos
descontinuados em vez de "find_spec()". Os métodos ainda são
respeitados para fins de compatibilidade com versões anteriores. No
entanto, se "find_spec()" for implementado no localizador de entrada
de caminho, os métodos legados serão ignorados."find_loader()" recebe
um argumento, o nome totalmente qualificado do módulo que está sendo
importado. "find_loader()" retorna uma tupla 2 onde o primeiro item é
o carregador e o segundo item é uma *porção* de espaço de nomes.Para
compatibilidade com versões anteriores de outras implementações do
protocolo de importação, muitos localizadores de entrada de caminho
também dão suporte ao mesmo método tradicional "find_module()" que os
localizadores de metacaminho. No entanto, os métodos "find_module()"
do localizador de entrada de caminho nunca são chamados com um
argumento "path" (espera-se que eles registrem as informações de
caminho apropriadas da chamada inicial para o gancho de caminho).O
método "find_module()" em localizadores de entrada de caminho foi
descontinuado, pois não permite que o localizador de entrada de
caminho contribua com porções para pacotes de espaço de nomes. Se
"find_loader()" e "find_module()" existirem em um localizador de
entrada de caminho, o sistema de importação sempre chamará
"find_loader()" em preferência a "find_module()".

Alterado na versão 3.10: Chamadas para "find_module()" e
"find_loader()" pelo sistema de importação vão levantar
"ImportWarning".

Alterado na versão 3.12: "find_module()" e "find_loader()" foram
removidos.


5.6. Substituindo o sistema de importação padrão
================================================

O mecanismo mais confiável para substituir todo o sistema de
importação é excluir o conteúdo padrão de "sys.meta_path",
substituindo-o inteiramente por um gancho de metacaminho
personalizado.

Se for aceitável alterar apenas o comportamento de instruções de
importação sem afetar outras APIs que acessam o sistema de importação,
então substituir a função embutida "__import__()" pode ser suficiente.

Para impedir seletivamente a importação de alguns módulos de um gancho
no início do metacaminho (em vez de desabilitar o sistema de
importação padrão completamente), é suficiente levantar
"ModuleNotFoundError" diretamente de "find_spec()" em vez de retornar
"None". O último indica que a busca do metacaminho deve continuar,
enquanto levantar uma exceção a encerra imediatamente.


5.7. Importações relativas ao pacote
====================================

Importações relativas usam caracteres de ponto no início. Um único
ponto no início indica uma importação relativa, começando com o pacote
atual. Dois ou mais pontos no início indicam uma importação relativa
para o(s) pai(s) do pacote atual, um nível por ponto após o primeiro.
Por exemplo, dado o seguinte layout de pacote:

   package/
       __init__.py
       subpackage1/
           __init__.py
           moduleX.py
           moduleY.py
       subpackage2/
           __init__.py
           moduleZ.py
       moduleA.py

Em "subpackage1/moduleX.py" ou "subpackage1/__init__.py", as seguintes
são importações relativas válidas:

   from .moduleY import spam
   from .moduleY import spam as ham
   from . import moduleY
   from ..subpackage1 import moduleY
   from ..subpackage2.moduleZ import eggs
   from ..moduleA import foo

Importações absolutas podem usar a sintaxe "import <>" ou "from <>
import <>", mas importações relativas podem usar apenas a segunda
forma; o motivo para isso é que:

   import XXX.YYY.ZZZ

deve expor "XXX.YYY.ZZZ" como uma expressão utilizável, mas .moduleY
não é uma expressão válida.


5.8. Considerações especiais para __main__
==========================================

O módulo "__main__" é um caso especial em relação ao sistema de
importação do Python. Conforme observado em em outro lugar, o módulo
"__main__" é inicializado diretamente na inicialização do
interpretador, muito parecido com "sys" e "builtins". No entanto,
diferentemente desses dois, ele não se qualifica estritamente como um
módulo integrado. Isso ocorre porque a maneira como "__main__" é
inicializado depende dos sinalizadores e outras opções com as quais o
interpretador é invocado.


5.8.1. __main__.__spec__
------------------------

Dependendo de como "__main__" é inicializado, "__main__.__spec__" é
definido apropriadamente ou como "None".

Quando o Python é iniciado com a opção "-m", "__spec__" é definido
como o spec de módulo ou pacote correspondente. "__spec__" também é
preenchido quando o módulo "__main__" é carregado como parte da
execução de um diretório, arquivo zip ou outra entrada "sys.path".

Nos demais casos, "__main__.__spec__" é definido como "None", pois o
código usado para preencher o "__main__" não corresponde diretamente a
um módulo importável:

* prompt interativo

* opção "-c"

* executar a partir de stdin

* executar diretamente de um arquivo de código-fonte ou bytecode

Note que "__main__.__spec__" é sempre "None" no último caso, *mesmo
se* o arquivo pudesse ser importado diretamente como um módulo. Use a
opção "-m" se metadados de módulo válidos forem desejados em
"__main__".

Note também que mesmo quando "__main__" corresponde a um módulo
importável e "__main__.__spec__" é definido adequadamente, eles ainda
são considerados módulos *distintos*. Isso se deve ao fato de que os
blocos protegidos por verificações "if __name__ == "__main__":" são
executados somente quando o módulo é usado para preencher o espaço de
nomes "__main__", e não durante a importação normal.


5.9. Referências
================

O maquinário de importação evoluiu consideravelmente desde os
primeiros dias do Python. A especificação original para pacotes ainda
está disponível para leitura, embora alguns detalhes tenham mudado
desde a escrita desse documento.

A especificação original para "sys.meta_path" era **PEP 302**, com
extensão subsequente em **PEP 420**.

**PEP 420** introduziu *pacotes de espaço de nomes* para Python 3.3.
**PEP 420** também introduziu o protocolo "find_loader()" como uma
alternativa ao "find_module()".

**PEP 366** descreve a adição do atributo "__package__" para
importações relativas explícitas em módulos principais.

**PEP 328** introduziu importações relativas absolutas e explícitas e
inicialmente propôs "__name__" para semântica. **PEP 366**
eventualmente especificaria "__package__".

**PEP 338** define módulos de execução como scripts.

**PEP 451** adiciona o encapsulamento do estado de importação por
módulo em objetos spec. Ele também descarrega a maioria das
responsabilidades inerentes dos carregadores de volta para o
maquinário de importação. Essas mudanças permitem a descontinuação de
várias APIs no sistema de importação e também a adição de novos
métodos para localizadores e carregadores.

-[ Notas de rodapé ]-

[1] Veja "types.ModuleType".

[2] A implementação de importlib evita usar o valor de retorno
    diretamente. Em vez disso, ela obtém o objeto do módulo procurando
    o nome do módulo em "sys.modules". O efeito indireto disso é que
    um módulo importado pode substituir a si mesmo em "sys.modules".
    Esse é um comportamento específico da implementação que não tem
    garantia de funcionar em outras implementações do Python.
