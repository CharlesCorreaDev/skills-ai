Instalando módulos Python
*************************

Como um projeto popular de desenvolvimento de código aberto, Python
tem uma comunidade de apoio ativa de colaboradores e usuários, que
também fazem o seu software disponível para outros desenvolvedores de
Python para usar sob os termos da licença de código aberto.

Isso permite aos usuários Python compartilhar e colaborar
efetivamente, se beneficiando das soluções que outros já tenham criado
para os problemas mais comuns (em alguns casos até mesmo os raros),
bem como potencialmente contribuindo com suas próprias soluções para o
conjunto de soluções comuns.

Este guia cobre a parte do processo de instalação. Para um guia sobre
criar e compartilhar seus próprios projetos Python, confira o Guia de
Usuário para Empacotamento de Python.

Nota:

  Para corporações e outros usuários institucionais, esteja ciente que
  muitas organizações têm suas próprias políticas em relação ao uso e
  contribuição para o software de código aberto. Por favor, leve em
  conta essas políticas ao usar as ferramentas de distribuição e
  instalação fornecidas com o Python.


Termos chave
============

* **pip** é o programa de instalação preferido. Ele é incluído por
  padrão nos instaladores binários do Python.

* Um *ambiente virtual* é um ambiente Python semi-isolado que permite
  que pacotes sejam instalados para uso por uma aplicação específica,
  em vez de serem instaladas em todo o sistema.

* "venv" é a ferramenta padrão para criar ambientes virtuais. O padrão
  é instalar **pip** em todos os ambientes virtuais criados.

* "virtualenv" é uma alternativa de terceiros (e predecessor) ao
  "venv".

* O Python Package Index (PyPI) é um repositório público de pacotes
  licenciados como código aberto e disponíveis para uso de outros
  usuários Python.

* O Python Packaging Authority é o grupo de desenvolvedores e autores
  de documentação responsáveis pela manutenção e evolução das
  ferramentas de empacotamento padrão e os metadados associados e
  padrões de formato de arquivo. Eles mantêm uma variedade de
  ferramentas, documentação e rastreadores de problemas no GitHub.

Alterado na versão 3.5: O uso de "venv" agora é recomendado para a
criação de ambientes virtuais.

Ver também:

  Guia de Usuário para Empacotamento de Python: Criando e usando
  ambientes virtuais


Uso básico
==========

As ferramentas de empacotamento padrão são todas projetadas para serem
usadas na linha de comando.

O comando a seguir instalará a versão mais recente de um módulo e suas
dependências do PyPI:

   python -m pip install AlgumPacote

Nota:

  Para usuários POSIX (incluindo usuários macOS e Linux), os exemplos
  neste guia presumem o uso de um *ambiente virtual*.Para usuários do
  Windows, os exemplos neste guia presumem que a opção de ajustar a
  variável de ambiente PATH do sistema foi selecionada durante a
  instalação do Python.

Também é possível especificar uma versão exata ou mínima diretamente
na linha de comando. Ao usar operadores de comparação como ">", "<" ou
algum outro caractere especial que é interpretado pelo shell, o nome
do pacote e a versão devem ser colocados entre aspas duplas:

   python -m pip install AlgumPacote==1.0.4    # versão específica
   python -m pip install "AlgumPacote>=1.0.4"  # versão mínima

Normalmente, se um módulo adequado já estiver instalado, tentar
instalá-lo novamente não terá efeito. A atualização de módulos
existentes deve ser solicitada explicitamente:

   python -m pip install --upgrade AlgumPacote

Mais informações e recursos sobre o **pip** e seus recursos podem ser
encontrados no Python Packaging User Guide.

A criação de ambientes virtuais é feita através do módulo "venv". A
instalação de pacotes em um ambiente virtual ativo usa os comandos
mostrados acima.

Ver também:

  Guia de Usuário para Empacotamento de Python: Instalando pacotes
  Python de distribuição


Como eu ...?
============

Estas são respostas rápidas ou links para algumas tarefas comuns.


... instalo pacotes apenas para o usuário atual?
------------------------------------------------

Passar a opção "--user" para "python -m pip install" irá instalar um
pacote apenas para o usuário atual, ao invés de para todos os usuários
do sistema.


... instalo pacotes científicos do Python?
------------------------------------------

Vários pacotes científicos do Python têm dependências binárias
complexas e atualmente não são fáceis de instalar usando o **pip**
diretamente. Frequentemente será mais fácil para os usuários
instalarem esses pacotes por outros meios ao invés de tentar
instalá-los com **pip**.

Ver também:

  Guia de Usuário para Empacotamento de Python: Instalando pacotes
  científicos


... trabalho com várias versões do Python instaladas em paralelo?
-----------------------------------------------------------------

No Linux, macOS e outros sistemas POSIX, use os comandos Python com
versão em combinação com a opção "-m" para executar a cópia apropriada
de **pip**:

   python3    -m pip install AlgumPacote  # Python 3 padrão
   python3.14 -m pip install AlgumPacote  # Python 3.14 especificamente

Comandos **pip** com versão apropriada também podem estar disponíveis.

No Windows, use o iniciador Python **py** em combinação com a opção
"-m":

   py -3    -m pip install AlgumPacote  # Python 3 padrão
   py -3.14 -m pip install AlgumPacote  # Python 3.14 especificamente


Problemas comuns de instalação
==============================


Instalando no sistema Python no Linux
-------------------------------------

Em sistemas Linux, uma instalação Python normalmente será incluída
como parte da distribuição. A instalação nesta instalação Python
requer acesso root ao sistema, e pode interferir na operação do
gerenciador de pacotes do sistema e outros componentes do sistema se
um componente for atualizado inesperadamente usando **pip**.

Em tais sistemas, geralmente é melhor usar um ambiente virtual ou uma
instalação por usuário ao instalar pacotes com **pip**.


Pip não instalado
-----------------

É possível que o **pip** não seja instalado por padrão. Uma solução
potencial é:

   python -m ensurepip --default-pip

Existem também recursos adicionais para instalar pip..


Instalando extensões binárias
-----------------------------

Antigamente, o Python dependia fortemente da distribuição baseada em
código-fonte, e esperava-se que os usuários finais compilassem módulos
de extensão a partir do código-fonte como parte do processo de
instalação.

Com a introdução do formato binário *wheel* e a possibilidade de
publicar *wheels* no PyPI, esse problema vem diminuindo, uma vez que
os usuários conseguem instalar extensões pré-construídas com mais
frequência, em vez de precisarem construí-las eles mesmos.

Algumas das soluções para instalar softwares científicos que ainda não
estão disponíveis como arquivos *wheel* pré-construídos também podem
ajudar a obter outras extensões binárias sem a necessidade para
construí-los localmente.

Ver também:

  Guia de Usuário para Empacotamento de Python: Extensões binárias
