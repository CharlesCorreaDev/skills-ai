Remoção pendente no Python 3.20
*******************************

* Chamar o método "__new__()" de "struct.Struct" sem o argumento
  *format* está descontinuado e será removido no Python 3.20. Chamar o
  método "__init__()" em objetos "Struct" já inicializados está
  descontinuado e será removido no Python 3.20.

  (Contribuição de Sergey B Kirpichev e Serhiy Storchaka em
  gh-143715.)

* Os atributos "__version__", "version" e "VERSION" foram
  descontinuados nestes módulos da biblioteca padrão e serão removidos
  no Python 3.20. Utilize "sys.version_info" em seu lugar.

  * "argparse"

  * "csv"

  * "ctypes"

  * "ctypes.macholib"

  * "decimal" (use "decimal.SPEC_VERSION")

  * "http.server"

  * "imaplib"

  * "ipaddress"

  * "json"

  * "logging" ("__date__" também descontinuado)

  * "optparse"

  * "pickle"

  * "platform"

  * "re"

  * "socketserver"

  * "tabnanny"

  * "tarfile"

  * "tkinter.font"

  * "tkinter.ttk"

  * "wsgiref.simple_server"

  * "xml.etree.ElementTree"

  * "xml.sax.expatreader"

  * "xml.sax.handler"

  * "zlib"

  (Contribuição de Hugo van Kemenade e Stan Ulbrych em gh-76007.)

* Descontinuações definidas por **PEP 829**:

  * Avisos são gerados para linhas "import" encontradas em arquivos
    "*name*.pth".

  * Arquivos "*name*.pth" não são mais decodificados usando a
    codificação da localidade (*locale encoding*) por padrão. Eles
    **DEVEM** estar codificados em "utf-8-sig".

  (Contribuição de Barry Warsaw em gh-148641.)

* "ast":

  * A criação de instâncias de nós abstratos da AST (como "ast.AST" ou
    "ast.expr") está descontinuada e levantará um erro no Python 3.20.

* "typing":

  * É desencorajado realizar verificações com "isinstance()" e
    "issubclass()" em classes de protocolo que não foram
    explicitamente decoradas com "runtime_checkable()", mas que herdam
    de uma classe de protocolo verificável em tempo de execução. Isso
    resultará em um "TypeError" no Python 3.20.

    (Contribuição de Bartosz Sławecki em gh-132604.)
