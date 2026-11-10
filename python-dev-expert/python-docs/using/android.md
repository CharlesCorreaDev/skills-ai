6. Utilizando Python no Android
*******************************

Python no Android é diferente do Python em plataformas de desktop. Em
uma plataforma desktop, o Python geralmente é instalado como um
recurso do sistema que pode ser usado por qualquer usuário daquele
computador. Os usuários então interagem com o Python executando um
executável **python** e inserindo comandos em um prompt interativo ou
executando um script Python.

No Android, não existe o conceito de instalação como recurso do
sistema. A única unidade de distribuição de software é uma aplicação,
ou "app". Também não há console onde você possa executar um executável
**python** ou interagir com um REPL do Python.

Como resultado, a única maneira de usar Python no Andoid é no modo
incorporado – ou seja, escrevendo uma aplicação Android nativo,
incorporando um interpretador Python usando "libpython" e invocando o
código Python usando API de incorporação do Python. O interpretador
Python completo, a biblioteca padrão e todo o seu código Python são
então empacotados para sua aplicação para seu próprio uso privado.

A biblioteca padrão do Python tem algumas omissões e restrições
notáveis no Andoid. Consulte o guia de disponibilidade de API para
Android para obter detalhes.


6.1. Adicionando Python a uma aplicação Android
===============================================

A maioria dos desenvolvedores de aplicações deve usar uma das
seguintes ferramentas, o que proporcionará uma experiência muito mais
fácil:

* Briefcase, do projeto BeeWare

* Buildozer, do projeto Kivy

* Chaquopy

* Flet

* pyqtdeploy

* Termux

Se você tem certeza de que quer fazer tudo isso manualmente, continue
lendo. Você pode usar a aplicação de teste como um guia; cada passo
abaixo contém um link para o arquivo relevante.

* Primeiro, obtenha uma construção do Python para Android:

  * A maneira mais fácil é baixar uma versão do Android em python.org.
    O diretório "prefix" mencionado abaixo está no nível raiz do
    pacote.

  * Ou, se quiser construí-la você mesmo, siga as instruções em
    Platforms/Android/README.md. O diretório "prefix" será criado em
    "cross-build/*HOST*".

* Adicione código ao seu arquivo build.gradle para copiar os seguintes
  itens para o seu projeto. Todos, exceto seu próprio código Python,
  podem ser copiados de "prefix/lib":

  * Em suas bibliotecas JNI:

    * "libpython*.*.so"

    * "lib*_python.so" (bibliotecas externas, tal como OpenSSL)

  * Em seus ativos (*assets*):

    * "python*.*" (a biblioteca padrão do Python)

    * "python*.*/site-packages" (seu próprio código Python)

* Adicione código a sua aplicação para extrair os ativos para o
  sistema de arquivos.

* Adicione código a sua aplicação para iniciar o Python em modo
  incorporado. Isso precisará ser código C chamado via JNI.


6.2. Construindo um pacote Python para Android
==============================================

Pacotes Python podem ser criados para Android como wheels e lançados
no PyPI. A ferramenta recomendada para isso é cibuildwheel, que
automatiza todos os detalhes da configuração de um ambiente de
compilação cruzada, da construção da wheel e dos testes em um
emulador.
