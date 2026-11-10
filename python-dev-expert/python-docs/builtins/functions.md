Funções embutidas
*****************

O interpretador do Python possui várias funções e tipos embutidos que
sempre estão disponíveis. A seguir listamos todas as funções em ordem
alfabética.

+---------------------------+-------------------------+-------------------------+---------------------------+
| Funções embutidas                                                                                         |
|===========================|=========================|=========================|===========================|
| **A** "abs()" "aiter()"   | **E** "enumerate()"     | **L** "len()" "list()"  | **R** "range()" "repr()"  |
| "all()" "anext()" "any()" | "eval()" "exec()"       | "locals()"  **M**       | "reversed()" "round()"    |
| "ascii()"  **B** "bin()"  | **F** "filter()"        | "map()" "max()"         | **S** "set()" "setattr()" |
| "bool()" "breakpoint()"   | "float()" "format()"    | "memoryview()" "min()"  | "sentinel()" "slice()"    |
| "bytearray()" "bytes()"   | "frozendict()"          | **N** "next()"  **O**   | "sorted()"                |
| **C** "callable()"        | "frozenset()"  **G**    | "object()" "oct()"      | "staticmethod()" "str()"  |
| "chr()" "classmethod()"   | "getattr()" "globals()" | "open()" "ord()"  **P** | "sum()" "super()"  **T**  |
| "compile()" "complex()"   | **H** "hasattr()"       | "pow()" "print()"       | "tuple()" "type()"  **V** |
| **D** "delattr()"         | "hash()" "help()"       | "property()"            | "vars()"  **Z** "zip()"   |
| "dict()" "dir()"          | "hex()"  **I** "id()"   |                         | **_** "__import__()"      |
| "divmod()"                | "input()" "int()"       |                         |                           |
|                           | "isinstance()"          |                         |                           |
|                           | "issubclass()" "iter()" |                         |                           |
+---------------------------+-------------------------+-------------------------+---------------------------+

abs(number, /)

   Retorna o valor absoluto de um número. O argumento pode ser um
   inteiro, um número de ponto flutuante ou um objeto implementando
   "__abs__()". Se o argumento é um número complexo, sua magnitude é
   retornada.

aiter(async_iterable, /)

   Retorna um *iterador assíncrono* para um *iterável assíncrono*.
   Equivalente a chamar "x.__aiter__()".

   Nota: Ao contrário de "iter()", "aiter()" não tem uma variante de 2
   argumentos.

   Adicionado na versão 3.10.

all(iterable, /)

   Retorna "True" se todos os elementos de *iterable* são verdadeiros
   (ou se *iterable* estiver vazio). Equivalente a:

      def all(iterable):
          for elemento in iterable:
              if not elemento:
                  return False
          return True

awaitable anext(async_iterator, /)
awaitable anext(async_iterator, default, /)

   Quando aguardado, retorna o próximo item do *iterador assíncrono*
   fornecido, ou *default* se fornecido e o iterador for *esgotado*.

   Esta é a variante assíncrona do "next()" embutido, e se comporta de
   forma semelhante.

   Isso chama o método "__anext__()" de *async_iterator*, retornando
   um *aguardável*. Ao aguardar isso, retorna o próximo valor do
   iterador. Se *default* for fornecido, ele será retornado se o
   iterador for esgotado, caso contrário, a exceção
   "StopAsyncIteration" será levantada.

   Adicionado na versão 3.10.

any(iterable, /)

   Retorna "True" se algum elemento de *iterable* for verdadeiro. Se
   *iterable* estiver vazio, retorna "False". Equivalente a:

      def any(iterable):
          for elemento in iterable:
              if elemento:
                  return True
          return False

ascii(object, /)

   Como "repr()", retorna uma string contendo uma representação
   imprimível de um objeto, mas faz escape de caracteres não-ASCII na
   string retornada por "repr()" usando sequências de escapes "\x",
   "\u" ou "\U". Isto gera uma string similar ao que é retornado por
   "repr()" no Python 2.

bin(integer, /)

   Converte um número inteiro para uma string de binários prefixada
   com "0b". O resultado é uma expressão Python válida. Se *integer*
   não é um objeto Python "int", ele tem que definir um método
   "__index__()" que devolve um inteiro. Alguns exemplos:

   >>> bin(3)
   '0b11'
   >>> bin(-10)
   '-0b1010'

   Se o prefixo "0b" é desejado ou não, você pode usar uma das
   seguintes maneiras.

   >>> format(14, '#b'), format(14, 'b')
   ('0b1110', '1110')
   >>> f'{14:#b}', f'{14:b}'
   ('0b1110', '1110')

   Veja também "enum.bin()" para representar valores negativos como
   complemento de dois.

   Veja também "format()" para mais informações.

class bool(object=False, /)

   Retorna um valor Booleano, isto é, "True" ou "False". O argumento é
   convertido usando o procedimento de teste de verdade padrão. Se o
   argumento for falso ou foi omitido, isso retorna "False"; senão
   "True". A classe "bool" é uma subclasse de "int" (veja Tipos
   numéricos --- int, float, complex). Ela não pode ser usada para
   criar outra subclasse. Suas únicas instâncias são "False" e "True"
   (veja Tipo booleano - bool).

   Alterado na versão 3.7: O parâmetro agora é somente-posicional

breakpoint(*args, **kws)

   Esta função coloca você no depurador no local da chamada.
   Especificamente, ela chama "sys.breakpointhook()", passando "args"
   e "kws" diretamente. Por padrão, "sys.breakpointhook()" chama
   "pdb.set_trace()" não esperando nenhum argumento. Neste caso, isso
   é puramente uma função de conveniência para você não precisar
   importar "pdb" explicitamente ou digitar mais código para entrar no
   depurador. Contudo, "sys.breakpointhook()" pode ser configurado
   para alguma outra função e "breakpoint()" irá automaticamente
   chamá-la, permitindo você ir para o depurador de sua escolha. Se
   "sys.breakpointhook()" não estiver acessível, esta função vai
   levantar "RuntimeError".

   Por padrão, o comportamento de "breakpoint()" pode ser alterado com
   a variável de ambiente "PYTHONBREAKPOINT". Veja
   "sys.breakpointhook()" para detalhes de uso.

   Observe que isso não é garantido se "sys.breakpointhook()" tiver
   sido substituído.

   Levanta um evento de auditoria "builtins.breakpoint" com o
   argumento "breakpointhook".

   Adicionado na versão 3.7.

class bytearray(source=b'')
class bytearray(source, encoding, errors='strict')

   Retorna um novo vetor de bytes. A classe "bytearray" é uma
   sequência mutável de inteiros no intervalo 0 <= x < 256. Ela tem a
   maior parte dos métodos mais comuns de sequências mutáveis,
   descritas em Tipos sequências mutáveis, assim como a maior parte
   dos métodos que o tipo "bytes" tem, veja Operações com Bytes e
   Bytearray.

   O parâmetro opcional *source* pode ser usado para inicializar o
   vetor de algumas maneiras diferentes:

   * Se é uma *string*, você deve informar o parâmetro *encoding* (e
     opcionalmente, *errors*); "bytearray()" então converte a string
     para bytes usando "str.encode()".

   * Se é um *inteiro*, o vetor terá esse tamanho e será inicializado
     com bytes nulos.

   * Se é um objeto em conformidade com a interface de buffer, um
     buffer somente leitura do objeto será usado para inicializar o
     vetor de bytes.

   * Se é um *iterável*, deve ser um iterável de inteiros no intervalo
     "0 <= x < 256", que serão usados como o conteúdo inicial do
     vetor.

   Sem nenhum argumento, um vetor de tamanho 0 é criado.

   Veja também Tipos de sequência binária --- bytes, bytearray,
   memoryview e Objetos Bytearray.

class bytes(source=b'')
class bytes(source, encoding, errors='strict')

   Retorna um novo objeto "bytes" que é uma sequência imutável de
   inteiros no intervalo "0 <= x < 256". "bytes" é uma versão imutável
   de "bytearray" -- tem os mesmos métodos de objetos imutáveis e o
   mesmo comportamento de índices e fatiamento.

   Consequentemente, argumentos do construtor são interpretados como
   os de "bytearray()".

   Objetos bytes também podem ser criados com literais, veja Literais
   de string e bytes.

   Veja também Tipos de sequência binária --- bytes, bytearray,
   memoryview, Objetos bytes, e Operações com Bytes e Bytearray.

callable(object, /)

   Retorna "True" se o argumento *object* parece ser chamável, "False"
   caso contrário. Se retorna "True", ainda é possível que a chamada
   falhe, mas se é "False", chamar *object* nunca será bem sucedido.
   Note que classes são chamáveis (chamar uma classe devolve uma nova
   instância); instâncias são chamáveis se suas classes possuem um
   método "__call__()".

   Adicionado na versão 3.2: Esta função foi removida na versão 3.0,
   mas retornou no Python 3.2.

chr(codepoint, /)

   Retorna a string representando um caractere com o ponto de código
   Unicode especificado. Por exemplo, "chr(97)" retorna a string
   "'a'", enquanto "chr(8364)" retorna a string "'€'". É o inverso de
   "ord()".

   O intervalo válido para o argumento vai de 0 até 1.114.111
   (0x10FFFF na base 16). Será lançada uma exceção "ValueError" se ele
   estiver fora desse intervalo.

@classmethod

   Transforma um método em um método de classe.

   Um método de classe recebe a classe como um primeiro argumento
   implícito, exatamente como um método de instância recebe a
   instância. Para declarar um método de classe, faça dessa forma:

      class C:
          @classmethod
          def f(cls, arg1, arg2): ...

   O termo "@classmethod" é uma função *decoradora* -- veja Definições
   de função para detalhes.

   Um método de classe pode ser chamado tanto da classe (como em
   "C.f()") quanto da instância (como em "C().f()"). A instância é
   ignorada, exceto por sua classe. Se um método de classe é chamado
   por uma classe derivada, o objeto da classe derivada é passado como
   primeiro argumento implícito.

   Métodos de classe são diferentes de métodos estáticos em C++ ou
   Java. Se você quer saber desses, veja "staticmethod()" nesta seção.
   Para mais informações sobre métodos de classe, consulte A
   hierarquia de tipos padrão.

   Alterado na versão 3.9: Métodos de classe agora podem envolver
   outros *descritores* tal como "property()".

   Alterado na versão 3.10: Métodos de classe agora herdam os
   atributos do método ("__module__", "__name__", "__qualname__",
   "__doc__" e "__annotations__") e têm um novo atributo
   "__wrapped__".

   Descontinuado desde a versão 3.11, removido na versão 3.13: Métodos
   de classe não podem mais envolver outros *descritores* tal como
   "property()".

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1, *, module=None)

   Compila o argumento *source* em código ou objeto AST. Objetos
   código podem ser executados por "exec()" ou "eval()". *source* pode
   ser uma string normal, uma string byte, ou um objeto AST. Consulte
   a documentação do módulo "ast" para saber como trabalhar com
   objetos AST.

   O argumento *filename* deve ser o arquivo de onde o código será
   lido; passe algum valor reconhecível se isso não foi lido de um
   arquivo ("'<string>'" é comumente usado).

   O argumento *mode* especifica qual o tipo de código deve ser
   compilado; pode ser "'exec'" se *source* consiste em uma sequência
   de instruções, "'eval'" se consiste de uma única expressão, ou
   "'single'" se consiste de uma única instrução interativa (neste
   último caso, instruções da expressão que são avaliadas para alguma
   coisa diferente de "None" serão exibidas). Também pode ser
   "'func_type'" se *source* consistir em uma assinatura de tipo de
   função, por exemplo "(int) -> str"; consulte "ast.parse()" para
   mais informações. Este modo exige a passagem de "ast.PyCF_ONLY_AST"
   em *flags*.

   Os argumentos opcionais *flags* e *dont_inherit* controlam quais
   opções do compilador devem ser ativadas e quais recursos futuros
   devem ser permitidos. Se nenhum estiver presente (ou ambos forem
   zero), o código é compilado com os mesmos sinalizadores que afetam
   o código que está chamando "compile()". Se o argumento *flags* for
   fornecido e *dont_inherit* não for (ou for zero), as opções do
   compilador e as instruções futuras especificadas pelo argumento
   *flags* são usadas além daquelas que seriam usadas de qualquer
   maneira. Se *dont_inherit* for um inteiro diferente de zero, então
   o argumento *flags* é -- os sinalizadores (recursos futuros e
   opções do compilador) no código circundante são ignorados.

   Opções de compilador e instruções futuras são especificadas por
   bits, assim pode ocorrer uma operação *OU* bit a bit para
   especificar múltiplas instruções. O sinalizador necessário para
   especificar um dado recurso futuro pode ser encontrado no atributo
   "compiler_flag" na instância "_Feature" do módulo "__future__".
   Sinalizadores de compilador podem ser encontrados no módulo "ast",
   com o prefixo "PyCF_".

   O argumento *optimize* especifica o nível de otimização do
   compilador; o valor padrão de "-1" seleciona o nível de otimização
   do interpretador dado pela opção "-O". Níveis explícitos são "0"
   (nenhuma otimização; "__debug__" é verdadeiro), "1" (instruções
   "assert" são removidas, "__debug__" é falso) ou "2" (strings de
   documentação também são removidas).

   O argumento opcional *module* especifica o nome do módulo. Ele é
   necessário para filtrar avisos de sintaxe sem ambiguidade por nome
   de módulo.

   Esta função levanta "SyntaxError" se o código-fonte compilado for
   inválido, incluindo um *source* que contenha um caractere nulo ou
   que não possa ser decodificado; "ValueError" se o *mode* ou *flags*
   forem inválidos, ou se uma string *source* contiver caracteres
   substitutos; "MemoryError" ou "RecursionError" se *source* for
   complexo demais para analisar ou compilar, por exemplo, uma
   expressão com muitos milhares de operadores alinhados e
   "OverflowError" se *source* for muito grande.

   Se você quer analisar código Python em sua representação AST, veja
   "ast.parse()".

   Levanta um evento de auditoria "compile" com os argumentos
   "source", "filename". Esse evento pode também ser levantando por
   uma compilação implícita.

   Nota:

     Quando compilando uma string com código multi-linhas em modo
     "'single'" ou "'eval'", entrada deve ser terminada por ao menos
     um caractere de nova linhas. Isso é para facilitar a detecção de
     instruções completas e incompletas no módulo "code".

   Aviso:

     É possível quebrar o interpretador Python com uma string
     suficientemente grande/complexa ao compilar para um objeto AST,
     devido limitações do tamanho da pilha no compilador AST do
     Python.

   Alterado na versão 3.2: Permitido o uso de marcadores de novas
   linhas no estilo Windows e Mac. Além disso, em modo "'exec'" a
   entrada não precisa mais terminar com uma nova linha. Também foi
   adicionado o parâmetro *optimize*.

   Alterado na versão 3.5: Anteriormente, "TypeError" era levantada
   quando havia bytes nulos em *source*.

   Alterado na versão 3.8: "ast.PyCF_ALLOW_TOP_LEVEL_AWAIT" agora pode
   ser passado em *flags* para habilitar o suporte em nível superior a
   "await", "async for", e "async with".

   Alterado na versão 3.8: Adicionado suporte para "mode='func_type'".

   Alterado na versão 3.12: "SyntaxError" é levantada, em vez de
   "ValueError", quando bytes nulos são encontrados em *source*.

   Alterado na versão 3.15: Adicionado o parâmetro *module*.

class complex(number=0, /)
class complex(string, /)
class complex(real=0, imag=0)

   Converte uma única string ou número para um número complexo, ou
   cria um número complexo a partir de partes real e imaginária.

   Exemplos:

      >>> complex('+1.23')
      (1.23+0j)
      >>> complex('-4.5j')
      -4.5j
      >>> complex('-1.23+4.5j')
      (-1.23+4.5j)
      >>> complex('\t( -1.23+4.5J )\n')
      (-1.23+4.5j)
      >>> complex('-Infinity+NaNj')
      (-inf+nanj)
      >>> complex(1.23)
      (1.23+0j)
      >>> complex(imag=-4.5)
      -4.5j
      >>> complex(-1.23, 4.5)
      (-1.23+4.5j)

   Se o argumento for uma string, ele deve conter ou a parte real (com
   o mesmo formato usado em "float()") ou uma parte imaginária (com o
   mesmo formato, mas com um sufixo "'j'" ou "'J'"), ou então ambas as
   partes real e imaginária (caso no qual o sinal da parte imaginária
   é obrigatório). A string pode opcionalmente ser cercada por espaços
   em branco e parênteses "'('" e "')'", que são ignorados. A string
   não deve conter espaços em branco entre os símbolos "'+'", "'-'", o
   sufixo "'j'" ou "'J'", e o número decimal. Por exemplo,
   "complex('1+2j')" é ok, mas "complex('1 + 2j')" levanta
   "ValueError". Mais precisamente, após descartar os parênteses e os
   espaços em branco do início e do final, a entrada deve ser conforme
   a regra de produção "complexvalue" da gramática a seguir:

      complexvalue: floatvalue |
                    floatvalue ("j" | "J") |
                    floatvalue sign absfloatvalue ("j" | "J")

   Se o argumento for um número, o construtor serve como uma conversão
   numérica tal qual "int" e "float". Para um objeto Python "x"
   qualquer, "complex(x)" delega para "x.__complex__()". Se
   "__complex__()" não está definido então a chamada é repassada para
   "__float__()". Se "__float__()" não está definido então a chamada
   é, novamente, repassada para "__index__()".

   Se dois argumentos forem passados ou argumentos nomeados forem
   usados, cada argumento pode ser de qualquer tipo numérico
   (incluindo complexo). Se ambos argumentos forem números reais, é
   retornado um número complexo com *real* como parte real e *imag*
   como parte imaginária. Se ambos os argumentos forem números
   complexos, é retornado um número complexo com parte real "real
   .real-imag.imag" e parte imaginária "real.imag+imag.real". Se um
   dos argumentos for um número real, somente a sua parte real é usada
   nas expressões anteriores.

   Veja também "complex.from_number()" que aceita apenas um único
   argumento numérico.

   Se todos os argumentos forem omitidos, retorna "0j".

   O tipo complexo está descrito em Tipos numéricos --- int, float,
   complex.

   Alterado na versão 3.6: Agrupar dígitos com sublinhados como em
   literais de código é permitido.

   Alterado na versão 3.8: Chamadas para "__index__()" se
   "__complex__()" e "__float__()" não estão definidas.

   Descontinuado desde a versão 3.14: Passar um número complexo como
   argumento *real* ou *imag* agora está descontinuado; deve ser
   passado apenas como um único argumento posicional.

delattr(object, name, /)

   Essa função está relacionada com "setattr()". Os argumentos são um
   objeto e uma string. A string deve ser o nome de um dos atributos
   do objeto. A função remove o atributo indicado, desde que o objeto
   permita. Por exemplo, "delattr(x, 'foobar')" é equivalente a "del
   x.foobar". *name* não precisa ser um identificador Python  (veja
   "setattr()").

class dict(**kwargs)
class dict(mapping, /, **kwargs)
class dict(iterable, /, **kwargs)

   Cria um novo dicionário. O objeto "dict" é a classe do dicionário.
   Veja também  Tipos mapeamentos --- dict, frozendict para
   documentação sobre esta classe.

   Para outros contêineres, consulte as classes embutidas
   "frozendict", "list", "set" e "tuple", bem como o módulo
   "collections".

dir()
dir(object, /)

   Sem argumentos, devolve a lista de nomes no escopo local atual. Com
   um argumento, tentará devolver uma lista de atributos válidos para
   esse objeto.

   Se o objeto tiver um método chamado "__dir__()", esse método será
   chamado e deve devolver a lista de atributos. Isso permite que
   objetos que implementam uma função personalizada "__getattr__()" ou
   "__getattribute__()" personalizem a maneira como "dir()" relata
   seus atributos.

   Se o objeto não fornecer "__dir__()", a função tentará o melhor
   possível para coletar informações do atributo "__dict__" do objeto,
   se definido, e do seu objeto de tipo. A lista resultante não está
   necessariamente completa e pode ser imprecisa quando o objeto
   possui um "__getattr__()" personalizado.

   O mecanismo padrão "dir()" se comporta de maneira diferente com
   diferentes tipos de objetos, pois tenta produzir as informações
   mais relevantes e não completas:

   * Se o objeto for um objeto de módulo, a lista conterá os nomes dos
     atributos do módulo.

   * Se o objeto for um objeto de tipo ou classe, a lista conterá os
     nomes de seus atributos e recursivamente os atributos de suas
     bases.

   * Caso contrário, a lista conterá os nomes dos atributos do objeto,
     os nomes dos atributos da classe e recursivamente os atributos
     das classes base da classe.

   A lista resultante é alfabeticamente ordenada. Por exemplo:

   >>> import struct
   >>> dir()   # show the names in the module namespace
   ['__builtins__', '__name__', 'struct']
   >>> dir(struct)   # show the names in the struct module
   ['Struct', '__all__', '__builtins__', '__doc__', '__file__',
    '__initializing__', '__loader__', '__name__', '__package__',
    '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
    'unpack', 'unpack_from']
   >>> class Shape:
   ...     def __dir__(self):
   ...         return ['area', 'perimeter', 'location']
   ...
   >>> s = Shape()
   >>> dir(s)
   ['area', 'location', 'perimeter']

   Nota:

     Como "dir()" é fornecido principalmente como uma conveniência
     para uso em um prompt interativo, ele tenta fornecer um conjunto
     interessante de nomes mais do que tenta fornecer um conjunto de
     nomes definido de forma rigorosa ou consistente, e seu
     comportamento detalhado pode mudar nos lançamentos. Por exemplo,
     os atributos de metaclasse não estão na lista de resultados
     quando o argumento é uma classe.

divmod(a, b, /)

   Recebe dois números (não complexos) como argumentos e retorna um
   par de números que consiste em seu quociente e resto ao usar a
   divisão inteira. Com tipos de operandos mistos, as regras para
   operadores aritméticos binários se aplicam. Para números inteiros,
   o resultado é o mesmo que "(a // b, a % b)". Para números de ponto
   flutuante, o resultado é "(q, a % b)", onde *q* geralmente é
   "math.floor(a / b)", mas pode ser 1 a menos que isso. Em qualquer
   caso, "q * b + a % b" está muito próximo de *a*, se "a % b" é
   diferente de zero, tem o mesmo sinal que *b* e "0 <= abs(a % b) <
   abs(b)".

enumerate(iterable, start=0)

   Devolve um objeto enumerado. *iterable* deve ser uma sequência, um
   *iterador* ou algum outro objeto que suporte a iteração. O método
   "__next__()" do iterador retornado por "enumerate()" devolve uma
   tupla contendo uma contagem (a partir de *start*, cujo padrão é 0)
   e os valores obtidos na iteração sobre *iterable*.

   >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
   >>> list(enumerate(seasons))
   [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
   >>> list(enumerate(seasons, start=1))
   [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

   Equivalente a:

      def enumerate(iterable, start=0):
          n = start
          for elem in iterable:
              yield n, elem
              n += 1

eval(source, /, globals=None, locals=None)

   Parâmetros:
      * **source** ("str" | code object) -- Uma expressão Python.

      * **globals** ("dict" | "frozendict" | "None") -- O espaço de
        nomes global (por padrão, "None").

      * **locals** (*mapping* | "None") -- O espaço de nomes local
        (por padrão, "None").

   Retorna:
      O resultado da expressão avaliada.

   levanta:
      Erros de sintaxe são reportados como exceções.

   Aviso:

     Esta função executa código arbitrário. Chamá-la com entrada
     fornecida pelo usuário não confiável levará a vulnerabilidades de
     segurança.

   O argumento *source* é analisado e avaliado como uma expressão
   Python (tecnicamente, uma lista de expressões), usando os
   dicionários *globals* e *locals* como espaços de nomes global e
   local. Se o dicionário *globals* estiver presente e não contiver um
   valor para a chave "__builtins__", uma referência ao dicionário do
   módulo "builtins" é inserida sob essa chave antes de *source* ser
   analisado. A sobrescrita de "__builtins__" pode ser usada para
   controlar ou alterar os nomes disponíveis, mas isso **não** é um
   mecanismo de segurança: o código executado ainda pode acessar todos
   os embutidos. Se o dicionário *locals* for omitido, o valor
   predefinido é o dicionário *globals*. Se ambos os mapeamentos forem
   omitidos, *source* é executado com os *globals* e *locals* do
   ambiente em que "eval()" é chamada. Note que *eval()* só terá
   acesso aos *escopos aninhados* (*non-locals*) no ambiente que a
   contém se eles já estiverem referenciados no escopo que chama
   "eval()" (por exemplo, através de uma instrução "nonlocal").

   Exemplo:

   >>> x = 1
   >>> eval('x+1')
   2

   >>> eval("1, 2")
   (1, 2)

   Esta função também pode ser usada para executar objetos código
   arbitrários (como os criados por "compile()"). Nesse caso, passe um
   objeto código em vez de uma string. Se o objeto código foi
   compilado com "'exec'" como o argumento *mode*, o valor de retorno
   de "eval()" será "None".

   Dicas: a execução dinâmica de instruções é implementada pela função
   "exec()". As funções "globals()" e "locals()" retornam os
   dicionários global e local atuais, respectivamente, o que pode ser
   útil para serem usados por "eval()" ou "exec()".

   Se a fonte fornecida for uma string, os espaços e tabulações à
   esquerda ou à direita serão removidos.

   Veja "ast.literal_eval()" para uma função para avaliar strings com
   expressões que contêm apenas literais.

   Levanta um evento de auditoria "exec" com o código objeto como
   argumento. Eventos de compilação de código também podem ser
   levantados.

   Alterado na versão 3.13: Os argumentos *globals* e *locals* podem
   agora ser passados como argumentos nomeados.

   Alterado na versão 3.13: A forma de uso do espaço de nomes *locals*
   padrão foi ajustada conforme descrito na função embutida
   "locals()".

   Alterado na versão 3.15: *globals* pode agora ser um "frozendict".

exec(source, /, globals=None, locals=None, *, closure=None)

   Aviso:

     Esta função executa código arbitrário. Chamá-la com entrada
     fornecida pelo usuário não confiável levará a vulnerabilidades de
     segurança.

   Esta função permite a execução dinâmica de código Python. O
   parâmetro *source* deve ser ou uma string ou um objeto código. Se
   for uma string, a mesma é analisada como um conjunto de instruções
   Python, o qual é então executado (exceto caso um erro de sintaxe
   ocorra). [1] Se for um objeto código, ele é simplesmente executado.
   Em todos os casos, espera-se que o código a ser executado seja
   válido como um arquivo de entrada (veja a seção Entrada de arquivo
   no Manual de Referência). Tenha cuidado, pois as instruções
   "nonlocal", "yield" e "return" não podem ser usadas fora das
   definições de funções mesmo dentro do contexto do código passado
   para a função "exec()" . O valor de retorno é sempre "None".

   Em todos os casos, se os parâmetros opcionais são omitidos, o
   código é executado no escopo atual. Se somente *globals* é
   fornecido, deve ser um dicionário (e não uma subclasse de
   dicionário), que será usado tanto para as variáveis globais quanto
   para locais. Se *globals* e *locals* são fornecidos, eles são
   usados para as variáveis globais e locais, respectivamente. Se
   fornecido, *locals* pode ser qualquer objeto de mapeamento. Lembre
   que no nível de módulo, globals e locals são o mesmo dicionário.

   Nota:

     Quando "exec" recebe dois objetos separados como *globals* e
     *locals*, o código será executado como se estivesse embutido em
     uma definição de classe. Isso significa que funções e classes
     definidas no código executado não poderão acessar variáveis que
     sofreram atribuições no escopo mais externo (pois, em uma
     definição de classe, tais variáveis seriam tratadas como
     variáveis de classe).

   Se o dicionário *globals* não contiver um valor para a chave
   "__builtins__", a referência ao dicionário do módulo embutido
   "builtins" é inserida com essa chave. A sobrescrita de
   "__builtins__" pode ser usada para controlar ou alterar os nomes
   disponíveis, mas isso **não** é um mecanismo de segurança: o código
   executado ainda pode acessar todos os embutidos.

   The *closure* argument specifies a closure--a tuple of cellvars.
   It's only valid when *source* is a code object containing *free
   (closure) variables*. The length of the tuple must exactly match
   the length of the code object's "co_freevars" attribute.

   Levanta um evento de auditoria "exec" com o código objeto como
   argumento. Eventos de compilação de código também podem ser
   levantados.

   Nota:

     As funções embutidas "globals()" e "locals()" devolvem os espaços
     de nomes global e local, respectivamente, o que pode ser útil
     para passar adiante e usá-los como segundo ou terceiro argumento
     para "exec()".

   Nota:

     *locals* padrão atua como descrito na função "locals()" abaixo.
     Se você precisa ver os efeitos do código em *locals* após a
     função "exec()" retornar, passe um dicionário *locals* explícito.

   Alterado na versão 3.11: Adicionado o parâmetro *closure*.

   Alterado na versão 3.13: Os argumentos *globals* e *locals* podem
   agora ser passados como argumentos nomeados.

   Alterado na versão 3.13: A forma de uso do espaço de nomes *locals*
   padrão foi ajustada conforme descrito na função embutida
   "locals()".

   Alterado na versão 3.15: *globals* pode agora ser um "frozendict".

filter(function, iterable, /)

   Constrói um iterador a partir dos elementos de *iterable* para os
   quais *function* é verdadeiro. *iterable* pode ser uma sequência,
   um contêiner que com suporte a iteração, ou um iterador. Se
   *function* for "None", a função identidade será usada, isto é,
   todos os elementos de *iterable* que são falsos são removidos.

   Note que "filter(function, iterable)" é equivalente a expressão
   geradora "(item for item in iterable if function(item))" se
   *function* não for "None" e "(item for item in iterable if item)"
   se *function* for "None".

   Veja "itertools.filterfalse()" para a função complementar que
   devolve elementos de *iterable* para os quais *function* é falso.

class float(number=0.0, /)
class float(string, /)

   Retorna um número de ponto flutuante construído a partir de um
   número ou string.

   Exemplos:

      >>> float('+1.23')
      1.23
      >>> float('   -12345\n')
      -12345.0
      >>> float('1e-003')
      0.001
      >>> float('+1E6')
      1000000.0
      >>> float('-Infinity')
      -inf

   Se o argumento for uma string, ele deve conter um número decimal,
   opcionalmente precedido por um sinal e opcionalmente embutido em um
   espaço em branco. O sinal opcional pode ser "'+'" ou "'-'"; um
   sinal "'+'" não tem efeito no valor produzido. O argumento também
   pode ser uma string representando um NaN (não um número) ou
   infinito positivo ou negativo. Mais precisamente, a entrada deve
   estar de acordo com a regra de produção "floatvalue" na seguinte
   gramática, depois que os espaços em branco iniciais e finais forem
   removidos:

      sign:          "+" | "-"
      infinity:      "Infinity" | "inf"
      nan:           "nan"
      digit:         <a Unicode decimal digit, i.e. characters in Unicode general category Nd>
      digitpart:     digit (["_"] digit)*
      number:        [digitpart] "." digitpart | digitpart ["."]
      exponent:      ("e" | "E") [sign] digitpart
      floatnumber:   number [exponent]
      absfloatvalue: floatnumber | infinity | nan
      floatvalue:    [sign] absfloatvalue

   O caso não é significativo, então, por exemplo, "inf", "Inf",
   "INFINITY" e "iNfINity" são todas grafias aceitáveis para o
   infinito positivo.

   Caso contrário, se o argumento é um inteiro ou um número de ponto
   flutuante, um número de ponto flutuante com o mesmo valor (com a
   precisão de ponto flutuante de Python) é retornado. Se o argumento
   está fora do intervalo de um ponto flutuante Python, uma exceção
   "OverflowError" será lançada.

   Para um objeto Python genérico "x", "float(x)" delega para o método
   "x.__float__()". Se "__float__()" não estiver definido, então ele
   delega para o método "__index__()".

   Veja também "float.from_number()" que aceita apenas um argumento
   numérico.

   Se nenhum argumento for fornecido, será retornado "0.0".

   O tipo float é descrito em Tipos numéricos --- int, float, complex.

   Alterado na versão 3.6: Agrupar dígitos com sublinhados como em
   literais de código é permitido.

   Alterado na versão 3.7: O parâmetro agora é somente-posicional

   Alterado na versão 3.8: Chamada para "__index__()" se "__float__()"
   não está definido.

format(value, format_spec='', /)

   Converte um valor *value* em uma representação "formatada",
   controlado por *format_spec*. A interpretação de *format_spec*
   dependerá do tipo do argumento *value*; no entanto há uma sintaxe
   de formatação padrão usada pela maioria dos tipos embutidos:
   Minilinguagem de especificação de formato.

   O *format_spec* padrão é uma string vazia que geralmente produz o
   mesmo efeito que chamar "str(value)".

   Uma chamada de "format(value, format_spec)" é convertida em
   "type(value).__format__(value, format_spec)", que ignora o
   dicionário da instância ao pesquisar o método "__format__()" de
   "value". Uma exceção "TypeError" é levantada se a pesquisa do
   método atingir "object" e o *format_spec* não estiver vazio, ou se
   o *format_spec* ou o valor de retorno não forem strings.

   Alterado na versão 3.4: "object().__format__(format_spec)" levanta
   um "TypeError" se *format_spec* não for uma string vazia.

class frozendict(**kwargs)
class frozendict(mapping, /, **kwargs)
class frozendict(iterable, /, **kwargs)

   Cria um novo dicionário imutável. O objeto "frozendict" é uma
   classe embutida. Veja também Tipos mapeamentos --- dict, frozendict
   para obter a documentação sobre esta classe.

   Para outros contêineres, consulte as classes embutidas "dict",
   "list", "set" e "tuple", bem como o módulo "collections".

   Adicionado na versão 3.15.

class frozenset(iterable=(), /)

   Retorna um novo objeto "frozenset", opcionalmente com elementos
   obtidos de *iteráveis*. "frozenset" é uma classe embutida. Veja
   também Tipo conjuntos --- set, frozenset para documentação sobre
   essa classe.

   Para outros contêineres veja as classes embutidas "set", "list",
   "tuple", e "dict", assim como o módulo "collections".

getattr(object, name, /)
getattr(object, name, default, /)

   Devolve o valor do atributo *name* de *object*. *name* deve ser uma
   string. Se a string é o nome de um dos atributos do objeto, o
   resultado é o valor de tal atributo. Por exemplo, "getattr(x,
   'foobar')" é equivalente a "x.foobar". Se o atributo não existir,
   *default* é devolvido se tiver sido fornecido, caso contrário a
   exceção "AttributeError" é levantada. *name* não precisa ser um
   identificador Python (veja "setattr()").

   Nota:

     Uma vez que desfiguração de nome privado acontece em tempo de
     compilação, deve-se manualmente mutilar o nome de um atributo
     privado (atributos com dois sublinhados à esquerda) para
     recuperá-lo com "getattr()".

globals()

   Retorna o dicionário implementando o espaço de nomes do módulo
   atual. Para código dentro de funções, isso é definido quando a
   função é definida e permanece o mesmo, independentemente de onde a
   função é chamada.

hasattr(object, name, /)

   Os argumentos são um objeto e uma string. O resultado é "True" se a
   string é o nome de um dos atributos do objeto, e "False" se ela não
   for. (Isto é implementado chamando "getattr(object, name)" e vendo
   se levanta um "AttributeError" ou não.)

hash(object, /)

   Retorna o valor hash de um objeto (se houver um). Valores hash são
   números inteiros. Eles são usados para rapidamente comparar chaves
   de dicionários durante uma pesquisa em um dicionário. Valores
   numéricos que ao serem comparados são iguais, possuem o mesmo valor
   hash (mesmo que eles sejam de tipos diferentes, como é o caso de 1
   e 1.0).

   Nota:

     Para objetos com métodos "__hash__()" personalizados, fique
     atento que "hash()" trunca o valor devolvido baseado no
     comprimento de bits da máquina hospedeira.

help()
help(request)

   Invoca o sistema de ajuda embutido. (Esta função é destinada para
   uso interativo.) Se nenhum argumento é passado, o sistema
   interativo de ajuda inicia no interpretador do console. Se o
   argumento é uma string, então a string é pesquisada como o nome de
   um módulo, função, classe, método, palavra-chave, ou tópico de
   documentação, e a página de ajuda é exibida no console. Se o
   argumento é qualquer outro tipo de objeto, uma página de ajuda para
   o objeto é gerada.

   Note que se uma barra(/) aparecer na lista de parâmetros de uma
   função, quando invocando "help()", significa que os parâmetros
   anteriores a barra são apenas posicionais. Para mais informações,
   veja a entrada no FAQ sobre parâmetros somente-posicionais.

   Esta função é adicionada ao espaço de nomes embutido pelo módulo
   "site".

   Alterado na versão 3.4: Mudanças em "pydoc" e "inspect" significam
   que as assinaturas reportadas para chamáveis agora são mais
   compreensíveis e consistentes.

hex(integer, /)

   Converte um número inteiro para uma string hexadecimal em letras
   minúsculas prefixada com "0x". Se *integer* não é um objeto "int"
   do Python, ele tem que definir um método "__index__()" que retorne
   um inteiro. Alguns exemplos:

   >>> hex(255)
   '0xff'
   >>> hex(-42)
   '-0x2a'

   Se você quer converter um número inteiro para uma string
   hexadecimal em letras maiúsculas ou minúsculas, com prefixo ou sem,
   você pode usar qualquer uma das seguintes maneiras:

   >>> '%#x' % 255, '%x' % 255, '%X' % 255
   ('0xff', 'ff', 'FF')
   >>> format(255, '#x'), format(255, 'x'), format(255, 'X')
   ('0xff', 'ff', 'FF')
   >>> f'{255:#x}', f'{255:x}', f'{255:X}'
   ('0xff', 'ff', 'FF')

   Veja também "format()" para mais informações.

   Veja também "int()" para converter uma string hexadecimal para um
   inteiro usando a base 16.

   Nota:

     Para obter uma string hexadecimal de um ponto flutuante, use o
     método "float.hex()".

id(object, /)

   Devolve a "identidade" de um objeto. Ele é um inteiro, o qual é
   garantido que será único e constante para este objeto durante todo
   o seu ciclo de vida. Dois objetos com ciclos de vida não
   sobrepostos podem ter o mesmo valor para "id()".

   Este é o endereço do objeto na memória.

   Levanta um evento de auditoria "builtins.id" com o argumento "id".

input()
input(prompt, /)

   Se o argumento *prompt* estiver presente, escreve na saída padrão
   sem uma nova linha ao final. A função então lê uma linha da fonte
   de entrada, converte a mesma para uma string (removendo o caractere
   de nova linha ao final), e devolve isso. Quando o final do arquivo
   (EOF / end-of-file) é encontrado, um erro "EOFError" é levantado.
   Exemplo:

      >>> s = input('--> ')
      --> Monty Python's Flying Circus
      >>> s
      "Monty Python's Flying Circus"

   Se o módulo "readline" foi carregado, então "input()" usará ele
   para prover edição de linhas elaboradas e funcionalidades de
   histórico.

   Levanta um evento de auditoria "builtins.input" com argumento
   "prompt" antes de ler a entrada.

   Levanta um evento de auditoria "builtins.input/result" com o
   resultado depois de ler a entrada com sucesso.

class int(number=0, /)
class int(string, /, base=10)

   Retorna um objeto do tipo inteiro construído a partir de um número
   ou string, ou retorna "0" caso nenhum argumento seja passado.

   Exemplos:

      >>> int(123.45)
      123
      >>> int('123')
      123
      >>> int('   -12_345\n')
      -12345
      >>> int('FACE', 16)
      64206
      >>> int('0xface', 0)
      64206
      >>> int('01110011', base=2)
      115

   Se o argumento definir um método "__int__()", então "int(x)"
   retorna "x.__int__()". Se *x* definir um método "__index__()",
   então ele retorna "x.__index__()". Para números de ponto flutuante,
   isto trunca o número na direção do zero.

   Se o argumento não for um número ou se *base* for fornecido, então
   o argumento deve ser uma instância de string, "bytes" ou
   "bytearray" representando um inteiro na base *base*. Opcionalmente,
   a string pode ser precedida por "+" ou "-" (sem espaço entre eles),
   ter zeros à esquerda, estar entre espaços em branco e ter
   sublinhados simples intercalados entre os dígitos.

   Uma string de inteiro de base n contém dígitos, cada um
   representando um valor de 0 a n-1. Os valores 0--9 podem ser
   representados por qualquer dígito decimal Unicode. Os valores 10--
   35 podem ser representados por "a" a "z" (ou "A" a "Z"). A *base*
   padrão é 10. As bases permitidas são 0 e 2--36. As strings base-2,
   -8 e -16 podem ser opcionalmente prefixadas com "0b"/"0B",
   "0o"/"0O" ou "0x"/"0X", como acontece com literais inteiros no
   código. Para a base 0, a string é interpretada de maneira
   semelhante a um literal inteiro no código, em que a base real é 2,
   8, 10 ou 16 conforme determinado pelo prefixo. A base 0 também não
   permite zeros à esquerda: "int('010', 0)" não é válido, enquanto
   "int('010')" e "int('010', 8)" são.

   O tipo inteiro está descrito em Tipos numéricos --- int, float,
   complex.

   Alterado na versão 3.4: Se *base* não é uma instância de "int" e o
   objeto *base* tem um método "base.__index__", então esse método é
   chamado para obter um inteiro para a base. Versões anteriores
   usavam "base.__int__" ao invés de "base.__index__".

   Alterado na versão 3.6: Agrupar dígitos com sublinhados como em
   literais de código é permitido.

   Alterado na versão 3.7: O primeiro parâmetro agora é somente-
   posicional.

   Alterado na versão 3.8: Chamada para "__index__()" se "__int__()"
   não está definido.

   Alterado na versão 3.11: Entradas de strings para "int" e
   representações em strings podem ser limitadas para ajudar a evitar
   ataques de negação de serviço. Uma exceção "ValueError" é levantada
   quando o limite é excedido durante a conversão de uma string em um
   "int" ou quando a conversão de um "int" em uma string excede o
   limite. Consulte a documentação sobre limitação de comprimento de
   conversão de string em inteiro.

   Alterado na versão 3.14: "int()" não delega mais ao método
   "__trunc__()".

isinstance(object, classinfo, /)

   Retorna "True" se o argumento *object* é uma instância do argumento
   *classinfo*, ou de uma subclasse dele (direta, indireta ou
   *virtual*). Se *object* não é um objeto do tipo dado, a função
   sempre devolve "False". Se *classinfo* é uma tupla de tipos de
   objetos (ou recursivamente, como outras tuplas) ou um Tipo União de
   vários tipos, retorna "True" se *object* é uma instância de
   qualquer um dos tipos. Se *classinfo* não é um tipo ou tupla de
   tipos ou outras tuplas, é levantada uma exceção "TypeError".
   "TypeError" pode não ser levantada por um tipo inválido se uma
   verificação anterior for bem-sucedida.

   Alterado na versão 3.10: *classinfo* pode ser um Tipo União.

issubclass(cls, classinfo, /)

   Retorna "True" se *cls* for uma subclasse (direta, indireta ou
   *virtual*) de *classinfo*. Uma classe é considerada uma subclasse
   de si mesma. *classinfo* pode ser uma tupla de objetos de classe
   (ou recursivamente, outras tuplas) ou um Tipo União, caso em que
   retorna "True" se *cls* for uma subclasse de qualquer entrada em
   *classinfo*. Em qualquer outro caso, é levantada uma exceção
   "TypeError".

   Alterado na versão 3.10: *classinfo* pode ser um Tipo União.

iter(iterable, /)
iter(callable, sentinel, /)

   Retorna um objeto *iterador*. O primeiro argumento é interpretado
   muito diferentemente dependendo da presença do segundo argumento.
   Sem um segundo argumento, o primeiro argumento deve ser uma coleção
   de objetos com suporte ao protocolo *iterável* (o método
   "__iter__()"), ou ele deve ter suporte ao protocolo de sequência (o
   método "__getitem__()" com argumentos inteiros começando em "0").
   Se ele não tem suporte nenhum desses protocolos, uma "TypeError" é
   levantada. Se o segundo argumento, *sentinel*, é fornecido, então o
   primeiro argumento deve ser um objeto chamável. O iterador criado
   neste caso irá chamar *callable* sem nenhum argumento para cada
   chamada para o seu método "__next__()"; se o valor devolvido é
   igual a *sentinel*, então "StopIteration" será levantado, caso
   contrário o valor será devolvido.

   Veja também Tipos relacionados a iteração.

   Uma aplicação útil da segunda forma de "iter()" é para construir um
   bloco de leitura. Por exemplo, ler blocos de comprimento fixo de um
   arquivo binário de banco de dados até que o final do arquivo seja
   atingido:

      from functools import partial
      with open('meusdados.db', 'rb') as f:
          for bloco in iter(partial(f.read, 64), b''):
              process_block(bloco)

len(object, /)

   Devolve o comprimento (o número de itens) de um objeto. O argumento
   pode ser uma sequência (tal como uma string, bytes, tupla, lista,
   ou um intervalo) ou uma coleção (tal como um dicionário, conjunto,
   ou conjunto imutável).

   "len" levanta "OverflowError" em tamanhos maiores que
   "sys.maxsize", tal como "range(2 ** 100)".

class list(iterable=(), /)

   Ao invés de ser uma função, "list" é na verdade um tipo de
   sequência mutável, conforme documentado em Listas e Tipos
   sequências --- list, tuple, range.

locals()

   Retorna um objeto de mapeamento representando a tabela de símbolos
   atual, com nomes de variáveis como as chaves, e as referências às
   quais cada variável está atrelada no momento como os valores.

   Em um escopo de módulo, assim como quando usando "exec()" ou
   "eval()" com um único espaço de nomes, esta função retorna o mesmo
   espaço de nomes que "globals()".

   Em um escopo de classe, ela retorna o espaço de nomes que será
   passado para o construtor da metaclasse.

   Quando usando "exec()" ou "eval()" com argumentos de espaço local e
   global distintos, ela retorna o espaço de nomes local passado na
   chamada.

   Em todos os casos acima, cada chamada a "locals()" em um dado
   quadro de execução vai retornar o *mesmo* objeto de mapeamento.
   Mudanças feitas através do objeto de mapeamento retornado por
   "locals()" serão visíveis tal qual variáveis locais atribuídas,
   reatribuídas ou deletadas, e atribuir, reatribuir ou deletar
   variáveis locais afetará imediatamente o conteúdo do objeto de
   mapeamento retornado.

   Em contraste aos casos acima, em um *escopo otimizado* (incluindo
   funções, geradores e corrotinas), cada chamada a "locals()" retorna
   um dicionário novo contendo as ligações atuais das variáveis locais
   da função e de quaisquer células com referências não-locais. Nesse
   caso, mudanças em ligações de nomes feitas através do dicionário
   retornado *não* são escritas de volta nas variáveis locais
   correspondentes nem nas células com referências não-locais, e
   atribuir, reatribuir ou deletar variáveis locais e células com
   referências não-locais *não* afeta o conteúdo dos dicionários que
   já foram retornados.

   Chamar a função "locals()" como parte de uma compreensão em uma
   função, gerador ou corrotina é equivalente a chamá-la no escopo que
   contém a compreensão, exceto que as variáveis de iteração
   inicializadas da compreensão serão incluídas. Em outros escopos,
   essa função se comporta como se a compreensão estivesse executando
   como uma função aninhada.

   Chamar a função "locals()" como parte de uma expressão geradora é
   equivalente a chamá-la em uma função geradora aninhada.

   Alterado na versão 3.12: O comportamento de "locals()" em uma
   compreensão foi atualizado conforme descrito na **PEP 709**.

   Alterado na versão 3.13: Como parte da **PEP 667**, o que acontece
   após a mutação de objetos de mapeamento retornados desta função
   está agora definido. O comportamento em *escopos otimizados* agora
   é o descrito acima. Além de estar definido, o comportamento em
   outros escopos não foi modificado em relação aos comportamentos em
   versões passadas.

map(function, iterable, /, *iterables, strict=False)

   Devolve um iterador que aplica *function* para cada item de
   *iterable*, gerando os resultados. Se argumentos *iterables*
   adicionais são passados, *function* deve ter a mesma quantidade de
   argumentos e ela é aplicada aos itens de todos os iteráveis em
   paralelo. Com múltiplos iteráveis, o iterador para quando o
   iterador mais curto é *esgotado*. Se *strict* for "True" e um dos
   iteráveis for esgotado antes dos outros, um "ValueError" será
   levanta. Para casos onde os parâmetros de entrada da função já
   estão organizados em tuplas, veja "itertools.starmap()".

   Alterado na versão 3.14: Adicionado o parâmetro *track*.

max(iterable, /, *, key=None)
max(iterable, /, *, default, key=None)
max(arg1, arg2, /, *args, key=None)

   Devolve o maior item em um iterável ou o maior de dois ou mais
   argumentos.

   Se um argumento posicional é fornecido, ele deve ser um *iterável*.
   O maior item no iterável é retornado. Se dois ou mais argumentos
   posicionais são fornecidos, o maior dos argumentos posicionais é
   devolvido.

   Existem dois parâmetros somente-nomeados opcionais. O parâmetro
   *key* especifica uma função de ordenamento de um argumento, como
   aquelas usadas por "list.sort()". O parâmetro *default* especifica
   um objeto a ser devolvido se o iterável fornecido estiver vazio. Se
   o iterável estiver vazio, e *default* não foi fornecido, uma
   exceção "ValueError" é levantada.

   Se múltiplos itens são máximos, a função devolve o primeiro
   encontrado. Isto é consistente com outras ferramentas de
   ordenamento que preservam a estabilidade, tais como
   "sorted(iterable, key=keyfunc, reverse=True)[0]" e
   "heapq.nlargest(1, iterable, key=keyfunc)".

   Alterado na versão 3.4: Adicionado o parâmetro *default* somente-
   nomeado.

   Alterado na versão 3.8: O valor de *key* pode ser "None".

class memoryview(object)

   Devolve um objeto de "visão da memória" criado a partir do
   argumento fornecido. Veja Visões de memória para mais informações.

min(iterable, /, *, key=None)
min(iterable, /, *, default, key=None)
min(arg1, arg2, /, *args, key=None)

   Devolve o menor item de um iterável ou o menor de dois ou mais
   argumentos.

   Se um argumento posicional é fornecido, ele deve ser um *iterável*.
   O menor item no iterável é devolvido. Se dois ou mais argumentos
   posicionais são fornecidos, o menor dos argumentos posicionais é
   devolvido.

   Existem dois parâmetros somente-nomeados opcionais. O parâmetro
   *key* especifica uma função de ordenamento de um argumento, como
   aquelas usadas por "list.sort()". O parâmetro *default* especifica
   um objeto a ser devolvido se o iterável fornecido estiver vazio. Se
   o iterável estiver vazio, e *default* não foi fornecido, uma
   exceção "ValueError" é levantada.

   Se múltiplos itens são mínimos, a função devolve o primeiro
   encontrado. Isto é consistente com outras ferramentas de
   ordenamento que preservam a estabilidade, tais como
   "sorted(iterable, key=keyfunc)[0]" e "heapq.nsmallest(1, iterable,
   key=keyfunc)".

   Alterado na versão 3.4: Adicionado o parâmetro *default* somente-
   nomeado.

   Alterado na versão 3.8: O valor de *key* pode ser "None".

next(iterator, /)
next(iterator, default, /)

   Recupera o próximo item do *iterador* chamando o seu método
   "__next__()". Se *default* foi fornecido, ele é devolvido caso o
   iterador tenha sido *esgotado*, caso contrário "StopIteration" é
   levantada.

class object

   Esta é a classe base definitiva de todas as outras classes. Ela tem
   métodos que são comuns a todas as instâncias de classes Python.
   Quando o construtor é chamado, ele retorna um novo objeto sem
   características. O construtor não aceita nenhum argumento.

   Nota:

     Instâncias de "object" *não* têm atributos "__dict__", então você
     não pode atribuir atributos arbitrários a uma instância de
     "object".

oct(integer, /)

   Converte um número inteiro para uma string em base octal, prefixada
   com "0o". O resultado é uma expressão Python válida. Se *integer*
   não for um objeto "int" Python, ele tem que definir um método
   "__index__()" que devolve um inteiro. Por exemplo:

   >>> oct(8)
   '0o10'
   >>> oct(-56)
   '-0o70'

   Se você quiser converter um número inteiro para uma string octal,
   com o prefixo "0o" ou não, você pode usar qualquer uma das formas a
   seguir.

   >>> '%#o' % 10, '%o' % 10
   ('0o12', '12')
   >>> format(10, '#o'), format(10, 'o')
   ('0o12', '12')
   >>> f'{10:#o}', f'{10:o}'
   ('0o12', '12')

   Veja também "format()" para mais informações.

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

   Abre *file* e retorna um *objeto arquivo* correspondente. Se o
   arquivo não puder ser aberto, uma "OSError" é levantada. Veja Lendo
   e escrevendo arquivos para mais exemplos de como usar esta função.

   *file* é um *objeto caminho ou similar* fornecendo o caminho
   (absoluto ou relativo ao diretório de trabalho atual) do arquivo
   que será aberto, ou de um inteiro descritor de arquivo a ser
   manipulado (Se um descritor de arquivo é fornecido, ele é fechado
   quando o objeto de I/O retornado é fechado, a não ser que *closefd*
   esteja marcado como "False").

   *mode* é uma string opcional que especifica o modo no qual o
   arquivo é aberto. O valor padrão é "'r'", o qual significa abrir
   para leitura em modo texto. Outros valores comuns são "'w'" para
   escrever (truncando o arquivo se ele já existe), "'x'" para criação
   exclusiva e "'a'" para anexar (o qual em *alguns* sistemas Unix,
   significa que *todas* as escritas anexam ao final do arquivo
   independentemente da posição de busca atual). No modo texto, se
   *encoding* não for especificada, UTF-8 é usado por padrão; se Modo
   UTF-8 do Python estiver desabilitado, "locale.getencoding()" é
   chamada para obter a codificação da localidade atual (Para ler e
   escrever bytes diretamente, use o modo binário e não especifique
   *encoding*). Os modos disponíveis são:

   +-----------+-----------------------------------------------------------------+
   | Caractere | Significado                                                     |
   |===========|=================================================================|
   | "'r'"     | abre para leitura (padrão)                                      |
   +-----------+-----------------------------------------------------------------+
   | "'w'"     | abre para escrita, truncando o arquivo primeiro (removendo tudo |
   |           | o que estiver contido no mesmo)                                 |
   +-----------+-----------------------------------------------------------------+
   | "'x'"     | abre para criação exclusiva, falhando caso o arquivo exista     |
   +-----------+-----------------------------------------------------------------+
   | "'a'"     | abre para escrita, anexando ao final do arquivo caso o mesmo    |
   |           | exista                                                          |
   +-----------+-----------------------------------------------------------------+
   | "'b'"     | modo binário                                                    |
   +-----------+-----------------------------------------------------------------+
   | "'t'"     | modo texto (padrão)                                             |
   +-----------+-----------------------------------------------------------------+
   | "'+'"     | aberto para atualização (leitura e escrita)                     |
   +-----------+-----------------------------------------------------------------+

   O modo padrão é "'r'" (abre para leitura de texto, um sinônimo de
   "'rt'"). Modos "'w+'" e "'w+b'" abrem e truncam o arquivo. Modos
   "'r+'" e "'r+b'" abrem o arquivo sem truncar o mesmo.

   Conforme mencionado em Visão Geral, Python diferencia entre
   entrada/saída binária e de texto. Arquivos abertos em modo binário
   (incluindo "'b'" no parâmetro *mode*) retornam o conteúdo como
   objetos "bytes" sem usar nenhuma decodificação. No modo texto (o
   padrão, ou quando "'t'" é incluído no parâmetro *mode*), o conteúdo
   do arquivo é retornado como "str", sendo os bytes primeiramente
   decodificados usando a codificação padrão ou usando a codificação
   definida em *encoding* se fornecida.

   Nota:

     Python não depende da noção básica do sistema operacional sobre
     arquivos de texto; todo processamento é feito pelo próprio
     Python, e é então independente de plataforma.

   *buffering* é um número inteiro opcional usado para definir a
   política de buffering. Passe 0 para desativar o buffer (permitido
   apenas no modo binário), 1 para selecionar o buffer de linha
   (usável apenas ao gravar no modo de texto) e um inteiro > 1 para
   indicar o tamanho em bytes de um buffer de bloco de tamanho fixo.
   Observe que especificar um tamanho de buffer dessa maneira se
   aplica a E/S com buffer binário, mas "TextIOWrapper" (ou seja,
   arquivos abertos com "mode='r+'") teriam outro buffer. Para
   desabilitar o buffer em "TextIOWrapper", considere usar o
   sinalizador "write_through" para "io.TextIOWrapper.reconfigure()".
   Quando nenhum argumento *buffering* é fornecido, a política de
   buffering padrão funciona da seguinte forma:

   * Arquivos binários são armazenados em buffer em blocos de tamanho
     fixo; o tamanho do buffer é "max(min(blocksize, 8 MiB),
     DEFAULT_BUFFER_SIZE)" quando o tamanho do bloco do dispositivo
     está disponível. Na maioria dos sistemas, o buffer normalmente
     tem 128 quilobytes de comprimento.

   * Arquivos de texto "interativos" (arquivos para os quais
     "isatty()" retornam "True") usam buffering de linha. Outros
     arquivos de texto usam a política descrita acima para arquivos
     binários.

   *encoding* é o nome da codificação usada para codificar ou
   decodificar o arquivo. Isto deve ser usado apenas no modo texto. A
   codificação padrão é UTF-8; se Modo UTF-8 do Python estiver
   desabilitado, o padrão depende da plataforma (o que
   "locale.getencoding()" retornar). Qualquer *codificação do texto*
   suportada pelo Python pode ser usada, e "encoding="locale""
   especifica a codificação da localidade atual explicitamente. Veja o
   módulo "codecs" para a lista de codificações suportadas.

   *errors* é uma string opcional que especifica como erros de
   codificação e de decodificação devem ser tratados — isso não pode
   ser utilizado no modo binário. Uma variedade de tratadores de erro
   padrão estão disponíveis, apesar que qualquer nome para tratamento
   de erro registrado com "codecs.register_error()" também é válido.
   Os nomes padrões podem ser encontrados em Error Handlers.

   *newline* determina como analisar caracteres de nova linha do
   fluxo. Ele pode ser "None", "''", "'\n'", "'\r'" e "'\r\n'". Ele
   funciona da seguinte forma:

   * Ao ler a entrada do fluxo, se *newline* for "None", o modo
     universal de novas linhas será ativado. As linhas na entrada
     podem terminar em "'\n'", "'\r'" ou "'\r\n'", e são traduzidas
     para "'\n'" antes de retornar ao chamador. Se for "''", o modo de
     novas linhas universais será ativado, mas as terminações de linha
     serão retornadas ao chamador sem tradução. Se houver algum dos
     outros valores legais, as linhas de entrada são finalizadas
     apenas pela string especificada e a finalização da linha é
     retornada ao chamador sem tradução.

   * Ao gravar a saída no fluxo, se *newline* for "None", quaisquer
     caracteres "'\n'" gravados serão traduzidos para o separador de
     linhas padrão do sistema, "os.linesep". Se *newline* for "''" ou
     "'\n'", nenhuma tradução ocorrerá. Se *newline* for um dos outros
     valores legais, qualquer caractere "'\n'" escrito será traduzido
     para a string especificada.

   Se *closefd* for "False" e um descritor de arquivo em vez de um
   nome de arquivo for fornecido, o descritor de arquivo subjacente
   será mantido aberto quando o arquivo for fechado. Se um nome de
   arquivo for fornecido *closefd* deve ser "True" (o padrão), caso
   contrário, um erro será levantado.

   Um abridor personalizado pode ser usado passando um chamável como
   *opener*. O descritor de arquivo subjacente para o objeto arquivo é
   obtido chamando *opener* com (*file*, *flags*). *opener* deve
   retornar um descritor de arquivo aberto (passando "os.open" como
   *opener* resulta em funcionalidade semelhante à passagem de
   "None").

   O arquivo recém-criado é non-inheritable.

   O exemplo a seguir usa o parâmetro dir_fd da função "os.open()"
   para abrir um arquivo relativo a um determinado diretório:

      >>> import os
      >>> dir_fd = os.open('algum_dir', os.O_RDONLY)
      >>> def opener(path, flags):
      ...     return os.open(path, flags, dir_fd=dir_fd)
      ...
      >>> with open('spamspam.txt', 'w', opener=opener) as f:
      ...     print('Isso será escrito para algum_dir/spamspam.txt', file=f)
      ...
      >>> os.close(dir_fd)  # não deixe vazar um descritor de arquivo

   O tipo de *objeto arquivo* retornado pela função "open()" depende
   do modo. Quando "open()" é usado para abrir um arquivo no modo
   texto ("'w'", "'r'", "'wt'", "'rt'", etc.), retorna uma subclasse
   de "io.TextIOBase" (especificamente "io.TextIOWrapper"). Quando
   usada para abrir um arquivo em modo binário com buffer, a classe
   retornada é uma subclasse de "io.BufferedIOBase". A classe exata
   varia: no modo binário de leitura, ele retorna uma
   "io.BufferedReader"; nos modos binário de gravação e binário
   anexado, ele retorna um "io.BufferedWriter" e, no modo
   leitura/gravação, retorna um "io.BufferedRandom". Quando o buffer
   está desativado, o fluxo bruto, uma subclasse de "io.RawIOBase",
   "io.FileIO", é retornado.

   Veja também os módulos de para lidar com arquivos, tais como
   "fileinput", "io" (onde "open()" é declarado), "os", "os.path",
   "tempfile" e "shutil".

   Levanta um evento de auditoria "open" com os argumentos "path",
   "mode", "flags".

   Os argumentos "mode" e "flags" podem ter sido modificados ou
   inferidos a partir da chamada original.

   Alterado na versão 3.3:

   * O parâmetro *opener* foi adicionado.

   * O modo "'x'" foi adicionado.

   * "IOError" costumava ser levantada, agora ela é um apelido para
     "OSError".

   * "FileExistsError" agora é levantado se o arquivo aberto no modo
     de criação exclusivo ("'x'") já existir.

   Alterado na versão 3.4:

   * O arquivo agora é não herdável.

   Alterado na versão 3.5:

   * Se a chamada de sistema é interrompida e o tratador de sinal não
     levanta uma exceção, a função agora tenta novamente a chamada de
     sistema em vez de levantar uma exceção "InterruptedError"
     (consulte **PEP 475** para entender a justificativa).

   * O tratador de erros "'namereplace'" foi adicionado.

   Alterado na versão 3.6:

   * Suporte adicionado para aceitar objetos implementados
     "os.PathLike".

   * No Windows, a abertura de um buffer do console pode retornar uma
     subclasse de "io.RawIOBase" que não seja "io.FileIO".

   Alterado na versão 3.11: O modo "'U'" foi removido.

   Alterado na versão 3.15: O UTF-8 agora é a codificação padrão, em
   vez de uma codificação de localidade dependente da plataforma
   (**PEP 686**).

ord(character, /)

   Retorna o valor ordinal de um caractere.

   Se o argumento for uma string de um caractere, retorna o ponto de
   código Unicode desse caractere.. Por exemplo, "ord('a')" retorna o
   número inteiro "97" e "ord('€')" (sinal do Euro) retorna "8364".
   Este é o inverso de "chr()".

   Se o argumento for um objeto "bytes" ou "bytearray" de comprimento
   1, retorna seu valor de byte único. Por exemplo, "ord(b'a')"
   retorna o inteiro "97".

pow(base, exp, mod=None)

   Retorna *base* à potência de *exp*; se *mod* estiver presente,
   retorna *base* à potência *exp*, módulo *mod* (calculado com mais
   eficiência do que "pow(base, exp) % mod"). A forma de dois
   argumentos "pow(base, exp)" é equivalente a usar o operador de
   potência: "base**exp".

   Quando argumentos são tipos numéricos embutidos com tipos de
   operandos mistos, aplicam-se as regras de coerção para operadores
   aritméticos binários. Para operandos "int", o resultado tem o mesmo
   tipo que os operandos (após coerção), a menos que o segundo
   argumento seja negativo; nesse caso, todos os argumentos são
   convertidos em ponto flutuante e um resultado ponto flutuante é
   entregue. Por exemplo, "pow(10, 2)" retorna "100", mas "pow(10,
   -2)" retorna "0.01". Para uma base negativa do tipo "int" ou
   "float" e um expoente não integral, um resultado complexo é
   entregue. Por exemplo, "pow(-9, 0.5)" retorna um valor próximo a
   "3j". Enquanto isso, para uma base negativa do tipo "int" ou
   "float" com um expoente integral, um resultado de ponto flutuante é
   retornado. Por exemplo, "pow(-9, 2.0)" retorna "81.0".

   Para operandos "int" *base* e *exp*, se *mod* estiver presente,
   *mod* também deve ser do tipo inteiro e *mod* deve ser diferente de
   zero. Se *mod* estiver presente e *exp* for negativo, *base* deve
   ser relativamente primo para *mod*. Nesse caso, "pow(inv_base,
   -exp, mod)" é retornado, onde *inv_base* é um inverso ao *base*
   módulo *mod*.

   Aqui está um exemplo de computação de um inverso para "38" módulo
   "97":

      >>> pow(38, -1, mod=97)
      23
      >>> 23 * 38 % 97 == 1
      True

   Alterado na versão 3.8: Para operandos "int", a forma de três
   argumentos de "pow" agora permite que o segundo argumento seja
   negativo, permitindo o cálculo de inversos modulares.

   Alterado na versão 3.8: Permite argumentos de palavra reservada.
   Anteriormente, apenas argumentos posicionais eram suportados.

print(*objects, sep=' ', end='\n', file=None, flush=False)

   Exibe *objects* no fluxo de texto *arquivo*, separado por *sep* e
   seguido por *end*. *sep*, *end*, *file* e *flush*, se houver, devem
   ser fornecidos como argumentos nomeados.

   Todos os argumentos que não são nomeados são convertidos em strings
   como "str()" faz e gravados no fluxo, separados por *sep* e
   seguidos por *end*. *sep* e *end* devem ser strings; eles também
   podem ser "None", o que significa usar os valores padrão. Se nenhum
   *object* for fornecido, "print()" escreverá apenas *end*.

   O argumento *file* deve ser um objeto com um método
   "write(string)"; se ele não estiver presente ou "None", então
   "sys.stdout" será usado. Como argumentos exibidos no console são
   convertidos para strings de texto, "print()" não pode ser usado com
   objetos arquivo em modo binário. Para esses casos, use
   "file.write(...)" ao invés.

   O buffer de saída geralmente é determinado por *arquivo*. No
   entanto, se *flush* for verdadeiro, o fluxo será descarregado à
   força.

   Alterado na versão 3.3: Adicionado o argumento nomeado *flush*.

class property(fget=None, fset=None, fdel=None, doc=None)

   Retorna um atributo de propriedade.

   *fget* é uma função para obter o valor de um atributo. *fset* é uma
   função para definir um valor para um atributo. *fdel* é uma função
   para deletar um valor de um atributo. E *doc* cria um docstring
   para um atributo.

   Um uso comum é para definir um atributo gerenciável "x":

      class C:
          def __init__(self):
              self._x = None

          def getx(self):
              return self._x

          def setx(self, valor):
              self._x = valor

          def delx(self):
              del self._x

          x = property(getx, setx, delx, "Eu sou a propriedade de 'x'.")

   Se *c* é uma instância de *C*, "c.x" irá invocar o método getter,
   "c.x = valor" irá invocar o método setter, e "del c.x" o método
   deleter.

   Se fornecido, *doc* será a docstring do atributo definido por
   property. Caso contrário, a property copiará a docstring de *fget*
   (se ela existir). Isso torna possível criar facilmente propriedades
   apenas para leitura usando "@property" como um *decorador*:

      class Parrot:
          def __init__(self):
              self._voltagem = 100000

          @property
          def voltagem(self):
              """Obtém a voltagem atual."""
              return self._voltagem

   O decorador "@property" transforma o método "voltage()" em um
   "getter" para um atributo somente leitura com o mesmo nome, e
   define a docstring de *voltage* para "Get the current voltage."

   @getter

   @setter

   @deleter

      Um objeto property possui métodos "getter", "setter" e "deleter"
      usáveis como decoradores, que criam uma cópia da property com o
      assessor correspondente a função definida para a função com
      decorador. Isso é explicado melhor com um exemplo:

         class C:
             def __init__(self):
                 self._x = None

             @property
             def x(self):
                 """Sou a propriedade de 'x'."""
                 return self._x

             @x.setter
             def x(self, value):
                 self._x = value

             @x.deleter
             def x(self):
                 del self._x

      Esse código é exatamente equivalente ao primeiro exemplo. Tenha
      certeza de nas funções adicionais usar o mesmo nome que a
      property original ("x" neste caso).

      O objeto property retornado também tem os atributos "fget",
      "fset", e "fdel" correspondendo aos argumentos do construtor.

   Alterado na versão 3.5: Agora é possível escrever nas docstrings de
   objetos property.

   __name__

      Atributo que contém o nome da propriedade. O nome da propriedade
      pode ser alterado em tempo de execução.

      Adicionado na versão 3.13.

class range(stop, /)
class range(start, stop, step=1, /)

   Em vez de ser uma função, "range" é realmente um tipo de sequência
   imutável, conforme documentado em Intervalos e Tipos sequências ---
   list, tuple, range.

repr(object, /)

   Return a string containing a printable representation of an object.
   For many types, this function makes an attempt to return a string
   that would yield an object with the same value when passed to
   "eval()"; otherwise, the representation is a string enclosed in
   angle brackets that contains the name of the type of the object
   together with additional information often including the name and
   address of the object.  A class can control what this function
   returns for its instances by defining a "__repr__()" method.

   Esta classe possui uma representação personalizada que pode ser
   executada:

      class Pessoa:
         def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

         def __repr__(self):
            return f"Pessoa({self.nome!r}, {self.idade!r})"

reversed(object, /)

   Retorna um *iterador* reverso. *seq* deve ser um objeto que possui
   o método "__reversed__()" ou suporta o protocolo de sequência (o
   método "__len__()" e o método "__getitem__()" com argumentos
   inteiros começando em "0").

round(number, ndigits=None)

   Retorna *number* arredondado para *ndigits* precisão após o ponto
   decimal. Se *ndigits* for omitido ou for "None", ele retornará o
   número inteiro mais próximo de sua entrada.

   Para os tipos embutidos com suporte a "round()", os valores são
   arredondados para o múltiplo mais próximo de 10 para a potência de
   menos *ndigit*; se dois múltiplos são igualmente próximos, o
   arredondamento é feito para a opção par (por exemplo, "round(0.5)"
   e "round(-0.5)" são "0" e "round(1.5)" é "2"). Qualquer valor
   inteiro é válido para *ndigits* (positivo, zero ou negativo). O
   valor de retorno é um número inteiro se *ndigits* for omitido ou
   "None". Caso contrário, o valor de retorno tem o mesmo tipo que
   *number*.

   Para um objeto Python geral "number", "round" delega para
   "number.__round__".

   Nota:

     O comportamento de "round()" para pontos flutuantes pode ser
     surpreendente: por exemplo, "round(2.675, 2)" fornece "2.67" em
     vez do esperado "2.68". Isso não é um bug: é resultado do fato de
     que a maioria das frações decimais não pode ser representada
     exatamente como um ponto flutuante. Veja Aritmética de ponto
     flutuante: problemas e limitações para mais informações.

class set(iterable=(), /)

   Retorna um novo objeto "set", opcionalmente com elementos obtidos
   de *iteráveis*. "set" é uma classe embutida. Veja também Tipo
   conjuntos --- set, frozenset para documentação sobre essa classe.

   Para outros contêineres, consulte as classes embutidas "frozenset",
   "list", "tuple" e "dict", bem como o módulo "collections".

setattr(object, name, value, /)

   Esta é a contrapartida de "getattr()". Os argumentos são um objeto,
   uma string e um valor arbitrário. A string pode nomear um atributo
   existente ou um novo atributo. A função atribui o valor ao
   atributo, desde que o objeto permita. Por exemplo, "setattr(x,
   'foobar', 123)" é equivalente a "x.foobar = 123".

   *name* não precisa ser um identificador do Python conforme definido
   em Nomes (identificadores e palavras reservadas) a menos que o
   objeto opte por impor isso, por exemplo, em um "__getattribute__()"
   personalizado ou via "__slots__". Um atributo cujo nome não é um
   identificador não será acessível usando a notação de ponto, mas
   pode ser acessado através de "getattr()" etc.

   Nota:

     Uma vez que desfiguração de nome privado acontece em tempo de
     compilação, deve-se manualmente mutilar o nome de um atributo
     privado (atributos com dois sublinhados à esquerda) para defini-
     lo com "setattr()".

class sentinel(name, /, *, repr=None)

   Retorna um novo objeto sinalizador único. *name* deve ser uma "str"
   e é utilizado, por padrão como a representação do objeto retornado:

      >>> FALTANDO = sentinel("FALTANDO")
      >>> FALTANDO
      FALTANDO

   O argumento opcional *repr* pode ser utilizado para especificar uma
   representação diferente:

      >>> MISSING = sentinel("MISSING", repr="<MISSING>")
      >>> MISSING
      <MISSING>

   Os objetos sinalizador são sempre verdadeiros e as comparações de
   igualdade são apenas entre si. Eles são destinados a serem
   comparados com o operador "is".

   "sentinel" não dá suporte a subclasse.

   Cópias superficiais ou profundas de um objeto sinalizador retornam
   o próprio objeto.

   Por convenção, sinalizadores são atribuídas a uma variável com um
   nome correspondente. As sentinelas definidas desta forma podem ser
   utilizadas em *dicas de tipo*:

      MISSING = sentinel("MISSING")

      def next_value(default: int | MISSING = MISSING):
          ...

   Os objetos sinalizador dá suporte ao operador |  para utilização em
   expressões de tipo.

   A "serialização com pickle" (em inglês, *pickling*) é possível para
   objetos sentinelas colocados no escopo global de um módulo, com um
   nome correspondente ao do sentinela, e para sentinelas colocados no
   escopo de classe, com um nome correspondente à *nome qualificado*
   do sentinela. Outros sentinelas, como os definidos no escopo de uma
   função, não são serializáveis com pickle. A identidade do sentinela
   é preservada após a serialização com pickle:

      import pickle

      PICKLABLE = sentinel("PICKLABLE")

      assert pickle.loads(pickle.dumps(PICKLABLE)) is PICKLABLE

      class Cls:
          PICKLABLE = sentinel("Cls.PICKLABLE")

      assert pickle.loads(pickle.dumps(Cls.PICKLABLE)) is Cls.PICKLABLE

   Os objetos sinalizador têm os seguintes atributos:

   __name__

      O nome do sinalizador.

   __module__

      O nome do módulo onde o sinalizador foi criado. Este atributo é
      gravável.

   Adicionado na versão 3.15.

class slice(stop, /)
class slice(start, stop, step=None, /)

   Retorna um objeto *fatia* representando o conjunto de índices
   especificados por "range(start, stop, step)". Os argumentos *start*
   e *step* têm o padrão "None".

   Objetos fatia também são gerados quando a sintaxe de fatiamento é
   usada. Por exemplo: "a[start:stop:step]" ou "a[start:stop, i]".

   Veja "itertools.islice()" para uma versão alternativa que retorna
   um *iterador*.

   start
   stop
   step

      Esses atributos somente leitura são definidos para os valores
      dos argumentos (ou seus valores padrão). Eles não possuem outra
      funcionalidade explícita; no entanto, eles são usados pelo NumPy
      e outros pacotes de terceiros.

   Alterado na versão 3.12: Os objetos slice agora são *hasheáveis*
   (desde que "start", "stop" e "step" sejam hasheáveis).

sorted(iterable, /, *, key=None, reverse=False)

   Retorna uma nova lista classificada dos itens em *iterable*.

   Possui dois argumentos opcionais que devem ser especificados como
   argumentos nomeados.

   *key* especifica a função de um argumento usado para extrair uma
   chave de comparação de cada elemento em *iterable* (por exemplo,
   "key=str.lower"). O valor padrão é "None" (compara os elementos
   diretamente).

   *reverse* é um valor booleano. Se definido igual a "True", então os
   elementos da lista são classificados como se cada comparação
   estivesse invertida.

   Usa "functools.cmp_to_key()" para converter a função das antigas
   *cmp* para uma função *key*.

   A função embutida "sorted()" é garantida como estável. Uma
   ordenação é estável se garantir não alterar a ordem relativa dos
   elementos que se comparam da mesma forma --- isso é útil para
   ordenar em várias passagens (por exemplo, ordenar por departamento
   e depois por nível de salário).

   O algoritmo de classificação usa apenas comparações "<" entre
   itens. Embora definir um método "__lt__()" seja suficiente para
   ordenação, **PEP 8** recomenda que todas as seis comparações ricas
   sejam implementadas. Isso ajudará a evitar erros ao usar os mesmos
   dados com outras ferramentas de ordenação, como "max()", que
   dependem de um método subjacente diferente. Implementar todas as
   seis comparações também ajuda a evitar confusão para comparações de
   tipo misto que podem chamar o método espelhado "__gt__()".

   Para exemplos de classificação e um breve tutorial de
   classificação, veja Técnicas de ordenação.

@staticmethod

   Transforma um método em método estático.

   Um método estático não recebe um primeiro argumento implícito. Para
   declarar um método estático, use este idioma:

      class C:
          @staticmethod
          def f(arg1, arg2, argN): ...

   A forma "@staticmethod" é uma função de *decorador* -- veja
   Definições de função para detalhes.

   Um método estático pode ser chamado na classe (tal como "C.f()") ou
   em uma instância (tal como "C().f()"). Além disso, o *descritor* de
   método estático também é um chamável, então ele pode ser usado na
   definição de classe (como "f()").

   Métodos estáticos em Python são similares àqueles encontrados em
   Java ou C++. Veja também "@classmethod" para uma variante útil na
   criação de construtores de classe alternativos.

   Como todos os decoradores, também é possível chamar "staticmethod"
   como uma função regular e fazer algo com seu resultado. Isso é
   necessário em alguns casos em que você precisa de uma referência
   para uma função de um corpo de classe e deseja evitar a
   transformação automática em método de instância. Para esses casos,
   use este idioma:

      def função_comum():
          ...

      class C:
          método = staticmethod(função_comum)

   Para mais informações sobre métodos estáticos, consulte A
   hierarquia de tipos padrão.

   Alterado na versão 3.10: Métodos estáticos agora herdam os
   atributos do método ("__module__", "__name__", "__qualname__",
   "__doc__" e "__annotations__"), têm um novo atributo "__wrapped__"
   e são agora chamáveis como funções regulares.

class str(*, encoding='utf-8', errors='strict')
class str(object)
class str(object, encoding, errors='strict')
class str(object, *, errors)

   Retorna uma versão "str" de *object*. Consulte "str()" para
   detalhes.

   "str" é uma *classe* de string embutida. Para informações gerais
   sobre strings, consulte Tipo sequência de texto --- str.

sum(iterable, /, start=0)

   Soma *start* e os itens de um *iterable* da esquerda para a direita
   e retornam o total. Os itens do *iterable* são normalmente números
   e o valor inicial não pode ser uma string.

   Para alguns casos de uso, existem boas alternativas para "sum()". A
   maneira rápida e preferida de concatenar uma sequência de strings é
   chamando "''.join(sequence)". Para adicionar valores de ponto
   flutuante com precisão estendida, consulte "math.fsum()". Para
   concatenar uma série de iteráveis, considere usar
   "itertools.chain()".

   Alterado na versão 3.8: O parâmetro *start* pode ser especificado
   como um argumento nomeado.

   Alterado na versão 3.12: A soma dos pontos flutuantes foi alterada
   para um algoritmo que oferece maior precisão e melhor
   comutatividade na maioria das compilações.

   Alterado na versão 3.14: Adicionada especialização para soma de
   complexos, usando o mesmo algoritmo para soma de flutuantes.

class super
class super(type, object_or_type=None, /)

   Retorna um objeto proxy que delega chamadas de método a uma classe
   pai ou irmão do *type*. Isso é útil para acessar métodos herdados
   que foram substituídos em uma classe.

   O *object_or_type* determina a *ordem de resolução de métodos* a
   ser pesquisada. A pesquisa inicia a partir da classe logo após o
   *type*.

   Por exemplo, se "__mro__" de *object_or_type* é "D -> B -> C -> A
   -> object" e o valor de *type* é "B", então "super()" procura por
   "C -> A -> object".

   O atributo "__mro__" da classe correspondente ao *object_or_type*
   lista a ordem de pesquisa de resolução de método usada por
   "getattr()" e "super()". O atributo é dinâmico e pode mudar sempre
   que a hierarquia da herança é atualizada.

   Se o segundo argumento for omitido, o objeto super retornado é
   desacoplado. Se o segundo argumento é um objeto, "isinstance(obj,
   type)" deve ser verdadeiro. Se o segundo argumento é um tipo,
   "issubclass(type2, type)" deve ser verdadeiro (isto é útil para
   classmethods).

   When called directly within an ordinary method of a class, both
   arguments may be omitted ("zero-argument "super()""). In this case,
   *type* will be the enclosing class, and *object_or_type* will be
   the first argument of the immediately enclosing function (typically
   "self"). Zero-argument "super()" will not work as expected within
   nested functions, including generator expressions, which implicitly
   create nested functions.

   Existem dois casos de uso típicos para *super*. Em uma hierarquia
   de classes com herança única, *super* pode ser usado para se
   referir a classes base sem nomeá-las explicitamente, tornando o
   código mais sustentável. Esse uso é paralelo ao uso de *super* em
   outras linguagens de programação.

   O segundo caso de uso é oferecer suporte à herança múltipla
   cooperativa em um ambiente de execução dinâmica. Esse caso de uso é
   exclusivo do Python e não é encontrado em idiomas ou linguagens
   compiladas estaticamente que suportam apenas herança única. Isso
   torna possível implementar "diagramas em losango", onde várias
   classes base implementam o mesmo método. Um bom design exige que
   tais implementações tenham a mesma assinatura de chamada em todos
   os casos (porque a ordem das chamadas é determinada em tempo de
   execução, porque essa ordem se adapta às alterações na hierarquia
   de classes e porque essa ordem pode incluir classes de irmãos
   desconhecidas antes do tempo de execução).

   Nos dois casos de uso, uma chamada típica de superclasse se parece
   com isso:

      class C(B):
          def método(self, arg):
              super().método(arg)    # Isso faz o mesmo que:
                                     # super(C, self).método(arg)

   Além das pesquisas de método, "super()" também funciona para
   pesquisas de atributo. Um possível caso de uso para isso é chamar
   *descritores* em uma classe pai ou irmã.

   Observe que "super()" é implementada como parte do processo de
   vinculação para procura explícita de atributos com ponto, tal como
   "super().__getitem__(nome)". Ela faz isso implementando seu próprio
   método "__getattribute__()" para pesquisar classes em uma ordem
   predizível que possui suporte a herança múltipla cooperativa. Logo,
   "super()" não é definida para procuras implícitas usando instruções
   ou operadores como "super()[name]".

   Observe também que, além da forma de argumento zero, "super()" não
   se limita ao uso de métodos internos. O formulário de dois
   argumentos especifica exatamente os argumentos e faz as referências
   apropriadas. O formulário de argumento zero funciona apenas dentro
   de uma definição de classe, pois o compilador preenche os detalhes
   necessários para recuperar corretamente a classe que está sendo
   definida, além de acessar a instância atual para métodos comuns.

   Para sugestões práticas sobre como projetar classes cooperativas
   usando "super()", consulte o guia para uso de super().

   Alterado na versão 3.14: Os objetos "super" agora são
   "serializáveis" e "copiáveis".

class tuple(iterable=(), /)

   Ao invés de ser uma função, "tuple" é na verdade um tipo de
   sequência imutável, conforme documentado em Tuplas e Tipos
   sequências --- list, tuple, range.

class type(object, /)
class type(name, bases, dict, /, **kwargs)

   Com um argumento, retorna o tipo de um *object*. O valor de retorno
   é um tipo de objeto e geralmente o mesmo objeto retornado por
   "object.__class__".

   A função embutida "isinstance()" é recomendada para testar o tipo
   de um objeto, porque ela leva sub-classes em consideração.

   Com três argumentos, retorna um novo objeto type. Esta é
   essencialmente a forma dinâmica da instrução "class". A string
   *name* é o nome da classe e se torna o atributo "__name__". A tupla
   *bases* contém as classes bases e se torna o atributo "__bases__";
   se vazio, "object", a base final de todas as classes é adicionada.
   O dicionário *dict* contém definições de atributo e método para o
   corpo da classe; ele pode ser copiado ou envolto antes de se tornar
   o atributo "__dict__". As duas instruções a seguir criam objetos
   "type" idênticos:

   >>> class X:
   ...     a = 1
   ...
   >>> X = type('X', (), dict(a=1))

   Veja também:

   * Documentação sobre atributos e métodos em classes.

   * Objetos tipo

   Argumentos nomeados fornecidos para a forma de três argumentos são
   passados para a máquina metaclasse apropriada (geralmente
   "__init_subclass__()") da mesma forma que palavras-chave em uma
   definição de classe (além de *metaclasse*) fariam.

   Diferentemente de uma instrução "class", a forma de três argumento
   não chama o método metaclasse "__prepare__" (veja Preparando o
   espaço de nomes da classe). Ise "types.new_class()" para criar
   dinamicamente uma classe usando a metaclasse apropriada.

   Veja também Personalizando a criação de classe.

   Alterado na versão 3.6: Subclasses de "type" que não substituem
   "type.__new__" não podem mais usar a forma com apenas um argumento
   para obter o tipo de um objeto.

   Alterado na versão 3.15: *dict* agora pode ser um "frozendict".

vars()
vars(object, /)

   Retorna o atributo "__dict__" para um módulo, classe, instância, or
   qualquer outro objeto com um atributo "__dict__".

   Objetos como modelos e instâncias têm um atributo atualizável
   "__dict__"; porém, outros projetos podem ter restrições de escrita
   em seus atributos "__dict__" (por exemplo, classes usam um
   "types.MappingProxyType" para prevenir atualizações diretas a
   dicionário).

   Sem nenhum argumento, "vars()" age como "locals()".

   Uma exceção "TypeError" é levantada se um objeto é especificado,
   mas ela não tem um atributo "__dict__" (por exemplo, se sua classe
   define o atributo "__slots__").

   Alterado na versão 3.13: O resultado de chamar esta função sem um
   argumento foi atualizado conforme descrito na embutida "locals()".

zip(*iterables, strict=False)

   Itera sobre vários iteráveis em paralelo, produzindo tuplas com um
   item de cada um.

   Exemplo:

      >>> for item in zip([1, 2, 3], ['açúcar', 'tempero', 'tudo que há de bom']):
      ...     print(item)
      ...
      (1, 'açúcar')
      (2, 'tempero')
      (3, 'tudo que há de bom')

   Mais formalmente: "zip()" retorna um iterador de tuplas, onde a
   *i*-ésima tupla contém o *i*-ésimo elemento de cada um dos
   iteráveis do argumento.

   Outra maneira de pensar em "zip()" é que ela transforma linhas em
   colunas e colunas em linhas. Isso é semelhante a transpor uma
   matriz.

   "zip()" é preguiçoso: Os elementos não serão processados até que o
   iterável seja iterado. Por exemplo, por um loop "for" ou por um
   "list".

   Uma coisa a considerar é que os iteráveis passados para "zip()"
   podem ter comprimentos diferentes; às vezes por design e às vezes
   por causa de um bug no código que preparou esses iteráveis. Python
   oferece três abordagens diferentes para lidar com esse problema:

   * Por padrão, "zip()" para quando o iterável mais curto tenha sido
     *esgotado*. Ele irá ignorar os itens restantes nos iteráveis mais
     longos, cortando o resultado para o comprimento do iterável mais
     curto:

        >>> list(zip(range(3), ['fi', 'fa', 'fo', 'fum']))
        [(0, 'fi'), (1, 'fa'), (2, 'fo')]

   * "zip()" é frequentemente usado em casos onde os iteráveis são
     considerados de tamanho igual. Nesses casos, é recomendado usar a
     opção "strict=True". Sua saída é a mesma do "zip()":: normal

        >>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
        [('a', 1), ('b', 2), ('c', 3)]

     Ao contrário do comportamento padrão, ele levanta uma exceção
     "ValueError" se um iterável for *esgotado* antes dos outros:

     >>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):
     ...     print(item)
     ...
     (0, 'fee')
     (1, 'fi')
     (2, 'fo')
     Traceback (most recent call last):
       ...
     ValueError: zip() argument 2 is longer than argument 1

     Sem o argumento "strict=True", qualquer bug que resulte em
     iteráveis de diferentes comprimentos será silenciado,
     possivelmente se manifestando como um bug difícil de encontrar em
     outra parte do programa.

   * Iteráveis mais curtos podem ser preenchidos com um valor
     constante para fazer com que todos os iteráveis tenham o mesmo
     comprimento. Isso é feito por "itertools.zip_longest()".

   Casos extremos: Com um único argumento iterável, "zip()" retorna um
   iterador de tuplas de um elemento. Sem argumentos, retorna um
   iterador vazio.

   Dicas e truques:

   * A ordem de avaliação da esquerda para a direita dos iteráveis é
     garantida. Isso torna possível um idioma para agrupar uma série
     de dados em grupos de comprimento n usando "zip(*[iter(s)]*n,
     strict=True)". Isso repete o *mesmo* iterador "n" vezes para que
     cada tupla de saída tenha o resultado de chamadas "n" para o
     iterador. Isso tem o efeito de dividir a entrada em pedaços de n
     comprimentos.

   * "zip()" em conjunto com o operador "*" pode ser usado para
     descompactar uma lista:

        >>> x = [1, 2, 3]
        >>> y = [4, 5, 6]
        >>> list(zip(x, y))
        [(1, 4), (2, 5), (3, 6)]
        >>> x2, y2 = zip(*zip(x, y))
        >>> x == list(x2) and y == list(y2)
        True

   Alterado na versão 3.10: Adicionado o argumento "strict".

__import__(name, globals=None, locals=None, fromlist=(), level=0)

   Nota:

     Esta é uma função avançada que não é necessária na programação
     diária do Python, ao contrário de "importlib.import_module()".

   Esta função é chamada pela instrução "import". Ela pode ser
   substituída (importando o módulo "builtins" e atribuindo a
   "builtins.__import__") para alterar a semântica da instrução
   "import", mas isso é **fortemente** desencorajado, pois geralmente
   é mais simples usar ganchos de importação (consulte **PEP 302**)
   para atingir os mesmos objetivos e não causa problemas com o código
   que pressupõe que a implementação de importação padrão esteja em
   uso. O uso direto de "__import__()" também é desencorajado em favor
   de "importlib.import_module()".

   A função importa o módulo *name*, potencialmente usando os dados
   *globals* e *locals* para determinar como interpretar o nome em um
   contexto de pacote. O *fromlist* fornece os nomes de objetos ou
   submódulos que devem ser importados do módulo, fornecidos por
   *name*. A implementação padrão não usa seu argumento *locals* e usa
   seus *globals* apenas para determinar o contexto do pacote da
   instrução "import".

   *level* specifies whether to use absolute or relative imports. "0"
   (the default) means only perform absolute imports.  For relative
   imports, "1" refers to the current package, "2" to its parent
   package, and so on (see **PEP 328** for details).

   Quando a variável *name* está no formato "pacote.módulo",
   normalmente, o pacote de nível superior (o nome até o primeiro
   ponto) é retornado, *não* o módulo nomeado por *name*. No entanto,
   quando um argumento *fromlist* não vazio é fornecido, o módulo
   nomeado por *name* é retornado.

   Por exemplo, a instrução "import spam" resulta em bytecode
   semelhante ao seguinte código:

      spam = __import__('spam', globals(), locals(), [], 0)

   A instrução "import spam.presunto" resulta nesta chamada:

      spam = __import__('spam.presunto', globals(), locals(), [], 0)

   Observe como "__import__()" retorna o módulo de nível superior
   aqui, porque este é o objeto vinculado a um nome pela instrução
   "import".

   Por outro lado, a instrução "from spam.presunto import ovos,
   salsicha as sals" resulta em

      _temp = __import__('spam.presunto', globals(), locals(), ['ovos', 'salsicha'], 0)
      ovos = _temp.ovos
      sals = _temp.salsicha

   Aqui, o módulo "spam.ham" é retornado de "__import__()". A partir
   desse objeto, os nomes a serem importados são recuperados e
   atribuídos aos seus respectivos nomes.

   Se você simplesmente deseja importar um módulo (potencialmente
   dentro de um pacote) pelo nome, use "importlib.import_module()".

   Alterado na versão 3.3: Valores negativos para *level* não são mais
   suportados (o que também altera o valor padrão para 0).

   Alterado na versão 3.9: Quando as opções de linha de comando "-E"
   ou "-I" estão sendo usadas, a variável de ambiente "PYTHONCASEOK" é
   agora ignorada.

-[ Notas de rodapé ]-

[1] Observe que o analisador sintático aceita apenas a convenção de
    fim de linha no estilo Unix. Se você estiver lendo o código de um
    arquivo, use o modo de conversão de nova linha para converter
    novas linhas no estilo Windows ou Mac.
