"token" --- Constantes usadas com árvores de análises do Python
***************************************************************

**Código-fonte:** Lib/token.py

======================================================================

Este módulo fornece constantes que representam os valores numéricos
dos nós das folhas da árvore de análise (tokens terminais). Consulte o
arquivo "Grammar/Tokens" na distribuição Python para obter as
definições dos nomes no contexto da gramática da linguagem. Os valores
numéricos específicos para os quais os nomes são mapeados podem mudar
entre as versões do Python.

O módulo também fornece um mapeamento de códigos numéricos para nomes
e algumas funções. As funções espelham definições nos arquivos de
cabeçalho do Python C.

Observe que o valor de um token pode depender das opções do
tokenizador. Por exemplo, um token ""+"" pode ser relatado como "PLUS"
ou "OP", ou um token ""match"" pode ser "NAME" ou "SOFT_KEYWORD".

token.tok_name

   Dicionário que mapeia os valores numéricos das constantes definidas
   neste módulo de volta para cadeias de nomes, permitindo que seja
   gerada uma representação mais legível de árvores de análise.

token.ISTERMINAL(x)

   Retorna "True" para valores de tokens terminais.

token.ISNONTERMINAL(x)

   Retorna "True" para valores de tokens não terminais.

token.ISEOF(x)

   Retorna "True" se *x* for o marcador que indica o final da entrada.

Os constantes de tokens são:

token.NAME

   Valor de token que indica um literal ou palavra reservada

token.NUMBER

   Valor de token que indica um literal numérico

token.STRING

   Valor de token que indica um literal de string ou byte, excluindo
   literais de strings formatadas. A string de token não é
   interpretada: ela inclui as aspas ao redor e o prefixo (se
   fornecido); contrabarras são incluídas literalmente, sem processar
   sequências de escape.

token.OP

   Um valor de token genérico que indica um operador ou delimitador.

   Este valor é relatado apenas pelo módulo "tokenize". Internamente,
   o tokenizador usa tipos exatos de tokens em vez disso.

token.COMMENT

   Valor de token usado para indicar um comentário. O analisador
   sintático ignora tokens "COMMENT".

token.NEWLINE

   Valor de token que indica o fim de uma linha lógica.

token.NL

   Valor de token usado para indicar uma nova linha não terminante. Os
   tokens "NL" são gerados quando uma linha lógica de código é
   continuada em várias linhas físicas. O analisador sintático ignora
   os tokens "NL".

token.INDENT

   Valor de token usado no início de uma linha lógica para indicar o
   início de um bloco indentado.

token.DEDENT

   Valor de token usado no início de uma linha lógica para indicar o
   fim de um bloco indentado.

token.FSTRING_START

   Valor de token usado para indicar o início de um literal de
   f-string.

   A string de token inclui o prefixo e as aspas iniciais, mas nenhum
   conteúdo do literal.

token.FSTRING_MIDDLE

   Valor de token usado para texto literal dentro de um literal de
   f-string, incluindo especificações de formato.

   Campos de substituição (ou seja, as partes não literais de
   f-strings) usam os mesmos tokens que outras expressões e são
   delimitados pelos tokens "LBRACE", "RBRACE", "EXCLAMATION" e
   "COLON".

token.FSTRING_END

   Valor de token usado para indicar o fim de um literal de f-string.

   A string do token contém as aspas de fechamento.

token.TSTRING_START

   Valor de token usado para indicar o início de um literal de string
   template.

   A string de token inclui o prefixo e as aspas iniciais, mas nenhum
   conteúdo do literal.

   Adicionado na versão 3.14.

token.TSTRING_MIDDLE

   Valor de token usado para texto literal dentro de um literal de
   string template, incluindo especificações de formato.

   Campos de substituição (ou seja, as partes não literais de
   t-strings) usam os mesmos tokens que outras expressões e são
   delimitados pelos tokens "LBRACE", "RBRACE", "EXCLAMATION" e
   "COLON".

   Adicionado na versão 3.14.

token.TSTRING_END

   Valor de token usado para indicar o fim de um literal de string
   template.

   A string do token contém as aspas de fechamento.

   Adicionado na versão 3.14.

token.ENDMARKER

   Valor de token que indica o fim da entrada. Usado em regras de
   gramática de nível superior.

token.ENCODING

   Valor de token que indica a codificação usada para decodificar os
   bytes de origem em texto. O primeiro token retornado por
   "tokenize.tokenize()" sempre será um token "ENCODING".

   Este tipo de token não é usado pelo tokenizador do C, mas é
   necessário para o módulo "tokenize".

Os seguintes tipos de token não são produzidos pelo módulo "tokenize"
e são definidos para usos especiais no tokenizador ou analisador:

token.TYPE_IGNORE

   Valor de token indicando que um comentário "type: ignore" foi
   reconhecido. Tais tokens são produzidos em vez de tokens "COMMENT"
   regulares somente com o sinalizador "PyCF_TYPE_COMMENTS".

token.TYPE_COMMENT

   Valor de token indicando que um comentário de tipo foi reconhecido.
   Tais tokens são produzidos em vez de tokens "COMMENT" regulares
   somente com o sinalizador "PyCF_TYPE_COMMENTS".

token.SOFT_KEYWORD

   Valor de token indicando uma palavra reservada contextual.

   O tokenizador nunca produz esse valor. Para verificar uma palavra
   reservada contextual, passe uma string do token "NAME" para
   "keyword.issoftkeyword()".

token.ERRORTOKEN

   Valor de token usado para indicar uma entrada errada.

   O módulo "tokenize" geralmente indica erros levantando exceções em
   vez de emitir este token. Ele também pode emitir tokens como "OP"
   ou "NAME" com strings que são rejeitadas posteriormente pelo
   parser.

Os tokens restantes representam operadores e delimitadores
específicos. (O módulo "tokenize" os relata como "OP"; consulte
"exact_type" na documentação "tokenize" para obter detalhes.)

+----------------------------------------------------+----------------------------------------------------+
| Token                                              | Valor                                              |
|====================================================|====================================================|
| token.LPAR                                         | ""(""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.RPAR                                         | "")""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.LSQB                                         | ""[""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.RSQB                                         | ""]""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.COLON                                        | "":""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.COMMA                                        | "",""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.SEMI                                         | "";""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.PLUS                                         | ""+""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.MINUS                                        | ""-""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.STAR                                         | ""*""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.SLASH                                        | ""/""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.VBAR                                         | ""|""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.AMPER                                        | ""&""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.LESS                                         | ""<""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.GREATER                                      | "">""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.EQUAL                                        | ""=""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.DOT                                          | "".""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.PERCENT                                      | ""%""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.LBRACE                                       | ""{""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.RBRACE                                       | ""}""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.EQEQUAL                                      | ""==""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.NOTEQUAL                                     | ""!=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.LESSEQUAL                                    | ""<=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.GREATEREQUAL                                 | "">=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.TILDE                                        | ""~""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.CIRCUMFLEX                                   | ""^""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.LEFTSHIFT                                    | ""<<""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.RIGHTSHIFT                                   | "">>""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.DOUBLESTAR                                   | ""**""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.PLUSEQUAL                                    | ""+=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.MINEQUAL                                     | ""-=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.STAREQUAL                                    | ""*=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.SLASHEQUAL                                   | ""/=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.PERCENTEQUAL                                 | ""%=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.AMPEREQUAL                                   | ""&=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.VBAREQUAL                                    | ""|=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.CIRCUMFLEXEQUAL                              | ""^=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.LEFTSHIFTEQUAL                               | ""<<=""                                            |
+----------------------------------------------------+----------------------------------------------------+
| token.RIGHTSHIFTEQUAL                              | "">>=""                                            |
+----------------------------------------------------+----------------------------------------------------+
| token.DOUBLESTAREQUAL                              | ""**=""                                            |
+----------------------------------------------------+----------------------------------------------------+
| token.DOUBLESLASH                                  | ""//""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.DOUBLESLASHEQUAL                             | ""//=""                                            |
+----------------------------------------------------+----------------------------------------------------+
| token.AT                                           | ""@""                                              |
+----------------------------------------------------+----------------------------------------------------+
| token.ATEQUAL                                      | ""@=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.RARROW                                       | ""->""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.ELLIPSIS                                     | ""...""                                            |
+----------------------------------------------------+----------------------------------------------------+
| token.COLONEQUAL                                   | "":=""                                             |
+----------------------------------------------------+----------------------------------------------------+
| token.EXCLAMATION                                  | ""!""                                              |
+----------------------------------------------------+----------------------------------------------------+

As seguintes constantes não-tokens são fornecidas:

token.N_TOKENS

   O número de tipos de token definidos neste módulo.

token.EXACT_TOKEN_TYPES

   Um dicionário que mapeia a representação de string de um token para
   seu código numérico.

   Adicionado na versão 3.8.

Alterado na versão 3.5: Adicionados os tokens "AWAIT" e "ASYNC".

Alterado na versão 3.7: Adicionados os tokens "COMMENT", "NL" e
"ENCODING".

Alterado na versão 3.7: Removido os tokens "AWAIT" e "ASYNC". "async"
e "await" são agora tokenizados como tokens "NAME".

Alterado na versão 3.8: Adicionados "TYPE_COMMENT", "TYPE_IGNORE",
"COLONEQUAL". Adicionados os tokens "AWAIT" e "ASYNC" (eles são
necessários para dar suporte à análise de versões mais antigas do
Python para "ast.parse()" com "feature_version" definido como 6 ou
inferior).

Alterado na versão 3.12: Adicionado "EXCLAMATION".

Alterado na versão 3.13: Removidos novamente os tokens "AWAIT" e
"ASYNC".
