Remoção pendente no Python 3.16
*******************************

* O sistema de importação:

  * A definição de "__loader__" em um módulo enquanto falha na
    definição de "__spec__.loader" está descontinuado. No Python 3.16,
    "__loader__" deixará de ser definido ou levado em consideração
    pelo sistema de importação ou pela biblioteca padrão.

* "array":

  * O código de formato "'u'" ("wchar_t") foi descontinuado na
    documentação desde o Python 3.3 e em tempo de execução desde o
    Python 3.13. Use o código de formato "'w'" ("Py_UCS4") para
    caracteres Unicode.

* "asyncio":

  * "asyncio.iscoroutinefunction()" foi descontinuado e será removido
    no Python 3.16, use "inspect.iscoroutinefunction()" em vez disso.
    (Contribuição de Jiahao Li e Kumar Aditya em gh-122875.)

  * O sistema de políticas "asyncio" está descontinuado e será
    removido no Python 3.16. Em particular, as seguintes classes e
    funções estão descontinuadas:

    * "asyncio.AbstractEventLoopPolicy"

    * "asyncio.DefaultEventLoopPolicy"

    * "asyncio.WindowsSelectorEventLoopPolicy"

    * "asyncio.WindowsProactorEventLoopPolicy"

    * "asyncio.get_event_loop_policy()"

    * "asyncio.set_event_loop_policy()"

    Os usuários devem usar "asyncio.run()" ou "asyncio.Runner" com
    *loop_factory* para usar a implementação de laço de eventos
    desejada.

    por exemplo, para usar "asyncio.SelectorEventLoop" no Windows:

       import asyncio

       async def main():
           ...

       asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop)

    (Contribuição de Kumar Aditya em gh-127949.)

* "builtins":

  * A inversão bit a bit em tipos booleanos, "~True" ou "~False" foi
    descontinuada desde o Python 3.12, pois produz resultados
    surpreendentes e não intuitivos ("-2" e "-1"). Use "not x" em vez
    disso para a negação lógica de um Booleano. No caso raro de você
    precisar da inversão bit a bit do inteiro subjacente, converta
    para "int" explicitamente ("~int(x)").

* "functools":

  * A chamada da implementação Python de "functools.reduce()" com
    *function* ou *sequence* como argumentos nomeados foi
    descontinuada desde o Python 3.14.

* "logging":

  * O suporte para manipuladores de registro personalizados com o
    argumento *strm* foi descontinuado e está programado para ser
    removido no Python 3.16. Em vez disso, defina manipuladores com o
    argumento *stream*. (Contribuição de Mariusz Felisiak em
    gh-115032.)

* "mimetypes":

  * Extensões válidas começam com um '.' ou estão vazias para
    "mimetypes.MimeTypes.add_type()". Extensões sem ponto estão
    descontinuadas e levantarão uma exceção "ValueError" no Python
    3.16. (Contribuição de Hugo van Kemenade em gh-75223.)

* "shutil":

  * A exceção "ExecError" foi descontinuada desde o Python 3.14. Ela
    não foi usada por nenhuma função em "shutil" desde o Python 3.4, e
    agora é um alias de "RuntimeError".

* "symtable":

  * O método "Class.get_methods" foi descontinuado desde o Python
    3.14.

* "sys":

  * A função "_enablelegacywindowsfsencoding()" foi descontinuada
    desde o Python 3.13. Use a variável de ambiente
    "PYTHONLEGACYWINDOWSFSENCODING".

* "sysconfig":

  * A função "sysconfig.expand_makefile_vars()" está descontinuada
    desde o Python 3.14. Em vez disso, use o argumento "vars" de
    "sysconfig.get_paths()".

* "tarfile":

  * O atributo não documentado e não utilizado "TarFile.tarfile" foi
    descontinuado desde o Python 3.13.
