"secrets" --- Gera números aleatórios seguros para gerenciar segredos
*********************************************************************

Adicionado na versão 3.6.

**Código-fonte:** Lib/secrets.py

======================================================================

The "secrets" module is used for generating cryptographically strong
random numbers suitable for managing data such as passwords, account
authentication, security tokens, and related secrets.

In particular, "secrets" should be used in preference to the default
pseudo-random number generator in the "random" module, which is
designed for modelling and simulation, not security or cryptography.

Ver também: **PEP 506**


Números aleatórios
==================

The "secrets" module provides access to the most secure source of
randomness that your operating system provides.

class secrets.SystemRandom

   Uma classe para gerar números aleatórios usando as fontes da mais
   alta qualidade fornecidas pelo sistema operacional. Veja
   "random.SystemRandom" para detalhes adicionais.

secrets.choice(seq)

   Retorna um elemento escolhido aleatoriamente de uma sequência não
   vazia.

secrets.randbelow(exclusive_upper_bound)

   Retorna um int aleatório no intervalo [0, *exclusive_upper_bound*).

secrets.randbits(k)

   Retorna um int não negativo com *k* bits aleatórios.


Gerando tokens
==============

The "secrets" module provides functions for generating secure tokens,
suitable for applications such as password resets, hard-to-guess URLs,
and similar.

secrets.token_bytes(nbytes=None)

   Return a random byte string containing *nbytes* number of bytes.

   If *nbytes* is not specified or "None", "DEFAULT_ENTROPY" is used
   instead.

      >>> token_bytes(16)
      b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'

secrets.token_hex(nbytes=None)

   Return a random text string, in hexadecimal.  The string has
   *nbytes* random bytes, each byte converted to two hex digits.

   If *nbytes* is not specified or "None", "DEFAULT_ENTROPY" is used
   instead.

      >>> token_hex(16)
      'f9bf78b9a18ce6d46a0cd2b0b86df9da'

secrets.token_urlsafe(nbytes=None)

   Return a random URL-safe text string, containing *nbytes* random
   bytes.  The text is Base64 encoded, so on average each byte results
   in approximately 1.3 characters.

   If *nbytes* is not specified or "None", "DEFAULT_ENTROPY" is used
   instead.

      >>> token_urlsafe(16)
      'Drmhze6EPcv0fN_81Bj-nA'


Quantos bytes os tokens devem usar?
-----------------------------------

To be secure against brute-force attacks, tokens need to have
sufficient randomness.  Unfortunately, what is considered sufficient
will necessarily increase as computers get more powerful and able to
make more guesses in a shorter period.  As of 2015, it is believed
that 32 bytes (256 bits) of randomness is sufficient for the typical
use-case expected for the "secrets" module.

Para aqueles que desejam gerenciar seu próprio comprimento de token,
você pode especificar explicitamente quanta aleatoriedade é usada para
tokens, fornecendo um argumento "int" para as várias funções
"token_*". Esse argumento é considerado o número de bytes de
aleatoriedade a serem usados.

Otherwise, if no argument is provided, or if the argument is "None",
the "token_*" functions use "DEFAULT_ENTROPY" instead.

secrets.DEFAULT_ENTROPY

   Default number of bytes of randomness used by the "token_*"
   functions.

   The exact value is subject to change at any time, including during
   maintenance releases.


Outras funções
==============

secrets.compare_digest(a, b)

   Return "True" if strings or *bytes-like objects* *a* and *b* are
   equal, otherwise "False", using a "constant-time compare" to reduce
   the risk of timing attacks. See "hmac.compare_digest()" for
   additional details.


Receitas e melhores práticas
============================

This section shows recipes and best practices for using "secrets" to
manage a basic level of security.

Gerar uma senha alfanumérica de oito caracteres:

   import string
   import secrets
   alphabet = string.ascii_letters + string.digits
   password = ''.join(secrets.choice(alphabet) for i in range(8))

Nota:

  As aplicações não devem **armazenar senhas em um formato
  recuperável**, seja em texto simples ou criptografado. Elas devem
  ser salgadas e transformadas em hash usando uma função hash de
  sentido único criptograficamente forte (irreversível).

Gerar uma senha alfanumérica de dez caracteres com pelo menos um
caractere minúsculo, pelo menos um caractere maiúsculo e pelo menos
três dígitos:

   import string
   import secrets
   alphabet = string.ascii_letters + string.digits
   while True:
       password = ''.join(secrets.choice(alphabet) for i in range(10))
       if (any(c.islower() for c in password)
               and any(c.isupper() for c in password)
               and sum(c.isdigit() for c in password) >= 3):
           break

Gerar uma senha longa do estilo XKCD:

   import secrets
   # Em sistemas Linux padrão, use um arquivo de dicionário conveniente.
   # Outras plataformas podem precisar fornecer sua própria lista de palavras.
   with open('/usr/share/dict/words') as f:
       words = [word.strip() for word in f]
       password = ' '.join(secrets.choice(words) for i in range(4))

Gerar uma URL temporária difícil de adivinhação contendo um token de
segurança adequado para aplicativos de recuperação de senha:

   import secrets
   url = 'https://example.com/reset=' + secrets.token_urlsafe()
