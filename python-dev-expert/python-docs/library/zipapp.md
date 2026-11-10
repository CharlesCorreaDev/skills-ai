"zipapp" --- Gerencia arquivos zip executáveis do Python
********************************************************

Adicionado na versão 3.5.

**Código-fonte:** Lib/zipapp.py

======================================================================

Este módulo fornece ferramentas para gerenciar a criação de arquivos
zip contendo código Python, que pode ser executado diretamente pelo
interpretador Python. O módulo fornece uma Interface de linha de
comando e uma API do Python.


Exemplo básico
==============

O exemplo a seguir mostra como a Interface de linha de comando pode
ser usada para criar um arquivo executável a partir de um diretório
contendo código Python. Quando executado, o arquivo executará a função
"main" do módulo "myapp" no arquivo.

   $ python -m zipapp myapp -m "myapp:main"
   $ python myapp.pyz
   <output from myapp>


Interface de linha de comando
=============================

Quando chamado como um programa a partir da linha de comando, as
seguintes opções estão disponíveis:

   $ python -m zipapp source [options]

Se *source* for um diretório, isso criará um arquivo a partir do
conteúdo de *source*. Se *source* for um arquivo, ele deve ser um
arquivo, e será copiado para o arquivo de destino (ou o conteúdo de
sua linha shebang será exibido se a opção --info for especificada).

As seguintes opções são compreendidas:

-o <output>, --output=<output>

   Escreve a saída em um arquivo chamado *output*. Se essa opção não
   for especificada, o nome do arquivo de saída será o mesmo que o
   *source* de entrada, com a extensão ".pyz" adicionada. Se um nome
   de arquivo explícito for fornecido, ele será usado como está (então
   uma extensão ".pyz" deve ser incluída se necessário).

   Um nome de arquivo de saída deve ser especificado se *source* for
   um arquivo (e nesse caso, *output* não deve ser o mesmo que
   *source*).

-p <interpreter>, --python=<interpreter>

   Adiciona uma linha "#!" ao arquivo especificando *interpreter* como
   o comando a ser executado. Além disso, no POSIX, torne o arquivo
   executável. O padrão é não escrever nenhuma linha "#!" e não tornar
   o arquivo executável.

-m <mainfn>, --main=<mainfn>

   Escreve um arquivo "__main__.py" no arquivo que executa *mainfn*. O
   argumento *mainfn* deve ter o formato "pkg.mod:fn", onde "pkg.mod"
   é um pacote/módulo no arquivo, e "fn" é um chamável no módulo
   fornecido. O arquivo "__main__.py" executará esse chamável.

   "--main" não pode ser especificado ao copiar um arquivo.

-c, --compress

   Compacta arquivos com o método deflate, reduzindo o tamanho do
   arquivo de saída. Por padrão, os arquivos são armazenados
   descompactados no arquivo.

   "--compress" não tem efeito ao copiar um arquivo.

   Adicionado na versão 3.7.

--info

   Exibe o interpretador incorporado no arquivo, para fins de
   diagnóstico. Neste caso, quaisquer outras opções são ignoradas e
   SOURCE deve ser um arquivo, não um diretório.

-h, --help

   Exibe uma mensagem curta de uso e sai


API do Python
=============

O módulo define duas funções de conveniência:

zipapp.create_archive(source, target=None, interpreter=None, main=None, filter=None, compressed=False)

   Cria um arquivo de aplicação a partir de *source*. A fonte pode ser
   qualquer um dos seguintes:

   * O nome de um diretório, ou um *objeto caminho ou similar*
     referente a um diretório, caso em que um novo arquivo de
     aplicação será criado a partir do conteúdo desse diretório.

   * O nome de um arquivo de aplicação existente, ou um *objeto
     caminho ou similar* referindo-se a tal arquivo, em cujo caso o
     arquivo é copiado para o alvo (modificando-o para refletir o
     valor dado para o argumento *interpreter*). O nome do arquivo
     deve incluir a extensão ".pyz", se necessário.

   * Um objeto arquivo aberto para leitura no modo bytes. O conteúdo
     do arquivo deve ser um arquivo de aplicação, e o objeto arquivo é
     presumido como estando posicionado no início do arquivo.

   O argumento *target* determina onde o arquivo resultante será
   escrito:

   * Se for o nome de um arquivo ou um *objeto caminho ou similar*, o
     arquivo será escrito nesse arquivo.

   * Se for um objeto arquivo aberto, o arquivo será escrito naquele
     objeto arquivo, que deve estar aberto para escrita no modo bytes.

   * Se o destino for omitido (ou "Nenhum"), a fonte deverá ser um
     diretório e o destino será um arquivo com o mesmo nome da fonte,
     com uma extensão ".pyz" adicionada.

   O argumento *interpreter* especifica o nome do interpretador Python
   com o qual o arquivo será executado. Ele é escrito como uma linha
   "shebang" no início do arquivo. No POSIX, isso será interpretado
   pelo sistema operacional, e no Windows será manipulado pelo
   inicializador Python. Omitir o *interpreter* resulta em nenhuma
   linha shebang sendo escrita. Se um interpretador for especificado,
   e o alvo for um nome de arquivo, o bit executável do arquivo alvo
   será definido.

   O argumento *main* especifica o nome de um chamável que será usado
   como o programa principal para o arquivo. Ele só pode ser
   especificado se a fonte for um diretório, e a fonte ainda não
   contiver um arquivo "__main__.py". O argumento *main* deve ter o
   formato "pkg.módulo:chamável" e o arquivo será executado importando
   "pkg.módulo" e executando o chamável fornecido sem argumentos. É um
   erro omitir *main* se a fonte for um diretório e não contiver um
   arquivo "__main__.py", pois, caso contrário, o arquivo resultante
   não seria executável.

   O argumento opcional *filter* especifica uma função de retorno de
   chamada que recebe um objeto Path representando o caminho para o
   arquivo que está sendo adicionado (relativo ao diretório da fonte).
   Ele deve retornar "True" se o arquivo for adicionado.

   O argumento opcional *compressed* determina se os arquivos são
   compactados. Se definido como "True", os arquivos no arquivo são
   compactados com o método deflate; caso contrário, os arquivos são
   armazenados descompactados. Este argumento não tem efeito ao copiar
   um arquivo existente.

   Se um objeto arquivo for especificado para *source* ou *target*, é
   responsabilidade do chamador fechá-lo após chamar create_archive.

   Ao copiar um arquivo existente, os objetos arquivo fornecidos
   precisam apenas dos métodos "read" e "readline" ou "write". Ao
   criar um arquivo de um diretório, se o alvo for um objeto arquivo,
   ele será passado para a classe "zipfile.ZipFile" e deve fornecer os
   métodos necessários para essa classe.

   Alterado na versão 3.7: Adicionados os parâmetros *filter* e
   *compressed*.

zipapp.get_interpreter(archive)

   Retorna o interpretador especificado na linha "#!" no início do
   arquivo. Se não houver nenhuma linha "#!", retorna "None". O
   argumento *archive* pode ser um nome de arquivo ou um objeto
   arquivo ou similar aberto para leitura no modo bytes. É presumido
   esteja no início do arquivo.


Exemplos
========

Compacte um diretório em um arquivo e execute-o.

   $ python -m zipapp myapp
   $ python myapp.pyz
   <output from myapp>

O mesmo pode ser feito usando a função "create_archive()":

   >>> import zipapp
   >>> zipapp.create_archive('myapp', 'myapp.pyz')

Para tornar o aplicativo diretamente executável no POSIX, especifique
um interpretador a ser usado.

   $ python -m zipapp myapp -p "/usr/bin/env python"
   $ ./myapp.pyz
   <saída de myapp>

Para substituir a linha shebang em um arquivo existente, crie um
arquivo modificado usando a função "create_archive()":

   >>> import zipapp
   >>> zipapp.create_archive('old_archive.pyz', 'new_archive.pyz', '/usr/bin/python3')

Para atualizar o arquivo no local, faça a substituição na memória
usando um objeto "BytesIO" e, em seguida, sobrescreva a fonte depois.
Observe que há um risco ao sobrescrever um arquivo no local de que um
erro resultará na perda do arquivo original. Este código não protege
contra tais erros, mas o código de produção deve fazê-lo. Além disso,
este método só funcionará se o arquivo couber na memória:

   >>> import zipapp
   >>> import io
   >>> temp = io.BytesIO()
   >>> zipapp.create_archive('myapp.pyz', temp, '/usr/bin/python2')
   >>> with open('myapp.pyz', 'wb') as f:
   ...     f.write(temp.getvalue())


Especificando o interpretador
=============================

Observe que se você especificar um interpretador e então distribuir
seu arquivo de aplicação, você precisa garantir que o interpretador
usado seja portátil. O inicializador Python para Windows oferece
suporte às formas mais comuns da linha POSIX "#!", mas há outras
questões a serem consideradas:

* Se você usar "/usr/bin/env python" (ou outras formas do comando
  "python", como "/usr/bin/python"), você precisa considerar que seus
  usuários podem ter Python 2 ou Python 3 como padrão, e escrever seu
  código para funcionar em ambas as versões.

* Se você usar uma versão explícita, por exemplo "/usr/bin/env
  python3", sua aplicação não funcionará para usuários que não tenham
  essa versão. (Isso pode ser o que você quer se não tiver tornado seu
  código compatível com Python 2).

* Não há como dizer "python X.Y ou posterior", então tome cuidado ao
  usar uma versão exata como "/usr/bin/env python3.4", pois você
  precisará alterar sua linha shebang para usuários do Python 3.5, por
  exemplo.

Normalmente, você deve usar "/usr/bin/env python2" ou "/usr/bin/env
python3", dependendo se seu código foi escrito para Python 2 ou 3.


Criando aplicações autônomas com zipapp
=======================================

Usando o módulo "zipapp", é possível criar programas Python
autocontidos, que podem ser distribuídos para usuários finais que
precisam apenas ter uma versão adequada do Python instalada em seu
sistema. A chave para fazer isso é agrupar todas as dependências da
aplicação no arquivo, junto com o código da aplicação.

As etapas para criar um arquivo autônomo são as seguintes:

1. Crie sua aplicação em um diretório normalmente, para que você tenha
   um diretório "myapp" contendo um arquivo "__main__.py" e qualquer
   código de aplicação de suporte.

2. Instale todas as dependências da sua aplicação no diretório
   "myapp", usando pip:

      $ python -m pip install -r requirements.txt --target myapp

   (isso presume que você tenha os requisitos do seu projeto em um
   arquivo "requirements.txt" - caso contrário, você pode simplesmente
   listar as dependências manualmente na linha de comando do pip).

3. Empacote a aplicação usando:

      $ python -m zipapp -p "interpreter" myapp

Isso produzirá um executável autônomo, que pode ser executado em
qualquer máquina com o interpretador apropriado disponível. Veja
Especificando o interpretador para detalhes. Ele pode ser enviado aos
usuários como um único arquivo.

No Unix, o arquivo "myapp.pyz" é executável como está. Você pode
renomear o arquivo para remover a extensão ".pyz" se preferir um nome
de comando "simples". No Windows, o arquivo "myapp.pyz[w]" é
executável em virtude do fato de que o interpretador Python registra
as extensões de arquivo ".pyz" e ".pyzw" quando instalado.


Advertência
-----------

Se sua aplicação depende de um pacote que inclui uma extensão C, esse
pacote não pode ser executado a partir de um arquivo zip (essa é uma
limitação do sistema operacional, pois o código executável deve estar
presente no sistema de arquivos para que o carregador do sistema
operacional o carregue). Nesse caso, você pode excluir essa
dependência do arquivo zip e exigir que seus usuários o tenham
instalado ou enviá-lo junto com seu arquivo zip e adicionar código ao
seu "__main__.py" para incluir o diretório que contém o módulo
descompactado em "sys.path". Nesse caso, você precisará certificar-se
de enviar binários apropriados para sua(s) arquitetura(s) de destino
(e potencialmente escolher a versão correta para adicionar ao
"sys.path" no tempo de execução, com base na máquina do usuário).


O formato de arquivo da aplicação zip Python
============================================

O Python tem sido capaz de executar arquivos zip que contêm um arquivo
"__main__.py" desde a versão 2.6. Para ser executado pelo Python, um
arquivo de aplicação simplesmente tem que ser um arquivo zip padrão
contendo um arquivo "__main__.py" que será executado como o ponto de
entrada para o aplicativo. Como de costume para qualquer script
Python, o pai do script (neste caso, o arquivo zip) será colocado em
"sys.path" e, portanto, outros módulos podem ser importados do arquivo
zip.

O formato de arquivo zip permite que dados arbitrários sejam
prefixados a um arquivo zip. O formato de aplicação zip usa essa
habilidade para prefixar uma linha "shebang" padrão POSIX ao arquivo
("#!/caminho/para/interpretador").

Formalmente, o formato de aplicação zip Python é:

1. Uma linha shebang opcional, contendo os caracteres "b'#!'" seguidos
   por um nome de interpretador e, em seguida, um caractere de nova
   linha ("b'\n'"). O nome do interpretador pode ser qualquer coisa
   aceitável para o processamento "shebang" do sistema operacional ou
   o inicializador Python no Windows. O interpretador deve ser
   codificado em UTF-8 no Windows e em "sys.getfilesystemencoding()"
   no POSIX.

2. Dados padrão do zipfile, conforme gerados pelo módulo "zipfile". O
   conteúdo do zipfile *deve* incluir um arquivo chamado "__main__.py"
   (que deve estar na "raiz" do zipfile - ou seja, não pode estar em
   um subdiretório). Os dados do zipfile podem ser compactados ou
   descompactados.

Se um arquivo de aplicação tiver uma linha shebang, ele poderá ter o
bit executável definido em sistemas POSIX, para permitir que seja
executado diretamente.

Não há exigência de que as ferramentas neste módulo sejam usadas para
criar arquivos de aplicações - o módulo é uma conveniência, mas
arquivos no formato acima criados por qualquer meio são aceitáveis
para Python.
