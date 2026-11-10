Remoção pendente no Python 3.14
*******************************

* "argparse": Os parâmetros *type*, *choices* e *metavar* de
  "argparse.BooleanOptionalAction" foram descontinuados e serão
  removidos na versão 3.14. (Contribuição de Nikita Sobolev em
  gh-92248.)

* "ast": Os seguintes recursos foram descontinuados na documentação
  desde Python 3.8, agora fazem com que um "DeprecationWarning" seja
  emitido em tempo de execução quando eles são acessados ou usados, e
  serão removidos no Python 3.14:

  * "ast.Num"

  * "ast.Str"

  * "ast.Bytes"

  * "ast.NameConstant"

  * "ast.Ellipsis"

  Usa "ast.Constant" em vez disso. (Contribuição de Serhiy Storchaka
  em gh-90953.)

* "asyncio":

  * As classes filhas dos observadores
    "asyncio.MultiLoopChildWatcher", "asyncio.FastChildWatcher",
    "asyncio.AbstractChildWatcher" e "asyncio.SafeChildWatcher" foram
    descontinuadas e serão removidas no Python 3.14. (Contribuição de
    Kumar Aditya em gh-94597.)

  * "asyncio.set_child_watcher()", "asyncio.get_child_watcher()",
    "asyncio.AbstractEventLoopPolicy.set_child_watcher()" e
    "asyncio.AbstractEventLoopPolicy.get_child_watcher()" foram
    descontinuados e serão removidos no Python 3.14. (Contribuição de
    Kumar Aditya em gh-94597.)

  * O método "get_event_loop()" da política de laço de eventos padrão
    agora emite um "DeprecationWarning" se não houver nenhum laço de
    eventos atual definido e decidir criar um. (Contribuição de Serhiy
    Storchaka e Guido van Rossum em gh-100160.)

* "email": Descontinua o parâmetro *isdst* em
  "email.utils.localtime()". (Contribuição de Alan Williams em
  gh-72346.)

* "importlib.abc" descontinuou as classes:

  * "importlib.abc.ResourceReader"

  * "importlib.abc.Traversable"

  * "importlib.abc.TraversableResources"

  Em vez disso, use classes "importlib.resources.abc":

  * "importlib.resources.abc.Traversable"

  * "importlib.resources.abc.TraversableResources"

  (Contribuição de Jason R. Coombs e Hugo van Kemenade em gh-93963.)

* "itertools" tinha suporte não documentado, ineficiente,
  historicamente cheio de bugs e inconsistente para operações de
  cópia, cópia profunda e serialização com pickle. Isso será removido
  na versão 3.14 para uma redução significativa no volume de código e
  na carga de manutenção. (Contribuição de Raymond Hettinger em
  gh-101588.)

* "multiprocessing": O método de inicialização padrão será alterado
  para um mais seguro no Linux, BSDs e outras plataformas POSIX não-
  macOS onde "'fork'" é atualmente o padrão (gh-84559). Adicionar um
  aviso de tempo de execução sobre isso foi considerado muito
  perturbador, pois não se espera que a maior parte do código se
  importe. Use as APIs "get_context()" ou "set_start_method()" para
  especificar explicitamente quando seu código *requer* "'fork'". Veja
  Contextos e métodos de inicialização.

* "pathlib": "is_relative_to()" e "relative_to()": passar argumentos
  adicionais foi descontinuado.

* "pkgutil": "pkgutil.find_loader()" e "pkgutil.get_loader()" agora
  levantam "DeprecationWarning"; use "importlib.util.find_spec()".
  (Contribuição de Nikita Sobolev em gh-97850.)

* "pty":

  * "master_open()": use "pty.openpty()".

  * "slave_open()": use "pty.openpty()".

* "sqlite3":

  * "version" e "version_info".

  * "execute()" e "executemany()" se espaços reservados nomeados forem
    usados e *parameters* for uma sequência em vez de um "dict" .

* "urllib": "urllib.parse.Quoter" está obsoleto: não foi planejado
  para ser uma API pública. (Contribuição de Gregory P. Smith em
  gh-88168.)
