Construindo extensões C e C++
*****************************

Uma extensão C para CPython é uma biblioteca compartilhada (por
exemplo, um arquivo ".so" no Linux, ".pyd" no Windows), que exporta
uma *função de inicialização*.

Veja Definindo módulos de extensão para detalhes.


Construindo extensões C e C ++ com setuptools
=============================================

A construção, o empacotamento e a distribuição de módulos de extensão
são melhor realizados com ferramentas de terceiros e estão fora do
escopo deste documento. Uma ferramenta adequada é o Setuptools, cuja
documentação pode ser encontrada em
https://setuptools.pypa.io/en/latest/setuptools.html.

O módulo "distutils", que estava incluído na biblioteca padrão até o
Python 3.12, agora é mantido como parte do Setuptools.
