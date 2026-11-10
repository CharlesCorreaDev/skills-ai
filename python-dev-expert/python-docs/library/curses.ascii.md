"curses.ascii" --- Utilitários para caracteres ASCII
****************************************************

**Código-fonte:** Lib/curses/ascii.py

======================================================================

The "curses.ascii" module supplies name constants for ASCII characters
and functions to test membership in various ASCII character classes.
The constants supplied are names for control characters as follows:

+-----------------+------------------------------------------------+
| Nome            | Significado                                    |
|=================|================================================|
| curses.ascii.N  |                                                |
| UL              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.S  | Início do cabeçalho, interrupção do console    |
| OH              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.S  | Início de texto                                |
| TX              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.E  | Fim de texto                                   |
| TX              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.E  | Fim de transmissão                             |
| OT              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.E  | Consulta, segue com controle de fluxo "ACK"    |
| NQ              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.A  | Confirmação                                    |
| CK              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.B  | Campainha                                      |
| EL              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.BS | Backspace                                      |
+-----------------+------------------------------------------------+
| curses.ascii.T  | Tabulação                                      |
| AB              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.HT | Apelido para "TAB": "Tabulação horizontal"     |
+-----------------+------------------------------------------------+
| curses.ascii.LF | Alimentação de linha ou *line feed*            |
+-----------------+------------------------------------------------+
| curses.ascii.NL | Apelido para "LF": "Nova linha"                |
+-----------------+------------------------------------------------+
| curses.ascii.VT | Tabulação vertical                             |
+-----------------+------------------------------------------------+
| curses.ascii.FF | Alimentação de formulário ou *form feed*       |
+-----------------+------------------------------------------------+
| curses.ascii.CR | Retorno de carro ou *carriage return*          |
+-----------------+------------------------------------------------+
| curses.ascii.SO | Deslocamento para fora ou *shift-out*, inicia  |
|                 | um conjunto de caracteres alternativo          |
+-----------------+------------------------------------------------+
| curses.ascii.SI | Deslocamento para dentro ou *shift-in*, retoma |
|                 | o conjunto de caracteres padrão                |
+-----------------+------------------------------------------------+
| curses.ascii.D  | Escape de conexão ou *data-link escape*        |
| LE              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.D  | XON, para controle de fluxo                    |
| C1              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.D  | Controle de dispositivo 2, control de fluxo em |
| C2              | modo bloco                                     |
+-----------------+------------------------------------------------+
| curses.ascii.D  | XOFF, para controle de fluxo                   |
| C3              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.D  | Controle de dispositivo 4                      |
| C4              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.N  | Confirmação negativa                           |
| AK              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.S  | Estado ocioso síncrono                         |
| YN              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.E  | Bloco de fim de transmissão                    |
| TB              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.C  | Cancelar                                       |
| AN              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.EM | Fim de mídia                                   |
+-----------------+------------------------------------------------+
| curses.ascii.S  | Substituir                                     |
| UB              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.E  | Escapar                                        |
| SC              |                                                |
+-----------------+------------------------------------------------+
| curses.ascii.FS | Separador de arquivos                          |
+-----------------+------------------------------------------------+
| curses.ascii.GS | Separador de grupos                            |
+-----------------+------------------------------------------------+
| curses.ascii.RS | Separador de registros, terminador de modo     |
|                 | bloco                                          |
+-----------------+------------------------------------------------+
| curses.ascii.US | Separador de unidades                          |
+-----------------+------------------------------------------------+
| curses.ascii.SP | Espaço                                         |
+-----------------+------------------------------------------------+
| curses.ascii.D  | Excluir                                        |
| EL              |                                                |
+-----------------+------------------------------------------------+

Note que muitos deles têm pouca significância prática no uso moderno.
Os mnemônicos derivam de convenções de teleimpressoras que antecedem
os computadores digitais.

O módulo fornece as seguintes funções, baseadas nas da biblioteca C
padrão:

curses.ascii.isalnum(c)

   Verifica se há um caractere alfanumérico ASCII; equivale a
   "isalpha(c) or isdigit(c)".

curses.ascii.isalpha(c)

   Verifica se há um caractere alfabético ASCII; equivale a
   "isupper(c) or islower(c)".

curses.ascii.isascii(c)

   Verifica se há um valor de caractere que se encaixa no conjunto
   ASCII de 7 bits.

curses.ascii.isblank(c)

   Checks for an ASCII blank character; space or horizontal tab.

curses.ascii.iscntrl(c)

   Verifica se há um caractere de controle ASCII (no intervalo de 0x00
   a 0x1f ou 0x7f).

curses.ascii.isdigit(c)

   Verifica se há um dígito decimal ASCII, "'0'" a "'9'". Isso
   equivale a "c in string.digits".

curses.ascii.isgraph(c)

   Checks for any ASCII printable character except space.

curses.ascii.islower(c)

   Verifica se há um caractere ASCII minúsculo.

curses.ascii.isprint(c)

   Verifica se há algum caractere ASCII imprimível, incluindo espaço.

curses.ascii.ispunct(c)

   Checks for any ASCII printable character which is not a space or an
   alphanumeric character.

curses.ascii.isspace(c)

   Verifica caracteres de espaço em branco ASCII; espaço, quebra de
   linha, retorno de carro, quebra de página, tabulação horizontal,
   tabulação vertical.

curses.ascii.isupper(c)

   Verifica se há uma letra maiúscula ASCII.

curses.ascii.isxdigit(c)

   Verifica se há um dígito hexadecimal ASCII. Isso equivale a "c in
   string.hexdigits".

curses.ascii.isctrl(c)

   Checks for an ASCII control character (ordinal values 0 to 31).
   Unlike "iscntrl()", this does not include the delete character
   (0x7f).

curses.ascii.ismeta(c)

   Verifica se há um caractere não ASCII (valores ordinais 0x80 e
   acima).

Essas funções aceitam números inteiros ou strings de caracteres
únicos; quando o argumento é uma string, ele é primeiro convertido
usando a função embutida "ord()".

Observe que todas essas funções verificam valores de bits ordinais
derivados do caractere da string que você passa; elas não sabem nada
sobre a codificação de caracteres da máquina host.

As duas funções a seguir aceitam uma string de caractere único ou um
valor de byte inteiro; elas retornam um valor do mesmo tipo.

curses.ascii.ascii(c)

   Retorna o valor ASCII correspondente aos 7 bits mais baixos de *c*.

curses.ascii.ctrl(c)

   Retorna o caractere de controle correspondente ao caractere
   fornecido (é feito um E bit a bit com 0x1f sobre o valor do bit do
   caractere).

curses.ascii.alt(c)

   Retorna o caractere de 8 vits correspondente ao caractere ASCII
   fornecido (é feito um OU bit a bit com 0x80 sobre o valor do bit do
   caractere).

A função a seguir aceita uma string de um único caractere ou um valor
inteiro; ela retorna uma string.

curses.ascii.unctrl(c)

   Retorna uma representação de string do caractere ASCII *c*. Se *c*
   for imprimível, essa string é o próprio caractere. Se o caractere
   for um caractere de controle (0x00--0x1f), a string consiste em um
   acento circunflexo ("'^'") seguido pela letra maiúscula
   correspondente. Se o caractere for de exclusão ASCII (0x7f), a
   string é "'^?'". Se o caractere tiver seu metabit (0x80) definido,
   o metabit é removido, as regras precedentes são aplicadas e "'!'" é
   adicionado ao resultado.

curses.ascii.controlnames

   Um vetor de strings de 33 elementos que contém os mnemônicos ASCII
   para os trinta e dois caracteres de controle ASCII de 0 (NUL) a
   0x1f (US), em ordem, mais o mnemônico "SP" para o caractere de
   espaço.
