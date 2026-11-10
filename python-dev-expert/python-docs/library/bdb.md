"bdb" --- Framework do depurador
********************************

**Código-fonte:** Lib/bdb.py

======================================================================

The "bdb" module handles basic debugger functions, like setting
breakpoints or managing execution via the debugger.

A seguinte exceção é definida:

exception bdb.BdbQuit

   Exceção levantada pela classe "Bdb" para sair do depurador.

The "bdb" module also defines two classes:

class bdb.Breakpoint(self, file, line, temporary=False, cond=None, funcname=None)

   Esta classe implementa pontos de interrupção temporários, contagens
   de ignorar, desativação e (re)ativação, além de condicionais.

   Os pontos de interrupção são indexados por número por meio de uma
   lista chamada "bpbynumber" e por pares "(file, line)" por meio de
   "bplist". O primeiro aponta para uma única instância da classe
   "Breakpoint". O segundo aponta para uma lista dessas instâncias, já
   que pode haver mais de um ponto de interrupção por linha.

   Ao criar um ponto de interrupção, seu "nome do arquivo" associado
   deve estar no formato canônico. Se um "funcname" for definido, um
   ponto de interrupção "atingido" será contado quando a primeira
   linha dessa função for executada. Um ponto de interrupção
   "condicional" sempre conta um "atingido".

   As instâncias de "Breakpoint" têm os seguintes métodos:

   deleteMe()

      Exclui o ponto de interrupção da lista associada a um
      arquivo/linha.  Se for o último ponto de interrupção nessa
      posição, ele também excluirá a entrada do arquivo/linha.

   enable()

      Marca o ponto de interrupção como ativado.

   disable()

      Marca o ponto de interrupção como desativado.

   bpformat()

      Retorna uma string com todas as informações sobre o ponto de
      interrupção, formatadas de maneira clara:

      * Número do ponto de interrupção.

      * Status temporário (del ou keep).

      * Posição do arquivo/linha.

      * Condição de interrupção.

      * Número de vezes para ignorar.

      * Número de vezes atingido.

      Adicionado na versão 3.2.

   bpprint(out=None)

      Exibe a saída de "bpformat()" no arquivo *out* ou, se for
      "None", na saída padrão.

   Instâncias "Breakpoint" possuem os seguintes atributos:

   file

      Nome do arquivo do "Breakpoint".

   line

      Número da linha do "Breakpoint" dentro de "file".

   temporary

      "True" se um "Breakpoint" em (file, line) for temporário.

   cond

      Condição para avaliar um "Breakpoint" em (file, line).

   funcname

      Nome da função que define se um "Breakpoint" é atingido ao
      entrar na função.

   enabled

      "True" se "Breakpoint" estiver ativado.

   bpbynumber

      Índice numérico de uma única instância de "Breakpoint".

   bplist

      Dicionário de instâncias de "Breakpoint" indexadas por tuplas
      ("file", "line").

   ignore

      Número de vezes para ignorar o "Breakpoint".

   hits

      Contagem do número de vezes que um "Breakpoint" foi atingido.

class bdb.Bdb(skip=None, backend='settrace')

   A "Bdb" atua como uma classe base genérica de depurador em Python.

   Esta classe cuida dos detalhes do mecanismo de rastreamento; uma
   classe derivada deve implementar a interação com o usuário. A
   classe de depuração padrão ("pdb.Pdb") é um exemplo.

   O argumento *skip*, se fornecido, deve ser um iterável de padrões
   de nomes de módulos no estilo glob. O depurador não entrará em
   frames que se originam em um módulo que corresponda a um desses
   padrões. Se um frame é considerado como originado em determinado
   módulo é determinado pelo valor de "__name__" nos globals do frame.

   O argumento *backend* especifica o backend a ser usado pela "Bdb".
   Ele pode ser "'settrace'" ou "'monitoring'". "'settrace'" usa
   "sys.settrace()", que oferece a melhor retrocompatibilidade. O
   backend "'monitoring'" usa o novo "sys.monitoring", introduzido no
   Python 3.12, que pode ser muito mais eficiente porque pode
   desabilitar eventos não utilizados. Estamos tentando manter
   interfaces idênticas para ambos os backends, mas existem algumas
   diferenças. Os desenvolvedores de depuradores são incentivados a
   usar o backend "'monitoring'" para obter melhor desempenho.

   Alterado na versão 3.1: Adicionado o parâmetro *skip*.

   Alterado na versão 3.14: Adicionado o parâmetro *backend*.

   Os seguintes métodos de "Bdb" normalmente não precisam ser
   substituídos.

   canonic(filename)

      Retorna a forma canônica de *filename*.

      Para nomes de arquivos reais, a forma canônica é um "caminho
      absoluto", "normalizado para distinguir maiúsculas e
      minúsculas", dependente do sistema operacional. Um *filename*
      com colchetes angulares, como ""<stdin>"" gerado no modo
      interativo, é retornado sem alterações.

   start_trace(self)

      Inicia o rastreamento. Para o backend "'settrace'", este método
      equivale a "sys.settrace(self.trace_dispatch)"

      Adicionado na versão 3.14.

   stop_trace(self)

      Para o rastreamento. Para o backend "'settrace'", este método
      equivale a "sys.settrace(None)"

      Adicionado na versão 3.14.

   reset()

      Define os atributos "botframe", "stopframe", "returnframe" e
      "quitting" com valores prontos para iniciar a depuração.

   trace_dispatch(frame, event, arg)

      Esta função é instalada como a função de rastreamento dos frames
      depurados. Seu valor de retorno é a nova função de rastreamento
      (na maioria dos casos, ela própria).

      A implementação padrão decide como despachar um frame,
      dependendo do tipo de evento (passado como string) que está
      prestes a ser executado. *event* pode ser um dos seguintes:

      * ""line"": Uma nova linha de código será executada.

      * ""call"": Um função está prestes a ser chamada, ou outro bloco
        de código foi inserido.

      * ""retorno"": Um função ou outro bloco de código está prestes a
        retornar.

      * ""exception"": Ocorreu uma exceção.

      For all the events, specialized functions (see below) are
      called.

      O parâmetro *arg* depende do evento anterior.

      Consulte a documentação de "sys.settrace()" para mais
      informações sobre a função de rastreamento. Para mais
      informações sobre objetos de código e de frame, consulte A
      hierarquia de tipos padrão.

   dispatch_line(frame)

      Se o depurador deve parar na linha atual, invoca o método
      "user_line()" (que deve ser substituído em subclasses). Levanta
      a exceção "BdbQuit" se o sinalizador "quitting" estiver definido
      (ele pode ser definido a partir de "user_line()"). Retorna uma
      referência ao método "trace_dispatch()" para continuar o
      rastreamento nesse escopo.

   dispatch_call(frame, arg)

      Se o depurador deve parar nesta chamada de função, invoca o
      método "user_call()" (que deve ser substituído em subclasses).
      Levanta a exceção "BdbQuit" se o sinalizador "quitting" estiver
      definido (ele pode ser definido a partir de "user_call()").
      Retorna uma referência ao método "trace_dispatch()" para
      continuar o rastreamento nesse escopo.

   dispatch_return(frame, arg)

      Se o depurador deve parar no retorno desta função, invoca o
      método "user_return()" (que deve ser substituído em subclasses).
      Levanta a exceção "BdbQuit" se o sinalizador "quitting" estiver
      definido (ele pode ser definido a partir de "user_return()").
      Retorna uma referência ao método "trace_dispatch()" para
      continuar o rastreamento nesse escopo.

   dispatch_exception(frame, arg)

      Se o depurador deve parar nesta exceção, invoca o método
      "user_exception()" (que deve ser substituído em subclasses).
      Levanta a exceção "BdbQuit" se o sinalizador "quitting" estiver
      definido (ele pode ser definido a partir de "user_exception()").
      Retorna uma referência ao método "trace_dispatch()" para
      continuar o rastreamento nesse escopo.

   Normalmente, as classes derivadas não substituem o seguinte
   métodos, mas podem fazê-lo se quiserem redefinir a definição de
   parada e  de pontos de interrupção.

   is_skipped_module(module_name)

      Retorna "True" se *module_name* corresponder a algum padrão de
      skip.

   stop_here(frame)

      Retorna "True" se frame estiver abaixo do frame inicial na
      pilha.

   break_here(frame)

      Retorna "True" se houver um ponto de interrupção efetivo para
      essa linha.

      Verifica se uma linha ou função ponto de interrupção existe e
      está em vigor.  Exclua os pontos de interrupção temporários com
      base nas informações de "effective()".

   break_anywhere(frame)

      Retorna "True" se existir algum ponto de interrupção para o nome
      de arquivo de *frame*'s.

   As classes derivadas devem substituir esses métodos para obter
   controle sobre a operação da depurador.

   user_call(frame, argument_list)

      Chamado a partir de "dispatch_call()" se um ponto de interrupção
      puder parar dentro da função chamada.

      *argument_list* não é mais usado e sempre será "None". O
      argumento é mantido por retrocompatibilidade.

   user_line(frame)

      Chamado a partir de "dispatch_line()" quando "stop_here()" ou
      "break_here()" retornam "True".

   user_return(frame, return_value)

      Chamado a partir de "dispatch_return()" quando "stop_here()"
      retorna "True".

   user_exception(frame, exc_info)

      Chamado a partir de "dispatch_exception()" quando "stop_here()"
      retorna "True".

   do_clear(arg)

      Manipula como um ponto de interrupção deve ser removido quando
      for temporário.

      Esse método deve ser implementado por classes derivadas.

   As classes derivadas e os clientes podem chamar os métodos a seguir
   para afetar o estado de stepping.

   set_step()

      Parar após uma linha de código.

   set_next(frame)

      Parar na próxima linha no frame fornecido ou abaixo dele.

   set_return(frame)

      Parar ao retornar do frame fornecido.

   set_until(frame, lineno=None)

      Parar quando a linha com *lineno* maior que a atual for
      alcançada ou ao retornar do frame atual.

   set_trace([frame])

      Inicia a depuração a partir de *frame*. Se *frame* não for
      especificado, a depuração começa a partir do frame do chamador.

      Alterado na versão 3.13: "set_trace()" entrará no depurador
      imediatamente, em vez de na próxima linha de código a ser
      executada.

   set_continue()

      Pare somente nos pontos de interrupção ou quando terminar.  Se
      não houver pontos de interrupção, defina o sistema função de
      rastreamento como "None".

   set_quit()

      Defina o atributo "quitting" como "True". Isso levanta "BdbQuit"
      na próxima chamada de um dos métodos "dispatch_*()".

   Classes derivadas e clientes podem chamar os métodos a seguir para
   manipular pontos de interrupção. Esses métodos retornam uma string
   contendo uma mensagem de erro se algo der errado, ou "None" se tudo
   estiver correto.

   set_break(filename, lineno, temporary=False, cond=None, funcname=None)

      Define um novo ponto de interrupção. Se a linha *lineno* não
      existir para o *filename* passado como argumento, retorna uma
      mensagem de erro. O *filename* deve estar na forma canônica,
      conforme descrito no método "canonic()".

   clear_break(filename, lineno)

      Exclui os pontos de interrupção em *filename* e *lineno*. Se
      nenhum tiver sido definido, retorna uma mensagem de erro.

   clear_bpbynumber(arg)

      Exclui o ponto de interrupção cujo índice é *arg* em
      "Breakpoint.bpbynumber". Se *arg* não for numérico ou estiver
      fora do intervalo, retorna uma mensagem de erro.

   clear_all_file_breaks(filename)

      Exclui todos os pontos de interrupção em *filename*. Se nenhum
      tiver sido definido, retorna uma mensagem de erro.

   clear_all_breaks()

      Exclui todos os pontos de interrupção existentes. Se nenhum
      tiver sido definido, retorna uma mensagem de erro.

   get_bpbynumber(arg)

      Retorna o ponto de interrupção especificado pelo número
      fornecido. Se *arg* for uma string, ele será convertido para um
      número. Se *arg* for uma string não numérica, se o ponto de
      interrupção nunca tiver existido ou tiver sido excluído, uma
      "ValueError" será levantada.

      Adicionado na versão 3.2.

   get_break(filename, lineno)

      Retorna "True" se houver um ponto de interrupção para *lineno*
      em *filename*.

   get_breaks(filename, lineno)

      Retorna todos os pontos de interrupção para *lineno* em
      *filename*, ou uma lista vazia se nenhum estiver definido.

   get_file_breaks(filename)

      Retorna todos os pontos de interrupção em *filename*, ou uma
      lista vazia se nenhum estiver definido.

   get_all_breaks()

      Retorna todos os pontos de interrupção definidos.

   Classes derivadas e clientes podem chamar os métodos a seguir para
   desabilitar e reiniciar eventos a fim de obter melhor desempenho.
   Esses métodos só funcionam ao usar o backend "'monitoring'".

   disable_current_event()

      Desabilita o evento atual até a próxima vez que
      "restart_events()" for chamada. Isso é útil quando o depurador
      não está interessado na linha atual.

      Adicionado na versão 3.14.

   restart_events()

      Reinicia todos os eventos desabilitados. Essa função é chamada
      automaticamente nos métodos "dispatch_*" após a chamada dos
      métodos "user_*". Se os métodos "dispatch_*" não forem
      substituídos, os eventos desabilitados serão reiniciados após
      cada interação do usuário.

      Adicionado na versão 3.14.

   Classes derivadas e clientes podem chamar os métodos a seguir para
   obter uma estrutura de dados que represente um stack trace
   (situação da pilha de execução).

   get_stack(f, t)

      Retorna uma lista de tuplas (frame, lineno) em um stack trace e
      um tamanho.

      O frame chamado mais recentemente é o último da lista. O tamanho
      é o número de frames abaixo do frame onde o depurador foi
      invocado.

   format_stack_entry(frame_lineno, lprefix=': ')

      Retorna uma string com informações sobre uma entrada da pilha,
      que é uma tupla "(frame, lineno)". A string retornada contém:

      * O nome de arquivo canônico que contém o quadro.

      * O nome da função ou ""<lambda>"".

      * O argumento de entrada.

      * O valor de retorno.

      * A linha de código (se existir).

   Os dois métodos a seguir podem ser chamados pelos clientes para
   usar um depurador e depurar uma *instrução*, fornecida como uma
   string.

   run(cmd, globals=None, locals=None)

      Depura uma instrução executada por meio da função "exec()".
      globals assume por padrão "__main__.__dict__", locals assume por
      padrão globals.

   runeval(expr, globals=None, locals=None)

      Depura uma expressão executada por meio da função "eval()".
      globals e locals têm o mesmo significado que em "run()".

   runctx(cmd, globals, locals)

      Por retrocompatibilidade. Chama o método "run()".

   runcall(func, /, *args, **kwds)

      Depura uma única chamada de função e retorna seu resultado.

Por fim, o módulo define as funções a seguir:

bdb.checkfuncname(b, frame)

   Retorna "True" se devemos interromper aqui, dependendo da forma
   como o "Breakpoint" foi configurado.

   If it was set via line number, it checks if "b.line" is the same as
   the one in *frame*. If the breakpoint was set via "function name",
   we have to check we are in the right *frame* (the right function)
   and if we are on its first executable line.

bdb.effective(file, line, frame)

   Retorna "(active breakpoint, delete temporary flag)" ou "(None,
   None)" como o ponto de interrupção sobre o qual agir.

   The *active breakpoint* is the first entry in "bplist" for the
   ("file", "line") (which must exist) that is "enabled", for which
   "checkfuncname()" is true, and that has neither a false "condition"
   nor positive "ignore" count.  The *flag*, meaning that a temporary
   breakpoint should be deleted, is "False" only when the "cond"
   cannot be evaluated (in which case, "ignore" count is ignored).

   Se essa entrada não existir, será retornado "(None, None)".

bdb.set_trace()

   Inicie a depuração com uma instância de "Bdb" a partir do frame do
   chamador.
