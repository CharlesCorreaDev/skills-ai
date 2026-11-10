Camada de Objetos Concretos
***************************

As funções neste capítulo são específicas para certos tipos de objetos
Python. Passar para eles um objeto do tipo errado não é uma boa ideia;
se você receber um objeto de um programa Python e não tiver certeza de
que ele tem o tipo certo, primeiro execute uma verificação de tipo;
por exemplo, para verificar se um objeto é um dicionário, use
"PyDict_Check()". O capítulo está estruturado como a "árvore
genealógica" dos tipos de objetos Python.

Aviso:

  Enquanto as funções descritas neste capítulo verificam
  cuidadosamente o tipo de objetos passados, muitos deles não
  verificam a passagem de "NULL" em vez de um objeto válido. Permitir
  a passagem de "NULL" pode causar violações ao acesso à memória e
  encerramento imediato do interpretador.


Objetos Fundamentais
====================

Esta seção descreve os objetos de tipo Python e o objeto singleton
"None".

* Objetos tipo

  * Creating Heap-Allocated Types

    * Type slot IDs

  * Soft-deprecated API

* O Objeto "None"


Objetos Numéricos
=================

* Objetos Inteiros

  * Build configuration

  * Export API

  * PyLongWriter API

  * Deprecated API

* Objetos Booleanos

* Objetos de ponto flutuante

  * As funções Pack e Unpack

    * Funções Pack

    * Funções de Unpack

* Objetos números complexos

  * Números complexos como estruturas C.


Objetos Sequência
=================

Operações genéricas em objetos de sequência foram discutidas no
capítulo anterior; Esta seção lida com os tipos específicos de objetos
sequência que são intrínsecos à linguagem Python.

* Objetos Bytes

* PyBytesWriter

  * Create, Finish, Discard

  * High-level API

  * Getters

  * Low-level API

  * Example creating the string "b'abc'"

  * Update "PyBytes_FromStringAndSize()" code

  * Update "_PyBytes_Resize()" code

* Objetos byte array

  * Macros para verificação de tipo

  * Funções diretas da API

  * Macros

* Objetos Unicode e Codecs

  * Objetos Unicode

    * Tipo Unicode

    * Propriedade de caracteres Unicode

    * Creating and accessing Unicode strings

    * Locale Encoding

    * File System Encoding

    * wchar_t Support

  * Built-in Codecs

    * Generic Codecs

    * UTF-8 Codecs

    * UTF-32 Codecs

    * UTF-16 Codecs

    * UTF-7 Codecs

    * Unicode-Escape Codecs

    * Raw-Unicode-Escape Codecs

    * Latin-1 Codecs

    * ASCII Codecs

    * Character Map Codecs

    * MBCS codecs for Windows

  * Methods and Slot Functions

  * PyUnicodeWriter

  * Deprecated API

* Objeto tupla

* Objetos sequência de estrutura

* Objeto List


Coleções
========

* Dictionary objects

  * Objetos de visão de dicionário

  * Frozen dictionary objects

  * Ordered dictionaries

* Objeto Set

  * Deprecated API


Objetos Função
==============

* Objetos Função

* Objetos de Método de Instância

* Objetos método

* Objeto célula

* Objetos código

* Sinalizadores de objetos código

* Informação adicional


Outros Objetos
==============

* File objects

  * Soft-deprecated API

* Objetos do Módulo

  * Module definition

    * Metadata slots

    * Feature slots

    * Creation and initialization slots

  * Module state

    * Slots for defining module state

    * Module token

  * Creating extension modules dynamically

  * Module definition struct

  * Support functions

    * Module lookup (single-phase initialization)

* Objetos Iteradores

  * Objetos intervalo

  * Tipos de iteradores embutidos

  * Outros objetos iteradores

* Objetos descritores

  * Descritores embutidos

* Objetos Slice

  * Objeto Ellipsis

* Objetos MemoryView

* Objetos buffer serializados com pickle

* Objetos referência fraca

* Capsules

* Objetos sentinel

* Objetos quadro

  * Frame locals proxies

  * Legacy local variable APIs

  * Internal frames

* Objetos Geradores

  * Objetos geradores assíncronos

  * Deprecated API

* Objetos corrotina

* Objetos de variáveis de contexto

* Objetos de indicação de tipos


API C para módulos de extensão
==============================

* API C de curses

* Dados internos

* Objetos DateTime

* Dados internos
