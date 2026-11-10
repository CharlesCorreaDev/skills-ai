"zipimport" - Importa módulos de arquivos Zip
*********************************************

**Código-fonte:** Lib/zipimport.py

======================================================================

Este módulo adiciona a capacidade de importar módulos Python ("*.py",
"*.pyc") e pacotes de arquivos em formato ZIP. Normalmente, não é
necessário usar o módulo "zipimport" explicitamente; ele é usado
automaticamente pelo mecanismo embutido no "import" para itens
"sys.path" que são caminhos para arquivos ZIP.

Normalmente, "sys.path" é uma lista de nomes de diretórios como
strings. Este módulo também permite que um item de "sys.path" seja uma
string que nomeia um arquivo ZIP. O arquivo ZIP pode conter uma
estrutura de subdiretório para suportar importações de pacotes, e um
caminho dentro do arquivo pode ser especificado para importar apenas
de um subdiretório. Por exemplo, o caminho "example.zip/lib/"
importaria apenas do subdiretório "lib/" dentro do arquivo.

Quaisquer arquivos podem estar presentes no arquivo ZIP, mas os
importadores são invocados apenas para os arquivos ".py" e ".pyc". A
importação ZIP de módulos dinâmicos (".pyd", ".so") não é permitida.
Observe que, se um arquivo contiver apenas arquivos ".py", o Python
não tentará modificá-lo adicionando o arquivo ".pyc" correspondente, o
que significa que, se um arquivo ZIP não contiver arquivos ".pyc", a
importação poderá ser bastante lenta.

Alterado na versão 3.15: Há suporte para entradas de arquivos zip
compactadas com Zstandard (*zstd*).

Alterado na versão 3.13: Suporte para ZIP64.

Alterado na versão 3.8: Anteriormente, não havia suporte para arquivos
ZIP com um comentário de arquivo.

Ver também:

  Nota da aplicação PKZIP
     Documentação do formato de arquivo ZIP feita por Phil Katz,
     criador do formato e dos algoritmos usados.

  **PEP 273** - Importar módulos de arquivos Zip
     Escrito por James C. Ahlstrom, que também forneceu uma
     implementação. O Python 2.3 segue a especificação em **PEP 273**,
     mas usa uma implementação escrita por Just van Rossum que utiliza
     os ganchos de importação descritos em **PEP 302**.

  "importlib" - A importação do maquinário de importação
     Pacote que fornece os protocolos relevantes para todos os
     importadores implementarem.

Este módulo define uma exceção:

exception zipimport.ZipImportError

   Exceção levantada por objetos zipimporter. É uma subclasse de
   "ImportError", portanto, também pode ser capturada como
   "ImportError".


Objetos zipimporter
===================

"zipimporter" é a classe para importar arquivos ZIP.

class zipimport.zipimporter(archivepath)

   Cria uma nova instância de zipimporter. *archivepath* deve ser um
   caminho para um arquivo ZIP ou para um caminho específico dentro de
   um arquivo ZIP. Por exemplo, um *archivepath* de "foo/bar.zip/lib"
   procurará módulos no diretório "lib" dentro do arquivo ZIP
   "foo/bar.zip" (desde que exista).

   "ZipImportError" é levantada se *archivepath* não apontar para um
   arquivo ZIP válido.

   Alterado na versão 3.12: Os métodos "find_loader()" e
   "find_module()", descontinuados na versão 3.10, foram removidos. Em
   vez disso, use "find_spec()".

   create_module(spec)

      Implementação de "importlib.abc.Loader.create_module()" que
      retorna "None" para solicitar explicitamente a semântica padrão.

      Adicionado na versão 3.10.

   exec_module(module)

      Implementação de "importlib.abc.Loader.exec_module()".

      Adicionado na versão 3.10.

   find_spec(fullname, target=None)

      Uma implementação de
      "importlib.abc.PathEntryFinder.find_spec()".

      Adicionado na versão 3.10.

   get_code(fullname)

      Retorna o objeto código para o módulo especificado. Levanta
      "ZipImportError" se o módulo não puder ser importado.

   get_data(pathname)

      Retorna os dados associados a *pathname*. Levanta "OSError" se o
      arquivo não for encontrado.

      Alterado na versão 3.3: "IOError" costumava ser levantada, agora
      ela é um apelido para "OSError".

   get_filename(fullname)

      Retorna o valor que "__file__" seria definido se o módulo
      especificado fosse importado. Levanta "ZipImportError" se o
      módulo não puder ser encontrado.

      Adicionado na versão 3.1.

   get_source(fullname)

      Retorna o código-fonte do módulo especificado. Levanta
      "ZipImportError" se o módulo não puder ser encontrado, e retorna
      "None" se o arquivo contiver o módulo, mas não tiver o código-
      fonte para ele.

   is_package(fullname)

      Retorna "True" se o módulo especificado por *fullname* é um
      pacote. Levanta "ZipImportError" se o módulo não pode ser
      localizado.

   invalidate_caches()

      Limpa o cache interno de informações sobre arquivos encontrados
      no arquivo ZIP.

      Adicionado na versão 3.10.

   archive

      O nome do arquivo ZIP associado ao importador, sem um possível
      subcaminho.

   prefix

      O subcaminho dentro do arquivo ZIP onde os módulos são
      pesquisados. Esta é a string vazia para objetos zipimporter que
      apontam para a raiz do arquivo ZIP.

   Os atributos "archive" e "prefix", quando combinados com uma barra,
   são iguais ao argumento original *archivepath* fornecido ao
   construtor da "zipimporter".


Exemplos
========

Aqui está um exemplo que importa um módulo de um arquivo ZIP - observe
que o módulo "zipimport" não é usado explicitamente.

   $ unzip -l arquivo_exemplo.zip
   Archive:  arquivo_exemplo.zip
     Length     Date   Time    Name
    --------    ----   ----    ----
        8467  01-01-00 12:30   exemplo.py
    --------                   -------
        8467                   1 file

   >>> import sys
   >>> # Adiciona o arquivo para a frente do caminho de pesquisa de módulos
   >>> sys.path.insert(0, 'arquivo_exemplo.zip')
   >>> import exemplo
   >>> exemplo.__file__
   'arquivo_exemplo.zip/exemplo.py'
