"dbm" --- Interfaces para "banco de dados" Unix
***********************************************

**Código-fonte:** Lib/dbm/__init__.py

======================================================================

"dbm" is a generic interface to variants of the DBM database:

* "dbm.sqlite3"

* "dbm.gnu"

* "dbm.ndbm"

If none of these modules are installed, the slow-but-simple
implementation in module "dbm.dumb" will be used. There is a third
party interface to the Oracle Berkeley DB.

Nota:

  None of the underlying modules will automatically shrink the disk
  space used by the database file. However, "dbm.sqlite3", "dbm.gnu"
  and "dbm.dumb" provide a "reorganize()" method that can be used for
  this purpose.

exception dbm.error

   Uma tupla contendo as exceções que podem ser levantadas por cada um
   dos módulos suportados, com a única exceção também chamada
   "dbm.error" como o primeiro item --- o último é usado quando
   "dbm.error" é levantada.

dbm.whichdb(filename)

   Esta função tenta adivinhar qual dos vários módulos de banco de
   dados simples disponíveis --- "dbm.sqlite3", "dbm.gnu", "dbm.ndbm"
   ou "dbm.dumb" --- deve ser usado para abrir o arquivo fornecido.

   Retorna um dos seguintes valores:

   * "None" se o arquivo não puder ser aberto porque está ilegível ou
     não existe

   * a string vazia ("''") se o formato do arquivo não puder ser
     adivinhado

   * uma string contendo o nome do módulo necessário, tal como
     "'dbm.ndbm'" ou "'dbm.gnu'"

   Alterado na versão 3.11: *filename* aceita um *objeto caminho ou
   similar*.

dbm.open(file, flag='r', mode=0o666)

   Abre um banco de dados e retorna o objeto banco de dados
   correspondendo.

   Parâmetros:
      * **file** (*path-like object*) -- O arquivo de banco de dados
        para abrir. Se o arquivo de banco de dados já existe, a função
        "whichdb()" é usada para determinar seu tipo e o módulo
        apropriado é usado; se ele não existir, o primeiro submódulo
        listado acima que pode ser importado é usado.

      * **flag** (*str*) --

        * "'r'" (padrão): Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'": Open database for reading and writing, creating it if
          it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

      * **mode** (*int*) -- The Unix file access mode of the file
        (default: octal "0o666"), used only when the database has to
        be created.

   Alterado na versão 3.11: *file* aceita um *objeto caminho ou
   similar*.

O objeto retornado por "open()" oferece suporte à funcionalidade
básica de *mapeamentos* mutáveis; chaves e seus valores
correspondentes podem ser armazenados, recuperados e excluídos, e
iteração, o operador "in" e os métodos "keys()", "get()",
"setdefault()" e "clear()" estão disponíveis. O método "keys()"
retorna uma lista em vez de um objeto de visualização. O método
"setdefault()" requer dois argumentos.

Key and values are always stored as "bytes". This means that when
strings are used they are implicitly converted to the default encoding
before being stored. For detailed information about accepted types,
see Key and value types.

Estes objetos também oferecem suporte a serem usados em uma instrução
"with", que vai fechá-los automaticamente quando estiver concluída.

Alterado na versão 3.2: "get()" and "setdefault()" methods are now
available for all "dbm" backends.

Alterado na versão 3.4: Adicionado suporte nativo para o protocolo de
gerenciamento de contexto para os objetos retornados por "open()".

Alterado na versão 3.8: Excluir uma chave de um banco de dados somente
leitura levanta uma exceção de banco de dados específica do módulo em
vez de "KeyError".

Alterado na versão 3.13: "clear()" methods are now available for all
"dbm" backends.


Key and value types
===================

The accepted types for keys and values vary by backend. Keys and
values are handled the same way, except where noted below:

* **Traditional backends:**

  * "dbm.gnu" and "dbm.ndbm": Accept "str" and "bytes" objects.

  * "dbm.dumb": Accepts "str" and "bytes" objects; "bytearray" is
    acceptable as a value, but not as a key.

* **SQLite backend** ("dbm.sqlite3"): Accepts "str", "bytes", "int",
  "float", "bool", "bytearray", "memoryview", and "array.array"
  objects.

**Storage format:**

All keys and values are stored as "bytes" objects in the database.
When retrieving, you'll always get bytes back, regardless of the
original type stored.

**Type conversion examples:**

* "db['key'] = 'string'" stored as "b'string'"

* "db['key'] = bytearray(b'data')" stored as "b'data'" ("dbm.dumb" and
  "dbm.sqlite3" only)

* "db['key'] = 42" stored as "b'42'" ("dbm.sqlite3" only)

* "db['key'] = 3.14" stored as "b'3.14'" ("dbm.sqlite3" only)

* "db['key'] = True" stored as "b'1'" ("dbm.sqlite3" only)

* "db['key'] = False" stored as "b'0'" ("dbm.sqlite3" only)

* "db['key'] = memoryview(b'data')" stored as "b'data'" ("dbm.sqlite3"
  only)

* "db['key'] = array.array('i', [1, 2, 3])" stored as bytes (for
  example, on little-endian:
  "b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'")
  ("dbm.sqlite3" only)

Os seguintes exemplos registram alguns hostnames e um título
correspondente, e então exibe o conteúdo do banco de dados:

   import dbm

   # Open database, creating it if necessary.
   with dbm.open('cache', 'c') as db:

       # Record some values
       db[b'hello'] = b'there'
       db['www.python.org'] = 'Python Website'
       db['www.cnn.com'] = 'Cable News Network'

       # Note that the keys are considered bytes now.
       assert db[b'www.python.org'] == b'Python Website'
       # Notice how the value is now in bytes.
       assert db['www.cnn.com'] == b'Cable News Network'

       # Often-used methods of the dict interface work too.
       print(db.get('python.org', b'not present'))

       # Storing a non-string key or value behavior depends on the backend:
       # - Traditional backends (ndbm, gnu, dumb) will raise a TypeError
       # - The sqlite3 backend accepts it and converts to bytes
       db['www.yahoo.com'] = 4

   # db is automatically closed when leaving the with statement.

Ver também:

  Módulo "shelve"
     Módulo persistente que armazena dados não-string.

Os submódulos individuais são descritos nas seções a seguir.


"dbm.sqlite3" --- SQLite backend for dbm
========================================

Adicionado na versão 3.13.

**Código-fonte:** Lib/dbm/sqlite3.py

======================================================================

This module uses the standard library "sqlite3" module to provide an
SQLite backend for the "dbm" module. The files created by
"dbm.sqlite3" can thus be opened by "sqlite3", or any other SQLite
browser, including the SQLite CLI.

Disponibilidade: not WASI.

Este módulo não funciona ou não está disponível em WebAssembly. Veja
Plataformas WebAssembly para mais informações.

dbm.sqlite3.open(filename, /, flag='r', mode=0o666)

   Abre um banco de dados SQLite.

   Parâmetros:
      * **filename** (*path-like object*) -- O caminho para o banco de
        dados a ser aberta.

      * **flag** (*str*) --

        * "'r'" (padrão): Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'": Open database for reading and writing, creating it if
          it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

      * **mode** -- O modo de acesso a arquivos do Unix do arquivo
        (padrão: octal "0o666"), usado apenas quando o banco de dados
        tem que ser criado.

   O objeto de banco de dados retornado se comporta de forma
   semelhante a um *mapeamento* mutável, mas o método "keys()" retorna
   uma lista e o método "setdefault()" requer dois argumentos. Ele
   também oferece suporte a um gerenciador de contexto de "fechamento"
   por meio da palavra reservada "with".

   Os seguintes métodos também são fornecidos:

   sqlite3.close()

      Fecha o banco de dados SQLite.

   sqlite3.reorganize()

      If you have carried out a lot of deletions and would like to
      shrink the space used on disk, this method will reorganize the
      database; otherwise, deleted file space will be kept and reused
      as new (key, value) pairs are added.

      Nota:

        While reorganizing, as much as two times the size of the
        original database is required in free disk space. However, be
        aware that this factor changes for each "dbm" submodule.

      Adicionado na versão 3.15.


"dbm.gnu" --- GNU database manager
==================================

**Código-fonte:** Lib/dbm/gnu.py

======================================================================

The "dbm.gnu" module provides an interface to the GDBM (GNU dbm)
library, similar to the "dbm.ndbm" module, but with additional
functionality like crash tolerance.

Nota:

  The file formats created by "dbm.gnu" and "dbm.ndbm" are
  incompatible and can not be used interchangeably.

Disponibilidade: not Android, not iOS, not WASI.

Este módulo não tem suporte em plataformas móveis ou plataformas
WebAssembly.

Disponibilidade: Unix.

exception dbm.gnu.error

   Raised on "dbm.gnu"-specific errors, such as I/O errors. "KeyError"
   is raised for general mapping errors like specifying an incorrect
   key.

dbm.gnu.open_flags

   Uma sequência de caracteres que o parâmetro *flag* de "open()"
   suporta.

dbm.gnu.open(filename, flag='r', mode=0o666, /)

   Abre um banco de dados GDBM e retorna um objeto "gdbm".

   Parâmetros:
      * **filename** (*path-like object*) -- O arquivo de banco de
        dados para abrir.

      * **flag** (*str*) --

        * "'r'" (padrão): Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'": Open database for reading and writing, creating it if
          it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

        Os seguintes caracteres adicionais podem ser acrescentados
        para controlar como o banco de dados é aberto:

        * "'f'": Abre o banco de dados em modo rápido. As gravações no
          banco de dados não serão sincronizadas.

        * "'s'": Modo sincronizado. Alterações no banco de dados serão
          gravadas imediatamente no arquivo.

        * "'u'": Não trava o banco de dados.

        Nem todos os sinalizadores são válidos para todas as versões
        do GDBM. Veja o membro "open_flags" para uma lista de
        caracteres de sinalizadores suportados.

      * **mode** (*int*) -- The Unix file access mode of the file
        (default: octal "0o666"), used only when the database has to
        be created.

   Levanta:
      **error** -- Se um argumento *flag* inválido for passado.

   Alterado na versão 3.11: *filename* aceita um *objeto caminho ou
   similar*.

   Objetos "gdbm" se comportam de forma semelhante aos *mapeamentos*
   mutáveis, mas os métodos "items()", "values()", "pop()",
   "popitem()" e "update()" não são suportados, "keys()" retorna uma
   lista e o método "setdefault()" requer dois argumentos. Ele também
   oferece suporte a um gerenciador de contexto de "fechamento" por
   meio da palavra reservada "with".

   Alterado na versão 3.2: Adiciionados os métodos "get()" e
   "setdefault()".

   Alterado na versão 3.13: Adicionado o método "clear()".

   Os seguintes métodos também são fornecidos:

   gdbm.close()

      Fecha o banco de dados GDBM.

   gdbm.firstkey()

      É possível fazer um laço em cada chave no banco de dados usando
      este método e o método "nextkey()". A travessia é ordenada pelos
      valores de hash internos do GDBM e não será classificada pelos
      valores de chave. Este método retorna a chave inicial.

   gdbm.nextkey(key)

      Retorna a chave que segue *key* na travessia. O código a seguir
      imprime cada chave no banco de dados "db", sem precisar criar
      uma lista na memória que contenha todas elas:

         k = db.firstkey()
         while k is not None:
             print(k)
             k = db.nextkey(k)

   gdbm.reorganize()

      Se você realizou muitas exclusões e gostaria de reduzir o espaço
      usado pelo arquivo GDBM, esta rotina reorganizará o banco de
      dados. Objetos "gdbm" não reduzirão o tamanho de um arquivo de
      banco de dados, exceto usando esta reorganização; caso
      contrário, o espaço de arquivo excluído será mantido e
      reutilizado à medida que novos pares (chave, valor) forem
      adicionados.

      Nota:

        While reorganizing, as much as one time the size of the
        original database is required in free disk space. However, be
        aware that this factor changes for each "dbm" submodule.

   gdbm.sync()

      Quando o banco de dados é aberto no modo rápido, esse método
      força a gravação de todos os dados não gravados no disco.


"dbm.ndbm" --- New Database Manager
===================================

**Código-fonte:** Lib/dbm/ndbm.py

======================================================================

The "dbm.ndbm" module provides an interface to the NDBM (New Database
Manager) library. This module can be used with the "classic" NDBM
interface or the GDBM (GNU dbm) compatibility interface.

Nota:

  The file formats created by "dbm.gnu" and "dbm.ndbm" are
  incompatible and can not be used interchangeably.

Aviso:

  A biblioteca NDBM enviada como parte do macOS tem uma limitação não
  documentada no tamanho dos valores, o que pode resultar em arquivos
  de banco de dados corrompidos ao armazenar valores maiores que esse
  limite. Ler esses arquivos corrompidos pode resultar em uma falha
  grave (falha de segmentação).

Disponibilidade: not Android, not iOS, not WASI.

Este módulo não tem suporte em plataformas móveis ou plataformas
WebAssembly.

Disponibilidade: Unix.

exception dbm.ndbm.error

   Raised on "dbm.ndbm"-specific errors, such as I/O errors.
   "KeyError" is raised for general mapping errors like specifying an
   incorrect key.

dbm.ndbm.library

   Nome da biblioteca de implementação NDBM usada.

dbm.ndbm.open(filename, flag='r', mode=0o666, /)

   Abre um banco de dados NDBM e retorna um objeto "ndbm".

   Parâmetros:
      * **filename** (*path-like object*) -- O nome base do arquivo de
        banco de dados (sem as extensões ".dir" ou ".pag").

      * **flag** (*str*) --

        * "'r'" (padrão): Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'": Open database for reading and writing, creating it if
          it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

      * **mode** (*int*) -- The Unix file access mode of the file
        (default: octal "0o666"), used only when the database has to
        be created.

   Alterado na versão 3.11: Aceita um *objeto caminho ou similar* como
   nome de arquivo.

   Objetos "ndbm" se comportam de forma semelhante aos *mapeamentos*
   mutáveis, mas os métodos "items()", "values()", "pop()",
   "popitem()" e "update()" não são suportados, "keys()" retorna uma
   lista e o método "setdefault()" requer dois argumentos. Ele também
   oferece suporte a um gerenciador de contexto de "fechamento" por
   meio da palavra reservada "with".

   Alterado na versão 3.2: Adiciionados os métodos "get()" e
   "setdefault()".

   Alterado na versão 3.13: Adicionado o método "clear()".

   O seguinte método também é fornecido:

   ndbm.close()

      Fecha o banco de dados NDBM.


"dbm.dumb" --- Portable DBM implementation
==========================================

**Código-fonte:** Lib/dbm/dumb.py

Nota:

  The "dbm.dumb" module is intended as a last resort fallback for the
  "dbm" module when a more robust module is not available. The
  "dbm.dumb" module is not written for speed and is not nearly as
  heavily used as the other database modules.

======================================================================

The "dbm.dumb" module provides a persistent "dict"-like interface
which is written entirely in Python. Unlike other "dbm" backends, such
as "dbm.gnu", no external library is required.

O módulo "dbm.dumb" define o seguinte:

exception dbm.dumb.error

   Raised on "dbm.dumb"-specific errors, such as I/O errors.
   "KeyError" is raised for general mapping errors like specifying an
   incorrect key.

dbm.dumb.open(filename, flag='c', mode=0o666)

   Abre um banco de dados "dbm.dumb".

   Parâmetros:
      * **filename** -- O nome base do arquivo do banco de dados (sem
        extensões). Um novo banco de dados cria os seguintes arquivos:
        - "*filename*.dat" - "*filename*.dir"

      * **flag** (*str*) --

        * "'r'": Open existing database for reading only.

        * "'w'": Open existing database for reading and writing.

        * "'c'" (padrão): Open database for reading and writing,
          creating it if it doesn't exist.

        * "'n'": Always create a new, empty database, open for reading
          and writing.

      * **mode** (*int*) -- The Unix file access mode of the file
        (default: octal "0o666"), used only when the database has to
        be created.

   Aviso:

     É possível travar o interpretador Python ao carregar um banco de
     dados com uma entrada suficientemente grande/complexa devido a
     limitações de profundidade de pilha no compilador AST do Python.

   Aviso:

     "dbm.dumb" does not support concurrent read/write access.
     (Multiple simultaneous read accesses are safe.) When a program
     has the database open for writing, no other program should have
     it open for reading or writing.

   Alterado na versão 3.5: "open()" sempre cria um novo banco de dados
   quando *flag* é "'n'".

   Alterado na versão 3.8: Um banco de dados aberto somente leitura se
   *flag* for "'r'". Um banco de dados não é criado se não existir se
   *flag* for "'r'" ou "'w'".

   Alterado na versão 3.11: *filename* aceita um *objeto caminho ou
   similar*.

   O objeto de banco de dados retornado se comporta de forma
   semelhante a um *mapeamento* mutável, mas os métodos "keys()" e
   "items()" retornam uma lista e o método "setdefault()" requer dois
   argumentos. Ele também oferece suporte a um gerenciador de contexto
   de "fechamento" por meio da palavra reservada "with".

   Os seguintes métodos também são fornecidos:

   dumbdbm.close()

      Fecha o banco de dados.

   dumbdbm.reorganize()

      If you have carried out a lot of deletions and would like to
      shrink the space used on disk, this method will reorganize the
      database; otherwise, deleted file space will not be reused.

      Nota:

        While reorganizing, no additional free disk space is required.
        However, be aware that this factor changes for each "dbm"
        submodule.

      Adicionado na versão 3.15.

   dumbdbm.sync()

      Sincroniza o diretório no disco e os arquivos de dados. Este
      método é chamado pelo método "shelve.Shelf.sync()".
