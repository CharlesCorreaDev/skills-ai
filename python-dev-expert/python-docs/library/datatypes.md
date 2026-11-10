Tipos de Dados
**************

Os módulos descritos neste capítulo fornecem uma variedade de tipos de
dados especializados, como datas e horas, vetores de tipo fixo, filas
de heap, filas de extremidade dupla e enumerações.

O Python também fornece alguns tipos de dados embutidos, em especial
"list", "tuple", "dict", "frozendict", "set" e "frozenset". A classe
"str" é usada para armazenar strings Unicode, e as classes "bytes" e
"bytearray" são usadas para armazenar dados binários.

Os seguintes módulos estão documentados neste capítulo:

* "datetime" --- Tipos básicos de data e hora

  * Aware and naive objects

  * Constantes

  * Available types

    * Common properties

    * Determining if an object is aware or naive

  * "timedelta" objects

    * Examples of usage: "timedelta"

  * Objetos "date"

    * Examples of usage: "date"

  * "datetime" objects

    * Examples of usage: "datetime"

  * Objetos "time"

    * Examples of usage: "time"

  * "tzinfo" objects

  * "timezone" objects

  * "strftime()" and "strptime()" behavior

    * "strftime()" and "strptime()" format codes

    * Technical detail

* "zoneinfo" --- Suporte a fuso horário da IANA

  * Usando "ZoneInfo"

  * Fontes de dados

    * Configurando as fontes de dados

      * Configuração em tempo de compilação

      * Configuração do ambiente

      * Configuração em tempo de execução

  * A classe "ZoneInfo"

    * String representations

    * Pickle serialization

  * Funções

  * Globals

  * Exceptions and warnings

* "calendar" --- Funções gerais relacionadas ao calendário

  * Uso na linha de comando

* "collections" --- Tipos de dados de contêineres

  * Objetos "ChainMap"

    * Exemplos e Receitas de "ChainMap"

  * Objetos "Counter"

  * Objetos "deque"

    * Receitas de "deque"

  * Objetos "defaultdict"

    * Exemplos de "defaultdict"

  * Função de fábrica para tuplas com campos nomeados "namedtuple()"

  * Objetos "OrderedDict"

    * Exemplos e receitas de "OrderedDict"

  * Objetos "UserDict"

  * Objetos "UserList"

  * Objetos "UserString"

* "collections.abc" --- Classes Base Abstratas para Contêineres

  * Classes Base Abstratas de Coleções

  * Classes Base Abstrata de Coleções -- Descrições Detalhadas

  * Exemplos e receitas

* "heapq" --- Algoritmo de fila heap

  * Exemplos básicos

  * Other Applications

  * Notas de implementação da fila de prioridade

  * Teoria

* "bisect" --- Algoritmo de bisseção de vetor

  * Observações sobre desempenho

  * Buscando em listas ordenadas

  * Exemplos

* "array"--- Vetores eficientes de valores numéricos

* "weakref" --- Referências fracas

  * Objetos referência fraca

  * Exemplo

  * Objetos finalizadores

  * Comparando finalizadores com métodos "__del__()"

* "types" --- Criação de tipos dinâmicos e nomes para tipos embutidos

  * Criação de tipos dinâmicos

  * Tipos padrão do interpretador

  * Classes e funções de utilidades adicionais

  * Funções de utilidade de corrotina

* "copy" --- Operações de cópia profunda e cópia rasa

* "pprint" --- Impressão bonita de dados

  * Funções

  * Objetos PrettyPrinter

  * Exemplo

* "reprlib" --- Implementação alternativa à "repr()"

  * Objetos Repr

  * Estendendo objetos Repr

* "enum" --- Suporte a enumerações

  * Conteúdo do módulo

  * Data types

    * Nomes "__dunder__" suportados

    * Nomes "_sunder_" suportados

  * Utilities and decorators

  * Notas

* "graphlib" --- Funcionalidade para operar com estruturas do tipo
  grafo

  * Exceções
