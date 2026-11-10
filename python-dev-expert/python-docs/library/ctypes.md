"ctypes" --- Uma biblioteca de funções externas para Python
***********************************************************

**Código-fonte:** Lib/ctypes

======================================================================

"ctypes" é uma biblioteca de funções externas para Python. Ela fornece
tipos de dados compatíveis com C e permite chamar funções em DLLs ou
bibliotecas compartilhadas. Ela pode ser usada para agrupar essas
bibliotecas em Python puro.

Este é um *módulo opcional*. Se ele estiver faltando na sua cópia do
CPython, procure a documentação do seu distribuidor (ou seja, quem lhe
forneceu o Python). Se você for o distribuidor, consulte Requisitos
para módulos opcionais.

Aviso:

  "ctypes" provides low-level access to native libraries and the
  process's memory, bypassing Python's safety mechanisms and allowing
  execution of arbitrary native code. Incorrect use can corrupt data
  and objects, reveal sensitive information, cause crashes, or
  otherwise compromise the running process.


Tutorial do ctypes
==================

Nota: Alguns exemplos de código fazem referência ao tipo ctypes
"c_int". Em plataformas em que "sizeof(long) == sizeof(int)" é um
apelido para "c_long". Então, você não deve ficar confuso se "c_long"
for impresso se você esperaria "c_int" --- eles são, na verdade, o
mesmo tipo.


Carregando bibliotecas de ligação dinâmica
------------------------------------------

"ctypes" exports the "cdll", and on Windows "windll" and "oledll"
objects, for loading dynamic link libraries.

You load libraries by accessing them as attributes of these objects.
"cdll" loads libraries which export functions using the standard
"cdecl" calling convention, while "windll" libraries call functions
using the "stdcall" calling convention. "oledll" also uses the
"stdcall" calling convention, and assumes the functions return a
Windows "HRESULT" error code. The error code is used to automatically
raise an "OSError" exception when the function call fails.

Alterado na versão 3.3: Erros do Windows costumavam levantar
"WindowsError", que agora é um apelido de "OSError".

Veja alguns exemplos para Windows. Note que "msvcrt" é a biblioteca C
padrão da MS que contém a maioria das funções C padrão e usa a
convenção de chamada "cdecl":

   >>> from ctypes import *
   >>> print(windll.kernel32)
   <WinDLL 'kernel32', handle ... at ...>
   >>> print(cdll.msvcrt)
   <CDLL 'msvcrt', handle ... at ...>
   >>> libc = cdll.msvcrt
   >>>

O Windows acrescenta automaticamente o sufixo de arquivo ".dll" usual.

Nota:

  Acessar a biblioteca padrão C por meio de "cdll.msvcrt" usará uma
  versão desatualizada da biblioteca, que pode ser incompatível com a
  usada pelo Python. Onde possível, use a funcionalidade nativa do
  Python; caso contrário, importe e use o módulo "msvcrt".

Other systems require the filename *including* the extension to load a
library, so attribute access can not be used to load libraries. Either
the "LoadLibrary()" method of the dll loaders should be used, or you
should load the library by creating an instance of "CDLL" by calling
the constructor.

For example, on Linux:

   >>> cdll.LoadLibrary("libc.so.6")
   <CDLL 'libc.so.6', handle ... at ...>
   >>> libc = CDLL("libc.so.6")
   >>> libc
   <CDLL 'libc.so.6', handle ... at ...>
   >>>

On macOS:

   >>> cdll.LoadLibrary("libc.dylib")
   <CDLL 'libc.dylib', handle ... at ...>
   >>> libc = CDLL("libc.dylib")
   >>> libc
   <CDLL 'libc.dylib', handle ... at ...>


Acessando funções de dlls carregadas
------------------------------------

Funções são acessadas como atributos de objetos dll:

   >>> libc.printf
   <_FuncPtr object at 0x...>
   >>> print(windll.kernel32.GetModuleHandleA)
   <_FuncPtr object at 0x...>
   >>> print(windll.kernel32.MyOwnFunction)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "ctypes.py", line 239, in __getattr__
       func = _StdcallFuncPtr(name, self)
   AttributeError: function 'MyOwnFunction' not found
   >>>

Observe que DLLs de sistema do Win32, como "kernel32" e "user32",
frequentemente exportam versões ANSI e UNICODE de uma função. A versão
UNICODE é exportada com um "W" anexado ao nome, enquanto a versão ANSI
é exportada com um "A" anexado ao nome. A função "GetModuleHandle" do
Win32, que retorna um *identificador de módulo* para um determinado
nome de módulo, tem o seguinte protótipo em C, e uma macro é usada
para expor um deles como "GetModuleHandle", dependendo se UNICODE está
definido ou não:

   /* versão ANSI */
   HMODULE GetModuleHandleA(LPCSTR lpModuleName);
   /* versão UNICODE */
   HMODULE GetModuleHandleW(LPCWSTR lpModuleName);

*windll* não tenta selecionar um deles magicamente, você deve acessar
a versão necessária especificando "GetModuleHandleA" ou
"GetModuleHandleW" explicitamente e então chamá-lo com objetos bytes
ou string, respectivamente.

Às vezes, DLLs exportam funções com nomes que não são identificadores
Python válidos, como ""??2@YAPAXI@Z"". Nesse caso, você precisa usar
"getattr()" para recuperar a função:

   >>> getattr(cdll.msvcrt, "??2@YAPAXI@Z")
   <_FuncPtr object at 0x...>
   >>>

No Windows, algumas dlls exportam funções não por nome, mas por
ordinal. Essas funções podem ser acessadas indexando o objeto dll com
o número ordinal:

   >>> cdll.kernel32[1]
   <_FuncPtr object at 0x...>
   >>> cdll.kernel32[0]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "ctypes.py", line 310, in __getitem__
       func = _StdcallFuncPtr(name, self)
   AttributeError: function ordinal 0 not found
   >>>


Chamando funções
----------------

Você pode chamar essas funções como qualquer outro chamável do Python.
Este exemplo usa a função "rand()", que não aceita argumentos e
retorna um inteiro pseudoaleatório:

   >>> print(libc.rand())
   1804289383

No Windows, você pode chamar a função "GetModuleHandleA()", que
retorna um identificador de módulo win32 (passando "None" como único
argumento para chamá-lo com um ponteiro "NULL"):

   >>> print(hex(windll.kernel32.GetModuleHandleA(None)))
   0x1d000000
   >>>

"ctypes" cannot determine a function's calling convention or
signature. Consult the function's C header file or documentation to
choose the correct calling convention and set the "argtypes"
attribute, as described in Especificando os tipos de argumentos
necessários (protótipos de função). Without "argtypes", the number of
arguments is not checked. Calling a function with an incorrect calling
convention or with incorrect arguments can corrupt memory or crash
Python.

On Windows, "ctypes" uses win32 structured exception handling to
prevent crashes from general protection faults when functions are
called with invalid argument values:

   >>> windll.kernel32.GetModuleHandleA(32)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   OSError: exception: access violation reading 0x00000020
   >>>

The "faulthandler" module can help debug crashes, such as segmentation
faults produced by erroneous C library calls.

"None", inteiros, objetos bytes e strings (unicode) são os únicos
objetos nativos do Python que podem ser usados diretamente como
parâmetros nessas chamadas de função. "None" é passado como um
ponteiro "NULL" em C, objetos bytes e strings são passados como
ponteiros para o bloco de memória que contém seus dados (char* ou
wchar_t*). Inteiros em Python são passados como o tipo padrão da
plataforma em C int, e seu valor é mascarado para se encaixar no tipo
em C.

Before we move on calling functions with other parameter types, we
have to learn more about "ctypes" data types.


Tipos de dados fundamentais
---------------------------

"ctypes" define vários tipos de dados primitivos compatíveis com C:

+---------------------------+---------------------------+---------------------------+---------------------------+
| Tipo ctypes               | Tipo em C                 | Tipo em Python            | "_type_"                  |
|===========================|===========================|===========================|===========================|
| "c_bool"                  | _Bool                     | "bool"                    | "'?'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_char"                  | char                      | 1-character "bytes"       | "'c'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_wchar"                 | "wchar_t"                 | 1-character "str"         | "'u'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_byte"                  | char                      | "int"                     | "'b'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_ubyte"                 | unsigned char             | "int"                     | "'B'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_short"                 | short                     | "int"                     | "'h'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_ushort"                | unsigned short            | "int"                     | "'H'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_int"                   | int                       | "int"                     | "'i'" *                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_int8"                  | "int8_t"                  | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_int16"                 | "int16_t"                 | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_int32"                 | "int32_t"                 | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_int64"                 | "int64_t"                 | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_uint"                  | unsigned int              | "int"                     | "'I'" *                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_uint8"                 | "uint8_t"                 | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_uint16"                | "uint16_t"                | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_uint32"                | "uint32_t"                | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_uint64"                | "uint64_t"                | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_long"                  | long                      | "int"                     | "'l'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_ulong"                 | unsigned long             | "int"                     | "'L'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_longlong"              | long long                 | "int"                     | "'q'" *                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_ulonglong"             | unsigned long long        | "int"                     | "'Q'" *                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_size_t"                | "size_t"                  | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_ssize_t"               | "Py_ssize_t"              | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_time_t"                | "time_t"                  | "int"                     | *                         |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_float"                 | float                     | "float"                   | "'f'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_double"                | double                    | "float"                   | "'d'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_longdouble"            | long double               | "float"                   | "'g'" *                   |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_char_p"                | char* (finalizado com     | "bytes" or "None"         | "'z'"                     |
|                           | NUL)                      |                           |                           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_wchar_p"               | wchar_t* (finalizado com  | "str" or "None"           | "'Z'"                     |
|                           | NUL)                      |                           |                           |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_void_p"                | void*                     | "int" or "None"           | "'P'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "py_object"               | PyObject*                 | "object"                  | "'O'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+
| VARIANT_BOOL              | short int                 | "bool"                    | "'v'"                     |
+---------------------------+---------------------------+---------------------------+---------------------------+

Além disso, se a aritmética complexa compatível com IEC 60559 (Anexo
G) for suportada em C e "libffi", os seguintes tipos complexos estarão
disponíveis:

+---------------------------+---------------------------+---------------------------+---------------------------+
| Tipo ctypes               | Tipo em C                 | Tipo em Python            | "_type_"                  |
|===========================|===========================|===========================|===========================|
| "c_float_complex"         | float complex             | "complex"                 | "'Zf'"                    |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_double_complex"        | double complex            | "complex"                 | "'Zd'"                    |
+---------------------------+---------------------------+---------------------------+---------------------------+
| "c_longdouble_complex"    | long double complex       | "complex"                 | "'Zg'"                    |
+---------------------------+---------------------------+---------------------------+---------------------------+

Alterado na versão 3.15: The "_type_" types "F", "D" and "G" have been
replaced with "Zf", "Zd" and "Zg".

Todos esses tipos podem ser criados chamando-os com um inicializador
opcional do tipo e valor corretos:

   >>> c_int()
   c_long(0)
   >>> c_wchar_p("Olá, mundo")
   c_wchar_p(139878537078816)
   >>> c_ushort(-3)
   c_ushort(65533)
   >>>

The constructors for numeric types will convert input using
"__bool__()", "__index__()" (for "int"), "__float__()" or
"__complex__()". This means "c_bool" accepts any object with a truth
value:

   >>> empty_list = []
   >>> c_bool(empty_list)
   c_bool(False)

Como esses tipos são mutáveis, seus valores também podem ser alterados
posteriormente:

   >>> i = c_int(42)
   >>> print(i)
   c_long(42)
   >>> print(i.value)
   42
   >>> i.value = -99
   >>> print(i.value)
   -99
   >>>

Atribuir um novo valor a instâncias dos tipos de ponteiro "c_char_p",
"c_wchar_p" e "c_void_p" altera o *local de memória* para o qual eles
apontam, *não o conteúdo* do bloco de memória (claro que não, porque
objetos string do Python são imutáveis):

   >>> s = "Olá, mundo"
   >>> c_s = c_wchar_p(s)
   >>> print(c_s)
   c_wchar_p(139878542513936)
   >>> print(c_s.value)
   Olá, mundo
   >>> c_s.value = "Opa, beleza?"
   >>> print(c_s)              # o local da memória foi alterado
   c_wchar_p(139878536944240)
   >>> print(c_s.value)
   Opa, beleza?
   >>> print(s)                # primeiro objeto está inalterado
   Olá, mundo
   >>>

No entanto, tome cuidado para não passá-los para funções que esperam
ponteiros para memória mutável. Se precisar de blocos de memória
mutáveis, o ctypes possui uma função "create_string_buffer()" que os
cria de várias maneiras. O conteúdo do bloco de memória atual pode ser
acessado (ou alterado) com a propriedade "raw"; se quiser acessá-lo
como uma string terminada em NUL, use a propriedade "value":

   >>> from ctypes import *
   >>> p = create_string_buffer(3)            # cria um buffer de 3 bytes, inicializado para NUL bytes
   >>> print(sizeof(p), repr(p.raw))
   3 b'\x00\x00\x00'
   >>> p = create_string_buffer(b"Opa")       # cria um buffer contendo uma string terminando com NUL
   >>> print(sizeof(p), repr(p.raw))
   4 b'Opa\x00'
   >>> print(repr(p.value))
   b'Opa'
   >>> p = create_string_buffer(b"Oi", 10)    # cria um buffer de 10 bytes
   >>> print(sizeof(p), repr(p.raw))
   10 b'Oi\x00\x00\x00\x00\x00\x00\x00\x00'
   >>> p.value = b"Oi"
   >>> print(sizeof(p), repr(p.raw))
   10 b'Oi\x00\x00\x00\x00\x00\x00\x00\x00'
   >>>

A função "create_string_buffer()" substitui a antiga função
"c_buffer()" (que ainda está disponível como um apelido). Para criar
um bloco de memória mutável contendo caracteres Unicode do tipo C
"wchar_t", use a função "create_unicode_buffer()".


Chamando funções, continuação
-----------------------------

Observe que printf imprime no canal de saída padrão real, *não* em
"sys.stdout", então esses exemplos só funcionarão no prompt do
console, não de dentro do *IDLE* ou *PythonWin*:

   >>> printf = libc.printf
   >>> printf(b"Hello, %s\n", b"World!")
   Hello, World!
   14
   >>> printf(b"Hello, %S\n", "World!")
   Hello, World!
   14
   >>> printf(b"%d bottles of beer\n", 42)
   42 bottles of beer
   19
   >>> printf(b"%f bottles of beer\n", 42.5)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ctypes.ArgumentError: argument 2: TypeError: Don't know how to convert parameter 2
   >>>

Como mencionado anteriormente, todos os tipos Python, exceto inteiros,
strings e objetos bytes, devem ser encapsulados no seu tipo "ctypes"
correspondente, para que possam ser convertidos para o tipo de dados C
necessário:

   >>> printf(b"An int %d, a double %f\n", 1234, c_double(3.14))
   An int 1234, a double 3.140000
   31
   >>>


Chamando funções variadas
-------------------------

Em muitas plataformas, chamar funções variádicas por meio do ctypes é
exatamente o mesmo que chamar funções com um número fixo de
parâmetros. Em algumas plataformas, em particular no ARM64 para
plataformas Apple, a convenção de chamada para funções variádicas
difere da usada para funções regulares.

Nessas plataformas é necessário especificar o atributo "argtypes" para
os argumentos de funções regulares (não variádicas):

   libc.printf.argtypes = [ctypes.c_char_p]

Já que especificar o atributo não impede a portabilidade, recomenda-se
sempre especificar o "argtypes" para todas as funções variádicas.


Chamando funções com seus próprios tipos de dados personalizados
----------------------------------------------------------------

Você também pode personalizar a conversão de argumentos "ctypes" para
permitir que instâncias de suas próprias classes sejam usadas como
argumentos de função. "ctypes" procura o atributo "_as_parameter_" e o
usa como argumento de função. O atributo deve ser um inteiro, string,
bytes, uma instância "ctypes" ou um objeto com um atributo
"_as_parameter_":

   >>> class Bottles:
   ...     def __init__(self, number):
   ...         self._as_parameter_ = number
   ...
   >>> bottles = Bottles(42)
   >>> printf(b"%d bottles of beer\n", bottles)
   42 bottles of beer
   19
   >>>

If you don't want to store the instance's data in the "_as_parameter_"
instance variable, you could define a "@property" which makes the
attribute available on request.


Especificando os tipos de argumentos necessários (protótipos de função)
-----------------------------------------------------------------------

É possível especificar os tipos de argumentos necessários de funções
exportadas de DLLs definindo o atributo "argtypes".

"argtypes" deve ser uma sequência de tipos de dados C (a função
"printf()" provavelmente não é um bom exemplo nesse caso, pois ela
aceita um número variável e diferentes tipos de parâmetros dependendo
da string de formato; por outro lado, ela é bastante útil para
experimentar esse recurso):

   >>> printf.argtypes = [c_char_p, c_char_p, c_int, c_double]
   >>> printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)
   String 'Hi', Int 10, Double 2.200000
   37
   >>>

Especificar um formato protege contra tipos de argumentos
incompatíveis (assim como um protótipo para uma função em C), e tenta
converter os argumentos para tipos válidos:

   >>> printf(b"%d %d %d", 1, 2, 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ctypes.ArgumentError: argument 2: TypeError: 'int' object cannot be interpreted as ctypes.c_char_p
   >>> printf(b"%s %d %f\n", b"X", 2, 3)
   X 2 3.000000
   13
   >>>

Setting "argtypes" also causes "ctypes" to raise "TypeError" if too
few arguments are passed:

   >>> printf(b"%s %d %f\n", b"X", 2)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: this function takes at least 4 arguments (3 given)

Functions using the "stdcall" calling convention require exactly as
many arguments as there are items in "argtypes". Functions using the
"cdecl" calling convention accept additional arguments, to support
variadic functions. The declaration must match the function's actual
signature; ctypes cannot verify this.

If you have defined your own classes which you pass to function calls,
you have to implement a "from_param()" class method for them to be
able to use them in the "argtypes" sequence. The "from_param()" class
method receives the Python object passed to the function call, it
should do a typecheck or whatever is needed to make sure this object
is acceptable, and then return the object itself, its "_as_parameter_"
attribute, or whatever you want to pass as the C function argument in
this case. Again, the result should be an integer, string, bytes, a
"ctypes" instance, or an object with an "_as_parameter_" attribute.


Tipos de Retorno
----------------

Por padrão, as funções são presumidas como retornando o tipo C int.
Outros retornos podem ser especificados definindo o atributo "restype"
do objeto função.

O protótipo C de "time()" é "time_t time(time_t *)". Porque "time_t"
pode ser de um tipo diferente do tipo de retorno padrão int, você deve
especificar o atributo "restype".

   >>> libc.time.restype = c_time_t

Os tipos de argumentos podem ser especificados usando "argtypes":

   >>> libc.time.argtypes = (POINTER(c_time_t),)

Para chamar uma função com um ponteiro "NULL" como primeiro argumento,
use "None":

   >>> print(libc.time(None))
   1150640792

Aqui está um exemplo mais avançado, ele usa a função "strchr()", que
espera um ponteiro de string e um char, e retorna um ponteiro para uma
string:

   >>> strchr = libc.strchr
   >>> strchr(b"abcdef", ord("d"))
   8059983
   >>> strchr.restype = c_char_p    # c_char_p is a pointer to a string
   >>> strchr(b"abcdef", ord("d"))
   b'def'
   >>> print(strchr(b"abcdef", ord("x")))
   None
   >>>

If you want to avoid the "ord("x")" calls above, you can set the
"argtypes" attribute, and the second argument will be converted from a
single character Python bytes object into a C char:

   >>> strchr.restype = c_char_p
   >>> strchr.argtypes = [c_char_p, c_char]
   >>> strchr(b"abcdef", b"d")
   b'def'
   >>> strchr(b"abcdef", b"def")
   Traceback (most recent call last):
   ctypes.ArgumentError: argument 2: TypeError: one character bytes, bytearray or integer expected
   >>> print(strchr(b"abcdef", b"x"))
   None
   >>> strchr(b"abcdef", b"d")
   b'def'
   >>>

Você também pode usar um objeto Python chamável (uma função ou uma
classe, por exemplo) como o atributo "restype", se a função externa
retornar um inteiro. O objeto chamável será chamado com o *inteiro*
que a função C retorna, e o resultado desta chamada será usado como o
resultado da sua chamada de função. Isso é útil para verificar valores
de retorno de erro e levantar uma exceção automaticamente:

   >>> GetModuleHandle = windll.kernel32.GetModuleHandleA
   >>> def ValidHandle(value):
   ...     if value == 0:
   ...         raise WinError()
   ...     return value
   ...
   >>>
   >>> GetModuleHandle.restype = ValidHandle
   >>> GetModuleHandle(None)
   486539264
   >>> GetModuleHandle("something silly")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 3, in ValidHandle
   OSError: [Errno 126] The specified module could not be found.
   >>>

"WinError" é uma função que chamará a API "FormatMessage()" do Windows
para obter a representação em string de um código de erro, e *retorna*
uma exceção.  "WinError" aceita um parâmetro de código de erro
opcional, se nenhum for usado, ela chama "GetLastError()" para
recuperá-lo.

Por favor, repare que um mecanismo de checagem de erro muito mais
poderoso está disponível através do atributo "errcheck"; consulte o
manual de referência para mais detalhes.


Passando ponteiros (ou: passando parâmetros por referência)
-----------------------------------------------------------

Às vezes, uma função da API C espera um *ponteiro* para um tipo de
dado como parâmetro, provavelmente para escrever no local
correspondente, ou se os dados forem muito grandes para serem passados
por valor. Isso também é conhecido como *passar parâmetros por
referência*.

"ctypes" exports the "byref()" function which is used to pass
parameters by reference.  The same effect can be achieved with the
"pointer()" function, although "pointer()" does a lot more work since
it constructs a real pointer object, so it is faster to use "byref()"
if you don't need the pointer object in Python itself:

   >>> i = c_int()
   >>> f = c_float()
   >>> s = create_string_buffer(b'\000' * 32)
   >>> print(i.value, f.value, repr(s.value))
   0 0.0 b''
   >>> libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
   ...             byref(i), byref(f), s)
   3
   >>> print(i.value, f.value, repr(s.value))
   1 3.1400001049 b'Hello'
   >>>


Estruturas e uniões
-------------------

Structures and unions must derive from the "Structure" and "Union"
base classes which are defined in the "ctypes" module. Each subclass
must define a "_fields_" attribute.  "_fields_" must be a list of
*2-tuples*, containing a *field name* and a *field type*.

The field type must be a "ctypes" type like "c_int", or any other
derived "ctypes" type: structure, union, array, pointer.

Aqui está um exemplo simples de uma estrutura POINT, que contém dois
inteiros nomeados *x* e *y*, e também mostra como inicializar uma
estrutura no construtor:

   >>> from ctypes import *
   >>> class POINT(Structure):
   ...     _fields_ = [("x", c_int),
   ...                 ("y", c_int)]
   ...
   >>> point = POINT(10, 20)
   >>> print(point.x, point.y)
   10 20
   >>> point = POINT(y=5)
   >>> print(point.x, point.y)
   0 5
   >>> POINT(1, 2, 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: too many initializers
   >>>

Você pode, no entanto, construir estruturas muito mais complicadas.
Uma estrutura pode conter outras estruturas, usando uma estrutura como
um tipo de campo.

Aqui está uma estrutura RECT que contém dois POINTs nomeados
*upperleft* e *lowerright*:

   >>> class RECT(Structure):
   ...     _fields_ = [("upperleft", POINT),
   ...                 ("lowerright", POINT)]
   ...
   >>> rc = RECT(point)
   >>> print(rc.upperleft.x, rc.upperleft.y)
   0 5
   >>> print(rc.lowerright.x, rc.lowerright.y)
   0 0
   >>>

Estruturas aninhadas também podem ser inicializadas no construtor de
várias maneiras:

   >>> r = RECT(POINT(1, 2), POINT(3, 4))
   >>> r = RECT((1, 2), (3, 4))

Os *descritor*es de campo podem ser obtidos a partir da *classe*; são
úteis para depuração, pois podem fornecer informações úteis. Veja
"CField":

   >>> POINT.x
   <ctypes.CField 'x' type=c_int, ofs=0, size=4>
   >>> POINT.y
   <ctypes.CField 'y' type=c_int, ofs=4, size=4>
   >>>

Aviso:

  "ctypes" does not support passing unions or structures with bit-
  fields to functions by value.  While this may work on 32-bit x86,
  it's not guaranteed by the library to work in the general case.
  Unions and structures with bit-fields should always be passed to
  functions by pointer.


Layout, alinhamento e ordem de bytes de estrutura/união
-------------------------------------------------------

Por padrão, os campos de Structure e Union são dispostos da mesma
forma que o compilador do C o faz. É possível substituir este
comportamento inteiramente especificando um atributo de classe
"_layout_" na definição da subclasse; veja a documentação do atributo
para detalhes.

É possível especificar o alinhamento máximo para os campos e/ou para a
própria estrutura definindo os atributos de classe "_pack_" e/ou
"_align_" respectivamente. Veja a documentação do atributo para mais
detalhes.

"ctypes" uses the native byte order for Structures and Unions.  To
build structures with non-native byte order, you can use one of the
"BigEndianStructure", "LittleEndianStructure", "BigEndianUnion", and
"LittleEndianUnion" base classes.  These classes cannot contain
pointer fields.


Campos de bit em estruturas e uniões
------------------------------------

É possível criar estruturas e uniões contendo campos de bits. Campos
de bits só são possíveis para campos de inteiros, a largura do bit é
especificada como o terceiro item nas tuplas "_fields_":

   >>> class Int(Structure):
   ...     _fields_ = [("first_16", c_int, 16),
   ...                 ("second_16", c_int, 16)]
   ...
   >>> print(Int.first_16)
   <ctypes.CField 'first_16' type=c_int, ofs=0, bit_size=16, bit_offset=0>
   >>> print(Int.second_16)
   <ctypes.CField 'second_16' type=c_int, ofs=0, bit_size=16, bit_offset=16>

É importante notar que a alocação e o layout de campos de bits na
memória não são definidos como um padrão C; sua implementação é
específica do compilador. Por padrão, o Python tentará corresponder ao
comportamento de um compilador "nativo" para a plataforma atual. Veja
o atributo "_layout_" para detalhes sobre o comportamento padrão e
como alterá-lo.


Vetores
-------

Vetores são sequências que contêm um número fixo de instâncias do
mesmo tipo.

A maneira recomendada de criar tipos vetor é multiplicando um tipo de
dado por um inteiro positivo:

   TenPointsArrayType = POINT * 10

Aqui está um exemplo de um tipo de dado um tanto artificial, uma
estrutura contendo 4 POINTs entre outras coisas:

   >>> from ctypes import *
   >>> class POINT(Structure):
   ...     _fields_ = ("x", c_int), ("y", c_int)
   ...
   >>> class MyStruct(Structure):
   ...     _fields_ = [("a", c_int),
   ...                 ("b", c_float),
   ...                 ("point_array", POINT * 4)]
   >>>
   >>> print(len(MyStruct().point_array))
   4
   >>>

Instâncias são criadas da maneira usual, chamando a classe:

   arr = TenPointsArrayType()
   for pt in arr:
       print(pt.x, pt.y)

O código acima exibe uma série de linhas "0 0", pois o conteúdo do
vetor é inicializado com zeros.

Inicializadores do tipo correto também podem ser especificados:

   >>> from ctypes import *
   >>> TenIntegers = c_int * 10
   >>> ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
   >>> print(ii)
   <c_long_Array_10 object at 0x...>
   >>> for i in ii: print(i, end=" ")
   ...
   1 2 3 4 5 6 7 8 9 10
   >>>


Ponteiros
---------

Pointer instances are created by calling the "pointer()" function on a
"ctypes" type:

   >>> from ctypes import *
   >>> i = c_int(42)
   >>> pi = pointer(i)
   >>>

Instâncias de ponteiros têm um atributo "contents" que retorna o
objeto para qual o ponteiro aponta, o objeto "i" acima:

   >>> pi.contents
   c_long(42)
   >>>

Note that "ctypes" does not have OOR (original object return), it
constructs a new, equivalent object each time you retrieve an
attribute:

   >>> pi.contents is i
   False
   >>> pi.contents is pi.contents
   False
   >>>

Atribuir outra instância "c_int" ao atributo do conteúdo do ponteiro
faria com que o ponteiro apontasse para o local de memória onde ela
está armazenada:

   >>> i = c_int(99)
   >>> pi.contents = i
   >>> pi.contents
   c_long(99)
   >>>

Instâncias de ponteiro também podem ser indexadas com inteiros:

   >>> pi[0]
   99
   >>>

Atribuir a um índice inteiro altera o valor apontado:

   >>> print(i)
   c_long(99)
   >>> pi[0] = 22
   >>> print(i)
   c_long(22)
   >>>

Também é possível usar índices diferentes de 0, mas você deve saber o
que está fazendo, assim como em C: Você pode acessar ou alterar locais
arbitrários da memória. Geralmente, você só usa este recurso se
receber um ponteiro de uma função C, e você *sabe* que o ponteiro na
verdade aponta para um vetor em vez de um único item.

Aviso:

  Because pointer objects support subscription, they implicitly
  support *iteration*. Unless doing this in a controlled manner, such
  as by manually calling "next()" on a "pointer()" iterator, this will
  typically lead to infinite loops or crashes, because ctypes has no
  way of knowing when to stop iteration. In other words, a "pointer"
  iterator will infinitely yield arbitrary memory.

Behind the scenes, the "pointer()" function does more than simply
create pointer instances, it has to create pointer *types* first. This
is done with the "POINTER()" function, which accepts any "ctypes"
type, and returns a new type:

   >>> PI = POINTER(c_int)
   >>> PI
   <class 'ctypes.LP_c_long'>
   >>> PI(42)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: expected c_long instead of int
   >>> PI(c_int(42))
   <ctypes.LP_c_long object at 0x...>
   >>>

Chamar o tipo ponteiro sem um argumento cria um ponteiro "NULL".
Ponteiros "NULL" possuem o valor booleano "False":

   >>> null_ptr = POINTER(c_int)()
   >>> print(bool(null_ptr))
   False
   >>>

"ctypes" checks for "NULL" when dereferencing pointers (but
dereferencing invalid non-"NULL" pointers would crash Python):

   >>> null_ptr[0]
   Traceback (most recent call last):
       ....
   ValueError: NULL pointer access
   >>>

   >>> null_ptr[0] = 1234
   Traceback (most recent call last):
       ....
   ValueError: NULL pointer access
   >>>


Segurança de thread (Thread safety) sem o GIL
---------------------------------------------

From Python 3.13 onward, the *GIL* can be disabled on the *free-
threaded build*. In ctypes, reads and writes to a single object
concurrently is safe, but not across multiple objects:

      >>> number = c_int(42)
      >>> pointer_a = pointer(number)
      >>> pointer_b = pointer(number)

No exemplo acima, é seguro apenas para um objeto ler e escrever no
endereço simultaneamente se o GIL estiver desabilitado. Portanto,
"pointer_a" pode ser compartilhado e escrito entre múltiplas threads,
mas apenas se "pointer_b" não estiver também tentando fazer o mesmo.
Se isso for um problema, considere usar um "threading.Lock" para
sincronizar o acesso à memória:

      >>> import threading
      >>> lock = threading.Lock()
      >>> # Thread 1
      >>> with lock:
      ...    pointer_a.contents = 24
      >>> # Thread 2
      >>> with lock:
      ...    pointer_b.contents = 42


Conversão de Tipos
------------------

Normalmente, o ctypes faz uma verificação de tipos estrita. Isso
significa que, se você tiver "POINTER(c_int)" na lista "argtypes" de
uma função ou como o tipo de um campo membro em uma definição de
estrutura, apenas instâncias de exatamente o mesmo tipo são aceitas.
Existem algumas exceções a esta regra, onde o ctypes aceita outros
objetos. Por exemplo, você pode passar instâncias de vetor compatíveis
em vez de tipos de ponteiro. Assim, para "POINTER(c_int)", o ctypes
aceita um vetor de c_int:

   >>> class Bar(Structure):
   ...     _fields_ = [("count", c_int), ("values", POINTER(c_int))]
   ...
   >>> bar = Bar()
   >>> bar.values = (c_int * 3)(1, 2, 3)
   >>> bar.count = 3
   >>> for i in range(bar.count):
   ...     print(bar.values[i])
   ...
   1
   2
   3
   >>>

Além disso, se um argumento de função for explicitamente declarado
como um tipo ponteiro (como "POINTER(c_int)") em "argtypes", um objeto
do tipo apontado ("c_int" neste caso) pode ser passado para a função.
O ctypes aplicará a conversão "byref()" necessária neste caso
automaticamente.

Para definir um campo do tipo PONTEIRO como "NULL", você pode atribuir
"None":

   >>> bar.values = None
   >>>

Sometimes you have instances of incompatible types.  In C, you can
cast one type into another type.  "ctypes" provides a "cast()"
function which can be used in the same way.  The "Bar" structure
defined above accepts "POINTER(c_int)" pointers or "c_int" arrays for
its "values" field, but not instances of other types:

   >>> bar.values = (c_byte * 4)()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: incompatible types, c_byte_Array_4 instance instead of LP_c_long instance
   >>>

Para esses casos, a função "cast()" é útil.

A função "cast()" pode ser usada para converter uma instância ctypes
em um ponteiro para um diferente tipo de dado ctypes. "cast()" recebe
dois parâmetros, um objeto ctypes que é ou pode ser convertido para um
ponteiro de algum tipo, e um tipo ponteiro ctypes. Ela retorna uma
instância do segundo argumento, que referencia o mesmo bloco de
memória que o primeiro argumento:

   >>> a = (c_byte * 4)()
   >>> cast(a, POINTER(c_int))
   <ctypes.LP_c_long object at ...>
   >>>

Então, "cast()" pode ser usada para atribuir ao campo "values" da
estrutura "Bar":

   >>> bar = Bar()
   >>> bar.values = cast((c_byte * 4)(), POINTER(c_int))
   >>> print(bar.values[0])
   0
   >>>


Tipos Incompletos
-----------------

*Tipos Incompletos* são estruturas, uniões ou vetores, cujos membros
ainda não foram especificados. Em C, eles são especificados por
declarações antecipadas, que são definidas posteriormente:

   struct cell; /* forward declaration */

   struct cell {
       char *name;
       struct cell *next;
   };

A tradução direta para código ctypes seria esta, mas não funciona:

   >>> class cell(Structure):
   ...     _fields_ = [("name", c_char_p),
   ...                 ("next", POINTER(cell))]
   ...
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 2, in cell
   NameError: name 'cell' is not defined
   >>>

because the new "class cell" is not available in the class statement
itself. In "ctypes", we can define the "cell" class and set the
"_fields_" attribute later, after the class statement:

   >>> from ctypes import *
   >>> class cell(Structure):
   ...     pass
   ...
   >>> cell._fields_ = [("name", c_char_p),
   ...                  ("next", POINTER(cell))]
   >>>

Vamos tentar. Criamos duas instâncias de "cell", e deixamos que elas
apontem uma para a outra, e finalmente seguimos a cadeia de ponteiros
algumas vezes:

   >>> c1 = cell()
   >>> c1.name = b"foo"
   >>> c2 = cell()
   >>> c2.name = b"bar"
   >>> c1.next = pointer(c2)
   >>> c2.next = pointer(c1)
   >>> p = c1
   >>> for i in range(8):
   ...     print(p.name, end=" ")
   ...     p = p.next[0]
   ...
   foo bar foo bar foo bar foo bar
   >>>


Funções Callbacks
-----------------

"ctypes" allows creating C callable function pointers from Python
callables. These are sometimes called *callback functions*.

Primeiro, você deve criar uma classe para função de retorno. A classe
sabe a convenção de chamada , o tipo de retorno, e o número e tipos de
argumentos que essa função irá receber.

A função de fábrica "CFUNCTYPE()" cria tipos para funções de retorno
usando a convenção de chamada "cdecl". No Windows, a função de fábrica
"WINFUNCTYPE()" cria tipos para funções de retorno usando a convenção
de chamada "stdcall".

Ambas estas funções de fábrica são chamadas com o tipo de resultado
como primeiro argumento, e os tipos de argumento esperados da função
de retorno como os argumentos restantes.

I will present an example here which uses the standard C library's
"qsort()" function, that is used to sort items with the help of a
callback function.  "qsort()" will be used to sort an array of
integers:

   >>> IntArray5 = c_int * 5
   >>> ia = IntArray5(5, 1, 7, 33, 99)
   >>> qsort = libc.qsort
   >>> qsort.restype = None
   >>>

A "qsort()" deve ser chamada com um ponteiro para os dados a serem
ordenados, o número de itens no vetor de dados, o tamanho de um item,
e um ponteiro para a função de comparação, a função de retorno
(callback). A função de retorno será então chamada com dois ponteiros
para itens, e ela deve retornar um inteiro negativo se o primeiro item
for menor que o segundo, um zero se eles forem iguais, e um inteiro
positivo caso contrário.

Então, nossa função de retorno (callback function) recebe ponteiros
para inteiros, e deve retornar um inteiro. Primeiro criamos o "type"
para a função de retorno:

   >>> CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
   >>>

Para começar, aqui está uma função de retorno (callback) simples que
mostra os valores que lhe são passados:

   >>> def py_cmp_func(a, b):
   ...     print("py_cmp_func", a[0], b[0])
   ...     return 0
   ...
   >>> cmp_func = CMPFUNC(py_cmp_func)
   >>>

O resultado:

   >>> qsort(ia, len(ia), sizeof(c_int), cmp_func)
   py_cmp_func 5 1
   py_cmp_func 33 99
   py_cmp_func 7 33
   py_cmp_func 5 7
   py_cmp_func 1 7
   >>>

Agora podemos realmente comparar os dois itens e retornar um resultado
útil:

   >>> def py_cmp_func(a, b):
   ...     print("py_cmp_func", a[0], b[0])
   ...     return a[0] - b[0]
   ...
   >>>
   >>> qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func))
   py_cmp_func 5 1
   py_cmp_func 33 99
   py_cmp_func 7 33
   py_cmp_func 1 7
   py_cmp_func 5 7
   >>>

Como podemos verificar facilmente, nosso vetor está ordenado agora:

   >>> for i in ia: print(i, end=" ")
   ...
   1 5 7 33 99
   >>>

As fábricas de funções podem ser usadas como fábricas de decoradores,
então também podemos escrever:

   >>> @CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
   ... def py_cmp_func(a, b):
   ...     print("py_cmp_func", a[0], b[0])
   ...     return a[0] - b[0]
   ...
   >>> qsort(ia, len(ia), sizeof(c_int), py_cmp_func)
   py_cmp_func 5 1
   py_cmp_func 33 99
   py_cmp_func 7 33
   py_cmp_func 1 7
   py_cmp_func 5 7
   >>>

Nota:

  Make sure you keep references to "CFUNCTYPE()" objects as long as
  they are used from C code. "ctypes" doesn't, and if you don't, they
  may be garbage collected, crashing your program when a callback is
  made.Além disso, note que se a função de retorno for chamada em uma
  thread criada fora do controle do Python (por exemplo, pelo código
  externo que chama a função de retorno), o ctypes cria uma nova
  thread Python "dummy" (fictícia) em cada invocação. Este
  comportamento é correto para a maioria dos propósitos, mas significa
  que os valores armazenados com "threading.local" *não* sobreviverão
  entre diferentes funções de retorno, mesmo quando essas chamadas são
  feitas a partir da mesma thread C.


Acessando valores exportados de dlls
------------------------------------

Algumas bibliotecas compartilhadas não exportam apenas funções, elas
também exportam variáveis. Um exemplo na própria biblioteca Python é a
"Py_Version", o número da versão de tempo de execução do Python
codificado em um único inteiro constante.

"ctypes" can access values like this with the "in_dll()" class methods
of the type.  *pythonapi* is a predefined symbol giving access to the
Python C api:

   >>> version = ctypes.c_int.in_dll(ctypes.pythonapi, "Py_Version")
   >>> print(hex(version.value))
   0x30c00a0

Um exemplo estendido que também demonstra o uso de ponteiros acessa o
ponteiro "PyImport_FrozenModules" exportado pelo Python.

Citando a documentação para esse valor:

   Este ponteiro é inicializado para apontar para um vetor de
   registros de "_frozen", terminado por um cujos membros são todos
   "NULL" ou zero. Quando um módulo congelado é importado, ele é
   pesquisado nesta tabela. O código de terceiros pode fazer truques
   com isso para fornecer uma coleção criada dinamicamente de módulos
   congelados.

So manipulating this pointer could even prove useful. To restrict the
example size, we show only how this table can be read with "ctypes":

   >>> from ctypes import *
   >>>
   >>> class struct_frozen(Structure):
   ...     _fields_ = [("name", c_char_p),
   ...                 ("code", POINTER(c_ubyte)),
   ...                 ("size", c_int),
   ...                 ("get_code", POINTER(c_ubyte)),  # Function pointer
   ...                ]
   ...
   >>>

Nós definimos tipo de dado "_frozen", para que possamos obter o
ponteiro para a tabela:

   >>> FrozenTable = POINTER(struct_frozen)
   >>> table = FrozenTable.in_dll(pythonapi, "_PyImport_FrozenBootstrap")
   >>>

Como "table" é um "pointer" para o vetor de registros "struct_frozen",
nós podemos iterar sobre ele, mas só temos que nos certificar de que
nosso loop termine, porque ponteiros não têm tamanho. Cedo ou tarde,
ele provavelmente travaria com uma violação de acesso ou algo assim,
então é melhor sair do loop quando atingirmos a entrada "NULL":

   >>> for item in table:
   ...     if item.name is None:
   ...         break
   ...     print(item.name.decode("ascii"), item.size)
   ...
   _frozen_importlib 31764
   _frozen_importlib_external 41499
   zipimport 12345
   >>>

O fato de que o Python padrão tem um módulo congelado e um pacote
congelado (indicado pelo membro "size" negativo) não é bem conhecido,
é usado apenas para testes. Experimente com "import __hello__" por
exemplo.


Surpresas
---------

There are some edges in "ctypes" where you might expect something
other than what actually happens.

Considere o exemplo a seguir:

   >>> from ctypes import *
   >>> class POINT(Structure):
   ...     _fields_ = ("x", c_int), ("y", c_int)
   ...
   >>> class RECT(Structure):
   ...     _fields_ = ("a", POINT), ("b", POINT)
   ...
   >>> p1 = POINT(1, 2)
   >>> p2 = POINT(3, 4)
   >>> rc = RECT(p1, p2)
   >>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
   1 2 3 4
   >>> # now swap the two points
   >>> rc.a, rc.b = rc.b, rc.a
   >>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
   3 4 3 4
   >>>

Hm. Nós com certeza esperávamos que a última instrução exibisse "3 4 1
2". O que aconteceu? Aqui estão os passos da linha "rc.a, rc.b = rc.b,
rc.a" acima:

   >>> temp0, temp1 = rc.b, rc.a
   >>> rc.a = temp0
   >>> rc.b = temp1
   >>>

Observe que "temp0" e "temp1" ainda são objetos que utilizam o buffer
interno do objeto "rc" acima. Portanto, executar "rc.a = temp0" copia
o conteúdo do buffer de "temp0" para o buffer de "rc". Isso, por sua
vez, altera o conteúdo de "temp1". Assim, a última atribuição "rc.b =
temp1" não produz o efeito esperado.

Tenha em mente que obter sub-objetos de estruturas, uniões e vetores
não copia o sub-objeto; em vez disso, recupera um objeto de
encapsulamento (wrapper) que acessa o buffer subjacente do objeto
raiz.

Outro exemplo que pode se comportar de maneira diferente do que alguém
poderia esperar é o seguinte:

   >>> s = c_char_p()
   >>> s.value = b"abc def ghi"
   >>> s.value
   b'abc def ghi'
   >>> s.value is s.value
   False
   >>>

Nota:

  Objetos instanciados a partir de "c_char_p" só podem ter seu valor
  definido para bytes ou inteiros.

Por que está imprimindo "False"? Instâncias de ctypes são objetos que
contêm um bloco de memória, além de alguns *descriptor*s que acessam o
conteúdo dessa memória. Armazenar um objeto Python no bloco de memória
não armazena o próprio objeto; em vez disso, armazena-se o seu
atributo "contents". Acessar o contents novamente constrói um novo
objeto Python a cada vez!


Tipos de dados de tamanho variável
----------------------------------

"ctypes" provides some support for variable-sized arrays and
structures.

A função "resize()" pode ser usada para redimensionar o buffer de
memória de um objeto ctypes existente. A função recebe o objeto como
primeiro argumento, e o tamanho solicitado em bytes como o segundo
argumento. O bloco de memória não pode ser tornado menor do que o
bloco de memória natural especificado pelo tipo do objeto, um
"ValueError" é levantado se isso for tentado:

   >>> short_array = (c_short * 4)()
   >>> print(sizeof(short_array))
   8
   >>> resize(short_array, 4)
   Traceback (most recent call last):
       ...
   ValueError: minimum size is 8
   >>> resize(short_array, 32)
   >>> sizeof(short_array)
   32
   >>> sizeof(type(short_array))
   8
   >>>

Isso é bom e funcional, mas como alguém acessaria os elementos
contidos neste vetor? Já que o tipo ainda sabe apenas sobre 4
elementos, obtemos erros ao acessar outros elementos:

   >>> short_array[:]
   [0, 0, 0, 0]
   >>> short_array[7]
   Traceback (most recent call last):
       ...
   IndexError: invalid index
   >>>

Another way to use variable-sized data types with "ctypes" is to use
the dynamic nature of Python, and (re-)define the data type after the
required size is already known, on a case by case basis.


Referência ctypes
=================


Loading shared libraries
------------------------

There are several ways to load shared libraries into the Python
process.  One way is to instantiate "CDLL" or one of its subclasses:

class ctypes.CDLL(name, mode=DEFAULT_MODE, handle=None, use_errno=False, use_last_error=False, winmode=None)

   Represents a loaded shared library.

   Functions in this library use the standard C calling convention,
   and are assumed to return int. The Python *global interpreter lock*
   is released before calling any function exported by these
   libraries, and reacquired afterwards. For different function
   behavior, use a subclass: "OleDLL", "WinDLL", or "PyDLL".

   If you have an existing "handle" to an already loaded shared
   library, it can be passed as the *handle* argument to wrap the
   opened library in a new "CDLL" object. In this case, *name* is only
   used to set the "_name" attribute, but it may be adjusted and/or
   validated.

   If *handle* is "None", the underlying platform's *dlopen(3)* or
   LoadLibraryExW function is used to load the library into the
   process, and to get a handle to it.

   *name* is the pathname of the shared library to open. If *name*
   does not contain a path separator, the library is found in a
   platform-specific way.

   On Windows, the ".DLL" suffix may be missing. (For details, see
   LoadLibraryExW documentation.) Other platform-specific prefixes and
   suffixes (for example, "lib", ".so", ".dylib", or version numbers)
   must be present in *name*; they are not added automatically. See
   Encontrando bibliotecas compartilhadas for more information.

   On non-Windows systems, *name* can  be "None". In this case,
   "dlopen()" is called with "NULL", which opens the main program as a
   "library". (Some systems do the same if *name* is empty;
   "None"/"NULL" is more portable.)

   Detalhes da implementação do CPython:: Since CPython is linked to
   "libc", a "None" *name* is often used to access the C standard
   library:

      >>> printf = ctypes.CDLL(None).printf
      >>> printf.argtypes = [ctypes.c_char_p]
      >>> printf(b"hello\n")
      hello
      6

   To access the Python C API, prefer "ctypes.pythonapi" which works
   across platforms.

   O parâmetro *mode* pode ser utilizado para especificar como a
   biblioteca é carregada. Para detalhes, consulte a página de manual
   *dlopen(3)*. No Windows, *mode* é ignorado. Em sistemas posix,
   RTLD_NOW é sempre adicionado e, não é configurável.

   The *use_errno* parameter, when set to true, enables a ctypes
   mechanism that allows accessing the system "errno" error number in
   a safe way. "ctypes" maintains a thread-local copy of the system's
   "errno" variable; if you call foreign functions created with
   "use_errno=True" then the "errno" value before the function call is
   swapped with the ctypes private copy, the same happens immediately
   after the function call. This mechanism only works for libraries
   that use the same C runtime library as the interpreter itself. A
   library linked against a different C runtime (for example, a
   different CRT on Windows) has its own "errno", which "ctypes"
   cannot observe.

   The function "ctypes.get_errno()" returns the value of the ctypes
   private copy, and the function "ctypes.set_errno()" changes the
   ctypes private copy to a new value and returns the former value.

   The *use_last_error* parameter, when set to true, enables the same
   mechanism for the Windows error code which is managed by the
   "GetLastError()" and "SetLastError()" Windows API functions;
   "ctypes.get_last_error()" and "ctypes.set_last_error()" are used to
   request and change the ctypes private copy of the windows error
   code.

   The *winmode* parameter is used on Windows to specify how the
   library is loaded (since *mode* is ignored). It takes any value
   that is valid for the Win32 API LoadLibraryExW flags parameter.
   When omitted, the default is to use the flags that result in the
   most secure DLL load, which avoids issues such as DLL hijacking.
   Passing the full path to the DLL is the safest way to ensure the
   correct library and dependencies are loaded.

   On Windows creating a "CDLL" instance may fail even if the DLL name
   exists. When a dependent DLL of the loaded DLL is not found, a
   "OSError" error is raised with the message *"[WinError 126] The
   specified module could not be found".* This error message does not
   contain the name of the missing DLL because the Windows API does
   not return this information making this error hard to diagnose. To
   resolve this error and determine which DLL is not found, you need
   to find the list of dependent DLLs and determine which one is not
   found using Windows debugging and tracing tools.

   Ver também:

     Microsoft DUMPBIN tool -- A tool to find DLL dependents.

   Alterado na versão 3.8: Added *winmode* parameter.

   Alterado na versão 3.12: The *name* parameter can now be a *path-
   like object*.

   Instances of this class have no public methods.  Functions exported
   by the shared library can be accessed as attributes or by index.
   Please note that accessing the function through an attribute caches
   the result and therefore accessing it repeatedly returns the same
   object each time.  On the other hand, accessing it through an index
   returns a new object each time:

      >>> from ctypes import CDLL
      >>> libc = CDLL("libc.so.6")  # On Linux
      >>> libc.time == libc.time
      True
      >>> libc['time'] == libc['time']
      False

   The following public attributes are available. Their name starts
   with an underscore to not clash with exported function names:

   _handle

      The system handle used to access the library.

   _name

      The name of the library passed in the constructor.

class ctypes.OleDLL

   See "CDLL", the superclass, for common information.

   Functions in this library use the "stdcall" calling convention, and
   are assumed to return the windows specific "HRESULT" code.
   "HRESULT" values contain information specifying whether the
   function call failed or succeeded, together with additional error
   code.  If the return value signals a failure, an "OSError" is
   automatically raised.

   Disponibilidade: Windows

   Alterado na versão 3.3: Costumava-se levantar "WindowsError", que
   agora é um apelido de "OSError".

class ctypes.WinDLL

   See "CDLL", the superclass, for common information.

   Functions in these libraries use the "stdcall" calling convention,
   and are assumed to return int by default.

   Disponibilidade: Windows

class ctypes.PyDLL

   See "CDLL", the superclass, for common information.

   When functions in this library are called, the Python GIL is *not*
   released during the function call, and after the function execution
   the Python error flag is checked. If the error flag is set, a
   Python exception is raised.

   Thus, this is only useful to call Python C API functions directly.

ctypes.RTLD_GLOBAL

   Flag to use as *mode* parameter.  On platforms where this flag is
   not available, it is defined as the integer zero.

ctypes.RTLD_LOCAL

   Flag to use as *mode* parameter.  On platforms where this is not
   available, it is the same as *RTLD_GLOBAL*.

ctypes.DEFAULT_MODE

   The default mode which is used to load shared libraries.  On OSX
   10.3, this is *RTLD_GLOBAL*, otherwise it is the same as
   *RTLD_LOCAL*.

Shared libraries can also be loaded by using one of the prefabricated
objects, which are instances of the "LibraryLoader" class, either by
calling the "LoadLibrary()" method, or by retrieving the library as
attribute of the loader instance.

class ctypes.LibraryLoader(dlltype)

   Class which loads shared libraries.  *dlltype* should be one of the
   "CDLL", "PyDLL", "WinDLL", or "OleDLL" types.

   "__getattr__()" has special behavior: It allows loading a shared
   library by accessing it as attribute of a library loader instance.
   The result is cached, so repeated attribute accesses return the
   same library each time.

   LoadLibrary(name)

      Load a shared library into the process and return it.  This
      method always returns a new instance of the library.

These prefabricated library loaders are available:

   ctypes.cdll

      Creates "CDLL" instances.

   ctypes.windll

      Creates "WinDLL" instances.

      Disponibilidade: Windows

   ctypes.oledll

      Creates "OleDLL" instances.

      Disponibilidade: Windows

   ctypes.pydll

      Creates "PyDLL" instances.

   ctypes.pythonapi

      An instance of "PyDLL" that exposes Python C API functions as
      attributes.  Note that all these functions are assumed to return
      C int, which is of course not always the truth, so you have to
      assign the correct "restype" attribute to use these functions.

      Nota:

        If the Python interpreter is statically linked, this may be
        "None".

Carregar uma biblioteca através de qualquer um desses objetos levanta
um evento de auditoria "ctypes.dlopen" com o argumento string "name",
o nome usado para carregar a biblioteca.

Accessing a function on a loaded library raises an auditing event
"ctypes.dlsym" with arguments "library" (the library object) and
"name" (the symbol's name as a string or integer).

In cases when only the library handle is available rather than the
object, accessing a function raises an auditing event
"ctypes.dlsym/handle" with arguments "handle" (the raw library handle)
and "name".


Encontrando bibliotecas compartilhadas
--------------------------------------

When programming in a compiled language, shared libraries are accessed
when compiling/linking a program, and when the program is run. The
programmer specifies a short name; the C compiler, linker, and runtime
dynamic library loader then interact in system-specific ways to find
the filename of the library to load.

While the mapping from short names to filenames is not consistently
exposed by platforms, the "ctypes.util" module provides a function,
"find_library()", that attempts to match it. However, as backwards
compatibility concerns make it difficult to adjust its behavior for
new platforms and configurations, the function is *soft deprecated*.

If wrapping a shared library with "ctypes", consider determining the
shared library name at development time, and hardcoding it into the
wrapper module instead of using "find_library()" to locate the library
at runtime. Also consider adding a configuration option or environment
variable to let users select a library to use, and then perhaps use
"find_library()" as a default or fallback.

ctypes.util.find_library(name)

   Try to find a library and return a pathname.

   *name* is the "short" library name without any prefix like "lib",
   suffix like ".so", ".dylib" or version number. (This is the form
   used for the posix linker option "-l".) The result is in a format
   suitable for passing to "CDLL".

   If no library can be found, return "None".

   The exact functionality is system dependent, and is *not
   guaranteed* to match the behavior of the compiler, linker, and
   loader used for (or by) Python. It is recommended to only use this
   function as a default or fallback,

   Suavemente descontinuado desde a versão 3.15: This function is kept
   for use in cases where it works, but not expected to be updated for
   additional platforms and configurations.

On Linux, "find_library()" tries to run external programs
("/sbin/ldconfig", "gcc", "objdump" and "ld") to find the library
file. If the output of these programs does not correspond to the
dynamic linker used by Python, the result of this function may be
misleading.

Alterado na versão 3.6: On Linux, the value of the environment
variable "LD_LIBRARY_PATH" is used when searching for libraries, if a
library cannot be found by any other means.

Veja alguns exemplos:

   >>> from ctypes.util import find_library
   >>> find_library("m")
   'libm.so.6'
   >>> find_library("c")
   'libc.so.6'
   >>> find_library("bz2")
   'libbz2.so.1.0'
   >>>

On macOS and Android, "find_library()" uses the system's standard
naming schemes and paths to locate the library, and returns a full
pathname if successful:

   >>> from ctypes.util import find_library
   >>> find_library("c")
   '/usr/lib/libc.dylib'
   >>> find_library("m")
   '/usr/lib/libm.dylib'
   >>> find_library("bz2")
   '/usr/lib/libbz2.dylib'
   >>> find_library("AGL")
   '/System/Library/Frameworks/AGL.framework/AGL'
   >>>

On Windows, "find_library()" searches along the system search path,
and returns the full pathname, but since there is no predefined naming
scheme a call like "find_library("c")" will fail and return "None".

ctypes.util.find_msvcrt()

   Returns the filename of the VC runtime library used by Python, and
   by the extension modules.

   If the name of the library cannot be determined, "None" is
   returned. Notably, this will happen for recent versions of the VC
   runtime library, which are not directly loadable.

   If you need to free memory, for example, allocated by an extension
   module with a call to the "free(void *)", it is important that you
   use the function in the same library that allocated the memory.

   Disponibilidade: Windows


Listing loaded shared libraries
-------------------------------

When writing code that relies on code loaded from shared libraries, it
can be useful to know which shared libraries have already been loaded
into the current process.

The "ctypes.util" module provides the "dllist()" function, which calls
the different APIs provided by the various platforms to help determine
which shared libraries have already been loaded into the current
process.

The exact output of this function will be system dependent. On most
platforms, the first entry of this list represents the current process
itself, which may be an empty string. For example, on glibc-based
Linux, the return may look like:

   >>> from ctypes.util import dllist
   >>> dllist()
   ['', 'linux-vdso.so.1', '/lib/x86_64-linux-gnu/libm.so.6', '/lib/x86_64-linux-gnu/libc.so.6', ... ]


Foreign functions
-----------------

As explained in the previous section, foreign functions can be
accessed as attributes of loaded shared libraries.  The function
objects created in this way by default accept any number of arguments,
accept any ctypes data instances as arguments, and return the default
result type specified by the library loader.

They are instances of a private local class "_FuncPtr" (not exposed in
"ctypes") which inherits from the private "_CFuncPtr" class:

   >>> import ctypes
   >>> lib = ctypes.CDLL(None)
   >>> issubclass(lib._FuncPtr, ctypes._CFuncPtr)
   True
   >>> lib._FuncPtr is ctypes._CFuncPtr
   False

class ctypes._CFuncPtr

   Base class for C callable foreign functions.

   Instances of foreign functions are also C compatible data types;
   they represent C function pointers.

   This behavior can be customized by assigning to special attributes
   of the foreign function object.

   restype

      Assign a ctypes type to specify the result type of the foreign
      function. Use "None" for void, a function not returning
      anything.

      It is possible to assign a callable Python object that is not a
      ctypes type, in this case the function is assumed to return a C
      int, and the callable will be called with this integer, allowing
      further processing or error checking.  Using this is deprecated,
      for more flexible post processing or error checking use a ctypes
      data type as "restype" and assign a callable to the "errcheck"
      attribute.

   argtypes

      Assign a tuple of ctypes types to specify the argument types
      that the function accepts. "TypeError" is raised if the function
      is called with fewer arguments than the length of this tuple.
      Functions using the "stdcall" calling convention also raise
      "TypeError" if called with more arguments; functions using the
      "cdecl" calling convention accept additional, unspecified
      arguments as well.

      When a foreign function is called, each actual argument is
      passed to the "from_param()" class method of the items in the
      "argtypes" tuple, this method allows adapting the actual
      argument to an object that the foreign function accepts.  For
      example, a "c_char_p" item in the "argtypes" tuple will convert
      a string passed as argument into a bytes object using ctypes
      conversion rules.

      New: It is now possible to put items in argtypes which are not
      ctypes types, but each item must have a "from_param()" method
      which returns a value usable as argument (integer, string,
      ctypes instance).  This allows defining adapters that can adapt
      custom objects as function parameters.

   errcheck

      Assign a Python function or another callable to this attribute.
      The callable will be called with three or more arguments:

      callable(result, func, arguments)

         *result* is what the foreign function returns, as specified
         by the "restype" attribute.

         *func* is the foreign function object itself, this allows
         reusing the same callable object to check or post process the
         results of several functions.

         *arguments* is a tuple containing the parameters passed to
         the function call, including any output parameters that
         "ctypes" created for the call; this allows specializing the
         behavior on the arguments used.

      If the callable returns the *arguments* tuple it received,
      unchanged, "ctypes" continues its normal processing of the
      result, which includes returning output parameters (see Function
      prototypes). Any other object returned by the callable is
      returned from the foreign function call instead. The callable
      can also check the result value and raise an exception if the
      foreign function call failed.

      For example, this callable raises an exception when the foreign
      function signals failure with a negative return value, and
      otherwise leaves the result to "ctypes":

         def errcheck(result, func, arguments):
             if result < 0:
                 raise RuntimeError(f"call failed with error {result}")
             return arguments

      This one instead replaces the result, converting a C "int" used
      as a boolean into a "bool":

         def errcheck(result, func, arguments):
             return result != 0

On Windows, when a foreign function call raises a system exception
(for example, due to an access violation), it will be captured and
replaced with a suitable Python exception. Further, an auditing event
"ctypes.set_exception" with argument "code" will be raised, allowing
an audit hook to replace the exception with its own.

Some ways to invoke foreign function calls as well as some of the
functions in this module may raise an auditing event
"ctypes.call_function" with arguments "function pointer" and
"arguments".


Function prototypes
-------------------

Foreign functions can also be created by instantiating function
prototypes. Function prototypes are similar to function prototypes in
C; they describe a function (return type, argument types, calling
convention) without defining an implementation.  The factory functions
must be called with the desired result type and the argument types of
the function, and can be used as decorator factories, and as such, be
applied to functions through the "@wrapper" syntax. See Funções
Callbacks for examples.

ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

   The returned function prototype creates functions that use the
   standard C calling convention.  The function will release the GIL
   during the call.  If *use_errno* is set to true, the ctypes private
   copy of the system "errno" variable is exchanged with the real
   "errno" value before and after the call; *use_last_error* does the
   same for the Windows error code.

ctypes.WINFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

   The returned function prototype creates functions that use the
   "stdcall" calling convention.  The function will release the GIL
   during the call.  *use_errno* and *use_last_error* have the same
   meaning as above.

   Disponibilidade: Windows

ctypes.PYFUNCTYPE(restype, *argtypes)

   The returned function prototype creates functions that use the
   Python calling convention.  Unlike "CFUNCTYPE()" and
   "WINFUNCTYPE()", ctypes does *not* release the GIL before calling
   the foreign function, so the function may safely use the Python C
   API. Note that this does not prevent the GIL from being released
   *during* the call.

Function prototypes created by these factory functions can be
instantiated in different ways, depending on the type and number of
the parameters in the call:

prototype(address)

   Returns a foreign function at the specified address which must be
   an integer.

prototype(callable)

   Create a C callable function (a callback function) from a Python
   *callable*.

prototype(func_spec[, paramflags])

   Returns a foreign function exported by a shared library.
   *func_spec* must be a 2-tuple "(name_or_ordinal, library)". The
   first item is the name of the exported function as string, or the
   ordinal of the exported function as small integer.  The second item
   is the shared library instance.

prototype(vtbl_index, name[, paramflags[, iid]])

   Returns a foreign function that will call a COM method.
   *vtbl_index* is the index into the virtual function table, a small
   non-negative integer. *name* is name of the COM method. *iid* is an
   optional pointer to the interface identifier which is used in
   extended error reporting.

   If *iid* is not specified, an "OSError" is raised if the COM method
   call fails. If *iid* is specified, a "COMError" is raised instead.

   COM methods use a special calling convention: They require a
   pointer to the COM interface as first argument, in addition to
   those parameters that are specified in the "argtypes" tuple.

   Disponibilidade: Windows

The optional *paramflags* parameter creates foreign function wrappers
with much more functionality than the features described above.

*paramflags* must be a tuple of the same length as "argtypes".

Each item in this tuple contains further information about a
parameter, it must be a tuple containing one, two, or three items.

The first item is an integer containing a combination of direction
flags for the parameter:

   1
      Specifies an input parameter to the function.

   2
      Output parameter.  The foreign function fills in a value.

   4
      Input parameter which defaults to the integer zero.

The optional second item is the parameter name as string.  If this is
specified, the foreign function can be called with named parameters.

The optional third item is the default value for this parameter.

The following example demonstrates how to wrap the Windows
"MessageBoxW" function so that it supports default parameters and
named arguments. The C declaration from the windows header file is
this:

   WINUSERAPI int WINAPI
   MessageBoxW(
       HWND hWnd,
       LPCWSTR lpText,
       LPCWSTR lpCaption,
       UINT uType);

Here is the wrapping with "ctypes":

   >>> from ctypes import c_int, WINFUNCTYPE, windll
   >>> from ctypes.wintypes import HWND, LPCWSTR, UINT
   >>> prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
   >>> paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", "Hello from ctypes"), (1, "flags", 0)
   >>> MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)

The "MessageBox" foreign function can now be called in these ways:

   >>> MessageBox()
   >>> MessageBox(text="Spam, spam, spam")
   >>> MessageBox(flags=2, text="foo bar")

A second example demonstrates output parameters.  The win32
"GetWindowRect" function retrieves the dimensions of a specified
window by copying them into "RECT" structure that the caller has to
supply.  Here is the C declaration:

   WINUSERAPI BOOL WINAPI
   GetWindowRect(
        HWND hWnd,
        LPRECT lpRect);

Here is the wrapping with "ctypes":

   >>> from ctypes import POINTER, WINFUNCTYPE, windll, WinError
   >>> from ctypes.wintypes import BOOL, HWND, RECT
   >>> prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
   >>> paramflags = (1, "hwnd"), (2, "lprect")
   >>> GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)
   >>>

Functions with output parameters will automatically return the output
parameter value if there is a single one, or a tuple containing the
output parameter values when there are more than one, so the
GetWindowRect function now returns a RECT instance, when called.

Output parameters can be combined with the "errcheck" protocol to do
further output processing and error checking.  The win32
"GetWindowRect" api function returns a "BOOL" to signal success or
failure, so this function could do the error checking, and raises an
exception when the api call failed:

   >>> def errcheck(result, func, args):
   ...     if not result:
   ...         raise WinError()
   ...     return args
   ...
   >>> GetWindowRect.errcheck = errcheck
   >>>

If the "errcheck" function returns the argument tuple it receives
unchanged, "ctypes" continues the normal processing it does on the
output parameters.  If you want to return a tuple of window
coordinates instead of a "RECT" instance, you can retrieve the fields
in the function and return them instead, the normal processing will no
longer take place:

   >>> def errcheck(result, func, args):
   ...     if not result:
   ...         raise WinError()
   ...     rc = args[1]
   ...     return rc.left, rc.top, rc.bottom, rc.right
   ...
   >>> GetWindowRect.errcheck = errcheck
   >>>


Funções utilitárias
-------------------

ctypes.addressof(obj)

   Returns the address of the memory buffer as integer.  *obj* must be
   an instance of a ctypes type.

   Levanta um evento de auditoria "ctypes.addressof" com o argumento
   "obj".

ctypes.alignment(obj_or_type)

   Returns the alignment requirements of a ctypes type. *obj_or_type*
   must be a ctypes type or instance.

ctypes.byref(obj[, offset])

   Returns a light-weight pointer to *obj*, which must be an instance
   of a ctypes type.  *offset* defaults to zero, and must be an
   integer that will be added to the internal pointer value.

   "byref(obj, offset)" corresponds to this C code:

      (((char *)&obj) + offset)

   The returned object can only be used as a foreign function call
   parameter. It behaves similar to "pointer(obj)", but the
   construction is a lot faster.

ctypes.CopyComPointer(src, dst)

   Copia um ponteiro COM de *src* para *dst* e devolve o valor
   "HRESULT" específico para Windows.

   Se *src* não for "NULL", o seu método "AddRef" é chamado,
   incrementando a contagem de referências.

   Em contraste, a contagem de referências de *dst* não será
   decrementada antes de atribuir o novo valor. A menos que *dst* seja
   "NULL", o chamador é responsável por decrementar a contagem de
   referências, chamando o método "Release" de *dst* quando
   necessário.

   Disponibilidade: Windows

   Adicionado na versão 3.14.

ctypes.cast(obj, type)

   Esta função é semelhante ao operador cast em C. Retorna uma nova
   instância de *type* que aponta para o mesmo bloco de memória que
   *obj*. *type* deve ser um tipo de ponteiro e *obj* deve ser um
   objeto que pode ser interpretado como um ponteiro.

ctypes.create_string_buffer(init, size=None)
ctypes.create_string_buffer(size)

   This function creates a mutable character buffer. The returned
   object is a ctypes array of "c_char".

   If *size* is given (and not "None"), it must be an "int". It
   specifies the size of the returned array.

   If the *init* argument is given, it must be "bytes". It is used to
   initialize the array items. Bytes not initialized this way are set
   to zero (NUL).

   If *size* is not given (or if it is "None"), the buffer is made one
   element larger than *init*, effectively adding a NUL terminator.

   If both arguments are given, *size* must not be less than
   "len(init)".

   Aviso:

     If *size* is equal to "len(init)", a NUL terminator is not added.
     Do not treat such a buffer as a C string.

   Por exemplo:

      >>> bytes(create_string_buffer(2))
      b'\x00\x00'
      >>> bytes(create_string_buffer(b'ab'))
      b'ab\x00'
      >>> bytes(create_string_buffer(b'ab', 2))
      b'ab'
      >>> bytes(create_string_buffer(b'ab', 4))
      b'ab\x00\x00'
      >>> bytes(create_string_buffer(b'abcdef', 2))
      Traceback (most recent call last):
         ...
      ValueError: byte string too long

   Levanta um evento de auditoria "ctypes.create_string_buffer" com os
   argumentos "init", "size".

ctypes.create_unicode_buffer(init, size=None)
ctypes.create_unicode_buffer(size)

   This function creates a mutable unicode character buffer. The
   returned object is a ctypes array of "c_wchar".

   The function takes the same arguments as "create_string_buffer()"
   except *init* must be a string and *size* counts "c_wchar".

   Levanta um evento de auditoria "ctypes.create_unicode_buffer" com
   os argumentos "init", "size".

ctypes.DllCanUnloadNow()

   This function is a hook which allows implementing in-process COM
   servers with ctypes.  It is called from the DllCanUnloadNow
   function that the _ctypes extension dll exports.

   Disponibilidade: Windows

ctypes.DllGetClassObject()

   This function is a hook which allows implementing in-process COM
   servers with ctypes.  It is called from the DllGetClassObject
   function that the "_ctypes" extension dll exports.

   Disponibilidade: Windows

ctypes.util.dllist()

   Tenta fornecer uma lista de caminhos das bibliotecas partilhadas
   carregadas no processo atual. Estes caminhos não são normalizados
   nem processados de forma alguma. A função pode levantar "OSError"
   se as APIs da plataforma subjacente falharem. A funcionalidade
   exata depende do sistema.

   Na maioria das plataformas, o primeiro elemento da lista
   corresponde ao arquivo executável atual. Pode ser uma string vazia.

   Disponibilidade: Windows, macOS, iOS, glibc, BSD libc, musl

   Adicionado na versão 3.14.

ctypes.FormatError([code])

   Returns a textual description of the error code *code*.  If no
   error code is specified, the last error code is used by calling the
   Windows API function "GetLastError()".

   Disponibilidade: Windows

ctypes.GetLastError()

   Returns the last error code set by Windows in the calling thread.
   This function calls the Windows "GetLastError()" function directly,
   it does not return the ctypes-private copy of the error code.

   Disponibilidade: Windows

ctypes.get_errno()

   Returns the current value of the ctypes-private copy of the system
   "errno" variable in the calling thread.

   Levanta um evento de auditoria "ctypes.get_errno" sem argumentos.

ctypes.get_last_error()

   Returns the current value of the ctypes-private copy of the system
   "LastError" variable in the calling thread.

   Disponibilidade: Windows

   Levanta um evento de auditoria "ctypes.get_last_error" sem
   argumentos.

ctypes.memmove(dst, src, count)

   Same as the standard C memmove library function: copies *count*
   bytes from *src* to *dst*. *dst* and *src* must be integers or
   ctypes instances that can be converted to pointers.

ctypes.memset(dst, c, count)

   Same as the standard C memset library function: fills the memory
   block at address *dst* with *count* bytes of value *c*. *dst* must
   be an integer specifying an address, or a ctypes instance.

ctypes.POINTER(type, /)

   Cria ou retorna um tipo de ponteiro ctypes. Os tipos de ponteiro
   são guardados em cache e reutilizados internamente, assim, chamar
   esta função repetidamente é eficiente. *type* deve ser um tipo
   ctypes.

   O tipo de ponteiro resultante é armazenado em cache no atributo
   "__pointer_type__" de *type*. É possível definir este atributo
   antes da primeira chamada a "POINTER" para definir um tipo de
   ponteiro personalizado. No entanto, fazer isto é desencorajado:
   criar manualmente um tipo de ponteiro adequado é difícil sem
   depender de detalhes de implementação que podem mudar em versões
   futuras do Python.

ctypes.pointer(obj, /)

   Cria uma nova instância de ponteiro, apontando para *obj*. O objeto
   devolvido é do tipo "POINTER(type(obj))".

   Nota: se você pretende apenas passar um ponteiro para um objeto em
   uma chamada de função externa, deve usar "byref(obj)", que é muito
   mais rápido.

ctypes.resize(obj, size)

   Esta função redimensiona o buffer de memória interno de *obj*, que
   deve ser uma instância de um tipo ctypes. Não é possível reduzir o
   buffer para menos do que o tamanho nativo do tipo do objeto,
   conforme dado por "sizeof(type(obj))", mas é possível aumentá-lo.

ctypes.set_errno(value)

   Define o valor atual da cópia privada do ctypes da variável do
   sistema "errno" na thread de chamada para *value* e devolve o valor
   anterior.

   Levanta um evento de auditoria "ctypes.set_errno" com o argumento
   "errno".

ctypes.set_last_error(value)

   Define o valor atual da cópia privada do ctypes da variável do
   sistema "LastError" na thread de chamada para *value* e devolve o
   valor anterior.

   Disponibilidade: Windows

   Levanta um evento de auditoria "ctypes.set_last_error" com o
   argumento "error".

ctypes.sizeof(obj_or_type)

   Retornar o tamanho em bytes de um tipo ctypes ou buffer de memória
   de instância. Faz o mesmo que o operador C "sizeof".

ctypes.string_at(ptr, size=-1)

   Retorna a string de bytes em *void *ptr*. Se *size* for
   especificado, é usado como tamanho; caso contrário, assume-se que a
   string é terminada por zero.

   Levanta um evento de auditoria "ctypes.string_at" com os argumentos
   "ptr" e "size".

ctypes.WinError(code=None, descr=None)

   Creates an instance of "OSError".  If *code* is not specified,
   "GetLastError()" is called to determine the error code. If *descr*
   is not specified, "FormatError()" is called to get a textual
   description of the error.

   Disponibilidade: Windows

   Alterado na versão 3.3: An instance of "WindowsError" used to be
   created, which is now an alias of "OSError".

ctypes.wstring_at(ptr, size=-1)

   Return the wide-character string at *void *ptr*. If *size* is
   specified, it is used as the number of characters of the string,
   otherwise the string is assumed to be zero-terminated.

   Levanta um evento de auditoria "ctypes.wstring_at" com os
   argumentos "ptr", "size".

ctypes.memoryview_at(ptr, size, readonly=False)

   Retorna um objeto "memoryview" de comprimento *size* que referencia
   a memória a partir de *void *ptr*.

   Se *readonly* for verdadeiro, o objeto "memoryview" devolvido não
   pode ser usado para modificar a memória subjacente. (Alterações
   feitas por outros meios ainda serão refletidas no objeto
   devolvido).

   Esta função é semelhante a "string_at()", com a diferença
   fundamental de não fazer uma cópia da memória especificada. É uma
   alternativa semanticamente equivalente (mas mais eficiente) a
   "memoryview((c_byte * size).from_address(ptr))". (Embora
   "from_address()" só aceite inteiros, *ptr* também pode ser
   fornecido como um objeto "ctypes.POINTER" ou um objeto "byref()".)

   Levanta um evento de auditoria "ctypes.memoryview_at" com os
   argumentos "address", "size" e "readonly".

   Adicionado na versão 3.14.


Data types
----------

class ctypes._CData

   This non-public class is the common base class of all ctypes data
   types. Among other things, all ctypes type instances contain a
   memory block that hold C compatible data; the address of the memory
   block is returned by the "addressof()" helper function. Another
   instance variable is exposed as "_objects"; this contains other
   Python objects that need to be kept alive in case the memory block
   contains pointers.

   Common methods of ctypes data types, these are all class methods
   (to be exact, they are methods of the *metaclass*):

   from_buffer(source[, offset])

      This method returns a ctypes instance that shares the buffer of
      the *source* object.  The *source* object must support the
      writeable buffer interface.  The optional *offset* parameter
      specifies an offset into the source buffer in bytes; the default
      is zero.  If the source buffer is not large enough a
      "ValueError" is raised.

      Levanta um evento de auditoria "ctypes.cdata/buffer" com os
      argumentos "pointer", "size", "offset".

   from_buffer_copy(source[, offset])

      This method creates a ctypes instance, copying the buffer from
      the *source* object buffer which must be readable.  The optional
      *offset* parameter specifies an offset into the source buffer in
      bytes; the default is zero.  If the source buffer is not large
      enough a "ValueError" is raised.

      Levanta um evento de auditoria "ctypes.cdata/buffer" com os
      argumentos "pointer", "size", "offset".

   from_address(address)

      This method returns a ctypes type instance using the memory
      specified by *address* which must be an integer.

      Este método, e outros que indiretamente chamam este método,
      levantam um evento de auditoria "ctypes.cdata" com o argumento
      "address".

   from_param(obj)

      This method adapts *obj* to a ctypes type.  It is called with
      the actual object used in a foreign function call when the type
      is present in the foreign function's "argtypes" tuple; it must
      return an object that can be used as a function call parameter.

      All ctypes data types have a default implementation of this
      classmethod that normally returns *obj* if that is an instance
      of the type.  Some types accept other objects as well.

   in_dll(library, name)

      This method returns a ctypes type instance exported by a shared
      library. *name* is the name of the symbol that exports the data,
      *library* is the loaded shared library.

   Common class variables of ctypes data types:

   __pointer_type__

      O tipo de ponteiro que foi criado chamando "POINTER()" para o
      tipo de dados ctypes correspondente. Se um tipo de ponteiro
      ainda não foi criado, o atributo está ausente.

      Adicionado na versão 3.14.

   Variáveis de instância comuns dos tipos de dados ctypes:

   _b_base_

      Sometimes ctypes data instances do not own the memory block they
      contain, instead they share part of the memory block of a base
      object.  The "_b_base_" read-only member is the root ctypes
      object that owns the memory block.

   _b_needsfree_

      This read-only variable is true when the ctypes data instance
      has allocated the memory block itself, false otherwise.

   _objects

      This member is either "None" or a dictionary containing Python
      objects that need to be kept alive so that the memory block
      contents is kept valid.  This object is only exposed for
      debugging; never modify the contents of this dictionary.


Tipos de dados fundamentais
---------------------------

class ctypes._SimpleCData

   This non-public class is the base class of all fundamental ctypes
   data types. It is mentioned here because it contains the common
   attributes of the fundamental ctypes data types.  "_SimpleCData" is
   a subclass of "_CData", so it inherits their methods and
   attributes. ctypes data types that are not and do not contain
   pointers can now be pickled.

   Instances have a single attribute:

   value

      This attribute contains the actual value of the instance. For
      integer and pointer types, it is an integer, for character
      types, it is a single character bytes object or string, for
      character pointer types it is a Python bytes object or string.

      When the "value" attribute is retrieved from a ctypes instance,
      usually a new object is returned each time.  "ctypes" does *not*
      implement original object return, always a new object is
      constructed.  The same is true for all other ctypes object
      instances.

   Each subclass has a class attribute:

   _type_

      Class attribute that contains an internal type code, as a
      single-character string. See Tipos de dados fundamentais for a
      summary.

      Types marked * in the summary may be (or always are) aliases of
      a different "_SimpleCData" subclass, and will not necessarily
      use the listed type code. For example, if the platform's long,
      long long and time_t C types are the same, then "c_long",
      "c_longlong" and "c_time_t" all refer to a single class,
      "c_long", whose "_type_" code is "'l'". The "'L'" code will be
      unused.

      Ver também:

        The "array" and struct modules, as well as third-party modules
        like numpy, use similar -- but slightly different -- type
        codes.

Fundamental data types, when returned as foreign function call
results, or, for example, by retrieving structure field members or
array items, are transparently converted to native Python types.  In
other words, if a foreign function has a "restype" of "c_char_p", you
will always receive a Python bytes object, *not* a "c_char_p"
instance.

Subclasses of fundamental data types do *not* inherit this behavior.
So, if a foreign functions "restype" is a subclass of "c_void_p", you
will receive an instance of this subclass from the function call. Of
course, you can get the value of the pointer by accessing the "value"
attribute.

These are the fundamental ctypes data types:

class ctypes.c_byte

   Representa o tipo de dados C signed char e interpreta o valor como
   um inteiro pequeno. O construtor aceita um inicializador inteiro
   opcional; não há verificação de overflow.

class ctypes.c_char

   Representa o tipo de dados C char e interpreta o valor como um
   único caractere. O construtor aceita um inicializador de string
   opcional; o comprimento da string deve ser exatamente um caractere.

class ctypes.c_char_p

   Representa o tipo de dados C char* quando aponta para uma string
   terminada em zero. Para um ponteiro de caractere geral que também
   pode apontar para dados binários, deve-se usar "POINTER(c_char)". O
   construtor aceita um endereço inteiro ou um objeto bytes.

class ctypes.c_double

   Representa o tipo de dados C double. O construtor aceita um
   inicializador opcional de tipo float.

class ctypes.c_longdouble

   Representa o tipo de dados C long double. O construtor aceita um
   inicializador opcional de tipo float. Em plataformas onde
   "sizeof(long double) == sizeof(double)", é um alias para
   "c_double".

class ctypes.c_float

   Representa o tipo de dados C float. O construtor aceita um
   inicializador opcional de tipo float.

class ctypes.c_double_complex

   Representa o tipo de dados C double complex, se disponível. O
   construtor aceita um inicializador opcional "complex".

   Adicionado na versão 3.14.

class ctypes.c_float_complex

   Representa o tipo de dados C float complex, se disponível. O
   construtor aceita um inicializador opcional "complex".

   Adicionado na versão 3.14.

class ctypes.c_longdouble_complex

   Representa o tipo de dados C long double complex, se disponível. O
   construtor aceita um inicializador opcional "complex".

   Adicionado na versão 3.14.

class ctypes.c_int

   Represents the C signed int datatype.  The constructor accepts an
   optional integer initializer; no overflow checking is done.  On
   platforms where "sizeof(int) == sizeof(long)" it is an alias to
   "c_long".

class ctypes.c_int8

   Represents the C 8-bit signed int datatype.  It is an alias for
   "c_byte".

class ctypes.c_int16

   Represents the C 16-bit signed int datatype.  Usually an alias for
   "c_short".

class ctypes.c_int32

   Represents the C 32-bit signed int datatype.  Usually an alias for
   "c_int".

class ctypes.c_int64

   Represents the C 64-bit signed int datatype.  Usually an alias for
   "c_longlong".

class ctypes.c_long

   Represents the C signed long datatype.  The constructor accepts an
   optional integer initializer; no overflow checking is done.

class ctypes.c_longlong

   Represents the C signed long long datatype.  The constructor
   accepts an optional integer initializer; no overflow checking is
   done. On platforms where "sizeof(long long) == sizeof(long)" it is
   an alias to "c_long".

class ctypes.c_short

   Represents the C signed short datatype.  The constructor accepts an
   optional integer initializer; no overflow checking is done.

class ctypes.c_size_t

   Represents the C "size_t" datatype. Usually an alias for another
   unsigned integer type.

class ctypes.c_ssize_t

   Represents the "Py_ssize_t" datatype. This is a signed version of
   "size_t"; that is, the POSIX "ssize_t" type. Usually an alias for
   another integer type.

   Adicionado na versão 3.2.

class ctypes.c_time_t

   Represents the C "time_t" datatype. Usually an alias for another
   integer type.

   Adicionado na versão 3.12.

class ctypes.c_ubyte

   Represents the C unsigned char datatype, it interprets the value as
   small integer.  The constructor accepts an optional integer
   initializer; no overflow checking is done.

class ctypes.c_uint

   Represents the C unsigned int datatype.  The constructor accepts an
   optional integer initializer; no overflow checking is done.  On
   platforms where "sizeof(int) == sizeof(long)" it is an alias for
   "c_ulong".

class ctypes.c_uint8

   Represents the C 8-bit unsigned int datatype.  It is an alias for
   "c_ubyte".

class ctypes.c_uint16

   Represents the C 16-bit unsigned int datatype.  Usually an alias
   for "c_ushort".

class ctypes.c_uint32

   Represents the C 32-bit unsigned int datatype.  Usually an alias
   for "c_uint".

class ctypes.c_uint64

   Represents the C 64-bit unsigned int datatype.  Usually an alias
   for "c_ulonglong".

class ctypes.c_ulong

   Represents the C unsigned long datatype.  The constructor accepts
   an optional integer initializer; no overflow checking is done.

class ctypes.c_ulonglong

   Represents the C unsigned long long datatype.  The constructor
   accepts an optional integer initializer; no overflow checking is
   done. On platforms where "sizeof(long long) == sizeof(long)" it is
   an alias to "c_long".

class ctypes.c_ushort

   Represents the C unsigned short datatype.  The constructor accepts
   an optional integer initializer; no overflow checking is done.

class ctypes.c_void_p

   Represents the C void* type.  The value is represented as integer.
   The constructor accepts an optional integer initializer.

class ctypes.c_wchar

   Represents the C "wchar_t" datatype, and interprets the value as a
   single character unicode string.  The constructor accepts an
   optional string initializer, the length of the string must be
   exactly one character.

class ctypes.c_wchar_p

   Represents the C wchar_t* datatype, which must be a pointer to a
   zero-terminated wide character string.  The constructor accepts an
   integer address, or a string.

class ctypes.c_bool

   Represent the C bool datatype (more accurately, _Bool from C99).
   Its value can be "True" or "False", and the constructor accepts any
   object that has a truth value.

class ctypes.HRESULT

   Represents a "HRESULT" value, which contains success or error
   information for a function or method call.

   Disponibilidade: Windows

class ctypes.py_object

   Representa o tipo de dados C PyObject*. Chamar isto sem um
   argumento cria um ponteiro "NULL" PyObject*.

   Alterado na versão 3.14: "py_object" é agora um *tipo genérico*.


Windows data types
------------------

**Source code:** Lib/ctypes/wintypes.py

The "ctypes.wintypes" module provides types for use with Windows APIs.
Most are aliases for types defined in "ctypes". See Microsoft's
Windows data types documentation for the corresponding C definitions.
On non-Windows platforms, the sizes and layouts of these types may
differ from their Windows counterparts.

Alterado na versão 3.14: Added "HCONV", "HCONVLIST", "HCURSOR",
"HDDEDATA", "HDROP", "HFILE", "HRESULT", and "HSZ".

Por exemplo:

   >>> from ctypes import POINTER
   >>> from ctypes.wintypes import LPRECT, RECT, SHORT
   >>> SHORT(-1).value
   -1
   >>> rect = RECT(0, 0, 100, 50)
   >>> rect.right, rect.bottom
   (100, 50)
   >>> LPRECT is POINTER(RECT)
   True


Simple types
~~~~~~~~~~~~

The following names are aliases for fundamental "ctypes" types:

+----------------------------------------------------+----------------------------------------------------+
| Windows types                                      | "ctypes" type                                      |
|====================================================|====================================================|
| class ctypes.wintypes.BYTE class                   | "c_ubyte"                                          |
| ctypes.wintypes.BOOLEAN                            |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.CHAR                         | "c_char"                                           |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.WCHAR                        | "c_wchar"                                          |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.WORD class                   | "c_ushort"                                         |
| ctypes.wintypes.USHORT class ctypes.wintypes.ATOM  |                                                    |
| class ctypes.wintypes.LANGID                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.DWORD class                  | "c_ulong"                                          |
| ctypes.wintypes.ULONG class                        |                                                    |
| ctypes.wintypes.COLORREF class                     |                                                    |
| ctypes.wintypes.LCID class ctypes.wintypes.LCTYPE  |                                                    |
| class ctypes.wintypes.LGRPID                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.BOOL class                   | "c_long"                                           |
| ctypes.wintypes.LONG class ctypes.wintypes.HRESULT |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.INT class                    | "c_int"                                            |
| ctypes.wintypes.HFILE                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.UINT                         | "c_uint"                                           |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.SHORT                        | "c_short"                                          |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.DOUBLE                       | "c_double"                                         |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.FLOAT                        | "c_float"                                          |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LARGE_INTEGER                | "c_longlong"                                       |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.ULARGE_INTEGER               | "c_ulonglong"                                      |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPCSTR class                 | "c_char_p"                                         |
| ctypes.wintypes.LPSTR                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPCOLESTR class              | "c_wchar_p"                                        |
| ctypes.wintypes.LPOLESTR class                     |                                                    |
| ctypes.wintypes.OLESTR class                       |                                                    |
| ctypes.wintypes.LPCWSTR class                      |                                                    |
| ctypes.wintypes.LPWSTR                             |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPCVOID class                | "c_void_p"                                         |
| ctypes.wintypes.LPVOID                             |                                                    |
+----------------------------------------------------+----------------------------------------------------+

"LARGE_INTEGER" and "ULARGE_INTEGER" expose an integer "value"
attribute, with no "LowPart", "HighPart", or "QuadPart" fields.

class ctypes.wintypes.WPARAM

   An unsigned integer type with the same size as "c_void_p".

class ctypes.wintypes.LPARAM

   A signed integer type with the same size as "c_void_p".

class ctypes.wintypes.VARIANT_BOOL

   A 16-bit Boolean type whose "value" attribute is a Python "bool".
   Assigning to "value" stores "-1" for a true value and "0" for a
   false value.


Handle types
~~~~~~~~~~~~

class ctypes.wintypes.HANDLE

   An alias for "c_void_p", used to represent Windows handles.

class ctypes.wintypes.HACCEL
class ctypes.wintypes.HBITMAP
class ctypes.wintypes.HBRUSH
class ctypes.wintypes.HCOLORSPACE
class ctypes.wintypes.HCONV
class ctypes.wintypes.HCONVLIST
class ctypes.wintypes.HCURSOR
class ctypes.wintypes.HDC
class ctypes.wintypes.HDDEDATA
class ctypes.wintypes.HDESK
class ctypes.wintypes.HDROP
class ctypes.wintypes.HDWP
class ctypes.wintypes.HENHMETAFILE
class ctypes.wintypes.HFONT
class ctypes.wintypes.HGDIOBJ
class ctypes.wintypes.HGLOBAL
class ctypes.wintypes.HHOOK
class ctypes.wintypes.HICON
class ctypes.wintypes.HINSTANCE
class ctypes.wintypes.HKEY
class ctypes.wintypes.HKL
class ctypes.wintypes.HLOCAL
class ctypes.wintypes.HMENU
class ctypes.wintypes.HMETAFILE
class ctypes.wintypes.HMODULE
class ctypes.wintypes.HMONITOR
class ctypes.wintypes.HPALETTE
class ctypes.wintypes.HPEN
class ctypes.wintypes.HRGN
class ctypes.wintypes.HRSRC
class ctypes.wintypes.HSTR
class ctypes.wintypes.HSZ
class ctypes.wintypes.HTASK
class ctypes.wintypes.HWINSTA
class ctypes.wintypes.HWND
class ctypes.wintypes.SC_HANDLE
class ctypes.wintypes.SERVICE_STATUS_HANDLE

   Aliases for "HANDLE" for use with specific Windows APIs. "HFILE" is
   an alias for "INT" and is listed among the simple types above.


Structures
~~~~~~~~~~

The following types are subclasses of "ctypes.Structure".

class ctypes.wintypes.RECT
class ctypes.wintypes.RECTL
class ctypes.wintypes.tagRECT

   A rectangle with "left", "top", "right", and "bottom" fields, all
   of type "LONG".

class ctypes.wintypes.SMALL_RECT

   A rectangle with "Left", "Top", "Right", and "Bottom" fields, all
   of type "SHORT".

class ctypes.wintypes.POINT
class ctypes.wintypes.POINTL
class ctypes.wintypes.tagPOINT

   A point with "x" and "y" fields, both of type "LONG".

class ctypes.wintypes.SIZE
class ctypes.wintypes.SIZEL
class ctypes.wintypes.tagSIZE

   Dimensions with "cx" and "cy" fields, both of type "LONG".

class ctypes.wintypes.FILETIME

   A file time with "dwLowDateTime" and "dwHighDateTime" fields, both
   of type "DWORD".

class ctypes.wintypes.MSG
class ctypes.wintypes.tagMSG

   A Windows message with the following fields:

   +----------------------------------------------------+----------------------------------------------------+
   | Campo                                              | Tipo                                               |
   |====================================================|====================================================|
   | "hWnd"                                             | "HWND"                                             |
   +----------------------------------------------------+----------------------------------------------------+
   | "message"                                          | "UINT"                                             |
   +----------------------------------------------------+----------------------------------------------------+
   | "wParam"                                           | "WPARAM"                                           |
   +----------------------------------------------------+----------------------------------------------------+
   | "lParam"                                           | "LPARAM"                                           |
   +----------------------------------------------------+----------------------------------------------------+
   | "time"                                             | "DWORD"                                            |
   +----------------------------------------------------+----------------------------------------------------+
   | "pt"                                               | "POINT"                                            |
   +----------------------------------------------------+----------------------------------------------------+

class ctypes.wintypes.WIN32_FIND_DATAA
class ctypes.wintypes.WIN32_FIND_DATAW

   Structures used by Windows file-search functions, with the
   following fields.  "WIN32_FIND_DATAA" uses "CHAR" for its file
   names, and "WIN32_FIND_DATAW" uses "WCHAR".

   +----------------------------------------------------+----------------------------------------------------+
   | Fields                                             | Tipo                                               |
   |====================================================|====================================================|
   | "dwFileAttributes"                                 | "DWORD"                                            |
   +----------------------------------------------------+----------------------------------------------------+
   | "ftCreationTime", "ftLastAccessTime",              | "FILETIME"                                         |
   | "ftLastWriteTime"                                  |                                                    |
   +----------------------------------------------------+----------------------------------------------------+
   | "nFileSizeHigh", "nFileSizeLow"                    | "DWORD"                                            |
   +----------------------------------------------------+----------------------------------------------------+
   | "dwReserved0", "dwReserved1"                       | "DWORD"                                            |
   +----------------------------------------------------+----------------------------------------------------+
   | "cFileName"                                        | An array of "MAX_PATH" characters                  |
   +----------------------------------------------------+----------------------------------------------------+
   | "cAlternateFileName"                               | An array of 14 characters                          |
   +----------------------------------------------------+----------------------------------------------------+


Pointer types
~~~~~~~~~~~~~

The following names are aliases for "ctypes.POINTER(T)", where *T* is
the type in the second column:

+----------------------------------------------------+----------------------------------------------------+
| Pointer types                                      | Referenced type                                    |
|====================================================|====================================================|
| class ctypes.wintypes.LPBOOL class                 | "BOOL"                                             |
| ctypes.wintypes.PBOOL                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PBOOLEAN                     | "BOOLEAN"                                          |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPBYTE class                 | "BYTE"                                             |
| ctypes.wintypes.PBYTE                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PCHAR                        | "CHAR"                                             |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPCOLORREF                   | "COLORREF"                                         |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPDWORD class                | "DWORD"                                            |
| ctypes.wintypes.PDWORD                             |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPFILETIME class             | "FILETIME"                                         |
| ctypes.wintypes.PFILETIME                          |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PFLOAT                       | "FLOAT"                                            |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPHANDLE class               | "HANDLE"                                           |
| ctypes.wintypes.PHANDLE                            |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PHKEY                        | "HKEY"                                             |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPHKL                        | "HKL"                                              |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPINT class                  | "INT"                                              |
| ctypes.wintypes.PINT                               |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PLARGE_INTEGER               | "LARGE_INTEGER"                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PLCID                        | "LCID"                                             |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPLONG class                 | "LONG"                                             |
| ctypes.wintypes.PLONG                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPMSG class                  | "MSG"                                              |
| ctypes.wintypes.PMSG                               |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPPOINT class                | "POINT"                                            |
| ctypes.wintypes.PPOINT                             |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PPOINTL                      | "POINTL"                                           |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPRECT class                 | "RECT"                                             |
| ctypes.wintypes.PRECT                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPRECTL class                | "RECTL"                                            |
| ctypes.wintypes.PRECTL                             |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPSC_HANDLE                  | "SC_HANDLE"                                        |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PSHORT                       | "SHORT"                                            |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPSIZE class                 | "SIZE"                                             |
| ctypes.wintypes.PSIZE                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPSIZEL class                | "SIZEL"                                            |
| ctypes.wintypes.PSIZEL                             |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PSMALL_RECT                  | "SMALL_RECT"                                       |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPUINT class                 | "UINT"                                             |
| ctypes.wintypes.PUINT                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PULARGE_INTEGER              | "ULARGE_INTEGER"                                   |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PULONG                       | "ULONG"                                            |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PUSHORT                      | "USHORT"                                           |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.PWCHAR                       | "WCHAR"                                            |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPWIN32_FIND_DATAA class     | "WIN32_FIND_DATAA"                                 |
| ctypes.wintypes.PWIN32_FIND_DATAA                  |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPWIN32_FIND_DATAW class     | "WIN32_FIND_DATAW"                                 |
| ctypes.wintypes.PWIN32_FIND_DATAW                  |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| class ctypes.wintypes.LPWORD class                 | "WORD"                                             |
| ctypes.wintypes.PWORD                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+


Constants and functions
~~~~~~~~~~~~~~~~~~~~~~~

ctypes.wintypes.MAX_PATH

   The value "260", used as the size of the file-name arrays in
   "WIN32_FIND_DATAA" and "WIN32_FIND_DATAW".

ctypes.wintypes.RGB(red, green, blue)

   Return a "COLORREF" value as a Python integer.  The *red*, *green*,
   and *blue* arguments are integers from "0" to "255", specifying the
   intensity of each color component:

      >>> from ctypes.wintypes import RGB
      >>> hex(RGB(255, 128, 0))
      '0x80ff'


Tipos de dados estruturados
---------------------------

class ctypes.Union(*args, **kw)

   Classe base abstrata para uniões em ordem de bytes nativa.

   Uniões partilham atributos e comportamentos comuns com estruturas;
   veja a documentação da "Structure" para mais detalhes.

class ctypes.BigEndianUnion(*args, **kw)

   Classe base abstrata para uniões em ordem de bytes *big endian*.

   Adicionado na versão 3.11.

class ctypes.LittleEndianUnion(*args, **kw)

   Classe base abstrata para uniões em ordem de bytes *little endian*.

   Adicionado na versão 3.11.

class ctypes.BigEndianStructure(*args, **kw)

   Classe base abstrata para estruturas em ordem de bytes *big
   endian*.

class ctypes.LittleEndianStructure(*args, **kw)

   Classe base abstrata para estruturas em ordem de bytes *little
   endian*.

Estruturas e uniões com ordem de bytes não nativa não podem conter
campos de tipo ponteiro ou quaisquer outros tipos de dados que
contenham campos de tipo ponteiro.

class ctypes.Structure(*args, **kw)

   Classe base abstrata para estruturas em ordem de bytes *nativa*.

   Concrete structure and union types must be created by subclassing
   one of these types, and at least define a "_fields_" class
   variable. "ctypes" will create *descriptor*s which allow reading
   and writing the fields by direct attribute accesses.  These are the

   _fields_

      Uma sequência que define os campos da estrutura. Os itens devem
      ser tuplas com 2 ou 3 elementos. O primeiro item é o nome do
      campo; o segundo item especifica o tipo do campo, que pode ser
      qualquer tipo de dados ctypes.

      Para campos de tipo inteiro como "c_int", pode ser fornecido um
      terceiro item opcional. Deve ser um inteiro positivo pequeno que
      define a largura em bits do campo.

      Os nomes dos campos devem ser únicos em uma estrutura ou união.
      Isto não é verificado, apenas um campo pode ser acessado quando
      os nomes são repetidos.

      É possível definir a variável de classe "_fields_" *depois* da
      instrução de classe que define a subclasse de Structure, o que
      permite criar tipos de dados que referenciam diretamente ou
      indiretamente a si mesmos:

         class List(Structure):
             pass
         List._fields_ = [("pnext", POINTER(List)),
                          ...
                         ]

      A variável de classe "_fields_" só pode ser definida uma vez.
      Atribuições posteriores levantarão um "AttributeError".

      Além disso, a variável de classe "_fields_" deve ser definida
      antes que o tipo de estrutura ou união seja usado pela primeira
      vez: uma instância ou subclasse é criada, "sizeof()" é chamada
      sobre ela, etc. Atribuições posteriores a "_fields_" levantarão
      um "AttributeError". Se "_fields_" não tiver sido definida antes
      de tal uso, a estrutura ou união não terá campos próprios, como
      se "_fields_" estivesse vazia.

      As sub-subclasses de tipos de estrutura herdam os campos da
      classe base, bem como os "_fields_" definidos na sub-subclasse,
      se existirem.

   _pack_

      An optional small integer that allows overriding the alignment
      of structure fields in the instance.

      This is only implemented for the MSVC-compatible memory layout
      (see "_layout_").

      Setting "_pack_" to 0 is the same as not setting it at all.
      Otherwise, the value must be a positive power of two. The effect
      is equivalent to "#pragma pack(N)" in C, except "ctypes" may
      allow larger *n* than what the compiler accepts.

      "_pack_" must already be defined when "_fields_" is assigned,
      otherwise it will have no effect.

      Descontinuado desde a versão 3.14, será removido na versão 3.19:
      For historical reasons, if "_pack_" is non-zero, the MSVC-
      compatible layout will be used by default. On non-Windows
      platforms, this default is deprecated and is slated to become an
      error in Python 3.19. If it is intended, set "_layout_" to
      "'ms'" explicitly.

   _align_

      An optional small integer that allows increasing the alignment
      of the structure when being packed or unpacked to/from memory.

      The value must not be negative. The effect is equivalent to
      "__attribute__((aligned(N)))" on GCC or "#pragma align(N)" on
      MSVC, except "ctypes" may allow values that the compiler would
      reject.

      "_align_" can only *increase* a structure's alignment
      requirements. Setting it to 0 or 1 has no effect.

      Using values that are not powers of two is discouraged and may
      lead to surprising behavior.

      "_align_" must already be defined when "_fields_" is assigned,
      otherwise it will have no effect.

      Adicionado na versão 3.13.

   _layout_

      Uma string opcional que nomeia o layout da estrutura/união.
      Atualmente, ele pode ser definido como:

      * ""ms"": o layout usado pelo compilador Microsoft (MSVC). No
        GCC e no Clang, este layout pode ser selecionado com
        "__attribute__((ms_struct))".

      * ""gcc-sysv"": o layout usado pelo GCC com o modelo de dados
        System V ou “SysV-like”, como usado no Linux e no macOS. Com
        este layout, "_pack_" não deve estar definido ou deve ser
        igual a zero.

      Se não for definido explicitamente, "ctypes" usará um valor
      predefinido que corresponde às convenções da plataforma. Este
      valor predefinido pode mudar em futuras versões do Python (por
      exemplo, quando uma nova plataforma ganha suporte oficial ou
      quando é identificada uma diferença entre plataformas
      semelhantes). Atualmente, o valor predefinido será:

      * No Windows: ""ms""

      * Quando "_pack_" está especificado: ""ms"". (Isto está
        descontinuado; veja a documentação de "_pack_".)

      * Caso contrário: ""gcc-sysv""

      "_layout_" já deve estar definido quando "_fields_" é atribuído,
      caso contrário, não terá efeito.

      Adicionado na versão 3.14.

   _anonymous_

      An optional sequence that lists the names of unnamed (anonymous)
      fields. "_anonymous_" must be already defined when "_fields_" is
      assigned, otherwise it will have no effect.

      The fields listed in this variable must be structure or union
      type fields. "ctypes" will create descriptors in the structure
      type that allows accessing the nested fields directly, without
      the need to create the structure or union field.

      Here is an example type (Windows):

         class _U(Union):
             _fields_ = [("lptdesc", POINTER(TYPEDESC)),
                         ("lpadesc", POINTER(ARRAYDESC)),
                         ("hreftype", HREFTYPE)]

         class TYPEDESC(Structure):
             _anonymous_ = ("u",)
             _fields_ = [("u", _U),
                         ("vt", VARTYPE)]

      The "TYPEDESC" structure describes a COM data type, the "vt"
      field specifies which one of the union fields is valid.  Since
      the "u" field is defined as anonymous field, it is now possible
      to access the members directly off the TYPEDESC instance.
      "td.lptdesc" and "td.u.lptdesc" are equivalent, but the former
      is faster since it does not need to create a temporary union
      instance:

         td = TYPEDESC()
         td.vt = VT_PTR
         td.lptdesc = POINTER(some_type)
         td.u.lptdesc = POINTER(some_type)

   It is possible to define sub-subclasses of structures, they inherit
   the fields of the base class.  If the subclass definition has a
   separate "_fields_" variable, the fields specified in this are
   appended to the fields of the base class.

   Structure and union constructors accept both positional and keyword
   arguments.  Positional arguments are used to initialize member
   fields in the same order as they are appear in "_fields_".  Keyword
   arguments in the constructor are interpreted as attribute
   assignments, so they will initialize "_fields_" with the same name,
   or create new attributes for names not present in "_fields_".

class ctypes.CField(*args, **kw)

   Descritor para campos de uma "Structure" ou "Union". Por exemplo:

      >>> class Color(Structure):
      ...     _fields_ = (
      ...         ('red', c_uint8),
      ...         ('green', c_uint8),
      ...         ('blue', c_uint8),
      ...         ('intense', c_bool, 1),
      ...         ('blinking', c_bool, 1),
      ...    )
      ...
      >>> Color.red
      <ctypes.CField 'red' type=c_ubyte, ofs=0, size=1>
      >>> Color.green.type
      <class 'ctypes.c_ubyte'>
      >>> Color.blue.byte_offset
      2
      >>> Color.intense
      <ctypes.CField 'intense' type=c_bool, ofs=3, bit_size=1, bit_offset=0>
      >>> Color.blinking.bit_offset
      1

   Todos os atributos são somente leitura.

   Os objetos "CField" são criados por meio de "_fields_"; não
   instancie a classe diretamente.

   Adicionado na versão 3.14: Anteriormente, os descritores tinham
   apenas os atributos "offset" e "size" e uma representação de string
   legível; a classe "CField" não estava disponível diretamente.

   name

      Nome do campo, como string.

   type

      Tipo do campo, como uma classe ctypes.

   offset
   byte_offset

      Deslocamento do campo, em bytes.

      Para campos de bits, este é o deslocamento da unidade de
      armazenamento alinhada por byte subjacente; veja "bit_offset".

   byte_size

      Tamanho do campo, em bytes.

      Para campos de bits, este é o tamanho da unidade de
      armazenamento subjacente. Normalmente, tem o mesmo tamanho que o
      tipo do campo de bits.

   size

      Para campos não-bit, equivalente a "byte_size".

      Para campos de bits, isto contém um valor compactado de bits
      compatível com versões anteriores que combina "bit_size" e
      "bit_offset". Prefira usar os atributos explícitos em vez disso.

   is_bitfield

      Verdadeiro se este for um campo de bits.

   bit_offset
   bit_size

      A localização de um campo de bits dentro da sua unidade de
      armazenamento, ou seja, dentro dos "byte_size" bytes de memória
      a partir de "byte_offset".

      Para obter o valor do campo, leia a unidade de armazenamento
      como um inteiro, desloque para a esquerda por "bit_offset" e
      acesse os "bit_size" bits menos significativos.

      Para campos não-bit, "bit_offset" é zero e "bit_size" é igual a
      "byte_size * 8".

   is_anonymous

      Verdadeiro se este campo for anônimo, ou seja, contém subcampos
      aninhados que devem ser fundidos em uma estrutura ou união
      contêiner.


Arrays and pointers
-------------------

class ctypes.Array(*args)

   Abstract base class for arrays.

   The recommended way to create concrete array types is by
   multiplying any "ctypes" data type with a non-negative integer.
   Alternatively, you can subclass this type and define "_length_" and
   "_type_" class variables. Array elements can be read and written
   using standard subscript and slice accesses; for slice reads, the
   resulting object is *not* itself an "Array".

   Arrays are generic over the type of their elements.

   _length_

      A positive integer specifying the number of elements in the
      array. Out-of-range subscripts result in an "IndexError". Will
      be returned by "len()".

   _type_

      Specifies the type of each element in the array.

   Array subclass constructors accept positional arguments, used to
   initialize the elements in order.

ctypes.ARRAY(type, length)

   Create an array. Equivalent to "type * length", where *type* is a
   "ctypes" data type and *length* an integer.

   Suavemente descontinuado desde a versão 3.14: In favor of
   multiplication.

class ctypes._Pointer

   Private, abstract base class for pointers.

   Concrete pointer types are created by calling "POINTER()" with the
   type that will be pointed to; this is done automatically by
   "pointer()".

   If a pointer points to an array, its elements can be read and
   written using standard subscript and slice accesses.  Pointer
   objects have no size, so "len()" will raise "TypeError".  Negative
   subscripts will read from the memory *before* the pointer (as in
   C), and out-of-range subscripts will probably crash with an access
   violation (if you're lucky).

   _type_

      Specifies the type pointed to.

   contents

      Returns the object to which to pointer points.  Assigning to
      this attribute changes the pointer to point to the assigned
      object.


Exceções
--------

exception ctypes.ArgumentError

   Esta exceção é levantada quando uma chamada de função externa não
   consegue converter um dos argumentos passados.

exception ctypes.COMError(hresult, text, details)

   Esta exceção é levantada quando uma chamada de método COM falha.

   hresult

      O valor inteiro que representa o código de erro.

   text

      A mensagem de erro.

   details

      A tupla de 5 itens "(descr, source, helpfile, helpcontext,
      progid)".

      *descr* é a descrição textual. *source* é o "ProgID" dependente
      da linguagem para a classe ou aplicação que levantou o erro.
      *helpfile* é o caminho do arquivo de ajuda. *helpcontext* é o
      identificador de contexto de ajuda. *progid* é o "ProgID" da
      interface que definiu o erro.

   Disponibilidade: Windows

   Adicionado na versão 3.14.
