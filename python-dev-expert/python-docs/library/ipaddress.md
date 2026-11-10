"ipaddress" --- Biblioteca de manipulação de IPv4/IPv6
******************************************************

**Código-fonte:** Lib/ipaddress.py

======================================================================

"ipaddress" fornece recursos para criar, manipular e operar em
endereços e redes IPv4 e IPv6.

As funções e classes neste módulo facilitam o tratamento de várias
tarefas relacionadas a endereços IP, incluindo verificar se dois hosts
estão ou não na mesma sub-rede, iterar sobre todos os hosts em uma
sub-rede específica, verificar se uma string representa ou não um
valor válido. Endereço IP ou definição de rede e assim por diante.

Esta é a referência completa da API do módulo -- para uma visão geral
e introdução, consulte Uma introdução ao módulo ipaddress.

Adicionado na versão 3.3.


Funções de fábrica de conveniência
==================================

O módulo "ipaddress" fornece funções de fábrica para criar endereços
IP, redes e interfaces de forma conveniente:

ipaddress.ip_address(address)

   Retorna um objeto "IPv4Address" ou "IPv6Address" dependendo do
   endereço IP passado como argumento.  Podem ser fornecidos endereços
   IPv4 ou IPv6;  números inteiros menores que "2**32" serão
   considerados IPv4 por padrão. Uma exceção "ValueError" é levantada
   se *address* não representar um endereço IPv4 ou IPv6 válido.

   >>> ipaddress.ip_address('192.168.0.1')
   IPv4Address('192.168.0.1')
   >>> ipaddress.ip_address('2001:db8::')
   IPv6Address('2001:db8::')

ipaddress.ip_network(address, strict=True)

   Retorna um objeto "IPv4Network" ou "IPv6Network" dependendo do
   endereço IP passado como argumento. *address* é uma string ou
   número inteiro que representa a rede IP. Podem ser fornecidas redes
   IPv4 ou IPv6; números inteiros menores que "2**32" serão
   considerados IPv4 por padrão. *strict* é passado para o construtor
   "IPv4Network" ou "IPv6Network". Uma exceção "ValueError" é
   levantada se *address* não representar um endereço IPv4 ou IPv6
   válido, ou se a rede tiver bits de host configurados.

   >>> ipaddress.ip_network('192.168.0.0/28')
   IPv4Network('192.168.0.0/28')

ipaddress.ip_interface(address)

   Retorna um objeto "IPv4Interface" ou "IPv6Interface" dependendo do
   endereço IP passado como argumento.  *address* é uma string ou um
   inteiro representando o endereço IP. Podem ser fornecidos endereços
   IPv4 ou IPv6;  números inteiros menores que "2**32" serão
   considerados IPv4 por padrão. Uma exceção "ValueError" é levantada
   se *address* não representar um endereço IPv4 ou IPv6 válido.

Uma desvantagem dessas funções de conveniência é que a necessidade de
lidar com os formatos IPv4 e IPv6 significa que as mensagens de erro
fornecem informações mínimas sobre o erro exato, pois as funções não
sabem se o formato IPv4 ou IPv6 foi pretendido. Relatórios de erros
mais detalhados podem ser obtidos chamando diretamente os construtores
de classe específicos da versão apropriada.


Endereços IP
============


Objetos de endereço
-------------------

Os objetos "IPv4Address" e "IPv6Address" compartilham muitos atributos
comuns. Alguns atributos que são significativos apenas para endereços
IPv6 também são implementados por objetos "IPv4Address", para
facilitar a escrita de código que lide corretamente com ambas as
versões de IP. Os objetos de endereço são *hasheáveis*, portanto podem
ser usados como chaves em dicionários.

class ipaddress.IPv4Address(address)

   Constrói um endereço IPv4. Uma exceção "AddressValueError" é
   levantada se *address* não for um endereço IPv4 válido.

   O seguinte constitui um endereço IPv4 válido:

   1. Uma string em notação decimal por ponto, consistindo de quatro
      inteiros decimais em um intervalo inclusivo 0--255 separado por
      pontos (e.g. "192.168.0.1"). Cada inteiro representa um octeto
      (byte) no endereço. Zeros à esquerda não são tolerados para
      evitar confusão com notação octal.

   2. Um inteiro que cabe em 32 bits.

   3. Um inteiro compactado em um objeto "bytes" de comprimento 4
      (octeto mais significativo primeiro).

   >>> ipaddress.IPv4Address('192.168.0.1')
   IPv4Address('192.168.0.1')
   >>> ipaddress.IPv4Address(3232235521)
   IPv4Address('192.168.0.1')
   >>> ipaddress.IPv4Address(b'\xC0\xA8\x00\x01')
   IPv4Address('192.168.0.1')

   Alterado na versão 3.8: Zeros à esquerda são tolerados, mesmo em
   casos ambíguos que se parecem com notação octal.

   Alterado na versão 3.9.5: Zeros à esquerda não são mais tolerados e
   são tratados como um erro. As strings de endereço IPv4 agora são
   analisadas de forma tão estrita quanto glibc "inet_pton()".

   version

      O número de versão apropriado: "4" para IPv4, "6" para IPv6.

      Alterado na versão 3.14: Disponibilizado na classe.

   max_prefixlen

      O número total de bits na representação de endereço para esta
      versão: "32" para IPv4, "128" para IPv6.

      O prefixo define o número de bits iniciais em um endereço que
      são comparados para determinar se um endereço faz ou não parte
      de uma rede.

      Alterado na versão 3.14: Disponibilizado na classe.

   compressed

   exploded

      A representação de string em notação decimal pontilhada. Zeros à
      esquerda nunca são incluídos na representação.

      Como o IPv4 não define uma notação abreviada para endereços com
      octetos definidos como zero, esses dois atributos são sempre
      iguais a "str(addr)" para endereços IPv4. A exposição desses
      atributos facilita a gravação de código de exibição que pode
      tratar endereços IPv4 e IPv6.

   packed

      A representação binária deste endereço -- um objeto "bytes" de
      comprimento apropriado (primeiro o octeto mais significativo).
      São 4 bytes para IPv4 e 16 bytes para IPv6.

   reverse_pointer

      O nome do registro PTR de DNS reverso para o endereço IP, por
      exemplo:

         >>> ipaddress.ip_address("127.0.0.1").reverse_pointer
         '1.0.0.127.in-addr.arpa'
         >>> ipaddress.ip_address("2001:db8::1").reverse_pointer
         '1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'

      Este é o nome que pode ser usado para realizar uma pesquisa PTR,
      não o nome do host resolvido em si.

      Adicionado na versão 3.5.

   is_multicast

      "True" se o endereço estiver reservado para uso multicast.
      Consulte **RFC 3171** (para IPv4) ou **RFC 2373** (para IPv6).

   is_private

      "True" se o endereço for definido como não acessível globalmente
      por iana-ipv4-special-registry (para IPv4) ou iana-ipv6-special-
      registry (para IPv6) com as seguintes exceções:

      * "is_private" é "False" para o espaço de endereço compartilhado
        ("100.64.0.0/10")

      * Para endereços IPv6 mapeados em IPv4, o valor "is_private" é
        determinado pela semântica dos endereços IPv4 subjacentes e a
        seguinte condição é válida (consulte
        "IPv6Address.ipv4_mapped"):

           address.is_private == address.ipv4_mapped.is_private

      "is_private" tem valor oposto a "is_global", exceto para o
      espaço de endereço compartilhado (intervalo "100.64.0.0/10")
      onde ambos são "False".

      Alterado na versão 3.13: Corrigidos alguns falsos positivos e
      falsos negativos.

      * "192.0.0.0/24" é considerado privado com exceção de
        "192.0.0.9/32" e "192.0.0.10/32" (anteriormente: apenas o sub-
        intervalo "192.0.0.0/29" foi considerado privado).

      * "64:ff9b:1::/48" é considerado privado.

      * "2002::/16" é considerado privado.

      * Existem exceções em "2001::/23" (de outra forma considerado
        privado): "2001:1::1/128", "2001:1::2/128", "2001:3::/32",
        "2001:4:112::/48", "2001:20::/28", "2001:30::/28". As exceções
        não são consideradas privadas.

   is_global

      "True" se o endereço for definido como não acessível globalmente
      por iana-ipv4-special-registry (para IPv4) ou iana-ipv6-special-
      registry (para IPv6) com a seguinte exceção:

      Para endereços IPv6 mapeados em IPv4, o valor "is_private" é
      determinado pela semântica dos endereços IPv4 subjacentes e a
      seguinte condição é válida (consulte "IPv6Address.ipv4_mapped"):

         address.is_global == address.ipv4_mapped.is_global

      "is_global" tem valor oposto a "is_private", exceto para o
      espaço de endereço compartilhado (intervalo "100.64.0.0/10")
      onde ambos são "False".

      Adicionado na versão 3.4.

      Alterado na versão 3.13: Corrigidos alguns falsos positivos e
      falsos negativos, veja "is_private" para detalhes.

   is_unspecified

      "True" se o endereço não estiver especificado. Consulte **RFC
      5735** (para IPv4) ou **RFC 2373** (para IPv6).

   is_reserved

      "True" se o endereço for indicado como reservado pela IETF. Para
      IPv4, este é apenas "240.0.0.0/4", o bloco de endereços
      "Reserved". Para IPv6, este é todos os endereços alocados como
      "Reserved by IETF" para uso futuro.

      Nota:

        Para IPv4, "is_reserved" não está relacionado ao valor do
        bloco de endereço da coluna "Reserved-by-Protocol" em iana-
        ipv4-special-registry.

      Cuidado:

        Para IPv6, "fec0::/10" um antigo prefixo de endereço de escopo
        Site-Local está atualmente excluído dessa lista (veja
        "is_site_local" & **RFC 3879**).

   is_loopback

      "True" se este for um endereço de loopack. Consulte **RFC 3330**
      (para IPv4) ou **RFC 2373** (para IPv6).

   is_link_local

      "True" se o endereço está reservado para uso de link local.
      Veja: **RFC 3927**.

   ipv6_mapped

      Objeto "IPv6Address" representando o endereço IPv6 mapeado para
      IPv6. Veja **RFC 4291**.

      Adicionado na versão 3.13.

IPv4Address.__format__(fmt)

   Retorna a representação string do endereço de IP, controlado por
   uma string de formato explícito. *fmt* pode ser um dos seguintes:
   "'s'", a opção padrão, equivalente à "str()", "'b'" para uma string
   binária preenchida com zeros, "'X'" ou "'x'" para uma representação
   hexadecimal maiúscula ou minúscula, ou "'n'", que equivale a "'b'"
   para endereços IPv4 e "'x'" para IPv6. Para representações binárias
   e hexadecimais, o especificador de forma "'#'" e a opção de
   agrupamento "'_'" estão disponíveis. "__format__" é utilizado por
   "format", "str.format" e f-strings.

   >>> format(ipaddress.IPv4Address('192.168.0.1'))
   '192.168.0.1'
   >>> '{:#b}'.format(ipaddress.IPv4Address('192.168.0.1'))
   '0b11000000101010000000000000000001'
   >>> f'{ipaddress.IPv6Address("2001:db8::1000"):s}'
   '2001:db8::1000'
   >>> format(ipaddress.IPv6Address('2001:db8::1000'), '_X')
   '2001_0DB8_0000_0000_0000_0000_0000_1000'
   >>> '{:#_n}'.format(ipaddress.IPv6Address('2001:db8::1000'))
   '0x2001_0db8_0000_0000_0000_0000_0000_1000'

   Adicionado na versão 3.9.

class ipaddress.IPv6Address(address)

   Constrói um endereço IPv6. Uma exceção "AddressValueError" é
   levantada se *address* não for um endereço IPv6 válido.

   O seguinte constitui um endereço IPv6 válido:

   1. Uma string constituída de oito grupos de quatro dígitos
      hexadecimais, cada grupo representando 16 bits. Os grupos são
      separados por dois pontos. Isto descreve uma notação *explodida*
      (longa); A string também pode ser *compactada* (notação curta)
      por vários meios. Ver **RFC 4291** para detalhes. Por exemplo,
      ""0000:0000:0000:0000:0000:0abc:0007:0def"" pode ser compactada
      para ""::abc:7:def"".

      Opcionalmente, a string pode ter um ID de escopo de zona,
      expressado por um sufixo "%scope_id". Se presente, o ID de
      escopo deve ser não vazio, e pode não conter "%". Ver **RFC
      4007** para detalhes. Por exemplo, "fe80::1234%1" pode
      identificar o endereço "fe80::1234" no primeiro link do nó.

   2. Um inteiro que cabe em 128 bits.

   3. Um inteiro compactado em um objeto "bytes" de comprimento 16,
      big-endian.

   >>> ipaddress.IPv6Address('2001:db8::1000')
   IPv6Address('2001:db8::1000')
   >>> ipaddress.IPv6Address('ff02::5678%1')
   IPv6Address('ff02::5678%1')

   compressed

   A forma curta da representação do endereço, com zeros à esquerda em
   grupos omitidos e a sequência mais longa de grupos consistida
   inteiramente por zeros colapsada em um grupo vazio único.

   Este também é o valor retornado por "str(addr)" para endereços
   IPv6.

   exploded

   A forma longa da representação do endereço, com todos zeros à
   esquerda em grupos consistindo inteiramente de zeros incluídos.

   Para os seguintes atributos e métodos, veja a documentação
   correspondente para a classe "IPv4Address":

   packed

   reverse_pointer

   version

   max_prefixlen

   is_multicast

   is_private

   is_global

      Adicionado na versão 3.4.

   is_unspecified

   is_reserved

   is_loopback

   is_link_local

   is_site_local

      "True" se o endereço estiver reservado para uso local do site.
      Observe que o espaço de endereço local do site foi descontinuado
      pelo **RFC 3879**. Use "is_private" para testar se este endereço
      está no espaço de endereços locais exclusivos conforme definido
      pelo **RFC 4193**.

   ipv4_mapped

      Para endereços que aparentam ser endereços mapeados para IPv4 no
      intervalo "::FFFF:0:0/96" conforme definido pela **RFC 4291**,
      esta propriedade relata o endereço IPv4 embutido. Para qualquer
      outro endereço, esta propriedade será "None".

   scope_id

      Para endereços com escopo definido pelo **RFC 4007**, esta
      propriedade identifica a zona específica do escopo do endereço à
      qual o endereço pertence, como uma string. Quando nenhuma zona
      de escopo for especificada, esta propriedade será "None".

   sixtofour

      Para endereços que parecem ser endereços 6to4 (começando com
      "2002::/16"), como definido pelo **RFC 3056**, esta propriedade
      reportará o endereço IPv4 incorporado. Para qualquer outro
      endereço, esta propriedade será "None".

   teredo

      Para endereços que parecem ser endereços Teredo (começando com
      "2001::/32"), como definido pelo **RFC 4380**, esta propriedade
      reportará o par de endereços "(server, client)" incorporado.
      Para qualquer outro endereço, esta propriedade será "None".

IPv6Address.__format__(fmt)

   Consulte a documentação do método correspondente em "IPv4Address".

   Adicionado na versão 3.9.


Conversão para strings e inteiros
---------------------------------

Para interoperar com interfaces de rede, como o módulo de soquete, os
endereços devem ser convertidos em strings ou inteiros. Isso é tratado
usando as funções internas "str()" e "int()":

   >>> str(ipaddress.IPv4Address('192.168.0.1'))
   '192.168.0.1'
   >>> int(ipaddress.IPv4Address('192.168.0.1'))
   3232235521
   >>> str(ipaddress.IPv6Address('::1'))
   '::1'
   >>> int(ipaddress.IPv6Address('::1'))
   1

Observe que os endereços com escopo IPv6 são convertidos em números
inteiros sem ID de zona de escopo.


Operadores
----------

Os objetos de endereço têm suporte a alguns operadores. Salvo
indicação em contrário, os operadores só podem ser aplicados entre
objetos compatíveis (ou seja, IPv4 com IPv4, IPv6 com IPv6).


Operadores de comparação
~~~~~~~~~~~~~~~~~~~~~~~~

Os objetos de endereço podem ser comparados com o conjunto usual de
operadores de comparação. Os mesmos endereços IPv6 com IDs de zona de
escopo diferentes não são iguais. Alguns exemplos:

   >>> IPv4Address('127.0.0.2') > IPv4Address('127.0.0.1')
   True
   >>> IPv4Address('127.0.0.2') == IPv4Address('127.0.0.1')
   False
   >>> IPv4Address('127.0.0.2') != IPv4Address('127.0.0.1')
   True
   >>> IPv6Address('fe80::1234') == IPv6Address('fe80::1234%1')
   False
   >>> IPv6Address('fe80::1234%1') != IPv6Address('fe80::1234%2')
   True


Operadores aritméticos
~~~~~~~~~~~~~~~~~~~~~~

Inteiros podem ser adicionados ou subtraídos de objetos de endereço.
Alguns exemplos:

   >>> IPv4Address('127.0.0.2') + 3
   IPv4Address('127.0.0.5')
   >>> IPv4Address('127.0.0.2') - 3
   IPv4Address('126.255.255.255')
   >>> IPv4Address('255.255.255.255') + 1
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ipaddress.AddressValueError: 4294967296 (>= 2**32) is not permitted as an IPv4 address


Definições de rede IP
=====================

Os objetos "IPv4Network" e "IPv6Network" fornecem um mecanismo para
definir e inspecionar definições de rede IP. Uma definição de rede
consiste em uma *máscara* e um *endereço de rede* e, como tal, define
um intervalo de endereços IP que é igual ao endereço de rede quando
mascarado (E binário) com a máscara. Por exemplo, uma definição de
rede com a máscara "255.255.255.0" e o endereço de rede "192.168.1.0"
consiste em endereços IP no intervalo inclusivo "192.168.1.0" a
"192.168.1.255".


Prefixo, máscara de rede e máscara de host
------------------------------------------

Existem várias maneiras equivalentes de especificar máscaras de rede
IP. Um *prefixo* "/<nbits>" é uma notação que denota quantos bits de
ordem superior estão definidos na máscara de rede. Uma máscara de
rede, ou *netmask*, é um endereço IP com um certo número de bits de
alta ordem definidos. Assim o prefixo "/24" é equivalente à máscara de
rede "255.255.255.0" em IPv4, ou "ffff:ff00::" em IPv6. Além disso,
uma máscara de host, ou *host mask*, é o inverso lógico de uma máscara
de rede e às vezes é usada (por exemplo, nas listas de controle de
acesso da Cisco) para denotar uma máscara de rede. A máscara de host
equivalente a "/24" em IPv4 é "0.0.0.255".


Objetos de rede
---------------

Todos os atributos implementados por objetos de endereço também são
implementados por objetos de rede. Além disso, os objetos de rede
implementam atributos adicionais. Todos estes são comuns entre
"IPv4Network" e "IPv6Network", portanto, para evitar duplicação, eles
são documentados apenas para "IPv4Network". Objetos de rede são
*hasheáveis*, portanto podem ser usados como chaves em dicionários.

class ipaddress.IPv4Network(address, strict=True)

   Constrói uma definição de rede IPv4. *address* pode ser um dos
   seguintes:

   1. Uma string que consiste em um endereço IP e uma máscara
      opcional, separados por uma barra ("/"). O endereço IP é o
      endereço de rede, e a máscara pode ser um único número, o que
      significa que é um *prefixo*, ou uma representação de string de
      um endereço IPv4. Se for o último, a máscara será interpretada
      como uma *máscara de rede* se começar com um campo diferente de
      zero, ou como uma *máscara de host* se começar com um campo
      zero, com a única exceção de uma máscara totalmente zero que é
      tratada como uma *máscara de rede*. Se nenhuma máscara for
      fornecida, será considerada "/32".

      Por exemplo, as seguintes especificações de *address* são
      equivalentes: "192.168.1.0/24", "192.168.1.0/255.255.255.0" e
      "192.168.1.0/0.0.0.255".

   2. Um número inteiro que cabe em 32 bits. Isto é equivalente a uma
      rede de endereço único, com o endereço de rede sendo *address* e
      a máscara sendo "/32".

   3. Um inteiro compactado em um objeto "bytes" de comprimento 4,
      big-endian. A interpretação é semelhante a um *address* no
      formato inteiro.

   4. Uma tupla de dois elementos de uma descrição de endereço e uma
      máscara de rede, onde a descrição do endereço é uma string, um
      número inteiro de 32 bits, um número inteiro compactado de 4
      bytes ou um objeto "IPv4Address" existente; e a máscara de rede
      é um número inteiro que representa o comprimento do prefixo (por
      exemplo, "24") ou uma string que representa a máscara do prefixo
      (por exemplo, "255.255.255.0").

   Uma exceção "AddressValueError" é levantada se *address* não for um
   endereço IPv4 válido. Uma exceção "NetmaskValueError" é levantada
   se a máscara não for válida para um endereço IPv4.

   Se *strict* for "True" e os bits do host estiverem definidos no
   endereço fornecido, então "ValueError" será levantada. Caso
   contrário, os bits do host serão mascarados para determinar o
   endereço de rede apropriado.

   Salvo indicação em contrário, todos os métodos de rede que aceitam
   outros objetos rede/endereço irão levantar "TypeError" se a versão
   IP do argumento for incompatível com "self".

   Alterado na versão 3.5: Adicionado o formulário de tupla de 2
   elementos para o parâmetro do construtor *address*.

   version

   max_prefixlen

      Consulte a documentação do atributo correspondente em
      "IPv4Address".

   is_multicast

   is_private

   is_unspecified

   is_reserved

   is_loopback

   is_link_local

      Esses atributos terão valor verdadeiro para a rede como um todo
      se forem verdadeiros tanto para o endereço de rede quanto para o
      endereço de broadcast.

   network_address

      O endereço de rede da rede. O endereço de rede e o comprimento
      do prefixo juntos definem exclusivamente uma rede.

   broadcast_address

      O endereço de broadcast da rede. Os pacotes enviados para o
      endereço de broadcast devem ser recebidos por todos os hosts da
      rede.

   hostmask

      A máscara do host, como um objeto "IPv4Address".

   netmask

      A máscara de rede, como um objeto "IPv4Address".

   with_prefixlen

   compressed

   exploded

      Uma representação de string da rede, com a máscara em notação de
      prefixo.

      "with_prefixlen" e "compressed" são sempre iguais a
      "str(network)". "exploded" usa a forma explodida do endereço de
      rede.

   with_netmask

      Uma representação em string da rede, com a máscara na notação de
      máscara de rede.

   with_hostmask

      Uma representação de string da rede, com a máscara na notação de
      máscara de host.

   num_addresses

      O número total de endereços na rede.

   prefixlen

      Comprimento do prefixo de rede, em bits.

   hosts()

      Retorna um iterador sobre os hosts utilizáveis na rede. Os hosts
      utilizáveis são todos os endereços IP que pertencem à rede,
      exceto o próprio endereço de rede e o endereço de transmissão da
      rede. Para redes com comprimento de máscara 31, o endereço de
      rede e o endereço de transmissão de rede também são incluídos no
      resultado. Redes com máscara 32 retornarão uma lista contendo o
      endereço de host único.

      >>> list(ip_network('192.0.2.0/29').hosts())
      [IPv4Address('192.0.2.1'), IPv4Address('192.0.2.2'),
       IPv4Address('192.0.2.3'), IPv4Address('192.0.2.4'),
       IPv4Address('192.0.2.5'), IPv4Address('192.0.2.6')]
      >>> list(ip_network('192.0.2.0/31').hosts())
      [IPv4Address('192.0.2.0'), IPv4Address('192.0.2.1')]
      >>> list(ip_network('192.0.2.1/32').hosts())
      [IPv4Address('192.0.2.1')]

   overlaps(other)

      "True" se esta rede estiver parcial ou totalmente contida em
      *other* ou *other* estiver totalmente contida nesta rede.

   address_exclude(network)

      Calcula as definições de rede resultantes da remoção da
      *network* fornecida desta. Retorna um iterador de objetos de
      rede. Levanta "ValueError" se *network* não estiver
      completamente contida nesta rede.

      >>> n1 = ip_network('192.0.2.0/28')
      >>> n2 = ip_network('192.0.2.1/32')
      >>> list(n1.address_exclude(n2))
      [IPv4Network('192.0.2.8/29'), IPv4Network('192.0.2.4/30'),
       IPv4Network('192.0.2.2/31'), IPv4Network('192.0.2.0/32')]

   subnets(prefixlen_diff=1, new_prefix=None)

      As sub-redes que se unem para criar a definição de rede atual,
      dependendo dos valores dos argumentos. *prefixlen_diff* é o
      valor pelo qual o comprimento do nosso prefixo deve ser
      aumentado. *new_prefix* é o novo prefixo desejado das sub-redes;
      deve ser maior que nosso prefixo. Um, e apenas um, de
      *prefixlen_diff* e *new_prefix* deve ser definido. Retorna um
      iterador de objetos de rede.

      >>> list(ip_network('192.0.2.0/24').subnets())
      [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]
      >>> list(ip_network('192.0.2.0/24').subnets(prefixlen_diff=2))
      [IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),
       IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')]
      >>> list(ip_network('192.0.2.0/24').subnets(new_prefix=26))
      [IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),
       IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')]
      >>> list(ip_network('192.0.2.0/24').subnets(new_prefix=23))
      Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
          raise ValueError('new prefix must be longer')
      ValueError: new prefix must be longer
      >>> list(ip_network('192.0.2.0/24').subnets(new_prefix=25))
      [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]

   supernet(prefixlen_diff=1, new_prefix=None)

      As super-redes contendo esta definição de rede, dependendo dos
      valores dos argumentos. *prefixlen_diff* é o valor pelo qual o
      comprimento do nosso prefixo deve ser diminuída. *new_prefix* é
      o novo prefixo desejado da super-rede; deve ser maior que nosso
      prefixo. Um, e apenas um, de *prefixlen_diff* e *new_prefix*
      deve ser definido. Retorna um único objeto rede.

      >>> ip_network('192.0.2.0/24').supernet()
      IPv4Network('192.0.2.0/23')
      >>> ip_network('192.0.2.0/24').supernet(prefixlen_diff=2)
      IPv4Network('192.0.0.0/22')
      >>> ip_network('192.0.2.0/24').supernet(new_prefix=20)
      IPv4Network('192.0.0.0/20')

   subnet_of(other)

      Retorna "True" se esta rede é uma sub-rede de *other*.

      >>> a = ip_network('192.168.1.0/24')
      >>> b = ip_network('192.168.1.128/30')
      >>> b.subnet_of(a)
      True

      Adicionado na versão 3.7.

   supernet_of(other)

      Retorna "True" se esta rede é uma super-rede de *other*.

      >>> a = ip_network('192.168.1.0/24')
      >>> b = ip_network('192.168.1.128/30')
      >>> a.supernet_of(b)
      True

      Adicionado na versão 3.7.

   compare_networks(other)

      Compara esta rede com *other*. Nesta comparação são considerados
      apenas os endereços de rede; bits de host não são. Retorna "-1",
      "0" ou "1".

      >>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.2/32'))
      -1
      >>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.0/32'))
      1
      >>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.1/32'))
      0

      Descontinuado desde a versão 3.7: Ele usa o mesmo algoritmo de
      ordenação e comparação que "<", "==" e ">"

class ipaddress.IPv6Network(address, strict=True)

   Constrói uma definição de rede IPv6. *address* pode ser um dos
   seguintes:

   1. Uma string que consiste em um endereço IP e um comprimento de
      prefixo opcional, separados por uma barra ("/"). O endereço IP é
      o endereço de rede e o comprimento do prefixo deve ser um único
      número, o *prefixo*. Se nenhum comprimento de prefixo for
      fornecido, será considerado "/128".

      Observe que as máscaras de rede expandidas atualmente não são
      suportadas. Isso significa que "2001:db00::0/24" é um argumento
      válido enquanto "2001:db00::0/ffff:ff00::" não é.

   2. Um número inteiro que cabe em 128 bits. Isto é equivalente a uma
      rede de endereço único, com o endereço de rede sendo *address* e
      a máscara sendo "/128".

   3. Um inteiro compactado em um objeto "bytes" de comprimento 16,
      big-endian. A interpretação é semelhante a um *address* no
      formato inteiro.

   4. Uma tupla de dois elementos de uma descrição de endereço e uma
      máscara de rede, onde a descrição do endereço é uma string, um
      número inteiro de 128 bits, um número inteiro compactado de 16
      bytes ou um objeto "IPv6Address" existente; e a máscara de rede
      é um número inteiro que representa o comprimento do prefixo.

   Uma exceção "AddressValueError" é levantada se *address* não for um
   endereço IPv6 válido. Uma exceção "NetmaskValueError" é levantada
   se a máscara não for válida para um endereço IPv6.

   Se *strict* for "True" e os bits do host estiverem definidos no
   endereço fornecido, então "ValueError" será levantada. Caso
   contrário, os bits do host serão mascarados para determinar o
   endereço de rede apropriado.

   Alterado na versão 3.5: Adicionado o formulário de tupla de 2
   elementos para o parâmetro do construtor *address*.

   version

   max_prefixlen

   is_multicast

   is_private

   is_unspecified

   is_reserved

   is_loopback

   is_link_local

   network_address

   broadcast_address

   hostmask

   netmask

   with_prefixlen

   compressed

   exploded

   with_netmask

   with_hostmask

   num_addresses

   prefixlen

   hosts()

      Retorna um iterador sobre os hosts utilizáveis na rede. Os hosts
      utilizáveis são todos os endereços IP que pertencem à rede,
      exceto o próprio endereço de anycast do roteador da sub-rede.
      Para redes com comprimento de máscara 127, o endereço anycast do
      roteador da sub-rede de rede é também incluído no resultado.
      Redes com máscara 128 retornarão uma lista contendo o endereço
      de host único.

   overlaps(other)

   address_exclude(network)

   subnets(prefixlen_diff=1, new_prefix=None)

   supernet(prefixlen_diff=1, new_prefix=None)

   subnet_of(other)

   supernet_of(other)

   compare_networks(other)

      Consulte a documentação do atributo correspondente em
      "IPv4Network".

   is_site_local

      Este atributo terá valor verdadeiro para a rede como um todo se
      for verdadeiro tanto para o endereço de rede quanto para o
      endereço de broadcast.


Operadores
----------

Os objetos de rede têm suporte a alguns operadores. Salvo indicação em
contrário, os operadores só podem ser aplicados entre objetos
compatíveis (ou seja, IPv4 com IPv4, IPv6 com IPv6).


Operadores lógicos
~~~~~~~~~~~~~~~~~~

Os objetos de rede podem ser comparados com o conjunto usual de
operadores lógicos. Os objetos de rede são ordenados primeiro por
endereço de rede e depois por máscara de rede.


Iteração
~~~~~~~~

Os objetos de rede podem ser iterados para listar todos os endereços
pertencentes à rede. Para iteração, *todos* os hosts são retornados,
incluindo os hosts inutilizáveis (para hosts utilizáveis, use o método
"hosts()"). Um exemplo:

   >>> for addr in IPv4Network('192.0.2.0/28'):
   ...     addr
   ...
   IPv4Address('192.0.2.0')
   IPv4Address('192.0.2.1')
   IPv4Address('192.0.2.2')
   IPv4Address('192.0.2.3')
   IPv4Address('192.0.2.4')
   IPv4Address('192.0.2.5')
   IPv4Address('192.0.2.6')
   IPv4Address('192.0.2.7')
   IPv4Address('192.0.2.8')
   IPv4Address('192.0.2.9')
   IPv4Address('192.0.2.10')
   IPv4Address('192.0.2.11')
   IPv4Address('192.0.2.12')
   IPv4Address('192.0.2.13')
   IPv4Address('192.0.2.14')
   IPv4Address('192.0.2.15')


Redes como contêineres de endereços
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Os objetos de rede podem atuar como contêineres de endereços. Alguns
exemplos:

   >>> IPv4Network('192.0.2.0/28')[0]
   IPv4Address('192.0.2.0')
   >>> IPv4Network('192.0.2.0/28')[15]
   IPv4Address('192.0.2.15')
   >>> IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')
   True
   >>> IPv4Address('192.0.3.6') in IPv4Network('192.0.2.0/28')
   False


Objetos de interface
====================

Os objetos de interface são *hasheáveis*, portanto podem ser usados
como chaves em dicionários.

class ipaddress.IPv4Interface(address)

   Constrói uma interface IPv4. O significado de *address* é o mesmo
   do construtor de "IPv4Network", exceto que endereços de host
   arbitrários são sempre aceitos.

   "IPv4Interface" é uma subclasse de "IPv4Address", portanto herda
   todos os atributos dessa classe. Além disso, os seguintes atributos
   estão disponíveis:

   ip

      O endereço ("IPv4Address") sem informações de rede.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.ip
      IPv4Address('192.0.2.5')

   network

      A rede ("IPv4Network") à qual esta interface pertence.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.network
      IPv4Network('192.0.2.0/24')

   with_prefixlen

      Uma representação de string da interface com a máscara em
      notação de prefixo.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.with_prefixlen
      '192.0.2.5/24'

   with_netmask

      Uma representação de string da interface com a rede como uma
      máscara de rede.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.with_netmask
      '192.0.2.5/255.255.255.0'

   with_hostmask

      Uma representação de string da interface com a rede como uma
      máscara de host.

      >>> interface = IPv4Interface('192.0.2.5/24')
      >>> interface.with_hostmask
      '192.0.2.5/0.0.0.255'

class ipaddress.IPv6Interface(address)

   Constrói uma interface IPv6. O significado de *address* é o mesmo
   do construtor de "IPv6Network", exceto que endereços de host
   arbitrários são sempre aceitos.

   "IPv6Interface" é uma subclasse de "IPv6Address", portanto herda
   todos os atributos dessa classe. Além disso, os seguintes atributos
   estão disponíveis:

   ip

   network

   with_prefixlen

   with_netmask

   with_hostmask

      Consulte a documentação do atributo correspondente em
      "IPv4Interface".


Operadores
----------

Os objetos de interface têm suporte a alguns operadores. Salvo
indicação em contrário, os operadores só podem ser aplicados entre
objetos compatíveis (ou seja, IPv4 com IPv4, IPv6 com IPv6).


Operadores lógicos
~~~~~~~~~~~~~~~~~~

Os objetos de interface podem ser comparados com o conjunto usual de
operadores lógicos.

Para comparação de igualdade ("==" e "!="), tanto o endereço IP quanto
a rede devem ser iguais para que os objetos sejam iguais. Uma
interface não será igual a nenhum endereço ou objeto de rede.

Para ordenação ("<", ">", etc) as regras são diferentes. Objetos de
interface e de endereço com a mesma versão IP podem ser comparados e
os objetos de endereço sempre serão ordenados antes dos objetos de
interface. Dois objetos de interface são primeiro comparados por suas
redes e, se forem iguais, então por seus endereços IP.


Outras funções de nível de módulo
=================================

O módulo também fornece as seguintes funções de nível de módulo:

ipaddress.v4_int_to_packed(address)

   Representa um endereço como 4 bytes compactados em ordem de rede
   (big-endian). *address* é uma representação inteira de um endereço
   IP IPv4. Uma exceção "ValueError" é levantada se o número inteiro
   for negativo ou muito grande para ser um endereço IP IPv4.

   >>> ipaddress.ip_address(3221225985)
   IPv4Address('192.0.2.1')
   >>> ipaddress.v4_int_to_packed(3221225985)
   b'\xc0\x00\x02\x01'

ipaddress.v6_int_to_packed(address)

   Representa um endereço como 16 bytes compactados em ordem de rede
   (big-endian). *address* é uma representação inteira de um endereço
   IP IPv6. Uma exceção "ValueError" é levantada se o número inteiro
   for negativo ou muito grande para ser um endereço IP IPv6.

ipaddress.summarize_address_range(first, last)

   Retorna um iterador do intervalo de rede resumido, considerando o
   primeiro e o último endereço IP. *first* é o primeiro "IPv4Address"
   ou "IPv6Address" no intervalo e *last* é o último "IPv4Address" ou
   "IPv6Address" no intervalo. Uma exceção "TypeError" é levantada se
   *first* ou *last* não forem endereços IP ou não forem da mesma
   versão. Uma exceção "ValueError" é levantada se *last* não for
   maior que *first* ou se a versão do *first* endereço não for 4 ou
   6.

   >>> [ipaddr for ipaddr in ipaddress.summarize_address_range(
   ...    ipaddress.IPv4Address('192.0.2.0'),
   ...    ipaddress.IPv4Address('192.0.2.130'))]
   [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'), IPv4Network('192.0.2.130/32')]

ipaddress.collapse_addresses(addresses)

   Retorna um iterador dos objetos "IPv4Network" ou "IPv6Network"
   recolhidos. *addresses* é um *iterável* de objetos "IPv4Network" ou
   "IPv6Network". Uma exceção "TypeError" é levantada se *addresses*
   contiver objetos de versão mista.

   >>> [ipaddr for ipaddr in
   ... ipaddress.collapse_addresses([ipaddress.IPv4Network('192.0.2.0/25'),
   ... ipaddress.IPv4Network('192.0.2.128/25')])]
   [IPv4Network('192.0.2.0/24')]

ipaddress.get_mixed_type_key(obj)

   Retorna uma chave adequada para ordenação entre redes e endereços.
   Os objetos de endereço e de rede não são ordenáveis por padrão;
   eles são fundamentalmente diferentes, então a expressão:

      IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

   não faz sentido. Porém, há alguns momentos em que você pode desejar
   que "ipaddress" os ordene de qualquer maneira. Se precisar fazer
   isso, você pode usar esta função como argumento *key* para
   "sorted()"

   *obj* é um objeto de rede ou de endereço.


Exceções personalizadas
=======================

Para oferecer suporte a relatórios de erros mais específicos de
construtores de classe, o módulo define as seguintes exceções:

exception ipaddress.AddressValueError(ValueError)

   Qualquer erro de valor relacionado ao endereço.

exception ipaddress.NetmaskValueError(ValueError)

   Qualquer erro de valor relacionado à máscara de rede.
