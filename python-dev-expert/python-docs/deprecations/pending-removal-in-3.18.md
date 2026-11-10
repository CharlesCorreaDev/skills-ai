Remoção pendente no Python 3.18
*******************************

* Não aceita mais um valor booleano quando um descritor de arquivo é
  esperado. (Contribuição de Serhiy Storchaka em gh-82626.)

* "decimal":

  * O especificador de formato de "Decimal" não padrão e não
    documentado "'N'", que só é suportado na implementação C do módulo
    "decimal", foi descontinuada desde o Python 3.13. (Contribuição de
    Serhiy Storchaka em gh-89902.)

* Descontinuações definidas por **PEP 829**:

  * Linhas de "import" em arquivos "*name*.pth" são silenciosamente
    ignoradas.

  (Contribuição de Barry Warsaw em gh-148641.)
