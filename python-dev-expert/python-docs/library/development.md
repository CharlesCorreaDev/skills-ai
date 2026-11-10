Ferramentas de Desenvolvimento
******************************

Os módulos descritos neste capítulo ajudam você a escrever softwares.
Por exemplo, o módulo "pydoc" recebe um módulo e gera documentação com
base no conteúdo do módulo. Os módulos "doctest" e "unittest" contêm
frameworks para escrever testes unitários que automaticamente
exercitam código e verificam se a saída esperada é produzida.

A lista de módulos descritos neste capítulo é:

* "typing" --- Suporte para dicas de tipo

  * Especificação para o sistema de tipos do Python

  * Apelidos de tipo

  * NewType

  * Anotações de objetos chamáveis

  * Genéricos

  * Anotando tuplas

  * O tipo de objetos de classe

  * Anotando geradores e corrotinas

  * Tipos genéricos definidos pelo usuário

  * O tipo "Any"

  * Subtipagem nominal vs estrutural

  * Conteúdo do módulo

    * Tipos primitivos especiais

      * Tipos especiais

      * Formas especiais

      * Criando tipos genéricos e apelidos de tipo

      * Outras diretivas especiais

    * Protocolos

    * ABCs e protocolos para trabalhar com E/S

    * Funções e decoradores

    * Auxiliares de introspecção

    * Constante

    * Apelidos descontinuados

      * Apelidos de tipos embutidos

      * Apelidos para tipos em "collections"

      * Apelidos de outros tipos concretos

      * Apelidos de contêineres ABC em "collections.abc".

      * Apelidos para ABCs assíncronas em "collections.abc"

      * Apelidos para outros ABCs em "collections.abc".

      * Apelidos de ABCs da "contextlib"

  * Cronograma de descontinuação dos principais recursos

* "pydoc" --- Gerador de documentação e sistema de ajuda online

* Modo de Desenvolvimento do Python

  * Efeitos do Modo de Desenvolvimento do Python

  * Exemplo de ResourceWarning

  * Exemplo de erro de descritor de arquivo inválido

* "doctest" --- Teste exemplos interativos de Python

  * Uso simples: verificando exemplos em Docstrings

  * Utilização comum: Verificando exemplos em um arquivo texto

  * Uso na linha de comando

  * Como ele funciona

    * Quais docstrings são examinadas?

    * Como os exemplos de docstrings são reconhecidos?

    * Qual é o contexto de execução?

    * E quanto às exceções?

    * Flags opcionais

    * Directives

    * Avisos

  * Basic API

  * API do Unittest

  * Advanced API

    * DocTest Objects

    * Example Objects

    * DocTestFinder objects

    * DocTestParser objects

    * TestResults objects

    * DocTestRunner objects

    * OutputChecker objects

  * Depuração

  * Soapbox

* "unittest" --- Framework de testes unitários

  * Exemplo Básico

  * Interface de Linha de Comando

    * Opções de linha de comando

  * Test Discovery

  * Organizando código teste

  * Reutilizando códigos de teste antigos

  * Ignorando testes e falhas esperadas

  * Distinguindo iterações de teste utilizando subtestes

  * Classes e funções

    * Casos de teste

    * Grouping tests

    * Carregando e executando testes

      * load_tests Protocol

  * Classes e Módulos de Definição de Contexto

    * setUpClass and tearDownClass

    * setUpModule and tearDownModule

  * Tratamento de sinal

* "unittest.mock" --- mock object library

  * Guia Rápido

  * A classe Mock

    * Fazendo chamadas

    * Deletando Atributos

    * Nomes de Mock e o atributo *name*

    * Anexando Mocks como Atributos

  * Os criadores de patches

    * patch

    * patch.object

    * patch.dict

    * patch.multiple

    * métodos do patch: *start* e *stop*

    * patch de embutidos

    * TEST_PREFIX

    * Aninhando Decoradores Patch

    * Onde fazer patch

    * Patching Descriptors and Proxy Objects

  * MagicMock and magic method support

    * Simulando Métodos Mágicos

    * Magic Mock

  * Ajudantes

    * sentinel

    * DEFAULT

    * chamada

    * create_autospec

    * ANY

    * FILTER_DIR

    * mock_open

    * Especificação automática

    * Vedando mocks

  * Order of precedence of "side_effect", "return_value" and *wraps*

* "unittest.mock" --- primeiros passos

  * Usando Mock

    * Mock patching methods

    * Mock for method calls on an object

    * Mocking classes

    * Nomeando os mocks

    * Tracking all calls

    * Setting return values and attributes

    * Raising exceptions with mocks

    * Side effect functions and iterables

    * Mocking asynchronous iterators

    * Mocking asynchronous context manager

    * Creating a mock from an existing object

    * Using side_effect to return per file content

  * Patch decorators

  * Further examples

    * Mocking chained calls

    * Partial mocking

    * Mocking a generator method

    * Applying the same patch to every test method

    * Mocking unbound methods

    * Checking multiple calls with mock

    * Coping with mutable arguments

    * Nesting patches

    * Mocking a dictionary with MagicMock

    * Mock subclasses and their attributes

    * Mocking imports with patch.dict

    * Tracking order of calls and less verbose call assertions

    * More complex argument matching

* "test" --- Pacote de Testes de Regressão do Python

  * Writing Unit Tests for the "test" package

  * Executando testes usando a interface de linha de comando

* "test.support" --- Utilities for the Python test suite

* "test.support.socket_helper" --- Utilities for socket tests

* "test.support.script_helper" --- Utilities for the Python execution
  tests

* "test.support.bytecode_helper" --- Support tools for testing correct
  bytecode generation

* "test.support.threading_helper" --- Utilities for threading tests

* "test.support.os_helper" --- Utilities for os tests

* "test.support.import_helper" --- Utilities for import tests

* "test.support.warnings_helper" --- Utilities for warnings tests
