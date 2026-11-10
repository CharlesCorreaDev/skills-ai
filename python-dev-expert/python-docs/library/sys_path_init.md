A inicialização do caminho de pesquisa de módulos "sys.path"
************************************************************

Um caminho de pesquisa de módulos é inicializado quando o Python é
iniciado. Este caminho de pesquisa de módulos pode ser acessado em
"sys.path".

A primeira entrada no caminho de pesquisa de módulos é o diretório que
contém o script de entrada, se houver. Caso contrário, a primeira
entrada é o diretório atual, que é o caso ao executar o console
interativo, um comando com "-c" ou um módulo com "-m".

A variável de ambiente "PYTHONPATH" é frequentemente usada para
adicionar diretórios ao caminho de pesquisa. Se esta variável de
ambiente for encontrada, o conteúdo será adicionado ao caminho de
pesquisa de módulos.

Nota:

  "PYTHONPATH" afetará todas as versões/ambientes Python instalados.
  Tenha cuidado ao definir isso em seu perfil do shell ou em variáveis
  de ambiente globais. O módulo "site" oferece técnicas mais
  diferenciadas, conforme mencionado abaixo.

Os próximos itens adicionados são os diretórios contendo módulos
padrão do Python, bem como quaisquer *módulos de extensão* dos quais
esses módulos dependem. Módulos de extensão são arquivos ".pyd" no
Windows e arquivos ".so" em outras plataformas. O diretório com os
módulos Python independentes de plataforma é chamado "prefix". O
diretório com os módulos de extensão é chamado "exec_prefix".

A variável de ambiente "PYTHONHOME" pode ser usada para definir os
locais "prefix" e "exec_prefix". Caso contrário, esses diretórios
serão encontrados usando o executável Python como ponto de partida e,
em seguida, procurando por vários arquivos e diretórios "de
referência". Observe que todos os links simbólicos são seguidos para
que o local real do executável do Python seja usado como ponto de
partida da pesquisa. O local do executável do Python é chamado "home".

Uma vez que "home" é determinado, o diretório "prefix" é encontrado
procurando primeiro por "python*majorversion**minorversion*.zip"
("python311.zip"). No Windows, o arquivo zip é procurado em "home" e
no Unix espera-se que o arquivo esteja em "lib". Observe que o local
esperado do arquivo zip é adicionado ao caminho de pesquisa de
módulos, mesmo que o arquivo não exista. Se nenhum arquivo for
encontrado, o Python no Windows continuará a pesquisa por "prefix"
procurando por "Lib\os.py". Python no Unix procurará por
"lib/python*majorversion*.*minorversion*/os.py"
("lib/python3.11/os.py"). No Windows, "prefix" e "exec_prefix" são
iguais, porém em outras plataformas
"lib/python*majorversion*.*minorversion*/lib-dynload" ("lib/python3.11
/lib-dynload") é pesquisado e usado como âncora para "exec_prefix". Em
algumas plataformas, "lib" pode ser "lib64" ou outro valor, veja
"sys.platlibdir" e "PYTHONPLATLIBDIR".

Uma vez encontrados, "prefix" e "exec_prefix" estão disponíveis em
"sys.base_prefix" e "sys.base_exec_prefix", respectivamente.

Se "PYTHONHOME" não estiver definido e um arquivo "pyvenv.cfg" for
encontrado ao lado do executável principal ou em seu diretório pai,
"sys.prefix" e "sys.exec_prefix" serão definidos para o diretório que
contém "pyvenv.cfg"; caso contrário, serão definidos com o mesmo valor
que "sys.base_prefix" e "sys.base_exec_prefix", respectivamente. Isso
é usado por Ambientes virtuais.

Finally, the "site" module is processed and "site-packages"
directories are added to the module search path.  The "PYTHONUSERBASE"
environment variable controls where is searched for user site-packages
and the "PYTHONNOUSERSITE" environment variable prevents searching for
user site-packages all together.  A common way to customize the search
path is to create "sitecustomize" or "usercustomize" modules as
described in the "site" module documentation.

Nota:

  The command line options "-E", "-P", "-I", "-S" and "-s" further
  affect path calculations, see their documentation for details.

Alterado na versão 3.14: "sys.prefix" e "sys.exec_prefix" agora são
definidos para o diretório "pyvenv.cfg" durante a inicialização do
caminho. Isso era feito anteriormente por "site" e, portanto, afetado
por "-S".


Ambientes virtuais
==================

Ambientes virtuais colocam um arquivo "pyvenv.cfg" em seu prefixo, o
que faz com que "sys.prefix" e "sys.exec_prefix" apontem para eles, em
vez da instalação base.

Os valores "prefix" e "exec_prefix" da instalação base estão
disponíveis em "sys.base_prefix" e "sys.base_exec_prefix".

Além de ser usado como um marcador para identificar ambientes
virtuais, "pyvenv.cfg" também pode ser usado para configurar a
inicialização do "site". Consulte a documentação de ambientes virtuais
do "site".

Nota:

  "PYTHONHOME" substitui a detecção "pyvenv.cfg".

Nota:

  There are other ways "virtual environments" could be implemented.
  This documentation refers to implementations based on the
  "pyvenv.cfg" mechanism, such as "venv", that many virtual
  environment implementations follow.


Arquivos _pth
=============

Para substituir completamente "sys.path", crie um arquivo "._pth" com
o mesmo nome da biblioteca compartilhada ou executável ("python._pth"
ou "python311._pth"). O caminho da biblioteca compartilhada é sempre
conhecido no Windows, mas pode não estar disponível em outras
plataformas. No arquivo "._pth", especifique uma linha para cada
caminho a ser adicionado a "sys.path". O arquivo baseado no nome da
biblioteca compartilhada substitui aquele baseado no executável, o que
permite que os caminhos sejam restritos para qualquer programa que
carregue o tempo de execução, se desejado.

Quando o arquivo existe, todos os registros e variáveis de ambiente
são ignorados, o modo isolado é ativado, e "site" não é importado a
menos que uma linha do arquivo especifique "import site". Caminhos em
branco e linhas começando com "#" são ignorados. Cada caminho pode ser
absoluto ou relativo ao local do arquivo. Instruções de importação
diferente de "site" não são permitidas, e código arbitrário não pode
ser especificado.

Note que arquivos ".pth" (sem o sublinhado no início) serão
processados normalmente pelo módulo "site" quando "import site" tiver
sido especificado.


Python embarcado
================

Se o Python estiver incorporado em outra aplicação,
"Py_InitializeFromConfig()" e a estrutura "PyConfig" podem ser usados
para inicializar o Python. Os detalhes específicos do caminho estão
descritos em Python Path Configuration.

Ver também:

  * Encontrando módulos para observações detalhadas do Windows.

  * Utilizando Python em plataformas Unix para detalhes do Unix.
