"socketserver" --- Um framework para servidores de rede
*******************************************************

**Código-fonte:** Lib/socketserver.py

======================================================================

O módulo "socketserver" simplifica a tarefa de escrever servidores de
rede.

Disponibilidade: not WASI.

Este módulo não funciona ou não está disponível em WebAssembly. Veja
Plataformas WebAssembly para mais informações.

Existem quatro classes básicas de servidores concretos:

class socketserver.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)

   Isso usa o protocolo TCP da internet, que fornece fluxos contínuos
   de dados entre o cliente e o servidor. Se *bind_and_activate* for
   true, o construtor tenta automaticamente invocar "server_bind()" e
   "server_activate()". Os outros parâmetros são passados para a
   classe base "BaseServer".

   Alterado na versão 3.15: O tamanho padrão de filas agora é
   "socket.SOMAXCONN" para "socketserver.TCPServer".

class socketserver.UDPServer(server_address, RequestHandlerClass, bind_and_activate=True)

   Isso usa datagramas, que são pacotes discretos de informações que
   podem chegar fora de ordem ou ser perdidos durante o trânsito. Os
   parâmetros são os mesmos de "TCPServer".

class socketserver.UnixStreamServer(server_address, RequestHandlerClass, bind_and_activate=True)
class socketserver.UnixDatagramServer(server_address, RequestHandlerClass, bind_and_activate=True)

   Essas classes usadas com menos frequência são semelhantes às
   classes TCP e UDP, mas usam soquetes de domínio Unix; elas não
   estão disponíveis em plataformas não Unix. Os parâmetros são os
   mesmos de "TCPServer".

Essas quatro classes processam solicitações *synchronously*; cada
solicitação deve ser concluída antes que a próxima solicitação possa
ser iniciada. Isso não é adequado se cada solicitação demorar muito
para ser concluída, porque exige muita computação ou porque retorna
muitos dados que o cliente demora a processar. A solução é criar um
processo ou thread separado para lidar com cada solicitação; as
classes misturadas "ForkingMixIn" e "ThreadingMixIn" podem ser usadas
para oferecer suporte ao comportamento assíncrono.

Criar um servidor requer várias etapas. Primeiro, você deve criar uma
classe de manipulador de solicitação estendendo a classe
"BaseRequestHandler" e substituindo seu método "handle()"; esse método
processará as solicitações recebidas. Segundo, você deve instanciar
uma das classes de servidor, passando a ela o endereço do servidor e a
classe de manipulador de solicitação. É recomendável usar o servidor
em uma instrução "with". Em seguida, chame o método "handle_request()"
ou "serve_forever()" do objeto do servidor para processar uma ou
muitas solicitações. Finalmente, chame "server_close()" para fechar o
soquete (a menos que você tenha usado uma instrução "with").

Ao herdar de "ThreadingMixIn" para comportamento de conexão em
threads, você deve declarar explicitamente como quer que suas threads
se comportem em um desligamento abrupto. A classe "ThreadingMixIn"
define um atributo *daemon_threads*, que indica se o servidor deve ou
não esperar pelo término da thread. Você deve definir o sinalizador
explicitamente se quiser que as threads se comportem de forma
autônoma; o padrão é "False", o que significa que o Python não sairá
até que todas as threads criadas por "ThreadingMixIn" tenham sido
encerradas.

As classes de servidor têm os mesmos métodos e atributos externos, não
importa qual protocolo de rede eles usam.


Notas sobre criação do servidor
===============================

Existem cinco classes em um diagrama de herança, quatro das quais
representam servidores síncronos de quatro tipos:

   +------------+
   | BaseServer |
   +------------+
         |
         v
   +-----------+        +------------------+
   | TCPServer |------->| UnixStreamServer |
   +-----------+        +------------------+
         |
         v
   +-----------+        +--------------------+
   | UDPServer |------->| UnixDatagramServer |
   +-----------+        +--------------------+

Observe que "UnixDatagramServer" deriva de "UDPServer", não de
"UnixStreamServer" --- a única diferença entre um IP e um servidor
Unix é a família de endereços.

class socketserver.ForkingMixIn
class socketserver.ThreadingMixIn

   Versões de fork e threads de cada tipo de servidor podem ser
   criadas usando essas classes mix-in. Por exemplo,
   "ThreadingUDPServer" é criado da seguinte forma:

      class ThreadingUDPServer(ThreadingMixIn, UDPServer):
          pass

   A classe mix-in vem primeiro, pois ela substitui um método definido
   em "UDPServer". Definir os vários atributos também altera o
   comportamento do mecanismo de servidor subjacente.

   "ForkingMixIn" e as classes Forking mencionadas abaixo estão
   disponíveis apenas em plataformas POSIX que oferecem suporte a
   "fork()".

   block_on_close

      "ForkingMixIn.server_close" aguarda até que todos os processos
      filho sejam concluídos, exceto se o atributo "block_on_close"
      for "False".

      "ThreadingMixIn.server_close" aguarda até que todos as threads
      não daemon sejam concluídos, exceto se o atributo
      "block_on_close" for "False".

   max_children

      Especifica quantos processos filho existirão para processar
      solicitações simultaneamente para "ForkingMixIn". Se o limite
      for atingido, novas solicitações aguardarão até que um processo
      filho seja concluído.

   daemon_threads

      Para "ThreadingMixIn", use threads como daemon definindo
      "ThreadingMixIn.daemon_threads" como "True" para não esperar até
      que as threads sejam concluídas.

   Alterado na versão 3.7: "ForkingMixIn.server_close" e
   "ThreadingMixIn.server_close" agora esperam até que todos os
   processos filhos e threads não daemon sejam concluídos. Adicione um
   novo atributo de classe "ForkingMixIn.block_on_close" para optar
   pelo comportamento pré-3.7.

class socketserver.ForkingTCPServer
class socketserver.ForkingUDPServer
class socketserver.ThreadingTCPServer
class socketserver.ThreadingUDPServer
class socketserver.ForkingUnixStreamServer
class socketserver.ForkingUnixDatagramServer
class socketserver.ThreadingUnixStreamServer
class socketserver.ThreadingUnixDatagramServer

   Essas classes são predefinidas usando as classes mix-in.

Adicionado na versão 3.12: As classes "ForkingUnixStreamServer" e
"ForkingUnixDatagramServer" foram adicionadas.

Para implementar um serviço, você deve derivar uma classe de
"BaseRequestHandler" e redefinir seu método "handle()". Você pode
então executar várias versões do serviço combinando uma das classes de
servidor com sua classe de manipulador de solicitação. A classe de
manipulador de solicitação deve ser diferente para serviços de
datagrama ou fluxo. Isso pode ser ocultado usando as subclasses de
manipulador "StreamRequestHandler" ou "DatagramRequestHandler".

Claro, você ainda tem que usar sua cabeça! Por exemplo, não faz
sentido usar um servidor de Forking se o serviço contém estado na
memória que pode ser modificado por diferentes solicitações, já que as
modificações no processo filho nunca atingiriam o estado inicial
mantido no processo pai e passado para cada filho. Neste caso, você
pode usar um servidor de Threading, mas provavelmente terá que usar
travas para proteger a integridade dos dados compartilhados.

Por outro lado, se você estiver construindo um servidor HTTP onde
todos os dados são armazenados externamente (por exemplo, no sistema
de arquivos), uma classe síncrona essencialmente tornará o serviço
"surdo" enquanto uma solicitação estiver sendo manipulada -- o que
pode ser por um tempo muito longo se um cliente for lento para receber
todos os dados que solicitou. Aqui, um servidor de Threading ou
Forking é apropriado.

Em alguns casos, pode ser apropriado processar parte de uma
solicitação de forma síncrona, mas terminar o processamento em um
filho bifurcado dependendo dos dados da solicitação. Isso pode ser
implementado usando um servidor síncrono e fazendo uma bifurcação
explícita no método da classe do manipulador de solicitações
"handle()".

Outra abordagem para lidar com múltiplas requisições simultâneas em um
ambiente que não oferece suporte a threads nem "fork()" (ou onde estes
são muito caros ou inapropriados para o serviço) é manter uma tabela
explícita de requisições parcialmente finalizadas e usar "selectors"
para decidir em qual requisição trabalhar em seguida (ou se deve lidar
com uma nova requisição recebida). Isto é particularmente importante
para serviços de fluxo onde cada cliente pode potencialmente ficar
conectado por um longo tempo (se threads ou subprocessos não puderem
ser usados).


Objetos Server
==============

class socketserver.BaseServer(server_address, RequestHandlerClass)

   Esta é a superclasse de todos os objetos Server no módulo. Ela
   define a interface, dada abaixo, mas não implementa a maioria dos
   métodos, o que é feito em subclasses. Os dois parâmetros são
   armazenados nos respectivos atributos "server_address" e
   "RequestHandlerClass".

   fileno()

      Retorna um descritor de arquivo inteiro para o soquete no qual o
      servidor está escutando. Esta função é mais comumente passada
      para "selectors", para permitir o monitoramento de múltiplos
      servidores no mesmo processo.

   handle_request()

      Processa uma única solicitação. Esta função chama os seguintes
      métodos em ordem: "get_request()", "verify_request()" e
      "process_request()". Se o método "handle()" fornecido pelo
      usuário da classe manipuladora levantar uma exceção, o método
      "handle_error()" do servidor será chamado. Se nenhuma
      solicitação for recebida dentro de "timeout" segundos,
      "handle_timeout()" será chamado e "handle_request()" retornará.

   serve_forever(poll_interval=0.5)

      Manipula solicitações até uma solicitação explícita
      "shutdown()". Sonda para desligamento a cada *poll_interval*
      segundos. Ignora o atributo "timeout". Ele também chama
      "service_actions()", que pode ser usado por uma subclasse ou
      mixin para fornecer ações específicas para um determinado
      serviço. Por exemplo, a classe "ForkingMixIn" usa
      "service_actions()" para limpar processos filhos zumbis.

      Alterado na versão 3.3: Adicionada chamada "service_actions" ao
      método "serve_forever".

   service_actions()

      Isso é chamado no laço "serve_forever()". Este método pode ser
      substituído por subclasses ou classes mixin para executar ações
      específicas para um determinado serviço, como ações de limpeza.

      Adicionado na versão 3.3.

   shutdown()

      Diz ao laço "serve_forever()" para parar e esperar até que isso
      aconteça. "shutdown()" deve ser chamado enquanto
      "serve_forever()" estiver em execução em um thread diferente,
      caso contrário, ocorrerá um impasse.

   server_close()

      Limpa o servidor. Pode ser substituído.

   address_family

      A família de protocolos à qual o soquete do servidor pertence.
      Exemplos comuns são "socket.AF_INET", "socket.AF_INET6" e
      "socket.AF_UNIX". Subclasse as classes de servidor TCP ou UDP
      neste módulo com o atributo de classe "address_family =
      AF_INET6" definido se você quiser classes de servidor IPv6.

   RequestHandlerClass

      A classe de manipulador de solicitações fornecida pelo usuário;
      uma instância dessa classe é criada para cada solicitação.

   server_address

      O endereço no qual o servidor está escutando. O formato dos
      endereços varia dependendo da família do protocolo; veja a
      documentação do módulo "socket" para detalhes. Para protocolos
      de internet, esta é uma tupla contendo uma string dando o
      endereço e um número de porta inteiro: "('127.0.0.1', 80)", por
      exemplo.

   socket

      O objeto soquete no qual o servidor ouve para solicitações
      recebidas.

   As classes de servidor oferecem suporte às seguintes variáveis de
   classe:

   allow_reuse_address

      Se o servidor permitirá a reutilização de um endereço. O padrão
      é "False", e pode ser definido em subclasses para alterar a
      política.

   request_queue_size

      O tamanho da fila de requisições. Se levar muito tempo para
      processar uma única requisição, todas as requisições que
      chegarem enquanto o servidor estiver ocupado serão colocadas em
      uma fila, até "request_queue_size" requisições. Quando a fila
      estiver cheia, outras requisições de clientes receberão um erro
      "Conexão negada". O valor padrão é geralmente 5, mas isso pode
      ser substituído por subclasses.

   socket_type

      O tipo de soquete usado pelo servidor; "socket.SOCK_STREAM" e
      "socket.SOCK_DGRAM" são dois valores comuns.

   timeout

      Duração do tempo limite, medida em segundos, ou "None" se nenhum
      tempo limite for desejado. Se "handle_request()" não receber
      nenhuma requisição de entrada dentro do período de tempo limite,
      o método "handle_timeout()" será chamado.

   Existem vários métodos de servidor que podem ser substituídos por
   subclasses de classes de servidor base, como "TCPServer"; esses
   métodos não são úteis para usuários externos do objeto de servidor.

   finish_request(request, client_address)

      Na verdade, processa a solicitação instanciando
      "RequestHandlerClass" e chamando seu método "handle()".

   get_request()

      Deve aceitar uma solicitação do soquete e retornar uma tupla de
      2 elementos contendo o *novo* objeto de soquete a ser usado para
      se comunicar com o cliente e o endereço do cliente.

   handle_error(request, client_address)

      Esta função é chamada se o método "handle()" de uma instância
      "RequestHandlerClass" levanta uma exceção. A ação padrão é
      exibir o traceback para erro padrão e continuar manipulando
      solicitações futuras.

      Alterado na versão 3.6: Agora é chamada apenas para exceções
      derivadas da classe "Exception".

   handle_timeout()

      Esta função é chamada quando o atributo "timeout" foi definido
      para um valor diferente de "None" e o período de timeout passou
      sem que nenhuma solicitação tenha sido recebida. A ação padrão
      para servidores de bifurcação é coletar o status de quaisquer
      processos filhos que tenham saído, enquanto em servidores de
      threading esse método não faz nada.

   process_request(request, client_address)

      Chama "finish_request()" para criar uma instância de
      "RequestHandlerClass". Se desejado, esta função pode criar um
      novo processo ou thread para manipular a solicitação; as classes
      "ForkingMixIn" e "ThreadingMixIn" fazem isso.

   server_activate()

      Chamado pelo construtor do servidor para ativar o servidor. O
      comportamento padrão para um servidor TCP apenas invoca
      "listen()" no soquete do servidor. Pode ser substituído.

   server_bind()

      Chamada pelo construtor do servidor para vincular o soquete ao
      endereço desejado. Pode ser substituída.

   verify_request(request, client_address)

      Deve retornar um valor booleano; se o valor for "True", a
      solicitação será processada, e se for "False", a solicitação
      será negada. Esta função pode ser substituída para implementar
      controles de acesso para um servidor. A implementação padrão
      sempre retorna "True".

   Alterado na versão 3.6: Foi adicionado suporte para o protocolo
   *gerenciador de contexto*. Sair do gerenciador de contexto é
   equivalente a chamar "server_close()".


Objetos manipulador de requisições
==================================

class socketserver.BaseRequestHandler

   Esta é a superclasse de todos os objetos manipulador de
   requisições. Ela define a interface, dada abaixo. Uma subclasse
   concreta do manipulador de requisições deve definir um novo método
   "handle()" e pode substituir qualquer um dos outros métodos. Uma
   nova instância da subclasse é criada para cada requisição.

   setup()

      Chamada antes do método "handle()" para executar quaisquer ações
      de inicialização necessárias. A implementação padrão não faz
      nada.

   handle()

      Esta função deve fazer todo o trabalho necessário para atender a
      uma solicitação. A implementação padrão não faz nada. Vários
      atributos de instância estão disponíveis para ela; a solicitação
      está disponível como "request"; o endereço do cliente como
      "client_address"; e a instância do servidor como "server", caso
      precise de acesso a informações por servidor.

      O tipo de "request" é diferente para serviços de datagrama ou
      fluxo. Para serviços de fluxo, "request" é um objeto soquete;
      para serviços de datagrama, "request" é um par de string e
      soquete.

   finish()

      Chamada após o método "handle()" para executar quaisquer ações
      de limpeza necessárias. A implementação padrão não faz nada. Se
      "setup()" levanta uma exceção, esta função não será chamada.

   request

      O *novo* objeto "socket.socket" a ser usado para se comunicar
      com o cliente.

   client_address

      Endereço do cliente retornado por "BaseServer.get_request()".

   server

      Objeto "BaseServer" usado para manipular a solicitação.

class socketserver.StreamRequestHandler
class socketserver.DatagramRequestHandler

   Essas subclasses "BaseRequestHandler" substituem os métodos
   "setup()" e "finish()" e fornecem os atributos "rfile" e "wfile".

   rfile

      Um objeto arquivo do qual recebe a solicitação é lido. Oferece
      suporte à interface legível "io.BufferedIOBase".

   wfile

      Um objeto arquivo no qual a resposta é escrita. Oferece suporte
      à interface gravável "io.BufferedIOBase"

   Alterado na versão 3.6: "wfile" também oferece suporte à interface
   gravável "io.BufferedIOBase".


Exemplos
========


Exemplo de "socketserver.TCPServer"
-----------------------------------

Este é o lado do servidor:

   import socketserver

   class MyTCPHandler(socketserver.BaseRequestHandler):
       """
       A classe de manipulador de solicitação para nosso servidor.

       Ela é instanciada uma vez por conexão com o servidor e deve
       substituir o método handle() para implementar a comunicação
       com o cliente.
       """

       def handle(self):
           # self.request é o soquete TCP conectado ao cliente
           pieces = [b'']
           total = 0
           while b'\n' not in pieces[-1] and total < 10_000:
               pieces.append(self.request.recv(2000))
               total += len(pieces[-1])
           self.data = b''.join(pieces)
           print(f"Received from {self.client_address[0]}:")
           print(self.data.decode("utf-8"))
           # só envia de volta os mesmos dados, mas em caixa alta
           self.request.sendall(self.data.upper())
           # após retornarmos, o soquete será fechado.

   if __name__ == "__main__":
       HOST, PORT = "localhost", 9999

       # Cria o servidor, ligando-o ao localhost na porta 9999
       with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
           # Ativa o servidor; isso vai mantê-lo em execução até você
           # interromper o programa com Ctrl-C
           server.serve_forever()

Uma classe de manipulador de solicitações alternativa que faz uso de
fluxos (objetos arquivo ou similares que simplificam a comunicação ao
fornecer a interface de arquivo padrão):

   class MyTCPHandler(socketserver.StreamRequestHandler):

       def handle(self):
           # self.rfile é um objeto arquivo ou similar criado pelo manipulador.
           # Agora podemos usar, por exemplo, readline() em vez de chamadas
           # brutas a recv().
           # Nos limitamos a 10000 bytes para evitar abuso pelo remetente.
           self.data = self.rfile.readline(10000).rstrip()
           print(f"{self.client_address[0]} wrote:")
           print(self.data.decode("utf-8"))
           # Da mesma forma, self.wfile é um objeto arquivo ou similar para
           # escrever de volta para o cliente
           self.wfile.write(self.data.upper())

A diferença é que a chamada "readline()" no segundo manipulador
chamará "recv()" várias vezes até encontrar um caractere de nova
linha, enquanto o primeiro manipulador teve que usar um laço "recv()"
para acumular dados até uma nova linha. Se tivesse usado apenas um
único "recv()" sem o laço, ele teria retornado apenas o que foi
recebido até agora do cliente. O TCP é baseado em fluxo: os dados
chegam na ordem em que foram enviados, mas não há correlação entre as
chamadas "send()" ou "sendall()" do cliente e o número de chamadas
"recv()" no servidor necessárias para recebê-los.

Este é o lado do cliente:

   import socket
   import sys

   HOST, PORT = "localhost", 9999
   data = " ".join(sys.argv[1:])

   # Cria um soquete (SOCK_STREAM significa um soquete TCP)
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
       # Conecta a um servidor e envia dados
       sock.connect((HOST, PORT))
       sock.sendall(bytes(data, "utf-8"))
       sock.sendall(b"\n")

       # Recebe dados do servidor e desliga
       received = str(sock.recv(1024), "utf-8")

   print("Sent:    ", data)
   print("Received:", received)

A saída do exemplo deve se parecer com algo como isso:

Servidor:

   $ python TCPServer.py
   127.0.0.1 wrote:
   b'hello world with TCP'
   127.0.0.1 wrote:
   b'python is nice'

Cliente:

   $ python TCPClient.py hello world with TCP
   Sent:     hello world with TCP
   Received: HELLO WORLD WITH TCP
   $ python TCPClient.py python is nice
   Sent:     python is nice
   Received: PYTHON IS NICE


Exemplo "socketserver.UDPServer"
--------------------------------

Este é o lado do servidor:

   import socketserver

   class MyUDPHandler(socketserver.BaseRequestHandler):
       """
       Esta classe funciona de forma semelhante à classe do manipulador TCP,
       exceto que self.request consiste em um par de dados e soquete do cliente
       e, como não há conexão, o endereço do cliente deve ser fornecido
       explicitamente ao enviar dados de volta via sendto().
       """

       def handle(self):
           data = self.request[0].strip()
           socket = self.request[1]
           print(f"{self.client_address[0]} wrote:")
           print(data)
           socket.sendto(data.upper(), self.client_address)

   if __name__ == "__main__":
       HOST, PORT = "localhost", 9999
       with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
           server.serve_forever()

Este é o lado do cliente:

   import socket
   import sys

   HOST, PORT = "localhost", 9999
   data = " ".join(sys.argv[1:])

   # SOCK_DGRAM é o tipo de soquete para usar para soquetes UDP
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   # Como você pode ver, não há uma chamada connect(); UDP não tem conexão.
   # Em vez disso, dados são enviados diretamente para o destinatário via sendto().
   sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
   received = str(sock.recv(1024), "utf-8")

   print("Sent:    ", data)
   print("Received:", received)

A saída do exemplo deve ser exatamente igual à do exemplo do servidor
TCP.


Mixins assíncronos
------------------

Para construir manipuladores assíncronos, use as classes
"ThreadingMixIn" e "ForkingMixIn".

Um exemplo para a classe "ThreadingMixIn":

   import socket
   import threading
   import socketserver

   class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

       def handle(self):
           data = str(self.request.recv(1024), 'ascii')
           cur_thread = threading.current_thread()
           response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
           self.request.sendall(response)

   class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
       pass

   def client(ip, port, message):
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
           sock.connect((ip, port))
           sock.sendall(bytes(message, 'ascii'))
           response = str(sock.recv(1024), 'ascii')
           print("Received: {}".format(response))

   if __name__ == "__main__":
       # Porta 0 significa selecionar uma porta não usada arbitrária
       HOST, PORT = "localhost", 0

       server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
       with server:
           ip, port = server.server_address

           # Inicia uma thread com o servidor -- essa thread vai então
           # iniciar mais um thread para cada requisição
           server_thread = threading.Thread(target=server.serve_forever)
           # Sai da thread do servidor quando a thread principal é encerrada
           server_thread.daemon = True
           server_thread.start()
           print("Server loop running in thread:", server_thread.name)

           client(ip, port, "Hello World 1")
           client(ip, port, "Hello World 2")
           client(ip, port, "Hello World 3")

           server.shutdown()

A saída do exemplo deve se parecer com algo como isso:

   $ python ThreadedTCPServer.py
   Server loop running in thread: Thread-1
   Received: Thread-2: Hello World 1
   Received: Thread-3: Hello World 2
   Received: Thread-4: Hello World 3

A classe "ForkingMixIn" é usada da mesma forma, exceto que o servidor
gerará um novo processo para cada solicitação. Disponível apenas em
plataformas POSIX que oferecem suporte a "fork()".
