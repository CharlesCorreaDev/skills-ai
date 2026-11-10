"array"--- Vetores eficientes de valores numéricos
**************************************************

======================================================================

This module defines an object type which can compactly represent an
array of basic values: characters, integers, floating-point numbers,
complex numbers.  Arrays are mutable *sequence* types and behave very
much like lists, except that the type of objects stored in them is
constrained.  The type is specified at object creation time by using a
*type code*, which is a single character.  The following type codes
are defined:

+-------------+----------------------+---------------------+-------------------------+---------+
| Código de   | Tipo em C            | Tipo em Python      | Tamanho mínimo em bytes | Notas   |
| tipo        |                      |                     |                         |         |
|=============|======================|=====================|=========================|=========|
| "'b'"       | signed char          | int                 | 1                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'B'"       | unsigned char        | int                 | 1                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'u'"       | wchar_t              | Caractere unicode   | 2                       | (1)     |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'w'"       | Py_UCS4              | Caractere unicode   | 4                       | (2)     |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'h'"       | signed short         | int                 | 2                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'H'"       | unsigned short       | int                 | 2                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'i'"       | signed int           | int                 | 2                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'I'"       | unsigned int         | int                 | 2                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'l'"       | signed long          | int                 | 4                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'L'"       | unsigned long        | int                 | 4                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'q'"       | signed long long     | int                 | 8                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'Q'"       | unsigned long long   | int                 | 8                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'e'"       | _Float16             | ponto flutuante     | 2                       | (3)     |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'f'"       | ponto flutuante      | ponto flutuante     | 4                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'d'"       | double               | ponto flutuante     | 8                       |         |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'Zf'"      | float complex        | complexo            | 8                       | (4)     |
+-------------+----------------------+---------------------+-------------------------+---------+
| "'Zd'"      | double complex       | complexo            | 16                      | (4)     |
+-------------+----------------------+---------------------+-------------------------+---------+

Notas:

1. Pode ser de 16 ou 32 bits dependendo da plataforma.

   Alterado na versão 3.9: "array('u')" agora usa "wchar_t" como tipo
   C no lugar do descontinuado "Py_UNICODE". Essa mudança não afeta o
   comportamento pois "Py_UNICODE" é um apelido para "wchar_t" desde
   Python 3.3.

   Descontinuado desde a versão 3.3, será removido na versão 3.16: Por
   favor, migre para o código de tipo "'w'".

2. Adicionado na versão 3.13.

3. The IEEE 754 binary16 "half precision" type was introduced in the
   2008 revision of the IEEE 754 standard. This type is not widely
   supported by C compilers.  It's available as _Float16 type, if the
   compiler supports the Annex H of the C23 standard.

   Adicionado na versão 3.15.

4. Complex types ("Zf" and "Zd") are available unconditionally,
   regardless on support for complex types (the Annex G of the C11
   standard) by the C compiler. As specified in the C11 standard, each
   complex type is represented by a two-element C array containing,
   respectively, the real and imaginary parts.

   Adicionado na versão 3.15.

Ver também:

  The ctypes and struct modules, as well as third-party modules like
  numpy, use similar -- but slightly different -- type codes.

A representação dos valores é definida pela arquitetura da máquina,
mais especificamente da implementação do C. O tamanho real pode ser
acessado pelo atributo "array.itemsize".

O módulo define o seguinte item:

array.typecodes

   A tuple with all available type codes.

   Alterado na versão 3.15: The type changed from "str" to "tuple".

O módulo define o seguinte tipo:

class array.array(typecode[, initializer])

   Um novo vetor cujos itens são restritos por *typecode* e
   inicializados a partir do valor opcional *initializer*, que deve
   ser um objeto "bytes" ou "bytearray", uma string Unicode ou
   iterável sobre elementos do tipo apropriado.

   Se for fornecido um objeto "bytes" ou "bytearray", o inicializador
   é passado para o método "frombytes()" do novo vetor; se for
   fornecida uma string Unicode, o inicializador é passado para o
   método "fromunicode()"; caso contrário, o iterador do inicializador
   é passado para o método "extend()" para adicionar itens iniciais ao
   vetor.

   Array objects support the ordinary mutable *sequence* operations of
   indexing, slicing, concatenation, and multiplication.  When using
   slice assignment, the assigned value must be an array object with
   the same type code; in all other cases, "TypeError" is raised.
   Array objects also implement the buffer interface, and may be used
   wherever *bytes-like objects* are supported.

   Arrays are generic over the type of their contents.

   Levanta um evento de auditoria "array.__new__" com os argumentos
   "typecode", "initializer".

   typecode

      O caractere de código de tipo usado para criar o vetor.

   itemsize

      O tamanho em bytes de um item do vetor em representação interna.

   append(value, /)

      Append a new item with the specified value to the end of the
      array.

   buffer_info()

      Retorna uma tupla "(address, length)" com o endereço corrente da
      memória e o tamanho em elementos do buffer usado para armazenar
      conteúdos do vetor. O tamanho do buffer da memória em bytes pode
      ser computado como "array.buffer_info()[1] * array.itemsize".
      Isso é ocasionalmente útil quando se está trabalhando com
      interfaces I/O de baixo nível (inerentemente inseguras) que
      precisam de endereços de memória, como algumas operações
      "ioctl()". Os números retornados são válidos enquanto o vetor
      existir e nenhuma operação de alteração de tamanho for aplicada
      a ele.

      Nota:

        Quando se está usando vetores de código escrito em C ou C++ (o
        único jeito efetivo de usar essa informação), faz mais sentido
        usar a interface do buffer suportada pelos vetores. Esse
        método é mantido para retrocompatibilidade e deve ser evitado
        em código novo. A interface de buffers está documentada em
        Protocolo de buffer.

   byteswap()

      "Byteswap" all items of the array.  This is only supported for
      values which are 1, 2, 4, 8 or 16 bytes in size; for other types
      of values, "RuntimeError" is raised.  It is useful when reading
      data from a file written on a machine with a different byte
      order.  Note, that for complex types the order of components
      (the real part, followed by imaginary part) is preserved.

   count(value, /)

      Return the number of occurrences of *value* in the array.

   extend(iterable, /)

      Acrescenta os itens de *iterable* ao final do vetor. Se
      *iterable* for outro vetor, ele deve ter *exatamente* o mesmo
      código de tipo; senão, ocorrerá uma "TypeError". Se *iterable*
      não for um vetor, ele deve ser iterável e seus elementos devem
      ser do tipo correto para ser acrescentado ao vetor.

   frombytes(buffer, /)

      Adiciona itens do *objeto bytes ou similar*, interpretando seu
      conteúdo como um vetor de valores de máquina (como se tivesse
      sido lido de um arquivo usando o método "fromfile()").

      Adicionado na versão 3.2: "fromstring()" foi renomeado para
      "frombytes()" para maior clareza.

   fromfile(f, n, /)

      Lê *n* itens (como valores de máquinas) do *objeto arquivo* *f*
      e adiciona-os ao fim do vetor. Se estão disponíveis menos de *n*
      itens, "EOFError" é levantada, mas os itens disponíveis ainda
      são inseridos ao final do vetor.

   fromlist(list, /)

      Adiciona itens de *list*.  Isso é equivalente a "for x in list:
      a.append(x)" exceto que se ocorrer um erro de tipo, o vetor não
      é alterado.

   fromunicode(ustr, /)

      Estende este vetor com dados da string Unicode fornecida. O
      vetor deve ter o código de tipo "'u'" ou "'w'"; caso contrário,
      uma "ValueError" é levantada. Use
      "array.frombytes(unicodestring.encode(enc))" para anexar dados
      Unicode a um vetor de algum outro tipo.

   index(value[, start[, stop]])

      Return the smallest *i* such that *i* is the index of the first
      occurrence of *value* in the array.  The optional arguments
      *start* and *stop* can be specified to search for *value* within
      a subsection of the array.  Raise "ValueError" if *value* is not
      found.

      Alterado na versão 3.10: Adicionados os parâmetros opcionais
      *start e *stop*.

   insert(index, value, /)

      Insert a new item *value* in the array before position *index*.
      Negative values are treated as being relative to the end of the
      array.

   pop(index=-1, /)

      Remove o item com o índice *i* do vetor e retorna este item. O
      valor padrão do argumento opcional é "-1", assim por padrão o
      último item é removido e retornado.

   remove(value, /)

      Remove the first occurrence of *value* from the array.

   clear()

      Remove todos os elementos do vetor.

      Adicionado na versão 3.13.

   reverse()

      Inverte a ordem dos itens no vetor.

   tobytes()

      Devolve os itens do vetor como um vetor de valores de máquina
      com a representação em bytes (a mesma sequência de bytes que
      seria escrita pelo método "tofile()".)

      Adicionado na versão 3.2: "tostring()" foi nomeado para
      "tobytes()" para maior clareza.

   tofile(f, /)

      Escreve todos os itens (como valores de máquinas) para o *objeto
      arquivo* *f*.

   tolist()

      Devolve os itens do vetor como uma lista comum.

   tounicode()

      Devolve os itens do vetor como uma string Unicode. O vetor deve
      ser do tipo "'u'" ou "'w'"; caso contrário "ValueError" é
      levantada. Use "array.tobytes().decode(enc)" para obter uma
      string Unicode de um vetor de outros tipos.

A representação em string de objetos vetor tem o formato
"array(typecode, initializer)". O *initializer* é omitido se o vetor
estiver vazio; caso contrário, é uma string Unicode se o *typecode*
for "'u'" ou "'w'"; caso contrário, é uma lista de números. A
representação em string pode ser convertida novamente para um array
com o mesmo tipo e valor usando "eval()", desde que a classe "array"
tenha sido importada usando "from array import array". As variáveis
"inf" e "nan" também devem ser definidas se contiverem valores de
ponto flutuante correspondentes. Exemplos:

   array('l')
   array('w', 'hello \u2641')
   array('l', [1, 2, 3, 4, 5])
   array('d', [1.0, 2.0, 3.14, -inf, nan])

Ver também:

  Módulo "struct"
     Empacotamento e desempacotamento de dados binários heterogêneos.

  NumPy
     O pacote NumPy define outro tipo de vetor.
