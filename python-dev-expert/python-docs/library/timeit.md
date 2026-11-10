"timeit" --- Mede o tempo de execução de pequenos trechos de código
*******************************************************************

**Código-fonte:** Lib/timeit.py

======================================================================

Este módulo fornece uma maneira simples de cronometrar pequenos
trechos do código Python. Ele tem uma Interface de linha de comando e
um chamável.  Ele evita uma série de armadilhas comuns para medir os
tempos de execução de um script. Veja também o capítulo "Algorithms"
de Tim Peters, na segunda edição do *Python Cookbook*, publicado pela
O'Reilly.


Basic examples
==============

O exemplo a seguir mostra como a Interface de linha de comando pode
ser usado para comparar três expressões diferentes:

   $ python -m timeit "'-'.join(str(n) for n in range(100))"
   10000 loops, best of 5: 30.2 usec per loop
   $ python -m timeit "'-'.join([str(n) for n in range(100)])"
   10000 loops, best of 5: 27.5 usec per loop
   $ python -m timeit "'-'.join(map(str, range(100)))"
   10000 loops, best of 5: 23.2 usec per loop

Isso pode ser obtido da interface Python interface

   >>> import timeit
   >>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
   0.3018611848820001
   >>> timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
   0.2727368790656328
   >>> timeit.timeit('"-".join(map(str, range(100)))', number=10000)
   0.23702679807320237

Um chamável também pode ser passado para a Python interface:

   >>> timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
   0.19665591977536678

Observe, entretanto, que "timeit()" determinará automaticamente o
número de repetições somente quando a interface de linha de comando
for usada. Na seção Exemplos você encontrará exemplos mais avançados.


Python interface
================

Este módulo define três funções e uma classe pública:

timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)

   Cria uma instância de "Timer" com o código de *setup* e a função
   *timer* função para executar o método "timeit()" com o total de
   execuções informado em *number*. O argumento opcional *globals*
   especifica um espaço de nomes no qual o código será executado.

   Alterado na versão 3.5: O parâmetro opcional *globals* foi
   adicionado.

timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=5, number=1000000, globals=None)

   Cria uma instância "Timer" com a instrução fornecida, o código de
   *setup* e a função *timer* e para executar o método "repeat()" com
   o total de execuções informando em *repeat* e o *número* de
   execuções fornecidos. O argumento opcional *globals* especifica um
   espaço de nomes no qual executar o código.

   Alterado na versão 3.5: O parâmetro opcional *globals* foi
   adicionado.

   Alterado na versão 3.7: Valor padrão de *repetição* mudou de 3 para
   5.

timeit.default_timer()

   O cronômetro padrão, que é sempre time.perf_counter(), retorna
   segundos com ponto flutuante. Uma alternativa,
   time.perf_counter_ns, retorna um inteiro em nanossegundos.

   Alterado na versão 3.3: "time.perf_counter()" é o cronômetro padrão
   agora.

class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)

   Classe para cronometrar a velocidade de execução de pequenos
   trechos de código.

   O construtor recebe uma instrução a ser cronometrada, uma instrução
   adicional usada para configuração e uma função de timer. Ambas as
   instruções têm como padrão "'pass'"; a função de timer é dependente
   da plataforma (veja a string do documento do módulo). *stmt* e
   *setup* também podem conter múltiplas instruções separadas por ";"
   ou novas linhas, desde que não contenham literais de string
   multilinhas. A instrução será, por padrão, executada dentro do
   espaço de nomes do *timeit*; esse comportamento pode ser controlado
   passando um espaço de nomes para *globals*.

   Para medir o tempo de execução da primeira instrução use o método
   "timeit()". Os métodos "repeat()" e "autorange()" são convenientes
   para chamar "timeit()" várias vezes.

   O tempo de execução de *setup* é excluído do tempo total de
   execução cronometrado.

   Os parâmetros *stmt* e *setup* também podem receber objetos que
   podem ser chamados sem argumentos. Isso incorporará chamadas a eles
   em uma função de timer que será executada por "timeit()". Observe
   que a sobrecarga de temporização é um pouco maior neste caso por
   causa das chamadas de função extras.

   Alterado na versão 3.5: O parâmetro opcional *globals* foi
   adicionado.

   timeit(number=1000000)

      Mede o tempo para a quantidade *number* de execuções da
      instrução principal. Isso executa a instrução setup uma vez e,
      em seguida, retorna o tempo necessário para executar a instrução
      principal várias vezes. O temporizador padrão retorna segundos
      como um float. O argumento é o número de vezes que o laço passa,
      com padrão de um milhão. A instrução principal, a instrução de
      configuração e a função de timer a ser usada são passadas para o
      construtor.

      Nota:

        Por padrão, "timeit()" desativa temporariamente *coleta de
        lixo* durante a temporização. A vantagem dessa abordagem é que
        ela torna temporizações independentes mais comparáveis. A
        desvantagem é que o GC pode ser um componente importante do
        desempenho da função que está sendo medida. Se for assim, o GC
        pode ser reativado como a primeira instrução na string
        *setup*. Por exemplo:

           timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()

   autorange(callback=None, target_time=None)

      Determina automaticamente quantas vezes chamar "timeit()".

      This is a convenience function that calls "timeit()" repeatedly
      so that the total time >= *Timer.target_time* seconds, returning
      the eventual (number of loops, time taken for that number of
      loops). It calls "timeit()" with increasing numbers from the
      sequence 1, 2, 5, 10, 20, 50, ... until the time taken is at
      least *target_time* seconds.

      Se *callback* for fornecido e não for "None", ele será chamado
      após cada tentativa e tem dois argumento: "callback(number,
      time_taken)".

      Adicionado na versão 3.6.

      Alterado na versão 3.15: The optional *target_time* parameter
      was added.

   repeat(repeat=5, number=1000000)

      Chama "timeit()" algumas vezes.

      Esse é um função de conveniência que chama o "timeit()"
      repetidamente e retorna uma lista de resultados.  O primeiro
      argumento especifica quantas vezes deve chamar o "timeit()".  O
      segundo argumento especifica o argumento *number* para
      "timeit()".

      Nota:

        É tentador calcular a média e o desvio padrão do vetor de
        resultados e relatá-los. No entanto, isso não é muito útil. Em
        um caso típico, o menor valor fornece um limite inferior para
        a velocidade com que sua máquina pode executar o trecho de
        código fornecido; valores mais altos no vetor de resultados
        normalmente não são causados pela variabilidade na velocidade
        do Python, mas por outros processos que interferem na precisão
        do seu tempo. Portanto, o "min()" do resultado é provavelmente
        o único número no qual você deve se interessar. Depois disso,
        você deve analisar o vetor inteiro e aplicar o bom senso em
        vez de estatística.

      Alterado na versão 3.7: Valor padrão de *repetição* mudou de 3
      para 5.

   print_exc(file=None)

      Função auxiliar para imprimir um traceback do código
      cronometrado.

      Uso típico:

         t = Timer(...)       # fora do try/except
         try:
             t.timeit(...)    # ou t.repeat(...)
         except Exception:
             t.print_exc()

      A vantagem em relação ao traceback padrão é que as linhas de
      origem no modelo compilado serão exibidas.  O argumento opcional
      *file* direciona para onde o traceback é enviado; o padrão é
      "sys.stderr".


Interface de linha de comando
=============================

Quando chamado como um programa a partir da linha de comando, as
seguintes opções estão disponíveis:

   python -m timeit [-n N] [-r N] [-u U] [-s S] [-p] [-v] [-h] [instrução ...]

As seguintes opções são permitidas

-n N, --number=N

   Quantas vezes deve executar 'statement'

-r N, --repeat=N

   Quantidade de vezes para repetir o cronômetro (o valor padrão é 5)

-s S, --setup=S

   instrução a ser executada apenas uma vez e quando iniciada (padrão
   "pass" )

-p, --process

   mede apenas o tempo de processamento, e não o tempo total de
   execução, usando "time.process_time()" em vez de
   "time.perf_counter()", que é o padrão

   Adicionado na versão 3.3.

-u, --unit=U

   especifique uma unidade de tempo para a saída do cronômetro; pode
   selecionar "nsec", "usec", "msec", ou "sec"

   Adicionado na versão 3.5.

-t, --target-time=T

   if "--number" is 0, the code will run until it takes at least this
   many seconds (default: 0.2)

   Adicionado na versão 3.15.

-v, --verbose

   imprime resultados brutos de tempo; repetir para obter mais
   precisão de dígitos

-h, --help

   imprime uma mensagem curta de uso e sai

Uma instrução multilinha pode ser fornecida especificando cada linha
como um argumento de instrução separado; linhas indentadas são
possíveis colocando um argumento entre aspas e usando espaços à
esquerda. Múltiplas opções "-s" são tratadas de forma semelhante.

If "-n" is not given, a suitable number of loops is calculated by
trying increasing numbers from the sequence 1, 2, 5, 10, 20, 50, ...
until the total time is at least "--target-time" seconds (default:
0.2).

As medições de "default_timer()" podem ser afetadas por outros
programas em execução na mesma máquina, portanto, a melhor coisa a
fazer quando uma cronometragem precisa é repeti-la algumas vezes e
usar o melhor tempo. A opção "-r" é boa para isso; o padrão de 5
repetições provavelmente é suficiente na maioria dos casos. Você pode
usar "time.process_time()" para medir o tempo de CPU.

Nota:

  Há uma certa sobrecarga padrão associada à execução de uma instrução
  *pass*. O código aqui não tenta ocultá-lo, mas você deve estar
  ciente disso.  A sobrecarga padrão pode ser medida invocando pelo
  programa sem argumento, e pode ser diferente entre diferentes
  versões Python.

Adicionado na versão 3.15: A saída é colorida por padrão e ela pode
ser controlada usando variáveis de ambiente.


Exemplos
========

É possível fornecer uma instrução de configuração que é executada
apenas uma vez no início:

   $ python -m timeit -s "text = 'sample string'; char = 'g'" "char in text"
   5000000 loops, best of 5: 0.0877 usec per loop
   $ python -m timeit -s "text = 'sample string'; char = 'g'" "text.find(char)"
   1000000 loops, best of 5: 0.342 usec per loop

Na saída, existem três campos. A contagem de laços, que informa
quantas vezes o corpo da instrução foi executado por repetição do laço
de temporização. A contagem de repetições ('melhor de 5') que informa
quantas vezes o laço de temporização foi repetido e, finalmente, o
tempo que o corpo da instrução levou, em média, na melhor repetição do
laço de temporização. Ou seja, o tempo necessário para a repetição
mais rápida dividido pela contagem de interações.

   >>> import timeit
   >>> timeit.timeit('char in text', setup='text = "sample string"; char = "g"')
   0.41440500499993504
   >>> timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"')
   1.7246671520006203

O mesmo pode ser feito usando a classe "Timer" e seus métodos:

   >>> import timeit
   >>> t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
   >>> t.timeit()
   0.3955516149999312
   >>> t.repeat()
   [0.40183617287970225, 0.37027556854118704, 0.38344867356679524, 0.3712595970846668, 0.37866875250654886]

Os exemplos a seguir mostram como cronometrar expressões que contêm
várias linhas. Aqui comparamos o custo de usar "hasattr()" vs.
"try"/"except" para testar atributos de objetos presentes e ausentes:

   $ python -m timeit "try:" "  str.__bool__" "except AttributeError:" "  pass"
   20000 loops, best of 5: 15.7 usec per loop
   $ python -m timeit "if hasattr(str, '__bool__'): pass"
   50000 loops, best of 5: 4.26 usec per loop

   $ python -m timeit "try:" "  int.__bool__" "except AttributeError:" "  pass"
   200000 loops, best of 5: 1.43 usec per loop
   $ python -m timeit "if hasattr(int, '__bool__'): pass"
   100000 loops, best of 5: 2.23 usec per loop

   >>> import timeit
   >>> # atributo está em falta
   >>> s = """\
   ... try:
   ...     str.__bool__
   ... except AttributeError:
   ...     pass
   ... """
   >>> timeit.timeit(stmt=s, number=100000)
   0.9138244460009446
   >>> s = "if hasattr(str, '__bool__'): pass"
   >>> timeit.timeit(stmt=s, number=100000)
   0.5829014980008651
   >>>
   >>> # atributo está presente
   >>> s = """\
   ... try:
   ...     int.__bool__
   ... except AttributeError:
   ...     pass
   ... """
   >>> timeit.timeit(stmt=s, number=100000)
   0.04215312199994514
   >>> s = "if hasattr(int, '__bool__'): pass"
   >>> timeit.timeit(stmt=s, number=100000)
   0.08588060699912603

Para dar ao módulo "timeit" acesso as funções que você definiu, você
pode passar o parâmetro *setup*, que contém um instrução de importar:

   def test():
       """Stupid test function"""
       L = [i for i in range(100)]

   if __name__ == '__main__':
       import timeit
       print(timeit.timeit("test()", setup="from __main__ import test"))

Outra opção é passar "globals()" para o parâmetro *globals*, o que
fará com que o código seja executado em seu espaço de nomes global.
Isso pode ser mais conveniente do que especificar individualmente
imports:

   def f(x):
       return x**2
   def g(x):
       return x**4
   def h(x):
       return x**8

   import timeit
   print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))
