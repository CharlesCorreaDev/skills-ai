"hmac" --- Código de autenticação de mensagem com chave hash
************************************************************

**Código-fonte:** Lib/hmac.py

======================================================================

Este módulo implementa o algoritmo HMAC conforme descrito por **RFC
2104**. A interface permite o uso de qualquer função hash com um
tamanho de resumo *fixo*. Em particular, funções de saída extensíveis
como SHAKE-128 ou SHAKE-256 não podem ser usadas com HMAC.

hmac.new(key, msg=None, digestmod)

   Retorna um novo objeto hmac. *key* é um objeto bytes ou bytearray
   que fornece a chave secreta. Se *msg* estiver presente, a chamada
   de método "update(msg)" é feita. *digestmod* é o nome do resumo,
   construtor do resumo ou módulo para o objeto HMAC usar. Pode ser
   qualquer nome adequado para "hashlib.new()". Apesar da posição do
   argumento, é obrigatório.

   Alterado na versão 3.4: O parâmetro *key* pode ser um objeto bytes
   ou bytearray. O parâmetro *msg* pode ser de qualquer tipo suportado
   por "hashlib". O parâmetro *digestmod* pode ser o nome de um
   algoritmo hash.

   Alterado na versão 3.8: O argumento *digestmod* agora é
   obrigatório. Passe-o como um argumento nomeado para evitar
   constrangimentos quando você não tiver uma *msg* inicial.

hmac.digest(key, msg, digest)

   Retorna o resumo de *msg* para o segredo *key* e *digest*
   fornecidos. A função equivale a "HMAC(key, msg, digest).digest()",
   mas usa uma implementação C otimizada ou inline, que é mais rápida
   para mensagens que cabem na memória. Os parâmetros *key*, *msg* e
   *digest* têm o mesmo significado que em "new()".

   Detalhe da implementação do CPython: a implementação otimizada do C
   é usada somente quando *digest* é uma string e o nome de um
   algoritmo de resumo, que é suportado pelo OpenSSL.

   Adicionado na versão 3.7.

class hmac.HMAC

   Um objeto HMAC tem os seguintes métodos:

HMAC.update(msg)

   Atualiza o objeto hmac com *msg*. Chamadas repetidas são
   equivalentes a uma única chamada com a concatenação de todos os
   argumentos: "m.update(a); m.update(b)" equivale a "m.update(a +
   b)".

   Alterado na versão 3.4: O parâmetro *msg* pode ser de qualquer tipo
   suportado por "hashlib".

HMAC.digest()

   Retorna o resumo dos bytes passados para o método "update()" até o
   momento. Este objeto bytes terá o mesmo comprimento que o
   *digest_size* do resumo dado ao construtor. Ele pode conter bytes
   não-ASCII, incluindo bytes NUL.

   Aviso:

     Ao comparar a saída de "digest()" com um resumo fornecido
     externamente durante uma rotina de verificação, é recomendável
     usar a função "compare_digest()" em vez do operador "==" para
     reduzir a vulnerabilidade a ataques de temporização.

HMAC.hexdigest()

   Como "digest()" exceto que o resumo é retornado como uma string com
   o dobro do comprimento contendo apenas dígitos hexadecimais. Isso
   pode ser usado para trocar o valor com segurança em e-mail ou
   outros ambientes não binários.

   Aviso:

     Ao comparar a saída de "hexdigest()" com um resumo fornecido
     externamente durante uma rotina de verificação, é recomendável
     usar a função "compare_digest()" em vez do operador "==" para
     reduzir a vulnerabilidade a ataques de temporização.

HMAC.copy()

   Retorna uma cópia ("clone") do objeto hmac. Isso pode ser usado
   para calcular eficientemente os resumos de strings que compartilham
   uma substring inicial comum.

Um objeto hash tem os seguintes atributos:

HMAC.digest_size

   O tamanho do resumo HMAC resultante em bytes.

HMAC.block_size

   O tamanho do bloco interna do algoritmo de hash em bytes.

   Adicionado na versão 3.4.

HMAC.name

   O nome canônico deste HMAC, sempre em letras minúsculas, por
   exemplo, "hmac-md5".

   Adicionado na versão 3.4.

Alterado na versão 3.10: Foram removidos os atributos não documentados
"HMAC.digest_cons", "HMAC.inner" e "HMAC.outer".

Este módulo também fornece a seguinte função auxiliar:

hmac.compare_digest(a, b)

   Retorna "a == b". Esta função usa uma abordagem projetada para
   evitar análise de tempo evitando comportamento de curto-circuito
   baseado em conteúdo, tornando-a apropriada para criptografia. *a* e
   *b* devem ser ambos do mesmo tipo: "str" (somente ASCII, como, por
   exemplo, retornado por "HMAC.hexdigest()"), ou um *objeto bytes ou
   similar*.

   Nota:

     Se *a* e *b* tiverem comprimentos diferentes, ou se ocorrer um
     erro, um ataque de temporização poderia teoricamente revelar
     informações sobre os tipos e comprimentos de *a* e *b*, mas não
     seus valores.

   Adicionado na versão 3.3.

   Alterado na versão 3.10: A função usa "CRYPTO_memcmp()" do OpenSSL
   internamente quando disponível.

Ver também:

  Módulo "hashlib"
     O módulo Python que fornece funções hash seguras.
