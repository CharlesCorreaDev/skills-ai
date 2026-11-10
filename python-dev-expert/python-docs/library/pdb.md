"pdb" --- O depurador do Python
*******************************

**Código-fonte:** Lib/pdb.py

======================================================================

O módulo "pdb" define um depurador de código-fonte interativo para
programas Python. Ele possui suporte a definição de pontos de
interrupção (condicionais) e passo único no nível da linha de origem,
inspeção de quadros de pilha, listagem de código-fonte e avaliação de
código Python arbitrário no contexto de qualquer quadro de pilha. Ele
também tem suporte a depuração *post-mortem* e pode ser chamado sob
controle do programa.

O depurador é extensível -- na verdade, ele é definido como a classe
"Pdb". Atualmente, isso não está documentado, mas é facilmente
compreendido pela leitura do código-fonte. A interface de extensão usa
os módulos "bdb" e "cmd".

Ver também:

  Módulo "faulthandler"
     Usado para despejar tracebacks (situação da pilha de execução) do
     Python explicitamente, em uma falha, após um tempo limite ou em
     um sinal do usuário.

  Módulo "traceback"
     Interface padrão para extrair, formatar e imprimir rastreamentos
     de pilha de programas Python.

O uso típico para entrar no depurador é inserir:

   import pdb; pdb.set_trace()

ou:

   breakpoint()

no local que você deseja entrar o depurador e, em seguida, executar o
programa. Você pode percorrer o código seguindo esta instrução e
continuar executando sem o depurador usando o comando "continue".

Alterado na versão 3.7: A função embutida "breakpoint()", quando
chamada com valores padrão, pode ser usada em vez de "import pdb;
pdb.set_trace()".

   def double(x):
      breakpoint()
      return x * 2
   val = 3
   print(f"{val} * 2 is {double(val)}")

O prompt do depurador é "(Pdb)", que é o indicador de que você está no
modo de depuração:

   > ...(2)double()
   -> breakpoint()
   (Pdb) p x
   3
   (Pdb) continue
   3 * 2 is 6

Alterado na versão 3.3: O preenchimento por tabulação através do
módulo "readline" está disponível para comandos e argumentos de
comando, por exemplo os nomes globais e locais atuais são oferecidos
como argumentos do comando "p".


Interface de linha de comando
=============================

Você também pode invocar "pdb" na linha de comando para depurar outros
scripts. Por exemplo:

   python -m pdb [-c comando] (-m módulo | -p pid | arquivo_python) [argumentos ...]

Quando invocado como um módulo, o pdb entra automaticamente na
depuração *post-mortem* se o programa que está sendo depurado for
encerrado de forma anormal. Após a depuração *post-mortem* (ou após a
saída normal do programa), o pdb reiniciará o programa. A
reinicialização automática preserva o estado do pdb (p.ex., pontos de
interrupção) e, na maioria dos casos, é mais útil do que encerrar o
depurador na saída do programa.

-c, --command <command>

   Para executar comandos como se fossem dados em um arquivo ".pdbrc".
   Veja Comandos de depuração.

   Alterado na versão 3.2: Adicionada a opção "-c".

-m <module>

   Para executar módulos de maneira similar ao "python -m". Assim como
   em um script, o depurador pausará a execução logo antes da primeira
   linha do módulo.

   Alterado na versão 3.7: Adicionada a opção "-m".

-p, --pid <pid>

   Anexa ao processo com o PID especificado.

   Adicionado na versão 3.14.

Para anexar a um processo Python em execução para depuração remota,
use a opção "-p" ou "--pid" com o PID do processo de destino:

   python -m pdb -p 1234

Nota:

  Anexar a um processo remoto bloqueado em uma chamada de sistema ou
  aguardando E/S só funcionará quando a próxima instrução de bytecode
  for executada ou quando o processo receber um sinal.

O uso típico para executar uma instrução sob o controle do depurador
é:

   >>> import pdb
   >>> def f(x):
   ...     print(1 / x)
   >>> pdb.run("f(2)")
   > <string>(1)<module>()
   (Pdb) continue
   0.5
   >>>

O uso típico para inspecionar um programa com falha é:

   >>> import pdb
   >>> def f(x):
   ...     print(1 / x)
   ...
   >>> f(0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 2, in f
   ZeroDivisionError: division by zero
   >>> pdb.pm()
   > <stdin>(2)f()
   (Pdb) p x
   0
   (Pdb)

Alterado na versão 3.13: A implementação da **PEP 667** significa que
atribuições de nomes feitas via "pdb" afetarão imediatamente o escopo
ativo, mesmo quando executado dentro de um *escopo otimizado*.

O módulo define as seguintes funções; cada uma entra no depurador de
uma maneira ligeiramente diferente:

pdb.run(statement, globals=None, locals=None)

   Executa a instrução *statement* (fornecida como uma string ou um
   objeto código) sob controle do depurador. O prompt do depurador
   aparece antes de qualquer código ser executado; você pode definir
   pontos de interrupção e digitar "continue" ou pode percorrer a
   instrução usando "step" ou "next" (todos esses comandos são
   explicados abaixo). Os argumentos opcionais *globals* e *locals*
   especificam o ambiente em que o código é executado; por padrão, o
   dicionário do módulo "__main__" é usado. (Veja a explicação das
   funções embutidas "exec()" ou "eval()".)

pdb.runeval(expression, globals=None, locals=None)

   Avalia a expressão *expression* (fornecida como uma string ou um
   objeto código) sob controle do depurador. Quando "runeval()"
   retorna, ele retorna o valor de *expression*. Caso contrário, esta
   função é semelhante a "run()".

pdb.runcall(function, *args, **kwds)

   Chama a função *function* (um objeto função ou método, não uma
   string) com os argumentos fornecidos. Quando "runcall()" retorna,
   ele retorna qualquer que seja a chamada de função retornada. O
   prompt do depurador aparece assim que a função é inserida.

pdb.set_trace(*, header=None, commands=None)

   Entra no depurador no quadro da pilha de chamada. Isso é útil para
   codificar um ponto de interrupção em um determinado ponto de um
   programa, mesmo que o código não esteja sendo depurado de outra
   forma (por exemplo, quando uma asserção falha). Se fornecido,
   *header* é impresso no console imediatamente antes do início da
   depuração. O argumento *commands*, se fornecido, é uma lista de
   comandos para executar quando o depurador é iniciado.

   Alterado na versão 3.7: O argumento somente-nomeado *header*.

   Alterado na versão 3.13: "set_trace()" entrará no depurador
   imediatamente, em vez da próxima linha de código a ser executada.

   Adicionado na versão 3.14: O argumento *commands*.

awaitable pdb.set_trace_async(*, header=None, commands=None)

   Versão async de "set_trace()". Esta função deve ser usada dentro de
   uma função async com "await".

      async def f():
          await pdb.set_trace_async()

   As instruções "await" são suportadas se o depurador for invocado
   por esta função.

   Adicionado na versão 3.14.

pdb.post_mortem(t=None)

   Entra em depuração post-mortem da exceção fornecida ou objeto
   traceback. Se nenhum valor for fornecido, usa a exceção que está
   sendo tratada no momento ou levanta "ValueError" se não houver
   nenhuma.

   Alterado na versão 3.13: Adiciona suporte a objetos exceção.

pdb.pm()

   Entra a depuração post-mortem da exceção encontrada em
   "sys.last_exc".

pdb.set_default_backend(backend)

   Há dois backends suportados para pdb: "'settrace'" e
   "'monitoring'". Consulte "bdb.Bdb" para obter detalhes. O usuário
   pode definir o backend padrão a ser usado caso nenhum seja
   especificado ao instanciar "Pdb". Se nenhum backend for
   especificado, o padrão será "'settrace'".

   Nota:

     "breakpoint()" e "set_trace()" não serão afetados por esta
     função. Eles sempre usam o backend "'monitoring'".

   Adicionado na versão 3.14.

pdb.get_default_backend()

   Retorna o backend padrão para pdb.

   Adicionado na versão 3.14.

As funções "run*" e a "set_trace()" são aliases, ou apelidos, para
instanciar a classe "Pdb" e chamar o método com o mesmo nome. Se você
deseja acessar outros recursos, faça você mesmo:

class pdb.Pdb(completekey='tab', stdin=None, stdout=None, skip=None, nosigint=False, readrc=True, mode=None, backend=None, colorize=False)

   "Pdb" é a classe do depurador.

   Os argumentos *completekey*, *stdin* e *stdout* são passados para a
   classe subjacente "cmd.Cmd"; veja a descrição lá.

   O argumento *skip*, se fornecido, deve ser um iterável de padrões
   de nome de módulo no estilo glob. O depurador não entrará nos
   quadros que se originam em um módulo que corresponde a um desses
   padrões. [1]

   Por padrão, o Pdb define um manipulador para o sinal SIGINT (que é
   enviado quando o usuário pressiona "Ctrl"-"C" no console) quando
   você dá um comando "continue". Isso permite que você entre no
   depurador novamente pressionando "Ctrl"-"C". Se você deseja que o
   Pdb não toque no manipulador SIGINT, defina *nosigint* como
   verdadeiro.

   O argumento *readrc* é padronizado como verdadeiro e controla se o
   Pdb carregará arquivos .pdbrc do sistema de arquivos.

   O argumento *mode* especifica como o depurador foi invocado. Ele
   afeta o funcionamento de alguns comandos do depurador. Os valores
   válidos são "'inline'" (usado pelo comando embutido breakpoint()),
   "'cli'" (usado pela invocação da linha de comando) ou "None" (para
   comportamento retrocompatível, como antes da adição do argumento
   *mode*).

   O argumento *backend* especifica o backend a ser usado pelo
   depurador. Se "None" for passado, o backend padrão será usado.
   Consulte "set_default_backend()". Caso contrário, os backends
   implementados são "'settrace'" e "'monitoring'".

   O argumento *colorize*, se definido como "True", habilitará a saída
   colorida no depurador, se houver suporte para cores. Isso destacará
   o código-fonte exibido no pdb.

   Exemplo de chamada para habilitar rastreamento com *skip*:

      import pdb; pdb.Pdb(skip=['django.*']).set_trace()

   Levanta um evento de auditoria "pdb.Pdb" sem argumentos.

   Alterado na versão 3.1: Adicionado o parâmetro *skip*.

   Alterado na versão 3.2: Adicionado o parâmetro *nosigint*.
   Anteriormente, um manipulador de SIGINT nunca era definido por Pdb.

   Alterado na versão 3.6: O argumento *readrc*.

   Adicionado na versão 3.14: Adicionado o argumento *mode*.

   Adicionado na versão 3.14: Adicionado o argumento *backend*.

   Adicionado na versão 3.14: Adicionado o argumento *colorize*.

   Alterado na versão 3.14: Pontos de interrupção em linha como
   "breakpoint()" ou "pdb.set_trace()" sempre interromperão o programa
   ao chamar o quadro, ignorando o padrão *skip* (se houver).

   run(statement, globals=None, locals=None)
   runeval(expression, globals=None, locals=None)
   runcall(function, *args, **kwds)
   set_trace()

      Consulte a documentação para as funções explicadas acima.


Comandos de depuração
=====================

Os comandos reconhecidos pelo depurador estão listados abaixo. A
maioria dos comandos pode ser abreviada para uma ou duas letras,
conforme indicado; por exemplo, "h(elp)" significa que "h" ou "help"
podem ser usados para inserir o comando de ajuda (mas não "he" ou
"hel", nem "H" ou "Help" ou "HELP"). Os argumentos para os comandos
devem ser separados por espaços em branco (espaços ou tabulações). Os
argumentos opcionais estão entre colchetes ("[]") na sintaxe do
comando; os colchetes não devem ser digitados. As alternativas na
sintaxe de comando são separadas por uma barra vertical ("|").

Digitar uma linha em branco repete o último comando digitado. Exceção:
se o último comando foi um comando "list", as próximas 11 linhas serão
listadas.

Os comandos que o depurador não reconhece são presumidos como
instruções Python e são executados no contexto do programa que está
sendo depurado. As instruções Python também podem ser prefixadas com
um ponto de exclamação ("!"). Essa é uma maneira poderosa de
inspecionar o programa que está sendo depurado; é até possível alterar
uma variável ou chamar uma função. Quando ocorre uma exceção em uma
instrução, o nome da exceção é impresso, mas o estado do depurador não
é alterado.

Alterado na versão 3.13: Expressões/instruções, cujo prefixo é um
comando pdb, agora são identificadas e executadas corretamente.

O depurador possui suporte a aliases. Os aliases podem ter parâmetros
que permitem um certo nível de adaptabilidade ao contexto em exame.

Vários comandos podem ser inseridos em uma única linha, separados por
";;". (Um único ";" não é usado, pois é o separador para vários
comandos em uma linha que é passada para o analisador Python.) Nenhuma
inteligência é aplicada para separar os comandos; a entrada é dividida
no primeiro par ";;", mesmo que esteja no meio de uma string entre
aspas. Uma solução alternativa para strings com caractere de ponto e
vírgula duplo é usar a concatenação de string implícita "';'';'" ou
"";"";"".

Para definir uma variável global temporária, use uma *variável de
conveniência*. Uma *variável de conveniência* é uma variável cujo nome
começa com "$". Por exemplo, "$foo = 1" define uma variável global
"$foo" que você pode usar na sessão do depurador. As *variáveis de
conveniência* são limpas quando o programa retoma a execução, portanto
é menos provável que interfira em seu programa em comparação ao uso de
variáveis normais como "foo = 1".

Existem quatro *variáveis de conveniência* predefinidas:

* "$_frame": o quadro atual que você está depurando

* "$_retval": o valor de retorno se o quadro estiver retornando

* "$_exception": a exceção se o quadro estiver levantando uma exceção

* "$_asynctask": a tarefa asyncio se o pdb parar em uma função
  assíncrona

Adicionado na versão 3.12: Adicionado o recurso de *variável de
conveniência*.

Adicionado na versão 3.14: Adicionada a variável de conveniência
"$_asynctask".

Se um arquivo ".pdbrc" existe no diretório inicial do usuário ou no
diretório atual, ele é lido com a codificação "'utf-8'" e executado
como se tivesse sido digitado no prompt do depurador, com a exceção de
que linhas vazias e linhas iniciando com "#" são ignoradas. Isso é
particularmente útil para aliases. Se ambos os arquivos existirem,
aquele no diretório inicial será lido primeiro e os aliases definidos
poderão ser substituídos pelo arquivo local.

Alterado na versão 3.2: ".pdbrc" agora pode conter comandos que
continuam a depuração, como "continue" ou "next". Anteriormente, esses
comandos não tinham efeito.

Alterado na versão 3.11: ".pdbrc" agora é lido com a codificação
"'utf-8'". Anteriormente, ele era lido com a codificação da localidade
do sistema.

h(elp) [command]

   Sem argumento, imprime a lista de comandos disponíveis. Com um
   *command* como argumento, imprime ajuda sobre esse comando. "help
   pdb" exibe a documentação completa (a docstring do módulo "pdb").
   Como o argumento *command* deve ser um identificador, "help exec"
   deve ser inserido para obter ajuda sobre o comando "!".

w(here) [count]

   Exibe um stack trace (situação da pilha de execução), com o quadro
   mais recente na parte inferior. Se *count* for 0, exibe a entrada
   do quadro atual. Se *count* for negativo, exibe os quadros menos
   recentes - *count*. Se *count* for positivo, exibe os quadros
   *count* mais recentes. Uma seta (">") indica o quadro atual, que
   determina o contexto da maioria dos comandos.

   Alterado na versão 3.14: o argumento *count* foi adicionado

d(own) [count]

   Move os níveis do quadro atual *count* (padrão 1) para baixo no
   stack trace (para um quadro mais recente).

u(p) [count]

   Move os níveis do quadro atual na *count* (padrão 1) para cima no
   stack trace (para um quadro mais antigo).

b(reak) [([filename:]lineno | function) [, condition]]

   Com um argumento *lineno*, define uma quebra na linha *lineno* no
   arquivo atual. O número da linha pode ser prefixado com *filename*
   e dois pontos, para especificar um ponto de interrupção em outro
   arquivo (possivelmente um que ainda não tenha sido carregado). O
   arquivo é pesquisado em "sys.path". Formas aceitáveis de *filename*
   são "/caminhoabsoluto/para/arquivo.py",
   "caminhorelativo/do/arquivo.py", "módulo" e "pacote.módulo".

   Com um argumento *function*, define uma interrupção na primeira
   instrução executável dentro dessa função. *function* pode ser
   qualquer expressão avaliada como uma função no espaço de nomes
   atual.

   Se um segundo argumento estiver presente, é uma expressão que deve
   ser avaliada como verdadeira antes que o ponto de interrupção seja
   respeitado.

   Sem argumento, lista todas as quebras, inclusive para cada ponto de
   interrupção, o número de vezes que o ponto de interrupção foi
   atingido, a contagem atual de ignorados e a condição associada, se
   houver.

   Cada ponto de interrupção recebe um número ao qual todos os outros
   comandos de ponto de interrupção se referem.

tbreak [([filename:]lineno | function) [, condition]]

   Ponto de interrupção temporário, que é removido automaticamente
   quando é atingido pela primeira vez. Os argumentos são os mesmos
   que para "break".

cl(ear) [filename:lineno | bpnumber ...]

   Com um argumento *filename:lineno*, limpa todos os pontos de
   interrupção nessa linha. Com uma lista separada por espaços de
   números de ponto de interrupção, limpa esses pontos de interrupção.
   Sem argumento, limpa todas as quebras (mas primeiro pede a
   confirmação).

disable bpnumber [bpnumber ...]

   Desativa os pontos de interrupção fornecidos como uma lista
   separada por espaços de números de pontos de interrupção.
   Desabilitar um ponto de interrupção significa que ele não pode
   interromper a execução do programa, mas, ao contrário de limpar um
   ponto de interrupção, ele permanece na lista de pontos de
   interrupção e pode ser (re)ativado.

enable bpnumber [bpnumber ...]

   Ativa o ponto de interrupção especificado.

ignore bpnumber [count]

   Define a contagem de ignorados para o número do ponto de
   interrupção especificado. Se *count* for omitida, a contagem de
   ignorados será definida como 0. Um ponto de interrupção se torna
   ativo quando a contagem de ignorados é zero. Quando diferente de
   zero, a contagem é decrementada cada vez que o ponto de interrupção
   é atingido e o ponto de interrupção não é desativado e qualquer
   condição associada é avaliada como verdadeira.

condition bpnumber [condition]

   Define uma nova *condition* para o ponto de interrupção, uma
   expressão que deve ser avaliada como verdadeira antes que o ponto
   de interrupção seja respeitado. Se *condition* for omitida,
   qualquer condição existente será removida; isto é, o ponto de
   interrupção é tornado incondicional.

commands [bpnumber]

   Especifica uma lista de comandos para o número do ponto de
   interrupção *bpnumber*. Os próprios comandos aparecem nas linhas
   seguintes. Digite em uma linha contendo apenas "end" para finalizar
   os comandos. Um exemplo:

      (Pdb) commands 1
      (com) p alguma_variável
      (com) end
      (Pdb)

   Para remover todos os comandos de um ponto de interrupção, digite
   "commands" e siga-o imediatamente com "end"; isto é, não dê
   comandos.

   Sem o argumento *bpnumber*, "commands" refere-se ao ponto de
   interrupção definido mais recentemente que ainda existe.

   Você pode usar comandos de ponto de interrupção para iniciar seu
   programa novamente. Simplesmente use o comando "continue", ou
   "step", ou qualquer outro comando que reinicie a execução.

   Especificar qualquer comando que retome a execução (atualmente
   "continue", "step", "next", "return", "until", "jump", "quit" e
   suas abreviações) finaliza a lista de comandos (como se esse
   comando fosse imediatamente seguido pelo end). Isso ocorre porque
   sempre que você retoma a execução (mesmo com um simples next ou
   step), você pode encontrar outro ponto de interrupção — que pode
   ter sua própria lista de comandos, levando a ambiguidades sobre
   qual lista executar.

   Se a lista de comandos contiver o comando "silent" ou um comando
   que retome a execução, a mensagem de ponto de interrupção contendo
   informações sobre o quadro não será exibida.

   Alterado na versão 3.14: As informações do quadro não serão
   exibidas se um comando que retome a execução estiver presente na
   lista de comandos.

s(tep)

   Executa a linha atual, interrompe na primeira ocasião possível (em
   uma função chamada ou na próxima linha na função atual).

n(ext)

   Continua a execução até que a próxima linha na função atual seja
   atingida ou ela retorne. (A diferença entre "next" e "step" é que
   "step" para dentro de uma função chamada, enquanto "next" executa
   funções chamadas em (quase) velocidade máxima, parando apenas na
   próxima linha da função atual.)

unt(il) [lineno]

   Sem argumento, continua a execução até que a linha com um número
   maior que o atual seja atingida.

   Com *lineno*, continua a execução até que uma linha com um número
   maior ou igual a *lineno* ser alcançada. Nos dois casos, também
   interrompe quando o quadro atual retornar.

   Alterado na versão 3.2: Permite fornecer um número de linha
   explícito.

r(eturn)

   Continua a execução até que a função atual retorne.

c(ont(inue))

   Continua a execução, interrompe apenas quando um ponto de
   interrupção for encontrado.

j(ump) lineno

   Define a próxima linha que será executada. Disponível apenas no
   quadro mais inferior. Isso permite voltar e executar o código
   novamente ou avançar para pular o código que você não deseja
   executar.

   Deve-se notar que nem todos os saltos são permitidos -- por
   exemplo, não é possível pular para o meio de um loop de "for" ou
   sair de uma cláusula "finally".

l(ist) [first[, last]]

   Lista o código-fonte do arquivo atual. Sem argumentos, lista 11
   linhas ao redor da linha atual ou continue a listagem anterior. Com
   "." como argumento, lista 11 linhas ao redor da linha atual. Com um
   argumento, lista 11 linhas nessa linha. Com dois argumentos, lista
   o intervalo especificado; se o segundo argumento for menor que o
   primeiro, ele será interpretado como uma contagem.

   A linha atual no quadro atual é indicada por "->". Se uma exceção
   estiver sendo depurada, a linha em que a exceção foi originalmente
   gerada ou propagada é indicada por ">>", se for diferente da linha
   atual.

   Alterado na versão 3.2: Adicionado o marcador ">>".

ll | longlist

   Lista todo o código-fonte da função ou quadro atual. As linhas
   interessantes estão marcadas como para "list".

   Adicionado na versão 3.2.

a(rgs)

   Imprime os argumentos da função atual e seus valores atuais.

p expression

   Avalia *expression* no contexto atual e imprima seu valor.

   Nota:

     "print()" também pode ser usado, mas não é um comando de
     depuração --- isso executa a função Python "print()".

pp expression

   Como o comando "p", exceto que o valor de *expression* é bastante
   impresso usando o módulo "pprint".

whatis expression

   Exibe o tipo de *expression*.

source expression

   Tenta obter o código-fonte de *expression* e exibe-o.

   Adicionado na versão 3.2.

display [expression]

   Exibe o valor de *expression* caso ela tenha sido alterada, sempre
   que a execução for interrompida no quadro atual.

   Sem *expression*, lista todas as expressões de exibição para o
   quadro atual.

   Nota:

     Display avalia *expression* e compara com o resultado da
     avaliação anterior de *expression*, portanto, quando o resultado
     é mutável, display pode não ser capaz de captar as alterações.

   Exemplo:

      lst = []
      breakpoint()
      pass
      lst.append(1)
      print(lst)

   Display não perceberá que "lst" foi alterado porque o resultado da
   avaliação foi modificado internamente por "lst.append(1)" antes de
   ser comparado:

      > example.py(3)<module>()
      -> pass
      (Pdb) display lst
      display lst: []
      (Pdb) n
      > example.py(4)<module>()
      -> lst.append(1)
      (Pdb) n
      > example.py(5)<module>()
      -> print(lst)
      (Pdb)

   Você pode fazer alguns truques com o mecanismo de cópia para
   fazê-lo funcionar:

      > example.py(3)<module>()
      -> pass
      (Pdb) display lst[:]
      display lst[:]: []
      (Pdb) n
      > example.py(4)<module>()
      -> lst.append(1)
      (Pdb) n
      > example.py(5)<module>()
      -> print(lst)
      display lst[:]: [1]  [old: []]
      (Pdb)

   Adicionado na versão 3.2.

undisplay [expression]

   Não exibe mais *expression* no quadro atual. Sem expressão, limpa
   todas as expressões de exibição para o quadro atual.

   Adicionado na versão 3.2.

interact

   Inicia um interpretador interativo (usando o módulo "code") em um
   novo espaço de nomes global inicializado a partir dos espaços de
   nomes locais e globais para o escopo atual. Use "exit()" ou
   "quit()" para sair do interpretador e retornar ao depurador.

   Nota:

     Como "interact" cria um novo espaço de nomes dedicado para
     execução de código, atribuições a variáveis não afetarão os
     espaços de nomes originais. No entanto, as modificações em
     quaisquer objetos mutáveis referenciados serão refletidas nos
     espaços de nomes originais, como de costume.

   Adicionado na versão 3.2.

   Alterado na versão 3.13: "exit()" e "quit()" podem ser usados para
   sair do comando "interact".

   Alterado na versão 3.13: "interact" direciona sua saída para o
   canal de saída do depurador em vez de "sys.stderr".

alias [name [command]]

   Cria um apelido chamado *name* que executa *command*. O comando
   *command* *não* deve ser colocado entre aspas. Parâmetros
   substituíveis podem ser indicados por "%1", "%2", ... e "%9",
   enquanto "%*" é substituído por todos os parâmetros. Se *command*
   for omitido, o apelido atual para *name* será mostrado. Se nenhum
   argumento for fornecido, todos os apelidos serão listados.

   Os aliases podem ser aninhados e podem conter qualquer coisa que
   possa ser digitada legalmente no prompt do pdb. Observe que os
   comandos internos do pdb *podem* ser substituídos por aliases. Esse
   comando é oculto até que o alias seja removido. O alias é aplicado
   recursivamente à primeira palavra da linha de comando; todas as
   outras palavras da linha são deixadas em paz.

   Como exemplo, aqui estão dois aliases úteis (especialmente quando
   colocados no arquivo ".pdbrc"):

      # Exibe variáveis de instância (use em "pi classInst")
      alias pi for k in %1.__dict__.keys(): print(f"%1.{k} = {%1.__dict__[k]}")
      # Exibe variáveis de instância em self
      alias ps pi self

unalias name

   Executa o alias *name* especificado.

! statement

   Executa a instrução *statement* (de uma só linha) no contexto do
   quadro de pilha atual. O ponto de exclamação pode ser omitido, a
   menos que a primeira palavra da instrução seja semelhante a um
   comando de depuração, por exemplo:

      (Pdb) ! n=42
      (Pdb)

   Para definir uma variável global, você pode prefixar o comando de
   atribuição com uma instrução "global" na mesma linha, por exemplo:

      (Pdb) global list_options; list_options = ['-l']
      (Pdb)

run [args ...]
restart [args ...]

   Reinicia o programa Python depurado. Se *args* for fornecido, ele é
   dividido com "shlex" e o resultado é usado como o novo "sys.argv".
   Histórico, pontos de interrupção, ações e opções do depurador são
   preservados. "restart" é um apelido para "run".

   Alterado na versão 3.14: Os comandos "run" e "restart" são
   desabilitados quando o depurador é invocado no modo "'inline'".

q(uit)

   Sai do depurador. O programa que está sendo executado é abortado.
   Uma entrada com fim de arquivo equivale a "quit".

   Um prompt de confirmação será exibido se o depurador for invocado
   no modo "'inline'". "y", "Y", "<Enter>" ou "EOF" confirmarão o
   encerramento.

   Alterado na versão 3.14: Um prompt de confirmação será exibido se o
   depurador for invocado no modo "'inline'". Após a confirmação, o
   depurador chamará "sys.exit()" imediatamente, em vez de levantar
   "bdb.BdbQuit" no próximo evento de rastreamento.

debug code

   Entra em um depurador recursivo que percorre *code* (que é uma
   expressão ou instrução arbitrária a ser executada no ambiente
   atual).

retval

   Exibe o valor de retorno para o último retorno de a função atual.

exceptions [excnumber]

   Lista ou salta entre exceções encadeadas.

   Ao usar "pdb.pm()" ou "Pdb.post_mortem(...)" com uma exceção
   encadeada em vez de um traceback, permite ao usuário mover entre as
   exceções encadeadas usando o comando "exceptions" para listar
   exceções e "exceptions <número>" para mudar para essa exceção.

   Exemplo:

      def out():
          try:
              middle()
          except Exception as e:
              raise ValueError("reraise middle() error") from e

      def middle():
          try:
              return inner(0)
          except Exception as e:
              raise ValueError("Middle fail")

      def inner(x):
          1 / x

      out()

   chamar "pdb.pm()" permitirá mover entre exceções:

      > example.py(5)out()
      -> raise ValueError("reraise middle() error") from e

      (Pdb) exceptions
        0 ZeroDivisionError('division by zero')
        1 ValueError('Middle fail')
      > 2 ValueError('reraise middle() error')

      (Pdb) exceptions 0
      > example.py(16)inner()
      -> 1 / x

      (Pdb) up
      > example.py(10)middle()
      -> return inner(0)

   Adicionado na versão 3.13.

-[ Notas de rodapé ]-

[1] Se um quadro é considerado originário de um determinado módulo é
    determinado pelo "__name__" nos globais do quadro.
