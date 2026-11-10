Importando módulos
******************

Os módulos descritos neste capítulo fornecem novas maneiras de
importar outros módulos Python e hooks para personalizar o processo de
importação.

A lista completa de módulos descritos neste capítulo é:

* "zipimport" - Importa módulos de arquivos Zip

  * Objetos zipimporter

  * Exemplos

* "pkgutil" --- Utilitário de extensão de pacote

* "modulefinder" --- Procura módulos usados por um script

  * Exemplo de uso de "ModuleFinder"

* "runpy" --- Localizando e executando módulos Python

* "importlib" --- A implementação de "import"

  * Introdução

  * Funções

  * "importlib.abc" -- Abstract base classes related to import

  * "importlib.machinery" -- Importers and path hooks

  * "importlib.util" -- Utility code for importers

  * Exemplos

    * Importing programmatically

    * Checando se o módulo pode ser importado

    * Importa o arquivo de origem diretamente

    * Implementing lazy imports

    * Setting up an importer

    * Approximating "importlib.import_module()"

* "importlib.resources" -- Leitura, abertura e acesso a recursos de
  pacotes

  * API funcional

* "importlib.resources.abc" -- Classes base abstratas para recursos

* "importlib.metadata" -- Acessando metadados do pacote

  * Visão Geral

  * API funcional

    * Pontos de entrada

    * Metadados de distribuição

    * Versões de distribuição

    * Arquivos de distribuição

    * Requisitos de distribuição

    * Mapeando importação pra pacotes de distribuição

  * Distribuições

  * Descoberta de distribuição

  * Implementando provedores personalizados

    * Exemplo

* A inicialização do caminho de pesquisa de módulos "sys.path"

  * Ambientes virtuais

  * Arquivos _pth

  * Python embarcado
