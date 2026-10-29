# Retorna informações da versão do arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.getversion.php

---

# Phar::getVersion

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 1.0.0)

Phar::getVersion — Retorna informações da versão do arquivo Phar

### Descrição

public function **Phar::getVersion**(): [string](language.types.string.md)

Retorna a versão da API de um arquivo Phar aberto.

### Parâmetros

### Valor Retornado

A versão da API do arquivo aberto. Não deve ser confundida com
a versão da API que a extensão phar carregada usará para criar
novos phars. Cada arquivo Phar tem a versão da API codificada em
seu manifesto. Consulte a documentação do [formato de arquivo Phar](phar.fileformat.md)
para obter mais informações.

### Veja também

- [Phar::apiVersion()](phar.apiversion.md) - Retorna a versão da API

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
