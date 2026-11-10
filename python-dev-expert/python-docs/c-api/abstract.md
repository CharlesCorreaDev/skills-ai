Camada de Objetos Abstratos
***************************

As funções neste capítulo interagem com objetos Python
independentemente do seu tipo, ou com classes amplas de tipos de
objetos (por exemplo, todos os tipos numéricos ou todos os tipos de
sequência). Quando usadas em tipos de objetos para os quais não se
aplicam, elas irão levantar uma exceção Python.

Não é possível usar essas funções em objetos que não foram
inicializados corretamente, como um objeto de lista criado por
"PyList_New()", mas cujos itens ainda não foram definidos para algum
valor diferente de "NULL".

* Protocolo de objeto

* Protocolo de chamada

  * O protocolo *tp_call*

  * O protocolo vectorcall

    * Controle de recursão

    * API de suporte à chamada de vetores

  * API de chamada de objetos

  * API de suporte a chamadas

* Protocolo de número

* Protocolo de sequência

* Protocolo de mapeamento

* Protocolo Iterador

* Protocolo de buffer

  * Estrutura de Buffer

  * Tipos de solicitação do buffer

    * campos independentes do pedido

    * apenas em formato

    * forma, avanços, suboffsets

    * requisições contíguas

    * requisições compostas

  * Vetores Complexos

    * Estilo NumPy: forma e avanços

    * Estilo-PIL: forma, avanços e suboffsets

  * Funções relacionadas ao Buffer
