"py_compile" --- Compila arquivos fonte do Python
*************************************************

**Código-fonte:** Lib/py_compile.py

======================================================================

O módulo "py_compile" fornece uma função para gerar um arquivo de
bytecode a partir de um arquivo fonte, e outra função usada quando o
arquivo fonte do módulo é invocado como um script.

Embora nem sempre seja necessária, essa função pode ser útil ao
instalar módulos para uso compartilhado, especialmente se alguns
usuários não tiverem permissão para gravar os arquivos de cache de
bytecodes no diretório que contém o código-fonte.

exception py_compile.PyCompileError

   Exceção levantada quando ocorre um erro ao tentar compilar o
   arquivo.

py_compile.compile(file, cfile=None, dfile=None, doraise=False, optimize=-1, invalidation_mode=PycInvalidationMode.TIMESTAMP, quiet=0)

   Compila um arquivo fonte para bytecode e grava o arquivo de cache
   de bytecode. O código-fonte é carregado a partir do arquivo chamado
   *file*. O bytecode é gravado em *cfile*, cujo padrão é o caminho
   **PEP 3147**/**PEP 488**, terminando em ".pyc". Por exemplo, se
   *file* for "/foo/bar/baz.py", o *cfile* será padronizado como
   "/foo/bar/__pycache__/baz.cpython-32.pyc" para o Python 3.2. Se
   *dfile* for especificado, ele será usado em vez de *file* como o
   nome do arquivo fonte do qual as linhas de origem são obtidas para
   exibição em tracebacks de exceção. Se *doraise* for verdadeiro, a
   "PyCompileError" será levantada quando um erro for encontrado
   durante a compilação de *file*. Se *doraise* for false (o padrão),
   uma string de erros será gravada em "sys.stderr", mas nenhuma
   exceção será levantada. Essa função retorna o caminho para o
   arquivo compilado em bytes, ou seja, qualquer valor *cfile* foi
   usado.

   Os argumentos *doraise* e *quiet* determinam como os erros são
   tratados durante a compilação do arquivo. Se *quiet* for 0 ou 1 e
   *doraise* for false, o comportamento padrão será ativado: uma
   string de erros será gravada em "sys.stderr" e a função retornará
   "None" em vez de um caminho. Se *doraise* for verdadeiro, uma
   "PyCompileError" será levantada. No entanto, se *quiet* for 2,
   nenhuma mensagem será escrita e *doraise* não terá efeito.

   Se o caminho que *cfile* se tornar (especificado ou computado
   explicitamente) for um link simbólico ou um arquivo não regular,
   "FileExistsError" será levantada. Isso serve como um aviso de que a
   importação transformará esses caminhos em arquivos regulares se for
   permitido gravar arquivos compilados em bytes nesses caminhos. Esse
   é um efeito colateral da importação usando a renomeação de arquivo
   para colocar o arquivo final compilado em bytecode para evitar
   problemas de gravação simultânea de arquivos.

   *optimize* controla o nível de otimização e é passado para a função
   embutida "compile()". O padrão de "-1" seleciona o nível de
   otimização do interpretador atual.

   *invalidation_mode* deve ser um membro da enum
   "PycInvalidationMode" e controla como o cache do bytecode gerado é
   invalidado em tempo de execução. O padrão é
   "PycInvalidationMode.CHECKED_HASH" se a variável de ambiente
   "SOURCE_DATE_EPOCH" estiver configurada, caso contrário, o padrão é
   "PycInvalidationMode.TIMESTAMP".

   Alterado na versão 3.2: Alterado o valor padrão de *cfile* para
   ficar em conformidade com a **PEP 3147**. O padrão anterior era
   *file* + "'c'" ("'o'" se a otimização estivesse ativada). Também
   foi adicionado o parâmetro *optimize*.

   Alterado na versão 3.4: Alterado o código para usar "importlib"
   para a gravação do arquivo de cache do bytecode. Isso significa que
   a semântica de criação/gravação de arquivo agora corresponde ao que
   "importlib" faz, por exemplo, permissões, semântica de gravação e
   movimentação, etc. Também foi adicionada a ressalva de que
   "FileExistsError" é levantada se *cfile* for um link simbólico ou
   um arquivo não regular.

   Alterado na versão 3.7: O parâmetro *invalidation_mode* foi
   adicionado conforme especificado em **PEP 552**. Se a variável de
   ambiente "SOURCE_DATE_EPOCH" estiver configurada,
   *invalidation_mode* será forçado a
   "PycInvalidationMode.CHECKED_HASH".

   Alterado na versão 3.7.2: A variável de ambiente
   "SOURCE_DATE_EPOCH" não substitui mais o valor do argumento
   *invalidation_mode* e, em vez disso, determina seu valor padrão.

   Alterado na versão 3.8: O parâmetro *quiet* foi adicionado.

class py_compile.PycInvalidationMode

   Uma enumeração de métodos possíveis que o interpretador pode usar
   para determinar se um arquivo de bytecode está atualizado com um
   arquivo fonte. O arquivo ".pyc" indica o modo de invalidação
   desejado em seu cabeçalho. Veja Invalidação de bytecode em cache
   para obter mais informações sobre como o Python invalida arquivos
   ".pyc" em tempo de execução.

   Adicionado na versão 3.7.

   TIMESTAMP

      O arquivo ".pyc" inclui o carimbo de data e hora e o tamanho do
      arquivo fonte, que o Python comparará com os metadados do
      arquivo fonte no tempo de execução para determinar se o arquivo
      ".pyc" precisa ser gerado novamente.

   CHECKED_HASH

      O arquivo ".pyc" inclui um hash do conteúdo do arquivo fonte,
      com o qual o Python comparará o fonte em tempo de execução para
      determinar se o arquivo ".pyc" precisa ser gerado novamente.

   UNCHECKED_HASH

      Como "CHECKED_HASH", o arquivo ".pyc" inclui um hash do conteúdo
      do arquivo fonte. No entanto, em tempo de execução, o Python
      presumirá que o arquivo ".pyc" está atualizado e não validará o
      ".pyc" contra o arquivo fonte.

      Essa opção é útil quando os ".pycs" são atualizados por algum
      sistema externo ao Python, como um sistema de compilação.


Interface de Linha de Comando
=============================

Este módulo pode ser invocado como um script para compilar vários
arquivos fonte. Os arquivos nomeados em *filenames* são compilados e o
bytecode resultante é armazenado em cache da maneira normal. Este
programa não pesquisa uma estrutura de diretórios para localizar
arquivos de origem; ele apenas compila arquivos nomeados
explicitamente. O status de saída será diferente de zero se um dos
arquivos não puder ser compilado.

<file> ... <fileN>
-

   Argumentos posicionais são arquivos para compilar. Se "-" for o
   único parâmetro, a lista de arquivos será obtida da entrada padrão.

-q, --quiet

   Suprime a saída de erros.

Alterado na versão 3.2: Adicionado suporte a "-".

Alterado na versão 3.10: Adicionado suporte a "-q".

Ver também:

  Módulo "compileall"
     Utilitários para compilar todos os arquivos fontes Python em uma
     árvore de diretórios.
