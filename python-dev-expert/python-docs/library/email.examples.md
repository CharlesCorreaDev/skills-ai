"email": Exemplos
*****************

Aqui estão alguns exemplos de como usar o pacote "email" para ler,
escrever e enviar mensagens de e-mail simples, bem como mensagens MIME
mais complexas.

Primeiro, vamos ver como criar e enviar uma mensagem de texto simples
(tanto o conteúdo do texto quanto os endereços podem conter caracteres
Unicode):

   # Importa smtplib para a função de envio
   import smtplib

   # Importa os módulos de email que precisamos
   from email.message import EmailMessage

   # Abre o arquivo de texto simples cujo nome está em arquivo texto para leitura.
   with open(textfile) as fp:
       # Create a text/plain message
       msg = EmailMessage()
       msg.set_content(fp.read())

   # me == o endereço de e-mail do remetente
   # you == o endereço de e-mail do destinatário
   msg['Subject'] = f'The contents of {textfile}'
   msg['From'] = me
   msg['To'] = you

   # Envia a mensagem via nosso próprio servidor SMTP.
   s = smtplib.SMTP('localhost')
   s.send_message(msg)
   s.quit()

A análise dos cabeçalhos **RFC 822** pode ser feita facilmente usando
as classes do módulo "parser":

   # Importa os módulos de email que precisamos
   #from email.parser import BytesParser
   from email.parser import Parser
   from email.policy import default

   # Se os cabeçalhos de e-mal estão em um arquivo, descomente essas duas linhas:
   # with open(messagefile, 'rb') as fp:
   #     headers = BytesParser(policy=default).parse(fp)

   #  Ou para análise de cabeçalhos em uma string (essa é uma operação comum), use:
   headers = Parser(policy=default).parsestr(
           'From: Foo Bar <user@example.com>\n'
           'To: <someone_else@example.com>\n'
           'Subject: Test message\n'
           '\n'
           'Body would go here\n')

   #  Agora os itens de cabeçalho podem ser acessadas como um dicionário:
   print('To: {}'.format(headers['to']))
   print('From: {}'.format(headers['from']))
   print('Subject: {}'.format(headers['subject']))

   # Você também pode acessar as partes dos endereços:
   print('Recipient username: {}'.format(headers['to'].addresses[0].username))
   print('Sender name: {}'.format(headers['from'].addresses[0].display_name))

Aqui está um exemplo de como enviar uma mensagem MIME contendo várias
fotos de família que podem estar em um diretório:

   # Importa smtplib para a função de envio.
   import smtplib

   # Aqui estão os módulos de pacotes de e-mail que precisamos.
   from email.message import EmailMessage

   # Cria a contêiner da mensagem de e-mail.
   msg = EmailMessage()
   msg['Subject'] = 'Our family reunion'
   # me == o endereço de e-mail do remetente
   # family = a lista dos endereços de e-mail de todos os destinatários
   msg['From'] = me
   msg['To'] = ', '.join(family)
   msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

   # Abre os arquivos no modo binário. Você também pode omitir
   # o subtipo se você quiser que MIMEImage adivinhe.
   for file in pngfiles:
       with open(file, 'rb') as fp:
           img_data = fp.read()
       msg.add_attachment(img_data, maintype='image',
                                    subtype='png')

   # Envia o e-mail por meio de nosso próprio servidor SMTP.
   with smtplib.SMTP('localhost') as s:
       s.send_message(msg)

Aqui está um exemplo de como enviar todo o conteúdo de um diretório
como uma mensagem de e-mail: [1]

   #!/usr/bin/env python3

   """Envia o conteúdo de um diretório como uma mensagem MIME."""

   import os
   import smtplib
   # Para adivinhar o tipo MIME com base na extensão do nome do arquivo
   import mimetypes

   from argparse import ArgumentParser

   from email.message import EmailMessage
   from email.policy import SMTP


   def main():
       parser = ArgumentParser(description="""\
   Envia o conteúdo de um diretório como uma mensagem MIME.
   A menos que a opção -o seja informada, o e-mail será enviado por
   meio de encaminhamento para o seu servidor SMTP local, que então
   realiza o processo de entrega normal. Sua máquina local deve estar
   executando um servidor SMTP.
   """)
       parser.add_argument('-d', '--directory',
                           help="""Mail the contents of the specified directory,
                           otherwise use the current directory.  Only the regular
                           files in the directory are sent, and we don't recurse to
                           subdirectories.""")
       parser.add_argument('-o', '--output',
                           metavar='FILE',
                           help="""Print the composed message to FILE instead of
                           sending the message to the SMTP server.""")
       parser.add_argument('-s', '--sender', required=True,
                           help='The value of the From: header (required)')
       parser.add_argument('-r', '--recipient', required=True,
                           action='append', metavar='RECIPIENT',
                           default=[], dest='recipients',
                           help='A To: header value (at least one required)')
       args = parser.parse_args()
       directory = args.directory
       if not directory:
           directory = '.'
       # Cria a mensagem
       msg = EmailMessage()
       msg['Subject'] = f'Contents of directory {os.path.abspath(directory)}'
       msg['To'] = ', '.join(args.recipients)
       msg['From'] = args.sender
       msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

       for filename in os.listdir(directory):
           path = os.path.join(directory, filename)
           if not os.path.isfile(path):
               continue
           # Adivinhe o tipo de conteúdo com base na extensão do arquivo.
           # A codificação será ignorada, embora devamos verificar coisas
           # simples como arquivos compactados ou compactados com gzip.
           ctype, encoding = mimetypes.guess_file_type(path)
           if ctype is None or encoding is not None:
               # Não foi possível fazer nenhuma suposição, ou o arquivo está
               # codificado (compactado), então use um tipo genérico de
               # conjunto de bits.
               ctype = 'application/octet-stream'
           maintype, subtype = ctype.split('/', 1)
           with open(path, 'rb') as fp:
               msg.add_attachment(fp.read(),
                                  maintype=maintype,
                                  subtype=subtype,
                                  filename=filename)
       # Agora envia ou armazena a mensagem
       if args.output:
           with open(args.output, 'wb') as fp:
               fp.write(msg.as_bytes(policy=SMTP))
       else:
           with smtplib.SMTP('localhost') as s:
               s.send_message(msg)


   if __name__ == '__main__':
       main()

Aqui está um exemplo de como desempacotar uma mensagem MIME, como a
acima, para um diretório de arquivos:

   #!/usr/bin/env python3

   """Desempacota uma mensagem MIME em um diretório de arquivos."""

   import os
   import email
   import mimetypes

   from email.policy import default

   from argparse import ArgumentParser


   def main():
       parser = ArgumentParser(description="""\
   Desempacota uma mensagem MIME em um diretório de arquivos.
   """)
       parser.add_argument('-d', '--directory', required=True,
                           help="""Unpack the MIME message into the named
                           directory, which will be created if it doesn't already
                           exist.""")
       parser.add_argument('msgfile')
       args = parser.parse_args()

       with open(args.msgfile, 'rb') as fp:
           msg = email.message_from_binary_file(fp, policy=default)

       try:
           os.mkdir(args.directory)
       except FileExistsError:
           pass

       counter = 1
       for part in msg.walk():
           # multipart/* são apenas contêineres
           if part.get_content_maintype() == 'multipart':
               continue
           # Os aplicativos realmente devem higienizar o nome de arquivo
           # fornecido para que uma mensagem de e-mail não possa ser
           # usada para substituir arquivos importantes
           filename = part.get_filename()
           if not filename:
               ext = mimetypes.guess_extension(part.get_content_type())
               if not ext:
                   # Usa uma extensão genérica de conjunto de bits
                   ext = '.bin'
               filename = f'part-{counter:03d}{ext}'
           counter += 1
           with open(os.path.join(args.directory, filename), 'wb') as fp:
               fp.write(part.get_payload(decode=True))


   if __name__ == '__main__':
       main()

Aqui está um exemplo de como criar uma mensagem HTML com uma versão
alternativa em texto simples. Para tornar as coisas um pouco mais
interessantes, incluímos uma imagem relacionada na parte html e
salvamos uma cópia do que vamos enviar para o disco, assim como
enviamos.

   #!/usr/bin/env python3

   import smtplib

   from email.message import EmailMessage
   from email.headerregistry import Address
   from email.utils import make_msgid

   # Cria a mensagem texto base.
   msg = EmailMessage()
   msg['Subject'] = "Pourquoi pas des asperges pour ce midi ?"
   msg['From'] = Address("Pepé Le Pew", "pepe", "example.com")
   msg['To'] = (Address("Penelope Pussycat", "penelope", "example.com"),
                Address("Fabrette Pussycat", "fabrette", "example.com"))
   msg.set_content("""\
   Salut!

   Cette recette [1] sera sûrement un très bon repas.

   [1] http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718

   --Pepé
   """)

   # Adiciona a versão HTML. Isso converte a mensagem em um contêiner
   # multiparte/alternativo, com a mensagem de texto original como a primeira
   # parte e a nova mensagem HTML como a segunda parte.
   asparagus_cid = make_msgid()
   msg.add_alternative("""\
   <html>
     <head></head>
     <body>
       <p>Salut!</p>
       <p>Cette
           <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
               recette
           </a> sera sûrement un très bon repas.
       </p>
       <img src="cid:{asparagus_cid}">
     </body>
   </html>
   """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
   # observe que precisamos remover o <> do msgid para usar no html.

   # Agora adiciona a imagem relacionada à parte html.
   with open("roasted-asparagus.jpg", 'rb') as img:
       msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg',
                                        cid=asparagus_cid)

   # Agora adiciona a imagem relacionada à parte html.
   with open('outgoing.msg', 'wb') as f:
       f.write(bytes(msg))

   # Envia a mensagem via servidor SMTP local.
   with smtplib.SMTP('localhost') as s:
       s.send_message(msg)

Se nos fosse enviada a mensagem do último exemplo, aqui está uma
maneira de processá-la:

   import os
   import sys
   import tempfile
   import mimetypes
   import webbrowser

   # Importa os módulos de e-mail que precisaremos
   from email import policy
   from email.parser import BytesParser


   def magic_html_parser(html_text, partfiles):
       """Retorna HTML com segurança e link para partfiles.

       Reescreve os atributos href="cid:...." para apontar aos arquivos em partfiles.
       Embora não seja trivial, isso deve ser possível usando html.parser.
       """
       raise NotImplementedError("Add the magic needed")


   # Em um programa real, você pegaria o nome de arquivo a partir dos argumentos.
   with open('outgoing.msg', 'rb') as fp:
       msg = BytesParser(policy=policy.default).parse(fp)

   # Agora os itens de cabeçalho podem ser acessados como um dicionário e
   # qualquer caractere não-ASCII será convertido para unicode:
   print('To:', msg['to'])
   print('From:', msg['from'])
   print('Subject:', msg['subject'])

   # Se quisermos imprimir uma prévia do conteúdo da mensagem, podemos
   # extrair o conteúdo menos formatado e imprimir as três primeiras linhas.
   # É claro que, se a mensagem não tiver uma parte de texto simples,
   # imprimir as três primeiras linhas de HTML provavelmente será inútil,
   # mas este é apenas um exemplo conceitual.
   simplest = msg.get_body(preferencelist=('plain', 'html'))
   print()
   print(''.join(simplest.get_content().splitlines(keepends=True)[:3]))

   ans = input("View full message?")
   if ans.lower()[0] == 'n':
       sys.exit()

   # Podemos extrair a alternativa richest para exibi-la:
   richest = msg.get_body()
   partfiles = {}
   if richest['content-type'].maintype == 'text':
       if richest['content-type'].subtype == 'plain':
           for line in richest.get_content().splitlines():
               print(line)
           sys.exit()
       elif richest['content-type'].subtype == 'html':
           body = richest
       else:
           print("Don't know how to display {}".format(richest.get_content_type()))
           sys.exit()
   elif richest['content-type'].content_type == 'multipart/related':
       body = richest.get_body(preferencelist=('html'))
       for part in richest.iter_attachments():
           fn = part.get_filename()
           if fn:
               extension = os.path.splitext(part.get_filename())[1]
           else:
               extension = mimetypes.guess_extension(part.get_content_type())
           with tempfile.NamedTemporaryFile(suffix=extension, delete=False) as f:
               f.write(part.get_content())
               # remove novamente o <> para ir da forma email de cid para html.
               partfiles[part['content-id'][1:-1]] = f.name
   else:
       print("Don't know how to display {}".format(richest.get_content_type()))
       sys.exit()
   with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
       f.write(magic_html_parser(body.get_content(), partfiles))
   webbrowser.open(f.name)
   os.remove(f.name)
   for fn in partfiles.values():
       os.remove(fn)

   # É claro que há muitas mensagens de e-mail que podem quebrar
   # esse simples programa, mas ele lidará com as mais comuns.

Até o prompt, a saída do comando acima é:

   To: Penelope Pussycat <penelope@example.com>, Fabrette Pussycat <fabrette@example.com>
   From: Pepé Le Pew <pepe@example.com>
   Subject: Pourquoi pas des asperges pour ce midi ?

   Salut!

   Cette recette [1] sera sûrement un très bon repas.

-[ Notas de rodapé ]-

[1] Obrigado a Matthew Dixon Cowles pela inspiração original e pelos
    exemplos.
