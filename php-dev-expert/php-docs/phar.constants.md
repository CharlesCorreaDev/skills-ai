# Constantes predefinidas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.constants.php

---

# Constantes predefinidas

As constantes abaixo são definidas por esta extensão e
só estarão disponíveis quando a extensão tiver sido compilada no PHP
ou tiver sido carregada dinamicamente em tempo de execução.

**Constantes de compactação Phar**

| Constante | Valor | Descrição |
| --- | --- | --- |
| **`Phar::NONE`** ([int](language.types.integer.md)) | 0x00000000 | sem compactação |
| **`Phar::COMPRESSED`** ([int](language.types.integer.md)) | 0x0000F000 | máscara de bits que pode ser usada com sinalizadores de arquivo para determinar se há alguma compactação presente |
| **`Phar::GZ`** ([int](language.types.integer.md)) | 0x00001000 | compactação zlib (gzip) |
| **`Phar::BZ2`** ([int](language.types.integer.md)) | 0x00002000 | compactação bzip2 |

**Constantes de formato de arquivo Phar**

| Constante | Valor | Descrição |
| --- | --- | --- |
| **`Phar::PHAR`** ([int](language.types.integer.md)) | 1 | formato de arquivo phar |
| **`Phar::TAR`** ([int](language.types.integer.md)) | 2 | formato de arquivo tar |
| **`Phar::ZIP`** ([int](language.types.integer.md)) | 3 | formato de arquivo zip |

**Constantes de assinatura Phar**

| Constante | Valor | Descrição |
| --- | --- | --- |
| **`Phar::MD5`** ([int](language.types.integer.md)) | 0x0001 | assinatura com algoritmo de hash md5 |
| **`Phar::SHA1`** ([int](language.types.integer.md)) | 0x0002 | assinatura com algoritmo de hash sha1 |
| **`Phar::SHA256`** ([int](language.types.integer.md)) | 0x0003 | assinatura com algoritmo de hash sha256 (requer extensão hash) |
| **`Phar::SHA512`** ([int](language.types.integer.md)) | 0x0004 | assinatura com algoritmo de hash sha512 (requer extensão hash) |
| **`Phar::OPENSSL`** ([int](language.types.integer.md)) | 0x0010 | assinatura com par de chaves pública/privada OpenSSL; esta é uma verdadeira assinatura de chave assimétrica |
| **`Phar::OPENSSL_SHA256`** ([int](language.types.integer.md)) |  |  |
| **`Phar::OPENSSL_SHA512`** ([int](language.types.integer.md)) |  |  |

**Constantes de substituição de MIME Phar webPhar**

| Constante | Valor | Descrição |
| --- | --- | --- |
| **`Phar::PHP`** ([int](language.types.integer.md)) | 0 | usado para instruir o parâmetro mimeoverrides de [Phar::webPhar()](phar.webphar.md) que a extensão deve ser analisada como um arquivo PHP |
| **`Phar::PHPS`** ([int](language.types.integer.md)) | 1 | usado para instruir o parâmetro mimeoverrides de [Phar::webPhar()](phar.webphar.md) que a extensão deve ser analisada como um arquivo-fonte PHP por meio de [highlight\_file()](function.highlight-file.md) |

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
