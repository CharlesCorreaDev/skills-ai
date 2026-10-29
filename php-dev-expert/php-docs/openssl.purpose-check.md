# Opções de verificação de propósito

> **Fonte / Source:** https://www.php.net/manual/pt_BR/openssl.purpose-check.php

---

## Opções de verificação de propósito

**`X509_PURPOSE_SSL_CLIENT`** ([int](language.types.integer.md))

**`X509_PURPOSE_SSL_SERVER`** ([int](language.types.integer.md))

**`X509_PURPOSE_NS_SSL_SERVER`** ([int](language.types.integer.md))

**`X509_PURPOSE_SMIME_SIGN`** ([int](language.types.integer.md))

**`X509_PURPOSE_SMIME_ENCRYPT`** ([int](language.types.integer.md))

**`X509_PURPOSE_CRL_SIGN`** ([int](language.types.integer.md))

**`X509_PURPOSE_ANY`** ([int](language.types.integer.md))

**`X509_PURPOSE_OCSP_HELPER`** ([int](language.types.integer.md))
:   Verifica o certificado para uso como auxiliar de resposta OCSP.
    Disponível a partir do PHP 8.4.0.

**`X509_PURPOSE_TIMESTAMP_SIGN`** ([int](language.types.integer.md))
:   Verifica o certificado para uso como um signatário de timestamp confiável.
    Disponível a partir do PHP 8.4.0.

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
