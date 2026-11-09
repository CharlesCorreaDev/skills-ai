# Opções/Constantes PKCS7

> **Fonte / Source:** https://www.php.net/manual/pt_BR/openssl.pkcs7.flags.php

---

## Opções/Constantes PKCS7

As funções S/MIME usam opções que são especificadas usando um
campo de bits que pode incluir um ou mais dos seguintes valores:

**CONSTANTES PKCS7**

| Constante | Descrição |
| --- | --- |
| **`PKCS7_TEXT`** ([int](language.types.integer.md)) | Adiciona cabeçalhos de tipo de conteúdo `text/plain` à mensagem criptografada/assinada. Se estiver descriptografando ou verificando, ele remove esses cabeçalhos da saída - se a mensagem descriptografada ou verificada não for do tipo MIME `text/plain`, então ocorrerá um erro. |
| **`PKCS7_BINARY`** ([int](language.types.integer.md)) | Normalmente, a mensagem de entrada é convertida para o formato "canônico", que está efetivamente usando `CR` e `LF` como fim de linha: conforme exigido pela especificação S/MIME. Quando esta opção está presente, nenhuma tradução ocorre. Isso é útil ao manipular dados binários que podem não estar no formato MIME. |
| **`PKCS7_NOINTERN`** ([int](language.types.integer.md)) | Ao verificar uma mensagem, os certificados (se houver) incluídos na mensagem são normalmente pesquisados para o certificado de assinatura. Com esta opção, apenas os certificados especificados no parâmetro `untrusted_certificates_filename` de [openssl\_pkcs7\_verify()](function.openssl-pkcs7-verify.md) são usados. No entanto, os certificados fornecidos ainda podem ser usados como CAs não confiáveis. |
| **`PKCS7_NOVERIFY`** ([int](language.types.integer.md)) | Não verifica o certificado do signatário de uma mensagem assinada. |
| **`PKCS7_NOCHAIN`** ([int](language.types.integer.md)) | Não encadeia a verificação de certificados de signatários: ou seja, não usa os certificados na mensagem assinada como CAs não confiáveis. |
| **`PKCS7_NOCERTS`** ([int](language.types.integer.md)) | Ao assinar uma mensagem, o certificado do signatário normalmente é incluído - com esta opção, ele é excluído. Isso reduzirá o tamanho da mensagem assinada, mas o verificador deve ter uma cópia do certificado do signatário disponível localmente (passado usando o `untrusted_certificates_filename` para [openssl\_pkcs7\_verify()](function.openssl-pkcs7-verify.md), por exemplo). |
| **`PKCS7_NOATTR`** ([int](language.types.integer.md)) | Normalmente, quando uma mensagem é assinada, um conjunto de atributos é incluído, que inclui o tempo de assinatura e os algoritmos simétricos suportados. Com esta opção, eles não são incluídos. |
| **`PKCS7_DETACHED`** ([int](language.types.integer.md)) | Ao assinar uma mensagem, usa a assinatura de texto simples com o tipo MIME `"multipart/signed"`. Este é o padrão não for especificada nsenhuma opção no parâmetro `flags` para [openssl\_pkcs7\_sign()](function.openssl-pkcs7-sign.md). Se esta opção for desativada, a mensagem será assinada usando assinatura opaca, que é mais resistente à tradução por retransmissões de e-mail, mas não pode ser lida por agentes de e-mail que não suportam S/MIME. |
| **`PKCS7_NOSIGS`** ([int](language.types.integer.md)) | Não tenta verificar as assinaturas em uma mensagem |
| **`PKCS7_NOOLDMIMETYPE`** ([int](language.types.integer.md)) | Disponível a partir do PHP 8.3.0. Define o content-type como `application/pkcs7-mime` em vez de `application/x-pkcs7-mime` para criptografar uma mensagem. |
| **`PKCS7_NOSMIMECAP`** ([int](language.types.integer.md)) | Disponível a partir do PHP 8.5.0. Não inclui as capacidades S/MIME (SMIMECapabilities) na assinatura. |
| **`PKCS7_CRLFEOL`** ([int](language.types.integer.md)) | Disponível a partir do PHP 8.5.0. Usa `CRLF` como fim de linha na saída. |
| **`PKCS7_NOCRL`** ([int](language.types.integer.md)) | Disponível a partir do PHP 8.5.0. Não inclui as CRLs na estrutura PKCS7. |
| **`PKCS7_NO_DUAL_CONTENT`** ([int](language.types.integer.md)) | Disponível a partir do PHP 8.5.0. Não inclui conteúdo duplicado, evitando a duplicação do conteúdo assinado. |

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
