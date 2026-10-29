# Retorna um array de tipos de assinatura suportados

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.getsupportedsignatures.php

---

# Phar::getSupportedSignatures

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.1.0)

Phar::getSupportedSignatures — Retorna um array de tipos de assinatura suportados

### Descrição

final public static function **Phar::getSupportedSignatures**(): [array](language.types.array.md)

Retorna um array de tipos de assinatura suportados.

### Parâmetros

Sem parâmetros.

### Valor Retornado

Retorna um array contendo qualquer um dos seguintes: `MD5`, `SHA-1`,
`SHA-256`, `SHA-512` ou `OpenSSL`.

### Veja também

- [Phar::getSignature()](phar.getsignature.md) - Retorna a assinatura MD5/SHA1/SHA256/SHA512/OpenSSL de um arquivo Phar
- [Phar::setSignatureAlgorithm()](phar.setsignaturealgorithm.md) - Define o algoritmo de assinatura para um phar e o aplica

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
