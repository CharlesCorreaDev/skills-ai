# Instalação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/openssl.installation.php

---

## Instalação

Para usar o suporte OpenSSL do PHP, o PHP deve ser compilado com **--with-openssl**.

A biblioteca OpenSSL também tem requisitos adicionais para operação normal em
tempo de execução. Mais notavelmente, o OpenSSL requer acesso a um gerador de
números aleatórios ou pseudoaleatórios; na maioria das plataformas Unix e similares (incluindo Linux),
isso significa que ele deve ter acesso a um dispositivo `/dev/urandom` ou
`/dev/random`.

A opção **--with-system-ciphers** do comando "configure"
está disponível, o que faz com que o PHP use a lista de cifras do sistema em vez de um padrão fixo codificado.

> **Nota**:
> **Nota para usuários do Win32**  
>
> Para que esta extensão funcione, existem arquivos
> DLL que devem estar disponíveis no
> PATH do sistema Windows. Para saber como fazer isso, veja a
> FAQ intitulada "[Como eu adiciono o meu diretório PHP ao PATH
> do Windows](faq.installation.md#faq.installation.addtopath)". Embora copiar arquivos DLL
> da pasta do PHP para o diretório system do Windows também funcione
> (porque o diretório system está, por padrão, no PATH do sistema),
> isso não é recomendado.
> *Esta extensão requer que os seguintes arquivos estejam no
> PATH:*
> libeay32.dll,
> ou, a partir do OpenSSL 1.1, libcrypto-\*.dll
>
> Além disso, se houver planos de usar as funções de geração de chaves e
> assinatura de certificados, será necessário instalar um arquivo
> openssl.cnf válido em seu sistema.
> Existe um arquivo de configuração de exemplo incluído
> nas distribuições binárias do PHP para Win32, no diretório
> extras/ssl.
>
> O PHP pesquisará o openssl.cnf usando a
> seguinte lógica:
>
> - a variável de ambiente `OPENSSL_CONF`, se
>   definida, será usada como o caminho (incluindo o nome do arquivo) do arquivo
>   de configuração.
> - a variável de ambiente `SSLEAY_CONF`, se
>   definida, será usada como o caminho (incluindo o nome do arquivo) do arquivo
>   de configuração.
> - Será assumido que o arquivo openssl.cnf deve ser
>   encontrado na área padrão de certificados, conforme configurado no momento em que
>   a DLL do openssl foi compilada. Isso geralmente significa que o nome de arquivo padrão
>   é C:\Program Files\Common Files\SSL\openssl.cnf (x64)
>   ou C:\Program Files (x86)\Common Files\SSL\openssl.cnf (x86), ou,
>   antes do PHP 7.4.0, C:\usr\local\ssl\openssl.cnf.
>
> É necessário escolher de o
> arquivo de configuração deve ser instalado no caminho padrão ou
> em outro lugar e usar variáveis de ambiente
> (possivelmente uma configuração para cada host virtual) para localizar o arquivo de configuração.
> Observe que é possível substituir o caminho padrão do script usando
> as opções no parâmetro `options` das funções que exigem um
> arquivo de configuração.
>
> **Cuidado**
>
> Deve ser assegurado que usuários não privilegiados não tenham permissão para modificar openssl.cnf.
>
> A partir do OpenSSL 3.0.0, que é usado no Windows por padrão a partir do PHP 8.2.0, vários
> algoritmos foram considerados legados. Esses algoritmos comumente caíram em desuso,
> foram considerados inseguros pela comunidade criptográfica ou algo semelhante.
> Esses algoritmos ainda estão disponíveis através do provedor legado
> (extras/ssl/legacy.dll); seu uso é descrito na seção sobre
> [» configuração do provedor](https://docs.openssl.org/master/man5/config/#Provider-Configuration)
> no manual do OpenSSL.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 7.4.0 | A opção **--with-openssl[=DIR]** não aceita mais um argumento de diretório, em favor da configuração da variável pkg-config PKG\_CONFIG\_PATH para a localização do OpenSSL ou especificando as variáveis OPENSSL\_LIBS e OPENSSL\_CFLAGS. |
| 7.4.0 | O caminho de configuração padrão do OpenSSL foi alterado de C:\usr\local\ssl para C:\Program Files\Common Files\SSL e C:\Program Files (x86)\Common Files\SSL, respectivamente. |

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
