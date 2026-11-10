Remoção pendente no Python 3.15
*******************************

* O sistema de importação:

  * A definição de "__cached__" em um módulo enquanto falha na
    definição de "__spec__.cached" está descontinuado. No Python 3.15,
    "__cached__" deixará de ser definido ou levado em consideração
    pelo sistema de importação ou pela biblioteca padrão. (gh-97879)

  * A definição de "__package__" em um módulo enquanto falha na
    definição de "__spec__.parent" está descontinuado. No Python 3.15,
    "__package__" deixará de ser definido ou levado em consideração
    pelo sistema de importação ou pela biblioteca padrão. (gh-97879)

* "ctypes":

  * A função não documentada "ctypes.SetPointerType()" foi
    descontinuada desde o Python 3.13.

* "http.server":

  * A classe obsoleta e raramente usada "CGIHTTPRequestHandler" foi
    descontinuada desde o Python 3.13. Não existe substituição direta.
    *Qualquer coisa* é melhor que CGI para fazer a interface de um
    servidor web com um manipulador de requisição.

  * O sinalizador "--cgi" para a interface de linha de comando
    **python -m http.server** foi descontinuado desde o Python 3.13.

* "importlib":

  * Método "load_module()": use "exec_module()".

* "pathlib":

  * ".PurePath.is_reserved()" foi descontinuado desde o Python 3.13.
    Use "os.path.isreserved()" para detectar caminhos reservados no
    Windows.

* "platform":

  * "platform.java_ver()" foi descontinuada desde o Python 3.13. Esta
    função é útil apenas para suporte Jython, tem uma API confusa e é
    amplamente não testada.

* "sysconfig":

  * O argumento *check_home* de "sysconfig.is_python_build()" foi
    descontinuado desde o Python 3.12.

* "threading":

  * "RLock()" não aceitará argumentos no Python 3.15. A passagem de
    quaisquer argumentos foi descontinuada a partir do Python 3.14,
    uma vez que a versão do Python não permite quaisquer argumentos,
    mas a versão C permite qualquer número de argumentos posicionais
    ou nomeados, ignorando todos os argumentos.

* "types":

  * "types.CodeType": o acesso a "codeobject.co_lnotab" foi
    descontinuado na **PEP 626** desde 3.10 e foi planejado para ser
    removido em 3.12, mas só recebeu uma "DeprecationWarning" adequada
    em 3.12. Pode ser removido em 3.15. (Contribuição de Nikita
    Sobolev em gh-101866.)

* "typing":

  * A não-documentada sintaxe de argumento nomeado para criar classes
    "NamedTuple" (por exemplo, "Point = NamedTuple("Point", x=int,
    y=int)") foi descontinuada desde o Python 3.13. Em vez disso, use
    as sintaxes baseada em classe ou funcional.

  * Ao usar a sintaxe funcional de "TypedDict"s, não passar um valor
    para o parâmetro *fields* ("TD = TypedDict("TD")") ou passar
    "None" ("TD = TypedDict("TD", None)") foi está descontinuado desde
    o Python 3.13. Use "class TD(TypedDict): pass" ou "TD =
    TypedDict("TD", {})" para criar uma classe TypedDict com nenhum
    campo.

  * A função decoradora "@typing.no_type_check_decorator" foi
    descontinuada desde o Python 3.13. Após oito anos no módulo
    "typing", ela ainda não foi suportada por nenhum verificador de
    tipo importante.

* Módulos "sre_compile", "sre_constants" e "sre_parse".

* "wave":

  * Os métodos "getmark()", "setmark()" e "getmarkers()" das classes
    "Wave_read" e "Wave_write" foram descontinuados desde o Python
    3.13.

* "zipimport":

  * "zipimport.zipimporter.load_module()" está descontinuado desde o
    Python 3.10. Em vez disso, use "exec_module()". (gh-125746.)
