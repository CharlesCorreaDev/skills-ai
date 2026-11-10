"reprlib" --- Implementação alternativa à "repr()"
**************************************************

**Código-fonte:** Lib/reprlib.py

======================================================================

O módulo "reprlib" fornece um meio de produzir representações de
objetos com limites no tamanho das strings resultantes. Isso é usado
no depurador Python e pode ser útil em outros contextos também.

Este módulo fornece uma classe, uma instância e uma função.

class reprlib.Repr(*, maxlevel=6, maxtuple=6, maxlist=6, maxarray=5, maxdict=4, maxset=6, maxfrozenset=6, maxdeque=6, maxstring=30, maxlong=40, maxother=30, fillvalue='...', indent=None)

   Classe que fornece serviços de formatação úteis na implementação de
   funções semelhantes à embutida "repr()"; limites de tamanho para
   diferentes tipos de objetos são adicionados para evitar a geração
   de representações excessivamente longas.

   Os argumentos nomeados do construtor podem ser usados como um
   atalho para definir os atributos da instância de "Repr". O que
   significa que a inicialização a seguir:

      aRepr = reprlib.Repr(maxlevel=3)

   É equivalente a:

      aRepr = reprlib.Repr()
      aRepr.maxlevel = 3

   Consulte a seção Objetos Repr para obter mais informações sobre
   atributos "Repr".

   Alterado na versão 3.12: Permite que atributos sejam definidos por
   meio de argumentos nomeados.

reprlib.aRepr

   Esta é uma instância de "Repr" que é usada para fornecer a função
   "repr()" descrita abaixo. Alterar os atributos deste objeto afetará
   os limites de tamanho usados por "repr()" e pelo depurador Python.

reprlib.repr(obj)

   Este é o método "repr()" de "aRepr". Ele retorna uma string
   semelhante à retornada pela função embutida de mesmo nome, mas com
   limites na maioria dos tamanhos.

Além das ferramentas de limitação de tamanho, o módulo também fornece
um decorador para detectar chamadas recursivas para "__repr__()" e
substituir uma string de espaço reservado.

@reprlib.recursive_repr(fillvalue='...')

   Decorador para métodos "__repr__()" para detectar chamadas
   recursivas dentro da mesma thread. Se uma chamada recursiva for
   feita, o *fillvalue* é retornado; caso contrário, a chamada usual
   "__repr__()" é feita. Por exemplo:

      >>> from reprlib import recursive_repr
      >>> class MyList(list):
      ...     @recursive_repr()
      ...     def __repr__(self):
      ...         return '<' + '|'.join(map(repr, self)) + '>'
      ...
      >>> m = MyList('abc')
      >>> m.append(m)
      >>> m.append('x')
      >>> print(m)
      <'a'|'b'|'c'|...|'x'>

   Adicionado na versão 3.2.


Objetos Repr
============

Instâncias "Repr" fornecem vários atributos que podem ser usados para
fornecer limites de tamanho para as representações de diferentes tipos
de objetos e métodos que formatam tipos de objetos específicos.

Repr.fillvalue

   Esta string é exibida para referências recursivas. O padrão é
   "...".

   Adicionado na versão 3.11.

Repr.maxlevel

   Limite de profundidade na criação de representações recursivas. O
   padrão é "6".

Repr.maxdict
Repr.maxlist
Repr.maxtuple
Repr.maxset
Repr.maxfrozenset
Repr.maxdeque
Repr.maxarray

   Limites no número de entradas representadas para o tipo de objeto
   nomeado. O padrão é "4" para "maxdict", "5" para "maxarray" e "6"
   para os demais.

Repr.maxlong

   Número máximo de caracteres na representação para um inteiro. Os
   dígitos são omitidos a partir do meio. O padrão é "40".

Repr.maxstring

   Limite no número de caracteres na representação da string. Observe
   que a representação "normal" da string é usada como fonte de
   caracteres: se sequências de escape forem necessárias na
   representação, elas poderão ser distorcidas quando a representação
   for encurtada. O padrão é "30".

Repr.maxother

   Este limite é usado para controlar o tamanho de tipos de objetos
   para os quais nenhum método de formatação específico está
   disponível no objeto "Repr". Ele é aplicado de maneira semelhante a
   "maxstring". O padrão é "20".

Repr.indent

   Se este atributo for definido como "None" (o padrão), a saída será
   formatada sem quebras de linha ou recuo, como o padrão "repr()".
   Por exemplo:

      >>> example = [
      ...     1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']
      >>> import reprlib
      >>> aRepr = reprlib.Repr()
      >>> print(aRepr.repr(example))
      [1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham']

   Se "indent" for definido como uma string, cada nível de recursão
   será colocado em sua própria linha, recuado por essa string:

      >>> aRepr.indent = '-->'
      >>> print(aRepr.repr(example))
      [
      -->1,
      -->'spam',
      -->{
      -->-->'a': 2,
      -->-->'b': 'spam eggs',
      -->-->'c': {
      -->-->-->3: 4.5,
      -->-->-->6: [],
      -->-->},
      -->},
      -->'ham',
      ]

   Definir "indent" como um valor inteiro positivo se comporta como se
   fosse definido como uma string com esse número de espaços:

      >>> aRepr.indent = 4
      >>> print(aRepr.repr(example))
      [
          1,
          'spam',
          {
              'a': 2,
              'b': 'spam eggs',
              'c': {
                  3: 4.5,
                  6: [],
              },
          },
          'ham',
      ]

   Adicionado na versão 3.12.

Repr.repr(obj)

   O equivalente ao "repr()" embutido que usa a formatação imposta
   pela instância.

Repr.repr1(obj, level)

   Implementação recursiva usada por "repr()". Esta usa o tipo de
   *obj* para determinar qual método de formatação chamar, passando
   *obj* e *level*. Os métodos específicos de tipo devem chamar
   "repr1()" para realizar a formatação recursiva, com "level - 1"
   para o valor de *level* na chamada recursiva.

Repr.repr_TYPE(obj, level)

   Métodos de formatação para tipos específicos são implementados como
   métodos com um nome baseado no nome do tipo. No nome do método,
   **TYPE** é substituído por "'_'.join(type(obj).__name__.split())".
   O despacho para esses métodos é tratado por "repr1()". Métodos
   específicos de tipo que precisam formatar um valor recursivamente
   devem chamar "self.repr1(subobj, level - 1)".


Estendendo objetos Repr
=======================

O uso de despacho dinâmico por "Repr.repr1()" permite que subclasses
de "Repr" adicionem suporte para tipos de objetos embutidos adicionais
ou modifiquem o tratamento de tipos já suportados. Este exemplo mostra
como suporte especial para objetos arquivo pode ser adicionado:

   import reprlib
   import sys

   class MyRepr(reprlib.Repr):

       def repr_TextIOWrapper(self, obj, level):
           if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
               return obj.name
           return repr(obj)

   aRepr = MyRepr()
   print(aRepr.repr(sys.stdin))         # exibe '<stdin>'

   <stdin>
