"xml.dom.pulldom" --- Suporte para construir árvores parciais de DOM
********************************************************************

**Código-fonte:** Lib/xml/dom/pulldom.py

======================================================================

O módulo "xml.dom.pulldom" fornece um "analisador sintático de pull"
que também pode ser solicitado a produzir fragmentos do documento
acessíveis via DOM, quando necessário. O conceito básico envolve
extrair "eventos" de um fluxo de XML recebido e processá-los. Ao
contrário do SAX, que também emprega um modelo de processamento
orientado a eventos juntamente com retornos de chamada, o usuário de
um analisador sintático pull é responsável por extrair explicitamente
os eventos do fluxo, repetindo esses eventos até que o processamento
seja concluído ou ocorra uma condição de erro.

Nota:

  Se você precisar analisar dados não confiáveis ou não autenticados,
  consulte Segurança no XML.

Alterado na versão 3.7.1: O analisador sintático de SAX não processa
mais entidades externas gerais por padrão para aumentar a segurança.
Para habilitar o processamento de entidades externas, passe uma
instância personalizada do analisador sintático em:

   from xml.dom.pulldom import parse
   from xml.sax import make_parser
   from xml.sax.handler import feature_external_ges

   parser = make_parser()
   parser.setFeature(feature_external_ges, True)
   parse(filename, parser=parser)

Exemplo:

   from xml.dom import pulldom

   doc = pulldom.parse('sales_items.xml')
   for event, node in doc:
       if event == pulldom.START_ELEMENT and node.tagName == 'item':
           if int(node.getAttribute('price')) > 50:
               doc.expandNode(node)
               print(node.toxml())

"event" é uma das seguintes constantes, e "node" é o nó ao qual o
evento se refere. Os nós implementam as interfaces "xml.dom"; eles são
criados pela implementação do DOM fornecida a "PullDOM", que é
"xml.dom.minidom" por padrão.

xml.dom.pulldom.START_DOCUMENT
xml.dom.pulldom.END_DOCUMENT

   O início e o fim do documento. *node* é o "Document".

xml.dom.pulldom.START_ELEMENT
xml.dom.pulldom.END_ELEMENT

   A tag de início e a tag de fim de um elemento. *node* é o
   "Element".

xml.dom.pulldom.CHARACTERS

   Dados de caractere. *node* é o nó "Text".

xml.dom.pulldom.IGNORABLE_WHITESPACE

   Espaço em branco no conteúdo do elemento, conforme declarado na
   DTD. *node* é o nó "Text".

xml.dom.pulldom.COMMENT

   Um comentário. *node* é o nó "Comment".

xml.dom.pulldom.PROCESSING_INSTRUCTION

   Uma instrução de processamento. *node* é o nó
   "ProcessingInstruction".

Como o documento é tratado como um fluxo "plano" de eventos, a
"árvore" do documento é implicitamente percorrida e os elementos
desejados são encontrados independentemente de sua profundidade na
árvore. Em outras palavras, não é necessário considerar questões
hierárquicas, como a busca recursiva dos nós do documento, embora, se
o contexto dos elementos fosse importante, seria necessário manter
algum estado relacionado ao contexto (ou seja, lembrar onde se está no
documento em um determinado ponto) ou utilizar o método
"DOMEventStream.expandNode()" e alternar para o processamento
relacionado ao DOM.

class xml.dom.pulldom.PullDOM(documentFactory=None)

   Subclasse de "xml.sax.handler.ContentHandler" que converte eventos
   SAX em eventos do *pull parser*. Os nós são criados, mas não são
   adicionados à árvore, a menos que "expandNode()" seja chamado.
   *documentFactory*, se fornecido, é uma implementação DOM usada para
   criar o documento; por padrão, utiliza-se a implementação de
   "xml.dom.minidom".

class xml.dom.pulldom.SAX2DOM(documentFactory=None)

   Subclasse de "PullDOM" que também adiciona cada nó criado à árvore,
   de modo que o documento completo seja construído.

xml.dom.pulldom.parse(stream_or_string, parser=None, bufsize=None)

   Retorna um "DOMEventStream" da entrada fornecida.
   *stream_or_string* pode ser um nome de arquivo ou um objeto arquivo
   ou similar. *parser*, se fornecido, deve ser um objeto "XMLReader".
   Esta função alterará o manipulador de documentos do analisador e
   ativará o suporte a espaços de nomes; outras configurações do
   analisador sintático (como a definição de um resolvedor de
   entidades) devem ter sido feitas previamente.

Se você tiver XML em uma string, poderá usar a função "parseString()":

xml.dom.pulldom.parseString(string, parser=None)

   Retorna um "DOMEventStream" que representa a *string*. A *string*
   deve ser uma instância de "str"; para analisar bytes, passe um
   objeto arquivo binário para "parse()".

xml.dom.pulldom.default_bufsize

   Valor padrão para o parâmetro *bufsize* para "parse()".

   O valor desta variável pode ser alterado antes de chamar "parse()"
   e o novo valor entrará em vigor.


Objetos DOMEventStream
======================

class xml.dom.pulldom.DOMEventStream(stream, parser, bufsize)

   Produz os eventos para os dados lidos do objeto arquivo *stream*
   pelo *parser* "XMLReader". Os dados são lidos em blocos de
   *bufsize* bytes — ou caracteres, no caso de um fluxo de texto — por
   vez.

   Alterado na versão 3.11: O suporte para o método "__getitem__()"
   foi removido

   getEvent()

      Retorna a próxima tupla "(event, node)" ou "None" ao final do
      documento. Consulte acima as informações sobre os eventos e os
      nós correspondentes. O nó atual não contém informações sobre
      seus filhos, a menos que "expandNode()" seja chamado.

   expandNode(node)

      Expande todos os filhos de *node* para *node*. Exemplo:

         from xml.dom import pulldom

         xml = '<html><title>Foo</title> <p>Algum texto <div>e mais</div></p> </html>'
         doc = pulldom.parseString(xml)
         for event, node in doc:
             if event == pulldom.START_ELEMENT and node.tagName == 'p':
                 # A seguinte instrução só exibe '<p/>'
                 print(node.toxml())
                 doc.expandNode(node)
                 # A seguinte instrução exibe o nó com todos os seus filhos '<p>Algum texto <div>e mais</div></p>'
                 print(node.toxml())

   reset()

      Descarta os eventos que ainda não foram lidos e prepare o objeto
      para análise de um novo documento.

   clear()

      Libera o analisador e o documento. O fluxo não é fechado, e o
      objeto não pode mais ser utilizado.
