Interfaces gráficas de usuário com Tk
*************************************

Tk/Tcl tem sido parte integrante do Python. Ele fornece um kit de
ferramentas de janela robusto e independente de plataforma, que está
disponível para programadores Python usando o pacote "tkinter" e sua
extensão, o módulo "tkinter.ttk".

O pacote "tkinter" é uma fina camada orientada a objetos no topo do
Tcl/Tk. Para usar "tkinter", você não precisa escrever o código Tcl,
mas precisará consultar a documentação do Tk e, ocasionalmente, a
documentação do Tcl. "tkinter" é um conjunto de envólucros que
implementam os widgets Tk como classes Python.

As principais virtudes do "tkinter" são que ele é rápido, e que
geralmente vem junto com o Python. Embora sua documentação padrão seja
fraca, um bom material está disponível, que inclui: referências,
tutoriais, um livro e outros. "tkinter" também é famoso por ter uma
aparência desatualizada, que foi amplamente melhorada no Tk 8.5. No
entanto, existem muitas outras bibliotecas GUI nas quais você pode
estar interessado. A wiki do Python lista várias frameworks e
ferramentas GUI alternativas.

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
