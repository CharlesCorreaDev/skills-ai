"rlcompleter" --- Função de autocomplemento para GNU readline
*************************************************************

**Código-fonte:** Lib/rlcompleter.py

======================================================================

O módulo "rlcompleter" define uma função de autocompletamento adequada
para ser passada para "set_completer()" no módulo "readline".

Quando este módulo é importado em uma plataforma Unix com o módulo
"readline" disponível, uma instância da classe "Completer" é criada
automaticamente e seu método "complete()" é definido como o
autocompletamento do readline. O método fornece o autocompletamento de
identificadores e palavras-chaves válidas do Python.

Exemplo:

   >>> import rlcompleter
   >>> import readline
   >>> readline.parse_and_bind("tab: complete")
   >>> readline. <TAB PRESSED>
   readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
   readline.__file__         readline.insert_text(      readline.set_completer(
   readline.__name__         readline.parse_and_bind(
   >>> readline.

O módulo "rlcompleter" é projetado para uso com o modo interativo do
Python. A menos que Python seja executado com a opção "-S", o módulo é
automaticamente importado e configurado (veja Configuração Readline).

Em plataformas sem "readline", a classe "Completer" definida por este
módulo ainda pode ser usada para propósitos personalizados.

class rlcompleter.Completer

   Os objetos Completer têm o seguinte método:

   complete(text, state)

      Retorna o próximo completamento possível para *text*.

      Quando chamado pelo módulo "readline", este método é chamado
      sucessivamente com "state == 0, 1, 2, ..." até que o método
      retorne "None".

      Se chamado para *text* que não inclui um caractere de ponto
      ("'.'"), ele será completado a partir dos nomes atualmente
      definidos em "__main__", "builtins" e palavras reservadas
      (conforme definido pelo módulo "keyword").

      Se chamado por um nome pontilhado, vai tentar avaliar qualquer
      coisa sem efeitos colaterais óbvios (as funções não serão
      avaliadas, mas pode levantar chamadas para "__getattr__()") até
      a última parte e encontrar correspondências para o resto por
      meio da função "dir()". Qualquer exceção levantada durante a
      avaliação da expressão é capturada, silenciada e "None" é
      retornado.
