"importlib.resources" -- Leitura, abertura e acesso a recursos de pacotes
*************************************************************************

**Código-fonte:** Lib/importlib/resources/__init__.py

======================================================================

Adicionado na versão 3.7.

Esse módulo aproveita o sistema de importação do Python para fornecer
acesso a *recursos* dentro de *pacotes*.

"Recursos" são recursos arquivo ou similares associados a um módulo ou
pacote em Python. Os recursos podem estar contidos diretamente em um
pacote, em um subdiretório contido nesse pacote ou adjacentes a
módulos fora de um pacote. Os recursos podem ser de texto ou binários.
Como resultado, as fontes de módulos Python de um pacote (.py),
artefatos de compilação (pycache) e artefatos de instalação (como
"nomes de arquivos reservados" em diretórios) são tecnicamente
recursos de fato desse pacote. Na prática, entretanto, os recursos são
principalmente os artefatos não-Python expostos especificamente pelo
autor do pacote.

Os recursos podem ser abertos ou lidos no modo binário ou de texto.

Os recursos são mais ou menos semelhantes a arquivos dentro de
diretórios, embora seja importante ter em mente que isso é apenas uma
metáfora.  Recursos e pacotes **não** precisam existir como arquivos e
diretórios físicos no sistema de arquivos: por exemplo, um pacote e
seus recursos podem ser importados de um arquivo zip usando
"zipimport".

Aviso:

  "importlib.resources" follows the same security model as the built-
  in "open()" function. Passing untrusted inputs to the functions in
  this module is unsafe.

Nota:

  O backport autônomo desse módulo fornece mais informações sobre uso
  do importlib.resources e migração do pkg_resources para o
  importlib.resources.

"Loaders" que desejam oferecer suporte à leitura de recursos devem
implementar um método "get_resource_reader(fullname)" conforme
especificado por "importlib.resources.abc.ResourceReader".

class importlib.resources.Anchor

   Representa uma âncora para recursos, seja um "objeto módulo" ou um
   nome de módulo como uma string. Definido como "Union[str,
   ModuleType]".

importlib.resources.files(anchor: Anchor | None = None)

   Retorna um objeto "Traversable" que representa o contêiner de
   recursos (pense em diretório) e seus recursos (pense em arquivos).
   Um Traversable pode conter outros contêineres (pense em
   subdiretórios).

   *anchor* é um "Anchor" opcional. Se a âncora for um pacote, os
   recursos são resolvidos a partir desse pacote. Se for um módulo, os
   recursos são resolvidos ao lado desse módulo (no mesmo pacote ou na
   raiz do pacote). Se a âncora for omitida, o módulo do chamador é
   usado.

   Adicionado na versão 3.9.

   Alterado na versão 3.12: *package* parameter was renamed to
   *anchor*. *package* was still accepted, but deprecated.

   Alterado na versão 3.15: *package* parameter was fully removed.
   *anchor* can now be a non-package module and if omitted will
   default to the caller's module. *package* is no longer accepted
   since Python 3.15. Consider passing the anchor positionally or
   using "importlib_resources >= 5.10" for a compatible interface on
   older Pythons.

importlib.resources.as_file(traversable)

   Dado um objeto "Traversable" que representa um arquivo ou
   diretório, normalmente de "importlib.resources.files()", retorna um
   gerenciador de contexto para uso em uma instrução "with". O
   gerenciador de contexto fornece um objeto "pathlib.Path".

   Sair do gerenciador de contexto limpa qualquer arquivo ou diretório
   temporário criado quando o recurso foi extraído, por exemplo, de um
   arquivo zip.

   Use "as_file" quando os métodos de Traversable ("read_text", etc.)
   forem insuficientes e for necessário um arquivo ou diretório real
   no sistema de arquivos.

   Adicionado na versão 3.9.

   Alterado na versão 3.12: Adicionado suporte para *traversable*
   representando um diretório.


API funcional
=============

Um conjunto de auxiliares simplificados e compatíveis com versões
anteriores está disponível. Estes permitem operações comuns em uma
única chamada de função.

Para todas as funções a seguir:

* *anchor* é um "Anchor", assim como em "files()". Ao contrário do
  comportamento em "files", *anchor* aqui não pode ser omitido.

* *path_names* são componentes do nome do caminho de um recurso,
  relativo à âncora. Por exemplo, para obter o texto de um recurso
  chamado "info.txt", use:

     importlib.resources.read_text(my_module, "info.txt")

  Assim como em "Traversable.joinpath", os componentes individuais
  devem usar barras ordinárias ("/") como separadores do caminho. Por
  exemplo, as seguintes chamadas são equivalentes:

     importlib.resources.read_binary(my_module, "pics/painting.png")
     importlib.resources.read_binary(my_module, "pics", "painting.png")

  Por motivos de compatibilidade com versões anteriores, funções que
  leem texto requerem um argumento *encoding* explícito se múltiplos
  *path_names* forem fornecidos. Por exemplo, para obter o texto de
  "info/chapter1.txt", use:

     importlib.resources.read_text(my_module, "info", "chapter1.txt",
                                   encoding='utf-8')

importlib.resources.open_binary(anchor, *path_names)

   Abre o recurso nomeado para leitura binária.

   Veja a introdução para detalhes sobre *anchor* e *path_names*.

   Esta função retorna um objeto "BinaryIO", isto é, um fluxo binário
   aberto para leitura.

   Esta função é mais ou menos equivalente a:

      files(anchor).joinpath(*path_names).open('rb')

   Alterado na versão 3.13: Múltiplos *path_names* são aceitos.

importlib.resources.open_text(anchor, *path_names, encoding='utf-8', errors='strict')

   Abre o recurso nomeado para leitura de texto. Por padrão, o
   conteúdo é lido como UTF-8 estrito.

   Veja a introdução para detalhes sobre *anchor* e *path_names*.
   *encoding* e *errors* têm o mesmo significado que na embutida
   "open()".

   Por motivos de compatibilidade com versões anteriores, o argumento
   *encoding* precisa ser passado explicitamente se houver múltiplos
   *path_names*. Essa limitação está agendada para ser removida no
   Python 3.15.

   Esta função retorna um objeto "TextIO", isto é, um fluxo de texto
   aberto para leitura.

   Esta função é mais ou menos equivalente a:

      files(anchor).joinpath(*path_names).open('r', encoding=encoding)

   Alterado na versão 3.13: Múltiplos *path_names* são aceitos.
   *encoding* e *errors* precisam ser fornecidos como argumentos
   nomeados.

importlib.resources.read_binary(anchor, *path_names)

   Lê e retorna o conteúdo do recurso nomeado como "bytes".

   Veja a introdução para detalhes sobre *anchor* e *path_names*.

   Esta função é mais ou menos equivalente a:

      files(anchor).joinpath(*path_names).read_bytes()

   Alterado na versão 3.13: Múltiplos *path_names* são aceitos.

importlib.resources.read_text(anchor, *path_names, encoding='utf-8', errors='strict')

   Lê e retorna o conteúdo do recurso nomeado como "str". Por padrão,
   o conteúdo é lido como UTF-8 estrito.

   Veja a introdução para detalhes sobre *anchor* e *path_names*.
   *encoding* e *errors* têm o mesmo significado que na embutida
   "open()".

   Por motivos de compatibilidade com versões anteriores, o argumento
   *encoding* precisa ser passado explicitamente se houver múltiplos
   *path_names*. Essa limitação está agendada para ser removida no
   Python 3.15.

   Esta função é mais ou menos equivalente a:

      files(anchor).joinpath(*path_names).read_text(encoding=encoding)

   Alterado na versão 3.13: Múltiplos *path_names* são aceitos.
   *encoding* e *errors* precisam ser fornecidos como argumentos
   nomeados.

importlib.resources.path(anchor, *path_names)

   Fornece o caminho para o *resource* como um caminho real do sistema
   de arquivos.  Essa função retorna um gerenciador de contexto para
   uso em uma instrução "with". O gerenciador de contexto fornece um
   objeto "pathlib.Path".

   Sair do gerenciador de contexto limpa qualquer arquivo temporário
   criado, por exemplo quando o recurso precisa ser extraído de um
   arquivo zip.

   Por exemplo, o método "stat()" requer um caminho real em um sistema
   de arquivos; ele pode ser usado assim:

      with importlib.resources.path(anchor, "resource.txt") as fspath:
          result = fspath.stat()

   Veja a introdução para detalhes sobre *anchor* e *path_names*.

   Esta função é mais ou menos equivalente a:

      as_file(files(anchor).joinpath(*path_names))

   Alterado na versão 3.13: Múltiplos *path_names* são aceitos.

importlib.resources.is_resource(anchor, *path_names)

   Retorna "True" se o recurso nomeado existe, senão "False". Esta
   função não considera diretórios como sendo recursos.

   Veja a introdução para detalhes sobre *anchor* e *path_names*.

   Esta função é mais ou menos equivalente a:

      files(anchor).joinpath(*path_names).is_file()

   Alterado na versão 3.13: Múltiplos *path_names* são aceitos.

importlib.resources.contents(anchor, *path_names)

   Retorna um iterável sobre os itens nomeados no pacote ou caminho. O
   iterável retorna nomes de recursos (por exemplo, arquivos) e outros
   itens que não recursos (por exemplo, diretórios) como "str". O
   iterável não recorre em subdiretórios.

   Veja a introdução para detalhes sobre *anchor* e *path_names*.

   Esta função é mais ou menos equivalente a:

      for resource in files(anchor).joinpath(*path_names).iterdir():
          yield resource.name

   Descontinuado desde a versão 3.11: Prefira "iterdir()" como acima,
   que oferece mais controle sobre os resultados e funcionalidade mais
   rica.
