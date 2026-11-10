"copy" --- Operações de cópia profunda e cópia rasa
***************************************************

**Código-fonte:** Lib/copy.py

======================================================================

As instruções de atribuição no Python não copiam objetos; elas criam
ligações entre um destino e um objeto. Para coleções mutáveis ou que
contêm itens mutáveis, às vezes é necessária uma cópia para que seja
possível alterar uma sem alterar a outra. Este módulo fornece
operações genéricas de cópia profunda e rasa (explicadas abaixo).

Resumo da interface:

copy.copy(obj)

   Retorna uma cópia rasa de *obj*.

copy.deepcopy(obj[, memo])

   Retorna uma cópia profunda  de *obj*.

copy.replace(obj, /, **changes)

   Cria um novo objeto do mesmo tipo que *obj*, substituindo os campos
   pelos valores de *changes*.

   Adicionado na versão 3.13.

exception copy.Error

   Levantada para erros específicos do módulo.

A diferença entre cópia profunda e rasa é relevante apenas para
objetos compostos (objetos que contêm outros objetos, como listas ou
instâncias de classe):

* Uma *cópia rasa* constrói um novo objeto composto e, na medida do
  possível, insere nele *referências* aos objetos encontrados no
  original.

* Uma *cópia profunda* constrói um novo objeto composto e então,
  recursivamente, insere nele *cópias* dos objetos encontrados no
  original.

Frequentemente, existem dois problemas com operações de cópia profunda
que não existem com operações de cópia rasa:

* Objetos recursivos (objetos compostos que, direta ou indiretamente,
  contêm uma referência a si mesmos) podem causar um laço recursivo.

* Como a cópia profunda copia tudo, ela pode copiar muito, incluindo
  dados que devem ser compartilhados entre as cópias.

A função "deepcopy()" evita esses problemas:

* mantendo um dicionário "memo" de objetos já copiados durante a
  passagem de cópia atual; e

* permitindo que as classes definidas pelo usuário substituam a
  operação de cópia ou o conjunto de componentes copiados.

Este módulo não copia tipos como módulo, método, stack trace (situação
da pilha de execução), quadro de empilhamento, arquivo, soquete,
janela ou outros tipos semelhantes. Ele "copia" funções e classes
(rasas e profundamente), devolvendo o objeto original inalterado; isso
é compatível com a maneira como estes itens são tratados pelo módulo
"pickle".

Cópias rasas (*shallow copies*) de muitas coleções podem ser feitas
utilizando o método "copy()" correspondente (como "list.copy()",
"dict.copy()" ou "set.copy()"), e de sequências (como listas ou
*bytearrays*) criando uma fatia (*slice*) de toda a sequência
("sequence[:]"). No entanto, esses métodos e o fatiamento podem criar
uma instância do tipo base ao copiar uma instância de uma subclasse,
enquanto "copy.copy()" normalmente retorna uma instância do mesmo
tipo.

As classes podem usar as mesmas interfaces para controlar a cópia que
usam para controlar a serialização com pickle. Veja a descrição do
módulo "pickle" para obter informações sobre esses métodos. Na
verdade, o módulo "copy" usa as funções pickle registradas do módulo
"copyreg".

Para que uma classe defina sua própria implementação de cópia, ela
pode definir métodos especiais "__copy__()" e "__deepcopy__()".

object.__copy__(self)

   Chamado para implementar a operação de cópia rasa; não é fornecido
   nenhum argumento adicional.

object.__deepcopy__(self, memo)

   Chamado para implementar a operação de cópia profunda; é passado um
   argumento, o dicionário *memo*. Se a implementação "__deepcopy__"
   precisar fazer uma cópia profunda de um componente, ela deve chamar
   a função "deepcopy()" com o componente como primeiro argumento e o
   dicionário *memo* como segundo argumento. O dicionário *memo* deve
   ser tratado como um objeto opaco.

A função "copy.replace()" é mais limitada que "copy()" e "deepcopy()",
e tem suporte apenas a tuplas nomeadas criadas por "namedtuple()",
"dataclasses" e outras classes que definem o método "__replace__()".

object.__replace__(self, /, **changes)

   Este método deve criar um novo objeto do mesmo tipo, substituindo
   os campos pelos valores de *changes*.

   Adicionado na versão 3.13.

Ver também:

  Módulo "pickle"
     Discussão dos métodos especiais usados para dar suporte à
     recuperação e à restauração do estado do objeto.
