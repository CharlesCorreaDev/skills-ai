"fileinput" --- Itera sobre linhas de múltiplos fluxos de entrada
*****************************************************************

**Código-fonte:** Lib/fileinput.py

======================================================================

Este módulo implementa uma classe auxiliar e funções para escrever
rapidamente um laço sobre uma entrada padrão ou uma lista de arquivos.
Se você quiser apenas ler ou escrever um arquivo veja "open()".

O uso típico é:

   import fileinput
   for line in fileinput.input(encoding="utf-8"):
       process(line)

Isto itera sobre as linhas de todos os arquivos listados em
"sys.argv[1:]", padronizando "sys.stdin" se a lista estiver vazia. Se
o nome de um arquivo for "'-'", ele também será substituído por
"sys.stdin" e os argumentos opcionais *mode* e *openhook* serão
ignorados. Para especificar uma lista alternativa de nomes de
arquivos, passe-a como primeiro argumento para "input()". Um único
nome de arquivo também é permitido.

Todos os arquivos são abertos em modo texto por padrão, mas você pode
substituir isso especificando o parâmetro *mode* na chamada para
"input()" ou "FileInput". Se ocorrer um erro de E/S durante a abertura
ou leitura de um arquivo, "OSError" será levantada.

Alterado na versão 3.3: "IOError" costumava ser levantada; agora é um
apelido de "OSError".

Se "sys.stdin" for usado mais de uma vez, o segundo e posterior uso
não retornará nenhuma linha, exceto talvez para uso interativo, ou se
tiver sido explicitamente redefinido (por exemplo, usando
"sys.stdin.seek(0)").

Arquivos vazios são abertos e fechados imediatamente; a única vez que
sua presença na lista de nomes de arquivos é perceptível é quando o
último arquivo aberto está vazio.

As linhas são retornadas com novas linhas intactas, o que significa
que a última linha de um arquivo pode não ter nenhuma.

Você pode controlar como os arquivos são abertos fornecendo um gancho
de abertura através do parâmetro *openhook* para "fileinput.input()"
ou "FileInput()". O gancho deve ser uma função que recebe dois
argumentos, *filename* e *mode*, e retorna um objeto arquivo ou
similar aberto de acordo. Se *encoding* e/ou *errors* forem
especificados, eles serão passados para o gancho como argumentos
nomeados adicionais. Este módulo fornece um "hook_compressed()" para
oferece suporte a arquivos compactados.

A seguinte função é a interface principal deste módulo:

fileinput.input(files=None, inplace=False, backup='', *, mode='r', openhook=None, encoding=None, errors=None)

   Cria uma instância da classe "FileInput". A instância será usada
   como estado global para as funções deste módulo e também será
   retornada para uso durante a iteração. Os parâmetros desta função
   serão passados para o construtor da classe "FileInput".

   A instância "FileInput" pode ser usada como um gerenciador de
   contexto na instrução "with". Neste exemplo, *input* é fechado após
   a saída da instrução "with", mesmo se ocorrer uma exceção:

      with fileinput.input(files=('spam.txt', 'eggs.txt'), encoding="utf-8") as f:
          for line in f:
              process(line)

   Alterado na versão 3.2: Pode ser usado como gerenciador de
   contexto.

   Alterado na versão 3.8: Os parâmetros nomeados *mode* e *openhook*
   agora são somente-nomeados.

   Alterado na versão 3.10: Os parâmetros somente-nomeados *encoding*
   e *errors* foram adicionados.

As funções a seguir usam o estado global criado por
"fileinput.input()"; se não houver estado ativo, "RuntimeError" será
levantada.

fileinput.filename()

   Retorna o nome do arquivo que está sendo lido no momento. Antes da
   primeira linha ser lida, retorna "None".

fileinput.fileno()

   Retorna o número inteiro de "descritor de arquivo" para o arquivo
   atual. Quando nenhum arquivo é aberto (antes da primeira linha e
   entre arquivos), retorna "-1".

fileinput.lineno()

   Retorna o número cumulativo da linha que acabou de ser lida. Antes
   da primeira linha ser lida, retorna "0". Após a leitura da última
   linha do último arquivo, retorna o número da linha dessa linha.

fileinput.filelineno()

   Retorna o número da linha no arquivo atual. Antes da primeira linha
   ser lida, retorna "0". Após a leitura da última linha do último
   arquivo, retorna o número da linha dessa linha no arquivo.

fileinput.isfirstline()

   Retorna "True" se a linha que acabou de ler for a primeira linha do
   seu arquivo, caso contrário retorna "False".

fileinput.isstdin()

   Retorna "True" se a última linha foi lida em "sys.stdin", caso
   contrário retorna "False".

fileinput.nextfile()

   Fecha o arquivo atual para que a próxima iteração leia a primeira
   linha do próximo arquivo (se houver); as linhas não lidas do
   arquivo não contarão para a contagem cumulativa de linhas. O nome
   do arquivo não é alterado até que a primeira linha do próximo
   arquivo seja lida. Antes da leitura da primeira linha, esta função
   não tem efeito; ele não pode ser usado para pular o primeiro
   arquivo. Após a leitura da última linha do último arquivo, esta
   função não terá efeito.

fileinput.close()

   Fecha a sequência.

A classe que implementa o comportamento de sequência fornecido pelo
módulo também está disponível para subclasses:

class fileinput.FileInput(files=None, inplace=False, backup='', *, mode='r', openhook=None, encoding=None, errors=None)

   A classe "FileInput" é a implementação; seus métodos "filename()",
   "fileno()", "lineno()", "filelineno()", "isfirstline()",
   "isstdin()", "nextfile()" e "close()" correspondem às funções de
   mesmo nome no módulo. Além disso, é *iterável* e possui um método
   "readline()" que retorna a próxima linha de entrada. A sequência
   deve ser acessada em ordem estritamente sequencial; acesso
   aleatório e "readline()" não podem ser misturados.

   Com *mode* você pode especificar qual modo de arquivo será passado
   para "open()". Deve ser um entre "'r'" e "'rb'".

   O *openhook*, quando fornecido, deve ser uma função que recebe dois
   argumentos, *filename* e *mode*, e retorna um objeto arquivo ou
   similar aberto de acordo. Você não pode usar *inplace* e *openhook*
   juntos.

   Você pode especificar *encoding* e *errors* que são passados para
   "open()" ou *openhook*.

   Uma instância "FileInput" pode ser usada como um gerenciador de
   contexto na instrução "with". Neste exemplo, *input* é fechado após
   a saída da instrução "with", mesmo se ocorrer uma exceção:

      with FileInput(files=('spam.txt', 'eggs.txt')) as input:
          process(input)

   Alterado na versão 3.2: Pode ser usado como gerenciador de
   contexto.

   Alterado na versão 3.8: Os parâmetros nomeados *mode* e *openhook*
   agora são somente-nomeados.

   Alterado na versão 3.10: Os parâmetros somente-nomeados *encoding*
   e *errors* foram adicionados.

   Alterado na versão 3.11: Os modos "'rU'" e "'U'" e o método
   "__getitem__()" foram removidos.

**Filtragem local opcional:** se o argumento nomeado "inplace=True"
for passado para "fileinput.input()" ou para o construtor "FileInput",
o arquivo é movido para um arquivo de backup e a saída padrão é
direcionada para o arquivo de entrada (se já existir um arquivo com o
mesmo nome do arquivo de backup, ele será substituído
silenciosamente). Isso torna possível escrever um filtro que reescreva
seu arquivo de entrada internamente. Se o parâmetro *backup* for
fornecido (normalmente como "backup='.<some extension>'"), ele
especifica a extensão do arquivo de backup, e o arquivo de backup
permanece disponível; por padrão, a extensão é "'.bak'" e é excluída
quando o arquivo de saída é fechado. A filtragem local é desativada
quando a entrada padrão é lida.

Os dois ganchos de abertura a seguir são fornecidos por este módulo:

fileinput.hook_compressed(filename, mode, *, encoding=None, errors=None)

   Abre de forma transparente arquivos compactados com gzip e bzip2
   (reconhecidos pelas extensões "'.gz'" e "'.bz2'") usando os módulos
   "gzip" e "bz2". Se a extensão do nome do arquivo não for "'.gz'" ou
   "'.bz2'", o arquivo é aberto normalmente (ou seja, usando "open()"
   sem qualquer descompactação).

   Os valores *encoding* e *errors* são passados para
   "io.TextIOWrapper" para arquivos compactados e abertos para
   arquivos normais.

   Exemplo de uso: "fi =
   fileinput.FileInput(openhook=fileinput.hook_compressed,
   encoding="utf-8")"

   Alterado na versão 3.10: Os parâmetros somente-nomeados *encoding*
   e *errors* foram adicionados.

fileinput.hook_encoded(encoding, errors=None)

   Retorna um gancho que abre cada arquivo com "open()", usando a
   *encoding* e *errors* fornecidas para ler o arquivo.

   Exemplo de uso: "fi =
   fileinput.FileInput(openhook=fileinput.hook_encoded("utf-8",
   "surrogateescape"))"

   Alterado na versão 3.6: Adicionado o parâmetro opcional *errors*.

   Descontinuado desde a versão 3.10: Esta função foi descontinuado já
   que "fileinput.input()" e "FileInput" agora possuem parâmetros
   *encoding* e *errors*.
