Introdução
**********

A Interface de Programação de Aplicações (API) para Python fornece aos
programadores C e C++ acesso ao interpretador Python em uma variedade
de níveis. A API pode ser usada igualmente em C++, mas, para abreviar,
geralmente é chamada de API Python/C. Existem dois motivos
fundamentalmente diferentes para usar a API Python/C. A primeira razão
é escrever *módulos de extensão* para propósitos específicos; esses
são módulos C que estendem o interpretador Python. Este é
provavelmente o uso mais comum. O segundo motivo é usar Python como um
componente em uma aplicação maior; esta técnica é geralmente referida
como *incorporação* Python em uma aplicação.

Escrever um módulo de extensão é um processo relativamente bem
compreendido, no qual uma abordagem de "livro de receitas" funciona
bem. Existem várias ferramentas que automatizam o processo até certo
ponto. Embora as pessoas tenham incorporado o Python em outras
aplicações desde sua existência inicial, o processo de incorporação do
Python é menos direto do que escrever uma extensão.

Muitas funções da API são úteis independentemente de você estar
incorporando ou estendendo o Python; além disso, a maioria das
aplicações que incorporam Python também precisará fornecer uma
extensão customizada, portanto, é provavelmente uma boa ideia se
familiarizar com a escrita de uma extensão antes de tentar incorporar
Python em uma aplicação real.


Compatibilidade com a versão da linguagem
=========================================

A API C do Python é compatível com as versões C11 e C++11 do C e C++.

Este é um limite inferior: a API C não requer recursos de versões
posteriores de C/C++. Você *não* precisa habilitar o "modo c11" do seu
compilador.


Padrões de codificação
======================

Se você estiver escrevendo código C para inclusão no CPython, **deve**
seguir as diretrizes e padrões definidos na **PEP 7**. Essas
diretrizes se aplicam independentemente da versão do Python com a qual
você está contribuindo. Seguir essas convenções não é necessário para
seus próprios módulos de extensão de terceiros, a menos que você
eventualmente espere contribuí-los para o Python.


Arquivos de inclusão
====================

Todas as definições de função, tipo e macro necessárias para usar a
API Python/C estão incluídas em seu código pela seguinte linha:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

Isso implica a inclusão dos seguintes cabeçalhos padrão: "<stdio.h>",
"<string.h>", "<errno.h>", "<limits.h>", "<assert.h>" e "<stdlib.h>"
(se disponível).

Nota:

  Uma vez que Python pode definir algumas definições de
  pré-processador que afetam os cabeçalhos padrão em alguns sistemas,
  você *deve* incluir "Python.h" antes de quaisquer cabeçalhos padrão
  serem incluídos.É recomendável sempre definir "PY_SSIZE_T_CLEAN"
  antes de incluir "Python.h". Veja Análise de argumentos e construção
  de valores para uma descrição desta macro.

Todos os nomes visíveis ao usuário definidos por Python.h (exceto
aqueles definidos pelos cabeçalhos padrão incluídos) têm um dos
prefixos "Py" ou "_Py". Nomes começando com "_Py" são para uso interno
pela implementação Python e não devem ser usados por escritores de
extensão. Os nomes dos membros da estrutura não têm um prefixo
reservado.

Nota:

  O código do usuário nunca deve definir nomes que começam com "Py" ou
  "_Py". Isso confunde o leitor e coloca em risco a portabilidade do
  código do usuário para versões futuras do Python, que podem definir
  nomes adicionais começando com um desses prefixos.

Os arquivos de cabeçalho são normalmente instalados com Python. No
Unix, eles estão localizados nos diretórios
"*prefix*/include/pythonversion/" e
"*exec_prefix*/include/pythonversion/", onde "prefix" e "exec_prefix"
são definidos pelos parâmetros correspondentes ao script **configure**
e *version* do Python é "'%d.%d' % sys.version_info[:2]". No Windows,
os cabeçalhos são instalados em "*prefix*/include", onde "prefix" é o
diretório de instalação especificado para o instalador.

Para incluir os cabeçalhos, coloque os dois diretórios (se diferentes)
no caminho de pesquisa do compilador para as inclusões. *Não* coloque
os diretórios pais no caminho de busca e então use "#include
<pythonX.Y/Python.h>"; isto irá quebrar em compilações
multiplataforma, uma vez que os cabeçalhos independentes da plataforma
em "prefix" incluem os cabeçalhos específicos da plataforma de
"exec_prefix".

Os usuários de C++ devem notar que embora a API seja definida
inteiramente usando C, os arquivos de cabeçalho declaram
apropriadamente os pontos de entrada como "extern "C"". Como
resultado, não há necessidade de fazer nada especial para usar a API
do C++.


System includes
---------------

   "Python.h" includes several standard header files. C extensions
   should include the standard headers that they use, and should not
   rely on these implicit includes. The implicit includes are:

   * "<assert.h>"

   * "<intrin.h>" (on Windows)

   * "<inttypes.h>"

   * "<limits.h>"

   * "<math.h>"

   * "<stdarg.h>"

   * "<string.h>"

   * "<wchar.h>"

   * "<sys/types.h>" (if present)

   The following are included for backwards compatibility, unless
   using Limited API 3.13 or newer:

   * "<ctype.h>"

   * "<unistd.h>" (on POSIX)

   The following are included for backwards compatibility, unless
   using Limited API 3.11 or newer:

   * "<errno.h>"

   * "<stdio.h>"

   * "<stdlib.h>"

Nota:

  Uma vez que Python pode definir algumas definições de
  pré-processador que afetam os cabeçalhos padrão em alguns sistemas,
  você *deve* incluir "Python.h" antes de quaisquer cabeçalhos padrão
  serem incluídos.


Macros úteis
============

Diversas macros úteis são definidas nos arquivos de cabeçalho do
Python. Muitas são definidas mais próximas de onde são úteis (por
exemplo, "Py_RETURN_NONE", "PyMODINIT_FUNC"). Outras de utilidade mais
geral são definidas aqui. Esta não é necessariamente uma lista
completa.

Py_CAN_START_THREADS

   If this macro is defined, then the current system is able to start
   threads.

   Currently, all systems supported by CPython (per **PEP 11**), with
   the exception of some WebAssembly platforms, support starting
   threads.

   Adicionado na versão 3.13.

Py_GETENV(s)

   Like "getenv(*s*)", but returns "NULL" if "-E" was passed on the
   command line (see "PyConfig.use_environment").


Docstring macros
----------------

PyDoc_STRVAR(name, str)

   Creates a variable with name *name* that can be used in docstrings.
   If Python is built without docstrings ("--without-doc-strings"),
   the value will be an empty string.

   Exemplo:

      PyDoc_STRVAR(pop_doc, "Remove e retorna o elemento mais à direita.");

      static PyMethodDef deque_methods[] = {
          // ...
          {"pop", (PyCFunction)deque_pop, METH_NOARGS, pop_doc},
          // ...
      }

   Expands to "PyDoc_VAR(*name*) = PyDoc_STR(*str*)".

PyDoc_STR(str)

   Expands to the given input string, or an empty string if docstrings
   are disabled ("--without-doc-strings").

   Exemplo:

      static PyMethodDef pysqlite_row_methods[] = {
          {"keys", (PyCFunction)pysqlite_row_keys, METH_NOARGS,
              PyDoc_STR("Retorna as chaves da linha.")},
          {NULL, NULL}
      };

PyDoc_VAR(name)

   Declares a static character array variable with the given *name*.
   Expands to "static const char *name*[]"

   Por exemplo:

      PyDoc_VAR(python_doc) = PyDoc_STR(
         "A genus of constricting snakes in the Pythonidae family native "
         "to the tropics and subtropics of the Eastern Hemisphere.");


General utility macros
----------------------

The following macros are for common tasks not specific to Python.

Py_UNUSED(arg)

   Use isso para argumentos não usados em uma definição de função para
   silenciar avisos do compilador. Exemplo: "int func(int a, int
   Py_UNUSED(b)) { return a; }".

   Adicionado na versão 3.4.

Py_GCC_ATTRIBUTE(name)

   Use a GCC attribute *name*, hiding it from compilers that don't
   support GCC attributes (such as MSVC).

   This expands to "__attribute__((*name)*)" on a GCC compiler, and
   expands to nothing on compilers that don't support GCC attributes.


Numeric utilities
~~~~~~~~~~~~~~~~~

Py_ABS(x)

   Retorna o valor absoluto de "x".

   The argument may be evaluated more than once. Consequently, do not
   pass an expression with side-effects directly to this macro.

   Se o resultado não puder ser representado (por exemplo, se "x"
   tiver o valor "INT_MIN" para o tipo int), o comportamento é
   indefinido.

   Corresponds roughly to "((*x*) < 0 ? -(*x*) : (*x*))"

   Adicionado na versão 3.3.

Py_MAX(x, y)
Py_MIN(x, y)

   Return the larger or smaller of the arguments, respectively.

   Any arguments may be evaluated more than once. Consequently, do not
   pass an expression with side-effects directly to this macro.

   "Py_MAX" corresponds roughly to "(((*x*) > (*y*)) ? (*x*) :
   (*y*))".

   Adicionado na versão 3.3.

Py_ARITHMETIC_RIGHT_SHIFT(type, integer, positions)

   Similar to "*integer* >> *positions*", but forces sign extension,
   as the C standard does not define whether a right-shift of a signed
   integer will perform sign extension or a zero-fill.

   *integer* should be any signed integer type. *positions* is the
   number of positions to shift to the right.

   Both *integer* and *positions* can be evaluated more than once;
   consequently, avoid directly passing a function call or some other
   operation with side-effects to this macro. Instead, store the
   result as a variable and then pass it.

   *type* is unused and only kept for backwards compatibility.
   Historically, *type* was used to cast *integer*.

   Alterado na versão 3.1: This macro is now valid for all signed
   integer types, not just those for which "unsigned type" is legal.
   As a result, *type* is no longer used.

Py_CHARMASK(c)

   O argumento deve ser um caractere ou um número inteiro no intervalo
   [-128, 127] ou [0, 255]. Esta macro retorna "c" convertido em um
   "unsigned char".

PY_BIG_ENDIAN
PY_LITTLE_ENDIAN

   Constants describing the byte order of the platform that Python was
   built for. Exactly one of them is "1" and the other is "0".


Assertion utilities
~~~~~~~~~~~~~~~~~~~

Py_UNREACHABLE()

   Use isso quando você tiver um caminho de código que não pode ser
   alcançado por design. Por exemplo, na cláusula "default:" em uma
   instrução "switch" para a qual todos os valores possíveis são
   incluídos nas instruções "case". Use isto em lugares onde você pode
   ficar tentado a colocar uma chamada "assert(0)" ou "abort()".

   No modo de lançamento, a macro ajuda o compilador a otimizar o
   código e evita um aviso sobre código inacessível. Por exemplo, a
   macro é implementada com "__builtin_unreachable()" no GCC em modo
   de lançamento.

   In debug mode, and on unsupported compilers, the macro expands to a
   call to "Py_FatalError()".

   A use for "Py_UNREACHABLE()" is following a call to a function that
   never returns but that is not declared "_Noreturn".

   Se um caminho de código for um código muito improvável, mas puder
   ser alcançado em casos excepcionais, esta macro não deve ser usada.
   Por exemplo, sob condição de pouca memória ou se uma chamada de
   sistema retornar um valor fora do intervalo esperado. Nesse caso, é
   melhor relatar o erro ao chamador. Se o erro não puder ser
   reportado ao chamador, "Py_FatalError()" pode ser usada.

   Adicionado na versão 3.7.

Py_SAFE_DOWNCAST(value, larger, smaller)

   Cast *value* to type *smaller* from type *larger*, validating that
   no information was lost.

   On release builds of Python, this is roughly equivalent to
   "((*smaller*) *value*)" (in C++, "static_cast<*smaller*>(*value*)"
   will be used instead).

   On debug builds (implying that "Py_DEBUG" is defined), this asserts
   that no information was lost with the cast from *larger* to
   *smaller*.

   *value*, *larger*, and *smaller* may all be evaluated more than
   once in the expression; consequently, do not pass an expression
   with side-effects directly to this macro.

Py_BUILD_ASSERT(cond)

   Realiza asserção de uma condição de tempo de compilação *cond*,
   como uma instrução. A construção falhará se a condição for falsa ou
   não puder ser avaliada em tempo de compilação.

   Corresponds roughly to "static_assert(*cond*)" on C23 and above.

   Por exemplo:

      Py_BUILD_ASSERT(sizeof(PyTime_t) == sizeof(int64_t));

   Adicionado na versão 3.3.

Py_BUILD_ASSERT_EXPR(cond)

   Realiza asserção de uma condição de tempo de compilação *cond*,
   como uma expressão que é avaliada com "0". A construção falhará se
   a condição for falsa ou não puder ser avaliada em tempo de
   compilação.

   Por exemplo:

      #define foo_to_char(foo) \
          ((char *)(foo) + Py_BUILD_ASSERT_EXPR(offsetof(struct foo, string) == 0))

   Adicionado na versão 3.3.


Type size utilities
~~~~~~~~~~~~~~~~~~~

Py_ARRAY_LENGTH(array)

   Calcula o comprimento de um vetor C alocado estaticamente em tempo
   de compilação.

   O argumento *array* deve ser um vetor C com tamanho conhecido em
   tempo de compilação. Passar um vetor com tamanho desconhecido, como
   um vetor alocado na heap, resultará em um erro de compilação em
   alguns compiladores ou produzirá resultados incorretos.

   Isso é aproximadamente equivalente a:

      sizeof(array) / sizeof((array)[0])

Py_MEMBER_SIZE(type, member)

   Return the size of a structure (*type*) *member* in bytes.

   Corresponds roughly to "sizeof(((*type* *)NULL)->*member*)".

   Adicionado na versão 3.6.


Macro definition utilities
~~~~~~~~~~~~~~~~~~~~~~~~~~

Py_FORCE_EXPANSION(X)

   This is equivalent to "*X*", which is useful for token-pasting in
   macros, as macro expansions in *X* are forcefully evaluated by the
   preprocessor.

Py_STRINGIFY(x)

   Convert "x" to a C string.  For example, "Py_STRINGIFY(123)"
   returns ""123"".

   Adicionado na versão 3.4.


Declaration utilities
---------------------

The following macros can be used in declarations. They are most useful
for defining the C API itself, and have limited use for extension
authors. Most of them expand to compiler-specific spellings of common
extensions to the C language.

Py_ALWAYS_INLINE

   Pede ao compilador para sempre embutir uma função em linha
   estática. O compilador pode ignorá-lo e decide não inserir a
   função.

   Corresponds to "always_inline" attribute in GCC and "__forceinline"
   in MSVC.

   Ele pode ser usado para inserir funções em linha estáticas críticas
   de desempenho ao compilar Python no modo de depuração com função de
   inserir em linha desabilitada. Por exemplo, o MSC desabilita a
   função de inserir em linha ao compilar no modo de depuração.

   Marcar cegamente uma função em linha estática com Py_ALWAYS_INLINE
   pode resultar em desempenhos piores (devido ao aumento do tamanho
   do código, por exemplo). O compilador geralmente é mais inteligente
   que o desenvolvedor para a análise de custo/benefício.

   Se o Python tiver sido compilado em modo de depuração (se a macro
   "Py_DEBUG" estiver definida), a macro "Py_ALWAYS_INLINE" não fará
   nada.

   Deve ser especificado antes do tipo de retorno da função. Uso:

      static inline Py_ALWAYS_INLINE int random(void) { return 4; }

   Adicionado na versão 3.11.

Py_NO_INLINE

   Desabilita a inserção em linha em uma função. Por exemplo, isso
   reduz o consumo da pilha C: útil em compilações LTO+PGO que faz uso
   intenso de inserção em linha de código (veja bpo-33720).

   Corresponds to the "noinline" attribute/specification on GCC and
   MSVC.

   Uso:

      Py_NO_INLINE static int random(void) { return 4; }

   Adicionado na versão 3.11.

Py_DEPRECATED(version)

   Use this to declare APIs that were deprecated in a specific CPython
   version. The macro must be placed before the symbol name.

   Exemplo:

      Py_DEPRECATED(3.8) PyAPI_FUNC(int) Py_OldFunction(void);

   Alterado na versão 3.8: Suporte a MSVC foi adicionado.

Py_LOCAL(type)

   Declare a function returning the specified *type* using a fast-
   calling qualifier for functions that are local to the current file.
   Semantically, this is equivalent to "static *type*".

Py_LOCAL_INLINE(type)

   Equivalente a "Py_LOCAL", mas que também exige que a função seja
   inserida localmente.

Py_LOCAL_SYMBOL

   Macro used to declare a symbol as local to the shared library
   (hidden). On supported platforms, it ensures the symbol is not
   exported.

   On compatible versions of GCC/Clang, it expands to
   "__attribute__((visibility("hidden")))".

Py_EXPORTED_SYMBOL

   Macro used to declare a symbol (function or data) as exported. On
   Windows, this expands to "__declspec(dllexport)". On compatible
   versions of GCC/Clang, it expands to
   "__attribute__((visibility("default")))". This macro is for
   defining the C API itself; extension modules should not use it.

Py_IMPORTED_SYMBOL

   Macro used to declare a symbol as imported. On Windows, this
   expands to "__declspec(dllimport)". This macro is for defining the
   C API itself; extension modules should not use it.

PyAPI_FUNC(type)

   Macro used by CPython to declare a function as part of the C API.
   Its expansion depends on the platform and build configuration. This
   macro is intended for defining CPython's C API itself; extension
   modules should not use it for their own symbols.

PyAPI_DATA(type)

   Macro used by CPython to declare a public global variable as part
   of the C API. Its expansion depends on the platform and build
   configuration. This macro is intended for defining CPython's C API
   itself; extension modules should not use it for their own symbols.


Outdated macros
---------------

The following *soft deprecated* macros have been used to features that
have been standardized in C11 (or previous standards).

Py_ALIGNED(num)

   On some GCC-like compilers, specify alignment to *num* bytes. This
   does nothing on other compilers.

   Use the standard "alignas" specifier rather than this macro.

   Suavemente descontinuado desde a versão 3.15.

PY_FORMAT_SIZE_T

   The "printf()" formatting modifier for "size_t". Use ""z"" directly
   instead.

   Suavemente descontinuado desde a versão 3.15.

Py_LL(number)
Py_ULL(number)

   Use *number* as a "long long" or "unsigned long long" integer
   literal, respectively.

   Expands to *number* followed by "LL" or "LLU", respectively, but
   will expand to some compiler-specific suffixes on some older
   compilers.

   Consider using the C99 standard suffixes "LL" and "LLU" directly.

   Suavemente descontinuado desde a versão 3.15.

PY_LONG_LONG
PY_INT32_T
PY_UINT32_T
PY_INT64_T
PY_UINT64_T

   Aliases for the types "long long", "int32_t", "uint32_t". "int64_t"
   and "uint64_t", respectively. Historically, these types needed
   compiler-specific extensions.

   Suavemente descontinuado desde a versão 3.15.

PY_LLONG_MIN
PY_LLONG_MAX
PY_ULLONG_MAX
PY_SIZE_MAX

   Aliases for the values "LLONG_MIN", "LLONG_MAX", "ULLONG_MAX", and
   "SIZE_MAX", respectively. Use these standard names instead.

   The required header, "<limits.h>", is included in "Python.h".

   Suavemente descontinuado desde a versão 3.15.

Py_MEMCPY(dest, src, n)

   This is an alias to "memcpy()".

   Suavemente descontinuado desde a versão 3.14: Use "memcpy()"
   directly instead.

Py_UNICODE_SIZE

   Size of the "wchar_t" type. Use "sizeof(wchar_t)" or
   "WCHAR_WIDTH/8" instead.

   The required header for the latter, "<limits.h>", is included in
   "Python.h".

   Suavemente descontinuado desde a versão 3.15.

Py_UNICODE_WIDE

   Defined if "wchar_t" can hold a Unicode character (UCS-4). Use
   "sizeof(wchar_t) >= 4" instead

   Suavemente descontinuado desde a versão 3.15.

Py_VA_COPY

   This is an alias to the C99-standard "va_copy" function.

   Historically, this would use a compiler-specific method to copy a
   "va_list".

   Alterado na versão 3.6: This is now an alias to "va_copy".

   Suavemente descontinuado desde a versão 3.15.


Objetos, tipos e contagens de referências
=========================================

A maioria das funções da API Python/C tem um ou mais argumentos, bem
como um valor de retorno do tipo PyObject*. Este tipo é um ponteiro
para um tipo de dados opaco que representa um objeto Python
arbitrário. Como todos os tipos de objeto Python são tratados da mesma
maneira pela linguagem Python na maioria das situações (por exemplo,
atribuições, regras de escopo e passagem de argumento), é adequado que
eles sejam representados por um único tipo C. Quase todos os objetos
Python vivem na pilha: você nunca declara uma variável automática ou
estática do tipo "PyObject", variáveis de apenas ponteiro do tipo
PyObject* podem ser declaradas. A única exceção são os objetos de
tipo; uma vez que estes nunca devem ser desalocados, eles são
normalmente objetos estáticos "PyTypeObject".

Todos os objetos Python (mesmo inteiros Python) têm um *tipo* e uma
*contagem de referências*. O tipo de um objeto determina que tipo de
objeto ele é (por exemplo, um número inteiro, uma lista ou uma função
definida pelo usuário; existem muitos mais, conforme explicado em A
hierarquia de tipos padrão). Para cada um dos tipos conhecidos, há uma
macro para verificar se um objeto é desse tipo; por exemplo,
"PyList_Check(a)" é verdadeiro se (e somente se) o objeto apontado por
*a* for uma lista Python.


Contagens de referências
------------------------

A contagem de referências é importante porque os computadores atuais
têm um tamanho de memória finito (e frequentemente severamente
limitado); ela conta quantos lugares diferentes existem que possuem
uma *referência forte* a um objeto. Tal lugar pode ser outro objeto,
ou uma variável C global (ou estática), ou uma variável local em
alguma função C. Quando a última *referência forte* a um objeto é
liberada (ou seja, sua contagem de referências se torna zero), o
objeto é desalocado. Se ele contiver referências a outros objetos,
essas referências são liberadas. Esses outros objetos podem ser
desalocados por sua vez, se não houver mais referências a eles, e
assim por diante. (Há um problema óbvio com objetos que referenciam
uns aos outros aqui; por enquanto, a solução é "não faça isso".)

Contagens de referências são sempre manipuladas explicitamente. A
maneira normal é usar a macro "Py_INCREF()" para obter uma nova
referência a um objeto (ou seja, incrementar sua contagem de
referências em um), e "Py_DECREF()" para liberar essa referência (ou
seja, decrementar a contagem de referências em um). A macro
"Py_DECREF()" é consideravelmente mais complexa do que a incref, pois
deve verificar se a contagem de referências se torna zero e, em
seguida, fazer com que o desalocador do objeto seja chamado. O
desalocador é um ponteiro para função contido na estrutura de tipo do
objeto. O desalocador específico do tipo cuida da liberação de
referências para outros objetos contidos no objeto se este for um tipo
de objeto composto, como uma lista, bem como de executar qualquer
finalização adicional necessária. Não há chance de a contagem de
referências transbordar; pelo menos tantos bits são usados para
armazenar a contagem de referência quantos forem os locais de memória
distintos na memória virtual (presumindo "sizeof(Py_ssize_t) >=
sizeof(void*)"). Portanto, o incremento da contagem de referências é
uma operação simples.

Não é necessário manter uma *referência forte* (ou seja, incrementar a
contagem de referências) para cada variável local que contém um
ponteiro para um objeto. Em teoria, a contagem de referências do
objeto aumenta em um quando a variável é feita para apontar para ele e
diminui em um quando a variável sai do escopo. No entanto, esses dois
se cancelam, portanto, no final, a contagem de referências não mudou.
A única razão real para usar a contagem de referências é evitar que o
objeto seja desalocado enquanto nossa variável estiver apontando para
ele. Se sabemos que existe pelo menos uma outra referência ao objeto
que vive pelo menos tanto quanto nossa variável, não há necessidade de
tomar uma nova *referência forte* (ou seja, incrementar a contagem de
referências) temporariamente. Uma situação importante em que isso
ocorre é em objetos que são passados como argumentos para funções C em
um módulo de extensão que são chamados de Python; o mecanismo de
chamada garante manter uma referência a todos os argumentos durante a
chamada.

No entanto, uma armadilha comum é extrair um objeto de uma lista e
mantê-lo por um tempo, sem tomar uma nova referência. Alguma outra
operação poderia remover o objeto da lista, liberando essa referência
e possivelmente desalocando-o. O perigo real é que operações
aparentemente inocentes podem invocar código Python arbitrário que
poderia fazer isso; existe um caminho de código que permite que o
controle flua de volta para o usuário a partir de um "Py_DECREF()",
então quase qualquer operação é potencialmente perigosa.

Uma abordagem segura é sempre usar as operações genéricas (funções
cujo nome começa com "PyObject_", "PyNumber_", "PySequence_" ou
"PyMapping_"). Essas operações sempre criam uma nova *referência
forte* (ou seja, incrementam a contagem de referências) do objeto que
retornam. Isso deixa o chamador com a responsabilidade de chamar
"Py_DECREF()" quando terminar com o resultado; isso logo se torna uma
segunda natureza.


Detalhes da contagem de referências
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O comportamento da contagem de referências de funções na API C/Python
é melhor explicado em termos de *propriedade de referências*. A
propriedade pertence às referências, nunca aos objetos (os objetos não
são possuídos: eles são sempre compartilhados). "Possuir uma
referência" significa ser responsável por chamar Py_DECREF nela quando
a referência não for mais necessária. A propriedade também pode ser
transferida, o que significa que o código que recebe a propriedade da
referência torna-se responsável por eventualmente efetuar um liberando
ela chamando "Py_DECREF()" ou "Py_XDECREF()" quando não é mais
necessário -- ou passando essa responsabilidade (geralmente para o
responsável pela chamada). Quando uma função passa a propriedade de
uma referência para seu chamador, diz-se que o chamador recebe uma
*nova* referência. Quando nenhuma propriedade é transferida, diz-se
que o chamador *toma emprestado* a referência. Nada precisa ser feito
para uma *referência emprestada*.

Conversely, when a calling function passes in a reference to an
object, there are two possibilities: the function *steals* a
reference to the object, or it does not.

*Stealing a reference* means that when you pass a reference to a
function, that function assumes that it now owns that reference. Since
the new owner can use "Py_DECREF()" at its discretion, you (the
caller) must not use that reference after the call.

Poucas funções roubam referências; as duas exceções notáveis são
"PyList_SetItem()" e "PyTuple_SetItem()", que roubam uma referência
para o item (mas não para a tupla ou lista na qual o item é
colocado!). Essas funções foram projetadas para roubar uma referência
devido a um idioma comum para preencher uma tupla ou lista com objetos
recém-criados; por exemplo, o código para criar a tupla "(1, 2,
"three")" pode ser parecido com isto (esquecendo o tratamento de erros
por enquanto; uma maneira melhor de codificar isso é mostrada abaixo):

   PyObject *t;

   t = PyTuple_New(3);
   PyTuple_SetItem(t, 0, PyLong_FromLong(1L));
   PyTuple_SetItem(t, 1, PyLong_FromLong(2L));
   PyTuple_SetItem(t, 2, PyUnicode_FromString("três"));

Aqui, "PyLong_FromLong()" retorna uma nova referência que é
imediatamente roubada por "PyTuple_SetItem()". Quando você quiser
continuar usando um objeto, embora a referência a ele seja roubada,
use "Py_INCREF()" para obter outra referência antes de chamar a função
de roubo de referência.

A propósito, "PyTuple_SetItem()" é a *única* maneira de definir itens
de tupla; "PySequence_SetItem()" e "PyObject_SetItem()" se recusam a
fazer isso, pois tuplas são um tipo de dados imutável. Você só deve
usar "PyTuple_SetItem()" para tuplas que você mesmo está criando.

O código equivalente para preencher uma lista pode ser escrita usando
"PyList_New()" e "PyList_SetItem()".

No entanto, na prática, você raramente usará essas maneiras de criar e
preencher uma tupla ou lista. Existe uma função genérica,
"Py_BuildValue()", que pode criar objetos mais comuns a partir de
valores C, dirigidos por uma *string de formato*. Por exemplo, os dois
blocos de código acima podem ser substituídos pelos seguintes (que
também cuidam da verificação de erros):

   PyObject *tuple, *list;

   tuple = Py_BuildValue("(iis)", 1, 2, "três");
   list = Py_BuildValue("[iis]", 1, 2, "três");

É muito mais comum usar "PyObject_SetItem()" e amigos com itens cujas
referências você está apenas pegando emprestado, como argumentos que
foram passados para a função que você está escrevendo. Nesse caso, o
comportamento deles em relação às referências é muito mais são, já que
você não precisa tomar uma nova referência só para poder doá-la
("mande-a ser roubada"). Por exemplo, esta função define todos os
itens de uma lista (na verdade, qualquer sequência mutável) para um
determinado item:

   int
   set_all(PyObject *target, PyObject *item)
   {
       Py_ssize_t i, n;

       n = PyObject_Length(target);
       if (n < 0)
           return -1;
       for (i = 0; i < n; i++) {
           PyObject *index = PyLong_FromSsize_t(i);
           if (!index)
               return -1;
           if (PyObject_SetItem(target, index, item) < 0) {
               Py_DECREF(index);
               return -1;
           }
           Py_DECREF(index);
       }
       return 0;
   }

A situação é ligeiramente diferente para os valores de retorno da
função. Embora passar uma referência para a maioria das funções não
altere suas responsabilidades de propriedade para aquela referência,
muitas funções que retornam uma referência a um objeto fornecem a
propriedade da referência. O motivo é simples: em muitos casos, o
objeto retornado é criado instantaneamente e a referência que você
obtém é a única referência ao objeto. Portanto, as funções genéricas
que retornam referências a objetos, como "PyObject_GetItem()" e
"PySequence_GetItem()", sempre retornam uma nova referência (o
chamador torna-se o dono da referência).

É importante perceber que se você possui uma referência retornada por
uma função depende de qual função você chama apenas --- *a plumagem*
(o tipo do objeto passado como um argumento para a função) *não entra
nela!* Assim, se você extrair um item de uma lista usando
"PyList_GetItem()", você não possui a referência --- mas se obtiver o
mesmo item da mesma lista usando "PySequence_GetItem()" (que leva
exatamente os mesmos argumentos), você possui uma referência ao objeto
retornado.

Aqui está um exemplo de como você poderia escrever uma função que
calcula a soma dos itens em uma lista de inteiros; uma vez usando
"PyList_GetItem()", e uma vez usando "PySequence_GetItem()".

   long
   sum_list(PyObject *list)
   {
       Py_ssize_t i, n;
       long total = 0, value;
       PyObject *item;

       n = PyList_Size(list);
       if (n < 0)
           return -1; /* Não é uma lista */
       for (i = 0; i < n; i++) {
           item = PyList_GetItem(list, i); /* Não pode falhar */
           if (!PyLong_Check(item)) continue; /* Ignora não-inteiros */
           value = PyLong_AsLong(item);
           if (value == -1 && PyErr_Occurred())
               /* Inteiro muito grande para caber em um C longo, sai */
               return -1;
           total += value;
       }
       return total;
   }

   long
   sum_sequence(PyObject *sequence)
   {
       Py_ssize_t i, n;
       long total = 0, value;
       PyObject *item;
       n = PySequence_Length(sequence);
       if (n < 0)
           return -1; /* Não tem comprimento */
       for (i = 0; i < n; i++) {
           item = PySequence_GetItem(sequence, i);
           if (item == NULL)
               return -1; /* Não é uma sequência ou outra falha */
           if (PyLong_Check(item)) {
               value = PyLong_AsLong(item);
               Py_DECREF(item);
               if (value == -1 && PyErr_Occurred())
                   /* Inteiro muito grande para caber em um C longo, sai */
                   return -1;
               total += value;
           }
           else {
               Py_DECREF(item); /* Descartar propriedade de referência */
           }
       }
       return total;
   }


Tipos
-----

Existem alguns outros tipos de dados que desempenham um papel
significativo na API Python/C; a maioria são tipos C simples, como
int, long, double e char*. Alguns tipos de estrutura são usados para
descrever tabelas estáticas usadas para listar as funções exportadas
por um módulo ou os atributos de dados de um novo tipo de objeto, e
outro é usado para descrever o valor de um número complexo. Eles serão
discutidos junto com as funções que os utilizam.

type Py_ssize_t
    * Parte da ABI Estável.*

   A signed integral type such that "sizeof(Py_ssize_t) ==
   sizeof(size_t)". C99 doesn't define such a thing directly (size_t
   is an unsigned integral type). See **PEP 353** for details.

Py_INVALID_SIZE

   A constant of type "Py_ssize_t" with value "-1", representing an
   invalid size.

PY_SSIZE_T_MAX
PY_SSIZE_T_MIN

   The limit values (largest positive one and smallest negative one,
   respectively) of type "Py_ssize_t".

PY_DWORD_MAX

   The maximum value of the Windows "DWORD" type. Expands to
   "0xffffffff" on all platforms.


Exceções
========

O programador Python só precisa lidar com exceções se o tratamento de
erros específico for necessário; as exceções não tratadas são
propagadas automaticamente para o chamador, depois para o chamador e
assim por diante, até chegarem ao interpretador de nível superior,
onde são relatadas ao usuário acompanhadas por um traceback (situação
da pilha de execução).

Para programadores C, entretanto, a verificação de erros sempre deve
ser explícita. Todas as funções na API Python/C podem levantar
exceções, a menos que uma declaração explícita seja feita de outra
forma na documentação de uma função. Em geral, quando uma função
encontra um erro, ela define uma exceção, descarta todas as
referências de objeto de sua propriedade e retorna um indicador de
erro. Se não for documentado de outra forma, este indicador é "NULL"
ou "-1", dependendo do tipo de retorno da função. Algumas funções
retornam um resultado booleano verdadeiro/falso, com falso indicando
um erro. Muito poucas funções não retornam nenhum indicador de erro
explícito ou têm um valor de retorno ambíguo e requerem teste
explícito para erros com "PyErr_Occurred()". Essas exceções são sempre
documentadas explicitamente.

O estado de exceção é mantido no armazenamento por thread (isso é
equivalente a usar o armazenamento global em uma aplicação sem
thread). Uma thread pode estar em um de dois estados: ocorreu uma
exceção ou não. A função "PyErr_Occurred()" pode ser usada para
verificar isso: ela retorna uma referência emprestada ao objeto do
tipo de exceção quando uma exceção ocorreu, e "NULL" caso contrário.
Existem várias funções para definir o estado de exceção:
"PyErr_SetString()" é a função mais comum (embora não a mais geral)
para definir o estado de exceção, e "PyErr_Clear()" limpa o estado da
exceção.

O estado de exceção completo consiste em três objetos (todos os quais
podem ser "NULL"): o tipo de exceção, o valor de exceção
correspondente e o traceback. Eles têm os mesmos significados que o
resultado no Python de "sys.exc_info()"; no entanto, eles não são os
mesmos: os objetos Python representam a última exceção sendo tratada
por uma instrução Python "try" ... "except", enquanto o estado de
exceção de nível C só existe enquanto uma exceção está sendo
transmitido entre funções C até atingir o laço de repetição principal
do interpretador de bytecode Python, que se encarrega de transferi-lo
para "sys.exc_info()" e amigos.

Observe que a partir do Python 1.5, a maneira preferida e segura para
thread para acessar o estado de exceção do código Python é chamar a
função "sys.exc_info()", que retorna o estado de exceção por thread
para o código Python. Além disso, a semântica de ambas as maneiras de
acessar o estado de exceção mudou, de modo que uma função que captura
uma exceção salvará e restaurará o estado de exceção de seu segmento
de modo a preservar o estado de exceção de seu chamador. Isso evita
bugs comuns no código de tratamento de exceções causados por uma
função aparentemente inocente sobrescrevendo a exceção sendo tratada;
também reduz a extensão da vida útil frequentemente indesejada para
objetos que são referenciados pelos quadros de pilha no traceback.

Como princípio geral, uma função que chama outra função para realizar
alguma tarefa deve verificar se a função chamada levantou uma exceção
e, em caso afirmativo, passar o estado da exceção para seu chamador.
Ele deve descartar todas as referências de objeto que possui e
retornar um indicador de erro, mas *não* deve definir outra exceção
--- que sobrescreveria a exceção que acabou de ser gerada e perderia
informações importantes sobre a causa exata do erro.

Um exemplo simples de detecção de exceções e transmiti-las é mostrado
no exemplo "sum_sequence()" acima. Acontece que este exemplo não
precisa limpar nenhuma referência de propriedade quando detecta um
erro. A função de exemplo a seguir mostra alguma limpeza de erro.
Primeiro, para lembrar por que você gosta de Python, mostramos o
código Python equivalente:

   def incr_item(dict, key):
       try:
           item = dict[key]
       except KeyError:
           item = 0
       dict[key] = item + 1

Aqui está o código C correspondente, em toda sua glória:

   int
   incr_item(PyObject *dict, PyObject *key)
   {
       /* Objetos todos inicializados para NULL para Py_XDECREF */
       PyObject *item = NULL, *const_one = NULL, *incremented_item = NULL;
       int rv = -1; /* Retorna valor inicializado para -1 (falha) */

       item = PyObject_GetItem(dict, key);
       if (item == NULL) {
           /* Trata de KeyError apenas: */
           if (!PyErr_ExceptionMatches(PyExc_KeyError))
               goto error;

           /* Limpa o erro e usa zero: */
           PyErr_Clear();
           item = PyLong_FromLong(0L);
           if (item == NULL)
               goto error;
       }
       const_one = PyLong_FromLong(1L);
       if (const_one == NULL)
           goto error;

       incremented_item = PyNumber_Add(item, const_one);
       if (incremented_item == NULL)
           goto error;

       if (PyObject_SetItem(dict, key, incremented_item) < 0)
           goto error;
       rv = 0; /* Success */
       /* Continua com o código de limpeza */

    error:
       /* Código de limpeza, compartilhado pelo caminho sucesso e falha */

       /* Usa Py_XDECREF() para ignorar referências NULL */
       Py_XDECREF(item);
       Py_XDECREF(const_one);
       Py_XDECREF(incremented_item);

       return rv; /* -1 para erro, 0 para sucesso */
   }

Este exemplo representa um uso endossado da instrução "goto" em C! Ele
ilustra o uso de "PyErr_ExceptionMatches()" e "PyErr_Clear()" para
lidar com exceções específicas, e o uso de "Py_XDECREF()" para
descartar referências de propriedade que podem ser "NULL" (observe o
"'X'" no nome; "Py_DECREF()" travaria quando confrontado com uma
referência "NULL"). É importante que as variáveis usadas para manter
as referências de propriedade sejam inicializadas com "NULL" para que
isso funcione; da mesma forma, o valor de retorno proposto é
inicializado para "-1" (falha) e apenas definido para sucesso após a
chamada final feita ser bem sucedida.


Incorporando Python
===================

A única tarefa importante com a qual apenas os incorporadores (em
oposição aos escritores de extensão) do interpretador Python precisam
se preocupar é a inicialização e, possivelmente, a finalização do
interpretador Python. A maior parte da funcionalidade do interpretador
só pode ser usada após a inicialização do interpretador.

A função de inicialização básica é "Py_Initialize()". Isso inicializa
a tabela de módulos carregados e cria os módulos fundamentais
"builtins", "__main__" e "sys". Ela também inicializa o caminho de
pesquisa de módulos ("sys.path").

"Py_Initialize()" não define a "lista de argumentos de script"
("sys.argv"). Se esta variável for necessária para o código Python que
será executado posteriormente, "PyConfig.argv" e "PyConfig.parse_argv"
devem estar definidas; veja Configuração de inicialização do Python.

Na maioria dos sistemas (em particular, no Unix e no Windows, embora
os detalhes sejam ligeiramente diferentes), "Py_Initialize()" calcula
o caminho de pesquisa de módulos com base em sua melhor estimativa
para a localização do executável do interpretador Python padrão,
presumindo que a biblioteca Python é encontrada em um local fixo em
relação ao executável do interpretador Python. Em particular, ele
procura por um diretório chamado "lib/python*X.Y*" relativo ao
diretório pai onde o executável chamado "python" é encontrado no
caminho de pesquisa de comandos do shell (a variável de ambiente
"PATH").

Por exemplo, se o executável Python for encontrado em
"/usr/local/bin/python", ele presumirá que as bibliotecas estão em
"/usr/local/lib/python*X.Y*". (Na verdade, este caminho particular
também é o local reserva, usado quando nenhum arquivo executável
chamado "python" é encontrado ao longo de "PATH".) O usuário pode
substituir este comportamento definindo a variável de ambiente
"PYTHONHOME", ou insira diretórios adicionais na frente do caminho
padrão definindo "PYTHONPATH".

The embedding application can steer the search by setting
"PyConfig.program_name" *before* calling "Py_InitializeFromConfig()".
Note that "PYTHONHOME" still overrides this and "PYTHONPATH" is still
inserted in front of the standard path.

Às vezes, é desejável "desinicializar" o Python. Por exemplo, a
aplicação pode querer iniciar novamente (fazer outra chamada para
"Py_Initialize()") ou a aplicação simplesmente termina com o uso de
Python e deseja liberar memória alocada pelo Python. Isso pode ser
feito chamando "Py_FinalizeEx()". A função "Py_IsInitialized()"
retorna verdadeiro se o Python está atualmente no estado inicializado.
Mais informações sobre essas funções são fornecidas em um capítulo
posterior. Observe que "Py_FinalizeEx()" *não* libera toda a memória
alocada pelo interpretador Python, por exemplo, a memória alocada por
módulos de extensão atualmente não pode ser liberada.


Compilações de depuração
========================

Python pode ser compilado com várias macros para permitir verificações
extras do interpretador e módulos de extensão. Essas verificações
tendem a adicionar uma grande quantidade de sobrecarga ao tempo de
execução, portanto, não são habilitadas por padrão.

Uma lista completa dos vários tipos de compilações de depuração está
no arquivo "Misc/SpecialBuilds.txt" na distribuição do código-fonte do
Python. Estão disponíveis compilações que oferecem suporte ao
rastreamento de contagens de referências, depuração do alocador de
memória ou criação de perfil de baixo nível do laço do interpretador
principal. Apenas as compilações usadas com mais frequência serão
descritas no restante desta seção.

Py_DEBUG

Compiling the interpreter with the "Py_DEBUG" macro defined produces
what is generally meant by a debug build of Python.

On Unix, "Py_DEBUG" can be enabled by adding "--with-pydebug" to the
"./configure" command. This will also disable compiler optimization.

On Windows, selecting a debug build (e.g., by passing the "-d" option
to "PCbuild/build.bat") automatically enables "Py_DEBUG".
Additionally, the presence of the not-Python-specific "_DEBUG" macro,
when defined by the compiler, will also implicitly enable "Py_DEBUG".

In addition to the reference count debugging described below, extra
checks are performed. See Python Debug Build for more details.

Defining "Py_TRACE_REFS" enables reference tracing (see the "configure
--with-trace-refs option"). When defined, a circular doubly linked
list of active objects is maintained by adding two extra fields to
every "PyObject".  Total allocations are tracked as well.  Upon exit,
all existing references are printed.  (In interactive mode this
happens after every statement run by the interpreter.)

Consulte "Misc/SpecialBuilds.txt" na distribuição do código-fonte
Python para informações mais detalhadas.


Ferramentas de terceiros recomendadas
=====================================

As seguintes ferramentas de terceiros oferecem abordagens mais simples
e mais sofisticadas para criar extensões C, C++ e Rust para Python:

* Cython

* cffi

* HPy

* nanobind (C++)

* Numba

* pybind11 (C++)

* PyO3 (Rust)

* SWIG

O uso de ferramentas como essas pode ajudar a evitar a criação de
código estritamente vinculado a uma versão específica do CPython,
evitar erros de contagem de referências e focar mais no seu próprio
código do que em usar a API do CPython. Em geral, novas versões do
Python podem ser suportadas atualizando a ferramenta, e seu código
frequentemente usará APIs mais novas e eficientes automaticamente.
Algumas ferramentas também oferecem suporte à compilação para outras
implementações do Python a partir de um único conjunto de fontes.

Esses projetos não são suportados pelas mesmas pessoas que mantêm o
Python, e quaisquer problemas precisam ser relatados diretamente aos
projetos. Lembre-se de verificar se o projeto ainda é mantido e tem
suporte, pois a lista acima pode ficar desatualizada.

Ver também:

  Guia do Usuário de Empacotamento do Python: Extensões Binárias
     O Guia do Usuário de Empacotamento do Python não abrange apenas
     várias ferramentas disponíveis que simplificam a criação de
     extensões binárias, mas também discute os vários motivos pelos
     quais a criação de um módulo de extensão pode ser desejável em
     primeiro lugar.
