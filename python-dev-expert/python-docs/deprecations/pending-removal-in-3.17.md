Remoção pendente no Python 3.17
*******************************

* "datetime":

  * "strptime()" chama usando uma string de formato contendo "%e" (dia
    do mês) sem um ano. Isso está descontinuado desde Python 3.15.
    (Contribuição de Stan Ulbrych em gh-70647.)

* "collections.abc":

  * "collections.abc.ByteString" está programado para remoção no
    Python 3.17.

    Use "isinstance(obj, collections.abc.Buffer)" para testar se "obj"
    implementa o protocolo de buffer em tempo de execução. Para uso em
    anotações de tipo, use "Buffer" ou uma união que especifique
    explicitamente os tipos suportados pelo seu código (por exemplo,
    "bytes | bytearray | memoryview").

    "ByteString" foi originalmente concebido para ser uma classe
    abstrata que serviria como um supertipo de "bytes" e "bytearray".
    No entanto, como o ABC nunca teve métodos, saber que um objeto era
    uma instância de "ByteString" nunca lhe dizia nada de útil sobre o
    objeto. Outros tipos comuns de buffer, como "memoryview", também
    nunca foram entendidos como subtipos de "ByteString" (seja em
    tempo de execução ou por verificadores de tipo estático).

    Veja **PEP 688** para mais detalhes. (Contribuição de Shantanu
    Jain em gh-91896.)

* "encodings":

  * Passar nomes de *codificação* não ASCII para
    "encodings.normalize_encoding()" está descontinuado e sua remoção
    está prevista para o Python 3.17. (Contribuição de Stan Ulbrych em
    gh-136702.)

* "profile":

  * O módulo "profile" está descontinuado e será removido no Python
    3.17. Em vez disso, utilize "profiling.tracing", que oferece uma
    API compatível. Consulte a **PEP 799** para obter detalhes.
    (Contribuição de Pablo Galindo e László Kiss Kollár em gh-138122.)

* "webbrowser":

  * "webbrowser.MacOSXOSAScript" está descontinuado em favor de
    "webbrowser.MacOS". (gh-137586)

* "typing":

  * Antes do Python 3.14, as uniões antigas eram implementadas usando
    a classe privada "typing._UnionGenericAlias". Essa classe não é
    mais necessária para a implementação, mas foi mantida para
    compatibilidade com versões anteriores, com remoção prevista para
    o Python 3.17. Os usuários devem usar auxiliares de introspecção
    documentados, como "typing.get_origin()" e "typing.get_args()", em
    vez de depender de detalhes de implementação privada.

  * "typing.ByteString", obsoleto desde o Python 3.9, está programado
    para ser removido no Python 3.17.

    Use "isinstance(obj, collections.abc.Buffer)" para testar se "obj"
    implementa o protocolo de buffer em tempo de execução. Para uso em
    anotações de tipo, use "Buffer" ou uma união que especifique
    explicitamente os tipos suportados pelo seu código (por exemplo,
    "bytes | bytearray | memoryview").

    "ByteString" foi originalmente concebido para ser uma classe
    abstrata que serviria como um supertipo de "bytes" e "bytearray".
    No entanto, como o ABC nunca teve métodos, saber que um objeto era
    uma instância de "ByteString" nunca lhe dizia nada de útil sobre o
    objeto. Outros tipos comuns de buffer, como "memoryview", também
    nunca foram entendidos como subtipos de "ByteString" (seja em
    tempo de execução ou por verificadores de tipo estático).

    Veja **PEP 688** para mais detalhes. (Contribuição de Shantanu
    Jain em gh-91896.)

* "tkinter":

  * Os métodos "trace_variable()", "trace()" (um apelido de
    "trace_variable()"), "trace_vdelete()" e "trace_vinfo()" da classe
    "tkinter.Variable", descontinuados desde o Python 3.14, têm
    remoção prevista para o Python 3.17. Em vez deles, utilize
    "trace_add()", "trace_remove()" e "trace_info()". (Contribuição de
    Serhiy Storchaka em gh-120220.)
