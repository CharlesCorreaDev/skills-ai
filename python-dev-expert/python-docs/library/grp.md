"grp" --- O banco de dados de grupos
************************************

======================================================================

Este módulo fornece acesso ao banco de dados de grupos Unix. Ele está
disponível em todas as versões do Unix.

Disponibilidade: Unix, not WASI, not Android, not iOS.

As entradas do banco de dados de grupos são relatadas como um objeto
tupla ou similar, cujos atributos correspondem aos membros da
estrutura "group" (campo Atributo abaixo, consulte "<grp.h>"):

+---------+-------------+-----------------------------------+
| Índice  | Atributo    | Significado                       |
|=========|=============|===================================|
| 0       | gr_name     | o nome do grupo                   |
+---------+-------------+-----------------------------------+
| 1       | gr_passwd   | a senha do grupo (criptografada); |
|         |             | geralmente vazia                  |
+---------+-------------+-----------------------------------+
| 2       | gr_gid      | O ID numérico do grupo            |
+---------+-------------+-----------------------------------+
| 3       | gr_mem      | todos os nomes de usuários dos    |
|         |             | membros do grupo                  |
+---------+-------------+-----------------------------------+

O gid é um inteiro, nome e senha são strings, e a lista de membros é
uma lista de strings. (Observe que a maioria dos usuários não são
listados explicitamente como membros do grupo em que estão, de acordo
com o banco de dados de senhas. Verifique ambos os bancos de dados
para obter informações completas sobre associação. Observe também que
um "gr_name" que começa com "+" ou "-" provavelmente é uma referência
YP/NIS e pode não ser acessível via "getgrnam()" ou "getgrgid()".)

Isto define os seguintes itens

grp.getgrgid(id)

   Retorna a entrada do banco de dados de grupos para o ID do grupo
   numérico fornecido. "KeyError" é levantada se a entrada solicitada
   não puder ser encontrada.

   Alterado na versão 3.10: "TypeError" é levantada para argumentos
   não inteiros, como pontos flutuantes ou strings.

grp.getgrnam(name)

   Retorna a entrada do banco de dados de grupos para o nome do grupo
   fornecido. "KeyError" é levantada se a entrada solicitada não puder
   ser encontrada.

grp.getgrall()

   Retorna uma lista de todas as entradas de grupo disponíveis, em
   ordem arbitrária.

Ver também:

  Módulo "pwd"
     Uma interface para o banco de dados de usuários, semelhante a
     esta.
