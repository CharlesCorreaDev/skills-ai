"email.generator": Geração de documentos MIME
*********************************************

**Código-fonte:** Lib/email/generator.py

======================================================================

Uma das tarefas mais comuns é gerar a versão plana (serializada) da
mensagem de e-mail representada por uma estrutura de objeto de
mensagem. Você precisará fazer isso se quiser enviar sua mensagem via
"smtplib.SMTP.sendmail()" ou exibir a mensagem no console. A tarefa
das classes geradoras é pegar uma estrutura de objeto de mensagem e
produzir uma representação serializada.

Assim como no módulo "email.parser", você não está limitado à
funcionalidade do gerador integrado; você mesmo pode criar um do zero.
No entanto, o gerador integrado sabe como gerar a maioria dos e-mails
em conformidade com os padrões, deve lidar perfeitamente com mensagens
de e-mail MIME e não MIME e foi projetado para que as operações de
análise e geração orientadas a bytes sejam inversas, presumindo que a
mesma "policy" não transformadora seja usada para ambas. Ou seja,
analisar o fluxo de bytes serializado por meio da classe "BytesParser"
e, em seguida, regenerar o fluxo de bytes serializado usando
"BytesGenerator" deve produzir uma saída idêntica à entrada [1]. (Por
outro lado, usar o gerador em um "EmailMessage" construído pelo
programa pode resultar em alterações no objeto "EmailMessage" à medida
que os padrões são preenchidos.)

A classe "Generator" pode ser usada para simplificar uma mensagem em
uma representação serializada de texto (em oposição a binária), mas
como o Unicode não pode representar dados binários diretamente, a
mensagem é necessariamente transformada em algo que contém apenas
caracteres ASCII, usando as técnicas de codificação de transferência
de conteúdo RFC de e-mail padrão para codificar mensagens de e-mail
para transporte em canais que não são "limpos de 8 bits".

Para acomodar o processamento reproduzível de mensagens assinadas por
SMIME, "Generator" desabilita a dobragem de cabeçalho para partes de
mensagens do tipo "multipart/signed" e todas as subpartes.

class email.generator.BytesGenerator(outfp, mangle_from_=None, maxheaderlen=None, *, policy=None)

   Retorna um objeto "BytesGenerator" que gravará qualquer mensagem
   fornecida ao método "flatten()", ou qualquer texto codificado
   surrogateescape fornecido ao método "write()", no *objeto arquivo
   ou similar* *outfp*. *outfp* deve oferecer suporte a um método
   "write" que aceite dados binários.

   Se o *mangle_from_* opcional for "True", coloca um caractere ">" na
   frente de qualquer linha no corpo que comece com a string exata
   ""From "", ou seja, "From" seguido por um espaço no início de uma
   linha. *mangle_from_* assume por padrão o valor da configuração
   "mangle_from_" da *policy* (que é "True" para a política "compat32"
   e "False" para todas as outras). *mangle_from_* deve ser usado
   quando as mensagens são armazenadas no formato mbox do Unix
   (consulte "mailbox" e WHY THE CONTENT-LENGTH FORMAT IS BAD).

   If *maxheaderlen* is not "None", refold any header lines that are
   longer than *maxheaderlen*, or if "0", do not rewrap any headers.
   If *maxheaderlen* is "None" (the default), wrap headers and other
   message lines according to the *policy* settings.

   Se *policy* for especificado, usa essa política para controlar a
   geração de mensagens. Se *policy* for "None" (o padrão), usa a
   política associada ao objeto "Message" ou "EmailMessage" passado
   para "flatten" para controlar a geração de mensagens. Consulte
   "email.policy" para obter detalhes sobre o que *policy* controla.

   Adicionado na versão 3.2.

   Alterado na versão 3.3: Adicionada o argumento nomeado *policy*.

   Alterado na versão 3.6: O comportamento padrão dos parâmetros
   *mangle_from_* e *maxheaderlen* é seguir a política.

   flatten(msg, unixfrom=False, linesep=None)

      Exibe a representação textual da estrutura do objeto de mensagem
      com raiz em *msg* no arquivo de saída especificado quando a
      instância "BytesGenerator" foi criada.

      Se a opção "policy" "cte_type" for "8bit" (o padrão), copia
      todos os cabeçalhos da mensagem original analisada que não
      tenham sido modificados para a saída, com todos os bytes com o
      bit mais alto definido reproduzidos como no original, e preserva
      a *Content-Transfer-Encoding* não ASCII de quaisquer partes do
      corpo que os contenham. Se "cte_type" for "7bit", converte os
      bytes com o bit mais alto definido, conforme necessário, usando
      uma *Content-Transfer-Encoding* compatível com ASCII. Ou seja,
      transforma partes com *Content-Transfer-Encoding* não ASCII
      (*Content-Transfer-Encoding: 8bit*) em um *Content-Transfer-
      Encoding* compatível com ASCII e codifica bytes não ASCII
      inválidos para RFC em cabeçalhos usando o conjunto de caracteres
      MIME "unknown-8bit", tornando-os compatíveis com RFC.

      Se *unixfrom* for "True", exibe o delimitador de cabeçalho de
      envelope usado pelo formato de caixa de correio Unix (consulte
      "mailbox") antes do primeiro dos cabeçalhos **RFC 5322** do
      objeto de mensagem raiz. Se o objeto raiz não tiver cabeçalho de
      envelope, crie um padrão. O padrão é "False". Observe que, para
      subpartes, nenhum cabeçalho de envelope é exibido.

      Se *linesep* não for "None", usa-o como caractere separador
      entre todas as linhas da mensagem simplificada. Se *linesep* for
      "None" (o padrão), usa o valor especificado na *policy*.

   clone(fp)

      Retorna um clone independente desta instância "BytesGenerator"
      com exatamente as mesmas configurações de opção e *fp* como o
      novo *outfp*.

   write(s)

      Codifica *s* usando o codec "ASCII" e o tratador de erros
      "surrogateescape" e passa-o para o método *write* do *outfp*
      passado ao construtor "BytesGenerator".

Para facilitar, "EmailMessage" fornece os métodos "as_bytes()" e
"bytes(aMessage)" (também conhecidos como "__bytes__()"), que
simplificam a geração de uma representação binária serializada de um
objeto de mensagem. Para mais detalhes, consulte "email.message".

Because strings cannot represent binary data, the "Generator" class
must convert any binary data in any message it flattens to an ASCII
compatible format, by converting them to an ASCII compatible *Content-
Transfer-Encoding*.  Using the terminology of the email RFCs, you can
think of this as "Generator" serializing to an I/O stream that is not
"8 bit clean".  In other words, most applications will want to be
using "BytesGenerator", and not "Generator".

class email.generator.Generator(outfp, mangle_from_=None, maxheaderlen=None, *, policy=None)

   Retorna um objeto "Generator" que gravará qualquer mensagem
   fornecida ao método "flatten()", ou qualquer texto fornecido ao
   método "write()", no *objeto arquivo ou similar* *outfp*. *outfp*
   deve oferecer suporte a um método "write" que aceite dados string.

   Se o *mangle_from_* opcional for "True", coloca um caractere ">" na
   frente de qualquer linha no corpo que comece com a string exata
   ""From "", ou seja, "From" seguido por um espaço no início de uma
   linha. *mangle_from_* assume por padrão o valor da configuração
   "mangle_from_" da *policy* (que é "True" para a política "compat32"
   e "False" para todas as outras). *mangle_from_* deve ser usado
   quando as mensagens são armazenadas no formato mbox do Unix
   (consulte "mailbox" e WHY THE CONTENT-LENGTH FORMAT IS BAD).

   If *maxheaderlen* is not "None", refold any header lines that are
   longer than *maxheaderlen*, or if "0", do not rewrap any headers.
   If *maxheaderlen* is "None" (the default), wrap headers and other
   message lines according to the *policy* settings.

   Se *policy* for especificado, usa essa política para controlar a
   geração de mensagens. Se *policy* for "None" (o padrão), usa a
   política associada ao objeto "Message" ou "EmailMessage" passado
   para "flatten" para controlar a geração de mensagens. Consulte
   "email.policy" para obter detalhes sobre o que *policy* controla.

   Alterado na versão 3.3: Adicionada o argumento nomeado *policy*.

   Alterado na versão 3.6: O comportamento padrão dos parâmetros
   *mangle_from_* e *maxheaderlen* é seguir a política.

   flatten(msg, unixfrom=False, linesep=None)

      Exibe a representação textual da estrutura do objeto de mensagem
      com raiz em *msg* no arquivo de saída especificado quando a
      instância "Generator" foi criada.

      Se a opção "policy" "cte_type" for "8bit", gera a mensagem como
      se a opção estivesse definida como "7bit". (Isso é necessário
      porque strings não podem representar bytes não ASCII.) Converte
      quaisquer bytes com o bit mais alto definido, conforme
      necessário, usando uma *Content-Transfer-Encoding* compatível
      com ASCII. Ou seja, transforma partes com *Content-Transfer-
      Encoding* não ASCII (*Content-Transfer-Encoding: 8bit*) em um
      *Content-Transfer-Encoding* compatível com ASCII e codifica
      bytes não ASCII inválidos para RFC em cabeçalhos usando o
      conjunto de caracteres MIME "unknown-8bit", tornando-os
      compatíveis com RFC.

      Se *unixfrom* for "True", exibe o delimitador de cabeçalho de
      envelope usado pelo formato de caixa de correio Unix (consulte
      "mailbox") antes do primeiro dos cabeçalhos **RFC 5322** do
      objeto de mensagem raiz. Se o objeto raiz não tiver cabeçalho de
      envelope, crie um padrão. O padrão é "False". Observe que, para
      subpartes, nenhum cabeçalho de envelope é exibido.

      Se *linesep* não for "None", usa-o como caractere separador
      entre todas as linhas da mensagem simplificada. Se *linesep* for
      "None" (o padrão), usa o valor especificado na *policy*.

      Alterado na versão 3.2: Adicionado suporte para recodificação de
      corpos de mensagens "8bit" e o argumento *linesep*.

   clone(fp)

      Retorna um clone independente desta instância "Generator" com
      exatamente as mesmas opções e *fp* como o novo *outfp*.

   write(s)

      Escreve *s* no método *write* do *outfp* passado ao construtor
      de "Generator". Isso fornece API arquivo ou similar suficiente
      para que instâncias de "Generator" sejam usadas na função
      "print()".

Para facilitar, "EmailMessage" fornece os métodos "as_string()" e
"str(aMessage)" (também conhecidos como "__str__()"), que simplificam
a geração de uma representação de string formatada de um objeto de
mensagem. Para mais detalhes, consulte "email.message".

O módulo "email.generator" também fornece uma classe derivada,
"DecodedGenerator", que é como a classe base "Generator", exceto que
as partes não-*text* não são serializadas, mas são representadas no
fluxo de saída por uma string derivada de um modelo preenchido com
informações sobre a parte.

class email.generator.DecodedGenerator(outfp, mangle_from_=None, maxheaderlen=None, fmt=None, *, policy=None)

   Age como "Generator", exceto que para qualquer subparte da mensagem
   passada para "Generator.flatten()", se a subparte for do tipo
   principal *text*, exibe a carga decodificada da subparte e, se o
   tipo principal não for *text*, em vez de exibi-la, preenche a
   string *fmt* usando informações da parte e exibe a string
   preenchida resultante.

   Para preencher *fmt*, executa "fmt % part_info", onde "part_info" é
   um dicionário composto pelas seguintes chaves e valores:

   * "type" -- Tipo MIME completo da parte não-*text*

   * "maintype" -- Tipo MIME principal da parte não-*text*

   * "subtype" -- Tipo sub-MIME da parte não-*text*

   * "filename" -- Nome de arquivo da parte não-*text*

   * "description" -- Descrição associada à parte não-*text*

   * "encoding" -- Codificação de transferência de conteúdo da parte
     não-*text*

   Se *fmt* for "None", usa o seguinte *fmt* padrão:

      "[Non-text (%(type)s) part of message omitted, filename
      %(filename)s]"

   Optional *mangle_from_* and *maxheaderlen* are as with the
   "Generator" base class.

-[ Notas de rodapé ]-

[1] Esta instrução presume que você usa a configuração apropriada para
    "unixfrom" e que não haja configurações "email.policy" que exijam
    ajustes automáticos (por exemplo, "refold_source" deve ser "none",
    que *não* é o padrão). Também não é 100% verdadeiro, pois, se a
    mensagem não estiver em conformidade com os padrões RFC,
    ocasionalmente informações sobre o texto original exato são
    perdidas durante a recuperação de erros de análise. O objetivo é
    corrigir esses últimos casos extremos sempre que possível.
