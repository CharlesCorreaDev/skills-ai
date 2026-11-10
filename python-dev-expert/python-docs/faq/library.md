FAQ de Bibliotecas e Extensões
******************************


Questões gerais sobre bibliotecas
=================================


Como encontrar um módulo ou aplicação para realizar uma tarefa X?
-----------------------------------------------------------------

Verifique a Referência de Bibliotecas para ver se há um módulo
relevante da biblioteca padrão. (Eventualmente, você aprenderá o que
está na biblioteca padrão e poderá pular esta etapa.)

Para pacotes de terceiros, pesquise no Python Package Index ou tente
no Google ou outro buscador na web. Pesquisando por "Python" mais uma
ou dois argumentos nomeados do seu tópico de interesse geralmente
encontrará algo útil.


Onde está o código-fonte do math.py (socket.py, regex.py, etc.)?
----------------------------------------------------------------

Se você não conseguir encontrar um arquivo de origem para um módulo,
ele pode ser um módulo embutido ou carregado dinamicamente,
implementado em C, C++ ou outra linguagem compilada. Nesse caso, você
pode não ter o arquivo de origem ou pode ser algo como "mathmodule.c",
em algum lugar do diretório de origem C (não no caminho do Python).

Existem (pelo menos) três tipos de módulos no Python:

1. módulos escritos em Python (.py)

2. módulos escritos em C e carregados dinamicamente (.dll, .pyd, .so,
   .sl, etc.);

3. módulos escritos em C e vinculados ao interpretador; para obter uma
   dessas listas, digite:

      import sys
      print(sys.builtin_module_names)


Como tornar um script Python executável no Unix?
------------------------------------------------

Você precisa fazer duas coisas: o arquivo do script deve ser
executável e a primeira linha deve começar com "#!" seguido do caminho
do interpretador Python.

Inicialmente, execute o "chmod +x scriptfile" ou, talvez, o "chmod 755
scriptfile".

A segunda coisa pode ser feita de várias maneiras. A maneira mais
direta é escrever

   #!/usr/local/bin/python

como a primeira linha do seu arquivo, usando o endereço do caminho
onde o interpretador Python está instalado.

Se você deseja que o script seja independente de onde o interpretador
Python mora, você pode usar o programa **env**. Quase todas as
variantes do Unix suportam o seguinte, presumindo que o interpretador
Python esteja em um diretório no "PATH" do usuário:

   #!/usr/bin/env python

Não faça isso para CGI scripts. A variável "PATH" para CGI scripts é
normalmente muito pequena, portanto, você precisa usar o caminho
completo do interpretador.

Ocasionalmente, o ambiente de um usuário está tão cheio que o programa
**/usr/bin/env** falha; ou não há nenhum programa env. Nesse caso,
você pode tentar o seguinte hack (graças a Alex Rezinsky):

   #! /bin/sh
   """:"
   exec python $0 ${1+"$@"}
   """

Uma pequena desvantagem é que isso define o script's __doc__ string.
Entretanto, você pode corrigir isso adicionando

   __doc__ = """...Alguma coisa..."""


Existe um pacote de curses/termcap para Python?
-----------------------------------------------

Para variantes Unix: A distribuição fonte padrão do Python vem com um
módulo do curses no subdiretório Modules, embora não seja compilado
por padrão.  (Observe que isso não está disponível na distribuição do
Windows -- não há módulo curses para o Windows.)

O módulo "curses" provê recursos básicos de curses, bem como muitas
funções adicionais de ncurses e curses SYSV, como cor, suporte a
conjuntos de caracteres alternativos, pads e suporte a mouse. Isso
significa que o módulo não é compatível com sistemas operacionais que
possuem apenas maldições BSD, mas não parece haver nenhum sistema
operacional mantido atualmente que se enquadre nesta categoria.


Existe a função onexit() equivalente ao C no Python?
----------------------------------------------------

O módulo "atexit" fornece uma função de registro similar ao "onexit()"
do C.


Por que o meu manipulador de sinal não funciona?
------------------------------------------------

O maior problema é que o manipulador de sinal é declarado com uma
lista de argumentos incorretos. Isso é chamado como

   manipulador(num_sinal, quadro)

portanto, isso deve ser declarado com dois parâmetros:

   def manipulador(num_sinal, quadro):
       ...


Tarefas comuns
==============


Como testar um programa ou componente Python?
---------------------------------------------

A Python vem com dois frameworks de teste. O módulo "doctest" busca
por exemplos nas docstrings de um módulo e os executa, comparando o
resultado com a saída esperada informada na docstring.

O módulo "unittest" é uma estrutura de teste mais sofisticada,
modelada nas estruturas de teste do Java e do Smalltalk.

Para facilitar os testes, você deve usar um bom design modular em seu
programa. Seu programa deve ter quase todas as funcionalidades
encapsuladas em funções ou métodos de classe -- e isso às vezes tem o
efeito surpreendente e agradável de fazer o programa executar mais
rápido (porque os acessos às variáveis locais são mais rápidos que os
acessos globais). Além disso, o programa deve evitar depender de
variáveis globais mutantes, pois isso torna os testes muito mais
difíceis de serem realizados.

A lógica principal do seu programa pode tão simples quanto

   if __name__ == "__main__":
       main_logic()

no botão do módulo principal do seus programa.

Depois que seu programa estiver organizado como uma coleção tratável
de comportamentos de funções e classes, você deverá escrever funções
de teste que exercitem os comportamentos. Um conjunto de testes que
automatiza uma sequência de testes pode ser associado a cada módulo.
Parece muito trabalhoso, mas como o Python é tão conciso e flexível, é
surpreendentemente fácil. Você pode tornar a codificação muito mais
agradável e divertida escrevendo suas funções de teste em paralelo com
o "código de produção", pois isso torna mais fácil encontrar bugs e
até mesmo falhas de design mais cedo.

Os "módulos de suporte" que não se destinam a ser o módulo principal
de um programa podem incluir um autoteste do módulo.

   if __name__ == "__main__":
       self_test()

Mesmo quando as interfaces externas não estiverem disponíveis, os
programas que interagem com interfaces externas complexas podem ser
testados usando as interfaces "falsas" implementadas no Python.


Como faço para criar uma documentação de doc strings?
-----------------------------------------------------

O módulo "pydoc" pode criar HTML a partir das strings de documentos em
seu código-fonte Python. Uma alternativa para criar documentação de
API puramente a partir de docstrings é epydoc. Sphinx também pode
incluir conteúdo docstring.


Como faço para pressionar uma tecla de cada vez?
------------------------------------------------

Para variantes do Unix existem várias soluções. Apesar de ser um
módulo grande para aprender, é simples fazer isso usando o módulo
curses.


Threads
=======


Como faço para programar usando threads?
----------------------------------------

Certifique-se de usar o módulo "threading" e não o módulo "_thread". O
módulo "threading" constrói abstrações convenientes sobre as
primitivas de baixo nível fornecidas pelo módulo "_thread".


Nenhuma de minhas threads parece funcionar, por que?
----------------------------------------------------

Assim que a thread principal acaba, todas as threads são eliminadas.
Sua thread principal está sendo executada tão rápida que não está
dando tempo para realizar qualquer trabalho.

Uma solução simples é adicionar um tempo de espera no final do
programa até que todos os threads sejam concluídos:

   import threading, time

   def thread_task(name, n):
       for i in range(n):
           print(name, i)

   for i in range(10):
       T = threading.Thread(target=thread_task, args=(str(i), i))
       T.start()

   time.sleep(10)  # <---------------------------!

Mas agora (em muitas plataformas) as threads não funcionam em
paralelo, mas parecem funcionar sequencialmente, um de cada vez! O
motivo é que o agendador de threads do sistema operacional não inicia
uma nova thread até que a thread anterior seja bloqueada.

Uma solução simples é adicionar um pequeno tempo de espera no início
da função:

   def thread_task(name, n):
       time.sleep(0.001)  # <--------------------!
       for i in range(n):
           print(name, i)

   for i in range(10):
       T = threading.Thread(target=thread_task, args=(str(i), i))
       T.start()

   time.sleep(10)

Em vez de tentar adivinhar um bom valor de atraso para "time.sleep()",
é melhor usar algum tipo de mecanismo de semáforo. Uma ideia é usar o
módulo "queue" para criar um objeto fila, deixar cada thread anexar um
token à fila quando terminar e deixar a thread principal ler tantos
tokens da fila quantos threads houver.


Como distribuo o trabalho entre várias threads de trabalho?
-----------------------------------------------------------

A maneira mais fácil é usar o módulo "concurrent.futures",
especialmente a classe "ThreadPoolExecutor".

Ou, se quiser um controle preciso sobre o algoritmo de despacho, você
pode escrever sua própria lógica manualmente. Use o módulo "queue"
para criar uma fila contendo uma lista de tarefas. A classe "Queue"
mantém uma lista de objetos e possui um método ".put(obj)" que
adiciona itens à fila e um método ".get()" para retorná-los. A classe
cuidará da trava necessário para garantir que cada trabalho seja
entregue exatamente uma vez.

Aqui está um exemplo simples:

   import threading, queue, time

   # A thread do worker obtém a tarefa da fila. Quando a fila está vazia,
   # ela presume que não haverá mais tarefas e encerra.
   # (Realisticamente, workers trabalharão até serem encerrados.)
   def worker():
       print('Running worker')
       time.sleep(0.1)
       while True:
           try:
               arg = q.get(block=False)
           except queue.Empty:
               print('Worker', threading.current_thread(), end=' ')
               print('queue empty')
               break
           else:
               print('Worker', threading.current_thread(), end=' ')
               print('running with argument', arg)
               time.sleep(0.5)

   # Cria a fila
   q = queue.Queue()

   # Inicia um pool de 5 workers
   for i in range(5):
       t = threading.Thread(target=worker, name='worker %i' % (i+1))
       t.start()

   # Começa a adicionar tarefa à fila
   for i in range(50):
       q.put(i)

   # Dá às threads tempo para executar
   print('Main thread sleeping')
   time.sleep(5)

Quando executado, isso produzirá a seguinte saída:

   Running worker
   Running worker
   Running worker
   Running worker
   Running worker
   Main thread sleeping
   Worker <Thread(worker 1, started 130283832797456)> running with argument 0
   Worker <Thread(worker 2, started 130283824404752)> running with argument 1
   Worker <Thread(worker 3, started 130283816012048)> running with argument 2
   Worker <Thread(worker 4, started 130283807619344)> running with argument 3
   Worker <Thread(worker 5, started 130283799226640)> running with argument 4
   Worker <Thread(worker 1, started 130283832797456)> running with argument 5
   ...

Consulte a documentação do módulo para mais detalhes; a classe "Queue"
fornece uma interface com recursos.


Que tipos de variáveis globais mutáveis são seguras para thread?
----------------------------------------------------------------

Uma *trava global do interpretador* (GIL) é usada internamente para
garantir que apenas um thread seja executado na VM Python por vez. Em
geral, Python oferece alternar entre threads apenas entre instruções
de bytecode; a frequência com que ele muda pode ser definida via
"sys.setswitchinterval()". Cada instrução de bytecode e, portanto,
todo o código de implementação C alcançado por cada instrução é,
portanto, atômico do ponto de vista de um programa Python.

Em teoria, isso significa que uma contabilidade exata requer um
entendimento exato da implementação do bytecode PVM. Na prática, isso
significa que as operações em variáveis compartilhadas de tipos de
dados integrados (inteiros, listas, dicionários, etc.) que "parecem
atômicas" realmente são.

Por exemplo, as seguintes operações são todas atômicas (L, L1, L2 são
listas, D, D1, D2 são dicionários, x, y são objetos, i, j são
inteiros):

   L.append(x)
   L1.extend(L2)
   x = L[i]
   x = L.pop()
   L1[i:j] = L2
   L.sort()
   x = y
   x.field = y
   D[x] = y
   D1.update(D2)
   D.keys()

Esses não são:

   i = i+1
   L.append(L[-1])
   L[i] = L[j]
   D[x] = D[x] + 1

Operações que substituem outros objetos podem invocar o método
"__del__()" desses outros objetos quando sua contagem de referências
chega a zero, e isso pode afetar as coisas. Isto é especialmente
verdadeiro para as atualizações em massa de dicionários e listas. Em
caso de dúvida, use um mutex!


Não podemos remover a Trava Global do interpretador?
----------------------------------------------------

A *trava global do interpretador* (GIL) é frequentemente vista como um
obstáculo para a implantação do Python em máquinas servidoras
multiprocessadas de ponta, porque um programa Python multi-threaded
efetivamente usa apenas uma CPU, devido à insistência de que (quase)
todo código Python só pode ser executado enquanto a GIL é mantida.

Com a aprovação da **PEP 703**, o trabalho está em andamento para
remover a GIL da implementação CPython do Python. Inicialmente, ele
será implementado como um sinalizador opcional de compilador ao
construir o interpretador, e assim construções separadas estarão
disponíveis com e sem a GIL. A longo prazo, a esperança é estabelecer
uma única construção, uma vez que as implicações de desempenho da
remoção do GIL sejam totalmente compreendidas. O Python 3.13
provavelmente será a primeira versão contendo esse trabalho, embora
possa não ser completamente funcional nesta versão.

O trabalho atual para remover a GIL é baseado em um fork do Python 3.9
com a GIL removida por Sam Gross. Antes disso, na época do Python 1.5,
Greg Stein implementou um conjunto abrangente de patches (os patches
de "threads livres") que removeu a GIL e a substituiu por um
travamento de granulação fina. Adam Olsen fez um experimento
semelhante em seu projeto python-safethread. Infelizmente, ambos os
experimentos iniciais exibiram uma queda acentuada no desempenho de
thread único (pelo menos 30% mais lento), devido à quantidade de
travamento de granulação fina necessária para compensar a remoção da
GIL. O fork do Python 3.9 é a primeira tentativa de remover a GIL com
um impacto aceitável no desempenho.

A presença da GIL nas versões atuais do Python não significa que você
não pode fazer bom uso do Python em máquinas com várias CPUs! Você só
precisa ser criativo ao dividir o trabalho entre vários *processos* em
vez de vários *threads*. A classe "ProcessPoolExecutor" no novo módulo
"concurrent.futures" fornece uma maneira fácil de fazer isso; o módulo
"multiprocessing" fornece uma API de nível inferior, caso você queira
mais controle sobre o despacho de tarefas.

O uso criterioso de extensões C também ajudará; se você usar uma
extensão C para executar uma tarefa demorada, a extensão poderá
liberar a GIL enquanto o thread de execução estiver no código C e
permitir que outros threads realizem algum trabalho. Alguns módulos de
biblioteca padrão como "zlib" e "hashlib" já fazem isso.

Uma abordagem alternativa para reduzir o impacto da GIL é fazer da GIL
uma trava por estado do interpretador em vez de verdadeiramente
global. Isso foi implementado pela primeira vez no Python 3.12 e está
disponível na API C. Uma interface Python para ele é esperada no
Python 3.13. A principal limitação para ele no momento provavelmente
são módulos de extensão de terceiros, já que estes devem ser escritos
com múltiplos interpretadores em mente para serem utilizáveis, então
muitos módulos de extensão mais antigos não serão utilizáveis.


Entrada e Saída
===============


Como faço para excluir um arquivo? (E outras perguntas sobre arquivos)
----------------------------------------------------------------------

Use "os.remove(arquivo)" ou "os.unlink(arquivo)"; para documentação,
veja o módulo "os". As duas funções são idênticas; "unlink()" é
simplesmente o nome da chamada do sistema para esta função no Unix.

Para remover um diretório, use "os.rmdir()"; use "os.mkdir()" para
criar um. "os.makedirs(caminho)" criará quaisquer diretórios
intermediários em "path" que não existam. "os.removedirs(caminho)"
removerá diretórios intermediários, desde que estejam vazios; se
quiser excluir toda uma árvore de diretórios e seu conteúdo, use
"shutil.rmtree()".

Para renomear um arquivos, use "os.rename(caminho_antigo,
caminho_novo)".

Para truncar um arquivo, abra-o usando "f = open(arquivo, "rb+")", e
use "f.truncate(posição)"; a posição tem como padrão a posição atual
de busca. Há também "os.ftruncate(fd, posição)" para arquivos abertos
com "os.open()", onde *fd* é o descritor de arquivo (um pequeno
inteiro).

O módulo "shutil" também contém uma série de funções para trabalhar em
arquivos, incluindo "copyfile()", "copytree()" e "rmtree()".


Como eu copio um arquivo?
-------------------------

O módulo "shutil" contém uma função "copyfile()". Observe que em
volumes NTFS do Windows, ele não copia fluxos de dados alternativos
nem forks de recursos em volumes HFS+ do macOS, embora ambos sejam
raramente usados agora. Ele também não copia permissões de arquivo e
metadados, embora usar "shutil.copy2()" em vez disso preserve a
maioria (embora não todos) deles.


Como leio (ou escrevo) dados binários?
--------------------------------------

Para ler ou escrever formatos de dados binários complexos, é melhor
usar o módulo "struct". Ele permite que você pegue uma string contendo
dados binários (geralmente números) e a converta em objetos Python; e
vice-versa.

Por exemplo, o código a seguir lê dois inteiros de 2 bytes e um
inteiro de 4 bytes no formato big-endian de um arquivo:

   import struct

   with open(filename, "rb") as f:
       s = f.read(8)
       x, y, z = struct.unpack(">hhl", s)

O '>' na string de formato força dados big-endian; a letra 'h' lê um
"inteiro curto" (2 bytes) e 'l' lê um "inteiro longo" (4 bytes) da
string.

Para dados mais regulares (por exemplo, uma lista homogênea de ints ou
floats), você também pode usar o módulo "array".

Nota:

  Para ler e escrever dados binários, é obrigatório abrir o arquivo no
  modo binário (aqui, passando ""rb"" para "open()"). Se você usar
  ""r"" em vez disso (o padrão), o arquivo será aberto no modo texto e
  "f.read()" retornará objetos "str" em vez de objetos "bytes".


Por que não consigo usar os.read() em um encadeamento com os.popen()?
---------------------------------------------------------------------

"os.read()" é uma função de baixo nível que pega um descritor de
arquivo, um pequeno inteiro representando o arquivo aberto.
"os.popen()" cria um objeto arquivo de alto nível, o mesmo tipo
retornado pela função embutida "open()". Assim, para ler *n* bytes de
um pipe *p* criado com "os.popen()", você precisa usar "p.read(n)".


Como acesso a porta serial (RS232)?
-----------------------------------

Para Win32, OSX, Linux, BSD, Jython, IronPython:

   pyserial

Para Unix, veja uma postagem da Usenet de Mitch Chapman:

   https://groups.google.com/groups?selm=34A04430.CF9@ohioee.com


Por que o sys.stdout (stdin, stderr) não fecha?
-----------------------------------------------

Os *objetos arquivos* do Python são uma camada de alto nível de
abstração em descritores de arquivo C de baixo nível.

Para a maioria dos objetos arquivo que você cria em Python por meio da
função embutida "open()", "f.close()" marca o objeto arquivo Python
como fechado do ponto de vista do Python e também organiza o
fechamento do descritor de arquivo C subjacente. Isso também acontece
automaticamente no destrutor de "f", quando "f" se torna lixo.

Mas stdin, stdout e stderr são tratados de forma especial pelo Python,
devido ao status especial que também lhes é dado pelo C. Executar
"sys.stdout.close()" marca o objeto arquivo de nível Python como
fechado, mas *não* fecha o descritor de arquivo C associado.

Para fechar o descritor de arquivo C subjacente para um desses três,
você deve primeiro ter certeza de que é isso que você realmente quer
fazer (por exemplo, você pode confundir módulos de extensão tentando
fazer E/S). Se for, use "os.close()":

   os.close(stdin.fileno())
   os.close(stdout.fileno())
   os.close(stderr.fileno())

Ou você pode usar as constantes numéricas 0, 1 e 2, respectivamente.


Programação Rede / Internet
===========================


Quais ferramentas para WWW existem no Python?
---------------------------------------------

Veja os capítulos intitulados Protocolos de Internet e Suporte e
Manuseio de Dados na Internet no Manual de Referência da Biblioteca.
Python tem muitos módulos que ajudarão você a construir sistemas web
do lado do servidor e do lado do cliente.

Um resumo dos frameworks disponíveis é disponibilizado por Paul Boddie
em https://wiki.python.org/moin/WebProgramming.


Qual módulo devo usar para ajudar na geração do HTML?
-----------------------------------------------------

Você pode encontrar uma coleção de links úteis na página wiki
WebProgramming.


Como envio um e-mail de um script Python?
-----------------------------------------

Use a biblioteca padrão do módulo "smtplib".

Aqui está um remetente de e-mail interativo muito simples. Este método
funcionará em qualquer host que suporte o protocolo SMTP.

   import sys, smtplib

   fromaddr = input("From: ")
   toaddrs  = input("To: ").split(',')
   print("Enter message, end with ^D:")
   msg = ''
   while True:
       line = sys.stdin.readline()
       if not line:
           break
       msg += line

   # O envio de e-mail real
   server = smtplib.SMTP('localhost')
   server.sendmail(fromaddr, toaddrs, msg)
   server.quit()

Uma alternativa somente para Unix usa o sendmail. A localização do
programa sendmail varia entre os sistemas; às vezes é
"/usr/lib/sendmail", às vezes "/usr/sbin/sendmail". A página de manual
do sendmail vai ajudar você. Aqui está um código de exemplo:

   import os

   SENDMAIL = "/usr/sbin/sendmail"  # local do sendmail
   p = os.popen("%s -t -i" % SENDMAIL, "w")
   p.write("To: receiver@example.com\n")
   p.write("Subject: teste\n")
   p.write("\n")  # linha vazia separando cabeçalho do corpo
   p.write("Algum texto\n")
   p.write("mais um pouco de texto\n")
   sts = p.close()
   if sts != 0:
       print("Status de saída do sendmail", sts)


Como evito um bloqueio no método connect() de um soquete?
---------------------------------------------------------

O módulo "select" é normalmente usado para ajudar com E/S assíncrona
nos soquetes.

Para evitar que a conexão TCP bloqueie, você pode definir o soquete
para o modo sem bloqueio. Então, quando você fizer o "connect()", você
se conectará imediatamente (improvável) ou obterá uma exceção que
contém o número de erro como ".errno". "errno.EINPROGRESS" indica que
a conexão está em andamento, mas ainda não terminou. Diferentes
sistemas operacionais retornarão valores diferentes, então você terá
que verificar o que é retornado no seu sistema.

Você pode usar o método "connect_ex()" para evitar criar uma exceção.
Ele retornará apenas o valor de errno. Para pesquisar, você pode
chamar "connect_ex()" novamente mais tarde -- "0" ou "errno.EISCONN"
indicam que você está conectado -- ou você pode passar este soquete
para "select.select()" para verificar se ele é gravável.

Nota:

  O módulo "asyncio" fornece uma biblioteca assíncrona de thread única
  e concorrente de propósito geral, que pode ser usada para escrever
  código de rede não bloqueante. A biblioteca de terceiros Twisted é
  uma alternativa popular e rica em recursos.


Base de Dados
=============


Existem interfaces para banco de dados em Python?
-------------------------------------------------

Sim.

Interfaces para hashes baseados em disco, como "DBM" e "GDBM" também
estão incluídas no Python padrão. Há também o módulo "sqlite3", que
fornece um banco de dados relacional baseado em disco leve.

Suporte para a maioria dos bancos de dados relacionais está
disponível. Para mais detalhes, veja a página wiki DatabaseProgramming
para detalhes.


Como você implementa objetos persistentes no Python?
----------------------------------------------------

O módulo de biblioteca "pickle" resolve isso de uma maneira muito
geral (embora você ainda não possa armazenar coisas como arquivos
abertos, soquetes ou janelas), e o módulo de biblioteca "shelve" usa
pickle e (g)dbm para criar mapeamentos persistentes contendo objetos
Python arbitrários.


Matemáticos e Numéricos
=======================


Como gero número aleatórios no Python?
--------------------------------------

O módulo padrão "random" implementa um gerador de números aleatórios.
O uso é simples:

   import random
   random.random()

Isso retorna um número flutuante aleatório no intervalo [0, 1).

Existem também muitos outros geradores aleatórios neste módulo, como:

* "randrange(a, b)" escolhe um número inteiro no intervalo entre [a,
  b).

* "uniform(a, b)" escolhe um número de ponto flutuante no intervalo
  [a, b).

* "normalvariate(mean, sdev)" gera números pseudoaleatórios que seguem
  uma distribuição normal (Gaussiana).

Algumas funções de nível elevado operam diretamente em sequencia,
como:

* "choice(S)" escolhe um elemento aleatório de uma determinada
  sequência.

* "shuffle(L)" embaralha uma lista internamente, ou seja permuta seus
  elementos aleatoriamente.

Existe também uma classe "Random" que você pode instanciar para criar
vários geradores de números aleatórios independentes.
