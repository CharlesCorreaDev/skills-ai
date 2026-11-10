"email.charset": Representando conjuntos de caracteres
******************************************************

**Código-fonte:** Lib/email/charset.py

======================================================================

Este módulo faz parte da API de e-mail legada ("Compat32"). Na nova
API, apenas a tabela de apelidos é usada.

O texto restante nesta seção é a documentação original do módulo.

Este módulo fornece uma classe "Charset" para representar conjuntos de
caracteres e conversões de conjuntos de caracteres em mensagens de
e-mail, bem como um registro de conjuntos de caracteres e vários
métodos práticos para manipular esse registro. Instâncias de "Charset"
são usadas em vários outros módulos do pacote "email".

Importa esta classe do módulo "email.charset".

class email.charset.Charset(input_charset=DEFAULT_CHARSET)

   Mapeia conjuntos de caracteres para suas propriedades de e-mail.

   Esta classe fornece informações sobre os requisitos impostos ao
   e-mail para um conjunto de caracteres específico. Também fornece
   rotinas práticas para conversão entre conjuntos de caracteres,
   considerando a disponibilidade dos codecs aplicáveis. Dado um
   conjunto de caracteres, ela fará o possível para fornecer
   informações sobre como usá-lo em uma mensagem de e-mail de forma
   compatível com RFC.

   Certos conjuntos de caracteres devem ser codificados com quoted-
   printable ou base64 quando usados em cabeçalhos ou corpos de
   e-mail. Certos conjuntos de caracteres devem ser convertidos
   diretamente e não são permitidos em e-mails.

   O *input_charset* opcional é descrito abaixo; ele é sempre
   convertido para letras minúsculas. Após ser normalizado por
   apelido, ele também é usado como uma consulta no registro de
   conjuntos de caracteres para descobrir a codificação do cabeçalho,
   a codificação do corpo e o codec de conversão de saída a serem
   usados para o conjunto de caracteres. Por exemplo, se
   *input_charset* for "iso-8859-1", os cabeçalhos e corpos serão
   codificados usando quoted-printable e nenhum codec de conversão de
   saída será necessário. Se *input_charset* for "euc-jp", os
   cabeçalhos serão codificados em base64, os corpos não serão
   codificados, mas o texto de saída será convertido do conjunto de
   caracteres "euc-jp" para o conjunto de caracteres "iso-2022-jp".

   Instâncias "Charset" têm os seguintes atributos de dados:

   input_charset

      O conjunto de caracteres inicial especificado. Apelidos comuns
      são convertidos em seus nomes de e-mail *oficiais* (por exemplo,
      "latin_1" é convertido para "iso-8859-1"). O padrão é "us-ascii"
      de 7 bits.

   header_encoding

      Se o conjunto de caracteres precisar ser codificado antes de ser
      usado em um cabeçalho de e-mail, este atributo será definido
      como "charset.QP" (para quoted-printable), "charset.BASE64"
      (para codificação base64) ou "charset.SHORTEST" para a
      codificação mais curta entre QP ou BASE64. Caso contrário, será
      "None".

   body_encoding

      O mesmo que *header_encoding*, mas descreve a codificação do
      corpo da mensagem de e-mail, que pode ser diferente da
      codificação do cabeçalho. "charset.SHORTEST" não é permitido
      para *body_encoding*.

   output_charset

      Alguns conjuntos de caracteres precisam ser convertidos antes de
      serem usados em cabeçalhos ou corpos de e-mail. Se
      *input_charset* for um deles, este atributo conterá o nome do
      conjunto de caracteres para o qual a saída será convertida. Caso
      contrário, será "None".

   input_codec

      O nome do codec Python usado para converter o *input_charset*
      para Unicode. Se nenhum codec de conversão for necessário, este
      atributo será "None".

   output_codec

      O nome do codec Python usado para converter Unicode para o
      *output_charset*. Se nenhum codec de conversão for necessário,
      este atributo terá o mesmo valor que o *input_codec*.

   Instâncias "Charset" também têm os seguintes métodos:

   get_body_encoding()

      Retorna a codificação de transferência de conteúdo usada para
      codificação do corpo.

      Esta é a string "quoted-printable" ou "base64", dependendo da
      codificação usada, ou é uma função, caso em que você deve chamar
      a função com um único argumento, sendo o objeto Message
      codificado. A função deve então definir o próprio cabeçalho
      *Content-Transfer-Encoding* com o valor apropriado.

      Retorna a string "quoted-printable" se *body_encoding* for "QP",
      retorna a string "base64" se *body_encoding* for "BASE64" e
      retorna a string "7bit" caso contrário.

   get_output_charset()

      Retorna o conjunto de caracteres de saída.

      Este é o atributo *output_charset* se não for "None", caso
      contrário, é *input_charset*.

   header_encode(string)

      Codifica o cabeçalho com a string *string*.

      O tipo de codificação (base64 ou quoted-printable) será baseado
      no atributo *header_encoding*.

   header_encode_lines(string, maxlengths)

      Codifica um cabeçalho de uma *string* convertendo-a primeiro em
      bytes.

      Isso é semelhante a "header_encode()", exceto que a string é
      ajustada aos comprimentos máximos de linha, conforme fornecido
      pelo argumento *maxlengths*, que deve ser um iterador: cada
      elemento retornado deste iterador fornecerá o próximo
      comprimento máximo de linha.

   body_encode(string)

      Codifica o corpo com a string *string*.

      O tipo de codificação (base64 ou quoted-printable) será baseado
      no atributo *body_encoding*.

   A classe "Charset" também fornece vários métodos para dar suporte a
   operações padrão e funções embutidas.

   __str__()

      Retorna *input_charset* como uma string convertida para
      minúsculas. "__repr__()" é um apelido para "__str__()".

   __eq__(other)

      Este método permite que você compare duas instâncias "Charset"
      para verificar a igualdade.

   __ne__(other)

      Este método permite que você compare duas instâncias "Charset"
      para verificar a desigualdade.

O módulo "email.charset" também fornece as seguintes funções para
adicionar novas entradas ao conjunto global de caracteres, alias e
registros de codec.

email.charset.add_charset(charset, header_enc=None, body_enc=None, output_charset=None)

   Adiciona propriedades de caracteres ao registro global.

   *charset* é o conjunto de caracteres de entrada e deve ser o nome
   canônico de um conjunto de caracteres.

   *header_enc* e *body_enc* opcionais são "charset.QP" para quoted-
   printable, "charset.BASE64" para codificação base64,
   "charset.SHORTEST" para a codificação mais curta entre quoted-
   printable ou base64, ou "None" para nenhuma codificação. "SHORTEST"
   é válido apenas para *header_enc*. O padrão é "None" para nenhuma
   codificação.

   *output_charset* opcional é o conjunto de caracteres que a saída
   deve conter. As conversões prosseguirão do conjunto de caracteres
   de entrada para Unicode e para o conjunto de caracteres de saída
   quando o método "Charset.body_encode()" for chamado. O padrão é
   gerar a saída no mesmo conjunto de caracteres da entrada.

   Tanto *input_charset* quanto *output_charset* devem ter entradas de
   codec Unicode no mapeamento de conjunto de caracteres para codec do
   módulo; use "add_codec()" para adicionar codecs que o módulo não
   conhece. Consulte a documentação do módulo "codecs" para obter mais
   informações.

   O registro do conjunto de caracteres global é mantido no dicionário
   global do módulo "CHARSETS".

email.charset.add_alias(alias, canonical)

   Adicione um apelido para o conjunto de caracteres. *alias* é o nome
   do alias, por exemplo, "latin-1". *canonical* é o nome canônico do
   conjunto de caracteres, por exemplo, "iso-8859-1".

   O registro global de apelido de conjunto de caracteres é mantido no
   dicionário global do módulo "ALIASES".

email.charset.add_codec(charset, codecname)

   Adiciona um codec que mapeia caracteres no conjunto de caracteres
   fornecido para e a partir do Unicode.

   *charset* é o nome canônico de um conjunto de caracteres.
   *codecname* é o nome de um codec Python, conforme apropriado para o
   segundo argumento do método "encode()" do "str".
