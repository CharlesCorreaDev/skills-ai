"email.encoders": Codificadores
*******************************

**Código-fonte:** Lib/email/encoders.py

======================================================================

Este módulo faz parte da API legada de e-mail ("Compat32"). Na nova
API, a funcionalidade é fornecida pelo parâmetro *cte* do método
"set_content()".

Este módulo está descontinuado no Python 3. As funções fornecidas aqui
não devem ser chamadas explicitamente, pois a classe "MIMEText" define
o tipo de conteúdo e o cabeçalho CTE usando os valores *_subtype* e
*_charset* passados durante a instanciação dessa classe.

O texto restante nesta seção é a documentação original do módulo.

Ao criar objetos "Message" do zero, você frequentemente precisa
codificar as cargas úteis para transporte por meio de servidores de
e-mail compatíveis. Isso é especialmente verdadeiro para mensagens do
tipo *image/** e *text/** contendo dados binários.

O pacote "email" fornece alguns codificadores convenientes em seu
módulo "encoders". Esses codificadores são realmente usados pelos
construtores de classe "MIMEAudio" e "MIMEImage" para fornecer
codificações padrão. Todas as funções de codificador recebem
exatamente um argumento, o objeto de mensagem a ser codificado. Eles
geralmente extraem a carga útil, codificam-na e redefinem a carga útil
para esse valor recém-codificado. Eles também devem definir o
cabeçalho *Content-Transfer-Encoding* conforme apropriado.

Observe que essas funções não são significativas para uma mensagem
multiparte. Elas devem ser aplicadas a subpartes individuais, e
levantarão um "TypeError" se for passada uma mensagem cujo tipo seja
multiparte.

Aqui estão as funções de codificação fornecidas:

email.encoders.encode_quopri(msg)

   Codifica a carga útil em formato quoted-printable e define o
   cabeçalho *Content-Transfer-Encoding* como "quoted-printable" [1].
   Esta é uma boa codificação para usar quando a maior parte da sua
   carga útil é de dados imprimíveis normais, mas contém alguns
   caracteres não imprimíveis.

email.encoders.encode_base64(msg)

   Codifica a carga útil em formato base64 e define o cabeçalho
   *Content-Transfer-Encoding* para "base64". Esta é uma boa
   codificação para usar quando a maior parte da sua carga útil é de
   dados não imprimíveis, pois é um formato mais compacto do que
   quoted-printable. A desvantagem da codificação base64 é que ela
   torna o texto não legível por humanos.

email.encoders.encode_7or8bit(msg)

   Na verdade, isso não modifica a carga útil da mensagem, mas define
   o cabeçalho *Content-Transfer-Encoding* para "7bit" ou "8bit",
   conforme apropriado, com base nos dados da carga útil.

email.encoders.encode_noop(msg)

   Isso não faz nada; nem mesmo define o cabeçalho *Content-Transfer-
   Encoding*.

-[ Notas de rodapé ]-

[1] Observe que a codificação com "encode_quopri()" também codifica
    todos os caracteres de tabulação e espaço nos dados.
