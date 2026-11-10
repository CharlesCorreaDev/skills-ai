"runpy" --- Localizando e executando módulos Python
***************************************************

**Código-fonte:** Lib/runpy.py

======================================================================

The "runpy" module is used to locate and run Python modules without
importing them first. Its main use is to implement the "-m" command
line switch that allows scripts to be located using the Python module
namespace rather than the filesystem.

Observe que este *não* é um módulo isolado - todo o código é executado
no processo atual, e quaisquer efeitos colaterais (como importações em
cache de outros módulos) irão permanecer em vigor após o retorno da
função.

Furthermore, any functions and classes defined by the executed code
are not guaranteed to work correctly after a "runpy" function has
returned. If that limitation is not acceptable for a given use case,
"importlib" is likely to be a more suitable choice than this module.

The "runpy" module provides two functions:

runpy.run_module(mod_name, init_globals=None, run_name=None, alter_sys=False)

   Executa o código do módulo especificado e retorna o dicionário de
   globals do módulo resultante. O código do módulo é localizado
   primeiro usando o mecanismo de importação padrão (consulte **PEP
   302** para detalhes) e então executado em um novo espaço de nomes
   de módulo.

   O argumento *mod_name* deve ser um nome de módulo absoluto. Se o
   nome do módulo se referir a um pacote ao invés de um módulo normal,
   então esse pacote é importado e o submódulo "__main__" dentro desse
   pacote é então executado e o dicionário global do módulo resultante
   retornado.

   O argumento opcional de dicionário *init_globals* pode ser usado
   para preencher previamente o dicionário global do módulo antes do
   código ser executado. *init_globals* não será modificado. Se
   qualquer uma das variáveis globais especiais abaixo for definida em
   *init_globals*, estas definições serão substituídas por
   "run_module()".

   The special global variables "__name__", "__spec__", "__file__",
   "__loader__" and "__package__" are set in the globals dictionary
   before the module code is executed. (Note that this is a minimal
   set of variables - other variables may be set implicitly as an
   interpreter implementation detail.)

   "__name__" é definido como *run_name* se este argumento opcional
   não for "None", para "mod_name + '.__main__'" se o módulo nomeado
   for um pacote e para o argumento *mod_name* caso contrário .

   "__spec__" será definido adequadamente para o módulo *efetivamente*
   importado (isto é, "__spec__.name" vai sempre ser *mod_name* ou
   "mod_name + '.__main__'", nunca *run_name*).

   "__file__", "__loader__" and "__package__" are set as normal based
   on the module spec.

   Se o argumento *alter_sys* for fornecido e for avaliado como
   "True", então "sys.argv[0]" será atualizado com o valor de
   "__file__" e "sys.modules[__name__]" é atualizado com um objeto de
   módulo temporário para o módulo que está sendo executado. Ambos
   "sys.argv[0]" e "sys.modules[__name__]" são restaurados para seus
   valores originais antes que a função retorne.

   Note que esta manipulação de "sys" não é segura para thread. Outras
   threads podem ver o módulo parcialmente inicializado, bem como a
   lista alterada de argumentos. É recomendado que o módulo "sys" seja
   deixado sozinho ao invocar esta função a partir do código
   encadeado.

   Ver também:

     A opção "-m" oferece funcionalidade equivalente na linha de
     comando.

   Alterado na versão 3.1: Adicionada capacidade de executar pacotes
   procurando por um submódulo "__main__".

   Alterado na versão 3.2: Adicionada a variável global "__cached__"
   (veja **PEP 3147**).

   Alterado na versão 3.4: Atualizado para aproveitar o recurso de
   spec de módulo adicionado por **PEP 451**. Isso permite que
   "__cached__" seja configurado corretamente para módulos executados
   desta forma, assim como garante que o nome real do módulo esteja
   sempre acessível como "__spec__.name".

   Alterado na versão 3.12: A definição de "__cached__", "__loader__"
   e "__package__" foi descontinuada. Veja "ModuleSpec" para
   alternativas.

   Alterado na versão 3.15: The global variable "__cached__" is no
   longer set.

runpy.run_path(path_name, init_globals=None, run_name=None)

   Executa o código no local do sistema de arquivos nomeado e retorna
   o dicionário de globals do módulo resultante. Assim como um nome de
   script fornecido à linha de comando CPython, *file_path* pode se
   referir a um arquivo fonte Python, um arquivo compilado em bytecode
   ou uma entrada válida de "sys.path" contendo um módulo "__main__"
   (por exemplo, um arquivo zip contendo um arquivo de nível superior
   "__main__.py").

   Para um script simples, o código especificado é simplesmente
   executado em um novo espaço de nomes de módulo. Para uma entrada
   válida "sys.path" (normalmente um arquivo zip ou diretório), a
   entrada é primeiro adicionada ao início de "sys.path". A função
   então procura e executa um módulo "__main__" usando o caminho
   atualizado. Observe que não há proteção especial contra invocar uma
   entrada "__main__" existente localizada em outro lugar em
   "sys.path" se não houver tal módulo no local especificado.

   O argumento opcional de dicionário *init_globals* pode ser usado
   para preencher previamente o dicionário de globals do módulo antes
   do código ser executado. *init_globals* não será modificado. Se
   qualquer uma das variáveis globais especiais abaixo for definida em
   *init_globals*, estas definições serão substituídas por
   "run_path()".

   The special global variables "__name__", "__spec__", "__file__",
   "__loader__" and "__package__" are set in the globals dictionary
   before the module code is executed. (Note that this is a minimal
   set of variables - other variables may be set implicitly as an
   interpreter implementation detail.)

   "__name__" é definido como *run_name* se este argumento opcional
   não for "None" e como "'<run_path>'" caso contrário.

   If *file_path* directly references a script file (whether as source
   or as precompiled byte code), then "__file__" will be set to
   *file_path*, and "__spec__", "__loader__" and "__package__" will
   all be set to "None".

   If *file_path* is a reference to a valid "sys.path" entry, then
   "__spec__" will be set appropriately for the imported "__main__"
   module (that is, "__spec__.name" will always be "__main__").
   "__file__", "__loader__" and "__package__" will be set as normal
   based on the module spec.

   Várias alterações também são feitas no módulo "sys". Primeiramente,
   "sys.path" pode ser alterado conforme descrito acima. "sys.argv[0]"
   é atualizado com o valor de *file_path* e "sys.modules[__name__]" é
   atualizado com um objeto de módulo temporário para o módulo que
   está sendo executado. Todas as modificações em itens em "sys" são
   revertidas antes que a função retorne.

   Note que, diferentemente de "run_module()", as alterações feitas em
   "sys" não são opcionais nesta função, pois esses ajustes são
   essenciais para permitir a execução das entradas do "sys.path".
   Como as limitações de segurança de threads ainda se aplicam, o uso
   dessa função no código encadeado deve ser serializado com a trava
   de importação ou delegado a um processo separado.

   Ver também:

     Opções de interface para funcionalidade equivalente na linha de
     comando ("python path/to/script").

   Adicionado na versão 3.2.

   Alterado na versão 3.4: Atualizado para aproveitar o recurso de
   spec de módulo adicionado por **PEP 451**. Isso permite que
   "__cached__" seja definido corretamente no caso em que "__main__" é
   importado de uma entrada "sys.path" válida em vez de ser executado
   diretamente.

   Alterado na versão 3.12: A definição de "__cached__", "__loader__"
   e "__package__" foi descontinuada.

   Alterado na versão 3.15: The global variable "__cached__" is no
   longer set.

Ver também:

  **PEP 338** -- Executando módulos como scripts
     PEP escrita e implementada por Nick Coghlan.

  **PEP 366** -- Importações relativas explícitas do módulo principal
     PEP escrita e implementada por Nick Coghlan.

  **PEP 451** -- Um tipo ModuleSpec para o sistema de importação
     PEP escrita e implementada por Eric Snow

  Linha de comando e ambiente - Detalhes da linha de comando do
  CPython

  A função "importlib.import_module()"
