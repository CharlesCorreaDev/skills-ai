# Algoritmos de Assinatura

> **Fonte / Source:** https://www.php.net/manual/pt_BR/openssl.signature-algos.php

---

## Algoritmos de Assinatura

**`OPENSSL_ALGO_DSS1`** ([int](language.types.integer.md))

**`OPENSSL_ALGO_SHA1`** ([int](language.types.integer.md))
:   Usado como algoritmo padrão por [openssl\_sign()](function.openssl-sign.md) e
    [openssl\_verify()](function.openssl-verify.md).

**`OPENSSL_ALGO_SHA224`** ([int](language.types.integer.md))

**`OPENSSL_ALGO_SHA256`** ([int](language.types.integer.md))

**`OPENSSL_ALGO_SHA384`** ([int](language.types.integer.md))

**`OPENSSL_ALGO_SHA512`** ([int](language.types.integer.md))

**`OPENSSL_ALGO_RMD160`** ([int](language.types.integer.md))

**`OPENSSL_ALGO_MD5`** ([int](language.types.integer.md))

**`OPENSSL_ALGO_MD4`** ([int](language.types.integer.md))

**`OPENSSL_ALGO_MD2`** ([int](language.types.integer.md))
:   Esta constante só está disponível
    se o PHP for compilado com suporte a MD2. Isso requer passar o CFLAG
    `-DHAVE_OPENSSL_MD2_H` ao compilar o PHP,
    e `enable-md2` ao compilar o OpenSSL 1.0.0+.

`↑` and `↓` to navigate •
`Enter` to select •
`Esc` to close • `/` to open

document.addEventListener("DOMContentLoaded", function() {
/\*{{{Search Modal\*/
const language = 'local';
initSearchModal();
initPHPSearch(language).then((searchCallback) => {
initSearchUI({language, searchCallback, limit: 30});
});
/\*}}}\*/
});
