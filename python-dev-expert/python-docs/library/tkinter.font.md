"tkinter.font" --- Invólucro de fontes Tkinter
**********************************************

**Código-fonte:** Lib/tkinter/font.py

======================================================================

O módulo "tkinter.font" apresenta a classe "Font" para criação e
utilização de fontes nomeadas.

Os diferentes pesos e inclinações de fontes são:

tkinter.font.NORMAL
tkinter.font.BOLD
tkinter.font.ITALIC
tkinter.font.ROMAN

class tkinter.font.Font(root=None, font=None, name=None, exists=False, **options)

   A classe "Font" representa uma fonte nomeada. Instâncias *font*
   recebem nomes únicos e podem ser especificadas por família, tamanho
   e configuração de estilo. Fontes nomeadas são os métodos Tk para
   criação e identificação de fontes de um objeto singular, ao invés
   de especificar a fonte por seus atributos em cada ocorrência.

   Alterado na versão 3.10: Duas fontes agora são consideradas iguais
   ("==") apenas quando ambas são instâncias de "Font" com o mesmo
   nome e pertencentes ao mesmo interpretador Tcl.argumentos:

         *font* - tupla de especificação da fonte (família, tamanho, opções)
         *name* - nome único da fonte
         *exists* - aponta para uma fonte nomeada existente se for verdadeiro

   palavras reservadas opcionais (ignoradas caso *font* seja
   especificado):

         *family* - a família da fonte, por exemplo, Courier, Times
         *size* - tamanho da fonte
            Se *size* for positivo, ele é interpretado como tamanho em pontos.
            Caso *size* seja um número negativo, seu valor absoluto é tratado
            como tamanho em pixels.
         *weight* - ênfase da fonte (normal,negrito)
         *slant* - ROMAN, ITALIC
         *underline* - sublinhamento da fonte (0 - sem sublinhamento, 1 - sublinhado)
         *overstrike* - fonte riscada (0 - sem risco, 1 - letras riscadas)

   actual(option=None, displayof=None)

      Retorna os atributos reais do tipo de letra, que podem diferir
      dos solicitados devido a limitações da plataforma. Sem nenhuma
      *option*, retorna um dicionário de todos os atributos; se a
      *option* for fornecida, devolve o valor desse atributo
      individual. Os atributos são resolvidos na exibição do widget
      *displayof* ou na janela principal da aplicação se este não for
      especificado.

   cget(option)

      Recupera um atributo da fonte.

   configure(**options)

      Modifica um ou mais atributos da fonte. Sem argumentos, retorna
      um dicionário dos atributos atuais.

      "config()" é um apelido de "configure()".

   copy()

      Retorna uma cópia distinta da fonte atual: uma nova fonte
      nomeada com os mesmos atributos, porém com um nome diferente,
      que pode ser reconfigurada independentemente da original. Se a
      fonte atual envolver uma descrição de fonte, a cópia será, em
      vez disso, uma fonte nomeada com seus atributos resolvidos.

   measure(text, displayof=None)

      Retorna, como um número inteiro de pixels, a quantidade de
      espaço que o texto ocuparia no dispositivo de exibição
      especificado, quando formatado com a fonte atual. Se nenhum
      dispositivo de exibição for especificado, considera-se a janela
      principal da aplicação.

   metrics(*options, **kw)

      Retorna dados específicos da fonte. Sem opções, retorna um
      dicionário que mapeia cada nome de métrica ao seu valor inteiro;
      se um nome de opção for fornecido, retorna o valor dessa métrica
      como um número inteiro. As opções incluem:

      *ascent* - distância entre a linha de base e o ponto mais alto
      que um caractere da fonte pode ocupar

      *descent* - distância entre a linha de base e o ponto mais baixo
      que um caractere da fonte pode ocupar

      *linespace* - separação vertical mínima necessária entre
      quaisquer dois caracteres da fonte, que garanta a ausência de
      sobreposição vertical entre as linhas.

      *fixed* - 1 caso a fonte seja de largura fixa, 0 caso contrário

tkinter.font.families(root=None, displayof=None)

   Retorna uma tupla com os nomes das famílias de fontes disponíveis.

tkinter.font.names(root=None)

   Retorna uma tupla com os nomes de todas as fontes definidas.

tkinter.font.nametofont(name, root=None)

   Retorna uma representação "Font" da fonte nomeada *name* já
   existente. *root* é o widget cujo interpretador Tcl detém a fonte;
   se omitido, utiliza-se a janela raiz padrão.

   Alterado na versão 3.10: O parâmetro *root* foi adicionado.
