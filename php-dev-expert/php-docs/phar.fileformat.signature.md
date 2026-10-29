# Formato de assinatura Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.fileformat.signature.php

---

## Formato de assinatura Phar

Phars que contêm uma assinatura sempre têm a assinatura anexada ao
final do arquivo Phar, após o carregador, o manifesto e o conteúdo do arquivo.
Os formatos de assinatura suportados no momento são MD5, SHA1, SHA256, SHA512
e OPENSSL.

**Formato de assinatura**

| Comprimento em bytes | Descrição |
| --- | --- |
| variável | A assinatura real: 20 bytes para uma assinatura SHA1, 16 bytes para uma assinatura MD5, 32 bytes para uma assinatura SHA256 e 64 bytes para uma assinatura SHA512. O comprimento de uma assinatura OPENSSL depende do tamanho da chave privada. |
| 4 bytes | Sinalizadores de assinatura. `0x0001` é usado para definir uma assinatura MD5, `0x0002` é usado para definir uma assinatura SHA1, `0x0003` é usado para definir uma assinatura SHA256 e `0x0004` é usado para definir uma assinatura SHA512. O suporte às assinaturas SHA256 e SHA512 está disponível a partir da versão 1.1.0 da API. `0x0010` é usado para definir uma assinatura OPENSSL, que está disponível a partir da versão 1.1.1 da API, se o OpenSSL estiver disponível. |
| 4 bytes | Palavra mágica `GBMB` usada para definir a presença de uma assinatura. |

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
