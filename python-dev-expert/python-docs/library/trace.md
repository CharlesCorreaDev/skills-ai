"trace" --- Rastreia ou acompanha a execução de instruções Python
*****************************************************************

**Código-fonte:** Lib/trace.py

======================================================================

The "trace" module allows you to trace program execution, generate
annotated statement coverage listings, print caller/callee
relationships and list functions executed during a program run.  It
can be used in another program or from the command line.

Ver também:

  Coverage.py
     Uma popular ferramenta de cobertura de terceiros que fornece
     saída HTML junto com recursos avançados, como cobertura de
     ramificações.


Uso na linha de comando
=======================

The "trace" module can be invoked from the command line.  It can be as
simple as

   python -m trace --count -C . algumarquivo.py ...

O comando acima irá executar "algumarquivo.py" e gerar listagens
anotadas de todos os módulos Python importados durante a execução para
o diretório atual.

--help

   Exibe o modo de uso e sai.

--version

   Exibe a versão do módulo e sai.

Adicionado na versão 3.8: Added "--module" option that allows running
an executable module.


Opções principais
-----------------

At least one of the following options must be specified when invoking
"trace".  The "--listfuncs" option is mutually exclusive with the "--
trace" and "--count" options. When "--listfuncs" is provided, neither
"--count" nor "--trace" are accepted, and vice versa.

-c, --count

   Produz um conjunto de arquivos de listagem anotada após a conclusão
   do programa que mostra quantas vezes cada instrução foi executada.
   Veja também "--coverdir", "--file" e "--no-report" abaixo.

-t, --trace

   Exibe linhas como elas são executadas.

-l, --listfuncs

   Exibe as funções executadas executando o programa.

-r, --report

   Produz uma lista anotada de uma execução de programa anterior que
   usava a opção "--count" e "--file". Isso não executa nenhum código.

-T, --trackcalls

   Exibe os relacionamentos de chamada expostos ao executar o
   programa.


Modificadores
-------------

-f, --file=<file>

   Nome de um arquivo para acumular contagens em várias execuções de
   rastreamento. Deve ser usado com a opção "--count".

-C, --coverdir=<dir>

   Diretório para onde vão os arquivos de relatório. O relatório de
   cobertura para "pacote.módulo" é escrito em arquivo
   "*dir*/*pacote*/*módulo*.cover".

-m, --missing

   Ao gerar listagens anotadas, marca as linhas que não foram
   executadas com ">>>>>>".

-s, --summary

   Ao usar "--count" ou "--report", escreve um breve resumo no stdout
   para cada arquivo processado.

-R, --no-report

   Não gera listagens anotadas. Isso é útil se você pretende fazer
   várias execuções com "--count", e então produzir um único conjunto
   de listagens anotadas no final.

-g, --timing

   Prefixa cada linha com o tempo desde o início do programa. Usado
   apenas durante o rastreamento.


Filtros
-------

Essas opções podem ser repetidas várias vezes.

--ignore-module=<mod>

   Ignora cada um dos nomes de módulo fornecidos e seus submódulos (se
   for um pacote). O argumento pode ser uma lista de nomes separados
   por uma vírgula.

--ignore-dir=<dir>

   Ignora todos os módulos e pacotes no diretório e subdiretórios
   nomeados. O argumento pode ser uma lista de diretórios separados
   por "os.pathsep".


Interface programática
======================

class trace.Trace(count=1, trace=1, countfuncs=0, countcallers=0, ignoremods=(), ignoredirs=(), infile=None, outfile=None, timing=False)

   Cria um objeto para rastrear a execução de uma única instrução ou
   expressão. Todos os parâmetros são opcionais. *count* ativa a
   contagem de números de linha. *trace* ativa o rastreamento de
   execução de linha. *countfuncs* ativa a listagem das funções
   chamadas durante a execução. *countcallers* ativa o rastreamento de
   relacionamento de chamada. *ignoremods* é uma lista de módulos ou
   pacotes a serem ignorados. *ignoreirs* é uma lista de diretórios
   cujos módulos ou pacotes devem ser ignorados. *infile* é o nome do
   arquivo do qual deve ler as informações de contagem armazenadas.
   *outfile* é o nome do arquivo no qual deve escrever as informações
   de contagem atualizadas. *timing* ativa a exibição de um carimbo de
   data/hora relativo ao momento em que o rastreamento foi iniciado.

   run(cmd)

      Executa o comando e reúne estatísticas da execução com os
      parâmetros de rastreamento atuais. *cmd* deve ser uma string ou
      objeto código, adequado para passar para "exec()".

   runctx(cmd, globals=None, locals=None)

      Executa o comando e reúne estatísticas da execução com os
      parâmetros de rastreamento atuais, nos ambientes global e local
      definidos. Se não for definido, *globals* e *locals* usam como
      padrão dicionários vazios.

   runfunc(func, /, *args, **kwds)

      Chama *func* com os argumentos fornecidos sob controle do objeto
      "Trace" com os parâmetros de rastreamento atuais.

   results()

      Retorna um objeto "CoverageResults" que contém os resultados
      cumulativos de todas as chamadas anteriores para "run", "runctx"
      e "runfunc" para a instância "Trace" fornecida. Não redefine os
      resultados de rastreamento acumulados.

class trace.CoverageResults

   Um contêiner para resultados de cobertura, criado por
   "Trace.results()". Não deve ser criado diretamente pelo usuário.

   update(other)

      Mescla dados de outro objeto "CoverageResults".

   write_results(show_missing=True, summary=False, coverdir=None, *, ignore_missing_files=False)

      Escreve os resultados da cobertura. Defina *show_missing* para
      mostrar as linhas que não tiveram ocorrências. Defina o
      *summary* para incluir na saída o resumo da cobertura por
      módulo. *coverdir* especifica o diretório no qual os arquivos de
      resultados de cobertura serão enviados. Se for "None", os
      resultados de cada arquivo de origem são colocados em seu
      diretório.

      Se *ignore_missing_files* for "True", as contagens de cobertura
      para arquivos que não existem mais serão ignoradas
      silenciosamente. Caso contrário, um arquivo ausente vai levantar
      "FileNotFoundError".

      Alterado na versão 3.13: Adicionado o parâmetro
      *ignore_missing_files*.

Um exemplo simples que demonstra o uso da interface programática:

   import sys
   import trace

   # cria um objeto Trace, dizendo a ele o que ignorar e se deve
   # fazer rastreamento ou contagem de linhas ou ambos.
   tracer = trace.Trace(
       ignoredirs=[sys.prefix, sys.exec_prefix],
       trace=0,
       count=1)

   # executa o novo comando usando o rastreador fornecido
   tracer.run('main()')

   # faz um relatório, colocando a saída no diretório atual
   r = tracer.results()
   r.write_results(show_missing=True, coverdir=".")
