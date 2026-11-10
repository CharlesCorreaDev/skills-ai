"uuid" --- Objetos UUID conforme **RFC 9562**
*********************************************

**Código-fonte:** Lib/uuid.py

======================================================================

Este módulo fornece objetos "UUID" imutáveis (a classe "UUID") e
funções para gerar UUIDs correspondentes a uma versão específica de
UUID, conforme especificado em **RFC 9562** (que substitui **RFC
4122**), por exemplo, "uuid1()" para a versão 1 de UUID, "uuid3()"
para a versão 3 de UUID e assim por diante. Observe que a versão 2 de
UUID foi omitida deliberadamente, pois está fora do escopo da RFC.

Se tudo o que você quer é um ID único, você provavelmente deve chamar
"uuid1()" ou "uuid4()". Note que "uuid1()" pode comprometer a
privacidade, pois cria um UUID contendo o endereço de rede do
computador. "uuid4()" cria um UUID aleatório.

Dependendo do suporte da plataforma subjacente, "uuid1()" pode ou não
retornar um UUID "seguro". Um UUID seguro é aquele que é gerado usando
métodos de sincronização que garantem que dois processos não possam
obter o mesmo UUID. Todas as instâncias de "UUID" têm um atributo
"is_safe" que retransmite qualquer informação sobre a segurança do
UUID, usando esta enumeração:

class uuid.SafeUUID

   Adicionado na versão 3.7.

   safe

      O UUID foi gerado pela plataforma de forma segura para
      multiprocessamento.

   unsafe

      O UUID não foi gerado de forma segura para multiprocessamento.

   unknown

      A plataforma não fornece informações sobre se o UUID foi gerado
      com segurança ou não.

class uuid.UUID(hex=None, bytes=None, bytes_le=None, fields=None, int=None, version=None, *, is_safe=SafeUUID.unknown)

   Create a UUID from either a string of 32 hexadecimal digits, a
   16-byte "bytes" object in big-endian order as the *bytes* argument,
   a 16-byte "bytes" object in little-endian order as the *bytes_le*
   argument, a tuple of six integers (32-bit *time_low*, 16-bit
   *time_mid*, 16-bit *time_hi_version*, 8-bit *clock_seq_hi_variant*,
   8-bit *clock_seq_low*, 48-bit *node*) as the *fields* argument, or
   a single 128-bit integer as the *int* argument. When a string of
   hex digits is given, curly braces, hyphens, and a URN prefix are
   all optional.  For example, these expressions all yield the same
   UUID:

      UUID('{12345678-1234-5678-1234-567812345678}')
      UUID('12345678123456781234567812345678')
      UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
      UUID(bytes=b'\x12\x34\x56\x78'*4)
      UUID(bytes_le=b'\x78\x56\x34\x12\x34\x12\x78\x56' +
                    b'\x12\x34\x56\x78\x12\x34\x56\x78')
      UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
      UUID(int=0x12345678123456781234567812345678)

   Exatamente um de *hex*, *bytes*, *bytes_le*, *fields* ou *int* deve
   ser fornecido. O argumento *version* é opcional; se fornecido, o
   UUID resultante terá sua variante e número de versão definidos de
   acordo com **RFC 9562**, substituindo bits no *hex*, *bytes*,
   *bytes_le*, *fields* ou *int* fornecido.

   A comparação de objetos UUID é feita por meio da comparação de seus
   atributos "UUID.int". A comparação com um objeto não UUID levanta
   uma "TypeError".

   "str(uuid)" retorna uma string no formato
   "12345678-1234-5678-1234-567812345678" onde os 32 dígitos
   hexadecimais representam o UUID.

As instâncias "UUID" têm estes atributos de somente leitura:

UUID.bytes

   The UUID as a 16-byte "bytes" object (containing the six integer
   fields in big-endian byte order).

UUID.bytes_le

   The UUID as a 16-byte "bytes" object (with *time_low*, *time_mid*,
   and *time_hi_version* in little-endian byte order).

UUID.fields

   Uma tupla dos seis campos de inteiros do UUID, que também estão
   disponíveis como seis atributos individuais e dois atributos
   derivados:

+----------------------------------------------------+----------------------------------------------------+
| Campo                                              | Significado                                        |
+----------------------------------------------------+----------------------------------------------------+
| UUID.time_low                                      | Os primeiros 32 bits do UUID. Relevante apenas     |
|                                                    | para a versão 1.                                   |
+----------------------------------------------------+----------------------------------------------------+
| UUID.time_mid                                      | Os próximos 16 bits do UUID. Relevante apenas para |
|                                                    | a versão 1.                                        |
+----------------------------------------------------+----------------------------------------------------+
| UUID.time_hi_version                               | Os próximos 16 bits do UUID. Relevante apenas para |
|                                                    | a versão 1.                                        |
+----------------------------------------------------+----------------------------------------------------+
| UUID.clock_seq_hi_variant                          | Os próximos 8 bits do UUID. Relevante apenas para  |
|                                                    | as versões 1 e 6.                                  |
+----------------------------------------------------+----------------------------------------------------+
| UUID.clock_seq_low                                 | Os próximos 8 bits do UUID. Relevante apenas para  |
|                                                    | as versões 1 e 6.                                  |
+----------------------------------------------------+----------------------------------------------------+
| UUID.node                                          | Os últimos 48 bits do UUID. Relevante apenas para  |
|                                                    | a versão 1.                                        |
+----------------------------------------------------+----------------------------------------------------+
| UUID.time                                          | O registro de data e hora de 60 bits como uma      |
|                                                    | contagem de intervalos de 100 nanossegundos desde  |
|                                                    | a época gregoriana (1582-10-15 00:00:00) para as   |
|                                                    | versões 1 e 6, ou o registro de data e hora de 48  |
|                                                    | bits em milissegundos desde a época Unix           |
|                                                    | (1970-01-01 00:00:00) para a versão 7.             |
+----------------------------------------------------+----------------------------------------------------+
| UUID.clock_seq                                     | Número de sequência de 14 bits. Relevante apenas   |
|                                                    | para as versões 1 e 6.                             |
+----------------------------------------------------+----------------------------------------------------+

UUID.hex

   O UUID como uma sequência hexadecimal de 32 caracteres minúsculos.

UUID.int

   O UUID como um inteiro de 128 bits.

UUID.urn

   O UUID como um URN conforme especificado no **RFC 9562**.

UUID.variant

   A variante UUID, que determina o layout interno do UUID. Esta será
   uma das constantes "RESERVED_NCS", "RFC_4122", "RESERVED_MICROSOFT"
   ou "RESERVED_FUTURE".

UUID.version

   O número da versão do UUID (1 a 8, significativo somente quando a
   variante é "RFC_4122").

   Alterado na versão 3.14: Adicionadas versões 6, 7 e 8 do UUID.

UUID.is_safe

   Uma enumeração de "SafeUUID" que indica se a plataforma gerou o
   UUID de forma segura para multiprocessamento.

   Adicionado na versão 3.7.

The "uuid" module defines the following functions:

uuid.getnode()

   Obtém o endereço de hardware como um inteiro positivo de 48 bits.
   Na primeira vez que isso for executado, ele pode iniciar um
   programa separado, o que pode ser bem lento. Se todas as tentativas
   de obter o endereço de hardware falharem, escolhemos um número
   aleatório de 48 bits com o bit multicast (bit menos significativo
   do primeiro octeto) definido como 1, conforme recomendado no **RFC
   4122**. "Endereço de hardware" significa o endereço MAC de uma
   interface de rede. Em uma máquina com várias interfaces de rede,
   endereços MAC administrados universalmente (ou seja, onde o segundo
   bit menos significativo do primeiro octeto é *não definido*) serão
   preferidos em relação a endereços MAC administrados localmente, mas
   sem nenhuma outra garantia de ordenação.

   Alterado na versão 3.7: Endereços MAC administrados universalmente
   são preferidos em vez de endereços MAC administrados localmente,
   pois os primeiros têm garantia de serem globalmente exclusivos,
   enquanto os últimos não.

uuid.uuid1(node=None, clock_seq=None)

   Gera um UUID a partir de um ID de host, número de sequência e hora
   atual de acordo com **RFC 9562, §5.1**.

   Quando *node* não é especificado, "getnode()" é usado para obter o
   endereço de hardware como um inteiro positivo de 48 bits. Quando um
   número de sequência *clock_seq* não é especificado, um inteiro
   positivo pseudoaleatório de 14 bits é gerado.

   Se *node* ou *clock_seq* excederem a contagem de bits esperada,
   apenas seus bits menos significativos serão mantidos.

uuid.uuid3(namespace, name)

   Gera um UUID com base no hash MD5 de um identificador de espaço de
   nomes (que é um UUID) e um nome (que é um objeto "bytes" ou uma
   string que será codificada usando UTF-8) de acordo com **RFC 9562,
   §5.3**.

uuid.uuid4()

   Gera um UUID aleatório em um método criptograficamente seguro de
   acordo com **RFC 9562, §5.4**.

uuid.uuid5(namespace, name)

   Gera um UUID com base no hash SHA-1 de um identificador de espaço
   de nomes (que é um UUID) e um nome (que é um objeto "bytes" ou uma
   string que será codificada usando UTF-8) de acordo com **RFC 9562,
   §5.5**.

uuid.uuid6(node=None, clock_seq=None)

   Gera um UUID a partir de um número de sequência e hora atual de
   acordo com **RFC 9562, §5.6**.

   Esta é uma alternativa ao "uuid1()" para melhorar a localidade do
   banco de dados.

   Quando *node* não é especificado, "getnode()" é usado para obter o
   endereço de hardware como um inteiro positivo de 48 bits. Quando um
   número de sequência *clock_seq* não é especificado, um inteiro
   positivo pseudoaleatório de 14 bits é gerado.

   Se *node* ou *clock_seq* excederem a contagem de bits esperada,
   apenas seus bits menos significativos serão mantidos.

   Adicionado na versão 3.14.

uuid.uuid7()

   Gera um UUID baseado em tempo de acordo com **RFC 9562, §5.7**.

   Para portabilidade entre plataformas sem precisão de
   submilissegundos, os UUIDs produzidos por esta função incorporam um
   registro de data e hora de 48 bits e usam um contador de 42 bits
   para garantir a monotonicidade dentro de um milissegundo.

   Adicionado na versão 3.14.

uuid.uuid8(a=None, b=None, c=None)

   Gera um UUID pseudoaleatório de acordo com **RFC 9562, §5.8**.

   Quando especificados, espera-se que os parâmetros *a*, *b* e *c*
   sejam inteiros positivos de 48, 12 e 62 bits, respectivamente. Se
   excederem a contagem de bits esperada, apenas os bits menos
   significativos serão mantidos; argumentos não especificados são
   substituídos por um inteiro pseudoaleatório de tamanho apropriado.

   Por padrão, *a*, *b* e *c* não são gerados por um gerador de
   números pseudoaleatórios criptograficamente seguro (CSPRNG). Use
   "uuid4()" quando um UUID precisar ser usado em um contexto de
   segurança sensível.

   Adicionado na versão 3.14.

The "uuid" module defines the following namespace identifiers for use
with "uuid3()" or "uuid5()".

uuid.NAMESPACE_DNS

   Quando esse espaço de nomes é especificado, a string *name* é um
   nome de domínio totalmente qualificado.

uuid.NAMESPACE_URL

   Quando esse espaço de nomes é especificado, a string *name* é uma
   URL.

uuid.NAMESPACE_OID

   Quando esse espaço de nomes é especificado, a string *name* é um
   OID ISO.

uuid.NAMESPACE_X500

   Quando esse espaço de nomes é especificado, a string *name* é um DN
   X.500 em DER ou um formato de saída de texto.

The "uuid" module defines the following constants for the possible
values of the "variant" attribute:

uuid.RESERVED_NCS

   Reservado para compatibilidade com NCS.

uuid.RFC_4122

   Especifica o layout do UUID fornecido em **RFC 4122**. Esta
   constante é mantida para retrocompatibilidade, mesmo que **RFC
   4122** tenha sido substituído por **RFC 9562**.

uuid.RESERVED_MICROSOFT

   Reservado para compatibilidade com Microsoft.

uuid.RESERVED_FUTURE

   Reservado para definição futura.

The "uuid" module defines the special Nil and Max UUID values:

uuid.NIL

   Uma forma especial de UUID que é especificada para ter todos os 128
   bits definidos como zero de acordo com **RFC 9562, §5.9**.

   Adicionado na versão 3.14.

uuid.MAX

   Uma forma especial de UUID que é especificada para ter todos os 128
   bits definidos como um, de acordo com **RFC 9562, §5.10**.

   Adicionado na versão 3.14.

Ver também:

  **RFC 9562** - Um espaço de nomes de URN de identificador
  universalmente exclusivo (UUID)
     Esta especificação define um espaço de nomes de Uniform Resource
     Name para UUIDs, o formato interno de UUIDs e métodos de geração
     de UUIDs.


Uso na linha de comando
=======================

Adicionado na versão 3.12.

The "uuid" module can be executed as a script from the command line.

   python -m uuid [-h] [-u {uuid1,uuid3,uuid4,uuid5,uuid6,uuid7,uuid8}] [-n ESPAÇOS-DE-NOME] [-N NOME]

As seguintes opções são aceitas:

-h, --help

   Mostra a mensagem de ajuda e sai.

-u <uuid>
--uuid <uuid>

   Especifica o nome da função a ser usada para gerar o uuid. Por
   padrão, "uuid4()" é usado.

   Alterado na versão 3.14: Permite gerar versões 6, 7 e 8 do UUID.

-n <namespace>
--namespace <namespace>

   O espaço de nomes é um "UUID", ou "@ns" onde "ns" é um UUID
   predefinido bem conhecido endereçado pelo nome do espaço de nomes.
   Como "@dns", "@url", "@oid" e "@x500". Necessário apenas para
   funções "uuid3()" / "uuid5()".

-N <name>
--name <name>

   O nome usado como parte da geração do uuid. Requerido apenas para
   funções "uuid3()" / "uuid5()".

-C <num>
--count <num>

   Gera *num* novos UUIDs.

   Adicionado na versão 3.14.


Exemplo
=======

Here are some examples of typical usage of the "uuid" module:

   >>> import uuid

   >>> # make a UUID based on the host ID and current time
   >>> uuid.uuid1()
   UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')

   >>> # make a UUID using an MD5 hash of a namespace UUID and a name
   >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
   UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')

   >>> # make a random UUID
   >>> uuid.uuid4()
   UUID('16fd2706-8baf-433b-82eb-8c7fada847da')

   >>> # make a UUID using a SHA-1 hash of a namespace UUID and a name
   >>> uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
   UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')

   >>> # make a UUID from a string of hex digits (braces and hyphens ignored)
   >>> x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

   >>> # convert a UUID to a string of hex digits in standard form
   >>> str(x)
   '00010203-0405-0607-0809-0a0b0c0d0e0f'

   >>> # get the raw 16 bytes of the UUID
   >>> x.bytes
   b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

   >>> # make a UUID from a 16-byte bytes object
   >>> uuid.UUID(bytes=x.bytes)
   UUID('00010203-0405-0607-0809-0a0b0c0d0e0f')

   >>> # get the Nil UUID
   >>> uuid.NIL
   UUID('00000000-0000-0000-0000-000000000000')

   >>> # get the Max UUID
   >>> uuid.MAX
   UUID('ffffffff-ffff-ffff-ffff-ffffffffffff')

   >>> # same as UUIDv1 but with fields reordered to improve DB locality
   >>> uuid.uuid6()
   UUID('1f0799c0-98b9-62db-92c6-a0d365b91053')

   >>> # get UUIDv7 creation (local) time as a timestamp in milliseconds
   >>> u = uuid.uuid7()
   >>> u.time
   1743936859822

   >>> # get UUIDv7 creation (local) time as a datetime object
   >>> import datetime as dt
   >>> dt.datetime.fromtimestamp(u.time / 1000)
   datetime.datetime(...)

   >>> # make a UUID with custom blocks
   >>> uuid.uuid8(0x12345678, 0x9abcdef0, 0x11223344)
   UUID('00001234-5678-8ef0-8000-000011223344')


Exemplo de linha de comando
===========================

Here are some examples of typical usage of the "uuid" command-line
interface:

   # gera um UUID aleatório - por padrão uuid4() é usado
   $ python -m uuid

   # gera um UUID usando uuid1()
   $ python -m uuid -u uuid1

   # gera um UUID usando uuid5
   $ python -m uuid -u uuid5 -n @url -N example.com

   # gera 42 UUIDs aleatórios
   $ python -m uuid -C 42
