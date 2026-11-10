Acesso a arquivos e diretórios
******************************

Os módulos descritos neste capítulo dizem respeito aos arquivos e
diretórios no disco. Por exemplo, existem módulos para ler as
propriedades dos arquivos, manipular o caminhos de forma
multiplataforma e para criar arquivos temporários. A lista completa de
módulos neste capítulo é:

* "pathlib" --- Caminhos do sistema de arquivos orientados a objetos

  * Uso básico

  * Exceções

  * Caminhos puros

    * Propriedades gerais

    * Operadores

    * Acessando partes individuais

    * Métodos e propriedades

  * Caminhos concretos

    * Analisando e gerando URIs

    * Expandindo e resolvendo caminhos

    * Consultando tipo de arquivo e status

    * Lendo e escrevendo arquivos

    * Lendo diretórios

    * Criando arquivos e diretórios

    * Copiando, movendo e excluindo

    * Permissões e propriedade

  * Linguagem de padrões

  * Comparação com o módulo "glob"

  * Comparação com os módulos "os" e "os.path"

    * Ferramentas correspondentes

  * Protocolos

* "os.path" --- Manipulações comuns de nomes de caminhos

* "stat" --- Interpretando resultados de "stat()"

* "filecmp" --- Comparações de arquivos e diretórios

  * A classe "dircmp"

* "tempfile" --- Gera arquivos temporários e diretórios

  * Exemplos

  * Deprecated functions and variables

* "glob" --- Expansão de padrão de nome de arquivo no estilo Unix

  * Exemplos

* "fnmatch" --- Correspondência de padrões de nome de arquivo Unix

* "linecache" --- Acesso aleatório a linhas de texto

* "shutil" --- Operações de arquivo de alto nível

  * Operações de diretório e arquivos

    * Operações de cópia eficientes dependentes da plataforma

    * Exemplo de copytree

    * exemplo rmtree

  * Operações de arquivamento

    * Exemplo de arquivo

    * Exemplo de arquivamento com *base_dir*

  * Consultando o tamanho do terminal de saída

Ver também:

  Módulo "os"
     Interfaces do sistema operacional, incluindo funções para
     trabalhar com arquivos num nível inferior a *objetos arquivos* do
     Python.

  Módulo "io"
     A biblioteca embutida de E/S do Python, incluindo as classes
     abstratas e algumas classes concretas, como E/S de arquivos.

  Função embutida "open()"
     A maneira padrão de abrir arquivos para ler e escrever em Python.
