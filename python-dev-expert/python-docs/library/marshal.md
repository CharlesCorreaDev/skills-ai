"marshal" --- Serialização interna de objetos Python
****************************************************

======================================================================

Este módulo contém funções que podem ler e gravar valores Python em
formato binário. O formato é específico para Python, mas independente
dos problemas de arquitetura da máquina (por exemplo, você pode gravar
um valor Python em um arquivo em um PC, transportar o arquivo para um
Mac e lê-lo de volta lá). Os detalhes do formato não são documentados
propositalmente; ele pode mudar entre as versões do Python (embora
raramente mude). [1]

This is not a general "persistence" module.  For general persistence
and transfer of Python objects through RPC calls, see the modules
"pickle" and "shelve".  The "marshal" module exists mainly to support
reading and writing the "pseudo-compiled" code for Python modules of
".pyc" files. Therefore, the Python maintainers reserve the right to
modify the marshal format in backward incompatible ways should the
need arise. The format of code objects is not compatible between
Python versions, even if the version of the format is the same. De-
serializing a code object in the incorrect Python version has
undefined behavior. If you're serializing and de-serializing Python
objects, use the "pickle" module instead -- the performance is
comparable, version independence is guaranteed, and pickle supports a
substantially wider range of objects than marshal.

Aviso:

  The "marshal" module is not intended to be secure against erroneous
  or maliciously constructed data.  Never unmarshal data received from
  an untrusted or unauthenticated source.

Existem funções que leem/gravam arquivos, bem como funções que operam
em objetos bytes ou similares.

Not all Python object types are supported; in general, only objects
whose value is independent from a particular invocation of Python can
be written and read by this module.  The following types are
supported:

* Numeric types: "int", "bool", "float", "complex".

* Strings ("str") and "bytes". *Bytes-like objects* like "bytearray"
  are marshalled as "bytes".

* Containers: "tuple", "list", "dict", "frozendict" (since "version"
  6), "set", "frozenset", and "slice" (since "version" 5). It should
  be understood that these are supported only if the values contained
  therein are themselves supported. Recursive containers are supported
  since "version" 3.

* The singletons "None", "Ellipsis" and "StopIteration".

* "code" objects, if *allow_code* is true. See note above about
  version dependence.

Alterado na versão 3.4:

* Added format version 3, which supports marshalling recursive lists,
  sets and dictionaries.

* Added format version 4, which supports efficient representations of
  short strings.

Alterado na versão 3.14: Added format version 5, which allows
marshalling slices.

Alterado na versão 3.15: Added format version 6, which allows
marshalling "frozendict".

O módulo define estas funções:

marshal.dump(value, file, version=version, /, *, allow_code=True)

   Grava o valor no arquivo aberto. O valor deve ser um tipo
   compatível. O arquivo deve ser *arquivo binário* gravável.

   Se o valor tem (ou contém um objeto que tem) um tipo não suportado,
   uma exceção "ValueError" é levantada -- mas dados de lixo também
   serão gravados no arquivo. O objeto não será lido corretamente por
   "load()". Há suporte a objetos código somente se *allow_code* for
   verdadeiro.

   O argumento *version* indica o formato de dados que o "dump" deve
   usar (veja abaixo).

   Levanta um evento de auditoria "marshal.dumps" com os argumentos
   "value", "version".

   Alterado na versão 3.13: Adicionado o parâmetro *allow_code*.

marshal.load(file, /, *, allow_code=True)

   Lê um valor do arquivo aberto e retorna-o. Se nenhum valor válido
   for lido (por exemplo, porque os dados têm um formato de
   empacotamento incompatível com uma versão diferente do Python),
   levanta "EOFError", "ValueError" ou "TypeError". Há suporte a
   objetos código somente se *allow_code* for verdadeiro. O arquivo
   deve ser um *arquivo binário* legível.

   Levanta um evento de auditoria "marshal.load" sem argumentos.

   Nota:

     Se um objeto contendo um tipo não suportado foi empacotado com
     "dump()", "load()" irá substituir "None" pelo tipo não
     empacotável.

   Alterado na versão 3.10: Esta chamada costumava levantar um evento
   de auditoria "code.__new__" para cada objeto código. Agora, ele
   levanta um único evento "marshal.load" para toda a operação de
   carregamento.

   Alterado na versão 3.13: Adicionado o parâmetro *allow_code*.

marshal.dumps(value, version=version, /, *, allow_code=True)

   Retorna o objeto bytes que seria escrito em um arquivo por
   "dump(value, file)". O valor deve ser um tipo compatível. Levanta
   uma exceção "ValueError" se o valor tem (ou contém um objeto que
   tem) um tipo não suportado. Há suporte a objetos código somente se
   *allow_code* for verdadeiro.

   O argumento *version* indica o formato de dados que "dumps" deve
   usar (veja abaixo).

   Levanta um evento de auditoria "marshal.dumps" com os argumentos
   "value", "version".

   Alterado na versão 3.13: Adicionado o parâmetro *allow_code*.

marshal.loads(bytes, /, *, allow_code=True)

   Converte o *objeto bytes ou similar* em um valor. Se nenhum valor
   válido for encontrado, levanta "EOFError", "ValueError" ou
   "TypeError". Há suporte a objetos código somente se *allow_code*
   for verdadeiro. Bytes extras na entrada são ignorados.

   Levanta um evento de auditoria "marshal.loads" com o argumento
   "bytes".

   Alterado na versão 3.10: Esta chamada costumava levantar um evento
   de auditoria "code.__new__" para cada objeto código. Agora, ele
   levanta um único evento "marshal.loads" para toda a operação de
   carregamento.

   Alterado na versão 3.13: Adicionado o parâmetro *allow_code*.

Além disso, as seguintes constantes são definidas:

marshal.version

   Indicates the format that the module uses. Version 0 is the
   historical first version; subsequent versions add new features.
   Generally, a new version becomes the default when it is introduced.

   +---------+-----------------+------------------------------------------------------+
   | Versão  | Available since | Novas funcionalidades                                |
   |=========|=================|======================================================|
   | 1       | Python 2.4      | Sharing interned strings                             |
   +---------+-----------------+------------------------------------------------------+
   | 2       | Python 2.5      | Binary representation of floats                      |
   +---------+-----------------+------------------------------------------------------+
   | 3       | Python 3.4      | Support for object instancing and recursion          |
   +---------+-----------------+------------------------------------------------------+
   | 4       | Python 3.4      | Efficient representation of short strings            |
   +---------+-----------------+------------------------------------------------------+
   | 5       | Python 3.14     | Support for "slice" objects                          |
   +---------+-----------------+------------------------------------------------------+
   | 6       | Python 3.15     | Support for "frozendict" objects                     |
   +---------+-----------------+------------------------------------------------------+

-[ Notas de rodapé ]-

[1] O nome deste módulo deriva de um pouco da terminologia usada pelos
    designers do Modula-3 (entre outros), que usam o termo
    "marshalling" para enviar dados em um formato independente.
    Estritamente falando, "to marshal" significa converter alguns
    dados da forma interna para a externa (em um buffer RPC, por
    exemplo) e "unmarshalling" para o processo reverso.
