# Configurações de Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/openssl.configuration.php

---

## Configurações de Execução

O comportamento destas funções é afetado pelas configurações do php.ini.

**Opções de Configuração de openssl**

| Nome | Padrão | Modificável | Registro de Alterações |
| --- | --- | --- | --- |
| openssl.cafile | "" | **`INI_PERDIR`** |  |
| openssl.capath | "" | **`INI_PERDIR`** |  |
| openssl.libctx | "custom" | **`INI_PERDIR`** |  |

Para mais detalhes e definições dos modos
INI\_\*, consulte os [Onde uma configuração deve ser definida](configuration.changes.modes.md).

Aqui está uma breve explicação das
diretivas de configuração.

`openssl.cafile` [string](language.types.string.md)
:   Localização do arquivo da Autoridade de Certificação no sistema de arquivos local que deve
    ser usado com a opção de contexto verify\_peer para autenticar a
    identidade do peer remoto.

`openssl.capath` [string](language.types.string.md)
:   Se cafile não for especificado ou se o certificado não for encontrado lá, o
    diretório apontado por capath será pesquisado para um certificado adequado.
    capath deve ser um diretório de certificado com hash correto.

`openssl.libctx` [string](language.types.string.md)
:   Especifica o tipo de contexto de biblioteca OpenSSL a ser usado.
    O valor padrão, `custom`, cria um contexto
    de biblioteca separado para cada trabalhador ou thread.
    Isso melhora o isolamento em relação a outras bibliotecas que estejam usando OpenSSL e,
    em compilações ZTS, aumenta a separação entre threads.
    Também é possível usar o valor `default`, que
    faz com que o PHP use o contexto de biblioteca padrão global do OpenSSL.

Veja também as opções de [contexto de fluxo SSL](context.ssl.md).

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
