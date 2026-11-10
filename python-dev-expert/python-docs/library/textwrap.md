"textwrap" --- Quebra automática e preenchimento de texto
*********************************************************

**Código-fonte:** Lib/textwrap.py

======================================================================

O módulo "textwrap" fornece algumas funções úteis, assim como a classe
"TextWrapper", que faz todo o trabalho. Se você estiver apenas
preenchendo ou quebrando uma ou duas strings, as funções de
conveniência deverão ser suficientes; caso contrário, você deve usar
uma instância de "TextWrapper" para maior eficiência.

textwrap.wrap(text, width=70, *, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None, placeholder=' [...]')

   Quebra do parágrafo único em *text* (uma string) para que cada
   linha tenha, no máximo, *width* caracteres. Retorna uma lista de
   linhas de saída, sem novas linhas ao final.

   Argumentos nomeados opcionais correspondem aos atributos de
   instância de "TextWrapper", documentados abaixo.

   Veja o método "TextWrapper.wrap()" para detalhes adicionais sobre
   como "wrap()" se comporta.

textwrap.fill(text, width=70, *, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, max_lines=None, placeholder=' [...]')

   Quebra o parágrafo único em *text* e retorna uma única string
   contendo o parágrafo quebrado. "fill()" é uma abreviação de

      "\n".join(wrap(text, ...))

   Em particular, "fill()" aceita exatamente os mesmos argumentos
   nomeados que "wrap()".

textwrap.shorten(text, width, *, fix_sentence_endings=False, break_long_words=True, break_on_hyphens=True, placeholder=' [...]')

   Reduz e trunca o texto *text* para que ele caiba na largura *width*
   fornecida.

   Primeiro, o espaço em branco em *text* é reduzido (todos os espaços
   em branco são substituídos por espaços simples). Se o resultado
   couber em *width*, ele será retornado. Caso contrário, palavras
   suficientes serão eliminadas do final para que as palavras
   restantes mais o *placeholder* caibam em *largura*:

      >>> textwrap.shorten("Olá  mundo!", width=12)
      'Olá mundo!'
      >>> textwrap.shorten("Olá  mundo!", width=11)
      'Olá [...]'
      >>> textwrap.shorten("Olá mundo", width=10, placeholder="...")
      'Olá...'

   Argumentos nomeados opcionais correspondem aos atributos de
   instância de "TextWrapper", documentados abaixo. Observe que o
   espaço em branco é reduzido antes do texto ser passado para a
   função "TextWrapper" "fill()", alterando assim o valor de
   "tabsize", "expand_tabs", "drop_whitespace" e "replace_whitespace"
   não terão efeito.

   Adicionado na versão 3.4.

textwrap.dedent(text)

   Remove qualquer espaço em branco inicial em comum de todas as
   linhas do *text*.

   Isso pode ser usado para alinhar strings entre aspas triplas à
   borda esquerda da tela, enquanto ainda as apresenta no código-fonte
   com indentação.

   Observe que tabulações e espaços são tratados como espaços em
   branco, mas não são iguais: as linhas ""  hello"" e ""\thello"" são
   consideradas como não tendo espaços em branco iniciais comuns.

   Linhas contendo apenas espaços em branco são ignoradas na entrada e
   normalizadas para uma nova linha de um único caractere na saída.

   Por exemplo:

      def test():
          # fim da primeira linha com \ para evitar uma linha vazia!
          s = '''\
          olá
            mundo
          '''
          print(repr(s))          # exibe '    olá\n      mundo\n    '
          print(repr(dedent(s)))  # exibe 'olá\n  mundo\n'

   Alterado na versão 3.14: A função "dedent()" agora normaliza
   corretamente linhas em branco que contenham apenas caracteres de
   espaço em branco. Anteriormente, a implementação apenas normalizava
   linhas em branco que contivessem tabulações e espaços.

textwrap.indent(text, prefix, predicate=None)

   Adiciona *prefix* ao início das linhas selecionadas em *text*.

   As linhas são separadas chamando "text.splitlines(True)".

   Por padrão, *prefix* é adicionado a todas as linhas que não
   consistem apenas em espaços em branco (incluindo quaisquer finais
   de linha).

   Por exemplo:

      >>> s = 'olá\n\n \nmundo'
      >>> indent(s, '  ')
      '  olá\n\n \n  mundo'

   O argumento opcional *predicate* pode ser usado para controlar
   quais linhas têm indentação. Por exemplo, é fácil adicionar
   *prefix* até mesmo em linhas vazias e apenas com espaços em branco:

      >>> print(indent(s, '+ ', lambda line: True))
      + olá
      +
      +
      + mundo

   Adicionado na versão 3.3.

"wrap()", "fill()" e "shorten()" funcionam criando uma instância
"TextWrapper" e chamando um único método nela. Essa instância não é
reutilizada, então para aplicações que processam muitas strings de
texto usando "wrap()" e/ou "fill()", pode ser mais eficiente criar seu
próprio objeto "TextWrapper".

O texto é preferencialmente colocado em espaços em branco e logo após
os hífens nas palavras hifenizadas; somente então palavras longas
serão quebradas se necessário, a menos que
"TextWrapper.break_long_words" seja definido como falso.

class textwrap.TextWrapper(**kwargs)

   O construtor "TextWrapper" aceita vários argumentos nomeados
   opcionais. Cada argumento nomeado corresponde a um atributo de
   instância, por exemplo:

      wrapper = TextWrapper(initial_indent="* ")

   é o mesmo que

      wrapper = TextWrapper()
      wrapper.initial_indent = "* "

   Você pode reutilizar o mesmo objeto "TextWrapper" muitas vezes e
   pode alterar qualquer uma de suas opções através de atribuição
   direta a atributos de instância entre os usos.

   Os atributos de instância "TextWrapper" (e argumentos nomeados para
   o construtor) são os seguintes:

   width

      (padrão: "70") O comprimento máximo das linhas quebradas.
      Contanto que não existam palavras individuais no texto de
      entrada maiores que "width", "TextWrapper" garante que nenhuma
      linha de saída será maior que "width" caracteres.

   expand_tabs

      (padrão: "True") Se verdadeiro, então todos os caracteres de
      tabulação em *text* serão expandidos para espaços usando o
      método "expandtabs()" de *text*.

   tabsize

      (padrão: "8") Se "expand_tabs" for verdadeiro, então todos os
      caracteres de tabulação em *text* serão expandidos para zero ou
      mais espaços, dependendo da coluna atual e do tamanho da
      tabulação fornecido.

      Adicionado na versão 3.3.

   replace_whitespace

      (padrão: "True") Se verdadeiro, após a expansão da tabulação,
      mas antes da quebra, o método "wrap()" substituirá cada
      caractere de espaço em branco por um único espaço. Os caracteres
      de espaço em branco substituídos são os seguintes: tabulação,
      nova linha, tabulação vertical, feed de formulário e retorno de
      carro ("'\t\n\v\f\r'").

      Nota:

        Se "expand_tabs" for falso e "replace_whitespace" for
        verdadeiro, cada caractere de tabulação será substituído por
        um único espaço, que *não* é o mesmo que expansão de
        tabulação.

      Nota:

        Se "replace_whitespace" for falso, novas linhas podem aparecer
        no meio de uma linha e causar uma saída estranha. Por esta
        razão, o texto deve ser dividido em parágrafos (usando
        "str.splitlines()" ou similar) que são agrupados
        separadamente.

   drop_whitespace

      (padrão: "True") Se verdadeiro, os espaços em branco no início e
      no final de cada linha (após quebra automática, mas antes do
      recuo) são eliminados. O espaço em branco no início do
      parágrafo, entretanto, não será eliminado se não houver espaço
      em branco após ele. Se o espaço em branco eliminado ocupar uma
      linha inteira, a linha inteira será eliminada.

   initial_indent

      (padrão: "''") String que será anexada à primeira linha da saída
      com quebra de linha. Conta para o comprimento da primeira linha.
      A string vazia não recebe indentação.

   subsequent_indent

      (padrão: "''") String que será anexada a todas as linhas da
      saída com quebra de linha, exceto a primeira. Conta para o
      comprimento de cada linha, exceto a primeira.

   fix_sentence_endings

      (padrão: "False") Se verdadeiro, "TextWrapper" tenta detectar
      finais de sentenças e garantir que as sentenças sejam sempre
      separadas por exatamente dois espaços. Isso geralmente é
      desejado para texto em fonte monoespaçada. No entanto, o
      algoritmo de detecção de frase é imperfeito: ele presume que o
      final de uma frase consiste em uma letra minúscula seguida por
      uma de "'.'", "'!'" ou "'?'", possivelmente seguido por um de
      "'"'" ou ""'"", seguido por um espaço. Um problema com este
      algoritmo é que ele é incapaz de detectar a diferença entre
      "Dr." em

         [...] Dr. Frankenstein's monster [...]

      e "Spot." em

         [...] See Spot. See Spot run [...]

      "fix_sentence_endings" é falso por padrão

      Como o algoritmo de detecção de frase depende de
      "string.lowercase" para a definição de "letra minúscula" e de
      uma convenção de usar dois espaços após um ponto final para
      separar frases na mesma linha, ele é específico para textos em
      inglês.

   break_long_words

      (padrão: "True") Se verdadeiro, palavras maiores que "width"
      serão quebradas para garantir que nenhuma linha seja maior que
      "width". Se for falso, palavras longas não serão quebradas e
      algumas linhas poderão ser maiores que "width". (Palavras longas
      serão colocadas sozinhas em uma linha, a fim de minimizar o
      valor pelo qual "width" é excedido.)

   break_on_hyphens

      (padrão: "True") Se verdadeiro, a quebra ocorrerá
      preferencialmente em espaços em branco e logo após hífens em
      palavras compostas, como é habitual em inglês. Se for falso,
      apenas os espaços em branco serão considerados locais
      potencialmente bons para quebras de linha, mas você precisa
      definir "break_long_words" como falso se quiser palavras
      verdadeiramente inseparáveis. O comportamento padrão nas versões
      anteriores era sempre permitir a quebra de palavras hifenizadas.

   max_lines

      (padrão: "None") Se não for "None", então a saída conterá no
      máximo *max_lines* linhas, com *placeholder* aparecendo no final
      da saída.

      Adicionado na versão 3.4.

   placeholder

      (padrão: "' [...]'") String que aparecerá no final do texto de
      saída se ele tiver sido truncado.

      Adicionado na versão 3.4.

   "TextWrapper" também fornece alguns métodos públicos, análogos às
   funções de conveniência em nível de módulo:

   wrap(text)

      Quebra o parágrafo único em *text* (uma string) para que cada
      linha tenha no máximo "width" caracteres. Todas as opções de
      quebra de linha são obtidas dos atributos da instância
      "TextWrapper". Retorna uma lista de linhas de saída, sem novas
      linhas finais. Se a saída agrupada não tiver conteúdo, a lista
      retornada estará vazia.

   fill(text)

      Quebra o parágrafo único em *text* e retorna uma única string
      contendo o parágrafo quebrado.
