"contextvars" --- Variáveis de contexto
***************************************

======================================================================

Este módulo fornece APIs para gerenciar, armazenar e acessar o estado
local do contexto. A classe "ContextVar" é usada para declarar e
trabalhar com *Variáveis de Contexto*. A função "copy_context()" e a
classe "Context" devem ser usadas para gerenciar o contexto atual em
frameworks assíncronos.

Os gerenciadores de contexto que possuem estado devem usar Variáveis
de Contexto ao invés de "threading.local()" para evitar que seu estado
vaze para outro código inesperadamente, quando usado em código
concorrente.

Veja também a **PEP 567** para detalhes adicionais.

Adicionado na versão 3.7.


Variáveis de contexto
=====================

class contextvars.ContextVar(name[, *, default])

   Esta classe é usada para declarar uma nova variável de contexto,
   como, por exemplo:

      var: ContextVar[int] = ContextVar('var', default=42)

   O parâmetro obrigatório *name* é usado para fins de introspecção e
   depuração.

   O parâmetro somente-nomeado opcional *default* é retornado por
   "ContextVar.get()" quando nenhum valor para a variável é encontrado
   no contexto atual.

   **Importante:** Variáveis de Contexto devem ser criadas no nível do
   módulo superior e nunca em fechamentos. Os objetos "Context" contêm
   referências fortes a variáveis de contexto que evitam que as
   variáveis de contexto sejam coletadas como lixo corretamente.

   "ContextVar"s are generic over the type of their contained value.

   name

      O nome da variável. Esta é uma propriedade somente leitura.

      Adicionado na versão 3.7.1.

   get([default])

      Retorna um valor para a variável de contexto para o contexto
      atual.

      Se não houver valor para a variável no contexto atual, o método
      vai:

      * retornar o valor do argumento *default* do método, se
        fornecido; ou

      * retornar o valor padrão para a variável de contexto, se ela
        foi criada com uma; ou

      * levantar uma "LookupError".

   set(value)

      Chame para definir um novo valor para a variável de contexto no
      contexto atual.

      O argumento *value* obrigatório é o novo valor para a variável
      de contexto.

      Retorna um objeto "Token" que pode ser usado para restaurar a
      variável ao seu valor anterior através do método
      "ContextVar.reset()".

      For convenience, the token object can be used as a context
      manager to avoid calling "ContextVar.reset()" manually:

         var = ContextVar('var', default='default value')with var.set('new value'):    assert var.get() == 'new value'assert var.get() == 'default value'

      It is a shorthand for:

         var = ContextVar('var', default='default value')

         token = var.set('new value')
         try:
             assert var.get() == 'new value'
         finally:
             var.reset(token)

         assert var.get() == 'default value'

      Adicionado na versão 3.14: Added support for using tokens as
      context managers.

   reset(token)

      Redefine a variável de contexto para o valor que tinha antes de
      "ContextVar.set()". que criou o *token*, ser usado.

      Por exemplo:

         var = ContextVar('var')

         token = var.set('novo valor')
         # código que usa 'var'; var.get() retorna 'novo valor'.
         var.reset(token)

         # Após uma chamada de redefinição, var não tem mais valor,
         # então var.get() levantaria uma exceção LookupError.

      The same *token* cannot be used twice.

class contextvars.Token

   *Token* objects are returned by the "ContextVar.set()" method. They
   can be passed to the "ContextVar.reset()" method to revert the
   value of the variable to what it was before the corresponding
   *set*. A single token cannot reset a context variable more than
   once.

   Tokens support the context manager protocol to automatically reset
   context variables. See "ContextVar.set()".

   Tokens are generic over the same type as the "ContextVar" which
   created them.

   Adicionado na versão 3.14: Adicionado suporte para uso como
   gerenciador de contexto.

   var

      Uma propriedade somente leitura. Aponta para o objeto
      "ContextVar" que criou o token.

   old_value

      Uma propriedade somente leitura. Definida com o valor que a
      variável tinha antes da chamada do método "ContextVar.set()" que
      criou o token. Aponta para "Token.MISSING" se a variável não foi
      definida antes da chamada.

   MISSING

      Um objeto marcador usado por "Token.old_value".


Gerenciamento de contexto manual
================================

contextvars.copy_context()

   Retorna uma cópia do objeto "Context" atual.

   O trecho a seguir obtém uma cópia do contexto atual e imprime todas
   as variáveis e seus valores que estão definidos nele:

      ctx: Context = copy_context()
      print(list(ctx.items()))

   A função tem uma complexidade *O*(1), ou seja, funciona igualmente
   rápida para contextos com algumas variáveis de contexto e para
   contextos que têm muitas delas.

class contextvars.Context

   Um mapeamento de "ContextVars" para seus valores.

   "Context()" cria um contexto vazio sem valores nele. Para obter uma
   cópia do contexto atual, use a função "copy_context()".

   Cada thread tem sua própria pilha efetiva de objetos "Context". O
   *contexto atual* é o objeto "Context" no topo da pilha da thread
   atual. Todos os objetos "Context" nas pilhas são considerados como
   *inseridos*.

   *Inserir* um contexto, o que pode ser feito chamando seu método
   "run()", torna o contexto o contexto atual, colocando-o no topo da
   pilha de contexto da thread atual.

   *Sair* do contexto atual, o que pode ser feito retornando do
   retorno de chamada passado para o método "run()", restaura o
   contexto atual para o que era antes de o contexto ser inserido,
   retirando o contexto do topo da pilha de contextos.

   Como cada thread tem sua própria pilha de contexto, os objetos
   "ContextVar" se comportam de maneira semelhante a
   "threading.local()" quando valores são atribuídos em threads
   diferentes.

   Tentar entrar em um contexto já inserido, incluindo contextos
   inseridos em outras threads, levanta uma exceção "RuntimeError".

   Após sair de um contexto, ele pode ser acessado novamente (de
   qualquer thread).

   Quaisquer alterações nos valores de "ContextVar" por meio do método
   "ContextVar.set()" são registradas no contexto atual. O método
   "ContextVar.get()" retorna o valor associado ao contexto atual.
   Sair de um contexto efetivamente reverte quaisquer alterações
   feitas nas variáveis de contexto enquanto o contexto foi inserido
   (se necessário, os valores podem ser restaurados ao inserir
   novamente o contexto).

   Context implementa a interface "collections.abc.Mapping".

   run(callable, *args, **kwargs)

      Entra no Context, executa "callable(*args, **kwargs)" e sai do
      Context. Retorna o valor de retorno de *callable* ou propaga uma
      exceção, se ocorrer uma.

      Exemplo:

         import contextvars

         var = contextvars.ContextVar('var')
         var.set('spam')
         print(var.get())  # 'spam'

         ctx = contextvars.copy_context()

         def main():
             # 'var' foi definida para 'spam' antes de
             # chamar 'copy_context()' e 'ctx.run(main)', então:
             print(var.get())  # 'spam'
             print(ctx[var])  # 'spam'

             var.set('ham')

             # Agora, após definir 'var' para 'ham':
             print(var.get())  # 'ham'
             print(ctx[var])  # 'ham'

         # Qualquer alteração que a função 'main' feitas a 'var'
         # serão contidos em 'ctx'.
         ctx.run(main)

         # A função 'main()' era executada no contexto 'ctx',
         # então alterações a 'var' são contidas nele:
         print(ctx[var])  # 'ham'

         # No entanto, fora de 'ctx', 'var' ainda está definida para 'spam':
         print(var.get())  # 'spam'

   copy()

      Retorna uma cópia rasa do objeto contexto.

   var in context

      Retorna "True" se *context* tem uma variável para *var*
      definida; do contrário, retorna "False".

   context[var]

      Retorna o valor da variável "ContextVar" *var*. Se a variável
      não for definida no objeto contexto, uma "KeyError" é levantada.

   get(var[, default])

      Retorna o valor para *var* se *var* tiver o valor no objeto
      contexto. Caso contrário, retorna *default*. Se *default* não
      for fornecido, retorna "None".

   iter(context)

      Retorna um iterador sobre as variáveis armazenadas no objeto
      contexto.

   len(proxy)

      Retorna o número das variáveis definidas no objeto contexto.

   keys()

      Retorna uma lista de todas as variáveis no objeto contexto.

   values()

      Retorna uma lista dos valores de todas as variáveis no objeto
      contexto.

   items()

      Retorna uma lista de tuplas de 2 elementos contendo todas as
      variáveis e seus valores no objeto contexto.


Suporte a asyncio
=================

Variáveis de contexto encontram suporte nativo em "asyncio" e estão
prontas para serem usadas sem qualquer configuração extra. Por
exemplo, aqui está um servidor simples de eco, que usa uma variável de
contexto para disponibilizar o endereço de um cliente remoto na Task
que lida com esse cliente:

   import asyncio
   import contextvars

   client_addr_var = contextvars.ContextVar('client_addr')

   def render_goodbye():
       # The address of the currently handled client can be accessed
       # without passing it explicitly to this function.

       client_addr = client_addr_var.get()
       return f'Good bye, client @ {client_addr}\r\n'.encode()

   async def handle_request(reader, writer):
       addr = writer.transport.get_extra_info('socket').getpeername()
       client_addr_var.set(addr)

       # In any code that we call, it is now possible to get the
       # client's address by calling 'client_addr_var.get()'.

       while True:
           line = await reader.readline()
           print(line)
           if not line.strip():
               break

       writer.write(b'HTTP/1.1 200 OK\r\n')  # status line
       writer.write(b'\r\n')  # headers
       writer.write(render_goodbye())  # body
       writer.close()

   async def main():
       srv = await asyncio.start_server(
           handle_request, '127.0.0.1', 8081)

       async with srv:
           await srv.serve_forever()

   asyncio.run(main())

   # To test it you can use telnet or curl:
   #     telnet 127.0.0.1 8081
   #     curl 127.0.0.1:8081
