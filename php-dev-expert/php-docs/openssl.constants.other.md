# Outras constantes

> **Fonte / Source:** https://www.php.net/manual/pt_BR/openssl.constants.other.php

---

## Outras constantes

**`OPENSSL_RAW_DATA`** ([int](language.types.integer.md))
:   Usada com [openssl\_encrypt()](function.openssl-encrypt.md) e
    [openssl\_decrypt()](function.openssl-decrypt.md) para indicar que os dados
    devem estar em formato binário bruto em vez de codificados em Base64.
    Veja as descrições das respectivas funções para mais detalhes.

**`OPENSSL_DONT_ZERO_PAD_KEY`** ([int](language.types.integer.md))
:   Evita que [openssl\_encrypt()](function.openssl-encrypt.md) preencha chaves menores que
    o comprimento padrão.

**`OPENSSL_ZERO_PADDING`** ([int](language.types.integer.md))
:   Por padrão, as operações de criptografia são preenchidas usando o preenchimento
    de bloco padrão e o preenchimento é verificado e removido ao descriptografar.
    Se **`OPENSSL_ZERO_PADDING`** for definido em `options` como
    [openssl\_encrypt()](function.openssl-encrypt.md) ou [openssl\_decrypt()](function.openssl-decrypt.md),
    nenhum preenchimento será realizado, a quantidade total
    de dados criptografados ou descriptografados deve ser um múltiplo do
    tamanho do bloco ou ocorrerá um erro.

**`OPENSSL_ENCODING_SMIME`** ([int](language.types.integer.md))
:   Indica que a codificação é S/MIME.

**`OPENSSL_ENCODING_DER`** ([int](language.types.integer.md))
:   Indica que a codificação é DER.

**`OPENSSL_ENCODING_PEM`** ([int](language.types.integer.md))
:   Indica que a codificação é PEM.

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
