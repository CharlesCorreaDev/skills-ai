# Retorna a assinatura MD5/SHA1/SHA256/SHA512/OpenSSL de um arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.getsignature.php

---

# Phar::getSignature

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::getSignature — Retorna a assinatura MD5/SHA1/SHA256/SHA512/OpenSSL de um arquivo Phar

### Descrição

public function **Phar::getSignature**(): [array](language.types.array.md)|[false](language.types.singleton.md)

Retorna a assinatura de verificação de um arquivo phar em uma string hexadecimal.

### Parâmetros

### Valor Retornado

Array com a assinatura do arquivo aberto na chave `hash` e `MD5`,
`SHA-1`,
`SHA-256`, `SHA-512` ou `OpenSSL`
em `hash_type`. Esta assinatura é um hash calculado sobre
todo o conteúdo do arquivo phar e pode ser usada para verificar a integridade do arquivo.
Uma assinatura válida é absolutamente necessária para todos os arquivos phar executáveis ​​se a
[variável INI phar.require\_hash](phar.configuration.md#ini.phar.require-hash)
estiver definida como true.
Se não houver assinatura, a função retornará **`false`**.

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
