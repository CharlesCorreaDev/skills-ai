"xml.sax.saxutils" --- Utilitários de SAX
*****************************************

**Código-fonte:** Lib/xml/sax/saxutils.py

======================================================================

O módulo "xml.sax.saxutils" contém uma série de classes e funções que
são comumente úteis ao criar aplicações SAX, seja em uso direto ou
como classes base.

xml.sax.saxutils.escape(data, entities={})

   Escapa "'&'", "'<'" e "'>'" em uma string de dados.

   Você pode escapar outras strings de dados passando um dicionário
   como o parâmetro opcional *entities*. As chaves e os valores devem
   ser strings; cada chave será substituída pelo seu valor
   correspondente. Os caracteres "'&'", "'<'" e "'>'" são sempre
   escapados, mesmo que *entities* seja fornecido.

   Nota:

     Esta função deve ser usada apenas para escapar caracteres que não
     podem ser usados diretamente em XML. Não a utilize como uma
     função geral de tradução de strings.

xml.sax.saxutils.unescape(data, entities={})

   Remove escape de "'&amp;'", "'&lt;'" e "'&gt;'" em uma string de
   dados.

   Você pode remover escape de outras strings de dados passando um
   dicionário como o parâmetro opcional *entities*. As chaves e os
   valores devem ser strings; cada chave será substituída pelo seu
   valor correspondente. "'&amp;'", "'&lt;'" e "'&gt;'" têm sempre o
   escape removido, mesmo que *entities* seja fornecido.

xml.sax.saxutils.quoteattr(data, entities={})

   Semelhante a "escape()", mas também prepara *data* para ser usado
   como um valor de atributo. O valor de retorno é uma versão entre
   aspas de *data* com quaisquer substituições adicionais necessárias.
   "quoteattr()" selecionará um caractere de aspas com base no
   conteúdo de *data*, tentando evitar a codificação de quaisquer
   caracteres de aspas na string. Se já houver caracteres de aspas
   simples e duplas em *data*, os caracteres de aspas duplas serão
   codificados e *data* será colocado entre aspas duplas. A string
   resultante pode ser usada diretamente como um valor de atributo:

      >>> print("<element attr=%s>" % quoteattr("ab ' cd \" ef"))
      <element attr="ab ' cd &quot; ef">

   Esta função é útil ao gerar valores de atributos para HTML ou
   qualquer SGML usando a sintaxe concreta de referência.

class xml.sax.saxutils.XMLGenerator(out=None, encoding='iso-8859-1', short_empty_elements=False)

   Esta classe implementa a interface "ContentHandler" escrevendo
   eventos SAX de volta em um documento XML. Em outras palavras, usar
   um "XMLGenerator" como manipulador de conteúdo reproduzirá o
   documento original que está sendo analisado. *out* deve ser um
   objeto arquivo ou similar, cujo padrão é *sys.stdout*. *encoding* é
   a codificação do fluxo de saída, cujo padrão é "'iso-8859-1'".
   *short_empty_elements* controla a formatação de elementos sem
   conteúdo: se "False" (o padrão), eles são emitidos como um par de
   tags de início/fim; se definido como "True", eles são emitidos como
   uma única tag autofechada.

   Alterado na versão 3.2: Foi adicionado o parâmetro
   *short_empty_elements*.

class xml.sax.saxutils.XMLFilterBase(base)

   Esta classe foi projetada para ficar entre um "XMLReader" e os
   manipuladores de eventos da aplicação cliente. Por padrão, ela não
   faz nada além de passar requisições para o leitor e eventos para os
   manipuladores sem modificações, mas subclasses podem substituir
   métodos específicos para modificar o fluxo de eventos ou as
   requisições de configuração à medida que passam.

   getParent()

      Retorna o leitor pai, ou "None" caso ele não esteja definido.

   setParent(parent)

      Define o leitor pai, a partir do qual os eventos são lidos.

xml.sax.saxutils.prepare_input_source(source, base='')

   Esta função recebe uma fonte de entrada e uma URL base opcional e
   retorna um objeto "InputSource" totalmente resolvido, pronto para
   leitura. A fonte de entrada pode ser fornecida como uma string, um
   objeto arquivo ou similar ou um objeto "InputSource"; os
   analisadores usarão esta função para implementar o argumento
   polimórfico *source* em seu método "parse()".
