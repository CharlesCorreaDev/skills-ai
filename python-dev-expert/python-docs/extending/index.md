Estendendo e incorporando o interpretador Python
************************************************

Este documento descreve o desenvolvimento de módulos com C ou C++ para
adicionar recursos ao interpretador Python criando novos módulos.
Esses módulos podem fazer o que o código Python faz -- definir
funções, tipos de objeto e métodos --, mas também interagir com
bibliotecas nativas ou obter melhor desempenho ao evitar a sobrecarga
de um interpretador. O documento também descreve como embutir o
interpretador Python em outra aplicação, de forma a utilizá-lo como
sendo uma linguagem de extensão. Por fim, é mostrado como se pode
compilar e fazer a vinculação dos módulos de extensão para que estes
possam ser carregados dinamicamente (em tempo de execução) pelo
interpretador, caso o sistema operacional subjacente suportar esse
recurso.

Este documento pressupõe conhecimentos básicos sobre C e Python. Para
uma introdução informal ao Python, consulte O tutorial do Python. A
Referência da Linguagem Python fornece uma definição mais formal da
linguagem. Referência da bibliotecas embutidas do Python documenta as
funções embutidas e tipos de objetos, e A biblioteca padrão do Python
documenta os módulos de objetos existentes (embutidos e escritos em
Python) que dão à linguagem sua ampla gama de aplicações.

Para uma descrição detalhada de toda a API Python/C, consulte o Manual
de referência da API C/Python separado.

Para dar suporte a extensões, a API do Python API (Application
Programmers Interface) define um conjunto de funções, macros e
variáveis que fornecem acesso à maior parte dos aspectos do sistema de
tempo de execução do Python.  A API do Python pode ser incorporada em
um arquivo fonte em C com a inclusão do cabeçalho ""Python.h"".

Nota:

  A interface de extensões em C é específica para o CPython, e módulos
  de extensão não funcionam em outras implementações do Python.  Em
  muitos casos, é possível evitar a criação destas extensões em C e
  preservar a portabilidade para outras implementações. Por exemplo,
  se o seu caso de uso for o de fazer chamadas a funções em
  bibliotecas C ou chamadas de sistema, considere utilizar o módulo
  "ctypes" ou a biblioteca cffi ao invés de escrever código C
  personalizado. Esses módulos permitem escrever código Python que
  pode interoperar com código C e que é mais portável entre
  implementações do Python do que escrever e compilar um módulo de
  extensão em C.


Ferramentas de terceiros recomendadas
=====================================

Este documenta aborda apenas as ferramentas básicas para a criação de
extensões fornecidas como parte desta versão do CPython. Algumas
ferramentas de terceiros oferecem abordagens mais simples e mais
sofisticadas para a criação de extensões em C e C++ para Python.

Embora este documento seja voltado para autores de extensões, ele
também deve ser útil para os autores de tais ferramentas. Por exemplo,
o módulo de tutorial pode servir como um caso de teste simples para
uma ferramenta de build ou como uma amostra da saída esperada de um
gerador de código.


Tutorial da API C
=================

Este tutorial descreve como escrever um módulo simples em C ou C++
usando a API C do Python — isto é, utilizando as ferramentas básicas
fornecidas como parte desta versão do CPython.

1. Seu primeiro módulo de extensão da API C


Guias para tópicos intermediários
=================================

Esta seção do guia aborda a criação de extensões C e C++ sem
assistência de ferramentas de terceiros. Destina-se principalmente aos
criadores dessas ferramentas, em vez de ser uma maneira recomendada de
criar suas próprias extensões C.

* Using the C API: Assorted topics

* Definindo Tipos de Extensão: Tutorial

* Defining Extension Types: Assorted Topics

* Construindo extensões C e C++

* Construindo Extensões C e C++ no Windows


Incorporando o tempo de execução do CPython em uma aplicação maior
==================================================================

Às vezes, em vez de criar uma extensão que é executada dentro do
interpretador Python como a aplicação principal, é desejável
incorporar o tempo de execução do CPython em uma aplicação maior. Esta
seção aborda alguns dos detalhes envolvidos para fazer isso com êxito.

* Incorporando o Python numa Outra Aplicação
