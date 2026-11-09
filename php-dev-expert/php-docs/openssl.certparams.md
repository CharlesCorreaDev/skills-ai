# Parâmetros de chave/certificado

> **Fonte / Source:** https://www.php.net/manual/pt_BR/openssl.certparams.php

---

# Parâmetros de chave/certificado

Várias funções openssl exigem um parâmetro de chave ou certificado.
Os seguintes métodos podem ser usados para obtê-los:

- Certificados
  1. Uma instância [OpenSSLCertificate](class.opensslcertificate.md)
     (ou antes do PHP 8.0.0, um [resource](language.types.resource.md) do tipo `OpenSSL X.509`)
     retornada de [openssl\_x509\_read()](function.openssl-x509-read.md)
  2. Uma string com o formato
     file://path/to/cert.pem; o arquivo nomeado deve
     conter um certificado codificado PEM
  3. Uma string contendo o conteúdo de um certificado, codificado em PEM,
     pode começar com `-----BEGIN CERTIFICATE-----`
- Solicitações de assinatura de certificado (CSRs)
  1. Uma instância de [OpenSSLCertificateSigningRequest](class.opensslcertificatesigningrequest.md)
     (ou antes do PHP 8.0.0, um [resource](language.types.resource.md) do tipo `OpenSSL X.509 CSR`)
     retornado de [openssl\_csr\_new()](function.openssl-csr-new.md)
  2. Uma string com o formato
     file://path/to/csr.pem; o arquivo nomeado deve
     conter um CSR codificado em PEM.
  3. Uma string contendo o conteúdo de um CSR, codificado em PEM,
     pode começar com `-----BEGIN CERTIFICATE REQUEST-----`
- Chaves Públicas/Privadas
  1. Uma instância de [OpenSSLAsymmetricKey](class.opensslasymmetrickey.md)
     (ou anterior ao PHP 8.0.0, um [resource](language.types.resource.md) do tipo `OpenSSL key`)
     retornada de [openssl\_get\_publickey()](function.openssl-get-publickey.md) ou
     [openssl\_get\_privatekey()](function.openssl-get-privatekey.md)
  2. Somente para chaves públicas: uma instância de [OpenSSLCertificate](class.opensslcertificate.md)
     (ou anterior ao PHP 8.0.0, um [resource](language.types.resource.md) do tipo `OpenSSL X.509`)
  3. Uma string com o formato
     file://path/to/file.pem - o arquivo nomeado deve
     conter um certificado e/ou chave privada codificado em PEM (pode conter ambos)
  4. Uma string contendo o conteúdo de um certificado/chave,
     codificado em PEM, pode começar com
     `-----BEGIN PUBLIC KEY-----`
  5. Para chaves privadas, pode ser usada também a sintaxe
     `array($key, $passphrase)` onde $key representa uma
     chave especificada usando a notação file:// ou de conteúdo textual acima, e
     $passphrase representa uma string contendo a senha para essa
     chave privada

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
