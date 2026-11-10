2. Análise léxica
*****************

Um programa Python é lido por um *analisador sintático*. A entrada
para o analisador sintático é um fluxo de *tokens*, gerados pelo
*analisador léxico* (também conhecido como *tokenizador*). Este
capítulo descreve como o analisador léxico produz esses tokens.

O analisador léxico determina a codificação do texto do programa
(UTF-8 por padrão), e o decodifica em caracteres da fonte. Se o texto
não puder ser decodificado, uma "SyntaxError" é levantada.

Em seguida, o analisador léxico usa os caracteres da fonte para gerar
um fluxo de tokens. Geralmente, o tipo de um token gerado depende do
próximo caracter da fonte a ser processado. Além disso, outros
comportamentos especiais do analisador também dependem do primeiro
caracter da fonte que ainda não foi processado. A seguinte tabela é um
resumo desses caracteres da fonte, com links para seções que contém
mais informação.

+----------------------------------------------------+----------------------------------------------------+
| Caractere                                          | Token seguinte (ou outra documentação relevante)   |
|====================================================|====================================================|
| * espaço  * tabulação  * quebra de página          | * Espaço em branco                                 |
+----------------------------------------------------+----------------------------------------------------+
| * CR, LF                                           | * Nova linha  * Indentação                         |
+----------------------------------------------------+----------------------------------------------------+
| * contrabarra ("\")                                | * Junção de linha explícita  * (Importante também  |
|                                                    | em sequências de escape em strings)                |
+----------------------------------------------------+----------------------------------------------------+
| * tralha ("#")                                     | * Comentário                                       |
+----------------------------------------------------+----------------------------------------------------+
| * aspas ("'", """)                                 | * Literal de string                                |
+----------------------------------------------------+----------------------------------------------------+
| * Letra ASCII ("a"-"z", "A"-"Z")  * Caractere não- | * Nome  * Literal de string ou bytes prefixado.    |
| ASCII                                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| * Sublinhado ("_")                                 | * Nome  * (Também pode ser parte de numerais       |
|                                                    | literais)                                          |
+----------------------------------------------------+----------------------------------------------------+
| * número ("0"-"9")                                 | * Numeral literal                                  |
+----------------------------------------------------+----------------------------------------------------+
| * ponto (".")                                      | * Numeral literal  * Operador                      |
+----------------------------------------------------+----------------------------------------------------+
| * ponto de interrogação ("?")  * cifrão ("$")  *   | * Erro (fora de literais de string e comentários)  |
| acento grave, crase, ou backquote ("​`​")  *       |                                                    |
| caractere de controle                              |                                                    |
+----------------------------------------------------+----------------------------------------------------+
| * Outro caractere exibível                         | * Operador ou delimitador                          |
+----------------------------------------------------+----------------------------------------------------+
| * fim do arquivo                                   | * Marcador de fim                                  |
+----------------------------------------------------+----------------------------------------------------+


2.1. Estrutura das linhas
=========================

Um programa Python é dividido em uma série de *linhas lógicas*.


2.1.1. Linhas lógicas
---------------------

O fim de uma linha lógica é representado pelo token "NEWLINE". As
instruções não podem cruzar os limites da linha lógica, exceto onde
"NEWLINE" for permitido pela sintaxe (por exemplo, entre as instruções
de instruções compostas). Uma linha lógica é construída a partir de
uma ou mais *linhas físicas* seguindo as regras explícitas ou
implícitas que *juntam as linhas*.


2.1.2. Linhas físicas
---------------------

Uma linha física é uma sequência de caracteres terminada por uma das
seguintes sequências de fim de linha:

* o formulário Unix usando ASCII LF (avanço de linha),

* o formulário do Windows usando a sequência ASCII CR LF (retorno
  seguido de avanço de linha),

* o formato 'Classic Mac OS' usando o caractere ASCII CR (retorno).

Independentemente da plataforma, cada uma dessas sequências é
substituída por um único caractere ASCII LF (avanço de linha). (Isso é
feito até mesmo dentro de literais de string.) Cada linha pode usar
qualquer uma das sequências; elas não precisam ser consistentes dentro
de um arquivo.

O fim da entrada também serve como um terminador implícito para a
linha física final.

Formalmente:

   newline: <ASCII LF> | <ASCII CR> <ASCII LF> | <ASCII CR>


2.1.3. Comentários
------------------

Um  comentário inicia com um caracter cerquilha ("#") que não é parte
de uma string literal, e termina com o fim da linha física.  Um
comentário significa o fim da linha lógica a menos que regras de
junção de linha implicitas sejam invocadas. Comentários são ignorados
pela sintaxe.


2.1.4. Declarações de codificação
---------------------------------

Se um comentário na primeira ou segunda linha de um script Python
corresponde com a expressão regular  "coding[=:]\s*([-\w.]+)", esse
comentário é processado com uma declaração de codificação; o primeiro
grupo dessa expressão indica a codificação do arquivo do código-fonte.
A declaração de codificação deve aparecer em uma linha exclusiva para
tal. Se está na segunda linha, a primeira linha também deve ser uma
linha somente com comentário. As formas recomendadas de uma declaração
de codificação são:

   # -*- coding: <nome-codificação> -*-

que é reconhecido também por GNU Emacs, e

   # vim:fileencoding=<nome-codificação>

que é reconhecido pelo VIM de Bram Moolenaar.

Se nenhuma codificação é declarada, a codificação padrão é UTF-8. Se a
codificação implícita ou explícita de um arquivo é UTF-8,  uma marca
inicial de ordem de byte UTF-8 ("b'\xef\xbb\xbf'") será ignorada em
vez de ser um erro de sintaxe.

Se uma codificação é declarada, o nome da codificação deve ser
reconhecida pelo Python (veja Standard Encodings). A codificação é
usada por toda análise léxica, incluindo literais strings, comment and
identificadores.

Toda a análise lexical, incluindo literais de string, comentários e
identificadores, funciona em texto Unicode decodificado usando a
codificação de origem. Qualquer ponto de código Unicode, exceto o
caractere de controle NUL, pode aparecer no código-fonte Python.

   source_character:  <any Unicode code point, except NUL>


2.1.5. Junção de linha explícita
--------------------------------

Duas ou mais linhas físicas podem ser juntadas em linhas lógicas
usando o caractere contrabarra  ("\") da seguinte forma: quando uma
linha física termina com uma contrabarra que não é parte da uma
literal string ou comentário, ela é juntada com a linha seguinte
formando uma única linha lógica, removendo a contrabarra e o caractere
de fim de linha seguinte. Por exemplo:

   if 1900 < year < 2100 and 1 <= month <= 12 \
      and 1 <= day <= 31 and 0 <= hour < 24 \
      and 0 <= minute < 60 and 0 <= second < 60:   # Parece ser uma data válida
           return 1

Uma linha terminada em uma contrabarra não pode conter um comentário.
Uma barra invertida não continua um comentário.  Uma contrabarra não
continua um token, exceto para strings literais (ou seja, tokens
diferentes de strings literais não podem ser divididos em linhas
físicas usando uma contrabarra).  Uma contrabarra é ilegal em qualquer
outro lugar em uma linha fora de uma string literal.


2.1.6. Junção de linha implícita
--------------------------------

Expressões entre parênteses, colchetes ou chaves podem ser quebradas
em mais de uma linha física sem a necessidade do uso de contrabarras.
Por exemplo:

   month_names = ['Januari', 'Februari', 'Maart',      # Estes são os
                  'April',   'Mei',      'Juni',       # nomes holandeses
                  'Juli',    'Augustus', 'September',  # para os meses
                  'Oktober', 'November', 'December']   # do ano

Linhas continuadas implicitamente podem conter comentários. O recuo
das linhas de continuação não é importante. Linhas de continuação em
branco são permitidas. Não há token NEWLINE entre linhas de
continuação implícitas. Linhas continuadas implicitamente também podem
ocorrer dentro de strings com aspas triplas (veja abaixo); nesse caso,
eles não podem conter comentários.


2.1.7. Linhas em branco
-----------------------

Uma linha lógica que contém apenas espaços, tabulações, quebras de
página e possivelmente um comentário é ignorada (ou seja, nenhum token
"NEWLINE" é gerado). Durante a entrada interativa de instruções, o
tratamento de uma linha em branco pode diferir dependendo da
implementação do interpretador. No interpretador interativo padrão,
uma linha lógica totalmente em branco (ou seja, uma que não contenha
nem mesmo espaço em branco ou um comentário) encerra uma instrução
multilinha.


2.1.8. Indentação
-----------------

O espaço em branco (espaços e tabulações) no início de uma linha
lógica é usado para calcular o nível de indentação da linha, que por
sua vez é usado para determinar o agrupamento de instruções.

As tabulações são substituídas (da esquerda para a direita) por um a
oito espaços, de modo que o número total de caracteres até e incluindo
a substituição seja um múltiplo de oito (essa é intencionalmente a
mesma regra usada pelo Unix). O número total de espaços que precedem o
primeiro caractere não em branco determina o recuo da linha. O recuo
não pode ser dividido em várias linhas físicas usando contrabarra; o
espaço em branco até a primeira contrabarra determina a indentação.

A indentação é rejeitada como inconsistente se um arquivo de origem
mistura tabulações e espaços de uma forma que torna o significado
dependente do valor de uma tabulação em espaços; uma exceção
"TabError" é levantada nesse caso.

**Nota de compatibilidade entre plataformas:** devido à natureza dos
editores de texto em plataformas não-UNIX, não é aconselhável usar uma
mistura de espaços e tabulações para o recuo em um único arquivo de
origem. Deve-se notar também que diferentes plataformas podem limitar
explicitamente o nível máximo de indentação.

Um caractere de quebra de página pode estar presente no início da
linha; ele será ignorado para os cálculos de indentação acima. Os
caracteres de quebra de página que ocorrem em outro lugar além do
espaço em branco inicial têm um efeito indefinido (por exemplo, eles
podem redefinir a contagem de espaços para zero).

Os níveis de indentação das linhas consecutivas são usados para gerar
tokens "INDENT" e "DEDENT", usando uma pilha, como segue.

Antes da leitura da primeira linha do arquivo, um único zero é
colocado na pilha; esse valor nunca mais será exibido. Os números
colocados na pilha sempre aumentarão estritamente de baixo para cima.
No início de cada linha lógica, o nível de indentação da linha é
comparado ao topo da pilha. Se for igual, nada acontece. Se for maior,
ele é colocado na pilha e é gerado um token "INDENT". Se for menor,
*deve* ser um dos números que aparecem na pilha; todos os números
maiores na pilha são retirados e, para cada número retirado, é gerado
um token "DEDENT". Ao final do arquivo, um token "DEDENT" é gerado
para cada número restante na pilha que seja maior que zero.

Aqui está um exemplo de um trecho de código Python indentado
corretamente (embora confuso):

   def perm(l):
           # Calcula a lista de todas as permutações de l
       if len(l) <= 1:
                     return [l]
       r = []
       for i in range(len(l)):
                s = l[:i] + l[i+1:]
                p = perm(s)
                for x in p:
                 r.append(l[i:i+1] + x)
       return r

O exemplo a seguir mostra vários erros de indentação:

    def perm(l):                       # erro: primeira linha indentada
   for i in range(len(l)):             # erro: não indentada
       s = l[:i] + l[i+1:]
           p = perm(l[:i] + l[i+1:])   # erro: indentação inesperada
           for x in p:
                   r.append(l[i:i+1] + x)
               return r                # erro: desindentação inconsistente

(Na verdade, os três primeiros erros são detectados pelo analisador
sintático; apenas o último erro é encontrado pelo analisador léxico
--- o recuo de não corresponde a um nível retirado da pilha.)


2.1.9. Espaços em branco entre tokens
-------------------------------------

Exceto no início de uma linha lógica ou em literais de string, os
caracteres de espaço em branco (espaço, tabulação e avanço de página)
podem ser usados indistintamente para separar tokens:

   whitespace:  ' ' | tab | formfeed

O espaço em branco é necessário entre dois tokens somente se sua
concatenação puder ser interpretada como um token diferente (por
exemplo, "ab" é um token, mas "a b" são dois tokens). Entretanto, "+a"
e "+ a" produzem dois tokens, "+" e "a", pois "+a" não é um token
válido.


2.1.10. Marcador de fim
-----------------------

No final da entrada não interativa, o analisador léxico gera um token
"ENDMARKER".


2.2. Outros tokens
==================

Além de "NEWLINE", "INDENT" e "DEDENT", existem as seguintes
categorias de tokens: *identificadores*, *palavras-chave* ("NAME"),
*literais* (como "NUMBER" e "STRING") e outros símbolos (*operadores*
e *delimitadores*, "OP"). Caracteres de espaço em branco (exceto os
terminadores lógicos de linha, discutidos anteriormente) não são
tokens, mas servem para delimitar tokens. Onde há ambiguidade, um
token compreende a string mais longa possível que forma um token
legal, quando lido da esquerda para a direita.


2.3. Nomes (identificadores e palavras reservadas)
==================================================

Tokens "NAME" representam *identificadores*, *palavras reservadas* e
*palavras reservadas contextuais*.

Nomes são compostos dos seguintes caracteres:

* letras maiúsculas e minúsculas ("A-Z" e "a-z"),

* o sublinhado ("_"),

* dígitos ("0" a "9"), que não podem aparecer como o primeiro
  caractere, e

* caracteres não ASCII. Nomes válidos podem conter apenas caracteres
  "semelhantes a letras" e "semelhantes a dígitos"; consulte
  Caracteres não ASCII em nomes para obter detalhes.

Os nomes devem conter pelo menos um caractere, mas não há limite
máximo de tamanho. Maiúsculas e minúsculas são relevantes.

Formalmente, nomes são descritos pelas seguintes definições léxicas:

   NAME:          name_start name_continue*
   name_start:    "a"..."z" | "A"..."Z" | "_" | <non-ASCII character>
   name_continue: name_start | "0"..."9"
   identifier:    <NAME, except keywords>

Observe que nem todos os nomes correspondentes a esta gramática são
válidos; consulte Caracteres não ASCII em nomes para obter detalhes.


2.3.1. Palavras reservadas
--------------------------

Os nomes a seguir são usados como palavras reservadas e não podem ser
usados como identificadores comuns. Eles devem ser escritos exatamente
como estão escritos aqui:

   False      await      else       import     pass
   None       break      except     in         raise
   True       class      finally    is         return
   and        continue   for        lambda     try
   as         def        from       nonlocal   while
   assert     del        global     not        with
   async      elif       if         or         yield


2.3.2. Palavras reservadas contextuais
--------------------------------------

Adicionado na versão 3.10.

Alguns nomes são reservados apenas em contextos específicos. São
conhecidos como *palavras reservadas contextuais*:

* "match", "case" e "_", quando usados na instrução "match".

* "type", quando usado na instrução "type".

* "lazy", quando usado antes de uma instrução "import".

Elas agem sintaticamente como palavra reservada em seus contextos
específicos, mas essa distinção é feita no nível do analisador
sintático, não na tokenização.

Como palavras reservadas contextuais, seu uso na gramática é possível
preservando a compatibilidade com o código existente que usa esses
nomes como identificadores.

Alterado na versão 3.12: "type" é agora uma palavra reservada
contextual.

Alterado na versão 3.15: "lazy" agora é uma palavra reservada
contextual.


2.3.3. Classes reservadas de identificadores
--------------------------------------------

Certas classes de identificadores (além de palavras reservadas)
possuem significados especiais. Essas classes são identificadas pelos
padrões de caracteres de sublinhado iniciais e finais:

"_*"
   Não importado por "from module import *".

"_"
   Em um padrão "case" de uma instrução "match", "_" é uma palavra
   reservada contextual que denota um curinga.

   Isoladamente, o interpretador interativo disponibiliza o resultado
   da última avaliação na variável "_". (Ele é armazenado no módulo
   "builtins", juntamente com funções embutidas como "print".)

   Em outros lugares, "_" é um identificador comum. Muitas vezes é
   usado para nomear itens "especiais", mas não é especial para o
   Python em si.

   Nota:

     O nome "_" é frequentemente usado em conjunto com
     internacionalização; consulte a documentação do módulo "gettext"
     para obter mais informações sobre esta convenção.Também é
     comumente usado para variáveis não utilizadas.

"__*__"
   Nomes definidos pelo sistema, informalmente conhecidos como nomes
   "dunder". Esses nomes e suas implementações são definidos pelo
   interpretador (incluindo a biblioteca padrão). Os nomes de sistema
   atuais são discutidos na seção Nomes de métodos especiais e em
   outros lugares. Provavelmente mais nomes serão definidos em versões
   futuras do Python. *Qualquer* uso de nomes "__*__", em qualquer
   contexto, que não siga o uso explicitamente documentado, está
   sujeito a quebra sem aviso prévio.

"__*"
   Nomes de classes privadas. Os nomes nesta categoria, quando usados
   no contexto de uma definição de classe, são reescritos para usar
   uma forma desfigurada para ajudar a evitar conflitos de nomes entre
   atributos "privados" de classes base e derivadas. Consulte a seção
   Identificadores (Nomes).


2.3.4. Caracteres não ASCII em nomes
------------------------------------

Nomes que contêm caracteres não ASCII precisam de normalização e
validação adicionais além das regras e gramática explicadas acima. Por
exemplo, "ř_1", "蛇" ou "साँप" são nomes válidos, mas "r〰2", "€" ou "
🐍" não são.

Esta seção explica as exatas regras.

Todos os nomes são convertidos para a forma de normalização NFKC
durante a análise sintática. Isso significa que, por exemplo, algumas
variantes tipográficas de caracteres são convertidas para sua forma
"básica". Por exemplo, "ﬁⁿₐˡᵢᶻₐᵗᵢᵒₙ" é normalizado para
"finalization", então o Python os trata como o mesmo nome:

   >>> ﬁⁿₐˡᵢᶻₐᵗᵢᵒₙ = 3
   >>> finalization
   3

Nota:

  A normalização é feita apenas no nível léxico. Funções de tempo de
  execução que recebem nomes como *strings* geralmente não normalizam
  seus argumentos. Por exemplo, a variável definida acima é acessível
  em tempo de execução no dicionário "globals()" como
  "globals()["finalization"]", mas não como
  "globals()["ﬁⁿₐˡᵢᶻₐᵗᵢᵒₙ"]".

Assim como os nomes que usam apenas ASCII devem conter somente letras,
dígitos e o sublinhado, e não podem começar com um dígito, um nome
válido deve começar com um caractere do conjunto "semelhante a letras"
"xid_start", e os caracteres restantes devem estar no conjunto
"semelhante a letras e dígitos" "xid_continue".

Esses conjuntos são baseados nos conjuntos *XID_Start* e
*XID_Continue*, conforme definidos pelo anexo UAX-31 do padrão
Unicode. O "xid_start" do Python inclui adicionalmente o sublinhado
("_"). Observe que o Python não está necessariamente em conformidade
com o UAX-31.

Uma lista não normativa de caracteres nos conjuntos *XID_Start* e
*XID_Continue*, conforme definidos pelo Unicode, está disponível no
arquivo DerivedCoreProperties.txt no Banco de Dados de Caracteres
Unicode. Para referência, as regras de construção para os conjuntos
"xid_*" são apresentadas abaixo.

O conjunto "id_start" é definido como a união de:

* Categoria Unicode "<Lu>" - letras maiúsculas (inclui "A" a "Z")

* Categoria Unicode "<Ll>" - letras minúsculas (inclui "a" a "z")

* Categoria Unicode "<Lt>" - letras em titlecase (coloca em maiúsculo
  a primeira letra de cada palavra principal)

* Categoria Unicode "<Lm>" - letras modificadoras

* Categoria Unicode "<Lo>" - outras letras

* Categoria Unicode "<Nl>" - números de letras

* {""_""} - o underscore (sublinhado)

* "<Other_ID_Start>" - um conjunto explícito de caracteres em
  PropList.txt para oferecer suporte à retrocompatibilidade

O conjunto "xid_start" fecha então este conjunto sob a normalização
NFKC, removendo todos os caracteres cuja normalização não é da forma
"id_start id_continue*".

O conjunto "id_continue" é definido como a união de:

* "id_start" (veja acima)

* Categoria Unicode "<Nd>" - números decimais (inclui "0" a "9")

* Categoria Unicode "<Pc>" - pontuações de conectores

* Categoria Unicode "<Mn>" - marcas sem espaçamento

* Categoria Unicode "<Mc>" - espaçamento combinando marcas

* "<Other_ID_Continue>" - outro conjunto explícito de caracteres em
  PropList.txt para oferecer suporte à retrocompatibilidade

Novamente, "xid_continue" fecha este conjunto sob a normalização NFKC.

As categorias Unicode usam a versão do Unicode Character Database (em
português, banco de dados de caracteres Unicode) incluída no módulo
"unicodedata".

Ver também:

  * **PEP 3131** -- Suporte a identificadores não-ASCII

  * **PEP 672** -- Considerações de segurança relacionadas ao Unicode
    para Python


2.4. Literais
=============

Literais são notações para valores constantes de alguns tipos
embutidos.

Em termos de análise lexical, Python tem literais de string, de bytes
e numéricos.

Outros "literais" são denotados lexicamente usando palavra reservada
("None", "True", "False") e o token de reticências especial ("...").


2.5. Literais de string e bytes
===============================

Literais de string são textos entre aspas simples ("'") ou aspas
duplas ("""). Por exemplo:

   "spam"
   'eggs'

A aspa usada para iniciar o literal também o encerra, portanto, um
literal de string só pode conter a outra aspa (exceto com sequências
de escape, veja abaixo). Por exemplo:

   'Diga "Olá", por favor.'
   "Não faça isso!"

Exceto por essa limitação, a escolha do caractere de aspas ("'" ou
""") não afeta como o literal é analisado.

Dentro de uma literal de string, o caractere de contrabarra ("\")
introduz uma sequência de escape *, que tem um significado especial
dependendo do caractere após a contrabarra. Por exemplo, `*"`` denota
o caractere de aspas duplas e *não* encerra a string:

   >>> print("Diga \"Olá\" para todo mundo!")
   Diga "Olá" para todo mundo!

Veja sequências de escape abaixo para uma lista completa dessas
sequências e mais detalhes.


2.5.1. Strings entre aspas triplas
----------------------------------

Strings também podem ser colocadas emgrupos correspondentes de três
aspas simples ou duplas. Geralmente, elas são chamadas de *strings
entre aspas triplas*:

   """Isso é uma string entre aspas triplas."""

Em literais com aspas triplas, aspas sem escape são permitidas (e são
mantidas), exceto que três aspas sem escape seguidas encerram o
literal, se forem do mesmo tipo ("'" ou """) usadas no início:

   """Essa string tem "aspas" dentro."""

Novas linhas sem escape também são permitidas e mantidas:

   '''Essa string entre aspas triplas
   continua na linha seguinte.'''


2.5.2. Prefixos de string
-------------------------

Literais de string podem ter um *prefixo* opcional que influencia como
o conteúdo do literal é analisado, por exemplo:

   b"data"
   f'{result=}'

Os prefixos permitidos são:

* "b": Literal de bytes

* "r": String bruta

* "f": Literal de string formatada ("f-string")

* "t": Literal de string template ("t-string")

* "u": Sem efeito (permitido para retrocompatibilidade)

Veja as seções vinculadas para obter detalhes sobre cada tipo.

Prefixos não diferenciam maiúsculas de minúsculas (por exemplo, '"B"'
funciona da mesma forma que '"b"'). O prefixo '"r"' pode ser combinado
com '"f"', '"t"' ou '"b"', portanto, '"fr"', '"rf"', '"tr"', '"rt"',
'"br"' e '"rb"' também são prefixos válidos.

Adicionado na versão 3.3: O prefixo "'rb'" de literais de bytes brutos
foi adicionado como sinônimo de "'br'".O suporte para o literal legado
unicode ("u'value'") foi reintroduzido para simplificar a manutenção
de bases de código duplas Python 2.x e 3.x. Consulte **PEP 414** para
obter mais informações.


2.5.3. Gramática formal
-----------------------

Literais de string, exceto "f-strings" e "t-strings", são descritos
pelas seguintes definições lexicais.

Essas definições usam negative lookaheads ("!") para indicar que uma
aspa final encerra o literal.

   STRING:          [stringprefix] (stringcontent)
   stringprefix:    <("r" | "u" | "b" | "br" | "rb"), case-insensitive>
   stringcontent:
      | "'''" ( !"'''" longstringitem)* "'''"
      | '"""' ( !'"""' longstringitem)* '"""'
      | "'" ( !"'" stringitem)* "'"
      | '"' ( !'"' stringitem)* '"'
   stringitem:      stringchar | stringescapeseq
   stringchar:      <any source_character, except backslash and newline>
   longstringitem:  stringitem | newline
   stringescapeseq: "\" <any source_character>

Observe que, como em todas as definições lexicais, os espaços em
branco são significativos. Em particular, o prefixo (se houver) deve
ser imediatamente seguido pela aspa inicial.


2.5.4. Sequências de escape
---------------------------

A menos que um prefixo '"r"' ou '"R"' esteja presente, as sequências
de escape em literais de string e bytes são interpretadas de acordo
com regras semelhantes àquelas usadas pelo Standard C. As sequências
de escape reconhecidas são:

+----------------------------------------------------+----------------------------------------------------+
| Sequência de escape                                | Significado                                        |
|====================================================|====================================================|
| "\"<newline>                                       | Fim de linha ignorado                              |
+----------------------------------------------------+----------------------------------------------------+
| "\\"                                               | Contrabarra                                        |
+----------------------------------------------------+----------------------------------------------------+
| "\'"                                               | Aspa simples                                       |
+----------------------------------------------------+----------------------------------------------------+
| "\""                                               | Aspas duplas                                       |
+----------------------------------------------------+----------------------------------------------------+
| "\a"                                               | ASCII Bell (BEL) - um sinal audível é emitido      |
+----------------------------------------------------+----------------------------------------------------+
| "\b"                                               | ASCII Backspace (BS) - apaga caractere à esquerda  |
+----------------------------------------------------+----------------------------------------------------+
| "\f"                                               | ASCII Formfeed (FF) - quebra de página             |
+----------------------------------------------------+----------------------------------------------------+
| "\n"                                               | ASCII Linefeed (LF) - quebra de linha              |
+----------------------------------------------------+----------------------------------------------------+
| "\r"                                               | ASCII Carriage Return (CR) - retorno de carro      |
+----------------------------------------------------+----------------------------------------------------+
| "\t"                                               | ASCII Horizontal Tab (TAB) - tabulação horizontal  |
+----------------------------------------------------+----------------------------------------------------+
| "\v"                                               | ASCII Vertical Tab (VT) - tabulação vertical       |
+----------------------------------------------------+----------------------------------------------------+
| "\*ooo*"                                           | Caractere octal                                    |
+----------------------------------------------------+----------------------------------------------------+
| "\x*hh*"                                           | Caractere hexadecimal                              |
+----------------------------------------------------+----------------------------------------------------+
| "\N{*name*}"                                       | Caractere nomeado Unicode                          |
+----------------------------------------------------+----------------------------------------------------+
| "\u*xxxx*"                                         | Caractere hexadecimal Unicode                      |
+----------------------------------------------------+----------------------------------------------------+
| "\U*xxxxxxxx*"                                     | Caractere hexadecimal Unicode                      |
+----------------------------------------------------+----------------------------------------------------+


2.5.4.1. Fim de linha ignorado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Uma contrabarra pode ser adicionada ao fim da linha para ignorar a
nova linha:

   >>> 'Esta string não vai incluir \
   ... contrabarras e caracteres de nova linha.'
   'Esta string não vai incluir contrabarras e caracteres de nova linha.'

O mesmo resultado pode ser obtido usando strings com aspas triplas, ou
parênteses e concatenação de literal string.


2.5.4.2. Caracteres escapados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para incluir uma contrabarra em um literal de string não-bruta Python,
ela deve ser duplicada. A sequência de escape "\\" denota um único
caractere de contrabarra:

   >>> print('C:\\Program Files')
   C:\Program Files

Da mesma forma, as sequências "\'" e "\"" denotam os caracteres de
aspas simples e duplas, respectivamente:

   >>> print('\' e \"')
   ' e "


2.5.4.3. Caractere octal
~~~~~~~~~~~~~~~~~~~~~~~~

A sequência "\*ooo*" denota um *caractere* com o valor octal (base 8)
*ooo*:

   >>> '\120'
   'P'

São aceitos até três dígitos octais (0 a 7).

Em um literal de bytes, *caractere* significa um *byte* com o valor
fornecido. Em um literal de string, significa um caractere Unicode com
o valor fornecido.

Alterado na versão 3.11: Escapes octais com valor maior que "0o377"
(255) produz uma "DeprecationWarning".

Alterado na versão 3.12: Escapes octais com valor maior que "0o377"
(255) produzem um "SyntaxWarning". Em uma versão futura do Python eles
eventualmente vão levantar um "SyntaxError".


2.5.4.4. Caractere hexadecimal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A sequência "\x*hh*" denota um *caractere* com o valor hexa (base 16)
*hh*:

   >>> '\x50'
   'P'

Ao contrário do padrão C, são necessários exatamente dois dígitos
hexadecimais.

Em um literal de bytes, *caractere* significa um *byte* com o valor
fornecido. Em um literal de string, significa um caractere Unicode com
o valor fornecido.


2.5.4.5. Caractere nomeado Unicode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A sequência "\N{*nome*}" denota um caractere Unicode com o *nome*
fornecido:

   >>> '\N{LATIN CAPITAL LETTER P}'
   'P'
   >>> '\N{SNAKE}'
   '🐍'

Esta sequência não pode aparecer em literais de bytes.

Alterado na versão 3.3: Foi adicionado suporte a *apelidos para nomes
<https://www.unicode.org/Public/17.0.0/ucd/NameAliases.txt>`__*.


2.5.4.6. Caracteres hexadecimais Unicode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As sequências "\u*xxxx*" e "\U*xxxxxxxx*" denotam o caractere Unicode
com o valor hexadecimal fornecido (base 16). São necessários
exatamente quatro dígitos para "\u"; são necessários exatamente oito
dígitos para "\U". Este último pode codificar qualquer caractere
Unicode.

   >>> '\u1234'
   'ሴ'
   >>> '\U0001f40d'
   '🐍'

Estas sequências não pode aparecer em literais de bytes.


2.5.4.7. Sequências de espace não reconhecidas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Diferentemente do Standard C, todas as sequências de escape não
reconhecidas são deixadas na string inalteradas, ou seja, *a
contrabarra é deixada no resultado*:

   >>> print('\q')
   \q
   >>> list('\q')
   ['\\', 'q']

Observe que, para literais de bytes, as sequências de escape
reconhecidas apenas em literais de string ("\N...", "\u...", "\U...")
se enquadram na categoria de escapes não reconhecidos.

Alterado na versão 3.6: Sequências de escape não reconhecidas produzem
um "DeprecationWarning".

Alterado na versão 3.12: Sequências de escape não reconhecidas
produzem um "SyntaxWarning". Em uma versão futura do Python eles vão
levantar um "SyntaxError".


2.5.5. Literais de bytes
------------------------

*Literais de bytes* são sempre prefixados com '"b"' ou '"B"'; eles
produzem uma instância do tipo "bytes" em vez do tipo "str". Eles
podem conter apenas caracteres ASCII; bytes com valor numérico igual
ou superior a 128 devem ser expressos com sequências de escape
(normalmente Caractere hexadecimal ou Caractere octal):

   >>> b'\x89PNG\r\n\x1a\n'
   b'\x89PNG\r\n\x1a\n'
   >>> list(b'\x89PNG\r\n\x1a\n')
   [137, 80, 78, 71, 13, 10, 26, 10]

Da mesma forma, um byte zero deve ser expresso usando uma sequência de
escape (normalmente "\0" ou "\x00").


2.5.6. Literais de string brutas
--------------------------------

Literais de string e bytes podem opcionalmente ser prefixados com uma
letra '"r"' ou '"R"'; tais construções são chamadas de *literais de
strings brutas* e *literais de bytes brutos* tratam as contrabarras
como caracteres literais. Como resultado, em literais de string bruta,
as sequências de escape não são tratados de maneira especial.

   >>> r'\d{4}-\d{2}-\d{2}'
   '\\d{4}-\\d{2}-\\d{2}'

Mesmo em um literal bruto, as aspas podem ser escapadas com uma
contrabarra, mas a barra invertida permanece no resultado; por
exemplo, "r"\""" é uma literal de string válida que consiste em dois
caracteres: uma contrabarra e aspas duplas; "r"\"" não é uma literal
de string válida (mesmo uma string bruta não pode terminar em um
número ímpar de contrabarras). Especificamente, *um literal bruto não
pode terminar em uma única contrabarra* (já que a contrabarra
escaparia do seguinte caractere de aspas). Observe também que uma
única contrabarra seguida por uma nova linha é interpretada como esses
dois caracteres como parte do literal, *não* como uma continuação de
linha.


2.5.7. Literais de strings formatadas
-------------------------------------

Adicionado na versão 3.6.

Alterado na versão 3.7: "await" e "async for" podem ser usados em
expressões dentro de f-strings.

Alterado na versão 3.8: Adicionado o especificador de depuração ("=")

Alterado na versão 3.12: Muitas restrições a expressões dentro de
f-strings foram removidas. Notavelmente, strings aninhadas,
comentários e contrabarras agora são permitidos.

Um *literal de string formatada* ou uma *f-string* é uma string
literal que começa com '"f"' ou '"F"'. Ao contrário de outras strings
literais, as f-strings não têm um valor constante. Elas podem conter
*campos de substituição* delimitados por chaves "{}". Os campos de
substituição contêm expressões que são avaliadas em tempo de execução.
Por exemplo:

   >>> who = 'Ninguém'
   >>> nationality = 'Espanhola'
   >>> f'{who.title()} está à espera da Inquisição {nationality}!'
   'Ninguém está à espera da Inquisição Espanhola!'

Quaisquer chaves duplas ("{{" ou "}}") fora dos campos de substituição
são substituídas pela chave simples correspondente:

   >>> print(f'{{...}}')
   {...}

Outros caracteres fora dos campos de substituição são tratados como em
literais de string comuns. Isso significa que sequências de escape são
decodificadas (exceto quando um literal também é marcado como uma
string bruta) e quebras de linha são possíveis em f-strings entre
aspas triplas.

   >>> nome = 'João'
   >>> cor_favorita = 'azul'
   >>> print(f'{nome}:\t{cor_favorita}')
   João: azul
   >>> print(rf"C:\Users\{nome}")
   C:\Users\João
   >>> print(f'''Três deve ser o número que deves contar
   ... e o número da contagem deve ser três.''')
   Três deve ser o número que deves contar
   ... e o número da contagem deve ser três.

Expressões em literais de strings formatadas são tratadas como
expressões Python regulares. Cada expressão é avaliada no contexto em
que a literal de string formatada aparece, da esquerda para a direita.
Uma expressão vazia não é permitida, e tanto "lambda" como expressões
":=" de atribuição devem ser cercadas por parênteses explícitos:

   >>> f'{(metade := 1/2)}, {metade * 42}'
   '0.5, 21.0'

É permitido reutilizar o tipo de aspas externas da f-string dentro de
um campo de substituição:

   >>> a = dict(x=2)
   >>> f"abc {a["x"]} def"
   'abc 2 def'

Contrabarras também são permitidas em campos de substituição e são
avaliadas da mesma forma que em qualquer outro contexto:

   >>> a = ["a", "b", "c"]
   >>> print(f"A lista a contém:\n{"\n".join(a)}")
   A lista a contém:
   a
   b
   c

É possível aninhar f-strings:

   >>> nome = 'mundo'
   >>> f'Repetido:{f' olá {nome}' * 3}'
   'Repetido: olá mundo olá mundo olá mundo'

Programas Python portáteis não devem utilizar mais de 5 níveis de
aninhamento.

CPython não possui limite para aninhamento de f-strings.

Expressões de substituição podem conter novas linhas tanto em
f-strings com aspas simples quanto nas de aspas triplas, e podem
conter comentários. Tudo o que vier após um "#" dentro de um campo de
substituição é um comentário (até mesmo chaves de fechamento e aspas).
Isso significa que campos de substituição com comentários devem ser
fechados em uma linha diferente:

   >>> a = 2
   >>> f"abc{a # Este comentário }" continua até o fim da linha
   ...      + 3}"
   'abc5'

Depois da expressão, campos de substituição podem opcionalmente
conter:

* um *especificador de depuração* -- um sinal de igual ("="),
  opcionalmente cercado por espaços em branco em um ou ambos os lados;

* um *especificador de conversão* -- "!s", "!r" ou "!a"; e/ou

* um *especificador de formatação* prefixado com um caractere de dois
  pontos (":").

Consulte o Módulo de f-strings na biblioteca padrão para detalhes
sobre como esses campos são avaliados.

Como o módulo explica, *especificadores de formato* são passados como
o segundo argumento para a função "format()" formatar um valor do
campo de substituição. Por exemplo, podem ser usados para especificar
a largura de campo e caracteres de preenchimento usando a
Minilinguagem de especificação de formato:

   >>> numero = 14.3
   >>> f'{numero:20.7f}'
   '          14.3000000'

Especificadores de formato de nível superior podem incluir campos de
substituição aninhados:

   >>> tamanho_campo = 20
   >>> precisao = 7
   >>> f'{numero:{tamanho_campo}.{precisao}f}'
   '          14.3000000'

Esses campos aninhados podem incluir seus próprios especificadores de
conversão campo e especificador de formato

   >>> numero = 3
   >>> f'{numero:{tamanho_campo}}'
   '                   3'
   >>> f'{numero:{tamanho_campo:05}}'
   '00000000000000000003'

No entanto, esses campos aninhados não podem incluir campos de
substituição mais profundamente aninhados.

Literais de strings formatadas não podem ser usadas como *docstrings*
, mesmo que não incluam expressões:

   >>> def foo():
   ... f "Não é um docstring"
   ...
   >>> print(foo.__doc__)
   None

Ver também:

  * **PEP 498** -- Interpolação de strings literais

  * **PEP 701** -- Formalização sintática de f-strings

  * "str.format()", que usa um mecanismo de string de formato
    relacionado.


2.5.8. Literais de string template (t-strings)
----------------------------------------------

Adicionado na versão 3.14.

Um *literal de string template* ou *t-string* é um literal de string
que é prefixado com '"t"' ou '"T"'. Essas strings seguem as mesmas
regras de sintaxe que literais de strings formatadas . Para conhecer
as diferenças nas regras de avaliação, consulte o módulo biblioteca
padrão em t-strings


2.5.9. Gramática formal para f-strings
--------------------------------------

F-strings são tratados parcialmente pelo *analisador léxico*, que
produz os tokens "FSTRING_START" , "FSTRING_MIDDLE" e "FSTRING_END", e
parcialmente pelo analisador sintático, que manipula expressões nos
campos de substituição. A maneira exata de como trabalho é dividido é
um detalhe de implementação do CPython.

Da mesma forma, a gramática f-string é uma mistura de definições
léxicas e sintáticas.

Espaços em branco são significativos nessas situações:

* Não pode haver espaços em branco em "FSTRING_START" (entre o prefixo
  e a aspas).

* Espaços em branco em "FSTRING_MIDDLE" fazem parte do conteúdo
  literal da string.

* No "fstring_replacement_field", se "f_debug_specifier" estiver
  presente, todo espaço em branco após a chave de abertura até o
  "f_debug_specifier", bem como o espaço em branco imediatamente após
  o "f_debug_specifier", é preservado como parte da expressão.

  A expressão não é tratada na fase de tokenização; ela é recuperada
  do código-fonte usando as localizações do token "{" token e do token
  após o "=".

A definição de "FSTRING_MIDDLE" usa lookaheads negativos ("!") para
indicar caracteres especiais (contrabarra, novas linhas, "{", "}") e
sequências ("f_quote").

   fstring:    FSTRING_START fstring_middle* FSTRING_END

   FSTRING_START:      fstringprefix ("'" | '"' | "'''" | '"""')
   FSTRING_END:        f_quote
   fstringprefix:      <("f" | "fr" | "rf"), case-insensitive>
   f_debug_specifier:  '='
   f_quote:            <the quote character(s) used in FSTRING_START>

   fstring_middle:
      | fstring_replacement_field
      | FSTRING_MIDDLE
   FSTRING_MIDDLE:
      | (!"\" !newline !'{' !'}' !f_quote) source_character
      | stringescapeseq
      | "{{"
      | "}}"
      | <newline, in triple-quoted f-strings only>
   fstring_replacement_field:
      | '{' f_expression [f_debug_specifier] [fstring_conversion]
            [fstring_full_format_spec] '}'
   fstring_conversion:
      | "!" ("s" | "r" | "a")
   fstring_full_format_spec:
      | ':' fstring_format_spec*
   fstring_format_spec:
      | FSTRING_MIDDLE
      | fstring_replacement_field
   f_expression:
      | ','.(conditional_expression | "*" or_expr)+ [","]
      | yield_expression

Nota:

  No trecho de gramática acima, as regras "f_quote" e "FSTRING_MIDDLE"
  são sensíveis ao contexto -- elas dependem do conteúdo de
  "FSTRING_START" da "fstring" que envolve mais próxima.A construção
  de uma gramática formal mais tradicional a partir deste modelo fica
  como exercício para o leitor.

A gramática para t-strings é idêntica à gramática para f-strings, com
*t* em vez de *f* no início dos nomes de regras e tokens e no prefixo.

   tstring:    TSTRING_START tstring_middle* TSTRING_END

   <rest of the t-string grammar is omitted; see above>


2.6. Literais numéricos
=======================

Tokens "NUMBER" representam literais numéricos, dos quais existem três
tipos: inteiros, números de ponto flutuante e números imaginários.

   NUMBER: integer | floatnumber | imagnumber

O valor numérico de um literal numérico é o mesmo que seria se fosse
passado como uma string para os construtores de classe "int", "float"
ou "complex", respectivamente. Observe que nem todas as entradas
válidas para esses construtores também são literais válidos.

Literais numéricos não incluem um sinal; uma frase como "-1" é, na
verdade, uma expressão composta pelo operador unário '"-"' e o literal
"1".


2.6.1. Inteiros literais
------------------------

Literais inteiros denotam números inteiros. Por exemplo:

   7
   3
   2147483647

Não há limite para o comprimento de literais inteiros, exceto o que
pode ser armazenado na memória disponível:

   7922816251426433759354395033679228162514264337593543950336

Sublinhados podem ser usados para agrupar dígitos para melhor
legibilidade e são ignorados para determinar o valor numérico do
literal. Por exemplo, os seguintes literais são equivalentes:

   100_000_000_000
   100000000000
   1_00_00_00_00_000

Sublinhados só podem ocorrer entre dígitos. Por exemplo, "_123",
"321_" e "123__321" *não* são literais válidos.

Os números inteiros podem ser especificados em binário (base 2), octal
(base 8) ou hexadecimal (base 16) usando os prefixos "0b", "0o" e
"0x", respectivamente. Os dígitos hexadecimais de 10 a 15 são
representados pelas letras "A"-"F", sem distinção entre maiúsculas e
minúsculas. Por exemplo:

   0b100110111
   0b_1110_0101
   0o177
   0o377
   0xdeadbeef
   0xDead_Beef

Um sublinhado pode seguir o especificador base. Por exemplo, "0x_1f" é
um literal válido, mas "0_x1f" e "0x__1f" não são.

Zeros à esquerda em um número decimal diferente de zero não são
permitidos. Por exemplo, "0123" não é um literal válido. Isso serve
para desambiguação com literais octais no estilo C, que o Python usava
antes da versão 3.0.

Formalmente, literais inteiros são descritos pelas seguintes
definições lexicais:

   integer:      decinteger | bininteger | octinteger | hexinteger | zerointeger
   decinteger:   nonzerodigit (["_"] digit)*
   bininteger:   "0" ("b" | "B") (["_"] bindigit)+
   octinteger:   "0" ("o" | "O") (["_"] octdigit)+
   hexinteger:   "0" ("x" | "X") (["_"] hexdigit)+
   zerointeger:  "0"+ (["_"] "0")*
   nonzerodigit: "1"..."9"
   digit:        "0"..."9"
   bindigit:     "0" | "1"
   octdigit:     "0"..."7"
   hexdigit:     digit | "a"..."f" | "A"..."F"

Alterado na versão 3.6: Os sublinhados agora são permitidos para fins
de agrupamento de literais.


2.6.2. Literais de ponto flutuante
----------------------------------

Literais de ponto flutuante (float), como "3.14" ou "1.5", denotam
aproximações de números reais.

Eles consistem em partes *inteiras* e *fracionárias*, cada uma
composta por dígitos decimais. As partes são separadas por um ponto
decimal, ".":

   2.71828
   4.0

Ao contrário dos literais inteiros, zeros à esquerda são permitidos
nas partes numéricas. Por exemplo, "077.010" é válido e denota o mesmo
número que "77.01".

Assim como em literais inteiros, sublinhados simples podem ocorrer
entre dígitos para ajudar na legibilidade:

   96_485.332_123
   3.14_15_93

Qualquer uma dessas partes, mas não ambas, pode estar vazia. Por
exemplo:

   10.  # (equivalente a 10.0)
   .001  # (equivalente a 0.001)

Opcionalmente, o inteiro e a fração podem ser seguidos por um
*expoente*: a letra "e" ou "E", seguida por um sinal opcional, "+" ou
"-", e um número no mesmo formato das partes inteira e fracionária. O
"e" ou "E" representa "dez vezes elevado à potência de":

   1.0e3  # (representa 1.0×10³ ou 1000.0)
   1.166e-5  # (representa 1.166×10⁻⁵ ou 0.00001166)
   6.02214076e+23  # (representa 6.02214076×10²³ ou 602214076000000000000000.)

Em floats com apenas partes inteiras e expoentes, o ponto decimal pode
ser omitido:

   1e3  # (equivalente a 1.e3 e 1.0e3)
   0e0  # (equivalente a 0.)

Formalmente, literais de ponto flutuante são descritos pelas seguintes
definições léxicas:

   floatnumber:
      | digitpart "." [digitpart] [exponent]
      | "." digitpart [exponent]
      | digitpart exponent
   digitpart: digit (["_"] digit)*
   exponent:  ("e" | "E") ["+" | "-"] digitpart

Alterado na versão 3.6: Os sublinhados agora são permitidos para fins
de agrupamento de literais.


2.6.3. Literais imaginários
---------------------------

Python possui objetos número complexo, mas não possui literais
complexos. Em vez disso, *literais imaginários* denotam números
complexos com parte real zero.

Por exemplo, na matemática, o número complexo 3+4.2*i* é escrito como
o número real 3 somado ao número imaginário 4.2*i*. Python usa uma
sintaxe semelhante, exceto que a unidade imaginária é escrita como "j"
em vez de *i*:

   3+4.2j

Esta é uma expressão composta pelo literal inteiro "3", o operador
'"+"' e o literal imaginário "4.2j". Como esses são três tokens
separados, espaços em branco são permitidos entre eles:

   3 + 4.2j

Nenhum espaço em branco é permitido *dentro* de cada token. Em
particular, o sufixo "j" não pode ser separado do número que o
precede.

O número antes do "j" tem a mesma sintaxe de um literal de ponto
flutuante. Portanto, os seguintes são literais imaginários válidos:

   4.2j
   3.14j
   10.j
   .001j
   1e100j
   3.14e-10j
   3.14_15_93j

Ao contrário de um literal de ponto flutuante, o ponto decimal pode
ser omitido se o número imaginário tiver apenas uma parte inteira. O
número ainda é avaliado como um número de ponto flutuante, não um
inteiro.

   10j
   0j
   1000000000000000000000000j   # equivalente a 1e+24j

O sufixo "j" não diferencia maiúsculas de minúsculas. Isso significa
que você pode usar "J" em vez disso:

   3.14J   # equivalente a 3.14j

Formalmente, literais imaginários são descritos pela seguinte
definição léxica:

   imagnumber: (floatnumber | digitpart) ("j" | "J")


2.7. Operadores e delimitadores
===============================

A seguinte gramática define os tokens de *operador* e de
*delimitador*, ou seja, o tipo de token genérico "OP". Uma lista
destes tokens e seus nomes também está disponível na documentação do
módulo "token".

   OP:
      | assignment_operator
      | bitwise_operator
      | comparison_operator
      | enclosing_delimiter
      | other_delimiter
      | arithmetic_operator
      | "..."
      | other_op

   assignment_operator:   "+=" | "-=" | "*=" | "**=" | "/="  | "//=" | "%=" |
                          "&=" | "|=" | "^=" | "<<=" | ">>=" | "@="  | ":="
   bitwise_operator:      "&"  | "|"  | "^"  | "~"   | "<<"  | ">>"
   comparison_operator:   "<=" | ">=" | "<"  | ">"   | "=="  | "!="
   enclosing_delimiter:   "("  | ")"  | "["  | "]"   | "{"   | "}"
   other_delimiter:       ","  | ":"  | "!"  | ";"   | "="   | "->"
   arithmetic_operator:   "+"  | "-"  | "**" | "*"   | "//"  | "/"   | "%"
   other_op:              "."  | "@"

Nota:

  Geralmente, *operadores* são usados para combinar expressões,
  enquanto que os *delimitadores* servem para outras coisas.
  Entretanto, não há distinção formal clara entre essas duas
  categorias.Alguns tokens podem servir tanto como operadores quanto
  delimitadores, dependendo da forma de uso. Por exemplo, "*" é tanto
  o operador de multiplicação quanto o delimitador usado para
  desempacotamento de sequências, e "@" é ao mesmo tempo a
  multiplicação de matrizes e o delimitador que introduz
  decoradores.Para alguns tokens, a distinção não é clara. Por
  exemplo, alguns consideram ".", "(" e ")" como sendo delimitadores,
  enquanto outros enxergam aí o operador "getattr()" e o(s)
  operador(es) de chamada de função.Alguns operadores do Python, como
  "and", "or" e "not in", usam tokens de palavra reservada ao invés de
  "símbolos" (tokens de operador).

Uma sequência de três pontos consecutivos ("...") tem o significado
especial de ser um literal de "Ellipsis".
