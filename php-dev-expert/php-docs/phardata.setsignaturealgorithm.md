# Define o algoritmo de assinatura para um phar e o aplica

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.setsignaturealgorithm.php

---

# PharData::setSignatureAlgorithm

(No version information available, might only be in Git)

PharData::setSignatureAlgorithm — Define o algoritmo de assinatura para um phar e o aplica

### Descrição

public function **PharData::setSignatureAlgorithm**([int](language.types.integer.md) `$algo`, [?](language.types.null.md)[string](language.types.string.md) `$privateKey` = **`null`**): [void](language.types.void.md)

> **Nota**:
>
> Este
> método requer que a configuração `phar.readonly` do php.ini seja
> definida como `0` para funcionar com objetos [Phar](class.phar.md).
> Caso contrário, uma exceção [PharException](class.pharexception.md) será lançada.

Define o algoritmo de assinatura para um phar e o aplica. O
algoritmo de assinatura deve ser um dos seguintes: `Phar::MD5`,
`Phar::SHA1`, `Phar::SHA256`,
`Phar::SHA512` ou `Phar::OPENSSL`.

### Parâmetros

`algo`
:   Um dos seguintes: `Phar::MD5`,
    `Phar::SHA1`, `Phar::SHA256`,
    `Phar::SHA512` ou `Phar::OPENSSL`

### Valor Retornado

Nenhum valor é retornado.

### Erros/Exceções

Lança [UnexpectedValueException](class.unexpectedvalueexception.md) para muitos erros,
[BadMethodCallException](class.badmethodcallexception.md) se chamado para um arquivo zip ou
um arquivo phar baseado em tar, e uma [PharException](class.pharexception.md)
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
