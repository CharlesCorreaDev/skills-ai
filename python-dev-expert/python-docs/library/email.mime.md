"email.mime""email.mime": Criando e-mail e objetos MIME do zero
***************************************************************

**Código-fonte:** Lib/email/mime/

======================================================================

Este módulo faz parte da API de e-mail legada ("Compat32"). Sua
funcionalidade é parcialmente substituída por "contentmanager" na nova
API, mas em certos aplicativos essas classes ainda podem ser úteis,
mesmo em código não legado.

Normalmente, você obtém uma estrutura de objeto de mensagem passando
um arquivo ou algum texto para um analisador sintático, que analisa o
texto e retorna o objeto de mensagem raiz. No entanto, você também
pode criar uma estrutura de mensagem completa do zero, ou até objetos
individuais de "Message" manualmente. De fato, você também pode pegar
uma estrutura existente e adicionar novos objetos "Message", movê-los,
etc. Isso cria uma interface muito conveniente para fatiar e cortar
dados de mensagens MIME.

Você pode criar uma nova estrutura de objeto criando instâncias de
"Message", adicionando anexos e todos os cabeçalhos apropriados
manualmente. Porém, para mensagens MIME, o pacote "email" fornece
algumas subclasses convenientes para facilitar as coisas.

Arquivo estão as classes:

class email.mime.base.MIMEBase(_maintype, _subtype, *, policy=compat32, **_params)

   Módulo: "email.mime.base"

   Esta é a classe base para todas as subclasses específicas de MIME
   de "Message". Normalmente você não criará instâncias
   especificamente de "MIMEBase", embora possa. A "MIMEBase" é
   fornecida principalmente como uma classe base conveniente para
   subclasses mais específicas para MIME.

   *_maintype* é o tipo principal de *Content-Type* (ex., *text* ou
   *image*) e *_subtype* é o tipo principal de *Content-Type* (ex.,
   *plain* ou *gif*). *_params* é um dicionário de parâmetros
   chave/valor e é passado diretamente para "Message.add_header".

   Se *policy* for especificado, (o padrão é a política "compat32")
   será passado para "Message".

   A classe "MIMEBase" sempre adiciona um cabeçalho *Content-Type*
   (com base em *_maintype*, *_subtype* e *_params*) e um cabeçalho
   *MIME-Version* (sempre definido como "1.0").

   Alterado na versão 3.6: Adicionado o parâmetro somente-nomeado
   *policy*.

class email.mime.nonmultipart.MIMENonMultipart

   Módulo: "email.mime.nonmultipart"

   Uma subclasse de "MIMEBase", esta é uma classe base intermediária
   para mensagens MIME que não são *multipart*. O principal objetivo
   desta classe é impedir o uso do método "attach()", que só faz
   sentido para mensagens *multipart*. Se "attach()" for chamado, uma
   exceção "MultipartConversionError" será levantada.

class email.mime.multipart.MIMEMultipart(_subtype='mixed', boundary=None, _subparts=None, *, policy=compat32, **_params)

   Módulo: "email.mime.multipart"

   Uma subclasse de "MIMEBase", esta é uma classe base intermediária
   para mensagens MIME que são *multipart*. O *_subtype* opcional é
   padronizado como *mixed*, mas pode ser usado para especificar o
   subtipo da mensagem. Um cabeçalho *Content-Type* de
   *multipart/_subtype* será adicionado ao objeto da mensagem. Um
   cabeçalho *MIME-Version* também será adicionado.

   O *boundary* opcional é a string de limites de várias partes.
   Quando "None" (o padrão), o limite é calculado quando necessário
   (por exemplo, quando a mensagem é serializada).

   *_subparts* é uma sequência de subpartes iniciais para a carga.
   Deve ser possível converter essa sequência em uma lista. Você
   sempre pode anexar novas subpartes à mensagem usando o método
   "Message.attach".

   O argumento opcional *policy* tem como padrão "compat32".

   Parâmetros adicionais para o cabeçalho *Content-Type* são retirados
   dos argumentos nomeados ou passados para o argumento *_params*, que
   é um dicionário.

   Alterado na versão 3.6: Adicionado o parâmetro somente-nomeado
   *policy*.

class email.mime.application.MIMEApplication(_data, _subtype='octet-stream', _encoder=email.encoders.encode_base64, *, policy=compat32, **_params)

   Módulo: "email.mime.application"

   Uma subclasse de "MIMENonMultipart", a classe "MIMEApplication" é
   usada para representar objetos de mensagem MIME do tipo principal
   *application*. *_data* contém os bytes para os dados brutos da
   aplicação. O *_subtype* opcional especifica o subtipo MIME e o
   padrão é *octet-stream*.

   O *_encoder* opcional é um chamável (isto é, função) que executará
   a codificação real dos dados para transporte. Esse chamável requer
   um argumento, que é a instância "MIMEApplication". Ele deve usar
   "get_payload()" e "set_payload()" para alterar a carga útil para o
   formulário codificado. Também deve adicionar *Content-Transfer-
   Encoding* ou outros cabeçalhos ao objeto de mensagem, conforme
   necessário. A codificação padrão é base64. Veja o módulo
   "email.encoders" para obter uma lista dos codificadores embutidos.

   O argumento opcional *policy* tem como padrão "compat32".

   *_params* são passados diretamente para o construtor da classe
   base.

   Alterado na versão 3.6: Adicionado o parâmetro somente-nomeado
   *policy*.

class email.mime.audio.MIMEAudio(_audiodata, _subtype=None, _encoder=email.encoders.encode_base64, *, policy=compat32, **_params)

   Módulo: "email.mime.audio"

   Uma subclasse de "MIMENonMultipart", a classe "MIMEAudio" é usada
   para criar objetos de mensagem MIME do tipo principal *audio*.
   *_audiodata* contém os bytes para os dados brutos de áudio. Se
   esses dados puderem ser decodificados como au, wav, aiff ou aifc,
   então o subtipo será automaticamente incluído no cabeçalho
   *Content-Type*. Caso contrário, você pode especificar
   explicitamente o subtipo de áudio por meio do argumento *_subtype*.
   Se o tipo menor não pôde ser adivinhado e *_subtype* não foi
   fornecido, então um exceção "TypeError" é levantada.

   O *_encoder* opcional é um chamável (ou seja, função) que executará
   a codificação real dos dados de áudio para transporte. Esse
   chamável requer um argumento, que é a instância "MIMEAudio". Ele
   deve usar "get_payload()" e "set_payload()" para alterar a carga
   útil para a forma codificada. Também deve adicionar *Content-
   Transfer-Encoding* ou outros cabeçalhos ao objeto de mensagem,
   conforme necessário. A codificação padrão é base64. Veja o módulo
   "email.encoders" para obter uma lista dos codificadores embutidos.

   O argumento opcional *policy* tem como padrão "compat32".

   *_params* são passados diretamente para o construtor da classe
   base.

   Alterado na versão 3.6: Adicionado o parâmetro somente-nomeado
   *policy*.

class email.mime.image.MIMEImage(_imagedata, _subtype=None, _encoder=email.encoders.encode_base64, *, policy=compat32, **_params)

   Módulo: "email.mime.image"

   Uma subclasse de "MIMENonMultipart", a classe "MIMEImage" é usada
   para criar objetos de mensagem MIME do tipo principal *image*.
   *_imagedata* contém os bytes para os dados de imagem bruta. Se esse
   tipo de dados puder ser detectado (jpeg, png, gif, tiff, rgb, pbm,
   pgm, ppm, rast, xbm, bmp, webp e exr tentados), então o subtipo
   será automaticamente incluído no cabeçalho *Content-Type*. Caso
   contrário, você pode especificar explicitamente o subtipo de imagem
   por meio do argumento *_subtype*. Se o tipo secundário não puder
   ser adivinhado e *_subtype* não for fornecido, então "TypeError"
   será levantada.

   O *_encoder* opcional é um chamável (ou seja, função) que executará
   a codificação real dos dados de imagem para transporte. Esse
   chamável requer um argumento, que é a instância "MIMEImage". Ele
   deve usar "get_payload()" e "set_payload()" para alterar a carga
   útil para a forma codificada. Também deve adicionar *Content-
   Transfer-Encoding* ou outros cabeçalhos ao objeto de mensagem,
   conforme necessário. A codificação padrão é base64. Veja o módulo
   "email.encoders" para obter uma lista dos codificadores embutidos.

   O argumento opcional *policy* tem como padrão "compat32".

   *_params* são passados diretamente para o construtor "MIMEBase".

   Alterado na versão 3.6: Adicionado o parâmetro somente-nomeado
   *policy*.

class email.mime.message.MIMEMessage(_msg, _subtype='rfc822', *, policy=compat32)

   Módulo: "email.mime.message"

   Uma subclasse de "MIMENonMultipart", a classe "MIMEMessage" é usada
   para criar objetos MIME do tipo principal *message*. *_msg* é usado
   como carga útil e deve ser uma instância da classe "Message" (ou
   uma subclasse dela), caso contrário, uma "TypeError" é levantada.

   O opcional *_subtype* define o subtipo da mensagem; o padrão é
   *rfc822*.

   O argumento opcional *policy* tem como padrão "compat32".

   Alterado na versão 3.6: Adicionado o parâmetro somente-nomeado
   *policy*.

class email.mime.text.MIMEText(_text, _subtype='plain', _charset=None, *, policy=compat32)

   Módulo: "email.mime.text"

   Uma subclasse de "MIMENonMultipart", a classe "MIMEText" é usada
   para criar objetos MIME do tipo principal *text*. *_text* é a
   string para a carga útil. *_subtype* é o tipo secundário e o padrão
   é *plain*. *_charset* é o conjunto de caracteres do texto e é
   passado como um argumento para o construtor "MIMENonMultipart"; o
   padrão é "us-ascii" se a string contiver apenas pontos de código
   "ascii" e "utf-8" caso contrário. O parâmetro *_charset* aceita uma
   string ou uma instância "Charset".

   A menos que o argumento *_charset* seja explicitamente definido
   como "None", o objeto MIMEText criado terá um cabeçalho *Content-
   Type* com um parâmetro "charset" e um cabeçalho *Content-Transfer-
   Encoding*. Isso significa que uma chamada "set_payload" subsequente
   não resultará em uma carga útil codificada, mesmo se um charset for
   passado no comando "set_payload". Você pode "redefinir" esse
   comportamento excluindo o cabeçalho "Content-Transfer-Encoding",
   após o qual uma chamada "set_payload" codificará automaticamente a
   nova carga útil (e adicionará um novo cabeçalho *Content-Transfer-
   Encoding*).

   O argumento opcional *policy* tem como padrão "compat32".

   Alterado na versão 3.5: *_charset* também aceita instâncias de
   "Charset".

   Alterado na versão 3.6: Adicionado o parâmetro somente-nomeado
   *policy*.
