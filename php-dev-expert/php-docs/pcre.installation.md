# Instalação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pcre.installation.php

---

## Instalação

A extensão PCRE é uma extensão do núcleo do PHP, portanto está sempre habilitada.
Por padrão, esta extensão é compilada usando a biblioteca PCRE
incluída. Alternativamente, uma biblioteca PCRE externa pode ser usada passando
a opção de configuração **--with-pcre-regex=DIR**
onde `DIR` é a localização do
PCRE incluir e arquivos de biblioteca. Recomenda-se utilizar PCRE 8.10 ou mais recente;
a partir do PHP 7.3.0, o PCRE2 é necessário.

A compilação just-in-time do PCRE é suportada por padrão, e
pode ser desabilitada com a opção de configuração **--without-pcre-jit**
a partir do PHP 7.0.12.

A versão do PHP para Windows tem suporte
nativo para esta extensão. Nenhuma extensão adicional precisa ser carregada
para usar essas funções.

PCRE é um projeto ativo e, à medida que muda, também muda a
funcionalidade do PHP que depende dele. É possível que certas partes
da documentação do PHP estejam desatualizadas, pois podem não cobrir os
recursos mais recentes que o PCRE oferece. Para obter uma lista de alterações, consulte o
[» registro de alterações da biblioteca PCRE](https://www.pcre.org/original/changelog.txt)
e também o seguinte histórico do PCRE incluído:

**Histórico de atualização da biblioteca PCRE incluída**

| Versão do PHP | Versão da PCRE atualizada | Notas |
| --- | --- | --- |
| 8.2.0 | 10.40 |  |
| 8.1.0 | 10.39 |  |
| 7.4.12, 8.0.0 | 10.35 |  |
| 7.4.6 | 10.34 |  |
| 7.4.0 | 10.33 |  |
| 7.3.0 | 10.32 |  |
| 7.2.0 | 8.41 |  |
| 7.0.3 | 8.38 | Consulte: CVE-2015-8383, CVE-2015-8386, CVE-2015-8387, CVE-2015-8389, CVE-2015-8390, CVE-2015-8391, CVE-2015-8393, CVE-2015-8394 |
| 7.0.0 | 8.37 | Consulte: CVE-2015-2325, CVE-2015-2326 |

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
