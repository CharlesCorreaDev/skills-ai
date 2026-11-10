Conteúdo da Documentação Python
*******************************

* O que há de novo no Python

  * O que há de novo no Python 3.15

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * **PEP 810**: Importações preguiçosas explícitas

      * **PEP 814**: Adiciona o tipo embutido frozendict

      * **PEP 661**: Adiciona o tipo embutido sentinela

      * **PEP 799**: Um pacote de perfilamento dedicado

      * Tachyon: Perfilador de amostragem estatística de alta
        frequência

      * **PEP 831**: Ponteiros de quadros habilitados por padrão

      * **PEP 798**: Desempacotamento em compreensões

      * **PEP 829**: Arquivos de configuração de inicialização de
        pacote

      * **PEP 803**: ABI Estável para construções com threads livres

      * **PEP 788**: Protegendo a API C de finalização do
        interpretador

      * Mensagens de erro melhoradas

    * Outras mudanças na linguagem

    * Console interativo padrão

    * Novos módulos

      * math.integer

    * Módulos melhorados

      * argparse

      * array

      * ast

      * asyncio

      * base64

      * binascii

      * calendar

      * collections

      * concurrent.futures

      * contextlib

      * ctypes

      * dataclasses

      * dbm

      * difflib

      * email

      * faulthandler

      * functools

      * gc

      * hashlib

      * http.client

      * http.server

      * importlib.metadata

      * inspect

      * json

      * locale

      * math

      * mimetypes

      * mmap

      * os

      * os.path

      * pathlib

      * pdb

      * pickle

      * pickletools

      * pprint

      * re

      * resource

      * shelve

      * socket

      * sqlite3

      * ssl

      * subprocess

      * symtable

      * sys

      * sys.monitoring

      * tarfile

      * threading

      * timeit

      * tkinter

      * tokenize

      * tomllib

      * types

      * typing

      * unicodedata

      * unittest

      * urllib.parse

      * venv

      * avisos

      * wave

      * webbrowser

      * xml

      * xml.parsers.expat

      * zlib

    * Otimizações

      * base64 e binascii

      * csv

      * Compilador JIT experimental atualizado

    * Removidos

      * ast

      * collections.abc

      * ctypes

      * datetime

      * glob

      * http.server

      * importlib

      * importlib.resources

      * pathlib

      * platform

      * sre_*

      * sysconfig

      * threading

      * types

      * typing

      * wave

      * zipimport

    * Descontinuados

      * Novas descontinuações

      * Remoção pendente no Python 3.16

      * Remoção pendente no Python 3.17

      * Remoção pendente no Python 3.18

      * Remoção pendente no Python 3.19

      * Remoção pendente no Python 3.20

      * Remoção pendente em versões futuras

      * descontinuações suave

    * Alterações na API C

      * Novas funcionalidades

      * Alterações na API C

      * APIs C removidas

      * APIs C descontinuadas

    * Alterações na construção

    * Portando para o Python 3.15

    * Alterações notáveis no 3.15.2

      * importlib

      * ssl

  * O que há de novo no Python 3.14

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * **PEP 649** e **PEP 749**: avaliação adiada de anotações

      * **PEP 734**: múltiplos interpretadores na biblioteca padrão

      * **PEP 750**: literais de string template

      * **PEP 768**: interface segura para depurador externo

      * Um novo tipo de interpretador

      * Melhorias no modo com threads livres

      * Mensagens de erro melhoradas

      * **PEP 784**: suporte ao Zstandard na biblioteca padrão

      * Capacidades de introspecção assíncrona

      * Controle de avisos seguros simultâneos

    * Outras mudanças na linguagem

      * Embutidos

      * Linha de comando e ambiente

      * PEP 758: permite expressões "except" e "except*" sem
        parênteses

      * PEP 765: fluxo de controle em blocos "finally"

      * Coleta de lixo

      * Console interativo padrão

    * Novos módulos

    * Módulos melhorados

      * argparse

      * ast

      * asyncio

      * calendar

      * concurrent.futures

      * configparser

      * contextvars

      * ctypes

      * curses

      * datetime

      * decimal

      * difflib

      * dis

      * errno

      * faulthandler

      * fnmatch

      * fractions

      * functools

      * getopt

      * getpass

      * graphlib

      * heapq

      * hmac

      * http

      * imaplib

      * inspect

      * io

      * json

      * linecache

      * logging.handlers

      * math

      * mimetypes

      * multiprocessing

      * operador

      * os

      * os.path

      * pathlib

      * pdb

      * pickle

      * platform

      * pydoc

      * re

      * socket

      * ssl

      * struct

      * symtable

      * sys

      * sys.monitoring

      * sysconfig

      * tarfile

      * threading

      * tkinter

      * turtle

      * types

      * typing

      * unicodedata

      * unittest

      * urllib

      * uuid

      * webbrowser

      * zipfile

    * Otimizações

      * asyncio

      * base64

      * bdb

      * difflib

      * gc

      * io

      * pathlib

      * pdb

      * textwrap

      * uuid

      * zlib

    * Removidos

      * argparse

      * ast

      * asyncio

      * email

      * importlib.abc

      * itertools

      * pathlib

      * pkgutil

      * pty

      * sqlite3

      * urllib

    * Descontinuados

      * Novas descontinuações

      * Remoção pendente no Python 3.15

      * Remoção pendente no Python 3.16

      * Remoção pendente no Python 3.17

      * Remoção pendente no Python 3.18

      * Remoção pendente no Python 3.19

      * Remoção pendente no Python 3.20

      * Remoção pendente em versões futuras

    * Alterações de bytecode do CPython

      * Pseudoinstruções

    * Alterações na API C

      * API C de configuração do Python

      * Novos recursos na API C

      * Mudanças na API C limitada

      * APIs C removidas

      * APIs C descontinuadas

        * Remoção pendente no Python 3.15

        * Remoção pendente no Python 3.16

        * Remoção pendente no Python 3.18

        * Remoção pendente em versões futuras

    * Alterações na construção

      * "build-details.json"

      * Descontinuação de assinaturas PGP

      * Python com threads livres é oficialmente suportado

      * Versões binárias para o compilador experimental just-in-time

    * Portando para o Python 3.14

      * Alterações na API Python

      * Mudanças em anotações (**PEP 649** e **PEP 749**)

        * Implicações para o código anotado

        * Implicações para leitores de "__annotations__"

        * Mudanças relacionadas

        * "from __future__ import annotations"

      * Alterações na API C

    * Alterações notáveis no 3.14.5

      * gc

  * O que há de novo no Python 3.13

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * Um melhor interpretador interativo

      * Mensagens de erro melhoradas

      * CPython com threads livres

      * Um compilador just-in-time (JIT) experimental

      * Definidas semânticas de mutação para "locals()"

      * Suporte para plataformas móveis

    * Outras mudanças na linguagem

    * Novos módulos

    * Módulos melhorados

      * argparse

      * array

      * ast

      * asyncio

      * base64

      * compileall

      * concurrent.futures

      * configparser

      * copy

      * ctypes

      * dbm

      * dis

      * doctest

      * email

      * enum

      * fractions

      * glob

      * importlib

      * io

      * ipaddress

      * itertools

      * marshal

      * math

      * mimetypes

      * mmap

      * multiprocessing

      * os

      * os.path

      * pathlib

      * pdb

      * queue

      * random

      * re

      * shutil

      * site

      * sqlite3

      * ssl

      * statistics

      * subprocess

      * sys

      * tempfile

      * time

      * tkinter

      * traceback

      * types

      * typing

      * unicodedata

      * venv

      * warnings

      * xml

      * zipimport

    * Otimizações

    * Módulos e APIs removidas

      * PEP 594: remove "baterias descarregadas" da biblioteca padrão

      * 2to3

      * embutidos

      * configparser

      * importlib.metadata

      * locale

      * opcode

      * optparse

      * pathlib

      * re

      * tkinter.tix

      * turtle

      * typing

      * unittest

      * urllib

      * webbrowser

    * Novas descontinuações

      * Remoção pendente no Python 3.14

      * Remoção pendente no Python 3.15

      * Remoção pendente no Python 3.16

      * Remoção pendente no Python 3.17

      * Remoção pendente no Python 3.18

      * Remoção pendente no Python 3.19

      * Remoção pendente no Python 3.20

      * Remoção pendente em versões futuras

    * Alterações de bytecode do CPython

    * Alterações na API C

      * Novas funcionalidades

      * Alterações na API C

      * Mudanças na API C Limitada

      * APIs C removidas

      * APIs C descontinuadas

        * Remoção pendente no Python 3.14

        * Remoção pendente no Python 3.15

        * Remoção pendente no Python 3.16

        * Remoção pendente no Python 3.18

        * Remoção pendente em versões futuras

    * Mudanças na construção

    * Portando para o Python 3.13

      * Alterações na API Python

      * Alterações na API C

    * Mudanças em teste de regressão

  * O que há de novo no Python 3.12

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * PEP 695: Sintaxe do parâmetro de tipo

      * PEP 701: Formalização sintática de f-strings

      * PEP 684: Uma GIL por interpretador

      * PEP 669: Monitoramento de baixo impacto para CPython

      * PEP 688: Tornando o protocolo de buffer acessível no Python

      * PEP 709: Fazendo inline de compreensão

      * Mensagens de erro melhoradas

    * Novos recursos relacionados a dicas de tipo

      * PEP 692: Usando "TypedDict" para tipagem mais precisa de
        "**kwargs"

      * PEP 698: substitui decorador para tipagem estática

    * Outras mudanças na linguagem

    * Novos módulos

    * Módulos melhorados

      * array

      * asyncio

      * calendar

      * csv

      * dis

      * fractions

      * importlib.resources

      * inspect

      * itertools

      * math

      * os

      * os.path

      * pathlib

      * platform

      * pdb

      * random

      * shutil

      * sqlite3

      * statistics

      * sys

      * tempfile

      * threading

      * tkinter

      * tokenize

      * types

      * typing

      * unicodedata

      * unittest

      * uuid

    * Otimizações

    * Alterações de bytecode do CPython

    * Ferramentas e daemons

    * Descontinuados

      * Remoção pendente no Python 3.13

      * Remoção pendente no Python 3.14

      * Remoção pendente no Python 3.15

      * Remoção pendente no Python 3.16

      * Remoção pendente no Python 3.17

      * Remoção pendente no Python 3.19

      * Remoção pendente no Python 3.20

      * Remoção pendente em versões futuras

    * Removidos

      * asynchat e asyncore

      * configparser

      * distutils

      * ensurepip

      * enum

      * ftplib

      * gzip

      * hashlib

      * importlib

      * imp

      * io

      * locale

      * smtpd

      * sqlite3

      * ssl

      * unittest

      * webbrowser

      * xml.etree.ElementTree

      * zipimport

      * Outros

    * Portando para Python 3.12

      * Alterações na API Python

    * Mudanças na construção

    * Alterações na API C

      * Novas funcionalidades

      * Portando para Python 3.12

      * Descontinuados

        * Remoção pendente no Python 3.14

        * Remoção pendente no Python 3.15

        * Remoção pendente no Python 3.16

        * Remoção pendente em versões futuras

      * Removidos

  * O que há de novo no Python 3.11

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * PEP 657: Localizações de erros refinadas em tracebacks

      * PEP 654: Grupos de exceção e "except*"

      * PEP 678: Exceções podem ser enriquecidas com notas

      * Melhorias no inicializador "py.exe" do Windows

    * Novos recursos relacionados a dicas de tipo

      * PEP 646: Genéricos variádicos

      * PEP 655: Marcando itens "TypedDict" individuais como
        obrigatórios ou não obrigatórios

      * PEP 673: Tipo "Self"

      * PEP 675: Tipo de string literal arbitrário

      * PEP 681: Transformações de classe de dados

      * PEP 563 pode não ser o futuro

    * Outras mudanças na linguagem

    * Outras mudanças na implementação do CPython

    * Novos módulos

    * Módulos melhorados

      * asyncio

      * contextlib

      * dataclasses

      * datetime

      * enum

      * fcntl

      * fractions

      * functools

      * gzip

      * hashlib

      * IDLE e idlelib

      * inspect

      * locale

      * logging

      * math

      * operator

      * os

      * pathlib

      * re

      * shutil

      * socket

      * sqlite3

      * string

      * sys

      * sysconfig

      * tempfile

      * threading

      * time

      * tkinter

      * traceback

      * typing

      * unicodedata

      * unittest

      * venv

      * warnings

      * zipfile

    * Otimizações

    * CPython mais rápido

      * Inicialização mais rápida

        * Importações congeladas/objetos de código estático

      * Tempo de execução mais rápido

        * Quadros Python menos custosos e mais preguiçosos

        * Chamadas de função Python em linha

        * PEP 659: Interpretador adaptativo especializado

      * Diversos

      * FAQ

        * Como devo escrever meu código para utilizar esses
          aceleradores?

        * O CPython 3.11 usará mais memória?

        * Não vejo nenhuma aceleração em minha carga de trabalho. Por
          que?

        * Existe um compilador JIT?

      * Sobre

    * Alterações de bytecode do CPython

      * Novos opcodes

      * Opcodes substituídos

      * Opcodes alterados/removidos

    * Descontinuados

      * Linguagem/Embutidos

      * Módulos

      * Biblioteca Padrão

    * Pendente remoção no Python 3.12

    * Removidos

    * Portando para Python 3.11

    * Mudanças na construção

    * Alterações na API C

      * Novas funcionalidades

      * Portando para Python 3.11

      * Descontinuados

      * Pendente remoção no Python 3.12

      * Removidos

    * Alterações notáveis no 3.11.4

      * tarfile

    * Alterações notáveis no 3.11.5

      * OpenSSL

  * O que há de novo no Python 3.10

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * Gerenciadores de contexto entre parênteses

      * Melhores mensagens de erro

        * SyntaxErrors

        * IndentationErrors

        * AttributeErrors

        * NameErrors

      * PEP 626: Números de linha precisos para depuração e outras
        ferramentas

      * PEP 634: Correspondência de padrão estrutural

        * Sintaxe e operações

        * Abordagem declarativa

        * Padrão simples: corresponder a um literal

          * Comportamento sem o curinga

        * Padrões com uma literal e variável

        * Padrões e classes

          * Padrões com parâmetros posicionais

        * Padrões aninhados

        * Padrões complexos e o curinga

        * Guarda

        * Outros recursos-chave

      * "EncodingWarning" opcional e opção "encoding="locale""

    * Novos recursos relacionados a dicas de tipo

      * PEP 604: novo operador de união de tipo

      * PEP 612: variáveis de especificação de parâmetros

      * PEP 613: TypeAlias

      * PEP 647: guardas de tipo definidas pelo usuário

    * Outras mudanças na linguagem

    * Novos módulos

    * Módulos melhorados

      * asyncio

      * argparse

      * array

      * asynchat, asyncore, smtpd

      * base64

      * bdb

      * bisect

      * codecs

      * collections.abc

      * contextlib

      * curses

      * dataclasses

        * __slots__

        * Campos somente-nomeados

      * distutils

      * doctest

      * encodings

      * enum

      * fileinput

      * faulthandler

      * gc

      * glob

      * hashlib

      * hmac

      * IDLE e idlelib

      * importlib.metadata

      * inspect

      * itertools

      * linecache

      * os

      * os.path

      * pathlib

      * platform

      * pprint

      * py_compile

      * pyclbr

      * shelve

      * statistics

      * site

      * socket

      * ssl

      * sqlite3

      * sys

      * _thread

      * threading

      * traceback

      * types

      * typing

      * unittest

      * urllib.parse

      * xml

      * zipimport

    * Otimizações

    * Descontinuados

    * Removidos

    * Portando para Python 3.10

      * Alterações na sintaxe Python

      * Alterações na API Python

      * Alterações na API C

    * Alterações de bytecode do CPython

    * Mudanças na construção

    * Alterações na API C

      * PEP 652: Mantendo a ABI estável

      * Novas funcionalidades

      * Portando para Python 3.10

      * Descontinuados

      * Removidos

    * Recursos de segurança notáveis no 3.10.7

    * Recursos de segurança notáveis no 3.10.8

    * Alterações notáveis no 3.10.12

      * tarfile

  * O que há de novo no Python 3.9

    * Resumo -- Destaques da versão

    * Você deve verificar DeprecationWarning no seu código

    * Novas funcionalidades

      * Operadores de mesclagem & atualização de dicionário

      * Novos métodos de strings para remover prefixos e sufixos

      * Type hinting genéricos nas coleções padrão

      * Novo analisador sintático

    * Outras mudanças na linguagem

    * Novos módulos

      * zoneinfo

      * graphlib

    * Módulos melhorados

      * ast

      * asyncio

      * compileall

      * concurrent.futures

      * curses

      * datetime

      * distutils

      * fcntl

      * ftplib

      * gc

      * hashlib

      * http

      * IDLE e idlelib

      * imaplib

      * importlib

      * inspect

      * ipaddress

      * math

      * multiprocessing

      * nntplib

      * os

      * pathlib

      * pdb

      * poplib

      * pprint

      * pydoc

      * random

      * signal

      * smtplib

      * socket

      * time

      * sys

      * tracemalloc

      * typing

      * unicodedata

      * venv

      * xml

    * Otimizações

    * Descontinuados

    * Removidos

    * Portando para Python 3.9

      * Alterações na API Python

      * Alterações na API C

      * Alterações de bytecode do CPython

    * Mudanças na construção

    * Alterações na API C

      * Novas funcionalidades

      * Portando para Python 3.9

      * Removidos

    * Alterações notáveis no Python 3.9.1

      * typing

      * Suporte a macOS 11.0 (Big Sur) e Apple Silicon Mac

    * Alterações notáveis no Python 3.9.2

      * collections.abc

      * urllib.parse

    * Alterações notáveis no Python 3.9.3

    * Alterações notáveis no Python 3.9.5

      * urllib.parse

    * Recursos de segurança notáveis no 3.9.14

    * Alterações notáveis no 3.9.17

      * tarfile

  * O que há de novo no Python 3.8

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * Expressões de atribuição

      * Parâmetros somente-posicionais

      * Cache do sistema de arquivos paralelo para arquivos de
        bytecode compilados

      * A compilação de depuração usa a mesma ABI da compilação de
        lançamento

      * As *f-strings* aceitam "=" para expressões auto-documentadas e
        depuração

      * PEP 578: Ganchos de auditoria em tempo de execução Python

      * PEP 587: Configuração de Inicialização do Python

      * PEP 590: Vectorcall: um protocolo de chamada rápida para
        CPython

      * Protocolo de Pickle 5 com buffers de dados fora da banda

    * Outras mudanças na linguagem

    * Novos módulos

    * Módulos melhorados

      * ast

      * asyncio

      * builtins

      * collections

      * cProfile

      * csv

      * curses

      * ctypes

      * datetime

      * functools

      * gc

      * gettext

      * gzip

      * IDLE e idlelib

      * inspect

      * io

      * itertools

      * json.tool

      * logging

      * math

      * mmap

      * multiprocessing

      * os

      * os.path

      * pathlib

      * pickle

      * plistlib

      * pprint

      * py_compile

      * shlex

      * shutil

      * socket

      * ssl

      * statistics

      * sys

      * tarfile

      * threading

      * tokenize

      * tkinter

      * time

      * typing

      * unicodedata

      * unittest

      * venv

      * weakref

      * xml

      * xmlrpc

    * Otimizações

    * Mudanças a construções e API C

    * Descontinuados

    * Remoção de APIs e recursos

    * Portando para o Python 3.8

      * Alterações no comportamento do Python

      * Alterações na API Python

      * Alterações na API C

      * Alterações de bytecode do CPython

      * Ferramentas e daemons

    * Alterações notáveis no Python 3.8.1

    * Alterações notáveis no Python 3.8.2

    * Alterações notáveis no Python 3.8.3

    * Alterações notáveis no Python 3.8.8

    * Alterações notáveis no Python 3.8.9

    * Alterações notáveis no Python 3.8.10

      * Suporte a macOS 11.0 (Big Sur) e Apple Silicon Mac

    * Alterações notáveis no Python 3.8.10

      * urllib.parse

    * Alterações notáveis no Python 3.8.12

      * Alterações na API Python

    * Recursos de segurança notáveis no 3.8.14

    * Alterações notáveis no 3.8.17

      * tarfile

  * O que há de novo no Python 3.7

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * PEP 563: Avaliação Postergada de Anotações

      * PEP 538: Coerção de localidade C legada

      * PEP 540: Modo de tempo de execução  UTF-8 forçado

      * PEP 553: "breakpoint()" embutida

      * PEP 539: Nova API C para armazenamento local de thread

      * PEP 562: Personalização de acesso aos atributos do módulo

      * PEP 564: Novas funções de tempo com resolução de nanossegundos

      * PEP 565: Mostra DeprecationWarning em "__main__"

      * PEP 560: Suporte básico para módulo "typing" e tipos genéricos

      * PEP 552: Arquivos .pyc baseados em hash

      * PEP 545: Traduções da documentação do Python

      * Modo de Desenvolvimento do Python (-X dev)

    * Outras mudanças na linguagem

    * Novos módulos

      * contextvars

      * dataclasses

      * importlib.resources

    * Módulos melhorados

      * argparse

      * asyncio

      * binascii

      * calendar

      * collections

      * compileall

      * concurrent.futures

      * contextlib

      * cProfile

      * crypt

      * datetime

      * dbm

      * decimal

      * dis

      * distutils

      * enum

      * functools

      * gc

      * hmac

      * http.client

      * http.server

      * idlelib e IDLE

      * importlib

      * io

      * ipaddress

      * itertools

      * locale

      * logging

      * math

      * mimetypes

      * msilib

      * multiprocessing

      * os

      * pathlib

      * pdb

      * py_compile

      * pydoc

      * queue

      * re

      * signal

      * socket

      * socketserver

      * sqlite3

      * ssl

      * string

      * subprocess

      * sys

      * time

      * tkinter

      * tracemalloc

      * types

      * unicodedata

      * unittest

      * unittest.mock

      * urllib.parse

      * uu

      * uuid

      * avisos

      * xml

      * xml.etree

      * xmlrpc.server

      * zipapp

      * zipfile

    * Alterações na API C

    * Mudanças na construção

    * Otimizações

    * Outras mudanças na implementação do CPython

    * Comportamento do Python descontinuado

    * Deprecated Python modules, functions and methods

      * aifc

      * asyncio

      * collections

      * dbm

      * enum

      * gettext

      * importlib

      * locale

      * macpath

      * threading

      * socket

      * ssl

      * sunau

      * sys

      * wave

    * Deprecated functions and types of the C API

    * Platform Support Removals

    * Remoção de APIs e recursos

    * Module Removals

    * Windows-only Changes

    * Porting to Python 3.7

      * Changes in Python Behavior

      * Alterações na API Python

      * Alterações na API C

      * Alterações de bytecode do CPython

      * Windows-only Changes

      * Other CPython implementation changes

    * Notable changes in Python 3.7.1

    * Notable changes in Python 3.7.2

    * Notable changes in Python 3.7.6

    * Notable changes in Python 3.7.10

    * Notable changes in Python 3.7.11

    * Notable security feature in 3.7.14

  * What's New In Python 3.6

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * PEP 498: Formatted string literals

      * PEP 526: Syntax for variable annotations

      * PEP 515: Underscores in Numeric Literals

      * PEP 525: Asynchronous Generators

      * PEP 530: Asynchronous Comprehensions

      * PEP 487: Simpler customization of class creation

      * PEP 487: Descriptor Protocol Enhancements

      * PEP 519: Adding a file system path protocol

      * PEP 495: Local Time Disambiguation

      * PEP 529: Change Windows filesystem encoding to UTF-8

      * PEP 528: Change Windows console encoding to UTF-8

      * PEP 520: Preserving Class Attribute Definition Order

      * PEP 468: Preserving Keyword Argument Order

      * New *dict* implementation

      * PEP 523: Adding a frame evaluation API to CPython

      * PYTHONMALLOC environment variable

      * DTrace and SystemTap probing support

    * Outras mudanças na linguagem

    * Novos módulos

      * segredos

    * Módulos melhorados

      * array

      * ast

      * asyncio

      * binascii

      * cmath

      * collections

      * concurrent.futures

      * contextlib

      * datetime

      * decimal

      * distutils

      * email

      * encodings

      * enum

      * faulthandler

      * fileinput

      * hashlib

      * http.client

      * idlelib e IDLE

      * importlib

      * inspect

      * json

      * logging

      * math

      * multiprocessing

      * os

      * pathlib

      * pdb

      * pickle

      * pickletools

      * pydoc

      * random

      * re

      * readline

      * rlcompleter

      * shlex

      * site

      * sqlite3

      * socket

      * socketserver

      * ssl

      * statistics

      * struct

      * subprocess

      * sys

      * telnetlib

      * time

      * timeit

      * tkinter

      * traceback

      * tracemalloc

      * typing

      * unicodedata

      * unittest.mock

      * urllib.request

      * urllib.robotparser

      * venv

      * avisos

      * winreg

      * winsound

      * xmlrpc.client

      * zipfile

      * zlib

    * Otimizações

    * Mudanças a construções e API C

    * Other Improvements

    * Descontinuados

      * New Keywords

      * Deprecated Python behavior

      * Deprecated Python modules, functions and methods

        * asynchat

        * asyncore

        * dbm

        * distutils

        * grp

        * importlib

        * os

        * re

        * ssl

        * tkinter

        * venv

      * xml

      * Deprecated functions and types of the C API

      * Deprecated Build Options

    * Removidos

      * Remoção de APIs e recursos

    * Porting to Python 3.6

      * Changes in 'python' Command Behavior

      * Alterações na API Python

      * Alterações na API C

      * Alterações de bytecode do CPython

    * Notable changes in Python 3.6.2

      * Novo alvo de construção "make regen-all"

      * Remoção do alvo de construção "make touch"

    * Notable changes in Python 3.6.4

    * Notable changes in Python 3.6.5

    * Notable changes in Python 3.6.7

    * Notable changes in Python 3.6.10

    * Notable changes in Python 3.6.13

    * Notable changes in Python 3.6.14

  * O que há de novo no Python 3.5

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * PEP 492 - Coroutines with async and await syntax

      * PEP 465 - A dedicated infix operator for matrix multiplication

      * PEP 448 - Additional Unpacking Generalizations

      * PEP 461 - percent formatting support for bytes and bytearray

      * PEP 484 - Type Hints

      * PEP 471 - os.scandir() function -- a better and faster
        directory iterator

      * PEP 475: Retry system calls failing with EINTR

      * PEP 479: Change StopIteration handling inside generators

      * PEP 485: A function for testing approximate equality

      * PEP 486: Make the Python Launcher aware of virtual
        environments

      * PEP 488: Elimination of PYO files

      * PEP 489: Multi-phase extension module initialization

    * Outras mudanças na linguagem

    * Novos módulos

      * typing

      * zipapp

    * Módulos melhorados

      * argparse

      * asyncio

      * bz2

      * cgi

      * cmath

      * código

      * collections

      * collections.abc

      * compileall

      * concurrent.futures

      * configparser

      * contextlib

      * csv

      * curses

      * dbm

      * difflib

      * distutils

      * doctest

      * email

      * enum

      * faulthandler

      * functools

      * glob

      * gzip

      * heapq

      * http

      * http.client

      * idlelib e IDLE

      * imaplib

      * imghdr

      * importlib

      * inspect

      * io

      * ipaddress

      * json

      * linecache

      * locale

      * logging

      * lzma

      * math

      * multiprocessing

      * operador

      * os

      * pathlib

      * pickle

      * poplib

      * re

      * readline

      * selectors

      * shutil

      * signal

      * smtpd

      * smtplib

      * sndhdr

      * socket

      * ssl

        * Підтримка BIO пам'яті

        * Application-Layer Protocol Negotiation Support

        * Other Changes

      * sqlite3

      * subprocess

      * sys

      * sysconfig

      * tarfile

      * threading

      * time

      * timeit

      * tkinter

      * traceback

      * types

      * unicodedata

      * unittest

      * unittest.mock

      * urllib

      * wsgiref

      * xmlrpc

      * xml.sax

      * zipfile

    * Other module-level changes

    * Otimizações

    * Mudanças a construções e API C

    * Descontinuados

      * New Keywords

      * Comportamento do Python descontinuado

      * Unsupported Operating Systems

      * Deprecated Python modules, functions and methods

    * Removidos

      * Remoção de APIs e recursos

    * Porting to Python 3.5

      * Alterações no comportamento do Python

      * Alterações na API Python

      * Alterações na API C

    * Notable changes in Python 3.5.4

      * Novo alvo de construção "make regen-all"

      * Remoção do alvo de construção "make touch"

  * O que há de novo no Python 3.4

    * Resumo -- Destaques da versão

    * Novas funcionalidades

      * PEP 453: Explicit Bootstrapping of PIP in Python Installations

        * Bootstrapping pip By Default

        * Mudanças na documentação

      * PEP 446: Newly Created File Descriptors Are Non-Inheritable

      * Melhorias no manuseio de Codecs

      * PEP 451: A ModuleSpec Type for the Import System

      * Outras mudanças na linguagem

    * Novos módulos

      * asyncio

      * ensurepip

      * enum

      * pathlib

      * selectors

      * statistics

      * tracemalloc

    * Módulos melhorados

      * abc

      * aifc

      * argparse

      * audioop

      * base64

      * collections

      * colorsys

      * contextlib

      * dbm

      * dis

      * doctest

      * email

      * filecmp

      * functools

      * gc

      * glob

      * hashlib

      * hmac

      * html

      * http

      * idlelib e IDLE

      * importlib

      * inspect

      * ipaddress

      * logging

      * marshal

      * mmap

      * multiprocessing

      * operador

      * os

      * pdb

      * pickle

      * plistlib

      * poplib

      * pprint

      * pty

      * pydoc

      * re

      * resource

      * select

      * shelve

      * shutil

      * smtpd

      * smtplib

      * socket

      * sqlite3

      * ssl

      * stat

      * struct

      * subprocess

      * sunau

      * sys

      * tarfile

      * textwrap

      * threading

      * traceback

      * types

      * urllib

      * unittest

      * venv

      * wave

      * weakref

      * xml.etree

      * zipfile

    * CPython Implementation Changes

      * PEP 445: Customization of CPython Memory Allocators

      * PEP 442: Safe Object Finalization

      * PEP 456: Secure and Interchangeable Hash Algorithm

      * PEP 436: Argument Clinic

      * Other Alterações a compilações e API C

      * Other Improvements

      * Otimizações Relevantes

    * Descontinuados

      * Deprecations in the Python API

      * Deprecated Features

    * Removidos

      * Operating Systems No Longer Supported

      * Remoção de APIs e recursos

      * Code Cleanups

    * Porting to Python 3.4

      * Changes in 'python' Command Behavior

      * Alterações na API Python

      * Alterações na API C

    * Alterado em 3.4.3

      * PEP 476: Habilitando verificação de certificado por padrão
        para clientes http stdlib

  * O que há de novo no Python 3.3

    * Resumo -- Destaques da versão

    * PEP 405: Ambientes Virtuais

    * PEP 420: Implicit Namespace Packages

    * PEP 3118: New memoryview implementation and buffer protocol
      documentation

      * Recursos

      * Mudanças na API

    * PEP 393: Flexible String Representation

      * Funcionalidade

      * Desempenho e utilização de recursos

    * PEP 397: Python Launcher for Windows

    * PEP 3151: Reworking the OS and IO exception hierarchy

    * PEP 380: Syntax for Delegating to a Subgenerator

    * PEP 409: Suppressing exception context

    * PEP 414: Explicit Unicode literals

    * PEP 3155: Qualified name for classes and functions

    * PEP 412: Key-Sharing Dictionary

    * PEP 362: Function Signature Object

    * PEP 421: Adding sys.implementation

      * SimpleNamespace

    * Using importlib as the Implementation of Import

      * New APIs

      * Visible Changes

    * Outras mudanças na linguagem

    * A Finer-Grained Import Lock

    * Builtin functions and types

    * Novos módulos

      * faulthandler

      * ipaddress

      * lzma

    * Módulos melhorados

      * abc

      * array

      * base64

      * binascii

      * bz2

      * codecs

      * collections

      * contextlib

      * crypt

      * curses

      * datetime

      * decimal

        * Recursos

        * Mudanças na API

      * email

        * Policy Framework

        * Provisional Policy with New Header API

        * Other API Changes

      * ftplib

      * functools

      * gc

      * hmac

      * http

      * html

      * imaplib

      * inspect

      * io

      * itertools

      * logging

      * math

      * mmap

      * multiprocessing

      * nntplib

      * os

      * pdb

      * pickle

      * pydoc

      * re

      * sched

      * select

      * shlex

      * shutil

      * signal

      * smtpd

      * smtplib

      * socket

      * socketserver

      * sqlite3

      * ssl

      * stat

      * struct

      * subprocess

      * sys

      * tarfile

      * tempfile

      * textwrap

      * threading

      * time

      * types

      * unittest

      * urllib

      * webbrowser

      * xml.etree.ElementTree

      * zlib

    * Otimizações

    * Mudanças a construções e API C

    * Descontinuados

      * Unsupported Operating Systems

      * Deprecated Python modules, functions and methods

      * Deprecated functions and types of the C API

      * Deprecated features

    * Porting to Python 3.3

      * Porting Python code

      * Porting C code

      * Building C extensions

      * Command Line Switch Changes

  * O que há de novo no Python 3.2

    * PEP 384: Defining a Stable ABI

    * PEP 389: Argparse Command Line Parsing Module

    * PEP 391:  Dictionary Based Configuration for Logging

    * PEP 3148:  The "concurrent.futures" module

    * PEP 3147:  PYC Repository Directories

    * PEP 3149: ABI Version Tagged .so Files

    * PEP 3333: Python Web Server Gateway Interface v1.0.1

    * Outras mudanças na linguagem

    * New, Improved, and Deprecated Modules

      * email

      * elementtree

      * functools

      * itertools

      * collections

      * threading

      * datetime and time

      * math

      * abc

      * io

      * reprlib

      * logging

      * csv

      * contextlib

      * decimal and fractions

      * ftp

      * popen

      * select

      * gzip and zipfile

      * tarfile

      * hashlib

      * ast

      * os

      * shutil

      * sqlite3

      * html

      * socket

      * ssl

      * nntp

      * сертифікати

      * imaplib

      * http.client

      * unittest

      * random

      * poplib

      * asyncore

      * tempfile

      * inspect

      * pydoc

      * dis

      * dbm

      * ctypes

      * site

      * sysconfig

      * pdb

      * configparser

      * urllib.parse

      * mailbox

      * turtledemo

    * Multi-threading

    * Otimizações

    * Unicode

    * Codecs

    * Documentação

    * IDLE

    * Code Repository

    * Mudanças a construções e API C

    * Porting to Python 3.2

  * O que há de novo no Python 3.1

    * PEP 372: Dicionários ordenados

    * PEP 378: Especificador de formato para separador de milhares

    * Outras mudanças na linguagem

    * New, Improved, and Deprecated Modules

    * Otimizações

    * IDLE

    * Mudanças a construções e API C

    * Porting to Python 3.1

  * O que há de novo no Python 3.0

    * Obstáculos comuns

      * print é uma função

      * Visualizações e iteradores em vez de listas

      * Comparações de ordenação

      * Inteiros

      * Texto vs. Dados em vez de Unicode vs. 8 bits

    * Visão geral das alterações da sintaxe

      * Nova sintaxe

      * Sintaxe alterada

      * Sintaxe removida

    * Mudanças já presentes no Python 2.6

    * Mudanças na biblioteca

    * **PEP 3101**: Uma nova abordagem para formatação de strings

    * Mudanças para exceções

    * Outras mudanças diversas

      * Operadores e métodos especiais

      * Funções embutidas

    * Mudanças a construções e API C

    * Desempenho

    * Portando para o Python 3.0

  * O que há de novo no Python 2.7

    * O futuro para o Python 2.x

    * Mudanças no tratamento de avisos de descontinuação

    * Recursos do Python 3.1

    * PEP 372: Adicionando um dicionário ordenado a coleções

    * PEP 378: Especificador de formato para separador de milhares

    * PEP 389: O módulo argparse para analisar linhas de comando

    * PEP 391: Configuração baseada em dicionário para logging

    * PEP 3106: Views de dicionário

    * PEP 3137: O objeto memoryview

    * Outras mudanças na linguagem

      * Alterações no interpretador

      * Otimizações

    * Módulos Novos ou Aprimorados

      * Novo módulo: importlib

      * Novo módulo: sysconfig

      * ttk: Widgets temáticos para Tk

      * Módulo atualizado: unittest

      * Módulo atualizado: ElementTree 1.3

    * Mudanças a construções e API C

      * Capsules

      * Alterações específicas da porta: Windows

      * Alterações específicas da porta: Mac OS X

      * Alterações específicas da porta: FreeBSD

    * Outras alterações e correções

    * Portando para Python 2.7

    * Novos recursos adicionados às versões de manutenção do Python
      2.7

      * Duas novas variáveis de ambiente para modo de depuração

      * PEP 434: Exceção de aprimoramento do IDLE para todos os
        branches

      * PEP 466: Aprimoramentos de segurança de rede do Python 2.7

      * PEP 477: Backport do ensurepip (PEP 453) para o Python 2.7

        * Inicializando pip por padrão

        * Mudanças na documentação

      * PEP 476: Habilitando verificação de certificado por padrão
        para clientes http stdlib

      * PEP 493: Ferramentas de migração de verificação HTTPS para
        Python 2.7

      * Novo alvo de construção "make regen-all"

      * Remoção do alvo de construção "make touch"

    * Reconhecimentos

  * O que há de novo no Python 2.6

    * Python 3.0

    * Changes to the Development Process

      * New Issue Tracker: Roundup

      * New Documentation Format: reStructuredText Using Sphinx

    * PEP 343: The 'with' statement

      * Writing Context Managers

      * The contextlib module

    * PEP 366: Explicit Relative Imports From a Main Module

    * PEP 370: Per-user "site-packages" Directory

    * PEP 371: The "multiprocessing" Package

    * PEP 3101: Advanced String Formatting

    * PEP 3105: "print" As a Function

    * PEP 3110: Exception-Handling Changes

    * PEP 3112: Byte Literals

    * PEP 3116: New I/O Library

    * PEP 3118: Revised Buffer Protocol

    * PEP 3119: Abstract Base Classes

    * PEP 3127: Integer Literal Support and Syntax

    * PEP 3129: Class Decorators

    * PEP 3141: A Type Hierarchy for Numbers

      * The "fractions" Module

    * Outras mudanças na linguagem

      * Otimizações

      * Alterações no interpretador

    * Módulos novos ou aprimorados

      * The "ast" module

      * The "future_builtins" module

      * The "json" module: JavaScript Object Notation

      * The "plistlib" module: A Property-List Parser

      * ctypes Enhancements

      * Improved SSL Support

    * Deprecations and Removals

    * Mudanças a construções e API C

      * Port-Specific Changes: Windows

      * Port-Specific Changes: Mac OS X

      * Port-Specific Changes: IRIX

    * Porting to Python 2.6

    * Reconhecimentos

  * What's New in Python 2.5

    * PEP 308: Conditional Expressions

    * PEP 309: Partial Function Application

    * PEP 314: Metadata for Python Software Packages v1.1

    * PEP 328: Absolute and Relative Imports

    * PEP 338: Executing Modules as Scripts

    * PEP 341: Unified try/except/finally

    * PEP 342: New Generator Features

    * PEP 343: The 'with' statement

      * Writing Context Managers

      * The contextlib module

    * PEP 352: Exceptions as New-Style Classes

    * PEP 353: Using ssize_t as the index type

    * PEP 357: The '__index__' method

    * Outras mudanças na linguagem

      * Interactive Interpreter Changes

      * Otimizações

    * New, Improved, and Removed Modules

      * The ctypes package

      * The ElementTree package

      * The hashlib package

      * The sqlite3 package

      * The wsgiref package

    * Mudanças a construções e API C

      * Port-Specific Changes

    * Porting to Python 2.5

    * Reconhecimentos

  * What's New in Python 2.4

    * PEP 218: Built-In Set Objects

    * PEP 237: Unifying Long Integers and Integers

    * PEP 289: Generator Expressions

    * PEP 292: Simpler String Substitutions

    * PEP 318: Decorators for Functions and Methods

    * PEP 322: Reverse Iteration

    * PEP 324: New subprocess Module

    * PEP 327: Decimal Data Type

      * Why is Decimal needed?

      * The "Decimal" type

      * The "Context" type

    * PEP 328: Multi-line Imports

    * PEP 331: Locale-Independent Float/String Conversions

    * Outras mudanças na linguagem

      * Otimizações

    * New, Improved, and Deprecated Modules

      * cookielib

      * doctest

    * Mudanças a construções e API C

      * Port-Specific Changes

    * Porting to Python 2.4

    * Reconhecimentos

  * What's New in Python 2.3

    * PEP 218: A Standard Set Datatype

    * PEP 255: Simple Generators

    * PEP 263: Source Code Encodings

    * PEP 273: Importing Modules from ZIP Archives

    * PEP 277: Unicode file name support for Windows NT

    * PEP 278: Universal Newline Support

    * PEP 279: enumerate()

    * PEP 282: The logging Package

    * PEP 285: A Boolean Type

    * PEP 293: Codec Error Handling Callbacks

    * PEP 301: Package Index and Metadata for Distutils

    * PEP 302: New Import Hooks

    * PEP 305: Comma-separated Files

    * PEP 307: Pickle Enhancements

    * Extended Slices

    * Outras mudanças na linguagem

      * String Changes

      * Otimizações

    * New, Improved, and Deprecated Modules

      * Date/Time Type

      * The optparse Module

    * Pymalloc: A Specialized Object Allocator

    * Mudanças a construções e API C

      * Port-Specific Changes

    * Outras alterações e correções

    * Porting to Python 2.3

    * Reconhecimentos

  * What's New in Python 2.2

    * Introdução

    * PEPs 252 and 253: Type and Class Changes

      * Old and New Classes

      * Descriptors

      * Multiple Inheritance: The Diamond Rule

      * Attribute Access

      * Related Links

    * PEP 234: Iterators

    * PEP 255: Simple Generators

    * PEP 237: Unifying Long Integers and Integers

    * PEP 238: Changing the Division Operator

    * Unicode Changes

    * PEP 227: Nested Scopes

    * Módulos novos ou aprimorados

    * Interpreter Changes and Fixes

    * Outras alterações e correções

    * Reconhecimentos

  * What's New in Python 2.1

    * Introdução

    * PEP 227: Nested Scopes

    * PEP 236: __future__ Directives

    * PEP 207: Rich Comparisons

    * PEP 230: Warning Framework

    * PEP 229: New Build System

    * PEP 205: Weak References

    * PEP 232: Function Attributes

    * PEP 235: Importing Modules on Case-Insensitive Platforms

    * PEP 217: Interactive Display Hook

    * PEP 208: New Coercion Model

    * PEP 241: Metadata in Python Packages

    * Módulos novos ou aprimorados

    * Outras alterações e correções

    * Reconhecimentos

  * What's New in Python 2.0

    * Introdução

    * What About Python 1.6?

    * New Development Process

    * Unicode

    * Compreensões de lista

    * Augmented Assignment

    * String Methods

    * Garbage Collection of Cycles

    * Other Core Changes

      * Minor Language Changes

      * Changes to Built-in Functions

    * Porting to 2.0

    * Extending/Embedding Changes

    * Distutils: Making Modules Easy to Install

    * XML Modules

      * SAX2 Support

      * DOM Support

      * Relationship to PyXML

    * Module changes

    * Novos módulos

    * IDLE Improvements

    * Deleted and Deprecated Modules

    * Reconhecimentos

  * Changelog

    * Python seguinte

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Testes

      * Construção

    * Python 3.15.2 final

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Construção

      * API C

    * Python 3.15.1 final

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.15.0 final

    * Python 3.15.0 candidato a lançamento 3

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.15.0 candidato a lançamento 2

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Construção

      * Windows

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.15.0 candidato a lançamento 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * Ferramentas/Demos

      * API C

    * Python 3.15.0 beta 4

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.15.0 beta 3

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.15.0 beta 2

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Testes

      * Construção

      * Windows

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.15.0 beta 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.15.0 alpha 8

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.15.0 alpha 7

      * Windows

      * Testes

      * Segurança

      * Biblioteca

      * Documentação

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.15.0 alpha 6

      * macOS

      * Windows

      * Testes

      * Segurança

      * Biblioteca

      * IDLE

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.15.0 alpha 5

      * Windows

      * Ferramentas/Demos

      * Testes

      * Biblioteca

      * Documentação

      * Núcleo e embutidos

      * API C

    * Python 3.15.0 alpha 4

      * Testes

      * Biblioteca

      * Núcleo e embutidos

    * Python 3.15.0 alpha 3

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * Documentação

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.15.0 alpha 2

      * Windows

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.15.0 alpha 1

      * macOS

      * Windows

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * IDLE

      * Documentação

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.14.0 beta 1

      * Windows

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * IDLE

      * Documentação

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * API C

      * Construção

    * Python 3.14.0 alpha 7

      * macOS

      * Windows

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * Documentação

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.14.0 alpha 6

      * macOS

      * Windows

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * Documentação

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.14.0 alpha 5

      * macOS

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * IDLE

      * Documentação

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * API C

      * Construção

    * Python 3.14.0 alpha 4

      * macOS

      * Ferramentas/Demos

      * Testes

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.14.0 alpha 3

      * Windows

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * Documentação

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.14.0 alpha 2

      * Windows

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * Documentação

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * API C

      * Construção

    * Python 3.14.0 alpha 1

      * macOS

      * Windows

      * Ferramentas/Demos

      * Testes

      * Segurança

      * Biblioteca

      * IDLE

      * Documentação

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * API C

      * Construção

    * Python 3.13.0 beta 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.13.0 alpha 6

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * API C

    * Python 3.13.0 alpha 5

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.13.0 alpha 4

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.13.0 alpha 3

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.13.0 alpha 2

      * Núcleo e embutidos

      * Biblioteca

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.13.0 alpha 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.12.0 beta 1

      * Segurança

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.12.0 alpha 7

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Construção

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * Ferramentas/Demos

      * API C

    * Python 3.12.0 alpha 6

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * API C

    * Python 3.12.0 alpha 5

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

    * Python 3.12.0 alpha 4

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.12.0 alpha 3

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.12.0 alpha 2

      * Segurança

      * Núcleo e embutidos

      * Construção

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * API C

    * Python 3.12.0 alpha 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.11.0 beta 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Construção

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.11.0 alpha 7

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.11.0 alpha 6

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * IDLE

      * API C

    * Python 3.11.0 alpha 5

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Construção

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.11.0 alpha 4

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * API C

    * Python 3.11.0 alpha 3

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * API C

    * Python 3.11.0 alpha 2

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.11.0 alpha 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.10.0 beta 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.10.0 alpha 7

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * IDLE

      * API C

    * Python 3.10.0 alpha 6

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.10.0 alpha 5

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.10.0 alpha 4

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.10.0 alpha 3

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.10.0 alpha 2

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.10.0 alpha 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.9.0 beta 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * Ferramentas/Demos

      * API C

    * Python 3.9.0 alpha 6

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.9.0 alpha 5

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.9.0 alpha 4

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * IDLE

      * API C

    * Python 3.9.0 alpha 3

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Construção

      * IDLE

      * API C

    * Python 3.9.0 alpha 2

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * API C

    * Python 3.9.0 alpha 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.8.0 beta 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.8.0 alpha 4

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.8.0 alpha 3

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.8.0 alpha 2

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Windows

      * IDLE

    * Python 3.8.0 alpha 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.7.0 final

      * Biblioteca

      * API C

    * Python 3.7.0 release candidate 1

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Construção

      * Windows

      * IDLE

    * Python 3.7.0 beta 5

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * macOS

      * IDLE

    * Python 3.7.0 beta 4

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

    * Python 3.7.0 beta 3

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.7.0 beta 2

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

    * Python 3.7.0 beta 1

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * API C

    * Python 3.7.0 alpha 4

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Windows

      * Ferramentas/Demos

      * API C

    * Python 3.7.0 alpha 3

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.7.0 alpha 2

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Construção

      * IDLE

      * API C

    * Python 3.7.0 alpha 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.6.6 final

    * Python 3.6.6 release candidate 1

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.6.5 final

      * Testes

      * Construção

    * Python 3.6.5 release candidate 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.6.4 final

    * Python 3.6.4 release candidate 1

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * macOS

      * IDLE

      * Ferramentas/Demos

      * API C

    * Python 3.6.3 final

      * Biblioteca

      * Construção

    * Python 3.6.3 release candidate 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * IDLE

      * Ferramentas/Demos

    * Python 3.6.2 final

    * Python 3.6.2 release candidate 2

      * Segurança

    * Python 3.6.2 release candidate 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * API C

      * Construção

      * Documentação

      * Ferramentas/Demos

      * Testes

      * Windows

    * Python 3.6.1 final

      * Núcleo e embutidos

      * Construção

    * Python 3.6.1 release candidate 1

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Windows

      * API C

      * Documentação

      * Testes

      * Construção

    * Python 3.6.0 final

    * Python 3.6.0 release candidate 2

      * Núcleo e embutidos

      * Ferramentas/Demos

      * Windows

      * Construção

    * Python 3.6.0 release candidate 1

      * Núcleo e embutidos

      * Biblioteca

      * API C

      * Documentação

      * Ferramentas/Demos

    * Python 3.6.0 beta 4

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

    * Python 3.6.0 beta 3

      * Núcleo e embutidos

      * Biblioteca

      * Windows

      * Construção

      * Testes

    * Python 3.6.0 beta 2

      * Núcleo e embutidos

      * Biblioteca

      * Windows

      * API C

      * Construção

      * Testes

    * Python 3.6.0 beta 1

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * API C

      * Testes

      * Construção

      * Ferramentas/Demos

      * Windows

    * Python 3.6.0 alpha 4

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Testes

      * Windows

      * Construção

    * Python 3.6.0 alpha 3

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * API C

      * Construção

      * Ferramentas/Demos

      * Documentação

      * Testes

    * Python 3.6.0 alpha 2

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Documentação

      * Testes

      * Windows

      * Construção

      * API C

      * Ferramentas/Demos

    * Python 3.6.0 alpha 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Documentação

      * Testes

      * Construção

      * Windows

      * Ferramentas/Demos

      * API C

    * Python 3.5.5 final

    * Python 3.5.5 release candidate 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

    * Python 3.5.4 final

      * Biblioteca

    * Python 3.5.4 release candidate 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * Documentação

      * Testes

      * Construção

      * Windows

      * API C

    * Python 3.5.3 final

    * Python 3.5.3 release candidate 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * API C

      * Documentação

      * Testes

      * Ferramentas/Demos

      * Windows

      * Construção

    * Python 3.5.2 final

      * Núcleo e embutidos

      * Testes

      * IDLE

    * Python 3.5.2 release candidate 1

      * Segurança

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Documentação

      * Testes

      * Construção

      * Windows

      * Ferramentas/Demos

    * Python 3.5.1 final

      * Núcleo e embutidos

      * Windows

    * Python 3.5.1 release candidate 1

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Documentação

      * Testes

      * Construção

      * Windows

      * Ferramentas/Demos

    * Python 3.5.0 final

      * Construção

    * Python 3.5.0 release candidate 4

      * Biblioteca

      * Construção

    * Python 3.5.0 release candidate 3

      * Núcleo e embutidos

      * Biblioteca

    * Python 3.5.0 release candidate 2

      * Núcleo e embutidos

      * Biblioteca

    * Python 3.5.0 release candidate 1

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Documentação

      * Testes

    * Python 3.5.0 beta 4

      * Núcleo e embutidos

      * Biblioteca

      * Construção

    * Python 3.5.0 beta 3

      * Núcleo e embutidos

      * Biblioteca

      * Testes

      * Documentação

      * Construção

    * Python 3.5.0 beta 2

      * Núcleo e embutidos

      * Biblioteca

    * Python 3.5.0 beta 1

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Testes

      * Documentação

      * Ferramentas/Demos

    * Python 3.5.0 alpha 4

      * Núcleo e embutidos

      * Biblioteca

      * Construção

      * Testes

      * Ferramentas/Demos

      * API C

    * Python 3.5.0 alpha 3

      * Núcleo e embutidos

      * Biblioteca

      * Construção

      * Testes

      * Ferramentas/Demos

    * Python 3.5.0 alpha 2

      * Núcleo e embutidos

      * Biblioteca

      * Construção

      * API C

      * Windows

    * Python 3.5.0 alpha 1

      * Núcleo e embutidos

      * Biblioteca

      * IDLE

      * Construção

      * API C

      * Documentação

      * Testes

      * Ferramentas/Demos

      * Windows

* O tutorial do Python

  * 1. Abrindo seu apetite

  * 2. Utilizando o interpretador Python

    * 2.1. Chamando o interpretador

      * 2.1.1. Passagem de argumentos

      * 2.1.2. Modo interativo

    * 2.2. O interpretador e seu ambiente

      * 2.2.1. Edição de código-fonte

  * 3. Uma introdução informal ao Python

    * 3.1. Usando Python como uma calculadora

      * 3.1.1. Números

      * 3.1.2. Texto

      * 3.1.3. Listas

    * 3.2. Primeiros passos para a programação

  * 4. Mais ferramentas de controle de fluxo

    * 4.1. Instruções "if"

    * 4.2. Instruções "for"

    * 4.3. A função "range()"

    * 4.4. Instruções "break" e "continue"

    * 4.5. Cláusulas "else" em laços

    * 4.6. Instruções "pass"

    * 4.7. Instruções "match"

    * 4.8. Definindo funções

    * 4.9. Mais sobre definição de funções

      * 4.9.1. Argumentos com valor padrão

      * 4.9.2. Argumentos nomeados

      * 4.9.3. Parâmetros especiais

        * 4.9.3.1. Argumentos posicional-ou-nomeados

        * 4.9.3.2. Parâmetros somente-posicionais

        * 4.9.3.3. Argumentos somente-nomeados

        * 4.9.3.4. Exemplos de funções

        * 4.9.3.5. Recapitulando

      * 4.9.4. Listas de argumentos arbitrárias

      * 4.9.5. Desempacotando listas de argumentos

      * 4.9.6. Expressões lambda

      * 4.9.7. Strings de documentação

      * 4.9.8. Anotações de função

    * 4.10. Intermezzo: estilo de codificação

  * 5. Estruturas de dados

    * 5.1. Mais sobre listas

      * 5.1.1. Usando listas como pilhas

      * 5.1.2. Usando listas como filas

      * 5.1.3. Compreensões de lista

      * 5.1.4. Compreensões de lista aninhadas

      * 5.1.5. Desempacotamento em Listas e Compreensões de Lista

    * 5.2. A instrução "del"

    * 5.3. Tuplas e Sequências

    * 5.4. Conjuntos

    * 5.5. Dicionários

    * 5.6. Técnicas de iteração

    * 5.7. Mais sobre condições

    * 5.8. Comparando sequências e outros tipos

  * 6. Módulos

    * 6.1. Mais sobre módulos

      * 6.1.1. Executando módulos como scripts

      * 6.1.2. O caminho de busca dos módulos

      * 6.1.3. Arquivos Python "compilados"

    * 6.2. Módulos padrões

    * 6.3. A função "dir()"

    * 6.4. Pacotes

      * 6.4.1. Importando * de um pacote

      * 6.4.2. Referências em um mesmo pacote

  * 7. Entrada e saída

    * 7.1. Formatação de saída mais elaborada

      * 7.1.1. Literais de string formatados

      * 7.1.2. O método format() de strings

      * 7.1.3. Formatação manual de strings

      * 7.1.4. Formatação de strings à moda antiga

    * 7.2. Lendo e escrevendo arquivos

      * 7.2.1. Métodos de objetos arquivo

      * 7.2.2. Gravando dados estruturados com "json"

  * 8. Erros e exceções

    * 8.1. Erros de sintaxe

    * 8.2. Exceções

    * 8.3. Tratamento de exceções

    * 8.4. Levantando exceções

    * 8.5. Encadeamento de exceções

    * 8.6. Exceções definidas pelo usuário

    * 8.7. Definindo ações de limpeza

    * 8.8. Ações de limpeza predefinidas

    * 8.9. Criando e tratando várias exceções não relacionadas

    * 8.10. Enriquecendo exceções com notas

  * 9. Classes

    * 9.1. Uma palavra sobre nomes e objetos

    * 9.2. Escopos e espaços de nomes do Python

      * 9.2.1. Exemplo de escopos e espaço de nomes

    * 9.3. Uma primeira olhada nas classes

      * 9.3.1. Sintaxe da definição de classe

      * 9.3.2. Objetos classe

      * 9.3.3. Objetos instância

      * 9.3.4. Objetos método

      * 9.3.5. Variáveis de classe e instância

    * 9.4. Observações aleatórias

    * 9.5. Herança

      * 9.5.1. Herança múltipla

    * 9.6. Variáveis privadas

    * 9.7. Curiosidades e conclusões

    * 9.8. Iteradores

    * 9.9. Geradores

    * 9.10. Expressões geradoras

  * 10. Um breve passeio pela biblioteca padrão

    * 10.1. Interface com o sistema operacional

    * 10.2. Caracteres curinga

    * 10.3. Argumentos de linha de comando

    * 10.4. Redirecionamento de erros e encerramento do programa

    * 10.5. Reconhecimento de padrões em strings

    * 10.6. Matemática

    * 10.7. Acesso à internet

    * 10.8. Data e hora

    * 10.9. Compressão de dados

    * 10.10. Medição de desempenho

    * 10.11. Controle de qualidade

    * 10.12. Baterias incluídas

  * 11. Um breve passeio pela biblioteca padrão --- parte II

    * 11.1. Formatando a saída

    * 11.2. Usando templates

    * 11.3. Trabalhando com formatos binários de dados

    * 11.4. Multi-threading

    * 11.5. Gerando logs

    * 11.6. Referências fracas

    * 11.7. Ferramentas para trabalhar com listas

    * 11.8. Aritmética decimal com ponto flutuante

  * 12. Ambientes virtuais e pacotes

    * 12.1. Introdução

    * 12.2. Criando ambientes virtuais

    * 12.3. Gerenciando pacotes com o pip

  * 13. E agora?

  * 14. Edição de entrada interativa e substituição de histórico

    * 14.1. Tab completion e histórico de edição

    * 14.2. Alternativas ao interpretador interativo

  * 15. Aritmética de ponto flutuante: problemas e limitações

    * 15.1. Erro de representação

  * 16. Anexo

    * 16.1. Modo interativo

      * 16.1.1. Tratamento de erros

      * 16.1.2. Scripts Python executáveis

      * 16.1.3. Arquivo de inicialização do modo interativo

      * 16.1.4. Módulos de customização

* Configurações e Uso do Python

  * 1. Linha de comando e ambiente

    * 1.1. Linha de comando

      * 1.1.1. Opções de interface

      * 1.1.2. Opções genéricas

      * 1.1.3. Opções diversas

      * 1.1.4. Controlando cores

    * 1.2. Variáveis de ambiente

      * 1.2.1. Variáveis de modo de depuração

  * 2. Utilizando Python em plataformas Unix

    * 2.1. Obtendo e instalando a versão mais recente do Python

      * 2.1.1. No Linux

        * 2.1.1.1. Instalação do IDLE

      * 2.1.2. No FreeBSD e OpenBSD

    * 2.2. Compilando o Python

    * 2.3. Paths e arquivos relacionados com o Python

    * 2.4. Diversos

    * 2.5. OpenSSL personalizado

  * 3. Configurando o Python

    * 3.1. Requisitos de construção

      * 3.1.1. Requisitos para módulos opcionais

    * 3.2. Arquivos gerados

      * 3.2.1. Script configure

    * 3.3. Opções de configuração

      * 3.3.1. Opções gerais

      * 3.3.2. Opções do compilador C

      * 3.3.3. Opções da ligação

      * 3.3.4. Opções para dependências de terceiros

      * 3.3.5. Opções de WebAssembly

      * 3.3.6. Opções de instalação

      * 3.3.7. Opções de desempenho

      * 3.3.8. Compilação de depuração do Python

      * 3.3.9. Opções de depuração

      * 3.3.10. Opções da ligação

      * 3.3.11. Opções da biblioteca

      * 3.3.12. Opções de segurança

      * 3.3.13. Opções do macOS

      * 3.3.14. Opções do iOS

      * 3.3.15. Opções de compilação cruzada

    * 3.4. Sistema de Construção Python

      * 3.4.1. Arquivos principais do sistema de construção

      * 3.4.2. Principais etapas de construção

      * 3.4.3. Alvos principais do Makefile

        * 3.4.3.1. make

        * 3.4.3.2. make platform

        * 3.4.3.3. make profile-opt

        * 3.4.3.4. make clean

        * 3.4.3.5. make distclean

        * 3.4.3.6. make install

        * 3.4.3.7. make test

        * 3.4.3.8. make ci

        * 3.4.3.9. make buildbottest

        * 3.4.3.10. make regen-all

      * 3.4.4. Extensões C

    * 3.5. Sinalizadores do compilador e do vinculador

      * 3.5.1. Sinalizadores do pré-processador

      * 3.5.2. Sinalizadores do compilador

      * 3.5.3. Sinalizadores do vinculador

  * 4. Utilizando Python no Windows

    * 4.1. Gerenciador de instalação do Python

      * 4.1.1. Instalação

      * 4.1.2. Uso básico

      * 4.1.3. Comando help

      * 4.1.4. Listando ambientes de execução

      * 4.1.5. Instalando ambientes de execução

      * 4.1.6. Instalações offline

      * 4.1.7. Desinstalando ambientes de execução

      * 4.1.8. Configuração

      * 4.1.9. Linhas shebang

      * 4.1.10. Instalação avançada

      * 4.1.11. Configuração administrativa

      * 4.1.12. Instalando binários com threads livres

      * 4.1.13. Index signatures

      * 4.1.14. Proxy settings

      * 4.1.15. Solução de problemas

    * 4.2. O pacote embutível

      * 4.2.1. Aplicação Python

      * 4.2.2. Incorporando Python

    * 4.3. Os pacotes nuget.org

      * 4.3.1. Pacotes com threads livres

    * 4.4. Pacotes Alternativos

    * 4.5. Versões do Windows suportadas

    * 4.6. Removendo a limitação de MAX_PATH

    * 4.7. Modo UTF-8

    * 4.8. Encontrando módulos

    * 4.9. Módulos adicionais

      * 4.9.1. PyWin32

      * 4.9.2. cx_Freeze

    * 4.10. Compilando Python no Windows

    * 4.11. O instalador completo (descontinuado)

      * 4.11.1. Etapas de instalação

      * 4.11.2. Removendo a limitação de MAX_PATH

      * 4.11.3. Instalando sem UI

      * 4.11.4. Instalando sem download

      * 4.11.5. Modificando uma instalação

      * 4.11.6. Instalando binários com threads livres

    * 4.12. Inicializador Python para Windows (descontinuado)

      * 4.12.1. Começando

        * 4.12.1.1. Pela linha de comando

        * 4.12.1.2. Ambientes virtuais

        * 4.12.1.3. Por um script

        * 4.12.1.4. Por associação de arquivos

      * 4.12.2. Linhas shebang

      * 4.12.3. Argumentos em linhas shebang

      * 4.12.4. Personalização

        * 4.12.4.1. Personalização via arquivos INI

        * 4.12.4.2. Personalizando versões padrão do Python

      * 4.12.5. Diagnósticos

      * 4.12.6. Teste de simulação

      * 4.12.7. Instalar sob demanda

      * 4.12.8. Códigos de retorno

  * 5. Usando Python em macOS

    * 5.1. Usando Python para macOS do "python.org"

      * 5.1.1. Etapas de instalação

      * 5.1.2. Como executar um script Python

    * 5.2. Distribuições alternativas

    * 5.3. Instalar pacotes Python adicionais

    * 5.4. Programação de GUI

    * 5.5. Tópicos avançados

      * 5.5.1. Instalando binários com threads livres

      * 5.5.2. Instalação usando a linha de comando

      * 5.5.3. Distribuindo aplicações Python

      * 5.5.4. Conformidade com a App Store

    * 5.6. Outros recursos

  * 6. Utilizando Python no Android

    * 6.1. Adicionando Python a uma aplicação Android

    * 6.2. Construindo um pacote Python para Android

  * 7. Usando Python no iOS

    * 7.1. Python em tempo de execução no iOS

      * 7.1.1. Compatibilidade com a versão do iOS

      * 7.1.2. Identificação da plataforma

      * 7.1.3. Disponibilidade da biblioteca padrão

      * 7.1.4. Módulos de extensão binária

      * 7.1.5. Binários stub do compilador

    * 7.2. Instalando Python no iOS

      * 7.2.1. Ferramentas para construir aplicações de iOS

      * 7.2.2. Adicionando Python a um projeto iOS

      * 7.2.3. Testando um pacote Python

    * 7.3. Conformidade com a App Store

      * 7.3.1. Código incompatível na biblioteca padrão

      * 7.3.2. Manifestos de privacidade

  * 8. Editores e IDEs

    * 8.1. IDLE --- editor e console Python

    * 8.2. Outros editores e IDEs

* A Referência da Linguagem Python

  * 1. Introdução

    * 1.1. Implementações Alternativas

    * 1.2. Notação

      * 1.2.1. Definições lexicais e sintáticas

  * 2. Análise léxica

    * 2.1. Estrutura das linhas

      * 2.1.1. Linhas lógicas

      * 2.1.2. Linhas físicas

      * 2.1.3. Comentários

      * 2.1.4. Declarações de codificação

      * 2.1.5. Junção de linha explícita

      * 2.1.6. Junção de linha implícita

      * 2.1.7. Linhas em branco

      * 2.1.8. Indentação

      * 2.1.9. Espaços em branco entre tokens

      * 2.1.10. Marcador de fim

    * 2.2. Outros tokens

    * 2.3. Nomes (identificadores e palavras reservadas)

      * 2.3.1. Palavras reservadas

      * 2.3.2. Palavras reservadas contextuais

      * 2.3.3. Classes reservadas de identificadores

      * 2.3.4. Caracteres não ASCII em nomes

    * 2.4. Literais

    * 2.5. Literais de string e bytes

      * 2.5.1. Strings entre aspas triplas

      * 2.5.2. Prefixos de string

      * 2.5.3. Gramática formal

      * 2.5.4. Sequências de escape

        * 2.5.4.1. Fim de linha ignorado

        * 2.5.4.2. Caracteres escapados

        * 2.5.4.3. Caractere octal

        * 2.5.4.4. Caractere hexadecimal

        * 2.5.4.5. Caractere nomeado Unicode

        * 2.5.4.6. Caracteres hexadecimais Unicode

        * 2.5.4.7. Sequências de espace não reconhecidas

      * 2.5.5. Literais de bytes

      * 2.5.6. Literais de string brutas

      * 2.5.7. Literais de strings formatadas

      * 2.5.8. Literais de string template (t-strings)

      * 2.5.9. Gramática formal para f-strings

    * 2.6. Literais numéricos

      * 2.6.1. Inteiros literais

      * 2.6.2. Literais de ponto flutuante

      * 2.6.3. Literais imaginários

    * 2.7. Operadores e delimitadores

  * 3. Modelo de dados

    * 3.1. Objetos, valores e tipos

    * 3.2. A hierarquia de tipos padrão

      * 3.2.1. None

      * 3.2.2. NotImplemented

      * 3.2.3. Ellipsis

      * 3.2.4. "numbers.Number"

        * 3.2.4.1. "numbers.Integral"

        * 3.2.4.2. "numbers.Real" ("float")

        * 3.2.4.3. "numbers.Complex" ("complex")

      * 3.2.5. Sequências

        * 3.2.5.1. Sequências imutáveis

        * 3.2.5.2. Sequências mutáveis

      * 3.2.6. Tipos de conjuntos

      * 3.2.7. Mapeamentos

        * 3.2.7.1. Dicionários

        * 3.2.7.2. Dicionários congelados

      * 3.2.8. Tipos chamáveis

        * 3.2.8.1. Funções definidas pelo usuário

          * 3.2.8.1.1. Atributos especiais de somente leitura

          * 3.2.8.1.2. Atributos especiais graváveis

        * 3.2.8.2. Métodos de instância

        * 3.2.8.3. Funções geradoras

        * 3.2.8.4. Funções de corrotina

        * 3.2.8.5. Funções geradoras assíncronas

        * 3.2.8.6. Funções embutidas

        * 3.2.8.7. Métodos embutidos

        * 3.2.8.8. Classes

        * 3.2.8.9. Instâncias de classe

      * 3.2.9. Módulos

        * 3.2.9.1. Atributos relacionados à importação em objetos de
          módulo

        * 3.2.9.2. Outros atributos graváveis em objetos de módulo

        * 3.2.9.3. Dicionários do módulo

      * 3.2.10. Classes personalizadas

        * 3.2.10.1. Atributos especiais

        * 3.2.10.2. Métodos especiais

      * 3.2.11. Instâncias de classe

        * 3.2.11.1. Atributos especiais

      * 3.2.12. Objetos de E/S (também conhecidos como objetos
        arquivo)

      * 3.2.13. Tipos internos

        * 3.2.13.1. Objetos código

          * 3.2.13.1.1. Atributos especiais de somente leitura

          * 3.2.13.1.2. Métodos de objetos código

        * 3.2.13.2. Objetos quadro

          * 3.2.13.2.1. Atributos especiais de somente leitura

          * 3.2.13.2.2. Atributos especiais graváveis

          * 3.2.13.2.3. Métodos de objetos quadro

        * 3.2.13.3. Objetos traceback

        * 3.2.13.4. Objetos slice

        * 3.2.13.5. Objetos método estático

        * 3.2.13.6. Objetos método de classe

    * 3.3. Nomes de métodos especiais

      * 3.3.1. Personalização básica

      * 3.3.2. Personalizando o acesso aos atributos

        * 3.3.2.1. Personalizando acesso a atributos de módulos

        * 3.3.2.2. Implementando descritores

        * 3.3.2.3. Invocando descritores

        * 3.3.2.4. __slots__

      * 3.3.3. Personalizando a criação de classe

        * 3.3.3.1. Metaclasses

        * 3.3.3.2. Resolvendo entradas de MRO

        * 3.3.3.3. Determinando a metaclasse apropriada

        * 3.3.3.4. Preparando o espaço de nomes da classe

        * 3.3.3.5. Executando o corpo da classe

        * 3.3.3.6. Criando o objeto classe

        * 3.3.3.7. Usos para metaclasses

      * 3.3.4. Personalizando verificações de instância e subclasse

      * 3.3.5. Emulando tipos genéricos

        * 3.3.5.1. O propósito de *__class_getitem__*

        * 3.3.5.2. *__class_getitem__* versus *__getitem__*

      * 3.3.6. Emulando objetos chamáveis

      * 3.3.7. Emulando tipos contêineres

      * 3.3.8. Emulando tipos numéricos

      * 3.3.9. Gerenciadores de contexto da instrução with

      * 3.3.10. Customizando argumentos posicionais na classe
        correspondência de padrão

      * 3.3.11. Emulando tipos buffer

      * 3.3.12. Anotações

      * 3.3.13. Pesquisa de método especial

    * 3.4. Corrotinas

      * 3.4.1. Objetos aguardáveis

      * 3.4.2. Objetos corrotina

      * 3.4.3. Iteradores assíncronos

      * 3.4.4. Gerenciadores de contexto assíncronos

  * 4. Modelo de execução

    * 4.1. Estrutura de um programa

    * 4.2. Nomeação e ligação

      * 4.2.1. Ligação de nomes

      * 4.2.2. Resolução de nomes

      * 4.2.3. Escopos de anotação

      * 4.2.4. Avaliação preguiçosa

      * 4.2.5. Builtins e execução restrita

      * 4.2.6. Interação com recursos dinâmicos

    * 4.3. Exceções

    * 4.4. Componentes do Ambiente de Execução

      * 4.4.1. Modelo Geral de Computação

      * 4.4.2. Modelo do Ambiente de Execução Python

  * 5. O sistema de importação

    * 5.1. "importlib"

    * 5.2. Pacotes

      * 5.2.1. Pacotes regulares

      * 5.2.2. Pacotes de espaço de nomes

    * 5.3. Caminho de busca

      * 5.3.1. O cache de módulos

      * 5.3.2. Localizadores e carregadores

      * 5.3.3. Ganchos de importação

      * 5.3.4. O metacaminho

    * 5.4. Carregando

      * 5.4.1. Carregadores

      * 5.4.2. Submódulos

      * 5.4.3. Especificações de módulo

      * 5.4.4. Atributo __path__ dos módulos

      * 5.4.5. Representações do módulo

      * 5.4.6. Invalidação de bytecode em cache

    * 5.5. O localizador baseado no caminho

      * 5.5.1. Localizadores de entrada de caminho

      * 5.5.2. Protocolo do localizador de entrada de caminho

    * 5.6. Substituindo o sistema de importação padrão

    * 5.7. Importações relativas ao pacote

    * 5.8. Considerações especiais para __main__

      * 5.8.1. __main__.__spec__

    * 5.9. Referências

  * 6. Expressões

    * 6.1. Conversões aritméticas

    * 6.2. Átomos

      * 6.2.1. Constantes embutidas

      * 6.2.2. Identificadores (Nomes)

        * 6.2.2.1. Desfiguração de nome privado

      * 6.2.3. Literais

        * 6.2.3.1. Identidade de objeto e literais

        * 6.2.3.2. Concatenação de literal de string

      * 6.2.4. Grupos de parênteses

      * 6.2.5. Exibições de contêiner

        * 6.2.5.1. Sintaxes de criação de lista

        * 6.2.5.2. Sintaxes de criação de conjunto

        * 6.2.5.3. Tuple displays

        * 6.2.5.4. Sintaxes de criação de dicionário

      * 6.2.6. Compreensões

        * 6.2.6.1. Filtering in comprehensions

        * 6.2.6.2. Complex comprehensions

        * 6.2.6.3. Unpacking in comprehensions

        * 6.2.6.4. Asynchronous comprehensions

        * 6.2.6.5. Gramática formal para compreensões

      * 6.2.7. Expressões geradoras

      * 6.2.8. Expressões yield

        * 6.2.8.1. Exemplos

        * 6.2.8.2. Funções geradoras assíncronas

    * 6.3. Primárias

      * 6.3.1. Referências de atributo

      * 6.3.2. Subscriptions and slicings

        * 6.3.2.1. Fatiamentos

        * 6.3.2.2. Comma-separated subscripts

        * 6.3.2.3. "Starred" subscriptions

        * 6.3.2.4. Formal subscription grammar

      * 6.3.3. Chamadas

    * 6.4. Expressão await

    * 6.5. O operador de potência

    * 6.6. Operações aritméticas unárias e bit a bit

    * 6.7. Operações binárias aritméticas

    * 6.8. Operações de deslocamento

    * 6.9. Operações binárias bit a bit

    * 6.10. Comparações

      * 6.10.1. Comparações de valor

      * 6.10.2. Operações de teste de pertinência

      * 6.10.3. Comparações de identidade

    * 6.11. Operações booleanas

    * 6.12. Expressões de atribuição

    * 6.13. Expressões condicionais

    * 6.14. Lambdas

    * 6.15. Listas de expressões

      * 6.15.1. Iterable unpacking

    * 6.16. Ordem de avaliação

    * 6.17. Precedência de operadores

  * 7. Instruções simples

    * 7.1. Instruções de expressão

    * 7.2. Instruções de atribuição

      * 7.2.1. Instruções de atribuição aumentada

      * 7.2.2. instruções de atribuição anotado

    * 7.3. A instrução "assert"

    * 7.4. A instrução "pass"

    * 7.5. A instrução "del"

    * 7.6. A instrução "return"

    * 7.7. A instrução "yield"

    * 7.8. A instrução "raise"

    * 7.9. A instrução "break"

    * 7.10. A instrução "continue"

    * 7.11. A instrução "import"

      * 7.11.1. Lazy imports

        * 7.11.1.1. Compatibility via "__lazy_modules__"

      * 7.11.2. Instruções future

    * 7.12. A instrução "global"

    * 7.13. A instrução "nonlocal"

    * 7.14. A instrução "type"

  * 8. Instruções compostas

    * 8.1. A instrução "if"

    * 8.2. A instrução "while"

    * 8.3. A instrução "for"

    * 8.4. A instrução "try"

      * 8.4.1. Cláusula "except"

      * 8.4.2. Cláusula "except*"

      * 8.4.3. Cláusula "else"

      * 8.4.4. Cláusula "finally"

    * 8.5. A instrução "with"

    * 8.6. A instrução "match"

      * 8.6.1. Visão Geral

      * 8.6.2. Guards

      * 8.6.3. Blocos irrefutáveis de case

      * 8.6.4. Padrões

        * 8.6.4.1. Padrões OR

        * 8.6.4.2. Padrões AS

        * 8.6.4.3. Padrões literais

        * 8.6.4.4. Padrões de captura

        * 8.6.4.5. Padrões curingas

        * 8.6.4.6. Padrões de valor

        * 8.6.4.7. Padrões de grupo

        * 8.6.4.8. Padrões de sequência

        * 8.6.4.9. Padrões de mapeamento

        * 8.6.4.10. Padrões de classe

    * 8.7. Definições de função

    * 8.8. Definições de classe

      * 8.8.1. Herança múltipla

    * 8.9. Corrotinas

      * 8.9.1. Definição de função de corrotina

      * 8.9.2. A instrução "async for"

      * 8.9.3. A instrução "async with"

    * 8.10. Listas de parâmetros de tipo

      * 8.10.1. Funções genéricas

      * 8.10.2. Classes genéricas

      * 8.10.3. Apelidos de tipo genérico

    * 8.11. Anotações

  * 9. Componentes de Alto Nível

    * 9.1. Programas Python completos

    * 9.2. Entrada de arquivo

    * 9.3. Entrada interativa

    * 9.4. Entrada de expressão

  * 10. Especificação completa da gramática

* Referência da bibliotecas embutidas do Python

  * Tipos embutidos

    * Teste do valor verdade

    * Operações booleanas --- "and", "or", "not"

    * Comparações

    * Tipos numéricos --- "int", "float", "complex"

      * Operações de bits em tipos inteiros

      * Métodos adicionais em tipos inteiros

      * Métodos adicionais em ponto flutuante

      * Métodos adicionais em números complexos

      * Hashing de tipos numéricos

    * Tipo booleano - "bool"

    * Tipos relacionados a iteração

      * Iteráveis

      * Iteradores

      * Tipos geradores

        * Iteradores geradores

        * Iteradores geradores assíncronos

    * Tipos sequências --- "list", "tuple", "range"

      * Operações comuns de sequências

      * Tipos sequência imutáveis

      * Tipos sequências mutáveis

      * Listas

      * Tuplas

      * Intervalos

    * Resumo dos métodos de tipo de sequência binária e de texto

    * Tipo sequência de texto --- "str"

      * String Methods

      * Strings literais formatadas (f-strings)

        * Especificador de depuração

        * Especificador de conversão

        * Especificador de formatação

      * literais de strings templates (t-strings)

      * Formatação de string no estilo "printf"

    * Tipos de sequência binária --- "bytes", "bytearray",
      "memoryview"

      * Objetos bytes

      * Objetos Bytearray

      * Operações com Bytes e Bytearray

      * Estilo de Formatação de bytes "printf"-style

      * Visões de memória

    * Tipo conjuntos --- "set", "frozenset"

    * Tipos mapeamentos --- "dict", "frozendict"

      * Objetos de visão de dicionário

      * Dicionários congelados

    * Tipos de Gerenciador de Contexto

    * Tipos de anotação de tipo --- *Apelido genérico*, *União*

      * Tipo Generic Alias

        * Classes genéricas padrão

        * Atributos especiais de objetos "GenericAlias"

      * Tipo União

    * Outros tipos embutidos

      * Módulos

      * Classes e Instâncias de Classes

      * Funções

      * Métodos

      * Objetos código

      * Objetos tipo

      * O objeto nulo

      * O Objeto Ellipsis

      * O Objeto NotImplemented

      * Objetos Internos

    * Atributos Especiais

    * Limitação de comprimento de string na conversão para inteiro

      * APIs afetadas

      * Configurando o limiter

      * Configuração recomendada

  * Constantes embutidas

    * Constantes adicionadas pelo módulo "site"

  * Funções embutidas

  * Exceções embutidas

    * Contexto da exceção

    * Herdando de exceções embutidas

    * Classes base

    * Exceções concretas

      * Exceções de sistema operacional

    * Avisos

    * Grupos de exceções

    * Hierarquia das exceções

  * Garantias de segurança de thread

    * Níveis de segurança de threads

      * Incompatível

      * Compatível

      * Seguro em objetos distintos

      * Seguro em objetos compartilhados

      * Atômica

    * Segurança de threads para objetos lista

    * Segurança de threads para objetos dict

    * Segurança de thread para objetos conjunto

    * Segurança para thread para objetos bytearray

    * Segurança para thread para objetos memoryview

  * Complexidade de tempo de operações em tipos embutidos

    * "list"

    * "tuple"

    * "dict", "frozendict"

    * "set", "frozenset"

    * "str", "bytes", "bytearray"

    * "memoryview"

    * "range"

    * Notas

* A biblioteca padrão do Python

  * Introdução

    * Observações sobre disponibilidade

      * Plataformas WebAssembly

      * Plataformas móveis

  * Serviços de Processamento de Texto

    * "string" --- Operações comuns de strings

      * Constantes de strings

      * Formatação personalizada de strings

      * Sintaxe das strings de formato

        * Minilinguagem de especificação de formato

        * Exemplos de formato

      * Strings template ($-strings)

      * Funções auxiliares

    * "string.templatelib" --- Suporte para literais de string
      template

      * Strings template

      * Tipos

      * Funções auxiliares

    * "re" --- Operações com expressões regulares

      * Sintaxe de expressão regular

        * Special characters

        * Special sequences

        * Standard escapes

      * Conteúdo do módulo

        * Sinalizadores

        * Funções

        * Exceções

      * Regular expression objects

      * Match objects

      * Regular expression examples

        * Checking for a pair

        * Simulando scanf()

        * search() vs. prefixmatch()

        * prefixmatch() vs. match()

        * Making a phonebook

        * Text munging

        * Finding all adverbs

        * Finding all adverbs and their positions

        * Raw string notation

        * Writing a tokenizer

    * "difflib" --- Helpers for computing deltas

      * Junk heuristic

      * The "difflib" algorithm

      * Diff generation

      * Junk definition functions

      * SequenceMatcher objects

      * Exemplos

        * SequenceMatcher examples

        * Differ example

        * A command-line interface to difflib

        * ndiff example

    * "textwrap" --- Quebra automática e preenchimento de texto

    * "unicodedata" --- Banco de dados de Unicode

    * "stringprep" --- Preparação de string para internet

    * "readline" --- Interface para o GNU readline

      * Arquivo init

      * Buffer de linha

      * Arquivo de histórico

      * Lista de histórico

      * Ganchos de inicialização

      * Autocomplemento

      * Exemplo

    * "rlcompleter" --- Função de autocomplemento para GNU readline

  * Serviços de Dados Binários

    * "struct" --- Interpreta bytes como dados binários empacotados

      * Funções e exceções

      * Format Strings

        * Byte Order, Size, and Alignment

        * Caracteres Formatados

        * Exemplos

      * Applications

        * Native Formats

        * Standard Formats

      * Classes

    * "codecs" --- Codec registry and base classes

      * Codec Base Classes

        * Error Handlers

        * Stateless Encoding and Decoding

        * Incremental Encoding and Decoding

          * IncrementalEncoder Objects

          * IncrementalDecoder Objects

        * Stream Encoding and Decoding

          * StreamWriter Objects

          * StreamReader Objects

          * StreamReaderWriter Objects

          * StreamRecoder Objects

      * Encodings and Unicode

      * Standard Encodings

      * Python Specific Encodings

        * Text Encodings

        * Binary Transforms

        * Standalone Codec Functions

        * Text Transforms

      * "encodings" --- Encodings package

      * "encodings.idna" --- Internationalized Domain Names in
        Applications

      * "encodings.mbcs" --- Windows ANSI codepage

      * "encodings.utf_8_sig" --- UTF-8 codec with BOM signature

  * Tipos de Dados

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

      * Função de fábrica para tuplas com campos nomeados
        "namedtuple()"

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

    * "types" --- Criação de tipos dinâmicos e nomes para tipos
      embutidos

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

  * Módulos Matemáticos e Numéricos

    * "numbers" --- Classes base abstratas numéricas

      * A torre numérica

      * Notas para implementadores de tipos

        * Adding more numeric ABCs

        * Implementando as operações aritméticas

    * "math" --- Funções matemáticas

      * Arimética de ponto flutuante

      * Funções de manipulação de ponto flutuante

      * Funções de potências, exponenciais e logarítmicas

      * Funções de soma e produto

      * Conversão angular

      * Funções trigonométricas

      * Funções hiperbólicas

      * Funções especiais

      * Funções de teoria dos números

      * Constantes

    * "math.integer" --- integer-specific mathematics functions

    * "cmath" --- Funções matemáticas para números complexos

      * Conversões de e para coordenadas polares

      * Funções de potência e logarítmicas

      * Funções trigonométricas

      * Funções hiperbólicas

      * Funções de classificação

      * Constantes

    * "decimal" --- Aritmética de ponto fixo decimal e ponto flutuante

      * Tutorial de início rápido

      * Objetos de Decimal

        * Operandos lógicos

      * Objetos de contexto

      * Constantes

      * Modos de arredondamento

      * Sinais

      * Observações sobre ponto flutuante

        * Atenuando o erro de arredondamento com  precisão maior

        * Valores especiais

      * Trabalhando com threads

      * Receitas

      * FAQ sobre Decimal

    * "fractions" --- Números racionais

    * "random" --- Gera números pseudoaleatórios

      * Funções de contabilidade

      * Funções para bytes

      * Funções para inteiros

      * Funções para sequências

      * Distribuições discretas

      * Distribuições com valor real

      * Gerador alternativo

      * Notas sobre reprodutibilidade

      * Exemplos

      * Receitas

      * Uso na linha de comando

      * Exemplos na linha de comando

    * "statistics" --- Funções estatísticas

      * Médias e medidas de valor central

      * Medidas de espalhamento

      * Estatísticas para relações entre duas entradas

      * Detalhes das funções

      * Exceções

      * Objetos "NormalDist"

      * Exemplos e receitas

        * Problemas clássicos de probabilidade

        * Entradas de Monte Carlo para simulações

        * Aproximação de distribuições binomiais

        * Classificador bayesiano ingênuo

  * Módulos de Programação Funcional

    * "itertools" --- Funções que criam iteradores para laços
      eficientes

      * Funções do intertools

      * Receitas com itertools

    * "functools" --- Funções e operações de ordem superior em objetos
      chamáveis

      * Objetos "partial"

    * "operator" --- Operadores padrões como funções

      * Mapeando os operadores para suas respectivas funções

      * Operadores in-place

  * Acesso a arquivos e diretórios

    * "pathlib" --- Caminhos do sistema de arquivos orientados a
      objetos

      * Uso básico

      * Exceções

      * Caminhos puros

        * Propriedades gerais

        * Operadores

        * Acessando partes individuais

        * Métodos e propriedades

      * Caminhos concretos

        * Analisando e gerando URIs

        * Expandindo e resolvendo caminhos

        * Consultando tipo de arquivo e status

        * Lendo e escrevendo arquivos

        * Lendo diretórios

        * Criando arquivos e diretórios

        * Copiando, movendo e excluindo

        * Permissões e propriedade

      * Linguagem de padrões

      * Comparação com o módulo "glob"

      * Comparação com os módulos "os" e "os.path"

        * Ferramentas correspondentes

      * Protocolos

    * "os.path" --- Manipulações comuns de nomes de caminhos

    * "stat" --- Interpretando resultados de "stat()"

    * "filecmp" --- Comparações de arquivos e diretórios

      * A classe "dircmp"

    * "tempfile" --- Gera arquivos temporários e diretórios

      * Exemplos

      * Deprecated functions and variables

    * "glob" --- Expansão de padrão de nome de arquivo no estilo Unix

      * Exemplos

    * "fnmatch" --- Correspondência de padrões de nome de arquivo Unix

    * "linecache" --- Acesso aleatório a linhas de texto

    * "shutil" --- Operações de arquivo de alto nível

      * Operações de diretório e arquivos

        * Operações de cópia eficientes dependentes da plataforma

        * Exemplo de copytree

        * exemplo rmtree

      * Operações de arquivamento

        * Exemplo de arquivo

        * Exemplo de arquivamento com *base_dir*

      * Consultando o tamanho do terminal de saída

  * Persistência de Dados

    * "pickle" --- Serialização de objetos Python

      * Relação com outros módulos Python

        * Comparação com "marshal"

        * Comparação com "json"

      * Formato de fluxo de dados

      * Interface do módulo

      * O que pode ser serializado e desserializado com pickle?

      * Serializando instâncias de classes com pickle

        * Persistência de objetos externos

        * Tabelas de despacho

        * Manipulação de objetos com estado

      * Redução personalizada para tipos, funções e outros objetos

      * Buffers fora da banda

        * API de provedor

        * API de consumidor

        * Exemplo

      * Restringindo globais

      * Desempenho

      * Exemplos

      * Interface de linha de comando

    * "copyreg" --- Registra funções de suporte "pickle"

      * Exemplo

    * "shelve" --- Python object persistence

      * Restrições

      * Exemplo

      * Exceções

    * "marshal" --- Serialização interna de objetos Python

    * "dbm" --- Interfaces para "banco de dados" Unix

      * Key and value types

      * "dbm.sqlite3" --- SQLite backend for dbm

      * "dbm.gnu" --- GNU database manager

      * "dbm.ndbm" --- New Database Manager

      * "dbm.dumb" --- Portable DBM implementation

    * "sqlite3" ---- interface DB-API 2.0 interface para bancos de
      dados SQLite

      * Tutorial

      * Referência

        * Funções do módulo

        * Constantes do módulo

        * Connection objects

        * Cursor objects

        * Row objects

        * Blob objects

        * PrepareProtocol objects

        * Exceções

        * SQLite and Python types

        * Default adapters and converters (deprecated)

        * Interface de linha de comando

      * Guias de como fazer

        * How to use placeholders to bind values in SQL queries

        * How to adapt custom Python types to SQLite values

          * How to write adaptable objects

          * How to register adapter callables

        * How to convert SQLite values to custom Python types

        * Adapter and converter recipes

        * How to use connection shortcut methods

        * How to use the connection context manager

        * How to work with SQLite URIs

        * How to create and use row factories

        * How to handle non-UTF-8 text encodings

      * Explicação

        * Controle de transações

          * Controle de transações através do atributo "autocommit"

          * Controle de transação através do atributo
            "isolation_level"

  * Compressão de Dados e Arquivamento

    * O pacote "compression"

    * "compression.zstd" --- Compactação compatível com o formato
      Zstandard

      * Exceções

      * Lendo e escrevendo arquivos compactados

      * Compactando e descompactando dados na memória

      * Dicionários de Zstandard

      * Controle avançado de parâmetros

      * Diversos

      * Exemplos

    * "zlib" --- Compactação compatível com **gzip**

    * "gzip" --- Suporte para arquivos **gzip**

      * Exemplos de uso

      * Interface de linha de comando

        * Opções de linha de comando

    * "bz2" --- Suporte para compressão **bzip2**

      * (Des)compressão de arquivos

      * (Des)compressão incremental

      * (De)compressão de uma só vez (one-shot)

      * Exemplos de uso

    * "lzma" --- Compressão usando o algoritmo LZMA

      * Lendo e escrevendo arquivos comprimidos

      * Comprimindo e descomprimindo dados na memória

      * Diversos

      * Especificando cadeias de filtros personalizadas

      * Constantes

      * Exemplos

    * "zipfile" --- Trabalha com arquivos ZIP

      * Objetos ZipFile

      * Objetos Path

      * Objetos PyZipFile

      * Objetos ZipInfo

      * Interface de linha de comando

        * Opções de linha de comando

      * Armadilhas de descompressão

        * Do próprio arquivo

        * Limitações do sistema de arquivos

        * Limitações de recursos

        * Interrupção

        * Comportamentos padrão da extração

    * "tarfile" --- Ler e gravar arquivos do tipo tar

      * Objetos TarFile

      * Objetos TarInfo

      * Filtros de extração

        * Default named filters

        * Filter errors

        * Dicas para verificação adicional

        * Suporte a versões mais antigas do Python

        * Stateful extraction filter example

      * Interface de Linha de Comando

        * Opções de linha de comando

      * Exemplos

        * Reading examples

        * Writing examples

      * Formatos tar suportados

      * Problemas de Unicode

  * Formatos de Arquivo

    * "csv" --- Leitura e escrita de arquivos CSV

      * Conteúdo do módulo

      * Dialects and formatting parameters

      * Reader objects

      * Writer objects

      * Exemplos

    * "configparser" --- Analisador sintático de arquivo de
      configuração

      * Início rápido

      * Tipos de dados suportados

      * Valores reservas

      * Estrutura dos arquivos INI

      * Seções não nomeadas

      * Interpolação de valores

      * Acesso através do protocolo de mapeamento

      * Personalizando o comportamento do analisador sintático

      * Exemplos de APIs legadas

      * Objetos ConfigParser

      * Objetos RawConfigParser

      * Exceções

    * "tomllib" --- Analisa arquivos TOML

      * Exemplos

      * Tabela de conversão

      * Considerações sobre limites e interoperabilidade

    * "netrc" --- Arquivo de processamento netrc

      * Objetos netrc

    * "plistlib" --- Gera e analisa arquivos Apple ".plist"

      * Exemplos

  * Serviços Criptográficos

    * "hashlib" --- Resumos de mensagens e hashes seguros

      * Algoritmos de hash

      * Uso

      * Construtores

      * Atributos

      * Objetos hash

      * Resumos de comprimento variável de SHAKE

      * Hash de arquivo

      * Derivação de chave

      * BLAKE2

        * Criando objetos hash

        * Constantes

        * Exemplos

          * Simple hashing

          * Using different digest sizes

          * Keyed hashing

          * Randomized hashing

          * Personalization

          * Modo árvore

        * Credits

    * "hmac" --- Código de autenticação de mensagem com chave hash

    * "secrets" --- Gera números aleatórios seguros para gerenciar
      segredos

      * Números aleatórios

      * Gerando tokens

        * Quantos bytes os tokens devem usar?

      * Outras funções

      * Receitas e melhores práticas

  * Serviços Genéricos do Sistema Operacional

    * "os" --- Diversas interfaces de sistema operacional

      * Nomes de arquivos, argumentos de linha de comando e variáveis
        de ambiente

      * Modo UTF-8 do Python

      * Parâmetros de processo

      * Criação de objetos arquivos

      * Operações dos descritores de arquivos

        * Consultando o tamanho de um terminal

        * Herança de descritores de arquivos

      * Arquivos e diretórios

        * Descritores de arquivo de temporizador

        * Atributos estendidos do Linux

      * Gerenciamento de processo

      * Interface do agendador

      * Diversas informações de sistema

      * Números aleatórios

    * "io" --- Ferramentas essenciais para trabalhar com fluxos

      * Visão Geral

        * E/S de texto

        * E/S binária

        * E/S bruta

      * Codificação do texto

        * Ativar EncodingWarning

      * Interface de alto nível do módulo

      * hierarquia de classe

        * I/O base classes

        * Raw file I/O

        * Buffered streams

        * E/S de texto

      * Static typing

      * Desempenho

        * E/S binária

        * E/S de texto

        * Multi-threading

        * Reentrancy

    * "time" --- Acesso e conversões de tempo

      * Funções

      * Constantes de ID de Relógio

      * Constantes de Fuso Horário

    * "logging" --- Recursos de registro de eventos para Python

      * Objetos Logger

      * Níveis de Logging

      * Objetos Handler

      * Formatter Objects

      * Filter Objects

      * LogRecord Objects

      * Atributos LogRecord

      * LoggerAdapter Objects

      * Thread Safety

      * Funções de Nível de Módulo

      * Module-Level Attributes

      * Integration with the warnings module

    * "logging.config" --- Configuração do módulo logging

      * Funções de configuração

      * Considerações de segurança

      * Esquema do Dicionário de Configuração

        * Detalhes do Esquema de Dicionário

        * Configuração Incremental

        * Conexões de objeto

        * Objetos definidos pelo usuário

        * Ordem de configuração de manipuladores

        * Acesso a objetos externos

        * Acesso a objetos internos

        * Resolução de importações e importadores personalizados

        * Configurando QueueHandler e QueueListener

      * Formato do arquivo de configuração

    * "logging.handlers" --- Manipuladores de logging

      * StreamHandler

      * FileHandler

      * NullHandler

      * WatchedFileHandler

      * BaseRotatingHandler

      * RotatingFileHandler

      * TimedRotatingFileHandler

      * SocketHandler

      * DatagramHandler

      * SysLogHandler

      * NTEventLogHandler

      * SMTPHandler

      * MemoryHandler

      * HTTPHandler

      * QueueHandler

      * QueueListener

    * "platform" ---  Acesso aos dados de identificação da plataforma
      subjacente

      * Multiplataforma

      * Plataforma Windows

      * Plataforma macOS

      * Plataforma iOS

      * Plataformas Unix

      * Plataformas Linux

      * Plataforma Android

      * Uso na linha de comando

    * "errno" --- Símbolos padrão do sistema errno

    * "ctypes" --- Uma biblioteca de funções externas para Python

      * Tutorial do ctypes

        * Carregando bibliotecas de ligação dinâmica

        * Acessando funções de dlls carregadas

        * Chamando funções

        * Tipos de dados fundamentais

        * Chamando funções, continuação

        * Chamando funções variadas

        * Chamando funções com seus próprios tipos de dados
          personalizados

        * Especificando os tipos de argumentos necessários (protótipos
          de função)

        * Tipos de Retorno

        * Passando ponteiros (ou: passando parâmetros por referência)

        * Estruturas e uniões

        * Layout, alinhamento e ordem de bytes de estrutura/união

        * Campos de bit em estruturas e uniões

        * Vetores

        * Ponteiros

        * Segurança de thread (Thread safety) sem o GIL

        * Conversão de Tipos

        * Tipos Incompletos

        * Funções Callbacks

        * Acessando valores exportados de dlls

        * Surpresas

        * Tipos de dados de tamanho variável

      * Referência ctypes

        * Loading shared libraries

        * Encontrando bibliotecas compartilhadas

        * Listing loaded shared libraries

        * Foreign functions

        * Function prototypes

        * Funções utilitárias

        * Data types

        * Tipos de dados fundamentais

        * Windows data types

          * Simple types

          * Handle types

          * Structures

          * Pointer types

          * Constants and functions

        * Tipos de dados estruturados

        * Arrays and pointers

        * Exceções

  * Bibliotecas de interface de linha de comando

    * "argparse" --- Analisador sintático para opções de linha de
      comando, argumentos e subcomandos

      * Objetos ArgumentParser

        * "prog"

        * "usage"

        * "description"

        * "epilog"

        * "parents"

        * "formatter_class"

        * "prefix_chars"

        * "fromfile_prefix_chars"

        * "argument_default"

        * "allow_abbrev"

        * "conflict_handler"

        * "add_help"

        * "exit_on_error"

        * "suggest_on_error"

        * "color"

      * O método add_argument()

        * "name" ou "flags"

        * "action"

        * "nargs"

        * "const"

        * "default"

        * "type"

        * "choices"

        * "required"

        * "help"

        * "metavar"

        * "dest"

        * "deprecated"

        * Classes de ação

      * O método parse_args()

        * Sintaxe de valores da opção

        * Argumentos inválidos

        * Argumentos contendo "-"

        * Abreviações de argumento (correspondência de prefixo)

        * Além do "sys.argv"

        * O objeto Namespace

      * Outros utilitários

        * Subcomandos

        * Objetos FileType

        * Grupos de argumentos

        * Exclusão mútua

        * Padrões do analisador sintático

        * Imprimindo a ajuda

        * Análise parcial

        * Personalizando a análise de arquivos

        * Métodos de saída

        * Análise misturada

        * Registrando ações e tipos personalizados

      * Exceções

        * Tutorial de Argparse

          * Conceitos

          * O básico

          * Apresentando os argumentos posicionais

          * Apresentando os argumentos opcionais

            * Opções curtas

          * Combinando argumentos posicionais e opcionais

          * Avançando um pouco mais

            * Especificando argumentos ambíguos

            * Opções conflitantes

          * Como traduzir a saída do argparse

          * Conversores de tipo personalizados

          * Conclusão

        * Migrando código "optparse" para "argparse"

    * "optparse" --- Analisador sintático para opções de linha de
      comando

      * Escolhendo uma biblioteca de análise de linha de comando

      * Introdução

      * Contexto

        * Terminologia

        * Para que servem as opções?

        * Para que servem os argumentos posicionais?

      * Tutorial

        * Compreendendo as ações de opções

        * A ação store

        * Manipulando opções (sinalizadores) booleanas

        * Outras ações

        * Valores padrão

        * Gerando texto de ajuda

          * Agrupando opções

        * Exibindo uma string de versão

        * How "optparse" handles errors

        * Juntando tudo

      * Guia de referência

        * Criando o analisador sintático

        * Preenchendo o analisador sintático

        * Definindo as opções

        * Atributos da classe Option

        * Ações de opção padrão

        * Tipos de opção padrão

        * Análise de argumentos

        * Consultando e manipulando seu analisador sintático de opções

        * Conflitos entre opções

        * Limpeza

        * Outros métodos

      * Funções de retorno de opção

        * Definindo uma opção de retorno de chamada

        * Como os retornos de chamada são chamados

        * Levantando erros em uma função de retorno

        * Exemplo de função de retorno 1: retorno de chamada trivial

        * Exemplo de função de retorno 2: verificar a ordem das opções

        * Exemplo 3 de função de retorno: verificar a ordem das opções
          (generalizada)

        * Exemplo de função de retorno 4: verificar uma condição
          arbitrária

        * Exemplo de função de retorno 5: argumentos fixos

        * Exemplo de função de retorno 6: argumentos variáveis

      * Extending "optparse"

        * Adicionando novos tipos

        * Adicionando novas ações

      * Exceções

    * "getpass" --- Entrada de senha portátil

    * "fileinput" --- Itera sobre linhas de múltiplos fluxos de
      entrada

    * "curses" --- Gerenciador de terminal para visualizadores de
      células de caracteres.

      * Funções

      * Window objects

      * Constantes

    * "curses.textpad" --- Text input widget for curses programs

      * Textbox objects

    * "curses.ascii" --- Utilitários para caracteres ASCII

    * "curses.panel" --- Uma extensão de pilha de painéis para o
      curses

      * Funções

      * Panel objects

    * "cmd" --- Suporte para interpretadores de comando orientado a
      linhas

      * Objetos Cmd

      * Exemplo do Cmd

  * Execução Concorrente

    * "threading" --- Paralelismo baseado em threads

      * Introdução

      * GIL and performance considerations

      * Referência

        * Thread-local data

        * Thread objects

        * Lock objects

        * RLock objects

        * Condition objects

        * Semaphore objects

        * "Semaphore" example

        * Event objects

        * Timer objects

        * Barrier objects

      * Using locks, conditions, and semaphores in the "with"
        statement

      * Iterator synchronization

    * "multiprocessing" --- Paralelismo baseado em processo

      * Introdução

        * A classe "Process"

        * Contextos e métodos de inicialização

        * Trocando objetos entre processos

        * Sincronização entre processos

        * Compartilhando estado entre processos

        * Usando um pool de workers

      * Referência

        * Global start method

        * "Process" e exceções

        * Encadeamentos e filas

        * Diversos

        * Objetos de conexão

        * Primitivas de sincronização

        * Objetos "ctypes" compartilhados

          * The "multiprocessing.sharedctypes" module

        * Gerenciadores

          * Customized managers

          * Using a remote manager

        * Objetos proxies

          * Limpeza

        * Process Pools

        * Listeners and Clients

          * Formatos de Endereços

        * Authentication keys

        * Gerando logs

        * The "multiprocessing.dummy" module

      * Programming guidelines

        * All start methods

        * The *spawn* and *forkserver* start methods

      * Exemplos

    * "multiprocessing.shared_memory" --- Memória compartilhada para
      acesso direto entre processos

    * O pacote "concurrent"

    * "concurrent.futures" --- Launching parallel tasks

      * Executor Objects

      * ThreadPoolExecutor

        * Exemplo de ThreadPoolExecutor

      * InterpreterPoolExecutor

      * ProcessPoolExecutor

        * ProcessPoolExecutor Example

      * Future Objects

      * Module Functions

      * Exception classes

    * "concurrent.interpreters" --- Múltiplos interpretadores no mesmo
      processo

      * Detalhes chaves

      * Introdução

        * Multiple Interpreters and Isolation

        * Running in an Interpreter

        * Concurrency and Parallelism

        * Communication Between Interpreters

        * "Sharing" Objects

      * Referência

        * Objetos interpretador

        * Exceções

        * Communicating Between Interpreters

      * Uso básico

    * "subprocess" --- Gerenciamento de subprocessos

      * Using the "subprocess" Module

        * Argumentos usados frequentemente

        * Construtor Popen

        * Exceções

      * Considerações de Segurança

      * Objetos Popen

      * Windows Popen Helpers

        * Constantes do Windows

      * API de alto nível mais antiga

      * Replacing Older Functions with the "subprocess" Module

        * Replacing **/bin/sh** shell command substitution

        * Replacing shell pipeline

        * Substituindo "os.system()"

        * Replacing the "os.spawn" family

        * Replacing "os.popen()"

      * Legacy Shell Invocation Functions

      * Notas

        * Timeout Behavior

        * Converter uma sequência de argumentos em uma string no
          Windows

        * Disable use of "posix_spawn()"

    * "sched" --- Agendador de eventos

      * Objetos Scheduler

    * "queue" --- Uma classe de fila sincronizada

      * Objetos Queue

        * Waiting for task completion

        * Terminating queues

      * Objetos SimpleQueue

    * "contextvars" --- Variáveis de contexto

      * Variáveis de contexto

      * Gerenciamento de contexto manual

      * Suporte a asyncio

    * "_thread"--- API de segmentação de baixo nível

  * Comunicação em Rede e Interprocesso

    * "asyncio" --- E/S assíncrona

      * Runners

        * Executando um programa asyncio

        * Runner context manager

        * Handling Keyboard Interruption

      * Coroutines and tasks

        * Corrotinas

        * Aguardáveis

        * Creating tasks

        * Task cancellation

        * Task groups

        * Dormindo

        * Running tasks concurrently

        * Eager task factory

        * Shielding from cancellation

        * Tempo limite

        * Waiting primitives

        * Running in threads

        * Scheduling from other threads

        * Introspecção

        * Task object

      * Streams

        * StreamReader

        * StreamWriter

        * Exemplos

          * Cliente para eco TCP usando streams

          * Servidor eco TCP usando streams

          * Obtém headers HTTP

          * Registra um soquete aberto para aguardar por dados usando
            streams

      * Synchronization Primitives

        * Lock

        * Evento

        * Condição

        * Semaphore

        * BoundedSemaphore

        * Barrier

      * Subprocessos

        * Criando subprocessos

        * Constantes

        * Interagindo com subprocessos

          * Subprocesso e Threads

          * Exemplos

      * Filas

        * Queue

        * Fila de prioridade

        * Filas LIFO (último a entrar, primeiro a sair)

        * Exceções

        * Exemplos

      * Exceções

      * Call graph introspection

        * Funções utilitárias de baixo nível

      * Command-line introspection tools

        * Opções de linha de comando

      * Laço de eventos

        * Event loop methods

          * Executar e interromper o laço

          * Agendando funções de retorno

          * Agendando funções de retorno atrasadas

          * Creating futures and tasks

          * Abrindo conexões de rede

          * Criando servidores de rede

          * Transferindo arquivos

          * TLS upgrade

          * Observando descritores de arquivo

          * Trabalhando com objetos soquete diretamente

          * DNS

          * Trabalhando com encadeamentos

          * Sinais Unix

          * Executando código em conjuntos de threads ou processos

          * Error handling API

          * Habilitando o modo de debug

          * Running subprocesses

        * Callback handles

        * Server objects

        * Event loop implementations

        * Exemplos

          * Hello World com call_soon()

          * Exibe a data atual com call_later()

          * Observa um descritor de arquivo por eventos de leitura

          * Define tratadores de sinais para SIGINT e SIGTERM

      * Futuros

        * Funções Future

        * Objeto Future

      * Transports e Protocols

        * Transportes

          * Transports Hierarchy

          * Base Transport

          * Read-only Transports

          * Write-only Transports

          * Transportes de datagrama

          * Transportes de Subprocesso

        * Protocolos

          * Protocolos de Base

          * Base Protocol

          * Streaming Protocols

          * Protocolos de Streaming Bufferizados

          * Protocolos de Datagramas

          * Protocolos de Subprocesso

        * Exemplos

          * TCP Echo Server

          * TCP Echo Client

          * UDP Echo Server

          * UDP Echo Client

          * Connecting Existing Sockets

          * loop.subprocess_exec() and SubprocessProtocol

      * Políticas

        * Getting and Setting the Policy

        * Policy Objects

        * Custom Policies

      * Suporte a plataformas

        * Todas as plataformas

        * Windows

          * Suporte para subprocesso no Windows

        * macOS

      * Extensão

        * Writing a custom event loop

        * Construtores privados de Future e Task

        * Suporte ao ciclo de vida de tarefas

      * Índice da API de alto nível

        * Tarefas

        * Filas

        * Subprocessos

        * Streams

        * Sincronização

        * Exceções

      * Índice de APIs de baixo nível

        * Obtendo o laço de eventos

        * Métodos do laço de eventos

        * Transportes

        * Protocolos

        * Políticas de laço de eventos

      * Desenvolvendo com asyncio

        * Modo de Depuração

        * Concorrência e Múltiplas Threads

        * Executando código bloqueante

        * Gerando logs

        * Detectar corrotinas nunca aguardadas

        * Detectar exceções nunca recuperadas

        * Asynchronous generators best practices

          * Close asynchronous generators explicitly

          * Create asynchronous generators only when the event loop is
            running

          * Avoid concurrent iteration and closure of the same
            generator

      * asyncio and free-threaded Python

        * Thread safety considerations

        * Using asyncio with threads

        * Producer/consumer across threads

    * "socket" --- Interface de rede de baixo nível

      * Famílias de soquete

      * Conteúdo do módulo

        * Exceções

        * Constantes

        * Funções

          * Criação de sockets

          * Outras funções

      * Socket Objects

      * Notas sobre tempo limite de soquete

        * Timeouts and the "connect" method

        * Timeouts and the "accept" method

      * Exemplo

    * "ssl" --- Invólucro de TLS/SSL para objetos socket

      * Funções, constantes e exceções.

        * Criação de socket

        * Criação de contexto

        * Signature algorithms

        * Exceções

        * Random generation

        * Manipulação de certificados

        * Constantes

      * SSL sockets

      * SSL contexts

      * Certificados

        * Certificate chains

        * CA certificates

        * Combined key and certificate

        * Self-signed certificates

      * Exemplos

        * Testing for SSL support

        * Client-side operation

        * Server-side operation

      * Notes on non-blocking sockets

      * Memory BIO support

      * SSL session

      * Considerações de segurança

        * Best defaults

        * Manual settings

          * Verifying certificates

          * Protocol versions

          * Cipher selection

        * Multi-processing

      * TLS 1.3

    * "select" --- Waiting for I/O completion

      * "/dev/poll" polling objects

      * Edge and level trigger polling (epoll) objects

      * Polling objects

      * Kqueue objects

      * Kevent objects

    * "selectors" --- High-level I/O multiplexing

      * Introdução

      * Classes

      * Exemplos

    * "signal" --- Define manipuladores para eventos assíncronos

      * Regras gerais

        * Execução de manipuladores de sinais Python

        * Sinais e threads

      * Conteúdo do módulo

      * Exemplos

      * Nota sobre SIGPIPE

      * Nota sobre manipuladores de sinais e exceções

    * "mmap" --- Suporte a arquivos mapeados na memória

      * ACCESS_* constants

      * Page size constants

      * PROT_* constants

      * MADV_* constants

      * MAP_* constants

      * MS_* constants

  * Manuseio de Dados na Internet

    * "email" --- Um e-mail e um pacote MIME manipulável

      * "email.message": Representing an email message

      * "email.parser": Parsing email messages

        * API do FeedParser

        * Parser API

        * Additional notes

      * "email.generator": Geração de documentos MIME

      * "email.policy": Policy Objects

      * "email.errors": Classes de Exceção e Defeito.

      * "email.headerregistry": Custom Header Objects

      * "email.contentmanager": Gerenciando conteúdo MIME

        * Content Manager Instances

      * "email": Exemplos

      * "email.message.Message": Representing an email message using
        the "compat32" API

      * "email.mime""email.mime": Criando e-mail e objetos MIME do
        zero

      * "email.header": Internationalized headers

      * "email.charset": Representando conjuntos de caracteres

      * "email.encoders": Codificadores

      * "email.utils": Utilitários diversos

      * "email.iterators": Iteradores

    * "json" --- Codificador e decodificador JSON

      * Uso básico

      * Codificadores e decodificadores

      * Exceções

      * Conformidade e interoperabilidade entre padrões

        * Codificações de caracteres

        * Valores numéricos infinitos e NaN

        * Nomes repetidos dentro de um objeto

        * Valores não objeto e não vetor de nível superior

        * Limitações de implementação

      * Interface de linha de comando

        * Opções de linha de comando

    * "mailbox" --- Manipule caixas de entradas em vários formatos

      * Objetos "Mailbox"

        * "Maildir" objects

        * "mbox" objects

        * "MH" objects

        * "Babyl" objects

        * "MMDF" objects

      * "Message" objects

        * "MaildirMessage" objects

        * "mboxMessage" objects

        * "MHMessage" objects

        * "BabylMessage" objects

        * "MMDFMessage" objects

      * Exceções

      * Exemplos

    * "mimetypes" --- Mapeia nomes de arquivos para tipos MIME

      * Objetos MimeTypes

      * Uso na linha de comando

      * Exemplos na linha de comando

    * "base64" --- Base16, Base32, Base64, Base85 Data Encodings

      * RFC 4648 Encodings

      * Base85 Encodings

      * Legacy Interface

      * Considerações de Segurança

    * "binascii" --- Converte entre binário e ASCII

    * "quopri" --- Codifica e decodifica dados MIME imprimidos entre
      aspas

  * Ferramentas de Processamento de Markup Estruturado

    * "html" --- Suporte HTML (HyperText Markup Language)

    * "html.parser" --- Analisador simples de HTML e XHTML

      * Exemplo de aplicação para análise de HTML

      * Métodos "HTMLParser"

      * Exemplos

    * "html.entities" --- Definições de entidades gerais de HTML

    * Módulos de Processamento de XML

      * Segurança no XML

    * "xml.etree.ElementTree" --- A API XML ElementTree

      * Tutorial

        * Árvore e elementos XML

        * Analisando XML

        * A API de pull para análise sem bloqueio

        * Encontrando elementos interessantes

        * Modificando um arquivo XML

        * Construindo documentos XML

        * Analisando XML com espaços de nomes

      * Suporte a XPath

        * Exemplo

        * Supported XPath syntax

      * Referência

        * Funções

      * Suporte a XInclude

        * Exemplo

      * Referência

        * Funções

        * Element Objects

        * ElementTree Objects

        * QName Objects

        * TreeBuilder Objects

        * Objetos XMLParser

        * XMLPullParser Objects

        * Exceções

    * "xml.dom" --- The Document Object Model API

      * Conteúdo do módulo

      * Objects in the DOM

        * DOMImplementation Objects

        * Objetos Node

        * Objetos NodeList

        * DocumentType Objects

        * Document Objects

        * Element Objects

        * Attr Objects

        * NamedNodeMap Objects

        * DocumentFragment Objects

        * CharacterData Objects

        * Comment Objects

        * Text and CDATASection Objects

        * Objetos ProcessingInstruction

        * Entity Objects

        * Notation Objects

        * Exceções

      * Conformance

        * Type Mapping

        * Accessor Methods

    * "xml.dom.minidom" --- Minimal DOM implementation

      * Objetos DOM

      * DOM Example

      * minidom e o padrão DOM

    * "xml.dom.pulldom" --- Suporte para construir árvores parciais de
      DOM

      * Objetos DOMEventStream

    * "xml.sax" --- Support for SAX2 parsers

      * SAXException Objects

    * "xml.sax.handler" --- Classes base para manipuladores de SAX

      * ContentHandler Objects

      * DTDHandler Objects

      * EntityResolver Objects

      * ErrorHandler Objects

      * LexicalHandler Objects

    * "xml.sax.saxutils" --- Utilitários de SAX

    * "xml.sax.xmlreader" --- Interface for XML parsers

      * XMLReader Objects

      * IncrementalParser Objects

      * Locator Objects

      * InputSource Objects

      * The "Attributes" Interface

      * The "AttributesNS" Interface

    * "xml.parsers.expat" --- Fast XML parsing using Expat

      * Objetos XMLParser

      * Exceções ExpatError

      * Exemplo

      * Content Model Descriptions

      * Constantes de erro de expatriados

  * Protocolos de Internet e Suporte

    * "webbrowser" --- Controlador de navegador web conveniente

      * Interface de linha de comando

      * Objetos controladores de navegador

    * "wsgiref" --- Implementação de referência e utilitários WSGI

      * "wsgiref.util" -- WSGI environment utilities

      * "wsgiref.headers" -- WSGI response header tools

      * "wsgiref.simple_server" -- a simple WSGI HTTP server

      * "wsgiref.validate" --- WSGI conformance checker

      * "wsgiref.handlers" -- server/gateway base classes

      * "wsgiref.types" -- WSGI types for static type checking

      * Exemplos

    * "urllib" --- Módulos de manipulação de URL

    * "urllib.request" --- Biblioteca extensível para abrir URLs

      * Objeto Request

      * OpenerDirector Objects

      * BaseHandler Objects

      * HTTPRedirectHandler Objects

      * HTTPCookieProcessor Objects

      * ProxyHandler Objects

      * HTTPPasswordMgr Objects

      * HTTPPasswordMgrWithPriorAuth Objects

      * AbstractBasicAuthHandler Objects

      * HTTPBasicAuthHandler Objects

      * ProxyBasicAuthHandler Objects

      * AbstractDigestAuthHandler Objects

      * HTTPDigestAuthHandler Objects

      * ProxyDigestAuthHandler Objects

      * HTTPHandler Objects

      * Objetos HTTPSHandler

      * FileHandler Objects

      * DataHandler Objects

      * FTPHandler Objects

      * CacheFTPHandler Objects

      * Objetos UnknownHandler

      * HTTPErrorProcessor Objects

      * Exemplos

      * Legacy interface

      * "urllib.request" Restrictions

    * "urllib.response" --- Response classes used by urllib

    * "urllib.parse" --- Analisa URLs para componentes

      * Análise de URL

      * Segurança ao analisar URLs

      * Analisando bytes codificados em ASCII

      * Structured Parse Results

      * URL Quoting

    * "urllib.error" --- Classes de exceção levantadas por
      urllib.request

    * "urllib.robotparser" ---  Analisador sintático de robots.txt

    * "http" --- Módulos HTTP

      * Códigos de estado HTTP

      * Categoria de estado HTTP

      * Métodos HTTP

    * "http.client" --- HTTP protocol client

      * Objetos de HTTPConnection

      * Objetos HTTPResponse

      * Exemplos

      * HTTPMessage Objects

    * "ftplib" --- FTP protocol client

      * Referência

        * FTP objects

        * FTP_TLS objects

        * Module variables

    * "poplib" --- Cliente de protocolo POP3

      * Objetos POP3

      * Exemplo POP3

    * "imaplib" --- IMAP4 protocol client

      * Objetos IMAP4

      * Exemplo IMAP4

    * "smtplib" --- Cliente de protocolo SMTP

      * Objetos SMTP

      * Exemplo SMTP

    * "uuid" --- Objetos UUID conforme **RFC 9562**

      * Uso na linha de comando

      * Exemplo

      * Exemplo de linha de comando

    * "socketserver" --- Um framework para servidores de rede

      * Notas sobre criação do servidor

      * Objetos Server

      * Objetos manipulador de requisições

      * Exemplos

        * Exemplo de "socketserver.TCPServer"

        * Exemplo "socketserver.UDPServer"

        * Mixins assíncronos

    * "http.server" --- HTTP servers

      * Interface de linha de comando

      * Considerações de segurança

    * "http.cookies" --- HTTP state management

      * Objetos Cookie

      * Objetos Morsel

      * Exemplo

    * "http.cookiejar" --- Cookie handling for HTTP clients

      * CookieJar and FileCookieJar objects

      * FileCookieJar subclasses and co-operation with web browsers

      * CookiePolicy objects

      * DefaultCookiePolicy objects

      * Cookie objects

      * Exemplos

    * "xmlrpc" --- Módulos de servidor e cliente XMLRPC

    * "xmlrpc.client" --- Cliente XML-RPC

      * Objetos ServerProxy

      * Objetos DateTime

      * Objetos Binários

      * Objetos Fault

      * Objetos ProtocolError

      * Objetos MultiCall

      * Convenience Functions

      * Exemplo de uso do cliente

      * Example of Client and Server Usage

    * "xmlrpc.server" --- Servidores XML-RPC básicos

      * SimpleXMLRPCServer objects

        * SimpleXMLRPCServer example

      * CGIXMLRPCRequestHandler

      * Documentando servidor XMLRPC

      * DocXMLRPCServer objects

      * DocCGIXMLRPCRequestHandler

    * "ipaddress" --- Biblioteca de manipulação de IPv4/IPv6

      * Funções de fábrica de conveniência

      * Endereços IP

        * Objetos de endereço

        * Conversão para strings e inteiros

        * Operadores

          * Operadores de comparação

          * Operadores aritméticos

      * Definições de rede IP

        * Prefixo, máscara de rede e máscara de host

        * Objetos de rede

        * Operadores

          * Operadores lógicos

          * Iteração

          * Redes como contêineres de endereços

      * Objetos de interface

        * Operadores

          * Operadores lógicos

      * Outras funções de nível de módulo

      * Exceções personalizadas

  * Serviços Multimídia

    * "wave" --- Read and write WAV files

      * Objetos Wave_read

      * Objetos Wave_write

    * "colorsys" --- Conversões entre sistemas de cores

  * Internacionalização

    * "gettext" --- Serviços de internacionalização multilíngues

      * API do GNU **gettext**

      * API baseada em classe

        * A classe "NullTranslations"

        * A classe "GNUTranslations"

        * Suporte a catálogo de mensagens do Solaris

        * O construtor Catalog

      * Internacionalizando seus programas e módulos

        * Localizando seu módulo

        * Localizando sua aplicação

        * Alterando os idiomas durante o uso

        * Traduções adiadas

      * Reconhecimentos

    * "locale" --- Serviços de internacionalização

      * Histórico, detalhes, dicas, dicas e advertências

      * Nomes de localidades

      * Para escritores de extensão e programas que incorporam Python

      * Acesso a catálogos de mensagens

  * Interfaces gráficas de usuário com Tk

    * "tkinter" --- Interface Python para Tcl/Tk

      * Arquitetura

      * Módulos Tkinter

      * O salva-vidas do Tkinter

        * Um programa "Olá Mundo"

        * Importantes conceitos TK

        * Desvendando como o Tkinter encapsula o Tcl/Tk

        * Como é que eu...? Que opção faz...?

        * Explorando o manual de referências do Tcl/Tk

      * Modelo de threading

      * Handy reference

        * Setting options

        * Geometry management

        * Coupling widget variables

        * The window manager

        * Tk option data types

        * Bindings and events

        * The index parameter

        * Imagens

      * Referência

        * Base and mixin classes

        * Toplevel widgets

        * Widget classes

        * Variable classes

        * Image classes

        * Other classes

        * Module-level functions

        * File handlers

        * Constantes

    * "tkinter.colorchooser" --- Diálogo de escolha de cor

    * "tkinter.font" --- Invólucro de fontes Tkinter

    * Tkinter dialogs

      * "tkinter.simpledialog" --- Standard Tkinter input dialogs

      * "tkinter.filedialog" --- File selection dialogs

        * Native load/save dialogs

      * "tkinter.commondialog" --- Dialog window templates

      * "tkinter.dialog" --- Classic Tk dialog boxes

    * "tkinter.messagebox" --- Prompts de mensagem do Tkinter

    * "tkinter.scrolledtext" --- Widget de texto com *scrollbar*

    * "tkinter.dnd" --- Suporte para arrastar e soltar

    * "tkinter.ttk" --- Widgets temáticos do Tk

      * Usando Ttk

      * Ttk widgets

      * Widget

        * Standard options

        * Scrollable widget options

        * Label options

        * Compatibility options

        * Widget states

        * ttk.Widget

      * Combobox

        * Opções

        * Eventos virtuais

        * ttk.Combobox

      * Spinbox

        * Opções

        * Eventos virtuais

        * ttk.Spinbox

      * Notebook

        * Opções

        * Tab options

        * Tab identifiers

        * Eventos virtuais

        * ttk.Notebook

      * Progressbar

        * Opções

        * ttk.Progressbar

      * Separator

        * Opções

      * Sizegrip

        * Platform-specific notes

        * Bugs

      * Treeview

        * Opções

        * Item options

        * Tag options

        * Column identifiers

        * Eventos virtuais

        * ttk.Treeview

      * Ttk styling

        * Layouts

      * Additional widgets

    * IDLE --- Editor e console Python

      * Menus

        * Menu File (Shell e Editor)

        * Menu Edit (Shell e Editor)

        * Menu Format (somente na janela do Editor)

        * Menu Run (somente na janela do Editor)

        * Menu Shell (somente na janela do Shell)

        * Menu Debug (somente na janela do Shell)

        * Menu Options (Shell e Editor)

        * Menu Window (Shell e Editor)

        * Menu Help (Shell e Editor)

        * Menus de contexto

      * Edição e navegação

        * Janelas do Editor

        * Teclas de atalho

        * Indentação automática

        * Busca e substituição

        * Autocomplementos

        * Dicas de chamada

        * Formatação de bloco

        * Contexto de código

        * Janela Shell

        * Cores de texto

      * Inicialização e execução de código

        * Uso na linha de comando

        * Falha na inicialização

        * Execução de código do usuário

        * Saída do usuário na Shell

        * Developing tkinter applications

        * Running without a subprocess

      * Ajuda e preferências

        * Help sources

        * Configurando preferências

        * IDLE on macOS

        * Extensions

      * idlelib --- implementation of IDLE application

    * "turtle" --- Gráficos tartaruga

      * Tutorial

        * Iniciando um ambiente da tartaruga

        * Desenho básico

          * Controle da Caneta

          * A posição da tartaruga

        * Criação de padrões algorítmicos

      * Referência

        * Métodos e funções Turtle

          * Movimento e desenho

          * Fala o estado de Turtle

          * Configurações de medida

          * Controle da Caneta

            * Estado do Desenho

            * Controle da Cor

            * Preenchimento

            * Mais sobre o Controle do Desenho

          * Estado da tartaruga

            * Visibilidade

            * Aparência

          * Eventos Utilizados

          * Métodos Especiais da Tartaruga

        * Métodos e funções de janela

          * Controle da Janela

          * Controle da animação

          * Usando os eventos de tela

          * Métodos de entrada

          * Configurações e métodos especiais

          * Métodos apenas de janela

        * Classes Públicas

        * Exceções

      * Guias de como fazer

        * How to automatically begin and end filling

        * How to use compound shapes

        * How to use the "turtle" module namespace

        * How to use turtle graphics in a script

        * How to use object-oriented turtle graphics

        * How to use "help()"

        * Tradução de docstrings em diferentes idiomas

        * Como configurar Screen and Turtles

      * Explicação

      * "turtledemo" --- Scripts de Demonstração

  * Ferramentas de Desenvolvimento

    * "typing" --- Suporte para dicas de tipo

      * Especificação para o sistema de tipos do Python

      * Apelidos de tipo

      * NewType

      * Anotações de objetos chamáveis

      * Genéricos

      * Anotando tuplas

      * O tipo de objetos de classe

      * Anotando geradores e corrotinas

      * Tipos genéricos definidos pelo usuário

      * O tipo "Any"

      * Subtipagem nominal vs estrutural

      * Conteúdo do módulo

        * Tipos primitivos especiais

          * Tipos especiais

          * Formas especiais

          * Criando tipos genéricos e apelidos de tipo

          * Outras diretivas especiais

        * Protocolos

        * ABCs e protocolos para trabalhar com E/S

        * Funções e decoradores

        * Auxiliares de introspecção

        * Constante

        * Apelidos descontinuados

          * Apelidos de tipos embutidos

          * Apelidos para tipos em "collections"

          * Apelidos de outros tipos concretos

          * Apelidos de contêineres ABC em "collections.abc".

          * Apelidos para ABCs assíncronas em "collections.abc"

          * Apelidos para outros ABCs em "collections.abc".

          * Apelidos de ABCs da "contextlib"

      * Cronograma de descontinuação dos principais recursos

    * "pydoc" --- Gerador de documentação e sistema de ajuda online

    * Modo de Desenvolvimento do Python

      * Efeitos do Modo de Desenvolvimento do Python

      * Exemplo de ResourceWarning

      * Exemplo de erro de descritor de arquivo inválido

    * "doctest" --- Teste exemplos interativos de Python

      * Uso simples: verificando exemplos em Docstrings

      * Utilização comum: Verificando exemplos em um arquivo texto

      * Uso na linha de comando

      * Como ele funciona

        * Quais docstrings são examinadas?

        * Como os exemplos de docstrings são reconhecidos?

        * Qual é o contexto de execução?

        * E quanto às exceções?

        * Flags opcionais

        * Directives

        * Avisos

      * Basic API

      * API do Unittest

      * Advanced API

        * DocTest Objects

        * Example Objects

        * DocTestFinder objects

        * DocTestParser objects

        * TestResults objects

        * DocTestRunner objects

        * OutputChecker objects

      * Depuração

      * Soapbox

    * "unittest" --- Framework de testes unitários

      * Exemplo Básico

      * Interface de Linha de Comando

        * Opções de linha de comando

      * Test Discovery

      * Organizando código teste

      * Reutilizando códigos de teste antigos

      * Ignorando testes e falhas esperadas

      * Distinguindo iterações de teste utilizando subtestes

      * Classes e funções

        * Casos de teste

        * Grouping tests

        * Carregando e executando testes

          * load_tests Protocol

      * Classes e Módulos de Definição de Contexto

        * setUpClass and tearDownClass

        * setUpModule and tearDownModule

      * Tratamento de sinal

    * "unittest.mock" --- mock object library

      * Guia Rápido

      * A classe Mock

        * Fazendo chamadas

        * Deletando Atributos

        * Nomes de Mock e o atributo *name*

        * Anexando Mocks como Atributos

      * Os criadores de patches

        * patch

        * patch.object

        * patch.dict

        * patch.multiple

        * métodos do patch: *start* e *stop*

        * patch de embutidos

        * TEST_PREFIX

        * Aninhando Decoradores Patch

        * Onde fazer patch

        * Patching Descriptors and Proxy Objects

      * MagicMock and magic method support

        * Simulando Métodos Mágicos

        * Magic Mock

      * Ajudantes

        * sentinel

        * DEFAULT

        * chamada

        * create_autospec

        * ANY

        * FILTER_DIR

        * mock_open

        * Especificação automática

        * Vedando mocks

      * Order of precedence of "side_effect", "return_value" and
        *wraps*

    * "unittest.mock" --- primeiros passos

      * Usando Mock

        * Mock patching methods

        * Mock for method calls on an object

        * Mocking classes

        * Nomeando os mocks

        * Tracking all calls

        * Setting return values and attributes

        * Raising exceptions with mocks

        * Side effect functions and iterables

        * Mocking asynchronous iterators

        * Mocking asynchronous context manager

        * Creating a mock from an existing object

        * Using side_effect to return per file content

      * Patch decorators

      * Further examples

        * Mocking chained calls

        * Partial mocking

        * Mocking a generator method

        * Applying the same patch to every test method

        * Mocking unbound methods

        * Checking multiple calls with mock

        * Coping with mutable arguments

        * Nesting patches

        * Mocking a dictionary with MagicMock

        * Mock subclasses and their attributes

        * Mocking imports with patch.dict

        * Tracking order of calls and less verbose call assertions

        * More complex argument matching

    * "test" --- Pacote de Testes de Regressão do Python

      * Writing Unit Tests for the "test" package

      * Executando testes usando a interface de linha de comando

    * "test.support" --- Utilities for the Python test suite

    * "test.support.socket_helper" --- Utilities for socket tests

    * "test.support.script_helper" --- Utilities for the Python
      execution tests

    * "test.support.bytecode_helper" --- Support tools for testing
      correct bytecode generation

    * "test.support.threading_helper" --- Utilities for threading
      tests

    * "test.support.os_helper" --- Utilities for os tests

    * "test.support.import_helper" --- Utilities for import tests

    * "test.support.warnings_helper" --- Utilities for warnings tests

  * Depuração e perfilamento

    * Tabela de eventos de auditoria

    * "bdb" --- Framework do depurador

    * "faulthandler" --- Dump the Python traceback

      * Dumping the traceback

      * Dumping the C stack

        * C Stack Compatibility

      * Fault handler state

      * Dumping the tracebacks after a timeout

      * Dumping the traceback on a user signal

      * Issue with file descriptors

      * Exemplo

    * "pdb" --- O depurador do Python

      * Interface de linha de comando

      * Comandos de depuração

    * "profiling" --- Python profilers

      * Introduction to profiling

      * Choosing a profiler

        * When to use statistical sampling

        * When to use deterministic tracing

      * Quick start

        * Statistical profiling

        * Deterministic profiling

      * Understanding profile output

      * Legacy compatibility

        * "profiling.tracing" --- Deterministic profiler

          * What is deterministic profiling?

          * Command-line interface

          * Programmatic usage examples

            * Basic profiling

            * Using the "Profile" class

          * Module reference

          * Using a custom timer

          * Limitations

        * "profiling.sampling" --- Statistical profiler

          * What is statistical profiling?

            * How time is estimated

            * When to use a different approach

          * Quick examples

          * Commands

            * The "run" command

            * The "attach" command

            * The "dump" command

            * The "replay" command

            * Profiling in production

            * Platform requirements

            * Version compatibility

          * Sampling configuration

            * Sampling rate and duration

            * Thread selection

            * Blocking mode

            * Special frames

            * Opcode-aware profiling

            * Real-time statistics

            * Subprocess profiling

            * Sampling efficiency

          * Profiling modes

            * Wall-clock mode

            * CPU mode

            * Comparing wall-clock and CPU profiles

            * GIL mode

            * Exception mode

          * Output formats

            * pstats format

            * Collapsed stacks format

            * Flame graph format

              * Differential flame graphs

            * Gecko format

            * Heatmap format

            * Binary format

          * Record and replay workflow

          * Live mode

            * Keyboard commands

          * Async-aware profiling

            * Async modes

            * Task markers and stack reconstruction

            * Option restrictions

          * Command-line interface

            * Global options

            * Dump options

            * Sampling options

            * Mode options

            * Output options

            * pstats display options

            * Run command options

    * "pstats" --- Statistics for profilers

      * Reading and displaying profile data

        * Working with statistics

        * Filtering output

        * Analyzing call relationships

        * Combining multiple profiles

      * The "Stats" class

      * Interface de linha de comando

    * "timeit" --- Mede o tempo de execução de pequenos trechos de
      código

      * Basic examples

      * Python interface

      * Interface de linha de comando

      * Exemplos

    * "trace" --- Rastreia ou acompanha a execução de instruções
      Python

      * Uso na linha de comando

        * Opções principais

        * Modificadores

        * Filtros

      * Interface programática

    * "tracemalloc" --- Trace memory allocations

      * Exemplos

        * Exibe o top 10

        * Compute differences

        * Get the traceback of a memory block

        * Pretty top

          * Record the current and peak size of all traced memory
            blocks

      * API

        * Funções

        * DomainFilter

        * Filter

        * Frame

        * Snapshot

        * Statistic

        * StatisticDiff

        * Trace

        * Traceback

  * Empacotamento e Distribuição de Software

    * "ensurepip" --- Inicialização do instalador do "pip"

      * Interface de linha de comando

      * API do módulo

    * "venv" --- Criação de ambientes virtuais

      * Criando ambientes virtuais

      * Como funcionam os venvs

      * API

      * Um exemplo de extensão de "EnvBuilder"

    * "zipapp" --- Gerencia arquivos zip executáveis do Python

      * Exemplo básico

      * Interface de linha de comando

      * API do Python

      * Exemplos

      * Especificando o interpretador

      * Criando aplicações autônomas com zipapp

        * Advertência

      * O formato de arquivo da aplicação zip Python

  * Serviços de Tempo de Execução Python

    * "sys" --- Parâmetros e funções específicas do sistema

    * "sys.monitoring" --- Monitoramento de eventos de execução

      * Identificadores de ferramenta

        * Registro e uso de ferramentas

      * Eventos

        * Eventos locais

        * Evento descontinuado

        * Eventos auxiliares

        * Outros eventos

        * O evento STOP_ITERATION

      * Ativação e desativação de eventos

        * Definir eventos globalmente

        * Eventos por objeto código

        * Desativação de eventos

      * Registro de funções de retorno de chamada

        * Argumentos da função de retorno de chamada

    * "sysconfig" --- Fornece acesso às informações de configuração do
      Python

      * Variáveis de configuração

      * Caminhos de instalação

      * Esquema de usuário

        * "posix_user"

        * "nt_user"

        * "osx_framework_user"

      * Esquema de home

        * "posix_home"

      * Esquema de prefixo

        * "posix_prefix"

        * "nt"

      * Funções de caminho de instalação

      * Outras funções

      * Uso na linha de comando

    * "builtins" --- Objetos embutidos

    * "__main__" --- Ambiente de código principal

      * "__name__ == '__main__'"

        * O que é o "ambiente de código principal"?

        * Uso idiomático

        * Considerações sobre pacotes

      * "__main__.py" em pacotes Python

        * Uso idiomático

      * "import __main__"

    * "warnings" --- Controle de avisos

      * Categorias de avisos

      * O filtro de avisos

        * Critérios de supressão de avisos repetidos

        * Descrevendo filtros de aviso

        * Filtro de avisos padrão

        * Overriding the default filter

      * Temporarily Suppressing Warnings

      * Testing Warnings

      * Updating Code For New Versions of Dependencies

      * Funções disponíveis

      * Gerenciadores de contexto disponíveis

      * Concurrent safety of Context Managers

    * "dataclasses" --- Data Classes

      * Conteúdo do módulo

      * Processamento pós-inicialização

      * Variáveis de classe

      * Variáveis de inicialização apenas

      * Frozen instances

      * Herança

      * Re-ordering of keyword-only parameters in "__init__()"

      * Funções padrão de fábrica

      * Valores padrão mutáveis

      * Descriptor-typed fields

    * "contextlib" --- Utilitários para contextos da instrução "with"

      * Utilitários

      * Exemplos e receitas

        * Supporting a variable number of context managers

        * Catching exceptions from "__enter__" methods

        * Cleaning up in an "__enter__" implementation

        * Replacing any use of "try-finally" and flag variables

        * Using a context manager as a function decorator

      * Single use, reusable and reentrant context managers

        * Reentrant context managers

        * Gerenciadores de contexto reutilizáveis

    * "abc" --- Classes base abstratas

    * "atexit" --- Manipuladores de saída

      * "atexit" Example

    * "traceback" --- Imprime ou recupera um traceback da pilha

      * Funções de nível de módulo

      * "TracebackException" Objects

      * "StackSummary" Objects

      * "FrameSummary" Objects

      * Examples of Using the Module-Level Functions

      * Examples of Using "TracebackException"

    * "__future__" --- Definições de instruções future

      * Conteúdo do módulo

    * "gc" --- Interface para o coletor de lixo

    * "inspect" --- Inspecione objetos vivos

      * Tipos e membros

      * Retrieving source code

      * Introspecting callables with the Signature object

      * Classes e funções

      * A pilha to interpretador

      * Fetching attributes statically

      * Current State of Generators, Coroutines, and Asynchronous
        Generators

      * Code Objects Bit Flags

      * Buffer flags

      * Interface de linha de comando

    * "annotationlib" --- Funcionalidade para introspecção de
      anotações

      * Semânticas de anotação

      * Classes

      * Funções

      * Receitas

        * Usando anotações em uma metaclasse

        * Creating a custom callable annotate function

      * Limitações do formato "STRING"

      * Limitações do formato "FORWARDREF"

      * Implicações de segurança de anotações de introspecção

    * "site" --- Gancho de configuração específico do site

      * Path extensions (".pth" files)

      * Startup entry points (".start" files)

      * Startup file examples

      * Migrating from "import" lines in ".pth" files to ".start"
        files

      * "sitecustomize"

      * "usercustomize"

      * Configuração Readline

      * Conteúdo do módulo

      * Interface de linha de comando

  * Interpretadores Python Personalizados

    * "code" --- Classes bases do interpretador

      * Objetos de interpretador interativo

      * Objetos de console Interativo

    * "codeop" --- Compila código Python

  * Importando módulos

    * "zipimport" - Importa módulos de arquivos Zip

      * Objetos zipimporter

      * Exemplos

    * "pkgutil" --- Utilitário de extensão de pacote

    * "modulefinder" --- Procura módulos usados por um script

      * Exemplo de uso de "ModuleFinder"

    * "runpy" --- Localizando e executando módulos Python

    * "importlib" --- A implementação de "import"

      * Introdução

      * Funções

      * "importlib.abc" -- Abstract base classes related to import

      * "importlib.machinery" -- Importers and path hooks

      * "importlib.util" -- Utility code for importers

      * Exemplos

        * Importing programmatically

        * Checando se o módulo pode ser importado

        * Importa o arquivo de origem diretamente

        * Implementing lazy imports

        * Setting up an importer

        * Approximating "importlib.import_module()"

    * "importlib.resources" -- Leitura, abertura e acesso a recursos
      de pacotes

      * API funcional

    * "importlib.resources.abc" -- Classes base abstratas para
      recursos

    * "importlib.metadata" -- Acessando metadados do pacote

      * Visão Geral

      * API funcional

        * Pontos de entrada

        * Metadados de distribuição

        * Versões de distribuição

        * Arquivos de distribuição

        * Requisitos de distribuição

        * Mapeando importação pra pacotes de distribuição

      * Distribuições

      * Descoberta de distribuição

      * Implementando provedores personalizados

        * Exemplo

    * A inicialização do caminho de pesquisa de módulos "sys.path"

      * Ambientes virtuais

      * Arquivos _pth

      * Python embarcado

  * Serviços da Linguagem Python

    * "ast" --- Árvores de sintaxe abstrata

      * Gramática abstrata

      * Classes de nós

        * Nós raízes

        * Literais

        * Variáveis

        * Expressões

          * Subscrição

          * Compreensões

        * Instruções

          * Importações

        * Fluxo de controle

        * Correspondência de padrões

        * Anotações de tipos

        * Parâmetros de tipo

        * Definições de função e classe

        * Async e await

      * Auxiliares de "ast"

      * Sinalizadores do compilador

      * Uso na linha de comando

    * "symtable" --- Acesso a tabela de símbolos do compilador

      * Generating Symbol Tables

      * Examining Symbol Tables

      * Uso na linha de comando

    * "token" --- Constantes usadas com árvores de análises do Python

    * "keyword" --- Testando palavras reservadas do Python

    * "tokenize" --- Tokenizador para código-fonte Python

      * Tokenizing input

      * Uso na linha de comando

      * Exemplos

    * "tabnanny" --- Detecção de indentação ambígua

    * "pyclbr" --- Suporte a navegador de módulos do Python

      * Objetos Function

      * Objetos Class

    * "py_compile" --- Compila arquivos fonte do Python

      * Interface de Linha de Comando

    * "compileall" --- Compilar bibliotecas do Python para bytecode

      * Uso na linha de comando

      * Funções públicas

    * "dis" --- Disassembler de bytecode do Python

      * Interface de linha de comando

      * Análise de bytecode

      * Funções de análise

      * Instruções em bytecode do Python

      * Opcode collections

    * "pickletools" --- Ferramentas para desenvolvedores pickle

      * Uso na linha de comando

        * Opções de linha de comando

      * Interface programática

  * Serviços Específicos do MS Windows

    * "msvcrt" --- Rotinas úteis do runtime MS VC++

      * Operações com arquivos

      * E/S de console

      * Outras funções

    * "winreg" --- Acesso aos registros do Windows

      * Funções

      * Constantes

        * Constantes HKEY_*

        * Direitos de acesso

          * Específico de 64 bits

        * Tipos de valores

      * Objetos identificador de registro

    * "winsound" --- Interface de reprodução de som para o Windows

      * Funções

      * Constantes

  * Serviços específicos do Unix

    * "shlex" --- Simple lexical analysis

      * shlex Objects

      * Regras de análise

      * Improved Compatibility with Shells

    * "posix" --- As chamadas de sistema mais comuns do POSIX

      * Suporte a arquivos grandes

      * Conteúdo notável do módulo

    * "pwd" --- A senha do banco de dados

    * "grp" --- O banco de dados de grupos

    * "termios" --- Controle de tty no estilo POSIX

      * Exemplo

    * "tty" --- Funções de controle de terminal

    * "pty" --- Utilitários de pseudoterminal

      * Exemplo

    * "fcntl" --- as chamadas de sistema "fcntl" e "ioctl"

    * "resource" --- Informação de uso de recursos

      * Limites de recursos

      * Uso de recursos

    * "syslog" --- Rotinas da biblioteca syslog do Unix

      * Exemplos

        * Exemplo simples

  * Interface de linha de comando (CLI) de módulos

  * Módulos substituídos

    * "getopt" --- Analisador sintático no estilo C para opções de
      linha de comando

    * "profile" --- Pure Python profiler

      * Migration

      * "profile" and "profiling.tracing" module reference

      * Differences from "profiling.tracing"

      * What is deterministic profiling?

      * Limitações

      * Calibration

      * Using a custom timer

  * Módulos removidos

  * Considerações de segurança

* Estendendo e incorporando o interpretador Python

  * Ferramentas de terceiros recomendadas

  * Tutorial da API C

  * Guias para tópicos intermediários

  * Incorporando o tempo de execução do CPython em uma aplicação maior

* Manual de referência da API C/Python

  * Introdução

    * Compatibilidade com a versão da linguagem

    * Padrões de codificação

    * Arquivos de inclusão

      * System includes

    * Macros úteis

      * Docstring macros

      * General utility macros

        * Numeric utilities

        * Assertion utilities

        * Type size utilities

        * Macro definition utilities

      * Declaration utilities

      * Outdated macros

    * Objetos, tipos e contagens de referências

      * Contagens de referências

        * Detalhes da contagem de referências

      * Tipos

    * Exceções

    * Incorporando Python

    * Compilações de depuração

    * Ferramentas de terceiros recomendadas

  * C API and ABI Stability

    * API C Instável

    * Stable Application Binary Interfaces

      * Compiling for Stable ABI

      * Stable ABI Scope and Performance

      * Stable ABI Caveats

    * Considerações da plataforma

    * ABI Checking

    * Conteúdo da API Limitada

  * A camada de nível muito alto

    * Símbolos iniciais disponíveis

    * Stack Effects

  * Contagem de referências

  * Tratamento de exceções

    * Impressão e limpeza

    * Levantando exceções

    * Emitindo avisos

    * Consultando o indicador de erro

    * Tratamento de sinal

    * Classes de exceção

    * Objeto Exceção

    * Objetos de exceção Unicode

    * Controle de recursão

    * Exception and warning types

      * Tipos de exceção

      * OSError aliases

      * Warning types

    * Tracebacks

  * Definindo módulos de extensão

    * Extension export hook

    * Inicialização multifásica

    * Várias instâncias de módulo

    * "PyInit" function

      * Inicialização monofásica legada

  * Slots de definição

    * Macros de conveniência

    * IDs de slot comuns

  * Utilitários

    * Utilitários do sistema operacional

    * Funções de sistema

    * Controle de processos

    * Importando módulos

    * Suporte a *marshalling* de dados

    * Análise de argumentos e construção de valores

      * Análise de argumentos

        * Strings e buffers

        * Números

        * Outros objetos

        * Funções da API

      * Construindo valores

    * Conversão e formação de strings

    * Classificação e conversão de caracteres

      * Bit masks

    * API do PyHash

    * Reflexão

    * Registro de codec e funções de suporte

      * API de pesquisa de codec

      * API de registro de tratamentos de erros de decodificação
        Unicode

      * Variáveis utilitárias de codec

    * API C PyTime

      * Tipos

      * Funções de relógio

      * Funções de relógio brutas

      * Funções de conversão

    * Suporte a Mapas do Perf

    * API C do Expat

  * Camada de Objetos Abstratos

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

  * Camada de Objetos Concretos

    * Objetos Fundamentais

      * Objetos tipo

        * Creating Heap-Allocated Types

          * Type slot IDs

        * Soft-deprecated API

      * O Objeto "None"

    * Objetos Numéricos

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

    * Objetos Sequência

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

    * Coleções

      * Dictionary objects

        * Objetos de visão de dicionário

        * Frozen dictionary objects

        * Ordered dictionaries

      * Objeto Set

        * Deprecated API

    * Objetos Função

      * Objetos Função

      * Objetos de Método de Instância

      * Objetos método

      * Objeto célula

      * Objetos código

      * Sinalizadores de objetos código

      * Informação adicional

    * Outros Objetos

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

    * API C para módulos de extensão

      * API C de curses

      * Dados internos

      * Objetos DateTime

      * Dados internos

  * Interpreter initialization and finalization

    * Before Python initialization

    * Variáveis de configuração global

    * Inicializando e encerrando o interpretador

    * Cautions regarding interpreter finalization

    * Interpreter views

    * Parâmetros de todo o processo

  * Thread states and the global interpreter lock

    * Desvinculação do estado de thread do código de extensão

      * APIs

    * Using the C API from foreign threads

      * Reusing a thread state across repeated calls

      * Attaching/detaching thread states

    * GIL-state APIs

    * Cuidados com o uso de fork()

    * APIs de alto nível

    * APIs de baixo nível

  * Asynchronous notifications

  * Operating system thread APIs

  * Primitivas de sincronização

    * Python critical section API

      * Low-level critical section API

    * Legacy locking APIs

  * Thread-local storage support

    * Thread-specific storage API

    * Dynamic allocation

    * Métodos

    * Legacy APIs

  * Multiple interpreters in a Python process

    * A per-interpreter GIL

    * Bugs and caveats

    * APIs de alto nível

    * APIs de baixo nível

    * Advanced debugger support

  * Profiling and tracing

  * Reference tracing

  * Performance statistics

  * Configuração de inicialização do Python

    * API C PyInitConfig

      * Exemplo

      * Criar configuração

      * Tratamento de erros

      * Opções de get

      * Opções de set

      * Módulo

      * Inicializar o Python

    * Opções de configuração

    * API de configuração Python em tempo de execução

    * API C PyConfig

      * Exemplo

      * PyWideStringList

      * PyStatus

      * PyPreConfig

      * Pré-inicializar Python com PyPreConfig

      * PyConfig

      * Initialization with PyConfig

      * Isolated Configuration

      * Configuração do Python

      * Python Path Configuration

    * Py_GetArgcArgv()

    * Multi-Phase Initialization Private Provisional API

  * Gerenciamento de Memória

    * Visão Geral

    * Allocator Domains

    * Raw Memory Interface

    * Interface da Memória

      * Apelidos descontinuados

    * Alocadores de objeto

    * Alocadores de memória padrão

    * Alocadores de memória

    * Debug hooks on the Python memory allocators

    * The pymalloc allocator

      * Customize pymalloc Arena Allocator

    * The mimalloc allocator

    * tracemalloc C API

    * Exemplos

  * Suporte a implementação de Objetos

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

  * API e Versionamento de ABI

    * Constantes de versão de tempo de construção

    * Versão de tempo de execução

    * Macros de empacotamento de bits

  * API C de monitoramento

  * Gerando eventos de execução

    * Gerenciando o Estado de um Monitoramento

* Instalando módulos Python

  * Termos chave

  * Uso básico

  * Como eu ...?

    * ... instalo pacotes apenas para o usuário atual?

    * ... instalo pacotes científicos do Python?

    * ... trabalho com várias versões do Python instaladas em
      paralelo?

  * Problemas comuns de instalação

    * Instalando no sistema Python no Linux

    * Pip não instalado

    * Instalando extensões binárias

* Python HOWTOs

* Perguntas Frequentes Sobre Python

  * Python Geral

    * Informações gerais

    * Python no mundo real

  * FAQ sobre programação

    * General questions

    * Core language

    * Números e strings

    * Desempenho

    * Sequences (tuples/lists)

    * Objetos

    * Módulos

  * FAQ sobre design e histórico

    * Por que o Python usa indentação para agrupamento de instruções?

    * Por que eu estou recebendo resultados estranhos com simples
      operações aritméticas?

    * Por que o cálculo de pontos flutuantes são tão imprecisos?

    * Por que strings do Python são imutáveis?

    * Por que o 'self' deve ser usado explicitamente em definições de
      método e chamadas?

    * Por que não posso usar uma atribuição em uma expressão?

    * Por que o Python usa métodos para algumas funcionalidades (ex:
      lista.index()) mas funções para outras (ex: len(lista))?

    * Por que o join() é um método de string em vez de ser um método
      de lista ou tupla?

    * Quão rápidas são as exceções?

    * Por que não existe uma instrução de switch ou case no Python?

    * Você não pode emular threads no interpretador em vez de confiar
      em uma implementação de thread específica do sistema
      operacional?

    * Por que expressões lambda não podem conter instruções?

    * O Python pode ser compilado para linguagem de máquina, C ou
      alguma outra linguagem?

    * Como o Python gerencia memória?

    * Por que o CPython não usa uma forma mais tradicional de esquema
      de coleta de lixo?

    * Por que toda memória não é liberada quando o CPython fecha?

    * Por que existem tipos de dados separados para tuplas e listas?

    * Como as listas são implementadas no CPython?

    * Como são os dicionários implementados no CPython?

    * Por que chaves de dicionário devem ser imutáveis?

    * Por que lista.sort() não retorna a lista ordenada?

    * Como você especifica e aplica um spec de interface no Python?

    * Por que não há goto?

    * Por que strings brutas (r-strings) não podem terminar com uma
      contrabarra?

    * Por que o Python não tem uma instrução "with" para atribuição de
      atributos?

    * Por que os geradores não suportam a instrução with?

    * Por que dois pontos são necessários para as instruções de
      if/while/def/class?

    * Por que o Python permite vírgulas ao final de listas e tuplas?

  * FAQ de Bibliotecas e Extensões

    * Questões gerais sobre bibliotecas

    * Tarefas comuns

    * Threads

    * Entrada e Saída

    * Programação Rede / Internet

    * Base de Dados

    * Matemáticos e Numéricos

  * FAQ sobre Extensão/Incorporação

    * Posso criar minhas próprias funções em C?

    * Posso criar minhas próprias funções em C++?

    * Escrever C é difícil; há alguma alternativa?

    * Como posso executar instruções arbitrárias de Python a partir de
      C?

    * Como posso executar e obter o resultado de uma expressão Python
      arbitrária a partir de C?

    * Como extraio valores em C a partir de um objeto Python?

    * Como posso utilizar Py_BuildValue() para criar uma tupla de
      comprimento arbitrário?

    * Como eu chamo um método de um objeto a partir do C?

    * Como posso capturar a saída da função PyErr_Print() (ou qualquer
      outra coisa que escreva para stdout/stderr)?

    * Como faço para acessar a partir do C um módulo escrito em
      Python?

    * Como posso interagir com objetos C++ a partir do Python?

    * Adicionei um módulo usando o arquivo de Setup e o make falha;
      por quê?

    * Como eu depuro uma extensão?

    * Quero compilar um módulo Python no meu sistema Linux, mas alguns
      arquivos estão faltando. Por quê?

    * Como posso distinguir "entrada incompleta" de "entrada
      inválida"?

    * Como encontro os símbolos __builtin_new ou __pure_virtual não-
      definidos no g++?

    * Posso criar uma classe de objetos com alguns métodos
      implementados em C e outros em Python (por exemplo, via
      herança)?

  * Python no Windows

    * Como faço para executar um programa Python no Windows?

    * Como eu faço para criar programas Python executáveis?

    * Por que Python às vezes demora tanto para iniciar?

    * Como eu faço para criar um executável a partir de um código
      Python?

    * Um arquivo "*.pyd" é o mesmo que um DLL?

    * Como eu posso embutir Python dentro de uma aplicação do Windows?

    * Como eu impeço editores de adicionarem tabulações na minha
      source do Python?

    * Como faço para verificar uma tecla pressionada sem bloquear?

    * Como resolvo o erro da api-ms-win-crt-runtime-l1-1-0.dll
      ausente?

  * FAQ da Interface Gráfica do Usuário

    * Perguntas Gerais sobre a GUI

    * Quais toolkits de GUI existem para o Python?

    * Perguntas do Tkinter

  * FAD de "Por que o Python está instalado em meu computador?"

    * O que é Python?

    * Porque Python está instalado em minha máquina?

    * Eu posso apagar o Python?

* Descontinuações

  * Remoção pendente no Python 3.16

  * Remoção pendente no Python 3.17

  * Remoção pendente no Python 3.18

  * Remoção pendente no Python 3.19

  * Remoção pendente no Python 3.20

  * Remoção pendente em versões futuras

  * descontinuações suave

  * Descontinuações na API C

    * Remoção pendente no Python 3.15

    * Remoção pendente no Python 3.16

    * Remoção pendente no Python 3.18

    * Remoção pendente no Python 3.19

    * Remoção pendente no Python 3.20

    * Remoção pendente em versões futuras

* Glossário

* Sobre esta documentação

  * Contribuidores da documentação do Python

* Lidando com bugs

  * Bugs na documentação

  * Usando o rastreador de problemas do Python

  * Começando a contribuir com o Python por conta própria

* Direitos autorais

* História e Licença

  * História do software

  * Termos e condições para acessar ou usar Python

    * PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2

    * ACORDO DE LICENCIAMENTO DA BEOPEN.COM PARA PYTHON 2.0

    * CONTRATO DE LICENÇA DA CNRI PARA O PYTHON 1.6.1

    * ACORDO DE LICENÇA DA CWI PARA PYTHON 0.9.0 A 1.2

    * ZERO-CLAUSE BSD LICENSE FOR CODE IN THE PYTHON DOCUMENTATION

  * Licenças e Reconhecimentos para Software Incorporado

    * Mersenne Twister

    * Soquetes

    * Serviços de soquete assíncrono

    * Gerenciamento de cookies

    * Rastreamento de execução

    * Funções UUencode e UUdecode

    * Chamadas de procedimento remoto XML

    * test_epoll

    * kqueue de seleção

    * SipHash24

    * strtod e dtoa

    * OpenSSL

    * expat

    * libffi

    * zlib

    * cfuhash

    * libmpdec

    * Conjunto de testes C14N do W3C

    * mimalloc

    * asyncio

    * Global Unbounded Sequences (GUS)

    * Ligações Zstandard

    * Módulo de perfilamento

    * Pacotes Pixi

    * Banco de dados de caracteres Unicode
