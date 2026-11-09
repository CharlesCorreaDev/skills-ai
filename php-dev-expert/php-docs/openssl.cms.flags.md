# Opções/Constantes CMS

> **Fonte / Source:** https://www.php.net/manual/pt_BR/openssl.cms.flags.php

---

## Opções/Constantes CMS

As funções do CMS usam opções que são especificados usando um
campo de bits que pode incluir um ou mais dos seguintes valores:

**CONSTANTES CMS**

| Constante | Descrição |
| --- | --- |
| **`OPENSSL_CMS_TEXT`** ([int](language.types.integer.md)) | Adiciona cabeçalhos de tipo de conteúdo text/plain a mensagens criptografadas/assinadas. Se estiver descriptografando ou verificando, ela remove esses cabeçalhos da saída - se a mensagem descriptografada ou verificada não for do tipo MIME text/plain, ocorrerá um erro. |
| **`OPENSSL_CMS_BINARY`** ([int](language.types.integer.md)) | Normalmente, a mensagem de entrada é convertida para o formato "canônico", que está efetivamente usando `CR` e `LF` como fim de linha: conforme exigido pela especificação CMS. Quando esta opção está presente, nenhuma tradução ocorre. Isso é útil ao manipular dados binários que podem não estar no formato CMS. |
| **`OPENSSL_CMS_NOINTERN`** ([int](language.types.integer.md)) | Ao verificar uma mensagem, os certificados (se houver) incluídos na mensagem são normalmente pesquisados para o certificado de assinatura. Com esta opção, apenas os certificados especificados no parâmetro `untrusted_certificates_filename` de [openssl\_cms\_verify()](function.openssl-cms-verify.md) são usados. No entanto, os certificados fornecidos ainda podem ser usados como CAs não confiáveis. |
| **`OPENSSL_CMS_NOVERIFY`** ([int](language.types.integer.md)) | Não verifica o certificado do signatário de uma mensagem assinada. |
| **`OPENSSL_CMS_NOCERTS`** ([int](language.types.integer.md)) | Ao assinar uma mensagem, o certificado do signatário normalmente é incluído - com esta opção, ele é excluído. Isso reduzirá o tamanho da mensagem assinada, mas o verificador deve ter uma cópia do certificado do signatário disponível localmente (passado usando o `untrusted_certificates_filename` para [openssl\_cms\_verify()](function.openssl-cms-verify.md), por exemplo). |
| **`OPENSSL_CMS_NOATTR`** ([int](language.types.integer.md)) | Normalmente, quando uma mensagem é assinada, um conjunto de atributos é incluído, que inclui o tempo de assinatura e os algoritmos simétricos suportados. Com esta opção, eles não são incluídos. |
| **`OPENSSL_CMS_DETACHED`** ([int](language.types.integer.md)) | Ao assinar uma mensagem, use a assinatura de texto simples com o tipo MIME `"multipart/signed"`. Este é o padrão se não for especificada nenhuma opção no parâmetro `flags` para [openssl\_cms\_sign()](function.openssl-cms-sign.md). Se esta opção for desativada, a mensagem será assinada usando assinatura opaca, que é mais resistente à tradução por retransmissões de e-mail, mas não pode ser lida por agentes de e-mail que não suportam S/MIME. |
| **`OPENSSL_CMS_NOSIGS`** ([int](language.types.integer.md)) | Não tenta verificar as assinaturas em uma mensagem |
| **`OPENSSL_CMS_OLDMIMETYPE`** ([int](language.types.integer.md)) | Disponível a partir do PHP 8.3.0. Define o content-type como `application/x-pkcs7-mime` em vez de `application/pkcs7-mime` para criptografar uma mensagem. |

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
