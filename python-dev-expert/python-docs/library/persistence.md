Persistência de Dados
*********************

Os módulos descritos neste capítulo possuem suporte ao armazenamento
de dados do Python em um formato persistente no disco. Os módulos
"pickle" e "marshal" podem transformar muitos tipos de dados do Python
em um fluxo de bytes e então recriar os objetos a partir dos bytes. Os
vários módulos relacionados ao DBM possuem suporte a uma família de
formatos de arquivo baseados em hash que armazenam um mapeamento de
strings para outras strings.

A lista de módulos descritos neste capítulo é:

* "pickle" --- Serialização de objetos Python

  * Relação com outros módulos Python

    * Comparação com "marshal"

    * Comparação com "json"

  * Formato de fluxo de dados

  * Interface do módulo

  * O que pode ser serializado e desserializado com pickle?

  * Serializando instâncias de classes com pickle

    * Persistência de objetos externos

    * Tabelas de despacho

    * Manipulação de objetos com estado

  * Redução personalizada para tipos, funções e outros objetos

  * Buffers fora da banda

    * API de provedor

    * API de consumidor

    * Exemplo

  * Restringindo globais

  * Desempenho

  * Exemplos

  * Interface de linha de comando

* "copyreg" --- Registra funções de suporte "pickle"

  * Exemplo

* "shelve" --- Python object persistence

  * Restrições

  * Exemplo

  * Exceções

* "marshal" --- Serialização interna de objetos Python

* "dbm" --- Interfaces para "banco de dados" Unix

  * Key and value types

  * "dbm.sqlite3" --- SQLite backend for dbm

  * "dbm.gnu" --- GNU database manager

  * "dbm.ndbm" --- New Database Manager

  * "dbm.dumb" --- Portable DBM implementation

* "sqlite3" ---- interface DB-API 2.0 interface para bancos de dados
  SQLite

  * Tutorial

  * Referência

    * Funções do módulo

    * Constantes do módulo

    * Connection objects

    * Cursor objects

    * Row objects

    * Blob objects

    * PrepareProtocol objects

    * Exceções

    * SQLite and Python types

    * Default adapters and converters (deprecated)

    * Interface de linha de comando

  * Guias de como fazer

    * How to use placeholders to bind values in SQL queries

    * How to adapt custom Python types to SQLite values

      * How to write adaptable objects

      * How to register adapter callables

    * How to convert SQLite values to custom Python types

    * Adapter and converter recipes

    * How to use connection shortcut methods

    * How to use the connection context manager

    * How to work with SQLite URIs

    * How to create and use row factories

    * How to handle non-UTF-8 text encodings

  * Explicação

    * Controle de transações

      * Controle de transações através do atributo "autocommit"

      * Controle de transação através do atributo "isolation_level"
