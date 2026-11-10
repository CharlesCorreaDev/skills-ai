Constantes embutidas
********************

Um pequeno número de constantes são definidas no espaço de nomes
embutido da linguagem. São elas:

False

   O valor falso do tipo "bool". As atribuições a "False" são ilegais
   e levantam "SyntaxError".

True

   O valor verdadeiro do tipo "bool". As atribuições a "True" são
   ilegais e levantam "SyntaxError".

None

   Um objeto frequentemente usado para representar a ausência de um
   valor, como quando argumentos padrão não são passados para uma
   função. Atribuições a "None" são ilegais e levantam um
   "SyntaxError". "None" é a única instância do tipo "NoneType".

NotImplemented

   Um valor especial que deve ser retornado pelos métodos especiais
   binários (por exemplo, "__eq__()", "__lt__()", "__add__()",
   "__rsub__()", etc.) para indicar que a operação não foi
   implementada em relação ao outro tipo; pode ser retornado pelos
   métodos especiais binários in-place (por exemplo, "__imul__()",
   "__iand__()", etc.) para o mesmo propósito. Ele não deve ser
   avaliado em um contexto booleano. "NotImplemented" é a única
   instância do tipo "types.NotImplementedType".

   Nota:

     Quando um método binário (ou local) retorna "NotImplemented", o
     interpretador tentará a operação refletida no outro tipo (ou
     algum outro fallback, dependendo do operador). Se todas as
     tentativas retornarem "NotImplemented", o interpretador levantará
     uma exceção apropriada. Retornar incorretamente "NotImplemented"
     resultará em uma mensagem de erro enganosa ou no valor
     "NotImplemented" sendo retornado ao código Python.Consulte
     Implementando as operações aritméticas para ver exemplos.

   Cuidado:

     "NotImplemented" e "NotImplementedError" não são intercambiáveis.
     Esta constante deve ser usada somente conforme descrito acima;
     veja "NotImplementedError" para detalhes sobre o uso correto da
     exceção.

   Alterado na versão 3.9: A avaliação de "NotImplemented" em um
   contexto booleano foi descontinuada.

   Alterado na versão 3.14: A avaliação de "NotImplemented" em um
   contexto booleano agora levanta um "TypeError". Anteriormente, ele
   era avaliado como "True" e emitia um "DeprecationWarning" desde o
   Python 3.9.

Ellipsis

   O mesmo que o literal de elipse ""..."", um objeto frequentemente
   usado para indicar que algo foi omitido. A atribuição a "Ellipsis"
   é possível, mas a atribuição a "..." levanta um "SyntaxError".
   "Ellipsis" é a única instância do tipo "types.EllipsisType".

__debug__

   Esta constante é verdadeira se o Python não foi iniciado com uma
   opção "-O". Veja também a instrução "assert".

Nota:

  Os nomes "None", "False", "True" e "__debug__" não podem ser
  reatribuídos (atribuições a eles, mesmo como um nome de atributo,
  levantam "SyntaxError" ), para que possam ser consideradas
  "verdadeiras" constantes.


Constantes adicionadas pelo módulo "site"
=========================================

O módulo "site" (que é importado automaticamente durante a
inicialização, exceto se a opção de linha de comando "-S" for
fornecida) adiciona várias constantes ao espaço de nomes embutido.
Eles são úteis para o console do interpretador interativo e não devem
ser usados em programas.

quit(code=None)
exit(code=None)

   Objetos que, quando exibidos, exibem uma mensagem como "Use quit()
   or Ctrl-D (i.e. EOF) to exit" e, quando acessados diretamente no
   interpretador interativo ou chamados como funções, levantam
   "SystemExit" com o código de saída especificado.

help

   Objeto que, quando exibido, exibe a mensagem "Type help() for
   interactive help, or help(object) for help about object." e, quando
   acessado diretamente no interpretador interativo, invoca o sistema
   de ajuda embutido (veja "help()").

copyright
credits

   Objetos que ao serem impressos ou chamados, imprimem o texto dos
   direitos autorais ou créditos, respectivamente.

license

   Objeto que, quando impresso, imprime a mensagem "Type license() to
   see the full license text" e, quando chamado, exibe o texto
   completo da licença de maneira semelhante a um paginador (uma tela
   por vez).
