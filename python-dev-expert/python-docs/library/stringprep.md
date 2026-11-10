"stringprep" --- Preparação de string para internet
***************************************************

**Código-fonte:** Lib/stringprep.py

======================================================================

Ao identificar coisas (como nomes de host) na internet, muitas vezes é
necessário comparar tais identificações para "igualdade". Exatamente
como essa comparação é executada pode depender do domínio da
aplicação, por exemplo, se deve ser insensível a maiúsculas e
minúsculas ou não. Também pode ser necessário restringir as possíveis
identificações, para permitir apenas identificações consistindo de
caracteres "imprimíveis".

**RFC 3454** define um procedimento para "preparar" strings Unicode em
protocolos de internet. Antes de passar strings para o fio, elas são
processadas com o procedimento de preparação, após o qual elas têm uma
certa forma normalizada. O RFC define um conjunto de tabelas, que
podem ser combinadas em perfis. Cada perfil deve definir quais tabelas
ele usa, e quais outras partes opcionais do procedimento "stringprep"
são parte do perfil. Um exemplo de um perfil "stringprep" é
"nameprep", que é usado para nomes de domínio internacionalizados.

O módulo "stringprep" expõe apenas as tabelas do **RFC 3454**. Como
essas tabelas seriam muito grandes para representar como dicionários
ou listas, o módulo usa o banco de dados de caracteres Unicode
internamente. O código-fonte do módulo em si foi gerado usando o
utilitário "mkstringprep.py".

Como resultado, essas tabelas são expostas como funções, não como
estruturas de dados. Existem dois tipos de tabelas no RFC: conjuntos e
mapeamentos. Para um conjunto, "stringprep" fornece a "função
característica", ou seja, uma função que retorna "True" se o parâmetro
fizer parte do conjunto. Para mapeamentos, ele fornece a função de
mapeamento: dada a chave, ele retorna o valor associado. Abaixo está
uma lista de todas as funções disponíveis no módulo.

stringprep.in_table_a1(code)

   Determina se *code* está na tabela A.1 (pontos de código não
   atribuídos no Unicode 3.2).

stringprep.in_table_b1(code)

   Determina se *code* está na tabela B.1 (comumente mapeado para
   nada).

stringprep.map_table_b2(code)

   Retorna o valor mapeado para *code* de acordo com a tabela B.2
   (mapeamento para dobramento de casos usado com NFKC).

stringprep.map_table_b3(code)

   Retorna o valor mapeado para *code* de acordo com a tabela B.3
   (mapeamento para dobramento de casos usado com nenhuma
   normalização).

stringprep.in_table_c11(code)

   Determina se *code* está na tabela C.1.1 (caracteres de espaço
   ASCII).

stringprep.in_table_c12(code)

   Determina se *code* está na tabela C.1.2 (caracteres de espaço não-
   ASCII).

stringprep.in_table_c11_c12(code)

   Determina se *code* está na tabela C.1 (caracteres de espaço, união
   de C.1.1 e C.1.2).

stringprep.in_table_c21(code)

   Determina se *code* está na tabela C.2.1 (caracteres de controle
   ASCII).

stringprep.in_table_c22(code)

   Determina se *code* está na tabela C.2.2 (caracteres de controle
   não-ASCII).

stringprep.in_table_c21_c22(code)

   Determina se *code* está na tabela C.2 (caracteres de controle,
   união de C.2.1 e C.2.2).

stringprep.in_table_c3(code)

   Determina se *code* está na tabela C.3 (uso privado).

stringprep.in_table_c4(code)

   Determina se *code* está na tabela C.4 (pontos de código não-
   caracteres).

stringprep.in_table_c5(code)

   Determina se *code* está na tabela C.5 (códigos substitutos).

stringprep.in_table_c6(code)

   Determina se *code* está na tabela C.6 (inapropriado para texto
   simples).

stringprep.in_table_c7(code)

   Determina se *code* está na tabela C.7 (inapropriado para para
   representação canônica).

stringprep.in_table_c8(code)

   Determina se *code* está na tabela C.8 (alteram propriedades de
   exibição ou estão descontinuadas).

stringprep.in_table_c9(code)

   Determina se *code* está na tabela C.9 (caracteres de tag).

stringprep.in_table_d1(code)

   Determina se *code* está na tabela D.1 (Caracteres com propriedade
   bidirecional "R" ou "AL").

stringprep.in_table_d2(code)

   Determina se *code* está na tabela D.2 (Caracteres com propriedade
   bidirecional "L").
