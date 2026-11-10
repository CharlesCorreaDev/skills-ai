Depuração e perfilamento
************************

Essas bibliotecas ajudam no desenvolvimento do Python: o depurador
permite que você percorra o código, analise os quadros de pilha e
defina pontos de interrupção etc., e os criadores de perfil executam o
código e fornecem uma análise detalhada dos tempos de execução,
permitindo identificar gargalos em seus programas. Os eventos de
auditoria fornecem visibilidade dos comportamentos de tempo de
execução que, de outra forma, exigiriam depuração ou correção
intrusiva.

* Tabela de eventos de auditoria

* "bdb" --- Framework do depurador

* "faulthandler" --- Dump the Python traceback

  * Dumping the traceback

  * Dumping the C stack

    * C Stack Compatibility

  * Fault handler state

  * Dumping the tracebacks after a timeout

  * Dumping the traceback on a user signal

  * Issue with file descriptors

  * Exemplo

* "pdb" --- O depurador do Python

  * Interface de linha de comando

  * Comandos de depuração

* "profiling" --- Python profilers

  * Introduction to profiling

  * Choosing a profiler

    * When to use statistical sampling

    * When to use deterministic tracing

  * Quick start

    * Statistical profiling

    * Deterministic profiling

  * Understanding profile output

  * Legacy compatibility

    * "profiling.tracing" --- Deterministic profiler

      * What is deterministic profiling?

      * Command-line interface

      * Programmatic usage examples

        * Basic profiling

        * Using the "Profile" class

      * Module reference

      * Using a custom timer

      * Limitations

    * "profiling.sampling" --- Statistical profiler

      * What is statistical profiling?

        * How time is estimated

        * When to use a different approach

      * Quick examples

      * Commands

        * The "run" command

        * The "attach" command

        * The "dump" command

        * The "replay" command

        * Profiling in production

        * Platform requirements

        * Version compatibility

      * Sampling configuration

        * Sampling rate and duration

        * Thread selection

        * Blocking mode

        * Special frames

        * Opcode-aware profiling

        * Real-time statistics

        * Subprocess profiling

        * Sampling efficiency

      * Profiling modes

        * Wall-clock mode

        * CPU mode

        * Comparing wall-clock and CPU profiles

        * GIL mode

        * Exception mode

      * Output formats

        * pstats format

        * Collapsed stacks format

        * Flame graph format

          * Differential flame graphs

        * Gecko format

        * Heatmap format

        * Binary format

      * Record and replay workflow

      * Live mode

        * Keyboard commands

      * Async-aware profiling

        * Async modes

        * Task markers and stack reconstruction

        * Option restrictions

      * Command-line interface

        * Global options

        * Dump options

        * Sampling options

        * Mode options

        * Output options

        * pstats display options

        * Run command options

* "pstats" --- Statistics for profilers

  * Reading and displaying profile data

    * Working with statistics

    * Filtering output

    * Analyzing call relationships

    * Combining multiple profiles

  * The "Stats" class

  * Interface de linha de comando

* "timeit" --- Mede o tempo de execução de pequenos trechos de código

  * Basic examples

  * Python interface

  * Interface de linha de comando

  * Exemplos

* "trace" --- Rastreia ou acompanha a execução de instruções Python

  * Uso na linha de comando

    * Opções principais

    * Modificadores

    * Filtros

  * Interface programática

* "tracemalloc" --- Trace memory allocations

  * Exemplos

    * Exibe o top 10

    * Compute differences

    * Get the traceback of a memory block

    * Pretty top

      * Record the current and peak size of all traced memory blocks

  * API

    * Funções

    * DomainFilter

    * Filter

    * Frame

    * Snapshot

    * Statistic

    * StatisticDiff

    * Trace

    * Traceback
