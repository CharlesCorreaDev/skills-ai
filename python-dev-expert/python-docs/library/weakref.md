"weakref" --- Referências fracas
********************************

**Código-fonte:** Lib/weakref.py

======================================================================

O módulo "weakref" permite ao programador Python criar *referências
fracas* para objetos.

A seguir, o termo *referente* significa o objeto ao qual é referido
por uma referência fraca.

Uma referência fraca a um objeto não é suficiente para mantê-lo vivo:
quando as únicas referências restantes a um referente são referências
fracas, a *coleta de lixo* está livre para destruir o referente e
reutilizar sua memória para outra coisa. Entretanto, até que o objeto
seja realmente destruído, a referência fraca poderá retornar o objeto
mesmo que não haja referências fortes a ele.

Um uso principal para referências fracas é implementar caches ou
mapeamentos contendo objetos grandes, onde é desejado que um objeto
grande não seja mantido ativo apenas porque aparece em um cache ou
mapeamento.

Por exemplo, se você tiver vários objetos de imagem binária grandes,
poderá associar um nome a cada um. Se você usasse um dicionário Python
para mapear nomes para imagens, ou imagens para nomes, os objetos de
imagem permaneceriam vivos apenas porque apareceriam como valores ou
chaves nos dicionários. As classes "WeakKeyDictionary" e
"WeakValueDictionary" fornecidas pelo módulo "weakref" são uma
alternativa, usando referências fracas para construir mapeamentos que
não mantêm objetos vivos apenas porque aparecem nos objetos de
mapeamento. Se, por exemplo, um objeto de imagem for um valor em um
"WeakValueDictionary", então quando as últimas referências restantes a
esse objeto de imagem forem as referências fracas mantidas por
mapeamentos fracos, a coleta de lixo poderá recuperar o objeto e suas
entradas correspondentes em mapeamentos fracos são simplesmente
excluídos.

"WeakKeyDictionary" e "WeakValueDictionary" usam referências fracas em
sua implementação, configurando funções de retorno de chamada nas
referências fracas que notificam os dicionários fracos quando uma
chave ou valor foi recuperado pela coleta de lixo. "WeakSet"
implementa a interface "set", mas mantém referências fracas aos seus
elementos, assim como "WeakKeyDictionary" faz.

"finalize" fornece uma maneira direta de registrar uma função de
limpeza a ser chamada quando um objeto é coletado como lixo. Isso é
mais simples de usar do que configurar uma função de retorno de
chamada em uma referência fraca não tratada, pois o módulo garante
automaticamente que o finalizador permaneça ativo até que o objeto
seja coletado.

A maioria dos programas deve descobrir que usar um desses tipos de
contêineres fracos ou "finalize" é tudo que eles precisam --
geralmente não é necessário criar suas próprias referências fracas
diretamente. O maquinário de baixo nível é exposto pelo módulo
"weakref" para benefício de usos avançados.

Nem todos os objetos podem ser referenciados de maneira fraca. Objetos
que oferecem suporte a referências fracas incluem instâncias de
classe, funções escritas em Python (mas não em C), métodos de
instância, conjuntos, frozensets, alguns *objetos arquivos*,
*geradores*, objetos tipo, sockets, arrays, deques, objetos padrão de
expressão regular e objetos código.

Alterado na versão 3.2: Adicionado suporte para thread.lock,
threading.Lock e objetos código.

Vários tipos embutidos como "list" e "dict" não oferecem suporta
diretamente a referências fracas, mas podem adicionar suporte através
de subclasses:

   class Dict(dict):
       pass

   obj = Dict(red=1, green=2, blue=3)   # este objeto é potencialmente fracamente referenciável

Outros tipos embutidos como "tuple" e "int" não oferecem suporte a
referências fracas mesmo em subclasses.

Os tipos de extensão podem ser facilmente criados para oferecer
suporte a referências fracas; veja Weak Reference Support.

Quando "__slots__" são definidos para um determinado tipo, o suporte a
referência fraca é desativado a menos que uma string "'__weakref__'"
também esteja presente na sequência de strings na declaração de
"__slots__". Veja a documentação de __slots__ para detalhes.

class weakref.ref(object[, callback])

   Retorna uma referência fraca para *object*. O objeto original pode
   ser recuperado chamando o objeto referência se o referente ainda
   estiver ativo; se o referente não estiver mais ativo, chamar o
   objeto referência fará com que "None" seja retornado. Se *callback*
   for fornecido e não for "None", e o objeto referência fraca
   retornado ainda estiver ativo, o função de retorno será chamada
   quando o objeto estiver prestes a ser finalizado; o objeto
   referência fraca será passado como único parâmetro para a função de
   retorno; o referente não estará mais disponível.

   É permitido que muitas referências fracas sejam construídas para o
   mesmo objeto. As funções de retorno registradas para cada
   referência fraca serão chamadas da função de retorno registrada
   mais recentemente para a função de retorno registrada mais antiga.

   As exceções levantadas pela função de retorno serão anotadas na
   saída de erro padrão, mas não poderão ser propagadas; elas são
   tratadas exatamente da mesma maneira que as exceções levantadas
   pelo método "__del__()" de um objeto.

   Referências fracas são *hasheáveis* se o *object* for hasheável.
   Elas manterão seu valor de hash mesmo depois que *object* for
   excluído. Se "hash()" for chamada pela primeira vez somente após o
   *object* ter sido excluído, a chamada vai levantar "TypeError".

   Referências fracas oferecem suporte a testes de igualdade, mas não
   de ordenação. Se os referentes ainda estiverem vivos, duas
   referências terão a mesma relação de igualdade que seus referentes
   (independentemente do *callback*). Se um dos referentes tiver sido
   excluído, as referências serão iguais somente se os objetos
   referência forem o mesmo objeto.

   Este é um tipo do qual pode ser feita subclasse em vez de uma
   função de fábrica.

   Referências fracas são genéricas em relação ao tipo do objeto ao
   qual se referem.

   __callback__

      Este atributo somente leitura retorna a função de retorno
      atualmente associada à referência fraca. Se não houver função de
      retorno ou se o referente da referência fraca não estiver mais
      ativo, então este atributo terá o valor "None".

   Alterado na versão 3.4: Adicionado o atributo "__callback__".

weakref.proxy(object[, callback])

   Retorna um intermediário (proxy, em inglês) para *object* que usa
   uma referência fraca. Isto provê suporte ao uso do intermediário na
   maioria dos contextos, em vez de exigir a desreferenciação
   explícita usada com objetos de referência fraca. O objeto retornado
   terá um tipo "ProxyType" ou "CallableProxyType", dependendo se
   *object* é chamável. Objetos intermediários não são *hasheáveis*
   independentemente do referente; isso evita uma série de problemas
   relacionados à sua natureza fundamentalmente mutável e impede seu
   uso como chaves de dicionário. *callback* é igual ao parâmetro de
   mesmo nome da função "ref()".

   Acessar um atributo do objeto intermediário depois que o referente
   é coletado como lixo levanta "ReferenceError".

   Alterado na versão 3.8: Estendeu o suporte ao operador em objetos
   intermediários para incluir os operadores "@" e "@=" para
   multiplicação de matrizes.

weakref.getweakrefcount(object)

   Retorna o número de referências fracas e intermediários que fazem
   referência a *object*.

weakref.getweakrefs(object)

   Retorna uma lista de todos os objetos intermediários e de
   referência fraca que fazem referência a *object*.

class weakref.WeakKeyDictionary([dict])

   Classe de mapeamento que faz referência fraca a chaves. Entradas no
   dicionário serão descartadas quando não houver mais uma referência
   forte à chave. Isso pode ser usado para associar dados adicionais a
   um objeto de propriedade de outras partes de uma aplicação sem
   adicionar atributos a esses objetos. Isso pode ser especialmente
   útil com objetos que substituem acessos de atributos.

   Note que quando uma chave com valor igual a uma chave existente
   (mas não identidade igual) é inserida no dicionário, ela substitui
   o valor, mas não substitui a chave existente. Devido a isso, quando
   a referência à chave original é excluída, ela também exclui a
   entrada no dicionário:

      >>> class T(str): pass
      ...
      >>> k1, k2 = T(), T()
      >>> d = weakref.WeakKeyDictionary()
      >>> d[k1] = 1   # d = {k1: 1}
      >>> d[k2] = 2   # d = {k1: 2}
      >>> del k1      # d = {}

   Uma solução alternativa seria remover a chave antes da
   reatribuição:

      >>> class T(str): pass
      ...
      >>> k1, k2 = T(), T()
      >>> d = weakref.WeakKeyDictionary()
      >>> d[k1] = 1   # d = {k1: 1}
      >>> del d[k1]
      >>> d[k2] = 2   # d = {k2: 2}
      >>> del k1      # d = {k2: 2}

   Alterado na versão 3.9: Adicionado suporte para operadores "|" e
   "|=", conforme especificado na **PEP 584**.

Objetos "WeakKeyDictionary" têm um método adicional que expõe as
referências internas diretamente. Não há garantia de que as
referências estejam "ativas" no momento em que são usadas, então o
resultado da chamada das referências precisa ser verificado antes de
ser usado. Isso pode ser usado para evitar a criação de referências
que farão com que o coletor de lixo mantenha as chaves por mais tempo
do que o necessário.

WeakKeyDictionary.keyrefs()

   Retorna um iterável das referências fracas às chaves.

class weakref.WeakValueDictionary([dict])

   Classe de mapeamento que faz referência fraca a valores. Entradas
   no dicionário serão descartadas quando nenhuma referência forte ao
   valor existir mais.

   Alterado na versão 3.9: Adicionado suporte para operadores "|" e
   "|=", conforme especificado na **PEP 584**.

Os objetos "WeakValueDictionary" têm um método adicional que apresenta
os mesmos problemas que o método "WeakKeyDictionary.keyrefs()".

WeakValueDictionary.valuerefs()

   Retorna um iterável das referências fracas aos valores.

class weakref.WeakSet([elements])

   Define a classe que mantém referências fracas para seus elementos.
   Um elemento será descartado quando nenhuma referência forte a ele
   existir mais.

class weakref.WeakMethod(method[, callback])

   Uma subclasse personalizada de "ref" que simula uma referência
   fraca a um método vinculado (ou seja, um método definido em uma
   classe e pesquisado em uma instância). Como um método vinculado é
   efêmero, uma referência fraca padrão não pode mantê-lo.
   "WeakMethod" tem um código especial para recriar o método vinculado
   até que o objeto ou a função original morra:

      >>> class C:
      ...     def method(self):
      ...         print("method called!")
      ...
      >>> c = C()
      >>> r = weakref.ref(c.method)
      >>> r()
      >>> r = weakref.WeakMethod(c.method)
      >>> r()
      <bound method C.method of <__main__.C object at 0x7fc859830220>>
      >>> r()()
      method called!
      >>> del c
      >>> gc.collect()
      0
      >>> r()
      >>>

   *callback* é o mesmo que o parâmetro de mesmo nome da função
   "ref()".

   Adicionado na versão 3.4.

class weakref.finalize(obj, func, /, *args, **kwargs)

   Retorna um objeto finalizador chamável que será chamado quando
   *obj* for coletado como lixo. Diferentemente de uma referência
   fraca comum, um finalizador sempre sobreviverá até que o objeto
   referência seja coletado, simplificando muito o gerenciamento do
   ciclo de vida.

   Um finalizador é considerado *alive* (vivo) até ser chamado
   (explicitamente ou na coleta de lixo), e depois disso ele é *dead*
   (morto). Chamar um finalizador vivo retorna o resultado da
   avaliação de "func(*arg, **kwargs)", enquanto chamar um finalizador
   morto retorna "None".

   Exceções levantadas por funções de retorno do finalizador durante a
   coleta de lixo serão mostradas na saída de erro padrão, mas não
   podem ser propagadas. Elas são tratadas da mesma forma que exceções
   levantadas de um método "__del__()" de um objeto ou de uma função
   de retorno da referência fraca.

   Quando o programa é encerrado (ou mais genericamente, no
   *desligamento do interpretador*), cada finalizador vivo restante é
   chamado, a menos que seu atributo "atexit" tenha sido definido como
   falso. Eles são chamados na ordem reversa da criação.

   Um finalizador nunca vai invocar sua função de retorno durante a
   parte posterior do *desligamento do interpretador* quando os
   globais do módulo podem ter sido substituídos por "None".

   __call__()

      Se *self* estiver vivo, marca-o como morto e retorna o resultado
      da chamada "func(*args, **kwargs)". Se *self* estiver morto,
      retorna "None".

   detach()

      Se *self* estiver vivo, marca-o como morto e retorna a tupla
      "(obj, func, args, kwargs)". Se *self* estiver morto, retorna
      "None".

   peek()

      Se *self* estiver vivo, retorna a tupla "(obj, func, args,
      kwargs)". Se *self* estiver morto, retorna "None".

   alive

      Propriedade que é verdadeiro se o finalizador estiver ativo,
      falsa caso contrário.

   atexit

      Uma propriedade booleana gravável que por padrão é verdadeiro.
      No *desligamento do interpretador*, todos os finalizadores vivos
      restantes para os quais "atexit" é verdadeiro são chamados na
      ordem reversa da criação.

   Nota:

     É importante garantir que *func*, *args* e *kwargs* não possuam
     nenhuma referência a *obj*, direta ou indiretamente, pois, caso
     contrário, *obj* nunca será coletado como lixo. Em particular,
     *func* não deve ser um método vinculado de *obj*.

   Adicionado na versão 3.4.

class weakref.ReferenceType

   O objeto tipo para objetos referências fracas.

class weakref.ProxyType

   O tipo de objeto para intermediários de objetos que não são
   chamáveis.

class weakref.CallableProxyType

   O objeto de tipo para intermediários de objetos chamáveis.

weakref.ProxyTypes

   Sequência contendo todos os objetos de tipo para intermediários.
   Isso pode tornar mais simples testar se um objeto é um
   intermediário sem depender da nomeação de ambos os tipos de
   intermediário.

Ver também:

  **PEP 205** - Referências fracas
     A proposta e a justificativa para esse recurso, incluindo links
     para implementações anteriores e informações sobre recursos
     semelhantes em outras linguagens.


Objetos referência fraca
========================

Objetos referência fraca não têm métodos nem atributos além de
"ref.__callback__". Um objeto referência fraca permite que o referente
seja obtido, se ele ainda existir, chamando-o:

>>> import weakref
>>> class Object:
...     pass
...
>>> o = Object()
>>> r = weakref.ref(o)
>>> o2 = r()
>>> o is o2
True

Se o referente não existir mais, chamar o objeto referência retornará
"None":

>>> del o, o2
>>> print(r())
None

O teste de se um objeto referência fraca ainda está vivo deve ser
feito usando a expressão "ref() is not None". Normalmente, o código da
aplicação que precisa usar um objeto de referência deve seguir este
padrão:

   # r é um objeto referência fraca
   o = r()
   if o is None:
       # referente foi coletado como lixo
       print("O objeto foi desalocado; não é possível mexer com ele.")
   else:
       print("O objeto ainda está vivo!")
       o.faz_algo_útil()

Usar um teste separado para "vivacidade" cria condições de corrida em
aplicações que usam mais de uma thread; uma outra thread pode fazer
com que uma referência fraca seja invalidada antes que a referência
fraca seja chamada; o idioma mostrado acima é seguro em aplicações que
usam mais de uma thread, bem como em aplicações de thread única.

Versões especializadas de objetos "ref" podem ser criadas por meio de
subclasse. Isso é usado na implementação do "WeakValueDictionary" para
reduzir a sobrecarga de memória para cada entrada no mapeamento. Isso
pode ser mais útil para associar informações adicionais a uma
referência, mas também pode ser usado para inserir processamento
adicional em chamadas para recuperar o referente.

Este exemplo mostra como uma subclasse de "ref" pode ser usada para
armazenar informações adicionais sobre um objeto e afetar o valor
retornado quando o referente é acessado:

   import weakref

   class ExtendedRef(weakref.ref):
       def __init__(self, ob, callback=None, /, **annotations):
           super().__init__(ob, callback)
           self.__counter = 0
           for k, v in annotations.items():
               setattr(self, k, v)

       def __call__(self):
           """Retorna um par contendo o referente e o número de
           vezes que a referência foi chamada.
           """
           ob = super().__call__()
           if ob is not None:
               self.__counter += 1
               ob = (ob, self.__counter)
           return ob


Exemplo
=======

Este exemplo simples mostra como uma aplicação pode usar IDs de objeto
para recuperar objetos que ele viu antes. Os IDs dos objetos podem
então ser usados em outras estruturas de dados sem forçar os objetos a
permanecerem vivos, mas os objetos ainda podem ser recuperados por ID
se o fizerem.

   import weakref

   _id2obj_dict = weakref.WeakValueDictionary()

   def remember(obj):
       oid = id(obj)
       _id2obj_dict[oid] = obj
       return oid

   def id2obj(oid):
       return _id2obj_dict[oid]


Objetos finalizadores
=====================

O principal benefício de usar "finalize" é que ele simplifica o
registro de um retorno de chamada sem precisar preservar o objeto
finalizador retornado. Por exemplo

>>> import weakref
>>> class Object:
...     pass
...
>>> kenny = Object()
>>> weakref.finalize(kenny, print, "You killed Kenny!")
<finalize object at ...; for 'Object' at ...>
>>> del kenny
You killed Kenny!

O finalizador pode ser chamado diretamente também. No entanto, o
finalizador vai invocar a função de retorno no máximo uma vez.

>>> def callback(x, y, z):
...     print("CALLBACK")
...     return x + y + z
...
>>> obj = Object()
>>> f = weakref.finalize(obj, callback, 1, 2, z=3)
>>> assert f.alive
>>> assert f() == 6
CALLBACK
>>> assert not f.alive
>>> f()                     # callback not called because finalizer dead
>>> del obj                 # callback not called because finalizer dead

Você pode desfazer o registro de um finalizador usando seu método
"detach()". Isso elimina o finalizador e retorna os argumentos
passados ao construtor quando ele foi criado.

>>> obj = Object()
>>> f = weakref.finalize(obj, callback, 1, 2, z=3)
>>> f.detach()
(<...Object object ...>, <function callback ...>, (1, 2), {'z': 3})
>>> newobj, func, args, kwargs = _
>>> assert not f.alive
>>> assert newobj is obj
>>> assert func(*args, **kwargs) == 6
CALLBACK

A menos que você defina o atributo "atexit" como "False", um
finalizador será chamado quando o programa sair se ele ainda estiver
vivo. Por exemplo

   >>> obj = Object()
   >>> weakref.finalize(obj, print, "obj dead or exiting")
   <finalize object at ...; for 'Object' at ...>
   >>> exit()
   obj dead or exiting


Comparando finalizadores com métodos "__del__()"
================================================

Suponha que queremos criar uma classe cujas instâncias representam
diretórios temporários. Os diretórios devem ser excluídos com seus
conteúdos quando o primeiro dos seguintes eventos ocorrer:

* o objeto é um lixo coletado,

* o método "remove()" do objeto é chamado, ou

* o programa finaliza.

Podemos tentar implementar a classe usando um método "__del__()" da
seguinte maneira:

   class TempDir:
       def __init__(self):
           self.name = tempfile.mkdtemp()

       def remove(self):
           if self.name is not None:
               shutil.rmtree(self.name)
               self.name = None

       @property
       def removed(self):
           return self.name is None

       def __del__(self):
           self.remove()

A partir do Python 3.4, os métodos "__del__()" não impedem mais que os
ciclos de referência sejam coletados como lixo, e os módulos globais
não são mais forçados a "None" durante *desligamento do
interpretador*. Então, esse código deve funcionar sem problemas no
CPython.

Entretanto, o tratamento dos métodos "__del__()" é notoriamente
específico da implementação, pois depende de detalhes internos da
implementação do coletor de lixo do interpretador.

Uma alternativa mais robusta pode ser definir um finalizador que faça
referência apenas às funções e objetos específicos de que necessita,
em vez de ter acesso ao estado completo do objeto:

   class TempDir:
       def __init__(self):
           self.name = tempfile.mkdtemp()
           self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

       def remove(self):
           self._finalizer()

       @property
       def removed(self):
           return not self._finalizer.alive

Definido assim, nosso finalizador recebe apenas uma referência aos
detalhes que ele precisa para limpar o diretório apropriadamente. Se o
objeto nunca for coletado como lixo, o finalizador ainda será chamado
na saída.

A outra vantagem dos finalizadores baseados em referências fracas é
que eles podem ser usados para registrar finalizadores para classes
onde a definição é controlada por terceiros, como executar código
quando um módulo é descarregado:

   import weakref, sys
   def unloading_module():
       # referência implícita aos globais do módulo do corpo da função
   weakref.finalize(sys.modules[__name__], unloading_module)

Nota:

  Se você criar um objeto finalizador em uma thread em um daemon assim
  que o programa sair, então há a possibilidade de que o finalizador
  não seja chamado na saída. No entanto, em um thread em um daemon
  "atexit.register()", "try: ... finally: ..." e "with: ..." não
  garantem que a limpeza ocorra também.
