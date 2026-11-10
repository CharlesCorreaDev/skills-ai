7. Entrada e saída
******************

Existem várias maneiras de apresentar a saída de um programa; os dados
podem ser exibidos em forma legível para seres humanos, ou escritos em
arquivos para uso posterior. Este capítulo apresentará algumas das
possibilidades.


7.1. Formatação de saída mais elaborada
=======================================

Até agora vimos duas maneiras de exibir valores: *expressões* e a
função "print()". (Uma outra maneira é utilizar o método "write()" de
objetos do tipo arquivo; o arquivo saída padrão pode ser referenciado
como "sys.stdout". Veja a Referência da Biblioteca Python para mais
informações sobre isso.)

Muitas vezes se deseja mais controle sobre a formatação da saída do
que simplesmente exibir valores separados por espaço. Existem várias
maneiras de formatar a saída.

* Para usar strings literais formatadas, comece uma string com "f" ou
  "F", antes de abrir as aspas ou aspas triplas. Dentro dessa string,
  pode-se escrever uma expressão Python entre caracteres "{" e "}",
  que podem se referir a variáveis, ou valores literais.

     >>> ano = 2016
     >>> evento = 'Referendo'
     >>> f'Resultados do {evento} {ano}'
     'Resultados do Referendo 2016'

* O método de strings "str.format()" requer mais esforço manual. Ainda
  será necessário usar "{" e "}" para marcar onde a variável será
  substituída e pode-se incluir diretivas de formatação detalhadas,
  mas também precisará incluir a informação a ser formatada. No bloco
  de código a seguir há dois exemplos de como formatar variáveis:

     >>> votos_sim = 42_572_654
     >>> votos_totais = 85_705_149
     >>> porcentagem = votos_sim / votos_totais
     >>> '{:-9} votos SIM  {:2.2%}'.format(votos_sim, porcentagem)
     ' 42572654 votos SIM  49.67%'

  Observe como "yes_votes" são preenchidos com espaços e um sinal
  negativo apenas para números negativos. O exemplo também imprime
  "percentage" multiplicado por 100, com 2 casas decimais e seguido
  por um sinal de porcentagem (veja Minilinguagem de especificação de
  formato para detalhes).

* Finalmente, pode-se fazer todo o tratamento da saída usando as
  operações de fatiamento e concatenação de strings para criar
  qualquer layout que se possa imaginar. O tipo string possui alguns
  métodos que realizam operações úteis para preenchimento de strings
  para uma determinada largura de coluna.

Quando não é necessário sofisticar a saída, mas apenas exibir algumas
variáveis com propósito de depuração, pode-se converter qualquer valor
para uma string com as funções "repr()" ou "str()".

A função "str()" serve para retornar representações de valores que
sejam legíveis para as pessoas, enquanto "repr()" é para gerar
representações que o interpretador Python consegue ler (ou levantará
uma exceção "SyntaxError", se não houver sintaxe equivalente). Para
objetos que não têm uma representação adequada para consumo humano,
"str()" devolve o mesmo valor que "repr()". Muitos valores, tal como
números ou estruturas, como listas e dicionários, têm a mesma
representação usando quaisquer das funções. Strings, em particular,
têm duas representações distintas.

Alguns exemplos:

   >>> s = 'Olá, mundo.'
   >>> str(s)
   'Olá, mundo.'
   >>> repr(s)
   "'Olá, mundo.'"
   >>> str(1/7)
   '0.14285714285714285'
   >>> x = 10 * 3.25
   >>> y = 200 * 200
   >>> s = 'O valor de x é ' + repr(x) + ' e de y é ' + repr(y) + '...'
   >>> print(s)
   O valor de x é 32.5 e de y é 40000...
   >>> # A repr() da string adiciona aspas e contrabarras:
   >>> olá = 'olá, mundo\n'
   >>> olás = repr(olá)
   >>> print(olás)
   'olá, mundo\n'
   >>> # O argumento de repr() pode ser qualquer objeto Python:
   >>> repr((x, y, ('spam', 'ovos')))
   "(32.5, 40000, ('spam', 'ovos'))"

O módulo "string" contém suporte para uma abordagem simples de criação
de modelos baseada em expressões regulares, via "string.Template".
Isso oferece outra maneira de substituir valores em strings, usando
espaços reservados como "$x" e substituindo-os por valores de um
dicionário. Essa sintaxe é fácil de usar, embora ofereça muito menos
controle sobre a formatação.


7.1.1. Literais de string formatados
------------------------------------

Strings literais formatadas (também chamadas f-strings, para abreviar)
permite que se inclua o valor de expressões Python dentro de uma
string, prefixando-a com "f" ou "F" e escrevendo expressões na forma
"{expression}".

Um especificador opcional de formato pode ser incluído após a
expressão. Isso permite maior controle sobre como o valor é formatado.
O exemplo a seguir arredonda pi para três casas decimais:

   >>> import math
   >>> print(f'O valor de pi é aproximadamente {math.pi:.3f}.')
   O valor de pi é aproximadamente 3.142.

Passando um inteiro após o "':'" fará com que o campo tenha um número
mínimo de caracteres de largura. Isso é útil para alinhar colunas.

   >>> tabela = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
   >>> for nome, telefone in tabela.items():
   ...     print(f'{nome:10} ==> {telefone:10d}')
   ...
   Sjoerd     ==>       4127
   Jack       ==>       4098
   Dcab       ==>       7678

Outros modificadores podem ser usados para converter o valor antes de
ser formatado. "'!a'" aplica a função "ascii()", "'!s'" aplica a
função "str()" e "'!r'" aplica a função "repr()"

   >>> animais = 'enguias'
   >>> print(f'Meu hovercraft está cheio de {animais}.')
   Meu hovercraft está cheio de enguias.
   >>> print(f'Meu hovercraft está cheio de {animais!r}.')
   Meu hovercraft está cheio de 'enguias'.

O especificador "=" pode ser usado para expandir uma expressão para o
texto da expressão, um sinal de igual e, então, a representação da
expressão avaliada:

>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'

Veja expressões autodocumentadas para mais informações sobre o
especificador "=". Para obter uma referência sobre essas
especificações de formato, consulte o guia de referência para a
Minilinguagem de especificação de formato.


7.1.2. O método format() de strings
-----------------------------------

Um uso básico do método "str.format()" tem esta forma:

   >>> print('Nós somos os {} que dizem "{}!"'.format('cavaleiros', 'Ni'))
   Nós somos os cavaleiros que dizem "Ni!"

As chaves e seus conteúdos (chamados campos de formatação) são
substituídos pelos objetos passados para o método "str.format()". Um
número nas chaves pode ser usado para referenciar a posição do objeto
passado no método "str.format()".

   >>> print('{0} e {1}'.format('spam', 'ovos'))
   spam e eggs
   >>> print('{1} e {0}'.format('spam', 'ovos'))
   eggs e spam

Se argumentos nomeados são passados para o método "str.format()", seus
valores serão referenciados usando o nome do argumento:

   >>> print('Este {comida} está {adjetivo}.'.format(
   ...       comida='spam', adjetivo='absolutamente horrível'))
   Este spam está absolutamente horrível.

Argumentos posicionais e nomeados podem ser combinados à vontade:

   >>> print('A história de {0}, {1} e {outro}.'.format('Bill', 'Manfred',
   ...                                                    outro='Georg'))
   A história de Bill, Manfred e Georg.

Se uma string de formatação é muito longa, e não se deseja quebrá-la,
pode ser bom fazer referência aos valores a serem formatados por nome,
em vez de posição. Isto pode ser feito passando um dicionário usando
colchetes "'[]'" para acessar as chaves.

   >>> tabela = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
   ...       'Dcab: {0[Dcab]:d}'.format(tabela))
   Jack: 4098; Sjoerd: 4127; Dcab: 8637678

Isto também pode ser feito passando o dicionário "table" como
argumentos nomeados com a notação "**".

   >>> tabela = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**tabela))
   Jack: 4098; Sjoerd: 4127; Dcab: 8637678

Isto é particularmente útil em conjunto com a função embutida
"vars()", que devolve um dicionário contendo todas as variáveis
locais:

   >>> tabela = {k: str(v) for k, v in vars().items()}
   >>> mensagem = " ".join([f'{k}: ' + '{' + k +'};' for k in tabela.keys()])
   >>> print(mensagem.format(**tabela))
   __name__: __main__; __doc__: None; __package__: None; __loader__: ...

Como exemplo, as linhas seguintes produzem um conjunto de colunas
alinhadas, com alguns inteiros e seus quadrados e cubos:

   >>> for x in range(1, 11):
   ...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
   ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
   10 100 1000

Para uma visão completa da formatação de strings com "str.format()",
veja a seção Sintaxe das strings de formato.


7.1.3. Formatação manual de strings
-----------------------------------

Aqui está a mesma tabela de quadrados e cubos, formatados manualmente:

   >>> for x in range(1, 11):
   ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
   ...     # Observe o uso do 'end' na linha anterior
   ...     print(repr(x*x*x).rjust(4))
   ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
   10 100 1000

(Note que o espaço entre cada coluna foi adicionado pela forma que a
função "print()" funciona: sempre adiciona espaços entre seus
argumentos.)

O método "str.rjust()" justifica uma string à direita, num campo de
tamanho definido, acrescentando espaços à esquerda. De forma similar,
os métodos "str.ljust()", justifica à esquerda, e "str.center()", para
centralizar. Esses métodos não escrevem nada, apenas retornam uma nova
string. Se a string de entrada é muito longa, os métodos não truncarão
a saída, e retornarão a mesma string, sem mudança; isso vai atrapalhar
o layout da coluna, mas geralmente é melhor do que a alternativa, que
estaria distorcendo o valor. (Se realmente quiser truncar, sempre se
pode adicionar uma operação de fatiamento, como em "x.ljust(n)[:n]".)

Existe ainda o método "str.zfill()" que preenche uma string numérica
com zeros à esquerda, e sabe lidar com sinais positivos e negativos:

   >>> '12'.zfill(5)
   '00012'
   >>> '-3.14'.zfill(7)
   '-003.14'
   >>> '3.14159265359'.zfill(5)
   '3.14159265359'


7.1.4. Formatação de strings à moda antiga
------------------------------------------

O operador % (módulo) também pode ser usado para formatação de string.
Dado "formato % valores" (onde *formato* é uma string), as instâncias
de "%" em "formato" serão substituídas por zero ou mais elementos de
"valores". Essa operação é conhecida como interpolação de string. Por
exemplo:

   >>> import math
   >>> print('O valor de pi é aproximadamente %5.3f.' % math.pi)
   O valor de pi é aproximadamente 3.142.

Mais informação pode ser encontrada na seção Formatação de string no
estilo printf.


7.2. Lendo e escrevendo arquivos
================================

"open()" retorna um *objeto arquivo*, e é mais utilizado com dois
argumentos posicionais: "open(filename, mode)"

   >>> f = open('arquivo_de_trabalho', 'w')

O primeiro argumento é uma string contendo o nome do arquivo. O
segundo argumento é outra string, contendo alguns caracteres que
descrevem o modo como o arquivo será usado. *modo* pode ser "'r'"
quando o arquivo será apenas lido, "'w'" para escrever (se o arquivo
já existir seu conteúdo prévio será apagado), e "'a'" para abrir o
arquivo para adição; qualquer escrita será adicionada ao final do
arquivo. A opção "'r+'" abre o arquivo tanto para leitura como para
escrita. O argumento *modo* é opcional, em caso de omissão será
presumido "'r'".

Normalmente, arquivos são abertos no *modo texto*, o que significa que
você lê strings de e para o arquivo, o qual está em um codificação
específica. Se a *codificação* não for especificada, o padrão é UTF-8
(veja "open()"). Adicionando "'b'" ao modo irá abrir o o arquivo em
*modo binário*. Dados no modo binário são lidos e escritos como
objetos "bytes".  Você não pode especificar a *codificação* quando
estiver abrindo os arquivos em modo binário.

Em modo texto, o padrão durante a leitura é converter terminadores de
linha específicos da plataforma ("\n" no Unix, "\r\n" no Windows) para
apenas "\n". Ao escrever no modo de texto, o padrão é converter as
ocorrências de "\n" de volta para os finais de linha específicos da
plataforma. Essa modificação de bastidores nos dados do arquivo é
adequada para arquivos de texto, mas corromperá dados binários, como
arquivos "JPEG" ou "EXE". Tenha muito cuidado para só usar o modo
binário, ao ler e gravar esses arquivos.

É uma boa prática usar a palavra-chave "with" ao lidar com arquivos. A
vantagem é que o arquivo é fechado corretamente após o término de sua
utilização, mesmo que uma exceção seja levantada em algum momento.
Usar "with" também é muito mais curto que escrever seu bloco
equivalente "try"-"finally":

   >>> with open('arquivo_de_trabalho') as f:
   ...     read_data = f.read()

   >>> # Podemos verificar se o arquivo foi fechado automaticamente.
   >>> f.closed
   True

Se você não está usando a palavra reservada "with", então você deveria
chamar "f.close()" para fechar o arquivo e imediatamente liberar
qualquer recurso do sistema usado por ele.

Aviso:

  Chamar "f.write()" sem usar a palavra reservada "with" ou chamar
  "f.close()" **pode** resultar nos argumentos de "f.write()" não
  serem completamente escritos no disco, mesmo se o programa for
  encerrado com êxito.

Depois que um arquivo é fechado, seja por uma instrução "with" ou
chamando "f.close()", as tentativas de usar o arquivo falharão
automaticamente.

   >>> f.close()
   >>> f.read()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: I/O operation on closed file.


7.2.1. Métodos de objetos arquivo
---------------------------------

Para simplificar, o resto dos exemplos nesta seção presumem que um
objeto arquivo chamado "f" já foi criado.

Para ler o conteúdo de um arquivo, chame "f.read(tamanho)", que lê um
punhado de dados devolvendo-os como uma string (em modo texto) ou
bytes (em modo binário). *tamanho* é um argumento numérico opcional.
Quando *tamanho* é omitido ou negativo, todo o conteúdo do arquivo é
lido e devolvido; se o arquivo é duas vezes maior que memória da
máquina, o problema é seu. Caso contrário, no máximo *tamanho*
caracteres (em modo texto) ou *tamanho* bytes (em modo binário) são
lidos e devolvidos. Se o fim do arquivo for atingido, "f.read()"
devolve uma string vazia ("''").

   >>> f.read()
   'Este é o arquivo inteiro.\n'
   >>> f.read()
   ''

O método "f.readline()" lê uma única linha do arquivo; o caractere de
quebra de linha ("\n") é mantido ao final da string, e só é omitido na
última linha do arquivo, se o arquivo não terminar com uma quebra de
linha. Isso elimina a ambiguidade do valor retornado; se
"f.readline()" retorna uma string vazia, o fim do arquivo foi
atingido. Linhas em branco são representadas por um "'\n'" -- uma
string contendo apenas o caractere terminador de linha.

   >>> f.readline()
   'Está é a primeira linha do arquivo.\n'
   >>> f.readline()
   'Segunda linha do arquivo\n'
   >>> f.readline()
   ''

Uma maneira alternativa de ler linhas do arquivo é iterar diretamente
pelo objeto arquivo. É eficiente, rápido e resulta em código mais
simples:

   >>> for line in f:
   ...     print(line, end='')
   ...
   Esta é a primeira linha do arquivo.
   Segunda linha do arquivo

Se desejar ler todas as linhas de um arquivo em uma lista, pode-se
usar "list(f)" ou "f.readlines()".

"f.write(string)" escreve o conteúdo de *string* para o arquivo,
retornando o número de caracteres escritos.

   >>> f.write('Este é um teste\n')
   15

Outros tipos de objetos precisam ser convertidos -- seja para uma
string (em modo texto) ou para bytes (em modo binário) -- antes de
escrevê-los:

   >>> value = ('a resposta', 42)
   >>> s = str(value)  # converte a tupla para string
   >>> f.write(s)
   18

"f.tell()" retorna um inteiro dando a posição atual do objeto arquivo,
no arquivo representado, como número de bytes desde o início do
arquivo, no modo binário, e um número ininteligível, quando no modo de
texto.

Para mudar a posição, use "f.seek(offset, de_onde)". A nova posição é
computada pela soma do deslocamento *offset* a um ponto de referência
especificado pelo argumento *de-onde*. Se o valor de *de_onde* é 0,a
referência é o início do arquivo, 1 refere-se à posição atual, e 2
refere-se ao fim do arquivo. Este argumento pode ser omitido e o valor
padrão é 0, usando o início do arquivo como referência.

   >>> f = open('arquivo_de_trabalho', 'rb+')
   >>> f.write(b'0123456789abcdef')
   16
   >>> f.seek(5)      # Vai até o 6º byte no arquivo
   5
   >>> f.read(1)
   b'5'
   >>> f.seek(-3, 2)  # Vai até o 3º byte antes do fim
   13
   >>> f.read(1)
   b'd'

Em arquivos texto (abertos sem um "b", em modo string), somente
*seeks* relativos ao início do arquivo serão permitidos (exceto se for
indicado o final do arquivo, com "seek(0, 2)") e o único valor válido
para *offset* são aqueles retornados por chamada à "f.tell()", ou
zero. Qualquer outro valor para *offset* produz um comportamento
indefinido.

Objetos arquivo tem alguns métodos adicionais, como "isatty()" e
"truncate()" que não são usados com frequência; consulte a Biblioteca
de Referência para um guia completo de objetos arquivo.


7.2.2. Gravando dados estruturados com "json"
---------------------------------------------

Strings podem ser facilmente gravadas e lidas em um arquivo. Números
dão um pouco mais de trabalho, já que o método "read()" só retorna
strings, que terão que ser passadas para uma função como "int()", que
pega uma string como "'123'" e retorna seu valor numérico 123. Quando
você deseja salvar tipos de dados mais complexos, como listas e
dicionários aninhados, a análise e serialização manual tornam-se
complicadas.

Ao invés de ter usuários constantemente escrevendo e depurando código
para gravar tipos complicados de dados em arquivos, o Python permite
que se use o popular formato de troca de dados chamado JSON
(JavaScript Object Notation). O módulo padrão chamado "json" pode
pegar hierarquias de dados em Python e convertê-las em representações
de strings; esse processo é chamado *serialização*. Reconstruir os
dados estruturados da representação string é chamado
*desserialização*. Entre serializar e desserializar, a string que
representa o objeto pode ser armazenada em um arquivo, ou estrutura de
dados, ou enviada por uma conexão de rede para alguma outra máquina.

Nota:

  O formato JSON é comumente usado por aplicativos modernos para
  permitir troca de dados. Pessoas que programam já estão
  familiarizadas com esse formato, o que o torna uma boa opção para
  interoperabilidade.

Um objeto "x", pode ser visualizado na sua representação JSON com uma
simples linha de código:

   >>> import json
   >>> x = [1, 'lista', 'simples']
   >>> json.dumps(x)
   '[1, "lista", "simples"]'

Outra variação da função "dumps()", chamada "dump()", serializa o
objeto para um *arquivo texto*. Se "f" é um *arquivo texto* aberto
para escrita, podemos fazer isto:

   json.dump(x, f)

Para decodificar o objeto novamente, se "f" é um objeto *arquivo
binário* ou *arquivo texto* que foi aberto para leitura:

   x = json.load(f)

Nota:

  Arquivos JSON devem ser codificados em UTF-8, a codificação padrão
  para *arquivos texto*.

Essa técnica de serialização simples pode manipular listas e
dicionários, mas a serialização de instâncias de classes arbitrárias
no JSON requer um pouco mais de esforço. A referência para o módulo
"json" contém uma explicação disso.

Ver também:

  O módulo "pickle"

  Ao contrário do JSON, *pickle* é um protocolo que permite a
  serialização de objetos Python arbitrariamente complexos. Por isso,
  é específico do Python e não pode ser usado para se comunicar com
  aplicativos escritos em outros linguagens. Também é inseguro por
  padrão: desserializar dados de pickle, provenientes de uma fonte não
  confiável, pode executar código arbitrário, se os dados foram
  criados por um invasor habilidoso.
