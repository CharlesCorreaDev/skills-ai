"dis" --- Disassembler de bytecode do Python
********************************************

**Código-fonte:** Lib/dis.py

======================================================================

The "dis" module supports the analysis of CPython *bytecode* by
disassembling it. The CPython bytecode which this module takes as an
input is defined in the file "Include/opcode.h" and used by the
compiler and the interpreter.

O bytecode é um detalhe de implementação do interpretador CPython. Não
há garantias de que bytecodes não serão adicionados, removidos ou
alterados entre as versões do Python. O uso deste módulo não deve ser
considerado que funcionará em todas as VMs do Python ou mesmo versões
do Python.

Alterado na versão 3.6: Cada instrução ocupa 2 bytes. Anteriormente, o
número de bytes variava de acordo com a instrução.

Alterado na versão 3.10: O argumento para instruções de pulo,
tratamento de exceção e laço é agora o deslocamento em instruções, ao
invés de em bytes.

Alterado na versão 3.11: Some instructions are accompanied by one or
more inline cache entries, which take the form of "CACHE"
instructions. These instructions are hidden by default, but can be
shown by passing "show_caches=True" to any "dis" utility. Furthermore,
the interpreter now adapts the bytecode to specialize it for different
runtime conditions. The adaptive bytecode can be shown by passing
"adaptive=True".

Alterado na versão 3.12: O argumento de um pulo é o deslocamento da
instrução alvo relativo à instrução que aparece imediatamente após as
entradas "CACHE" da instrução de pulo.Como consequência, a presença de
instruções "CACHE" é transparente para pulos adiante, mas precisa ser
considerada ao lidar com pulos para trás.

Alterado na versão 3.13: A saída agora mostra rótulos lógicos ao invés
dos deslocamentos das instruções para alvos de pulos e de tratadores
de exceções. A opção de linha de comando "-O" e o argumento
"show_offsets" foram adicionados.

Alterado na versão 3.14: A opção de linha de comando "-P" e o
argumento "show_positions" foram adicionados.A opção de linha de
comando "-S" foi adicionada.

Exemplo: Dada a função "myfunc()":

   def myfunc(alist):
       return len(alist)

o comando a seguir pode ser usado para mostrar a desconstrução de
"myfunc()":

   >>> dis.dis(myfunc)
     2           RESUME                   0

     3           LOAD_GLOBAL              1 (len + NULL)
                 LOAD_FAST_BORROW         0 (alist)
                 CALL                     1
                 RETURN_VALUE

(O "2" é o número da linha).


Interface de linha de comando
=============================

The "dis" module can be invoked as a script from the command line:

   python -m dis [-h] [-C] [-O] [-P] [-S] [infile]

As seguintes opções são aceitas:

-h, --help

   Exibe o modo de uso e sai.

-C, --show-caches

   Mostra caches em linha

   Adicionado na versão 3.13.

-O, --show-offsets

   Mostra os deslocamentos das instruções

   Adicionado na versão 3.13.

-P, --show-positions

   Mostra posições de instruções no código-fonte.

   Adicionado na versão 3.14.

-S, --specialized

   Mostra bytecode especializado.

   Adicionado na versão 3.14.

Se "infile" for especificada, o seu código desmontado será escrito no
stdout. Caso contrário, será feito o desmonte da compilação do código-
fonte recebido do stdin.


Análise de bytecode
===================

Adicionado na versão 3.4.

A API de análise de bytecode permite que partes do código Python sejam
encapsuladas em um objeto "Bytecode" que facilite o acesso aos
detalhes do código compilado.

class dis.Bytecode(x, *, first_line=None, current_offset=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)

   Analisa o bytecode correspondente a uma função, um gerador, um
   gerador assíncrono, uma corrotina, um método, uma string de código-
   fonte, ou um objeto de código (conforme retornado por "compile()").

   Esta é um invólucro de conveniência que encapsula muitas das
   funções listadas abaixo, principalmente a "get_instructions()", já
   que iterar sobre sobre uma instância de "Bytecode" produz operações
   bytecode como instâncias de "Instruction".

   Se *first_line* não for "None", ele indica o número de linha que
   deve ser reportado para a primeira linha de código-fonte no código
   desmontado.  Caso contrário, a informação de linha de código-fonte
   (se houver) é extraída diretamente da desconstrução do objeto de
   código.

   Se *current_offset* não for "None", ele é um deslocamento em
   instruções no código desconstruído. Definir este argumento
   significa que o "dis()" vai mostrar um marcador de "instrução
   atual" sobre o opcode especificado.

   Se *show_caches* for "True", o "dis()" vai exibir entradas de cache
   em linha usadas pelo interpretador para especializar o bytecode.

   Se *adaptive* for "True", o "dis()" vai exibir bytecode
   especializado que pode ser diferente do bytecode original.

   Se *show_offsets* for "True", o "dis()" vai incluir deslocamentos
   em instruções na saída.

   Se *show_positions* for "True", "dis()" incluirá posições do
   código-fonte da instrução na saída.

   classmethod from_traceback(tb, *, show_caches=False)

      Constrói uma instância de "Bytecode" a partir do traceback
      fornecido, definindo *current_offset* apontando para a instrução
      responsável pela exceção.

   codeobj

      O objeto de código compilado.

   first_line

      A primeira linha de código-fonte do objeto de código (caso
      disponível).

   dis()

      Retorna uma visualização formatada das operações em bytecode (as
      mesmas que seriam impressas pela "dis.dis()", mas retornadas
      como uma string multilinha).

   info()

      Retorna uma string multilinha formatada com informação detalhada
      sobre o objeto de código, como "code_info()".

   Alterado na versão 3.7: Este método agora lida com objetos de
   corrotina e de gerador assíncrono.

   Alterado na versão 3.11: Adicionados os parâmetros *show_caches* e
   *adaptive*.

   Alterado na versão 3.13: Adicionado o parâmetro *show_offsets*

   Alterado na versão 3.14: Foi adicionado o parâmetro
   *show_positions*.

Exemplo:

   >>> bytecode = dis.Bytecode(myfunc)
   >>> for instr in bytecode:
   ...     print(instr.opname)
   ...
   RESUME
   LOAD_GLOBAL
   LOAD_FAST_BORROW
   CALL
   RETURN_VALUE


Funções de análise
==================

The "dis" module also defines the following analysis functions that
convert the input directly to the desired output. They can be useful
if only a single operation is being performed, so the intermediate
analysis object isn't useful:

dis.code_info(x)

   Retorna uma string multilinha formatada com informação detalhada
   sobre o objeto de código correspondente à função, gerador, gerador
   assíncrono, corrotina, método, string de código-fonte ou objeto de
   código fornecido.

   Observe que o conteúdo exato de strings de informação de código são
   altamente dependentes da implementação e podem mudar de forma
   arbitrária através de VMs Python ou lançamentos do Python.

   Adicionado na versão 3.2.

   Alterado na versão 3.7: Este método agora lida com objetos de
   corrotina e de gerador assíncrono.

dis.show_code(x, *, file=None)

   Imprime no arquivo *file* (ou "sys.stdout" caso *file* não seja
   especificado) informações detalhadas sobre o objeto de código
   correspondente à função, método, string de código-fonte fornecido.

   Este é um atalho conveniente para "print(code_info(x), file=file)",
   destinado à exploração interativa no prompt do interpretador.

   Adicionado na versão 3.2.

   Alterado na versão 3.4: Adicionado o parâmetro *file*.

dis.dis(x=None, *, file=None, depth=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)

   Desmonta o objeto *x*.  *x* pode denotar um módulo, uma classe, um
   método, uma função, um gerador, um gerador assíncrono, uma
   corrotina, um objeto de código, uma string de código-fonte ou uma
   sequência de bytes contendo bytecode bruto. Para um módulo, são
   desmontadas todas as funções. Para uma classe, são desmontados
   todos os métodos (incluindo métodos de classe e estáticos). Para um
   objeto de código ou sequência de bytecodes brutos, é impressa uma
   linha para cada instrução de bytecode. Além disso, objetos de
   código aninhados são desmontados recursivamente. Estes podem
   incluir expressões geradoras, funções aninhadas, corpos de classes
   aninhadas, e objetos de código usados para escopos de anotação.
   Strings são compiladas para objetos de código com a função embutida
   "compile()" antes de serem desmontadas.  Se nenhum objeto for
   fornecido, o último traceback é desmontado.

   O resultado é escrito como texto no arquivo *file* caso tenha sido
   fornecido como argumento, ou para "sys.stdout" caso contrário.

   A profundidade máxima de recursão é limitada por *depth* a menos
   que seja "None". "depth=0" significa não fazer recursão.

   Se *show_caches* for "True", essa função vai exibir entradas de
   cache em linha usadas pelo interpretador para especializar o
   bytecode.

   Se *adaptive* for "True", essa função vai exibir bytecode
   especializado que pode ser diferente do bytecode original.

   Alterado na versão 3.4: Adicionado o parâmetro *file*.

   Alterado na versão 3.7: Foi implementada a desmontagem recursiva, e
   adicionado o parâmetro *depth*.

   Alterado na versão 3.7: Este método agora lida com objetos de
   corrotina e de gerador assíncrono.

   Alterado na versão 3.11: Adicionados os parâmetros *show_caches* e
   *adaptive*.

   Alterado na versão 3.13: Foi adicionado o parâmetro *show_offsets*.

   Alterado na versão 3.14: Foi adicionado o parâmetro
   *show_positions*.

dis.distb(tb=None, *, file=None, show_caches=False, adaptive=False, show_offset=False, show_positions=False)

   Desmonta a função no topo da pilha de um traceback, usando o último
   traceback caso nenhum tenha sido passado.  A instrução que causou a
   exceção é indicada.

   O resultado é escrito como texto no arquivo *file* caso tenha sido
   fornecido como argumento, ou para "sys.stdout" caso contrário.

   Alterado na versão 3.4: Adicionado o parâmetro *file*.

   Alterado na versão 3.11: Adicionados os parâmetros *show_caches* e
   *adaptive*.

   Alterado na versão 3.13: Foi adicionado o parâmetro *show_offsets*.

   Alterado na versão 3.14: Foi adicionado o parâmetro
   *show_positions*.

dis.disassemble(code, lasti=-1, *, file=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)
dis.disco(code, lasti=-1, *, file=None, show_caches=False, adaptive=False, show_offsets=False, show_positions=False)

   Desmonta um objeto de código, indicando a última instrução se
   *lasti* tiver sido fornecido.  A saída é dividida em colunas da
   seguinte forma:

   1. a localização do código-fonte da instrução. Informações
      completas sobre a localização são exibidas se *show_positions*
      for verdadeiro. Caso contrário (o padrão), apenas o número da
      linha é exibido.

   2. a instrução atual, indicada por "-->",

   3. um rótulo da instrução, indicado com ">>",

   4. o endereço da instrução

   5. o nome do código da operação,

   6. os parâmetros da operação, e

   7. a interpretação dos parâmetros, em parênteses.

   A interpretação dos parâmetros reconhece nomes de variáveis locais
   e globais, valores de constantes, alvos de ramificações, e
   operadores de comparação.

   O resultado é escrito como texto no arquivo *file* caso tenha sido
   fornecido como argumento, ou para "sys.stdout" caso contrário.

   Alterado na versão 3.4: Adicionado o parâmetro *file*.

   Alterado na versão 3.11: Adicionados os parâmetros *show_caches* e
   *adaptive*.

   Alterado na versão 3.13: Foi adicionado o parâmetro *show_offsets*.

   Alterado na versão 3.14: Foi adicionado o parâmetro
   *show_positions*.

dis.get_instructions(x, *, first_line=None, show_caches=False, adaptive=False)

   Retorna um iterador sobre as instruções na função, método, string
   de código-fonte ou objeto de código fornecido.

   O iterador gera uma série de tuplas nomeadas "Instruction" contendo
   detalhes de cada operação no código fornecido.

   Se *first_line* não for "None", ele indica o número de linha que
   deve ser reportado para a primeira linha de código-fonte no código
   desmontado.  Caso contrário, a informação de linha de código-fonte
   (se houver) é extraída diretamente da desconstrução do objeto de
   código.

   The *adaptive* parameter works as it does in "dis()".

   Adicionado na versão 3.4.

   Alterado na versão 3.11: Adicionados os parâmetros *show_caches* e
   *adaptive*.

   Alterado na versão 3.13: O parâmetro *show_caches* foi
   descontinuado e não tem mais efeito. O iterador gera as instâncias
   da "Instruction" com o campo *cache_info* populado
   (independentemente do valor de *show_caches*) e não gera mais items
   separados para as entradas de cache.

dis.findlinestarts(code)

   Essa função geradora usa o método "co_lines()" do objeto de código
   *code* para encontrar as posições que correspondem aos inícios de
   cada linha do código-fonte.  Elas são geradas em pares "(offset,
   lineno)".

   Alterado na versão 3.6: Números de linhas podem ser decrescentes.
   Antes, eles eram sempre crescentes.

   Alterado na versão 3.10: The **PEP 626** "co_lines()" method is
   used instead of the "co_firstlineno" and "codeobject.co_lnotab"
   attributes of the code object.

   Alterado na versão 3.13: Números de linha podem ser "None" para
   bytecode que não corresponde a um código-fonte.

dis.findlabels(code)

   Detecta todas as posições na string de bytecode compilado bruto
   *code* que são alvos de pulos, e as retorna em uma lista.

dis.stack_effect(opcode, oparg=None, *, jump=None)

   Calcula o efeito que o *opcode* com argumento *oparg* tem na pilha.

   Se a operação tiver um alvo de pulo e *jump* for "True",
   "stack_effect()" vai retornar o efeito na pilha de realizar o pulo.
   Se *jump* for "False", ela vai retornar o efeito na pilha de não
   pular. E se *jump* for "None" (o padrão), vai retornar o efeito
   máximo na pilha dentre os dois casos.

   Adicionado na versão 3.4.

   Alterado na versão 3.8: Adicionado o parâmetro *jump*.

   Alterado na versão 3.13: Se "oparg" for omitido (ou "None"), agora
   é retornado o efeito na pilha para o caso "oparg=0". Anteriormente
   isso era um erro caso o opcode usasse o seu argumento. Além disso,
   agora não é mais um erro passar um inteiro como "oparg" quando o
   "opcode" não o usa; o "oparg" nesse caso é ignorado.


Instruções em bytecode do Python
================================

A função "get_instructions()" e a classe "Bytecode" fornecem detalhes
de instruções de bytecode como instâncias de "Instruction":

class dis.Instruction

   Detalhes de uma operação em bytecode

   opcode

      código numérico da operação, correspondendo aos valores dos
      opcodes listados abaixo e aos valores dos bytecodes nas Opcode
      collections.

   opname

      nome legível por humanos para a operação

   baseopcode

      código numérico para a operação base caso a operação seja
      especializada; caso contrário, igual ao "opcode"

   baseopname

      nome legível por humanos para a operação base caso a operação
      seja especializada; caso contrário, igual ao "opname"

   arg

      argumento numérico para a operação (se houver), caso contrário
      "None"

   oparg

      apelido para "arg"

   argval

      valor resolvido do argumento (se houver), caso contrário "None"

   argrepr

      descrição legível por humanos do argumento da operação (se
      houver), caso contrário uma string vazia.

   offset

      índice de início da operação dentro da sequência de bytecodes

   start_offset

      índice de início da operação dentro da sequência de bytecodes,
      incluindo as operações de "EXTENDED_ARG" prefixadas, caso
      presentes; caso contrário, igual a "offset"

   cache_offset

      índice de início das entradas de cache que seguem a operação

   end_offset

      índice de fim das entradas de cache que seguem a operação

   starts_line

      "True" se esse opcode inicia uma linha, "False" caso contrário

   line_number

      linha de código-fonte associada a esse opcode (se houver), senão
      "None"

   is_jump_target

      "True" se algum outro código pula para cá, senão "False"

   jump_target

      índice do bytecode que é alvo do pulo caso essa seja uma
      operação de pulo, caso contrário "None"

   positions

      objeto "dis.Positions" contendo os pontos de início e fim
      cobertos por esta instrução.

   cache_info

      Informações sobre as entradas de cache desta instrução, como
      tripletos do formato "(nome, tamanho, dados)", onde "nome" e
      "tamanho" descrevem o formato do cache e dados são o conteúdo do
      cache. "cache_info" é "None" se a instrução não tiver caches.

   Adicionado na versão 3.4.

   Alterado na versão 3.11: Adicionado o campo "positions".

   Alterado na versão 3.13: Alterado o campo "starts_line".Adicionados
   os campos "start_offset", "cache_offset", "end_offset",
   "baseopname", "baseopcode", "jump_target", "oparg", "line_number" e
   "cache_info".

class dis.Positions

   Caso a informação não esteja disponível, alguns campos podem ser
   "None".

   lineno

   end_lineno

   col_offset

   end_col_offset

   Adicionado na versão 3.11.

O compilador de Python atualmente gera as seguintes instruções de
bytecode.

**Instruções gerais**

A seguir, vamos usar "STACK" para nos referirmos à pilha do
interpretador, e vamos descrever operações nela como se ela fosse uma
lista do Python. Nessa linguagem, "STACK[-1]" é o topo da pilha.

NOP

   Código para não fazer nada.  Usado como espaço reservado pelo
   otimizador de bytecode, e para gerar eventos de rastreamento de
   linha.

NOT_TAKEN

   Código sem ação. Usado pelo interpretador para registrar os eventos
   "BRANCH_LEFT" e "BRANCH_RIGHT" para "sys.monitoring".

   Adicionado na versão 3.14.

POP_ITER

   Remove o iterador do topo da pilha.

   Adicionado na versão 3.14.

POP_TOP

   Remove o item no topo da pilha:

      STACK.pop()

END_FOR

   Remove o item no topo da pilha. Equivalente a "POP_TOP". Usado como
   limpeza ao final de laços, o que explica o nome.

   Adicionado na versão 3.12.

END_SEND

   Implementa "del STACK[-2]". Usado como limpeza quando um gerador
   termina.

   Adicionado na versão 3.12.

COPY(i)

   Coloca o i-ésimo item no topo da pilha sem removê-lo da sua posição
   original:

      assert i > 0
      STACK.append(STACK[-i])

   Adicionado na versão 3.11.

SWAP(i)

   Troca o topo da pilha de lugar com o i-ésimo elemento.

      STACK[-i], STACK[-1] = STACK[-1], STACK[-i]

   Adicionado na versão 3.11.

CACHE

   Ao invés de ser uma instrução de fato, este opcode é usado para
   demarcar espaço extra para o interpretador armazenar dados úteis
   diretamente no próprio bytecode. É escondido automaticamente por
   todas as utilidades do "dis", mas pode ser visualizado com
   "show_caches=True".

   Do ponto de vista lógico, este espaço faz parte da instrução
   anterior. Muitos opcodes esperam ser seguidos por um número exato
   de caches, e instruem o interpretador a pulá-los em tempo de
   execução.

   Caches populados podem se parecer com qualquer instrução, de forma
   que ler ou modificar bytecode adaptativo bruto contendo dados
   "quickened" requer muito cuidado.

   Adicionado na versão 3.11.

**Operações unárias**

Operações unárias tiram o topo da pilha, aplicam a operação, e põem o
resultado de volta na pilha.

UNARY_NEGATIVE

   Implementa "STACK[-1] = -STACK[-1]".

UNARY_NOT

   Implementa "STACK[-1] = not STACK[-1]".

   Alterado na versão 3.13: Essa instrução agora requer que o operando
   seja exatamente do tipo "bool".

UNARY_INVERT

   Implementa "STACK[-1] = ~STACK[-1]".

GET_ITER

   Implementa "STACK[-1] = iter(STACK[-1])".

GET_YIELD_FROM_ITER

   Se "STACK[-1]" for um *iterador gerador* ou um objeto *corrotina*,
   nada acontece.  Caso contrário, implementa "STACK[-1] =
   iter(STACK[-1])".

   Adicionado na versão 3.5.

TO_BOOL

   Implementa "STACK[-1] = bool(STACK[-1])".

   Adicionado na versão 3.13.

**Operações binárias e internas**

Operações binárias removem os dois itens no topo da pilha ("STACK[-1]"
e "STACK[-2]"). A operação é realizada, e o resultado é colocado de
volta na pilha.

As operações internas são como as operações binárias, só que a
operação é feita internamente caso suportado por "STACK[-2]", e o
"STACK[-1]" resultante pode ser (mas não necessariamente é) o
"STACK[-2]" original.

BINARY_OP(op)

   Implementa os operadores binários e locais (depende do valor de
   *op*):

      rhs = STACK.pop()
      lhs = STACK.pop()
      STACK.append(lhs op rhs)

   Adicionado na versão 3.11.

   Alterado na versão 3.14: Com oparg :"NB_SUBSCR", implementa
   subscrito binário (substitui o opcode "BINARY_SUBSCR")

STORE_SUBSCR

   Implementa:

      key = STACK.pop()
      container = STACK.pop()
      value = STACK.pop()
      container[key] = value

DELETE_SUBSCR

   Implementa:

      key = STACK.pop()
      container = STACK.pop()
      del container[key]

BINARY_SLICE

   Implementa:

      end = STACK.pop()
      start = STACK.pop()
      container = STACK.pop()
      STACK.append(container[start:end])

   Adicionado na versão 3.12.

STORE_SLICE

   Implementa:

      end = STACK.pop()
      start = STACK.pop()
      container = STACK.pop()
      value = STACK.pop()
      container[start:end] = value

   Adicionado na versão 3.12.

**Opcodes para corrotinas**

GET_AWAITABLE(where)

   Implementa "STACK[-1] = get_awaitable(STACK[-1])", onde
   "get_awaitable(o)" retorna "o" se "o" for um objeto de corrotina ou
   um gerador com o sinalizador "CO_ITERABLE_COROUTINE", ou então
   resolve "o.__await__".

      Se o operando "where" não for zero, ele indica onde a instrução
      ocorre:

      * "1": Após uma chamada a "__aenter__"

      * "2": Após uma chamada a "__aexit__"

   Adicionado na versão 3.5.

   Alterado na versão 3.11: Anteriormente, esta instrução não tinha um
   oparg.

GET_AITER

   Implementa "STACK[-1] = STACK[-1].__aiter__()".

   Adicionado na versão 3.5.

   Alterado na versão 3.7: Não é mais aceitado que o "__aiter__"
   retorne objetos aguardáveis.

GET_ANEXT

   Implementa "STACK.append(get_awaitable(STACK[-1].__anext__()))".
   Veja "GET_AWAITABLE" para o significado de "get_awaitable".

   Adicionado na versão 3.5.

END_ASYNC_FOR

   Termina um laço "async for".  Trata exceções levantadas ao aguardar
   um item seguinte. A pilha contém o iterável async em "STACK[-2]" e
   a exceção levantada em "STACK[-1]". Ambos são retirados. Se a
   exceção não for "StopAsyncIteration", ela é re-levantada.

   Adicionado na versão 3.8.

   Alterado na versão 3.11: A representação da exceção na pilha
   consiste agora de um item, ao invés de três.

CLEANUP_THROW

   Trata uma exceção levantada durante um chamada a "throw()" ou
   "close()" através do quadro atual.  Se "STACK[-1]" for uma
   instância de "StopIteration", remove três valores da pilha e põe de
   volta o seu membro "value".  Caso contrário, re-levanta
   "STACK[-1]".

   Adicionado na versão 3.12.

**Opcodes genéricos**

SET_ADD(i)

   Implementa:

      item = STACK.pop()
      set.add(STACK[-i], item)

   Usado para implementar compreensões de conjuntos.

LIST_APPEND(i)

   Implementa:

      item = STACK.pop()
      list.append(STACK[-i], item)

   Usado para implementar compreensões de lista.

MAP_ADD(i)

   Implementa:

      value = STACK.pop()
      key = STACK.pop()
      dict.__setitem__(STACK[-i], key, value)

   Usado para implementar compreensões de dicionário.

   Adicionado na versão 3.1.

   Alterado na versão 3.8: O valor do mapa é "STACK[-1]", e a sua
   chave, "STACK[-2]". Antes, eles estavam ao contrário.

Para as instruções "SET_ADD", "LIST_APPEND" e "MAP_ADD", o valor ou
par chave/valor é removido da pilha, mas o objeto de contêiner
continua na pilha para que ele esteja disponível para as iterações
seguintes do laço.

RETURN_VALUE

   Retorna "STACK[-1]" para quem chamou a função.

YIELD_VALUE

   Gera "STACK.pop()" a partir de um *gerador*.

   Alterado na versão 3.11: oparg definido como sendo a profundidade
   da pilha.

   Alterado na versão 3.12: oparg definido como sendo a profundidade
   do bloco exception, para o fechamento eficiente de geradores.

   Alterado na versão 3.13: oparg é "1" caso esta instrução seja parte
   de um yield-from ou await, e "0" caso contrário.

SETUP_ANNOTATIONS

   Verifica se "__annotations__" está definido em "locals()" e, se não
   estiver, é inicializado como um "dict" vazio. Este opcode é emitido
   somente se o corpo de uma classe ou módulo contém *anotações de
   variáveis* estaticamente.

   Adicionado na versão 3.6.

POP_EXCEPT

   Remove o valor no topo da pilha, o qual é usado para restaurar o
   estado de exceção.

   Alterado na versão 3.11: A representação da exceção na pilha
   consiste agora de um item, ao invés de três.

RERAISE

   Re-levanta a exceção que se encontra no topo da pilha. Se o oparg
   não for zero, remove um valor adicional do topo da pilha, o qual é
   atribuído ao "f_lasti" do quadro atual.

   Adicionado na versão 3.9.

   Alterado na versão 3.11: A representação da exceção na pilha
   consiste agora de um item, ao invés de três.

PUSH_EXC_INFO

   Remove um valor do topo da pilha. Põe a exceção atual no topo da
   pilha. Põe de volta no topo da pilha o valor que foi removido
   inicialmente. Usado em tratadores de exceções.

   Adicionado na versão 3.11.

CHECK_EXC_MATCH

   Verifica correspondências de exceções em "except". Testa de
   "STACK[-2]" é uma exceção que corresponde a "STACK[-1]". Remove
   "STACK[-1]" do topo da pilha, e põe no seu lugar o resultado
   booleano do teste.

   Adicionado na versão 3.11.

CHECK_EG_MATCH

   Verifica correspondências de exceções em "except*". Aplica
   "split(STACK[-1])" no grupo de exceções que representa "STACK[-2]".

   No caso de uma correspondência, remove dois itens do topo da pilha
   e põe nela o subgrupo que falhou a correspondência ("None" caso a
   correspondência tenha sido total), seguido pelo subgrupo que
   correspondeu. Quando não há correspondência nenhuma, remove um item
   (o tipo da correspondência) e põe "None" no seu lugar.

   Adicionado na versão 3.11.

WITH_EXCEPT_START

   Chama a função na posição 4 da pilha com argumentos (tipo, val, tb)
   representando a exceção no topo da pilha. Usado para implementar a
   chamada "context_manager.__exit__(*exc_info())" quando uma exceção
   ocorreu em uma instrução "with".

   Adicionado na versão 3.9.

   Alterado na versão 3.11: A função "__exit__" fica agora na posição
   4 pilha, ao invés da 7. A representação da exceção pilha consiste
   agora de um item, não três.

LOAD_COMMON_CONSTANT

   Envia uma constante comum para a pilha. O interpretador contém uma
   lista codificada de constantes suportadas por esta instrução. Usado
   pela instrução "assert" para carregar "AssertionError".

   Adicionado na versão 3.14.

LOAD_BUILD_CLASS

   Põe a função "builtins.__build_class__()" no topo da pilha.  Ela
   será chamada posteriormente para construir uma classe.

GET_LEN

   Executa "STACK.append(len(STACK[-1]))". Usado em instruções "match"
   onde a comparação com a estrutura do padrão é necessária.

   Adicionado na versão 3.10.

MATCH_MAPPING

   Se "STACK[-1]" for uma instância de "collections.abc.Mapping" (ou,
   de forma mais técnica: se tiver o sinalizador "Py_TPFLAGS_MAPPING"
   definido no seu "tp_flags"), põe "True" no topo da pilha. Caso
   contrário, põe "False".

   Adicionado na versão 3.10.

MATCH_SEQUENCE

   Se "STACK[-1]" for uma instância de "collections.abc.Sequence" e
   *não* for uma instância de "str"/"bytes"/"bytearray" (ou, de forma
   mais técnica: se tiver o sinalizador "Py_TPFLAGS_SEQUENCE" definido
   no seu "tp_flags"), põe "True" no topo da pilha. Caso contrário,
   põe "False".

   Adicionado na versão 3.10.

MATCH_KEYS

   "STACK[-1]" é uma tupla de chaves de um mapeamento, e "STACK[-2]" é
   o sujeito de uma correspondência. Se "STACK[-2]" contiver todas as
   chaves em "STACK[-1]", põe no topo da pilha um "tuple" contendo os
   valores correspondentes. Caso contrário, põe "None".

   Adicionado na versão 3.10.

   Alterado na versão 3.11: Anteriormente, essa instrução também
   colocava na pilha um valor booleano indicando sucesso ("True") ou
   falha ("False").

STORE_NAME(namei)

   Implementa "name = STACK.pop()". *namei* é o índice de *name* no
   atributo "co_names" do objeto de código. O compilador tenta usar
   "STORE_FAST" ou "STORE_GLOBAL" se possível.

DELETE_NAME(namei)

   Implementa "del name", onde *namei* é o índice no atributo
   "co_names" do objeto de código.

UNPACK_SEQUENCE(count)

   Desempacota "STACK[-1]" em *count* valores individuais, os quais
   são postos na pilha da direita para a esquerda. Requer que haja
   exatamente *count* valores:

      assert(len(STACK[-1]) == count)
      STACK.extend(STACK.pop()[:-count-1:-1])

UNPACK_EX(counts)

   Implementa atribuição com um alvo estrelado: desempacota o iterável
   "STACK[-1]" em valores individuais, sendo que pode haver menos
   valores do que itens no iterável: um dos novos valores será a lista
   de todos os itens que sobraram.

   A quantidade de valores antes e após o valor que será a lista é
   limitada a 255.

   A quantidade de valores antes do valor lista é passada no argumento
   do opcode. A quantidade de valores após a lista, se houver, é
   passada usando um "EXTENDED_ARG". A consequência é que o argumento
   pode ser visto como um valor de dois bytes, onde o byte "de baixo"
   de *counts* é a quantidade de valores antes do valor lista, e o
   byte "de cima" de *counts*, a quantidade após.

   Os valores extraídos são postos na pilha da direita para a
   esquerda, ou seja, após executar "a, *b, c = d" os valores serão
   armazenados como "STACK.extend((a, b, c))".

STORE_ATTR(namei)

   Implementa:

      obj = STACK.pop()
      value = STACK.pop()
      obj.name = value

   onde *namei* é o índice do nome no "co_names" do objeto de código.

DELETE_ATTR(namei)

   Implementa:

      obj = STACK.pop()
      del obj.name

   onde *namei* é o índice do nome no "co_names" do objeto de código.

STORE_GLOBAL(namei)

   Funciona como o "STORE_NAME", mas o nome é armazenado com um nome
   global.

DELETE_GLOBAL(namei)

   Funciona como o "DELETE_NAME", mas deleta um nome global.

LOAD_CONST(consti)

   Põe "co_consts[consti]" no topo da pilha.

LOAD_SMALL_INT(i)

   Coloca o inteiro "i" na pilha. "i" deve estar em "range(256)"

   Adicionado na versão 3.14.

LOAD_NAME(namei)

   Põe no topo da pilha o valor associado a "co_names[namei]". O nome
   é procurado nos locais, nos globais, e então nos embutidos.

LOAD_LOCALS

   Envia uma referência ao dicionário local para a pilha. Isso é usado
   para preparar dicionários de espaço de nomes para
   "LOAD_FROM_DICT_OR_DEREF" e "LOAD_FROM_DICT_OR_GLOBALS".

   Adicionado na versão 3.12.

LOAD_FROM_DICT_OR_GLOBALS(i)

   Extrai um mapeamento da pilha e procura o valor de
   "co_names[namei]". Se o nome não for encontrado, procura-o nas
   variáveis globais e, em seguida, nas variáveis embutidas,
   semelhante a "LOAD_GLOBAL". Isso é usado para carregar variáveis
   globais em escopos de anotação dentro dos corpos de classe.

   Adicionado na versão 3.12.

BUILD_TEMPLATE

   Constrói uma nova instância "Template" a partir de uma tupla de
   strings e uma tupla de interpolações e envia o objeto resultante
   para a pilha:

      interpolations = STACK.pop()
      strings = STACK.pop()
      STACK.append(_build_template(strings, interpolations))

   Adicionado na versão 3.14.

BUILD_INTERPOLATION(format)

   Constrói uma nova instância "Interpolation" a partir de um valor e
   sua expressão de origem e envia o objeto resultante para a pilha.

   Se nenhuma especificação de conversão ou formato estiver presente,
   "format" será definido como "2".

   If the low bit of "format" is set, it indicates that the
   interpolation contains a format specification.

   If "format >> 2" is non-zero, it indicates that the interpolation
   contains a conversion. The value of "format >> 2" is the conversion
   type ("0" for no conversion, "1" for "!s", "2" for "!r", and "3"
   for "!a"):

      conversion = format >> 2
      if format & 1:
          format_spec = STACK.pop()
      else:
          format_spec = None
      expression = STACK.pop()
      value = STACK.pop()
      STACK.append(_build_interpolation(value, expression, conversion, format_spec))

   Adicionado na versão 3.14.

BUILD_TUPLE(count)

   Creates a tuple consuming *count* items from the stack, and pushes
   the resulting tuple onto the stack:

      if count == 0:
          value = ()
      else:
          value = tuple(STACK[-count:])
          STACK = STACK[:-count]

      STACK.append(value)

BUILD_LIST(count)

   Works as "BUILD_TUPLE", but creates a list.

BUILD_SET(count)

   Works as "BUILD_TUPLE", but creates a set.

BUILD_MAP(count)

   Pushes a new dictionary object onto the stack.  Pops "2 * count"
   items so that the dictionary holds *count* entries: "{...,
   STACK[-4]: STACK[-3], STACK[-2]: STACK[-1]}".

   Alterado na versão 3.5: The dictionary is created from stack items
   instead of creating an empty dictionary pre-sized to hold *count*
   items.

BUILD_STRING(count)

   Concatenates *count* strings from the stack and pushes the
   resulting string onto the stack.

   Adicionado na versão 3.6.

LIST_EXTEND(i)

   Implementa:

      seq = STACK.pop()
      list.extend(STACK[-i], seq)

   Used to build lists.

   Adicionado na versão 3.9.

SET_UPDATE(i)

   Implementa:

      seq = STACK.pop()
      set.update(STACK[-i], seq)

   Used to build sets.

   Adicionado na versão 3.9.

DICT_UPDATE(i)

   Implementa:

      map = STACK.pop()
      dict.update(STACK[-i], map)

   Used to build dicts.

   Adicionado na versão 3.9.

DICT_MERGE(i)

   Like "DICT_UPDATE" but raises an exception for duplicate keys.

   Adicionado na versão 3.9.

LOAD_ATTR(namei)

   If the low bit of "namei" is not set, this replaces "STACK[-1]"
   with "getattr(STACK[-1], co_names[namei>>1])".

   If the low bit of "namei" is set, this will attempt to load a
   method named "co_names[namei>>1]" from the "STACK[-1]" object.
   "STACK[-1]" is popped. This bytecode distinguishes two cases: if
   "STACK[-1]" has a method with the correct name, the bytecode pushes
   the unbound method and "STACK[-1]". "STACK[-1]" will be used as the
   first argument ("self") by "CALL" or "CALL_KW" when calling the
   unbound method. Otherwise, "NULL" and the object returned by the
   attribute lookup are pushed.

   Alterado na versão 3.12: If the low bit of "namei" is set, then a
   "NULL" or "self" is pushed to the stack before the attribute or
   unbound method respectively.

LOAD_SUPER_ATTR(namei)

   This opcode implements "super()", both in its zero-argument and
   two-argument forms (e.g. "super().method()", "super().attr" and
   "super(cls, self).method()", "super(cls, self).attr").

   It pops three values from the stack (from top of stack down):

   * "self": the first argument to the current method

   * "cls": the class within which the current method was defined

   * the global "super"

   With respect to its argument, it works similarly to "LOAD_ATTR",
   except that "namei" is shifted left by 2 bits instead of 1.

   The low bit of "namei" signals to attempt a method load, as with
   "LOAD_ATTR", which results in pushing "NULL" and the loaded method.
   When it is unset a single value is pushed to the stack.

   The second-low bit of "namei", if set, means that this was a two-
   argument call to "super()" (unset means zero-argument).

   Adicionado na versão 3.12.

COMPARE_OP(opname)

   Performs a Boolean operation.  The operation name can be found in
   "cmp_op[opname >> 5]". If the fifth-lowest bit of "opname" is set
   ("opname & 16"), the result should be coerced to "bool".

   Alterado na versão 3.13: The fifth-lowest bit of the oparg now
   indicates a forced conversion to "bool".

IS_OP(invert)

   Performs "is" comparison, or "is not" if "invert" is 1.

   Adicionado na versão 3.9.

CONTAINS_OP(invert)

   Performs "in" comparison, or "not in" if "invert" is 1.

   Adicionado na versão 3.9.

IMPORT_NAME(namei)

   Imports the module "co_names[namei]".  "STACK[-1]" and "STACK[-2]"
   are popped and provide the *fromlist* and *level* arguments of
   "__import__()". The module object is pushed onto the stack.  The
   current namespace is not affected: for a proper import statement, a
   subsequent "STORE_FAST" instruction modifies the namespace.

IMPORT_FROM(namei)

   Loads the attribute "co_names[namei]" from the module found in
   "STACK[-1]". The resulting object is pushed onto the stack, to be
   subsequently stored by a "STORE_FAST" instruction.

JUMP_FORWARD(delta)

   Increments bytecode counter by *delta*.

JUMP_BACKWARD(delta)

   Decrements bytecode counter by *delta*. Checks for interrupts.

   Adicionado na versão 3.11.

JUMP_BACKWARD_NO_INTERRUPT(delta)

   Decrements bytecode counter by *delta*. Does not check for
   interrupts.

   Adicionado na versão 3.11.

POP_JUMP_IF_TRUE(delta)

   If "STACK[-1]" is true, increments the bytecode counter by *delta*.
   "STACK[-1]" is popped.

   Alterado na versão 3.11: The oparg is now a relative delta rather
   than an absolute target. This opcode is a pseudo-instruction,
   replaced in final bytecode by the directed versions
   (forward/backward).

   Alterado na versão 3.12: This is no longer a pseudo-instruction.

   Alterado na versão 3.13: Essa instrução agora requer que o operando
   seja exatamente do tipo "bool".

POP_JUMP_IF_FALSE(delta)

   If "STACK[-1]" is false, increments the bytecode counter by
   *delta*. "STACK[-1]" is popped.

   Alterado na versão 3.11: The oparg is now a relative delta rather
   than an absolute target. This opcode is a pseudo-instruction,
   replaced in final bytecode by the directed versions
   (forward/backward).

   Alterado na versão 3.12: This is no longer a pseudo-instruction.

   Alterado na versão 3.13: Essa instrução agora requer que o operando
   seja exatamente do tipo "bool".

POP_JUMP_IF_NOT_NONE(delta)

   If "STACK[-1]" is not "None", increments the bytecode counter by
   *delta*. "STACK[-1]" is popped.

   Adicionado na versão 3.11.

   Alterado na versão 3.12: This is no longer a pseudo-instruction.

POP_JUMP_IF_NONE(delta)

   If "STACK[-1]" is "None", increments the bytecode counter by
   *delta*. "STACK[-1]" is popped.

   Adicionado na versão 3.11.

   Alterado na versão 3.12: This is no longer a pseudo-instruction.

FOR_ITER(delta)

   "STACK[-1]" is an *iterator*.  Call its "__next__()" method. If
   this yields a new value, push it on the stack (leaving the iterator
   below it).  If the iterator indicates it is *exhausted* then the
   byte code counter is incremented by *delta*.

   Alterado na versão 3.12: Up until 3.11 the iterator was popped when
   it was exhausted.

LOAD_GLOBAL(namei)

   Loads the global named "co_names[namei>>1]" onto the stack. If the
   low bit of "namei" is set, a "NULL" is pushed onto the stack after
   the global variable.

   Alterado na versão 3.11: The low bit of "namei" indicates whether a
   "NULL" is pushed.

   Alterado na versão 3.13: The "NULL" is pushed after the global
   variable, rather than before it.

LOAD_FAST(var_num)

   Pushes a reference to the local "co_varnames[var_num]" onto the
   stack.

   Alterado na versão 3.12: This opcode is now only used in situations
   where the local variable is guaranteed to be initialized. It cannot
   raise "UnboundLocalError".

LOAD_FAST_BORROW(var_num)

   Pushes a borrowed reference to the local "co_varnames[var_num]"
   onto the stack.

   Adicionado na versão 3.14.

LOAD_FAST_LOAD_FAST(var_nums)

   Pushes references to "co_varnames[var_nums >> 4]" and
   "co_varnames[var_nums & 15]" onto the stack.

   Adicionado na versão 3.13.

LOAD_FAST_BORROW_LOAD_FAST_BORROW(var_nums)

   Pushes borrowed references to "co_varnames[var_nums >> 4]" and
   "co_varnames[var_nums & 15]" onto the stack.

   Adicionado na versão 3.14.

LOAD_FAST_CHECK(var_num)

   Pushes a reference to the local "co_varnames[var_num]" onto the
   stack, raising an "UnboundLocalError" if the local variable has not
   been initialized.

   Adicionado na versão 3.12.

LOAD_FAST_AND_CLEAR(var_num)

   Pushes a reference to the local "co_varnames[var_num]" onto the
   stack (or pushes "NULL" onto the stack if the local variable has
   not been initialized) and sets "co_varnames[var_num]" to "NULL".

   Adicionado na versão 3.12.

STORE_FAST(var_num)

   Stores "STACK.pop()" into the local "co_varnames[var_num]".

STORE_FAST_STORE_FAST(var_nums)

   Stores "STACK[-1]" into "co_varnames[var_nums >> 4]" and
   "STACK[-2]" into "co_varnames[var_nums & 15]".

   Adicionado na versão 3.13.

STORE_FAST_LOAD_FAST(var_nums)

   Stores "STACK.pop()" into the local "co_varnames[var_nums >> 4]"
   and pushes a reference to the local "co_varnames[var_nums & 15]"
   onto the stack.

   Adicionado na versão 3.13.

DELETE_FAST(var_num)

   Deletes local "co_varnames[var_num]".

MAKE_CELL(i)

   Creates a new cell in slot "i".  If that slot is nonempty then that
   value is stored into the new cell.

   Adicionado na versão 3.11.

LOAD_DEREF(i)

   Loads the cell contained in slot "i" of the "fast locals" storage.
   Pushes a reference to the object the cell contains on the stack.

   Alterado na versão 3.11: "i" is no longer offset by the length of
   "co_varnames".

LOAD_FROM_DICT_OR_DEREF(i)

   Pops a mapping off the stack and looks up the name associated with
   slot "i" of the "fast locals" storage in this mapping. If the name
   is not found there, loads it from the cell contained in slot "i",
   similar to "LOAD_DEREF". This is used for loading *closure
   variables* in class bodies (which previously used
   "LOAD_CLASSDEREF") and in annotation scopes within class bodies.

   Adicionado na versão 3.12.

STORE_DEREF(i)

   Stores "STACK.pop()" into the cell contained in slot "i" of the
   "fast locals" storage.

   Alterado na versão 3.11: "i" is no longer offset by the length of
   "co_varnames".

DELETE_DEREF(i)

   Empties the cell contained in slot "i" of the "fast locals"
   storage. Used by the "del" statement.

   Adicionado na versão 3.2.

   Alterado na versão 3.11: "i" is no longer offset by the length of
   "co_varnames".

COPY_FREE_VARS(n)

   Copia as "n" *variáveis livres (de clausura)* do fechamento para o
   quadro. Remove a necessidade de código especial do lado do chamador
   ao chamar closures.

   Adicionado na versão 3.11.

RAISE_VARARGS(argc)

   Raises an exception using one of the 3 forms of the "raise"
   statement, depending on the value of *argc*:

   * 0: "raise" (re-raise previous exception)

   * 1: "raise STACK[-1]" (raise exception instance or type at
     "STACK[-1]")

   * 2: "raise STACK[-2] from STACK[-1]" (raise exception instance or
     type at "STACK[-2]" with "__cause__" set to "STACK[-1]")

CALL(argc)

   Calls a callable object with the number of arguments specified by
   "argc". On the stack are (in ascending order):

   * The callable

   * "self" or "NULL"

   * The remaining positional arguments

   "argc" is the total of the positional arguments, excluding "self".

   "CALL" pops all arguments and the callable object off the stack,
   calls the callable object with those arguments, and pushes the
   return value returned by the callable object.

   Adicionado na versão 3.11.

   Alterado na versão 3.13: The callable now always appears at the
   same position on the stack.

   Alterado na versão 3.13: Calls with keyword arguments are now
   handled by "CALL_KW".

CALL_KW(argc)

   Calls a callable object with the number of arguments specified by
   "argc", including one or more named arguments. On the stack are (in
   ascending order):

   * The callable

   * "self" or "NULL"

   * The remaining positional arguments

   * The named arguments

   * A "tuple" of keyword argument names

   "argc" is the total of the positional and named arguments,
   excluding "self". The length of the tuple of keyword argument names
   is the number of named arguments.

   "CALL_KW" pops all arguments, the keyword names, and the callable
   object off the stack, calls the callable object with those
   arguments, and pushes the return value returned by the callable
   object.

   Adicionado na versão 3.13.

CALL_FUNCTION_EX(flags)

   Calls a callable object with variable set of positional and keyword
   arguments.  If the lowest bit of *flags* is set, the top of the
   stack contains a mapping object containing additional keyword
   arguments. Before the callable is called, the mapping object and
   iterable object are each "unpacked" and their contents passed in as
   keyword and positional arguments respectively. "CALL_FUNCTION_EX"
   pops all arguments and the callable object off the stack, calls the
   callable object with those arguments, and pushes the return value
   returned by the callable object.

   Adicionado na versão 3.6.

PUSH_NULL

   Pushes a "NULL" to the stack. Used in the call sequence to match
   the "NULL" pushed by "LOAD_ATTR" for non-method calls.

   Adicionado na versão 3.11.

MAKE_FUNCTION

   Pushes a new function object on the stack built from the code
   object at "STACK[-1]".

   Alterado na versão 3.10: Flag value "0x04" is a tuple of strings
   instead of dictionary

   Alterado na versão 3.11: Qualified name at "STACK[-1]" was removed.

   Alterado na versão 3.13: Extra function attributes on the stack,
   signaled by oparg flags, were removed. They now use
   "SET_FUNCTION_ATTRIBUTE".

SET_FUNCTION_ATTRIBUTE(flag)

   Sets an attribute on a function object. Expects the function at
   "STACK[-1]" and the attribute value to set at "STACK[-2]"; consumes
   both and leaves the function at "STACK[-1]". The flag determines
   which attribute to set:

   * "0x01" a tuple of default values for positional-only and
     positional-or-keyword parameters in positional order

   * "0x02" a dictionary of keyword-only parameters' default values

   * "0x04" a tuple of strings containing parameters' annotations

   * "0x08" a tuple containing cells for free variables, making a
     closure

   * "0x10" the *annotate function* for the function object

   Adicionado na versão 3.13.

   Alterado na versão 3.14: Added "0x10" to indicate the annotate
   function for the function object.

BUILD_SLICE(argc)

   Pushes a slice object on the stack.  *argc* must be 2 or 3.  If it
   is 2, implements:

      end = STACK.pop()
      start = STACK.pop()
      STACK.append(slice(start, end))

   if it is 3, implements:

      step = STACK.pop()
      end = STACK.pop()
      start = STACK.pop()
      STACK.append(slice(start, end, step))

   See the "slice()" built-in function for more information.

EXTENDED_ARG(ext)

   Prefixes any opcode which has an argument too big to fit into the
   default one byte. *ext* holds an additional byte which act as
   higher bits in the argument. For each opcode, at most three
   prefixal "EXTENDED_ARG" are allowed, forming an argument from two-
   byte to four-byte.

CONVERT_VALUE(oparg)

   Convert value to a string, depending on "oparg":

      value = STACK.pop()
      result = func(value)
      STACK.append(result)

   * "oparg == 1": call "str()" on *value*

   * "oparg == 2": call "repr()" on *value*

   * "oparg == 3": call "ascii()" on *value*

   Used for implementing formatted string literals (f-strings).

   Adicionado na versão 3.13.

FORMAT_SIMPLE

   Formats the value on top of stack:

      value = STACK.pop()
      result = value.__format__("")
      STACK.append(result)

   Used for implementing formatted string literals (f-strings).

   Adicionado na versão 3.13.

FORMAT_WITH_SPEC

   Formats the given value with the given format spec:

      spec = STACK.pop()
      value = STACK.pop()
      result = value.__format__(spec)
      STACK.append(result)

   Used for implementing formatted string literals (f-strings).

   Adicionado na versão 3.13.

MATCH_CLASS(count)

   "STACK[-1]" is a tuple of keyword attribute names, "STACK[-2]" is
   the class being matched against, and "STACK[-3]" is the match
   subject.  *count* is the number of positional sub-patterns.

   Pop "STACK[-1]", "STACK[-2]", and "STACK[-3]". If "STACK[-3]" is an
   instance of "STACK[-2]" and has the positional and keyword
   attributes required by *count* and "STACK[-1]", push a tuple of
   extracted attributes. Otherwise, push "None".

   Adicionado na versão 3.10.

   Alterado na versão 3.11: Anteriormente, essa instrução também
   colocava na pilha um valor booleano indicando sucesso ("True") ou
   falha ("False").

RESUME(context)

   A no-op. Performs internal tracing, debugging and optimization
   checks.

   The "context" operand consists of two parts. The lowest two bits
   indicate where the "RESUME" occurs:

   * "0" The start of a function, which is neither a generator,
     coroutine nor an async generator

   * "1" Depois de uma expressão "yield"

   * "2" After a "yield from" expression

   * "3" Depois de uma expressão "await"

   The next bit is "1" if the RESUME is at except-depth "1", and "0"
   otherwise.

   Adicionado na versão 3.11.

   Alterado na versão 3.13: The oparg value changed to include
   information about except-depth

RETURN_GENERATOR

   Create a generator, coroutine, or async generator from the current
   frame. Used as first opcode of in code object for the above
   mentioned callables. Clear the current frame and return the newly
   created generator.

   Adicionado na versão 3.11.

SEND(delta)

   Equivalent to "STACK[-1] = STACK[-2].send(STACK[-1])". Used in
   "yield from" and "await" statements.

   If the call raises "StopIteration", pop the top value from the
   stack, push the exception's "value" attribute, and increment the
   bytecode counter by *delta*.

   Adicionado na versão 3.11.

HAVE_ARGUMENT

   This is not really an opcode.  It identifies the dividing line
   between opcodes in the range [0,255] which don't use their argument
   and those that do ("< HAVE_ARGUMENT" and ">= HAVE_ARGUMENT",
   respectively).

   If your application uses pseudo instructions or specialized
   instructions, use the "hasarg" collection instead.

   Alterado na versão 3.6: Now every instruction has an argument, but
   opcodes "< HAVE_ARGUMENT" ignore it. Before, only opcodes ">=
   HAVE_ARGUMENT" had an argument.

   Alterado na versão 3.12: Pseudo instructions were added to the
   "dis" module, and for them it is not true that comparison with
   "HAVE_ARGUMENT" indicates whether they use their arg.

   Descontinuado desde a versão 3.13: Use "hasarg" instead.

CALL_INTRINSIC_1

   Calls an intrinsic function with one argument. Passes "STACK[-1]"
   as the argument and sets "STACK[-1]" to the result. Used to
   implement functionality that is not performance critical.

   The operand determines which intrinsic function is called:

   +-------------------------------------+-------------------------------------+
   | Operand                             | Descrição                           |
   |=====================================|=====================================|
   | "INTRINSIC_1_INVALID"               | Not valid                           |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_PRINT"                   | Prints the argument to standard     |
   |                                     | out. Used in the REPL.              |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_IMPORT_STAR"             | Performs "import *" for the named   |
   |                                     | module.                             |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_STOPITERATION_ERROR"     | Extracts the return value from a    |
   |                                     | "StopIteration" exception.          |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_ASYNC_GEN_WRAP"          | Wraps an async generator value      |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_UNARY_POSITIVE"          | Performs the unary "+" operation    |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_LIST_TO_TUPLE"           | Converts a list to a tuple          |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEVAR"                 | Cria um "typing.TypeVar"            |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_PARAMSPEC"               | Cria um "typing.ParamSpec"          |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEVARTUPLE"            | Cria um "typing.TypeVarTuple"       |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_SUBSCRIPT_GENERIC"       | Returns "typing.Generic"            |
   |                                     | subscripted with the argument       |
   +-------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEALIAS"               | Creates a "typing.TypeAliasType";   |
   |                                     | used in the "type" statement. The   |
   |                                     | argument is a tuple of the type     |
   |                                     | alias's name, type parameters, and  |
   |                                     | value.                              |
   +-------------------------------------+-------------------------------------+

   Adicionado na versão 3.12.

CALL_INTRINSIC_2

   Calls an intrinsic function with two arguments. Used to implement
   functionality that is not performance critical:

      arg2 = STACK.pop()
      arg1 = STACK.pop()
      result = intrinsic2(arg1, arg2)
      STACK.append(result)

   The operand determines which intrinsic function is called:

   +------------------------------------------+-------------------------------------+
   | Operand                                  | Descrição                           |
   |==========================================|=====================================|
   | "INTRINSIC_2_INVALID"                    | Not valid                           |
   +------------------------------------------+-------------------------------------+
   | "INTRINSIC_PREP_RERAISE_STAR"            | Calculates the "ExceptionGroup" to  |
   |                                          | raise from a "try-except*".         |
   +------------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEVAR_WITH_BOUND"           | Creates a "typing.TypeVar" with a   |
   |                                          | bound.                              |
   +------------------------------------------+-------------------------------------+
   | "INTRINSIC_TYPEVAR_WITH_CONSTRAINTS"     | Creates a "typing.TypeVar" with     |
   |                                          | constraints.                        |
   +------------------------------------------+-------------------------------------+
   | "INTRINSIC_SET_FUNCTION_TYPE_PARAMS"     | Sets the "__type_params__"          |
   |                                          | attribute of a function.            |
   +------------------------------------------+-------------------------------------+

   Adicionado na versão 3.12.

LOAD_SPECIAL

   Performs special method lookup on "STACK[-1]". If
   "type(STACK[-1]).__xxx__" is a method, leave
   "type(STACK[-1]).__xxx__; STACK[-1]" on the stack. If
   "type(STACK[-1]).__xxx__" is not a method, leave
   "STACK[-1].__xxx__; NULL" on the stack.

   Adicionado na versão 3.14.

**Pseudo-instructions**

These opcodes do not appear in Python bytecode. They are used by the
compiler but are replaced by real opcodes or removed before bytecode
is generated.

SETUP_FINALLY(target)

   Set up an exception handler for the following code block. If an
   exception occurs, the value stack level is restored to its current
   state and control is transferred to the exception handler at
   "target".

SETUP_CLEANUP(target)

   Like "SETUP_FINALLY", but in case of an exception also pushes the
   last instruction ("lasti") to the stack so that "RERAISE" can
   restore it. If an exception occurs, the value stack level and the
   last instruction on the frame are restored to their current state,
   and control is transferred to the exception handler at "target".

SETUP_WITH(target)

   Like "SETUP_CLEANUP", but in case of an exception one more item is
   popped from the stack before control is transferred to the
   exception handler at "target".

   This variant is used in "with" and "async with" constructs, which
   push the return value of the context manager's "__enter__()" or
   "__aenter__()" to the stack.

POP_BLOCK

   Marks the end of the code block associated with the last
   "SETUP_FINALLY", "SETUP_CLEANUP" or "SETUP_WITH".

JUMP
JUMP_NO_INTERRUPT

   Undirected relative jump instructions which are replaced by their
   directed (forward/backward) counterparts by the assembler.

JUMP_IF_TRUE
JUMP_IF_FALSE

   Conditional jumps which do not impact the stack. Replaced by the
   sequence "COPY 1", "TO_BOOL", "POP_JUMP_IF_TRUE/FALSE".

LOAD_CLOSURE(i)

   Pushes a reference to the cell contained in slot "i" of the "fast
   locals" storage.

   Note that "LOAD_CLOSURE" is replaced with "LOAD_FAST" in the
   assembler.

   Alterado na versão 3.13: This opcode is now a pseudo-instruction.


Opcode collections
==================

These collections are provided for automatic introspection of bytecode
instructions:

Alterado na versão 3.12: The collections now contain pseudo
instructions and instrumented instructions as well. These are opcodes
with values ">= MIN_PSEUDO_OPCODE" and ">= MIN_INSTRUMENTED_OPCODE".

dis.opname

   Sequence of operation names, indexable using the bytecode.

dis.opmap

   Dictionary mapping operation names to bytecodes.

dis.cmp_op

   Sequence of all compare operation names.

dis.hasarg

   Sequence of bytecodes that use their argument.

   Adicionado na versão 3.12.

dis.hasconst

   Sequence of bytecodes that access a constant.

dis.hasfree

   Sequence of bytecodes that access a *free (closure) variable*.
   'free' in this context refers to names in the current scope that
   are referenced by inner scopes or names in outer scopes that are
   referenced from this scope.  It does *not* include references to
   global or builtin scopes.

dis.hasname

   Sequence of bytecodes that access an attribute by name.

dis.hasjump

   Sequence of bytecodes that have a jump target. All jumps are
   relative.

   Adicionado na versão 3.13.

dis.haslocal

   Sequence of bytecodes that access a local variable.

dis.hascompare

   Sequence of bytecodes of Boolean operations.

dis.hasexc

   Sequence of bytecodes that set an exception handler.

   Adicionado na versão 3.12.

dis.hasjrel

   Sequence of bytecodes that have a relative jump target.

   Descontinuado desde a versão 3.13: All jumps are now relative. Use
   "hasjump".

dis.hasjabs

   Sequence of bytecodes that have an absolute jump target.

   Descontinuado desde a versão 3.13: All jumps are now relative. This
   list is empty.
