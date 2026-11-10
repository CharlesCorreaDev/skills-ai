"html.parser" --- Analisador simples de HTML e XHTML
****************************************************

**Código-fonte:** Lib/html/parser.py

======================================================================

Este módulo define uma classe "HTMLParser" que serve como base para
analisar arquivos de texto formatados em HTML (HyperText Markup
Language) e XHTML.

class html.parser.HTMLParser(*, convert_charrefs=True, scripting=False)

   Cria uma instância de analisador sintático capaz de analisar
   marcação inválida.

   Se *convert_charrefs* for verdadeiro (o padrão), todas as
   referências de caracteres (exceto as de elementos como "script" e
   "style") serão convertidas automaticamente para os caracteres
   Unicode correspondentes.

   Se *scripting* for falso (o padrão), o conteúdo do elemento
   "noscript" será analisado normalmente; se for verdadeiro, será
   retornado como está, sem ser analisado.

   Uma instância de "HTMLParser" recebe dados HTML e chama métodos de
   tratamento quando encontra tags de abertura, tags de fechamento,
   texto, comentários e outros elementos de marcação. O usuário deve
   criar uma subclasse de "HTMLParser" e substituir seus métodos para
   implementar o comportamento desejado.

   Este analisador sintático não verifica se as tags de fechamento
   correspondem às tags de abertura nem chama o manipulador de tags de
   fechamento para elementos que são fechados implicitamente pelo
   fechamento de um elemento externo.

   Alterado na versão 3.4: Adicionado o argumento nomeado
   *convert_charrefs*.

   Alterado na versão 3.5: O valor padrão para o argumento
   *convert_charrefs* agora é "True".

   Alterado na versão 3.14.1: Adicionado o parâmetro *scripting*.


Exemplo de aplicação para análise de HTML
=========================================

Como exemplo básico, abaixo está um analisador HTML simples que usa a
classe "HTMLParser" para exibir as tags de abertura, tags de
fechamento e dados à medida que são encontrados:

   from html.parser import HTMLParser

   class MyHTMLParser(HTMLParser):
       def handle_starttag(self, tag, attrs):
           print("Encontrada a tag de abertura  :", tag)

       def handle_endtag(self, tag):
           print("Encontrada a tag de fechamento:", tag)

       def handle_data(self, data):
           print("Encontrados alguns dados      :", data)

   parser = MyHTMLParser()
   parser.feed('<html><head><title>Teste</title></head>'
               '<body><h1>Me analise!</h1></body></html>')

A saída então será:

   Encontrada a tag de abertura  : html
   Encontrada a tag de abertura  : head
   Encontrada a tag de abertura  : title
   Encontrados alguns dados      : Teste
   Encontrada a tag de fechamento: title
   Encontrada a tag de fechamento: head
   Encontrada a tag de abertura  : body
   Encontrada a tag de abertura  : h1
   Encontrados alguns dados      : Me analise!
   Encontrada a tag de fechamento: h1
   Encontrada a tag de fechamento: body
   Encontrada a tag de fechamento: html


Métodos "HTMLParser"
====================

Instâncias de "HTMLParser" têm os seguintes métodos:

HTMLParser.feed(data)

   Fornece algum texto ao analisador. Ele será processado na medida em
   que consistir em elementos completos; dados incompletos serão
   armazenados em buffer até que mais dados sejam fornecidos ou que o
   método "close()" seja chamado. Os dados devem ser do tipo "str".

HTMLParser.close()

   Força o processamento de todos os dados em buffer como se fossem
   seguidos por uma marca de fim de arquivo. Este método pode ser
   redefinido por uma classe derivada para definir processamento
   adicional no final da entrada, mas a versão redefinida deve sempre
   chamar o método "close()" da classe base "HTMLParser".

HTMLParser.reset()

   Reinicializa a instância. Perde todos os dados não processados.
   Este método é chamado implicitamente no momento da instanciação.

HTMLParser.getpos()

   Retorna o número da linha atual e o deslocamento.

HTMLParser.get_starttag_text()

   Retorna o texto da tag de abertura aberta mais recentemente.
   Normalmente, isso não é necessário para processamento estruturado,
   mas pode ser útil ao lidar com HTML "como implantado" ou para
   regenerar a entrada com alterações mínimas (o espaço em branco
   entre os atributos pode ser preservado, etc.).

Os seguintes métodos são chamados quando elementos de dados ou de
marcação são encontrados e devem ser sobrescritos em uma subclasse. As
implementações da classe base não fazem nada (exceto por
"handle_startendtag()"):

HTMLParser.handle_starttag(tag, attrs)

   Este método é chamado para manipular a tag de abertura de um
   elemento (por exemplo, "<div id="main">").

   The *tag* argument is the name of the tag converted to lower case.
   The *attrs* argument is a list of "(name, value)" pairs containing
   the attributes found inside the tag's "<>" brackets.  The *name*
   will be translated to lower case, and quotes in the *value* have
   been removed, and character and entity references have been
   replaced.  For empty attributes, *value* is "None".

   Por exemplo, para a tag "<A HREF="https://www.cwi.nl/">", este
   método seria chamado como "handle_starttag('a', [('href',
   'https://www.cwi.nl/')])".

   Todas as referências de entidade de "html.entities" são
   substituídas nos valores dos atributos.

HTMLParser.handle_endtag(tag)

   Este método é chamado para manipular a tag de fechamento de um
   elemento (por exemplo, "</div>").

   O argumento *tag* é o nome da etiqueta convertido para letras
   minúsculas.

HTMLParser.handle_startendtag(tag, attrs)

   Similar a "handle_starttag()", mas chamado quando o analisador
   sintático encontra uma tag vazia no estilo XHTML ("<img ... />").
   Este método pode ser substituído por subclasses que requerem essa
   informação lexical específica; a implementação padrão simplesmente
   chama "handle_starttag()" e "handle_endtag()".

HTMLParser.handle_data(data)

   Este método é chamado para processar dados arbitrários (por
   exemplo, nós de texto e o conteúdo de elementos como "script" e
   "style").

HTMLParser.handle_entityref(name)

   Este método é chamado para processar uma referência de caractere
   nomeada no formato "&name;" (por exemplo, "&gt;"), onde *name* é
   uma referência de entidade genérica (por exemplo, "'gt'"). Este
   método só é chamado se *convert_charrefs* for falso.

HTMLParser.handle_charref(name)

   Este método é chamado para processar referências de caracteres
   numéricos decimais e hexadecimais no formato "&#*NNN*;" e
   "&#x*NNN*;". Por exemplo, o equivalente decimal para "&gt;" é
   "&#62;", enquanto o hexadecimal é "&#x3E;"; neste caso, o método
   receberá "'62'" ou "'x3E'". Este método só é chamado se
   *convert_charrefs* for falso.

HTMLParser.handle_comment(data)

   Este método é chamado quando um comentário é encontrado (por
   exemplo, "<!--comentário-->").

   Por exemplo, o comentário "<!-- comentário -->" fará com que este
   método seja chamado com o argumento "' comentário '".

   O conteúdo dos comentários condicionais do Internet Explorer
   (condcoms) também será enviado para este método, portanto, para
   "<!--[if IE 9]>conteúdo específico do IE9<![endif]-->", este método
   receberá "'[if IE 9]>conteúdo específico do IE9<![endif]'".

HTMLParser.handle_decl(decl)

   Este método é chamado para lidar com uma declaração de doctype HTML
   (por exemplo, "<!DOCTYPE html>").

   O parâmetro *decl* será todo o conteúdo da declaração dentro da
   marcação "<!...>" (por exemplo, "'DOCTYPE html'").

HTMLParser.handle_pi(data)

   Método chamado quando uma instrução de processamento é encontrada.
   O parâmetro *data* conterá a instrução de processamento completa.
   Por exemplo, para a instrução de processamento "<?proc
   color='red'>", este método seria chamado como "handle_pi("proc
   color='red'")". Ele foi projetado para ser substituído por uma
   classe derivada; a implementação da classe base não faz nada.

   Nota:

     A classe "HTMLParser" usa as regras sintáticas SGML para
     processar instruções. Uma instrução de processamento XHTML que
     usa o caractere "'?'" no final fará com que o "'?'" seja incluído
     em *data*.

HTMLParser.unknown_decl(data)

   Este método é chamado quando uma declaração não reconhecida é lida
   pelo analisador sintático.

   O parâmetro *data* será todo o conteúdo da declaração dentro da
   marcação "<![...]>". Às vezes, é útil que ele seja sobrescrito por
   uma classe derivada. A implementação da classe base não faz nada.


Exemplos
========

A classe a seguir implementa um analisador sintático que será usado
para ilustrar mais exemplos:

   from html.parser import HTMLParser
   from html.entities import name2codepoint

   class MyHTMLParser(HTMLParser):
       def handle_starttag(self, tag, attrs):
           print("Tag inicial:", tag)
           for attr in attrs:
               print("     attr:", attr)

       def handle_endtag(self, tag):
           print("Tag final  :", tag)

       def handle_data(self, data):
           print("Dados      :", data)

       def handle_comment(self, data):
           print("Comentário :", data)

       def handle_entityref(self, name):
           c = chr(name2codepoint[name])
           print("Ent nomeada:", c)

       def handle_charref(self, name):
           if name.startswith('x'):
               c = chr(int(name[1:], 16))
           else:
               c = chr(int(name))
           print("Num ent    :", c)

       def handle_decl(self, data):
           print("Decl       :", data)

   parser = MyHTMLParser()

Analisando um doctype:

   >>> parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
   ...             '"http://www.w3.org/TR/html4/strict.dtd">')
   Decl       : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"

Analisando um elemento com alguns atributos e um título:

   >>> parser.feed('<img src="python-logo.png" alt="The Python logo">')
   Tag inicial: img
        attr: ('src', 'python-logo.png')
        attr: ('alt', 'The Python logo')
   >>>
   >>> parser.feed('<h1>Python</h1>')
   Tag inicial: h1
   Dados      : Python
   Tag final  : h1

O conteúdo de elementos como "script" e "style" é retornado como está,
sem mais análises:

   >>> parser.feed('<style type="text/css">#python { color: green }</style>')
   Tag inicial: style
        attr: ('type', 'text/css')
   Dados      : #python { color: green }
   Tag final  : style

   >>> parser.feed('<script type="text/javascript">'
   ...             'alert("<strong>hello! &#9786;</strong>");</script>')
   Tag inicial: script
        attr: ('type', 'text/javascript')
   Dados      : alert("<strong>hello! &#9786;</strong>");
   Tag final  : script

Attribute names are converted to lowercase, quotes from attribute
values removed, and "None" is returned as *value* for empty attributes
(such as "checked"):

   >>> parser.feed("<input TYPE='checkbox' checked required='' disabled=disabled>")
   Start tag: input
        attr: ('type', 'checkbox')
        attr: ('checked', None)
        attr: ('required', '')
        attr: ('disabled', 'disabled')

Analisando comentários:

   >>> parser.feed('<!-- a comment -->'
   ...             '<!--[if IE 9]>IE-specific content<![endif]-->')
   Comentário : a comment
   Comentário : [if IE 9]>IE-specific content<![endif]

Analisando referências de caracteres nomeadas e numéricas e
convertendo-as para o caractere correto (nota: essas 3 referências são
todas equivalentes a "'>'"):

   >>> parser = MyHTMLParser()
   >>> parser.feed('&gt;&#62;&#x3E;')
   Data     : >>>

   >>> parser = MyHTMLParser(convert_charrefs=False)
   >>> parser.feed('&gt;&#62;&#x3E;')
   Named ent: >
   Num ent  : >
   Num ent  : >

Alimentar o "feed()" com blocos incompletos funciona, mas
"handle_data()" pode ser chamado mais de uma vez se *convert_charrefs*
for falso:

   >>> for chunk in ['<sp', 'an>buff', 'ered', ' text</s', 'pan>']:
   ...     parser.feed(chunk)
   ...
   Start tag: span
   Data     : buff
   Data     : ered
   Data     :  text
   End tag  : span

Analisando HTML inválido (por exemplo, atributos sem aspas) também
funciona:

   >>> parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
   Tag inicial: p
   Tag inicial: a
        attr: ('class', 'link')
        attr: ('href', '#main')
   Dados      : tag soup
   Tag final  : p
   Tag final  : a
