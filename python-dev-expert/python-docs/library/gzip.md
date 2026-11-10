"gzip" --- Suporte para arquivos **gzip**
*****************************************

**Código-fonte:** Lib/gzip.py

======================================================================

Esse módulo disponibiliza uma interface simples para comprimir e
extrair arquivos como os programas GNU **gzip** e **gunzip** fazem.

Este é um *módulo opcional*. Se ele estiver faltando na sua cópia do
CPython, procure a documentação do seu distribuidor (ou seja, quem lhe
forneceu o Python). Se você for o distribuidor, consulte Requisitos
para módulos opcionais.

A compressão de dados é realizada pelo módulo "zlib".

O módulo "gzip" fornece a classe "GzipFile", bem como as funções de
conveniência "open()", "compress()" e "decompress()". A classe
"GzipFile" lê e grava arquivos no formato **gzip**, compactando ou
descompactando automaticamente os dados para que se pareçam com um
*objeto arquivo* comum.

Observe que formatos de arquivo adicionais que podem ser
descompactados pelos programas **gzip** e **gunzip**, como aqueles
produzidos por **compress** e **pack**, não são suportados por este
módulo.

Este módulo define os seguintes itens:

gzip.open(filename, mode='rb', compresslevel=6, encoding=None, errors=None, newline=None)

   Abre um arquivo comprimido com gzip em modo binário ou texto,
   retornando *objeto arquivo*.

   O argumento *filename* pode ser um nome de arquivo real (um objeto
   "str" ou "bytes"), ou um objeto arquivo existente para ler ou
   gravar.

   O argumento *mode* pode ser qualquer um de "'r'", "'rb'", "'a'",
   "'ab'", "'w'", "'wb'", "'x'" ou "'xb'" para modo binário, ou
   "'rt'", "'at'", "'wt'" ou "'xt'" para modo texto. O padrão é
   "'rb'".

   O argumento *compresslevel* é um inteiro de 0 a 9, como para o
   construtor de "GzipFile".

   Para o modo binário, esta função equivale ao construtor de
   "GzipFile": "GzipFile(filename, mode, compresslevel)". Neste caso,
   os argumentos *encoding*, *errors* e *newline* não devem ser
   fornecidos.

   Para o modo texto, um objeto "GzipFile" é criado e encapsulado em
   uma instância "io.TextIOWrapper" com a codificação especificada,
   comportamento de tratamento de erros e final(is) de linha.

   Alterado na versão 3.3: Adicionado suporte para *filename* ser um
   objeto arquivo, suporte para modo texto e os argumentos *encoding*,
   *errors* e *newline*.

   Alterado na versão 3.4: Adicionado suporte para os modos "'x'",
   "'xb'" e "'xt'".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

   Alterado na versão 3.15: O nível de compressão padrão foi reduzido
   para 6 (antes era 9). Esse é o nível padrão utilizado pela maioria
   das ferramentas de compressão e oferece um equilíbrio melhor entre
   velocidade e desempenho.

exception gzip.BadGzipFile

   Uma exceção levantada para arquivos gzip inválidos. Herda de
   "OSError". "EOFError" e "zlib.error" também podem ser levantadas
   para arquivos gzip inválidos.

   Adicionado na versão 3.8.

class gzip.GzipFile(filename=None, mode=None, compresslevel=6, fileobj=None, mtime=None)

   Construtor para a classe "GzipFile", que simula a maioria dos
   métodos de um *objeto arquivo*, com exceção do método "truncate()".
   Pelo menos um dos métodos *fileobj* e *filename* deve receber um
   valor não trivial.

   A nova instância de classe é baseada em *fileobj*, que pode ser um
   arquivo comum, um objeto "io.BytesIO" ou qualquer outro objeto que
   simule um arquivo. O padrão é "None", caso em que *filename* é
   aberto para fornecer um objeto arquivo.

   Quando *fileobj* não é "None", o argumento *filename* é usado
   apenas para ser incluído no cabeçalho do arquivo **gzip**, que pode
   incluir o nome original do arquivo descompactado. O padrão é o nome
   de arquivo *fileobj*, se discernível; caso contrário, o padrão é a
   string vazia e, neste caso, o nome original do arquivo não é
   incluído no cabeçalho.

   O argumento *mode* pode ser qualquer um dos seguintes: "'r'",
   "'rb'", "'a'", "'ab'", "'w'", "'wb'", "'x'" ou "'xb'", dependendo
   se o arquivo será lido ou escrito. O padrão é o modo de *fileobj*,
   se discernível; caso contrário, o padrão é "'rb'". Em versões
   futuras do Python, o modo de *fileobj* não será usado. É melhor
   sempre especificar *mode* para escrita.

   Observe que o arquivo é sempre aberto em modo binário. Para abrir
   um arquivo compactado em modo texto, use "open()" (ou envolva seu
   "GzipFile" com um "io.TextIOWrapper").

   O argumento *compresslevel* é um inteiro de "0" a "9" que controla
   o nível de compressão; "1" é o mais rápido e produz a menor
   compressão, e "9" é o mais lento e produz a maior compressão. "0"
   significa sem compressão. O padrão é "6".

   O argumento opcional *mtime* é o registro de data e hora
   (*timestamp*) solicitado pelo gzip. O tempo é expresso no formato
   Unix, isto é, em segundos contados a partir de 00:00:00 UTC, 1º de
   janeiro de 1970. Defina *mtime* como "0" para gerar um fluxo
   compactado que não dependa do momento de sua criação. Se *mtime*
   for omitido ou definido como "None", utiliza-se o horário atual; no
   entanto, caso o horário atual esteja fora do intervalo entre
   00:00:00 UTC, 1º de janeiro de 1970, e 06:28:15 UTC, 7 de fevereiro
   de 2106 — ou se o valor fornecido para o argumento *mtime* estiver
   fora da faixa de "0" a "2**32-1" —, o valor "0" será utilizado em
   seu lugar.

   Veja abaixo o atributo "mtime" que é definido durante a
   descompactação.

   Chamar o método "close()" de um objeto "GzipFile" não fecha
   *fileobj*, pois você pode querer adicionar mais material após os
   dados compactados. Isso também permite que você passe um objeto
   "io.BytesIO" aberto para escrita como *fileobj* e recupere o buffer
   de memória resultante usando o método "getvalue()" do objeto
   "io.BytesIO".

   "GzipFile" suporta a interface "io.BufferedIOBase", incluindo
   iteração e a instrução "with". Apenas o método "truncate()" não é
   implementado.

   "GzipFile" também disponibiliza os seguintes métodos e atributos:

   peek(n)

      Lê *n* bytes não compactados sem avançar a posição do arquivo. O
      número de bytes retornados pode ser maior ou menor que o
      solicitado.

      Nota:

        Embora chamar "peek()" não altere a posição do arquivo
        "GzipFile", ele pode alterar a posição do objeto arquivo
        subjacente (por exemplo, se o "GzipFile" foi construído com o
        parâmetro *fileobj*).

      Adicionado na versão 3.2.

   mode

      "'rb'" para leitura e "'wb'" para escrita.

      Alterado na versão 3.13: Em versões anteriores era um inteiro
      "1" ou "2".

   mtime

      Ao descompactar, este atributo é definido como o último registro
      de data e hora no cabeçalho lido mais recentemente. É um inteiro
      que contém o número de segundos desde a era Unix (00:00:00 UTC,
      1º de janeiro de 1970). O valor inicial antes da leitura de
      qualquer cabeçalho é "None".

   name

      O caminho para o arquivo gzip no disco, como "str" ou "bytes".
      Equivalente à saída de "os.fspath()" no caminho de entrada
      original, sem nenhuma outra normalização, resolução ou expansão.

   Alterado na versão 3.1: Foi adicionado suporte para a instrução
   "with", juntamente com o argumento do construtor *mtime* e o
   atributo "mtime".

   Alterado na versão 3.2: Foi adicionado suporte para arquivos
   preenchidos com zeros e não pesquisáveis.

   Alterado na versão 3.3: O método "io.BufferedIOBase.read1()" agora
   está implementado.

   Alterado na versão 3.4: Adicionado suporte para os modos "'x'" e
   "'xb'".

   Alterado na versão 3.5: Adicionado suporte para escrever *objetos
   bytes ou similares* arbitrários. O método "read()" agora aceita o
   argumento "None".

   Alterado na versão 3.6: Aceita um *objeto caminho ou similar*.

   Descontinuado desde a versão 3.9: Abrir "GzipFile" para escrita sem
   especificar o argumento *mode* está descontinuado.

   Alterado na versão 3.12: Remove o atributo "filename" e usa o
   atributo "name".

   Alterado na versão 3.15: O nível de compressão padrão foi reduzido
   para 6 (antes era 9). Esse é o nível padrão utilizado pela maioria
   das ferramentas de compressão e oferece um equilíbrio melhor entre
   velocidade e desempenho.

gzip.compress(data, compresslevel=6, *, mtime=0)

   Compacta *data*, retornando um objeto "bytes" contendo os dados
   compactados. *compresslevel* e *mtime* têm o mesmo significado que
   no construtor de "GzipFile" acima, mas *mtime* assume o valor
   padrão 0 para uma saída reprodutível.

   Adicionado na versão 3.2.

   Alterado na versão 3.8: Adicionado o parâmetro *mtime* para saída
   reproduzível.

   Alterado na versão 3.11: A velocidade é melhorada pela compactação
   de todos os dados de uma só vez, em vez de em fluxo contínuo.
   Chamadas com *mtime* definido como "0" são delegadas a
   "zlib.compress()" para maior velocidade. Nessa situação, a saída
   pode conter um valor de byte "OS" no cabeçalho gzip diferente de
   255 "unknown", conforme fornecido pela implementação subjacente do
   zlib.

   Alterado na versão 3.13: O byte do cabeçalho gzip do sistema
   operacional tem a garantia de ser definido como 255 quando esta
   função é usada, como era o caso na versão 3.10 e anteriores.

   Alterado na versão 3.14: O parâmetro *mtime* agora assume o valor
   padrão 0 para uma saída reprodutível. Para o comportamento anterior
   de usar a hora atual, passe "None" para *mtime*.

   Alterado na versão 3.15: O nível de compressão padrão foi reduzido
   para 6 (antes era 9). Esse é o nível padrão utilizado pela maioria
   das ferramentas de compressão e oferece um equilíbrio melhor entre
   velocidade e desempenho.

gzip.decompress(data)

   Descompacta *data*, retornando um objeto "bytes" contendo os dados
   descompactados. Esta função é capaz de descompactar dados de gzip
   de vários membros (vários blocos gzip concatenados). Quando é certo
   que os dados contêm apenas um membro, a função "zlib.decompress()"
   com *wbits* definido como 31 é mais rápida.

   Adicionado na versão 3.2.

   Alterado na versão 3.11: A velocidade é melhorada ao descompactar
   os membros de uma só vez na memória, em vez de fazê-lo de forma
   contínua.


Exemplos de uso
===============

Exemplo de como ler um arquivo comprimido:

   import gzip
   with gzip.open('/home/joe/arquivo.txt.gz', 'rb') as f:
       file_content = f.read()

Exemplo de como criar um arquivo comprimido com GZIP:

   import gzip
   content = b"Muito conteúdo aqui"
   with gzip.open('/home/joe/arquivo.txt.gz', 'wb') as f:
       f.write(content)

Exemplo de como comprimir um arquivo existente com GZIP:

   import gzip
   import shutil
   with open('/home/joe/arquivo.txt', 'rb') as f_in:
       with gzip.open('/home/joe/arquivo.txt.gz', 'wb') as f_out:
           shutil.copyfileobj(f_in, f_out)

Exemplo de como comprimir uma string binária com compressão GZIP:

   import gzip
   s_in = b"Muito conteúdo aqui"
   s_out = gzip.compress(s_in)

Ver também:

  Módulo "zlib"
     O módulo básico de compactação de dados necessário para dar
     suporte ao formato de arquivo do **gzip**.

  Caso a (des)compressão do gzip seja um gargalo, o pacote python-isal
  acelera a (des)compressão com uma API quase sempre compatível.


Interface de linha de comando
=============================

O módulo "gzip" fornece uma interface de linha de comando simples para
compactar ou descompactar arquivos.

Uma vez executado, o módulo "gzip" mantém o(s) arquivo(s) de entrada.

Alterado na versão 3.8: Adiciona uma nova interface de linha de
comando com um mensagem de uso. Por padrão, ao executar a CLI, o nível
de compactação padrão é 6.


Opções de linha de comando
--------------------------

file

   Se o *arquivo* não for especificado, ler de "sys.stdin"

--fast

   Indica o método mais rápido de compressão (menor compressão)

--best

   Indica o método mais lento de compressão (melhor compressão).

-d, --decompress

   Descompacta o arquivo dado.

-h, --help

   Exibe a mensagem de ajuda.
