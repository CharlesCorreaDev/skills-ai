Conversão e formação de strings
*******************************

Funções para conversão de números e saída formatada de strings.

int PyOS_snprintf(char *str, size_t size, const char *format, ...)
    * Parte da ABI Estável.*

   Saída não superior a *size* bytes para *str* de acordo com a string
   de formato *format* e os argumentos extras. Veja a página man do
   Unix *snprintf(3)*.

int PyOS_vsnprintf(char *str, size_t size, const char *format, va_list va)
    * Parte da ABI Estável.*

   Saída não superior a *size* bytes para *str* de acordo com o string
   de formato *format* e a variável argumento de lista *va*. Página
   man do Unix *vsnprintf(3)*.

"PyOS_snprintf()" e "PyOS_vsnprintf()" envolvem as funções
"snprintf()" e "vsnprintf()" da biblioteca Standard C. Seu objetivo é
garantir um comportamento consistente em casos extremos, o que as
funções do Standard C não garantem.

Os invólucros garantem que "str[size-1]" seja sempre "'\0'" no
retorno. Eles nunca escrevem mais do que *size* bytes (incluindo o
"'\0'" ao final) em str. Ambas as funções exigem que "str != NULL",
"size > 0", "format != NULL" e "size < INT_MAX". Note que isso
significa que não há equivalente ao "n = snprintf(NULL, 0, ...)" do
C99 que determinaria o tamanho de buffer necessário.

O valor de retorno (*rv*) para essas funções deve ser interpretado da
seguinte forma:

* Quando "0 <= rv < size", a conversão de saída foi bem-sucedida e os
  caracteres de *rv* foram escritos em *str* (excluindo o "'\0'" byte
  em "str[rv]").

* Quando "rv >= size", a conversão de saída foi truncada e um buffer
  com "rv + 1" bytes teria sido necessário para ter sucesso.
  "str[size-1]" é "'\0'" neste caso.

* Quando "rv < 0", a conversão da saída falhou e "str[size-1]" é
  "'\0'" neste caso também, mas o resto de *str* é indefinido. A causa
  exata do erro depende da plataforma subjacente.

As funções a seguir fornecem strings independentes de localidade para
conversões de números.

unsigned long PyOS_strtoul(const char *str, char **ptr, int base)
    * Parte da ABI Estável.*

   Converte a parte inicial da string em "str" para um valor unsigned
   long de acordo com a "base" fornecida, que deve estar entre "2" e
   "36" inclusive, ou ser o valor especial "0".

   Espaços em branco iniciais e diferenciação entre caracteres
   maiúsculos e minúsculos são ignorados. Se "base" for zero, procura
   um "0b", "0o" ou "0x" inicial para informar qual base. Se estes
   estiverem ausentes, o padrão é "10". Base deve ser 0 ou entre 2 e
   36 (inclusive). Se "ptr" não for "NULL", conterá um ponteiro para o
   fim da varredura.

   Se o valor convertido ficar fora do intervalo do tipo de retorno
   correspondente, ocorrerá um erro de intervalo ("errno" é definido
   como "ERANGE") e "ULONG_MAX" será retornado. Se nenhuma conversão
   puder ser realizada, "0" será retornado.

   Veja também a página man do Unix *strtoul(3)*.

   Adicionado na versão 3.2.

long PyOS_strtol(const char *str, char **ptr, int base)
    * Parte da ABI Estável.*

   Converte a parte inicial da string em "str" para um valor long de
   acordo com a "base" fornecida, que deve estar entre "2" e "36"
   inclusive, ou ser o valor especial "0".

   O mesmo que "PyOS_strtoul()", mas retorna um valor long e
   "LONG_MAX" em caso de estouro.

   Veja também a página man do Unix *strtol(3)*.

   Adicionado na versão 3.2.

double PyOS_string_to_double(const char *s, char **endptr, PyObject *overflow_exception)
    * Parte da ABI Estável.*

   Converte uma string "s" em double, levantando uma exceção Python em
   caso de falha. O conjunto de strings aceitas corresponde ao
   conjunto de strings aceito pelo construtor "float()" do Python,
   exceto que "s" não deve ter espaços em branco à esquerda ou à
   direita. A conversão é independente da localidade atual.

   Se "endptr" for "NULL", converte a string inteira. Levanta
   "ValueError" e retorna "-1.0" se a string não for uma representação
   válida de um número de ponto flutuante.

   Se endptr não for "NULL", converte o máximo possível da string e
   define "*endptr" para apontar para o primeiro caractere não
   convertido. Se nenhum segmento inicial da string for a
   representação válida de um número de ponto flutuante, define
   "*endptr" para apontar para o início da string, levanta ValueError
   e retorna "-1.0".

   If "s" represents a value that is too large to store in a float
   (for example, ""1e500"" is such a string on many platforms) then if
   "overflow_exception" is "NULL" return "INFINITY" (with an
   appropriate sign) and don't set any exception.  Otherwise,
   "overflow_exception" must point to a Python exception object; raise
   that exception and return "-1.0".  In both cases, set "*endptr" to
   point to the first character after the converted value.

   Se qualquer outro erro ocorrer durante a conversão (por exemplo, um
   erro de falta de memória), define a exceção Python apropriada e
   retorna "-1.0".

   Adicionado na versão 3.1.

char *PyOS_double_to_string(double val, char format_code, int precision, int flags, int *ptype)
    * Parte da ABI Estável.*

   Converte um *val* double para uma string usando *format_code*,
   *precision* e *flags* fornecidos.

   *format_code* deve ser um entre "'e'", "'E'", "'f'", "'F'", "'g'",
   "'G'" ou "'r'". Para "'r'", a precisão *precision* fornecida deve
   ser 0 e é ignorada. O código de formato "'r'" especifica o formato
   padrão de "repr()".

   *flags* podem ser zero ou mais dos seguintes valores combinados por
   meio do operador OR:

   Py_DTSF_SIGN

      Sempre preceda a string retornada com um caractere de sinal,
      mesmo que *val* não seja negativo.

   Py_DTSF_ADD_DOT_0

      Garante que a string retornada não se pareça com um número
      inteiro.

   Py_DTSF_ALT

      Aplica as regras de formatação "alternativas". Veja a
      documentação para o especificador "'#'" de "PyOS_snprintf()"
      para detalhes.

   Py_DTSF_NO_NEG_0

      Zero negativo é convertido para zerp positivo.

      Adicionado na versão 3.11.

   If *ptype* is non-"NULL", then the value it points to will be set
   to one of the following constants depending on the type of *val*:

   +----------------------------------------------------+----------------------------------------------------+
   | **ptype*                                           | type of *val*                                      |
   |====================================================|====================================================|
   | Py_DTST_FINITE                                     | finite number                                      |
   +----------------------------------------------------+----------------------------------------------------+
   | Py_DTST_INFINITE                                   | infinite number                                    |
   +----------------------------------------------------+----------------------------------------------------+
   | Py_DTST_NAN                                        | not a number                                       |
   +----------------------------------------------------+----------------------------------------------------+

   O valor de retorno é um ponteiro para *buffer* com a string
   convertida ou "NULL" se a conversão falhou. O chamador é
   responsável por liberar a string retornada chamando "PyMem_Free()".

   Adicionado na versão 3.1.

int PyOS_mystricmp(const char *str1, const char *str2)
int PyOS_mystrnicmp(const char *str1, const char *str2, Py_ssize_t size)
    * Parte da ABI Estável.*

   Comparação de strings sem distinção entre maiúsculas e minúsculas.
   Essas funções funcionam de maneira quase idêntica a "strcmp()" e
   "strncmp()" (respectivamente), exceto pelo fato de ignorarem
   maiúsculas e minúsculas em caracteres ASCII.

   Retorna "0" se as strings forem iguais, um valor negativo se *str1*
   for ordenada lexicograficamente antes de *str2*, ou um valor
   positivo se for ordenada depois.

   Nos argumentos *str1* ou *str2*, um byte NUL marca o fim da string.
   Para "PyOS_mystrnicmp()", o argumento *size* fornece o tamanho
   máximo da string, como se NUL estivesse presente no índice
   fornecido por *size*.

   Estas funções não usam a localidade.

int PyOS_stricmp(const char *str1, const char *str2)
int PyOS_strnicmp(const char *str1, const char *str2, Py_ssize_t size)

   Comparação de strings sem distinção entre maiúsculas e minúsculas.

   No Windows, estes são apelidos de "stricmp()" e "strnicmp()",
   respectivamente.

   Em outras plataformas, são apelidos de "PyOS_mystricmp()" e
   "PyOS_mystrnicmp()", respectivamente.


Classificação e conversão de caracteres
***************************************

As macros a seguir fornecem classificação e conversão de caracteres
independentes de localidade (ao contrário da biblioteca padrão C
"ctype.h"). O argumento deve ser um char com ou sem sinal.

Py_ISALNUM(c)

   Retorna verdadeiro se o caractere *c* for um caractere
   alfanumérico.

Py_ISALPHA(c)

   Retorna verdadeiro se o caractere *c* for um caractere alfabético
   ("a-z" e "A-Z").

Py_ISDIGIT(c)

   Retorna verdadeiro se o caractere *c* for um dígito decimal
   ("0-9").

Py_ISLOWER(c)

   Retorna verdadeiro se o caractere *c* for uma letra minúscula do
   ASCII ("a-z").

Py_ISUPPER(c)

   Retorna verdadeiro se o caractere *c* for uma letra maiúscula do
   ASCII ("A-Z").

Py_ISSPACE(c)

   Retorna verdadeiro se o caractere *c* for um caractere de espaço em
   branco (espaço, tabulação, retorno de carro, nova linha, tabulação
   vertical ou alimentação de formulário).

Py_ISXDIGIT(c)

   Retorna verdadeiro se o caractere *c* for um dígito hexadecimal
   ("0-9", "a-f" e "A-F").

Py_TOLOWER(c)

   Retorna o equivalente em minúsculas do caractere *c*.

Py_TOUPPER(c)

   Retorna o equivalente em maiúsculas do caractere *c*.


Bit masks
=========

The following constants are bit masks used by the character
classification macros above:

PY_CTF_ALNUM
PY_CTF_ALPHA
PY_CTF_DIGIT
PY_CTF_LOWER
PY_CTF_SPACE
PY_CTF_UPPER
PY_CTF_XDIGIT

   Values used internally by the "Py_IS*" classification macros above.
   Exposed for backwards compatibility only.

   Suavemente descontinuado desde a versão 3.15.2.
