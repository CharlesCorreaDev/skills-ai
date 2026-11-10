"string" --- Operações comuns de strings
****************************************

**Código-fonte:** Lib/string/__init__.py

======================================================================

Ver também:

  Tipo sequência de texto --- str

  String Methods


Constantes de strings
=====================

As constantes definidas neste módulo são:

string.ascii_letters

   A concatenação das constantes "ascii_lowercase" e "ascii_uppercase"
   descritas abaixo. Este valor não depende da localidade.

string.ascii_lowercase

   As letras minúsculas "'abcdefghijklmnopqrstuvwxyz'". Este valor não
   depende da localidade e não mudará.

string.ascii_uppercase

   As letras maiúsculas "'ABCDEFGHIJKLMNOPQRSTUVWXYZ'". Este valor não
   depende da localidade e não mudará.

string.digits

   A string "'0123456789'".

string.hexdigits

   A string "'0123456789abcdefABCDEF'".

string.octdigits

   A string "'01234567'".

string.punctuation

   String de caracteres ASCII que são considerados caracteres de
   pontuação na localidade "C": "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~".

string.printable

   String de caracteres ASCII que são considerados imprimíveis pelo
   Python. Esta é uma combinação de "digits", "ascii_letters",
   "punctuation" e "whitespace".

   Nota:

     Por design, "string.printable.isprintable()" retorna "False". Em
     particular, "string.printable" não é imprimível no sentido POSIX
     (veja *LC_CTYPE*).

string.whitespace

   Uma string contendo todos os caracteres ASCII que são considerados
   espaços em branco. Isso inclui espaço de caracteres, tabulação,
   avanço de linha, retorno, avanço de formulário e tabulação
   vertical.


Formatação personalizada de strings
===================================

A classe embutida de string fornece a capacidade de substituir
variáveis complexas e de formatar valores por meio do método
"format()" descrito na **PEP 3101**. A classe "Formatter" no módulo
"string" permite que você crie e personalize seus próprios
comportamentos de formatação de strings, usando a mesma implementação
do método embutido "format()".

class string.Formatter

   A classe "Formatter" tem os seguintes métodos públicos:

   format(format_string, /, *args, **kwargs)

      O método principal da API. Ele aceita uma string de formato e um
      conjunto arbitrário de argumentos posicionais e nomeados. É
      apenas um invólucro que chama "vformat()".

      Alterado na versão 3.7: Um argumento de string de formato é
      agora somente-posicional.

   vformat(format_string, args, kwargs)

      Esta função realiza o trabalho real de formatação. Ela é exposta
      como uma função separada para casos em que você deseja passar um
      dicionário predefinido de argumentos, em vez de desempacotar e
      empacotar novamente o dicionário como argumentos individuais
      usando a sintaxe "*args" e "**kwargs". "vformat()" faz o
      trabalho de quebrar a string de formato em dados de caracteres e
      campos de substituição. Ela chama os vários métodos descritos a
      seguir.

   Além disso, o "Formatter" define uma série de métodos que devem ser
   substituídos por subclasses:

   parse(format_string)

      Percorre format_string e retorna um iterável de tuplas
      (*literal_text*, *field_name*, *format_spec*, *conversion*).
      Isso é usado por "vformat()" para quebrar a string em texto
      literal ou em campos de substituição.

      Os valores da tupla representam, conceitualmente, um intervalo
      de texto literal, seguido de um único campo de substituição. Se
      não houver texto literal (o que pode ocorrer se dois campos de
      substituição forem consecutivos), *literal_text* será uma string
      de comprimento zero. Se não houver campo de substituição, os
      valores de *field_name*, *format_spec* e *conversion* serão
      "None". O valor de *field_name* não é modificado, e a numeração
      automática de campos posicionais não numerados é realizada por
      "vformat()".

   get_field(field_name, args, kwargs)

      Dado *field_name*, converte-o em um objeto a ser formatado. A
      autonumeração de *field_name* retornada de "parse()" é feita por
      "vformat()" antes de chamar este método. Retorna uma tupla (obj,
      used_key). A versão padrão aceita strings no formato definido na
      **PEP 3101**, como "0[name]" ou "label.title". *args* e *kwargs*
      são como os argumentos passados para "vformat()". O valor de
      retorno *used_key* tem o mesmo significado que o parâmetro *key*
      em "get_value()".

   get_value(key, args, kwargs)

      Obtém o valor de um campo. O argumento *key* será um inteiro ou
      uma string. Se for um inteiro, ele representa o índice do
      argumento posicional em *args*; se for uma string, representa um
      argumento nomeado em *kwargs*.

      O parâmetro *args* é definido para a lista de argumentos
      posicionais de "vformat()", e o parâmetro *kwargs* é definido
      para o dicionário de argumentos nomeados.

      Para nomes de campos compostos, essas funções são chamadas
      apenas para o primeiro componente do nome do campo; os
      componentes subsequentes são tratados por meio de operações
      normais de atributo e de indexação.

      Então, por exemplo, a expressão de campo '0.name' faria com que
      "get_value()" fosse chamado com o argumento *key* 0. O atributo
      "name" será pesquisado após a função "get_value()" retornar,
      chamando a função embutida "getattr()".

      Se o índice ou palavra-chave se referir a um item que não
      existe, um "IndexError" ou "KeyError" deve ser levantado.

   check_unused_args(used_args, args, kwargs)

      Implementa a verificação de argumentos não usados, se desejar.
      Os argumentos para esta função são o conjunto de todas as chaves
      de argumento realmente referidas na string de formato (inteiros
      para argumentos posicionais e strings para argumentos nomeados),
      e uma referência a *args* e *kwargs* que foi passada para
      vformat. O conjunto de argumentos não utilizados pode ser
      calculado com base nesses parâmetros. Presume-se que
      "check_unused_args()" levante uma exceção caso a verificação
      falhe.

   format_field(value, format_spec)

      "format_field()" simplesmente chama o global embutido
      "format()". O método é fornecido para que as subclasses possam
      substituí-lo.

   convert_field(value, conversion)

      Converte o valor (retornado por "get_field()") de acordo com um
      tipo de conversão (como na tupla retornada pelo método
      "parse()"). A versão padrão entende os tipos de conversão "s"
      (str), "r" (repr) e "a" (ascii).


Sintaxe das strings de formato
==============================

O método "str.format()" e a classe "Formatter" compartilham a mesma
sintaxe para strings de formato (embora no caso de "Formatter", as
subclasses possam definir sua própria sintaxe de string de formato). A
sintaxe é relacionada a literais de strings formatadas e literais de
strings templates, mas é menos sofisticada e, em especial, não oferece
suporte a expressões arbitrárias em interpolações.

As strings de formato contêm "campos de substituição" entre chaves
"{}". Tudo o que não estiver entre chaves é considerado texto literal
e é copiado inalterado para a saída. Se você precisar incluir um
caractere de chave no texto literal, ele pode ser escapado
duplicando-o: "{{" e "}}".

A gramática para um campo de substituição é a seguinte:

   replacement_field: "{" [field_name] ["!" conversion] [":" format_spec] "}"
   field_name:        arg_name ("." attribute_name | "[" element_index "]")*
   arg_name:          [identifier | digit+]
   attribute_name:    identifier
   element_index:     digit+ | index_string
   index_string:      <any source character except "]"> +
   conversion:        "r" | "s" | "a"
   format_spec:       format-spec:format_spec

Em termos menos formais, o campo de substituição pode começar com um
*field_name* que especifica o objeto cujo valor deve ser formatado e
inserido na saída, em vez do próprio campo de substituição. O
*field_name* é opcionalmente seguido de um campo *conversion*, que é
precedido por um ponto de exclamação "'!'", e de um *format_spec*, que
é precedido por dois pontos "':'". Eles especificam um formato não
padrão para o valor de substituição.

Veja também a seção Minilinguagem de especificação de formato.

O próprio *field_name* começa com um *arg_name*, que pode ser um
número ou uma palavra-chave. Se for um número, ele se refere a um
argumento posicional, e se for uma palavra-chave, ele se refere a um
argumento nomeado. Um *arg_name* é tratado como um número se uma
chamada à "str.isdecimal()" na string retornar verdadeiro. Se os
arg_names numéricos em uma string de formato forem 0, 1, 2, … em
sequência, eles podem ser todos omitidos (não apenas alguns) e os
números 0, 1, 2, … serão inseridos automaticamente nessa ordem. Como
*arg_name* não está delimitado por aspas, não é possível especificar
chaves de dicionário arbitrárias (por exemplo, as strings "'10'" ou
"':-]'") em uma string de formato. O *arg_name* pode ser seguido por
qualquer número de expressões de índice ou de atributo. Uma expressão
da forma "'.name'" seleciona o atributo nomeado com "getattr()",
enquanto uma expressão da forma "'[index]'" faz uma pesquisa de índice
com "__getitem__()".

Alterado na versão 3.1: Os especificadores de argumento posicional
podem ser omitidos para "str.format()", de forma que "'{}
{}'.format(a, b)" é equivalente a "'{0} {1}'.format(a, b)".

Alterado na versão 3.4: Os especificadores de argumento posicional
podem ser omitidos para "Formatter".

Alguns exemplos simples de string de formato:

   "Primeiro, tu deverás contar até {0}"  # Referencia o primeiro argumento posicional
   "Traga-me um {}"                       # Referencia implicitamente o primeiro argumento posicional
   "De {} para {}"                        # Mesmo que "De {0} para {1}"
   "Minha missão é {nome}"                # Referencia argumento nomeado 'nome'
   "Peso em toneladas {0.peso}"           # O atributo 'peso' do primeiro argumento posicional
   "Unidades destruídas: {jogadores[0]}"  # Primeiro elemento do argumento nomeado 'jogadores'.

O campo *conversion* causa uma coerção de tipo antes da formatação.
Normalmente, o trabalho de formatação de um valor é feito pelo método
"__format__()" do próprio valor. No entanto, em alguns casos, é
desejável forçar um tipo a ser formatado como string, substituindo sua
própria definição de formatação. Ao converter o valor em uma string
antes de chamar "__format__()", a lógica de formatação normal é
contornada.

Atualmente, há suporte para três sinalizadores de conversão: "'!s'",
que chama "str()" no valor; "'!r'", que chama "repr()"; e "'!a'", que
chama "ascii()".

Alguns exemplos:

   "Harold é um {0!s} esperto"        # Chama str() no primeiro argumento
   "Trazei à luz o {name!r} sagrado"    # Chama repr() no primeiro argumento
   "Mais {!a}"                      # Chama ascii() no primeiro argumento

O campo *format_spec* contém uma especificação de como o valor deve
ser apresentado, incluindo detalhes como a largura do campo, o
alinhamento, o preenchimento, a precisão decimal e assim por diante.
Cada tipo de valor pode definir sua própria "minilinguagem de
formatação" ou interpretação de *format_spec*.

A maioria dos tipos embutidos oferece suporte a uma minilinguagem de
formatação comum, descrita na próxima seção.

O campo *format_spec* também pode conter campos de substituição
aninhados. Esses campos de substituição aninhados podem conter um nome
de campo, um sinalizador de conversão e uma especificação de formato,
mas um aninhamento mais profundo não é permitido. Os campos de
substituição em format_spec são substituídos antes que a string
*format_spec* seja interpretada. Isso permite que a formatação de um
valor seja especificada dinamicamente.

Veja a seção Exemplos de formato para alguns exemplos.


Minilinguagem de especificação de formato
-----------------------------------------

"Especificações de formato" são usadas nos campos de substituição
contidos em uma string de formato para definir como os valores
individuais são apresentados (consulte Sintaxe das strings de formato,
Literais de strings formatadas e Literais de string template
(t-strings)). Elas também podem ser passadas diretamente para a função
embutida "format()". Cada tipo formatável pode definir como a
especificação do formato deve ser interpretada.

A maioria dos tipos embutidos implementa as seguintes opções para
especificações de formato, embora algumas das opções de formatação
sejam válidas apenas para tipos numéricos.

Uma convenção geral é que uma especificação de formato vazia produz o
mesmo resultado que se você tivesse chamado "str()" no valor. Uma
especificação de formato não vazio geralmente modifica o resultado.

A forma geral de um *especificador de formato padrão* é:

   format_spec:             [options][width_and_precision][type]
   options:                 [[fill]align][sign]["z"]["#"]["0"]
   fill:                    <any character>
   align:                   "<" | ">" | "=" | "^"
   sign:                    "+" | "-" | " "
   width_and_precision:     [width_with_grouping][precision_with_grouping]
   width_with_grouping:     [width][grouping]
   precision_with_grouping: "." [precision][grouping] | "." grouping
   width:                   digit+
   precision:               digit+
   grouping:                "," | "_"
   type:                    "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g"
                            | "G" | "n" | "o" | "s" | "x" | "X" | "%"

Se um valor *align*  válido for especificado, ele pode ser precedido
por um caractere de preenchimento *fill* que pode ser qualquer
caractere e o padrão é um espaço se omitido. Não é possível usar uma
chave literal (""{"" ou ""}"") como o caractere *fill* em uma string
formatada literal ou ao usar o método "str.format()". No entanto, é
possível inserir uma chave com um campo de substituição aninhado. Esta
limitação não afeta a função "format()".

O significado das várias opções de alinhamento é o seguinte:

+-----------+------------------------------------------------------------+
| Opção     | Significado                                                |
|===========|============================================================|
| "'<'"     | Força o alinhamento à esquerda do campo no espaço          |
|           | disponível (este é o padrão para a maioria dos objetos).   |
+-----------+------------------------------------------------------------+
| "'>'"     | Força o alinhamento à direita do campo no espaço           |
|           | disponível (este é o padrão para números).                 |
+-----------+------------------------------------------------------------+
| "'='"     | Força o preenchimento a ser colocado após o sinal (se      |
|           | houver), mas antes dos dígitos. É usado para imprimir      |
|           | campos na forma "+000000120". Esta opção de alinhamento só |
|           | é válida para tipos numéricos, excluindo "complex". Torna- |
|           | se o padrão para números quando "0" precede imediatamente  |
|           | a largura do campo.                                        |
+-----------+------------------------------------------------------------+
| "'^'"     | Força a centralização do campo no espaço disponível.       |
+-----------+------------------------------------------------------------+

Observe que, a menos que uma largura de campo mínima seja definida, a
largura do campo sempre será igual à largura dos dados que preenchem,
de modo que a opção de alinhamento não tem significado neste caso.

A opção *sign* só é válida para tipos numéricos e pode ser um dos
seguintes:

+-----------+------------------------------------------------------------+
| Opção     | Significado                                                |
|===========|============================================================|
| "'+'"     | Indica que um sinal deve ser usado para números positivos  |
|           | e negativos.                                               |
+-----------+------------------------------------------------------------+
| "'-'"     | Indica que um sinal deve ser usado apenas para números     |
|           | negativos (este é o comportamento padrão).                 |
+-----------+------------------------------------------------------------+
| espaço    | Indica que um espaço inicial deve ser usado em números     |
|           | positivos e um sinal de menos em números negativos.        |
+-----------+------------------------------------------------------------+

A opção "'z'" força valores de ponto flutuante de zero negativo para
zero positivo após o arredondamento, conforme a precisão do formato.
Esta opção só é válida para tipos de apresentação de ponto flutuante.

Alterado na versão 3.11: Adicionada a opção "'z'" (veja também **PEP
682**).

A opção "'#'" faz com que a "forma alternativa" seja usada na
conversão. A forma alternativa é definida de forma diferente para cada
tipo. Esta opção é válida apenas para tipos inteiros, pontos
flutuantes e complexos. Para inteiros, quando a saída binária, octal
ou hexadecimal é usada, esta opção adiciona o prefixo respectivo
"'0b'", "'0o'", "'0x'" ou "'0X'" ao valor de saída. Para pontos
flutuantes e complexos, a forma alternativa faz com que o resultado da
conversão sempre contenha um caractere de ponto decimal, mesmo que não
haja nenhum dígito após. Normalmente, um caractere de ponto decimal
aparece no resultado dessas conversões apenas se houver um dígito
depois. Além disso, nas conversões "'g'" e "'G'", os zeros finais não
são removidos do resultado.

O *width* é um número inteiro decimal que define a largura mínima
total do campo, incluindo quaisquer prefixos, separadores e outros
caracteres de formatação. Se não for especificado, a largura do campo
será determinada pelo conteúdo.

Quando nenhum alinhamento explícito é fornecido, preceder o campo
*width* com um caractere zero ("'0'") habilita o preenchimento por
zero, com reconhecimento de sinal, para tipos numéricos, exceto
"complex". Isso é equivalente a um caractere *fill* de valor "'0'" e
*alignment* de "'='".

Alterado na versão 3.10: Preceder o campo *width* com "'0'" não afeta
mais o alinhamento padrão de strings.

*precision* é um número decimal que indica quantos dígitos devem ser
exibidos depois do ponto decimal para um valor de ponto flutuante
formatado com "'f'" e "'F'", ou antes e depois do ponto decimal para
um valor de ponto flutuante formatado com "'g'" ou "'G'". Para tipos
não numéricos, o campo indica o tamanho máximo do campo -- em outras
palavras, quantos caracteres serão usados do conteúdo do campo.
*precision* não é permitido para valores inteiros.

A opção *grouping* após os campos *width* e *precision* especifica um
separador de grupo de dígitos para as partes inteira e fracionária de
um número, respectivamente. Pode ser um dos seguintes:

+-----------+------------------------------------------------------------+
| Opção     | Significado                                                |
|===========|============================================================|
| "','"     | Insere uma vírgula a cada 3 dígitos para tipos de          |
|           | apresentação inteiros "'d'" e de ponto flutuante,          |
|           | excluindo "'n'". Não há suporte para essa opção em outros  |
|           | tipos de apresentação.                                     |
+-----------+------------------------------------------------------------+
| "'_'"     | Insere um sublinhado a cada 3 dígitos para tipos de        |
|           | apresentação inteiros "'d'" e tipos de apresentação de     |
|           | ponto flutuante, excluindo "'n'". Para os tipos de         |
|           | apresentação inteiros "'b'", "'o'", "'x'" e "'X'", os      |
|           | sublinhados são inseridos a cada 4 dígitos. Para outros    |
|           | tipos de apresentação, esta opção não é suportada.         |
+-----------+------------------------------------------------------------+

Para um separador que respeita as configurações da localidade, utilize
em vez disso o "'n'" do tipo de apresentação para ponto flutuante ou
do tipo de apresentação para números inteiros.

Alterado na versão 3.1: Adicionada a opção "','" (veja também **PEP
378**).

Alterado na versão 3.6: Adicionada a opção "'_'" (veja também **PEP
515**).

Alterado na versão 3.14: Suporte a opção *grouping* para a parte
fracionária.

Finalmente, o *type* determina como os dados devem ser apresentados.

Os tipos de apresentação de string disponíveis são:

   +-----------+------------------------------------------------------------+
   | Tipo      | Significado                                                |
   |===========|============================================================|
   | "'s'"     | Formato de string. Este é o tipo padrão para strings e     |
   |           | pode ser omitido.                                          |
   +-----------+------------------------------------------------------------+
   | None      | O mesmo que "'s'".                                         |
   +-----------+------------------------------------------------------------+

Os tipos de apresentação inteira disponíveis são:

   +-----------+------------------------------------------------------------+
   | Tipo      | Significado                                                |
   |===========|============================================================|
   | "'b'"     | Formato binário. Exibe o número na base 2.                 |
   +-----------+------------------------------------------------------------+
   | "'c'"     | Caractere. Converte o inteiro no caractere Unicode         |
   |           | correspondente antes de imprimir.                          |
   +-----------+------------------------------------------------------------+
   | "'d'"     | Inteiro decimal. Exibe o número na base 10.                |
   +-----------+------------------------------------------------------------+
   | "'o'"     | Formato octal. Exibe o número na base 8.                   |
   +-----------+------------------------------------------------------------+
   | "'x'"     | Formato hexadecimal. Exibe o número na base 16, usando     |
   |           | letras minúsculas para os dígitos acima de 9.              |
   +-----------+------------------------------------------------------------+
   | "'X'"     | Formato hexadecimal. Exibe o número na base 16, usando     |
   |           | letras maiúsculas para os dígitos acima de 9. No caso de   |
   |           | "'#'" ser especificado, o prefixo "'0x'" será maiúsculo    |
   |           | para "'0X'" também.                                        |
   +-----------+------------------------------------------------------------+
   | "'n'"     | Número. É o mesmo que "'d'", exceto pelo fato de utilizar  |
   |           | a configuração de localidade atual para inserir os         |
   |           | separadores de grupo de dígitos apropriados. Observe que a |
   |           | localidade padrão não é a localidade do sistema.           |
   |           | Dependendo do seu caso de uso, talvez você queira definir  |
   |           | "LC_NUMERIC" com "locale.setlocale()" antes de usar "'n'". |
   +-----------+------------------------------------------------------------+
   | None      | O mesmo que "'d'".                                         |
   +-----------+------------------------------------------------------------+

Além dos tipos de apresentação acima, os inteiros podem ser formatados
com os tipos de apresentação de ponto flutuante listados abaixo
(exceto "'n'" e "None"). Ao fazer isso, "float()" é usado para
converter o inteiro em um número de ponto flutuante antes da
formatação.

Os tipos de apresentação disponíveis para valores "float" e "Decimal"
são:

   +-----------+------------------------------------------------------------+
   | Tipo      | Significado                                                |
   |===========|============================================================|
   | "'e'"     | Notação científica. Para uma dada precisão "p", formata o  |
   |           | número em notação científica com a letra "e" separando o   |
   |           | coeficiente do expoente. O coeficiente tem um dígito antes |
   |           | e "p" dígitos depois do ponto decimal, totalizando "p + 1" |
   |           | dígitos significativos. Sem precisão fornecida, usa uma    |
   |           | precisão de "6" dígitos após o ponto decimal para "float"  |
   |           | e mostra todos os dígitos de coeficiente para "Decimal".   |
   |           | Se "p=0", o ponto decimal é omitido a menos que a opção    |
   |           | "#" seja usada.  Para "float", o expoente sempre contém    |
   |           | pelo menos dois dígitos e é zero se o valor for zero.      |
   +-----------+------------------------------------------------------------+
   | "'E'"     | Notação científica. O mesmo que "'e'", exceto que usa um   |
   |           | 'E' maiúsculo como caractere separador.                    |
   +-----------+------------------------------------------------------------+
   | "'f'"     | Notação de ponto fixo. Para uma dada precisão "p", formata |
   |           | o número como um número decimal com exatamente "p" dígitos |
   |           | após o ponto decimal. Sem precisão fornecida, usa uma      |
   |           | precisão de "6" dígitos após o ponto decimal para "float"  |
   |           | e uma precisão grande o suficiente para mostrar todos os   |
   |           | dígitos de coeficiente para "Decimal". Se "p=0", o ponto   |
   |           | decimal é omitido a menos que a opção "#" seja usada.      |
   +-----------+------------------------------------------------------------+
   | "'F'"     | Notação de ponto fixo. O mesmo que "'f'", mas converte     |
   |           | "nan" para "NAN" e "inf" para "INF".                       |
   +-----------+------------------------------------------------------------+
   | "'g'"     | Formato geral. Para uma determinada precisão "p >= 1",     |
   |           | isso arredonda o número para "p" dígitos significativos e, |
   |           | então, formata o resultado em ponto fixo ou em notação     |
   |           | científica, conforme sua magnitude. Uma precisão de "0" é  |
   |           | tratada como equivalente a uma precisão de "1".  As regras |
   |           | precisas são as seguintes: suponha que o resultado         |
   |           | formatado com tipo de apresentação "'e'" e precisão "p-1"  |
   |           | teria o expoente "exp". Então, se "m <= exp < p", onde "m" |
   |           | é -4 para pontos flutuantes e -6 para "Decimals", o número |
   |           | é formatado com o tipo de apresentação "'f'" e precisão    |
   |           | "p-1-exp". Caso contrário, o número é formatado com o tipo |
   |           | de apresentação "'e'" e a precisão "p-1". Em ambos os      |
   |           | casos, zeros à direita insignificantes são removidos do    |
   |           | significando, e o ponto decimal também é removido se não   |
   |           | houver dígitos restantes após ele, a menos que a opção     |
   |           | "'#'" seja usada.  Sem precisão fornecida, usa uma         |
   |           | precisão de "6" dígitos significativos para "float". Para  |
   |           | "Decimal", o coeficiente do resultado é formado a partir   |
   |           | dos dígitos do coeficiente do valor; a notação científica  |
   |           | é usada para valores menores que "1e-6" em valor absoluto  |
   |           | e valores em que o valor posicional do dígito menos        |
   |           | significativo é maior que 1, e a notação de ponto fixo é   |
   |           | usada de outra forma.  Infinito positivo e negativo, zero  |
   |           | positivo e negativo e não- números, são formatados como    |
   |           | "inf", "-inf", "0", "-0" e "nan", respectivamente,         |
   |           | independentemente da precisão.                             |
   +-----------+------------------------------------------------------------+
   | "'G'"     | Formato geral. O mesmo que "'g'", exceto muda para "'E'"   |
   |           | se o número ficar muito grande. As representações de       |
   |           | infinito e de NaN também são maiúsculas.                   |
   +-----------+------------------------------------------------------------+
   | "'n'"     | Número. É o mesmo que "'g'", exceto pelo fato de utilizar  |
   |           | a configuração de localidade atual para inserir os         |
   |           | separadores de grupo de dígitos apropriados para a parte   |
   |           | inteira de um número. Observe que a localidade padrão não  |
   |           | é a localidade do sistema. Dependendo do seu caso de uso,  |
   |           | talvez você queira definir "LC_NUMERIC" com                |
   |           | "locale.setlocale()" antes de usar "'n'".                  |
   +-----------+------------------------------------------------------------+
   | "'%'"     | Porcentagem. Multiplica o número por 100 e exibe no        |
   |           | formato fixo ("'f'"), seguido de um sinal de porcentagem.  |
   +-----------+------------------------------------------------------------+
   | None      | Para "float", é o como o tipo "'g'", exceto que quando a   |
   |           | notação de ponto fixo é usada para formatar o resultado,   |
   |           | ela sempre inclui pelo menos um dígito após o ponto        |
   |           | decimal, e troca para a notação científica quando "exp >=  |
   |           | p - 1". Quando a precisão não é especificada, este último  |
   |           | será tão grande quanto necessário para representar o valor |
   |           | fornecido fielmente.  Para "Decimal", é o mesmo que "'g'"  |
   |           | ou "'G'", dependendo do valor de "context.capitals" no     |
   |           | contexto decimal atual.  O efeito geral é combinar a saída |
   |           | de "str()" conforme alterada pelos demais modificadores de |
   |           | formato.                                                   |
   +-----------+------------------------------------------------------------+

O resultado deve ser arredondado corretamente para uma dada precisão
"p" de dígitos após o ponto decimal. O modo de arredondamento para
"float" corresponde ao da função embutida "round()". Para "Decimal", o
modo de arredondamento do contexto atual será aplicado.

Os tipos de apresentação disponíveis para "complex" são os mesmos que
para "float" ("'%'" não é permitido). Os componentes real e imaginário
de um número complexo são formatados como números de ponto flutuante,
conforme o tipo de apresentação especificado. Eles são separados pelo
sinal obrigatório da parte imaginária, que é terminada por um sufixo
"j". Se o tipo de apresentação estiver faltando, o resultado
corresponderá à saída de "str()" (números complexos com uma parte real
diferente de zero também são cercados por parênteses), possivelmente
alterado por outros modificadores de formato.


Exemplos de formato
-------------------

Esta seção contém exemplos da sintaxe de "str.format()" e comparação
com a antiga formatação com "%".

Na maioria dos casos, a sintaxe é semelhante à antiga formatação com
"%", com a adição de "{}" e o uso de ":" em vez de "%". Por exemplo,
"'%03.2f'" pode ser traduzido para "'{:03.2f}'".

A nova sintaxe de formato também oferece suporte a novas e diferentes
opções, como mostradas nos exemplos a seguir.

Acessando argumentos por posição:

   >>> '{0}, {1}, {2}'.format('a', 'b', 'c')
   'a, b, c'
   >>> '{}, {}, {}'.format('a', 'b', 'c')  # somente 3.1+
   'a, b, c'
   >>> '{2}, {1}, {0}'.format('a', 'b', 'c')
   'c, b, a'
   >>> '{2}, {1}, {0}'.format(*'abc')      # desempacotando sequência de argumentos
   'c, b, a'
   >>> '{0}{1}{0}'.format('abra', 'cad')   # índices dos argumentos podem ser repetidos
   'abracadabra'

Acessando argumentos por nome:

   >>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
   'Coordinates: 37.24N, -115.81W'
   >>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
   >>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
   'Coordinates: 37.24N, -115.81W'

Acessando atributos dos argumentos:

   >>> c = 3-5j
   >>> ('The complex number {0} is formed from the real part {0.real} '
   ...  'and the imaginary part {0.imag}.').format(c)
   'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
   >>> class Point:
   ...     def __init__(self, x, y):
   ...         self.x, self.y = x, y
   ...     def __str__(self):
   ...         return 'Point({self.x}, {self.y})'.format(self=self)
   ...
   >>> str(Point(4, 2))
   'Point(4, 2)'

Acessando itens dos argumentos:

   >>> coord = (3, 5)
   >>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
   'X: 3;  Y: 5'

Substituindo "%s" e "%r":

   >>> "repr() mostra aspas: {!r}; str() não mostra: {!s}".format('teste1', 'teste2')
   "repr() mostra aspas: 'teste1'; str() não mostra: teste2"

Alinhando o texto e especificando uma largura:

   >>> '{:<30}'.format('alinhado à esquerda')
   'alinhado à esquerda           '
   >>> '{:>30}'.format('alinhado à direita')
   '            alinhado à direita'
   >>> '{:^30}'.format('centralizado')
   '         centralizado         '
   >>> '{:*^30}'.format('centralizado')  # usa '*' como preenchimento
   '*********centralizado*********'

Substituindo "%+f", "%-f" e "% f" e especificando um sinal:

   >>> '{:+f}; {:+f}'.format(3.14, -3.14)  # mostra sempre
   '+3.140000; -3.140000'
   >>> '{: f}; {: f}'.format(3.14, -3.14)  # mostra um espaço para números positivos
   ' 3.140000; -3.140000'
   >>> '{:-f}; {:-f}'.format(3.14, -3.14)  # mostra apenas o sinal de menos -- o mesmo que '{:f}; {:f}'
   '3.140000; -3.140000'

Substituindo "%x" e "%o" e convertendo o valor para bases diferentes:

   >>> # format também tem suporte a números binários
   >>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
   'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
   >>> # com 0x, 0o ou 0b como prefixo:
   >>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
   'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

Usando a vírgula ou o sublinhado como separador de grupos de dígitos:

   >>> '{:,}'.format(1234567890)
   '1,234,567,890'
   >>> '{:_}'.format(1234567890)
   '1_234_567_890'
   >>> '{:_b}'.format(1234567890)
   '100_1001_1001_0110_0000_0010_1101_0010'
   >>> '{:_x}'.format(1234567890)
   '4996_02d2'
   >>> '{:_}'.format(123456789.123456789)
   '123_456_789.12345679'
   >>> '{:.,}'.format(123456789.123456789)
   '123456789.123,456,79'
   >>> '{:,._}'.format(123456789.123456789)
   '123,456,789.123_456_79'

Expressando uma porcentagem:

   >>> points = 19
   >>> total = 22
   >>> 'Correct answers: {:.2%}'.format(points/total)
   'Correct answers: 86.36%'

Usando formatação específica do tipo:

   >>> import datetime as dt
   >>> d = dt.datetime(2010, 7, 4, 12, 15, 58)
   >>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
   '2010-07-04 12:15:58'

Aninhando argumentos e exemplos mais complexos:

   >>> for align, text in zip('<^>', ['left', 'center', 'right']):
   ...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
   ...
   'left<<<<<<<<<<<<'
   '^^^^^center^^^^^'
   '>>>>>>>>>>>right'
   >>>
   >>> octets = [192, 168, 0, 1]
   >>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
   'C0A80001'
   >>> int(_, 16)
   3232235521
   >>>
   >>> width = 5
   >>> for num in range(5,12):
   ...     for base in 'dXob':
   ...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
   ...     print()
   ...
       5     5     5   101
       6     6     6   110
       7     7     7   111
       8     8    10  1000
       9     9    11  1001
      10     A    12  1010
      11     B    13  1011


Strings template ($-strings)
============================

Nota:

  O recurso descrito aqui foi introduzido no Python 2.4; um método de
  modelagem simples baseado em expressões regulares. Ele é anterior a
  "str.format()", literais de strings formatadas e literais de strings
  templates.Não tem relação com os literais de string template
  (t-strings), introduzidos no Python 3.14. Estes são avaliados como
  objetos da classe "string.templatelib.Template", encontrados no
  módulo "string.templatelib".

Strings template fornecem substituições de string mais simples,
conforme descrito em **PEP 292**. Um caso de uso primário para strings
template é a internacionalização (i18n), uma vez que, nesse contexto,
a sintaxe e a funcionalidade mais simples tornam mais fácil traduzir
do que outros recursos embutidos de formatação de strings no Python.
Como um exemplo de biblioteca construída sobre strings template para
i18n, veja o pacote flufl.i18n.

Strings template oferecem suporte a substituições baseadas em "$",
usando as seguintes regras:

* "$$" é um escape; é substituído por um único "$".

* "$identifier" nomeia um espaço reservado de substituição
  correspondente à chave de mapeamento ""identifier"". Por padrão,
  ""identifier"" é restrito a qualquer string ASCII alfanumérica que
  não distingue maiúsculas e minúsculas (incluindo sublinhados) e que
  começa com um sublinhado ou com uma letra ASCII. O primeiro
  caractere não identificador após o caractere "$" termina esta
  especificação de espaço reservado.

* "${identifier}"  é equivalente a "$identifier". É necessário quando
  caracteres identificadores válidos seguem o marcador de posição, mas
  não fazem parte do marcador, como ""${noun}ification"".

Qualquer outra ocorrência de "$" na string resultará em uma
"ValueError" sendo levantada.

O módulo "string" fornece uma classe "Template" que implementa essas
regras. Os métodos de "Template" são:

class string.Template(template)

   O construtor recebe um único argumento que é a string template

   substitute(mapping={}, /, **kwds)

      Executa a substituição do modelo, retornando uma nova string.
      *mapping* é qualquer objeto dicionário ou similar com chaves que
      correspondem aos marcadores de posição no modelo. Como
      alternativa, você pode fornecer argumentos nomeados, os quais
      são espaços reservados. Quando *mapping* e *kwds* são fornecidos
      e há duplicatas, os marcadores de *kwds* têm precedência.

   safe_substitute(mapping={}, /, **kwds)

      Como "substitute()", exceto que se os espaços reservados
      estiverem faltando em *mapping* e *kwds*, em vez de levantar uma
      exceção "KeyError", o espaço reservado original aparecerá na
      string resultante intacta. Além disso, ao contrário de
      "substitute()", qualquer outra ocorrência de "$" simplesmente
      retornará "$" em vez de levantar "ValueError".

      Embora outras exceções ainda possam ocorrer, esse método é
      chamado de "seguro" porque sempre tenta retornar uma string
      utilizável em vez de levantar uma exceção. Em outro sentido,
      "safe_substitute()" pode ser qualquer coisa diferente de seguro,
      uma vez que irá ignorar silenciosamente modelos malformados
      contendo delimitadores pendentes, chaves não correspondidas ou
      espaços reservados que não são identificadores Python válidos.

   is_valid()

      Retorna "False" se o modelo tiver espaços reservados inválidos
      que farão com que "substitute()" levante "ValueError".

      Adicionado na versão 3.11.

   get_identifiers()

      Retorna uma lista dos identificadores válidos no modelo, na
      ordem em que aparecem pela primeira vez, ignorando quaisquer
      identificadores inválidos.

      Adicionado na versão 3.11.

   Instâncias de "Template" também fornecem um atributo de dados
   públicos:

   template

      Este é o objeto passado para o argumento *template* do
      construtor. Em geral, você não deve alterá-lo, mas o acesso
      somente leitura não é obrigatório.

Aqui está um exemplo de como usar uma instância de Template:

   >>> from string import Template
   >>> s = Template('$who likes $what')
   >>> s.substitute(who='tim', what='kung pao')
   'tim likes kung pao'
   >>> d = dict(who='tim')
   >>> Template('Give $who $100').substitute(d)
   Traceback (most recent call last):
   ...
   ValueError: Invalid placeholder in string: line 1, col 11
   >>> Template('$who likes $what').substitute(d)
   Traceback (most recent call last):
   ...
   KeyError: 'what'
   >>> Template('$who likes $what').safe_substitute(d)
   'tim likes $what'

Uso avançado: você pode derivar subclasses de "Template" para
personalizar a sintaxe do espaço reservado, caractere delimitador ou
toda a expressão regular usada para analisar strings template. Para
fazer isso, você pode substituir estes atributos de classe:

* *delimiter* -- Este é a string literal que descreve um delimitador
  de introdução do espaço reservado. O valor padrão é "$". Note que
  esta *não* deve ser uma expressão regular, já que a implementação
  irá chamar "re.escape()" nesta string conforme necessário. Observe
  também que você não pode alterar o delimitador após a criação da
  classe (ou seja, um delimitador diferente deve ser definido no
  espaço de nomes da classe da subclasse).

* *idpattern* -- Esta é a expressão regular que descreve o padrão para
  espaço reservado sem envolto em chaves. O valor padrão é a expressão
  regular "(?a:[_a-z][_a-z0-9]*)". Se for fornecido e *braceidpattern*
  for "None", esse padrão também se aplicará o espaço reservado com
  chaves.

  Nota:

    Uma vez que *flags* padrão é "re.IGNORECASE", o padrão "[a-z]"
    pode corresponder a alguns caracteres não ASCII. É por isso que
    usamos o sinalizador local "a" aqui.

  Alterado na versão 3.7: *braceidpattern* pode ser usado para definir
  padrões separados usados dentro e fora das chaves.

* *braceidpattern* -- É como *idpattern*, mas descreve o padrão para
  espaços reservados com chaves. O padrão é "None", o que significa
  recorrer a *idpattern* (ou seja, o mesmo padrão é usado dentro e
  fora das chaves). Se fornecido, permite definir padrões diferentes
  para espaço reservado com e sem chaves.

  Adicionado na versão 3.7.

* *flags* -- Os sinalizadores de expressão regular que serão aplicados
  ao compilar a expressão regular usada para reconhecer substituições.
  O valor padrão é "re.IGNORECASE". Note que "re.VERBOSE" sempre será
  adicionado aos sinalizadores, então *idpattern*s personalizados
  devem seguir as convenções para expressões regulares verbosas.

  Adicionado na versão 3.2.

Como alternativa, você pode fornecer todo o padrão de expressão
regular substituindo o atributo *pattern* de classe. Se você fizer
isso, o valor deve ser uma string de padrão de expressão regular, ou
um objeto compilado de expressão regular, com quatro grupos de captura
nomeados. Os grupos de captura correspondem às regras fornecidas
acima, junto com a regra inválida do espaço reservado:

* *escaped* -- Este grupo corresponde à sequência de escape, por
  exemplo "$$", no padrão.

* *named* -- Este grupo corresponde ao nome do espaço reservado sem
  chaves; não deve incluir o delimitador no grupo de captura.

* *braced* -- Este grupo corresponde ao nome do espaço reservado entre
  chaves; ele não deve incluir o delimitador ou chaves no grupo de
  captura.

* *invalid* -- Esse grupo corresponde a qualquer outro padrão de
  delimitador (geralmente um único delimitador) e deve aparecer por
  último na expressão regular.

Os métodos nesta classe irão levantar "ValueError" se o padrão
corresponder ao modelo sem que um desses grupos nomeados corresponda.


Funções auxiliares
==================

string.capwords(s, sep=None)

   Divide o argumento em palavras usando "str.split()", coloca cada
   palavra em maiúscula usando "str.capitalize()", e junte as palavras
   em maiúsculas usando "str.join()". Se o segundo argumento opcional
   *sep* estiver ausente ou "None", os caracteres de espaço em branco
   são substituídos por um único espaço e os espaços em branco à
   esquerda e à direita são removidos, caso contrário *sep* é usado
   para dividir e unir as palavras.
