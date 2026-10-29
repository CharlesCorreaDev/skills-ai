# Função fictícia (Phar::setAlias ​​não é válido para PharData)

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.setalias.php

---

# PharData::setAlias

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::setAlias — Função fictícia (Phar::setAlias ​​não é válido para PharData)

### Descrição

public function **PharData::setAlias**([string](language.types.string.md) `$alias`): [bool](language.types.boolean.md)

Arquivos tar/zip não executáveis ​​não podem ter um apelido, então esse método simplesmente
gera uma exceção.

### Parâmetros

`alias`
:   Uma string abreviada à qual este arquivo pode ser referenciado no
    acesso ao empacotador de fluxo `phar`. Este parâmetro é ignorado.

### Valor Retornado

### Erros/Exceções

Lança [PharException](class.pharexception.md) em todas as chamadas do método.

### Veja também

- [Phar::setAlias()](phar.setalias.md) - Define o apelido para o arquivo Phar

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
