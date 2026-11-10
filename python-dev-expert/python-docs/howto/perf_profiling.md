Python support for the "perf map" compatible profilers
******************************************************

The Linux perf profiler and samply are powerful tools that allow you
to profile and obtain information about the performance of your
application. Both tools have vibrant ecosystems that aid with the
analysis of the data they produce.

The main problem with using these profilers with Python applications
is that they only get information about native symbols, that is, the
names of functions and procedures written in C. This means that the
names and file names of Python functions in your code will not appear
in the profiler output.

Since Python 3.12, the interpreter can run in a special mode that
allows Python functions to appear in the output of compatible
profilers. When this mode is enabled, the interpreter will interpose a
small piece of code compiled on the fly before the execution of every
Python function and it will teach the profiler the relationship
between this piece of code and the associated Python function using
perf map files.

Nota:

  Support for profiling is available on Linux and macOS on select
  architectures. Perf is available on Linux, while samply can be used
  on both Linux and macOS. samply support on macOS is available
  starting from Python 3.15. Check the output of the "configure" build
  step or check the output of "python -m sysconfig | grep
  HAVE_PERF_TRAMPOLINE" to see if your system is supported.

Por exemplo, considere o seguinte script:

   def foo(n):
       result = 0
       for _ in range(n):
           result += 1
       return result

   def bar(n):
       foo(n)

   def baz(n):
       bar(n)

   if __name__ == "__main__":
       baz(1000000)

Podemos executar "perf" para obter amostras de rastreamentos de pilha
da CPU em 9999 hertz:

   $ perf record -F 9999 -g -o perf.data python meu_script.py

Então podemos usar "perf report" para analisar os dados:

   $ perf report --stdio -n -g

   # Children      Self       Samples  Command     Shared Object       Symbol
   # ........  ........  ............  ..........  ..................  ..........................................
   #
       91.08%     0.00%             0  python.exe  python.exe          [.] _start
               |
               ---_start
               |
                   --90.71%--__libc_start_main
                           Py_BytesMain
                           |
                           |--56.88%--pymain_run_python.constprop.0
                           |          |
                           |          |--56.13%--_PyRun_AnyFileObject
                           |          |          _PyRun_SimpleFileObject
                           |          |          |
                           |          |          |--55.02%--run_mod
                           |          |          |          |
                           |          |          |           --54.65%--PyEval_EvalCode
                           |          |          |                     _PyEval_EvalFrameDefault
                           |          |          |                     PyObject_Vectorcall
                           |          |          |                     _PyEval_Vector
                           |          |          |                     _PyEval_EvalFrameDefault
                           |          |          |                     PyObject_Vectorcall
                           |          |          |                     _PyEval_Vector
                           |          |          |                     _PyEval_EvalFrameDefault
                           |          |          |                     PyObject_Vectorcall
                           |          |          |                     _PyEval_Vector
                           |          |          |                     |
                           |          |          |                     |--51.67%--_PyEval_EvalFrameDefault
                           |          |          |                     |          |
                           |          |          |                     |          |--11.52%--_PyCompactLong_Add
                           |          |          |                     |          |          |
                           |          |          |                     |          |          |--2.97%--_PyObject_Malloc
   ...

Como você pode ver, as funções Python não são mostradas na saída,
apenas "_PyEval_EvalFrameDefault" (a função que avalia o bytecode
Python) aparece. Infelizmente isso não é muito útil porque todas as
funções Python usam a mesma função C para avaliar bytecode, portanto
não podemos saber qual função Python corresponde a qual função de
avaliação de bytecode.

Em vez disso, se executarmos o mesmo experimento com o suporte "perf"
ativado, obteremos:

   $ perf report --stdio -n -g

   # Children      Self       Samples  Command     Shared Object       Symbol
   # ........  ........  ............  ..........  ..................  .....................................................................
   #
       90.58%     0.36%             1  python.exe  python.exe          [.] _start
               |
               ---_start
               |
                   --89.86%--__libc_start_main
                           Py_BytesMain
                           |
                           |--55.43%--pymain_run_python.constprop.0
                           |          |
                           |          |--54.71%--_PyRun_AnyFileObject
                           |          |          _PyRun_SimpleFileObject
                           |          |          |
                           |          |          |--53.62%--run_mod
                           |          |          |          |
                           |          |          |           --53.26%--PyEval_EvalCode
                           |          |          |                     py::<module>:/src/script.py
                           |          |          |                     _PyEval_EvalFrameDefault
                           |          |          |                     PyObject_Vectorcall
                           |          |          |                     _PyEval_Vector
                           |          |          |                     py::baz:/src/script.py
                           |          |          |                     _PyEval_EvalFrameDefault
                           |          |          |                     PyObject_Vectorcall
                           |          |          |                     _PyEval_Vector
                           |          |          |                     py::bar:/src/script.py
                           |          |          |                     _PyEval_EvalFrameDefault
                           |          |          |                     PyObject_Vectorcall
                           |          |          |                     _PyEval_Vector
                           |          |          |                     py::foo:/src/script.py
                           |          |          |                     |
                           |          |          |                     |--51.81%--_PyEval_EvalFrameDefault
                           |          |          |                     |          |
                           |          |          |                     |          |--13.77%--_PyCompactLong_Add
                           |          |          |                     |          |          |
                           |          |          |                     |          |          |--3.26%--_PyObject_Malloc


Using the samply profiler
=========================

samply is a modern profiler that can be used as an alternative to
perf. It uses the same perf map files that Python generates, making it
compatible with Python's profiling support. samply is particularly
useful on macOS where perf is not available.

To use samply with Python, first install it following the instructions
at https://github.com/mstange/samply, then run:

   $ samply record PYTHONPERFSUPPORT=1 python my_script.py

This will open a web interface where you can analyze the profiling
data interactively. The advantage of samply is that it provides a
modern web-based interface for analyzing profiling data and works on
both Linux and macOS.

On macOS, samply support requires Python 3.15 or later. Also on macOS,
samply can't profile signed Python executables due to restrictions by
macOS. You can profile with Python binaries that you've compiled
yourself, or which are unsigned or locally-signed (such as anything
installed by Homebrew). In order to attach to running processes on
macOS, run "samply setup" once (and every time samply is updated) to
self-sign the samply binary.


Como habilitar o suporte a perfilação com "perf"
================================================

O suporte à perfilação com "perf" pode ser habilitado desde o início
usando a variável de ambiente "PYTHONPERFSUPPORT" ou a opção "-X
perf", ou dinamicamente usando "sys.activate_stack_trampoline()" e
"sys.deactivate_stack_trampoline()".

As funções "sys" têm precedência sobre a opção "-X", a opção "-X" tem
precedência sobre a variável de ambiente.

Exemplo usando a variável de ambiente:

   $ PYTHONPERFSUPPORT=1 perf record -F 9999 -g -o perf.data python meu_script.py
   $ perf report -g -i perf.data

Exemplo usando a opção "-X":

   $ perf record -F 9999 -g -o perf.data python -X perf meu_script.py
   $ perf report -g -i perf.data

Exemplo usando as APIs de "sys" em "example.py":

   import sys

   sys.activate_stack_trampoline("perf")
   do_profiled_stuff()
   sys.deactivate_stack_trampoline()

   non_profiled_stuff()

... então:

   $ perf record -F 9999 -g -o perf.data python ./example.py
   $ perf report -g -i perf.data


Como obter os melhores resultados
=================================

For best results, keep frame pointers enabled. On supported GCC-
compatible toolchains, CPython builds itself with "-fno-omit-frame-
pointer" and similar flags (see "--without-frame-pointers" for
details). These flags allow profilers to unwind using only the frame
pointer and not on DWARF debug information. This is because as the
code that is interposed to allow "perf" support is dynamically
generated it doesn't have any DWARF debugging information available.

Você pode verificar se o seu sistema foi compilado com este
sinalizador executando:

   $ python -m sysconfig | grep 'no-omit-frame-pointer'

Se você não vir nenhuma saída, significa que seu interpretador não foi
compilado com ponteiros de quadro e, portanto, pode não ser capaz de
mostrar funções Python na saída de "perf".


Como trabalhar sem ponteiros de quadro
======================================

Se você estiver trabalhando com um interpretador Python que foi
compilado sem ponteiros de quadro, você ainda pode usar o perfilador
"perf", mas a sobrecarga será um pouco maior porque o Python precisa
gerar informações de desenrolamento para cada chamada de função Python
em tempo real. Além disso, "perf" levará mais tempo para processar os
dados porque precisará usar as informações de depuração DWARF para
desenrolar a pilha e este é um processo lento.

Para habilitar esse modo, você pode usar a variável de ambiente
"PYTHON_PERF_JIT_SUPPORT" ou a opção "-X perf_jit", que habilitará o
modo JIT para o perfilador "perf".

Nota:

  Devido a um bug na ferramenta "perf", apenas versões "perf"
  superiores à v6.8 funcionarão com o modo JIT. A correção também foi
  portada para a versão v6.7.2 da ferramenta.Note que ao verificar a
  versão da ferramenta "perf" (o que pode ser feito executando "perf
  version") você deve levar em conta que algumas distros adicionam
  alguns números de versão personalizados, incluindo um caractere "-".
  Isso significa que "perf 6.7-3" não é necessariamente "perf 6.7.3".

Ao usar o modo JIT do perf, você precisa de uma etapa extra antes de
poder executar "perf report". Você precisa chamar o comando "perf
inject" para injetar as informações JIT no arquivo "perf.data".:

   $ perf record -F 9999 -g -k 1 --call-graph dwarf -o perf.data python -Xperf_jit meu_script.py
   $ perf inject -i perf.data --jit --output perf.jit.data
   $ perf report -g -i perf.jit.data

ou usando a variável de ambiente:

   $ PYTHON_PERF_JIT_SUPPORT=1 perf record -F 9999 -g --call-graph dwarf -o perf.data python meu_script.py
   $ perf inject -i perf.data --jit --output perf.jit.data
   $ perf report -g -i perf.jit.data

O comando "perf inject --jit" lerá "perf.data", pegará automaticamente
o arquivo de dump perf que o Python cria (em "/tmp/perf-$PID.dump") e,
em seguida, criará "perf.jit.data" que mescla todas as informações
JIT. Ele também deve criar muitos arquivos "jitted-XXXX-N.so" no
diretório atual, que são imagens ELF para todos os trampolins JIT que
foram criados pelo Python.

Aviso:

  Ao usar "--call-graph dwarf", a ferramenta "perf" fará snapshots da
  pilha do processo que está sendo perfilado e salvará as informações
  no arquivo "perf.data". Por padrão, o tamanho do dump da pilha é de
  8192 bytes, mas você pode alterar o tamanho passando-o após uma
  vírgula, como "--call-graph dwarf,16384".O tamanho do dump da pilha
  é importante porque, se for muito pequeno, o "perf" não conseguirá
  desfazer o descompasso da pilha e a saída será incompleta. Por outro
  lado, se for muito grande, o "perf" não conseguirá amostrar o
  processo com a frequência desejada, pois a sobrecarga será maior.O
  tamanho da pilha é particularmente importante ao criar perfis de
  código Python compilado com níveis de otimização baixos (como
  "-O0"), pois essas construções tendem a ter quadros de pilha
  maiores. Se você estiver compilando Python com "-O0" e não estiver
  vendo funções Python na saída do perfil, tente aumentar o tamanho do
  despejo de pilha para 65528 bytes (o máximo):

     $ perf record -F 9999 -g -k 1 --call-graph dwarf,65528 -o perf.data python -Xperf_jit meu_script.py

  Diferentes sinalizadores de compilação podem impactar
  significativamente os tamanhos de pilha:

  * Construções com "-O0" geralmente têm quadros de pilha muito
    maiores do que aquelas com "-O1" ou superior

  * Adiciona otimizações ("-O1", "-O2", etc.) normalmente reduz o
    tamanho da pilha

  * Os ponteiros de quadro ("-fno-omit-frame-pointer") geralmente
    fornecem um desenrolamento de pilha mais confiável
