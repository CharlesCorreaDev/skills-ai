Suporte a implementação de Objetos
**********************************

Este capítulo descreve as funções, tipos e macros usados ao definir
novos tipos de objeto.

* Alocando objetos na heap

  * Apelidos suavemente descontinuados

* Ciclo de vida do objeto

  * Eventos de vida

  * Destruição de isolado cíclico

  * Funções

* Estruturas comuns de objetos

  * Macros e tipos de objetos base

  * Implementing functions and methods

  * Accessing attributes of extension types

    * Member flags

    * Member types

    * Defining Getters and Setters

* Estruturas de objetos tipo

  * Referências rápidas

    * "slots tp"

    * sub-slots

    * slot typedefs

  * PyTypeObject Definition

  * PyObject Slots

  * PyVarObject Slots

  * PyTypeObject Slots

  * Static Types

  * Tipos no heap

  * Number Object Structures

  * Mapping Object Structures

  * Sequence Object Structures

  * Buffer Object Structures

  * Async Object Structures

  * Slot Type typedefs

  * Exemplos

* Suporte a Coleta Cíclica de Lixo

  * Traversal

    * Traversal-safe functions

    * "DuringGC" functions

  * Controlando o estado do coletor de lixo

  * Querying Garbage Collector State
