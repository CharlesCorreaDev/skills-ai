"pyclbr" --- Suporte a navegador de módulos do Python
*****************************************************

**Código-fonte:** Lib/pyclbr.py

======================================================================

O módulo "pyclbr" fornece informações limitadas sobre as funções,
classes e métodos definidos em um módulo codificado em Python. As
informações são suficientes para implementar um navegador de módulos.
As informações são extraídas do código-fonte do Python em vez de
importar o módulo, portanto, este módulo é seguro para uso com código
não confiável. Essa restrição torna impossível o uso deste módulo com
módulos não implementados no Python, incluindo todos os módulos de
extensão padrão e opcionais.

pyclbr.readmodule(module, path=None)

   Retorna um dicionário que mapeia os nomes de classe no nível do
   módulo aos descritores de classe. Se possível, descritores para
   classes base importadas estão incluídos. O parâmetro *module* é uma
   string com o nome do módulo a ser lido; pode ser o nome de um
   módulo dentro de um pacote. Se fornecido, *path* é uma sequência de
   caminhos de diretório anexada a "sys.path", que é usada para
   localizar o código-fonte do módulo.

   Esta função é a interface original e é mantida apenas para
   compatibilidade reversa. Ela retorna uma versão filtrada da
   seguinte.

pyclbr.readmodule_ex(module, path=None)

   Retorna uma árvore baseada em dicionário que contém uma função ou
   descritores de classe para cada função e classe definida no módulo
   com uma instrução "def" ou "class". O dicionário retornado mapeia
   os nomes das funções e das classes no nível do módulo para seus
   descritores. Objetos aninhados são inseridos no dicionário filho de
   seus pais. Como em readmodule, *module* nomeia o módulo a ser lido
   e *path* é anexado ao sys.path. Se o módulo que está sendo lido for
   um pacote, o dicionário retornado terá uma chave "'__path__'" cujo
   valor é uma lista que contém o caminho de pesquisa do pacote.

Adicionado na versão 3.7: Descritores para definições aninhadas. Eles
são acessados através do novo atributo filho. Cada um tem um novo
atributo pai.

Os descritores retornados por essas funções são instâncias das classes
Function e Class. Não se espera que os usuários criem instâncias
dessas classes.


Objetos Function
================

class pyclbr.Function

   Instâncias da classe "Function" descrevem funções definidas por
   instruções def. Elas têm os seguintes atributos:

   file

      Nome do arquivo no qual a função está definida.

   module

      O nome do módulo que define a função descrita.

   name

      O nome da função.

   lineno

      O número da linha no arquivo em que a definição é iniciada.

   parent

      Para funções de nível superior, "None". Para funções aninhadas,
      o pai.

      Adicionado na versão 3.7.

   children

      Um "dicionário" que mapeia nomes para descritores para funções e
      classes aninhadas.

      Adicionado na versão 3.7.

   is_async

      "True" para funções que são definidas com o prefixo "async".
      Caso contrário, "False".

      Adicionado na versão 3.10.


Objetos Class
=============

class pyclbr.Class

   Instâncias da classe "Class" descrevem classes definidas por
   instruções class. Elas têm os mesmos atributos que "Functions" e
   mais dois.

   file

      Nome do arquivo no qual a classe está definida.

   module

      O nome do módulo que define a classe descrita.

   name

      O nome da classe.

   lineno

      O número da linha no arquivo em que a definição é iniciada.

   parent

      Para classes de nível superior, "None". Para classes aninhadas,
      o pai.

      Adicionado na versão 3.7.

   children

      Um dicionário que mapeia nomes para descritores para funções e
      classes aninhadas.

      Adicionado na versão 3.7.

   super

      Uma lista de objetos "Class" que descreve as classes base
      imediatas da classe que está sendo descrita. Classes nomeadas
      como superclasses, mas que não podem ser descobertas por
      "readmodule_ex()" são listadas como uma string com o nome da
      classe em vez de como objetos de "Class".

   methods

      Um "dicionário" que mapeia nomes de métodos para números de
      linha. Isso pode ser derivado do dicionário "children" mais
      novo, mas permanece para compatibilidade retroativa.
