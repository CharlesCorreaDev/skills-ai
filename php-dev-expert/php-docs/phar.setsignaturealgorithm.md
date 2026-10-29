# Define o algoritmo de assinatura para um phar e o aplica

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.setsignaturealgorithm.php

---

# Phar::setSignatureAlgorithm

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.1.0)

Phar::setSignatureAlgorithm — Define o algoritmo de assinatura para um phar e o aplica

### Descrição

public function **Phar::setSignatureAlgorithm**([int](language.types.integer.md) `$algo`, [?](language.types.null.md)[string](language.types.string.md) `$privateKey` = **`null`**): [void](language.types.void.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Define o algoritmo de assinatura para um Phar e o aplica. O
algoritmo de assinatura deve ser um dos seguintes: `Phar::MD5`,
`Phar::SHA1`, `Phar::SHA256`,
`Phar::SHA512` ou `Phar::OPENSSL`.

Observe que todos os arquivos phar executáveis ​​têm uma assinatura criada
automaticamente, `SHA1` por padrão. Arquivos de dados baseados em tar ou zip
(arquivos criados com a classe [PharData](class.phardata.md)) devem ter
sua assinatura criada e definida explicitamente via
**Phar::setSignatureAlgorithm()**.

### Parâmetros

`algo`
:   Um dos seguintes: `Phar::MD5`,
    `Phar::SHA1`, `Phar::SHA256`,
    `Phar::SHA512` ou `Phar::OPENSSL`.

`privateKey`
:   O conteúdo de uma chave privada OpenSSL, conforme extraído de um certificado ou
    arquivo de chave OpenSSL:

    ```
    <?php
    $private = openssl_get_privatekey(file_get_contents('private.pem'));
    $pkey = '';
    openssl_pkey_export($private, $pkey);
    $p->setSignatureAlgorithm(Phar::OPENSSL, $pkey);
    ?>
    ```

    Consulte [introdução ao phar](phar.using.md) para obter instruções sobre
    nomeação e posicionamento do arquivo de chave pública.

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

Lança [UnexpectedValueException](class.unexpectedvalueexception.md) para vários erros,
e uma [PharException](class.pharexception.md)
se ocorrer algum problema ao liberar as alterações no disco.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `privateKey` agora é anulável. |

### Veja também

- [Phar::getSupportedSignatures()](phar.getsupportedsignatures.md) - Retorna um array de tipos de assinatura suportados
- [Phar::getSignature()](phar.getsignature.md) - Retorna a assinatura MD5/SHA1/SHA256/SHA512/OpenSSL de um arquivo Phar

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
