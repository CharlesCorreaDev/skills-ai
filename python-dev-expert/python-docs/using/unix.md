2. Utilizando Python em plataformas Unix
****************************************


2.1. Obtendo e instalando a versão mais recente do Python
=========================================================


2.1.1. No Linux
---------------

O Python vem pré-instalado na maioria das distribuições Linux e está
disponível como um pacote em todas as outras. No entanto, há certos
recursos que você pode querer usar que não estão disponíveis no pacote
da sua distribuição. Você pode compilar a versão mais recente do
Python a partir do código-fonte.

No caso de a versão mais recente do Python não vir pré-instalada e não
estar nos repositórios também, você pode criar pacotes para sua
própria distro. Dê uma olhada nos seguintes links:

Ver também:

  https://www.debian.org/doc/manuals/maint-guide/first.en.html
     para usuários Debian

  https://en.opensuse.org/Portal:Packaging
     para usuários OpenSuse

  https://docs.fedoraproject.org/en-US/package-
  maintainers/Packaging_Tutorial_GNU_Hello/
     para usuários Fedora

  https://slackbook.org/html/package-management-making-packages.html
     para usuários do Slackware


2.1.1.1. Instalação do IDLE
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Em alguns casos, o IDLE pode não estar incluído em sua instalação do
Python.

* Para usuários do Debian e do Ubuntu:

     sudo apt update
     sudo apt install idle

* Para usuários do Fedora, RHEL e CentOS:

     sudo dnf install python3-idle

* Para usuários do SUSE e do OpenSUSE:

     sudo zypper install python3-idle

* Para usuários do Alpine Linux:

     sudo apk add python3-idle


2.1.2. No FreeBSD e OpenBSD
---------------------------

* usuários do FreeBSD, para adicionar a utilização do pacote utilize:

     pkg install python3

* Usuários do OpenBSD, para adicionar pacotes use:

     pkg_add -r python

     pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/<insert your architecture here>/python-<version>.tgz

  Por exemplo, usuários i386 podem pegar a versão 2.5.1 do Python
  usando o comando:

     pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/i386/python-2.5.1p2.tgz


2.2. Compilando o Python
========================

Ver também:

  Se você deseja contribuir com o CPython, consulte o devguide, que
  inclui instruções de construção e outras dicas sobre como configurar
  o ambiente.

Se você quer compilar o CPython, a primeira coisa que você precisa
fazer é baixar o código-fonte. Você pode baixar a última versão ou
obter um clone atualizado. Você também pode querer instalar os
requisitos de construção.

O processo de compilação consiste nos comandos usuais:

   ./configure
   make
   make install

Opções de configuração e advertências para plataformas específicas do
Unix estão amplamente documentadas no arquivo README.rst na raiz da
árvore de fontes Python.

Aviso:

  "make install" pode sobrescrever ou mascarar o arquivo binário
  "python3". "make altinstall" é, portanto, recomendado ao invés de
  "make install" uma vez que o mesmo apenas instala o arquivo
  "*exec_prefix*/bin/python*version*".


2.3. Paths e arquivos relacionados com o Python
===============================================

Estes estão sujeitos a diferenças dependendo das convenções de
instalação local; "prefix" e "exec_prefix" dependem da instalação e
devem ser interpretados da mesma forma que para o software GNU; eles
poderão ser os mesmos.

Por exemplo, na maioria dos sistemas Linux, o padrão para ambos é
"/usr".

+-------------------------------------------------+--------------------------------------------+
| Arquivo/diretório                               | Significado                                |
|=================================================|============================================|
| "*exec_prefix*/bin/python3"                     | Localização recomendada do interpretador.  |
+-------------------------------------------------+--------------------------------------------+
| "*prefix*/lib/python*version*",                 | A localização recomendada dos diretórios   |
| "*exec_prefix*/lib/python*version*"             | contendo os módulos padrão.                |
+-------------------------------------------------+--------------------------------------------+
| "*prefix*/include/python*version*",             | Localizações recomendadas dos diretórios   |
| "*exec_prefix*/include/python*version*"         | contendo os arquivos de inclusão           |
|                                                 | necessários para o desenvolvimento de      |
|                                                 | extensões Python e incorporação do         |
|                                                 | interpretador.                             |
+-------------------------------------------------+--------------------------------------------+


2.4. Diversos
=============

Para usar facilmente scripts Python no Unix, você precisa torná-los
executáveis, por exemplo, com

   $ chmod +x script

e colocar uma linha Shebang apropriada no topo do script. Uma boa
escolha normalmente é

   #!/usr/bin/env python3

que procura o interpretador do Python no conjunto "PATH". No entanto,
alguns sistemas Unix podem não ter o comando **env**, então você pode
precisar codificar "/usr/bin/python3" como o caminho do interpretador.

Para usar comandos Shell em seus scripts Python, veja o módulo
"subprocess".


2.5. OpenSSL personalizado
==========================

1. Para usar a configuração OpenSSL do seu fornecedor e armazenamento
   confiável do sistema, localize o diretório com o arquivo
   "openssl.cnf" ou link simbólico em "/etc". Na maioria das
   distribuições o arquivo está em "/etc/ssl" ou em "/etc/pki/tls". O
   diretório também deve conter um arquivo "cert.pem" e/ou um
   diretório "certs".

      $ find /etc/ -name openssl.cnf -printf "%h\n"
      /etc/ssl

2. Baixe, construa e instale o OpenSSL. Certifique-se de usar
   "install_sw" e não "install". O destino "install_sw" não substitui
   o "openssl.cnf".

      $ curl -O https://www.openssl.org/source/openssl-VERSÃO.tar.gz
      $ tar xzf openssl-VERSÃO
      $ pushd openssl-VERSÃO
      $ ./config \
          --prefix=/usr/local/custom-openssl \
          --libdir=lib \
          --openssldir=/etc/ssl
      $ make -j1 depend
      $ make -j8
      $ make install_sw
      $ popd

3. Construa o Python com o OpenSSL personalizado (veja as opções
   configure "--with-openssl" e "--with-openssl-rpath")

      $ pushd python-3.x.x
      $ ./configure -C \
          --with-openssl=/usr/local/custom-openssl \
          --with-openssl-rpath=auto \
          --prefix=/usr/local/python-3.x.x
      $ make -j8
      $ make altinstall

Nota:

  As versões de patches do OpenSSL têm uma ABI compatível com versões
  anteriores. Você não precisa recompilar o Python para atualizar o
  OpenSSL. É suficiente substituir a instalação personalizada do
  OpenSSL por uma versão mais recente.
