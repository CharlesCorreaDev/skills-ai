Módulos de Processamento de XML
*******************************

**Código-fonte:** Lib/xml/

======================================================================

As interfaces do Python para processar XML estão agrupadas no pacote
"xml".

Nota:

  Se você precisar analisar dados não confiáveis ou não autenticados,
  consulte Segurança no XML.

É importante observar que os módulos no pacote "xml" exigem que está
disponível pelo menos um analisador sintático XML compatível com SAX.
O analisador sintático Expat está incluído no Python, então o módulo
"xml.parsers.expat" estará sempre disponível.

A documentação para os pacotes "xml.dom" e "xml.sax" são a definição
das ligações Python para as interfaces DOM e SAX.

Os submódulos de manipulação XML são:

* "xml.etree.ElementTree": a API de ElementTree, um processador XML
  simples e leve

* "xml.dom": a definição da API de DOM

* "xml.dom.minidom": uma implementação mínima do DOM

* suporte para construir árvores parciais de DOM no "xml.dom.pulldom"

* "xml.sax": Classe base SAX2 e funções de conveniência

* "xml.parsers.expat": a ligação do analisador sintático Expat

This module also defines utility functions.

xml.is_valid_name(name)

   Return "True" if the string is a valid element or attribute name,
   "False" otherwise.

   Almost all characters are permitted in names, except control
   characters and those which either are or reasonably could be used
   as delimiters. Characters like ":", "-", ".", "_", and "·" are
   permitted, but "<", "/", "!", "?", and "=" are forbidden. The name
   cannot start with a digit or a character like "-", ".", and "·".

   Adicionado na versão 3.15.

xml.is_valid_text(data)

   Return "True" if the string is a sequence of legal XML 1.0
   characters, "False" otherwise.

   Almost all characters are permitted in XML 1.0 documents, except C0
   control characters (excluding TAB, CR and LF), surrogate characters
   and special Unicode characters U+FFFE and U+FFFF.

   Adicionado na versão 3.15.


Segurança no XML
================

Um atacante pode abusar dos recursos XML para realizar ataques de
negação de serviço, acessar arquivos locais, gerar conexões de rede
com outras máquinas ou contornar firewalls. quando XML controlado pelo
atacante está sendo analisado, no Python ou de qualquer outra forma.

Os analisadores XML embutidos do Python dependem da biblioteca
libexpat, comumente chamada Expat, para análise de XML.

Por padrão, Expat não acessa arquivos locais nem cria conexões de
rede.

Versões do Expat anteriores à 2.7.2 podem ser vulneráveis às
vulnerabilidades "billion laughs", "quadratic blowup" e "large
tokens", ou ao uso desproporcional de memória dinâmica. O Python
inclui uma cópia do Expat, e o uso da versão incluída ou de uma versão
do sistema depende de como o interpretador Python "foi configurado" no
seu ambiente. O Python pode ser vulnerável se usar versões antigas do
Expat. Verifique "pyexpat.EXPAT_VERSION".

"xmlrpc" é **vulnerável** ao ataque "decompression bomb".

billion laughs / exponential entity expansion
   O ataque Billion Laughs (bilhões de risadas, em uma tradução livre)
   - também conhecido como "exponential entity expansion" (expansão
   exponencial de entidades, em uma tradução livre) - usa vários
   níveis de entidades aninhadas. Cada entidade se refere a outra
   entidade várias vezes, e a definição final da entidade contém uma
   pequena string. A expansão exponencial resulta em vários gigabytes
   de texto e consome muita memória e tempo de CPU.

quadratic blowup entity expansion
   Um ataque "quadratic blowup" (explosão quadrática, em uma tradução
   livre) português) é semelhante a um ataque Billion Laughs; ele
   abusa da expansão de entidades também. Em vez de entidades
   aninhadas, ele repete uma grande entidade com alguns milhares de
   caracteres repetidamente. O ataque não é tão eficiente quanto o
   caso exponencial, mas evita acionar contramedidas do analisador
   sintático que proíbem entidades profundamente aninhadas.

decompression bomb
   "Bombas de descompressão" em uma tradução livre. Também conhecidas
   como ZIP bomb, se aplicam a todas as bibliotecas XML que podem
   analisar fluxos XML comprimidos, como fluxos de HTTP compactados
   com gzip ou arquivos comprimidos com LZMA. Para um atacante, isso
   pode reduzir a quantidade de dados transmitidos em três magnitudes
   ou mais.

large tokens
   Expat precisa analisar novamente os símbolos não finalizados; sem a
   proteção introduzida no Expat 2.6.0, isso pode levar a um tempo de
   execução quadrático que pode ser usado para causar negação de
   serviço na aplicação ao analisar XML. O problema é conhecido como
   **CVE 2023-52425**.
